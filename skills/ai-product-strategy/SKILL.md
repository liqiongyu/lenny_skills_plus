---
name: "ai-product-strategy"
description: "Create an AI Product Strategy Pack (thesis, use cases, system plan, eval plan, roadmap)."
---

# AI Product Strategy

## Scope

**Covers**
- Defining an executable product strategy for an AI/LLM/agent product or AI feature portfolio
- Translating AI uncertainty (non-determinism, emergent risks) into an empirical plan with evals + instrumentation
- Choosing product form factor (assistant vs copilot vs agent), autonomy boundaries, and a safety/security posture
- Setting kill criteria so you know when to pivot or stop investing
- Producing a strategy pack leaders and teams can use to align and execute

**When to use**
- "Define our AI product strategy / LLM strategy / agent strategy."
- "Prioritize AI use cases and turn them into an AI roadmap."
- "We're adding AI to an existing product—what should we build and how do we measure it?"
- "We want to ship an agent; define autonomy, security, and rollout."
- "Should we keep investing in our AI feature, or kill it?"

**When NOT to use**
- You need to **build/implement** an LLM system (RAG pipeline, prompt engineering, tool use) → use `building-with-llms`.
- You need to **evaluate a specific AI vendor or tool** (Claude vs GPT, build vs buy for one tool) → use `evaluating-new-technology`.
- You need to **design an AI platform for third-party developers** (APIs, ecosystem, marketplace) → use `platform-strategy`.
- You need to **rapidly prototype** an AI demo/proof-of-concept → use `vibe-coding`.
- You need a long-term product/company **vision** → use `defining-product-vision` first.
- You need deep **competitor research**, battlecards, or win/loss → use `competitive-analysis`.
- You need a feature-level **PRD/spec/design doc** → use `writing-prds` / `writing-specs-designs` after strategy.
- You don't yet have a clear **problem/ICP hypothesis** → use `problem-definition` / `conducting-user-interviews`.

## Inputs

**Minimum required**
- Product context (what exists today) + target customer/user + their job/pain
- Strategy horizon (default: 3–12 months) + constraints (budget, latency, policy/legal, data access, platform)
- Intended AI surface and scope: assistant / copilot / agent; where it lives in the workflow
- Success metrics (1–3) and guardrails (2–5), including safety/trust, cost, and latency

**Missing-info strategy**
- Ask up to 5 questions from [references/INTAKE.md](references/INTAKE.md) (3–5 at a time).
- If details remain missing, proceed with clearly labeled assumptions and provide 2–3 options (use-case focus, autonomy level, build/buy).

## Outputs (deliverables)

Produce an **AI Product Strategy Pack** in Markdown (in-chat; or as files if requested), in this order:

1) **Context snapshot** (decision, users, constraints, why now)
2) **Strategy thesis** (value prop, why-now, differentiation, non-goals)
3) **Use-case portfolio** (prioritized opportunities with feasibility + risk)
4) **Autonomy policy** (assistant→copilot→agent boundaries + human control points)
5) **System plan** (build/buy, data plan, eval plan, cost/latency budgets)
6) **Empirical learning plan** (experiments, instrumentation, iteration cadence)
7) **Roadmap** (phases, milestones, exit criteria, owners)
8) **Kill criteria** (when to pivot or stop; sunk-cost guardrails)
9) **Risks / Open questions / Next steps** (always included)

Templates: [references/TEMPLATES.md](references/TEMPLATES.md)

**Quick mode:** If the user needs a lightweight strategy (single feature, early exploration, or time-boxed to <1 hour), produce items 1–3 + 7 + 9 and note which sections were skipped. The user can expand later.

## Workflow (8 steps)

### 1) Frame the decision and boundaries
- **Inputs:** User request + constraints.
- **Actions:** Define the decision to make, strategy horizon, and audience. Decide whether this is for a single feature, a product line, or a platform capability. Write 3–5 explicit non-goals. Determine if quick mode or full mode is appropriate.
- **Outputs:** Draft **Context snapshot** + **scope boundaries**.
- **Checks:** You can state "We are deciding X by date Y for audience Z," and list what's explicitly out of scope.

### 2) Map the user workflow and role shift
- **Inputs:** Target user + current workflow.
- **Actions:** Map the workflow steps where AI changes the user's job. Note "human control points" (where a user must review/approve). Identify the 3–5 trust-destroying failure modes that matter most (hallucination, privacy leaks, incorrect actions, bias, cost blowouts).
- **Outputs:** Workflow notes + role-shift bullets (in thesis or appendix).
- **Checks:** Value is tied to a real workflow step (not generic "AI magic"). Each failure mode has a named consequence.

### 3) Build a use-case portfolio and prioritize bets
- **Inputs:** Workflow map + constraints + risk appetite.
- **Actions:** List 6–12 candidate use cases. Score value vs feasibility vs risk. Select the top 1–3 bets and 1 "explore later" bet. For each rejected candidate, note why it was cut (this prevents revisiting dead ends later).
- **Outputs:** **Use-case portfolio** table + recommendation.
- **Checks:** Each selected bet has a clear user, measurable outcome, and known "must-not-do" constraints.

