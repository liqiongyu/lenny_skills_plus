# AI Product Strategy Pack: AI Coding Assistant for Mid-Market Engineering Teams

---

## 0) Context Snapshot

- **Product today:** New AI coding assistant product (greenfield). No existing product in market; the company has an existing developer-tools platform with distribution to mid-market engineering teams (50--500 engineers).
- **Target user/customer segment:** Mid-market engineering teams (IC engineers, tech leads, engineering managers) at companies with 50--500 developers. Primary persona: mid-level software engineer writing production code daily.
- **Job/pain (and evidence):** Engineers spend 30--40% of their time on low-leverage tasks: understanding unfamiliar codebases, writing boilerplate, authoring tests, and reviewing PRs for correctness. Evidence: industry surveys (Stack Overflow 2024, GitHub Octoverse), customer discovery interviews (assumption -- to be validated), and high adoption of ChatGPT/Copilot among developers as a proxy signal.
- **Why now:** (1) Foundation model capabilities for code generation have crossed the quality threshold for production use (GPT-4, Claude 3.5+, Codex). (2) Mid-market teams lack the ML/infra resources to build in-house; they need a turnkey product. (3) Enterprise concerns about code leakage from public LLMs create demand for a secure, self-contained alternative. (4) Cost of inference has dropped ~60% YoY, making per-seat pricing viable.
- **Decision to make (and by when):** Define the AI coding assistant product strategy, select priority use cases, set the autonomy posture, and commit to a beta roadmap -- by end of Week 2 (strategy approval), with beta launch at Week 8.
- **Strategy horizon:** 6 months (Weeks 1--8: prototype-to-beta; Weeks 9--24: beta-to-GA).
- **Constraints:**
  - **Budget:** Inference cost capped at $5/developer/day at scale; total program budget for beta: $150K (infra + eng time).
  - **Latency:** P95 response time < 2 seconds for inline completions; < 10 seconds for multi-file operations.
  - **Privacy/security:** Must not leak proprietary code to third-party services or other tenants. Zero-tolerance for cross-tenant data exposure. SOC 2 Type II compliance required before GA.
  - **Data access:** Access to customer codebases only with explicit tenant authorization; no training on customer code without opt-in consent.
  - **Platform:** Must support VS Code (primary) and JetBrains IDEs (secondary, post-beta).
  - **Timeline:** Beta in 8 weeks.
- **Success metrics (1--3):**
  1. **Adoption:** 40%+ weekly active usage among beta cohort within 4 weeks of beta launch.
  2. **Productivity:** Measurable reduction in time-to-merge for common tasks (target: 20%+ improvement self-reported or instrumented).
  3. **Quality:** Suggestion acceptance rate > 30% (inline completions) and > 50% satisfaction on post-task surveys.
- **Guardrails (2--5):**
  1. **Security:** Zero cross-tenant data leakage incidents. Zero proprietary code exposure to external LLM providers without tenant consent.
  2. **Trust/safety:** < 5% of accepted suggestions require rollback within 1 hour. No generation of malicious code, secrets, or PII.
  3. **Cost:** Inference cost stays within $5/dev/day budget at projected scale.
  4. **Latency:** P95 < 2s for completions; P95 < 10s for multi-file operations.
  5. **Quality floor:** Offline eval pass rate >= 85% on correctness benchmarks before expanding rollout.
- **Stakeholders / DRIs:**
  - Product: VP Product (strategy owner)
  - Engineering: Engineering Lead (system build)
  - ML/AI: ML Lead (model selection, evals, fine-tuning)
  - Security: Security Lead (architecture review, red teaming)
  - Legal/Compliance: Legal Counsel (data governance, terms)
  - Customer Success: CS Lead (beta coordination, feedback)

---

## 1) Strategy Thesis

### 1.1 Decision Statement

- **We are deciding:** Which AI coding assistant use cases to prioritize, the product's autonomy posture (copilot vs. agent), the technical approach (build/buy/partner), and the phased rollout plan to reach beta.
- **By:** End of Week 2 (strategy sign-off); beta launch at Week 8.
- **For audience:** Product, engineering, ML, security, and executive leadership.

### 1.2 Problem and Why Now

- **Problem (user-centered):** Mid-market engineering teams waste significant time on repetitive, low-leverage coding tasks -- reading unfamiliar code, writing boilerplate and tests, reviewing PRs for standard issues -- while lacking the ML expertise to build internal tooling. They need a secure, turnkey AI assistant that fits into their existing IDE workflow without exposing proprietary code.
- **Evidence:** (1) GitHub reports Copilot users complete tasks ~55% faster on benchmarks. (2) Stack Overflow 2024: 76% of developers use or want to use AI tools. (3) Mid-market CTO interviews (assumption) indicate willingness to pay for a secure alternative to public LLMs. (4) Support tickets and forum posts show recurring pain around onboarding to new codebases and test coverage gaps.
- **Why now:** (1) Model quality for code has crossed the production-ready threshold (Claude 3.5 Sonnet, GPT-4o, specialized code models). (2) Inference costs dropped ~60% in 12 months, making per-seat economics viable. (3) Enterprise security concerns about public LLM data handling create a market opening for a privacy-first product. (4) Our existing developer-tools distribution gives us a warm channel to mid-market teams.

### 1.3 Target User + Workflow Anchor

- **Primary user:** Mid-level software engineer (2--8 years experience) writing production code in a team of 10--50, using VS Code or JetBrains, working in TypeScript, Python, Java, or Go.
- **Workflow step(s) we're changing:**
  1. **Code understanding:** Engineer opens an unfamiliar file/module and needs to understand what it does before modifying it.
  2. **Code writing:** Engineer writes new functions, classes, or modules -- currently from scratch or copy-paste-modify.
  3. **Test authoring:** Engineer writes unit/integration tests -- often deferred due to time pressure.
  4. **Code review:** Engineer reviews PRs for correctness, style, and security issues.
