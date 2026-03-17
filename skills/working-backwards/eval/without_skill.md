# Working Backwards: Role-Based Dashboard Governance for Enterprise Analytics Platform

---

## Phase 1: Divergent PR/FAQ Options

We begin by generating three distinct product directions, each addressing the core problem -- admins cannot tailor dashboards by role, causing irrelevant data exposure, stalled adoption, and blocked enterprise expansion -- through a different lens.

---

### Option A: Role-Based Default Dashboards

**Concept:** The platform ships a set of admin-configured default dashboards that are automatically assigned to users based on their organizational role (e.g., "Sales Rep," "Finance Lead," "IT Admin"). Admins define role-to-dashboard mappings in a central console. Users land on their role-appropriate dashboard on login and can optionally pin additional dashboards from an approved catalog.

**Strengths:**
- Simple mental model for admins: map role to dashboard, done.
- Fast to implement -- mainly requires a role-assignment layer and a default-dashboard resolver.
- Clear governance story: admins control what each role sees out of the box.

**Weaknesses:**
- Roles are often too coarse. A "Marketing Manager" in EMEA and one in APAC may need very different views.
- No concept of data-level permissions -- a user could still navigate to raw data or build custom queries that exceed their intended scope.
- Doesn't address the governance requirement for least-privilege data access; it only controls the starting screen.
- Scales poorly: large enterprises with 50+ roles create a combinatorial management burden.

**Risk Profile:** Low implementation risk, but moderate strategic risk -- may not satisfy enterprise security reviews and could require a follow-on project for true data-level governance.

---

### Option B: Dashboard Packs by Department

**Concept:** Curated bundles of dashboards ("packs") are created per department -- Sales Pack, Finance Pack, Engineering Pack, etc. Admins assign packs to teams or individuals. Each pack includes pre-built dashboards, relevant KPIs, and templated reports. Packs can be versioned and updated centrally.

**Strengths:**
- Feels like a "product" -- easy to market and easy for admins to understand.
- Versioning and central updates reduce maintenance burden for admins.
- Could be extended to a marketplace model (partner-built packs, industry packs).

**Weaknesses:**
- Departments are not the right abstraction for data governance. A department pack still doesn't enforce what data a user can or cannot see within those dashboards.
- Packs are rigid -- real organizations have cross-functional teams, dotted-line reports, and project-based structures that don't map to neat department boundaries.
- High content creation cost upfront. Each pack requires curation, testing, and ongoing maintenance.
- Still doesn't solve the least-privilege requirement -- a user with the "Sales Pack" could potentially see all sales data across regions, not just their territory.

