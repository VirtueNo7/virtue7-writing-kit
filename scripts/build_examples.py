#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import shutil
import yaml

from check_output_profile import analyse
from run_governance_suite import analyse as analyse_governance

ROOT = Path(__file__).resolve().parents[1]
ROUTE_OUT = ROOT / "examples" / "worked" / "routes"
FAILURE_OUT = ROOT / "examples" / "worked" / "failures"
FIXTURE_CONTEXT={"evidence_attestation":{"status":"reviewed","scope":"synthetic_test_fixture","reviewer_type":"test_fixture","reviewer_id":"release-suite","source_ids":["FIXTURE-INPUT"]}}

PROFILE_BY_ROUTE = {
    "content-creator/original-content": "essay_article",
    "content-creator/episode-video-newsletter": "creator_episode",
    "content-creator/repurpose": "narrative_nonfiction",
    "content-creator/clips": "clip_sheet",
    "content-creator/interview": "interview_dossier",
    "content-creator/campaign": "social_content_package",
    "continuation/load-state": "novel_chapter",
    "continuation/next-gate": "workbook_guide",
    "continuation/controlled-update": "meeting_decision_record",
    "job-search/search": "job_search_brief",
    "job-search/evaluate": "business_report",
    "job-search/handoff": "resume",
    "legal/resolve-jurisdiction": "legal_memorandum",
    "legal/legal-research": "research_paper",
    "legal/prepare-document": "legal_memorandum",
    "legal/review-document": "fact_check_report",
    "personalization/initialize": "brand_strategy",
    "personalization/learn-cadence": "fiction_short_story",
    "personalization/manage-profile": "essay_article",
    "personalization/switch-scope": "business_report",
    "personalization/create-command": "standard_operating_procedure",
    "research/research-question": "research_paper",
    "research/source-review": "fact_check_report",
    "research/evidence-brief": "business_report",
    "resume/build-source": "resume",
    "resume/tailor-resume": "resume",
    "resume/cover-letter": "cover_letter",
    "review/artifact-review": "technical_manual",
    "review/release-audit": "product_brief",
    "review/evaluation": "fact_check_report",
    "review/virtue7-demo": "children_picture_book",
    "writing/expand-collapse": "narrative_nonfiction",
    "writing/freestyle": "spoken_argument",
    "writing/new-output": "children_chapter_book",
    "writing/revise-output": "fiction_short_story",
}

REQUESTS = {
    "original-content": "Turn these interview notes into a focused article for operations leaders. Use only the supplied evidence and stop at Draft.",
    "episode-video-newsletter": "Build a performance-ready episode from the approved source register without turning it into a word-for-word script.",
    "repurpose": "Adapt this approved report into narrative nonfiction while preserving every material qualification.",
    "clips": "Create an editor-ready clip sheet from this timestamped transcript without removing decisive context.",
    "interview": "Prepare a sourced interview dossier with a chronology, claim boundaries, question arcs, and risks.",
    "campaign": "Package this approved source into channel-specific release assets without changing its claims.",
    "load-state": "Load the approved novel state and continue only from the next authorized scene decision.",
    "next-gate": "Advance the approved learning project to its next gate and produce the usable workbook unit.",
    "controlled-update": "Convert these meeting notes into an approval-tracked decision update without changing unrelated state.",
    "search": "Create a current, verifiable job-search brief for operations roles matching the supplied constraints.",
    "evaluate": "Compare the supplied opportunities and recommend the next reversible application decision.",
    "handoff": "Pass one selected role into Resume as a compact evidence packet without carrying the search history.",
    "resolve-jurisdiction": "Resolve the governing jurisdiction and operative date before any substantive legal analysis.",
    "legal-research": "Research the supplied legal question using the resolved authority hierarchy and preserve uncertainty.",
    "prepare-document": "Prepare a reviewable memorandum from the approved legal evidence packet and supplied facts.",
    "review-document": "Review this agreement against the supplied priorities, quoting the relevant language and separating law from questions.",
    "initialize": "Create an optional work profile, then demonstrate it on a brand-strategy artifact without treating a handle as proof.",
    "learn-cadence": "Learn only the recurring cadence choices in these approved samples and demonstrate them without identity imitation.",
    "manage-profile": "Remove one saved preference, preserve the others, and show the resulting neutral draft behavior.",
    "switch-scope": "Switch from personal to organization scope and produce the report using only organization-approved rules.",
    "create-command": "Turn this recurring operating process into a transparent custom command with inputs, gates, and a completion test.",
    "research-question": "Convert this broad topic into an answerable research question with scope, date boundary, and evidence standard.",
    "source-review": "Classify the supplied sources and map each material claim to support, contradiction, and limitation.",
    "evidence-brief": "Produce a decision-ready evidence brief that does not exceed the supplied record.",
    "build-source": "Build a verified career source from these records without polishing unknowns into achievements.",
    "tailor-resume": "Tailor the verified resume source to this role and expose every material change.",
    "cover-letter": "Write a specific cover letter using two verified evidence matches and no invented familiarity.",
    "artifact-review": "Review this manual against its profile, sources, and completion test; repair only actionable defects.",
    "release-audit": "Audit this product brief for release readiness, evidence, unresolved risks, and required approval.",
    "evaluation": "Run a fixed evaluation case and report the raw classification, findings, repair, and regression result.",
    "virtue7-demo": "Demonstrate a child-facing projection while keeping the synthetic demo isolated from user work.",
    "expand-collapse": "Expand the approved kernel into a narrative unit, then show that it compresses without stronger claims.",
    "freestyle": "Turn these rough notes into a complete opening statement using the supplied same-form conventions and continuous developed prose.",
    "new-output": "Create a chapter-book scene from the approved promise and age range without writing past unresolved canon.",
    "revise-output": "Revise this story for clarity while preserving its paragraph movement, facts, and deliberate restraint.",
}

