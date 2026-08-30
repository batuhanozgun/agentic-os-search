# Research → Architecture Boundary — evidence synthesis

**Status:** active synthesis; direct SOUL evidence + predecessor prior art + bounded inference  
**Date:** 2026-08-30

## Question

What contract should separate SOUL Research outputs from SOUL architecture decisions, and what does the current evidence imply about the role and stopping condition of this research project?

This note does **not** define SOUL architecture. It separates:

- direct SOUL development-governance evidence,
- predecessor research-house prior art,
- observed Development OS failure lessons,
- bounded implications for the research programme.

## 1. Direct SOUL contract: research is evidence, not decision

Primary SOUL governance is explicit:

- `development/01_governance/ROLE_MODEL.md`: Researcher establishes external or empirical evidence needed by a decision; it may survey sources, compare alternatives and record uncertainty, but may not silently turn findings into architecture decisions or omit conflicting evidence.
- `development/05_evidence/EVIDENCE_TEMPLATE.md`: an evidence record must state its question, source/method, supported findings, limitations, what it **does not prove**, and decision relevance. It must not state an architecture decision unless the proper decision process has accepted it.
- `development/01_governance/DECISION_POLICY.md`: **Research is not decision.** Architecture evidence must be connected to SOUL's own requirements and constraints through the decision process. Architecture decisions require an ADR and independent review before acceptance; foundation decisions additionally require impact analysis, independent verification of the claimed need and human-owner approval.

Therefore the direct SOUL boundary is not `research result → architecture truth`.

A more faithful chain is:

**question / evidence gap → research evidence → design/decision synthesis → explicit ADR or bounded work decision → independent challenge/verification → accepted or reopened decision**.

## 2. Architecture must not inherit KEEL or current tools as schema

`development/02_architecture/README.md` states that KEEL is evidence and prior art, not the default SOUL schema. A KEEL mechanism may be retained only after it is mapped to a required capability or architectural property in the new design.

`development/03_plan/ROADMAP.md` reinforces the ordering:

1. Phase 1 defines SOUL's purpose/boundaries/lifecycle/completion/governance.
2. Phase 2 derives capability architecture without current KEEL folders/mechanisms as the organising principle.
3. Phase 3 derives the failure model and control ownership.
4. Technology/component choices are deferred until Phase 11, after accepted architecture exists.

Implication: early research should primarily inform **definition, capability necessity/coverage, failure classes, control properties, trade-offs and falsifiers**. Framework/tool selection is downstream unless a concrete research question requires it as evidence.

## 3. SOUL's current research-quality requirements

`REASONING_POLICY.md` requires, when external knowledge matters:

- primary or authoritative sources for current technical facts when possible;
- version/date re-check for time-sensitive claims;
- preservation of disagreements and limitations;
- similarity not treated as equivalence;
- popularity not treated as architecture quality;
- available tools/frameworks not allowed to define the problem before requirements;
- for analytical claims, provenance appropriate to risk: `claim → computation/method → inputs/data → source/version`.

It also explicitly rejects indefinite research merely because more information could be collected once the defined completion condition has been met.

These rules define evidence quality, but the present Phase-0 repository does not yet contain a complete SOUL-product research completion schema for Phases 1–3.

## 4. Development OS learned that evidence must not auto-route to repair

`WP-021-DEVELOPMENT-LIFECYCLE-WORK-SELECTION-IMPROVEMENT.md` is direct process evidence that the previous routing was too eager to transform material FAIL / Requires-repair results into repair-shaped implementation work.

WP-021's target correction is stronger than `reason more`:

- substantive next-work selection is separate from result integration and implementation;
- `repair` must be a conclusion, not an automatic default;
- the next work may instead be design, reframing, investigation, research into another control/state layer, roadmap revision or a real owner decision;
- research is conditional on an evidence gap and remains evidence rather than decision authority;
- more analysis or more artefacts is not a success metric.

This yields a key boundary for SOUL Research:

**research should be opened because a decision-critical uncertainty can change the next authorised work or downstream design, not because research is generally desirable.**

## 5. Pre-build assurance: independent evidence paths are non-substitutable

WP-021/WP-022 establish a candidate pre-build chain for material process design:

1. freeze a design candidate on an exact target;
2. fresh separate adversarial review of the **design before implementation**;
3. historical replay/development evaluation under frozen criteria;
4. synthesize surviving findings and replay results;
5. revise/freeze a build-ready design;
6. do not implement while a material design finding remains unresolved;
7. after implementation, require fresh exact-target verification and separate post-build adversarial review.

WP-022 makes an important epistemic point: a clean adversarial review does not remove the replay requirement, and replay evidence does not remove the adversarial-review requirement. They attack different error surfaces.

For SOUL Research this suggests that one evidence type should not silently stand in for another:

- literature convergence ≠ causal effectiveness;
- historical replay ≠ generalisation;
- verifier conformance ≠ frame/design robustness;
- multi-model agreement ≠ independent ground truth.

## 6. Four current failure lessons for research → architecture handoff

The 2026-08-29 pre-build adversarial review of WP-021 produced four medium/material findings. These are Development OS findings, not automatically SOUL product requirements, but they expose handoff hazards relevant to research design.

### F-AR-009 — acceptance authority can be circular or unowned

Evidence/challenge is insufficient if no non-circular actor/rule determines that material findings are resolved and an architecture decision may transition status.

Research implication:
- a research report should not contain an implicit `therefore adopt` transition;
- downstream decision ownership, independent challenge and fresh-target status must remain explicit.

