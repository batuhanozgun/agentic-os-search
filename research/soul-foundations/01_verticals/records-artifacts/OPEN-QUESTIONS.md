# Records / Artifacts — Open Questions

**Status:** prioritised research queue after object-boundaries pass; not automatic execution authority  
**Date:** 2026-09-01

## What changed

The previous P0 questions — natural object model, recordhood threshold, and artifact boundary — received bounded answers in:

- `synthesis/OBJECT-BOUNDARIES.md`
- `synthesis/ARTIFACT-COUNTERCHECK.md`

They are no longer the highest-information unknowns, although the resulting model remains provisional and can be reopened by later evidence.

## Current established working distinctions

Enough evidence now exists to avoid collapsing:

- higher-level persistent information resource/content identity,
- record role/status,
- representation / instantiation,
- copy / instance,
- version / revision,
- semantic derivation,
- aggregation / set.

`Artifact` is not retained as an **unqualified** foundational Records super-category. Qualified concepts such as `information artifact` remain candidates for the unresolved broader persistent-information frame.

---

# P0 — frame-changing / next-pass candidates

## Q1. Minimum persistent information / record envelope

What minimum properties must survive with a persistent information resource so that it can later be:

- identified,
- interpreted,
- contextualised,
- traced to source/derivation,
- placed in time and status,
- checked for integrity where required,
- related to other resources/aggregations,
- found and reconstructed?

Candidate property families exposed so far:

- identity;
- resource/record role or type;
- representation information;
- provenance/source;
- occurrence/context linkage;
- temporal semantics;
- version/change/status;
- integrity/fixity;
- relations/aggregation;
- currentness/authority signal;
- discovery metadata.

**Disconfirming tests:**
- remove a candidate property and construct a case where later use still succeeds without material ambiguity or loss;
- find a property omitted from the list whose absence causes a distinct failure;
- test whether requirements differ qualitatively by persistent-object class or retention horizon.

**Why P0:** storage, organisation, retrieval, and preservation mechanisms cannot be evaluated coherently until we know what must actually survive.

---

## Q2. Broader persistent-information category

What neutral frame should contain important persistent information that is not necessarily a record?

Candidates to compare rather than inherit:

- persistent information resource,
- information object,
- information content entity,
- information artifact,
- record resource (possibly too record-centric),
- another frame exposed by research.

**Key test:** which candidate preserves the object-boundary distinctions without importing Work, physical-object, or domain-specific semantics into the Records vertical?

This question also controls whether `records-artifacts/` should eventually be renamed.

---

## Q3. Identity/significance thresholds

When should a change or transformation produce:

- the same instance,
- a new instance/representation,
- a new version/revision,
- a new record,
- a new derived information resource?

The object-boundaries pass shows there is no universal file-level rule. The unresolved problem is what property/significance criteria make these decisions defensible across classes and horizons.

---

# P1 — property and lifecycle semantics

## Q4. Change/status semantics

Which record-side states/transitions are genuinely distinct rather than one generic `updated` state?

Candidate distinctions:

- draft,
- current,
- authoritative/current-of-record,
- historical,
- superseded,
- corrected,
- retracted/invalidated,
- derived,
- transformed/migrated,
- archived,
- disposed.

**Boundary:** define record-side semantics without deciding which Actor is authorised to assign them.

---

## Q5. Temporal semantics

Which time axes are required across persistent-resource classes?

Candidates:

- occurrence/event time,
- observation time,
- valid time,
- recording/transaction time,
- creation/capture time,
- modification/version time,
- publication time,
- supersession/retraction time,
- freshness/validity horizon.

**Disconfirming test:** if two time axes never produce different answers, reconstruction, or controls in relevant cases, they should not remain separate by terminology alone.

---

## Q6. Aggregation and relation semantics

When does collection/series/order/thread/case context carry information that cannot be reconstructed from item-level metadata?

How should:

- hierarchy,
- membership,
- ordering,
- provenance relations,
- version relations,
- derivation relations

coexist without turning organisation into a second source of truth?

---

## Q7. Integrity / authenticity / reliability / correctness

What must be separately represented or tested to distinguish:

- bit-level fixity/integrity,
- authenticity/identity continuity,
- provenance completeness,
- reliability of creation process,
- factual/semantic correctness,
- current validity?

The foundational research already shows these are non-substitutable; the remaining question is their minimum record-side semantics by class/risk/horizon.

---

# P2 — organisation, retrieval, preservation

## Q8. Canonical resource versus discovery/derived views

How should indexes, caches, summaries, embeddings, catalogues, alternate organisations, and search results refer to persistent resources without becoming silent shadow authorities?

---

## Q9. Retrieval sufficiency

What does `ulaşılabilir olmak` actually require?

Distinguish at least:

- known-item lookup,
- attribute/filter retrieval,
- semantic discovery,
- exhaustive/high-recall retrieval,
- temporal/as-of retrieval,
- provenance traversal,
- aggregation reconstruction,
- forensic reconstruction.

A resource can be preserved yet operationally lost if the required retrieval mode cannot recover it.

---

## Q10. Preservation horizon

Which properties and controls must survive for:

- session-scale,
- project-scale,
- organisational/operational,
- audit/legal,
- archival/long-term

horizons?

Does the model change qualitatively by horizon, or only the strength/quantity of preservation metadata and controls?

---

## Q11. Retention / deletion / disposition

What information must be preserved about deletion, expiration, supersession, or disposition so that removal does not erase necessary history/context?

**Boundary:** Records may define lifecycle semantics; authority to destroy or retain remains deferred to later cross-vertical work.

---

# Deferred relational questions

Cross-vertical questions remain in `DEFERRED-RELATIONS.md`, including:

- Records ↔ Work activity/production/consumption;
- Records ↔ Actors originator/custody/authority;
- Records ↔ Evidence claim-support relation;
- provenance graph ownership;
- retention/disposition authority;
- derived-record creation;
- artifact-as-work-product semantics.

These are visible but must not redirect the current Records research into Work or Actors design.

## Current next-logical-work note

The highest-information candidate is **Q1 — Minimum persistent information / record envelope**.

That is a research recommendation, not execution authority. A new long pass should first re-anchor its purpose, scope, exclusions, and return condition with the user.