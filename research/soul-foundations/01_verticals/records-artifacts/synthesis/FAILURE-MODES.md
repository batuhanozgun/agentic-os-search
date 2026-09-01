# Records / Artifacts — Failure Modes

**Status:** research-derived failure inventory; not exhaustive  
**Purpose:** make later record/storage designs falsifiable against concrete ways persistence and retrieval can fail.

## A. Existence / durability failures

### A1. Record loss

The representation is physically/logically deleted, corrupted beyond recovery, or never durably captured.

### A2. Partial persistence

Some components survive but required attachments, metadata, relationships, indexes or representation dependencies do not.

### A3. Replica illusion

Multiple apparent copies share one hidden failure domain, so redundancy is weaker than assumed.

### A4. Undetected corruption

Bits change without usable fixity/integrity evidence.

## B. Interpretation failures

### B1. Format obsolescence

Bytes survive but future software cannot parse/render them.

### B2. Semantic obsolescence

Structure is readable but meanings, units, codes, vocabularies or domain assumptions are lost.

### B3. Dependency loss

The record depends on schemas, software, algorithms, keys, standards, external resources or related objects that disappear.

### B4. Community-knowledge drift

Terms once considered obvious become ambiguous or change meaning; preserved content becomes effectively unintelligible.

## C. Identity failures

### C1. Identity collision

Two distinct logical records/versions receive the same practical identity or are merged by an access layer.

### C2. Identity drift

A stable identifier silently begins to denote a materially different thing without explicit version/supersession semantics.

### C3. Version/content conflation

A content hash or version ID is treated as the continuing logical record identity, making evolution or multiple manifestations semantically incoherent.

### C4. Locator identity

A path/URL/database key is treated as identity even though the object can move or the locator can be reused.

### C5. Granularity mismatch

The system's storage unit (row/file/object) is assumed to be the record unit, causing one conceptual record to fragment or many records to collapse into one.

## D. History / change failures

### D1. Silent overwrite

A correction/update destroys the prior state and its historical/evidential value.

### D2. History without current truth

Every version is preserved but the system cannot reliably determine which is current, valid, superseded, rejected or disputed.

### D3. Correction-as-falsification

Replacing a historically false claim with the later-correct value erases evidence that the old claim existed and may have influenced actions.

### D4. Update semantics collapse

Correction, revision, derivation, annotation, migration, invalidation and supersession are all represented as generic `update`, losing their different meanings.

### D5. Migration break

Format/storage migration preserves readable content but loses identity, provenance, relationships, significant properties or authenticity evidence.

### D6. Version explosion

Unlimited versions are retained without appraisal, compaction or lifecycle rules, degrading cost and retrieval quality.

## E. Temporal failures

### E1. Timestamp ambiguity

A time value exists but it is unclear whether it means occurrence, creation, receipt, capture, update or system-transaction time.

### E2. Retroactive truth loss

The system cannot distinguish `we believed X at time T` from `X was valid at time T` when later corrections arrive.

### E3. Ordering illusion

Clock/order metadata is treated as stronger than the system can actually guarantee, creating false causal or chronological narratives.

## F. Provenance / context failures

### F1. Source gap

The record exists but its origin or evidence chain cannot be established.

### F2. Derivation opacity

A summary, transformation, conversion or generated artifact lacks links to inputs and transformation history.

### F3. Provenance flattening

Complex lineage is reduced to one `source` field, hiding multiple inputs, transformations or observers.

### F4. Provenance-of-provenance blindness

The system stores provenance claims without recording who/what generated or transformed those claims.

### F5. Context stripping

The item is preserved but relationships to related records, function, series, creator context or surrounding structure disappear.

### F6. False contextual merge

Records from different origins/contexts are reorganised into one apparent canonical structure in a way that changes interpretation.

## G. Trust failures

### G1. Checksum overclaim

A matching checksum is interpreted as proof of authenticity, correctness or authority. It only supports fixity of the checked representation.

### G2. Authenticity without reliability

A record is demonstrably genuine but its original content was inaccurate/unreliable; authenticity is mistaken for truth.

### G3. Reliability without provenance

Content appears plausible but its creation process/source cannot be established well enough for the intended risk.

### G4. Uncontrolled transformation

A derived/migrated representation is used as if original/canonical without documented transformation or validation.

## H. Organisation / retrieval failures

### H1. Stored but unfindable

The record persists but lacks identifiers, metadata or indexes sufficient for later discovery.

### H2. Search-result authority substitution

A search hit, summary, embedding result or cached view is treated as the canonical source because it is visible first.

### H3. Stale index/view

Derived access structures lag behind canonical changes and return obsolete or deleted/superseded records.

### H4. Retrieval miss → absence claim

Failure to retrieve is treated as evidence that no record exists despite incomplete index/coverage.

### H5. Retrieval hit → relevance/truth claim

Finding a semantically similar item is treated as proof that it is the intended, current, authorised or authoritative record.

### H6. Taxonomy lock-in

One classification scheme is treated as the intrinsic structure of the records and suppresses alternative contextual relationships or later reclassification.

### H7. Duplicate source of truth

Metadata, summary, index or replica becomes independently editable and silently diverges from the designated canonical source.

## I. Access / rights failures

### I1. Permanently inaccessible record

The record survives but encryption keys, permissions, credentials or rights information needed for legitimate use are lost.

### I2. Excessive access

Persistence outlives the authority/privacy context and exposes records beyond legitimate access.

### I3. Rights metadata loss

Users cannot tell whether preservation, transformation or distribution is permitted.

## J. Lifecycle / disposition failures

### J1. Over-retention

Everything is kept by default, increasing privacy/legal/cost/discovery risk and making meaningful retrieval harder.

### J2. Premature destruction

Records are deleted before evidential, operational, legal or research value ends.

### J3. Vague disposition

Rules such as `delete when no longer needed` delegate record lifecycle to inconsistent local judgment.

### J4. Delete-semantics confusion

Tombstone, hide, logical delete, version deletion and irreversible destruction are not distinguished.

### J5. Retention-history gap

The system cannot later establish why a record was retained, transferred or destroyed.

## K. Model-level failures

### K1. Storage-first architecture

A database/file/vector-store choice silently determines record identity, granularity and history semantics before requirements are known.

### K2. Universal-record schema

One record shape is imposed on heterogeneous record types even when their preservation/evidence requirements differ.

### K3. `Memory` umbrella collapse

State, evidence, documents, facts, events, indexes and derived knowledge are stored under one undifferentiated memory abstraction, hiding different lifecycle/trust requirements.

### K4. Linear-lifecycle absolutism

A simple creation→use→disposition lifecycle is treated as ontological truth even for records that are continuously captured, reused, reorganised and pluralised.

### K5. Immutability absolutism

`never mutate and never delete` is treated as universal correctness, ignoring correction semantics, privacy, retention and cost.

### K6. Mutability absolutism

`current state is enough` is treated as universal correctness, erasing history/provenance needed for accountability or recovery.

## How this inventory should be used later

A candidate record model should not merely be described positively. It should be tested against the failure classes relevant to its intended record types and risk.

The list is deliberately broader than what every implementation must prevent. Coverage requirements should be derived from purpose/risk rather than turning the inventory into ritual bureaucracy.