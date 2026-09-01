# Minimum Persistent-Information Envelope — Bounded Synthesis

**Status:** bounded synthesis for approved minimum-envelope pass  
**Date:** 2026-09-01  
**Scope:** Records / persistent-information vertical only; not a storage schema or SOUL architecture decision.

## Research question

What minimum information must survive **with or around** a persistent information resource so that it can later be correctly identified, interpreted, contextualised, traced, placed in time/status, assessed for continuity/integrity, related to other resources, and retrieved/reconstructed — and which of those requirements vary by resource class, use, risk, or retention horizon?

---

# 1. Executive result

The initial phrase **`minimum envelope` survives only after a material reframing**.

The evidence does not support one universal bundle of metadata fields physically attached to every persistent object.

Different authoritative systems define valid but materially different minima because they protect different outcomes:

- DataCite's mandatory core is designed for identification/citation/retrieval;
- NARA's transfer minimum is designed for permanent U.S. federal records to remain identifiable, serviceable, interpretable, preservable and accessible;
- Australia's NAA starts with three core properties for all records and adds metadata as value/longevity/transfer requirements rise;
- PREMIS defines implementation-independent information a preservation repository needs to know, explicitly separating `need to know` from `must repeat/store locally`;
- OAIS requires all major PDI **classes** for long-term AIPs but lets the archive determine the detail needed in each class according to its holdings, Preservation Objectives, Designated Community and Knowledge Base.

The stronger synthesis is therefore:

> **A persistent resource needs a minimum preservation/reuse closure, not a universal object-local metadata envelope.**

Working definition:

> **Minimum preservation closure** = the smallest set of information, relationships, interpretive dependencies, controls and reliable bindings — whether intrinsic, externally linked, inherited from controlled context, or maintained by infrastructure — that allows a specified future use of a specified resource class to remain possible at a specified horizon/risk level.

This term is a local research synthesis, not an existing standard or proposed SOUL component.

The important shift is:

`Which fields must every object contain?`

→

`What must remain reliably knowable/recoverable for the intended future use, and where may that knowledge safely live?`

---

# 2. Why one universal minimum failed

## 2.1 Different valid minima protect different capabilities

### DataCite

Mandatory properties in Schema 4.7:

- Identifier;
- Creator;
- Title;
- Publisher;
- PublicationYear;
- ResourceType.

This is a coherent minimum for **citation/identification/retrieval** of research outputs. It does not attempt to be sufficient archival preservation metadata.

### NARA permanent-record transfer

NARA's common minimum requires:

- File Name;
- Record ID;
- Title;
- Description;
- Creator;
- Creation Date;
- Rights;
- plus Coverage/Relation when applicable.

The objective is long-lived permanent federal records that can be identified, serviced, interpreted, preserved and provided for access.

### NAA cumulative minimum

Australia explicitly varies the minimum by information value and expected longevity:

- Core: Identifier, Creator, Date Created;
- Additional for higher-value/long-term: Title, Protective Marking, Disposal Class, Format;
- Transfer/archival: Rights, Integrity Check.

### PREMIS

PREMIS's `core` means what most preservation repositories are likely to need. `Mandatory` means information the repository must know **if applicable**; it need not be redundantly written on each object if the repository reliably knows it through another mechanism.

### OAIS

For long-term AIPs, OAIS requires classes of Reference, Provenance, Context, Fixity and Access Rights information, plus Representation Information. But content depth varies by archive, Designated Community and Preservation Objective.

### Conclusion

There is no contradiction among these minima once their protected outcome is made explicit.

The contradiction appears only if one assumes:

> `minimum metadata` has a single context-free meaning.

That assumption is rejected.

---

# 3. The minimum is parameterised

The evidence indicates that a defensible minimum depends on at least these variables:

## 3.1 Intended future use / protected capability

Examples:

- known-item lookup;
- semantic discovery;
- citation;
- operational continuation;
- evidential/accountability use;
- audit/legal review;
- migration/transformation;
- independent interpretation;
- forensic reconstruction;
- archival reuse.

