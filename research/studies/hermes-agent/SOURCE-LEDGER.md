# Hermes Agent — Kaynak ve yürütme rotası

2026-09-10 / plan v0.12. Primary pin `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; current Work STATE'tedir. Bu checkpoint AP özgün teslimini kaydeder; yeni upstream araştırması veya eski deney tekrarı değildir.

## Korunan geçmiş

[Exact SOURCE-LEDGER-THROUGH-V0.9](SOURCE-LEDGER-THROUGH-V0.9.md), eski blob `dbd340e8de555307fea331d34f457b8266b9d127` ile korunur. [v0.11 tam defter](https://github.com/batuhanozgun/agentic-os-search/blob/634ab66f195130d551d58dfc062639e0feec23fa/research/studies/hermes-agent/SOURCE-LEDGER.md) UI/A ve M3-S/SA aktarım tarihçesini taşır. Hiçbir eski ID yeniden numaralanmadı.

| Kayıt | Kaynak / yürütme |
|---|---|
| İlk H/T ve skill U01B | [v0.9 defteri](SOURCE-LEDGER-THROUGH-V0.9.md), [U01B sources](evidence/2026-09-07-u01b/SOURCES.md) |
| W01–W08 unpinned | [W reading/access](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| D01–D22 / transport | [D sources](evidence/2026-09-08-context-transfer/SOURCES.md) |
| U01B2 skill/onay | [sources](evidence/2026-09-08-u01b2/SOURCES.json) |
| E/C/V selected worker | [sources](evidence/2026-09-08-worker-policy/SOURCES.md) |
| J/MW middleware/manual AST | [sources](evidence/2026-09-09-review-middleware/SOURCES.md) |
| M2/N memory/pending | [sources](evidence/2026-09-09-memory-pending/SOURCES.md) |
| UI/A01–A08 | [UI sources](evidence/2026-09-10-ui-profile/SOURCES.md), [result](evidence/2026-09-10-ui-profile/RESULT.json) |
| M3-S/SA01–SA08 | [SA sources](evidence/2026-09-10-pending-caller/SOURCES.md), [result](evidence/2026-09-10-pending-caller/POLICY-RESULT.json) |
| **AP/UI-local/AP01–AP06** | **[AP sources](evidence/2026-09-10-ui-profile-approval/original/evidence/SOURCES.md)**, [result](evidence/2026-09-10-ui-profile-approval/original/evidence/ACCESS-RESULT.json) |

AP'nin local UI01–UI11 numaraları UI/A defterindekileri yeniden tanımlamaz. Canonical atıfta package + local ID birlikte kullanılır. AP UTC 05:40:37, A UTC 05:42:55, SA UTC 05:12:08 koşuları ayrı tutulur. Tek actual slash_access.py blob'u `07204201e411f29f912bb9bba6beec0566acab9d` ortak; config/source holder'ları sentetik. A'nın semantic mutantı yalnız A'ya aittir. Örtüşen source gözlemleri independent corroboration sayılmaz.

## AP aktarımı

[PUBLICATION](evidence/2026-09-10-ui-profile-approval/PUBLICATION.md), [TRANSFER-CHECK](evidence/2026-09-10-ui-profile-approval/TRANSFER-CHECK.json). 25054-byte ZIP, SHA-256 `fccfac09b4b104ee46e43eb750fc3d02e62ae7e1ab1a84fe964dd3f361d5dfb2`. On dört manifest girdisi ve manifestin kendisi dahil on beş dosya; local/GitHub recursive original tree `afbe1e767ddaf7e570b72197c7300d20d91f21d4` eşleşti. Bu kaynak/ürün doğruluğu değil, transfer bütünlüğüdür. Hiçbir eski deney yeniden koşulmadı.

## Kapsam ve sonraki kaynak

[Kapsam değerlendirmesi](inventory/SCOPE-REVIEW-2026-09-10.md) yeni yöntemsel değerlendirmedir; upstream mekanizma bulgusu değildir. Sonraki teknik rota 13/M3-S12/S13 → `_restore_or_build_system_prompt` → invalidate/rebuild/compression/cache → prepared request. Full/selected/actual/synthetic sınırları ayrıca tutulacak. Q26 full originals, W freshness, gerçek provider ve bütün platform/quality soruları açıktır.
