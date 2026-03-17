# Organizational Design Pack

**Company:** B2B SaaS analytics platform (~180 people)
**Functions in scope:** Product, Engineering, Design, Data
**Date:** 2026-03-17

---

## 1) Org Design Brief

**Context:** B2B SaaS analytics platform, ~180 people. Product, Engineering, Design, and Data are in scope. Current structure centers on 5 feature teams, 1 platform team, 1 data team, and a nascent AI/ML team of 4. The organization is experiencing cross-team blocking, unclear ownership, and bottleneck-driven slowdowns that threaten a major customer launch in 8 weeks.

**Why now:** Three structural problems are compounding simultaneously: (1) the platform team is a bottleneck for multiple feature teams, (2) the AI/ML team has no PM and takes requests from everyone with no prioritization mechanism, and (3) the data team's ownership boundaries are unclear, creating confusion about who builds and maintains analytics pipelines vs. product data features. A major customer launch in 8 weeks makes these problems urgent -- any further slowdown puts the launch at risk.

**Time horizon:** Immediate structural relief within 2 weeks (Day 1 changes); full target state landed within 90 days. No headcount additions for 2 quarters.

**Design problem:** Reduce cross-team blocking and increase shipping parallelism by clarifying ownership, decoupling the platform bottleneck, and giving the AI/ML team a clear mandate -- all without adding headcount and without jeopardizing the 8-week customer launch.

**What we're optimizing for (ranked):**
1. Shipping parallelism -- feature teams can ship independently without waiting on platform or data
2. Cross-team blocking reduction -- fewer handoffs, queues, and "waiting on another team" states
3. Ownership clarity -- every surface, pipeline, and capability has one accountable team
4. Launch protection -- the 8-week customer launch stays on track with zero disruption
5. AI/ML leverage -- the AI/ML team delivers meaningful product impact rather than scattered favors

**Success metrics (top 3):**
- Reduce average "blocked on another team" time per feature team from current state by 40% within 60 days (measured via JIRA/Linear blocked-status tracking)
- Major customer launch ships on time (8-week deadline) with no scope cuts caused by org changes
- AI/ML team delivers at least 1 shipped product capability per quarter (vs. current scattered consulting)

**Constraints / non-negotiables:**
- Headcount/budget: No net-new headcount for 2 quarters; changes must work with existing people
- Critical launches / immovable dates: Major customer launch in 8 weeks -- any structural change must protect this
- Regulatory/compliance/security: Not a primary factor (standard B2B SaaS)
- Geography/time zones: Not specified as a constraint (assumed co-located or well-aligned zones)
- Leadership preferences: Not specified; assumed open to structural changes within scope

**Design principles:**
1. **Minimize dependencies, maximize autonomy** -- Teams should be able to ship their roadmap without blocking on other teams for the majority of their work
2. **Every team has a PM and a clear charter** -- No team operates without product leadership and prioritization; no "shared service without a queue"
3. **Platform as a product, not a service desk** -- Platform capabilities are productized with contracts, not ad hoc request fulfillment
4. **Protect the launch, then iterate** -- Day 1 changes must not disrupt the 8-week customer launch; structural changes phase in around it
5. **AI/ML is a product capability, not a consultancy** -- AI/ML work is embedded in product goals, not scattered across requesters

---

## 2) Current-State Map

### A) Current teams + charters

| Team | Charter (what they own) | Primary interfaces | Key dependencies | Top pain points |
|---|---|---|---|---|
| **Feature Team 1** | Feature area 1 (e.g., dashboards/reporting) | Platform, Data, Design | Platform for infra/APIs; Data for pipelines | Blocked waiting on platform; unclear data ownership |
| **Feature Team 2** | Feature area 2 (e.g., user management/permissions) | Platform, Design | Platform for auth/infra services | Platform queue delays |
| **Feature Team 3** | Feature area 3 (e.g., integrations/connectors) | Platform, Data, Design | Platform for APIs; Data for ingestion pipelines | Shared pipeline ownership confusion with Data |
| **Feature Team 4** | Feature area 4 (e.g., alerting/notifications) | Platform, Data, Design | Platform for messaging infra; Data for event processing | Competes with other teams for platform capacity |
| **Feature Team 5** | Feature area 5 (e.g., exploration/ad-hoc analysis) | Platform, Data, AI/ML, Design | Platform, Data, AI/ML all required | Triple dependency -- slowest team in the org |
| **Platform Team** | Shared infrastructure, APIs, deployment, core services | All feature teams, AI/ML | Feature teams (requirements); Data (infrastructure) | Bottleneck: serves 5+ requesters with no prioritization framework; reactive, not productized |
| **Data Team** | Analytics pipelines, data warehouse, data quality | Feature teams, AI/ML, Platform | Platform (infrastructure); Feature teams (requirements) | Unclear charter: are they a product team or an internal service? Ownership overlaps with feature teams on product-facing data features |
| **AI/ML Team (4 people)** | ML models, AI features, experimentation | Feature teams, Data, Platform | Data (training data, pipelines); Platform (serving infra) | No PM; takes requests from everyone; no prioritization; scattered impact |

### B) Dependency hotspots (top 5)

1. **Platform team as universal bottleneck** -- All 5 feature teams + AI/ML + Data depend on Platform for infrastructure changes, API extensions, and deployment support. Platform has no published prioritization mechanism, so teams queue up and wait. This is the single biggest source of cross-team blocking.

