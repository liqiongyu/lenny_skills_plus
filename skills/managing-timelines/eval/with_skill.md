# Timeline Management Pack — Enterprise SSO Integration (AWS re:Invent Launch)

## 1) Deadline & commitment model

- **Date type:** Fixed external deadline
- **Why now:** AWS re:Invent conference on **December 3** is a public event with immovable dates. Sales and Marketing are planning demos, booth collateral, and customer conversations around enterprise SSO availability. Missing this date means waiting for the next comparable audience moment (likely Q2 next year).
- **Decision owner (date/scope trade-offs):** Product lead (you) for scope trades; VP Engineering or CTO for resource reallocation; VP Sales/CMO for external messaging changes.
- **Commitment ladder:**
  - **Commitment:** We will complete Discovery + Solutioning (security review initiated, technical design approved, SOC 2 gap analysis drafted) by **Week 3 (Oct 14)**.
  - **Forecast:** Based on current team shape and known dependencies, we expect a feature-complete, security-reviewed, SOC 2-documented enterprise SSO integration ready for launch by **December 3**. Confidence: **Medium**. This becomes a commitment after the Build phase code-complete milestone passes on November 15.
  - **Target:** GA announcement at AWS re:Invent main stage / booth demo on December 3.
- **Confidence:** **Medium** (M)
- **Top 3 risks:**
  1. Security review has not started and the timeline for external reviewers / internal security team availability is unknown.
  2. SOC 2 documentation updates require auditor coordination, which is outside the team's direct control.
  3. Two backend engineers must handle both IdP integration work and security remediation; any unplanned findings from the security review could consume significant capacity.
- **What is variable:** **Scope** is the primary trade lever. Date is fixed (external event). Resources are constrained (team is set). Quality/security are non-negotiable (enterprise customers, SOC 2). Therefore, scope is what we cut if we slip.

---

## 2) Phase plan (with decision gates)

| Phase | Start | End | Output(s) | Decision gate (what must be true to proceed) | Date type |
|---|---|---|---|---|---|
| **Discovery** | Sep 24 (Week 1) | Oct 4 (Week 2) | IdP requirements doc (SAML 2.0 / OIDC scope), security review request submitted, SOC 2 gap analysis started, UX wireframes for SSO config flow | Security review is scheduled with confirmed reviewer and timeline; IdP requirements are signed off by engineering lead | Commitment |
| **Solutioning** | Oct 7 (Week 3) | Oct 18 (Week 4) | Technical design doc approved, security review in progress with preliminary findings, SOC 2 change list finalized, UX designs complete and reviewed, dependency plan locked | Tech design is approved; no blocking security findings discovered; SOC 2 change list is achievable within timeline | Commitment |
| **Build** | Oct 21 (Week 5) | Nov 15 (Week 8) | Backend SSO service (SAML + OIDC), frontend admin config UI, security review remediation complete, SOC 2 docs updated, integration tests passing, staging deployment | Code complete; all P0 security findings resolved; SOC 2 documentation accepted by compliance; QA sign-off on staging | Forecast (becomes commitment after Week 4 gate) |
| **Launch** | Nov 18 (Week 9) | Dec 2 (Week 10) | Production deployment, customer beta validation, launch comms (blog, docs, Sales enablement), re:Invent demo ready, rollback plan tested, monitoring + alerting live | Go/no-go: production stable for 48+ hrs with beta customers; no P0/P1 bugs open; Sales/Marketing collateral approved | Forecast |

**Next commitment date (re-forecast checkpoint):** **October 18 (end of Week 4 / Solutioning gate).** At this point we will have security review preliminary results, a locked tech design, and SOC 2 change list -- enough information to convert the Build/Launch forecast into a commitment or escalate.

---

## 3) Milestone tracker + RAG

### RAG definitions

- **Green:** On track; no decisions needed; milestone will be met within planned dates.
- **Yellow (Amber):** Risk is emerging that could cause a 3+ day slip on any milestone; a decision or assist is needed within 1 week to stay on track. Weekly review must include a proposed resolution.
- **Red:** Cannot meet the committed/forecasted date without a scope cut, resource change, or date move. Requires immediate escalation to the decision owner within 24 hours with options.

