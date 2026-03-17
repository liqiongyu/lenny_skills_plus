# Showcase: Pricing Strategy

> Demonstrates the value of the `pricing-strategy` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `pricing-strategy`. We sell analytics to finance teams. Current: $99/user/mo with a 14-day trial. Goal: increase expansion revenue without hurting retention. Motion: self-serve + sales assist. Constraints: must keep a free tier; SSO only on enterprise. Output: Pricing Strategy Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 16-section strategy document covering current state assessment, strategic principles, 4-tier structure, expansion mechanics, migration plan, trial overhaul, feature gating philosophy, pricing page positioning, sales triggers, financial modeling, competitive positioning, roadmap, metrics, and risks | 9-section Pack following a prescribed methodology (Context Snapshot, Segment Map + Value Narrative, Value Metric Options, WTP Evidence Plan, Price-Point Options + Recommendation, Conversion Mechanics Plan, Rollout + Instrumentation, Pricing Review Cadence, Risks/Open Questions) with quality-gate self-assessment |
| Completeness | Covers an exceptionally wide range including free viewer seats, PQL signal definitions, feature gating philosophy, financial modeling with break-even analysis, competitive positioning against 4 alternatives, and pricing page design recommendations | Additionally includes a WTP evidence plan with 16-26 planned customer interviews, Van Westendorp survey methodology, interview prompt scripts (copy-paste ready), 3 price-point options with comparative analysis, and a formal pricing review cadence with triggers |
| Actionability | Provides specific expansion mechanics (viewer seats, tier upgrades, add-ons, annual commitments) with per-trigger nudge messages; PQL signals with enrichment sources; migration plan with retention safeguards | Provides 5 explicit hypotheses to validate before launch, a rollout plan phased across 4 stages (internal prep, new signups, opt-in migration, full migration) with grandfathering rules and rollback playbook, and event instrumentation with 10+ specific tracking events |
| Specificity | Names specific pricing ($0/$49/$99/custom), defines 14 feature dimensions across 4 tiers, financial model projects 12-month revenue composition shift, and includes break-even conditions | Names specific pricing ($0/$79/$99/$129/custom), evaluates 3 value metric candidates with pros/cons per segment, defines add-on pricing for 4 add-ons, and provides 5 experiments with hypotheses, segments, primary metrics, and duration |
| Quality gates | No self-assessment; summary of key decisions | Includes a quality-gate checklist across 8 sections plus a rubric scoring 7 categories; pricing review cadence defines triggers to revisit sooner and required inputs for each review |

## Key Differences

1. **WTP evidence plan before commitment.** The skill-guided output includes a full willingness-to-pay validation plan with 5 hypotheses, 16-26 planned interviews segmented by customer type, Van Westendorp survey methodology, copy-paste interview prompts, and a pilot offer design. The baseline proposes specific prices and tiers without a structured plan to validate them first, which increases the risk of pricing misalignment.

2. **Price-point options with comparative analysis.** The with-skill output presents 3 pricing options (conservative, expansion-optimized, aggressive) with explicit tradeoff analysis for each, including who wins, who loses, and specific risks. The baseline presents one recommended tier structure without formally considering alternatives or articulating the risk profile of the chosen approach.

3. **Rollback playbook.** The skill-guided output includes a 6-step rollback playbook triggered by guardrail breaches (e.g., "logo retention increases by >1pp for 2 consecutive months"), specifying exactly what to pause, what to communicate, how to diagnose, and how to iterate. The baseline includes retention safeguards (90-day price protection, downgrade path) but does not formalize a rollback procedure.

4. **Conversion mechanics experimentation.** The with-skill output defines 5 specific experiments (reverse trial, annual pricing default, add-on upsell prompt, Team plan pilot, advanced analytics sampling) with hypotheses, segments, primary metrics, durations, and risk notes. The baseline describes expansion mechanics and upgrade nudges but does not frame them as testable experiments with success criteria.

5. **Financial modeling depth.** The baseline includes a distinctive financial model projecting 12-month revenue composition shift, blended ARPU changes, and break-even conditions for the free tier. The skill-guided output does not include financial modeling, which is a notable gap -- the baseline's projection that blended ARPU drops 10% while revenue per account increases 35% provides important context for the pricing decision.

## Verdict

The baseline is the more comprehensive document, covering financial modeling, competitive positioning, feature gating philosophy, and PQL signal design in detail. The skill-guided output is the more disciplined strategic artifact: its WTP validation plan, comparative price-point analysis, rollback playbook, and experiment backlog create a safer path to implementation. The baseline's financial model and the skill-guided output's WTP evidence plan complement each other -- an ideal pricing strategy would combine both.

## With Skill Output

<details>
<summary>Expand full output (~37k)</summary>

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
