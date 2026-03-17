# Post-mortem Pack: Payments Processing API Outage (2026-03-16)

---

## 1) Retro Brief + Agenda

### Retro Brief
- **Review type:** Incident (Production Outage)
- **Title:** Payments API 90-Minute Outage Due to Database Migration Failure
- **Date/time:** 2026-03-17 (timebox: 90 min)
- **Facilitator:** Engineering Manager, Payments Team (to be confirmed)
- **Scribe:** Senior Engineer, Payments Team (to be confirmed)
- **Decision owner:** VP Engineering or Director of Infrastructure (to be confirmed)
- **Attendees:** On-call engineer, database migration author, platform/infra lead, incident responders, QA/staging environment owner, payments product manager
- **Audience for write-up:** Engineering team + Engineering Leadership
- **Goal:** Learning + prevention -- understand the systemic conditions that allowed a staging-passing migration to fail in production, clarify incident response roles, and update playbooks to prevent recurrence.
- **Ground rules:**
  - "We are here to improve systems, not judge individuals."
  - "Assume people acted reasonably given what they knew at the time."
  - "If performance topics exist, we will handle them separately through the right channels."
- **Pre-reads / evidence:**
  - Database migration PR and review comments
  - Staging test results / CI pipeline logs
  - Production error logs and alerting timeline
  - On-call escalation Slack thread / PagerDuty timeline
  - Payments API error rate dashboard (2026-03-16)
  - Current rollback playbook (version prior to incident)

### Agenda (90 min)
1. Frame goal + ground rules (5 min)
2. Facts + timeline walkthrough (20 min)
3. Contributing factors -- 5 Whys deep dive (25 min)
4. Learnings + decisions (15 min)
5. Action tracker -- owners and due dates (15 min)
6. Kill criteria / triggers for future migrations (5 min)
7. Wrap: owners, follow-up date, shareout plan (5 min)

---

## 2) Facts + Timeline

### Impact Snapshot
- **Customer impact:** ~2,000 transactions failed or were delayed over 90 minutes. Affected customers experienced payment failures, timeouts, or duplicate charge attempts. Potential downstream effects on order fulfillment and customer trust.
- **Business impact:** Revenue loss from ~2,000 failed transactions (exact dollar amount TBD -- action item to quantify). Potential SLA breach with payment processor partners. Customer support ticket surge expected. Reputational risk if customers experienced double-charges.
- **Internal impact:** On-call engineer consumed for 90+ minutes; incident commander role was unclear, adding confusion and coordination overhead; rollback playbook was outdated, forcing ad-hoc troubleshooting; engineering leadership had to be pulled in manually.
- **How we know:** Production error logs, Payments API error rate dashboard, PagerDuty alerts, Slack incident channel, transaction failure count from database query. (Hypothesis: exact customer-facing impact numbers need validation from support ticket volume and payment processor reconciliation.)

### Timeline

