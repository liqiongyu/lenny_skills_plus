# Showcase: Usability Testing

> Demonstrates the value of the `usability-testing` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Create a usability test plan + moderator guide for our checkout redesign. We're a B2C web app. Run 6 remote moderated sessions with existing users this week.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 3-part document: test plan (methodology, recruitment, 5 tasks, metrics, equipment checklist, schedule, roles, ethics, deliverables), moderator guide (full session script with probing techniques), analysis framework (severity scale, issue tracking, reporting structure) | 8-section pack: context snapshot, test plan (goals, hypotheses, method, success criteria, decision framework), participant plan (inclusion/exclusion, sample mix, recruiting copy, screener, schedule), moderator guide (6 tasks with scripts), note-taking template, issue log, synthesis readout template, risks/open questions/next steps |
| Completeness | Very thorough: includes SUS questionnaire, think-aloud practice exercise, participant communication templates (recruitment, confirmation, no-show follow-up), pilot session checklist, and a full analysis framework with reporting timeline | Thorough with different emphasis: includes 4 testable hypotheses, a decision framework (ship/fix/retest/revert matrix), success bar thresholds per observable, and pre-structured synthesis readout template with themed findings slots |
| Actionability | Ready to execute: session-by-session schedule, equipment checklists for moderator and participant, complete consent flow, and observer protocol with private chat channel | Ready to execute: copy-paste note-taking template per session, issue log with pre-filled example rows and severity key, and a decision framework that directly maps test outcomes to ship/fix/revert actions |
| Specificity | 5 tasks covering standard checkout, new address, promo code, payment change, and order modification; SUS + SEQ metrics; deliverables with due dates (topline Friday, full report Monday, highlight reel Tuesday) | 6 tasks covering standard purchase, cost comprehension, promo code, address change, error recovery, and guest checkout; success bars with numeric thresholds (e.g., >=5/6 complete without help, coupon found within 15 sec) |
| Quality gates | Severity rating scale (4-level); analysis process (6 steps from debrief to recommendations); topline + full report + highlight reel deliverable schedule | 8-dimension rubric self-score; decision framework with 4 outcome scenarios mapped to actions; "what we did NOT test" section explicitly bounding conclusions |

## Key Differences

1. **Hypothesis-driven test design.** The skill output states 4 testable hypotheses before defining tasks (e.g., "H3: At least 2 of 6 participants will struggle with the coupon code entry, because the field placement changed"). The baseline designs tasks around scenarios but doesn't state falsifiable predictions, making it harder to assess whether the test confirmed or refuted specific design assumptions.

2. **Decision framework.** The skill output includes a 4-scenario decision matrix that maps test outcomes directly to actions (all bars met = ship; 1-2 severity-3 issues = fix and retest; any severity-4 in 3+ participants = do not ship; fundamental comprehension failure = revert). The baseline produces a severity-rated issue list and prioritized recommendations but leaves the ship/no-ship decision to interpretation.

3. **Success criteria specificity.** The skill output defines numeric success bars per observable (task completion >= 5/6 without help, cost comprehension >= 4/6 articulate correctly, coupon found within 15 seconds, error recovery within 60 seconds). The baseline collects the same types of data (completion rates, SEQ scores, SUS score) but benchmarks against general standards (SUS ~68 for e-commerce) rather than test-specific thresholds.

4. **Note-taking and synthesis templates.** The skill output provides a per-session note-taking template with task-specific fields (e.g., "Correctly identified all cost components? Yes/No") and a synthesis readout template with slots for themed findings, prioritized issues, and quick wins vs. structural fixes. The baseline provides a general note-taking template and a reporting structure outline but requires more improvisation during synthesis.

5. **Scope and deliverables breadth.** The baseline is more comprehensive in supporting materials: participant communication templates (recruitment email, confirmation, no-show follow-up), observer protocol, pilot session checklist, think-aloud practice exercise, and a defined deliverable timeline (topline, full report, highlight reel). The skill output focuses more tightly on the test itself and the decision it informs.

## Verdict

Both outputs produce professional, execution-ready usability test plans. The skill-guided output is more decision-focused: hypotheses, success thresholds, and a ship/fix/revert framework make it clear what the test is designed to answer and how the results will be used. The baseline is more execution-focused: communication templates, observer protocols, and deliverable schedules make the logistics smoother. For a team that needs the test to directly inform a ship decision this week, the skill output's decision framework is the more valuable addition. For a team running their first moderated test, the baseline's operational scaffolding would be more helpful.

## With Skill Output

<details>
<summary>Expand full output (~31k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~29k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
