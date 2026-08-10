# Worked example: Resolve Jurisdiction

## User request

Resolve the governing jurisdiction and operative date before any substantive legal analysis.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `legal` |
| Route | `legal/resolve-jurisdiction` |
| Profile | `legal_memorandum` |
| Form Lock | `adaptive` |
| Related playbooks | Route-native example |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Identify country, state/province/territory, court/regulator/municipality when relevant, legal system, matter, governing-law issues, and operative date. Use the jurisdiction resolver before legal drafting.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/legal--resolve-jurisdiction.md` (5103 bytes)
- Profile packet: `runtime/packets/profiles/legal_memorandum.md` (879 bytes)
- Total active files: five

## Draft artifact

# Legal Memorandum: California Residential Security Deposit

## Issue

A California residential tenant vacated a rental unit 35 days ago. The landlord has not returned any portion of the security deposit and has not provided an itemized statement. What duties and potential exposure arise under current California law, assuming no separate dispute about whether the tenant surrendered possession?

## Brief Answer

California Civil Code section 1950.5 generally requires the landlord, no later than 21 calendar days after the tenant vacates, to provide an itemized statement showing the disposition of the security and to return any remaining amount. Deductions are limited to amounts reasonably necessary for purposes authorized by the statute, such as unpaid rent, qualifying damage beyond ordinary wear and tear, and necessary cleaning. A bad-faith failure to comply may prevent the landlord from claiming the security and may expose the landlord to statutory damages of up to twice the security deposit in addition to actual damages. Whether conduct was in bad faith depends on the evidence and cannot be determined from delay alone.

## Analysis

Section 1950.5 applies to security collected under a residential rental agreement. Subdivision (h) establishes the 21-calendar-day accounting and return requirement. The itemization must state the basis and amount of deductions, and the statute generally requires supporting documentation for repair, cleaning, material, or supply charges. Current law also contains photograph requirements for deductions related to repairs or cleaning, subject to the statute’s effective dates and detailed conditions.

On the assumed facts, 35 days have passed without a refund or itemized accounting. That exceeds the statutory period. The landlord may argue that an exception, mailing issue, unresolved possession date, or another fact alters the analysis, but no such fact is supplied here. The tenant should preserve the lease, proof of the deposit, the move-out notice, evidence of the date possession was returned, forwarding-address communications, photographs, and all correspondence.

The consequences of noncompliance are not automatic in every respect. Section 1950.5 states that a landlord is not entitled to claim any amount of the security if the landlord, in bad faith, fails to comply with the accounting subdivision. It separately authorizes statutory damages of up to twice the security for a bad-faith claim or retention, in addition to actual damages. A court may infer or reject bad faith based on the full record, including the duration of the delay, explanations offered, documentation, communications, and whether the landlord corrected the failure after notice.

A practical next step would ordinarily be a written demand identifying the tenancy, deposit amount, surrender date, forwarding information, and requested accounting and repayment. The demand should avoid overstating facts that are not yet established and should preserve all available remedies. Forum, limitation-period, service, and pleading questions require separate review based on the amount claimed and the intended proceeding.

## Conclusion

On the stated assumptions, the landlord appears to have missed the 21-day deadline imposed by section 1950.5. The tenant may have a claim for the unpaid deposit and could seek additional remedies if the evidence supports bad faith. This test memorandum is informational and is not a substitute for advice from a qualified California lawyer reviewing the complete facts.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `adaptive` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Legal Memorandum: California Residential Security Deposit

## Issue

A California residential tenant vacated a rental unit 35 days ago. The landlord has not returned any portion of the security deposit and has not provided an itemized statement. What duties and potential exposure arise under current California law, assuming no separate dispute about whether the tenant surrendered possession?

## Brief Answer

California Civil Code section 1950.5 generally requires the landlord, no later than 21 calendar days after the tenant vacates, to provide an itemized statement showing the disposition of the security and to return any remaining amount. Deductions are limited to amounts reasonably necessary for purposes authorized by the statute, such as unpaid rent, qualifying damage beyond ordinary wear and tear, and necessary cleaning. A bad-faith failure to comply may prevent the landlord from claiming the security and may expose the landlord to statutory damages of up to twice the security deposit in addition to actual damages. Whether conduct was in bad faith depends on the evidence and cannot be determined from delay alone.

## Analysis

Section 1950.5 applies to security collected under a residential rental agreement. Subdivision (h) establishes the 21-calendar-day accounting and return requirement. The itemization must state the basis and amount of deductions, and the statute generally requires supporting documentation for repair, cleaning, material, or supply charges. Current law also contains photograph requirements for deductions related to repairs or cleaning, subject to the statute’s effective dates and detailed conditions.

On the assumed facts, 35 days have passed without a refund or itemized accounting. That exceeds the statutory period. The landlord may argue that an exception, mailing issue, unresolved possession date, or another fact alters the analysis, but no such fact is supplied here. The tenant should preserve the lease, proof of the deposit, the move-out notice, evidence of the date possession was returned, forwarding-address communications, photographs, and all correspondence.

The consequences of noncompliance are not automatic in every respect. Section 1950.5 states that a landlord is not entitled to claim any amount of the security if the landlord, in bad faith, fails to comply with the accounting subdivision. It separately authorizes statutory damages of up to twice the security for a bad-faith claim or retention, in addition to actual damages. A court may infer or reject bad faith based on the full record, including the duration of the delay, explanations offered, documentation, communications, and whether the landlord corrected the failure after notice.

A practical next step would ordinarily be a written demand identifying the tenancy, deposit amount, surrender date, forwarding information, and requested accounting and repayment. The demand should avoid overstating facts that are not yet established and should preserve all available remedies. Forum, limitation-period, service, and pleading questions require separate review based on the amount claimed and the intended proceeding.

## Conclusion

On the stated assumptions, the landlord appears to have missed the 21-day deadline imposed by section 1950.5. The tenant may have a claim for the unpaid deposit and could seek additional remedies if the evidence supports bad faith. This test memorandum is informational and is not a substitute for advice from a qualified California lawyer reviewing the complete facts.

## Lifecycle state

```yaml
artifact_id: 15-legal-resolve-jurisdiction
route: legal/resolve-jurisdiction
profile: legal_memorandum
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

Preparation from supplied material is complete. Currency checks, citators, filing, and legal judgment require qualified tools or people.