| Time (UTC, 2026-03-16) | Event | Evidence / Link | Notes (Fact vs Hypothesis) |
|---|---|---|---|
| ~14:00 | Database migration deployed to production via standard deploy pipeline | Deploy logs, CI/CD pipeline run | **Fact** |
| ~14:00 - 14:05 | Migration begins executing against production database; starts encountering performance degradation due to table lock on high-volume table | Database slow query logs (to be confirmed) | **Hypothesis** -- exact mechanism of failure needs confirmation from DB logs |
| ~14:05 - 14:10 | Payments API begins returning elevated error rates (timeouts, 500s) as database queries fail or time out | API error rate dashboard | **Fact** -- error rate spike visible in monitoring |
| ~14:10 | Automated alerting fires (PagerDuty page to on-call engineer) | PagerDuty alert log | **Fact** (assumption: alerting fired within ~10 min; exact timestamp to be confirmed) |
| ~14:10 - 14:25 | On-call engineer begins investigation; identifies database migration as likely cause; attempts to assess rollback options | Slack thread in #incidents | **Fact** |
| ~14:25 | On-call engineer reviews existing rollback playbook; discovers it is outdated and does not cover this migration pattern | Rollback playbook document (last updated date TBD) | **Fact** -- confirmed by on-call engineer report |
| ~14:30 | On-call engineer begins pulling in additional engineers for help | Slack thread | **Fact** |
| ~14:30 - 14:40 | Confusion over who is incident commander; no one formally declares IC role; coordination overhead increases | Slack thread, verbal reports | **Fact** -- multiple people confirmed role ambiguity |
| ~14:40 | On-call engineer escalates to engineering manager / leadership | Slack escalation, PagerDuty escalation | **Fact** |
| ~14:40 - 15:10 | Team works on manual rollback; identifies that migration cannot be simply reverted due to partial state; develops ad-hoc fix | Slack thread, DB admin console logs | **Hypothesis** -- exact rollback steps need documentation |
| ~15:10 - 15:25 | Fix applied; database migration rolled back or remediated; payments API begins recovering | Deploy logs, API error rate dashboard | **Fact** -- recovery visible in dashboard |
| ~15:30 | Payments API fully recovered; error rates return to baseline | API error rate dashboard | **Fact** |
| ~15:30 - 16:00 | Post-incident verification: spot-check transactions, confirm no data corruption, begin customer impact assessment | Transaction reconciliation queries | **Hypothesis** -- verification steps assumed; need confirmation |

**Key durations:**
- Time to detect: ~10 minutes (deployment to first alert)
- Time to escalate: ~30 minutes (first alert to escalation)
- Time to resolve: ~90 minutes (deployment to full recovery)
- Escalation delay: ~20 minutes of confusion before clear IC ownership

---

## 3) Contributing Factors + Root Cause Hypotheses

### Contributing Factors (Clustered)

| Cluster | Factor | Evidence | "Why it made sense at the time" | Fix Direction |
|---|---|---|---|---|
| **Tech** | Staging environment has only ~1% of production data volume | Staging DB size vs prod DB size | Cost and maintenance constraints; staging was "good enough" for functional testing historically | Create a prod-representative staging tier for migration testing, or add a synthetic data-volume test step |
| **Tech** | No automated migration dry-run or shadow-run against prod-scale data | CI pipeline config | Migrations passed functional tests; performance testing at scale was not part of the pipeline | Add a migration validation step that tests against prod-scale data or a sampled copy |
| **Process** | Rollback playbook was outdated and did not cover recent migration patterns | Playbook document (last modified date TBD) | Playbooks are written once and rarely updated; no ownership or review cadence existed | Assign playbook ownership; add "playbook freshness" check to deploy checklist |
| **Process** | Incident commander role was undefined for this type of incident | Incident response policy (or lack thereof) | The team had informal escalation habits that worked for smaller incidents; formal IC rotation was not established | Define IC rotation and on-call escalation policy with clear declaration protocol |
| **People** | On-call engineer had to investigate + coordinate + escalate simultaneously without IC support | On-call schedule, Slack thread | Single on-call was standard practice; IC role was assumed to be implicit | Separate on-call responder role from IC role; ensure IC is declared within first 10 minutes of any S1+ incident |
| **Comms** | No proactive customer communication during the 90-minute outage | Customer support logs (to confirm) | No status page update protocol tied to payment incidents; team was focused on fix, not comms | Add a "customer comms" step to the incident response checklist triggered at S1/S2 severity |
| **Environment** | Production data volume grew significantly since staging was last calibrated | Data growth metrics (hypothesis) | Data growth was organic and incremental; no one was tracking the staging-to-prod data ratio | Add a quarterly staging-vs-prod data parity check |

### 5-Whys Analysis: Top Contributing Factor -- Migration Passed Staging but Failed in Production

1. **Why did the migration fail in production?**
   Because the migration triggered table locks and long-running queries on a high-volume table that caused timeouts in the payments API.

2. **Why didn't we catch this in staging?**
   Because staging only contains ~1% of production data, so the migration completed quickly and did not trigger the same locking/timeout behavior.

3. **Why does staging have only 1% of production data?**
   Because there is no process or tooling to maintain a production-representative data volume in staging. The staging environment was set up for functional correctness, not performance validation.

