# SOUL Foundations — STATE

**Status:** active research library; independent discovery corpora are closed; refined top-level adequacy result is user-evaluated and accepted as the current working research hypothesis; ground-deepening research program is planned  
**Repository cleanup/currentness verification:** COMPLETE on 2026-09-02; acceptance/next-stage routing refreshed on 2026-09-02  
**Current authorised substantive activity:** USER EVALUATION / REFINEMENT of the `03_ground-deepening` plan only  
**Current return condition:** user accepts/refines the ground-deepening plan and chooses whether/where to authorize the first substantive ground pass

## Dependency state

- **Layer 0 — bounded context / predecessor reconstruction:** COMPLETE for current purpose in `research/soul-context/`.
- **Independent discovery research (`01_verticals/`):** COMPLETE / USER-EVALUATED for the original bounded questions.
  - Records / persistent information: closed.
  - Work: closed.
  - Actors: closed.
  - Technical Work Environment: closed.
- **Top-level adequacy / hierarchy inquiry (`02_adequacy/`):** BOUNDEDLY SUFFICIENT; USER-EVALUATED / ACCEPTED AS WORKING RESEARCH HYPOTHESIS.
- **Ground-deepening stage (`03_ground-deepening/`):** PLAN READY / AWAITING USER EVALUATION; substantive research not started.
- **Cross-ground relation/control composition:** NOT AUTHORISED.
- **SOUL/Development OS architecture, final ontology/data model, implementation:** NOT AUTHORISED.

## Accepted top-level working research hypothesis

The project will proceed under the working hypothesis that the principal top-level problem grounds for later SOUL and Development OS reasoning are:

```text
Environment / Operating Reality                 [working label]
    ├─ Operating World / Work Domain
    └─ Work-Support Environment
         └─ Technical Work Environment

Information / Representation State
    └─ Records / Persistent Information

Work

Actors / Agency–Participation–Authority

+ typed relations / control / transitions across grounds
```

This is a **research-routing hierarchy**, not architecture, final ontology, schema or a claim of universal exhaustiveness.

Acceptance means only that this is the current best frame under which deeper research will be planned and later tested.

## Meaning of `01_verticals/`

`01_verticals/` preserves the completed **independent discovery studies** that generated the evidence base:

- `records-artifacts/`
- `work/`
- `actors/`
- `work-environment/`

These are not now assumed to be the final four top-level grounds.

Current level alignment is:

```text
Information / Representation
    └─ Records / Persistent Information          ← existing deep corpus

Environment / Operating Reality
    └─ Work-Support Environment
         └─ Technical Work Environment           ← existing deep corpus

Work                                             ← existing broad/deep corpus
Actors                                           ← existing broad/deep corpus
```

The old corpora remain stable evidence packages and should not be renamed/reorganized merely to mirror the new hierarchy.

## Meaning of `02_adequacy/`

`02_adequacy/` is the comparative/adequacy layer that tested whether the independent discovery studies were collectively sufficient and correctly level-aligned.

It established the current working hierarchy by:
- extracting SOUL/Development OS problem families before fitting them to the original labels;
- testing coverage, separability, reduction and rival decompositions;
- identifying the broader Information / Representation ground above Records;
- identifying Operating World / Work Domain as a missing problem;
- testing and revising five-peer versus one Environment-parent hierarchy;
- using cross-lineage holdouts and adversarial omission tests;
- preserving relation/control as cross-ground composition fabric rather than a peer bucket.

Its current result is accepted as a **working research hypothesis**, not as architecture truth.

## Meaning of `03_ground-deepening/`

`03_ground-deepening/` is the planned stage for bringing each accepted top-level ground to sufficient internal research scope/depth.

Current planning surfaces:
- `03_ground-deepening/STATE.md`
- `03_ground-deepening/PLAN.md`
- `03_ground-deepening/INDEX.md`
- `03_ground-deepening/CURRENT-SURFACES.md`

The plan standardizes **quality gates**, not semantic layer counts.

For each ground:
1. recover existing evidence;
2. test level/boundary adequacy;
3. derive a ground-specific decomposition;
4. deepen only materially under-supported branches;
5. record but do not prematurely solve cross-ground relations;
6. run adversarial omission/reduction tests;
7. close only after user evaluation.

## Current expected asymmetry

### Environment
Likely high-intensity new research. Parent-level/Operating-World semantics require independent deepening. Existing Technical Work Environment and archived operating-world research are major prior evidence, but neither automatically completes the parent ground.

### Information
Likely high-intensity new research. Broader Information / Representation semantics above persistent Records require a substantial first-principles pass. Existing Records research is preserved as the deep persistence branch.

### Work
Existing Work corpus already addresses the top-level ground directly and deeply. Begin with a coverage/gap audit under the accepted hierarchy; reopen substantive research only if material Work-local gaps appear.

### Actors
Existing Actors corpus already addresses the top-level ground directly and deeply. Begin with a coverage/gap audit; reopen substantive research only if material Actors-local gaps appear.

## Recommended plan order

Current recommendation by expected information gain:

1. Environment;
2. Information;
3. Work coverage/gap audit;
4. Actors coverage/gap audit.

This is a recommendation, not an irreversible dependency or current authorization to start Environment.

## Cross-ground relation rule

Ground deepening is no longer blind to other grounds.

Relations needed to define local boundaries or failure cases may be used and recorded. However, systematic typed relation/control/composition research remains a later phase.

A cross-ground question alone is not sufficient reason to reopen a ground-local corpus.

## Phase boundary

```text
01  independent discovery research                 COMPLETE
02  top-level adequacy / hierarchy discovery        COMPLETE + USER-ACCEPTED WORKING HYPOTHESIS
03  ground-specific scope/depth completion          PLAN READY; AWAITING USER EVALUATION
04  cross-ground relations / composition            LOGICAL LATER CANDIDATE; NOT AUTHORISED
05  SOUL / Development OS architecture derivation   LOGICAL LATER CANDIDATE; NOT AUTHORISED
```

Numbers 04 and 05 are planning labels only, not committed repository phases or authorised work.

## Epistemic guardrails

- Completed research ≠ independent verification.
- Same-model completeness checks are adversarial self-review, not independent verification.
- Research grounds ≠ ontology classes/modules/components.
- A concrete thing may participate in several grounds under different roles.
- Next logical work ≠ next authorised work.
- The four-ground hypothesis must remain reopenable if deeper research exposes forced fit, leakage or a materially stronger rival decomposition.

## Current retrieval

Parent currentness:

`STATE.md → INDEX.md`

Independent discovery evidence:

`01_verticals/<package>/INDEX or KEY → FINDINGS-MAP → synthesis → focused finding → audit/source recovery`

Accepted adequacy result:

`02_adequacy/STATE → KEY/FINDINGS-MAP → synthesis/ADEQUACY-SYNTHESIS → focused finding → current audit/source recovery`

Ground-deepening plan:

`03_ground-deepening/STATE → PLAN → INDEX → CURRENT-SURFACES`

## Next authorised work

**USER EVALUATION / REFINEMENT OF THE `03_ground-deepening` PLAN ONLY.**

Do not automatically begin substantive Environment, Information, Work or Actors research, relation/control composition, SOUL/Development OS architecture, ontology/data-model work or implementation until the plan is accepted and the next ground is explicitly authorised.
