# Organizational Restructuring Plan

## B2B SaaS Analytics Platform (~180 people)

---

## 1. Current State Assessment

### Existing Structure

| Team | Size (est.) | Role |
|------|-------------|------|
| Feature Teams (x5) | ~120 | Build product features end-to-end |
| Platform Team (x1) | ~20 | Shared infrastructure, CI/CD, APIs, SDKs |
| Data Team (x1) | ~18 | Pipelines, warehousing, analytics infrastructure |
| AI/ML Team (x1) | 4 | ML models, AI features, experimentation |
| Leadership / Staff | ~18 | Eng managers, directors, PMs, design, etc. |

### Diagnosed Symptoms

1. **Platform team is a bottleneck.** Feature teams depend on the platform team for infrastructure work, API changes, and shared-service modifications. The platform team cannot absorb all requests, creating a queue that blocks feature delivery.

2. **AI/ML team has no PM and takes requests from everyone.** Without a dedicated PM, the AI/ML team lacks prioritization authority. Every feature team and stakeholder routes requests directly, leading to context-switching, partial work, and no strategic roadmap.

3. **Data team ownership is unclear.** Ambiguity around whether the data team owns data pipelines, analytics dashboards, data governance, customer-facing data features, or some combination. This leads to duplicated work, dropped responsibilities, and cross-team finger-pointing.

---

## 2. Dependency Map

### Current Dependency Graph

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Feature Tm 1 │────▶│              │     │              │
├──────────────┤     │              │     │              │
│ Feature Tm 2 │────▶│   Platform   │     │  Data Team   │
├──────────────┤     │    Team      │◀───▶│  (unclear    │
│ Feature Tm 3 │────▶│  (BOTTLENECK)│     │   ownership) │
├──────────────┤     │              │     │              │
│ Feature Tm 4 │────▶│              │     │              │
├──────────────┤     │              │     │              │
│ Feature Tm 5 │────▶│              │     │              │
└──────────────┘     └──────┬───────┘     └──────┬───────┘
                            │                     │
                            ▼                     ▼
                     ┌──────────────┐
                     │   AI/ML Tm   │
                     │  (no PM,     │
                     │  pulled in   │
                     │  all dirs)   │
                     └──────────────┘
```

### Key Dependency Bottlenecks

| Bottleneck | Blocking Impact | Frequency |
|------------|----------------|-----------|
| Platform team API changes | Feature teams wait 1-3 sprints for platform work | Every sprint |
| Platform team infra provisioning | New services / scaling blocked | Monthly |
| AI/ML prioritization | Features with AI components delayed, AI team thrashes | Continuous |
| Data pipeline changes | Feature teams and AI/ML wait on data team for schema changes, new sources | Bi-weekly |
| Data ownership gaps | Incidents where no team claims ownership of a data flow | Monthly |

### Critical Path for 8-Week Customer Launch

The major customer launch likely touches multiple teams. The critical dependencies are:

```
Customer Launch Feature Scope
        │
        ├── Feature Team(s) building launch features
        │       │
        │       ├── Platform: API changes, scaling, auth
        │       ├── Data: new data pipelines or schema changes
        │       └── AI/ML: ML model integration (if applicable)
        │
        └── Cross-cutting: monitoring, SLAs, performance
