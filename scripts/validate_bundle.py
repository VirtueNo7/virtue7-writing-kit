#!/usr/bin/env python3
"""Validate required files, version consistency, manifests, and boundary markers."""
from pathlib import Path
import hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

REQUIRED = [
    "00_START_HERE.md", "MASTER_PROMPT.md", "BUNDLE_MANIFEST.yaml", "README.md",
    "config/kit.yaml", "config/reference-policy.yaml", "config/voice-policy.yaml",
    "architecture/01-content-system.md", "architecture/08-reference-grounding.md",
    "architecture/09-voice-governance.md", "workflows/01-new-book.md",
    "workflows/02-master-builder-demo.md", "workflows/07-build-reference-library.md",
    "workflows/08-build-voice-contract.md", "workflows/09-run-drift-test.md",
    "templates/reference-register.md", "templates/voice-contract.md",
    "templates/reference-packet.md", "templates/passage-provenance.md",
    "templates/drift-report.md", "demo/master-builder/subject-profile.yaml",
    "docs/whitepaper/compressible-content-architecture_whitepaper.pdf",
    "docs/whitepaper/compressible-content-architecture_ai-readable.txt",
]

MARKERS = {
    "00_START_HERE.md": ["generated books are white-label by default", "do not infer any details about the person who uploaded the archive", "reference-grounded writing"],
    "MASTER_PROMPT.md": ["C = (K, U, E, R, V, P, Q)", "project-native voice canon"],
    "demo/master-builder/00_START_TEST.md": ["fictional", "without external research"],
}

def main() -> int:
    failures=[]
    for rel in REQUIRED:
        if not (ROOT/rel).exists(): failures.append(f"Missing required file: {rel}")
    for rel, markers in MARKERS.items():
        p=ROOT/rel
        if not p.exists(): continue
        text=p.read_text(encoding="utf-8",errors="replace").lower()
        for marker in markers:
            if marker.lower() not in text: failures.append(f"Missing boundary marker in {rel}: {marker}")
    for rel in ["README.md","BUNDLE_MANIFEST.yaml","config/kit.yaml"]:
        p=ROOT/rel
        if p.exists() and VERSION not in p.read_text(encoding="utf-8",errors="replace"):
            failures.append(f"Version {VERSION} not found in {rel}")
    if failures:
        print("Bundle validation failed:")
        for f in failures: print(f"- {f}")
        return 1
    print("Bundle validation passed.")
    print(f"Version: {VERSION}")
    print(f"Root: {ROOT}")
    print(f"Files: {sum(1 for p in ROOT.rglob('*') if p.is_file())}")
    return 0
if __name__ == "__main__": raise SystemExit(main())
