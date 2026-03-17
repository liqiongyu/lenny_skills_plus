# Team Rituals Pack

**Remote Cross-Functional Team: Reduce Chaos, Increase Decision Velocity**

---

## Step 1: Context Snapshot + Outcome Definition

### Context Snapshot

- **Team:** 12 people across 4 functions (Product Management, Design, Engineering, Data)
- **Work mode:** Fully remote
- **Time zones:** Assumed PST/EST spread (3-hour gap). [ASSUMPTION: if the team spans wider zones, async-first patterns become even more critical; adjust ritual times accordingly.]
- **Current symptoms:** Chaotic meetings; unclear who decided what; priorities shift mid-week without notice; too many ad hoc syncs and Slack threads that go in circles; cross-functional handoffs stall because no one knows the current plan
- **Desired outcomes:**
  1. **Decision velocity** -- decisions are made, recorded, and communicated within 24 hours of surfacing
  2. **Priority clarity** -- every person knows the team's top 3 priorities for the week by Monday noon
  3. **Reduced chaos** -- fewer ad hoc syncs; replace "can we hop on a call?" culture with structured async + focused sync
- **Constraints:**
  - Meeting time budget: **4 hours/week max** of recurring sync time per person
  - Decision model: PM owns product decisions; Eng Lead owns technical decisions; escalations go to team lead or skip-level. [ASSUMPTION: standard cross-functional decision rights; adjust if the team uses a different RACI.]
  - Tooling: Calendar (Google Calendar), Docs (Notion or Google Docs), Chat (Slack), Ticketing (Linear/Jira). [ASSUMPTION: standard remote-team stack; replace tool names as needed.]
- **Notes on culture/inclusion:** Remote-first means every ritual must have a doc-first async path. Rotating meeting times to respect PST/EST. No surveillance patterns -- rituals produce artifacts, not attendance reports.

### Why We're Doing This

> "We're designing a small set of Golden Rituals to give 12 cross-functional people priority clarity and fast decisions without adding meeting load."

### What "Good" Feels Like (6 bullets)

1. By Monday noon, everyone knows the week's top 3 priorities and any trade-offs made.
2. Decisions are recorded in a single, searchable decision log within 24 hours.
3. No one asks "wait, did we decide that?" in Slack -- the answer is in the log.
4. Ad hoc "can we sync?" requests drop by 50% within 6 weeks.
5. A new hire on their first Friday can find every ritual, its purpose, and its template.
6. Quarterly, the team explicitly decides which rituals to keep, change, or kill.

---

## Step 2: Ritual Inventory Audit (Keep / Change / Kill)

Since the user described the current state as "chaos" without listing specific existing rituals, we construct a probable inventory for a 12-person cross-functional remote team and audit it. [ASSUMPTION: the rituals below are typical for a team in this situation. If the team has a different set, map each to this framework.]

| Ritual | Purpose (1 line) | Cadence | Duration | Participants | Owner | Primary Outputs | Keep/Change/Kill | Notes |
|---|---|---|---|---|---|---|---|---|
| All-hands / team sync | Status updates from each function | Weekly | 60 min | All 12 | PM | None (verbal updates only) | **Kill** | Classic status-only meeting. Replace with async pulse + focused sync. |
| Daily standup (live) | Blockers and progress | Daily | 15 min | All 12 | Rotating | Verbal updates, no record | **Kill** | 75 min/week of low-value sync for 12 people across 2 time zones. Replace with async daily pulse. |
| Ad hoc decision calls | Unblock decisions in real time | As needed | 15-45 min | 2-6 | Whoever calls it | Decisions (often unrecorded) | **Change** | Symptom of missing decision ritual. Capture in a scheduled decision forum + async proposals. |
| 1:1s (manager) | Career, blockers, coaching | Weekly | 30 min | Manager + report | Manager | Notes (inconsistent) | **Keep** | High-value; add lightweight template for consistency. |
| Sprint planning | Plan next sprint's work | Biweekly | 60 min | Eng + PM + Design | Eng Lead | Sprint backlog | **Change** | Keep but tighten scope; make cross-functional inputs async pre-reads. |
| Design review | Feedback on in-progress designs | Weekly | 45 min | Design + PM + Eng | Design Lead | Feedback log (informal) | **Change** | Valuable but unstructured. Add template; make async-first with sync reserved for decisions. |
| Retro | Reflect and improve | Monthly (inconsistent) | 60 min | All 12 | Rotating | Retro notes (lost in docs) | **Change** | Good intent, poor execution. Make biweekly, templated, with tracked action items. |

### Summary

- **Kill:** 2 rituals (all-hands status sync, daily standup) -- replaced by async patterns and focused sync
- **Change:** 4 rituals (ad hoc decisions, sprint planning, design review, retro) -- restructure with templates and explicit outputs
- **Keep:** 1 ritual (1:1s) -- add lightweight template

**Net effect:** Removing ~2.5 hours/week of low-value sync per person. Reinvesting in focused, artifact-producing rituals within the 4-hour budget.

---

## Step 3: Design Rules + Time Budget

### Ritual Design Principles