**Risk Profile:** Medium implementation risk (content creation, versioning infrastructure), high strategic risk (doesn't solve governance, may need rework).

---

### Option C: Permissioned Saved Views with Governance Controls

**Concept:** A new permissions model that operates at the *view* level. Admins define data scopes (which datasets, dimensions, and metric ranges a role or group can access), then create or approve "Saved Views" -- pre-configured dashboard states that respect those scopes. Users see only the Saved Views they are authorized for. Users can create personal views, but only within their data scope. Admins get an audit log of who accessed what, when.

**Strengths:**
- Directly addresses least-privilege: data scopes enforce what a user can see, not just what dashboard they land on.
- Flexible: works for role-based, department-based, project-based, or geography-based organizations.
- Audit log and governance console satisfy enterprise security review requirements.
- Saved Views can be shared, promoted to "official" status, or retired -- natural lifecycle management.
- Enables self-service within guardrails, which drives adoption (users feel empowered, not restricted).

**Weaknesses:**
- Most complex to implement: requires a permissions engine, data-scope definitions, view-level access control, and an audit system.
- Admin UX must be carefully designed to avoid overwhelming complexity.
- 8-week beta timeline is aggressive for this scope.

**Risk Profile:** High implementation risk (most engineering work), but low strategic risk (directly solves the stated problem and positions the platform for enterprise growth).

---

## Phase 1 Decision: Option Selection

### Evaluation Matrix

| Criterion                        | Weight | Option A (Role Defaults) | Option B (Dept Packs) | Option C (Permissioned Views) |
|----------------------------------|--------|--------------------------|-----------------------|-------------------------------|
| Solves least-privilege requirement | 30%   | 2/5                      | 1/5                   | 5/5                           |
| Drives adoption post-rollout      | 25%   | 3/5                      | 3/5                   | 4/5                           |
| Enterprise security readiness     | 20%   | 2/5                      | 2/5                   | 5/5                           |
| Implementation feasibility (8 wk) | 15%   | 5/5                      | 3/5                   | 2/5                           |
| Long-term platform leverage       | 10%   | 2/5                      | 3/5                   | 5/5                           |
| **Weighted Score**                |        | **2.55**                 | **2.10**              | **4.20**                      |

**Selected: Option C -- Permissioned Saved Views with Governance Controls**

Option C is the only option that directly addresses the enterprise requirements for least-privilege data access, governance, and audit. While implementation risk is highest, the 8-week beta can be scoped to a viable subset (see backcasting plan). Options A and B both leave a governance gap that would require follow-on work, effectively doubling the total investment.

---

## Phase 2: Full PR/FAQ -- Permissioned Saved Views

---

### PRESS RELEASE

**FOR IMMEDIATE RELEASE**

**[Platform Name] Launches Permissioned Saved Views: Enterprise Admins Can Now Deliver the Right Data to the Right People, Automatically**

*New governance-first dashboard experience drives adoption while enforcing least-privilege data access*

**[City, Date]** -- [Platform Name], the analytics platform trusted by enterprise teams, today announced Permissioned Saved Views, a new capability that lets admins define data scopes and curate dashboard views tailored to every role, team, and geography in their organization -- all while enforcing least-privilege access controls and providing a complete audit trail.

**The Problem**

Enterprise analytics platforms face a paradox: the more data they surface, the harder it becomes for individual users to find what matters. Today, most platforms offer one-size-fits-all dashboards. Admins lack the tools to tailor the experience by role, and security teams lack visibility into who is accessing what data. The result: teams see irrelevant metrics, adoption stalls after initial rollout, and IT cannot pass enterprise security reviews because there is no way to enforce least-privilege data access.

**The Solution**

Permissioned Saved Views introduces three connected capabilities:

1. **Data Scopes.** Admins define named scopes that specify which datasets, dimensions, filters, and metric ranges a group of users can access. For example, a "North America Sales" scope limits a user to revenue data for NA territories only. Scopes are composable -- a regional VP might hold the "NA Sales" scope plus a "Global Forecast" scope.

2. **Saved Views.** Any dashboard state -- filters, date ranges, visible widgets, layout -- can be saved as a named View. Admins can promote Views to "Official" status, making them appear in a curated catalog for authorized users. Users can also create personal Views, but only within the boundaries of their assigned data scopes.

3. **Governance Console.** A single pane of glass for admins to manage scopes, review View access, and inspect a real-time audit log. The console shows who accessed which View, when, and flags anomalies such as a user repeatedly hitting scope boundaries.

**Customer Quote**

"Before Permissioned Saved Views, our department leads complained that the dashboards were either too noisy or missing the metrics they cared about. Our security team blocked the enterprise rollout because we couldn't prove least-privilege access. Now, we set up scopes in minutes, curate official Views per team, and hand security a clean audit log. Adoption jumped from 30% to 78% in the first quarter after rollout." -- *[Composite customer persona], VP of Business Intelligence, [Enterprise Company]*

**How It Works**

- An admin opens the Governance Console and creates a Data Scope called "EMEA Marketing" that includes the marketing dataset filtered to EMEA region, with access to campaign performance, spend, and attribution metrics.
- The admin opens the main dashboard, configures it to show EMEA campaign performance, saves the state as "EMEA Campaign Overview," and marks it as Official.
- The admin assigns the "EMEA Marketing" scope to the EMEA Marketing team group (synced from the company's identity provider via SCIM/SSO).
- EMEA Marketing team members log in and see "EMEA Campaign Overview" as their default View. They can explore further, create personal Views, or request access to additional scopes -- but they cannot see data outside their assigned scopes.
- The security team opens the Governance Console, reviews the audit log, and confirms that no user accessed data outside their scope during the last quarter.

**Availability**

Permissioned Saved Views enters closed beta on [date, 8 weeks from now] for Enterprise plan customers. General availability is planned for [date, ~4 weeks after beta]. Existing customers can request beta access through their account manager.

---

### FREQUENTLY ASKED QUESTIONS

#### Customer / External FAQs

**Q1: What is a Data Scope and how is it different from a dashboard filter?**

A Data Scope is a server-enforced access boundary. Unlike a dashboard filter -- which a user can change or remove -- a Data Scope is set by an admin and cannot be bypassed by the end user. When a user has the "NA Sales" scope, every query they run, every View they open, and every export they create is automatically filtered to North American sales data. There is no way for the user to "unfilter" and see global data unless an admin grants them a broader scope.

**Q2: How do Data Scopes interact with our existing SSO and identity provider?**

Data Scopes are assigned to groups, and groups are synced from your identity provider (IdP) via SCIM or SAML group claims. If you already have groups like "EMEA Marketing" or "NA Sales Reps" in your IdP, you can map Data Scopes directly to those groups. When a user is added or removed from a group in your IdP, their Data Scopes update automatically at next login (or within 15 minutes for active sessions via SCIM push).

**Q3: Can users create their own Views, or is it admin-only?**

Both. Admins can create and promote "Official" Views that appear in a curated catalog for specific groups. Individual users can also create personal "My Views" -- but these are always bounded by the user's assigned Data Scopes. A user cannot create a View that shows data outside their scope. Admins can optionally disable personal View creation for specific groups if stricter control is needed.

**Q4: What happens when a user tries to access data outside their scope?**

The query is automatically filtered to the user's scope. The user does not see an error -- they simply see results within their authorized data. If a user shares a View URL with a colleague who has a different scope, the colleague sees the same dashboard layout but with data filtered to their own scope. The Governance Console logs scope-boundary events for admin review.

**Q5: Does this slow down dashboard performance?**

No. Data Scopes are implemented as query-level filters injected at the data layer, similar to how row-level security works in modern databases. We benchmarked the feature at <50ms additional latency on p99 queries across datasets up to 500M rows. For most customers, the difference is imperceptible.

**Q6: How does the audit log work?**

Every View access, scope change, and admin action is recorded in an immutable audit log accessible from the Governance Console. Logs include: timestamp, user ID, View ID, scope applied, query fingerprint, and result row count. Logs can be exported as CSV or streamed to your SIEM (Splunk, Datadog, etc.) via webhook. Retention is 12 months by default, configurable up to 7 years for compliance.

**Q7: Can we migrate our existing dashboards to Saved Views?**

Yes. Any existing dashboard can be saved as a View in one click. We provide a migration wizard that walks admins through: (1) auditing existing dashboards, (2) defining Data Scopes, (3) converting dashboards to Official Views, and (4) assigning scopes to groups. The wizard estimates the migration at 1-2 hours for a typical deployment with 10-20 dashboards and 5-10 scopes.

**Q8: What is the pricing impact?**

Permissioned Saved Views is included in the Enterprise plan at no additional cost. Data Scopes, Saved Views, and the Governance Console are all part of the Enterprise tier. Audit log SIEM streaming is available as an add-on for customers on the Business plan who want governance features without the full Enterprise package.

#### Internal / Stakeholder FAQs

**Q9: Why did we choose Permissioned Saved Views over simpler approaches like role-based default dashboards?**

We evaluated three options. Role-based defaults and department packs both fail the enterprise security requirement: they control which dashboard a user lands on but do not enforce what data the user can access. Every enterprise prospect in our pipeline (12 accounts, $3.2M combined ARR) has flagged least-privilege data access as a gate to procurement approval. Permissioned Saved Views is the only option that clears that gate. (See Phase 1 evaluation above.)

**Q10: Can we really ship a beta in 8 weeks?**

Yes, with a scoped beta. The beta includes: (1) Data Scopes (single-dimension filtering, e.g., region or department), (2) Saved Views (save/load/share), (3) Governance Console (scope management + basic audit log), and (4) SCIM group sync for scope assignment. Deferred to GA: multi-dimension scopes, SIEM streaming, migration wizard, personal View creation controls, and anomaly detection in the audit log. See the backcasting plan for the detailed week-by-week breakdown.

**Q11: What are the biggest technical risks?**

1. **Query injection layer.** Injecting scope filters into every query path (API, dashboard, export, scheduled reports) without regression is the highest-risk workstream. Mitigation: We will instrument a shadow-mode in weeks 1-3 that logs what the filter *would* have done, before enforcing it in week 4.
2. **Performance.** Scope filters add query complexity. Mitigation: Benchmarking against top-10 customer datasets in weeks 2-3, with a performance budget of <50ms p99 overhead.
3. **SCIM sync latency.** If group changes don't propagate quickly, a removed user might retain access. Mitigation: Session-level scope refresh on each page load (cache for 5 minutes, hard refresh on SCIM push event).

**Q12: What is the adoption metric for success?**

Primary: **Weekly Active View Users (WAVU)** -- the number of unique users who open at least one Saved View per week. Target: 60% of provisioned users within 90 days of rollout at each beta customer. Secondary: **Scope Coverage** -- percentage of users with at least one Data Scope assigned. Target: 90% within 30 days of admin onboarding.

**Q13: How does this affect our existing API?**

All API endpoints that return data will respect Data Scopes. API tokens will be associated with a scope (or set of scopes) configured by the admin. This is a breaking change for API consumers who currently receive unscoped data. We will: (1) communicate the change 4 weeks before GA, (2) provide a migration guide, (3) support a `X-Legacy-Unscoped: true` header for 90 days post-GA that returns unscoped data with a deprecation warning in the response.

**Q14: What about support readiness?**

We will deliver: (1) a support runbook covering the top 20 anticipated issues (scope misconfiguration, View access errors, SCIM sync delays, audit log queries), (2) a 90-minute training session for Tier 1 and Tier 2 support, (3) an internal FAQ seeded from beta customer feedback, and (4) escalation paths to the feature engineering team for weeks 1-4 post-GA.

**Q15: What is the competitive landscape?**

Looker offers row-level security but no curated View concept. Tableau has user filters but governance is fragmented across multiple admin consoles. Power BI has row-level security plus a governance hub, but it is tightly coupled to the Microsoft ecosystem. Our differentiation is the combination of data-level scoping + curated Views + a unified Governance Console in a platform-agnostic product. This positions us to win deals where the customer is multi-cloud or uses a non-Microsoft data stack.

---

## Phase 3: Backcasting Plan -- 8-Week Beta

### Overview

Working backwards from the beta launch date (Week 8), we identify every milestone, dependency, and workstream required. The plan is organized into five parallel tracks:

1. **Permissions & Security** -- Data Scopes engine, query injection, SCIM integration, security review
2. **Product & UX** -- Saved Views UI, Governance Console, admin workflows
3. **Analytics Instrumentation** -- Event tracking, WAVU metric, scope coverage metric
4. **Documentation** -- Admin guides, API migration guide, in-product help
5. **Support Enablement** -- Runbooks, training, escalation paths

---

### Week-by-Week Plan

#### Week 1: Foundation & Design

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | Permissions model design doc: define Scope schema (name, dataset, dimension, filter expression, group assignment). Threat model document. | Security Eng + Backend Lead | None |
| Permissions & Security | SCIM integration design: map IdP groups to Scopes. | Identity Eng | IdP sandbox access |
| Product & UX | Finalize wireframes for: Scope creation wizard, View save/load/share flow, Governance Console (scope list, audit log table). | Product Design | PM sign-off on Option C scope |
| Product & UX | Define beta customer cohort (3-5 Enterprise accounts). Begin outreach. | PM + Account Managers | Sales pipeline data |
| Analytics Instrumentation | Event taxonomy design: define all events (view_opened, scope_applied, scope_boundary_hit, view_created, view_shared, admin_scope_created, admin_scope_assigned, audit_log_queried). | Data/Analytics Eng | Product spec |
| Documentation | Outline admin guide structure. Identify top 20 support scenarios. | Technical Writer | Wireframes |
| Support Enablement | Identify support champions (1 per Tier 1, 1 per Tier 2). Schedule training for Week 6. | Support Lead | None |

#### Week 2: Core Engine -- Shadow Mode

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | Implement Scope storage (DB schema, CRUD API). Scope assignment API (group-to-scope mapping). | Backend Eng | Design doc approved |
| Permissions & Security | Query injection layer v1 (shadow mode): intercept all query paths, log what scope filter *would* apply, but do not enforce. | Backend Eng (query layer) | Scope storage API |
| Permissions & Security | SCIM listener: receive group push events, update scope assignments. | Identity Eng | SCIM design doc |
| Product & UX | Saved View data model: View = (dashboard_id, filter_state, layout_state, name, owner, visibility, official_flag). CRUD API. | Backend Eng | None |
| Analytics Instrumentation | Instrument shadow-mode events: log scope_would_apply and scope_boundary_would_hit events to analytics pipeline. | Data Eng | Shadow mode deployed |
| Documentation | Draft "What are Data Scopes?" conceptual doc. | Technical Writer | Design doc |

#### Week 3: Enforcement & UI Scaffolding

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | Analyze shadow-mode logs from internal dogfooding. Validate that scope filters produce correct results on top-10 customer dataset shapes. | QA + Backend Eng | Shadow mode running for 5+ days |
| Permissions & Security | Performance benchmark: measure p99 latency overhead of scope filter injection on representative queries. Target: <50ms. | Performance Eng | Shadow mode |
| Permissions & Security | Begin security review: share threat model and permissions design with internal security team. Schedule review meeting for Week 5. | Security Lead | Threat model doc |
| Product & UX | Frontend: Scope creation wizard (admin-only). | Frontend Eng | Wireframes + Scope API |
| Product & UX | Frontend: Save View dialog (name, official flag, group visibility). View catalog page (list of Official Views for the user). | Frontend Eng | Wireframes + View API |
| Analytics Instrumentation | Implement WAVU metric pipeline: aggregate view_opened events into weekly active user count. Build internal dashboard. | Data Eng | Event taxonomy live |
| Documentation | Draft "Creating and Managing Data Scopes" step-by-step guide. | Technical Writer | Scope wizard UI |

#### Week 4: Enforcement Go-Live & Governance Console

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | Flip scope enforcement from shadow mode to enforced mode (internal environment first). All queries now filtered by scope. | Backend Eng | Shadow mode validation passed, benchmark passed |
| Permissions & Security | Audit log backend: immutable append-only log of all scope-related events. Query API for Governance Console. | Backend Eng | Event taxonomy |
| Permissions & Security | SCIM end-to-end test: verify group add/remove propagates scope assignment within 15 minutes. | Identity Eng + QA | SCIM listener |
| Product & UX | Frontend: Governance Console v1 -- scope list with assignment counts, basic audit log table (filterable by user, date, scope). | Frontend Eng | Audit log API |
| Product & UX | Frontend: Default View assignment -- admin can set which Official View is the landing page for a scope/group. | Frontend Eng | View catalog |
| Analytics Instrumentation | Implement scope_coverage metric: % of provisioned users with at least one scope assigned. Add to internal dashboard. | Data Eng | Scope assignment API |
| Documentation | Draft "Governance Console Overview" guide. | Technical Writer | Console UI |

#### Week 5: Integration Testing & Security Review

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | **Security review meeting.** Walk through: scope enforcement logic, SCIM sync, audit log integrity, API token scoping, session handling. | Security Team + Engineering | Threat model, code review |
| Permissions & Security | Address security review findings (expected: 3-5 items, budget 2 days of engineering). | Backend Eng | Security review |
| Permissions & Security | API token scoping: admin can assign scopes to API tokens. Unscoped tokens return deprecation warning. | Backend Eng | Scope assignment API |
| Product & UX | End-to-end integration test suite: 30+ scenarios covering scope enforcement, View CRUD, SCIM sync, audit log correctness, cross-scope View sharing. | QA | All features code-complete |
| Product & UX | UX polish pass: loading states, error messages, empty states, scope boundary messaging. | Frontend Eng + Design | Integration testing feedback |
| Analytics Instrumentation | Validate event accuracy: compare analytics events against audit log for consistency. Fix discrepancies. | Data Eng + QA | Both systems live |
| Documentation | Draft API migration guide: explain scoped API behavior, `X-Legacy-Unscoped` header, 90-day deprecation timeline. | Technical Writer | API token scoping |
| Support Enablement | Draft support runbook: top 20 scenarios with diagnosis steps and resolution. | Technical Writer + Support Lead | Integration testing (informs real failure modes) |

#### Week 6: Beta Environment & Support Training

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | Harden: rate limiting on Governance Console APIs. Audit log tamper detection (hash chain). | Security Eng | Security review findings resolved |
| Permissions & Security | Penetration test (internal or contracted): attempt scope bypass via direct API, export, scheduled reports, embedded URLs. | Security Team / External | Enforcement live, API scoping live |
| Product & UX | Deploy to beta environment (isolated staging with production-like data volumes). | DevOps + Backend Eng | All integration tests passing |
| Product & UX | Beta onboarding flow: in-product wizard that walks an admin through creating their first Scope, saving their first Official View, and assigning the scope to a group. | Frontend Eng + Design | Beta environment |
| Analytics Instrumentation | Deploy analytics to beta environment. Verify WAVU and scope_coverage metrics populate correctly. | Data Eng | Beta environment |
| Documentation | Publish admin guide, Governance Console guide, API migration guide to docs site (beta-flagged, accessible only to beta customers). | Technical Writer | All drafts reviewed |
| Support Enablement | **Support training session (90 minutes).** Cover: feature overview, common admin workflows, runbook walkthrough, escalation paths. | PM + Engineering Lead + Support Lead | Runbook complete, beta environment live |
| Support Enablement | Set up dedicated Slack channel for beta support. Engineering on-call rotation for beta period. | Support Lead + Engineering | Training complete |

#### Week 7: Beta Customer Onboarding

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | Monitor penetration test results. Remediate any findings (budget: 2 days). | Security Eng | Pen test complete |
| Product & UX | Onboard beta customer #1 (white-glove): PM + CSM walk the admin through setup. Observe, take notes, capture friction points. | PM + CSM | Beta environment, docs published |
| Product & UX | Onboard beta customers #2 and #3 (guided self-serve): provide docs + async Slack support. Observe setup time and support questions. | CSM | Beta environment, docs published |
| Product & UX | Daily bug triage during onboarding. Fix P0/P1 issues same day. | Engineering (on-call) | Beta customers live |
| Analytics Instrumentation | Monitor WAVU and scope_coverage metrics for beta customers. Report daily to PM. | Data Eng | Analytics live in beta |
| Documentation | Update docs based on beta customer feedback (expected: 5-10 clarifications or additions). | Technical Writer | Beta feedback |
| Support Enablement | Monitor Slack channel. Log all questions into runbook as new scenarios. | Support Champions | Training complete |

#### Week 8: Beta Stabilization & GA Planning

| Track | Deliverable | Owner | Dependencies |
|-------|-------------|-------|--------------|
| Permissions & Security | Final security sign-off: confirm all pen test and security review findings are resolved. Document residual risks (if any) with mitigations. | Security Lead | Pen test remediation complete |
| Permissions & Security | Scope enforcement audit: verify zero scope-bypass incidents during beta week. | Security Eng | Audit log data from beta |
| Product & UX | Beta retrospective: compile feedback from all beta customers. Prioritize GA polish items. | PM | 1 week of beta usage |
| Product & UX | Define GA scope: confirm deferred items (multi-dimension scopes, SIEM streaming, migration wizard, anomaly detection) and target timeline. | PM + Engineering Lead | Beta retro |
| Product & UX | GA launch checklist: marketing brief, changelog entry, in-app announcement, account manager talking points. | PM + Marketing | Beta retro |
| Analytics Instrumentation | Beta metrics report: WAVU, scope_coverage, setup time, support ticket volume, scope_boundary_hit frequency. | Data Eng + PM | 1 week of beta data |
| Documentation | Finalize all docs. Remove beta flags. Prepare for GA publication. | Technical Writer | Beta feedback incorporated |
| Support Enablement | Update runbook with real beta issues. Conduct 30-minute refresher for support team. | Support Lead | Beta support logs |
| Support Enablement | Define GA support SLA: P0 (scope bypass) = 1 hour response, P1 (enforcement bug) = 4 hours, P2 (UI issue) = 1 business day. | Support Lead + Engineering | Beta experience |

---

### Dependency Map (Critical Path)

```
Week 1: Permissions design doc ──────────────────────────────────────────────┐
         │                                                                    │
Week 2: Scope storage + Shadow mode ─────────────────────────────┐           │
         │                                                        │           │
Week 3: Shadow mode validation + Benchmark ──────────┐           │           │
         │                                            │           │           │
Week 4: Enforcement go-live ──────────────┐           │           │           │
         │                                 │           │           │           │
Week 5: Security review ─────┐            │           │           │           │
         │                    │            │           │           │           │
Week 6: Pen test + Beta env ──┼── Training │           │           │           │
         │                    │            │           │           │           │
Week 7: Beta onboarding ─────┘            │           │           │           │
         │                                 │           │           │           │
Week 8: GA planning ──────────────────────┘───────────┘───────────┘───────────┘
```

**Critical path:** Permissions design (W1) -> Scope storage + shadow mode (W2) -> Shadow validation + benchmark (W3) -> Enforcement go-live (W4) -> Security review (W5) -> Beta environment (W6) -> Beta onboarding (W7) -> Stabilization (W8).

**Key risk mitigations on the critical path:**
- Shadow mode (W2-W3) de-risks enforcement by validating correctness before flipping the switch.
- Security review is scheduled for W5 (not W7-W8) to leave remediation time.
- Beta onboarding starts with one white-glove customer (W7 day 1) to catch issues before the remaining customers go live.

---

### Resource Requirements

| Role | Headcount | Weeks | Notes |
|------|-----------|-------|-------|
| Backend Engineer (scope engine) | 2 | 8 | Core permissions and query injection |
| Backend Engineer (APIs, audit) | 1 | 6 (W2-W7) | View CRUD, audit log, API scoping |
| Frontend Engineer | 2 | 7 (W2-W8) | Admin UX, Governance Console, View catalog |
| Identity / SCIM Engineer | 1 | 4 (W1-W4) | SCIM integration, group sync |
| Product Designer | 1 | 4 (W1-W4) | Wireframes, UX polish |
| QA Engineer | 1 | 5 (W3-W7) | Integration testing, beta monitoring |
| Security Engineer | 1 | 4 (W1, W5-W7) | Threat model, review, pen test, hardening |
| Data / Analytics Engineer | 1 | 7 (W1-W7) | Event instrumentation, metrics pipelines |
| Technical Writer | 1 | 7 (W1-W7) | All documentation deliverables |
| PM | 1 | 8 | Coordination, beta management, GA planning |
| DevOps | 0.5 | 2 (W6-W7) | Beta environment provisioning |
| Support Lead | 0.5 | 4 (W1, W5-W8) | Training, runbook, beta support |
| CSM | 0.5 | 2 (W7-W8) | Beta customer onboarding |

**Total: ~12.5 FTE-equivalents across 8 weeks.**

---

### Success Criteria for Beta

| Metric | Target | Measurement |
|--------|--------|-------------|
| Weekly Active View Users (WAVU) | 60% of provisioned users per beta customer | Analytics pipeline |
| Scope Coverage | 90% of users have at least one scope within 7 days of admin setup | Analytics pipeline |
| Admin Setup Time | <2 hours for first scope + first official View | Observed during onboarding |
| Scope Bypass Incidents | 0 | Audit log + security monitoring |
| P0/P1 Bugs in Beta | <3 total | Bug tracker |
| Support Ticket Volume | <10 tickets per beta customer in Week 7 | Support channel logs |
| Net Promoter Score (admin) | >40 | Post-beta survey |
| Security Review Sign-off | Approved with no unresolved critical findings | Security team |

---

### Post-Beta / GA Roadmap (Deferred Items)

| Feature | Target | Rationale for Deferral |
|---------|--------|------------------------|
| Multi-dimension scopes (e.g., region AND department AND date range) | GA + 4 weeks | Increases scope engine complexity; single-dimension covers 80% of beta use cases |
| SIEM streaming (Splunk, Datadog webhook) | GA + 4 weeks | Requires integration testing with multiple SIEM platforms |
| Migration wizard (convert existing dashboards to Views) | GA + 2 weeks | Nice-to-have for onboarding; manual migration is feasible for beta |
| Personal View creation controls (admin can disable per group) | GA + 2 weeks | Low-risk addition; beta customers can manage via communication |
| Audit log anomaly detection (ML-based alerts) | GA + 8 weeks | R&D effort; not required for initial enterprise security approval |
| Dashboard Pack templates (pre-built Official Views by industry) | GA + 12 weeks | Content creation effort; beta validates the infrastructure first |

---

### Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Scope filter injection misses a query path (e.g., export, scheduled report) | Medium | Critical (data leak) | Shadow mode + explicit enumeration of all query entry points in W2. Integration test suite covers every path. |
| Performance regression under scope enforcement | Low | High | Benchmark in W3 with production-scale data. Performance budget enforced in CI. |
| SCIM sync delay causes stale scope assignments | Medium | Medium | Session-level scope refresh (5-min cache). SCIM push event triggers immediate invalidation. |
| Beta customer admin finds UX too complex | Medium | Medium | White-glove onboarding for customer #1. In-product onboarding wizard. Rapid iteration in W7. |
| Security review surfaces architectural issue requiring redesign | Low | Critical | Early threat modeling in W1. Security team involved in design review, not just code review. |
| 8-week timeline slips | Medium | High | Scoped beta (single-dimension scopes, no SIEM, no migration wizard). Weekly milestone check-ins. PM empowered to cut scope. |

---

*This document was produced using the Working Backwards method: start with the customer outcome (enterprise admins can deliver least-privilege, role-tailored analytics views), write the press release and FAQ as if the product already exists, then work backwards through the plan to make it real.*
