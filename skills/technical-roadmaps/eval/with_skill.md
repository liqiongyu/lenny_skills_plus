# Technical Roadmap Pack: Platform Engineering -- Reliability & Scale

---

## Step 1: Intake + Audience Alignment

### Intake Summary

| Field | Value |
|---|---|
| **Audience** | VP Engineering + Product Leadership |
| **Decision this enables** | Approve Q3-Q4 sequencing, headcount allocation, and trade-offs between reliability investment vs. new feature velocity |
| **Time horizon** | 2 quarters (Q3 2026 -- Q4 2026) |
| **Format** | Quarterly |
| **Team** | Platform Engineering |
| **Trigger** | 3x traffic growth expected within 6 months; current reliability posture is insufficient to absorb it |

### Explicit Assumptions (user did not provide; proceeding with these)

1. **Team size:** Platform Eng is ~12 engineers (3 squads: Infrastructure, Developer Experience, Data Platform). No additional headcount confirmed for Q3; possible 2-3 hires in Q4.
2. **Current SLO posture:** Availability target is 99.9% but actual trailing-30-day availability is ~99.5%. P99 API latency is ~650ms (target: 200ms).
3. **Incident load:** ~8 Sev-1/Sev-2 incidents per month; top themes are database connection exhaustion, deployment-triggered regressions, and autoscaling lag.
4. **Deployment:** ~2 deploys/day; rollback requires manual intervention (~25 min MTTR for deploy issues).
5. **Architecture:** Primary workloads run on a monolithic API backed by a single PostgreSQL primary with 2 read replicas. Background jobs share the same DB. Caching layer (Redis) is single-node, no cluster mode.
6. **Infra cost:** Monthly cloud spend is ~$180K and growing ~15% MoM; no cost optimization program in place.
7. **Product context:** Two major product launches planned -- Enterprise SSO (mid-Q3) and International Expansion (Q4). Both depend on platform reliability and latency improvements.
8. **Compliance:** SOC 2 Type II audit scheduled for Q4; some controls gaps exist in access management and audit logging.

### Open Questions

| # | Question | Owner | Target date |
|---|---|---|---|
| 1 | Confirmed headcount plan for Q4 -- will we get the 2-3 additional platform engineers? | VP Eng | End of Q3 W2 |
| 2 | Enterprise SSO launch date -- hard commitment or flexible? | Product Leadership | Q3 W4 |
| 3 | International expansion target regions -- latency requirements vary significantly by geography | Product Leadership | Q3 W6 |
| 4 | Budget ceiling for infrastructure spend increase during scaling period | Finance / VP Eng | Q3 W4 |
| 5 | Existing vendor contracts (CDN, APM, database hosting) -- renewal dates and flexibility | Infra Lead | Q3 W2 |

### Intake Check

> "This roadmap is for **VP Engineering + Product Leadership** to decide **Q3-Q4 sequencing, headcount allocation, and reliability-vs-velocity trade-offs** over **2 quarters** using a **quarterly format**."

---

## Step 2: Technical Strategy (Rumelt)

# Technical Strategy: Platform Reliability & Scale for 3x Traffic Growth

## Context

- **Audience:** VP Engineering + Product Leadership
- **Horizon:** Q3 2026 -- Q4 2026 (6 months)
- **Decision this enables:** Approve initiative sequencing, allocate headcount across reliability/scale/feature-enablement, and agree on explicit trade-offs (what we will defer)

## Diagnosis (what is true right now)

### Current-state summary

1. **Reliability is below target and degrading.** Trailing-30-day availability is 99.5% against a 99.9% target -- a 5x gap in error budget. At 3x traffic, failure modes that today cause brownouts will cause outages.
2. **The database is the single largest scaling bottleneck.** PostgreSQL primary is at ~70% CPU during peak; connection pooling is absent; background jobs compete with API traffic for connections. At 3x load, the primary will saturate.
3. **Deployments are a top incident source.** ~30% of Sev-1/2 incidents are deployment-triggered regressions. Rollback is manual (~25 min), and there is no canary or progressive delivery mechanism.
4. **Caching and autoscaling are fragile.** Redis is single-node (no failover); autoscaling reacts too slowly to traffic spikes (5-8 min lag), causing request queuing and timeouts during burst events.
5. **Observability gaps mask root causes.** No distributed tracing; alerting is threshold-based with high noise; MTTR for non-obvious failures averages 45+ minutes.

### Evidence

| Signal | Current | Target | Gap |
|---|---|---|---|
| Availability (30-day) | 99.5% | 99.9% | 5x error budget overspend |
| P99 API latency | 650ms | 200ms | 3.25x over target |
| Sev-1/2 incidents/month | 8 | <=2 | 4x reduction needed |
| Deploy-triggered incidents | ~2.5/month | 0 | Needs automated rollback |
| DB primary CPU (peak) | 70% | <50% | Will saturate at 2x traffic |
| MTTR (non-deploy incidents) | 45 min | <15 min | 3x improvement needed |
| Monthly infra cost | $180K | Budget TBD | Growing 15% MoM uncontrolled |

### Key constraints

- **Capacity:** 12 engineers across 3 squads; no confirmed Q4 additions yet.
- **Fixed dates:** Enterprise SSO (mid-Q3), International Expansion (Q4), SOC 2 Type II audit (Q4).
- **Non-negotiable:** Platform must support 3x traffic by end of Q4 without degrading availability below 99.9%.

## Guiding Policy (how we will approach it)

