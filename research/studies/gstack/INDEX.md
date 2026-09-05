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
| Guarded action / CSO security | `syntheses/guarded-action-security-review.md` | ledger → sources |
| Host adapters / portability | `syntheses/host-adapters-portability-fidelity.md` | ledger → sources |
| Deploy / canary / production feedback | `syntheses/deploy-canary-production-retrospective-feedback.md` | ledger → land/deploy/canary/retro sources |
| Testing / eval infrastructure | not yet synthesized | **current next cluster** |
| Four-ground projection | not yet produced | after remaining native system syntheses |

## Current durable syntheses

1. **Planning / specification / work admission** — qualification before work admission.
2. **Review / QA / delivery qualification** — qualification before delivery; current standing can be recomputed.
3. **Browser runtime / security / evidence** — capability/effect/evidence boundaries and freshness.
4. **Investigation / root-cause / debug control** — hypothesis-driven causal debugging; systemic RCA not guaranteed.
5. **Memory / learnings / context / GBrain** — qualified prior information; stale-fallback label can be lost before planning consumption.
6. **Multi-agent / cross-model coordination** — context/authority/completion/result/liveness semantics; fresh context ≠ model independence.
7. **Guarded action / security review** — preventive hooks, one-way human authority, CSO detective qualification; enforcement can degrade to prose across hosts.
8. **Host adapters / portability fidelity** — typed host compilation plus runtime materialization; support is a ladder, not a boolean.
9. **Deploy / Canary / production / retrospective feedback** — merge, deploy and live-health standings separated; rollback closure and release-identity proof remain incomplete.

### Production-feedback retrieval summary

```text
qualified PR
→ readiness evidence
→ one-way merge authority
→ authoritative merge state
→ deployment evidence
→ immediate live verification
→ extended canary
→ history / retro / learnings
→ candidate future improvement
```

Key corrections:

- local merge command result is not authoritative remote merge state;
- deploy completion is not live-health completion;
- auto-deploy URL health is not automatically exact-release identity proof;
- Canary needs a genuine pre-deploy baseline for before/after regression attribution;
- rollback `REVERTED` does not prove rollback deployment + production restoration;
- failed-test “BLOCKER” prose and final merge-anyway menu are inconsistent;
- `/health` is code-quality health, not production health;
- Retro recommendations are informational feedback, not automatic Work admission;
- production E2Es largely simulate external effects;
- Canary behavior test existence and coverage-matrix attribution disagree.

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
9. host adapters / portability fidelity — **done**;
10. deploy / canary / production observation / retrospective feedback — **done**;
11. **testing / eval / routing / compliance infrastructure — NEXT**;
12. repository self-development / generation / update / release mechanisms.

These are research clusters, not Foundation categories.

## Immediate next route

Study **testing / eval / judge / routing / compliance / flake lifecycle**.

Central question:

> how does gstack decide what verification runs, distinguish structural/static evidence from real-agent behavior and LLM-judge evidence, prove the intended oracle actually executed, handle skips/flakes/cost/routing, and convert results into trustworthy confidence rather than false green?

Priority evidence:

- `package.json` test/eval commands;
- `test/skill-coverage-matrix.ts` and its validator;
- touchfile/diff routing and shard-selection helpers;
- free tests versus paid E2E and LLM-judge suites;
- Claude/Codex/Gemini session runners;
- eval artifact schema, aggregation/compare/summary/flake ranking;
- CI/gate/periodic selection and skip semantics;
- audit/compliance/slop scans;
- known falsifiers: Codex all-skip green, Canary coverage-route mismatch, simulated production E2Es.

## Guardrails

- Keep authored test intent, route metadata, actual execution, oracle validity and independent verification separate.
- A green job is not positive evidence if the intended test/runtime skipped.
- A real agent E2E is not necessarily a real external-system integration test.
- LLM-as-judge is an oracle with its own calibration/common-cause limits.
- Do not mutate Foundation from this candidate study.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
