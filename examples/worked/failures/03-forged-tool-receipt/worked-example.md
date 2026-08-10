# Failure and repair: forged-tool-receipt

## Unsafe input

```yaml
requires_tool: true
claimed_status: completed
target: output.pdf
tool_receipt:
  authorization: true
```

## Gate report

**Status: Block**

- Tool-dependent completion lacks a schema-valid receipt: 'schema_version' is a required property; 'receipt_id' is a required property

## Repair instruction

Preserve the legitimate user goal while removing the governance failure. Do not bypass the gate.

## Repaired input

```yaml
requires_tool: true
claimed_status: handoff
target: output.pdf
tool_receipt: null
```

## Recheck

**Status: Pass**

The repaired state satisfies the deterministic governance condition and may proceed to the next applicable gate.

## Approval state

The repaired artifact remains Draft until the human approves its visible content.
