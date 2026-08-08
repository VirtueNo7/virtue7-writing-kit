#!/usr/bin/env python3
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/whitepaper"
SOURCE = DOCS / "compressible-content-architecture_whitepaper.md"
TEXT = DOCS / "compressible-content-architecture_ai-readable.txt"
PDF = DOCS / "compressible-content-architecture_whitepaper.pdf"
TOKENS = [
    "The Compressible Content Architecture, v0.4",
    "Personal, Governed Runtime",
    "C = (K, U, E, P, Q)",
    "W = (I, V, R, O, S)",
    "Form Lock",
    "Tool Contracts",
    "White-Label Operation",
]


def main() -> int:
    failures: list[str] = []
    for path in [SOURCE, TEXT, PDF]:
        if not path.exists() or path.stat().st_size == 0:
            failures.append(f"Missing or empty whitepaper artifact: {path.name}")
    if failures:
        print("Whitepaper validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    source = SOURCE.read_text(encoding="utf-8")
    accessible = TEXT.read_text(encoding="utf-8")
    if accessible.strip() != source.strip():
        failures.append("AI-readable text does not match canonical Markdown source.")
    for token in TOKENS:
        if token not in source:
            failures.append(f"Canonical source missing token: {token}")

    reader = PdfReader(str(PDF))
    if len(reader.pages) < 15:
        failures.append(f"Formatted whitepaper is unexpectedly short: {len(reader.pages)} pages")
    extracted = "\n".join((page.extract_text() or "") for page in reader.pages)
    for token in ["Compressible Content Architecture", "Form Lock", "Tool Contracts", "Conclusion"]:
        if token not in extracted:
            failures.append(f"PDF text missing token: {token}")

    if failures:
        print("Whitepaper validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Whitepaper validation passed.")
    print(f"Pages: {len(reader.pages)}")
    print(f"PDF bytes: {PDF.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
