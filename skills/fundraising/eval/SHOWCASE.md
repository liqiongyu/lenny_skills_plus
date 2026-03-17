# Showcase: Fundraising

> Demonstrates the value of the `fundraising` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `fundraising`. We're 2 technical co-founders building a B2B developer productivity tool that auto-generates API documentation from code. We have 8 design partners (3 actively using daily), 2 paid pilots at $500/month each, and $150k in savings as runway (about 5 months left). We want to raise $1.5-2.0M pre-seed to hire 2 engineers and 1 designer and reach 20 paying customers in 9 months. Our network includes 5 angel investors and 2 warm VC intros. Produce a full Fundraising Pack including a raise decision memo, round design, pitch narrative + deck outline with a strong first slide, an investor target list of 30 firms, outreach scripts, and a diligence prep checklist. Output: Fundraising Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7 sections (Decision Memo, Round Design, Pitch Narrative + Deck, Investor List, Outreach Scripts, Diligence Checklist, Execution Playbook) plus appendices | 8 numbered sections following a fundraising workflow: Raise Decision Memo, Round Design Brief, Pitch Narrative + Deck Outline, Investor ICP + Target List + Pipeline Tracker, Outreach Scripts, Diligence Prep, Operating Cadence, Risks/Next Steps |
| Completeness | Comprehensive coverage including round structure, 12-slide deck outline, 4-tier investor list, 6 outreach scripts, extensive diligence checklist, and execution playbook with common objections | All of the above plus falsifiable raise/don't-raise criteria, a non-VC alternatives analysis (bootstrap, delay, angel bridge), leading milestone indicators by month, and a "100 No's" resilience plan |
| Actionability | Week-by-week action plan for 10 weeks; diligence checklist organized by 8 categories with checkboxes | Day-by-day action plan for the first 14 days with specific owners per task; pipeline stages defined (8 stages) with weekly activity targets |
| Specificity | Names 10 specific VC funds with check sizes; 12-slide deck outline with talking points per slide | Names 30 specific investors tiered by warm-path proximity with fit reasons per fund; deck outline includes a 2-minute talk track and Slide 1 designed for the "strongest point first" pattern |
| Quality gates | Benchmarks appendix comparing company position to market medians | 6-category quality gate checklist plus rubric self-score of 12/12 |

## Key Differences

1. **Raise decision with falsifiable criteria.** The skill output includes explicit go/no-go criteria: "We raise if at least 2 of 5 angels commit within 4 weeks AND at least 1 design partner converts to paid during the process." It also evaluates 4 alternatives (bootstrap, delay, angel bridge, grants) with honest assessments. The baseline recommends raising but frames the analysis as arguments for/against rather than testable criteria.

2. **30-firm investor list with tiered sequencing.** The skill output provides 30 named investors organized into 3 tiers by warm-path proximity (Tier 1: warm, weeks 1-3; Tier 2: high-fit, weeks 2-5; Tier 3: additional, weeks 3-6), each with a specific fit reason and warm-path strategy. The baseline provides a similar-quality list but organizes it by investor type rather than by outreach sequence.

3. **Pitch narrative with "strongest point first."** The skill output designs Slide 1 around the strongest proof point (3 teams using daily, 2 paid without outbound) and a "why now" bullet, following the principle that investors decide in the first 30 seconds. The baseline starts with a traditional title slide and puts traction on Slide 6.

4. **Operating cadence with resilience planning.** The skill output includes a weekly fundraising dashboard, a pitch iteration log, and a "100 No's" resilience plan with pattern-detection rules (e.g., "If 3+ say 'too early,' consider the angel bridge"). The baseline includes a rules-of-engagement section and objection responses but does not build a systematic iteration and resilience system.

5. **FAQ/objection responses with follow-up artifacts.** The skill output maps each of 5 common objections to a specific follow-up artifact (metrics one-pager, market sizing slide, competitive matrix, team slide, architecture overview). The baseline provides objection responses inline but does not connect them to specific leave-behind documents.

## Verdict

Both outputs are strong, comprehensive fundraising packs. The skill output's main advantage is process discipline: falsifiable raise criteria, tiered investor sequencing, day-by-day execution plans, and a systematic feedback loop for pitch iteration. The baseline offers more raw content (more outreach script variants, a detailed diligence checklist with folder structure, market benchmarks) and would be useful as a reference alongside the skill output's operational framework.

## With Skill Output

<details>
<summary>Expand full output (~22k)</summary>

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
