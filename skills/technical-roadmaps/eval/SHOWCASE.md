# Showcase: Technical Roadmaps

> Demonstrates the value of the `technical-roadmaps` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're adding 3x traffic in 6 months and reliability is shaky. Create a technical roadmap (2 quarters) for Platform Eng. Audience is VP Eng + Product leadership. Use quarterly format.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 3-layer structure: executive summary with metrics table, Q3 (4 workstreams with initiative tables), Q4 (4 workstreams), staffing requirements, product dependencies, governance gates | 7-step structure: intake + audience alignment, Rumelt-style technical strategy (diagnosis, guiding policy, coherent actions), initiative inventory, prioritization + sequencing with dependency diagram, quarterly roadmap tables, 5 initiative briefs, dependency + risk register, alignment + governance plan |
| Completeness | Broad scope: includes staffing requests (+6 engineers), multi-region/multi-AZ deployment, service mesh, chaos engineering, sharding strategy, and internal developer portal | Focused scope: 8 initiatives with explicit cut list (4 items deferred with rationale and revisit triggers); no headcount assumptions beyond current team; capacity model showing 30-38% utilization of available eng-weeks |
| Actionability | Initiative tables with milestones per workstream; Q3/Q4 gate criteria; staffing requirements table; appendix with prioritization framework | Initiative briefs (5 detailed) each with problem, approach, scope in/out, dependencies, milestones, risks + mitigations, and success metrics with baselines; decision gates at specific weeks (W3, W10) |
| Specificity | Uses general descriptions ("containerize remaining monolith components," "evaluate and implement horizontal partitioning"); staffing needs quantified | Uses specific technical proposals (PgBouncer for connection pooling, Redis Cluster via blue-green migration, burn-rate alerting for SLOs); current-state evidence quantified (70% CPU peak, 60% alert false-positive rate, 650ms P99) |
| Quality gates | Quarterly review gates (Q3: 2x capacity validated; Q4: 3.5x validated); biweekly reporting to VP Eng | 6 decision gates across Q3-Q4 with specific week numbers; "trade, don't add" update policy; 4-tier governance cadence (weekly/biweekly/monthly/quarterly) with defined audiences |

## Key Differences

1. **Strategic framing (Rumelt structure).** The skill output opens with a formal technical strategy: diagnosis (5 evidence-backed current-state problems), guiding policy (5 principles that constrain choices), and coherent actions derived from the policy. The baseline opens with a current-state assessment and moves directly to workstreams. The strategic layer helps leadership understand *why* initiatives are sequenced this way, not just *what* is being built.

2. **Explicit trade-offs and cut list.** The skill output includes a 4-item cut list (microservices decomposition, multi-region, IDP, database engine migration) each with rationale and a "revisit when" trigger. The baseline includes all of these as planned initiatives (multi-AZ, service mesh, sharding, developer portal), which may be aspirational given the team size and timeline.

3. **Capacity realism.** The skill output calculates available eng-weeks (312 total, ~187 after BAU/on-call), shows the roadmap consumes 30-38% of capacity, and plans around current headcount. The baseline requests 6 additional engineers and 40-50% infrastructure cost increase, which represents a different planning approach but also a dependency that may not materialize.

4. **Initiative brief depth.** The skill output provides 5 detailed initiative briefs each containing: problem with evidence, proposed approach with explicit non-goals, "why now" justification, scoped in/out lists, dependency tables, milestone sequences with decision gates, risk tables with mitigations, and success metrics with baselines and targets. The baseline provides initiative descriptions within workstream tables but without the same per-initiative analytical depth.

5. **Dependency and risk management.** The skill output includes a dedicated cross-team dependency register (5 dependencies with owners, impact-if-delayed, and mitigation) and a risk register (7 risks with likelihood, impact, mitigation, owner, and review date). The baseline includes Q3/Q4 risk tables and product dependencies but doesn't consolidate them into a trackable register with review dates.

## Verdict

The baseline covers more technical ground (chaos engineering, service mesh, sharding, multi-region) and is bolder in its scope ambitions. The skill-guided output is more disciplined in scope management, strategic justification, and operational governance. For a VP Eng making sequencing and resource allocation decisions -- the stated audience -- the skill output's explicit trade-offs, capacity model, and decision gates provide more directly useful decision-making material. The baseline would serve well as inspiration for a longer-horizon technical vision document.

## With Skill Output

<details>
<summary>Expand full output (~43k)</summary>

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
