# Showcase: Marketplace Liquidity

> Demonstrates the value of the `marketplace-liquidity` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `marketplace-liquidity`. We run an on-demand dog walking marketplace in NYC, SF, and LA. Core action: request -> booked within 10 minutes. Goal: improve booking fill rate from 55% to 75% in SF evenings within 6 weeks. Baseline: p50 time-to-book is 18 minutes, cancellation rate is 9%. Constraints: $25k/month in incentives, limited eng capacity. Output a Marketplace Liquidity Management Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 12 sections organized by workstreams (supply activation, matching speed, cancellation reduction, demand shaping) with implementation timeline and budget | 8 sections: context snapshot, liquidity definition, metric tree, local market segmentation, bottleneck diagnosis, intervention plan with 8 experiments, measurement + instrumentation plan, and operating cadence |
| Completeness | Covers a wide range of interventions (guaranteed earnings floors, auto-accept, predictive dispatch, scheduled walks, wait-time transparency) with a post-campaign sustainability plan | Covers interventions plus a formal liquidity definition, a 9-metric tree with data sources, 8-segment scorecard, bottleneck diagnosis with second-order effects (flip-flop risk, graduation problem), instrumentation gaps, and alert definitions |
| Actionability | Organized by weekly implementation with specific interventions per week; includes kill criteria ($15 cost per incremental booking) | 8 prioritized experiments each with hypothesis, segment, primary metric, guardrail metric, expected effect, effort level, and timebox; includes explicit reallocation triggers and a weekly review agenda with decision log |
| Specificity | Provides specific dollar amounts per intervention and channel-specific expected impact; daily/weekly metrics to review | Decomposes the 20pp fill rate gap into supply (~12pp), matching speed (~5pp), and cancellation recapture (~3pp); provides event definitions with key fields and data sources for instrumentation |
| Quality gates | Decision rules for lever performance with kill criteria | 9-dimension rubric scoring 18/18; 6-category checklist covering scope, metrics, fragmentation, interventions, measurement, and finalization |

## Key Differences

1. **Formal liquidity definition and metric tree.** The skill output defines liquidity as a composite (fill rate x fulfillment quality) with explicit thresholds for 6 dimensions, then builds a 9-metric tree (1 north star, 6 drivers, 3 guardrails) with data sources and segmentation capabilities. The baseline tracks similar metrics but does not define liquidity formally or structure metrics hierarchically.

2. **Local market segmentation and bottleneck diagnosis.** The skill version creates an 8-segment scorecard (city x daypart x day-type) with per-segment baselines, bottleneck labels (supply-limited vs mechanics-limited), and confidence flags. It diagnoses the primary failure mode with specific evidence signals. The baseline identifies root cause hypotheses but does not segment the market or differentiate bottleneck types per segment.

3. **Second-order effects and marketplace dynamics.** The skill output explicitly addresses flip-flop risk (reliability improvements driving demand growth that re-creates supply constraints), graduation/disintermediation risk (walkers building direct relationships), and incentive dependency. The baseline acknowledges some of these risks but does not systematically analyze marketplace dynamics.

4. **Instrumentation and event definitions.** The skill version provides 8 event definitions (request_created, offer_sent, offer_responded, etc.) with key fields, identifies 4 instrumentation gaps with remediation plans and priorities, and defines 4 alerts with specific triggers. The baseline assumes analytics infrastructure exists without specifying the event model.

5. **Operating cadence with reallocation triggers.** The skill output defines a weekly liquidity review meeting with a structured agenda (topline trend, segment deep dive, experiment readouts, reallocation decisions, quality check, commitments) and 4 explicit reallocation triggers. The baseline includes a weekly review cadence but without a formal agenda structure or trigger-based reallocation rules.

## Verdict

The baseline provides a practical, action-oriented plan with creative interventions (guaranteed earnings floor, auto-accept, scheduled walks) and a helpful post-campaign sustainability plan. The skill-guided version adds analytical rigor through its formal liquidity definition, segmented diagnosis, metric tree, instrumentation plan, and operating cadence. For a marketplace operations team, the skill version provides the diagnostic framework needed to understand why interventions succeed or fail, not just what to try.

## With Skill Output

<details>
<summary>Expand full output (~30k)</summary>

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
