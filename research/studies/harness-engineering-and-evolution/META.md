# Harness Engineering and Evolution — Metadata

- **Study ID/type:** harness-engineering-and-evolution / hybrid.
- **Status:** ACTIVE/PARTIAL; U00, U01-A/B, U02-A/B, U03-A/B/C and U04 complete at distinct bounded depths. Plan v0.9; U05 is next logical phase after return/user direction. [STATE](STATE.md) controls current work.
- **Started:** 2026-09-12. **Updated:** 2026-09-16.
- **Research objects:** Harness Engineering Masterclass video (`mQfTdNVCOB0`), Meta-Harness paper (`2603.28052v1`), operational composition and evidence-driven harness change.
- **Primary question:** How are information, tools, state and control formed into a working system, and under which evidence, evaluation and authority conditions may that system change?

## Distinct role and current results

The older context–memory–harness package concerns problem-domain boundaries. This study follows source/experience → candidate → execution → observation → selection → qualified change. Neither the chapter list nor a benchmark winner is adopted as architecture.

U01-A/B preserve classification and TerminalBench source chains and limited TB diagnostics: code/result identity, coverage, effective configuration, caller-specific checks, observation fidelity and protocol-versus-effect. Their original execution limits remain in their evidence directories.

U02-A covers instruction discovery/loading, eligible source-to-request transfer, context management versus caching, tool admission versus effect, executor-scoped containment and persistence versus safe replay/current authorization. [Note08](notes/08-INSTRUCTIONS-AND-WORKING-CONTEXT.md) → [Note09](notes/09-TOOL-REQUESTS-AND-EXECUTION-BOUNDARIES.md) → [Note10](notes/10-DURABLE-STATE-AND-QUALIFIED-CONTINUATION.md).

U02-B adds lifecycle/event scope, delegated work versus conversation control, actual worker context/procedure loading, evidence tied to the checked artifact, trace versus diagnosis and qualified evolution. [Note11](notes/11-ORCHESTRATION-DELEGATION-AND-PROCEDURES.md) → [Note12](notes/12-VERIFICATION-OBSERVABILITY-AND-QUALIFIED-EVOLUTION.md). All ten responsibilities and the separate loop have bounded treatment, not a universal causal map.

U03-A adds a classification experiment/comparator audit: selected-policy versus search performance, heterogeneous transfer, comparator-relative context savings, original MCE/GEPA/ACE mechanisms and metric/call/unit identity. Positive reported results and historical recovery limits remain together. [Note13](notes/13-CLASSIFICATION-EXPERIMENT-AND-COMPARATOR-AUDIT.md) → [SOURCES](evidence/2026-09-15-u03a-classification/SOURCES.md) / [REVIEW](evidence/2026-09-15-u03a-classification/REVIEW-AND-LIMITS.md).

U03-B adds math-specific policy and exposure analysis: four lexical routes; stored corpus versus eligible/presented context; native dataset-quality fields and proof grading; all-model versus four-model transfer comparison; pre-solve routing versus optional adaptive retrieval. Positive no-retrieval transfer is retained alongside a near-tied dense comparison on models not used in search. [Note14](notes/14-MATH-RETRIEVAL-EXPERIMENT-AUDIT.md) → [SOURCES](evidence/2026-09-16-u03b-math/SOURCES.md) / [REVIEW](evidence/2026-09-16-u03b-math/REVIEW-AND-LIMITS.md).

U03-C adds coding run/lineage separation, inherited KIRA versus added environment preparation, repeated-task versus new-task evidence, and a pinned task request/verifier/reward chain. Proposer diagnosis, worker completion, measured outcome and accepted change stay separate. The selected 19-task demo is not the full-benchmark run. [Note15](notes/15-CODING-EXPERIMENT-AND-COMPARATOR-AUDIT.md) → [SOURCES](evidence/2026-09-16-u03c-coding/SOURCES.md) / [REVIEW](evidence/2026-09-16-u03c-coding/REVIEW-AND-LIMITS.md). Local arithmetic is not experimental validation.