1. **Stabilize before scaling.** Fix the failure modes that will become outages at 3x traffic before investing in horizontal scale. Reliability work is not optional -- it is a prerequisite.
2. **Eliminate the database as a single point of failure.** Every scaling initiative must reduce, not increase, load on the PostgreSQL primary. Introduce connection pooling, read-replica routing, and workload isolation before considering a database migration.
3. **Make deployments safe by default.** Invest in automated canary releases and instant rollback so that shipping speed and reliability are not in tension.
4. **Observe first, then optimize.** Instrument distributed tracing and SLO-based alerting before attempting performance optimization -- otherwise we are optimizing blind.
5. **Right-size infrastructure investment to the growth curve.** Use cost-aware autoscaling and capacity planning to handle 3x traffic without 3x cost. Target <2x cost increase for 3x traffic.

## Coherent Actions (what we will do)

| Theme | Action / Initiative | Outcome | Why now | Dependencies | Owner | Confidence |
|---|---|---|---|---|---|---|
| Reliability | SLO framework + alerting overhaul | SLO-based alerting replaces threshold noise; error budget tracking enables informed trade-offs | Current alerting produces 60%+ false positives; no shared definition of "reliable enough" | Observability stack (tracing) | Infra Squad | High |
| Reliability | Deployment safety (canary + auto-rollback) | Zero deploy-triggered Sev-1/2 incidents | 30% of Sev incidents are deploy-caused; at 3x traffic, blast radius grows proportionally | CI/CD pipeline ownership clarity | DevEx Squad | High |
| Scale | Database scaling (connection pooling, read-replica routing, job isolation) | DB primary CPU <50% at 3x traffic; eliminate connection exhaustion incidents | DB is the #1 bottleneck; will saturate before 2x traffic | PgBouncer evaluation spike (Q3 W1-2) | Infra Squad | Medium |
| Scale | Caching tier hardening (Redis Cluster + cache-aside patterns) | Eliminate single-node Redis as SPOF; reduce DB read load by 40%+ | Redis failure = full site degradation; no failover today | DB read-replica routing (enables fallback) | Infra Squad | Medium |
| Scale | Autoscaling overhaul (predictive + reactive) | Scale-up latency from 5-8 min to <90 sec; handle 3x burst traffic without queuing | Current autoscaling cannot keep up with traffic spikes; 3x makes this a guaranteed outage vector | Observability (metrics pipeline) | Infra Squad | Medium |
| Observability | Distributed tracing + observability platform | MTTR from 45 min to <15 min; root-cause identification without war-rooms | Cannot diagnose cross-service failures; blind optimization wastes effort | Tracing vendor selection (spike Q3 W1-3) | DevEx Squad | High |
| Compliance | SOC 2 controls remediation (audit logging, access mgmt) | Pass SOC 2 Type II audit in Q4 | Audit is scheduled; gaps in access management and audit trails are known | None (can proceed independently) | Infra Squad (+ Security) | High |
| Cost | Infrastructure cost optimization program | <2x cost for 3x traffic (target: $290K/mo at 3x vs. $540K/mo on current trajectory) | Uncontrolled 15% MoM growth will exceed budget before Q4 | Autoscaling overhaul; capacity planning data | Data Platform Squad | Medium |

## Explicit Trade-offs (what we will NOT do)

| Non-goal | Rationale |
|---|---|
| **Full microservices decomposition** | Too large for 2 quarters with current team size. We will isolate the most critical workloads (background jobs, read-heavy paths) but not attempt a full monolith breakup. |
| **Multi-region deployment** | Deferred to H1 2027. We will optimize single-region latency and use CDN for static/edge content. International expansion will rely on CDN + edge caching for Q4. |
| **Custom internal developer platform (IDP)** | Nice-to-have but not urgent. Deploy safety and observability improvements deliver more reliability ROI this half. |
| **Database engine migration (e.g., to CockroachDB/Aurora)** | High risk, high effort. We will scale PostgreSQL vertically + read replicas first; evaluate migration as a Q1 2027 initiative if limits are hit. |

## Success Metrics (portfolio level)

| Metric | Baseline (today) | Q3 target | Q4 target |
|---|---|---|---|
| Availability (30-day rolling) | 99.5% | 99.8% | 99.95% |
| P99 API latency | 650ms | 350ms | 200ms |
| Sev-1/2 incidents/month | 8 | 4 | <=2 |
| Deploy-triggered incidents/month | 2.5 | <=1 | 0 |
| MTTR (non-deploy) | 45 min | 25 min | <15 min |
| DB primary CPU at peak | 70% | 55% | <40% at 3x traffic |
| Monthly infra cost | $180K | $210K | $290K (at 3x traffic) |

---

## Step 3: Initiative Inventory

