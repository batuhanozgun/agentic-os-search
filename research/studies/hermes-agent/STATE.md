# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / PINNED CALLER-MEMORY ANALYSIS + RECOVERED SOURCE-SELECTED WORKER-POLICY EVIDENCE  
**Son kayıt tarihi:** 2026-09-09  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN.md](RESEARCH-PLAN.md), v0.7.  
**Araştırma tamamlandı mı?** HAYIR. Son U01-D2 dilimi yayımlandı; tam gerçek çağrı entegrasyonu, öğrenme kalitesi ve genel HERMES sentezi kapanmadı.

## Yetkilendirilmiş amaç ve sınırlar

Kullanıcı HERMES'i dipten yukarı araştırmayı, kanıtla planı değiştirmeyi ve kalıcı study kaydını yetkilendirdi; 2026-09-08'de devam edip operasyonel sınıra kadar çalışmayı yeniden onayladı. 2026-09-09'daki son talep, biten çalışma dilimini önce repo'ya kaydetmek ve repo'yu sonraki adıma hazır etmektir. Bu tur yayın/süreklilik işidir; yeni HERMES deneyi başlatılmadı. Mevcut araştırma yetkisi sürer; her iç kaynak grubu için yeni izin gerekmez.

Hedef önce HERMES-native model, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesidir. OpenClaw ayrı sonraki araştırma adayıdır. Kurulum, provider/model çağrısı, hesap/credential kullanımı, Codex görevi, Foundation aktivasyonu, upstream değişikliği veya benimseme bu yetkinin parçası değildir. Zararsız offline bileşen araştırması ile bütün ürünü çalıştırma ayrılır. Yanıtlar arasında otomatik/background araştırma yapılmaz.

Kullanıcı Codex'in başka repository kullandığını açıkladı. HERMES çalışma ve yayın durumu bu research repo'sundadır; geçmiş eşzamanlı main değişimleri Codex'e atfedilmez. Uygulama ayarları veya geçmiş araç sunumu farkının nedeni doğrulanmış değildir; bu yayın ayar/izin değişikliği yapmaz.

## Birikimli çalışma ve geçmişin korunması

