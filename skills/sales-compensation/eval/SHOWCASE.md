# Showcase: Sales Compensation

> Demonstrates the value of the `sales-compensation` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `sales-compensation`. We're a seed-stage B2B SaaS company selling an API monitoring tool. ACV is $15k, average sales cycle is 40 days, and we're hiring our first 2 AEs. ARR target: $600k this year (currently $50k). We have founder-led sales playbooks but no formal comp plan. Concern: we've seen early churns in the first 90 days from rushed deals. Create a Sales Comp Plan Pack with OTE/pay mix recommendations, quota-setting methodology with a 3-month ramp, commission mechanics (including an accelerator for >100% attainment), a retention-alignment addendum (clawback or holdback for 90-day churn), admin rules for edge cases (multi-year deals, expansion), and a rep-facing FAQ document. Output: Sales Comp Plan Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8 sections: executive summary, OTE/pay mix, quota methodology, commission mechanics, retention addendum, admin rules (edge cases), rep-facing FAQ, glossary | 10-section canonical structure: context snapshot with assumptions, comp philosophy (desired behaviors + anti-goals), role-to-metric mapping, OTE + pay mix with economic viability check, quota + ramp model with scenario analysis, commission mechanics (6 sub-sections), retention-alignment addendum with fairness check, admin + governance, rep-facing one-pager + FAQ, and risks/open questions/next steps |
| Completeness | OTE at $120k (55/45 split); 10% base commission rate; accelerators at 1.5x and 1.8x with 3x OTV cap; holdback mechanism; admin rules for multi-year, expansion, renewals, discounting, SPIFs, splits, and leaves | OTE at $150k (50/50 split); 27% base commission rate; accelerators at 1.5x and 2.0x with no hard cap; holdback mechanism; admin rules for multi-year, expansion, mid-period changes, departures, and leaves; plus comp philosophy, 8 assumptions with validation plans, scenario analysis (3 scenarios), and economic viability check |
| Actionability | FAQ covers 17 questions organized by topic; commission calculation examples in section 4; glossary of 12 terms | 5 worked payout examples (standard, strong, ramp, churned deal, discounted deal); rep-facing one-pager with "quick math" table; 10 FAQ questions; 30-90 day validation plan with 7 action items |
| Specificity | Quota derivation shows OTE-to-quota ratio and deals-per-month calculation; discount policy has 3 tiers with commission impact at 50% rate for >20% | Quota derivation includes top-down and bottom-up cross-check, pipeline coverage calculation (4-5x), ramp-adjusted annual total with gap analysis, and 3-scenario model showing company-level ARR under different attainment levels |
| Quality gates | Document control table and signature lines | 6-part checklist (scope, incentive alignment, economics, ramp/fairness, retention quality, operability) plus 7-dimension rubric (14/14); explicit note that the document requires legal review |

## Key Differences

1. **Comp philosophy with anti-goals.** The skill output opens with an explicit comp philosophy section listing 5 desired behaviors and 5 anti-goals (closing bad-fit customers, deep discounting, pipeline stuffing, sandbagging, complexity). This creates a testable design rationale: every plan mechanic can be traced to a desired behavior or anti-goal. The baseline states design principles in a table but does not formally separate desired behaviors from what the plan aims to prevent.

2. **Economic viability modeling.** The with-skill output includes a 3-scenario economic viability check (low/base/high attainment) showing comp cost as a percentage of AE bookings (52-73%) with a note that the ratio should improve to <30% within 18 months. It also includes a company-level scenario analysis showing total new ARR under each scenario with founder contribution. The baseline checks OTE-to-quota ratio but does not model total comp cost relative to bookings.

3. **Assumptions table with validation plans.** The skill output names 8 assumptions (win rate, discount level, gross margin, churn rate, pipeline split, ramp time, CAC payback, comp budget) with specific values used and validation plans for each. The baseline embeds assumptions in the analysis but does not catalog or validate them separately.

4. **OTE and rate calibration.** The outputs differ substantially on OTE ($150k vs $120k) and commission rate (27% vs 10%). The skill output's higher OTE reflects a 50/50 split with a $275k quota yielding a 27% effective rate. The baseline uses a 55/45 split with the same $275k quota at a 10% base rate, reaching parity through the lower OTV ($54k vs $75k). Both are defensible; the skill output positions for a more competitive hire at seed stage while the baseline is more capital-conservative.

5. **Holdback fairness check.** The skill output includes a 3-question fairness check for the holdback mechanism (Does the AE influence retention? Are there non-AE churn drivers? Is 20% proportional?) plus specific rep messaging language. The baseline explains the holdback clearly and compares it to clawback but does not perform a formal fairness assessment or provide messaging scripts.

## Verdict

Both outputs are well-designed compensation plans appropriate for a seed-stage company. The skill-guided output is stronger in plan design methodology (comp philosophy, economic modeling, assumption tracking, fairness checks) and produces a more transparent rationale chain from philosophy to mechanics. The baseline is stronger in operational coverage (expansion revenue tiers, renewal bonuses, SPIF framework, strategic discount exceptions, split deal rules) and provides more edge-case detail. A real deployment would benefit from the skill output's design rigor combined with the baseline's operational completeness.

## With Skill Output

<details>
<summary>Expand full output (~35k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~25k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
