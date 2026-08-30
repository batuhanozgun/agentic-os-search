# SOUL Research Dimension Map — Stage 1 foundation extraction

**Status:** active; foundation-derived dimensions, not architecture  
**Date:** 2026-08-30

## Purpose

Translate SOUL's accepted/current foundation and Phase-1..3 roadmap gates into **research dimensions and evidence obligations** without converting them into mechanisms, roles, tools, services or a product backlog.

This stage deliberately distinguishes:

- **Foundation constraint / owner-defined property:** currently authoritative; research does not vote on whether SOUL should have it.
- **Researchable system question:** evidence can inform how the property can be satisfied, what failure classes threaten it, what capabilities are necessary, and which alternative layers/control patterns are credible.
- **Empirical/generalisation claim:** requires scenario, experiment, comparative or field evidence rather than prose alone.

## Source basis

Primary SOUL sources:

- `development/00_foundation/VISION.md`
- `development/00_foundation/DEFINITION.md`
- `development/00_foundation/SUCCESS_CRITERIA.md`
- `development/00_foundation/NON_NEGOTIABLES.md`
- `development/03_plan/ROADMAP.md`

Boundary control:

- `ROLE_MODEL.md`
- `EVIDENCE_TEMPLATE.md`
- `DECISION_POLICY.md`
- `REASONING_POLICY.md`

## Foundation-level fixed properties — do not turn into popularity questions

The following are current architectural constraints or success properties, not open questions such as `is this a good idea?`:

- critical project truth must outlive chat/model memory;
- producer self-certification is insufficient for material work;
- evidence cannot be replaced by plausible narrative;
- authority must be explicit and bounded;
- state, memory, context and knowledge are distinct concepts;
- humans are not fallback search engines or hidden orchestrators;
- fresh-session continuation is required;
- missing capability must be explicit and governed;
- critical control state cannot be solely controlled by the constrained component;
- unknown/unverified/blocked/partial/stale/conflicted/failed must be representable;
- repeated preventable/detectable failures should migrate toward stronger controls when practicable;
- one material fact should have one authoritative home;
- domain assumptions must not silently leak into stable core;
- core evolution is governed;
- observability is part of correctness;
- general-purpose SOUL must demonstrate transfer across materially different pilots.

Research may discover that a foundation constraint is internally inconsistent or impossible under another constraint. That would be **counter-evidence requiring a foundation decision path**, not permission for research to silently rewrite the foundation.

# Candidate research dimensions

## D1 — Intended outcome → bounded work definition

### Foundation demand

SOUL receives an intended outcome and must distinguish factual gaps from human preferences/values/constraints/approval boundaries. Success requires an explicit bounded work definition with assumptions, unknowns, constraints, acceptance criteria and human decision boundaries.

### Researchable questions

- What recurring failure classes occur when agents translate ambiguous or underspecified human outcomes into work definitions?
- How can factual uncertainty, preference/value ambiguity, hard constraints, soft preferences and authority/approval boundaries be distinguished reliably?
- When should a system ask, infer, research, defer, or refuse to proceed?
- How can the system detect that the user's apparent request is a proposed method rather than the actual outcome?
- What evidence shows that clarification/framing improved outcome fidelity rather than merely adding questions?

### Evidence classes

- human–AI requirements/intent elicitation literature and standards;
- historical agent failures where request→task translation drifted;
- comparative task cases with hidden/ambiguous premises;
- adversarial prompts where method is mistaken for objective;
- owner-relevant acceptance tests across materially different domains.

### Strong falsifiers / counter-frames

- a lighter direct-execution baseline performs equally or better on outcome fidelity for the same task class;
- clarification protocol increases owner burden without reducing material framing errors;
- a proposed universal intent schema fails on a materially different domain or value-laden task.

### Downstream decision dimensions

Phase 1 purpose/boundary/completion semantics; later goal/work-definition domain model.

---

## D2 — Task-specific system formation and capability derivation

### Foundation demand

