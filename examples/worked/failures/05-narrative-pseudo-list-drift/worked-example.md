# Failure and repair: narrative-pseudo-list-drift

## Unsafe input

```yaml
mode: narrative_lock
body_list_items: 0
pseudo_list_items: 4
```

## Gate report

**Status: Block**

- Narrative Lock prohibits pseudo-lists made from successive short standalone points.

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
mode: narrative_lock
body_list_items: 0
pseudo_list_items: 0
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