1. İlk keşif pin/tree ve çalışma sınırlarını kurdu; [02 review](notes/02-BACKGROUND-LEARNING.md) conversation snapshot, fork, köken/guard ve pending kesitini kaydetti.
2. [03 curator](notes/03-SKILL-CURATION.md), beceri bakım politikası, otomatik/LLM yolları, rapor/cron ve rollback sınırlarını ekledi. U01-C kimliği korunur. Tarihsel H22 orta aralık eksikliği current eksik okuma değildir.
3. U01B, H22/S01 tam okuması ve iki exact modülle 10 sentetik durum üretti. Önce sohbet ZIP'i olarak kalan kanıt mevcut curator çalışması korunarak yayımlandı; v0.4 oldu. [04 notu](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [deney](evidence/2026-09-07-u01b/component-probe/README.md), [aktarım](evidence/2026-09-07-u01b/PUBLICATION.md).
4. İlk 2026-09-08 devamında pinned caller isteği iki 429 verdi; sekiz unpinned resmî belge [05 sözleşme notunu](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) ve K01–K09 planned kontrollerini üretti. V0.5 ve tarihsel durum [a218acfc STATE](https://github.com/batuhanozgun/agentic-os-search/blob/a218acfc20e7ece488709e00a9762166ec970fba/research/studies/hermes-agent/STATE.md) içindedir. O belge turu yeni kod/deney değildi.
5. Caller turunda pinned Git tree/blob okuması kaynakları getirdi. [06 caller/aktarım](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md) ve [07 bellek/replay](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md), [D defteri](evidence/2026-09-08-context-transfer/SOURCES.md) ve [üç-modüllü/yedi-durumlu transport kanıtı](evidence/2026-09-08-context-transfer/README.md) eklendi. Plan v0.6; yayın `29ab9b816843bab6f9e5f5b5815590fbac2b1713`.
6. Ayrı U01B2 ZIP dilimi önceki 06/07/transport kanıtı korunarak yayımlandı: [08 girişi](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [özgün kanıt](evidence/2026-09-08-u01b2/README.md), [yayın uzlaştırması](evidence/2026-09-08-u01b2/PUBLICATION.md). Manifest dahil 15 özgün dosya korundu; yeni deney yapılmadı, o yayın v0.6 sırasını değiştirmedi.
7. Son U01-D2 araştırma dilimi source-selected executor/gerçek whitelist tüketicisini birleştirip 14 ana, tam name-validator eklenmesiyle ayrı 5 tanılayıcı durum ve ayrı gerçek pre-import kimlik ret kontrolü üretti. İlk yayını araç çağrısı hatası nedeniyle ZIP'te kalmıştı. **2026-09-09'da bu teslim repo'ya alındı:** [09 girişi](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [tam araştırma](evidence/2026-09-08-worker-policy/RESEARCH.md), [yayın](evidence/2026-09-08-worker-policy/PUBLICATION.md). ZIP'in 25 manifest girdisi ve manifest dahil 26 özgün dosyası doğrulandı; GitHub'daki özgün subtree, yerelde dosyalardan hesaplanan Git tree kimliğiyle eşleşti. Eski koşular tekrarlanmadı. Plan v0.7 yalnız yeni kanıtı ve kalan devam sınırını uzlaştırır.

Önceki 01–08 notları ve eski evidence klasörleri bu yayında değişmez. [Yayın öncesi tam STATE](https://github.com/batuhanozgun/agentic-os-search/blob/36f1b7e6ae07da5c1d9d57ff9633d48473c42537/research/studies/hermes-agent/STATE.md) önceki ayrıntıları korur. Birikimli kaynak otoritesi [SOURCE-LEDGER](SOURCE-LEDGER.md); E/C/V, H/S/W/D/P ve U01B2 kimlikleri kendi defterleriyle yorumlanır.

## Kanıtın güncel statüsü

**Pinned kaynak analizi:** Ordinary loop'un ortak kontrolü, worker yerleşimi, ContextVar/callback ile thread-local whitelist'in farklı aktarımı, effect/persistence/delivery sırası; memory lock/reload/final-budget batch/frozen snapshot ve payload tabanlı pending apply kaynakta incelenmiştir. Bu, her caller'ın runtime doğrulaması değildir.

**Önceki ayrı deneyler:** U01B (iki exact modül/10 durum), transport (üç exact modül/sentetik policy ile 7 durum) ve U01B2 (iki exact arşiv modülü/12 senaryo) kendi tarihleri ve sınırlarıyla korunur. W01–W08, primary pin'e bağlanmamış belgelerdir.

**U01-D2 — kaydedilmiş yürütme:** C01–C14 UTC `2026-09-08T19:31:50.677314+00:00`; V01–V05 `2026-09-08T19:36:58.555297+00:00`; kimlik ret kontrolü `2026-09-08T19:36:24.270992+00:00`. Python 3.13.5/Linux. Pool/context/name-validator tam kaynakları kimlik doğrulandı; büyük executor/plugins yalnız elle aktarılmış seçili işlevler ve açık sınır taklitleriyle yürütüldü. [E defteri](evidence/2026-09-08-worker-policy/SOURCES.md) bu ayrımı taşır.

Seçili zincirde parent whitelist reddederken worker tüketicisi listeyi görmedi; deneysel worker binding ret davranışını geri getirdi. Bağımsız scope/guardrail/lifecycle kontrolleri engellemeyi sürdürdü. Tam name-validator'ın sentetik geniş ad kümesi kabulü dar review yetkisini otomatik uygulamadı; dar ad kümesi ve bozuk JSON erken durdurdu. `dispatched` callback kabul işaretiydi; gerçek etki handler sayısıyla ayrıldı. Tekrar callback girişi bir marker etkisinden sonra reddedildi.

**Hâlâ açık:** Elle aktarılmış tanımların tam orijinallerle AST eşitliği; tam review/AIAgent kurulumu, gerçek valid-name kümesi, tüm executor/plugins/middleware bağımlılıkları ve telafi edici kontrollerle erişilebilirlik. `verify_excerpts.py` tam orijinallere karşı NOT RUN. Memory M01/M02 de statik aday kalır. Bu dar kanıt üretimde genel yetki açığı, gerçekleşmiş olay/olay oranı, bütün ürün PASS'i veya öğrenme kalitesi değildir. Aktarım bütünlüğü davranış doğrulaması değildir.

## İlk sonraki yetkili iş — U01-D artık boşluğu

**İlk somut işlem:** 09 → E kaynak defteri üzerinden E01/E02 tam pinned dosyalarını blob kimlikleriyle yerelde elde et ve mevcut `verify_excerpts.py` ile seçili tanım sadakatini kontrol et. Beklenen blob'lar E01 `799199c10f9930da77c01da2324373614b27cb78`, E02 `da8d7e2c68b2346e6ecc15567d755d96085ef767`. AST eşitliği yalnız extraction kontrolüdür; tam entegrasyon kapanışı sayılmaz.

**Ardından ayırıcı soru:** Gerçek review/fork kurulumu → `valid_tool_names` üretimi → ordinary executor/middleware → worker policy tüketicisi sırasında aynı kısıt başka noktada kuruluyor veya uygulanıyor mu? Tam pinned modüller ve zararsız handler ile yürütülebilen parçaları, kalan taklitleri ve gerçek handler girişini ayrı kaydet. Bir ek kontrol bulunursa önceki çıkarımı daralt; baştan bypass sonucu varsayma.

Bağımlılık kapanışı kurulamıyorsa hangi halka/iddianın açık kaldığını kaydet; bütün ürünü kurmaya/provider çağırmaya sessizce geçme. Aynı selected-function fixture'ı tekrar çoğaltmak bu boşluğu kapatmaz. Mekanizma kaynak ve sınırlarıyla yeterince açıklanınca Q26'nın ileri entegrasyon doğrulamasını açık tutarak daha geniş araştırmaya ilerle; tek konu bütün aileleri yutmasın.

Sonraki sıra korunur: actual CLI/gateway pending caller'da onaylayan/profil/store → bellek dosyası/canlı nesne/snapshot/istek ve 07/M01–M02 → ledger/backup/restore/sync → sonraki skill/cache yükleme → U01-C curator nested batch/report/cron. 08/U01B2 default_name staging/replay ve rollback/diğer-yazar ayrımları bu yollara bağlanır. Kaynak bağımlılığı sıra değiştirirse kanıtı plana kaydet.

**Başa dönme:** `run_agent.py` erişimi ve H22 orta aralığı artık ilk-okuma engeli değildir. U01-D2 yerel deneyleri ve bu yayın tamamlanmıştır; ilk iş aynı 14/5 durumu yeniden üretmek değildir. Tam upstream HEAD güncellemesi veya kurulu release testi de bu yayın tarafından yapılmış sayılmaz.

## Hâlâ açık geniş kapsam

Tam alt envanter; alternatif transport/caller/worker; review cancellation ve shared-store eşzamanlılığı; actual pending UI; curator batch/report; skill ledger/backup/sync; model-visible reload/invalidation; gateway/cron/provider/backend/delegation/UI; install/update/CI/eval ve gelecek-task kalite. Native alt-sistem sentezleri, genel ilişkiler, dört-alan projeksiyonu ve CORE henüz yok. Dosya veya test sayısı tamamlanma yüzdesi değildir.

## Yeni oturum girişi ve güncel yayın anlamı

Canonical agent bootstrap → research root/studies catalog → META/STATE/INDEX → METHOD ve plan v0.7 → **09 + worker-policy PUBLICATION + RESEARCH/SOURCES**. Gerekli iddia için 06/07 ve D defterine dön; 08 ve eski kanıtları kendi sınırlarıyla oku.

Worker-policy ve U01B2 teslimlerindeki NOT PUBLISHED/NOT APPLIED/eski main/plan ifadeleri tarihsel kayıttır; güncel durum bu STATE ve ilgili PUBLICATION dosyalarıdır. Yeni oturum sohbet ZIP'ine bağımlı değildir. Kullanıcının elle dosya taşıması gerekmez.

Mandatory control erişimi veya çözülemeyen yetki/state çelişkisinde etkilenen iş durur. Diğer iş hatlarının yetkisi kendi STATE yüzeylerindedir. Bu yayın yalnız HERMES package ve katalog satırını etkiler; Foundation/context/Codex/control/başka study'leri değiştirmez. Bitiş ölçütü METHOD'dur.
