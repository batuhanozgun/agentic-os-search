# Records / Artifacts — Foundational Synthesis

**Status:** bounded foundational synthesis; vertical remains open  
**Date:** 2026-09-01  
**Authority:** research synthesis only; not a SOUL architecture decision

## Research question

What is a `record`, independently of a particular environment, storage medium, software architecture or agent system, and what properties must be preserved so recorded information can be managed and recovered correctly over time?

## What the first broad pass establishes

### 1. There is no safe universal equation `record = stored information`

Records-management, archival-science and digital-record literature use several overlapping but non-identical definitions. The recurring themes are:

- persistence / recording beyond the immediate moment,
- representation of something — often an activity, event, transaction, state or claim,
- context and relationships that make the representation intelligible,
- metadata/provenance that support identity and evidential use,
- continued usability or accountability value.

The exact boundary varies by legal, organisational, archival and technical context. This means a SOUL Foundations study should not begin by declaring every durable byte sequence a record.

### 2. A record is not necessarily a discrete physical or storage object

Archival literature explicitly recognises records that exist through the structure and context of an information system rather than as one physical object. A record may also be an aggregate or derive meaning through its relationship to other records.

Therefore these questions must be separated:

- What is the conceptual record?
- What representation(s) embody it?
- Where/how are those representations stored?
- What metadata/relationships outside the content are required to interpret or trust it?

### 3. `Preserved bytes` is a weaker claim than `preserved information`

OAIS provides the clearest cross-check. A digital object requires Representation Information — structure, semantics and sometimes software, algorithms, standards or instructions — before a future community can interpret/use it. Representation Information can itself depend on other Representation Information.

This yields a critical distinction:

`bit/object persistence` ≠ `meaning persistence` ≠ `record continuity` ≠ `future usability`.

A checksum can show that a bitstream has not changed in an undocumented way. It cannot by itself establish that the object is the correct record, still meaningful, correctly contextualised, authoritative, or retrievable.

### 4. What must persist is a preservation envelope, not necessarily one blob

The current evidence supports thinking in terms of a **preservation envelope** whose components may be embedded, external or relational.

Candidate dimensions are:

1. **Content / representation** — the recorded symbols, data, document, object or aggregate.
2. **Representation information** — enough structure/semantics/dependency information to interpret the content for the intended future user/community.
3. **Identity / reference information** — enough to distinguish the continuing thing, particular versions and relevant identifiers.
4. **Provenance / lineage** — where it came from and which transformations/derivations led to it.
5. **Temporal information** — enough time semantics to distinguish occurrence/validity from recording/system history when that distinction matters.
6. **Context / relationships** — relevant bonds to related records, functions, sources, aggregates or surrounding structure.
7. **Trust evidence** — fixity/integrity/authenticity/reliability information appropriate to the purpose and risk.
8. **Rights / access information** — conditions under which preservation and use are allowed.
9. **Management/lifecycle information** — current status, retention/disposition rules and relevant preservation actions.
10. **Discovery/access metadata** — identifiers, descriptions and indexes needed to locate and retrieve it.

This is **not** a proposed mandatory schema. Different record types and preservation objectives may require different subsets. The important result is that a record's required persistence boundary can extend beyond its payload.

### 5. Record management is a lifecycle/governance problem, not storage alone

ISO 15489 and NARA both place creation/capture, organisation, access, use, migration/conversion and disposition inside records management. This means `store()` and `get()` are only two operations in a much larger problem.

A record-management system must potentially answer:

- What should be recorded at all?
- When does information become captured/managed as a record?
- What identity and context are attached at capture?
- How can the record change without erasing relevant history?
- Which representation is current, historical, superseded or invalid?
- How is it found later?
- Who may access it?
- How long should it exist?
- When and how may it be deleted or transferred?
- What must survive migration or format change?

### 6. Permanence is not the same as `keep forever`

Records-management practice treats appraisal and disposition as first-class. Some records are permanent; many are temporary and should be destroyed after explicit retention conditions. Vague `keep until no longer needed` rules are themselves a control failure in NARA guidance.

Therefore immutability and permanent retention must be separated:

- an immutable version can still have a finite retention period;
- a logically continuing record can acquire new versions;
- a delete operation can mean current-version removal, tombstoning, supersession, or irreversible disposition;
- retaining every version forever can create cost, privacy, discovery and governance failures.

### 7. Identity has multiple layers

Git, S3 versioning and W3C PROV independently demonstrate that `identity` need not be one identifier:

- a logical/current name can remain stable,
- a particular version can have its own identifier,
- exact content can have a content-derived identifier/hash,
- a storage locator can change,
- multiple representations can refer to aspects/versions of the same broader thing.

