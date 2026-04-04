---
name: "sales-qualification"
description: "Build a Sales Qualification Pack (ICP, scorecard, discovery script, pipeline hygiene rules)."
---

# Sales Qualification

## Scope

**Covers**
- Defining what “qualified” means for your business (fit + need + access + urgency)
- Writing explicit **disqualification rules** to avoid time sinks
- Creating a **qualification scorecard** that produces consistent decisions across reps
- Designing a **discovery/qualification call script** that surfaces deal reality quickly
- Setting **stage exit criteria** + “no next step, no stage” pipeline hygiene rules
- Implementing a lightweight rollout + measurement plan for adoption

**When to use**
- “Our pipeline is full but nothing closes—help us qualify better.”
- “Create a lead qualification scorecard and disqualification criteria.”
- “Write a discovery/qualification script for SDRs/AEs.”
- “Define stage exit criteria so deals don’t rot in CRM.”
- “We’re spending time on bad-fit leads—create rules to stop it.”

**When NOT to use**
- You don’t have an ICP hypothesis or you’re still pre-problem/solution fit (start with `founder-sales` or `problem-definition`)
- You need a full sales org design (roles, hiring, enablement system) rather than qualification (use `building-sales-team`)
- You need to navigate a complex multi-stakeholder enterprise deal already in flight (use `enterprise-sales`)
- You need to design OTE, quotas, or commission mechanics for reps (use `sales-compensation`)
- You need pricing/packaging strategy, contracting, or legal/security review
- You want lead scraping/spammy outreach or anything deceptive

## Inputs

**Minimum required**
- Product + target customer (1 sentence each)
- ICP hypothesis (industry, size, buyer titles, “not for” exclusions)
- Sales motion (inbound/outbound/PLG→sales/enterprise) + current stages (if any)
- Typical deal profile (ACV range, cycle length, required stakeholders)
- Current pain: what “bad leads” look like (examples of 3–5 recent losses or stalls)
- Constraints: rep capacity, required response times, tooling (CRM), and handoff (SDR→AE)

**Missing-info strategy**
- Ask up to 5 questions from [references/INTAKE.md](references/INTAKE.md) (max 3–5 at a time).
- If data is missing, proceed with explicit assumptions and ship **two variants** if needed: (A) “Simple SMB motion” vs (B) “Complex/enterprise motion”.

## Outputs (deliverables)

Produce a **Sales Qualification Pack** in Markdown (in-chat; or as files if requested):

1) **Context snapshot** (ICP, motion, constraints, “what qualified means”)
2) **Qualification charter** (ICP segments, disqualifiers, qualification criteria, stage exit criteria)
3) **Qualification scorecard** (weighted criteria + thresholds + examples)
4) **Discovery/qualification script** (agenda, opener, question bank, disqualify talk track)
5) **CRM artifacts** (qualification notes template + required fields + pipeline hygiene rules)
6) **Rollout + measurement plan** (training, coaching, KPIs, iteration loop)
7) **Risks / Open questions / Next steps** (always included)

Templates: [references/TEMPLATES.md](references/TEMPLATES.md)

## Workflow (7 steps)

### 1) Intake + define the qualification decision
- **Inputs:** User context; [references/INTAKE.md](references/INTAKE.md); sample deals (won/lost/stalled).
- **Actions:** Clarify the decision you’re optimizing for: **pursue now**, **nurture**, or **disqualify**. Define the unit of analysis (lead, account, opportunity) and who qualifies (SDR, AE, founder).
- **Outputs:** Context snapshot + decision definitions + assumptions/unknowns.
- **Checks:** A rep can answer: “What decision am I making after this call?”

### 2) Lock ICP segments + hard disqualifiers (protect time)
- **Inputs:** ICP hypothesis; loss notes; product constraints; pricing guardrails.
- **Actions:** Create 1–3 ICP segments (primary/secondary) plus **explicit exclusions**. Write **hard disqualifiers** (fast “no” rules) that prevent time waste (e.g., wrong segment, no meaningful pain, cannot access buyer, cannot meet minimum price/value threshold).
- **Outputs:** ICP segment table + disqualifier list + a graceful disqualify talk track.
- **Checks:** Disqualifiers are observable and can be applied within the first 10–15 minutes.

### 3) Build the qualification scorecard (fit × need × access × urgency)
- **Inputs:** ICP + disqualifiers; desired outcomes; buyer risks.
- **Actions:** Choose 5–8 criteria and weight them. Add clear scoring anchors (0/1/2/3 or 1–5). Define thresholds for **accept**, **nurture**, **reject**. Add “minimum must-pass” criteria (non-negotiables).
- **Outputs:** Qualification scorecard + scoring rules + examples.
- **Checks:** Two different reps scoring the same deal should land within ~1 tier (accept/nurture/reject).