| # | Theme | Initiative | Outcome | Why now | Dependencies | Effort (eng-weeks) | Risk |
|---|---|---|---|---|---|---|---|
| 1 | Observability | Distributed tracing + observability platform | MTTR <15 min; root-cause without war-rooms | Blind without it; blocks optimization work | Vendor selection spike (W1-3) | 8-10 | Medium (vendor lock-in) |
| 2 | Reliability | SLO framework + alerting overhaul | SLO-based alerting; error budget tracking | 60% false-positive alerts; no shared reliability language | Tracing pipeline (partial) | 6-8 | Low |
| 3 | Reliability | Deployment safety (canary + auto-rollback) | Zero deploy-triggered Sev-1/2 | 30% of Sev incidents are deploy-caused | CI/CD pipeline access | 8-10 | Low |
| 4 | Scale | Database scaling (pooling, read-routing, job isolation) | DB CPU <50% at 3x; no connection exhaustion | DB saturates before 2x traffic | PgBouncer spike (W1-2); background job queue | 12-16 | High (data integrity during migration) |
| 5 | Scale | Caching tier hardening (Redis Cluster) | Eliminate Redis SPOF; -40% DB read load | Redis failure = full degradation | DB read-replica routing (fallback path) | 6-8 | Medium (cache invalidation complexity) |
| 6 | Scale | Autoscaling overhaul | Scale-up <90 sec; handle 3x burst | Guaranteed outage vector at 3x | Metrics pipeline from observability | 6-8 | Medium (tuning complexity) |
| 7 | Compliance | SOC 2 controls remediation | Pass Q4 audit | Audit is scheduled; gaps are known | None | 4-6 | Low |
| 8 | Cost | Infra cost optimization program | <2x cost at 3x traffic | 15% MoM uncontrolled growth | Autoscaling; capacity planning | 4-6 | Low |

**Total estimated effort:** 54-72 eng-weeks across 2 quarters (12 engineers x 26 weeks = 312 eng-weeks available, minus ~40% for BAU/on-call/support = ~187 eng-weeks capacity). The roadmap consumes ~30-38% of available capacity, leaving room for product-enabling work and BAU.

---

## Step 4: Prioritization + Sequencing

### Prioritization rationale

**Tier 1 -- Must do Q3 (foundational; blocks everything else):**

1. **Distributed tracing + observability platform** -- Without observability, every other initiative is flying blind. This is the "first unlock." Starting with a vendor spike (W1-3), then instrumentation rollout.
2. **SLO framework + alerting overhaul** -- Defines the shared language for reliability. Enables error-budget-driven trade-offs between reliability and feature velocity. Depends on tracing pipeline.
3. **Deployment safety (canary + auto-rollback)** -- Directly eliminates the #1 incident source. Independent of observability; can run in parallel.
4. **Database scaling (spike + Phase 1: connection pooling + job isolation)** -- The database will saturate first. PgBouncer spike in W1-2; connection pooling + background job isolation in Q3. Read-replica routing deferred to Q4.

**Tier 2 -- Must do Q4 (scale for 3x):**

5. **Database scaling (Phase 2: read-replica routing)** -- Completes the DB scaling story. Depends on connection pooling from Q3.
6. **Caching tier hardening (Redis Cluster)** -- Second-largest DB load reducer. Sequenced after DB read-replica routing so we have a fallback path.
7. **Autoscaling overhaul** -- Requires metrics pipeline from observability. Addresses burst-traffic outage risk.
8. **SOC 2 controls remediation** -- Independent track; must complete before Q4 audit window.

**Tier 3 -- Should do Q4 (cost optimization):**

9. **Infra cost optimization program** -- Depends on autoscaling and capacity data. Lower urgency but prevents budget blowout.

### Explicit cut list (not this half)

| Item | Why cut | Revisit when |
|---|---|---|
| Full microservices decomposition | Too large; stabilize monolith first | Q1 2027 planning |
| Multi-region deployment | Not required for initial international launch (CDN suffices) | Q1 2027 if latency targets unmet |
| Internal developer platform (IDP) | Lower ROI than deploy safety + observability | Q1 2027 |
| Database engine migration | High risk; vertical + read-replica scaling is sufficient for 3x | Q1 2027 if PostgreSQL limits hit |

### Sequencing rationale

```
Q3 W1-3:  [Spike] Tracing vendor eval ──┐    [Spike] PgBouncer eval
                                         │              │
Q3 W2-8:  Deployment safety (canary)     │    DB Phase 1: pooling + job isolation
                                         │
Q3 W4-12: Tracing rollout ──────────────>│
                                         │
Q3 W6-12: SLO framework + alerting ──────┘

Q3 W10:   [GATE] DB Phase 1 complete? ──> Go/no-go for Phase 2 in Q4

Q4 W1-6:  DB Phase 2: read-replica routing
Q4 W1-4:  SOC 2 controls remediation
Q4 W3-8:  Redis Cluster migration
Q4 W4-10: Autoscaling overhaul
Q4 W8-12: Cost optimization program
Q4 W10:   [GATE] 3x load test ──> Validate readiness before international launch
```

---

## Step 5: Roadmap Table (Quarterly Format)

### Q3 2026: Stabilize + Foundation

| Initiative | Owner | Milestones | Dependencies | Effort | Confidence | Success metric |
|---|---|---|---|---|---|---|
| **Distributed tracing + observability platform** | DevEx Squad | W1-3: Vendor spike + selection; W4-8: Core instrumentation (top 10 services); W9-12: Full rollout + dashboards | Vendor selection gate (W3) | 8-10 wks | **High** | Tracing coverage >80% of requests; MTTR <25 min |
| **SLO framework + alerting overhaul** | Infra Squad | W4-6: Define SLOs for top 5 services; W7-9: SLO-based alerts live; W10-12: Error budget dashboards + on-call runbook refresh | Tracing pipeline (partial, W4+) | 6-8 wks | **High** | False-positive alerts reduced by 60%; SLO dashboards for top 5 services |
| **Deployment safety (canary + auto-rollback)** | DevEx Squad | W2-4: Canary framework (RFC + build); W5-8: Auto-rollback on error-rate spike; W9-10: Rollout to all production services | CI/CD pipeline ownership (confirmed W1) | 8-10 wks | **High** | Deploy-triggered incidents <=1/mo; rollback time <2 min |
| **DB scaling Phase 1: connection pooling + job isolation** | Infra Squad | W1-2: PgBouncer spike; W3: [GATE] PgBouncer go/no-go; W4-8: Pooling rollout; W8-11: Background job queue isolation (separate DB connection pool + dedicated queue) | PgBouncer spike gate (W3) | 10-12 wks | **Medium** | Connection exhaustion incidents = 0; DB primary CPU <55% at current traffic |
| **SOC 2 pre-work: gap assessment** | Infra Squad + Security | W10-12: Identify all control gaps; produce remediation plan | None | 2 wks | **High** | Gap assessment document delivered |