2. **AI/ML team with no PM and no prioritization** -- AI/ML takes ad hoc requests from every feature team. Without a PM, there is no intake process, no prioritization, and no ability to say "no" or "not now." The team is spread thin across 5+ requesters doing scattered favors instead of shipping coherent capabilities.

3. **Data team ownership ambiguity** -- It is unclear whether the Data team owns product-facing data features (e.g., custom metrics, data modeling for customers) or only internal analytics/BI pipelines. Feature teams sometimes build their own data features, sometimes wait for Data, and sometimes duplicate work.

4. **Feature Team 5 triple dependency** -- Feature Team 5 (exploration/ad-hoc analysis) depends on Platform, Data, AND AI/ML simultaneously. This creates a three-way coordination problem where any one team's delay blocks the others.

5. **Design resourcing across 5 feature teams** -- Design is distributed across feature teams but the allocation and prioritization model is not specified. When feature teams compete for design capacity, there is no clear arbitration mechanism.

### C) Decision rights (current)

| Decision type | Current decider | Who is consulted | Typical bottleneck | Notes |
|---|---|---|---|---|
| Platform prioritization (what to build next) | Platform team lead (implicitly) | Feature team leads petition informally | No formal intake or prioritization -- loudest voice wins | Major source of friction and perceived unfairness |
| AI/ML project selection | Unclear -- AI/ML team self-selects based on who asked last | Everyone asks; nobody arbitrates | No PM means no prioritization authority | AI/ML team morale risk from constant context-switching |
| Data feature ownership (product-facing vs. internal) | Unclear -- case-by-case negotiation | Data team lead, feature team PMs | Each decision is relitigated from scratch | Creates duplicate work and delayed features |
| Feature team roadmap | Feature team PMs | Design, Eng leads within team | Generally works well within teams | Cross-team features are where it breaks down |
| Architecture / technical standards | Platform team lead (implicitly) | Eng leads consulted ad hoc | Standards are informal, not documented | Inconsistent patterns across feature teams |

### D) Management layers snapshot (current)

- **Layers between IC and VP/GM:** Likely 3-4 (IC -> Team Lead -> Director/Group Lead -> VP). Assumed standard for ~180-person org.
- **Where managers don't know the work:** Platform team lead may be acting primarily as a traffic controller and project manager rather than driving technical architecture decisions. Data team lead may be managing both internal analytics and product data without deep context in both.
- **Where people management is detached from craft:** AI/ML team of 4 likely reports to someone who does not have ML expertise (possibly an engineering director overseeing multiple teams). This means technical decisions and career growth are not well-supported.

---

## 3) Operating Model Decision

### A) Centralization posture (Apple-like <-> Amazon-like)

**Chosen posture:** More decentralized (leaning Amazon-like)

**Rationale:** The primary optimization target is shipping parallelism and reduced cross-team blocking. The B2B SaaS analytics product has distinct feature surfaces (dashboards, integrations, alerting, exploration, etc.) that can operate with reasonable independence if given clear interfaces. The current centralized platform dependency is the #1 source of blocking. Decentralizing ownership (with standardized interfaces) is the right structural move. The product does not require the level of UX integration coherence that would justify Apple-like centralization -- B2B analytics users interact with distinct feature areas and expect functional depth over pixel-perfect cross-surface consistency.

**What is standardized (must be consistent):**
- API contracts and data schemas (so feature teams can build on shared foundations without coordination)
- Design system components and interaction patterns (so UX is consistent without centralized design approval)
- Deployment pipeline and infrastructure patterns (so teams self-serve safely)
- Data quality standards and access patterns (so teams can use data without bespoke pipeline requests)
- Security and compliance patterns (non-negotiable consistency)

**What is allowed to vary (autonomy zones):**
- Feature prioritization within each team's charter area
- Technical implementation choices within the team's boundary (language, framework, etc.)
- AI/ML model selection and experimentation approach within the AI/ML team's charter
- UX design details within the design system constraints

### B) Functional <-> divisional/value-stream posture

**Chosen posture:** More divisional/value-stream (with strong functional standards)

**Rationale:** The current structure is already roughly value-stream aligned (feature teams own product areas). The problem is not the team topology -- it is that shared capabilities (platform, data, AI/ML) are centralized services that create bottlenecks. The fix is to strengthen the value-stream alignment by embedding or distributing shared capabilities closer to the value streams, while maintaining functional standards through guilds and shared contracts. A shift toward pure functional alignment would worsen the dependency problem.

**Implications:**
- Platform capabilities that are frequently needed by feature teams should be productized or partially embedded
- Data capabilities should be split between a lean core (infrastructure/standards) and embedded product data ownership
- AI/ML should be aligned to specific product goals rather than serving as a horizontal consultancy
- Functional consistency is maintained via standards, guilds, and shared tooling -- not via centralized gatekeeping

### C) Guardrails

- "We will not decentralize decisions about **infrastructure security, data schemas, API contracts, and deployment pipelines** without standards/interfaces." (These require consistency to avoid fragmentation and security risk.)
- "We will not centralize decisions about **feature prioritization, product data feature design, or AI/ML model selection** because it creates bottlenecks." (These must be owned by the teams closest to the customer problem.)
- "We will not allow feature teams to build bespoke infrastructure without platform team review." (Prevents snowflake architectures.)