### Milestone tracker

| # | Milestone | Deliverable | Owner | Target date | Confidence | RAG | Dependencies | Notes / next decision |
|---|---|---|---|---|---|---|---|---|
| M1 | IdP requirements locked | Requirements doc (SAML 2.0 + OIDC support matrix) | Backend Eng Lead | Oct 2 | H | Green | Customer interviews (Sales input) | Sales to provide top-5 enterprise customer IdP requirements by Sep 27 |
| M2 | Security review scheduled + kicked off | Confirmed reviewer, scope doc submitted, review in progress | Product Lead (you) | Oct 4 | M | **Yellow** | Security team / external reviewer availability | **Start immediately** -- this is the longest-lead dependency. Escalate if not scheduled by Sep 27. |
| M3 | UX designs complete | Admin SSO config screens, error states, onboarding flow | Designer | Oct 14 | H | Green | IdP requirements (M1) | Designer can start wireframes in parallel with requirements finalization |
| M4 | Technical design approved | Architecture doc covering auth flows, token management, session handling, multi-tenant isolation | Backend Eng Lead | Oct 11 | H | Green | IdP requirements (M1) | Include security reviewer in design review for early feedback |
| M5 | SOC 2 gap analysis + change list finalized | List of documentation, policy, and control changes needed | Product Lead | Oct 18 | M | Yellow | Compliance/auditor input | Confirm auditor availability for review cycle by Oct 4 |
| M6 | Security review preliminary findings delivered | Written report of findings + severity ratings | Security Reviewer | Oct 25 | M | Yellow | Security review start (M2) | If findings are P0, triggers immediate scope/timeline reassessment |
| M7 | Backend SSO service code complete | SAML 2.0 + OIDC authentication, provisioning (SCIM if in scope), session management | Backend Eng 1 + 2 | Nov 8 | M | Green | Tech design (M4), security findings (M6) | Two backend engineers pair on core auth; split SAML vs OIDC tracks |
| M8 | Frontend admin UI code complete | SSO configuration, connection testing, status dashboard | Frontend Eng | Nov 8 | H | Green | UX designs (M3), backend API contracts (M4) | Can start building against API contracts by Week 5 |
| M9 | Security remediation complete | All P0/P1 findings resolved, re-verification passed | Backend Eng Lead | Nov 12 | M | Yellow | Security findings (M6) | Buffer built in; if findings are minor, this completes early |
| M10 | SOC 2 documentation updated + accepted | Updated policies, control descriptions, evidence artifacts | Product Lead | Nov 15 | M | Yellow | SOC 2 change list (M5), auditor review cycle | Auditor turnaround time is the risk; submit drafts by Nov 1 |
| M11 | Integration testing + staging deployment | End-to-end tests passing (Okta, Azure AD, Google Workspace), staging env live | Backend Eng 2 + Frontend Eng | Nov 15 | M | Green | Code complete (M7, M8) | Test against at least 3 IdPs |
| M12 | Beta customer validation | 2-3 enterprise customers successfully configure SSO in staging/production | Product Lead + Sales | Nov 22 | M | Green | Staging (M11), customer recruitment (Sales) | Recruit beta customers by Nov 1 |
| M13 | Launch readiness | Production deployed, monitoring live, rollback tested, docs published, Sales enablement complete | Full team | Nov 29 | M | Green | Beta validation (M12), SOC 2 (M10) | Go/no-go decision on Nov 29 |
| M14 | AWS re:Invent launch | Live demo, booth materials, blog post, customer-facing docs | Product Lead + Marketing | Dec 3 | M | Green | Launch readiness (M13) | Marketing collateral must be finalized by Nov 25 |

---

## 4) Governance cadence

- **Update cadence:** Weekly (every Monday)
- **Forum(s):**
  - **Weekly project review** (30 min, Mondays): Core team + Product Lead. In-person or video.
  - **Async Slack update** (Fridays): Summary posted to #enterprise-sso-launch channel for broader stakeholders.
  - **Exec briefing** (biweekly, or immediately on Red): Product Lead to VP Eng / CTO.

