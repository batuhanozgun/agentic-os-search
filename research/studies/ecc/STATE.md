# ECC — STATE

**Updated:** 2026-09-19 — U11-D backlog-coordination/consumption source inquiry COMPLETE / PUBLISHED.
**Last completed unit:** U11-D / Q04e3. [Note22](notes/22-BACKLOG-COORDINATION-AND-CONSUMPTION.md), [sources](evidence/U11-D-SOURCES.md), [MR23](ROUND-U11-D.md). Q04e3a has the bounded source answer; Q04e3b retains stronger runtime/liveness/uptake/acceptance claims. This does not complete ECC.
**Current/next authorized research:** U11-E / Q04e4 orchestration-template resolution and multi-session launch composition, **NOT STARTED**. No U11-D publication task remains.
**Current publication:** [U11-D receipt](PUBLICATION-U11-D.md), commit `9e0cca5a0b68151a5d4f390f07355a7d0f817d48`, fully read back as blob `691d618f237578cccf304c5d2cfdedb72a051ca5`. Note22 commit `1e8684a3e1f6afec64b9c9d135fc3d370d6ad978`, full-read blob `261d6fc497f3ec608a883f3ebf919671ed7b7f23`; ledger commit `9b46155e904560c90b89e657f3d0d4e00e2e46cf`, full-read blob `33b057b0c14dad46820b4b19b95640cd74fe6988`. Entry/round readbacks and checked catalogue through `7f65dc36a6a9a2c9990d020bb4e70f6fed9f9d0d` are recorded in the receipt.
**Study:** ACTIVE / PARTIAL. **METHOD / PLAN:** 0.1 / 0.24.
**Target:** `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a`, unchanged.
**Publication obligations:** no user upload or merge. No named branch/PR or force update. This study's main changes are ECC-local plus only its checked CATALOG row; independent concepts work is preserved.

## Current result and evidence boundary

Note22 explains unread handoff selection, assignment/source read marking, rebalancing, persistent daemon decisions, explicit CLI maintenance and actual input/consumer boundaries. Automatic backlog distribution is disabled by default. Normal drain retains a source message when routing is deferred for saturation; rebalancing rereads capacity and checks the source lead. These are real controls, not proof of task completion.

The global frontier groups unread recipients, not declared lead roles. A new child can receive task text through admission/launch and also an unread companion handoff. With enabled automation, no intervening consumer acknowledgement and successful admission, a later pass can select that child as a lead and forward the same task again. Per-team limits are not a global depth or task-lineage termination guard. Native process completion does not mark the companion handoff read. This is a conditional source path, not observed infinite processes or a claim that every custom host lacks a consumer.

Rebalancing uses all unread counts in some guards and handoff-only counts in assignment. Unlike drain, its post-assignment marker does not check whether the returned action routes work. Changed capacity between checks and assignment can expose a DeferredSaturated/source-read mismatch. Routing, message/projection persistence, source markers and daemon summaries are separate effects; errors or competing snapshots can leave work moved without a matching current acknowledgement or summary. These are conditional interleavings, not executed losses or duplicate rates.

Cooloff has no elapsed-time expiry. With unresolved prior deferrals and the relevant count/streak, zero reroutes cause dispatch to be skipped. The rebalance writer leaves the controlling deferred/streak fields unchanged, so new usable dispatch capacity need not be retried. A streak frozen below five need not reach the escalation flag. Positive rebalance/recovery branches remain explicit. Restart is not itself a reset of persistent activity. No live hang or recovery experiment was run.

Health combines current inbox pressure with historical daemon activity, not accepted deliverables. Explicit CLI routing bypasses the daemon cooloff/recorder wrappers and does not automatically refresh their history. The inbox command prints a limited recent view but marks all unread incoming rows before printing; marked-read does not guarantee displayed or consumed task content. The complete native runtime and comms paths do not provide an automatic inbox-to-stdin/accepted-output loop. The separately read session-bridge module shares metrics, not inbox messages. Initial launch input, stored handoff, operator output and effective worker uptake remain distinct.

Relevant manager and daemon tests were inspected, NOT RUN. Their oracles concern message rows, actions, counts and controlled callbacks, not live model uptake or eventual persistent recovery. No E09, Rust build, target process/daemon/service, model/provider, installation or upstream change occurred. Q04e3b preserves actual multi-cycle/host/OS behavior, task identity/uptake/acceptance, concurrency/cancellation/fairness, leaf/termination, cooloff recovery/observer freshness and custom integrations. E06 remains excluded; E08 is one adapted review run; E04/E07 and both E05 histories stay separate.

## Purpose and authority

