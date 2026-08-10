#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib, zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT_DIR=ROOT.parent
EXCLUDE={"__pycache__",".DS_Store",".git"}
FIXED_TIMESTAMP=(2020,1,1,0,0,0)
def included(path:Path)->bool:
    return path.is_file() and not any(part in EXCLUDE or part.startswith("._") for part in path.parts) and path.suffix != ".pyc"
def digest(path:Path)->str: return hashlib.sha256(path.read_bytes()).hexdigest()
def write_archive(root:Path,out_dir:Path)->Path:
    version=(root/'VERSION').read_text(encoding='utf-8').strip()
    release_root=f'virtue7-writing-kit_v{version}'
    output=out_dir/f'{release_root}.zip'; output.parent.mkdir(parents=True,exist_ok=True)
    files=[p for p in sorted(root.rglob('*'),key=lambda p:p.relative_to(root).as_posix()) if included(p)]
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in files:
            info=zipfile.ZipInfo((Path(release_root)/path.relative_to(root)).as_posix(),date_time=FIXED_TIMESTAMP)
            info.compress_type=zipfile.ZIP_DEFLATED; info.create_system=3; info.external_attr=0o100644<<16; info.flag_bits=0x800
            archive.writestr(info,path.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        names=archive.namelist(); roots={n.split('/')[0] for n in names if n}
        bad=[n for n in names if '__MACOSX' in n or '/._' in n or n.endswith('.DS_Store') or '/.git/' in n]
        if bad or roots!={release_root} or names!=sorted(names): raise ValueError(f'ZIP verification failed: bad={bad}, roots={roots}')
        for info,source in zip(archive.infolist(),files,strict=True):
            if info.date_time!=FIXED_TIMESTAMP or (info.external_attr>>16)!=0o100644 or archive.read(info)!=source.read_bytes():
                raise ValueError(f'Non-deterministic metadata/content mismatch: {info.filename}')
    checksum=digest(output); output.with_suffix('.zip.sha256').write_text(f'{checksum}  {output.name}\n',encoding='utf-8')
    print(f'{output} ({len(files)} files; {checksum})'); return output
def build_all(root:Path=ROOT,out_dir:Path=OUT_DIR)->list[Path]: return [write_archive(root,out_dir)]
def main()->int: build_all(); return 0
if __name__=='__main__': raise SystemExit(main())
