# Technology Evaluation Pack: AI Guardrails Vendor for Customer-Facing Support Agent

---

## 1) Evaluation Brief

### Summary
- **Decision to make:** Adopt (or defer) a third-party AI guardrails vendor to protect a new customer-facing support agent from prompt injection and unsafe tool use.
- **Candidate technology:** AI guardrails vendor (category: prompt-injection detection / output filtering / tool-use policy enforcement). Specific vendor TBD pending shortlist -- representative vendors in this space include Lakera Guard, Robust Intelligence (Cisco), Prompt Armor, Pangea, and Calypso AI. Links to be gathered during shortlisting.
- **Owner:** Engineering lead (support-agent project DRI) -- to be named.
- **Decision deadline:** 3 weeks from kickoff (target: ~2026-04-07).
- **Stakeholders:** Security/InfoSec, backend engineering (support-agent team), data/privacy (DPO), legal/compliance, customer support ops, end users (customers interacting with the agent).

### Problem and context
- **Problem statement (1 sentence):** Our customer-facing support agent can invoke tools (e.g., look up orders, update tickets, search the KB) on behalf of users, and we currently have no systematic defense against prompt injection, data exfiltration, or unintended tool invocation that could expose PII or take harmful actions.
- **Who experiences the pain:**
  - **Customers** -- risk of receiving incorrect, manipulated, or harmful responses; risk of PII leakage.
  - **Support ops** -- reputational and compliance exposure from agent misbehavior.
  - **Security/compliance** -- SOC2 audit surface expands when an AI agent has tool access to PII-containing systems.
  - **Engineering** -- building ad-hoc safety checks without a framework is slow and error-prone.
- **Current approach/stack:**
  - Zendesk as the ticketing/support platform.
  - Internal knowledge base (KB) for agent retrieval.
  - No AI guardrails layer today -- the support agent is in development and has no production-grade safety controls beyond basic prompt engineering.
- **What's broken / too slow / too expensive / too risky:**
  - Prompt engineering alone is insufficient to prevent adversarial prompt injection in a customer-facing context.
  - No structured logging, alerting, or policy enforcement for tool calls made by the agent.
  - Without a guardrails layer, launching the support agent to customers would create unacceptable compliance and safety risk given PII in the system.
- **Non-goals:**
  1. We are NOT choosing the LLM provider itself (that decision is separate).
  2. We are NOT building a full AI safety research program -- we need a practical, deployable defense layer.
  3. We are NOT replacing Zendesk or the internal KB in this evaluation.
  4. We are NOT evaluating the support agent's conversational quality or accuracy (separate workstream).
  5. We are NOT performing a formal penetration test (that follows after vendor selection; this is a structured first-pass risk review).

### Success and constraints
- **Success metrics (leading):**
  - Guardrails layer blocks >= 95% of a curated red-team prompt-injection test suite within the pilot.
  - Mean latency overhead of the guardrails layer is < 300ms p95 per request.
  - Zero false-positive blocks on a representative set of 200 legitimate customer queries.
  - Engineering integration effort is <= 2 engineer-weeks.
- **Success metrics (lagging):**
  - Zero prompt-injection incidents in the first 90 days of production.
  - SOC2 auditor accepts the guardrails layer as a compensating control for AI tool use.
  - Support agent NPS / CSAT does not degrade vs. human-only baseline.
- **Hard constraints:**
  - SOC2 Type II compliance required (vendor must hold or be in progress).
  - PII is present in support conversations -- vendor must have a DPA, clear data retention/deletion policy, and must NOT train on customer data.
  - SSO (SAML/OIDC) required for vendor dashboard access.
  - Budget: <= $50,000/year all-in (license + implementation support).
  - Decision within 3 weeks; pilot must be completable within that window or immediately after.
  - SaaS deployment acceptable; on-prem not required but data must not leave approved regions (US/EU).
- **Deal breakers:**
  - Vendor trains on customer data by default with no opt-out.
  - No SOC2 Type II report (or credible timeline to one).
  - No SSO support.
  - Latency overhead > 500ms p95 (degrades customer experience unacceptably).
  - Annual cost > $50,000 at projected volume.
  - No API-based integration (requires only a UI -- we need inline, programmatic enforcement).
