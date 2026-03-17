# User Feedback Analysis Pack — Onboarding & Activation (B2B SaaS)

---

## 0) Context Snapshot

- **Product:** B2B SaaS platform (generalized; applicable to project management, CRM, analytics, or similar multi-seat tools)
- **Area/workflow in scope:** Onboarding + activation (from account creation through first value milestone)
- **Decision to support + deadline:** What to fix in the next 2 sprints (~4 weeks). Team needs a ranked list of onboarding/activation improvements with clear owners by sprint planning.
- **Time window:** Last 90 days
- **Sources included:** (1) Support tickets related to onboarding and activation (redacted excerpts), (2) Churn survey comments (post-cancellation or downgrade survey open-ends)
- **Sources excluded (and why):** Sales call notes (not provided), product analytics/funnels (quantitative; out of scope for this qualitative synthesis), app store/G2 reviews (not provided), internal beta feedback (not representative of production users)
- **Segments that matter:** SMB (1-50 seats, self-serve or low-touch) vs Mid-market (51-500 seats, sales-assisted with dedicated onboarding)
- **Constraints (PII/internal-only):** All excerpts are pre-redacted; no PII. Internal-only deliverable. No customer names, email addresses, or company identifiers.
- **Time box + confidence target:** Directional confidence sufficient for sprint-level decisions. Not seeking statistical significance; seeking pattern convergence across sources and segments.
- **Stakeholders/audience:** Product Manager (primary), Engineering Lead, Head of Customer Success
- **Assumptions / unknowns:**
  - Actual ticket and survey volumes are not provided; this analysis uses **synthesized representative data** based on common B2B SaaS onboarding patterns to demonstrate the full analysis framework. All "quotes" are illustrative composites, not real customer verbatims.
  - Activation definition assumed: user completes core setup (team invite + first workflow created + first integration connected) within 14 days.
  - SMB:Mid-market ratio assumed ~70:30 based on typical B2B SaaS distributions.

---

## 1) Source Inventory + Sampling Plan

| Source | What it contains | Time window | Volume (est.) | Sampling method | Segment coverage | Notes / access constraints |
|---|---|---|---:|---|---|---|
| Support tickets (onboarding-tagged) | Tickets categorized under onboarding, setup, getting started, activation, first-use | Last 90 days | ~420 tickets | Stratified: 50 SMB + 30 Mid-market (random within each) | SMB (~70%), Mid-market (~30%) | Redacted excerpts only; no internal test accounts included |
| Churn survey comments | Open-ended responses from cancellation/downgrade survey, filtered to mentions of onboarding/setup/getting-started | Last 90 days | ~85 responses | All responses mentioning onboarding/setup keywords reviewed; 60 coded in detail | SMB (~65%), Mid-market (~35%) | Self-selected sample (only users who filled out survey); skews toward users who cared enough to explain |

**Inclusions:**
- All tickets tagged "onboarding," "setup," "getting-started," "activation," "first-use," or containing those keywords in the first message
- All churn survey responses where the open-end mentions onboarding, setup, integration, getting started, or first week/month

**Exclusions:**
- Billing-only tickets (no onboarding signal)
- Tickets from internal/test accounts
- Churn survey responses that mention only pricing with no onboarding context
- Feature requests not related to onboarding flow (e.g., advanced reporting features)

**Bias acknowledgment:**
- Support tickets skew toward users who encountered blockers severe enough to write in; silent churners and users who self-resolved are underrepresented.
- Churn surveys skew toward users willing to provide a reason; "rage quitters" who cancel without comment are missing.
- Mid-market accounts may file fewer tickets per-issue because they have a dedicated CSM handling problems informally (underrepresented in ticket data).

---

## 2) Taxonomy + Codebook

### Themes (12 tags)

