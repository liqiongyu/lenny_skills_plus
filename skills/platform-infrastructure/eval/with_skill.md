# Platform & Infrastructure Improvement Pack

**Company:** B2B Analytics SaaS (Series B, 50 engineers)
**Date:** 2026-03-17
**Decision statement:** We will extract export, filtering, and permissions into shared platform services, define a Postgres scaling plan with lead-time-aware triggers, and commit to reliability SLOs -- all sequenced by blast radius so the highest-leverage work ships first, enabling the enterprise push without a firefighting spiral.

---

## 1) Context Snapshot

- **System(s) in scope:** Core B2B analytics SaaS platform -- all product services, the shared Postgres database, and the internal tooling layer consumed by feature teams.
- **Users/customers:** Enterprise and mid-market analytics buyers; internal consumers are ~8-10 feature teams (50 engineers total).
- **Primary pains (1-3):**
  1. **Developer velocity** -- every feature team re-implements export, filtering, and permission checks, creating duplicated effort and inconsistent behavior.
  2. **Database scaling** -- Postgres at 500 GB with increasing query latency; 5x traffic growth expected in 6 months from enterprise push.
  3. **Reliability risk** -- no formal SLOs; enterprise customers will demand contractual uptime and performance guarantees.
- **Time horizon / deadline:** 6 months to enterprise launch readiness. Postgres scaling work must begin immediately given lead times.
- **Stakeholders / decision-maker(s):** VP Engineering (decision-maker), Platform/Infra lead (DRI for shared services), Product Engineering leads (consumers), SRE/on-call rotation (reliability ownership).
- **Constraints (security/compliance, staffing, risk tolerance):**
  - Series B staffing: no dedicated platform team yet; will need to carve out 4-6 engineers from feature teams or hire.
  - Enterprise push implies SOC 2 / data residency requirements are imminent.
  - Risk tolerance: moderate -- can tolerate planned migrations but not extended outages or data loss.
- **Assumptions (explicit):**
  - A1: Current Postgres instance is a single primary with read replicas (no sharding today).
  - A2: Feature teams number 8-10, each with 4-6 engineers; at least 4 teams have built their own export, filtering, or permissions logic.
  - A3: No formal SLOs exist today; monitoring is basic (uptime pings, some application metrics).
  - A4: The enterprise push will bring customers with contractual SLA requirements (99.9%+ availability).
  - A5: Current query latency degradation is primarily from large analytical queries competing with transactional workload on the same Postgres instance.
- **Success definition (measures):**
  - Export, filtering, and permissions available as platform services consumed by >= 3 teams within 4 months.
  - Postgres scaling plan executed with headroom for 5x growth before enterprise launch.
  - Published SLOs for top 5 user journeys with measurement infrastructure in place.
  - Zero P0 incidents caused by DB saturation or permission inconsistencies during enterprise onboarding.
- **Non-goals / out of scope:**
  - Rewriting the entire application architecture or migrating off Postgres entirely.
  - Product/market positioning of the analytics platform (use `platform-strategy`).
  - Broader technical roadmap sequencing beyond infra (use `technical-roadmaps`).
  - Legacy code cleanup unrelated to shared capabilities (use `managing-tech-debt`).
  - Engineering culture or process changes (use `engineering-culture`).

---

## 2) Shared Capabilities Inventory + Platformization Plan

### Shared Capabilities Inventory

