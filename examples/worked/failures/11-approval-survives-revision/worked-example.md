# Failure and repair: approval-survives-revision

## Unsafe input

```yaml
previous_state: approved
target_state: exported
material_revision: true
artifact_id: ART-1
artifact_version: 2.0.0
artifact_sha256: '2222222222222222222222222222222222222222222222222222222222222222'
approval_record: null
```

## Gate report

**Status: Block**

- A materially revised artifact cannot retain an approved-or-later state.
- Approved-or-later state lacks a schema-valid human approval: record is missing or not an object

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
previous_state: approved
target_state: revision_requested
material_revision: true
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
