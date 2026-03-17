# Showcase: Product Operations

> Demonstrates the value of the `product-operations` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `product-operations`. 8 PMs, rapid shipping, stakeholders complain about "no visibility" and surprise launches.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8 sections covering problem diagnosis, operating model, launch tiering, checklists, launch calendar, roles, tooling, implementation roadmap | 8-section canonical structure with context snapshot, charter with non-goals, RACI, cadence calendar with ritual specs, artifact library with templates, insights pipeline, release enablement system, and 30/60/90 implementation plan |
| Completeness | Covers roadmap tool, communication cadences, launch tiering, checklists, roles, and implementation phases; missing insights pipeline, decision log, post-launch capture, and explicit charter boundaries | Includes full charter with engagement model, 5 rituals each with output artifacts, insights pipeline (intake-triage-routing-reporting), decision log stewardship, post-launch capture, and explicit non-goals |
| Actionability | Implementation roadmap spans 4 phases (foundation through ongoing) with checklists but no measurable targets or named pilot areas | 30/60/90 plan with named pilot area, 5 metrics with baselines and targets, iteration loop at weeks 4/8/12, and specific day-level next steps |
| Specificity | Launch tiering has 3 tiers with examples and coordination requirements; RACI table covers Tier 1 launches in appendix | 3-tier release system with specific lead times (5 vs 10 business days), full RACI for 7 operational areas, 5 ritual specs each with purpose/inputs/agenda/decisions/output |
| Quality gates | No self-assessment or quality verification | Full rubric self-assessment (10/10) across 5 dimensions covering charter clarity, operating model, cadence quality, insights pipeline, and implementation |

## Key Differences

1. **Charter with explicit boundaries and engagement model.** The skill output defines a Product Ops charter with mission, scope, non-goals ("does not own product strategy or PRDs"), an engagement model (intake channel, prioritization, SLAs), and 5 measurable success criteria. The baseline defines the Product Operations Lead role but does not establish a formal charter or engagement model.

2. **Insights pipeline from intake to action.** The with-skill output specifies a complete feedback pipeline with 5 sources, a taxonomy (theme, segment, severity, evidence type, product area), a 4-stage workflow (intake, triage, routing, reporting), and a decision path for routed insights. The baseline does not address how customer/stakeholder feedback gets processed and routed to PMs.

3. **Ritual specifications tied to artifacts.** Each of the 5 rituals in the skill output has a detailed spec (purpose, inputs, agenda, decisions made, output artifact, follow-ups). The baseline describes meeting cadences and their content but does not systematically tie each ritual to a specific output artifact with a definition of done.

4. **Post-launch capture and iteration.** The skill output includes a post-launch capture process for Tier 2/3 releases (Day 3 async check-in, Day 14 retro) producing process improvement actions. The baseline mentions post-launch retrospectives for Tier 1 only in the optimization phase without specifying a structured capture process.

5. **Measurement plan with baselines.** The skill output defines 5 metrics (stakeholder surprise score <10%, ad-hoc requests reduced 50%, enablement coverage 100%, PM satisfaction >70%, ritual adoption >80%) with measurement methods and baselines. The baseline lists success metrics (0 surprise launches, 100% checklist completion) but without current baselines or measurement methods.

## Verdict

The skill-guided output provides a more complete operating system with stronger charter boundaries, a missing-from-baseline insights pipeline, and tighter ritual-to-artifact connections. The baseline is practical and well-organized but reads more as an implementation checklist than a full operating model. The key differentiator is that the skill output addresses the entire Product Ops lifecycle (intake, processing, decision-making, enablement, measurement) while the baseline focuses primarily on communication and launch coordination.

## With Skill Output

<details>
<summary>Expand full output (~26k)</summary>

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
