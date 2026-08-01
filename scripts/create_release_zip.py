#!/usr/bin/env python3
from pathlib import Path
import zipfile,sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/f'{ROOT.name}.zip'
EXCLUDE={'__pycache__','.DS_Store'}
def main():
    if OUT.exists(): OUT.unlink()
    with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if not p.is_file() or any(x in EXCLUDE or x.startswith('._') for x in p.parts) or p.suffix=='.pyc': continue
            z.write(p,Path(ROOT.name)/p.relative_to(ROOT))
    with zipfile.ZipFile(OUT) as z:
        bad=[n for n in z.namelist() if '__MACOSX' in n or '/._' in n or n.endswith('.DS_Store')]
        roots={n.split('/')[0] for n in z.namelist() if n}
        if bad or roots!={ROOT.name}: print('ZIP verification failed',bad,roots); return 1
    print(OUT)
    return 0
if __name__=='__main__': raise SystemExit(main())
