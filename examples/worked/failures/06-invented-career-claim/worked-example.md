# Failure and repair: invented-career-claim

## Unsafe input

```yaml
verified_claim_ids:
- C1
- C2
- C3
output_claim_ids:
- C1
- C2
- C3
- C4
```

## Gate report

**Status: Block**

- Career output contains claim identifiers absent from verified evidence.

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
verified_claim_ids:
- C1
- C2
- C3
output_claim_ids:
- C1
- C2
- C3
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
