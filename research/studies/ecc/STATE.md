# ECC — STATE

**Updated:** 2026-09-18 — U09-B bounded Node operator bridge source inquiry COMPLETE / PUBLISHED.
**Last completed unit:** U09-B / Q04g2. [Note16](notes/16-NODE-OPERATOR-BRIDGE-AND-TARGET-BINDING.md), [sources S206–S217 plus re-entry](evidence/U09-B-SOURCES.md), [MR17](ROUND-U09-B.md). Q04g2a has a bounded source answer; Q04g2b retains stronger target/recipient/durability/algorithm validation. This does not complete ECC.
**Current/next authorized research:** U10-A / Q06d1 Rust evaluation → admission → actual use, **NOT STARTED**. No unfinished U09-B publication task remains.
**Current publication:** [U09-B receipt](PUBLICATION-U09-B.md), commit `12b457ec2e2c02fed9182f02fcd81b53e1afe00b`, fully read back as blob `5cb7242b8bcf53fe2b147b28e2953efd4f707f5f`. Note16 commit `fac3c3f2a695ac2d6c20d53567e095c47151a064`, full readback blob `cf8ee46f972057af3e1573caf870293a6d06a6d6`; ledger commit `4d3319c61cd89fb24a1b43b9dd40dda5cc6b3d95`, full readback blob `4ad5aefaa2a92ab1669fa98c429ff612270bc7a2`. Entry/round/catalogue checks through `563883f120b129aa89087252c40f246524d2e456` are recorded in the receipt.
**Study:** ACTIVE / PARTIAL. **METHOD / PLAN:** 0.1 / 0.18.
**Unchanged target:** `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a`.
**Publication obligations:** no material output awaits user upload or merge. No branch/PR or force update. Changes are ECC-local plus only the mechanically checked ECC catalogue row.

## Current result and evidence boundary

Note16 joins the actual Node CLI/server/client and two stores to Rust configuration/graph/message consumers. It distinguishes displayed versus commanded database, card record versus worker, page recall versus Rust action, graph backfill versus its transitive policy checks, bounded imported snapshots versus current complete state, and rendered advisory versus admitted message and recipient action.

The concrete contract mismatch is Node steer/hold messages constructed as conflict without --file, while the pinned Rust build_message requires a file. With that consumer and ids resolved, the command is rejected before intended message insertion; query is a different path. The fake-runner test checks constructed arguments without exercising that consumer. This is source evidence, not an observed installed-binary or live-agent incident. The dispatcher records thrown send failure as skipped and retains only in-memory successful-send cooldown.

Useful controls remain: selected-stateDb card mutation/readback, read-only POST gates, fixed argv without shell, copy-only TUI action, hostname checking, escaped UI, private atomic export and declared-only advisory views. Missing stronger guarantees do not imply the whole system is broken. The original bridge source criterion is mapped in Note16 section10 and was not replaced with a test count.

No new target code, suite, Rust build, live server, provider/model, process signal, database fixture or E08 ran. Source tests were inspected only. E07 remains its prior Python/SQLite/Git fixture; E06 remains unverified/excluded. WAL-specific snapshot concerns are conditional: the inspected Rust open does not enable WAL, and no actual journal mode was observed. Full proximity/inventory/projection, connector/recall and visualization coverage remains unfinished at the ledger's scope.

U09-A's Notes13–15 remain COMPLETE/PUBLISHED, not restarted or promoted into all-path runtime certification. Q04g1c and Q04g2b preserve stronger claims and their reopening conditions. Broad orchestration, separate evaluation, host/provider, release/scanner/observability, native synthesis and final omission work remain in PLAN/QUESTIONS.

## Purpose and authority

Explain the actual ECC-native working system through pinned mechanisms and limits; maintain repository-centred continuity and a revisable method case. Comprehensive joint evaluation with Batu follows completed ECC research. Foundation relevance is a provisional reuse cue, not taxonomy, architecture or adoption. The [U07-A family map](inventory/U07-A-FAMILY-MAP.md) owns breadth dispositions; it is not complete recursive/mirror/semantic coverage or CORE.