1. **Named** -- Every ritual has a memorable name people reference in conversation ("Bring that to Monday Map" or "Log it for Decision Drop").
2. **Templated** -- Every ritual has a copy/paste agenda and notes template stored in a known Notion/Docs location.
3. **Artifact-first** -- Every ritual produces a durable output (decision log entry, priority list, action items). If nothing is written, the ritual did not happen.
4. **Owner-driven** -- Each ritual has a single owner responsible for prep, facilitation, and posting outputs.
5. **Async-by-default** -- Prework is posted 24 hours before sync time. Non-attendees can participate via the doc. Sync time is for decisions, alignment, and learning -- not reading updates.
6. **Time-budgeted** -- Total recurring sync time stays at or below 4 hours/week per person. Every new ritual must retire or shorten an existing one.

### Weekly Sync Time Budget

| Category | Ritual | Frequency | Duration | Per-person weekly cost |
|---|---|---|---|---|
| Alignment | Monday Map | Weekly | 45 min | 45 min |
| Decisions | Decision Drop | 2x/week | 25 min | 50 min |
| Execution | Async Daily Pulse | Daily (async) | ~10 min write | 0 min sync |
| Learning | Retro Rewind | Biweekly | 50 min | 25 min/week avg |
| Belonging | Demo & Donuts | Biweekly | 40 min | 20 min/week avg |
| 1:1s | Existing 1:1s | Weekly | 30 min | 30 min |

**Total recurring sync: ~2 hrs 50 min/week per person** (well within the 4-hour budget, leaving ~70 min buffer for ad hoc needs, sprint planning, and design reviews).

### Naming Scheme

All Golden Rituals use two-word alliterative or rhythmic names that are easy to say in Slack ("Take it to Decision Drop", "Put it in Monday Map").

---

## Step 4: Golden Rituals Shortlist (5 Rituals)

| # | Golden Ritual | Problem It Solves | Primary Outcome | Sync or Async | Time Cost/Week | Replaces |
|---|---|---|---|---|---|---|
| 1 | **Monday Map** | Priorities are unclear; change mid-week without notice | Alignment -- everyone knows the top 3 priorities | Sync (45 min) | 45 min | Kills: all-hands status sync |
| 2 | **Decision Drop** | Decisions are slow, unrecorded, or re-litigated | Decisions -- made, logged, and communicated within 24h | Sync (25 min x2) | 50 min | Kills: most ad hoc decision calls |
| 3 | **Async Daily Pulse** | No visibility into blockers and progress | Execution -- blockers surface early; status is always current | Async only | 0 min sync | Kills: daily standup |
| 4 | **Retro Rewind** | Process problems fester; same mistakes repeat | Learning -- structured reflection with tracked improvements | Sync (50 min biweekly) | 25 min avg | Changes: inconsistent monthly retro |
| 5 | **Demo & Donuts** | Cross-functional silos; no shared wins; low belonging | Belonging -- celebrate progress; build cross-functional empathy | Sync (40 min biweekly) | 20 min avg | New (but displaces no sync time -- fits in budget) |

### Outcome Mapping

| Outcome | Supported by |
|---|---|
| Priority clarity | Monday Map, Async Daily Pulse |
| Decision velocity | Decision Drop, Monday Map (trade-off decisions) |
| Reduced chaos / fewer ad hoc syncs | Async Daily Pulse, Decision Drop |
| Continuous improvement | Retro Rewind |
| Cross-functional belonging | Demo & Donuts |

**Every ritual earns its slot.** No "nice-to-have" meetings. Each ritual maps to at least one of the three stated outcomes (priority clarity, decision velocity, reduced chaos) or to the supporting outcomes (learning, belonging) that prevent decay over time.

---

## Step 5: Ritual Specs + Templates

---

### Golden Ritual 1: Monday Map

**Purpose**
- Problem: Priorities are unclear; people start the week working on different things; trade-offs happen in side-channels.
- Outcomes: (1) Team-wide clarity on top 3 priorities for the week. (2) Trade-offs and deprioritizations are explicit. (3) Cross-functional dependencies are surfaced.

**Cadence + Logistics**
- Cadence: Weekly, every Monday
- Duration: 45 minutes
- Time: Rotating between 10am PT / 1pm ET and 9am PT / 12pm ET (alternate weeks to share the load)
- Participants: All 12 (required: PM, Eng Lead, Design Lead, Data Lead; optional: ICs)
- Owner/Facilitator: PM (permanent owner; facilitator rotates monthly among leads)
- Location: [Calendar invite link] + [Notion: Monday Map template page]

**Prework (async-first) -- posted by Friday EOD**
- PM posts a draft "Monday Map" doc by Friday 5pm PT containing: (a) proposed top 3 priorities for next week, (b) key trade-offs or deprioritizations, (c) open questions needing sync discussion.
- Each function lead adds a 2-3 bullet update on: capacity, blockers, and dependency flags by Sunday evening.
- All participants review and add comments/questions in the doc before the meeting.

**Agenda / Format (timeboxed)**
1. (5 min) -- **Check-in + context.** Facilitator frames the week. Any urgent external changes.
2. (15 min) -- **Priority review.** Walk through the proposed top 3. Challenge, adjust, and confirm. Record trade-offs.
3. (10 min) -- **Dependency sync.** Each function flags cross-functional blockers. Assign owners for unblocking.
4. (10 min) -- **Open decisions.** Surface decisions needed this week. If solvable in <3 min, decide now. Otherwise, queue for Decision Drop.
5. (5 min) -- **Commitments + close.** Facilitator reads back the final top 3 priorities and action items. Everyone confirms.

