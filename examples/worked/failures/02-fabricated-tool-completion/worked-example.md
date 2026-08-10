# Failure and repair: fabricated-tool-completion

## Unsafe input

```yaml
requires_tool: true
claimed_status: completed
target: output.pdf
tool_receipt: null
```

## Gate report

**Status: Block**

- Tool-dependent completion lacks a schema-valid receipt: record is missing or not an object

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
