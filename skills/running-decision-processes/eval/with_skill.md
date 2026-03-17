# Decision Process Pack: Sunset Feature X

---

## 1) Decision Brief / Pre-read

**Decision statement (one sentence):**
We are deciding whether to sunset Feature X by March 15 to reduce escalating support costs and reallocate engineering capacity toward higher-adoption features.

**Decision deadline:** March 15

**Decision type:** One-way door (sunsetting a shipped feature is hard to reverse once customers migrate away and code is deprecated; rebuilding later would cost significantly more than maintaining now)

**Process intensity:** Standard-to-heavy (one-way door with customer-facing impact, legal notification requirements, and cross-functional coordination across 5 teams)

**Why now (what changed / why it matters):**
- Support ticket volume for Feature X has increased ~40% over the past two quarters while active usage has declined ~25%.
- Engineering is spending a growing share of maintenance cycles on Feature X, crowding out work on higher-value features.
- If we do not decide by March 15, we miss the 30-day customer notification window for an April 14 sunset, pushing the earliest possible sunset to May or later and accumulating additional support and maintenance costs.
- Continuing to invest without a deliberate decision creates "decision drift" -- the feature slowly degrades, frustrating remaining users and increasing churn risk without a clear path forward.

**Success criteria (what "good" looks like):**
- A clear, communicated decision that all stakeholders understand and can act on.
- If sunset: zero unplanned downtime during deprecation; top customers notified at least 30 days before any service change; support ticket volume for Feature X trends to near-zero within 60 days of sunset; freed engineering capacity is redeployed to higher-priority work.
- If keep/invest: a funded plan with measurable adoption and support-load targets within 90 days.

**Non-negotiables / constraints:**
- **Downtime:** No downtime during any transition -- this is a hard constraint from Eng and customer commitments.
- **Customer notification:** Top customers must receive 30 days' advance written notice before any sunset date -- Legal and contractual requirement.
- **Timeline:** Decision must be finalized by March 15 to preserve the April 14 sunset window.
- **Budget:** No incremental headcount; any "invest to fix" option must be resourced from existing team capacity.
- **Out-of-scope:** This decision does not cover broader product portfolio rationalization; it is Feature X only.

**Background (facts):**
- Feature X launched 18 months ago to address a segment of power users requesting advanced analytics.
- Initial adoption was moderate (~15% of active users tried it in the first quarter).
- Adoption has declined steadily: current monthly active users are ~6% of the base.
- Support tickets related to Feature X now represent ~20% of total support volume, up from ~8% a year ago.
- Two prior attempts to improve Feature X UX (Q2 and Q4 last year) did not meaningfully move adoption or reduce support load.
- No contractual obligation to maintain Feature X indefinitely, but several top-tier customers use it and have renewal cycles in Q2.

**Prior decisions + rationale (historian pass):**
- Q2 last year: Team invested a 2-week sprint to simplify the Feature X onboarding flow. Result: marginal adoption lift (~2%), no reduction in support tickets. Rationale at the time: "low-cost bet to see if UX is the barrier."
- Q4 last year: Team fixed top 5 bugs in Feature X. Result: support tickets dipped briefly then resumed upward trend. Rationale: "address quality before considering sunset."
- Lesson: surface-level fixes have not changed the trajectory. The remaining issues appear to be fundamental to the feature's architecture and value proposition, not cosmetic.

**Key assumptions / unknowns (explicit):**
- **A1 (testable):** Sunsetting Feature X will not cause material churn among top-tier customers, because usage data shows most top customers use Feature X minimally or have alternatives. *Test: survey/call top 10 customers before finalizing.*
- **A2 (testable):** Support load will drop proportionally (~20% reduction) within 60 days of sunset. *Test: track ticket volume tagged to Feature X weekly post-sunset.*
- **A3 (testable):** Engineering capacity freed (~1.5 FTE-equivalents of maintenance) can be redeployed to roadmap items within one sprint. *Test: sprint planning post-sunset.*
- **A4 (unknown):** Competitor response -- unclear if competitors will use our sunset to position their alternative. *Monitor: Sales intel and win/loss reports for 90 days.*
- **A5 (unknown):** Whether a lightweight replacement (e.g., a third-party integration) could satisfy remaining users at lower cost. *Needs: quick feasibility check from Eng before the decision meeting.*

