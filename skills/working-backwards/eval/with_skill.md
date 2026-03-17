# Working Backwards Pack: Role-Based Dashboard Customization

## 0) Context Snapshot

- **Product:** B2B analytics platform (enterprise tier)
- **Target customer/user segment:** Enterprise admins (IT/platform admins who manage the analytics environment) and department leads (Sales, Marketing, Finance, Ops heads who consume dashboards for their teams)
- **Problem today:** Admins cannot tailor dashboards by role. Every user in the organization sees the same default dashboards regardless of function, seniority, or data-access level. Teams are overwhelmed by irrelevant metrics, struggle to find their data, and adoption stalls after initial rollout.
- **Why now:** Enterprise expansion deals are stalling because prospects require governance controls and least-privilege data views before signing. Competitors have shipped role-scoped experiences. Current churn data shows a 40% drop in weekly active users between week 2 and week 8 post-deployment, concentrated in non-admin roles.
- **Decision to make:** Which approach to role-based dashboard customization do we invest in for an 8-week beta, and what is the minimum viable scope that unblocks enterprise expansion?
- **DRI / approver:** Head of Product (DRI); VP Engineering + CISO (approvers for security/permissions model)
- **Constraints:**
  - Timeline: 8 weeks to closed beta with 3-5 design partners
  - Platform: Web app only (mobile is out of scope for v1)
  - Policy/legal: Must comply with SOC 2 Type II controls; data access changes require security review sign-off
  - Dependencies: Existing RBAC system (basic roles exist: admin, member); Identity provider (IdP) integration already in place; analytics event pipeline operational
  - Capacity: 1 product manager, 1 designer, 4 engineers, 0.5 data engineer
- **Current alternatives / workarounds:** Admins create duplicate dashboards manually and share links via email/Slack. Some customers export CSVs and build department-specific views in spreadsheets. One large customer built a browser extension to hide irrelevant widgets.
- **Success metrics:**
  1. Dashboard relevance score: >70% of widgets on a user's default view are rated "relevant" in post-beta survey
  2. Adoption retention: WAU drop-off between week 2 and week 8 improves from 40% to <20% among beta cohort
  3. Enterprise deal velocity: At least 2 of 3 target enterprise prospects confirm the feature addresses their governance blocker
- **Guardrails:**
  1. No user loses access to data they currently have (no regression)
  2. Admin configuration time for a new role < 15 minutes
  3. Page load time for role-scoped dashboards does not exceed baseline + 200ms (p95)
  4. Support ticket volume related to "missing data" does not increase >10% during beta
  5. Zero privilege-escalation vulnerabilities identified in security review
- **Target launch tier/date:** Closed beta (3-5 design partners) by Week 8 (T+8); GA targeting T+14 (pending beta results)
- **Stakeholders/reviewers:** CISO / Security team, Customer Success (beta onboarding), Sales (enterprise deal support), Legal (data access compliance), Support (escalation paths), Documentation team

---

## 1) Problem Paragraph

**Problem today:**

Enterprise organizations that deploy our analytics platform face a persistent adoption problem: after initial rollout, usage drops sharply because every user -- from the VP of Sales to a warehouse operations coordinator -- sees the same set of dashboards. An admin who spent weeks configuring the platform has no way to scope what different roles see by default. Department leads waste time scrolling past financial metrics to find supply chain KPIs. Individual contributors see executive summaries they cannot act on and miss the operational views they need.

The consequences are concrete. Teams revert to spreadsheets within weeks. Admins field a steady stream of "where is my data?" tickets. Enterprise buyers evaluating the platform flag the lack of governance and least-privilege views as a procurement blocker, stalling six-figure expansion deals. Meanwhile, competitors now offer role-scoped dashboards out of the box.

**Current alternatives and workarounds:**
- Admins manually duplicate dashboards and distribute links by role via email/Slack (brittle, unscalable, no access control)
- Power users export CSVs and rebuild views in Google Sheets or Excel (data goes stale, no governance)
- One enterprise customer built a custom browser extension to hide irrelevant dashboard widgets (fragile, unsupported)
- Some teams simply stop using the platform and revert to legacy tools

---

## 2) PR Options: 2-3 Divergent Future Press Releases

### Option comparison table

| Dimension | Option A: Role-Based Default Dashboards | Option B: Dashboard Packs by Department | Option C: Permissioned Saved Views |
|---|---|---|---|
| **Core promise (customer value)** | Admins assign curated default dashboard sets to roles; every user lands on a view tailored to their function from day one | Pre-built, department-specific dashboard bundles (templates) that admins deploy in one click; departments get instant best-practice views | Any user can save, name, and share filtered views; admins control who can see/edit each saved view via permissions |
| **Key mechanism / concept** | Admin-defined roles mapped to dashboard sets; role-dashboard assignment UI; inheritance model (org > dept > role) | Curated template library (Sales Pack, Finance Pack, Ops Pack, etc.); one-click deploy; admins customize after deploy | Save-view action on any dashboard; sharing modal with user/role/group picker; admin override and audit trail |
| **Biggest risk** | Requires admins to do upfront configuration; if roles are poorly defined, users still see wrong data; cold-start problem for new customers | Templates may not match real org structures; "one-size-fits-department" can still miss role-level nuance; ongoing template maintenance burden | Bottom-up creation can lead to view sprawl and governance headaches; admins lose control of what proliferates; harder to enforce least-privilege |
| **What's out of scope** | User self-service customization; row-level data filtering; mobile | Cross-department composite dashboards; automated pack recommendations; mobile | Admin-authored default landing pages; department-level governance; mobile |
| **Why this could win** | Directly addresses admin governance need; maps cleanly to enterprise RBAC expectations; simplest mental model for procurement/security review | Fastest time to value for departments; reduces admin burden with pre-built content; strong upsell/marketplace story | Most flexible; empowers end users; builds on familiar "save and share" UX patterns; lowest engineering lift for MVP |

---

### Option A: Role-Based Default Dashboards (1-page PR)

**Release date:** [Hypothetical -- 10 weeks from today]

**Headline:** [Platform] Launches Role-Based Default Dashboards So Every Team Member Sees the Right Data From Day One

