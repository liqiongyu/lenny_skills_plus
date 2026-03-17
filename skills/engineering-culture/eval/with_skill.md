# Engineering Culture Operating System Pack

**Organization:** B2B Analytics SaaS
**Scope:** Full engineering org (40 engineers, 5 teams)
**Decision owner:** VP Engineering / Head of Engineering (assumed)
**Date:** 2026-03-17
**Timeline:** One quarter (Q2 2026) -- goal is daily deploys and 50% P1 reduction

---

## 1) Culture + Capability Snapshot

### Context

- **Scope:** Full engineering org
- **Products/systems:** B2B analytics SaaS platform
- **Stage:** Growth/scale (established product, operational maturity needed)
- **Eng size + topology:** 40 engineers across 5 teams (assumed: 4 feature teams + 1 platform team)
- **Remote/hybrid:** Not specified (assumed hybrid; does not change analysis)
- **Decision owner(s):** VP Engineering (assumed)
- **Timeline / forcing function:** One quarter -- increase deploy frequency to daily, reduce P1 incidents by 50%

### Symptoms (evidence)

- **Symptom 1: Slow PR cycle time (3+ days in review)**
  - Evidence: PRs sit in review for 3+ days across all teams. This indicates unclear review ownership, lack of review SLAs, and likely large PRs that are difficult to review quickly.

- **Symptom 2: No owned on-call rotation**
  - Evidence: On-call rotates randomly with no team ownership. Nobody feels accountable for production health. Likely contributes to the 2 P1 incidents/month because issues are detected late and response is uncoordinated.

- **Symptom 3: Platform team is a bottleneck for every feature team**
  - Evidence: All feature teams depend on platform for infrastructure changes, deploy pipeline access, or shared service modifications. Platform has no product interface -- requests arrive ad hoc, creating queueing delays and context-switching.

- **Symptom 4: PMs complain engineering "goes dark" mid-sprint**
  - Evidence: No shared visibility into work-in-progress after sprint planning. No mid-sprint check-ins, no async status artifacts, no shared toolchain norms. PMs cannot tell whether work is on track, blocked, or scope-changed until the end of the sprint.

### Current Delivery System Snapshot

| Dimension | Current state |
|---|---|
| Release/deploy cadence | Twice per week via manual release trains |
| CI/CD maturity | Assumed: CI exists but deploys are manual; limited automated testing (needs data); no progressive delivery |
| Rollback strategy | Assumed: manual rollback or redeploy; no canary/staged rollout (needs data) |
| On-call / incident process | Random rotation, no team-owned on-call, no defined escalation path; 2 P1s/month |
| Toolchain | Assumed: GitHub for code, likely Jira or Linear for work tracking, Slack for comms (needs confirmation) |

### Baseline Metrics (best-effort)

| Metric | Current (estimated) | Target (end of quarter) | Confidence |
|---|---|---|---|
| Deploy frequency | ~2/week (release train) | 1/day (minimum) | High (stated) |
| Lead time for changes | 5-10 days (assumption: PR time + release train wait) | 1-3 days | Medium |
| Change failure rate | ~10-15% (inferred from 2 P1s/month on ~8 deploys/month) | <5% | Medium |
| MTTR | Unknown (needs data) | <2 hours | Low |
| PR cycle time | 3+ days | <24 hours | High (stated) |
| P1 incidents/month | 2 | <=1 | High (stated) |
| Experiment throughput | Unknown | Needs data | Low |
| DevEx sentiment | Not measured | Establish baseline in 30 days | N/A |
| **Missing instrumentation** | MTTR tracking, change failure rate, deploy frequency per team, experiment throughput, DevEx survey |

### Capability Map (evidence-based)

| Capability bucket | Current state | Evidence | Gap | Candidate initiative |
|---|---|---|---|---|
| **Technical** | CI exists; deploys are manual release trains; limited progressive delivery; test coverage unknown | 2x/week manual deploys; 2 P1s/month; no canary/flag infrastructure mentioned | Automated deploy pipeline, progressive delivery (canary/flags), observability for faster detection | Implement CD pipeline; add feature flags; improve observability and alerting |
| **Architectural** | Rails monolith + 3 Go microservices; platform team owns shared infra | All feature teams depend on platform for changes; monolith likely has shared ownership hotspots | Unclear ownership boundaries in monolith; platform has no self-service interface; coupling between feature teams and platform | Define module ownership within monolith; build platform self-service layer; document service contracts |
| **Cultural** | Low ownership (random on-call); heroics rewarded implicitly; engineers "go dark" | No team-owned on-call; PMs lose visibility; PRs sit 3+ days (low review urgency) | Ownership culture; review discipline; transparency norms; blameless incident learning | Team-owned on-call; review SLAs; async status rituals; blameless retros |
| **Management/Lean** | Large batch releases; no WIP limits; no explicit priorities mid-sprint | Release trains batch work; no mid-sprint check-ins; PMs blind mid-sprint | Small batch delivery; WIP limits; continuous prioritization; shared visibility | Daily deploys; WIP limits; mid-sprint async updates; delivery metrics dashboards |

### Priority Shifts (4)

**1) From "release trains" to "continuous delivery"**
- Why now: Twice-a-week manual deploys are the single biggest constraint on clock speed. Batching increases risk (larger changesets = more P1s) and increases lead time.
- What changes in behavior: Engineers deploy their own changes daily via automated pipeline. No more waiting for the train.
- Leading indicators: Deploy frequency (target: 1/day), average changeset size (should decrease), time from merge to production.

