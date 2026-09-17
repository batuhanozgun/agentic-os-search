# Work Management / Project Control — PLAN

## Strategy

Research in ordered contrast, not by product popularity. Each unit is chosen because it represents a materially different way of modelling or controlling work. The sequence may change when new evidence exposes a better dependency or a missing prerequisite; any change must be reflected in `STATE.md` with a reason.

## U00 — Program setup — COMPLETE

Outputs:

- `META.md`
- `STATE.md`
- `METHOD.md`
- this plan
- `INDEX.md`
- root catalog/index discovery updates

## U01 — OpenProject — classical project-control baseline

Purpose:

- establish a mature baseline for project, work package, hierarchy/WBS, relations, schedules, milestones and status;
- distinguish work representation from scheduling/control;
- inspect reopen/change/history semantics rather than only board/Gantt UI.

Expected output: separate `openproject` external-target package with pinned source and bounded findings, plus parent-state update.

## U02 — Flowable — process, case and decision control

Purpose:

- separate predefined workflow (BPMN), adaptive/knowledge work (CMMN) and explicit decision logic (DMN);
- inspect execution semantics, human/system tasks, wait states, events, compensation/cancellation and case-plan evolution;
- test whether “project plan” is the wrong abstraction for some work.

## U03 — Beads — dependency graph / actionable frontier

Purpose:

- inspect issue/dependency graph, blockers, ready work, claim/ownership and distributed persistence;
- compare derived readiness with status-column task management;
- connect selectively to `recursive-prerequisite-discovery` without assuming conceptual equivalence.

## U04 — OpenSpec — artifact enablement graph

Purpose:

- inspect artifact dependencies, generation readiness and custom workflow schemas;
- distinguish “dependency as gate” from “dependency as enablement” where source supports it;
- test artifact-production graphs as work-control substrate.

## U05 — Spec Kit — specification-to-convergence lifecycle

Purpose:

- inspect specification, planning, task generation, implementation and convergence/revision loops;
- identify what persists, what is regenerated and how plan/task drift is handled;
- compare planned decomposition with progressive discovery.

## U06 — Leantime — strategy-to-execution chain

Purpose:

- inspect goals/strategy, projects, milestones, tasks, dependencies, risks and retrospectives;
- recover how high-level intent remains connected to execution state;
- add organizational/project-management concepts missing from agent-native systems.

## U07 — Gas Town — multi-agent work coordination

Purpose:

- inspect persistent work state, actor roles, allocation/claim, parallel work, convoys or equivalent coordination primitives;
- distinguish coordination substrate from task representation;
- inspect provenance/recovery and failure behavior for multiple agents.

## U08 — Cross-unit synthesis

Produce a mechanism-oriented synthesis across first-wave units:

- common primitives;
- irreducible differences;
- where tree, DAG, state machine, case plan and artifact graph models break down;
- how readiness, authority, verification, reversal and recovery differ;
- which questions remain unanswered for SOUL / Development OS.

Do **not** rank products or propose architecture unless separately authorised.

## U09 — Gap-driven second wave

Activate only to cover a demonstrated missing dimension. Candidate pool:

- ERPNext — ERP/project/resource/cost integration;
- Camunda — durable process orchestration and human/system execution;
- Plane — issue/cycle/triage plus agent access;
- Redmine — mature issue/workflow/relations baseline;
- Taiga — agile Scrum/Kanban semantics;
- Huly — project + docs + communication unified workspace;
- TASKS.md / similar — minimal file-native human/agent queue.

A candidate enters U09 only with an explicit gap statement such as “first wave does not cover resource-cost control” or “no minimal baseline exists.”

## U10 — Bounded closure

Closure requires:

- every activated unit has a recoverable source ref/date and epistemic boundary;
- common dimensions are compared without silently normalizing incompatible terms;
- gaps and non-findings are explicit;
- parent `STATE.md` records whether the package is review-ready, bounded-complete or still open;
- no Foundation/architecture adoption is inferred from research completion.
