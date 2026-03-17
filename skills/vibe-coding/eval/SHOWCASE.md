# Showcase: Vibe Coding

> Demonstrates the value of the `vibe-coding` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `vibe-coding`. 60-minute prototype: "AI meeting notes → action items": - Demo promise: "In 60 minutes, we will demo pasting meeting notes and getting a prioritized action-item list for a PM."

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Five phases organized chronologically (setup through polish); architecture diagram; risk table; prompt engineering notes | Six-section pack: vibe coding brief, prototype spec, prompt pack (5 sliced prompts), build plan with task board, demo script + runbook, risks/open questions/next steps |
| Completeness | Covers the build plan with minute-by-minute phases, API integration details, rendering design, and a V2 roadmap | Covers scope control (non-goals, fake-vs-real decisions), full prototype spec with acceptance criteria, structured prompt pack for agent-assisted coding, task board with validation steps, demo talk track, and backup plan |
| Actionability | Provides implementation outlines (JavaScript functions, API call structure, system prompt) that point toward actual code | Provides copy-paste-ready agent prompts (A through E) with explicit constraints, output format, and verification steps per slice; each slice has a definition of done |
| Specificity | System prompt for LLM extraction is fully written out; data model includes JSON schema; rendering layout is detailed section-by-section | Mock extraction logic uses deterministic rules (no API dependency); data model, sample input, and expected output table are all specified; acceptance criteria are checkboxable |
| Quality gates | Risk mitigation table and "what to cut" priority list; no formal quality checklist | Full quality gate with six checklists (scope, spec, vibe coding loop, build tools, demo readiness, final pack) and a five-category rubric self-assessment |

## Key Differences

1. **Scope control and fake-vs-real decisions.** The skill output explicitly decides what is real vs. mocked (data: mock; LLM: mock; integrations: none; auth: none; persistence: session-only) in a structured table, with rationale for each choice. The baseline output assumes a real LLM API call, which introduces API key management, network dependency, and latency risk into a 60-minute prototype.

2. **Agent-ready prompt pack.** The skill output provides five structured prompts (A through E) designed for an AI coding agent, each with context, constraints, deliverable scope, and output format. This embodies the "vibe coding" methodology of working with an AI pair programmer. The baseline output is a human-readable build plan that doesn't leverage AI-assisted coding patterns.

3. **Demo stability vs. feature richness.** The skill output prioritizes demo reliability by mocking the AI extraction (deterministic JS rules, no network calls), ensuring the happy path never crashes. The baseline output uses a real OpenAI API call, which adds impressive capability but introduces failure modes (API key issues, network errors, rate limits) during the demo.

4. **Backup and fallback planning.** The skill output includes a detailed backup plan (screenshots, video recording, alternate flow, quick restart), a change log template, and explicit validation steps per slice. The baseline output has a risk mitigation table and a "what to cut" priority order but less structured fallback planning.

5. **Demo script quality.** Both outputs include demo talk tracks, but the skill output structures it as a five-section narrative (problem, hero scenario, real vs. mocked, learnings, next steps) with timing per section and explicit acknowledgment of what is faked. The baseline output provides a shorter demo script that assumes a working LLM integration.

## Verdict

The skill-guided output is better optimized for the actual goal: shipping a reliable, demo-ready prototype in 60 minutes. Its mock-first approach, structured agent prompts, and explicit scope control reduce the risk of spending the timebox debugging API issues. The baseline output is more technically ambitious (real LLM integration) and includes valuable prompt engineering notes, but that ambition increases the risk of not having a working demo at the end of the session.

## With Skill Output

<details>
<summary>Expand full output (~26k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~16k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
