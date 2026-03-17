# Showcase: Analyzing User Feedback

> Demonstrates the value of the `analyzing-user-feedback` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `analyzing-user-feedback`. Context: B2B SaaS. Area: onboarding + activation. Decision: what to fix in the next 2 sprints. Sources: last 90 days of support tickets (redacted excerpts) + churn survey comments. Segments: SMB vs Mid-market. Output: a User Feedback Analysis Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Executive summary, methodology, 5 themes, quantitative summary, recommendations, metrics, risks | Context snapshot, source inventory, codebook with 12 themes, normalized feedback table (25 items), theme reports, ranked recommendations, feedback loop plan, quality self-assessment |
| Completeness | 5 themes with segment breakdown, churn correlation, sprint recommendations | 12 codebook themes with definitions/includes/excludes, 25 individually tagged feedback items, 9 detailed theme reports with confidence ratings, sprint allocation, and open questions with answer plans |
| Actionability | 5 recommendations with expected impact and success metrics | 10 ranked actions with specific owners, sprint allocation, evidence links, and 5 open questions each with fastest-way-to-answer plans |
| Specificity | Representative quotes are illustrative patterns; metrics are estimated ranges | Each feedback item has an ID, source, date, segment, severity, root cause type; themes include frequency percentages and confidence levels |
| Quality gates | Appendix with data confidence notes | Full rubric self-assessment (27/30) with checklist across 6 dimensions; explicit data-synthesized caveat |

## Key Differences

1. **Codebook rigor.** The skill output builds a formal 12-theme taxonomy with definitions, includes/excludes, examples, severity scales, root cause types, and tagging rules before any analysis begins. The baseline groups feedback into 5 broad themes using bottom-up affinity mapping without a reusable codebook, making the analysis harder to reproduce or extend.

2. **Individual feedback traceability.** The skill output includes a normalized table of 25 individually tagged items with item IDs, sources, dates, segments, and severity scores, creating an auditable evidence chain from raw data to recommendations. The baseline presents aggregated patterns without traceable individual items.

3. **Feedback loop design.** The skill output dedicates a full section to sustaining the analysis with daily tagging cadence, biweekly reviews, engineering rotation, and explicit storage/query plans. The baseline mentions tracking but does not define an operating model for ongoing feedback analysis.

4. **Bias and confidence transparency.** The skill output explicitly rates confidence per theme (High/Medium-High/Medium), acknowledges synthesized data limitations, and calls out silent-churner and mid-market underrepresentation biases. The baseline notes sample limitations in an appendix but does not rate confidence per finding.

5. **Open questions with resolution plans.** The skill output lists 5 specific unknowns with the fastest way to answer each and what data is needed, creating a learning plan alongside the action plan. The baseline recommends supplementing with qualitative interviews but does not structure the unknowns as resolvable questions.

## Verdict

The skill output produces a more rigorous and sustainable analysis framework -- the codebook, tagged feedback table, and feedback loop mean the work compounds over time rather than being a one-off report. The baseline is a solid executive briefing with good recommendations, but the skill version is better suited for teams that need to run this analysis repeatedly and trace decisions back to evidence.

## With Skill Output

<details>
<summary>Expand full output (~43k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~19k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
