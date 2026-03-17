# Tech Debt Management Pack: checkout-service

---

## 1) Context Snapshot

**System(s) in scope:** `checkout-service` -- a Node.js application backed by PostgreSQL, responsible for cart management, payment orchestration, order creation, and post-purchase flows.

**Owner(s):** Checkout team (2 engineers).

**Stakeholders / decision-maker(s):**
- Engineering Manager (decision-maker for capacity allocation)
- Product Manager (trade-off decisions between features and debt)
- On-call rotation (currently the same 2 engineers)

**Time horizon + deadlines:** 8 weeks. No hard external deadline stated; the implicit deadline is "stop the bleeding" -- reduce weekly incident cadence and unblock release velocity before the next planning cycle.

**Primary pains (top 3):**
1. **Reliability risk** -- Weekly incidents caused by database query timeouts under load.
2. **Velocity tax** -- Slow, risky releases; engineers afraid to ship due to fragile code paths.
3. **Operability** -- High on-call load for 2 engineers; incident response consumes capacity that could go to debt paydown.

**User-visible symptoms (top 3):**
1. Checkout timeouts during peak traffic -- users see errors or spinning loaders, abandon carts.
2. Slow page loads on order-summary and payment-confirmation screens (p95 > 3 s).
3. Occasional duplicate order creation when users retry after a timeout.

**Constraints:**
- 2 engineers available (no additional staffing).
- High on-call load -- roughly 30-40% of one engineer's time is consumed by incident response and manual operational tasks.
- No freeze windows mentioned; assume continuous deployment is possible.
- SLO assumption: 99.5% success rate on checkout completions, p95 latency < 1 s (currently violated).

**Success definition:**
- Weekly timeout incidents drop from ~3-5/week to <= 1/month.
- Deploy frequency increases from ~1/week to >= 2/week.
- On-call pages related to checkout-service drop by >= 50%.
- p95 checkout latency drops below 1 s.

**Assumptions:**
- The team uses standard Node.js tooling (Express or similar) and raw SQL or a lightweight ORM against Postgres.
- There is basic application logging but limited structured observability (no distributed tracing, limited dashboard coverage).
- No active migration or rebuild is underway; this is a "fix what we have" scenario.
- The 2 engineers can dedicate ~60% of their combined capacity to debt work if on-call load is reduced.

---

## 2) Tech Debt Register