### Weekly review agenda (30 min)

1. **RAG review** (10 min): Walk each milestone -- what is Yellow/Red? What changed since last week?
2. **Decisions needed** (10 min): List open decisions with owner + deadline. Make decisions in the room or assign a decision date.
3. **Scope changes + trades** (5 min): Any new requests? Apply "trade, don't add" rule. Log trades.
4. **Next week plan** (5 min): Top 3 priorities for the coming week; any blockers to pre-clear.

### Escalation triggers

| Trigger | Status | Action |
|---|---|---|
| Security review not scheduled by Sep 27 | **Red** | Escalate to VP Eng to source internal or external reviewer immediately |
| Security review findings include any P0 (critical vulnerability) | **Red** | Reassess scope; escalate to CTO for resource/timeline decision within 48 hours |
| Any milestone slips 3+ business days | **Yellow** | Propose mitigation at next weekly review; identify scope trade from cut list |
| Any milestone slips 5+ business days | **Red** | Escalate to decision owner within 24 hours with 3 options (cut scope / add resources / move date) |
| SOC 2 auditor is unavailable for review before Nov 15 | **Red** | Escalate to compliance lead; explore interim documentation approach |
| Fewer than 2 beta customers recruited by Nov 8 | **Yellow** | Sales leadership to intervene on customer recruitment |
| Code complete (M7/M8) not achieved by Nov 12 | **Red** | Trigger scope cut: drop SCIM provisioning or one IdP; compress QA |

### Decision log

| Date | Decision | Decision owner | Context / rationale | Follow-ups (owner/date) |
|---|---|---|---|---|
| Sep 24 | Treat Dec 3 as fixed external deadline; scope is the trade variable | Product Lead | AWS re:Invent is immovable; Sales/Marketing commitments already in motion | Communicate commitment model to all stakeholders (Product Lead / Sep 27) |
| Sep 24 | Security review must start by Oct 4 or escalate | Product Lead | Longest-lead dependency; blocking Build phase confidence | Schedule review (Product Lead / Sep 27) |

---

## 5) Scope & change-control plan

### Non-goals (explicitly out of scope)

- Custom/proprietary IdP integrations (only SAML 2.0 and OIDC standard protocols)
- Self-serve SSO configuration for non-enterprise tiers
- Migration tooling for existing customers switching auth methods
- SSO for mobile native apps (web only for V1)
- Directory sync beyond basic SCIM provisioning (if SCIM is even in scope)

### Cut list (pre-approved trade-offs, ordered by priority)

**Cut first (lowest user impact):**
1. **SCIM provisioning (auto user sync):** Manual user invite remains available. Saves ~1 week backend effort. Cut if any milestone slips 5+ days.
2. **Google Workspace IdP support:** Launch with Okta + Azure AD only (covers ~80% of enterprise SSO market). Add Google Workspace in fast-follow (January). Saves ~3 days.
3. **SSO status dashboard in admin UI:** Replace with a simple "connection active/inactive" indicator. Saves ~2 days frontend effort.

**Cut next (moderate impact, requires stakeholder sign-off):**
4. **OIDC support:** Launch with SAML 2.0 only. Covers the majority of enterprise customers but limits some modern IdP setups. Saves ~1 week backend effort.
5. **Polished onboarding wizard:** Replace with documentation-guided setup (step-by-step docs instead of in-app wizard). Saves ~1 week designer + frontend effort.

**Never cut (non-negotiables):**
- SAML 2.0 authentication (core SSO flow)
- Security review completion and P0/P1 remediation
- SOC 2 documentation updates (contractual requirement for enterprise customers)
- Basic admin configuration UI (must be able to set up SSO without engineering assistance)
- Okta + Azure AD support (minimum viable IdP coverage)
- Rollback capability and production monitoring

### Freeze points

| Freeze | Date | What it means |
|---|---|---|
| **Scope freeze** | Oct 18 (end of Solutioning) | No new features added after this date. Any new request must go through change control with an explicit trade. |
| **Code freeze** | Nov 15 (end of Build) | No new code except P0 bug fixes and security remediations. All changes require Backend Eng Lead approval. |
| **Launch readiness freeze** | Nov 29 | Go/no-go decision. No changes to launch plan, collateral, or deployment after this point unless P0. |

