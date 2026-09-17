# Work Management / Project Control — STATE

## Authority

This file is the authoritative package-local current-work state for `work-management-project-control`.

User authorization on 2026-09-17: plan the research program, process candidate repositories sequentially, and reflect the work durably in the research repository. This authorization does **not** authorize Foundation mutation, SOUL/Development OS architecture decisions, product adoption or installation.

## Current status

**ACTIVE / U01–U04 BOUNDED-COMPLETE; U05 SPEC KIT NEXT**

OpenProject provides the classical project/work-package baseline; Flowable provides durable process/case/decision execution; Beads provides an agent-native dependency/frontier/claim model; OpenSpec provides an artifact-dependency/living-plan model. The next unit is GitHub Spec Kit.

## Completed

### U00 — Program framing and method setup

- bounded research object defined: large-work / project-control methodology rather than “pick a project-management product”;
- study classified as `focused-topic`;
- common comparison matrix defined in `METHOD.md`;
- first-wave targets selected to maximize methodological diversity rather than feature-count repetition;
- sequence and revision rules recorded in `PLAN.md`;
- prior studies identified as comparison inputs without treating them as canonical work ontology.

### U01 — OpenProject — BOUNDED-COMPLETE

Durable external-target package: `../openproject/`.

Key source-bounded findings:
- WorkPackage separates lifecycle, type, assignment/responsibility, schedule and history.
- hierarchy, temporal dependency, closure blocking and semantic relations are distinct mechanisms;
- manual/automatic scheduling separates relation existence from active control;
- type×role workflow controls allowed state transitions and reopening;
- Project/Program/Portfolio distinguish operational and strategic aggregation.

### U02 — Flowable — BOUNDED-COMPLETE

Durable external-target package: `../flowable/`.

Key source-bounded findings:
- BPMN durable process execution persists at waits and composes human/system activity;
- CMMN exposes condition/event/manual-activation case control with a richer plan-item lifecycle;
- DMN separates repeatable decision policy from execution flow;
- migration/retry/suspend/cancel/terminate/compensate are different forms of revision/recovery;
- recorded state and engine-executed transition are distinct categories.

### U03 — Beads — BOUNDED-COMPLETE

Durable external-target package: `../beads/`.

Key source-bounded findings:
- actionable ready work is derived rather than synonymous with open status;
- source has richer readiness-affecting dependency semantics than simplified repo documentation;
- discovery provenance is distinct from prerequisite blocking;
- claim is race-safe and separate liveness lease/heartbeat supports dead-worker recovery;
- reopen recomputes downstream blocking; durable graph state lives in Dolt.

### U04 — OpenSpec — BOUNDED-COMPLETE

Durable external-target package: `../openspec/`.

Source-bounded findings at `Fission-AI/OpenSpec@bae58cf61479986431bb798acbe5a688a591c18c`:

- a change is represented through differentiated planning artifacts, not one task record;
- workflow schemas define a validated artifact DAG; artifact readiness means planning dependencies are materialized;
- `apply.requires` creates a separate implementation-readiness boundary, and tracked tasks create blocked/ready/all-done apply progress;
- artifact `done` is primarily materialization/file-existence, not semantic acceptance;
- proposal/spec/design/tasks remain editable during implementation; tasks are a living checklist;
- code/artifact drift is explicitly reconciled before archive, where proposed deltas can become current-spec truth;
- the work method/schema is configurable and distinct from a change instance.

See `../openspec/FINDINGS.md` and `../openspec/SOURCE-LEDGER.md`.

## First-wave unit queue

1. **U01 — OpenProject** — **COMPLETE**
2. **U02 — Flowable** — **COMPLETE**
3. **U03 — Beads** — **COMPLETE**
4. **U04 — OpenSpec** — **COMPLETE**
5. **U05 — Spec Kit** — **NEXT** — specification → plan → tasks → implementation/convergence loop.
6. **U06 — Leantime** — strategy/goals → milestones/projects/tasks → execution and retrospective surfaces.
7. **U07 — Gas Town** — multi-agent work allocation, persistent work state and large-scale coordination.
8. **U08 — Cross-unit synthesis** — compare mechanism families without forcing a winner or universal ontology.
9. **U09 — Gap-driven second wave** — only if first-wave synthesis exposes missing coverage.
10. **U10 — Bounded closure / evaluation checkpoint**.

## Conditional second-wave candidates

Not yet activated as full units; activate only for a demonstrated coverage gap:

- ERPNext — enterprise/ERP project, resource, cost and operational integration;
- Camunda — process orchestration and human/system task execution;
- Plane — modern issue/cycle/triage model and agent-access surface;
- Redmine — mature issue relation/subtask/workflow baseline;
- Taiga — Scrum/Kanban/agile work-state baseline;
- Huly — unified project/document/communication workspace;
- TASKS.md or another minimal file-native agent queue — minimum viable shared-work representation.

## Method learning after U01–U04

Ten distinctions are now load-bearing:

1. **relation identity ≠ control effect**;
2. **recorded state ≠ executed transition**;
3. **backtracking is a family, not one transition**;
4. **lifecycle status ≠ derived actionable standing**;
5. **claim/assignment ≠ holder liveness**;
6. **work-discovery provenance ≠ prerequisite relation**;
7. **work item ≠ work artifact**;
8. **materialized artifact ≠ semantically accepted/current artifact**;
9. **planning readiness ≠ implementation readiness ≠ implementation completion**;
10. **work method/schema can be an explicit object distinct from the work instance**.

Later units should preserve these distinctions rather than normalizing every system into task/status/dependency.

## Unit completion contract

Before a unit can be marked source-bounded complete:

1. current upstream target and default branch/release are revalidated;
2. a concrete ref/version/date is recorded;
3. the target's own ontology is recovered before mapping it to our terms;
4. evidence covers the relevant method dimensions, not only README feature claims;
5. state/dependency/ownership/change/recovery semantics are distinguished where present;
6. “what this does not establish” is written explicitly;
7. relevant existing studies are compared selectively, not projected onto the target;
8. package/catalog state is updated before moving to the next unit.

## Current next action

Begin **U05 GitHub Spec Kit**. Recover its native specification-driven lifecycle, constitution/spec/plan/tasks boundaries, how tasks are generated and grouped, how implementation discovers or reconciles missed work, what “convergence” means in current source/docs, and whether phase sequencing is enforced, advisory or agent-procedural. Contrast with OpenSpec without adopting either project's self-comparison claims.

## Fresh-session recovery

A new session should read:

1. `META.md`
2. this `STATE.md`
3. `METHOD.md`
4. `PLAN.md`
5. completed target package(s) only when comparison requires them: `../openproject/`, `../flowable/`, `../beads/`, `../openspec/`.

Then resume the first unfinished unit listed above. Do not infer completion from files merely existing.
