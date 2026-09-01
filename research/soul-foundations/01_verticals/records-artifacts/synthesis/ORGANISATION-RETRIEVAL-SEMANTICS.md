# Organisation / Derived Views / Retrieval Semantics — Bounded Synthesis

**Status:** bounded synthesis for approved organisation/retrieval pass  
**Date:** 2026-09-01  
**Scope:** Records / persistent-information semantics only; not a search/storage/SOUL architecture.

## Research question

How must persistent information be organised and reached again so that the intended resource, version, standing and context can be found/reconstructed while access descriptions, indexes, caches, summaries and other derived views do not silently replace or distort the source-bearing information they describe?

---

# 1. Executive result

The research rejects two simple models:

`organisation = one canonical hierarchy`

and

`retrieval = generic search over stored records`.

The stronger bounded result is:

> **Organisation and retrieval are purpose-relative views over persistent information. Context-preserving relations, descriptive/knowledge organisation and access/retrieval projections solve different problems and may coexist. Retrieval sufficiency must be defined relative to the question being asked, the corpus/view coverage, temporal/standing scope, and required precision/recall.**

A second important correction is that `canonical vs derived` is too binary.

A derived description, query output or access collection can simultaneously:

- be derived from another resource;
- serve as an access/discovery view;
- have its own identity;
- and, depending on use, become a record in its own right.

Therefore **derivation, access function, recordhood and recordkeeping/source designation are independent dimensions**.

The key Records-side requirement is not that every access view be non-authoritative or ephemeral. It is:

> preserve exact binding and lineage between an access/derived object and the resource/version/standing it describes or derives from, plus enough freshness/coverage semantics to interpret what retrieval from that view means.

Who is authorised to designate a recordkeeping/current source remains outside this vertical.

---

# 2. Organisation is not one thing

## O1 — Context-preserving organisation

Purpose:
- preserve provenance;
- archival bond;
- creator/function/activity context;
- membership/order/aggregation relations whose loss changes interpretation or reconstructability.

Evidence:
- SAA provenance/original-order/archival-bond traditions;
- ICA RiC contextual relations and Record Sets.

Key property:

**The organisation is evidence/context-bearing.**

Changing or flattening it can lose information, not merely navigation convenience.

### Example

A correspondence series ordered by transaction/case may reveal process. Replacing that organisation with subject folders can make topical access easier while destroying process context if the original relations are not preserved separately.

---

## O2 — Descriptive / knowledge organisation

Purpose:
- describe subjects/types/topics;
- normalize labels;
- provide controlled vocabularies;
- supply broader/narrower/related concepts;
- enable alternative conceptual navigation and query expansion.

Evidence:
- SKOS concept schemes, mappings, collections and semantic relations;
- archival description/finding aids.

Key property:

**The organisation is interpretive/descriptive.**

It can be valuable and curated without being the same relation as provenance or original order.

### Important consequence

Multiple concept schemes/classifications can legitimately coexist.

An access taxonomy should not overwrite a provenance relation merely because it is easier to browse.

---

## O3 — Access / retrieval organisation

Purpose:
- accelerate known-item lookup;
- support filtering;
- support ranking/discovery;
- supply finding aids/catalogues;
- maintain caches/projections/search indexes;
- expose alternate access collections.

Evidence:
- OAIS Finding/Retrieval/Ordering Aids;
- FAIR searchable indexing;
- IR theory;
- materialized-view/cache/search-index counterexamples.

Key property:

**The organisation is query/use optimized and may be lossy, selective, inferred or temporarily stale.**

This is not automatically a defect. It becomes a defect when the view is used for a claim stronger than its coverage/freshness/derivation supports.

---

# 3. Multiple organisations can coexist without multiple source-of-truth objects

ICA RiC provides a strong counterexample to exclusive hierarchy:

- one Record may simultaneously belong to more than one Record Set;
- grouping can reflect provenance, formal classification, activity, researcher purpose or another contextual criterion;
- order can differ by criterion.

SKOS separately allows multiple concept schemes and mappings.

SAA original-order practice also demonstrates that contextual organisation can be preserved while catalogues/indexes provide alternate access.

## Bounded conclusion

> **Membership in an organisation is often a relation/view, not the identity of the record itself.**

A record may therefore be reachable through:

- provenance context;
- case/thread membership;
- subject taxonomy;
- creator index;
- temporal grouping;
- search ranking;
- a researcher-defined collection

without becoming six distinct source records merely because it appears in six access structures.

