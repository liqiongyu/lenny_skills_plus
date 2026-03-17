# Weekly Product Review Meeting Pack

## Context

**Problem:** The current weekly product review devolves into status updates, consistently runs over 60 minutes, and fails to produce clear decisions or unblock teams.

**Redesign goal:** Transform the meeting into a decision-focused, timeboxed 60-minute session that reviews metrics, makes 1-2 decisions on experiment results, and surfaces blockers — with all status updates moved to async pre-reads.

---

## 1. Meeting Brief

### Purpose Statement

> Make 1-2 data-informed decisions per week on active experiments and product direction, review key metrics for anomalies, and surface cross-functional blockers that require real-time collaboration to resolve. This meeting does NOT exist for status updates — those happen asynchronously in the pre-read.

### Meeting Metadata

| Field | Detail |
|---|---|
| **Meeting name** | Weekly Product Review |
| **Cadence** | Weekly, same day/time (recommended: Tuesday 10:00-11:00 AM) |
| **Duration** | 60 minutes, hard stop |
| **Location** | Primary conference room + video link for remote participants |
| **Facilitator** | Product Manager (rotates quarterly to Design or Eng lead) |
| **Decision owner** | Product Manager (final call if no consensus reached) |
| **Timekeeper** | Designated rotating role (not the facilitator) |
| **Note-taker** | Designated rotating role (not the facilitator) |

### Attendees (12 persons)

| Role | Name (placeholder) | Responsibility in Meeting |
|---|---|---|
| **Product Manager** (Facilitator) | [Name] | Facilitates, owns decisions, sets agenda priorities |
| **Engineering Lead — Backend** | [Name] | Technical feasibility input, eng blockers |
| **Engineering Lead — Frontend** | [Name] | Technical feasibility input, eng blockers |
| **Engineering Lead — Platform/Infra** | [Name] | Scalability and reliability input |
| **Senior Engineer / Tech Lead** | [Name] | Implementation detail, experiment technical review |
| **Design Lead** | [Name] | UX metrics, design experiment results, user research signals |
| **UX Researcher** | [Name] | Qualitative data, user feedback synthesis |
| **Data/Analytics Lead** | [Name] | Metrics review, experiment statistical analysis |
| **Data Analyst** | [Name] | Dashboard prep, anomaly detection |
| **Marketing Lead** | [Name] | GTM implications of decisions, market signal input |
| **Growth/Product Marketing** | [Name] | Funnel metrics, messaging experiment results |
| **Engineering Manager** | [Name] | Resourcing and capacity input for blocker resolution |

### Standing Rules

1. **No laptops open** except for the note-taker and whoever is presenting a specific slide.
2. **Pre-read is mandatory.** If you haven't read it, you listen — you don't ask clarifying questions that are answered in the pre-read.
3. **"Status" is a banned word.** Any status update that sneaks in gets redirected: "That's great — put it in Slack. What decision do you need from this group?"
4. **Silence = consent.** If a decision is proposed and no one objects within 30 seconds, it's ratified.
5. **Hard stop at 60 minutes.** Unfinished items go to a follow-up async thread or a 1:1, not an extended meeting.

---

## 2. Pre-Read Template

> **Distributed by:** PM (or delegate)
> **Distributed when:** By end of day Monday (24 hours before meeting)
> **Format:** Shared doc (Notion/Google Doc) with comment permissions for all attendees
> **Expected read time:** 10-15 minutes

---

### PRE-READ: Weekly Product Review — Week of [DATE]

#### A. Metrics Dashboard Summary

> **Owner:** Data/Analytics Lead
> **Due to PM:** Monday 12:00 PM

**North Star Metric**

| Metric | This Week | Last Week | WoW Change | 4-Week Trend | Target |
|---|---|---|---|---|---|
| [e.g., Weekly Active Users] | [value] | [value] | [+/- %] | [arrow/sparkline] | [value] |

**Key Product Metrics (Top 5)**

| Metric | This Week | Last Week | WoW Change | Status |
|---|---|---|---|---|
| Activation rate (new users) | | | | On Track / Watch / Off Track |
| Feature adoption — [Feature X] | | | | |
| Retention — Day 7 | | | | |
| NPS / CSAT | | | | |
| Revenue per account (expansion) | | | | |

