#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "profile-fixtures"

EXISTING = {
    "children_picture_book": "01_childrens_read_aloud.md",
    "technical_manual": "02_interface_clarity_technical_guidance.md",
    "essay_article": "03_strategic_historical_essay.md",
    "research_paper": "04_research_brief.md",
    "legal_memorandum": "05_california_legal_memo.md",
    "resume": "06_resume_profile.md",
    "job_search_brief": "07_job_search_brief.md",
    "novel_chapter": "18_narrative_lock_chapter.md",
    "standard_operating_procedure": "20_operating_procedure.md",
}

PASS = {
    "children_chapter_book": """# The Lantern Map

Mira found the brass lantern beneath the loose board in her grandmother's workshop. It was dented, cold, and much heavier than it looked. When she rubbed the glass clean, a blue line appeared inside it and pointed toward the old railway cutting beyond the garden.

She waited until morning because Grandmother's first rule was simple: mysteries were allowed, but disappearing without a note was not. Together they packed water, bread, and a red scarf for marking the path. The lantern's blue line brightened whenever Mira chose the safer fork.

Before leaving the garden, Mira drew the route on a scrap of paper and tucked it beneath the blue teapot. She added the time they expected to return. Grandmother nodded, not because the map was perfect, but because someone at home would know where to begin looking.

At the cutting they heard a thin whistle under the stones. A young fox had slipped between two sleepers and could not pull free. Mira wanted to rush forward, but the gravel shifted under her boot. She stopped, tested each step, and showed Grandmother where the ground still held firm.

They made a loop from the red scarf and eased it around the fox. Mira kept her hands low while Grandmother lifted the loose timber. The fox scrambled free, shook dust from its ears, and vanished into the bracken. Under the sleeper lay a small metal badge shaped like the lantern.

On the walk home, the blue line faded. Mira understood that the lantern had not been mapping treasure. It had been mapping decisions: leave a note, prepare, test the ground, and help without creating another danger. She placed the badge beside the workshop door, ready for the next careful mystery.
""",
    "spoken_argument": """# Opening Statement

The record begins with a simple fact: the council approved the repair budget before the community hall closed. That fact does not resolve every question about the closure, but it gives the discussion a fixed starting point. The public was told that the building required urgent work, and nobody needs to pretend that safety concerns are trivial in order to ask what happened next.

The timeline matters because the stated reason for a temporary closure was followed by months without a published schedule. Meeting minutes record the allocation, contractor correspondence records an initial inspection, and later notices acknowledge additional work. Those sources establish that the project changed. They do not, by themselves, establish that every delay was avoidable.

That qualification is important. A delayed public project is not automatically evidence of misconduct. Buildings reveal hidden defects, contractors encounter supply problems, and safety work can expand once walls are opened. But uncertainty about cause does not eliminate the obligation to explain decisions made with public money. It increases the value of a clear record.

The evidence therefore supports a narrower proposition than either side may prefer. Residents cannot fairly claim that nothing was done, because the record shows inspections, procurement activity, and completed work. The council cannot fairly claim that the existing notices provide a complete account, because the notices omit the current scope, unresolved dependencies, and a reliable reopening sequence.

The strongest counterpoint is that publishing a date too early can create another promise the project may fail to keep. That is true. A responsible timetable can identify dependencies rather than invent certainty. It can say which work is complete, which work remains, what must happen before the next stage begins, and when the public will receive another update if the final date is still unknown.

This is not an argument for certainty where the evidence cannot support it. It is an argument for separating what is known from what remains unresolved, then giving the community enough information to judge the project on the record rather than on rumor.

The council does not need to guarantee the future tonight. It needs to account for the past, identify the present condition of the work, and explain the next decision point. That is the practical standard the evidence supports, and it is the standard the community is entitled to expect.
""",
    "narrative_nonfiction": """# The Night the River Changed Course

The council record dated 14 March 1952 describes three days of rain and a breach beside the eastern levee. The source fixes the date and location, but it does not explain why the breach widened so quickly.

Engineering notes written that week identify saturated soil and an unfinished repair. They suggest that the river exploited an existing weakness rather than creating an entirely new channel. However, the surviving measurements are incomplete.

Residents later remembered a wall of water arriving before dawn. Those interviews add human detail, although memories recorded decades later cannot establish minute-by-minute timing. Their agreement is strongest on the sound, the darkness, and the loss of the lower road.

The evidence therefore supports a limited conclusion. Rain supplied the pressure, the unfinished repair supplied the weak point, and the low road shaped the flood's first movement. It cannot prove that any single decision caused every later loss.

That distinction matters because the rebuilt levee was not merely higher. The new design added inspection access and recorded maintenance intervals. The archive shows a community changing not only a structure but the way it noticed risk.
""",
    "business_report": """# Service Intake Review

## Executive Summary

Support data and interview evidence show that configuration questions create avoidable repeat contacts. The decision is whether to improve onboarding before adding more support capacity.

## Findings

The source data records 126 repeat contacts in the quarter. Interviews identify unclear ownership and inconsistent setup language as the common causes.

## Implications

Additional staffing would absorb demand without removing its source. A guided setup check could reduce demand while preserving an escalation path for complex cases.

## Recommendation

Recommend a four-week pilot for the guided check. The next step is to approve an owner, baseline the repeat-contact rate, and review the result before wider release.
""",
    "workbook_guide": """# Configuration Review Workbook

## Purpose

Use this guide to test a setup before release.

## Exercise: Map the Current State

- Record the intended user.
- List the required inputs.
- Mark every unresolved dependency.

## Practice: Run the Check

1. Open the test environment.
2. Complete the setup as a new user.
3. Record the first point of uncertainty.

## Completion Check

- Check your work against the expected result.
- Confirm that an owner is named for every failure.
- Save the completion record with the test date.
""",
    "cover_letter": """Dear Hiring Team,

I am applying for the Operations Coordinator role because it combines service delivery, records, and cross-team follow-through. My experience includes coordinating a high-volume intake process and supporting a team through changing priorities.

In my current position, I built a shared tracking routine that reduced unresolved handoffs and gave managers a reliable weekly view. I also supported the rollout of a revised customer process, documenting exceptions and helping colleagues adopt the change.

The role's emphasis on accurate communication and dependable execution matches the work I have delivered. I would welcome the opportunity to discuss how that evidence could support your team.

Sincerely,
Jordan Lee
""",
    "creator_episode": """# Why Setup Friction Survives

## Hook

The hardest setup problem is often the one experienced users no longer notice.

## Central Question

Why do configuration questions keep returning after documentation has been expanded?

## Development

We follow one new user through the first ten minutes and compare the expected path with the actual decisions the interface demands.

## Evidence or Story

The source register contains support records, five observed sessions, and the product team's current setup guide. The evidence points to unclear decision ownership rather than missing prose.

## Conclusion

More documentation cannot repair a decision the interface has failed to frame.

## Next Action

Run the setup with one new user and record the first choice they cannot explain.
""",
    "interview_dossier": """# Interview Dossier: Rowan Vale

## Background

- Product educator and former support lead.

## Chronology

- 2022: joined the support team.
- 2024: led onboarding research.

## Themes

- Setup decisions, user confidence, and support feedback.

## Verified Claims

- The supplied biography confirms both roles.

## Open Questions

- Which observation changed the onboarding plan?

## Question Arcs

- Begin with the first field study, test the mechanism, then examine limits.

## Risks

- Do not present internal estimates as published results.
""",
    "clip_sheet": """# Clip Sheet

| Timecode | Hook | Context | In Point | Out Point | Title Options | Destination | Rights |
|---|---|---|---|---|---|---|---|
| 03:12 | Experts stop seeing beginner friction | Discussion follows a new-user observation | 03:12 | 04:01 | The Expert Blind Spot; Why Setup Stalls | Short video | Cleared transcript |
| 11:08 | More instructions can create more choices | Qualification follows immediately | 11:08 | 12:02 | Documentation Is Not the Interface; Choice Overload | Newsletter embed | Cleared transcript |
""",
    "fiction_short_story": """# The Last Tram

Rain had erased the timetable, but Mara waited beneath the broken clock because her brother's note said the last tram still came for anyone carrying an unfinished promise.

At midnight a single carriage rounded the corner without touching the rails. The conductor asked for no fare. He only looked at the sealed letter in Mara's hand and asked whether she wanted forgiveness or merely delivery.

She had rehearsed an answer for seven years. In the quiet carriage, it sounded borrowed. Mara broke the seal, read the first line, and understood that the letter accused her brother of the silence she had chosen herself.

At the final stop she found no platform, only the old hospital garden and one lit window. She rewrote the letter on the conductor's blank ticket. This time she began with what she had done.

The tram returned before dawn. The promise was not finished, but it was finally hers.
""",
    "brand_strategy": """# Fieldnote Positioning

## Audience

Operations teams that need reliable records without a complex implementation programme.

## Problem

Important decisions are scattered across meetings, messages, and personal notes.

## Promise

Turn approved decisions into a durable operating record.

## Proof

Supplied customer evidence supports faster retrieval and clearer ownership; no performance percentage is approved.

## Difference

Fieldnote connects decisions, owners, and evidence instead of offering another blank document store.

## Boundaries

Do not claim automated compliance or guaranteed time savings.

## Open Questions

Which integrations are required for the first customer segment?
""",
    "product_brief": """# Guided Setup Brief

## Problem
New users cannot explain which configuration path applies to them.

## Evidence
Five observed sessions and 126 support records show repeated uncertainty at the same decision.

## Users
First-time workspace administrators.

## Proposed Value
Frame the decision before asking for configuration details.

## Requirements
- The flow must explain each path in plain language.
- Acceptance criteria: a test user shall select a path and state why it applies.

## Non-Goals
- Rebuilding advanced configuration.

## Risks
- Oversimplifying uncommon setups.

## Success Conditions
- Fewer unresolved choices during observed sessions.

## Open Questions
- Which exception requires escalation?
""",
    "meeting_decision_record": """# Setup Pilot Decision

## Context
- Repeat configuration contacts increased during the quarter.

## Decisions
- Run a four-week guided-setup pilot.

## Rationale
- Observation and support evidence identify the same decision point.

## Actions
- Build the prototype.
- Recruit five test users.

## Owners
- Prototype: Sam.
- Research: Ari.

## Due Dates
- Prototype due 2026-09-01.

## Dependencies
- Approved test environment.

## Unresolved Questions
- Which exception path needs specialist review?
""",
    "social_content_package": """# Release Package

## Source Kernel
- Setup friction often comes from an unframed decision.

## Titles
- The Setup Choice Experts Stop Seeing
- Documentation Cannot Make the Decision for You

## Description
- A practical look at the decision behind repeated setup questions.

## Channel Assets
- Newsletter opening: begin with the observed session.
- Short post: state the mechanism and one qualification.

## Calls to Action
- Run one new-user setup observation.

## Release Checklist
- Verify every number.
- Confirm transcript rights.
- Approve the visible version.
""",
    "fact_check_report": """# Fact Check: Did the Pilot Cut Contacts in Half?

## Question
Did the 2025 guided-setup pilot reduce repeat contacts by fifty percent?

## Methodology
Compare the dated 2025 pilot report with the 2024 baseline and the 2026 correction note.

## Findings
The verified fact is that contacts fell during the pilot. The fifty-percent figure is a credible report based on a filtered subset.

## Claim Statuses
- Verified fact: total contacts declined.
- Credible report: the filtered group declined by fifty percent.
- Interpretation: the guide caused the entire decline.
- Unknown: the effect after the pilot window.

## Contradictions
The correction note excludes two support queues included in the baseline.

## Limitations
The sources do not isolate seasonality.

## Conclusion
The broad claim is not verified; a narrower reported result is supported.

## Sources
- 2024 baseline report.
- 2025 pilot analysis.
- 2026 correction note.
""",
}