Metadata sufficient for one is not automatically sufficient for another.

## 3.2 Resource class / structure

Examples:

- simple self-contained document;
- structured dataset;
- database export;
- multi-file logical record;
- evolving/versioned resource;
- derived analytical output;
- aggregate/case/thread;
- executable/algorithm-dependent digital object;
- classified/restricted record.

## 3.3 Retention horizon / environmental change

A resource used only while its creating environment remains stable can safely inherit more context from that environment.

Long-lived resources face increasing risk that:

- identifiers change;
- software disappears;
- format semantics become obscure;
- organization/team knowledge disappears;
- vocabularies change;
- external registries disappear;
- current system state no longer explains historical state.

NAA explicitly increases required metadata with longevity/value. OAIS makes Representation Information relative to future Designated Community knowledge.

## 3.4 Risk / consequence / control requirements

Security-classified records need metadata that ordinary records do not. High-value archival transfers require integrity checks where ordinary low-value transactional information may be sufficiently protected by shared system controls.

## 3.5 Expected transformations

If migration, normalization, transcoding, summarization or other transformation is expected, the system needs to know which **significant / transformational properties** must survive and how to validate them. OAIS and PREMIS make this more explicit than the initial candidate model did.

---

# 4. Preservation-closure obligation families

The evidence supports a set of recurring **obligation families**. These are not universal fields. A family says what must remain knowable **when the protected use depends on it**.

## O1 — Referential identity and exact binding

### Question

**Which resource/version/representation is this metadata, history or request about?**

### Evidence

- OAIS Reference Information;
- PREMIS objectIdentifier;
- NARA File Name + Record ID;
- NAA Identifier;
- DataCite Identifier;
- FAIR persistent identifier and metadata→data identifier binding.

### Failure if closure is absent

- metadata attaches to the wrong object/version;
- copy and resource identity collapse;
- old identifiers break after migration;
- exact historical state cannot be referenced;
- external metadata exists but cannot be reliably joined to its target.

### Current status

**Strongest baseline obligation family.**

The exact identifier need not be globally persistent in every local context, but the scope/scheme/domain in which it is unique must remain knowable.

### Externalisation

Safe if the binding to the exact resource/version/representation is stable, unambiguous and itself preserved.

---

## O2 — Interpretability / representation closure

### Question

**How are the stored data/bits/symbols to be interpreted by the intended future user/system?**

### Evidence

OAIS is strongest here:

- structure representation;
- semantic representation;
- software/algorithm/instructions/encryption as other representation information;
- recursive Representation Information Networks;
- required depth depends on the Designated Community knowledge base.

PREMIS requires format knowledge for file/bitstream objects and supports environment information.

NARA requires enough documentation to interpret permanent electronic records.

### Failure if closure is absent

- bytes survive but meaning is lost;
- data can be opened but units/fields/codes are uninterpretable;
- required software/algorithm disappears;
- encryption or encoding knowledge disappears;
- a multi-object representation loses how components fit together.

### Current status

**Invariant at the level of purpose, variable at the level of explicit metadata.**

A short-lived plain-text resource may rely safely on current shared knowledge. Long-term/complex resources need increasingly explicit representation information.

### Externalisation

Allowed and often preferable for shared standards/registries, but only if availability and exact version binding remain controlled. OAIS explicitly treats disappearing Representation Information dependencies as information-loss risk.

---

## O3 — Origin / provenance / contextual history closure

### Question

**Where did this come from, in what context, and through which material transformations/history?**

### Evidence

- ISO 23081: record metadata should support interpretation in business/people context and events affecting the record;
- OAIS Provenance + Context;
- NARA Creator/Creation Date/Description and contextual metadata;
- NAA Creator/Date Created plus richer history where needed;
- FAIR detailed provenance;
- W3C PROV entity/activity/agent derivation;
- ICA RiC contextual/provenance relations.

### Failure if closure is absent

