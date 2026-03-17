# Showcase: Organizational Design

> Demonstrates the value of the `organizational-design` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `organizational-design`. Context: B2B SaaS analytics platform, ~180 people; Product/Eng/Design/Data in-scope. Current structure: 5 feature teams, 1 platform team, 1 data team, and a new AI/ML team of 4. Symptoms: platform team is a bottleneck (every feature team depends on them for API changes), the AI/ML team has no PM and takes requests from everyone, data team ownership is unclear (analytics vs data engineering vs ML pipelines). Goals: increase shipping parallelism and reduce cross-team blocking without adding headcount for 2 quarters. A major customer launch is in 8 weeks. Create an Organizational Design Pack with a current-state dependency map, 2-3 restructuring options (including platform productization and value-stream alignment), a recommendation with Day 1 changes, and a transition plan that protects the upcoming launch. Output: Organizational Design Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Standard 10-section document with logical flow but no prescribed framework | Full 8-section Org Design Pack following a rigorous methodology (Brief, Current-State Map, Operating Model Decision, Org Options, Recommendation + Scorecard, Operating Mechanisms, Transition Plan, Risks/Open Questions) |
| Completeness | Covers key areas (diagnosis, 3 options, recommendation, transition) but lacks explicit design principles, decision rights tables, and operating mechanisms | Comprehensive coverage including explicit design principles, centralization/decentralization posture, decision rights RACI tables, interface contracts, escalation triggers, and rollback criteria |
| Actionability | Provides a phased timeline and staffing plan but Day 1 actions are embedded in phase descriptions rather than called out explicitly | Separates Day 1 changes from follow-on changes with concrete week-by-week sequencing; includes copy-paste comms plan with audience-specific messaging |
| Specificity | Options include specific team sizes and org charts but dependency analysis stays at a high level | Each option explicitly states which dependencies are removed vs. moved; dependency hotspots are ranked and mapped to specific mitigations |
| Quality gates | No self-assessment or rubric; no explicit checklist | Includes a multi-section quality gate checklist (dependency/parallelism, UX coherence, decision rights, transition/people-risk) plus a rubric self-score for each option |

## Key Differences

1. **Current-state diagnostic depth.** The skill-guided output produces a detailed current-state map with team charters, dependency hotspots ranked by severity, a decision-rights audit, and a management-layers snapshot. The baseline covers the same ground more briefly without the structured decomposition into dependency, decision, and management dimensions.

2. **Operating model framing.** The with-skill output explicitly positions the org on centralization and functional/divisional spectrums with guardrails for what must stay centralized vs. decentralized. The baseline jumps directly to restructuring options without articulating an overarching operating model philosophy.

3. **Dependency removed vs. moved analysis.** For each option, the skill-guided output explicitly distinguishes dependencies that are eliminated from those merely relocated, along with new dependencies that might be created. The baseline describes pros and cons but does not perform this structural analysis.

4. **Transition safety mechanisms.** The with-skill output includes rollback triggers, a phased comms plan broken down by audience (execs, managers, ICs, specific impacted teams), and Day 30/60/90 measurement checkpoints. The baseline provides a reasonable transition plan but without explicit rollback criteria or audience-segmented communications.

5. **Decision rights as a first-class artifact.** The skill-guided output produces a full decision-rights table (owner, consulted, informed, escalation trigger) covering seven decision types, plus interface contracts between teams. The baseline mentions RACI for the data team but does not systematically map decision rights across the organization.

## Verdict

Both outputs are competent and address the core challenge of reducing cross-team blocking. The skill-guided output stands out for its systematic methodology: explicit operating model choices, dependency-removed-vs-moved analysis, decision rights tables, and structured transition safety mechanisms. The baseline provides a solid restructuring plan but lacks the diagnostic depth and operational governance artifacts that would make the recommendation immediately executable.

## With Skill Output

<details>
<summary>Expand full output (~46k)</summary>

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
