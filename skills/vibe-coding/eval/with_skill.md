# Vibe Coding Prototype Pack: AI Meeting Notes to Action Items

---

## 1) Vibe Coding Brief

### Demo promise (one sentence)
"In 60 minutes, we will demo pasting meeting notes and getting a prioritized action-item list for a PM."

### Context
- **What we're prototyping:** A single-page web app where a PM pastes raw meeting notes into a text area, clicks "Generate," and receives a structured, prioritized list of action items with owners, deadlines, and priority levels.
- **Target user:** Product Manager (IC-level) who attends 4-8 meetings per day and needs to quickly extract and share action items.
- **Where it fits (internal/customer/concept):** Concept exploration -- proving that AI-powered extraction is fast, accurate enough to be useful, and worth investing in a full integration (Zoom, Google Meet, Slack).
- **Demo audience:** PM team lead + 2 engineers; internal stakeholder review to decide whether to pursue a production build.

### Non-goals (5)
1. Real LLM / AI integration (all AI output is mocked with deterministic rules).
2. User authentication or accounts.
3. Persistent storage or database (session-only; refresh clears state).
4. Multi-user collaboration or sharing.
5. Polished visual design or design-system compliance (functional styling only).

### Success criteria (demo-ready)
- The user can: paste meeting notes, click "Generate," and see a prioritized action-item list within 2 seconds.
- The user can: filter action items by priority (High / Medium / Low) and by owner.
- The demo shows: a preloaded "demo mode" with realistic sample notes that runs the hero path in one click.
- Reliability requirement: The hero path (paste notes -> generate -> view list) must never crash, show a blank screen, or produce empty output during the demo.

### Constraints
- **Timebox:** 60 minutes total (planning already done; ~55 min for build + package).
- **Platform preference:** Single-page web app (HTML + CSS + vanilla JS or lightweight framework). No build step required -- open `index.html` in a browser.
- **Data sensitivity / compliance:** No real meeting data in the prototype. All sample notes are fictional. No PII.
- **Tools allowed:** File creation and terminal commands (local dev server optional).

### Fake vs real (decisions)
| Concern | Decision | Rationale |
|---------|----------|-----------|
| Data | **Mock** -- hardcoded sample meeting notes (3 scenarios) | No API dependency; demo stability |
| LLM / AI extraction | **Mock** -- deterministic JS rules parse notes for action patterns | Avoids API key, cost, latency, flakiness |
| Integrations | **None / Stub** -- no calendar, Slack, or Zoom integration | Out of timebox; would require auth |
| Auth | **None** -- no login | Not needed for concept demo |
| Persistence | **Session-only** -- in-memory JS state; refresh resets | Avoids backend/DB setup |

---

## 2) Prototype Spec

### User flow (hero scenario)
1. **Open the app** -- PM opens `index.html` in a browser and sees a clean interface with a large text area, a "Generate Action Items" button, and a "Load Demo Notes" shortcut.
2. **Paste or load notes** -- PM either pastes their own meeting notes into the text area OR clicks "Load Demo Notes" to auto-fill with realistic sample content.
3. **Generate action items** -- PM clicks "Generate Action Items." The mock extraction engine parses the notes and renders a structured table of action items below the input area.
4. **Review and filter** -- PM sees each action item with: description, owner, priority (High/Medium/Low), and deadline. PM can filter by priority or owner using dropdown filters above the table.
5. **Copy to clipboard** -- PM clicks "Copy as Markdown" to get a clean, pasteable summary for Slack or a doc.

### Screens / components (MVP)

**Screen: Main (single page)**

| Component | Purpose | Inputs | Outputs | Edge cases |
|-----------|---------|--------|---------|------------|
| Header bar | App title + brief tagline | None | Visual only | -- |
| Notes input area | Accept raw meeting notes | Free-text paste or "Load Demo" button | Text in textarea | Empty input -> show inline warning |
| "Generate Action Items" button | Trigger mock extraction | Click event | Parsed action items rendered below | Disabled state when textarea is empty |
| "Load Demo Notes" button | Pre-fill textarea with sample notes | Click event | Textarea populated | -- |
| Action items table | Display extracted items | Parsed data array | Rendered rows with description, owner, priority, deadline | No items found -> friendly message |
| Filter bar | Filter by priority and owner | Dropdown selections | Filtered table view | "All" option resets filters |
| "Copy as Markdown" button | Export action items | Click event | Clipboard populated; toast confirmation | Empty list -> button disabled |
| Toast notification | Confirm clipboard copy | Triggered by copy action | Disappears after 2s | -- |

