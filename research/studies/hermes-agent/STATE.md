# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / REVIEW-ADMISSION SOURCE TRACE + BOUNDED RANGE CROSS-CHECK + EXACT MIDDLEWARE EVIDENCE  
**Son kayıt tarihi:** 2026-09-09  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN.md](RESEARCH-PLAN.md), v0.8.  
**Araştırma tamamlandı mı?** HAYIR. U01-D3 ilerledi; tam review/worker entegrasyonu, öğrenme kalitesi ve genel HERMES sentezi kapanmadı.

## Yetkilendirilmiş amaç ve sınırlar

Kullanıcı HERMES'i dipten yukarı araştırmayı, kanıtla planı değiştirmeyi ve kalıcı study kaydını yetkilendirdi. 2026-09-09'da son worker-policy paketinin yayını tamamlandıktan sonra araştırmaya devam etmemizi istedi. Bu tur U01-D3 kaynak/deney çalışmasıdır; her iç kaynak grubu için yeni izin gerekmez. Hedef önce HERMES-native model, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesidir.

OpenClaw ayrı sonraki araştırma adayıdır. Kurulum, provider/model çağrısı, hesap/credential kullanımı, Codex görevi, Foundation aktivasyonu, upstream değişikliği veya benimseme bu yetkinin parçası değildir. Zararsız offline bileşen araştırması ile bütün ürünü çalıştırma ayrılır. Yanıtlar arasında otomatik/background araştırma yapılmaz.

Codex başka repository kullanır; bu research main'indeki eşzamanlı değişimler ona atfedilmez. Araç/uygulama ayarları değiştirilmedi; geçmiş araç sunumu farkına teknik neden uydurulmaz. Bu tur yalnız HERMES paketi ve katalogdaki ilgili satır değişir.

## Birikimli çalışma ve geçmiş