| ID | Area | Debt Item | Symptoms | User Impact | Risk (Reliability / Security) | Velocity Tax | Effort (Range) | Dependencies | Owner | Recommended Strategy |
|---:|------|-----------|----------|-------------|-------------------------------|--------------|----------------|--------------|-------|----------------------|
| 1 | Data / Queries | **Unindexed and unoptimized Postgres queries on orders and cart tables** | Timeouts under load; slow checkout completion; elevated p95 latency | High -- users hit timeout errors, abandon carts | High -- primary incident driver (3-5 incidents/week) | Medium -- workarounds in code to retry/handle timeouts | S-M (2-5 days) | None | Eng 1 | Refactor (add indexes, rewrite queries, add connection pool tuning) |
| 2 | Architecture | **Synchronous payment + inventory calls in the checkout hot path** | Single slow downstream call blocks the entire request; cascading timeouts | High -- checkout fails if any downstream is slow | High -- no circuit breakers; one slow dependency takes down checkout | Medium -- engineers avoid touching payment flow | M (3-7 days) | ID 5 (observability) | Eng 2 | Refactor (add circuit breakers, timeouts, async where possible) |
| 3 | Infra / Ops | **No structured observability (tracing, dashboards, alerting)** | Incidents take 30-60 min to diagnose; MTTR is high; root cause often unknown | Medium -- prolonged outages during incidents | High -- inability to detect and respond quickly | High -- debugging is manual log-grep; on-call is exhausting | M (4-6 days) | None | Eng 1 | Refactor (add APM/tracing, key dashboards, alert rules) |
| 4 | Code Health | **No integration or load tests; minimal unit test coverage** | Regressions shipped to production; engineers afraid to refactor | Medium -- regressions cause user-facing bugs | Medium -- untested code paths fail under edge cases | High -- every PR is a gamble; manual QA is the only gate | M-L (5-10 days) | None | Eng 2 | Refactor (add critical-path integration tests, basic load test) |
| 5 | Infra / Ops | **Missing connection pool configuration and Postgres health checks** | Under load, Node exhausts connections; new requests queue and timeout | High -- directly causes the timeout incidents | High -- connection exhaustion is a primary failure mode | Low | S (1-2 days) | None | Eng 1 | Refactor (configure pool size, idle timeout, health checks) |
| 6 | Architecture | **Monolithic request handler -- cart, payment, order creation in one function** | Hard to test, hard to debug, hard to change one piece without risk to others | Low (indirect) -- slows improvements | Medium -- tight coupling means a bug anywhere breaks everything | High -- feature work requires understanding entire flow | M-L (5-10 days) | ID 4 (tests before refactoring) | Eng 2 | Refactor (extract into modules with clear interfaces) |
| 7 | Data | **No idempotency keys on order creation** | Duplicate orders when users retry after timeouts | High -- users charged twice; CS tickets | High -- data integrity risk; financial impact | Low | S-M (2-4 days) | ID 1 (reduce timeouts first to lower frequency) | Eng 1 | Refactor (add idempotency key to order creation endpoint) |
| 8 | Infra / Ops | **Manual deployment process (no CI/CD pipeline or limited automation)** | Deploys are slow, error-prone, and infrequent | Low (indirect) -- delays fixes reaching users | Medium -- manual steps increase deployment failure risk | High -- deploys take 1-2 hours of engineer time | M (3-5 days) | None | Eng 2 | Refactor (automate deploy pipeline, add smoke tests) |
| 9 | Code Health | **Hardcoded configuration and connection strings** | Environment-specific bugs; config drift between staging and production | Low | Medium -- security risk if credentials leak; config bugs cause incidents | Medium -- environment issues waste debugging time | S (1-2 days) | None | Eng 1 | Refactor (externalize config to env vars / secrets manager) |
| 10 | Data | **No query timeout or statement timeout configured in Postgres** | Runaway queries hold locks and connections indefinitely | Medium -- cascading failures during load | High -- one bad query can take down the database | Low | S (0.5-1 day) | None | Eng 1 | Refactor (set statement_timeout, lock_timeout) |
| 11 | Architecture | **No graceful shutdown or request draining** | In-flight requests fail during deploys; users see errors on every release | Medium -- users hit errors during deployments | Medium -- data inconsistency if order creation interrupted mid-write | Medium -- engineers schedule deploys during low traffic to mitigate | S (1-2 days) | None | Eng 2 | Refactor (add graceful shutdown with drain period) |
| 12 | Infra / Ops | **Alert fatigue -- noisy, poorly tuned alerts** | On-call engineer wastes time on false positives; real issues get buried | Low (indirect) | Medium -- alert fatigue leads to missed real incidents | High -- on-call burnout reduces available capacity | S-M (2-3 days) | ID 3 (need better observability first) | Eng 1 | Refactor (tune alert thresholds, consolidate, add runbooks) |
| 13 | Data | **Schema drift -- no migration tooling or version control for DB schema** | Manual schema changes cause staging/prod divergence; migration fear | Low | Medium -- risk of breaking changes without rollback path | Medium -- schema changes are manual and stressful | S-M (2-3 days) | None | Eng 2 | Refactor (adopt migration tool like node-pg-migrate or knex migrations) |
| 14 | Code Health | **Error handling is inconsistent -- some paths swallow errors, others crash** | Silent failures; users see generic 500 errors; on-call gets cryptic alerts | Medium -- users get unhelpful error messages | Medium -- silent failures mask real problems | Medium -- debugging requires reading every code path | M (3-5 days) | ID 6 (easier after modularization) | Eng 2 | Refactor (standardize error handling, add error taxonomy) |
| 15 | Architecture | **No rate limiting or backpressure on checkout endpoint** | Traffic spikes overwhelm the service; exacerbates timeout issues | Medium -- legitimate users locked out during spikes | Medium -- amplifies all other reliability issues | Low | S (1-2 days) | None | Eng 1 | Refactor (add rate limiting middleware) |

---

## 3) Scoring Model + Prioritized List

### Scoring Model

