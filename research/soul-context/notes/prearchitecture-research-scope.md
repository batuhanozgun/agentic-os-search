# SOUL Research — Pre-Architecture Scope Boundary

**Status:** provisional scope cut; derived from D1–D10 + Phase 1–3 roadmap gates  
**Date:** 2026-08-30

## Question

Which parts of the D1–D10 research-dimension map must be sufficiently understood **before SOUL Phase 1 Definition, Phase 2 Capability Architecture and Phase 3 Failure Model**, and which parts should be deliberately deferred to later architecture/evaluation phases?

This is a scope-control document, not an architecture plan.

## Why this boundary is necessary

The SOUL roadmap is dependency ordered. It intentionally postpones:

- detailed state/memory/context/retrieval architecture,
- runtime orchestration implementation,
- evidence/evaluation architecture,
- authority/policy implementation,
- self-extension architecture,
- observability implementation,
- technology selection

until later phases.

Therefore `important to SOUL` cannot be equated with `must be fully researched now`.

Pre-architecture research should resolve only uncertainties needed to make Phase 1–3 decisions without importing KEEL mechanisms or arbitrary framework assumptions.

# Scope cut by dimension

## D1 — Intended outcome → bounded work definition

### Must know before Phase 1–3

- material failure classes in goal/request interpretation;
- distinctions between missing fact, assumption, constraint, preference/value and approval/authority boundary;
- evidence that `request ≠ true objective/method` is a real recurring failure surface, not only one KEEL anecdote;
- minimum properties a bounded work definition must expose so Phase 1 can define SOUL's input/lifecycle/completion boundary.

### Can defer

- final dialogue/clarification algorithm;
- prompt format or schema implementation;
- UI for elicitation;
- domain-specific requirements methods.

### Pre-architecture stop condition

Enough when Phase 1 can define the goal/work boundary and human-vs-system information responsibility with known major failure classes and no mechanism lock-in.

---

## D2 — Task-specific system formation and capability derivation

### Must know before Phase 1–3

- a defensible abstraction of `capability` versus role/tool/workflow/mechanism;
- principles for deriving necessary functions/capabilities from outcome + failure/control obligations;
- evidence for when motivation/authority separation can matter and the burden of proof for adding permanent functions/roles;
- cross-domain capability coverage tests sufficient to challenge software-development leakage.

### Can defer

- exact capability registry schema;
- capability implementation/admission engine;
- model/tool/provider selection;
- detailed generated-role format.

### Pre-architecture stop condition

Enough when Phase 2 can enumerate capabilities by function/property without using KEEL folders or a chosen framework as the taxonomy.

---

## D3 — Internal/external state, memory, context, knowledge and retrieval

### Must know before Phase 1–3

- conceptual distinctions among authoritative internal state, memory/history, actor context, knowledge/evidence and externally observed world state;
- material failure classes: duplication/drift, stale state, omission, unknown-needed context, freshness/validity loss, derived-view authority leakage;
- cold-start and changing-world requirements that imply later capabilities/controls;
- what must be observable in Phase-3 failure signals.

### Can defer

- database/repository/vector-store choices;
- retrieval ranking/embedding algorithms;
- compression implementation;
- exact context-window budgeting;
- detailed Phase-5 storage/retrieval architecture.

### Pre-architecture stop condition

Enough when Phase 2 can derive information/context capabilities and Phase 3 can name the main failure/control properties without committing to a storage or retrieval mechanism.

---

## D4 — Authority, bounded agency and human governance

### Must know before Phase 1–3

- owner-value/judgement/approval decisions versus researchable/technical/system decisions;
- common authority-leak/self-extension/circular-acceptance failure classes;
- properties of protected control state and least privilege relevant to capability/failure mapping;
- evidence that adding more roles is not automatically stronger separation.

### Can defer

- full policy language;
- permissions engine/ACL implementation;
- exact escalation UI;
- Phase-8 authority-rule encoding.

### Pre-architecture stop condition

Enough when Phase 1 can state human-governance boundaries and Phase 2–3 can allocate required authority/control capabilities and failure ownership without inventing a concrete enforcement technology.

---

## D5 — Evidence, provenance, verification and completion

### Must know before Phase 1–3

- claim/evidence classes relevant to material work;
- producer self-certification and correlated-agreement failure classes;
- deterministic versus semantic/evaluative verification distinction;
- exact-target/freshness/provenance properties;
- legitimate uncertainty/non-verification states;
- what `completion` must mean at the abstract system level.

### Can defer

- concrete evaluator architecture;
- benchmark suite and grading implementation;
- provenance storage engine;
- model-diversity/vendor strategy;
- detailed Phase-7 verification orchestration.

### Pre-architecture stop condition

Enough when Phase 1 can define completion and Phase 2–3 can derive evidence/verification capabilities plus their main failure/control obligations.

---

## D6 — Failure representation, containment, recovery and liveness

### Must know before Phase 1–3

This is **directly Phase-3 critical**.

Need:

- a domain-neutral failure taxonomy at the right abstraction level;
- observable signals and uncertainty states;
- prevention/detection/containment/recovery/regression categories;
- root-cause versus proximate-failure distinction;
- liveness/deadlock/starvation/meta-work failure classes;
- conditions that distinguish repair from reframe/research/redesign/non-completion.

### Can defer

- detailed recovery engine;
- domain-specific incident playbooks;
- exact retry/backoff policies;
- runtime implementation of recovery state machines.

### Pre-architecture stop condition

Enough only when every material Phase-2 capability has failure/control ownership and the taxonomy survives materially different scenario families without collapsing into software bug categories.

---

## D7 — Learning, controlled evolution and capability admission

### Must know before Phase 1–3

