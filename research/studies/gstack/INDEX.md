# gstack Study — INDEX

## Role

Retrieval router for the durable `garrytan/gstack` external-target study.

Read `STATE.md` first for current progress/authorization, `META.md` for epistemic boundary, and `SOURCE-LEDGER.md` for detailed source coverage.

## Current study target

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
Observed 2026-09-05; package version 1.79.0.

## Current phase

- **Layer 1 / native subsystems:** CLOSED — 11 bounded syntheses.
- **Layer 2 / cross-system composition:** CLOSED — `syntheses/cross-system-composition.md`.
- **Layer 3 / Foundation four-ground projection:** **NEXT**.

## Read routes

| Need | Read first | Then |
|---|---|---|
| Current progress / next work | `STATE.md` | relevant synthesis / source ledger |
| Scope / authority / freshness | `META.md` | `METHOD.md` |
| Detailed source coverage | `SOURCE-LEDGER.md` | pinned upstream source |
| Planning / work admission | `syntheses/planning-specification-work-admission.md` | ledger → sources |
| Review / QA / ship | `syntheses/review-qa-ship-delivery-qualification.md` | ledger → sources |
| Browser runtime / security / evidence | `syntheses/browser-runtime-security-evidence.md` | ledger → sources |
| Investigation / causal control | `syntheses/investigation-root-cause-debug-control.md` | ledger → sources |
| Memory / learnings / GBrain | `syntheses/memory-learnings-context-gbrain.md` | ledger → sources |
| Multi-agent / cross-model | `syntheses/multi-agent-cross-model-coordination.md` | ledger → sources |
| Guarded action / CSO security | `syntheses/guarded-action-security-review.md` | ledger → sources |
| Host adapters / portability | `syntheses/host-adapters-portability-fidelity.md` | ledger → sources |
| Deploy / Canary / production feedback | `syntheses/deploy-canary-production-retrospective-feedback.md` | ledger → sources |
| Testing / eval / routing / compliance | `syntheses/testing-eval-routing-compliance-flake-lifecycle.md` | ledger → sources |
| Self-development / generation / upgrade / release | `syntheses/repository-self-development-generation-upgrade-release.md` | ledger → sources |
| Whole native system | `syntheses/cross-system-composition.md` | subsystem syntheses → sources |
| Four-ground projection | not yet produced | **current next layer** |

## Native subsystem set

1. Planning / specification / work admission
2. Review / QA / delivery qualification
3. Browser runtime / security / evidence
4. Investigation / causal control
5. Memory / learnings / context / GBrain
6. Multi-agent / cross-model coordination
7. Guarded action / security review
8. Host adapters / portability fidelity
9. Deploy / Canary / production / retrospective feedback
10. Testing / eval / routing / compliance / flake lifecycle
11. Repository self-development / generation / upgrade / release

## Cross-system composition result

The current gstack-native model is:

> **an artifact-mediated, qualification-driven software-development operating system whose control plane repeatedly turns heterogeneous evidence and authority into bounded state transitions across repositories, agents, runtime tools, hosts and production surfaces.**

It is a federation of partial state machines rather than one global workflow engine.

### Core planes

```text
WORK / EFFECT PATH
intent → admitted work → implementation → delivery → production → feedback

AUTHORITY / CONTROL PLANE
user decisions → delegation → capabilities → one-way doors → release authority

EVIDENCE / REPRESENTATION PLANE
source → tests → runtime observations → reports → aggregates → standings

RUNTIME / ENVIRONMENT PLANE
repo/worktree → host/process/filesystem → browser/network → external systems → production

SELF-DEVELOPMENT PLANE
failure → source change → generation/install → eval → release → stronger controls
```

### Core native mechanisms

admission; representation/handoff; qualification; authority; capability/effect boundary; verification/observation; aggregation; transition; freshness/invalidation; continuity; feedback; adaptation/self-development.

These remain native abstractions, not Foundation categories.

## Synthesis ladder

```text
pinned source
→ native subsystem syntheses               ✓
→ cross-system composition synthesis       ✓
→ four-ground projection                   ← NEXT
→ neutral cross-ground mechanism synthesis
→ compact gstack core model
```

Higher synthesis never removes source re-entry.

## Immediate next route — Foundation projection

Before projecting, re-read current canonical Foundation state and the accepted boundaries for Information, Work, Actors and Environment. Foundation changed during this external study; do not project from stale summaries.

Then ask:

1. **Information:** what informational state, representation, transformation, selection/exposure, provenance/freshness and evidence machinery does gstack realize?
2. **Work:** how are pursuits admitted, organized, sequenced/parallelized, qualified, completed/deferred and distinguished from their representations/evidence?
3. **Actors:** which persistent parties/roles/agents carry participation, authority, obligation, attribution and responsibility; how are delegation/capability/collective roles realized?
4. **Environment:** what domain/work conditions, resources, runtime surfaces, constraints, dynamics and external state make or limit work?
5. **Cross-ground:** which native mechanisms bind these grounds operationally without being forced into one ground?

## Guardrails

- Foundation projection is comparison/retrieval, not automatic adoption.
- Do not force a native mechanism into exactly one ground when it is relational.
- Preserve counterexamples and qualification-loss seams.
- Keep authority, capability, evidence and effect distinct.
- Keep current standing separate from historical artifact/ceremony existence.
- Do not mutate Foundation from this study.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
