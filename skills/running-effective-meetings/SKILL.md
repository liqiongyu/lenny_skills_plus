---
name: "running-effective-meetings"
description: "Run effective meetings: brief, agenda, facilitation script, decision log. See also: running-effective-1-1s (1:1s), running-offsites (offsites)."
---

# Running Effective Meetings

## Scope

**Covers**
- Deciding whether a meeting is needed (vs async doc/message)
- Choosing the right meeting format (operational / strategic / decision / workshop)
- Preparing a pre-read and “priming” to avoid context-less discussions
- Facilitating discussion, capturing decisions, and ensuring follow-through
- Improving recurring meeting hygiene (split/kill/shorten meetings)

**When to use**
- “Create an agenda and facilitation plan for a decision meeting.”
- “We need a weekly operational cadence — design the meeting format and templates.”
- “This meeting keeps going in circles — redesign it so we decide and assign actions.”
- “Turn this messy invite into a clear meeting brief + pre-read + follow-up.”

**When NOT to use**
- The goal is purely status updates (use async updates instead).
- There is no discussion to be had (you already have the decision and only need to broadcast it).
- The “decision owner” is not attending and cannot delegate decision rights.
- You need a recurring 1:1 with a direct report or manager (use `running-effective-1-1s`; different structure and relationship dynamics).
- You need a multi-day offsite or retreat (use `running-offsites`; this skill covers single meetings, not multi-session programs).
- You need a formal decision process with RACI, options scoring, and escalation (use `running-decision-processes`; this skill captures decisions within meetings but does not design the full decision framework).
- You need a design review or architecture review with technical critique (use `running-design-reviews`; specialized facilitation and feedback norms apply).
- The topic is a sensitive HR/legal/medical issue requiring specialist handling.

## Inputs

**Minimum required**
- Meeting objective (what changes after the meeting)
- Meeting type (or “recommend”): operational / strategic discussion / decision / workshop
- Attendees (and the decision owner, if any)
- Time box + date/time constraints (and remote/hybrid details)
- Context links or a 5–10 bullet background summary

**Missing-info strategy**
- Ask up to 5 questions from [references/INTAKE.md](references/INTAKE.md).
- If answers aren’t available, proceed with explicit assumptions and label unknowns.

## Outputs (deliverables)

Produce a **Meeting Pack** in Markdown (in-chat; or as files if requested), in this order:
1) **Meeting brief** (goal, type, decision(s), roles, pre-work)
2) **Pre-read** (context, options, open questions; “discover” happens async)
3) **Agenda** (timed, discussion-first)
4) **Facilitation script** (priming, prompts, how to handle stalls)
5) **Notes template** + **Decision log** + **Action items table**
6) **Follow-up message** (decisions, owners, deadlines, who-else-needs-to-know)
7) **Risks / Open questions / Next steps** (always included)

Templates: [references/TEMPLATES.md](references/TEMPLATES.md)

## Workflow (7 steps)

### 1) Decide if a meeting is needed and pick the format
- **Inputs:** Request + context + constraints.
- **Actions:** Clarify objective; decide whether the live meeting is for **discussion** only; pick meeting type (operational vs strategic vs decision vs workshop).
- **Outputs:** Meeting type recommendation + meeting objective + draft brief header.
- **Checks:** You can answer: “What will be different after this meeting?”

### 2) Define the discussion scope (what is in-room vs async)
- **Inputs:** Objective; stakeholders; open questions.
- **Actions:** Separate **Discover / Discuss / Decide**:
  - Discover (context/data/options) → async pre-read
  - Discuss (trade-offs, objections, clarifications) → live meeting
  - Decide (final call + recording) → after discussion, captured explicitly
- **Outputs:** Pre-read outline + list of discussion questions + decision statement(s).
- **Checks:** At least 60% of the live time is reserved for discussion, not reading.

### 3) Prime participants (pre-work + pre-read)
- **Inputs:** Pre-read outline; attendee list.
- **Actions:** Create a priming section (goal, conversation category, decision rights); assign pre-work; send pre-read 24–48h before when possible.
- **Outputs:** Complete pre-read + pre-work assignments.
- **Checks:** Every attendee can arrive “ready to discuss” without a live info dump.

