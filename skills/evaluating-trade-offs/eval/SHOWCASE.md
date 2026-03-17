# Showcase: Evaluating Trade Offs

> Demonstrates the value of the `evaluating-trade-offs` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `evaluating-trade-offs`. We're a 30-person B2B SaaS company deciding whether to invest our only growth engineer for the next 2 quarters in SEO content infrastructure or paid acquisition tooling. SEO has compounding returns but slow payoff (6+ months); paid gives immediate pipeline but requires ongoing spend ($8k/month). We need to hit $200k ARR by Q4. Current ARR is $80k. Build a Trade-off Evaluation Pack with all-in cost (including eng time + opportunity cost), order-of-magnitude impact ranges for both options, a worse-first mitigation plan, and stop/continue triggers with a 6-week review date. Output: Trade-off Evaluation Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Side-by-side comparison format: Option A, Option B, comparison table, math check, decision triggers, recommendation | 8 numbered sections following a decision methodology: Trade-off Brief, Options Matrix, Cost Table, Impact Ranges, Pre-mortems, Worse-First Plan, Stop/Continue Triggers, Recommendation Memo |
| Completeness | Both options analyzed with cost estimates, impact ranges, risk profiles, and a math section checking feasibility | All of the above plus a 4th option (sequenced hybrid), explicit opportunity cost per option, "10x check" comparing options across time horizons, and pre-mortems for the top 2 options |
| Actionability | Decision triggers for choosing each option and mid-stream switching criteria | Specific stop/continue triggers with quantified thresholds, a 6-week review date with named owner, and a $2-4k manual test to de-risk the biggest assumption before committing |
| Specificity | Impact ranges with pessimistic/base/optimistic scenarios; CPL math for paid viability | 4 options scored on 8 weighted criteria; incremental cost table separating eng salary from variable costs; explicit assumptions that drive the decision, each testable |
| Quality gates | Decision triggers section with green/red signal criteria per option | Rubric self-assessment scoring 12/12 across 6 dimensions |

## Key Differences

1. **Structured decision methodology vs. comparison format.** The skill output follows a deliberate progression: frame the decision, score options against weighted criteria, calculate all-in costs with opportunity costs, estimate impact ranges, stress-test via pre-mortems, plan for the downside, and set kill triggers. The baseline provides a thorough side-by-side comparison but does not follow a formal decision methodology.

2. **Pre-mortems with cheapest validation tests.** The skill output includes specific pre-mortems for both top options ("It's Q4 and we're at $130k ARR -- what happened?") and identifies the cheapest evidence to de-risk the biggest assumption: a $2-4k manual paid campaign test before committing the engineer. The baseline identifies risks but does not suggest a low-cost validation step.

3. **Worse-first mitigation plan.** The skill output explicitly names the "worse first" path (paid acquisition creates a non-compounding channel), explains why the short-term pain is worth it, defines 6 leading indicators to watch weekly, and provides a communication plan for stakeholders. The baseline does not frame the decision through a worse-first lens.

4. **Sunk-cost reset and kill criteria.** The skill output includes a "sunk-cost reset question" to force honest reassessment at the 6-week mark, with 5 specific continue triggers and 5 specific stop triggers with quantified thresholds (e.g., "CPL exceeds $800 after 4 weeks"). The baseline provides decision triggers but frames them as initial decision criteria rather than ongoing reassessment tools.

5. **Assumption transparency.** The skill output names 3 key assumptions that drive the decision and explicitly states: "If Q4 is aspirational rather than a hard gate, the calculus shifts significantly toward SEO." The baseline reaches a similar conclusion but embeds assumptions within the analysis rather than surfacing them as decision-critical variables.

## Verdict

Both outputs reach the same recommendation (paid acquisition first) and provide strong analytical support. The skill output's advantage is methodological rigor: it forces the decision-maker through pre-mortems, assumption testing, and kill criteria that protect against confirmation bias. The baseline is an excellent analytical comparison but is more static -- it helps you make the decision today rather than building the system to revisit it at week 6.

## With Skill Output

<details>
<summary>Expand full output (~10k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~7k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
