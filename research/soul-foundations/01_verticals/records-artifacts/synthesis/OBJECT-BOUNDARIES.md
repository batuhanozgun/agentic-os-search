# Records / Artifacts — Object Boundaries Synthesis

**Status:** bounded synthesis for completed object-boundaries pass  
**Date:** 2026-09-01  
**Scope:** Records vertical only; not a SOUL architecture decision.

## Research question

Among persistent information-bearing things, which object distinctions are genuinely load-bearing; when does something count as a record; is `artifact` a useful foundational category; and how should identity behave across copies, representations, versions, corrections, derivations, and aggregations?

## Executive result

The evidence does **not** support a flat ontology such as:

`file/document/artifact = record`

or:

`everything persistent = record`.

A better-supported working model is **layered and relational**:

1. there is some information-bearing resource/content that can persist and be identified;
2. that resource can have one or more concrete representations/instantiations/copies;
3. it can have time/content-specific versions or revisions while still belonging to a broader identity family;
4. `record` is not adequately explained by storage alone — it involves persistent representation plus an activity/context/evidence/reference/recordkeeping relation;
5. record status can be context-dependent even when content is identical;
6. derived objects and aggregations can acquire identities and management semantics of their own;
7. `artifact` is too polysemous to serve as a stable foundational super-category for this vertical.

The strongest current synthesis is therefore:

> **Record is best treated provisionally as a contextual role/type of persistent information resource, not as a synonym for file, document, copy, or all persisted data. Recordhood has a representational core and a contextual/recordkeeping dimension.**

This is a cross-source inference, not the verbatim definition of any one standard.

---

# 1. Competing recordhood models

## Model A — Stored-information model

### Form

`record = information/data stored on a medium`

### Support

Some archival dictionary uses are broad enough to resemble this definition, and database terminology also uses `record` for a grouped unit of fields.

### Failure

It over-classifies.

NARA explicitly excludes some persistent copies, publication stocks, library/museum materials, and physical exhibits from record status. Identical copies can differ in record status because their purpose/use differs. Persistent storage is therefore insufficient.

### Verdict

**Rejected as a general Records-domain definition.** Useful only as source-specific computing terminology.

---

## Model B — Institutional/evidence/status model

### Form

A record is information created/received in activity/business and retained or required to be retained because it documents activity or has informational/evidential value.

### Support

NARA and ISO-derived records-management practice strongly fit this family. Record status can depend on business purpose, institutional control, use, disposition obligations, and whether a copy/draft carries unique documentary value.

### Strength

Explains why:

- an identical convenience copy can be non-record while another copy used in business is a record;
- a circulated draft can be a record while an uncirculated rough draft may not be;
- a query result/output can become a record if it has documentary significance.

### Failure / limitation

If used alone it can make recordhood look like an administrative label applied to arbitrary information and understate constitutive representational/context properties.

### Verdict

**Strong for operational record status, insufficient alone as universal ontology.**

---

## Model C — Diplomatics / constitutive-properties model

### Form

A record has stable/fixed documentary form and content, identifiable context, and archival bond/relationships; authenticity and reliability are meaningful record properties.

### Support

InterPARES/diplomatics.

### Strength

Protects against calling a bare payload or mutable transient state a record when the context/relationships required to interpret it are missing.

### Failure / limitation

Digital/dynamic environments can make strict fixity difficult. Contemporary archival theory contains explicit criticism of overly essentialist `recordness`. The model can become too restrictive if it requires traditional documentary stability for all digital records.

### Verdict

**Retain as a property/challenge model, not as the only recordhood threshold.**

---

## Model D — Persistent representation of occurrences

### Form

A record is a persistent representation of an activity/event/process/other occurrent, created by a participant, observer, or authorized proxy.

### Support

Geoffrey Yeo and later archival-theory synthesis.

### Strength

Explains why record is not simply `information`: it represents something that happened or was done, and persistence allows that representation to outlive the occurrence.

It also separates records from persistent representations that do not normally represent occurrences.

### Failure / limitation

Operational systems may intentionally retain reference/knowledge objects whose importance is not cleanly reducible to an occurrence. This model may therefore define `record` well while leaving a broader persistent-information domain outside it.

### Verdict

**Strong conceptual core for recordhood; likely needs a broader persistent-information category around it.**

---

## Model E — ICA RiC record-resource / instantiation model

### Form

