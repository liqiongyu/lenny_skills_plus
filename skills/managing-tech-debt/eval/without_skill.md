# Tech Debt Management Plan: checkout-service

## 1. Executive Summary

The `checkout-service` (Node.js + PostgreSQL) is experiencing weekly incidents caused by timeouts and slow release cycles. This plan provides a structured approach to identifying, prioritizing, and resolving the most impactful technical debt items over an 8-week period with 2 engineers, while accounting for high on-call load.

---

## 2. Tech Debt Register

Below is a prioritized register of likely tech debt items based on the reported symptoms (weekly timeout incidents, slow releases, high on-call burden).

| # | Debt Item | Category | Severity | Effort | Priority |
|---|-----------|----------|----------|--------|----------|
| 1 | Missing or insufficient database query indexing | Performance | High | Medium | P0 |
| 2 | No connection pooling or misconfigured pool settings | Performance | High | Low | P0 |
| 3 | Missing request timeouts and circuit breakers | Reliability | High | Medium | P0 |
| 4 | No automated test suite (unit/integration) | Quality | High | High | P1 |
| 5 | Manual deployment process / lack of CI/CD pipeline | Velocity | High | Medium | P1 |
| 6 | Missing health checks and readiness probes | Observability | Medium | Low | P1 |
| 7 | No structured logging or distributed tracing | Observability | Medium | Medium | P1 |
| 8 | N+1 query patterns in checkout flow | Performance | Medium | Medium | P2 |
| 9 | Lack of database migration tooling | Velocity | Medium | Low | P2 |
| 10 | Missing retry logic with exponential backoff | Reliability | Medium | Low | P2 |
| 11 | Monolithic route handlers (no service layer separation) | Maintainability | Medium | High | P2 |
| 12 | Outdated Node.js version and dependencies | Security | Medium | Medium | P3 |
| 13 | No API documentation or schema validation | Quality | Low | Medium | P3 |
| 14 | Hard-coded configuration values | Maintainability | Low | Low | P3 |
| 15 | Missing graceful shutdown handling | Reliability | Low | Low | P3 |

---

## 3. Prioritization Rationale

Items were prioritized using the following criteria:

- **Impact on incidents**: Does fixing this directly reduce weekly timeout incidents?
- **Impact on velocity**: Does fixing this speed up releases?
- **Effort vs. return**: Is the fix achievable within the constrained capacity?
- **On-call relief**: Does this reduce the on-call burden for the 2 engineers?

**P0** items directly address the root causes of timeout incidents. **P1** items improve release velocity and observability. **P2** and **P3** items are important but can be deferred beyond the 8-week window if needed.

---

## 4. Capacity Planning

**Available capacity:**
- 2 engineers x 8 weeks = 16 engineer-weeks total
- On-call overhead estimate: ~25% (high on-call load) = -4 engineer-weeks
- **Effective capacity: ~12 engineer-weeks**

**Allocation:**
- Milestone 1 (Weeks 1-3): ~4.5 engineer-weeks
- Milestone 2 (Weeks 4-6): ~4.5 engineer-weeks
- Milestone 3 (Weeks 7-8): ~3 engineer-weeks

---

## 5. Milestones

### Milestone 1: Stop the Bleeding (Weeks 1-3)

**Goal:** Reduce weekly timeout incidents by 80% and stabilize the service.

**Focus:** P0 items — database performance and timeout handling.

| Task | Owner | Week | Effort | Done Criteria |
|------|-------|------|--------|---------------|
| Audit and add missing database indexes on checkout-related tables | Eng 1 | 1 | 3 days | Slow query log shows no queries > 500ms on core checkout path |
| Review and tune PG connection pool settings (pool size, idle timeout, max connections) | Eng 2 | 1 | 2 days | Connection pool metrics visible; no connection exhaustion errors |
| Add request-level timeouts to all downstream calls (DB, external APIs) | Eng 1 | 2 | 3 days | All outbound calls have explicit timeouts; no hanging requests |
| Implement circuit breaker pattern for external service calls | Eng 2 | 2 | 3 days | Circuit breaker trips after 5 failures; fallback responses served |
| Add basic alerting on error rates and p99 latency | Eng 1 | 3 | 2 days | PagerDuty alerts fire when p99 > 2s or error rate > 5% |
| Load test checkout flow and validate fixes | Eng 2 | 3 | 2 days | Checkout flow handles 2x current peak without timeouts |

