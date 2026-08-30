# SOUL Research Dimension Map — Stage 2 historical-failure red team

**Status:** active; foundation-derived + historical-failure challenged, not architecture  
**Date:** 2026-08-30

## Purpose

Translate SOUL's accepted/current foundation and Phase-1..3 roadmap gates into **research dimensions and evidence obligations** without converting them into mechanisms, roles, tools, services or a product backlog.

This stage deliberately distinguishes:

- **Foundation constraint / owner-defined property:** currently authoritative; research does not vote on whether SOUL should have it.
- **Researchable system question:** evidence can inform how the property can be satisfied, what failure classes threaten it, what capabilities are necessary, and which alternative layers/control patterns are credible.
- **Empirical/generalisation claim:** requires scenario, experiment, comparative or field evidence rather than prose alone.

Stage 2 additionally attacks the foundation-derived map with the reconstructed KEEL/os-architect/SOUL failure corpus. The purpose is to detect missing dimensions rather than force all failures into a convenient taxonomy.

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

Historical challenge sources:

- `research/soul-context/repos/os-architect/README.md`
- `research/soul-context/repos/keel/README.md`
- `research/soul-context/repos/soul/README.md`
- `research/soul-context/notes/transition-to-soul.md`
- `research/soul-context/notes/research-to-architecture-boundary.md`

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
- critical control state cannot be solely controlled by the component it constrains;
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

## D10 — Work selection, decomposition, orchestration and lifecycle

### Why Stage 2 added this dimension

The Stage-1 nine-dimension map did not cleanly represent two independent historical signals:

1. os-architect's **working-loop failure**: static state can survive while work movement, responsibility, update obligation and next action do not;
2. SOUL WP-021's current Development-OS failure hypothesis: a material result can be faithfully integrated yet still be routed too quickly into `repair`, so **result integration and substantive next-work selection are different functions**.

SOUL `DEFINITION.md` independently lists execution, orchestration, handoff, verification, evaluation, recovery and completion under Runtime. Therefore this is not merely a predecessor-process quirk.

### Foundation demand

The generated task-specific system must not only possess capabilities; it must turn the current objective/state/evidence into correctly bounded next work, sequence/decompose it, coordinate responsibility and handoff, and reach explicit completion/non-completion without losing purpose or becoming trapped in local execution momentum.

### Researchable questions

- How should a system select the **next unit of work** from objective, state, dependencies, evidence, risk and unresolved decisions without defaulting to the previous actor's completion frame?
- When is work decomposition too coarse, too fine, too serial, or unnecessarily multi-agent?
- How are result integration, next-work selection, technical design and implementation motivations separated when materially necessary without multiplying roles by default?
- How should risk/uncertainty determine reasoning depth before execution?
- What handoff contract preserves objective, protected properties, evidence, unresolved assumptions and reopen conditions rather than only task status?
- How are oscillation, deadlock, starvation, infinite investigation and premature closure represented and bounded?
- When does a material finding justify repair, reframing, research, redesign, roadmap change or a genuine owner decision?

### Evidence classes

- historical work trajectories from SOUL/KEEL/predecessors;
- workflow/project/program decision prior art where it addresses stateful work selection rather than generic planning advice;
- process-mining / incident reconstruction;
- blind replay or holdout trajectories with future findings hidden;
- simpler-routing versus separated-responsibility comparisons;
- cross-domain work-lifecycle cases where the same work-selection logic is stressed by different task structures.

### Strong falsifiers / counter-frames

- added planner/role/gate complexity detects no material failure earlier than a simpler baseline;
- faithful result integration still manufactures a repair-shaped task without a separate justified decision;
- handoff preserves status but loses purpose, assumptions or decision rationale;
- route classification oscillates or permanently escalates without a representable terminal state;
- implementation actor silently redesigns because the build-ready boundary is not meaningful;
- process overhead/owner interventions grow without measured reliability benefit.

### Downstream decision dimensions

Phase 1 lifecycle/completion principles; Phase 2 function/capability allocation; Phase 6 runtime/orchestration/recovery; cross-cutting Development OS learning.

---

# Cross-cutting evidence classes

The dimensions above imply at least six **different evidence functions**. They are not interchangeable.

1. **Normative/foundation authority** — defines current values/constraints; evidence can challenge feasibility/consistency but not silently override authority.
2. **Historical/observational failure evidence** — shows what occurred; does not alone establish universal cause or generality.
3. **External primary/prior-art evidence** — shows known mechanisms, standards, hazards or trade-offs; popularity/convergence does not decide SOUL architecture.
4. **Comparative scenario evidence** — tests whether a concept/property transfers across materially different domains and hidden assumptions.
5. **Causal/experimental evidence** — needed when claiming a specific component/role/control causes improvement or is necessary; bundled-treatment evidence may be insufficient.
6. **Independent challenge/verification evidence** — tests conformance, hidden assumptions or failure paths; must be calibrated to claim and independence level.

## Cross-cutting burden-of-proof metrics

These are not separate architecture dimensions, but any proposed research-backed control/process should be evaluated against them where material:

- false-positive / false-negative cost;
- owner intervention burden;
- agent/tool/token/time cost;
- context load versus omission/error rate;
- coordination/handoff failure rate;
- complexity introduced versus failure class prevented/detected;
- liveness / latency to safe completion;
- generalisation versus domain-specific special casing.