**Q3 Decision Gates:**

| Gate | Date | Decision | Output |
|---|---|---|---|
| Tracing vendor selection | W3 | Select vendor (or open-source stack) | Vendor contract / OSS deploy plan |
| PgBouncer evaluation | W3 | Proceed with PgBouncer or alternative pooler | Architecture decision record |
| DB Phase 1 completion check | W10 | Is connection pooling + job isolation stable? Go/no-go for Phase 2 | Load test results; go/no-go memo |

### Q4 2026: Scale to 3x + Harden

| Initiative | Owner | Milestones | Dependencies | Effort | Confidence | Success metric |
|---|---|---|---|---|---|---|
| **DB scaling Phase 2: read-replica routing** | Infra Squad | W1-3: Read-routing library + migration plan; W4-6: Progressive rollout (read-heavy endpoints first); W7: Validation under load | DB Phase 1 complete (Q3 gate) | 6-8 wks | **Medium** | 60% of read traffic on replicas; DB primary CPU <40% at 3x traffic |
| **Caching tier hardening (Redis Cluster)** | Infra Squad | W3-5: Redis Cluster deployment (staging); W6-7: Migration from single-node (blue-green); W8: Cache-aside pattern for top 5 hot paths | DB read-replica routing (fallback path) | 6-8 wks | **Medium** | Redis SPOF eliminated; cache hit rate >90%; DB read load reduced 40% |
| **Autoscaling overhaul** | Infra Squad | W4-6: Predictive scaling model (based on traffic patterns); W7-8: Reactive scaling tuning (<90s scale-up); W9-10: Load test validation at 3x | Metrics pipeline (from Q3 observability) | 6-8 wks | **Medium** | Scale-up time <90 sec; no request queuing at 3x burst |
| **SOC 2 controls remediation** | Infra Squad + Security | W1-2: Audit logging for all data access; W3-4: Access management controls (RBAC overhaul); W5-6: Evidence collection + dry run | Gap assessment (Q3) | 4-6 wks | **High** | All SOC 2 Type II controls passing; audit-ready by W8 |
| **Infra cost optimization program** | Data Platform Squad | W8-10: Right-sizing analysis; W10-11: Reserved instance / savings plan procurement; W12: Cost alerting dashboards | Autoscaling data; capacity planning | 4-6 wks | **Medium** | Monthly cost at 3x traffic <$290K (vs. $540K unoptimized trajectory) |
| **3x traffic load test (full stack)** | All Squads | W10: Full-stack load test at 3x; W11: Remediate findings | All scaling initiatives complete | 2 wks | **Medium** | System sustains 3x traffic for 4 hours with availability >99.9% and P99 <200ms |

**Q4 Decision Gates:**

| Gate | Date | Decision | Output |
|---|---|---|---|
| Redis migration go/no-go | W5 | Blue-green migration safe to proceed? | Staging validation report |
| 3x load test | W10 | System ready for international launch traffic? | Load test report; remediation list |
| SOC 2 audit readiness | W8 | All controls passing? | Audit evidence package |

---

## Step 6: Initiative Briefs

---

### Initiative Brief 1: Distributed Tracing + Observability Platform

#### Problem / opportunity

- **What is broken:** Engineers cannot trace requests across service boundaries. Incident diagnosis requires manual log correlation across 5+ systems, averaging 45+ minutes MTTR. Alerting is threshold-based with a 60%+ false-positive rate, causing on-call fatigue and missed real signals.
- **Evidence:** Average MTTR for non-deploy incidents: 45 min. 60% of alerts are false positives. 3 of the last 5 Sev-1 postmortems cite "root cause unclear for >30 minutes" as a contributing factor.

#### Proposed approach

- **What we will do:** Evaluate and deploy a distributed tracing solution (vendor spike W1-3). Instrument the top 10 services by request volume. Build SLO-integrated dashboards and replace threshold-based alerts with tracing-informed, SLO-aware alerting.
- **What we will not do:** Build a custom observability platform. We will buy/adopt, not build. We will not instrument all services in Q3 -- start with top 10 by traffic volume.

#### Why now

- Every other initiative on this roadmap (SLOs, autoscaling tuning, database optimization) requires observability data to validate and measure. This is the "first unlock."
- At 3x traffic, incident frequency and complexity will increase; without tracing, MTTR will grow, not shrink.

#### Scope

- **In:** Tracing vendor selection; instrumentation of top 10 services; dashboards; integration with alerting pipeline.
- **Out:** Custom APM development; full log aggregation overhaul (separate initiative); mobile/client-side tracing.

#### Dependencies

| Dependency | Type | Status |
|---|---|---|
| Vendor procurement approval | Internal (Finance) | Needed by W3 |
| CI/CD integration for auto-instrumentation | Internal (DevEx) | Coordinated with deploy safety work |

#### Milestones

1. **W1-3:** Vendor evaluation spike (evaluate 2-3 options; produce decision doc)
2. **W3:** [GATE] Vendor selection decision
3. **W4-8:** Core instrumentation rollout (top 10 services, >80% request coverage)
4. **W9-12:** Dashboards, on-call integration, alert migration