- orphaned content with unknown source;
- derived output cannot be traced;
- migration/transformation history cannot be reconstructed;
- record cannot be related back to the circumstance that made it meaningful;
- authenticity/reliability assessments become impossible or overconfident.

### Current status

**Strong general obligation, but required depth is variable.**

Important qualification: the minimum may sometimes be an explicit `unknown`, not a discovered creator. OAIS explicitly allows this depending on archival requirements.

### Externalisation

Provenance is naturally relational/graph-like and can live outside the payload. The relation and referenced entities/events must themselves remain resolvable and correctly version-bound.

---

## O4 — Temporal / version / state / status closure

### Question

**Which state of the resource is this, when was the relevant fact/action/status true, and what later events changed its standing?**

### Evidence

- NAA warns not to overwrite creation date with later closure/migration/modification dates;
- PREMIS models preservation Events with type/date/outcome and object links;
- W3C PROV treats revision as generation of new entities;
- prior object-boundaries pass established resource/version/representation separation;
- records metadata standards preserve events affecting records.

### Failure if closure is absent

- current and historical truth collapse;
- old version presented as current;
- correction/retraction cannot be reconstructed;
- creation time is overwritten by migration/modification time;
- provenance chain loses ordering.

### Current status

**Conditional but load-bearing whenever change/currentness/history matters.**

A genuinely immutable one-state object may need little beyond a creation/registration time. Evolving records require substantially richer temporal/state closure.

### Externalisation

Safe as event/history records if exact target binding and append/history integrity are preserved.

---

## O5 — Integrity / continuity / authenticity evidence closure

### Question

**What evidence allows us to determine that the preserved representation is the intended one and has not suffered an undetected material change?**

### Evidence

- OAIS Fixity Information is a required PDI class for AIPs;
- PREMIS models fixity/signatures but does not require explicit fixity on every object;
- NAA places Integrity Check at its Transfer/archival level rather than Core;
- ISO 23081 links metadata to integrity/authenticity assertions.

### Failure if closure is absent

- silent corruption goes undetected;
- wrong representation is treated as original/current;
- a transformation loses material properties without evidence;
- authenticity claim rests only on continued accessibility.

### Current status

**Integrity is a preservation/control obligation when continuity matters, but an explicit per-object checksum/signature is not a universal metadata minimum.**

A repository may satisfy integrity through storage/system controls, event history or other mechanisms. Long-horizon/transfer/high-risk uses justify stronger object-bound evidence.

### Important non-equivalence

Fixity/integrity does **not** prove factual correctness, provenance completeness or current validity.

---

## O6 — Relationship / aggregation / derivation closure

### Question

**Does this resource depend on other resources or an aggregation/order for its meaning, identity, provenance or reconstruction?**

### Evidence

- NARA Relation mandatory when applicable for multi-file logical records/components;
- PREMIS object relationships;
- FAIR qualified references;
- ICA RiC contextual/record-set relations;
- OAIS Context and Representation Information can include related objects/components.

### Failure if closure is absent

- multi-file logical record becomes isolated fragments;
- case/thread/order meaning disappears;
- derivation source is lost;
- representation components cannot be reassembled.

### Current status

**Conditional.**

It is not minimum for a truly standalone resource, but it becomes constitutive when meaning/reconstruction depends on relations.

### Externalisation

Usually natural. Relationship graph/aggregation membership must have durable identifiers, direction/semantics where needed, and version-aware binding.

---

## O7 — Rights / access / use-constraint closure

### Question

**What restrictions, permissions or legal/use conditions materially constrain preservation, access or reuse?**

### Evidence

- OAIS Access Rights is a PDI class;
- NARA Rights is part of permanent-transfer minimum;
- NARA classified records need additional classification metadata;
- NAA places Rights at Transfer level and Protective Marking at higher-value/long-term level;
- FAIR requires clear usage license for reuse.

### Failure if closure is absent

- restricted information is improperly disclosed;
- preservation action is performed without permission;
- lawful reuse becomes impossible because rights status is lost;
- classification/declassification obligations cannot be executed.

### Current status

