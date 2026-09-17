# Work Management / Project Control — STATE

## Authority

This file is the authoritative package-local current-work state for `work-management-project-control`.

User authorization on 2026-09-17: plan the research program, process candidate repositories sequentially, and reflect the work durably in the research repository. This authorization does **not** authorize Foundation mutation, SOUL/Development OS architecture decisions, product adoption or installation.

## Current status

**ACTIVE / U01 OPENPROJECT BOUNDED-COMPLETE; U02 FLOWABLE NEXT**

The program framing and common comparison method are established. OpenProject has been completed as the first classical project-control baseline at pinned ref `f531cc348d6920dd6d02f9b395f90878db57b3d3`. The next research unit is Flowable.

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

Source-bounded findings established at `opf/openproject@f531cc348d6920dd6d02f9b395f90878db57b3d3`:

- WorkPackage is the main operational work object and separates type, status, author, assignee, responsible actor, schedule and history surfaces.
- Parent/child decomposition is distinct from ordinary work-package relations.
- Relation types carry different control effects: temporal predecessor/successor, closure blocker, duplicate propagation and non-enforcing semantic relations are not one generic dependency.
- Manual versus automatic scheduling separates relation existence from active schedule enforcement.
- Status transition authority is configurable by work-package type × role, with author/assignee-specific additions; reverse transitions/reopen are normal when configured.
- Project / Program / Portfolio composition separates operational execution from strategic visibility/coordination.
- No single canonical “ready frontier” was found in this slice; readiness/control is distributed across workflow, blockers and schedule constraints.

See `../openproject/FINDINGS.md` and `../openproject/SOURCE-LEDGER.md`.

## First-wave unit queue

1. **U01 — OpenProject** — **COMPLETE** — classical project/work-package baseline.
2. **U02 — Flowable** — **NEXT** — BPMN / CMMN / DMN; predefined process versus adaptive case work versus explicit decision logic.
3. **U03 — Beads** — agent-native dependency graph, blockers and ready frontier.
4. **U04 — OpenSpec** — artifact/work dependency graph and progressive spec-driven enablement.
5. **U05 — Spec Kit** — specification → plan → tasks → implementation/convergence loop.
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

## Method learning after U01

The initial comparison matrix survives U01, but one distinction is now explicitly load-bearing for later units:

**relation identity ≠ control effect.**

OpenProject shows that hierarchy, semantic relation, scheduling dependency and closure blocking can be represented as different edge families, and even a temporal relation may remain present while manual scheduling disables its date-control effect. Later units should therefore record both the relation and the effect/enforcement semantics.

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

Begin **U02 Flowable**. First recover the native boundary between BPMN process instances, CMMN cases/case plans and DMN decisions before mapping any of them onto “project/task/workflow” vocabulary. Pay particular attention to adaptive work, human tasks, wait/event states, cancellation/termination/compensation and persisted engine state.

## Fresh-session recovery

A new session should read:

1. `META.md`
2. this `STATE.md`
3. `METHOD.md`
4. `PLAN.md`
5. completed target package(s), beginning with `../openproject/META.md`, only when comparison requires them.

Then resume the first unfinished unit listed above. Do not infer completion from files merely existing.
