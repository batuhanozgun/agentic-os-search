# Records Mechanism Pattern Landscape — Bounded Synthesis

**Status:** bounded synthesis for mechanism-pattern landscape pass  
**Date:** 2026-09-01  
**Scope:** Records-relevant mechanism semantics and trade-offs; not a SOUL architecture or technology selection.

## Research question

How do major persistence/history/organisation/retrieval mechanism families satisfy or fail different Records Requirement Profiles, and which semantic obligations remain external to each pattern?

---

# 1. Executive result

The evidence rejects `pick one universal storage model` as a useful Records answer.

Different pattern families make different capabilities natural:

- mutable current-state stores make present operational state/querying natural;
- temporal/system-versioned stores make some system-time history queries natural;
- event-history models make typed transition/replay history natural when events are well designed;
- versioned object stores make representation recovery and object-version retention natural;
- content-addressed snapshot DAGs make exact content identity, branching and snapshot lineage natural;
- preservation-oriented layouts make rebuildable, validated versioned object preservation natural;
- graphs make heterogeneous relationship/context traversal natural;
- search indexes make discovery/ranking/filtering natural.

But **none of these native strengths equals a complete Records model**.

The strongest bounded principle is:

> **A mechanism should be evaluated as a partial satisfier of a requirement profile. Its native semantics, external semantic obligations, retention/failure behavior and derived-view role must be explicit.**

This produces a second principle:

> **Mechanism composition is often rational because Records obligations are heterogeneous, but hybrid composition creates new binding/synchronisation/authority failure modes and is not automatically superior.**

---

# 2. Evaluation axes from the first six passes

Mechanisms are compared against these Records-side questions:

1. **identity granularity** — representation, version, resource family, aggregate;
2. **current standing** — what is current/designated/reliable/available for a role;
3. **historical reconstructability** — prior states/versions and change meaning;
4. **temporal semantics** — system-known vs effective/applicable time when needed;
5. **typed change semantics** — revision, migration, derivation, correction, supersession, retraction, removal/destruction;
6. **provenance/derivation** — exact source/version and transformation lineage;
7. **integrity/continuity** — corruption/change detection and preservation evidence;
8. **relations/aggregation** — contextual graphs, component membership/order;
9. **retrieval contract** — known item, semantic, exhaustive, current/as-of, provenance traversal;
10. **retention/disposition** — what can be removed, how, and what history remains;
11. **transfer/rebuildability/interpretability** — surviving system/storage change;
12. **source vs derived-view binding** — avoiding shadow authority/stale projection errors.

A mechanism's `support` on one axis does not imply correctness on the others.

---

# 3. Pattern family A — Mutable current-state store

## Native shape

A current-state relational/document/key-value store typically models a logical identity/key with a current mutable value/row/document.

## Natural strengths

- current operational state;
- direct structured queries/filters;
- transactional update semantics where supported;
- constraints and application-level currentness;
- efficient replacement of current values.

## Records obligations that remain external unless deliberately added

- durable prior states/history;
- correction vs supersession vs migration semantics;
- effective-time/system-known distinctions;
- immutable evidence of what existed before overwrite;
- provenance/derivation;
- representation/version identity beyond the current key;
- archival preservation/fixity;
- residual disposition history.

## Important MVCC myth

PostgreSQL MVCC demonstrates why implementation `version` is not durable Records history. Old tuple versions support transaction isolation and can later be vacuumed/reclaimed.

### Verdict

**Good fit:** profiles dominated by current state, short/controlled horizon and modest history requirements.

**Poor fit alone:** profiles requiring durable historical/as-of reconstruction, transformation lineage or long-term preservation.

A mutable current-state store is not inherently anti-records; the failure is assuming current state is sufficient when the profile says otherwise.

---

# 4. Pattern family B — System-versioned / temporal current-state store

## Native shape

Current table/state plus automatically maintained historical row versions and system-time periods.

## Natural strengths

- current + historical row values;
- system-time `AS OF` querying;
- relatively low application burden for capturing update/delete history;
- direct mapping to structured records/facts.

## Critical boundaries

### System time ≠ domain-effective time

Engine-maintained `ValidFrom/ValidTo` naming can be misleading for Records semantics. The periods usually describe when a row version was current in the database/system, not necessarily when a policy/fact was effective in the governed world.

### Row version ≠ semantic change

The engine does not know whether a row changed because of:

- correction;
- supersession;
- migration;
- reclassification;
- editorial update;
- other semantic event.

### History retention is separate

SQL Server supports history retention policies and history can be cleaned. With system versioning disabled, privileged users can alter/delete history.

## External obligations

- typed semantic change/status;
- provenance/derivation;
- effective-time axis if different;
- record/resource/version identity above rows;
- integrity/audit evidence appropriate to risk;
- long-term representation/transfer closure.

### Verdict

**Good fit:** structured profiles needing system-known row history and as-of querying.

**Partial fit:** regulated/audit profiles if additional semantic integrity/authority/provenance controls exist.

**Not sufficient by label:** `temporal` does not mean complete bitemporal recordkeeping or archival history.

---

# 5. Pattern family C — Append-only event/change-history / Event Sourcing

## Native shape

Durable change events are treated as the primary history from which current state may be reconstructed/projection-derived.

## Natural strengths

- typed transition history if events are semantically designed;
- replay/rebuild;
- temporal reconstruction from event sequence;
- provenance-like history of state changes;
- derived current projections that can be rebuilt.

## Main Records risks

### Event completeness assumption

Replay only reconstructs what events encode. If events omit:

- effective time;
- exact source/version;
- correction/retraction meaning;
- external dependencies;
- actor/provenance facts;
- schema interpretation;

the event log can be complete operationally but incomplete as a Records history.

### Event schema evolution

Long-lived event streams require preserved meaning across event schema/business-rule changes. Replaying old events through new code can change interpretation unless historical semantics/rules are controlled.

### Retroactive correction

Late-arriving facts and corrections challenge a simple one-dimensional event sequence; system-known ordering may differ from effective/applicable ordering.

### Retention and privacy

`append-only forever` conflicts with some disposition/privacy profiles.

## Counter-frame

Fowler explicitly notes adequate history can be kept by other means; event sourcing is not uniquely required for history.

### Verdict

**Good fit:** profiles where semantically meaningful changes are central and replay/audit reconstruction is valuable.

**Poor fit alone:** preserved document/representation objects, rich semantic discovery, long-term format interpretation, or cases where deletion/disposition requirements conflict with indefinite event retention.

---

# 6. Pattern family D — Versioned immutable object store

## Native shape

Stable key/name with multiple opaque object versions; newest storage version is default/current for basic retrieval. Optional retention/WORM controls can protect versions.

## Natural strengths

- recovery from overwrite/delete;
- retention of exact representation versions;
- version-specific IDs;
- large binary/object storage;
- optional WORM/legal-hold style protection;
- decoupling current key from historical versions.

## Semantic limits

### Newest object version ≠ record currentness

Storage currentness says which PUT/delete-marker is latest. It does not say:

- which policy is effective;
- which publication is retracted;
- whether a version is corrected/superseded;
- which version is designated for a role.

### Delete marker ≠ destruction

S3 delete markers hide the current key while historical versions remain. Permanent deletion is a separate operation.

### Object Lock ≠ authenticity/truth

WORM protects against overwrite/delete for a period. It does not establish factual correctness, provenance completeness or semantic identity.

### Metadata/relations/search remain limited

Rich provenance, aggregation graphs and retrieval indexes generally live elsewhere.

### Verdict

**Good fit:** profiles dominated by durable representation/version retention, large objects, recovery and retention protection.

**Needs companion semantics:** standing/currentness, provenance, semantic relations and discovery.

---

# 7. Pattern family E — Content-addressed snapshot / Merkle-DAG model (Git-like)

## Native shape

Immutable/content-addressed blobs and trees; commits link snapshots to parent history; mutable refs name current branch tips.

## Natural strengths

- exact content identity;
- snapshot integrity through content addressing;
- branching/merging lineages;
- efficient deduplication;
- reproducible tree snapshots;
- explicit parent relationships;
- distributed copying/exchange.

## Records-relevant limitations

### Content identity ≠ continuing logical identity

A content hash changes on any content change and therefore cannot alone represent a logical resource family/current role.

### Refs are mutable currentness views

Branch/tag refs can move. Immutable content objects coexist with mutable logical names.

### History can be rewritten

Git explicitly supports rebase/history rewrite/replace mechanisms. This may be useful for software but conflicts with treating visible Git history as intrinsically immutable audit truth.

### Unreachable history can disappear

Garbage collection/reflog expiry can prune unreachable history. `content-addressed` does not mean `retained forever`.

### Commit metadata is limited provenance

