# Platform & Infrastructure Improvement Plan

## B2B Analytics SaaS — Series B, 50 Engineers

---

## 1. Shared Capabilities Plan

### 1.1 Problem Statement

Multiple feature teams are independently rebuilding export functionality, filtering logic, and permission checks. This results in:

- **Duplicated effort**: Engineering hours wasted re-implementing solved problems
- **Inconsistent behavior**: Users experience different filtering semantics, export formats, and permission enforcement across features
- **Maintenance burden**: Bug fixes and improvements must be applied in multiple places
- **Security risk**: Permission checks implemented ad hoc increase the surface area for authorization bugs

### 1.2 Shared Capability Inventory

| Capability | Current State | Estimated Duplication |
|---|---|---|
| Export (CSV, Excel, PDF) | Rebuilt per feature team | 4-6 implementations |
| Filtering & query building | Custom per feature | 5+ implementations |
| Permission / authorization checks | Inline per endpoint | Scattered across codebase |
| Pagination | Mixed cursor/offset | 3-4 implementations |
| Audit logging | Partial coverage | Inconsistent |
| Rate limiting | Ad hoc or missing | Varies |

### 1.3 Recommended Shared Services Architecture

#### A. Export Service

- **Scope**: Centralized async export pipeline supporting CSV, Excel, PDF, and scheduled exports
- **Design**:
  - Accept a standardized export request (data source, filters, format, recipient)
  - Use a job queue (e.g., Redis-backed Sidekiq, or a dedicated task queue) for async processing
  - Store generated files in object storage (S3/GCS) with signed URLs
  - Notify users via webhook/email on completion
- **API Contract**:
  ```
  POST /api/v1/exports
  {
    "source": "dashboard_metrics",
    "filters": { ... },
    "format": "csv",
    "notify": "email"
  }
  ```
- **Benefits**: Uniform format support, centralized size limits, progress tracking, retry logic

#### B. Filtering & Query Engine

- **Scope**: Shared filter definition, parsing, validation, and SQL generation
- **Design**:
  - Define a filter DSL (JSON-based) that all feature teams use
  - Central library validates filter syntax, prevents injection, applies tenant scoping
  - Generates parameterized SQL or query builder calls
  - Supports common operations: equality, range, contains, in-list, date ranges, null checks
- **Filter Schema Example**:
  ```json
  {
    "filters": [
      { "field": "created_at", "op": "gte", "value": "2026-01-01" },
      { "field": "status", "op": "in", "value": ["active", "trial"] }
    ],
    "sort": { "field": "created_at", "dir": "desc" }
  }
  ```
- **Benefits**: Consistent UX, single place for query optimization, SQL injection prevention

#### C. Authorization Service

- **Scope**: Centralized permission evaluation replacing inline checks
- **Design**:
  - Implement a policy engine (consider OPA/Rego, Casbin, or custom RBAC/ABAC service)
  - Define resources, actions, and roles in a central policy store
  - Expose a lightweight SDK that feature teams call: `authz.check(user, action, resource)`
  - Cache permission evaluations with short TTLs for hot paths
  - Emit audit events for every authorization decision
- **Migration Path**:
  1. Catalog all existing permission checks across the codebase
  2. Map them to a unified role/permission model
  3. Implement the central service with a compatibility shim
  4. Migrate teams incrementally (one feature area per sprint)
  5. Remove legacy inline checks after validation
- **Benefits**: Single source of truth for access control, auditable, easier compliance (SOC 2, etc.)

### 1.4 Platform Team Structure

- **Recommendation**: Form a dedicated Platform Engineering team (3-5 engineers initially)
- **Charter**: Own shared capabilities, define APIs, provide SDKs, maintain SLOs for platform services
- **Operating Model**:
  - Platform team builds and maintains core services
  - Feature teams consume via well-documented SDKs and APIs
  - Platform team holds office hours and reviews integration PRs
  - Shared capabilities are versioned; breaking changes follow a deprecation policy

### 1.5 Migration Strategy

