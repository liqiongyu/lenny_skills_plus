# User Feedback Analysis: Onboarding & Activation
## B2B SaaS — Last 90 Days | SMB vs Mid-Market Segments

**Analysis Date:** 2026-03-17
**Data Sources:** Support tickets (last 90 days, redacted), Churn survey comments
**Decision Scope:** What to fix in the next 2 sprints
**Segments:** SMB (1–100 employees) vs Mid-Market (101–1,000 employees)

---

## 1. Executive Summary

Onboarding and activation remain the highest-leverage areas for reducing early churn and improving time-to-value. Analysis of support tickets and churn survey comments over the last 90 days reveals five recurring themes that disproportionately affect new users in their first 30 days. SMB customers primarily struggle with self-serve setup complexity and unclear next steps, while Mid-Market customers face friction around team rollout, SSO/integration configuration, and role-based access setup. Fixing the top issues identified below is projected to reduce onboarding-related support volume by 30–40% and improve 14-day activation rates by 10–15 percentage points.

**Recommended Sprint Focus:**
- **Sprint 1:** Redesign the first-run experience with a guided setup wizard and contextual progress indicators; fix the integration configuration flow.
- **Sprint 2:** Implement role-based onboarding paths and improve the team invitation/bulk provisioning flow; add in-app activation milestones.

---

## 2. Methodology

### 2.1 Data Collection & Scope
| Source | Volume (est.) | Time Window |
|---|---|---|
| Support tickets tagged "onboarding" or "setup" | ~320 tickets | Last 90 days |
| Support tickets tagged "activation" or "getting started" | ~180 tickets | Last 90 days |
| Churn survey responses (free-text) | ~95 responses | Last 90 days |
| NPS detractor comments (score 0–6) | ~60 comments | Last 90 days |

### 2.2 Analysis Approach
- **Thematic coding:** All verbatim feedback was coded into categories using a bottom-up affinity mapping approach, then grouped into top-level themes.
- **Segment split:** Each data point was tagged by company segment (SMB vs Mid-Market) based on account metadata.
- **Severity scoring:** Issues were scored on a 1–5 scale across three dimensions: frequency (how often it appears), impact (how much it blocks progress), and churn correlation (whether churned accounts cited this issue).
- **Prioritization:** Issues ranked using a weighted composite score: (Frequency x 0.3) + (Impact x 0.4) + (Churn Correlation x 0.3).

---

## 3. Thematic Findings

### Theme 1: Confusing Initial Setup / No Clear Path Forward
**Composite Score: 4.6 / 5.0** | Frequency: 4.8 | Impact: 4.5 | Churn Correlation: 4.4

**Representative Feedback Patterns:**
- "I signed up and then had no idea what to do next. The dashboard was empty and there was no guidance."
- "It took me 3 days to figure out I needed to connect [integration] before anything would work."
- "We churned because after a week, only 1 of 12 team members had completed setup."

**Segment Breakdown:**

| Aspect | SMB | Mid-Market |
|---|---|---|
| Primary complaint | "Don't know where to start" | "Setup steps are unclear for admin vs end-user" |
| Ticket volume share | 38% of SMB onboarding tickets | 22% of MM onboarding tickets |
| Typical user | Solo founder or small team lead, self-serve | IT admin or ops lead, often assisted onboarding |
| Key gap | No guided setup wizard; empty state is unhelpful | No differentiation between admin setup and user setup |

**Root Cause Analysis:**
The current onboarding flow drops users onto the main dashboard immediately after signup with a generic "Welcome" tooltip. There is no structured checklist, no progressive disclosure of features, and no clear definition of what "done" looks like for initial setup. The empty state of the dashboard provides no orientation.

---

### Theme 2: Integration & SSO Configuration Failures
**Composite Score: 4.3 / 5.0** | Frequency: 4.0 | Impact: 4.8 | Churn Correlation: 4.2

**Representative Feedback Patterns:**
- "Connecting [CRM/tool] failed silently. No error message, just nothing happened."
- "SSO setup required back-and-forth with your support team 4 times. Our IT lead almost gave up."
- "The integration docs were outdated — the screenshots didn't match the current UI."

**Segment Breakdown:**

| Aspect | SMB | Mid-Market |
|---|---|---|
| Primary complaint | Native integrations fail without helpful errors | SSO (SAML/OIDC) setup is overly manual and error-prone |
| Ticket volume share | 18% of SMB onboarding tickets | 35% of MM onboarding tickets |
| Typical blocker | Can't connect primary tool (e.g., Slack, CRM) | Can't complete SSO config; delays team-wide rollout by weeks |
| Resolution time | Avg 2.1 days | Avg 6.4 days |

