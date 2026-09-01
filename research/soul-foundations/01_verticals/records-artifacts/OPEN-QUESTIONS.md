# Records / Persistent Information — Open Questions

**Status:** prioritised research queue after minimum-preservation-closure pass; not automatic execution authority  
**Date:** 2026-09-01

## What changed

Three bounded Records passes now exist:

1. foundational recordhood / persistent-information pass;
2. object boundaries / recordhood / artifact / identity-change pass;
3. minimum persistent-information / record envelope pass.

The third pass rejected a universal object-local metadata bundle and replaced it with a working **minimum preservation closure** frame:

> the smallest information/context/dependency closure required for a specified future use of a specified resource class at a specified horizon/risk level.

See:

- `synthesis/MINIMUM-ENVELOPE.md`
- `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md`
- `sources/minimum-envelope.md`

The closure model is provisional research synthesis, not a SOUL schema or architecture.

---

# Current working distinctions

Do not collapse:

- higher-level persistent information resource/content identity;
- record role/status;
- representation / instantiation;
- copy / instance;
- version / revision;
- semantic derivation;
- aggregation / set;
- object-local information versus externally linked/inherited/reconstructable context;
- preservation obligation versus metadata field/storage location;
- current status versus historical existence;
- integrity/authenticity versus factual correctness.

`Artifact` remains rejected as an unqualified foundational Records super-category; qualified concepts such as `information artifact` remain possible source/domain terms.

---

# P0 — frame-changing / highest-information next candidates

## Q1. Change / status / temporal lifecycle semantics

How should a persistent-information/Records model distinguish and preserve:

- creation/capture;
- revision/versioning;
- migration/re-instantiation;
- semantic derivation;
- supersession;
- correction;
- retraction/invalidation;
- archival preservation state;
- expiration/disposition/deletion

so that **current truth/status**, **historical truth**, **identity**, **provenance**, and **reconstructability** can coexist rather than being collapsed into generic `update`?

### Why this is now P0

The minimum-closure pass showed temporal/version/status closure is conditional but becomes load-bearing for every evolving/currentness-sensitive resource. Storage and retrieval choices would otherwise silently encode a change model before its semantics are understood.

### Key discriminators

- event/occurrence time vs observation/capture time vs recording/system time;
- content revision vs representation migration;
- authoritative/current status vs historical existence;
- correction vs replacement vs retraction;
- deletion of payload vs preservation of disposition/history metadata;
- status event vs new resource/version;
- inherited/external currentness signals and their historical binding.

### Disconfirming tests

- find cases where proposed statuses/events produce no distinct reconstruction/control outcome and should be merged;
- find evolving-resource cases that cannot be reconstructed with the candidate state/event distinctions;
- ensure archival immutability assumptions do not overfit operational/current-information resources.

---

## Q2. Identity/significant-property thresholds under transformation

When should change create:

- same instance;
- new instance/representation;
- new version/revision;
- new record;
- new derived information resource?

The object-boundaries pass showed no universal file-level rule. The minimum-closure pass added two stronger lenses:

- explicit Preservation Objectives;
- significant / transformational properties that must survive.

### Key question

Can identity-change thresholds be made defensible by asking **which protected properties/functions remain invariant**, rather than classifying changes by file operation alone?

---

## Q3. Profile derivation / minimum-closure calculation

Given:

- intended future use;
- resource class;
- retention horizon;
- risk/control obligations;
- expected transformations;
- target knowledge base/community,

how should the system determine which preservation-closure obligations must be explicit, may be inherited/external, or are unnecessary?

### Why not automatically next

Formalising profiles too early may freeze abstractions before change/status and retrieval research expose their real variation. Keep open and revisit after those semantics mature unless new evidence makes it urgent.

---

## Q4. Broader persistent-information category

What neutral frame should contain important persistent information that is not necessarily a record?

Candidates remain:

- persistent information resource;
- information object;
- information content entity;
- information artifact;
- another frame exposed by research.

The correct answer controls whether the historical `records-artifacts/` package should eventually be renamed.

Do not rename yet merely because unqualified `artifact` was rejected.

---

# P1 — organisation / relations / integrity semantics

## Q5. Aggregation and relation semantics

When does collection/series/order/thread/case context carry information that cannot be reconstructed from isolated items?

How should hierarchy, membership, ordering, provenance, version and derivation relations coexist while preserving exact target/version binding?

---

## Q6. Integrity / authenticity / reliability / correctness

The research has established they are non-substitutable. Remaining Records-side question:

What minimum evidence/metadata/control state is needed by resource class, risk and horizon to distinguish:

- bit-level fixity/integrity;
- identity/authenticity continuity;
- provenance completeness;
- reliability of creation process;
- factual/semantic correctness;
- current validity?

Factual correctness/evidential sufficiency must not be absorbed into Records preservation semantics.

---

## Q7. External dependency survivability

When can required closure safely live in:

- external metadata registry;
- provenance/relation graph;
- aggregate/system governance context;
- shared vocabulary/schema/format registry;
- deterministic reconstruction rule?

Need operational criteria for:

- exact binding;
- version locking;
- historical scope/membership;
- dependency availability;
- transfer/materialisation;
- failure recovery.

This remains architecture-neutral: determine semantic safety conditions, not storage topology.

---

# P2 — retrieval / access / preservation operations

## Q8. Canonical resource versus discovery/derived views

How should indexes, caches, summaries, embeddings, catalogues, alternate organisations and search results refer to canonical resources without becoming shadow authorities?

---

## Q9. Retrieval sufficiency

What does `ulaşılabilir olmak` require for materially different retrieval modes?

Distinguish at least:

- known-item lookup;
- attribute/filter retrieval;
- semantic discovery;
- exhaustive/high-recall retrieval;
- temporal/as-of retrieval;
- provenance traversal;
- aggregation reconstruction;
- forensic reconstruction.

The minimum-closure pass established that retrieval is a system-level obligation; it did not define the metadata/index closure for each mode.

---

## Q10. Retention / deletion / disposition semantics

What record-side information must survive expiration, deletion or disposition so removal does not erase necessary history/context?

Need distinguish:

- retention rule/class;
- disposition event;
- destruction confirmation;
- tombstone/reference identity;
- legal hold/exception state;
- payload deletion versus metadata/history retention.

**Boundary:** authority to destroy/retain is deferred to Actors/Work/policy synthesis.

---

# Cross-vertical deferred questions

Continue to use `DEFERRED-RELATIONS.md` for:

- Records ↔ Work production/consumption/change;
- Records ↔ Actors creator/custody/authority;
- Records ↔ Evidence claim-support relation;
- provenance graph ownership;
- rights/disposition authority;
- artifact-as-work-product semantics.

These remain visible but must not redirect Records research into other verticals.

---

# Current next-logical-work note

The highest-information internal Records candidate is **Q1 — Change / status / temporal lifecycle semantics**.

Reason: the first three passes have now clarified `what a record/resource is` and `what information closure must survive`; the next major ambiguity is **how persistent information changes without destroying either current or historical meaning**.

This is a research recommendation only. A new long pass must first re-anchor purpose, scope/exclusions, and operational return condition with the user.