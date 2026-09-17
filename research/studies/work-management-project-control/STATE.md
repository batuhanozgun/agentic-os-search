# Work Management / Project Control — STATE

## Authority

This file is the authoritative package-local current-work state for `work-management-project-control`.

User authorization on 2026-09-17: plan the research program, process candidate repositories sequentially, and reflect the work durably in the research repository. This authorization does **not** authorize Foundation mutation, SOUL/Development OS architecture decisions, product adoption or installation.

## Current status

**ACTIVE / U01–U08 COMPLETE; U09 ERPNext GAP UNIT NEXT**

The first wave is complete and synthesized in `08-CROSS-UNIT-SYNTHESIS.md`. One material gap remains from the user's original SAP-PS-like framing: enterprise resource/cost/accounting/operational integration. ERPNext is activated as the only immediate U09 second-wave target to cover that gap.

## Completed units

- **U00 — Method/program setup** — COMPLETE
- **U01 — OpenProject** — BOUNDED-COMPLETE (`../openproject/`)
- **U02 — Flowable** — BOUNDED-COMPLETE (`../flowable/`)
- **U03 — Beads** — BOUNDED-COMPLETE (`../beads/`)
- **U04 — OpenSpec** — BOUNDED-COMPLETE (`../openspec/`)
- **U05 — GitHub Spec Kit** — BOUNDED-COMPLETE (`../spec-kit/`)
- **U06 — Leantime** — BOUNDED-COMPLETE (`../leantime/`)
- **U07 — Gas Town** — BOUNDED-COMPLETE (`../gastown/`)
- **U08 — Cross-unit synthesis and gap assessment** — COMPLETE (`08-CROSS-UNIT-SYNTHESIS.md`)

## First-wave synthesis result

Six mechanism families are now source-bounded:

1. classical project/schedule control;
2. durable process/case/decision execution;
3. dependency-DAG/actionable-frontier control;
4. artifact-dependency/living-plan control;
5. spec-driven procedural decomposition/convergence;
6. multi-agent orchestration/execution control.

Leantime also adds the strategy→goal→milestone→delivery alignment axis.

The first wave rejects the shortcut “large-work management = task tracking + dependencies.” It shows multiple independent standings and control surfaces: intent, representation, readiness, execution, actor authority/liveness, verification, integration and outcome.

## U09 gap decision

### Activated: ERPNext

Reason: enterprise project control remains under-covered, specifically the binding of project/task structure to:

- people/resource/time records;
- timesheets;
- expenses/costing;
- procurement/material/business operations where applicable;
- billing/revenue/accounting;
- budget/financial standing;
- operational transactions outside the project tracker itself.

### Not activated now

- **Camunda:** Flowable already covers the process/case/decision family for this bounded program.
- **Plane / Redmine / Taiga:** issue/agile work control is sufficiently represented for current open questions by OpenProject, Leantime and Beads.
- **Huly:** unified communication/document workspace is not the demonstrated gap.
- **TASKS.md/minimal queue:** existing Beads + Wayfinder + recursive-prerequisite research is sufficient for the current bounded comparison.

## Load-bearing method distinctions after U01–U08

1. relation identity ≠ control effect;
2. recorded state ≠ executed transition;
3. backtracking is a family, not one transition;
4. lifecycle status ≠ derived actionable standing;
5. claim/assignment ≠ holder liveness;
6. work-discovery provenance ≠ prerequisite relation;
7. work item ≠ work artifact;
8. materialized artifact ≠ semantically accepted/current artifact;
9. planning readiness ≠ implementation readiness ≠ implementation completion;
10. work method/schema can be an explicit object distinct from the work instance;
11. whole-plan state ≠ current-session admitted work slice;
12. requirements-quality approval ≠ implementation task completion;
13. source-directed repair ≠ arbitrary downstream patching;
14. initial-plan completion ≠ convergence with realized state;
15. delivery progress ≠ objective/outcome progress;
16. execution lifecycle standing ≠ strategic trajectory standing;
17. strategic traceability relation ≠ ownership/dependency relation;
18. reasoning/support artifacts ≠ task-state controls unless explicitly wired;
19. work substrate ≠ orchestration substrate;
20. actor identity ≠ runtime session;
21. logical readiness ≠ dispatch admissibility under capacity;
22. work state ≠ scheduling/execution-attempt state;
23. worker completion ≠ aggregate completion ≠ integrated/verified standing;
24. event-driven transition ≠ reconciled derived state;
25. relation meaning / control effect / enforcement point must be recorded separately;
26. completion signal ≠ verified effect ≠ desired outcome.

These are research distinctions, not a proposed SOUL or Development OS schema.

## Current next action

Begin **U09 ERPNext**. Recover its native Project/Task/Timesheet/cost/billing/resource relationships before mapping them to SAP-PS-like concepts. Focus on what project records actually control or aggregate, what accounting/operational transactions merely reference projects/tasks, how costing/billing is derived, how time and people are represented, and which enterprise control concepts remain absent even after ERPNext.

## Closure condition

After U09, perform U10 bounded closure/evaluation:

- update parent synthesis/gap conclusion if ERPNext changes it;
- decide whether any material gap still justifies another target;
- update `META.md`, `PLAN.md`, `INDEX.md`, root `CATALOG.md` / `INDEX.md`;
- mark the parent review-ready/bounded-complete if fresh-session recovery is coherent;
- do not make SOUL/Development OS architecture or adoption decisions.

## Fresh-session recovery

Read `META.md` → this `STATE.md` → `METHOD.md` → `PLAN.md` → `08-CROSS-UNIT-SYNTHESIS.md`. Then execute U09 ERPNext only. Completed target packages are opened selectively when comparison requires them.
