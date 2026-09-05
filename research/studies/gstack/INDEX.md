# gstack Study — INDEX

## Role

Retrieval router for the durable `garrytan/gstack` external-target study.

Read `STATE.md` first for current progress and authorization. Read `META.md` for the epistemic boundary and pinned target snapshot.

## Current study target

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`

Observed 2026-09-05; package version 1.79.0.

## Read routes

| Need | Read first | Then |
|---|---|---|
| Current study progress / next work | `STATE.md` | relevant source ledger / synthesis |
| Scope, authority, freshness | `META.md` | `METHOD.md` |
| Why research is structured this way | `METHOD.md` | `inventory/STRUCTURE.md` |
| What has actually been read | `SOURCE-LEDGER.md` | pinned upstream source |
| Repository/system decomposition | `inventory/STRUCTURE.md` | subsystem syntheses |
| Discovery → planning → specification → work admission | `syntheses/planning-specification-work-admission.md` | ledger → pinned sources |
| Implementation → review/QA → ship qualification | `syntheses/review-qa-ship-delivery-qualification.md` | ledger → pinned sources |
| Browser runtime / security / evidence semantics | `syntheses/browser-runtime-security-evidence.md` | ledger → pinned runtime/test sources |
| Failure → hypothesis → fix → verification / causal control | `syntheses/investigation-root-cause-debug-control.md` | ledger → investigate/freeze/learning sources |
| Memory / learnings / context / GBrain | not yet synthesized | **current next cluster** |
| Final four-ground view | not yet produced | only after gstack-native model is sufficiently stable |
| Cross-ground mechanisms | not yet produced | remain neutral until later Foundation comparison |

## Current durable syntheses

### 1. Planning / specification / work admission

`planning-specification-work-admission.md`

```text
idea / intent
  → discovery + premise/alternative qualification
  → approved durable design
  → scope / engineering review
  → executable specification
  → safety / quality / sink gates
  → issue + archive
  → optional isolated execution
```

Key themes: qualification before admission, explicit authority, durable plan/design artifacts as later control inputs, composed/generated skill behavior.

### 2. Review / QA / ship / delivery qualification

`review-qa-ship-delivery-qualification.md`

```text
implemented branch
  → merged-code tests + failure ownership
  → semantic changed-path coverage
  → conditional plan completion
  → optional plan-driven browser verification
  → fresh pre-landing review
  → specialist / red-team / adversarial challenge
  → fix → re-test → re-review
  → evidence-bearing PR/release artifacts
```

Key correction: gstack does not require a universal historical `review → QA → ship` ceremony. Current qualification can be recomputed at ship time.

### 3. Browser runtime / security / evidence

`browser-runtime-security-evidence.md`

```text
skill/browser contract
  → CLI + persistent daemon
  → BrowserManager + per-tab state
  → Chromium / persistent context
  → capability/isolation/security boundaries
  → observed effects
  → evidence / audit / activity
  → freshness / ambiguity / trust handling
```

Key corrections: own-only tab isolation is contextual; command READ/WRITE labels are not security capabilities; local/tunnel surfaces are structurally separated; CDP is deny-default; headless cross-restart persistence is opt-in; security controls have heterogeneous failure polarity.

### 4. Investigation / root-cause / debug control

`investigation-root-cause-debug-control.md`

```text
failure observation
  → evidence acquisition
  → explicit causal hypothesis
  → falsification
      ├─ false → revise / 3-strike escalation
      └─ supported
          → bounded intervention
          → regression test
          → full suite
          → fresh original-symptom reproduction
          → durable investigation learning
```

Key corrections:

- the “no fix before root cause” rule is a strong behavioral contract, not a machine-readable causal-state gate;
- Claude-host Edit/Write freeze has real deny/fail-closed enforcement, but Bash is outside it;
- freeze enforcement is host-specific: common external-host frontmatter strips hooks and OpenClaw's adaptation omits Scope Lock;
- `/investigate` does not automatically clear its freeze state;
- “root cause” can mean the first confirmed local causal mechanism; the workflow does not mandate separate prevention/detection/systemic-cause analysis;
- investigate's causal methodology has only the generic structural coverage floor, unlike the more strongly tested freeze submechanism.

## Planned synthesis ladder

```text
Level 0  pinned gstack source
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

This is a synthesis hierarchy, not an evidence hierarchy: higher levels never replace the ability to descend to pinned source.

## Provisional subsystem map

1. governing ethos / behavioral policy / skill-generation contract;
2. **planning / specification / work admission — bounded synthesis exists**;
3. **review / QA / delivery qualification — bounded synthesis exists**;
4. **browser runtime / security / evidence — bounded synthesis exists**;
5. **investigation / root-cause / debug control — bounded synthesis exists**;
6. **memory / learnings / context / GBrain — NEXT**;
7. multi-agent / cross-model coordination;
8. guarded-action / CSO security-review mechanisms beyond browser/freeze;
9. host adapters / portability fidelity;
10. deploy / canary / production observation / retrospective feedback;
11. testing / eval / routing / compliance infrastructure;
12. repository self-development / generation / update / release mechanisms.

These are research clusters, not Foundation categories.

## Immediate next route

Study **memory / learnings / context / GBrain**.

The central question is not just storage. It is:

> how does gstack create, classify, retrieve, decay, trust, invalidate, scope and reuse prior informational state so earlier work improves later work without silently becoming stale or contaminated authority?

This is now a direct dependency because planning and investigate already consume prior decisions/learnings, and investigate writes verified causal lessons back for future sessions.

## Guardrails

- Understand a source in gstack-native terms before four-ground projection.
- Do not treat prompt/template text as proof of executed behavior.
- Keep intended policy, implementation, structural pins and behavioral evidence distinct.
- Do not treat first-party tests as independent verification.
- Do not equate cross-model diversity with verification independence.
- Keep promotion/retention behavior separate from evidence about system quality.
- Interpret “gate”, “required”, “always-on”, “security”, “root cause” and “coverage” from actual control semantics.
- Do not generalize pair-agent tab isolation to shared local browser clients.
- Do not infer default cross-restart persistence from within-daemon browser continuity.
- Do not describe investigate freeze as a filesystem sandbox or universal host capability.
- Treat prior learnings as sourced/fallible informational state, not automatic truth.
- Do not promote candidate patterns into Foundation/SOUL/Development OS merely because gstack implements them.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
