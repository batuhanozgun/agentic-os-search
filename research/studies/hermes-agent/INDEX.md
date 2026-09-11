# Hermes Agent — INDEX

Current work/completion authority [STATE](STATE.md); classification/reuse [META](META.md); method/closure [METHOD](METHOD.md). Current plan [v0.15](RESEARCH-PLAN.md). This router is not independent Work authority.

## Current explanatory layer

| Question | First route |
|---|---|
| How does a normal input become context, execution, durable state and delivery? | [synthesis/02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) → [16/U02](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md) |
| How are durable Kanban tasks claimed and their results accepted? | **[17/U03](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md)** → [RESEARCH](evidence/2026-09-10-kanban-task/RESEARCH.md) → [SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md) |
| Which old evidence was recovered, and did recovery run new tests? | [PUBLICATION](evidence/2026-09-10-kanban-task/PUBLICATION.md), [MANIFEST](evidence/2026-09-10-kanban-task/RECOVERY-MANIFEST.json); no new behavior run |
| Where are complete K01–K08 inputs/results? | [Committed original archive](evidence/2026-09-10-kanban-task/original-evidence.tar.xz); [derived result summary](evidence/2026-09-10-kanban-task/RESULT-SUMMARY.json) for browsing, [exact SPEC](evidence/2026-09-10-kanban-task/SPEC.md) |
| What does learning/change look like inside the core? | [synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md); read 02/U02 for normal-compaction refinement |
| What next? | [STATE](STATE.md), [PLAN](RESEARCH-PLAN.md): actual Kanban goal-loop/worker continuation, then goal/loop/heartbeat distinctions |
| Is the whole system researched? | No; [coverage](inventory/CORE-COVERAGE-2026-09-10.md), [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

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
| Kalıcı task/run/claim/completion and recovered K evidence | **[17](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md)**, [U03 README](evidence/2026-09-10-kanban-task/README.md) |
| Scope rebalance and source inventory | [SCOPE-REVIEW](inventory/SCOPE-REVIEW-2026-09-10.md), [CORE-COVERAGE](inventory/CORE-COVERAGE-2026-09-10.md), [SOURCE-LEDGER](SOURCE-LEDGER.md) |

## Fresh-session cautions

U03 is partially source-explained and has recovered selected-function/real-SQLite evidence. It is not full-module or whole-runtime validation, and recovery is not a new execution. A/SA/AP/M4/old N/MW/C/V and U02 histories stay separate. The original archive is in the repository; do not ask the user for the old chat ZIP. Detailed K snapshots and mutant observations are inside it, not fully copied into RESULT-SUMMARY.

Q07/Q22 ordinary compaction→API-message source connection stands; M4's artificial V04 order is not a demonstrated actual compression failure. Q26/Q29 full-worker/original verifier remains open. No third completed synthesis, native CORE, four-area projection or architecture/adoption is asserted. Historical indexes and statements about access/publication are not current authority.
