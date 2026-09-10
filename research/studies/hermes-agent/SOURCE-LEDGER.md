# Hermes Agent — Birikimli kaynak ve yürütme rotası

**Güncel ek:** 2026-09-10 / U01-M3 ayrı M3-S/SA tesliminin yayını, plan v0.11. Primary pin `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`. Current work authority STATE; bu dosya kaynak/okuma/yürütme router'ıdır.

## Önceki tam kayıt — değiştirilmeden korunur

**[SOURCE-LEDGER-THROUGH-V0.9.md](SOURCE-LEDGER-THROUGH-V0.9.md)**, `91af4415c22e05b80484b935383ceeb04a3c5b7b` içindeki önceki birikimli defterin exact blob kopyasıdır: `dbd340e8de555307fea331d34f457b8266b9d127`. Aynı package root'unda tutulduğu için göreli kanıt bağlantıları korunur. H01–H22, U01B S, W01–W08, D01–D22, E/C/V, J/MW ve M2-S/R/N kimlikleri yeniden numaralandırılmadı veya silinmedi.

Bu donmuş defter v0.9'a kadarki kaynak/koşu/aktarım tarihçesidir. İçindeki eski current/next-work cümleleri tarihsel anlamdadır; bugünkü sıra STATE/plan v0.11'dir. V0.10'un UI/A kaydı aşağıda korunur; bu yeni yayın eski deneylerin tekrarı veya upstream revalidation değildir.

