# Skill Optimization Workflow

Standard workflow for optimizing an existing skill pack using the `/skill-creator` eval loop.

## Prerequisites

- Skill already exists at `skills/<slug>/` with SKILL.md + references/
- Original Refound source at `sources/refound/raw/<slug>/SKILL.md` (if available)
- Branch created for the optimization work

## Workflow (6 Steps)

### Step 1: Snapshot baseline

```bash
mkdir -p <slug>-workspace/skill-snapshot
cp -r skills/<slug>/* <slug>-workspace/skill-snapshot/
```

This preserves the old version for A/B comparison.

### Step 2: Gap analysis

Read both versions (original Refound source + current skill pack) and analyze:

1. **What the current version does well** — structure, workflow completeness, safety coverage, insight conversion rate
2. **What's missing or weak** — disambiguation with neighboring skills, missing deliverables, template actionability, rubric calibration, example coverage
3. **Boundary clarity** — does the description correctly trigger for in-scope prompts and NOT trigger for neighboring skills?

Identify the neighboring/confusable skills by checking the skill's category and related topics.

### Step 3: Draft improvements

Apply improvements to these files:

**SKILL.md** (main changes):
- **Description**: Add `NOT for` clauses referencing specific neighboring skills
- **Scope**: Expand "When NOT to use" with explicit skill redirects
- **Deliverables**: Add any missing deliverables (e.g., kill criteria, quick mode)
- **Workflow**: Sharpen checks, add failure mode awareness, reference source insights
- **Examples**: Add boundary example showing correct redirect + anti-pattern example
- **Anti-patterns**: Add 3-5 common failure modes to avoid (if applicable)

**references/RUBRIC.md**:
- Add specific 0/1/2 boundary definitions for each scoring dimension
- Each level should be concrete enough that two reviewers would agree

**references/TEMPLATES.md**:
- Add templates for any new deliverables
- Consider adding a "quick mode" subset if applicable

**Lint after editing:**
```bash
python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<slug>
```

### Step 4: Design test prompts (3 cases)

Create 3 test prompts covering different scenarios:

| # | Type | Purpose |
|---|------|---------|
| 1 | **Full execution** | Realistic, detailed prompt that exercises the complete workflow |
| 2 | **Variant / edge case** | Different scenario (quick mode, different industry, partial info) |
| 3 | **Boundary redirect** | Prompt that should be REJECTED and redirected to a neighboring skill |

Save to `<slug>-workspace/evals.json`.

### Step 5: Run evals (6 subagents in parallel)

For each of the 3 test prompts, launch 2 subagents simultaneously:

- **with_skill**: Uses the improved version at `skills/<slug>/`
- **old_skill**: Uses the snapshot at `<slug>-workspace/skill-snapshot/`

Each subagent:
1. Reads the SKILL.md and all references/
2. Follows the workflow to produce output
3. Saves to `<slug>-workspace/iteration-1/<eval-name>/<variant>/outputs/`

While subagents run, draft assertions for each eval (section presence, quality checks, boundary behavior).

When subagents complete:
1. Save `timing.json` for each run
2. Grade with assertions (programmatic script preferred)
3. Create `benchmark.json` with pass rates, tokens, duration
4. Generate eval viewer: `generate_review.py --static`

### Step 6: Review + commit

Present results to user. Key metrics to report:

| Eval | Improved | Baseline | Key Difference |
|------|----------|----------|----------------|
| Full execution | X/Y | X/Y | What's new |
| Variant | X/Y | X/Y | What's different |
| Boundary | X/Y | X/Y | Redirect accuracy |

If user approves:
1. Lint final check
2. Commit changes (only skill files, not workspace)
3. Push + create PR

## Improvement Patterns (reusable across skills)

### Common improvements that apply to most skills:

1. **NOT-for disambiguation** — Every skill should explicitly name 2-4 neighboring skills in the description
2. **Kill criteria / exit conditions** — Strategy and planning skills benefit from "when to stop" deliverables
3. **Quick mode** — Skills with >6 deliverables can offer a lightweight subset
4. **Anti-patterns** — 3-5 common failure modes specific to the skill's domain
5. **Rubric calibration** — Specific 0/1/2 boundaries instead of one-line descriptions
6. **Boundary examples** — Show what happens when a mismatched prompt arrives

### Improvements that depend on skill type:

| Skill Type | Likely Improvements |
|------------|-------------------|
| Strategy / Planning | Kill criteria, quick mode, anti-patterns |
| Execution / Process | Checklist sharpening, failure mode examples |
| Communication | Tone/audience awareness, format options |
| Career / Personal | Sensitivity guardrails, personalization |
| Sales / GTM | Stage-appropriate guidance, metric examples |

## File Structure

```
<slug>-workspace/
├── evals.json                          # Test prompts
├── skill-snapshot/                     # Old version (baseline)
│   ├── SKILL.md
│   └── references/
├── grade_all.py                        # Grading script
└── iteration-1/
    ├── <eval-name>/
    │   ├── eval_metadata.json          # Prompt + assertions
    │   ├── with_skill/
    │   │   ├── outputs/strategy-pack.md
    │   │   ├── timing.json
    │   │   └── grading.json
    │   └── old_skill/
    │       ├── outputs/strategy-pack.md
    │       ├── timing.json
    │       └── grading.json
    ├── benchmark.json
    └── review.html                     # Eval viewer
```
