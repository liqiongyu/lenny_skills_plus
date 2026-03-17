# Showcase: Prioritizing Roadmap

> Demonstrates the value of the `prioritizing-roadmap` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `prioritizing-roadmap`. Product: Team collaboration SaaS. ICP: 10-200 person tech companies, team leads. Decision: Pick Q2 roadmap themes and top 8 initiatives in 2 weeks. North Star: weekly active teams completing >=1 project. Constraints: 6 engineers, 1 designer; must complete SSO launch; platform migration dependency in May. Stakeholders: Head of Product (decider), Eng Manager, Growth PM, CS lead. We have 15 candidate initiatives from backlog, customer requests, and internal ideas. Output: Roadmap Prioritization Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 9-step process guide describing how to prioritize a roadmap (establish criteria, map constraints, score candidates, apply North Star lens, identify themes, stack rank, validate, define metrics, communicate) | 8-section Roadmap Prioritization Pack that executes the prioritization end-to-end (Context Snapshot, Season Framing, Opportunity Inventory with 15 scored items, Scoring Model, Shortlist + Parking Lot, Roadmap Draft, Decision Narrative, Risks/Open Questions) with quality-gate self-assessment |
| Completeness | Provides a complete methodology framework with scoring criteria weights, sequencing guidelines, and a 10-day decision timeline; however, the 15 initiatives are not actually named or scored -- the framework is left for the user to apply | All 15 candidate initiatives are named, described with problem statements, scored on ICE with documented assumptions, and sorted into a delivery backlog and discovery backlog; the top 8 are selected with explicit capacity allocation and a parking lot with per-item deferral rationale |
| Actionability | Delivers a reusable process that could be applied to any roadmap decision; includes an example scoring template but with placeholder values | Delivers a complete, decision-ready artifact: season framing with 5 bets and 5 non-goals, a Now/Next/Later roadmap with week-level timing, capacity allocation by theme, and 8 next steps with owners and deadlines |
| Specificity | Defines 5 weighted scoring criteria and a 1-5 scale; suggests 3 themes as a framework but notes that specific initiatives need to be applied by the team | Defines ICE scales with concrete anchors (e.g., Impact 5 = ">10% lift in North Star within the quarter"), scores all 15 initiatives with common-currency impact ranges, and makes explicit tradeoff decisions (e.g., "activation over enterprise expansion" and "many small wins over one big bet") |
| Quality gates | No self-assessment; notes 4 areas the plan does not cover | Includes a quality-gate checklist across 7 dimensions plus rubric scores for 9 categories; "Think Bigger" section proposes 3 big bets with discovery next steps to prevent incrementalism |

## Key Differences

1. **Process guide vs. executed artifact.** The most fundamental difference: the baseline delivers a methodology for how to prioritize a roadmap but does not actually do it. It provides scoring criteria, a sequencing framework, and a 10-day timeline for the team to follow. The skill-guided output executes the entire prioritization, producing a complete, decision-ready artifact with all 15 initiatives scored and the top 8 selected with rationale.

2. **Season framing and narrative.** The with-skill output opens with a "Season of Activation Reliability" framing that explains why these priorities matter now, backed by specific evidence (40% funnel drop at "create first project," 30% support ticket spike, 5 enterprise deals blocked on SSO). The baseline suggests identifying themes but does not produce the strategic narrative that connects priorities to business context.

3. **Opportunity inventory with evidence tagging.** The skill-guided output tags each of 15 initiatives with a conviction level (Known, Belief, Hypothesis), evidence quality, and whether it belongs in a delivery or discovery backlog. The baseline recommends scoring and validation but does not differentiate between initiatives that are ready to commit to and those that need discovery first.

4. **Explicit tradeoff communication.** The with-skill output includes a "Key Tradeoffs Made Explicit" section naming 3 tradeoffs (activation over enterprise expansion, many small wins over one big bet, designer bottleneck shapes sequencing) and a "Non-Goals" section listing 5 things the team is explicitly not doing. The baseline recommends communicating what was deprioritized but does not produce the tradeoff narrative.

5. **"Think Bigger" ideas.** The skill-guided output includes 3 "big bet" ideas (instant team setup, collaboration multiplier, integration-first onboarding) with "what we'd need to believe/learn" and specific discovery next steps. This prevents the roadmap from being purely incremental. The baseline does not include a mechanism for ensuring ambitious ideas are captured alongside near-term priorities.

## Verdict

These two outputs serve fundamentally different purposes. The baseline is a strong process guide that teaches a team how to prioritize -- useful if the team needs to learn the methodology. The skill-guided output is an executed prioritization pack that delivers the actual roadmap decision with all 15 initiatives scored, the top 8 selected, tradeoffs articulated, and next steps assigned. For a team that needs a decision-ready artifact in 2 weeks, the skill-guided output is dramatically more useful; for a team building a repeatable process, the baseline's framework has standalone value.

## With Skill Output

<details>
<summary>Expand full output (~34k)</summary>

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