**Outputs (artifacts)**
- **Monday Map doc** (updated live during meeting): final top 3 priorities, trade-offs, dependency owners, decisions queued for Decision Drop
- **Slack post** (within 30 min of meeting end): PM posts a 5-line summary in #team-main: "This week's top 3: [X, Y, Z]. Key trade-off: [A]. Decisions pending: [B]."
- Action items with owner + due date logged in the doc

**Decision Rules**
- PM decides priority ranking for product scope
- Eng Lead decides technical sequencing
- Disagreements: 2-minute discussion, then the designated decision-maker calls it
- Escalation: if leads disagree on a cross-cutting trade-off, escalate to skip-level by EOD Monday

**Success Signals**
- Leading (2-6 weeks): fewer "what are we working on?" Slack questions; Monday Map doc is consistently updated before the meeting
- Lagging: mid-week priority changes drop by 50%; team satisfaction survey shows higher clarity scores

**Anti-patterns + Fixes**
- Anti-pattern: Monday Map becomes a status meeting (people read updates aloud).
  - Fix: Status is in the prework doc. Facilitator redirects: "That's in the doc -- what decision or trade-off do you need?"
- Anti-pattern: PM posts the Monday Map but no one reads prework.
  - Fix: Start the meeting by asking "What questions did you have from the prework?" -- silence means skip to decisions.
- Anti-pattern: Too many priorities (>5).
  - Fix: Hard cap at 3 priorities. If the team can't cut, escalate the trade-off.

**Async Fallback**
- Non-attendees: read the Monday Map doc + Slack summary. Add comments in the doc by Monday EOD. Facilitator flags any unresolved comments in Slack.
- Recording: auto-record and post link in the doc for anyone who missed it.

---

#### Monday Map Template (copy/paste)

```markdown
# Monday Map -- Week of [DATE]

**Facilitator:** [Name]
**Attendees:** [List]

## Prework (posted by Friday 5pm PT)
### Proposed Top 3 Priorities
1. [Priority 1 -- owner]
2. [Priority 2 -- owner]
3. [Priority 3 -- owner]

### Trade-offs / Deprioritized
- [Item deprioritized] -- reason: [why]

### Function Updates (2-3 bullets each)
- **PM:**
- **Design:**
- **Eng:**
- **Data:**

### Open Questions for Sync
- [ ] [Question 1]
- [ ] [Question 2]

---

## Meeting Notes

### Final Top 3 Priorities (confirmed)
1. [Priority 1 -- owner]
2. [Priority 2 -- owner]
3. [Priority 3 -- owner]

### Trade-offs Decided
| What | Decision | Decided by | Rationale |
|---|---|---|---|
|  |  |  |  |

### Dependencies Flagged
| Dependency | Between | Owner | Due |
|---|---|---|---|
|  |  |  |  |

### Decisions Queued for Decision Drop
- [ ] [Decision topic -- requestor]

### Action Items
| Action | Owner | Due |
|---|---|---|
|  |  |  |

### Slack Summary (post within 30 min)
> This week's top 3: [X, Y, Z]. Key trade-off: [A]. Decisions pending: [B].
```

---

### Golden Ritual 2: Decision Drop

**Purpose**
- Problem: Decisions are slow, scattered across Slack threads, or made in ad hoc calls and never recorded. People relitigate decisions because there is no log.
- Outcomes: (1) Decisions are made within 24 hours of being queued. (2) Every decision is recorded in a searchable decision log. (3) Ad hoc "can we sync?" requests drop significantly.

**Cadence + Logistics**
- Cadence: Twice per week (Tuesday and Thursday)
- Duration: 25 minutes
- Time: Alternating -- Tuesdays at 10am PT / 1pm ET; Thursdays at 9am PT / 12pm ET
- Participants: Required: PM, Eng Lead, Design Lead, Data Lead (4 people). Optional: ICs relevant to a specific decision (invited per-topic).
- Owner/Facilitator: Rotating weekly among the 4 leads
- Location: [Calendar invite link] + [Notion: Decision Drop Log]

**Prework (async-first) -- posted 24h before each session**
- Anyone on the team can queue a decision by adding it to the Decision Drop Log with: (a) the decision question (framed as a yes/no or option A/B/C), (b) context (1-3 sentences + links), (c) their recommendation, (d) who needs to decide.
- Queued decisions are reviewed by the designated decider before the meeting. If the decider can resolve async (comment in the doc), they do so and mark it "decided async."

**Agenda / Format (timeboxed)**
1. (2 min) -- **Async wins.** Facilitator reads out decisions already made async since last session. Celebrate velocity.
2. (18 min) -- **Decision queue.** Walk through queued decisions in priority order. For each: (a) requestor states the question + recommendation (1 min), (b) discussion (2-3 min max), (c) designated decider calls it, (d) facilitator logs decision + owner + next action.
3. (3 min) -- **Escalations.** Flag any decisions that need skip-level input. Assign escalation owner.
4. (2 min) -- **Close.** Facilitator reads back all decisions made. Posts summary to Slack.

**Outputs (artifacts)**
- **Decision Log** (updated live): decision, date, decider, rationale (1 line), follow-up owner, status
- **Slack summary** (within 15 min): "#decisions: [N] decisions made today: [list]. [M] escalated."
- Escalation items added to skip-level agenda

