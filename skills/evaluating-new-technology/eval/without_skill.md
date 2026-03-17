# Technology Evaluation: AI Guardrails for Customer-Facing Support Agent

## 1. Executive Summary

We are evaluating AI guardrails solutions to secure a customer-facing support agent built on Zendesk and an internal knowledge base. The agent will handle customer inquiries autonomously, requiring robust protection against prompt injection, PII leakage, and unauthorized tool use. This evaluation assesses leading AI guardrails vendors against our security, compliance, and operational requirements within a $50k/yr budget and a 3-week decision timeline.

**Recommendation:** Pending vendor shortlist scoring (Section 8), but this document provides the framework and criteria for a defensible decision.

---

## 2. Problem Statement

### Business Context
We are deploying a customer-facing AI support agent that will interact directly with end users, access internal knowledge base content, and execute actions within Zendesk (e.g., updating tickets, issuing refunds, looking up order status). This introduces several risk vectors:

- **Prompt injection attacks**: Malicious users crafting inputs designed to override system instructions, exfiltrate data, or trigger unauthorized actions.
- **PII exposure**: The agent has access to customer records containing names, emails, addresses, payment information, and support history. Unguarded responses could leak PII from other customers or internal systems.
- **Unauthorized tool use**: The agent has access to Zendesk APIs and internal KB retrieval. Without guardrails, a compromised prompt could trigger bulk data exports, ticket modifications, or escalation bypasses.
- **Compliance risk**: As a SOC2-certified organization handling PII, any data breach or unauthorized access through the AI agent constitutes a compliance violation.

### Current State
- **Zendesk**: Primary customer support platform, contains ticket history, customer profiles, and macros.
- **Internal KB**: Proprietary knowledge base with product documentation, troubleshooting guides, and policy documents. Some content is internal-only and should never surface to customers.
- **No AI guardrails layer**: Currently relying on basic prompt engineering and system-message instructions, which are insufficient against adversarial inputs.

### Desired End State
A production-grade guardrails layer that sits between user inputs and the AI agent, and between the agent's outputs and the user, providing:
- Real-time prompt injection detection and blocking
- PII detection and redaction in both inputs and outputs
- Tool-use authorization and scope enforcement
- Audit logging for compliance
- Minimal latency impact on customer experience

---

## 3. Requirements

### 3.1 Functional Requirements

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| FR-1 | Detect and block prompt injection attempts in real time | Must-have | Must handle direct injection, indirect injection via retrieved content, and jailbreak attempts |
| FR-2 | Detect and redact PII in agent outputs before delivery to users | Must-have | Names, emails, phone numbers, addresses, SSNs, payment card numbers, account numbers |
| FR-3 | Detect and flag PII in user inputs for logging/audit purposes | Should-have | For compliance trail, not necessarily blocking |
| FR-4 | Enforce tool-use policies (allowlist/denylist actions per context) | Must-have | E.g., agent can read tickets but cannot bulk-export; refund limits enforced |
| FR-5 | Content filtering for harmful/toxic/off-topic outputs | Should-have | Prevent agent from generating inappropriate content |
| FR-6 | Topic guardrails to keep agent within support scope | Nice-to-have | Prevent agent from answering questions about competitors, politics, etc. |
| FR-7 | Hallucination detection / groundedness checking | Nice-to-have | Flag responses not grounded in KB content |

### 3.2 Non-Functional Requirements

| ID | Requirement | Priority | Threshold |
|----|------------|----------|-----------|
| NFR-1 | Latency overhead | Must-have | < 200ms p95 added latency per request |
| NFR-2 | Availability | Must-have | 99.9% uptime SLA |
| NFR-3 | Throughput | Must-have | Support 100+ concurrent conversations |
| NFR-4 | SOC2 Type II compliance | Must-have | Vendor must hold SOC2 Type II or be in active audit |
| NFR-5 | SSO integration | Must-have | SAML 2.0 or OIDC for admin dashboard access |
| NFR-6 | Data residency | Should-have | US data residency option |
| NFR-7 | Fail-open vs. fail-closed configurability | Must-have | Option to block requests when guardrails service is unavailable |

