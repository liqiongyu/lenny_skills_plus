# North Star Metric Pack: B2B SaaS Team Collaboration Tool

## 1. Context & Product Summary

**Product type:** B2B SaaS platform for team collaboration (e.g., comparable to Slack, Microsoft Teams, Notion, or Asana in the collaboration space)

**Core value proposition:** Enable distributed and co-located teams to communicate, coordinate work, and share knowledge more effectively, reducing friction in cross-functional collaboration and accelerating decision-making.

**Primary user segments:**
- Individual contributors (ICs) who use the tool daily for communication and task coordination
- Team leads / managers who oversee work, run standups, and track team progress
- Executives / admins who provision accounts, manage billing, and monitor adoption
- Cross-functional stakeholders (design, engineering, marketing, sales) who collaborate on shared projects

**Business model:** Seat-based SaaS subscription (freemium tier + paid Team and Enterprise plans), with revenue driven by seat expansion within accounts and plan upgrades.

**Stage:** Growth stage (post product-market fit, focused on scaling adoption and retention)

---

## 2. North Star Metric Definition

### Chosen North Star Metric

> **Weekly Active Collaborating Teams (WACT)**
>
> *The number of teams (defined as 3+ users within the same workspace) that performed at least 2 distinct collaborative actions in the past 7 days.*

### Why This Metric

A strong North Star Metric for a B2B collaboration tool must satisfy three criteria outlined by Amplitude/Lenny Rachitsky's framework:

| Criterion | How WACT Satisfies It |
|---|---|
| **Reflects value delivered to customers** | A team that collaborates multiple times per week is genuinely getting value from the product. Single-user activity or passive logins do not indicate collaboration value. |
| **Represents a leading indicator of revenue** | Revenue in seat-based B2B SaaS grows when more teams within an account adopt the tool and when existing teams expand. WACT directly tracks the unit of monetization (teams/seats) and the behavior that drives retention. |
| **Is actionable** | Product, growth, and customer success teams can influence WACT through onboarding improvements, feature launches, integrations, and activation campaigns. |

### Definition Details

| Component | Specification |
|---|---|
| **"Team"** | A group of 3 or more users within the same workspace or organizational unit. Can be an explicit team entity or inferred from a shared channel/project with 3+ active members. |
| **"Collaborative action"** | Any action that involves interaction between 2+ people: sending a message in a shared channel, commenting on a task, co-editing a document, completing a shared workflow step, @mentioning a colleague, reacting to someone's post, or participating in a huddle/call. Excludes solo actions (private notes, personal settings changes). |
| **"2 distinct collaborative actions"** | The team collectively performs at least 2 qualifying actions in the 7-day window. This threshold filters out teams that only passively open the app. |
| **Measurement cadence** | Computed daily on a rolling 7-day window. Reported weekly in executive dashboards; trended monthly and quarterly. |
| **Segmentation dimensions** | By company size (SMB / Mid-Market / Enterprise), by plan tier (Free / Team / Enterprise), by geography, by team function, by account age cohort. |

### Metric Alternatives Considered and Rejected

| Candidate | Reason for Rejection |
|---|---|
| **DAU or WAU** | Too generic; does not distinguish between a user who logs in passively and one who actually collaborates. A collaboration tool's value is inherently multi-user. |
| **Messages sent per week** | Too narrow; captures only one modality of collaboration. Teams that primarily use task boards, shared docs, or video would be undercounted. |
| **Net Revenue Retention (NRR)** | A lagging financial indicator, not a leading product-usage metric. By the time NRR dips, the damage is already done. |
| **Weekly Active Users (WAU)** | Does not capture the *team-level* value. A workspace could have many individual active users who never interact, which is a failure mode for a collaboration tool. |
| **Time spent in app** | Vanity metric. More time could mean the tool is confusing, not that it is delivering value. |

---

## 3. Input Metric Driver Tree

The driver tree decomposes the North Star Metric into actionable layers that different teams can own and influence.

```
                    NORTH STAR METRIC
            Weekly Active Collaborating Teams (WACT)
                           |
          -----------------+-----------------
          |                |                |
     [BREADTH]        [DEPTH]         [FREQUENCY]
   # of Activated    Collaboration    Avg Collaborative
      Teams          Intensity per     Sessions per
                       Team              Team/Week
          |                |                |
    +-----+-----+    +----+----+     +-----+-----+
    |           |     |         |     |           |
 New Team   Retained  Actions   Unique  Days      Return
 Activation Collab.   per Team  Action  Active    Rate
  Rate      Teams     per Week  Types   per Week  (W1->W2)
    |           |         |       Used
    |           |         |
  +-+-+     +--+--+    +--+--+
  |   |     |     |    |     |
Sign-  Team  Churn  Re-   Msg  Task/Doc
up to  Invite Rate  activ. Volume Collab
1st    Accept       Rate          Volume
Collab Rate
Action
```

