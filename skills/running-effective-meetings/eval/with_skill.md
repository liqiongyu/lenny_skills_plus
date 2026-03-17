# Meeting Pack: Weekly Product Review

> Produced using the `running-effective-meetings` skill pack.

---

## Workflow Trace

### Step 1 -- Decide if a meeting is needed and pick the format

**Is a meeting needed?** Yes. The team needs real-time discussion on experiment results and trade-offs, cross-functional input on blockers, and fast decision-making on what to ship/kill/extend. These cannot happen asynchronously because they require live debate across PM, Eng, Design, Data, and Marketing.

**What will be different after this meeting?** Each week, the team will leave with (a) a shared view of product health via metrics, (b) 1-2 explicit decisions on experiment results (ship / kill / extend), and (c) named owners for every blocker with a resolution deadline.

**Meeting type:** Hybrid -- Operational (metrics review, blockers) + Decision (experiment calls). Because the current meeting devolves into status updates, the redesign must strictly separate "Discover" (async) from "Discuss + Decide" (live). The format is a **Decision-focused operational meeting** -- structured timekeeping with explicit decision points.

**Current diagnosis:** The meeting is a textbook "status meeting in disguise" (Anti-pattern #1) compounded by "no pre-read" (Anti-pattern #2) and "missing decision capture" (Anti-pattern #4). The fix is to move all status and context to a mandatory pre-read and reserve live time for discussion and decisions only.

### Step 2 -- Define the discussion scope (in-room vs. async)

| Phase | What happens | Where |
|---|---|---|
| **Discover** | Metrics dashboard, experiment data, blocker status, decision memos | Async pre-read (sent 24h before) |
| **Discuss** | Debate experiment results, trade-offs, blocker resolution options | Live meeting (40 min of 60) |
| **Decide** | Ship/kill/extend calls on experiments; blocker owners + deadlines | Live meeting, captured in real time |

**Pre-read outline:**
- Metrics snapshot (5 key KPIs with WoW trends)
- Decision memo per experiment up for review (max 2 per week)
- Blocker log with proposed resolutions

**Discussion questions for the live meeting:**
1. Which experiment results are conclusive enough to act on this week?
2. For borderline results, what additional evidence would change our minds?
3. Which blockers require cross-functional negotiation (not just assignment)?

**Decision statements:**
- "We will ship / kill / extend experiment X based on the data reviewed."
- "Blocker Y is assigned to [Owner] with resolution by [Date]."

**Check:** 40 of 60 minutes (67%) are reserved for discussion and decisions. Passes the 60% threshold.

### Step 3 -- Prime participants (pre-work + pre-read)

See the full **Pre-Read Template** in Section 2 below. It is sent every Monday by 10:00 AM (24 hours before the Tuesday meeting).

**Pre-work assignments:**
- **Data lead:** Update the metrics dashboard and flag anomalies by Monday 10 AM.
- **PM (experiment owner):** Write a 1-page decision memo per experiment up for review (using the template below) by Monday 10 AM.
- **Eng leads:** Update the blocker log with current status and proposed resolutions by Monday noon.
- **All attendees:** Read the pre-read and add async comments/questions in the shared doc by Monday 5 PM.
- **Design / Marketing:** Flag any downstream impacts of pending decisions via comments.

**Check:** Every attendee can arrive ready to discuss. No live info dump is needed.

### Step 4 -- Build a timed agenda

See the full **Timed Agenda** in Section 3 below. Key design rules applied:
- 3 topics max (metrics, experiments, blockers)
- Every segment has an explicit expected output
- Discussion time is 40 of 60 minutes
- Deep-dive off-ramp: any topic needing 10+ minutes of additional debate is parked and scheduled as a 30-minute follow-up with the relevant subset

### Step 5 -- Assign roles and write the facilitation script

See the full **Facilitation Script** in Section 4 below. Roles are named; escalation path is defined.

### Step 6 -- Run the meeting and capture decisions/actions

See the **Notes + Decision Log Template** in Section 5 below. This is used live during the meeting.

### Step 7 -- Close, follow up, and improve meeting hygiene

See the **Follow-Up Email Template** in Section 6 below. Hygiene recommendations are in Section 8.

---

## Section 1: Meeting Brief

**Title:** Weekly Product Review
**Cadence:** Every Tuesday, 10:00-11:00 AM (recurring)
**Meeting type:** Decision-focused operational meeting
**Remote/hybrid:** Remote-first (Zoom); hybrid-compatible with shared screen + collaborative doc

**Objective (what changes after):**
The team has a shared, up-to-date view of product health, has made 1-2 explicit decisions on active experiments (ship / kill / extend), and has assigned owners to every cross-functional blocker with a resolution deadline.

**Desired outputs:**
1. Metrics health check -- confirmed understanding of product trajectory (no surprises)
2. Decision record for each experiment reviewed (ship / kill / extend + rationale)
3. Blocker resolution plan with named owners and deadlines
4. Parking lot items routed to the right forum

**Decision(s) to be made:**
| Decision | Decision owner | Deadline |
|---|---|---|
| Ship / kill / extend Experiment A | Head of Product (PM lead) | End of meeting |
| Ship / kill / extend Experiment B | Head of Product (PM lead) | End of meeting |
| Blocker resolution assignments | Relevant Eng lead or PM | End of meeting |

**Attendees + roles (12 people):**

| Role | Person | Meeting responsibility |
|---|---|---|
| **Facilitator** | PM Lead (rotating monthly) | Run agenda, keep time, manage discussion |
| **Decision owner** | Head of Product | Final call on experiment decisions |
| **Note-taker** | Rotates weekly (assign in calendar invite) | Live capture in shared doc |
| **Timekeeper** | Design Lead (or designate) | Call out time warnings at 2-min and 0-min marks |
| Eng Lead -- Backend | [Name] | Input on feasibility, blockers |
| Eng Lead -- Frontend | [Name] | Input on feasibility, blockers |
| Eng Lead -- Platform | [Name] | Input on infrastructure blockers |
| Senior Designer | [Name] | Input on UX impact of experiment decisions |
| Data Lead | [Name] | Present metrics, answer data questions |
| Marketing Lead | [Name] | Input on GTM timing, messaging implications |
| PM -- Growth | [Name] | Input on growth experiments, funnel impact |
| PM -- Core Product | [Name] | Input on core feature experiments |

**Pre-work (async -- due Monday 5 PM):**
- **Read:** Pre-read doc (metrics dashboard + decision memos + blocker log)
- **Comment on:** Flag questions, risks, or disagreements in the shared doc
- **Bring:** Your recommendation on each experiment (ship / kill / extend) and why

**Constraints:**
- Time box: 60 minutes hard stop (no overruns)
- Must-avoid behaviors: Round-robin status updates, live data exploration, re-reading the pre-read aloud, opening new topics not in the pre-read
- Ground rule: If you haven't read the pre-read, you listen -- you don't ask context questions that are answered in the doc

---

## Section 2: Pre-Read Template

> **Instructions:** This template is populated each week and shared as a Google Doc (or Notion page) by Monday 10:00 AM. All attendees must read and add comments by Monday 5:00 PM.

---

### Weekly Product Review Pre-Read -- Week of [DATE]

**Read time:** ~10 minutes
**Action required:** Read, comment with questions/disagreements, come with your recommendation on each experiment.

---

#### Part A: Metrics Dashboard (Data Lead fills in by Monday 10 AM)

| KPI | This week | Last week | WoW change | 4-week trend | Status |
|---|---|---|---|---|---|
| Weekly Active Users (WAU) | | | | | On track / Watch / Alert |
| Activation rate (new users) | | | | | On track / Watch / Alert |
| Revenue (MRR) | | | | | On track / Watch / Alert |
| Retention (Week-4 cohort) | | | | | On track / Watch / Alert |
| NPS / CSAT | | | | | On track / Watch / Alert |

**Data Lead commentary (3 bullets max):**
1. [Notable movement and likely cause]
2. [Notable movement and likely cause]
3. [Anything that needs discussion]

**Questions for the team (if any):**
- [Data Lead flags anything that needs cross-functional input]

---

#### Part B: Experiment Decision Memos (PM fills in per experiment -- max 2)

##### Experiment 1: [NAME]

| Field | Detail |
|---|---|
| **Hypothesis** | [What we believed would happen] |
| **Key metric** | [Primary success metric] |
| **Duration** | [Start date -- end date; N weeks] |
| **Sample size** | [N users per variant] |
| **Statistical significance** | [Yes/No; p-value or confidence interval] |

**Results summary (3 bullets):**
1. [Primary metric result vs. goal]
2. [Secondary metric result]
3. [Unexpected finding or caveat]

**Options:**
| Option | Description | Pros | Cons / Risks |
|---|---|---|---|
| **Ship** | Roll out to 100% | [List] | [List] |
| **Kill** | Revert to control | [List] | [List] |
| **Extend** | Run N more weeks with [change] | [List] | [List] |

**PM recommendation:** [Ship / Kill / Extend] because [1-sentence rationale].
**What would change my mind:** [Specific evidence or argument].

##### Experiment 2: [NAME]

[Same structure as Experiment 1]

---

#### Part C: Blocker Log (Eng Leads update by Monday noon)

| # | Blocker | Owner | Status | Proposed resolution | Cross-functional input needed? |
|---|---|---|---|---|---|
| 1 | | | Open / In progress / Resolved | | Yes (from whom) / No |
| 2 | | | | | |
| 3 | | | | | |

---

#### Part D: Async Comment Section

> **All attendees:** Add your questions, disagreements, or flags below by Monday 5 PM. Tag the relevant person.

- [Name]: [Comment]
- [Name]: [Comment]

---

## Section 3: Timed Agenda

**Meeting:** Weekly Product Review
**Duration:** 60 minutes (hard stop)
**Rule:** No status updates. If it's in the pre-read, don't repeat it. Discuss, decide, move.

| Time | Min | Segment | Lead | Format | Expected output |
|---:|---:|---|---|---|---|
| 0:00-0:03 | 3 | **Priming** -- state objective, mode, decision rights, ground rules | Facilitator | Script (read aloud) | Shared understanding of why we're here and how we'll operate |
| 0:03-0:10 | 7 | **Metrics check** -- Data Lead highlights only anomalies and items needing discussion (no full readout) | Data Lead | Verbal + screen share | Confirmed: metrics are healthy OR flagged items requiring action |
| 0:10-0:15 | 5 | **Metrics Q&A** -- clarifying questions only (not problem-solving) | Facilitator | Open Q&A | Outstanding data questions resolved; problem-solving items parked |
| 0:15-0:30 | 15 | **Experiment 1 discussion** -- PM presents recommendation (1 min), then open debate on trade-offs | PM (experiment owner) | Structured discussion | Trade-offs surfaced; objections heard |
| 0:30-0:33 | 3 | **Experiment 1 decision** -- Decision owner makes the call | Decision owner | Decide | Decision recorded: ship / kill / extend + rationale |
| 0:33-0:45 | 12 | **Experiment 2 discussion** -- same structure | PM (experiment owner) | Structured discussion | Trade-offs surfaced; objections heard |
| 0:45-0:48 | 3 | **Experiment 2 decision** -- Decision owner makes the call | Decision owner | Decide | Decision recorded: ship / kill / extend + rationale |
| 0:48-0:55 | 7 | **Blockers** -- only blockers requiring cross-functional negotiation (pre-filtered from log) | Eng Lead(s) | Discussion + assign | Each blocker has an owner + deadline OR is escalated |
| 0:55-0:60 | 5 | **Close-out** -- 3 questions + parking lot + hygiene | Facilitator | Confirm | Written: decisions, actions, who-else-needs-to-know |

**Total discussion + decision time:** 45 minutes (75% of meeting). **Total context-setting:** 15 minutes (25%). Exceeds 60% discussion threshold.

**Deep-dive off-ramp rule:** If any topic needs more than its timebox, the facilitator says: "We're at time. Let's capture what we know, park the rest, and schedule a 30-minute deep dive with [relevant subset] by [date]." This is non-negotiable.

---

## Section 4: Facilitation Script

### Opening -- Priming (0:00-0:03)

> **Facilitator reads aloud:**
>
> "Good morning. Welcome to the Weekly Product Review. Let me set the frame for today.
>
> **Objective:** We're here to do three things: (1) confirm our metrics are healthy or flag what's not, (2) make ship/kill/extend decisions on [Experiment A] and [Experiment B], and (3) resolve any cross-functional blockers.
>
> **Meeting type:** This is a decision-focused meeting. We are not here for status updates -- those are in the pre-read.
>
> **Decision rights:** [Head of Product] is the decision owner for experiment calls today. They will make the final call after hearing your input.
>
> **Mode:** We're optimizing for tactical efficiency. Short, direct input. Disagree openly now so we don't relitigate later.
>
> **Ground rules:**
> - If it's in the pre-read, don't repeat it. Reference it by section.
> - We timebox every segment. When I call time, we move on or park it.
> - [Note-taker] is capturing decisions and actions live in the shared doc. Speak clearly.
> - New topics go to the parking lot -- we don't add agenda items mid-meeting.
>
> **Check:** Has everyone read the pre-read? [Pause.] Good. Let's go."

### Transition: Priming to Metrics Check (0:03)

> **Facilitator:** "[Data Lead], you have 7 minutes. Highlight only what moved significantly or needs team discussion. Skip anything that's on track."

### Metrics Check (0:03-0:10)

Data Lead shares screen with dashboard. Talks through anomalies only.

**If Data Lead starts reading every row:**
> **Facilitator:** "We can see the green rows. Focus us on the yellows and reds -- what needs our attention?"

### Transition: Metrics Check to Q&A (0:10)

> **Facilitator:** "Thanks, [Data Lead]. Quick clarifying questions only -- if something needs problem-solving, we'll park it. You have 5 minutes."

### Metrics Q&A (0:10-0:15)

**If someone starts problem-solving:**
> **Facilitator:** "That's a great question but it's a deep dive. Let me add it to the parking lot. [Note-taker], capture that. Let's stay with clarifying questions."

### Transition: Metrics to Experiment 1 (0:15)

> **Facilitator:** "Good. Metrics are [healthy / flagged -- we'll address the flag in the parking lot]. Now to decisions. [PM], you have 1 minute to state your recommendation for [Experiment 1], then we'll open for discussion. Remember: the data is in the pre-read. Just give us your call and your top reason."

### Experiment 1 Discussion (0:15-0:30)

PM states recommendation (1 minute). Facilitator opens discussion.

**Prompts to draw out dissent:**
> - "Who disagrees with the recommendation? What's your strongest counter-argument?"
> - "What are we assuming that might be false?"
> - "If we ship this and it fails, what's the most likely reason?"
> - "[Marketing], any GTM timing concerns? [Eng], any technical debt implications?"

**If discussion stalls or circles:**
> **Facilitator:** "I'm hearing two camps: [A] and [B]. The trade-off is [X]. [Decision owner], do you have enough input to decide, or do you need one more specific piece of evidence?"

**If someone introduces new data not in the pre-read:**
> **Facilitator:** "That's new information. Can you drop it in the doc right now? [Decision owner], does this change your thinking enough to defer, or can we decide with what we have?"

### Transition: Experiment 1 Decision (0:30)

> **Facilitator:** "Time check: we're at 30 minutes. [Decision owner], you've heard the input. What's the call on [Experiment 1]?"

### Experiment 1 Decision Capture (0:30-0:33)

Decision owner states the decision. Facilitator confirms.

> **Facilitator:** "[Note-taker], please read back the decision."
>
> **Note-taker:** "Decision: [Ship/Kill/Extend] [Experiment 1]. Rationale: [1 sentence]. Owner for follow-up: [Name]. Deadline: [Date]."
>
> **Facilitator:** "[Decision owner], is that accurate? Good. Moving on."

### Experiment 2 Discussion + Decision (0:33-0:48)

Same structure as Experiment 1. 12 minutes discussion + 3 minutes decision.

### Transition: Experiments to Blockers (0:48)

> **Facilitator:** "Two decisions made. Nice work. Now blockers. [Eng Lead], which blockers from the log need cross-functional help? Skip anything you can resolve within Eng. You have 7 minutes."

### Blockers (0:48-0:55)

**Format:** Eng Lead names the blocker, proposed resolution, and what they need from another function. The relevant person responds. Facilitator captures owner + deadline.

**If a blocker becomes a deep dive:**
> **Facilitator:** "This needs more than 2 minutes. [Name] and [Name], can you schedule a 30-minute session this week? [Note-taker], capture the blocker, the two owners, and a deadline for the follow-up meeting."

### Close-Out (0:55-1:00)

> **Facilitator:** "We're at 55 minutes. Let's close. Three questions.
>
> **Question 1: What did we decide?**
> [Note-taker reads back the decisions from the log.]
>
> **Question 2: Who does what by when?**
> [Note-taker reads back action items.]
>
> **Question 3: Who else needs to know?**
> [Facilitator asks:] 'Do any of these decisions affect teams not in this room -- Sales, Support, Customer Success, Leadership? Who's responsible for informing them?'
>
> **Parking lot review:** We parked [N] items. [Facilitator assigns each parked item to an owner for follow-up or routes to the right meeting.]
>
> **Hygiene check (monthly):** 'Last item -- once a month I'll ask: is this meeting still earning its 60 minutes? Anything we should change? [Pause for 15 seconds.] Okay, we're done. Thanks everyone.'"

---

## Section 5: Notes + Decision Log Template

> **Instructions:** This is a live shared document (Google Doc or Notion). The note-taker fills it in during the meeting. It becomes the permanent record.

---

### Weekly Product Review Notes -- [DATE]

**Attendees:** [List names or note absences]
**Facilitator:** [Name] | **Decision owner:** [Name] | **Note-taker:** [Name] | **Timekeeper:** [Name]

---

#### Meeting summary (3 bullets)

1. [Most important decision or outcome]
2. [Second most important decision or outcome]
3. [Key blocker resolved or escalated]

---

#### Metrics Health Check

| KPI | Status | Notes |
|---|---|---|
| WAU | On track / Watch / Alert | |
| Activation rate | | |
| Revenue (MRR) | | |
| Retention (Week-4) | | |
| NPS / CSAT | | |

**Flagged items requiring follow-up:**
- [Item]: [Owner] will [action] by [date]

---

#### Decisions

| # | Decision | Options considered | Rationale | Decision owner | Date | Status |
|---|---|---|---|---|---|---|
| 1 | [Ship / Kill / Extend] [Experiment name] | Ship, Kill, Extend | [1-2 sentence rationale] | [Name] | [Date] | Decided |
| 2 | [Ship / Kill / Extend] [Experiment name] | Ship, Kill, Extend | [1-2 sentence rationale] | [Name] | [Date] | Decided |
| 3 | [Blocker resolution decision, if any] | | | [Name] | [Date] | Decided / Deferred |

---

#### Action Items

| # | Action | Owner | Due date | Notes / Dependencies |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

#### Parking Lot

| # | Topic | Raised by | Routed to | Follow-up owner | Follow-up deadline |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

---

#### Async Follow-ups Needed

| Who needs to know | What they need to know | Who informs them | By when |
|---|---|---|---|
| | | | |
| | | | |

---

## Section 6: Follow-Up Email Template

> **Instructions:** Sent by the note-taker (or facilitator) within 4 hours of the meeting. Keep it scannable.

---

**To:** [All attendees + stakeholders who need to know]
**Subject:** [Product Review] Decisions + Actions -- Week of [DATE]

Hi team,

Here's the summary from today's Weekly Product Review. Full notes and decision log: [LINK TO SHARED DOC]

### Decisions Made

1. **[Experiment 1 name]: [SHIP / KILL / EXTEND]**
   - Rationale: [1 sentence]
   - Follow-up owner: [Name] -- [specific next step] by [date]

2. **[Experiment 2 name]: [SHIP / KILL / EXTEND]**
   - Rationale: [1 sentence]
   - Follow-up owner: [Name] -- [specific next step] by [date]

### Action Items

| Action | Owner | Due |
|---|---|---|
| [Action 1] | [Name] | [Date] |
| [Action 2] | [Name] | [Date] |
| [Action 3] | [Name] | [Date] |
| [Action 4] | [Name] | [Date] |

### Blockers Resolved / Escalated

- **[Blocker 1]:** [Resolution or escalation path]. Owner: [Name]. Deadline: [Date].
- **[Blocker 2]:** [Resolution or escalation path]. Owner: [Name]. Deadline: [Date].

### Who Else Needs to Know

- [Name] will inform [Sales / Support / Leadership / etc.] about [decision] by [date].

### Parking Lot (Scheduled for Follow-Up)

- [Topic]: [Owner] scheduling a 30-min deep dive with [Names] by [date].

---

Next Product Review: [Day, Date, Time]. Pre-read due: [Day, Date, Time].

Thanks,
[Facilitator / Note-taker name]

---

## Section 7: Risks, Open Questions, and Next Steps

### Risks

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **Pre-read compliance drops off.** People stop reading the pre-read and context questions resurface in the live meeting, eating into discussion time. | Medium | High -- meeting reverts to status-in-disguise | Facilitator enforces the ground rule: "If it's in the pre-read, we skip your question." After 2 weeks of non-compliance, the team lead addresses it directly. |
| 2 | **Meeting creep.** Over time, additional agenda items get added ("just one more thing") and the meeting expands back to 75-90 minutes. | Medium | Medium -- erodes trust in the format | Facilitator holds the hard stop at 60 minutes. Any overflow goes to parking lot. Monthly hygiene check reviews whether the meeting is staying on scope. |
| 3 | **Decision owner is absent.** If the Head of Product is out, experiment decisions may be deferred, creating a backlog. | Low | High -- decisions pile up | Designate a standing delegate (PM Lead or VP Eng) with pre-authorized decision rights when the primary decision owner is unavailable. |
| 4 | **Too few experiments some weeks.** If no experiments are ready for review, 30 minutes of the agenda is empty. | Low | Low -- wasted time | Facilitator repurposes experiment time for a deeper metrics discussion or a forward-looking topic from the parking lot. If there are no decisions to make, shorten the meeting to 30 minutes that week. |
| 5 | **12 people is too many for real discussion.** Cross-functional representation is valuable but 12 voices may mean some people never speak. | Medium | Medium -- silent participants disengage | Rotate "required" vs. "optional" attendees based on the week's experiments. Aim for 7-8 required + 4-5 optional (attend only if experiments touch their area). |

### Open Questions

1. **Who is the first note-taker?** The rotation needs to be seeded with a first volunteer and a published schedule.
2. **Where does the shared doc live?** Confirm whether the team uses Google Docs, Notion, or Confluence. The templates above are format-agnostic but the doc needs a persistent home and a consistent URL.
3. **What is the experiment review cadence?** Are there always 2 experiments per week, or does this vary? If variable, the facilitator needs a rule for how to fill or shorten the agenda.
4. **Should the meeting be recorded?** Remote-first teams often record for async catch-up, but this can reduce candor. Decide as a team.
5. **Integration with sprint planning:** If the team runs sprints, how does the Tuesday Product Review relate to sprint ceremonies? Ensure experiment decisions flow into sprint planning without creating a separate status sync.

### Next Steps

| # | Action | Owner | Deadline |
|---|---|---|---|
| 1 | Circulate this Meeting Pack to all 12 attendees for feedback | PM Lead (Facilitator) | This week |
| 2 | Set up the recurring calendar invite with the agenda and pre-read template link in the description | PM Lead | This week |
| 3 | Create the shared doc (metrics dashboard + decision memo + blocker log + notes template) in the team's doc tool | Data Lead + PM Lead | This week |
| 4 | Publish the note-taker rotation schedule (12-week rotation) | PM Lead | This week |
| 5 | Run the first meeting using this pack | PM Lead (Facilitator) | Next Tuesday |
| 6 | After the first meeting, do a 5-minute retro: "What worked? What to change?" | Facilitator | Next Tuesday (end of meeting or async) |
| 7 | After 4 weeks, conduct a hygiene audit: keep / shorten / split / kill? | PM Lead | 4 weeks from launch |

---

## Section 8: Meeting Hygiene Recommendations

Based on the diagnosis that the current meeting devolves into status updates and runs over, here are specific, actionable changes:

1. **Kill the status round-robin.** Move all status updates to the async pre-read. The live meeting starts with discussion, not reporting. This alone should recover 20-25 minutes per week.

2. **Enforce the hard stop.** The meeting ends at 60 minutes. No exceptions. The facilitator gives a 5-minute warning at 0:55 and starts the close-out script. Overruns signal agenda bloat, not insufficient time.

3. **Cap experiments at 2 per week.** If more experiments need review, prioritize by decision urgency. The rest go to next week or to a dedicated async decision doc.

4. **Separate strategy from operations.** If strategic topics keep surfacing (roadmap direction, market positioning, competitive response), do not let them colonize this meeting. Schedule a separate monthly 90-minute strategic discussion with a smaller group (PM leads, Head of Product, Eng leads).

5. **Shrink the invite when possible.** 12 people is the ceiling, not the floor. Each week, mark attendees as "Required" (those whose input is needed for this week's experiments/blockers) or "Optional" (those who should read the follow-up but don't need to be live). Target 7-8 required.

6. **Monthly hygiene retro.** On the first Tuesday of each month, add 5 minutes at the end for: "Is this meeting still earning 60 minutes of 12 people's time? What should change?" Make one concrete improvement per month.

---

## Quality Gate: Rubric Self-Assessment

| # | Dimension | Score | Evidence |
|---|---|---|---|
| 1 | Objective clarity | **2** | Objective is specific: "shared metrics view + 1-2 experiment decisions + blocker owners with deadlines." You can answer "what will be different after this meeting?" in one sentence. |
| 2 | Right meeting format | **2** | Decision-focused operational format chosen; status-in-disguise explicitly eliminated; operational and strategic are separated. |
| 3 | Discover/Discuss/Decide separation | **2** | Pre-read covers all discovery (metrics, experiment data, blockers). 67-75% of live time is discussion + decision. Decisions are captured explicitly with rationale. |
| 4 | Pre-read quality | **2** | Pre-read includes metrics dashboard, structured decision memos with options/pros/cons/recommendation, blocker log, and async comment section. Attendees can arrive ready to discuss. |
| 5 | Agenda quality | **2** | Timed agenda with 3 topics, each segment has an explicit expected output, discussion time is 75% of the meeting, deep-dive off-ramp rule is defined. |
| 6 | Facilitation readiness | **2** | All 4 roles assigned (facilitator, decision owner, note-taker, timekeeper). Full facilitation script with priming, transition cues, discussion prompts, "if stuck" branches, and close-out questions. |
| 7 | Decision/action capture | **2** | Decision log template with options considered, rationale, owner, date, and status. Action items table with owner and due date. Both are filled live. |
| 8 | Close-out alignment | **2** | Close-out script explicitly asks all 3 questions: what did we decide, who does what by when, who else needs to know. Note-taker reads back decisions. |
| 9 | Follow-up quality | **2** | Follow-up email template sent within 4 hours with decisions, actions, blockers, stakeholders to inform, and link to full notes. |
| 10 | Hygiene improvements | **2** | 6 specific, actionable hygiene recommendations: kill status round-robin, enforce hard stop, cap experiments, separate strategy, shrink invite, monthly hygiene retro. |
| | **Total** | **20/20** | |

**Passing bar: 16/20. Score: 20/20. Pass.**

---

## Checklist Verification

### A) "Is a meeting needed?" checklist
- [x] The goal requires real-time discussion (experiment trade-offs, blocker negotiation).
- [x] The decision owner (Head of Product) will attend.
- [x] There is a draft pre-read with shared context (metrics + decision memos).
- [x] The meeting has clear primary outputs (decisions + blocker resolutions).
- [x] Attendees are the minimum set needed to discuss and act (12 cross-functional, with optional attendance recommended).

### B) Pre-meeting checklist
- [x] Meeting brief completed (objective, type, outputs, roles).
- [x] Pre-read template created with 24h lead time.
- [x] Agenda is timed; 3 topics max.
- [x] Roles assigned: facilitator, decision owner, note-taker, timekeeper.
- [x] Deep dive off-ramp defined (parking lot + follow-up scheduling).

### C) In-meeting facilitation checklist
- [x] Priming script written (objective, mode, decision rights, ground rules).
- [x] Discussion prompts and "if stuck" branches included.
- [x] Live capture in notes template.
- [x] Timebox enforcement with transition cues.
- [x] Escalation path: facilitator summarizes trade-offs, asks decision owner to choose.

### D) Close-out checklist
- [x] "What did we decide?" -- note-taker reads back.
- [x] "Who does what by when?" -- action items with owners + due dates.
- [x] "Who else needs to know?" -- stakeholders named + inform-owner assigned.
- [x] Open questions recorded with owner and plan.

### E) Post-meeting checklist
- [x] Follow-up email template with 4-hour target.
- [x] Decision log with rationale.
- [x] Action items table ready for tracker entry.
- [x] Hygiene recommendations: keep/kill/shorten/split guidance provided.