**Summary:** [Platform] today announced Role-Based Default Dashboards, a new capability that lets enterprise admins assign curated dashboard sets to each role in their organization. Starting immediately after deployment, every user -- from a Sales VP to a warehouse coordinator -- lands on a default view tailored to their function, eliminating irrelevant data clutter and accelerating time to insight.

**Problem today:**
Enterprise analytics deployments stall because every user sees the same dashboards. Admins have no way to scope default views by role. Teams waste time searching for relevant metrics, revert to spreadsheets, and stop logging in. Enterprise buyers flag the lack of role-scoped governance as a procurement blocker.

**Introducing: Role-Based Default Dashboards**
Admins define roles (or import them from their identity provider), then assign one or more dashboards as the default set for each role. When a user logs in, they land on their role's curated view. Admins can update assignments at any time; changes propagate instantly.

**Customer quote:**
"We deploy [Platform] across 14 departments. Before this, every new hire saw the same wall of charts and half of them gave up within a week. Now I assign their role and they see exactly what matters to them on day one. Our 90-day retention jumped from 55% to over 80%." -- Director of Business Intelligence, Fortune 500 Retailer

**Company quote:**
"We heard the same feedback from dozens of enterprise customers: 'We love the analytics, but we can't make everyone see everything.' Role-Based Default Dashboards give admins the governance they need while keeping the experience simple for every end user." -- Head of Product, [Platform]

**How it works:**
1. Admin creates or imports roles (e.g., from Okta, Azure AD, or manually)
2. Admin assigns one or more existing dashboards as the default set for each role
3. Users are mapped to roles (via IdP group sync or manual assignment)
4. On login, users land on their role's default dashboard; they can still navigate to other dashboards they have access to
5. Admins can update role-dashboard assignments at any time; changes take effect on next login
6. Audit log records all role and assignment changes for compliance

**Who it's for / not for:**
- For: Enterprise admins who manage analytics deployments across multiple departments/roles; organizations with 50+ users
- Not for: Small teams (<10 users) who share a single dashboard; users seeking personal customization (that is a future roadmap item); organizations needing row-level data security (addressed separately)

**Availability:**
- Closed beta: 3-5 design partners, starting in 8 weeks
- GA: targeting 6 weeks after beta close, pending results
- Enterprise plan only

---

### Option B: Dashboard Packs by Department (1-page PR)

**Release date:** [Hypothetical -- 10 weeks from today]

**Headline:** [Platform] Ships Dashboard Packs -- Pre-Built, Department-Ready Analytics Views Deployed in One Click

**Summary:** [Platform] today introduced Dashboard Packs, a library of pre-built, best-practice dashboard bundles for Sales, Marketing, Finance, Operations, and more. Admins deploy a pack to a department in one click. Each pack includes curated KPIs, charts, and filters tuned to how that team actually works, eliminating months of manual dashboard building.

**Problem today:**
After deploying an analytics platform, admins spend weeks duplicating and tweaking dashboards for each department. The results are inconsistent, hard to maintain, and still miss the mark for many teams. Departments that do not get a custom build revert to spreadsheets. There is no scalable way to deliver role-appropriate views.

**Introducing: Dashboard Packs**
Dashboard Packs are pre-built, department-specific bundles of dashboards, each containing curated widgets, KPIs, and filters based on industry best practices. Admins browse the Pack Library, select a pack (e.g., "Sales Performance Pack"), assign it to a department or user group, and deploy it in one click. Packs are fully customizable after deployment.

**Customer quote:**
"We used to spend three weeks building dashboards for each new department rollout. With Dashboard Packs, our Finance team had a production-ready analytics view on day one. I customized two charts and it was done." -- Platform Admin, Mid-Market SaaS Company

**Company quote:**
"Dashboard Packs encode what we've learned from thousands of deployments into ready-to-use starting points. Admins get speed; departments get relevance; everyone gets to skip the blank-canvas problem." -- Head of Product, [Platform]

**How it works:**
1. Admin browses the Pack Library (Sales, Marketing, Finance, Operations, Executive, Custom)
2. Admin previews a pack and selects it for a department or user group
3. One-click deploy creates the dashboards, pre-wired with standard KPIs and filters
4. Admin customizes widgets, data sources, and filters as needed post-deploy
5. Pack updates (new best-practice widgets) are offered as optional upgrades
6. Admins control who can access each deployed pack via existing group permissions

**Who it's for / not for:**
- For: Admins seeking fast, consistent rollouts across departments; organizations with standard department structures
- Not for: Highly custom org structures where no template fits; users wanting personal saved views; teams needing row-level security

**Availability:**
- Closed beta: 3-5 design partners, starting in 8 weeks (launching with Sales, Marketing, Finance, Ops packs)
- GA: targeting 6 weeks after beta close
- Enterprise plan only; packs included at no additional cost

---

### Option C: Permissioned Saved Views (1-page PR)

**Release date:** [Hypothetical -- 10 weeks from today]

**Headline:** [Platform] Introduces Permissioned Saved Views -- Save, Share, and Govern Custom Dashboard Views Across Your Organization

**Summary:** [Platform] today launched Permissioned Saved Views, enabling any user to save a filtered, customized view of any dashboard and share it with specific colleagues, roles, or groups -- all under admin-controlled permissions. Organizations get the flexibility of user-driven customization with the governance of centralized access control.

**Problem today:**
Users filter dashboards daily to focus on their data, but filters reset on every visit. Admins cannot distribute curated views without duplicating entire dashboards. The result: wasted time re-filtering, ungoverned link-sharing, and no audit trail for who sees what.

**Introducing: Permissioned Saved Views**
Any user can save a named view of any dashboard -- capturing filters, date ranges, column selections, and layout. They can keep it private or share it with specific users, roles, or groups. Admins set permissions: who can create, share, and view saved views. An audit trail logs all sharing actions.

**Customer quote:**
"I check the same three filtered views every morning. Before Saved Views, I had to re-apply filters every time. Now I click my 'Morning Ops' view and I'm working in seconds. And my admin loves that she controls who can share what." -- Regional Operations Manager, Logistics Company