### F-AR-010 — bundled treatment cannot establish component necessity

The proposed replay changed Planner, Designer/Builder separation, Researcher use, pre-build review and execution count together. Without an ablation or credible comparator, a better bundle cannot establish that a permanent Planner is necessary.

Research implication:
- when a durable role/control/mechanism is justified by an effectiveness claim, the evidence design must distinguish package benefit from component necessity;
- ablation, simpler baseline or alternative causal identification may be required.

### F-AR-011 — selective context can hide decisive evidence without detection

`required-now / retrieve-on-trigger / forensic` labels are unsafe if classification authority, candidate-source inventory, omission detection and unknown-trigger recovery are missing.

Research implication:
- a curated research synthesis is a derived view, not source completeness;
- downstream consumers need enough provenance and omission-awareness to recover disconfirming or unexpectedly relevant sources;
- `not retrieved` must not become `does not exist`.

### F-AR-012 — rollback is not real until lifecycle semantics exist

A checkpoint/branch proves prior state availability, not safe recovery after later canonical work.

Research implication:
- claims such as `reversible`, `safe fallback`, `recoverable` or `can be rolled back` require explicit invariants, disable/partial-rollout behaviour and forward-restoration semantics when they carry architectural weight.

## 7. Predecessor research-house prior art — informative, not SOUL authority

`batuhanozgun/keel-research/PROMOTION.md` has an explicit historical boundary:

> the research repo produces research, not a product backlog.

Its four layers are:

1. research package;
2. anatomy placement;
3. accumulated epistemic judgement;
4. product promotion through a separate conscious owner/product evaluation.

It classifies research signals as `SUPPORT`, `GAP`, `RISK`, `CONTRADICTION`, `UNTESTED`, `ALTERNATIVE`, explicitly stating that these are not TODOs, feature requests or bugs.

Before promotion it asks whether the problem is still real/material, whether evidence is replicated, whether existing mechanics already cover it, whether change complexity creates new failure modes, whether more evidence is required, and which parts are owner value choices versus technical judgements.

This is predecessor prior art, not a current SOUL rule. Its relevance is that SOUL independently arrives at the same higher-level separation in `ROLE_MODEL`, `EVIDENCE_TEMPLATE`, `DECISION_POLICY` and WP-021: **epistemic signal and product work are different state transitions.**

## 8. Minimal current model of the boundary

The strongest evidence-supported working model is:

**Research informs. Work selection decides what kind of next work is justified. Design/ADR turns evidence into a candidate technical commitment. Independent verification/challenge constrains the claim. Accepted governance changes status. Implementation comes later.**

No one step should silently absorb the authority of the next.

In particular:

- research finding ≠ requirement;
- requirement/capability hypothesis ≠ mechanism;
- mechanism candidate ≠ accepted architecture;
- verification PASS ≠ adversarial robustness;
- historical success ≠ generalisation;
- accepted design ≠ implementation proof.

## 9. Provisional output shape for SOUL Research

This is a bounded inference from the direct contracts above, not a discovered verbatim SOUL Research charter.

A useful research output for later architecture work would likely be a **decision-oriented evidence package** containing at least:

- exact question / decision dimension informed;
- why the uncertainty is material;
- observations vs inferences vs assumptions;
- primary/authoritative sources and versions;
- conflicting evidence / alternatives;
- source quality and known omissions;
- what the evidence supports;
- what it explicitly does not prove;
- relevant capability/failure/control-property hypotheses;
- credible alternative frames/layers;
- strongest falsifiers / disconfirming evidence;
- where causal necessity is and is not identified;
- remaining uncertainty and what additional evidence would change the decision;
- downstream decision relevance without an embedded architecture verdict.

## 10. Provisional stopping condition

No canonical SOUL Research stopping contract has yet been found in the checked research workspace or Phase-0 product tree.

The best evidence-supported provisional rule is therefore:

**stop a research line when its defined decision-critical uncertainty has been reduced enough that additional evidence is unlikely to change the authorised next-work/design decision at the required risk level, or when the remaining uncertainty is explicitly bounded and must be resolved by another method/phase.**

This is stronger than `we read enough sources`, but it still requires later formalisation before becoming a project-wide research rule.

## 11. Open gaps

1. No separate verbatim `SOUL Research charter` or research→architecture handoff schema was found in the checked `research/soul-context` tree.
2. The current SOUL Phase-0 tree has roadmap descriptions for Phases 1–3 but no accepted Phase-1/2/3 work packages demonstrating the downstream contract in use.
3. The proposed Development OS lifecycle is itself under design revision after WP-022; it is evidence about failure classes, not accepted governance.
4. True model-level independence remains unresolved; fresh same-model context reduces anchoring but is not independent ground truth.
5. Generalisation across materially different SOUL tasks is not yet demonstrated.
6. Selective-context completeness / omission detection remains an open design problem.
7. A formal SOUL Research package schema, stopping rule and promotion/handoff gate still need to be derived rather than assumed.

## 12. Next research question

The next high-information question is no longer `does research differ from architecture?` — that is directly established.

It is:

**What are the minimum research dimensions and evidence classes SOUL must cover before Phase 1–3 can define SOUL, derive capability architecture and build a failure model without inheriting KEEL's frame or producing an unbounded research programme?**

Answering that requires deriving the research question map from the now-established product intent, predecessor failure classes, roadmap gates and explicit counter-evidence — not proposing SOUL mechanisms.