# Records / Artifacts — Vertical Research

## Purpose

Research the records / artifacts problem domain independently before using it inside a broader SOUL architecture model.

The concern is broader than a database or file format: what information-bearing things persist across time, what makes them identifiable and trustworthy, how they are represented and stored, how they change, how they are organised and related, and how they can be found and recovered later.

## Current status

The first **foundational pass** reached its explicit user-return condition on 2026-09-01. The Records / Artifacts vertical itself remains open.

The pass established enough source-grounded structure to reject a storage-first framing and to prioritise narrower internal questions about recordness, identity, granularity, change and current-vs-historical truth.

## Canonical research outputs for this pass

Read in this order:

1. `STATE.md` — current vertical state and authorisation boundary.
2. `INDEX.md` — topic/claim routing.
3. `FOUNDATIONAL-SYNTHESIS.md` — main bounded synthesis for the completed pass.
4. `SOURCES.md` — consolidated source ledger and source limitations.
5. `OPEN-QUESTIONS.md` — prioritised internal Records research queue.
6. `synthesis/RETURN-CONDITION-REVIEW.md` — self-review showing why the pass stopped at the user-return gate.

Supporting detail:

- `sources/` — narrower source ledgers grouped by lens; subordinate to `SOURCES.md` and used for claim recovery/deepening.
- `synthesis/CONCEPT-BOUNDARIES.md` — provisional anti-confusion vocabulary.
- `synthesis/FAILURE-MODES.md` — research-derived failure inventory for later model falsification.
- `DEFERRED-RELATIONS.md` — cross-vertical observations deliberately not solved here.
- `RESEARCH-PLAN.md` — the completed pass question, evidence strategy, counter-frames and return condition.

No duplicate foundational synthesis or duplicate open-question source of truth is maintained under `synthesis/`.

## Starting questions

The research began from questions such as:

- What is a record? What is an artifact? Are these the same category?
- What distinctions exist among data, information, record, document, state, event, fact, claim, evidence, knowledge, memory, and derived view?
- What does persistence mean independently of a particular storage technology?
- How is identity assigned and preserved across changes?
- What should be mutable, immutable, versioned, superseded, corrected, or deleted?
- How are provenance, authorship, lineage, authority, validity, and time represented?
- How is information organised without creating multiple conflicting sources of truth?
- How is information indexed, searched, retrieved, reconstructed, and re-contextualised later?
- What failure modes recur across different record/storage paradigms?
- Which principles are stable across filesystems, databases, version control, event logs, archives, knowledge systems, and other storage/record paradigms?

These remain probes, not a fixed taxonomy or exhaustive research plan.

## Bounded findings from the foundational pass

The current evidence supports these anti-collapse rules without fixing a final ontology:

- `record` is not safely equivalent to `stored information`, file, document, row or artifact;
- preserved bits are not the same as preserved meaning or record continuity;
- record identity can differ from version identity, content identity and locator;
- time has multiple semantics; one generic timestamp is insufficient for many record histories;
- provenance, context and relationships can carry record meaning outside the payload;
- organisation for preserving context and organisation for access/search are different functions;
- retention/disposition is part of records management; `keep everything forever` is not a neutral default;
- current-state, multiversion, event-history, immutable-object and graph patterns are alternative mechanisms, not predetermined architecture choices;
- archival theory itself contains competing `recordness` frames, including contextual/emergent views, so a universal `Record` object class is not yet justified.

See `FOUNDATIONAL-SYNTHESIS.md` for evidence-calibrated detail and caveats.

## Vertical isolation

This research may discover that records depend on work, actors, authority, or other concepts. Such relations are captured in `DEFERRED-RELATIONS.md` when material, but the active research does not turn into Work, Actors, orchestration, Development System, or SOUL architecture research.

Isolation is methodological only. It does not assume records are ontologically independent.

## Scope evolution

The terms `records-artifacts` are provisional labels for the research target. If evidence shows that the domain should be split, renamed, expanded, or reframed, the research structure may change explicitly rather than forcing findings into the initial label.

## Epistemic rule

Research findings are not SOUL architecture decisions. `SOURCES.md`, detailed ledgers, indexes and syntheses are derived research views; load-bearing exact claims must remain recoverable to their primary sources.