### Change control rule: "Trade, don't add"

- **Rule:** No new scope enters the project without removing equivalent effort from the plan. The requestor must propose what to cut.
- **Decision owner:** Product Lead (you) for scope trades within the cut list. VP Engineering for trades that touch non-negotiables or require additional resources.
- **Evaluation criteria:** (1) Does it block the Dec 3 launch? (2) Can we ship it in a fast-follow? (3) What is the trade-off from the cut list?
- **What gets traded off first:** Items from the "Cut first" list above, in order.

---

## 6) Stakeholder comms pack

### 6a) Weekly update template (for Slack #enterprise-sso-launch + email)

```
ENTERPRISE SSO INTEGRATION — WEEKLY UPDATE
Week [X] of 10 | [Date]

STATUS: [GREEN / YELLOW / RED]

WHAT CHANGED SINCE LAST UPDATE:
- [Key change 1]
- [Key change 2]

THIS WEEK'S PROGRESS:
- [Milestone achieved or progress]
- [Milestone achieved or progress]

NEXT WEEK'S PLAN:
- [Priority 1]
- [Priority 2]
- [Priority 3]

RISKS (top 3):
1. [Risk] — [Mitigation] — Owner: [Name]
2. [Risk] — [Mitigation] — Owner: [Name]
3. [Risk] — [Mitigation] — Owner: [Name]

DECISIONS NEEDED:
- [Decision] — Owner: [Name] — Needed by: [Date]

SCOPE CHANGES:
- [What was traded and why, or "None this week"]

TIMELINE:
- Next milestone: [Milestone] — [Date]
- Launch: December 3 (AWS re:Invent)
```

### 6b) Sales-specific comms template

```
TO: Sales Leadership + AEs
SUBJECT: Enterprise SSO Launch — Sales Update (Week [X])

LAUNCH DATE: December 3 at AWS re:Invent [ON TRACK / AT RISK / DELAYED]

WHAT SALES NEEDS TO KNOW:
- Current status: [1-2 sentences on overall progress]
- What's included at launch: [Bullet list of confirmed capabilities]
- What's NOT included at launch (fast-follow): [Bullet list]
- Beta access: [Available / date] — [How to nominate customers]

ACTION ITEMS FOR SALES:
- [ ] [Action item with deadline]
- [ ] [Action item with deadline]

TALK TRACK FOR CUSTOMERS:
- "We're launching enterprise SSO with [Okta/Azure AD] support at re:Invent.
  [SCIM / additional IdPs] will follow in [January]. Happy to get you into
  our beta program starting [date]."

QUESTIONS? Contact [Product Lead] in #enterprise-sso-launch.
```

### 6c) Marketing-specific comms template

```
TO: Marketing / PMM
SUBJECT: Enterprise SSO Launch — Marketing Update (Week [X])

LAUNCH DATE: December 3 at AWS re:Invent [ON TRACK / AT RISK / DELAYED]

CONTENT READINESS:
- Blog post draft due: [Date] — Status: [Not started / In progress / Review]
- Customer-facing docs due: [Date] — Status: [Not started / In progress / Review]
- re:Invent booth materials due: [Date] — Status: [Not started / In progress / Review]
- Demo environment ready: [Date] — Status: [Not started / In progress / Review]

SCOPE CONFIRMED FOR LAUNCH MESSAGING:
- [Feature 1 — safe to message]
- [Feature 2 — safe to message]

DO NOT MESSAGE (not confirmed for launch):
- [Feature that may be cut or fast-followed]

KEY DATES FOR MARKETING:
- Nov 1: Feature scope finalized — safe to begin final collateral
- Nov 15: Demo environment available for screenshots/video
- Nov 25: All collateral must be finalized
- Dec 3: Launch

ACTION ITEMS:
- [ ] [Action item with deadline]
```

### 6d) Executive briefing template

