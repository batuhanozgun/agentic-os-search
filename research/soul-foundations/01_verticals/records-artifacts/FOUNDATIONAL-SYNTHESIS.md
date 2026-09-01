# Records / Artifacts — Foundational Synthesis

**Status:** bounded foundational-pass synthesis; not final vertical conclusion  
**Date:** 2026-09-01  
**Source trace:** `SOURCES.md`

## Research question

What is a record, independently of a particular environment, storage medium, software architecture, or agent system; and what must be preserved and managed so information can be found, interpreted, trusted, changed appropriately, and reused later?

## Executive result

The strongest cross-disciplinary result is **not** a single universal definition of `record`.

The evidence instead supports a more useful boundary:

> A record is not adequately characterised by persistence alone. In the strongest records/archival frames, recordhood is a role played by an information-bearing representation that is created or received in relation to an activity/event/affair and retained so that it can later support action, reference, evidence, accountability, memory, or information use. Its durable usefulness depends not only on content but on sufficient identity, context, provenance, temporal semantics, integrity/authenticity evidence, relationships and representation information.

This is a **cross-source synthesis**, not an ISO quote and not yet a SOUL ontology.

Two corrections follow immediately:

1. `record = stored information` is too broad. NARA explicitly distinguishes records from some other stored/reference materials; ISO/InterPARES tie recordhood to activity/evidence/retention roles.
2. `record = immutable historical event` is too narrow. Records can be documents, structured data, aggregations or other forms; authoritative records can be corrected, versioned, superseded or migrated while their lineage and prior states remain important.

The foundational problem therefore looks less like **"where do we store information?"** and more like:

> **How do we preserve an information-bearing object's identity, meaning, context, history, trust properties and retrievability across time and change, while keeping authoritative source, versions, derivations and views distinguishable?**

## 1. `Information` is not a sufficiently precise storage primitive

Buckland's information-science distinction is useful because it separates:

- information as a process of becoming informed,
- information as knowledge/cognitive state,
- information as a thing/object regarded as informative.

Only the third is directly storable/retrievable as an external object. This matters because a system cannot literally persist another actor's `knowledge` merely by writing bytes; it persists representations from which knowledge may later be reconstructed or formed.

### Bounded implication

For this research, `information` should remain an umbrella term. We should not build the Records vertical on a DIKW-style assumption that data mechanically becomes information and then knowledge. The literature contains multiple incompatible definitions, and the hierarchy would prematurely settle an epistemological question that the records problem does not require us to settle.

A safer working distinction is:

- **representation / information-bearing object:** externally persistent thing that can carry information;
- **content/meaning:** what can be interpreted from that representation under some representation/context knowledge;
- **knowledge:** not assumed to be identical to the stored representation.

This distinction is provisional but robust enough to prevent `database contents = knowledge` collapse.

## 2. Recordhood appears relational/contextual, not merely intrinsic

Across ISO, NARA, SAA and InterPARES, the same bytes/object can fail to be a `record` under one institutional definition while qualifying under another because recordhood depends on relations such as:

- created/received in an activity or conduct of affairs,
- set aside/maintained,
- evidential/informational value,
- role in accountability/reference/action.

NARA's federal definition is especially useful as a negative case: reference/library/museum materials can be stored and informative without being federal records.

### Synthesis

`Record` is therefore best treated in this pass as a **functional/contextual status of an information-bearing representation**, not as a file type or storage class.

This does **not** prove that recordhood is only a relation; some archival/diplomatic traditions impose internal/formal requirements as well. But persistence alone is insufficient.

## 3. Record, document and artifact should not yet be synonyms

### Document

A document is a representation/content object in a broad ordinary/information-science sense. Some records are documents, but records need not be limited to traditional documents; structured/event/database records can perform record roles.

### Record

A representation with a recordkeeping relation/status: created/received in relation to activity and retained for evidence/reference/information/accountability or analogous durable use.

### Artifact

The current research has **not** found a comparably stable cross-disciplinary definition of `artifact` that makes it coextensive with `record`. In software, research, archaeology and digital scholarship, `artifact` can mean produced object/output much more broadly.

### Current verdict

Keep `records-artifacts` as the provisional vertical name, but do not merge the terms conceptually. A likely future distinction is:

- `artifact` = broader produced/obtained persistent object;
- `record` = an information-bearing object with a specific recordkeeping/evidential/reference role.

This remains a hypothesis because the artifact side has not yet received an equally deep independent terminology pass.

