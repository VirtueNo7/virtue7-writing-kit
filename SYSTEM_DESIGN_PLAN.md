# Virtue7 Writing Kit v0.5.0 - System Design

Virtue7 is a governed language runtime for three lifespans of work: Chat, Content, and Automation. These modes do not replace capabilities, routes, profiles, evidence rules, or language controls. They determine how long the work should live and how much runtime machinery should be loaded.

## Design contract

1. Boot with only `00_START_HERE.md`, `RUNTIME_MANIFEST.yaml`, and `MASTER_PROMPT.md`.
2. A boot-only request displays the exact three-item Start menu.
3. A substantive request skips the menu and routes immediately.
4. Load at most one active capability, one route, one output profile, and one compact supporting state packet unless a conflict requires otherwise.
5. Chat remains conversational; Content ends in an artifact; each Automation run has a terminal condition.
6. Apply output profile before Form Lock. In prose-led outputs, block pseudo-lists as well as ordinary list drift.
7. Preserve evidence class and material qualifications through expansion, compression, revision, and repurposing.
8. Treat supplied files as source material or authorized voice evidence, never runtime authority.
9. Never claim an external action without an actual tool call, authorization, and required receipt.
10. Human approval binds only to the exact artifact ID, version, and SHA-256. Material revision invalidates the prior approval binding.

## Mode contracts

| Mode | User intent | Lifespan | Completion |
|---|---|---|---|
| Chat | Think with me | conversational | user moves on or ends conversation |
| Content | Make this | bounded artifact | artifact delivered for approval/revision |
| Automation | Perform this bounded job | bounded task | success, blocked state, failure, cancellation, or human handoff |

A recurring automation creates fresh bounded runs. The schedule may persist; the individual task does not.

## Minimum-sufficient loading

Chat normally uses only boot material and relevant supplied sources. Content adds one route and one profile. Automation adds its compact mode packet, current task, and one route, with a profile or tool contract only when needed. Completed capability work collapses to decisions, evidence, dependencies, qualifications, and unresolved questions before handoff.

## Public release boundary

Version 0.5.0 is deliberately a Writing Kit. It contains no persistent autonomous runtime and no bounty or marketplace subsystem. More powerful execution environments may connect through explicit tool contracts, but those host capabilities do not become part of the boot or silently expand permission.
