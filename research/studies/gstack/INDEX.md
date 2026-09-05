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
| Research method | `METHOD.md` | `inventory/STRUCTURE.md` |
| Actual read coverage | `SOURCE-LEDGER.md` | pinned upstream source |
| Planning / work admission | `syntheses/planning-specification-work-admission.md` | ledger → pinned sources |
| Review / QA / ship qualification | `syntheses/review-qa-ship-delivery-qualification.md` | ledger → pinned sources |
| Browser runtime / security / evidence | `syntheses/browser-runtime-security-evidence.md` | ledger → pinned sources |
| Investigation / causal control | `syntheses/investigation-root-cause-debug-control.md` | ledger → pinned sources |
| Memory / learnings / context / GBrain | `syntheses/memory-learnings-context-gbrain.md` | ledger → checkpoint/learning/brain sources |
| Multi-agent / cross-model coordination | `syntheses/multi-agent-cross-model-coordination.md` | ledger → Agent/Codex/pairing sources |
| Guarded action / CSO security review | not yet synthesized | **current next cluster** |
| Four-ground projection | not yet produced | only after native model stabilizes |
| Cross-ground mechanisms | not yet produced | keep neutral until later Foundation comparison |

---

## Current durable syntheses

### 1. Planning / specification / work admission

`planning-specification-work-admission.md`

```text
intent
→ discovery / premise qualification
→ approved durable design
→ scope + engineering review
→ executable specification
→ safety / quality / sink gates
→ issue/archive
→ optional isolated execution
```

### 2. Review / QA / ship / delivery qualification

`review-qa-ship-delivery-qualification.md`

```text
implemented branch
→ merged-code tests + ownership
→ semantic changed-path coverage
→ conditional plan completion
→ optional browser verification
→ fresh pre-landing review
→ specialist/red-team/adversarial challenge
→ fix → re-test → re-review
→ evidence-bearing release / PR
```

Key correction: current qualification can be recomputed; a universal historical `review → QA → ship` ceremony is not required.

### 3. Browser runtime / security / evidence

`browser-runtime-security-evidence.md`

```text
browser contract
→ persistent daemon / BrowserManager / TabSession
→ capability + listener + tab + CDP boundaries
→ external effects
→ browser evidence / audit / activity
→ freshness / ambiguity / trust handling
```

Key correction: own-only tab isolation is contextual and cannot be generalized to all clients/resources.

### 4. Investigation / root-cause / debug control

`investigation-root-cause-debug-control.md`

```text
failure
→ evidence
→ explicit causal hypothesis
→ falsification
   ├─ false → revise / 3-strike escalation
   └─ supported → bounded fix
                  → regression + full suite
                  → fresh original reproduction
                  → durable learning
```

Key correction: causal-before-fix is mainly behavioral contract; `root cause` does not guarantee systemic prevention/detection depth.

### 5. Memory / learnings / context / GBrain

`memory-learnings-context-gbrain.md`

```text
prior information
→ provenance / confidence / branch / TTL / scope / type
→ trust + privacy + ingest policy
→ consumer-specific retrieval / budget
→ current context
```

Key correction: cache knows when it serves `stale-fallback`, but planning preflight suppresses that status and can expose stale content without a stale label.

### 6. Multi-agent / cross-model coordination

`multi-agent-cross-model-coordination.md`

```text
parent work state
→ dispatch / role selection
→ context included or withheld
→ authority + resource scope
→ foreground / parallel / remote execution semantics
→ child result contract
→ validation / dedupe / consensus
→ timeout / partial-failure / cancellation policy
→ parent continuation
```

Key results:

- fresh-context specialization ≠ outside-model diversity ≠ independent verification;
- v1.79's stranded-parent recurrence demonstrates that liveness semantics must be explicit interface state, not runtime-default assumption;
- `/ship` → `/document-release` uses a spawned-session child with narrowed authority, machine-readable JSON result, parent validation and shared-working-tree recovery;
- fresh context does not imply filesystem/worktree isolation;
- Review Army and Design Shotgun both fan out Agents but one is primarily verification/coverage while the other expands the candidate space;
- Autoplan deliberately gives Claude and Codex different context roles;
- nested Codex under Codex is suppressed because same-model self-review is not the intended diversity;
- multi-agent failure polarity is work-criticality specific;
- global foreground protection is strongly structural but runtime enforcement and host-neutral delegation remain incomplete;
- Review Army production topology has weaker behavioral evidence than its checklist/structural contract.

---

## Synthesis ladder

```text
Level 0  pinned source
   ↓
Level 1  source-grounded mechanism records
   ↓
Level 2  semantic subsystem syntheses
   ↓
Level 3  cross-system synthesis
   ↓
Level 4  four-ground projection + neutral cross-ground mechanisms
   ↓
Level 5  compact gstack core model
```

Higher synthesis never removes source re-entry.

---

## Provisional subsystem map

1. governing ethos / behavioral policy / skill-generation contract;
2. **planning / specification / work admission — done**;
3. **review / QA / delivery qualification — done**;
4. **browser runtime / security / evidence — done**;
5. **investigation / root-cause / debug control — done**;
6. **memory / learnings / context / GBrain — done**;
7. **multi-agent / cross-model coordination — done**;
8. **guarded-action / CSO security-review mechanisms — NEXT**;
9. host adapters / portability fidelity;
10. deploy / canary / production observation / retrospective feedback;
11. testing / eval / routing / compliance infrastructure;
12. repository self-development / generation / update / release mechanisms.

These are research clusters, not Foundation categories.

---

## Immediate next route

Study **guarded-action / CSO security-review mechanisms beyond browser/freeze**.

Central question:

> outside the already-synthesized browser security and investigate freeze controls, how does gstack constrain dangerous action, represent security standing, verify candidate vulnerabilities, separate advisory findings from enforced blocks, and decide when uncertainty should deny, degrade, escalate or remain informational?

Primary routes:

- `/cso` scan → candidate → verifier → report/standing;
- `/careful`, `/guard` and mutation/dangerous-operation hooks;
- security confidence and false-positive handling;
- enforced control versus advisory prose;
- persistence/audit/receipts and stale-security-state risks;
- selected host hook loss only where needed for the security-control boundary;
- structural tests versus production-topology behavioral E2Es.

---

## Guardrails

- Understand gstack-native mechanism before four-ground projection.
- Keep intended policy, implementation, structural pins and behavioral evidence distinct.
- Do not treat first-party tests, same-family fan-out or cross-model diversity as independent verification by default.
- Interpret “gate”, “security”, “root cause”, “memory”, “agent”, “parallel”, “independent”, “isolation” and “coverage” from actual control semantics.
- Preserve source/view differences: generated skill vs template, checkpoint vs current source, warm vs stale brain context, child data vs parent instruction.
- Name the isolated resource: fresh context, browser tab, worktree, filesystem, memory or model are different boundaries.
- Do not generalize Claude-host Agent semantics to other hosts; current Codex-host dispatch fidelity has a known gap.
- Do not mutate Foundation from this candidate study.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
