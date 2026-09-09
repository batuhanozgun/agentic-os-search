# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / REVIEW-ADMISSION AND MIDDLEWARE EVIDENCE + RECOVERED MEMORY/PENDING FIVE-MODULE EVIDENCE  
**Son kayıt tarihi:** 2026-09-09  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN.md](RESEARCH-PLAN.md), v0.9.  
**Araştırma tamamlandı mı?** HAYIR. U01-M2'nin ZIP'te kalan sonuçları yayımlandı; actual UI/profile/request, tam review/worker entegrasyonu, öğrenme kalitesi ve genel HERMES sentezi kapanmadı.

## Yetkilendirilmiş amaç ve sınırlar

Kullanıcı HERMES'i dipten yukarı araştırmayı, kanıtla planı değiştirmeyi ve kalıcı study kaydını yetkilendirdi. 2026-09-09'da araştırmaya devam etmemizi, sonuçların repo'ya yansıtılmasını ve sonraki adıma hazırlanmasını istedi. Son turdaki yayın eksikliğini tekrar sorması üzerine bu tur yalnız U01-M2 tesliminin yayın/süreklilik onarımı yapıldı; yeni HERMES deneyi başlatılmadı. Mevcut araştırma yetkisi sürer; her iç kaynak grubu için yeni izin gerekmez. Hedef önce HERMES-native model, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesidir.

OpenClaw ayrı sonraki araştırma adayıdır. Kurulum, provider/model çağrısı, hesap/credential kullanımı, Codex görevi, Foundation aktivasyonu, upstream değişikliği veya benimseme bu yetkinin parçası değildir. Zararsız offline bileşen araştırması ile bütün ürünü çalıştırma ayrılır. Yanıtlar arasında otomatik/background araştırma yapılmaz.

Codex başka repository kullanır; bu research main'indeki eşzamanlı değişimler ona atfedilmez. Araç/uygulama ayarları değiştirilmedi; geçmiş araç sunumu farkına teknik neden uydurulmaz. Bu yayın yalnız HERMES paketi ve katalogdaki ilgili satırı değiştirir.

## Birikimli çalışma ve geçmiş