**Anomaly Alerts** (anything outside 2-sigma or unexpected)

- [ ] **Anomaly 1:** [Description, magnitude, hypothesis for cause]
- [ ] **Anomaly 2:** [Description, magnitude, hypothesis for cause]

> **Attendee action:** Review metrics. Add a comment on any anomaly you have context on. Come prepared to discuss anomalies only — no need to discuss metrics that are on track.

---

#### B. Decision Memo #1

> **Topic:** [e.g., "Ship Experiment X to 100% or Kill"]
> **Decision owner:** [PM name]
> **Author of memo:** [Person who ran the experiment]

**Context** (3-5 sentences max)

[What experiment was run, why, for how long, targeting which segment.]

**Results Summary**

| Variant | Sample Size | Primary Metric | Secondary Metric | Statistical Significance |
|---|---|---|---|---|
| Control | [n] | [value] | [value] | — |
| Variant A | [n] | [value] | [value] | p = [value] |
| Variant B | [n] | [value] | [value] | p = [value] |

**Qualitative Signals** (if any)

- User feedback: [1-2 bullet summary]
- Support ticket trend: [1 bullet]

**Options on the Table**

| Option | Pros | Cons | Effort Estimate |
|---|---|---|---|
| A: Ship to 100% | [bullets] | [bullets] | [T-shirt size] |
| B: Iterate and re-test | [bullets] | [bullets] | [T-shirt size] |
| C: Kill | [bullets] | [bullets] | [T-shirt size] |

**Author's Recommendation:** [Option X], because [1-2 sentence rationale].

> **Attendee action:** Read the memo. Add your position (Support / Oppose / Need Discussion) as a comment before the meeting. If you oppose, state your concern in one sentence.

---

#### C. Decision Memo #2

