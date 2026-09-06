# gstack — Observed Structure and Research Decomposition

## Role

This file is the **orientation inventory** used to discover and route the gstack corpus. It is not the final architecture model and it is not a directory→subsystem mapping.

Primary pinned target:

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`

The study is now boundedly complete. For current conclusions use:

1. `../CORE.md` — compact result;
2. `../INDEX.md` — retrieval router;
3. `../syntheses/cross-system-composition.md` — whole native system;
4. relevant subsystem synthesis;
5. `../SOURCE-LEDGER.md` — source/read provenance;
6. `../revalidation/2026-09-06-v1.80.0.md` — current-main delta through v1.80.

This inventory remains useful for explaining how the source corpus was decomposed without treating repository layout as ontology.

---

## High-level observed system

The completed source pass supports this broad decomposition:

```text
                      gstack
                        │
        ┌───────────────┼────────────────┐
        │               │                │
  behavior/policy   workflow/work     runtime/effects
        │               │                │
        └──────────┬────┴───────┬────────┘
                   │            │
            durable state    verification /
             & artifacts      eval / audit
                   │            │
                   └──────┬─────┘
                          │
                 ship / deploy /
               production feedback
                          │
                          ▼
               learning / self-change
                          │
                          ▼
              generation / setup /
                upgrade / release