## 4. Persistence has multiple independent layers

The sources repeatedly falsify a one-dimensional meaning of `persistent`.

### 4.1 Bit/object persistence

The bytes/object still exist. PREMIS/Library of Congress fixity mechanisms address whether digital content changed unexpectedly at the bit level.

### 4.2 Identity persistence

A stable reference continues to denote the intended resource. RFC 8141 and PID systems show that identity can be location-independent.

But persistent naming does not guarantee availability or unchanged content. PID persistence is partly a governance/infrastructure commitment.

### 4.3 Interpretability persistence

OAIS makes the strongest case: a data object without sufficient Representation Information may survive physically but cease to be intelligible to its future audience.

### 4.4 Context persistence

Why it existed, what activity/event it relates to, its relations to other objects and its provenance remain recoverable.

### 4.5 Trust persistence

There remains enough evidence to judge whether it is what it purports to be, whether it changed, and how reliable/accurate its content may be.

### 4.6 Discovery/access persistence

The object can still be found and accessed. FAIR makes clear that findability, accessibility, interoperability and reusability are distinct properties.

### Result

A stored object can therefore be:

- preserved but not findable,
- findable but inaccessible,
- accessible but uninterpretable,
- interpretable but unauthenticated,
- authentic but factually wrong,
- correct at one time but stale now,
- richly indexed but no longer authoritative.

This multi-dimensional persistence model is one of the strongest results of the pass.

## 5. Content alone is not the durable record

ISO/NARA records metadata, OAIS, PREMIS, RiC and W3C PROV converge from different directions on a common point: durable use often requires information **about** the object and its relations/history.

A useful non-canonical decomposition is:

1. **Content / payload** — the represented material.
2. **Identity/reference** — what object/version this is.
3. **Representation information** — how to interpret the payload/formats/schema/encoding.
4. **Context/relations** — why it exists and how it relates to surrounding objects/activities.
5. **Provenance/lineage** — origin, derivation, custody and changes.
6. **Temporal semantics** — when the represented fact/event was valid/observed versus when it was recorded/changed.
7. **Integrity/fixity evidence** — whether undocumented alteration occurred.
8. **Management status** — retention, disposition, supersession, access restrictions or analogous control metadata.
9. **Discovery description/indexing** — enough metadata/organisation to find it later.

These are **properties/information obligations**, not a proposed database schema. Different object classes and risk horizons will need different subsets/depth.

## 6. Authenticity, integrity, reliability and accuracy are not interchangeable

This is a load-bearing distinction.

InterPARES and archival sources make the separation explicit:

- **Authenticity:** is this what it purports to be; has identity/integrity been preserved rather than substituted/tampered?
- **Integrity/fixity:** has it remained complete/unaltered except through documented/authorised change? Bit fixity is a narrow technical instance, not the whole semantic concept.
- **Reliability:** can the record be trusted as a representation/statement of the activity/facts, considering how it was created and completeness/control of creation?
- **Accuracy:** is the represented content correct/precise?
- **Usability:** can it be located, retrieved, presented and interpreted for use?

### Critical consequence

An authentic record can contain a lie, error, biased observation or obsolete claim. Cryptographic hashes, immutable logs or signatures can establish aspects of integrity/authenticity but **cannot turn false input into true information**.

This is a direct counterexample to any future design that equates `tamper-proof` with `truth`.

## 7. Provenance is necessary for many uses but is not truth

W3C PROV, NIST, OAIS and archival provenance all treat history/origin/derivation as important, but with different emphases.

The common core is that provenance helps answer:

- where did this come from,
- what produced/transformed it,
- what prior entities it derives from,
- what happened to it over time,
- sometimes who had custody/responsibility.

### Boundary

Provenance supports interpretation, reproducibility, accountability and trust assessment. It does **not** itself establish that the source was correct, competent, unbiased or truthful.

Therefore:

`known provenance ≠ verified truth`

and

`unknown provenance ≠ necessarily false`, though it may sharply reduce justified trust/reusability.

## 8. Identity and versioning require explicit semantics

W3C PROV, DataCite, NISO/Crossref and temporal systems expose a recurring ambiguity:

> When does a changed thing remain the same resource, and when is it a new entity/version?

There is no universal answer.

Examples:

- PROV can treat each revision as a new entity while relating revisions.
- DataCite permits the same DOI for minor changes but recommends new DOI for major changes; the steward determines the boundary.
- NISO scholarly version terminology permits a Version of Record followed by Corrected/Enhanced Versions of Record.