- **Assumptions (to verify):**
  - Support agent will handle ~10,000 conversations/month at launch, scaling to ~50,000/month within 12 months. [TO VERIFY with product/growth]
  - Zendesk integration will be via API/webhook, not a native Zendesk app. [TO VERIFY with eng]
  - The LLM provider's built-in content filtering is necessary but insufficient; we need an additional layer for prompt injection and tool-use policy. [TO VERIFY via red-team testing]

---

## 2) Options & Criteria Matrix

### Options

| Option | Description |
|---|---|
| **A: Status quo (no guardrails)** | Launch the support agent with prompt-engineering-only defenses. Add manual review for edge cases. |
| **B: Buy -- AI guardrails vendor** | Integrate a third-party guardrails vendor (e.g., Lakera Guard, Robust Intelligence, Prompt Armor) as an inline filter layer. |
| **C: Build -- custom guardrails layer** | Build an in-house prompt-injection classifier + tool-use policy engine using open-source models/libraries (e.g., rebuff, llm-guard, custom classifier). |
| **D: Hybrid -- vendor + custom hardening** | Use a vendor for baseline detection, supplemented by custom tool-use policies, human approval gates, and defense-in-depth controls we build ourselves. |

### Criteria

| Criterion | Weight | How we measure | A: Status quo | B: Buy vendor | C: Build | D: Hybrid | Notes |
|---|---:|---|---:|---:|---:|---:|---|
| **Problem fit (prompt-injection detection accuracy)** | 25% | Red-team test suite: % blocked | 1 | 4 | 3 | 4 | Status quo relies on prompt engineering alone. Build requires significant ML effort to match vendor accuracy. |
| **Workflow impact / risk reduction** | 25% | Reduction in unmitigated risk surface; enables launch | 1 | 4 | 3 | 5 | Hybrid gives deepest defense. Status quo likely blocks launch. |
| **Time-to-value** | 15% | Weeks to production-ready integration | 5 | 4 | 2 | 3 | Status quo is "free" but unsafe. Vendor is fastest safe option. Build takes 6-10 weeks minimum. |
| **Integration complexity** | 10% | Engineer-weeks to integrate; # of touchpoints | 5 | 3 | 2 | 2 | Vendor integration is API-based (~1-2 weeks). Build/hybrid require more custom work. |
| **Security/privacy/compliance** | 10% | SOC2, DPA, data handling, SSO | 2 | 4 | 4 | 4 | Status quo has no guardrails audit story. Vendor provides compliance artifacts. Build keeps data in-house. |
| **Total cost of ownership (12 mo)** | 10% | License + eng time + maintenance | 5 | 3 | 2 | 3 | Status quo costs nothing extra but carries incident cost risk. Build is expensive in eng bandwidth. |
| **Lock-in / exit path** | 5% | Data export, API abstraction, switching cost | 5 | 3 | 5 | 4 | Vendor creates dependency but can be abstracted behind an interface. Build has no lock-in. |
| **Weighted score** | -- | -- | **2.4** | **3.7** | **2.7** | **3.8** | Hybrid scores highest; pure vendor is close second. |

**Scoring notes:**
- Scores are 1-5 (1 = weak, 5 = strong). Weighted by importance.
- Status quo scores high on cost and simplicity but fails on the core problem (prompt-injection defense) and blocks launch.
- Build scores well on lock-in and compliance but poorly on time-to-value and bandwidth cost.

### Integration + data fit notes

- **Required integrations:**
  - SSO (SAML 2.0 or OIDC) for vendor dashboard/admin access.
  - REST API for inline request/response filtering (must support synchronous calls with < 300ms latency).
  - Audit log export (to our SIEM or logging pipeline) for SOC2 evidence.
  - Zendesk: the guardrails layer sits between the LLM orchestrator and Zendesk APIs, not inside Zendesk itself.
  - Internal KB: read-only; guardrails layer does not need direct KB access (the agent retrieves, guardrails layer inspects the prompt/response).
