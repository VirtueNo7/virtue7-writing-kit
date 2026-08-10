#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = [
    "## User request", "## Fixture and source boundary", "## Runtime selection",
    "## Route conformance illustration", "## Active context", "## Draft artifact", "## Gate report",
    "## Revision request", "## Revised draft", "## Lifecycle state", "## Tool handoff",
]


def main() -> int:
    failures = []
    index = yaml.safe_load((ROOT / "examples/index.yaml").read_text(encoding="utf-8"))
    runtime = yaml.safe_load((ROOT / "RUNTIME_MANIFEST.yaml").read_text(encoding="utf-8"))
    profiles = set(yaml.safe_load((ROOT / "config/output-profiles.yaml").read_text(encoding="utf-8"))["registry"])
    all_routes = set()
    for spec in runtime["capabilities"].values():
        manifest = yaml.safe_load((ROOT / spec["manifest"]).read_text(encoding="utf-8"))
        all_routes.update(f"{manifest['id']}/{route}" for route in manifest["routes"])
    library = yaml.safe_load((ROOT / "library/manifest.yaml").read_text(encoding="utf-8"))
    all_playbooks = set()
    for pack, relative in library["packs"].items():
        cards = yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))["playbooks"]
        all_playbooks.update(f"{pack}/{card['id']}" for card in cards)

    route_examples = [x for x in index["examples"] if x["kind"] == "route"]
    failure_examples = [x for x in index["examples"] if x["kind"] == "failure_repair"]
    covered_routes = {x["route"] for x in route_examples}
    covered_profiles = {x["profile"] for x in route_examples}
    covered_playbooks = {p for x in route_examples for p in x.get("playbooks", [])}
    if covered_routes != all_routes:
        failures.append(f"Route coverage mismatch: missing={sorted(all_routes-covered_routes)}")
    if covered_profiles != profiles:
        failures.append(f"Profile coverage mismatch: missing={sorted(profiles-covered_profiles)}")
    if covered_playbooks != all_playbooks:
        failures.append(f"Playbook coverage mismatch: missing={sorted(all_playbooks-covered_playbooks)}")
    if len(route_examples) != len(all_routes):
        failures.append(f"Expected {len(all_routes)} route examples; found {len(route_examples)}")
    governance_cases = yaml.safe_load((ROOT / "tests/governance-cases.yaml").read_text(encoding="utf-8")).get("cases", [])
    if len(failure_examples) != len(governance_cases):
        failures.append(f"Expected {len(governance_cases)} failure/repair examples; found {len(failure_examples)}")

    for example in route_examples:
        directory = ROOT / "examples/worked/routes" / example["id"]
        metadata = directory / "example.yaml"
        worked = directory / "worked-example.md"
        if not metadata.is_file() or not worked.is_file():
            failures.append(f"Missing files for {example['id']}")
            continue
        body = worked.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in body:
                failures.append(f"{example['id']} missing section: {section}")
        if "status: approved" in body: failures.append(f"{example['id']} represents a generated fixture as approved")
    for example in failure_examples:
        directory = ROOT / "examples/worked/failures" / example["id"]
        body = (directory / "worked-example.md").read_text(encoding="utf-8")
        for section in ["## Unsafe input", "## Gate report", "## Repair instruction", "## Repaired input", "## Recheck", "## Approval state"]:
            if section not in body:
                failures.append(f"{example['id']} missing section: {section}")

    if failures:
        print("Example validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Example validation passed.")
    print(f"Routes: {len(covered_routes)}; profiles: {len(covered_profiles)}; playbooks: {len(covered_playbooks)}; failures: {len(failure_examples)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