---

## 4) Org Options

### Option A -- "Productize Platform + Embed Data + Align AI/ML"

**Summary:** Keep the 5 feature teams intact. Transform Platform from a service desk into a true internal platform product team with published APIs and SLAs. Split Data into a lean "Data Platform" team (infrastructure/standards) and embed product data engineers into feature teams. Assign AI/ML to one primary product area (Feature Team 5 or a new combined team) with a dedicated PM.

**Where on the spectrums:** More decentralized; more divisional/value-stream

**Pros (what improves):**
- Feature teams gain self-service platform capabilities -- blocking drops significantly
- Data ownership becomes clear: Data Platform owns infrastructure; feature teams own product data features
- AI/ML gets a PM and a clear charter -- scattered consulting ends
- Minimal disruption to existing feature team structure

**Cons (what worsens):**
- Platform team must shift from reactive service to proactive product thinking (culture change)
- Embedding data engineers into feature teams reduces data team size and may create knowledge silos
- AI/ML aligned to one product area may slow AI adoption in other areas (mitigated by guild/office hours)

**Key dependencies removed (vs moved):**
- REMOVED: Feature teams waiting on Platform for API extensions (self-service via published platform products)
- REMOVED: Feature teams waiting on Data for product data pipelines (embedded data engineers)
- REMOVED: AI/ML scattered requests (single PM + single charter)
- MOVED (manageable): Data Platform still serves feature teams for infrastructure -- but via published interfaces, not ad hoc requests

**Risks/assumptions:**
- Assumes Platform team has the talent to shift from reactive to productized mode
- Assumes data engineers are willing to be embedded into feature teams
- Assumes there is a PM available (internal transfer) for AI/ML without adding headcount

**Teams + charters (proposed):**

| Team | Charter | Interfaces | Dependencies | Leadership roles |
|---|---|---|---|---|
| Feature Team 1 | Dashboards/reporting (incl. product data features) | Platform Products (APIs), Design System | Platform Products (self-service) | PM, Eng Lead, embedded Data Eng |
| Feature Team 2 | User management/permissions | Platform Products (APIs), Design System | Platform Products (self-service) | PM, Eng Lead |
| Feature Team 3 | Integrations/connectors (incl. ingestion data) | Platform Products (APIs), Design System | Platform Products (self-service) | PM, Eng Lead, embedded Data Eng |
| Feature Team 4 | Alerting/notifications | Platform Products (APIs), Design System | Platform Products (self-service) | PM, Eng Lead |
| Feature Team 5 + AI/ML | Exploration/ad-hoc analysis + AI-powered features | Platform Products, Data Platform, Design System | Platform Products, Data Platform | PM (new to AI/ML scope), Eng Lead, ML Lead |
| Platform Products | Internal platform: APIs, infra, deployment, self-service tooling | All feature teams (via published APIs/SLAs) | None (they are the foundation) | PM (internal transfer), Platform Eng Lead |
| Data Platform | Data infrastructure, warehouse, quality standards, shared schemas | All teams (via published data contracts) | Platform Products (infrastructure) | Data Lead (existing) |
| Design | Design system, UX standards, embedded designers in feature teams | All feature teams | None | Design Lead |

**Decision rights changes (top 5):**
1. Platform prioritization: shifts from ad hoc petitioning to PM-owned roadmap with published intake + SLAs
2. AI/ML project selection: PM for the combined team decides, aligned to product goals (not ad hoc requests)
3. Product data feature ownership: feature teams with embedded data engineers own this, not the Data team
4. Data infrastructure prioritization: Data Platform PM/Lead owns, with quarterly planning input from feature teams
5. Cross-team architecture decisions: Platform Eng Lead + guild review (not implicit Platform gatekeeper)

### Option B -- "Value-Stream Pods with Shared Platform SLAs"

**Summary:** Consolidate the 5 feature teams into 3 larger value-stream pods (each with PM, Eng, Design, Data, and where needed, ML). Reduce Platform to a lean infrastructure team with strict SLAs. Dissolve the standalone Data and AI/ML teams entirely by distributing their people into the pods.

**Where on the spectrums:** Strongly decentralized; strongly divisional/value-stream

**Pros (what improves):**
- Maximum autonomy: each pod has everything it needs to ship independently
- Dependencies between pods are minimal -- each pod has embedded data + (where needed) ML capabilities
- Decision speed increases dramatically within each pod

**Cons (what worsens):**
- Significant disruption: dissolving Data and AI/ML teams and reshuffling into 3 pods is a large change
- Risk of knowledge silos: data and ML expertise fragments across pods
- Platform team (now very lean) may not have capacity for cross-cutting infrastructure improvements
- 8-week launch risk is HIGH -- this is too much change to execute safely before the launch
- Career path concerns for data and ML specialists embedded in product pods
- 3 larger pods reduce the granularity of ownership (feature areas are merged)

**Key dependencies removed (vs moved):**
- REMOVED: All Data and AI/ML cross-team dependencies (everyone is in a pod)
- REMOVED: Most Platform dependencies (pods own more of their stack)
- MOVED (risky): Infrastructure work now duplicated across pods or starved in a too-lean platform team
- CREATED: Pod-to-pod coordination for cross-cutting features (e.g., a feature that spans dashboards + integrations)

