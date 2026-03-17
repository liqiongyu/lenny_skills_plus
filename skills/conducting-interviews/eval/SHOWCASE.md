# Showcase: Conducting Interviews

> Demonstrates the value of the `conducting-interviews` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `conducting-interviews`. Create a 45-minute hiring manager interview for a Senior Product Manager at a Series B healthcare SaaS company (80 people). The role owns the provider-facing scheduling product. I want to evaluate product sense, execution rigor, healthcare domain curiosity, and cross-functional collaboration with engineering and clinical ops. The candidate previously worked at a consumer health app and has no B2B experience. Include a question map with behavioral probes, a scorecard with rating anchors, and a debrief summary template. Output: Interview Execution Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8 sections mixing questions, scorecard, and debrief template; includes live design exercises alongside behavioral questions | 8 sections with a strict criteria-first methodology: criteria locked before questions, each question maps to exactly one criterion, scorecard with evidence requirements, substance-over-polish guardrails |
| Completeness | Covers all 4 criteria plus a regulatory awareness question; includes debrief template with scores and key evidence | Full coverage of 4 criteria plus global questions, a dedicated substance-over-polish guardrails section, a detailed notes template with blank fields, and a debrief template with B2B readiness assessment |
| Actionability | Provides an interviewer script but mixes hypothetical and behavioral questions; scorecard uses 1-4 scale with anchors | Complete minute-by-minute runbook with opening/closing scripts, per-question substance checks, note-taking reminders, and a 1-5 scale scorecard with evidence-based requirements |
| Specificity | Includes 8 questions with specific healthcare scheduling scenarios (35% drop-off rate exercise); 4-level rating anchors per criterion | 4 primary behavioral questions with 5 probes each, "what good sounds like" descriptions, and substance checks to catch polished-but-thin answers; 5-level anchors with evidence requirements |
| Quality gates | No self-assessment | Full quality gate checklist (5 categories) plus rubric self-score of 30/30 |

## Key Differences

1. **Criteria-first methodology.** The skill output locks 4 evaluation criteria with "strong" and "weak" behavioral anchors before writing any questions. Each question maps to exactly one criterion. The baseline weaves criteria and questions together, making it harder to ensure complete coverage and avoid double-counting.

2. **Substance-over-polish guardrails.** The skill output includes a dedicated section with countermeasures for both polished communicators (reduce false positives) and less-polished communicators (reduce false negatives). The baseline has no explicit mechanism to separate communication style from actual product judgment.

3. **Behavioral purity vs. mixed format.** The skill output uses primarily behavioral questions ("tell me about a time...") with specificity probes. The baseline mixes behavioral questions with live design exercises and hypotheticals, which can favor candidates who think well on their feet over those with deeper but less performative experience.

4. **Evidence capture discipline.** The skill output includes a full notes template with blank fields per question, note-taking reminders after each question section, and a scorecard that requires 2-4 bullets of evidence per rating. The baseline provides a debrief template but lacks the in-interview evidence capture scaffolding.

5. **Debrief depth.** The skill output includes a B2B transition readiness assessment checklist, explicit "verbatim moments" capture for strongest/weakest answers, and a structured debrief summary. The baseline provides a similar structure but without the B2B-specific assessment or the verbatim evidence anchoring.

## Verdict

The skill output produces a more methodologically rigorous interview pack that minimizes common hiring biases (halo effect, polish-over-substance, confirmation bias). The baseline is a strong, usable interview guide with creative question design, but the skill pack's criteria-first structure, substance guardrails, and evidence capture discipline make it more reliable for consistent, fair evaluation across multiple interviewers and candidates.

## With Skill Output

<details>
<summary>Expand full output (~31k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~15k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