Batu owns purpose/material phase choices. Assistant owns authorized research, proportionate isolated fixtures, sequencing, package organization and verifiable publication. Writes stay under research/studies/ecc/** plus only ECC discovery changes in shared CATALOG/INDEX. Preserve other studies, concepts, Foundation, soul-context, explorations, upstream and agent-control. No user-home/config/cache mutation, installation, credentials/provider/model calls, upstream report/patch or SOUL/Development OS implementation.

## Next authorized work — U10-A / Q06d1

Begin with the actual S156 entry `ecc2/src/harness_eval.rs`, blob `641275970ba925a398bf2ed1441ca949b6ab5a1e`, 18,300 bytes, fully read in contiguous ranges. Follow main HarnessEvalCommands/dispatcher and the real StateStore methods. Trace candidate/evidence identity → samples/oracle/policy → comparison/health → admission/rollback/audit → actual consumer of the active choice. Examine rejection, stale/invalid inputs or failure ordering and targeted test doubles.

Do not assume recorded scores were generated by a live trial, a health field is independent verification, or an active registry row changes a running worker. Establish the actual contract. PLAN0.18 carries the return condition and the separate following Node capsule/replay framework. No automatic live benchmark, new fixture quota or implementation. Do not repeat the completed Node/Rust bridge or E07 merely for context.

## Recovery route

After canonical bootstrap: STATE → INDEX → META/WHY/METHOD/PLAN/QUESTIONS → Note16/U09-B sources/MR17/current receipt. For load-bearing Rust context recover Note15/A3 sources/MR16/A3 receipt and only required Notes13–14/ledgers/rounds/receipts. E07 README owns its execution limits. Original notes/evidence, not a ledger alone, support stronger synthesis. FULL/SELECTED/test-source/execution classes remain distinct.

Publication is closed. Opening U09-B IN PROGRESS labels and MR17/receipt statements about later checks are chronological history, not a fresh publication task. No old ZIP upload or U09-A retry is required. Same-assistant reading/hash/diff checks are correspondence checks, not independent research validation.

## Preserved history

Full pre-U09-B state/retry account: [STATE at 81381afc](https://github.com/batuhanozgun/agentic-os-search/blob/81381afc5be7d4628def9a41a10a52e6be95ba83/research/studies/ecc/STATE.md). The prior ECC_U09_A3_Unpublished_Checkpoint.zip is historical correspondence; no material unmatched finding was identified, and it is not required for repository-only continuation. Its reading ranges are not merged into canonical source coverage.

U09-A source closure/retry: [PUBLICATION-U09-A3](PUBLICATION-U09-A3.md), through `81381afc5be7d4628def9a41a10a52e6be95ba83`. U09-A2: [receipt](PUBLICATION-U09-A2.md), through `097a074d1b55a04fd08f66ab16ebe5c627c51f13`; first Rust slice: [receipt](PUBLICATION-U09-A.md), through `3b3139cabc33aa9ae1aea64bc0327e4a2aad6894`. U08-A remains source-complete/published: [receipt](PUBLICATION-U08-A.md), through `b4b736d00145ca92e3099733bff9902a2fc3fa3c`. U07-A breadth checkpoint: `0743feae8728faebb48982ec22c447b06f2a0eaa`.

E06 [diagnosis](RECOVERY-U08-A-20260918.md), [quarantine](evidence/u08-a-recovery/README.md) and [recovery receipt](PUBLICATION-U08-A-RECOVERY.md) remain untouched. Both E05 histories remain distinct: [conversation reconciliation](evidence/u06-a-conversation-record/README.md), [main-path evidence](evidence/u06-a-config-probe/README.md). Prior catalogue errors remain in the A3 receipt; this pass's exact matched one-row update does not erase them or prove universal transport reliability. Earlier evidence and concurrent work outside ECC remain protected.