**Risks/assumptions:**
- Assumes enough data and ML talent to distribute across 3 pods (4 ML people across 3 pods is thin)
- Assumes teams can absorb the disruption without launch impact (HIGH RISK given 8-week launch)
- Assumes pod leads can manage multi-disciplinary teams effectively

**Teams + charters (proposed):**

| Team | Charter | Interfaces | Dependencies | Leadership roles |
|---|---|---|---|---|
| Pod A: Core Analytics | Dashboards, reporting, exploration, AI-powered features | Platform Infra (SLAs), other pods (APIs) | Platform Infra | Pod PM, Eng Lead, Design, Data Eng, ML Eng |
| Pod B: Connectivity | Integrations, connectors, data ingestion, alerting | Platform Infra (SLAs), other pods (APIs) | Platform Infra | Pod PM, Eng Lead, Design, Data Eng |
| Pod C: Platform & Access | User management, permissions, admin, core platform features | Other pods (APIs) | None (owns its own infra) | Pod PM, Eng Lead, Design |
| Platform Infra | Lean infrastructure: deployment, monitoring, core shared services | All pods (via SLAs) | None | Platform Lead |

**Decision rights changes (top 5):**
1. Feature prioritization: fully within each pod, no cross-pod approval needed
2. Data pipeline ownership: pod-owned (no central data team arbitration)
3. ML prioritization: Pod A owns ML roadmap (ML engineers embedded there)
4. Platform prioritization: SLA-driven, not request-driven; pod leads negotiate quarterly
5. Cross-pod features: escalated to leadership for sequencing (new coordination mechanism needed)

### Option C -- "Targeted Fixes: Platform Productization + AI/ML PM + Data Charter Clarification" (Minimum Viable Reorg)

**Summary:** Make the smallest structural changes that address the top 3 friction loops. (1) Add a PM to Platform and publish intake/SLAs. (2) Assign a PM to AI/ML and align AI/ML to Feature Team 5. (3) Publish a clear Data team charter that defines what Data owns (infrastructure/warehouse) vs. what feature teams own (product data features). No team dissolution or embedding. This is a "tighten the interfaces" approach rather than a restructure.

**Where on the spectrums:** Balanced (current structure stays); slightly more decentralized via published interfaces

**Pros (what improves):**
- Lowest disruption -- protects the 8-week launch with near-zero risk
- Platform bottleneck addressed via PM-driven prioritization and published SLAs (not restructuring)
- AI/ML gets a PM and clear alignment to one product area
- Data charter clarification resolves ownership ambiguity without moving people

**Cons (what worsens):**
- Feature teams still depend on Platform (dependency is managed, not removed)
- Data engineers are not embedded -- feature teams still request from Data for product data features
- Does not fundamentally change team topology; parallelism gains are moderate, not transformational
- May feel like "half measures" and require a follow-on reorg in 2-3 quarters

**Key dependencies removed (vs moved):**
- MANAGED (not removed): Platform bottleneck -- PM + SLAs reduce chaos but Platform is still a central dependency
- REMOVED: AI/ML scattered requests (PM + single alignment)
- MANAGED (not removed): Data ownership -- charter clarification reduces confusion but feature teams still depend on Data for infrastructure

**Risks/assumptions:**
- Assumes that Platform PM + SLAs are sufficient to reduce blocking without embedding/distributing
- Assumes Data team accepts a narrower charter (infrastructure only) without resistance
- Assumes the moderate parallelism gains are sufficient to meet the "increase parallelism" goal

**Teams + charters (proposed):**

| Team | Charter | Interfaces | Dependencies | Leadership roles |
|---|---|---|---|---|
| Feature Teams 1-4 | (unchanged) | Platform (via SLAs), Data (via charter), Design | Platform, Data | (unchanged) |
| Feature Team 5 + AI/ML alignment | Exploration + AI features (AI/ML embedded via dotted line) | Platform (via SLAs), Data Platform, Design | Platform, Data | PM (covers AI/ML scope), Eng Lead, ML Lead |
| Platform | Core infra + APIs -- now with PM, published intake, SLAs | All feature teams | None | PM (internal transfer), Platform Eng Lead |
| Data | Data infrastructure, warehouse, quality (NOT product data features) | All teams (via published data contracts) | Platform | Data Lead |
| Design | (unchanged) | All teams | None | Design Lead |

**Decision rights changes (top 5):**
1. Platform prioritization: PM-owned with published intake/SLAs (was ad hoc)
2. AI/ML project selection: Feature Team 5 PM decides (was nobody)
3. Product data feature ownership: explicitly assigned to feature teams (was ambiguous)
4. Data infrastructure requests: via published data contracts (was ad hoc)
5. Architecture standards: Platform Lead + quarterly guild review (was implicit)

---

## 5) Recommendation + Scorecard

**Recommended option:** Option A -- "Productize Platform + Embed Data + Align AI/ML"

**Fallback option:** Option C -- "Targeted Fixes" (if embedding data engineers or assigning a PM proves infeasible in the short term)

### Rubric score summary

