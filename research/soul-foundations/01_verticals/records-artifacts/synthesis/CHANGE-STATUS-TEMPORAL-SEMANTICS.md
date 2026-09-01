# Change / Status / Temporal Semantics — Bounded Synthesis

**Status:** bounded synthesis for approved change/status/temporal pass  
**Date:** 2026-09-01  
**Scope:** Records / persistent-information semantics only; not a temporal-storage architecture, workflow, or SOUL design.

## Research question

Which semantic distinctions about change through time must remain distinguishable across creation/capture, revision, migration, derivation, supersession, correction, retraction/removal, and disposition so that a persistent information resource's present standing and historical states remain reconstructable without generic `update` erasing meaning?

---

# 1. Direction correction: `truth` was the wrong word

The pre-pass framing sometimes used `current truth` and `historical truth`.

That wording is too strong for Records research.

Prior passes already established:

- authenticity does not imply factual correctness;
- fixity/integrity does not imply truth;
- provenance completeness does not establish evidential sufficiency.

A Records model can preserve **what resource/state existed, what status was asserted, what was effective/designated, and what the system knew/recorded at a time**. It cannot by itself determine whether the underlying proposition was factually true.

Therefore this pass uses:

- **current standing / current effective or designated state**;
- **historical state / historical standing**;
- **system-known/recorded state** where that differs from domain-effective state.

This correction prevents change semantics from absorbing evidence/reasoning semantics.

---

# 2. Executive result

The evidence rejects a single generic lifecycle state or `updated_at` model for evolving persistent information.

The stronger architecture-neutral result is:

> **Change is multidimensional. A persistent resource can simultaneously have a version lineage, production/reproduction state, currentness/designation standing, reliance/editorial status, availability status, and preservation/custody history. These dimensions answer different questions and must not be forced into one universal status enum.**

Likewise, change kinds are not interchangeable:

- revision is not necessarily correction;
- correction is not supersession;
- supersession is not retraction;
- retraction is not removal;
- removal is not destruction;
- migration/re-instantiation is not necessarily revision;
- derivation is broader than revision;
- disposition is broader than destruction.

The minimum semantic requirement is therefore not `store every event` or `keep every snapshot`.

It is:

> preserve enough **typed change facts, identity/lineage relations, standing assertions, relevant temporal semantics, and provenance bindings** to reconstruct the states and transitions required by the intended future-use profile.

This is a semantic obligation. It does not prescribe event sourcing, temporal tables, immutable storage, append-only logs, snapshots, or any other mechanism.

---

# 3. Why generic `update` fails

A generic update records only that something changed. It does not preserve **what kind of semantic change occurred**.

Consider these cases:

1. DOCX → PDF/A migration with no intended informational change.
2. A dataset receives a substantive new version.
3. A published article receives a correction because the prior version contained an error.
4. A newer policy supersedes an older policy even though the older policy remains historically valid for its earlier period.
5. A publication is retracted but remains available for transparency.
6. Full text is removed while identifying metadata remains.
7. A temporary record is destroyed after authorized disposition, while destruction proof remains.
8. A summary is derived from a source record and becomes an independently citable object.

All can appear as `resource changed at time T` in a naive system, but they have different effects on:

- identity;
- current standing;
- historical interpretation;
- reliability/reliance signal;
- availability;
- provenance;
- future retrieval;
- retention/history obligations.

Therefore `update` is a transport/storage observation, not an adequate semantic category.

---

# 4. Change kinds that survived cross-domain comparison

These categories are working semantic families, not proposed enums.

## C1 — Creation / generation

### Meaning

A new information-bearing entity/resource/version comes into existence.

### Distinguish from capture

Creation can precede the time a repository/records system receives or registers the resource.

### Identity effect

Introduces an identity at the relevant level: resource, version, representation, or derived object depending on what was created.

### Temporal implication

Creation/generation time is an event time. It need not equal system capture/recording time.

---

## C2 — Capture / registration / ingestion

### Meaning

An already-existing resource becomes known to, accepted by, or managed within a system/repository.

### Why separate from creation

A report can be authored Monday and captured into a records system Friday. Collapsing the two loses delay/history and can misstate provenance.

### Identity effect

