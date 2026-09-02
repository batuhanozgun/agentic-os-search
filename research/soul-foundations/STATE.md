# SOUL Foundations — STATE

**Status:** active research library; four intended independent foundation corpora are sufficiently complete and user-evaluated for the current foundation purpose  
**Repository cleanup/currentness verification:** COMPLETE on 2026-09-02  
**Current authorised substantive activity:** four-foundation adequacy inquiry — test whether Records, Work, Actors and Technical Work Environment provide a sufficient top-level analytical/problem-ground decomposition for later SOUL and Development OS reasoning  
**Current step:** frame the adequacy test with the user before broad comparative research; do not assume the four-area hypothesis is true  
**Current return condition:** reach a bounded, evidence-backed judgment on adequacy/coverage/separability/productive-decomposition and return it to the user before opening lower-level SOUL/Development OS design branches

## Dependency state

- **Layer 0 — bounded context / prior-repository reconstruction:** COMPLETE for current purpose in `research/soul-context/`.
- **Records / persistent information:** SUFFICIENTLY COMPLETE; USER-EVALUATED; READING PACKAGE CLOSED.
- **Work:** SUFFICIENTLY COMPLETE; USER-EVALUATED; RETRIEVAL CLOSURE COMPLETE.
- **Actors:** SUFFICIENTLY COMPLETE; USER-EVALUATED; RETRIEVAL CLOSURE COMPLETE.
- **Technical Work Environment / Teknik Çalışma Ortamı:** SUFFICIENTLY COMPLETE; USER-EVALUATED.
- **Earlier broad Environment / operating-world research:** SUPERSEDED FOR THE INTENDED FOURTH-REGION PURPOSE; archived as historical research only.
- **Cross-foundation adequacy inquiry:** AUTHORISED on 2026-09-02; current framing question is whether the four intended corpora are sufficient and productive as top-level analytical/problem grounds for later SOUL and Development OS work.
- **SOUL/Development OS architecture, final ontology/data model, implementation:** NOT AUTHORISED.

## Adequacy inquiry

### Current question

> Do Records, Work, Actors and Technical Work Environment provide a sufficient and productive top-level analytical/problem-ground decomposition for reasoning about later SOUL and Development OS structure, or does the evidence require a different decomposition, an additional first-order region, or a distinct relation/control plane?

### Working success criteria

The four-area hypothesis is not accepted merely because important examples can be fitted into the four labels.

The inquiry must test at least:

1. **Coverage / adequacy:** can decision-critical SOUL and Development OS problem families be expressed within the four areas or genuinely relationally among them without hiding a distinct first-order region?
2. **Separability:** do the four areas carry meaningfully distinct questions, or is one reducible to another / better represented differently?
3. **Productive decomposition:** does each area open coherent lower-level research/design questions rather than merely serving as a broad bucket?
4. **Rival decomposition:** is there a materially better top-level split?
5. **SOUL vs Development OS independence:** a decomposition may be adequate for one and inadequate for the other; do not force a shared answer.

### Evidence strategy

The first problem inventory should be extracted **without using the four current labels as the organizing frame**. Only after the inventory exists should it be mapped against Records / Work / Actors / Technical Work Environment and their relations.

Use distinct evidence roles:

- `research/soul-context/repos/soul/` — current explicit SOUL intent and Development OS first-party evidence;
- `research/soul-context/repos/os-architect/` — historical lived failures, work-discipline problems, owner corrections and KEEL-development experience;
- `research/soul-context/repos/keel/` — concrete predecessor mechanisms and the failure/problem pressures they attempted to address;
- `research/soul-context/repos/keel-research/` — bounded predecessor prior-art only when relevant; not SOUL authority;
- four current independent foundation corpora — tested only after unconstrained problem extraction, not used to seed the initial problem inventory;
- external/independent cases or literature — used as holdouts/counterexamples where needed so the adequacy judgment does not become circular within one project lineage.

Predecessor mechanisms are evidence of experienced problems and attempted solutions, **not privileged architecture defaults**. SOUL's current documents are first-party evidence of intent and known requirements, but cannot by themselves prove the completeness of the four-area decomposition. KEEL/os-architect/SOUL share lineage and therefore can share omissions; cross-lineage challenge remains necessary for a strong adequacy judgment.

### Current methodological guardrail

Do not begin by asking `where does this fit among the four?`.

Begin by asking:

> What first-order problems must a system like SOUL or a development system like Development OS be able to reason about, govern, preserve, perform, constrain, observe, verify, recover from or adapt to?

Then test the four-area hypothesis against the independently produced problem set.

## Current independent foundation library

### Records / persistent information

Canonical vertical:
- `01_verticals/records-artifacts/`

Current synthesis:
- `01_verticals/records-artifacts/synthesis/RECORDS-VERTICAL-SYNTHESIS.md`

The research is user-evaluated, its reading package is closed, and its vertical-local state does not carry parent-level next-work authorization.

Reopen only on explicit direction or a material later falsifier.

