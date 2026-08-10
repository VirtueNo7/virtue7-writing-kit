# Case study: hardening the public foundation

This is an engineering case study of the repository itself. It is not a customer outcome, field study, or independent efficacy claim.

## Problem

The v0.5.0 package had substantial route, profile, example, and release coverage, but several claims were stronger than their executable evidence. Generated examples appeared approved without a human event; structural profile checks could pass semantically false work; tool completion had no universal receipt; release ZIPs inherited source timestamps; route packets named gates without compiling their canonical content; and several public architecture documents were absent from the supplied archive.

## Changes and trace

| Risk | v0.5.0 control | Executable evidence |
|---|---|---|
| Approval transferred or invented | Exact artifact/version/SHA approval schema | `schemas/approval-record.schema.json`; `scripts/run_governance_suite.py` |
| Tool completion fabricated | Authorization- and target-bound receipt | `schemas/tool-receipt.schema.json`; forged-receipt negative case |
| Semantic nonsense passed structural rules | Evidence-sensitive pass requires attestation | `scripts/check_output_profile.py`; `scripts/run_adversarial_suite.py` |
| Gates named but not loaded | Canonical gate content and hash compiled | `scripts/build_runtime_packets.py`; generated packet index |
| ZIP varies by environment metadata | Fixed timestamps, permissions, ordering | `scripts/create_release_zip.py`; `scripts/test_release_reproducibility.py` |
| Examples self-approved | Generated route examples remain revised drafts | `scripts/build_examples.py`; `scripts/validate_examples.py` |

## Result and limits

The release suite deterministically exercises schemas, governance repairs, adversarial no-context cases, generated artifacts, local links, manifest integrity, and archive reproducibility. These are repository-level controls. They do not establish real-world writing quality, factual correctness, legal adequacy, security against every prompt injection, or provider-wide consistency. Those remain evaluation and deployment responsibilities.