**2) From "random on-call" to "team-owned production responsibility"**
- Why now: 2 P1s/month with no ownership means slow detection, slow response, and no feedback loop to the team that caused the issue. This is the root cause of reliability problems.
- What changes in behavior: Each team owns on-call for their services/modules. Teams that ship code own the consequences. Incidents trigger blameless retros with action items.
- Leading indicators: MTTR, P1 count, % of incidents with completed retros.

**3) From "platform as gatekeeper" to "platform as enabler"**
- Why now: Platform bottleneck slows every feature team. Conway's Law says if platform gates everything, architecture will centralize further.
- What changes in behavior: Platform provides self-service tools and golden paths. Feature teams can deploy, provision, and configure without platform tickets.
- Leading indicators: Platform ticket queue length (should decrease), feature team deploy autonomy (% of deploys without platform intervention).

**4) From "going dark" to "transparent delivery"**
- Why now: PM trust erosion leads to micromanagement or disengagement. Engineering credibility depends on visible progress.
- What changes in behavior: Async status updates tied to PRs/issues. Mid-sprint visibility via shared dashboards. PMs can see work state without asking.
- Leading indicators: PM satisfaction (survey), number of "where is this?" interruptions (should decrease).

---

## 2) Engineering Culture Code (v1)

### Principle 1: You Build It, You Run It

- **What it means:** The team that writes the code owns it in production. Ownership includes monitoring, on-call, incident response, and fixing issues -- not just shipping features.
- **Behaviors we expect:**
  - Do: Take on-call shifts for your team's services and respond within the defined SLA.
  - Do: Write a blameless retro within 48 hours of any P1 incident your team is involved in, with at least one concrete action item.
  - Do: Add monitoring and alerting as part of the definition of done for any new feature or service change.
- **Behaviors we avoid:**
  - Don't: Ship a feature and declare it "platform's problem" if it breaks in production.
  - Don't: Skip retros or write retros that assign blame to individuals.
- **Decision rules:** When an incident occurs, the team that owns the affected service leads the response. If ownership is ambiguous, the on-call engineer escalates to the VP Eng to assign a temporary owner within 1 hour, and ownership is clarified permanently within 1 week.
- **Anti-patterns:** "Not my service" deflection; retros that produce zero action items; on-call rotations where the person on-call has no context on the system.
- **How we'll know it's working:** Every P1 has a retro with action items tracked to completion. MTTR decreases quarter over quarter. On-call burden is distributed evenly across teams (no single team taking >30% of pages).

### Principle 2: Ship Small, Ship Often

- **What it means:** We optimize for small, frequent, reversible changes over large, batched releases. Smaller changesets are easier to review, safer to deploy, and faster to roll back.
- **Behaviors we expect:**
  - Do: Break work into PRs that can be reviewed in under 30 minutes (target: <300 lines changed).
  - Do: Deploy your changes within 1 business day of merge. Do not let merged code sit undeployed.
  - Do: Use feature flags for any change that cannot be safely shipped incrementally.
- **Behaviors we avoid:**
  - Don't: Batch multiple unrelated changes into one PR or one deploy.
  - Don't: Treat deploy day as a special event that requires coordination across teams.
- **Decision rules:** If a change is too large to ship safely in one PR, decompose it into smaller slices behind a feature flag before starting implementation. If you are unsure whether a change needs a flag, ask in the team's Slack channel -- default to using a flag.
- **Anti-patterns:** "Big bang" releases; PRs open for a week accumulating scope; "just one more thing" before the deploy.
- **How we'll know it's working:** Average PR size decreases; deploy frequency reaches daily; change failure rate stays below 5%.

### Principle 3: Reviews Are a Service, Not a Gate

- **What it means:** Code review exists to improve quality and share knowledge, but it must not be a bottleneck. We treat review as a time-sensitive service with SLAs, not an optional activity engineers get to when they feel like it.
- **Behaviors we expect:**
  - Do: Respond to review requests within 4 business hours (first pass). Final approval within 24 hours.
  - Do: If you cannot review in time, re-assign or escalate -- do not let PRs sit silently.
  - Do: Distinguish blocking feedback ("this will break X") from suggestions ("consider Y for readability") using conventional labels (e.g., `blocking:`, `nit:`, `question:`).
- **Behaviors we avoid:**
  - Don't: Sit on a review request for days without communication.
  - Don't: Use review as a gatekeeping mechanism to enforce personal style preferences.
- **Decision rules:** If a PR has not received a first-pass review within 4 hours, the author pings the assigned reviewer. If no response within 8 hours, the author escalates to the team lead. Stale reviews are surfaced in the weekly delivery review.
- **Anti-patterns:** PRs with 15 comments and no resolution; "LGTM" without reading the code; using reviews to relitigate design decisions that were already agreed upon.
- **How we'll know it's working:** Median PR cycle time drops below 24 hours; zero PRs older than 48 hours without a first review.

### Principle 4: Make Work Visible

- **What it means:** The state of every piece of in-flight work should be discoverable without asking someone. Transparency enables trust across functions and reduces "where is this?" interruptions.
- **Behaviors we expect:**
  - Do: Keep issue/ticket status up to date daily (move cards, update descriptions with blockers).
  - Do: Link every PR to its parent issue. Include a brief "what and why" in PR descriptions.
  - Do: Post a weekly async status update (per team) summarizing: shipped, in progress, blocked, next up.