### Data model (prototype-level)

**Entities:**

```
MeetingNotes {
  rawText: string       // The pasted meeting notes
}

ActionItem {
  id: number            // Auto-increment
  description: string   // The action item text
  owner: string         // Extracted or "Unassigned"
  priority: "High" | "Medium" | "Low"  // Derived from keywords
  deadline: string      // Extracted date or "TBD"
  source: string        // The sentence/line it came from
}
```

**Example mock data (sample meeting notes input):**

```
Team standup - March 15, 2026

Attendees: Sarah (PM), Mike (Eng), Priya (Design), Tom (QA)

Discussion:
- Sarah: We need to finalize the Q2 roadmap by Friday. This is high priority.
  I'll send the draft to the team by Wednesday for review.
- Mike: The API migration is blocked. I need access credentials from DevOps.
  ACTION: Mike to file a ticket with DevOps by end of day today.
- Priya: Design review for the onboarding flow is ready. Can someone
  schedule a 30-min review session this week?
  ACTION: Sarah to schedule design review by Thursday.
- Tom: We have 3 critical bugs from the last release. I'll prioritize
  the login timeout bug first since it affects 20% of users.
  ACTION: Tom to fix login timeout bug by Wednesday. High priority.
- Sarah: Let's also plan the customer demo for next Tuesday.
  ACTION: Sarah to prepare demo script by Monday.
  ACTION: Mike to ensure staging environment is stable by Monday.

Next meeting: March 18, 2026
```

**Expected mock output (action items):**

| # | Description | Owner | Priority | Deadline |
|---|-------------|-------|----------|----------|
| 1 | Finalize Q2 roadmap - send draft to team for review | Sarah | High | Wed Mar 17 |
| 2 | File ticket with DevOps for API migration access credentials | Mike | High | Today (EOD) |
| 3 | Schedule 30-min design review for onboarding flow | Sarah | Medium | Thu Mar 19 |
| 4 | Fix login timeout bug (affects 20% of users) | Tom | High | Wed Mar 17 |
| 5 | Prepare customer demo script | Sarah | Medium | Mon Mar 22 |
| 6 | Ensure staging environment is stable for customer demo | Mike | Medium | Mon Mar 22 |

### Mock extraction logic (deterministic rules)
The mock extraction engine uses simple pattern matching (no LLM):
1. Lines starting with "ACTION:" or containing "action:" are extracted as action items.
2. Sentences containing "need to," "will," "should," "must," followed by a verb phrase are candidates.
3. Owner is extracted from the name before the colon or the subject of the sentence.
4. Priority is derived from keywords: "high priority," "critical," "urgent," "blocked" -> High; "by [date]" with no urgency marker -> Medium; everything else -> Low.
5. Deadline is extracted from date-like patterns ("by Friday," "by end of day," "by Wednesday").

### Acceptance criteria (observable)
- [ ] User can open index.html in any modern browser and see the app without errors.
- [ ] User can paste text into the textarea (minimum 10 characters required).
- [ ] User can click "Load Demo Notes" and see the textarea populated with sample notes.
- [ ] User can click "Generate Action Items" and see a table of 5+ action items within 1 second.
- [ ] Each action item row displays: description, owner, priority badge, and deadline.
- [ ] User can filter by priority (All / High / Medium / Low) and the table updates instantly.
- [ ] User can filter by owner (All / specific names) and the table updates instantly.
- [ ] User can click "Copy as Markdown" and paste a formatted list into another app.
- [ ] Empty textarea shows an inline warning; "Generate" button is disabled.
- [ ] No console errors during the hero path.

