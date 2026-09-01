# Records / Artifacts — Open Questions After Foundational Pass

**Status:** prioritised research queue; not an authorised phase transition  
**Date:** 2026-09-01

## Priority rule

Questions are ordered by expected ability to change the internal Records model. This is not a commitment to execute all of them in order. The user-facing return gate has been reached; further work remains inside the same vertical only when explicitly continued.

## P0 — frame-changing

### Q1. Natural object model

Can the observed distinctions be represented with a minimal set such as:

- persistent resource,
- record/status,
- version/state,
- representation/instance,
- aggregation/collection,
- derived view,

or does this collapse important cases?

**Disconfirming test:** construct cases where two proposed categories have no independent failure/management semantics, or where a missing category is repeatedly forced into several others.

### Q2. Recordhood threshold

Is a `record` simply a persistent representation retained in relation to activity/evidence/reference, or should stable identity/context/integrity be constitutive requirements before something qualifies as a record?

**Competing frames:** ISO/NARA activity/evidence framing; InterPARES diplomatics; information-science `information-as-thing`; technical event/state records.

### Q3. Artifact boundary

Does `artifact` name a broader useful category (e.g. produced object that may not be a record), or is it an unnecessary software/research term that should be removed from this vertical?

**Disconfirming test:** find high-value persistent objects that clearly matter to the system but do not satisfy a defensible record definition.

## P1 — property semantics

### Q4. Minimum context / metadata by class and horizon

What minimum identity, representation, provenance, temporal, relation, integrity and discovery metadata is necessary for different persistent-object classes and retention horizons?

**Risk:** too little causes semantic loss; too much creates unbounded maintenance and processing burden.

### Q5. Authority/change semantics

What record-side statuses are genuinely distinct: draft, current, authoritative, historical, superseded, corrected, retracted, invalidated, derived, cached, archived, disposed?

**Boundary:** do not decide which Actor may assign statuses yet.

### Q6. Temporal semantics

Which time axes are needed across record classes: event/occurrence, observation, valid, recording/transaction, modification/version, publication, supersession, freshness horizon?

**Disconfirming test:** if two axes never produce different answers or controls in relevant cases, merge them.

### Q7. Aggregation and relation semantics

When does collection/series/order carry information that cannot be reconstructed from item-level metadata? How should hierarchy, graph relations and provenance coexist?

## P2 — access / retrieval / preservation

### Q8. Canonical source versus discovery views

How should indexes, caches, summaries, embeddings, catalogues and alternate organisations point to canonical records without becoming shadow sources of truth?

### Q9. Retrieval sufficiency

What does it mean to be able to `reach the information again`? Need to distinguish known-item lookup, semantic discovery, exhaustive recall, temporal retrieval, provenance traversal and reconstruction.

### Q10. Preservation horizon

Which properties must survive for session-scale, project-scale, organizational, legal/audit and archival horizons? Does the required model change qualitatively or only in degree?

## Deferred relational questions

These were exposed by the Records research but are not solved here:

- **Records ↔ Work:** which activity/work produced, consumed, changed, verified or superseded a record?
- **Records ↔ Actors:** who/what created, asserted, observed, changed, verified or has custody of a record?
- **Records ↔ Authority:** who may declare a version authoritative, correct/retract it, change retention, or dispose of it?
- **Records ↔ Evidence:** evidence is relational to a claim/decision; the Records vertical can preserve evidence objects and provenance but cannot alone define evidential sufficiency.

These relations should be available to later vertical/synthesis work but must not redirect the current Records research into Work/Actors design.
