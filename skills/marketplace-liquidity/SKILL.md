---
name: "marketplace-liquidity"
description: "Diagnose and improve marketplace liquidity: metric tree, fragmentation map, bottleneck diagnosis."
---

# Marketplace Liquidity Management

## Scope

**Covers**
- Defining **liquidity as reliability**: how often a user can complete the marketplace’s core action (find → match → transact) within an acceptable time and quality threshold
- Measuring liquidity **where it actually happens** (by “local markets” like geo × category × time window), not just in global averages
- Diagnosing liquidity failure modes: **fragmentation**, supply–demand imbalance (“flip-flop”), matching/mechanics issues, and quality/trust breakdowns
- Designing a practical **liquidity operating system**: scorecards, weekly review cadence, and a “whac-a-mole” rebalancing plan (move attention/inventory/incentives)
- Producing an actionable **experiment backlog** to improve liquidity (supply, demand, matching, pricing/incentives, trust & safety)

**When to use**
- “We need to improve marketplace liquidity / match rate / fill rate”
- “Time-to-match is too slow” / “buyers can’t find availability”
- “Supply and demand are imbalanced across cities/categories”
- “Our marketplace feels unreliable” / “conversion drops due to no availability”
- “We need a liquidity dashboard + operating cadence + experiments”

**When NOT to use**
- You don’t operate a two-sided marketplace (no matching between supply and demand).
- The primary problem is **value proposition / ICP** (use `problem-definition` or `measuring-product-market-fit`).
- You only need **pricing changes** (use `pricing-strategy`) without a liquidity diagnosis.
- You need a general growth plan unrelated to matching reliability (use `designing-growth-loops` / `retention-engagement`).
- You want to measure whether you have product-market fit (use `measuring-product-market-fit`); liquidity assumes the core value proposition is already validated.
- You need to design or optimize a referral/viral/content growth loop (use `designing-growth-loops`); this skill focuses on match reliability, not acquisition loops.
- You need a retention or engagement playbook for a non-marketplace product (use `retention-engagement`).

## Inputs

**Minimum required**
- Marketplace type + sides (who are “buyers” and “sellers”)
- The **core action** you consider a successful outcome (e.g., request → booked; search → purchase; message → hire)
- Top 1–3 priority segments (geo/category/user cohort) and the time window you care about
- Best-available baseline metrics (even if rough): demand volume, supply availability, match/fill rate, time-to-match, cancellations/quality
- Constraints: budget, incentives you can/can’t use, policy/brand/trust, engineering capacity, timebox

**Missing-info strategy**
- Ask up to 5 questions from [references/INTAKE.md](references/INTAKE.md), then proceed.
- If data is missing, proceed with explicit assumptions and label confidence.
- Do not request secrets or PII; prefer aggregated metrics or redacted examples.

## Outputs (deliverables)

Produce a **Marketplace Liquidity Management Pack** (Markdown in-chat; or as files if requested) containing:

1) **Context snapshot** (goal, timebox, segments, constraints, decision this informs)
2) **Liquidity definition + thresholds** (reliability definition and “good enough” targets)
3) **Liquidity metric tree** (north-star + driver metrics, with event definitions)
4) **Fragmentation map + segment scorecard** (where liquidity is weak/strong; the “local markets” that matter)
5) **Bottleneck diagnosis** (supply vs demand vs matching/mechanics vs quality; include “flip-flop” state)
6) **Intervention plan + prioritized experiment backlog** (including reallocation/“whac-a-mole” plan)
7) **Measurement + instrumentation plan** (dashboards, alerts, tracking gaps)
8) **Operating cadence** (weekly liquidity review agenda + owners)
9) **Risks / Open questions / Next steps** (always included)

Templates and expanded guidance:
- [references/TEMPLATES.md](references/TEMPLATES.md)
- [references/WORKFLOW.md](references/WORKFLOW.md)
- [references/CHECKLISTS.md](references/CHECKLISTS.md)
- [references/RUBRIC.md](references/RUBRIC.md)

## Workflow (7 steps)

### 1) Intake + define the decision and local market(s)
- **Inputs:** User context; [references/INTAKE.md](references/INTAKE.md).
- **Actions:** Clarify the goal (metric + target + by when), define the core action, pick the “local market” unit (e.g., city × category × week), and decide the decision this work will inform (what you’ll do differently).
- **Outputs:** Context snapshot + local market definition.
- **Checks:** A stakeholder can answer: “Which segment(s) improve by how much, by when, and what will we change based on the result?”

### 2) Define liquidity as reliability + set thresholds
- **Inputs:** Core action, time sensitivity, quality constraints (cancellations, refunds, etc.).
- **Actions:** Define liquidity as the probability of success within thresholds (time-to-match, quality). Choose 1 north-star liquidity metric and 3–6 drivers (fill rate/match rate, time-to-match, availability, acceptance, cancellation).
- **Outputs:** Liquidity definition + “good enough” targets + metric tree outline.
- **Checks:** The definition is measurable, segmentable, and aligned to the user’s experience (“reliability”).

### 3) Build a segment scorecard + diagnose fragmentation
- **Inputs:** Baseline data by geo/category/time window (best available).
- **Actions:** Create a segment scorecard for each local market: demand, supply, matching, and quality metrics. Identify fragmentation (thin markets, long tail categories, uneven geo distribution) and “uniform needs” vs heterogeneous needs.
- **Outputs:** Fragmentation map + ranked list of worst segments (where liquidity blocks growth).
- **Checks:** The scorecard avoids global averages and includes enough volume to be meaningful (or flags low-confidence segments).

