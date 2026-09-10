# Hermes Agent — Birikimli kaynak ve yürütme rotası

**Güncel ek:** 2026-09-10 / U01-M3. Primary pin `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`. Current work authority STATE; bu dosya kaynak/okuma/yürütme router'ıdır.

## Önceki tam kayıt — değiştirilmeden korunur

**[SOURCE-LEDGER-THROUGH-V0.9.md](SOURCE-LEDGER-THROUGH-V0.9.md)**, `91af4415c22e05b80484b935383ceeb04a3c5b7b` içindeki önceki birikimli defterin exact blob kopyasıdır: `dbd340e8de555307fea331d34f457b8266b9d127`. Aynı package root'unda tutulduğu için göreli kanıt bağlantıları korunur. H01–H22, U01B S, W01–W08, D01–D22, E/C/V, J/MW ve M2-S/R/N kimlikleri yeniden numaralandırılmadı veya silinmedi.

Bu donmuş defter **v0.9'a kadarki kaynak/koşu/aktarım tarihçesidir**. İçindeki eski current/next-work ve publication cümleleri tarihsel anlamdadır; bugünkü devam sırası STATE/plan v0.10'dur. Progressive retrieval için eski ayrıntı ile yeni kaynak dilimi ayrıldı; yeni teknik deney veya kaynak yeniden-doğrulaması sayılmaz.

| Önceki soru | Derin kayıt |
|---|---|
| H/S kimlikleri, ilk keşif/review/curator/skill mutator | Donmuş defter H ve U01B bölümleri; [U01B SOURCES](evidence/2026-09-07-u01b/SOURCES.md) |
| Unpinned web sözleşmeleri ve tarihsel erişim | [W defteri](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| Pinned caller/worker/store ve P transport | [D defteri](evidence/2026-09-08-context-transfer/SOURCES.md) |
| U01B2 arşiv deneyi | [U01B2 SOURCES](evidence/2026-09-08-u01b2/SOURCES.json) |
| Selected executor/policy ile C/V | [E defteri](evidence/2026-09-08-worker-policy/SOURCES.md) |
| Gerçek review/round/Relay, manuel AST, exact middleware | [J defteri](evidence/2026-09-09-review-middleware/SOURCES.md) |
| Beş-modül memory/pending N01–N12 | [M2 defteri](evidence/2026-09-09-memory-pending/SOURCES.md) |

## UI01–UI13 / U01-M3 — yeni kaynak ve koşu

**[Tam UI defteri](evidence/2026-09-10-ui-profile/SOURCES.md)** her path/blob/satır aralığını ve actual/synthetic sınırını taşır. [12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md) → [RESEARCH](evidence/2026-09-10-ui-profile/RESEARCH.md).

UI01–UI07: gerçek CLI/gateway command handlers, busy/inbound/adapter wiring, profile scopes ve home override önceliği; SELECTED SOURCE READ, NOT EXECUTED. UI09: routed-profile config-write upstream testinin FULL READ'i, NOT RUN. UI10–UI13: mevcut M2 exact arşiv kaynaklarının yeniden kullanımı; yeni M2 execution değil.

**UI08:** `gateway/slash_access.py`, blob `07204201e411f29f912bb9bba6beec0566acab9d`, 5666 byte. FULL READ, tam local Git blob doğrulaması ve A01–A08 EXECUTED. Koşu UTC `2026-09-10T05:42:55.258536+00:00`, Python 3.13.5/Linux. [RESULT](evidence/2026-09-10-ui-profile/RESULT.json), [SPEC](evidence/2026-09-10-ui-profile/SPEC.md), [probe](evidence/2026-09-10-ui-profile/policy_probe.py). Config/platform/source holders sentetik; gerçek gateway/ingress/profile/handler/store/provider koşusu yok. Bozuk dosya gerçek import guard'ında reddedildi; ayrı always-allow test mutantını ret oracle'ı yakaladı.

A01–A08 source-informed exploratory diagnostiktir; ürün PASS veya independent researcher doğrulaması değildir. Önceki N/MW/C/V/P testleri tekrarlanmadı. Eski M2 canlı/disk/frozen sonuçları actual caller source seçimine bağlandı, fakat full UI runtime veya gerçek request ölçümüne yükseltilmedi.

Yeni 10 dosyalık evidence core'un local bytes'tan hesaplanan ve GitHub recursive tree olarak geri okunan kimliği `1052daf850945e5644239030d88fc2012305c1c2` eşleşti. Bu transfer kimliğidir; davranış kapsamı artmaz. [MANIFEST](evidence/2026-09-10-ui-profile/MANIFEST.json) ve [PUBLICATION](evidence/2026-09-10-ui-profile/PUBLICATION.md).

## Freshness ve ilk açık halka

Primary değişmedi; default-branch `cfdbbb6...` araması yalnız navigasyondu. Büyük dosyaların direct raw materyalizasyonunda DNS/cache-miss olmasına rağmen connector kaynak okuması çalıştı; bu source absence değildir. GitHub yazma çağrıları bu tur çalıştı; gelecek tool availability garantisi değildir.

İlk aktif halka Q07/Q22: apply sonrasında gerçek CLI/cached gateway disk/store/frozen/prompt/prepared request. UI01–UI07 bütün profile/auth/hook/transport varyantlarını kapatmaz. Q26/Q29 full-original/full-worker ve geniş F01–F12 soruları açık; ayrıntı STATE/plan/OPEN-QUESTIONS'tadır. Kaynak kimliği, source fidelity, bounded execution ve product effectiveness birbirinin yerine geçmez.