SOUL is not a fixed team/workflow. It must determine which capabilities, roles, tools, knowledge sources, controls and verification a task requires, including missing capabilities.

### Researchable questions

- What is a **capability** at the right abstraction level for a general-purpose agentic system?
- How can capability necessity be derived from outcome/failure/control obligations rather than copied from existing frameworks?
- When is an existing capability sufficient, when must it be adapted, and when is a genuinely missing capability present?
- What failure modes arise from over-decomposition, under-decomposition, duplicated capability ownership or hidden capability improvisation?
- Which functions require distinct success motivations/authority boundaries and which can safely remain combined?

### Evidence classes

- cross-domain task/capability decomposition cases;
- systems-engineering/function-allocation prior art;
- agent-framework/multi-agent prior art used as comparative evidence, not schema;
- ablation/comparator evidence when claiming a durable role/component is necessary;
- historical KEEL/Development-OS evidence of role/motivation failure.

### Strong falsifiers / counter-frames

- the same property is achieved with a materially simpler capability structure;
- proposed capability categories collapse or overlap across domains;
- a durable role/control is justified only by bundled-treatment improvement without component-level identification.

### Downstream decision dimensions

Phase 2 Capability Architecture; Phase 9 self-extension lifecycle.

---

## D3 — Persistent state, memory, context, knowledge and retrieval

### Foundation demand

Critical state outlives model memory; state/memory/context/knowledge are different; fresh sessions continue correctly; agents receive sufficient current context without treating all history as equally relevant/authoritative.

### Researchable questions

- What information classes have different authority, lifetime, freshness, trust and retrieval semantics?
- Which information must be always-present, selectively retrieved, reconstructable, or purely forensic?
- How can selective context reduce attention load without hiding evidence the actor does not know it needs?
- How are omission, stale retrieval, conflicting sources, derived summaries and unknown triggers detected?
- What minimum persistent state is sufficient for cold-start continuation?

### Evidence classes

- context engineering / memory / information-retrieval literature;
- cold-start reconstruction tests;
- omission/adversarial retrieval tests;
- stale/conflict scenarios;
- comparative context-budget experiments with outcome/error measures, not token reduction alone.

### Strong falsifiers / counter-frames

- lower context load correlates with missed material evidence;
- a retrieval trigger depends on evidence omitted from the actor's current context;
- a derived summary becomes de facto authority and drifts from source truth;
- fresh session cannot reconstruct next responsibility without chat replay.

### Downstream decision dimensions

Phase 4 domain model; Phase 5 state/memory/context/knowledge/retrieval architecture.

---

## D4 — Authority, bounded agency and human governance

### Foundation demand

Agents/tools/capabilities cannot silently widen authority. Human owner supplies genuine values, judgement, authority and approvals, not technical/search work the system can derive.

### Researchable questions

- Which decisions are normative/value choices versus researchable/technical choices?
- How should authority be represented so it is explicit, inspectable and difficult for the constrained component to rewrite?
- What are common authority-leak patterns in agent/tool systems?
- When does separation of roles reduce conflict of motivation, and when does it only add coordination cost?
- What escalation design avoids both hidden owner orchestration and unsafe autonomous widening?

### Evidence classes

- access-control / least-privilege / separation-of-duties literature;
- human-in-the-loop governance and safety evidence;
- concrete privilege-escalation/failure cases;
- motivation/function-allocation analyses;
- authority-boundary adversarial scenarios.

### Strong falsifiers / counter-frames

- proposed separation merely relocates authority ambiguity;
- no non-circular actor can accept/dispose a technical finding;
- safety mechanism turns human owner into routine scheduler/verifier;
- protected control remains writable by the component it constrains.

### Downstream decision dimensions

Phase 1 human-governance principles; Phase 8 authority/policy/safety/human governance.

---

## D5 — Evidence, provenance, verification and completion

### Foundation demand

Plausible narrative/tool success/agent agreement/self-declaration are not proof. Completion requires acceptance conditions, evidence obligations, required verification, policy gates and human approvals. High-impact analytical claims require traceable provenance.