A future record model that uses one undifferentiated `id` risks conflating these semantics.

### 8. Time has multiple semantics

Temporal-database theory distinguishes at least:

- **valid time:** when the represented fact/state holds in the modelled world;
- **transaction time:** when the database/system contains or knows the representation.

Records can add further relevant times: creation, receipt, observation, capture, derivation, supersession and disposition. Therefore a generic `timestamp` field is not an adequate conceptual time model.

### 9. Change must have explicit semantics

The source set shows several distinct mechanisms that should not be collapsed into `update`:

- replacement/overwrite,
- new version,
- derivation,
- correction,
- supersession,
- annotation,
- invalidation,
- migration/conversion,
- deletion/disposition.

Git demonstrates immutable versions plus moving references. S3 demonstrates stable keys plus opaque versions. Event Sourcing demonstrates immutable change events plus derived current state. None is universally correct, but they expose a common design requirement: if history or evidence matters, the meaning of change must be explicit rather than silent overwrite.

### 10. Provenance is relational and can recurse

W3C PROV represents generation, use, derivation, attribution, association and delegation as relations among entities, activities and agents. It also supports provenance descriptions about provenance descriptions.

Therefore provenance cannot be reduced to a single `source` string without losing substantial semantics in cases where trust or derivation matters.

This vertical does **not** pursue the Actor or Work implications of those relations; they are deferred.

### 11. Organisation for context and organisation for access are different problems

Archival provenance/original-order ideas preserve creation/functional context. SKOS/taxonomies, descriptive metadata and search indexes organise information for discovery and access. FAIR emphasises persistent identifiers, rich metadata and searchable indexing.

This suggests at least three organisational layers:

1. context-preserving relationships,
2. descriptive metadata,
3. access/discovery structures.

A search index, vector index, taxonomy or summary may be an extremely useful derived view without being the authoritative record itself.

### 12. Storage architecture is downstream of required record properties

Current research identified several distinct persistence/state patterns:

- mutable current-state store,
- multiversion current-state store,
- immutable/versioned object store,
- content-addressed object graph,
- append-only event/change history with derived state,
- graph relationship representation,
- document/file collections with metadata,
- derived search/access indexes.

These patterns optimise different properties. Choosing a database or storage technology before deciding which history, identity, provenance, temporal, retrieval and disposition guarantees are required would invert the dependency.

### 13. `Artifact` is broader and more domain-dependent than `record`

NIST definitions use artifact for both a piece of evidence and a work product such as models or source code produced/used to convey information. This overlaps strongly with record but does not establish synonymy.

Current bounded view:

- **artifact** is a broader produced/used object or work product in many technical contexts;
- **record** more specifically foregrounds durable recorded representation, context/history and later evidential/informational use.

This distinction remains provisional and must be tested rather than canonised.

## Candidate working definition — explicitly provisional

A definition useful enough to continue research, but not yet ready for architecture use, is:

> **A record is a persistent recorded representation maintained so that something about a past or continuing occurrence, state, activity, decision, claim or information object can be recovered later with enough identity and context to serve its intended informational, evidential or accountability purpose.**

Why this wording is provisional:

- `persistent` may be relative to required lifetime rather than permanent;
- not every discipline requires an activity/transaction link;
- `identity and context` may live outside the payload;
- what counts as enough context/trust depends on purpose and risk;
- legal definitions can override generic conceptual definitions.

The working definition should therefore be treated as a hypothesis to stress-test, not as a result to build SOUL around.

## Strongest anti-collapse rules from the first pass

Do not silently equate:

- information = record,
- record = file/document/database row,
- record = artifact,
- stored = preserved,
- preserved bits = preserved meaning,
- checksum match = authentic record,
- current state = complete history,
- version = logical identity,
- content hash = record identity,
- one timestamp = temporal history,
- search result = authoritative source,
- taxonomy/index = canonical organisation,
- delete = one universal operation,
- long retention = permanent record,
- derived view = source record.

## Current research judgement

The Records / Artifacts vertical is **not complete**. The broad pass is sufficient to reject an early storage-first framing and to expose the load-bearing dimensions that need deeper study.

The highest-information next questions are now narrower:

1. Is `recordness` best understood as an intrinsic category, a contextual role/status, or a family of record types?
2. What exactly constitutes record identity across correction, versioning, migration, derivation and aggregation?
3. Which change semantics preserve truth/history without making current truth unusably ambiguous?
4. What is the correct granularity: item, assertion, event, document, aggregate, collection, or context-dependent unit?
5. Which parts of the preservation envelope are intrinsic to a record and which may safely remain external/derived?

These are recorded in `OPEN-QUESTIONS.md` and should drive the next deepening pass before any storage architecture selection.