**Conditional on the existence/materiality of rights/access constraints.**

`No restrictions` can itself be a meaningful explicit status in settings where ambiguity is unsafe.

### Vertical boundary

This pass can establish that constraint information must be preserved. It does **not** decide which Actor may grant/change rights.

---

## O8 — Discovery / retrieval-path closure

### Question

**Can the intended user/system find and retrieve the correct resource through the required retrieval mode?**

### Evidence

- FAIR: identifiers, metadata↔identifier binding, searchable registration, retrievable protocols;
- DataCite: metadata specifically for citation/search/retrieval;
- NARA: metadata index enabling identification/service/access;
- NAA Identifier as access point; richer title/description aids discovery.

### Failure if closure is absent

- resource is preserved but operationally lost;
- known identifier cannot resolve;
- semantic discovery cannot distinguish candidates;
- only stale index/summary can locate an otherwise authoritative resource.

### Current status

**System-level obligation; object-local descriptive richness is retrieval-mode dependent.**

Known-item lookup may need a reliable identifier and registry only. Semantic/exhaustive discovery needs richer descriptive/index information.

### Externalisation

Expected. Search indexes/catalogues are derived access structures. They must remain linked to canonical resource identity and must not silently become authority.

---

# 5. Two newly exposed meta-obligations

The initial candidate list missed two variables that materially determine the envelope.

## M1 — Preservation/use objective and target knowledge base

OAIS shows that `what must be preserved` cannot be decided without specifying:

- what future users must be able to do;
- which Designated Community is assumed;
- what knowledge that community can safely be assumed to possess;
- what Preservation Objectives must remain measurable.

Therefore the minimum cannot be computed from the resource alone.

A metadata package that is sufficient for today's expert may be insufficient for a future generalist; conversely, encoding every shared definition inside every short-lived object is unnecessary duplication.

### Working rule

Before asking whether a property is `minimum`, specify the protected future-use capability/horizon.

---

## M2 — Significant / transformational properties

When preservation involves change, it becomes necessary to know **which properties are supposed to remain invariant across transformation**.

Examples:

- human-readable content;
- numeric values/units;
- visual layout;
- ordering;
- executable behaviour;
- relationships among components.

OAIS explicitly preserves Preservation Objectives and Transformational Information Properties; PREMIS includes significantProperties.

This is not ordinary descriptive metadata. It is a preservation criterion.

### Working rule

If transformations are expected, a minimum closure needs either explicit significant-property criteria or another objective/oracle capable of determining whether the transformed resource still satisfies the intended identity/use.

---

# 6. Intrinsic vs external information

## Result

The evidence rejects the assumption that all required information must be embedded in the content object.

NARA explicitly allows metadata to be embedded, maintained in a records application, or both. NAA permits common metadata to be held at aggregate/system-governance level. PREMIS defines `mandatory` as what the repository needs to know independent of storage location. FAIR explicitly separates data, metadata and infrastructure. OAIS Representation Information can be recursively referenced.

Therefore the relevant distinction is not:

`inside object = safe` / `outside object = unsafe`

but:

> **Is the dependency durably bound, resolvable, version-correct, reconstructable and protected for the required horizon?**

## 6.1 Intrinsic / embedded

Advantages:

- portability;
- fewer external link dependencies;
- self-description;
- easier transfer across system boundaries.

Risks:

- duplication;
- stale duplicated metadata;
- difficult coordinated updates;
- large or recursive representation/context information cannot sensibly be embedded everywhere.

## 6.2 External linked metadata/context

Advantages:

- shared facts can be represented once;
- relationship/provenance graphs fit naturally;
- registries/vocabularies can evolve centrally;
- avoids per-object duplication.

Risks:

- broken link / registry loss;
- locator points to a changed resource;
- referenced schema/vocabulary version disappears;
- access controls later prevent interpretation;
- metadata/resource identity mismatch;
- aggregate membership changes without historical trace.

## 6.3 Inherited from controlled system/aggregate context