Author/time/message/parents are useful but not full business/provenance/authority/rights/retention semantics.

### Verdict

**Good fit:** snapshot/version lineage for file/tree-oriented content, source/research artefacts, branching histories and exact content binding.

**Poor universal fit:** regulatory retention, large heterogeneous binary repositories, rich current-standing/retraction semantics, exhaustive metadata retrieval, or records whose natural unit is not a tree snapshot.

Git can be an excellent mechanism inside a Records profile without being a universal Records model.

---

# 8. Pattern family F — Preservation-oriented versioned object layout (OCFL-like)

## Native shape

Application-independent object root with explicit inventory, checksums/digests and sequential immutable version directories; designed for repository rebuildability and long-term object management.

## Natural strengths

- persistent versioned object inventory;
- content fixity/inventory validation;
- immutable prior versions;
- physical/logical path separation;
- repository rebuildability/transparency;
- storage-technology independence;
- preservation-oriented handling of multi-file objects.

## Limits

OCFL intentionally focuses on storage layout/versioned digital objects. It does not by itself solve:

- recordhood/context;
- business currentness/supersession/retraction;
- rich provenance beyond what supplied metadata expresses;
- graph-like contextual relations across many objects;
- semantic/exhaustive search;
- actor authority;
- factual correctness.

Its rebuildability goal can motivate richer self-contained metadata than some operational profiles need.

### Verdict

**Strong fit:** archival/preservation profiles needing transparent, reconstructable, versioned digital-object storage.

**Not universal operational store:** a long-term preservation layout should not be imposed on every short-lived/current-state record merely because it is robust.

---

# 9. Pattern family G — Graph/relationship representation

## Native shape

Entities/resources connected through typed edges/triples; possibly multiple/named graphs.

## Natural strengths

- heterogeneous relationships;
- provenance/derivation graphs;
- aggregation/context membership;
- alternate organisational views;
- traversals across record/resource/context relations;
- flexible schema evolution at relationship level.

## Critical limits

### Graph presence ≠ assertion semantics

RDF graph names, for example, are not automatically source/provenance/authority semantics.

### Mutable graph ≠ history

A graph can be updated destructively unless change/version semantics are layered in.

### Relation ≠ truth/authority

A triple/edge's existence does not establish its evidential authority, provenance or current standing.

### Blob/object preservation external

Graph stores are often not natural preservation mechanisms for large binary/file representations and their fixity/format closure.

### Verdict

**Good fit:** profiles where context/relations/provenance/aggregation traversal is load-bearing.

**Companion required:** persistent representations, history/standing, integrity and retrieval assurance appropriate to profile.

---

# 10. Pattern family H — Derived search/index/projection

## Native shape

Materialized structure optimized for querying, ranking, filtering or semantic access; usually regenerated or synchronized from source-bearing content/metadata.

## Natural strengths

- full-text/token retrieval;
- filters/facets;
- ranking;
- semantic/vector retrieval in other index families;
- high-performance access;
- purpose-specific denormalized views.

## Lucene evidence

- updateDocument is delete + add at index level;
- readers can remain on old point-in-time snapshots until refreshed;
- prior index commits are normally disposable depending on deletion policy;
- writer sequence numbers are transient and not durable record identity.

## Records implications

### Index history ≠ source history

Index versions/commits track access-structure state, not necessarily record history.

### Staleness can be intentional or harmful

Historical snapshot index may be valid for `as-of index T`; stale index is failure only when presented as current without appropriate freshness semantics.

### Search hit/miss claims are coverage-bound

Indexes need source/version binding, coverage and freshness contracts from Pass 5.

### Verdict

**Good fit:** discovery and retrieval profiles.

**Normally a derived role:** should not silently substitute for exact source/version/standing unless explicitly designated for a bounded recordkeeping role.

---

# 11. Capability matrix

Legend:

- **N** = comparatively native/strong;
- **P** = partial / depends heavily on application semantics;
- **E** = normally external/companion concern.

This is a conceptual matrix, not a benchmark.