| Theme | Definition | Includes | Excludes | Example excerpt (redacted) |
|---|---|---|---|---|
| **T1: Team invite failures** | User cannot successfully invite team members or invitees cannot join | Email delivery failures, permission errors on invite, SSO conflicts during invite, invite link expiration | Post-onboarding team management (adding seats later) | "I sent invites to my team 3 days ago and none of them received the email." |
| **T2: Integration setup confusion** | User struggles to connect third-party tools during initial setup | Unclear OAuth flows, missing integration docs, wrong permissions, failed connections | Ongoing integration sync errors after successful setup | "I spent 45 minutes trying to connect [Tool] and kept getting a generic error." |
| **T3: First workflow / project setup friction** | User cannot figure out how to create their first meaningful artifact in the product | Empty state confusion, unclear templates, no guidance on first steps, overwhelming options | Advanced workflow customization by experienced users | "After signing up I stared at a blank screen and had no idea where to start." |
| **T4: Onboarding content gaps** | Missing, outdated, or unhelpful documentation/guides/tooltips during onboarding | Broken links, stale screenshots, missing steps, tutorials that don't match current UI | General knowledge base quality (non-onboarding articles) | "The getting started guide references a button that doesn't exist anymore." |
| **T5: Admin/permissions confusion** | Admin setup (roles, permissions, workspace config) is unclear or error-prone | Role assignment confusion, workspace vs project permissions, SSO/SCIM setup issues | Day-to-day permission changes by established admins | "I can't figure out how to make someone a project admin without giving them full workspace access." |
| **T6: Activation milestone unclear** | User doesn't understand what "success" looks like or what to do next | No progress indicators, no "you're set up" confirmation, unclear value proposition post-signup | Users who activated successfully but later churned for other reasons | "I completed the tutorial but I'm not sure if I'm actually set up correctly." |
| **T7: Performance / loading issues** | Slow load times, timeouts, or errors during onboarding steps | Slow initial workspace provisioning, import timeouts, laggy UI during setup | General performance issues unrelated to onboarding | "The import took over 20 minutes and then timed out. I had to start over." |
| **T8: Data import / migration pain** | Difficulty importing existing data from previous tools | CSV format errors, field mapping confusion, partial imports, no rollback | Manual data entry (not import-related) | "I exported from [Competitor] but half my fields didn't map correctly." |
| **T9: Mobile onboarding gaps** | Onboarding flow is incomplete, broken, or missing on mobile | Missing mobile setup steps, responsive layout issues, mobile-specific bugs | General mobile app feature requests | "I tried to finish setup on my phone but the integration page doesn't load on mobile." |
| **T10: Trial/plan confusion** | Uncertainty about trial limits, feature gating, or what happens at trial end during onboarding | Feature gates encountered during setup, unclear trial countdown, surprise limitations | Post-trial billing disputes (pricing, not onboarding) | "I hit a limit on users halfway through setting up my team and didn't know I was on a restricted trial." |
| **T11: SSO/security setup blockers** | SSO, SAML, or security configuration blocks team from starting | SAML misconfiguration, domain verification failures, MFA setup issues | Ongoing SSO maintenance | "Our IT team spent 3 hours trying to get SAML working and we still can't log in." |
| **T12: Time-to-value too long** | User perceives that onboarding takes too many steps or too much time to reach value | Too many required steps, mandatory fields that feel unnecessary, long setup wizards | Users who completed onboarding quickly but later churned | "By the time I finished all the setup steps I'd lost interest. It felt like homework." |

### Severity Scale

- **1 = Minor:** Annoyance; workaround exists; user self-resolves with minimal friction. Low churn risk.
- **2 = Moderate:** Slows onboarding meaningfully; some users need support help; adds days to activation timeline.
- **3 = Major:** Core onboarding step is impaired; high risk of user abandoning setup; significant support burden.
- **4 = Critical:** Complete blocker; user cannot proceed; data loss risk; likely to churn immediately.

### Root Cause Types

- **bug** — Software defect (error, crash, data corruption)
- **ux** — Confusing flow, missing affordance, poor information architecture
- **docs** — Missing, outdated, or unclear documentation/tooltips
- **expectation** — Mismatch between what user expected and what product does
- **integration** — Third-party API issue, auth flow problem, compatibility gap
- **infra** — Performance, scaling, or infrastructure limitation
- **other** — Does not fit above categories

### Tagging Rules

- Choose **one primary theme** per item. Use secondary themes only when a ticket clearly spans two distinct issues.
- If unsure, tag as `Needs review` and add a note.
- Severity should reflect the **impact on the user**, not the engineering effort to fix.
- Root cause should reflect the **most proximate cause** (e.g., if a bug causes confusion, root cause = bug, not UX).

---

## 3) Normalized Feedback Table

Below is a representative sample of 25 tagged items (from the full coded set of ~140 items). Real deployments should include the full table in a spreadsheet.

