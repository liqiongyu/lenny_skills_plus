# Showcase: Media Relations

> Demonstrates the value of the `media-relations` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `media-relations`. We're launching a developer-focused AI code review tool on March 15. Our ICP is engineering leaders at mid-market SaaS companies (200-2000 employees). Goal: 8-10 quality mentions in developer/tech publications (e.g., The New Stack, InfoQ, DevOps.com) within 2 weeks of launch. We can offer 1 exclusive to a top-tier outlet and have 3 customer case studies ready. No revenue numbers can be shared publicly. Budget: $0 (no PR agency). Create a Media Relations Pack with a tiered media list of 20 outlets/reporters, an exclusive/embargo plan, 3 pitch email templates (exclusive offer, general pitch, follow-up), an outreach tracker, and interview prep with talking points and Q&A. Output: Media Relations Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 9 sections: tiered media list, exclusive + embargo strategy, 4 pitch templates (exclusive, embargo, post-launch, podcast), outreach tracker, interview prep, execution timeline, press kit checklist, success metrics, and risk mitigation | 9 sections: context snapshot, newsworthiness brief, media list + tiering, exclusive/embargo plan, pitch kit (7 email templates), press materials checklist + media FAQ, outreach tracker, interview prep, and risks/open questions |
| Completeness | Includes elements not in the prompt: an embargo plan with case study allocation per outlet, a podcast-specific pitch template, a press kit checklist, and success metrics table | Includes elements not in the prompt: a newsworthiness brief with 3 angle options, a media FAQ table, sensitive topic response guides, bridging phrases, post-interview thank-you template, and evidence-to-collect checklist |
| Actionability | Execution timeline provides a day-by-day plan from Feb 28 to Mar 29 with specific owner assignments; pitch templates are ready to customize | Staggered outreach timeline with specific dates and fallback plans; pitch templates include word counts and multiple subject-line options; interview prep includes 6 sensitive topics with safe responses |
| Specificity | Lists specific reporter names per outlet; case study allocation strategy differentiates angles per outlet; interview prep has 8 Q&A pairs with detailed suggested answers | Lists specific reporter names and beats per outlet with "why fit" rationale; 3 distinct angle options with "what's new," "why now," "who cares," and "proof" for each; interview prep has 3 key messages, proof/avoid lists, and sensitive topic responses |
| Quality gates | Success metrics table with 7 quantified targets | 8-category checklist plus a 6-dimension rubric scoring 11/12 (docked 1 point for TBD materials) |

## Key Differences

1. **Newsworthiness brief with angle options.** The skill output opens with a structured newsworthiness analysis providing 3 distinct angles (the "review gap" created by AI coding assistants, mid-market underserved by dev tools, customer-story-led), each with "what's new," "why now," "who cares," and "proof." The baseline weaves angle thinking into pitch templates but does not separate angle development from pitch execution.

2. **Exclusive-only strategy vs. exclusive + embargo.** The skill version recommends an exclusive-only approach (no embargo) with a clear rationale: $0 budget and limited brand recognition make embargo coordination risky. The baseline adds an embargo layer on top of the exclusive, distributing different case studies to different embargo outlets. The baseline's approach is more ambitious; the skill version's is more pragmatic for the stated constraints.

3. **Media FAQ as a separate artifact.** The skill output includes a structured media FAQ table with 8 questions, short on-the-record answers, proof/link references, and "what to avoid" notes per question. This serves as both spokesperson prep and a quick-reference during interviews. The baseline covers similar ground in the interview prep Q&A section but does not separate it into a standalone, sharable artifact.

4. **Pitch template variety and word-count discipline.** The skill version provides 7 email templates (exclusive, standard, practitioner/newsletter, follow-up #1, follow-up #2/close-the-loop, post-interview thank-you) with explicit word counts (100-160 words). The baseline provides 4 templates (exclusive, embargo, post-launch, podcast) that are slightly longer and more detailed.

5. **Explicit evidence collection checklist.** The skill output separates "what we can credibly say" from "what we should avoid saying" and "evidence to collect before outreach begins" (6 specific items with checkboxes). This pre-flight check prevents premature outreach. The baseline includes a press kit checklist but does not make the truth/safety distinction as explicit.

## Verdict

Both outputs are professional and comprehensive, reflecting genuine expertise in media relations. The baseline adds value with its embargo strategy, case study allocation approach, and day-by-day execution timeline. The skill-guided version differentiates through its structured newsworthiness analysis, pragmatic exclusive-only strategy, media FAQ artifact, and explicit truth/safety guardrails. For a founder running their first press outreach with no PR agency, the skill version's angle development and evidence-collection checklist provide critical strategic scaffolding.

## With Skill Output

<details>
<summary>Expand full output (~41k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~24k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
