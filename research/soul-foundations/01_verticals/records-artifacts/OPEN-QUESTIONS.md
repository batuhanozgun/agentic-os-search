# Records / Persistent Information — Open Questions

**Status:** prioritised research queue after organisation/retrieval pass; not automatic execution authority  
**Date:** 2026-09-01

## What changed

Five bounded Records passes now exist:

1. foundational recordhood / persistent-information;
2. object boundaries / recordhood / artifact / identity-change;
3. minimum envelope → **minimum preservation closure**;
4. change / status / temporal semantics;
5. organisation / derived views / retrieval semantics.

Pass 5 established that organisation is plural/purpose-relative rather than one canonical hierarchy, and retrieval sufficiency depends on the information need, corpus/coverage, temporal/standing scope, freshness and precision/recall requirements.

See:

- `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md`
- `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md`
- `sources/organisation-retrieval-semantics.md`

---

# P0 — frame-changing / highest-information next candidates

## Q1. Records profile / requirement derivation

The first five passes now expose many requirements that are **conditional rather than universal**.

Given a particular:

- resource / record class;
- intended future use;
- retention horizon;
- risk / consequence / legal-security obligations;
- expected transformations;
- target future knowledge base/community;
- retrieval needs and coverage expectations,

how should a Records model determine which obligations must be preserved and how strongly?

Candidate obligation families already exposed include:

- identity and exact binding;
- representation / interpretability;
- provenance/context;
- temporal/version/standing history;
- integrity/continuity assurance;
- aggregation/relations;
- rights/use constraints;
- organisation/access descriptions;
- retrieval coverage/freshness/recall;
- preservation objective/significant properties.

### Key questions

- Which obligations are baseline for a profile and which are conditional?
- Which semantic dimensions may safely be merged because they cannot vary independently for the protected use?
- Which information may remain external/inherited/reconstructable versus must travel with the resource across boundaries?
- What assurance level is needed for each obligation?
- Can a small number of profile families capture most requirements, or does the evidence require rule-based derivation rather than fixed profiles?

### Why P0 now

Continuing to add semantic dimensions without a derivation rule risks turning the Records research into an unbounded checklist. Conversely, selecting storage/search technology now would silently choose which obligations to support before deciding when they actually apply.

### Disconfirming tests

- construct simple resource/use cases where a proposed profile over-requires semantics with no protected benefit;
- construct high-risk/long-horizon cases where a proposed profile omits a required obligation;
- test whether profile variables are redundant or whether a missing variable changes requirements;
- test whether fixed profiles fail cases that a rule-based derivation handles better, and vice versa.

---

## Q2. Identity / significant-property thresholds under transformation

When does transformation create:

- same instance;
- new representation/instance;
- new version/revision;
- new record;
- distinct derived information resource?

The evidence now supplies stronger discriminators:

- preservation/use objective;
- significant/transformational properties;
- broader resource vs version vs representation identity;
- revision vs migration vs derivation semantics;
- whether downstream retrieval/source binding needs independent identity.

This remains frame-changing but may be easier to resolve after a profile derivation model clarifies which protected properties matter for a given use.

---

## Q3. External dependency survivability / portability

When may preservation closure safely depend on:

- external metadata registries;
- provenance/relation graphs;
- controlled vocabularies/schemas;
- indexes/finding aids;
- aggregate/system context;
- deterministic reconstruction rules?

Need stronger profile-relative criteria for:

- exact binding;
- historical version locking;
- dependency disappearance;
- transfer/materialisation;
- fallback/recovery;
- schema/vocabulary drift;
- access-control dependency.

Pass 5 made this more important because organisation/retrieval relies heavily on derived/external structures.

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

Do not rename merely because unqualified `artifact` was rejected.

---

# P1 — remaining Records semantics / assurance

## Q5. Assurance profile

What level/type of evidence is required by profile to support:

- identity/authenticity continuity;
- bit/representation integrity;
- provenance completeness;
- creation-process reliability;
- standing/currentness;
- access-view freshness/coverage?

Keep distinct from factual correctness and evidential sufficiency.

---

## Q6. Disposition residual identity / discoverability

After authorised payload destruction/removal, what minimum identity/status/history/tombstone or finding-aid information should survive for different profiles?

Questions include:

- should prior identifiers continue to resolve to a destruction/removal state?
- when should existence history remain discoverable?
- what must survive to prove authorised destruction without preserving the payload?

Authority, legal hold, retention schedule and approval workflow remain deferred.

---

## Q7. Derived-resource promotion boundary

When does a summary, query output, finding aid, access collection or projection stop being merely an access view and require independent Records management as a persistent resource/record?

Pass 5 established that derivation, access function and recordhood are independent dimensions. The exact promotion threshold remains use/context dependent and intersects Work semantics, so solve only the Records-side criteria here and defer production/authority questions.

---

# P2 — later mechanism comparison

## Q8. Storage/state pattern comparison

Only after requirement/profile derivation is sufficiently bounded, compare mechanism families against required Records semantics:

- current-state mutable store;
- multiversion store;
- immutable/versioned objects;
- content-addressed object graph;
- event/change history + projections;
- graph relation representation;
- file/document collections + metadata/indexes;
- separate access/search indexes.

This is **not yet authorised next work** and must not become a familiarity-driven technology choice.

---

# Cross-vertical deferred questions

Continue to use `DEFERRED-RELATIONS.md` for:

- Records ↔ Work production/consumption/change;
- Records ↔ Actors originator/custody/authority;
- evidence/claim sufficiency;
- provenance ownership;
- recordkeeping/current-source designation authority;
- rights/disposition authority;
- artifact-as-work-product semantics.

Do not solve these from Records alone.

---

# Current next-logical-work note

The highest-information internal Records candidate is now **Q1 — Records profile / requirement derivation**.

Reason: five passes have established object, preservation, change and retrieval semantics, but most requirements are conditional. Before comparing storage/search mechanisms, the research needs a bounded method for determining **which Records obligations apply to which use/profile**.

A new long pass must first re-anchor purpose, scope/exclusions and operational return condition with the user.