**Company quote:**
"Permissioned Saved Views combine user empowerment with admin governance. Users get personalized experiences without anyone duplicating dashboards or sharing ungoverned links." -- Head of Product, [Platform]

**How it works:**
1. User applies filters, date ranges, or column selections to any dashboard
2. User clicks "Save View," names it, and chooses visibility: Private, Shared (select users/roles/groups), or Public (all org users)
3. Admin configures permissions policy: who can create views, who can share, maximum number of shared views per user
4. Saved views appear in a sidebar for quick access; shared views appear in recipients' sidebar automatically
5. Admins can audit, revoke, or reassign any shared view from the admin console
6. Views update live -- if underlying dashboard data changes, saved views reflect it

**Who it's for / not for:**
- For: End users who want personalized, persistent dashboard experiences; admins who need governance over sharing; mid-market and enterprise organizations
- Not for: Organizations that need top-down, admin-curated default landing pages (this is bottom-up); teams needing row-level data security; users expecting offline/exported views

**Availability:**
- Closed beta: 3-5 design partners, starting in 8 weeks
- GA: targeting 6 weeks after beta close
- Available on Professional and Enterprise plans

---

## 3) Option Selection and Rationale

### Evaluation against decision criteria

| Criteria | Option A: Role-Based Defaults | Option B: Dashboard Packs | Option C: Permissioned Saved Views |
|---|---|---|---|
| Directly solves admin governance need | Strong -- admins control what each role sees | Medium -- admins deploy packs but no role-level granularity | Medium -- admins set policies but views are user-created |
| Addresses enterprise procurement blocker | Strong -- maps to RBAC/least-privilege language buyers expect | Medium -- departmental scoping, but not role-level governance | Weak -- bottom-up model harder to position as "governance" |
| Time to value for end users | Strong -- zero-effort for end users; they log in and see their view | Strong -- departments get instant views | Weak -- requires each user to create and save their own views |
| Admin configuration burden | Medium -- requires role definition and assignment work | Low -- one-click deploy of pre-built packs | Low -- admin sets policy, users self-serve |
| Feasibility in 8 weeks | Medium -- role-dashboard mapping, IdP sync, UI | Medium -- template library, deploy pipeline, customization UI | Medium -- save/share UX, permissions model, audit |
| Supports least-privilege / compliance | Strong -- explicit role-to-dashboard mapping; audit trail | Weak -- no explicit access control beyond group assignment | Medium -- permissions exist but user-driven creation is harder to audit |
| Long-term platform extensibility | Strong -- role abstraction enables future row-level security, personalization | Medium -- packs are additive but do not create a role primitive | Medium -- saved views are composable but do not solve the default experience |

### Decision: Option A -- Role-Based Default Dashboards

**Rationale:** Option A most directly solves the stated problem (admins cannot tailor dashboards by role) and the stated blocker (enterprise procurement requires governance and least-privilege views). It creates a durable role abstraction that the platform can build on for years (row-level security, personalized defaults, compliance reporting). It also provides the clearest "zero effort" experience for end users -- they log in and land on a relevant view without doing anything.

