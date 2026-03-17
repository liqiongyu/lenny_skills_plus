# Showcase: Retention Engagement

> Demonstrates the value of the `retention-engagement` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `retention-engagement`. Product: meditation and mindfulness app (B2C subscription). Segment: paid subscribers ($9.99/month). Baseline: D30 paid retention is 22%, with a clear engagement cliff after week 2 (daily sessions drop from 4.2 to 1.1). We have push and in-app channels only (no email). Constraint: 4-week sprint, 1 PM + 2 engineers, no major app redesign allowed. Create a Retention & Engagement Improvement Pack with a diagnosis naming the primary failure mode, an aha-moment definition tied to observable behavior, 6-8 experiment cards (e.g., streak mechanics, personalized session recommendations, 'resume your plan' entry point), a measurement plan with specific events and dashboard specs, and a 30/60/90 execution plan. Output: Retention & Engagement Improvement Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7 sections: diagnosis, aha-moment, 8 experiment cards, measurement plan, 30/60/90 execution, prioritization, risks | 9-section canonical structure: context snapshot, metric definitions + guardrails, diagnosis with cohort snapshot, activation/aha definition with validation plan, lever hypotheses map, prioritized experiment backlog with ICE scoring, measurement + instrumentation plan, 30/60/90 execution plan, and risks/open questions |
| Completeness | Diagnosis covers 5 root causes; aha-moment has 3 components; 8 experiments with field tables; measurement plan with instrumentation and dashboards | Diagnosis includes 2-segment cohort analysis with estimated baselines, onboarding drop-off funnel, 5 candidate aha behaviors evaluated against retention, chosen activation definition with validation plan and decision rule, 8 hypotheses mapped to failure modes, and 6 detailed experiment cards |
| Actionability | 30/60/90 plan has weekly task tables with owners; experiments have field tables with audience, duration, effort, and risk | Each experiment card includes hypothesis statement, success metric, leading indicators, guardrails, required instrumentation events, rollout plan, rollback plan, and expected decision date; 30/60/90 plan is dependency-sequenced |
| Specificity | Aha-moment requires 5 program sessions + 1 reflection in 14 days; metrics table has current/target columns | Aha-moment requires 3 distinct days with sessions in 7 days; 5 metric definitions with exact behavior, segment, window, baseline, target, and data source; 6 dashboards specified with audience and refresh frequency |
| Quality gates | 5 risks with likelihood/impact/mitigation | Full checklist (20+ items covering problem fit, input contract, metric clarity, diagnosis quality, aha definition, insight-to-action mapping, experiment design, prioritization, execution plan, safety/trust) plus rubric (20/20) |

## Key Differences

1. **Segment-level diagnosis with cohort estimates.** The skill output analyzes two segments separately (activated paid users vs. unconverted paid users) with estimated D1/D7/D30/WAU metrics for each, identifies the biggest leak (activated users x week 2-3 transition), and names the primary failure mode (engagement decay) and secondary (activation failure). The baseline provides a single-segment diagnosis without distinguishing failure modes by segment.

2. **Activation definition with validation protocol.** The with-skill output evaluates 5 candidate aha behaviors against retention, selects one (3 distinct days in 7 days), specifies a retrospective validation plan with a decision rule ("if separation is less than 15pp, revise"), and lists 4 required tracking events. The baseline proposes a more complex aha-moment (5 program sessions + 1 reflection in 14 days) without a formal validation protocol or decision rule for revision.

3. **Lever hypotheses map connecting diagnosis to experiments.** The skill output includes an explicit mapping table connecting each failure mode to a lever, hypothesis, leading indicator, and experiment ideas before presenting the experiment cards. The baseline goes directly from diagnosis to experiment cards without this intermediate mapping.

4. **ICE scoring for transparent prioritization.** The skill output scores all 8 experiments on Impact, Confidence, and Effort, producing a transparent rank order. The top recommendation (post-first-session reminder prompt, score 20.0) is clearly justified by its high confidence and low effort. The baseline prioritizes by ship date and effort but without a formal scoring framework.

5. **Push notification frequency governance.** The skill output identifies push fatigue as a specific risk (running 3 push experiments simultaneously) and prescribes a frequency cap (max 1 push/day per user across all experiments). The baseline flags push fatigue but handles it less specifically (cap at 1 push/day without cross-experiment coordination).

## Verdict

Both outputs are strong retention plans with well-designed experiments. The skill-guided output excels in diagnostic rigor (segment-level analysis, failure mode identification, validated activation definition) and operational discipline (ICE scoring, lever mapping, push frequency governance). The baseline provides more experiments (8 vs 6 detailed cards) and a slightly more granular weekly execution table. The key advantage of the skill output is its structured connection from diagnosis through activation definition through lever hypotheses to prioritized experiments, making the logic chain from insight to action transparent and auditable.

## With Skill Output

<details>
<summary>Expand full output (~40k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~22k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