NAA provides a concrete example: common disposal/format/rights information may be held in governance documentation or an information asset register rather than repeated on every record.

This is safe only if:

- membership/scope is explicit;
- the applicable context version is historically recoverable;
- later migration does not silently detach the record from that context;
- the inheritance rule itself is durable and interpretable.

## 6.4 Reconstructable rather than stored

A value does not have to be stored if it can be deterministically reconstructed from preserved authoritative inputs/rules.

But `can be recomputed today` is not enough. For long horizons the algorithm, inputs, rule version, execution semantics and required environment may themselves become part of the closure.

---

# 7. A practical classification: baseline, conditional, useful

This is a conceptual research classification, not a schema obligation table.

| Obligation family | Status | Why |
|---|---|---|
| Referential identity + exact binding | **baseline** | without target identity metadata/context cannot be reliably attached or retrieved |
| Interpretability / representation | **baseline in purpose; explicit detail conditional** | data must be intelligible, but shared environment/knowledge can satisfy some of the obligation |
| Origin/context/provenance | **baseline in purpose; depth conditional** | enough context must survive for intended use/trust; `unknown` may be valid state |
| Discovery/retrieval path | **baseline at system level; richness conditional** | preserved but unreachable information fails intended reuse; semantic discovery needs more than known-item lookup |
| Temporal/version/status | **conditional** | essential for evolving/currentness-sensitive resources; simpler for one-state objects |
| Integrity/fixity evidence | **conditional by horizon/risk/control model** | long-term/high-value transfer needs stronger explicit evidence; repository controls may supply it elsewhere |
| Relations/aggregation/derivation | **conditional on dependency** | standalone objects need less; composite/derived/ordered resources need explicit relation closure |
| Rights/access/use constraints | **conditional on constraints/use** | essential where restrictions/permissions matter, unnecessary detail where they do not |
| Lifecycle/disposition metadata | **conditional management obligation** | required by record-management policy/value/horizon, not necessarily by semantic interpretation itself |
| Preservation objective/significant properties | **conditional meta-obligation** | critical when transformation/long-term preservation must be judged against explicit goals |

## `Useful but not universally minimum` examples

Depending on the protected use, these may add substantial value without being a baseline requirement on every object:

- human-readable Title/Description;
- keywords/tags;
- multiple historical identifiers;
- detailed creator/contributor roles;
- checksums on every object when integrity is already protected at another layer;
- per-object duplicated rights/disposal data inherited from a controlled aggregate;
- rich provenance when a simpler origin statement is sufficient;
- full format/application detail for short-lived resources in a stable environment.

The classification can change for a particular profile. `Title`, for example, is mandatory for DataCite and NARA permanent transfer, but not NAA's Core level.

---

# 8. `Minimum` decision test

A property/information item belongs in a specific minimum profile only if all of the following hold:

1. **Protected-use dependency:** absence can cause a material failure of the defined future use/preservation objective.
2. **Non-substitutability:** the obligation is not already satisfied by another reliable property, relation, rule or infrastructure control.
3. **Recoverability:** if external/inherited, the alternative source is expected to remain resolvable and version-correct for the horizon.
4. **Binding:** the information can be unambiguously associated with the exact resource/version/representation/context it describes.
5. **Horizon/risk fit:** the cost/complexity is justified by longevity, transformation, consequence and uncertainty.
6. **Epistemic explicitness:** if the value is unknown, the system can distinguish `unknown` from `not applicable`, `not captured`, or silently missing when that distinction matters.

This test is derived synthesis, not a source standard.

---

# 9. Horizon profiles — what changes qualitatively

The evidence, especially NAA and OAIS, indicates that the model changes **both quantitatively and qualitatively** with horizon.

## H1 — Session / short operational horizon

Can often inherit:

- file/representation interpretation from current software;
- actor/project context from active system state;
- rights/security from live platform policy;
- discovery from current indexes.

Minimum local metadata can therefore be small **if the surrounding context is itself reliable and in scope for the horizon**.

Main risk: mistaking temporary environmental availability for durable information.

