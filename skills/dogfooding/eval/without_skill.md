# Dogfooding Sprint Plan: AI Meeting Notes Tool

## Product Context

**Product:** AI-powered meeting notes tool for remote teams
**Core Workflow:** Join meeting → Auto-record → Generate summary → Extract action items → Share to Slack/Notion
**Sprint Duration:** 2 weeks (10 business days)
**Team:** 8-person product team
**Environment:** Production app, real internal meetings, live Slack and Notion integrations

---

## 1. Scenario Map

### 1.1 Meeting Types Covered

| Meeting Type | Frequency | Typical Duration | Participants | Key Outputs |
|---|---|---|---|---|
| Daily Standup | Daily (10×) | 15 min | 8 people | Status updates, blockers, commitments |
| 1:1 Meetings | 2×/week per PM | 30 min | 2 people | Feedback, career items, private action items |
| Sprint Planning | 1×/week | 60 min | 8 people | Sprint backlog, story assignments, estimates |
| Product Review | 1×/week | 45 min | 8 people + stakeholders | Demo notes, feedback, decisions |
| Ad-hoc / Brainstorm | ~3×/week | 30–60 min | 2–5 people | Ideas, rough decisions, follow-ups |
| Stakeholder Sync | 1×/week per PM | 30 min | 2–4 people | Status, risks, requests |

### 1.2 Scenario Stress Tests

Each scenario is designed to push a specific edge of the product:

| # | Scenario | What It Tests | Success Criteria |
|---|---|---|---|
| S1 | 15-min standup with 8 speakers | Speaker identification at scale, brevity of summary | Each speaker's update captured; summary ≤ 200 words |
| S2 | 1:1 with sensitive HR/performance topic | Privacy controls, ability to redact or mark confidential | Confidential flag respected; summary not auto-shared |
| S3 | 60-min planning session with screen-share | Long-form capture, technical term accuracy | All user stories referenced are captured; action items assigned to correct owners |
| S4 | Meeting where someone joins 10 min late | Handling of partial attendance, late-join audio sync | Late joiner's contributions captured; no "unknown speaker" labels |
| S5 | Back-to-back meetings (≤ 2 min gap) | Session boundary detection, no bleed between meetings | Two distinct summaries generated; no cross-contamination |
| S6 | Meeting with heavy crosstalk / interruptions | Transcription accuracy under noise | Key decisions still extracted; action items not duplicated |
| S7 | Meeting conducted partially in a second language | Multilingual robustness | Non-English segments flagged or translated; summary remains coherent |
| S8 | External stakeholder meeting shared to Slack | Sharing workflow, formatting, permissions | Summary posts to correct Slack channel within 5 min of meeting end |
| S9 | Meeting with no clear action items | Graceful handling of "nothing to do" | Summary generated without fabricated action items |
| S10 | Meeting that runs 2× over scheduled time | Long-running session stability, summary length management | No crash or timeout; summary appropriately condensed |

### 1.3 Integration Scenarios

| # | Integration | Scenario | Pass Criteria |
|---|---|---|---|
| I1 | Slack — Auto-post | Summary auto-posts to #team-meetings channel | Post appears ≤ 5 min after meeting ends; formatting renders correctly |
| I2 | Slack — Thread replies | Team members react/comment on summary in thread | Reactions and thread replies do not break the summary |
| I3 | Notion — Auto-create page | Summary creates a new page in "Meeting Notes" database | Page appears with correct date, attendees, and tags |
| I4 | Notion — Action item sync | Action items sync as checkboxes with assignees | Each item has owner, due date (if mentioned), and checkbox state |
| I5 | Slack + Notion combined | Summary shared to both simultaneously | No duplication, no race condition, both destinations receive identical content |

---

## 2. Daily Routines

### 2.1 Individual PM Daily Routine

**Morning (before standup):**
1. Open the meeting notes tool dashboard — confirm today's meetings are on the calendar sync
2. Check that the recording bot is authorized for each meeting room/link
3. Review yesterday's summaries for any flagged issues (missed action items, wrong speaker labels)

**During each meeting:**
1. Confirm the recording indicator is visible to all participants
2. Note any moments where the tool might struggle (crosstalk, name mispronunciation, topic switch) — jot a timestamp in the dogfooding log
3. Do NOT manually take notes — rely entirely on the tool (this is critical for honest evaluation)