- **Behaviors we avoid:**
  - Don't: Communicate progress only through Slack DMs or verbal stand-ups with no written record.
  - Don't: Let issues sit in "In Progress" for more than 5 days without an update.
- **Decision rules:** If work is blocked for more than 1 day, the engineer updates the ticket with the blocker and tags the blocking party. If a PM asks "what's the status?" and the answer is not findable in the work tracker, that is a process failure.
- **Anti-patterns:** "Going dark" for days; stand-ups where everyone says "same as yesterday"; dashboards that no one looks at.
- **How we'll know it's working:** PMs report fewer "where is this?" interruptions (tracked via quarterly survey); 90%+ of PRs link to issues; weekly async updates are published consistently.

### Principle 5: Platform Enables, Teams Decide

- **What it means:** The platform team provides tools, golden paths, and self-service capabilities. Feature teams use these to move fast without waiting for platform. Platform does not make product decisions for feature teams, and feature teams do not make infrastructure decisions without consulting platform's documented standards.
- **Behaviors we expect:**
  - Do: Platform publishes a service catalog of available capabilities, with documentation and self-service access.
  - Do: Feature teams use platform's golden paths for new services, deploys, and infrastructure provisioning.
  - Do: Platform tracks adoption metrics (% of teams on golden path, ticket queue length) and treats these as their product metrics.
- **Behaviors we avoid:**
  - Don't: Route every infrastructure request through a platform ticket queue when a self-service option exists.
  - Don't: Build custom one-off infrastructure without checking if platform already offers a solution.
- **Decision rules:** If a feature team needs something platform does not offer, they file a request with a business case. Platform triages within 2 business days. If platform cannot deliver within the sprint, the feature team and platform agree on a workaround or escalate to VP Eng.
- **Anti-patterns:** Platform as ticket queue; feature teams building shadow infrastructure; platform building tools nobody uses.
- **How we'll know it's working:** Platform ticket queue decreases by 50%; feature team deploy autonomy increases; platform team NPS from internal customers improves.

---

## 3) Org / Architecture Alignment Brief (Conway's Law Analysis)

### Current Org + Operating Model

**Teams (assumed based on context):**

| Team | Focus | Size (est.) |
|---|---|---|
| Platform | Infrastructure, CI/CD, shared services, deploy pipeline | ~8 engineers |
| Feature Team A | Core analytics / dashboards | ~8 engineers |
| Feature Team B | Data ingestion / pipelines | ~8 engineers |
| Feature Team C | Integrations / connectors | ~8 engineers |
| Feature Team D | User management / billing / admin | ~8 engineers |

**Cross-team dependencies (today):**
- All 4 feature teams depend on Platform for deploy access, infrastructure provisioning, and shared service modifications.
- Feature Teams A and B likely share significant surface area in the Rails monolith (analytics features depend on data ingestion).
- The 3 Go microservices have unclear ownership -- likely owned by Platform or shared across teams (needs confirmation).

**Where decisions happen (today):**
- Technical decisions: Assumed ad hoc, no architecture decision record (ADR) process.
- Deploy decisions: Platform controls the release train schedule.
- Prioritization: PMs set sprint priorities per team, but mid-sprint changes happen without a visible process.

### Architecture + Ownership Boundaries

**Key components/services:**

| Component | Technology | Owner (today) | Ownership clarity |
|---|---|---|---|
| Rails monolith (core app) | Ruby on Rails | Shared across all feature teams | LOW -- multiple teams edit same models, controllers, and database |
| Go microservice 1 | Go | Unclear (likely Platform or Team B) | LOW |
| Go microservice 2 | Go | Unclear | LOW |
| Go microservice 3 | Go | Unclear | LOW |
| Deploy pipeline / CI | Custom (assumed) | Platform | Medium -- Platform controls, but process is manual |
| Infrastructure (hosting, DBs, queues) | Various | Platform | Medium |

**Coupling hotspots:**
1. **Rails monolith shared database:** Multiple feature teams read/write the same tables. Schema changes are high-risk and require cross-team coordination.
2. **Platform deploy pipeline:** All teams funnel through the same manual release train. Platform is the single point of coordination.
3. **Go microservices with unclear ownership:** When these services break, nobody knows who responds. When they need changes, requests go to Platform by default.

### Conway's Law Findings (Misalignments)

**Misalignment 1: Monolith with shared ownership vs. 4 independent feature teams**
- **Impact:** The org says "4 independent feature teams" but the architecture says "one shared codebase with no boundaries." Teams step on each other. PRs touch shared code and require cross-team review, contributing to the 3+ day review cycle.
- **Evidence:** PRs sit 3+ days (often waiting for reviewers from other teams who own adjacent code). Feature teams cannot ship independently because changes overlap in the monolith.
- **Root cause:** No module ownership within the monolith. No CODEOWNERS file or domain boundaries enforced in code.

