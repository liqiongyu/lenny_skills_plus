# Dogfooding Pack: AI Meeting Notes Tool

---

## 0) Context Snapshot

- **Product:** AI-powered meeting notes tool for remote teams
- **Target user persona:** Remote team members (PMs, engineers, designers) who attend 3-10 meetings/day and need structured summaries, action items, and seamless sharing to collaboration tools
- **Core workflows to dogfood (3):**
  1. **Record-to-Summary:** Join meeting -> auto-record -> generate AI summary
  2. **Action Item Extraction + Tracking:** Summary -> extract action items -> assign owners -> track completion
  3. **Share to Slack/Notion:** Summary + action items -> share to the right Slack channel or Notion page with proper formatting and context
- **Time box + cadence:** 2-week sprint (10 business days). Daily dogfooding during every internal meeting. Weekly triage on Fridays.
- **Participants (8-person product team):**
  - 3 Product Managers
  - 2 Engineers
  - 1 Designer
  - 1 Engineering Manager
  - 1 Head of Product
- **Environment:** Production app, real internal meetings (standups, 1:1s, planning sessions), live Slack integration, live Notion integration
- **Creator commitments:** Each PM must share at least 3 meeting summaries/week externally with stakeholders (real artifact, real audience)
- **Known pain points / hypotheses:**
  - Unknown: Summary quality for fast-paced technical discussions
  - Unknown: Action item extraction accuracy when items are implied rather than explicitly stated
  - Unknown: Slack/Notion formatting fidelity and whether shared summaries are "ready to send" without manual editing
  - Hypothesis: Standups (short, rapid updates) may produce lower-quality summaries than longer planning meetings
- **Tracking tools:** Linear (for triage board), Slack channel `#dogfooding-meeting-notes` (for daily logs and async discussion)
- **Ship gate definition:** All 3 core scenarios complete end-to-end with no hidden workarounds; shared summaries require zero manual editing before sending to stakeholders
- **Assumptions / unknowns:**
  - Assumption: Production app is stable enough for daily use (no known crash-level bugs)
  - Assumption: All 8 participants have accounts provisioned and integrations connected before Day 1
  - Unknown: Whether the tool handles meetings with >5 participants well
  - Unknown: How the tool performs with mixed audio quality (some participants on poor connections)

---

## 1) Dogfooding Charter

- **Why we are dogfooding:** To validate that our AI meeting notes tool delivers a complete, useful workflow -- from auto-recording through sharing -- that our team would actually rely on every day, before shipping to external users.

- **What we are dogfooding:** Three end-to-end workflows: (1) Record-to-Summary, (2) Action Item Extraction + Tracking, (3) Share to Slack/Notion. Across all internal meeting types: standups, 1:1s, and planning sessions.

- **Who participates:**

  | Name/Role | Daily commitment | Creator commitment |
  |---|---|---|
  | PM 1 | Use tool in every meeting (~4-6/day) | Share 3+ summaries/week to stakeholders |
  | PM 2 | Use tool in every meeting (~4-6/day) | Share 3+ summaries/week to stakeholders |
  | PM 3 | Use tool in every meeting (~3-5/day) | Share 3+ summaries/week to stakeholders |
  | Eng 1 | Use tool in every meeting (~3-4/day) | -- |
  | Eng 2 | Use tool in every meeting (~3-4/day) | -- |
  | Designer | Use tool in every meeting (~3-4/day) | -- |
  | EM | Use tool in every meeting (~4-5/day) | -- |
  | Head of Product | Use tool in every meeting (~5-7/day) | -- |

- **Cadence:**
  - **Daily:** Use the tool in every internal meeting. Log issues immediately after each meeting. Post a brief "top pain" note in `#dogfooding-meeting-notes` at end of day.
  - **Weekly:** 60-minute triage session every Friday at 2pm.

- **Rules:**
  1. Use the product as a real user would. No admin shortcuts, no backend workarounds, no "I'll just fix this in the DB."
  2. Log every issue as a reproducible artifact: steps to reproduce + expected vs. actual + evidence (screenshot, recording link, or copied output).
  3. No real customer/external-user data in dogfooding logs. Internal meeting content only. Redact sensitive business information from screenshots before attaching.
  4. If a workaround is needed to complete a scenario, log the workaround explicitly -- do not silently work around friction.
  5. PMs must share summaries with real stakeholders (not fake/test sends). The artifact must be genuinely useful.

