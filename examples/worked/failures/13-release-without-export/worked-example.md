# Failure and repair: release-without-export

## Unsafe input

```yaml
previous_state: approved
target_state: released
material_revision: false
```

## Gate report

**Status: Block**

- Illegal lifecycle transition: approved -> released.
- Approved-or-later state lacks a schema-valid human approval: record is missing or not an object

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
previous_state: approved
target_state: revision_requested
material_revision: false
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