```
TO: VP Engineering / CTO / CEO
SUBJECT: Enterprise SSO — Exec Briefing (Week [X])

STATUS: [GREEN / YELLOW / RED]

ONE-LINE SUMMARY: [Single sentence on where we stand]

COMMITMENT MODEL:
- Committed: [What we've committed to and by when]
- Forecasted: [What we're forecasting with confidence level]
- At risk: [What's at risk and why]

KEY DECISIONS MADE THIS WEEK:
- [Decision and rationale]

ESCALATIONS / DECISIONS NEEDED FROM YOU:
- [Decision needed] — Impact if delayed: [Impact] — Needed by: [Date]
- Options: (1) [Option A] (2) [Option B] (3) [Option C]
- Recommended: [Option]

RESOURCE ASKS:
- [Any resource requests]

TIMELINE SNAPSHOT:
- Week [X] of 10
- Next critical milestone: [Milestone] — [Date]
- Launch: December 3
```

### 6e) Escalation note template (when status turns Red)

```
TO: [Decision owner]
SUBJECT: [RED] Enterprise SSO — Escalation: [Issue summary]
PRIORITY: Urgent — decision needed by [date]

WHAT IS RED AND WHY:
[1-3 sentences describing the blocker and root cause]

IMPACT IF UNCHANGED:
- [Specific impact on Dec 3 launch date]
- [Impact on scope, quality, or customer commitments]

OPTIONS:
1. CUT SCOPE: [What to cut] — Impact: [What customers lose] —
   Keeps Dec 3: [Yes/No]
2. ADD RESOURCES: [What's needed] — Cost: [Effort/$] —
   Keeps Dec 3: [Yes/No]
3. MOVE DATE: New date [X] — Impact: [Miss re:Invent, customer
   commitments] — Risk: [Downstream effects]
4. REDUCE QUALITY (if applicable): [What gets reduced] —
   Risk: [Customer/compliance impact]

RECOMMENDED OPTION: [Option #] because [rationale].

DECISION NEEDED BY: [Date/time]
DECISION OWNER: [Name]

Contact [Product Lead] for questions — available [time/channel].
```

---

## 7) Escalation decision framework: Negotiate the date vs. cut scope

This framework answers the critical question: **when do we negotiate the date, and when do we cut scope?**

### Cut scope when:

| Condition | Rationale |
|---|---|
| The slip is 5 days or less and a cut-list item can absorb it | Small scope trade preserves the date with minimal customer impact |
| The cut item is already on the "Cut first" list and has low customer impact | Pre-approved trades exist for exactly this situation |
| Sales/Marketing have already committed externally to a Dec 3 launch | External commitments make date movement extremely costly |
| The remaining scope still delivers a viable, valuable product | Customers get SSO at re:Invent; fast-follow fills the gap |
| The issue is isolated to one workstream (e.g., frontend polish) | Cutting from that workstream doesn't cascade |

### Negotiate the date when:

| Condition | Rationale |
|---|---|
| Security review reveals P0 vulnerabilities requiring 2+ weeks of remediation | Shipping with unresolved security issues is a non-negotiable blocker for enterprise customers |
| SOC 2 auditor cannot complete review cycle before Dec 3 | Enterprise customers require SOC 2 compliance; launching without it undermines the value proposition |
| Core SAML 2.0 authentication is not functional / stable by Nov 15 | The non-negotiable minimum is broken; no amount of scope cutting fixes this |
| Multiple milestones are Red simultaneously (3+) | Systemic issue signals the plan is fundamentally off; cutting scope alone won't recover |
| The remaining scope after all feasible cuts does not meet the "minimum viable launch" bar (SAML 2.0 + Okta + Azure AD + admin UI + security review + SOC 2) | A launch that doesn't clear the minimum bar damages credibility more than a delay |
| Team health is at serious risk (sustained overtime for 3+ weeks) | Burning out the team for a conference date creates longer-term damage |

### Decision process