### Work

Canonical vertical:
- `01_verticals/work/`

Current synthesis:
- `01_verticals/work/synthesis/WORK-VERTICAL-SYNTHESIS.md`

The research remains bounded-complete, user-evaluated and available for selective recovery.

### Actors

Canonical vertical:
- `01_verticals/actors/`

Current synthesis:
- `01_verticals/actors/synthesis/ACTORS-VERTICAL-SYNTHESIS.md`

The research remains bounded-complete, user-evaluated and available for selective recovery.

### Technical Work Environment

Canonical vertical:
- `01_verticals/work-environment/`

Current synthesis:
- `01_verticals/work-environment/synthesis/WORK-ENVIRONMENT-VERTICAL-SYNTHESIS.md`

Strongest bounded result:

> **A Technical Work Environment is a bounded realized technical support context in which a selected set of capabilities, services, resources and interfaces are effectively available under particular constraints, configuration and current state. It may, but need not, have an explicit profile/definition.**

The research does not require an intrinsic `Environment` object class. A later representation may be relational/compositional while the technical-environment problem remains first-order.

## Superseded operating-world research

The earlier broad Environment pass researched a different question: a boundary-relative operating world/external-state problem.

That corpus is preserved byte-for-byte under:
- `history/superseded/operating-world-environment/corpus/`

Archive interpretation:
- `history/superseded/operating-world-environment/ARCHIVE-NOTICE.md`

Archived corpus tree SHA:
- `93fe3fc6810b6f6472539583e46144db2803ce17`

This matches the former active Environment tree at archival time.

It is not one of the four current intended foundation corpora and must not be used as evidence for the Technical Work Environment result.

## Historical handoffs

Point-in-time transition/handoff files are archived under:
- `history/handoffs/`

They preserve what was current at those checkpoints. Their internal `current` language is historical and does not override this state.

There is **no current parent handoff**. Current parent authority is `STATE.md` plus routing through `INDEX.md`.

## Cleanup / currentness verification closure

The 2026-09-02 cleanup was performed to prevent fresh-session drift between current research state and historical repository state, without deleting substantive research history.

Verification established:

1. `research/soul-foundations/` root contains only current parent surfaces plus `00_context/`, `01_verticals/` and `history/`;
2. active `01_verticals/` contains exactly the four intended corpora: `records-artifacts/`, `work/`, `actors/`, `work-environment/`;
3. the superseded broad Environment corpus is absent from active verticals and preserved byte-for-byte in history;
4. historical parent handoffs are absent from the current root and live only under `history/handoffs/`;
5. Records, Work, Actors and Technical Work Environment local states no longer carry stale parent next-work/evaluation authority;
6. Work, Actors, Records and Technical Work Environment currentness manifests/revision bindings were checked against current repository blob SHAs after the cleanup; all bound current surfaces matched at closure;
7. Technical Work Environment evidence ledgers were moved under `evidence/sources/` with their original blob identities preserved;
8. historical/orientation/audit surfaces that remain within active vertical packages are explicitly classified as historical/audit/plan rather than preferred current conclusions;
9. no known current route depends on the removed active `environment/` path or a current parent handoff.

Repository code-search results were used only as a supplementary stale-reference probe, not as the sole verification method, because external/search indexes can lag repository state.

**Closure judgment:** no known repository-currentness drift remains on the canonical fresh-session route at this checkpoint.

This is a repository-state/currentness judgment, not independent verification of the substantive research findings themselves.

## Current epistemic position

Established at independent-research level:
- the bounded results preserved inside each of the four active vertical corpora;
- each vertical's explicit verification/source limitations.

Not established merely by completing those corpora:
- that the four labels are exhaustive ontology classes;
- that they are mutually exclusive modules;
- that one cross-foundation relation/control/coordination fabric is the correct next model;
- that the same concrete structures recur across Development OS, SOUL and task-specific systems;
- any final SOUL or Development OS architecture, schema or implementation.

Historical cross-foundation statements about recurrence, relation/control/coordination or the old broad Environment remain hypotheses/inferences unless later explicitly re-evaluated against the current four intended corpora.

## Retrieval/currentness rule

For current parent-level orientation:

`STATE.md → INDEX.md → required active vertical INDEX → KEY/FINDINGS-MAP → descend only as needed`

Do not enter `history/` unless historical/audit recovery is intentional.

## Next logical work

Within the authorised adequacy inquiry, the next logical work is to construct an unconstrained SOUL problem inventory and an unconstrained Development OS problem inventory from current first-party intent, predecessor lived failures/mechanisms and independent challenge evidence, without organizing the inventory under the four current foundation labels. The inventories should then be mapped against the four areas and their genuine relations, followed by missing-region/reduction/rival-decomposition stress tests.

## Next authorised work

**Four-foundation adequacy inquiry only.**

Do not yet open lower-level SOUL/Development OS architecture, final ontology/data-model design or implementation. Do not treat predecessor repository organization or current four foundation labels as architecture defaults.