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

This is a research-routing frame, not architecture or ontology. Lower hierarchy and parent labels remain challengeable during `03_ground-deepening/`.

### `03_ground-deepening/` — recursive ground/node depth research

This layer brings each accepted top-level ground to sufficient internal research depth **one active hierarchical node at a time**.

Key rules:
- do not impose one shared layer count or identical research workflow on all grounds;
- at most one hierarchical node is researched substantively at a time;
- sibling/other grounds may be consulted only for bounded boundary, counterexample or deferred-relation purposes;
- one node pass discovers only its immediate children;
- discovering a child does not authorize researching that child;
- each closed node returns to user evaluation before any deeper or sibling activation.

## Current stage

### Environment / Operating Reality

`03_ground-deepening/grounds/environment/` is **boundedly complete / user-evaluated** for the current foundation purpose.

Current bounded tree:

```text
Environment / Operating Reality
    ├─ Domain Reality
    │    ├─ Domain State
    │    │    ├─ Domain Structure
    │    │    │    ├─ Constituent Composition
    │    │    │    └─ Relational Organization
    │    │    └─ Domain Condition
    │    │         ├─ Realized Characteristics
    │    │         └─ Criterion-Relative Standing
    │    └─ Domain Dynamics
    └─ Work Conditions
         ↳ Technical Work Environment
```

### Information / Representation State

`03_ground-deepening/grounds/information/` is the **current single active top-level node**, explicitly selected by the user on 2026-09-04 after Environment closure.

Current progress:

```text
N0 internal evidence recovery       ← complete
N1 parent coherence attack          ← provisional pass / complete
N2 first-principles problem map     ← bounded complete / no children accepted
N3 immediate-child clustering       ← CURRENT
```

N1 found a coherent first-order research problem region around mediated informational access/representation and the independent semantics/failures of informational states, transformations and relations. This is not an ontology-primitive decision and the current parent label remains provisional.

N2 exposed twelve problem families and rejected the inherited observation/belief/evidence/context/Records noun list as a hierarchy because it mixes processes, states/results, relations/roles, cross-cutting dimensions and lifecycle conditions.

The prior Records corpus remains deep evidence for persistent-information problems but does not predetermine the Information hierarchy.

For current status and routing read:

1. `STATE.md` — sole parent-level dynamic authority;
2. `INDEX.md` — current retrieval router;
3. `03_ground-deepening/STATE.md` and the active Information package.

## Level alignment of existing deep corpora

```text
Information / Representation                    ← active parent research; provisional label/internal structure
    ? Records / Persistent Information           ← existing deep corpus; position still to be tested

Environment / Operating Reality                 ← boundedly complete
    └─ Work Conditions
         ↳ Technical Work Environment            ← existing deep specialization/profile

Work                                             ← existing broad/deep corpus; inactive
Actors                                           ← existing broad/deep corpus; inactive
```

Existing corpora remain stable evidence packages even when later research changes their parent level or role in the research hierarchy.

## Historical material

Superseded research paths and point-in-time handoffs live under `history/`.

Historical material is retained for audit, research-path reconstruction and later falsifier recovery. It is not current project authority merely because a search result finds it directly.

## Retrieval model

For completed independent corpora:

`KEY → FINDINGS-MAP → synthesis → relevant topic finding → completeness/audit or source ledger → primary/authoritative source`

Cross-foundation and ground-deepening packages define their own progressive routes in local `INDEX.md` files.

Higher-level surfaces are intentionally compressed. When a decision depends on omitted nuance, source scope or a contested claim, descend rather than filling the gap by assumption.

## Authority/currentness rule

For current project state, authorization and next responsibility, read:

1. `STATE.md` — sole parent-level dynamic authority;
2. `INDEX.md` — current retrieval router.

Vertical-local `STATE`, README files, manifests, cross-foundation research outputs and historical handoffs do not override parent authority about what the project should do next.

## Isolation and composition rule

Ground/node deepening may acknowledge and record relations needed to define local boundaries, but systematic typed relation/control/composition research remains a later phase unless explicitly authorised.

## Epistemic rule

Keep separate:
- established bounded research finding;
- cross-foundation inference;
- accepted working research hypothesis;
- open question;
- candidate research/design decision;
- accepted architecture decision.

Same-model completeness/omission checks are adversarial self-review, not independent verification.

## Relationship to other research packages

`research/soul-context/` remains the bounded context-reconstruction package for SOUL, Development OS and predecessor work.

`research/ai-knowledge-strategies/` and `research/context-memory-harness-engineering/` contain later technical research relevant to Information failure surfaces. They are evidence inputs only and explicitly carry no Foundation-tree or architecture authority.
