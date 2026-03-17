# Showcase: Writing PRDs

> Demonstrates the value of the `writing-prds` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `writing-prds`. Product: analytics dashboard. Users: admins. Feature: saved views. Output: PR/FAQ + PRD.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Two-part document: PR/FAQ followed by a 15-section PRD covering overview through milestones; includes technical data model, API endpoints, and schema evolution strategy | Three-part document: context snapshot with artifact selection rationale, PR/FAQ with 8 customer FAQs, and a PRD with numbered requirements (R1-R13), UX flows/states, metrics/instrumentation, rollout plan, and risks/open questions/next steps |
| Completeness | Very thorough PRD with user personas, user stories (US-1 to US-10), detailed technical design (data model, API endpoints, versioning, security), information architecture diagram, edge cases table, and rollout timeline | Covers requirements with acceptance criteria and edge cases, UX flows with error states and accessibility considerations, instrumentation plan with per-metric data sources, three-tier rollout with go/no-go criteria, and rollback triggers |
| Actionability | User stories are prioritized P0-P2; technical design includes database schema and API endpoints ready for engineering review; rollout plan has weekly milestones with deliverables | Requirements use MoSCoW priority with testable acceptance criteria; instrumentation table maps each metric to its data source, event name, owner, and cadence; rollback triggers are quantitative (load time >500ms, CRUD reliability <99%) |
| Specificity | Detailed technical specifications: JSONB data model with all fields, 11 API endpoints, versioning strategy storing 10 most recent versions, rate limiting at 50 ops/minute, 100-view per-user cap | Success metrics have specific targets (40% adoption, 25% time-to-insight reduction, 15% export reduction); guardrails have defined thresholds (p95 +200ms, zero cross-workspace incidents, 99.5% CRUD reliability); per-user limit of 50 views with rationale |
| Quality gates | Notes on approach section explains structural decisions; no formal quality checklist | Full quality checklist (11 items) and rubric scoring across 7 dimensions; artifact selection rationale explains why PR/FAQ is included |

## Key Differences

1. **Artifact selection and narrative alignment.** The skill output opens with a context snapshot that articulates the problem, "why now" (revenue-blocking deals, security concern, competitive gap), and an explicit artifact selection table explaining why PR/FAQ is included alongside the PRD. The baseline output jumps directly into the PR/FAQ without this framing context.

2. **Requirements methodology.** The skill output uses numbered requirements (R1-R13) with MoSCoW priority labels (Must/Should/Could), testable acceptance criteria, and edge case notes per requirement. The baseline output uses user stories (US-1 to US-10) with P0-P2 priority, then expands into detailed requirements by feature area. Both are valid approaches; the skill output is more directly testable by QA.

3. **Instrumentation and measurement plan.** The skill output includes a dedicated instrumentation table mapping each success metric and guardrail to specific event names, data sources, owners, and review cadence. The baseline output defines success metrics and mentions analytics events but does not provide the same level of per-metric instrumentation mapping.

4. **Technical design depth.** The baseline output provides significantly more technical detail: a full database schema (three tables with all fields), 11 REST API endpoints, performance calculations (1-2 GB storage estimate), indexing recommendations, schema evolution strategy, and security considerations including rate limiting. The skill output deliberately stays at a product-requirements level, leaving technical design to engineering.

5. **Rollout and rollback specificity.** The skill output defines a three-tier rollout (internal dogfood, closed beta with 20 customers, phased GA at 10/25/50/100%) with explicit go/no-go criteria per tier and quantitative rollback triggers. The baseline output has a five-phase rollout (Alpha through post-launch) but with less specific advancement criteria.

## Verdict

The two outputs reflect different PRD philosophies. The skill-guided output is a product-manager-centric document focused on requirements clarity, measurement readiness, and rollout discipline -- it would serve well for stakeholder alignment and QA handoff. The baseline output is more engineering-forward, with a detailed technical design that could accelerate implementation. The skill output's advantage is its measurement plan and rollback criteria; the baseline output's advantage is its implementation-ready technical spec. In practice, a complete product development process benefits from both.

## With Skill Output

<details>
<summary>Expand full output (~36k)</summary>

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