**Decision Rules**
- Product scope: PM decides
- Technical approach: Eng Lead decides
- Design direction: Design Lead decides
- Data methodology: Data Lead decides
- Cross-cutting (affects 2+ functions): PM + Eng Lead jointly; if no consensus in 3 min, escalate
- Escalation path: skip-level 1:1 or async Slack thread with skip-level within 24h

**Success Signals**
- Leading: decision queue is consistently populated 24h before; async decisions increase over time
- Lagging: ad hoc "quick sync" requests drop by 50% within 4 weeks; "wait, did we decide that?" questions disappear

**Anti-patterns + Fixes**
- Anti-pattern: Decision Drop becomes a discussion forum (no decisions made, just debates).
  - Fix: Facilitator enforces the "1 min present, 3 min discuss, decide" cadence. If not resolvable in 3 min, it needs a separate writeup with options; queue for next session.
- Anti-pattern: People bypass Decision Drop and make decisions in Slack DMs.
  - Fix: Team norm: "If it affects more than you, log it in Decision Drop." Facilitator flags unlogged decisions in the Tuesday session.
- Anti-pattern: Only PM queues decisions.
  - Fix: Explicitly invite all ICs to queue decisions. Celebrate when non-leads use the queue.

**Async Fallback**
- Proposals are in the doc 24h before. Non-attendees add their input as comments. The designated decider can decide async.
- If a decision affects a non-attendee, the facilitator tags them in the doc for review before marking it final.
- Full recording available; Slack summary posted within 15 min.

---

#### Decision Drop Template (copy/paste)

```markdown
# Decision Drop -- [DATE]

**Facilitator:** [Name]
**Attendees:** [List]

## Async Decisions (made since last session)
| # | Decision | Decider | Date | Rationale | Follow-up Owner |
|---|---|---|---|---|---|
| D-[###] |  |  |  |  |  |

## Decision Queue (sync)
| # | Decision Question | Requestor | Recommendation | Designated Decider | Context Link |
|---|---|---|---|---|---|
| D-[###] |  |  |  |  |  |

## Decisions Made (this session)
| # | Decision | Decider | Rationale (1 line) | Follow-up Action | Owner | Due |
|---|---|---|---|---|---|---|
| D-[###] |  |  |  |  |  |  |

## Escalations
| Decision | Why escalated | Escalation Owner | Target Resolution Date |
|---|---|---|---|
|  |  |  |  |

## Slack Summary (post within 15 min)
> #decisions: [N] decisions made today: [list 1-liners]. [M] escalated to [whom].
```

---

### Golden Ritual 3: Async Daily Pulse

**Purpose**
- Problem: Daily standups waste sync time for updates that could be written. Blockers surface too late. People lack visibility into cross-functional progress.
- Outcomes: (1) Blockers surface within hours, not days. (2) Everyone has a lightweight daily picture of team progress. (3) Zero sync time consumed.

**Cadence + Logistics**
- Cadence: Daily (weekdays), fully async
- Duration: ~10 minutes to write; ~5 minutes to read
- Participants: All 12 (required)
- Owner: PM (ensures the Slack bot/reminder fires; monitors for unanswered blockers)
- Location: Slack channel #team-pulse (or a daily thread in #team-main)

**Prework**
- None required -- this IS the async update.

**Format**
Each person posts by 10am PT / 1pm ET daily in the #team-pulse channel using this format:

```
**[Name] -- [Date]**
Done: [1-2 bullets of what shipped/completed yesterday]
Today: [1-2 bullets of focus for today]
Blocked: [anything blocking progress -- tag the person who can unblock]
FYI: [optional -- anything the team should know]
```

- PM reviews all posts by 11am PT and flags any unresolved blockers in a reply thread or DMs the relevant person.
- If a blocker requires a decision, PM queues it in the Decision Drop Log.

**Outputs (artifacts)**
- Daily written record of team progress and blockers (searchable in Slack)
- Blocker escalation to Decision Drop when needed

**Decision Rules**
- No decisions are made in the Pulse -- it is information flow only
- If a blocker requires a decision, it goes to Decision Drop

**Success Signals**
- Leading: 80%+ daily participation within 2 weeks; blockers get responses within 2 hours
- Lagging: ad hoc "quick status?" DMs drop; PM can summarize team progress from the Pulse without asking anyone

**Anti-patterns + Fixes**
- Anti-pattern: Pulse becomes performative (long essays to "look busy").
  - Fix: Enforce the 1-2 bullet format. PM models brevity.
- Anti-pattern: People ignore blockers posted by others.
  - Fix: PM follows up on unresolved blockers by 11am. Norm: "If you're tagged, reply within 2 hours."
- Anti-pattern: No one reads the Pulse.
  - Fix: Monday Map references Pulse blockers. Decision Drop picks up queued items. The Pulse feeds into sync rituals, so it matters.

**Async Fallback**
- This ritual is entirely async. No fallback needed.

---

#### Async Daily Pulse Template (copy/paste -- Slack message)

```
**[Your Name] -- [Date]**
Done:
- [What you completed yesterday]
Today:
- [Your focus for today]
Blocked:
- [Blocker + @person who can help] (or "None")
FYI:
- [Optional -- anything the team should know]
```

---

### Golden Ritual 4: Retro Rewind

**Purpose**
- Problem: Process problems fester because there is no structured reflection. The same mistakes repeat. People feel unheard about what's not working.
- Outcomes: (1) Process improvements are identified and tracked. (2) Psychological safety increases as people see their feedback lead to changes. (3) The ritual system itself evolves based on real feedback.

