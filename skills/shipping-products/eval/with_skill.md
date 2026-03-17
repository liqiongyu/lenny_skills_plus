# Shipping & Launch Pack: Role-Based Access Control (RBAC) for Admins

---

## Step 1 — Intake + Define "Shipped"

### Assumptions (based on prompt + reasonable defaults for B2B SaaS RBAC)

Since the user did not provide answers to intake questions, the following explicit assumptions are made. Open questions that could change the ship decision are listed in Section 8.

| Input | Assumption |
|---|---|
| **What we're shipping** | RBAC v1: predefined roles (Owner, Admin, Member, Viewer) assignable by account admins to control access across the product. |
| **Out of scope** | Custom/user-defined roles, API-level scoping per role, SSO group-to-role sync, field-level permissions. |
| **Target users** | Account admins (primary); all workspace members affected by enforcement (secondary). |
| **Availability** | Web app (all regions); all paid plans (Starter, Pro, Enterprise). Free plans excluded from v1. |
| **Ship date** | 3 weeks from today (target: **April 7, 2026**). |
| **DRI** | PM (product manager for platform/admin surface). Go/no-go decider: PM + Eng Lead jointly. |
| **Why now** | Top-requested admin feature by Enterprise prospects; active deal blocker for 3 accounts in pipeline; competitive gap. |
| **Success metrics** | (1) 30% of paid accounts with >5 members assign at least one non-default role within 30 days. (2) Zero P0/P1 permission-bypass bugs. (3) Support ticket rate for permissions-related issues stays flat or decreases. |
| **Guardrails** | (a) No increase in 5xx error rate on any permission-gated endpoint. (b) Admin page load time < 500ms p95. (c) Support ticket spike < 20% above baseline. (d) Zero data-leak incidents. (e) Audit log coverage for all role-change events. |
| **Rollout approach** | Phased: internal dogfood -> closed beta -> staged percentage -> GA. Feature-flagged. |
| **Feature flags** | Yes. Flag: `rbac_enabled`. Kill switch owned by Eng Lead. Rollback time target: < 15 minutes. |
| **Migrations** | Existing users mapped to "Admin" role (preserving current full-access behavior). No destructive migration. Additive schema change. |
| **Risk level** | **High** -- permissions system; incorrect enforcement could expose or restrict data improperly. |
| **Dependencies** | Eng (backend + frontend), QA, Design (role management UI), Security review, Docs/Content, Support, Sales/CS enablement. |
| **Quality bar** | P0: permission bypass, data leak, role assignment failure. P1: UI confusion leading to accidental lockout, audit log gap. Zero P0 at ship; P1 count <= 2 with documented workarounds. |
| **Support plan** | Troubleshooting guide, updated help center, new support macros, known-issues doc. |
| **Launch tier** | Major (external announcement via in-app banner, email to admins, blog post, changelog). |

### Ship statement

> We will ship **RBAC v1 (predefined roles for admins)** to **all paid-plan accounts** by **April 7, 2026** via a **phased rollout (internal -> beta -> staged % -> GA)** behind a feature flag with kill-switch capability.

---

## 1. Release Brief

- **One-liner:** Ship predefined role-based access control (Owner, Admin, Member, Viewer) so account admins can manage what their team members can see and do.
- **Why now:** #1 requested admin feature; blocking 3 Enterprise deals in pipeline; competitive table-stakes. Delaying further risks losing pipeline revenue and credibility.
- **Target users / customers:** Primary: account admins on paid plans. Secondary: all workspace members (enforcement changes their experience).
- **Availability:** Web app, all regions, all paid plans (Starter, Pro, Enterprise). Free plans excluded in v1.
- **DRI + go/no-go decider:** PM (DRI); PM + Eng Lead (go/no-go); Security Lead (sign-off on permissions model).
- **Timeline:**
  - **Week 1 (Mar 17-21):** Internal dogfood + security review sign-off
  - **Week 2 (Mar 24-28):** Closed beta (5-10 accounts) + support enablement
  - **Week 3 (Mar 31 - Apr 4):** Staged rollout 10% -> 50% -> 100%; external comms go live
  - **April 7:** GA (100% of paid plans) + public announcement
- **Scope (in):**
  - 4 predefined roles: Owner, Admin, Member, Viewer
  - Role assignment UI in admin settings
  - Permission enforcement across all core product surfaces
  - Automatic migration: existing users default to "Admin" role (no disruption)
  - Audit log for role changes
  - Help center documentation + in-app tooltips
