# Records / Persistent Information — Findings Map

**Reading layer:** L1 — topic-level orientation and routing  
**Status:** derived map of the completed Records vertical; not evidence and not a substitute for the integrated or topic syntheses.

## Purpose of this map

Use this file after `KEY.md` when the top-level result is not enough but a full read of the vertical is unnecessary.

Each section answers three questions:

1. What problem did the research expose?
2. What bounded conclusion survived?
3. Where should a deeper read continue?

---

## 1. What is the persistent thing?

### Problem

A file, row, copy, document, record, version, representation, derived output, and aggregate are easy to collapse into one storage object.

### Bounded result

They are not reliably the same thing.

The research keeps separate, when relevant:

- broader resource/information identity;
- record role/status;
- version/revision identity;
- representation/instantiation/copy;
- derived resource;
- aggregation/set/contextual grouping.

`Record` is narrower than `anything persisted`; recordhood depends partly on context/function rather than file shape alone.

Unqualified `artifact` was rejected as the foundational super-category because its meaning changes sharply across domains.

### Go deeper

- `synthesis/OBJECT-BOUNDARIES.md`
- `FOUNDATIONAL-SYNTHESIS.md`
- `synthesis/ARTIFACT-COUNTERCHECK.md`
- `sources/object-boundaries-recordhood.md`

---

## 2. What must survive with persistent information?

### Problem

Preserving bytes does not guarantee that future users can identify, interpret, trust, relate, or find the intended information.

### Bounded result

There is no universal object-local metadata bundle.

The stronger idea is a purpose-relative **preservation closure**: all load-bearing information and dependencies needed for a stated future use must remain reliably knowable/recoverable.

Recurring obligation families include:

- exact identity/binding;
- interpretation/representation information;
- provenance/context;
- history/standing where change matters;
- integrity/continuity assurance;
- relations/aggregation/derivation;
- rights/use constraints;
- organisation/retrieval;
- transfer/dependency survivability;
- preservation objectives/significant properties where transformations matter.

Required information may be embedded, linked, inherited, relational, or reconstructable. Location is separate from requirement.

### Go deeper

- `synthesis/MINIMUM-ENVELOPE.md`
- `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md`
- `sources/minimum-envelope.md`
- `sources/digital-preservation.md`

---

## 3. How does persistent information change through time?

### Problem

A generic `update` destroys distinctions between materially different changes.

### Bounded result

Revision, migration, derivation, supersession, correction, retraction/reliance withdrawal, removal, transfer, and destruction can have different effects on identity, standing, availability, and history.

There is also no safe universal single `status` or single `timestamp` model.

Two temporal perspectives can be independently important:

- when something applies/effectively holds;
- when the managing system learned/recorded it.

The target is reconstructability of the required present and historical views, not maximal history for every resource.

### Go deeper

- `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md`
- `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md`
- `sources/change-status-temporal-semantics.md`
- `sources/provenance-identity-time-versioning.md`

---

## 4. How should persistent information be organised?

### Problem

A single folder tree, taxonomy, or hierarchy can silently mix several different purposes.

### Bounded result

At least three functions can diverge:

- organisation that preserves origin/context/relations;
- descriptive or knowledge organisation for meaning/navigation;
- access organisation optimised for finding/filtering/ranking.

Several organisations may coexist over the same underlying resources. Multiple views do not automatically imply multiple source resources.

The semantic role of the relation matters more than forcing one master hierarchy.

### Go deeper

- `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md`
- `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md`
- `sources/organisation-retrieval-semantics.md`
- `sources/organization-retrieval-lifecycle.md`

---

## 5. What does it mean to find information again?

### Problem

`Search worked` is too weak a statement. Different questions require different retrieval guarantees.

### Bounded result

Exact known-item lookup, structured filtering, topical discovery, exhaustive/high-recall search, current-standing lookup, historical/as-of lookup, provenance traversal, and aggregate reconstruction are different retrieval needs.

A search hit does not automatically prove exact identity, current standing, authority, completeness, or truth.

A miss supports absence only to the degree that corpus coverage, matching sensitivity, aliases, permissions, freshness, and temporal scope justify it.

Derived views/indexes may be stale or selective without being wrong; the failure occurs when their actual coverage/freshness does not support the claim being made.

### Go deeper

- `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md`
- `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md`
- `synthesis/FAILURE-MODES.md`
- `sources/organisation-retrieval-semantics.md`

---

## 6. Do all persistent resources need the same requirements?

### Problem

