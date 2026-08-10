#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import importlib.util
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(relative: str):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []
    taxonomy = load("config/taxonomy.yaml")
    form_modes = set(taxonomy["form_lock_modes"])
    prose_modes = set(taxonomy["prose_modes"])
    artifact_states = list(taxonomy["artifact_states"]); transitions = taxonomy.get("artifact_transitions", {})
    gates = load("config/gates.yaml")["gates"]
    form_config = load("config/form-lock.yaml")
    prose_config = load("config/prose-modes.yaml")["prose_modes"]
    runtime_config = load("config/runtime.yaml")
    kit_config = load("config/kit.yaml")
    runtime = load("RUNTIME_MANIFEST.yaml")
    profiles = load("config/output-profiles.yaml")["registry"]

    if form_modes != set(form_config["modes"]):
        failures.append("Form Lock taxonomy does not match config/form-lock.yaml.")
    if prose_modes != set(prose_config):
        failures.append("Prose-mode taxonomy does not match config/prose-modes.yaml.")
    if set(transitions) != set(artifact_states): failures.append("Every artifact state must have an explicit transition entry.")
    if artifact_states != runtime_config["artifact_lifecycle"]["states"]:
        failures.append("Artifact lifecycle does not match the canonical taxonomy.")
    if kit_config["output_defaults"].get("artifact_status") not in artifact_states:
        failures.append("Default artifact status is not in the canonical lifecycle.")
    if runtime_config["artifact_lifecycle"].get("initial_state") != "draft":
        failures.append("Artifact lifecycle must begin in draft.")
    for field in ["artifact_record_schema","approval_record_schema"]:
        relative=runtime_config["artifact_lifecycle"].get(field)
        if not relative or not (ROOT/relative).is_file(): failures.append(f"Missing lifecycle schema: {field}")
    if not (ROOT/runtime_config.get("tool_truth",{}).get("receipt_schema","")).is_file(): failures.append("Missing tool receipt schema.")
    if runtime_config["artifact_lifecycle"].get("material_revision_resets_to") != "revised_draft":
        failures.append("Material revisions must return to revised_draft.")
    for gate_id, relative in gates.items():
        if not (ROOT / relative).is_file():
            failures.append(f"Gate {gate_id} points to missing file: {relative}")

    route_registry: set[str] = set()
    for runtime_id, runtime_spec in runtime["capabilities"].items():
        manifest_path = ROOT / runtime_spec["manifest"]
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        for gate_id in manifest.get("quality_defaults", []):
            if gate_id not in gates:
                failures.append(f"{manifest_path}: unknown default gate {gate_id}")
        manifest_routes = set(manifest["routes"])
        runtime_routes = set(runtime_spec["routes"])
        if manifest_routes != runtime_routes:
            failures.append(f"{runtime_id}: runtime and capability route registries differ")
        for route_id, spec in manifest["routes"].items():
            route_registry.add(f"{manifest['id']}/{route_id}")
            if not (ROOT / spec["file"]).is_file():
                failures.append(f"Missing route file: {spec['file']}")
            packet = ROOT / runtime_spec["routes"][route_id]
            if not packet.is_file():
                failures.append(f"Missing compiled route packet: {packet.relative_to(ROOT)}")

    for profile_id, relative in profiles.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"Missing profile file: {relative}")
            continue
        profile = yaml.safe_load(path.read_text(encoding="utf-8"))
        if profile.get("id") != profile_id:
            failures.append(f"Profile key/id mismatch: {profile_id} != {profile.get('id')}")
        if str(profile.get("version")) != str(taxonomy["version"]):
            failures.append(f"{profile_id}: profile version does not match taxonomy version")
        if profile.get("default_prose_mode") not in prose_modes:
            failures.append(f"{profile_id}: unknown prose mode {profile.get('default_prose_mode')}")
        lock_id = profile.get("default_form_lock")
        if lock_id and lock_id not in form_modes:
            failures.append(f"{profile_id}: unknown Form Lock {lock_id}")
        gate = profile.get("quality_gate")
        if gate and not (ROOT / gate).is_file():
            failures.append(f"{profile_id}: missing quality gate {gate}")
        if not (ROOT / "runtime/packets/profiles" / f"{profile_id}.md").is_file():
            failures.append(f"{profile_id}: missing compiled profile packet")

    library = load("library/manifest.yaml")
    for pack_name, relative in library["packs"].items():
        pack = load(relative)
        for card in pack.get("playbooks", []):
            prefix = f"{pack_name}/{card.get('id', '?')}"
            if card.get("route") not in route_registry:
                failures.append(f"{prefix}: unknown route {card.get('route')}")
            if card.get("profile") and card["profile"] not in profiles:
                failures.append(f"{prefix}: unknown profile {card['profile']}")
            if card.get("form_lock") and card["form_lock"] not in form_modes:
                failures.append(f"{prefix}: unknown Form Lock {card['form_lock']}")
            for gate_id in card.get("gates", []):
                if gate_id not in gates:
                    failures.append(f"{prefix}: unknown gate {gate_id}")

    spec = importlib.util.spec_from_file_location("profile_checker", ROOT / "scripts/check_output_profile.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    unsupported = set(profiles) - set(module.SUPPORTED_PROFILES)
    if unsupported:
        failures.append(f"Profiles missing automated checker support: {sorted(unsupported)}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    license_md = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    if "MIT License" not in license_text or "MIT License" not in license_md:
        failures.append("LICENSE and LICENSE.md do not agree on MIT licensing.")
    if "RIGHTS HOLDER" in license_md or "No public reuse" in license_md:
        failures.append("LICENSE.md retains a provisional rights notice.")

    if failures:
        print("Schema validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Schema validation passed.")
    print(f"Routes: {len(route_registry)}")
    print(f"Profiles: {len(profiles)}")
    print(f"Gates: {len(gates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