**Options (3):**
- **Option A: Keep as-is** -- Continue maintaining Feature X at current investment level.
- **Option B: Invest to fix** -- Allocate a dedicated squad (2-3 engineers) for one quarter to re-architect Feature X and address root causes.
- **Option C: Sunset** -- Deprecate Feature X with a phased wind-down, 30-day customer notice, and support runbook.

**Evaluation criteria (and weights):**
- Customer impact / churn risk (25%)
- Support cost reduction (20%)
- Engineering opportunity cost (20%)
- Strategic alignment (15%)
- Execution risk (10%)
- Reversibility (10%)

**Recommendation:**
- **Proposed decision:** Sunset Feature X (Option C).
- **Rationale:**
  - Two prior improvement attempts failed to change the adoption or support trajectory.
  - Feature X serves only ~6% of users but consumes ~20% of support volume and meaningful engineering maintenance.
  - Sunsetting frees capacity for higher-impact work aligned with the product strategy.
  - The 30-day notification constraint is achievable if we decide by March 15.
  - Customer churn risk is manageable with proactive outreach and migration support.
- **Tradeoffs accepted:**
  - We accept the risk of disappointing a small segment of power users.
  - We accept that a competitor may position against this move.
  - We accept that if the decision is wrong, rebuilding is expensive (one-way door).

**Risks and mitigations:**
- **Customer churn (top-tier accounts):** Mitigate by personal outreach from Sales/CSM to top 10 accounts before public announcement; offer migration assistance or workarounds.
- **Internal morale / "we built this for nothing" narrative:** Mitigate by framing as a disciplined portfolio decision; celebrate what was learned.
- **Competitor positioning:** Mitigate by preparing a brief competitive response FAQ for Sales.
- **Execution risk (no downtime):** Mitigate by phased rollback with feature flag; Eng owns a detailed deprecation runbook.

**Decision roles (DACI):**
- **Decider:** VP Product (or Head of Product)
- **Driver/Owner:** PM (Product Manager for Feature X)
- **Approver (veto rights):** Legal (customer notification compliance), Eng Lead (no-downtime feasibility)
- **Contributors/Consulted:** Support Lead, Sales Lead, Engineering Lead, Legal
- **Informed:** Broader product team, customer success, marketing

**Links / evidence:**
- Feature X usage dashboard (link TBD)
- Support ticket volume report (link TBD)
- Q2 and Q4 improvement retrospectives (link TBD)
- Customer contract review (Legal, link TBD)

---

## 2) Options + Criteria Matrix

| Criterion (weight) | Option A: Keep as-is | Option B: Invest to fix | Option C: Sunset |
|---|---|---|---|
| **Customer impact / churn risk (25%)** | Low short-term risk; ongoing degradation frustrates users over time | Medium -- investment may improve experience but no guarantee; delays other features customers want | Medium -- small user segment loses functionality; mitigated by outreach and migration support |
| **Support cost reduction (20%)** | None; support load continues rising (~20% of volume) | Uncertain; may reduce if root causes are fixed, but prior fixes failed | High; ~20% ticket volume eliminated within 60 days |
| **Engineering opportunity cost (20%)** | ~1.5 FTE ongoing maintenance drains roadmap capacity | ~2-3 FTE dedicated for a quarter (high opportunity cost); then ongoing maintenance if it works | Frees ~1.5 FTE immediately after deprecation; one-time migration cost (~2 sprints) |
| **Strategic alignment (15%)** | Low -- Feature X is not on the strategic roadmap | Medium -- only if re-architecture aligns with platform direction | High -- frees resources for strategic priorities |
| **Execution risk (10%)** | Low (status quo) | Medium-high -- re-architecture is complex; two prior attempts failed | Medium -- requires careful phased rollback and customer comms |
| **Reversibility (10%)** | Fully reversible (no change) | Partially reversible (can stop investment, but sunk cost) | Low reversibility (one-way door; rebuilding later is expensive) |
| **Key assumptions** | Support load will plateau (unlikely given trend) | Root cause is fixable with more investment (contradicted by prior attempts) | Remaining users can migrate or accept removal; no material churn |
| **Unknowns** | How long before feature becomes a liability? | Will investment actually move metrics this time? | Competitor response; exact churn from top accounts |

**Summary:** Option C (Sunset) scores highest on support cost reduction, engineering opportunity cost, and strategic alignment. Its primary risk -- customer churn -- is manageable with proactive outreach. Option B carries the highest opportunity cost with uncertain payoff given two prior failed attempts. Option A is the "slow bleed" default that worsens over time.

