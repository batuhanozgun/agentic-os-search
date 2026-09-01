# Records / Persistent Information — Open Questions

**Status:** prioritised research queue after change/status/temporal pass; not automatic execution authority  
**Date:** 2026-09-01

## What changed

Four bounded Records passes now exist:

1. foundational recordhood / persistent-information;
2. object boundaries / recordhood / artifact / identity-change;
3. minimum envelope → **minimum preservation closure**;
4. change / status / temporal semantics.

Pass 4 rejected generic `update`, one universal status enum, and one universal timestamp model.

Current bounded change model distinguishes:

- resource/version/representation/derivation lineage;
- typed change facts;
- production/reproduction state;
- role/context-scoped currentness/designation;
- reliance/editorial standing;
- availability/presence;
- preservation/custody history;
- effective/applicable time vs system-known/recorded time when they diverge.

These are semantic questions, not mandatory fields/components.

See:

- `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md`
- `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md`
- `sources/change-status-temporal-semantics.md`

---

# P0 — frame-changing / highest-information next candidates

## Q1. Organisation, canonical/derived views, and retrieval sufficiency

How should persistent information be organised and reached again while preserving the distinctions established by the first four passes?

The next pass should jointly investigate:

### Canonical resource vs derived/discovery views

How should:

- indexes;
- catalogues;
- search results;
- caches;
- summaries;
- embeddings/semantic indexes;
- alternate organisational views

refer to canonical resources without becoming stale or shadow sources of truth/standing?

### Retrieval modes

What information/relations are required for materially different retrieval questions:

- known-item lookup;
- attribute/filter lookup;
- semantic discovery;
- exhaustive/high-recall retrieval;
- current-standing retrieval;
- historical/as-of retrieval;
- system-known-as-of retrieval;
- version/derivation/provenance traversal;
- aggregate/case/thread reconstruction?

### Organisation / aggregation / relation semantics

When does hierarchy, membership, order, series, case/thread context or graph relation carry meaning that cannot be reconstructed from isolated records?

### Change propagation

If canonical standing changes through correction, supersession, retraction, removal or other transition, what must happen semantically so derived/indexed views do not continue presenting stale standing as current?

**Why P0:**

The first four passes now define the object, preservation closure, and temporal/status distinctions that retrieval must respect. Continuing to refine object semantics without testing reachability would risk drift away from the original Records objective: information must not merely persist; the right state/identity must be recoverable later.

**Architecture boundary:**

Do not select search engine, vector database, graph database, relational schema, ranking algorithm, embedding model, or storage topology. First define organisation/retrieval semantics and failure conditions.

---

## Q2. Identity / significant-property thresholds under transformation

When does a transformation remain:

- the same representation;
- a new representation/instance;
- a new version/revision;
- a new record;
- a distinct derived information resource?

The evidence now supplies better discriminators:

- preservation/use objective;
- significant/transformational properties;
- resource family vs version vs representation identity;
- revision vs migration vs derivation semantics.

This remains unresolved but can now be tested with organisation/retrieval use cases instead of abstract file operations alone.

---

## Q3. Profile derivation / preservation-closure calculation

Given:

- intended future use;
- resource class;
- retention horizon;
- risk/control obligations;
- expected transformations;
- target knowledge base/community,

how should a Records system determine which preservation obligations must be explicit, may be external/inherited/reconstructable, or are unnecessary?

**Why not yet first:** retrieval/organisation semantics are likely to expose additional profile variation; formalising the profile rule before that evidence may freeze the model too early.

---

## Q4. Neutral umbrella category

What is the best neutral category around/above `record` for persistent information that may not itself be a record?

Candidates remain:

- persistent information resource;
- information object;
- information content entity;
- information artifact;
- another frame exposed by research.

This controls whether the historical `records-artifacts/` package should eventually be renamed.

---

# P1 — remaining Records semantics

## Q5. External dependency survivability

When can required closure safely remain in an external registry, schema/vocabulary, provenance graph, aggregate context, or reconstruction rule?

Need stronger criteria for:

- historical version locking;
- exact binding;
- dependency disappearance;
- transfer/materialisation;
- recovery/fallback.

This may be partially answered by Q1 because retrieval itself depends on external derived/index structures.

## Q6. Integrity / authenticity / reliability / correctness

The distinctions are established, but profile-specific assurance remains unresolved:

- fixity/integrity;
- identity/authenticity continuity;
- provenance completeness;
- creation-process reliability;
- factual correctness;
- current validity/standing.

Records research must continue to avoid absorbing factual truth/evidential sufficiency.

## Q7. Disposition residual identity/history

After authorised payload destruction/removal, what minimum identity/status/history/tombstone evidence should survive for different use/risk profiles?

Pass 4 established only the semantic boundary: destruction can coexist with retained destruction proof/history.

Authority, retention schedules, legal hold and approval workflow remain deferred.

---

# Cross-vertical deferred questions

Continue to use `DEFERRED-RELATIONS.md` for:

- Records ↔ Work production/consumption/change;
- Records ↔ Actors originator/custody/authority;
- evidence/claim sufficiency;
- provenance ownership;
- rights/disposition authority;
- artifact-as-work-product semantics.

Do not solve these from Records alone.

---

# Current next-logical-work note

The highest-information internal Records candidate is now **Q1 — organisation + canonical/derived views + retrieval sufficiency**.

This direction was re-derived from Pass 4 rather than inherited from the previous queue:

- current/historical standing is now semantically explicit;
- stale discovery views are a concrete failure mode;
- aggregation/relations affect reconstruction;
- the original Records objective includes organising and reaching information again.

A new long pass must first re-anchor purpose, scope/exclusions, and operational return condition with the user.