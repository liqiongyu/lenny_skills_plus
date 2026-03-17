# Showcase: Designing Growth Loops

> Demonstrates the value of the `designing-growth-loops` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're an AI onboarding assistant for HR teams at the early growth stage with some PMF in the mid-market segment. Our goal is to increase WAU by 30% in the next 90 days, focused on the mid-market segment. We have limited engineering resources (2 developers) and all tactics must be brand-safe. We believe our best growth lever is our HRIS integrations (we're listed on several HRIS marketplaces). Please design a growth loop, map the full loop mechanics, identify the key bottlenecks, and propose the first 2-3 experiments we should run.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7 sections: loop design with primary + secondary loops, 6-stage mechanics map, 3 bottlenecks, 3 experiments, 90-day roadmap, WAU impact model, key risks | 11 sections: context snapshot, loop inventory + baseline, 6 loop candidates (micro + macro), loop map with bottleneck hypotheses, channel fit triad, paid loop feasibility gate, loop scorecard, measurement + instrumentation plan, experiment backlog with win/lose/learn criteria, 30/60/90 plan, risks/open questions/next steps |
| Completeness | Covers primary and secondary loops, 3 experiments with detailed designs and kill criteria, resource allocation plan, and a WAU impact model with estimated lift per lever | Inventories 6 candidate loops (including 2 deferred and 1 gated), applies a channel fit triad, scores all candidates on 5 dimensions, provides a paid loop feasibility gate, and specifies 9 instrumentation events with properties |
| Actionability | 3 experiments with specific weekly breakdowns, engineering cost estimates (dev-weeks), and kill criteria (e.g., "+15% install rate after 4 weeks") | 6 prioritized experiments with hypotheses, leading + lagging metrics, effort estimates, timeboxes, and win/lose/learn criteria; instrumentation plan identifies 4 gaps with specific fixes and effort |
| Specificity | Experiment 2 (auto-magic setup) describes specific auto-configuration logic; Experiment 3 (hiring manager pulse) specifies email content and dashboard scope; WAU model estimates per-experiment lift | Loop scorecard scores 6 candidates on Impact/Confidence/Effort/Cycle-time/Risk with numeric totals; baseline metrics include confidence labels (low/medium/high); each instrumentation event names specific properties to capture |
| Quality gates | No self-assessment | Full quality gate (7 checklists) plus rubric scoring 15/16 with identified gap (evidence grounding at 1/2 due to missing baseline data) |

## Key Differences

1. **Systematic loop inventory.** The skill output evaluates 6 candidate loops (marketplace, referral, co-marketing, sales expansion, community, paid) with explicit go/no-go verdicts before selecting the top 2. The baseline identifies primary and secondary loops directly without exploring alternatives, which risks anchoring on the first viable option.

2. **Paid loop feasibility gate.** The skill output includes a dedicated gate check for paid acquisition that evaluates LTV, margin, CAC, and attribution readiness -- concluding "not yet viable" with 4 prerequisites before revisiting. The baseline does not evaluate paid channels, leaving a strategic question unaddressed.

3. **Instrumentation as a prerequisite.** The skill output specifies 9 events with exact property schemas (e.g., `integration_installed` with `hris_platform`, `marketplace_source`, `company_size`), identifies 4 instrumentation gaps with effort estimates, and makes instrumentation Week 1's top priority. The baseline tracks metrics but does not specify the event-level instrumentation needed to measure them.

4. **Baseline with confidence labels.** The skill output documents current metrics with explicit confidence levels (e.g., "activation rate: ~25-40%, low confidence") and flags where estimates need validation. The baseline uses a WAU impact model with estimated ranges but without labeling the confidence level of each assumption.

5. **Experiment design depth.** The baseline's experiments include more detailed product design (auto-magic setup configuration logic, hiring manager email content spec). The skill output's experiments have stronger measurement methodology (hypotheses, leading + lagging metrics, win/lose/learn criteria, dependencies). The two approaches are complementary -- the baseline is more shippable, the skill output is more measurable.

## Verdict

The baseline produces more immediately buildable experiment designs with specific product specifications and a WAU impact model. The skill output provides a more rigorous growth framework -- systematic loop evaluation, instrumentation planning, and measurement discipline -- that reduces the risk of investing engineering effort in unvalidated loops. For a 2-developer team with 90 days, the skill pack's instrumentation-first approach and paid loop gating provide essential guardrails against wasting scarce capacity.

## With Skill Output

<details>
<summary>Expand full output (~36k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~15k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