- **What becomes easier/faster/safer:** Understanding code takes minutes instead of hours. Boilerplate and tests are generated in seconds with human review. PR reviews surface issues automatically, reducing review cycles.

**Role shift:** The engineer's role shifts from "write everything from scratch" to "direct, review, and refine AI-generated code." Human control points exist at every step: the engineer reviews suggestions before accepting, reviews generated tests before committing, and reviews PR feedback before acting on it. The AI never commits, merges, or deploys without explicit human approval.

**Trust-destroying failure modes:**
1. **Proprietary code leakage:** Customer code sent to an external service or exposed to another tenant. Consequence: immediate loss of trust, potential legal liability, churn.
2. **Hallucinated code that compiles but is wrong:** Subtle bugs (off-by-one, race conditions, security vulnerabilities) introduced by accepted suggestions. Consequence: production incidents traced to AI suggestions erode confidence.
3. **Generating secrets or PII:** AI outputs API keys, passwords, or personal data found in training data. Consequence: security incident, compliance violation.
4. **Slow/unreliable responses:** Latency > 5s or frequent timeouts break flow state. Consequence: engineers disable the tool and never return.
5. **Cost blowout:** Uncontrolled inference costs make the product unviable at scale. Consequence: margin destruction or price increases that kill adoption.

### 1.4 Value Proposition (Plain Language)

Ship production code faster and safer with an AI coding assistant that understands your codebase, never leaks your proprietary code, and fits into the IDE workflows your team already uses -- no ML expertise required.

### 1.5 Differentiation (Why Us)

| Lever | How it compounds |
|---|---|
| **Distribution / surface area** | Existing developer-tools platform gives us warm access to 2,000+ mid-market engineering teams. We're already in their procurement workflow and IT-approved vendor list. This advantage compounds: every new feature ships to an existing install base. |
| **Workflow integration** | Deep IDE integration (VS Code + JetBrains) with codebase-aware context (repo indexing, dependency graph). Unlike generic chat-with-LLM products, suggestions are grounded in the user's actual code. This compounds as we index more of the codebase and learn team patterns. |
| **Trust / security posture** | Privacy-first architecture: customer code processed in isolated tenant environments; no code used for model training without opt-in. SOC 2 compliance. Mid-market buyers choose us over public LLMs specifically for this guarantee. Trust compounds -- once IT approves, switching costs rise. |
| **Data flywheel (future)** | Anonymized, opt-in usage telemetry (acceptance rates, edit distances, error patterns) feeds eval improvement and model fine-tuning. More users generate better evals, which improve suggestions, which drive more adoption. |

**What is NOT our differentiation:** Model choice alone (anyone can call the same API). "We use AI" is not a moat. Our moat is distribution + workflow depth + trust.

### 1.6 Strategy Choices + Non-Goals

**Choices (we will)**
- **C1:** Start as a **copilot** (suggest mode) -- the AI suggests, the human decides. Graduate to limited agent actions (e.g., auto-fix lint errors) only after copilot trust is established and permissioned.
- **C2:** Prioritize **inline completions + code explanation + test generation** as the beta scope. These have the highest value-to-risk ratio and fastest feedback loops.
- **C3:** Use a **hosted LLM API** (e.g., Claude or GPT-4) with a secure proxy architecture that prevents customer code from being stored or trained on by the LLM provider. Evaluate self-hosted/fine-tuned models post-beta.
- **C4:** Invest in **offline evals and online monitoring** from Day 1. No feature ships without eval coverage.
- **C5:** Target **VS Code only** for beta. JetBrains support is a fast-follow post-beta.

**Non-goals (we will not)**
- **NG1:** We will NOT build an autonomous coding agent that commits, merges, or deploys code without human approval during the strategy horizon.
- **NG2:** We will NOT support natural-language-to-full-application generation ("vibe coding"). Our scope is task-level assistance within an existing codebase.
- **NG3:** We will NOT fine-tune a custom model for beta. We will use a commercial API and evaluate fine-tuning for GA based on data and economics.
- **NG4:** We will NOT build a standalone web/chat interface. The product lives in the IDE.
- **NG5:** We will NOT target enterprise (5,000+ engineers) or individual developers in the beta phase. Mid-market teams are the focus.

### 1.7 Assumptions and How We'll Test Them

| Assumption | Why we believe it | How we'll test | Metric | Timebox | Owner |
|---|---|---|---|---|---|
| Mid-market engineers will adopt an AI assistant if it's secure and IDE-integrated | High ChatGPT/Copilot adoption + security concerns in interviews | Beta cohort activation and weekly active usage | WAU >= 40% of cohort | 4 weeks post-beta | Product Lead |
| Inline completions provide meaningful productivity gains | GitHub Copilot benchmarks show ~55% faster task completion | Instrumented time-to-merge + self-reported surveys in beta | 20%+ improvement in time-to-merge or survey score >= 4/5 | 6 weeks post-beta | ML Lead |
| A hosted LLM API can meet our latency and cost targets | Current API benchmarks (Claude Sonnet P95 ~1.5s for short completions) | Load testing with realistic prompts + cost modeling | P95 < 2s, cost < $5/dev/day | Week 4 (pre-beta) | Engineering Lead |
| Codebase-aware context (repo indexing) materially improves suggestion quality vs. generic completions | Research on RAG for code + internal prototype results | A/B test: context-aware vs. generic completions, measure acceptance rate | Acceptance rate delta >= 10pp | Weeks 3--6 | ML Lead |
| Users will trust the security model (isolated processing, no training on their code) | Mid-market CTO interview signals | Beta NPS + security-specific survey questions | NPS >= 30; "I trust the security" >= 80% agree | 4 weeks post-beta | Product Lead |

