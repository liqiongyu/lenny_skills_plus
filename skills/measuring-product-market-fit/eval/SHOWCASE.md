# Showcase: Measuring Product Market Fit

> Demonstrates the value of the `measuring-product-market-fit` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `measuring-product-market-fit`. Product: SOC2 compliance automation for startups. Stage: early PMF. Segments: founders doing it themselves vs compliance leads at 200-500 employee companies. Data: 6-month cohorts, onboarding funnel, and in-app survey. Decision: whether to double down on founders vs move upmarket. Output: a PMF Measurement Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 10 sections: executive summary, segment definitions, PMF framework (5 methods), survey design, cohort analysis framework, decision framework with scoring matrix, implementation roadmap, ongoing tracking, risks, and summary | 8 sections: context snapshot, PMF measurement model, Sean Ellis survey instrument + results, behavioral evidence (retention + engagement), reference/advocacy evidence log, PMF scorecard + diagnosis, action plan, and risks/open questions |
| Completeness | Comprehensive framework covering Sean Ellis, retention, onboarding funnel, engagement depth, and revenue/willingness-to-pay metrics; includes a weighted scoring matrix and decision rules for 4 outcomes | Provides completed analysis with actual results data (survey scores, retention curves, engagement frequency, onboarding funnel conversion rates) and a definitive recommendation; includes 8 named reference customers with verbatim quotes |
| Actionability | Primarily a measurement plan -- tells you what to measure and how, with checklists for each phase; does not provide results or a recommendation | Provides a completed PMF diagnosis with a clear recommendation ("double down on Founder-DIY"), 5 prioritized actions with hypotheses, leading/lagging indicators, owners, and timeboxes |
| Specificity | Segment definitions are detailed; survey questions include segment-specific additions; decision rules are well-specified ("double down on founders if Sean Ellis 40%+ and retention flattens") | Segment-specific results are quantified: Founder-DIY at 46.4% VD (n=112), Compliance Lead at 10.7% VD (n=56); retention curves per segment (Founder-DIY M6=50%, Compliance Lead M6=15%); activation funnel gaps quantified (Compliance Lead: 28% reach first evidence run vs 64% for Founders) |
| Quality gates | No formal quality assessment | 7-category checklist plus a 7-dimension rubric scoring 14/14 |

## Key Differences

1. **Completed analysis vs. measurement plan.** The most fundamental difference: the skill output provides a completed PMF measurement with actual data, analysis, and a definitive recommendation. The baseline provides an excellent framework for how to measure PMF but stops before producing results. For a decision-maker needing to act within 30 days, the skill output is immediately actionable.

2. **Triangulation with real evidence.** The skill version triangulates three evidence types (survey scores, behavioral data, reference customers) per segment, with specific numbers and quotes. It shows how the signals converge (Founder-DIY: strong on all three) or diverge (Compliance Lead: weak on all three). The baseline describes triangulation as a methodology but does not demonstrate it with data.

3. **Root cause analysis of segment differences.** The skill output diagnoses why Compliance Leads lack PMF through 4 structural root causes: product gap (SOC2-only when they need multi-framework), integration gap (no GRC stack integration), activation gap (18.5-day median to first value vs 2.8 days for founders), and value misalignment ("replace consultants" is irrelevant to people who are the compliance team). The baseline identifies the importance of segment differences but does not diagnose root causes.

4. **Reference customer evidence with verbatim quotes.** The skill version includes 8 named reference customers with specific evidence types, verbatim benefit statements, dates, and willingness to go public. This makes the PMF assessment tangible: Founder-DIY has 6 strong advocates with revenue-linked language, while Compliance Lead has 2 lukewarm references with caveats. The baseline does not include reference evidence.

5. **Drift triggers and re-measurement cadence.** The skill output defines 6 specific drift triggers (e.g., "VD% drops below 35%," "M3 retention drops below 45%," "net new signups decline >20% MoM for 2 consecutive months") that force immediate re-measurement. The baseline recommends quarterly re-measurement but without trigger-based urgency.

## Verdict

The baseline is an excellent measurement framework that would serve a team well in planning their PMF analysis. The skill-guided output leaps ahead by providing the completed analysis itself, with segment-specific data, triangulated evidence, root cause diagnosis, and a clear strategic recommendation. This difference is particularly impactful given the prompt's 30-day decision timeline -- the skill version delivers the answer, not just the methodology.

## With Skill Output

<details>
<summary>Expand full output (~30k)</summary>

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
