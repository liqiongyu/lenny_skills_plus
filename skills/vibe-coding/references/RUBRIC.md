# Rubric (score 1–5 per category)

Suggested bar for “demo-ready”: average ≥ 4.0 and no category below 3.

## 1) Demo clarity and scope control
1 = No demo promise; scope is “everything”
2 = Demo promise exists but is vague (“show the app”); non-goals not listed; fake-vs-real decisions absent
3 = Demo promise exists; some non-goals; partial fake-vs-real decisions
4 = Demo promise is specific and observable; non-goals listed; fake-vs-real mostly decided; timebox may be tight
5 = Crisp demo promise; strong non-goals; explicit fake-vs-real; timebox is realistic

## 2) Prototype contract quality (spec + acceptance)
1 = Vague requirements; no acceptance criteria
2 = User flow described at high level; acceptance criteria missing or subjective (“looks good”)
3 = Basic flow and acceptance criteria; missing edge cases
4 = Flow, components, and data shape defined; acceptance criteria are observable; 1-2 gaps in edge cases
5 = Clear flow, components, data shape, and observable acceptance criteria for every user-visible step

## 3) Vibe coding execution loop quality
1 = Random prompting; no checkpoints; large diffs
2 = Prompts exist but are not structured into slices; validation happens only at the end
3 = Some structure; occasional validation; incomplete logging
4 = Sliced task board with validation per slice; logging exists but inconsistent; failures mostly tracked
5 = Tight loop: plan then small diff then run/verify then log; failures become tasks; progress is predictable

## 4) Safety and robustness
1 = Secrets or risky operations; no rollback
2 = No secrets exposed but no confirmation gates for destructive operations; rollback plan absent
3 = Some guardrails; partial rollback/runbook
4 = Least privilege applied; confirmation gates for risky actions; rollback exists but runbook has gaps
5 = Least privilege; no secrets; confirmation gates for risky actions; rollback and runbook are clear

## 5) Demo readiness and handoff
1 = Only works on the creator’s machine; no demo narrative
2 = Runs on the creator’s machine with setup; demo script is a bullet list of features, not a narrative
3 = Runs with help; basic demo script
4 = Runs from clean start with documented steps; demo script has a narrative arc; no backup plan
5 = Runs from clean start; demo script is clear; backup plan exists; next steps are prioritized

