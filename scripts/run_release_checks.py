#!/usr/bin/env python3
from pathlib import Path
import os, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
steps=[
 "build_profile_fixtures.py","build_playbook_index.py","build_runtime_packets.py","test_boot_contract.py","test_writing_contract.py","build_examples.py","build_whitepaper.py",
 "run_evaluation_suite.py","run_adversarial_suite.py","run_governance_suite.py","validate_contract_schemas.py","benchmark_runtime.py","build_validation_report.py",
 "validate_schema.py","validate_runtime.py","validate_playbook_library.py","validate_examples.py","validate_repository_files.py",
 "validate_whitepaper.py","build_file_manifest.py","verify_file_manifest.py","validate_bundle.py","test_release_reproducibility.py","create_release_zip.py"]
for name in steps:
 command=[sys.executable,f"scripts/{name}"]; print("\n$ "+" ".join(command),flush=True)
 result=subprocess.run(command,cwd=ROOT,env=os.environ.copy())
 if result.returncode: raise SystemExit(result.returncode)
 for cache in ROOT.rglob("__pycache__"): shutil.rmtree(cache,ignore_errors=True)
print("\nAll release checks passed.")
