# Platform Strategy Pack: Internal ML Platform

---

## 1) Platform Product Charter

**Platform name:** ML Platform (internal)

**Platform type:** Internal

**Platform owner:** Platform Engineering team (2 engineers)

**Primary users:**
- **ML Engineers** (~25 of the 40 engineers): Build, train, validate, and deploy ML models. Need a fast, reliable path from experiment to production.
- **Application/Backend Engineers** (~10): Consume model predictions via APIs or batch pipelines. Need stable, versioned inference endpoints with predictable latency and clear data contracts.
- **Data/Analytics Engineers** (~5): Prepare features, manage training datasets, and monitor data quality. Need safe, auditable access to PII-bearing data and reproducible feature pipelines.

**Top jobs-to-be-done:**
1. **Ship a model to production reliably** -- go from validated notebook/experiment to a production inference endpoint without manual infra work, config drift, or multi-day back-and-forth with platform engineers.
2. **Roll back or update a model safely** -- canary, shadow, or blue-green deploy a new model version with automatic health checks, and revert in minutes if quality degrades.
3. **Access training/inference data without compliance anxiety** -- use PII-bearing datasets through governed, auditable pipelines so engineers never touch raw PII directly.
4. **Monitor model health in production** -- detect data drift, latency degradation, and prediction-quality drops with dashboards and alerts, not ad hoc scripts.
5. **Reproduce any past experiment or deployment** -- trace from a production model back to its training data, code, hyperparameters, and evaluation metrics.

**User promise (1 sentence):**
"Any ML engineer can take a validated model from experiment to monitored production in under 2 hours, with full auditability and zero direct PII exposure."

**Non-goals:**
1. **Not a training-infrastructure platform.** We do not manage GPU clusters, distributed training frameworks, or hyperparameter search infrastructure. Teams choose their own training tooling; we start at the "model artifact" boundary.
2. **Not a data warehouse or feature store product.** We provide governed access to features and datasets for ML workflows, but the canonical data warehouse, ETL orchestration, and BI layer are owned by the Data Engineering team.
3. **Not an experiment-management tool.** We integrate with experiment trackers (MLflow, W&B, etc.) but do not replace them.
4. **Not a general-purpose CI/CD platform.** We provide ML-specific deployment pipelines. General application CI/CD remains with the DevOps/SRE team.
5. **Not responsible for model correctness.** ML engineers own model quality, evaluation, and bias testing. The platform provides the hooks (eval gates, monitoring) but not the judgment.

**Why now:**
- Model deployment cycle time is ~2 weeks, creating a bottleneck that delays feature launches and A/B tests.
- Two recent SOC2 audit findings flagged inconsistent PII access patterns across ML workflows.
- Platform engineers spend >60% of time on ad hoc deployment requests instead of building reusable infrastructure.
- The team is growing (40 engineers) and ad hoc processes do not scale; each new ML engineer currently requires ~1 week of onboarding to learn deployment tribal knowledge.

**Constraints:**
- **Security/privacy/compliance:** PII present in training and inference data. SOC2 Type II compliance required. All data access must be logged and auditable. Encryption at rest and in transit mandatory.
- **Reliability/SLOs:** Production inference endpoints must maintain p99 latency < 200ms and 99.9% uptime. Deployment rollback must complete within 5 minutes.
- **Budget/resourcing:** 2 platform engineers (no near-term headcount increase). Must leverage managed services and open-source tooling to stay within capacity.
- **Timeline/deadline:** Next SOC2 audit in ~6 months. Core paved-road capabilities must be in place before audit.

**Assumptions (explicit):**
1. ML engineers are willing to adopt a standardized model packaging format (e.g., containerized model artifacts with a standard interface) in exchange for automated deployment.
2. Existing experiment tracking tools (MLflow/W&B) will remain; the platform integrates rather than replaces.
3. The Data Engineering team will expose governed feature/data endpoints that the ML platform can consume; we do not need to build a feature store from scratch.
4. Leadership supports allocating 1-2 sprints of ML engineer time for migration/adoption of the paved road.
5. Managed Kubernetes (or equivalent) is available or will be provisioned by the infrastructure team.

**Success metrics:**

- **Outcome metrics:**
  - **Model deployment cycle time:** from ~2 weeks to < 2 hours (north star)
  - **Deployment failure rate:** from estimated ~20% to < 5% (failed deploys requiring manual intervention)
  - **SOC2 audit findings related to ML data access:** zero new findings
  - **Time-to-rollback:** from ~1 hour (manual) to < 5 minutes (automated)