Turning every discovered Records distinction into a universal checklist would over-preserve some resources and under-specify others.

### Bounded result

Requirements should be derived from context and re-evaluated when that context changes.

Important inputs include:

- the exact resource/population being considered;
- intended future use;
- retrieval/reconstruction needs;
- horizon/environmental change;
- consequence/risk;
- external legal/policy/security/privacy/archival constraints;
- version/change behavior;
- transformation/transfer exposure;
- dependencies/aggregation;
- target users and assumed knowledge.

For each obligation, keep separate:

- whether it is required;
- how strong/deep it must be;
- how/where it is satisfied;
- how sufficiency is tested.

`Unknown` is different from `not required`.

### Go deeper

- `synthesis/REQUIREMENT-PROFILE-DERIVATION.md`
- `synthesis/REQUIREMENT-PROFILE-COUNTERCHECK.md`
- `sources/requirement-profile-derivation.md`

---

## 7. Which storage/history/search pattern is the right one?

### Problem

Technology labels invite false conclusions such as `versioned = history solved` or `graph = provenance solved`.

### Bounded result

No reviewed mechanism pattern natively supplies all Records obligations.

Different patterns make different capabilities natural: current state, system-time history, typed event history, object-version recovery, content/snapshot lineage, preservation rebuildability, relationship traversal, or discovery.

A concrete system may combine several of these patterns in one physical technology or across several technologies.

The correct evaluation order is:

> derive the Records requirements first, then judge mechanisms against them.

### Go deeper

- `synthesis/MECHANISM-PATTERN-LANDSCAPE.md`
- `synthesis/MECHANISM-PATTERN-COUNTERCHECK.md`
- `sources/mechanism-pattern-landscape.md`

---

## 8. When should persistence end or custody change?

### Problem

`Keep forever` and `delete after N years` are both inadequate universal rules.

### Bounded result

Retention/disposition is a first-order Records problem.

A governed termination/custody transition can depend on:

- which record population the rule applies to;
- which rule/version applies;
- the event/condition that starts eligibility;
- retention/transfer conditions;
- holds/freezes/exceptions;
- the intended final action;
- evidence that the action actually occurred;
- what residual identity/history is still required.

Being due for disposition is not the same as having been destroyed. Transfer is not destruction. Hiding/removal is not necessarily irreversible deletion. Residual destruction evidence can have its own later retention needs.

### Go deeper

- `synthesis/RETENTION-DISPOSITION-SEMANTICS.md`
- `synthesis/RETENTION-DISPOSITION-COUNTERCHECK.md`
- `sources/retention-disposition.md`

---

## 9. What failures should later designs be tested against?

### Problem

Positive descriptions can sound complete while missing predictable failure surfaces.

### Bounded result

The vertical maintains a failure inventory covering loss, unreadability, identity drift, silent overwrite, temporal confusion, provenance loss, false trust, stale/partial retrieval, rights failures, over/under-retention, and storage-first modeling errors.

The inventory is not a universal checklist. A concrete profile should select the failure classes relevant to its stated use and risk.

### Go deeper

- `synthesis/FAILURE-MODES.md`
- relevant topic synthesis for the failure being tested

---

## 10. Why did the vertical stop?

### Problem

Foundational research can expand indefinitely unless a stop condition distinguishes missing dimensions from refinements and implementation details.

### Bounded result

A dedicated omission review found retention/disposition to be the only clear missing first-order Records dimension at the current foundation level, and that dimension then received a focused pass.

Remaining issues currently fall into:

- bounded conceptual refinements;
- profile-specific decisions;
- implementation assurance;
- matters outside this vertical.

The vertical remains reopenable if a later counterexample exposes a genuinely new Records problem that the current model cannot represent.

### Go deeper

- `synthesis/VERTICAL-COMPLETENESS-COUNTERCHECK.md`
- `sources/vertical-completeness-omission-review.md`
- `OPEN-QUESTIONS.md`
- `STATE.md`

---

# Integrated deepening route

If the question spans several sections above rather than one topic, read:

1. `synthesis/RECORDS-VERTICAL-SYNTHESIS.md`
2. then the relevant topic synthesis/syntheses;
3. then their counter-checks;
4. then the pass-specific source ledger;
5. then the primary source for exact/load-bearing claims.

`INDEX.md` is the authoritative routing table for those paths.

## Epistemic warning

This map is a selective view. Its job is to help a reader decide **where to descend**, not to remove the need to descend when a consequential question depends on nuance, caveat, source scope, or a counterexample.