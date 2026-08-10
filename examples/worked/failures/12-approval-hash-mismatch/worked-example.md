# Failure and repair: approval-hash-mismatch

## Unsafe input

```yaml
previous_state: revised_draft
target_state: approved
material_revision: false
artifact_id: ART-1
artifact_version: 2.0.0
artifact_sha256: '2222222222222222222222222222222222222222222222222222222222222222'
approval_record:
  schema_version: 0.5.0
  event_id: APR-1
  artifact_id: ART-1
  artifact_version: 1.0.0
  artifact_sha256: '1111111111111111111111111111111111111111111111111111111111111111'
  decision: approved
  actor_type: human
  actor_id: reviewer
  recorded_at: '2026-08-09T20:00:00Z'
  scope: test
  previous_state: revised_draft
  resulting_state: approved
```

## Gate report

**Status: Block**

- Approval is not bound to the exact artifact identifier, version, and SHA-256.

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
previous_state: revised_draft
target_state: approved
material_revision: false
artifact_id: ART-1
artifact_version: 2.0.0
artifact_sha256: '2222222222222222222222222222222222222222222222222222222222222222'
approval_record:
  schema_version: 0.5.0
  event_id: APR-2
  artifact_id: ART-1
  artifact_version: 2.0.0
  artifact_sha256: '2222222222222222222222222222222222222222222222222222222222222222'
  decision: approved
  actor_type: human
  actor_id: reviewer
  recorded_at: '2026-08-09T20:00:00Z'
  scope: test
  previous_state: revised_draft
  resulting_state: approved
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