### Layer 1: Breadth Metrics (Acquisition & Activation)

| Metric | Definition | Owner | Target |
|---|---|---|---|
| **New Team Activation Rate** | % of newly created workspaces/teams that reach the "activated" state (3+ members, 2+ collaborative actions) within 14 days of signup | Growth / Onboarding | > 40% |
| **Signup-to-First-Collaborative-Action Time** | Median time from account creation to the first collaborative action involving 2+ users | Growth / Product | < 24 hours |
| **Team Invite Acceptance Rate** | % of team invitations sent that result in an accepted invite and a logged-in user within 7 days | Growth / Product | > 60% |
| **Workspace Creation Rate** | Number of new workspaces created per week | Marketing / Growth | Trending up QoQ |

### Layer 2: Depth Metrics (Engagement Quality)

| Metric | Definition | Owner | Target |
|---|---|---|---|
| **Collaborative Actions per Team per Week** | Average number of qualifying collaborative actions performed by each active team in a 7-day window | Product / Engagement | > 50 actions/team/week |
| **Unique Collaboration Modalities Used** | Average number of distinct collaboration types used per team per week (messaging, task comments, doc co-editing, reactions, video/huddle, file sharing) | Product | >= 3 modalities |
| **Cross-Team Collaboration Rate** | % of active teams that interact with at least one other team in the same account per week | Product / Platform | > 25% |
| **Integration Adoption Rate** | % of active teams using at least 1 third-party integration (e.g., Google Drive, GitHub, Jira, Figma) | Ecosystem / Partnerships | > 35% |

### Layer 3: Frequency Metrics (Retention & Habit)

| Metric | Definition | Owner | Target |
|---|---|---|---|
| **Days Active per Team per Week** | Average number of distinct days a team has collaborative activity in a 7-day window | Product / Engagement | >= 4 days |
| **Week-over-Week Team Return Rate** | % of teams active in week N that are also active in week N+1 | Product / CS | > 85% |
| **DAU/WAU Ratio (Stickiness)** | Ratio of daily active collaborating teams to weekly active collaborating teams | Product | > 0.55 (55%) |
| **Reactivation Rate** | % of lapsed teams (inactive for 2+ weeks) that return to active collaboration in a given week | Growth / CS | > 10% |

### Layer 4: Monetization & Expansion Metrics (Business Outcomes)

| Metric | Definition | Owner | Target |
|---|---|---|---|
| **Free-to-Paid Conversion Rate** | % of free-tier workspaces that upgrade to a paid plan within 90 days | Growth / Revenue | > 8% |
| **Net Seat Expansion Rate** | Net change in paid seats within existing accounts (adds minus removes) as % of starting seats, measured monthly | Sales / CS | > 3% MoM |
| **Net Revenue Retention (NRR)** | Annual recurring revenue retained from existing customers including expansion, contraction, and churn | Finance / CS | > 120% |
| **Account-Level Churn Rate** | % of paying accounts that cancel or downgrade to free in a given month | CS / Product | < 2% monthly |

---

## 4. Metric Measurement Playbook

### Data Collection Requirements

| Data Point | Source | Collection Method |
|---|---|---|
| User actions (messages, comments, reactions, edits) | Product event stream | Real-time event tracking (e.g., Segment, Amplitude, or internal pipeline) |
| Team/workspace membership | Application database | Nightly ETL to analytics warehouse |
| Invite sends and acceptances | Application database + email service | Event tracking + transactional email logs |
| Subscription and billing data | Billing system (Stripe, etc.) | Daily sync to data warehouse |
| Integration usage | Integration platform logs | Event tracking per integration action |

### Instrumentation Checklist

- [ ] Every collaborative action emits a structured event with: `user_id`, `team_id`, `workspace_id`, `action_type`, `timestamp`, `target_object_id`, `collaborator_ids`
- [ ] Team membership changes (join, leave, invite) are tracked as distinct events
- [ ] A derived table `team_weekly_activity` is computed daily, aggregating collaborative actions per team per rolling 7-day window
- [ ] WACT is computed from `team_weekly_activity` where `distinct_collaborative_actions >= 2` and `team_member_count >= 3`
- [ ] Dashboard refreshes daily by 6:00 AM UTC

### Dashboard Layout (Recommended)

**Executive Dashboard (weekly cadence):**
1. WACT trend line (8-week view) with WoW % change
2. WACT by segment (plan tier, company size, geography)
3. Activation funnel: Signups -> Invited 3+ -> First Collab Action -> Activated Team
4. Week-over-week retention cohort heatmap
5. Top 5 movers (accounts with biggest WACT increase/decrease)