### Researchable questions

- Which claim types admit deterministic verification, which require semantic/evaluative judgement, and which remain fundamentally uncertain?
- What forms of independence materially reduce correlated error?
- How should exact-target freshness and evidence-to-claim binding work across evolving artefacts?
- How can systems distinguish `used real data` from `recommendation actually derived from data`?
- Which completion states and evidence thresholds are proportionate to risk?

### Evidence classes

- software/system verification and validation prior art;
- scientific reproducibility/provenance methods;
- evaluation science / benchmark design;
- adversarial/mutation/negative tests;
- same-model versus diverse independent review comparisons where possible.

### Strong falsifiers / counter-frames

- green test never exercises the claimed rejected/failure state;
- verifier inherits producer rationale before deriving expectations;
- exact target changes after review;
- multiple agreeing models share the same source/frame failure;
- analytical conclusion cannot be reconstructed from method/inputs/source.

### Downstream decision dimensions

Phase 1 completion semantics; Phase 7 evidence/provenance/verification/evaluation architecture.

---

## D6 — Failure representation, containment, recovery and liveness

### Foundation demand

Unknown/unverified/blocked/partial/stale/conflicted/failed are legitimate states. Failures must not become silent drift or false completion and must have bounded recovery paths.

### Researchable questions

- What agentic failure taxonomy is sufficiently general across domains without becoming an unbounded defect catalogue?
- Which failure classes require prevention, detection, containment, recovery, human escalation, or explicit non-completion?
- How should partial success, uncertainty, stale state, conflicting evidence and not-assessable conditions be represented?
- What distinguishes a bounded repair from a required reframe/redesign/research path?
- What liveness/deadlock/starvation failures are introduced by stronger control processes?

### Evidence classes

- historical failure corpus from KEEL/SOUL/predecessors;
- cross-domain incident/failure literature;
- fault-tolerance/recovery prior art;
- state-machine counterexamples;
- adversarial failure injection / recovery scenarios.

### Strong falsifiers / counter-frames

- failure taxonomy only names software-development problems;
- recovery semantics require inventing architecture during the incident;
- a `safe fallback` discards later canonical truth;
- stronger gates produce unbounded meta-work or deadlock.

### Downstream decision dimensions

Phase 3 Failure Model; Phase 6 runtime/recovery; Phase 10 observability.

---

## D7 — Learning, controlled evolution and missing-capability admission

### Foundation demand

Repeated validated lessons should become stronger controls where practicable. Running work may not silently rewrite the rules by which its own correctness/authority/completion are judged. Missing capabilities follow a governed build/test/verify/admit lifecycle.

### Researchable questions

- When is a repeated failure sufficiently general to justify a durable control or architectural change?
- How can lessons be invoked at the relevant future moment without indiscriminate context loading?
- What separates local repair, class-level control, architecture change and foundation reopening?
- What evidence should be required before a generated capability is admitted?
- How can rollback/disable/forward restoration preserve truth after a bad evolution step?

### Evidence classes

- software change-control / configuration-management / safety-case prior art;
- online adaptation/self-modification research;
- mutation/regression evidence;
- historical lesson-transfer failures;
- prospective capability-admission trials.

### Strong falsifiers / counter-frames

- lesson exists only as prose and is repeatedly missed;
- new capability self-certifies or changes admission criteria;
- replay/historical evidence is treated as proof of future generalisation;
- rollback lacks invariants and forward-restoration semantics.

### Downstream decision dimensions

Definition's Evolution concern; Phase 9 Self-Extension Architecture; Phase 13 hardening/migration.

---

## D8 — Observability and reconstructability

### Foundation demand

A human must be able to determine what is happening, why, under whose authority, with what evidence, what is blocked, and why the system stopped. Observability is part of correctness.

### Researchable questions

- What minimum event/state/decision/evidence trace lets a fresh human or agent reconstruct material behaviour without replaying hidden reasoning?
- How should traces distinguish state truth from explanatory/derived views?
- What observability is required for failure diagnosis, authority audit, verification and cost control?
- How can observability avoid turning into unbounded logging/context growth?