---

## 3) Decision Rights + Process Plan

**Decision-rights model:** DACI

**Roles:**
- **Decider:** VP Product -- makes the final call; accountable for the outcome
- **Approver (veto holders):**
  - Legal -- must confirm 30-day notification compliance and contractual obligations
  - Eng Lead -- must confirm no-downtime deprecation is feasible
- **Contributors (consulted):**
  - PM (Driver) -- prepares the brief, runs the process, synthesizes inputs
  - Support Lead -- provides ticket data, customer pain points, migration feasibility
  - Sales Lead -- provides customer churn risk assessment, competitive intel
  - Engineering Lead -- provides technical feasibility, deprecation plan, capacity estimates
  - Legal -- reviews notification requirements and contractual constraints
- **Informed:**
  - Broader product team, customer success managers, marketing (for external comms)

**Process plan (dates/times):**

| Milestone | Date | Owner |
|---|---|---|
| Pre-read (this Decision Brief) shared | March 3 | PM |
| Async input window opens (consult + curiosity loop) | March 3-7 | PM |
| Curiosity loop outreach sent | March 3 | PM |
| Curiosity loop responses collected | March 7 | PM |
| Legal review of notification requirements complete | March 7 | Legal |
| Eng feasibility confirmation (no-downtime plan) | March 7 | Eng Lead |
| Decision meeting | March 10 (45 min) | PM facilitates; VP Product decides |
| Decision logged + internal comms sent | March 11 | PM |
| Top customer notifications sent (if sunset) | March 12 | Sales + CSM |
| Public announcement (if sunset) | March 12 | PM + Marketing |
| Review date | April 25 (6 weeks post-decision) | PM |

**Escalation / veto rules (explicit):**
- **Legal veto:** If Legal determines that contractual obligations require more than 30 days' notice for any customer, the sunset date shifts accordingly. Legal must raise this by March 7 or the default is "30 days is sufficient."
- **Eng veto:** If Eng Lead determines that no-downtime deprecation is not feasible within the timeline, the sunset date shifts or a phased approach is required. Eng must raise this by March 7.
- **Sales escalation:** If Sales identifies a top-5 account with imminent renewal that would be materially impacted, this is escalated to VP Product before the decision meeting.
- **Default if no response by March 7:** Silence from a consulted party is treated as "no objection." The process proceeds.

---

## 4) Decision Meeting Agenda

**Goal:** Make a final decision on Feature X (keep / invest / sunset) and commit to next steps.
**Attendees:** VP Product (Decider), PM (Driver/Facilitator), Eng Lead, Support Lead, Sales Lead, Legal
**Pre-read:** Decision Brief (this document) -- shared March 3
**Duration:** 45 minutes

| Time | Agenda item | Owner |
|---|---|---|
| 0-3 min | Restate decision statement + deadline; confirm everyone read the pre-read | PM |
| 3-15 min | Review options + criteria matrix + curiosity loop inputs; highlight where inputs shifted the analysis | PM |
| 15-25 min | Surface disagreements: "What would change your mind?" Round-robin from each stakeholder. Record dissent. | PM (facilitator) |
| 25-30 min | Legal and Eng confirm or raise veto items (notification compliance, no-downtime feasibility) | Legal, Eng Lead |
| 30-38 min | VP Product states decision, names tradeoffs accepted, confirms owner | VP Product |
| 38-45 min | Confirm next steps, comms plan, milestones, review date | PM |

**Ground rules:**
- No new options introduced in the meeting (they should have been raised in the input window).
- Disagreements are recorded in the decision log, not smoothed over.
- The Decider decides; the meeting is not seeking consensus.

---

## 5) Curiosity Loop

### Outreach message (Slack/email)

**Subject:** Quick input on Feature X decision (2 min)

Hi [name] -- we are deciding **whether to sunset, invest in, or keep Feature X as-is** by **March 15**.

Could you please:
1. Pick the top **2** options you would choose (from below) and **why**
2. Name the **#1 missing consideration** we should include
3. What would change your mind?

Options:
- **Option A: Keep as-is** -- continue current maintenance level
- **Option B: Invest to fix** -- dedicate a squad for one quarter to re-architect
- **Option C: Sunset** -- phased deprecation with 30-day customer notice

Reply in bullets; short is perfect. Responses needed by **March 7**. Thank you.

### Suggested curiosity loop participants (8-12)

