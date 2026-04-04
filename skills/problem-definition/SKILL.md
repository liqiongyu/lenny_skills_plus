---
name: "problem-definition"
description: "Define a product problem: problem statement, JTBD, alternatives, evidence, metrics. See also: writing-prds (solution spec)."
---

# Problem Definition

## Scope

**Covers**
- Turning a vague idea into a crisp, testable **problem definition**
- Writing a shareable **problem statement** (1-liner + expanded)
- Capturing **Jobs To Be Done (JTBD)** and target segments
- Mapping **current alternatives** (including non-digital/analog) and “why now / why digital”
- Building an **evidence + assumptions log** to drive learning
- Defining **success metrics + guardrails** and clear **scope boundaries**

**When to use**
- “Write a problem statement for…”
- “We need to define the problem space / JTBD.”
- “We keep jumping to solutions; help us get clear on the real problem.”
- “Pressure to ‘do AI’ — verify there’s a real pain point first.”
- “Before we write a PRD, align on what problem we’re solving.”

**When NOT to use**
- You already have an approved problem definition and need a delivery-ready PRD (use `writing-prds`)
- You need roadmap prioritization across many competing initiatives (use `prioritizing-roadmap`)
- You need to set company-level strategy/vision (use `defining-product-vision`)
- You need a competitive landscape analysis as the primary output (use `competitive-analysis`); this skill references alternatives only to frame the problem
- You’re doing deep research execution (recruiting, interviews, analysis); use this to frame *what to learn*, not as a substitute for `conducting-user-interviews` or `designing-surveys`
- You need to analyze existing user feedback data (use `analyzing-user-feedback`); this skill frames the problem, not the evidence pipeline

## Inputs

**Minimum required**
- Product/context + target user (or segment hypotheses)
- The triggering signal (customer quotes, data trend, stakeholder request, competitor move)
- The decision to make (e.g., invest now vs later; explore vs stop) + timeline
- Known constraints (tech/legal/privacy/compliance/capacity)

**Missing-info strategy**
- Ask up to 5 questions from [references/INTAKE.md](references/INTAKE.md).
- If still missing, proceed with clearly labeled assumptions and list **Open questions** that would change the decision.

## Outputs (deliverables)

Produce a **Problem Definition Pack** in Markdown (in-chat; or as files if the user requests):

1) **Context snapshot** (product, user, trigger, decision, constraints)
2) **Problem statement** (1-liner + expanded) + **why now**
3) **JTBD** (primary job + key sub-jobs) + target segment notes
4) **Current alternatives** (including analog/non-digital) + gaps + switching costs
5) **Evidence & assumptions log** (what we know vs what we’re guessing)
6) **Success criteria** (outcome metric(s), leading indicators) + **guardrails**
7) **Scope boundaries** (in/out, non-goals, dependencies)
8) **Prototype / learning plan** (fast prototype + tests to de-risk)
9) **Risks / Open questions / Next steps** (always included)

Templates: [references/TEMPLATES.md](references/TEMPLATES.md)  
Expanded heuristics: [references/WORKFLOW.md](references/WORKFLOW.md)

## Workflow (8 steps)

### 1) Intake + decision framing
- **Inputs:** User context; [references/INTAKE.md](references/INTAKE.md).
- **Actions:** Clarify the decision, time horizon, stakeholders, and constraints. Capture the trigger signal (data/quotes/event).
- **Outputs:** Context snapshot.
- **Checks:** You can state the decision in one sentence (“We are deciding whether to… by <date>”).

### 2) Define the target user + situation (segment + context)
- **Inputs:** Context snapshot.
- **Actions:** Specify who experiences the problem, when it happens, frequency, and what’s at stake. If multiple segments, pick a primary and list others as secondary.
- **Outputs:** Target user + context bullets.
- **Checks:** The segment is specific enough that a researcher could recruit for it.

### 3) Write the problem statement (1-liner + expanded)
- **Inputs:** Target user + trigger signal.
- **Actions:** Draft a crisp 1-liner, then expand with symptoms, root causes (hypotheses), and impact. Include **why now**.
- **Outputs:** Problem statement section (using [references/TEMPLATES.md](references/TEMPLATES.md)).
- **Checks:** Statement describes the problem without implying a specific solution or technology.