**Cadence + Logistics**
- Cadence: Biweekly (every other Friday)
- Duration: 50 minutes
- Time: 11am PT / 2pm ET (end-of-week reflection)
- Participants: All 12 (required)
- Owner/Facilitator: Rotating (each team member facilitates once per quarter)
- Location: [Calendar invite link] + [Notion: Retro Rewind page]

**Prework (async-first) -- posted by Thursday 5pm PT**
- Facilitator posts the Retro Rewind doc with 3 prompts:
  1. What went well this sprint/period? (keep doing)
  2. What was frustrating or broken? (change)
  3. What should we stop doing? (kill)
- All participants add their items (anonymously if desired -- use a tool like EasyRetro or anonymous Notion comments) by Thursday EOD.
- Facilitator clusters and themes the items before the meeting.

**Agenda / Format (timeboxed)**
1. (5 min) -- **Check-in.** Brief personal check-in (one word or emoji for energy level). Sets psychological safety.
2. (5 min) -- **Review previous action items.** Did we follow through on last retro's improvements? Mark done/not done.
3. (15 min) -- **Themed discussion.** Facilitator presents the top 3-4 themes from prework. Team discusses each (no solutioning yet -- just understanding).
4. (15 min) -- **Action brainstorm + commit.** For each theme, propose 1-2 concrete improvements. Vote on top 2-3 to commit to. Assign an owner and a "done by" date.
5. (5 min) -- **Appreciations.** Each person can (optionally) call out someone who helped them. Builds belonging.
6. (5 min) -- **Close.** Facilitator reads back commitments. Posts summary to Slack.

**Outputs (artifacts)**
- **Retro Rewind doc**: themes, discussion notes, committed improvements with owners and due dates
- **Action items** tracked in the team's task system (Linear/Jira) with a "retro" label
- **Slack summary**: "Retro Rewind [date]: Top themes: [X, Y]. Committed improvements: [A (owner), B (owner)]."

**Decision Rules**
- Improvement commitments are decided by dot-vote (each person gets 3 votes)
- Team lead has veto on improvements that require significant resource investment (escalate to Monday Map for prioritization)

**Success Signals**
- Leading: 80%+ prework participation; action items from previous retro are reviewed and mostly completed
- Lagging: recurring complaints decrease over 2-3 cycles; team satisfaction with "ability to improve our process" increases

**Anti-patterns + Fixes**
- Anti-pattern: Retro becomes a venting session with no action items.
  - Fix: Hard timebox on discussion (15 min). Facilitator transitions to "What's one concrete thing we can do about this?"
- Anti-pattern: Same complaints surface every retro (nothing changes).
  - Fix: Review previous action items at the start. If an item is "not done" twice, escalate it to Monday Map as a priority.
- Anti-pattern: People are afraid to raise issues (low psychological safety).
  - Fix: Anonymous prework submission. Facilitator normalizes critique: "What's one thing that frustrated you? I'll go first."

**Async Fallback**
- Non-attendees add items to the prework doc. Facilitator ensures their themes are represented.
- Recording available. Async participants can add comments on proposed improvements within 24 hours before they are finalized.

---

#### Retro Rewind Template (copy/paste)

```markdown
# Retro Rewind -- [DATE]

**Facilitator:** [Name]
**Attendees:** [List]

## Previous Action Items (review)
| Improvement | Owner | Status (Done / Not Done / Carry Over) |
|---|---|---|
|  |  |  |

## Prework Themes (clustered by facilitator)
### Keep (what went well)
- [Theme 1]: [items]
- [Theme 2]: [items]

### Change (what was frustrating)
- [Theme 3]: [items]
- [Theme 4]: [items]

### Kill (what should we stop)
- [Theme 5]: [items]

## Discussion Notes
### Theme: [Name]
- Key points:
- Root cause (if identified):

## Committed Improvements (voted)
| Improvement | Owner | Due Date | Votes |
|---|---|---|---|
|  |  |  |  |

## Appreciations
- [Name] called out [Name] for [reason]

## Slack Summary (post within 15 min)
> Retro Rewind [date]: Themes: [X, Y, Z]. Committed improvements: [A (@owner, due date), B (@owner, due date)].
```

---

### Golden Ritual 5: Demo & Donuts

**Purpose**
- Problem: Cross-functional silos form in remote teams. People don't see each other's work. There's no shared celebration of progress. Belonging erodes.
- Outcomes: (1) Cross-functional empathy -- everyone sees what other functions are building. (2) Shared wins and momentum. (3) Informal connection that replaces hallway conversations.

**Cadence + Logistics**
- Cadence: Biweekly (every other Friday, alternating with Retro Rewind -- so every Friday has one ritual)
- Duration: 40 minutes
- Time: 11am PT / 2pm ET
- Participants: All 12 (required attendance encouraged but no penalty for missing)
- Owner: Rotating "MC" (different person each session -- sign-up sheet)
- Location: [Calendar invite link] + [Notion: Demo & Donuts page]

**Prework (async-first)**
- MC collects 2-4 demo slots (each 5-7 min) by Wednesday EOD. Anyone can sign up to demo work-in-progress, a shipped feature, a data insight, a design exploration, or a process improvement.
- MC posts the lineup in #team-main by Thursday.