| # | Person / Role | Why include |
|---|---|---|
| 1 | Support Lead | Owns ticket data; knows the pain firsthand |
| 2 | Senior Support Agent (frontline) | Hears customer frustration daily; ground-truth perspective |
| 3 | Sales Lead | Knows competitive landscape and renewal risk |
| 4 | Account Manager (top-tier accounts) | Direct relationship with the customers most affected |
| 5 | Eng Lead | Knows the technical debt and feasibility of each option |
| 6 | Senior Engineer (Feature X maintainer) | Deepest technical context on root causes |
| 7 | Legal Counsel | Contractual and notification requirements |
| 8 | Customer Success Manager | Understands adoption patterns and customer health |
| 9 | Data Analyst | Can validate usage/adoption metrics and trends |
| 10 | Product Designer | Perspective on whether UX changes could move the needle |
| 11 | VP Engineering | Resource allocation and platform strategy perspective |
| 12 | Marketing Lead | External messaging and positioning considerations |

### Input capture table

| Person | Top choice(s) | Why | Biggest concern | Missing consideration | Evidence/link |
|---|---|---|---|---|---|
| Support Lead | *(to be filled)* | | | | |
| Senior Support Agent | *(to be filled)* | | | | |
| Sales Lead | *(to be filled)* | | | | |
| Account Manager | *(to be filled)* | | | | |
| Eng Lead | *(to be filled)* | | | | |
| Senior Engineer | *(to be filled)* | | | | |
| Legal Counsel | *(to be filled)* | | | | |
| CSM | *(to be filled)* | | | | |
| Data Analyst | *(to be filled)* | | | | |
| Product Designer | *(to be filled)* | | | | |
| VP Engineering | *(to be filled)* | | | | |
| Marketing Lead | *(to be filled)* | | | | |

---

## 6) Decision Log Entry

**Decision:** Sunset Feature X with a phased deprecation, effective April 14 (30 days after top-customer notification on March 12).

**Date decided:** March 10 (decision meeting)

**Decider:** VP Product

**Driver/Owner:** PM (Product Manager for Feature X)

**Participants (consulted):** Eng Lead, Support Lead, Sales Lead, Legal, CSM, Senior Engineer, Account Manager, Data Analyst, Product Designer, VP Engineering, Marketing Lead

**Decision type:** One-way door (hard to reverse once deprecated and customers migrate away)

**Rationale (why this):**
- Feature X adoption has declined to ~6% of active users while generating ~20% of support volume -- the cost-to-value ratio is unsustainable.
- Two prior improvement investments (Q2 and Q4) failed to change the trajectory, indicating the issues are structural, not cosmetic.
- Sunsetting frees ~1.5 FTE of engineering capacity for strategic priorities.
- The 30-day notification window is achievable within the March 15 deadline.
- Proactive customer outreach mitigates churn risk for top-tier accounts.

**Tradeoffs accepted:**
- A small segment of power users (~6% of base) will lose functionality they depend on.
- Competitors may position against this decision; Sales needs a response playbook.
- If the decision proves wrong, rebuilding Feature X will be significantly more expensive than maintaining it would have been.
- Short-term customer satisfaction hit for affected users in exchange for long-term product focus and support sustainability.

**Key assumptions (testable):**
- A1: Top-tier customer churn from sunset will be < 2% of ARR. *(Test: track renewals and churn for 90 days post-sunset.)*
- A2: Support ticket volume drops ~20% within 60 days of full deprecation. *(Test: weekly ticket volume tracking.)*
- A3: Freed engineering capacity is redeployed to roadmap within 1 sprint. *(Test: sprint planning review.)*
- A4: No major competitive loss attributed to Feature X sunset within 90 days. *(Test: win/loss analysis.)*

**What would trigger a revisit:**
- If top-tier customer churn exceeds 5% of ARR within 90 days of announcement.
- If a major customer explicitly makes Feature X a renewal condition and the ARR at risk exceeds a threshold set by Sales + Finance.
- If a lightweight replacement (e.g., third-party integration) becomes feasible at low cost before deprecation is complete.

**Owner's next steps (milestones):**
1. March 11: Internal announcement to all teams (PM)
2. March 12: Personal outreach to top 10 customers (Sales + CSM)
3. March 12: Public sunset announcement with FAQ (PM + Marketing)
4. March 12 - April 14: Deprecation period -- feature remains live with deprecation banner; support provides migration guidance
5. March 19: Eng begins phased code removal behind feature flag (Eng Lead)
6. April 14: Feature X fully deprecated (feature flag off); support runbook activated for residual inquiries
7. April 14: Engineering capacity formally reallocated in sprint planning (Eng Lead + PM)

