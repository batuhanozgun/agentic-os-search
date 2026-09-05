# gstack Study — INDEX

## Role

Retrieval router for the durable `garrytan/gstack` external-target study.

Read `STATE.md` first for current progress/authorization, `META.md` for epistemic boundary, and `SOURCE-LEDGER.md` for actual read coverage.

## Current study target

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
Observed 2026-09-05; package version 1.79.0.

## Read routes

| Need | Read first | Then |
|---|---|---|
| Current progress / next work | `STATE.md` | relevant synthesis / ledger |
| Scope / authority / freshness | `META.md` | `METHOD.md` |
| Actual read coverage | `SOURCE-LEDGER.md` | pinned upstream source |
| Planning / work admission | `syntheses/planning-specification-work-admission.md` | ledger → sources |
| Review / QA / ship | `syntheses/review-qa-ship-delivery-qualification.md` | ledger → sources |
| Browser runtime / security / evidence | `syntheses/browser-runtime-security-evidence.md` | ledger → sources |
| Investigation / causal control | `syntheses/investigation-root-cause-debug-control.md` | ledger → sources |
| Memory / learnings / GBrain | `syntheses/memory-learnings-context-gbrain.md` | ledger → sources |
| Multi-agent / cross-model | `syntheses/multi-agent-cross-model-coordination.md` | ledger → sources |
| Guarded action / CSO security | `syntheses/guarded-action-security-review.md` | ledger → careful/guard/CSO/one-way sources |
| Host adapters / portability | not yet synthesized | **current next cluster** |
| Four-ground projection | not yet produced | only after native model stabilizes |

## Current durable syntheses

1. **Planning / specification / work admission** — qualification before work admission.
2. **Review / QA / delivery qualification** — qualification before delivery; current standing can be recomputed.
3. **Browser runtime / security / evidence** — capability/effect/evidence boundaries and freshness.
4. **Investigation / root-cause / debug control** — hypothesis-driven causal debugging; systemic RCA not guaranteed.
5. **Memory / learnings / context / GBrain** — qualified prior information; stale-fallback label can be lost before planning consumption.
6. **Multi-agent / cross-model coordination** — context/authority/completion/result/liveness semantics; fresh context ≠ model independence; v1.79 stranded-parent recurrence.
7. **Guarded action / security review** — preventive hooks, one-way human authority, CSO detective qualification; runtime enforcement can degrade to prose across hosts.

## Synthesis ladder

```text
pinned source
→ mechanism records
→ subsystem syntheses
→ cross-system synthesis
→ four-ground projection + neutral cross-ground mechanisms
→ compact gstack core model
```

Higher synthesis never removes source re-entry.

## Provisional subsystem map

1. governing ethos / behavioral policy / generation contract;
2. planning / specification / work admission — **done**;
3. review / QA / delivery qualification — **done**;
4. browser runtime / security / evidence — **done**;
5. investigation / causal control — **done**;
6. memory / learnings / GBrain — **done**;
7. multi-agent / cross-model coordination — **done**;
8. guarded-action / CSO security-review — **done**;
9. **host adapters / portability fidelity — NEXT**;
10. deploy / canary / production observation / retrospective feedback;
11. testing / eval / routing / compliance infrastructure;
12. repository self-development / generation / update / release mechanisms.

These are research clusters, not Foundation categories.

## Immediate next route

Study **host adapters / portability fidelity**.

Central question:

> when gstack renders one conceptual workflow for different coding-agent hosts, which semantics are genuinely preserved and which are rewritten, suppressed, approximated or weakened because the host has different tools, hooks, session semantics or model capabilities?

Priority evidence:

- `hosts/*.ts` type/config model;
- `scripts/gen-skill-docs.ts` host generation and safety-prose substitutions;
- tool/path rewrites and suppressed resolvers;
- Claude hooks versus external-host behavior;
- Codex-host Agent dispatch mismatch;
- GBrain/cross-model suppression;
- generated/golden host fixtures and tests;
- user-visible versus silent semantic degradation.

## Guardrails

- Understand gstack-native mechanism before four-ground projection.
- Keep authored policy, implementation, structural pins and behavioral evidence distinct.
- Do not equate syntactic generation success with semantic portability.
- Host capability must be part of any enforcement/authority claim.
- Do not mutate Foundation from this candidate study.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
