# Rubric (Shipping & Launch Pack)

Score each dimension **0/1/2**.

- **0** = missing or unusable
- **1** = present but incomplete
- **2** = clear, executable, decision-ready

Suggested passing bar: **>= 10/14**. No dimension at 0.

## Dimensions

## 1) Clarity of release (0–2)
- **0:** Unclear what is shipping or to whom; no release description.
- **1:** Release is described but scope boundaries are fuzzy; audience or platforms/regions missing.
- **2:** One-liner, audience, platforms/regions, and non-goals are all explicit.

## 2) Rollout + rollback quality (0–2)
- **0:** “Ship to everyone” with no rollback plan or kill switch.
- **1:** Rollout phases exist but rollback steps are vague or stop-the-line triggers are missing.
- **2:** Phased rollout with eligibility criteria, kill switch, rollback steps, and explicit stop-the-line triggers.

## 3) Quality bar / PQL (0–2)
- **0:** No explicit quality bar or stop-ship criteria.
- **1:** Checklist exists but includes vague items (“test thoroughly”); ownership is unclear.
- **2:** Measurable stop-ship criteria with owners; known risks and mitigations listed.

## 4) Measurement + monitoring (0–2)
- **0:** No plan to detect regressions or measure success.
- **1:** Metrics defined but monitoring/alerts are incomplete; no alert thresholds or dashboard owners.
- **2:** Success metrics + guardrails defined; dashboards/alerts owned; thresholds explicit.

## 5) Comms + enablement (0–2)
- **0:** No comms plan; internal teams will learn about the launch from customers.
- **1:** Comms drafted but incomplete; enablement materials (docs, support readiness) missing.
- **2:** Internal and external comms ready; docs/support enablement included; every audience knows what changed and what to do.

## 6) Execution readiness (0–2)
- **0:** No runbook; launch is ad hoc with no defined roles or timeline.
- **1:** Some execution notes exist but roles, timing, or escalation path are unclear.
- **2:** Launch runbook with timeline, roles, and escalation path; go/no-go is checklist-based.

## 7) Learning loop (0–2)
- **0:** No plan to learn or improve after launch.
- **1:** Post-launch retro is mentioned but not scheduled; no PQL update plan.
- **2:** Post-launch review scheduled with owner; hypotheses and follow-ups defined; PQL update plan included.

## Passing bar (recommended)
- **No open “stop-ship” items** on [CHECKLISTS.md](CHECKLISTS.md).
- Score **>= 10/14** with no dimension at 0.
- If risk is high (permissions, money movement, availability), require: rollout+rollback = 2 and monitoring = 2.