Usually does not create a new higher-level intellectual identity merely because a system first saw the object. It may create a repository-specific instance/identifier.

---

## C3 — Revision / version creation

### Meaning

A resource is modified in a way treated as a new version/revision within a broader identity family.

### Evidence

W3C PROV models revision as a subtype of derivation. DataCite separates canonical resource identity from version-specific identities and lets stewards determine major/minor version thresholds.

### Identity effect

Usually:

`same broader resource family` → `new version/revision identity`

but threshold is domain/purpose dependent.

### Important distinction

Revision says **a revised version exists**. It does not by itself say the prior version was erroneous, invalid, superseded, or unsuitable for use.

---

## C4 — Representation migration / re-instantiation

### Meaning

The resource/version receives a new carrier, encoding, format, or representation.

Examples:

- DOCX → PDF/A;
- source file → normalized preservation representation;
- digitisation of a physical record;
- replicated representation in another storage environment.

### Identity effect

A new representation/instance can exist without a new higher-level version if the protected significant properties/function remain equivalent for the intended use.

### Evidence

JAV permits one VoR in multiple formats/locations. PREMIS records migration/normalization/replication as preservation events rather than treating them inherently as intellectual revisions.

### Boundary

If transformation changes protected/significant properties, it may cross into a new version or derived resource. The previous minimum-closure pass established Preservation Objectives/significant properties as the right lens for this threshold.

---

## C5 — Semantic derivation

### Meaning

A new information object is produced from one or more sources through selection, transformation, computation, summarisation, translation, aggregation, or other semantic processing.

### Identity effect

Normally a distinct entity/resource with provenance to source(s), even if the derivation remains within a recognizable family.

### Important distinction

PROV makes revision a type of derivation, but many derivations are not revisions.

A summary of a report is derived from it; it is not normally a new version of the report.

---

## C6 — Supersession / replacement standing

### Meaning

For a given role/context, one resource/version is designated to replace or take precedence over another.

### Why it is not a content-change kind

Supersession is fundamentally a **standing/relation assertion**:

`A is superseded by B for context/role R`

B may be:

- a corrected version;
- a planned new edition;
- a revised policy;
- a new dataset release;
- another resource entirely.

### Identity effect

The superseded resource usually retains historical identity.

### Temporal effect

Supersession can have an effective date distinct from creation/publication of the successor.

---

## C7 — Correction / erratum

### Meaning

A prior state contained an error/defect that is explicitly amended.

### Why distinct from generic revision

NISO JAV distinguishes Corrected VoR from Enhanced VoR. ICMJE distinguishes corrections of errors from evolving science/debate. Crossref treats editorially significant corrections as explicit updates.

### Semantic effect

Correction carries a proposition about the earlier state:

> the previous content required correction in a specified respect.

That historical fact should survive even when the corrected version becomes preferred/current.

### Identity/representation pattern

Domain practice may use:

- a separate correction notice;
- a corrected version;
- both;
- occasionally an in-situ change (which Crossref discourages for significant updates because it obscures history).

The Records requirement is not one exact pattern; it is recoverable linkage between original, correction action/notice, corrected state, and relevant times.

---

## C8 — Retraction / withdrawal of reliance standing

### Meaning

A resource's standing as something that should be relied upon/cited/treated as valid in its publication context is withdrawn or materially downgraded.

### Why distinct from deletion

NISO CREC, ICMJE and Crossref all support retaining/discovering the original while clearly surfacing retracted status and linked notice.

### Identity effect

Original identity normally remains. Retraction adds/changes standing and creates a related notice/event.

### Important terminology warning

Do **not** normalize `retraction` to W3C PROV `invalidation`.

PROV invalidation means destruction/cessation/expiry after which the entity is no longer available for use. Scholarly retraction normally leaves the entity available but changes reliance/editorial standing.

Same word-family, different semantics.

---

## C9 — Removal / access unavailability

### Meaning

Content becomes unavailable for access while identifying/status metadata may remain.

### Evidence

NISO CREC treats removal separately from retraction and recommends preserving metadata identifying the removed publication/status.

### Why distinct from retraction

- a retracted item may remain fully accessible;
- a removed item may be inaccessible regardless of why its reliability/status changed.