- **Input/leading metrics:**
  - Paved-road adoption rate (% of new model deployments using the platform pipeline)
  - Platform NPS / developer satisfaction score (quarterly survey)
  - Mean time from model artifact registration to production endpoint live
  - Number of ad hoc deployment requests to platform engineers (target: trending to zero)
  - Audit log coverage (% of PII data accesses with complete audit trail)
  - Documentation coverage (% of platform capabilities with up-to-date docs)

---

## 2) Platform Surface & Interface Map

### 2a) Surface inventory

| Capability | Owner | Consumer(s) | Interface | Paved road? | SLA/SLO | Status | Notes |
|---|---|---|---|---|---|---|---|
| **Model Registry** | Platform team | ML Engineers, App Engineers | CLI + REST API | Y | 99.9% availability | To build (Now) | Stores versioned model artifacts with metadata, lineage |
| **Deployment Pipeline** | Platform team | ML Engineers | CLI (`ml deploy`) + GitOps config | Y | Deploys complete < 15 min; rollback < 5 min | To build (Now) | Canary/blue-green with automated health checks |
| **Inference Serving** | Platform team | App Engineers, ML Engineers | REST/gRPC endpoints (auto-provisioned) | Y | p99 < 200ms, 99.9% uptime | To build (Now) | Autoscaling, A/B traffic splitting |
| **PII-Safe Data Access Layer** | Platform team + Data Eng | ML Engineers, Data Engineers | Python SDK + SQL proxy | Y | Audit log completeness: 100% | To build (Now) | Tokenization, access logging, role-based access |
| **Model Monitoring & Alerting** | Platform team | ML Engineers | Dashboard (Grafana) + alert config (YAML) | Y | Alerts fire < 5 min of threshold breach | To build (Next) | Data drift, prediction quality, latency |
| **Experiment Integration** | Platform team | ML Engineers | SDK hooks for MLflow/W&B | N (optional) | Best-effort | To build (Next) | Link experiment runs to registry entries |
| **Feature Access SDK** | Data Eng (platform integrates) | ML Engineers | Python SDK | N (optional) | Depends on Data Eng SLO | Planned (Next) | Governed read access to feature store |
| **CI/CD Hooks (model testing)** | Platform team | ML Engineers | GitHub Actions / CI config templates | Y | Tests run < 10 min | To build (Now) | Pre-deploy eval gates, data validation |

### 2b) Boundary contract

- **Platform owns (defaults):**
  - Model artifact packaging standard (container format, interface spec)
  - Deployment pipeline (build, test, canary, promote, rollback)
  - Inference infrastructure (serving runtime, autoscaling, load balancing)
  - PII data access governance (tokenization, audit logging, access control)
  - Monitoring infrastructure (metrics collection, dashboards, alerting framework)
  - Authentication and authorization for platform services (SSO integration, service accounts)
  - Logging and observability pipeline for ML services

- **Domain teams (ML engineers) own:**
  - Model code, training logic, and evaluation criteria
  - Feature engineering and selection
  - Defining monitoring thresholds (what constitutes drift or quality degradation for their model)
  - Writing model-specific tests and eval suites
  - Choosing experiment tracking tools and training infrastructure
  - Business logic around model predictions (post-processing, fallbacks)

- **Shared responsibilities:**
  - Incident response for production model failures (platform triages infra; ML engineer triages model quality)
  - Capacity planning (ML engineers forecast load; platform provisions infrastructure)
  - Security reviews for new model types or data sources (joint with Security team)

### 2c) Default decisions ("paved road")

- **AuthN/AuthZ:** All platform services use corporate SSO (OIDC). Service-to-service auth via mTLS with short-lived certificates. Role-based access control: `ml-engineer`, `ml-viewer`, `platform-admin`. No custom auth implementations.
- **Logging/Observability:** Structured JSON logs to centralized logging (ELK/Datadog). All inference requests logged with request ID, model version, latency, and prediction metadata (no raw PII in logs). Distributed tracing enabled by default.
- **Deployment/Release:** GitOps-based deployment. Merge to `main` triggers build; promote to staging via CLI; promote to production with automated canary (5% -> 25% -> 100% over 30 minutes with automatic rollback on error-rate spike). No SSH-to-prod, no manual kubectl.
- **Data Access:** All PII access goes through the PII-Safe Data Access Layer. Raw PII is never exposed directly. Tokenized datasets are the default for training. De-tokenization requires explicit approval and audit log entry. Data retention policies enforced automatically.
- **Guardrails (AI/ML-specific):** Pre-deploy eval gate required (model must pass a defined test suite before promotion). Model cards are required metadata in the registry. Prediction monitoring is auto-enabled for all production models.