1. İlk keşif ve [02 review](notes/02-BACKGROUND-LEARNING.md): conversation snapshot/fork, köken, guard ve pending kesitleri.
2. [03 curator](notes/03-SKILL-CURATION.md): bakım politikası, otomatik/LLM yolları, rapor/cron ve rollback. U01-C kimliği korunur.
3. U01B: tam skill mutator okuması, iki exact modül/10 sentetik durum ve sonradan canonical yayın. [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [kanıt](evidence/2026-09-07-u01b/component-probe/README.md).
4. U01-DOC: erişim hatasının yaşandığı turda sekiz unpinned belge ve K01–K09 tasarımları. [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md). Bu belge turu kod yürütmesi değildir.
5. Caller/memory turu: [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md), [D kaynak defteri](evidence/2026-09-08-context-transfer/SOURCES.md), üç exact modül/sentetik policy/7 durum. Yayın `29ab9b816843bab6f9e5f5b5815590fbac2b1713`.
6. U01B2: ayrı iki-modül/12-senaryo kaydı, [08 girişi](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md) ve [yayın uzlaştırması](evidence/2026-09-08-u01b2/PUBLICATION.md). Önceki çalışmalar ezilmedi; aktarım yeni deney değildi.
7. U01-D2: [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md) ve [worker-policy kanıtı](evidence/2026-09-08-worker-policy/README.md). Tam pool/context/name-validator ile manuel seçili executor/plugins; 14 C + ayrı 5 V durumu ve kimlik ret kontrolü. 2026-09-09'da `9a95b2cf1f8a0460ac6128e1409bf54aa3191022` üzerindeki v0.7 yayını bu dilimin sohbet ZIP bağımlılığını kapattı.
8. U01-D3: [10 giriş](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) → [araştırma](evidence/2026-09-09-review-middleware/RESEARCH.md), [J defteri](evidence/2026-09-09-review-middleware/SOURCES.md). Gerçek review constructor/valid-name/round/Relay kaynak bağı; 22 tanım için sınırlı manuel-range AST cross-check; exact middleware ile 8 durum. Tam büyük-orijinal verifier koşusu yapılmadı. Bu ayrı çalışma `c0ef2374a34cbb30f5f58a28333f89254931b00f` üzerinde plan v0.8 ile kayıtlıydı ve bu yayında korunur.
9. **U01-M2, bu yayında geri kazanılan ayrı dilim:** [11 giriş](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md) → [tam araştırma](evidence/2026-09-09-memory-pending/RESEARCH.md), [M2 defteri](evidence/2026-09-09-memory-pending/SOURCES.md), [N01–N12](evidence/2026-09-09-memory-pending/RESULT.json). Beş tam modüllü bellek/pending koşusu daha önce çalıştırılmış fakat ZIP'te kalmıştı. 18 özgün kanıt dosyasının yerel Git tree kimliği uzak readback ile eşleşti; ek üç teslim dosyası da içerikleri değişmeden evidence/delivery altında korundu. [Yayın uzlaştırması](evidence/2026-09-09-memory-pending/PUBLICATION.md), [aktarım kontrolü](evidence/2026-09-09-memory-pending/TRANSFER-CHECK.json). Bu yayın yeni deney değildir; v0.9 eski teslimi mevcut v0.8 ile birleştirir.

[Önceki eksiksiz v0.8 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/c0ef2374a34cbb30f5f58a28333f89254931b00f/research/studies/hermes-agent/STATE.md) ve [v0.7 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/9a95b2cf1f8a0460ac6128e1409bf54aa3191022/research/studies/hermes-agent/STATE.md) tarih/ref ve önceki ayrıntıları korur. Önceki 01–10 notları, bütün eski evidence klasörleri ve yöntem bu tur değişmez. Kimlikler kendi defterleriyle yorumlanır; test sayıları birleştirilerek ürün PASS sayısı yapılmaz.

## Kanıtın güncel statüsü

**D3 source-backed bağlantı:** Standart review constructor'ına parent toolset'leri aktarılır; _load_tools valid_tool_names'i şemalardan üretir. Daha dar review izni ayrı thread-local whitelist olarak kurulur. İncelenen kurulum/round yolu bu ikisini eşitlemez. Bu, constructor'ın dar ad kümesiyle otomatik telafi edeceği rakip açıklamayı sınırlar; bütün runtime'larda telafi yokluğu değildir. Dangerous-command auto-deny, scope, guardrail ve mutator kontrolleri ayrı kalır.

**D3 sınırlı kaynak cross-check:** UTC `2026-09-09T08:13:01.073141+00:00`. 15 executor + 7 plugin tanımı, yeniden manuel transkribe edilmiş canonical aralıklarla AST eşitliği verdi; negatif AST değişikliği yakalandı. Büyük E01/E02 tam yerel dosya hash'i doğrulanmadı; eski `verify_excerpts.py` NOT RUN. Ad-hoc ilk eşitlik SPEC'ten önceydi; ortak assistant/transkripsiyon riski ve keşifsel statü korunur.

**D3 yürütme:** UTC `2026-09-09T08:12:19.368928+00:00`, Python 3.13.5/Linux. Tam `hermes_cli/middleware.py`, blob `897e4afc07ba0d78ba928baf39a8573422b648be`, fake registry ve sentetik callback/handler ile MW01–MW08. Erken callback hatasında devam; kısa-devrede sıfır etki; downstream hatada asıl exception; başarılı ilk etki sonrası üst hata/ikinci-next'te ilk sonucun korunması gözlendi. Bozuk kaynak gerçek import guard'ıyla reddedildi. Gerçek worker/PluginManager/Relay/AIAgent çalıştırılmadı.

**M2 yürütme:** UTC `2026-09-09T08:10:46.824877+00:00`–`2026-09-09T08:10:46.849596+00:00`, Python 3.13.5/Linux. Beş complete Git-blob-verified modül: memory store/tool, write approval/shared commands ve provenance. N01–N12 ve gerçek pre-import kimlik ret kontrolü. Geçici dosyalar ve Linux fcntl dalı gerçek; home/config/registry/terminal callback, sentinel scanner ve utils.atomic_write_text yerine temp/replace yardımcısı sentetik. Bu D3 middleware koşusundan ayrı, daha önce yapılmış bir koşudur; yayın sırasında tekrarlanmadı.

**M01/Q27 artık bounded execution:** Pre-commit write failure disk eski/live yeni/snapshot eski bırakabildi; doğrudan tool yükseltti, ortak command başarısızlığı bildirdi ve pending'i korudu. Reload/retry toparlanması gözlendi; sessiz başarı veya her gerçek caller'da aynı kullanıcı etkisi iddia edilmez.

**M02/Q28 artık bounded execution:** Single new_text ve batch content sentinel taramasından geçerken batch new_text ön taramayı atlayabildi; explicit reload aynı sentetik tarayıcıyla snapshot'ı maskeledi, raw/live korundu. Gerçek threat scanner, zararlı içerik veya modele ulaşma doğrulanmadı.

**M2 diğer ayrımlar:** Normal disk/live yazımı frozen snapshot'ı değiştirmedi. Unreadable-file, final-budget/no-write batch ve supplied-store disabled-target kontrolleri çalıştı. N06 stale iki-store kullanımı sıralıdır; yarış güvencesi değildir. N08 proposal origin ile apply origin ayrıldı; gerçek onaylayan yetkisi ölçülmedi. N11 successful apply + pending unlink failure Approved 1 metniyle kaydı bırakabildi; tekrar add kayıt çoğaltmadı. N12 semantik geçersiz batch staging'den sonra apply'de reddedildi. Gerçek UI/profile/config-refresh/request ve tüm replay türleri açık.

**Statik kalan:** tool-round persist-before-execute ve post-effect persistence; Relay managed/unmanaged ve callback/postprocessing. Yeni DB/Relay koşusu yok. M2'nin ayrı review kaynak notu J gözlemlerinin bağımsız tekrarı değildir. Eski U01B/transport/U01B2/C/V/MW/N deneyleri bu yayında tekrarlanmadı. W01–W08 unpinned kalır; upstream current HEAD/kurulu release doğrulaması yoktur.

## Sıradaki aktif yetkili iş — gerçek pending onayı ve profil/store

**İlk somut soru:** CLI ve gateway'de `/memory` / `/skills` pending onayını hangi gerçek çağırıcı, hangi onaylayan kimlik, aktif home/profil ve canlı ya da yeni yüklenen store üzerinden uygular? `hermes_cli/cli_commands_mixin.py` ve `gateway/slash_commands.py` navigasyon adaylarından başlayarak ilgili callsite'ları primary pin'de doğrula; ortak `hermes_cli/write_approval_commands.py` (D17/H08/M2-S03), memory replay (D15/M2-S02) ve skill apply işlevlerine bağla. Dosya adı, docstring veya ortak command deneyi bütün UI zincirini kapatmaz.

M2/N08–N12 artık bu zincirin normal/hata/temizleme readback'i için girdidir; ilk iş aynı 12 fixture'ı tekrar üretmek değildir. Ardından dosya/canlı nesne/frozen snapshot/gerçek istek görünümünü compression/rebuild/reload ile bağla. M01/M02'nin bounded karşı-sınamaları yapıldı; bu sonuçların gerçek çağırıcıdaki etkisi hâlâ açıktır. 08/U01B2 default_name staging/replay, canlı preview/hedef sürümü ve rollback/diğer-yazar soruları ilgili yollara bağlanır. Sonra ledger/backup/restore/sync, sonraki skill/cache yükleme ve U01-C nested batch/report/cron gelir.

**Sıra gerekçesi:** V0.8, standart ad-kümesi/round/middleware kaynaklarıyla Q26'nın güçlü hükmünü açık tutarak geniş öğrenme zincirine geçmişti. V0.9 bu sırayı korur; M2'nin eski bağımsız çalışma diliminde önden yapılmış bellek deneylerini kayda ekler. Bu yeni faz yetkisi veya U01-D kapanışı değildir; mevcut kanıtın uzlaştırılmasıdır.

## Açık tutulan ileri doğrulama / yeniden açma koşulu

Q26 ve Q29'un tam-runtime düzeyi OPEN. E01 `799199c10f9930da77c01da2324373614b27cb78` ve E02 `da8d7e2c68b2346e6ecc15567d755d96085ef767` tam yerel orijinalleri elde edilirse eski `verify_excerpts.py` ile daha güçlü fidelity kontrolü yapılır. Ardından gerçek review/fork, actual valid names, executor/PluginManager/middleware/Relay bağımlılıkları ve zararsız handler birlikte sınanır. Kurulum/provider yetkisi sessizce genişletilmez.

Bu halka, yeni exact materyalizasyon/bağımlılık erişimi sağlandığında, yeni source değişimi olduğunda veya bulgu adoption/tasarım/güvenlik hükmü için yük taşıdığında yeniden açılmalıdır. Aynı eski selected fixture'ları tekrar etmek gerekli yeni kanıtı üretmez. Genel bypass, üretim olayı/oranı veya öğrenme kalitesi iddiası yetkili/kanıtlanmış değildir.

## Açık geniş kapsam ve yeni oturum

F01–F12 alt envanter ve bağımlılık kapanışı; alternatif caller/worker/transport; cancellation/shared-store; actual pending UI; curator raporları; ledger/sync; prompt reload; gateway/cron/provider/backend/delegation/UI; install/update/CI/eval ve gelecek-task kalite açık. Native alt-sistem sentezi, genel ilişkiler, dört-alan ve CORE henüz yok.

Canonical agent bootstrap → research root/studies catalog → META/STATE/INDEX → METHOD ve v0.9 plan → **11 + M2 PUBLICATION/SOURCES/RESEARCH/RESULT sınırları**. D3 bağlamı için 10/J, pending geçmişi için 07/D17/D15 ve 08'e dön. Q26 yeniden açılırsa 09/E/C/V ve D3'ün sınırlı fidelity kaydı birlikte okunur. Eski notlardaki ilk sonraki dosya ve erişim cümleleri current STATE yerine geçmez.

M2 ve eski teslimlerdeki NOT PUBLISHED/eski plan/main ifadeleri tarihsel metindir; ilgili PUBLICATION ile okunur. Yeni oturum son bellek kanıtına sohbet ZIP'i olmadan erişebilir; kullanıcı elle dosya taşımak zorunda değildir. Çözülemeyen mandatory control/authorization/state çelişkisinde etkilenen iş durur. Diğer çalışma hatlarının yetkisi kendi STATE dosyalarındadır. Bitiş ölçütü METHOD; dosya/test sayısı tamamlanma yüzdesi değildir.
