# ECC — Adaptive Research Plan

**Version:** 0.16 / 2026-09-18. STATE owns current work/publication; METHOD 0.1 retained. U09-A2 completes a bounded storage/observer/resource-continuity slice, not the whole U09-A lifecycle criterion. [MR15](ROUND-U09-A2.md) records the scope/evidence decision. No historic evidence or completion criterion is lowered.

## Current result and phase map

[Note13](notes/13-RUST-SESSION-LIFECYCLE-FIRST-SLICE.md) and [its sources](evidence/U09-A-SOURCES.md) explain CLI/record/runner/harness/daemon distinctions. [Note14](notes/14-STORE-OBSERVER-AND-WORKTREE-CONTINUITY.md) and [additional sources](evidence/U09-A2-SOURCES.md) now explain lookup, retained output, derived board, actual TUI consumer/controller and worktree-path continuity. [E07](evidence/u09-a2-sql-git-probe/README.md) is a source-derived SQL/Git fixture, not an original Rust or live-host execution. U09-A/Q04g1 stays IN PROGRESS at execution-attempt ownership.

U08-A's [Note12](notes/12-PLAN-CANVAS-FEEDBACK-AND-CONTINUATION.md), sources and MR13 remain bounded/published. Its original E06 remains unverified/excluded; [recovery records](RECOVERY-U08-A-20260918.md) are historical, not a new publication prerequisite. Both E05 histories remain separate.

| Phase | Current standing / obligation |
|---|---|
| P0 Method/work foundation | U00 complete; no repeat setup |
| P1 Native discovery | U07-A first-tier family accounting; descendants/mirrors/representativeness PARTIAL |
| P2 Mechanism slices | Earlier units preserved; U08-A source-complete; U09-A first and second slices recorded, parent IN PROGRESS |
| P3 Subsystems/relations | Scoped synthesis candidates in U07-A map; no completed whole-system synthesis |
| P4 Project comparison | Then-current Foundation/project and selected studies; joint discussion after completed research |
| P5 CORE/closure challenge | Consequential unexplained families and reverse-inventory/holdout checks remain |
| P6 Method case | MR15 preserves actual consumer discovery, explicit fixture controls and partiality; no independent efficacy claim |

The [U07-A family map](inventory/U07-A-FAMILY-MAP.md) remains breadth authority. Its earlier pass-time next-unit labels do not override STATE. No complete recursive inventory, mirror audit, CORE or final joint evaluation is claimed. Research-internal sequencing and branch/merge timing remain assistant-managed.

## U09-A — current unit, do not restart completed slices

**Parent question Q04g1:** How does ECC2 turn a command and stored session record into an actual running, stopped or resumed process? What survives interruption, and which observation justifies a lifecycle transition?

**Q04g1a — bounded source answer, Notes13–14:** normal command/record/runner path; actual output producer–database–dashboard consumer; state/board distinction; same-id relaunch and daemon reconciliation; cleanup versus retained resources. E07 discriminates bounded retention, partial statement effects, an id-only stale write and recreated path versus Git identity. Original Rust integration and model/context restoration are not established.

**Q04g1b — next authorized continuation:** Which actor/process owns a particular execution attempt, and what prevents an obsolete or revoked attempt from continuing or overwriting current state?

Start from the existing S187/S188/S189/S190 source identities, not giant files at line 1:

1. Re-enter `ecc2/src/session/runtime.rs` / capture_command_output and its post-spawn error/finalization paths; trace child ownership, database-error cleanup and which tasks remain after an early return.
2. Join `manager.rs` run_session, activate_pending_worktree_sessions, resume_session_with_program and stop_session_recorded to actual state writers. Distinguish stop-before-pid, Pending/Idle/Stale resume, stale finalizers and delayed activation. Recover relevant session/queue schema and actual constraints before claiming attempt fencing or its absence.
3. Bind consequential cancellation/termination claims to the exact dependency/platform contract where available. Cargo.toml's Tokio 1 declaration and moving documentation alone do not establish a built runtime. Follow an actual supervisor exit/restart counterpart; retain source-only limits rather than launching a live model campaign.
4. Inspect targeted test assertions and doubles. A proportionate non-model fixture is optional only where it resolves a remaining discriminator. Do not rerun E07 to recover context or treat more test cases as automatic progress.