### Out of scope
- Real NLP / LLM integration
- Backend server or API
- Database / persistence
- User accounts / auth
- Mobile-responsive layout (desktop-first for demo)
- Accessibility audit (basic semantic HTML only)
- Deployment / hosting
- Unit tests (manual verification only)

---

## 3) Prompt Pack (safe vibe coding)

### Prompt A -- Scaffold the runnable thin slice

```
Context:
- Goal: Build a single-page web app where a PM pastes meeting notes and
  gets a prioritized action-item list. No LLM -- mock extraction with
  JS pattern matching. Must open from index.html with no build step.
- Platform/stack: HTML + CSS + vanilla JavaScript. Single index.html file
  (or index.html + style.css + app.js if cleaner). No frameworks, no npm.
- Timebox: 60 minutes total. This is slice 1 of 4.

Instructions:
- Propose a plan (3-6 bullets) before writing any code.
- Keep changes small and localized.
- List every file you will create or modify.
- Include exact run commands (e.g., "open index.html in browser" or
  "python3 -m http.server 8000").
- Do NOT add any secrets, API keys, or credentials.
- If anything is risky or destructive, stop and ask first.

Deliverable for this slice:
- A page with: header, textarea for notes input, "Generate" button,
  and a placeholder output area that shows "Action items will appear here"
  when clicked.
- The page must run by opening index.html. No errors in console.

Output format:
1) Plan (3-6 bullets)
2) File list
3) Full file contents (since this is the first slice)
4) Run instructions
5) Manual test steps to verify
```

### Prompt B -- Implement the mock extraction engine (slice 2)

```
Context:
- Current state: The app runs. It has a textarea, a "Generate" button,
  and a placeholder output area.
- Next slice: Implement a mock extraction engine that parses pasted
  meeting notes and renders a table of action items with description,
  owner, priority, and deadline.

Acceptance criteria:
- Pasting the sample meeting notes and clicking "Generate" produces
  5-6 action items in a table.
- Each row has: description, owner, priority (High/Medium/Low badge),
  and deadline.
- Empty input shows a warning; button is disabled when textarea is empty.

Constraints:
- Keep existing behavior working.
- Use deterministic JS pattern matching (regex), not an LLM.
- Prefer simple, readable code over clever architecture.
- No new dependencies.

Output: Plan + file changes + manual test steps.
```

### Prompt C -- Add filtering and "Load Demo Notes" (slice 3)

```
Context:
- Current state: App runs, generates mock action items from pasted notes.
- Next slice: Add priority filter dropdown, owner filter dropdown,
  and a "Load Demo Notes" button.

Acceptance criteria:
- "Load Demo Notes" populates the textarea with realistic sample notes.
- Priority filter (All/High/Medium/Low) instantly filters the table.
- Owner filter (All + each unique owner) instantly filters the table.
- Filters combine (priority AND owner).

Constraints:
- Keep existing extraction logic working.
- Filters should work on the already-generated data (no re-extraction).
- Simple solution preferred.

Output: Plan + file changes + manual test steps.
```

### Prompt D -- Add "Copy as Markdown" and demo polish (slice 4)

```
Context:
- Current state: App runs with extraction, filtering, and demo notes.
- Next slice: Add "Copy as Markdown" button, toast notification,
  visual polish for demo readiness, and a "demo mode" flow.

Acceptance criteria:
- "Copy as Markdown" copies a formatted action-item list to clipboard.
- A toast notification confirms the copy (disappears after 2 seconds).
- The overall layout is clean enough for a stakeholder demo.
- A "demo mode" one-click path: Load Demo Notes -> auto-generate ->
  results visible.

Constraints:
- No new dependencies. CSS-only polish.
- Keep all existing behavior working.
- This is the final slice; prioritize demo stability.

Output: Plan + file changes + manual test steps.
```

### Prompt E -- Debug a break (fast triage)

```
Inputs:
- Error message / symptom: [PASTE ERROR HERE]
- Steps to reproduce: [DESCRIBE WHAT YOU DID]

Instructions:
- Start with the smallest change likely to fix it.
- Suggest 1-3 hypotheses; pick the most likely.
- Provide a verification step after the fix.
- Do NOT refactor unrelated code.
```