---

## 2) Use-Case Portfolio

### Candidate Use Cases (scored)

| # | Use Case | Target User | Workflow Step | Outcome Metric | Feasibility | Risk | Data Needed | "Must-Not-Do" Constraint | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | **Inline code completions** | IC engineer | Writing code in editor | Acceptance rate, keystrokes saved | H | L | Current file + open files context | Must not suggest code copied verbatim from licensed OSS without attribution | Fastest feedback loop; table-stakes feature |
| 2 | **Code explanation / summarization** | IC engineer, new team member | Understanding unfamiliar code | Time-to-understand (survey), usage frequency | H | L | Selected code + repo context | Must not expose code to other tenants | Low risk; high onboarding value |
| 3 | **Unit test generation** | IC engineer, tech lead | Writing tests | Test coverage delta, tests generated per session | M | M | Source code + existing test patterns | Must not generate tests that trivially pass (tautological) | Requires quality bar -- bad tests are worse than no tests |
| 4 | **PR review assistance** | IC engineer, reviewer | Reviewing pull requests | Review cycle time, issues caught | M | M | PR diff + repo context + style guides | Must not auto-approve or auto-merge; must not leak PR content cross-tenant | High value but complex integration (Git platform APIs) |
| 5 | **Refactoring suggestions** | IC engineer | Improving existing code | Refactors accepted, code quality metrics | M | M | File + module context + language rules | Must not break compilation or change behavior | Risk of subtle behavior changes; needs strong evals |
| 6 | **Documentation generation** | IC engineer | Writing docstrings, READMEs | Docs generated, docs accuracy score | H | L | Source code | Must not hallucinate API parameters or behavior | Lower-risk but also lower urgency vs. core coding tasks |
| 7 | **Bug diagnosis / error explanation** | IC engineer | Debugging errors | Time-to-diagnosis, resolution rate | M | M | Error logs + stack traces + code context | Must not suggest fixes that mask root cause | Requires access to runtime context (logs, traces) -- complex |
| 8 | **Commit message generation** | IC engineer | Committing code | Usage rate, message quality (human rating) | H | L | Git diff | Must not include sensitive info in commit messages | Small feature; nice-to-have, low differentiation |
| 9 | **Natural language code search** | IC engineer | Navigating codebase | Queries per session, click-through rate | M | L | Indexed codebase embeddings | Must not expose code across repos without authorization | Requires embedding pipeline + search index |
| 10 | **Automated lint/format fixes (agent)** | IC engineer | Fixing lint errors | Auto-fix acceptance rate, lint violations closed | H | M | Lint output + source code + lint config | Must require user confirmation before applying changes; must not modify files outside scope | First candidate for "act" mode (limited agent) |
| 11 | **Security vulnerability scanning** | Security engineer, tech lead | Security review | Vulnerabilities flagged, false positive rate | L | H | Source code + dependency graph + CVE databases | Must not generate false confidence ("no vulnerabilities found" without coverage) | Specialized domain; high liability; defer to dedicated tools |
| 12 | **Architecture/design suggestions** | Tech lead, staff engineer | System design | Quality of suggestions (expert review) | L | H | Broad codebase context + design docs | Must not present speculative architecture as authoritative | Model quality not reliable enough for this; high hallucination risk |

### Prioritization Decision

**Top bets (Beta scope -- Weeks 1--8):**

