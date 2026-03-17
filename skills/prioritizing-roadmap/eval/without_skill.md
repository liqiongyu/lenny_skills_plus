# Q2 Roadmap Prioritization Plan

## Product Context

- **Product**: Team collaboration SaaS
- **ICP**: 10–200 person tech companies, team leads
- **North Star Metric**: Weekly active teams completing >= 1 project
- **Decision**: Select Q2 roadmap themes and top 8 initiatives within 2 weeks
- **Team Capacity**: 6 engineers, 1 designer
- **Hard Constraints**: Must complete SSO launch; platform migration dependency in May
- **Candidate Pool**: 15 initiatives to evaluate

---

## Step 1: Establish Prioritization Criteria

To rank the 15 candidate initiatives, use a weighted scoring framework aligned with the North Star metric (weekly active teams completing >= 1 project). The following criteria should be used:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| North Star Impact | 30% | How directly does this initiative drive more teams to complete projects weekly? |
| Strategic Alignment | 20% | Does it serve the ICP (tech team leads at 10–200 person companies)? Does it support retention, expansion, or acquisition? |
| Effort & Feasibility | 20% | Can the team (6 eng, 1 designer) realistically deliver this in Q2 given constraints? |
| Risk & Dependencies | 15% | Does it have external dependencies (e.g., platform migration)? Technical or adoption risk? |
| Revenue / Retention Signal | 15% | Is this blocking deals, causing churn, or requested by high-value accounts? |

### Scoring Scale

- **5** — Transformative / trivial effort / no risk
- **4** — Strong positive impact
- **3** — Moderate impact
- **2** — Minor impact
- **1** — Negligible or negative

---

## Step 2: Map Hard Constraints

Before scoring, lock in non-negotiable commitments:

### Locked Initiatives
1. **SSO Launch** — Must ship. This is a hard constraint. Allocate engineering time first.
2. **Platform Migration Prep** — Dependency lands in May. Any initiative that requires the new platform cannot start before migration is complete. Plan accordingly.

### Capacity Budget (Rough Allocation)

Assuming Q2 = 13 weeks, 6 engineers, 1 designer:

- **Total engineering weeks**: ~78 eng-weeks
- **SSO Launch (estimated)**: ~12–16 eng-weeks (2–3 engineers for 4–6 weeks)
- **Platform migration buffer**: ~8–10 eng-weeks (stabilization, integration work post-May)
- **Remaining for new initiatives**: ~52–58 eng-weeks
- **Design capacity**: ~13 designer-weeks (minus ~3 weeks for SSO = ~10 weeks available)

This means the top 8 initiatives must fit within roughly 52–58 eng-weeks and 10 designer-weeks after accounting for SSO and migration work.

---

## Step 3: Score All 15 Candidates

Create a scoring spreadsheet with each initiative as a row and the five criteria as columns. For each initiative:

1. Have the PM (or a small group of PM + eng lead + designer) independently score each criterion 1–5.
2. Calculate weighted score: `(North Star Impact x 0.30) + (Strategic Alignment x 0.20) + (Effort & Feasibility x 0.20) + (Risk & Dependencies x 0.15) + (Revenue/Retention Signal x 0.15)`
3. Rank by weighted score.

### Example Scoring Template

| # | Initiative | North Star (30%) | Strategic (20%) | Feasibility (20%) | Risk (15%) | Revenue (15%) | Weighted Score | Eng-Weeks Est. |
|---|-----------|-----------------|----------------|-------------------|------------|---------------|---------------|-----------------|
| 1 | SSO Launch | 3 | 5 | 4 | 3 | 5 | **LOCKED** | 14 |
| 2 | [Initiative B] | ? | ? | ? | ? | ? | ? | ? |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 15 | [Initiative O] | ? | ? | ? | ? | ? | ? | ? |

---

## Step 4: Apply the North Star Lens

After initial scoring, stress-test the top candidates with these questions:

1. **Activation**: Does this help new teams complete their first project faster?
2. **Frequency**: Does this bring existing teams back to complete projects more often?
3. **Team Size**: Does this help teams grow (more members = stickier)?
4. **Completion Rate**: Does this remove friction in the project completion flow?

Any initiative that scores high overall but has weak North Star linkage should be deprioritized unless it is a strategic necessity (like SSO).

---

## Step 5: Identify Q2 Themes

Group the top-scoring initiatives into 2–3 coherent themes. Themes help communicate the roadmap internally and externally. Examples based on typical collaboration SaaS priorities:

### Suggested Theme Framework

- **Theme 1: Enterprise Readiness** — SSO launch, admin controls, audit logs, permissions. Rationale: Unlocks 50–200 person companies in the ICP.
- **Theme 2: Project Completion Velocity** — Initiatives that directly improve the rate at which teams finish projects (workflow improvements, templates, notifications, integrations). Rationale: Directly drives the North Star metric.
- **Theme 3: Team Activation & Growth** — Onboarding improvements, invite flows, team setup experience. Rationale: More active teams = more teams completing projects.

Assign each of the top 8 initiatives to a theme. If an initiative does not fit any theme, reconsider its inclusion.

---

## Step 6: Stack Rank and Sequence the Top 8

After scoring and theming, select the top 8 by:

1. **Sort by weighted score** (descending).
2. **Check cumulative capacity**: Add eng-week and designer-week estimates top-down. Stop when you hit the budget ceiling (~52–58 eng-weeks, ~10 designer-weeks, excluding SSO and migration).
3. **Check dependencies**: Anything that depends on May platform migration must be sequenced for late Q2 (June). Anything that depends on SSO must wait for SSO to ship.
4. **Resolve ties**: If two initiatives have similar scores, prefer the one with lower risk, shorter cycle time, or stronger revenue signal.

### Sequencing Framework

| Month | Focus | Rationale |
|-------|-------|-----------|
| **April** | SSO launch (finish), 2–3 low-dependency initiatives | Ship SSO early. Start quick wins that don't require platform migration. |
| **May** | Platform migration lands. Continue in-progress work. Start migration-dependent items. | Absorb migration risk. Begin integration work. |
| **June** | Ship remaining initiatives. Polish and iterate on April launches based on data. | Close out Q2 commitments. Measure North Star impact. |

---

## Step 7: Validate with Stakeholders

Before finalizing, run the proposed roadmap through three validation checks:

### 7a. Engineering Feasibility Review
- Present the top 8 + SSO + migration to the engineering team.
- Ask: "Can we commit to delivering these 10 items in Q2 with 6 engineers?"
- Adjust scope or sequence based on technical feedback.

### 7b. Customer & Sales Signal Check
- Cross-reference the top 8 against: top customer requests, churn reasons, deal-blocking features.
- If a high-revenue-signal initiative was scored out of the top 8, reconsider.

### 7c. Leadership Alignment
- Present themes + top 8 to leadership/founders.
- Frame as: "Here are the Q2 themes, the top 8 initiatives, and how they drive weekly active teams completing projects."

---

## Step 8: Define Success Metrics for Each Initiative

For each of the top 8 initiatives, define:

| Initiative | Leading Metric | Lagging Metric | Target |
|-----------|---------------|----------------|--------|
| SSO Launch | SSO setup completion rate | Enterprise plan conversions | 80% setup completion in first month |
| [Initiative 2] | [e.g., time to first project completion] | [North Star movement] | [specific number] |
| ... | ... | ... | ... |

---

## Step 9: Communicate the Roadmap

### Internal Communication
- Share a one-page roadmap summary: themes, top 8 initiatives, timeline, and what was explicitly deprioritized (and why).
- The "not doing" list is as important as the "doing" list — it prevents scope creep.

### External Communication
- For customers/prospects: share themes, not specific features, to maintain flexibility.
- For enterprise prospects waiting on SSO: provide a specific ship date commitment.

---

## Two-Week Decision Timeline

| Day | Activity | Participants | Output |
|-----|----------|-------------|--------|
| Day 1–2 | Gather data: customer requests, churn analysis, sales feedback, usage analytics | PM | Data packet for scoring |
| Day 3–4 | Independent scoring of 15 initiatives against 5 criteria | PM, Eng Lead, Designer | Individual scorecards |
| Day 5 | Calibration session: align scores, debate disagreements, finalize ranking | PM, Eng Lead, Designer | Consensus ranked list |
| Day 6–7 | Eng feasibility review: estimate eng-weeks, flag risks, check dependencies | Eng Lead + Engineers | Validated estimates |
| Day 8 | Stack rank top 8, assign to themes, draft sequence | PM | Draft roadmap |
| Day 9 | Stakeholder review: sales, CS, leadership | PM + Stakeholders | Feedback |
| Day 10 | Final adjustments, lock roadmap | PM, Eng Lead | Final Q2 roadmap |

---

## Risk Mitigation Plan

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| SSO launch delays, consuming more capacity | Medium | High | Timebox SSO. Define MVP scope. No feature creep. |
| Platform migration in May causes instability | Medium | High | Reserve 8–10 eng-weeks buffer. Avoid shipping major features same week as migration. |
| Designer bottleneck (1 designer for 8+ initiatives) | High | Medium | Prioritize design-heavy work early. Use existing patterns/components for lower-design items. Stagger design reviews. |
| Scope creep on individual initiatives | Medium | Medium | Define MVP for each initiative upfront. Use a "must have / nice to have / out of scope" framework. |
| Key engineer unavailability (PTO, illness) | Low | Medium | Avoid single-point-of-failure assignments. Pair on critical-path work. |

---

## What This Plan Does NOT Cover

- **Specific initiative names or descriptions**: You will need to apply this framework to your actual 15 candidates.
- **Detailed sprint planning**: This is a quarterly roadmap prioritization, not a sprint plan. Break initiatives into sprints after the roadmap is locked.
- **Technical architecture decisions**: Engineering will need to determine implementation approaches for each selected initiative.
- **Pricing or packaging changes**: If any initiative has pricing implications, that requires a separate workstream.

---

## Summary

1. Score all 15 initiatives against 5 weighted criteria anchored to the North Star metric.
2. Lock SSO and platform migration buffer as non-negotiable capacity commitments.
3. Select the top 8 initiatives that fit within remaining capacity (~52–58 eng-weeks, ~10 designer-weeks).
4. Group into 2–3 themes for coherence and communication.
5. Sequence by dependency (migration in May) and risk (SSO first).
6. Validate with engineering, customers/sales, and leadership.
7. Define success metrics per initiative.
8. Communicate clearly — including what you are NOT doing.
9. Complete the entire decision process in 10 working days.
