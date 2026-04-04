---
name: "running-decision-processes"
description: "Run a decision process end-to-end: RAPID/DACI roles, options matrix, decision log, comms."
---

# Running Decision Processes

## Scope

**Covers**
- Running an end-to-end decision process for a cross-functional, high-stakes, or high-ambiguity decision
- Making **implicit assumptions explicit** (so they can be tested and reviewed later)
- Avoiding "decision drift" (hesitation, hidden vetoes, unclear decision rights)
- Capturing durable artifacts: decision brief, roles, meeting plan, decision log, comms, and a review loop

**When to use**
- "Draft a decision memo / pre-read and run the decision meeting."
- "We're stuck between two bad options—help us decide and commit."
- "Set up RAPID/DACI/RACI for this decision and clarify who decides."
- "Create an options + criteria matrix and a decision log entry."
- "This feels like a one-way door / irreversible decision—tighten the process."

**When NOT to use**
- You need to decide **what problem to solve** (do problem definition first).
- You need **prioritization across many opportunities** (use a roadmap/prioritization workflow).
- The "decision" is actually a **status update** or routine coordination (use a meeting/operating cadence).
- The decision is **personal/legal/HR** or requires specialist counsel (escalate to humans and domain experts).
- You need a **deep analytical comparison** of options with weighted scoring and sensitivity analysis (use `evaluating-trade-offs`).
- You need to **map systemic feedback loops and second-order effects** across an ecosystem (use `systems-thinking`).
- You need to **build stakeholder buy-in** for an already-made decision (use `stakeholder-alignment`).
- You need to **facilitate a meeting** that is not centered on making a specific decision (use `running-effective-meetings`).

## Inputs

**Minimum required**
- Decision to make (one sentence) and decision deadline (or "no later than" date)
- Context/why now (what changed; what happens if you don't decide)
- Scope boundaries + non-negotiables (policy, budget, timeline, customer commitments)
- Stakeholders and required approvers (who can block / who must live with the outcome)
- Current options under consideration (even if rough) and key uncertainties

**Missing-info strategy**
- Ask up to 5 questions from [references/INTAKE.md](references/INTAKE.md).
- If answers are unavailable, proceed with explicit assumptions and label unknowns.

## Outputs (deliverables)

Produce a **Decision Process Pack** (Markdown in-chat, or files if requested) in this order:
1) **Decision Brief / Pre-read** (problem, context, decision statement, constraints, criteria, options, recommendation if any)
2) **Options + Criteria Matrix** (including assumptions/unknowns that drive the choice)
3) **Decision Rights + Process** (RAPID/DACI/RACI, roles, timeline, meeting plan)
4) **Decision Log Entry** (decision, rationale, tradeoffs, assumptions, owner, review date)
5) **Decision Communication** (announcement + what changes + next steps)
6) **Decision Review Plan** (what to measure, when to revisit, how to learn)
7) **Risks / Open questions / Next steps** (always included)

Templates: [references/TEMPLATES.md](references/TEMPLATES.md)

## Workflow (8 steps)

