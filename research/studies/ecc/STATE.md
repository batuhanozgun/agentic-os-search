# ECC — STATE

**Updated:** 2026-09-18 — U09-A bounded Rust lifecycle source study COMPLETE / PUBLISHED.
**Last completed unit:** U09-A / Q04g1, across [Note13](notes/13-RUST-SESSION-LIFECYCLE-FIRST-SLICE.md), [Note14](notes/14-STORE-OBSERVER-AND-WORKTREE-CONTINUITY.md) and [Note15](notes/15-EXECUTION-ATTEMPT-OWNERSHIP-AND-REVOCATION.md). Q04g1a/b have bounded source answers. This is not certified runtime safety, complete Rust-controller coverage or completion of ECC.
**Current/next authorized research:** U09-B / Q04g2 Node operator data/action bridge, **NOT STARTED**. There is no unfinished U09-A3 publication task to redo.
**Current publication:** [U09-A3 receipt](PUBLICATION-U09-A3.md), commit `74214867a3c1e1bc29de651d3015299df887fc3b`, fully read back as blob `4ae4d98dfd7c23d6557bd2ddaf958df32ce62b97`. Note15 commit `31d2c30a9345767d85c676bf9901da758b1c7a84`, full readback blob `92402576546ffe0c98084f7c1f538d0b38551f7c`; [A3 sources](evidence/U09-A3-SOURCES.md) commit `98afa49dc060f31ae1b31454d2e87710a3ac73cb`, full readback blob `1956a9c282dc122756c4edff97fafccff3a0620f`. [MR16](ROUND-U09-A3.md) and entry/discovery readbacks completed through `94e029a02eaac5c12072532c71d556ad9018d498` as recorded in the receipt.
**Study:** ACTIVE / PARTIAL. **METHOD / PLAN:** 0.1 / 0.17.
**Unchanged target:** `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a`.
**Publication obligations:** no material output awaits user upload or merge. No branch/PR was created. Final net changes are ECC-local plus only the ECC catalogue row; intermediate catalogue errors and their corrections are explicitly recorded in the receipt.

## Publication retry verified — 2026-09-18

