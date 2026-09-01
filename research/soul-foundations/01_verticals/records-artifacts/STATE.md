# Records / Persistent Information — STATE

**Status:** active vertical; change/status/temporal pass return condition met  
**Parent:** `research/soul-foundations/`  
**Last updated:** 2026-09-01  
**User-return gate:** YES

## Current objective

Establish a first-principles, source-grounded understanding of the persistent-information / records problem domain before relating it to Work, Actors, the SOUL Development System, or SOUL architecture.

The package directory remains `records-artifacts/` for continuity. `Artifact` is not treated as an unqualified foundational Records category.

---

# Completed research passes

1. **Foundational Records / persistent-information** — recordhood/problem structure; rejected storage-first framing.
2. **Object boundaries / artifact / identity-change** — separated resource, record role, version, representation, derivation and aggregation; rejected unqualified `artifact` as super-category.
3. **Minimum envelope → minimum preservation closure** — rejected universal object-local metadata bundle; established profile-relative information/dependency closure.
4. **Change / status / temporal semantics** — rejected generic `update`, one universal status enum, and one universal timestamp model; established architecture-neutral reconstructability semantics.

## Pass 4 outputs

- plan: `CHANGE-LIFECYCLE-PLAN.md`
- synthesis: `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md`
- adversarial check: `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md`
- source ledger: `sources/change-status-temporal-semantics.md`

---

# Current bounded result

## Change is multidimensional

Do not collapse:

- creation/generation vs capture/registration;
- revision/version vs representation migration/re-instantiation;
- semantic derivation vs revision;
- supersession vs correction;
- correction vs generic revision/enhancement;
- retraction/reliance withdrawal vs removal/access unavailability;
- removal vs destruction/disposition;
- preservation/custody events vs resource standing/version semantics.

## One universal `status` is not supported

Independent status/standing questions can include:

- production/reproduction state;
- identity/version lineage;
- role/context-scoped currentness/designation/precedence;
- reliance/editorial standing;
- availability/presence;
- preservation/custody history.

These are conditional semantic dimensions, **not mandatory stored fields**. A resource profile may merge dimensions when they cannot vary independently for its protected use.

## Temporal result

One generic timestamp is insufficient when domain-effective standing and system knowledge diverge.

The strongest general distinction is:

- **effective/applicable time** — when a fact/status/relation applies in the governed/modelled domain;
- **system-known/recorded time** — when the managing system learned/recorded/asserted it.

Creation, capture, publication, correction, retraction, migration, transfer, destruction, etc. are normally **typed event occurrence times**, not automatically universal independent temporal axes.

## Terminology correction

The earlier phrase `current truth / historical truth` is retired.

Records semantics preserve:

- current standing/designation;
- historical state/standing;
- system-known historical state when required;
- identity/provenance lineage.

They do **not** establish factual truth or evidential sufficiency.

## Reconstructability result

A current snapshot alone can lose history/transition meaning. A raw event list alone can also be insufficient if event semantics, identity binding, effective time, or currentness rules are not preserved.

The architecture-neutral obligation is:

> preserve enough typed change facts, standing assertions, identity/lineage relations, temporal semantics and provenance bindings to reconstruct the views required by the preservation/reuse profile.

No event-sourcing or temporal-database architecture is implied.

## Disposition boundary

Disposition remains in Records only at the terminal information-history boundary:

- transfer vs disposal/destruction are distinct;
- destruction can make payload irrecoverable while certifiable destruction history/identity remains where required.

Retention schedules, legal holds, authority, approvals and execution workflow remain deferred.

---

# Pass 4 return-condition verdict

**MET.**

- main change kinds compared across independent publishing/versioning, provenance, preservation, temporal-data, archival and records-management sources;
- status vocabulary reduced to semantic dimensions rather than copied as one enum;
- time distinctions tested and bounded;
- identity/provenance effects made explicit;
- current/historical reconstruction requirements explicit;
- disposition kept inside the Records semantic boundary without authority/workflow drift;
- adversarial pass challenged over-separation, source-term collisions, architecture contamination, time overfitting and currentness assumptions;
- source trace and synthesis persisted;
- no storage architecture, Work model, Actors model, authority system or SOUL schema selected.

This is a research-process checkpoint, **not independent proof of a universal lifecycle model** and not completion of the Records vertical.

---

# Current highest-information unknown

The first four passes now establish enough about:

- what persistent objects/records are;
- what information closure must survive;
- how change/status/time must remain semantically reconstructable.

The next major Records gap is now:

> **How should persistent information be organised and retrieved so canonical identity, derived/discovery views, aggregations, version/standing history, and current/as-of retrieval remain distinguishable without stale indexes/summaries becoming shadow authorities?**

See `OPEN-QUESTIONS.md`.

## Next logical work

A bounded **organisation / canonical-vs-derived views / retrieval sufficiency** pass.

## Next authorised work

**RETURN TO USER AND RE-ANCHOR DIRECTION.**

Do not automatically execute another long pass.

Before continuation:

1. restate/re-evaluate purpose and direction;
2. define scope/exclusions;
3. define operational return condition;
4. obtain user approval;
5. then work to that return condition without stopping at the first useful finding.

Work, Actors, cross-vertical synthesis, Development System design, and SOUL architecture remain outside the authorised stage.