# SOUL Foundations Research

## Purpose

This package preserves first-principles research into foundational problem regions that may later inform SOUL and Development OS work.

The repository is a **research library and continuity surface**, not a pre-declared SOUL ontology. Research labels, distinctions, synthesis results and counterexamples are evidence/research outputs; they do not automatically become architecture decisions.

Within the wider `research/` tree, this package has a distinct role: **foundational ground research**. Focused-topic and external-target studies that may pressure-test or later help implement Foundation-derived structure live separately under `research/studies/**`.

For current status and authorization always read:

1. `STATE.md`;
2. `INDEX.md`.

This README is stable orientation, not the sole dynamic authority.

---

## Research progression

### `01_verticals/` — independent discovery research

Completed bounded research corpora:

1. `records-artifacts/` — persistent information / Records;
2. `work/` — Work;
3. `actors/` — Actors;
4. `work-environment/` — Technical Work Environment.

These were intentionally researched as independent questions. They are preserved as deep evidence corpora and were **not assumed to be the final four top-level Foundation grounds**.

### `02_adequacy/` — first top-level adequacy synthesis

The independent studies were compared together and pressure-tested against SOUL/Development OS needs and materially different external traditions.

This stage found two level corrections:

- actual Operating/Domain Reality was missing from the original independent set;
- Records was too narrow for the broader Information/Representation problem.

A reopened hierarchy pass then found that target/domain reality and Work-support conditions should remain distinct but are better aligned as lower roles/branches under one broader Environment-like problem ground rather than as peer top-level grounds.

Accepted working hypothesis from that stage:

```text
Environment / Operating Reality
Information / Representation
Work
Actors / Agency–Participation–Authority

+ typed relations / control / transitions
```

This was explicitly a falsifiable research hypothesis, not architecture or ontology.

### `03_ground-deepening/` — recursive ground/node research

This stage tested and deepened each accepted ground one active hierarchical node at a time.

Core rules included:

- no forced shared layer count across grounds;
- at most one substantive hierarchical node active at a time;
- immediate children discovered before any child research was authorized;
- deepening only where decision-critical evidence justified it;
- leaf status did not mean absence of rich internal concepts;
- systematic cross-ground relation/control composition remained deferred.

Current accepted ground results:

#### Environment / Operating Reality

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
         ↳ Technical Work Environment profile
```

Environment is boundedly complete / accepted for the current Foundation depth.

#### Information / Representation

```text
Information / Representation
    ├─ Informational State / Representational Constitution
    └─ Informational Dynamics / Formation–Transition
         ├─ Formation / Acquisition
         ├─ Derivation / Transformation
         └─ Selection / Exposure

Records / Persistent Information
    ↳ deep persistence specialization/profile across Information
```

Information is boundedly complete / accepted for the current Foundation depth.

The three Dynamics children are accepted bounded immediate problem regions but have not received separate child passes because current evidence did not justify deeper recursion.

#### Work

Work survived a post-Environment/Information coverage/gap audit.

Current status:

```text
Work
    ← boundedly complete / accepted
    ← rich multidimensional internal problem map
    ← no universal immediate-child hierarchy promoted
```

The prior deep Work vertical remains the evidence-bearing corpus.

#### Actors / Agency–Participation–Authority

Actors survived a post-Environment/Information/Work coverage/gap audit and contemporary agentic holdouts.

Current status:

```text
Actors / Agency–Participation–Authority
    ← boundedly complete / accepted
    ← rich relational / multi-anchor internal problem map
    ← no universal immediate-child hierarchy promoted
```

Important naming warning: `Actors` is an umbrella research label, not `active doers only` and not one universal Actor primitive. Non-performing beneficiaries, affected parties, rights holders, principals, recipients and accountability forums can be semantically relevant typed positions.

### `04_top-level-adequacy-rerun/` — post-deepening adequacy test

After all four grounds were accepted, the top-level hypothesis was re-run rather than inherited.

The rerun tested:

- missing fifth-ground candidates;
- wrong-level placement and reduction;
- pairwise and multi-ground boundary pressure;
- materially different external domain holdouts;
- serious rival top-level decompositions.

Current bounded result under user evaluation:

```text
Environment / Operating Reality
Information / Representation
Work
Actors / Agency–Participation–Authority

+ typed relations / control / transitions
```

No fifth peer ground, required merge/split, wrong-level correction or materially stronger rival survived the rerun.

The selected external holdouts included metrology/scientific measurement, emergency management, healthcare/patient safety and governance-heavy AI risk management.

---

## Current Foundation frontier

A critical distinction after the adequacy rerun:

```text
four-ground adequacy                     ← boundedly supported
systematic relation/control composition  ← not yet researched
architecture                             ← not authorised by Foundation research
ontology / data model                    ← not authorised
implementation                           ← not authorised
```

The strongest unresolved Foundation question is now:

> **How do Environment, Information, Work and Actors compose through typed relations, derived standings, controls and transitions without collapsing their local semantics?**

Important pressure already exposed includes:

- goal/outcome/value/criteria directedness;
- Actor ↔ Work participation/obligation/authority;
- capability/access/actionability/effective power;
- observation/referent binding;
- dependency/coordination/support;
- verification/validation/acceptance;
- provenance/attribution/accountability;
- target/effect/causation;
- delegation/access/enforcement/transitive authority;
- feedback/learning/evolution.

These are **deferred research pressures, not an accepted relation taxonomy**.

Current authorization is always controlled by `STATE.md`.

---

## Relationship to candidate studies

Canonical candidate-study library:

`research/studies/`

Discovery surface:

`research/studies/CATALOG.md`

Candidate studies may supply:

- external evidence/counterexamples;
- falsifiers and design pressure;
- concrete mechanisms;
- capability/service/data-source landscape information;
- benchmark/test ideas;
- later implementation references.

They do **not** define the Foundation hierarchy merely by existing in the catalog.

The intended retrieval pattern is:

```text
current Foundation/design question
→ candidate-study catalog
→ selected package META
→ package STATE/INDEX/findings when needed
→ current authoritative external source if freshness is decision-critical
→ present research/design decision
```

Current examples include:

- `ai-knowledge-strategies/`;
- `anthropic-ai-native-sdlc-playbook/`;
- `context-memory-harness-engineering/`;
- `multi-agent-patterns/`;
- `hands-on-large-language-models/`;
- `public-apis/`.

---

## Retrieval model

For current Foundation state:

`STATE.md → INDEX.md → active/current package STATE → KEY → FINDINGS-MAP → synthesis → targeted deep evidence`

For completed ground packages, descend only as far as the current decision requires.

Higher-level surfaces are intentionally compressed. When a decision depends on omitted nuance, source scope or a contested claim, descend rather than filling the gap by assumption.

Historical material under `history/` remains useful for audit/reconstruction but does not override current parent authority.

---

## Epistemic rules

Keep separate:

- bounded Foundation research finding;
- accepted working research hypothesis;
- candidate-study finding;
- cross-ground inference;
- residual/open question;
- deferred relation/composition pressure;
- architecture/design decision;
- implementation state.

Also keep separate:

```text
same-model adversarial review
!= independent verification

exact Git SHA binding
!= substantive truth verification
```

User acceptance closes sequencing/evaluation gates; it does not convert same-model synthesis into independent replication.