> [Same template as Decision Memo #1, if applicable for the week]
> If there is no second decision, state: "No second decision this week."

---

#### D. Blockers Board

> **Owner:** Each functional lead adds their own by Monday 3:00 PM

| # | Blocker | Raised By | Blocking What | Cross-Functional Help Needed From | Days Blocked |
|---|---|---|---|---|---|
| 1 | [Description] | [Name/Role] | [Feature/workstream] | [Role/team needed] | [n] |
| 2 | [Description] | [Name/Role] | [Feature/workstream] | [Role/team needed] | [n] |
| 3 | [Description] | [Name/Role] | [Feature/workstream] | [Role/team needed] | [n] |

> **Attendee action:** If you are listed in "Help Needed From," come with a proposed resolution or escalation path.

---

#### E. Parking Lot (from last week)

| Item | Owner | Status |
|---|---|---|
| [Carryover item] | [Name] | [Resolved / Still Open / Escalated] |

---

## 3. Timeboxed Agenda

| Time | Duration | Segment | Owner | Purpose |
|---|---|---|---|---|
| 0:00 - 0:02 | 2 min | **Opening & Ground Rules** | Facilitator (PM) | State purpose, confirm pre-read completion, name timekeeper |
| 0:02 - 0:10 | 8 min | **Metrics Review** | Data Lead | Anomalies only — what's off track and why. No celebrating green metrics. |
| 0:10 - 0:12 | 2 min | **Transition / Questions on Metrics** | Facilitator | Quick clarifying questions only. Deep dives go to async. |
| 0:12 - 0:30 | 18 min | **Decision #1: Experiment Review** | Memo Author + PM | Present recommendation (3 min), discuss (10 min), decide (5 min) |
| 0:30 - 0:32 | 2 min | **Transition / Decision Capture** | Note-taker + Facilitator | Read back the decision aloud, confirm DRI and deadline |
| 0:32 - 0:48 | 16 min | **Decision #2: Experiment Review** | Memo Author + PM | Present recommendation (3 min), discuss (8 min), decide (5 min) |
| 0:48 - 0:50 | 2 min | **Transition / Decision Capture** | Note-taker + Facilitator | Read back the decision aloud, confirm DRI and deadline |
| 0:50 - 0:57 | 7 min | **Blockers Round** | Facilitator (round-robin) | Each blocker: 1 min to state, 1 min to assign resolution owner. No solving in meeting. |
| 0:57 - 1:00 | 3 min | **Recap & Close** | Facilitator | Recap decisions, action items, blockers. Name follow-up owners. Hard stop. |

### Flex Rules

- If there is only 1 decision this week, Decision #2 time converts to extended Blocker Round (up to 18 min) or early end.
- If there are 0 decisions, the meeting can be shortened to 30 minutes (metrics + blockers only) or cancelled with async check-in.
- If a decision cannot be reached in its timebox, the facilitator calls it: "We're moving this to an async decision thread. [Decision Owner] will post a final recommendation by [day]. Silence by EOD = consent."

---

## 4. Facilitation Script with Transition Cues

### 0:00 — Opening (2 min)

> **Facilitator says:**
>
> "Good morning. Welcome to our weekly product review. A reminder: this meeting exists to make decisions, not share updates. If it's in the pre-read, we've all read it.
>
> Today we have: a metrics check, [one/two] decision(s) on the table, and [N] blockers to assign.
>
> [Timekeeper name], you're on the clock. [Note-taker name], you're capturing decisions and actions.
>
> Quick check — has everyone read the pre-read? [Pause for nods.] Great. Let's go."

**If someone hasn't read it:**

> "No problem — please listen and hold questions that are answered in the doc. We'll move on."

---

### 0:02 — Metrics Review (8 min)

> **Facilitator says:**
>
> "[Data Lead name], take us through anomalies only. We're looking for anything off-track that this group needs to be aware of. Green metrics — we skip."

**Transition cue at 8 minutes:**

> "Thank you. Any quick clarifying questions on the metrics? I'll take two. [Pause.] Okay, if there's more to discuss, drop it in the #product-metrics Slack channel and tag [Data Lead]. Moving to decisions."

**If someone starts a deep-dive:**

> "That's a great thread — let's take it offline. [Name], can you and [Data Lead] sync after and share findings in Slack? Moving on."

---

### 0:12 — Decision #1 (18 min)

> **Facilitator says:**
>
> "Decision one: [Topic]. [Memo Author name], you have 3 minutes to present your recommendation. We've all read the memo, so focus on what's changed since you wrote it, or the single strongest argument for your recommendation. Go."

**At 3 minutes (presentation end):**

> "Thanks. Opening for discussion. I saw some pre-read comments — [Name], you flagged a concern about [X]. Let's start there."

**Discussion management cues:**

- If someone repeats a point: "I think we've captured that — [Note-taker], do we have it? Yes. Next perspective."
- If side conversation starts: "Let's keep one conversation. [Name], finish your point."
- If going off-topic: "Interesting, but that's a different decision. Parking lot. Back to [Topic]."
- If stalemate: "I'm hearing two positions: [A] and [B]. Let's do a quick poll. Thumbs up for A, thumbs down for B, sideways for 'can live with either.' [Pause.] Okay, [majority direction] — [Decision Owner], your call."

**At 15 minutes (decision time):**

> "We have 3 minutes. [Decision Owner name], based on the discussion, what's the call?"

**After decision is stated:**

> "[Note-taker], read back the decision."

**Note-taker reads:** "Decision: [Exact decision]. DRI: [Name]. Deadline: [Date]. Any objections? [5-second pause.] Logged."

---

### 0:30 — Transition (2 min)

> **Facilitator says:**
>
> "Good. Decision one is locked. Let's move to decision two."

*(If no Decision #2 this week: "No second decision this week. We're moving to blockers — we have extra time, so let's use it well.")*

---

### 0:32 — Decision #2 (16 min)

> [Same flow as Decision #1, with slightly compressed discussion time: 3 min present, 8 min discuss, 5 min decide.]

**At 0:48:**

> "[Note-taker], read back decision two."

---

### 0:50 — Blockers Round (7 min)

> **Facilitator says:**
>
> "Blockers. We have [N] on the board. We're not solving them here — we're assigning an owner and a resolution deadline. [Name], blocker one — go. You have 60 seconds."

**For each blocker:**

> "[Person who can help], can you own unblocking this? When can [Raiser] expect resolution? [Confirm date.] Logged. Next."

**If someone starts solving in the meeting:**

> "Love the energy — but not now. [Helper name], you and [Raiser name] sync after this meeting. We need a resolution path by [day]. Next blocker."

**If time runs short:**

> "We have [N] blockers remaining. I'm going to ask those to be posted in #product-blockers Slack with an owner tagged. If you're tagged, respond by EOD."

---

### 0:57 — Recap & Close (3 min)

> **Facilitator says:**
>
> "Recap. [Note-taker], give us the three things: decisions made, action items, and blocker owners."

**Note-taker reads the summary aloud.**

> **Facilitator says:**
>
> "Follow-up email goes out within 2 hours. If your name is on an action item, you'll see a deadline. Silence = acknowledgment.
>
> Anything I missed? [5-second pause.] No? We're done. 60 minutes. Thanks, everyone."

**If it's 0:59 and someone raises a new topic:**

> "Great topic — but we're at time. Drop it in Slack or the parking lot for next week. Meeting adjourned."

---

## 5. Notes & Decision Log Template

> **Maintained by:** Note-taker (rotating)
> **Published to:** Shared team workspace (Notion/Confluence) + Slack channel within 1 hour post-meeting

---

### MEETING NOTES: Weekly Product Review — [DATE]

**Attendees present:** [Names]
**Absent:** [Names]
**Facilitator:** [Name] | **Timekeeper:** [Name] | **Note-taker:** [Name]

---

#### Metrics Snapshot

| Metric | Status | Note |
|---|---|---|
| [North Star Metric] | On Track / Watch / Off Track | [1-line note if anomaly discussed] |
| [Other anomaly discussed] | | |

**Follow-up needed:** [Any async investigation assigned, with owner]

---

#### Decision Log

| # | Decision | Rationale (1 sentence) | DRI | Deadline | Dissent Noted |
|---|---|---|---|---|---|
| D-[YYYY-WW]-01 | [Exact decision statement] | [Why this option was chosen] | [Name] | [Date] | [None / Name: concern] |
| D-[YYYY-WW]-02 | [Exact decision statement] | [Why this option was chosen] | [Name] | [Date] | [None / Name: concern] |

> **Decision numbering convention:** D-[Year]-[Week Number]-[Sequence]. Example: D-2026-12-01 is the first decision of week 12, 2026. This creates a searchable, traceable log.

---

#### Action Items

| # | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| A-[YYYY-WW]-01 | [Specific action] | [Name] | [Date] | Open |
| A-[YYYY-WW]-02 | [Specific action] | [Name] | [Date] | Open |
| A-[YYYY-WW]-03 | [Specific action] | [Name] | [Date] | Open |

---

#### Blockers Addressed

| Blocker | Resolution Owner | Resolution Deadline | Resolution Path |
|---|---|---|---|
| [Description] | [Name] | [Date] | [1-line: what they'll do] |

---

#### Parking Lot (for next week or async)

| Item | Raised By | Suggested Forum |
|---|---|---|
| [Topic] | [Name] | Next week's review / Async thread / Separate meeting |

---

#### Meeting Health Check (Facilitator fills post-meeting)

| Dimension | Rating (1-5) | Note |
|---|---|---|
| Stayed on time | | |
| Pre-reads were read | | |
| Decisions were made (not deferred) | | |
| Discussion quality (diverse input, not groupthink) | | |
| Energy/engagement | | |

---

## 6. Follow-Up Email Template

> **Sent by:** PM (or Note-taker by delegation)
> **Sent to:** All attendees + any stakeholders on the CC list
> **Sent when:** Within 2 hours of meeting end
> **Subject line format:** `[Product Review W[##]] Decisions: [1-line summary] | [N] Action Items`

---

**Subject:** [Product Review W12] Decisions: Ship Experiment X to 100%, Kill Experiment Y | 5 Action Items

---

Hi team,

Here's the summary from today's Weekly Product Review (Tuesday, [Date]).

### Decisions Made

**Decision 1: [Title]**
- **Decision:** [Exact decision statement in one sentence.]
- **Rationale:** [One sentence on why.]
- **DRI:** [Name]
- **Deadline:** [Date]
- **Dissent noted:** [None / Name raised concern about X — logged for monitoring.]

**Decision 2: [Title]**
- **Decision:** [Exact decision statement in one sentence.]
- **Rationale:** [One sentence on why.]
- **DRI:** [Name]
- **Deadline:** [Date]
- **Dissent noted:** [None / Name raised concern about X.]

### Action Items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | [Specific, verb-started action] | [Name] | [Date] |
| 2 | [Specific, verb-started action] | [Name] | [Date] |
| 3 | [Specific, verb-started action] | [Name] | [Date] |
| 4 | [Specific, verb-started action] | [Name] | [Date] |
| 5 | [Specific, verb-started action] | [Name] | [Date] |

> If your name is listed above and the action or deadline doesn't look right, reply to this email by EOD today. **Silence = acknowledgment.**

### Blockers Update

| Blocker | Owner | Expected Resolution |
|---|---|---|
| [Description] | [Name] | [Date] |

### Metrics Watch Items

- [Anomaly 1]: [Name] investigating, update expected by [Date].
- [Anomaly 2]: Resolved — [1-line explanation].

### Parking Lot (Carried to Next Week)

- [Topic] — [Name] to prepare async write-up by [Date]

---

Full meeting notes: [Link to Notion/Confluence page]

Next week's pre-read will be distributed by Monday EOD. If you have a decision to bring to next week's review, submit your Decision Memo draft to [PM name] by Friday EOD.

Best,
[PM Name]

---

## Appendix: Implementation Playbook

### How to Roll This Out

**Week 0 — Setup (before first meeting)**
1. Share this Meeting Pack with all 12 attendees. Tell them: "We're redesigning our weekly review. Read the Meeting Brief and Pre-Read Template. This is how we operate starting next week."
2. Create the shared pre-read document in your team workspace.
3. Set up the decision log as a running document (append-only, never delete).
4. Assign the first week's Timekeeper and Note-taker.
5. Book the meeting for 55 minutes (not 60) in the calendar to give people a 5-minute buffer before their next meeting.

**Week 1 — First Meeting**
- Facilitator reads the Opening script verbatim. It will feel formal. That's intentional — you're resetting norms.
- Be strict on timeboxes. End early if you finish early. Ending early teaches the team that this meeting respects their time.
- If someone gives a status update, redirect with: "Thanks — that's an update, not a decision. Where does this group need to weigh in?"

**Weeks 2-4 — Calibration**
- Use the Meeting Health Check after each session. If "Pre-reads were read" scores below 3 for two consecutive weeks, address it directly: "We can't make good decisions without preparation. What's blocking people from reading?"
- Adjust the timebox allocations based on reality. If you consistently have only 1 decision, shorten the meeting to 45 minutes.

**Month 2+ — Maintenance**
- Rotate the facilitator role quarterly to prevent PM from becoming a bottleneck.
- Review the decision log monthly. Are decisions sticking? Are deadlines being met? If not, the meeting has a downstream execution problem, not a meeting problem.
- Every quarter, ask: "Should this meeting still exist in this form?" Kill it or evolve it.

### Common Failure Modes and Fixes

| Failure Mode | Symptom | Fix |
|---|---|---|
| Status updates creep back in | Meeting runs over; low decision count | Facilitator interrupts immediately. Post a visible "NO STATUS UPDATES" sign. |
| Pre-reads aren't read | Clarifying questions that are answered in the doc | Name the offenders kindly: "That's in the pre-read, page 2." Peer pressure works. |
| Decisions get re-litigated | Same topic appears in multiple weeks | Point to the decision log: "We decided this in W10. What new information has emerged?" |
| One person dominates discussion | Others disengage | Facilitator calls on quiet people: "[Name], you haven't weighed in — what's your read?" |
| Blockers aren't actually unblocked | Same blockers appear week after week | Escalate: "This has been blocked for 3 weeks. We're escalating to [VP/exec] today." |
| Meeting feels rushed | Important decisions feel jammed | Reduce to 1 decision per week. Use the other slot for a deeper discussion on one strategic topic. |
| Low attendance | People skip or send proxies | Reduce attendee list. If someone doesn't need to be in every decision, make them optional and tag them only for relevant weeks. |

---

*This Meeting Pack is a living document. Review and update it quarterly based on what's working and what isn't.*