| Dimension | Option A | Option B | Option C |
|---|---|---|---|
| 1) Optimization clarity + success metrics | 2 | 2 | 2 |
| 2) Current-state diagnosis (dependencies + decisions) | 2 | 2 | 2 |
| 3) Operating model fit | 2 | 2 | 1 |
| 4) Option quality (tradeoffs) | 2 | 2 | 1 |
| 5) Decision rights + operating mechanisms | 2 | 2 | 1 |
| 6) Leadership/craft leverage | 2 | 1 | 1 |
| 7) Feasibility + transition safety | 2 | 0 | 2 |
| **Total** | **14** | **11** | **10** |

### Decision narrative (why this, why now, why not the others)

**Why Option A:** It directly addresses all three structural problems (platform bottleneck, AI/ML chaos, data ownership ambiguity) with changes that are significant enough to produce real parallelism gains but modular enough to phase around the 8-week launch. Platform productization is the highest-leverage single change -- it converts a bottleneck into a self-service platform. Embedding data engineers gives feature teams the ownership they need to ship data features independently. Aligning AI/ML to Feature Team 5 with a PM ends the scattered consulting model and delivers focused impact.

**Why now:** The 8-week launch creates urgency. Day 1 changes (PM assignments, charter publication) can happen in Week 1 without disrupting the launch. Embedding data engineers and platform productization can phase in starting Week 3-4 (after launch-critical work is stabilized). Waiting another quarter means the same blocking patterns will slow the launch and compound.

**Why not Option B:** Too much disruption for the 8-week launch window. Dissolving teams and creating pods is a high-risk change that would take 4-6 weeks of transition during a critical launch period. It also fragments the 4-person AI/ML team across 3 pods, which is too thin. Option B is a valid long-term evolution if Option A succeeds and the org wants to go further.

**Why not Option C:** It manages dependencies without removing them. The parallelism gains are moderate, and the organization will likely need a follow-on reorg in 2-3 quarters. However, it is the right fallback if Option A's people moves (embedding data engineers, PM transfers) prove infeasible.

### Day 1 changes (minimum viable reorg)

1. **Assign a PM to Platform team** (internal transfer from a feature team with lower near-term launch pressure, or a senior PM takes dual scope temporarily). Platform PM publishes an intake process and preliminary SLAs within Week 1.
2. **Assign a PM to AI/ML and align AI/ML with Feature Team 5.** The Feature Team 5 PM expands scope to cover AI/ML, or a PM from another team with AI product interest transfers. AI/ML team stops taking ad hoc requests from other teams immediately.
3. **Publish the Data team charter clarification.** Data team lead and VP jointly communicate: "Data team owns data infrastructure, warehouse, and quality. Product data features are owned by feature teams." This is a communication + charter change, not a people move.
4. **Freeze non-launch-critical platform requests.** For the 8-week launch period, Platform team prioritizes only launch-critical work. Non-critical requests queue for post-launch.
5. **Announce the plan** to all managers with the phased timeline. No people moves in Week 1 except PM assignments.

### Follow-on changes (next 30-90 days)

- **Week 3-4 (post-launch stabilization):** Begin embedding 2-3 data engineers from the Data team into Feature Teams 1, 3, and 5 (the teams with the most product data feature work). Data Platform retains the remaining data engineers for infrastructure.
- **Week 4-6:** Platform team publishes first set of self-service APIs/tooling and deprecates the ad hoc request process for covered capabilities.
- **Week 6-8:** Feature Team 5 + AI/ML formally merge into a single team with combined standup and planning.
- **Week 8-12:** Platform team completes first iteration of self-service tooling; measure blocking-time reduction. Evaluate whether additional data engineers should be embedded or if the split is sufficient.

---

## 6) Operating Mechanisms

**Decision rights (new):**

| Decision | Owner | Consulted | Informed | Escalation trigger |
|---|---|---|---|---|
| Feature team roadmap | Feature team PM | Eng Lead, Design, Data Eng (if embedded) | VP Product | Cross-team scope conflict |
| Platform roadmap + prioritization | Platform PM | Feature team PMs (quarterly planning) | VP Engineering | >2 feature teams blocked for >1 week |
| AI/ML project selection | Feature Team 5 PM | ML Lead, Data Platform Lead | VP Product | Other teams requesting >20% of AI/ML capacity |
| Data infrastructure prioritization | Data Platform Lead | Feature team PMs (quarterly) | VP Engineering | Schema changes affecting >2 teams |
| Product data feature ownership | Feature team PM (owning team) | Data Platform Lead (for infrastructure needs) | Data Platform Lead | Unclear ownership (escalate to VP Product) |
| Architecture standards | Platform Eng Lead + Architecture Guild | Eng Leads from all teams | All engineers | Deviation from standards (guild review) |
| Headcount allocation | VP Product + VP Engineering | Feature team PMs, Leads | All managers | Budget constraint conflicts |

**What is centralized:**
- Infrastructure security, deployment pipeline, API contract standards (Platform team)
- Data schema standards and data quality bar (Data Platform)
- Design system components and accessibility standards (Design team)
- Architecture review for cross-cutting changes (Architecture Guild)

**What is decentralized:**
- Feature prioritization and roadmap within team charter
- Product data feature design and implementation (feature teams)
- AI/ML model selection and experimentation (Feature Team 5 + AI/ML)
- UX design details within design system constraints