**Product Team Dashboard (daily cadence):**
1. Daily snapshot of WACT with 7-day rolling average
2. Collaborative actions breakdown by type (message, comment, co-edit, reaction, call)
3. Modality adoption distribution
4. New team activation rate (14-day cohort)
5. Feature-level engagement (which features drive the most collaborative actions)

**Growth Team Dashboard (daily cadence):**
1. Signup-to-activation funnel with conversion rates at each step
2. Invite send rate and acceptance rate by channel (email, link, SSO)
3. Reactivation rate and lapsed team count
4. Free-to-paid conversion pipeline

---

## 5. Goal-Setting Framework

### Quarterly OKR Example

**Objective:** Accelerate team-level adoption and deepen collaboration habits

| Key Result | Current | Target | Timeline |
|---|---|---|---|
| Increase WACT from 12,000 to 15,600 | 12,000 | 15,600 (+30%) | Q3 end |
| Improve new team activation rate from 35% to 45% | 35% | 45% | Q3 end |
| Increase average collaboration modalities per team from 2.1 to 3.0 | 2.1 | 3.0 | Q3 end |
| Improve W1-to-W2 team retention from 82% to 87% | 82% | 87% | Q3 end |

### Benchmarking Guidance

For a B2B SaaS collaboration tool at growth stage:

| Metric | Below Average | Average | Best-in-Class |
|---|---|---|---|
| DAU/WAU (stickiness) | < 40% | 40-55% | > 60% |
| New team activation (14-day) | < 25% | 25-40% | > 50% |
| Week-over-week team retention | < 75% | 75-85% | > 90% |
| Free-to-paid conversion (90-day) | < 4% | 4-8% | > 12% |
| Net Revenue Retention | < 100% | 100-120% | > 130% |

---

## 6. Anti-Gaming & Guardrail Metrics

The North Star Metric should never be optimized in isolation. Define guardrail metrics that ensure WACT growth is healthy:

| Guardrail Metric | What It Prevents | Threshold |
|---|---|---|
| **NPS / CSAT Score** | Prevents growth at the cost of user satisfaction (e.g., spammy notifications to boost activity) | NPS > 40; CSAT > 4.0/5.0 |
| **Support Ticket Volume per Active Team** | Prevents counting teams that are active but struggling | < 0.5 tickets/team/month |
| **Spam / Low-Quality Action Rate** | Prevents inflation of collaborative actions with bot-generated or trivial activity | < 2% of total actions flagged |
| **User-Reported Notification Overload** | Prevents engagement tactics that annoy users | < 5% of users report overload in surveys |
| **Gross Margin** | Prevents acquiring/retaining teams at unsustainable cost | > 70% |
| **Seat Utilization Rate** | Prevents counting teams where only 1-2 of 10 seats are active | > 60% of paid seats active monthly |

---

## 7. Driver Tree to Action: Strategic Playbook

### Lever 1: Accelerate New Team Activation

**Problem:** Many signups never invite teammates or complete a collaborative action.

**Initiatives:**
1. **Guided onboarding flow** -- After signup, prompt the user to invite 2+ teammates before showing the main workspace. Pre-populate a "Getting Started" channel/project with a collaborative template (e.g., "Introduce yourself" prompt, a shared task checklist).
2. **Magic invite link** -- Generate a shareable link that auto-joins new members to the team with one click (no email confirmation friction).
3. **Bot-assisted first collaboration** -- Deploy an onboarding bot that prompts the team to complete a simple collaborative exercise (e.g., "Everyone react to this message with your favorite emoji" or "Assign one task to a teammate").
4. **Time-to-value email drip** -- For teams that sign up but do not activate within 48 hours, trigger a 3-email sequence with social proof, a video walkthrough, and a direct offer for a live onboarding session.

### Lever 2: Deepen Collaboration Modalities

**Problem:** Teams use only messaging but do not adopt richer collaboration features (tasks, docs, video).

**Initiatives:**
1. **Contextual feature discovery** -- When a user shares a bullet list in chat, suggest converting it to a task board. When a user pastes a long document, suggest creating a shared doc instead.
2. **Weekly team digest** -- Send each team lead a weekly summary: "Your team sent 120 messages, completed 5 tasks, and co-edited 0 documents this week. Try collaborative docs for your next project brief."
3. **Template gallery** -- Offer pre-built project templates (Sprint Planning, Product Launch, Design Review) that inherently use multiple collaboration modalities.
4. **Integration prompts** -- When a user mentions a tool by name (e.g., "I updated the Figma file"), prompt them to install the integration for seamless in-app collaboration.

### Lever 3: Improve Week-over-Week Retention