**After each meeting (within 30 min):**
1. Review the generated summary against your memory of the meeting
2. Rate the summary: Accuracy (1–5), Completeness (1–5), Usefulness (1–5)
3. Check action items: Are they correct? Assigned to the right person? Any missing?
4. Share the summary to the designated Slack channel or Notion database
5. Log any bugs or quality issues on the triage board (see Section 5)

**End of day (5 min):**
1. Confirm all meetings from today have summaries generated
2. Log daily reflection in the dogfooding log: "What surprised me today?"

### 2.2 Team-Wide Daily Routine

| Time | Activity | Owner | Duration |
|---|---|---|---|
| 9:00 AM | Standup (recorded by the tool) | Rotating facilitator | 15 min |
| 9:20 AM | Quick check: Did yesterday's standup summary post correctly? | On-call PM | 2 min |
| 4:30 PM | Async Slack check-in: "Any critical bugs found today?" | All PMs | 5 min async |
| 5:00 PM (Fri) | Weekly retro and report generation | Dogfooding Lead | 45 min |

### 2.3 Week 1 vs. Week 2 Focus

| Aspect | Week 1: Exploration | Week 2: Stress + Polish |
|---|---|---|
| Goal | Establish baseline, find obvious bugs | Push edge cases, validate fixes |
| Scenarios | S1–S5, I1–I3 | S6–S10, I4–I5, re-test fixed S1–S5 |
| Sharing | Internal only (team Slack) | External stakeholder sharing required |
| Bug bar | Log everything, no severity filter | Focus on P0/P1; P2+ deferred to backlog |
| Reporting | Daily logs, mid-week pulse check | Daily logs, full weekly report, ship/no-ship gate |

---

## 3. Creator Commitments

Every PM signs the following commitment at sprint kickoff:

### 3.1 Individual Commitments

| # | Commitment | Measurable Target | Verification |
|---|---|---|---|
| C1 | Use the tool for every internal meeting | 100% of scheduled meetings recorded | Dashboard audit: meetings recorded / meetings scheduled |
| C2 | Never take manual notes as a backup | 0 parallel note docs created | Honor system + spot checks |
| C3 | Review every summary within 30 min | Median review time ≤ 30 min post-meeting | Timestamp of first log entry vs. meeting end time |
| C4 | Rate every summary on the 3-axis scale | 100% of summaries rated | Log completeness check |
| C5 | Share ≥ 3 summaries/week externally | ≥ 3 external shares per PM per week | Slack/Notion share log |
| C6 | Log every bug or quality issue | No "I forgot to log it" at retro | Cross-reference: low ratings without corresponding bug = gap |
| C7 | Attempt ≥ 2 stress-test scenarios per week | ≥ 2 scenario tags in log per week | Scenario coverage tracker |

### 3.2 Team-Level Commitments

| # | Commitment | Target |
|---|---|---|
| T1 | Minimum meetings recorded per week (team total) | ≥ 40 meetings/week |
| T2 | All 10 scenarios attempted at least once by end of sprint | 10/10 coverage |
| T3 | All 5 integration scenarios validated | 5/5 coverage |
| T4 | External stakeholder summaries shared | ≥ 24 total (8 PMs × 3/week) across sprint |
| T5 | Bug triage meeting held every other day | 5 triage sessions over 2 weeks |

### 3.3 Accountability

- The **Dogfooding Lead** (one designated PM) tracks compliance daily via dashboard
- Any PM who falls below commitment thresholds for 2 consecutive days gets a private Slack nudge
- End-of-sprint commitment scorecard is shared with the full team (anonymized scores, named outliers only if they opt in)

---

## 4. Dogfooding Log Specification

### 4.1 Log Entry Schema