```

---

## 3. Restructuring Options

### Option A: Embed & Decentralize (Federation Model)

**Core idea:** Distribute platform and data engineers into feature teams. Keep a thin "core platform" team. Assign the AI/ML team to a single PM.

**Changes:**

- **Platform team (20 people) splits into:**
  - Core Platform (8 people): owns CI/CD, infrastructure-as-code, shared APIs, developer experience. Provides self-service tooling so feature teams do not need to file requests for routine work.
  - 12 platform engineers embed into the 5 feature teams (~2 per team, with 2 remaining as floaters). These embedded engineers handle team-specific infrastructure, API endpoints, and scaling needs directly.

- **Data team (18 people) splits into:**
  - Core Data (6 people): owns data warehouse, governance, shared pipelines, master data model.
  - 12 data engineers embed into feature teams (~2 per team, with 2 remaining as floaters/on-call). Embedded data engineers own their team's data pipelines and analytics.

- **AI/ML team (4 people):**
  - Assigns to the feature team most aligned with the customer launch (or the team with the strongest AI roadmap).
  - One of the existing PMs takes on AI/ML prioritization as part of their portfolio.
  - Post-launch, evaluate whether AI/ML stays embedded or reforms as a shared team with a dedicated PM.

**Pros:**
- Maximizes shipping parallelism: each feature team is nearly self-sufficient.
- Eliminates most cross-team blocking for routine work.
- Clear ownership: if a feature team owns a data pipeline, there is no ambiguity.

**Cons:**
- Risk of divergent infrastructure patterns across teams (inconsistency).
- Core platform/data teams become very small; may struggle with large cross-cutting projects.
- Embedded engineers may feel professionally isolated from their discipline peers.
- Significant change during a critical 8-week window.

---

### Option B: Platform-as-a-Product with Clear Intake (Reinforced Center Model)

**Core idea:** Keep centralized teams but fix the operating model. Platform and data teams operate as internal product teams with SLAs, self-service tooling, and explicit intake processes. AI/ML gets a PM.

**Changes:**

- **Platform team remains centralized (20 people) but restructures internally:**
  - Designates 2 "customer-facing" engineers who act as liaisons to feature teams (rotating quarterly).
  - Builds self-service capabilities aggressively: feature flags, service scaffolding, API gateway config, and monitoring dashboards that feature teams can use without platform tickets.
  - Publishes a quarterly platform roadmap and weekly capacity allocation. Feature teams request time through a transparent intake process with SLAs (e.g., P1 = 48 hours, P2 = 1 sprint, P3 = roadmap consideration).
  - Allocates 30% of capacity to "embedded support" for the top-priority feature team each quarter (currently: the customer launch team).

- **Data team remains centralized (18 people) with explicit ownership charter:**
  - Defines a clear RACI: Data team owns ingestion, transformation, warehouse, and governance. Feature teams own their own analytics dashboards and reporting logic using self-service BI tools.
  - Publishes a data catalog and schema change process.
  - Assigns 2 data engineers as embedded support for the customer launch team for 8 weeks.

- **AI/ML team (4 people):**
  - Gets a part-time PM (an existing PM takes 30-40% allocation to AI/ML).
  - AI/ML team defines a quarterly roadmap; ad-hoc requests go through the PM for prioritization.
  - For the next 8 weeks, AI/ML is 100% allocated to customer launch work (if applicable) or their top-priority initiative.

**Pros:**
- Lower disruption: people stay in their teams, reducing change management burden.
- Preserves deep expertise and consistency in platform and data domains.
- Self-service tooling investment pays long-term dividends.
- Feasible to implement incrementally alongside the 8-week launch.

**Cons:**
- Does not fully eliminate the bottleneck; reduces it through process, not structure.
- Self-service tooling takes time to build (may not be ready for 8-week launch).
- Relies on discipline and adherence to intake processes.
- Data ownership clarity depends on RACI being respected, which requires cultural change.

---

### Option C: Hybrid — Selective Embedding + Platform-as-a-Product (Recommended)

**Core idea:** Embed a subset of platform and data engineers into the highest-priority teams while keeping a strong core. Implement self-service and intake processes for the remaining teams. Give AI/ML a PM and a home.

**Changes:**

- **Platform team (20 people) restructures to:**
  - Core Platform (14 people): retains ownership of CI/CD, infrastructure, shared APIs, developer experience. Immediately begins building self-service tooling for the top 3 most-requested capabilities (based on historical ticket analysis). Implements transparent intake with SLAs.
  - Embedded Platform Engineers (6 people): 2 embedded into the customer launch feature team (highest priority), 2 embedded into the next-highest-priority feature team, 2 remain as a "SWAT team" that can be assigned to any team facing a critical blocker for up to 2 weeks at a time.

- **Data team (18 people) restructures to:**
  - Core Data (12 people): owns warehouse, governance, shared pipelines, data catalog. Publishes clear ownership charter (RACI). Begins self-service data access initiative.
  - Embedded Data Engineers (6 people): 2 embedded into the customer launch team, 2 into the feature team with the heaviest data dependency, 2 as floaters for urgent cross-team data work.

- **AI/ML team (4 people):**
  - Formally reports to the engineering director who owns the product area most aligned with AI (likely the analytics or insights product area).
  - Gets a dedicated PM (an existing PM shifts 50% of their time to AI/ML; their current feature team backfills PM coverage from a senior designer or eng lead for tactical sprint work).
  - For the next 8 weeks, AI/ML is ring-fenced: they work only on the customer launch (if AI is in scope) or their single top initiative. All other requests are deferred to a backlog the new PM maintains.
  - Post-launch: evaluate whether to grow to 6-8 people by internal transfer (not new headcount) or to embed AI/ML engineers into feature teams.

**Pros:**
- Balances parallelism gains (embedding) with consistency and deep expertise (strong core teams).
- Directly addresses the 8-week launch by embedding resources into the launch team.
- AI/ML gets real prioritization authority without waiting for a new hire.
- Incremental: can adjust the ratio of embedded vs. core over time based on results.
- Does not require headcount increase.

**Cons:**
- Moderate organizational change; requires clear communication.
- Embedded engineers need dotted-line management (functional lead for career growth, team lead for daily work).
- Risk of "two-class" system where non-embedded feature teams feel under-resourced.

---

## 4. Recommendation: Option C (Hybrid)

### Why Option C

| Criterion | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Shipping parallelism | High | Medium | High |
| Cross-team blocking reduction | High | Medium | High |
| Risk during 8-week launch | High (too much change) | Low | Medium |
| Long-term sustainability | Medium (fragmentation risk) | Medium (bottleneck persists) | High |
| Implementation effort | High | Low | Medium |
| No new headcount required | Yes | Yes | Yes |
| AI/ML team effectiveness | Medium | Medium | High |
| Data ownership clarity | High | Medium | High |

Option C provides the best balance: it directly unblocks the customer launch by embedding engineers where they are needed most, while maintaining strong centralized teams for consistency and long-term platform health. It is achievable within the constraints (no new headcount, 8-week launch deadline) and can be tuned over time.

---

## 5. Transition Plan

### Phase 0: Preparation (Week 1)

**Objective:** Align leadership, communicate the plan, de-risk the customer launch.

| Action | Owner | Deliverable |
|--------|-------|-------------|
| Leadership alignment meeting: present Options A/B/C, confirm Option C | VP Engineering | Decision document signed off by CTO, VP Eng, VP Product |
| Identify the 6 platform engineers and 6 data engineers for embedding | Platform Lead + Data Lead | Named list with team assignments |
| Identify the PM who will take on AI/ML (50% allocation) | VP Product | PM assignment confirmed, current responsibilities redistributed |
| Map customer launch critical path across all teams | Launch PM + Eng Leads | Gantt chart or dependency map with owners for each workstream |
| Draft and send all-hands communication explaining changes | VP Engineering | Company-wide email + FAQ document |
| Set up new Slack channels / communication norms for embedded engineers | Engineering Operations | Channels created, norms documented |

### Phase 1: Embed & Stabilize (Weeks 2-3)

**Objective:** Move embedded engineers into their new teams. Establish working norms. Protect the customer launch.

| Action | Owner | Deliverable |
|--------|-------|-------------|
| Embedded platform engineers join their assigned feature teams | Platform Lead | Engineers attending feature team standups, with access to repos and boards |
| Embedded data engineers join their assigned feature teams | Data Lead | Engineers attending feature team standups |
| AI/ML team begins working with new PM; create 8-week sprint plan | AI/ML Lead + New PM | Sprint plan for AI/ML aligned to launch or top initiative |
| Core Platform team publishes intake process and SLAs | Platform Lead | Documented intake process in wiki, Slack bot or Jira workflow for requests |
| Core Data team publishes ownership RACI and data catalog v1 | Data Lead | RACI matrix shared, initial data catalog accessible |
| Customer launch team holds kickoff with all embedded members | Launch PM | Kickoff meeting, aligned sprint plan, identified risks |
| Establish weekly cross-team sync for embedded engineers | Platform Lead + Data Lead | 30-min weekly meeting for embedded engineers to share patterns and avoid divergence |

### Phase 2: Execute Customer Launch (Weeks 3-8)

**Objective:** Ship the customer launch on time. Let the new structure prove itself.

| Action | Owner | Deliverable |
|--------|-------|-------------|
| Customer launch team operates with embedded platform + data engineers | Launch PM | Features shipped on schedule |
| SWAT team (2 platform floaters) available for critical blockers on other teams | Platform Lead | Response within 24 hours for P1 requests from non-launch teams |
| Core Platform begins self-service tooling sprint (top 3 capabilities) | Platform Lead | At least 1 self-service capability shipped by Week 6 |
| Core Data begins self-service data access initiative | Data Lead | Self-service query tool or dashboard builder accessible by Week 6 |
| AI/ML team executes against sprint plan; PM triages all incoming requests | AI/ML PM | Backlog maintained, no unplanned work accepted without PM approval |
| Bi-weekly retro on new structure: what is working, what is not | VP Engineering | Retro notes with action items |
| Track metrics (see below) weekly | Engineering Operations | Dashboard updated weekly |

### Phase 3: Evaluate & Adjust (Weeks 9-12, Post-Launch)

**Objective:** Assess the restructuring, make permanent decisions, plan next quarter.

| Action | Owner | Deliverable |
|--------|-------|-------------|
| Post-launch retrospective covering all teams | VP Engineering | Retro document with quantitative and qualitative findings |
| Decide embedding ratio: increase, decrease, or maintain | VP Engineering + Leads | Decision document for next quarter |
| Evaluate AI/ML team: does it need a full-time PM? Should it grow via internal transfer? | VP Product + AI/ML Lead | AI/ML team charter for next quarter |
| Assess self-service tooling adoption; prioritize next capabilities | Platform Lead | Self-service roadmap for Q+1 |
| Formalize data ownership RACI based on lessons learned | Data Lead | Updated RACI, any ownership transfers completed |
| Decide whether non-launch feature teams also get embedded engineers | VP Engineering | Embedding plan for next quarter |
| Communicate results and next steps to the company | VP Engineering | All-hands update |

---

## 6. Metrics to Track

### Leading Indicators (Weekly)

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Cross-team blocking tickets | 50% reduction by Week 6 | Count of Jira tickets blocked on another team |
| Platform request queue depth | Below 10 open requests | Platform intake board |
| Time-to-resolve platform requests | P1 < 48 hrs, P2 < 1 sprint | Ticket timestamps |
| AI/ML unplanned work ratio | < 15% of sprint capacity | Sprint tracking |
| Customer launch milestone completion | On track (green/yellow/red) | Weekly status report |

### Lagging Indicators (Monthly / Quarterly)

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Feature team cycle time (idea to production) | 20% improvement by end of Q | Deployment tracking |
| Number of production incidents caused by unclear ownership | Zero | Incident post-mortems |
| Developer satisfaction (survey) | Improvement in "I can ship without waiting on other teams" | Quarterly pulse survey |
| Platform self-service adoption | 50% of routine requests handled via self-service by Q end | Self-service usage analytics |

---

## 7. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Customer launch is delayed due to restructuring distraction | Medium | High | Phase 0 happens in Week 1 only; embedding is designed to help, not hinder the launch. Launch team gets more resources, not fewer. |
| Non-launch feature teams feel neglected | Medium | Medium | SWAT team provides safety net. Transparent intake with SLAs ensures non-launch work is not ignored. Communicate that this is a temporary prioritization, not a permanent hierarchy. |
| Embedded engineers lose connection to their discipline | Medium | Low | Weekly cross-team sync for embedded engineers. Dotted-line reporting to functional lead for career growth, code reviews, and standards. |
| Platform consistency degrades as embedded engineers diverge | Low | Medium | Core platform team sets standards and reviews. Embedded engineers follow shared architecture guidelines. Weekly sync catches drift early. |
| AI/ML PM (50% allocation) is insufficient | Medium | Medium | Monitor AI/ML throughput. If the PM is overloaded, consider a full-time reassignment or promote an AI/ML engineer to tech lead who handles tactical prioritization. |
| Teams resist the change | Medium | Medium | Involve team leads in the planning (Phase 0). Frame the change as "giving teams more autonomy and fewer blockers." Solicit feedback in bi-weekly retros and adjust. |

---

## 8. Communication Plan

| Audience | When | Channel | Message |
|----------|------|---------|---------|
| Engineering leadership (directors, senior managers) | Week 1, Day 1 | In-person / video meeting | Full plan presentation, gather input, finalize decisions |
| All engineering | Week 1, Day 3 | All-hands + written memo | Why we are making changes, what changes, what it means for each team, FAQ |
| Affected individuals (embedded engineers, AI/ML PM) | Week 1, Day 2 | 1:1 conversations | Personal conversation about new role, expectations, support available |
| Product and design | Week 1, Day 3 | Joint meeting with VP Product | How this affects product team workflows, new PM allocation for AI/ML |
| Customer success / sales (re: launch) | Week 1, Day 4 | Stakeholder update | Reassurance that launch is on track and getting more resources |
| Whole company | Week 2 | Company all-hands | Brief overview of engineering org changes and why |

---

## 9. Organizational Chart: Before and After

### Before

```
VP Engineering
├── Feature Team 1 (PM, EM, ~20 engineers)
├── Feature Team 2 (PM, EM, ~20 engineers)
├── Feature Team 3 (PM, EM, ~20 engineers)
├── Feature Team 4 (PM, EM, ~20 engineers)
├── Feature Team 5 (PM, EM, ~20 engineers)
├── Platform Team (EM, ~20 engineers)
├── Data Team (EM, ~18 engineers)
└── AI/ML Team (4 engineers, no PM)
```

### After (Option C)

```
VP Engineering
├── Feature Team 1 (PM, EM, ~20 eng + 2 embedded platform + 2 embedded data)
│   └── [CUSTOMER LAUNCH TEAM — highest priority]
├── Feature Team 2 (PM, EM, ~20 eng + 2 embedded platform + 2 embedded data)
├── Feature Team 3 (PM, EM, ~20 engineers)
├── Feature Team 4 (PM, EM, ~20 engineers)
├── Feature Team 5 (PM, EM, ~20 engineers)
├── Core Platform Team (EM, 14 engineers)
│   ├── Self-service tooling squad
│   ├── Infrastructure & reliability squad
│   └── SWAT pair (2 engineers, rotational cross-team support)
├── Core Data Team (EM, 12 engineers)
│   ├── Data warehouse & governance squad
│   ├── Shared pipelines squad
│   └── Floater pair (2 engineers, urgent cross-team data work)
└── AI/ML Team (4 engineers + 50% PM from existing PM pool)
    └── Reports to director of most-aligned product area
```

**Dotted-line relationships:**
- Embedded platform engineers → Core Platform Lead (standards, career growth, code review)
- Embedded data engineers → Core Data Lead (standards, career growth, code review)

---

## 10. Summary of Key Decisions

1. **Adopt Option C (Hybrid):** Selectively embed 6 platform + 6 data engineers into highest-priority feature teams while maintaining strong core teams.
2. **Ring-fence the customer launch:** The launch team gets 2 embedded platform + 2 embedded data engineers, plus AI/ML allocation if applicable.
3. **Give AI/ML a PM:** Reallocate 50% of an existing PM's time to AI/ML prioritization immediately.
4. **Clarify data ownership:** Publish a RACI within the first 2 weeks. Core Data owns ingestion, transformation, warehouse, and governance. Feature teams own their analytics and reporting.
5. **Invest in self-service:** Core Platform and Core Data teams begin building self-service capabilities immediately, targeting at least one shipped capability by Week 6.
6. **Evaluate at Week 9:** Use quantitative metrics and qualitative feedback to decide next-quarter adjustments. No permanent decisions until the structure has been tested through the launch.