### Guardrail

This does not mean every organisation is arbitrary.

Some relations (provenance, archival bond, constitutive component/order) can be context-bearing and must survive. Others are convenient access projections. The system must distinguish the relation's semantics rather than flatten every grouping to one generic `tag/folder` relation.

---

# 4. `Canonical vs derived` is replaced by a multidimensional access-view model

The word `canonical` creates two problems:

1. prior Records research already found that current/designated standing can be role/context scoped rather than globally singular;
2. deciding who may declare a source canonical is an authority question outside Records.

For this vertical, the useful questions are instead:

## A1 — What is the target/source binding?

Which exact:
- resource family;
- version/revision;
- representation/instantiation;
- standing/as-of state

is described, indexed, summarized, cached or transformed?

Without exact binding, derived metadata can be correct but attached to the wrong target.

## A2 — What is the derivation relation?

Is the access object:
- descriptive metadata;
- a surrogate/finding aid;
- an index entry;
- a cache/projection;
- a summary/extract;
- a transformed dissemination package;
- an independently derived report/resource?

Different transformations lose/preserve different information.

## A3 — What is its own recordhood / lifecycle?

NARA demonstrates that query/report outputs can themselves be records depending on purpose/use.

OAIS demonstrates a related pattern: an Access Collection can begin as a purpose-specific derived collection and later be preserved as a new archival collection if considered valuable enough.

Therefore:

`derived from X` does not imply `not a record`.

## A4 — What is its access function?

Does it support:
- finding;
- exact retrieval;
- ordering/dissemination;
- topical discovery;
- ranking;
- browsing;
- historical navigation?

OAIS explicitly separates Finding Aids and Retrieval Aids.

## A5 — What are its coverage and freshness semantics?

- Which resources/versions are represented?
- As of when?
- Is lag expected?
- Is the view exhaustive or selective?
- Can the source be revalidated/resolved?

These properties determine what hit/miss/currentness claims the view can support.

---

# 5. Derived/access views form at least three operational patterns

These are relational patterns, not object classes.

## V1 — Descriptive surrogate

Examples:
- finding aid;
- catalogue record;
- package description;
- subject description.

Purpose:
- represent enough about another resource/collection to enable identification, understanding and discovery.

Properties:
- often intentionally selective;
- may describe at aggregate rather than item level;
- may have multiple versions/technologies for one source;
- source should remain resolvable/bound.

Failure:
- user mistakes omitted detail for source absence.

---

## V2 — Computed access projection

Examples:
- search index;
- materialized view;
- cache;
- ranking projection;
- automatically mined access collection.

Purpose:
- optimize query/visibility/performance.

Properties:
- can lag source state;
- can be incomplete or purpose-specific;
- often rebuildable/refreshable;
- may contain inferred/algorithmic organisation.

Evidence:
- PostgreSQL materialized views require refresh;
- Elasticsearch search visibility follows refresh semantics;
- HTTP caches have explicit fresh/stale/validation semantics;
- OAIS Access Collections can be based on unverified pattern-recognition results.

Failure:
- projection's currentness or inference is mistaken for source standing/fact.

---

## V3 — Derived persistent resource

Examples:
- formal report from system data;
- selected extract;
- published query result;
- summary used as a business record;
- access collection deliberately promoted to preservation.

Purpose:
- creates a new information object with continuing use beyond immediate access.

Properties:
- can have its own identity, status, preservation closure and lifecycle;
- must retain derivation/source-version provenance where relevant;
- may itself later be indexed/described by other access views.

Failure:
- treating it merely as a disposable cache loses an independently meaningful record.

---

# 6. Retrieval is not one operation

The evidence supports a **retrieval contract** rather than one generic `search` guarantee.

A retrieval contract should specify, at minimum:

- target/information need;
- identity granularity;
- current vs historical/system-known temporal scope;
- corpus/view coverage;
- freshness/as-of expectation;
- relevance/precision/recall expectation;
- resolution target (candidate description vs exact source resource);
- required provenance/aggregation traversal.

This is a research synthesis, not a proposed API.

---

# 7. Retrieval-mode families and sufficiency

## R1 — Known-item / exact-identity retrieval

Question:
> `Give me resource/version X.`

Primary need:
- unambiguous identifier/alias mapping;
- exact target binding;
- locator/resolver path;
- existence/availability status.

Ranking/semantic similarity is secondary or unnecessary.

