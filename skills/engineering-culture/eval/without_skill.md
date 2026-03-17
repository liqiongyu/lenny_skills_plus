# Engineering Culture Improvement Plan

## Context Summary

- **Company**: B2B analytics SaaS
- **Team**: 40 engineers across 5 teams
- **Architecture**: Rails monolith + 3 Go microservices
- **Current deploy cadence**: Twice/week via manual release trains
- **Incident rate**: ~2 P1 incidents/month
- **Key symptoms**: Slow PR reviews (3+ days), no on-call ownership, platform team bottleneck, poor mid-sprint communication
- **Goal**: Daily deploys + 50% P1 reduction within one quarter

---

## 1. Deployment Pipeline & Release Process

### Current Problem
Manual release trains twice a week create large batch sizes, increase risk per deploy, and slow feedback loops.

### Recommendations

**Move to continuous delivery with feature flags**
- Adopt a trunk-based development model. Engineers merge small PRs to `main` daily.
- Implement a feature flag system (e.g., LaunchDarkly, Flipper for Rails, or a lightweight internal solution). Every new feature ships behind a flag so that deploys are decoupled from releases.
- Replace the manual release train with an automated CI/CD pipeline that deploys to production on every green merge to `main`.

**Invest in deployment confidence**
- Require a passing CI suite (unit, integration, and a lightweight smoke test against staging) before any merge.
- Add automated canary or rolling deploys for the Rails monolith. Route 5% of traffic to the new version, monitor error rates and latency for 10 minutes, then promote or roll back automatically.
- For the Go microservices, implement blue-green or canary deploys via your container orchestrator (Kubernetes or similar).

**Reduce batch size**
- Set a soft guideline: PRs should be under 300 lines of diff. Anything larger needs a justification or should be broken into a stack.
- Encourage short-lived branches (< 1 day).

### Timeline
- **Weeks 1-2**: Set up feature flag infrastructure and automated CI gating.
- **Weeks 3-4**: Implement canary deploys on one service as a pilot.
- **Weeks 5-8**: Roll out automated deploys across all services. Sunset the manual release train.
- **Weeks 9-12**: Refine, monitor, and achieve daily (or more frequent) deploys.

---

## 2. PR Review Process & Code Velocity

### Current Problem
PRs sit in review for 3+ days. This kills velocity, increases merge conflicts, and demoralizes engineers.

### Recommendations