---

## 3) Lifecycle Stage & Open/Close Strategy

### 3a) Stage diagnosis

| Stage | Evidence | What we should do now | What to avoid |
|---|---|---|---|
| **Step 0 -- Conditions met** (current stage) | - Clear demand: 40 engineers blocked by 2-week deploy cycles. - SOC2 pressure creates urgency for governed data access. - Two platform engineers exist as a seed team. - No existing "platform product" -- today it is ad hoc scripts and tribal knowledge. - No external consumers; purely internal. | - Build the core paved road (registry, pipeline, serving, data access). - Treat it as a product: define users, measure adoption, run feedback loops. - Prove value with 2-3 pilot teams before mandating adoption. - Establish governance for PII access before SOC2 audit. | - Premature "platform thinking" (marketplace, extensions, partner APIs). - Building for hypothetical future scale instead of current pain. - Trying to boil the ocean: pick the narrowest valuable path first. |

**Stage justification:** This is clearly Step 0 (conditions met for an internal platform). The evidence is:
1. There is genuine demand (40 engineers, 2-week cycle times, SOC2 findings).
2. There is no existing platform product, only ad hoc processes.
3. The platform is internal-only with no ecosystem or external consumers.
4. The team is small (2 engineers), meaning we must prove value before expanding scope.

There is no moat to build (Step 1) or ecosystem to open (Step 2) -- this is about internal developer productivity and compliance.

### 3b) Open/close decisions (this quarter)

- **Decision 1: Standardize model packaging format**
  - Options: (a) Enforce a single container-based format from day one; (b) Support 2-3 formats and converge later; (c) Accept anything and normalize at deploy time.
  - Recommendation: Option (a) -- single container-based format with a standard prediction interface.
  - Rationale: With 2 platform engineers, supporting multiple formats is unsustainable. A single format simplifies the pipeline, reduces bugs, and creates a clear contract. Migration cost is acceptable if we provide a scaffold tool.
  - Risks/mitigations: Some teams have non-containerized models (pickle files, custom servers). Mitigation: provide a `ml package` CLI tool that wraps existing artifacts into the standard format. Allow a 2-month grace period for migration.

- **Decision 2: PII data access governance model**
  - Options: (a) Platform-managed tokenization layer (all PII access goes through SDK); (b) Policy-only approach (document rules, rely on team compliance); (c) Hybrid (SDK for new workflows, policy for legacy).
  - Recommendation: Option (a) -- platform-managed tokenization layer.
  - Rationale: SOC2 audit is in 6 months. Policy-only approaches have already produced audit findings. A technical control is more reliable and auditable than process controls alone.
  - Risks/mitigations: Building a tokenization layer is non-trivial for 2 engineers. Mitigation: use an existing open-source or managed solution (e.g., Google DLP API, HashiCorp Vault transform secrets engine) rather than building from scratch. Start with the 3 most common data access patterns.

- **Decision 3: Mandate vs opt-in adoption**
  - Options: (a) Mandate all new deployments use the platform by month 3; (b) Opt-in with strong incentives; (c) Opt-in with a hard mandate deadline at month 6.
  - Recommendation: Option (c) -- opt-in with incentives for 3 months, then mandate for new deployments at month 6 (aligned with SOC2 audit).
  - Rationale: Early opt-in lets us iterate on the paved road with willing teams. A mandate deadline creates urgency and aligns with the SOC2 compliance requirement.
  - Risks/mitigations: Risk of low early adoption leaving the platform untested. Mitigation: recruit 2-3 champion teams to pilot in month 1; use their feedback to improve before wider rollout.

---

## 4) Moat & Ecosystem Model

### 4a) Participants + incentives

| Participant | What they want | What they contribute | Incentive we provide | Friction today |
|---|---|---|---|---|
| **ML Engineers** | Ship models fast, focus on ML not infra | Model artifacts, eval suites, adoption/feedback | Automated deployment, zero-toil deploys, self-service | 2-week deploy cycle, manual processes, config drift |
| **App/Backend Engineers** | Stable, versioned prediction endpoints | Load/usage data, integration feedback | Auto-provisioned endpoints with SLAs, versioned APIs | Fragile hand-rolled integrations, no versioning |
| **Data Engineers** | Clear data consumption patterns, fewer ad hoc requests | Governed feature endpoints, data pipeline maintenance | Reduced ad hoc data requests via self-service SDK | Constant "can you give me access to X" requests |
| **Platform Engineers** | Leverage (build once, serve many), reduced toil | Platform capabilities, paved roads, governance | Shift from ad hoc firefighting to product building | >60% time on ad hoc requests |
| **Security/Compliance** | Auditable, compliant data access; zero PII incidents | Audit requirements, security reviews, policy input | Automatic audit trails, enforced access controls | Manual audit evidence gathering, inconsistent controls |
| **Engineering Leadership** | Faster time-to-market, SOC2 compliance, team productivity | Budget, staffing decisions, mandate authority | Measurable productivity gains, clean audit results | Unclear ROI of platform investment |