| Phase | Duration | Focus |
|---|---|---|
| Phase 1 | Weeks 1-4 | Catalog existing implementations, define unified APIs |
| Phase 2 | Weeks 5-10 | Build Export Service and Filter Engine v1 |
| Phase 3 | Weeks 8-14 | Build Authorization Service v1 (overlapping) |
| Phase 4 | Weeks 12-20 | Migrate feature teams (1-2 teams per sprint) |
| Phase 5 | Weeks 20-24 | Deprecate and remove legacy implementations |

---

## 2. Postgres Scaling Analysis

### 2.1 Current State Assessment

| Metric | Current | Concern Level |
|---|---|---|
| Database size | 500 GB | Moderate — approaching practical limits for single-node |
| Query latency | Increasing | High — user-facing impact |
| Expected growth | 5x in 6 months | Critical — 2.5 TB without intervention |
| Connection count | Likely growing with team/feature count | Moderate |
| Write volume | Unknown but likely growing with analytics ingestion | High |

### 2.2 Immediate Optimizations (Weeks 1-4)

These require no architectural changes and can deliver quick wins:

#### A. Query Performance Audit
- Run `pg_stat_statements` to identify the top 20 slowest and most frequent queries
- Use `EXPLAIN ANALYZE` on each; look for sequential scans, missing indexes, and poor join plans
- Add targeted indexes (partial indexes, covering indexes, expression indexes as needed)
- Identify and fix N+1 query patterns in application code

#### B. Connection Pooling
- Deploy PgBouncer in transaction mode if not already present
- Target: reduce active connections from potentially hundreds to a managed pool (50-100 server connections)
- This alone often improves p99 latency significantly

#### C. Configuration Tuning
- Review and optimize: `shared_buffers` (25% of RAM), `effective_cache_size` (75% of RAM), `work_mem`, `maintenance_work_mem`
- Enable `pg_stat_monitor` for detailed query analytics
- Set `random_page_cost` appropriately for SSD storage (1.1-1.5)

#### D. Table Maintenance
- Identify bloated tables with `pgstattuple`; run targeted `VACUUM FULL` during maintenance windows
- Check for unused indexes consuming write overhead
- Add table partitioning to the largest tables (likely time-series analytics data) using native declarative partitioning by date range

### 2.3 Medium-Term Scaling (Weeks 4-12)

#### A. Read Replicas
- Deploy 1-2 read replicas for analytics/reporting queries
- Route read traffic at the application level (or use a proxy like PgPool-II)
- Target: offload 60-80% of read traffic from primary
- Acceptable replication lag: <1 second for most analytics use cases

#### B. Table Partitioning
- Partition the largest tables (analytics events, audit logs, time-series metrics) by month or week
- Benefits: faster queries with partition pruning, easier data lifecycle management, parallel query execution
- Implementation:
  ```sql
  CREATE TABLE events (
    id bigint GENERATED ALWAYS AS IDENTITY,
    tenant_id uuid NOT NULL,
    created_at timestamptz NOT NULL,
    ...
  ) PARTITION BY RANGE (created_at);

  CREATE TABLE events_2026_q1 PARTITION OF events
    FOR VALUES FROM ('2026-01-01') TO ('2026-04-01');
  ```

#### C. Data Archival Strategy
- Define retention policies: hot data (0-90 days in primary), warm data (90-365 days in read replica or cheaper storage), cold data (>1 year in object storage/Parquet)
- Implement automated archival jobs that move old partitions
- Target: keep primary database under 500 GB even with 5x growth

#### D. Caching Layer
- Add Redis/Memcached for frequently-read, slowly-changing data:
  - Permission/role lookups (TTL: 60s)
  - Dashboard metadata and configuration (TTL: 300s)
  - Aggregated analytics results (TTL: varies by freshness requirement)
- Target: 40-60% cache hit rate for read queries, reducing DB load proportionally

### 2.4 Long-Term Architecture (Months 3-6)

#### A. Analytical Workload Separation (OLAP Split)
- Move heavy analytical queries to a dedicated analytical store
- Options:
  - **ClickHouse**: Excellent for time-series analytics, columnar storage, fast aggregations
  - **TimescaleDB**: If staying in the Postgres ecosystem is important
  - **BigQuery/Redshift**: If preferring managed services