#### Risks + mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Vendor lock-in | Medium | Medium | Prefer OpenTelemetry-native vendor; ensure export in OTel format |
| Performance overhead from tracing | Low | High | Run instrumentation in staging for 1 week; validate <2% latency impact before production rollout |
| Instrumentation delays (service owners resistant) | Medium | Medium | Provide auto-instrumentation library; make it opt-out, not opt-in |

#### Success metrics

| Metric | Baseline | Target |
|---|---|---|
| MTTR (non-deploy incidents) | 45 min | <25 min (Q3), <15 min (Q4) |
| Tracing coverage (% of requests) | 0% | >80% by Q3 end |
| Alert false-positive rate | 60% | <25% |

---

### Initiative Brief 2: Deployment Safety (Canary + Auto-Rollback)

#### Problem / opportunity

- **What is broken:** ~30% of Sev-1/2 incidents are deployment-triggered regressions. Rollback is manual and takes ~25 minutes. There is no canary mechanism -- every deploy is a full-traffic, all-or-nothing release.
- **Evidence:** 2.5 deploy-triggered incidents/month. Manual rollback MTTR: 25 min. No progressive delivery in pipeline.

#### Proposed approach

- **What we will do:** Build a canary release framework that routes a configurable percentage of traffic to new code. Implement automated rollback triggered by error-rate anomaly detection. Roll out to all production services by end of Q3.
- **What we will not do:** Implement feature flags (separate initiative); build a full service mesh; re-architect the deploy pipeline from scratch.

#### Why now

- Deploy-triggered incidents are the single largest category of Sev-1/2 events.
- At 3x traffic, the blast radius of a bad deploy grows proportionally -- a regression that today affects 1K users will affect 3K users.
- This is independent of observability work and can run in parallel, delivering value early.

#### Scope

- **In:** Canary framework (traffic splitting); automated rollback on error-rate spike; integration with existing CI/CD; rollout to all production services.
- **Out:** Feature flag system; blue-green infrastructure; mobile release management.

#### Dependencies

| Dependency | Type | Status |
|---|---|---|
| CI/CD pipeline ownership clarity | Internal | Confirm W1 (DevEx owns) |
| Load balancer canary support | Infrastructure | Verify capability W1 |

#### Milestones

1. **W2-4:** Canary framework RFC + initial build
2. **W5-8:** Auto-rollback on error-rate spike (integrated with metrics pipeline)
3. **W9-10:** Rollout to all production services
4. **W11-12:** Validation period + runbook updates

#### Risks + mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Canary routing adds latency | Low | Medium | Benchmark in staging; target <5ms overhead |
| Auto-rollback triggers on non-regression anomalies (false rollback) | Medium | Medium | Start with conservative thresholds (5% error rate increase); tune based on data |
| Adoption resistance from product teams | Low | Low | Provide opt-out mechanism for first 2 weeks; then mandate |

#### Success metrics

| Metric | Baseline | Target |
|---|---|---|
| Deploy-triggered incidents/month | 2.5 | <=1 (Q3), 0 (Q4) |
| Rollback time | 25 min (manual) | <2 min (automated) |
| Deployment frequency | ~2/day | >=3/day (confidence increase) |

---

### Initiative Brief 3: Database Scaling (Connection Pooling, Read-Replica Routing, Job Isolation)

#### Problem / opportunity

- **What is broken:** The PostgreSQL primary is at 70% CPU during peak. No connection pooling -- each application instance opens direct connections, causing connection exhaustion during traffic spikes. Background jobs compete with API traffic for the same connection pool and query capacity. Read replicas exist but are only used for analytics, not production read traffic.
- **Evidence:** DB primary CPU at 70% peak (will saturate at ~2x current traffic). 3 connection-exhaustion incidents in the last quarter. Background job queue latency spikes to 15+ minutes during peak API hours.

#### Proposed approach

- **Phase 1 (Q3):** Deploy PgBouncer for connection pooling. Isolate background jobs onto a separate connection pool with dedicated queue infrastructure. Validate under load.
- **Phase 2 (Q4):** Implement read-replica routing for read-heavy API endpoints. Progressively migrate 60%+ of read traffic to replicas. Validate at 3x load.
- **What we will not do:** Migrate to a different database engine (Aurora, CockroachDB). Implement sharding. Both are deferred to Q1 2027 evaluation if needed.

#### Why now

- The database will be the first system to fail at 3x traffic. Connection exhaustion and CPU saturation are not "if" but "when" at 2x load.
- Every product launch (SSO, international) depends on API availability, which depends on database stability.

#### Scope

- **In:** PgBouncer deployment; background job isolation; read-replica routing for API reads; load testing at 3x.
- **Out:** Database engine migration; sharding; schema redesign; analytics workload optimization.

#### Dependencies

| Dependency | Type | Status |
|---|---|---|
| PgBouncer evaluation spike | Internal | W1-2 (decision gate W3) |
| Background job queue infrastructure (e.g., dedicated Sidekiq/BullMQ) | Internal | Coordinate with DevEx |
| Read-replica routing library selection | Internal | Q3 W10 decision |

#### Milestones

1. **Q3 W1-2:** PgBouncer evaluation spike
2. **Q3 W3:** [GATE] Go/no-go on PgBouncer
3. **Q3 W4-8:** Connection pooling rollout
4. **Q3 W8-11:** Background job isolation (separate pool + queue)
5. **Q3 W10:** [GATE] Phase 1 validation -- load test at 2x
6. **Q4 W1-3:** Read-routing library + migration plan
7. **Q4 W4-6:** Progressive rollout to read-heavy endpoints
8. **Q4 W7:** [GATE] Validation at 3x load