RiC separates information/content-level Record Resources from their physical/digital Instantiations. Records are discrete information content formed/inscribed in persistent recoverable form during life/work activity and document/evidence Activity.

### Strength

Directly handles:

- one record with PDF, DOCX, and printed instantiations;
- copies through time;
- lost original instantiation with surviving derived instantiation;
- record-set / record / record-part boundaries;
- contextual judgement when digitisation/re-instantiation changes what counts as the `same` record.

### Key implication

File identity and record identity are different questions.

### Failure / limitation

RiC is an archival-description model and deliberately tolerates contextual judgement; it does not provide a universal deterministic algorithm for when transformation creates a new record.

### Verdict

**Best current concrete model for testing multi-level object boundaries, but not adopted as a SOUL schema.**

---

# 2. Reconciled recordhood model

The competing models are not fully mutually exclusive. They appear to address different layers.

## Layer 1 — representational eligibility

For something to be a plausible record, evidence strongly suggests it must at minimum be a **persistent/recoverable information-bearing representation**, rather than an evanescent state with no ability to endure beyond the generating circumstance.

This condition is necessary but not sufficient.

## Layer 2 — occurrence/activity/context relation

Records are repeatedly tied to life/work/business activity, transaction, event, function, or other occurrence. This relation explains their documentary/evidential character.

## Layer 3 — recordkeeping/status relation

Record status can depend on why/how an information object is retained, used, controlled, circulated, or relied upon. NARA's copy/draft cases demonstrate that identical or near-identical content may have different record status.

## Layer 4 — trust/context properties

Stable identity, context, provenance, integrity, relations/archival bond, and interpretability determine whether the record remains usable/trustworthy over time. These properties may be constitutive in some traditions and quality requirements in others.

### Working conclusion

`recordhood` is therefore unlikely to be either:

- purely intrinsic (`the bytes make it a record`), or
- purely assigned (`anything declared a record is a record`).

The strongest current model is a **hybrid**:

> a persistent information representation has recordhood when it stands in the relevant documentary relation to activity/occurrence and is retained/captured/used within a context in which that representation has continuing evidential, reference, accountability, memory, or informational function.

Specific legal/organizational systems may impose narrower thresholds.

---

# 3. Natural object distinctions

The research does not justify a final universal ontology, but several distinctions repeatedly survive independent counterexamples.

## 3.1 Persistent information resource / content-level identity

A neutral placeholder is needed for the broader class of identifiable, persistent information-bearing things before deciding whether they are records.

Examples:

- a policy document;
- a dataset;
- a publication;
- a source-code package;
- a preserved external reference;
- a record;
- a derived analytical report.

`Persistent information resource` is used here as a **working research label**, not a proposed SOUL class.

Why this distinction is needed:

- not every persistent information resource is a record under NARA/records-management frames;
- one resource can have multiple representations/instantiations;
- a broader identity can span multiple versions.

---

## 3.2 Record

A record is not the broad persistent-resource category. It is the subset/role with a documentary relation to an occurrence/activity/context and a reason/function for being retained or relied upon.

Important consequence:

`record` is partly semantic/contextual, not merely a storage datatype.

---

## 3.3 Representation / Instantiation

This distinction is strongly load-bearing.

Independent support:

- RiC: Record Resource vs Instantiation;
- Web/HTTP: resource vs representation;
- preservation models: intellectual/content entity vs representation/files;
- scholarly publishing: one version can exist in multiple formats/locations.

### Counterexample

A record exists as:

- DOCX,
- PDF/A,
- printed paper.

Treating each file/physical copy as a separate content-level record can lose the fact that they communicate one higher-level record. Treating them as identical objects can lose format/materiality/provenance differences.

Therefore both levels are needed.

---

## 3.4 Copy / instance

`copy` is not equivalent to `non-record` and not equivalent to `new record`.

NARA shows identical copies can independently acquire record status through different use/purpose. RiC similarly permits multiple instantiations of a Record.

This requires at least two questions:

1. Is this materially/logically a separate instance/copy?
2. Does this copy have distinct record status/identity in this context?

Conflating them loses important management semantics.

---

## 3.5 Version / revision / state-specific identity

This distinction is also load-bearing.

W3C PROV treats each revision result as a new Entity while allowing versions to specialize/alternate with a more general entity. DataCite similarly supports canonical resource identity plus version-specific identifiers.

