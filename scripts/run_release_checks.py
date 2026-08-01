#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,shutil,os
ROOT=Path(__file__).resolve().parents[1]
for cache in ROOT.rglob('__pycache__'):
    shutil.rmtree(cache, ignore_errors=True)
os.environ['PYTHONDONTWRITEBYTECODE']='1'
steps=[['python','scripts/run_evaluation_suite.py'],['python','scripts/validate_runtime.py'],['python','scripts/build_file_manifest.py'],['python','scripts/validate_bundle.py'],['python','scripts/create_release_zip.py']]
for step in steps:
    print('\n$ '+' '.join(step)); r=subprocess.run(step,cwd=ROOT,env=os.environ.copy())
    if r.returncode: raise SystemExit(r.returncode)
print('\nAll release checks passed.')