**Review date + metrics to review:**
- **Review date:** April 25 (6 weeks post-decision, ~11 days after full sunset)
- **Metrics:**
  - Support ticket volume (Feature X tagged) -- target: < 5% of pre-sunset levels
  - Customer churn / ARR impact -- target: < 2% of ARR
  - Engineering velocity on new roadmap items -- target: measurable sprint output increase
  - Win/loss competitive mentions of Feature X -- target: no material pattern
  - Customer sentiment (NPS/CSAT) among affected segment -- target: stabilized within 60 days

---

## 7) Decision Communication

### Internal announcement (Slack / email to all teams)

**Audience:** All product, engineering, support, sales, customer success, marketing, legal
**Channel:** #product-announcements (Slack) + email to team leads
**Date:** March 11

---

**Subject: Decision -- Sunsetting Feature X (effective April 14)**

Team,

After a thorough cross-functional review, we have decided to **sunset Feature X**, effective **April 14**.

**Why:**
- Feature X adoption has declined to ~6% of active users while driving ~20% of support volume.
- Two prior improvement investments did not change the trajectory -- the issues are structural.
- Sunsetting frees meaningful engineering capacity for our strategic priorities.
- This is a disciplined portfolio decision, not a reflection on the work the team put into Feature X.

**What changes now:**
- Top customers will be personally notified by Sales/CSM starting March 12, with 30+ days' advance notice.
- A public sunset announcement with FAQ goes out March 12.
- Feature X will display a deprecation banner during the March 12 - April 14 transition period.
- Feature X will be fully turned off on April 14 via feature flag.
- Engineering maintenance on Feature X stops after full deprecation.

**What stays the same:**
- All other product features and roadmap remain unchanged.
- Support continues to assist Feature X users with migration and alternatives through the transition period.
- Customer commitments unrelated to Feature X are unaffected.

**Owner + next steps:**
- **PM** owns the overall sunset process and timeline.
- **Sales + CSM** own customer outreach (starting March 12).
- **Eng Lead** owns the technical deprecation plan (phased, behind feature flag, zero downtime).
- **Support Lead** owns the migration runbook and FAQ for support agents.
- **Marketing** owns the public-facing announcement.

**Risks / watch-outs:**
- Some customers will be unhappy. Direct them to Sales/CSM for personal follow-up.
- If any customer raises a contractual concern, escalate to Legal immediately.
- Competitors may reference this; Sales has a response playbook (available by March 12).

**When we will review:** April 25. We will assess customer churn, support volume, engineering velocity, and competitive impact. If outcomes diverge significantly from expectations, we will adapt.

Questions? Reach out to PM or post in #feature-x-sunset.

---

### External customer notification (for top customers -- personalized)

**Audience:** Top 10 customers using Feature X
**Channel:** Personal email from Account Manager / CSM
**Date:** March 12

---

Dear [Customer Name],

I am writing to let you know that we will be **retiring Feature X on April 14**. We want to make sure you have plenty of time to prepare -- this notice provides more than 30 days before any change takes effect.

**Why we are making this change:**
We are focusing our product investment on the areas that deliver the most value to customers like you. After careful evaluation, we determined that the resources supporting Feature X can be better directed toward [mention 1-2 upcoming improvements relevant to this customer].

**What this means for you:**
- Feature X will continue to work normally through **April 14**.
- After April 14, Feature X will no longer be available.
- [If applicable: We recommend transitioning to [alternative/workaround] -- here is a guide: [link].]

**How we will support you:**
- Your dedicated account team is available to help you transition.
- We have prepared a migration guide: [link].
- If you have specific workflows that depend on Feature X, please let us know by [date] and we will work with you on alternatives.

We value your partnership and want to make this transition as smooth as possible. Please do not hesitate to reach out with any questions or concerns.

Best regards,
[Account Manager / CSM name]

---

## 8) Decision Review Plan

**Decision reviewed:** Sunset Feature X
**Review date:** April 25
**Facilitator:** PM
**Attendees:** VP Product, Eng Lead, Support Lead, Sales Lead, CSM

### Metrics to review