- **Data flow (inputs -> processing -> outputs):**
  1. Customer sends message via Zendesk chat/email.
  2. Support agent orchestrator receives message, retrieves context from KB and Zendesk ticket history.
  3. **Guardrails layer (input filter):** Inspects the assembled prompt for injection patterns, PII leakage risk, and policy violations BEFORE sending to the LLM.
  4. LLM generates a response + tool-call requests.
  5. **Guardrails layer (output filter):** Inspects LLM response and tool-call requests for unsafe content, PII exposure, and policy violations BEFORE executing tools or returning to customer.
  6. Tool calls (e.g., order lookup, ticket update) execute only if guardrails approve; high-risk actions require human approval.
  7. Final response delivered to customer via Zendesk.
  8. All guardrails decisions logged (allow/block/flag) for audit and evaluation.
- **Migration effort:** Minimal -- this is greenfield (the support agent is not yet in production). Integration is additive, not a migration.
- **Exit plan:**
  - Abstract the guardrails vendor behind an internal interface/adapter so switching vendors requires changing only the adapter implementation.
  - Ensure all guardrails configuration (policies, rules, thresholds) is stored in our own repo, not solely in the vendor's dashboard.
  - Contractual: negotiate annual contract with 30-day termination clause or monthly billing during the first year.

---

## 3) Build vs Buy Analysis

### Decision frame
- **What we would build (if Build):** A prompt-injection detection classifier (fine-tuned or rule-based), a tool-use policy engine (allowlist/denylist per tool, parameter validation), and a logging/alerting pipeline for blocked requests.
- **What we would buy (if Buy):** An inline API service that classifies prompt injection, enforces output policies, and provides a dashboard for configuration and audit logs.
- **What we would not do (non-goals):** We would not build a general-purpose AI safety research platform, a content moderation system for non-support use cases, or a replacement for the LLM provider's built-in content filters.

### Bandwidth / TCO ledger

| Cost area | Build (estimate) | Buy (estimate) | Notes |
|---|---|---|---|
| **Initial build/implementation** | 6-10 engineer-weeks (~$60k-$100k loaded cost) | 1-2 engineer-weeks integration (~$10k-$20k) + license setup | Build requires ML expertise for classifier training + policy engine development. |
| **Ongoing maintenance/upgrades** | 2-4 engineer-weeks/year (~$20k-$40k) for model retraining, new attack patterns, false-positive tuning | Vendor handles model updates; ~1 engineer-week/year for config tuning (~$10k) | Prompt injection is an adversarial, evolving threat -- maintenance is non-trivial for build. |
| **On-call/incident response** | Team owns 100% of incidents; guardrails failures are P1 | Vendor provides SLA + support; team owns integration-layer incidents | Vendor reduces on-call burden but does not eliminate it. |
| **Security/compliance work** | Self-audit; must produce own SOC2 evidence for this component | Vendor provides SOC2 report, DPA, pen-test summaries | Build creates more compliance work for our security team. |
| **Vendor management/procurement** | $0 | ~2 weeks procurement + legal review; $30k-$50k/year license | Vendor cost is real but predictable. |
| **Opportunity cost** | 6-10 weeks of eng time NOT spent on agent features, accuracy, or other projects | 1-2 weeks; team can focus on agent quality and launch | This is the critical factor -- we are a small team with a launch deadline. |
| **12-month total (est.)** | **$80k-$140k** (loaded eng cost) + ongoing risk of under-investment | **$50k-$70k** (license + integration + management) | Buy is cheaper and faster; build is only justified if vendor market is unacceptable. |

### Core competency check
- **Is this a differentiator for our business?** No. Prompt-injection defense is a security/infrastructure concern, not a product differentiator. Our differentiation is in the quality and helpfulness of the support agent, not in the safety plumbing.
- **If we build, do we have the expertise?** Partially. We have backend engineers who could build a policy engine, but we lack dedicated ML security expertise for building and maintaining a production-grade prompt-injection classifier against evolving attacks.
- **If we buy, are we comfortable with vendor dependency?** Yes, with mitigations: (1) abstract behind an adapter interface, (2) maintain our own tool-use policy layer as defense-in-depth, (3) negotiate contract flexibility. The vendor market for guardrails is maturing rapidly -- switching cost is manageable if we design for it.

**Build vs buy recommendation:** Buy (with custom hardening) -- i.e., Option D (Hybrid).

---

## 4) Proof-of-Value Pilot Plan