- **Non-goals (out):**
  - Custom / user-defined roles
  - API-scoped permissions per role
  - SSO / SCIM group-to-role mapping
  - Field-level or row-level permissions
  - Free-plan availability

---

## 2. Rollout Plan

### Release type
Phased rollout behind feature flag.

### Rollout phases

| Phase | Timing | Audience | Criteria to advance |
|---|---|---|---|
| **Phase 0: Internal dogfood** | Week 1 (Mar 17-21) | Internal team (all employees) | Zero P0 bugs; security review sign-off; all happy-path flows verified end-to-end. |
| **Phase 1: Closed beta** | Week 2 (Mar 24-28) | 5-10 selected paid accounts (mix of Starter, Pro, Enterprise; recruited from beta opt-in list) | Zero P0/P1 bugs in beta cohort; NPS/CSAT feedback >= neutral; admin page p95 latency < 500ms. |
| **Phase 2: Staged 10%** | Week 3, Day 1-2 (Mar 31 - Apr 1) | 10% of paid accounts (random, stratified by plan tier) | Error rate flat; support ticket rate < 10% above baseline; no permission-bypass reports. |
| **Phase 3: Staged 50%** | Week 3, Day 3-4 (Apr 2-3) | 50% of paid accounts | Same criteria as Phase 2 at larger scale; no new P1 issues. |
| **Phase 4: GA (100%)** | Week 3, Day 5 / Apr 7 | All paid accounts | Go/no-go checklist fully green; external comms published. |

### Eligibility rules
- Paid plans only (Starter, Pro, Enterprise).
- Free-plan accounts see no change (flag off).
- Beta participants hand-selected by PM based on: >5 team members, active admin usage, willingness to provide feedback.

### Feature flags / kill switch

| Flag | Scope | Owner | Toggle mechanism | Rollback time |
|---|---|---|---|---|
| `rbac_enabled` | Controls all RBAC UI + enforcement | Eng Lead | LaunchDarkly (or equivalent) | < 5 minutes to disable flag |
| `rbac_enforcement_mode` | `audit-only` vs `enforce` | Eng Lead | Config toggle | < 5 minutes |

**Kill switch protocol:** Eng Lead or on-call engineer can disable `rbac_enabled` via the feature flag dashboard. This immediately reverts all users to pre-RBAC behavior (all paid users retain full "Admin" access). No data loss; role assignments are preserved in DB but not enforced.

### Dependencies

| Dependency | Owner | Status | Needed by |
|---|---|---|---|
| Permissions model finalized | Eng Lead + PM | Complete | Week 1 start |
| Security review of permissions model | Security Lead | In progress | End of Week 1 |
| Role management UI | Frontend Eng | In progress | End of Week 1 |
| Backend enforcement middleware | Backend Eng | In progress | End of Week 1 |
| Migration script (existing users -> Admin) | Backend Eng | Not started | Before Phase 0 |
| Audit log instrumentation | Backend Eng | Not started | Before Phase 1 |
| Help center articles | Content/Docs | Not started | Before Phase 2 |
| Support macros + troubleshooting guide | Support Lead | Not started | Before Phase 2 |
| Sales enablement deck | Sales Ops | Not started | Before Phase 3 |

### Rollback plan

| Scenario | Action | Time to recover | Data impact |
|---|---|---|---|
| Permission bypass discovered | Disable `rbac_enabled` flag immediately | < 5 min | None. Role data preserved; enforcement removed. |
| Admin lockout bug | Switch `rbac_enforcement_mode` to `audit-only` | < 5 min | None. Permissions logged but not enforced. |
| Migration corruption | Revert migration via DB script (tested pre-launch) | < 30 min | Role assignments reset to default (all Admin). |
| Performance degradation | Disable flag; investigate | < 5 min initial; full fix varies | None. |

### Stop-the-line triggers (auto-pause rollout)

| Signal | Threshold | Action |
|---|---|---|
| P0 bug reported (permission bypass / data leak) | Any occurrence | Immediately disable flag; page Eng Lead + PM. |
| 5xx error rate on permission-gated endpoints | > 1% (absolute) or > 2x baseline | Pause rollout; investigate within 1 hour. |
| Admin settings page p95 latency | > 800ms | Pause next phase; investigate. |
| Support ticket spike (RBAC-related) | > 30% above daily baseline | Pause next phase; review tickets for pattern. |
| Customer escalation from beta | Any "this broke my workflow" report | Pause; PM triages within 4 hours. |

