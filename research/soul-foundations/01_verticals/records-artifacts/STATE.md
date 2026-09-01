# Records / Artifacts — STATE

**Status:** active vertical — foundational pass complete at user-return gate  
**Parent:** `research/soul-foundations/`  
**Last updated:** 2026-09-01

## Current objective

Establish a first-principles, source-grounded understanding of the records / artifacts problem domain before relating it to Work, Actors, the SOUL Development System, or SOUL architecture.

## Completed pass

The foundational pass asked what a record is, what must persist for later trustworthy use, and which distinctions among data, information, document, record, state, event, claim, evidence, knowledge, memory, and derived representation are load-bearing.

Outputs:

- `RESEARCH-PLAN.md` — question, lenses, counter-frames and return condition.
- `SOURCES.md` — cross-disciplinary source ledger and limitations.
- `FOUNDATIONAL-SYNTHESIS.md` — bounded synthesis, falsified simplifications, candidate invariant properties and failure surfaces.
- `OPEN-QUESTIONS.md` — prioritised next questions and deferred cross-vertical relations.

## Foundational result

The pass does not support `record = file`, `record = anything persisted`, `preserve bytes = preserve meaning`, `immutable = true/trustworthy`, or `stored = retrievable` as adequate general models.

The strongest bounded synthesis is that recordhood is contextual/functional rather than a storage format, and durable trustworthy reuse can require separable properties including identity, representation/interpretability, context, provenance, temporal semantics, integrity/change trace, authority/status, relations, findability/retrievability and lifecycle/retention.

`record` and `artifact` are not yet proven to be the same category. `artifact` remains under-defined relative to the now-better-grounded record concept.

## Candidate invariant properties for the next Records pass

- identity,
- content/representation,
- interpretability,
- context,
- provenance/lineage,
- time,
- integrity/change trace,
- authority/status,
- findability/retrievability,
- lifecycle/retention,
- relationships/aggregation.

These are research candidates, not fields, components or SOUL primitives.

## Deferred relations

- Records ↔ Work: production/use/change/verification/supersession relations.
- Records ↔ Actors: creation/assertion/observation/custody/change/verification relations.
- Records ↔ Authority: who may establish authoritative/corrected/retracted/disposed status.
- Records ↔ Evidence: record preservation can support evidence, but evidential sufficiency is relational to claims/decisions and is not solved in this vertical.

## Return-condition verdict

**MET for the foundational pass.**

The major competing frames were compared; load-bearing distinctions and failure surfaces are explicit; limiting/counter evidence was sought; source trace is persisted; unresolved questions are concrete and prioritised; no storage technology or SOUL architecture was selected.

This verdict is a research-process checkpoint, **not independent verification of the synthesis** and not completion of the Records / Artifacts vertical.

## Next logical work

Use `OPEN-QUESTIONS.md`, beginning with the natural object model / recordhood threshold / artifact boundary because these can still change the frame for all later Records research.

## Next authorised work

**RETURN TO USER.** Further Records research may continue on user direction. Work, Actors, cross-vertical synthesis, Development System design, and SOUL architecture remain outside the current authorised stage.