### 3.3 Integration Requirements

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| IR-1 | REST API / SDK for inline request interception | Must-have | Must support synchronous call pattern in the agent pipeline |
| IR-2 | Support for major LLM providers (OpenAI, Anthropic, etc.) | Must-have | Model-agnostic or multi-model support |
| IR-3 | Zendesk integration or webhook compatibility | Should-have | Native integration preferred; webhook/API fallback acceptable |
| IR-4 | Logging integration (Datadog, Splunk, or similar) | Should-have | For centralized monitoring and alerting |
| IR-5 | Admin dashboard for policy configuration | Must-have | Non-engineering staff should be able to update guardrail policies |

### 3.4 Budget and Timeline Constraints

- **Budget**: $50,000/year maximum (all-in: licensing, implementation, support)
- **Decision deadline**: 3 weeks from evaluation start
- **Target go-live**: Within 6 weeks of vendor selection
- **Implementation resources**: 1 senior backend engineer, 1 security engineer (part-time)

---

## 4. Vendor Landscape

### 4.1 Vendor Shortlist

Based on market research, the following vendors are identified for evaluation:

| Vendor | Category | Pricing Model | Est. Annual Cost |
|--------|----------|---------------|-----------------|
| **Lakera Guard** | Dedicated AI guardrails (prompt injection focus) | Per-API-call | $15k-$40k/yr |
| **Protect AI (Guardian)** | AI security platform | Per-model / per-app | $20k-$50k/yr |
| **Robust Intelligence (AI Firewall)** | AI firewall / guardrails | Platform license | $30k-$60k/yr |
| **Arthur AI (Arthur Shield)** | AI observability + guardrails | Platform license | $25k-$50k/yr |
| **Guardrails AI (open-source + cloud)** | Open-source framework + managed option | Free (OSS) / usage-based (cloud) | $0-$25k/yr |
| **NVIDIA NeMo Guardrails** | Open-source framework | Free (self-hosted) | $0 + infra costs |
| **Pangea (AI Guard)** | Security APIs including AI guard | Per-API-call | $10k-$30k/yr |
| **Custom/DIY** | In-house using open-source models | Engineering time | $15k-$25k/yr (eng time + infra) |

### 4.2 Eliminated Early

| Vendor | Reason for Elimination |
|--------|----------------------|
| **NVIDIA NeMo Guardrails** | Requires significant self-hosting infrastructure and ML expertise; no managed option; no SOC2 attestation for the tooling itself |
| **Custom/DIY** | 3-week timeline insufficient for building and validating custom injection detection; ongoing maintenance burden exceeds team capacity |

---

## 5. Evaluation Criteria and Scoring Framework

### Scoring Scale
- **5** = Exceeds requirements, best-in-class
- **4** = Fully meets requirements
- **3** = Meets requirements with minor gaps
- **2** = Partially meets requirements, workarounds needed
- **1** = Does not meet requirements
- **0** = Disqualifying gap

### Weighted Criteria

| Category | Weight | Criteria |
|----------|--------|----------|
| **Security Efficacy** | 30% | Prompt injection detection accuracy, PII detection coverage, false positive rate, bypass resistance |
| **Compliance & Trust** | 20% | SOC2 status, SSO support, audit logging, data handling practices, vendor security posture |
| **Integration & Architecture** | 20% | API design, SDK quality, Zendesk compatibility, latency overhead, deployment model |
| **Operational Maturity** | 15% | Admin dashboard, policy management, monitoring/alerting, documentation quality |
| **Cost & Commercial** | 15% | Total cost within budget, pricing transparency, contract flexibility, support tiers |

---

## 6. Detailed Vendor Assessment

### 6.1 Lakera Guard

**Overview:** Purpose-built prompt injection detection API. Strong focus on injection attacks with an evolving set of additional guardrails (PII, content moderation, unknown links).