1. İlk keşif ve [02 review](notes/02-BACKGROUND-LEARNING.md): conversation snapshot/fork, köken, guard ve pending kesitleri.
2. [03 curator](notes/03-SKILL-CURATION.md): bakım politikası, otomatik/LLM yolları, rapor/cron ve rollback. U01-C kimliği korunur.
3. U01B: tam skill mutator okuması, iki exact modül/10 sentetik durum ve sonradan canonical yayın. [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [kanıt](evidence/2026-09-07-u01b/component-probe/README.md).
4. U01-DOC: erişim hatasının yaşandığı turda sekiz unpinned belge ve K01–K09 tasarımları. [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md). Bu belge turu kod yürütmesi değildir.
5. Caller/memory turu: [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md), [D kaynak defteri](evidence/2026-09-08-context-transfer/SOURCES.md), üç exact modül/sentetik policy/7 durum. Yayın `29ab9b816843bab6f9e5f5b5815590fbac2b1713`.
6. U01B2: ayrı iki-modül/12-senaryo kaydı, [08 girişi](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md) ve [yayın uzlaştırması](evidence/2026-09-08-u01b2/PUBLICATION.md). Önceki çalışmalar ezilmedi; aktarım yeni deney değildi.
7. U01-D2: [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md) ve [worker-policy kanıtı](evidence/2026-09-08-worker-policy/README.md). Tam pool/context/name-validator ile manuel seçili executor/plugins; 14 C + ayrı 5 V durumu ve kimlik ret kontrolü. 2026-09-09'da `9a95b2cf1f8a0460ac6128e1409bf54aa3191022` üzerindeki v0.7 yayını sohbet ZIP bağımlılığını kapattı.
8. **U01-D3, bu tur:** [10 giriş](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) → [tam araştırma](evidence/2026-09-09-review-middleware/RESEARCH.md) ve [J defteri](evidence/2026-09-09-review-middleware/SOURCES.md). Gerçek review constructor/valid-name/round/Relay kaynak bağı; 22 tanım için sınırlı manuel-range AST cross-check; exact tam middleware modülüyle 8 yeni tanılayıcı durum. Tam büyük kaynak dosyalarıyla eski verifier koşusu yapılamadı; daha dar kontrol onun yerine geçirilmedi.

[Önceki eksiksiz STATE](https://github.com/batuhanozgun/agentic-os-search/blob/9a95b2cf1f8a0460ac6128e1409bf54aa3191022/research/studies/hermes-agent/STATE.md) tarih/ref ve geçmiş aktarım ayrıntılarını korur. Önceki 01–09 notları, bütün eski evidence klasörleri ve yöntem bu tur değişmez. Kimlikler kendi defterleriyle yorumlanır; test sayıları birleştirilerek ürün PASS sayısı yapılmaz.

## Kanıtın güncel statüsü

**Yeni source-backed bağlantı:** Standart review constructor'ına parent toolset'leri aktarılır; _load_tools valid_tool_names'i şemalardan üretir. Daha dar review izni ayrı thread-local whitelist olarak kurulur. İncelenen kurulum/round yolu bu ikisini eşitlemez. Bu, constructor'ın dar ad kümesiyle otomatik telafi edeceği rakip açıklamayı sınırlar; bütün runtime'larda telafi yokluğu değildir. Dangerous-command auto-deny, scope, guardrail ve mutator kontrolleri ayrı kalır.

**Sınırlı kaynak cross-check:** UTC `2026-09-09T08:13:01.073141+00:00`. 15 executor + 7 plugin tanımı, yeniden manuel transkribe edilmiş canonical aralıklarla AST eşitliği verdi; negatif AST değişikliği yakalandı. Büyük E01/E02 tam yerel dosya hash'i doğrulanmadı; eski `verify_excerpts.py` NOT RUN. Ad-hoc ilk eşitlik SPEC'ten önceydi; ortak assistant/transkripsiyon riski ve keşifsel statü korunur.

**Yeni yürütme:** UTC `2026-09-09T08:12:19.368928+00:00`, Python 3.13.5/Linux. Tam `hermes_cli/middleware.py`, blob `897e4afc07ba0d78ba928baf39a8573422b648be`, fake registry ve sentetik callback/handler ile MW01–MW08. Erken callback hatasında devam; kısa-devrede sıfır etki; downstream hatada asıl exception; başarılı ilk etki sonrası üst hata/ikinci-next'te ilk sonucun korunması gözlendi. Bozuk kaynak gerçek import guard'ıyla reddedildi. Gerçek worker/PluginManager/Relay/AIAgent çalıştırılmadı.

**Statik kalan:** tool-round persist-before-execute ve post-effect persistence ayrımı; Relay managed/unmanaged ve callback/postprocessing farkı. Yeni DB/Relay koşusu yoktur. Memory M01/M02 statik aday kalır. Önceki U01B/transport/U01B2/C/V deneyleri tekrarlanmadı. W01–W08 unpinned kalır; upstream current HEAD/kurulu release doğrulaması yoktur.

## Sıradaki aktif yetkili iş — gerçek pending onayı ve profil/store

**İlk somut soru:** CLI ve gateway'de `/memory` / `/skills` pending onayını hangi gerçek çağırıcı, hangi onaylayan kimlik, aktif home/profil ve canlı ya da yeni yüklenen store üzerinden uygular? Ortak `hermes_cli/write_approval_commands.py` (D17/H08), `tools/memory_tool.py` (D15) ve skill apply işlevlerinin gerçek UI çağrı noktalarını pinned kaynakta takip et. Dosya adına veya docstring'e bakarak bütün UI zincirini kapanmış sayma.

Ardından bellek dosyası/canlı nesne/frozen snapshot/gerçek istek görünümünü ve 07/M01–M02'yi zararsız sentinel'larla ayır. 08/U01B2 default_name staging/replay, canlı preview/hedef-sürümü ve rollback/diğer-yazar sorularını ilgili yollara bağla. Sonra ledger/backup/restore/sync, sonraki skill/cache yükleme ve U01-C nested batch/report/cron gelir.

**Bu sıra değişikliğinin gerekçesi:** U01-D3, standart ad-kümesi oluşumu ve aradaki çağrı/hata halkalarını kaynakla ilerletti. V0.7/METHOD, tek whitelist adayının bütün araştırmayı yutmasını yasaklamıyordu ama açıkça buna karşı sınırlı ilerleme öneriyordu. Bu tur o seçenek uygulanır: açıklanmış kısmi mekanizma korunur, güçlü Q26 iddiası açıkken geniş öğrenme zincirinin sonraki halkasına geçilir. U01-D tamamlandı veya güvenlik açığı kesinleşti denmez.

## Açık tutulan ileri doğrulama / yeniden açma koşulu

Q26 ve Q29'un tam-runtime düzeyi OPEN. E01 `799199c10f9930da77c01da2324373614b27cb78` ve E02 `da8d7e2c68b2346e6ecc15567d755d96085ef767` tam yerel orijinalleri elde edilirse eski `verify_excerpts.py` ile daha güçlü fidelity kontrolü yapılır. Ardından gerçek review/fork, actual valid names, executor/PluginManager/middleware/Relay bağımlılıkları ve zararsız handler birlikte sınanır. Kurulum/provider yetkisi sessizce genişletilmez.

Bu halka, yeni exact materyalizasyon/bağımlılık erişimi sağlandığında, yeni source değişimi olduğunda veya bulgu adoption/tasarım/güvenlik hükmü için yük taşıdığında yeniden açılmalıdır. Aynı eski selected fixture'ları tekrar etmek gerekli yeni kanıtı üretmez. Genel bypass, üretim olayı/oranı veya öğrenme kalitesi iddiası yetkili/kanıtlanmış değildir.

## Açık geniş kapsam ve yeni oturum

F01–F12 alt envanter ve bağımlılık kapanışı; alternatif caller/worker/transport; cancellation/shared-store; actual pending UI; curator raporları; ledger/sync; prompt reload; gateway/cron/provider/backend/delegation/UI; install/update/CI/eval ve gelecek-task kalite açık. Native alt-sistem sentezi, genel ilişkiler, dört-alan ve CORE henüz yok.

Canonical agent bootstrap → research root/studies catalog → META/STATE/INDEX → METHOD ve v0.8 plan → **10 + J SOURCES/RESEARCH + yeni sonuçların sınırları**. Pending çalışması için 07/D17/D15 ve 08'e dön. Q26 yeniden açılırsa 09/E/C/V ve bu turun sınırlı fidelity kaydı birlikte okunur. Eski notlardaki ilk sonraki dosya, NOT PUBLISHED ve eski erişim cümleleri current STATE yerine geçmez; hiçbir eski dosya ilk kez okunacakmış gibi başa alınmaz.

Çözülemeyen mandatory control/authorization/state çelişkisinde etkilenen iş durur. Diğer çalışma hatlarının yetkisi kendi STATE dosyalarındadır. Bitiş ölçütü METHOD; dosya/test sayısı tamamlanma yüzdesi değildir.
