# Records / Artifacts — Vertical Research

## Purpose

Research the records / artifacts problem domain independently before using it inside a broader SOUL architecture model.

The starting concern is broader than a database or file format: what information-bearing things persist across time, what makes them identifiable and trustworthy, how they are represented and stored, how they change, how they are organised and related, and how they can be found and recovered later.

## Starting questions

The research begins from questions such as:

- What is a record? What is an artifact? Are these the same category?
- What distinctions exist among data, information, record, document, state, event, fact, claim, evidence, knowledge, memory, and derived view?
- What does persistence mean independently of a particular storage technology?
- How is identity assigned and preserved across changes?
- What should be mutable, immutable, versioned, superseded, corrected, or deleted?
- How are provenance, authorship, lineage, authority, validity, and time represented?
- How is information organised without creating multiple conflicting sources of truth?
- How is information indexed, searched, retrieved, reconstructed, and re-contextualised later?
- What are the relevant failure modes: loss, duplication, staleness, ambiguity, corruption, untraceable derivation, inaccessible storage, retrieval failure, and context distortion?
- Which principles are stable across filesystems, databases, version control, event logs, archives, knowledge systems, and other storage/record paradigms?

These questions are starting probes, not a fixed taxonomy or exhaustive research plan.

## Vertical isolation

This research may discover that records depend on work, actors, authority, or other concepts. Such relations should be captured as deferred relational questions when they matter, but the active research should not turn into Work, Actors, orchestration, or SOUL architecture research.

Isolation is methodological only. It must not assume records are ontologically independent.

## Scope evolution

The terms `records-artifacts` are provisional labels for the research target. If evidence shows that the domain should be split, renamed, expanded, or reframed, the research structure may change explicitly rather than forcing findings into the initial label.

## Output expectation

The eventual output should be a source-grounded research package that distinguishes observations, competing models, trade-offs, failure modes, unresolved questions, and bounded synthesis. It should be usable by later research without requiring old chat history.
