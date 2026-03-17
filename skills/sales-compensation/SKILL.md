---
name: "sales-compensation"
description: "Design a sales compensation plan (OTE & pay mix, quotas & ramp, commission mechanics, and retention-aligned incentives) and produce a Sales Comp Plan Pack. Use for AE/SDR/AM comp plans, early sales hires, and GTM scaling. NOT for sales team hiring/org design (use building-sales-team), pipeline qualification (use sales-qualification), or offer negotiation (use negotiating-offers). Category: Sales & GTM."
---

# Sales Compensation

## Scope

**Covers**
- Designing compensation plans for revenue roles (typically SDR/BDR, AE, AM/CSM with expansion)
- Setting **OTE**, **base/variable mix**, **quota**, and **ramp**
- Defining commission mechanics (crediting rules, accelerators, clawbacks, payout timing)
- Aligning incentives with **long-term customer value** (retention / NRR), not just bookings
- Producing rep-facing plan docs + admin rules so payouts are actually operable

**When to use**
- “Design a comp plan for our first AEs/SDRs.”
- “What should our OTE and base/variable split be?”
- “Set quotas and a ramp plan for new reps.”
- “Create accelerators + rules so reps don’t game discounting.”
- “Our reps close bad-fit deals that churn—align comp with retention/NRR.”

**When NOT to use**
- You need to hire, structure, or onboard an early sales team (use `building-sales-team` for org design, scorecards, and ramp plans)
- You need to improve pipeline quality, lead scoring, or qualification criteria (use `sales-qualification`)
- You need to negotiate a specific offer with an individual candidate (use `negotiating-offers`)
- You need legal/tax/HR advice, employment compliance guidance, or jurisdiction-specific plan language (use qualified professionals)
- You’re designing **executive compensation** or equity plans (different problem)
- You don’t yet have basic GTM foundations (ICP, pricing, what counts as a closed-won) — do that first, then return
- You want an overly complex “formula soup” plan that can’t be explained in one page or administered reliably

## Inputs

**Minimum required**
- Company stage + GTM motion (inbound/outbound/PLG/enterprise) and primary sales roles
- What you sell + pricing model + typical ACV/ARR and sales cycle length
- Your economic constraints: gross margin, CAC payback target (or runway), budget for sales comp
- Target outcomes for the period (bookings/revenue/NRR) and the time horizon you care about (e.g., 90-day retention, annual renewals)
- Current baseline (if any): pipeline conversion, win rate, ramp time, churn/NRR
- Constraints: simplicity tolerance, payout timing preference, risk tolerance (for the company and for reps)

**Missing-info strategy**
- Ask up to 5 questions from [references/INTAKE.md](references/INTAKE.md), then proceed.
- If key data is missing, make explicit assumptions and include:
  - **Assumptions & unknowns**
  - **Sensitivity ranges** (e.g., quota/rates under low/base/high scenarios)
  - **Validation plan** (what to measure in the next 30–90 days)

## Outputs (deliverables)

Produce a **Sales Comp Plan Pack** in Markdown (in-chat; or as files if requested), in this order:

1) **Context snapshot** (roles, stage, goals, constraints, time horizon)
2) **Comp philosophy** (what behaviors you want; what you want to prevent)
3) **Role → metric mapping** (what gets paid on, and why it’s controllable)
4) **OTE + pay mix table** (base/variable split by role + rationale)
5) **Quota + ramp model** (quota by period + ramp schedule + any draw/guarantee)
6) **Commission mechanics spec** (crediting, rates, accelerators, splits, discount policy, payout timing, clawbacks)
7) **Retention-alignment addendum** (choose one approach; define measurement + timing)
8) **Admin & governance** (required CRM fields, payout process, disputes, exceptions, change control)
9) **Rep-facing one-pager + FAQ** (copy/paste)
10) **Risks / Open questions / Next steps** (always included)

Templates: [references/TEMPLATES.md](references/TEMPLATES.md)

## Workflow (7 steps)

### 1) Intake + plan boundaries (what problem are we solving?)
- **Inputs:** User context; [references/INTAKE.md](references/INTAKE.md).
- **Actions:** Confirm roles in scope, selling motion, time horizon (bookings vs retention), budget constraints, and “must-not” behaviors (discounting, churny deals, channel conflict). Identify what data you do/don’t have.
- **Outputs:** Context snapshot + assumptions/unknowns + decision on time horizon.
- **Checks:** Success is measurable (who/what/by when) and the plan scope is explicit.

### 2) Define role responsibilities + “what gets paid on”
- **Inputs:** Role definitions; pipeline stages; revenue recognition basics; retention model.
- **Actions:** Choose 1 primary performance metric per role (e.g., ARR bookings, qualified meetings, expansion ARR, gross profit). Define “crediting” rules (when a deal counts, splits, renewals).
- **Outputs:** Role → metric mapping + crediting rules draft.
- **Checks:** The metric is (a) measurable, (b) attributable, and (c) reasonably controllable by the rep.