---

## 4) Build Plan + Task Board

### Time budget (60 minutes)

| Phase | Minutes | Cumulative |
|-------|---------|------------|
| Planning (already done in this doc) | 0 | 0 |
| Slice 1: Scaffold | 10 | 10 |
| Slice 2: Mock extraction engine | 15 | 25 |
| Slice 3: Filtering + Load Demo | 15 | 40 |
| Slice 4: Copy + polish + demo mode | 12 | 52 |
| Demo script + runbook + QA | 8 | 60 |

### Task Board (4 vertical slices)

| Slice | User-visible behavior | Agent prompt | Validation steps | Definition of Done | Notes |
|------:|------------------------|-------------|------------------|-------------------|-------|
| 1 | App runs; textarea + "Generate" button shows placeholder output | Prompt A | 1. Open index.html in browser. 2. Verify header, textarea, button visible. 3. Click "Generate" -> see placeholder text. 4. Check console for zero errors. | Page loads with no errors; button click shows placeholder. | Keep it dead simple. Single file ok. |
| 2 | Mock action-item extraction produces a structured table | Prompt B | 1. Paste sample meeting notes. 2. Click "Generate." 3. Verify 5-6 rows in table with description, owner, priority badge, deadline. 4. Try empty input -> see warning. 5. No console errors. | Extraction works on sample notes; empty-input guard works. | Regex-based. Test with 2 different note formats. |
| 3 | Priority + owner filter dropdowns; "Load Demo Notes" button | Prompt C | 1. Click "Load Demo Notes" -> textarea fills. 2. Generate -> see items. 3. Filter by "High" -> only high-priority rows shown. 4. Filter by owner -> only that owner's items. 5. Combine filters -> intersection shown. 6. "All" resets. | All three controls work; filters combine correctly. | Populate owner dropdown dynamically from results. |
| 4 | "Copy as Markdown" with toast; visual demo polish; one-click demo mode | Prompt D | 1. Generate items. 2. Click "Copy as Markdown." 3. Paste into a text editor -> verify formatted list. 4. See toast notification appear and disappear. 5. Full demo flow: Load Demo -> Generate -> Filter -> Copy. No errors. | Clipboard works; toast shows; demo flow is smooth end-to-end. | Final slice. Freeze features after this. |

### Change log template (fill during build)

| Slice | What changed | Why | How verified | Issues found |
|-------|-------------|-----|-------------|-------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

---

## 5) Demo Script + Runbook

### Runbook (how to run)

**Prerequisites:**
- Any modern web browser (Chrome, Firefox, Safari, Edge).
- No server required. No npm. No build step. No dependencies.

**Setup:**
```bash
# Option A: Just open the file
open prototype/index.html
# (or double-click index.html in Finder / File Explorer)

# Option B: Local server (if clipboard API needs HTTPS context)
cd prototype/
python3 -m http.server 8000
# Then open http://localhost:8000 in your browser
```

**Where to open it:** `http://localhost:8000` or directly open `prototype/index.html`.

**Known limitations:**
- LLM extraction is mocked -- output is deterministic, not AI-generated.
- No persistence -- refreshing the page resets all state.
- Clipboard API may require localhost or HTTPS (not `file://`) in some browsers.
- Desktop-only layout; not optimized for mobile.

### Demo talk track (3-5 minutes)

**1) Context -- the problem (30 seconds)**
"As PMs, we sit in 4 to 8 meetings a day. After each meeting, we manually scan notes to find action items, figure out who owns what, and prioritize. This takes 10-15 minutes per meeting and things still fall through the cracks. What if we could automate this?"

