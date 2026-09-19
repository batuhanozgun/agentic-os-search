# ECC — STATE

**Updated:** 2026-09-19 — U11-B scheduled-work source inquiry COMPLETE / PUBLISHED.
**Last completed unit:** U11-B / Q04e1. [Note20](notes/20-SCHEDULED-WORK-ADMISSION-AND-RETRY.md), [sources](evidence/U11-B-SOURCES.md), [MR21](ROUND-U11-B.md). Q04e1a has the bounded source answer; Q04e1b keeps stronger occurrence/runtime/acceptance claims. This does not complete ECC.
**Current/next authorized research:** U11-C / Q04e2 remote-request intake, target/authority, dispatch and result/failure/retry, **NOT STARTED**. No U11-B publication task remains.
**Current publication:** [U11-B receipt](PUBLICATION-U11-B.md), commit `6842cf981097c528a6f44f55f1c6ea98d6cab779`, fully read back as blob `c4feb89ba203732990d37e7d9efdfddf4aa768a8`. Note20 commit `18287f3ba8d97fd329853f7c5a2080d5e7cdec69`, full-read blob `e68ea0b092977a3095f6bb9ff03565805fe3ae73`; source ledger commit `becd7b1f0564a47d3d187e08863b39f4ce2cff62`, full-read blob `c9f6a215be774677cc542fe5208abfddb3934141`. Entry/round/catalogue checks through `d3f4064608a7b02ee91376e3d755c71c64d688e9` are in the receipt.
**Study:** ACTIVE / PARTIAL. **METHOD / PLAN:** 0.1 / 0.22.
**Target:** `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a`, unchanged.
**Publication obligations:** no user upload or merge. No new branch/PR or force update. Study changes are ECC-local plus only its mechanically checked CATALOG row; independent concepts work is preserved.

## Current result and evidence boundary

Note20 explains a recurring session-admission producer. Normal creation validates cron/future time and an explicit profile, then stores timing, task, path and profile name. Dispatch resolves current configuration, selects due rows in order, queues a session and only then calculates/records another time. UTC pass time, originally due occurrence, admitted session, live process and accepted task result remain distinct.

A requested worktree at capacity can yield a Pending queued session and a successful admission return without a runner. The daemon's max_parallel_sessions is the due-query batch limit in this chain, not a subtraction of live sessions or per-schedule non-overlap. Successful advancement records the pass time, not completed work. Missed cron times are not individually replayed, and the daemon's work-plus-sleep cycle is not an exact firing guarantee.

Admission and the by-id schedule update are separate effects. After a finite schedule's final occurrence, successful admission can precede a no-future-time error, leaving the old row due. An early persistent error can prevent later due rows from being reached; prior side effects remain although the batch returns no partial outcome vector. Competing due snapshots and removal after selection expose separate duplicate/revocation boundaries. Removing a row prevents fresh future selection, not already-admitted work. The returned schedule/session association is not stored as occurrence/result history by the examined schedule writer.

These are source observations and conditional interleavings, not executed production incidents. Positive validation, ordered limits, worktree queue retention, successful advancement, future-selection removal and daemon error reporting remain part of the explanation. Q04e1b retains actual timing/restart, malformed/migrated rows, configuration/filesystem/binary correspondence, occurrence ownership, terminal handling, cancellation/backoff/fairness, durable provenance and task acceptance.

The ordinary scheduling test and selected queue tests were inspected, NOT RUN. The declared cron0.17.0 contract was checked through version-labelled primary source documentation; crate bytes and a built binary were not verified. No target code/test, SQL fixture, Rust build, process, recurring task, server, provider/model, installation or E09 ran. E08 remains its one adapted review-flow experiment; E06 stays excluded; E04/E07 and both E05 histories stay separate.

## Purpose and authority

Explain the actual ECC-native working system through pinned mechanisms and limits while maintaining repository-centred continuity and a revisable method case. Whole-study joint evaluation with Batu follows completed research. Foundation/SOUL/Development OS relations are provisional reuse hints, not taxonomy, architecture or adoption. [U07-A family map](inventory/U07-A-FAMILY-MAP.md) owns breadth obligations, not final recursive/mirror coverage or CORE.

