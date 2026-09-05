# gstack Study — INDEX

## Role

Retrieval router for the durable `garrytan/gstack` external-target study.

Read `STATE.md` first for current progress and authorization. Read `META.md` for the epistemic boundary and pinned target snapshot.

## Current study target

`garrytan/gstack` at pinned commit:

`0d1bd5616c0ef096bb7ccee336f63c60ee408618`

Observed 2026-09-05; commit timestamp 2026-09-01T23:42:11Z; package version 1.79.0.

## Read routes

| Need | Read first | Then |
|---|---|---|
| Current study progress / next work | `STATE.md` | relevant source ledger / synthesis |
| Scope, authority, freshness | `META.md` | `METHOD.md` |
| Why the research is structured this way | `METHOD.md` | `inventory/STRUCTURE.md` |
| What has actually been read | `SOURCE-LEDGER.md` | pinned upstream source |
| System/repository decomposition | `inventory/STRUCTURE.md` | subsystem syntheses as they are created |
| Discovery → planning → specification → work admission | `syntheses/planning-specification-work-admission.md` | `SOURCE-LEDGER.md`, then pinned sources for load-bearing reuse |
| Implementation → review/QA → ship qualification | `syntheses/review-qa-ship-delivery-qualification.md` | `SOURCE-LEDGER.md`, then pinned sources |
| Final four-ground view | not yet produced | only after gstack-native subsystem model is sufficiently stable |
| Cross-ground mechanisms | not yet produced | keep gstack-native/neutral until later Foundation comparison is authorised and mature |

## Current durable syntheses

### `syntheses/planning-specification-work-admission.md`

Bounded reconstruction of:

```text
idea / intent
  → discovery + premise/alternative qualification
  → approved durable design
  → scope / engineering review
  → executable specification
  → safety / quality / sink gates
  → issue + archive
  → optional isolated agent execution
```

Also covers interactive vs `/autoplan` delegated authority, generated-skill composition, selected deterministic invariants/E2Es, and the analytical separation of office-hours promotion/relationship behavior from planning-quality evidence.

### `syntheses/review-qa-ship-delivery-qualification.md`

Bounded reconstruction of implementation-to-release qualification:

```text
implemented branch
  → merged-code tests + failure ownership
  → semantic changed-path coverage
  → conditional plan completion gate
      → optional plan-driven browser verification
  → fresh pre-landing diff review
  → specialist / red-team / adversarial challenge
  → fix → re-test → re-review closure
  → evidence-bearing release / PR artifacts
```

Key result: gstack does **not** require a universal prior `review → QA → ship` ceremony. A current Eng Review is required by default as a qualification type, but `/ship` can satisfy it with its own fresh diff-scoped review. A discoverable plan, on the other hand, can become an active ship-time control object whose NOT DONE / UNVERIFIABLE items interrupt delivery until resolved or explicitly overridden.

Neither synthesis is a whole-gstack lifecycle conclusion. Browser/runtime security and post-landing production feedback remain open.

## Planned synthesis ladder

```text
Level 0  pinned gstack source
   ↓
Level 1  source-grounded notes / mechanism records
   ↓
Level 2  semantic subsystem syntheses
   ↓
Level 3  cross-system synthesis
   ↓
Level 4  four-ground projection + neutral cross-ground mechanisms
   ↓
Level 5  compact gstack core model
```

This is a synthesis hierarchy, not an evidence hierarchy: higher levels never replace the ability to descend to pinned source.

## Provisional subsystem map

The observed repository currently supports these research clusters; boundaries remain revisable:

1. governing ethos / behavioral policy / skill-generation contract;
2. **planning / specification / work admission — bounded synthesis exists**;
3. **review / QA / delivery qualification — bounded synthesis exists**;
4. **browser / tool-use runtime + persistent execution environment — NEXT**;
5. security, permission, tunnel/isolation and guarded action — likely coupled to cluster 4;
6. investigation/root-cause workflow;
7. memory, learnings, context and GBrain mechanisms;
8. multi-agent / cross-model coordination;
9. host adapters / model-portability layer;
10. deploy, canary, production observation and retrospective feedback;
11. testing / eval / routing / compliance infrastructure;
12. repository self-development, generation and release mechanisms.

The initial cluster map is already changing in response to source evidence: planning + specification merged because their authority/artifact transitions form one mechanism, while review/QA/ship formed a delivery-qualification mechanism rather than a simple lifecycle sequence. Continue allowing evidence to reshape these boundaries.

These are research clusters, not Foundation categories.

## Immediate next route

Study the **browser/runtime + security/permission boundary** next. QA and ship now rely on browser outputs as a distinct evidence channel, so the next dependency is to establish what `$B` actually does, what state it persists, how daemon/CDP/tunnel/listener boundaries are enforced, and which safety claims are runtime-enforced versus instruction-level.

## Guardrails

- Do not classify source files into Information/Work/Actors/Environment before their gstack-native role is understood.
- Do not treat prompt/template text as proof of executed behavior.
- Keep intended policy, implementation structure, deterministic pins and behavioral E2E evidence distinct.
- Do not treat gstack's own documentation or tests as independent verification of gstack.
- Do not equate cross-model diversity with verification independence without checking shared framing/oracles.
- Keep promotional/retention behavior separate from evidence about work-system quality.
- Treat “gate”, “required”, “always-on” and “coverage” according to their actual control semantics rather than labels.
- Do not promote candidate patterns into Foundation/SOUL/Development OS merely because the external system implements them.
- Do not silently substitute current gstack HEAD for the pinned snapshot.