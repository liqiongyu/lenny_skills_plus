# Showcase: Setting OKRs Goals

> Demonstrates the value of the `setting-okrs-goals` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Set quarterly OKRs for Growth. Teams keep arguing about conversion rate vs volume.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6-step advisory framework: diagnose, recommended OKRs, resolve conflict, common pitfalls, filled-in example, presentation guidance | 6-section pack: context snapshot, alignment map, OKR tables with per-KR detail, metric robustness analysis, systems/habits plan, review + grading plan, risks/open questions |
| Completeness | Covers the conceptual framework well with 3 objectives and a conflict resolution strategy, but KRs use placeholder variables (X, Y, Z) and lack operational detail | Complete operational OKR system: 7 KRs with baselines, targets, owners, data sources, anti-gaming notes, guardrails, plus weekly/mid-cycle/end-of-cycle review cadences |
| Actionability | Provides a template and filled example but requires significant customization; weekly leading indicators mentioned but not defined in the OKR tables | Immediately executable: every KR has a named Amplitude event, a specific owner, and a data source; 6 default-on systems with cadences and artifact outputs |
| Specificity | Generic framework adaptable to many companies; specific example uses illustrative numbers but doesn't address the rate-vs-volume tension at the metric design level | Directly resolves the rate-vs-volume tension through metric architecture: absolute counts as primary KRs, rates as supporting KRs with denominator guardrails, and an explicit resolution framework |
| Quality gates | Mentions pitfalls to avoid and leading indicators conceptually | Full checklist (7 categories, 30+ items) + 10-dimension rubric; per-KR failure mode table with detection mechanisms |

## Key Differences

1. **Rate vs. volume resolution at the metric level.** The skill output resolves the core tension architecturally: absolute activated users is the North Star, rates are supporting metrics paired with denominator guardrails, and a dedicated section explains the design principle. The baseline acknowledges the tension and proposes a "hold both in productive tension" framework, but doesn't build anti-gaming safeguards into the KR definitions themselves.

2. **Anti-gaming and metric robustness.** The skill output includes a per-KR failure modes table identifying specific gaming vectors (e.g., narrowing sign-up criteria to boost activation rate) with detection mechanisms and guardrails. The baseline mentions the risk of optimizing one metric at the expense of another but doesn't embed protections into the KR specifications.

3. **Operational review cadence.** The skill output defines a complete learning loop: weekly 45-minute reviews with a 4-part agenda, mid-cycle checkpoint rules (what changes are allowed vs. not), and end-of-cycle grading with a 0.0-1.0 scoring method. The baseline recommends weekly growth reviews but provides no structured agenda, checkpoint rules, or grading methodology.

4. **Systems and habits plan.** The skill output specifies 6 default-on systems (full-funnel metrics review, experiment pipeline review, session recording review, paid channel audit, cross-team standup, spend reconciliation) each with cadence, owner, and artifact output. The baseline has no equivalent operational layer between the OKRs and day-to-day execution.

5. **Assumption and context management.** The skill output explicitly labels assumptions, flags evidence gaps (baselines need confirmation, budget needs CFO sign-off, "activated user" definition may not exist), and assigns owners with due dates. The baseline presents a cleaner, more polished document but does not surface the unknowns that could invalidate the targets.

## Verdict

The baseline provides a thoughtful advisory framework for resolving the conversion-vs-volume debate and offers a solid OKR template. The skill-guided output goes further by embedding the resolution into the metric architecture itself, adding anti-gaming safeguards, and building the operational infrastructure (review cadences, systems, grading) needed to make OKRs work in practice. The difference is most pronounced in metric robustness and operational readiness.

## With Skill Output

<details>
<summary>Expand full output (~24k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~11k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
