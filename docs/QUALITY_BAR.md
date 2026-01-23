# Quality bar for generated skills

> 中文版: `QUALITY_BAR.zh-CN.md`

A generated skill pack is “good” only if it is executable by an agent under uncertainty.

Mandatory:
- Clear boundary (when to use / when not to use)
- Explicit input contract + missing-info handling
- Explicit output contract (deliverables)
- 5–9 step workflow, each step has:
  - Inputs
  - Actions
  - Outputs
  - Checks / “definition of done”
- Progressive disclosure:
  - SKILL.md stays short and navigates to references
- At least:
  - 2 positive examples (good prompts)
  - 1 negative/boundary example (when NOT to use)

Nice to have:
- A question bank for intake
- A rubric with pass/fail thresholds
- Templates that generate files (PRD, email, experiment plan, etc.)
- Simple “lint” scripts or validation scripts

Red flags:
- Vague advice (“consider”, “think about”, “it depends”) without artifacts
- No explicit deliverables
- No quality gates
- One giant wall of text in SKILL.md
