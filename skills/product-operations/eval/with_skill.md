# Product Ops Operating System Pack

**Prepared for:** Product organization with 8 PMs, rapid shipping cadence, and stakeholder visibility gaps

---

## 0) Context Snapshot

- **Company/product:** Mid-stage product org (assumed B2B SaaS) shipping frequently across multiple product areas.
- **Org stage:** 8 PMs, likely 4-6 product pods, scaling past the point where informal coordination works.
- **Top frictions (ranked):**
  1. **No visibility:** Stakeholders (Sales, CS, Support, leadership) don't know what's shipping or when.
  2. **Surprise launches:** Releases land without enablement; Support/Sales learn about changes from customers.
  3. **Ad-hoc status requests:** PMs spend excessive time answering "what's the status of X?" pings from across the org.
- **Desired outcomes (30-90 days):** Stakeholders have predictable access to what's shipping and when; Support/Sales are never surprised by a launch; PMs reclaim time lost to ad-hoc status updates.
- **Stakeholders + decision owners:** Head of Product (decision owner for cadences), Eng leads (release coordination), Sales leadership (pipeline/positioning), CS leadership (customer impact), Support leadership (readiness/deflection), Data/Analytics (metrics, dashboards).
- **Current cadence + artifacts:** Assumed informal -- sporadic Slack updates, inconsistent roadmap docs, no standard release comms. No formal planning cadence beyond quarterly OKR setting.
- **Tooling constraints:** Assumed standard stack (Jira or Linear for tracking, Slack for comms, Notion or Confluence for docs). No custom dashboards.
- **Assumptions / unknowns:**
  - No dedicated Product Ops person exists yet; this pack assumes Product Ops is being stood up for the first time.
  - No regulated/compliance constraints assumed. If present, release tiering would need additional gates.
  - Org is shipping weekly or more frequently (inferred from "rapid shipping").

**Problem statement:** Product Ops exists to reduce stakeholder surprise and status-request overhead, and to improve cross-functional visibility and launch readiness for an 8-PM product team shipping at high velocity.

---

## 1) Product Ops Charter

**Mission:** Build and maintain the operating systems that give the product org and its cross-functional partners predictable visibility into what's shipping, when, and what it means for them -- so PMs can focus on product outcomes, not coordination overhead.

**Primary customer(s):** PMs (reduce coordination burden), Head of Product (org-wide visibility), cross-functional partners (Sales, CS, Support, Eng leadership).

**What we own (scope):**
- Operating cadence design and stewardship (rituals, agendas, calendar)
- Standard artifact templates (product updates, roadmap views, launch briefs)
- Insights pipeline: intake, triage, and routing of cross-functional feedback to product area owners
- Release enablement process: readiness checks, internal comms, training materials, post-launch capture
- Reporting and dashboards that surface status without requiring ad-hoc asks

**What we do NOT own (non-goals):**
- Product strategy, vision, or prioritization decisions (PMs and Head of Product retain these)
- Roadmap content -- we standardize the format and cadence, not what goes on the roadmap
- Individual feature specifications or PRDs
- Customer research methodology or user interviews
- Engineering process (sprint planning, code review, CI/CD)

**Product Ops informs decisions; PMs keep decision rights.** Product Ops provides better inputs, clearer artifacts, and smoother processes. It does not become a shadow PM org or a bottleneck for shipping.

**Engagement model (how to work with us):**
- **Intake channel:** #product-ops Slack channel for requests; async form for non-urgent process improvement ideas.
- **Prioritization:** Product Ops triages weekly; work is prioritized against the current quarter's top friction points.
- **SLAs:** Launch enablement requests require 5 business days lead time for Tier 2 (Medium) and 10 business days for Tier 3 (High) releases.

**Success metrics (measurable at 90 days):**
1. Stakeholder surprise score: <10% of releases flagged as "I didn't know this was coming" by Sales/CS/Support (survey or retro data).
2. Ad-hoc status request volume: 50%+ reduction in "what's the status of X?" pings in Slack (measured via sample audit).
3. Launch enablement coverage: 100% of Tier 2 and Tier 3 releases have an enablement bundle published before launch.
4. PM satisfaction: PMs report reduced coordination overhead (quarterly pulse survey, target: >70% agree).
5. Ritual adoption: >80% attendance and artifact completion rate for core cadences by Day 90.

