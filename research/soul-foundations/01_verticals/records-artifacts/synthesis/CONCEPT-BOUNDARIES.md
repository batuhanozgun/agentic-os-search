# Records / Artifacts — Concept Boundaries

**Status:** provisional vocabulary for research; not canonical SOUL ontology  
**Date:** 2026-09-01

## Why this file exists

The vertical cannot be researched cleanly if adjacent terms are silently treated as synonyms. This file records working distinctions strong enough to prevent category collapse while keeping uncertain boundaries open.

## Working term map

| Term | Provisional working boundary | Confidence / caveat |
|---|---|---|
| **Data** | Encoded symbols, measurements, values or observations that can be processed/represented. | Broad umbrella; discipline-dependent. A database `record` can mean a row, which is not the same sense as archival record. |
| **Information** | Data/content interpreted or usable in a context; the semantic thing conveyed, not necessarily its durable carrier. | Strong distinction from bitstream supported by OAIS; philosophical definition deliberately left open. |
| **Record** | Persistent recorded representation maintained for later informational/evidential/accountability use with enough identity/context for that purpose. | Working hypothesis only; archival/legal/technical definitions differ. |
| **Document** | A bounded information-bearing representation/object intended for human or system use; may or may not be managed as a record. | Needs dedicated document-theory research if it becomes load-bearing. |
| **Artifact** | Broad produced/used object or work product; in technical contexts may itself be evidence or carry information. | NIST shows multiple meanings. Overlaps with record; not synonym. |
| **State** | A condition/configuration of some represented system or entity at a point/interval. | A state may be recorded, derived or transient; `state` itself is not automatically a record. |
| **Event** | An occurrence/change represented as something that happened, often with temporal identity. | An event record is a representation of the event, not the event itself. |
| **Fact** | A proposition treated as true about the represented world. | Semantic/epistemic notion, not a persistence unit. A stored assertion may later be corrected without changing what actually happened. |
| **Claim** | An assertion that something is the case. | Can be recorded without being true. Keeping claim and fact separate is important for correction/provenance. |
| **Evidence** | Material/information used to support or challenge a claim, decision or conclusion. | Relational role: the same record can be evidence for one claim and irrelevant to another. |
| **Knowledge** | Interpreted/accepted understanding held by a person/system/community, potentially derived from many records. | Not safely equivalent to stored records. Needs separate research if `knowledge management` becomes a later vertical/subproblem. |
| **Memory** | Either the capacity/mechanism for retaining and retrieving information or the retained content itself, depending on domain. | Too overloaded to use as a primitive without qualification. |
| **Derived view** | A projection, summary, index, cache, materialized view, embedding, report or other transformation computed from source material. | May be persistent and useful but is not automatically authoritative or lossless. |

## Record vs information

The strongest distinction currently available:

- information is what is conveyed/understood;
- a record is a managed persistent representation that lets some information/evidence survive across time and context.

This does not imply every record has one fixed human-readable message. Records may be structured, dynamic, aggregated or system-resident.

## Record vs storage object

A storage object answers `what unit does this storage technology read/write/address?`.

A record answers a different question: `what recorded representation must remain identifiable/contextualised for its intended future use?`

Possible relationships include:

- one record → one storage object,
- one record → many files/objects,
- many records → one database/file/container,
- one logical record → many versions/manifestations,
- a record → content plus external metadata/relations spread across stores.

Therefore storage granularity must not define record granularity by default.

## Record vs document

A document can be produced for communication/reference and never acquire a managed records role. Conversely, a record can be system-generated structured data, an event/log entry, or an aggregate not naturally described as a conventional document.

Working hypothesis:

`document` foregrounds an information-bearing communicative/bounded representation; `record` foregrounds persistence, context, history and evidential/informational role.

This needs further source work before being used as a formal distinction.

## Record vs artifact

NIST uses `artifact` for:

- a piece of evidence,
- a project work product produced/used to capture and convey information, such as source code or models.

