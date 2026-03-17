# Enterprise Deal Execution Pack

**Deal Parameters**
- ACV: ~$80,000
- Timeline: 6 weeks (close target)
- Champion: Ops stakeholder
- Economic Buyer: Finance
- Security Review: IT
- Blockers: Procurement vendor onboarding + security questionnaire

---

## 1. Mutual Action Plan (MAP)

### Overview

This mutual action plan outlines the shared milestones, owners, and deadlines required to complete evaluation and procurement within the 6-week window. Both parties commit to the dates below; any slippage should be flagged within 24 hours.

### Week-by-Week Plan

| Week | Milestone | Owner | Due Date | Status |
|------|-----------|-------|----------|--------|
| **Week 1** | Kick-off alignment call — confirm evaluation criteria, success metrics, and decision process | Seller + Ops Champion | Week 1, Day 1 | Not Started |
| Week 1 | Share ROI / business case draft with Ops Champion for internal circulation | Seller | Week 1, Day 3 | Not Started |
| Week 1 | Ops Champion circulates business case to Finance (Economic Buyer) | Ops Champion | Week 1, Day 5 | Not Started |
| Week 1 | Submit vendor onboarding intake form to Procurement | Seller | Week 1, Day 5 | Not Started |
| **Week 2** | Technical deep-dive / demo for IT + Ops | Seller (SE) | Week 2, Day 1 | Not Started |
| Week 2 | Deliver completed security questionnaire to IT | Seller | Week 2, Day 2 | Not Started |
| Week 2 | Finance confirms budget availability and approval path | Finance (Econ Buyer) | Week 2, Day 5 | Not Started |
| **Week 3** | IT begins security review of questionnaire + documentation | IT Security | Week 3, Day 1 | Not Started |
| Week 3 | Address any follow-up security questions (SLA: 24-hour turnaround) | Seller | Week 3, ongoing | Not Started |
| Week 3 | Procurement reviews vendor onboarding package and flags gaps | Procurement | Week 3, Day 3 | Not Started |
| Week 3 | Mid-deal checkpoint call — Seller + Champion + Finance | All | Week 3, Day 5 | Not Started |
| **Week 4** | IT security review complete — conditional or full approval | IT Security | Week 4, Day 3 | Not Started |
| Week 4 | Procurement vendor onboarding complete | Procurement | Week 4, Day 5 | Not Started |
| Week 4 | Final commercial terms shared (order form / SOW) | Seller | Week 4, Day 5 | Not Started |
| **Week 5** | Legal redlines exchanged (if applicable) | Legal / Seller | Week 5, Day 3 | Not Started |
| Week 5 | Finance signs off on final pricing and payment terms | Finance (Econ Buyer) | Week 5, Day 5 | Not Started |
| **Week 6** | Final contract sent for e-signature | Seller | Week 6, Day 1 | Not Started |
| Week 6 | Contract fully executed | All | Week 6, Day 3 | Not Started |
| Week 6 | Kickoff onboarding / implementation planning | Seller (CS) | Week 6, Day 5 | Not Started |

### Key Assumptions

- Both parties agree to respond to requests within 2 business days unless otherwise noted.
- Security questionnaire will be pre-completed by the seller before submission.
- No net-new legal entity or contracting entity changes are required.
- Budget has been directionally approved; Finance confirmation in Week 2 is a formality, not a new ask.

### Escalation Protocol

- If any milestone slips by more than 3 business days, both parties will schedule a same-week escalation call.
- Seller executive sponsor and buyer executive sponsor will be looped in if the deal risks missing the 6-week window.

---

## 2. Procurement & Security Tracker

### 2A. Procurement — Vendor Onboarding Tracker

