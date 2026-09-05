# gstack — Observed Structure and Research Decomposition

## Scope

This file records the **observed system/repository decomposition** used to route research. It is not a claim that repository directories map one-to-one to conceptual subsystems.

Pinned target: `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`.

## High-level observed system

Current source supports the following first-pass system model:

```text
                    gstack
                      │
          ┌───────────┼────────────┐
          │           │            │
   behavioral     workflow      executable
     policy       contracts       runtime
          │           │            │
          └──────┬────┴─────┬──────┘
                 │          │
             durable     verification /
             state &        eval / audit
             artifacts          │
                 │              │
                 └──────┬───────┘
                        │
                 ship / deploy /
                production feedback
                        │
                        ▼
                 future behavior
```

This is provisional. Its purpose is to stop the study from mistaking a directory list for the system architecture.

## 1. Governing policy / behavior-contract layer

Observed sources include:

- `ETHOS.md`
- `AGENTS.md`
- `CLAUDE.md`
- `DESIGN.md`
- skill templates and their preambles/sections

Important emerging property: gstack appears to propagate shared behavioral principles into many workflow surfaces rather than leaving them only as human-readable repository doctrine.

Research question: **Which policies are advisory language, which become generated skill contract, and which have deterministic/runtime/test enforcement?**

## 2. Workflow skill layer

README/project structure and actual paths expose many role- or workflow-shaped skills. Preliminary families:

### Discovery / planning / design

- office-hours
- CEO / engineering / design / DevEx plan review
- design consultation
- autoplan
- spec

### Review / investigation / quality

- review
- investigate
- QA / QA-only
- design review
- DevEx review
- security/CSO

### Multi-agent / cross-model

- pair-agent
- Codex second-opinion/review surfaces
- benchmark / model comparison

### Shipping / production / learning

- ship
- land-and-deploy
- canary
- document-release
- retro
- learn
- GBrain setup/sync

### Capability / safety controls

- browse
- careful/freeze/guard/unfreeze family (exact snapshot paths still to verify)

These family labels are study navigation aids, not a complete list or a final taxonomy.

## 3. Shared composition / generation layer

Repository instructions indicate that generated skill documents are assembled from canonical templates/shared material. Relevant surfaces include:

- skill doc generation scripts;
- preamble injection;
- reusable sections;
- shared browser helpers;
- shared Codex/cross-model helpers;
- shared orchestration/reference-document helpers.

This layer is load-bearing because repeated policy or handoff behavior may originate here rather than independently in every skill.

## 4. Browser / execution runtime

`ARCHITECTURE.md` describes a material software subsystem rather than prompt-only tooling:

```text
agent / CLI
   ↓
compiled Bun browse client
   ↓ localhost HTTP
long-lived Bun daemon/server
   ↓ CDP
persistent Chromium
```

Key intended properties:

- persistent browser process and state;
- persistent tabs/cookies/login/localStorage;
- fast repeated command path after startup;
- daemon state / lifecycle management;
- local and restricted tunnel surfaces;
- scoped token/security design;
- deterministic capability surface beneath higher-level agent orchestration.

Runtime source/tests must be inspected before claiming every documented property is implemented exactly as described.

## 5. Durable state / information surfaces

Already visible in orientation/office-hours material:

- design documents;
- project-local gstack artifacts;
- developer/builder profile data;
- learnings / GBrain context;
- browser daemon state;
- git/repository state;
- release/documentation artifacts;
- analytics/eureka/session records.

The study will treat these as information/state mechanisms first in gstack-native terms, then later project them onto Foundation Information.

## 6. Eval / test / compliance layer

`package.json` exposes a large first-class eval/test lifecycle:

- free test shards;
- Windows-specific tests;
- paid LLM evals;
- E2E skill tests;
- routing E2E;
- Codex and Gemini E2E variants;
- LLM judge recommendation tests;
- section-loading tests;
- gate vs periodic tiers;
- sharded paid evaluation;
- eval list/compare/summary/flake-rank/watch/select operations;
- compliance audit;
- slop scan/diff.

This suggests behavioral quality is treated as an operational subsystem. The study still needs to determine criteria, oracle quality, coverage, and how failures feed back into changes.

## 7. Host / model portability layer

The repository's current public framing and eval scripts indicate support beyond one agent host/model. This likely requires adapters/detection/generation differences rather than a single universal prompt surface.

Research question: **Which parts are canonical behavior and which are host-specific translations or bounded variants?**

## 8. Self-development / release layer

Repository instructions and package scripts show gstack also contains mechanisms for developing and validating gstack itself:

- generation of skill docs;
- skill checks;
- tests/evals;
- release procedures;
- changelog/evolution history;
- self-dogfooding patterns.

This matters because the system may form a learning/control loop where its own operational failures lead to new contracts/tests/runtime controls.

## Documented vs observed structure warning

`docs/PROJECT_STRUCTURE.md` is useful but not authoritative about every path at the pinned revision. A directly attempted fetch of `skill/SKILL.md.tmpl` returned 404 even though the project-structure document described that path. Therefore:

```text
repository documentation about structure
!= observed pinned tree
```

Use actual contents/tree for path existence and source retrieval.

## Provisional semantic clusters for synthesis

These are the current research clusters, expected to evolve:

1. policy + generated behavior contract;
2. discovery/planning/specification;
3. review/investigation/QA;
4. browser/runtime capability;
5. security/guarded action;
6. durable information/memory/context;
7. multi-agent/cross-model coordination;
8. host/model portability;
9. ship/deploy/production feedback;
10. eval/testing/compliance;
11. self-generation/release/evolution.

The decisive criterion for cluster boundaries is whether the sources jointly explain a coherent mechanism, not whether they live in the same directory.