| Capability | Current duplication (where/how) | Consumer teams/services | Proposed platform contract (API/schema/SDK) | Migration approach | Expected impact | Risks |
|---|---|---:|---|---|---|---|
| **Data Export Service** | 4+ teams each built CSV/Excel/PDF export with own queuing, formatting, progress tracking. Different timeout handling, file size limits, and error behavior across teams. | 5 | REST API: `POST /platform/exports` (accepts query definition, format, delivery method). Async job with webhook/polling status. SDK wrapper for common languages. Returns signed download URL. | Phase 1: New exports use platform service. Phase 2: Migrate existing exports team-by-team with adapter shim (old endpoints proxy to new service). Phase 3: Deprecate team-specific implementations over 2 sprints per team. | Eliminates ~3 weeks/quarter of duplicated export work across teams. Consistent UX (progress bars, retry, size limits). Single place to enforce export audit logging for compliance. | Migration friction if teams have custom export formats. Must support current file-size limits during transition. |
| **Filtering & Query Engine** | 4+ teams built bespoke filtering UIs and query builders. Different syntax, operators, and performance characteristics. Some teams hit Postgres directly; others use materialized views. | 6 | Internal SDK/library: `FilterEngine.build(schema, filters) -> SQL/query`. Shared filter grammar (field, operator, value, combinator). Server-side validation and query plan analysis (reject queries exceeding cost threshold). | Phase 1: Ship SDK as internal package; new features adopt it. Phase 2: Teams wrap existing filters with adapter that delegates to SDK. Phase 3: Remove bespoke query builders over 3-month window. | Consistent filter behavior across product. Single optimization point for query performance. Blocks dangerous queries before they hit Postgres. | Filter grammar must be expressive enough for all current use cases. Performance regression risk if SDK adds overhead; mitigate with benchmarking. |
| **Permissions Service** | 3+ teams implemented role checks, feature flags, and entitlement gates independently. Inconsistent enforcement (some check at API layer, some at DB layer, some at UI only). | 7 | gRPC service: `PermissionsService.Check(subject, action, resource) -> {allowed, reason}`. Policy-as-code (OPA/Cedar). SDK with middleware for common frameworks. Caching layer (local + distributed) with TTL-based invalidation. | Phase 1: Deploy permissions service alongside existing checks (shadow mode -- log discrepancies, don't enforce). Phase 2: Flip enforcement to platform service per team/endpoint. Phase 3: Remove inline permission logic. | Consistent access control (critical for enterprise/SOC 2). Single audit log for all permission decisions. Eliminates ~2 weeks/quarter of duplicated authz work. | Shadow mode must run long enough to catch edge cases. Latency budget: permission checks must add < 5 ms p99. Cache invalidation bugs could cause access control failures. |

### Platformization Decisions

- **What becomes a shared primitive (and why):**
  - **Export** -- 5 consumers, high duplication, compliance requirement for audit trail. Stable contract surface (input: query + format; output: file).
  - **Filtering** -- 6 consumers, highest duplication count, and directly tied to Postgres performance problems (unoptimized queries). Centralizing this is also a scaling lever.
  - **Permissions** -- 7 consumers (every team needs it), enterprise customers require consistent RBAC, and SOC 2 demands a single audit trail. Inconsistent enforcement is a security risk.

- **What remains product-specific (and why):**
  - **Visualization rendering** -- highly product-specific; each analytics view has unique charting/rendering needs. Not enough commonality for a shared primitive yet.
  - **Notification preferences** -- only 2 teams use notifications today and the UX requirements differ significantly. Revisit when a third consumer appears.
  - **Custom report scheduling** -- closely tied to individual product domains; too early to abstract.

- **Ownership model:**
  - Dedicated **Platform Services team** (4-6 engineers, carved from feature teams + 2 new hires). This team owns the shared services, SLOs, and migration support.
  - Feature teams own integration/migration of their code to platform services. Platform team provides pairing support during migration sprints.

- **Versioning + backwards compatibility plan:**
  - Semantic versioning for all platform service APIs and SDKs.
  - **Breaking changes require a 2-sprint deprecation window** with migration guide.
  - Export and Permissions services: versioned API paths (`/v1/`, `/v2/`). Old versions supported for 3 months after new version GA.
  - Filtering SDK: major version bumps require opt-in; minor/patch versions are backward-compatible.

---

## 3) Quality Attributes Spec (SLOs/SLIs + Privacy/Safety)

### Reliability Targets

- **Availability:** 99.9% measured monthly for all tier-1 user journeys (see SLO table below). This translates to ~43 minutes of allowed downtime per month.
- **Error rate:** < 0.1% 5xx error rate on tier-1 APIs measured over rolling 7-day windows.
- **MTTR (Mean Time to Recover):** < 30 minutes for P0 incidents (complete service unavailability); < 2 hours for P1 (degraded but functional).
- **Error budget policy:** When monthly error budget is < 25% remaining, freeze non-critical deployments and prioritize reliability work until budget resets.

### Performance Targets

- **Dashboard load (primary journey):** p95 < 2 seconds, p99 < 4 seconds end-to-end.
- **API response (CRUD operations):** p95 < 200 ms, p99 < 500 ms.
- **Export jobs:** Initiation < 1 second; completion for datasets < 100 MB within 60 seconds. Larger exports: progress updates every 10 seconds.
- **Permission checks:** p99 < 5 ms (cached), p99 < 50 ms (uncached).
- **Filter query execution:** p95 < 500 ms for standard filters; queries exceeding 5 seconds are killed and user is prompted to narrow scope.

### Privacy/Safety Requirements

- **Encryption:** TLS 1.2+ in transit; AES-256 at rest for all data stores (Postgres, object storage, caches).
- **Access control:** RBAC enforced through the Permissions Service for all API endpoints. No direct DB access from application code without going through the service layer.
- **Data residency:** Prepare for regional deployment (US, EU) to support enterprise data residency requirements. Architecture must support tenant-level data isolation.
- **Retention:** Define retention policies per data class: operational data (2 years), audit logs (7 years), analytics events (1 year raw, aggregated indefinitely). Automated purge jobs.
- **Audit trail:** All permission checks, data exports, and admin actions logged to immutable audit store. Required for SOC 2 Type II.

### Operability Requirements

- **Dashboards:** Unified platform health dashboard (Datadog/Grafana) covering: DB metrics, API latency/error rates, export job queue depth, permission service latency, SLO burn rate.
- **Alerts:** PagerDuty integration. Alert on SLO burn rate (fast burn: 10x consumption rate, slow burn: 2x consumption rate). DB-specific alerts on connection count, replication lag, disk usage, query duration.
- **Runbooks:** One runbook per P0 scenario (DB failover, permission service outage, export queue backup, full disk). Runbooks linked from alert definitions.
- **On-call:** Platform team owns a dedicated on-call rotation. Feature teams handle product-specific incidents but escalate to platform on-call for shared service issues.

### Cost Guardrails

- **Top drivers:** Postgres (compute + storage), application compute (Kubernetes), object storage (exports), observability tooling.
- **Monthly budget caps:** Set alerts at 80% and 100% of monthly infrastructure budget. Any single service exceeding 120% of its allocation triggers cost review.
- **Optimization targets:** Reduce per-query cost by 40% through filtering engine optimization and read replica routing. Export storage: auto-expire files after 7 days.

### Proposed SLOs/SLIs

| User journey / API | SLI | SLO target | Measurement method | Owner | Notes |
|---|---|---|---|---|---|
| Dashboard load (primary) | Time from request to interactive render | p95 < 2 s, p99 < 4 s | RUM (Real User Monitoring) + synthetic checks every 60 s | Product Eng + Platform | Tier-1 journey; measured end-to-end including API + rendering |
| API CRUD operations | Server-side latency (request received to response sent) | p95 < 200 ms, p99 < 500 ms | Application metrics (histogram) | Platform team | Excludes network transit; measured at load balancer |
| Data export completion | Time from job creation to download-ready | < 60 s for datasets < 100 MB | Export service metrics (job duration histogram) | Platform team | Larger exports measured separately; SLO applies to 90th percentile of jobs |
| Permission check latency | Latency of `Check()` RPC | p99 < 5 ms (cached), p99 < 50 ms (uncached) | gRPC service metrics | Platform team | Cache hit rate target: > 95% |
| Overall availability | Successful requests / total requests (excluding maintenance) | 99.9% monthly | Load balancer access logs + health checks | SRE / Platform team | 43 min downtime budget per month |
| Filter query execution | Query execution time for standard filter operations | p95 < 500 ms | DB query metrics + application instrumentation | Platform team | Queries exceeding 5 s are killed; tracked separately as "timeout rate" |

---

## 4) Scaling "Doomsday Clock" + Capacity Plan

### Doomsday Clock

| Component/limit | Metric | Current | Trigger threshold | Estimated lead time to mitigate | Mitigation project | Owner |
|---|---|---:|---:|---|---|---|
| **Postgres disk (500 GB)** | Total DB size (GB) | 500 GB | 650 GB (70% of typical managed instance max before perf cliff) | 6-8 weeks | Data archival + partitioning (see below) | Platform lead |
| **Postgres IOPS** | Read/Write IOPS | ~8,000 (est.) | 12,000 (80% of provisioned IOPS on current instance class) | 4-6 weeks | Read replica routing for analytics queries + connection pooler (PgBouncer) | Platform lead |
| **Postgres connections** | Active connections | ~150 (est.) | 300 (75% of max_connections, typically 400 on managed instances) | 2-3 weeks | PgBouncer connection pooling; review connection lifecycle in application code | Platform eng |
| **Postgres query latency** | p95 query duration (ms) | ~800 ms (est., degrading) | 500 ms (target), 1,500 ms (critical) | 4-6 weeks | Separate OLTP/OLAP workloads; read replicas for heavy analytics; query optimization via filtering engine | Platform lead |
| **Postgres replication lag** | Replica lag (seconds) | < 1 s (est.) | 10 s sustained | 2-3 weeks | Investigate write amplification; tune WAL settings; consider logical replication for selective tables | Platform eng |
| **Application compute (K8s)** | CPU/memory utilization across pods | ~55% (est.) | 75% sustained over 1 hour | 1-2 weeks | Horizontal auto-scaling policy; right-size pod resource requests | SRE |
| **Export queue depth** | Pending export jobs | ~20 (est.) | 200 (indicates backlog buildup) | 1-2 weeks | Auto-scale export workers; implement priority queue (enterprise jobs first) | Platform eng |
| **Object storage (exports)** | Total stored export files (GB) | ~50 GB (est.) | 500 GB (cost threshold) | 1 week | Auto-expire exports after 7 days; lazy-generate on re-request | Platform eng |

### Capacity Plan

**Top scaling risks (ordered by time-to-breach):**

1. **Postgres disk + query latency (CRITICAL -- breach in ~3 months at current growth):** At 5x traffic growth, the 500 GB database will approach managed instance limits within 3 months. Query latency is already degrading, indicating the problem is immediate.
2. **Postgres IOPS + connections (HIGH -- breach in ~4 months):** 5x traffic means ~5x connection demand and proportional IOPS increase. Connection pooling buys time but doesn't solve the fundamental read/write contention.
3. **Export queue saturation (MEDIUM -- breach in ~5 months):** Enterprise customers will drive heavier export usage; queue must scale horizontally.

**Proposed scaling projects (sequenced by urgency):**

**Project S1: Postgres Workload Separation (Month 1-2)**
- Separate OLTP (transactional) and OLAP (analytical/reporting) workloads.
- Route read-heavy analytics queries to dedicated read replicas.
- Deploy PgBouncer for connection pooling (reduce active connections by ~60%).
- Expected outcome: Buys 6+ months of headroom on connections and IOPS.

**Project S2: Data Archival + Table Partitioning (Month 2-3)**
- Implement time-based partitioning on the largest tables (event logs, audit trails, analytics data).
- Archive data older than 12 months to cold storage (S3 + Athena for ad-hoc queries).
- Target: Reduce active DB size from 500 GB to ~200 GB.
- Expected outcome: Significant improvement in query performance; disk pressure eliminated for 12+ months.

**Project S3: Filtering Engine Query Optimization (Month 2-4)**
- Deploy the shared Filtering SDK with built-in query cost analysis.
- Kill queries exceeding cost threshold; guide users to narrow filters.
- Add query plan caching for common filter patterns.
- Expected outcome: 40% reduction in average query cost; eliminates runaway queries.

**Project S4: Evaluate Postgres Vertical Upgrade vs. Citus/Read Scaling (Month 3-4)**
- If S1-S3 are insufficient for 5x headroom, evaluate:
  - **Option A:** Vertical upgrade to larger instance class (quick but has ceiling).
  - **Option B:** Citus extension for horizontal scaling (distributes large tables across nodes).
  - **Option C:** Introduce a dedicated analytical data store (ClickHouse/Redshift) for reporting workloads, keeping Postgres lean for OLTP.
- Decision criteria: cost, migration complexity, operational burden, and headroom provided.

**Feature-freeze / priority policy when triggers fire:**
- **Yellow (trigger threshold reached):** Scaling work becomes P1; no new features that increase DB load. Platform team gets 2 additional engineers from feature teams.
- **Red (critical threshold reached):** Full feature freeze on DB-intensive work. All available engineers support scaling mitigation. Stakeholder communication within 4 hours of red status.
- **Monitoring:** Weekly capacity review meeting (30 min) until all metrics are below 50% of trigger thresholds.

---

## 5) Instrumentation Plan (Observability + Server-Side Analytics)

### Observability Gaps

| Area | Current state | Gap | Proposed instrumentation | Owner | Priority |
|---|---|---|---|---|---|
| **Database metrics** | Basic uptime monitoring | No query-level latency tracking, no connection pool metrics, no replication lag alerts | Postgres exporter (prometheus) + PgBouncer metrics. Dashboards: query duration histograms, connection utilization, replication lag, table bloat, cache hit ratio. Alerts: p95 query > 500 ms, connections > 300, replication lag > 10 s. | Platform eng | P0 |
| **SLO burn rate** | No SLOs defined | No burn-rate tracking or alerting | Implement SLO tracking (Datadog SLO monitors or Prometheus + sloth). Multi-window burn-rate alerts (fast: 5 min window, slow: 1 hr window). Dashboard showing remaining error budget per SLO. | SRE / Platform | P0 |
| **Platform service health** | N/A (services don't exist yet) | No metrics for new shared services | Each platform service (Export, Filtering, Permissions) ships with: request rate, error rate, latency histograms, queue depth (export), cache hit rate (permissions). Standard RED metrics dashboard per service. | Platform eng | P1 (ship with services) |
| **Distributed tracing** | Partial or absent | Cannot trace a request end-to-end across services | Deploy OpenTelemetry SDK across all services. Trace context propagation through HTTP headers and gRPC metadata. Sample rate: 100% for errors, 10% for success in production. | Platform eng | P1 |
| **Cost monitoring** | Cloud provider billing dashboard only | No per-service or per-feature cost attribution | Tag all infrastructure resources by service/team. Weekly automated cost report. Alert on >20% week-over-week increase per service. | SRE | P2 |
| **Export job observability** | Basic job success/fail logging | No duration tracking, no queue depth visibility, no per-tenant metrics | Export service emits: job_created, job_started, job_completed, job_failed events with duration, file size, tenant_id. Dashboard: queue depth, completion time histogram, failure rate by type. | Platform eng | P1 |

### Server-Side Analytics Event Contract

- **Canonical identity fields:**
  - `user_id` (UUID) -- authenticated user; always present for logged-in actions.
  - `account_id` (UUID) -- the organization/tenant; always present.
  - `anonymous_id` (UUID) -- generated client-side for pre-auth tracking; merged to `user_id` on login via server-side merge event.
  - **Merge rules:** On authentication, emit `identity_merged(anonymous_id, user_id, account_id)`. Analytics pipeline deduplicates and re-attributes pre-auth events to the resolved user.

- **Delivery semantics:**
  - **At-least-once** delivery from application to event bus (Kafka/SQS).
  - **Dedupe strategy:** Every event carries a `event_id` (UUID v7, time-sortable). Consumers deduplicate on `event_id` within a 24-hour window.
  - Events are produced server-side at the point of action completion (not on request receipt).

- **Schema/versioning:**
  - JSON Schema registry (e.g., SchemaStore in a git repo or a schema registry service).
  - Events follow `noun.verb` naming convention (e.g., `export.completed`, `filter.applied`, `permission.checked`).
  - Schema changes require a PR review; breaking changes produce a new event version (`export.completed.v2`) with a 3-month overlap period.

- **Data QA checks:**
  - **Schema validation:** Events validated against JSON Schema at production time (reject malformed events to dead-letter queue).
  - **Volume anomaly detection:** Alert if any event type volume drops > 50% or increases > 300% compared to 7-day rolling average.
  - **Null-rate checks:** Alert if required fields have null rate > 1%.
  - **Dedupe rate monitoring:** Track duplicate event rate; alert if > 5% (indicates producer retry storms).

### Event Taxonomy (Starter Table)

| Event name | When emitted (server action) | Required properties | Identity fields | Consumers (teams) | Notes |
|---|---|---|---|---|---|
| `dashboard.loaded` | Server completes data fetch for dashboard render | `dashboard_id`, `query_count`, `total_duration_ms`, `data_points_returned` | `user_id`, `account_id` | Product analytics, Performance monitoring | Primary journey; correlate with RUM for full picture |
| `export.requested` | Export job created in queue | `export_id`, `format` (csv/xlsx/pdf), `estimated_rows`, `filter_hash` | `user_id`, `account_id` | Platform team, Product analytics | Track export patterns to optimize common formats |
| `export.completed` | Export file ready for download | `export_id`, `format`, `file_size_bytes`, `duration_ms`, `row_count` | `user_id`, `account_id` | Platform team, Billing (large exports) | Used for SLO measurement |
| `export.failed` | Export job fails after retries exhausted | `export_id`, `error_type`, `error_message`, `retry_count` | `user_id`, `account_id` | Platform team, SRE | Triggers alert if failure rate > 2% |
| `filter.applied` | Filter query executed via Filtering SDK | `filter_hash`, `field_count`, `query_duration_ms`, `rows_scanned`, `rows_returned` | `user_id`, `account_id` | Platform team, Product analytics | Feeds query optimization; identifies expensive patterns |
| `filter.rejected` | Query killed due to cost threshold | `filter_hash`, `estimated_cost`, `threshold`, `rejection_reason` | `user_id`, `account_id` | Platform team, Product (UX improvement) | Track to improve filter UX guidance |
| `permission.checked` | Permission service processes a Check() call | `subject_id`, `action`, `resource_type`, `resource_id`, `result` (allowed/denied), `latency_ms`, `cache_hit` | `user_id`, `account_id` | Security, Compliance/Audit | High-volume; sample at 10% for analytics, 100% for audit log |
| `permission.denied` | Permission check returns denied | `subject_id`, `action`, `resource_type`, `resource_id`, `reason` | `user_id`, `account_id` | Security, Product (UX -- show proper error) | 100% capture; used for security review |
| `identity.merged` | User authenticates, linking anonymous to known | `anonymous_id`, `method` (password/sso/oauth) | `user_id`, `account_id`, `anonymous_id` | Analytics pipeline | Triggers re-attribution of pre-auth events |
| `account.limit_approached` | Tenant usage approaches plan limit | `limit_type`, `current_value`, `limit_value`, `percentage_used` | `account_id` | Billing, Customer Success, Product | Drives upsell and capacity planning |

---

## 6) Discoverability Plan

**Not applicable.** This is a B2B SaaS analytics product, not a content-heavy web property. SEO/discoverability is not a primary concern for the application itself. Marketing site SEO is out of scope for this infrastructure plan.

---

## 7) Execution Roadmap

Prioritized by **blast radius** (how many teams/users are affected if we don't act) crossed with urgency (time-to-breach).

### Roadmap

| Milestone | Scope | Acceptance criteria | Owner | Dependencies | ETA range | Rollout/rollback |
|---|---|---|---|---|---|---|
| **M0: Platform Team Formation** | Hire/reassign 4-6 engineers; establish platform team charter, on-call rotation, and communication channels | Team staffed; charter published; on-call rotation active; Slack channel + weekly sync established | VP Engineering | Budget approval; backfill plan for feature teams | Week 1-2 | N/A |
| **M1: Emergency DB Relief (PgBouncer + Read Replicas)** | Deploy PgBouncer connection pooler; route analytics read queries to dedicated read replica(s) | Active connections reduced by >= 50%; analytics queries running on replica; p95 query latency reduced by >= 30% | Platform lead | M0 (team exists); DBA access to Postgres config | Week 2-4 | Rollback: disable PgBouncer and revert DNS/connection strings to primary. Read replica routing toggled via feature flag. |
| **M2: Observability Foundation** | Deploy Postgres metrics exporter, SLO tracking, distributed tracing (OpenTelemetry), platform health dashboards | All SLO dashboards live; burn-rate alerts firing; DB metrics (connections, IOPS, replication lag, query duration) visible; tracing deployed to >= 3 critical services | SRE / Platform eng | M0; observability tooling access (Datadog/Grafana) | Week 3-5 | Rollback: disable exporters/agents if perf impact; dashboards are additive (no rollback needed). |
| **M3: Permissions Service (Shadow Mode)** | Deploy permissions service; integrate with 2 pilot teams in shadow mode (log-only, no enforcement) | Service deployed; shadow mode processing 100% of permission checks for pilot teams; discrepancy rate tracked on dashboard; latency < 5 ms p99 (cached) | Platform eng | M0; policy language chosen (OPA/Cedar); pilot teams identified | Week 4-8 | Rollback: disable shadow mode integration (feature flag per team). No user impact since shadow mode is non-enforcing. |
| **M4: Data Archival + Table Partitioning** | Partition largest tables by time; archive data > 12 months to cold storage (S3); verify query performance improvement | Active DB size reduced to < 250 GB; archived data queryable via Athena; no data loss verified via row-count reconciliation; p95 query latency improved by >= 40% | Platform lead + DBA | M1 (read replicas for safe migration); M2 (monitoring to verify) | Week 5-9 | Rollback: partitioning is additive; if issues, queries can still access all partitions. Archive has 30-day restore window from S3. |
| **M5: Filtering SDK (v1)** | Ship internal Filtering SDK with query cost analysis; integrate with 2 pilot teams | SDK published as internal package; 2 teams using it in production; queries exceeding cost threshold are rejected; average query cost reduced by >= 25% for pilot teams | Platform eng | M1 (read replicas reduce load); M2 (query metrics to measure improvement) | Week 6-10 | Rollback: teams revert to direct query building (SDK is opt-in via import). Feature flag to disable cost-threshold rejection. |
| **M6: Permissions Service (Enforcement)** | Flip from shadow mode to enforcement for pilot teams; roll out to remaining teams | All teams enforcing via platform permissions service; discrepancy rate < 0.1%; audit log capturing 100% of permission decisions; SOC 2 audit trail requirement met | Platform eng + Security | M3 (shadow mode validated); M2 (monitoring in place) | Week 8-12 | Rollback: per-team feature flag reverts to inline permission checks. Gradual rollout: 1 team per week. |
| **M7: Export Service (v1)** | Deploy shared export service; migrate 2 pilot teams | Export service handling production traffic for 2 teams; async job processing with status tracking; export SLO met (< 60 s for < 100 MB); audit logging active | Platform eng | M2 (observability); M5 (filtering SDK for export query building) | Week 9-14 | Rollback: pilot teams revert to existing export code (old endpoints remain active during migration). Traffic split via feature flag. |
| **M8: Full Rollout + Scaling Evaluation** | All teams on platform services (filtering, permissions, export); evaluate need for S4 (Citus/vertical upgrade/analytical store) | >= 6 teams consuming each platform service; all SLOs met for 2 consecutive weeks; scaling evaluation document published with recommendation | Platform lead | M4-M7 complete; 4 weeks of production data on new architecture | Week 14-20 | Rollback: per-team feature flags for each service. Scaling evaluation informs next phase (no rollback needed). |
| **M9: Enterprise Readiness Certification** | Validate all SLOs met under load test simulating 5x traffic; SOC 2 controls verified; runbooks tested via game day | Load test passes with all SLOs green at 5x current traffic; SOC 2 evidence package complete; 1 game day executed with < 30 min MTTR | VP Engineering + Platform lead + Security | M6, M7, M8 complete; load testing infrastructure | Week 20-24 | N/A (validation milestone). If SLOs fail under load test, trigger S4 scaling project immediately. |

### Sequencing Rationale (Blast Radius Priority)

1. **M0-M1 (Weeks 1-4): Stop the bleeding.** DB is the single point of failure for all 50 engineers and all customers. PgBouncer + read replicas are the highest-blast-radius, lowest-effort wins.
2. **M2 (Weeks 3-5): See before you act.** Without observability, every subsequent decision is guesswork. This is foundational.
3. **M3/M4 (Weeks 4-9): Permissions + DB scaling in parallel.** Permissions affects all 7 consumer teams (highest blast radius among shared capabilities). DB archival/partitioning addresses the most urgent scaling risk.
4. **M5/M6 (Weeks 6-12): Filtering + Permissions enforcement.** Filtering SDK directly reduces DB load (scaling lever) and improves developer velocity. Permissions enforcement completes the security/compliance story.
5. **M7 (Weeks 9-14): Export.** Important but lower blast radius than permissions and filtering; fewer teams blocked and no security/compliance urgency.
6. **M8-M9 (Weeks 14-24): Consolidation + certification.** Full rollout, scaling evaluation, and enterprise readiness validation.

---

## 8) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Platform team staffing delay** -- cannot hire or reassign 4-6 engineers quickly enough | Medium | High (entire roadmap slips) | Begin internal reassignment immediately (2-3 engineers); hire for remaining slots in parallel. Feature teams accept temporary velocity reduction. |
| **Postgres hits critical threshold before M1 completes** -- query latency becomes unacceptable before PgBouncer/replicas are ready | Medium | High (customer-facing outages) | Fast-track M1 to 2-week delivery. Prepare emergency vertical upgrade as backup (can execute in days). Implement query timeout (kill queries > 10 s) as immediate stopgap. |
| **Migration friction underestimated** -- teams resist or are slower than expected to adopt platform services | Medium | Medium (roadmap extends 4-8 weeks) | Dedicated migration support from platform team (pairing). Executive mandate from VP Eng. Track migration per-team on weekly dashboard. |
| **Permission service shadow mode reveals deep inconsistencies** -- existing permission implementations disagree significantly | Medium | Medium (delays enforcement) | Extend shadow mode by 2-4 weeks. Triage discrepancies by severity: fix critical ones immediately, defer cosmetic ones. Document "golden" behavior as the authoritative source. |
| **5x traffic growth arrives faster than 6 months** -- enterprise deals close early or marketing spike occurs | Low | High (DB/infra crisis) | M1 (DB relief) must complete in 4 weeks regardless. Maintain "emergency scaling playbook" (vertical upgrade + aggressive caching) as a break-glass option. |
| **SOC 2 audit requirements are broader than anticipated** -- additional controls needed beyond permissions audit trail | Medium | Medium (scope creep) | Engage security/compliance consultant in Week 1-2 to enumerate full control requirements. Build controls inventory in parallel with M3. |

### Open Questions

1. **Postgres managed service or self-hosted?** If managed (e.g., AWS RDS/Aurora), what is the current instance class and max scaling tier? This affects the ceiling for vertical upgrades and available extensions (Citus).
2. **How many distinct permission models exist across teams?** Need an audit of current RBAC/ACL implementations to understand the scope of consolidation into the permissions service.
3. **Is there an existing data warehouse or analytics pipeline?** If yes, the export service and analytics event contract can leverage it; if no, we need to factor pipeline setup into the roadmap.
4. **What is the current deployment model (K8s, ECS, bare metal)?** This affects how platform services are deployed and how auto-scaling is configured.
5. **Are there existing enterprise customer SLA commitments?** If contractual SLAs already exist, they constrain our SLO targets (SLOs must be stricter than SLAs).
6. **What is the budget for infrastructure scaling?** Vertical Postgres upgrades and Citus licensing have different cost profiles; need budget parameters to recommend the right option.
7. **Is there an existing on-call rotation, or is this being created from scratch?** Affects M0 timeline and platform team formation.

### Next Steps

1. **This week:** VP Engineering approves platform team formation (M0). Identify 2-3 engineers to reassign immediately. Post job requisitions for remaining slots.
2. **This week:** DBA/platform lead begins M1 -- deploy PgBouncer in staging; configure read replica routing. Target production deployment in 2 weeks.
3. **This week:** Run a 1-hour audit of existing permission implementations across all teams. Document the current state to scope M3.
4. **Week 2:** Finalize observability tooling choices (Datadog vs. Grafana stack) and begin M2 implementation.
5. **Week 2:** Publish this Platform & Infrastructure Improvement Pack to all engineering teams. Schedule 30-minute walkthrough for stakeholders.
6. **Week 3:** Hold first weekly capacity review meeting (30 min). Review doomsday clock metrics and track progress on M1.
7. **Week 4:** Evaluate M1 results. If insufficient, fast-track S4 evaluation (vertical upgrade vs. Citus vs. analytical store).
8. **Ongoing:** Bi-weekly platform team retrospective to assess migration progress and surface blockers.

---

## Quality Gate Self-Assessment

### Checklist Verification

**A) Scope + contracts**
- [x] "When to use / When NOT to use" is explicit; redirects to `platform-strategy`, `technical-roadmaps`, `managing-tech-debt`, and `engineering-culture`.
- [x] Inputs are sufficient; missing info handled via 5 explicit assumptions (A1-A5).
- [x] Deliverables are explicit and ordered (sections 1-8).

**B) Platformization quality**
- [x] All 3 shared capability candidates have 2+ consumers (Export: 5, Filtering: 6, Permissions: 7).
- [x] Each has a proposed contract (REST API, internal SDK, gRPC service) and ownership model.
- [x] Migration/rollout plan exists per capability (phased with shims, shadow mode, deprecation windows).

**C) Infrastructure quality attributes**
- [x] Reliability and performance targets are measurable (SLOs/SLIs table with specific numbers).
- [x] Privacy/safety requirements spelled out (encryption, residency, retention, audit).
- [x] Operability covered (dashboards, alerts, runbooks, on-call).
- [x] Cost guardrails included (budgets, alerts, optimization targets).

**D) Scaling readiness ("doomsday clock")**
- [x] 8 limits enumerated with current values (or explicit estimates).
- [x] Trigger thresholds account for lead time (e.g., disk trigger at 650 GB with 6-8 week lead time).
- [x] Each trigger has an owner and named mitigation project.
- [x] Clear yellow/red policy for reprioritization/feature freeze.

**E) Instrumentation + analytics**
- [x] 6 observability gaps identified with owners and priorities.
- [x] 10 canonical events captured server-side.
- [x] Identity strategy defined (user_id, account_id, anonymous_id) with merge rules.
- [x] Data quality checks defined (schema validation, volume anomalies, null rates, dedupe rates).

**F) Discoverability**
- [x] Explicitly marked "Not applicable" with rationale.

**G) Execution readiness**
- [x] 10 milestones with acceptance criteria and owners.
- [x] Dependencies and rollout/rollback plans included for every milestone.
- [x] Risks (6), open questions (7), and next steps (8) are present and actionable.
