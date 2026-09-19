# ECC — STATE

**Updated:** 2026-09-19 — U11-C remote-intake/dispatch/result source inquiry COMPLETE / PUBLISHED.
**Last completed unit:** U11-C / Q04e2. [Note21](notes/21-REMOTE-INTAKE-DISPATCH-AND-RESULT-BOUNDARIES.md), [sources](evidence/U11-C-SOURCES.md), [MR22](ROUND-U11-C.md). Q04e2a has the bounded source answer; Q04e2b retains stronger authority/runtime/uptake/acceptance claims. This does not complete ECC.
**Current/next authorized research:** U11-D / Q04e3 unread-handoff/backlog coordination and actual consumer/acknowledgement, **NOT STARTED**. No U11-C publication task remains.
**Current publication:** [U11-C receipt](PUBLICATION-U11-C.md), commit `725da117c9ad432245b62748cd8ffccdee771833`, fully read back as blob `49b523036d24050b966228c8961f72e0b3bde98f`. Note21 commit `6985dc986c9cf20293d3b7a95a546cf70f222ec2`, full-read blob `2f854ecb06772115c16a8e7b0a023b1b64ea4818`; ledger commit `39a1e2267a531c958026e5f5db1eee3555dec6ec`, full-read blob `cd6f2381455a17fde44426a73c43fbce09d56be5`. Complete entry/round checks and corrected catalogue correspondence through `56b1ac34ba639aba7fdeaa0f62fe216d77f9e2fa` are recorded in the receipt.
**Study:** ACTIVE / PARTIAL. **METHOD / PLAN:** 0.1 / 0.23.
**Target:** `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a`, unchanged.
**Publication obligations:** no user upload or merge. No new branch/PR or force update. Final net study changes are ECC-local plus only the checked ECC CATALOG row.

## Current result and evidence boundary

Note21 explains the real HTTP/CLI intake, request store, dispatcher, targeted assignment/top-level admission, result writer and operator/message consumers. The separate HTTP service records accepted requests and returns202; it does not itself dispatch them. Constant health is not queue/worker health. Exact bearer and input/target checks are real; body reading on the synchronous service precedes route-specific authentication, without an explicit body bound or accepted-stream deadline in the inspected functions. Deployed exposure and external controls were not tested.

A target session is a lead for delegate routing, not necessarily the final worker. Under the native schema and enabled FK behavior, successful deletion of that lead sets a pending request's target to null. A fresh dispatch read treats None as an untargeted request and can admit a new top-level session. Referential integrity is maintained while the distinction between never-targeted and target-disappeared is lost. This conditional case depends on successful eligible deletion and a fresh read; an already-held target snapshot can instead fail lookup. No live deletion/dispatch incident was executed.

Reuse checks harness/state/backlog, not requested profile/environment equivalence. Its branches send a handoff without reapplying the request's profile, while new-child branches use the known profile-resolution path. Remote priority orders request selection, but the shared handoff is Normal priority and carries no remote request id/requester. These are propagation boundaries, not a measured privilege escalation or assertion that every existing profile is wrong.

The remote row stores result_session_id/action/error/time, a real routing-provenance mechanism. Dispatched can still mean a Pending worktree or persisted handoff, not a ready worker or accepted output. Ordinary routing errors can be recorded per item and later requests attempted. Failed rows leave automatic pending selection; saturated rows remain pending. Result-write errors and competing snapshots remain separate read/route/acknowledgement boundaries. Message persistence/read flags are not per-request worker acknowledgement.

Three relevant test bodies were fully inspected, NOT RUN; a directly inserted row labelled http was not called an HTTP/auth test. Primary SQLite/Rust/HTTP documentation bounds source claims, not installed/built conformance. No target code/test, SQL fixture, Rust build, socket/server, provider/model, installation, upstream patch or E09 occurred. E08 remains its one adapted review run; E06 stays excluded; E04/E07 and both E05 histories are separate.

Q04e2b retains installed networking/transport/resource behavior, actor/grant/token/target/revision authority, migrated schema, concurrency/idempotency, profile/environment compatibility, full tests and actual per-request acknowledgement/acceptance. Older stronger residuals remain unchanged. No architecture or adoption follows.

## Purpose and authority

