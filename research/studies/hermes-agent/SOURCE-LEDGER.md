# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-12 / U11 / plan v0.24.** Current work [STATE](STATE.md). Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest 0.21.0. Source reading, native diagnostic, sentez ve yayın ayrı statülerdir.

## U11 — Incremental kaynak çalışması; yeni execution yok

[26](notes/26-RUNTIME-BACKEND-AND-CONTROL-OWNERSHIP.md) → [A RESEARCH](evidence/2026-09-12-runtime-backend/RESEARCH.md)/[S01–S04](evidence/2026-09-12-runtime-backend/SOURCES.md) → [B BACKEND-OWNERSHIP](evidence/2026-09-12-runtime-backend/BACKEND-OWNERSHIP.md)/[S05–S16](evidence/2026-09-12-runtime-backend/BACKEND-SOURCES.md). [NOT RUN](evidence/2026-09-12-runtime-backend/CHECKS-NOT-RUN.md), [PUBLICATION](evidence/2026-09-12-runtime-backend/PUBLICATION.md).

S01 runtime_provider/S02 init selected; S03 turn_facade full; S04 conversation_loop selected. B: native codex_runtime selected; native session/client/projector full; ordinary API caller/helper/run_agent selected; MCP server full; docs selected. Dosya kimliği ve native satır aralıkları kendi kaynak defterlerinde. FULL READ, full-byte materyalizasyon, dependency closure ve execution eşit değildir. Hiçbir yeni SDK/native subprocess/model/DB/API/credential veya upstream test suite koşusu yapılmadı. U11 RESULT veya başarı sayacı yoktur.

Başlangıç checkpoint'i d3a4baeeb7afd97d38588c674c4842f01e87c6f0 ve A e562de82ab4ea33872e55d501c8b59f26b441fa8 main/ref ve içerikten geri okundu; sonra B açıldı. A'nın özgün RESEARCH/SOURCES dosyaları B'de korunur. Source-only iddialar conditional binding/history/control/receipt sınırlarıdır; gerçek yanlış model veya data-loss sonucu değildir. Current first-new-source Q54; Q55/Q56 ve bütün eski residual'lar açık.

## U10 — Korunan kaynak ve tek bounded koşu

[25](notes/25-CRON-EXECUTION-AND-CONTEXT.md) → **[S01–S10](evidence/2026-09-12-cron-execution-context/SOURCES.md)** → [RESEARCH](evidence/2026-09-12-cron-execution-context/RESEARCH.md) / [NOT RUN](evidence/2026-09-12-cron-execution-context/CHECKS-NOT-RUN.md). S01 scheduler selected; S02 prompt full+selector execution; S03 monitor/S04 notepad/S05 script/S06 preflight full-read not-run; S07 agent_init selected; S08 detached teardown full-read not-run; S09 run_agent selected; S10 MIT.

S02 blob `91d673649d6dca8ba3120d10671a8966e67a01ce`, 16.049 byte; source SHA-256 `bc5fecf6dc019ad7dec221c4a0913685d07e33a3a9a974e5fca0cb5962c6654c`. [SPEC](evidence/2026-09-12-cron-execution-context/SPEC.md)/[tam RESULT](evidence/2026-09-12-cron-execution-context/RESULT.json)/[MANIFEST/raw](evidence/2026-09-12-cron-execution-context/MANIFEST.json). C01–C06 actual local files/mtime/read, synthetic root/unused imports; full builder/run_job/model/SQLite/network NOT RUN. N00 source-identity, N01 order/N02 cap explicit source mutants. UTC 2026-09-12T07:25:53.109130+00:00–07:25:53.118497+00:00; one successful run. RESULT SHA-256 `cdf30b7cb1b599b3b87d2d757bfaa26ed93508669f0c26f0b6c639b95b0537f7`.

Attempt-00 parse error precedes all cases; original probe/log and exact narrow revision archived. Old tests not rerun. Raw archive includes only S02/S10 and diagnostic evidence, not all parent files. [synthesis04](synthesis/04-SCHEDULED-WORK-AND-CONTEXT-PROVISIONAL.md) is derived U07–U10 explanation, not independent evidence.

## Tamamlanmış önceki rotalar

| Birim | Kanıt yolu |
|---|---|
| U09 /24 | [RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md)/[SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md)/[NOT RUN](evidence/2026-09-12-cron-occurrence-admission/CHECKS-NOT-RUN.md)/[PUBLICATION](evidence/2026-09-12-cron-occurrence-admission/PUBLICATION.md); T0–T4 source-only |
| U08 /23 | [SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md)/[RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md) → SPEC/RESULT/MANIFEST/raw; B native async bridge, synthetic transport |
| U07 /22 | [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md) → SPEC/RESULT/MANIFEST/raw; D native queue/temp SQLite |
| U06 /21 | [SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md)/[RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md) → SPEC/RESULT/MANIFEST/raw; L process-local lease |
| U05 /20 | [SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md)/[NOT RUN](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md) |
| U04-A/B | [A SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [B RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json); exact raw/probe yolu bunlarda |
| U03/U02 | [Kanban SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md), [Turn SOURCES](evidence/2026-09-10-turn-lifecycle/SOURCES.md) |

Önceki bütün source/hash/date/disposition zinciri [exact U10 ledger](https://github.com/batuhanozgun/agentic-os-search/blob/b658913dd8148dd9a4850414159f13513904f137/research/studies/hermes-agent/SOURCE-LEDGER.md) → exact v0.22 ve [through-v0.9](SOURCE-LEDGER-THROUGH-V0.9.md) üzerinden korunur. U04-B 33 original subtree d01c92f7414713300934be3bb4e3d40ac57631b3. A/B/L/D/B/C ID'leri case veya independent replication eşitliği değildir. Eski hiçbir evidence dosyası yeniden yazılmadı.

U10'un default-branch 28326a6ccd7484f37bbcd19c9f32658c2368b370 pointer'ları tarihsel navigation only kaydıdır. U11 yeni default-branch pointer'larını kendi SOURCES dosyaları taşır; current fix doğrulaması veya primary upgrade yok. U10 yayın [PUBLICATION](evidence/2026-09-12-cron-execution-context/PUBLICATION.md)'da; hash/link/tar kontrolleri behavior test değildir.
