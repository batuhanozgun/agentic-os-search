# EXP-004 — STATE

**Güncelleme:** 2026-09-21, MS01 Checkpoint A.
**Güncel çalışma:** **MS01 — SOUL Çalışma Sistemi Taslağı v0.1 / ACTIVE, PARTIAL SYNTHESIS.** İlk bütünleşik mekanizma taslağı, soru-bankası yürüyüşü ve test→mekanizma/açıklar tablosu yazıldı. Tam MS01/EXP-004 kapanışı henüz yok.
**Güncel yetki:** Kullanıcı, RV01 sonrasında sorulan ilerleme planını «anlaştık. devam et.» diyerek başlattı. Yetki, aynı exploration içinde isimli mekanizmaları kurmak, aynı taslağı iki senaryoda kurgusal yürütmek ve EXP-004'te korumaktır; nihai mimari/adoption, gerçek ürün veya implementasyon değildir.
**İlk teslimat:** [MS01 ana taslak](artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md), [soru-bankası yürüyüşü](artifacts/MS01-QUESTION-BANK-WALKTHROUGH.md), [kapsama/açıklar/kaynaklar](artifacts/MS01-COVERAGE-AND-OPEN-MECHANISMS.md).
**Sonraki bağlı sorumluluk:** Aynı MS01 üzerinde romanın uçtan uca kurgusal yürüyüşü; gerekli mekanizma değişiklikleri; iki senaryonun birleşim/kapsama ve gereksiz-parça incelemesi. Yeni bağımsız DQ05 varsayılanı yoktur.

## 1. Amaç ve sınır

EXP-004, Foundation/studies birikimiyle SOUL'un büyük, uzun, birden fazla aktör ve baştan tam bilinmeyen işler için kuracağı çalışma düzenini düşünür. Kapanış çıktısı yalnız dikkat/kanıt maddeleri değil, adlandırılmış parçaları, ilişkileri ve kurgusal işleyişi olan bir SOUL taslağıdır.

Kullanıcının drift itirazı ve [RV01](reflections/RV01-DIRECTION-REVIEW-AND-MECHANISM-TARGET.md), yararlı derinleşmenin korunmasını ama mekanizma sentezinin ertelenmemesini belirledi. Hook örneği belirli ürün/API/kod zorunluluğu değildir. Yerel taslak adları Concepts'te ortak tanım veya kabul edilmiş mimari sayılmaz. Kullanıcının planı başlatması P1–P5 taslak tercihlerinin doğruluğunu kanıtlamaz.

Gerçek roman, yıllık soru-bankası, öğrenci/okur deneyi, model/provider çalıştırma, yeni tool kurulumu, baz SOUL davranış değişikliği veya Development OS implementasyonu yapılmadı. Yazma yalnız bu EXP-004 paketindedir. Foundation, studies, concepts, önceki EXP'ler ve agent-control değişmez.

## 2. MS01 Checkpoint A'da ne somutlaştı?

Baz SOUL için Host Runtime, Bootstrap Actor B0, Working State erişimi, başlangıç yöntem/araçları ve owner/operator yetki girdisi ayrıldı. İlk Mission formation işi, henüz oluşmamış Mission Contract'tan değil başlangıç yetkisinden başlar. Yeni alan rolleri bu başlangıç zemininden bağlanır; rol adı yeni uzmanlık yaratmaz.

Taslakta model yönlendirmesi ile host yaptırımı birlikte seçildi. Mission başına tek mantıksal commit otoritesi var; paralel aktörler candidate üretir. Bu tek model/işlem/makine zorunluluğu değildir. Kayıt, çalışan mekanizma ve gerçek kapasite ayrı tutuldu.

K1 Mission Interpreter/Discovery Driver; K2 Work Coordinator; K3 Context Builder; K4 Capability Binder/Method Selector; K5 Domain Workbench; K6 Run Controller/State Committer/Effect Broker; K7 Change & Recovery Manager isimli işlevler açıklandı. RV01'in Method Library'si kayıt yüzeyi, selector ise aktör/yöntem ortak uygulanabilirliği nedeniyle K4 içinde düşünülür. Yedi servis/agent seçilmedi.

Kontrol noktaları: `before_work_start`, `before_effect`, `before_result_admission`, `after_state_change`, `on_resume`. Bunlar kurgusal etiketlerdir. Hook anlamsal yeterliği yoktan çözmez; hostun gerçek kontrol yolu önceden/sonradan çalışmalıdır. Başlatma izni, sonuç kabulü ve haricî etki izni ayrı mekanizmalardır.

Soru-bankası yürüyüşü MC/Work/Run/Context/QC/Decision/Configuration kimlikleriyle talep, kaynak incelemesi, bağlama, iki küçük örnek üretme, inceleme/revizyon, kaynak değişimi, geç sonuç ve bilinmeyen etkiden dönüşü ilişkilendirdi. İki örneğin iç incelemeye kabulü ile yıllık program ve öğrenci sonucu özellikle ayrıdır. Bütün fixture kimlikleri kurgusaldır; gerçek source/actor oturumu veya yazılmış uygulama nesnesi değildir.

T1–T15 ve DQ01–DQ04 için karşılık tablosu var. G01 keşif, G02 context/anlamsal etki, G03 host/etki/recovery, G04 qualification, G05 ilerleme/kapasite, G06 yöntem birleşimi/transfer ve G07 roman bütünlüğü açıkları isimli taşıyıcılara bağlandı. Tasvir edilmiş mekanizma, kısmi açıklama ve yürüyüşü bekleyen kısım ayrı; hiçbiri runtime doğrulaması değildir.

## 3. Korunan tamamlanmış birikim