**Problem:** Teams try the tool for 1-2 weeks but revert to email or other tools.

**Initiatives:**
1. **Habit loop triggers** -- Implement smart notifications that surface unread items at optimal times (based on the team's historical activity patterns), creating a daily check-in habit.
2. **Workflow lock-in** -- Build features that become the system of record (e.g., standup automation, decision logs, meeting notes archive) so the cost of switching away increases.
3. **Champion program** -- Identify the most active user in each team ("champion") and provide them with advanced tips, early access to features, and recognition to keep them engaged and evangelizing.
4. **Health score alerting** -- Build an internal team health score. When a previously active team's score drops (fewer actions, fewer active members), trigger a customer success intervention (in-app prompt or CSM outreach).

### Lever 4: Expand Within Accounts

**Problem:** One team in a company uses the tool but other departments remain on legacy tools.

**Initiatives:**
1. **Cross-team discovery** -- When a user @mentions someone outside their team, suggest creating a cross-team channel/project, exposing the tool to new groups.
2. **Admin expansion dashboard** -- Give workspace admins visibility into which departments have adopted and which have not, with a "Send Invite" button for unadopted teams.
3. **Department-specific templates** -- Create tailored templates for Sales, Engineering, Marketing, HR, and Support teams so each department sees immediate relevance.
4. **Enterprise SSO + auto-provisioning** -- Reduce friction for large-scale rollouts by supporting SCIM provisioning so IT can deploy to the entire org at once.

---

## 8. Review Cadence & Governance

| Review | Cadence | Participants | Focus |
|---|---|---|---|
| **Daily standup metric check** | Daily | Product + Growth leads | WACT daily snapshot, activation funnel anomalies |
| **Weekly metric review** | Weekly | Product, Growth, Engineering, Design leads | WACT trend, driver metrics, experiment results |
| **Monthly business review** | Monthly | VP/C-level + all functional leads | WACT vs. target, monetization metrics, strategic pivots |
| **Quarterly North Star audit** | Quarterly | CEO, CPO, CTO, CFO | Validate that WACT still reflects true value; adjust definition or targets if needed |

### When to Reconsider the North Star Metric

Revisit the North Star Metric if any of the following occur:
- **Business model shift** (e.g., moving from seat-based to usage-based pricing)
- **Product pivot** (e.g., shifting from team collaboration to enterprise knowledge management)
- **WACT grows but revenue does not** (indicates the metric has decoupled from business value)
- **Market maturation** (e.g., collaboration becomes table stakes and differentiation shifts to AI/automation features)
- **Acquisition changes the product scope** significantly

---

## 9. Implementation Checklist

### Phase 1: Foundation (Weeks 1-2)
- [ ] Align leadership on WACT as the North Star Metric
- [ ] Define and document the precise event taxonomy for collaborative actions
- [ ] Audit current event instrumentation against the required data points
- [ ] Instrument any missing events in the product

### Phase 2: Measurement (Weeks 3-4)
- [ ] Build the `team_weekly_activity` derived table in the data warehouse
- [ ] Compute WACT historically (backfill at least 6 months) to establish baselines
- [ ] Build the executive, product, and growth dashboards
- [ ] Validate data accuracy by spot-checking 10-20 teams manually

### Phase 3: Operationalize (Weeks 5-8)
- [ ] Set quarterly WACT targets and decompose into driver metric targets
- [ ] Assign each driver metric to a team owner
- [ ] Establish the weekly review cadence
- [ ] Kick off the first round of initiatives targeting the weakest drivers
- [ ] Set up automated alerts for significant WACT drops (> 5% WoW)

### Phase 4: Iterate (Ongoing)
- [ ] Run A/B experiments tied to specific driver metrics
- [ ] Conduct quarterly North Star audit
- [ ] Refine the metric definition as product and market evolve
- [ ] Share WACT progress in all-hands meetings to build company-wide alignment

---

## 10. Summary

| Element | Detail |
|---|---|
| **North Star Metric** | Weekly Active Collaborating Teams (WACT) |
| **Definition** | Teams (3+ members) with 2+ collaborative actions in a rolling 7-day window |
| **Primary driver categories** | Breadth (activation), Depth (engagement quality), Frequency (retention/habit) |
| **Key input metrics** | New team activation rate, collaborative actions per team, modalities used, W-o-W retention, invite acceptance rate |
| **Guardrail metrics** | NPS, support tickets, spam rate, seat utilization, gross margin |
| **Review cadence** | Daily check, weekly review, monthly business review, quarterly audit |

This North Star Metric Pack provides the complete framework for a B2B SaaS team collaboration tool to align the entire organization around a single metric that reflects genuine customer value, predicts long-term revenue growth, and is decomposable into actionable initiatives across every function.
