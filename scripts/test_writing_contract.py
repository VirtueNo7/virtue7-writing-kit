#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    failures = []
    registry = yaml.safe_load((ROOT / "config/output-profiles.yaml").read_text(encoding="utf-8"))["registry"]
    if registry.get("spoken_argument") != "profiles/spoken-argument.yaml":
        failures.append("spoken_argument is not registered.")
    profile = yaml.safe_load((ROOT / "profiles/spoken-argument.yaml").read_text(encoding="utf-8"))
    if profile.get("default_form_lock") != "narrative_lock":
        failures.append("spoken_argument must default to Narrative Lock.")
    if profile.get("structure", {}).get("same_form_evidence") != "preserve_structure_when_supplied":
        failures.append("spoken_argument must preserve supplied same-form structure.")

    capability = (ROOT / "capabilities/writing/CAPABILITY.md").read_text(encoding="utf-8")
    route = (ROOT / "capabilities/writing/routes/freestyle.md").read_text(encoding="utf-8")
    required = {
        "capability": ["same-form examples as primary form evidence", "does not authorize invented show wrappers"],
        "route": ["select `spoken_argument`", "it controls form before generic profile defaults", "do not infer a branded intro, outro", "inspect the actual body for fragment stacks"],
    }
    for phrase in required["capability"]:
        if phrase not in capability:
            failures.append(f"Writing capability missing safeguard: {phrase}")
    for phrase in required["route"]:
        if phrase not in route:
            failures.append(f"Freestyle route missing safeguard: {phrase}")

    compiled = ROOT / "runtime/packets/routes/writing--freestyle.md"
    if compiled.exists():
        compiled_text = compiled.read_text(encoding="utf-8")
        for phrase in ["select `spoken_argument`", "same-form evidence", "fragment stacks"]:
            if phrase not in compiled_text:
                failures.append(f"Compiled writing packet missing safeguard: {phrase}")

    form_lock = (ROOT / "config/form-lock.yaml").read_text(encoding="utf-8")
    form_gate = (ROOT / "quality/FORM_LOCK_GATE.md").read_text(encoding="utf-8")
    article_profile = (ROOT / "profiles/essay-article.yaml").read_text(encoding="utf-8")
    for phrase, source, label in [
        ("pseudo_lists", form_lock, "Form Lock config"),
        ("short standalone paragraphs", form_gate, "Form Lock gate"),
        ("short_point_sequences", article_profile, "essay/article profile"),
    ]:
        if phrase not in source:
            failures.append(f"{label} missing pseudo-list safeguard: {phrase}")

    if failures:
        print("Writing contract test failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Writing contract test passed: opening statements route to spoken_argument and same-form evidence controls form.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