### Result

The Records vertical needs at least three identity questions, not one:

1. **conceptual/resource identity:** what continuing thing are we talking about?
2. **version/state identity:** which materially distinct state/release of it?
3. **representation/instance identity:** which file/copy/encoding/location represents that version?

A fourth may be required for aggregations/collections.

This is a research distinction, not yet a final ontology.

## 9. Mutation, correction, supersession and deletion are different operations

A naive CRUD model hides important record semantics.

Evidence across event sourcing, temporal databases, scholarly corrections and archival management suggests at least these distinct cases:

- **mutation:** change the current representation/state;
- **new version/revision:** preserve relation to prior state while creating distinguishable state;
- **correction:** assert that a prior representation contained an error and provide a corrected state without pretending the prior state never existed;
- **supersession:** a newer record becomes the operative/current authority while older record remains historically relevant;
- **retraction/invalidation:** retain existence/history while explicitly withdrawing validity/endorsement;
- **deletion/disposition:** remove content under a retention/disposition rule, possibly retaining metadata/tombstone/audit evidence;
- **migration/transformation:** representation changes while intended intellectual/content identity is preserved.

Which operation is appropriate depends on record type, risk, legal/operational need and future reconstruction requirements. The research therefore should not begin from `records must be immutable`.

## 10. Current state and historical record are distinct information products

Event sourcing and temporal database research provide a useful technical counter-frame.

A system may need both:

- **current state:** what is currently believed/operative;
- **history:** how that state came to be / prior recorded states.

Temporal database theory adds a more important distinction:

- **valid/event time:** when a fact is/was true in the represented world;
- **transaction/recording time:** when the system learned/recorded the fact.

These can diverge.

Example:

> On 10 September the system learns that an address changed on 1 August.

Overwriting a single `updated_at` field loses the difference between change-in-world and change-in-knowledge.

### Bounded implication

`state`, `event`, and `record` should remain distinct categories until further research. A current-state snapshot can be a record, an event can be a record, and an event sequence can reconstruct state—but none of these equivalences is universal.

## 11. Organisation is not just a user-interface concern

Archival provenance/original order, RiC relations, metadata standards and IR/FAIR show multiple legitimate organisation modes:

- creator/provenance grouping,
- original/process order,
- hierarchical aggregation,
- semantic/entity relations,
- subject/classification/taxonomy,
- identifier-based linking,
- search indexes / derived retrieval structures.

No single mode dominates all purposes.

### Important distinction

**Canonical organisation and discovery organisation need not be the same thing.**

An archive can preserve provenance/original order while providing subject indexes/catalogues. A database can preserve canonical entities while search indexes expose alternate retrieval views.

This suggests a strong general property:

> multiple derived access/organisation views may be desirable, but they must not silently become competing authoritative sources.

This remains a research property, not a chosen implementation.

## 12. Preservation and retrieval are orthogonal enough to fail separately

FAIR and IR make this explicit.

An object can be perfectly preserved yet practically lost if:

- no identifier points to it,
- metadata is insufficient,
- it is not indexed,
- vocabulary/query mismatch prevents discovery,
- permissions/access path are unavailable,
- retrieval returns a derived/stale representation instead of the authoritative target.

Conversely, a search engine can retrieve highly relevant material that is stale, unauthoritative, corrupted or contextless.

### Result

`stored`, `preserved`, `discoverable`, `retrievable`, `relevant`, `authoritative`, and `trustworthy` must be separate properties.

Search success is not a truth or authority oracle.

## 13. Metadata is itself a record-management problem

Metadata is often treated as a static wrapper around data. The evidence does not support that simplification.

Metadata:

- can be created at different lifecycle points,
- can be derived automatically or asserted manually,
- can change,
- can be incomplete or wrong,
- can itself need provenance/versioning,
- can outlive unavailable content (FAIR A2),
- can affect interpretation, authenticity and discovery.

Therefore `metadata about X` may itself require identity, provenance, authority and temporal semantics.

### Anti-recursion boundary

This does not imply infinite metadata-about-metadata. The stopping principle should be functional/risk based: preserve enough metadata lineage to support the claims, reconstruction, interpretation and controls that matter for the object's required use horizon.

The exact stopping rule remains unresolved.

## 14. Lifecycle and continuum are competing useful frames

NARA/records management commonly uses lifecycle language: creation → maintenance/use → disposition/transfer.