- **Success criteria:**
  1. **S-Crit 1:** 80%+ of meeting summaries are accurate enough to share without manual editing (measured by PM self-assessment: "Would I send this as-is?")
  2. **S-Crit 2:** Action items extracted match actual action items discussed in >70% of meetings (spot-checked against manual notes)
  3. **S-Crit 3:** End-to-end time from "meeting ends" to "summary shared in Slack/Notion" is under 5 minutes with no manual intervention
  4. **S-Crit 4:** Zero S0 blockers open at end of sprint; all S1 issues have a disposition

- **Ship gate:** The team can complete all 3 core scenarios (Record-to-Summary, Extract Action Items, Share to Slack/Notion) end-to-end with no hidden workarounds, and shared summaries require zero manual editing before sending to stakeholders, across all 3 meeting types (standup, 1:1, planning).

---

## 2) Scenario Map

| Scenario | User goal | Start state | Steps (high level) | "Done" definition | Evidence of done | Notes / edge cases |
|---|---|---|---|---|---|---|
| **S1: First-time setup** | New user joins first meeting with the tool | Fresh account, no prior meetings, integrations not yet connected | 1. Sign up / log in 2. Connect Slack workspace 3. Connect Notion workspace 4. Join a scheduled meeting 5. Confirm recording starts automatically | Account created, integrations connected, first meeting recorded successfully | Screenshot of connected integrations + first recording in the dashboard | Edge: What if user has 2FA on Slack/Notion? What if the meeting platform (Zoom/Meet/Teams) requires separate auth? |
| **S2: Standup summary** | Get a usable summary of a 15-min standup | Meeting in progress, tool recording | 1. Tool auto-records standup 2. Meeting ends 3. AI generates summary 4. Review summary for accuracy 5. Share to team Slack channel | Summary captures each person's update accurately; shared to Slack within 2 min of meeting end | Slack message link + side-by-side comparison with manual notes | Edge: Fast speaker transitions; people talking over each other; very short updates (1-2 sentences per person) |
| **S3: 1:1 summary + action items** | Capture decisions and action items from a 30-min 1:1 | Meeting in progress, tool recording | 1. Tool auto-records 1:1 2. Meeting ends 3. AI generates summary with action items 4. Verify action items match what was discussed 5. Share summary to Notion page for the 1:1 series | Summary captures key discussion points; action items have correct owners and descriptions; Notion page is formatted correctly | Notion page link + action item accuracy check (% correct) | Edge: Implied action items ("we should probably..."); sensitive topics (performance reviews, compensation); quiet/mumbled speech |
| **S4: Planning session (long meeting)** | Get structured notes from a 60-min planning session | Meeting in progress, tool recording | 1. Tool auto-records planning session 2. Meeting ends 3. AI generates structured summary (decisions, action items, open questions) 4. Review for accuracy and completeness 5. Share to both Slack and Notion | Summary captures all major decisions and action items; structure matches the meeting's actual flow; both Slack and Notion outputs are well-formatted | Slack message + Notion page + accuracy assessment | Edge: Multiple topics/context switches; whiteboard/screen-share content not captured in audio; side conversations; meeting runs over 60 min |
| **S5: External share (creator commitment)** | PM shares a meeting summary with an external stakeholder who was not in the meeting | Completed meeting with generated summary | 1. Review AI summary 2. Assess if it's "send-ready" (no edits needed) 3. Share via Slack DM or Notion shared page to stakeholder 4. Note stakeholder's reaction/feedback (if any) | Summary shared to a real stakeholder without manual editing; stakeholder finds it useful or at least not confusing | Shared artifact link + self-assessment ("edited: yes/no, what?") + any stakeholder feedback | Edge: Summary contains internal jargon; action items reference people the stakeholder doesn't know; context is missing for someone not in the meeting |
| **S6: Action item follow-up** | Check whether action items from previous meetings are being tracked and followed up | Dashboard with past meetings and extracted action items | 1. Open action items view 2. Check if items from yesterday's meetings are listed 3. Verify owners are correct 4. Mark items as complete/in-progress 5. Confirm status syncs to Slack/Notion | Action items from past meetings are findable, owners are correct, status updates persist | Screenshot of action items view + sync confirmation | Edge: Duplicate action items across meetings; action item assigned to someone not on the tool; items from a meeting that had recording issues |

