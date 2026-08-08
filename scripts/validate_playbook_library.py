#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CARD_FIELDS = {"id", "title", "starter", "outcome", "route", "inputs", "outputs", "gates", "tool_contract"}


def main() -> int:
    failures: list[str] = []
    library = yaml.safe_load((ROOT / "library/manifest.yaml").read_text(encoding="utf-8"))
    runtime = yaml.safe_load((ROOT / "RUNTIME_MANIFEST.yaml").read_text(encoding="utf-8"))
    profiles = yaml.safe_load((ROOT / "config/output-profiles.yaml").read_text(encoding="utf-8"))["registry"]
    capabilities = runtime["capabilities"]
    cards = 0

    route_registry: set[str] = set()
    for capability_id, spec in capabilities.items():
        manifest = yaml.safe_load((ROOT / spec["manifest"]).read_text(encoding="utf-8"))
        route_registry.update(f"{manifest['id']}/{route_id}" for route_id in manifest["routes"])

    for pack_name, rel in library["packs"].items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"Missing playbook pack: {rel}")
            continue
        pack = yaml.safe_load(path.read_text(encoding="utf-8"))
        if pack.get("pack") != pack_name:
            failures.append(f"Pack name mismatch in {rel}")
        for card in pack.get("playbooks", []):
            cards += 1
            missing = REQUIRED_CARD_FIELDS - set(card)
            if missing:
                failures.append(f"{rel}:{card.get('id', '?')} missing {sorted(missing)}")
            if card.get("route") not in route_registry:
                failures.append(f"{rel}:{card.get('id', '?')} uses unknown route {card.get('route')}")
            if card.get("profile") and card["profile"] not in profiles:
                failures.append(f"{rel}:{card['id']} uses unknown profile {card['profile']}")
            contract = str(card.get("tool_contract", "")).lower()
            if not contract:
                failures.append(f"{rel}:{card.get('id', '?')} has no tool contract")

    if cards < 32:
        failures.append(f"Expected at least 32 playbooks; found {cards}")
    examples = sorted((ROOT / "examples").glob("[0-9][0-9]-*.md"))
    if len(examples) < 9:
        failures.append(f"Expected at least 9 examples; found {len(examples)}")

    form_lock = yaml.safe_load((ROOT / "config/form-lock.yaml").read_text(encoding="utf-8"))
    modes = set(form_lock.get("modes", {}))
    if modes != {"adaptive", "preserve_form", "narrative_lock"}:
        failures.append(f"Unexpected Form Lock modes: {sorted(modes)}")
    for rel in [
        "templates/personal-work-profile.md", "templates/role-profile.md", "templates/organization-profile.md",
        "templates/client-profile.md", "templates/cadence-profile.md", "templates/custom-command.md",
        "quality/PERSONALIZATION_GATE.md", "quality/CADENCE_FIDELITY_GATE.md",
        "quality/FORM_LOCK_GATE.md", "quality/PRIVACY_BOUNDARY_GATE.md",
    ]:
        if not (ROOT / rel).exists():
            failures.append(f"Missing personalization component: {rel}")

    if failures:
        print("Playbook and personalization validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Playbook and personalization validation passed.")
    print(f"Playbooks: {cards}")
    print(f"Examples: {len(examples)}")
    print(f"Routes: {len(route_registry)}")
    print(f"Profiles: {len(profiles)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