| Criterion | Score | Notes |
|-----------|-------|-------|
| Prompt injection detection | 5 | Industry-leading detection; trained on large corpus of injection attacks; regularly updated |
| PII detection/redaction | 3 | Available but not as mature as dedicated PII vendors; covers common PII types |
| Tool-use enforcement | 2 | No native tool-use policy engine; would need custom implementation |
| SOC2 compliance | 4 | SOC2 Type II certified |
| SSO | 3 | SAML SSO available on enterprise plans |
| API/SDK quality | 4 | Clean REST API, Python SDK, low-latency (<100ms typical) |
| Zendesk integration | 2 | No native Zendesk integration; API-level integration required |
| Admin dashboard | 3 | Basic dashboard; policy configuration improving |
| Pricing fit | 4 | Usage-based pricing fits within $50k for expected volume |
| Overall | **3.5** | Strong on core injection detection; gaps in tool-use and broader guardrails |

**Strengths:**
- Best-in-class prompt injection detection
- Low latency API
- Proven in production at scale
- Straightforward integration

**Weaknesses:**
- Limited tool-use policy enforcement (would need supplementary solution)
- PII detection is secondary capability
- Relatively narrow feature set compared to full-platform vendors

---

### 6.2 Protect AI (Guardian)

**Overview:** Comprehensive AI security platform including model scanning, LLM firewalling, and runtime guardrails.

| Criterion | Score | Notes |
|-----------|-------|-------|
| Prompt injection detection | 4 | Strong detection with multiple model-based classifiers |
| PII detection/redaction | 4 | Comprehensive PII detection with configurable redaction |
| Tool-use enforcement | 3 | Policy engine for restricting model capabilities; evolving |
| SOC2 compliance | 4 | SOC2 Type II certified |
| SSO | 4 | Full SAML/OIDC support |
| API/SDK quality | 3 | SDK available; API docs adequate; some complexity in setup |
| Zendesk integration | 2 | No native integration; API/webhook required |
| Admin dashboard | 4 | Full-featured dashboard with policy builder |
| Pricing fit | 3 | Can fit within budget on standard tier; enterprise features may push beyond |
| Overall | **3.4** | Comprehensive platform but potentially more than needed; moderate integration effort |

**Strengths:**
- Broad coverage of AI security concerns beyond just guardrails
- Good compliance posture
- Active policy management interface
- Model-scanning capabilities (useful for future state)

**Weaknesses:**
- Platform complexity may be overkill for current use case
- Pricing could exceed budget at scale
- Integration requires more upfront engineering effort

---

### 6.3 Robust Intelligence (AI Firewall)

**Overview:** Enterprise AI security platform with "AI Firewall" product for real-time input/output validation.

| Criterion | Score | Notes |
|-----------|-------|-------|
| Prompt injection detection | 4 | Robust detection; enterprise-validated |
| PII detection/redaction | 4 | Built-in PII scanning with configurable sensitivity |
| Tool-use enforcement | 3 | Action-level policies configurable per application |
| SOC2 compliance | 4 | SOC2 Type II certified |
| SSO | 4 | Full SSO support |
| API/SDK quality | 3 | Well-documented API; Python/Node SDKs |
| Zendesk integration | 2 | No native integration |
| Admin dashboard | 4 | Enterprise-grade dashboard with analytics |
| Pricing fit | 2 | Typically targets larger enterprises; $50k may be entry-level with limited features |
| Overall | **3.2** | Strong enterprise product but potentially over-budget and over-engineered for current needs |

**Strengths:**
- Enterprise-proven at scale
- Comprehensive security analytics and reporting
- Strong compliance documentation
- Continuous model for guardrail updates

**Weaknesses:**
- Pricing likely at or above budget ceiling
- Sales cycle may not fit 3-week timeline
- Feature richness comes with integration complexity

---

### 6.4 Arthur AI (Arthur Shield)

**Overview:** AI observability platform with Shield product for real-time guardrails on LLM applications.