### 4) Define stage exit criteria + “no next step, no stage”
- **Inputs:** Current pipeline stages (or create minimal set); scorecard thresholds.
- **Actions:** Write stage definitions and exit criteria (what evidence is required to advance). Add pipeline hygiene rules: required fields, maximum stage age, and “no next step, no stage”.
- **Outputs:** Stage exit criteria table + hygiene rules + stalled-deal policy.
- **Checks:** Every active opportunity has (a) a next step with date, (b) an owner, and (c) a reason it can win.

### 5) Create the discovery/qualification script + question bank
- **Inputs:** Scorecard criteria; common loss reasons; buyer workflow.
- **Actions:** Draft a 20–30 minute call flow that surfaces: current state, pain/impact, trigger/urgency, stakeholders/decision process, constraints, and next step. Include a **disqualify path** (“not a fit, here’s what I recommend instead”) and a nurture path.
- **Outputs:** Call agenda + opener + question bank mapped to scorecard criteria.
- **Checks:** The script reliably produces a decision (accept/nurture/reject) by the end of the call.

### 6) Create CRM note template + rollout/measurement plan
- **Inputs:** CRM constraints; team roles; existing fields/stages; metrics baseline.
- **Actions:** Produce a single notes template that captures scorecard inputs in a structured way. Define required fields, lost/nurture reasons, and a 2-week rollout plan (training, call reviews, calibration).
- **Outputs:** CRM qualification notes template + rollout plan + measurement plan.
- **Checks:** A manager can audit 10 opportunities quickly and see consistent qualification evidence.

### 7) Quality gate + finalize
- **Inputs:** Draft pack.
- **Actions:** Run [references/CHECKLISTS.md](references/CHECKLISTS.md) and score with [references/RUBRIC.md](references/RUBRIC.md). Add **Risks / Open questions / Next steps** and a short “iteration loop” (what to revisit after 20–30 calls).
- **Outputs:** Final Sales Qualification Pack.
- **Checks:** The pack is copy/paste ready and reduces time spent on bad-fit deals immediately.

## Quality gate (required)
- Use [references/CHECKLISTS.md](references/CHECKLISTS.md) and [references/RUBRIC.md](references/RUBRIC.md).
- Always include: **Risks**, **Open questions**, **Next steps**.

## Anti-patterns

Avoid these common failure modes when building qualification systems:

1. **Qualification without disqualification.** Building a scorecard that only measures “how good” a lead is without defining hard “no” rules. The primary value of qualification is protecting rep time by saying no fast. Every qualification system must include explicit disqualifiers that can be applied in the first 10-15 minutes.
2. **BANT/MEDDICC cargo-culting.** Adopting a framework label (BANT, MEDDICC, MEDDPICC) without calibrating criteria and thresholds to your specific product, ACV, and buying process. A $12k ACV deal does not need a champion-mapping exercise; a $200k enterprise deal does. Adapt the framework to your reality.
3. **Scorecard without scoring anchors.** Listing criteria (budget, authority, need, timing) without defining what a 0, 1, 2, or 3 looks like for each. Two reps should score the same deal within one tier. If anchors are vague, the scorecard produces inconsistent decisions and is quickly abandoned.
4. **Pipeline stages without exit criteria.** Defining stages (Discovery, Evaluation, Negotiation) but not specifying what evidence is required to advance. Deals drift forward on optimism. Every stage must have observable, verifiable exit criteria.
5. **Over-qualifying early-stage pipelines.** Applying enterprise-grade qualification rigor when you have fewer than 50 opportunities and are still learning your ICP. At very early stages, you need signal collection, not gate-keeping. Use `founder-sales` first.

## Examples

**Example 1 (inbound B2B SaaS):**
“Use `sales-qualification`. We sell workflow automation to HR ops teams (50-500 employees). Inbound leads are high volume but low close rate. We need an SDR qualification script + scorecard + stage exit criteria. Output: a Sales Qualification Pack.”

**Example 2 (outbound mid-market/enterprise):**
“Use `sales-qualification`. We’re doing outbound to security leaders. ACV $50k-$200k, cycle 90-180 days. Deals stall after first call. Output: disqualifiers, MEDDICC-style scorecard, and CRM note template + hygiene rules.”

**Boundary example (redirect to founder-sales):**
“Just give me a list of leads to call and a generic pitch.”
Response: explain this skill focuses on qualification decisions and artifacts; ask for ICP/product context and propose using `founder-sales` for outreach messaging if needed.

**Boundary example (redirect to enterprise-sales):**
“I have a $500k deal with 8 stakeholders and need help navigating the decision process and closing strategy.”
Response: this skill builds qualification systems and scorecards, not deal-specific strategy. Redirect to `enterprise-sales` for multi-stakeholder deal navigation, and use the qualification artifacts from this skill to assess new opportunities going forward.