**Return condition unchanged:** one coherent lifecycle explanation and an important restart/failure contrast, with exact sources and open dependency boundaries. Finish the remaining source-level ownership explanation, or split explicitly if its load-bearing family is still too large. Do not require universal runtime certification to finish a bounded source study; equally, do not silently omit an actual effectful caller. Then reassess U09-A closure before activating Node Q04g2.

**Known completed contribution, not next work:** StateStore get_session/get_latest_session, append_output_line/get_output_lines and bounded retention; board derivation; TUI polling/cache/render path; effectful tick and interaction-dependent cadence; base-checkout/cache-link resource explanation and cleanup-path discriminator. Remaining unrelated schema, UI filters/rendering, cache mutation and branch-validation details are not full-read by this slice; revisit only when load-bearing or during final omission checks.

**Source depth:** MR14's refinement stands. main.rs 452,777 bytes, manager.rs 276,483 and store.rs 314,307 require complete relevant functions and caller/helper/consumer closure, not false whole-file FULL labels. S199 dashboard.rs is also selected, not fully read. Exact ranges remain in the ledgers. Source trees resolve filenames; names do not prove integration.

**Method check:** Does the next pass close an actual ownership question without spreading into every adjacent scheduler/evaluator? The first continuation found the real cross-process observer and a second controller. Preserve that result and its exact range handoff; keep a usable source result separate from runtime uncertainty.

## Following priorities — revisable, not automatically activated

1. Node operator/control-pane data/action bridge after bounded Rust lifecycle closure. Follow it earlier only when an actual load-bearing Rust consumer requires it.
2. Separate evaluation paths: Rust paired-seed registry versus Node capsule/replay/receipt and deliberately unavailable execution; evidence producer, admitted change and actual use. Do not transplant E04 conclusions.
3. Representative procedural/native workflow and host/provider composition: outer human gates, generated OpenCode assets, Python LLM layer and material host variants.
4. Release/packed-artifact qualification, external scanner boundaries, operational readiness/cost and remaining inventory omissions.
5. Scoped native syntheses from original notes, challenged by unread descendants and broad documents; then CORE and bounded project-facing comparison. Joint discussion follows completed research.

No independent AgentShield/AURA audit, installation, provider campaign or architecture/implementation phase is authorized by a pointer.

## Residuals and reopening

- Q01a2: recursive/body/mirror coverage and final omission challenge.
- Q03b/c: interrupted Kimi two-copy retry; repair/uninstall/merged JSON; abrupt/concurrent/cross-store/legacy durability.
- Q04b/c/e: snapshot/SQLite ingestion, imported roles/limited-list closure, supervision/acceptance/resumption and valuable-output retention.
- Q04f2: Plan Canvas exact review/actor/acknowledgment, ended-session discovery, Stop projection and live uptake. Q04g1b/g2: Rust attempt ownership and Node operator relations. Q04h: native review caller/outer gates/host validity.
- Q05b/c: completeness/status/conflict/duplicate recall; actual uptake/governed review/ECC2 projection and stronger isolation/replication.
- Q06b/c2/d: observation/archive scope, semantic independence/applicability, unique/comparable/version-bound outcomes and actual change admission; distinct Rust/Node evaluation families.
- Q07a2/b2/c2/d: actual guard effects/authority, fact uptake/current-target binding, collector/decision/action coupling, scanner/release boundaries. S138/S139 remain partial; S150 is policy source, not verified scanner behavior.
- Q08: producer-specific meanings of success, progress, health, presence, confidence and no-objection. Board percentages are now explained as heuristics, not task-completion evidence.
- Q09 whole-study evaluation remains deferred, not forgotten. Q10/MR15 records method effects and costs without independent validation.

E01–E05 keep original scopes, both E05 histories remain distinct, and E06 stays quarantined/unverified. E07 has its own prerecord, runner, actual results and correspondence checks. No Rust build, upstream test or real model/host ran in U09-A2. Earlier notes/inventories/ledgers are preserved. STATE may advance publication only after actual readbacks/scope checks; a published slice is not completed ECC research.
