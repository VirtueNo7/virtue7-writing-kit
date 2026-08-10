#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = {
    "approval-record": ("schemas/approval-record.schema.json", "tests/contracts/approval-record.json"),
    "tool-receipt": ("schemas/tool-receipt.schema.json", "tests/contracts/tool-receipt.json"),
    "artifact-record": ("schemas/artifact-record.schema.json", "tests/contracts/artifact-record.json"),
    "extension-manifest": ("schemas/extension-manifest.schema.json", "tests/contracts/extension-manifest.json"),
}


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def main() -> int:
    failures = []
    loaded = {}
    for name, (schema_path, fixture_path) in CONTRACTS.items():
        schema = load(schema_path)
        fixture = load(fixture_path)
        try:
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema, format_checker=FormatChecker()).validate(fixture)
        except Exception as error:
            failures.append(f"{name}: {error}")
        loaded[name] = fixture

    approval = loaded["approval-record"]
    artifact = loaded["artifact-record"]
    if approval["artifact_id"] != artifact["artifact_id"]:
        failures.append("Approval record artifact_id does not match artifact record.")
    if approval["artifact_version"] != artifact["version"]:
        failures.append("Approval record version does not match artifact record.")
    if approval["artifact_sha256"] != artifact["sha256"]:
        failures.append("Approval record SHA-256 does not match artifact record.")
    if artifact.get("approval_artifact_sha256") != artifact["sha256"]:
        failures.append("Artifact approval binding does not match current SHA-256.")
    if approval["event_id"] != artifact.get("approval_receipt_id"):
        failures.append("Artifact approval receipt does not resolve to the approval event.")

    # Required negative controls: placeholders, booleans, and mismatched hashes must fail.
    invalid_approval = {**approval, "actor_type": "model"}
    invalid_receipt = {**loaded["tool-receipt"], "authorization": True}
    invalid_artifact = {**artifact, "approval_artifact_sha256": "1111111111111111111111111111111111111111111111111111111111111111"}
    schema_pairs = [
        ("model self-approval", load(CONTRACTS["approval-record"][0]), invalid_approval),
        ("boolean tool authorization", load(CONTRACTS["tool-receipt"][0]), invalid_receipt),
    ]
    for label, schema, instance in schema_pairs:
        if Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(instance):
            failures.append(f"Negative control unexpectedly valid: {label}")
    if invalid_artifact["approval_artifact_sha256"] == invalid_artifact["sha256"]:
        failures.append("Mismatched artifact-hash negative control is ineffective.")

    if failures:
        print("Contract schema validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Contract schema validation passed: {len(CONTRACTS)} schemas and cross-record bindings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
