# Showcase: Shipping Products

> Demonstrates the value of the `shipping-products` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're shipping Role-Based Access Control (RBAC) for admins in 3 weeks. Create a Shipping & Launch Pack: staged rollout, go/no-go criteria (PQL), support enablement, and internal/external comms.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8-section document: exec summary, staged rollout, PQL criteria, support enablement, internal comms, external comms, risk register, RACI matrix | 8-section pack: intake/ship statement, release brief, rollout plan, critical path analysis, PQL with 25 stop-ship criteria, measurement plan, comms + enablement, launch day runbook + post-launch review |
| Completeness | Comprehensive coverage including a full RACI matrix, detailed support training program with certification, and a messaging framework with value propositions | Comprehensive with a different emphasis: critical path forcing function ("if we had to ship tomorrow"), 25 individually measurable PQL criteria across 5 categories, and a minute-by-minute launch day runbook |
| Actionability | Well-organized with clear phase gates, training schedules, and external comms timeline; RACI matrix clarifies cross-functional responsibilities | Highly operational: explicit stop-the-line triggers with thresholds, rollback scenarios with time-to-recover estimates, go/no-go checklist (not gut feel), and post-launch review with data sources and retro prompts |
| Specificity | Includes custom role support, SSO/SCIM integration, and penetration testing as scope items; $500K pipeline influence target; NPS >= 40 for beta | Scoped tighter (4 predefined roles only, no custom roles); specific threshold values for every guardrail (5xx > 1%, latency > 800ms, ticket spike > 30%); names exact audit log fields (actor, target, old role, new role, timestamp) |
| Quality gates | 3-tier PQL (Critical/Important/Informational) with clear thresholds; go/no-go decision process with designated authority | 25 stop-ship criteria organized by category (Correctness, Security, Reliability, Observability, Support) each with verification method and owner; known issues documented with fix timelines |

## Key Differences

1. **Scope discipline and critical path.** The skill output applies a "if we had to ship tomorrow" forcing function to identify the absolute critical path and explicitly lists what gets cut or deferred post-GA (bulk assignment, email notifications, API key scoping). The baseline includes a broader scope (custom roles, SSO/SCIM integration, bulk assignment) which may be aspirational for a 3-week timeline.

2. **Stop-the-line triggers.** The skill output defines 5 automatic stop-the-line triggers with precise thresholds (any P0, 5xx > 1%, latency > 800ms, ticket spike > 30%, customer escalation from beta) that pause rollout without requiring a meeting. The baseline has go/no-go criteria but frames them as decision-meeting inputs rather than automatic circuit breakers.

3. **Launch day operational detail.** The skill output includes a full runbook with T-7d through T+7d timeline, named roles (Incident Lead, Comms Lead, Eng On-Call, Support Lead), and an escalation path with specific routing. The baseline provides a launch day checklist (T-24h, T-0, T+4h, T+24h, T+72h) which is useful but less granular on roles and escalation.

4. **Post-launch learning loop.** The skill output schedules a post-launch review with specific data sources (adoption dashboard, health dashboard, support tickets, beta feedback, sales pipeline, incident log), 5 retro prompts, and a categorized follow-up table. The baseline mentions a retrospective but doesn't define the data sources or analysis structure.

5. **Support enablement depth.** The baseline provides a more detailed support training program with certification requirements, multiple training sessions by tier, and a structured escalation path. The skill output covers support readiness but with less training infrastructure detail, focusing instead on macros, troubleshooting guides, and known-issues documentation.

## Verdict

Both outputs are strong launch packs for a high-risk permissions feature. The skill-guided output excels in operational rigor -- stop-the-line triggers, rollback scenarios, and the critical path forcing function make it better suited for real-time launch management. The baseline is stronger on cross-functional communication (RACI, messaging framework, detailed training program) and broader scope planning. For a 3-week timeline on a security-sensitive feature, the skill output's tighter scope and operational guardrails are the more valuable differentiator.

## With Skill Output

<details>
<summary>Expand full output (~34k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~25k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