- Stream data from Postgres via CDC (Debezium/Kafka Connect) to the analytical store
- Feature teams query the analytical store for dashboards and reports; Postgres handles transactional workloads

#### B. Sharding Evaluation
- If single-tenant queries dominate, consider tenant-based sharding using Citus or application-level sharding
- For a B2B SaaS with analytics, tenant-based sharding is natural since queries rarely cross tenant boundaries
- **Citus** (Postgres extension) can shard by `tenant_id` with minimal application changes
- Decision point: pursue sharding only if the OLAP split + read replicas + partitioning are insufficient

#### C. Connection Architecture
- Evaluate upgrading to a service mesh or sidecar proxy pattern for database connections
- Consider Postgres logical replication for zero-downtime migrations

### 2.5 Projected Capacity Timeline

| Milestone | Database Size | Strategy | Target Latency (p95) |
|---|---|---|---|
| Today | 500 GB | Single node | Degrading |
| Month 1 | 550 GB | Optimized queries + pooling | <200ms |
| Month 3 | 700 GB | Read replicas + partitioning + caching | <150ms |
| Month 6 | 800 GB primary + archive | OLAP split + archival | <100ms transactional, <2s analytical |
| Month 6 (without action) | ~2.5 TB | Unscalable | >1s, outages likely |

---

## 3. Reliability SLOs

### 3.1 SLO Framework

We recommend defining SLOs across four dimensions: availability, latency, correctness, and freshness.

### 3.2 Proposed SLOs

#### Tier 1 — User-Facing API (Dashboard, Core Analytics)

| SLI | SLO Target | Measurement |
|---|---|---|
| Availability | 99.9% (8.7 hours downtime/year) | Successful responses / total requests (exclude 4xx) |
| Latency (p50) | < 100ms | Server-side request duration |
| Latency (p95) | < 500ms | Server-side request duration |
| Latency (p99) | < 1,500ms | Server-side request duration |
| Error rate | < 0.1% | 5xx responses / total responses |

#### Tier 2 — Export & Batch Processing

| SLI | SLO Target | Measurement |
|---|---|---|
| Availability | 99.5% | Job processing success rate |
| Completion time (p95) | < 5 minutes for exports under 100K rows | Job start to file available |
| Completion time (p95) | < 30 minutes for exports under 1M rows | Job start to file available |
| Data correctness | 100% | Export matches query results at time of request |

#### Tier 3 — Internal Platform Services (AuthZ, Filtering)

| SLI | SLO Target | Measurement |
|---|---|---|
| Availability | 99.95% | Higher than Tier 1 since they are dependencies |
| Latency (p99) | < 50ms | Authorization check duration |
| Correctness | 100% | No false-positive authorizations ever |
| Cache hit rate | > 80% | For permission lookups |

#### Tier 4 — Database & Infrastructure

| SLI | SLO Target | Measurement |
|---|---|---|
| Database availability | 99.95% | Connection success rate |
| Replication lag | < 5 seconds (p99) | Replica lag metric |
| Query latency (p95) | < 200ms for transactional queries | pg_stat_statements |
| Backup RPO | < 1 hour | Time since last successful backup |
| Backup RTO | < 4 hours | Time to restore from backup |

### 3.3 Error Budget Policy

- **Budget**: With 99.9% availability SLO, the error budget is 0.1% per rolling 30-day window (~43 minutes/month)
- **When budget is healthy (>50% remaining)**: Normal feature velocity, deploy at will
- **When budget is stressed (10-50% remaining)**: Require additional review for risky deploys, increase monitoring
- **When budget is exhausted (<10% remaining)**: Freeze non-critical deploys, all engineering effort focuses on reliability until budget recovers
- **Review cadence**: Weekly SLO review in engineering standup, monthly SLO review with leadership

### 3.4 Observability Requirements

To measure these SLOs, implement:

