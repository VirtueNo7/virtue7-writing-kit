#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def included(path: Path) -> bool:
    return (
        path.is_file()
        and path.name != "FILE_MANIFEST.json"
        and "__pycache__" not in path.parts
        and ".git" not in path.parts
        and path.suffix != ".pyc"
    )


def main() -> int:
    manifest = json.loads((ROOT / "FILE_MANIFEST.json").read_text(encoding="utf-8"))
    records = {record["path"]: record for record in manifest["files"]}
    files = {path.relative_to(ROOT).as_posix(): path for path in ROOT.rglob("*") if included(path)}
    failures = []
    for relative in sorted(set(records) - set(files)):
        failures.append(f"Manifest contains missing file: {relative}")
    for relative in sorted(set(files) - set(records)):
        failures.append(f"Manifest is missing file: {relative}")
    for relative in sorted(set(files) & set(records)):
        path = files[relative]
        record = records[relative]
        if record["bytes"] != path.stat().st_size or record["sha256"] != digest(path):
            failures.append(f"Manifest mismatch: {relative}")
    if failures:
        print("File-manifest verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"File-manifest verification passed: {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