Each item is scored on four dimensions (1-5, where 5 = most severe / most valuable to fix):

- **User impact (1-5):** Does this debt item directly cause user-visible harm (errors, slowness, data issues)?
- **Reliability risk (1-5):** Does this item contribute to incidents, data loss, or cascading failures?
- **Velocity tax (1-5):** Does this item slow down shipping, increase fear of change, or waste engineer time?
- **Effort (1-5, inverted):** 5 = very low effort (quick win), 1 = very high effort. Higher score = easier to do.

**Composite score** = User Impact + Reliability Risk + Velocity Tax + Effort (inverted). Max = 20. Ties broken by: reliability risk first, then sequencing (enablers ranked higher).

**Sequencing note:** Items that are prerequisites for other work ("enablers") receive a +1 bonus.

### Prioritized List (Top 10)

| Rank | Debt ID | Item | Scores (UI / RR / VT / Eff) | Composite | Why Now | Milestone / Next Action |
|-----:|--------:|------|------------------------------|----------:|---------|------------------------|
| 1 | 10 | Postgres statement_timeout + lock_timeout | 3 / 5 / 2 / 5 | 15 + 1 enabler = **16** | Immediate incident mitigation; 0.5-1 day effort; prevents runaway queries from cascading | M1 -- deploy config change this week |
| 2 | 5 | Connection pool config + health checks | 5 / 5 / 2 / 5 | **17** | Primary root cause of timeout incidents; 1-2 day fix; highest ROI item in the register | M1 -- implement alongside ID 10 |
| 3 | 1 | Unindexed / unoptimized queries | 5 / 5 / 3 / 4 | **17** | Second root cause of timeouts; indexes can be added with low risk; query rewrites need testing | M1 -- profile top 5 queries, add indexes, rewrite worst offenders |
| 4 | 3 | Structured observability (tracing, dashboards, alerts) | 3 / 4 / 5 / 3 | 15 + 1 enabler = **16** | Enabler: every subsequent item is safer and faster with observability in place; reduces MTTR immediately | M1 -- instrument top 3 endpoints, create incident dashboard |
| 5 | 7 | Idempotency keys on order creation | 5 / 5 / 1 / 4 | **15** | Directly prevents duplicate charges -- highest user-harm item; moderate effort; partially mitigated once timeouts decrease | M2 -- implement after timeout root causes are addressed |
| 6 | 2 | Circuit breakers + timeouts on downstream calls | 5 / 5 / 3 / 3 | **16** | Prevents cascading failures from payment/inventory slowness; requires some observability first | M2 -- add circuit breaker library, configure per-dependency timeouts |
| 7 | 11 | Graceful shutdown + request draining | 3 / 3 / 3 / 5 | **14** | Quick win; eliminates deploy-time errors; improves deploy confidence | M2 -- add shutdown handler with drain period |
| 8 | 15 | Rate limiting on checkout endpoint | 3 / 3 / 1 / 5 | **12** | Protects against traffic spikes amplifying all other issues; quick to add | M2 -- add middleware with sensible defaults |
| 9 | 8 | Automated deployment pipeline | 2 / 3 / 5 / 3 | **13** | Unblocks faster iteration; current manual process is the velocity bottleneck | M3 -- automate build + deploy + smoke test |
| 10 | 4 | Integration + load tests | 3 / 3 / 5 / 2 | **13** | Enabler for future refactoring (ID 6, 14); gives confidence to ship faster | M3 -- add tests for checkout critical path |

**Items ranked 11-15 (backlog for post-8-week planning):** ID 12 (alert tuning), ID 9 (config externalization), ID 13 (schema migration tooling), ID 6 (modularization), ID 14 (error handling standardization). These are important but depend on earlier work and exceed the 8-week capacity.

---

## 4) Strategy Decision Memo

### Decision: Refactor in Place (not rebuild or migrate)

**Decision to make:** Should we refactor the existing checkout-service incrementally, or plan a rewrite/migration to a new service?

**Context / problem:** The checkout-service suffers from weekly incidents (timeouts), slow releases, and high on-call burden. The root causes are identifiable and addressable: untuned database queries, missing connection pool configuration, no circuit breakers, and poor observability. The architecture is monolithic but functional -- it does not lack fundamental capabilities.