| Pattern | Current state | Durable versions/history | Typed change/standing | Effective/as-of | Provenance/relations | Integrity/preservation | Discovery/retrieval | Long-term rebuild/transfer |
|---|---|---|---|---|---|---|---|---|
| Mutable current-state store | N | E | E | E | P | E | P/N | E |
| System-versioned temporal store | N | N/P | E | P | E/P | E/P | P/N | E |
| Event/change-history | P (projection) | N | N if modeled | P/N if modeled | P/N | P | P | P |
| Versioned object store | N (latest key) | N | E | E/P | E | P/N with lock/fixity | E/P | P |
| Content-addressed snapshot DAG | P (refs) | N while reachable | P | P | P | P/N content integrity | P | P |
| OCFL-like preservation layout | P | N | P/E | E/P | P/E | N | E | N |
| Graph representation | P | P/E | P if modeled | P if modeled | N | E | N for traversal | E/P |
| Search/index projection | N as index view | P by policy | E/P | P if indexed | P | E | N | E |

The matrix intentionally avoids `supports = solved`.

---

# 12. Cross-pattern scenario tests

## S1 — Short-lived internal current-state record

Profile:
- current known-item/structured retrieval;
- little history;
- low consequence;
- same environment.

### Suitable pattern behavior

A mutable current-state store may satisfy most needs directly, with lightweight identity/context and possibly a simple index.

### Over-engineering risk

OCFL/event sourcing/content-addressed history can add costs with little profile value if no history/preservation obligation exists.

### Lesson

Robust history mechanisms are not automatically better Records choices.

---

## S2 — Policy requiring current + historical/as-of standing

Profile:
- resource/version family;
- effective dates/current designation;
- historical as-of retrieval;
- supersession/correction history.

### Candidate satisfiers

- temporal store can provide useful system-known row history;
- immutable version objects/Git-like snapshots can preserve exact versions;
- event history can preserve standing transitions;
- search index can expose current/historical retrieval.

### Missing semantics in any single pattern

- temporal table needs explicit semantic standing/effective-time model;
- object/Git versioning needs designation/supersession relations;
- events need durable resource representations and query projections;
- index needs exact binding/freshness.

### Lesson

The profile likely requires **composition of semantics**, but not one mandatory topology.

---

## S3 — Audit/reproducible derived report

Profile:
- exact source/version provenance;
- derivation history;
- report representation preservation;
- later exact retrieval.

### Candidate pattern roles

- content-addressed snapshots or versioned objects: exact inputs/report versions;
- graph/event provenance: derivation relation and processing history;
- current-state DB: current metadata/status;
- index: discovery.

### Failure if naive

A Git commit containing report files is not necessarily enough if external dataset versions/process parameters are absent. An event log of report generation is not enough if report representation is missing.

### Lesson

`provenance` and `preserved object` are separable mechanism concerns.

---

## S4 — High-volume sensitive temporary transactions

Profile:
- structured current lookup;
- strong security/access;
- accountable deletion after short retention;
- limited long-term history.

### Candidate pattern behavior

Current-state store with necessary audit/disposition evidence can fit better than indefinite event/content version retention.

### Risk

Automatic versioning/history mechanisms can create over-retention/privacy exposure if disposition semantics are not applied to noncurrent versions/events/indexes.

### Lesson

History capability can conflict with deletion/minimisation requirements.

---

## S5 — Multi-file archival scientific dataset

Profile:
- long-term independent interpretation;
- versioned releases;
- aggregation/dependencies;
- fixity;
- transfer/rebuildability;
- discovery/provenance.

### Candidate pattern roles

- OCFL-like preservation layout/versioned object repository: preserved package/object history;
- graph/provenance metadata: cross-object/context relations;
- search/index: discovery;
- PIDs/registries: reference identity.

### Lesson

A preservation profile strongly motivates role-specialized composition because object preservation and discovery/context have different native structures.

---

# 13. Myth/failure tests

## `Immutable = trustworthy record`

Rejected.

Content-addressing/WORM/version immutability can support integrity/retention but cannot establish provenance, recordhood, factual correctness, current standing or authorization.

## `Versioning = history solved`

Rejected.

Object versions or Git commits do not say whether change is correction, migration, derivation or supersession. MVCC versions may disappear entirely.

## `Temporal DB = bitemporal Records model`

Rejected.

System-versioning gives system-time history; effective time and semantic statuses remain separate if required.

## `Event sourcing = provenance/audit solved`

Rejected.

Events only preserve encoded semantics; schema/rule evolution, external sources, effective time, retention and preserved representations still matter.

## `Graph = context/provenance solved`

Rejected.

Graph structure provides relation representation, not authority/provenance/fixity/history automatically.

## `Git = permanent audit log`

Rejected.

History can be rewritten/replaced; unreachable objects/reflogs can expire/prune; retention/currentness require policy beyond content addressing.