| # | Requirement | Description | Owner | Status | Date Submitted | Date Completed | Notes |
|---|-------------|-------------|-------|--------|----------------|----------------|-------|
| P1 | Vendor registration form | Complete buyer's vendor portal registration (W-9, bank details, entity info) | Seller | Not Started | — | — | Request form from Procurement Day 1 |
| P2 | Certificate of Insurance (COI) | Provide current COI meeting buyer's minimum coverage thresholds | Seller | Not Started | — | — | Typical: $1M general liability, $5M umbrella |
| P3 | Business references | Provide 2–3 customer references (ideally same industry) | Seller | Not Started | — | — | Prep references in advance; notify them |
| P4 | Financial stability documentation | D&B report, audited financials, or similar proof of solvency | Seller | Not Started | — | — | If startup, prepare investor backing narrative |
| P5 | Diversity / sustainability certifications | Any applicable certifications (minority-owned, B-Corp, etc.) | Seller | Not Started | — | — | Check if buyer requires these |
| P6 | Standard contract / terms review | Buyer Procurement reviews seller's standard MSA / order form | Procurement + Legal | Not Started | — | — | Flag non-standard terms early |
| P7 | PO issuance | Purchase order created after all approvals | Procurement | Not Started | — | — | Requires security + Finance sign-off first |

### 2B. Security Review Tracker

| # | Requirement | Description | Owner | Status | Date Submitted | Date Completed | Notes |
|---|-------------|-------------|-------|--------|----------------|----------------|-------|
| S1 | Security questionnaire (SIG / CAIQ / custom) | Complete buyer's security questionnaire in full | Seller (Security team) | Not Started | — | — | Identify format early — SIG Lite vs. full SIG vs. custom |
| S2 | SOC 2 Type II report | Provide current SOC 2 Type II report (or bridge letter if in audit) | Seller | Not Started | — | — | Must be <12 months old |
| S3 | Penetration test summary | Executive summary of most recent third-party pen test | Seller | Not Started | — | — | Redact as needed; provide under NDA |
| S4 | Data processing addendum (DPA) | Signed DPA if personal data is processed | Seller + Legal | Not Started | — | — | Check if GDPR, CCPA, or HIPAA applies |
| S5 | Architecture / data flow diagram | High-level diagram showing data ingestion, storage, processing, and egress | Seller (SE) | Not Started | — | — | Clarify tenant isolation model |
| S6 | Encryption standards | Documentation of encryption at rest + in transit | Seller | Not Started | — | — | AES-256, TLS 1.2+ expected |
| S7 | Incident response plan | Summary of IR plan and SLAs for breach notification | Seller | Not Started | — | — | Buyer may require ≤72-hour notification |
| S8 | Sub-processor list | List of third-party sub-processors with data access | Seller | Not Started | — | — | Common ask under GDPR frameworks |
| S9 | Access control documentation | SSO/SAML support, RBAC model, MFA enforcement | Seller | Not Started | — | — | Confirm IdP compatibility |
| S10 | Follow-up Q&A | Address any clarifications or gaps from IT review | Seller + IT | Not Started | — | — | Target 24-hour SLA on responses |

### Tracker Usage Notes

- Update status weekly (Not Started / In Progress / Submitted / Approved / Blocked).
- Flag any item as "Blocked" immediately and note the blocker in the Notes column.
- Items S1–S3 are typically the long poles; submit these in Week 1–2 to stay on timeline.
- Assign a single internal DRI (directly responsible individual) on the seller side to chase all procurement and security items.

---

## 3. Champion Enablement One-Pagers

### 3A. One-Pager: Internal Business Case (For Champion to Share with Finance)

**Title: Business Case Summary — [Your Product Name]**

