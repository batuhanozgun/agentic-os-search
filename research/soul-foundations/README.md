# SOUL Foundations Research

## Purpose

This package preserves first-principles research into foundational problem regions that may later inform SOUL and Development OS work.

The repository is a **research library and continuity surface**, not a pre-declared SOUL ontology. Research labels, distinctions, synthesis results and counterexamples are evidence/research outputs; they do not automatically become architecture decisions.

## Research layers

### `01_verticals/` — independent discovery research

Contains four completed, user-evaluated bounded research corpora:

1. `records-artifacts/` — persistent information / Records;
2. `work/` — Work;
3. `actors/` — Actors;
4. `work-environment/` — Technical Work Environment.

These folders preserve the original independent research questions. They are **not assumed to be the final four top-level research grounds**.

### `02_adequacy/` — top-level hierarchy adequacy research

Tests what the independent discovery evidence implies when considered together for SOUL and Development OS.

Its current user-accepted **working research hypothesis** is:

```text
Environment / Operating Reality
    ├─ Operating World / Work Domain
    └─ Work-Support Environment
         └─ Technical Work Environment

Information / Representation State
    └─ Records / Persistent Information

Work
Actors / Agency–Participation–Authority

+ typed relations / control / transitions
```

This is a research-routing hierarchy, not architecture or ontology.

### `03_ground-deepening/` — ground-specific depth planning / later research

This layer plans how to bring each accepted top-level ground to sufficient internal research depth.

Key rule: **do not impose one shared layer count or identical research workflow on all four grounds.**

Environment and Information have known parent-level research gaps. Work and Actors already have broad/deep independent corpora and therefore begin with coverage/gap tests rather than automatic re-research.

Read `03_ground-deepening/STATE.md` and `PLAN.md` for current status and method.

## Level alignment of existing deep corpora

```text
Information / Representation
    └─ Records / Persistent Information          ← existing deep corpus

Environment / Operating Reality
    └─ Work-Support Environment
         └─ Technical Work Environment           ← existing deep corpus

Work                                             ← existing broad/deep corpus
Actors                                           ← existing broad/deep corpus
```

Existing corpora remain stable evidence packages even when later research changes their parent level or role in the research hierarchy.

## Historical material

Superseded research paths and point-in-time handoffs live under `history/`.

Historical material is retained for audit, research-path reconstruction and later falsifier recovery. It is not current project authority merely because a search result finds it directly.

In particular, the earlier broad `Environment` pass is archived as boundary-relative operating-world research because it answered a different question from the intended Technical Work Environment vertical. It remains useful prior evidence for later Environment/Operating World research.

## Retrieval model

For completed independent corpora:

`KEY → FINDINGS-MAP → synthesis → relevant topic finding → completeness/audit or source ledger → primary/authoritative source`

Cross-foundation packages define their own progressive routes in their local `INDEX.md` files.

Higher-level surfaces are intentionally compressed. When a decision depends on omitted nuance, source scope or a contested claim, descend rather than filling the gap by assumption.

## Authority/currentness rule

For current project state, authorization and next responsibility, read:

1. `STATE.md` — sole parent-level dynamic authority;
2. `INDEX.md` — current retrieval router.

Vertical-local `STATE`, `README`, manifests, cross-foundation research outputs and historical handoffs do not override parent authority about what the project should do next.

## Isolation and composition rule

The independent discovery stage deliberately avoided solving cross-ground relations prematurely.

Ground deepening may now acknowledge and record relations needed to define local boundaries, but systematic typed relation/control/composition research remains a later phase unless explicitly authorised.

## Epistemic rule

Keep separate:
- established bounded research finding;
- cross-foundation inference;
- accepted working research hypothesis;
- open question;
- candidate research/design decision;
- accepted architecture decision.

Same-model completeness/omission checks are adversarial self-review, not independent verification.

## Relationship to `research/soul-context/`

`research/soul-context/` remains the bounded context-reconstruction package for SOUL, Development OS and predecessor work. It is not duplicated here. Use its `INDEX.md` when that context becomes relevant.
