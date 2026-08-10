#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import importlib.util
import os
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def load_builder():
    path = ROOT / "scripts/create_release_zip.py"
    spec = importlib.util.spec_from_file_location("release_builder", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def copy_source(target: Path, timestamp: int, mode: int) -> Path:
    source = target / "source"
    shutil.copytree(
        ROOT,
        source,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
    )
    for path in source.rglob("*"):
        os.utime(path, (timestamp, timestamp), follow_symlinks=False)
        if path.is_file():
            path.chmod(mode)
    return source


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    builder = load_builder()
    with tempfile.TemporaryDirectory(prefix="virtue7-repro-", dir=ROOT.parent) as raw:
        temp = Path(raw)
        first_root = copy_source(temp / "first", 946684800, 0o600)
        second_root = copy_source(temp / "second", 1893456000, 0o755)
        first = builder.build_all(first_root, temp / "first-out")
        second = builder.build_all(second_root, temp / "second-out")
        failures = []
        for left, right in zip(first, second, strict=True):
            if left.read_bytes() != right.read_bytes():
                failures.append(f"{left.name}: {digest(left)} != {digest(right)}")
        if failures:
            print("Release reproducibility failed:")
            for failure in failures:
                print(f"- {failure}")
            return 1
        print("Release reproducibility passed across differing source mtimes and modes.")
        for path in first:
            print(f"- {path.name}: {digest(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
