#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
MAX_BOOT_BYTES=16000
MAX_CAP_MANIFEST_BYTES=5000

def main():
    failures=[]; m=yaml.safe_load((ROOT/'RUNTIME_MANIFEST.yaml').read_text(encoding='utf-8'))
    boot=m['boot']['files']
    if len(boot)!=3: failures.append(f'Boot must contain exactly 3 files; found {len(boot)}.')
    for rel in boot:
        if not (ROOT/rel).exists(): failures.append(f'Missing boot file: {rel}')
    if sum((ROOT/x).stat().st_size for x in boot if (ROOT/x).exists())>MAX_BOOT_BYTES: failures.append('Boot packet exceeds 16,000 bytes.')
    for cid,spec in m['capabilities'].items():
        p=ROOT/spec['manifest']
        if not p.exists(): failures.append(f'Missing capability manifest: {p.relative_to(ROOT)}'); continue
        if p.stat().st_size>MAX_CAP_MANIFEST_BYTES: failures.append(f'Capability manifest too large: {p.relative_to(ROOT)}')
        cm=yaml.safe_load(p.read_text(encoding='utf-8'))
        cap=ROOT/cm['capability']
        if not cap.exists(): failures.append(f'Missing capability file: {cm["capability"]}')
        for rid,rs in cm['routes'].items():
            rp=ROOT/rs['file']
            if not rp.exists(): failures.append(f'Missing route: {rs["file"]}')
    if failures:
        print('Runtime validation failed:'); [print('- '+x) for x in failures]; return 1
    print('Runtime validation passed.')
    print(f'Boot: 3 files, {sum((ROOT/x).stat().st_size for x in boot)} bytes')
    print(f'Capabilities: {len(m["capabilities"])}')
    return 0
if __name__=='__main__': raise SystemExit(main())