## H2 — Project / medium-term continuity

Actor/session turnover and system changes make implicit context less safe.

Increasing need for:

- stable resource/version identity;
- provenance/history;
- explicit status/currentness;
- durable relationships/dependencies;
- reconstructable decision/context links;
- format/environment knowledge for non-trivial resources.

## H3 — Organisational / operational records horizon

Adds stronger needs around:

- accountable creator/origin;
- retention/disposition;
- security/protective markings;
- policy/authority status;
- migration/change history;
- controlled vocabulary/context continuity.

## H4 — Audit/legal/regulated horizon

Strengthens:

- exact identity/version binding;
- event/change trace;
- integrity/authenticity evidence;
- rights/access history;
- preservation of superseded/corrected states where required;
- provenance and custody/context.

## H5 — Archival / indefinite long-term

Qualitative shift: current software, jargon, institutional memory and external standards can no longer be assumed.

Requires deliberate closure over:

- representation information networks;
- Designated Community/knowledge assumptions;
- preservation objectives;
- significant/transformational properties;
- PDI classes;
- dependency/reference survival;
- explicit migration/transformation evidence.

### Conclusion

Longer horizon is not simply `more fields`.

It changes **what may safely remain implicit**.

---

# 10. Resource-class sensitivity

## Simple stable document

May require relatively little explicit representation context if format/language are stable and widely understood.

## Structured dataset

Interpretability can require schema, units, code lists, missing-value semantics, column meaning, calibration or domain vocabulary.

## Multi-file logical record

Relations/membership/order become constitutive.

## Evolving/versioned resource

Temporal/version/status history becomes essential.

## Derived analytical output

Derivation provenance and source/version binding become essential.

## Executable/algorithm-dependent object

Representation closure may include runtime/software/algorithm/environment semantics.

## Restricted/classified resource

Rights/security status and review/declassification metadata become essential.

### Conclusion

The same named obligation family can have radically different concrete metadata depending on resource class.

---

# 11. What the pass falsified

## `One universal minimum metadata list exists`

Rejected.

Different valid standards have different minima because they protect different outcomes/horizons.

## `Everything required must be embedded in each object`

Rejected.

Authoritative sources explicitly permit external, inherited, registry and system-level knowledge.

## `More metadata is always safer`

Rejected as a general rule.

NAA uses a deliberately small cumulative minimum and permits shared aggregate/system metadata; PREMIS avoids requiring redundant stored values when repositories already know them.

More duplicated metadata can create stale/conflicting copies.

## `Persistent ID solves identity`

Rejected as sufficient.

Identifier scope/scheme, exact version/representation binding, migration history and resolution infrastructure matter.

## `Fixity is the universal minimum proof of preservation`

Rejected.

Fixity is optional in PREMIS's object metadata and only appears at NAA's transfer level, while OAIS requires a fixity information class for archival AIPs. The required integrity mechanism is horizon/control dependent.

## `Provenance alone preserves meaning/trust`

Rejected.

Provenance does not substitute for representation information, fixity, current validity, rights or factual correctness.

## `Discovery metadata is always part of the object envelope`

Rejected.

Discovery is frequently infrastructure/index based, and the amount of descriptive metadata depends on retrieval mode.

---

# 12. Main architecture-neutral model after this pass

The strongest Records-only conceptual model is now:

```text
Preservation / future-use profile
  = intended use
  + resource class
  + retention horizon
  + risk / control obligations
  + expected transformations
  + target knowledge base / community

        ↓ determines

Required preservation closure
  ├─ identity / exact binding
  ├─ interpretation / representation
  ├─ origin / provenance / context
  ├─ temporal / version / status            [when change matters]
  ├─ integrity / continuity evidence        [risk/horizon dependent]
  ├─ relations / aggregation / derivation   [when dependencies exist]
  ├─ rights / access / use constraints      [when applicable]
  └─ discovery / retrieval path

        ↓ each obligation may be satisfied by

  ├─ intrinsic / embedded information
  ├─ external linked metadata or registry
  ├─ relation/provenance graph
  ├─ aggregate/system-level inherited context
  ├─ preserved business/system rule
  └─ deterministic reconstruction from preserved inputs

provided that the dependency itself remains
identified + bound + resolvable + version-correct + interpretable
for the required horizon.
```