- why lesson-as-prose / lesson-not-invoked is a material failure class;
- difference between local correction, class-level control, architecture evolution and foundation reopening;
- core property that self-modification/admission cannot self-certify or rewrite its own judging rules;
- failure/control obligations created by missing capability and future evolution.

### Can defer

- exact build/test/verify/admit pipeline;
- capability registry implementation;
- automated policy synthesis;
- Phase-9 self-extension mechanism;
- concrete rollback orchestration.

### Pre-architecture stop condition

Enough when Phase 2–3 can reserve the required evolution/admission capabilities and failure boundaries without defining the final self-extension architecture.

---

## D8 — Observability and reconstructability

### Must know before Phase 1–3

- what material facts/actions/decisions/evidence/authority/failures must be externally observable for correctness and diagnosis;
- difference between authoritative state and derived operational views;
- observability failure classes relevant to Phase-3 detection;
- minimum reconstructability needed for fresh-session and independent review.

### Can defer

- logging stack;
- event-sourcing implementation;
- dashboard/cockpit design;
- telemetry retention/aggregation technology;
- detailed Phase-10 operational model.

### Pre-architecture stop condition

Enough when Phase 2 can derive observability capabilities and Phase 3 can attach detectable signals to material failures, without choosing telemetry technology.

---

## D9 — Generality, domain transfer and task-specific architecture

### Must know before Phase 1–3

This is **directly Phase-2 gate critical**.

Need:

- materially different target scenario families;
- criteria for detecting domain leakage into core;
- method for testing capability and failure coverage across scenarios;
- distinction between invariant property and task-specific operating structure;
- negative cases capable of falsifying a claimed universal abstraction.

### Can defer

- full production pilots;
- v1 implementation benchmarking;
- long-running domain transfer evaluation;
- optimization for every supported domain.

### Pre-architecture stop condition

Enough when the Phase-2 capability map can be attacked by materially different scenarios and no capability is classified core merely because software-development history made it familiar.

---

## D10 — Work selection, decomposition, orchestration and lifecycle

### Must know before Phase 1–3

- distinction between result integration, next-work selection, design and implementation;
- failure classes from premature repair routing, execution/completion bias, lost purpose across handoff and unbounded investigation;
- principles for risk-proportional reasoning/work depth;
- abstract lifecycle properties needed for Phase 1 and function/capability derivation in Phase 2;
- external-state invalidation/replanning as a general work-lifecycle requirement, not only static backlog sequencing.

### Can defer

- permanent Planner role decision;
- exact routing state machine;
- orchestration framework;
- queue/scheduler implementation;
- detailed Phase-6 runtime topology.

### Pre-architecture stop condition

Enough when Phase 1 can define lifecycle/completion states and Phase 2–3 can derive orchestration/work-selection functions plus failure obligations **without presupposing a specific planner/agent topology**.

# Priority classes for SOUL Research before Phase 1–3

## P0 — gate-critical; must be materially developed before architecture

- D1 — goal/work definition boundary
- D2 — capability abstraction/derivation
- D6 — failure taxonomy/control ownership
- D9 — cross-domain/generalisation challenge
- D10 — lifecycle/work-selection properties

These directly determine whether Phase 1–3 can be framed without KEEL leakage.

## P1 — cross-cutting control properties; minimum model required now

- D3 — information/state/context/world-state distinctions
- D4 — authority/human boundary
- D5 — evidence/verification/completion semantics
- D7 — evolution/admission boundary
- D8 — observability/reconstructability

These need enough research to derive capabilities/failures, but detailed architecture belongs later.

This priority split is not a statement that P1 is less important to the final system. It is a **dependency/scope judgement** about what must be resolved before Phase 1–3.

# Global pre-architecture research stop gate

The programme should not wait for exhaustive literature coverage of D1–D10.

A defensible transition toward Phase 1–3 would require at least:

1. **Question coverage:** every P0 dimension has explicit decision-critical questions, evidence, counter-evidence and bounded remaining uncertainty.
2. **Capability abstraction:** Phase 2 can be organised by functions/properties, not current tools, frameworks or KEEL folders.
3. **Failure coverage:** a cross-domain failure taxonomy can map every candidate capability to observable failure/control obligations.
4. **Domain holdout:** materially different scenario families attack capability/failure coverage and reveal no unresolved high-impact domain leakage.
5. **Authority/evidence minimums:** P1 dimensions are sufficiently defined that Phase 2–3 do not silently invent human boundaries, evidence semantics, state concepts or observability requirements.
6. **No unresolved frame blocker:** no known material counter-evidence suggests the research question map itself is missing a higher-level problem class.
7. **Residual uncertainty ledger:** deferred questions are explicitly assigned to later phases/methods rather than disappearing.
8. **Research-promotion boundary preserved:** the research output remains evidence/question/failure/capability input; architecture commitments still require the SOUL decision path.

# What should explicitly NOT block Phase 1–3

The following should not be required merely to feel `well researched`:

- choosing an agent framework or LLM provider;
- designing the final memory/retrieval database;
- deciding every role name/topology;
- proving final runtime performance;
- building the final verification/evaluation system;
- exhaustive coverage of every industry/domain;
- resolving every lower-risk implementation trade-off;
- proving generality from completed production pilots before architecture exists.

# Main uncertainty after this scope cut

The P0/P1 split is derived from the current roadmap and failure evidence, not yet independently validated.

The next adversarial task is to test whether a P1 dimension contains a hidden **Phase-1/2 framing dependency** that would make deferral dangerous, or whether a P0 dimension has been over-promoted because predecessor history makes it salient.

That check should be run against the external holdout families and explicit roadmap gate language, not by preference.