| item_id | source | date | segment | lifecycle_stage | verbatim_excerpt | primary_theme | secondary_themes | severity | root_cause_type | impact_notes |
|---|---|---|---|---|---|---|---|---:|---|---|
| ST-001 | support | 2026-01-15 | SMB | onboarding | "Sent invites to 5 team members, none received them. Checked spam, nothing. Tried resending 3 times." | T1: Team invite failures | -- | 4 | bug | Complete blocker; team cannot start using product |
| ST-002 | support | 2026-01-18 | Mid-market | onboarding | "Our IT admin configured SAML but users get a 'domain not verified' error. We've been going back and forth with support for a week." | T11: SSO/security setup blockers | T1 | 4 | integration | Entire company blocked from starting |
| ST-003 | support | 2026-01-22 | SMB | activation | "I connected [CRM Tool] but none of my contacts synced. The status says 'connected' but the data isn't there." | T2: Integration setup confusion | -- | 3 | bug | Core setup step appears complete but isn't; silent failure |
| ST-004 | support | 2026-02-01 | SMB | onboarding | "After signup I got dropped into an empty dashboard. No tutorial, no prompts. I literally didn't know what to click." | T3: First workflow setup friction | T6 | 3 | ux | New user has no path forward; high abandonment risk |
| ST-005 | support | 2026-02-03 | Mid-market | onboarding | "The getting started guide says to click 'New Project' in the sidebar but there is no sidebar on our plan. We have a top nav." | T4: Onboarding content gaps | -- | 2 | docs | User loses trust in documentation |
| ST-006 | support | 2026-02-05 | SMB | activation | "I tried to import our data from [Competitor]. The CSV upload kept failing with 'invalid format' but didn't tell me what was wrong." | T8: Data import/migration pain | -- | 3 | ux | User cannot bring existing data; blocks activation |
| ST-007 | support | 2026-02-08 | Mid-market | onboarding | "We need project-level admins but the only options are 'member' and 'workspace admin.' This is a dealbreaker for our compliance team." | T5: Admin/permissions confusion | -- | 3 | expectation | Feature gap perceived during onboarding; churn risk for compliance-sensitive orgs |
| ST-008 | support | 2026-02-10 | SMB | onboarding | "Integration page doesn't even load on my iPhone. Just a spinning wheel." | T9: Mobile onboarding gaps | T2 | 3 | bug | Mobile users cannot complete setup |
| ST-009 | support | 2026-02-12 | SMB | activation | "I finished the setup wizard and it just said 'Done!' but I don't feel done. What am I supposed to do now?" | T6: Activation milestone unclear | -- | 2 | ux | User doesn't know if they succeeded or what to do next |
| ST-010 | support | 2026-02-15 | Mid-market | onboarding | "We imported 12,000 records and it took 35 minutes, then failed at 80%. No way to resume, had to restart." | T8: Data import/migration pain | T7 | 4 | infra | Large data imports unreliable; blocks mid-market setup |
| ST-011 | support | 2026-02-18 | SMB | onboarding | "Didn't realize I was on a 5-user trial until I tried to invite my 6th team member. The error message just said 'limit reached.'" | T10: Trial/plan confusion | T1 | 3 | ux | Surprise limitation mid-setup; trust violation |
| ST-012 | support | 2026-02-20 | SMB | activation | "There are like 15 steps in the setup checklist. I gave up around step 8. Way too much before I can even see if this tool works for us." | T12: Time-to-value too long | -- | 3 | ux | User abandons before reaching value |
| ST-013 | support | 2026-02-22 | Mid-market | onboarding | "We can't figure out how to set up different permissions for different teams. The docs say it's possible but don't explain how." | T5: Admin/permissions confusion | T4 | 3 | docs | Mid-market need for granular permissions unmet by docs |
| ST-014 | support | 2026-02-25 | SMB | activation | "The template library is overwhelming. 50+ templates and no way to filter by use case. I just wanted a simple project board." | T3: First workflow setup friction | -- | 2 | ux | Paradox of choice slows activation |
| ST-015 | support | 2026-03-01 | SMB | onboarding | "Invite link expired after 24 hours. My teammate was on vacation and couldn't accept in time. Now I can't resend." | T1: Team invite failures | -- | 3 | ux | Overly aggressive expiration + no resend option |
| CS-001 | churn_survey | 2026-01-20 | SMB | -- | "Setup took way too long. By the time I figured things out, my trial was almost over and I hadn't gotten real value from it." | T12: Time-to-value too long | T10 | 3 | ux | Churned before activation |
| CS-002 | churn_survey | 2026-01-28 | Mid-market | -- | "We couldn't get SSO working and your support took 5 days to respond. We went with [Competitor] instead." | T11: SSO/security setup blockers | -- | 4 | integration | Lost deal due to setup blocker + slow support |
| CS-003 | churn_survey | 2026-02-05 | SMB | -- | "I never understood what I was supposed to do after signing up. The product felt empty and confusing." | T3: First workflow setup friction | T6 | 3 | ux | Churned without activating |
| CS-004 | churn_survey | 2026-02-12 | Mid-market | -- | "Data migration was a nightmare. Half our records were corrupted after import and there was no way to undo it." | T8: Data import/migration pain | -- | 4 | bug | Data corruption during import; trust destroyed |
| CS-005 | churn_survey | 2026-02-18 | SMB | -- | "Too many steps to get started. [Competitor] let me do my first task in 5 minutes. Yours took an hour." | T12: Time-to-value too long | -- | 3 | ux | Direct competitive comparison; lost to faster onboarding |
| CS-006 | churn_survey | 2026-02-25 | SMB | -- | "My team invites never worked. After 3 support emails I gave up. A collaboration tool where you can't collaborate." | T1: Team invite failures | -- | 4 | bug | Churned due to complete blocker |
| CS-007 | churn_survey | 2026-03-02 | Mid-market | -- | "The permissions model doesn't work for organizations with multiple departments. We need role-based access, not just admin/member." | T5: Admin/permissions confusion | -- | 3 | expectation | Mid-market deal lost on permissions gap |
| CS-008 | churn_survey | 2026-03-05 | SMB | -- | "I connected [Tool] but had to redo it 3 times because it kept disconnecting. Not a good first impression." | T2: Integration setup confusion | -- | 3 | bug | Repeated failures erode trust |
| CS-009 | churn_survey | 2026-03-08 | Mid-market | -- | "Your onboarding guide was clearly written for small teams. Nothing about enterprise setup, SSO, or bulk user provisioning." | T4: Onboarding content gaps | T11 | 2 | docs | Mid-market feels unsupported by docs |
| CS-010 | churn_survey | 2026-03-12 | SMB | -- | "Hit the trial user limit right when I was getting my team set up. Felt like a bait and switch." | T10: Trial/plan confusion | -- | 3 | ux | Trust violation at critical setup moment |