Therefore **reliance standing** and **availability** are different dimensions.

---

## C10 — Preservation/custody event

### Meaning

A repository performs an action such as migration, normalization, replication, validation, transfer, accession/deaccession, or other preservation/custody operation.

### Evidence

PREMIS models preservation events explicitly; NARA distinguishes transfer from disposal/destruction.

### Why separate from resource status/version

A migration event can happen to a current, superseded, corrected, retracted, or archival resource. It describes **what was done to/manage the representation**, not necessarily its editorial/business standing.

---

## C11 — Disposition / destruction history

### Meaning

Disposition is the terminal records-management action family: transfer for continued preservation or disposal of temporary records. Destruction is one disposal action.

### Evidence

NARA explicitly distinguishes disposition from destruction and requires irrecoverable destruction while allowing a certifiable record of destruction to remain.

### Records-side boundary

This pass does not decide:

- who is authorized to destroy;
- retention period;
- legal hold policy;
- approval workflow.

It only establishes:

> destruction of payload/content does not necessarily entail erasure of the resource's identity, disposition fact, destruction time, authority reference, or audit proof where those remain required.

---

# 5. One universal `status` enum is not supported

The sources use `state` and `status` for different semantic dimensions.

RiC `RecordState` refers to production/reproduction state such as `draft` or `copy`.

Crossmark/current publishing guidance uses status for editorially significant updates such as correction/retraction.

NISO JAV uses publication/version states such as VoR, CVoR and EVoR.

PREMIS events describe preservation operations.

NARA lifecycle/disposition concepts describe custody/retention actions.

These are not mutually exclusive values in one scalar domain.

A resource could simultaneously be:

- an official/version-of-record publication;
- a specific corrected version;
- currently the preferred version;
- available online;
- preserved in an archive;
- subject to a later preservation migration.

Or:

- a historical version;
- superseded;
- retracted;
- still publicly available;
- permanently preserved.

Forcing these into one `status` value loses information.

---

# 6. Working multidimensional standing model

The research supports treating the following as separate **questions**, not necessarily stored fields/components.

## D1 — Production / reproduction state

Question:

> At what production stage or transmission form is this representation/record?

Examples:
- draft;
- proof;
- accepted manuscript;
- copy;
- original;
- Version of Record.

Sources: RiC, NISO JAV.

---

## D2 — Identity / version lineage

Question:

> How is this resource/version related to predecessor, successor, broader family, or source derivation?

Examples:
- version-of;
- previous-version-of;
- new-version-of;
- derived-from;
- predecessor/successor;
- branch/merge.

Sources: DataCite, W3C PROV, RFC 5829.

This dimension is naturally relational and may form a graph rather than a scalar state.

---

## D3 — Currentness / designation / precedence

Question:

> For a specified role/context, which resource/version should presently be treated as current, preferred, effective, or authoritative-of-record?

Important:

`latest timestamp` is not a universal answer.

RFC 5829 permits multiple latest versions on branches and explicitly defines latest-version as system-defined. Scholarly VoR is formally declared rather than inferred from time alone.

Currentness is therefore role/context sensitive and may be multi-valued.

---

## D4 — Reliance / editorial integrity standing

Question:

> Is the resource currently considered fit for reliance in its governing publication/evidence context?

Examples:
- no known concern/current;
- expression of concern;
- corrected;
- partially retracted;
- retracted.

Sources: NISO CREC, COPE/ICMJE, Crossref.

This dimension should not be equated with factual truth. It records a governing standing/assertion.

---

## D5 — Availability / presence

Question:

> Is the content/representation currently accessible or still present?

Examples:
- available;
- restricted;
- removed;
- destroyed;
- payload absent but metadata retained.

A resource can be retracted but available, or removed without erasing identifying metadata.

---

## D6 — Preservation / custody state/history

Question:

> What preservation/custody actions or transitions have occurred?

Examples:
- captured/ingested;
- migrated;
- replicated;
- validated;
- transferred;
- accessioned/deaccessioned;
- disposed/destroyed.

This is largely event/history semantics rather than one current content status.

---

# 7. Temporal semantics: two general perspectives + typed event times