U04 combines the native responsibilities and outer search in an operating/change synthesis. It distinguishes current work-state updates, maintained knowledge and executable policy; preserves claim-specific evidence at handoffs; and adds an explicitly analytical acceptance/materialization/actual-consumer boundary. Selective GSTACK and HERMES cases make the latter distinctions concrete. The three experiment families are not merged into one efficacy verdict. [Note16](notes/16-OPERATING-ARRANGEMENT-AND-QUALIFIED-CHANGE-SYNTHESIS.md) → [Note17](notes/17-CROSS-STUDY-COMPARISON-AND-RESEARCH-REUSE.md) → [SOURCES](evidence/2026-09-16-u04-synthesis/SOURCES.md) / [REVIEW](evidence/2026-09-16-u04-synthesis/REVIEW-AND-LIMITS.md).

## Potential reuse

**Foundation:** Information (source/view status, evidence, applicability and uncertainty); Work (admission, progress, comparison and continuation); Actors (ownership, authority, consumer-relative applicability and accepted change); Environment (actual executor, model and prerequisites). These remain provisional many-to-many retrieval hints, not taxonomy membership.

**SOUL:** candidate mechanisms, selection criteria, falsifiers, exclusions and prerequisite questions for work-specific system formation/change; research need not become a prompt or dependency. U03 supplies experiment-design pressure. U04 connects operating work, diagnostic experience, candidate selection and actual use without assuming that every failure needs another component. The paper's research-input suggestion remains engineering advice, not measured SOUL benefit. **Development OS:** exact artifact/evidence/constraint handoff, qualified continuation, accepted-versus-materialized change and actual consumption. No implementation ownership or operating rule changes.

**Reuse modes/stages:** mechanism reference, design pressure, counterexample, experiment-design input and later architecture-facing comparison. Revisit when task mix, client, model, evaluator, procedure, dependency or authority makes qualification load-bearing. Limited or rejected mechanisms remain useful research.

## Pins and validation limits

Framework: `stanford-iris-lab/meta-harness@0cbc31e97c9e6d24232d1dc754827c02e1ec415c`; current-main equality last rechecked in U03-B. Selected coding artifact: `stanford-iris-lab/meta-harness-tbench2-artifact@57fefdb2ff84af3fd81b69d67814acbe69bd0743`. Narrow Harbor source: `527d50deb63a5d279e8c20593c18a2cbc7f61f9e`. Paper v1 is historical, not today's leaderboard. U03-C adds KIRA README at `652dacbf14d29ea93a83c496ee91e0e5ba286721` and one task's files at `harbor-framework/terminal-bench-2@69671fbaac6d67a7ef0dfec016cc38a64ef7a77c`; neither establishes the original run's exact dependency closure.

U01-B executed copied excerpts and an exact shell with fake commands, not full upstream modules/live tasks. Parent-file/host/historical/independent-verification limits persist; U01-A's unrun checks remain unrun. [U01-B CHECKS](evidence/2026-09-12-u01b-terminalbench/CHECKS.md).

U02-A/B's documentation, supplied SRT and selected media checks remain scoped in their evidence directories. Full audio alignment, native caption provenance and current-runtime efficacy remain open. Web pages are dated views, not immutable source identities. No new media work occurred in U03/U04.

U03-A/B/C use selected exact-version paper/method sections, primary source contracts and descriptive arithmetic. Historical adapters, candidate/sample lineage, paired results, independent searches and complete cost/measurement correspondence remain unrecovered. Math scorer/corpus transformations and coding historical run/verification identities stay open. U03-C's arithmetic-oracle typo and correction are recorded in REVIEW.

U04 selectively uses GSTACK at `0d1bd5616c0ef096bb7ccee336f63c60ee408618` and HERMES at `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`. One GSTACK test file was read in full and a HERMES handler range inspected; neither was run. Existing study revalidation is not extended to current upstream behavior. U04 performs no new arithmetic, application test, model, retriever, compiler, installer or benchmark. Its normal/adverse paths are analytical and its review is not independent verification.

## Entry and neighbours

[STATE](STATE.md) → [INDEX](INDEX.md) → [METHOD](METHOD.md)/[PLAN](RESEARCH-PLAN.md). The integrated explanation is now Notes16–17. Return U04; U05 justified probes is next logical phase, with U06 current-project projection and U07 closure still open. No final CORE, adopted architecture, schema, implementation or agent-control change follows. [BRIDGE](BRIDGE-QUESTIONS.md) remains the initial hypothesis set, developed but not converted to architecture by U04.

[The Carbon Layer](../the-carbon-layer/INDEX.md) provides discovery without duplicating this hybrid study. U04's selected GSTACK/HERMES contribution is recorded in Note17; their independent campaign states are unchanged. Related studies remain selectively discoverable through the parent catalog.
