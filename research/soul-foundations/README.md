# SOUL Foundations Research

## Purpose

This package preserves independent first-principles research into foundational problem regions that may later inform SOUL and Development OS work.

The repository is a **research library and continuity surface**, not a pre-declared SOUL ontology. Research labels, distinctions, synthesis results and counterexamples are evidence/research outputs; they do not automatically become architecture decisions.

## Current independent research corpora

The independent research library contains four completed foundation corpora under `01_verticals/`:

1. `01_verticals/records-artifacts/` — persistent information / Records.
2. `01_verticals/work/` — Work.
3. `01_verticals/actors/` — Actors.
4. `01_verticals/work-environment/` — Technical Work Environment / Teknik Çalışma Ortamı.

These names are research/retrieval labels. A later synthesis may rename, split, combine, nest or dissolve them without contradicting the independent findings they preserve.

## Cross-foundation research layers

Cross-foundation tests and comparative research live outside `01_verticals/` so they do not silently rewrite the independently researched corpora.

- `02_adequacy/` — evaluates whether the independently researched foundation regions provide sufficient and productive top-level analytical/problem grounds for later SOUL and Development OS reasoning, including rival-decomposition and external holdout tests.

Read that package's own `STATE.md` and `INDEX.md` for its current epistemic status and retrieval route.

A cross-foundation result can challenge the level, boundary or relationship among independent corpora without converting the result into architecture or changing the historical research question each vertical answered.

## Historical material

Superseded research paths and point-in-time handoffs live under:

- `history/`

Historical material is retained for audit, research-path reconstruction and later falsifier recovery. It is not current project authority merely because a search result finds it directly.

In particular, the earlier broad `Environment` pass is archived as boundary-relative **operating-world** research because it answered a different question from the intended Technical Work Environment vertical.

## Retrieval model

Each completed vertical should be recovered progressively rather than by rereading its entire corpus by default:

`KEY → FINDINGS-MAP → synthesis → relevant topic finding → completeness/audit or source ledger → primary/authoritative source`

Cross-foundation packages define their own progressive route in their local `INDEX.md`.

Higher-level surfaces are intentionally compressed. When a decision depends on omitted nuance, source scope or a contested claim, descend rather than filling the gap by assumption.

## Authority/currentness rule

For current project state, authorization and next responsibility, read:

1. `STATE.md` — sole parent-level dynamic authority;
2. `INDEX.md` — current retrieval router.

Vertical-local `STATE`, `README`, manifests, cross-foundation research outputs and historical handoffs do not override parent authority about what the project should do next.

## Vertical isolation rule

Independent foundation research deliberately avoided treating other verticals' conclusions as axioms. Material relations encountered during a vertical were recorded in `DEFERRED-RELATIONS.md` rather than solved prematurely.

Isolation is methodological, not ontological. It does not establish that the original problem regions are truly independent, exhaustive or required to become separate modules/classes.

## Epistemic rule

Keep separate:

- established independent research finding;
- cross-foundation inference;
- working hypothesis;
- open question;
- candidate research/design decision;
- accepted architecture decision.

Same-model completeness/omission checks are adversarial self-review, not independent verification.

## Relationship to `research/soul-context/`

`research/soul-context/` remains the bounded context-reconstruction package for SOUL, Development OS and predecessor work. It is not duplicated here. Use its `INDEX.md` when that context becomes relevant.