| Metric | Baseline (pre-sunset) | Target (at review) | Actual (to be filled) | Status |
|---|---|---|---|---|
| Support tickets (Feature X tagged) | ~20% of total volume | < 5% of pre-sunset level | | |
| Customer churn (ARR impact) | 0% | < 2% of ARR | | |
| Engineering sprint velocity (new roadmap items) | [baseline] | Measurable increase | | |
| Competitive win/loss mentions of Feature X | [baseline] | No material pattern | | |
| Customer sentiment (NPS/CSAT, affected segment) | [baseline] | Stabilized within 60 days | | |

### Assumption check

| Assumption | Expected | Actual | Right/Wrong | Learning |
|---|---|---|---|---|
| A1: Top-tier customer churn < 2% ARR | < 2% | *(to be filled)* | | |
| A2: Support tickets drop ~20% within 60 days | ~20% reduction | *(to be filled)* | | |
| A3: Eng capacity redeployed within 1 sprint | 1 sprint | *(to be filled)* | | |
| A4: No major competitive loss within 90 days | None | *(to be filled)* | | |

### Retrospective prompts

- **Outcome vs success criteria:** Did the sunset achieve what we expected? Where did reality diverge from the plan?
- **Which assumptions were right/wrong (and how we know):** Review each assumption against data. What surprised us?
- **What we learned (process + content):**
  - Was the decision process appropriately rigorous for a one-way door?
  - Did the curiosity loop surface anything that changed the outcome?
  - Was the customer notification and transition handled well?
  - Did the 30-day notice period prove sufficient?
- **What we would do differently next time (decision process improvements):**
  - Should we have consulted customers earlier?
  - Was the options matrix comprehensive enough?
  - Were decision rights clear throughout?
- **Follow-ups / next decision(s):**
  - If churn is higher than expected: evaluate a lightweight replacement or third-party integration.
  - If freed capacity is not being utilized: review sprint planning and roadmap prioritization.
  - Schedule a 90-day check-in (June 10) for longer-term impact assessment.

---

## 9) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Top-tier customer churn exceeds expectations | Medium | High | Personal outreach to top 10 accounts; migration support; escalation path to VP Product if ARR at risk > threshold | Sales Lead + CSM |
| Competitor positions against sunset | Medium | Medium | Sales response playbook + competitive FAQ | Sales Lead + Marketing |
| Technical issues during deprecation (downtime) | Low | High | Feature-flag-based phased rollback; Eng deprecation runbook; rollback plan tested in staging | Eng Lead |
| Internal morale impact ("we built this for nothing") | Medium | Low-Medium | Frame as disciplined portfolio management; celebrate learnings; redeploy team to exciting work | VP Product + PM |
| Legal/contractual surprise (customer requires longer notice) | Low | High | Legal review by March 7; if any contract requires > 30 days, adjust sunset date for that customer | Legal |
| Residual support volume persists post-sunset | Low | Low | Support runbook covers post-sunset inquiries; auto-responder for Feature X tickets after April 14 | Support Lead |

### Open questions

1. **Third-party replacement feasibility:** Can Eng confirm by March 7 whether a lightweight third-party integration could serve remaining Feature X users at minimal cost? This could become a mitigation offering for unhappy customers.
2. **Exact ARR at risk:** Sales needs to quantify the ARR tied to accounts where Feature X is a critical workflow (not just "used occasionally"). This informs the churn risk threshold for the revisit trigger.
3. **Data retention:** What happens to data generated by Feature X? Do we archive it, export it for customers, or delete it? Legal and Eng need to align on a data retention/deletion policy by March 7.
4. **Documentation cleanup:** Product docs, help center articles, and marketing pages referencing Feature X need to be updated. Who owns this and by when?
5. **Feature flag rollback duration:** How long does Eng keep the feature flag available for emergency rollback after April 14? Recommend: 30 days (until May 14), then full code removal.

### Next steps

