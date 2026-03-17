# Shipping & Launch Pack: Role-Based Access Control (RBAC) for Admins

**Feature:** Role-Based Access Control (RBAC) for Admin Users
**Target Ship Date:** 3 weeks from today
**Document Owner:** Product Manager
**Last Updated:** 2026-03-17

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Staged Rollout Plan](#2-staged-rollout-plan)
3. [Go/No-Go Criteria (Product Quality Launch Criteria)](#3-gono-go-criteria-pql)
4. [Support Enablement Plan](#4-support-enablement-plan)
5. [Internal Communications Plan](#5-internal-communications-plan)
6. [External Communications Plan](#6-external-communications-plan)
7. [Risk Register & Mitigations](#7-risk-register--mitigations)
8. [Key Contacts & RACI](#8-key-contacts--raci)

---

## 1. Executive Summary

We are launching Role-Based Access Control (RBAC) for admin users, enabling organizations to define granular permissions across their workspace. This feature allows admins to create custom roles (e.g., Billing Admin, User Manager, Viewer), assign them to team members, and enforce least-privilege access across the product.

**Why it matters:** RBAC is the #1 requested feature from Enterprise and Mid-Market accounts. It unblocks expansion deals, reduces security audit friction, and is a prerequisite for SOC 2 Type II and ISO 27001 compliance positioning.

**Scope of launch:**
- Custom role creation and management
- Pre-built default roles (Owner, Admin, Member, Viewer)
- Role assignment to individual users and groups
- Permission inheritance and override logic
- Audit log integration for role changes
- Admin dashboard for role/permission visibility

---

## 2. Staged Rollout Plan

### Phase 0: Internal Dogfood (Week 1, Days 1-3)

| Item | Detail |
|------|--------|
| **Audience** | Internal team only (all employees) |
| **Goal** | Validate core workflows, catch UX issues, stress-test edge cases |
| **Feature flag** | `rbac_enabled = internal_only` |
| **Success criteria** | Zero P0/P1 bugs; core flows (create role, assign role, enforce permission) work end-to-end |
| **Rollback** | Instant flag flip; revert to legacy "admin/member" binary model |

**Actions:**
- Engineering enables RBAC on internal workspace
- QA runs full regression suite against internal environment
- All PMs, designers, and engineers use RBAC for 48 hours minimum
- Bug bash scheduled for Day 2 afternoon
- Collect structured feedback via internal form

### Phase 1: Closed Beta (Week 1, Day 4 - Week 2, Day 3)

| Item | Detail |
|------|--------|
| **Audience** | 10-15 hand-picked accounts (mix of Enterprise, Mid-Market, power users) |
| **Goal** | Validate with real-world org structures, permission models, and workflows |
| **Feature flag** | `rbac_enabled = beta_cohort` |
| **Success criteria** | NPS >= 40 from beta cohort; <2% error rate on role operations; no data leakage incidents |
| **Rollback** | Per-account flag disable; 15-minute rollback window |

**Actions:**
- CSM outreach to beta candidates (pre-qualified accounts who requested RBAC)
- Provide beta onboarding guide and dedicated Slack channel
- Daily monitoring of error rates, latency, and permission enforcement accuracy
- Structured check-in calls at Day 3 and Day 6
- Collect feedback on: role creation UX, permission granularity, migration from old model

**Beta Account Selection Criteria:**
- Active Enterprise or Mid-Market plan
- Expressed interest in RBAC (feature request, sales conversation)
- Diverse org sizes (10-person team, 100-person team, 500+ person team)
- At least 2 accounts with complex permission needs (multi-department, external contractors)
- Willingness to provide feedback and participate in check-ins

### Phase 2: Limited GA (Week 2, Day 4 - Week 3, Day 2)

| Item | Detail |
|------|--------|
| **Audience** | All Enterprise plan customers |
| **Goal** | Validate at scale; confirm support readiness; finalize documentation |
| **Feature flag** | `rbac_enabled = enterprise_tier` |
| **Success criteria** | <0.5% support ticket increase related to RBAC; 95th percentile API latency <300ms; zero permission escalation bugs |
| **Rollback** | Tier-level flag disable; 30-minute rollback window |

**Actions:**
- Enable for all Enterprise accounts via automated flag rollout
- In-app announcement banner for Enterprise admins
- Monitor support ticket volume and categorization hourly for first 48 hours
- On-call engineering rotation specifically for RBAC issues
- CSM proactive outreach to top 20 Enterprise accounts

### Phase 3: General Availability (Week 3, Day 3 - Day 5)

| Item | Detail |
|------|--------|
| **Audience** | All customers on eligible plans (Business and above) |
| **Goal** | Full launch with marketing, PR, and sales enablement |
| **Feature flag** | `rbac_enabled = ga` (default on for eligible plans) |
| **Success criteria** | All PQL criteria met; marketing assets live; support team fully enabled |
| **Rollback** | Plan-level flag disable if critical issue discovered |

**Actions:**
- Enable for all Business+ accounts
- Publish blog post, changelog entry, and help center articles
- Send email announcement to all eligible account admins
- Sales team begins pitching RBAC in active deals
- Social media and community announcements
- Monitor for 72 hours post-GA before declaring launch complete

### Rollout Timeline Summary

```
Week 1:  [Internal Dogfood ][    Closed Beta                ]
Week 2:  [    Closed Beta   ][    Limited GA (Enterprise)    ]
Week 3:  [  Limited GA cont.][    General Availability       ]
```

---

## 3. Go/No-Go Criteria (PQL)

Each phase gate requires explicit sign-off before advancing. A single "No-Go" in any Critical category blocks progression.

### Critical Criteria (All must be "Go")

| # | Category | Criterion | Measurement | Threshold | Owner |
|---|----------|-----------|-------------|-----------|-------|
| C1 | **Stability** | P0/P1 bug count | Bug tracker | 0 open P0; <=2 open P1 with mitigations | Engineering Lead |
| C2 | **Security** | Permission enforcement accuracy | Automated test suite + manual audit | 100% — no permission escalation or leakage | Security Team |
| C3 | **Security** | Penetration test results | Third-party pen test report | All critical/high findings remediated | Security Team |
| C4 | **Performance** | API latency (role operations) | APM dashboard (p95) | < 300ms for role CRUD; < 500ms for permission checks | Engineering Lead |
| C5 | **Performance** | System load under RBAC enforcement | Load test results | < 5% increase in overall API latency; no degradation for non-RBAC endpoints | Engineering Lead |
| C6 | **Data Integrity** | Migration accuracy (legacy -> RBAC) | Migration validation script | 100% of existing permissions preserved; zero access regressions | Engineering Lead |
| C7 | **Compliance** | Audit log completeness | Log review | All role mutations logged with actor, timestamp, before/after state | Engineering Lead |

### Important Criteria (Must be "Go" or have documented mitigation)

| # | Category | Criterion | Measurement | Threshold | Owner |
|---|----------|-----------|-------------|-----------|-------|
| I1 | **UX Quality** | Beta NPS score | Post-beta survey | >= 40 | Product Manager |
| I2 | **UX Quality** | Task completion rate (create role, assign role) | Usability testing / analytics | >= 90% without support intervention | Product Designer |
| I3 | **Documentation** | Help center articles published | Content audit | All 8 planned articles live and reviewed | Technical Writer |
| I4 | **Support** | Support team enablement complete | Training completion tracker | 100% of Tier 1 and Tier 2 agents trained and certified | Support Lead |
| I5 | **Support** | Internal KB articles and macros ready | KB audit | All planned articles and 10+ macros published | Support Lead |
| I6 | **Monitoring** | Dashboards and alerts configured | Dashboard review | RBAC-specific dashboard live; alerts for error rate > 1%, latency > 500ms, permission failures | Engineering Lead |
| I7 | **Rollback** | Rollback procedure tested | Rollback drill | Successfully tested in staging; documented and reviewed | Engineering Lead |
| I8 | **Legal** | Terms of service / DPA updates | Legal review | Approved by Legal if RBAC changes data processing scope | Legal |

### Informational Criteria (Track but do not block)

| # | Category | Criterion | Measurement | Target |
|---|----------|-----------|-------------|--------|
| F1 | **Adoption** | % of Enterprise admins who create a custom role within 7 days | Product analytics | >= 25% |
| F2 | **Adoption** | Average number of custom roles per org | Product analytics | >= 3 |
| F3 | **Support** | RBAC-related ticket volume as % of total | Support analytics | < 3% of total volume |
| F4 | **Sales** | Pipeline influenced by RBAC | CRM data | >= $500K in first 30 days |

### Go/No-Go Decision Process

1. **Decision meeting:** Held 24 hours before each phase transition
2. **Attendees:** PM, Engineering Lead, Design Lead, Support Lead, Security Lead, GM/VP Product
3. **Format:** Each owner presents their criteria status (Go / No-Go / Go-with-mitigation)
4. **Decision authority:** GM/VP Product makes final call
5. **Documentation:** Decision and any conditions recorded in launch tracker

---

## 4. Support Enablement Plan

### 4.1 Training Program

**Timeline:** Complete by end of Week 2 (before Limited GA)

| Session | Audience | Duration | Format | Content |
|---------|----------|----------|--------|---------|
| RBAC Deep Dive | Tier 2 + Escalation | 90 min | Live workshop | Architecture, permission model, edge cases, troubleshooting |
| RBAC Overview | All Tier 1 | 45 min | Recorded + quiz | Feature overview, common scenarios, when to escalate |
| RBAC for CSMs | Customer Success | 60 min | Live workshop | Value positioning, onboarding guidance, migration support |
| RBAC Troubleshooting Lab | Tier 2 | 60 min | Hands-on lab | Sandbox environment, simulate common issues, practice resolution |

**Certification requirement:** All Tier 1 agents must pass a 15-question quiz (80% threshold) before handling RBAC tickets.

### 4.2 Knowledge Base & Macros

**Internal KB Articles (for agents):**

| Article | Content |
|---------|---------|
| RBAC Troubleshooting Decision Tree | Step-by-step flowchart for diagnosing permission issues |
| RBAC Permission Model Reference | Complete matrix of permissions by role type |
| RBAC Migration Guide (Internal) | How legacy admin/member permissions map to new roles |
| RBAC Known Issues & Workarounds | Living document updated during rollout |
| RBAC Escalation Criteria | When and how to escalate RBAC issues to Tier 2 / Engineering |

**Support Macros (10 pre-built):**

1. "How to create a custom role" — step-by-step walkthrough
2. "How to assign a role to a user" — with screenshots
3. "Understanding default roles" — explains Owner, Admin, Member, Viewer
4. "Permission denied error" — troubleshooting steps
5. "How to audit role changes" — navigating the audit log
6. "Migrating from legacy permissions" — what changed and what to expect
7. "RBAC not available on my plan" — plan eligibility explanation + upgrade path
8. "How to remove or modify a role" — including impact warnings
9. "Bulk role assignment" — for large teams
10. "RBAC and SSO/SCIM integration" — how roles interact with identity providers

### 4.3 Escalation Path

```
Tier 1 (General Support)
  |-- Can resolve: basic how-to, plan eligibility, UI navigation
  |-- Escalate if: permission enforcement bug, data access issue, migration problem
  |
Tier 2 (Technical Support)
  |-- Can resolve: permission debugging, audit log analysis, configuration issues
  |-- Escalate if: suspected security issue, data integrity concern, system-wide impact
  |
Engineering On-Call (RBAC-specific rotation during rollout)
  |-- Handles: bugs, security incidents, performance issues
  |-- Rotation: 24/7 for first 2 weeks post-GA, then folded into standard on-call
```

### 4.4 Support Monitoring During Rollout

- **Dedicated RBAC ticket tag** in support system for tracking and routing
- **Hourly ticket volume check** during first 48 hours of each phase
- **Daily support standup** during rollout weeks — review ticket trends, update KB, adjust macros
- **Escalation SLA:** Tier 1 to Tier 2 within 2 hours for RBAC issues during rollout; Engineering response within 1 hour for P1 escalations
- **Weekly support retrospective** during rollout to capture learnings

---

## 5. Internal Communications Plan

### 5.1 Timeline & Channels

| When | What | Channel | Audience | Owner |
|------|------|---------|----------|-------|
| Week 1, Day 1 | "RBAC Launch Kickoff" announcement | All-hands Slack channel | All employees | Product Manager |
| Week 1, Day 1 | Detailed launch plan shared | Confluence/Notion | Engineering, Product, Design, Support, Sales, CS | Product Manager |
| Week 1, Day 3 | Internal dogfood feedback summary | Engineering Slack channel | Engineering + Product | QA Lead |
| Week 2, Day 1 | Beta progress update | All-hands Slack channel | All employees | Product Manager |
| Week 2, Day 3 | Sales enablement session | Live meeting + recording | Sales + CS | Product Marketing |
| Week 2, Day 5 | Go/No-Go decision for Limited GA | Email + Slack | Leadership + launch team | GM/VP Product |
| Week 3, Day 1 | "RBAC is live for Enterprise" | All-hands Slack channel | All employees | Product Manager |
| Week 3, Day 3 | GA launch announcement | All-hands Slack + email | All employees | Product Marketing |
| Week 3, Day 5 | Launch retrospective | Meeting invite | Launch team | Product Manager |

### 5.2 Key Messages by Audience

**Engineering:**
- Migration path details and backward compatibility guarantees
- On-call rotation schedule and escalation procedures
- Performance benchmarks and monitoring dashboards
- Known technical debt and post-launch improvements roadmap

**Sales:**
- Competitive positioning: how our RBAC compares to alternatives
- Pricing impact: RBAC availability by plan tier
- Objection handling for common prospect concerns
- Demo script and sandbox environment access
- Target account list for proactive outreach

**Customer Success:**
- Migration support playbook for existing customers
- Proactive outreach templates for top accounts
- Common onboarding patterns and best practices
- Expansion opportunity identification criteria

**Support:**
- Training schedule and certification requirements
- New KB articles and macro availability
- Escalation path changes during rollout
- Ticket tagging and routing updates

**Marketing:**
- Launch date and embargo details
- Approved messaging and positioning
- Asset availability timeline (blog, email, social)
- Press/analyst briefing schedule if applicable

### 5.3 Internal FAQ

Prepare and distribute an internal FAQ covering:
- Why are we launching RBAC now?
- What plans include RBAC?
- How does RBAC interact with existing SSO/SCIM?
- What happens to existing admin/member permissions?
- What are the known limitations at launch?
- What is the post-launch roadmap for RBAC enhancements?
- How do customers request early access during beta?
- What is the rollback plan if something goes wrong?

---

## 6. External Communications Plan

### 6.1 Pre-Launch (Week 1-2)

| Asset | Channel | Audience | Timing | Owner |
|-------|---------|----------|--------|-------|
| Beta invitation emails | Email | Selected beta accounts | Week 1, Day 4 | CSM Team |
| Beta onboarding guide | Help center (unlisted) | Beta participants | Week 1, Day 4 | Technical Writer |
| "Coming soon" teaser | In-app banner (Enterprise) | Enterprise admins | Week 2, Day 1 | Product Marketing |
| Sales one-pager | PDF / Sales portal | Prospects in pipeline | Week 2, Day 3 | Product Marketing |

### 6.2 Launch Day (Week 3, Day 3)

| Asset | Channel | Audience | Owner |
|-------|---------|----------|-------|
| Blog post: "Introducing RBAC: Granular Access Control for Your Team" | Company blog | Public | Content Marketing |
| Changelog entry | In-app changelog | All users | Product Manager |
| Email announcement | Email | All eligible account admins | Email Marketing |
| In-app announcement | Modal / banner | Admins on eligible plans | Product Manager |
| Social media posts | Twitter/X, LinkedIn | Public / followers | Social Media Manager |
| Help center: 8 new articles | Help center | All users | Technical Writer |
| Video walkthrough (2-3 min) | YouTube + Help center | All users | Product Marketing |
| Community post | Community forum | Community members | Community Manager |

### 6.3 Post-Launch (Week 3, Day 4+)

| Asset | Channel | Audience | Timing | Owner |
|-------|---------|----------|--------|-------|
| Customer webinar: "Getting Started with RBAC" | Zoom / webinar platform | All customers | Week 4 | Customer Education |
| Case study outreach | Email to beta participants | Marketing pipeline | Week 4-5 | Content Marketing |
| "RBAC Best Practices" guide | Blog + Help center | All users | Week 5 | Technical Writer |
| Sales battlecard update | Internal sales portal | Sales team | Week 3, Day 5 | Product Marketing |

### 6.4 External Messaging Framework

**Headline:** Take control of who can do what across your workspace with Role-Based Access Control.

**Value propositions (prioritized):**
1. **Security & Compliance:** Enforce least-privilege access to meet SOC 2, ISO 27001, and internal audit requirements.
2. **Operational Efficiency:** Stop manually managing permissions one user at a time. Define a role once, apply it to your entire team.
3. **Flexibility:** Build custom roles that match your org structure, or start with our smart defaults.
4. **Visibility:** Full audit trail of every permission change, so you always know who has access to what.

**Key proof points:**
- Pre-built default roles get you started in minutes
- Custom roles support unlimited permission combinations
- Complete audit log for compliance reporting
- Seamless migration from existing permissions (zero downtime)
- Integrates with SSO and SCIM for automated provisioning

### 6.5 Help Center Articles Plan

| # | Article Title | Content Summary |
|---|--------------|-----------------|
| 1 | Introduction to RBAC | Overview of the feature, concepts, and terminology |
| 2 | Getting Started: Setting Up Roles | Step-by-step guide to creating your first custom role |
| 3 | Default Roles Explained | What Owner, Admin, Member, and Viewer can do |
| 4 | Creating and Managing Custom Roles | Detailed guide on custom role creation, editing, deletion |
| 5 | Assigning Roles to Users and Groups | How to apply roles, bulk assignment, role changes |
| 6 | Understanding the Permission Model | How permissions inherit, override, and interact |
| 7 | RBAC Audit Log | How to view and export role change history |
| 8 | Migrating to RBAC from Legacy Permissions | What changed, what was preserved, how to adjust |

---

## 7. Risk Register & Mitigations

| # | Risk | Likelihood | Impact | Mitigation | Contingency |
|---|------|-----------|--------|------------|-------------|
| R1 | Permission escalation bug allows unauthorized access | Low | Critical | Pen testing, automated permission verification suite, code review by security team | Immediate rollback to legacy model; security incident response procedure |
| R2 | Migration breaks existing user access | Medium | High | Dual-write period during migration; automated validation script comparing before/after access | Per-account rollback capability; manual permission restoration from backup |
| R3 | Performance degradation from permission checks on every API call | Medium | High | Permission caching layer; load testing at 3x expected traffic; async permission resolution for non-critical paths | Feature flag to disable granular checks and fall back to role-level caching |
| R4 | Support team overwhelmed by RBAC tickets | Medium | Medium | Comprehensive training; pre-built macros; proactive customer communication; self-service documentation | Surge staffing plan; engineering support for Tier 1 overflow; temporary in-app guided setup wizard |
| R5 | Low adoption due to complex UX | Low | Medium | Usability testing during beta; smart defaults; setup wizard for common patterns | Post-launch UX sprint; guided onboarding flow; CSM-assisted setup for top accounts |
| R6 | SSO/SCIM integration conflicts with RBAC role assignments | Medium | Medium | Integration testing with top 5 IdPs; documented behavior for conflicts | Manual override capability; IdP-side role mapping documentation |
| R7 | Customers lock themselves out by misconfiguring roles | Medium | Low | "Owner" role cannot be removed from last remaining owner; confirmation dialogs for destructive changes; recovery flow | Support-assisted account recovery; admin backdoor for emergency access restoration (audit-logged) |

---

## 8. Key Contacts & RACI

| Role | Person | Responsibilities |
|------|--------|-----------------|
| **Product Manager** (Responsible) | [Name] | Launch plan ownership, go/no-go facilitation, stakeholder coordination |
| **Engineering Lead** (Responsible) | [Name] | Technical delivery, performance, security, on-call rotation |
| **Design Lead** (Consulted) | [Name] | UX quality, usability testing, design QA |
| **QA Lead** (Responsible) | [Name] | Test planning, regression, migration validation |
| **Security Lead** (Accountable) | [Name] | Pen test coordination, security review sign-off |
| **Support Lead** (Responsible) | [Name] | Agent training, KB/macros, escalation path |
| **Product Marketing** (Responsible) | [Name] | External messaging, assets, sales enablement |
| **Technical Writer** (Responsible) | [Name] | Help center articles, beta guides, changelog |
| **CSM Lead** (Consulted) | [Name] | Beta recruitment, customer onboarding support |
| **GM / VP Product** (Accountable) | [Name] | Final go/no-go authority, resource allocation |

### RACI Matrix

| Activity | PM | Eng Lead | Design | QA | Security | Support | PMM | Tech Writer | CSM | GM |
|----------|:--:|:--------:|:------:|:--:|:--------:|:-------:|:---:|:-----------:|:---:|:--:|
| Rollout plan | R | C | C | C | C | C | I | I | I | A |
| Go/No-Go decision | R | R | C | R | R | R | I | I | I | A |
| Feature development | C | R | C | R | C | I | I | I | I | I |
| Security review | I | C | I | C | R | I | I | I | I | A |
| Support training | C | C | I | I | I | R | I | C | I | I |
| External comms | C | I | C | I | I | I | R | R | C | A |
| Sales enablement | C | I | I | I | I | I | R | I | C | I |
| Beta management | R | C | C | I | I | C | I | I | R | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## Appendix A: Launch Day Checklist

### T-24 Hours
- [ ] Final go/no-go meeting completed — decision: GO
- [ ] All PQL Critical criteria confirmed green
- [ ] All PQL Important criteria confirmed green or mitigated
- [ ] Rollback procedure reviewed with on-call engineer
- [ ] Support team certification complete (100%)
- [ ] All help center articles published and reviewed
- [ ] Blog post drafted, reviewed, and scheduled
- [ ] Email announcement drafted, reviewed, and scheduled
- [ ] In-app announcement configured and tested
- [ ] Social media posts drafted and scheduled
- [ ] Monitoring dashboards verified functional

### T-0 (Launch)
- [ ] Feature flag set to GA for all eligible plans
- [ ] In-app announcement activated
- [ ] Blog post published
- [ ] Changelog entry published
- [ ] Email sent to eligible account admins
- [ ] Social media posts published
- [ ] Community forum post published
- [ ] Video walkthrough published
- [ ] Engineering on-call confirmed and monitoring
- [ ] Support team on standby

### T+4 Hours
- [ ] Error rate check: within acceptable thresholds
- [ ] Support ticket volume check: no unexpected spikes
- [ ] Performance dashboard check: latency within bounds
- [ ] Social media sentiment check: no major concerns
- [ ] Beta customer feedback check: no regressions

### T+24 Hours
- [ ] Comprehensive metrics review
- [ ] Support ticket trend analysis
- [ ] Customer feedback summary compiled
- [ ] Any hotfixes needed identified and prioritized
- [ ] Internal status update sent to stakeholders

### T+72 Hours
- [ ] Launch declared complete (or issues documented)
- [ ] Post-launch metrics snapshot taken
- [ ] Retrospective scheduled
- [ ] Post-launch improvement backlog created

---

## Appendix B: Key Metrics Dashboard

Track these metrics daily during rollout, weekly post-GA:

**Adoption:**
- % of eligible accounts with RBAC active
- % of accounts with at least one custom role
- Average number of roles per account
- % of users with non-default role assigned

**Quality:**
- RBAC-related error rate (permission check failures / total checks)
- API latency (p50, p95, p99) for role operations
- API latency impact on non-RBAC endpoints
- Number of open P0/P1/P2 bugs

**Support:**
- RBAC ticket volume (absolute and as % of total)
- RBAC ticket resolution time (median and p90)
- Escalation rate for RBAC tickets
- Top 5 RBAC ticket categories

**Business:**
- Deals influenced by RBAC (pipeline value)
- Deals closed with RBAC as cited factor
- Expansion revenue attributed to RBAC
- Churn risk reduction for accounts requesting RBAC
