# gstack Study — INDEX

## Role

Retrieval router for the durable `garrytan/gstack` external-target study.

Read `STATE.md` first for current progress/authorization, `META.md` for epistemic boundary, and `SOURCE-LEDGER.md` for actual source coverage.

## Current study target

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
Observed 2026-09-05; package version 1.79.0.

## Current phase

**First/native subsystem layer: boundedly complete (11 syntheses).**  
**Current next layer: cross-system composition.**

## Read routes

| Need | Read first | Then |
|---|---|---|
| Current progress / next work | `STATE.md` | relevant synthesis / ledger |
| Scope / authority / freshness | `META.md` | `METHOD.md` |
| Actual source coverage | `SOURCE-LEDGER.md` | pinned upstream source |
| Planning / work admission | `syntheses/planning-specification-work-admission.md` | ledger → sources |
| Review / QA / ship | `syntheses/review-qa-ship-delivery-qualification.md` | ledger → sources |
| Browser runtime / security / evidence | `syntheses/browser-runtime-security-evidence.md` | ledger → sources |
| Investigation / causal control | `syntheses/investigation-root-cause-debug-control.md` | ledger → sources |
| Memory / learnings / GBrain | `syntheses/memory-learnings-context-gbrain.md` | ledger → sources |
| Multi-agent / cross-model | `syntheses/multi-agent-cross-model-coordination.md` | ledger → sources |
| Guarded action / CSO security | `syntheses/guarded-action-security-review.md` | ledger → sources |
| Host adapters / portability | `syntheses/host-adapters-portability-fidelity.md` | ledger → sources |
| Deploy / Canary / production feedback | `syntheses/deploy-canary-production-retrospective-feedback.md` | ledger → sources |
| Testing / eval / routing / compliance | `syntheses/testing-eval-routing-compliance-flake-lifecycle.md` | ledger → test/eval sources |
| Self-development / generation / upgrade / release | `syntheses/repository-self-development-generation-upgrade-release.md` | ledger → generator/setup/upgrade/version/history sources |
| Cross-system composition | not yet produced | **current next layer** |
| Four-ground projection | not yet produced | after cross-system model stabilizes |

## Native synthesis set

1. **Planning / specification / work admission** — qualification before work admission.
2. **Review / QA / delivery qualification** — qualification before delivery; current standing can be recomputed.
3. **Browser runtime / security / evidence** — capability/effect/evidence boundaries and freshness.
4. **Investigation / root-cause / debug control** — hypothesis-driven causal debugging; systemic RCA not guaranteed.
5. **Memory / learnings / context / GBrain** — qualified prior information; stale-fallback label can be lost before planning consumption.
6. **Multi-agent / cross-model coordination** — context/authority/completion/result/liveness semantics; fresh context ≠ model independence.
7. **Guarded action / security review** — preventive hooks, one-way human authority, CSO detective qualification; enforcement can degrade to prose across hosts.
8. **Host adapters / portability fidelity** — typed host compilation plus runtime materialization; support is a ladder, not a boolean.
9. **Deploy / Canary / production / retrospective feedback** — merge, deploy and live-health standings separated; rollback closure and release-identity proof remain incomplete.
10. **Testing / eval / routing / compliance / flake lifecycle** — test existence, selection, execution, oracle, retry/flake and finalized evidence are separate standings.
11. **Repository self-development / generation / upgrade / release** — authored source, generated behavior, installed runtime, running process, migration and release identity are separate standings.

## First-layer closure result

The subsystem layer is sufficiently complete for the pinned revision to stop adding more sibling clusters. Chronology/evolution was sampled horizontally rather than treated as a twelfth taxonomy branch.

The evolution evidence supports a recurring pattern:

```text
prose / local convention
→ concrete failure
→ named state distinction
→ reusable resolver/helper/CLI
→ structural invariant/scanner
→ behavioral/environment E2E
→ CI/release consequence when justified
```

This is not universal or complete; the pinned repo still contains explicit negative findings where an outer standing flattens a more qualified state.

## Synthesis ladder

```text
pinned source
→ mechanism/subsystem syntheses            ← FIRST LAYER CLOSED
→ cross-system composition synthesis       ← NEXT
→ four-ground projection + neutral cross-ground mechanisms
→ compact gstack core model
```

Higher synthesis never removes source re-entry.

## Immediate next route — cross-system composition

Central question:

> how do the 11 native subsystems compose into one operating system; which work, information, authority, evidence, standing and runtime objects cross subsystem boundaries; where are those objects re-qualified, invalidated, transformed or flattened; and what feedback loops make the system adaptive over time?

Priority views:

1. **End-to-end work lifecycle** — idea → discovery → admitted work → implementation → review/evidence → delivery → production → feedback → candidate future work.
2. **Authority/control plane** — human decision rights, child delegation, tool capabilities, host/runtime enforcement, security intervention and release authority.
3. **Information/evidence lineage** — source, plan, diff, review, runtime observation, memory, eval and release artifacts with their freshness/standing transitions.
4. **Runtime/environment plane** — repo/worktree, host, browser, process, filesystem, external systems and production surfaces.
5. **Feedback/self-development loops** — retro/learnings/evals/failures → new work → stronger controls → generation/setup/release.
6. **Seam analysis** — where qualification strengthens versus where metadata/standing is lost.

Produce one bounded gstack-native cross-system synthesis before any Foundation mapping.

## Guardrails

- Do not turn the subsystem list into the four-ground taxonomy prematurely.
- Keep authored intent, implemented control, test evidence and external/independent verification separate.
- Treat “gate”, “current”, “supported”, “secure”, “deployed”, “updated”, “reverted” and “green” as typed standings whose actual semantics must be named.
- Preserve known counterexamples; do not make the cross-system model cleaner than the implementation.
- Do not mutate Foundation from this candidate study.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
