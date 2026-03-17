# Showcase: AI Product Strategy

> Demonstrates the value of the `ai-product-strategy` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `ai-product-strategy`. Product: AI coding assistant. Users: mid-market engineering teams. Constraints: beta in 8 weeks, must not leak proprietary code, cost cap, latency target. Output: AI Product Strategy Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 16 free-form sections (Executive Summary, Problem, Users, Vision, Features, Security, Architecture, Cost, GTM, Metrics, Risks, Team, Execution, Competitive, Roadmap, Open Questions) | 9 structured sections following the skill's workflow (Context Snapshot, Strategy Thesis, Use-Case Portfolio, Autonomy Policy, System Plan, Empirical Plan, Roadmap, Kill Criteria, Risks/OQ/Next Steps) + self-assessment |
| Completeness | Good general coverage; strong on implementation details (architecture diagrams, cost per server, hiring plan, competitive landscape). Missing: formal autonomy policy, kill criteria, empirical learning plan with experiments, structured use-case scoring, quality gate | All 9 required deliverables produced. 12 use cases scored on 8 dimensions. 6 experiments with decision rules. 7 kill criteria. Self-assessment checklist + rubric scoring (20/20) |
| Actionability | A reader could start building from this, but would need additional meetings to align on what to measure, when to stop, and who owns what experiment | A reader can act on this without a meeting: every section has owners, metrics, timeboxes, and decision rules. Kill criteria prevent sunk-cost traps |
| Specificity | Concrete on technical details (vLLM, gRPC, FAISS, quantization tiers). Generic on strategy decisions (no explicit non-goals, no scored alternatives) | Concrete on both strategy AND execution: 5 explicit non-goals, 5 assumptions with tests, 12 use cases scored and ranked, 7 "must never do" rules |
| Quality gates | None. No self-check, rubric, or quality assessment | Full quality gate: 7-section checklist + 10-dimension rubric scored 20/20. Explicitly flags what was checked |

## Key Differences

1. **Systematic use-case prioritization.** The skill output evaluates 12 candidate use cases on feasibility, risk, data needs, and "must-not-do" constraints in a structured table, then explicitly selects top 3 bets with rationale and records WHY rejected candidates were cut. The baseline lists features with priority labels (P0/P1) but doesn't show the scoring or alternatives considered.

2. **Autonomy policy as a first-class deliverable.** The skill output includes a detailed autonomy table mapping each capability to its mode (suggest/assist/act), approval requirements, permission scope, audit logging, rollback mechanism, failure modes, and mitigations. It includes a 7-item "must never do" list and a prompt injection/tool misuse plan. The baseline discusses security architecture extensively but never formally defines what the AI can/cannot do at each capability level.

3. **Kill criteria and empirical learning plan.** The skill output defines 7 explicit conditions under which the team would stop investing, pivot, or scale back -- with specific metrics, thresholds, timeboxes, and triggered actions. It also defines 6 experiments (each with hypothesis, success metric, guardrail metric, instrumentation, timebox, owner, and decision rule). The baseline has milestones and risk mitigations but no formal experiments, no decision rules, and no kill criteria.

4. **Role shift analysis.** The skill output explicitly maps how the engineer's role changes with AI (from "write everything" to "direct, review, refine"), identifies human control points, and names 5 trust-destroying failure modes with consequences. The baseline discusses personas and pain points but doesn't analyze the workflow transformation.

5. **Self-assessment quality gate.** The skill output concludes with a formal self-check against 7 checklists and a 10-dimension rubric, scoring itself 20/20 and explicitly stating what was verified. The baseline has no quality self-check.

## Verdict

The skill pack transforms a good general strategy document into a **decision-ready, actionable strategy pack**. The baseline output is well-written and covers implementation details (architecture, cost modeling, competitive landscape, hiring) that are useful but tangential to the core strategy decision. The skill-guided output is more disciplined: it forces structured use-case scoring, explicit autonomy boundaries, empirical plans with decision rules, and kill criteria -- the artifacts that prevent the most common AI product strategy failures (scope creep, sunk-cost traps, shipping without evals, agent-first without permissions). The 48k skill output is nearly 2x the size of the 26k baseline, but the additional length is entirely in structured tables, explicit criteria, and decision frameworks -- not filler.

## With Skill Output

<details>
<summary>Expand full output (~48k, 485 lines)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~26k, 507 lines)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
- With-skill: ~48k output, 9 structured sections + quality gate
- Baseline: ~26k output, 16 free-form sections