Records-continuum theory challenges a strictly linear custody/lifecycle view, especially for digital records, emphasizing simultaneous/multiple contexts and ongoing recordkeeping/metadata relationships.

### Current treatment

Do not choose one as universal yet.

- Lifecycle is operationally useful for management transitions and retention/disposition.
- Continuum is a useful counter-frame against assuming meaning/context begins at creation and then moves through clean sequential phases.

A later records pass should test whether SOUL-relevant persistent information is better modelled by states/transitions, overlapping concerns, or both.

## 15. Preliminary category map

This is a **working discrimination map**, not a final taxonomy.

| Term | Current bounded meaning | Key warning |
|---|---|---|
| Data | symbolic/recorded values or observations under some representation | not automatically true, contextualised or meaningful |
| Information | overloaded umbrella: process, knowledge, or informative thing depending on frame | do not use as a precise storage type |
| Information-bearing representation | persistent/external object capable of carrying interpretable content | broader than record |
| Document | bounded representation/content object | not every document is necessarily a record; not every record is a conventional document |
| Record | representation retained in a contextual/evidential/reference role related to activity/event/affairs | recordhood is not just storage format |
| Artifact | broader produced/obtained object; exact boundary unresolved | do not equate with record yet |
| Event | representation of an occurrence/change | event can be recorded; event ≠ record by definition |
| State | values believed/operative for a system/object at a point/interval | current state may hide history |
| Claim | proposition/assertion that can be supported, contradicted or qualified | claim ≠ fact |
| Fact | proposition treated as true of the world under an epistemic frame | storing a claim does not make it fact |
| Evidence | information/object used to support or challenge a claim/decision | evidence status is relational to what it bears on |
| Provenance | history/origin/derivation/custody information | provenance ≠ truth |
| Metadata | information describing/relating/managing another resource | metadata can itself be wrong, mutable and provenance-bearing |
| Derived view | summary/index/cache/transformation computed or curated from sources | usefulness ≠ authority; must retain source/derivation boundary |
| Memory | overloaded; can mean stored history, retrieved context, cognitive memory, or institutional record | postpone until a dedicated memory distinction pass |
| Knowledge | cognitive/epistemic concept or encoded knowledge representation depending on field | do not equate stored representation with knowledge without explicit model |

## 16. Cross-disciplinary invariant candidates

The following properties survived multiple independent lenses strongly enough to carry into the next Records pass as **candidate invariants**:

1. **Identity** — the object/version/representation being referred to must be distinguishable.
2. **Content/representation** — some persistent carrier encodes the material.
3. **Interpretability** — representation/schema/format semantics must remain available enough for intended users/systems.
4. **Context** — meaning/use often depends on why/how/where the object arose and its relations.
5. **Provenance/lineage** — origin and transformation history materially affect reuse/trust/reconstruction.
6. **Time** — event/validity/recording/change times may differ and matter.
7. **Integrity/change trace** — undocumented alteration must be distinguishable from authorised/documented evolution when material.
8. **Authority/status** — current/official/superseded/retracted/derived status must be distinguishable where decisions depend on it.
9. **Findability/retrievability** — persistence without rediscovery can be operational loss.
10. **Lifecycle/retention** — not everything should persist forever; preservation and disposition are policy/risk/value questions.
11. **Relationship/aggregation** — records rarely stand alone; collection/series/entity/derivation relations can carry meaning.

These are not necessarily fields on every record and not necessarily eleven SOUL primitives.

## 17. Failure surface map

### Existence failures

- loss / accidental deletion,
- unavailable storage,
- format/media obsolescence,
- corruption.

### Identity failures

- duplicate identifiers,
- one identifier silently denotes changed semantic object,
- copies/versions/representations conflated,
- broken references/reference rot.

### Meaning/context failures

- payload survives but schema/representation information is missing,
- source context detached,
- aggregation/order/relations lost,
- ambiguous terminology/units.

### Trust failures

- tampering or undocumented alteration,
- false authorship/origin,
- authentic but inaccurate/unreliable content mistaken for truth,
- provenance missing or fabricated,
- derived view mistaken for source.

### Temporal failures

- stale observation treated as current,
- event time confused with recording time,
- correction overwrites what was previously believed,
- current authority and historical validity conflated.

### Change/version failures

- destructive overwrite,
- fork/branch without lineage,
- superseded/retracted item still appears current,
- minor/major change boundary inconsistent,
- metadata changes without trace.

### Retrieval failures

