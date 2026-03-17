# Showcase: Writing North Star Metrics

> Demonstrates the value of the `writing-north-star-metrics` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `writing-north-star-metrics`. B2B SaaS (team collaboration tool): - Product: Team collaboration SaaS

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Ten sections: context, metric definition, driver tree, measurement playbook, goal-setting, anti-gaming guardrails, strategic playbook, review cadence, implementation checklist, summary | Nine sections following a deliberate workflow: context snapshot, north star narrative, candidate metrics evaluation table, chosen metric spec, driver tree + guardrails, validation + rollout plan, risks, open questions, next steps |
| Completeness | Covers metric definition, four-layer driver tree, measurement instrumentation, OKR examples, benchmarking guidance, strategic playbook with 4 levers, and an implementation checklist | Covers five candidate metrics evaluated head-to-head, a full metric spec with formula/rules/exclusions/example calculation, six drivers with proxy metrics and concrete levers, five guardrails with quantitative thresholds, and a validation plan |
| Actionability | Strategic playbook names 4+ specific initiatives per lever; implementation checklist is phased (Foundation, Measurement, Operationalize, Iterate); OKR examples include current vs. target | Next steps table has 8 actions with named owners, timelines, and success criteria; decision rules specify escalation triggers ("if WATC declines for 2 consecutive weeks"); communication plan maps weekly/bi-weekly/monthly/quarterly cadence |
| Specificity | Metric defined with threshold (3+ members, 2+ collaborative actions); driver tree uses ASCII art diagram with three layers; four dashboard layouts specified (executive, product, growth) | Metric defined with formula (numerator/denominator), time window, unit, non-trivial threshold with three qualifying conditions, inclusion/exclusion rules, segmentation slices, and a worked example calculation (3,150 teams for the week of March 9-15) |
| Quality gates | No formal quality gate | Nine checklists (narrative, candidates, chosen metric, metric spec, driver tree, validation/rollout, final pack, anti-pattern scan) plus a nine-category rubric self-score |

## Key Differences

1. **Candidate metric deliberation.** The skill output evaluates five candidate metrics in a structured comparison table (WATC, TVMR, TTFTP, Collaboration Depth, Friction-Free Onboarding Rate), with each assessed on value measurement, gaming risk, controllability, and instrumentation readiness. The selection rationale explains why the chosen metric beat each alternative. The baseline output presents one metric (WACT) and lists rejected alternatives in a brief table without structured comparison.

2. **Metric specification precision.** The skill output provides a formal metric spec with numerator formula, time window (Monday-Sunday UTC), three conditions for "non-trivial" project completion, inclusion/exclusion rules (e.g., exclude single-member teams, internal/test accounts), and a worked example calculation with real numbers. The baseline output defines the metric with a component table but lacks the formal spec, exclusion rules, and worked example.

3. **Guardrail design with quantitative thresholds.** The skill output defines five guardrails with specific triggers: project quality threshold (alert below 70%, investigate below 60%), support ticket volume (not increase >15% QoQ), 30-day team churn (below 25%), invite fatigue opt-out rate (below 5%), and revenue correlation (WATC teams should have >=2x MRR). The baseline output lists six guardrails with directional thresholds (NPS > 40, spam < 2%) but less detail on escalation triggers.

4. **Validation methodology.** The skill output includes a validation section with sanity checks (does the metric move when expected?), leadingness/correlation checks (do inputs predict the outcome?), and known caveats. It specifies that WATC should predict free-to-paid conversion at >=2x and have >=30% lower 90-day churn. The baseline output includes a "When to Reconsider" section but no structured pre-launch validation plan.

5. **North star narrative and decision-settling scope.** The skill output opens with a customer value model, defines the value moment ("a team completes a non-trivial project together"), and explicitly states which decisions the metric should and should not settle. The baseline output provides a "Why This Metric" rationale but does not explicitly scope what the metric can and cannot resolve.

## Verdict

Both outputs arrive at very similar metrics (WATC vs. WACT) for the same product, validating the core insight. The skill-guided output is more rigorous in its approach: structured candidate evaluation, formal metric spec with worked example, quantitative guardrail thresholds, and a pre-launch validation plan. The baseline output compensates with a richer strategic playbook (4 levers with 4+ named initiatives each) and benchmarking guidance with industry comparisons. The skill output is better suited for a team that needs to operationalize and defend the metric choice; the baseline is useful for a team that already has buy-in and needs an execution playbook.

## With Skill Output

<details>
<summary>Expand full output (~32k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~20k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
