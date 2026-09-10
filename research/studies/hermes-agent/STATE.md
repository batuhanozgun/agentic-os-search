# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / PINNED UI-PROFILE APPROVAL CALLER TRACE + BOUNDED SLASH-POLICY EXECUTION  
**Son kayıt:** 2026-09-10  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN](RESEARCH-PLAN.md), v0.10.  
**Araştırma tamamlandı mı?** HAYIR. Normal CLI/gateway onay kaynak zinciri ilerledi; gerçek prompt/request görünürlüğü, bütün UI/profile/worker entegrasyonu ve genel HERMES sentezi açık.

## Yetkilendirilmiş amaç ve sınırlar

Kullanıcının araştırmaya devam ve operasyonel sınıra kadar çalışma yetkisi sürer. Son kesintiye ilişkin doğrulanmış backend hata nedeni yoktur; arka planda yapılmış iş varsayılmadı. Bu tur gerçek kaynak incelemesi, dar offline deney ve repository yayını yürütüldü. Her iç kaynak grubu için yeni izin gerekmez.

Amaç önce HERMES-native mekanizma modeli, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesidir. OpenClaw ayrı adaydır. Kurulum, bütün ürünü başlatma, provider/model çağrısı, gerçek credential kullanımı, upstream değişikliği, Codex görevi, Foundation aktivasyonu veya adoption bu kapsamda değildir. Yanıtlar arasında otomatik/background çalışma yapılmaz. Codex başka repository kullanır; research main değişimleri ona atfedilmez. Araç/uygulama ayarları değiştirilmez.

## Birikimli durum ve korunmuş kanıt

| Dilim | Kalıcı giriş ve statü |
|---|---|
| İlk keşif / U01 review | [01](notes/01-ORIENTATION.md), [02](notes/02-BACKGROUND-LEARNING.md); pin, snapshot/fork/köken/guard kaynakları |
| U01-C curator | [03](notes/03-SKILL-CURATION.md); bakım/report/cron/rollback, kendi kimliği korunur |
| U01B / U01B2 | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md); ayrı bounded skill/onay deneyleri |
| U01-DOC | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md); sekiz unpinned belge, K01–K09 tarihsel tasarım |
| U01-D / U01-M | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md); caller/store kaynakları ve eski transport kanıtı |
| U01-D2 / D3 | [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md); selected worker/C/V, sınırlı 22-range AST ve exact middleware MW kanıtları |
| U01-M2 | [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md); beş tam modül/N01–N12, `91af441...` v0.9 yayınıyla ZIP bağımlılığı kapanmıştı |
| **U01-M3, bu tur** | **[12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md)** → [araştırma](evidence/2026-09-10-ui-profile/RESEARCH.md), [UI kaynakları](evidence/2026-09-10-ui-profile/SOURCES.md), [A01–A08](evidence/2026-09-10-ui-profile/RESULT.json) |

01–11 notları ve eski evidence klasörleri bu tur değiştirilmedi. Eski tarih/ref/deney ayrıntıları [v0.9 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/91af4415c22e05b80484b935383ceeb04a3c5b7b/research/studies/hermes-agent/STATE.md) ve Git geçmişinde korunur. Önceki birikimli kaynak defteri byte-identical [SOURCE-LEDGER-THROUGH-V0.9](SOURCE-LEDGER-THROUGH-V0.9.md) olarak saklandı; güncel [SOURCE-LEDGER](SOURCE-LEDGER.md) eski ve yeni kaynaklara yönlendirir. Donmuş defterin eski next-work cümleleri current authority değildir.

## Yeni bulguların epistemik statüsü

**SOURCE OBSERVATION:** CLI live/fresh store seçimi ve gateway fresh-store kullanımı; normal external-message ingress auth/canonical slash gate/busy-idle/handler/shared apply zinciri; primary/secondary profile wrapper'ları, context-local home ve transport-authorization damgası; pending namespace/record alanları; approval mode callback'i ile payload apply'in ayrılığı; mode setter'da cached-agent eviction; gateway skill diff kesintisi.

**EXECUTED, bounded:** UTC `2026-09-10T05:42:55.258536+00:00`, Python 3.13.5/Linux. UI08 tam slash_access.py, 5666 byte ve blob `07204201e411f29f912bb9bba6beec0566acab9d`. A01–A08 policy resolver/karar beklentileri eşleşti. Config/platform/source holders sentetik. Bozuk source pre-import reddi ve açık always-allow test mutantını yakalayan ret oracle'ı ayrı kaydedildi. Gateway/UI/profile/store/provider çalıştırılmadı. UI09 upstream test kaynağı okundu, koşturulmadı.