### Hypotheses
- **H1:** The guardrails vendor blocks >= 95% of prompt-injection attacks from a curated red-team test suite of 50+ attack patterns (direct injection, indirect injection, jailbreak, tool-abuse attempts).
- **H2:** The guardrails layer adds < 300ms p95 latency overhead per request at a throughput of 100 concurrent requests.
- **H3:** The false-positive rate on 200 representative legitimate customer queries is < 2% (i.e., fewer than 4 legitimate queries incorrectly blocked).

### Scope and timeline
- **Pilot scope (in):**
  - Integrate the vendor's API into the support agent's staging environment.
  - Run the red-team test suite (input injection + output filtering).
  - Run the legitimate-query test set (false-positive measurement).
  - Measure latency overhead under simulated load.
  - Verify SSO integration, audit log export, and DPA terms.
- **Pilot scope (out):**
  - No real customer traffic during the pilot.
  - No evaluation of the support agent's answer quality (separate workstream).
  - No formal penetration test (follows after adoption decision).
- **Pilot duration:** 5 business days (1 week), with 2 days for integration, 2 days for testing, 1 day for analysis and write-up.
- **Pilot users:** 2 engineers (support-agent team) + 1 security engineer for red-team testing.
- **Environment:** Staging environment with synthetic and anonymized data. No production PII used in the pilot.

### Measurement
- **Success metrics + thresholds:**

| Metric | Target | Method |
|---|---|---|
| Prompt-injection block rate | >= 95% of red-team suite | Automated test suite; manual verification of misses |
| False-positive rate | < 2% on 200 legitimate queries | Automated test; manual review of any blocks |
| Latency overhead (p95) | < 300ms | Load test with 100 concurrent requests |
| SSO integration | Working (pass/fail) | Manual verification |
| Audit log export | Structured logs available in our pipeline (pass/fail) | Manual verification |

- **Data collection plan:** All test results logged to a shared spreadsheet/dashboard. Latency measured via instrumented API calls. Red-team results categorized by attack type (direct injection, indirect injection, jailbreak, tool abuse, data exfiltration).
- **Evaluation method:** Scoring against the thresholds above. Red-team suite includes known-good attack patterns from public datasets (e.g., Gandalf, Tensor Trust, custom tool-abuse scenarios). Results reviewed by security engineer.

### Operational + safety plan
- **Permissions model:** Only the 2 pilot engineers and 1 security engineer have access to the vendor dashboard and staging environment. Vendor API key stored in secrets manager with access logging.
- **Human approval points:** N/A during pilot (all traffic is synthetic). In production, high-risk tool calls (e.g., account modifications, PII access) will require human approval -- this will be validated in the pilot's design review but not in live traffic.
- **Rollback plan:** The guardrails layer is a middleware component in staging. Rollback = disable the middleware and route requests directly to the LLM. Takes < 1 hour.
- **Data deletion/retention plan:** All pilot data is synthetic/anonymized. Vendor trial account and any data stored on vendor side to be deleted within 7 days of pilot completion. Request written confirmation of deletion.

### Exit criteria (binary)
- **Adopt if:** All three hypotheses (H1, H2, H3) pass AND no deal-breaker issues found (SOC2, SSO, data handling, cost).
- **Iterate if:** H1 passes but H2 or H3 are borderline (e.g., latency 300-500ms, false-positive rate 2-5%). Work with vendor on tuning; extend pilot by 3 days.
- **Reject if:** H1 fails (block rate < 90%), OR any deal-breaker issue is confirmed (no SOC2, no SSO, trains on data, cost > $50k), OR latency > 500ms with no vendor mitigation plan.

---

## 5) Risk & Guardrails Review

### Risk register (top 10)

