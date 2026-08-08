#!/usr/bin/env python3
from pathlib import Path
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
for cache in ROOT.rglob("__pycache__"):
    shutil.rmtree(cache, ignore_errors=True)
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

steps = [
    ["python", "scripts/run_evaluation_suite.py"],
    ["python", "scripts/validate_runtime.py"],
    ["python", "scripts/validate_playbook_library.py"],
    ["python", "scripts/validate_whitepaper.py"],
    ["python", "scripts/build_file_manifest.py"],
    ["python", "scripts/validate_bundle.py"],
    ["python", "scripts/create_release_zip.py"],
]
for step in steps:
    print("\n$ " + " ".join(step))
    result = subprocess.run(step, cwd=ROOT, env=os.environ.copy())
    if result.returncode:
        raise SystemExit(result.returncode)
    for cache in ROOT.rglob("__pycache__"):
        shutil.rmtree(cache, ignore_errors=True)
print("\nAll release checks passed.")