The source comparison does **not** support either extreme:

- one universal timestamp;
- a universal list of many independent top-level timestamp fields.

The strongest cross-domain distinction is borrowed cautiously from temporal-database theory.

## T1 — Effective / valid time

Question:

> When did this fact/status/relation apply in the modelled domain or governing context?

Examples:
- policy becomes effective 1 October;
- resource is designated superseded starting 15 March;
- correction states a value should be treated as corrected from an earlier effective period.

Temporal-database literature calls the analogous concept `valid time`.

## T2 — System-known / recorded time

Question:

> When did the managing system/repository record, learn, or assert this fact/status/relation?

Temporal-database literature calls the analogous concept `transaction time`.

These can diverge.

Example:

- a policy supersession is effective 1 August;
- the repository receives/registers the supersession on 10 August.

Without both perspectives, a historical query can answer either:

- `what was actually effective on 5 August?`, or
- `what did this system know on 5 August?`,

but not both reliably.

## Typed event occurrence times

Creation, capture, publication, revision, correction, retraction, migration, removal, transfer, and destruction each may have occurrence timestamps.

These should not automatically become ten universal temporal axes. They are **times of typed events**.

This gives a simpler bounded model:

- event type + event occurrence time;
- effective/valid interval where a standing/fact has domain applicability;
- system-known/recorded time where audit/reconstruction of knowledge state matters.

Resource profiles that do not need one of these distinctions should not carry it by terminology alone.

---

# 8. Current standing and historical reconstruction must coexist

The Records requirement exposed by the sources is not `immutability` as an end in itself.

It is **reconstructability**.

Depending on future-use profile, a system may need to answer:

1. **Current-standing query**
   - Which version/resource is currently designated for this role?
   - Is it corrected/retracted/removed/restricted?

2. **Historical-domain query**
   - What resource/version/status was effective/designated at time T?

3. **Historical-system-knowledge query**
   - What did the system know/record at system time S, even if a later correction changed our understanding?

4. **Lineage query**
   - What predecessor/version/source did this derive from?

5. **Transition query**
   - Why/how did current standing change, and what event/notice established it?

A current snapshot alone cannot answer all five.

A raw event list alone also may not answer them if:

- event semantics are ambiguous;
- resource/version binding is unclear;
- effective time is not distinguished from recording time;
- currentness/authority rules were implicit and later changed;
- events were recorded at incompatible granularity.

Therefore the semantic requirement is:

> preserve enough typed transitions + standing assertions + identity relations + temporal bindings to reconstruct the required views.

How a system stores/recomputes those views is outside this pass.

---

# 9. Identity/provenance effects matrix

| Change | Higher-level resource identity | New version/entity? | New representation? | Standing effect | History/provenance requirement |
|---|---|---|---|---|---|
| creation | new identity at created level | yes | maybe | establishes initial standing | creator/origin + creation/capture distinction as needed |
| capture/registration | usually same external resource | not necessarily | repository instance may be new | may establish managed-record status | preserve source/capture time/binding |
| minor edit | usually same family | domain-dependent | maybe | often none | enough history if materially relevant |
| substantive revision | same family often | usually yes | one or more | may or may not supersede prior | predecessor/revision relation |
| migration/re-instantiation | same family/version if significant properties preserved | not necessarily | yes | usually unchanged | transformation event + source/target binding |
| semantic derivation | related but distinct resource | yes | yes | independent standing possible | derivation/source relation + process/context as needed |
| supersession | both identities persist | no requirement by itself | no requirement | precedence/currentness changes | superseded-by relation + effective time/context |
| correction | original identity persists | often corrected version/notice | maybe | previous state identified as requiring correction; corrected state may become preferred | explicit correction relation + what/when changed |
| retraction | original identity persists | notice often separate | original remains | reliance/editorial standing changes | retraction notice/reason/date/bidirectional linkage as applicable |
| removal | identity/metadata persists | not necessarily | content access changes | availability changes | removal status/date/reason linkage |
| preservation migration | same logical identity if preservation objective met | not necessarily | yes | editorial/currentness usually unchanged | preservation event + significant-property outcome |
| destruction/disposition | historical identity may persist as tombstone/audit reference | payload may cease | payload unavailable | terminal availability/custody change | certifiable destruction/disposition record where required |