Explain ECC's actual native working system through pinned mechanisms and limits while preserving repository-centred continuity and a revisable method case. Joint whole-study evaluation with Batu follows completed research. Foundation/SOUL/Development OS relations are provisional reuse hints, not taxonomy, architecture or adoption. [U07-A family map](inventory/U07-A-FAMILY-MAP.md) retains breadth obligations; native syntheses/CORE and recursive/mirror/holdout closure remain incomplete.

Batu owns material purpose/phase changes. Assistant owns authorized research, proportionate isolated fixtures, sequencing and verified publication. Writes remain research/studies/ecc/** plus necessary ECC discovery in shared CATALOG/INDEX. Preserve other studies, Foundation, concepts, explorations, soul-context, upstream and agent-control. No user-home/config/cache mutation, credential/provider/model call, live endpoint, installation, upstream issue/patch or SOUL implementation.

## Next authorized work — U11-E / Q04e4

Trace template source/variables/defaults → validation/resolution → capacity snapshot → ordered session admission → anchor/handoff relationships → returned/persisted outcomes → actual execution dependency or consumer. Separate substituted text, launch order, execution ordering, successful task completion and accepted result. Include a normal useful example and a meaningful validation/capacity/later-step failure/retry contrast. A fixture is optional for a material discriminator, not a quota.

Entry at unchanged pin: S195 config/mod.rs resolve_orchestration_template within390–480, then actual template/step types and interpolation helpers. S187 manager.rs launch_orchestration_template/build_template_variables within595–790, then known queue/profile/handoff paths only as needed. S186 main.rs Template arm around1570–1635 and actual CLI/configuration examples/tests. Recover complete load-bearing bodies; these coordinates are aids and earlier incidental template reading is not completed U11-E research.

PLAN0.24 owns the bounded return condition. Do not assume ordered template steps are a workflow DAG or a completion-aware dependency system. Do not restart answered backlog/intake/scheduling/lifecycle/review/evaluation or activate live agents. Other procedures, host/provider composition, release/scanner/audit/observability, native syntheses and final omission work remain later priorities.

## Recovery and publication

After canonical bootstrap: STATE → INDEX → META/WHY/METHOD/PLAN/QUESTIONS → Note22/U11-D sources/MR23/current receipt. Earlier load-bearing claims require original notes/evidence through INDEX. FULL/SELECTED/truncated/test-source/dependency-contract/executed remain distinct. Publication is closed. Opening IN PROGRESS and chronological MR/receipt references to subsequent checks do not create new repair tasks.

Catalogue publication changed its control point this turn. Actual unreferenced candidate diffs were checked before moving main, and erroneous full-text candidates were rejected. The final local reconstruction matched the existing whole base hash when its ECC row was reverted. Its checked bytes were base64-transferred as blob38cf60a3cbce837d7ed22fcfb095c143bc9eb4f2; subsequent trees referenced that identity. The final actual diff changed only ECC. Concurrent concepts commits invalidated the initial parent, so the checked blob was rebound to the fresh base and reviewed again before a non-force main update.

No bad catalogue candidate reached main. Unreferenced rejected or old-base candidate Git objects are historical preparation artifacts, not pending branches/PRs or user merge work. Repeated manual text preparation remained costly and error-prone; successful pre-main checking is not proof of universally reliable serialization. The receipt preserves the errors, exact successful route and its limits. Local byte/hash work was publication administration, not a new ECC experiment.

Inputb6d6883→7f65dc3 includes eight ECC-local paths, the one-row catalogue change and five independently updated concepts paths. Their changes were preserved, not produced by this research. Same-assistant readback/hash/diff checks establish correspondence, not independent research validation. No upload, merge or old ZIP recovery is needed.

## Preserved history

Complete pre-U11-D state: [STATE at input b6d6883](https://github.com/batuhanozgun/agentic-os-search/blob/b6d6883a047938cd034e462f1c2f891b134f2c8f/research/studies/ecc/STATE.md). U11-C remains COMPLETE/PUBLISHED: [Note21](notes/21-REMOTE-INTAKE-DISPATCH-AND-RESULT-BOUNDARIES.md), [sources](evidence/U11-C-SOURCES.md), [MR22](ROUND-U11-C.md), [receipt](PUBLICATION-U11-C.md). Earlier U11-B/U11-A/U10/U09/U08/U07 notes, ledgers and receipts remain reachable through INDEX and unchanged.

Q04e1b/e2b, Q04g1c/Q04g2b/Q04h2/Q06d1b/Q06d2b remain open alongside Q04e3b. E06 exclusion/recovery, both E05 histories and prior publication corrections retain their scopes. The old U09-A3 ZIP is historical only. Concurrent concepts/control changes do not rewrite ECC meanings or acceptance.
