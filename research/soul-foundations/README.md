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

It established and the user accepted the working top-level research frame:

```text
Environment / Operating Reality
Information / Representation State
    └─ Records / Persistent Information
Work
Actors / Agency–Participation–Authority

+ typed relations / control / transitions
```

Its Environment lower hierarchy was intentionally a working hypothesis for deeper research rather than permanent authority.

This is a research-routing frame, not architecture or ontology.

### `03_ground-deepening/` — ground-specific depth research

This layer brings each accepted top-level ground to sufficient internal research depth **one ground at a time**.

Key rules:
- do not impose one shared layer count or identical research workflow on all grounds;
- at most one ground is researched substantively at a time;
- other grounds may be consulted only for bounded boundary/counterexample/relation purposes;
- each ground receives its own closure and user evaluation.

The first substantive package is:
- `03_ground-deepening/grounds/environment/`

Its bounded current research result refines the Environment lower structure to:

```text
Environment / Operating Reality
    ├─ Domain / Effect Reality
    └─ Work Conditions / Enabling–Constraining Environment
         └─ Technical Work Environment
```

The older `Work-Support Environment` phrase was broadened because realized conditions can constrain, degrade, block or endanger Work as well as positively support it.

Read package-local `STATE.md` / `INDEX.md` surfaces for epistemic/current status. Parent `STATE.md` remains the sole authority for what happens next.

## Level alignment of existing deep corpora

```text
Information / Representation
    └─ Records / Persistent Information          ← existing deep corpus

Environment / Operating Reality
    └─ Work Conditions / Enabling–Constraining Environment
         └─ Technical Work Environment           ← existing deep corpus

Work                                             ← existing broad/deep corpus
Actors                                           ← existing broad/deep corpus
```

Existing corpora remain stable evidence packages even when later research changes their parent level or role in the research hierarchy.

## Historical material

Superseded research paths and point-in-time handoffs live under `history/`.

Historical material is retained for audit, research-path reconstruction and later falsifier recovery. It is not current project authority merely because a search result finds it directly.

In particular, the earlier broad `Environment` pass is archived as boundary-relative operating-world research because it answered a different question from the intended Technical Work Environment vertical. It remains useful prior evidence for current/later Environment research but does not override the current `03` Environment package.

## Retrieval model

For completed independent corpora:

`KEY → FINDINGS-MAP → synthesis → relevant topic finding → completeness/audit or source ledger → primary/authoritative source`

Cross-foundation and ground-deepening packages define their own progressive routes in local `INDEX.md` files.

Higher-level surfaces are intentionally compressed. When a decision depends on omitted nuance, source scope or a contested claim, descend rather than filling the gap by assumption.

## Authority/currentness rule

For current project state, authorization and next responsibility, read:

1. `STATE.md` — sole parent-level dynamic authority;
2. `INDEX.md` — current retrieval router.

Vertical-local `STATE`, `README`, manifests, cross-foundation research outputs and historical handoffs do not override parent authority about what the project should do next.

## Isolation and composition rule

The independent discovery stage deliberately avoided solving cross-ground relations prematurely.

Ground deepening may acknowledge and record relations needed to define local boundaries, but systematic typed relation/control/composition research remains a later phase unless explicitly authorised.

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