This is a research model, not implementation architecture.

---

# 13. Most important conceptual correction

The natural unit of this problem is no longer `metadata field` and probably not `envelope` in a physical sense.

The evidence supports thinking in terms of **closure of future-use dependencies**.

A resource is adequately preserved for a particular purpose only if every load-bearing dependency required for that purpose remains available and interpretable:

- its own representation;
- the identity/metadata that describes it;
- the schemas/vocabularies/standards needed to interpret that metadata;
- the provenance/relationship graph needed for context;
- the infrastructure or preserved information needed to resolve those dependencies.

OAIS's Representation Information Network makes this recursive dependency explicit.

Therefore:

> **The envelope boundary is logical, not necessarily physical.**

---

# 14. Remaining uncertainty

## U1 — Neutral umbrella category

The broader category above/around `record` is still unresolved (`persistent information resource`, `information object`, `information content entity`, qualified `information artifact`, etc.). This pass did not need to resolve it.

## U2 — Exact profile derivation rule

We now know the dimensions that parameterise the minimum, but not yet a rigorous method for deriving a profile for a given resource/use/horizon.

## U3 — Identity/significance thresholds

The prior unresolved question remains: when transformation creates a new representation, version, record or derived resource. Preservation Objectives/significant properties now provide a better lens for that question.

## U4 — Change/status semantics

Which statuses and events must be first-class (`current`, `superseded`, `corrected`, `retracted`, `archived`, etc.) remains a separate Records problem.

## U5 — Retrieval sufficiency

This pass established that retrievability is a system-level closure obligation but did not determine the different metadata/index requirements for known-item, semantic, exhaustive, temporal and forensic retrieval.

## U6 — External-dependency survivability

The pass identifies broken external context as a failure surface. The precise conditions under which externalised metadata/context is safe enough for different horizons remain to be made operational.

---

# 15. Highest-information next internal Records direction

This pass materially changes the next-step ordering.

Before choosing storage or retrieval technology, the next strongest question is now:

> **How should a Records system represent change through time — creation, revision, supersession, correction, retraction/invalidation, derivation, migration and disposition — so that current truth, historical truth, identity and provenance remain simultaneously reconstructable?**

Why this rises above the prior queue:

1. the minimum-closure pass shows temporal/version/status information is conditional but becomes central whenever resources evolve;
2. current-vs-historical ambiguity is a recurring failure that storage choices will otherwise encode prematurely;
3. transformation/significant-property evidence now gives a better basis for identity-change thresholds;
4. this question remains entirely inside Records while preparing later organisation/retrieval work.

A competing candidate is the **profile derivation rule** (how to derive closure from class/use/horizon). That may be better treated after concrete change/retrieval semantics expose more real profile variation rather than formalising profiles too early.

This is next logical work, not automatic execution authority.

---

# 16. Return-condition review

1. Candidate obligation/property families tested across independent lenses: **met**.
2. Invariant-purpose vs conditional vs useful-but-nonminimum distinction: **met at bounded conceptual level**.
3. Intrinsic vs externally linked/inherited information analysed with failure cases: **met**.
4. Resource class and retention-horizon sensitivity tested: **met**.
5. Omission/adverse pass: **performed separately; see `MINIMUM-ENVELOPE-COUNTERCHECK.md`**.
6. `Minimum envelope` abstraction challenged: **met — retained only as logical preservation closure, not physical field bundle**.
7. No storage/schema architecture selected: **met**.
8. Source trace/synthesis/open issues persisted: **met once package state/index are updated**.
9. Next Records direction re-derived from findings: **met provisionally — change/time/status semantics now highest-information candidate**.

**Pass verdict: RETURN CONDITION MET, subject to repository consolidation and state update.**

This does not complete the Records vertical.