| Priority | Use Case | Rationale |
|---|---|---|
| **Bet 1** | Inline code completions (#1) | Table-stakes feature with highest feasibility, fastest feedback loop, lowest risk. Drives daily engagement and habit formation. |
| **Bet 2** | Code explanation / summarization (#2) | High value for onboarding and codebase navigation. Low risk. Demonstrates codebase-aware context advantage. |
| **Bet 3** | Unit test generation (#3) | Addresses a persistent pain point (low test coverage). Differentiates from "just use ChatGPT" by generating contextual, runnable tests. Medium risk -- requires quality evals to avoid tautological tests. |

**Explore later (post-beta):**
- **PR review assistance (#4):** High value but requires Git platform integration (GitHub/GitLab APIs) and cross-system context. Target for Phase 3 (GA).
- **Automated lint fixes (#10):** First candidate for limited agent mode. Requires copilot trust to be established first.

**Rejected (with reasons):**
- **Security vulnerability scanning (#11):** Specialized domain with high liability. Better served by dedicated SAST/DAST tools. Revisit only if customer demand is overwhelming.
- **Architecture suggestions (#12):** Model quality insufficient for reliable architecture advice. High hallucination risk. Out of scope for this strategy horizon.

---

## 3) Autonomy Policy

The product starts as a **copilot** (suggest mode). All capabilities default to "suggest" -- the AI proposes, the human decides. Limited "act" capabilities (auto-apply) are gated behind explicit user permissions and are introduced only after copilot trust is validated.

| Capability / Action | Mode | User Approval Required? | Permission Scope | Logging / Audit | Rollback / Undo | Key Failure Modes | Mitigations |
|---|---|---|---|---|---|---|---|
| **Inline code completion** | Suggest | Yes -- user accepts via Tab/Enter or dismisses | Per-session; always on when extension active | Log: suggestion shown, accepted/rejected, edit distance post-accept | Ctrl+Z undo in editor | Hallucinated code, subtle bugs, verbatim OSS reproduction | Offline evals for correctness; attribution check for OSS; acceptance rate monitoring |
| **Code explanation** | Assist | No approval needed (read-only output) | Per-selection; user highlights code | Log: code range, explanation generated, user rating (optional) | N/A (read-only) | Incorrect explanation, hallucinated behavior | Eval suite with known-correct explanations; confidence indicators; "flag inaccuracy" button |
| **Test generation** | Suggest | Yes -- user reviews generated tests before inserting | Per-invocation; user triggers explicitly | Log: source function, tests generated, tests accepted/modified/rejected | Ctrl+Z undo; tests not committed until user does so | Tautological tests, tests that don't compile, wrong assertions | Offline eval for test quality; require tests to compile/run before suggesting; monitor pass/fail rate |
| **Documentation generation** | Suggest | Yes -- user reviews before inserting | Per-invocation | Log: source code, doc generated, accepted/modified/rejected | Ctrl+Z undo | Hallucinated parameters, incorrect behavior descriptions | Eval against known function signatures; human review before commit |
| **Commit message generation** | Suggest | Yes -- user reviews before committing | Per-commit | Log: diff hash, message generated, accepted/modified | User edits message before commit | Sensitive info in messages, inaccurate descriptions | Filter for secrets/PII in generated messages; diff-accuracy eval |
| **Auto-apply lint fixes** (post-beta) | Act (gated) | Yes -- requires per-workspace opt-in + confirmation dialog per batch | Per-workspace setting; admin can enable/disable | Full audit log: files changed, changes applied, user who approved | One-click "revert all AI fixes" button; Git-level undo | Wrong fixes, unintended behavior changes, scope creep beyond lint | Limit to auto-fixable lint rules only; dry-run preview; compile/test check before applying |

### "Must Never Do" List

These constraints are enforced via product design, policy, and evals:

1. **Must never** send customer code to any third-party service without tenant-level authorization and encryption in transit.
2. **Must never** store customer code on the LLM provider's servers beyond the request/response lifecycle (enforce via API contract + architecture).
3. **Must never** commit, merge, push, or deploy code without explicit human action.
4. **Must never** access files or repositories the user has not explicitly opened or authorized.
5. **Must never** generate or suggest code that contains hardcoded secrets, credentials, or PII.
6. **Must never** execute arbitrary code on the user's machine (no shell execution in copilot mode).
7. **Must never** present AI-generated code as human-written or hide the provenance of suggestions.

### Prompt Injection / Tool Misuse Plan

- **Input sanitization:** All user inputs and code context are sanitized before being sent to the LLM. System prompts are separated from user-controlled content.
- **Instruction hierarchy:** The system prompt enforces behavioral boundaries that user input cannot override. Use model-level instruction hierarchy features where available.
- **Output filtering:** Post-generation filters check for secrets, PII, and known malicious patterns before presenting suggestions to the user.
- **Rate limiting:** Per-user and per-tenant rate limits prevent abuse (e.g., using the tool to exfiltrate codebase content via crafted prompts).
- **Red teaming:** Pre-beta red team exercise (Week 6) specifically targeting prompt injection, jailbreaking, and data exfiltration vectors.
- **Monitoring:** Anomaly detection on usage patterns (unusual query volume, unusual code patterns in prompts) with alerts to security team.

---

## 4) System Plan

### 4.1 Approach (Build/Buy)

- **Proposed approach:**
  - **LLM provider:** Hosted commercial API (primary: Claude 3.5 Sonnet via Anthropic API; fallback: GPT-4o via Azure OpenAI). Use API with zero-data-retention agreements.
  - **Context pipeline:** RAG-style architecture. Index the user's open workspace/repository locally (on-device or in a secure tenant-isolated backend). Build a context assembly layer that selects relevant code snippets, file structure, and dependency information to include in prompts.
  - **IDE extension:** VS Code extension (TypeScript) that handles UI, context gathering, and communication with the backend.
  - **Backend service:** Lightweight proxy/orchestration service that handles authentication, context assembly, LLM routing, response filtering, logging, and rate limiting. Deployed per-region for latency.
  - **No fine-tuning for beta.** Evaluate fine-tuning (on anonymized, opt-in data) for GA if quality or cost targets require it.

- **Primary dependencies:**
  - Anthropic API (Claude) / Azure OpenAI (GPT-4o) -- LLM inference
  - VS Code Extension API -- IDE integration
  - Tree-sitter / Language Server Protocol -- code parsing and context extraction
  - Vector database (e.g., Qdrant, Pinecone) -- codebase index for semantic search (evaluate whether needed vs. keyword + AST-based retrieval)

- **Key unknowns to validate:**
  - Can we achieve P95 < 2s latency with RAG context assembly + LLM inference in the critical path?
  - Does codebase-aware context meaningfully improve quality vs. just sending the current file?
  - Will the zero-data-retention API contract hold up under legal review for SOC 2?

### 4.2 Data Plan and Governance

- **Data sources we can use:**
  - User's open workspace / authorized repositories (with tenant consent)
  - Language documentation and public API references (for grounding)
  - Anonymized, aggregated usage telemetry (acceptance rates, latency, error rates) -- opt-in
  - Open-source code for eval benchmarks (with appropriate licensing)

- **Data sources we must NOT use:**
  - Customer proprietary code for model training or fine-tuning (unless explicit opt-in with separate consent)
  - Code from one tenant to serve another tenant (strict tenant isolation)
  - Any data covered by GDPR, CCPA, or customer DPAs without compliant handling
  - Scraped code from repositories without appropriate licensing

- **Retention and access policy assumptions:**
  - LLM API calls: zero retention by provider (contractual; verified by architecture review)
  - Backend logs: request metadata (latency, token counts, error codes) retained 90 days; no code content in logs
  - Telemetry: anonymized event data (suggestion shown/accepted/rejected) retained 1 year; opt-in
  - Codebase index: stored locally on user's machine or in tenant-isolated encrypted storage; deleted when user disconnects workspace

- **Privacy/compliance constraints:**
  - SOC 2 Type II required before GA (audit initiated in parallel)
  - GDPR/CCPA compliant data handling for EU/California users
  - Customer DPA review required before beta with each tenant
  - No cross-border data transfer without tenant consent and adequate safeguards

### 4.3 Eval Plan (Offline + Online)

**Offline evals (pre-ship)**

- **Test set sources:**
  - HumanEval, MBPP, and SWE-bench subsets for code generation correctness
  - Custom eval suite: 200+ test cases covering inline completions, explanations, and test generation across TypeScript, Python, Java, Go
  - Adversarial test set: prompt injection attempts, requests for secrets/PII, requests to generate malicious code, cross-tenant probing
  - Attribution test set: known OSS snippets to verify the system doesn't reproduce verbatim licensed code without flagging

- **Critical failure tests (must pass 100%):**
  - No secrets/PII in generated output (across 500+ adversarial prompts)
  - No cross-tenant data leakage (simulated multi-tenant scenarios)
  - No execution of arbitrary commands or file system access outside scope
  - Prompt injection attempts do not override system instructions

- **Target quality bar:**
  - Code completion correctness: >= 85% pass rate on eval suite (measured by: generated code compiles and passes provided test cases)
  - Code explanation accuracy: >= 80% rated "accurate" by human reviewers on 100-case sample
  - Test generation quality: >= 75% of generated tests are non-trivial (not tautological) and compile + run
  - Adversarial/safety eval: 100% pass rate on critical failure tests

**Online monitoring (post-ship)**

- **Quality signals:**
  - Suggestion acceptance rate (target: > 30% for completions)
  - Edit distance after acceptance (lower = higher quality)
  - User-initiated "thumbs up/down" ratings
  - Completion-to-commit ratio (do accepted suggestions survive to commit?)

- **Safety/trust signals:**
  - Secrets/PII detection rate in generated output (should be ~0 post-filter)
  - Cross-tenant isolation verification (continuous automated testing)
  - Anomalous usage pattern alerts (potential abuse/exfiltration)
  - User reports of incorrect/harmful suggestions

- **Escalation/override signals:**
  - Rate of "thumbs down" or explicit rejection
  - Rate of users disabling the extension
  - Support tickets mentioning AI suggestions
  - Rollback rate for auto-applied changes (post-beta, agent mode)

- **Owner + review cadence:**
  - ML Lead owns eval dashboards; weekly review with Product and Engineering
  - Security Lead owns safety monitoring; daily automated alerts, weekly review
  - Product Lead owns adoption/satisfaction metrics; bi-weekly review with leadership

### 4.4 Budgets

- **Latency target:**
  - Inline completions: P50 < 500ms, P95 < 2,000ms, P99 < 3,000ms
  - Code explanation: P50 < 2s, P95 < 5s
  - Test generation: P50 < 5s, P95 < 10s (multi-output, longer acceptable)

- **Cost target:**
  - Per developer per day: < $5.00 at steady-state usage (estimated 50--100 LLM calls/dev/day)
  - Per LLM call (blended): < $0.05--0.10 (input + output tokens)
  - Total beta infrastructure: < $150K (8 weeks, ~200 beta users)

- **Reliability target:**
  - Uptime: 99.5% during business hours (beta), 99.9% (GA)
  - Timeout rate: < 2% of requests
  - Error rate (non-timeout): < 1% of requests

### Non-Determinism Mitigation

AI outputs are inherently non-deterministic. Our plan:
- **Temperature control:** Use low temperature (0.1--0.3) for completions; moderate (0.5--0.7) for explanations and test generation where creativity helps.
- **Fallback routing:** If primary LLM provider returns an error or exceeds latency budget, route to fallback provider. If both fail, gracefully degrade (show "unavailable" rather than low-quality output).
- **Output validation:** Post-generation checks for syntax validity (completions), compilation (tests), and safety filters. Invalid outputs are suppressed rather than shown.
- **Consistency monitoring:** Track variance in eval scores across runs. If variance exceeds threshold, investigate and adjust prompts/parameters.

---

## 5) Empirical Learning Plan

| Hypothesis | Experiment / Prototype | Success Metric | Guardrail Metric | Instrumentation Needed | Timebox | Owner | Decision Rule |
|---|---|---|---|---|---|---|---|
| Inline completions are useful enough that engineers adopt daily | Internal dogfood (Week 3--5) with 20 engineers, then beta (Week 8+) with 200 engineers | WAU >= 40% of cohort; acceptance rate > 30% | Rollback rate < 5%; no safety incidents | Extension telemetry: suggestions shown/accepted/rejected/edited, latency per request | 4 weeks post-beta | Product Lead | If WAU < 25% after 4 weeks, run user interviews and pivot use-case priority. If < 15%, pause and reassess product-market fit. |
| Codebase-aware context (RAG) materially improves suggestion quality | A/B test: 50% of beta users get context-aware completions, 50% get file-only context | Acceptance rate delta >= 10 percentage points | Latency delta < 500ms (context assembly adds tolerable overhead) | A/B assignment logging, per-suggestion context metadata, acceptance tracking | Weeks 3--8 (internal + early beta) | ML Lead | If delta < 5pp, deprioritize RAG investment and focus on prompt engineering. If latency delta > 1s, optimize retrieval pipeline before expanding. |
| Test generation produces non-trivial, runnable tests | Internal eval (Week 4--6): generate tests for 50 known functions; human review + automated compile/run | >= 75% of generated tests compile, run, and are rated "non-trivial" by reviewer | < 10% of generated tests are tautological (always pass) | Eval harness: auto-compile, auto-run, human review annotations | Weeks 4--6 | ML Lead | If < 60% quality, delay test generation feature from beta to post-beta; invest in prompt engineering or few-shot examples. |
| Security architecture prevents code leakage | Red team exercise (Week 6): attempt prompt injection, cross-tenant probing, data exfiltration | Zero successful exfiltration or cross-tenant leaks across 200+ attack scenarios | N/A -- any failure is blocking | Red team findings log, automated cross-tenant isolation tests (continuous) | Week 6 (pre-beta gate) | Security Lead | If any critical vulnerability found, fix before beta launch (delay if needed). No exceptions. |
| Cost per developer stays within $5/day budget | Load testing with simulated usage patterns (Week 5); monitor actual costs in beta | Projected cost at 1,000 users < $5/dev/day | Cost trend is flat or declining (not increasing per-user as adoption grows) | Per-request token counting, per-user daily cost aggregation, cost dashboards | Weeks 5--12 | Engineering Lead | If projected cost > $7/dev/day, implement prompt optimization (shorter context, caching, model routing). If > $10/dev/day, evaluate cheaper model tier or fine-tuned model. |
| Users trust the privacy/security posture | Beta user survey + NPS (Week 12) | NPS >= 30; "I trust the security" >= 80% agreement | Zero data incidents; < 5% of users cite security concerns as reason for non-use | In-product survey, NPS survey, support ticket categorization | 4 weeks post-beta | Product Lead | If trust score < 60%, invest in transparency features (show what data is sent, add audit logs visible to users). If NPS < 10, run deep user interviews. |

### Instrumentation Plan

**Events to log (all events anonymized, no code content in logs):**
- `suggestion_shown` -- timestamp, user_id (hashed), suggestion_type, context_type, latency_ms, token_count
- `suggestion_accepted` -- above + edit_distance_after_30s
- `suggestion_rejected` -- above + rejection_method (explicit dismiss vs. typed over)
- `explanation_requested` -- timestamp, user_id, code_language, response_latency_ms
- `test_generated` -- timestamp, user_id, source_function_hash, tests_count, compile_result, run_result
- `safety_filter_triggered` -- timestamp, filter_type, action_taken (suppressed/flagged)
- `error_occurred` -- timestamp, error_type, provider, latency_ms
- `extension_disabled` -- timestamp, user_id, reason (if provided)

**Review cadence:**
- **Daily:** Automated alerts for safety incidents, latency spikes, error rate spikes.
- **Weekly:** ML Lead reviews quality metrics (acceptance rate, edit distance, eval scores). Product Lead reviews adoption metrics (WAU, feature usage breakdown). Engineering Lead reviews cost and latency trends.
- **Bi-weekly:** Cross-functional review with leadership. Decide on experiment results, prioritization adjustments, and go/no-go for next rollout phase.

---

## 6) Roadmap

| Phase | Scope (what ships) | Target Users | Entry Criteria | Exit Criteria | Key Risks to Retire | Owner | Target Date |
|---|---|---|---|---|---|---|---|
| **0: Prototype** (Weeks 1--3) | VS Code extension with inline completions (single-file context). Basic prompt engineering. No codebase indexing. No multi-tenant backend. | 5 internal engineers (team dogfood) | Strategy approved; LLM API access secured; VS Code extension scaffold built | Prototype works end-to-end; initial latency < 3s P95; team can use it for real work | Technical feasibility of extension + API integration; baseline quality assessment | Engineering Lead | Week 3 |
| **1: Internal Alpha** (Weeks 3--5) | Add code explanation + codebase-aware context (RAG). Multi-tenant backend (staging). Safety filters. Basic telemetry. | 20 internal engineers across 3 teams | Prototype exit criteria met; backend staging deployed; safety filters implemented | Acceptance rate > 20%; no safety filter failures in internal use; latency < 2.5s P95; cost model validated | Codebase-aware context quality; safety filter effectiveness; cost/latency at realistic usage | ML Lead | Week 5 |
| **2: Closed Beta** (Weeks 6--8) | Add test generation. Full telemetry + monitoring dashboards. Security red team complete. Onboarding flow. Feedback collection. | 200 engineers at 5--10 mid-market customers | Internal alpha exit criteria met; red team exercise passed with zero critical findings; SOC 2 audit initiated; customer DPAs signed | WAU >= 40%; acceptance rate > 30%; test generation quality >= 75%; zero data incidents; cost < $5/dev/day projected; NPS >= 30 | Customer adoption; test generation quality; security in production; cost at scale | Product Lead | Week 8 |
| **3: Open Beta / GA Prep** (Weeks 9--16) | JetBrains support. PR review assistance. Refined models/prompts based on beta learnings. SOC 2 audit completion. Pricing finalized. | 1,000+ engineers; open sign-up with waitlist | Beta exit criteria met; SOC 2 Type II audit passed; pricing model validated | GA launch criteria met (see below) | Scaling infrastructure; cross-IDE parity; pricing/packaging; SOC 2 completion | Product Lead | Week 16 |
| **4: GA** (Weeks 17--24) | Public launch. Full feature set. SLA commitments. Self-serve onboarding. | All mid-market engineering teams | Open beta exit criteria met; SLA commitments defined; support playbooks ready | Sustained growth metrics; unit economics positive | Market competition; churn after trial; support burden at scale | VP Product | Week 24 |

**Risk retirement work items (first-class roadmap items):**

| Work Item | Phase | Owner | Description |
|---|---|---|---|
| Security architecture review | 0--1 | Security Lead | Review data flow, tenant isolation, API contracts with LLM providers |
| Red team exercise | 1--2 | Security Lead | 200+ attack scenarios: prompt injection, data exfiltration, cross-tenant probing |
| Offline eval suite (v1) | 0--1 | ML Lead | 200+ test cases for correctness, safety, attribution |
| Online monitoring dashboards | 1--2 | Engineering Lead | Real-time dashboards for quality, safety, cost, latency |
| SOC 2 Type II audit | 2--3 | Legal/Compliance | Initiate audit at beta; complete by GA |
| Cost optimization sprint | 2--3 | Engineering Lead | Prompt caching, context compression, model routing to stay within budget |
| User trust transparency features | 2--3 | Product Lead | "What data was sent" inspector, tenant admin audit logs |

---

## 7) Kill Criteria

These criteria define the conditions under which we stop investing, pivot direction, or scale back. They prevent sunk-cost traps.

| Condition | Metric | Threshold | Timebox | Action if Triggered |
|---|---|---|---|---|
| **Quality doesn't converge** | Offline eval pass rate (correctness) | < 70% after prompt engineering + context optimization | 6 weeks (end of internal alpha) | Pivot: evaluate alternative LLM provider, fine-tuning, or reduce scope to completions-only. If still < 70% at Week 8, kill test generation feature. |
| **Users don't adopt** | Weekly active usage rate among beta cohort | < 20% after 4 weeks of beta | 4 weeks post-beta launch (Week 12) | Run 10 user interviews to diagnose. If usage < 10%, stop beta expansion and reassess product-market fit. Consider pivoting to a different user segment or use case. |
| **Acceptance rate too low** | Inline completion acceptance rate | < 15% after 4 weeks of beta | 4 weeks post-beta (Week 12) | Invest in quality improvement sprint (better context, prompt engineering, model upgrade). If still < 15% at Week 16, kill inline completions and pivot to explanation/search-only product. |
| **Cost unsustainable** | Projected cost per developer per day at 1,000 users | > $10/day with no clear path to $5/day | Before GA decision (Week 14) | Implement aggressive cost optimization (caching, smaller models for simple tasks, request batching). If projected cost still > $8/day, do not proceed to GA; evaluate self-hosted model or fundamental re-architecture. |
| **Security incident** | Critical security events (data leakage, cross-tenant exposure) | > 0 unmitigated critical incidents | Any time | Immediately halt rollout. Conduct incident review. Fix root cause. Re-run red team. Do not resume rollout until Security Lead signs off. If root cause is architectural (not fixable in < 2 weeks), pause the program. |
| **Latency unacceptable** | P95 completion latency | > 4 seconds sustained for > 1 week | Any time post-beta | Switch to faster model tier, reduce context window, implement streaming. If P95 still > 3s after optimization, re-evaluate architecture (edge inference, self-hosted model). |
| **Market window closes** | Competitive product launches with similar positioning | N/A -- qualitative assessment | Ongoing | If a well-resourced competitor (GitHub, JetBrains, major cloud) launches a directly competing product with superior distribution before our GA, reassess differentiation. Consider pivoting to a niche (specific language, specific compliance need) or partnering rather than competing head-on. |

---

## 8) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| **LLM provider changes terms** (raises prices, changes data retention, degrades quality) | M | H | Maintain fallback provider (dual-vendor architecture). Negotiate committed pricing. Monitor quality weekly. | Engineering Lead |
| **Model quality insufficient for test generation** (tautological or non-compiling tests) | M | M | Extensive offline evals before launch. Gate test generation behind quality threshold. Delay feature if quality bar not met. | ML Lead |
| **Beta customers churn due to quality issues** in early weeks | M | H | Set expectations clearly during onboarding ("beta, improving weekly"). Fast iteration cycle (weekly model/prompt updates). Dedicated CS contact per beta customer. | Product Lead |
| **Competitor launches before our GA** (GitHub Copilot improvements, JetBrains AI) | H | M | Focus on differentiation (security, mid-market fit, codebase-aware context). Accelerate timeline if feasible. Avoid feature-for-feature competition. | VP Product |
| **SOC 2 audit delays block GA** | M | H | Start audit process in Week 6 (not Week 12). Engage audit firm early. Assign dedicated compliance owner. | Legal/Compliance |
| **Internal team capacity** -- 8-week beta timeline is aggressive | M | H | Scope to 3 features only for beta (completions, explanations, test gen). No scope creep. Defer JetBrains and PR review to post-beta. | Engineering Lead |
| **Prompt injection attack succeeds** in production, causing data leakage or harmful output | L | H | Red team pre-beta. Safety filters. Instruction hierarchy. Monitoring and alerting. Incident response plan. | Security Lead |
| **Cost model breaks at scale** -- per-user cost higher than projected | M | H | Load test with realistic patterns pre-beta. Implement cost monitoring from Day 1. Have cost optimization playbook ready (caching, routing, context compression). | Engineering Lead |

### Open Questions

- **OQ1:** Which LLM provider should be primary (Claude vs. GPT-4o vs. both)? Decision depends on latency benchmarking, pricing negotiation, and zero-data-retention contract terms. Target decision: Week 2.
- **OQ2:** Should codebase indexing happen on-device (local) or in a secure backend? On-device is more private but harder to maintain; backend is faster to iterate but requires tenant isolation infrastructure. Target decision: Week 2.
- **OQ3:** What is the right pricing model for mid-market? Per-seat subscription? Usage-based? Freemium with paid tier? Needs market research and competitive analysis. Target decision: Week 10 (before GA).
- **OQ4:** How do we handle open-source attribution? If the model suggests code that closely matches a GPL/LGPL-licensed project, do we flag it? What is our legal exposure? Target decision: Week 4 (legal review).
- **OQ5:** Should we invest in a fine-tuned model for GA, or will prompt engineering + RAG be sufficient? Depends on beta quality data and cost analysis. Target decision: Week 14.
- **OQ6:** What is the right internal team size/structure? Do we need a dedicated ML engineer, or can we rely on prompt engineering + commercial APIs? Target decision: Week 2 (staffing plan).

### Next Steps (Weeks 1--2)

1. **[Product Lead, Week 1]** Circulate this strategy pack for review. Schedule strategy approval meeting for end of Week 1.
2. **[Engineering Lead, Week 1]** Set up LLM API access (Anthropic + Azure OpenAI). Run initial latency and cost benchmarks with representative code prompts.
3. **[ML Lead, Week 1]** Build v0 offline eval suite (50 test cases for inline completions). Establish baseline quality scores.
4. **[Security Lead, Week 1]** Begin security architecture review. Draft data flow diagram for LLM API integration. Review zero-data-retention contract terms.
5. **[Engineering Lead, Week 1--2]** Scaffold VS Code extension prototype. Get end-to-end "type code, get suggestion" working locally.
6. **[Product Lead, Week 2]** Finalize beta customer shortlist (5--10 mid-market teams). Begin outreach for beta sign-up.
7. **[Legal/Compliance, Week 2]** Initiate SOC 2 readiness assessment. Draft customer DPA template.
8. **[ML Lead, Week 2]** Run codebase-aware context experiment (file-only vs. repo-context) on internal codebase. Report initial quality delta.

---

## Quality Gate: Self-Assessment

### Checklist Results

**1) Strategy thesis checklist**
- [x] Decision statement is explicit (what, by when, for whom).
- [x] Problem is user-centered with 4 evidence points.
- [x] "Why now" is concrete (model capability, cost curve, market demand, distribution).
- [x] Differentiation is defensible with 4 compounding levers (not "we use AI").
- [x] Non-goals are explicit (5 listed).
- [x] Assumptions listed with tests, metrics, owners, and timeboxes (5 assumptions).

**2) Use-case portfolio checklist**
- [x] Portfolio lists 12 candidates.
- [x] Top 3 bets have clear target user + workflow anchor + measurable outcome.
- [x] Each selected bet includes "must-not-do" constraints.
- [x] Feasibility and risk assessed and tied to constraints.

**3) Autonomy policy checklist**
- [x] Form factor is minimum autonomy needed (copilot, not agent).
- [x] Action-taking capabilities have approval model, permission scope, audit logs, and rollback.
- [x] "Must never do" list is explicit (7 items) and enforced via product + policy + evals.
- [x] Prompt injection / tool misuse plan included.

**4) System plan checklist**
- [x] Data sources explicit; prohibited data and governance constraints clear.
- [x] Eval plan includes offline tests with critical failure cases.
- [x] Online monitoring signals + cadence + owner defined.
- [x] Budgets explicit: cost, latency, reliability.
- [x] Non-determinism acknowledged with mitigation (fallbacks, guardrails, routing, temperature control).

**5) Empirical learning plan checklist**
- [x] Every key assumption has experiment + decision rule (6 experiments).
- [x] Instrumentation is concrete (8 event types) with owners.
- [x] Plan monitors both utility (acceptance rate, WAU) and risk (safety incidents, anomalous usage).
- [x] Rollout is staged and reversible (Prototype -> Internal -> Beta -> GA).

**6) Roadmap checklist**
- [x] Phases have entry/exit criteria.
- [x] Owners/DRIs named.
- [x] Risk retirement work included as first-class items (7 items).

**7) Final packaging checklist**
- [x] Pack includes Risks (8), Open questions (6), Next steps (8).
- [x] Major trade-offs stated (quality vs. cost vs. latency vs. autonomy).
- [x] Assumptions clearly labeled vs. facts.
- [x] Output is shareable as-is.