### 4) Build a timed agenda that matches the format
- **Inputs:** Meeting type; discussion questions; time box.
- **Actions:** Timebox segments; limit to 1–3 topics; include explicit decision points; reserve time for closing alignment.
- **Outputs:** Agenda with timing, prompts, and expected outputs per section.
- **Checks:** Agenda maps each segment to a tangible output (decision, list, owner, next step).

### 5) Assign roles and write the facilitation script
- **Inputs:** Agenda; participants.
- **Actions:** Assign facilitator, decision owner, note-taker, timekeeper; write prompts and “if stuck” branches; set ground rules (parking lot, stack, time boxing).
- **Outputs:** Facilitation script + roles list.
- **Checks:** Roles are named; escalation path is clear if consensus fails.

### 6) Run the meeting and capture decisions/actions in real time
- **Inputs:** Script; notes template.
- **Actions:** Start with priming; facilitate discussion; capture decisions and action items as they happen; keep to time boxes.
- **Outputs:** Filled notes + decision log entries + action items table.
- **Checks:** No important decision is left implicit or “to be clarified later.”

### 7) Close, follow up, and improve meeting hygiene
- **Inputs:** Captured notes/decisions/actions.
- **Actions:** End with: (1) What did we decide? (2) Who does what by when? (3) Who else needs to know? Send follow-up within 24h; propose hygiene changes (split strategic vs operational, cancel/shorten recurring meetings).
- **Outputs:** Follow-up message + updated trackers + hygiene recommendations + Risks/Open questions/Next steps.
- **Checks:** Every action item has an owner and due date; stakeholders to inform are named.

## Quality gate (required)
- Use [references/CHECKLISTS.md](references/CHECKLISTS.md) and score with [references/RUBRIC.md](references/RUBRIC.md).
- Always include: **Risks**, **Open questions**, **Next steps**.

## Examples

**Example 1 (Operational cadence):** “Design a weekly operational meeting for a product squad to track priority projects without drifting into strategy.”  
Expected: a structured meeting brief, recurring agenda template, status update pattern, and a hygiene rule to move strategy to a separate forum.

**Example 2 (Decision meeting):** “Create a decision meeting pack for choosing between two onboarding flows (A vs B) with PM/Design/Eng and a decision owner.”  
Expected: pre-read with options + evidence, timed agenda, facilitation prompts for trade-offs, and a decision record + action items.

**Boundary example (redirect):** “I need to plan a 2-day strategy offsite with breakout sessions, team dinners, and a follow-up plan.”
Response: This is an offsite, not a single meeting. Redirect to `running-offsites` for the full offsite pack (brief, run-of-show, prework, logistics, post-offsite plan). If one session within the offsite needs a focused meeting pack, handle that session here.

**Boundary example (reframe):** “Schedule a meeting to ‘get alignment’ but there’s no decision, no owner, and no pre-read.”
Response: ask for the decision/outcome; recommend async discovery first; refuse to produce a meeting pack until objective/owner is defined.

## Anti-patterns (common failure modes)

1. **”Status meeting in disguise”** -- Labeling a meeting as a “discussion” but filling the agenda with round-robin updates. Live time should be for discussion and decisions; status belongs in async pre-reads.
2. **No pre-read sent** -- Spending the first 20 minutes of a 30-minute meeting giving context. Participants arrive cold, discussion time is crushed, and decisions get deferred.
3. **Too many topics** -- Cramming 5+ agenda items into a single meeting. Each topic gets shallow treatment and nothing gets decided. Limit to 1-3 topics per meeting.
4. **Missing decision capture** -- Good discussion happens but no one writes down what was decided, by whom, or by when. The same discussion repeats next week.
5. **No follow-up within 24h** -- Decisions and action items stay in the facilitator’s notes. Stakeholders who were not present never learn the outcomes. Alignment decays.

## Reference files
- [references/INTAKE.md](references/INTAKE.md)
- [references/WORKFLOW.md](references/WORKFLOW.md)
- [references/TEMPLATES.md](references/TEMPLATES.md)
- [references/CHECKLISTS.md](references/CHECKLISTS.md)
- [references/RUBRIC.md](references/RUBRIC.md)
- [references/SOURCE_SUMMARY.md](references/SOURCE_SUMMARY.md)
- [references/EXAMPLES.md](references/EXAMPLES.md)