Explain ECC's actual native working system with source-grounded mechanisms and limits, preserving repository-centred continuity and a revisable method case. Joint whole-study evaluation with Batu follows completed research. Foundation/SOUL/Development OS relevance is provisional reuse, not taxonomy or architecture. [U07-A family map](inventory/U07-A-FAMILY-MAP.md) retains breadth obligations; native syntheses/CORE and recursive/mirror/holdout coverage remain unfinished.

Batu owns material purpose/phase changes. Assistant owns authorized research, proportionate isolated fixtures, sequencing and verified publication. Writes remain research/studies/ecc/** plus only necessary ECC discovery changes in shared CATALOG/INDEX. Preserve other studies, Foundation, concepts, explorations, soul-context, upstream and agent-control. No user-home/config/cache mutation, credential/provider/model call, live endpoint, installation, upstream issue/patch or SOUL implementation.

## Next authorized work — U11-D / Q04e3

Trace unread handoff/source/priority → lead/team selection → route/reuse/spawn/defer → source-message acknowledgement → durable daemon activity/pressure → rebalancing/recovery → actual downstream consumer. Separate routable backlog, live work and accepted output. Inspect a material saturation, write/read-acknowledgement failure, changed delegate or interrupted-route counterpart and what later passes can repeat.

Entry at unchanged pin: S187 manager.rs drain_inbox/auto_dispatch_backlog/coordinate_backlog/rebalance_team_backlog within880–1180, complete targeted assignment1490–1695 and send_task_handoff2775–2995 as needed. S189 daemon.rs coordinate_backlog_cycle/with and recorder callbacks120–365. S190 store.rs unread-handoff/target/mark-read methods2650–2960 and delegated_children near3915. Recover full relevant functions and actual recipient-input callers; these coordinates are aids, not a claim that this downstream inquiry is already complete.

PLAN0.23 owns the bounded return condition. Do not infer worker uptake from a message row or remote result. Preserve source identity/priority/profile propagation questions without immediately prescribing a universal architecture. A fixture is optional for an actual discriminator, not a quota. Do not restart answered intake/scheduling/lifecycle/review/evaluation or activate a live campaign. Team/template, other procedures, host/provider/release/scanner/audit/observability, native synthesis and omission work remain later priorities.

## Recovery and publication

After canonical bootstrap: STATE → INDEX → META/WHY/METHOD/PLAN/QUESTIONS → Note21/U11-C sources/MR22/current receipt. Earlier load-bearing claims require original notes/evidence through INDEX. FULL/SELECTED/truncated/test-source/dependency-contract/executed remain distinct. Publication is closed; opening IN PROGRESS and MR22/receipt references to subsequent checks are chronological history, not a new repair task.

Catalogue preparation matched the complete base and a mechanically changed candidate. The actual tool argument nevertheless accidentally altered OpenProject's relevance cell; returned-hash mismatch and patch inspection detected it. The cell was restored and the final returned blob exactly matched the precomputed24,852-byte candidate. Net CATALOG diff is +1/-1 for ECC only. The receipt records the intermediate error and the remaining checked-file-to-manually-emitted-payload gap. This correction is complete, not proof of a generally reliable copying workflow or a new user task. No research result was altered to conceal it.

Input29b07b6→56b1ac3 changed only eight ECC-local paths plus CATALOG; earlier independent concepts changes in the input were preserved. Same-assistant readbacks/hash/diff checks are correspondence, not independent validation. No upload, merge or old ZIP recovery is needed.

## Preserved history

Complete pre-U11-C state: [STATE at input29b07b6](https://github.com/batuhanozgun/agentic-os-search/blob/29b07b6529618f9a654d44a86e3ed6b05b8b40f9/research/studies/ecc/STATE.md). U11-B remains COMPLETE/PUBLISHED through `19b7b8e039448af7c78bd426af1e6c8619bbd548`: [Note20](notes/20-SCHEDULED-WORK-ADMISSION-AND-RETRY.md), [sources](evidence/U11-B-SOURCES.md), [MR21](ROUND-U11-B.md), [receipt](PUBLICATION-U11-B.md). Earlier U11-A/U10/U09/U08/U07 notes, ledgers and receipts remain reachable through INDEX and unchanged.

Q04e1b/Q04g1c/Q04g2b/Q04h2/Q06d1b/Q06d2b remain open alongside Q04e2b. E06 exclusion/recovery, both E05 histories and prior publication corrections retain their scopes. The old U09-A3 ZIP is historical only. Concurrent concepts/control changes do not rewrite ECC meanings or acceptance.