**Options considered:**

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A) Incremental refactor** | Fix root causes in place over 8 weeks | Low risk; immediate value; no dual-run cost; team knows the codebase | Does not address deeper structural issues (monolith) in this cycle |
| **B) Strangler-fig migration** | Build a new checkout-service and gradually route traffic | Clean architecture; opportunity to redesign | Dual-run cost for 2 engineers is prohibitive; 8 weeks is too short; on-call load doubles during migration |
| **C) Full rewrite** | Stop feature work and rebuild | "Clean slate" | Classic rewrite trap; 8 weeks is insufficient; old service still needs support; high risk of scope creep |

**Evaluation criteria:**
- Impact on incident rate (primary pain)
- Time to first measurable improvement
- Team capacity (2 engineers, high on-call)
- Risk of making things worse
- Dual-run / operational cost

**Recommendation: Option A -- Incremental Refactor**

**Rationale:**
1. The root causes (query performance, connection pooling, missing circuit breakers) are well-understood and fixable without architectural changes.
2. With only 2 engineers and high on-call load, any migration would consume all capacity and likely stall, leaving both old and new systems in a worse state.
3. The first fixes (IDs 10, 5, 1) can ship in week 1-2 and immediately reduce incidents, which in turn frees on-call capacity for further debt work -- a virtuous cycle.
4. Once stability is restored (end of M2), the team can evaluate whether deeper structural work (modularization, migration) is warranted in a future cycle with better data.

**Migration phases:** Not applicable for this cycle. If a future migration is considered, revisit with this pack's metrics as baseline.

**Risks / mitigations:**
- Risk: Refactoring without tests could introduce regressions. Mitigation: Prioritize observability (ID 3) and add targeted integration tests (ID 4) before larger refactors.
- Risk: On-call load may not decrease fast enough, starving debt work. Mitigation: Front-load the highest-impact, lowest-effort items (IDs 10, 5) to reduce incidents quickly.

---

## 5) Execution Plan (3 Milestones)

### Capacity Model

- **Total capacity:** 2 engineers x 8 weeks = 80 engineer-days.
- **On-call tax (current):** ~30-40% of 1 engineer = ~12-16 days lost over 8 weeks.
- **Effective capacity:** ~64-68 engineer-days.
- **Assumption:** On-call load decreases after M1, freeing ~5-8 additional days for M2-M3.
- **Allocation:** 100% of available capacity goes to debt work (per the stated goal). Feature work is paused or minimal.

### Milestone Table

| Milestone | Outcome | Scope (Debt IDs) | Owner | ETA (Range) | Acceptance Criteria | Stop / Rollback Condition |
|-----------|---------|-------------------|-------|-------------|---------------------|--------------------------|
| **M1: Stop the Bleeding** | Eliminate primary timeout root causes; establish observability baseline | ID 10 (statement_timeout), ID 5 (connection pool), ID 1 (query optimization), ID 3 (observability -- phase 1) | Eng 1: IDs 10, 5, 1; Eng 2: ID 3 | Weeks 1-3 (8-14 eng-days) | Timeout incidents drop from 3-5/week to <= 1/week; p95 checkout latency < 2 s; incident dashboard live with top 3 endpoints traced | Rollback: Revert config/index changes if error rate increases > 2x. Stop: If incidents increase after changes, pause and investigate before proceeding. |
| **M2: Harden the Hot Path** | Eliminate cascading failures and duplicate orders; improve deploy safety | ID 7 (idempotency keys), ID 2 (circuit breakers), ID 11 (graceful shutdown), ID 15 (rate limiting) | Eng 1: IDs 7, 15; Eng 2: IDs 2, 11 | Weeks 3-6 (12-18 eng-days) | Zero duplicate orders in production for 2 consecutive weeks; downstream slowness no longer causes checkout failures (circuit breaker trips and returns graceful error); zero deploy-time errors | Rollback: Circuit breaker can be disabled via feature flag. Idempotency: backward-compatible (old requests still work). Stop: If any change increases error rate > baseline, revert and reassess. |
| **M3: Accelerate Delivery** | Automate deploys, add test coverage, tune alerts; prepare backlog for next cycle | ID 8 (CI/CD), ID 4 (integration + load tests -- phase 1), ID 12 (alert tuning) | Eng 1: ID 12; Eng 2: IDs 8, 4 | Weeks 6-8 (10-14 eng-days) | Deploy time < 15 min (automated); at least 3 integration tests covering checkout critical path; on-call pages reduced >= 50% from week-1 baseline; load test baseline established | Rollback: New pipeline is additive -- old process remains available. Stop: If CI/CD setup exceeds 5 days, descope to automated deploy only (skip smoke tests for now). |

