# Showcase: Planning Under Uncertainty

> Demonstrates the value of the `planning-under-uncertainty` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `planning-under-uncertainty`. We believe our self-serve onboarding is hurting conversion (trial-to-paid is 4% vs industry benchmark of 8-12%), but we don't know if the problem is activation UX, value demonstration, pricing page friction, or ICP mismatch. We have 1 PM, 2 engineers, and 1 designer for 6 weeks. Create an Uncertainty Planning Pack with an uncertainty map ranking the 4 hypotheses by impact and testability, an experiment portfolio (mix of qual interviews + quantitative A/B tests), a Plan v0 that commits to learning milestones (not delivery dates), a pivot triggers for each hypothesis, and a weekly cadence for reviewing results and deciding next experiments. Output: Uncertainty Planning Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8-section plan covering uncertainty map, experiment portfolio, learning milestones, pivot triggers, weekly cadence, risk register, success criteria, and next steps | 7-section Pack following a prescribed methodology (Decision Frame, Uncertainty Map, Hypotheses + Experiment Portfolio, Plan v0 with Learning Gates, Buffers/Contingencies/Triggers, Cadence + Comms, Risks/Open Questions/Next Steps) with quality-gate self-assessment |
| Completeness | Comprehensive experiment portfolio with pre-planned experiments for each root cause (activation, value, pricing, ICP); includes a "what went well" section placeholder | Decision frame explicitly defines "why now," mode (peacetime vs wartime), decision owner, success metrics, guardrails ("must not worsen"), and what is flexible vs fixed; includes 5 contingency plans (A through E) with pre-committed responses |
| Actionability | Provides a week-by-week plan with specific deliverables per team member per week; experiments are detailed with owners and success metrics | Experiments include explicit decision rules ("if >70% complete activation with guidance vs <30% baseline, build the guided flow"); 7 operational triggers with specific thresholds and pre-committed actions; stakeholder update template with fill-in-the-blank format |
| Specificity | Experiments specify statistical methods (Bayesian for low volume); pivot triggers have 9 specific conditions with clear actions; learning milestones have target dates | Each of 7 experiments has a primary signal, guardrails, segment/sample, duration, and a decision rule; uncertainty map scores 7 unknowns on confidence and impact with validation method, owner, and deadline per item |
| Quality gates | No self-assessment; success criteria table with week-by-week targets | Includes a rubric self-assessment scoring 9 dimensions; plan v0 uses learning gates as phase transitions rather than fixed delivery dates |

## Key Differences

1. **Decision frame and mode selection.** The skill-guided output opens with an explicit decision frame that names the decision type ("commit to a remediation path"), classifies the mode as "peacetime" (chronic underperformance, not acute crisis), and identifies the decision owner. The baseline jumps into the uncertainty map without framing the decision context, mode, or owner.

2. **Contingency plans with pre-committed responses.** The with-skill output defines 5 contingency plans (A through E) covering each possible outcome of the diagnosis phase, with specific deliverables and owners for each. The baseline pre-plans experiments for each root cause but does not formalize them as pre-committed contingency plans with selection criteria.

3. **Operational triggers with thresholds.** The skill-guided output specifies 7 triggers with numeric thresholds (e.g., "ICP-match conversion >= 2x non-ICP and non-ICP is >40% of trial base") and pre-committed actions. The baseline provides 9 pivot triggers but some are qualitative ("first A/B test shows no lift after 1 week") rather than threshold-based.

4. **Stakeholder communication template.** The with-skill output includes a fill-in-the-blank weekly stakeholder update template with sections for status, learnings, decisions made, decisions needed, next week's plan, and a metric snapshot. The baseline describes a weekly meeting structure but does not provide a communication artifact for stakeholders outside the core team.

5. **Buffer and scope management.** The skill-guided output explicitly defines three types of buffers (time, capacity, scope) and explains how each absorbs overruns. It also specifies that Phase 3 is scoped to a single intervention, preventing scope sprawl. The baseline mentions risk mitigation but does not formalize buffer types or scope constraints for the build phase.

## Verdict

Both outputs are strong and produce detailed experiment portfolios with clear learning milestones. The baseline is notably thorough in its experiment design, providing pre-planned experiments for each of four root causes with specific metrics. The skill-guided output adds structural rigor through its decision frame, pre-committed contingency plans, numeric trigger thresholds, and explicit buffer management. For a team navigating genuine uncertainty, the pre-committed "if X then Y" decision rules in the skill-guided output would reduce deliberation time during the program.

## With Skill Output

<details>
<summary>Expand full output (~26k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~17k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
