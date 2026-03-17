# Showcase: Designing Surveys

> Demonstrates the value of the `designing-surveys` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `designing-surveys`. We're a B2B analytics tool. Decision: route new signups to the right onboarding path and prevent sales from contacting non-buyers. Survey type: onboarding profiling. Channel: in-product during first session. Constraints: keep under 2 minutes. Output: Survey Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6 sections: survey flow (4 screens), onboarding path mapping table, sales suppression rules, implementation notes, timing estimate | 7 sections: context snapshot, survey brief with hypotheses, questionnaire with rationale per question, instrument table (CSV-ready), analysis + reporting plan with routing logic and decision thresholds, launch plan + QA checklist, risks/open questions/next steps |
| Completeness | Covers survey questions, routing logic, sales suppression rules, and practical implementation notes (progressive save, revisit from settings) | Adds decision framing (what decision this informs, by when), explicit hypotheses, analysis plan with predefined segment cuts, open-ended coding plan (12-tag list), decision thresholds for different result scenarios, pilot plan, and monitoring plan |
| Actionability | Routing logic table maps segment + buyer signal to onboarding path and sales action; sales suppression rules are specific (4 rules including enrichment window) | Instrument table is CSV-ready for direct import; analysis plan includes decision thresholds (e.g., "if completion rate < 60%, shorten survey"); reporting plan defines weekly dashboard + monthly memo with specific audiences |
| Specificity | 6 questions across 4 screens with conditional logic (Q6 only for mid-market+); includes multi-select for current tools; provides screen-by-screen time estimates | 5 questions across 3 screens with randomization rules specified per question (randomize non-ordinal lists, do not randomize ordinal); routing logic table maps Q04 x Q02 combinations to 4 segments with specific sales actions |
| Quality gates | No self-assessment | Full quality gate (7 checklists) plus rubric scoring 4.6/5 average |

## Key Differences

1. **Decision-anchored design.** The skill output opens with a context snapshot naming the specific decision ("route new signups and suppress sales outreach to non-buyers"), a deadline ("within 2 weeks of pilot completion"), and success criteria (completion rate >= 75%, routing accuracy >= 85%, sales non-buyer outreach reduced >= 50%). The baseline describes the purpose but without explicit success criteria or a timeline.

2. **Question design rationale.** The skill output includes a rationale column for every question explaining why it is asked and how it feeds into routing. The baseline provides routing logic per question but without explaining why each question was chosen over alternatives, making it harder to evaluate whether the right questions are being asked.

3. **Analysis and reporting plan.** The skill output provides predefined segment cuts, an open-ended coding plan for the free-text question (12 tags with coding rules), and decision thresholds for different result scenarios (e.g., "if > 40% are individual ICs, validates hypothesis that sales is over-contacting"). The baseline provides routing rules but no plan for analyzing the aggregate data or making decisions based on result patterns.

4. **Pilot and QA methodology.** The skill output includes a pilot plan (50-100 signups, 4 specific review criteria including drop-off by screen and "Other" response rates), a launch schedule (5-day ramp), and monitoring targets (completion rate, drop-off watchpoints, segment mix). The baseline includes implementation notes (progressive save, skip option) but without a structured pilot or monitoring plan.

5. **Survey instrument rigor.** The skill output specifies randomization rules per question (randomize Q01 and Q03 options to reduce primacy bias; do not randomize Q02 and Q04 because they are ordinal), mobile layout constraints (max 6 options, vertical layout), and a screen-by-screen layout recommendation. The baseline has a well-designed flow but without explicit bias-reduction measures.

## Verdict

The baseline produces a more immediately shippable survey with practical implementation details (progressive save, conditional logic, enrichment window). The skill pack produces a more methodologically sound survey instrument with explicit decision framing, bias-reduction measures, a structured pilot plan, and an analysis plan that ensures the data actually drives the routing decisions it was designed to inform. The skill output's routing logic table (Q04 x Q02 matrix) is simpler and arguably more robust than the baseline's multi-variable routing, while the baseline's additional question (current tools) provides useful competitive intelligence.

## With Skill Output

<details>
<summary>Expand full output (~20k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~6k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
