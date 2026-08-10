#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, json, re, sys

SUPPORTED_PROFILES = {
    'children_picture_book', 'children_chapter_book', 'narrative_nonfiction', 'spoken_argument',
    'essay_article', 'research_paper', 'technical_manual', 'business_report',
    'workbook_guide', 'resume', 'cover_letter', 'legal_memorandum',
    'creator_episode', 'interview_dossier', 'clip_sheet', 'job_search_brief',
    'fiction_short_story', 'novel_chapter', 'brand_strategy', 'product_brief',
    'standard_operating_procedure', 'meeting_decision_record',
    'social_content_package', 'fact_check_report',
}

EVIDENCE_SENSITIVE_PROFILES = SUPPORTED_PROFILES - {'children_picture_book','children_chapter_book','workbook_guide','fiction_short_story','novel_chapter'}

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

def evidence_attested(context):
    r=context.get('evidence_attestation') if isinstance(context,dict) else None
    return bool(isinstance(r,dict) and r.get('status')=='reviewed' and r.get('scope') and r.get('reviewer_type') in {'human','test_fixture'} and r.get('reviewer_id') and r.get('source_ids'))

def analyse(profile: str, text: str, context=None):
    m=metrics(text); low=text.lower(); findings=[]
    def block(cond,msg):
        if cond: findings.append({'severity':'Block','message':msg})
    def req(cond,msg): block(not cond,msg)

    # universal semantic finish
    block(m['generic_hits_per_1000'] >= 8,
          'Generic abstraction density indicates polished but low-information prose.')

    if profile == 'children_picture_book':
        req(m['list_items']==0,'Narrative body must not use bullet or numbered lists.')
        req(m['heading_count']<=1,'Picture-book narrative has too many interior headings.')
        req(120 <= m['words'] <= 1200,'Length is outside the broad picture-book test range.')
        req(m['avg_sentence_words']<=20,'Sentence cadence may be too complex for read-aloud use.')
        lines=[p.strip() for p in text.split('\n') if 3<=len(p.strip())<=70]
        req(any(text.count(line)>=2 for line in lines),'No repeated refrain or participation cue detected.')

    elif profile == 'children_chapter_book':
        req(m['list_items']==0,'Chapter-book narrative must not use body lists.')
        req(m['heading_count']<=3,'Chapter-book sample has excessive interior headings.')
        req(m['paragraphs']>=4,'Chapter-book sample needs developed scenes and paragraphs.')
        req(m['words']>=250,'Chapter-book sample is too short to demonstrate narrative movement.')

    elif profile == 'narrative_nonfiction':
        req(m['list_items']<=2,'Narrative nonfiction has excessive body-list drift.')
        req(m['heading_count']<=5,'Narrative nonfiction is over-sectioned.')
        req(m['paragraphs']>=5,'Narrative nonfiction needs developed paragraph movement.')
        req(any(x in low for x in ['source','record','evidence','according to']), 'Evidence boundary is not visible.')
        req(any(x in low for x in ['suggests','however','cannot','uncertain','limitation']), 'Interpretive limits are not visible.')

    elif profile == 'spoken_argument':
        req(m['list_items']==0,'Spoken argument must remain continuous prose unless lists are explicitly requested.')
        req(m['heading_count']<=1,'Spoken argument should have no interior headings unless the supplied form requires them.')
        req(m['paragraphs']>=6,'Spoken argument needs developed paragraph movement.')
        block(m['short_paragraph_ratio']>=0.5 and m['paragraphs']>=6,'Fragment stacks or slogan chains indicate Narrative Lock drift.')
        req(any(x in low for x in ['evidence','record','timeline','fact','according to','source']), 'Evidence boundary is not visible.')
        req(any(x in low for x in ['however','but','to be clear','does not mean','cannot','qualification','counterpoint']), 'Counterargument or qualification is not visible.')

    elif profile == 'technical_manual':
        req(m['heading_count']>=2,'Technical guidance needs navigational headings.')
        req(m['list_items']>=3,'Technical guidance needs visible rules or ordered steps.')
        req(any(v in low for v in ['use ','keep ','avoid ','confirm ','test ','group ','select ','open ']),'Direct action language is weak.')
        req(m['max_sentence_words']<=45,'At least one sentence is too dense for procedural guidance.')

    elif profile == 'business_report':
        for h in ['executive summary','findings','implications','recommendation']:
            req(any(h in x.lower() for x in m['headings']),f'Missing business-report section: {h}.')
        req(any(x in low for x in ['evidence','source','data']), 'Business report does not expose its evidence basis.')
        req(any(x in low for x in ['recommend','decision','next step']), 'Business report lacks a decision-ready recommendation.')

    elif profile == 'workbook_guide':
        req(m['heading_count']>=3,'Workbook needs navigational headings.')
        req(m['list_items']>=3,'Workbook needs usable exercises or steps.')
        req(any(x in low for x in ['exercise','practice','activity']), 'Workbook has no exercise or practice activity.')
        req(any(x in low for x in ['completion check','check your work','success check']), 'Workbook lacks a completion check.')

    elif profile in {'fiction_short_story', 'novel_chapter'}:
        req(m['list_items']==0,'Narrative Lock prohibits bullet or numbered lists in the story body.')
        req(m['heading_count']<=1,'Narrative body has unrequested interior headings.')
        req(m['paragraphs']>=3,'Narrative movement needs developed paragraphs.')
        block(m['short_paragraph_ratio']>=0.65 and m['paragraphs']>=4,'Fragment stacks indicate narrative Form Lock drift.')

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

    elif profile == 'cover_letter':
        req(m['list_items']==0,'Cover letter should use developed paragraphs rather than lists.')
        req(3<=m['paragraphs']<=7,'Cover letter should contain three to seven developed paragraphs.')
        req(any(x in low for x in ['experience','delivered','led','built','improved','supported']), 'Cover letter lacks a concrete evidence example.')
        req(any(x in low for x in ['role','position','team','organisation','organization']), 'Target role or organization is not visible.')

    elif profile == 'job_search_brief':
        req(m['heading_count']>=4,'Job brief lacks navigable role grouping.')
        req(m['list_items']>=8,'Job brief lacks structured decision fields.')
        for field in ['match rationale','verification needed','recommended action']:
            req(field in low,f'Missing decision field: {field}.')
        req('next step' in low,'No controlled handoff is present.')

    elif profile == 'creator_episode':
        for h in ['hook','central question','development','conclusion','next action']:
            req(any(h in x.lower() for x in m['headings']),f'Missing creator-episode section: {h}.')
        req(any(x in low for x in ['source','evidence','story']), 'Episode lacks an evidence or story beat.')

    elif profile == 'interview_dossier':
        for h in ['background','chronology','themes','verified claims','open questions','question arcs','risks']:
            req(any(h in x.lower() for x in m['headings']),f'Missing interview-dossier section: {h}.')
        req(m['list_items']>=5,'Interview dossier lacks scannable questions or evidence records.')

    elif profile == 'clip_sheet':
        for field in ['hook','context','in point','out point','title options','destination','rights']:
            req(field in low,f'Missing clip-sheet field: {field}.')
        req(bool(re.search(r'\b\d{1,2}:\d{2}(?::\d{2})?\b', text)), 'Clip sheet lacks a visible timecode.')
        req(m['list_items']>=4 or '|' in text,'Clip sheet needs repeated records or a table.')

    elif profile == 'standard_operating_procedure':
        for h in ['purpose','scope','roles','procedure','exceptions','controls','records','escalation','review']:
            req(any(h in x.lower() for x in m['headings']),f'Missing SOP section: {h}.')
        req(m['list_items']>=6,'SOP needs ordered or scannable operational steps.')
        req(any(x in low for x in ['owner','responsible','accountable']), 'SOP ownership is not explicit.')
        req(any(x in low for x in ['evidence of completion','completion record','record of completion']), 'Proof of completion is not defined.')

    elif profile == 'product_brief':
        for h in ['problem','evidence','users','requirements','non-goals','risks','success','open questions']:
            req(any(h in x.lower() for x in m['headings']),f'Missing product brief section: {h}.')
        req(any(x in low for x in ['acceptance criteria','must ','shall ']), 'Requirements are not visibly testable.')

    elif profile == 'brand_strategy':
        for h in ['audience','problem','promise','proof','difference','boundaries','open questions']:
            req(any(h in x.lower() for x in m['headings']),f'Missing brand strategy section: {h}.')
        req(any(x in low for x in ['evidence','source','supported']), 'Brand proof boundary is weak.')

    elif profile == 'meeting_decision_record':
        for h in ['context','decisions','rationale','actions','owners','due dates','dependencies','unresolved questions']:
            req(any(h in x.lower() for x in m['headings']),f'Missing decision-record section: {h}.')
        req(m['list_items']>=4,'Decision record lacks scannable actions and ownership.')

    elif profile == 'fact_check_report':
        for h in ['question','methodology','findings','claim statuses','contradictions','limitations','conclusion','sources']:
            req(any(h in x.lower() for x in m['headings']),f'Missing fact-check section: {h}.')
        req(any(x in low for x in ['verified fact','credible report','interpretation','allegation','theory','unknown']), 'Claim classification is absent.')
        req(len(re.findall(r'\b(?:19|20)\d{2}\b', text))>=2,'Source dating is insufficient.')


    elif profile == 'social_content_package':
        for h in ['source kernel','titles','description','channel assets','calls to action','release checklist']:
            req(any(h in x.lower() for x in m['headings']),f'Missing release-package section: {h}.')
        req(m['list_items']>=5,'Release package lacks usable asset options or checks.')

    else:
        findings.append({'severity':'Block','message':f'Unknown profile: {profile}'})

    if profile in EVIDENCE_SENSITIVE_PROFILES and not evidence_attested(context): findings.append({'severity':'Block','message':'Evidence-sensitive profiles require a reviewed evidence attestation; structural conformance alone cannot pass.'})
    return {'status':'Block' if findings else 'Pass','profile':profile,'metrics':m,'assurance':'evidence_attested' if evidence_attested(context) else 'structural_only','findings':findings}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path',type=Path); ap.add_argument('--profile',required=True); ap.add_argument('--context',type=Path); ap.add_argument('--json',action='store_true'); ap.add_argument('--expect',choices=['Pass','Block'])
    a=ap.parse_args(); context=json.loads(a.context.read_text(encoding='utf-8')) if a.context else None; result=analyse(a.profile,a.path.read_text(encoding='utf-8'),context)
    print(json.dumps(result,indent=2) if a.json else f"{a.path.name}: {result['status']} ({a.profile})\n"+'\n'.join('- '+x['message'] for x in result['findings']))
    if a.expect and result['status']!=a.expect: return 2
    return 0 if result['status']=='Pass' else 1
if __name__=='__main__': raise SystemExit(main())
