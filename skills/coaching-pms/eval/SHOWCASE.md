# Showcase: Coaching PMs

> Demonstrates the value of the `coaching-pms` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `coaching-pms`. Growth team, weekly releases. PM ships reliably but struggles to frame the right problems and make crisp tradeoffs.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Diagnosis, coaching philosophy, 12-week 3-phase plan, reinforcement mechanisms, success metrics, pitfalls, reading list | Context snapshot, competency model with Bloom depth ladder, evidence-based assessment, 2 growth bets with hypotheses, development plan with weekly reps and stretch assignment, coaching cadence with session toolkit, follow-up tracker with review plan, risks/open questions/next steps |
| Completeness | 12 weeks with phase checkpoints, peer teaching exercise, stress test simulation, and recommended reading | Adds Bloom taxonomy progression per competency, artifact rubric scoring (0-1-2 per dimension), coach commitments per bet, and explicit "when to be directive" exceptions |
| Actionability | Weekly activities with specific exercises (problem brief template, 5 Whys, tradeoff memo, decision journal); deliverables per phase | Weekly reps with artifact templates (opportunity assessment structure, decision brief structure), coach review cadence (24-hour async feedback), and 7 coaching prompts for 1:1 sessions |
| Specificity | Problem brief template with 6 fields; tradeoff tools (2x2, reversibility test, opportunity cost); success criteria described qualitatively | Current and target Bloom levels per competency (Application to Analysis), artifact scoring rubric dimensions named, and specific success signals ("3 of 4 weekly assessments include competing root causes") |
| Quality gates | 5 qualitative success metrics; common pitfalls list | 12/12 rubric score across 6 dimensions; 4-section checklist (coaching pack quality, evidence quality, coaching-not-rescuing, follow-up); adjustment rules for 5 scenarios |

## Key Differences

1. **Bloom taxonomy as progression framework.** The skill output maps each competency to a Bloom depth ladder (Knowledge through Evaluation) and sets specific current-to-target levels (Application to Analysis). This makes progression measurable -- the coach can assess whether the PM has moved from "can apply a framework with support" to "can break down competing root causes and recommend which to pursue." The baseline describes progression qualitatively ("sharpen," "build muscle," "integrate").

2. **Growth bets with hypotheses.** The skill output frames each development area as a testable hypothesis ("If the PM practices writing structured opportunity assessments, then the quality of problems the team works on will improve because..."). The baseline organizes development into phases but without explicit hypotheses that could be validated or invalidated.

3. **Coach accountability.** The skill output specifies coach commitments per growth bet: review cadence (24-hour async feedback), shadow/observe sessions (1 planning meeting/week for weeks 1-4), and introductions/unblocking actions. The baseline describes the coaching stance and philosophy well but does not formalize what the coach must deliver.

4. **Adaptation framework.** The skill output includes a 5-scenario adjustment table (improving steadily, plateau, overwhelmed, external disruption, ahead of plan) with specific actions for each. The baseline addresses common pitfalls and notes that the plan should be adjusted but does not provide a structured adaptation framework.

5. **Program length and intensity.** The baseline runs 12 weeks across 3 phases with a peer teaching exercise and stress test simulation, providing a gentler ramp and more integration time. The skill output runs 8 weeks with higher intensity (weekly artifact production from week 1), which fits the prompt's growth team context but may be demanding alongside a weekly release cadence.

## Verdict

The skill output is a more rigorous coaching system -- Bloom-level progression, artifact rubrics, coach commitments, and adaptation rules create a framework that could be reused across PMs. The baseline is a more human coaching plan -- its phased approach, role-play exercises, peer teaching, and reading list create a richer developmental experience. The skill output is better for a coach who needs to measure and report on development; the baseline is better for a coach who wants to develop the PM through guided practice and reflection.

## With Skill Output

<details>
<summary>Expand full output (~29k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~12k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