| Criterion | Score | Notes |
|-----------|-------|-------|
| Prompt injection detection | 3 | Adequate detection; more focused on observability |
| PII detection/redaction | 4 | Strong PII detection as part of broader data quality focus |
| Tool-use enforcement | 2 | Limited native tool-use policy enforcement |
| SOC2 compliance | 4 | SOC2 Type II certified |
| SSO | 4 | Full SSO support on enterprise plan |
| API/SDK quality | 4 | Clean SDK; good documentation |
| Zendesk integration | 2 | No native integration |
| Admin dashboard | 5 | Excellent observability dashboard; best-in-class monitoring |
| Pricing fit | 3 | Fits budget on standard tier; observability features add value |
| Overall | **3.3** | Excellent observability but guardrails are secondary to monitoring focus |

**Strengths:**
- Best-in-class observability and monitoring
- Strong PII detection
- Good SDK and developer experience
- Useful beyond guardrails (LLM monitoring, evaluation)

**Weaknesses:**
- Prompt injection detection not as specialized as Lakera
- Tool-use enforcement is limited
- Guardrails feel like an add-on to the observability platform

---

### 6.5 Guardrails AI (Open Source + Cloud)

**Overview:** Open-source Python framework for adding guardrails to LLM applications, with an optional managed cloud offering.

| Criterion | Score | Notes |
|-----------|-------|-------|
| Prompt injection detection | 3 | Community validators available; quality varies; can plug in external models |
| PII detection/redaction | 3 | PII validators available (regex + NER-based) |
| Tool-use enforcement | 4 | Flexible validator framework allows custom tool-use policies |
| SOC2 compliance | 2 | Cloud offering is newer; SOC2 status uncertain; self-hosted option available |
| SSO | 2 | Cloud dashboard SSO may be limited; self-hosted N/A |
| API/SDK quality | 4 | Excellent Python SDK; well-designed validator architecture |
| Zendesk integration | 2 | No native integration; custom validators needed |
| Admin dashboard | 2 | Cloud dashboard is basic; self-hosted has no dashboard |
| Pricing fit | 5 | Open-source core is free; cloud pricing very competitive |
| Overall | **3.0** | Maximum flexibility and cost efficiency; compliance and maturity concerns |

**Strengths:**
- Open-source core provides full control and customization
- Extensible validator architecture for custom guardrails
- Most cost-effective option
- Strong community and ecosystem
- Tool-use enforcement is naturally built into the framework

**Weaknesses:**
- SOC2 compliance uncertain for cloud offering
- Requires more engineering effort to deploy and maintain
- Detection quality depends on chosen validators
- No enterprise support guarantees on open-source tier

---

### 6.6 Pangea (AI Guard)

**Overview:** Security-as-a-service APIs including AI Guard for LLM content filtering, prompt injection, and PII handling.

| Criterion | Score | Notes |
|-----------|-------|-------|
| Prompt injection detection | 3 | Adequate detection; part of broader security API suite |
| PII detection/redaction | 4 | Strong PII handling leveraging existing Redact API |
| Tool-use enforcement | 2 | No native tool-use policy engine |
| SOC2 compliance | 4 | SOC2 Type II certified (strong security focus overall) |
| SSO | 4 | Full SSO support |
| API/SDK quality | 4 | Clean, well-documented APIs; multiple SDK languages |
| Zendesk integration | 2 | No native integration |
| Admin dashboard | 3 | Functional dashboard for API management |
| Pricing fit | 4 | Usage-based pricing fits budget well |
| Overall | **3.2** | Good security pedigree and PII handling; prompt injection not as specialized |

**Strengths:**
- Strong security company DNA (founded by ex-security leaders)
- Excellent PII redaction capabilities
- Competitive pricing
- Broader security API suite (AuthN, Vault, etc.) could add future value

**Weaknesses:**
- AI guardrails are newer addition to their platform
- Prompt injection detection less proven than specialists
- Tool-use enforcement gaps

---

## 7. Comparison Matrix