`more analysis`, `more roles`, `more files` or `fewer reviewer findings` are not success metrics by themselves.

# Stage 2 — historical-failure coverage attack

## Reconstructed failure classes mapped to dimensions

| Historical / current failure class | Primary dimension(s) | Coverage judgement |
|---|---|---|
| repo bloat, duplicate truth, mixed information lifetimes, inaccessible canonical files | D3, D8 | covered; authority/lifetime/retrieval + reconstructability |
| state survives but work movement/update responsibility/next action does not | **D10**, D8 | **Stage-1 gap; caused D10 addition** |
| echo/self-citation, shared-source agreement, verifier blindness, false green | D5 | covered; independence/oracle/falsifiability |
| question treated as task; premise/goal not re-derived | D1 | covered |
| session preserves result but loses purpose/reason | D1, D3, D10 | covered only with D10; purpose must survive handoff, not merely state |
| owner becomes hidden orchestrator or technical verifier | D4, D10 | covered |
| learned lesson remains prose / applied in one sibling line but not another / not invoked at need time | D7, D3 | covered; evolution + retrieval trigger |
| control is green but measures the wrong property or produces zero information | D5, D6 | covered; claim-to-test validity + failure detection |
| combined role motivations bias plan/design/build toward completion | D2, D4, D10 | covered; function necessity + authority + work lifecycle |
| material finding auto-routes into repair-shaped work | **D10**, D6 | **Stage-1 gap; caused D10 addition** |
| selective context hides unknown-needed counter-evidence | D3, D5 | covered; omission-aware retrieval + evidence completeness |
| rollback/fallback asserted without lifecycle semantics | D6, D7 | covered; recovery versus governed evolution |
| KEEL guarantee depends on Claude Code hooks/tool metadata | D9, D2 | covered; domain/runtime-specific mechanism versus invariant capability |
| human-readable prose and machine state are mixed, creating drift/ambiguous truth | D3, D8 | covered |
| separate reviewer seat shares same model/frame and produces pseudo-independence | D5, D9 | covered; epistemic independence + generalisation across perspectives |
| existing mechanism anchors redesign; `would we build this from zero?` omitted | D2, D10; research-process cross-cut | covered as necessity/alternative-layer challenge; not a standalone product dimension |
| new process/role complexity grows without measured benefit | D2, D10; cross-cut burden metrics | covered as necessity and proportionality, not separate foundation property |

## Stage-2 result

The initial map was **not complete**. Historical failure evidence forced D10.

After adding D10, no currently reconstructed high-level failure class is completely unmapped. That does **not** prove completeness. It only means the known predecessor corpus no longer supplies an obvious uncovered class.

This is exactly where confirmation risk increases: the map is now partly shaped by the same failure corpus used to test it. Therefore the next validity step must use **materially different external/domain scenarios**, not more internal KEEL/SOUL examples.

# Current ten-dimension map

1. D1 — Intended outcome → bounded work definition
2. D2 — Task-specific system formation and capability derivation
3. D3 — State / memory / context / knowledge / retrieval
4. D4 — Authority / bounded agency / human governance
5. D5 — Evidence / provenance / verification / completion
6. D6 — Failure representation / containment / recovery / liveness
7. D7 — Learning / controlled evolution / capability admission
8. D8 — Observability / reconstructability
9. D9 — Generality / domain transfer / task-specific architecture
10. D10 — Work selection / decomposition / orchestration / lifecycle

# Remaining challenge before freezing dimensions

## 1. External/domain holdout challenge

The current dimensions were derived from SOUL foundation and challenged with SOUL/KEEL/predecessor history. That is not independent enough to claim generality.

Need materially different scenario families that can reveal missing dimensions without inheriting software-development language.

At minimum test against:

- analytical decision-support work with uncertain/conflicting evidence and consequential recommendation;
- open-ended research / synthesis work where completion and evidence saturation differ from artifact delivery;
- operational / coordination work with changing external state, temporal deadlines and recovery needs.

A fourth scenario may be needed if these three still share hidden knowledge-work structure.

## 2. Pre-architecture relevance challenge

For each D1–D10 ask:

- must this be researched before Phase 1–3 decisions, or can it wait for a later phase?
- what minimum unknown must be resolved now?
- what would be premature implementation detail?

The dimension may remain architecturally important while only part of it belongs in the pre-architecture research programme.

## 3. Stopping-condition challenge

A dimension is too broad if no evidence can say `enough for the next decision`.

Before freezing, each dimension needs:

- exact decision-critical unknowns;
- minimum evidence classes;
- disconfirming evidence/falsifier;
- known limitations;
- explicit point where remaining uncertainty can be deferred to a later phase/test.

# Stage-2 conclusion

The research programme should currently be organised around **ten property/failure dimensions**, not technologies, frameworks, KEEL folders, or a growing catalogue of historical defects.

The map remains provisional until external/domain holdout scenarios challenge it. The next step is therefore not to collect literature for all ten dimensions indiscriminately. It is to design a small **scenario holdout matrix** that can falsify the dimension set, expose software-development frame leakage, and identify which parts of D1–D10 truly need evidence before Phase 1–3.