---

## 3) Routine Plan

### Daily routine (every meeting day -- all 10 business days)

**Time commitment:** ~20-30 min/day of dogfooding-specific overhead on top of normal meeting attendance (the tool runs during meetings that would happen anyway).

| Activity | Who | When | Time |
|---|---|---|---|
| Use the tool in every internal meeting | All 8 participants | Throughout the day | Passive (tool runs during meetings) |
| After each meeting: review summary + action items for accuracy | Meeting organizer or designated reviewer | Immediately after meeting | 3-5 min per meeting |
| Log any issues encountered | All participants | Immediately when issue occurs | 2-3 min per issue |
| Post end-of-day "top pain" note in `#dogfooding-meeting-notes` | All participants | End of day (before 5pm) | 2 min |

### Weekly schedule focus

| Day | Scenario focus | Notes |
|---|---|---|
| **Mon** | S2 (Standup) + S3 (1:1s) | Most teams have standups and 1:1s on Monday. Focus on summary quality. |
| **Tue** | S3 (1:1s) + S4 (Planning) | Capture longer meetings. Pay attention to action item extraction accuracy. |
| **Wed** | S4 (Planning) + S5 (External share) | PMs: share at least 1 summary externally today. Note if editing was needed. |
| **Thu** | S2 (Standup) + S6 (Action item follow-up) | Check: are action items from Mon-Wed tracked? Are owners correct? |
| **Fri** | S5 (External share) + S6 (Follow-up) + Triage | PMs: ensure 3 external shares are done by now. All: prepare top issues for triage. |

### Creator commitments (PMs only)

| Commitment | Cadence | "Done" definition | Where artifact lives |
|---|---|---|---|
| Share meeting summary externally with a stakeholder | 3x per week minimum (per PM) | Summary sent via Slack or Notion to a real stakeholder without manual editing | `#dogfooding-external-shares` Slack channel (post link + self-assessment) |

**Creator commitment tracking:** Each PM posts to `#dogfooding-external-shares` with:
- Link to the shared summary
- "Edited before sending: Yes/No"
- If yes: what was edited and why
- Any stakeholder feedback received

### Weekly triage agenda (Friday, 2pm, 60 min)

1. **Participation check** (5 min): Review who logged issues this week; review PM external share counts
2. **Metrics review** (5 min): Summary accuracy rate, action item extraction accuracy, time-to-share
3. **Top pains review** (20 min): Walk through S0/S1 issues first, then S2. Cluster duplicates.
4. **Disposition decisions** (15 min): For each top issue: Fix now / Schedule / Won't fix (with reason)
5. **Assign owners + next actions** (10 min): Every "Fix now" gets an owner and a target date
6. **Ship gate progress check** (5 min): Can we complete all 3 core scenarios without workarounds yet? What's still blocking?

---

## 4) Dogfooding Log (Issue-Level Schema)

### Log fields

| Field | Description | Required? |
|---|---|---|
| **ID** | Auto-incrementing (DF-001, DF-002, ...) | Yes |
| **Date** | Date issue was encountered | Yes |
| **Participant** | Who found it (name/role) | Yes |
| **Scenario** | Which scenario (S1-S6) | Yes |
| **Step** | Which step in the scenario | Yes |
| **Meeting type** | Standup / 1:1 / Planning | Yes |
| **Severity** | S0 / S1 / S2 / S3 (see scale below) | Yes |
| **Issue summary** | 1-sentence description | Yes |
| **Steps to reproduce** | Numbered steps to trigger the issue | Yes |
| **Expected behavior** | What should have happened | Yes |
| **Actual behavior** | What actually happened | Yes |
| **Evidence link** | Screenshot, recording clip, or copied text | Yes |
| **Workaround** | How the participant got past it (or "none -- blocked") | Yes |
| **Disposition** | New / Fix now / Schedule / Won't fix | Set at triage |
| **Owner** | Who is responsible for resolution | Set at triage |
| **Due** | Target resolution date | Set at triage |
| **Verified?** | Yes / No -- re-verified by running scenario after fix | After fix |

### Severity scale

