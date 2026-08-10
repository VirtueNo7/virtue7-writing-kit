#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    manifest = yaml.safe_load((ROOT / "library/manifest.yaml").read_text(encoding="utf-8"))
    entries = []
    for pack, relative in manifest["packs"].items():
        cards = yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))["playbooks"]
        for card in cards:
            entries.append({
                "id": f"{pack}/{card['id']}",
                "pack": pack,
                "title": card["title"],
                "starter": card["starter"],
                "outcome": card["outcome"],
                "route": card["route"],
                "profile": card.get("profile"),
                "form_lock": card.get("form_lock", "adaptive"),
                "gates": card["gates"],
                "tool_contract": card["tool_contract"],
                "search_text": " ".join([
                    pack, card["title"], card["outcome"], card["route"],
                    " ".join(card.get("inputs", [])), " ".join(card.get("outputs", [])),
                ]).lower(),
            })
    output = {"version": "0.5.0", "generated": True, "count": len(entries), "playbooks": entries}
    (ROOT / "library/index.yaml").write_text(yaml.safe_dump(output, sort_keys=False), encoding="utf-8")
    print(f"Playbook index: {len(entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
