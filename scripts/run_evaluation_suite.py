#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
from check_output_profile import analyse
ROOT=Path(__file__).resolve().parents[1]
FIXTURE_CONTEXT={'evidence_attestation':{'status':'reviewed','scope':'synthetic_test_fixture','reviewer_type':'test_fixture','reviewer_id':'release-suite','source_ids':['FIXTURE-INPUT']}}

def main():
    spec=yaml.safe_load((ROOT/'tests/evaluation-cases.yaml').read_text(encoding='utf-8'))
    results=[]; failures=[]
    for case in spec['cases']:
        fixture_dir=spec.get('fixture_directory','tests/fixtures')
        p=ROOT/fixture_dir/case['file']
        result=analyse(case['profile'],p.read_text(encoding='utf-8'),case.get('context',FIXTURE_CONTEXT))
        ok=result['status']==case['expect']
        results.append({'file':case['file'],'profile':case['profile'],'expected':case['expect'],'actual':result['status'],'assurance':result['assurance'],'ok':ok,'findings':result['findings']})
        if not ok: failures.append(case['file'])
    out=ROOT/'tests/LATEST_RESULTS.json'; out.write_text(json.dumps(results,indent=2),encoding='utf-8')
    print(f"Evaluation: {len(results)-len(failures)}/{len(results)} matched expected outcomes.")
    for r in results: print(f"- {'PASS' if r['ok'] else 'FAIL'} {r['file']}: expected {r['expected']}, got {r['actual']}")
    return 1 if failures else 0
if __name__=='__main__': raise SystemExit(main())
