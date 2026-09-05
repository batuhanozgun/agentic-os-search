# gstack — Study Metadata

## Identity

- **Study ID:** `gstack`
- **Title:** gstack Software Factory / Agentic SDLC Study
- **Study type:** `external-target`
- **Status:** ACTIVE / IN PROGRESS
- **Research object:** Garry Tan's `garrytan/gstack` repository as an implemented agentic software-development workflow/runtime system

## Primary source snapshot

- **Repository:** `https://github.com/garrytan/gstack`
- **Observed branch:** `main`
- **Pinned research commit:** `0d1bd5616c0ef096bb7ccee336f63c60ee408618`
- **Pinned release context:** package version `1.79.0`; commit title begins `v1.79.0.0 fix: ship subagent dispatches...`
- **Pinned commit timestamp:** 2026-09-01T23:42:11Z
- **Study observation date:** 2026-09-05
- **Freshness risk:** HIGH. The target repository was releasing repeatedly across late August / 1 September 2026 and contains a very large changelog. Load-bearing current-state claims must be revalidated against target HEAD before later reuse.

The pinned commit is the canonical source surface for this study pass. `main` may move during or after the study; unpinned HEAD observations are not interchangeable with the pinned corpus.

## Primary question / purpose

Build a source-grounded model of what gstack actually is and how it works as a software-development operating system / software factory, rather than reducing it to a collection of prompt files.

The study should answer, after gstack-native synthesis is stable:

1. What does gstack do in **Information / Representation**?
2. What does gstack do in **Work**?
3. What does gstack do in **Actors / Agency–Participation–Authority**?
4. What does gstack do in **Environment / Operating Reality**?
5. Which important gstack mechanisms are irreducibly cross-ground, and how does gstack make the four areas work together as one operational system?

The four accepted Foundation grounds are an upper-layer projection and comparison frame, **not a source-bucketing scheme**. Source reading begins from gstack's own concepts, workflows, runtime, artifacts, roles, controls, tests and feedback mechanisms.

## Potential relevance

### Foundation

Strong potential relevance across all four accepted grounds and later composition work. Use only as candidate external evidence, pressure test, falsifier, counterexample, comparator or mechanism example. Do not treat gstack design choices as Foundation truth.

### SOUL

Potentially strong relevance to end-to-end work lifecycle, information/artifact continuity, agent/human roles, authority and approval gates, runtime capability, persistent learning, verification, cross-model challenge, production feedback and system self-improvement.

### Development OS

Potentially strong relevance as an implemented reference system for agentic SDLC orchestration, review/QA/ship workflows, developer-environment tooling, browser/runtime integration, CI/eval, security controls and operational feedback loops.

## Potential reuse modes

- external evidence / real-system pressure test;
- candidate mechanism or pattern;
- failure-mode and boundary counterexample;
- comparison target for later SOUL / Development OS design work;
- source of verification/evaluation patterns;
- source of runtime, capability, authority and information-flow examples.

None of these modes constitutes adoption.

## Epistemic / authority boundary

- This package is a **candidate study**, not Foundation canon and not SOUL / Development OS architecture.
- Research observations describe the pinned external target unless explicitly labelled inference or hypothesis.
- Repository documentation is evidence about intended design, not automatically evidence that runtime behavior matches it.
- Skill/template instructions are behavior contracts or intended orchestration; when a load-bearing claim depends on execution, inspect the relevant runtime/shared code/tests/evals where available.
- Search/retrieval misses are not evidence of absence.
- Derived notes and syntheses do not replace source files; load-bearing claims must remain traceable back to pinned source paths.
- The current SOUL Foundation state is not modified by this study.

## Revisit / revalidation triggers

Revalidate the external target when:

- a later Foundation, SOUL or Development OS decision would rely on a gstack mechanism;
- gstack HEAD has materially advanced beyond the pinned commit;
- a cited workflow/runtime/eval file changed;
- the study is compared against a newer gstack release;
- a finding is promoted from illustrative evidence to load-bearing design input.

## Research method

See `METHOD.md`.

Core discipline:

```text
pinned source
    -> source-grounded leaf notes
    -> semantic subsystem syntheses
    -> cross-system synthesis
    -> four-ground + neutral cross-ground projection
    -> compact core model
```

Evidence provenance remains a graph/backreference structure even when synthesis is hierarchical.

## Entrypoints

- `INDEX.md` — package router
- `STATE.md` — current work state and authorization
- `METHOD.md` — research and synthesis method
- `SOURCE-LEDGER.md` — source coverage / read ledger
- `inventory/STRUCTURE.md` — observed system/repository decomposition

## Related studies

- `../anthropic-ai-native-sdlc-playbook/` — later comparator for agent-native SDLC / operating-model patterns; do not use as the discovery frame for gstack-native modeling.
- `../multi-agent-patterns/` — later comparator for coordination / verification topology.
- `../context-memory-harness-engineering/` — later comparator for context, memory and harness/runtime mechanisms.

## What not to infer

Do **not** infer from this package that:

- gstack is correct, optimal or generally applicable;
- documented behavior is proven runtime behavior;
- every skill is equally important;
- every mechanism belongs cleanly to exactly one Foundation ground;
- Foundation should adopt gstack terminology or architecture;
- the pinned `1.79.0` snapshot represents future gstack HEAD.