**Key risks:**
- Product Ops scope creep into product strategy/prioritization.
- PM resistance to new templates if perceived as bureaucratic overhead.
- Under-resourcing: if no dedicated person is assigned, the system stalls.

---

## 2) Operating Model + RACI

### Operating model

- **Model:** Centralized (one Product Ops function serving all 8 PMs and cross-functional partners). Rationale: the core problems (visibility, surprise launches) are org-wide, not isolated to one pod. Centralized ensures consistency.
- **Reporting line(s):** Product Ops reports to Head of Product. Partners closely with Eng leads, Sales Ops, and CS Ops.
- **How work is prioritized:** Product Ops maintains a quarterly "top frictions" list (derived from PM feedback + stakeholder input). All new requests are triaged against this list weekly.
- **Escalation path:** Product Ops lead escalates blockers/conflicts to Head of Product. Cross-functional disputes (e.g., enablement timing vs. release dates) escalate to Head of Product + relevant functional lead.

### RACI table

| Area | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Planning cadence (OKRs/roadmap) | Product Ops (facilitation) | Head of Product | PMs, Eng leads | Sales, CS, Support |
| Weekly product update | PMs (content) | Product Ops (aggregation + distribution) | Eng leads | Sales, CS, Support, Exec team |
| Roadmap updates (stakeholder-facing) | Product Ops (format + distribution) | Head of Product | PMs | Sales, CS, Support |
| Release readiness + enablement | Product Ops (process + bundle) | PM (ship decision) | Eng lead, QA, Support, Sales | CS, Marketing |
| Insights intake + routing | Product Ops (triage + routing) | Product Ops lead | CS, Sales, Support, Data | PMs (receiving routed insights) |
| Decision log stewardship | Product Ops (maintenance) | PM (decision owner) | Eng lead | Stakeholders |
| Post-launch capture + retro | Product Ops (facilitation) | PM | Eng, Support, Sales | Head of Product |

---

## 3) Cadence Calendar (Rituals That Produce Artifacts)

| Cadence | Ritual | Purpose | Owner | Attendees | Output Artifact | Time |
|---|---|---|---|---|---|---|
| Weekly | Product Update | Give stakeholders a single, predictable source of "what shipped, what's next, what's at risk" | Product Ops | PMs (contributors), Sales/CS/Support/Eng leads (consumers) | Weekly Product Update (written, distributed async) | 30 min prep by each PM; Product Ops aggregates + publishes by Thursday 4pm |
| Biweekly | Roadmap Review | Align on roadmap changes, surface dependencies, update stakeholder-facing roadmap view | Head of Product | PMs, Eng leads, Product Ops | Updated roadmap artifact + decision log entries | 45 min, alternating weeks |
| Per-release | Launch Readiness Check | Confirm enablement bundle is complete and all stakeholders are prepared before Tier 2/3 releases ship | Product Ops | PM (owner), Eng lead, Support, Sales | Readiness sign-off (go/no-go) + published enablement bundle | 30 min (async for Tier 1) |
| Monthly | Insights Review | Review routed feedback themes, assign owners, decide what enters the planning backlog | Product Ops | PMs, CS lead, Support lead, Data | Insights Digest with actions + owners | 45 min |
| Quarterly | Planning/QBR | Set quarterly priorities, review Product Ops effectiveness, update friction list | Head of Product | PMs, Eng leads, Sales/CS/Support leads, Product Ops | Quarterly plan + Product Ops retrospective + updated friction list | Half-day |

### Ritual Spec: Weekly Product Update