| Önceki soru | Derin kayıt |
|---|---|
| H/S kimlikleri, ilk keşif/review/curator/skill mutator | Donmuş defter H ve U01B bölümleri; [U01B SOURCES](evidence/2026-09-07-u01b/SOURCES.md) |
| Unpinned web sözleşmeleri ve tarihsel erişim | [W defteri](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| Pinned caller/worker/store ve P transport | [D defteri](evidence/2026-09-08-context-transfer/SOURCES.md) |
| U01B2 arşiv deneyi | [U01B2 SOURCES](evidence/2026-09-08-u01b2/SOURCES.json) |
| Selected executor/policy ile C/V | [E defteri](evidence/2026-09-08-worker-policy/SOURCES.md) |
| Gerçek review/round/Relay, manuel AST, exact middleware | [J defteri](evidence/2026-09-09-review-middleware/SOURCES.md) |
| Beş-modül memory/pending N01–N12 | [M2 defteri](evidence/2026-09-09-memory-pending/SOURCES.md) |

## UI01–UI13 / U01-M3 — v0.10 kaydı korunur

**[Tam UI defteri](evidence/2026-09-10-ui-profile/SOURCES.md)** her path/blob/satır aralığını ve actual/synthetic sınırını taşır. [12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md) → [RESEARCH](evidence/2026-09-10-ui-profile/RESEARCH.md).

UI01–UI07: gerçek CLI/gateway command handlers, busy/inbound/adapter wiring, profile scopes ve home override önceliği; SELECTED SOURCE READ, NOT EXECUTED. UI09: routed-profile config-write upstream testinin FULL READ'i, NOT RUN. UI10–UI13: mevcut M2 exact arşiv kaynaklarının yeniden kullanımı; yeni M2 execution değil.

**UI08:** `gateway/slash_access.py`, blob `07204201e411f29f912bb9bba6beec0566acab9d`, 5666 byte. FULL READ, tam local Git blob doğrulaması ve A01–A08 EXECUTED. Koşu UTC `2026-09-10T05:42:55.258536+00:00`, Python 3.13.5/Linux. [RESULT](evidence/2026-09-10-ui-profile/RESULT.json), [SPEC](evidence/2026-09-10-ui-profile/SPEC.md), [probe](evidence/2026-09-10-ui-profile/policy_probe.py). Config/platform/source holders sentetik; gerçek gateway/ingress/profile/handler/store/provider koşusu yok. Bozuk dosya gerçek import guard'ında reddedildi; ayrı always-allow test mutantını ret oracle'ı yakaladı.

A01–A08 source-informed exploratory diagnostiktir; ürün PASS veya independent researcher doğrulaması değildir. Önceki N/MW/C/V/P testleri o araştırmada tekrarlanmadı. M2 canlı/disk/frozen sonuçları actual caller source seçimine bağlandı, full UI runtime veya request ölçümüne yükseltilmedi.

UI evidence core'un local bytes ve GitHub recursive tree kimliği `1052daf850945e5644239030d88fc2012305c1c2` olarak kayıtlıdır; bu yayında yeniden koşulmadı. [MANIFEST](evidence/2026-09-10-ui-profile/MANIFEST.json) ve [PUBLICATION](evidence/2026-09-10-ui-profile/PUBLICATION.md) değişmeden korunur.

## M3-S01–S13 / SA01–SA08 — ayrı teslim

[13 giriş](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md) → [tam M3-S SOURCES](evidence/2026-09-10-pending-caller/SOURCES.md), [RESEARCH](evidence/2026-09-10-pending-caller/RESEARCH.md). UI kimlikleriyle karıştırma. Tam defter exact path/blob, FULL/SELECTED/EXECUTED ve kaynak aralıklarıdır; büyük dosyalar yerelde tam kaynak diye saklanmamıştır.

M3-S01–S08: CLI/gateway caller, adapter, inbound/busy, run, authz ve home kaynak seçkileri. M3-S09: UI08 ile aynı tam slash_access.py blob'u. M3-S10: upstream test kaynağı FULL READ/NOT RUN. M3-S11: multiplex design belgesi FULL READ/TARGET CLAIM. M3-S12/S13: system_prompt.py ve turn_context.py seçkileri, memory_parts/build/invalidate/cache bağı; gerçek prepared request ölçümü değil.

**SA koşusu:** UTC `2026-09-10T05:12:08.954654+00:00`, Python 3.13.5/Linux; [POLICY-RESULT](evidence/2026-09-10-pending-caller/POLICY-RESULT.json), [SPEC](evidence/2026-09-10-pending-caller/SPEC.md), [probe](evidence/2026-09-10-pending-caller/policy_probe.py). Yalnız S09 ithal edildi; synthetic config/source holder'ları. Sekiz source-informed beklenti ve gerçek bozuk-source pre-import reddi. SA06 supplied config/profile etiketi duyarlılığı deployment izolasyon kusuru değildir; SA08 boş chat_type normal adapter hatası değildir.

UI/A ve SA aynı koşu değildir: test kodu, senaryolar ve negatif kontroller farklıdır. A kaydının always-allow mutantı SA'ya aktarılmaz; örtüşen kaynaklar independent evidence sayılmaz. Bu yayın hiçbirini tekrar çalıştırmadı. [M2 arşiv-source kontrolü](evidence/2026-09-10-pending-caller/REUSED-SOURCE-CHECK.json) yeni M2 yürütmesi değildir.

**Aktarım:** [PUBLICATION](evidence/2026-09-10-pending-caller/PUBLICATION.md), [TRANSFER-CHECK](evidence/2026-09-10-pending-caller/TRANSFER-CHECK.json). ZIP'in 18 özgün dosyası korunur; tüm özgünler yeniden konumlandırıldıktan sonra local/remote tree `246a833b3a13414be817a02fa58f4b5259126fb0` eşleşir. Özgün 12 taslağı delivery altında tarihsel kalır, current giriş 13'tür. Eski NOT PUBLISHED aktif engel değildir.

## Freshness ve ilk açık halka

Primary değişmedi; moving-branch search ref'leri yalnız navigasyondu. W belgeleri unpinned, current HEAD/kurulu release doğrulanmamış kalır. M3-S/SA aktarımı yeni upstream kontrolü değildir. Geçmiş DNS/cache/tool-resource hataları kaynak yokluğu veya gelecek kabiliyet garantisi değildir.

İlk aktif halka Q07/Q22: apply sonrasında gerçek CLI/cached gateway disk/store/frozen/stored prompt/prepared request. Somut ilk soru `_restore_or_build_system_prompt`, ardından compression/keep-prompt ve cache yaşam döngüsü. Tam profile/auth/hook/transport varyantları, Q26/Q29 full-original/full-worker ve F01–F12 açık. Kaynak kimliği, fidelity, bounded execution ve product effectiveness birbirinin yerine geçmez.
