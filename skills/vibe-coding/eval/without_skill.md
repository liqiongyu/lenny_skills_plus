# 60-Minute Prototype: AI Meeting Notes to Action Items

## Demo Promise

> "In 60 minutes, we will demo pasting meeting notes and getting a prioritized action-item list for a PM."

---

## Minute-by-Minute Build Plan

### Phase 1: Project Setup (Minutes 0-5)

**Goal:** Scaffold the project so we have a running "Hello World" web page.

1. Create a new project directory: `meeting-action-items/`
2. Initialize with a single `index.html` file (we are going pure client-side to eliminate backend complexity)
3. Add a minimal CSS file (`style.css`) for layout
4. Add a JavaScript file (`app.js`) for logic
5. Open in browser to confirm the page loads

**Tech stack decision:** Pure HTML + CSS + JavaScript with a single OpenAI API call from the browser. No framework, no bundler, no server. This maximizes time spent on the actual feature and minimizes yak-shaving.

**Files at the end of Phase 1:**
```
meeting-action-items/
  index.html
  style.css
  app.js
```

### Phase 2: Build the Input UI (Minutes 5-15)

**Goal:** A clean paste-and-submit interface a PM would feel comfortable using.

**Layout:**
- Header with app title: "Meeting Notes -> Action Items"
- Large textarea (at least 10 rows) with placeholder text showing an example of meeting notes
- A dropdown to select priority framework (MoSCoW / Eisenhower / Simple High-Medium-Low)
- A "Generate Action Items" button
- An empty output area below the button (hidden until results arrive)

**Key UI decisions:**
- Textarea should be full-width, large enough to paste a full meeting transcript without scrolling
- Button should be visually prominent (solid color, large)
- Output area should be clearly separated from input area
- Add a small "Paste sample notes" link that fills the textarea with realistic example meeting notes for demo purposes

**Sample meeting notes to hardcode for the demo button:**
```
Product sync - March 17, 2026

Attendees: Sarah (PM), Mike (Eng Lead), Lisa (Design), James (QA)

Sarah: We need to ship the onboarding revamp by end of Q2. The current
drop-off rate at step 3 is 40%. Lisa, can you have updated wireframes
by Friday?

Lisa: I can do the mobile wireframes by Friday. Desktop will need
until next Wednesday. I also need the copy from marketing - can
someone chase that?

Mike: My team can start on the API changes Monday if we lock the
schema today. We also have a tech debt ticket for the auth module
that keeps blocking us - I'd like to prioritize that this sprint.

Sarah: Let's prioritize the auth fix - it's blocking three other
teams too. James, can you write regression tests for the auth
module while Mike's team works on the fix?

James: Yes, I'll start the test plan tomorrow. I'll need access to
the staging environment though - my credentials expired.

Sarah: I'll file the access request today. Also, everyone please
review the Q2 OKR draft I sent yesterday and leave comments by
Thursday. Mike, can you estimate the API work and share capacity
needs by Wednesday?

Mike: Will do. Also flagging - we need to decide on the caching
strategy before we go too far. Can we schedule a 30-min technical
design review next week?

Sarah: I'll schedule that for Tuesday. Let's also invite the
infrastructure team.
```

### Phase 3: Wire Up the AI Call (Minutes 15-30)

**Goal:** Send meeting notes to an LLM and get structured action items back.

**API approach:**
- Use the OpenAI Chat Completions API (GPT-4o or GPT-4o-mini)
- API key entered by the user in a small input field at the top of the page (stored in localStorage for convenience during the demo)
- Single API call with a carefully crafted system prompt

**System prompt (this is the core IP of the prototype):**

```
You are an expert project management assistant. Your job is to extract
every action item from meeting notes and return them in a structured
JSON format.

Rules:
1. Extract EVERY commitment, request, or task mentioned - do not miss any.
2. Identify the owner (who is responsible). If unclear, mark as "Unassigned".
3. Identify the deadline if mentioned. Use ISO date format (YYYY-MM-DD).
   If no deadline, mark as "No deadline specified".
4. Write each action item as a clear, imperative sentence starting with
   a verb (e.g., "Update the wireframes..." not "Wireframes need updating").
5. Assess priority using this framework:
   - P0 (Critical): Blocks other teams or is on the critical path
   - P1 (High): Has a stated deadline this week or is explicitly prioritized
   - P2 (Medium): Has a deadline but further out, or is important but not urgent
   - P3 (Low): Nice-to-have, no urgency, no stated dependency
6. Add a brief rationale for each priority assignment (1 sentence).
7. Group action items by owner.

Return ONLY valid JSON in this exact schema:
{
  "meeting_title": "string",
  "meeting_date": "string",
  "attendees": ["string"],
  "action_items": [
    {
      "id": 1,
      "action": "string (imperative sentence)",
      "owner": "string",
      "deadline": "string (YYYY-MM-DD or 'No deadline specified')",
      "priority": "P0 | P1 | P2 | P3",
      "priority_rationale": "string",
      "dependencies": ["string"] or [],
      "source_quote": "string (brief quote from notes that spawned this)"
    }
  ],
  "summary": "string (2-3 sentence executive summary of key decisions and next steps)"
}
```