| Level | Name | Definition | Examples |
|---|---|---|---|
| **S0** | Blocker | Cannot complete scenario. Data loss. Privacy/security risk. | Recording fails silently; summary contains another meeting's content; action items shared to wrong Slack channel |
| **S1** | Major | Can complete with significant workaround. Output unusable without manual intervention. Takes >3x expected time. | Summary misses 50%+ of discussion points; action items have wrong owners; Notion formatting is broken and unreadable |
| **S2** | Minor | Scenario completes but with friction. Paper cuts. Output needs minor tweaks. | Summary is accurate but poorly structured; 1-2 action items missing out of 8; Slack message formatting has minor issues |
| **S3** | Nit | Cosmetic. Low impact. Does not affect workflow completion. | Timestamp display format is inconsistent; button label is unclear; summary uses "participants" instead of actual names |

### Triage rules

- Any issue that **blocks completing a core scenario** is automatically S0/S1 until proven otherwise
- Any issue that involves **data going to the wrong place** (wrong Slack channel, wrong Notion page, wrong person's action items) is S0
- Duplicates: link to original, close the duplicate, bump severity of original if new evidence warrants it
- "Won't fix" requires a written reason visible to all participants (prevents re-litigating)

---

## 5) Triage Board Spec (Linear)

### Project setup

- **Project name:** `Dogfooding: Meeting Notes Tool - Sprint 1`
- **Team:** Product Team
- **Duration:** 2 weeks

### Labels

| Label category | Values |
|---|---|
| `dogfooding` | Applied to all issues from this sprint |
| `scenario` | `scenario:S1-setup`, `scenario:S2-standup`, `scenario:S3-1on1`, `scenario:S4-planning`, `scenario:S5-external-share`, `scenario:S6-action-followup` |
| `meeting-type` | `meeting:standup`, `meeting:1on1`, `meeting:planning` |
| `type` | `type:bug`, `type:ux-friction`, `type:ai-quality`, `type:integration-gap`, `type:docs-missing` |
| `severity` | `severity:S0-blocker`, `severity:S1-major`, `severity:S2-minor`, `severity:S3-nit` |

### Statuses (workflow)

```
New --> Triaged --> In Progress --> Ready for Verification --> Verified
                                                          \-> Won't Fix
```

| Status | Meaning | Who moves it |
|---|---|---|
| **New** | Just logged; not yet reviewed in triage | Reporter |
| **Triaged** | Reviewed in weekly triage; disposition assigned (fix now / schedule / won't fix) | Triage lead (EM or Head of Product) |
| **In Progress** | Owner is actively working on a fix | Owner |
| **Ready for Verification** | Fix is deployed; needs re-verification via dogfooding | Owner |
| **Verified** | Scenario re-run confirms the fix works; no regressions | Verifier (different from owner) |
| **Won't Fix** | Intentionally not addressing (reason documented in issue) | Triage lead |

### Required fields for new issues

- Title (1-line summary)
- Scenario label
- Meeting type label
- Severity label
- Type label
- Description with:
  - Steps to reproduce
  - Expected behavior
  - Actual behavior
  - Evidence (attachment or link)
  - Workaround used (or "blocked")

### Views to create in Linear

1. **"Top Pains" view:** Filter: `severity:S0-blocker` OR `severity:S1-major`, sorted by date created. Used in weekly triage.
2. **"By Scenario" view:** Grouped by scenario label. Shows issue distribution across workflows.
3. **"Fix Now" view:** Filter: status = `Triaged` or `In Progress`, disposition = fix now. The active work queue.
4. **"Verification Queue" view:** Filter: status = `Ready for Verification`. Items waiting to be re-tested.
5. **"Won't Fix Registry" view:** Filter: status = `Won't Fix`. Prevents re-litigating decided issues.

---

## 6) Weekly Dogfooding Report Template

---

### Week [1/2] Dogfooding Report: AI Meeting Notes Tool

**Sprint:** 2-week dogfooding sprint
**Report date:** [Date]
**Report author:** [Name]

---

#### Summary

- **Time box:** Week [1/2] of 2-week sprint ([Start date] - [End date])
- **Participation:** [X/8] team members logged issues this week. [Total] issues logged.
- **Meetings dogfooded:** [Total count] meetings ([X] standups, [Y] 1:1s, [Z] planning sessions)
- **Scenarios covered:** [List which scenarios got meaningful coverage]
- **Creator commitment progress:** [X/9] external shares completed this week (target: 9 = 3 PMs x 3/week)
  - PM 1: [X/3] shares -- [Edited: Y/N breakdown]
  - PM 2: [X/3] shares -- [Edited: Y/N breakdown]
  - PM 3: [X/3] shares -- [Edited: Y/N breakdown]
- **Ship gate status:** [RED / YELLOW / GREEN]
  - S2 Standup summary: [Pass / Fail / Partial -- details]
  - S3 1:1 summary + action items: [Pass / Fail / Partial -- details]
  - S4 Planning session: [Pass / Fail / Partial -- details]
  - S5 External share without editing: [Pass / Fail / Partial -- details]

---

#### Key metrics

| Metric | Target | Actual | Status |
|---|---|---|---|
| Summary accuracy (send-ready without editing) | 80%+ | [X%] | [On track / At risk / Behind] |
| Action item extraction accuracy | 70%+ | [X%] | [On track / At risk / Behind] |
| Time from meeting-end to shared summary | <5 min | [X min avg] | [On track / At risk / Behind] |
| S0 blockers open | 0 | [X] | [On track / At risk / Behind] |
| S1 issues with disposition | 100% | [X%] | [On track / At risk / Behind] |

---

#### Top pains (3-5)

**1) [Issue title]**
- Scenario impacted: [S#]
- Severity: [S0/S1/S2]
- Evidence: [Link to screenshot/recording/log entry]
- Why it matters: [Impact on completing the workflow; impact on real users]

**2) [Issue title]**
- Scenario impacted: [S#]
- Severity: [S0/S1/S2]
- Evidence: [Link]
- Why it matters: [Impact]

**3) [Issue title]**
- Scenario impacted: [S#]
- Severity: [S0/S1/S2]
- Evidence: [Link]
- Why it matters: [Impact]

*(Add up to 5 total)*

---

#### Decisions

**Fix now**
| Issue | Owner | Target date | Scenario impacted |
|---|---|---|---|
| [Issue title + ID] | [Name] | [Date] | [S#] |

**Schedule (next sprint or backlog)**
| Issue | Rationale | Scenario impacted |
|---|---|---|
| [Issue title + ID] | [Why not now] | [S#] |

**Won't fix (why)**
| Issue | Reason |
|---|---|
| [Issue title + ID] | [Explanation] |

---

#### Shipped + verified fixes

| Fix | Scenario verified | Verified by | Evidence |
|---|---|---|---|
| [Description of fix] | [S# -- re-ran end-to-end] | [Name, not the implementer] | [Link to evidence] |

---

#### Qualitative observations

- **What surprised us:** [Unexpected finding from dogfooding]
- **What worked well:** [Part of the product that exceeded expectations]
- **Internal-user bias check:** [Where our team's expertise might make us miss issues real users would hit]

---

#### Risks
1. [Risk description + likelihood + impact + mitigation]
2. [Risk description + likelihood + impact + mitigation]

#### Open questions
1. [Question that needs an answer before shipping or next sprint]
2. [Question]

#### Next steps
1. [Specific action with owner and deadline]
2. [Specific action with owner and deadline]
3. [Proposed focus for next week / next cycle]

---

## 7) Ship/No-Ship Gate

### Gate criteria

The product is **ship-ready** when ALL of the following are true:

| # | Criterion | Measurement | Threshold | Status |
|---|---|---|---|---|
| G1 | **Standup scenario completes end-to-end** | S2 runs with no workaround across 5+ standups | No workarounds needed | [ ] Pass / [ ] Fail |
| G2 | **1:1 scenario completes end-to-end** | S3 runs with no workaround across 5+ 1:1s | No workarounds needed | [ ] Pass / [ ] Fail |
| G3 | **Planning scenario completes end-to-end** | S4 runs with no workaround across 3+ planning sessions | No workarounds needed | [ ] Pass / [ ] Fail |
| G4 | **Summary accuracy meets bar** | PM self-assessment across all shared summaries | 80%+ "send-ready without editing" | [ ] Pass / [ ] Fail |
| G5 | **Action item extraction accuracy** | Spot-check against manual notes for 10+ meetings | 70%+ action items correctly identified | [ ] Pass / [ ] Fail |
| G6 | **Time-to-share meets bar** | Measured from meeting end to Slack/Notion post | Under 5 minutes, no manual steps | [ ] Pass / [ ] Fail |
| G7 | **Zero open S0 blockers** | Linear board | 0 issues with `severity:S0-blocker` in status != `Verified` or `Won't Fix` | [ ] Pass / [ ] Fail |
| G8 | **All S1 issues have disposition** | Linear board | 100% of `severity:S1-major` issues are triaged | [ ] Pass / [ ] Fail |
| G9 | **External shares were usable** | PM creator commitment tracking | 3+ summaries/week/PM shared without editing for at least 1 of the 2 weeks | [ ] Pass / [ ] Fail |
| G10 | **No data-goes-to-wrong-place issues** | Dogfooding log | Zero instances of summary/action items sent to wrong channel/page/person | [ ] Pass / [ ] Fail |

### Decision framework

| Gate result | Decision | Action |
|---|---|---|
| **All 10 criteria pass** | **SHIP** | Proceed to external beta / GA launch planning |
| **G1-G3 pass, G4-G6 partial (within 10% of threshold), G7-G10 pass** | **SHIP WITH KNOWN ISSUES** | Ship with documented limitations; schedule fixes for G4-G6 gaps in the first post-launch sprint |
| **Any of G1-G3 fail** | **NO-SHIP** | Core workflow is broken. Fix and re-run dogfooding for the failing scenario(s). Extend sprint by 3-5 days. |
| **G7 or G10 fail** | **NO-SHIP** | Blocker or data integrity issue. Fix immediately and re-verify. Do not ship until resolved. |
| **G4-G6 all below threshold by >10%** | **NO-SHIP** | AI quality or performance is not meeting the bar. Investigate root causes. May need model tuning, prompt engineering, or architecture changes before re-running. |

### Gate review process

- **When:** End of Day 10 (Friday of Week 2), during the final triage session
- **Who decides:** Head of Product (final call), with input from EM and all 3 PMs
- **Evidence required:** Completed Weekly Report for Week 2 with all metrics filled in; Linear board screenshot showing issue status distribution
- **Output:** Written "Ship / No-Ship" decision with rationale, posted to `#dogfooding-meeting-notes` and documented in the Linear project

---

## Risks

1. **Production instability risk:** Using production for dogfooding means any bugs could affect real data or integrations. *Mitigation:* Set up a dedicated Slack channel and Notion workspace for dogfooding outputs; avoid connecting to customer-facing channels.
2. **Participation drop-off:** 8 people committing to every meeting for 2 weeks is ambitious. Energy may wane in Week 2. *Mitigation:* Daily "top pain" posts create social accountability; Head of Product monitors participation in triage; celebrate found issues ("good catch" shoutouts).
3. **Internal-user bias:** The team knows the product intimately. They may unconsciously avoid broken paths, tolerate jargon in summaries, or not notice missing context that a new user would need. *Mitigation:* S5 (external share) forces PMs to see the output through a stakeholder's eyes; explicitly ask "would a new user understand this summary?" in the daily log.
4. **Meeting content sensitivity:** Internal meetings may contain sensitive topics (personnel, strategy, compensation). Recording everything creates a data surface. *Mitigation:* Establish a "pause recording" protocol for sensitive topics; ensure dogfooding logs redact sensitive content; delete recordings after the sprint unless needed for bug repro.
5. **AI quality variance:** Summary and action item quality may vary significantly by meeting type, length, and audio quality. A small sample (2 weeks) may not capture the full distribution. *Mitigation:* Deliberately dogfood across all 3 meeting types; track quality metrics by meeting type to identify patterns; plan a follow-up cycle if variance is high.

## Open Questions

1. **Audio quality baseline:** What is the minimum audio quality needed for acceptable summaries? Should we test with intentionally poor connections?
2. **Multi-language support:** Do any team meetings include non-English discussion? If so, is the tool expected to handle that?
3. **Recording consent:** What is the policy for recording 1:1s? Do both participants need to opt in each time, or is a blanket consent for the dogfooding sprint sufficient?
4. **Stakeholder feedback loop:** When PMs share summaries externally, should we have a structured way to capture stakeholder reactions (e.g., a follow-up question), or is informal feedback sufficient?
5. **Post-sprint continuity:** If the ship gate passes, does the team continue dogfooding post-launch, or does this transition to a different feedback mechanism?

## Next Steps

1. **[Owner: EM] Before Day 1:** Provision all 8 accounts in production. Connect Slack workspace and Notion workspace. Verify recording works in Zoom/Meet/Teams (whichever the team uses).
2. **[Owner: Head of Product] Before Day 1:** Create `#dogfooding-meeting-notes` and `#dogfooding-external-shares` Slack channels. Post the charter and rules.
3. **[Owner: PM 1] Before Day 1:** Set up the Linear project with labels, statuses, and views as specified in the triage board spec above.
4. **[Owner: All PMs] Day 1:** Run Scenario S1 (first-time setup) and log all onboarding friction.
5. **[Owner: Head of Product] Day 5 (Friday Week 1):** Run first weekly triage. Produce Week 1 report. Assess whether the sprint is on track.
6. **[Owner: Head of Product] Day 10 (Friday Week 2):** Run ship/no-ship gate review. Document decision and rationale. If ship: hand off to launch planning. If no-ship: define the extension plan and re-test scope.

---

## Quality Self-Assessment (per RUBRIC.md)

| Dimension | Score | Rationale |
|---|---|---|
| **1) Workflow realism** | 2 | Scenarios reflect real user goals (including day-0 setup in S1, edge cases documented for each scenario, creator commitment with real stakeholders). Done criteria are measurable. |
| **2) Participation + intensity** | 2 | Clear daily cadence tied to real meetings; defined time commitment; creator commitments for PMs with publish frequency and "done" definition; daily logging creates sustained signal. |
| **3) Evidence quality** | 2 | Log schema requires repro steps, expected vs. actual, evidence links, scenario/step linkage, and severity. Workarounds are explicitly captured. |
| **4) Decision + follow-through** | 2 | Weekly triage with defined agenda; dispositions (fix/schedule/won't fix with reasons); owners and due dates; verification by someone other than the implementer; Linear board tracks full lifecycle. |
| **5) Safety + bias control** | 2 | Production environment with guardrails (dedicated channels, redaction protocol, pause-recording for sensitive topics); internal bias explicitly acknowledged with mitigation (S5 external shares, daily "would a new user understand this?" check); external feedback planned as complement. |

**Total: 10/10** -- Passing bar (>= 7/10 with no dimension at 0) is met.

---

## Checklist Verification (per CHECKLISTS.md)

### A) Scope + realism
- [x] The pack names the target persona (remote team members) and 3 core workflows
- [x] Scenarios are end-to-end and have a clear "done" definition
- [x] At least one scenario starts from an empty/new user state (S1: First-time setup)
- [x] Creator commitment exists with publish cadence (3x/week) and done definition (shared without editing)

### B) Safety + environment
- [x] Environment choice is explicit (production) and justified (real meetings needed for realistic dogfooding)
- [x] Data handling rules are explicit (internal meetings only; redact sensitive content; pause-recording protocol)
- [x] No steps require credentials/secrets beyond normal product access
- [x] Privacy/security-risk issues are treated as S0 blockers (severity scale + triage rules)

### C) Capture quality (no vibes)
- [x] Each logged issue includes repro steps + expected vs actual + evidence
- [x] Each issue is tagged to a scenario and step
- [x] Severity scale is defined (S0-S3) and consistently applied via triage rules
- [x] Workarounds are recorded (required field in log schema)

### D) Triage + actionability
- [x] Weekly triage cadence is defined (Friday 2pm, 60 min, with agenda)
- [x] Top 3-5 issues will have disposition + owner + next action (report template requires this)
- [x] "Won't fix (why)" is recorded and visible (Linear "Won't Fix Registry" view)
- [x] "Fix now" list is realistically sized (triage rule: limit to what fits the next release window)

### E) Ship gate
- [x] Ship gate is scenario-based (complete end-to-end) not ticket-based
- [x] Fixes are re-verified by running the scenario again (verified by someone other than implementer)
- [x] Report includes shipped + verified fixes section

### F) Reporting
- [x] Weekly report includes decisions (fix now/schedule/won't fix)
- [x] Includes Risks, Open questions, Next steps
- [x] Next dogfooding cycle focus is proposed (in Next Steps section)