### 4) Map current alternatives (including non-digital) + “why use this”
- **Inputs:** Problem statement.
- **Actions:** List how users solve this today (manual workarounds, spreadsheets, incumbents, doing nothing). Include at least one analog/non-digital alternative when relevant.
- **Outputs:** Alternatives table + gaps + switching costs.
- **Checks:** You can answer: “Why would a user give this the time of day vs their current way?”

### 5) Separate problem from solution (avoid the shiny object trap)
- **Inputs:** Alternatives + early solution ideas (if any).
- **Actions:** Capture solution ideas as **hypotheses**, not commitments. If “AI” (or any tech) is proposed, state the user pain point first and treat tech choice as an implementation detail.
- **Outputs:** Evidence & assumptions log (with test ideas).
- **Checks:** Each assumption has a proposed test and a confidence level.

### 6) Define success criteria + guardrails
- **Inputs:** Problem statement + evidence.
- **Actions:** Define measurable outcomes, leading indicators, and guardrails (quality, trust, cost, latency, support load, etc.).
- **Outputs:** Success metrics + guardrails section.
- **Checks:** Metrics are unambiguous and tied to the user’s desired outcome.

### 7) Visualize the end state + prototype a path to clarity
- **Inputs:** Success criteria + scope constraints.
- **Actions:** Describe what “done” looks like (user-visible end state). Create a fast prototype/experiment plan to validate the hardest assumptions before building.
- **Outputs:** End-state description + prototype/learning plan.
- **Checks:** The team can “see the end” and name the 1–3 biggest unknowns being tested.

### 8) Quality gate + finalize the pack
- **Inputs:** Full draft pack.
- **Actions:** Run [references/CHECKLISTS.md](references/CHECKLISTS.md) and score with [references/RUBRIC.md](references/RUBRIC.md). Add Risks/Open questions/Next steps.
- **Outputs:** Final Problem Definition Pack.
- **Checks:** A stakeholder can review async and decide “proceed / pause / stop” without a meeting.

## Quality gate (required)
- Use [references/CHECKLISTS.md](references/CHECKLISTS.md) and [references/RUBRIC.md](references/RUBRIC.md).
- Always include: **Risks**, **Open questions**, **Next steps**.

## Anti-patterns (common failure modes)

1. **Solution-first framing** — The problem statement embeds a specific technology or feature (“We need an AI chatbot for support”) instead of describing the user pain. Strip the solution; restate as a user struggle with evidence.
2. **Segment hand-waving** — “Our users” without specifying who, when, and how often. A problem definition that applies to everyone applies to no one. Require a recruitable segment description.
3. **Evidence-free conviction** — The pack lists assumptions but marks them all “high confidence” without citing any data, quotes, or signals. Insist on at least one concrete evidence artifact per top assumption.
4. **Metric theater** — Success metrics exist but are unmeasurable within the stated timeline or are vanity metrics (e.g., “user happiness”). Every metric needs a measurement method and a realistic baseline.
5. **Scope creep via JTBD** — Sub-jobs multiply until the problem definition covers the entire product. Cap sub-jobs at 3-5 and explicitly mark anything beyond as out-of-scope.

## Examples

**Example 1 (B2B SaaS):** “Define the problem for improving onboarding activation in our analytics product.”
Expected: a pack with a tight segment, current onboarding alternatives/workarounds, measurable activation outcomes, and a prototype plan to test the most uncertain hypothesis.

**Example 2 (Consumer):** “Users abandon checkout on mobile; define the problem space and JTBD before proposing fixes.”
Expected: a problem statement grounded in evidence, an alternatives map (including ‘do nothing’), and guardrails (fraud/chargebacks/support load).

**Boundary example (redirect to writing-prds):** “Write a PRD for building an AI assistant; we don’t know what problem it solves.”
Response: push back; run this skill to define the user pain point and success metrics first, then hand off to `writing-prds`.

**Boundary example (redirect to conducting-user-interviews):** “We think onboarding is broken but have zero user data. Define the problem.”
Response: flag that the problem definition will be assumption-heavy; recommend running `conducting-user-interviews` first to gather evidence, then return here to frame the problem with real data.