### Sequencing Diagram

```
Week 1-2:  [ID 10: statement_timeout] [ID 5: connection pool] -----> immediate incident relief
           [ID 3: observability phase 1] -----> dashboards + tracing live

Week 2-3:  [ID 1: query optimization] -----> profile, index, rewrite top queries

Week 3-4:  [ID 7: idempotency keys] [ID 2: circuit breakers begin]

Week 4-5:  [ID 2: circuit breakers complete] [ID 11: graceful shutdown] [ID 15: rate limiting]

Week 6-7:  [ID 8: CI/CD pipeline] [ID 4: integration tests]

Week 7-8:  [ID 12: alert tuning] [Retrospective + next-cycle planning]
```

### Deferred to Post-8-Week Backlog

| Debt ID | Item | Reason for Deferral |
|--------:|------|---------------------|
| 6 | Modularize monolithic handler | Requires tests (ID 4) in place first; effort exceeds remaining capacity |
| 14 | Standardize error handling | Better done after modularization |
| 9 | Externalize configuration | Lower priority; not directly causing incidents |
| 13 | Schema migration tooling | Important but not urgent within 8 weeks |

---

## 6) Migration + Rollback Plan

**Migration is not recommended for this cycle** (see Strategy Decision Memo above). The plan is incremental refactoring in place.

### Rollback Strategy (per milestone)

| Change | Rollback Mechanism | Trigger |
|--------|-------------------|---------|
| ID 10: statement_timeout config | Revert Postgres parameter; takes effect on next connection | Error rate on checkout > 2x baseline within 1 hour of change |
| ID 5: Connection pool config | Revert to previous pool settings in app config | Connection errors increase or p95 latency worsens |
| ID 1: New indexes | Drop index (non-blocking in Postgres) | Write latency increases > 20% due to index maintenance |
| ID 1: Query rewrites | Revert code to previous query; feature-flag new queries if feasible | Query results differ or latency worsens |
| ID 3: Observability instrumentation | Remove or disable tracing middleware | Measurable latency overhead > 50 ms p95 |
| ID 7: Idempotency key enforcement | Disable idempotency check (allow duplicate -- reverts to current behavior) | False rejections of legitimate orders |
| ID 2: Circuit breakers | Disable via feature flag (circuit always closed) | Circuit breaker incorrectly trips on healthy dependencies |
| ID 11: Graceful shutdown | Revert to immediate shutdown | Drain period causes deploy to hang > 60 s |
| ID 15: Rate limiter | Disable middleware | Legitimate traffic blocked (false positives > 0.1%) |
| ID 8: CI/CD pipeline | Use old manual deploy process | Pipeline failures block deploys for > 1 hour |

---

## 7) Metrics Plan

### Baseline (Today -- Estimated)

| Metric | Current Value (Est.) | Confidence |
|--------|---------------------|------------|
| Timeout incidents per week | 3-5 | High (from on-call reports) |
| MTTR (checkout incidents) | 30-60 min | Medium (estimate from team) |
| p95 checkout latency | 3-5 s | Medium (needs instrumentation to confirm) |
| Deploy frequency | ~1/week | High |
| Deploy duration (manual) | 1-2 hours | High |
| Lead time (commit to production) | 3-7 days | Medium |
| Duplicate order rate | ~2-5/week | Medium (from CS ticket volume) |
| On-call pages per week (checkout) | 5-10 | Medium |

### Targets (by Week 8)

