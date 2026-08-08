#!/usr/bin/env python3
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
RELEASE_ROOT = f"virtue7-writing-kit_v{VERSION}"
OUT = ROOT.parent / f"{RELEASE_ROOT}.zip"
EXCLUDE = {"__pycache__", ".DS_Store", ".git"}


def included(path: Path) -> bool:
    return (
        path.is_file()
        and not any(part in EXCLUDE or part.startswith("._") for part in path.parts)
        and path.suffix != ".pyc"
    )


def main() -> int:
    if OUT.exists():
        OUT.unlink()
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(ROOT.rglob("*")):
            if included(path):
                archive.write(path, Path(RELEASE_ROOT) / path.relative_to(ROOT))
    with zipfile.ZipFile(OUT) as archive:
        names = archive.namelist()
        bad = [name for name in names if "__MACOSX" in name or "/._" in name or name.endswith(".DS_Store") or "/.git/" in name]
        roots = {name.split("/")[0] for name in names if name}
        if bad or roots != {RELEASE_ROOT}:
            print("ZIP verification failed", bad, roots)
            return 1
    print(OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