4. **Why is there no production-representative testing for migrations?**
   Because migration testing was treated as a pass/fail functional check in CI, and performance testing at scale was not part of the migration approval process. The risk of data-volume-dependent failures was not surfaced in any checklist or review.

5. **Why was this risk not surfaced in any review process?**
   Because the migration review process focused on schema correctness and backward compatibility, not on execution performance at scale. There was no checklist item or automated gate that required scale testing for migrations affecting high-traffic tables.

### 5-Whys Analysis: Second Contributing Factor -- Incident Response Delays

1. **Why did it take 30 minutes to escalate?**
   Because the on-call engineer was simultaneously investigating the root cause, attempting remediation, and trying to coordinate with others -- without a designated incident commander.

2. **Why was there no incident commander?**
   Because the IC role was not formally defined in the team's incident response process. Historically, the on-call engineer informally played all roles.

3. **Why was the IC role not formally defined?**
   Because previous incidents were smaller and resolved quickly by the on-call engineer alone. The informal process "worked" until this incident exceeded one person's capacity.

4. **Why did this incident exceed one person's capacity?**
   Because the rollback playbook was outdated, so the engineer could not follow a known-good procedure and had to debug in real time while also coordinating.

5. **Why was the rollback playbook outdated?**
   Because playbooks have no assigned owner, no review cadence, and no freshness check in the deploy process. They are written at creation time and then forgotten.

### Root Cause Hypotheses

1. **The migration validation pipeline lacks a production-scale testing gate.** Migrations are validated only for functional correctness against a small dataset, allowing performance and locking issues to reach production undetected. (Confidence: **high**)

2. **The incident response process lacks formal role definitions and escalation triggers, causing coordination overhead that extends resolution time.** The absence of a declared IC role and an up-to-date rollback playbook turned a recoverable issue into a 90-minute outage. (Confidence: **high**)

3. **Staging environment drift from production is unmonitored.** As production data grew, the gap between staging and production widened without anyone tracking or flagging the divergence. (Confidence: **medium** -- needs data growth metrics to confirm)

---

## 4) Learnings + Decisions

### Learnings

1. **Learning:** We learned that functional test coverage in staging is necessary but not sufficient for database migrations -- performance and locking behavior at production scale can be qualitatively different.
   - **Evidence:** Migration passed all staging tests but caused table locks and timeouts on production's larger dataset.
   - **Implication:** We need a migration validation step that accounts for data volume and concurrency at production scale.

2. **Learning:** We learned that our incident response process relies on implicit role assignment that breaks down when an incident requires more than one person.
   - **Evidence:** 20+ minutes of confusion over IC ownership; on-call engineer was overloaded with investigation + coordination + escalation simultaneously.
   - **Implication:** We need an explicit IC declaration protocol triggered at S1/S2 severity, separate from the on-call responder role.

3. **Learning:** We learned that rollback playbooks become outdated silently and are only discovered to be inadequate during an incident -- the worst possible time.
   - **Evidence:** On-call engineer attempted to follow playbook at ~14:25 and found it did not cover the current migration pattern.
   - **Implication:** Playbooks need an owner, a regular review cadence, and a "last validated" date checked before deploy.

4. **Learning:** We learned that we had no proactive customer communication protocol tied to payment-affecting incidents, leaving ~2,000 affected customers without status updates.
   - **Evidence:** No status page update was posted during the 90-minute outage (to be confirmed with support team).
   - **Implication:** The incident response checklist should include a customer communication step triggered at the same time as IC declaration.

5. **Learning:** We learned that staging environment parity with production is a drifting metric that no one owns -- it erodes gradually until it causes a failure.
   - **Evidence:** Staging has ~1% of production data; the ratio has likely worsened over time as production grew.
   - **Implication:** We need a periodic parity check and an alert when staging drift exceeds a defined threshold.

### Decisions (with Tradeoffs)

