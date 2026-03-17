# Showcase: Platform Infrastructure

> Demonstrates the value of the `platform-infrastructure` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `platform-infrastructure`. We're a B2B analytics SaaS (Series B, 50 engineers) where every feature team keeps rebuilding export functionality, filtering logic, and permission checks. Our Postgres database is approaching limits (500GB, query latency increasing) and we expect 5x traffic growth in 6 months from an enterprise push. Create a Platform & Infrastructure Improvement Pack with a shared capabilities plan (export, filtering, permissions as platform services), a Postgres scaling analysis with a doomsday clock and migration options (read replicas, sharding, or move to a new DB), reliability SLOs (p99 latency, uptime targets), and an execution roadmap prioritized by blast radius. Output: Platform & Infrastructure Improvement Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 5-section plan covering shared capabilities, Postgres scaling, SLOs, execution roadmap, and outcomes summary | 8-section Pack following a prescribed methodology (Context Snapshot, Shared Capabilities Inventory + Platformization Plan, Quality Attributes Spec, Scaling Doomsday Clock + Capacity Plan, Instrumentation Plan, Discoverability, Execution Roadmap, Risks/Open Questions) with quality-gate self-assessment |
| Completeness | Covers shared services architecture with API examples, Postgres scaling across 3 time horizons, 4-tier SLOs, and a phased roadmap with staffing | Additionally includes an instrumentation plan with observability gaps analysis, a server-side analytics event contract with schema/versioning standards, identity merge rules, data QA checks, and 10 canonical events with full property definitions |
| Actionability | Provides SQL examples for table partitioning, specific tool recommendations, and a phase-by-phase staffing plan | Each milestone has explicit acceptance criteria, rollout/rollback procedures, and dependencies; doomsday clock has 8 components with current values, trigger thresholds, lead times, and named mitigation projects |
| Specificity | SLOs are defined across 4 tiers (user-facing, batch, internal services, database) with specific latency and availability targets | Shared capability contracts specify exact API shapes (REST, gRPC, SDK), versioning policies (2-sprint deprecation window), migration approaches (shadow mode for permissions), and cache requirements (p99 < 5ms cached, < 50ms uncached) |
| Quality gates | No self-assessment; key decision points listed for Weeks 4, 8, 12, 16, 20 | Includes a multi-section quality-gate checklist covering scope, platformization, infrastructure quality, scaling readiness, instrumentation, discoverability, and execution readiness |

## Key Differences

1. **Doomsday clock with lead-time awareness.** The skill-guided output produces a doomsday clock tracking 8 infrastructure limits (disk, IOPS, connections, query latency, replication lag, compute, export queue, object storage) with current values, trigger thresholds calculated to account for mitigation lead times, and named projects tied to each trigger. The baseline identifies scaling risks but presents them as a linear timeline rather than a trigger-based monitoring system.

2. **Shared capability contracts at API level.** The with-skill output defines each shared service with a specific interface (REST for exports, internal SDK for filtering, gRPC for permissions), along with migration approaches (adapter shims, shadow mode, opt-in SDK adoption), versioning policies, and backward compatibility commitments. The baseline provides architecture descriptions and API examples but without the migration mechanics or compatibility guarantees.

3. **Observability and instrumentation plan.** The skill-guided output includes a dedicated instrumentation section identifying 6 observability gaps, defining 10 canonical server-side analytics events with full property schemas, identity merge rules, delivery semantics (at-least-once with dedup), and data QA checks. The baseline recommends observability tools but does not define event schemas or data quality standards.

4. **Feature-freeze policy tied to scaling triggers.** The with-skill output defines yellow and red policies: at yellow (trigger threshold), scaling becomes P1 and platform team gets additional engineers; at red (critical threshold), a full feature freeze applies to DB-intensive work with 4-hour stakeholder communication. The baseline does not formalize a feature-freeze trigger tied to infrastructure metrics.

5. **Blast-radius sequencing rationale.** The skill-guided output explicitly explains why milestones are sequenced by blast radius (DB affects all 50 engineers and all customers first; observability must precede informed decisions; permissions affects the most consumer teams). The baseline sequences work by phase (stabilize, platform, scale) but does not articulate the blast-radius reasoning behind the ordering.

## Verdict

Both outputs are technically strong and cover the same core areas. The baseline provides practical details like SQL partitioning examples, specific tool recommendations, and a staffing plan that the skill-guided output omits. The skill-guided output excels in operational governance: the doomsday clock with lead-time-aware triggers, feature-freeze policies, observability gap analysis, event schema contracts, and blast-radius-justified sequencing create a more operationally mature plan. For a Series B company preparing for enterprise customers, the governance artifacts in the skill-guided output would be particularly valuable for SOC 2 readiness and on-call maturity.

## With Skill Output

<details>
<summary>Expand full output (~37k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~20k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
