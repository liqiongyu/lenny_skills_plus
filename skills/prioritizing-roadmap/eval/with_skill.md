# Roadmap Prioritization Pack — Team Collaboration SaaS, Q2

---

## 0) Context Snapshot

- **Product:** Team collaboration SaaS
- **Primary customer segment:** 10-200 person tech companies; team leads
- **Decision to make (and deadline):** Pick Q2 roadmap themes and top 8 initiatives; decision in 2 weeks
- **Horizon + cadence:** Next quarter (Q2); refresh quarterly; rolling 12-month view maintained
- **North Star / primary goal:** Weekly active teams completing >=1 project
- **Guardrails:**
  1. Support tickets per new team (must not increase)
  2. Net revenue churn (must not increase)
  3. Crash-free session rate (must not decrease)
  4. Gross margin (must stay above threshold)
  5. NPS among team leads (must not decline)
- **Constraints:**
  - 6 engineers, 1 designer
  - Must complete SSO launch (hard commitment to enterprise deals)
  - Platform migration dependency in May (blocks certain backend work until migration completes)
- **Stakeholders:**
  - Head of Product — decider
  - Eng Manager — approver (capacity + feasibility)
  - Growth PM — contributor (activation + growth inputs)
  - CS lead — contributor (retention + support inputs)
- **Notes / assumptions:**
  - 15 candidate initiatives sourced from backlog, customer requests, and internal ideas
  - Sales is pushing enterprise features; product wants to protect the activation funnel
  - Platform migration expected to complete mid-May; work that depends on it cannot start until then
  - Designer capacity is the tightest constraint (1 designer across all initiatives)

---

## 1) Season Framing

### Season Name
**"Season of Activation Reliability"**

### Why Now (What Changed)
- **Activation has plateaued:** New team sign-ups are growing, but the percentage reaching their first completed project has been flat for two quarters. The growth engine is leaking at the top of the funnel.
- **Reliability is eroding trust:** Support ticket volume for onboarding-related errors spiked 30% last quarter. Trial-to-paid conversion dipped alongside crash-free session rate.
- **Enterprise demand is real but constrained:** Five active enterprise deals are blocked on SSO. However, the team cannot pursue a full enterprise suite this quarter without sacrificing activation work.
- **Platform migration creates a forcing function:** The May migration will temporarily limit backend work but will unlock performance and scalability improvements for H2. Sequencing around this dependency is critical.

### Season Bets (5)
1. **Improve time-to-first-project for new teams** — Reduce friction from sign-up to first completed project.
2. **Eliminate reliability blockers in onboarding** — Fix the errors and crashes that prevent new users from reaching the value moment.
3. **Increase team collaboration depth** — More team members actively participating means stronger retention and stickier adoption.
4. **Deliver SSO as the enterprise "wedge"** — Unblock enterprise deals without derailing activation focus.
5. **Build a foundation for Q3 growth** — Use the platform migration window to set up infrastructure that supports faster iteration later.

### Non-Goals (5)
- **Full enterprise admin suite** — Beyond SSO and basic roles, enterprise admin features are deferred to a future season when we have evidence of adoption.
- **Pricing or packaging overhaul** — Monetization experiments are out of scope this quarter; current plans are performing adequately.
- **Major UI redesign** — No visual overhaul unrelated to activation and reliability improvements.
- **New product lines or integrations marketplace** — Exploratory new verticals or a third-party integration platform are deferred.
- **Mobile app feature parity** — Mobile improvements beyond critical bug fixes are postponed; desktop/web is the primary activation path.

### Success Criteria
- **Primary metric (common currency):** Weekly active teams completing >=1 project (target: +12-18% by end of Q2)
- **Guardrails:**
  - Support tickets per new team: no increase (target: -10%)
  - Net revenue churn: does not increase quarter-over-quarter
  - Crash-free session rate: >=99.5%
  - Gross margin: maintained above current threshold
  - NPS among team leads: does not decline

---

## 2) Opportunity Inventory (Truth vs. Hypotheses)

15 candidate initiatives normalized into problem/outcome statements, tagged by conviction level.