**Misalignment 2: Platform as gatekeeper vs. feature teams needing autonomy**
- **Impact:** Platform's org structure creates a centralized bottleneck that mirrors the centralized deploy pipeline. Conway's Law is working as designed -- the architecture (centralized deploy) mirrors the org (centralized platform team). To change the architecture, you must change the org model.
- **Evidence:** PMs complain about engineering going dark -- often because teams are blocked on platform requests. Feature teams cannot deploy without platform involvement.
- **Root cause:** Platform operates as a service desk rather than a product team. No self-service interface, no golden paths, no internal product management.

**Misalignment 3: Random on-call vs. team-owned services**
- **Impact:** When nobody owns on-call for specific services, the architecture's implicit ownership (which team last touched it) does not match the operational model (random rotation). Incident response is slow because the on-call person may have no context on the failing service.
- **Evidence:** 2 P1 incidents/month; on-call rotates randomly.
- **Root cause:** On-call was never redesigned as the org grew from a small team to 40 engineers. The model that worked at 10 does not work at 40.

### Proposed Changes (Operating Model)

**Change 1: Define module ownership within the Rails monolith**
- **Rationale:** Before extracting microservices (expensive), define clear domain boundaries within the monolith. Assign each major module/domain to a single team. Use CODEOWNERS to enforce.
- **Transition plan:**
  1. Week 1-2: Map the monolith into 4-6 domain modules (e.g., analytics-core, ingestion, integrations, user-admin, billing, shared-libs).
  2. Week 2-3: Assign primary ownership of each module to one team. Document in CODEOWNERS and a team wiki page.
  3. Week 3-4: Configure CI to auto-assign reviewers based on CODEOWNERS. Cross-module PRs require explicit approval from both owning teams.
  4. Ongoing: Track cross-module PR frequency as a coupling metric. High cross-module traffic signals a boundary is wrong.
- **Trade-offs:** Some modules will be hard to assign cleanly. Shared libraries and database schemas will need joint ownership rules. This adds friction for changes that span domains, but that friction is a feature -- it makes coupling visible.

**Change 2: Reposition Platform as an internal product team**
- **Rationale:** Platform must shift from "ticket queue for requests" to "product team that builds self-service tools." This requires Platform to have its own product manager (or a designated PM liaison) and to measure success by adoption and autonomy metrics, not by tickets closed.
- **Transition plan:**
  1. Week 1-2: Audit current platform requests -- categorize into "should be self-service," "requires platform engineering," and "should be feature team's responsibility."
  2. Week 3-4: Build or document the first 2-3 self-service capabilities (e.g., deploy pipeline access, new service scaffolding, environment provisioning).
  3. Week 5-8: Migrate feature teams to self-service for the top 3 request categories. Platform stops accepting tickets for these.
  4. Week 9-12: Platform publishes a service catalog and tracks adoption metrics.
- **Trade-offs:** Platform team needs to invest in documentation and tooling upfront, which means fewer feature requests for platform itself. Some feature teams will resist taking on operational responsibility they previously delegated to platform.

**Change 3: Assign Go microservice ownership to feature teams**
- **Rationale:** Each microservice should be owned by the team closest to its business domain. If a Go service handles data ingestion, Team B (data ingestion) owns it. If it handles integrations, Team C owns it.
- **Transition plan:**
  1. Week 1: Map each Go service to its primary business domain and assign a team.
  2. Week 2-3: Knowledge transfer sessions -- current maintainers walk the new owning team through architecture, runbooks, and known issues.
  3. Week 4: Ownership transfer complete. New team takes on-call for the service.
- **Trade-offs:** New owning teams may lack Go expertise. Budget 1-2 weeks of ramp-up time. Consider pairing with Platform engineers during the transition.

### Standardization (where consistency matters)

| Area | Standard (required across all teams) |
|---|---|
| **On-call policy** | Each team owns on-call for its services. Rotation is weekly, within the team. On-call engineer has <15 min response SLA for P1. Compensation/time-off policy defined by VP Eng. |
| **Code review standards** | First-pass review within 4 business hours. Final approval within 24 hours. Use `blocking:` / `nit:` / `question:` labels. CODEOWNERS enforced in CI. |
| **Incident/retro expectations** | Every P1 and P2 gets a blameless retro within 48 hours. Retro must produce at least 1 action item with an owner and a due date. Action items tracked in the team's backlog. |
| **Release/deploy policy** | Teams can deploy independently via the automated pipeline (once built). No manual release trains. Deploys require: passing CI, at least 1 approval, and a rollback plan (automated or documented). |
| **Leveling (senior expectations)** | Senior engineers are expected to: own on-call, mentor juniors on review practices, drive cross-team technical decisions via RFCs/ADRs, and lead incident response. (Needs further calibration with engineering leadership.) |

---

## 4) Clock Speed + DevEx Improvement Backlog

### Clock Speed Targets (Q2 2026)

| Metric | Current | Target (end of Q2) | Guardrail |
|---|---|---|---|
| Deploy frequency | ~2/week (batched) | >=1/day (per team) | No deploy freezes longer than 1 day except for critical incidents |
| Lead time (merge to prod) | ~2-5 days (release train wait) | <4 hours | N/A |
| PR cycle time | 3+ days | <24 hours median | No PRs open >48 hours without first review |
| Change failure rate | ~10-15% (estimated) | <5% | If CFR exceeds 10% for 2 weeks, pause new features and focus on quality |
| MTTR | Unknown | <2 hours for P1 | Instrument within 30 days |
| P1 incidents/month | 2 | <=1 | If P1s increase after switching to daily deploys, slow down and investigate |