This produces a useful identity pattern:

`resource family / conceptual identity`

→ `specific version/revision`

→ `one or more representations/instances`

This pattern is not mandatory for all domains, but it explains cases that a flat object model cannot.

---

## 3.6 Derived information object / derived view

A transformation must be classified by semantic effect, not by the fact that software produced a new file.

### Representation-like transformation

A new format or carrier can remain an instantiation/representation of the same higher-level record when relevant information/function is preserved.

Examples:

- PDF/A migration preserving a document's significant information;
- print and PDF forms considered equivalent for a user's purpose.

### New derived information object

A summary, extraction, analytical transformation, selected query output, translation with substantive transformation, or other semantic derivation may warrant a new identity with provenance to the source.

W3C PROV's derivation/revision vocabulary supports this distinction, and NARA shows system outputs/query results can themselves become records.

### Boundary

There is no universal file-level rule. The decisive question is whether the new object merely re-expresses the relevant identity or makes a new assertion/selection/transformation that needs independent provenance/status.

---

## 3.7 Aggregation / record set

Aggregation is not just a folder convenience.

Archival bond and RiC Record Set concepts show that grouping/order/relationships can carry information that item-level content does not.

Examples:

- case file;
- correspondence thread;
- transaction series;
- collection whose order reveals process;
- dataset release consisting of coordinated files.

A model that stores only isolated items can preserve bytes while destroying reconstructive meaning.

---

# 4. `Artifact` verdict

## Evidence

`Artifact` does not have stable cross-domain semantics:

- archival science: physical/man-made object, often three-dimensional, or a resource whose material object has intrinsic value;
- software/systems engineering: work product produced/used during a project;
- security/assessment contexts: evidence submitted to support a claim;
- forensics/imaging: unintended distortion or by-product introduced by a process.

These meanings are materially different.

## Candidate models tested

### A. Artifact as supertype above record

Rejected for the Records vertical. In archival terminology an artifact may be a physical object that is not a record; in software engineering it is defined via work-product semantics, pulling Work into the Records taxonomy.

### B. Record and artifact as two sibling primitives

Not supported. The artifact side does not have a single stable property boundary comparable to the record literature.

### C. Artifact as source-specific/contextual label

Supported.

`Artifact` is useful when a source/domain already defines it, for example:

- software build artifact;
- archival physical artifact;
- research artifact;
- forensic artifact.

But its meaning must be qualified by context.

## Verdict

**DISCARD `artifact` as a foundational super-category for the Records vertical. RETAIN it only as a qualified, source-specific term.**

Implication:

The directory name `records-artifacts` is now historically understandable but conceptually stale. Renaming the package is a repository-structure decision and is not performed automatically in this pass; the finding should be carried forward before any rename.

---

# 5. Identity and change matrix

| Scenario | Same higher-level resource? | Separate version/entity? | Separate representation/instance? | Can record status differ? | Current bounded interpretation |
|---|---|---|---|---|---|
| byte-for-byte copy | usually yes | usually no | yes | yes | copy identity and record status are separate questions |
| same content, PDF vs DOCX | often yes | not necessarily | yes | possibly | representation difference alone need not create new record |
| digitised paper original | often yes for informational purpose | not necessarily | yes | context-dependent | materiality may make it a different record for some uses |
| minor metadata/edit change | often yes | maybe | maybe | usually unchanged | threshold is policy/domain sensitive |
| substantive revision | yes as family | yes | one or more | yes | preserve revision relation; do not collapse history |
| correction of published record | yes as family | usually yes/status-specific | one or more | yes | original history + correction relationship should remain explicit |
| retraction/invalidation | identity persists | status event/new notice often separate | yes | materially yes | do not delete identity simply because current authority is withdrawn |
| summary/extraction | source family relation only | yes, derived entity | yes | may become record | semantic selection creates independent provenance obligation |
| format migration | usually yes if function/significant properties preserved | not necessarily | yes | maybe | `same` depends on preservation purpose/significant properties |
| query result | source data not same object | yes as output entity | yes | can be record | a derived output can acquire documentary status |
| aggregation/collection | members retain identity | aggregation has own identity | may have own representation | yes | aggregation/order can carry independent context |

This matrix is a research aid, not a universal implementation rule.

---

# 6. What is now load-bearing

The following distinctions have survived this pass strongly enough to guide further Records research:

