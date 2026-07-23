#!/usr/bin/env python3
"""Validate required files and obvious white-label boundary violations."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "00_START_HERE.md",
    "MASTER_PROMPT.md",
    "BUNDLE_MANIFEST.yaml",
    "config/kit.yaml",
    "architecture/01-content-system.md",
    "workflows/01-new-book.md",
    "workflows/02-master-builder-demo.md",
    "demo/master-builder/subject-profile.yaml",
    "docs/whitepaper/compressible-content-architecture_whitepaper.pdf",
    "docs/whitepaper/compressible-content-architecture_ai-readable.txt",
]

TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".json", ".py"}

REQUIRED_MARKERS = {
    "00_START_HERE.md": ["generated books are white-label by default", "do not infer any details about the person who uploaded the archive"],
    "demo/master-builder/00_START_TEST.md": ["fictional", "without external research"],
}


def main() -> int:
    failures = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            failures.append(f"Missing required file: {rel}")

    for rel, markers in REQUIRED_MARKERS.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        for marker in markers:
            if marker.lower() not in text:
                failures.append(f"Missing required boundary marker in {rel}: {marker}")

    if failures:
        print("Bundle validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Bundle validation passed.")
    print(f"Root: {ROOT}")
    print(f"Files: {sum(1 for p in ROOT.rglob('*') if p.is_file())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
