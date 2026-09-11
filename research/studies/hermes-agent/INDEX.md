# Hermes Agent — INDEX

Current work/completion authority [STATE](STATE.md); classification/reuse [META](META.md); method/closure [METHOD](METHOD.md). Current plan [v0.16](RESEARCH-PLAN.md). This router is not independent Work authority.

## Current explanatory layer

| Question | First route |
|---|---|
| How is work continued across turns, and why do different loops stop? | **[synthesis/03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md)** → [18/U04](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → [RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md) |
| Which sources were read and which code actually ran? | [U04 SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [SPEC](evidence/2026-09-11-multi-turn-continuity/SPEC.md), [MANIFEST](evidence/2026-09-11-multi-turn-continuity/MANIFEST.json) |
| Where are the exact G/H observations and runnable inputs? | [Committed evidence archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz); [summary](evidence/2026-09-11-multi-turn-continuity/RESULT-SUMMARY.json) is only a browsing view |
| How does a normal input become context, execution, durable state and delivery? | [synthesis/02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) → [16/U02](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md) |
| How are durable Kanban tasks claimed and their results accepted? | [17/U03](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md) → [RESEARCH](evidence/2026-09-10-kanban-task/RESEARCH.md) |
| What does learning/change look like inside the core? | [synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md); read 02/U02 for normal-compaction refinement |
| What next? | [STATE](STATE.md), [PLAN](RESEARCH-PLAN.md): actual session lease/history/SessionDB, rotation/restart continuation and driver recovery |
| Is the whole system researched? | No; [new coverage](inventory/CONTINUITY-COVERAGE-2026-09-11.md), [broad U02 map](inventory/CORE-COVERAGE-2026-09-10.md), [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

## Mechanism and historical evidence routes

| Question | Entry |
|---|---|
| Original rationale / scope / method | [00-WHY](00-WHY-THIS-RESEARCH.md), [METHOD](METHOD.md) |
| Initial topology / orientation | [STRUCTURE](inventory/STRUCTURE.md), [01](notes/01-ORIENTATION.md) |
| Review snapshot/fork/ownership | [02](notes/02-BACKGROUND-LEARNING.md) |
| Curator maintenance/report/cron | [03](notes/03-SKILL-CURATION.md) |
| Skill transaction/approval | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [U01B](evidence/2026-09-07-u01b/component-probe/README.md) |
| Historical unpinned documentation contracts | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md), [W](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| Caller/worker/context transfer | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [D](evidence/2026-09-08-context-transfer/SOURCES.md) |
| MemoryStore/pending replay | [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) |
| Default-name roundtrip/live diff/rollback | [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [U01B2](evidence/2026-09-08-u01b2/README.md) |
| Selected worker policy / full validator | [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [E/C/V](evidence/2026-09-08-worker-policy/README.md) |
| Review admission / middleware / manual-range AST | [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md), [J/MW](evidence/2026-09-09-review-middleware/README.md) |
| Five-full-module memory/pending diagnostic | [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md), [M2/N](evidence/2026-09-09-memory-pending/README.md) |
| Actual CLI/gateway pending/profile source | [12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md), [UI/A](evidence/2026-09-10-ui-profile/SOURCES.md) |
| Separate pending-caller delivery | [13](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md), [M3-S/SA](evidence/2026-09-10-pending-caller/SOURCES.md) |
| Separate AP six-case recovery | [14](notes/14-AP-DELIVERY-RECONCILIATION.md), [AP original](evidence/2026-09-10-ui-profile-approval/README.md) |
| M4 fresh store vs old stored prompt | [15](notes/15-MEMORY-PROMPT-RESTORE-BOUNDARIES.md), [M4 RESULT](evidence/2026-09-10-prompt-restore/RESULT.json); actual compaction caller in 16/C13 |
| General turn/context/session and stop/delivery | [16](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md), [U02 RESEARCH](evidence/2026-09-10-turn-lifecycle/RESEARCH.md) |
| Kalıcı task/run/claim/completion and recovered K evidence | [17](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md), [U03 README](evidence/2026-09-10-kanban-task/README.md), [K archive](evidence/2026-09-10-kanban-task/original-evidence.tar.xz) |
| Actual multi-turn caller, goal/loop/heartbeat and new G/H evidence | **[18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md)**, [U04 README](evidence/2026-09-11-multi-turn-continuity/README.md) |
| Scope rebalance and source inventory | [SCOPE-REVIEW](inventory/SCOPE-REVIEW-2026-09-10.md), [CONTINUITY-COVERAGE](inventory/CONTINUITY-COVERAGE-2026-09-11.md), [SOURCE-LEDGER](SOURCE-LEDGER.md) |

## Fresh-session cautions

U04 is new research/execution, U03 publication was recovery. G manual selection, H full-blob-verified heartbeat, K real-SQLite/reduced-DDL selection, U02 source-only and earlier A/SA/AP/M4/N/MW/C/V remain distinct. Three provisional syntheses are explanations, not independent evidence or a completed native CORE.

Exact G/H code/raw/logs are in the committed archive. The browsing summary is not a substitute for exact traces. No old chat ZIP is needed. Full heartbeat identity does not establish full goals/CLI/driver/K/E source fidelity or whole-runtime quality.

Same-session history is not resolved by looking only at the quiet wrapper: S10 facade can substitute admission history, and turn_facade_lease was inaccessible (429). The next real task is that consumer/SessionDB and restart/rotation driver connection, not repeating G/H tests. Q07/Q22 last-wire/timing and Q26/Q29 full-worker remain open. Historical 'next' and access statements are not current authority. No Foundation/four-area/architecture/adoption decision follows automatically.