1. **Metrics**: Prometheus/Datadog for request latency histograms, error rates, saturation
2. **Logging**: Structured JSON logs with request IDs, tenant IDs, and latency breakdowns
3. **Tracing**: Distributed tracing (Jaeger/Datadog APM) across all services, especially for the shared capability calls
4. **Dashboards**: One SLO dashboard per tier, visible to all engineers
5. **Alerting**:
   - Page (PagerDuty): >1% error rate sustained for 5 minutes, database primary down
   - Warn (Slack): SLO burn rate exceeding budget, replication lag >10s, export queue depth >100
6. **SLO Tracking Tool**: Consider Nobl9, Sloth, or a custom Prometheus recording rules setup

---

## 4. Execution Roadmap

### 4.1 Overview

The plan spans 6 months, divided into three phases. Each phase delivers independent value while building toward the full vision.

```
Month 1-2:  STABILIZE  — Quick wins, stop the bleeding
Month 3-4:  PLATFORM   — Build shared capabilities, scale reads
Month 5-6:  SCALE      — Analytical workload separation, full migration
```

### 4.2 Phase 1: Stabilize (Weeks 1-8)

**Goal**: Reduce immediate pain, establish foundations

| Week | Workstream | Deliverable | Owner | Dependencies |
|---|---|---|---|---|
| 1-2 | DB Performance | Query audit report; top 10 queries optimized | 1 Senior SRE + 1 Backend | pg_stat_statements access |
| 1-2 | Observability | SLO dashboards for Tier 1 and Tier 4 | 1 SRE | Metrics pipeline |
| 1-3 | Connection Pooling | PgBouncer deployed and configured | 1 SRE | Staging environment |
| 2-4 | Shared Capabilities | Catalog of all existing export/filter/authz implementations | Platform lead + feature team leads | Codebase access, interviews |
| 3-4 | DB Performance | Missing indexes added; bloated tables vacuumed | 1 SRE | Maintenance window |
| 3-6 | Read Replicas | 2 read replicas provisioned; read routing implemented | 1 SRE + 1 Backend | Infrastructure provisioning |
| 4-8 | Platform Team | Platform team formed (3 engineers); charter defined | Engineering leadership | Hiring/reallocation |
| 5-8 | API Design | Shared Export, Filter, and AuthZ API specs finalized (RFC process) | Platform team | Stakeholder review |

**Phase 1 Success Criteria**:
- p95 API latency reduced by 30%
- SLO dashboards operational
- Platform team staffed and chartered
- API specs approved by feature team leads

### 4.3 Phase 2: Platform Build (Weeks 9-16)

**Goal**: Deliver shared capabilities v1, partition database, begin migrations

| Week | Workstream | Deliverable | Owner | Dependencies |
|---|---|---|---|---|
| 9-12 | Export Service | Export Service v1 (CSV, Excel) with async processing | Platform team (2 eng) | Object storage, job queue |
| 9-12 | Filter Engine | Shared filter library v1 with SDK | Platform team (1 eng) | API spec |
| 9-14 | AuthZ Service | Authorization service v1 with policy engine | Platform team (2 eng) + 1 Security | Policy model |
| 10-12 | DB Partitioning | Top 3 largest tables partitioned by date range | 1 SRE + 1 Backend | Maintenance window, testing |
| 11-13 | Caching | Redis caching layer for permission lookups and dashboard metadata | 1 Backend | Redis infrastructure |
| 12-14 | Migration: Team 1 | First feature team migrated to shared Export + Filter | Platform team + Feature team 1 | Export Service v1, Filter v1 |
| 14-16 | Migration: Team 2-3 | Two more feature teams migrated | Platform team support | v1 services stable |

**Phase 2 Success Criteria**:
- Export Service handling 100% of Team 1's exports
- Filter Engine SDK adopted by 3 teams
- Authorization service evaluating permissions for at least 1 feature area
- Database primary under 500 GB with partitioning + archival active
- p95 latency < 200ms

### 4.4 Phase 3: Scale (Weeks 17-24)

**Goal**: Handle 5x traffic, complete migrations, operational maturity