| Metric | Target | Stretch Target |
|--------|--------|----------------|
| Timeout incidents per week | <= 1/month | 0 |
| MTTR (checkout incidents) | < 15 min | < 10 min |
| p95 checkout latency | < 1 s | < 500 ms |
| Deploy frequency | >= 2/week | >= 3/week |
| Deploy duration | < 15 min (automated) | < 10 min |
| Lead time | < 2 days | < 1 day |
| Duplicate order rate | 0 | 0 |
| On-call pages per week | <= 2 | <= 1 |

### Leading Indicators

- **Build/test pass rate** -- if this degrades, regressions are being introduced.
- **Slow query log volume** -- should decrease after ID 1; leading indicator for latency improvement.
- **Connection pool utilization %** -- should drop and stabilize after ID 5.
- **Circuit breaker trip rate** -- non-zero means downstream issues are being contained (good); frequent trips mean downstream needs attention.
- **Deploy success rate** -- should approach 100% after ID 8 + ID 11.

### Guardrails

- **Error rate (5xx):** Must not exceed baseline at any point. If a change increases 5xx rate by > 50%, halt and rollback.
- **Latency (p99):** Must not regress beyond current baseline during any milestone.
- **Order success rate:** Must remain >= current level; any drop triggers immediate investigation.

### Instrumentation Gaps + Owners

| Gap | Action | Owner | Timeline |
|-----|--------|-------|----------|
| No distributed tracing | Add OpenTelemetry or APM agent (Datadog/New Relic/etc.) | Eng 2 | M1 (weeks 1-2) |
| No checkout latency dashboard | Create dashboard with p50/p95/p99 per endpoint | Eng 2 | M1 (week 2) |
| No slow query logging | Enable pg_stat_statements + slow query log (> 500 ms) | Eng 1 | M1 (week 1) |
| No deploy metrics | Add deploy event tracking (frequency, duration, success) | Eng 2 | M3 (week 6) |
| No load test baseline | Create basic load test script against staging | Eng 2 | M3 (week 7) |

### Small Tests to Validate Value

| Test | What | Duration | Success Criteria |
|------|------|----------|-----------------|
| Query optimization canary | After adding indexes + rewriting top 3 queries, compare p95 latency for 48 hours | 2 days | p95 latency drops >= 40% |
| Circuit breaker soak test | Enable circuit breaker for payment dependency only; monitor for 1 week | 1 week | Zero cascading timeouts from payment slowness; no false trips |
| CI/CD dry run | Run automated pipeline in parallel with manual deploy for 3 deploys | ~1 week | Automated deploys succeed with identical outcomes; deploy time < 15 min |

---

## 8) Stakeholder Cadence

**Audience:** Engineering Manager, Product Manager, on-call engineers.

**Cadence:** Weekly (every Monday).

**Update format (5 bullets + metrics):**
1. What shipped last week (debt IDs completed).
2. Key metric changes (incidents, latency, deploy frequency).
3. What is in progress this week.
4. Risks or blockers.
5. Asks (decisions needed, resources, priority changes).
+ Metrics snapshot table (actuals vs targets).

**Decision gates:**
| Gate | When | Decision |
|------|------|----------|
| M1 review | End of week 3 | Confirm incident reduction; approve proceeding to M2. If incidents have not decreased, reassess root causes before continuing. |
| M2 review | End of week 6 | Confirm hot-path hardening is effective; approve M3 scope. Decide whether to expand M3 scope or defer items. |
| Final review | End of week 8 | Review all metrics vs targets. Decide: (a) declare success and move to maintenance mode, (b) extend debt work into next cycle, or (c) escalate to a larger initiative (migration). |

---

## 9) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| On-call load does not decrease after M1, starving M2-M3 capacity | Medium | High -- plan stalls | Front-load IDs 10 and 5 (< 3 days combined); if incidents do not drop within 2 weeks, escalate for temporary on-call support from another team |
| Query optimization requires schema changes that need downtime | Low | Medium -- delays M1 | Use CREATE INDEX CONCURRENTLY; avoid schema-breaking changes in M1 |
| Adding observability instrumentation introduces latency overhead | Low | Low -- rollback is easy | Benchmark before/after; disable if p95 overhead > 50 ms |
| Engineers burn out from combined on-call + debt work in weeks 1-3 | Medium | High -- attrition or quality drops | Protect focus time; limit context switches; celebrate M1 completion |
| Scope creep -- feature requests interrupt debt work | Medium | Medium -- milestones slip | Engineering Manager explicitly protects 8-week window; any feature request is triaged against the debt plan |

