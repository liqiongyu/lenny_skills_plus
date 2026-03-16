# Scoring Rubric (0/1/2)

Suggested passing bar: **≥ 16/20**.

## 1) Decision clarity (0–2)
- **0:** No decision statement; unclear what's being decided or for whom.
- **1:** Decision stated but missing horizon or audience; scope boundaries vague.
- **2:** Explicit "We are deciding X by date Y for audience Z" with clear non-goals.

## 2) Problem and "why now" (0–2)
- **0:** No problem statement or generic "AI is the future."
- **1:** Problem named but lacks user evidence; "why now" is hand-wavy.
- **2:** User-centered problem with 1–2 evidence points; concrete "why now" (capability shift, cost curve, regulation, market timing).

## 3) Differentiation (0–2)
- **0:** No differentiation or "we use AI" is the only moat.
- **1:** One advantage named but not defensible or compounding.
- **2:** 2+ defensible compounding levers (data, distribution, workflow, UX, trust); explains why these compound over time.

## 4) Strategy choices and non-goals (0–2)
- **0:** No explicit choices or non-goals.
- **1:** Choices listed but <3 non-goals or assumptions unlabeled.
- **2:** Clear choices + 3+ non-goals; assumptions labeled with tests, metrics, owners, timeboxes.

## 5) Use-case portfolio quality (0–2)
- **0:** Only 1–2 use cases considered; no scoring or comparison.
- **1:** Multiple candidates but top bets lack measurable outcomes or "must-not-do" constraints.
- **2:** 6–12 candidates scored; top 1–3 bets have clear user + workflow anchor + measurable outcome + constraints. Rejected candidates have a noted reason.

## 6) Autonomy policy quality (0–2)
- **0:** No mention of autonomy boundaries or form factor choice.
- **1:** Form factor chosen but missing approval model, audit, or rollback for action-taking.
- **2:** Explicit boundaries; every action capability has permissions + auditability + rollback. "Must never do" list exists. Prompt injection / tool misuse plan included.

## 7) Eval + measurement plan (0–2)
- **0:** No eval plan or only vague "we'll monitor."
- **1:** Either offline or online evals, but not both; missing risk/safety signals.
- **2:** Both offline (test set + critical failures) and online (quality + safety signals + cadence + owner). Non-determinism acknowledged with fallback plan.

## 8) Data + governance readiness (0–2)
- **0:** Data plan not mentioned.
- **1:** Data sources listed but prohibited data or governance constraints missing.
- **2:** Explicit sources + prohibited data + retention/access policy + privacy/compliance constraints.

## 9) Empirical learning plan quality (0–2)
- **0:** No experiments or "we'll iterate" without specifics.
- **1:** Experiments listed but missing decision rules, timeboxes, or owners.
- **2:** Every key assumption has experiment + success metric + guardrail metric + timebox + owner + decision rule. Rollout is staged and reversible.

## 10) Roadmap executability (0–2)
- **0:** Feature list without phases, criteria, or owners.
- **1:** Phased but missing exit criteria or risk retirement work.
- **2:** Phased (Prototype→Internal→Beta→GA) with entry/exit criteria, owners, risk retirement as first-class items, and kill criteria defined.