Therefore artifact is presently best treated as a broad adjacent category. An artifact may become/be maintained as a record when its persistent context/history/evidential role matters; some artifacts may not be records under a given records regime.

Do not encode `record ⊂ artifact` or `artifact ⊂ record` as a universal ontology yet.

## Record vs event

The occurrence and its record are distinct:

`event/occurrence` → something happens  
`event record` → a persistent representation/assertion that the event happened

Event-sourced systems intentionally promote event records to the primary persistence model, but that is an architecture choice rather than an ontological identity between event and record.

## Record vs state

`current state` can be:

- a directly persisted authoritative representation,
- a snapshot derived from event history,
- a cached/materialized view,
- an ephemeral in-memory condition.

Therefore `state` and `record` must remain separate concepts until the persistence strategy is known.

## Record vs claim / fact / evidence

These distinctions are important for truth maintenance:

- a **claim** can be stored even if later shown false;
- a **fact** concerns what is actually true, not merely what was stored;
- a **record** preserves that a claim/observation/decision existed in a context;
- **evidence** is a role a record or other material plays relative to a question/claim.

A correction regime that overwrites a false historical claim with the new truth can destroy the fact that the old claim was once made and acted upon. Conversely, retaining only old claims without a clear current-status model can make present truth ambiguous.

## Trust properties: do not collapse them

### Fixity

Evidence that a particular representation/bitstream has not changed in an undocumented way between relevant points. A checksum is a common mechanism.

### Integrity

Whether the record remains complete and unaltered in relevant respects according to the governing preservation/recordkeeping requirements. Broader than a hash comparison.

### Authenticity

Confidence that the record is what it purports to be, with identity and integrity supported by provenance/procedural evidence.

### Reliability

Confidence that the record's content can be relied on as an accurate representation for its intended evidential purpose, often tied to how/when/by whom it was created.

### Usability

Whether the record can be found, retrieved, presented and understood in the context required for use.

These are related but non-substitutable. Passing one does not automatically prove the others.

## Identity boundary

Do not use `ID` without specifying which identity is intended:

| Identity | Question |
|---|---|
| logical/resource identity | What continuing thing are we talking about across versions/time? |
| version/manifestation identity | Which particular state/representation is this? |
| content identity | Are these exact bytes/content the same? |
| locator/reference | Where/how do I reach it or the current version? |
| provenance identity | Which generated/derived entity in a lineage is this? |
| aggregate identity | Which collection/series/set does this unit belong to? |

Git and W3C PROV show that useful systems/models explicitly separate at least some of these concerns.

## Time boundary

A record can carry multiple non-equivalent times:

- occurrence / valid time,
- creation time,
- authoring time,
- receipt/observation time,
- capture/registration time,
- system/transaction time,
- modification/derivation time,
- supersession/invalidation time,
- retention cutoff / disposition time.

These should be named by semantics, not stored as generic timestamps whose meaning depends on oral convention.

## Mutation boundary

`Change` currently decomposes into different semantic operations:

- edit/overwrite,
- correction,
- new version,
- derivation/transformation,
- annotation,
- supersession,
- invalidation,
- migration/conversion,
- deletion/tombstone,
- final disposition/destruction.

Whether the logical record identity continues across each operation is an open question that depends on purpose and record type. The operation must not decide that question implicitly.

## Organisation boundary

Distinguish:

- **intrinsic/context relationships** — provenance, archival bonds, sequence/aggregation arising from creation/use;
- **descriptive metadata** — information describing the resource;
- **access organisation** — taxonomy, index, search fields, embeddings, ranking structures, catalogs;
- **derived representations** — summaries/materialized views/caches.

A convenient access layer is not automatically canonical truth.

## Working anti-confusion vocabulary

Until deeper research changes it, use explicit qualifiers:

- `logical record`
- `record version`
- `record representation`
- `content object`
- `record metadata`
- `provenance record`
- `current view`
- `historical version`
- `derived view`
- `access index`
- `retention/disposition state`

This vocabulary exists to expose hidden modeling choices, not to prescribe a final schema.