### 4) Diagnose bottlenecks (flip-flop + mechanics + quality)
- **Inputs:** Segment scorecard; any qualitative evidence (support tickets, user feedback, ops notes).
- **Actions:** For each priority segment, label the primary failure mode:
  - **Supply-limited** (not enough availability/inventory)
  - **Demand-limited** (not enough intent/requests)
  - **Matching/mechanics-limited** (ranking, discovery, response time, pricing friction)
  - **Quality/trust-limited** (cancellations, no-shows, fraud, low ratings)
  Also check for the “flip-flop” dynamic (which side is currently the constraint) and the **graduation problem** (top suppliers leaving).
- **Outputs:** Bottleneck diagnosis per segment + evidence notes.
- **Checks:** Each diagnosis includes at least 1 metric signal and 1 plausible causal story you can test.

### 5) Generate interventions + experiment backlog (including reallocation)
- **Inputs:** Bottleneck diagnosis; constraints; available levers.
- **Actions:** Create intervention options for each bottleneck type (supply, demand, mechanics, quality). Include a “whac-a-mole” plan: how you will reallocate attention/inventory/incentives across segments weekly. Convert interventions into experiments with clear hypotheses and success metrics.
- **Outputs:** Prioritized experiment backlog + reallocation playbook.
- **Checks:** Every experiment has (a) a segment, (b) a primary metric, (c) a target effect size or directional expectation, and (d) a plausible cycle time.

### 6) Design measurement + liquidity operating cadence
- **Inputs:** Chosen metrics and experiments.
- **Actions:** Specify dashboards/alerts, event definitions, and instrumentation gaps. Create a weekly liquidity review agenda and decision log (what gets rebalanced, what gets shut down, what gets scaled).
- **Outputs:** Measurement plan + operating cadence (owners if known).
- **Checks:** Each key metric is tied to a data source and update frequency; the cadence produces concrete decisions, not status updates.

### 7) Quality gate + finalize the pack
- **Inputs:** Draft pack; [references/CHECKLISTS.md](references/CHECKLISTS.md) and [references/RUBRIC.md](references/RUBRIC.md).
- **Actions:** Run the checklist and score with the rubric. Tighten the pack until it is specific, segment-aware, and testable. Always include **Risks / Open questions / Next steps**.
- **Outputs:** Final Marketplace Liquidity Management Pack.
- **Checks:** The next 2 weeks of work are unblocked (data pulls, 1–3 experiments, cadence).

## Anti-patterns

1. **Global-average blindness** — Reporting a single marketplace-wide match rate instead of segmenting by local market (geo x category x time). A 70% global fill rate can hide a 30% rate in your fastest-growing city. Always segment before diagnosing.
2. **Supply-side-only tunnel vision** — Assuming liquidity problems are always supply shortages. Many marketplaces have adequate supply but poor matching/discovery mechanics or quality/trust breakdowns that suppress conversion.
3. **Incentive addiction without diagnosis** — Throwing subsidies or promotions at both sides without first identifying whether the bottleneck is supply, demand, mechanics, or quality. This burns budget and masks the real constraint.
4. **Ignoring the flip-flop dynamic** — Treating the supply/demand balance as static. Marketplaces oscillate: today's supply shortage becomes tomorrow's demand shortage once you over-correct. The operating cadence must track which side is currently the constraint.
5. **Fragmentation denial** — Treating heterogeneous local markets as one uniform market. A marketplace with 50 categories where 5 drive 90% of volume needs a long-tail strategy, not a blanket growth plan.

## Quality gate (required)
- Use [references/CHECKLISTS.md](references/CHECKLISTS.md) and [references/RUBRIC.md](references/RUBRIC.md).
- Always include: **Risks**, **Open questions**, **Next steps**.

## Examples

**Example 1 (services marketplace, geo fragmentation):**  
“Use `marketplace-liquidity`. We run a home cleaning marketplace across 12 cities. Goal: increase booking fill rate from 62% → 80% in 8 weeks in our bottom 4 cities. We suspect supply is thin and response times are slow. Output a Marketplace Liquidity Management Pack with a segment scorecard, bottleneck diagnosis, and a prioritized experiment backlog.”

**Example 2 (B2B marketplace, category imbalance):**  
“Use `marketplace-liquidity`. We match startups with freelance designers. Liquidity is strong in ‘logo design’ but weak in ‘product design’ and ‘brand refresh.’ Goal: cut median time-to-first-qualified-match from 5 days to 2 days for product design in 60 days. Provide a liquidity metric tree, fragmentation map, and operating cadence.”

**Boundary example (not a liquidity problem — acquisition copy):**
“Write Google Ads copy to get more buyers.”
Response: this is primarily acquisition/copy. If marketplace reliability is already strong, use `copywriting` / channel-specific growth work. If reliability is unknown, start with an intake to confirm a liquidity bottleneck first.

**Boundary example (redirect to measuring-product-market-fit):**
“We launched a pet-sitting marketplace 3 months ago. Do we even have product-market fit?”
Response: This is a PMF measurement question, not a liquidity diagnosis. Use `measuring-product-market-fit` to run a Sean Ellis survey and retention analysis first. Once PMF is confirmed for at least one segment, return here to optimize match reliability.