### 4) Define differentiation + "why us / why now"
- **Inputs:** Top bets + assets + market context.
- **Actions:** Draft the strategy thesis: value prop, why-now, and defensible differentiation. Differentiation must come from compounding advantages (data moat, distribution, workflow integration, UX, trust)—not from model choice or "we use AI." Write key assumptions and how you'll test them.
- **Outputs:** **Strategy thesis** (copy/paste from template).
- **Checks:** Differentiation names at least 2 compounding advantages. Assumptions each have a test + metric + owner.

### 5) Choose form factor and autonomy policy (assistant → copilot → agent)
- **Inputs:** Bets + constraints + safety requirements.
- **Actions:** Start with the minimum autonomy needed for utility (don't default to agent). Specify what the system can do, what it can suggest, and what it must never do. Define permission prompts, approvals, logging, and rollback for any action-taking behavior. Include a plan for prompt injection / tool misuse.
- **Outputs:** **Autonomy policy** table.
- **Checks:** Every action capability has explicit permissions + auditability + rollback. There's a "must never do" list enforced via product + policy + evals.

### 6) Draft the system plan (build/buy, data, evals, budgets)
- **Inputs:** Autonomy policy + constraints + data access.
- **Actions:** Choose a strategy-level technical approach (e.g., RAG, tool use, fine-tuning, multi-agent) and a data plan. Define eval strategy (offline + online), quality targets, and cost/latency budgets. Acknowledge non-determinism and plan for variance (fallbacks, guardrails, routing).
- **Outputs:** **System plan**.
- **Checks:** There's a plausible path to meet quality + safety + cost + latency with measurable evals.

### 7) Make it empirical (experiments + instrumentation + iteration)
- **Inputs:** Thesis + system plan + assumptions.
- **Actions:** Design experiments/prototypes and a "watch/listen" plan post-launch (per Nick Turley: if you don't stop, and watch, and listen, you'll miss both utility and risks). Define instrumentation (events/logs), review cadence, and an iteration loop for both utility and risk.
- **Outputs:** **Empirical learning plan**.
- **Checks:** Every major assumption has a test + metric + owner + timebox. Instrumentation covers both utility signals and risk/safety signals.

### 8) Roadmap + kill criteria + quality gate + finalize
- **Inputs:** Full draft pack.
- **Actions:**
  1. Create a phased roadmap (Prototype → Internal → Beta → GA) with milestones, exit criteria, and owners.
  2. Define **kill criteria**: the conditions under which you'd stop investing, pivot direction, or scale back autonomy. This prevents sunk-cost traps. Examples: "If <metric> hasn't reached X after Y weeks, we stop/pivot."
  3. Run [references/CHECKLISTS.md](references/CHECKLISTS.md) and score with [references/RUBRIC.md](references/RUBRIC.md).
  4. Always add **Risks / Open questions / Next steps**.
- **Outputs:** Final **AI Product Strategy Pack**.
- **Checks:** A stakeholder can act on the pack without a meeting; trade-offs and unknowns are explicit; there's a clear "what would make us stop."

## Quality gate (required)
- Use [references/CHECKLISTS.md](references/CHECKLISTS.md) and [references/RUBRIC.md](references/RUBRIC.md).
- Always include: **Risks**, **Open questions**, **Next steps**.

## Examples

**Example 1 (AI-first product):** "Use `ai-product-strategy` to define strategy for an AI coding assistant for mid-market engineering teams. Constraints: ship a beta in 8 weeks; must not leak proprietary code; budget capped at $X/month."
Expected: strategy thesis + prioritized use cases + autonomy policy + system/eval plan + roadmap + kill criteria.

**Example 2 (AI feature portfolio):** "Use `ai-product-strategy` to prioritize AI opportunities for a customer support platform. Decide copilot vs agent, include safety posture, and propose a 2-quarter roadmap."
Expected: use-case portfolio with 1–3 bets, a clear agency-control policy, empirical plan, and phased roadmap with exit criteria.

**Example 3 (Quick mode):** "I have 30 minutes—give me a lightweight AI strategy for adding summarization to our internal wiki."
Expected: context snapshot + 3–5 use cases scored in a table + phased roadmap + risks/next steps. Note that autonomy policy and system plan were skipped and should be done before build.

**Boundary example:** "Pick the best LLM provider."
Response: this is a vendor evaluation, not a product strategy—use `evaluating-new-technology`. If the broader product decision is unclear, offer to run this strategy workflow first to define what you need from a provider.

## Common anti-patterns (avoid these)

1. **"We use AI" as differentiation.** If your only moat is "we added an LLM," anyone can copy you in weeks. Push for data, distribution, or workflow advantages.
2. **Agent-first without permissions.** Defaulting to maximum autonomy before validating with copilot mode. Start with suggest, graduate to act.
3. **No evals = no strategy.** A strategy without measurable quality targets and offline evals is a wish list. Non-deterministic systems require empirical validation.
4. **Ignoring the cost curve.** AI inference costs are real. A strategy that doesn't model cost-per-user or cost-per-task will hit a wall at scale.
5. **"We'll iterate" without a plan.** Iteration requires instrumentation, review cadence, and decision rules—not just good intentions.