### 4b) Compounding loop

**Loop A (Internal Productivity Flywheel):**

More models deployed via paved road --> More deployment patterns/edge cases captured --> Better pipeline reliability and tooling --> Lower friction for next deployment --> More engineers adopt the paved road --> More models deployed via paved road

**Leading indicators (measurable):**
- Weekly count of paved-road deployments (target: increasing week-over-week)
- Ratio of paved-road to ad hoc deployments (target: >80% by month 4)
- Mean deployment time via paved road (target: decreasing as tooling improves)
- Platform engineer time on ad hoc requests (target: <20% by month 4)

**Loop B (Data Governance Flywheel):**

More PII access through governed SDK --> More comprehensive audit logs --> Easier SOC2 evidence collection --> Stronger compliance posture --> More confidence to work with sensitive data --> More ML use cases enabled --> More PII access through governed SDK

**Leading indicators:**
- % of PII data accesses via governed SDK (target: 100% by month 6)
- Time to produce SOC2 audit evidence for ML data access (target: <1 hour, down from days)

### 4c) Seeding plan + investment gates

- **Seed actions:**
  1. Recruit 2-3 champion ML teams (ideally teams with upcoming model launches) for month-1 pilot.
  2. Build the `ml deploy` CLI with the simplest happy path (single model, single endpoint, no canary) in sprint 1-2.
  3. Create a "migration cookbook" with step-by-step guides for the 3 most common model types.
  4. Run a weekly "platform office hours" (30 min) to collect feedback and unblock adopters.
  5. Publish a "paved road vs ad hoc" comparison dashboard showing deploy time, failure rate, and audit coverage.

- **Investment gates (signals that justify more spend):**
  - Gate 1 (month 2): 3+ teams have completed at least one paved-road deployment. Deployment time < 1 hour for happy path. --> Invest in canary/rollback automation.
  - Gate 2 (month 4): >50% of new deployments use the paved road. Zero SOC2-relevant PII access outside governed SDK. --> Request budget for monitoring/alerting layer and consider part-time PM allocation.
  - Gate 3 (month 6): >80% paved-road adoption. Deployment cycle time < 2 hours. Clean SOC2 audit for ML data access. --> Make the case for a third platform engineer and expand scope to feature access and experiment integration.

---

## 5) Governance & Policy Plan

**What is open now:**
- Model Registry: any ML engineer can register, version, and browse model artifacts.
- Deployment Pipeline: any ML engineer can deploy to staging self-service; production deploys require passing the eval gate.
- Monitoring Dashboards: read access for all engineers; write access (custom dashboards) for model owners.
- Platform documentation and migration guides: open to all.

**What remains closed (and why):**
- Direct PII data access: closed. All access must go through the PII-Safe Data Access Layer. Reason: SOC2 compliance, auditability.
- Infrastructure configuration (Kubernetes manifests, scaling policies, networking): closed to domain teams. Reason: 2-person platform team cannot support arbitrary infra changes; paved-road defaults ensure reliability.
- Production rollback override (skip canary, force-promote): closed to `platform-admin` role only. Reason: safety; automated canary is the default and manual override is emergency-only.

**Access + permissions model:**
| Role | Capabilities |
|---|---|
| `ml-engineer` | Register models, deploy to staging/production (via pipeline), view logs and monitoring, access tokenized PII data, create alerts |
| `ml-viewer` | View model registry, dashboards, and logs (read-only) |
| `platform-admin` | All of the above + modify pipeline config, override rollback, manage access control, modify governance policies |
| `data-access-auditor` | View audit logs for PII data access (Security/Compliance team) |

All roles enforce corporate SSO. Service accounts use mTLS with short-lived certificates and are scoped to specific capabilities.

**Quotas/limits + abuse prevention:**
- Staging environment: each team limited to 5 concurrent model deployments (prevents resource exhaustion).
- Production: deployment frequency limit of 10 per team per day (prevents runaway automation).
- PII data access: rate-limited per user per hour; anomalous access patterns trigger alerts to Security team.
- Model artifact size limit: 10 GB per artifact (prevents registry storage abuse; exceptions require platform-admin approval).