| # | Opportunity | Target Segment | Problem Statement | Intended Outcome Metric/Driver | Conviction | Evidence | Effort | Dependencies | Track |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Guided setup wizard + starter templates | New teams | Teams don't know how to configure their workspace or start a first project; many abandon before reaching value | Time-to-first-project; activation rate | Belief | Funnel data shows 40% drop at "create first project" step; CS hears confusion weekly; competitors have guided flows | M | Designer (high) | Delivery |
| 2 | Onboarding reliability bug fixes | All new users | Errors and crashes during onboarding block early progress and erode trust | Crash-free sessions; activation completion rate | Known | Error logs show 3 critical bugs; support tickets up 30%; correlated with activation drop | M | Platform migration (partial) | Delivery |
| 3 | Invite flow redesign | New teams | Teams fail to invite collaborators during onboarding, limiting perceived value and reducing stickiness | % projects with >=2 collaborators | Belief | Cohort analysis: teams with 3+ members in week 1 have 2.4x higher retention; current invite flow has 25% completion rate | S | Designer (low) | Delivery |
| 4 | SSO implementation (must-do) | Enterprise prospects | Enterprise trials cannot proceed without SSO; 5 deals worth ~$400K ARR are blocked | Enterprise trial-to-paid conversion; ARR | Known | 5 active deals explicitly blocked; sales pipeline data; security review completed | L | Security review (done); Eng capacity (high) | Delivery |
| 5 | Real-time collaboration (co-editing) | Active teams | Teams switch to other tools for real-time work because our product lacks co-editing, reducing engagement depth | Weekly active teams; session duration | Belief | Feature request is #1 in feedback portal (200+ votes); 3 churned accounts cited this; competitive gap | L | Platform migration (blocked until mid-May) | Delivery |
| 6 | Project status dashboard for team leads | Team leads | Team leads lack visibility into project progress across their teams, leading to status meetings and workarounds | Team lead weekly active usage; projects completed | Belief | 15 customer interviews cite "visibility" as top pain; team leads are 60% of our power users | M | None | Delivery |
| 7 | Notification and digest overhaul | All users | Notification fatigue causes users to ignore updates, missing important project changes | DAU; return visit rate | Hypothesis | Anecdotal complaints; no quantitative data on notification engagement; some churn exit surveys mention "noise" | M | None | Discovery |
| 8 | Admin roles (phase 1 - basic) | Enterprise teams | Admins at larger companies need minimal role-based access control to manage team permissions | Enterprise activation; reduced security-related support tickets | Hypothesis | Anecdotal feedback from 3 enterprise prospects; no usage data yet; depends on SSO being live | M | SSO (must complete first) | Discovery |
| 9 | Performance optimization (page load speed) | All users | Slow page loads (>3s on key screens) frustrate users and correlate with lower engagement | Page load time; session depth; crash-free rate | Known | Performance monitoring shows p95 load time of 4.2s on dashboard; correlated with lower retention cohorts | S | Platform migration (benefits from it) | Delivery |
| 10 | Automated project archiving + cleanup | Active teams | Completed and abandoned projects clutter the workspace, making it harder to find active work | Projects completed (by reducing noise); team lead satisfaction | Belief | CS reports this as a frequent complaint for teams with 20+ projects; no quantitative impact data | S | None | Delivery |
| 11 | API for third-party integrations | Power users / developers | Technical teams want to connect our product to their existing tool stack (Slack, Jira, GitHub) | Retention of technical teams; expansion revenue | Hypothesis | 8 feature requests from large accounts; competitive products have APIs; no prototype or validation | L | Platform migration (better to build on new platform) | Discovery |
| 12 | Custom project workflows | Mid-market teams | Teams with specific processes (e.g., agile, design sprints) cannot customize project stages, forcing workarounds | Activation of mid-market segment; projects completed | Hypothesis | 12 customer requests; 2 churned accounts mentioned rigidity; no prototype tested | M | Designer (medium) | Discovery |
| 13 | In-app help + contextual tooltips | New users | Users get stuck on features and leave rather than finding help; current help center is external and hard to navigate | Support tickets per new team; activation rate | Belief | Support ticket analysis: 35% of new-user tickets are "how do I do X"; help center bounce rate is high | S | None | Delivery |
| 14 | Team health / activity analytics | Team leads | Team leads cannot identify disengaged team members or stalled projects without manual checking | Team lead retention; weekly active teams | Hypothesis | Mentioned in 5 customer interviews; no quantitative validation; could be a differentiator | M | Project status dashboard (builds on it) | Discovery |
| 15 | Do nothing / invest in quality + tech debt | All users | Accumulated tech debt slows feature velocity and increases bug rate; doing nothing has an opportunity cost | Engineering velocity; bug rate; crash-free rate | Known | Sprint velocity has declined 15% over 3 quarters; tech debt tickets are 25% of backlog | S-M | Platform migration (aligns well) | Delivery |