## `Object versioning = archival preservation`

Rejected.

Versioning can recover old bytes but not ensure interpretation, metadata closure, provenance, significant properties or rebuildability.

## `Search index can be the source because it contains the data`

Rejected as a general rule.

Indexes have independent update/delete/commit lifecycles and are optimized projections. They may be designated sources in a bounded role, but that designation requires explicit semantics and binding.

---

# 14. Hybrid/composition result

## Evidence-backed reason hybrids recur

The obligations are structurally heterogeneous:

- preservation of large immutable representations;
- mutable current standing;
- typed change/history;
- contextual/provenance graph;
- full-text/semantic retrieval.

One physical structure can sometimes satisfy several, but no reviewed pattern makes all of them native.

## But hybrid is not automatically better

Composition creates additional failure modes:

- stale projections;
- mismatched identifiers/version bindings;
- inconsistent deletion/disposition across stores;
- duplicated editable metadata/source-of-truth conflicts;
- incomplete transfer of dependencies;
- unclear which layer answers currentness/authority;
- different retention histories between source and index/log/graph.

## Architecture-neutral composition rule

If several mechanisms are used, each role must state:

1. which Records obligation it satisfies;
2. which resource/version identity it binds to;
3. whether it is source-bearing, history-bearing, context-bearing or access-derived for that role;
4. freshness/as-of semantics;
5. update/rebuild relationship;
6. retention/disposition relationship;
7. failure behavior when another component is unavailable.

This is a semantic contract, not a prescribed microservice/data topology.

---

# 15. Main mechanism-selection principle

The first six passes plus this landscape imply a disciplined ordering:

```text
context/appraisal
→ Records Requirement Profile
→ observable acceptance/failure requirements
→ compare mechanism patterns
→ compose/select mechanisms
→ only then concrete technology/schema/topology
```

Reversing this order creates storage-first architecture.

---

# 16. Residual uncertainties

## U1 — Assurance strength

Mechanism pattern comparison still lacks domain-independent assurance levels for integrity, availability, retention and audit history.

## U2 — Identity threshold under transformation

Pattern capabilities do not solve when a transformation is same representation vs new version vs new derived resource; the requirement profile must still supply the semantic rule/significant properties.

## U3 — Cross-mechanism deletion/disposition

When one logical record exists across source object, event history, graph metadata and search index, what does complete/correct disposition mean for each representation and residual history? Records semantics exist, but concrete coordinated mechanism requirements need further study.

## U4 — Failure/recovery semantics for composed systems

Which component must be reconstructable from which others? The profile can demand recoverability, but architecture-independent composition invariants need refinement.

## U5 — Mechanism verification

This pass is conceptual/source-based. Actual products/configurations can violate or strengthen the pattern assumptions and require implementation-specific verification later.

---

# 17. Highest-information next Records frontier

This pass moves the Records vertical close to its first broad synthesis boundary.

The next highest-value work is **not** immediately choosing concrete technologies.

The evidence suggests a bounded **Records vertical consolidation / completeness adversarial review** should come first:

> Across recordhood, preservation closure, change/time, organisation/retrieval, requirement derivation and mechanism patterns, what major Records problem classes are still missing or under-researched before the vertical can be considered sufficiently complete for later cross-vertical work?

Why this rises now:

- mechanism comparison covers the original `how stored/managed/organised/retrieved` question at pattern level;
- multiple unresolved issues may be refinements rather than missing foundational dimensions;
- a completeness/red-team pass can reveal omitted domains (e.g. confidentiality/privacy, archival appraisal, replication/disaster recovery, concurrency/distributed consistency, semantic knowledge claims) without automatically expanding scope;
- it can determine whether to deepen Records further or stop the vertical and move to another foundation later.

This is next logical work, not a SOUL architecture decision.

---

# 18. Return-condition review

1. Major pattern families source-grounded and compared: **met**.
2. Native semantics vs external obligations explicit: **met**.
3. Cross-pattern scenarios tested: **met**.
4. Mechanism myths tested: **met**.
5. Hybrid necessity challenged rather than assumed: **met**.
6. No implementation winner selected: **met**.
7. Source ledger persisted: **met**.
8. Companion adversarial counter-check still required before closing pass: **pending**.
9. Next frontier re-derived provisionally: **Records vertical completeness/adversarial consolidation**.

Pass is ready for adversarial counter-check.