---

## 4) Themes & Evidence Report

### Theme 1 — Team Invite Failures (T1)

**Summary:** Users cannot successfully invite team members due to email delivery failures, link expiration issues, and lack of resend options. This is the single most damaging onboarding blocker because a collaboration tool that can't onboard a team is fundamentally broken.

**Who is impacted:** Primarily SMB (self-serve); they lack a CSM to escalate to. Mid-market affected less frequently because CSMs often handle invites manually.

**Frequency:** ~18% of coded support tickets; 3 of 10 churn survey mentions. Appears in both sources consistently.

**Severity/impact:** 3-4 (Major to Critical). When invites fail, the entire team is blocked. Users cannot experience collaborative value. Directly causes churn.

**Root causes (hypotheses):**
- Email deliverability issues (SPF/DKIM misconfiguration on outbound invite emails)
- Invite link expiration too aggressive (24 hours) with no resend mechanism
- SSO conflicts when invite recipient's domain has SSO enforced but invite flow doesn't account for it

**Representative evidence (redacted):**
- "Sent invites to 5 team members, none received them. Checked spam, nothing." (ST-001, SMB, Jan 2026)
- "Invite link expired after 24 hours. My teammate was on vacation." (ST-015, SMB, Mar 2026)
- "My team invites never worked. After 3 support emails I gave up." (CS-006, SMB, Feb 2026)

**Confidence:** High. Corroborated across both sources and multiple segments. Root cause (email deliverability) is a known engineering issue type that can be verified with logs.

---

### Theme 2 — First Workflow / Project Setup Friction (T3)

**Summary:** After completing account creation, users encounter an empty state with insufficient guidance. They don't know what to do first, the template library is overwhelming, and there is no clear path to creating a first meaningful artifact.

**Who is impacted:** Both segments, but SMB more severely (no CSM to guide them). New users in the first 0-3 days.

**Frequency:** ~15% of coded support tickets; 2 churn survey mentions. Second most common theme.

**Severity/impact:** 3 (Major). Users who can't start their first real task within the first session are at high risk of never returning.

**Root causes (hypotheses):**
- Empty state design lacks progressive disclosure (no default project, no guided first task)
- Template library has no use-case filtering or "recommended for you" logic
- Onboarding checklist exists but doesn't connect to actual product actions

**Representative evidence (redacted):**
- "After signup I got dropped into an empty dashboard. No tutorial, no prompts." (ST-004, SMB, Feb 2026)
- "The template library is overwhelming. 50+ templates and no way to filter by use case." (ST-014, SMB, Feb 2026)
- "I never understood what I was supposed to do after signing up." (CS-003, SMB, Feb 2026)

**Confidence:** High. Consistent pattern across sources. Empty-state problem is directly observable in the product.

---

### Theme 3 — Data Import / Migration Pain (T8)

**Summary:** Users attempting to migrate from competing tools encounter silent failures, unhelpful error messages, data corruption, and no ability to resume or roll back failed imports. This disproportionately affects Mid-market accounts with larger datasets.

**Who is impacted:** Both segments, but Mid-market severity is higher (larger datasets, more at stake). Critical during first week.

**Frequency:** ~12% of coded support tickets; 1 churn survey mention (but with extreme severity when it occurs).

**Severity/impact:** 3-4 (Major to Critical). Data corruption during import destroys trust immediately. Large imports timing out waste hours.

**Root causes (hypotheses):**
- CSV parser has poor error reporting (no line-level error detail)
- Import job has no resume/checkpoint mechanism for large datasets
- Field mapping UI doesn't validate or preview before committing
- No rollback mechanism if import produces bad data

**Representative evidence (redacted):**
- "The CSV upload kept failing with 'invalid format' but didn't tell me what was wrong." (ST-006, SMB, Feb 2026)
- "We imported 12,000 records and it took 35 minutes, then failed at 80%. No way to resume." (ST-010, Mid-market, Feb 2026)
- "Half our records were corrupted after import and there was no way to undo it." (CS-004, Mid-market, Feb 2026)

**Confidence:** High for the problem existence; Medium for root causes (need engineering investigation of import pipeline).

---

### Theme 4 — Time-to-Value Too Long (T12)

**Summary:** The onboarding process has too many required steps before users can experience core product value. Users compare unfavorably to competitors and churn before activating. Particularly acute for SMB users who expect self-serve, fast setup.

**Who is impacted:** Primarily SMB. Users in first 1-7 days.

**Frequency:** ~10% of coded support tickets; 3 churn survey mentions. High signal from churn surveys suggests this is a silent killer (users leave rather than file tickets).

**Severity/impact:** 3 (Major). Users who don't reach value in the first session have dramatically lower activation rates.

**Root causes (hypotheses):**
- Setup wizard requires too many mandatory steps before user can do "real work"
- No "skip for now" option on non-critical setup steps
- Activation milestone (team invite + first workflow + first integration) may be too ambitious as a single gate

**Representative evidence (redacted):**
- "There are like 15 steps in the setup checklist. I gave up around step 8." (ST-012, SMB, Feb 2026)
- "Setup took way too long. By the time I figured things out, my trial was almost over." (CS-001, SMB, Jan 2026)
- "Too many steps to get started. [Competitor] let me do my first task in 5 minutes." (CS-005, SMB, Feb 2026)

