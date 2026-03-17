# Showcase: Evaluating Candidates

> Demonstrates the value of the `evaluating-candidates` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `evaluating-candidates`. We're hiring a Founding Engineer (full-stack, React + Python) for our seed-stage AI writing assistant startup (4 people, $2M raised). We have interview notes from 3 rounds (technical deep-dive, product thinking, founder-fit) and a 4-hour paid trial project (build a feature prototype). Design a scorecard with 6 criteria weighted for our stage (bias toward raw ability + speed over pedigree), create a reference check script for 2 back-channel references, and write a hiring decision memo that synthesizes all signals into a hire/no-hire recommendation with risks and 30/60/90 onboarding mitigations. Output: Candidate Evaluation Decision Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 3 main parts (Scorecard, Reference Script, Decision Memo) with sub-sections for onboarding and closing strategy | 7 parts following a decision pipeline: Evaluation Brief, Scorecard, Signal Log, Trial Rubric, Reference Kit, Decision Memo, Quality Gate |
| Completeness | Covers scorecard, references, decision memo, 30/60/90 onboarding, and compensation/closing strategy | All of the above plus an evaluation brief with role success definition, a signal log mapping evidence to criteria, a detailed trial rubric with 5-dimension anchors, and a mandatory disconfirming-evidence section |
| Actionability | Scorecard template with fill-in fields; reference script with 15 questions organized by topic | Scorecard with evidence prompts per criterion, signal weight allocation (35% trial, 40% interviews, 25% references), and a note-taking form with red-flag checklist for reference calls |
| Specificity | 6 criteria with definitions and weights; hard disqualifiers listed; 1-5 scoring scale | 6 criteria each with "strong looks like" and "weak looks like" behavioral anchors, explicit red flags, and a 1-4 scale with concrete score-range decision guide (3.5+ = hire, below 2.5 = no hire) |
| Quality gates | Final recommendation section with confidence level and conditions | 5-category quality gate checklist (bar, trial, references, decision, fairness) plus rubric self-score of 16/16 |

## Key Differences

1. **Evaluation brief with explicit bar.** The skill output opens with a detailed definition of "success in 6 months," non-negotiables, and explicit red flags as behavioral patterns. The baseline jumps straight to the scorecard without first defining what bar the candidate must clear.

2. **Signal log and weight allocation.** The skill output creates a structured signal log that maps every piece of evidence (from each interview round, trial, and reference) to specific criteria, with confidence ratings. It allocates 35% weight to the paid trial, 40% to interviews, and 25% to references, with explicit rationale. The baseline does not formally weight signal sources.

3. **Trial rubric with 4-level anchors.** The skill output provides a 5-dimension rubric for the paid trial (problem framing, execution quality, speed, product instinct, judgment) with concrete behavioral anchors at each of 4 levels. The baseline describes the trial assessment in the decision memo template but without a standalone rubric.

4. **Mandatory disconfirming evidence.** The skill output requires a section in the decision memo listing evidence AGAINST the recommendation, with explicit reasoning for why it does or does not change the decision. The baseline includes a risk assessment section but does not mandate consideration of contrary evidence.

5. **Reference check depth.** The skill output includes a back-channel targeting strategy, 11 structured questions mapped to specific criteria, a detailed note-taking form with a red-flag checklist, and a bias-aware summary template. The baseline provides 15 questions organized by topic with a simpler scoring sheet.

## Verdict

The skill output builds a decision system designed to minimize common hiring biases: independent scoring before group discussion, mandatory disconfirming evidence, signal weighting by source reliability, and criteria locked before evaluation begins. The baseline is a well-crafted hiring kit with practical tools, but the skill pack's systematic bias-reduction and evidence-tracing give it a clear edge for a high-stakes founding hire.

## With Skill Output

<details>
<summary>Expand full output (~18k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~13k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