**Escalation triggers:**
- Any team blocked on another team for >3 business days -> escalate to both team leads
- Any team blocked for >1 week -> escalate to VP level
- Any architectural decision affecting >2 teams -> Architecture Guild review
- Any charter overlap or ownership dispute -> VP Product arbitrates within 48 hours

**Planning cadence:**

| Cadence | Purpose | Participants | Outputs |
|---|---|---|---|
| Weekly | Team-level sprint planning | Individual teams | Sprint commitments |
| Bi-weekly | Cross-team sync (30 min) | All PMs + Platform PM + Data Lead | Dependency updates, blocking issues, upcoming interface needs |
| Monthly | Platform roadmap review | Platform PM, all feature PMs, VP Eng | Platform priorities for next month, SLA updates |
| Quarterly | Org-wide planning | VPs, all PMs, all Eng Leads | Quarterly goals, headcount allocation, charter reviews |

**Interface contracts:**

- **Platform <-> Feature Teams:** Published API catalog with versioning, SLAs (response time for new capability requests: triaged within 3 business days; critical launch items within 1 business day). Self-service tooling for common operations (deployment, environment provisioning, monitoring setup).
- **Data Platform <-> Feature Teams:** Published data contracts (schema, quality SLAs, access patterns). Feature teams own product data features built on top of Data Platform infrastructure. Data Platform provides infrastructure, not business logic.
- **Design <-> Feature Teams:** Design system with documented components. Designers embedded in feature teams follow system but have autonomy within it. Monthly design review for cross-team consistency.
- **AI/ML <-> Other Teams (post-alignment):** AI/ML office hours (2 hours/week) for other teams to consult. Any work request >2 days goes through Feature Team 5 PM prioritization. Other teams can use published ML models/APIs self-service.

---

## 7) Transition Plan

**Guiding approach:** Phased rollout with launch protection. The 8-week customer launch is the hard constraint. Phase 1 (Day 1 changes) is purely PM assignments + charter communication -- zero disruption to in-flight work. Phase 2 (post-launch) executes the structural changes (data embedding, platform productization, team merge). This ensures the launch ships on time while setting up the structural improvements to land cleanly after.

### A) Sequencing (phases)

| Phase | Dates | What changes | Owners | Success checks |
|---|---|---|---|---|
| **Phase 0: Announce + align** | Week 1 (Day 1-5) | Communicate plan to all managers. Assign PM to Platform (internal transfer). Assign PM scope for AI/ML to Feature Team 5 PM. Publish Data charter clarification. Freeze non-launch Platform requests. | VP Product, VP Engineering | All managers briefed. PMs assigned. AI/ML stops ad hoc requests. |
| **Phase 1: Launch protection** | Week 2-8 | No structural changes. Platform PM establishes intake process and preliminary SLAs. AI/ML works exclusively on Feature Team 5 priorities. Data charter in effect (feature teams own product data features in principle; Data team continues current support for launch-critical items). | Platform PM, Feature Team 5 PM, Data Lead | Launch ships on time. Platform PM has published intake process. AI/ML delivers on Feature Team 5 goals. |
| **Phase 2: Embed + productize** | Week 9-12 | Embed 2-3 data engineers into Feature Teams 1, 3, 5. Platform publishes first self-service APIs. Feature Team 5 + AI/ML formally merge. | VP Engineering, Data Lead, Platform PM | Data engineers settled in new teams. Platform self-service live. AI/ML team fully integrated with FT5. |
| **Phase 3: Measure + adjust** | Week 13-16 | Measure blocking-time reduction. Evaluate embedding success. Adjust charter boundaries as needed. Quarterly planning with new structure. | VP Product, VP Engineering | Blocking time reduced by 40%. Team satisfaction survey. Quarterly plan reflects new structure. |

### B) Comms plan

**Audience groups and messaging:**

| Audience | Message focus | Format | Timing |
|---|---|---|---|
| **Executive team** | Strategic rationale, expected outcomes, timeline, what they need to reinforce | 1:1 briefings with VP Product/VP Eng | Week 1, Day 1 (before all-hands) |
| **Managers (PMs, Eng Leads, Design Lead, Data Lead)** | Detailed plan: what changes, what stays, new decision rights, their role in the transition | Manager workshop (90 min) | Week 1, Day 1-2 |
| **All ICs (Product, Eng, Design, Data)** | Why we're making changes, what changes for them, what stays the same, timeline, how to raise concerns | All-hands or team-level meetings | Week 1, Day 3-4 |
| **AI/ML team (4 people)** | Direct conversation: you're joining Feature Team 5, you get a PM, here's the charter, here's why this is better for you | 1:1s with VP Eng + Feature Team 5 PM | Week 1, Day 1-2 (before all-hands) |
| **Data team** | Direct conversation: charter clarification, some of you will embed in feature teams (Phase 2), here's the timeline and what it means for your career | Team meeting with VP Eng + Data Lead | Week 1, Day 2 (before all-hands) |

**Narrative outline (for all-hands):**
1. **Why now:** We have three structural bottlenecks that are slowing us down and threatening the customer launch. This is not about performance -- it is about structure.
2. **What changes:** Platform gets a PM and becomes a product team. AI/ML joins Feature Team 5 with a PM. Data team charter is clarified. After the launch, we embed data engineers into feature teams.
3. **What stays:** Feature teams 1-5 stay intact. Your day-to-day work does not change during the launch period. Reporting lines stay the same in Phase 1.
4. **How decisions work now:** Platform has a PM and an intake process. AI/ML requests go through Feature Team 5 PM. Data infrastructure requests go through Data Platform.
5. **Timeline:** Weeks 1-8 are about protecting the launch. Structural changes begin Week 9.

