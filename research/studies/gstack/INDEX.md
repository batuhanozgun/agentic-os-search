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
| Browser runtime / security / evidence semantics | `syntheses/browser-runtime-security-evidence.md` | `SOURCE-LEDGER.md`, then pinned runtime/test sources |
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

### `syntheses/browser-runtime-security-evidence.md`

Bounded reconstruction of the browser as an evidence-producing execution environment:

```text
skill/browser contract
  → CLI + long-lived daemon
  → BrowserManager + per-tab TabSession
  → Chromium / persistent context
  → command + snapshot/ref surface
  → token/domain/tab/listener capability boundaries
  → observed browser effects
  → evidence / audit / activity
  → freshness / ambiguity / trust handling
```

Key corrections:

- strict tab isolation applies to own-only pair-agent/tunnel clients, not universally to shared local skill clients;
- browser command read/write labels are not sufficient security classifications — token capabilities reclassify actual side effects;
- local and tunnel surfaces are physically separated by listener topology before normal scoped-token controls;
- raw CDP is deny-default and selected denials are behaviorally exercised against real Chromium;
- headless cross-restart session persistence is opt-in, not implied by ordinary between-call persistence;
- security controls have different failure polarities: some hard-deny, while ML classification, audit and some permission hardening are graceful/best-effort;
- a stale security-status surface with no live measurement source was removed rather than allowed to report false-green protection.

None of the three syntheses is a whole-gstack lifecycle conclusion. Investigation, memory/context, guarded action, production feedback, eval infrastructure and other clusters remain open.

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
4. **browser runtime + security / permission / evidence boundary — bounded synthesis exists**;
5. **investigation / root-cause workflow — NEXT**;
6. memory, learnings, context and GBrain mechanisms;
7. multi-agent / cross-model coordination;
8. guarded-action / CSO security-review mechanisms beyond browser-native controls;
9. host adapters / model-portability layer;
10. deploy, canary, production observation and retrospective feedback;
11. testing / eval / routing / compliance infrastructure;
12. repository self-development, generation and release mechanisms.

The initial cluster map continues changing in response to source evidence: planning + specification merged because their authority/artifact transitions form one mechanism; review/QA/ship formed a delivery-qualification mechanism rather than a simple lifecycle sequence; browser/runtime and browser-native security merged because evidence validity and capability isolation are inseparable in the actual implementation.

These are research clusters, not Foundation categories.

## Immediate next route

Study the **investigation / root-cause workflow** next.

The reason is causal continuity: planning/specification explains how work becomes executable; review/ship explains how implemented work becomes delivery-qualified; browser/runtime explains how external effects and evidence are produced. `/investigate` is the next high-value mechanism for understanding how gstack responds when observed reality contradicts intended behavior — hypothesis formation, reproduction, falsification, scope lock, escalation, regression tests, fresh verification and durable learning.

## Guardrails

- Do not classify source files into Information/Work/Actors/Environment before their gstack-native role is understood.
- Do not treat prompt/template text as proof of executed behavior.
- Keep intended policy, implementation structure, deterministic pins and behavioral E2E evidence distinct.
- Do not treat gstack's own documentation or tests as independent verification of gstack.
- Do not equate cross-model diversity with verification independence without checking shared framing/oracles.
- Keep promotional/retention behavior separate from evidence about work-system quality.
- Treat “gate”, “required”, “always-on”, “security” and “coverage” according to their actual control semantics rather than labels.
- Do not generalize pair-agent/tunnel tab isolation to shared local browser skill clients.
- Do not infer default cross-restart headless browser persistence from within-daemon state continuity.
- Do not promote candidate patterns into Foundation/SOUL/Development OS merely because the external system implements them.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