```

The final cross-system synthesis sharpens this further: gstack is better modeled as a **federation of partial state machines connected through artifacts, standings, authority/control relations and runtime effects** than as one central workflow engine.

---

## 1. Governing policy / behavior-contract layer

Important source families include:

- `ETHOS.md`;
- `AGENTS.md`;
- `CLAUDE.md`;
- `DESIGN.md`;
- `SKILL.md.tmpl` sources;
- `scripts/resolvers/**`;
- host/model configuration and overlays.

Shared behavioral rules can exist at several strengths:

```text
doctrine / prose
→ generated workflow contract
→ structural invariant
→ runtime enforcement
→ behavioral test / CI consequence
```

Do not infer enforcement strength from the presence of policy text alone.

---

## 2. Workflow / work-system layer

The corpus contains workflow-shaped skills spanning:

### Discovery / planning / design

- `office-hours`;
- CEO / engineering / design / DevEx plan review;
- design consultation;
- `autoplan`;
- `spec`.

### Review / investigation / quality

- `review`;
- `investigate`;
- `qa` / `qa-only`;
- design / DevEx review;
- `cso`.

### Coordination

- `pair-agent`;
- Codex/outside-model surfaces;
- review-army / specialist dispatch;
- worktree/parallel planning surfaces.

### Delivery / production / feedback

- `ship`;
- `land-and-deploy`;
- `canary`;
- `document-release`;
- `retro`;
- `learn`;
- context / GBrain surfaces.

These are source/workflow families, not Foundation categories.

---

## 3. Shared composition / generation layer

Canonical generated behavior is assembled from actual source surfaces including:

- root and per-skill `SKILL.md.tmpl` files;
- `scripts/gen-skill-docs.ts`;
- `scripts/resolvers/index.ts`;
- `scripts/resolvers/sections.ts`;
- `scripts/resolvers/composition.ts`;
- host configurations under `hosts/**`;
- model overlays;
- carved sections / manifests.

Important source-view rule:

```text
generated SKILL.md
!= canonical authoring source
```

Generated output is an executable/inspectable view whose semantics depend on template, resolver, host/model and composition inputs.

---

## 4. Browser / execution runtime

The browser subsystem is material software, not prompt-only tooling:

```text
agent / browser CLI
        ↓
long-lived Bun daemon/server
        ↓
BrowserManager + TabSession
        ↓
Playwright / Chromium / CDP
```

Relevant controls include:

- persistent tabs/profile/session state;
- scoped tokens and tab/domain/capability restrictions;
- URL/path/CDP boundaries;
- reference invalidation;
- audit/activity evidence;
- optional tunnel exposure;
- session persistence/restore.

The stateful runtime makes freshness and ownership part of browser-evidence validity.

---

## 5. Guarded-action / security controls

Actual pinned paths include:

- `careful/SKILL.md.tmpl` + `careful/bin/check-careful.sh`;
- `freeze/SKILL.md.tmpl` + `freeze/bin/check-freeze.sh`;
- `guard/SKILL.md.tmpl`;
- `unfreeze/SKILL.md.tmpl`;
- one-way-door registry and Claude question-preference hook;
- `cso` detective/advisory security workflow.

The study distinguishes:

```text
preventive runtime interposition
!= human decision authority
!= detective security evidence
```

and:

```text
enforcement-point scope
!= protected-effect scope
```

Current-main note: v1.80 repairs a pinned `/freeze` state-root fail-open defect; see the revalidation file. The broader Edit/Write-only boundary and host-portability limits remain.

---

## 6. Durable information / continuity layer

Observed durable/state surfaces include:

- design and specification artifacts;
- review and decision logs;
- context checkpoints;
- local learnings;
- GBrain/cache/policy data;
- browser daemon/session state;
- git/repository state;
- test/eval artifacts;
- security reports;
- deploy/canary/retro histories;
- generation/install/update/release state.

A central final finding is that these representations carry different provenance/freshness/authority semantics; there is no one generic “memory” standing.

---

## 7. Test / eval / compliance layer

The completed synthesis found a first-class verification pipeline including:

- free/static tests;
- Windows-specific execution;
- real-agent E2E;
- Codex/Gemini external-runtime E2E;
- LLM-as-judge evals;
- coverage/touchfile/tier routing;
- paid planner/shard/reconciler infrastructure;
- strict execution census;
- partial/finalized eval artifacts;
- baseline/compare/summary/flake tooling;
- compliance/audit/slop scans.

Protected conclusion:

```text
test exists
!= selected
!= executed
!= intended runtime exercised
!= oracle valid
!= finalized result
!= independent verification
```

The testing/eval cluster is no longer “research pending”; it is synthesized in `../syntheses/testing-eval-routing-compliance-flake-lifecycle.md`.

---

## 8. Host / model portability layer

The pinned repository has a typed host-generation system plus heterogeneous setup/runtime standing.

Key distinction:

```text
registered
< generated
< structurally valid
< installable
< runtime-capable
< behaviorally exercised
< failure-path exercised
< independently validated
```

Host and model are separate axes. Generation/adaptation can preserve, rewrite, suppress, inline, weaken or leave behavior unsupported.

---

## 9. Delivery / production feedback layer

The source exposes distinct operational standings across:

```text
qualified PR
→ merge authority
→ authoritative merged state
→ deployment evidence
→ live verification
→ optional longitudinal canary
→ rollback/recovery action
→ retrospective / later learning
```

The study explicitly preserves:

```text
merge command != merged state
deploy completed != service healthy
revert pushed != production restored
```

---

## 10. Repository self-development / release layer

The repository develops and qualifies itself through:

- source templates/resolvers/runtime code;
- generation;
- setup/materialization;
- user-local render/relink;
- tests/evals;
- update detection;
- manual/background upgrade;
- migrations;
- version/changelog/release gates;
- operational feedback and repeated-failure hardening.

This forms a recursive loop in which failure classes increasingly become reusable helpers, runtime controls, structural pins and behavioral/environment tests.

v1.80 adds further examples around setup capability degradation, installer ownership/provenance and test-environment fidelity.

---

## Final semantic research clusters

The first-pass clusters converged into eleven bounded native subsystem syntheses:

1. planning / specification / work admission;
2. review / QA / delivery qualification;
3. browser runtime / security / evidence;
4. investigation / causal control;
5. memory / learnings / context / GBrain;
6. multi-agent / cross-model coordination;
7. guarded action / security review;
8. host adapters / portability fidelity;
9. deploy / Canary / production / retrospective feedback;
10. testing / eval / routing / compliance / flake lifecycle;
11. repository self-development / generation / upgrade / release.

Chronology/evolution was used horizontally to pressure-test these mechanisms rather than promoted as a twelfth sibling.

---

## Documented vs observed structure warning

Repository documentation is useful evidence about intended architecture but does not override the observed pinned tree or runtime source.

An early example in this study was `docs/PROJECT_STRUCTURE.md` describing a `skill/SKILL.md.tmpl` path while the pinned tree had root `SKILL.md.tmpl`.

Therefore:

```text
repository self-description
!= observed source topology by identity
```

Current docs may later repair such drift; historical mismatch remains evidence about source/view fidelity at the pinned snapshot.

---

## Closure note

This inventory's discovery questions are closed by the durable synthesis package. Do **not** continue researching a cluster merely because an early question is visible here.

Current continuation authority lives in `../STATE.md`. At study closure there is **no active gstack research Work**. Current-main behavior beyond the recorded v1.80 checkpoint requires freshness revalidation rather than automatic continuation.