**FAQ topics:**
- "Does my team change?" (Phase 1: no. Phase 2: some data engineers move.)
- "Who is my manager?" (No manager changes in Phase 1. Phase 2 manager changes communicated in Week 7.)
- "How do I get Platform/Data help now?" (Published intake process, SLAs, no more ad hoc petitioning.)
- "What happens to the AI/ML team?" (Joins Feature Team 5 with a PM. Better for impact and career growth.)
- "Will there be more reorgs?" (We are committing to this structure for at least 2 quarters. Day 30/60/90 check-ins to adjust.)

### C) Risk mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Launch disruption** | Low (if Phase 1 is executed as planned) | Critical | Phase 1 makes zero structural changes. Freeze non-launch Platform requests. AI/ML stops ad hoc work but continues any launch-critical AI features already in flight. |
| **Data engineer resistance to embedding** | Medium | Medium | Communicate career path: embedded data engineers gain product context and broader scope. Maintain Data Guild for knowledge sharing and career community. Data Lead retains dotted-line mentorship. |
| **No PM available for Platform** | Medium | High | Fallback: senior PM takes dual scope temporarily (50% Platform, 50% feature team) for 4-6 weeks while recruiting or internally transferring. If no PM in 4 weeks, escalate to VP Product. |
| **Platform team struggles to productize** | Medium | Medium | Start small: productize the top 3 most-requested capabilities first. Platform PM + VP Eng co-own the transition. If Platform cannot productize within 8 weeks, re-evaluate team composition. |
| **AI/ML team morale (loss of independence)** | Low-Medium | Medium | Frame as: you get a PM, clear goals, and the ability to ship real product features instead of scattered favors. ML Lead retains technical authority. Office hours maintain visibility with other teams. |
| **Feature teams build duplicate data capabilities** | Low | Medium | Data Platform publishes a clear "what we provide" catalog. Architecture Guild reviews any new data infrastructure. Quarterly charter review catches overlap. |

**Rollback triggers:**
- If the customer launch is at risk due to org changes (any signal): immediately revert to pre-change decision processes for launch-critical work
- If 2+ data engineers request to return to Data team within 30 days of embedding: pause embedding, diagnose, and adjust
- If Platform blocking time does not decrease within 60 days of PM assignment: escalate to VP Eng for deeper diagnosis (may need talent change, not just process change)

### D) Measurement and checkpoints

**Day 30 check (Week 4-5):**
- Platform PM is operational: intake process published, SLAs communicated, first prioritization cycle completed
- AI/ML team is working exclusively on Feature Team 5 priorities (no ad hoc requests from other teams)
- Data charter clarification is understood by all teams (survey or spot-check)
- Customer launch is on track (no launch impact from org changes)
- Metric: baseline "blocked on another team" time measured across all feature teams

**Day 60 check (Week 8-9):**
- Customer launch has shipped successfully
- Phase 2 is beginning: data engineer embedding starts, Platform self-service development in progress
- AI/ML + Feature Team 5 merger is formalized
- Metric: compare "blocked on another team" time to baseline -- target 20% reduction already visible
- Qualitative: manager pulse survey on clarity of decision rights and ownership

**Day 90 check (Week 12-13):**
- Data engineers are embedded and productive in feature teams
- Platform self-service APIs are live for top 3 capabilities
- AI/ML has shipped at least 1 product capability through Feature Team 5
- Metric: "blocked on another team" time reduced by 40% from baseline
- Metric: feature team cycle time (lead time from start to ship) improved
- Qualitative: all-hands retro on org changes -- what's working, what needs adjustment
- Decision: commit to structure for next quarter or identify adjustments

---

## 8) Risks / Open questions / Next steps

### Risks (top 5)

1. **PM availability is the critical bottleneck.** Option A requires 2 PM assignments (Platform + AI/ML scope expansion). If no PM is available internally, the entire plan is delayed. Mitigation: identify candidates in Week 1; fallback is dual-scope PM.

2. **Platform productization is a multi-quarter journey, not a quick fix.** Assigning a PM helps with prioritization, but true self-service platform capabilities take 2-3 quarters to build. Feature teams may remain partially blocked on Platform during the transition. Mitigation: start with the top 3 most-requested capabilities; accept partial improvement in Q1.

3. **Data engineer embedding creates knowledge silos.** Data engineers embedded in feature teams may lose connection to the broader data community and develop inconsistent practices. Mitigation: Data Guild (bi-weekly), Data Platform retains standards ownership, Data Lead maintains dotted-line mentorship.

4. **AI/ML team of 4 is too small for the expected scope.** Even aligned to one product area, 4 ML engineers may not be sufficient to deliver meaningful AI-powered features while maintaining existing models. This may become a headcount request in 2 quarters. Mitigation: focus ruthlessly on 1-2 high-impact capabilities; defer breadth.