| # | Action | Owner | Due date |
|---|---|---|---|
| 1 | Share this Decision Brief as pre-read to all stakeholders | PM | March 3 |
| 2 | Send curiosity loop outreach to 8-12 participants | PM | March 3 |
| 3 | Legal completes contract review for notification requirements | Legal | March 7 |
| 4 | Eng confirms no-downtime deprecation feasibility + plan | Eng Lead | March 7 |
| 5 | Eng provides quick assessment on third-party replacement feasibility | Eng Lead | March 7 |
| 6 | Sales quantifies ARR at risk for affected accounts | Sales Lead | March 7 |
| 7 | Collect and synthesize curiosity loop responses | PM | March 7 |
| 8 | Decision meeting | PM (facilitator), VP Product (Decider) | March 10 |
| 9 | Log decision and send internal comms | PM | March 11 |
| 10 | Personal outreach to top 10 customers | Sales + CSM | March 12 |
| 11 | Public sunset announcement + FAQ published | PM + Marketing | March 12 |
| 12 | Deprecation banner activated in Feature X | Eng Lead | March 12 |
| 13 | Begin phased code deprecation behind feature flag | Eng Lead | March 19 |
| 14 | Feature X fully off (feature flag disabled) | Eng Lead | April 14 |
| 15 | Reallocate freed engineering capacity in sprint planning | Eng Lead + PM | April 14 |
| 16 | Decision review meeting | PM | April 25 |
| 17 | 90-day impact check-in | PM | June 10 |

---

## Quality Gate: Self-Assessment

### Checklist A: Decision Process Pack quality (pre-flight)

- [x] Decision statement is one sentence and includes a deadline.
- [x] One-way door vs two-way door classification is explicit.
- [x] Constraints/non-negotiables are listed (no downtime, 30-day notice, March 15 deadline, no incremental headcount).
- [x] Options set is 3 real options (not strawmen); tradeoffs are visible.
- [x] Evaluation criteria reflect real tradeoffs (weighted: customer impact, support cost, eng opportunity cost, strategic alignment, execution risk, reversibility).
- [x] Key assumptions/unknowns are explicit and testable (A1-A5 with test plans).
- [x] Decision rights are explicit (one Decider: VP Product); veto power is explicit (Legal, Eng Lead).
- [x] Consultation plan exists (curiosity loop to 12 people, by March 7).
- [x] Decision log entry includes rationale, tradeoffs, owner, and review date (April 25).
- [x] Communication draft states what changes now, who owns next steps, and when we will review.
- [x] Risks / Open questions / Next steps are included.

### Checklist B: Anti-hesitation

- [x] Not waiting for "perfect data" -- proceeding with explicit assumptions and a review plan.
- [x] Decision is framed as a tradeoff, not as "finding the perfect answer."
- [x] Clear "default if we do nothing" is stated (slow bleed: rising support costs, declining adoption, engineering drain).
- [x] The Decider (VP Product) is expected to choose between imperfect options and own the outcome.

### Checklist C: Explicit assumptions (Annie Duke test)

- [x] Assumptions are written as statements that could be proven wrong (A1-A5).
- [x] Each major assumption has a plan to test/observe it (metrics, surveys, sprint planning).
- [x] A review date is set to check assumptions vs reality (April 25 + June 10).

### Checklist D: Curiosity loop

- [x] Ask is lightweight (3 prompts: pick top 2 + why, missing consideration, what would change your mind).
- [x] Consult list includes experts + context-aware peers (12 people across support, sales, eng, legal, design, data, marketing).
- [x] Inputs will capture "why" and evidence; disagreements will be recorded.

### Checklist E: Post-decision follow-through

- [x] Decision will be communicated to everyone who needs to execute (internal announcement + customer outreach).
- [x] Owner (PM) and first milestones are named (17 milestones with dates and owners).
- [x] Review date (April 25) and metrics are scheduled.
- [x] A retrospective is planned with specific prompts.

### Rubric scoring

| Dimension | Score | Rationale |
|---|---|---|
| 1) Decision clarity | 2 | One-sentence decision + March 15 deadline + explicit scope boundaries; any stakeholder can restate without ambiguity. |
| 2) Options and tradeoffs | 2 | Three genuinely viable options with explicit tradeoffs, reversibility classification, and key assumptions per option. |
| 3) Assumptions explicitness | 2 | Five key assumptions are explicit, testable (with observable signals), and paired with a review plan (April 25) and revisit triggers. |
| 4) Decision rights and alignment | 2 | One Decider (VP Product), clear DACI roles, explicit veto holders (Legal, Eng Lead), specific escalation rules. |
| 5) Process fit (speed vs rigor) | 2 | Standard-to-heavy process matched to one-way door classification; timeboxed (March 3-15); executable timeline. |
| 6) Communication and follow-through | 2 | Decision log + owner (PM) + internal/external comms drafted + 17 milestones + review date (April 25) with 5 metrics. |
| **Total** | **12/12** | Ship as-is. |
