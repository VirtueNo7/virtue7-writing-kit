#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def load(p): return yaml.safe_load((ROOT/p).read_text(encoding='utf-8'))
def main():
    failures=[]
    m=load('RUNTIME_MANIFEST.yaml')
    if m['bundle']['version']!='0.5.0': failures.append('Runtime bundle version is not 0.5.0.')
    for mid in ('chat','content','automation'):
        if mid not in m.get('modes',{}): failures.append(f'Missing mode: {mid}')
    if set(m.get('modes',{})) != {'chat','content','automation'}: failures.append('Public runtime must expose exactly Chat, Content, and Automation modes.')
    if len(m.get('capabilities',{})) != 9: failures.append(f"Expected 9 capabilities; found {len(m.get('capabilities',{}))}.")
    routes=sum(len(c.get('routes',{})) for c in m.get('capabilities',{}).values())
    if routes != 35: failures.append(f'Expected 35 routes; found {routes}.')
    pi=load('runtime/packet-index.yaml')
    if len(pi.get('routes',{})) != 35: failures.append('Compiled route packet count is not 35.')
    if len(pi.get('profiles',{})) != 24: failures.append('Compiled profile packet count is not 24.')
    forbidden=['agents','opportunities']
    for cap in forbidden:
        if cap in m.get('capabilities',{}): failures.append(f'Removed capability remains registered: {cap}')
    boot=sum((ROOT/f).stat().st_size for f in m['boot']['files'])
    if boot > m['boot'].get('maximum_bytes',13000): failures.append(f'Boot exceeds byte budget: {boot}.')
    if failures:
        print('Runtime validation failed:'); [print('- '+x) for x in failures]; return 1
    print(f'Runtime validation passed: 3 modes, 9 capabilities, 35 routes, 24 profiles; boot {boot} bytes.')
    return 0
if __name__=='__main__': raise SystemExit(main())