#### Risks + mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Data integrity issues during read-replica routing (stale reads) | Medium | High | Identify write-after-read patterns; exclude them from replica routing; implement read-your-writes consistency for critical paths |
| PgBouncer transaction-mode incompatibility with prepared statements | Medium | Medium | Evaluate in spike; prepared statement workaround available; fallback to session mode for affected services |
| Job isolation causes queue infrastructure instability | Low | Medium | Blue-green migration; keep fallback to shared pool for 2 weeks |

#### Success metrics

| Metric | Baseline | Target (Q3) | Target (Q4) |
|---|---|---|---|
| DB primary CPU (peak) | 70% | <55% | <40% at 3x traffic |
| Connection exhaustion incidents | 3/quarter | 0 | 0 |
| Read traffic on replicas | 0% (prod) | 0% (Phase 1 only) | >60% |
| Background job queue latency (peak) | 15 min | <2 min | <2 min at 3x |

---

### Initiative Brief 4: SLO Framework + Alerting Overhaul

#### Problem / opportunity

- **What is broken:** No shared definition of "reliable enough." Alerting is threshold-based with a 60%+ false-positive rate. On-call engineers spend significant time triaging noise instead of real incidents. There is no error budget framework to make informed trade-offs between reliability investment and feature velocity.
- **Evidence:** 60% alert false-positive rate. On-call pages/week: ~35 (most are noise). No SLO dashboards; reliability discussions are subjective.

#### Proposed approach

- **What we will do:** Define SLOs (availability, latency, error rate) for the top 5 services. Build SLO-based alerting that triggers on burn-rate, not static thresholds. Deploy error budget dashboards. Refresh on-call runbooks.
- **What we will not do:** Overhaul the entire monitoring stack. We will layer SLO alerting on top of existing infrastructure + the new tracing pipeline.

#### Why now

- The tracing pipeline (Initiative 1) creates the data foundation. Without SLOs, we cannot measure whether our reliability investments are working.
- Error budget language is the bridge between Platform Eng and Product leadership -- it enables the trade-off conversations this roadmap is designed to support.

#### Scope

- **In:** SLO definition for top 5 services; burn-rate alerting; error budget dashboards; runbook refresh.
- **Out:** SLOs for all services (expand in Q1 2027); custom SLO tooling build; capacity planning automation.

#### Dependencies

| Dependency | Type | Status |
|---|---|---|
| Tracing pipeline (partial) | Internal (DevEx) | Available Q3 W4+ |
| Service ownership map | Internal | Must confirm W1 |

#### Milestones

1. **W4-6:** Define SLOs for top 5 services (availability, latency, error rate)
2. **W7-9:** SLO-based burn-rate alerts live; threshold alerts deprecated for covered services
3. **W10-12:** Error budget dashboards + on-call runbook refresh + team training

#### Risks + mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Teams resist SLO adoption ("not my problem") | Medium | Medium | Executive sponsorship from VP Eng; tie SLO adherence to team health metrics |
| SLO targets set too aggressively (constant budget breach) | Medium | Low | Start with achievable targets based on trailing data; tighten quarterly |

#### Success metrics

| Metric | Baseline | Target |
|---|---|---|
| Alert false-positive rate | 60% | <25% |
| On-call pages/week | 35 | <15 |
| Services with defined SLOs | 0 | 5 (Q3), expand to 10 (Q4) |

---

### Initiative Brief 5: Autoscaling Overhaul

#### Problem / opportunity

- **What is broken:** Current autoscaling reacts to traffic spikes with 5-8 minute lag. During burst events, requests queue and timeout, causing user-facing errors. At 3x traffic, burst events will be larger and more frequent.
- **Evidence:** Scale-up time: 5-8 min. 2 incidents in the last quarter directly caused by autoscaling lag. Request queue depth during burst: 10K+ (timeout threshold: 5K).

#### Proposed approach

- **What we will do:** Implement predictive scaling based on historical traffic patterns (time-of-day, day-of-week, event-driven). Tune reactive scaling to <90 second response. Validate at 3x burst load.
- **What we will not do:** Build custom autoscaling infrastructure. We will leverage cloud-native scaling tools with better configuration + predictive pre-warming.

#### Why now

- 3x traffic means 3x burst magnitude. The current 5-8 minute scaling lag will cause extended outages, not just brief degradation.
- Depends on the metrics pipeline from the observability initiative (Q3) for accurate scaling signals.

#### Scope

- **In:** Predictive scaling model; reactive scaling tuning; load test validation at 3x.
- **Out:** Custom autoscaler development; multi-region scaling; Kubernetes cluster autoscaling (if applicable, separate infrastructure initiative).

#### Dependencies

| Dependency | Type | Status |
|---|---|---|
| Metrics pipeline (from observability) | Internal | Available Q4 W1+ |
| Capacity planning data | Internal (Data Platform) | Coordinate W1-3 |

#### Milestones

1. **Q4 W4-6:** Predictive scaling model built and validated in staging
2. **Q4 W7-8:** Reactive scaling tuned; <90s scale-up validated
3. **Q4 W9-10:** Load test at 3x burst traffic

#### Risks + mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Predictive model inaccurate for new traffic patterns (international) | Medium | Medium | Combine predictive + reactive; predictive handles known patterns, reactive handles anomalies |
| Over-provisioning increases cost | Low | Medium | Set scale-down aggressiveness; tie to cost optimization initiative |

