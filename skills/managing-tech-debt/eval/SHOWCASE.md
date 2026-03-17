# Showcase: Managing Tech Debt

> Demonstrates the value of the `managing-tech-debt` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `managing-tech-debt`. System: `checkout-service` (Node + Postgres). Pain: weekly incidents from timeouts + slow releases. Horizon: 8 weeks. Constraint: 2 engineers available, on-call load high. Output: Tech Debt Management Pack with a prioritized register and 3 milestones.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8 sections: executive summary, register (15 items), prioritization rationale, capacity planning, 3 milestones, risks, governance, and definition of done | 9 sections: context snapshot, register (15 items with detailed schema), scoring model + prioritized list, strategy decision memo, execution plan, migration/rollback plan, metrics plan, stakeholder cadence, and risks/open questions |
| Completeness | Solid coverage of the essentials with clear milestone tasks, owners, and done criteria; includes a governance section and plan-level success definition | Significantly more detailed: includes a formal strategy decision memo (refactor vs rebuild vs migrate), per-item rollback mechanisms, baseline + target metrics with confidence levels, instrumentation gap analysis, and stakeholder update templates |
| Actionability | Each milestone has a task table with owner, week, effort, and done criteria; decision rules are concise and clear | Each milestone has acceptance criteria AND stop/rollback conditions; includes a capacity model (80 engineer-days - on-call tax), specific "small tests to validate value," and per-change rollback triggers |
| Specificity | Register items have severity/effort/priority columns; milestone tasks reference specific techniques (CONCURRENTLY index creation, circuit breaker thresholds) | Register items have a 10-column schema including user impact, reliability risk, velocity tax, effort range, dependencies, owner, and recommended strategy; scoring model uses a 4-dimension composite with explicit tie-breaking rules |
| Quality gates | Plan-level definition of done with 6 success criteria | 8-category checklist plus a 7-dimension rubric scoring 26/28 with per-dimension rationale |

## Key Differences

1. **Strategy decision memo.** The skill output includes a formal decision memo evaluating three options (incremental refactor, strangler-fig migration, full rewrite) with pros, cons, and evaluation criteria. This makes the "refactor in place" decision explicit and defensible. The baseline implicitly assumes refactoring without documenting the alternatives considered.

2. **Register depth and scoring model.** The skill version's register uses a consistent 10-column schema per item and scores each on 4 dimensions (user impact, reliability risk, velocity tax, effort) with a composite score. Dependencies between items are mapped (e.g., "ID 4 tests needed before ID 6 modularization"). The baseline's register is simpler (6 columns) and uses P0-P3 labels without a transparent scoring methodology.

3. **Rollback mechanisms per change.** The skill output specifies a rollback mechanism and quantified trigger for every single change (e.g., "Drop index if write latency increases > 20%," "Disable circuit breaker via feature flag if incorrectly trips"). The baseline mentions rollback strategies generally but does not map them to individual items.

4. **Metrics plan with baselines and instrumentation gaps.** The skill version provides a comprehensive metrics plan with estimated current baselines (including confidence levels), 8-week targets, stretch targets, leading indicators, guardrails, and 5 instrumentation gaps with remediation plans and owners. The baseline lists KPIs and daily tracking metrics but without baseline estimates or instrumentation gap analysis.

5. **Stakeholder cadence and decision gates.** The skill output defines a weekly stakeholder update format (5 bullets + metrics snapshot), three decision gates at milestone boundaries, and specific questions for each gate. The baseline has a governance section with weekly check-ins and milestone demos but without structured update templates or gate questions.

## Verdict

The baseline delivers a clean, practical tech debt plan that a team could execute immediately. The skill-guided version adds substantial rigor through its strategy decision memo, transparent scoring model, per-change rollback plans, metrics baseline analysis, and stakeholder communication structure. For a 2-engineer team with high on-call load, the skill version's explicit capacity model and stop conditions provide critical safety nets that reduce execution risk.

## With Skill Output

<details>
<summary>Expand full output (~30k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~9k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
