# Rubric (Technical Roadmaps)

Score each dimension 1–5. A strong pack is **≥4** on most dimensions and **no 1s**.

## 1) Diagnosis quality
1: Vague ("we need to improve reliability") with no evidence.
3: Some evidence, but missing key constraints or "why now".
5: Specific constraints with clear evidence and urgency.

**0/1/2 boundary guide:**
- **0 (fail):** Diagnosis is absent or a single vague sentence with no data, incidents, or architectural evidence cited.
- **1 (borderline):** Diagnosis names problems but relies on generalities ("performance is slow"); lacks quantified signals (latency percentiles, incident counts, cost trends) or omits "why now" urgency.
- **2 (pass):** Diagnosis cites 3+ specific evidence points (e.g., P99 latency, incident frequency, scaling limits), explicitly states constraints, and explains why acting this quarter is necessary.

## 2) Guiding policy coherence
1: A list of slogans; doesn't constrain choices.
3: Some principles, but too many or inconsistent.
5: 3–5 crisp principles that clearly drive decisions.

**0/1/2 boundary guide:**
- **0 (fail):** No guiding policy, or policy is a list of aspirational slogans ("move fast", "be reliable") that do not constrain any initiative choice.
- **1 (borderline):** 1-2 principles are stated but they are too broad to distinguish which initiatives belong on the roadmap vs. off; or there are 6+ competing principles with no prioritization.
- **2 (pass):** 3-5 principles are stated, each clearly ruling something in or out; a reader could use them to resolve a prioritization tie between two candidate initiatives.

## 3) Actionability of coherent actions
1: Wishlist; no owners, deps, or milestones.
3: Some execution detail, but sequencing unclear.
5: Executable plan with owners, deps, milestones, and decision gates.

**0/1/2 boundary guide:**
- **0 (fail):** Actions are a bullet list of themes ("improve observability", "reduce tech debt") with no owners, no timelines, and no dependencies mapped.
- **1 (borderline):** Actions have some detail (rough effort, partial owners) but sequencing rationale is missing; a team lead could not start execution without asking follow-up questions.
- **2 (pass):** Each action has an owner, milestone dates, dependency links, and high-uncertainty items include a decision gate (spike/RFC/prototype) before full commitment.

## 4) Alignment and stakeholder usefulness
1: Written for the wrong audience; no decision ask.
3: Audience is implied; decisions unclear.
5: Audience + decision are explicit; stakeholders can approve/critique async.

**0/1/2 boundary guide:**
- **0 (fail):** Audience is never stated; document mixes detail levels (low-level implementation details for execs, or vague themes for the executing team); no decision ask is articulated.
- **1 (borderline):** Audience is mentioned but the document's depth/format does not match (e.g., too technical for a VP audience); decision ask is implicit or buried.
- **2 (pass):** Audience and decision are stated in the first section; the document's depth matches the audience; a stakeholder could approve, critique, or request changes asynchronously without a meeting.

## 5) Feasibility and trade-offs
1: Ignores capacity/constraints; no trade-offs.
3: Mentions constraints, but doesn't change plan.
5: Plan reflects constraints; non-goals/cut list is explicit.

**0/1/2 boundary guide:**
- **0 (fail):** No mention of capacity, headcount, or competing priorities; the roadmap implies unlimited resources; no items are cut or deprioritized.
- **1 (borderline):** Constraints are listed somewhere but the roadmap itself does not visibly reflect them (e.g., 20 initiatives for a 5-person team with no phasing); non-goals exist but are vague.
- **2 (pass):** The roadmap explicitly scopes to available capacity; a cut list or "not now" section names specific items that were deprioritized and why; trade-offs between competing initiatives are stated.

## 6) Measurability and risk management
1: No success metrics; risks missing.
3: Some metrics/risks, but shallow or unowned.
5: Metrics (baseline → target) + risk register with owners and mitigations.

**0/1/2 boundary guide:**
- **0 (fail):** No success metrics for any initiative; risks section is absent or contains only "things might be late."
- **1 (borderline):** Metrics are listed but lack baselines or targets (e.g., "improve latency" without current P99 or target); risks are named but have no owners or mitigations.
- **2 (pass):** Each top initiative has at least one metric with baseline and target (e.g., "P99 latency from 800ms to 200ms"); risk register includes 3+ risks with owner, likelihood, impact, and mitigation plan.

## Ship / no-ship guidance
- **Ship:** No 1s, and at least four dimensions are 4–5.
- **Revise:** Any 1, or more than two dimensions at 3 or below.