Batu owns purpose/material phase changes. The assistant owns authorized source research, proportionate isolated fixtures, sequencing and verified publication. Writes remain research/studies/ecc/** plus only necessary ECC discovery changes in shared CATALOG/INDEX. Preserve other studies, Foundation, concepts, explorations, soul-context, upstream and agent-control. No user-home/config/cache mutation, installation, credential/provider/model calls, upstream report/patch or SOUL implementation.

## Next authorized work — U11-C / Q04e2

Trace actual remote CLI/HTTP producer → input/authentication/target binding → pending request → targeted assignment or top-level session admission → durable status/result/error → recipient/operator consumer and retry. Request acceptance, dispatch, recipient uptake and completed work are distinct. Inspect a meaningful invalid/unauthorized/routing failure and a continuation or competing-dispatch boundary; do not infer safety from a default loopback address.

Entry at the unchanged pin: S186 main.rs RemoteCommands within563–655 and Remote match within2733–2910 → run_remote_dispatch_server and its real HTTP helpers. S187 manager.rs request construction within250–445, run_remote_dispatch_requests/inner loop within463–592, then actual targeted assignment/handoff functions as needed. S190 store.rs request schema and insert/list/success/failure methods within1620–1770; S189 daemon wrapper. Recover complete load-bearing functions; the ranges are location aids, not full-source substitutes.

PLAN0.22 owns the bounded return condition. Remote/delegation bodies incidentally exposed during U11-B are not completed research. Do not restart answered scheduling/basic lifecycle or create a live endpoint, model run or test quota. Broader delegate/team/template controls, other procedures, host/provider, release/scanner/audit/observability, native syntheses and final omission work remain.

## Recovery and publication

After canonical bootstrap: STATE → INDEX → META/WHY/METHOD/PLAN/QUESTIONS → Note20/U11-B sources/MR21/current receipt. Earlier load-bearing claims require original notes/evidence through INDEX. FULL/SELECTED/truncated/test-source/dependency-contract/local-execution remain distinct. The source ledger records incidental ranges and unresolved monolithic-file retrieval costs rather than claiming exhaustive coverage.

Publication is closed. Opening IN PROGRESS labels and MR21/receipt statements about subsequent checks are chronological history, not new repair tasks. Same-assistant readback/hash/diff checks establish correspondence, not independent research validation. No user upload, merge or old ZIP recovery is needed.

CATALOG's complete base was matched before the one-row change; the returned blob matched the mechanically prepared candidate and the net diff was +1/-1. No new catalogue correction was needed. Prior error histories remain in their own receipts. A concurrent concepts/STATE update was preserved and is not this study's work.

## Preserved history

Complete pre-U11-B state: [STATE at input e34c9f7](https://github.com/batuhanozgun/agentic-os-search/blob/e34c9f7fe42ef62aa4372901a469aa9bacdf09ee/research/studies/ecc/STATE.md). U11-A remains COMPLETE/PUBLISHED through `ab3da7f3113f7303664c17f091923c97bc84016c`: [Note19](notes/19-NATIVE-REVIEW-CALLER-AND-DECISION-BOUNDARIES.md), [sources](evidence/U11-A-SOURCES.md), [MR20](ROUND-U11-A.md), [receipt](PUBLICATION-U11-A.md), [E08](evidence/u11-a-review-flow-probe/README.md). Earlier U10/U09/U08/U07 units and their original ledgers/receipts remain accessible through INDEX and unchanged.

Stronger Q04g1c/Q04g2b/Q04h2/Q06d1b/Q06d2b remain open alongside Q04e1b. E06 exclusion/recovery, two E05 histories and U11-A's corrected evidence/catalogue preparation errors retain their original authority and limits. The old U09-A3 ZIP is historical only. Concurrent concepts/control changes do not rewrite ECC meanings or acceptance.
