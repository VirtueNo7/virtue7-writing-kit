#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, json, re, sys

GENERIC_PHRASES = [
    'transformative landscape','living tapestry','brighter horizon','unlock potential',
    'gateway to renewal','profound testament','evolving paradigm','authentic responsiveness',
    'limitation into opportunity','holistic reimagining','shared vision','latent potential',
    'dynamic collaboration','journey toward','catalyst for change','human spirit'
]

def strip_md(text: str) -> str:
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.M)
    text = re.sub(r'^\s*(?:[-*+] |\d+[.)]\s+)', '', text, flags=re.M)
    return text

def metrics(text: str):
    headings = re.findall(r'^#{2,6}\s+(.+)$', text, flags=re.M)
    lists = re.findall(r'^\s*(?:[-*+] |\d+[.)]\s+)', text, flags=re.M)
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip() and not p.lstrip().startswith('#')]
    plain = strip_md(text)
    words = re.findall(r"\b[\w’'-]+\b", plain)
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', plain) if re.search(r'\w', s)]
    lens = [len(re.findall(r"\b[\w’'-]+\b", s)) for s in sents]
    short_paras = sum(len(re.findall(r'\w+', p)) <= 8 for p in paras)
    generic_hits = sum(plain.lower().count(x) for x in GENERIC_PHRASES)
    return {
        'words': len(words), 'headings': headings, 'heading_count': len(headings),
        'list_items': len(lists), 'paragraphs': len(paras),
        'short_paragraph_ratio': round(short_paras/max(len(paras),1),3),
        'avg_sentence_words': round(sum(lens)/max(len(lens),1),1),
        'max_sentence_words': max(lens or [0]), 'generic_phrase_hits': generic_hits,
        'generic_hits_per_1000': round(generic_hits/max(len(words),1)*1000,2)
    }

def analyse(profile: str, text: str):
    m=metrics(text); low=text.lower(); findings=[]
    def block(cond,msg):
        if cond: findings.append({'severity':'Block','message':msg})
    def req(cond,msg): block(not cond,msg)

    # universal semantic finish
    block(m['generic_phrase_hits'] >= 4 or m['generic_hits_per_1000'] >= 7,
          'Generic abstraction density indicates polished but low-information prose.')

    if profile == 'children_picture_book':
        req(m['list_items']==0,'Narrative body must not use bullet or numbered lists.')
        req(m['heading_count']<=1,'Picture-book narrative has too many interior headings.')
        req(120 <= m['words'] <= 1200,'Length is outside the broad picture-book test range.')
        req(m['avg_sentence_words']<=20,'Sentence cadence may be too complex for read-aloud use.')
        lines=[p.strip() for p in text.split('\n') if 3<=len(p.strip())<=70]
        req(any(text.count(line)>=2 for line in lines),'No repeated refrain or participation cue detected.')

    elif profile == 'technical_manual':
        req(m['heading_count']>=2,'Technical guidance needs navigational headings.')
        req(m['list_items']>=3,'Technical guidance needs visible rules or ordered steps.')
        req(any(v in low for v in ['use ','keep ','avoid ','confirm ','test ','group ','select ','open ']),'Direct action language is weak.')
        req(m['max_sentence_words']<=45,'At least one sentence is too dense for procedural guidance.')

    elif profile == 'essay_article':
        req(m['list_items']==0,'Essay or strategic narrative should remain continuous prose.')
        req(m['heading_count']<=1,'Essay is over-sectioned.')
        req(m['paragraphs']>=5,'Argument needs developed paragraph movement.')
        block(m['short_paragraph_ratio']>=0.65 and m['heading_count']>=3,'Visible outline scaffolding dominates the prose.')
        concrete = len(re.findall(r'\b(?:19|20)\d{2}\b', text)) + len(re.findall(r'\b\d+\b', text))
        req(concrete>=2,'The essay lacks concrete anchors or specific evidence.')

    elif profile == 'research_paper':
        required_groups=[['abstract'],['background','literature'],['evidence','results'],['interpretation','discussion'],['conclusion'],['references']]
        for group in required_groups: req(any(any(x in h.lower() for x in group) for h in m['headings']),f"Missing research section: {'/'.join(group)}.")
        req(len(re.findall(r'\b(?:19|20)\d{2}\b', text))>=3,'Insufficient visible source dating.')
        req(any(x in low for x in ['suggests','does not','depends','however','limitation','cannot']), 'Research uncertainty or limitation language is weak.')
        req(any(x in low for x in ['references','source']), 'Visible source section or source language is missing.')

    elif profile == 'legal_memorandum':
        for h in ['issue','brief answer','analysis','conclusion']:
            req(any(h == x.lower().strip() for x in m['headings']),f'Missing legal memorandum section: {h}.')
        req(any(x in low for x in ['california','texas','new york','australia','england','canada','jurisdiction']), 'Jurisdiction is not explicit.')
        req(bool(re.search(r'\b(?:section|§|article|rule|code|act)\b', low)), 'Controlling authority is not identified.')
        req(any(x in low for x in ['assuming','assumed','cannot be determined','depends','if the facts']), 'Fact or uncertainty boundary is weak.')
        req('not a substitute' in low or 'not legal advice' in low or 'informational' in low, 'Informational status is not stated.')

    elif profile == 'resume':
        for h in ['professional summary','core skills','professional experience','education']:
            req(any(h in x.lower() for x in m['headings']),f'Missing resume section: {h}.')
        req(m['list_items']>=8,'Resume lacks scannable evidence bullets.')
        req(bool(re.search(r'\b\d+(?:\s|\s?percent|%)', low)), 'No quantified achievement detected in this test fixture.')
        block(bool(re.search(r'\b(i|me|my)\b', low)),'First-person resume phrasing detected.')

    elif profile == 'job_search_brief':
        req(m['heading_count']>=4,'Job brief lacks navigable role grouping.')
        req(m['list_items']>=8,'Job brief lacks structured decision fields.')
        for field in ['match rationale','verification needed','recommended action']:
            req(field in low,f'Missing decision field: {field}.')
        req('next step' in low,'No controlled handoff is present.')

    else:
        findings.append({'severity':'Block','message':f'Unknown profile: {profile}'})

    return {'status':'Block' if findings else 'Pass','profile':profile,'metrics':m,'findings':findings}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path',type=Path); ap.add_argument('--profile',required=True); ap.add_argument('--json',action='store_true'); ap.add_argument('--expect',choices=['Pass','Block'])
    a=ap.parse_args(); result=analyse(a.profile,a.path.read_text(encoding='utf-8'))
    print(json.dumps(result,indent=2) if a.json else f"{a.path.name}: {result['status']} ({a.profile})\n"+'\n'.join('- '+x['message'] for x in result['findings']))
    if a.expect and result['status']!=a.expect: return 2
    return 0 if result['status']=='Pass' else 1
if __name__=='__main__': raise SystemExit(main())