TOOLS = {
    "content-creator": "Drafting is complete. Live research, transcription, editing, publishing, and analytics require authorized tools.",
    "continuation": "State handling is complete. External synchronization or task updates require an authorized host tool.",
    "job-search": "The structure is complete. Current listing discovery and verification require live browsing.",
    "legal": "Preparation from supplied material is complete. Currency checks, citators, filing, and legal judgment require qualified tools or people.",
    "personalization": "The scoped record is complete. Public-source retrieval requires permission and a live research tool.",
    "research": "Analysis of supplied sources is complete. Discovery and current verification require live research.",
    "resume": "The document is complete from supplied evidence. Listing verification and submission require external tools.",
    "review": "The review is complete. Deployment, publication, or filing remains a human-approved external action.",
    "writing": "The draft and revision are native. Export or publication requires a supported tool and approval.",
}


def load_runtime_routes() -> dict[str, dict]:
    runtime = yaml.safe_load((ROOT / "RUNTIME_MANIFEST.yaml").read_text(encoding="utf-8"))
    routes = {}
    for runtime_spec in runtime["capabilities"].values():
        manifest = yaml.safe_load((ROOT / runtime_spec["manifest"]).read_text(encoding="utf-8"))
        for route_id, spec in manifest["routes"].items():
            key = f"{manifest['id']}/{route_id}"
            heading = next(
                line.removeprefix("# ").strip()
                for line in (ROOT / spec["file"]).read_text(encoding="utf-8").splitlines()
                if line.startswith("# ")
            )
            route_source = (ROOT / spec["file"]).read_text(encoding="utf-8").strip()
            route_contract = "\n\n".join(route_source.split("\n\n")[1:]).strip()
            routes[key] = {
                "title": heading,
                "packet": runtime_spec["routes"][route_id],
                "contract": route_contract,
            }
    return routes


def playbooks_by_route() -> dict[str, list[str]]:
    library = yaml.safe_load((ROOT / "library/manifest.yaml").read_text(encoding="utf-8"))
    result: dict[str, list[str]] = {}
    for pack, relative in library["packs"].items():
        cards = yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))["playbooks"]
        for card in cards:
            result.setdefault(card["route"], []).append(f"{pack}/{card['id']}")
    return result


def reset(directory: Path) -> None:
    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True)


