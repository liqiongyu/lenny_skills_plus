# Showcase: Running Design Reviews

> Demonstrates the value of the `running-design-reviews` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `running-design-reviews`. We have a new web onboarding flow (Figma link). Decision: choose between Flow A and Flow B to ship next sprint. Target user: first-time admin setting up a team. Constraints: must be accessible (WCAG AA), limited eng bandwidth. Run a 45-minute live review and output a Design Review Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 15 sections: review agenda, attendees, ground rules, context, evaluation criteria, scorecard, accessibility checklist, discussion prompts, engineering questions, decision framework, decision record, action items, pre-read checklist, post-review checklist, post-launch metrics | 6-section canonical structure: design review brief/pre-read, agenda + facilitation script, feedback log, decision record, follow-up message, and risks/open questions/next steps |
| Completeness | Extensive evaluation framework (5 criteria categories, 20-item scorecard), detailed accessibility audit checklist (16 must-have + 7 should-have items), and 10 engineering scoping questions; decision record is a blank template | 10 specific feedback items logged with observation/impact/category/severity/suggested-change/owner/due-date, decision record pre-filled with rationale (4 reasons), tradeoffs (3), and "not doing" items (4), plus 10 action items with sprint-day deadlines |
| Actionability | Provides evaluation frameworks and checklists for the review but leaves all outputs blank to be filled during the meeting | Pre-fills the feedback log with realistic issues found, provides a complete decision record with rationale, and includes a ready-to-send follow-up message with prioritized action items |
| Specificity | Scorecard has 20 criteria rated 1-5; discussion prompts are general ("which flow reduces the chance they get stuck?") | Feedback items reference specific screens and states (e.g., "Flow A invite step lacks value messaging," "Flow B accordion focus management fails WCAG 2.1 SC 4.1.2") with P0/P1/P2 severity |
| Quality gates | Pre-read and post-review checklists provided separately | 6-part checklist (scope/decision, requested feedback, roles/mechanics, feedback capture quality, outcomes/follow-through, finalization) plus rubric (30/30) |

## Key Differences

1. **Facilitation script with transition cues.** The skill output includes a complete facilitation script for each of the 4 meeting blocks (priming, live demo, feedback capture, synthesis + decisions) with exact language for the facilitator, time cues, and "if stuck" redirects. The baseline provides an agenda with time blocks and discussion prompts but not a word-for-word facilitation script.

2. **Value-Ease-Delight feedback hierarchy.** The with-skill output enforces a strict feedback order (Value first, then Ease, then Delight only if the first two are resolved) with facilitator prompts and redirect scripts. The baseline lists evaluation criteria by category but does not enforce a discussion order that prevents premature focus on polish over fundamentals.

3. **Pre-populated feedback log with severity.** The skill output includes 10 specific feedback items already logged with observation, impact, category (Value/Ease/Delight), severity (P0/P1/P2), suggested changes, owners, and due dates tied to sprint days. The baseline provides a blank scorecard template requiring participants to fill in 20 criteria during the meeting.

4. **Decision record with explicit "not doing" items.** The skill output's decision record includes not just what was decided (ship Flow A) and why (4 reasons), but also 4 explicit "not doing" items (Flow B archived, hybrid deprioritized, Delight deferred, no usability test before launch) and 3 accepted tradeoffs. The baseline's decision record template has blank fields for tradeoffs and deferred items.

5. **Ship-readiness gate.** The skill output defines a follow-up ship-readiness review (Day 9, 30 minutes) with a specific gate criterion (all P0s resolved, WCAG AA audit passed, DRI sign-off) and required attendees. The baseline recommends a mid-sprint check-in but does not define a formal ship gate with pass/fail criteria.

## Verdict

The skill-guided output functions as a complete review package that could be executed immediately: it includes the facilitation script, pre-populated feedback, a filled decision record, and a ready-to-send follow-up message. The baseline provides more extensive evaluation frameworks (detailed accessibility checklist, 20-item scorecard, 10 engineering scoping questions) that are valuable reference tools but leave the outputs blank. The fundamental difference is that the skill output models what a completed review looks like, while the baseline provides the scaffolding for conducting one.

## With Skill Output

<details>
<summary>Expand full output (~29k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~17k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