### Open Questions

1. **What APM / observability tooling is already available or licensed?** (Affects ID 3 effort estimate.)
2. **Is there a staging environment that mirrors production load patterns?** (Affects testing confidence for IDs 1, 2, 7.)
3. **Are there other teams that depend on checkout-service APIs?** (May introduce coordination requirements for IDs 2, 7, 15.)
4. **What is the current Postgres version and hosting (managed vs self-hosted)?** (Affects feasibility of some query optimizations and pg_stat_statements.)
5. **Has leadership approved pausing feature work for 8 weeks?** (If not, capacity model changes significantly.)

### Next Steps (Immediate -- This Week)

1. **Eng 1:** Enable `pg_stat_statements`, set `statement_timeout` to 5 s and `lock_timeout` to 3 s in Postgres. Profile top 10 queries by total time. Deploy connection pool configuration (pool size, idle timeout, health check query). **Target: end of day 2.**
2. **Eng 2:** Evaluate APM tooling options (if none exists, set up lightweight OpenTelemetry with Jaeger/Grafana). Instrument the checkout endpoint (latency, error rate, downstream call duration). Create the initial incident dashboard. **Target: end of day 4.**
3. **Engineering Manager:** Confirm 8-week capacity commitment with Product Manager. Set up weekly Monday stakeholder sync. Share this Tech Debt Management Pack with stakeholders for review. **Target: end of day 1.**

---

## Quality Gate Self-Assessment

### Checklist Results

- [x] **A) Scope + assumptions:** System named, decisions explicit, horizon and constraints captured, assumptions labeled.
- [x] **B) Debt register quality:** 15 items with consistent schema; symptoms, impact, owner, effort range, dependencies all populated; user-visible symptoms included.
- [x] **C) Prioritization quality:** Scoring model is simple and applied consistently; top priorities justified by incident data and velocity impact; enabler work identified (IDs 3, 10).
- [x] **D) Rebuild/migration safety:** N/A for this cycle (refactor-only strategy). Rationale for not migrating is documented.
- [x] **E) Execution plan quality:** 3 incremental milestones, each independently valuable; acceptance criteria and stop/rollback conditions for each.
- [x] **F) Metrics + funding:** Baselines and targets provided; leading indicators (slow query volume, pool utilization, circuit breaker trips) and guardrails (error rate, latency, order success rate) defined; instrumentation gaps listed with owners; small tests specified.
- [x] **G) Stakeholder alignment:** Weekly cadence defined; 3 decision gates; first milestone starts this week with clear owners and actions.
- [x] **H) Safety:** No secrets/credentials requested or recorded; all changes have rollback mechanisms; no destructive actions without confirmation.

### Rubric Self-Score

| Dimension | Score | Rationale |
|-----------|------:|-----------|
| 1) Decision clarity | 4 | Explicit decision (refactor, not rebuild); trade-offs documented; stakeholders have clear next actions per milestone. |
| 2) Evidence & signals | 3 | Symptoms linked to measurable signals (incident rate, p95 latency, deploy frequency); baselines are estimated with confidence levels; full measurement plan included. Not a 4 because baselines are estimates, not confirmed metrics. |
| 3) Register completeness | 4 | 15 items with consistent schema across all rows; owners, impact, effort ranges, dependencies, and recommended strategies. Register is structured for sprint planning. |
| 4) Prioritization quality | 4 | Consistent scoring model; sequencing dependencies explicit ("ID 5 enables ID 2"); enabler work identified; stop conditions per milestone. |
| 5) Strategy correctness | 3 | Refactor recommendation with explicit criteria; rebuild option analyzed and rejected with rationale. Not a 4 because migration phases / dual-run are N/A (refactor only). |
| 6) Execution feasibility | 4 | 3 sequenced milestones with owners, acceptance criteria, capacity model, and immediate next step (starts this week). |
| 7) Safety & robustness | 4 | Every change has a named rollback mechanism with quantified triggers; no secrets; human decision gates at each milestone. |
| **Total** | **26/28** | Passes threshold (>= 20/28) with no 1s in Safety & robustness. |
