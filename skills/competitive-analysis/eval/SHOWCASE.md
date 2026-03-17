# Showcase: Competitive Analysis

> Demonstrates the value of the `competitive-analysis` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `competitive-analysis`. Product: SOC2 automation for startups. ICP: CTOs at 50-500 employee SaaS. Decision: reduce losses to Vanta. Known alternatives: Vanta, Drata, in-house spreadsheets, consultants. Output: Competitive Analysis Pack + battlecard for Vanta.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 5 sections (market overview, profiles, battlecard, recommendations) in a flat layout | 9 numbered sections following a systematic workflow: context snapshot, alternatives map, landscape table, JTBD criteria, positioning hypotheses, win/loss themes, battlecards, recommendations, monitoring plan |
| Completeness | Covers competitor profiles and a Vanta battlecard well; misses formal alternatives map, customer decision criteria framework, and monitoring plan | Full competitive alternatives map including status quo, workarounds, non-consumption; JTBD-framed decision criteria; 4 battlecards; monitoring plan with signals and cadence |
| Actionability | Recommendations are grouped by time horizon (short/medium/long) but lack explicit ties to win themes or loss risks | 10 recommendations each tied back to specific win themes or loss risks; monitoring plan assigns owners and update triggers |
| Specificity | Provides specific talk tracks and discovery questions for the Vanta battlecard; competitor profiles are solid but lack a structured comparison matrix | Customer decision comparison matrix with per-alternative ratings; 3 positioning hypotheses each naming a specific alternative with proof-point placeholders and tradeoffs |
| Quality gates | No self-assessment or rubric | Full quality gate checklist (7 categories) plus a rubric scoring 24/30 with dimension-level notes |

## Key Differences

1. **Systematic alternatives mapping.** The skill output maps 8 alternatives across 6 categories (status quo, workaround, analog, direct, indirect, non-consumption) and identifies the true deal alternative. The baseline jumps directly to competitor profiles without this structured taxonomy, missing the spreadsheet and do-nothing competitors that often account for "no decision" losses.

2. **Customer-framed decision criteria.** The skill output frames 9 decision criteria as JTBD outcomes (e.g., "How fast can I get audit-ready?") with a comparison matrix across all alternatives. The baseline lists competitor dimensions in a table but frames them from the vendor's perspective rather than the buyer's.

3. **Positioning hypotheses with tradeoffs.** The skill output provides 3 distinct positioning hypotheses, each naming a specific alternative, target segment, and explicit tradeoffs/non-goals. The baseline offers positioning recommendations but without the hypothesis-driven structure that makes them testable and debatable.

4. **Battlecard depth and coverage.** The skill output produces 4 battlecards (Vanta, Drata, DIY, consultants) with do/don't talk tracks, objection tables, and traps to avoid. The baseline provides a strong Vanta battlecard with discovery questions and competitive traps, but covers only Vanta in detail.

5. **Monitoring and sustainability.** The skill output includes a monitoring plan with 7 signal types, sources, cadence, owners, and update triggers. The baseline ends with a one-line note to refresh quarterly, providing no mechanism to keep the analysis current.

## Verdict

Both outputs demonstrate strong competitive analysis capability, but the skill pack enforces a more systematic and comprehensive methodology. The baseline produces a solid Vanta battlecard suitable for immediate sales use, while the skill output delivers a complete competitive intelligence operating system -- from alternatives taxonomy through monitoring -- that is more durable and decision-useful for the full range of stakeholders (sales, product, marketing).

## With Skill Output

<details>
<summary>Expand full output (~39k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~16k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
