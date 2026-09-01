# Records / Persistent Information — Vertical Research

## Purpose

Research the persistent-information / records problem domain independently before using it inside a broader SOUL architecture model.

The concern is broader than a database or file format: what information-bearing things persist across time, what makes them identifiable/interpretable, what context must survive, how they change, how they are organised/related, and how the correct information/state can be found and reconstructed later.

The directory name `records-artifacts/` is retained for continuity. Current research no longer assumes that unqualified `artifact` is a valid foundational super-category.

## Current status

Four bounded internal passes have reached explicit user-return conditions on 2026-09-01:

1. **Foundational Records pass** — broad problem structure; rejected storage-first framing.
2. **Object-boundaries pass** — separated resource/record/representation/copy/version/derivation/aggregation; tested `artifact` and identity/change cases.
3. **Minimum preservation-closure pass** — rejected one universal object-local metadata bundle; reframed minimum as profile-relative information/dependency closure.
4. **Change/status/temporal pass** — rejected generic `update`, one universal status enum and one universal timestamp; established reconstructability-oriented change semantics.

The Records vertical itself remains open.

## Current canonical reading order

1. `STATE.md` — current vertical state and authorisation boundary.
2. `INDEX.md` — topic/claim retrieval routing.
3. `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` — latest bounded synthesis.
4. `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md` — adverse test of latest frame.
5. `synthesis/MINIMUM-ENVELOPE.md` — minimum preservation-closure basis.
6. `synthesis/OBJECT-BOUNDARIES.md` — recordhood/object-boundary basis.
7. `OPEN-QUESTIONS.md` — current prioritised internal Records queue.
8. `FOUNDATIONAL-SYNTHESIS.md` — original broader foundation when needed.
9. Relevant pass-specific source ledger and its primary sources as routed by `INDEX.md`.

Pass plans:
- `RESEARCH-PLAN.md`
- `OBJECT-BOUNDARIES-PLAN.md`
- `MINIMUM-ENVELOPE-PLAN.md`
- `CHANGE-LIFECYCLE-PLAN.md`

Cross-vertical observations:
- `DEFERRED-RELATIONS.md`.

---

# Current bounded working model

## Object and identity distinctions

Keep separate during further research, without treating them as final SOUL primitives:

- higher-level persistent information resource/content identity;
- record role/status;
- representation/instantiation;
- copy/instance;
- version/revision;
- semantic derivation;
- aggregation/set.

Recordhood remains hybrid/contextual rather than storage-based. Unqualified `artifact` remains rejected as the vertical's super-category; qualified artifact concepts remain source/domain-specific candidates.

## Minimum preservation closure

There is no evidence-supported universal metadata field bundle for every persistent object.

The current working frame is:

> **Minimum preservation closure** = the smallest information, relationship, interpretive-dependency, control and binding closure required for a specified future use of a specified resource class at a specified horizon/risk level.

The closure depends on use, resource class, horizon/environmental change, risk/control obligations, expected transformations, and target knowledge/community.

Required knowledge may be embedded, external, relational, inherited or reconstructable if dependency survival and exact binding remain protected.

## Change / status / temporal result

Evolving persistent information cannot be reduced safely to one generic `update`.

The current bounded model distinguishes semantic effects of:

- creation vs capture;
- revision/version vs representation migration;
- derivation vs revision;
- supersession vs correction;
- correction vs generic revision/enhancement;
- retraction/reliance withdrawal vs removal/access unavailability;
- removal vs terminal destruction/disposition;
- preservation/custody events vs resource standing.

A single universal `status` is also unsupported. Independent questions can concern:

- production/reproduction state;
- version/lineage relations;
- role/context-scoped currentness/designation;
- reliance/editorial standing;
- availability/presence;
- preservation/custody history.

These are semantic dimensions, not required database columns.

For time, the strongest general distinction is between:

- **effective/applicable time** — when a standing/fact/relation applies in the governed domain;
- **system-known/recorded time** — when the managing system learns/records it.

Other named dates are usually typed event times unless a profile needs an independent temporal axis.

The purpose is reconstructability of current/historical standing and lineage, not factual-truth determination.

---

# Anti-collapse rules now supported

- `record` ≠ every stored/persistent thing;
- resource identity ≠ version identity ≠ representation/copy identity;
- representation ≠ semantic derivation;
- preservation obligation ≠ metadata field/storage location;
- currentness/designation ≠ version lineage;
- correction ≠ generic revision;
- supersession ≠ correction;
- retraction ≠ removal ≠ destruction;
- preservation migration ≠ semantic revision by default;
- effective/applicable time ≠ system-known time when they diverge;
- authenticity/integrity/history preservation ≠ factual truth;
- preserved resource ≠ correctly retrievable/currently presented resource.

---

# Current highest-information question

The first four passes now provide enough ground to test the other half of the original Records problem: **organisation and reaching information again**.

Current highest-information question:

> **How should persistent information be organised and retrieved so canonical identity, derived/discovery views, aggregations, version/standing history, and current/as-of retrieval remain distinguishable without stale indexes/summaries becoming shadow authorities?**

This is `next logical work`, not automatic execution authority.

See `OPEN-QUESTIONS.md` for competing residual questions.

## Vertical isolation

Records research may expose relations to Work, Actors, authority or evidence. Material relations are captured in `DEFERRED-RELATIONS.md` but are not solved from this vertical.

No storage topology, database, vector system, Git model, event-sourcing model, temporal schema, agent-memory architecture, Work model, Actor model, Development System design or SOUL architecture has been selected by these passes.

## Scope evolution

The package name remains historical/provisional. If later evidence supports `records`, `persistent-information`, `information-resource`, or another frame, repository structure may change explicitly rather than forcing findings into the initial label.

## Epistemic rule

Research findings are not SOUL architecture decisions. Plans, source ledgers, indexes and syntheses are derived research views; load-bearing exact claims must remain recoverable to primary sources.