1. **Decision:** Implement a migration dry-run step that tests migrations against a production-scale dataset (sampled or synthetic) before production deployment.
   - **Why:** Learning #1 -- functional tests alone missed a critical performance failure.
   - **Tradeoffs:** Increases migration deploy time; requires infrastructure investment (prod-scale test DB or shadow run tooling); may slow down low-risk migrations.
   - **Owner:** Platform/Infra Lead

2. **Decision:** Define and publish an incident response policy with formal IC rotation, declaration protocol (within 10 min of S1/S2), and escalation triggers.
   - **Why:** Learning #2 -- implicit roles caused 20+ minutes of coordination overhead.
   - **Tradeoffs:** Adds process overhead to smaller incidents; requires training and practice drills.
   - **Owner:** Engineering Manager, Payments Team

3. **Decision:** Assign ownership of all critical runbooks/playbooks and institute a quarterly review cadence with a "last validated" date visible in each doc.
   - **Why:** Learning #3 -- outdated playbook extended resolution time.
   - **Tradeoffs:** Ongoing maintenance cost; requires someone to own the review process.
   - **Owner:** On-call Program Owner (to be designated)

4. **Decision:** Add customer communication as a required step in the S1/S2 incident response checklist, with a status page update template ready to publish within 15 minutes of IC declaration.
   - **Why:** Learning #4 -- customers received no proactive communication.
   - **Tradeoffs:** Requires coordination with comms/support team; risk of premature or inaccurate updates if triggered too early.
   - **Owner:** Product Manager, Payments + Comms Lead

---

## 5) Action Tracker

| # | Action | Type | Owner | Due Date | Success Signal | Follow-up Date | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Build a migration dry-run pipeline step that validates migrations against a prod-representative dataset (sampled copy or synthetic scale) | Guardrail | Platform/Infra Lead | 2026-04-14 | All migrations to high-traffic tables pass a scale test gate before prod deploy; no prod migration failures due to data volume in next quarter | 2026-04-21 | May require a new staging-prod dataset; evaluate cost of maintaining a sampled prod DB |
| 2 | Write and publish incident response policy: IC rotation, declaration protocol (within 10 min of S1/S2), escalation matrix, role definitions | Process | Engineering Manager, Payments | 2026-03-31 | Policy published in internal wiki; all on-call engineers have read and acknowledged; next S1/S2 incident has IC declared within 10 min | 2026-04-07 | Run a tabletop drill within 2 weeks of publication |
| 3 | Assign owners to all critical playbooks (payments rollback, DB migration rollback, API failover); update each to cover current patterns | Process | On-call Program Owner (TBD -- assign by 2026-03-24) | 2026-04-07 | All critical playbooks have a named owner, a "last validated" date within the past quarter, and coverage for current migration patterns | 2026-04-14 | Set a quarterly calendar reminder for playbook review |
| 4 | Add customer communication step to S1/S2 incident checklist; create status page update template | Process | PM, Payments + Comms Lead | 2026-03-31 | S1/S2 checklist includes comms step; status page template exists and was used in next qualifying incident | 2026-04-14 | Coordinate with support team for escalation-to-comms handoff |
| 5 | Quantify the revenue impact of this outage (~2,000 transactions) and reconcile customer-facing effects (failed charges, duplicates) | Fix (immediate) | Payments Team Lead | 2026-03-21 | Revenue impact documented; affected customers identified; remediation actions (refunds, retries) completed | 2026-03-24 | Partner with finance and support |
| 6 | Implement quarterly staging-vs-prod data parity check; set alert threshold at >10x divergence | Instrumentation | Platform/Infra Lead | 2026-04-30 | Automated parity check running quarterly; alert fires if staging data volume falls below 10% of prod for key tables | 2026-05-07 | Start with payments-critical tables; expand to other services later |
| 7 | Run a tabletop incident response drill using this incident scenario to validate the new IC policy | Training | Engineering Manager, Payments | 2026-04-14 | Drill completed; IC was declared within protocol; debrief notes captured | 2026-04-21 | Schedule within 2 weeks of policy publication |