**User prompt:**
```
Here are the meeting notes. Extract all action items:

---
{meeting_notes}
---

Priority framework to use: {selected_framework}
```

**JavaScript implementation outline:**

```javascript
async function generateActionItems() {
  const notes = document.getElementById('notes-input').value;
  const apiKey = document.getElementById('api-key').value;

  if (!notes.trim()) {
    showError('Please paste your meeting notes first.');
    return;
  }
  if (!apiKey.trim()) {
    showError('Please enter your OpenAI API key.');
    return;
  }

  showLoading(true);

  try {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: 'gpt-4o',
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: `Here are the meeting notes:\n\n${notes}` }
        ],
        temperature: 0.2,
        response_format: { type: 'json_object' }
      })
    });

    const data = await response.json();
    const result = JSON.parse(data.choices[0].message.content);
    renderActionItems(result);
  } catch (err) {
    showError('Failed to process notes. Check your API key and try again.');
    console.error(err);
  } finally {
    showLoading(false);
  }
}
```

**Key technical decisions:**
- `temperature: 0.2` for consistent, factual extraction (not creative)
- `response_format: { type: 'json_object' }` to guarantee valid JSON back
- Single API call (no chaining) to keep latency under 10 seconds

### Phase 4: Build the Output Rendering (Minutes 30-45)

**Goal:** Display the action items in a clean, PM-friendly format.

**Output layout (render from the JSON):**

**Section 1: Executive Summary**
- Meeting title and date in a header
- Attendees as a tag/chip list
- 2-3 sentence summary in a highlighted box

**Section 2: Action Items by Priority**
- Four collapsible groups: P0, P1, P2, P3
- Each group header shows count (e.g., "P0 - Critical (2 items)")
- Color coding: P0 = red, P1 = orange, P2 = blue, P3 = gray

**Each action item card shows:**
```
[ ] Update mobile wireframes for onboarding flow
    Owner: Lisa          Deadline: 2026-03-21 (Friday)
    Priority: P1 - Has explicit Friday deadline
    Dependencies: None
    Source: "Lisa, can you have updated wireframes by Friday?"
```

**Section 3: Owner Summary View**
- A toggle to switch from "by priority" to "by owner" view
- Groups all action items under each person's name
- Shows count per person (e.g., "Sarah (4 items)")
- Useful for a PM who wants to send each person their list

**Section 4: Quick Export**
- "Copy as Markdown" button -- copies a formatted markdown list to clipboard
- "Copy as Slack message" button -- copies a Slack-formatted version
- The markdown format:

```markdown
## Action Items from Product Sync (March 17, 2026)

### P0 - Critical
- [ ] **Fix auth module tech debt** — Owner: Mike | Deadline: This sprint
  > Blocking three other teams

### P1 - High
- [ ] **Update mobile wireframes** — Owner: Lisa | Deadline: Mar 21
  > Needed before engineering can start
...
```

**Rendering function outline:**

```javascript
function renderActionItems(data) {
  const output = document.getElementById('output');
  output.innerHTML = '';
  output.style.display = 'block';

  // Summary section
  output.appendChild(createSummarySection(data));

  // Priority view (default)
  const priorityView = createPriorityView(data.action_items);
  output.appendChild(priorityView);

  // Owner view (hidden by default)
  const ownerView = createOwnerView(data.action_items);
  ownerView.style.display = 'none';
  output.appendChild(ownerView);

  // View toggle
  output.appendChild(createViewToggle(priorityView, ownerView));

  // Export buttons
  output.appendChild(createExportButtons(data));
}
```

### Phase 5: Polish, Test, and Prep Demo (Minutes 45-60)

**Goal:** Make it demo-ready with no embarrassing rough edges.

**Polish checklist:**

1. **Loading state:** Add a spinner or "Analyzing meeting notes..." message with a subtle animation while the API call is in flight
2. **Error handling:** Graceful error messages for:
   - Empty input
   - Missing API key
   - API errors (rate limit, invalid key, network failure)
   - Malformed JSON response (fallback: show raw text)
3. **Responsive layout:** Ensure it looks reasonable on a laptop screen (the demo environment). No need for mobile optimization.
4. **Checkbox interactivity:** Clicking checkboxes should toggle strikethrough on the action item text (satisfying micro-interaction for the demo)
5. **Local persistence:** Save the last result to localStorage so refreshing doesn't lose output
6. **Typography:** Use a clean system font stack; ensure text hierarchy is clear (headings, body, metadata)

**Demo test run (do this at minute 50):**
1. Open the app in a browser
2. Click "Paste sample notes" to load the hardcoded example
3. Click "Generate Action Items"
4. Verify all expected action items appear
5. Toggle between priority and owner views
6. Click "Copy as Markdown" and paste into a text editor to verify
7. Test with empty input (should show error)
8. Test with API key removed (should show error)

