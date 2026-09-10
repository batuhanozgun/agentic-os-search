# Hermes Agent — Kaynak ve yürütme rotası

2026-09-10 / plan v0.14. Primary pin `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; Work STATE'tedir. U02 general core source incelemesidir, eski deney veya teslim recovery'sinin tekrarı değildir.

## Korunan geçmiş

[Exact v0.9 defteri](SOURCE-LEDGER-THROUGH-V0.9.md), blob `dbd340e8de555307fea331d34f457b8266b9d127`. [V0.13 tam defteri](https://github.com/batuhanozgun/agentic-os-search/blob/c163836d959e3ada2f31afd353bb364671b5fb32/research/studies/hermes-agent/SOURCE-LEDGER.md) önceki AP/M4 kaynak/transfer/koşu ayrıntılarını taşır. Eski ID'ler değişmez.

| Kayıt | Ayrıntılı kaynak rotası |
|---|---|
| H/T ve U01B | [v0.9](SOURCE-LEDGER-THROUGH-V0.9.md), [U01B](evidence/2026-09-07-u01b/SOURCES.md) |
| W01–W08 unpinned | [reading/access](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| D/P caller/transport | [D](evidence/2026-09-08-context-transfer/SOURCES.md) |
| U01B2 skill/onay | [sources](evidence/2026-09-08-u01b2/SOURCES.json) |
| E/C/V worker | [sources](evidence/2026-09-08-worker-policy/SOURCES.md) |
| J/MW manual AST/middleware | [sources](evidence/2026-09-09-review-middleware/SOURCES.md) |
| M2/N memory/pending | [sources](evidence/2026-09-09-memory-pending/SOURCES.md) |
| UI/A | [sources](evidence/2026-09-10-ui-profile/SOURCES.md) |
| M3-S/SA | [sources](evidence/2026-09-10-pending-caller/SOURCES.md) |
| AP | [sources](evidence/2026-09-10-ui-profile-approval/original/evidence/SOURCES.md), [publication](evidence/2026-09-10-ui-profile-approval/PUBLICATION.md) |
| M4 prompt restore | [sources](evidence/2026-09-10-prompt-restore/SOURCES.md), [RESULT](evidence/2026-09-10-prompt-restore/RESULT.json), [publication](evidence/2026-09-10-prompt-restore/PUBLICATION.md) |

A/SA/AP ayrı ve örtüşen koşulardır, bağımsız doğrulama değildir. AP original15 tree `afbe1e767ddaf7e570b72197c7300d20d91f21d4` önceki recovery'de yayımlandı. M4 UTC `2026-09-10T16:11:51.320434+00:00` V01–V08, beş exact archived M2 modülü + manually selected restore/invalidation functions, fake DB/agent/reduced builder. Full-parent/current-wire ölçümü değildi. M4 core11 transfer tree `8dd2cfd73516926b5bc7d1adf0737556c2d6bf61` önceki yayın kaydıdır; bu tur yeniden doğrulanan HERMES koşusu değildir.

## U02 — genel core source trace

**[C01–C18 + reused R01/R02 defteri](evidence/2026-09-10-turn-lifecycle/SOURCES.md)** → [16](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md), [RESEARCH](evidence/2026-09-10-turn-lifecycle/RESEARCH.md). C kimlikleri bu paket-local source kimlikleridir; eski worker C senaryolarıyla karıştırılmaz. C01 turn_context, C04 request assembly, C06 per-attempt, C07 call, C09 tool round, C10/C11 text/stop, C16 persistence ve C17 kanban_stop tam okunmuştur; büyük caller/compaction ve bazı fazlar SELECTED sınırlarıyla ayrı kaydedilir.

C13 actual admitted-compaction caller: invalidate/reload → real build → byte-equal keep → commit/return. C01/C04 yeni active prompt'u API-message kopyasına taşır. C06/C07 middleware/transport sınırı; final network content/timing açık. Eski M4 V04 artificial sıra actual compression diye promote edilmez.

C14/C15/C18 gateway lease/generation/cache/history/result/delivery; C16 actual persistence True/False/None ve DB row projection; C12/C17 task timeout/terminal-nudge kaynak köprüleridir. Bütün SQLite/lease/claim/terminal receipt uygulaması açılmış değildir.

**Yürütme:** bu dilimde HERMES modülü/testi/modeli çalıştırılmadı. Doküman link/hash kontrolleri publication-only'dir. Source reader'ın aynı mekanizmaya yeniden ulaşması independent verification değildir. Kritik karşı yol yeni actual source caller'dır, yeni runtime sonuç değil.

## Sentez, topoloji ve freshness

[Synthesis/02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) ordinary execution modelidir, [synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) learning/change modeli korunur. [CORE-COVERAGE](inventory/CORE-COVERAGE-2026-09-10.md) hedefli map'tir; recursive bütün upstream tree veya tüm içerik listesi değildir.

Default-branch search `77e55b4...` ve web docs sadece navigation. Kod iddiaları primary'ye bağlıdır. Yerel raw materialization DNS hatası connector source okumalarının yokluğu değildir. Saklanan response retrieval tutarsız görünen kritik C13 noktaları direct pinned path/range ile yeniden açıldı. Eski 429 kalıcı engel değil; bu gözlem backend root cause veya gelecek tool availability garantisi değildir.

Current Work: kanban kalıcı task/claim/run/terminal receipt; sonra goal/loop/heartbeat ve SessionDB bağları. Full worker Q26/Q29, last-wire/variant Q07/Q22 ve genel F01–F12 açık. Yayın kimlikleri [PUBLICATION](evidence/2026-09-10-turn-lifecycle/PUBLICATION.md) ile bağlanır; transfer davranış doğrulaması değildir.