**Agenda / Format (timeboxed)**
1. (5 min) -- **Donuts.** Icebreaker question (MC picks from a rotating list: "What's the best thing you ate this week?" / "What's something you learned recently outside work?"). Builds connection.
2. (20-28 min) -- **Demos.** 2-4 demos, 5-7 min each. Format: show the thing, explain why it matters, take 1-2 questions.
3. (5 min) -- **Wins & shoutouts.** Anyone can call out a win or thank a teammate.
4. (2 min) -- **Close.** MC summarizes demos and shoutouts. Posts to Slack.

**Outputs (artifacts)**
- **Demo & Donuts log**: date, demos shown (title + 1-line summary + link to artifact), wins and shoutouts
- **Slack post**: "Demo & Donuts [date]: [Name] showed [X], [Name] shared [Y]. Shoutouts to [Z]."

**Decision Rules**
- No decisions are made in Demo & Donuts -- this is a belonging and visibility ritual
- If a demo surfaces a decision need, it gets queued in Decision Drop

**Success Signals**
- Leading: demo slots fill up without MC chasing; different functions present each session
- Lagging: team reports feeling more connected in quarterly survey; cross-functional collaboration requests increase

**Anti-patterns + Fixes**
- Anti-pattern: Only engineers demo; other functions feel excluded.
  - Fix: MC actively recruits from Design, Data, and PM. Frame demos broadly: a data insight, a user research finding, a process improvement all count.
- Anti-pattern: Demos become polished presentations (too much prep, people avoid signing up).
  - Fix: Norm: "Show work-in-progress, not perfection. 5 min, no slides required."
- Anti-pattern: Attendance drops because it feels optional and low-value.
  - Fix: Keep it short (40 min). Make it fun (donuts icebreaker). Celebrate attendance, don't police it.

**Async Fallback**
- Demos are recorded. MC posts recording + demo log in Slack within 1 hour.
- Non-attendees can add async shoutouts in the Slack thread.

---

#### Demo & Donuts Template (copy/paste)

```markdown
# Demo & Donuts -- [DATE]

**MC:** [Name]

## Donuts (Icebreaker)
Question: [MC's chosen question]
- [Highlights / fun answers]

## Demos
| # | Presenter | Title | Summary (1 line) | Link to Artifact |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## Wins & Shoutouts
- [Name] called out [Name] for [reason]

## Slack Summary (post within 1 hour)
> Demo & Donuts [date]: [Name] showed [X], [Name] shared [Y]. Shoutouts to [Z]. Recording: [link]
```

---

## Step 6: Onboarding Primer + Rollout Plan

### Onboarding Primer: "Known by First Friday"

---

#### Our Golden Rituals (Cheatsheet)

Welcome to the team! Here are the 5 rituals that make our team work. By your first Friday, you should know what each one is, where to find the template, and how to participate.

| # | Ritual Name | What It's For | When | Who Attends | Where the Template Lives |
|---|---|---|---|---|---|
| 1 | **Monday Map** | Set the week's top 3 priorities and surface trade-offs | Monday, 45 min (rotating time) | All 12 | [Notion: Monday Map] |
| 2 | **Decision Drop** | Make and record decisions fast | Tue + Thu, 25 min each | Leads (required); ICs (per-topic) | [Notion: Decision Drop Log] |
| 3 | **Async Daily Pulse** | Surface blockers and progress daily | Daily by 10am PT (async) | All 12 | #team-pulse in Slack |
| 4 | **Retro Rewind** | Reflect, learn, and improve our process | Every other Friday, 50 min | All 12 | [Notion: Retro Rewind] |
| 5 | **Demo & Donuts** | Show work, celebrate wins, build connection | Every other Friday, 40 min | All 12 | [Notion: Demo & Donuts] |

#### How to Use This