A miss is relatively informative only if the identifier registry/resolution domain is the intended complete domain and sufficiently fresh.

---

## R2 — Attribute / structured filter retrieval

Question:
> `Give me records matching explicit structured predicates.`

Primary need:
- structured fields/relations with known semantics;
- consistent scope/units/vocabulary;
- index/scan coverage for the target corpus.

IR's text-relevance assumptions may be inappropriate where exact structural matching is required.

---

## R3 — Semantic / topical discovery

Question:
> `Show material relevant to this topic/need.`

Primary need:
- descriptive representations/features;
- relevance/ranking or conceptual relations;
- useful precision at inspected depths;
- tolerance for imperfect recall depending on use.

SKOS query expansion can improve recall through broader/narrower relations; this illustrates that discovery organisation changes the retrieval set without changing the underlying records.

### Epistemic limit

A high-ranked hit is a **candidate relevant item**, not proof that it is:
- the intended exact record;
- current/designated;
- authoritative for a role;
- complete;
- factually correct.

---

## R4 — Exhaustive / high-recall retrieval

Question:
> `Find all materially relevant records in the bounded corpus.`

Primary need:
- explicit corpus/coverage definition;
- high recall / false-negative sensitivity;
- query expansion/multiple strategies where needed;
- deduplication/identity resolution;
- freshness sufficient for the bounded corpus.

IR theory directly distinguishes this from top-results web search: professional searches can value recall far more than precision.

### Epistemic limit

If the relevant universe is unknown/open, `all` may be impossible to establish from retrieval alone.

---

## R5 — Current-standing retrieval

Question:
> `Which resource/version is currently designated/effective for role/context C?`

Primary need:
- standing relation scoped to role/context;
- currentness semantics from Pass 4;
- fresh enough access view or validation against source-standing data;
- exact version binding.

### Important result

A stale index may correctly identify an existing resource while still be wrong about current standing.

Therefore known-item existence and current-standing retrieval are different guarantees.

---

## R6 — Historical / as-of retrieval

Question:
> `What state/representation/standing applied at time T?`

Primary need:
- historical state/version preservation;
- effective/applicable temporal semantics;
- version/standing timeline;
- temporal selection rules.

RFC 7089 Memento is a strong countermodel: Original Resource, Memento, TimeGate and TimeMap distinguish current resource from access to prior states.

### Coverage limit

A Memento TimeMap lists versions known to a server. That is not logically equivalent to proving no other prior state exists elsewhere.

---

## R7 — System-known-as-of retrieval

Question:
> `What did the managing system know/record at time T?`

Primary need:
- system-known/recorded-time history from Pass 4;
- distinction from domain-effective time;
- historical metadata/standing state.

This differs from R6 when information was learned retroactively.

---

## R8 — Provenance / derivation traversal

Question:
> `Where did this come from and what derives from it?`

Primary need:
- typed derivation/provenance relations;
- exact entity/version binding;
- traversal closure for the required scope.

Text similarity is not a substitute for provenance.

---

## R9 — Aggregation / case / thread reconstruction

Question:
> `Reconstruct the relevant collection, case, sequence or context.`

Primary need:
- membership relations;
- ordering where meaningful;
- historical membership if it changes;
- provenance/context relations;
- component identity.

A set of independently retrieved items is insufficient if the relation/order carries meaning.

---

# 8. Retrieval hit and miss have bounded epistemic meaning

## Hit

A retrieval hit establishes only that:

> this retrieval mechanism/view surfaced this candidate under this query and view state.

Additional claims require additional checks.

### Hit does not by itself establish

- exact identity;
- current standing;
- designated recordkeeping status;
- completeness;
- factual truth;
- evidential sufficiency;
- provenance authenticity.

---

## Miss

A retrieval miss establishes only that:

> this retrieval mechanism/view did not surface a matching candidate under this query and view state.

### Stronger absence inference requires

- a bounded target corpus/domain;
- adequate coverage/indexing of that corpus;
- a query mechanism capable of matching the sought object;
- freshness/as-of consistency with the claim;
- sufficiently high recall for the requested absence claim;
- correct identity/alias/temporal scope.

### Therefore

`not retrieved` → `not present` is invalid unless the retrieval contract makes that inference sufficiently sensitive.

This directly operationalises the project's source-view-fidelity principle inside the Records domain.

---

# 9. Freshness is a semantic property of derived access

Three independent technical systems show the same general pattern:

- HTTP caches distinguish fresh/stale and support validation;
- PostgreSQL materialized views persist query results until refreshed;
- Elasticsearch changes become searchable after refresh rather than necessarily immediately.

This does **not** recommend any of those technologies.

It supports the Records-side principle:

> **Source change and access-view visibility are separate events unless a profile guarantees otherwise.**

## Safe semantic patterns

A derived view can be safe without synchronous refresh if its contract makes at least one of these true where required:

- its `as-of`/generation/freshness state is known;
- current-sensitive use validates against source standing at resolution time;
- the profile tolerates bounded lag;
- stale output is explicitly historical rather than presented as current;
- the view can be rebuilt/revalidated from preserved source/binding information.

## Unsafe pattern

A view with unknown freshness/coverage that is used to answer `what is current?` as if it were source truth.

---

# 10. Change propagation to access views is an obligation, not necessarily synchronous invalidation

When source standing changes through:

- correction;
- supersession;
- retraction;
- removal;
- version creation;
- changed access rights

access structures may temporarily lag.

The architecture-neutral requirement is:

> the retrieval profile must define when a derived view is sufficiently current for the claim it serves and what validation/resolution is required when it is not.

Examples:

- topical discovery may tolerate a short indexing lag;
- current-policy lookup may require source-standing validation;
- historical/as-of retrieval should intentionally preserve older standing rather than `update` it away;
- a retracted publication may remain discoverable, but retrieval must not silently present it as unretracted/currently reliable.

---

# 11. Organisation/retrieval failure modes refined

## F1 — Context replacement

A subject/access taxonomy replaces provenance/original-order relations rather than coexisting with them.

Loss:
- evidential/reconstructive context.

## F2 — View/source identity drift

An access description/index entry continues to resolve but now describes a different version/resource than originally intended.

Loss:
- exact binding.

## F3 — Shadow standing

A derived view stores independently editable `current/authoritative` status and diverges from the designated standing source.

Loss:
- currentness consistency.

## F4 — Stale-current confusion

A view is correctly stale but users/system treat it as current.

Loss:
- standing correctness, not necessarily source existence.

## F5 — Coverage blindness

A partial index/catalogue is treated as exhaustive.

Loss:
- valid absence/exhaustiveness inference.

## F6 — Granularity mismatch

Aggregate-level description is queried as though it were exhaustive item-level indexing, or vice versa.

Loss:
- recall/interpretation.

## F7 — Derived-output demotion

A query output/report that acquired independent business/evidential meaning is treated as disposable cache only.

Loss:
- independent record/history.

## F8 — Access-view promotion

A lossy summary/search result is treated as the source resource without resolution/provenance.

Loss:
- omitted context/source fidelity.

## F9 — Temporal flattening

Current search index cannot retrieve historical standing/version and users infer the past from present metadata.

Loss:
- historical reconstruction.

## F10 — Relation loss

Items remain individually findable but case/thread/order/provenance relations cannot be reconstructed.

Loss:
- aggregation meaning.

---

# 12. What the pass rejected

## `One hierarchy should organise all records`

Rejected as universal.

RiC permits multiple simultaneous Record Sets/contexts; SKOS permits multiple concept schemes; archival practice can preserve original order and add indexes/descriptions.

## `Taxonomy is the ontology of the records`

Rejected.

Knowledge organisation is useful for access and query expansion but need not encode provenance or intrinsic record relations.

## `Derived view = non-record`

Rejected.

NARA output records and OAIS promotion of Access Collections show derived outputs may acquire independent continuing recordhood/preservation value.

## `Search index = source of truth`

Rejected as general framing.

Indexes/projections can be stale, selective and purpose-specific.

## `Derived views must always update synchronously`

Rejected.

Caches/materialized views/NRT indexes demonstrate safe lag is possible when freshness/validation semantics are explicit and fit the use.

## `Retrieval miss proves absence`

Rejected without strong coverage/recall/freshness assumptions.

## `Retrieval hit proves authority/currentness/truth`

Rejected.

IR relevance and Records standing/identity are separate questions.

## `All retrieval needs the same precision/recall profile`

Rejected.

Known-item, web-like discovery and professional high-recall retrieval have materially different success criteria.

---

# 13. Architecture-neutral model after this pass