**Support model:**
- Primary channel: `#ml-platform` Slack channel for questions and requests.
- Office hours: weekly 30-minute session for deeper issues and feedback.
- Incident escalation: page platform on-call (PagerDuty rotation between 2 platform engineers) for production inference outages. ML engineers handle model-quality incidents with platform providing monitoring data.
- SLA for platform bugs: P0 (production outage) -- respond within 30 minutes, resolve within 4 hours. P1 (degraded service) -- respond within 2 hours, resolve within 1 business day. P2 (feature request/minor bug) -- triaged within 1 week.

**Docs + examples:**
- Before "general availability" (month 3), the following must exist:
  - Getting Started guide (< 15 min to first staging deploy)
  - Model packaging reference (container format spec, interface contract)
  - PII Data Access guide (SDK usage, what's allowed, how to request access)
  - Deployment pipeline reference (config options, canary behavior, rollback)
  - Troubleshooting guide (top 10 failure modes and fixes)
  - 2 end-to-end example models (one simple, one with PII data access)

**Versioning + deprecation policy:**
- Platform CLI and SDK follow semantic versioning.
- Breaking changes require 4-week notice in `#ml-platform` channel and migration guide.
- Deprecated APIs/interfaces remain functional for at least 2 release cycles (minimum 8 weeks).
- Model serving API contract (input/output schema) is versioned per model; consumers pin to a version.

**Parity rules:**
- Not applicable (internal platform; no first-party vs third-party distinction). All internal teams have equal access to platform capabilities.

**Pricing/packaging:**
- Not applicable (internal platform; costs allocated to the platform team's budget). If cost allocation becomes necessary, charge-back by inference compute usage per team (deferred to Later horizon).

---

## 6) AI System Defensibility

**AI use cases enabled by this platform:**
- **Model serving** (primary): Real-time and batch inference for ML models (recommendations, fraud detection, NLP classification, etc.)
- **Potential future:** ML-assisted code review for model code, automated model selection/tuning (agent workflows). These are Later-horizon explorations, not current scope.

**Context sources:**
- Training datasets (feature store, data warehouse) -- may contain PII
- Model artifacts (weights, configs, hyperparameters) -- no PII
- Experiment metadata (MLflow/W&B) -- no PII
- Production inference logs (request/response metadata) -- PII-tokenized
- Model evaluation results and monitoring data -- no PII

**Context storage/retrieval:**
- Model Registry serves as the single source of truth for model artifacts and metadata.
- Training data accessed exclusively through PII-Safe Data Access Layer (tokenized by default).
- Inference logs stored in centralized logging with PII fields automatically redacted/tokenized.
- Freshness: model registry is real-time; monitoring data has < 5 min lag; audit logs are append-only and immutable.

**Experiences:**
- Currently: single experience surface (deploy + serve + monitor pipeline). All models go through the same paved road.
- Future: if multiple AI experiences emerge (e.g., chat-based model debugging, automated retraining agents), they will share the same context repository (registry + monitoring data + audit logs) and the same governance policies.

**Guardrails:**
- **Least privilege:** ML engineers access only their team's models and data. Cross-team model access requires explicit grant. PII access is tokenized by default; de-tokenization requires approval and audit entry.
- **Audit logs:** All model deployments, data accesses, and configuration changes are logged with user identity, timestamp, and action. Logs are immutable and retained for 2 years (SOC2 requirement).
- **Human approvals:** De-tokenization of PII data. Production deployment override (skip canary). Deletion of model artifacts. Changes to access control policies.
- **Evaluation & monitoring:** Pre-deploy eval gate (model must pass defined test suite). Production monitoring for data drift (statistical tests on input distributions), prediction quality (if ground truth available), latency, and error rates. Alert thresholds set by model owners, enforced by platform. Quarterly review of monitoring coverage.

---

## 7) Metrics & Operating Model

### 7a) Metrics

**North-star outcome metric:**
- **Model deployment cycle time** (time from "model artifact ready" to "serving production traffic"): target < 2 hours, down from ~2 weeks.

**Input metrics (adoption, productivity, reliability):**
| Metric | Current baseline | 3-month target | 6-month target |
|---|---|---|---|
| Paved-road adoption (% of new deployments) | 0% | 50% | >80% |
| Mean deploy time (paved road) | N/A | < 1 hour | < 30 min |
| Deployment failure rate | ~20% (est.) | < 10% | < 5% |
| Time-to-rollback | ~1 hour (manual) | < 10 min | < 5 min |
| Platform engineer time on ad hoc requests | >60% | <40% | <20% |
| Developer satisfaction (quarterly NPS) | Not measured | Baseline established | >30 NPS |

**Guardrail metrics (cost, abuse, privacy):**
| Metric | Threshold | Action if breached |
|---|---|---|
| PII access outside governed SDK | 0 incidents | Immediate investigation; block access path |
| SOC2 audit findings (ML-related) | 0 new findings | Prioritize remediation in next sprint |
| Platform infrastructure cost | < $X/month (TBD based on baseline) | Review resource allocation; optimize autoscaling |
| Unplanned platform outages | < 1 per month | Post-incident review; invest in reliability |

### 7b) Operating model

- **Platform PM/owner:** In the near term, one of the 2 platform engineers serves as de facto PM (owns roadmap, intake, stakeholder communication). By month 4 (investment gate 2), request a part-time PM allocation from Engineering Leadership.
- **Intake + prioritization process:**
  - Feature requests and bug reports via `#ml-platform` Slack channel and a lightweight intake form (GitHub Issues template).
  - Weekly triage (30 min): platform team reviews incoming requests, categorizes as P0/P1/P2, and slots into the current or next sprint.
  - Quarterly roadmap review with Engineering Leadership and ML team leads.
- **Release/versioning cadence:**
  - Platform CLI/SDK: bi-weekly releases (aligned with sprint cadence).
  - Infrastructure changes: continuous delivery with automated testing.
  - Breaking changes: 4-week deprecation notice, aligned with monthly release cycle.
- **Documentation ownership:**
  - Platform team owns all platform docs (Getting Started, API reference, guides).
  - Docs are treated as product surface: every new feature ships with updated docs or the feature is not considered "done."
  - ML engineers contribute model-specific examples and case studies.
- **Support/on-call model:**
  - 2-person PagerDuty rotation (1 week on, 1 week off) for production incidents.
  - `#ml-platform` Slack channel for non-urgent questions (target: response within 4 business hours).
  - Weekly office hours (30 min) for deeper discussion and feedback.
- **Feedback loop:**
  - Quarterly developer satisfaction survey (5 questions, NPS).
  - Sprint retrospectives include platform adoption and feedback review.
  - Adoption metrics dashboard reviewed weekly by platform team.
  - Quarterly roadmap review incorporates aggregated feedback themes.

---

## 8) 12-Month Roadmap

### Now (0-3 months): "Paved Road v1"

**Goal:** Prove the paved road works for the happy path. Address SOC2 urgent gaps.

| Milestone | Description | Owner | Dependencies | Target |
|---|---|---|---|---|
| Model Registry v1 | Versioned artifact store with metadata, lineage, CLI upload/browse | Platform team | Managed object storage provisioned | Month 1 |
| Standard packaging format | Container spec + `ml package` CLI scaffold tool | Platform team | None | Month 1 |
| Deployment Pipeline v1 | GitOps deploy to staging (single command); manual promote to prod | Platform team | Model Registry, Kubernetes access | Month 2 |
| PII-Safe Data Access Layer v1 | Tokenization SDK for top 3 data access patterns; audit logging | Platform team + Data Eng | Data Eng feature endpoints | Month 2 |
| Pilot with 2-3 champion teams | End-to-end deploy of real models through the paved road | Platform team + pilot teams | Pipeline v1, Registry v1 | Month 2-3 |
| Getting Started docs + 2 example models | Documentation sufficient for self-service onboarding | Platform team | Pipeline v1 working | Month 3 |
| Automated canary + rollback | Canary promotion (5% -> 25% -> 100%) with automatic rollback on error spike | Platform team | Pipeline v1 validated by pilots | Month 3 |

### Next (3-6 months): "Production-Grade + SOC2 Ready"

**Goal:** Harden for production. Achieve >80% adoption. Pass SOC2 audit for ML data access.

| Milestone | Description | Owner | Dependencies | Target |
|---|---|---|---|---|
| Model Monitoring v1 | Data drift detection, latency/error dashboards, configurable alerts | Platform team | Inference serving instrumented | Month 4 |
| Pre-deploy eval gates | Automated test suite execution before production promotion; block on failure | Platform team | CI/CD integration | Month 4 |
| PII Data Access 100% coverage | All ML PII access routed through governed SDK; legacy paths blocked | Platform team + Data Eng + Security | SDK v1 validated by pilots | Month 5 |
| SOC2 audit evidence automation | Automated export of audit logs, access reports, policy documentation | Platform team + Security | Audit logging complete | Month 5 |
| Adoption mandate for new deployments | All new model deployments must use paved road (legacy models grandfathered) | Eng Leadership + Platform team | Pipeline reliable, docs complete | Month 6 |
| A/B traffic splitting | Route % of traffic to model variants for online experiments | Platform team | Inference serving v1 stable | Month 6 |

### Later (6-12 months): "Expand + Mature"

**Goal:** Expand platform capabilities. Reduce remaining toil. Build toward full self-service.

| Milestone | Description | Owner | Dependencies | Target |
|---|---|---|---|---|
| Feature Access SDK integration | Governed read access to feature store from ML training/inference code | Platform team + Data Eng | Data Eng feature store mature | Month 7-8 |
| Experiment tracker integration | Link MLflow/W&B experiment runs to registry entries and production deployments | Platform team | Registry v1 stable | Month 8 |
| Self-service monitoring customization | ML engineers define custom drift detectors and alert rules via config | Platform team | Monitoring v1 stable | Month 9 |
| Legacy model migration | Migrate remaining ad hoc deployments to paved road | Platform team + ML teams | All Now/Next features stable | Month 9-10 |
| Cost allocation and visibility | Per-team inference cost dashboards; optional charge-back | Platform team + Finance | Inference serving instrumented | Month 11 |
| Platform capability expansion assessment | Evaluate: batch inference pipeline, automated retraining, model A/B framework | Platform team + Eng Leadership | Adoption >90%, stable operations | Month 12 |

**Dependencies:**
- Data Engineering team must provide governed feature endpoints by month 2 (critical path for PII Data Access Layer).
- Infrastructure team must provision managed Kubernetes access by month 1 (critical path for deployment pipeline).
- Security team must define SOC2 audit evidence requirements by month 1 (shapes audit logging design).
- Engineering Leadership must communicate adoption mandate by month 5 (for month 6 enforcement).

**Resourcing assumptions:**
- 2 platform engineers at 80% capacity on platform work (20% on-call/support/ad hoc).
- Part-time Data Engineering support (0.25 FTE equivalent) for PII Data Access Layer integration.
- Part-time PM allocation requested at investment gate 2 (month 4).
- Third platform engineer requested at investment gate 3 (month 6), if approved, starts contributing at month 8.

**Rollback/exit paths:**
- If pilot teams reject the standard packaging format (month 2): support 1-2 additional formats as a bridge, but keep the standard as the primary path. Do not support more than 3 formats.
- If PII tokenization layer proves too complex for 2 engineers (month 2): fall back to a lighter-weight approach (access logging + policy enforcement without tokenization) for the SOC2 audit, and revisit tokenization in the Next horizon.
- If adoption stalls below 30% at month 4: conduct user research to identify blockers; consider delaying mandate and investing in migration tooling/support.
- If the third engineer is not approved at month 6: reduce Later-horizon scope to maintenance and incremental improvements; defer feature access SDK and experiment integration.

---

## Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| 2-engineer team is too small to deliver Now-horizon on time | Medium | High | Ruthlessly prioritize. Defer monitoring to Next if needed. Use managed services to reduce build scope. |
| ML engineers resist standard packaging format | Medium | Medium | Co-design with champion teams. Provide scaffold tooling. Allow grace period. |
| Data Engineering team cannot provide governed endpoints on time | Medium | High | Start with a minimal data access proxy; build toward full feature store integration. Have a fallback plan for SOC2 (policy + logging without SDK). |
| SOC2 audit timeline accelerates | Low | High | Front-load PII governance work. Have audit evidence templates ready by month 3. |
| Platform becomes a bottleneck (2 engineers, 40 consumers) | Medium | High | Invest in self-service from day one. Automate everything that can be automated. Limit scope to paved-road defaults; say no to custom requests. |
| Champion team attrition (key pilot engineers leave or shift priorities) | Low | Medium | Recruit 3 pilot teams (not 2) to have redundancy. Ensure leadership sponsorship for pilot participation. |

### Open Questions

1. **Training infrastructure boundary:** Should the platform eventually include managed training (GPU scheduling, distributed training)? Or is that permanently out of scope? Decision needed by month 6 to inform Later-horizon planning.
2. **Feature store ownership:** Will Data Engineering build a proper feature store, or should the ML platform team own feature serving? This affects the Later-horizon roadmap significantly.
3. **Multi-model pipelines:** Some teams are building inference pipelines that chain multiple models. Should the platform support DAG-based inference, or is that a domain-team responsibility? Defer decision until adoption data is available (month 6).
4. **Cost allocation model:** If per-team charge-back is implemented, how will shared infrastructure costs (registry, monitoring) be allocated? Finance team input needed.
5. **On-call sustainability:** A 2-person on-call rotation is fragile. What is the plan if one engineer is on vacation or leaves? Escalation path to a broader engineering on-call needed.

### Next Steps

| Action | Owner | Deadline |
|---|---|---|
| Finalize standard model packaging format spec with 2-3 ML engineers | Platform Engineer 1 | Week 2 |
| Secure managed Kubernetes access from Infrastructure team | Platform Engineer 2 | Week 2 |
| Recruit 2-3 champion teams for pilot; get leadership sponsorship | Platform Engineer 1 (de facto PM) | Week 2 |
| Define SOC2 audit evidence requirements with Security team | Platform Engineer 2 + Security | Week 3 |
| Align with Data Engineering on governed feature endpoint timeline | Platform Engineer 1 + Data Eng lead | Week 3 |
| Build Model Registry v1 and `ml package` CLI | Platform Engineers 1 + 2 | Month 1 |
| Present this strategy pack to Engineering Leadership for alignment | Platform Engineer 1 (de facto PM) | Week 3 |
| Schedule weekly platform office hours starting month 1 | Platform Engineer 1 | Week 1 |

---

## Quality Gate: Checklist Verification

### A) Input readiness -- PASS
- [x] Platform type (internal) and owner (platform engineering team) stated.
- [x] Primary users (ML engineers, app engineers, data engineers) and top jobs explicit.
- [x] Current state (ad hoc processes, 2-week cycle time) and biggest pains described with concrete examples.
- [x] Constraints (PII, SOC2, 2 engineers, 6-month audit timeline) captured.
- [x] Decisions on the table named (packaging format, PII governance model, mandate timeline).

### B) Platform-as-product -- PASS
- [x] Platform Product Charter exists with user promise, non-goals, and assumptions.
- [x] PM/owner identified (platform engineer as de facto PM, with plan to request dedicated PM).
- [x] Success metrics include developer productivity metrics (cycle time, deploy frequency, time-to-rollback).

### C) Surface area + boundary -- PASS
- [x] Surface inventory lists capabilities, owners, consumers, and interfaces.
- [x] Paved-road defaults explicitly documented.
- [x] Boundary contract clear (platform vs domain ownership).

### D) Lifecycle + ecosystem -- PASS
- [x] Lifecycle stage chosen (Step 0) and justified with evidence.
- [x] Open/close decisions explicit for this quarter.
- [x] Compounding loops defined as causal chains with measurable leading indicators.
- [x] Seeding plan with investment gates defined.

### E) Governance -- PASS
- [x] What is open now vs later stated.
- [x] Policies for access control, quotas, versioning/deprecation exist.
- [x] Sustainability addressed: docs, support, incident response, compatibility commitments.

### F) AI system (applicable) -- PASS
- [x] Context treated as first-class asset with permissions and audit.
- [x] Guardrails include least privilege, logging, evaluation/monitoring.
- [x] Human-in-the-loop points defined (de-tokenization, deployment override).

### G) Roadmap + decision-readiness -- PASS
- [x] 12-month roadmap uses Now/Next/Later and is consistent with resourcing.
- [x] Dependencies and sequencing explicit.
- [x] Rollback/exit paths included.
- [x] Risks, open questions, and next steps with owners included.

### Rubric Self-Assessment

| Dimension | Score | Rationale |
|---|---|---|
| 1) Clarity of scope and user promise | 5 | Clear users, specific jobs, non-goals, assumptions; user promise is one sentence. |
| 2) Platform-as-product operating model | 4 | Operating model defined with metrics, intake, support. Gap: PM is a platform engineer wearing two hats; not yet a dedicated role. |
| 3) Surface area and boundary design | 5 | Surface map, boundary contract, and paved-road defaults are explicit and comprehensive. |
| 4) Lifecycle stage and strategic coherence | 5 | Stage 0 justified with 4 evidence points; open/close decisions are concrete and near-term. |
| 5) Ecosystem and moat logic | 4 | Internal flywheel loops defined with leading indicators. Moat concept less applicable (internal platform); no external ecosystem. |
| 6) Governance and sustainability | 5 | Access model, quotas, versioning, deprecation, support, and docs plan are all addressed. |
| 7) AI system defensibility | 4 | Context sources, permissions, audit, and guardrails defined. Eval/monitoring plan exists but will mature with the monitoring milestone. |
| 8) Roadmap realism and decision-readiness | 5 | Now/Next/Later with dependencies, resourcing, rollback paths, and clear next actions with owners and deadlines. |

**Overall score: 37/40** -- Strategy pack is decision-ready. Primary gap is dedicated PM ownership (addressed in investment gate 2).