**2) Hero scenario walkthrough (2 minutes)**
"Let me show you what we built in 60 minutes."
- Click **"Load Demo Notes"** -- "Here are realistic notes from a team standup. Notice the mix of discussion, decisions, and action items buried in the text."
- Click **"Generate Action Items"** -- "In under a second, we get a structured table. Each item has a description, an owner, a priority level, and a deadline. Notice that it correctly identified 6 action items from the free-form text."
- Use the **priority filter** -- "I can filter to just High-priority items. Three items surface: the roadmap, the DevOps blocker, and the login bug."
- Use the **owner filter** -- "Or I can filter by owner. Here are all of Sarah's items -- she has the most action items from this meeting."
- Click **"Copy as Markdown"** -- "One click gives me a formatted list I can paste directly into Slack or a project doc." [Paste into a visible text editor to show the output.]

**3) What's real vs mocked (30 seconds)**
"Transparency: the extraction engine right now is pattern-matching with rules, not an actual LLM. In production, we'd swap this for a call to an LLM API. The UI, the data flow, and the user experience are real. The AI is the one piece we'd plug in."

**4) What we learned (30 seconds)**
"Building this in 60 minutes told us three things: (1) The user flow works -- paste, generate, filter, copy. PMs can go from raw notes to actionable list in 10 seconds. (2) The filtering by priority and owner is immediately useful. (3) The hard part is extraction accuracy, which is exactly what we'd test next with a real LLM."

**5) Next steps (30 seconds)**
"If this direction resonates, our next sprint would be: integrate a real LLM for extraction, run an accuracy eval on 20 real meeting transcripts, and add a Slack integration to share action items directly to channels."

### Backup plan (if it breaks)

- **Screenshot fallback:** Take 4 screenshots before the demo covering: (1) empty state, (2) notes loaded, (3) action items generated, (4) filtered view. Walk through screenshots if the live demo fails.
- **Video fallback:** Record a 2-minute screen recording of the full hero flow before the demo. Store in the prototype folder as `demo-recording.mp4`.
- **Alternate flow:** If clipboard copy fails, manually select and copy the table content. If filtering breaks, show the full unfiltered table and explain the filtering feature verbally.
- **Quick restart:** Refresh the browser. The app has no persistent state, so a refresh returns to a clean starting point instantly.

---

## 6) Risks / Open questions / Next steps

### Risks (with mitigations)

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Mock extraction accuracy is poor on real-world notes (messy formatting, abbreviations, implicit actions) | High | High | Explicitly position as "rule-based mock" in demo. Next step: LLM integration + accuracy eval on 20 real transcripts. |
| Clipboard API fails on `file://` protocol | Medium | Medium | Use `python3 -m http.server` for the demo. Document in runbook. Test before the meeting. |
| Stakeholders expect production-ready features (auth, persistence, integrations) | Medium | Medium | Non-goals slide at the start of demo. Emphasize this is a 60-min concept validation, not a product. |
| Demo notes don't represent the audience's actual meeting style | Low | Medium | Prepare 2-3 sample note formats (standup, 1:1, planning). Let the audience paste their own notes live if time permits. |
| Browser compatibility issues (CSS, JS) | Low | Low | Test on Chrome and Firefox before demo. Use only standard, well-supported APIs. |

### Open questions

1. **Extraction approach:** Should production use a general-purpose LLM (GPT-4, Claude) with prompt engineering, or a fine-tuned model? Depends on accuracy requirements and cost tolerance.
2. **Integration priority:** Which integration is most valuable first -- Zoom transcript import, Google Meet, or Slack export? Needs PM team input.
3. **Accuracy bar:** What extraction accuracy (precision/recall on action items) is "good enough" to ship v1? Need to define an eval set and threshold (e.g., 90% precision, 80% recall).
4. **Multi-language support:** Do meeting notes come in languages other than English? Affects extraction logic.
5. **Editing workflow:** Should users be able to edit, add, or remove action items after extraction? Not in the prototype, but likely needed for production.

### Next steps (prioritized)