### Bottleneck Map (Value Stream)

A typical change currently flows:

```
Idea (PM) --> Issue (tracked?) --> Branch (engineer) --> PR (3+ days in review)
    --> Merge --> Wait for release train (1-3 days) --> Manual deploy --> Production
    --> Incident? (random on-call, slow response) --> No structured retro
```

**Where work gets stuck:**

| Bottleneck | Wait time | Root cause |
|---|---|---|
| PR review | 3+ days | No review SLAs, no CODEOWNERS, large PRs, unclear reviewer assignment |
| Release train wait | 1-3 days after merge | Manual batched deploys, platform gating |
| Platform dependency | Days to weeks | No self-service, platform as ticket queue |
| Incident response | Unknown (likely hours) | Random on-call, no runbooks, no ownership |
| Cross-team coordination in monolith | Variable | Shared code ownership, no module boundaries |

### Prioritized Backlog

| # | Initiative | Lever | Impact | Effort | Dependencies | Owner | Metric / Leading Indicator |
|---|---|---|---|---|---|---|---|
| 1 | **Implement CODEOWNERS + auto-reviewer assignment** | Cultural / Tech | High -- directly reduces PR review wait | S (1-2 days) | Module ownership mapping (Change 1) | Tech lead + each team lead | PR cycle time, % PRs with auto-assigned reviewer |
| 2 | **Establish review SLA (4h first pass / 24h approval)** | Cultural | High -- directly attacks 3+ day PR cycle | S (announce + enforce) | CODEOWNERS in place | VP Eng + team leads | Median time-to-first-review, PR cycle time |
| 3 | **Automate deploy pipeline (CD)** | Technical | Critical -- unlocks daily deploys | L (4-6 weeks) | Platform team capacity; CI stability | Platform tech lead | Deploy frequency, time from merge to prod |
| 4 | **Add feature flags infrastructure** | Technical | High -- enables progressive delivery and safe daily deploys | M (2-3 weeks) | CD pipeline (can start in parallel) | Platform engineer (assigned) | % of deploys using flags, rollback time |
| 5 | **Implement team-owned on-call rotations** | Cultural / Mgmt | High -- directly reduces MTTR and P1 count | M (2-3 weeks to set up, ongoing) | Module/service ownership mapping | VP Eng + team leads | MTTR, P1 count, on-call response time |
| 6 | **Establish blameless retro process** | Cultural | Medium -- creates feedback loop from incidents to code quality | S (1 week to define process, ongoing) | On-call ownership | VP Eng | % of P1/P2s with completed retros, # action items completed |
| 7 | **Build platform self-service (top 3 capabilities)** | Architectural / Tech | High -- unblocks feature teams | L (6-8 weeks) | Platform team reprioritization | Platform team lead | Platform ticket queue length, feature team deploy autonomy % |
| 8 | **Define module boundaries in Rails monolith** | Architectural | High -- reduces cross-team coupling | M (2-3 weeks for mapping + CODEOWNERS) | None | Senior engineers (1 per team) + architect | Cross-module PR frequency, merge conflicts |
| 9 | **Improve observability (alerting + dashboards)** | Technical | Medium -- faster detection, lower MTTR | M (3-4 weeks) | Service ownership (to know what to monitor) | Platform + each team | Alert-to-detection time, dashboard usage |
| 10 | **Implement WIP limits per team** | Management/Lean | Medium -- reduces context switching, improves flow | S (1 week to agree on limits) | Work tracker configuration | Team leads | Average WIP per engineer, cycle time |
| 11 | **Set up DevEx baseline survey** | Cultural / Mgmt | Medium -- enables measurement of improvement | S (1 week) | None | VP Eng or designated DRI | Survey completion rate, baseline scores |
| 12 | **Assign Go microservice ownership to feature teams** | Architectural | Medium -- closes ownership gaps | M (2-3 weeks including knowledge transfer) | Module/service mapping | VP Eng + team leads | Incident response time for Go services, on-call coverage |

### First 2-Week Quick Wins

**Win 1: Ship CODEOWNERS file and auto-reviewer assignment**
- Owner: Tech lead (with input from all team leads)
- Actions: Map monolith modules to teams, create CODEOWNERS, enable in CI.
- Expected signal: PRs get a reviewer auto-assigned within minutes. Time-to-first-review drops measurably within 1 week.

**Win 2: Announce and enforce review SLA (4h / 24h)**
- Owner: VP Eng
- Actions: Communicate the SLA in all-hands and in writing. Add a Slack bot or dashboard that flags PRs approaching SLA. Team leads responsible for enforcement in their teams.
- Expected signal: Median time-to-first-review drops below 8 hours within 2 weeks.

**Win 3: Launch DevEx baseline survey**
- Owner: VP Eng or designated DRI
- Actions: Send a 10-question survey covering: deploy ease, review speed, on-call burden, platform dependency pain, cross-functional collaboration satisfaction.
- Expected signal: >80% completion rate. Establishes a baseline for quarterly comparison.

---

## 5) Cross-Functional Workflow Contract

### Toolchain + Shared Artifacts

| Purpose | Tool (assumed -- confirm with team) | Who uses it |
|---|---|---|
| Source of truth for work tracking | Linear / Jira | PM, Eng, Design |
| Source of truth for decisions | RFC/ADR docs in repo or wiki | Eng leads, PM (read access for all) |
| Source of truth for code + changes | GitHub | Eng (primary), PM/Design (read access) |
| Communication | Slack | All |
| Incident tracking | PagerDuty or Opsgenie (to be set up if not present) | Eng on-call |