**Demo script (what you say during the 2-minute demo):**
1. "We built a tool that turns messy meeting notes into a prioritized action-item list for PMs."
2. Paste the sample notes (or type a brief summary of what they contain)
3. Click "Generate Action Items"
4. While it loads: "Under the hood, we're using GPT-4o with a specialized prompt that extracts owners, deadlines, dependencies, and assigns priority levels."
5. Walk through the output: "Here we see 8 action items, grouped by priority. Two are P0 because they're blocking other teams."
6. Click on an owner: "PMs can also view by owner -- here's everything Sarah needs to do."
7. Click "Copy as Markdown": "One click to export for Slack, Notion, or Jira."
8. "This took 60 minutes. Next steps would be Slack integration, recurring meeting tracking, and follow-up reminders."

---

## Architecture Diagram

```
+------------------+     +-------------------+     +------------------+
|                  |     |                   |     |                  |
|  Textarea Input  |---->|  OpenAI API Call  |---->|  Rendered Output |
|  (meeting notes) |     |  (GPT-4o, JSON)  |     |  (cards + export)|
|                  |     |                   |     |                  |
+------------------+     +-------------------+     +------------------+
        |                         |                        |
   User pastes             System prompt             Two views:
   raw notes               extracts items            - By priority
                            with metadata            - By owner
                                                          |
                                                    Export buttons:
                                                    - Markdown
                                                    - Slack format
```

---

## Risk Mitigation

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| API key doesn't work | Medium | Have a backup key; test at minute 45 |
| JSON parsing fails | Low | Use `response_format: json_object`; add try/catch with raw text fallback |
| Action items are low quality | Medium | Low temperature (0.2); detailed system prompt with examples |
| Takes longer than 60 min | Medium | Cut the owner-view toggle first; cut export buttons second; the core value is input + output |
| Demo WiFi fails | Low | Pre-cache one API response in localStorage as a fallback |

---

## What to Cut if Running Behind

**Priority order (cut from bottom up):**

1. **Must have (minutes 0-35):** Input textarea, API call, basic list output
2. **Should have (minutes 35-45):** Priority grouping with color coding, owner view toggle
3. **Nice to have (minutes 45-55):** Copy-to-clipboard export, checkbox interactivity
4. **Stretch (minutes 55-60):** localStorage persistence, loading animation polish

If you're at minute 40 and don't have output rendering working, skip the fancy card layout and just render the JSON as a formatted `<pre>` block with syntax highlighting. A working demo with ugly output beats a pretty demo that doesn't work.

---

## Prompt Engineering Notes

The quality of this prototype lives or dies on the system prompt. Key design decisions:

1. **Imperative verb format** ("Update the wireframes" not "Wireframes should be updated") -- this is how PMs write tasks in Jira/Asana/Linear.

2. **Source quotes** -- Including the exact quote from the meeting notes that spawned each action item builds trust. PMs can verify the AI didn't hallucinate a task.

3. **Priority rationale** -- Not just "P1" but "P1 because it has an explicit Friday deadline." This makes the prioritization auditable and lets the PM override intelligently.

4. **Dependencies array** -- Surfaces blocked/blocking relationships. E.g., "Start API work" depends on "Lock the schema today." This is the kind of insight that separates useful extraction from a simple bullet list.

5. **Temperature 0.2** -- We want factual extraction, not creativity. Higher temperatures risk inventing action items that weren't discussed.

6. **JSON mode** -- Guarantees parseable output. Without this, GPT sometimes wraps JSON in markdown code fences or adds preamble text, which breaks `JSON.parse()`.

---

## Extending Beyond 60 Minutes (V2 Roadmap)

If this prototype gets traction, here's where to go next:

1. **Slack integration** -- Paste a Slack thread URL instead of raw text; auto-post action items back to the channel
2. **Recurring meeting tracking** -- Compare action items across weekly meetings; flag overdue or carried-over items
3. **Jira/Linear ticket creation** -- One-click to create tickets from each action item with pre-filled fields
4. **Multi-meeting context** -- Upload several meeting transcripts; the AI identifies cross-meeting themes and escalation patterns
5. **Meeting recording input** -- Accept audio/video files; transcribe with Whisper first, then extract actions
6. **Team profiles** -- Learn each team member's role and typical responsibilities to improve owner assignment accuracy
7. **Follow-up reminders** -- Send automated nudges via Slack/email when deadlines approach

---

## Complete File Structure (End State)

```
meeting-action-items/
  index.html          # Single-page app shell
  style.css           # Layout and component styles
  app.js              # All logic: API call, rendering, export
  README.md           # Setup instructions (just "open index.html")
```

Total lines of code estimate: ~350-450 lines across all three files. No dependencies. No build step. Open `index.html` in a browser and it works.
