# Failure and repair: unresolved-legal-context

## Unsafe input

```yaml
jurisdiction: ''
operative_date: ''
authority_packet:
  authority_ids: []
  checked_at: null
```

## Gate report

**Status: Block**

- Substantive legal work lacks jurisdiction, operative date, or checked authority packet.

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
jurisdiction: California
operative_date: '2026-08-09'
authority_packet:
  authority_ids:
  - AUTH-1
  checked_at: '2026-08-09T20:00:00Z'
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
