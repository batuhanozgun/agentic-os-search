# Harness Engineering and Evolution — Metadata

- **Study ID/type:** harness-engineering-and-evolution / hybrid.
- **Status:** ACTIVE/PARTIAL; U00, U01-A/B and bounded U02-A/B complete at different evidence depths. Plan v0.5. [STATE](STATE.md) controls current work.
- **Started:** 2026-09-12. **Updated:** 2026-09-15.
- **Research objects:** Harness Engineering Masterclass video (`mQfTdNVCOB0`), Meta-Harness paper (`2603.28052v1`), operational composition and evidence-driven harness change.
- **Primary question:** How are information, tools, state and control formed into a working system, and under which evidence, evaluation and authority conditions may that system change?

## Distinct role and current results

The older context–memory–harness package concerns problem-domain boundaries. This study follows source/experience → candidate → execution → observation → selection → qualified change. Neither the chapter list nor a benchmark winner is adopted as architecture.

U01-A/B preserve classification and TerminalBench source chains and limited TB diagnostics: code/result identity, coverage, effective configuration, caller-specific checks, observation fidelity and protocol-versus-effect. Their original execution limits remain in their evidence directories.

U02-A covers instruction discovery/loading, eligible source-to-request transfer, context management versus caching, tool admission versus effect, executor-scoped containment and persistence versus safe replay/current authorization. [Note08](notes/08-INSTRUCTIONS-AND-WORKING-CONTEXT.md) → [Note09](notes/09-TOOL-REQUESTS-AND-EXECUTION-BOUNDARIES.md) → [Note10](notes/10-DURABLE-STATE-AND-QUALIFIED-CONTINUATION.md).

U02-B adds lifecycle/event scope, delegated work versus conversation control, actual worker context/procedure loading, evidence tied to the checked artifact, trace versus diagnosis and qualified evolution. [Note11](notes/11-ORCHESTRATION-DELEGATION-AND-PROCEDURES.md) → [Note12](notes/12-VERIFICATION-OBSERVABILITY-AND-QUALIFIED-EVOLUTION.md). The diagnostic matrix is treated as leads, not a unique causal map. All ten responsibilities and the separate loop have bounded treatment; full synthesis and project projection remain open.

## Potential reuse

**Foundation:** Information (source/view status, evidence and uncertainty); Work (admission, progress, effect and continuation); Actors (ownership, authority and accepted change); Environment (actual executor and prerequisites). Composition/feedback/adaptation may matter. These are provisional many-to-many retrieval hints, not taxonomy membership.

**SOUL:** candidate mechanisms, selection criteria, falsifiers, exclusions and prerequisite questions for work-specific system formation/change; research need not become a prompt or dependency. **Development OS:** exact artifact/evidence/constraint handoff, qualified continuation and current authority. No implementation ownership or operating rule is changed.

**Reuse modes/stages:** mechanism reference, design pressure, counterexample, experiment-design input and later architecture-facing comparison. Revisit when a task, client, model, evaluator, procedure, dependency or authority change makes qualification load-bearing. Limited or rejected mechanisms remain useful research.

## Pins and validation limits

Framework: `stanford-iris-lab/meta-harness@0cbc31e97c9e6d24232d1dc754827c02e1ec415c`. Selected artifact: `stanford-iris-lab/meta-harness-tbench2-artifact@57fefdb2ff84af3fd81b69d67814acbe69bd0743`. Narrow Harbor source: `527d50deb63a5d279e8c20593c18a2cbc7f61f9e`. Paper v1 is historical, not today's leaderboard.

U01-B executed copied Python excerpts and an exact shell with fake commands, not full upstream modules or live tasks. Parent-file/host/historical/independent-verification limits persist; U01-A's unrun checks remain unrun. [U01-B CHECKS](evidence/2026-09-12-u01b-terminalbench/CHECKS.md).

U02-A used selected documentation, an abstract, derivative transcript and twelve sampled media frames. [U02-A SOURCES](evidence/2026-09-13-u02a-responsibilities/SOURCES.md). U02-B fully read a newly supplied 714-cue SRT and inspected thirteen selected frames from a newly hashed muxed MP4, alongside selected primary documentation and companion text. No new application behavior was executed; analytical cases are not tests. Full audio alignment, caption provenance and current-runtime efficacy remain open. Web pages are dated views, not immutable code identities. [U02-B SOURCES](evidence/2026-09-15-u02b-coordination/SOURCES.md) / [REVIEW](evidence/2026-09-15-u02b-coordination/REVIEW-AND-LIMITS.md).

Revalidate exact client/runtime/source conditions before load-bearing use. No final CORE, accepted architecture, schema, implementation or agent-control change follows from these units.

## Entry and neighbours

[STATE](STATE.md) → [INDEX](INDEX.md) → [METHOD](METHOD.md)/[PLAN](RESEARCH-PLAN.md). Next: U03 experimental/comparator audit. U04 full synthesis, U05 justified probes, U06 project projection and U07 reverse closure remain open. [BRIDGE](BRIDGE-QUESTIONS.md) is still the initial hypothesis set.

[The Carbon Layer collection](../the-carbon-layer/INDEX.md) provides a video discovery route without duplicating this hybrid study. Related studies remain selectively discoverable through the parent catalog. Their names are not proof of fresh substantive comparison; no other study was newly audited in U02-B.