Each meeting generates one log entry. Use a shared Notion database or Google Sheet with the following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `entry_id` | Auto-increment | Yes | Unique identifier |
| `date` | Date | Yes | Meeting date |
| `pm_name` | Select (8 options) | Yes | Which PM logged this |
| `meeting_type` | Select | Yes | Standup / 1:1 / Planning / Review / Ad-hoc / Stakeholder |
| `meeting_duration_min` | Number | Yes | Actual duration in minutes |
| `num_participants` | Number | Yes | Number of attendees |
| `scenario_tags` | Multi-select | No | Which stress-test scenarios (S1–S10, I1–I5) were relevant |
| `summary_generated` | Checkbox | Yes | Did the tool produce a summary? |
| `generation_time_sec` | Number | Yes | Seconds from meeting end to summary available |
| `accuracy_rating` | Rating (1–5) | Yes | How accurately did the summary reflect what happened? |
| `completeness_rating` | Rating (1–5) | Yes | Were all important points and decisions captured? |
| `usefulness_rating` | Rating (1–5) | Yes | Would you send this summary as-is to a stakeholder? |
| `action_items_correct` | Number | Yes | Count of correctly identified action items |
| `action_items_missed` | Number | Yes | Count of action items that should have been captured but weren't |
| `action_items_hallucinated` | Number | Yes | Count of action items the tool fabricated |
| `shared_to` | Multi-select | No | Slack / Notion / Email / Not shared |
| `shared_externally` | Checkbox | No | Was this shared outside the product team? |
| `bugs_filed` | Relation (to Triage Board) | No | Links to any bug entries created |
| `qualitative_notes` | Long text | No | Free-form observations, surprises, frustrations |
| `screenshot_url` | URL | No | Link to screenshot of any UI issue |

### 4.2 Log Views

Create the following saved views:

1. **My Entries** — Filtered to current PM, sorted by date descending
2. **Daily Team Summary** — Grouped by date, showing average ratings and total meetings
3. **Scenario Coverage** — Grouped by scenario tag, showing count and average ratings
4. **Bug Correlation** — Entries with bugs_filed, sorted by severity
5. **External Shares Tracker** — Filtered to shared_externally = true, grouped by PM

---

## 5. Triage Board Specification

### 5.1 Board Structure

Use a Kanban-style board (Notion board view, Linear, or GitHub Projects) with these columns:

| Column | Description |
|---|---|
| **New** | Just reported, not yet reviewed |
| **Triaged** | Reviewed, severity and category assigned |
| **In Progress** | Engineering is actively working on it |
| **Fixed (Awaiting Verify)** | Fix deployed, waiting for PM to re-test |
| **Verified** | PM confirmed the fix works |
| **Won't Fix** | Intentional behavior or deferred beyond this sprint |

### 5.2 Issue Card Schema

| Field | Type | Required | Description |
|---|---|---|---|
| `issue_id` | Auto-increment | Yes | Unique identifier |
| `title` | Text | Yes | Brief description (≤ 80 chars) |
| `reported_by` | Select | Yes | PM who found it |
| `date_reported` | Date | Yes | When it was found |
| `category` | Select | Yes | See categories below |
| `severity` | Select | Yes | P0 / P1 / P2 / P3 |
| `meeting_type` | Select | Yes | Which meeting type triggered it |
| `scenario_tag` | Multi-select | No | Related stress-test scenario |
| `description` | Long text | Yes | Detailed reproduction steps |
| `expected_behavior` | Long text | Yes | What should have happened |
| `actual_behavior` | Long text | Yes | What actually happened |
| `screenshot_url` | URL | No | Visual evidence |
| `log_entry_link` | Relation | No | Link to the dogfooding log entry |
| `assigned_to` | Person | No | Engineer responsible |
| `date_fixed` | Date | No | When the fix was deployed |
| `verified_by` | Select | No | PM who verified the fix |
| `date_verified` | Date | No | When verification happened |

### 5.3 Issue Categories

| Category | Examples |
|---|---|
| **Transcription** | Wrong words, missed speech, speaker misidentification |
| **Summary Quality** | Inaccurate summary, too long/short, wrong emphasis |
| **Action Items** | Missed items, hallucinated items, wrong assignee, wrong due date |
| **Integration — Slack** | Formatting issues, wrong channel, failed post, slow delivery |
| **Integration — Notion** | Page not created, wrong database, missing fields |
| **Recording** | Failed to start, dropped audio, partial recording, no end detection |
| **Performance** | Slow generation, timeout, high latency |
| **Privacy/Security** | Unauthorized sharing, failed redaction, confidential leak |
| **UX/UI** | Confusing interface, missing controls, poor mobile experience |
| **Other** | Anything not covered above |

### 5.4 Severity Definitions

