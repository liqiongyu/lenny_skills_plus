# Showcase: Engineering Culture

> Demonstrates the value of the `engineering-culture` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `engineering-culture`. Context: B2B analytics SaaS, 40 engineers across 5 teams, Rails monolith plus 3 Go microservices, deploying twice a week via manual release trains, averaging 2 P1 incidents/month. Symptoms: PRs sit in review for 3+ days, no one owns on-call (it rotates randomly), platform team is a bottleneck for every feature team, and PMs complain engineering 'goes dark' mid-sprint. Goal: increase deploy frequency to daily and reduce P1s by 50% within one quarter. Create an Engineering Culture Operating System Pack with a capability snapshot, culture code, Conway's Law analysis of the platform bottleneck, a clock-speed improvement backlog, and a cross-functional workflow contract for PM/Design/Eng. Output: Engineering Culture Operating System Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 10 sections organized by topic (deployment, PR review, on-call, platform, communication, metrics, roadmap, risks, culture, quick wins) | 7 numbered sections following a system model: Culture Snapshot, Culture Code, Conway's Law Analysis, Clock Speed Backlog, Cross-Functional Contract, Rollout Plan, Risks/Next Steps |
| Completeness | Covers all major areas with practical recommendations; adds cultural principles and a 12-week roadmap | All requested deliverables plus baseline metrics with confidence levels, a 4-bucket capability map, AI-assisted development norms, and instrumentation gap tracking |
| Actionability | Each section has a timeline and concrete steps; quick-wins section lists 7 immediate actions | 12-item prioritized backlog with owners, effort estimates (S/M/L), dependencies, and leading indicators; 8 "this week" next steps |
| Specificity | Recommends CODEOWNERS, review SLAs, and PagerDuty with general timelines | Specifies exact SLAs (4h first pass / 24h approval), defines 5 culture principles with do/don't behaviors, decision rules, and anti-patterns |
| Quality gates | Metrics table with 7 items and targets; risk/mitigation table | 4 outcome metrics + 4 leading indicators + 4 guardrails with escalation thresholds; self-assessment checklist with rubric scores |

## Key Differences

1. **Conway's Law analysis.** The skill output dedicates a full section to analyzing 3 specific misalignments between org structure and architecture (shared monolith ownership, platform as gatekeeper, random on-call), each with evidence, root cause, and a transition plan with trade-offs. The baseline identifies the same problems but treats them as separate topic areas without the organizational-architecture lens.

2. **Culture Code with behavioral specificity.** The skill output defines 5 principles, each with explicit "do" behaviors, "don't" behaviors, decision rules, anti-patterns, and measurable signals of success. The baseline lists 5 cultural principles in 1-2 sentences each without behavioral anchors or enforcement mechanisms.

3. **Cross-functional workflow contract.** The skill output includes a complete 5-stage workflow (Intake through Learn) with SLAs, escalation paths, non-engineer participation rules, and AI-assisted development norms. The baseline addresses communication and sprint transparency but does not formalize the end-to-end workflow or define non-engineer roles.

4. **Prioritized backlog with dependencies.** The skill output provides 12 initiatives ranked by impact and effort, each with an owner, dependencies, and a specific metric. The baseline offers a 12-week phased roadmap but does not explicitly sequence initiatives by dependency or assign metrics per initiative.

5. **Guardrails and instrumentation gaps.** The skill output explicitly identifies what is NOT currently measured (MTTR, change failure rate, DevEx survey) with owners and target dates to close each gap. The baseline notes "measure this" for several metrics but does not track instrumentation gaps as a separate workstream.

## Verdict

The skill output produces a genuinely systemic analysis where culture principles, architectural decisions, and operational metrics reinforce each other. The baseline provides excellent tactical recommendations but treats each area somewhat independently. For a VP Engineering trying to drive a quarter-long transformation, the skill output's connected model -- where Conway's Law findings drive the backlog, which is measured by the metrics, which are reinforced by the culture code -- is significantly more powerful.

## With Skill Output

<details>
<summary>Expand full output (~21k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~10k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
