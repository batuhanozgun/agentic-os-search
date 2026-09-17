# Work Management / Project Control — STATE

## Authority

This file is the authoritative package-local current-work state for `work-management-project-control`.

User authorization on 2026-09-17: plan the research program, process candidate repositories sequentially, and reflect the work durably in the research repository. This authorization does **not** authorize Foundation mutation, SOUL/Development OS architecture decisions, product adoption or installation.

## Current status

**ACTIVE / U01–U06 BOUNDED-COMPLETE; U07 GAS TOWN NEXT**

OpenProject provides the classical project/work-package baseline; Flowable provides durable process/case/decision execution; Beads provides an agent-native dependency/frontier/claim model; OpenSpec provides an artifact-DAG/living-plan model; Spec Kit provides spec-driven decomposition plus an implement→converge loop; Leantime adds strategy/goal/milestone/program alignment. The next unit is Gas Town.

## Completed

### U00 — Program framing and method setup

- bounded research object defined: large-work / project-control methodology rather than “pick a project-management product”;
- common comparison matrix defined in `METHOD.md`;
- first-wave targets selected to maximize methodological diversity rather than feature-count repetition;
- sequence and revision rules recorded in `PLAN.md`.

### U01 — OpenProject — BOUNDED-COMPLETE
Package: `../openproject/`.

Core contribution: classical work-package hierarchy/relations/scheduling/workflow/portfolio baseline.

### U02 — Flowable — BOUNDED-COMPLETE
Package: `../flowable/`.

Core contribution: durable process/case/decision execution, wait states, migration, retry/cancel/compensation distinctions.

### U03 — Beads — BOUNDED-COMPLETE
Package: `../beads/`.

Core contribution: computed actionable frontier, typed graph control, CAS claim, liveness lease and dead-worker recovery.

### U04 — OpenSpec — BOUNDED-COMPLETE
Package: `../openspec/`.

Core contribution: artifact dependency graph, living plan, planning/apply/completion separation, archive reconciliation.

### U05 — GitHub Spec Kit — BOUNDED-COMPLETE
Package: `../spec-kit/`.

Core contribution: spec-driven staged decomposition, reviewer-owned requirement gates, bounded session execution and implement→converge remediation loop.

### U06 — Leantime — BOUNDED-COMPLETE
Package: `../leantime/`.

Source-bounded findings at `Leantime/leantime@056835f1c29cf1f587415e6c45ddaf8d69f8d24c`:

- goals/metrics, milestones, tickets/tasks, sprints and project/program/strategy containers are distinct work/control objects;
- goal standing (`on track / at risk / miss`) differs from task lifecycle standing (`new / blocked / in progress / waiting for approval / done`);
- goals maintain explicit start/current/target metric values and history;
- goal↔milestone traceability is an explicit many-to-many `tracked_by` relation;
- milestone progress is separately derived from delivery work, so delivery completion and objective attainment remain distinct;
- project-custom task labels map to smaller semantic status categories for cross-project aggregation;
- roadmap/milestone, sprint and program groupings are orthogonal planning/aggregation surfaces;
- plugin-backed resource allocation remains outside this unit's load-bearing findings pending paired-plugin validation.

See `../leantime/FINDINGS.md` and `../leantime/SOURCE-LEDGER.md`.

## First-wave unit queue

1. **U01 — OpenProject** — **COMPLETE**
2. **U02 — Flowable** — **COMPLETE**
3. **U03 — Beads** — **COMPLETE**
4. **U04 — OpenSpec** — **COMPLETE**
5. **U05 — Spec Kit** — **COMPLETE**
6. **U06 — Leantime** — **COMPLETE**
7. **U07 — Gas Town** — **NEXT** — multi-agent work allocation, persistent work state and large-scale coordination.
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

## Method learning after U01–U06

Eighteen distinctions are now load-bearing:

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
18. reasoning/support artifacts (risk/retro/canvas) ≠ task-state controls unless explicitly wired.

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

Begin **U07 Gas Town**. Recover the native work and actor topology: Mayor/rigs/polecats/convoys or current equivalents, how work is represented/allocated/claimed, what persists across agents, how parallelism and completion are coordinated, how failures/abandoned workers are recovered, what provenance/attribution exists, and where Gas Town delegates work-state semantics to Beads rather than owning them. Preserve the Beads/Gas Town boundary explicitly.

## Fresh-session recovery

Read `META.md` → this `STATE.md` → `METHOD.md` → `PLAN.md`; open completed target packages only when comparison requires them. Resume the first unfinished unit above.