This matrix is a research aid, not an implementation rule.

---

# 10. Important terminology collisions

## `Invalidation`

In W3C PROV, invalidation means cessation/destruction/expiry such that the entity is no longer available for use.

In ordinary records/publishing language, `invalid`, `invalidated`, or `retracted` may instead indicate a reliance/status judgment while the object remains available.

**Rule:** never normalize source-specific `invalidation` terms without preserving their source semantics.

## `State` / `status`

RiC RecordState = production/reproduction state such as draft/copy.

Crossmark status = current editorial update standing.

Database state = stored values at a time.

Preservation state = repository/custody condition/event history.

**Rule:** every status/state assertion needs a semantic axis/domain, not only a string value.

## `Current` / `latest`

Can mean:

- newest by time;
- tip of a branch;
- formally declared VoR;
- effective policy;
- preferred/current operational version;
- currently available representation.

**Rule:** `current` requires a role/context/selection rule.

---

# 11. What this pass falsified

## `Every change creates a new version`

Rejected.

Representation migration, replication and minor non-significant edits need not create a new higher-level version.

## `Every new file is a new version`

Rejected.

One VoR may exist in many formats/copies; preservation migration can produce a new representation.

## `Correction is just revision`

Rejected.

Correction specifically records that a prior state contained an error/defect requiring amendment; generic revision/enhancement does not.

## `Supersession = correction`

Rejected.

Supersession is a precedence/currentness relation and can result from many causes, including ordinary edition/version replacement without error.

## `Retraction = removal`

Rejected.

Retraction changes reliance/editorial standing while content usually remains discoverable; removal changes content availability.

## `Removal = destruction`

Rejected.

CREC removal preserves identifying metadata; NARA destruction is intended to make the record irrecoverable while destruction proof can remain.

## `Migration = revision`

Rejected.

Migration is a representation/preservation event unless protected informational properties change enough to cross an identity/version threshold.

## `Derivation = revision`

Rejected.

PROV makes revision a subtype of derivation; derived summaries/outputs need not be versions of source.

## `Current/latest = greatest timestamp`

Rejected.

RFC 5829 allows multiple branch tips and system-defined latest versions; other domains use formal designation/effective standing.

## `One status enum can encode lifecycle`

Rejected.

Independent sources use orthogonal status domains.

## `One timestamp is enough`

Rejected when effective/domain time and system-known time can diverge.

## `Every named date needs its own universal time axis`

Also rejected.

Many named dates are event occurrence times. Promote separate temporal axes only when their semantics produce different reconstruction answers.

## `Immutable history guarantees truth`

Rejected.

An immutable, perfectly preserved record can preserve an error or false assertion exactly.

## `Deletion should erase all trace`

Rejected as a universal rule.

Records-management systems may require proof/history of destruction even after payload is irrecoverable.

---

# 12. Compact architecture-neutral model

```text
Persistent information identity
  ├─ broader resource/family identity
  ├─ version/revision identities + lineage relations
  ├─ representation/instance identities
  └─ derived-resource relations

Change history
  ├─ typed events
  │    creation / capture / revision / migration / correction /
  │    retraction / removal / transfer / destruction / ...
  ├─ event occurrence time
  ├─ effective/valid time when applicable
  └─ system-known/recorded time when required

Standing dimensions (orthogonal questions)
  ├─ production/reproduction state
  ├─ currentness/designation/precedence
  ├─ reliance/editorial standing
  ├─ availability/presence
  └─ preservation/custody state/history

Required result
  ├─ current standing reconstructable
  ├─ historical effective standing reconstructable
  ├─ historical system-known state reconstructable [when required]
  └─ identity/provenance lineage reconstructable
```

No line above implies a table, event store, graph database, status enum, or immutable log.

---

# 13. Relationship to minimum preservation closure

The previous pass said preservation closure is purpose/class/horizon/risk dependent.

This pass refines the temporal part of that closure:

For an evolving resource, closure may require enough information to preserve:

- exact identity/version/representation binding;
- typed change semantics;
- standing/currentness assertions;
- effective and system-known temporal distinctions where they diverge;
- predecessor/successor/derivation/supersession relations;
- preservation/migration event history where identity continuity depends on it;
- terminal removal/destruction/disposition history where required.

For a truly one-state, short-lived resource, much of this may be unnecessary.

Thus `change history` is not universally maximal; it is profile-relative just like the rest of preservation closure.

---

# 14. Remaining uncertainty

## U1 — Identity/significant-property threshold

The semantic distinction is clearer, but a general decision rule remains unresolved:

> exactly when does a transformation remain a new representation, become a new version, or become a distinct derived resource?

Preservation Objectives and significant properties are the best current lens, but the threshold is still class/use dependent.

## U2 — Currentness/designation semantics by domain

We know currentness is role/context dependent and can be multi-valued. We have not yet defined how different resource classes establish/designate currentness without importing authority/Actor semantics.

## U3 — Retrieval of current vs historical standing

This pass establishes the semantic questions that retrieval may need to answer but not the organisation/index requirements for:

- current-only retrieval;
- as-of/effective-time retrieval;
- system-known-as-of retrieval;
- version lineage traversal;
- retraction/correction propagation into discovery views.

## U4 — Aggregation/history

A set/case/thread can evolve independently of its members. Membership/order history may require temporal semantics beyond individual resource histories.

## U5 — External standing propagation

A canonical record may be correctly marked retracted/superseded while stale indexes/caches/summaries continue presenting old standing. The semantic propagation obligation is visible; safe derived-view/retrieval design remains open.

## U6 — Disposition residual identity

The pass establishes that destruction history can survive payload destruction, but the minimum residual identity/tombstone/history profile is use/risk/policy dependent.

---

# 15. Re-derived next internal direction

The pass changes the relative priority of the remaining questions.

Before it, `identity/significant-property threshold` looked like the obvious next continuation. It remains important but is now partly constrained by the significant-property and change-kind model.

A broader, higher-information gap is now exposed:

> **How should persistent information be organised and retrieved so canonical identity, derived/discovery views, version/standing history, aggregations, and current/as-of retrieval remain distinguishable without derived indexes/summaries becoming shadow sources of truth?**

Why this rises:

1. the first four passes now establish what resource/record/version/representation distinctions exist, what closure must survive, and what temporal/change semantics retrieval may need to respect;
2. the original Records research objective explicitly includes organisation and reaching information again;
3. stale discovery views are now a concrete failure mode: a correct retraction/supersession status at the canonical source is insufficient if retrieval surfaces old standing;
4. aggregation/relations and retrieval are tightly coupled but can still be studied architecture-neutrally before selecting search/database technology;
5. delaying retrieval further risks over-optimising the object/history model without testing whether users/systems can actually recover the right state.

A bounded next pass should therefore likely combine:

- canonical resource vs derived/index/cache/summary views;
- organisation/aggregation/relation semantics;
- materially distinct retrieval modes (known-item, semantic, exhaustive, current, as-of, provenance/lineage, aggregate reconstruction);
- standing/freshness propagation requirements;
- retrieval failure and shadow-authority risks.

This is **next logical work**, not automatic execution authority.

---

# 16. Return-condition review

1. Main change kinds compared across independent disciplines: **met**.
2. Status vocabulary reduced to separate semantic dimensions rather than one copied enum: **met at bounded conceptual level**.
3. Load-bearing time distinctions identified conditionally: **met** — effective/valid vs system-known/recorded plus typed event times.
4. Identity/provenance effects explicit for revision, migration, derivation, supersession, correction, retraction/removal: **met**.
5. Current and historical reconstruction requirements explicit: **met**.
6. Disposition Records-side boundary separated from authority/policy/workflow: **met**.
7. Adversarial pass: **required separately before final return**.
8. Source trace + synthesis persisted: **met once source ledger and package routing/state are consolidated**.
9. Next direction re-derived from findings: **met provisionally — organisation/retrieval/derived-view semantics now appears higher-information than another narrow identity pass**.
10. No storage architecture, Work model, Actors model, authority system, or SOUL schema selected: **met**.

**Provisional pass verdict: return condition met subject to adversarial counter-check and repository consolidation.**

This does not complete the Records / persistent-information vertical.