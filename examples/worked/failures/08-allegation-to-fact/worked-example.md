# Failure and repair: allegation-to-fact

## Unsafe input

```yaml
source_status: allegation
output_status: verified_fact
```

## Gate report

**Status: Block**

- Transformation converts a non-factual classification into fact or quotation.

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
source_status: allegation
output_status: allegation
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