| # | Risk | Likelihood | Impact | Owner | Mitigation | Status |
|---|---|---:|---:|---|---|---|
| 1 | **Vendor guardrails do not catch novel/sophisticated prompt injection attacks** | High | High | Security eng | Defense-in-depth: vendor guardrails are ONE layer. Add: tool-use policy engine (allowlist actions, validate parameters), human approval for high-risk actions, rate limiting, output scanning for PII, continuous red-team eval. Do NOT rely on vendor as sole defense. | Monitor |
| 2 | **Vendor processes/stores PII in a way that violates our compliance posture** | Medium | High | DPO / Legal | Require DPA before pilot. Confirm: no training on customer data, data retention < 30 days, deletion on request, sub-processor list reviewed. Use anonymized data in pilot. | Blocker (until DPA signed) |
| 3 | **Vendor does not hold SOC2 Type II** | Medium | High | Security eng | Require SOC2 report or bridge letter before contract. If only Type I or in progress, evaluate timeline and request compensating evidence (pen-test summary, architecture review). | Blocker (until verified) |
| 4 | **Latency overhead degrades customer experience** | Medium | Medium | Backend eng | Measure in pilot. Require < 300ms p95. Evaluate async/streaming options if borderline. Fallback: bypass guardrails for latency-sensitive paths with compensating controls (post-hoc audit). | Monitor |
| 5 | **False positives block legitimate customer queries** | Medium | Medium | Backend eng | Measure in pilot. Require < 2% false-positive rate. Implement a "soft block" mode: flag but don't block, with human review queue, during initial rollout. Tune thresholds with vendor. | Monitor |
| 6 | **Vendor lock-in: switching cost grows over time** | Low | Medium | Eng lead | Abstract vendor behind an adapter interface from day one. Store policies in our own repo. Negotiate contract with termination flexibility. Re-evaluate annually. | Monitor |
| 7 | **Vendor experiences outage; support agent is blocked** | Medium | Medium | Backend eng | Implement circuit breaker: if guardrails service is unavailable, degrade to safe mode (human-only routing) rather than unguarded agent responses. SLA requirement: 99.9% uptime. | Monitor |
| 8 | **Vendor raises prices or changes terms at renewal** | Low | Medium | Eng lead / Finance | Negotiate multi-year pricing or cap. Maintain the ability to switch (see #6). Budget for 20% annual increase in forecasting. | Monitor |
| 9 | **Red-team test suite is not comprehensive enough; false confidence** | Medium | High | Security eng | Use public attack datasets (Gandalf, Tensor Trust, OWASP LLM Top 10 examples) plus custom tool-abuse scenarios. Commit to quarterly red-team refreshes post-launch. Engage external red-team firm within 90 days of launch. | Monitor |
| 10 | **Team lacks bandwidth to complete pilot + integration in 3-week timeline** | Medium | Medium | Eng lead | Timebox pilot to 1 week. Assign 2 dedicated engineers. If timeline slips, defer launch rather than skip guardrails. | Monitor |

### Security/privacy/compliance prompts

- **What data is processed?** Customer support messages (contain PII: names, emails, order numbers, potentially payment info fragments), agent responses, tool-call requests and responses (ticket data, KB excerpts).
- **Where does data flow?** Customer -> Zendesk -> our orchestrator -> guardrails vendor API (prompt text + response text) -> LLM -> back through guardrails -> customer. The vendor sees prompt and response text.
- **Required controls:**
  - SSO (SAML 2.0 / OIDC) for vendor dashboard -- **deal breaker if absent**.
  - RBAC for vendor dashboard (admin vs. viewer roles).
  - Audit logs: all guardrails decisions (allow/block/flag) must be exportable to our logging pipeline.
  - Encryption: TLS 1.2+ in transit; encryption at rest for any stored data.
  - Data retention: vendor must retain request data for <= 30 days (or configurable), with deletion on request.
  - Data residency: US or EU (confirm which regions the vendor operates in).
- **Evidence to request from vendor:**
  - SOC2 Type II report (or bridge letter + timeline).
  - Penetration test summary (last 12 months).
  - DPA (Data Processing Agreement) with sub-processor list.
  - Incident response process documentation.
  - Data flow architecture diagram showing where customer data is processed and stored.

### AI-specific guardrails guidance

**Critical principle: Do NOT rely on the vendor's guardrails as the sole or primary security layer.**

Vendor claims like "blocks prompt injection" or "prevents jailbreaks" should be treated as marketing claims until independently verified. The reality of prompt-injection defense in 2026:

- No guardrails product catches 100% of attacks. Prompt injection is an unsolved problem in the research community. New attack vectors emerge continuously.
- Determined attackers (or even curious users) will find bypasses. The vendor's detection models have blind spots.
- "Guardrails" are a useful LAYER but must be part of defense-in-depth:

**Defense-in-depth architecture (required regardless of vendor choice):**

| Layer | Control | Owner |
|---|---|---|
| 1. Input filtering | Vendor guardrails: detect injection patterns in user input | Vendor + backend eng |
| 2. Prompt construction | Minimize injection surface: system prompt hardening, context isolation, input/instruction separation | Backend eng |
| 3. Tool-use policy | Allowlist of permitted tools + parameter validation. Agent cannot call tools outside the allowlist. High-risk tools (account changes, PII access) require human approval. | Backend eng |
| 4. Output filtering | Vendor guardrails: scan LLM output for PII leakage, policy violations, harmful content | Vendor + backend eng |
| 5. Rate limiting | Per-user and per-session rate limits on tool calls and message volume | Backend eng |
| 6. Logging & monitoring | Log all guardrails decisions, tool calls, and flagged interactions. Alert on anomalies. | Backend eng + security |
| 7. Human-in-the-loop | Escalation queue for flagged interactions. Human review for high-risk actions. | Support ops |
| 8. Continuous evaluation | Quarterly red-team testing. Monitor guardrails performance metrics. Retrain/update as attacks evolve. | Security eng |

---

## 6) Decision Memo

### Recommendation
- **Decision:** Adopt a guardrails vendor with custom hardening (Option D: Hybrid approach). Run a 1-week pilot to validate the top vendor candidate, then proceed to production integration if pilot passes.
- **Why this option wins:**
  1. **Fastest path to safe launch.** The support agent cannot ship to customers without a guardrails layer. A vendor provides production-grade detection in 1-2 weeks of integration vs. 6-10+ weeks to build.
  2. **Not a core competency.** Prompt-injection defense is security infrastructure, not our product differentiator. Buy the commodity; build the differentiation (agent quality, KB accuracy, workflow automation).
  3. **Defense-in-depth is non-negotiable regardless.** Even with a vendor, we must build tool-use policies, human approval gates, logging, and rate limiting. The hybrid approach ensures we are not solely dependent on any single layer.
  4. **Budget-feasible.** At $30k-$50k/year, the vendor fits within the $50k budget and is cheaper than the loaded engineering cost of building and maintaining an equivalent system.
  5. **Reversible.** By abstracting the vendor behind an adapter, we can switch vendors or move to a build if the market matures or our needs change.
- **Key trade-offs:**
  - We accept vendor dependency for a critical security component (mitigated by adapter abstraction and defense-in-depth).
  - We accept that no guardrails solution is perfect (mitigated by multi-layer defense and continuous red-teaming).
  - We spend $30k-$50k/year on a vendor instead of investing that in internal tooling (justified by faster time-to-market and lower total eng cost).

### Evidence summary
- **What evidence supports the recommendation:**
  - Build vs buy analysis shows vendor is 40-60% cheaper in year-one TCO and significantly faster.
  - AI security research consensus: prompt injection is an unsolved, adversarial problem that requires continuous model updates -- favoring a vendor with dedicated security research teams over in-house maintenance.
  - The defense-in-depth architecture ensures we are not solely reliant on vendor claims.
  - Pilot plan will provide first-party evidence before any contract is signed.
- **What assumptions remain unverified:**
  - Specific vendor's detection accuracy against our red-team suite (to be validated in pilot).
  - Latency overhead at our traffic patterns (to be validated in pilot).
  - Volume-based pricing at 50k conversations/month (to be confirmed with vendor).
  - SOC2 Type II status of the shortlisted vendor (to be confirmed before pilot).

### Adoption plan (if pilot passes)

| Phase | Timeline | Activities | Owner |
|---|---|---|---|
| **1. Vendor shortlist** | Week 1, Days 1-2 | Evaluate 2-3 vendors against deal-breakers (SOC2, SSO, pricing, API capability). Select top candidate for pilot. | Eng lead + Security eng |
| **2. Pilot** | Week 1, Day 3 - Week 2, Day 2 | Integrate in staging. Run red-team suite, false-positive tests, latency tests. Verify SSO, audit logs, DPA. | 2 backend eng + 1 security eng |
| **3. Pilot review** | Week 2, Day 3 | Evaluate pilot results against exit criteria. Go/no-go decision. | Eng lead + Security eng + DPO |
| **4. Contract & procurement** | Week 2, Day 4 - Week 3 | Negotiate contract (annual or monthly, termination clause). Sign DPA. Complete procurement. | Eng lead + Legal + Finance |
| **5. Production integration** | Week 3 - Week 5 | Integrate guardrails into production pipeline. Build adapter interface, tool-use policy layer, logging, circuit breaker, human escalation queue. | Backend eng team |
| **6. Staged rollout** | Week 5 - Week 7 | Roll out to 10% of support traffic (shadow mode: log but don't block). Validate in production. Increase to 50%, then 100%. | Backend eng + Support ops |
| **7. Post-launch monitoring** | Ongoing | Monitor guardrails metrics (block rate, false positives, latency). Quarterly red-team refresh. Annual vendor review. | Security eng + Backend eng |

- **Training/change management:** Support ops team briefed on the human escalation queue and how to handle flagged interactions. Engineering team trained on the adapter interface and guardrails configuration. Runbook created for guardrails service incidents.
- **Monitoring:** Dashboard tracking: block rate, false-positive rate, latency p50/p95/p99, guardrails service availability, human escalation volume. Alerts on: block-rate anomaly (sudden spike or drop), latency > 500ms, service downtime.

### Rollback / exit plan
- **How we revert:** The guardrails layer is middleware. Disable it by routing traffic directly to the LLM (circuit breaker pattern). If guardrails must be removed entirely, the adapter interface isolates all vendor-specific code -- remove or replace the adapter.
- **Rollback trigger:** If in the first 30 days of production: false-positive rate > 5%, latency > 500ms sustained, vendor SLA breached (< 99.5% uptime), or a critical security incident caused by guardrails failure.
- **If rollback is triggered:** Revert to human-only support routing (no AI agent) until the issue is resolved or an alternative vendor is integrated. Do NOT run the AI agent without guardrails.
- **Data export/deletion:** Request full data deletion from vendor within 30 days of contract termination. Confirm in writing. Our own logs are retained per our standard retention policy.
- **Contract guardrails:** Annual contract with 30-day termination clause (or monthly billing for year one). No auto-renewal without explicit approval. Annual review of vendor pricing, roadmap, and alternatives.

---

## 7) Risks / Open Questions / Next Steps

### Risks (summary)
| Risk | Owner | Status |
|---|---|---|
| Guardrails do not catch novel attacks (single-layer reliance) | Security eng | Mitigated by defense-in-depth architecture |
| Vendor data handling violates compliance | DPO / Legal | Blocker until DPA signed and reviewed |
| Vendor lacks SOC2 Type II | Security eng | Blocker until verified |
| Latency degrades CX | Backend eng | Monitor; validate in pilot |
| False positives block legitimate queries | Backend eng | Monitor; validate in pilot |
| Team bandwidth to meet 3-week timeline | Eng lead | Monitor; prioritize and assign dedicated resources |

### Open questions
1. **Which specific vendors to shortlist?** Need to evaluate Lakera Guard, Robust Intelligence (Cisco), Prompt Armor, Pangea, and Calypso AI against our deal-breakers. Are there others the security team recommends?
2. **What is the projected conversation volume at launch and at 12 months?** Needed for accurate pricing and load testing. (Assumption: 10k/mo launch, 50k/mo at 12 months -- to verify with product/growth.)
3. **Does the LLM provider offer built-in guardrails that partially overlap?** If so, how do we avoid paying for redundant filtering? (e.g., OpenAI content filtering, Anthropic usage policies.)
4. **What is the support agent's tool inventory?** Need the full list of tools the agent can invoke to build the tool-use policy allowlist. (To verify with the agent development team.)
5. **Who is the DRI for this evaluation?** Eng lead is assumed but should be formally assigned.
6. **What is the legal/procurement lead time?** Can we execute a contract within the 3-week timeline, or do we need to start procurement in parallel with the pilot?
7. **Will we engage an external red-team firm?** Recommended within 90 days of launch. Need budget and timeline for this.

### Next steps

| # | Action | Owner | Deadline |
|---|---|---|---|
| 1 | Assign DRI for the evaluation. Confirm projected conversation volumes with product/growth. | Eng lead | Day 1 |
| 2 | Shortlist 2-3 vendors against deal-breakers (SOC2, SSO, API, pricing). Request SOC2 reports, DPAs, and trial access. | Eng lead + Security eng | Day 2 |
| 3 | Build the red-team test suite (50+ attack patterns: direct injection, indirect injection, jailbreak, tool-abuse, data exfiltration). Use public datasets + custom scenarios. | Security eng | Day 3 |
| 4 | Curate the legitimate-query test set (200 representative customer queries, anonymized). | Support ops + Backend eng | Day 3 |
| 5 | Run the 1-week pilot with the top vendor candidate. | 2 backend eng + 1 security eng | Days 3-9 |
| 6 | Review pilot results against exit criteria. Make go/no-go recommendation. | Eng lead + Security eng + DPO | Day 10 |
| 7 | If go: initiate contract/procurement in parallel. Begin production integration. | Eng lead + Legal | Days 10-15 |
| 8 | Design and implement the defense-in-depth layers (tool-use policy, human approval, logging, circuit breaker) in parallel with vendor integration. | Backend eng team | Days 10-21 |
| 9 | Plan external red-team engagement within 90 days of launch. | Security eng | Day 15 |

---

## Quality Gate: Self-Assessment

### Checklist (from references/CHECKLISTS.md)

**Evaluation Pack completeness:**
- [x] Problem statement is tool-agnostic and tied to a real workflow.
- [x] Non-goals are explicit (5 listed).
- [x] Success metrics and deal breakers are defined.
- [x] Options include status quo + at least one credible alternative (4 options).
- [x] Criteria are measurable or falsifiable in a pilot.
- [x] Integration/data flow and migration effort are documented.
- [x] Build vs buy analysis includes bandwidth + opportunity cost.
- [x] Risk register lists top risks with owners and mitigations (or "blocker").
- [x] Pilot plan is time-boxed with exit criteria (adopt/iterate/reject).
- [x] Decision memo includes adoption plan and rollback/exit plan.
- [x] Risks / Open questions / Next steps are included.

**Build vs buy sanity:**
- [x] "Core competency" test is answered (not a differentiator).
- [x] Maintenance/on-call ownership is explicit (12-month view).
- [x] Hidden costs considered (security work, upgrades, support, training).
- [x] Vendor lock-in and exit plan are evaluated (adapter pattern, contract terms).
- [x] Decision is consistent with current team capacity and priorities.

**AI vendor due diligence:**
- [x] Data usage is clear (no training on customer data; DPA required).
- [x] Security posture evidence requested (SOC2, encryption, audit logs, SSO/RBAC).
- [x] Prompt injection/jailbreak risk considered; mitigations are defense-in-depth (8-layer architecture).
- [x] "Guardrails catch everything" claims are treated as unverified; tested in pilot/red-team.
- [x] Human approval points and logging are defined for action-taking behavior.

### Rubric scores (from references/RUBRIC.md)

| Dimension | Score | Rationale |
|---|---:|---|
| Problem clarity | 4 | Crisp problem statement with non-goals; stakeholders identified. Would be 5 with stakeholder sign-off (requires live alignment meeting). |
| Criteria quality | 4 | Criteria are measurable with pilot thresholds; weights assigned; deal-breakers explicit. Would be 5 once every criterion is validated in the pilot. |
| Options coverage | 5 | Status quo + vendor + build + hybrid all considered with trade-offs. |
| Evidence strength | 4 | Pilot plan with hypotheses, metrics, and timeline. Would be 5 after pilot results are in. |
| Build vs buy reasoning | 5 | TCO + bandwidth + opportunity cost + core competency + lock-in/exit all addressed. 12-month maintenance view included. |
| Risk management | 5 | Top 10 risks with owners, mitigations, blocker/monitor labels. AI guardrails claims treated skeptically with defense-in-depth architecture. |
| Decision readiness | 4 | Clear recommendation with rationale, adoption plan, and rollback plan. Would be 5 once DRI is formally assigned and procurement timeline confirmed. |

**Average score: 4.4** (exceeds the 4.0 threshold for customer-facing/sensitive-data evaluations)
**Risk management score: 5** (exceeds the >= 4 requirement)

---

*Technology Evaluation Pack produced using the `evaluating-new-technology` skill pack.*
