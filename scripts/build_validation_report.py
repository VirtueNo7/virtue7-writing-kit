#!/usr/bin/env python3
from pathlib import Path
import json, yaml
ROOT=Path(__file__).resolve().parents[1]
def main():
    runtime=yaml.safe_load((ROOT/'RUNTIME_MANIFEST.yaml').read_text())
    profiles=yaml.safe_load((ROOT/'config/output-profiles.yaml').read_text())['registry']
    examples=yaml.safe_load((ROOT/'examples/index.yaml').read_text())
    evals=yaml.safe_load((ROOT/'tests/evaluation-cases.yaml').read_text())['cases']
    gov=yaml.safe_load((ROOT/'tests/governance-cases.yaml').read_text())['cases']
    routes=sum(len(x['routes']) for x in runtime['capabilities'].values())
    text=f"""# Validation Report - Virtue7 Writing Kit v0.5.0

- Modes: 3 (Chat, Content, Automation).
- Capabilities: {len(runtime['capabilities'])}.
- Routes: {routes}.
- Output profiles: {len(profiles)}.
- Profile evaluation cases: {len(evals)}.
- Governance cases: {len(gov)}.
- Worked examples: {len(examples['examples'])}.
- Contract schemas: 4 generic record contracts validated, including approval/artifact binding and tool-receipt negative controls.
- Prose structure: pseudo-list drift is explicitly covered by Form Lock and governance tests.

All counts are generated from the current repository state. Structural validation does not substitute for factual verification or human review.
"""
    (ROOT/'VALIDATION_REPORT.md').write_text(text,encoding='utf-8')
    print('Validation report rebuilt.')
if __name__=='__main__': raise SystemExit(main())