| Severity | Definition | Response Time | Fix Target |
|---|---|---|---|
| **P0 — Blocker** | Tool is unusable; meetings cannot be recorded or summaries never generate | Triage within 2 hours | Fix within 24 hours |
| **P1 — Critical** | Major feature broken; summaries are consistently inaccurate or integrations fail | Triage within 4 hours | Fix within 48 hours |
| **P2 — Major** | Noticeable quality issue; affects usefulness but workaround exists | Triage within 1 day | Fix within sprint if possible |
| **P3 — Minor** | Cosmetic or edge-case issue; low impact on daily use | Triage within 2 days | Backlog for future sprint |

### 5.5 Triage Cadence

| Day | Activity | Attendees | Duration |
|---|---|---|---|
| Mon | Triage all weekend/Monday issues | Dogfooding Lead + Eng Lead | 20 min |
| Wed | Mid-week triage + verify fixes | Dogfooding Lead + Eng Lead | 20 min |
| Fri | End-of-week triage + prep for weekly report | Dogfooding Lead + Eng Lead + PM team | 30 min |

---

## 6. Weekly Report Template

Generate this report every Friday. Distribute to: Product team, Engineering lead, Design lead, and executive sponsor.

---

```
DOGFOODING WEEKLY REPORT — WEEK [1/2]
AI Meeting Notes Tool
Report Date: [YYYY-MM-DD]
Prepared by: [Dogfooding Lead Name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
[2–3 sentence overview: overall tool readiness, biggest win, biggest concern]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

USAGE METRICS

| Metric                              | Target   | Actual  | Status   |
|-------------------------------------|----------|---------|----------|
| Total meetings recorded             | ≥ 40     | [##]    | [✅/⚠️/❌] |
| Summaries generated                 | 100%     | [##%]   | [✅/⚠️/❌] |
| Avg generation time (sec)           | ≤ 120    | [##]    | [✅/⚠️/❌] |
| External shares (total across team) | ≥ 12     | [##]    | [✅/⚠️/❌] |
| PMs meeting all commitments         | 8/8      | [#/8]   | [✅/⚠️/❌] |
| Scenarios covered (cumulative)      | Week 1: 5, Week 2: 10 | [#/target] | [✅/⚠️/❌] |

QUALITY RATINGS (Averaged across all entries)

| Dimension       | This Week | Last Week | Trend |
|-----------------|-----------|-----------|-------|
| Accuracy        | [#.#/5]   | [#.#/5]   | [↑/↓/→] |
| Completeness    | [#.#/5]   | [#.#/5]   | [↑/↓/→] |
| Usefulness      | [#.#/5]   | [#.#/5]   | [↑/↓/→] |
| Overall (avg)   | [#.#/5]   | [#.#/5]   | [↑/↓/→] |

ACTION ITEM ACCURACY

| Metric                    | Count | Rate    |
|---------------------------|-------|---------|
| Correctly identified      | [##]  | [##%]   |
| Missed                    | [##]  | [##%]   |
| Hallucinated              | [##]  | [##%]   |
| Action Item Precision     | —     | [##%]   |
| Action Item Recall        | —     | [##%]   |

(Precision = correct / (correct + hallucinated))
(Recall = correct / (correct + missed))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BUG SUMMARY

| Severity | New This Week | Fixed | Verified | Open | Total (Cumulative) |
|----------|---------------|-------|----------|------|--------------------|
| P0       | [#]           | [#]   | [#]      | [#]  | [#]                |
| P1       | [#]           | [#]   | [#]      | [#]  | [#]                |
| P2       | [#]           | [#]   | [#]      | [#]  | [#]                |
| P3       | [#]           | [#]   | [#]      | [#]  | [#]                |
| Total    | [#]           | [#]   | [#]      | [#]  | [#]                |

Top 3 Bugs This Week:
1. [ISSUE_ID] — [Title] — [Severity] — [Status]
2. [ISSUE_ID] — [Title] — [Severity] — [Status]
3. [ISSUE_ID] — [Title] — [Severity] — [Status]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO COVERAGE

| Scenario | Attempted? | Avg Accuracy | Notable Findings |
|----------|------------|--------------|------------------|
| S1       | [Y/N]      | [#.#/5]      | [brief note]     |
| S2       | [Y/N]      | [#.#/5]      | [brief note]     |
| S3       | [Y/N]      | [#.#/5]      | [brief note]     |
| S4       | [Y/N]      | [#.#/5]      | [brief note]     |
| S5       | [Y/N]      | [#.#/5]      | [brief note]     |
| S6       | [Y/N]      | [#.#/5]      | [brief note]     |
| S7       | [Y/N]      | [#.#/5]      | [brief note]     |
| S8       | [Y/N]      | [#.#/5]      | [brief note]     |
| S9       | [Y/N]      | [#.#/5]      | [brief note]     |
| S10      | [Y/N]      | [#.#/5]      | [brief note]     |
| I1–I5    | [#/5]      | —            | [brief note]     |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTEGRATION HEALTH

| Integration       | Status      | Issues | Notes              |
|-------------------|-------------|--------|--------------------|
| Slack auto-post   | [🟢/🟡/🔴] | [#]    | [brief note]       |
| Slack threading   | [🟢/🟡/🔴] | [#]    | [brief note]       |
| Notion page sync  | [🟢/🟡/🔴] | [#]    | [brief note]       |
| Notion action items| [🟢/🟡/🔴]| [#]    | [brief note]       |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMMITMENT SCORECARD

| PM Name   | Meetings Recorded | Summaries Rated | External Shares | Scenarios Tested | Bugs Logged | Compliance |
|-----------|-------------------|-----------------|-----------------|------------------|-------------|------------|
| [PM 1]    | [#/#]             | [#/#]           | [#/3]           | [#]              | [#]         | [✅/⚠️]    |
| [PM 2]    | [#/#]             | [#/#]           | [#/3]           | [#]              | [#]         | [✅/⚠️]    |
| ...       | ...               | ...             | ...             | ...              | ...         | ...        |
| Team Avg  | [##%]             | [##%]           | [##/12]         | [##]             | [##]        | —          |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUALITATIVE HIGHLIGHTS

What's Working Well:
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

What Needs Improvement:
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

Surprising Findings:
- [Bullet 1]
- [Bullet 2]

User Quotes (verbatim from log entries):
> "[Quote from a PM about a positive experience]" — [PM Name]
> "[Quote from a PM about a pain point]" — [PM Name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATIONS FOR NEXT WEEK / POST-SPRINT

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 7. Ship / No-Ship Gate

The ship/no-ship decision is made at the end of Week 2 (Day 10, Friday afternoon). The Dogfooding Lead presents the final weekly report to the decision-making group: PM Lead, Engineering Lead, Design Lead, and Executive Sponsor.

### 7.1 Mandatory Pass Criteria (ALL must be met to ship)

Every criterion below must pass. A single failure results in a **No-Ship** decision.

| # | Criterion | Measurement | Threshold |
|---|---|---|---|
| G1 | No open P0 bugs | Triage board count | 0 open P0 issues |
| G2 | No open P1 bugs older than 48 hours | Triage board age check | 0 P1 issues unresolved > 48 hrs |
| G3 | Summary generation reliability | % of meetings that produced a summary | ≥ 98% |
| G4 | Average accuracy rating | Mean across all log entries | ≥ 3.5 / 5.0 |
| G5 | Average usefulness rating | Mean across all log entries | ≥ 3.5 / 5.0 |
| G6 | Action item recall | Correct / (Correct + Missed) | ≥ 80% |
| G7 | Action item precision | Correct / (Correct + Hallucinated) | ≥ 85% |
| G8 | Slack integration uptime | % of auto-posts that succeeded | ≥ 95% |
| G9 | Notion integration uptime | % of auto-syncs that succeeded | ≥ 95% |
| G10 | Summary generation latency (p95) | 95th percentile generation time | ≤ 180 seconds |
| G11 | External sharing completed | Total external shares across team | ≥ 24 (8 PMs × 3/week × 2 weeks, with 50% floor) |
| G12 | No privacy/security incidents | Count of P0/P1 privacy category bugs | 0 confirmed incidents |

### 7.2 Soft Criteria (Inform the decision but are not automatic blockers)

| # | Criterion | Measurement | Target | Weight |
|---|---|---|---|---|
| S1 | Average completeness rating | Mean across all log entries | ≥ 3.5 / 5.0 | Medium |
| S2 | Week-over-week quality improvement | Week 2 avg ratings vs. Week 1 | Positive trend | Medium |
| S3 | PM willingness to continue using | End-of-sprint survey: "Would you keep using this?" | ≥ 6/8 say Yes | High |
| S4 | Stakeholder feedback | External recipients' reaction (thumbs up/neutral/negative) | ≥ 70% positive or neutral | High |
| S5 | Scenario coverage | All 10 scenarios + 5 integrations tested | 15/15 | Low |
| S6 | Total open P2 bugs | Triage board count | ≤ 10 | Low |
| S7 | Mean generation time | Average (not p95) generation time | ≤ 60 seconds | Medium |

### 7.3 Decision Framework

```
┌─────────────────────────────────────────────────────────┐
│                  ALL G1–G12 PASS?                       │
│                                                         │
│          YES                           NO               │
│           │                             │               │
│           ▼                             ▼               │
│   ┌───────────────┐          ┌──────────────────┐       │
│   │ Check Soft     │          │ AUTOMATIC NO-SHIP│       │
│   │ Criteria S1–S7 │          │                  │       │
│   └───────┬───────┘          │ List failing     │       │
│           │                  │ gates. Determine │       │
│           ▼                  │ fix timeline.    │       │
│   ┌───────────────┐          │ Schedule re-gate │       │
│   │ ≥ 5/7 soft    │          │ in 3–5 days.     │       │
│   │ criteria met? │          └──────────────────┘       │
│   └───┬───────┬───┘                                     │
│    YES│       │NO                                       │
│       ▼       ▼                                         │
│   ┌──────┐ ┌──────────────┐                             │
│   │ SHIP │ │ CONDITIONAL  │                             │
│   │      │ │ SHIP         │                             │
│   └──────┘ │              │                             │
│            │ Ship with:   │                             │
│            │ - Known issues│                            │
│            │   documented │                             │
│            │ - 1-week     │                             │
│            │   follow-up  │                             │
│            │   checkpoint │                             │
│            └──────────────┘                             │
└─────────────────────────────────────────────────────────┘
```

### 7.4 Post-Gate Actions

**If SHIP:**
- Publish release notes with known limitations
- Set up production monitoring dashboard mirroring key dogfooding metrics
- Schedule 30-day post-launch check-in
- Archive dogfooding log and triage board as baseline reference

**If CONDITIONAL SHIP:**
- Document all known issues in a public-facing "Known Issues" page
- Assign owners to each open issue with committed fix dates
- Schedule 1-week follow-up gate review
- Limit initial rollout (e.g., beta flag, 10% of users, or invite-only)

**If NO-SHIP:**
- Identify the 3 most impactful failing gates
- Engineering creates a fix plan with estimated dates for each
- Schedule a re-gate review (typically 3–5 business days after fixes land)
- Continue dogfooding during the fix period to validate improvements
- If 2 consecutive no-ship decisions occur, escalate to executive sponsor for scope/timeline re-evaluation

---

## Appendix A: Sprint Calendar Overview

| Day | Date Slot | Key Activities |
|-----|-----------|----------------|
| D1 (Mon) | Week 1 Start | Kickoff meeting, tool onboarding, sign commitments, first standup recorded |
| D2 (Tue) | | Full day of meetings recorded, first log entries, first triage |
| D3 (Wed) | | Mid-week triage, scenarios S1–S3 attempted |
| D4 (Thu) | | 1:1 meetings focus, scenario S2 (privacy), first external shares |
| D5 (Fri) | | Week 1 report, scenarios S4–S5, integration tests I1–I3 |
| D6 (Mon) | Week 2 Start | Review Week 1 report, plan Week 2 stress tests |
| D7 (Tue) | | Scenarios S6–S7 (crosstalk, multilingual), verify Week 1 fixes |
| D8 (Wed) | | Mid-week triage, scenarios S8–S9, integration tests I4–I5 |
| D9 (Thu) | | Scenario S10, final external shares push, pre-gate data collection |
| D10 (Fri) | Sprint End | Final weekly report, ship/no-ship gate review, retrospective |

## Appendix B: End-of-Sprint Survey (for S3 soft criterion)

Distribute to all 8 PMs on Day 10 morning, before the gate review.

1. **Would you continue using this tool for your meetings if it shipped today?** (Yes / No / Only with improvements)
2. **What is the single most valuable thing the tool does?** (Free text)
3. **What is the single most frustrating thing about the tool?** (Free text)
4. **How confident are you in sharing a tool-generated summary with an external stakeholder without editing it?** (1–5 scale)
5. **Rank the following by importance for improvement:** (Drag to rank)
   - Transcription accuracy
   - Summary quality
   - Action item extraction
   - Speed of generation
   - Slack integration
   - Notion integration
   - Privacy controls
   - UI/UX
6. **Any other feedback?** (Free text)