**Discovery backlog (needs validation before committing):** #7 Notification overhaul, #8 Admin roles, #11 API integrations, #12 Custom workflows, #14 Team health analytics

**Delivery backlog (ready to commit):** #1 Guided setup, #2 Reliability bugs, #3 Invite flow, #4 SSO, #5 Real-time collaboration, #6 Project status dashboard, #9 Performance optimization, #10 Automated archiving, #13 In-app help, #15 Quality/tech debt investment

---

## 3) Scoring Model (Common Currency + ICE)

### Common Currency
**North Star units: Weekly active teams completing >=1 project** (target: +12-18% by end of Q2)

For initiatives that don't directly move the North Star (e.g., SSO, tech debt), we convert to the common currency via proxy:
- SSO: measured by enterprise trial conversion, which feeds into active teams within 1-2 quarters
- Tech debt: measured by engineering velocity recovery, which accelerates future North Star impact

### ICE Scales

**Impact (0-5):** Expected delta in weekly active teams completing >=1 project within Q2.
- 5 = Step-change impact (>10% lift in North Star within the quarter)
- 4 = Strong impact (5-10% lift)
- 3 = Meaningful impact (2-5% lift)
- 2 = Moderate impact (1-2% lift) or indirect/delayed impact
- 1 = Marginal impact (<1%) or unclear time-to-impact

**Confidence (0-5):** Based on evidence quality, not optimism.
- 5 = Strong evidence (quantitative data + repeated customer signal + successful precedent)
- 4 = Good evidence (directional data + strong qualitative signal)
- 3 = Some evidence (directional data or strong qualitative signal, but gaps)
- 2 = Weak evidence (mostly qualitative, limited data)
- 1 = Mostly hypothesis (intuition, anecdotal)

**Ease (0-5):** Relative cost/complexity, factoring in capacity and dependencies.
- 5 = Small scope, no dependencies, can ship in 1-2 weeks
- 4 = Small-medium scope, minimal dependencies, 2-4 weeks
- 3 = Medium scope, some dependencies, 4-6 weeks
- 2 = Medium-large scope, significant dependencies, 6-8 weeks
- 1 = Large scope, many dependencies, 8+ weeks or blocked

### Scoring Table