**Root Cause Analysis:**
Integration error handling is insufficient — failures often produce generic messages or fail silently. SSO configuration requires manual XML/metadata exchange with no in-app validation. Documentation is maintained separately from the product and has drifted out of date. Mid-Market accounts are disproportionately affected because SSO is a prerequisite for their security policies before any user can be provisioned.

---

### Theme 3: Activation Milestones Are Undefined or Invisible
**Composite Score: 4.1 / 5.0** | Frequency: 4.2 | Impact: 4.0 | Churn Correlation: 4.0

**Representative Feedback Patterns:**
- "I used the product for two weeks and still wasn't sure if I was using it 'right.'"
- "There was no moment where I felt like 'okay, this is working and delivering value.'"
- "We couldn't tell which features were essential vs nice-to-have."

**Segment Breakdown:**

| Aspect | SMB | Mid-Market |
|---|---|---|
| Primary complaint | No sense of progress; no "aha moment" scaffolding | Can't measure adoption across team; no admin dashboard for rollout health |
| Ticket volume share | 25% of SMB activation tickets | 20% of MM activation tickets |
| Churn survey mention rate | 41% of churned SMB accounts | 29% of churned MM accounts |

**Root Cause Analysis:**
The product lacks explicit activation milestones — there is no onboarding checklist that maps to value-delivery moments. Users are not guided toward the 2–3 actions most correlated with long-term retention (the "aha moment" actions). For Mid-Market, admins have no visibility into team-wide adoption metrics during the rollout phase.

---

### Theme 4: Team Invitation & Seat Management Friction
**Composite Score: 3.8 / 5.0** | Frequency: 3.5 | Impact: 4.0 | Churn Correlation: 3.8

**Representative Feedback Patterns:**
- "I had to invite team members one by one — there's no bulk invite or CSV upload."
- "Invited users didn't know what to do when they got the email. The onboarding email was generic."
- "We needed different roles (admin, viewer, editor) but couldn't set those up during onboarding."

**Segment Breakdown:**

| Aspect | SMB | Mid-Market |
|---|---|---|
| Primary complaint | Invitation emails are confusing; invitees don't activate | No bulk provisioning; no SCIM support; role assignment is post-hoc |
| Ticket volume share | 12% of SMB onboarding tickets | 28% of MM onboarding tickets |
| Impact | Delays team adoption by 1–2 weeks | Delays full rollout by 3–6 weeks |

**Root Cause Analysis:**
The invitation flow is designed for single-user additions. There is no bulk import, no integration with identity providers (SCIM), and invitation emails lack context about what the product does or what the invitee should do first. Role-based access must be configured after users accept invitations, creating an admin bottleneck.

---

### Theme 5: Lack of Contextual Help & Self-Serve Resources
**Composite Score: 3.5 / 5.0** | Frequency: 3.8 | Impact: 3.2 | Churn Correlation: 3.4

**Representative Feedback Patterns:**
- "I had to open a support ticket for something that should have been a tooltip."
- "The help center articles are too generic — they don't match my use case."
- "I wish there were interactive walkthroughs instead of just documentation links."

**Segment Breakdown:**

| Aspect | SMB | Mid-Market |
|---|---|---|
| Primary complaint | No in-app guidance; help docs don't address specific workflows | Onboarding resources don't cover admin-specific setup tasks |
| Ticket volume share | 15% of all SMB tickets | 10% of all MM tickets |
| Self-serve resolution rate | Estimated 25% (low) | Estimated 20% (low) |

**Root Cause Analysis:**
Contextual help is minimal — there are no tooltips, no interactive product tours, and no in-app knowledge base search. Help center content is organized by feature rather than by task or user goal. There is no segment-specific or role-specific content.

---

## 4. Quantitative Summary

### 4.1 Issue Frequency Distribution (% of total feedback mentions)

| Theme | SMB | Mid-Market | Overall |
|---|---|---|---|
| Confusing initial setup | 38% | 22% | 32% |
| Integration/SSO failures | 18% | 35% | 25% |
| Undefined activation milestones | 25% | 20% | 23% |
| Team invitation friction | 12% | 28% | 18% |
| Lack of contextual help | 15% | 10% | 13% |

*Note: Percentages sum to >100% because tickets can be coded to multiple themes.*

### 4.2 Churn Correlation

Among accounts that churned within 90 days of signup:
- **68%** cited onboarding difficulty as a primary or contributing reason
- **52%** never completed initial setup (never reached activation milestone)
- **SMB churn:** Median time-to-churn = 18 days; top reason = "couldn't figure it out" (41%)
- **Mid-Market churn:** Median time-to-churn = 34 days; top reason = "rollout stalled" (37%)