**Establish review SLAs**
- First meaningful review within 4 business hours. Final approval within 24 hours.
- Track these metrics and make them visible on a team dashboard (use a tool like LinearB, Sleuth, or a simple script against your Git provider's API).

**Assign clear reviewers**
- Use CODEOWNERS files to auto-assign reviewers based on file paths. This eliminates the "who should review this?" ambiguity.
- Each PR should have exactly one required reviewer (not two or three). Trust your engineers.

**Reduce review burden**
- Invest in automated linting, formatting (RuboCop for Rails, `gofmt`/`golangci-lint` for Go), and static analysis. Robots should catch style issues, not humans.
- Write clear PR descriptions with a template: What changed? Why? How to test? Any risks?
- Encourage authors to self-review before requesting review and to annotate non-obvious sections.

**Cultural shifts**
- Normalize small PRs. A PR that takes 15 minutes to review gets reviewed fast. A PR that takes 2 hours sits.
- Introduce "review blocks" -- 30-minute windows at 10am and 2pm where engineers prioritize clearing their review queue.
- Recognize and praise fast, high-quality reviewers publicly.

### Timeline
- **Week 1**: Implement CODEOWNERS, PR templates, and automated linting.
- **Week 2**: Announce review SLAs. Start tracking metrics.
- **Weeks 3-12**: Monitor, coach, and iterate. Publicly celebrate improvements.

---

## 3. On-Call & Incident Management

### Current Problem
Random on-call rotation means no ownership, no expertise building, and slow incident response. Two P1s/month is too many.

### Recommendations

**Structured on-call rotation by team**
- Each of the 5 teams owns the services and code they build. On-call rotates within the team on a weekly basis.
- Every team has a primary and secondary on-call. Primary responds; secondary is backup.
- Use PagerDuty or Opsgenie to manage rotations, escalation policies, and alerting.

**On-call onboarding & runbooks**
- Each team maintains runbooks for their services covering: common alerts, diagnostic steps, rollback procedures, escalation criteria.
- New on-call engineers shadow for one rotation before going primary.
- Provide a "first 5 minutes" checklist for every alert: check dashboards, check recent deploys, check dependent services.

**Incident response process**
- Define severity levels clearly (P1 = customer-facing outage or data integrity issue, P2 = degraded service, etc.).
- For P1s: Incident commander (rotating role) coordinates. Communication goes to a dedicated Slack channel. Status updates every 15 minutes.
- Mandatory blameless post-mortems for every P1 within 48 hours. Post-mortems must identify contributing causes and produce action items with owners and deadlines.

**Reduce P1 frequency**
- Analyze the last 6 months of P1s. Categorize them (deploy-related, infrastructure, data pipeline, third-party dependency, etc.). Attack the top category.
- Improve observability: structured logging, distributed tracing (e.g., Datadog, Honeycomb), and SLO-based alerting rather than threshold-based alerting.
- Require pre-deploy checklists for high-risk changes (database migrations, schema changes, infrastructure modifications).

### Timeline
- **Weeks 1-2**: Define severity levels, set up PagerDuty with team-based rotations, create escalation policies.
- **Weeks 3-4**: Teams draft initial runbooks. Conduct a P1 retrospective analysis.
- **Weeks 5-8**: Implement observability improvements targeting the top P1 category.
- **Weeks 9-12**: Refine alerting, complete runbook coverage, measure P1 trend.

---

## 4. Platform Team & Internal Developer Experience

### Current Problem
The platform team is a bottleneck for every feature team. This creates dependencies, waiting, and frustration.

### Recommendations

**Shift platform from gatekeeper to enabler**
- Platform team should build self-service tools, not do work on behalf of feature teams. The goal is to make feature teams autonomous.
- Identify the top 5 reasons feature teams file tickets to platform. Build self-service solutions for at least 3 of them within the quarter.

**Specific self-service targets (likely candidates)**
- **Infrastructure provisioning**: Provide Terraform modules or internal CLI tools so feature teams can spin up their own staging environments, add new queues, or create database read replicas without a platform ticket.
- **CI/CD pipeline configuration**: Let feature teams own their pipeline configs (e.g., `.github/workflows/` or equivalent) with platform-provided templates.
- **Observability setup**: Provide dashboards-as-code templates so teams can instrument and monitor their own services.

**Embed, don't centralize**
- Consider rotating a platform engineer into each feature team for 2-week stints to transfer knowledge and identify friction points.
- Establish "platform office hours" (2 hours/week) for ad-hoc questions instead of requiring tickets for everything.

**Define a platform product roadmap**
- Treat the platform as an internal product. The platform team's "customers" are the feature teams.
- Run a quarterly survey or retrospective asking feature teams: What slows you down? What do you need from platform?
- Prioritize platform work based on developer-hours-saved, not technical elegance.

### Timeline
- **Weeks 1-2**: Survey feature teams to identify top friction points. Audit current ticket backlog.
- **Weeks 3-6**: Build and ship first 2 self-service solutions.
- **Weeks 7-10**: Ship 1-2 more. Begin platform embedding rotation.
- **Weeks 11-12**: Re-survey. Measure reduction in platform tickets.

---

## 5. Communication & Sprint Transparency

### Current Problem
PMs complain that engineering "goes dark" mid-sprint. This erodes trust and leads to misaligned priorities.

### Recommendations

**Async status updates**
- Engineers post a brief daily standup update in a shared Slack channel or tool (Geekbot, Standuply, or just a pinned thread): What I did, what I'm doing, any blockers.
- This replaces or supplements synchronous standups, which often become rote.

**Mid-sprint check-ins**
- At the midpoint of each sprint (e.g., Wednesday of a 2-week sprint), hold a 30-minute sync between the tech lead and PM for each team. Review: Are we on track? Any scope changes needed? Any surprises?
- If something is at risk, surface it here -- not at sprint review.

**Work-in-progress visibility**
- Use your project management tool (Jira, Linear, etc.) rigorously. Every piece of work should have a ticket. Ticket status should reflect reality.
- Automate status transitions where possible (e.g., PR opened = "In Review", PR merged = "Done").

**Demo culture**
- End every sprint with a 30-minute demo. Engineers show working software, not slides. PMs, designers, and stakeholders attend.
- This builds shared understanding and celebrates progress.

**Escalation norms**
- Define a clear norm: If a task is blocked for more than half a day, escalate. No one should silently spin.
- Create a lightweight escalation path: engineer -> tech lead -> engineering manager. Response expected within 2 hours during business hours.

### Timeline
- **Week 1**: Set up async standup tooling. Announce new norms.
- **Week 2**: Begin mid-sprint check-ins.
- **Weeks 3-4**: Automate ticket status transitions. Introduce demo culture.
- **Weeks 5-12**: Iterate based on PM and engineer feedback.

---

## 6. Metrics & Accountability

### What to Measure

Track these weekly and review them in a monthly engineering leadership meeting:

| Metric | Current Baseline | 90-Day Target |
|---|---|---|
| Deploy frequency | 2x/week | 1x/day (minimum) |
| PR review time (first review) | 3+ days | < 4 hours |
| PR merge time (open to merge) | 4-5 days (est.) | < 24 hours |
| P1 incidents/month | 2 | 1 or fewer |
| Mean time to recovery (MTTR) | Unknown (measure) | < 1 hour |
| Platform team tickets from feature teams | Unknown (measure) | 50% reduction |
| Sprint goal completion rate | Unknown (measure) | > 80% |

### How to Measure
- **Deploy frequency**: Count production deploys per day from CI/CD logs.
- **PR metrics**: Use GitHub/GitLab API or a tool like LinearB.
- **Incident metrics**: Track in PagerDuty or your incident management tool.
- **Platform tickets**: Track in your ticketing system with a "platform" label.
- **Sprint completion**: Track in your project management tool.

### Accountability
- Each team's tech lead owns their team's metrics and reports weekly.
- The engineering manager reviews cross-team trends monthly.
- Share a monthly "engineering health" summary with the broader org (PMs, leadership) to build trust.

---

## 7. Implementation Roadmap (12-Week Overview)

### Phase 1: Foundation (Weeks 1-4)
- Set up feature flag infrastructure
- Implement CODEOWNERS and PR review SLAs
- Define incident severity levels and set up PagerDuty with team-based rotations
- Survey feature teams on platform friction points
- Launch async standups and mid-sprint check-ins
- Begin measuring all baseline metrics

### Phase 2: Build (Weeks 5-8)
- Roll out automated deploys (canary/rolling) across services
- Ship first self-service platform tools
- Implement observability improvements targeting top P1 category
- Teams draft runbooks; conduct P1 retrospective
- Automate ticket status transitions
- Review and adjust PR review SLAs based on data

### Phase 3: Scale & Refine (Weeks 9-12)
- Achieve daily deploys; sunset manual release trains
- Ship remaining self-service platform tools
- Refine alerting and on-call processes
- Re-survey feature teams on platform experience
- Conduct quarter retrospective; measure against targets
- Document what worked and plan next quarter

---

## 8. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Engineers resist daily deploys due to fear of breaking production | Start with low-risk services. Invest heavily in canary deploys and automated rollback. Celebrate successful daily deploys. |
| PR review SLAs feel like surveillance | Frame as a team norm, not a management mandate. Track at team level, not individual level initially. |
| On-call burden feels unfair across teams (some services are noisier) | Invest in reducing alert noise first. Compensate on-call with time off or stipend. |
| Platform self-service tools take too long to build | Start with the simplest wins (documentation, templates, scripts) before building full self-service platforms. |
| PMs over-index on new communication rituals | Keep ceremonies lightweight. If a mid-sprint check-in has nothing to discuss, cancel it. Avoid process theater. |
| Quarter is too short to achieve all goals | Prioritize deploy frequency and P1 reduction as the primary goals. Communication and platform improvements are supporting goals that may extend into Q2. |

---

## 9. Cultural Principles to Reinforce

Throughout this transformation, consistently reinforce these principles:

1. **Ownership over assignment.** Teams own their services end-to-end: building, shipping, running, and fixing them.
2. **Small batches over big bangs.** Small PRs, small deploys, small experiments. Reduce the blast radius of everything.
3. **Transparency over opacity.** Share status, share metrics, share post-mortems. Default to open.
4. **Automation over manual gates.** If a human is doing something a machine could do, automate it.
5. **Speed and safety are not tradeoffs.** Deploying more frequently with smaller changes is both faster and safer than deploying less frequently with larger changes.

---

## 10. Quick Wins (First 2 Weeks)

To build momentum, prioritize these high-impact, low-effort changes immediately:

1. **Set up CODEOWNERS** -- 1 hour of work, immediate impact on review assignment.
2. **Add automated linting to CI** -- eliminates an entire class of review comments.
3. **Announce PR review SLA** (4-hour first review) -- costs nothing, sets expectations.
4. **Assign on-call by team** in PagerDuty -- can be done in a day.
5. **Start async standups** -- pick a Slack bot and turn it on.
6. **Schedule the first mid-sprint PM check-in** -- put it on the calendar now.
7. **Pull the last 6 months of P1 data** and categorize root causes -- the analysis alone will reveal your highest-leverage improvement.

These seven actions can all be completed in the first two weeks and will create visible, immediate improvements in velocity, reliability, and communication.
