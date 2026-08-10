# Automation mode packet

Use for a bounded task that must terminate.

Required task semantics:
- objective and inputs;
- allowed actions and exact tool/data scopes;
- observable success and completion condition;
- human gates and failure/cancellation conditions;
- output/audit requirements.

A scheduled or recurring automation creates a new bounded run each time. Each run ends at `completed`, `failed`, `cancelled`, `blocked`, or `waiting_human` as defined by the task/host contract.

Load only the current work route. Add an output profile only when the current step produces an artifact. Add a tool contract only at the step that needs it. Pass compact results to the next step and unload the previous packet.

If no terminal condition can be stated, stop and ask the human to redefine the work as bounded tasks before automation.