### Rubric Self-Score

| Dimension | Score | Rationale |
|---|---|---|
| 1) Decision clarity | 2/2 | Explicit "deciding X by Y for Z" with 5 non-goals |
| 2) Problem and "why now" | 2/2 | User-centered problem with 4 evidence points; 4 concrete "why now" factors |
| 3) Differentiation | 2/2 | 4 compounding levers (distribution, workflow integration, trust, data flywheel); explicitly states model choice is NOT a moat |
| 4) Strategy choices and non-goals | 2/2 | 5 choices + 5 non-goals; 5 assumptions with tests, metrics, owners, timeboxes |
| 5) Use-case portfolio quality | 2/2 | 12 candidates scored; top 3 with user + workflow + metric + constraints; rejected candidates have reasons |
| 6) Autonomy policy quality | 2/2 | Copilot-first; 6 capabilities with full permissions/audit/rollback; 7-item "must never do" list; prompt injection plan |
| 7) Eval + measurement plan | 2/2 | Offline (200+ cases, critical failure tests, quality bars) + online (quality, safety, escalation signals, weekly cadence, owners); non-determinism mitigated |
| 8) Data + governance readiness | 2/2 | Explicit sources + prohibited data + retention policy + privacy/compliance constraints |
| 9) Empirical learning plan quality | 2/2 | 6 experiments with hypothesis, metric, guardrail, timebox, owner, decision rule; staged rollout |
| 10) Roadmap executability | 2/2 | 5 phases with entry/exit criteria, owners, dates; 7 risk retirement items; kill criteria defined |
| **Total** | **20/20** | |

Passing bar: >= 16/20. **Score: 20/20. PASS.**