**The Problem**
- [1–2 sentences describing the operational pain the champion's team faces today. Be specific: hours lost, error rates, manual processes, revenue leakage, etc.]
- Current cost of inaction: $___/year (quantify if possible — headcount hours, missed SLAs, rework costs).

**The Proposed Solution**
- [Your Product] automates/streamlines [specific workflow], reducing [metric] by [X%] based on benchmarks from similar customers.
- Deployment model: [SaaS / on-prem / hybrid]. No infrastructure changes required on buyer side.

**Financial Summary**

| Item | Detail |
|------|--------|
| Annual Contract Value | ~$80,000 |
| Payment terms | Annual upfront (or quarterly — confirm) |
| Expected ROI | [X]x within [Y] months |
| Payback period | [Z] months |
| Hard savings | $___/year (reduced headcount, eliminated tool, etc.) |
| Soft savings | $___/year (time savings, error reduction, faster cycle times) |
| Total cost of ownership (3-yr) | ~$240,000 (assuming flat renewal) |

**Why Now**
- [Tie to a business trigger: fiscal year planning, regulatory deadline, leadership initiative, competitive pressure, team scaling challenge.]
- Delaying by one quarter costs approximately $_____ in continued inefficiency.

**Risk Mitigation**
- Security review underway with IT — on track for approval by Week 4.
- Vendor onboarding with Procurement initiated — standard process, no unusual requirements.
- [X] similar-sized companies in our industry are already live (reference available).

**Ask**
- Finance to confirm budget allocation by [date — Week 2].
- Approve final order form by [date — Week 5].

---

### 3B. One-Pager: Security & Compliance Summary (For Champion to Share with IT)

**Title: Security Overview — [Your Product Name]**

**Architecture**
- Deployment: Multi-tenant SaaS hosted on [AWS / Azure / GCP], region [US-East / EU-West / specify].
- Tenant isolation: [Logical / physical separation at database level].
- Data residency: Customer data stored in [region]. No cross-border transfers unless specified.

**Compliance & Certifications**
- SOC 2 Type II (current report available under NDA)
- [ISO 27001 / HIPAA / GDPR / FedRAMP — list all applicable]
- Annual third-party penetration testing (summary available)
- GDPR-compliant DPA available for execution

**Data Security**
- Encryption at rest: AES-256
- Encryption in transit: TLS 1.2+
- Key management: [AWS KMS / Azure Key Vault / customer-managed keys available]
- Data retention: Configurable; default [X] days. Customer can request deletion at any time.

**Access Control**
- SSO/SAML 2.0 supported (compatible with Okta, Azure AD, OneLogin, etc.)
- Role-based access control (RBAC) with admin-configurable permissions
- MFA enforced for all accounts
- Audit logging with export capability

**Incident Response**
- Dedicated security team with 24/7 on-call rotation
- Breach notification SLA: [≤72 hours / ≤24 hours — specify]
- Customer communication via [email + status page]

**Sub-processors**
- Full sub-processor list available upon request.
- Notification of sub-processor changes: [30 / 60] days advance notice.

**What We Need from IT**
- Preferred security questionnaire format (SIG, CAIQ, or custom) — we will complete within [X] business days.
- Any specific compliance requirements beyond standard review.
- SSO configuration details for pilot/production setup.

---

### 3C. One-Pager: Deal Summary & Talking Points (For Champion's Internal Meetings)

**Title: Executive Talking Points — [Your Product Name] Evaluation**

**Elevator Pitch (30 seconds)**
> "We've been evaluating [Product] to solve [specific pain point]. It reduces [key metric] by [X%], pays for itself within [Y] months, and [Z] similar companies in our space are already using it. The annual cost is ~$80K and we can be live within [implementation timeline]. I'm asking for budget approval and support through procurement so we can close by [target date]."

**Anticipated Questions & Answers**

| Question | Answer |
|----------|--------|
| Why this vendor over alternatives? | [2–3 differentiators: feature superiority, integration fit, pricing, customer success model, time-to-value] |
| Why ~$80K? Is there room to negotiate? | Pricing is competitive for this category. We benchmarked against [Competitor A] at $[X] and [Competitor B] at $[Y]. This is the best value for our requirements. |
| What's the implementation effort? | [X] weeks, [Y] hours of internal team time. Vendor provides dedicated onboarding support included in the contract. |
| What happens if it doesn't work? | [Cancellation terms, pilot period, SLA guarantees, or money-back provisions if applicable.] |
| Is it secure? | IT is conducting a full security review. Vendor holds SOC 2 Type II and supports SSO, encryption, and RBAC. No red flags identified so far. |
| What's the urgency? | [Business trigger]. Every month of delay costs us approximately $[X] in [lost productivity / revenue / compliance risk]. |

**Champion's Internal Action Items**

1. Share business case one-pager with Finance contact by [date].
2. Introduce seller's SE to IT security lead for questionnaire hand-off by [date].
3. Schedule 30-minute alignment call with Finance + Ops + IT by end of Week 1.
4. Confirm decision-making process: who has final signature authority and is there a review board or committee?
5. Flag any competing priorities or budget freezes that could delay approval.

---

## 4. Deal Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Security review takes longer than 2 weeks | Medium | High — delays everything downstream | Submit questionnaire + SOC 2 in Week 1; set 24-hr SLA on follow-ups |
| Procurement onboarding backlog | Medium | Medium — delays PO issuance | Submit vendor registration in Week 1; get champion to flag as priority internally |
| Finance pushes budget to next quarter | Low | High — deal slips 3+ months | Anchor business case to time-sensitive trigger; quantify cost of delay |
| Legal redlines extend negotiation | Low | Medium — adds 1–2 weeks | Use buyer's paper if possible; pre-clear key terms with seller legal |
| Champion loses internal momentum | Medium | High — deal stalls | Weekly check-ins; provide fresh content (case studies, ROI updates) to keep narrative alive |
| IT requests on-site assessment or additional audit | Low | High — adds 3–4 weeks | Proactively offer architecture review call; provide pen test + SOC 2 early |
| Competing project absorbs budget | Low | High — deal killed | Map to strategic initiative; get executive sponsor alignment early |

---

## 5. Communication Cadence

| Meeting | Frequency | Attendees | Purpose |
|---------|-----------|-----------|---------|
| Champion sync | Weekly (30 min) | Seller AE + Ops Champion | Pipeline status, blocker removal, internal coaching |
| Technical review | As needed | Seller SE + IT | Security Q&A, architecture review, integration planning |
| Finance alignment | Bi-weekly or as needed | Seller AE + Finance (Econ Buyer) | Budget confirmation, commercial terms, ROI validation |
| Internal deal review | Weekly | Seller AE + Sales Manager | Forecast accuracy, risk assessment, resource requests |
| Executive sponsor touchpoint | As needed (escalation) | Seller VP + Buyer VP/C-level | Unblock stalled items, reinforce strategic value |

---

## 6. Key Contacts & Roles

| Role | Name | Title | Email | Phone | Notes |
|------|------|-------|-------|-------|-------|
| Champion (Ops) | [TBD] | [Title] | | | Primary internal advocate; drives day-to-day evaluation |
| Economic Buyer (Finance) | [TBD] | [Title] | | | Budget authority; needs ROI justification |
| Security Reviewer (IT) | [TBD] | [Title] | | | Owns security questionnaire and technical approval |
| Procurement Contact | [TBD] | [Title] | | | Manages vendor onboarding and PO issuance |
| Legal (if applicable) | [TBD] | [Title] | | | Contract redlines and DPA review |
| Executive Sponsor (Buyer) | [TBD] | [Title] | | | Escalation path; strategic alignment |
| Account Executive (Seller) | [TBD] | [Title] | | | Deal owner; commercial terms |
| Solutions Engineer (Seller) | [TBD] | [Title] | | | Technical demo, security Q&A, architecture review |
| Executive Sponsor (Seller) | [TBD] | [Title] | | | Escalation counterpart; exec-to-exec alignment |

---

*This deal execution pack should be treated as a living document. Update the mutual action plan and trackers at least weekly. Share relevant sections with buyer stakeholders to maintain transparency and shared accountability.*
