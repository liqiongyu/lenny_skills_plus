# Showcase: Product Taste Intuition

> Demonstrates the value of the `product-taste-intuition` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `product-taste-intuition`. Domain: fintech onboarding. Target user: first-time user connecting their bank account and seeing their net worth dashboard for the first time. The user job is to feel confident their data is safe and see value within 2 minutes of connecting. Benchmarks: propose 4-5 (at least 2 outside fintech, e.g., best-in-class trust/identity flows). Time box: 90 minutes. Constraints: mobile-first, must meet accessibility AA, high-trust design required. Create a Taste Calibration Pack with benchmark study notes (3+ concrete moments per benchmark), 5-7 taste rules specific to fintech onboarding trust, falsifiable hypotheses about our current flow, and a validation plan (5-user task test + instrumentation). Output: Taste Calibration Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6 sections: benchmark selection, study notes, taste rules, hypotheses, validation plan, appendix matrix | 8-section canonical structure: taste calibration brief, benchmark set, product study notes with moments, taste rules + anti-patterns, intuition-to-hypothesis log, validation plan, practice plan, and risks/open questions |
| Completeness | 5 benchmarks with summary notes, 7 taste rules, 5 hypotheses, timed validation plan, and a benchmark-rule matrix | 5 benchmarks with 3-4 detailed moments each (19 total), 10 taste rules with 6 anti-patterns, 5 hypotheses with counter-signals and smallest viable tests, validation plan with 5 prioritized tests, and a 4-week practice cadence |
| Actionability | Hypotheses have measurement plans and falsification thresholds; validation plan is timed across 90 minutes | Each hypothesis specifies the smallest viable test, exact participant counts, success metrics with deltas, and decision rules for each outcome; includes a 4-week practice plan with weekly outputs |
| Specificity | Benchmark notes describe general patterns ("clean design," "progressive disclosure") without moment-level detail | Each benchmark has moment-by-moment analysis (what I did, what happened, emotion/friction, why it might work) with specific copy artifacts and pattern candidates |
| Quality gates | Benchmark-rule cross-reference matrix in appendix | Full checklist (pack completeness, taste rule quality, hypothesis quality, validation realism) plus rubric self-score (35/35) across 7 categories |

## Key Differences

1. **Moment-based observation depth.** The skill output documents 3-4 specific user moments per benchmark with a structured format (action, response, emotion, hypothesis). For example, Monarch M3 describes the net worth number animating from $0 to the actual figure at 32pt+ type, creating a "delight/confidence" emotion. The baseline describes Monarch's patterns in summary without this moment-level granularity.

2. **Anti-patterns as guardrails.** The with-skill output includes 6 named anti-patterns ("trust badge carpet," "skeleton of nothing," "data dump dashboard," "silent failure," "Hotel California settings," "legal-first copy") each with specific replacement rules tied to taste rules. The baseline provides do/don't rules but does not name and catalog anti-patterns separately.

3. **Intuition-to-hypothesis translation with falsification.** The skill output explicitly separates intuitive feelings ("It feels like...") from testable hypotheses, and each hypothesis includes both a predicted signal and a counter-signal (what would prove it wrong). The baseline's hypotheses are testable but do not separately articulate what evidence would falsify them.

4. **Practice plan with peer calibration.** The skill output includes a 4-week practice cadence (1.5 hours/week, weekly synthesis, peer calibration session in Week 2, retrospective in Week 4) designed to build ongoing taste muscle. The baseline's validation plan is a one-time 90-minute exercise without a sustained practice loop.

5. **Tradeoffs and non-goals.** The skill output explicitly lists 5 intentional tradeoffs (feature density sacrificed for first-number clarity, no customization during onboarding, educational content deferred, single-account linking priority, desktop-parity deprioritized). The baseline acknowledges constraints but does not formally document what the team is choosing NOT to optimize for.

## Verdict

The skill-guided output is significantly deeper in its observational methodology and more complete as a taste-building system. Its moment-based benchmark analysis, anti-pattern catalog, and 4-week practice plan make it a tool for ongoing taste development rather than a one-time analysis. The baseline is a competent taste audit with good benchmarks and hypotheses, but it functions more as a design assessment than a calibration system that changes how a team evaluates design over time.

## With Skill Output

<details>
<summary>Expand full output (~46k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~17k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