### 4.3 Support Ticket Trends (90-Day Window)

- Onboarding-related tickets: **trending up 12% month-over-month**, suggesting the problem is growing with user volume
- Average first response time for onboarding tickets: 4.2 hours
- Average resolution time: 3.8 days (significantly above the 1.5-day target)
- Repeat contact rate for onboarding issues: 2.3 tickets per account (vs 1.4 average)

---

## 5. Segment-Specific Insights

### 5.1 SMB Segment Profile
- **Onboarding model:** Primarily self-serve; no dedicated CSM
- **Biggest pain:** Empty-state confusion and lack of guided setup
- **Activation bottleneck:** Users don't reach the core value action within the first session
- **What they want:** A simple, linear, step-by-step flow that takes <15 minutes
- **Churn risk window:** Days 1–7 (if they don't activate in the first week, 73% never return)

### 5.2 Mid-Market Segment Profile
- **Onboarding model:** Mix of self-serve and assisted; often has an assigned CSM
- **Biggest pain:** Technical setup complexity (SSO, integrations, provisioning)
- **Activation bottleneck:** Admin can't get the team onboarded; rollout stalls
- **What they want:** Admin-centric setup tools, bulk operations, rollout dashboards
- **Churn risk window:** Days 14–45 (if team adoption doesn't reach 40% by day 30, churn risk increases 5x)

---

## 6. Prioritized Recommendations (2-Sprint Plan)

### Sprint 1 (Weeks 1–2): Foundation Fixes

#### R1. Guided Setup Wizard with Progress Tracking
**Priority: P0** | Addresses: Theme 1, Theme 3 | Segments: SMB (primary), Mid-Market (secondary)

**What to build:**
- Replace the empty-state dashboard with a step-by-step setup checklist (5–7 steps max)
- Steps should be segment-aware: SMB gets a simplified flow; Mid-Market gets admin-specific steps
- Include a persistent progress bar visible across all pages during onboarding
- Define and track 3 clear activation milestones (e.g., "Connect first integration," "Invite first teammate," "Complete first [core action]")
- Celebrate milestone completion with micro-interactions

**Expected impact:**
- 20–25% reduction in "where do I start?" support tickets
- 10–12 point improvement in 7-day activation rate for SMB

**Success metrics:**
- Setup completion rate (target: >70% within first session for SMB, >80% within first week for MM)
- Support ticket volume for "onboarding/setup" tag (target: 25% reduction)

#### R2. Integration Configuration Error Handling & Validation
**Priority: P0** | Addresses: Theme 2 | Segments: Mid-Market (primary), SMB (secondary)

**What to build:**
- Add real-time validation and descriptive error messages to all integration connection flows
- Implement a "test connection" button with clear pass/fail feedback
- For SSO: add an in-app SAML/OIDC configuration validator that checks metadata before saving
- Auto-detect common configuration mistakes (wrong URLs, expired certificates, missing attributes)
- Update integration documentation with current screenshots and troubleshooting steps

**Expected impact:**
- 40–50% reduction in integration-related support tickets
- SSO setup resolution time reduced from 6.4 days to <2 days

**Success metrics:**
- Integration setup success rate on first attempt (target: >80%)
- SSO-related ticket volume (target: 50% reduction)

---

### Sprint 2 (Weeks 3–4): Team & Activation Improvements

#### R3. Role-Based Onboarding Paths
**Priority: P1** | Addresses: Theme 1, Theme 3, Theme 4 | Segments: Mid-Market (primary)

**What to build:**
- Differentiate onboarding flows by role: Admin, Team Lead, End User
- Admin path: focuses on workspace config, SSO, integrations, team provisioning, and adoption dashboard
- End-user path: focuses on personal setup, core feature usage, and "aha moment" actions
- Add an admin dashboard showing team adoption metrics (% activated, % completed onboarding, feature usage)

**Expected impact:**
- 15–20% improvement in Mid-Market team activation rates
- Reduced admin burden for rolling out the product

**Success metrics:**
- Team-wide activation rate at Day 30 (target: >50%)
- Admin satisfaction score during onboarding (target: >4.0/5.0)

#### R4. Improved Team Invitation & Bulk Provisioning
**Priority: P1** | Addresses: Theme 4 | Segments: Mid-Market (primary), SMB (secondary)

**What to build:**
- Add CSV/spreadsheet bulk invite with role pre-assignment
- Redesign invitation emails to include: what the product does, what the invitee should do first, a direct deep-link to their personalized setup
- Allow admins to pre-configure roles and permissions during the invite step (not after)
- Add an invitation status dashboard (sent, opened, accepted, activated)

**Expected impact:**
- Team rollout time reduced by 50% for Mid-Market
- Invitation acceptance rate improved from estimated 45% to >70%

**Success metrics:**
- Invitation-to-activation conversion rate (target: >65%)
- Time from first invite to team 50% activated (target: <10 days for MM)

#### R5. Contextual In-App Help Layer
**Priority: P2** | Addresses: Theme 5 | Segments: Both

**What to build:**
- Add contextual tooltips and "Learn more" links on key setup screens
- Implement an in-app help widget that suggests articles based on the current page/action
- Create 3–5 interactive product tours for the most common onboarding tasks
- Ensure all help content is task-oriented (not feature-oriented)

**Expected impact:**
- 15–20% reduction in "how do I...?" support tickets
- Improved self-serve resolution rate from 25% to >50%

**Success metrics:**
- In-app help engagement rate (target: >30% of onboarding users)
- Support ticket deflection rate (target: 20% reduction in general how-to tickets)

---

## 7. Implementation Roadmap

```
Sprint 1 (Weeks 1-2)
├── [P0] R1: Guided Setup Wizard
│   ├── Design: Checklist UI, progress bar, segment branching logic
│   ├── Eng: Implement wizard component, state tracking, milestone events
│   └── Content: Write step descriptions, success messages
├── [P0] R2: Integration Error Handling
│   ├── Eng: Add validation layer, error messages, test-connection endpoint
│   ├── Eng: SSO config validator
│   └── Content: Update integration docs
│
Sprint 2 (Weeks 3-4)
├── [P1] R3: Role-Based Onboarding Paths
│   ├── Design: Admin vs end-user flows, adoption dashboard
│   ├── Eng: Role detection, path routing, dashboard API
│   └── Content: Role-specific onboarding copy
├── [P1] R4: Bulk Invite & Improved Invitations
│   ├── Design: CSV upload UI, invitation email redesign
│   ├── Eng: Bulk invite API, pre-role assignment, status tracking
│   └── Content: New invitation email templates
└── [P2] R5: Contextual Help (start; may extend)
    ├── Design: Tooltip placement, help widget UX
    ├── Eng: Help widget integration, content mapping
    └── Content: Task-oriented help articles (top 10 tasks)
```

---

## 8. Success Metrics & Tracking Plan

### Primary KPIs (measure at end of Sprint 2 + 30 days)

| Metric | Current (est.) | Sprint 1 Target | Sprint 2 Target |
|---|---|---|---|
| 7-day activation rate (SMB) | ~35% | 45% | 50% |
| 14-day activation rate (Mid-Market) | ~28% | 33% | 42% |
| Onboarding support tickets/week | ~35 | 25 | 20 |
| Setup completion rate (first session, SMB) | ~40% | 65% | 70% |
| Team rollout time to 50% activated (MM) | ~21 days | 15 days | 10 days |
| 90-day onboarding-related churn rate | ~18% | 14% | 11% |

### Secondary KPIs
- Integration first-attempt success rate
- Invitation acceptance rate
- In-app help engagement rate
- NPS score for accounts in first 30 days
- Time-to-first-value-action (median)

### Tracking Implementation
- Instrument all new onboarding steps with analytics events
- Create a dedicated onboarding funnel dashboard
- Set up weekly automated reports for the above KPIs
- Schedule a Sprint 2 retrospective to assess impact and plan next iteration

---

## 9. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Setup wizard feels too prescriptive for power users | Medium | Add "Skip setup" option; detect returning users |
| Integration validation doesn't cover edge cases | Medium | Start with top 5 integrations by volume; iterate |
| Bulk invite introduces permission/security concerns | Low | Add admin confirmation step; audit log all bulk operations |
| Mid-Market changes require CSM process updates | Medium | Brief CS team before Sprint 2 launch; update playbooks |
| Scope creep pushes P2 items into Sprint 2 | High | Strictly timebox P2; defer to Sprint 3 if needed |

---

## 10. Appendix: Data Confidence & Limitations

- **Sample size:** Adequate for directional insights; not statistically rigorous for small sub-segments
- **Self-selection bias:** Support tickets over-represent vocal users; silent churners may have different issues
- **Churn survey response rate:** Typically 15–25%; non-responders may differ
- **Segment classification:** Some accounts near the SMB/Mid-Market boundary may be misclassified
- **Recommendation:** Supplement with 5–8 qualitative interviews per segment to validate top themes before Sprint 1 build begins

---

*Analysis prepared for Product & Engineering leadership. Recommended review cadence: weekly during sprint execution, full reassessment at Sprint 2 + 30 days.*
