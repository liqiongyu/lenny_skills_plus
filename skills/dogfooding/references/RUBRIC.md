# Rubric (Dogfooding Pack)

Score each dimension **0/1/2**.

- **0** = missing or unusable
- **1** = present but incomplete
- **2** = clear, executable, decision-ready

Suggested passing bar: **>= 7/10** with no dimension at 0.

## 1) Workflow realism (0–2)
- **0:** Scenarios are vague or feature-based (“test the dashboard”); no end-to-end “done” criteria.
- **1:** Scenarios are end-to-end but miss day-0 setup, creator reality, or edge cases; done criteria are informal.
- **2:** Scenarios reflect real user goals (including day-0 + edge cases) with measurable done criteria.

## 2) Participation + intensity (0–2)
- **0:** Dogfooding is optional, ad hoc, or has no cadence; participation is inconsistent.
- **1:** Regular sessions exist but are not sustained or not role-appropriate; “creator commitments” missing where relevant.
- **2:** Clear cadence with defined time commitment; “creator commitments” where relevant; daily use produces stable signal.

## 3) Evidence quality (0–2)
- **0:** Findings are opinions or vibes (“feels slow”); no repro steps, evidence, or severity ratings.
- **1:** Some issues have repro steps but many lack expected-vs-actual, severity, or scenario linkage.
- **2:** Issues are reproducible artifacts with evidence, severity, scenario linkage, and steps to reproduce.

## 4) Decision + follow-through (0–2)
- **0:** No triage process; no owners assigned; issues accumulate without dispositions.
- **1:** Triage happens but dispositions are inconsistent; weak linkage to scenario completion or ship gate.
- **2:** Triage produces clear dispositions (fix/schedule/won’t-fix), owners, and verified scenario-based improvements.

## 5) Safety + bias control (0–2)
- **0:** Uses real customer data unsafely; internal persona mismatch is ignored; no environment guardrails.
- **1:** Some guardrails exist (e.g., staging environment) but aren’t consistently enforced; bias from internal expertise is unacknowledged.
- **2:** Environment/data rules are clear and enforced; dogfooding limits are acknowledged; external feedback is planned to complement.