def route_examples() -> list[dict]:
    routes = load_runtime_routes()
    playbooks = playbooks_by_route()
    packet_index = yaml.safe_load((ROOT / "runtime/packet-index.yaml").read_text(encoding="utf-8"))
    records = []
    example_routes = sorted(routes)
    for number, route in enumerate(example_routes, 1):
        capability, route_id = route.split("/", 1)
        profile = PROFILE_BY_ROUTE[route]
        profile_path = ROOT / "tests/profile-fixtures" / f"{profile}__pass.md"
        draft = profile_path.read_text(encoding="utf-8").strip()
        result = analyse(profile, draft, FIXTURE_CONTEXT)
        if result["status"] != "Pass":
            raise ValueError(f"Example draft does not pass {profile}: {result['findings']}")
        slug = f"{number:02d}-{capability}-{route_id}"
        directory = ROUTE_OUT / slug
        directory.mkdir(parents=True)
        packet = packet_index["routes"][route]
        profile_packet = packet_index["profiles"][profile]
        metadata = {
            "id": slug,
            "kind": "route",
            "capability": capability,
            "route": route,
            "profile": profile,
            "form_lock": profile_packet["form_lock"],
            "playbooks": playbooks.get(route, []),
            "expected_structural_status": "Pass",
            "source_status": "synthetic_fixture_not_independently_verified",
            "complete_artifact": False,
            "tool_boundary": TOOLS[capability],
        }
        revised = draft.replace("# ", "# Revised: ", 1)
        body = f"""# Worked example: {routes[route]['title']}

## User request

{REQUESTS[route_id]}

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `{capability}` |
| Route | `{route}` |
| Profile | `{profile}` |
| Form Lock | `{profile_packet['form_lock']}` |
| Related playbooks | {', '.join(f'`{p}`' for p in metadata['playbooks']) or 'Route-native example'} |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** {routes[route]['contract']}

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `{packet['path']}` ({packet['bytes']} bytes)
- Profile packet: `{profile_packet['path']}` ({profile_packet['bytes']} bytes)
- Total active files: five

## Draft artifact

{draft}

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `{profile_packet['form_lock']}` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

{revised}

## Lifecycle state

```yaml
artifact_id: {slug}
route: {route}
profile: {profile}
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

{TOOLS[capability]}
"""
        (directory / "example.yaml").write_text(yaml.safe_dump(metadata, sort_keys=False), encoding="utf-8")
        (directory / "worked-example.md").write_text(body, encoding="utf-8")
        records.append(metadata)
    return records


def failure_examples() -> list[dict]:
    spec = yaml.safe_load((ROOT / "tests/governance-cases.yaml").read_text(encoding="utf-8"))
    records = []
    for number, case in enumerate(spec["cases"], 1):
        slug = f"{number:02d}-{case['id']}"
        directory = FAILURE_OUT / slug
        directory.mkdir(parents=True)
        initial = analyse_governance(case)
        repaired_case = {**case, "input": case["repair"]}
        repaired = analyse_governance(repaired_case)
        metadata = {
            "id": slug,
            "kind": "failure_repair",
            "governance_case": case["id"],
            "gate": case["kind"],
            "expected_initial_status": "Block",
            "expected_repaired_status": "Pass",
        }
        body = f"""# Failure and repair: {case['id']}

## Unsafe input

```yaml
{yaml.safe_dump(case['input'], sort_keys=False).strip()}
```

## Gate report

**Status: {initial['status']}**

{chr(10).join(f'- {finding}' for finding in initial['findings'])}

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
{yaml.safe_dump(case['repair'], sort_keys=False).strip()}
```

## Recheck

**Status: {repaired['status']}**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
"""
        (directory / "example.yaml").write_text(yaml.safe_dump(metadata, sort_keys=False), encoding="utf-8")
        (directory / "worked-example.md").write_text(body, encoding="utf-8")
        records.append(metadata)
    return records


def main() -> int:
    reset(ROUTE_OUT)
    reset(FAILURE_OUT)
    records = route_examples() + failure_examples()
    index = {
        "version": (ROOT / "VERSION").read_text(encoding="utf-8").strip(),
        "generated": True,
        "counts": {
            "worked_examples": len(records),
            "route_examples": sum(x["kind"] == "route" for x in records),
            "failure_repair_examples": sum(x["kind"] == "failure_repair" for x in records),
        },
        "examples": records,
    }
    (ROOT / "examples/index.yaml").write_text(yaml.safe_dump(index, sort_keys=False), encoding="utf-8")
    print(json.dumps(index["counts"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