### Work Flow (Idea to Learn)

**1) Intake / Spec (PM + Eng + Design)**
- PM writes a 1-page spec (problem, success criteria, constraints, open questions) in the work tracker.
- Eng lead and Design review within 2 business days and add technical/design considerations.
- Spec is approved by PM + Eng lead before work starts. Approval is recorded on the ticket.
- **Who is accountable:** PM owns the spec; Eng lead owns the technical feasibility assessment.

**2) Build (Eng, with Design collaboration)**
- Engineer breaks the spec into issues/tasks linked to the parent spec.
- PRs reference the parent issue. PR descriptions include: what changed, why, how to test, rollback plan.
- Design reviews UI changes via staging/preview environments before merge (if applicable).
- **Mid-sprint visibility:** Engineers update ticket status daily. Blockers are flagged in the ticket and in the team Slack channel.

**3) Review (Eng)**
- Auto-assigned via CODEOWNERS. Manual override allowed.
- SLA: 4-hour first pass, 24-hour final approval.
- Reviewers use labels: `blocking:`, `nit:`, `question:`.
- If the SLA is breached, author escalates to team lead.

**4) Release (Eng, automated)**
- Merge to main triggers automated deploy pipeline (once built; until then, deploys happen via streamlined manual process with team-owned access).
- Feature flags for anything that is not fully ready or needs gradual rollout.
- Rollback: automated rollback if health checks fail; manual rollback via revert PR if needed.
- **Who can deploy:** Any engineer on the team that owns the code. No platform approval needed (post-CD migration).

**5) Learn (PM + Eng + Data)**
- PM defines success metrics in the spec. Eng instruments them before or during the build.
- After deploy, PM and Eng review metrics within 1 week.
- Experiments (A/B tests) require: a hypothesis, a success metric, a sample size estimate, and an analysis owner (PM or Data).
- Experiment results are documented in the parent ticket and shared in the weekly delivery review.

### Working Agreements

| Agreement | Detail |
|---|---|
| **PR expectations** | Description with what/why, linked issue, test coverage for new logic, rollout notes (flag? canary? full?), rollback plan if applicable. |
| **Review SLA** | First pass: 4 business hours. Final approval: 24 hours. Escalation: author -> team lead -> VP Eng. |
| **Merge/deploy policy** | Requires: green CI, >=1 approval from CODEOWNERS-designated reviewer. Deploy: automated on merge (target state). No Friday deploys of high-risk changes (team discretion). |
| **Experiment policy** | Hypothesis + success metric + sample size before build. Analysis owner assigned. Results shared in weekly review. Guardrails: <1% error rate increase, <5% latency regression. |
| **Scope change mid-sprint** | PM and Eng lead agree in writing (ticket comment). If scope increases, something else is deprioritized. No silent scope creep. |
| **Blocker escalation** | Blocked >1 day: update ticket + tag blocking party. Blocked >2 days: escalate to both team leads. Blocked >3 days: escalate to VP Eng. |

### Non-Engineer Participation

| Role | Allowed contributions | Safety rails |
|---|---|---|
| **PM** | File issues, write specs, update ticket status, request experiments, review metrics dashboards, comment on PRs (for context, not code approval) | PMs do not approve code merges. PMs do not change deploy schedules. |
| **Design** | Review UI changes in staging, file issues for design bugs, provide design specs as linked Figma/assets in tickets | Design reviews happen pre-merge via staging/preview. Design does not block deploys unless a blocking issue is filed. |
| **Marketing/Sales** | Request feature flags for launches, file issues for customer-facing content changes | All requests go through PM triage. No direct engineering requests. |

### AI-Assisted Development Norms

| Dimension | Norm |
|---|---|
| **Allowed uses** | Boilerplate generation, test writing, refactoring, documentation, migration scripts, code review assistance, debugging assistance. |
| **Required human checks** | All AI-generated code must be reviewed by a human engineer before merge. The reviewer must understand the intent and verify correctness -- "LGTM" on AI code without reading it is a review SLA violation. |
| **PR context** | PRs containing AI-generated code must note this in the description (e.g., "AI-assisted: test generation"). This is for transparency, not gatekeeping. |
| **"No silent changes" rule** | AI tools must not commit or deploy changes without explicit human approval. No automated merges from AI agents. No AI-initiated deploys. |
| **Data handling** | Do not paste customer data, secrets, or PII into AI tools. Use anonymized/synthetic data for AI-assisted debugging. |
| **Security-sensitive code** | Authentication, authorization, payment processing, and data access control code requires manual human authorship and review, even if AI assists with scaffolding. |

---

## 6) Rollout + Measurement Plan

### 30/60/90 Plan

**Days 1-30: Foundation**

| Week | Actions | Owner | Output |
|---|---|---|---|
| 1-2 | Ship CODEOWNERS + auto-reviewer assignment; announce review SLA; launch DevEx survey; map monolith modules to teams | Tech lead, VP Eng | CODEOWNERS file merged; SLA communicated; survey sent; module map draft |
| 2-3 | Assign Go microservice ownership; start knowledge transfer; define on-call rotations per team; begin CD pipeline design | VP Eng, Platform lead | Ownership assignments documented; on-call schedule published; CD design doc |
| 3-4 | Go live with team-owned on-call; establish blameless retro process; implement WIP limits; start building CD pipeline | VP Eng, Team leads, Platform | On-call rotations active; retro template in use; WIP limits agreed |