5. **Design resourcing remains unaddressed.** This plan does not restructure Design. If Design capacity is already a bottleneck across 5 feature teams, the increased parallelism from other changes may expose Design as the new constraint. Mitigation: monitor Design blocking in Day 30/60 checks; address in next quarter if needed.

### Open questions

- **Who are the specific PM candidates for Platform and AI/ML scope?** This must be identified in Week 1. VP Product should have names before the manager workshop.
- **Which data engineers are best suited for embedding, and into which teams?** Data Lead and Eng Leads should assess skills and preferences before Phase 2.
- **How coupled is the product architecture between feature areas?** The current-state map assumes reasonable decoupling. If the codebase is a monolith with shared modules, platform productization and team autonomy will be harder than assumed.
- **What is the current Design team structure and capacity model?** Not addressed in this pack. If Design is already a constraint, it may need its own redesign.
- **What is the reporting structure for embedded data engineers?** Options: (a) report to feature team Eng Lead (full integration), (b) report to Data Lead with dotted line to feature team (functional reporting). Recommend (a) for ownership clarity with (b) as a transition step.
- **What does the AI/ML team's current project portfolio look like?** Need to understand what in-flight work exists and whether any of it is launch-critical before shutting down ad hoc requests.

### Next steps (next 1-2 weeks)

1. **VP Product + VP Engineering align on Option A** (or fallback to Option C). Identify PM candidates for Platform and AI/ML scope expansion. Target: end of Day 2.
2. **Brief all managers** (PM + Eng Leads + Data Lead + Design Lead) on the plan, timeline, and their role. Collect concerns and adjust. Target: Day 2-3.
3. **Communicate to all ICs** via all-hands or team meetings. Publish the Data charter clarification. Announce Platform PM and AI/ML alignment. Target: Day 3-5.
4. **Platform PM starts:** publish intake process and preliminary SLAs. Triage the current backlog. Freeze non-launch requests. Target: end of Week 1.
5. **AI/ML team transitions:** Feature Team 5 PM takes on AI/ML scope. AI/ML team stops accepting ad hoc requests. Any launch-critical AI work in flight is explicitly identified and protected. Target: end of Week 1.
6. **Baseline measurement:** capture current "blocked on another team" time across all feature teams for Day 30/60/90 comparison. Target: end of Week 2.

---

## Quality Gate: Checklist + Rubric Self-Assessment

### A) Pack quality checklist

- [x] Optimization target is explicit (shipping parallelism, cross-team blocking reduction) with 3 success metrics
- [x] Constraints/non-negotiables are listed (no headcount for 2Q, 8-week launch)
- [x] Current-State Map captures real dependency/decision bottlenecks (platform bottleneck, AI/ML chaos, data ambiguity)
- [x] Operating Model Decision is explicit (more decentralized, more value-stream) with guardrails
- [x] 3 org options presented with clear pros/cons and assumptions
- [x] Recommendation includes Day 1 changes vs follow-on changes
- [x] Decision rights are clear enough that a manager can answer "who decides?" without ambiguity
- [x] Management layers and leadership roles are explicit
- [x] Transition plan includes comms, sequencing, and safety rails (continuity + rollback triggers)
- [x] Risks / Open questions / Next steps are included

### B) Dependency & parallelism checklist

- [x] Top dependency hotspots are listed and addressed (platform productization, data embedding, AI/ML alignment)
- [x] Interfaces between teams are explicit (API catalog, data contracts, SLAs)
- [x] Shared services/platform teams have clear service boundaries and prioritization mechanisms
- [x] The reorg does not merely "move dependencies" -- each option explicitly states what is removed vs moved

### C) UX coherence checklist

- [x] Design system provides cross-team UX consistency
- [x] Standards documented and enforcement clear (Design Lead + monthly design review)
- [x] Decentralized teams align on shared UX principles

### D) Decision rights checklist

- [x] Decisions have explicit owners and escalation triggers
- [x] "Consulted vs informed" is clear (RACI-style table provided)
- [x] Decision logging recommended (quarterly charter reviews)

### E) Transition & people-risk checklist

- [x] In-flight projects have stable ownership during transition (Phase 1 = no structural changes)
- [x] Managers have a clear message for their team (comms plan with audience-specific messaging)
- [x] Plan avoids serial reorgs; check-ins scheduled (Day 30/60/90)

### Rubric self-score (Option A / recommended)

| Dimension | Score | Rationale |
|---|---|---|
| 1) Optimization clarity + success metrics | 2 | Explicit optimization targets, 3 testable metrics, clear constraints |
| 2) Current-state diagnosis | 2 | Dependency hotspots, decision rights, management layers all mapped with concrete bottleneck examples |
| 3) Operating model fit | 2 | Posture is explicit with rationale tied to product architecture and execution needs; guardrails defined |
| 4) Option quality | 2 | 3 viable options with pros/cons, dependency analysis (removed vs moved), and clear tradeoffs |
| 5) Decision rights + operating mechanisms | 2 | Full RACI-style table, escalation triggers, planning cadence, interface contracts |
| 6) Leadership/craft leverage | 2 | PM assignments address the "no PM" gap; craft leverage maintained via ML Lead, Data Lead roles; layers addressed |
| 7) Feasibility + transition safety | 2 | Phased plan protects 8-week launch; comms plan; rollback triggers; Day 30/60/90 checkpoints |
| **Total** | **14/14** | Ship as-is |
