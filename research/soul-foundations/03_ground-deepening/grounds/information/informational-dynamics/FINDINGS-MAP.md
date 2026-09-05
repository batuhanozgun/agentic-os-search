# Informational Dynamics / Formation–Transition — Findings Map

**Document role:** CURRENT_L1  
**Status:** boundedly complete / awaiting user evaluation  
**Date:** 2026-09-05

## 1. Does Informational Dynamics survive as a coherent node?

Yes, for the current Foundation purpose. It owns information-formation/change/availability transition semantics that cannot be reduced to State, Work, Actors or Environment without losing failure distinctions.

Route: `N1-NODE-COHERENCE-ATTACK.md`.

## 2. What problem families were found?

N2 found eleven families spanning acquisition, encoding, derivation, semantic transformation, aggregation, retrieval/context formation, communication, revision, reconciliation, propagation and persistence transitions.

They are not eleven children.

Route: `N2-FIRST-PRINCIPLES-PROBLEM-INVENTORY.md`.

## 3. What immediate children are currently recommended?

```text
Informational Dynamics / Formation–Transition
    ├─ Informational Formation / Acquisition
    ├─ Informational Derivation / Transformation
    └─ Informational Selection / Exposure
```

Route: `N3-IMMEDIATE-CHILD-DISCOVERY.md`.

## 4. Formation / Acquisition

Protected question:

> How does a phenomenon, source act, signal, assertion or source resource become a newly instantiated informational state?

Key failures:

- biased/partial observation;
- wrong source eligibility;
- sampling/detectability gaps;
- parsing/capture corruption;
- source/procedure/result binding loss;
- observation/assertion/copied-state confusion.

## 5. Derivation / Transformation

Protected question:

> How do existing informational states produce or change another informational state or standing, and what semantic effect occurs?

Key failures:

- invalid inference/computation;
- lossy normalization/translation;
- aggregation/summary distortion;
- identity/version confusion;
- revision/history loss;
- merge/reconciliation error;
- provenance/lineage loss.

## 6. Selection / Exposure

Protected question:

> Which existing informational states become visible/available to a use or consumer, and what omission/coverage/order/freshness failures arise?

Key failures:

- source exists but is not retrieved;
- wrong version/rank dominates;
- selection omits decisive evidence;
- stale context/view is exposed;
- publication/delivery makes the wrong state available;
- retrieval miss is mistaken for absence;
- correction fails to propagate to consumer-visible views.

## 7. Why Selection / Exposure is not just Transformation

Because source information can remain unchanged while the visible working set changes. A faithful transformation of a bad selected set and a bad transformation of a complete selected set require different diagnosis and remedies.

NIST TREC and W3C Web Annotation provide materially different external holdouts for this distinction.

Routes: `N4-BOUNDARY-ANTI-COLLAPSE.md`, `N5-EXTERNAL-CROSS-DOMAIN-FALSIFIERS.md`.

## 8. Why Revision is not a fourth child

Correction, retraction, supersession and standing change are load-bearing, but they mainly specialize state-to-state transformation and often require downstream Selection/Exposure propagation. Their authority semantics can cross Work/Actors/control.

Route: `N6-OMISSION-REDUCTION-RIVAL-AUDIT.md`.

## 9. Why Communication is not a fourth child

Communication can combine:

- re-encoding/translation → Transformation;
- publication/delivery → Selection/Exposure;
- receiver-relative instantiation → Formation;
- sender/receiver authority → Actors;
- channel conditions → Environment.

Thus it is a composite pattern, not a clean universal peer.

## 10. Why Propagation/Synchronization is not a fourth child

A changed source may require recomputation/invalidation (Transformation) and correct downstream visibility/retrieval (Selection/Exposure). Propagation is a cross-branch dependency pattern.

## 11. Where does Records / persistence fit?

Persistence remains a deep specialization/profile across State and all three Dynamics branches:

- capture/write;
- migration/update/revision;
- retrieval/recall;
- retention/disposition and historical reconstruction obligations.

This research does not move Records into the Dynamics child hierarchy.

## 12. Cross-cutting transition dimensions

Retained explicitly:

- trigger/origin;
- input/output cardinality;
- semantic effect;
- identity/version effect;
- standing/applicability/currentness effect;
- visibility/availability effect;
- provenance/lineage;
- time/order;
- determinism/reproducibility;
- reversibility/reconstructability;
- propagation lag/freshness;
- source/consumer/authority relation;
- use-relative relevance.

## 13. Boundary rule

The same operation can touch multiple branches. Classify by protected question and reference frame, not by verb.

Example: external retrieval may be Formation relative to the local system/source boundary and Selection relative to the eligible result universe/current context.

## 14. Label refinement

Recommended current research label:

`Informational Dynamics / Formation–Transition`

Reason: the previous qualifier `Formation–Transformation` under-signals Selection/Exposure and non-content standing/availability transitions.

This recommendation awaits user evaluation.

## 15. Verification status

N5 used materially different external sources/traditions. N6 is same-model adversarial review. No independent second-researcher/model replication has been performed.

## 16. Closure / reopen

N7 closes the node boundedly for user evaluation. Reopen triggers are recorded in `N7-NODE-CLOSURE.md` and `OPEN-QUESTIONS.md`.