| # | Opportunity | Common-Currency Impact (range) | Impact (0-5) | Confidence (0-5) | Ease (0-5) | ICE Score | Key Assumptions | Notes |
|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | Guided setup wizard + templates | +5-10% activation lift | 4 | 3 | 3 | 36 | Templates reduce friction; new users complete first project faster; requires designer | Top tier |
| 2 | Onboarding reliability bug fixes | +3-7% activation lift | 3 | 4 | 3 | 36 | Bug fixes remove blockers; impact shows within weeks; some fixes blocked by migration | Top tier |
| 3 | Invite flow redesign | +2-4% activation lift | 3 | 3 | 4 | 36 | Small UI changes increase invite completion; more collaborators = higher retention | Top tier |
| 13 | In-app help + contextual tooltips | +2-4% activation lift | 3 | 3 | 4 | 36 | Reduces support tickets; helps new users self-serve; quick to implement | Top tier |
| 9 | Performance optimization | +1-3% retention lift | 2 | 4 | 4 | 32 | Faster loads improve engagement; benefits amplified post-migration | Strong |
| 15 | Quality / tech debt investment | +0-2% (indirect, enables future velocity) | 2 | 4 | 3 | 24 | Recovers 15% velocity decline; reduces bug rate; aligns with migration window | Enabler |
| 6 | Project status dashboard | +2-4% team lead retention lift | 3 | 3 | 2 | 18 | Team leads are power users; visibility increases engagement; medium effort | Good but lower ease |
| 10 | Automated project archiving | +1-2% activation lift | 2 | 3 | 4 | 24 | Reduces clutter for active teams; quick win; lower impact ceiling | Quick win |
| 4 | SSO (must-do) | Indirect (enterprise pipeline) | 2 | 5 | 1 | 10 | Doesn't move North Star directly this quarter; required commitment; large effort | Must-do regardless of score |
| 5 | Real-time collaboration | +4-8% engagement lift | 4 | 3 | 1 | 12 | High impact but large scope and blocked by migration; best for late Q2 or Q3 | Blocked until mid-May |
| 7 | Notification overhaul | +1-3% DAU lift | 2 | 1 | 3 | 6 | Hypothesis only; needs discovery; anecdotal evidence | Discovery first |
| 8 | Admin roles (phase 1) | Indirect (enterprise) | 2 | 1 | 2 | 4 | Depends on SSO; anecdotal need; no usage data | Discovery after SSO |
| 12 | Custom project workflows | +1-3% mid-market activation | 2 | 2 | 2 | 8 | Some customer requests; no prototype; medium effort | Discovery first |
| 11 | API for integrations | +1-3% power user retention | 2 | 1 | 1 | 2 | Large scope; needs new platform; hypothesis | Discovery; defer to H2 |
| 14 | Team health analytics | +1-2% team lead retention | 2 | 1 | 2 | 4 | No quantitative validation; depends on dashboard | Discovery after #6 |

---

## 4) Shortlist + Parking Lot

### Applying Constraints

**Capacity:** 6 engineers, 1 designer for approximately 12 weeks. Rough capacity: ~72 engineer-weeks, ~12 designer-weeks.

**Hard commitments:** SSO must ship (~16-20 engineer-weeks, ~2 designer-weeks).

**Remaining capacity after SSO:** ~52-56 engineer-weeks, ~10 designer-weeks.

**Dependency gate:** Platform migration completes mid-May; migration-dependent work can start in the second half of Q2.

### Stress-Test Scenarios

**Base scenario (recommended):** Assume migration completes on schedule mid-May; activation improvements are the primary focus; SSO ships on time.

**Conservative scenario:** Migration slips 2-3 weeks; one fewer engineer available due to migration support; only 6 initiatives fit.

**Aggressive scenario:** Migration completes early May; reliability fixes are smaller than estimated; capacity opens for real-time collaboration kickoff in late Q2.

### Shortlist — Top 8 Initiatives (Base Scenario)

| Rank | Initiative | Rationale | Est. Effort | Quarter Timing |
|---|---|---|---:|---|
| 1 | **SSO implementation** (must-do) | Hard commitment; unblocks $400K enterprise pipeline | 16-20 eng-weeks, 2 designer-weeks | Full quarter (start immediately) |
| 2 | **Onboarding reliability bug fixes** | Highest-confidence activation blocker; Known evidence; quick wins possible pre-migration, deeper fixes post-migration | 8-10 eng-weeks | Early Q2 (quick wins) + late Q2 (migration-dependent) |
| 3 | **Guided setup wizard + starter templates** | Highest-impact activation initiative; addresses the biggest funnel drop-off | 8-10 eng-weeks, 4 designer-weeks | Early-to-mid Q2 |
| 4 | **Invite flow redesign** | High ICE; small scope; compounds with guided setup to improve team activation | 3-4 eng-weeks, 2 designer-weeks | Early Q2 |
| 5 | **In-app help + contextual tooltips** | High ICE; small scope; reduces support tickets and supports activation | 3-4 eng-weeks, 1 designer-week | Mid Q2 |
| 6 | **Performance optimization** | High confidence; benefits from migration; improves experience for all users | 4-6 eng-weeks | Late Q2 (post-migration) |
| 7 | **Automated project archiving** | Quick win; improves active team experience; low effort | 2-3 eng-weeks | Mid Q2 (fill gaps) |
| 8 | **Quality / tech debt investment** | Recovers engineering velocity; aligns with migration window; enables faster Q3 delivery | 4-6 eng-weeks | Throughout Q2 (20% time allocation) |