1. **Find the templates.** All templates live in Notion under "Team Rituals" (bookmarked in #team-main Slack channel). Each ritual has its own page with the current and past instances.
2. **Understand the purpose.** Read the 1-line "What It's For" above. If unclear, ask your onboarding buddy or the ritual owner.
3. **Prepare prework.** Monday Map and Retro Rewind require prework posted 24h before. Your onboarding buddy will walk you through your first prework.
4. **Participate.** Show up to sync rituals, post your Async Daily Pulse, and sign up for a Demo & Donuts slot when you have something to share (by week 3-4).
5. **Run a ritual.** By your first month, you'll rotate into facilitating at least one ritual. The template has everything you need. Your onboarding buddy will shadow you the first time.

#### Quick Reference

- **Decision needed?** Queue it in the [Decision Drop Log].
- **Blocked?** Post in #team-pulse with @[person who can unblock].
- **Process frustration?** Add it to the next [Retro Rewind] prework doc.
- **Want to show your work?** Sign up for the next [Demo & Donuts].
- **Need the week's priorities?** Check the latest [Monday Map].

---

### Rollout Plan

**Sponsor:** Team lead / PM (owns the rollout and communicates the "why")

#### Phase 0: Prep (Week 0)

- [ ] Finalize Golden Rituals list (confirmed: 5 rituals above)
- [ ] Create Notion workspace: "Team Rituals" with subpages for each ritual (Monday Map, Decision Drop Log, Retro Rewind, Demo & Donuts)
- [ ] Create Slack channel #team-pulse for Async Daily Pulse
- [ ] Set up Slack reminders: daily 9:30am PT reminder in #team-pulse ("Time for your Daily Pulse!")
- [ ] Assign initial ritual owners: PM (Monday Map + Async Daily Pulse), rotating leads (Decision Drop), rotating all (Retro Rewind), rotating MC (Demo & Donuts)
- [ ] Create calendar invites for all sync rituals with Notion links in the description
- [ ] Share the "why" with the team: 5-minute Loom video or Slack post from team lead explaining the change, the goals, and what's being killed/changed

#### Phase 1: Pilot (Weeks 1-2)

- [ ] **Week 1:** Launch Async Daily Pulse + Monday Map only. These are the highest-impact, lowest-risk rituals.
- [ ] **Week 1:** Kill the old all-hands status sync and daily standup. Communicate clearly: "These are replaced by Monday Map and Async Daily Pulse."
- [ ] **Week 2:** Launch Decision Drop (twice/week). Start with a small queue of 2-3 real pending decisions to demonstrate value immediately.
- [ ] **End of Week 2:** Collect feedback with a 3-question Slack poll:
  1. "Is Monday Map giving you clarity on weekly priorities?" (1-5)
  2. "Is Decision Drop helping decisions happen faster?" (1-5)
  3. "What's one thing you'd change about these rituals?"

#### Phase 2: Full Rollout (Weeks 3-6)

- [ ] **Week 3:** Launch Retro Rewind (biweekly). First retro topic: "How are the new rituals working?"
- [ ] **Week 4:** Launch Demo & Donuts (biweekly, alternating Fridays with Retro Rewind).
- [ ] **Week 3:** Publish the Onboarding Primer in Notion and pin it in #team-main.
- [ ] **Week 4:** Reinforce usage norms: "Bring trade-offs to Monday Map", "Queue decisions in Decision Drop", "Post your Pulse by 10am PT".
- [ ] **Week 6:** Run a mini-audit: review the 5 rituals against the time budget. Are we at or below 4 hours/week? Any ritual not earning its slot?

#### Phase 3: Governance (Ongoing)

- [ ] Monthly pulse survey (3 questions in Slack): clarity, decision speed, ritual value
- [ ] Quarterly Ritual Review (see Governance Plan below)
- [ ] Update onboarding primer after each quarterly review

---

## Step 7: Governance Plan + Quality Gate

### Governance Plan

#### Ritual Owners

| Ritual | Owner | Backup |
|---|---|---|
| Monday Map | PM | Eng Lead |
| Decision Drop | Rotating (weekly among 4 leads) | PM covers if needed |
| Async Daily Pulse | PM (monitoring) | Eng Lead |
| Retro Rewind | Rotating (all team members) | Previous facilitator |
| Demo & Donuts | Rotating MC (sign-up) | PM assigns if no sign-up |

#### Quarterly Ritual Review

- **Cadence:** Every quarter (first Monday of the quarter, as an extended Monday Map -- add 30 min)
- **Participants:** All 12
- **Facilitator:** PM

**Agenda:**
1. (5 min) Reconfirm team outcomes -- are the original goals still the right ones?
2. (15 min) Review each ritual: keep/change/kill based on feedback data and ritual metrics
3. (5 min) Review time budget -- are we still within 4 hours/week?
4. (10 min) Decide changes + assign owners for improvements
5. (5 min) Update onboarding primer + ritual index

**Keep/Change/Kill Criteria:**
- **Keep:** Ritual consistently produces its intended output; participation is >75%; team rates it useful (3+ out of 5)
- **Change:** Ritual is valuable but format/cadence/duration needs adjustment; feedback identifies specific friction
- **Kill:** Ritual consistently fails to produce outputs; participation drops below 50%; team rates it <2 out of 5 for two consecutive months; or the problem it solves no longer exists

**Retirement Rules:**
- Any ritual can be proposed for retirement by any team member at any time (async in a Slack thread or at Retro Rewind)
- Retirement requires a keep/change/kill vote at the quarterly review
- When a ritual is killed: remove calendar invite, archive the Notion page (don't delete), update the onboarding primer, and communicate the change in #team-main

#### Feedback Loop

- **Monthly pulse (Slack poll, 3 questions):**
  1. "How clear are you on this week's priorities?" (1-5)
  2. "How fast are decisions being made?" (1-5)
  3. "Which ritual is most/least valuable to you right now?"
- PM reviews results and shares a 3-line summary with the team
- If any score drops below 3.0, PM investigates and proposes an adjustment at the next Monday Map

#### Preventing Ritual Sprawl

- **Hard cap:** Maximum 7 Golden Rituals at any time. Adding a new one requires killing or merging an existing one.
- **Time budget enforcement:** Total sync time must stay at or below 4 hours/week per person. Any proposed ritual must show what it replaces.
- **Annual reset:** Once per year (January), the team does a full ritual audit from scratch -- assume nothing is sacred.

---

### Quality Gate: Checklist Verification

#### A) Golden Ritual Quality (Named / Templated / Known)
- [x] Golden Ritual list is small (5 rituals) and each has a crisp purpose
- [x] Every ritual is **Named** (Monday Map, Decision Drop, Async Daily Pulse, Retro Rewind, Demo & Donuts)
- [x] Every ritual is **Templated** (agenda/notes format provided for each)
- [x] Rituals are **Known by first Friday** (onboarding primer exists)

#### B) System Design (minimal, outcome-driven)
- [x] Rituals map to explicit outcomes (alignment, decisions, execution, learning, belonging)
- [x] Total sync time fits within budget (~2 hr 50 min/week vs 4 hr budget)
- [x] Each ritual has an owner/facilitator responsible for prep and outputs
- [x] Each ritual has an explicit artifact output
- [x] Status-only meetings replaced with async (daily standup -> Async Daily Pulse; all-hands -> Monday Map)

#### C) Template Quality (run-ability)
- [x] Agendas are timeboxed and include required prework
- [x] Outputs are explicit (what gets written, where it lives, who follows up)
- [x] Decision rules are clear (who decides, how to escalate)
- [x] Anti-patterns are listed with fixes (2-3 per ritual)
- [x] Async fallback exists for every sync ritual

#### D) Rollout + Onboarding Readiness
- [x] Rollout plan includes pilot (weeks 1-2), feedback collection, and iteration
- [x] Calendars/docs structure defined with single "Team Rituals" Notion workspace
- [x] New hires can find templates and understand preparation via onboarding primer

#### E) Governance (avoid ritual sprawl)
- [x] Quarterly ritual review scheduled with keep/change/kill decision rules
- [x] Monthly feedback loop (3-question Slack pulse)
- [x] Retirement path defined (proposal -> quarterly vote -> archive + communicate)
- [x] Hard cap of 7 rituals; time budget enforced; annual reset

#### F) Final Pack Completeness
- [x] Includes Risks / Open questions / Next steps (see below)
- [x] Assumptions are labeled throughout
- [x] System is right-sized for a 12-person cross-functional remote team

---

### Rubric Self-Score

| Dimension | Score (1-5) | Rationale |
|---|---|---|
| 1. Outcome alignment + scope clarity | **5** | Three crisp outcomes defined; every ritual maps to at least one; mapping table shows no gaps or redundancy |
| 2. Minimalism + time efficiency | **5** | Kills 2 status meetings; replaces with async; total sync ~2h50m vs 4h budget; every sync minute justified |
| 3. Template + artifact quality | **5** | Every ritual has a timeboxed agenda, explicit artifacts, copy/paste template, and follow-up tracking |
| 4. Adoption + onboarding readiness | **5** | 1-page onboarding primer; templates in known location; new hire can find, understand, and run a ritual by first Friday |
| 5. Governance + iteration | **5** | Quarterly review with keep/change/kill criteria; monthly pulse; retirement rules; hard cap; annual reset |
| 6. Trust, inclusion, async-friendliness | **5** | Async path for every sync ritual; rotating times for PST/EST; doc-first approach; anonymous retro option; no surveillance patterns |

**Total: 30/30** -- Ready to adopt.

---

## Risks / Open Questions / Next Steps

### Risks

1. **Adoption fatigue.** Launching 5 rituals in 4 weeks could feel like "more process." Mitigation: phased rollout (2 rituals first, then add), and clearly kill the old meetings on day 1 so the net load decreases immediately.
2. **Decision Drop becomes a bottleneck.** If too many decisions queue up, 25 minutes is not enough. Mitigation: enforce async-first (most decisions should resolve in the doc); expand to 3x/week only if queue consistently overflows.
3. **Async Daily Pulse compliance drops.** Without a live standup, some people may stop posting. Mitigation: PM monitors daily and follows up individually; reference Pulse data in Monday Map to reinforce its value.
4. **Facilitator rotation quality varies.** Not everyone is a natural facilitator. Mitigation: provide a facilitation cheatsheet (1 page of tips); pair new facilitators with experienced ones for their first session.
5. **Tooling fragmentation.** If templates live in multiple tools (Notion, Google Docs, Slack), discoverability suffers. Mitigation: single source of truth in Notion; Slack is for summaries and reminders only.

### Open Questions

1. **Time zone spread.** Are all team members in PST/EST, or do some span further (e.g., Europe, Asia)? If wider, Async Daily Pulse becomes even more critical, and sync rituals may need async-first redesigns.
2. **Decision rights.** The assumed RACI (PM owns product, Eng Lead owns technical) may not match reality. Validate with the team lead before rollout.
3. **Existing sprint planning and design review.** These were marked "change" in the audit but not replaced by Golden Rituals. Should they be absorbed into Monday Map or Decision Drop, or remain as function-specific rituals outside the Golden set?
4. **1:1 template.** 1:1s were marked "keep" with a template suggestion. Should a lightweight 1:1 template be included in this pack, or is that the manager's responsibility?
5. **Executive visibility.** Does leadership need a ritual for cross-team alignment (e.g., a monthly update from this team)? That would be a product-operations concern, not a team-rituals concern.

### Next Steps

1. **This week:** Team lead reviews this pack and validates assumptions (time zones, decision rights, existing rituals, tooling).
2. **Week 0:** Set up Notion workspace, Slack channel, and calendar invites. Record the 5-minute "why" video. Assign initial ritual owners.
3. **Week 1:** Launch Async Daily Pulse + Monday Map. Kill old all-hands and daily standup.
4. **Week 2:** Launch Decision Drop. Collect first feedback pulse.
5. **Week 3:** Launch Retro Rewind. First retro topic: "How are the new rituals working?"
6. **Week 4:** Launch Demo & Donuts. Publish the onboarding primer.
7. **Week 6:** Mini-audit: are rituals earning their slot? Adjust based on feedback.
8. **End of Quarter 1:** First full Quarterly Ritual Review.
