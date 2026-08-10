#!/usr/bin/env python3
from pathlib import Path
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs/whitepaper'; SOURCE=DOCS/'virtue7_whitepaper.md'; TEXT=DOCS/'virtue7_ai-readable.txt'; PDF=DOCS/'virtue7_whitepaper.pdf'
TOKENS=['Virtue7: A Lightweight Governed Runtime for AI Work','Chat | Create Content | Automate a Task','task = bounded work with a terminal state','Minimum-Sufficient Runtime','C = (K, U, E, P, Q)','Bounded Automation','Controlled Improvement','Conclusion']
def main():
    failures=[]
    for p in [SOURCE,TEXT,PDF]:
        if not p.exists() or p.stat().st_size==0: failures.append(f'Missing or empty whitepaper artifact: {p.name}')
    if failures: print('Whitepaper validation failed:'); [print('- '+x) for x in failures]; return 1
    source=SOURCE.read_text(encoding='utf-8'); accessible=TEXT.read_text(encoding='utf-8')
    if accessible.strip()!=source.strip(): failures.append('AI-readable text does not match canonical Markdown source.')
    for t in TOKENS:
        if t not in source: failures.append(f'Canonical source missing token: {t}')
    for t in ['Build an Agent','Agent Commons','Agent Foundry','Find a ' + 'boun' + 'ty','Opportunity Engine']:
        if t.lower() in source.lower(): failures.append(f'Whitepaper still contains removed subsystem: {t}')
    reader=PdfReader(str(PDF)); extracted='\n'.join((p.extract_text() or '') for p in reader.pages)
    if not (4 <= len(reader.pages) <= 10): failures.append(f'Whitepaper should remain compact (4-10 pages); found {len(reader.pages)} pages')
    for t in ['Lightweight Governed Runtime','Three Operating Modes','Bounded Automation','Controlled Improvement','Conclusion']:
        if t not in extracted: failures.append(f'PDF text missing token: {t}')
    if failures: print('Whitepaper validation failed:'); [print('- '+x) for x in failures]; return 1
    print(f'Whitepaper validation passed: {len(reader.pages)} pages, {PDF.stat().st_size} bytes.'); return 0
if __name__=='__main__': raise SystemExit(main())
