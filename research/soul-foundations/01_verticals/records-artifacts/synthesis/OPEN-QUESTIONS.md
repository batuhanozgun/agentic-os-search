# Records / Artifacts — Open Questions

**Status:** prioritised research queue, not a roadmap beyond this vertical  
**Date:** 2026-09-01

## Priority rule

Questions are ordered by information value: first investigate uncertainties whose answer could materially change the definition, granularity, identity or management model for records. Technology comparison comes later.

## P0 — Frame-changing questions

### Q1. Is `recordness` a type, a role/status, or a family resemblance?

Competing evidence permits at least three frames:

1. records are a distinct kind of persistent representation;
2. information objects become records when captured/maintained in a context for evidential/informational/accountability purposes;
3. `record` is a family of domain-specific types whose shared core is too weak for one universal ontology.

Why decision-critical:
- This changes whether a future system needs a `Record` primitive, a `record status/role`, or multiple record classes.

Needed research:
- archival diplomatics / recordness literature,
- legal/administrative record definitions,
- digital records in dynamic systems,
- information-object/document theory counterexamples.

### Q2. What is the identity of a record across change?

Cases to distinguish:
- typo correction,
- factual correction,
- ordinary revision,
- superseding policy/document,
- format migration,
- lossy/lossless conversion,
- derived summary,
- aggregation/splitting,
- restoration from backup,
- re-signing/re-wrapping,
- changed metadata only.

Why decision-critical:
- Determines whether change creates a new record, a new version of the same logical record, a derived record, or an invalidated/superseded state.

### Q3. What is the correct unit/granularity of a record?

Candidates:
- assertion/claim,
- event,
- message,
- database row/object,
- document/file,
- transaction,
- conversation/thread,
- dataset,
- aggregate/series/collection,
- dynamic information-system state.

Why decision-critical:
- Identity, versioning, provenance, retention, indexing and permissions all depend on granularity.
- Archival sources explicitly allow both item and aggregate concepts and records that are not discrete physical objects.

### Q4. Which information is constitutive of the record and which is external management/context metadata?

Examples:
- author/originator,
- capture time,
- provenance chain,
- relationships,
- fixity evidence,
- access rights,
- retention state,
- search taxonomy,
- representation dependencies.

Why decision-critical:
- Determines portability and what must move together for a record to remain the same/usable.
- OAIS shows that meaning can depend on an external representation-information network.

### Q5. How should current truth and historical truth coexist?

Need to preserve distinctions such as:
- `X was believed/recorded at T`,
- `X was actually valid at T`,
- `X is the current accepted correction`,
- `old X is superseded but historically authentic`.

Why decision-critical:
- A model optimised only for current truth destroys historical evidence; a model optimised only for immutable history can make current operational truth ambiguous.

## P1 — Management-model questions

### Q6. Which trust properties are required by which record types?

Need to operationally distinguish:
- authenticity,
- reliability,
- integrity,
- fixity,
- usability,
- completeness,
- authority/currentness.

Question:
- What evidence/control is actually sufficient for each property under different risk levels?

### Q7. Lifecycle, continuum, or another model?

Compare:
- linear lifecycle (creation/receipt → maintenance/use → disposition),
- records continuum (creation/capture/organisation/pluralisation as overlapping dimensions),
- event/state/version models from computing.

Goal:
- determine whether one lifecycle model can cover dynamic digital records or whether lifecycle should be represented as orthogonal states/events.

### Q8. How should correction, supersession, invalidation, derivation and deletion differ?

Needed:
- exact semantic transition vocabulary,
- rules for retaining prior states,
- current-version resolution,
- audit/provenance effects,
- irreversible deletion/disposition evidence.

### Q9. What is the minimal preservation envelope for different preservation objectives?

Potential objectives:
- reproduce exact bits,
- render equivalent human-visible content,
- preserve semantic data values,
- preserve evidential/authentic record,
- preserve executable/interactive behaviour,
- preserve ability to re-perform/reconstruct an outcome.

OAIS strongly suggests the answer depends on intended future use/community.

### Q10. How should retention/disposition interact with version history and provenance?

Questions:
- Can provenance survive after content is deleted?
- Should tombstones/metadata persist after lawful destruction?
- How do retention rules apply to versions, derivatives, indexes and replicas?
- How is deletion itself recorded without recreating deleted sensitive content?

## P2 — Organisation and retrieval questions

### Q11. What is canonical organisation versus access organisation?

Compare:
- provenance/original-order relationships,
- hierarchical file/series structures,
- subject taxonomies / SKOS,
- graph relationships,
- tags,
- full-text indexes,
- semantic/vector indexes,
- generated summaries.

Goal:
- allow multiple useful access views without multiplying sources of truth.

### Q12. What guarantees should retrieval provide?

Separate:
- exact identifier lookup,
- metadata/filter lookup,
- relationship traversal,
- lexical search,
- semantic similarity,
- ranking/recommendation,
- reconstruction of context/aggregate.

Question:
- How does a retrieval result carry freshness, authority, provenance and confidence back to the source record?

### Q13. How should derived views be invalidated/refreshed?

Examples:
- search indexes,
- embeddings,
- summaries,
- materialized views,
- caches,
- extracted facts.

Failure to solve this creates stale-view/source-fidelity problems.

## P3 — Storage-pattern comparison after semantics mature

### Q14. Which persistence patterns best satisfy which record requirements?

Candidate pattern families already identified:
- mutable current-state database,
- bitemporal/multiversion database,
- immutable/versioned object store,
- content-addressed graph/version control,
- append-only event store + projections,
- document/file repository,
- graph store,
- hybrid canonical store + derived indexes.

Do not compare these as generic `which database is best?`; compare against identity/history/provenance/retrieval/disposition requirements established by P0/P1.

### Q15. What belongs in one store versus separate specialised stores?

Possible separations:
- canonical content,
- metadata/provenance graph,
- event/history log,
- search index,
- vector/semantic index,
- archive/cold storage,
- audit/fixity evidence.

Need to evaluate atomicity, consistency, recovery and source-of-truth risks before choosing separation.

## P4 — Term boundary cleanup

### Q16. Record vs document vs artifact

Current distinctions are useful but insufficiently settled for formal ontology.

### Q17. Record vs knowledge / memory

Need to determine whether `knowledge` and `memory` are later independent problem domains, derived roles over records, or umbrella words that should be avoided in architecture.

### Q18. Evidence as record type or relational role?

A record can become evidence relative to a claim. Determine whether `Evidence` should be modeled as a separate object type or as a typed relationship between source material and a claim/decision.

This question touches later Work/Actor concerns and must stay bounded in the current vertical.

## Current next deepening order

Unless new evidence changes the frame, the next research pass should address:

1. Q1 recordness,
2. Q2 identity across change,
3. Q3 granularity,
4. Q4 intrinsic vs external envelope,
5. Q5 current vs historical truth.

Only after these are materially narrowed should storage technology/pattern evaluation become the main activity.