**Key milestone (Day 30):** Review SLA in effect, CODEOWNERS enforced, team-owned on-call live, DevEx baseline established, CD pipeline in progress.

**Days 31-60: Acceleration**

| Week | Actions | Owner | Output |
|---|---|---|---|
| 5-6 | CD pipeline MVP (automated deploy for at least 1 team); feature flag infrastructure MVP; first blameless retros completed | Platform lead, VP Eng | 1 team deploying via CD; feature flag system operational |
| 7-8 | Roll out CD pipeline to remaining teams; platform self-service for top 2 capabilities; cross-functional workflow contract training | Platform lead, VP Eng | All teams on CD; self-service docs published; workflow training completed |

**Key milestone (Day 60):** All teams deploying via CD (target: daily). Feature flags available. Platform self-service for top use cases. First retro action items completed.

**Days 61-90: Reinforcement + Measurement**

| Week | Actions | Owner | Output |
|---|---|---|---|
| 9-10 | Observability improvements (dashboards, alerting per team); platform self-service expansion; second DevEx survey | Platform, Team leads, VP Eng | Team dashboards live; self-service expanded; DevEx survey #2 |
| 11-12 | Quarter review: measure all targets (deploy freq, P1 count, PR cycle time, DevEx scores); publish results; adjust culture code and backlog for Q3 | VP Eng | Quarter review doc; updated backlog for Q3; culture code v1.1 |

**Key milestone (Day 90):** Daily deploys achieved. P1s reduced by 50% (target: <=1/month). PR cycle time <24 hours. DevEx survey shows improvement. Quarter review completed with data.

### Rituals + Cadence (Reinforcement)

| Ritual | Cadence | Purpose | Owner | Output artifact |
|---|---|---|---|---|
| **Weekly delivery review** (per team) | Weekly, 30 min | Review: shipped, cycle time, incidents, blockers, WIP. Celebrate wins. | Team lead | Meeting notes with metrics snapshot |
| **Blameless incident retro** | Within 48h of P1/P2 | Root cause analysis, action items, process improvements | Incident commander (rotating) | Retro doc with action items (tracked in backlog) |
| **Monthly engineering all-hands** | Monthly, 45 min | Share progress on culture/delivery metrics, recognize teams, surface cross-team issues | VP Eng | Slide deck with metrics + recognition |
| **Quarterly architecture review** | Quarterly, 90 min | Review module ownership, coupling metrics, Conway's Law alignment, platform roadmap | VP Eng + senior engineers | Architecture decision record (ADR) if changes needed |
| **Cross-functional sync** (PM + Eng leads) | Weekly, 30 min | Align on priorities, surface blockers, review experiment results, address collaboration friction | PM lead + Eng leads | Written summary of decisions and action items |

### Metrics + Guardrails

