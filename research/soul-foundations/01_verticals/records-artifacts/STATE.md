# Records / Persistent Information — STATE

**Status:** active vertical; organisation/retrieval pass return condition met  
**Parent:** `research/soul-foundations/`  
**Last updated:** 2026-09-01  
**User-return gate:** YES

## Current objective

Establish a first-principles, source-grounded understanding of the persistent-information / Records problem domain before relating it to Work, Actors, the SOUL Development System, or SOUL architecture.

The package directory remains `records-artifacts/` for continuity. `Artifact` is not treated as an unqualified foundational Records category.

---

# Completed research passes

1. **Foundational Records / persistent-information** — recordhood/problem structure; rejected storage-first framing.
2. **Object boundaries / artifact / identity-change** — separated resource, record role, version, representation, derivation and aggregation; rejected unqualified `artifact` as super-category.
3. **Minimum envelope → minimum preservation closure** — rejected universal object-local metadata bundle; established profile-relative information/dependency closure.
4. **Change / status / temporal semantics** — rejected generic `update`, one universal status and one universal timestamp model; established architecture-neutral reconstructability semantics.
5. **Organisation / derived views / retrieval semantics** — rejected one canonical hierarchy and one generic `search` notion; established plural organisation roles and claim-relative retrieval sufficiency.

## Pass 5 outputs

- plan: `ORGANISATION-RETRIEVAL-PLAN.md`
- synthesis: `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md`
- adversarial check: `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md`
- source ledger: `sources/organisation-retrieval-semantics.md`

---

# Current bounded result

## Organisation is purpose-relative

Do not automatically collapse:

- context/provenance-preserving organisation;
- descriptive / knowledge organisation;
- access / retrieval organisation;
- exact source/version/standing binding.

These are semantic roles, **not mandatory separate stores/components**. A simple profile may combine roles where no protected distinction is lost.

Multiple organisations are permitted but not required. A resource may participate in several contextual, subject, aggregate or access structures without becoming several source records merely because it appears in several views.

## `Canonical vs derived` was too binary

Current Records-side model distinguishes:

- derivation relation;
- access/discovery function;
- own resource/record identity;
- recordkeeping/designated-source role;
- exact source/version/standing binding;
- freshness/coverage semantics.

A derived output can itself become a persistent resource/record or designated recordkeeping source for a bounded role. Authority to establish such designation remains deferred.

## Retrieval is claim-relative

Different retrieval needs require different closure, including:

- known-item / exact identity;
- structured filter;
- semantic/topical discovery;
- exhaustive/high-recall retrieval;
- current-standing retrieval;
- historical/as-of retrieval;
- system-known-as-of retrieval;
- provenance/derivation traversal;
- aggregation/case/thread reconstruction.

A hit does not by itself establish exact identity, current standing, completeness, authority, truth or evidential sufficiency.

A miss does not by itself establish absence. Strong absence inference becomes possible only when corpus/domain, coverage, matching sensitivity, aliases/identity scope, freshness/as-of and recall are sufficiently bounded.

## Derived-view freshness

Source change and access-view visibility are separate facts unless a profile guarantees otherwise.

Staleness is not inherently wrong. The failure is **freshness/as-of semantics mismatching the claim**. Historical snapshots are intentionally non-current; current-sensitive retrieval needs an adequate assurance path to current standing, not necessarily a direct origin lookup.

Freshness can depend on source version/standing, schema/vocabulary version and corpus coverage, not only elapsed time.

## Architecture boundary

No hierarchy/graph/vector/search/database/cache/storage topology has been selected.

Plural relationships do not imply graph architecture; retrieval contracts are conceptual guarantees/assumptions, not API requirements.

---

# Pass 5 return-condition verdict

**MET.**

- context-preserving, descriptive/knowledge and access/retrieval organisation were compared;
- binary canonical/derived framing was replaced with a bounded relational model;
- materially different retrieval modes and sufficiency requirements were distinguished;
- stale/incomplete/lossy/duplicate/independently-editable view failures were tested;
- retrieval hit/miss epistemic limits are explicit;
- standing-change propagation was bounded without synchronous-invalidation architecture;
- adversarial pass challenged over-separation, graph drift, source/derived hierarchy, miss/absence absolutism, stale-view assumptions and IR scope drift;
- source trace and synthesis are persisted;
- no search/storage/SOUL architecture was selected.

This is a research-process checkpoint, **not independent proof of a universal organisation/retrieval model** and not completion of the Records vertical.

---

# Current highest-information unknown

Five passes now establish enough about:

- persistent object/record boundaries;
- minimum preservation closure;
- change/standing/time reconstruction;
- organisation/access views and retrieval semantics.

The next major Records gap is now:

> **How should these conditional findings be turned into purpose-relative Records profiles / requirement-derivation rules so a given resource/use/horizon/risk gets the necessary identity, preservation, history, organisation, retrieval and assurance obligations — without requiring every possible property or prematurely selecting storage architecture?**

See `OPEN-QUESTIONS.md`.

## Next logical work

A bounded **Records profile / requirement derivation** pass.

## Next authorised work

**RETURN TO USER AND RE-ANCHOR DIRECTION.**

Do not automatically execute another long pass.

Before continuation:

1. re-evaluate purpose and direction against all completed passes;
2. define scope/exclusions;
3. define operational return condition;
4. obtain user approval;
5. then work to that return condition without stopping at the first useful finding.

Work, Actors, cross-vertical synthesis, Development System design, and SOUL architecture remain outside the authorised stage.