| Criterion (Weight) | Lakera Guard | Protect AI | Robust Intel. | Arthur AI | Guardrails AI | Pangea |
|-------------------|-------------|-----------|--------------|----------|--------------|--------|
| **Security Efficacy (30%)** | 4.0 | 3.8 | 3.8 | 3.0 | 3.2 | 3.0 |
| **Compliance & Trust (20%)** | 3.6 | 4.0 | 4.0 | 4.0 | 2.0 | 4.0 |
| **Integration & Arch. (20%)** | 3.5 | 3.0 | 3.0 | 3.5 | 3.5 | 3.5 |
| **Ops Maturity (15%)** | 3.0 | 4.0 | 4.0 | 4.5 | 2.0 | 3.0 |
| **Cost & Commercial (15%)** | 4.0 | 3.0 | 2.0 | 3.0 | 5.0 | 4.0 |
| **Weighted Total** | **3.65** | **3.52** | **3.42** | **3.45** | **3.02** | **3.42** |

---

## 8. Risk Analysis

### 8.1 Vendor Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Vendor goes out of business (startup risk) | Medium | High | Prefer vendors with strong funding; ensure API abstraction layer for portability |
| Guardrails bypassed by novel attack | Medium | High | Layer defenses: guardrails + output validation + rate limiting + human escalation |
| Latency degrades customer experience | Low | Medium | Require SLA with latency guarantees; implement async fallback patterns |
| False positives block legitimate customers | Medium | Medium | Tune sensitivity thresholds; implement override/escalation flow; monitor FP rate |
| Vendor raises prices significantly | Medium | Medium | Negotiate multi-year pricing; maintain portability layer |
| SOC2 attestation lapses | Low | High | Require notification clause in contract; annual verification |

### 8.2 Implementation Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Integration more complex than estimated | Medium | Medium | Allocate buffer in timeline; start with PoC before full rollout |
| Agent performance degradation with guardrails | Medium | Medium | Load test during PoC; establish latency budgets |
| Guardrails conflict with legitimate agent capabilities | Medium | Low | Iterative policy tuning during staged rollout |
| Team lacks expertise to configure/maintain | Low | Medium | Select vendor with strong documentation and support; prefer managed solutions |

---

## 9. Proof of Concept Plan

### 9.1 PoC Objectives
1. Validate prompt injection detection accuracy against our threat model
2. Measure latency impact under realistic load
3. Verify PII detection/redaction accuracy
4. Test integration with our agent pipeline (Zendesk + KB)
5. Evaluate admin experience for policy management

### 9.2 PoC Structure

**Duration:** 5 business days per vendor (run top 2 candidates in parallel)

**Test Dataset:**
- 50 benign customer support queries (baseline)
- 30 prompt injection attempts (direct injection, indirect via context, jailbreaks)
- 20 queries containing PII in various formats
- 10 queries attempting to trigger unauthorized tool use

**Success Criteria:**
| Metric | Target |
|--------|--------|
| Prompt injection detection rate | > 95% |
| False positive rate on benign queries | < 5% |
| PII detection rate | > 98% |
| P95 latency overhead | < 200ms |
| Integration effort | < 3 engineering days |

### 9.3 PoC Timeline

| Week | Activity |
|------|----------|
| Week 1 | Finalize shortlist (top 2), sign PoC agreements, set up test environment |
| Week 2 | Run PoC testing (parallel), collect metrics |
| Week 3 | Analyze results, vendor Q&A, final decision and contract negotiation |

---

## 10. Architectural Integration Design

### 10.1 Target Architecture

```
Customer (Zendesk)
    |
    v
[Zendesk Webhook / API Gateway]
    |
    v
[Input Guardrails Layer]  <-- Prompt injection detection, input PII flagging
    |
    v
[AI Support Agent]  <-- LLM + KB retrieval + Zendesk tools
    |
    v
[Output Guardrails Layer]  <-- PII redaction, content filtering, response validation
    |
    v
[Zendesk Response / Customer]
```

### 10.2 Key Design Decisions

1. **Synchronous inline pattern**: Guardrails must be in the critical path (not async) to block dangerous content before it reaches the customer.
2. **Fail-closed default**: If the guardrails service is unavailable, route to human agent rather than letting unguarded responses through.
3. **Separation of input and output guardrails**: Different policies for each direction (e.g., we want to detect injection on input but redact PII on output).
4. **Abstraction layer**: Wrap vendor API calls in an internal interface to enable vendor switching without agent code changes.
5. **Audit logging**: All guardrail decisions (pass, block, redact) logged with request context for compliance and tuning.