```
1. Milestone slips 3+ days
   └─> Yellow: Identify mitigation + scope trade at weekly review
       └─> Trade accepted? -> Execute trade, stay on Dec 3
       └─> No viable trade? -> Move to step 2

2. Milestone slips 5+ days OR multiple Yellow milestones
   └─> Red: Escalation note within 24 hours to decision owner
       └─> Can we cut from the cut list and keep Dec 3?
           └─> Yes -> Execute cut, communicate to stakeholders
           └─> No -> Move to step 3

3. Non-negotiable is blocked OR cuts exhaust viable scope
   └─> Convene decision owner + VP Eng + Sales leadership
       └─> Option A: Reduced launch at re:Invent (announce SSO coming,
            demo in staging, GA in January)
       └─> Option B: Soft launch before re:Invent (limited GA with
            subset of features), full GA in January
       └─> Option C: Move launch to January (miss re:Invent entirely)
       └─> Decision within 48 hours to preserve time for plan adjustment
```

---

## 8) Risks / Open questions / Next steps

### Risks

| Risk | Impact | Probability | Mitigation | Owner | Early signal | Status |
|---|---|---|---|---|---|---|
| Security review delays (not started, reviewer availability unknown) | Build phase blocked; remediation timeline unknown | **High** | Submit review request immediately (Sep 24); escalate to VP Eng if not scheduled by Sep 27; identify backup external reviewer | Product Lead | Review not scheduled by Sep 27 | **Yellow — action needed this week** |
| Security review surfaces P0 findings requiring major rework | 1-3 week slip on backend; could break the Dec 3 date | **Medium** | Include security reviewer in tech design (Week 3) for early feedback; reserve 1 week buffer in Build for remediation | Backend Eng Lead | Preliminary findings report (M6, Oct 25) | Open |
| SOC 2 auditor availability / review cycle time | SOC 2 docs not accepted before launch; enterprise deal blocker | **Medium** | Contact auditor this week to confirm timeline; draft docs in parallel with Build; submit early (Nov 1) | Product Lead | Auditor response to scheduling request by Oct 4 | Open |
| Backend engineer capacity (2 engineers covering auth + security remediation) | Insufficient capacity if security work is larger than expected | **Medium** | Pre-identify a third backend engineer who could assist for 2-3 weeks if needed; cut SCIM first to free capacity | Backend Eng Lead | Security findings scope (Oct 25) | Open |
| Beta customer recruitment | Cannot validate in production before launch | **Low** | Sales to identify 2-3 enterprise customers using Okta/Azure AD willing to beta test; start outreach by Oct 14 | Sales Lead | Customer commitments by Nov 1 | Open |
| re:Invent demo environment stability | Embarrassing demo failure at the conference | **Low** | Dedicated demo tenant; rehearse demo by Nov 25; have fallback video recording | Frontend Eng + Product Lead | Demo rehearsal (Nov 25) | Open |

### Open questions

| # | Question | Impact on plan | Owner | Answer needed by |
|---|---|---|---|---|
| Q1 | Who is conducting the security review (internal team or external firm)? What is their availability? | Determines whether M2 is achievable by Oct 4 | Product Lead | **Sep 27** (this week) |
| Q2 | What is the SOC 2 auditor's review turnaround time? Can we get on their calendar for a Nov 1-15 review window? | Determines whether M10 is achievable | Product Lead | **Oct 4** |
| Q3 | Is SCIM provisioning a requirement for the Dec 3 launch, or can it be a fast-follow? | If not required, this is our biggest scope buffer (~1 week) | Product Lead + Sales | **Oct 4** |
| Q4 | Do we need to support Google Workspace at launch, or can we launch with Okta + Azure AD only? | Saves ~3 days if we defer | Product Lead + Sales | **Oct 4** |
| Q5 | Is a third backend engineer available as a contingency if security remediation is extensive? | Determines our resource flexibility | VP Engineering | **Oct 18** (Solutioning gate) |
| Q6 | What is the re:Invent booth/session plan -- do we need a live demo, or is a recorded demo acceptable? | Affects launch readiness scope | Marketing | **Oct 14** |

### Next steps (owners + dates)