**Parked ideas (revisit next quarter):**
- Full staging data refresh pipeline (expensive; evaluate after migration dry-run is in place)
- Automated rollback for failed migrations (complex; needs architectural review)
- Canary deployment for database migrations (worth exploring after dry-run pipeline is proven)

---

## 6) Kill Criteria / Triggers

| Signal (Observable) | Window | Trigger Threshold | Committed Action | Owner | Evidence Source |
|---|---|---|---|---|---|
| Another production migration failure caused by data volume difference | 90 days after dry-run pipeline ships | 1 or more occurrences | Halt all non-critical migrations; escalate to VP Engineering for infrastructure investment decision | Platform/Infra Lead | Incident log, production error dashboard |
| IC is not declared within 10 minutes on an S1/S2 incident | 60 days after IC policy ships | 2 or more occurrences | Mandatory incident response re-training for all on-call engineers within 2 weeks; review IC policy for gaps | Engineering Manager, Payments | PagerDuty + Slack incident channel timestamps |
| Critical playbooks are found outdated (>90 days since last validation) during an incident | Ongoing after playbook ownership is assigned | 1 occurrence | Freeze deploys for the affected system until playbook is updated and validated; assign backup owner | On-call Program Owner | Playbook "last validated" dates, incident debrief notes |
| Customer-impacting S1/S2 incident occurs without status page update within 15 minutes of IC declaration | 60 days after comms step is added to checklist | 1 occurrence | Retrospective on comms process gap; add automated status page trigger to alerting pipeline | PM, Payments + Comms Lead | Status page update log, incident timeline |
| Staging-to-prod data ratio drops below 5% for any payments-critical table | Ongoing after parity check ships | Threshold breach | Block migrations to affected tables until staging data is refreshed | Platform/Infra Lead | Automated parity check dashboard |

---

## 7) Dissemination Plan

### 1-Page Shareout (for Engineering + Leadership)

**TL;DR:**
- **What happened:** A database migration passed staging but failed in production due to a 100x data volume difference, causing a 90-minute outage in the payments API affecting ~2,000 transactions.
- **What we learned:** Our migration validation pipeline lacks production-scale testing; our incident response process has no formal IC role; our rollback playbooks are outdated and unowned.
- **What changed:** We are building a prod-scale migration dry-run gate (due April 14), publishing a formal IC policy (due March 31), assigning playbook owners with quarterly review cadence (due April 7), and adding customer comms to the incident checklist (due March 31).

**Top 3 Actions (with owners + dates):**
1. Build migration dry-run pipeline against prod-scale data -- Platform/Infra Lead -- 2026-04-14
2. Publish IC rotation + declaration policy for S1/S2 incidents -- Engineering Manager, Payments -- 2026-03-31
3. Assign playbook owners and update all critical playbooks -- On-call Program Owner (TBD) -- 2026-04-07

**Where to find the full doc:** [Link to this post-mortem document in internal wiki -- to be published]

**Distribution:**
- Engineering team: Share in #engineering Slack channel and team all-hands (week of 2026-03-17)
- Engineering leadership: Present 1-page shareout in next leadership sync (week of 2026-03-17)
- Broader engineering org: Add to internal "Incident Learnings" wiki page

### Impact & Learnings Review (Recurring Ritual)

- **Cadence:** Biweekly for the first 8 weeks (to track action item completion), then monthly
- **Attendees:** Engineering Manager (Payments), Platform/Infra Lead, On-call Program Owner, PM (Payments)
- **Inputs:** This post-mortem doc, action tracker status, incident log for new incidents, migration dry-run pipeline metrics
- **Agenda:**
  1. Status of open action items from this post-mortem (10 min)
  2. Any new incidents or near-misses related to these factors? (10 min)
  3. What has changed / what did we learn since last review? (5 min)
  4. Decisions or escalations needed (5 min)
- **Owner:** Engineering Manager, Payments Team

---

## 8) Risks / Open Questions / Next Steps