| Çalışma | Statü ve korunacak ayrım |
|---|---|
| T1–T15, SC02 | Tamamlanmış konuşma içi kavramsal/sentetik çalışmalar. Son T15; yeni MS01 yürüyüşü T16 değildir. |
| SY01 | T1–T15'in ortak sorumluluklar, alan yöntemleri ve kapasite/kanıt yükleri ara sentezi; yeniden yapılacak iş değil. |
| DQ01–DQ04 | Keşif/yeterlik, yöntem seçimi, üst iş anlayışı ve koşullu aktarım için tamamlanmış kavramsal girdiler; doğrulanmış SOUL yetkinliği değil. |
| RV01 | Yön değerlendirmesi ve mekanizma sentezine dönüş tamamlandı. Kaynak-bağlı aynı-assistant değerlendirmesi, bağımsız drift denetimi değil. |
| MS01 | Başlatılmış bütünleşik taslak. Checkpoint A yazıldı; roman yürüyüşü ve son birleşim açık. |

Bu girişte eski araştırma metinleri yeniden özetlenerek bağımsız kanıt üretilmez. Ayrıntı [INDEX](INDEX.md), ilgili asıl devamlar ve onların kaynak defterlerindedir. Önceki uzun STATE'in bütün metni [RV01 yayınındaki immutable STATE](https://github.com/batuhanozgun/agentic-os-search/blob/0dd58080eeea4ee8c7eaaaef0902d02fce825edc/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/STATE.md) üzerinden korunur; o ref'in MS01-pending yönü artık tarihsel checkpoint'tir.

## 4. Kaynak arşivi ve onarım — kapalı tarihsel iş

**Arşiv:** REPAIRED / MAIN-PUBLISHED. Korunan kesim U001–U016 / S001–S015; 31 görünür mesaj, 16 kaynak dosyası. Kümülatif kaynak adresi 126. [Diyalog INDEX](sources/conversation/INDEX.md), [manifest](SOURCE-MANIFEST.json), [aktarım sınırı](checks/TRANSCRIPTION-NOTE.md). MS01 ve sonraki notlar bu sayımı genişletmez; tam konuşma transkripti değildir.

İlk S001–S013 yoğunlaştırmaları [ayrı tarihsel dizinde](artifacts/condensed-before-repair/README.md) korunur; özgün görünen yanıtlardan tam aktarım daha sonra yapıldı. S014 yanlış tamlık bildirimi, S015 özgün T08 yanıtı, U016 onarım ve yatay/dikey genişleme açıklamasıdır. T08 devam notu ile S015 aynı belge değildir.

Onarım yayını PR #31; merge `b949fe66454a1943ac9c99827e79f68f962658be`, kapanış `e372ed7558b0b0ebbf388c864b0733382d1418ba`. [PUBLICATION](checks/PUBLICATION.md) bu onarımın kaydıdır; MS01 yayını değildir. Platform export'u/bağımsız transkripsiyon doğrulaması iddiası yoktur. Kaynak/manifest/onarım dosyaları bu tur değişmez.

## 5. Yayın ve kanıt sınırı

MS01 başlangıcı RV01 yayın commit'i `0dd58080eeea4ee8c7eaaaef0902d02fce825edc`'dir. Önceki ana yayınlar: SY01 `000786d1f7742ac87937017ac9cea18a5e329865`; DQ01 `06dcefc2f192cb0cd4eb216d3f3194c2bfa48269`; DQ02 `3a9359a8bdf75203358dcda5b2fcdb2fb3eac3ef`; DQ03 `97627337ad622b715f3a9c562d62bb11ecda5d31`; DQ04 `49029c8ed9027745850627a529290e079c1f09a4`.

Bu checkpoint'in yazma kapsamı üç MS01 dosyası ve current STATE/INDEX'tir. Eski ayrıntılı girişler Git'teki exact yayınlarından erişilebilir; önceki eserler/source dosyaları yeniden yazılmadı. Araştırma katkısı ve tam/seçici okuma sınırları MS01 kapsama dosyasındadır.

Yerel model/runtime/DB/hook veya eski test suite çalıştırılmadı. Dar özgün Beads claim kodu okundu; çalıştırılmadı. Yayın/diff/readback birer repository kontrolüdür; taslağın bilişsel veya operasyonel başarısı değildir. Bu STATE kendi gelecekteki commit'ini veya henüz yapılmamış readback'i ilan etmez.

## 6. Yeniden giriş ve sonraki çalışma

Yeni MS01 devralışı: **bu STATE → INDEX → RV01 → MS01 ana taslak → soru-bankası yürüyüşü → kapsama/açıklar**. Mevcut araştırma birikiminin ilk devralışında SY01 ve DQ01–DQ04 tam okunur; aynı konuşmada tam okunmuş değişmemiş sürümler yeniden okunmuş gibi raporlanmadan kullanılabilir. İlgili asıl T/kaynak ve studies primary rotasına kararın gerektirdiği derinlikte dönülür.

Sonraki MS01 işi G07'dir: aynı K1–K7 ve kayıtlar üzerinde romanın ilk yazılabilir işi, uzun kaynak okuması, motivasyon revizyonu, editoryal anlaşmazlık ve bütünsel teslimini kurgusal yürütmek. Sonuç gerekiyorsa aynı taslağın mekanizma sözleşmesini değiştirir; yeni bağımsız dikkat listesi veya DQ05 otomatik açılmaz.

Bu tur Checkpoint A kullanıcıya döndürülür. Roman ve son birleşim/kapsama incelemesi yapılmadan MS01 v0.1 ve EXP-004 kapatılmaz. Kapanış için canlı SOUL'u kurmak veya bütün alan yetkinliğini kanıtlamak şart koşulmaz; kalan açıkların isimli mekanizmaya, dayanağa ve sınanacak iddiaya bağlı olması gerekir.