| # | Action | Owner | Due date |
|---|---|---|---|
| 1 | **Submit security review request and confirm reviewer + timeline** | Product Lead | **Sep 25** (tomorrow) |
| 2 | Contact SOC 2 auditor to confirm availability for Nov review window | Product Lead | Sep 27 |
| 3 | Kick off IdP requirements gathering (customer interviews via Sales) | Backend Eng Lead + Sales | Sep 27 |
| 4 | Start UX wireframes for SSO admin configuration flow | Designer | Sep 27 |
| 5 | Confirm SCIM and Google Workspace scope decisions with Sales | Product Lead | Oct 4 |
| 6 | Communicate commitment model and project plan to all stakeholders | Product Lead | Sep 27 |
| 7 | Set up #enterprise-sso-launch Slack channel and weekly review calendar invite | Product Lead | Sep 25 |
| 8 | Send first weekly update (Week 1 status) | Product Lead | Sep 27 |
| 9 | Identify 2-3 beta customer candidates | Sales Lead | Oct 14 |
| 10 | Identify contingency backend engineer | VP Engineering | Oct 18 |

---

## Appendix: Week-by-week summary

| Week | Dates | Phase | Key milestones | Critical actions |
|---|---|---|---|---|
| 1 | Sep 24-27 | Discovery | -- | Submit security review; start requirements; start wireframes; stakeholder comms |
| 2 | Sep 30 - Oct 4 | Discovery | M1 (IdP reqs), M2 (security review started) | Lock IdP requirements; confirm security reviewer; confirm auditor availability |
| 3 | Oct 7-11 | Solutioning | M4 (tech design approved) | Tech design review with security input; SOC 2 gap analysis |
| 4 | Oct 14-18 | Solutioning | M3 (UX designs), M5 (SOC 2 change list) | **Solutioning gate / re-forecast checkpoint**; scope freeze |
| 5 | Oct 21-25 | Build | M6 (security preliminary findings) | Backend build starts; frontend starts on API contracts; security findings review |
| 6 | Oct 28 - Nov 1 | Build | -- | Core auth implementation; submit SOC 2 draft docs to auditor; recruit beta customers |
| 7 | Nov 4-8 | Build | M7 (backend code complete), M8 (frontend code complete) | Code complete target; integration testing begins |
| 8 | Nov 11-15 | Build | M9 (security remediation), M10 (SOC 2 accepted), M11 (staging) | **Code freeze (Nov 15)**; all security items resolved; staging deployed |
| 9 | Nov 18-22 | Launch | M12 (beta validation) | Beta customers testing; launch collateral finalization; demo prep |
| 10 | Nov 25 - Dec 2 | Launch | M13 (launch readiness), M14 (re:Invent launch) | **Launch readiness freeze (Nov 29)**; go/no-go; production deployment; demo rehearsal |
| Event | Dec 3 | **LAUNCH** | AWS re:Invent | Live demo, customer conversations, GA announcement |

---

## Quality gate self-assessment

Scored against [references/RUBRIC.md](../references/RUBRIC.md):

| Criterion | Score | Notes |
|---|---|---|
| 1) Deadline clarity | 2 | Fixed external deadline stated with justification; scope is the named trade variable |
| 2) Commitment ladder | 2 | Commit/forecast/target defined and used consistently; re-forecast checkpoint set (Oct 18) |
| 3) Phase plan + gates | 2 | Four phases with concrete outputs and decision gates; commitments limited to Discovery/Solutioning |
| 4) Milestones + ownership | 2 | 14 deliverable-based milestones with owners, dates, dependencies, confidence, and RAG |
| 5) RAG usefulness | 2 | Action-oriented definitions; Yellow/Red include explicit asks with deadlines |
| 6) Governance cadence | 2 | Weekly review agenda, escalation triggers table, decision log started |
| 7) Scope protection | 2 | Non-goals, ordered cut list, freeze points, "trade don't add" rule with named decision owner |
| 8) Stakeholder comms | 2 | Five templates (weekly, Sales, Marketing, Exec, escalation) with commitment language and decision asks |
| 9) Risk management | 2 | Risk register with early signals and owners; open questions with time-bound deadlines; next steps with owners and dates |
| 10) AI/ML outer loop | N/A | Not applicable (no AI/ML component) |
| **Total** | **18/18** | Passing bar: >= 16/20 |
