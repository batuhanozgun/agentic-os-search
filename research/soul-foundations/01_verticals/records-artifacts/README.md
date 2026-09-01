# Records / Persistent Information — Vertical Research

## Purpose

Research the persistent-information / Records problem domain independently before using it inside a broader SOUL architecture model.

The concern is broader than a database or file format: what information-bearing things persist across time, what makes them identifiable/interpretable, what context must survive, how they change, how they are organised/related, and how the correct information/state can be found and reconstructed later.

The directory name `records-artifacts/` is retained for continuity. Current research no longer assumes that unqualified `artifact` is a valid foundational super-category.

## Current status

Five bounded internal passes have reached explicit user-return conditions on 2026-09-01:

1. **Foundational Records pass** — broad problem structure; rejected storage-first framing.
2. **Object-boundaries pass** — separated resource/record/representation/copy/version/derivation/aggregation; tested `artifact` and identity/change cases.
3. **Minimum preservation-closure pass** — rejected one universal object-local metadata bundle; reframed minimum as profile-relative information/dependency closure.
4. **Change/status/temporal pass** — rejected generic `update`, one universal status enum and one universal timestamp; established reconstructability-oriented change semantics.
5. **Organisation/derived-view/retrieval pass** — rejected one universal hierarchy and one generic `search`; separated organisation roles, derived/source relations and retrieval contracts.

The Records vertical itself remains open.

## Current canonical reading order

1. `STATE.md` — current vertical state and authorisation boundary.
2. `INDEX.md` — topic/claim retrieval routing.
3. `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` — latest bounded synthesis.
4. `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md` — adverse test of latest frame.
5. `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` — change/standing/time basis.
6. `synthesis/MINIMUM-ENVELOPE.md` — minimum preservation-closure basis.
7. `synthesis/OBJECT-BOUNDARIES.md` — recordhood/object-boundary basis.
8. `OPEN-QUESTIONS.md` — current prioritised internal Records queue.
9. `FOUNDATIONAL-SYNTHESIS.md` — original broader foundation when needed.
10. Relevant pass-specific source ledger and its primary sources as routed by `INDEX.md`.

Pass plans:
- `RESEARCH-PLAN.md`
- `OBJECT-BOUNDARIES-PLAN.md`
- `MINIMUM-ENVELOPE-PLAN.md`
- `CHANGE-LIFECYCLE-PLAN.md`
- `ORGANISATION-RETRIEVAL-PLAN.md`

Cross-vertical observations:
- `DEFERRED-RELATIONS.md`.

---

# Current bounded working model

## Object / preservation / change

Current research keeps separate, where the protected use needs them:

- higher-level persistent information resource/content identity;
- record role/status;
- representation/instantiation;
- copy/instance;
- version/revision;
- semantic derivation;
- aggregation/set;
- minimum preservation closure;
- change/standing/temporal history.

There is no universal metadata bundle, status enum or timestamp model. Requirements are profile-relative and architecture-neutral.

## Organisation / retrieval

Organisation is not one intrinsic master tree.

Current evidence distinguishes semantic roles for:

- context/provenance-preserving organisation;
- descriptive / knowledge organisation;
- access / retrieval organisation;
- exact source/version/standing binding.

These roles may be implemented together when no protected distinction is lost. Multiple organisations are allowed but not required.

`Canonical vs derived` is too binary. Derivation, access function, own recordhood, recordkeeping/designated-source role, exact source/version binding and freshness/coverage are separate dimensions.

Retrieval sufficiency is claim-relative. Known-item lookup, semantic discovery, exhaustive/high-recall retrieval, current-standing retrieval, historical/as-of retrieval, system-known-as-of retrieval, provenance traversal and aggregate reconstruction can require different guarantees.

A hit does not automatically establish exact identity, current standing, completeness, truth or evidential sufficiency. A miss supports absence only when corpus/coverage/matching/freshness/recall are sufficiently bounded.

A derived view may intentionally lag or represent a historical state; the semantic failure is mismatch between its freshness/as-of contract and the claim it is used to answer.

---

# Anti-collapse rules now supported

- `record` ≠ every stored/persistent thing;
- resource identity ≠ version identity ≠ representation/copy identity;
- representation ≠ semantic derivation;
- preservation obligation ≠ metadata field/storage location;
- currentness/designation ≠ version lineage;
- correction ≠ generic revision;
- retraction ≠ removal ≠ destruction;
- effective/applicable time ≠ system-known time when they diverge;
- context organisation ≠ subject taxonomy ≠ access index when their semantics diverge;
- derived access view ≠ automatically non-record;
- retrieval hit ≠ source/standing/truth proof;
- retrieval miss ≠ absence without adequate coverage;
- stale ≠ incorrect unless its as-of/freshness semantics mismatch the use;
- authenticity/integrity/history preservation ≠ factual truth.

---

# Current highest-information question

Five passes have exposed many requirements that are conditional rather than universal.

Current highest-information question:

> **How should a Records model derive the appropriate requirement/profile for a given resource, intended use, retention horizon, risk/control context, expected transformations and retrieval needs — deciding which identity, preservation, history, organisation, retrieval and assurance obligations apply without requiring every possible property or prematurely choosing storage architecture?**

This is `next logical work`, not automatic execution authority.

See `OPEN-QUESTIONS.md` for competing residual questions.

## Vertical isolation

Records research may expose relations to Work, Actors, authority or evidence. Material relations are captured in `DEFERRED-RELATIONS.md` but are not solved from this vertical.

No storage topology, database, vector system, graph database, Git model, event-sourcing model, temporal schema, search/ranking architecture, agent-memory architecture, Work model, Actor model, Development System design or SOUL architecture has been selected by these passes.

## Scope evolution

The package name remains historical/provisional. If later evidence supports `records`, `persistent-information`, `information-resource`, or another frame, repository structure may change explicitly rather than forcing findings into the initial label.

## Epistemic rule

Research findings are not SOUL architecture decisions. Plans, source ledgers, indexes and syntheses are derived research views; load-bearing exact claims must remain recoverable to primary sources.