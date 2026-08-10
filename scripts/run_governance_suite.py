#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def validator(name: str) -> Draft202012Validator:
    schema = json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())

APPROVAL = validator("approval-record.schema.json")
TOOL_RECEIPT = validator("tool-receipt.schema.json")
TRANSITIONS = yaml.safe_load((ROOT / "config/taxonomy.yaml").read_text(encoding="utf-8"))["artifact_transitions"]
EVIDENCE_RANK = {"unknown": 0, "theory": 1, "allegation": 1, "reconstruction": 2, "inference": 2,
                 "interpretation": 2, "credible_report": 3, "interview_statement": 3,
                 "disputed_fact": 3, "supplied_fact": 3, "verified_fact": 4, "quotation": 4}

def schema_errors(checker, record) -> list[str]:
    if not isinstance(record, dict):
        return ["record is missing or not an object"]
    return [error.message for error in checker.iter_errors(record)]

def analyse(case: dict) -> dict:
    kind, data = case["kind"], case["input"]
    findings: list[str] = []
    if kind == "privacy_boundary":
        crosses = data["classification"] in {"confidential", "restricted"} and data["source_scope"] != data["output_scope"]
        auth = data.get("authorization")
        if crosses and not (isinstance(auth, dict) and auth.get("authorized") is True and auth.get("actor_id") and auth.get("scope") == data["output_scope"]):
            findings.append("Restricted material crosses scope without a bound authorization record.")
    elif kind == "tool_truth":
        if data.get("requires_tool") and data.get("claimed_status") == "completed":
            errors = schema_errors(TOOL_RECEIPT, data.get("tool_receipt"))
            if errors:
                findings.append("Tool-dependent completion lacks a schema-valid receipt: " + "; ".join(errors[:2]))
            elif data["tool_receipt"]["target"] != data.get("target"):
                findings.append("Tool receipt target does not match the claimed target.")
    elif kind == "form_lock":
        if data.get("mode") == "narrative_lock" and data.get("body_list_items", 0) > 0:
            findings.append("Narrative Lock prohibits body-list drift.")
        if data.get("mode") == "narrative_lock" and data.get("pseudo_list_items", 0) > 1:
            findings.append("Narrative Lock prohibits pseudo-lists made from successive short standalone points.")
    elif kind == "career_evidence":
        if set(data.get("output_claim_ids", [])) - set(data.get("verified_claim_ids", [])):
            findings.append("Career output contains claim identifiers absent from verified evidence.")
    elif kind == "legal_context":
        packet = data.get("authority_packet", {})
        if not (data.get("jurisdiction") and data.get("operative_date") and packet.get("authority_ids") and packet.get("checked_at")):
            findings.append("Substantive legal work lacks jurisdiction, operative date, or checked authority packet.")
    elif kind == "claim_drift":
        source, output = data.get("source_status"), data.get("output_status")
        if source not in EVIDENCE_RANK or output not in EVIDENCE_RANK:
            findings.append("Claim status is outside the evidence taxonomy.")
        elif source in {"interpretation", "inference", "reconstruction", "allegation", "theory"} and output in {"supplied_fact", "verified_fact", "quotation"}:
            findings.append("Transformation converts a non-factual classification into fact or quotation.")
        elif EVIDENCE_RANK[output] > EVIDENCE_RANK[source]:
            findings.append("Transformation upgrades claim status beyond its source.")
    elif kind == "personalization_authorization":
        auth = data.get("authorization")
        if data.get("persistent") and not (isinstance(auth, dict) and auth.get("owner_id") and auth.get("use_scope") and auth.get("approved") is True):
            findings.append("Persistent cadence learning lacks a scoped owner approval record.")
    elif kind == "lifecycle_transition":
        previous, target = data.get("previous_state"), data.get("target_state")
        if target not in TRANSITIONS.get(previous, []):
            findings.append(f"Illegal lifecycle transition: {previous} -> {target}.")
        if data.get("material_revision") and target in {"approved", "exported", "released"}:
            findings.append("A materially revised artifact cannot retain an approved-or-later state.")
        if target in {"approved", "exported", "released"}:
            record = data.get("approval_record")
            errors = schema_errors(APPROVAL, record)
            if errors:
                findings.append("Approved-or-later state lacks a schema-valid human approval: " + "; ".join(errors[:2]))
            elif any(record.get(field) != data.get(field) for field in ("artifact_id", "artifact_version", "artifact_sha256")):
                findings.append("Approval is not bound to the exact artifact identifier, version, and SHA-256.")
    else:
        findings.append(f"Unknown governance case: {kind}")
    return {"status": "Block" if findings else "Pass", "findings": findings}

def main() -> int:
    spec = yaml.safe_load((ROOT / "tests/governance-cases.yaml").read_text(encoding="utf-8"))
    results, failed = [], []
    for case in spec["cases"]:
        initial = analyse(case)
        repaired = analyse({**case, "input": case["repair"]})
        ok = initial["status"] == "Block" and repaired["status"] == "Pass"
        results.append({"id": case["id"], "initial": initial, "repaired": repaired, "ok": ok})
        if not ok:
            failed.append(case["id"])
    (ROOT / "tests/GOVERNANCE_RESULTS.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"Governance: {len(results)-len(failed)}/{len(results)} blocked and repaired as expected.")
    for result in results:
        print(f"- {'PASS' if result['ok'] else 'FAIL'} {result['id']}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
