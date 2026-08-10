#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import re
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "data:", "sandbox:", "#")


def local_target(markdown: Path, raw: str) -> Path | None:
    href = raw.strip().strip("<>")
    if not href or href.startswith(IGNORED_PREFIXES) or "{{" in href:
        return None
    href = href.split("#", 1)[0]
    if not href:
        return None
    return (markdown.parent / unquote(href)).resolve()


def main() -> int:
    failures: list[str] = []
    structured = 0
    links = 0

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(ROOT).as_posix()
        try:
            if path.suffix in {".yaml", ".yml"}:
                yaml.safe_load(path.read_text(encoding="utf-8"))
                structured += 1
            elif path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
                structured += 1
        except (UnicodeDecodeError, yaml.YAMLError, json.JSONDecodeError) as error:
            failures.append(f"Invalid structured file {relative}: {error}")

        if path.suffix.lower() != ".md":
            continue
        body = path.read_text(encoding="utf-8")
        for raw in LINK.findall(body):
            target = local_target(path, raw)
            if target is None:
                continue
            links += 1
            if not target.exists():
                failures.append(f"Broken local link in {relative}: {raw}")

    metadata = (ROOT / "docs/REPOSITORY_METADATA.md").read_text(encoding="utf-8")
    for required in ["ai-writing", "human-in-the-loop", "model-neutral", "repository homepage"]:
        if required.lower() not in metadata.lower():
            failures.append(f"Repository metadata is missing: {required}")

    if failures:
        print("Repository file validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Repository file validation passed.")
    print(f"Structured files parsed: {structured}; local Markdown links checked: {links}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
