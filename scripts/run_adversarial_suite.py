#!/usr/bin/env python3
from pathlib import Path
import yaml

from check_output_profile import analyse

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    spec = yaml.safe_load((ROOT / "tests/adversarial-output-cases.yaml").read_text(encoding="utf-8"))
    failures = []
    for case in spec["cases"]:
        path = ROOT / spec["fixture_directory"] / case["file"]
        result = analyse(case["profile"], path.read_text(encoding="utf-8"))
        ok = result["status"] == case["expect"]
        print(f"- {'PASS' if ok else 'FAIL'} {case['file']}: expected {case['expect']}, got {result['status']}")
        if not ok:
            failures.append(case["file"])
    if failures:
        print(f"Adversarial evaluation failed: {len(failures)} cases escaped release-grade blocking.")
        return 1
    print(f"Adversarial evaluation passed: {len(spec['cases'])} semantically unsafe artifacts denied release-grade Pass without evidence context.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