---

## 11. Total Cost of Ownership (3-Year View)

| Cost Component | Year 1 | Year 2 | Year 3 | Total |
|---------------|--------|--------|--------|-------|
| Vendor licensing | $35,000 | $38,000 | $41,000 | $114,000 |
| Implementation (engineering) | $15,000 | $0 | $0 | $15,000 |
| Ongoing maintenance (eng time) | $5,000 | $8,000 | $8,000 | $21,000 |
| Infrastructure (if needed) | $2,000 | $2,000 | $2,000 | $6,000 |
| **Total** | **$57,000** | **$48,000** | **$51,000** | **$156,000** |

*Note: Year 1 exceeds $50k budget due to one-time implementation costs. Recommend treating implementation as a separate engineering budget line item, keeping recurring licensing within the $50k/yr envelope.*

---

## 12. Recommendation

### Primary Recommendation: Lakera Guard

**Rationale:**
- Highest weighted score (3.65) driven by best-in-class prompt injection detection, which is our primary threat vector
- Within budget at expected usage levels
- Lowest integration complexity and fastest time-to-value
- SOC2 Type II certified with SSO support
- Low latency overhead aligns with customer experience requirements

**Gap Mitigation:**
- Tool-use enforcement gap: Implement lightweight custom middleware using allow/deny lists for Zendesk API calls (estimated 2 days engineering)
- PII detection supplement: Consider layering Pangea Redact API specifically for PII if Lakera's PII detection proves insufficient during PoC

### Secondary Recommendation: Protect AI (Guardian)

**Rationale:**
- Most comprehensive single-vendor solution
- Strong compliance posture
- Better native tool-use policy enforcement
- Consider if tool-use enforcement is deemed critical and custom implementation is undesirable

**Caveat:** Confirm pricing fits within budget during PoC negotiation; platform complexity may slow initial deployment.

---

## 13. Decision Framework

### Go / No-Go Criteria After PoC

| Criterion | Go Threshold | No-Go Threshold |
|-----------|-------------|-----------------|
| Injection detection rate | >= 95% | < 85% |
| False positive rate | <= 5% | > 10% |
| PII detection rate | >= 98% | < 90% |
| P95 latency | <= 200ms | > 500ms |
| SOC2 verified | Confirmed | Not available |
| SSO verified | Working | Not available |
| Annual cost confirmed | <= $50k | > $60k |
| Integration PoC | Completed in <= 3 days | > 5 days |

### Escalation Path
If no vendor meets Go thresholds across all criteria:
1. Re-evaluate with relaxed thresholds and compensating controls
2. Consider hybrid approach (e.g., Lakera for injection + Pangea for PII)
3. Extend timeline by 2 weeks for additional vendor evaluation
4. Escalate to VP Engineering for budget increase if needed

---

## 14. Next Steps

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Review and approve evaluation criteria with security team | Security Lead | Day 2 |
| 2 | Contact Lakera and Protect AI for PoC access and pricing | Engineering Lead | Day 3 |
| 3 | Prepare test dataset (injection attacks, PII samples, benign queries) | ML Engineer | Day 5 |
| 4 | Set up isolated test environment mirroring production pipeline | Backend Engineer | Day 5 |
| 5 | Execute PoC for both vendors (parallel) | Engineering Team | Day 10 |
| 6 | Compile PoC results and present to stakeholders | Engineering Lead | Day 12 |
| 7 | Final vendor selection and contract negotiation | Engineering Lead + Procurement | Day 15 |
| 8 | Procurement and legal review | Legal/Procurement | Day 18 |
| 9 | Decision sign-off | VP Engineering | Day 21 |

---

*Document prepared for internal evaluation purposes. Vendor scores are estimates based on publicly available information and should be validated during proof-of-concept testing.*