| Priority | Next step | Owner | Estimated effort | Dependency |
|----------|-----------|-------|-----------------|------------|
| P0 | Integrate real LLM (Claude or GPT-4) for extraction; replace mock engine | Eng lead | 1-2 days | API key + budget approval |
| P0 | Build accuracy eval set: 20 real meeting transcripts with manually labeled action items | PM (you) | 2-3 hours | Access to real meeting notes (anonymized) |
| P1 | Run accuracy eval: measure precision/recall on eval set with LLM extraction | Eng lead | 1 day | Eval set + LLM integration |
| P1 | Add Slack "share" integration: post action items to a channel | Eng | 1-2 days | Slack API token |
| P2 | Add persistence (save/load sessions) with a lightweight backend | Eng | 2-3 days | Architecture decision (Firebase, Supabase, etc.) |
| P2 | User testing: 5 PMs use the tool for 1 week; collect feedback | PM | 1 week | Working LLM version |
| P3 | Zoom / Google Meet transcript import | Eng | 3-5 days | API access + OAuth |

---

## Quality Gate

### Checklist results

**A) Scope + demo promise checklist**
- [x] Demo promise is one sentence and timeboxed.
- [x] Hero scenario is a single runnable flow (not a list of screens).
- [x] 5 explicit non-goals prevent scope creep.
- [x] "Fake vs real" decisions are explicit (data, integrations, auth).

**B) Prototype spec checklist**
- [x] User flow is written as 5 concrete steps.
- [x] Acceptance criteria are observable ("User can...").
- [x] Data model is simple and includes example mock data.
- [x] Out-of-scope items are listed.

**C) Vibe coding loop checklist**
- [x] Agent receives constraints and asks clarifying questions when needed (prompts structured with constraints).
- [x] Changes are small and localized; file list is explicit (each prompt specifies file scope).
- [x] App is run and verified after each slice (validation steps per slice).
- [x] A short change log template exists (to be filled during build).
- [x] No secrets/credentials are requested, pasted, or written to files.

**D) "Build tools to build the thing" checklist**
- [x] Not needed for this prototype -- the build is straightforward HTML/CSS/JS with no repetitive content generation step. Explicitly skipping Step 6 to stay within timebox.

**E) Demo readiness checklist**
- [x] Runbook enables a fresh user to run the prototype in under 2 minutes.
- [x] Demo script is 3-5 minutes and tells a coherent story (problem -> solution -> what's real -> learnings -> next steps).
- [x] Demo does not rely on fragile external dependencies (no APIs, no network, no auth).
- [x] Backup plan exists (screenshots, video recording, alternate flow, quick restart).

**F) Final pack checklist**
- [x] All deliverables are present in the specified order (brief -> spec -> prompts -> plan -> demo -> risks).
- [x] Risks, open questions, and next steps are specific and prioritized.
- [x] Rubric score meets the bar (see below).

### Rubric self-assessment

| Category | Score | Justification |
|----------|-------|---------------|
| 1) Demo clarity and scope control | **5** | Crisp one-sentence demo promise; 5 non-goals; explicit fake-vs-real table; 60-min timebox is realistic for 4 slices of vanilla HTML/CSS/JS. |
| 2) Prototype contract quality | **5** | 5-step user flow; 10 observable acceptance criteria; data model with example mock data; out-of-scope listed; edge cases covered (empty input, no results). |
| 3) Vibe coding execution loop quality | **5** | 4 sliced task board with validation steps per slice; structured prompt pack (A-E) with constraints, output format, and verification; change log template; tight generate-run-verify-log loop. |
| 4) Safety and robustness | **5** | No secrets anywhere; no risky operations; all data is mock/fictional; prompts include "ask before risky actions"; rollback is trivial (git revert or delete folder); no network dependencies. |
| 5) Demo readiness and handoff | **5** | Runbook with two run options; 5-section demo talk track with timing; backup plan (screenshots, video, alternate flow, restart); next steps are prioritized with owners and effort estimates. |

**Average: 5.0 / 5.0** -- Exceeds the "demo-ready" bar (>= 4.0, no category below 3).

---

## Appendix: File structure (expected after build)

```
prototype/
  index.html          # Main page (HTML structure)
  style.css           # Styling (clean, demo-ready)
  app.js              # Application logic (extraction, filtering, clipboard)
  sample-notes.js     # Sample meeting notes data (3 scenarios)
  README.md           # Quick-start instructions
```

All files are self-contained. No build step. No dependencies. No server required (with the caveat that clipboard API may prefer localhost).
