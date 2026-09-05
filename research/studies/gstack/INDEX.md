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
| Final four-ground view | not yet produced | only after gstack-native subsystem model is sufficiently stable |
| Cross-ground mechanisms | not yet produced | keep gstack-native/neutral until later Foundation comparison is authorised and mature |

## Current durable syntheses

### `syntheses/planning-specification-work-admission.md`

Bounded reconstruction of the first studied mechanism chain:

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

It is **not** a whole-gstack lifecycle conclusion. The immediate open dependency is whether later review/QA/ship mechanisms consume and enforce these qualified states.

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

The observed repository supports at least these research clusters; boundaries remain revisable while subsystem reconstruction is active:

1. governing ethos / behavioral policy / skill-generation contract;
2. **planning / specification / work admission — first bounded synthesis exists**;
3. review / investigation / QA / verification;
4. browser / tool-use runtime and persistent execution environment;
5. security, permission, isolation and guarded action;
6. memory, learnings, context and GBrain mechanisms;
7. multi-agent / cross-model coordination;
8. host adapters / model-portability layer;
9. ship, deploy, canary, production observation and retrospective feedback;
10. testing / eval / routing / compliance infrastructure;
11. repository self-development, generation and release mechanisms.

The earlier separate “product discovery/planning” and “work specification/orchestration” inventory clusters are provisionally merged into one bounded planning/specification/work-admission mechanism because source evidence shows they share authority gates, durable artifacts, and handoff semantics. This can be split again if later lifecycle evidence requires it.

These are research clusters, not claimed Foundation categories.

## Immediate next route

Study the **review → QA → ship admission chain** next, including review-readiness/dashboard consumers and the relevant tests. The key unresolved question is whether the qualifications produced upstream actually constrain shipping or are only recommendations/configurable signals.

## Guardrails

- Do not classify source files into Information/Work/Actors/Environment before their gstack-native role is understood.
- Do not treat prompt/template text as proof of executed behavior.
- Keep intended policy, structurally pinned contract, and behavioral E2E evidence distinct.
- Do not treat gstack's own documentation or tests as independent verification of gstack.
- Do not equate cross-model diversity with verification independence without checking shared framing/oracles.
- Keep promotional/retention behavior separate from evidence about work-system quality.
- Do not promote candidate patterns into Foundation/SOUL/Development OS merely because the external system implements them.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
