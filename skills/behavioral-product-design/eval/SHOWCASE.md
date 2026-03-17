# Showcase: Behavioral Product Design

> Demonstrates the value of the `behavioral-product-design` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `behavioral-product-design`. Users abandon checkout at shipping. Support tickets mention "not sure when it arrives" and "returns are unclear".

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Diagnosis, 5 interventions, roadmap, measurement, risks, theoretical summary | Context snapshot with baseline metrics, target behavior spec, journey map, behavioral diagnosis table, 10 interventions mapped to mechanisms, 3 prioritized bets with full design specs, experiment plan with instrumentation |
| Completeness | Covers behavioral principles and design ideas broadly; 3-phase roadmap | Adds explicit target behavior definition, guardrail metrics, detailed UX copy/states/accessibility for each spec, rollout/rollback plans with stop-the-line triggers, and 12 instrumentation events |
| Actionability | Interventions described conceptually with effort/impact ratings | Each top bet has a full design spec with UX copy drafts, edge-case states, accessibility requirements, and a feature-flag rollout plan an engineer could implement |
| Specificity | References behavioral science theory with citations (Ellsberg, Kahneman, etc.) | Maps each intervention to a specific journey step, names the behavioral mechanism, states a quantified hypothesis (e.g., "+5-8 pp"), and defines measurement events by name and properties |
| Quality gates | None explicit | 5-section checklist (target behavior, diagnosis, intervention quality, ethics/trust, experiment readiness) plus a 27/30 rubric self-score |

## Key Differences

1. **Target behavior precision.** The skill output defines a specific, observable, measurable target behavior ("complete shipping step within 3 minutes") with a numeric baseline (~45%), target (+10 pp), and 4 guardrail metrics. The baseline identifies the problem area but does not define a precise behavioral target or guardrails.

2. **Design spec depth.** The skill output provides implementation-ready specs for each top bet, including UX copy drafts, component states (loading, success, error, address-not-entered), accessibility annotations, and rollback plans. The baseline describes interventions conceptually and assigns effort/impact ratings but leaves implementation details to the reader.

3. **Experiment rigor.** The skill output defines a multi-variant A/B test with 12 named instrumentation events (each with typed properties), sample size considerations, a 2-week minimum duration, and a ship/iterate/kill decision rule. The baseline recommends A/B testing in a later optimization phase without defining the experiment structure.

4. **Ethics integration.** The skill output embeds ethical controls into each spec (transparency about delivery date accuracy, honest scarcity framing, default selection based on customer value not revenue). The baseline addresses ethics in a risks section but does not weave controls into the design specs themselves.

5. **Theoretical grounding vs. applied mechanism.** The baseline provides a rich theoretical foundation (10 named behavioral principles with citations), which is educational. The skill output trades some theoretical breadth for tighter mechanism-to-intervention mapping, where each design decision explicitly names which bias it addresses and why, making the reasoning more auditable.

## Verdict

Both outputs demonstrate strong behavioral science knowledge. The baseline excels as a strategic brief with rich theoretical framing, while the skill output is materially closer to an implementation-ready product spec. For a team that needs to brief leadership, either works; for a team that needs to ship and measure changes next sprint, the skill output provides the spec, instrumentation, and experiment plan to do so.

## With Skill Output

<details>
<summary>Expand full output (~37k)</summary>

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
