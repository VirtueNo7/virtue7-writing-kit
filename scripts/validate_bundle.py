#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
 '00_START_HERE.md','RUNTIME_MANIFEST.yaml','MASTER_PROMPT.md','VERSION','README.md','LICENSE',
 'config/form-lock.yaml','config/output-profiles.yaml','config/taxonomy.yaml','config/gates.yaml',
 'schemas/artifact-record.schema.json','schemas/approval-record.schema.json','schemas/tool-receipt.schema.json','schemas/extension-manifest.schema.json',
 'docs/whitepaper/virtue7_whitepaper.md','docs/whitepaper/virtue7_ai-readable.txt','docs/whitepaper/virtue7_whitepaper.pdf'
]
FORBIDDEN_PATHS=['capabilities/agents','capabilities/opportunities','config/agents.yaml','library/agent-packs','runtime/agent_foundry.py','runtime/agent_commons.py','runtime/opportunity_engine.py','docs/agent-foundry.md','docs/agent-commons.md','docs/opportunity-engine.md']
FORBIDDEN_TEXT=['Build an agent','Find a ' + 'boun' + 'ty','Agent Foundry','Agent Commons','Opportunity Engine']
def main():
    failures=[]
    for rel in REQUIRED:
        if not (ROOT/rel).exists(): failures.append(f'Missing required file: {rel}')
    for rel in FORBIDDEN_PATHS:
        if (ROOT/rel).exists(): failures.append(f'Removed subsystem still present: {rel}')
    runtime=yaml.safe_load((ROOT/'RUNTIME_MANIFEST.yaml').read_text())
    if len(runtime.get('capabilities',{}))!=9: failures.append('Bundle must ship 9 capabilities.')
    if sum(len(c['routes']) for c in runtime['capabilities'].values())!=35: failures.append('Bundle must ship 35 routes.')
    if len(yaml.safe_load((ROOT/'config/output-profiles.yaml').read_text())['registry'])!=24: failures.append('Bundle must ship 24 profiles.')
    # User-facing/runtime control surfaces must not advertise removed subsystems.
    for rel in ['00_START_HERE.md','MASTER_PROMPT.md','README.md','RUNTIME_MANIFEST.yaml','BUNDLE_MANIFEST.yaml','docs/architecture.md','docs/whitepaper/virtue7_whitepaper.md']:
        text=(ROOT/rel).read_text(encoding='utf-8')
        for token in FORBIDDEN_TEXT:
            if token.lower() in text.lower(): failures.append(f'{rel} still advertises removed subsystem: {token}')
    if failures:
        print('Bundle validation failed:'); [print('- '+x) for x in failures]; return 1
    print('Bundle validation passed: writing-focused public release boundary is clean.')
    return 0
if __name__=='__main__': raise SystemExit(main())
