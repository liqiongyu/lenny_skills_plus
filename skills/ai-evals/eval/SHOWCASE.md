# Showcase: AI Evals

> Demonstrates the value of the `ai-evals` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `ai-evals`. SUT: Drafts customer-support replies using retrieved KB articles. Decision: Ship/no-ship for a new prompt + retrieval policy. Constraints: No PII leakage; must cite KB; must refuse unsafe requests.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Flat sections covering objectives, metrics, test design, methods, monitoring | Full PRD-style eval with 11 numbered sections; dedicated red-team, infra, and decision-gate sections |
| Completeness | Covers safety, groundedness, retrieval, reply quality, and regression | Adds eval PRD with scope/non-goals, detailed red-team threat model with process, infrastructure diagram, cost estimates, and post-ship feedback loops |
| Actionability | Metric tables with thresholds are usable; human eval protocol is clear | Adds concrete red-team staffing/hours, infrastructure architecture diagrams, cost/time estimates ($5-9k, 5-7 days), and a gated ship/no-ship decision tree |
| Specificity | Good metric definitions with pass thresholds; sample eval case in JSON | Adds specific threat categories with examples, annotator calibration requirements, conditional ship options, and detailed post-ship monitoring with alert thresholds |
| Quality gates | Implicit through metric thresholds | Explicit 5-gate decision framework with hard blocks vs. soft blocks, named decision authorities, and escalation paths |

## Key Differences

1. **Decision framework depth.** The skill output provides a 5-gate ship/no-ship decision tree with hard blocks (safety, groundedness) vs. soft blocks (retrieval, quality), named decision authorities per gate, and conditional ship options. The baseline defines thresholds but leaves the actual ship decision process implicit.

2. **Red-team rigor.** The skill output dedicates a full section to adversarial testing with a structured threat model (7 threat types with examples), red-team composition and process (unstructured exploration + structured attacks + escalation probes), and explicit exit criteria. The baseline covers adversarial test cases as part of the dataset but lacks a red-team methodology.

3. **Operational readiness.** The skill output includes infrastructure diagrams, versioning requirements, cost/time estimates for the full eval cycle, and a detailed post-ship monitoring plan with production metrics, periodic re-evaluation cadence, and a feedback loop. The baseline mentions monitoring as a brief appendix-level concern.

4. **Eval PRD framing.** The skill output opens with a formal Eval PRD section defining scope, non-goals, constraints, and the precise system-under-test boundary. The baseline jumps directly into metrics and methods without this framing, making it harder to know what is and is not in scope.

5. **Sample artifacts.** The skill output includes a JSON sample eval case with gold labels, expected behavior tags, and risk categories, plus a claim-level verification pipeline. The baseline provides metric definitions and rubrics but fewer concrete examples of what test data and scoring look like in practice.

## Verdict

The skill output transforms an eval plan from a metrics catalog into an executable program with clear decision authority, staffing, infrastructure, and post-ship operations. Both outputs define solid metrics, but the skill version is materially more likely to result in a defensible ship/no-ship decision because it addresses the organizational and operational dimensions that baseline eval plans typically omit.

## With Skill Output

<details>
<summary>Expand full output (~61k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~22k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