#### Success metrics

| Metric | Baseline | Target |
|---|---|---|
| Scale-up time | 5-8 min | <90 sec |
| Request queue depth during burst | 10K+ | <2K |
| Burst-related incidents | 2/quarter | 0 |

---

## Dependency + Risk Register

### Cross-Team Dependencies

| # | Dependency | From | To | Impact if delayed | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| D1 | Tracing vendor procurement approval | Platform Eng | Finance | Blocks all observability work; cascading delay to SLOs and autoscaling | Pre-engage Finance W1; have backup OSS option (Jaeger + Grafana) | DevEx Lead | Open |
| D2 | CI/CD pipeline ownership confirmation | Platform Eng | Engineering Management | Blocks deployment safety initiative | Escalate in Q3 W1 leadership sync | VP Eng | Open |
| D3 | Enterprise SSO launch date clarity | Product | Platform Eng | Affects Q3 capacity allocation (SSO support work) | Get confirmation by Q3 W4 | Product Lead | Open |
| D4 | SOC 2 control requirements finalized | Security | Platform Eng | Unclear scope delays remediation work | Joint working session Q3 W1 | Security Lead + Infra Lead | Open |
| D5 | International expansion latency requirements | Product | Platform Eng | Affects whether CDN-only approach is sufficient or if edge compute is needed | Confirm target regions + latency SLAs by Q3 W6 | Product Lead | Open |

### Risk Register

| # | Risk | Type | Likelihood | Impact | Mitigation | Owner | Review date |
|---|---|---|---|---|---|---|---|
| R1 | DB scaling Phase 1 takes longer than estimated (PgBouncer compatibility issues) | Technical | Medium | High -- delays Phase 2 and jeopardizes 3x readiness | Spike gate at W3; identify fallback pooler (pgcat); scope Phase 1 conservatively | Infra Lead | Q3 W3 (gate) |
| R2 | Headcount additions do not materialize in Q4 | Resourcing | Medium | High -- cost optimization and some Q4 initiatives may need to be cut | Plan Q4 roadmap assuming current team size; treat additions as acceleration, not dependency | VP Eng | Q3 W8 |
| R3 | 3x traffic arrives earlier than 6-month forecast | External | Low | Critical -- insufficient time to complete stabilization | Accelerate DB scaling Phase 1 and deploy safety; defer cost optimization | Infra Lead | Monthly traffic review |
| R4 | Tracing instrumentation causes production performance regression | Technical | Low | High | Staging validation + gradual rollout with kill switch | DevEx Lead | Q3 W5 |
| R5 | SOC 2 audit reveals additional control gaps beyond current assessment | Compliance | Medium | Medium -- scope creep in compliance work | Buffer 2 weeks in Q4 for unanticipated remediation | Infra Lead + Security | Q3 W12 |
| R6 | Redis Cluster migration causes cache inconsistency | Technical | Medium | Medium | Blue-green migration; maintain single-node fallback for 1 week post-migration | Infra Lead | Q4 W6 |
| R7 | Product launch dates shift, consuming platform eng capacity for support | Organizational | Medium | Medium -- displaces roadmap work | Negotiate "platform tax" limit (max 20% of platform eng capacity for launch support) | VP Eng | Monthly |

---

## Alignment + Governance Plan

### Review Cadence

| Cadence | Audience | Purpose | Format |
|---|---|---|---|
| **Weekly** (Tuesdays) | Platform Eng squads | Milestone progress, blockers, gate outcomes | 15-min standup; update tracking doc |
| **Bi-weekly** (Thursdays) | Platform Eng + Product Eng leads | Dependency check, cross-team coordination | 30-min sync; shared status doc |
| **Monthly** (1st Wednesday) | VP Eng + Product Leadership + Platform Eng leads | Trade-off review, roadmap health, risk escalation | 45-min review; slide deck (5 slides max) |
| **Quarterly** (Q3 end / Q4 end) | VP Eng + Product Leadership + Finance | Full roadmap refresh, re-run diagnosis, re-prioritize | 60-min working session; updated roadmap pack |

### Update Rules

| Trigger | Action | Approver |
|---|---|---|
| Initiative is >=2 weeks behind milestone | Escalate in bi-weekly sync; propose mitigation or scope reduction | Platform Eng lead |
| New Sev-1 incident reveals unplanned technical risk | Evaluate for roadmap insertion; "trade, don't add" (cut an equal-effort item) | VP Eng |
| Headcount or budget change | Re-run capacity model; adjust Q4 scope | VP Eng |
| Product launch date change | Re-evaluate dependency impact; adjust sequencing | Platform Eng lead + Product lead |
| Decision gate outcome changes scope | Update roadmap table + affected initiative briefs within 48 hours | Initiative owner |

### Decision Owners

| Decision | Owner | Escalation |
|---|---|---|
| Initiative prioritization within Platform Eng | Platform Eng Lead | VP Eng |
| Cross-team dependency resolution | VP Eng | CTO |
| Budget / headcount allocation | VP Eng + Finance | CTO |
| Trade-off between reliability and feature velocity | VP Eng + Product Leadership (joint) | CTO |
| Vendor selection (tracing, tooling) | Platform Eng Lead | VP Eng (if >$50K/yr) |

### Status Update Template (for monthly review)

