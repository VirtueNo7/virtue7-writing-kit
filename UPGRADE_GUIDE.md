# Upgrade Guide: v0.4.0 to v0.5.0

Version 0.5.0 preserves user-owned profiles, project records, capabilities, routes, playbooks, and white-label output behavior while adding a compact mode-first boot, compiled runtime packets, stronger approval/tool records, broader validation, and prose-structure hardening.

1. Preserve canonical source, claim, profile, and project-state records.
2. Replace the v0.4.0 runtime files with the v0.5.0 release and regenerate compiled packets when developing from source.
3. Keep existing capability and playbook identifiers; the shipped capability set remains 9 modules and 35 routes.
4. Add the `spoken_argument` profile where oral advocacy or presentation-ready prose needs its own form.
5. Convert informal approval markers into `schemas/approval-record.schema.json` when exact approval lineage matters. Content without an exact artifact hash remains Draft or Revised Draft until approved.
6. Record tool-dependent completion with `schemas/tool-receipt.schema.json`. Boolean flags and prose claims are not receipts.
7. Re-run profile, evidence, privacy, Form Lock, governance, adversarial, manifest, whitepaper, and reproducibility checks.
8. Review prose-led outputs for pseudo-lists. Short standalone points should be developed into connected prose or formatted as real list items when a list is appropriate.

No profile, command, source, client rule, or channel rule becomes global during upgrade.