### 1) Classify the decision (speed vs rigor)
- **Inputs:** Decision statement (draft); deadline; stakes.
- **Actions:** Classify as **one-way door** (hard to reverse) vs **two-way door** (reversible). Set a timebox and required rigor (light/standard/heavy). Name the failure cost (what's the worst credible outcome?).
- **Outputs:** Decision classification + process intensity + timebox.
- **Checks:** The process chosen matches reversibility and stakes (no "heavy process" for reversible choices; no "wing it" for irreversible ones).

### 2) Make the decision explicit (anti-hesitation)
- **Inputs:** Context/why now; constraints; success criteria.
- **Actions:** Turn implicit debate into a crisp decision: "We are deciding **X** by **date** to achieve **Y**." List non-negotiables and what "good" means.
- **Outputs:** Decision Brief sections: Decision statement, Why now, Success criteria, Constraints.
- **Checks:** A stakeholder can restate the decision in one sentence without adding qualifiers.

### 3) Gather context (historian pass)
- **Inputs:** Prior docs; past decisions; stakeholder perspectives.
- **Actions:** Reconstruct relevant history (what was tried, what failed, and why). Surface "baggage" and hidden constraints. Collect only the decision-relevant facts.
- **Outputs:** Decision Brief sections: Background, Prior decisions + rationale, Known constraints.
- **Checks:** The brief distinguishes **facts** vs **assumptions** vs **opinions**.

### 4) Generate options + criteria; log assumptions
- **Inputs:** Candidate options; goals; constraints.
- **Actions:** Define evaluation criteria and (if helpful) weights. Expand to 2–4 viable options (including "do nothing" if appropriate). For each option, make key assumptions explicit (what must be true for this to work?).
- **Outputs:** Options + Criteria Matrix; Assumptions/Unknowns list.
- **Checks:** Each option has at least 2–3 explicit assumptions; criteria reflect actual tradeoffs (not "everything is important").

### 5) Design the decision process + decision rights
- **Inputs:** Stakeholder list; org constraints; decision intensity.
- **Actions:** Choose a decision-rights model (RAPID/DACI/RACI). Assign roles (who recommends, who decides, who must be consulted, who is informed). Create a tight plan: pre-read, input window, meeting, decision capture, comms.
- **Outputs:** Decision Rights + Process doc; meeting plan.
- **Checks:** There is exactly one **Decider** (or a clearly defined decision body), and veto power is explicit.

### 6) Run a "curiosity loop" (contextual advice)
- **Inputs:** Key unknowns; list of 8–12 people to consult (mix of experts + context-aware peers).
- **Actions:** Ask lightweight, specific questions that demand rationale ("pick top 2 and why", "what would change your mind?"). Capture inputs, disagreements, and decision-relevant evidence. Update options/assumptions accordingly.
- **Outputs:** Curiosity Loop input summary; updated matrix/assumptions.
- **Checks:** Inputs are specific and actionable (not generic opinions); dissent is recorded, not smoothed over.

### 7) Decide and commit (document the why)
- **Inputs:** Final brief + matrix; role assignments; meeting agenda.
- **Actions:** Run the decision meeting (or async decision) with a bias toward clarity. Make the decision explicit, name the tradeoffs, assign an owner, and set a review date. Document rationale and what would cause a revisit.
- **Outputs:** Decision Log Entry; committed next steps; decision announcement draft.
- **Checks:** The decision and owner are unambiguous; the team knows what changes tomorrow.

### 8) Communicate, execute, and review (learning loop)
- **Inputs:** Decision log; implementation plan; metrics.
- **Actions:** Send the decision communication. Translate into tasks/milestones. Schedule a review to compare outcomes vs assumptions and capture learning (keep "intuition" testable).
- **Outputs:** Sent comms (or ready-to-send); review plan; retrospective prompts.
- **Checks:** A review date and measurement plan exist; assumptions are testable and tracked.

## Quality gate (required)
- Run [references/CHECKLISTS.md](references/CHECKLISTS.md) and score with [references/RUBRIC.md](references/RUBRIC.md).
- Always include: **Risks**, **Open questions**, **Next steps**.

## Examples

**Example 1:** "We need to decide whether to sunset Feature X by March 15. Create a decision memo, run a RAPID decision process, and draft the announcement."  
Expected: Decision Brief + options/criteria matrix + RAPID roles + decision log entry + comms + review plan.

**Example 2:** "We're split on building vs buying an analytics tool. It's a one-way door. Set up a rigorous process and capture assumptions so we can learn."  
Expected: One-way door classification + weighted criteria + assumptions log + consultation loop + decision log with review date.

**Boundary example:** "Help me decide if I should change careers."
Response: This skill is for organizational product/leadership decisions; suggest a personal decision framework or coach instead.

**Boundary example (neighbor redirect):** "Compare the pros and cons of three vendor options with a weighted scoring model."
Response: this is an analytical trade-off comparison, not a decision process. Use `evaluating-trade-offs` for weighted criteria matrices and sensitivity analysis. Come back here once you need to run the decision meeting and assign roles.

## Anti-patterns

1. **Process theater** — Running a heavy RAPID/DACI process for a two-way-door decision that should take 30 minutes. Always classify reversibility first and match process intensity to stakes.
2. **Hidden veto** — Assigning decision roles on paper but allowing unnamed stakeholders to block the outcome informally. Every veto holder must be explicit in the RAPID/DACI assignment.
3. **Options theater** — Including strawman alternatives to make the preferred option look inevitable. Each option must be genuinely viable with articulated tradeoffs.
4. **Decision without a log** — Making the decision in the meeting but never documenting the rationale, assumptions, or review date. Every decision must produce a durable log entry.
5. **Consensus disguised as clarity** — Ending with "we all agree" instead of naming the single Decider and the explicit tradeoffs accepted. Alignment is not the same as unanimity.