**Confidence:** Medium-High. Consistent across sources. Would benefit from quantitative funnel data to pinpoint exact drop-off steps.

---

### Theme 5 — Integration Setup Confusion (T2)

**Summary:** Connecting third-party tools during onboarding is confusing, fragile, and produces silent failures. Users encounter generic error messages, disconnections, and OAuth flows that don't clearly communicate what permissions are needed.

**Who is impacted:** Both segments. Users in first 1-7 days (integration is typically a setup step).

**Frequency:** ~10% of coded support tickets; 1 churn survey mention.

**Severity/impact:** 3 (Major). Integrations are often the activation trigger; if they fail, core value is blocked.

**Root causes (hypotheses):**
- OAuth error handling shows generic messages instead of actionable guidance
- Silent sync failures (status shows "connected" but data isn't flowing)
- No integration health check or diagnostic tool available to users
- Reconnection flow is unreliable

**Representative evidence (redacted):**
- "I connected [CRM Tool] but none of my contacts synced. The status says 'connected' but the data isn't there." (ST-003, SMB, Jan 2026)
- "I spent 45 minutes trying to connect [Tool] and kept getting a generic error." (ST example, composite)
- "I connected [Tool] but had to redo it 3 times because it kept disconnecting." (CS-008, SMB, Mar 2026)

**Confidence:** High for the problem; Medium for root causes (need engineering audit of integration error handling and monitoring).

---

### Theme 6 — SSO/Security Setup Blockers (T11)

**Summary:** Mid-market customers with SSO/SAML requirements encounter configuration failures that block their entire organization from accessing the product. Combined with slow support response times, this causes deal losses.

**Who is impacted:** Almost exclusively Mid-market. IT admins during initial setup (day 0-3).

**Frequency:** ~8% of coded support tickets; 2 churn survey mentions. Lower frequency but extremely high severity.

**Severity/impact:** 4 (Critical). Blocks entire organization. Often a competitive evaluation moment where delays mean lost deals.

**Root causes (hypotheses):**
- SAML configuration has insufficient validation/error messages
- Domain verification process is unclear
- No self-serve SSO diagnostic tool
- Support response time for SSO issues is too slow for evaluation timelines

**Representative evidence (redacted):**
- "Our IT admin configured SAML but users get a 'domain not verified' error. We've been going back and forth with support for a week." (ST-002, Mid-market, Jan 2026)
- "We couldn't get SSO working and your support took 5 days to respond. We went with [Competitor] instead." (CS-002, Mid-market, Jan 2026)

**Confidence:** High. Clear pattern. Each instance represents a potential lost deal.

---

### Theme 7 — Admin/Permissions Confusion (T5)

**Summary:** The permissions model (workspace admin vs. member binary) doesn't meet Mid-market needs for role-based access control. Documentation doesn't clearly explain what is possible.

**Who is impacted:** Mid-market primarily. Admins during initial workspace configuration.

**Frequency:** ~8% of coded support tickets; 1 churn survey mention.

**Severity/impact:** 3 (Major). Not a technical blocker but a dealbreaker for compliance-sensitive organizations.

**Root causes (hypotheses):**
- Permissions model designed for SMB (simple binary) doesn't scale to multi-department orgs
- Documentation doesn't explain the permissions model's boundaries clearly
- No migration path from "try it out" to "enterprise configuration"

**Representative evidence (redacted):**
- "We need project-level admins but the only options are 'member' and 'workspace admin.'" (ST-007, Mid-market, Feb 2026)
- "The permissions model doesn't work for organizations with multiple departments." (CS-007, Mid-market, Mar 2026)

**Confidence:** Medium-High. Consistent across both sources for Mid-market. Needs PM decision on whether to invest in RBAC vs. accept Mid-market friction.

---

### Theme 8 — Onboarding Content Gaps (T4)

**Summary:** Getting started guides, tooltips, and documentation are outdated, segment-agnostic, or missing entirely for key scenarios (enterprise setup, specific integration guides).

**Who is impacted:** Both segments. Mid-market particularly underserved (docs assume small-team setup).

**Frequency:** ~7% of coded support tickets; 1 churn survey mention.

**Severity/impact:** 2 (Moderate). Slows users down and erodes trust but rarely a complete blocker.

**Root causes (hypotheses):**
- Docs not updated when UI changes ship
- No segment-specific onboarding paths (SMB vs Mid-market)
- No ownership model for docs freshness

**Representative evidence (redacted):**
- "The getting started guide says to click 'New Project' in the sidebar but there is no sidebar on our plan." (ST-005, Mid-market, Feb 2026)
- "Your onboarding guide was clearly written for small teams. Nothing about enterprise setup." (CS-009, Mid-market, Mar 2026)

**Confidence:** Medium. Evidence is clear but small sample. Quick audit of current docs can validate.

---

### Theme 9 — Trial/Plan Confusion (T10)

**Summary:** Users encounter trial limitations (seat limits, feature gates) unexpectedly during setup, feeling blindsided at a critical moment.

**Who is impacted:** SMB primarily (self-serve trial flow).

**Frequency:** ~5% of coded support tickets; 1 churn survey mention.

**Severity/impact:** 3 (Major). Trust violation at a critical moment. Users describe it as "bait and switch."

**Root causes (hypotheses):**
- Trial limits not surfaced upfront during signup
- Error messages at limit don't explain the path forward (upgrade options, extending trial)
- Feature gates encountered during setup steps create confusion about what the product actually offers

**Representative evidence (redacted):**
- "Didn't realize I was on a 5-user trial until I tried to invite my 6th team member." (ST-011, SMB, Feb 2026)
- "Hit the trial user limit right when I was getting my team set up. Felt like a bait and switch." (CS-010, SMB, Mar 2026)

**Confidence:** Medium. Pattern is clear but sample is small. Can be validated with product analytics (how many trial users hit limits during onboarding).

---

### Segment-Level Summary

| Theme | SMB Impact | Mid-Market Impact | Overall Rank |
|---|---|---|---:|
| T1: Team invite failures | **High** (primary blocker) | Moderate (CSM workaround) | 1 |
| T3: First workflow setup friction | **High** (no guidance) | Moderate (CSM guides) | 2 |
| T8: Data import/migration pain | Moderate | **High** (larger datasets) | 3 |
| T12: Time-to-value too long | **High** (self-serve) | Moderate (assisted) | 4 |
| T2: Integration setup confusion | **High** | **High** | 5 |
| T11: SSO/security blockers | Low (rare) | **Critical** (deal-blocking) | 6 |
| T5: Admin/permissions confusion | Low | **High** (dealbreaker) | 7 |
| T4: Onboarding content gaps | Moderate | Moderate | 8 |
| T10: Trial/plan confusion | **High** (trust) | Low (sales-negotiated) | 9 |

---

## 5) Recommendations + Learning Plan

### Recommended Actions (Ranked for Next 2 Sprints)

| Rank | Action | Type | Theme(s) | Expected Impact | Owner (suggested) | Time Horizon | Evidence |
|---:|---|---|---|---|---|---|---|
| 1 | **Fix email deliverability for team invites** — Audit SPF/DKIM/DMARC configuration; add email delivery monitoring; implement retry logic | bug | T1 | High: Unblocks the #1 onboarding blocker. Expect 15-20% reduction in onboarding support tickets. | Eng (Platform) | Sprint 1 | ST-001, ST-015, CS-006 |
| 2 | **Add invite resend + extend link expiration to 7 days** — Allow one-click resend from the team page; extend expiration from 24h to 7d | ux | T1 | Medium-High: Eliminates the most common follow-up complaint about invites. | Eng (Product) | Sprint 1 | ST-015, CS-006 |
| 3 | **Redesign empty state with guided first task** — Replace blank dashboard with a "Create your first [artifact]" flow that pre-populates from a use-case question | ux | T3, T6 | High: Directly addresses the #2 theme. Expect measurable improvement in day-1 activation rate. | PM + Eng (Product) + Design | Sprint 1-2 | ST-004, ST-014, CS-003 |
| 4 | **Add actionable error messages to CSV import** — Show line-level errors, preview before commit, add field mapping validation | ux | T8 | Medium-High: Reduces import failure frustration. Critical for Mid-market conversion. | Eng (Product) | Sprint 1 | ST-006, ST-010, CS-004 |
| 5 | **Add import resume/checkpoint for large datasets** — Allow imports >5000 rows to resume from last checkpoint on failure | infra | T8 | High for Mid-market: Eliminates the most severe import failure (35-min imports lost). | Eng (Platform) | Sprint 2 | ST-010, CS-004 |
| 6 | **Implement integration health check + sync status** — Replace "connected" badge with actual sync status; surface errors with remediation steps | ux/bug | T2 | Medium-High: Eliminates silent integration failures. | Eng (Integrations) | Sprint 2 | ST-003, CS-008 |
| 7 | **Surface trial limits at signup and during onboarding** — Show seat count, trial duration, and feature access clearly in the setup flow; improve limit-reached error with upgrade/extend CTA | ux | T10 | Medium: Prevents trust-eroding surprise. Quick win. | PM + Eng (Growth) | Sprint 1 | ST-011, CS-010 |
| 8 | **Reduce mandatory onboarding steps** — Audit the setup checklist; make non-critical steps skippable ("do later"); let users reach core value faster | ux | T12 | High: Directly addresses competitive loss on time-to-value. Requires PM decision on which steps are truly required. | PM + Design | Sprint 2 | ST-012, CS-001, CS-005 |
| 9 | **Add SAML configuration validator + diagnostic tool** — Self-serve tool that tests SAML config and shows specific errors | ux | T11 | High for Mid-market: Reduces SSO setup from days to hours. Protects deals. | Eng (Platform) | Sprint 2 | ST-002, CS-002 |
| 10 | **Audit and update getting-started docs** — Fix stale screenshots, add Mid-market onboarding path, link to current UI | docs | T4 | Low-Medium: Reduces support tickets but not a primary churn driver. Quick win. | PM + Tech Writer | Sprint 1 | ST-005, CS-009 |

### Sprint Allocation Summary

**Sprint 1 (focus: remove blockers + quick wins):**
- Fix invite email deliverability (#1)
- Add invite resend + extend expiration (#2)
- Begin empty state redesign (#3 - start)
- Add CSV import error messages (#4)
- Surface trial limits at signup (#7)
- Audit and update getting-started docs (#10)

**Sprint 2 (focus: activation quality + mid-market):**
- Complete empty state redesign (#3 - finish)
- Add import resume/checkpoint (#5)
- Implement integration health check (#6)
- Reduce mandatory onboarding steps (#8)
- Add SAML configuration validator (#9)

### Open Questions (to de-risk)

1. **What is the actual invite email delivery rate?**
   - Why it matters: If delivery rate is 60% vs 95%, the fix priority and approach differ dramatically.
   - Fastest way to answer: Pull email delivery logs from the transactional email provider (e.g., SendGrid/Postmark) for the last 30 days.
   - Data needed: Delivery rate, bounce rate, spam classification rate for invite emails.

2. **Which onboarding steps have the highest drop-off?**
   - Why it matters: "Too many steps" feedback needs quantitative validation to know which steps to make skippable.
   - Fastest way to answer: Instrument the onboarding checklist funnel (if not already) and pull step-by-step completion rates.
   - Data needed: Step completion funnel, segmented by SMB vs Mid-market.

3. **How many Mid-market prospects abandon during SSO setup?**
   - Why it matters: If SSO blockers are losing 20%+ of Mid-market pipeline, the SAML validator should be prioritized higher.
   - Fastest way to answer: Ask Sales/CS to flag deals lost due to SSO issues in CRM; cross-reference with SSO-tagged support tickets.
   - Data needed: Count of deals lost or delayed due to SSO, average delay duration.

4. **Is the permissions model a product gap or a docs/messaging gap?**
   - Why it matters: Building RBAC is a multi-quarter investment; better docs/workarounds might address 80% of complaints.
   - Fastest way to answer: 5-6 targeted interviews with Mid-market churners who cited permissions.
   - Data needed: Specific permission scenarios users needed, willingness to use workarounds.

5. **What does the competitive onboarding experience actually look like?**
   - Why it matters: Multiple churners compared unfavorably to competitors on time-to-value.
   - Fastest way to answer: Competitive teardown of top 3 competitors' signup-to-first-value flow (30 min each).
   - Data needed: Step count, time to first value, required vs optional steps for each competitor.

---

## 6) Feedback Loop Plan

| Activity | Cadence | Owner(s) | Inputs | Output | Notes |
|---|---|---|---|---|---|
| Onboarding ticket triage + tagging | Daily | Support Lead + rotating engineer | New onboarding-tagged tickets | Updated feedback table with tags | Use codebook from this pack; flag severity 4 items immediately |
| Theme review + trend analysis | Bi-weekly (every sprint) | PM (Onboarding) + Support Lead | Tagged table + new churn survey data | Updated theme counts + new emerging themes | 30-min sync; compare to previous sprint |
| Engineering support rotation | Weekly (1 half-day) | Eng Lead (rotating) | Top 5 unresolved onboarding tickets | Direct fixes or bug tickets filed | Engineer spends 4 hours on triage; builds empathy + catches quick fixes |
| Stakeholder share-out | Monthly | PM (Onboarding) | Theme report + recommendation progress | Monthly VoC update (1-page summary) | Send to PM, Eng Lead, Head of CS, VP Product |
| Churn survey review | Monthly | PM + CS Lead | New churn survey responses | Updated churn reason analysis | Focus on onboarding-cited reasons; compare month-over-month |

### Where Insights Live

- **Primary repository:** Shared Notion/Confluence workspace under "Voice of Customer > Onboarding & Activation"
- **Tagged feedback table:** Google Sheet or Airtable (linked from Notion), updated weekly
- **Theme report:** Updated bi-weekly in Notion; versioned with date stamps
- **Recommendation tracker:** Linked to sprint board (Jira/Linear) via theme tags so progress is visible

### Update Triggers (review outside cadence)

- New product launch affecting onboarding flow
- Support ticket spike (>2x weekly average for onboarding tags)
- Churn rate increase >15% month-over-month for new accounts
- Competitor launch or pricing change that affects competitive positioning

### Engineering Participation Model

- **Weekly rotation:** One engineer spends a half-day triaging the top 5 onboarding support tickets. They either fix directly (if <2 hours) or file a detailed bug with reproduction steps.
- **Sprint demo:** Each sprint, the rotating engineer presents 1-2 "user pain stories" from their triage experience at sprint demo. This keeps the whole team connected to customer reality.
- **Escalation path:** Severity 4 items are escalated immediately to the Eng Lead via Slack, bypassing sprint cadence.

---

## 7) Risks / Open Questions / Next Steps

### Risks

1. **Synthesized data risk:** This analysis uses representative composite data, not actual customer verbatims. Before executing recommendations, validate the top 3 themes against real ticket data and churn surveys. The framework and codebook are ready to apply; the specific frequency counts need real-data confirmation.

2. **Source bias toward vocal users:** Support tickets and churn surveys both represent users who proactively communicated. Silent churners (signed up, never activated, never filed a ticket or survey) are invisible in this data. They may have entirely different blockers. Product analytics (activation funnel) are needed to fill this gap.

3. **Mid-market underrepresentation:** Mid-market users may file fewer tickets because CSMs handle issues informally. The true Mid-market pain may be worse than what appears in ticket data. Cross-reference with CS team's qualitative notes.

4. **Sprint capacity assumption:** The 2-sprint plan assumes engineering capacity to address 10 items across 2 sprints. If capacity is constrained, prioritize ranks 1-4 (invite fix, empty state redesign, import errors, trial limits).

5. **Permissions model is a product strategy question:** The admin/permissions gap (T5) is not a sprint-level fix. It requires a product strategy decision about Mid-market investment. Do not attempt to solve this in 2 sprints; instead, improve documentation and assess the business case.

### Open Questions

1. What is the actual email delivery rate for team invite emails? (Blocks validating the #1 recommendation.)
2. Which specific onboarding steps have the highest drop-off? (Needed before reducing mandatory steps.)
3. How many Mid-market deals are lost or delayed due to SSO setup issues? (Sizes the business impact of SAML validator.)
4. Is the permissions model a product gap or a docs gap for Mid-market? (Determines whether to build RBAC or improve workaround documentation.)
5. What do the top 3 competitors' onboarding flows look like in practice? (Needed to benchmark time-to-value improvements.)
6. Are there silent churners with different blockers not captured by tickets/surveys? (Requires activation funnel analysis.)

### Next Steps

1. **Immediate (this week):** Share this pack with PM, Eng Lead, and Head of CS. Validate the top 5 themes against real ticket/survey data. Adjust frequency counts and severity based on actual data.
2. **Sprint planning (next session):** Use the sprint allocation summary to scope Sprint 1 work. Pull email delivery logs and onboarding funnel data to answer open questions #1 and #2.
3. **Within 2 weeks:** Set up the feedback loop (daily tagging, bi-weekly review, engineering rotation). Create the shared feedback table using the schema from this pack.
4. **Within 4 weeks (end of Sprint 2):** Re-run theme analysis with 30 days of newly tagged data to measure whether fixes are reducing ticket volume and churn mentions for addressed themes.
5. **Within 6 weeks:** Conduct 5-6 targeted interviews with Mid-market churners who cited permissions (open question #4) and complete competitive onboarding teardown (open question #5).

---

## Quality Gate: Self-Assessment

### Checklist Results

**A) Scope + decision readiness**
- [x] Decision explicit and dated (what to fix in next 2 sprints)
- [x] In-scope and out-of-scope listed
- [x] Time window and sampling documented
- [x] PII constraints honored (all redacted)

**B) Data coverage + bias controls**
- [x] Source inventory with inclusions/exclusions
- [x] Sampling strategy documented (stratified by segment)
- [x] Loud-user bias acknowledged
- [x] Segment coverage included (SMB vs Mid-market)

**C) Taxonomy/codebook quality**
- [x] Clear definitions with includes/excludes/examples
- [x] Manageable tag set (12 themes)
- [x] Severity scale defined and applied
- [x] Tagging rules support inter-rater consistency

**D) Theme synthesis quality**
- [x] Themes in plain language (customer POV)
- [x] Representative evidence with source attribution
- [x] Quantification with sampling caveats
- [x] Root cause hypotheses separated from facts
- [x] Rejection/friction reasons captured

**E) Recommendations executable**
- [x] Each recommendation tied to theme and evidence
- [x] Time horizons and types specified
- [x] Quick wins included (invite resend, trial limits, docs audit)
- [x] Open questions with concrete answer plans

**F) Feedback loop + durability**
- [x] Cadence and owner model defined
- [x] Engineering participation defined (weekly rotation)
- [x] Storage/query plan exists
- [x] Risks / Open questions / Next steps included

### Rubric Self-Score

| Dimension | Score | Rationale |
|---|---:|---|
| 1) Decision clarity | 5 | Decision, deadline, scope, and success criteria are explicit |
| 2) Data coverage + sampling rigor | 3 | Multiple sources documented with sampling rationale; however, data is synthesized/representative, not real -- limitations clearly stated |
| 3) Taxonomy/codebook usability | 5 | Well-defined tags with includes/excludes/examples; severity scale; consistent tagging rules |
| 4) Theme quality + evidence traceability | 4 | Specific themes with multiple supporting items, quantified by frequency and severity, split by segment; confidence levels stated. Would be 5 with real data and larger sample. |
| 5) Actionability of recommendations | 5 | Ranked actions with owners, time horizons, sprint allocation, expected impact, and a learning plan for unknowns |
| 6) Durability + loop design | 5 | Clear operating model with cadence, owners, engineering rotation, storage plan, escalation path, and update triggers |
| **Total** | **27/30** | Exceeds target of 20/30. Data coverage score reflects synthesized data; all other dimensions are strong. |

**Note:** The data coverage score of 3 is appropriate given that this analysis uses synthesized representative data rather than actual customer verbatims. When re-run with real data, this dimension should score 4-5 if the sampling plan is followed.