- preserved but unindexed/unfindable,
- query vocabulary mismatch,
- relevant result omitted,
- wrong version/representation retrieved,
- search ranking substitutes relevance for authority/freshness.

### Governance/lifecycle failures (record-side only)

- over-retention creates noise/risk/cost,
- premature disposition destroys needed evidence,
- access restrictions make needed records unusable,
- uncontrolled copies create shadow truth.

Actor/work authority questions behind these are deferred.

## 18. What the foundational pass falsified

### F1 — `Record = file`

Rejected. Record concepts are format-independent and can include structured/electronic/non-document forms.

### F2 — `Record = anything persisted`

Rejected as a universal definition. Formal/legal/archival definitions add contextual/evidential/retention conditions and explicitly permit persistent non-record material.

### F3 — `Preserve the bytes and the record is preserved`

Rejected. OAIS/PREMIS/archival metadata show interpretability, context, provenance and integrity evidence can be necessary.

### F4 — `Immutable = trustworthy`

Rejected. Immutability/fixity can support integrity/authenticity but cannot establish accuracy/reliability/truth of initial content.

### F5 — `One timestamp is enough`

Rejected for important temporal cases. Valid/event time and transaction/recording time can diverge.

### F6 — `One authoritative object must never change`

Rejected as a universal rule. Correction/version/supersession models preserve authority while allowing controlled evolution and lineage.

### F7 — `If it is stored, it can be retrieved later`

Rejected. Findability/indexing/metadata/access are separate properties.

### F8 — `Metadata is timeless truth about the object`

Rejected. Metadata can change, be incomplete, derived, incorrect and itself require provenance.

## 19. What this pass does not establish

It does not establish:

- a final universal definition of `record`;
- that every persistent SOUL object should be governed as a formal record;
- a final `record vs artifact` boundary;
- a final data/information/knowledge ontology;
- a database, filesystem, Git, event-sourcing, graph, vector or hybrid architecture;
- append-only as a universal rule;
- a canonical metadata schema;
- a universal versioning threshold;
- a universal retention/disposition policy;
- the final relationship between Records, Work and Actors;
- any SOUL product architecture decision.

## 20. Highest-information unresolved questions

The foundational pass narrows the next Records work to concrete questions rather than generic breadth.

### Q1 — What is the natural object model?

Do we need a small family such as `resource / record / representation / version / aggregation / derived view`, or can fewer concepts preserve the distinctions above without semantic overload?

Why high value: identity, versioning, authority and retrieval all depend on this boundary.

### Q2 — What makes a persistent representation cross the threshold into `record`?

Is activity/evidence/reference retention enough, or do trustworthy-record requirements such as stable identity/context/integrity need to be constitutive rather than quality properties?

Why high value: determines whether `record` is a broad role/status or a narrower trusted object class.

### Q3 — What are the minimum metadata/context obligations by record class and risk horizon?

The evidence supports `more than content`, but not one universal metadata set.

Why high value: prevents both context loss and unbounded metadata bureaucracy.

### Q4 — What are the semantics of authority and change on the Records side?

Need to distinguish current/authoritative, historical, superseded, corrected, retracted, derived and cached states without solving Actor authority.

Why high value: directly prevents shadow truth and destructive overwrite.

### Q5 — Which temporal model is necessary?

When do we need event time, observation time, valid time, transaction/recording time, version time and freshness horizon?

Why high value: stale-world and retroactive-correction errors are otherwise structurally invisible.

### Q6 — How should canonical record structures coexist with multiple discovery views?

Need to test hierarchy, graph relations, indexes, semantic search and derived summaries as views without promoting retrieval structures to authority.

Why high value: connects preservation to actual later reuse while protecting source/view fidelity.

### Q7 — What does `artifact` add that `record/resource` does not?

Why high value: the vertical's current name may encode a redundant or genuinely broader category.

## 21. Return-condition assessment

The foundational pass has reached its intended return condition:

- multiple competing record definitions/frames were compared;
- category boundaries are explicit enough to expose where they remain unresolved;
- persistence, trust, identity, temporal, versioning, organisation and retrieval properties have cross-disciplinary support;
- counter-evidence and negative cases were actively incorporated;
- source trace is persisted;
- next questions are concrete and information-value ordered;
- no storage technology or SOUL architecture has been selected.

This is **not independent verification of the synthesis**. It is a source-grounded research synthesis with direct-source cross-checking. A later challenge/review pass may change the framing.

The Records / Artifacts vertical itself remains open.
