# Showcase: User Onboarding

> Demonstrates the value of the `user-onboarding` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're a B2B team analytics tool where new admins must connect at least one integration (Slack, Jira, or GitHub) before they see any value. Our current 7-day activation rate is 12% and we need to get it to 18% by end of quarter, without reducing signup completion rate. Most users drop off during the integration setup step. We have about 5,000 new signups per month. Please produce the full onboarding redesign pack: first-30-seconds experience, first-mile milestone map, experiment backlog with prioritization, and measurement plan.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Four-part structure (first 30s, milestones, experiments, measurement) with appendices for quick wins and research | Nine-section structured pack with context snapshot, FTUE journey map, activation spec, first-30s spec, first-mile plan, measurement plan, experiment backlog, rollout plan, and risks/next steps |
| Completeness | Covers the core deliverables; milestones go to M7 (team expansion); 12 experiments with tiers; measurement plan with dashboards | Comprehensive end-to-end pack including friction log, activation definition with validation plan, instrumentation schema (16 events), full experiment cards for top 3, phased rollout, and self-assessment rubric |
| Actionability | Experiments have ICE scores and a weekly execution roadmap; milestones have target percentages; quick wins listed for immediate shipping | Every experiment has a full card (hypothesis, audience, primary metric, guardrails, instrumentation, duration/sample, rollout/rollback, risks); next steps have week-by-week owners and timelines |
| Specificity | Good specificity on experiment hypotheses and milestone conversion targets; measurement plan has event schema and statistical requirements | Highly specific: activation defined behaviorally with exact events and time windows; 16 named analytics events with properties; sample size calculations; feature flag names; rollback triggers with quantitative thresholds |
| Quality gates | No formal quality gate or self-assessment | Full checklist covering scope, activation definition, first-30s quality, first-mile plan, measurement readiness, plus a rubric scoring each dimension |

## Key Differences

1. **Activation definition rigor.** The skill-guided output devotes an entire section to defining "activation" as a behavioral metric (integration connected AND dashboard viewed with data within 7 days), with a three-step validation plan including retroactive cohort analysis and causal holdout. The baseline output defines activation more loosely (integration connected + user returns) without a validation methodology.

2. **First-30-seconds value delivery.** The skill output introduces a demo dashboard with sample data that delivers immediate value before requiring any setup, transforming the integration step from a cold prerequisite into a motivated upgrade. The baseline output sends users directly to the integration selector, relying on social proof and time estimates to motivate the OAuth step.

3. **Instrumentation depth.** The skill output specifies 16 distinct analytics events with named properties and "used in" mappings, plus four named dashboards with assigned owners. The baseline output lists events in a table format but lacks the per-event property detail and explicit dashboard specifications.

4. **Experiment card completeness.** The skill output provides full experiment cards for the top 3 experiments, each with hypothesis, metrics, guardrails, instrumentation requirements, duration/sample sizing, rollout ramp percentages, rollback criteria, and risk/edge case analysis. The baseline output provides experiment descriptions with ICE scores but less operational detail for execution.

5. **Phased rollout and risk management.** The skill output includes a five-phase sequencing plan across the quarter with explicit rollback triggers (primary metric decline >2pp, guardrail degradation >10%, support ticket thresholds) and a structured rollback process. The baseline output has a weekly execution roadmap but less formalized rollback and escalation criteria.

## Verdict

Both outputs are substantive and would provide real value to a growth team. The skill-guided output is notably more execution-ready, with a behavioral activation definition backed by a validation plan, granular instrumentation schemas, and fully specified experiment cards that a team could run without additional planning. The baseline output is a strong strategic document but would require more work to translate into instrumented experiments with rollback criteria.

## With Skill Output

<details>
<summary>Expand full output (~45k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~23k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