| Week | Workstream | Deliverable | Owner | Dependencies |
|---|---|---|---|---|
| 17-19 | OLAP Split | Analytical store deployed (ClickHouse or TimescaleDB); CDC pipeline operational | 1 SRE + 1 Data eng | Kafka/CDC infrastructure |
| 17-20 | Migration: All Teams | Remaining feature teams migrated to shared capabilities | Platform team + all feature teams | Stable v1 services |
| 18-20 | Dashboard Queries | Analytical dashboard queries routed to OLAP store | Backend + Platform | OLAP store populated |
| 19-22 | Data Archival | Automated archival pipeline moving cold data to object storage | 1 SRE | Archival policy approved |
| 20-22 | Load Testing | Comprehensive load test at 5x current traffic | SRE team | Staging environment at scale |
| 21-23 | Legacy Cleanup | Remove deprecated export/filter/authz implementations | Feature teams | All migrations complete |
| 22-24 | Operational Runbooks | Runbooks for all platform services; on-call rotation established | Platform + SRE | Service stability |
| 24 | SLO Review | Formal SLO review; adjust targets based on 3 months of data | Engineering leadership | SLO data |

**Phase 3 Success Criteria**:
- System handles 5x current traffic in load tests with SLOs met
- All feature teams consuming shared capabilities (zero legacy export/filter/authz code)
- OLAP store handling 100% of analytical queries
- Database primary stable at <600 GB with archival active
- Error budget healthy across all tiers
- On-call rotation staffed and runbooks complete

### 4.5 Staffing Summary

| Role | Phase 1 | Phase 2 | Phase 3 | Notes |
|---|---|---|---|---|
| Platform Engineers | 0 → 3 | 3-4 | 3-4 | Core platform team |
| SRE | 2 | 2 | 2 | DB scaling, infrastructure |
| Backend (borrowed from feature teams) | 1-2 | 1 | 0 | Migration support |
| Data Engineer | 0 | 0 | 1 | OLAP pipeline |
| **Total dedicated** | **3-5** | **6-7** | **6-7** | ~12-14% of 50 engineers |

### 4.6 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Database outage before scaling completes | Medium | Critical | Prioritize read replicas and connection pooling in Phase 1 |
| Feature teams resist adopting shared capabilities | Medium | High | Executive sponsorship; demonstrate time savings; make migration easy with SDKs |
| Platform team understaffed due to competing priorities | High | High | Dedicated headcount commitment from leadership; protect from feature work |
| Shared service becomes bottleneck/single point of failure | Medium | High | Design for high availability from day 1; circuit breakers; graceful degradation |
| OLAP migration introduces data inconsistencies | Medium | Medium | Dual-write validation period; automated reconciliation checks |
| 5x traffic arrives sooner than expected | Low | Critical | Phase 1 quick wins provide 2-3x headroom; can accelerate Phase 2 |

### 4.7 Key Decision Points

1. **Week 4**: Finalize analytical store choice (ClickHouse vs. TimescaleDB vs. managed service)
2. **Week 8**: Decide on authorization model (RBAC vs. ABAC vs. hybrid) based on catalog findings
3. **Week 12**: Evaluate whether Citus sharding is needed based on partitioning + OLAP split results
4. **Week 16**: Go/no-go on Phase 3 timeline based on Phase 2 migration velocity
5. **Week 20**: Assess whether SLO targets need adjustment based on real-world data

---

## 5. Summary of Expected Outcomes

| Metric | Today | After 6 Months |
|---|---|---|
| Duplicate export implementations | 4-6 | 1 (shared service) |
| Duplicate filter implementations | 5+ | 1 (shared library) |
| Permission check consistency | Ad hoc, inconsistent | Centralized, auditable |
| Database size (primary) | 500 GB, growing | <600 GB (with archival) |
| API latency (p95) | Degrading (>500ms) | <200ms transactional |
| Traffic capacity | ~1x (at limit) | 5-10x headroom |
| Availability SLO | Unmeasured | 99.9% measured and tracked |
| Engineering time on redundant infra work | ~15-20% | <5% |
| Time to add export to new feature | 2-3 weeks | 1-2 days (SDK integration) |

---

*This plan should be reviewed with engineering leadership, SRE, and feature team leads before execution begins. Priorities may shift based on the query audit findings in Week 1-2 and the capability catalog in Week 2-4.*