### Evidence classes

- distributed-systems/observability prior art;
- audit/event-sourcing/provenance literature;
- forensic reconstruction exercises;
- operator usability studies/scenarios;
- omission and stale-view tests.

### Strong falsifiers / counter-frames

- operator cannot explain why system stopped or who authorised a material action;
- trace exists but cannot establish causal/state sequence;
- observability data becomes another conflicting source of truth;
- trace volume makes retrieval/diagnosis less reliable.

### Downstream decision dimensions

Phase 10 Observability and Operational Model; cross-cutting all phases.

---

## D9 — Generality, domain transfer and task-specific architecture

### Foundation demand

SOUL's generality must come from deriving task-specific operating systems above a stable core, not from encoding one fixed workflow. A credible v1 needs materially different pilots; one successful domain is insufficient evidence.

### Researchable questions

- Which properties are genuinely invariant across software production, analytical decision support, research/design/operations and other materially different work?
- Which properties must remain task-specific rather than entering core?
- What scenario families are sufficiently different to falsify software-development overfitting?
- What counts as transfer versus superficial reuse of shared vocabulary?
- How should capability/failure coverage be evaluated across domains before implementation technology is chosen?

### Evidence classes

- cross-domain comparative task analysis;
- materially different scenario stress tests;
- domain-specific standards/prior art where relevant;
- transfer/generalisation evaluation;
- negative cases where a proposed core abstraction fails or becomes domain leakage.

### Strong falsifiers / counter-frames

- core requires software-specific workflow semantics to function;
- same mechanism works only because pilots share hidden structure;
- success criteria are measurable only in one domain;
- a claimed invariant becomes contradictory or meaningless in another domain.

### Downstream decision dimensions

Phase 1 system/non-system boundary; Phase 2 capability coverage; Phase 3 failure coverage; Phase 12 pilots/evaluation.

---

# Cross-cutting evidence classes

The dimensions above imply at least six **different evidence functions**. They are not interchangeable.

1. **Normative/foundation authority** — defines current values/constraints; evidence can challenge feasibility/consistency but not silently override authority.
2. **Historical/observational failure evidence** — shows what occurred; does not alone establish universal cause or generality.
3. **External primary/prior-art evidence** — shows known mechanisms, standards, hazards or trade-offs; popularity/convergence does not decide SOUL architecture.
4. **Comparative scenario evidence** — tests whether a concept/property transfers across materially different domains and hidden assumptions.
5. **Causal/experimental evidence** — needed when claiming a specific component/role/control causes improvement or is necessary; bundled-treatment evidence may be insufficient.
6. **Independent challenge/verification evidence** — tests conformance, hidden assumptions or failure paths; must be calibrated to claim and independence level.

# Initial deduplication result

The 14 current success criteria do **not** require 14 independent research programmes. They cluster into nine higher-level dimensions above.

Potential overlaps to watch in Stage 2:

- D3 context/knowledge and D8 observability may share provenance/state mechanisms but protect different properties.
- D4 authority and D5 verification both use separation, but authority correctness and epistemic correctness are distinct.
- D6 recovery and D7 evolution both respond to failure; recovery restores work, evolution changes the system for future work.
- D2 capability formation and D9 generality intersect; capability categories must not be inferred from one domain.

# Stage-1 conclusion

Foundation extraction supports a research programme organised around **properties and failure obligations**, not technologies or existing KEEL folders.

The next stage must try to break this nine-dimension map using the already reconstructed KEEL/os-architect/SOUL failure evidence:

- Does any observed failure not fit?
- Are any dimensions only implementation concerns rather than pre-architecture research obligations?
- Is a dimension too broad to have a meaningful stopping condition?
- Did foundation wording cause us to miss a credible counter-frame?
- Are we accidentally treating a non-negotiable implementation shape as a fixed property?

Only after that adversarial mapping should evidence requirements and stopping conditions be frozen.