**BOUNDED INFERENCE:** Komut-adı yetkisi işlem/kayıt sahipliğiyle eşdeğer değildir. Aynı active home'a yönlenen session'lar bu storage katmanında aynı pending/memory alanına gider. Önceki M2 live/disk ayrışmasının kullanıcıya etkisi gerçek caller'ın live/fresh store seçimine bağlıdır. Bu üretimde yetkisiz erişim/olay/öğrenme kalitesi hükmü değildir.

**OPEN:** Tam transport authorization/profile-route resolver ve opsiyonel hook yolları; actual caller hata enjeksiyonu; aynı profile'ın çok-session cache/konfigürasyon tutarlılığı; onay sonrası gerçek prepared request. Normal source trace, full UI runtime doğrulamasına yükseltilmedi. Tüm eski test kümeleri ayrı kalır; ürün PASS toplamı veya tamamlanma yüzdesi yoktur.

## İlk sonraki aktif yetkili iş — onaydan model görünümüne

**Q07/Q22:** CLI'nin mevcut ajanında ve gateway'in cached agent tekrar-kullanımında, onaylanan dosya değişikliği ne zaman store/frozen snapshot/system-prompt/request'e taşınır? `load_from_disk`, prompt invalidation, turn prologue ve gateway cache reuse callsite'larını birlikte takip et. `/memory approval on` ayar değişikliği ile `/memory approve <id>` payload uygulaması birbirinin yerine geçmez.

Önce pinned kaynak bağı kurulacak; zararsız offline prepared-request readback mümkünse gerçek/sentetik bağımlılıklar açıkça ayrılarak çalıştırılacak. Provider/model çağrısına veya bütün ürün kurulumuna geçilmez. Ne “apply success hemen modele görünür” ne de “cached prompt kesin eski kalır” baştan kabul edilir. Bounded durma noktası: hangi çağrının hangi görünümü yenilediği ve hangi dalın hâlâ açık olduğu kaynak/kanıtla açıklanabilir olmalı.

Ardından ledger/backup/restore/sync, sonraki skill/cache yükleme, U01-C nested operations/report/cron ve F01–F12 kalan aileleri. Q05/Q23/Q24'ün normal onay source yolu artık ilk kez bulunacak iş değildir; ileri auth/profile/hook/platform ve cleanup sınırları açık tutulur. Aynı A veya N fixture'larını çoğaltmak entegrasyon kanıtı değildir.

## Ertelenmiş ileri doğrulama ve yeniden açma

Q26/Q29 full review/AIAgent/executor/PluginManager/Relay zinciri ve tam E01/E02 local originals ile legacy verify_excerpts.py hâlâ OPEN/NOT RUN. E01 `799199c10f9930da77c01da2324373614b27cb78`; E02 `da8d7e2c68b2346e6ecc15567d755d96085ef767`. D3'ün manuel-range AST eşleşmesi bu koşuyu ikame etmez. Yeni tam kaynak/bağımlılık erişimi, ilgili değişiklik veya load-bearing tasarım/adoption kararı yeniden açma tetikleyicisidir.

Native alt-sistem sentezi, bütün ilişkiler, dört-alan projeksiyonu ve CORE tamamlanmadı. Scope/security tartışması HERMES'in geri kalanını yutmayacak.

## Yeni oturum girişi

Canonical agent bootstrap → research root/studies catalog → META/STATE/INDEX → METHOD ve plan v0.10 → **12 + UI SOURCES/RESEARCH + RESULT sınırları**. Onay sonrası görünürlükte 07/11 ve M2 exact sources'a dön. Worker sorusu yeniden açılırsa 09/10 + E/J defterleri okunur. Eski NOT PUBLISHED, 429, ilk dosya veya v0.9 next-work ifadeleri yalnız tarihsel kayıttır; yeniden ZIP taşıma gerekmez.

Mandatory control/authorization/state çelişkisinde etkilenen iş durur. Bu yayın yalnız HERMES study ve katalogdaki ilgili satır kapsamındadır; Foundation/context/Codex/control/başka study dosyaları değiştirilmez. Bitiş ölçütü METHOD'dur.
