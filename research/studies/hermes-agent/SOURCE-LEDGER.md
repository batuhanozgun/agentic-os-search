# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-13 / U12 / plan v0.25.** Current work [STATE](STATE.md). Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest0.21.0. Kaynak okuma, native diagnostic, sentez ve yayın ayrı statülerdir.

## U12 — Araç kabulü ve delegation, yeni execution yok

[27](notes/27-TOOL-ADMISSION-AND-DELEGATION.md) → [A TOOL-ADMISSION](evidence/2026-09-13-tool-delegation/TOOL-ADMISSION.md)/[S01–S07](evidence/2026-09-13-tool-delegation/TOOL-SOURCES.md) → [B DELEGATION-LIFECYCLE](evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md)/[S08–S15](evidence/2026-09-13-tool-delegation/DELEGATION-SOURCES.md). [NOT RUN](evidence/2026-09-13-tool-delegation/CHECKS-NOT-RUN.md), [PUBLICATION](evidence/2026-09-13-tool-delegation/PUBLICATION.md).

A: tool_executor ve turn_tool_validation full; turn_tool_round/model_tools/registry/file_tools/dispatch_helpers selected. B: delegate_tool, child toolsets, batch dispatch, child run, config, results, live registry, async delegation sekiz dosya full-read. Tam aralıklar/blob'lar local kaynak defterlerindedir. FULL READ local-byte materialization, dependency closure veya execution değildir. Yeni child/tool/model/DB/SDK/OS/suite çalıştırması ve RESULT yoktur.

Başlangıç planı0fd4b597002eb478cd1ed913a588ba44fe70edb3 ve A ef51c3f4b1d4d94038a428fa9bac1a21dfda778f actual main/ref/content/scope ile doğrulandı; sonra B açıldı. Ayrı harness commit'i bc99f6e9661bcbbaba9fb2db7332ebad16756775 korunur ve bu çalışmaya atfedilmez. A'nın TOOL-ADMISSION/TOOL-SOURCES özgün metinleri B'de değişmez. Q54 source-advanced; actual parent completion consumer Q57 ilk next, eski residual'lar açık.

## U11 — Korunan runtime/backend kaynak birimi

[26](notes/26-RUNTIME-BACKEND-AND-CONTROL-OWNERSHIP.md) → [A RESEARCH](evidence/2026-09-12-runtime-backend/RESEARCH.md)/[A SOURCES](evidence/2026-09-12-runtime-backend/SOURCES.md) → [B BACKEND-OWNERSHIP](evidence/2026-09-12-runtime-backend/BACKEND-OWNERSHIP.md)/[B SOURCES](evidence/2026-09-12-runtime-backend/BACKEND-SOURCES.md). [NOT RUN](evidence/2026-09-12-runtime-backend/CHECKS-NOT-RUN.md), [PUBLICATION](evidence/2026-09-12-runtime-backend/PUBLICATION.md).

U11 S01–S16'nın full/selected kapsamları kendi defterlerindedir; yeni SDK/native process/model/DB/credential/suite koşusu yoktur. Başlangıç d3a4baeeb7afd97d38588c674c4842f01e87c6f0, A e562de82ab4ea33872e55d501c8b59f26b441fa8, B f29058678d922497a5ed38b2ef89636d58f828de, makbuz6a9a8c48204102d592780971a212b363ec97bc98. Bunlar yeniden yayımlanacak işler değildir. Q55/Q56 source sınırlarını U12 yeniden test etmez.

## U10 — Korunan kaynak ve tek bounded koşu

[25](notes/25-CRON-EXECUTION-AND-CONTEXT.md) → [S01–S10](evidence/2026-09-12-cron-execution-context/SOURCES.md) → [RESEARCH](evidence/2026-09-12-cron-execution-context/RESEARCH.md) / [NOT RUN](evidence/2026-09-12-cron-execution-context/CHECKS-NOT-RUN.md). S01 scheduler selected; S02 prompt full+selector execution; S03 monitor/S04 notepad/S05 script/S06 preflight full-read not-run; S07 agent_init selected; S08 detached teardown full-read not-run; S09 run_agent selected; S10 MIT.

S02 blob91d673649d6dca8ba3120d10671a8966e67a01ce,16.049 byte; source SHA-256 bc5fecf6dc019ad7dec221c4a0913685d07e33a3a9a974e5fca0cb5962c6654c. [SPEC](evidence/2026-09-12-cron-execution-context/SPEC.md)/[tam RESULT](evidence/2026-09-12-cron-execution-context/RESULT.json)/[MANIFEST/raw](evidence/2026-09-12-cron-execution-context/MANIFEST.json). C01–C06 actual local files/mtime/read, synthetic root/unused imports; full builder/run_job/model/SQLite/network NOT RUN. N00 source-identity, N01 order/N02 cap source mutants. UTC2026-09-12T07:25:53.109130+00:00–07:25:53.118497+00:00; bir başarılı run. RESULT SHA-256 cdf30b7cb1b599b3b87d2d757bfaa26ed93508669f0c26f0b6c639b95b0537f7.

Attempt-00 parse failure vaka öncesidir; özgün probe/log ve dar revision korunur. Eski testler yeniden koşulmadı. Raw yalnız S02/S10 ve diagnostic kanıtlarıdır, bütün parent kaynaklar değil. [synthesis04](synthesis/04-SCHEDULED-WORK-AND-CONTEXT-PROVISIONAL.md) derived U07–U10 açıklamasıdır, bağımsız evidence değil.

## Tamamlanmış önceki rotalar

| Birim | Kanıt yolu |
|---|---|
| U09 /24 | [RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md)/[SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md)/[NOT RUN](evidence/2026-09-12-cron-occurrence-admission/CHECKS-NOT-RUN.md)/[PUBLICATION](evidence/2026-09-12-cron-occurrence-admission/PUBLICATION.md); T0–T4 source-only |
| U08 /23 | [SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md)/[RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md) → SPEC/RESULT/MANIFEST/raw; B native async bridge, synthetic transport |
| U07 /22 | [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md) → SPEC/RESULT/MANIFEST/raw; D native queue/temp SQLite |
| U06 /21 | [SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md)/[RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md) → SPEC/RESULT/MANIFEST/raw; L process-local lease |
| U05 /20 | [SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md)/[NOT RUN](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md) |
| U04-A/B | [A SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [B RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json); exact raw/probe yolları |
| U03/U02 | [Kanban SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md), [Turn SOURCES](evidence/2026-09-10-turn-lifecycle/SOURCES.md) |

Önceki source/hash/date/disposition zinciri [exact U11 ledger](https://github.com/batuhanozgun/agentic-os-search/blob/6a9a8c48204102d592780971a212b363ec97bc98/research/studies/hermes-agent/SOURCE-LEDGER.md) → U10/v0.22 ve [through-v0.9](SOURCE-LEDGER-THROUGH-V0.9.md) ile korunur. U04-B33 original subtree d01c92f7414713300934be3bb4e3d40ac57631b3. A/B/L/D/B/C kimlikleri eş vaka veya independent replication değildir. Önceki evidence değiştirilmedi.

U12'nin mutable navigation/default-branch ve raw erişim sınırları TOOL-SOURCES/DELEGATION-SOURCES'tadır. Primary upgrade/current fix kararı yok. Yayın/ref/diff/readback yalnız aktarım ve süreklilik kontrolüdür; HERMES davranış deneyi değildir.