```text
Persistent source-bearing information
  ├─ identity / version / representation
  ├─ standing / temporal history
  ├─ provenance / contextual relations
  └─ preservation closure

        ↕ exact bindings / derivation / membership relations

Organisation & access layer(s)
  ├─ context-preserving organisation
  ├─ descriptive / knowledge organisation
  ├─ access descriptions / finding aids
  ├─ computed indexes / projections / caches
  └─ derived persistent resources

        ↓ interpreted through

Retrieval contract
  ├─ information need / target
  ├─ identity granularity
  ├─ temporal / standing scope
  ├─ corpus & coverage
  ├─ freshness / as-of state
  ├─ precision / recall requirement
  └─ resolution / provenance requirement

        ↓ produces

candidate(s) / exact resource / historical state / relation subgraph / aggregation
```

The physical implementation may collapse or separate these layers. The semantic distinctions must survive where the protected use depends on them.

---

# 14. Most important conceptual corrections

## Correction 1 — `canonical` is role/context scoped

Records should not assume one globally canonical object.

The safer Records-side concept is:

> a **designated source/recordkeeping/standing relation scoped to a role/context**, plus exact version/representation binding.

Authority to establish that designation is deferred.

## Correction 2 — source/derived is a relation, not a permanent class hierarchy

An object can be derived from another and still become a first-class record/resource with its own lifecycle.

## Correction 3 — organisation is plural

Different organisational views can coexist because they preserve/optimise different semantics. Their relation types and purposes matter more than choosing one master folder tree.

## Correction 4 — retrieval success is claim-relative

The question `can I find something?` is too weak. The system must know what retrieval contract the downstream claim requires.

---

# 15. Remaining uncertainty

## U1 — Profile derivation is now load-bearing

The first five passes now expose several conditional requirements:

- preservation closure;
- change/history depth;
- organisation relations;
- retrieval coverage/freshness/recall.

A method is still needed to derive the correct Records profile from resource class, use, horizon, risk and knowledge assumptions.

## U2 — Identity/significant-property thresholds

Access/transformation cases reinforce the unresolved boundary between new representation, version, derived resource and new record.

## U3 — External dependency survivability

Access relies heavily on external indexes, descriptions, vocabularies and relation graphs. The exact durability/materialisation rules by horizon remain only partially bounded.

## U4 — Assurance/trust profile

Identity/fixity/provenance/current-standing checks remain distinct. The required assurance strength by risk/profile is not fully derived.

## U5 — Disposition residual discoverability

After payload destruction, what should an identifier/tombstone/finding aid reveal, and for how long, remains profile-dependent.

## U6 — Neutral umbrella term

`persistent information resource` remains a working label rather than final ontology.

---

# 16. Highest-information next internal Records direction

This pass changes the next-step ordering.

The evidence no longer supports continuing to add isolated semantic dimensions indefinitely before integration.

The strongest next question is now:

> **Can the Records findings accumulated so far be converted into a small set of purpose-relative Records profiles / requirement derivation rules — specifying which identity, preservation, history, organisation, retrieval and assurance obligations apply for a given resource/use/horizon/risk — without prematurely choosing storage architecture?**

Why this rises now:

1. five passes have exposed many conditional rather than universal requirements;
2. preservation closure already depends on profile variables;
3. change semantics showed dimensions can be merged when they cannot vary independently for the use;
4. retrieval shows success criteria differ strongly by information need and coverage requirement;
5. without a derivation rule, a later technology/storage comparison would either over-require everything or silently omit needed semantics.

A competing candidate is a direct storage-pattern comparison. The evidence suggests that would still be premature until the requirement/profile selection rule is at least bounded.

This is next logical work, not automatic execution authority.

---

# 17. Return-condition review

1. Context-preserving vs descriptive/knowledge vs access organisation compared: **met**.
2. Source-bearing vs derived/access relationship model: **met at bounded relational level; binary canonical framing replaced**.
3. Different retrieval modes and sufficiency: **met at architecture-neutral conceptual level**.
4. Stale/incomplete/lossy/duplicate view failures tested: **met**.
5. Hit/miss epistemic limits explicit: **met**.
6. Standing-change propagation specified without synchronous architecture: **met**.
7. Adversarial pass: **performed separately; see `ORGANISATION-RETRIEVAL-COUNTERCHECK.md`**.
8. Source trace/synthesis/residual questions persisted: **met once state/index consolidation completes**.
9. Next direction re-derived: **met provisionally — profile/requirement derivation now highest-information candidate**.
10. No search/storage/vector/graph/database/SOUL architecture selected: **met**.

**Pass verdict: RETURN CONDITION MET, subject to adversarial check and repository consolidation.**

This does not complete the Records vertical.