- **Purpose:** Eliminate ad-hoc status pings by providing a single, predictable, written update each week.
- **Inputs:** Each PM submits a 5-bullet update (wins/shipped, what's next, risks/asks, metrics snapshot, links) by Thursday 2pm.
- **Agenda:** No meeting. Product Ops aggregates, adds a "cross-cutting" section (dependencies, upcoming launches), and publishes to #product-updates and email by Thursday 4pm.
- **Decisions made:** None directly; flags surface in roadmap review or async threads.
- **Output artifact:** Weekly Product Update (Slack post + Notion/Confluence page).
- **Follow-ups + owners:** Flagged risks assigned to PM + Eng lead for resolution.

### Ritual Spec: Biweekly Roadmap Review

- **Purpose:** Catch roadmap drift early, surface cross-pod dependencies, update stakeholder-facing roadmap.
- **Inputs:** Current roadmap artifact, OKR tracker, dependency flags from PMs.
- **Agenda (45 min):**
  - [5 min] Product Ops: highlight changes since last review, new dependencies.
  - [25 min] PMs: walk through changes to their area (2-3 min each, focus on what changed and why).
  - [10 min] Decisions: what moves, what's at risk, what stakeholders need to know.
  - [5 min] Action items + owners.
- **Decisions made:** Roadmap changes ratified; dependency resolutions assigned.
- **Output artifact:** Updated roadmap artifact + decision log entries.
- **Follow-ups + owners:** Product Ops publishes updated stakeholder roadmap view within 24 hours.

### Ritual Spec: Launch Readiness Check

- **Purpose:** Ensure no release surprises downstream partners. Confirm enablement materials are ready before go-live.
- **Inputs:** Enablement bundle draft, release notes, Support/Sales readiness confirmation.
- **Agenda (30 min for Tier 2/3; async checklist for Tier 1):**
  - [5 min] PM: what's changing, who's impacted.
  - [10 min] Support/Sales: readiness check -- do you have what you need?
  - [5 min] Eng: monitoring, rollback readiness.
  - [10 min] Go/no-go decision + action items.
- **Decisions made:** Ship/hold/delay.
- **Output artifact:** Readiness sign-off + published enablement bundle.
- **Follow-ups + owners:** PM owns ship decision; Product Ops publishes enablement bundle to all stakeholders.

### Ritual Spec: Monthly Insights Review

- **Purpose:** Turn accumulated customer/stakeholder feedback into prioritized, owned action items.
- **Inputs:** Insights Digest (prepared by Product Ops from pipeline), top themes with evidence.
- **Agenda (45 min):**
  - [10 min] Product Ops: present top 5 themes with evidence (volume, severity, segments).
  - [20 min] Discussion: which themes need action, which are already addressed, which need more data.
  - [15 min] Assign owners + decide next steps (backlog, research, planning input).
- **Decisions made:** Theme ownership assigned; items flagged for quarterly planning.
- **Output artifact:** Insights Digest with actions + owners.
- **Follow-ups + owners:** Product Ops tracks action completion; unresolved items escalate to next review.

---

## 4) Standard Artifact Library

### Artifact List

| Artifact | Primary Audience | Owner | Cadence | Definition of Done |
|---|---|---|---|---|
| Weekly Product Update | Sales, CS, Support, Eng leads, Exec | Product Ops (aggregation); PMs (content) | Weekly (Thursday) | All PMs contributed; cross-cutting section included; published to #product-updates + email |
| Stakeholder Roadmap View | Sales, CS, Support, Exec | Product Ops (format); Head of Product (content) | Updated biweekly after roadmap review | Current quarter + next quarter view; dates are ranges, not commitments; stakeholder-friendly language |
| Decision Log | PMs, Eng leads, Head of Product | Product Ops (stewardship); PM (entries) | Continuous; reviewed biweekly | Every significant product decision has context, options, rationale, owner, and review date |
| Launch Enablement Bundle | Support, Sales, CS, Marketing | Product Ops (process); PM (content) | Per-release (Tier 2/3) | All sections complete; Support/Sales confirmed readiness; published 2+ days before launch |
| Insights Digest | PMs, Head of Product | Product Ops | Monthly | Top 5 themes with evidence; owner assigned; decision path identified |

### Weekly Product Update (Template)

```
# Weekly Product Update — [Date]

## Org-wide highlights (Product Ops)
- Key launches this week:
- Upcoming launches (next 2 weeks):
- Cross-cutting risks/dependencies:

## [Product Area 1] — [PM Name]
- Wins / shipped:
- What's next:
- Risks / asks:
- Metrics snapshot:
- Links (PRDs/specs/notes):

## [Product Area 2] — [PM Name]
(same structure)

## [Repeat for each product area]
```

### Decision Log (Template)

| Date | Decision | Context | Options Considered | Rationale | Owner | Review Date |
|---|---|---|---|---|---|---|
| | | | | | | |

### Launch Enablement Bundle (Template)

```
# Launch Enablement Bundle — [Feature/Release Name]

## Release tier: [Low / Medium / High]
## Target launch date: [Date]
## PM owner: [Name]

### What changed (1 paragraph)
[Plain-language summary of the change and why it matters.]

### Who's impacted (eligibility/segments)
- Customer segments:
- Internal teams:

### How it works (user steps)
1.
2.
3.

### FAQs + edge cases
- Q:
  A:

### Support macros / troubleshooting
- Scenario:
  Resolution:

### Sales talk track (if relevant)
- Positioning:
- Key objection handling:

### Monitoring + guardrails
- Key metrics to watch:
- Alert thresholds:
- Dashboard link:

### Rollback / mitigation
- Rollback procedure:
- Rollback owner:
- Decision criteria for rollback:

### Owner + escalation
- PM: [Name]
- Eng: [Name]
- Escalation: [Name/channel]
```

---

## 5) Insights Pipeline

### Sources

| Source | Channel | Volume (est.) | Signal Quality | Owner |
|---|---|---|---|---|
| CS/Sales notes | CRM notes, Slack #customer-feedback | Medium | Mixed (anecdotal + pattern) | CS Ops / Sales Ops |
| Support tickets | Help desk (Zendesk/Intercom) | High | Good (tagged, measurable) | Support lead |
| Product analytics | Analytics platform (Amplitude/Mixpanel) | High | Good (quantitative) | Data/Analytics |
| Research/interviews | Research repo, interview notes | Low | High (structured) | PM / UX Research |
| Community/social/reviews | G2, social, community forums | Low | Mixed | Marketing / Product Ops |

### Taxonomy (minimal)

| Field | Example Values |
|---|---|
| Theme | onboarding, activation, reliability, pricing, feature-gap, UX-friction, performance |
| Segment | SMB, mid-market, enterprise, new-user, power-user |
| Severity | Low (nice-to-have), Medium (workaround exists), High (blocking/churning) |
| Evidence type | Quote, ticket volume, metric change, churned account, NPS verbatim |
| Product area | [Area 1], [Area 2], ... (map to PM ownership) |

### Intake, Triage, Routing

| Stage | Owner | Input | Output | Cadence |
|---|---|---|---|---|
| **Intake** | Product Ops | Raw feedback from all sources | Tagged items in insights backlog (theme, segment, severity, evidence, product area) | Continuous; batch processing 2x/week |
| **Triage** | Product Ops | Tagged insights backlog | Prioritized themes (top 5-10) with evidence summaries | Weekly (internal Product Ops review) |
| **Routing** | Product Ops | Prioritized themes | Routed to product area PM owner with context + evidence | Weekly (async Slack or email notification to PM) |
| **Reporting** | Product Ops | Routed + resolved items | Monthly Insights Digest (top themes, evidence, actions, owners) | Monthly (feeds into Monthly Insights Review ritual) |

### Decision path for routed insights

1. PM receives routed insight with evidence.
2. PM decides: (a) add to backlog, (b) needs more research, (c) already addressed, (d) won't do (with rationale).
3. Product Ops tracks disposition. Unresolved high-severity items escalate to Monthly Insights Review.
4. Patterns that span multiple product areas surface in Biweekly Roadmap Review for Head of Product visibility.

---

## 6) Release Enablement System

### Release Tiering

| Tier | Examples | Required Steps | Owner(s) |
|---|---|---|---|
| **Tier 1 (Low)** | UI copy change, minor bug fix, backend optimization invisible to users | PM updates weekly product update; no enablement bundle needed | PM |
| **Tier 2 (Medium)** | New feature behind flag, workflow change, pricing change for subset, API change | Enablement bundle (lite); Slack announcement to Support + Sales; readiness check (async) | PM + Product Ops |
| **Tier 3 (High)** | GA launch, migration, breaking change, pricing overhaul, major UX redesign | Full enablement bundle; Launch Readiness Check meeting; training session for Support/Sales; post-launch capture | PM + Product Ops + Eng lead |

### Enablement Workflow

```
[PM assigns tier] --> [Tier 1: update weekly product update, done]
                  --> [Tier 2/3: PM drafts enablement bundle]
                      --> [Product Ops reviews + distributes 5 days before (T2) / 10 days before (T3)]
                      --> [Support/Sales confirm readiness]
                      --> [T2: async go/no-go | T3: Launch Readiness Check meeting]
                      --> [Launch]
                      --> [Post-launch capture: Day 3 check-in, Day 14 retro]
```

### Post-Launch Capture

For every Tier 2/3 release, Product Ops facilitates a lightweight post-launch capture:

- **Day 3 check-in (async):** PM + Support report any early issues (support ticket spike, unexpected behavior, customer confusion). Quick Slack thread in #product-ops.
- **Day 14 retro (15-min sync for Tier 3; async for Tier 2):**
  - What went well in the launch process?
  - What surprised us (customers, Support, Sales)?
  - What should we change in the enablement process?
  - Outcome: 1-3 action items for Product Ops to improve the system.

---

## 7) 30/60/90 Implementation Plan

| Timebox | Goal | Scope | Deliverables | Pilot Area | Metrics | Risks |
|---|---|---|---|---|---|---|
| **0-30 days** | Foundation + quick win | Stand up weekly product update + launch enablement for 1 pod | Published charter; weekly product update running (all 8 PMs); enablement bundle template published; 1 Tier 2/3 release uses the enablement process | Pilot pod: highest-shipping product area (most launch surprises) | Weekly update published on time 4/4 weeks; pilot pod enablement bundle completed for 1+ release; baseline stakeholder surprise survey sent | PM resistance to weekly update template; no dedicated Product Ops person assigned |
| **31-60 days** | Cadence + insights | Add biweekly roadmap review + insights pipeline intake | Biweekly roadmap review running; insights intake + triage operational; decision log template in use; stakeholder roadmap view published | Expand enablement to all Tier 2/3 releases org-wide | 50%+ reduction in ad-hoc status pings (sample audit); all Tier 2/3 releases have enablement bundles; roadmap review attendance >80% | Roadmap review becomes "status theater" if not well-facilitated; insights intake overwhelms Product Ops without clear triage |
| **61-90 days** | Full system + measure | Monthly insights review live; post-launch capture active; full system operational | First Monthly Insights Review completed; post-launch capture running for all Tier 2/3; 90-day retrospective on Product Ops effectiveness; updated friction list for Q2 | Full org (all 8 PMs, all cross-functional partners) | Stakeholder surprise score <10%; PM satisfaction >70% (coordination overhead reduced); insights review producing owned action items; enablement coverage 100% for Tier 2/3 | System fatigue if too many rituals introduced at once; need to prune anything that isn't producing value |

### Measurement Plan

| Metric | Baseline (Day 0) | Target (Day 90) | How Measured |
|---|---|---|---|
| Stakeholder surprise score | Not measured (assumed high, given complaints) | <10% of releases flagged as surprise | Post-release survey to Sales/CS/Support: "Were you aware of this release before it shipped?" |
| Ad-hoc status request volume | High (qualitative) | 50%+ reduction | Sample audit: count "what's the status of X?" messages in key Slack channels, Week 1 vs. Week 10 |
| Launch enablement coverage (Tier 2/3) | 0% (no process exists) | 100% | Tracker: did every Tier 2/3 release have a published enablement bundle before launch? |
| PM coordination overhead | High (qualitative) | >70% report improvement | Quarterly pulse survey: "Product Ops has reduced the time I spend on coordination and status updates" |
| Ritual adoption (attendance + artifact completion) | N/A | >80% | Attendance tracking + artifact publication log |

### Iteration Loop

- **Week 4:** Retrospective with pilot pod PMs -- what's working, what's overhead, what to adjust.
- **Week 8:** Retrospective with cross-functional partners -- are surprises decreasing? What's still missing?
- **Week 12 (Day 90):** Full Product Ops retrospective. Update charter, prune rituals that aren't earning their keep, update friction list, plan Q2 focus areas.

---

## 8) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **No dedicated Product Ops person assigned.** The system requires someone to own aggregation, triage, facilitation, and enablement. Without a named owner, it will decay within weeks. | High | High | Head of Product must assign a named owner (full-time or significant part-time) before Day 1. If no dedicated hire, designate an existing PM or Chief of Staff with at least 50% allocation. |
| **PM resistance to templates.** PMs may see weekly updates and enablement bundles as busywork, especially if they're already shipping fast. | Medium | Medium | Start minimal (5-bullet update, <10 min). Demonstrate value quickly by showing stakeholders stop pinging PMs for status. Iterate on template based on PM feedback at Week 4 retro. |
| **Process for process's sake.** Adding cadences without tying each to a specific friction point. | Medium | High | Every ritual and artifact must map to one of the top 3 friction points. If it doesn't reduce surprise, status overhead, or enablement gaps, cut it. |
| **Insights pipeline overwhelm.** Too much inbound signal with insufficient triage capacity. | Medium | Medium | Start with Support tickets only (highest volume, most structured). Add CS/Sales feedback in Month 2. Keep taxonomy minimal (5 themes max at launch). |
| **Stakeholder expectations exceed Product Ops scope.** Sales/CS may expect Product Ops to "fix the roadmap" or prioritize their requests. | Medium | Medium | Charter is explicit: Product Ops informs decisions, PMs decide. Reinforce at QBR and in every Insights Review. |

### Open Questions

1. **Who is the Product Ops owner?** Is this a new hire, an existing PM rotating into the role, or a Chief of Staff function? The answer determines Day 0 readiness and scope ambition.
2. **What tooling is in place?** Specific tool choices (Jira vs. Linear, Notion vs. Confluence, Slack workflows vs. email) will shape template formats and automation potential.
3. **Which product area has the most launch surprises?** This determines the pilot pod for the first 30 days. Need data from Support/Sales to confirm.
4. **Are there existing templates or artifacts that PMs are already using?** If yes, standardize around those rather than introducing new formats. Reduces adoption friction.
5. **Is there appetite for a quarterly stakeholder satisfaction survey?** This is the most direct way to measure "fewer surprises" but requires cross-functional buy-in to administer.
6. **Are there compliance or regulatory gates** that should be layered into the release tiering? (Assumed no; confirm.)

### Next Steps

1. **Head of Product:** Confirm the Product Ops owner (person + allocation) and authorize the charter. Target: this week.
2. **Product Ops owner:** Schedule a 30-min kickoff with the pilot pod PM(s) to introduce the weekly update template and get feedback. Target: Week 1.
3. **Product Ops owner:** Send baseline stakeholder surprise survey to Sales, CS, and Support leads ("How often are you surprised by product releases?"). Target: Week 1.
4. **Product Ops owner:** Publish the enablement bundle template to the team wiki and walk through it with the pilot pod PM for the next Tier 2/3 release. Target: Week 1-2.
5. **Product Ops owner:** Set up #product-updates Slack channel (or equivalent) and publish the first Weekly Product Update. Target: end of Week 1.
6. **Head of Product:** Review this pack with Eng leads, Sales, CS, and Support leads. Gather feedback. Adjust charter scope if needed. Target: Week 2.
7. **Week 4 retro:** Product Ops owner facilitates retrospective with pilot pod. Adjust templates, cadence, and scope based on feedback. Decide whether to expand enablement org-wide.

---

## Self-Assessment (Rubric)

| Dimension | Score | Rationale |
|---|---|---|
| 1) Clarity of charter + boundaries | **2** | Charter has scope, non-goals, engagement model, explicit preservation of PM decision rights, and 5 measurable success criteria. |
| 2) Practical operating model | **2** | RACI is complete with named roles for all key areas. Centralized model is justified. Intake, prioritization, and escalation paths are defined. |
| 3) Cadence + artifacts produce decisions | **2** | 5 rituals, each with a named output artifact. Templates provided for all core artifacts. No "just a meeting" entries. |
| 4) Insights pipeline drives action | **2** | Full intake-triage-routing-reporting chain with owners and cadence. Decision path is explicit (PM decides disposition; unresolved items escalate). |
| 5) Implementation + adoption | **2** | 30/60/90 plan with named pilot area, specific metrics with baselines and targets, iteration loop at weeks 4/8/12, and change comms plan. |
| **Total** | **10/10** | Passes the >= 7/10 bar with no dimension at 0. |