Batu's retry request was reconciled against main `fc8aa2983e986d7b65c07c4558a364949efd1fc3`: U09-A closure and entry alignment were already complete. The [receipt's retry verification](PUBLICATION-U09-A3.md#retry-verification-and-local-packet-disposition--2026-09-18) was then written through the connected GitHub update action in commit `fbeecdca3150a4f19bc8ae6b2a12a399f3dea9f3`, returning blob `94d72428c46f9809e36fc6aa9ab58a5fa9c09fd6`, equal to the prepared candidate. Its added section was read back through EOF; the commit comparison showed only that receipt, +21/-0. The complete pre-edit receipt and STATE bytes had first been matched to their canonical Git-blob hashes.

The prior `ECC_U09_A3_Unpublished_Checkpoint.zip` is historical local correspondence, not a pending upload or replacement patch. Its contents and manifest were checked against the canonical research; no material unmatched finding was identified. Its reading ranges are not merged into the source ledger. The repository is sufficient for research continuation without the archive. Earlier chat and local-draft statements that publication remained pending are superseded by the verified main closure, while their pass-time access limitations remain historical facts rather than an explanation of who published earlier commits.

This retry adds only publication reconciliation to the existing receipt and this STATE. It does not change Note15, source evidence, MR16, PLAN, QUESTIONS, META, INDEX, CATALOG or any other study, and starts no new research or experiment. U09-A remains COMPLETE/PUBLISHED; U09-B/Q04g2 remains next authorized and NOT STARTED. No user upload, branch or merge action is required.

## Current result and evidence boundary

The original U09-A source criterion is mapped to evidence in Note15 section10: actual command/configuration/record/launch, output-to-TUI consumer and effectful observer, stop/resume/resource continuity, then schema/writer/dependency-bound attempt ownership and failure/restart paths. It was not weakened or replaced with a test count. Explaining a mechanism's missing guarantees can complete a source question without certifying the target.

Note15 distinguishes session from execution-attempt identity; stop before versus after admission; post-spawn error from future cancellation; task-handle drop from runtime shutdown; a legal but stale finalizer after same-id resume; and live process from restored supervision. Actual admission/transition guards, normal detachment, signals and database acknowledgments remain positive mechanisms.

These are source observations and conditional schedules, not observed races/orphans, live process-tree termination or restored native context. Cargo.lock resolves Tokio1.53.1 and its tag source was examined, but registry-crate bytes and an actual locked build were not matched. No new experiment/E08, target test, Rust build, model/provider, native host or process signal occurred. E07 remains only its prior SQLite/Git fixture and was not repeated.

Q04g1c preserves stronger empirical/platform/host/dependency/ownership claims and their reopening conditions. Broad Rust scheduling/templates/remote/comms/evaluation, full TUI behavior, every worktree variant and whole-ECC families remain unfinished. Their existence does not erase the completed bounded lifecycle source answer.

## Purpose and authority

Source-grounded ECC research with repository-centred continuity and method evaluation. Comprehensive joint evaluation with Batu remains after completed research; intermediate checks and scoped native synthesis continue. Foundation relevance is a reuse cue, not adopted taxonomy/design. The [U07-A family map](inventory/U07-A-FAMILY-MAP.md) is first-tier coverage, not recursive/mirror/semantic closure or CORE.

Batu owns purpose/material phase choices. Assistant owns authorized research, proportionate isolated fixtures, sequencing, repository organization and verifiable publication. Writes stay under research/studies/ecc/** plus only ECC discovery changes in shared CATALOG/INDEX. Preserve other studies, concepts, Foundation, soul-context, explorations, upstream and agent-control. No user-home/config/cache mutation, installation, credentials/provider/model calls, upstream report/patch or SOUL/Development OS implementation.

## Next authorized work — U09-B / Q04g2

Re-enter S12 `scripts/control-pane.js`, then the known S160 `scripts/lib/control-pane` tree `b1aa05b67fc57ae209dab53abeaa75a8700b22ab`. Follow actual server/state/actions/message-sink imports rather than guessing names. Trace operator request → selected store/executable → mutation/message/process action → refreshed view/error and follow-up. Establish Rust ECC2 versus separate ECC state/work-item boundaries and a material failure/continuation contrast. Similar labels and database paths are not proof of a unified controller.

PLAN0.17 supplies the bounded return condition. Follow Rust again only where a new caller makes it load-bearing; do not redo Notes13–15 or rerun E07 for context. Separate evaluation, scheduling/native workflow, host/provider, release/scanner/observability, native synthesis and final omission checks remain in PLAN/QUESTIONS. No automatic live runtime/model campaign or whole-ECC closure.

## Recovery path

After canonical bootstrap: STATE → INDEX → META/WHY/METHOD/PLAN/QUESTIONS → Note15/A3 sources/MR16/current receipt. Recover Notes13–14 and their ledgers/rounds/receipts for parent lifecycle context; E07 README for its execution limits. For older load-bearing claims, use Note12/U08-A sources/round/receipt and U07-A family map/ledger/receipt. Original evidence, not a ledger alone, supports stronger synthesis. Full-versus-selected coverage remains explicit.

Current publication is closed. Receipt/MR16 pass-time statements about later checking and old U09-A IN PROGRESS frontiers are historical, not fresh work instructions. The receipt also preserves two actual shared-catalogue recopy errors, corrected before final closure; the final net delta is only ECC. Do not claim those faulty intermediate writes never reached main, or that a final correct diff proves transport reliability. Publication checks are same-assistant correspondence/consistency, not independent research validation.

## Preserved history

U09-A2: `097a074d1b55a04fd08f66ab16ebe5c627c51f13`, [receipt](PUBLICATION-U09-A2.md). First Rust slice: `3b3139cabc33aa9ae1aea64bc0327e4a2aad6894`, [receipt](PUBLICATION-U09-A.md). U08-A remains source-complete/published through `b4b736d00145ca92e3099733bff9902a2fc3fa3c`, [receipt](PUBLICATION-U08-A.md). U07-A breadth checkpoint: `0743feae8728faebb48982ec22c447b06f2a0eaa`.

Historical E06 remains unverified/excluded: [diagnosis](RECOVERY-U08-A-20260918.md), [quarantine/checks](evidence/u08-a-recovery/README.md), [recovery receipt](PUBLICATION-U08-A-RECOVERY.md). Neither E07 nor this source work recovers or replaces it. Both E05 histories stay separate: [conversation reconciliation](evidence/u06-a-conversation-record/README.md), [main-path record](evidence/u06-a-config-probe/README.md). Earlier evidence and concurrent work outside ECC must remain intact.