**Total estimated effort:** ~48-63 engineer-weeks, ~9 designer-weeks. Fits within capacity with buffer for unknowns.

### Parking Lot (Not This Quarter)

| Initiative | Reason for Deferral | Recommended Next Step |
|---|---|---|
| Real-time collaboration (#5) | Large scope; blocked by migration; high impact but cannot ship meaningfully in Q2 | Begin technical design in late Q2; target Q3 as a flagship initiative |
| Project status dashboard (#6) | Good initiative but lower ease; designer capacity is fully allocated to activation work | Scope a lightweight v1 for Q3; gather more team-lead feedback |
| Admin roles - phase 1 (#8) | Insufficient evidence; depends on SSO shipping first | Run discovery interviews with 5 enterprise prospects post-SSO launch |
| Custom project workflows (#12) | Hypothesis-level conviction; medium effort with no validated demand | Prototype and test with 3-5 mid-market teams in Q2 (discovery only) |
| Notification overhaul (#7) | Hypothesis only; no quantitative data on impact | Instrument notification engagement metrics in Q2; decide in Q3 |
| API for integrations (#11) | Large scope; better built on new platform post-migration | Defer to H2; document requirements from top 5 integration requests |
| Team health analytics (#14) | No quantitative validation; depends on dashboard shipping first | Defer until project status dashboard ships |

### Key Tradeoffs Made Explicit
- **Activation over enterprise expansion:** Beyond SSO, enterprise features (admin roles, API) are deferred. We are betting that improving activation for our core ICP (10-200 person tech companies) is the highest-leverage move.
- **Many small wins over one big bet:** Real-time collaboration is the most requested feature but cannot ship in Q2 given scope and migration dependency. We chose multiple high-confidence, medium-scope initiatives instead.
- **Designer bottleneck shapes sequencing:** With 1 designer, we must sequence design-heavy work (guided setup, invite flow) carefully. In-app help and archiving require less design support.

---

## 5) Roadmap Draft

### Now / Next / Later

| Now (Weeks 1-4) | Next (Weeks 5-8) | Later (Weeks 9-12 + Beyond) |
|---|---|---|
| **SSO implementation** (start; runs through quarter) | **Guided setup wizard + templates** (design done; build + iterate) | **Performance optimization** (post-migration) |
| **Onboarding reliability bug fixes** (quick wins, pre-migration fixes) | **In-app help + contextual tooltips** (build + ship) | **Onboarding reliability bug fixes** (migration-dependent fixes) |
| **Invite flow redesign** (design + build; small scope) | **Automated project archiving** (build + ship) | **Real-time collaboration** (technical design begins; Q3 flagship) |
| **Quality / tech debt** (ongoing 20% allocation) | **Quality / tech debt** (ongoing 20% allocation) | **Admin roles discovery** (post-SSO interviews) |
| **Guided setup wizard** (design phase) | **SSO implementation** (complete + launch) | **Project status dashboard** (scope v1 for Q3) |

### Q2 Themes

| Theme | Key Initiatives | % of Capacity |
|---|---|---|
| **Activation: Remove friction to first project** | Guided setup wizard, Invite flow redesign, In-app help | ~35% |
| **Reliability: Earn trust through stability** | Onboarding bug fixes, Performance optimization, Quality/tech debt | ~30% |
| **Enterprise: Deliver the SSO wedge** | SSO implementation | ~25% |
| **Housekeeping: Quick wins** | Automated archiving | ~5% |
| **Buffer for unknowns** | Unallocated | ~5% |

### Portfolio Balance Check
- **Core (stability + quality):** Reliability bug fixes, performance optimization, tech debt (~30%) -- strong
- **Growth (activation + expansion):** Guided setup, invite flow, in-app help (~35%) -- strong
- **Enterprise / revenue:** SSO (~25%) -- adequate given constraints
- **Big bets / exploration:** Real-time collaboration design begins; discovery for admin roles, custom workflows (~5%) -- light this quarter, intentionally so; Q3 will shift toward bigger bets post-migration

### Rolling Plan Cadence
- **Rolling horizon:** 12 months (theme-level beyond Q2)
- **Refresh cadence:** Quarterly; major strategic re-plan every 6 months (next: end of Q2)
- **Update triggers:**
  - Platform migration completes or slips significantly
  - North Star metric moves >5% in either direction
  - Major competitive move or market shift
  - Enterprise pipeline changes materially (e.g., large deal requiring new commitment)

---

## 6) Decision Narrative (Why These, Why Now)

### One-Paragraph Summary

Q2 is the **"Season of Activation Reliability."** Our core growth engine -- new teams reaching their first completed project -- has stalled despite healthy top-of-funnel sign-ups. The evidence is clear: onboarding errors block progress, the setup experience confuses new teams, and invite flows leak collaborators. Meanwhile, five enterprise deals worth $400K ARR are stuck on SSO. This quarter, we will focus 65% of capacity on activation and reliability improvements that directly move our North Star (weekly active teams completing >=1 project) and 25% on delivering SSO as the enterprise wedge. We are explicitly choosing not to pursue large new features (real-time collaboration, API integrations, enterprise admin) until we have fixed the foundation, shipped SSO, and completed the platform migration. This discipline sets up Q3 for bigger bets on a stronger platform.

### Top Reasons
- **Activation is the bottleneck:** Growing sign-ups without fixing activation is wasting acquisition spend. The guided setup wizard targets the biggest single funnel drop-off (40% at "create first project").
- **Reliability is eroding trust:** Known bugs are directly correlated with lower trial-to-paid conversion. These are the highest-confidence items on the list.
- **SSO is a must-do commitment:** $400K in pipeline is blocked. Delivering SSO this quarter earns enterprise credibility without requiring a full enterprise suite.
- **Small wins compound:** Invite flow, in-app help, and archiving are low-effort, high-confidence improvements that reinforce the activation theme.
- **Tech debt investment protects velocity:** A deliberate 20% allocation to quality and tech debt prevents further velocity decline and aligns with the migration window.

### Non-Goals (Explicit "No's")
- **Real-time collaboration:** Our most-requested feature, but too large to ship meaningfully in Q2 with migration constraints. We will begin technical design in late Q2 and target it as the Q3 flagship. This is a sequencing decision, not a deprioritization.
- **Project status dashboard:** Valuable for team leads but lower priority than removing activation blockers. Scoped for Q3.
- **Enterprise admin suite:** Beyond SSO, enterprise features are deferred until we see adoption data from SSO launch.
- **API / integrations platform:** Best built on the new platform post-migration. Deferred to H2.
- **Pricing overhaul, mobile feature parity, major UI redesign:** Out of scope this season.

### Think Bigger (Required)

**Big bet 1: "Instant team setup" -- one-click workspace with auto-generated project plan**
- Why it matters: Compresses time-to-value from days to minutes; could be the single biggest activation lever
- What we'd need to believe/learn: Users trust AI-generated defaults; template quality doesn't degrade perceived value; works across team sizes
- Discovery next step: Build a prototype that auto-generates a project from a 3-question intake; test with 10 new teams; measure setup completion rate vs. current flow (Growth PM, Q2 discovery)

**Big bet 2: "Collaboration multiplier" -- AI-powered team activity digest + smart follow-ups**
- Why it matters: Solves both notification fatigue and team lead visibility in one experience; could differentiate us from competitors
- What we'd need to believe/learn: Users engage with AI-generated summaries; accuracy is high enough to be trusted; doesn't feel intrusive
- Discovery next step: Mock up a weekly digest email powered by project activity data; send to 50 team leads; measure open rate and qualitative feedback (Growth PM, late Q2)

**Big bet 3: "Integration-first onboarding" -- connect Slack/GitHub/Jira during setup, auto-populate projects**
- Why it matters: Reduces setup effort dramatically for technical teams; makes our product the hub rather than another tool to check
- What we'd need to believe/learn: Teams will authorize integrations during onboarding (trust barrier); auto-populated projects are useful, not noisy
- Discovery next step: Survey 20 technical teams on integration willingness during setup; prototype one integration (Slack) on new platform (Eng Manager, Q3)

---

## 7) Alignment + Communication Plan

| Audience | What They Need | Format | Frequency | Owner |
|---|---|---|---|---|
| Leadership team | Strategic rationale, North Star targets, resource allocation, key risks | Roadmap review deck + narrative memo | Decision meeting (this week); monthly update | Head of Product |
| Engineering team | Initiative scope, sequencing, dependencies, migration coordination | Sprint planning docs + roadmap board | Bi-weekly sprint planning; weekly standup | Eng Manager |
| Design | Design brief per initiative; priority sequence; capacity plan | Design brief docs + 1:1 | Weekly design sync | Head of Product + Designer |
| Sales | SSO timeline; what we are/aren't building for enterprise; talking points | Sales enablement memo + FAQ | At launch of roadmap; monthly update | Growth PM |
| Customer Success | What's changing for customers; support ticket reduction initiatives; timeline | CS brief + updated help docs | At launch; bi-weekly sync | CS Lead |
| Broader company | Season theme; top priorities; how to submit new inputs | All-hands update + async doc | Quarterly all-hands; roadmap doc always accessible | Head of Product |

### Roadmap Update Mechanism
- **Single source of truth:** Roadmap board in the team's project management tool, linked from the company wiki. The board shows Now/Next/Later with status, owners, and dependencies.
- **How new inputs are handled:** New requests go to the Growth PM for triage. Items that could change the top 8 are flagged for the next bi-weekly roadmap check-in. Nothing enters "Now" without Head of Product approval.
- **How/when priorities are re-scored:** Full re-score at the quarterly refresh. Mid-quarter re-score only if an update trigger fires (migration slip, major metric shift, new enterprise commitment).

---

## 8) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Platform migration slips past mid-May** | Medium | High -- blocks reliability fixes, performance optimization, and delays real-time collaboration design | Eng Manager to provide weekly migration status updates; have a "conservative scenario" plan that shifts migration-dependent work to Q3; pre-identify which reliability fixes can be done independently |
| **SSO takes longer than estimated** | Medium | Medium -- consumes more capacity, crowding out activation work | Scope SSO to minimum viable (SAML 2.0 only, no SCIM); weekly check-ins on progress; if >20% over estimate by week 6, descope one lower-priority initiative |
| **Designer bottleneck causes delays** | Medium | Medium -- guided setup and invite flow require significant design work | Sequence design work carefully (invite flow first, then guided setup); use existing component library to reduce design effort; Head of Product to do content/copy work to free up designer |
| **Activation improvements don't move the North Star** | Low-Medium | High -- quarter's thesis is wrong | Instrument activation funnel metrics before shipping; run A/B tests where possible; have a "pivot trigger" -- if first two activation initiatives show <1% lift after 4 weeks, reassess |
| **Enterprise deals close before SSO ships** | Low | Medium -- lost revenue | Communicate realistic timeline to sales; offer manual SSO provisioning for largest deal if needed |

### Open Questions

| Question | Why It Matters | Owner | Deadline |
|---|---|---|---|
| Is the activation bottleneck primarily "setup confusion" or "reliability/crashes"? | Determines whether guided setup or bug fixes should get more investment | Growth PM (cohort analysis) | Week 1 of Q2 |
| Which onboarding reliability bugs can be fixed independently of the platform migration? | Determines how much reliability work can start immediately vs. waits for May | Eng Manager (technical assessment) | Week 1 of Q2 |
| What is the minimum SSO scope that unblocks enterprise deals? | Prevents SSO scope creep from consuming activation capacity | Head of Product + Sales | Before roadmap decision meeting |
| How much designer time does the guided setup wizard actually require? | Designer capacity is the tightest constraint; overestimate here delays other work | Designer (effort estimate) | Week 1 of Q2 |
| Should real-time collaboration technical design start in Q2 or wait for Q3? | Starting design now accelerates Q3 delivery but consumes engineering attention | Head of Product + Eng Manager | Week 4 of Q2 |

### Next Steps

| # | Action | Owner | Deadline |
|---|---|---|---|
| 1 | Run cohort analysis to validate activation bottleneck assumptions (setup confusion vs. reliability) | Growth PM | 1 week from now |
| 2 | Eng Manager to assess which reliability bugs are migration-independent and produce a phased fix plan | Eng Manager | 1 week from now |
| 3 | Schedule roadmap decision meeting with all stakeholders; share this pack for async review 2 days before | Head of Product | Within 5 business days |
| 4 | Confirm minimum SSO scope with sales team; document what is in/out | Head of Product | Before decision meeting |
| 5 | Designer to produce effort estimates for guided setup wizard and invite flow redesign | Designer | Before decision meeting |
| 6 | After decision meeting: update roadmap board, publish season brief to company, begin sprint planning | Head of Product + Eng Manager | Within 2 days of decision |
| 7 | Instrument activation funnel metrics (pre-ship baseline) for guided setup, invite flow, and in-app help | Growth PM + Engineering | Week 2 of Q2 |
| 8 | Schedule mid-quarter roadmap check-in (week 6) to assess progress and decide on migration-dependent work | Head of Product | Set calendar invite now |

---

## Quality Gate: Self-Assessment

### Checklist Results

| Checklist | Status | Notes |
|---|---|---|
| A) Decision framing | Pass | Decision, deadline, stakeholders, success criteria, constraints all explicit |
| B) Season framing | Pass | Season named; 4 "why now" bullets; 5 bets; 5 non-goals; success criteria mapped |
| C) Opportunity inventory | Pass | 15 items with problem statements, outcome metrics, conviction levels, evidence, effort, dependencies; discovery vs. delivery split |
| D) Scoring model | Pass | Common currency defined (North Star units); ICE scales with concrete anchors; assumptions documented per item |
| E) Roadmap draft | Pass | Now/Next/Later + quarterly themes; dependencies mapped; capacity allocated; parking lot explicit with rationale; rolling cadence defined |
| F) Alignment + communication | Pass | Decision narrative with "why now/these/not others"; 3 Think Bigger ideas; single source of truth; comms plan with audiences, cadence, owners |
| G) Final pack | Pass | All 8 deliverables included; plain language; Risks/Open questions/Next steps with owners and deadlines |

### Rubric Scores

| Category | Score (0-2) | Notes |
|---|---|---|
| Decision framing clarity | 2 | Decision, audience, deadline, success criteria explicit |
| Season framing usefulness | 2 | Clear season name, specific bets, explicit non-goals, compelling "why now" |
| Opportunity inventory quality | 2 | All 15 items have problem/outcome, evidence, conviction; discovery vs. delivery split |
| Common-currency scoring reproducibility | 2 | Scales defined with anchors; ICE model with documented assumptions |
| Tradeoffs explicitness | 2 | Parking lot with per-item rationale; constraints visibly shaped ranking; "no's" named with reasons |
| Roadmap coherence | 2 | Sequenced by dependencies and learning; capacity accounted for; rolling cadence defined |
| Balance (core/growth/quality/big bets) | 2 | Portfolio percentages stated; light big-bet allocation acknowledged and justified |
| Alignment readiness | 2 | Narrative clear; comms plan names channels, audiences, cadence; initiatives have owners |
| Risks/open questions/next steps | 2 | 5 specific risks with mitigations; 5 open questions with owners/deadlines; 8 next steps with actions/owners/timelines |

**Total: 18/18 — Strong. Ready to share and align.**