### Risks
- **Revenue impact may be larger than estimated.** The ~2,000 transaction figure is preliminary; duplicate charges or downstream fulfillment failures could increase financial and reputational exposure. Quantification (Action #5) is due 2026-03-21.
- **On-call Program Owner is not yet designated.** Action #3 (playbook ownership) depends on this role being assigned by 2026-03-24. If unassigned, playbooks remain unowned.
- **Migration dry-run pipeline may be complex to build.** Maintaining a prod-representative dataset for testing has infrastructure cost and data privacy implications. If blocked, a manual scale-test checklist for high-risk migrations should be implemented as an interim measure.
- **Cultural adoption of IC protocol.** Publishing a policy is insufficient; engineers need practice (hence Action #7, tabletop drill). Without adoption, the policy is shelf-ware.

### Open Questions
1. What is the exact financial impact of the ~2,000 affected transactions? Were any charges duplicated? (Owner: Payments Team Lead, by 2026-03-21)
2. When was the rollback playbook last updated, and how many other critical playbooks are similarly outdated? (Owner: On-call Program Owner, by 2026-03-31)
3. What is the actual current staging-to-production data ratio for key tables? Has it been worsening over time? (Owner: Platform/Infra Lead, by 2026-03-24)
4. Were any external SLA commitments breached with payment processor partners? (Owner: PM, Payments, by 2026-03-24)
5. Did automated alerting fire at the right threshold and time, or is there a detection gap to address? (Owner: On-call engineer, by 2026-03-21)

### Next Steps
1. **This week (by 2026-03-21):** Quantify revenue impact (Action #5); answer open questions #3 and #5; designate On-call Program Owner.
2. **Next week (by 2026-03-28):** Begin drafting IC policy (Action #2); begin playbook audit (Action #3); share 1-page shareout with engineering and leadership.
3. **By end of March:** Publish IC policy (Action #2); publish customer comms checklist (Action #4); complete playbook updates (Action #3).
4. **By mid-April:** Ship migration dry-run pipeline (Action #1); run tabletop drill (Action #7).
5. **By end of April:** Ship staging parity check (Action #6); hold first biweekly Impact & Learnings Review.

---

## Quality Gate: Self-Assessment Against Rubric

| Dimension | Score | Rationale |
|---|---|---|
| 1) Clarity of scope and safety | **2** | Goal is explicit (learning + prevention); blameless norms established; facilitator/scribe/decision owner roles assigned; audience defined (engineering + leadership) |
| 2) Evidence and timeline quality | **2** | Timestamped timeline with evidence links; facts vs hypotheses are explicitly labeled throughout; impact is quantified (~2,000 transactions, 90 min duration) |
| 3) Systems thinking (contributing factors) | **2** | Multi-factor analysis across Tech/Process/People/Comms/Environment clusters; "why it made sense" captured for each factor; two full 5-Whys chains (5 levels each) on top factors |
| 4) Decisions and actionability | **2** | 7 concrete actions with owner, due date, success signal, and follow-up date; top actions directly address top contributing factors; "later ideas" are explicitly parked |
| 5) Learning dissemination | **2** | 1-page TL;DR shareout with top 3 actions; recurring biweekly Impact & Learnings Review with owner, inputs, attendees, and agenda |
| 6) Kill criteria / triggers | **2** | 5 observable signals with specific thresholds and pre-committed actions (halt, retrain, freeze, block); ownership is clear for each |
| **Total** | **12/12** | Ship as-is |

### Checklist Verification

**Prep checklist:**
- [x] Review type is clear (incident)
- [x] Facilitator, scribe, and decision owner are assigned
- [x] Attendees are the people with the best evidence
- [x] Pre-reads/evidence links are collected
- [x] Stated goal is learning + improvement (not blame)
- [x] Privacy constraints handled (no individual names used)

**Output quality checklist:**
- [x] Includes: brief + agenda, impact snapshot, timeline, contributing factors, decisions, action tracker
- [x] Top contributing factors map to top action items
- [x] Action items have owner + due date + success signal + follow-up date
- [x] Kill criteria have committed actions (not "we'll discuss")
- [x] Language is blameless and system-focused
- [x] Doc includes 1-page shareout and dissemination plan
- [x] Includes Risks / Open questions / Next steps