BLOCK = {
    "spoken_argument": """# Opening Statement

The evidence matters.

The timeline matters.

The calls matter.

What did they know?

When did they know it?

Show me the record.

Show me the facts.

But maybe there is another explanation.

That does not mean the theory is wrong.

It means we ask questions.

And that is the point.
""",
}


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    profiles = yaml.safe_load((ROOT / "config/output-profiles.yaml").read_text(encoding="utf-8"))["registry"]
    cases = []
    for profile in profiles:
        if profile in EXISTING:
            pass_text = (ROOT / "tests/fixtures" / EXISTING[profile]).read_text(encoding="utf-8")
        else:
            pass_text = PASS[profile]
        pass_name = f"{profile}__pass.md"
        block_name = f"{profile}__block.md"
        (OUT / pass_name).write_text(pass_text.strip() + "\n", encoding="utf-8")
        block_text = BLOCK.get(profile, "# Incomplete Draft\n\nA vague placeholder without the profile's required evidence or structure.\n")
        (OUT / block_name).write_text(block_text.strip() + "\n", encoding="utf-8")
        cases.extend([
            {"file": pass_name, "profile": profile, "expect": "Pass"},
            {"file": block_name, "profile": profile, "expect": "Block"},
        ])
    spec = {"version": (ROOT / "VERSION").read_text(encoding="utf-8").strip(), "fixture_directory": "tests/profile-fixtures", "cases": cases}
    (ROOT / "tests/evaluation-cases.yaml").write_text(yaml.safe_dump(spec, sort_keys=False), encoding="utf-8")
    print(f"Profile fixtures: {len(cases)} cases across {len(profiles)} profiles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