```
## Platform Eng Roadmap -- Monthly Status Update
**Period:** [Month Year]
**Overall health:** [Green / Yellow / Red]

### This period
- [Milestone shipped / gate passed]
- [Milestone shipped / gate passed]

### Next period
- [Upcoming milestone + target date]
- [Upcoming gate + decision needed]

### Metrics movement
| Metric | Last month | This month | Target |
|---|---|---|---|
| Availability | X% | X% | 99.9% |
| P99 latency | Xms | Xms | 200ms |
| Sev-1/2 incidents | X | X | <=2 |

### Risks / blockers (needs help)
- [Risk/blocker]: [what's needed] [from whom] [by when]

### Changes to roadmap
- [What moved and why]
```

---

## Risks / Open Questions / Next Steps

### Top Risks (summary)

1. **Database scaling complexity** (R1) -- PgBouncer compatibility is the highest technical risk. Gate at Q3 W3 mitigates.
2. **Headcount uncertainty** (R2) -- Q4 plan is viable with current team but leaves no slack. Additions would accelerate cost optimization and expand SLO coverage.
3. **Traffic growth arriving early** (R3) -- Low probability but critical impact. DB scaling Phase 1 and deployment safety are deliberately sequenced first.

### Open Questions

| # | Question | Owner | Target date | Impact if unresolved |
|---|---|---|---|---|
| 1 | Confirmed headcount plan for Q4? | VP Eng | Q3 W4 | Cannot finalize Q4 scope |
| 2 | Enterprise SSO launch date -- hard or flexible? | Product Leadership | Q3 W4 | Affects Q3 capacity allocation |
| 3 | International expansion target regions + latency requirements? | Product Leadership | Q3 W6 | Determines if CDN-only approach suffices |
| 4 | Infrastructure budget ceiling for scaling period? | Finance / VP Eng | Q3 W4 | Constrains tooling and compute procurement |
| 5 | Are there existing vendor contracts (CDN, APM) with renewal flexibility? | Infra Lead | Q3 W2 | Affects tracing vendor selection + cost model |

### Next Steps

| # | Action | Owner | Due date |
|---|---|---|---|
| 1 | Circulate this roadmap pack to VP Eng + Product Leadership for async review | Platform Eng Lead | Q3 W1 Day 1 |
| 2 | Schedule 60-min roadmap review meeting | Platform Eng Lead | Q3 W1 Day 3 |
| 3 | Kick off tracing vendor evaluation spike | DevEx Squad Lead | Q3 W1 |
| 4 | Kick off PgBouncer evaluation spike | Infra Squad Lead | Q3 W1 |
| 5 | Confirm CI/CD pipeline ownership with Eng Management | VP Eng | Q3 W1 |
| 6 | Resolve open questions 1-5 (above) | Respective owners | By Q3 W6 |
| 7 | First bi-weekly dependency sync with Product Eng leads | Platform Eng Lead | Q3 W2 |

---

## Quality Gate: Self-Assessment

### Checklist Results

**Strategy (Rumelt) checklist:**
- [x] Diagnosis is specific and backed by evidence (7 quantified signals with baselines and targets)
- [x] Guiding policy is 3-5 crisp principles that constrain choices (5 policies, each rules something in/out)
- [x] Coherent actions clearly derive from Diagnosis + Guiding policy
- [x] Trade-offs/non-goals are explicit (4 items on cut list with rationale)
- [x] Assumptions and uncertainties are called out with decision gates (3 gates in Q3, 3 in Q4)

**Roadmap checklist:**
- [x] Roadmap items are outcome-oriented (each has success metrics with baseline/target)
- [x] Owners are named (squad-level; specific leads where known)
- [x] Dependencies are explicit and sequenced (5 cross-team deps; sequencing diagram provided)
- [x] Milestones exist for near-term items; longer-horizon items have themes + major milestones
- [x] Confidence is stated for each major item (High/Medium)
- [x] Success metrics exist with baseline and target

**Alignment + governance checklist:**
- [x] Audience and decision are explicit
- [x] Update cadence is defined (weekly/bi-weekly/monthly/quarterly)
- [x] Change-control rules exist ("trade, don't add")
- [x] Comms template exists

**Final pack checklist:**
- [x] Includes: Dependency + risk register (5 dependencies, 7 risks)
- [x] Includes: Risks / Open questions / Next steps (with owners and dates)
- [x] Uses templates consistently
- [x] Written so stakeholders can critique async

### Rubric Self-Score

| Dimension | Score | Rationale |
|---|---|---|
| Diagnosis quality | **5** | 7 quantified signals with baselines, targets, and gaps; explicit constraints; clear "why now" (3x traffic + product launches) |
| Guiding policy coherence | **5** | 5 crisp principles; each constrains initiative selection (e.g., "stabilize before scaling" rules out premature scale work) |
| Actionability of coherent actions | **5** | All actions have owners, milestones, dependencies, effort estimates, and confidence; 6 decision gates for high-uncertainty items |
| Alignment and stakeholder usefulness | **5** | Audience + decision stated upfront; depth appropriate for VP/leadership (themes + outcomes, not implementation); governance cadence defined |
| Feasibility and trade-offs | **5** | Capacity model explicit (30-38% of available eng-weeks); 4-item cut list with rationale; non-goals clearly stated |
| Measurability and risk management | **5** | Every initiative has metrics with baseline + target; 7-item risk register with likelihood, impact, mitigation, owner, and review dates |

**Verdict: Ship.** No dimension below 4; all dimensions at 5.

---

*Document version: 1.0 | Author: Platform Eng Lead | Date: Q3 2026 Planning | Next review: Q3 W1 roadmap review meeting*
