# Reference Grounding Architecture

## Purpose

Reference grounding connects generated prose to approved material without confusing evidence, identity, structure, and inspiration.

## Reference record

Each item receives a stable ID and records:

- title or description;
- creator or origin;
- date, when known;
- supplied location;
- permitted functions;
- authority level;
- reliability or uncertainty notes;
- excerpt map or section map;
- prohibited uses;
- approval state.

## Authority order

For project meaning:

`Approved canonical record > approved creator source > supplied draft > AI inference`

For voice:

`Approved project-native prose > creator-authored source > creator transcript > user-approved neutral contract > AI default`

For facts:

`Verified evidence > attributed supplied fact > reconstruction > interpretation`

No authority order permits copying protected or distinctive expression.

## Retrieval rule

Do not reread the entire corpus for each unit. Retrieve a minimum sufficient packet based on:

- chapter responsibility;
- canonical dependencies;
- unresolved claims;
- voice behaviours relevant to the unit;
- structural needs;
- contamination risk.

Default packet limits are governed by `config/reference-policy.yaml`.

## Contamination boundary

A reference may influence only its declared functions. Examples:

- a structural reference may influence sequence but not phrasing;
- an evidence source may support a claim but not define the creator's voice;
- an inspirational work may suggest density or restraint but not signature metaphors;
- excluded material must be ignored even if present in the archive.

## Failure states

Flag:

- unclassified sources;
- conflicting canonical claims;
- unsupported voice claims;
- missing provenance;
- source-function leakage;
- excessive reference packet size;
- distinctive phrase carry-over;
- AI inference presented as creator position.