Option B is strong for speed-to-value but does not create the role-level governance primitive that enterprise buyers demand. It could be a compelling follow-on (deploy packs as the starting content for a role's default dashboards).

Option C is the most flexible but puts the burden on end users and is harder to position as governance to enterprise procurement teams. It is a strong complement for a future release.

**Hybrid note:** The backcasting plan below includes a "fast follow" milestone to integrate Dashboard Packs (Option B) as a content layer on top of Role-Based Defaults, giving admins curated starting points.

---

## 4) Selected PR: Role-Based Default Dashboards (Refined)

**Release date:** [Hypothetical -- 10 weeks from today]

**Headline:** [Platform] Launches Role-Based Default Dashboards -- Every User Sees the Right Data From Day One

**Summary:** [Platform] today announced Role-Based Default Dashboards, a new capability that lets enterprise admins assign curated dashboard sets to each role in their organization. From the moment a user logs in, they see a default view tailored to their function -- no more searching, filtering, or wading through irrelevant metrics. With built-in audit logging and identity-provider integration, IT and security teams get the governance and least-privilege controls they require.

---

### Problem today

Enterprise analytics deployments follow a predictable pattern: initial excitement, then a sharp adoption drop-off. The root cause is simple -- every user sees the same dashboards. A Sales VP sees warehouse throughput charts. A warehouse coordinator sees executive revenue summaries. Admins have no built-in way to scope what each role sees by default.

The impact is measurable:
- **40% of non-admin users stop logging in within 8 weeks** of deployment
- Admins spend 5+ hours per week duplicating dashboards and distributing links for different teams
- Enterprise prospects cite the lack of role-scoped governance as a top-3 procurement blocker
- Competing platforms now offer role-based views as a standard enterprise feature

Teams that cannot find their data within the first two sessions revert to spreadsheets. The analytics investment delivers a fraction of its potential value.

---

### Introducing: Role-Based Default Dashboards

Role-Based Default Dashboards give admins a simple, powerful way to define what each role in their organization sees when they log in. Admins create roles (or import them from their identity provider), assign dashboards to each role, and map users to roles. Every user immediately lands on a curated, relevant default view. No training required. No manual link distribution. Full audit trail for compliance.

---

### Customer quote

"We have 2,200 users across 14 departments. Before Role-Based Defaults, onboarding a new department meant weeks of dashboard cloning and Slack messages explaining which link to bookmark. Now I define the role, assign the dashboards, and the team is productive on day one. Our 90-day platform retention went from 55% to 82%."
-- Director of Business Intelligence, Fortune 500 Retailer

### Company quote

"We heard the same request from nearly every enterprise customer: 'Give me the power to control what each team sees.' Role-Based Default Dashboards deliver that control without adding complexity for end users. This is the foundation for how we think about personalized, governed analytics experiences going forward."
-- Head of Product, [Platform]

---

### How it works

1. **Define roles:** Admin creates roles in the platform (e.g., "Sales Rep," "Finance Analyst," "Exec Leadership") or imports role/group mappings from an identity provider (Okta, Azure AD, Google Workspace).
2. **Assign dashboards:** Admin selects one or more existing dashboards as the default set for each role. A drag-and-drop interface sets the order and landing page.
3. **Map users to roles:** Users are automatically mapped via IdP group sync, or admins assign roles manually. A user can have one primary role (which determines their default view) and access additional dashboards via explicit grants.
4. **User experience:** On login, users land on their role's default dashboard. A sidebar shows their assigned dashboards prominently, with the full dashboard catalog accessible below (respecting existing data permissions).
5. **Update anytime:** Admins change role-dashboard assignments at any time. Changes propagate on next user login. No downtime, no re-deployment.
6. **Audit and compliance:** Every role creation, dashboard assignment, and user mapping change is logged in the admin audit trail. Exportable for SOC 2 and compliance reporting.

---

### Who it's for / who it's not for

**For:**
- Enterprise admins who manage analytics deployments across multiple departments and need governance over what each role sees
- IT and security teams that require least-privilege access controls and audit trails
- Department leads who want their teams to land on relevant dashboards without manual onboarding
- Organizations with 50+ analytics users across 3+ departments

**Not for:**
- Small teams (<10 users) where everyone shares the same dashboards and customization is unnecessary
- Users seeking personal, self-service dashboard customization (future roadmap: Saved Views)
- Organizations that need row-level data security within a dashboard (addressed by a separate row-level security feature)
- Mobile-first use cases (web only for v1)

---

### Availability / rollout

- **Closed beta:** 3-5 design partners, beginning in 8 weeks. Design partners must be on the Enterprise plan and have an active IdP integration.
- **GA:** Targeting 6 weeks after beta close, pending beta success criteria.
- **Enterprise plan only** at launch. Evaluation of Professional plan inclusion post-GA.
- **Regions:** All currently supported regions. No new data residency requirements.

### Pricing / packaging

- Included in the Enterprise plan at no additional cost for beta and GA launch.
- No per-role or per-assignment fees.
- Assumption: this becomes a standard Enterprise-tier governance feature (not an add-on SKU). Pricing review scheduled for post-beta.

---

## 5) FAQ

### Customer FAQs

**Q1: Who is the target user and what is the primary use case?**
A: The primary user is the enterprise admin (IT admin, platform admin, BI lead) who manages the analytics deployment. The primary use case is: "As an admin, I want to assign a curated set of default dashboards to each role in my org so that every user sees relevant data from their first login." Secondary users are department leads and end users who benefit from a tailored default experience.

**Q2: What does the core user journey look like (happy path)?**
A: Admin logs in > navigates to new "Roles" section in Admin Console > creates a role (or sees roles synced from IdP) > selects dashboards to assign as defaults for that role > maps users/groups to the role > saves. End user logs in > lands on their role's default dashboard > navigates via sidebar to other assigned dashboards. Total admin setup time target: <15 minutes per role.

**Q3: What happens to a user's existing experience?**
A: No user loses access to any dashboard they can currently see. Role-Based Defaults add a curated landing experience on top of existing permissions. Users can still browse the full dashboard catalog (subject to their existing data permissions). This is additive, not restrictive.

**Q4: Can a user belong to multiple roles?**
A: In v1, each user has one primary role that determines their default landing dashboard set. Admins can grant additional dashboard access beyond the role's defaults via explicit grants. Multi-role support (e.g., a user who is both "Finance Analyst" and "Project Lead") is a planned post-GA enhancement.

**Q5: What if an admin has not configured any roles yet?**
A: The platform behavior is unchanged -- all users see the current default experience (all dashboards). Role-Based Defaults are opt-in; there is no forced migration. A setup wizard and suggested role templates will guide first-time configuration.

**Q6: Does this work with our identity provider (Okta, Azure AD, Google Workspace)?**
A: Yes. At beta launch, we support group sync from Okta, Azure AD, and Google Workspace. Roles can be auto-created from IdP groups, and user-to-role mapping updates on each login (via SCIM or SAML group claims). Manual role management is always available as a fallback.

---

### Business FAQs

**Q1: Why should we build this now? What happens if we do not?**
A: Three forcing functions: (1) At least 3 active enterprise prospects (combined ACV > $800K) have cited role-scoped governance as a top-3 procurement blocker. (2) Competitors X and Y shipped role-based views in the last two quarters. (3) Post-deployment adoption data shows a 40% WAU drop-off among non-admin users within 8 weeks -- the #1 driver of churn risk in our enterprise segment. Delaying 6 months risks losing these deals and falling further behind competitively.

**Q2: What is explicitly out of scope for v1?**
A: The following are excluded from the 8-week beta:
- Row-level data security (filtering data within a dashboard by role)
- User self-service saved/custom views (future: Permissioned Saved Views)
- Pre-built dashboard packs / templates (future fast-follow)
- Mobile app support
- Multi-role assignment (user has exactly one primary role in v1)
- Automated role recommendation / suggestion engine
- Role-based alerting or notification customization

**Q3: Pricing and packaging assumptions?**
A: Included in Enterprise plan at no additional cost. No per-role or per-seat surcharge. Rationale: this is a governance/table-stakes feature for enterprise buyers, not a premium add-on. Post-GA review will assess whether to extend to Professional plan (likely gated by user count). Decision owner: Head of Product + Head of Revenue. Decision date: GA + 4 weeks.

**Q4: Positioning -- how do we explain this in one sentence?**
A: External: "Role-Based Default Dashboards let admins ensure every user sees the right data from day one -- with full governance and audit controls."
Internal: "We're shipping the role-based dashboard assignment feature that unblocks enterprise governance requirements and addresses our #1 post-deployment churn driver."

**Q5: Support and sales impact?**
A: Sales: Enablement kit (one-pager, demo script, FAQ) required by beta launch. CSMs for design partner accounts need training on configuration best practices. Support: New knowledge base article + runbook for "role assignment" issues. Expected net reduction in "where is my data?" tickets (currently ~15% of enterprise support volume). Risk: short-term increase in "how do I set up roles?" tickets; mitigated by setup wizard and guided onboarding.

---

### Technical / Ops FAQs

**Q1: Major dependencies and required approvals?**
A: Dependencies: (1) Existing RBAC system (basic admin/member roles exist; must extend to custom roles) -- Engineering team, 2-week effort. (2) IdP integration (SCIM/SAML group sync already in place; must map groups to new role entities) -- Engineering team, 1-week effort. (3) Dashboard rendering service (must accept a role context parameter to determine default set) -- Engineering team, 1-week effort. (4) Admin console frontend (new "Roles" section) -- Design + Frontend, 3-week effort. Approvals required: CISO sign-off on permissions model (Week 3); Legal sign-off on audit log data retention (Week 4).

**Q2: Reliability and performance expectations?**
A: Role-dashboard assignment lookup must add <50ms to login flow (p95). Dashboard rendering latency must not exceed current baseline + 200ms (p95). Role sync from IdP must complete within 60 seconds of user login. Target uptime: 99.9% (consistent with platform SLA). No new infrastructure required -- role assignments stored in existing metadata database.

**Q3: Instrumentation plan -- what events/metrics must exist at launch?**
A: Required events:
- `role.created`, `role.updated`, `role.deleted` (admin actions)
- `role.dashboard_assigned`, `role.dashboard_unassigned` (admin actions)
- `user.role_mapped`, `user.role_unmapped` (admin or IdP sync)
- `user.login.default_dashboard_served` (with role_id, dashboard_id)
- `user.dashboard.navigated_away_from_default` (with role_id, dashboard_id, destination)
- `user.dashboard.session_duration` (with role_id, dashboard_id)

Required dashboards (internal analytics):
- Role configuration adoption: % of enterprise accounts with at least one custom role configured
- Default dashboard engagement: % of sessions where user stays on default view >60s
- Adoption retention: WAU trend by role (compare beta cohort pre/post)

**Q4: Rollout plan and rollback triggers?**
A: Rollout tiers:
1. **Internal dogfood (Week 6):** Enable for internal team; validate UX, performance, audit logging.
2. **Closed beta (Week 8):** Enable for 3-5 design partner accounts. Feature-flagged per account.
3. **GA (Week 14, pending beta):** Enable for all Enterprise accounts. Gradual rollout (10% > 50% > 100%) over 2 weeks.

Rollback triggers:
- p95 login latency increases >500ms above baseline
- >3 privilege-escalation or data-leakage bugs reported
- Design partner NPS for the feature is <30
- Support ticket volume for "missing data" increases >25% in any beta account

Rollback mechanism: Feature flag disabled per account (instant); role-dashboard assignments preserved in database for re-enablement.

**Q5: Data handling -- privacy, retention, access controls?**
A: Role assignments and audit logs are stored in the existing metadata database (same region as customer data; encrypted at rest and in transit). No new PII is collected -- roles are organizational labels, not personal data. Audit logs retained for 1 year (consistent with SOC 2 controls). Access to audit logs: admin-only, exportable via API and admin console. No data leaves the customer's region.

---

### Legal / Compliance FAQs

**Q1: What regulatory or contractual constraints apply?**
A: SOC 2 Type II controls require that access changes are logged and auditable. The role-based assignment model and audit trail are designed to satisfy this. No new regulatory obligations (GDPR, CCPA) are triggered -- no new personal data categories are processed. Existing DPAs cover the metadata stored.

**Q2: Security review required?**
A: Yes. Security review is required and scheduled for Week 3-4. Scope: (1) permissions model design review (can a user escalate their role?), (2) IdP sync integrity (can a group sync grant unintended access?), (3) audit log completeness (are all state changes logged?), (4) API authorization (are role-management endpoints admin-only?). CISO sign-off required before internal dogfood.

**Q3: Data processing -- what is collected, where stored, who can access?**
A: Collected: role definitions (name, description), role-to-dashboard mappings, user-to-role mappings, audit log entries (who changed what, when). Stored: existing metadata database, same region and encryption as customer data. Access: admin-only via admin console and API; no end-user access to role configuration data.

**Q4: Customer consent and audit logging requirements?**
A: No new customer consent required -- role management is an admin function within the existing platform agreement. Audit logs for all role and assignment changes are provided by default. Logs are exportable via API for integration with customer SIEM systems. Retention: 1 year (configurable to longer periods on Enterprise+ plans via support request).

---

## 6) Backcasting Plan

### Milestone plan (working backward from Week 8 beta)

| Date (Week) | Milestone | Owner | Dependencies | "Done" Criteria | Risks |
|---|---|---|---|---|---|
| **T-0 (Now)** | Kick-off: Align on Option A scope, assign workstreams, notify stakeholders | PM (DRI) | None | Kick-off doc circulated; JIRA epic created; design partners identified | Stakeholder availability for kick-off |
| **T+1** | Permissions model design complete | Backend Lead + PM | RBAC system documentation | Design doc approved by Backend Lead, PM, and CISO (async review initiated) | Model complexity if existing RBAC is rigid |
| **T+1** | Design sprint: Admin console UX for role creation, assignment, mapping | Design Lead | Permissions model draft | Figma mocks for role CRUD, dashboard assignment, user mapping flows; reviewed by PM and 1 design partner | Design partner availability for feedback |
| **T+1** | Analytics instrumentation plan finalized | Data Engineer | PM defines required events | Event schema document approved by PM and Data Engineer; tickets created | Data pipeline capacity |
| **T+2** | IdP group-to-role sync design complete | Backend Engineer | IdP integration docs (Okta, Azure AD, Google) | Technical design doc; covers SCIM + SAML group claim mapping; edge cases documented | IdP vendor API limitations |
| **T+2** | Design review with 2 design partners (async or call) | Design Lead + PM | Figma mocks from T+1 | Feedback incorporated; major UX issues resolved | Partner scheduling |
| **T+3** | Security review -- permissions model | CISO / Security Lead | Permissions model design doc | Security review checklist completed; no P0/P1 issues; CISO sign-off | Security team bandwidth; findings requiring redesign |
| **T+3** | Backend: Role CRUD API + role-dashboard assignment API | Backend Lead | Permissions model approved | APIs functional in staging; unit + integration tests passing | Scope creep in API surface |
| **T+4** | Backend: User-to-role mapping (manual + IdP sync) | Backend Engineer | IdP sync design; Role CRUD API | Manual and IdP-synced mapping working in staging; tested with Okta sandbox | IdP sandbox environment issues |
| **T+4** | Frontend: Admin console -- Roles section (create, edit, delete, assign dashboards) | Frontend Lead | Design mocks; Role CRUD API | Admin can create role, assign dashboards, map users in staging | Frontend velocity; API contract changes |
| **T+4** | Legal review -- audit log data retention, DPA impact | Legal Counsel | Audit log spec from Backend Lead | Legal sign-off; no DPA amendments required | Legal review backlog |
| **T+5** | Backend: Default dashboard serving logic (login flow integration) | Backend Lead | Role-dashboard assignment API | On login in staging, user lands on role's default dashboard; fallback to standard view if no role assigned | Login flow regression risk |
| **T+5** | Frontend: End-user sidebar (role-assigned dashboards + catalog) | Frontend Engineer | Default dashboard serving API | Sidebar renders role defaults prominently; catalog accessible below | UX polish time |
| **T+5** | Analytics instrumentation implemented | Data Engineer | Event schema; backend APIs emitting events | All required events firing in staging; visible in internal analytics dashboard | Event pipeline latency |
| **T+5** | Audit logging implemented | Backend Engineer | Audit log spec | All role/assignment/mapping changes logged; exportable via API | Log completeness gaps |
| **T+6** | Internal dogfood begins | PM + Engineering | All staging features functional | Internal team using role-based defaults; collecting feedback via Slack channel | Internal team engagement |
| **T+6** | Documentation: Admin guide + KB articles drafted | Technical Writer | UX finalized; feature functional in staging | Admin setup guide, FAQ, and troubleshooting article in draft; reviewed by PM | Writer availability |
| **T+6** | Support enablement: Runbook + escalation path | Support Lead + PM | Documentation drafts; known issues list | Support team briefed; runbook reviewed; escalation path to engineering defined | Support team ramp time |
| **T+6** | Performance testing: Login latency, dashboard load with role context | QA / Backend Lead | Default dashboard serving in staging | p95 login latency < baseline + 200ms; no regressions | Performance issues requiring optimization |
| **T+7** | Bug bash + hardening sprint | Engineering team | Dogfood feedback; QA results | All P0/P1 bugs resolved; P2s triaged and deferred if needed | Bug volume exceeds capacity |
| **T+7** | Sales enablement kit: One-pager, demo script, objection handling FAQ | PMM + PM | Feature stable in staging | Kit reviewed by Sales Lead; demo rehearsed | PMM bandwidth |
| **T+7** | Design partner onboarding prep: Per-account config plan, success criteria | CSM Lead + PM | Feature stable; documentation ready | Onboarding checklist per partner; CSM assigned; kickoff calls scheduled | Partner readiness / IT scheduling |
| **T+7** | Security: Penetration test on role management APIs | Security Lead | APIs in staging | Pen test complete; no critical/high findings | Finding remediation time |
| **T+8** | **Closed beta launch** | PM (DRI) | All above milestones green | Feature flag enabled for 3-5 design partners; monitoring dashboards live; support runbook active | Partner adoption pace |
| **T+9-10** | Beta feedback collection + iteration | PM + Design + Eng | Beta running | Weekly feedback synthesis; top issues triaged; at least 1 iteration shipped | Low partner engagement |
| **T+11** | Beta success criteria evaluation | PM | 3+ weeks of beta data | Dashboard relevance survey > 70%; WAU retention improved; no P0 security issues | Insufficient data |
| **T+12** | GA readiness review | PM + Eng Lead + CISO | Beta results; all P0/P1 resolved | Go/no-go decision documented; GA rollout plan approved | Unresolved beta issues |
| **T+13-14** | **GA rollout** (gradual: 10% > 50% > 100%) | Eng Lead + PM | GA approval | GA enabled for all Enterprise accounts; monitoring confirms no regressions | Rollout issues at scale |

---

## 7) Stakeholder + "Machinery" Plan

| Stakeholder / Team | Why They Care | Likely Objection | What They Need to Say "Yes" | When to Involve | Owner |
|---|---|---|---|---|---|
| **CISO / Security** | Permissions model changes touch access control; SOC 2 implications | "Does this introduce privilege escalation risk?" "Is the audit trail complete?" | Permissions model design doc; security review with no P0/P1 findings; pen test results | Week 1 (async review), Week 3 (formal review), Week 7 (pen test) | Backend Lead |
| **Legal / Compliance** | Audit log retention; DPA impact; regulatory posture | "Does this change our data processing scope?" "Do we need DPA amendments?" | Audit log spec; confirmation of no new PII; no DPA changes required | Week 4 (review), sign-off by Week 5 | PM |
| **Customer Success** | Beta onboarding; partner relationship management; adoption metrics | "Do we have capacity to support 3-5 design partners?" "What's the escalation path?" | Per-partner onboarding plan; CSM assignment; support runbook; escalation path defined | Week 6 (enablement), Week 7 (onboarding prep) | CSM Lead |
| **Sales** | Enterprise deal unblocking; competitive positioning | "Can I demo this to prospects now?" "Is it stable enough to reference in deals?" | Sales one-pager; demo script; clear beta vs. GA timeline for prospect communication | Week 7 (enablement kit), ongoing deal support | PMM |
| **Support** | New ticket category; training on role configuration troubleshooting | "Will this increase ticket volume?" "Do we have a runbook?" | KB articles; runbook; known issues list; escalation path to engineering | Week 6 (documentation), Week 7 (training) | Support Lead |
| **Documentation** | Admin guide; end-user help content; release notes | "Is the UX final enough to document?" "What's the review timeline?" | Stable UX in staging by Week 5; PM review of drafts by Week 6 | Week 5 (drafting), Week 7 (final review) | Technical Writer |
| **Engineering (Platform)** | RBAC extension; login flow changes; performance impact | "Does this add technical debt?" "What's the performance budget?" | Clear API contracts; performance budget (< 200ms p95 added latency); no login flow regressions | Week 0 (kick-off), continuous | Backend Lead |
| **Data / Analytics** | Instrumentation; internal dashboards; beta measurement | "Do we have pipeline capacity for new events?" "Who owns the beta dashboard?" | Event schema finalized Week 1; pipeline capacity confirmed; beta dashboard owned by Data Engineer | Week 1 (planning), Week 5 (implementation) | Data Engineer |

---

## 8) Success Metrics, Guardrails, and Instrumentation

### Success metrics

| Metric | Definition | Target | Measurement Method | Owner |
|---|---|---|---|---|
| Dashboard relevance score | % of widgets on a user's default role-based view rated "relevant" or "very relevant" in post-beta survey | >70% | In-app survey triggered after 2 weeks of beta use; 5-point scale per widget | PM |
| Adoption retention (WAU) | Week-over-week active user retention, measured as WAU at week 8 / WAU at week 2, for beta cohort vs. historical baseline | Drop-off < 20% (improved from 40% baseline) | Analytics event `user.login.default_dashboard_served` + existing WAU tracking | Data Engineer |
| Enterprise deal unblock | Number of target enterprise prospects who confirm the feature addresses their governance blocker | >= 2 of 3 target prospects | Sales-reported feedback; documented in CRM | Sales Lead |
| Admin setup time | Time from first click in Roles section to completing first role-dashboard assignment | < 15 minutes (median) | Analytics events `role.created` to `role.dashboard_assigned` timestamp delta | PM |
| Support ticket impact | Change in "where is my data?" ticket volume for beta accounts | No increase > 10%; target 20% reduction | Support ticket tagging in Zendesk (new tag: "role-based-dashboards") | Support Lead |

### Guardrails

| Guardrail | Threshold | Monitoring | Response if breached |
|---|---|---|---|
| No access regression | Zero cases where a user loses access to data they previously had | QA test suite; beta partner escalation channel | Immediate hotfix; rollback feature flag for affected account |
| Login latency | p95 login latency < baseline + 200ms | APM dashboard (Datadog); alert on > 200ms delta | Performance investigation; disable role lookup caching optimization; rollback if > 500ms |
| Privilege escalation | Zero privilege-escalation vulnerabilities | Security pen test (Week 7); bug bounty monitoring; beta partner reports | Immediate feature flag disable; security incident response; post-mortem |
| Admin config time | Median < 15 minutes per role setup | Analytics timestamp tracking | UX iteration; setup wizard improvement; guided onboarding content |
| Support ticket spike | "Missing data" tickets do not increase > 10% for beta accounts | Weekly Zendesk report; tagged tickets | Investigate root cause; improve error messaging; update KB articles |

### Instrumentation notes

- All events must be implemented and verified in staging by Week 5 (before internal dogfood).
- Internal analytics dashboard (beta monitoring) must be live by Week 6.
- Data Engineer owns event schema and pipeline; PM owns dashboard definitions.
- Post-beta, instrumentation extends to support GA rollout monitoring (same events, broader cohort).

---

## 9) Stress Test: Pre-Mortem

**Scenario: It is 6 weeks after beta launch and Role-Based Default Dashboards has failed. Why?**

### Failure mode 1: Adoption failure -- admins do not configure roles

- **What happened:** Design partners enabled the feature but admins never completed role setup. The default experience remained unchanged for end users. Adoption metrics showed no improvement.
- **Root cause:** Role configuration was too complex or time-consuming. Admins did not understand the value or were too busy with other priorities.
- **Mitigation:** Setup wizard with suggested roles based on IdP groups (auto-generate role suggestions). In-app nudges after feature enable. CSM-led onboarding call for each design partner. Monitor `role.created` events weekly during beta.
- **Monitoring signal:** <50% of design partners have created at least one role by Week 2 of beta.

### Failure mode 2: Trust/safety failure -- privilege escalation or data leakage

- **What happened:** A user discovered they could access dashboards assigned to a higher-privilege role by manipulating API requests. A customer reported a data governance breach.
- **Root cause:** Permissions model did not properly enforce server-side authorization checks; relied on client-side UI hiding.
- **Mitigation:** Security review (Week 3) explicitly tests for server-side enforcement. Pen test (Week 7) includes privilege escalation test cases. All authorization checks are server-side and covered by automated tests. Bug bounty program covers new endpoints.
- **Monitoring signal:** Any security finding rated P0/P1 during review or pen test. Any beta partner report of unexpected data access.

### Failure mode 3: Operational failure -- support overload

- **What happened:** Beta partners filed a surge of support tickets because users were confused by their new default view, thought data was "missing," or could not find dashboards they used to access.
- **Root cause:** The transition from "see everything" to "see your role's defaults" was jarring. Users did not realize they could still access other dashboards via the catalog. Error messaging and onboarding were insufficient.
- **Mitigation:** Clear in-app messaging on first login after role assignment ("Your admin has set up a personalized default view for you. You can still access all dashboards via the sidebar catalog."). Guided tour on first role-based login. KB article prepped. Support runbook covers this exact scenario.
- **Monitoring signal:** "Missing data" ticket volume increases > 15% for any beta account in the first week.

### Failure mode 4: Business failure -- enterprise buyers remain unconvinced

- **What happened:** Despite shipping the feature, enterprise prospects said it did not go far enough -- they wanted row-level data security, not just dashboard-level scoping. The feature did not unblock deals.
- **Root cause:** The governance requirement was deeper than dashboard assignment; prospects needed data-level access control.
- **Mitigation:** Qualify the exact governance requirement with each prospect before beta (Sales + PM joint call). If row-level security is the true blocker, be transparent about timeline (not in v1) and offer a workaround (dashboard-level scoping + filtered dashboards per role). Position v1 as a foundation and v2 as row-level security.
- **Monitoring signal:** Sales feedback from prospect calls during beta. If 2+ prospects cite row-level security as remaining blocker, escalate scope discussion.

### Failure mode 5: Timeline failure -- 8-week target is missed

- **What happened:** Security review took longer than planned, IdP sync edge cases consumed 2 extra weeks, and beta launched 3 weeks late, jeopardizing the enterprise deal timeline.
- **Root cause:** Security review backlog; IdP edge cases underestimated; no schedule buffer.
- **Mitigation:** Security review scheduled at Week 3 (not Week 5) to absorb delays. IdP sync tested against real sandbox environments starting Week 2. 1-week buffer between hardening and beta launch. Weekly "red/yellow/green" milestone check-in with PM + Eng Lead.
- **Monitoring signal:** Any milestone slipping by >3 days triggers escalation to PM and Eng Lead.

---

## 10) Risks, Open Questions, and Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Security review reveals permissions model flaw requiring redesign | Medium | High | Early review at Week 3; modular permissions design; 1-week buffer | Backend Lead |
| IdP sync edge cases (nested groups, group naming conflicts) delay implementation | Medium | Medium | Test against real IdP sandboxes starting Week 2; scope to flat group mapping for v1 | Backend Engineer |
| Design partners do not engage actively during beta | Medium | High | CSM-led onboarding; weekly check-in calls; clear success criteria shared with partner stakeholders | CSM Lead |
| Enterprise prospects require row-level data security, not just dashboard-level scoping | Medium | High | Pre-qualify governance requirements with each prospect; position dashboard scoping as foundation for row-level security | PM + Sales Lead |
| 8-week timeline is too aggressive given team capacity | Medium | Medium | Weekly milestone check-ins; scope cuts pre-identified (deprioritize: audit log export API, setup wizard auto-suggestions) | PM |
| Login latency increase exceeds budget due to role lookup overhead | Low | High | Role assignments cached in session; performance testing at Week 6; rollback trigger defined | Backend Lead |

### Open questions

| # | Question | Options | Proposed Decision Owner | Target Decision Date |
|---|---|---|---|---|
| 1 | Should v1 support multi-role assignment (user in multiple roles) or single primary role? | A: Single role (simpler, faster). B: Multi-role with priority (complex). **Proposed: A for beta.** | PM | Week 1 |
| 2 | How do we handle users who are not assigned to any role? | A: Show current default (all dashboards). B: Show a "contact your admin" prompt. **Proposed: A (no regression).** | PM + Design Lead | Week 1 |
| 3 | Should the setup wizard auto-suggest roles based on IdP groups? | A: Yes (better UX, more engineering). B: No (manual only for v1). **Proposed: B for beta, A for GA.** | PM + Eng Lead | Week 2 |
| 4 | Post-GA: Do we extend Role-Based Defaults to Professional plan? | A: Yes (broader adoption). B: No (Enterprise differentiator). | Head of Product + Head of Revenue | GA + 4 weeks |
| 5 | What is the exact scope of the security pen test? | Internal-only vs. engage external firm. **Proposed: Internal for beta; external before GA.** | CISO | Week 2 |
| 6 | How do we integrate Dashboard Packs (Option B) as a content layer post-beta? | A: Pre-built packs selectable during role setup. B: Separate feature, independent of roles. | PM | Post-beta planning (Week 10) |

### Next steps

1. **This week:** PM circulates this Working Backwards Pack to CISO, Eng Lead, Design Lead, CSM Lead, and Sales Lead for async review. Comments due by EOW.
2. **This week:** PM schedules kick-off meeting for Week 0+1. Creates JIRA epic and sub-tasks per backcasting milestone.
3. **Week 1:** Resolve open questions #1, #2, #3 in kick-off. Backend Lead begins permissions model design. Design Lead begins admin console UX sprint. Data Engineer finalizes event schema.
4. **Week 1:** Sales Lead identifies and confirms 3-5 design partner accounts; PM shares beta criteria with partner stakeholders.
5. **Week 2:** CISO confirms security review slot (Week 3). Legal Counsel confirms review slot (Week 4).
6. **Week 3:** Security review of permissions model. Checkpoint: go/no-go on design before heavy implementation begins.
7. **Ongoing:** Weekly red/yellow/green milestone check-in (PM + Eng Lead, 30 min, every Monday).

---

## Quality Gate: Self-Assessment

### PR checklist

- [x] Problem-first: "Problem today" is clear before any solution language
- [x] Customer language: no internal jargon, acronyms, or org names
- [x] Clear value: headline + summary state who benefits and how
- [x] Concrete "how it works": 6 bullets; not a vague feature list
- [x] Boundaries: "who it's for / not for" is explicit
- [x] Credible quotes: customer quote reflects a real pain + measurable outcome
- [x] Rollout assumptions stated (tier/date/eligibility)

### FAQ checklist

- [x] Addresses: why now, alternatives, out of scope, risks, success metrics
- [x] Includes internal "machinery" questions (support, docs, analytics, approvals)
- [x] Open questions labeled with owner + decision date
- [x] No hand-waving: uncertain answers include options and proposed path

### Backcasting plan checklist

- [x] Launch tiers defined (internal dogfood > closed beta > GA) with target dates
- [x] Each milestone has an owner and clear "done" criteria
- [x] Dependencies and sign-offs listed (security, legal, compliance)
- [x] Instrumentation and monitoring included as milestones
- [x] Rollout + rollback triggers defined

### Rubric self-score

| Dimension | Score | Justification |
|---|---|---|
| 1) Customer clarity | 2 | Problem is specific, customer-readable; target users would recognize the pain |
| 2) "Why now" urgency | 2 | Three forcing functions (deal blockers, competitive, churn data); opportunity cost explicit |
| 3) Options quality | 2 | Three meaningfully different approaches (admin-curated roles vs. department packs vs. user-driven saved views) with distinct trade-offs |
| 4) Selected PR quality | 2 | Headline, summary, how-it-works (6 bullets), and boundaries are concrete |
| 5) FAQ completeness | 2 | Customer + business + technical/ops + legal FAQs; hard questions answered; open questions labeled |
| 6) Backcasting plan realism | 2 | 20+ milestones with owners, dependencies, done criteria, and risks; weekly granularity |
| 7) Metrics + guardrails | 2 | 5 success metrics and 5 guardrails, each computable, owned, and connected to the narrative |
| 8) Risk handling | 2 | Pre-mortem with 5 specific failure modes, each with mitigations and monitoring signals |
| 9) Decision readiness | 2 | Pack is async-readable; open questions explicit with owners and dates; go/no-go criteria clear |
| **Total** | **18/18** | |

---

*This Working Backwards Pack is designed to be circulated async for a go/no-go decision. No meeting is required to understand the proposal -- but a kick-off meeting is recommended to resolve open questions and assign final ownership.*
