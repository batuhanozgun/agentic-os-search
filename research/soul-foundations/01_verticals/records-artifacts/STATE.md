# Records / Artifacts — STATE

**Status:** active vertical — foundational pass complete at user-return gate  
**Parent:** `research/soul-foundations/`  
**Last updated:** 2026-09-01

## Current objective

Establish a first-principles, source-grounded understanding of the records / artifacts problem domain before relating it to Work, Actors, the SOUL Development System, or SOUL architecture.

## Completed pass

The foundational pass asked what a record is, what must persist for later trustworthy use, and which distinctions among data, information, document, record, state, event, claim, evidence, knowledge, memory, and derived representation are load-bearing.

Canonical outputs:

- `RESEARCH-PLAN.md` — question, lenses, counter-frames and return condition.
- `SOURCES.md` — consolidated cross-disciplinary source ledger and limitations.
- `FOUNDATIONAL-SYNTHESIS.md` — main bounded synthesis.
- `OPEN-QUESTIONS.md` — prioritised next internal Records questions.
- `synthesis/CONCEPT-BOUNDARIES.md` — supporting provisional term boundaries.
- `synthesis/FAILURE-MODES.md` — supporting failure inventory.
- `synthesis/RETURN-CONDITION-REVIEW.md` — self-review of the pass return condition.
- `sources/` — subordinate detailed source ledgers by lens.
- `DEFERRED-RELATIONS.md` — cross-vertical observations deliberately not solved here.

The package has been consolidated so there is one main foundational synthesis and one main open-question queue; supporting subdirectories do not maintain competing copies.

## Foundational result

The pass does not support `record = file`, `record = anything persisted`, `preserve bytes = preserve meaning`, `immutable = true/trustworthy`, or `stored = retrievable` as adequate general models.

The strongest bounded synthesis is that recordhood is at least materially contextual/functional rather than a storage format, but the deeper `type vs managed role/status vs family of record types` question remains open. Durable trustworthy reuse can require separable properties including identity, representation/interpretability, context, provenance, temporal semantics, integrity/change trace, authority/status, relations, findability/retrievability and lifecycle/retention.

`record` and `artifact` are not proven to be the same category. `artifact` remains broader/context-dependent in current evidence and requires more targeted boundary work if it stays load-bearing.

## Candidate research dimensions

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

These are research dimensions, not fields, components or SOUL primitives.

## Counter-frames preserved

- Record definitions differ across evidence, information, persistent-representation and contextual/emergent-recordness traditions.
- Linear lifecycle and records-continuum models are both retained as competing lenses.
- Record is not assumed to be a discrete object; aggregate/system-resident/contextual records remain possible.
- Artifact is not assumed synonymous with record.
- Immutability, event sourcing, versioned object storage, graph representation and current-state databases remain alternative mechanisms/patterns, not selected architecture.

## Deferred relations

See `DEFERRED-RELATIONS.md`.

Material relations currently include Records↔Work, Records↔Actors, authority, evidence, provenance ownership and retention/disposition authority. They are recorded but not solved from this vertical.

## Return-condition verdict

**MET for the foundational pass.**

The major competing frames were compared; load-bearing distinctions and failure surfaces are explicit; limiting/counter evidence was sought; source trace is persisted; unresolved questions are concrete and prioritised; no storage technology or SOUL architecture was selected.

This verdict is a research-process checkpoint, **not independent verification of the synthesis** and not completion of the Records / Artifacts vertical.

## Next logical internal research

Use `OPEN-QUESTIONS.md`. Highest-information targets are currently:

1. recordness / natural object model — intrinsic type vs contextual/managed role/status vs family of record types;
2. identity across change;
3. granularity of the natural record unit;
4. intrinsic vs external preservation envelope;
5. coexistence of current truth and historical truth.

## Next authorised work

**RETURN TO USER.**

Further Records research may continue on user direction. Work, Actors, cross-vertical synthesis, Development System design, and SOUL architecture remain outside the current authorised stage. A later continuation can resume from the repository without replaying old chat.