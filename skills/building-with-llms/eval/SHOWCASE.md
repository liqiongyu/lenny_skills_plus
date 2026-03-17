# Showcase: Building with LLMs

> Demonstrates the value of the `building-with-llms` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're building a customer support copilot for our B2B SaaS help desk product. The copilot should draft reply suggestions for support agents using our internal KB articles (about 500 articles in Zendesk). Agents will review and approve before sending. Key requirements: every response must include a citation to the source KB article, the system must never fabricate policy, and it must abstain when no KB article covers the question. We're worried about prompt injection and PII exfiltration. Success metrics: reduce median first-reply time from 8 minutes to under 3 minutes while keeping CSAT above 4.5. Budget: $0.15/ticket max LLM cost. Please produce the full feature brief, prompt and tool contract, data and eval plan, and launch plan.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Feature brief, system architecture, prompt, API contract, eval plan (offline + online), 4-phase launch plan, rollback plan, appendices | Feature brief with job statement and failure modes, system design sketch with architecture diagram, prompt with output schema and tool contracts, 20-case test set + 12 red-team cases with rubric, build/iteration plan with debug loop, launch/monitoring plan with alerts |
| Completeness | 200-case gold eval set, silver set for regression, offline + online metrics, CI/CD gates, 4-phase launch with A/B test | Adds structured output JSON schema, 2 formal tool contracts (search_kb, log_feedback), 6 automated checks, prompt changelog format, and coding agent safety constraints |
| Actionability | Prompt template with Jinja-style variables; API endpoint spec with request/response schema; CI gate requirements | 4 worked examples (happy path, partial coverage + staleness, abstention, injection), cost breakdown per component, thin-slice prototype plan with real/mocked matrix, and a 7-step debug loop |
| Specificity | Confidence threshold at 0.72; 200-case gold set stratified by topic/priority/complexity; retrieval recall@5 target >= 92% | 5 named failure modes ranked by severity, context strategy with instruction hierarchy (system > KB > ticket), conflict handling rules (cite both + recommend newer), and staleness policy (nightly + 1-hour re-index) |
| Quality gates | CI/CD gates for prompt changes; cost estimator flags per PR | 6-section checklist (feature brief, prompt/tool, data/eval, build/iteration, production readiness, final pack) plus 30/30 rubric self-score |

## Key Differences

1. **Structured output contract.** The skill output defines a JSON output schema with required fields (draft_reply, citations, confidence, abstained, agent_notes) and provides 4 worked examples showing exactly what the LLM should produce in normal, tricky, abstention, and injection cases. The baseline specifies the API response format but does not constrain the LLM's output structure or provide input/output examples.

2. **Red-team suite.** The skill output includes 12 specific red-team cases covering direct injection, indirect injection, PII exfiltration, role hijack, encoded injection, tool misuse, data poisoning, multi-turn injection, emotional manipulation, and more. The baseline lists 6 adversarial categories and requires 100% pass rate but does not enumerate specific test cases.

3. **Tool contracts.** The skill output formally specifies two tools (search_kb, log_feedback) with input/output schemas, side effects, safety constraints, and confirmation requirements. The baseline describes the retrieval pipeline and API endpoint but does not frame retrieval as a tool contract the LLM interacts with.

4. **Build/iteration loop.** The skill output defines a 7-step debug loop (reproduce, label, add to test set, fix, re-run eval, measure, ship/iterate) with a prompt changelog format and coding agent constraints (diff size limits, approval gates, no secrets). The baseline describes a CI/CD pipeline and evaluation cadence but does not formalize the prompt iteration workflow.

5. **Cost analysis depth.** Both outputs provide cost estimates within the $0.15 budget. The baseline notes actual costs will be ~$0.001/ticket with GPT-4o-mini, providing useful context. The skill output breaks costs down by component (embedding, retrieval, reranking, generation) and discusses model routing as a cost optimization strategy.

## Verdict

Both outputs are comprehensive and production-quality. The baseline is stronger on evaluation rigor (200-case gold set with human annotators, CI/CD integration, A/B test design) and operational maturity (16-week phased rollout). The skill output is stronger on prompt engineering specifics (structured output, worked examples, tool contracts, instruction hierarchy) and the developer iteration workflow. Together they represent complementary perspectives -- the baseline from an ML operations angle, the skill output from a prompt engineering and product design angle.

## With Skill Output

<details>
<summary>Expand full output (~43k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~21k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