### 3) Set OTE + base/variable mix (pay risk where it belongs)
- **Inputs:** Talent market bands (if known), role seniority, sales cycle, role risk, stage.
- **Actions:** Set OTE targets and the base/variable mix per role. Choose a default mix (often ~50/50 for many AE roles) and adjust based on cycle length, product maturity, and expected rep autonomy.
- **Outputs:** OTE + pay mix table with rationale and guardrails.
- **Checks:** OTE is economically viable for the business and believable to candidates; pay mix matches controllability and sales cycle length.

### 4) Build quota + ramp model (make “on target” realistic)
- **Inputs:** Targets; baseline conversion (or assumptions); expected ramp time; territory/segment definitions.
- **Actions:** Create a quota model (top-down + bottom-up cross-check). Define ramp schedule, draw/guarantee (if used), and what happens if the plan changes mid-year.
- **Outputs:** Quota + ramp tables (low/base/high scenarios).
- **Checks:** A rep at OTE can realistically hit quota with the assumed pipeline and conversion.

### 5) Define commission mechanics (simple, compute-able, enforceable)
- **Inputs:** OTE/Quota; metric definitions; discount/margin constraints.
- **Actions:** Set rates, accelerators/decelerators, and payout timing. Add guardrails: discount approval thresholds, deal qualification minimums, splits/overlays, clawbacks/chargebacks, and edge-case rules.
- **Outputs:** Commission mechanics spec + 2–3 worked payout examples.
- **Checks:** A Sales Ops/admin can calculate payouts from CRM data without manual interpretation.

### 6) Add retention/quality alignment (avoid paying for churn)
- **Inputs:** Retention/NRR goals; churn timing; implementation/onboarding reality; data availability.
- **Actions:** Choose one retention-alignment approach (e.g., partial holdback until 90 days, commission adjustment on early churn, pay on collected revenue, or NRR multipliers). Define measurement windows and how disputes are handled.
- **Outputs:** Retention-alignment addendum (chosen approach + rationale + admin rules).
- **Checks:** The approach is understandable to reps and proportional to their influence on retention.

### 7) Quality gate + finalize (rep-ready + admin-ready)
- **Inputs:** Draft pack.
- **Actions:** Run [references/CHECKLISTS.md](references/CHECKLISTS.md) and score using [references/RUBRIC.md](references/RUBRIC.md). Produce the rep-facing one-pager + FAQ. Always include **Risks / Open questions / Next steps** and a 30–90 day validation plan.
- **Outputs:** Final Sales Comp Plan Pack.
- **Checks:** The plan can be explained in one page, computed from CRM fields, and aligns incentives with business + customer outcomes.

## Quality gate (required)
- Use [references/CHECKLISTS.md](references/CHECKLISTS.md) and [references/RUBRIC.md](references/RUBRIC.md).
- Always include: **Risks**, **Open questions**, **Next steps**.

## Anti-patterns

Avoid these common failure modes when designing sales compensation:

1. **Formula soup.** Creating a comp plan with 4+ metrics, nested multipliers, and conditional accelerators that no rep can mentally model. If a rep cannot estimate their payout from memory after closing a deal, the plan is too complex. Stick to 1 primary metric per role and at most 1-2 secondary adjustments.
2. **Paying for bookings while ignoring churn.** Rewarding reps purely on closed-won ARR with no retention alignment. This incentivizes closing bad-fit customers, aggressive discounting to pull deals forward, and over-promising during the sales process. Always include at least one retention-alignment mechanism.
3. **Unrealistic quotas that kill morale.** Setting quotas top-down from the board plan without a bottom-up cross-check (pipeline coverage, conversion rates, ramp time). When fewer than 50-60% of reps hit quota, the plan is broken, not the reps. Always stress-test quotas under low/base/high scenarios.
4. **Copy-pasting comp plans across stages.** Using a Series C comp structure (territories, overlays, SPIFs, multi-tier accelerators) for a seed-stage team with 2 reps and no pipeline history. Early-stage plans should be simple: base + variable on one metric, with a clear ramp and draw.
5. **No ramp protection for new hires.** Putting new reps on full quota from day one without a draw, guarantee, or reduced ramp quota. Reps who feel underwater from week one either leave or cut corners. Ramp plans must reflect realistic time-to-productivity.

## Examples

**Example 1 (first AE comp plan, seed-stage SaaS):**
“Use `sales-compensation`. We’re seed-stage B2B SaaS, $12k ACV, 45-day cycle. Hiring first 2 AEs. Goal: $600k ARR this year. Output: a Sales Comp Plan Pack with OTE/pay mix, quotas+ramp, commission mechanics, and a rep-facing FAQ.”

**Example 2 (retention-aligned comp, churn problem):**
“Use `sales-compensation`. Reps optimize for bookings and we churn in the first 90 days. We want comp to reflect retention/NRR without being overly complex. Output: a Sales Comp Plan Pack with a retention-alignment addendum and clear admin rules.”

**Boundary example (redirect to legal counsel):**
“Write a legally binding compensation agreement for California employees and tell me what’s compliant.”
Response: explain this skill produces a comp-plan spec and rep-facing materials, but legal/compliance review must be done by qualified counsel.

**Boundary example (redirect to building-sales-team):**
“We need to figure out what roles to hire, how to interview them, and how much to pay them.”
Response: the org design, scorecards, and hiring process belong to `building-sales-team`. Use this skill specifically for the comp plan (OTE, quotas, commission mechanics) once you know which roles you are hiring.
