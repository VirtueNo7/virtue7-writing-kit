#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or p.name=='FILE_MANIFEST.json' or '__pycache__' in p.parts or '.git' in p.parts or p.suffix=='.pyc': continue
        files.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)})
    data={'bundle':'Virtue7 Writing Kit','version':(ROOT/'VERSION').read_text().strip(),'files':files}
    (ROOT/'FILE_MANIFEST.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(f'Wrote {len(files)} records.')
if __name__=='__main__': main()
