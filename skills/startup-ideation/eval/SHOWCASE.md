# Showcase: Startup Ideation

> Demonstrates the value of the `startup-ideation` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `startup-ideation`. We're 2 founders: ex-ops managers in logistics + a PM from warehouse software. Constraints: 3 months runway, can do sales calls, prefer B2B SaaS. Decision: pick 1 idea to validate in 14 days. Output: Startup Ideation Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 12-section document: founder-market fit, 5 ideas, scoring matrix, recommendation, 14-day validation plan, competitive landscape, MVP scope, unit economics, GTM playbook, risk register, decision log, key metrics | 9-section pack: context snapshot, unfair advantages + 10 signals, shift scan (12 "why now" shifts), 20-idea opportunity table, tarpit/differentiation check, scorecard (top 5), top idea brief (1-pager), 2-week validation plan with stop/pivot rules, risks/open questions/next steps |
| Completeness | Covers the full startup journey from ideation through MVP spec and 90-day GTM; includes unit economics model, cold outreach template, and discovery call script | Covers ideation with exceptional depth: 10 operator signals, 12 shift categories, 20 ideas evaluated, 9 pruned via tarpit check, top 5 scored on 8 weighted criteria, with a designated pivot idea |
| Actionability | Very actionable for the chosen idea: includes clickable prototype spec, discovery call script, cold outreach template, and pivot playbook | Actionable at the decision level: each of 20 ideas has a "first test (48h-2w)" column, the validation plan has daily milestones with stop/pivot rules at Day 7 and Day 14, and the pivot target (Idea #1) is pre-selected |
| Specificity | Specific to dock scheduling: names competitors (C3 Reservations, Opendock, Manhattan), estimates ACV ($6-24K), and describes the MVP feature set | Specific to freight invoice audit: names the LLM capability shift, quantifies the pain ($100K-2.5M/yr in overcharges), identifies the mid-market gap vs. enterprise incumbents (Cass, CTSI), and specifies gain-share pricing (25-30%) |
| Quality gates | Go/no-go criteria at Day 7 (problem validation) and Day 13 (solution validation) with numeric thresholds | 8-category quality checklist (opportunity thesis, Why Now, off-the-beaten-path, tarpit, scorecard, brief, validation, final pack) + 5-test validation plan with per-test pass/fail/pivot criteria |

## Key Differences

1. **Idea generation breadth and pruning rigor.** The skill output generates 20 opportunity theses from 10 operator-observed signals, then systematically prunes 3 (discarded), parks 8 (interesting but not best fit), and scores the remaining 9 down to a top 5. The baseline generates 5 ideas and scores them on a simpler matrix. The wider funnel with explicit tarpit checks produces higher confidence that the best idea wasn't missed.

2. **"Why Now" analysis depth.** The skill output dedicates an entire section to 12 categorized shifts (capability, cost, behavior, distribution, regulatory, infrastructure) that explain why these opportunities exist today and didn't 3 years ago. The baseline mentions "Why Now" for each idea but treats it as one evaluation dimension rather than a systematic scan of enabling conditions.

3. **Unfair advantage and signal sourcing.** The skill output maps 4 unfair advantages with evidence and 10 specific operator signals (with direct quotes like "Every facility I managed had a different spreadsheet for dock doors") before generating ideas. The baseline assesses founder-market fit but doesn't systematically extract signals from lived experience to seed ideation.

4. **Pivot planning.** The skill output designates Idea #1 (3PL billing reconciliation) as the pre-selected pivot target with explicit criteria for when to switch, and the sensitivity analysis between the top two ideas is documented. The baseline includes a pivot playbook (try Idea B, then D) but the alternatives weren't evaluated at the same depth as the primary choice.

5. **Validation plan specificity.** Both outputs have strong 14-day plans. The skill output structures 5 sequential tests with per-test success metrics and stop/pivot rules (e.g., "If <5 calls completed by Day 3, pivot to 3PL billing"). The baseline uses a 2-phase approach (problem validation Week 1, solution validation Week 2) with go/no-go thresholds that are clear but less granular.

## Verdict

The baseline is a more complete startup playbook -- it extends through MVP scope, unit economics, and GTM execution. The skill-guided output is a stronger ideation and decision-making tool -- it generates more ideas, applies more rigorous pruning, and produces higher confidence that the selected idea is the best option given the team's constraints. For a team with 3 months of runway making a one-shot bet, the skill output's broader search and more disciplined evaluation process is the more valuable contribution.

## With Skill Output

<details>
<summary>Expand full output (~47k)</summary>

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