**Success Metrics:**
- Timeout incidents reduced from ~1/week to ≤1/month
- p99 latency for checkout endpoint < 2 seconds
- Zero connection pool exhaustion events

---

### Milestone 2: Accelerate Releases (Weeks 4-6)

**Goal:** Cut release cycle time in half and improve confidence in deployments.

**Focus:** P1 items — CI/CD, testing, observability.

| Task | Owner | Week | Effort | Done Criteria |
|------|-------|------|--------|---------------|
| Set up CI pipeline (lint, build, basic smoke tests) | Eng 1 | 4 | 3 days | Every PR triggers automated checks; merge blocked on failure |
| Write integration tests for core checkout flow (happy path + top 3 failure modes) | Eng 2 | 4-5 | 5 days | Checkout flow has ≥70% code coverage on critical path |
| Set up CD pipeline with staged rollout (canary or blue-green) | Eng 1 | 5 | 3 days | One-click deploy to staging; automated promotion to production |
| Add health check and readiness endpoints | Eng 2 | 5 | 1 day | `/health` and `/ready` endpoints respond; orchestrator uses them |
| Implement structured JSON logging with request correlation IDs | Eng 1 | 6 | 3 days | All log entries include correlation ID; logs queryable in log aggregator |
| Add key business metrics dashboard (checkout success rate, latency percentiles, error breakdown) | Eng 2 | 6 | 2 days | Dashboard visible to team; reviewed in weekly standup |

**Success Metrics:**
- Release frequency increases from (estimated) biweekly to multiple times per week
- Time from merge to production < 1 hour
- Mean time to detect (MTTD) incidents < 5 minutes via alerting/dashboards

---

### Milestone 3: Harden and Reduce Toil (Weeks 7-8)

**Goal:** Reduce on-call burden and set the foundation for ongoing maintainability.

**Focus:** P2 items — query optimization, retry logic, migration tooling, on-call improvements.

| Task | Owner | Week | Effort | Done Criteria |
|------|-------|------|--------|---------------|
| Identify and fix top 3 N+1 query patterns in checkout flow | Eng 1 | 7 | 3 days | Identified queries replaced with batch/join queries; verified via query logs |
| Add retry logic with exponential backoff for transient failures | Eng 2 | 7 | 2 days | External call failures retry up to 3x; no retry storms observed |
| Set up database migration tooling (e.g., node-pg-migrate or similar) | Eng 2 | 7 | 1 day | Migrations run via CLI; tracked in version control |
| Create runbooks for top 3 incident types | Eng 1 | 8 | 2 days | Runbooks linked in PagerDuty; on-call engineer can follow step-by-step |
| Implement graceful shutdown handling | Eng 2 | 8 | 1 day | In-flight requests complete before process exits; zero dropped requests during deploy |
| Conduct retrospective and update tech debt register for next quarter | Both | 8 | 0.5 day | Updated register with remaining items, new items, and revised priorities |

**Success Metrics:**
- On-call pages reduced by 50% compared to pre-plan baseline
- Database query count per checkout request reduced by 30%+
- All deploys are zero-downtime

---

## 6. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| On-call interruptions consume more than 25% capacity | High | Plan slips by 1-2 weeks | Milestone 1 fixes should reduce on-call load, freeing capacity for later milestones. If needed, descope Milestone 3 to P2 items only. |
| Database index changes cause unexpected locking | Medium | Brief production impact | Run index creation with `CONCURRENTLY` option; schedule during low-traffic windows. |
| Circuit breaker tuning causes false positives | Medium | Degraded checkout experience | Start with conservative thresholds; tune based on production traffic data. |
| Engineers pulled to other projects | Medium | Milestone delays | Secure explicit management commitment for 8-week allocation before starting. |

---

## 7. Governance

- **Weekly check-in** (30 min): Review progress against milestone, adjust priorities if needed.
- **Incident correlation**: After each on-call incident, tag whether it maps to a register item. This validates priorities.
- **Milestone demo**: At the end of each milestone, demonstrate improvements with before/after metrics.
- **Register hygiene**: Add new debt items as discovered; re-prioritize at each milestone boundary.

---

## 8. Definition of Done (Plan-Level)

After 8 weeks, the plan is considered successful if:

1. Weekly timeout incidents reduced by ≥80%
2. Release cycle time reduced by ≥50%
3. On-call pages reduced by ≥50%
4. Core checkout flow has automated test coverage
5. CI/CD pipeline enables same-day releases
6. Observability stack provides < 5 minute incident detection