1. **resource/content identity ≠ representation/instantiation**
2. **copy/instance identity ≠ record status**
3. **broader resource identity ≠ version/revision identity**
4. **representation ≠ semantic derivation**
5. **record ≠ all persistent information**
6. **record status has contextual/functional semantics**
7. **aggregation can have independent meaning/identity**
8. **current/authoritative status ≠ historical existence/identity**
9. **authenticity ≠ factual correctness**
10. **artifact is not a stable unqualified Records primitive**

---

# 7. Counterexamples that broke simpler models

## `One file = one record`

Fails when one record has DOCX/PDF/print instantiations or one database/file contains many record parts/records.

## `Same bytes = same record status`

Fails under NARA copy rules: same-content copies can serve different purposes and have different status.

## `New file = new record`

Fails for format migration/re-instantiation where a new file preserves the same higher-level record.

## `Same resource = one immutable object`

Fails for evolving resources with separately citable versions; DataCite/PROV distinguish canonical identity from versions.

## `Update means overwrite`

Fails for substantive revision/correction/retraction where historical state and change relation matter.

## `Artifact is the broad category`

Fails because the term means incompatible things across archival, software, evidence, and forensic contexts.

## `Recordhood is purely intrinsic`

Fails because copies/drafts can differ in record status by use/control/context.

## `Recordhood is purely declared status`

Fails because record traditions repeatedly require persistence/representation/activity/context properties; an arbitrary evanescent or context-free datum does not become a robust record merely by label.

---

# 8. Unresolved questions after this pass

## U1 — Minimum record envelope

What minimum properties must travel with a persistent information resource so later users can identify, interpret, contextualize, trust, change, and retrieve it appropriately?

Candidates include:

- identity;
- type/role;
- provenance/source;
- relevant occurrence/context;
- creation/capture time;
- version/state/status;
- representation metadata;
- integrity/fixity where needed;
- relation/aggregation context;
- authority/currentness signal;
- discovery/index metadata.

The correct minimum may differ by class and retention horizon.

## U2 — Change/status semantics

Which record-side transitions must remain first-class rather than one generic update:

- draft;
- current;
- superseded;
- corrected;
- retracted/invalidated;
- archived;
- disposed;
- derived;
- transformed/migrated?

## U3 — Identity thresholds

When exactly should transformation create:

- same instance;
- new instance;
- new version;
- new record;
- new derived resource?

The evidence suggests this cannot be universal and needs a property/significance decision model.

## U4 — Broader persistent-information domain

If `artifact` is discarded, what neutral term/frame should contain important persistent information that is not a record? `Persistent information resource` is only a working placeholder.

## U5 — Package rename

Should `records-artifacts/` eventually become `records/`, `persistent-information/`, or another name after the broader-domain question is resolved? Renaming now may be premature because U4 remains open.

---

# 9. Highest-information next internal Records pass

The evidence suggests the next pass should **not** yet select storage technology.

The highest-value next question is:

> **What is the minimum persistent information/record envelope required to preserve identity, context, provenance, temporal/status semantics, integrity, relationships, and retrievability across time — and which properties vary by record class or retention horizon?**

Why this comes next:

- object boundaries are now sufficient to avoid treating files as the natural unit;
- storage/organisation/retrieval decisions depend on what properties must actually survive;
- without a minimum envelope, any database/schema/storage comparison would optimize mechanisms before requirements are known;
- it keeps the research inside Records rather than drifting to Work/Actors.

This is `next logical work`, not automatically authorised next work.

---

# 10. Return-condition review

1. **Competing recordhood models compared:** yes — stored-information, institutional/status, diplomatics, persistent-representation, and RiC multi-level models.
2. **Load-bearing object distinctions counter-tested:** yes — resource, record, representation/instantiation, copy, version, derivation, aggregation.
3. **Artifact verdict:** yes — discard as unqualified foundational Records category; retain only qualified/source-specific use.
4. **Identity/change semantics explicit:** yes at conceptual level; implementation thresholds remain open.
5. **Adverse evidence/ambiguity explicit:** yes — recordhood traditions disagree; same/new identity after transformation remains context-sensitive.
6. **Source trace persisted:** yes — `sources/object-boundaries-recordhood.md`.
7. **Next research can be defined concretely:** yes — minimum persistent information/record envelope.

**Pass status: RETURN CONDITION MET.**

This does not complete the Records vertical.