# Hermes Agent — Kaynak ve yürütme rotası

2026-09-10 / plan v0.13. Primary pin `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; Work STATE'tedir. Aynı turda AP recovery ve sonra yeni M4 araştırma/koşu/sentez ayrılır.

## Korunan geçmiş

[Exact v0.9 defteri](SOURCE-LEDGER-THROUGH-V0.9.md) blob `dbd340e8de555307fea331d34f457b8266b9d127` korunur. [v0.12 defteri](https://github.com/batuhanozgun/agentic-os-search/blob/a14c8152a918a3379b4a0d6d67af9f7aece2f70e/research/studies/hermes-agent/SOURCE-LEDGER.md) AP/önceki aktarım kimliklerini taşır. Eski ID'ler değişmez.

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
| AP local-UI/AP01–AP06 | [sources](evidence/2026-09-10-ui-profile-approval/original/evidence/SOURCES.md), [publication](evidence/2026-09-10-ui-profile-approval/PUBLICATION.md) |

A/SA/AP'nin local ID'leri package ile birlikte kullanılır. Ortak slash_access blob'u üç bağımsız source veya koşu toplamı yapmaz. A semantic mutantı diğerlerine aktarılmaz. AP 15 original tree `afbe1e767ddaf7e570b72197c7300d20d91f21d4` checkpoint a14c815'te kaydedildi; eski deneyler tekrarlanmadı.

## M4 — yeni source ve execution

**[M4 tam defteri](evidence/2026-09-10-prompt-restore/SOURCES.md)** → [15](notes/15-MEMORY-PROMPT-RESTORE-BOUNDARIES.md), [RESEARCH](evidence/2026-09-10-prompt-restore/RESEARCH.md).

M4-S01 loop parent `2e88c103275d756cfe8cb0e092b309f5f4406cb2`, selected 500–780/755–900; dört complete restore/identity definition. M4-S02 system_prompt parent `9bd52f03fc7568990f2bf157dc1301f9c81adbbb`, selected 430–750/EOF; iki memory/invalidate definition executed, builder/static-prefix source only. M4-S03 main loop callback/phase bağları stored-response source read. Büyük parent dosyaları locally full-byte verified veya full executed değildir.

**Koşu UTC `2026-09-10T16:11:51.320434+00:00`:** [V01–V08 RESULT](evidence/2026-09-10-prompt-restore/RESULT.json), [SPEC](evidence/2026-09-10-prompt-restore/SPEC.md), [probe](evidence/2026-09-10-prompt-restore/probe.py). Beş exact M2 upstream modülü ve setup/helpers tekrar kullanıldı; eski N suite'i değil. Sentetik DB/agent/reduced builder ve belirtilmiş çevre. Endpoint cached-prompt seçimi/disk-live-frozen/fake DB; actual final request değil. İki identity kontrolü ve iki separate comparator mutantı recorded. Local selection hash parent fidelity ispatı değildir.

Çekirdek 11 dosyanın local/GitHub recursive tree kimliği `8dd2cfd73516926b5bc7d1adf0737556c2d6bf61` eşleşti (`truncated:false`). [MANIFEST](evidence/2026-09-10-prompt-restore/MANIFEST.json), [PUBLICATION](evidence/2026-09-10-prompt-restore/PUBLICATION.md). Transfer, behavior verification'dan ayrıdır.

## Türetilmiş üst katman ve açık kaynak

[Synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md), 02–15 notlarından türetilmiş ilk provisional alt-sistem açıklamasıdır; yeni bağımsız source veya whole-product verdict değildir. [SCOPE-REVIEW](inventory/SCOPE-REVIEW-2026-09-10.md) mevcut kanıt/kapsam değerlendirmesidir.

turn_context, request assembly ve sonraki system-prompt isteği 429 nedeniyle tam açılamadı. Saklanmış yanıttan full tail/callsite geri okundu; erişim engelinin etrafından dolaşılmadı. Q07/Q22 actual caller/request, Q26 full originals/worker, W freshness, full profile/scanner/quality açık. Sonraki aktif genel loop/context/session ve geniş topoloji kontrolü bu köprüleri doğru kapsamda geri açar.
