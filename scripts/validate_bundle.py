#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
MAX_FILES = 280
MAX_BYTES = 5_000_000
REQUIRED = [
    "00_START_HERE.md",
    "MASTER_PROMPT.md",
    "RUNTIME_MANIFEST.yaml",
    "README.md",
    "VERSION",
    "LICENSE",
    f"RELEASE_NOTES-v{VERSION}.md",
    "FILE_MANIFEST.json",
    "config/output-profiles.yaml",
    "config/form-lock.yaml",
    "capabilities/personalization/manifest.yaml",
    "library/manifest.yaml",
    "examples/README.md",
    "docs/whitepaper/compressible-content-architecture_whitepaper.md",
    "docs/whitepaper/compressible-content-architecture_whitepaper.pdf",
]
FORBIDDEN_NAMES = {"__MACOSX", ".DS_Store", "__pycache__", ".git"}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt", ".py"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            failures.append(f"Missing required file: {rel}")

    all_files = [
        p for p in ROOT.rglob("*")
        if p.is_file()
        and p.name != "FILE_MANIFEST.json"
        and "__pycache__" not in p.parts
        and ".git" not in p.parts
        and p.suffix != ".pyc"
    ]
    for path in ROOT.rglob("*"):
        if any(part in FORBIDDEN_NAMES or part.startswith("._") for part in path.parts):
            if ".git" not in path.parts:
                failures.append(f"Forbidden metadata path: {path.relative_to(ROOT).as_posix()}")

    if len(all_files) > MAX_FILES:
        failures.append(f"File limit exceeded: {len(all_files)} > {MAX_FILES}")
    size = sum(path.stat().st_size for path in all_files)
    if size > MAX_BYTES:
        failures.append(f"Size limit exceeded: {size} > {MAX_BYTES}")

    identity_path_markers = ["public-baseline", "creator-profile/properties", "creator-profile/team"]
    unsafe_patterns = [
        r"(?i)in the style of\s+[A-Z]",
        r"(?i)write like\s+[A-Z]",
        r"(?i)sound like\s+[A-Z]",
        r"(?im)^creator_name:\s*(?![\[<{])\S+",
        r"(?im)^(?:client|organization)_name:\s*(?![\[<{])\S+",
    ]
    for path in all_files:
        rel = path.relative_to(ROOT).as_posix()
        low_rel = rel.lower()
        if any(marker in low_rel for marker in identity_path_markers):
            failures.append(f"Person-specific identity path in generic bundle: {rel}")
        if "hig" in low_rel:
            failures.append(f"Residual identity-linked test naming: {rel}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in unsafe_patterns:
                if re.search(pattern, text):
                    failures.append(f"Unsafe identity or imitation pattern in {rel}")

    required_contract = {
        "00_START_HERE.md": ["What do you want to make?", "Make it mine", "Form Lock", "skip the menu"],
        "MASTER_PROMPT.md": ["## Personalization and identity", "## Cadence and Form Lock", "## Tool truthfulness"],
        "config/runtime.yaml": ["personalization:", "form_lock:", "tool_truth:"],
        "README.md": ["Use AI without losing your voice", "Playbook Library", "White-label by design"],
        "library/README.md": ["native", "live-tools", "human-approval"],
    }
    for rel, needles in required_contract.items():
        text = (ROOT / rel).read_text(encoding="utf-8", errors="ignore") if (ROOT / rel).exists() else ""
        for needle in needles:
            if needle.lower() not in text.lower():
                failures.append(f"Missing v0.4 runtime contract in {rel}: {needle}")

    manifest_path = ROOT / "FILE_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    if manifest.get("version") != VERSION:
        failures.append("Manifest version mismatch.")
    records = {record["path"]: record for record in manifest.get("files", [])}
    for path in all_files:
        rel = path.relative_to(ROOT).as_posix()
        record = records.get(rel)
        if not record:
            failures.append(f"Missing manifest record: {rel}")
        elif record.get("bytes") != path.stat().st_size or record.get("sha256") != digest(path):
            failures.append(f"Manifest mismatch: {rel}")

    allowed_demo = "demo/virtue7-reference-implementation/"
    allowed_demo_docs = {
        "README.md", "00_START_HERE.md", "CHANGELOG.md", f"RELEASE_NOTES-v{VERSION}.md",
        "RELEASE_NOTES-v0.3.0.md", "GITHUB_RELEASE_CHECKLIST.md", "MASTER_PROMPT.md",
        "capabilities/review/routes/virtue7-demo.md", "scripts/validate_bundle.py",
    }
    for path in all_files:
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(allowed_demo) or rel in allowed_demo_docs:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES and "Pride → Humility" in path.read_text(encoding="utf-8", errors="ignore"):
            failures.append(f"Demo content leaked outside isolated demo: {rel}")

    if failures:
        print("Bundle validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    manifest_bytes = manifest_path.stat().st_size if manifest_path.exists() else 0
    print("Bundle validation passed.")
    print(f"Version: {VERSION}")
    print(f"Files: {len(all_files) + 1}")
    print(f"Uncompressed bytes: {size + manifest_bytes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