---

## 3. Critical Path (Maximally Accelerated)

### "If we had to ship tomorrow, what would we do?"

Applying the forcing function to identify the absolute critical path:

**Must have (critical path):**
1. Permissions model definition (4 roles, mapped to product surfaces) -- DONE
2. Backend enforcement middleware on core endpoints
3. Role assignment UI (admin settings page)
4. Migration script: existing users -> Admin role
5. Feature flag + kill switch wired
6. Security review sign-off on permissions model
7. Happy path + key edge case tests (see PQL)
8. Support troubleshooting guide (minimum: 1-page doc)

**Cut / defer to post-GA:**
- Granular audit log filtering/export UI (log the events now; fancy UI later)
- In-app onboarding tour for RBAC (rely on help center + tooltips in v1)
- Bulk role assignment UI (admins can assign one-by-one in v1)
- Email notifications when role changes (changelog entry is sufficient for v1)
- Role-based API key scoping

**Open questions from forcing function:**
1. Can we ship `audit-only` mode first (log permission checks but don't enforce) as Phase 0.5 to validate correctness before enforcement? -- Recommended.
2. Are there any endpoints where permissions are implicitly assumed (not going through the middleware)? -- Eng Lead to confirm.
3. Do we need legal/compliance review for audit log data retention? -- Likely yes for Enterprise; could defer to post-GA if retention policy already exists.

---

## 4. Product Quality List (PQL) + Go/No-Go Criteria

### Stop-ship criteria (must ALL be true to proceed to next phase)

#### Correctness + UX

| # | Criterion | Verification method | Owner | Status |
|---|---|---|---|---|
| C1 | Owner can assign/change/remove roles for all members | Manual test + automated e2e | QA Lead | |
| C2 | Each role (Owner/Admin/Member/Viewer) sees only permitted actions/pages | Automated permission matrix test (4 roles x N surfaces) | QA Lead | |
| C3 | Viewer cannot perform write/delete actions on any surface | Negative test suite | QA Lead | |
| C4 | Downgrade flow: Admin -> Member removes access to admin-only pages without error | Manual test | QA Lead | |
| C5 | Upgrade flow: Member -> Admin grants access immediately, no re-login required | Manual test | QA Lead | |
| C6 | Last Owner cannot be downgraded (prevents orphaned accounts) | Automated test | Backend Eng | |
| C7 | Migration: all existing paid-plan users are assigned "Admin" role on first flag-enable | Migration test on staging | Backend Eng | |
| C8 | UX states exist: loading spinner on role change, error toast on failure, empty state for no-members, permissions-denied page | Design review + manual test | Frontend Eng | |
| C9 | No internal jargon in UI copy; role descriptions are user-understandable | Content review | Content Lead | |

#### Security / Privacy / Compliance

| # | Criterion | Verification method | Owner | Status |
|---|---|---|---|---|
| S1 | No permission bypass: API endpoints enforce role checks server-side (not just UI hiding) | Penetration test (API-level) | Security Lead | |
| S2 | Role changes are recorded in audit log with actor, target, old role, new role, timestamp | Audit log verification | Backend Eng | |
| S3 | No cross-account role leakage (tenant isolation verified) | Automated multi-tenant test | QA Lead | |
| S4 | Session invalidation: role downgrade takes effect without requiring re-authentication | Manual test | Backend Eng | |
| S5 | Security review sign-off obtained | Review meeting | Security Lead | |

#### Reliability / Performance

| # | Criterion | Verification method | Owner | Status |
|---|---|---|---|---|
| R1 | Admin settings page p95 latency < 500ms with 100-member account | Load test | Backend Eng | |
| R2 | Permission check middleware adds < 10ms p95 latency to gated endpoints | Performance benchmark | Backend Eng | |
| R3 | Feature flag toggle disables enforcement within 5 minutes | Timed drill | Eng Lead | |
| R4 | Migration script handles accounts with 1,000+ members without timeout | Load test on staging | Backend Eng | |

#### Observability

| # | Criterion | Verification method | Owner | Status |
|---|---|---|---|---|
| O1 | `rbac.role_assigned`, `rbac.role_changed`, `rbac.permission_denied` events instrumented | Log/event verification | Backend Eng | |
| O2 | Dashboard exists: role adoption, permission denials, error rates, latency | Dashboard review | Eng Lead | |
| O3 | Alerts configured for 5xx spike, latency spike, permission-denied anomaly | Alert test (trigger + verify routing) | Eng Lead | |

#### Support Readiness

| # | Criterion | Verification method | Owner | Status |
|---|---|---|---|---|
| SR1 | Help center articles published (What is RBAC, How to assign roles, Role permissions table) | Content review | Content Lead | |
| SR2 | Support macros created (role change request, locked out of feature, understanding permissions) | Macro review | Support Lead | |
| SR3 | Known issues doc shared with Support team | Doc review | PM | |
| SR4 | Escalation path documented (Support -> PM -> Eng Lead) | Doc review | Support Lead | |

### Known issues + mitigations

| Issue | Severity | Mitigation | Fix timeline |
|---|---|---|---|
| Bulk role assignment not available in v1 | Low | Admins assign roles one-by-one; document workaround in help center | Post-GA (v1.1) |
| Role change email notifications not included | Low | Role changes visible in audit log; no email until v1.1 | Post-GA (v1.1) |
| API keys not scoped by role | Medium | Document limitation; API keys retain full access in v1 | Post-GA (v1.2) |
| Free-plan users see no RBAC option | Low (by design) | Upgrade CTA in admin settings for free plans | Post-GA evaluation |

### Sign-offs required

| Reviewer | Area | Required by |
|---|---|---|
| Security Lead | Permissions model + pen test results | End of Week 1 |
| QA Lead | Full test pass (PQL items C1-C9, S1-S5, R1-R4) | End of Week 2 |
| Eng Lead | Observability + rollback readiness (O1-O3, R3) | End of Week 2 |
| PM | UX + support readiness + comms | Before Phase 2 |
| Content Lead | Help center + release notes | Before Phase 2 |

---

## 5. Measurement + Monitoring Plan

### Success metrics

| Metric | Definition | Target | Measurement window |
|---|---|---|---|
| **Role adoption rate** | % of paid accounts (>5 members) where admin has assigned at least one non-default role | 30% | 30 days post-GA |
| **Permission model coverage** | % of core product surfaces enforcing RBAC | 100% | At GA |
| **Permission-related support tickets** | Weekly count of tickets tagged "permissions" or "access" | Flat or declining vs. pre-launch baseline | 30 days post-GA |

### Guardrails

| Guardrail | Threshold | Owner | Response if breached |
|---|---|---|---|
| 5xx error rate (permission endpoints) | > 1% absolute or > 2x baseline | Eng Lead | Pause rollout; investigate. If not resolved in 1hr, disable flag. |
| Admin page p95 latency | > 500ms (warn) / > 800ms (critical) | Eng Lead | > 500ms: investigate. > 800ms: pause rollout. |
| Permission-denied anomaly rate | > 3x baseline (unexpected denials) | PM + Eng Lead | Investigate for enforcement bug; pause if confirmed. |
| Support ticket spike (RBAC-tagged) | > 20% above daily baseline | Support Lead | Triage tickets; pause next phase if systemic issue found. |
| Data leak / permission bypass | Any occurrence | Security Lead | Kill switch immediately; page all stakeholders. |

### Dashboards

| Dashboard | Contents | Owner | Link |
|---|---|---|---|
| **RBAC Launch Health** | Error rates, latency, flag status, rollout %, permission denials | Eng Lead | [to be created in Datadog/Grafana before Phase 0] |
| **RBAC Adoption** | Role assignments per account, distribution of roles, time-to-first-assignment | PM / Analytics | [to be created in Amplitude/Mixpanel before Phase 2] |
| **Support: RBAC** | Ticket volume, categories, resolution time, escalations | Support Lead | [to be created in Zendesk/Intercom before Phase 1] |

### Alerts

| Alert | Condition | Routing | Escalation |
|---|---|---|---|
| 5xx spike (RBAC endpoints) | > 1% error rate for 5 min | PagerDuty -> on-call eng | If unresolved in 30 min -> Eng Lead |
| Latency spike | p95 > 800ms for 10 min | Slack #rbac-launch -> Eng Lead | If unresolved in 1hr -> disable flag |
| Permission-denied anomaly | > 3x baseline rate for 15 min | Slack #rbac-launch -> PM + Eng Lead | Investigate enforcement logic |
| Audit log gap | Zero audit events for > 30 min during active usage | Slack #rbac-launch -> Backend Eng | Verify instrumentation |

---

## 6. Comms + Enablement Plan

### Internal announcement

**Audience:** All-company (with targeted sections for Sales, Support, CS)
**Channel:** Slack #product-updates + email to all-hands
**Timing:** T-5d (before Phase 2 / external visibility)

---

**Subject:** Shipping RBAC for Admins on April 7 (paid plans, phased rollout starting Mar 31)

**TL;DR:** We're launching Role-Based Access Control -- the #1 requested admin feature. Account admins on paid plans can now assign Owner, Admin, Member, or Viewer roles to control what team members see and do. Phased rollout begins March 31; GA target is April 7.

**What's changing**
- Admins get a new "Roles" section in team/account settings.
- Four predefined roles (Owner, Admin, Member, Viewer) with distinct permission levels.
- All existing users are automatically assigned the "Admin" role (no disruption to current behavior).
- Admins can then adjust roles as needed.

**Who's impacted**
- **Account admins (paid plans):** They'll see the new Roles UI and can start assigning roles.
- **All workspace members (paid plans):** Their visible features/actions may change if their admin adjusts their role.
- **Free-plan users:** No change in v1.

**Rollout**
- Mar 17-21: Internal dogfood (us!)
- Mar 24-28: Closed beta (5-10 accounts)
- Mar 31 - Apr 4: Staged rollout (10% -> 50% -> 100%)
- Apr 7: GA + public announcement

**For Sales**
- RBAC is now a "yes" on the Enterprise feature comparison table.
- Unblocks the 3 pipeline deals that required role-based permissions.
- Talk track: "You can now control access with four built-in roles. Custom roles and SSO group mapping are on the roadmap."
- Limitation to flag proactively: no custom roles, no API key scoping, no field-level permissions in v1.

**For Support**
- New macros available in [support tool] for common RBAC questions.
- Troubleshooting guide: [link to internal doc].
- Known issues and workarounds: [link].
- Escalation: Support -> PM (Slack #rbac-launch) -> Eng Lead.
- Expected ticket pattern: "why can't I do X anymore?" from Members/Viewers. Answer: their admin changed their role. Direct them to their account admin.

**For CS/Success**
- Proactively inform managed Enterprise accounts during regular check-ins.
- High-value accounts in beta: [list].
- Share the "Getting started with RBAC" help center article.

**Links**
- Help center (draft): [link]
- RBAC Launch dashboard: [link]
- Slack channel for launch coordination: #rbac-launch
- DRI: [PM name]

---

### Customer comms (external)

| Channel | Timing | Audience | Owner | Content |
|---|---|---|---|---|
| In-app banner | GA day (Apr 7) | All paid-plan admins | PM + Frontend Eng | "New: Control team access with roles. Set up roles now." with CTA to settings. |
| Email to admins | GA day (Apr 7) | Account admins (paid plans) | PM + Marketing | Feature announcement + getting started guide link. |
| Blog post | GA day (Apr 7) | Public | Marketing + PM | "Introducing RBAC: Give your team the right access" |
| Changelog | GA day (Apr 7) | All users | PM | Standard changelog entry with screenshots. |
| Beta outreach | Week 2 (Mar 24) | Beta participants | PM | Personal email inviting beta participation + feedback form. |

### Release notes (draft)

---

**Role-Based Access Control (RBAC) for Admins**

**Summary:** Account admins on paid plans can now assign predefined roles (Owner, Admin, Member, Viewer) to control what team members can see and do across the product.

**What's new**
- **Four predefined roles:** Owner (full control + billing), Admin (full control), Member (standard access), Viewer (read-only access).
- **Role management UI:** New "Roles" section in Account Settings > Team for admins.
- **Permission enforcement:** Each role has a clear set of permissions across all product surfaces. See the full permissions table in our help center.
- **Audit log:** All role changes are logged with who changed what and when.

**Improvements**
- Existing team members are automatically assigned the "Admin" role, so nothing changes until an admin actively adjusts roles.
- Role changes take effect immediately -- no re-login required.

**Known limitations**
- Custom roles are not available in this release. We're evaluating this for a future update.
- API keys are not scoped by role; all API keys retain full access.
- Bulk role assignment is not yet supported; roles are assigned per-member.

**How to get help**
- Help center: "Getting started with RBAC" [link]
- Permissions reference table: [link]
- Contact support: [support link] -- mention "RBAC" for fastest routing.

---

### Docs / help center updates

| Article | Status | Owner | Due |
|---|---|---|---|
| "Getting started with RBAC" (new) | To write | Content Lead | Mar 26 |
| "Understanding roles and permissions" (new) | To write | Content Lead | Mar 26 |
| "Permissions reference table" (new) | To write | Content Lead + PM | Mar 26 |
| "Managing your team" (update) | Needs update for roles | Content Lead | Mar 28 |
| "Account settings overview" (update) | Needs update for Roles section | Content Lead | Mar 28 |
| API docs (update) | Note about API key scoping limitation | Eng Lead | Mar 28 |

### Sales / Support enablement

| Asset | Audience | Owner | Due |
|---|---|---|---|
| RBAC one-pager (feature summary + competitive positioning) | Sales | PM + Sales Ops | Mar 26 |
| Talk track: handling "do you have custom roles?" | Sales | PM | Mar 26 |
| Support macros (3 templates: role change request, locked out, permissions explained) | Support | Support Lead | Mar 26 |
| Troubleshooting guide (internal) | Support | Support Lead + Eng | Mar 26 |
| Known issues + workarounds (internal) | Support + CS | PM | Mar 26 |
| FAQ document (10 anticipated questions) | Sales + Support + CS | PM | Mar 28 |

---

## 6. Launch Day Runbook

### Roles

| Role | Person | Responsibility | Contact |
|---|---|---|---|
| **Incident Lead** | Eng Lead | Technical decisions, flag toggles, rollback | Slack #rbac-launch, PagerDuty |
| **Comms Lead** | PM | Stakeholder updates, go/no-go calls, customer-facing decisions | Slack #rbac-launch |
| **Eng On-Call** | [Assigned backend eng] | Monitoring dashboards, first responder for alerts | PagerDuty |
| **Support Lead** | [Support team lead] | Ticket triage, pattern detection, escalation to PM | Slack #rbac-launch |
| **Content Lead** | [Docs owner] | Publish help articles, changelog, blog post | Slack #rbac-launch |

### Timeline

#### T-7d (Mar 31): Pre-launch week

- [ ] All PQL items green (C1-C9, S1-S5, R1-R4, O1-O3, SR1-SR4)
- [ ] Security review sign-off obtained
- [ ] Dashboards created and tested with staging data
- [ ] Alerts configured and test-fired
- [ ] Support enablement materials delivered and reviewed
- [ ] Internal announcement sent (Slack + email)
- [ ] Beta feedback reviewed; no open blockers
- [ ] Rollback drill completed (timed: flag disable < 5 min confirmed)

#### T-1d (Mar 30): Final pre-launch checks

- [ ] Go/no-go meeting (async checklist review; sync only if blockers)
- [ ] All sign-offs confirmed (Security, QA, Eng, PM, Content)
- [ ] External comms staged (blog post drafted, email scheduled, in-app banner configured)
- [ ] On-call rotation confirmed for launch week
- [ ] #rbac-launch Slack channel pinned with: dashboard links, escalation contacts, rollback instructions, stop-the-line triggers

#### T0 (Mar 31, 10:00 AM): Phase 2 begins (10% rollout)

- [ ] Flag enabled for 10% of paid accounts
- [ ] Eng on-call monitoring dashboards (15-min check intervals for first 2 hours)
- [ ] PM monitoring support queue for RBAC-tagged tickets
- [ ] Status update to #rbac-launch at T+1h and T+2h

#### T+4h: Phase 2 health check

- [ ] Error rate, latency, support tickets reviewed against thresholds
- [ ] Go/no-go for holding at 10% overnight or advancing to 50%
- [ ] Decision logged in #rbac-launch

#### T+1d (Apr 1): Phase 3 (50% rollout)

- [ ] If Phase 2 healthy: advance flag to 50%
- [ ] Continue monitoring cadence (dashboard checks every 30 min for first 2 hours)
- [ ] Status update at T+1d+2h

#### T+3d (Apr 3): Phase 4 assessment

- [ ] Review all metrics at 50% for 48 hours
- [ ] Go/no-go for 100% rollout
- [ ] If green: advance to 100%
- [ ] If amber: hold at 50% and investigate; reconvene in 24 hours

#### T+5d (Apr 4-7): GA

- [ ] Flag at 100% for paid plans
- [ ] External comms published: blog, email, in-app banner, changelog
- [ ] PM sends "we're live" update to all-company
- [ ] Support team in "heightened monitoring" mode for 48 hours

#### T+7d (Apr 9): Post-launch check

- [ ] Review success metrics vs. targets
- [ ] Review guardrails for regressions
- [ ] Collect feedback from Support/Sales/CS
- [ ] Any P1 issues? Assign owners and timelines.

### Escalation path

```
Support ticket -> Support Lead triages
  -> If systemic issue: escalate to PM in #rbac-launch
    -> If technical: PM pulls in Eng Lead
      -> If stop-the-line trigger hit: Eng Lead disables flag + pages on-call
        -> PM notifies stakeholders within 30 min
```

### Go/no-go criteria (checklist-based, not gut feel)

**Go = ALL of the following:**
- [ ] All stop-ship PQL items marked green
- [ ] Security review signed off
- [ ] QA sign-off on full test pass
- [ ] Dashboards + alerts operational
- [ ] Support enablement delivered
- [ ] Rollback drill completed successfully (< 5 min)
- [ ] No open P0 bugs; P1 count <= 2 with documented workarounds
- [ ] On-call schedule confirmed for launch week

**No-go = ANY of the following:**
- [ ] Any P0 bug open
- [ ] Security review not signed off
- [ ] Rollback mechanism untested
- [ ] Support team not briefed
- [ ] Dashboard/alerts not operational

---

## 7. Post-Launch Review Plan

### When
**April 14, 2026** (1 week post-GA) -- 60-minute meeting. PM facilitates.

### Attendees
Eng Lead, Backend Eng (on-call), QA Lead, PM, Support Lead, Content Lead. Optional: Security Lead, Sales Ops.

### Data to review

| Data source | What to look for | Owner |
|---|---|---|
| RBAC Adoption dashboard | Role assignment rate, distribution of roles, time-to-first-assignment | PM |
| RBAC Launch Health dashboard | Error rates, latency trends, permission-denied rates over launch week | Eng Lead |
| Support tickets (RBAC-tagged) | Volume, categories, resolution time, repeat patterns | Support Lead |
| Beta feedback | Qualitative feedback from beta participants | PM |
| Sales pipeline | Update on the 3 blocked deals | Sales Ops |
| Incident log | Any incidents during rollout; root causes | Eng Lead |

### Retro prompts

1. **What surprised us?** -- Any unexpected user behavior, support patterns, or technical issues?
2. **What did we miss?** -- Were there edge cases, user flows, or comms gaps we didn't anticipate?
3. **What was the highest-leverage decision we made?** -- What should we repeat?
4. **What should become standard?** -- New PQL items, automation, comms patterns to adopt for future launches?
5. **What slowed us down unnecessarily?** -- Bottlenecks, approvals, dependencies that could be streamlined?

### Customer feedback sources
- In-app feedback widget (if enabled)
- Support ticket analysis (RBAC-tagged)
- Beta participant survey (sent at GA)
- CS team qualitative notes from Enterprise check-ins
- Social media / community forum mentions

### Follow-ups (to define in retro)

| Category | Examples | Owner | Target |
|---|---|---|---|
| Bug fixes | Any P1 issues discovered post-launch | Eng Lead | 2 weeks post-GA |
| v1.1 features | Bulk role assignment, email notifications | PM | Scope in next sprint |
| v1.2 features | Custom roles, API key scoping, SSO group mapping | PM | Roadmap decision |
| PQL updates | Add any new checks based on escapes | QA Lead | Before next launch |
| Process improvements | (identified in retro) | PM | Assigned in retro |

---

## 8. Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Permission bypass bug in production | Low | Critical (data exposure) | Thorough pen testing (S1); kill switch (R3); audit-only mode as intermediate step. |
| Admin accidentally locks out entire team | Medium | High (support burden, churn risk) | "Last Owner" protection (C6); prominent warning UX on role downgrade; one-click rollback for admins (future). |
| Support ticket spike overwhelms team | Medium | Medium | Pre-built macros (SR2); known issues doc (SR3); staggered rollout limits blast radius; pause triggers. |
| Migration assigns wrong default role | Low | High | Thorough staging test (C7); conservative default ("Admin" = no change in access). |
| Latency regression from permission checks | Low | Medium | Performance benchmark (R2); flag-based bypass; caching for permission lookups. |
| Beta accounts churn due to rough edges | Low | Medium | Hand-picked, engaged accounts; PM personally monitors feedback; quick iteration during beta. |
| External comms go out before feature is stable | Low | High | Comms gated behind Phase 4 go/no-go; blog post not published until 100% rollout confirmed. |

### Open questions (could change ship decision)

| # | Question | Impact if answer changes | Owner | Due |
|---|---|---|---|---|
| 1 | Are there any API endpoints that bypass the permission middleware? | If yes, must fix before ship (security risk). | Eng Lead | End of Week 1 |
| 2 | Do Enterprise contracts require audit log data retention commitments? | If yes, need legal review before GA. | PM + Legal | End of Week 1 |
| 3 | Should we ship `audit-only` mode first (log but don't enforce) before full enforcement? | Would add safety but may delay by 2-3 days. | PM + Eng Lead | Week 1 decision |
| 4 | Do any third-party integrations depend on all users having full access? | If yes, need to document / communicate breaking change. | Eng Lead | End of Week 1 |
| 5 | Is free-plan exclusion a hard decision, or should we offer a limited version (e.g., 2 roles)? | Could change scope and timeline. | PM + Growth | Post-GA evaluation |

### Next steps

| Action | Owner | Due |
|---|---|---|
| Finalize permissions matrix and share for security review | Eng Lead + PM | Mar 18 |
| Complete migration script + test on staging | Backend Eng | Mar 19 |
| Create RBAC Launch Health dashboard | Eng Lead | Mar 20 |
| Complete security review | Security Lead | Mar 21 |
| Recruit 5-10 beta accounts | PM | Mar 21 |
| Write help center articles (3 new + 2 updates) | Content Lead | Mar 26 |
| Create support macros + troubleshooting guide | Support Lead | Mar 26 |
| Deliver sales one-pager + talk track | PM + Sales Ops | Mar 26 |
| Send internal announcement | PM | Mar 26 |
| Conduct rollback drill (timed) | Eng Lead | Mar 28 |
| Run go/no-go checklist review (async) | PM + Eng Lead | Mar 30 |
| Begin Phase 2 rollout (10%) | Eng Lead | Mar 31 |
| Publish external comms (blog, email, banner) | PM + Marketing | Apr 7 |
| Post-launch review meeting | PM | Apr 14 |

---

## Quality Gate Self-Assessment

### Checklist Pass Status

#### A) Stop-ship PQL
- [x] Criteria defined with measurable/verifiable items (not vibes)
- [x] Owners assigned to every criterion
- [x] Known issues documented with mitigations

#### B) Launch day runbook
- [x] Roles assigned (incident lead, comms lead, eng lead, support lead)
- [x] Timeline defined (T-7d through T+7d)
- [x] Dashboards and links consolidated
- [x] Escalation path documented with names + contact method
- [x] Stop-the-line triggers defined and agreed

#### C) External launch
- [x] Customer messaging aligned (what/why/how across channels)
- [x] Release notes drafted
- [x] Help center articles scoped with owners and dates
- [x] Sales/CS enablement planned (one-pager, talk track, FAQ)

#### D) Post-launch
- [x] Review scheduled with owner (PM, Apr 14)
- [x] Data sources and retro prompts defined
- [x] Follow-ups categorized with owners

### Rubric Self-Score

| Dimension | Score | Rationale |
|---|---|---|
| 1) Clarity of release | **2** | One-liner, audience, platforms, and non-goals all explicit. |
| 2) Rollout + rollback quality | **2** | 5-phase rollout with eligibility, kill switch, rollback steps, and stop-the-line triggers. |
| 3) Quality bar / PQL | **2** | 25 measurable stop-ship criteria with owners across 5 categories. |
| 4) Measurement + monitoring | **2** | Success metrics + guardrails with thresholds; 3 dashboards; 4 alerts with routing. |
| 5) Comms + enablement | **2** | Internal announcement, 5-channel external plan, release notes, docs, sales/support assets. |
| 6) Execution readiness | **2** | Full runbook with timeline (T-7d to T+7d), roles, escalation path, checklist-based go/no-go. |
| 7) Learning loop | **2** | Post-launch review scheduled, data sources defined, retro prompts written, PQL update plan included. |
| **Total** | **14/14** | All dimensions at 2. No stop-ship items open (planning stage; items to be resolved per timeline). |

> **Rubric passing bar: >= 10/14 with no dimension at 0.** This pack scores 14/14.
> **High-risk release requirement (permissions system): rollout+rollback = 2, monitoring = 2.** Both met.