**Outcome metrics (what we're trying to achieve):**
1. Deploy frequency: >=1/day per team (measured via deploy pipeline logs)
2. P1 incidents/month: <=1 (measured via incident tracker)
3. PR cycle time (median): <24 hours (measured via GitHub metrics)
4. DevEx satisfaction: improvement over baseline (measured via quarterly survey)

**Leading indicators (early signals of progress):**
1. Time-to-first-review: <4 hours median (shows review SLA is working)
2. Average PR size: decreasing trend (shows "ship small" culture taking hold)
3. Platform ticket queue length: decreasing (shows self-service is working)
4. Retro action item completion rate: >80% (shows accountability loop is working)

**Guardrails (what must not get worse):**
1. Change failure rate: must stay <10%, target <5% (if it rises, slow down)
2. MTTR: must decrease or stay flat (instrument within 30 days)
3. Customer-reported bugs: must not increase (track via support volume)
4. Engineer burnout: monitor via DevEx survey; on-call load must be distributed evenly

**Instrumentation gaps + owners:**
| Gap | Owner | Target date |
|---|---|---|
| MTTR tracking (no incident tracker with timestamps) | Platform lead | Day 14 |
| Change failure rate (no automated tracking) | Platform lead | Day 30 (tied to CD pipeline) |
| Deploy frequency per team (manual deploys not tracked) | Platform lead | Day 30 (automated with CD) |
| DevEx survey (does not exist yet) | VP Eng | Day 14 |
| Experiment throughput (no tracking) | PM lead + Data | Day 60 |

---

## 7) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **CD pipeline takes longer than 6 weeks** | Medium | High -- daily deploys blocked | Start with 1 team as pilot; other teams use streamlined manual process in parallel; timebox to 8 weeks max before escalating |
| **Feature teams resist owning on-call** | Medium | High -- ownership culture fails to take hold | VP Eng communicates expectation clearly; provide on-call training and runbooks; ensure compensation/time-off policy is fair; make it non-negotiable |
| **Module boundaries in monolith are wrong** | Medium | Medium -- CODEOWNERS creates friction in wrong places | Treat initial mapping as v0; review cross-module PR metrics monthly; adjust boundaries based on data |
| **Platform team is stretched too thin** | High | High -- self-service AND CD pipeline both delayed | Sequence carefully: CD pipeline first (highest impact); self-service second; consider temporary contractor support for platform |
| **PR cycle time improves but quality drops** | Low | High -- more P1s would undermine the entire effort | Change failure rate guardrail; require tests in PRs; monitor P1 trend weekly; if CFR >10% for 2 weeks, pause and investigate |
| **Culture change is superficial (values poster syndrome)** | Medium | Medium -- rituals happen but behaviors do not change | VP Eng must model the behaviors; celebrate examples in all-hands; address violations directly; measure via DevEx survey, not just process compliance |

### Open Questions

1. **What is the current CI/CD stack?** The CD pipeline approach depends on whether CI is already solid (fast, reliable, good test coverage) or needs investment first.
2. **What is the test coverage and flake rate?** If CI is unreliable, daily deploys will be painful. A CI reliability sprint may need to come before or in parallel with CD.
3. **What is the actual MTTR for recent P1 incidents?** This baseline is critical for measuring improvement.
4. **Are the 3 Go microservices well-documented and tested?** Knowledge transfer to feature teams will be harder if there are no runbooks or tests.
5. **What work tracker does the org use?** The workflow contract assumes a modern tracker (Linear/Jira) -- if the org uses something else, adjust accordingly.
6. **Is there executive sponsorship beyond VP Eng?** Culture change at this scale benefits from CEO/CTO backing, especially for the platform repositioning.
7. **What is the on-call compensation/time-off policy?** Team-owned on-call will face resistance if engineers feel it is uncompensated labor.
8. **Are there compliance or security constraints on deploy frequency?** Some B2B customers may require change windows or audit trails that affect daily deploy feasibility.

### Next Steps (smallest next actions)

| # | Action | Owner | By when |
|---|---|---|---|
| 1 | VP Eng reviews this pack and confirms scope, team assignments, and any corrections to assumptions | VP Eng | This week |
| 2 | Map monolith modules to teams (draft) | Senior engineer from each team | This week |
| 3 | Create CODEOWNERS file based on module mapping | Tech lead | This week |
| 4 | Announce review SLA (4h / 24h) to all engineers | VP Eng | This week |
| 5 | Send DevEx baseline survey (10 questions) | VP Eng | This week |
| 6 | Draft on-call rotation schedule per team | Team leads | Week 2 |
| 7 | Platform lead creates CD pipeline design doc | Platform lead | Week 2 |
| 8 | Schedule cross-functional sync (PM + Eng leads) | VP Eng + PM lead | Week 1 |

---

## Quality Gate Self-Assessment

| Checklist item | Status |
|---|---|
| Scope and boundaries explicit | PASS -- scope is full eng org, decision owner identified, timeline stated |
| 2-5 concrete symptom examples | PASS -- 4 symptoms with evidence |
| Capability map (tech/arch/cultural/mgmt) | PASS -- all 4 buckets covered with evidence and gaps |
| Stated vs lived culture distinguished | PASS -- random on-call and "going dark" are lived culture vs. likely stated values of ownership |
| 3-7 culture code principles with behaviors/rules | PASS -- 5 principles, each with do/don't, decision rules, anti-patterns, signals |
| Conway's Law analysis with transition steps and trade-offs | PASS -- 3 misalignments, 3 proposed changes with transition plans and trade-offs |
| Clock speed targets and guardrails | PASS -- targets and guardrails table with specific thresholds |
| Backlog items with owners, effort, dependencies, metrics | PASS -- 12 initiatives with all fields |
| 1-2 "start this week" actions | PASS -- 3 quick wins for first 2 weeks, 8 actions for this week |
| Workflow contract (issue to PR to deploy to learn) | PASS -- 5-stage workflow with SLAs, escalation paths, non-engineer participation |
| AI norms with human checks | PASS -- 6 AI norm categories defined |
| 30/60/90 rollout with rituals and measurement | PASS -- detailed 30/60/90 with weekly actions, 5 rituals, 4+4+4 metrics/indicators/guardrails |
| Risks, open questions, next steps included | PASS -- 6 risks, 8 open questions, 8 next steps |
| Internal consistency (principles match workflows match metrics) | PASS -- e.g., "Ship Small" principle connects to PR size metric, CD pipeline initiative, and deploy frequency target |

### Rubric Self-Scores

| Dimension | Score | Notes |
|---|---|---|
| Clarity of scope and contracts | 5 | Clear boundaries, inputs, deliverables, success criteria |
| Evidence-based diagnosis | 4 | Evidence supports all claims; some metrics are estimated (labeled); instrumentation gaps identified |
| Capability model completeness | 5 | All 4 buckets addressed with initiatives |
| Actionability and specificity | 5 | Prioritized backlog with owners, effort, dependencies, metrics |
| Org/architecture alignment | 5 | 3 misalignments with evidence, proposed changes, transition plans, trade-offs |
| Clock speed + quality guardrails | 5 | Targets, guardrails, concrete system improvements, connected to metrics |
| Workflow contract + cross-functional fit | 5 | End-to-end workflow, SLAs, escalation, non-engineer participation, failure modes |
| AI-assisted development norms | 4 | Allowed uses, human checks, data handling defined; edge cases (e.g., AI in incident response) not addressed |
| Rollout and reinforcement | 5 | 30/60/90 plan, 5 rituals, metrics, guardrails, feedback loops |
