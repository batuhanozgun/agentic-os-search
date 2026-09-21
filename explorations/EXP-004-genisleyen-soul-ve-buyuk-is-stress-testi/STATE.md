# EXP-004 — STATE

**Güncelleme:** 2026-09-21, MS01 Checkpoint B.
**Güncel durum:** **MS01 — SOUL Çalışma Sistemi Taslağı v0.1 / PROVISIONAL DRAFT, REVIEW READY.** İsimli mekanizmalar, soru-bankası ve roman yürüyüşleri, eski testlerin karşılıkları ve sınırlı birleşim/sadeleştirme incelemesi hazırdır. EXP-004'ün taslakla kapanışı kullanıcı değerlendirmesini bekler; mimari veya gerçekleştirilmiş SOUL yeterliği kabul edilmedi.
**Güncel yetki:** Kullanıcının A teslimatından sonra verdiği «peki izliyorum ve okuyorum seni. devam et.» yönü, roman yürüyüşü ve aynı MS01 üzerinde gerekli değişiklik/birleşim incelemesini yetkilendirir. Yeni ürün, gerçek roman/öğrenci/okur deneyi, model/provider koşusu veya implementasyon değildir.
**Paket:** [MS01 ana taslak](artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md), [banka yürüyüşü — A](artifacts/MS01-QUESTION-BANK-WALKTHROUGH.md), [roman yürüyüşü — B](artifacts/MS01-NOVEL-WALKTHROUGH.md), [kapsama/birleşim/açıklar/kaynaklar](artifacts/MS01-COVERAGE-AND-OPEN-MECHANISMS.md).
**Sonraki sorumluluk:** Bu taslağın kullanıcı değerlendirmesi; varsa adı konmuş mekanizma düzeltmesi. Otomatik yeni DQ05, yeni test kampanyası veya implementasyon yoktur.

## 1. Amaç ve sınır

EXP-004, Foundation/studies birikimiyle SOUL'un büyük, uzun, çok aktörlü ve baştan tam bilinmeyen bir işi nasıl üstleneceğini düşünür. Kullanıcının drift itirazı ve [RV01](reflections/RV01-DIRECTION-REVIEW-AND-MECHANISM-TARGET.md) sonucunda kapanış çıktısı yalnız dikkat maddeleri değil, adlandırılmış parçaları ve işleyişi bulunan bir SOUL taslağı olarak belirginleştirildi.

B'de bu çıktı bir değerlendirme adayına ulaştı. Bu assistant'ın sınırlı self-review hükmüdür; kullanıcı onayı, bağımsız doğrulama veya nihai mimari kabulü değildir. Taslak adları Concepts ortak tanımı veya Foundation ground'larının servis listesi değildir. Gerçek SOUL/Development OS, roman, yıllık soru-bankası veya canlı model/okur/öğrenci deneyi yapılmadı. Yazma yalnız EXP-004'tedir; Foundation, studies, concepts, diğer EXP'ler ve agent-control korunur.

## 2. MS01 A'dan B'ye somut durum

A'da Host Runtime, Bootstrap Actor B0, Working State, başlangıç yöntem/araç ve owner/operator yetkisi kuruldu. K1 Mission Interpreter/Discovery Driver; K2 Work Coordinator; K3 Context Builder; K4 Capability Binder/Method Selector; K5 Domain Workbench; K6 Run Controller/State Committer/Effect Broker; K7 Change & Recovery Manager aynı işlev kimlikleriyle korunur.

P1 model yönlendirmesi/host yaptırımı; P2 mission başına tek mantıksal commit yolu/paralel candidate üretimi; P3 aktör–yöntem–bilgi–ortam ortak uygulanabilirliği; P4 start/result/effect sınırları; P5 library ile etkin configuration ayrımı korunur. Yedi zorunlu agent/process seçilmedi.

B'de P6 Work kipi/etkisine bağlı admission; P7 exact sıralı Assembly Snapshot ve Design/working assembly/Delivery Baseline ayrımı; P8 kaynak-bağlı süren Reading Pass ve farklı bilgi kipleri; P9 tekil yöntem yerine birlikte çalışan konfigürasyon incelemesi eklendi. Narrative Ledger, Scene Brief ve Revision Package ek servisler değil mevcut kayıt/Work sözleşmelerinin alan görünümleridir.

Roman yürüyüşü ilk keşif sahnesini, yazımdan doğan aday fikri, A/B motivasyon revizyonunu, bilgi aktarım boşluğunu, kaynak boyunca/ilişkili okuma düzenini, editoryal seçimi ve kesintiden dönüşü aynı K1–K7 içinde bağladı. Tam roman olmadığı için bütünsel kabul ve teslim son dalları koşullu tarif edildi; yapılmış veya olumlu sonuçlanmış sayılmadı.

Banka yürüyüşü Checkpoint A olarak değişmeden kaldı; iç örnek dilim ile yıllık hedef ve öğrenci sonucu ayrımı sürer. O dosyanın «roman sonraki iş» cümleleri tarihsel A yönüdür. Güncel kuyruk bu STATE ve MS01 B tarafından belirlenir.

İki senaryonun sınırlı birleşim/sadeleştirme incelemesi ve T1–T15/DQ01–DQ04 karşılıkları kapsam dosyasında güncellendi. G01 keşif, G02 context/anlamsal etki, G03 gerçek host/etki/recovery, G04 qualification, G05 ilerleme/kapasite, G06 yöntem birleşimi/transfer, G07 gerçek uzun-eser üretme/değerlendirme yeterliği açık kalır. G07'nin kurgusal yürüyüş alt-işi tamamlanması gerçek kapasite açığını kapatmaz.

## 3. Korunan birikim ve kaynak statüsü

T1–T15/SC02, SY01, DQ01–DQ04 ve RV01 tamamlanmış önceki kavramsal girdilerdir; yeniden yapılacak iş değildir. MS01 bunları kaynak transkripti veya gerçek deney sonucu yapmaz. T sayısı T1–T15 olarak kalır.

Korunmuş kaynak arşivi U001–U016 / S001–S015, 31 görünür mesaj ve 16 dosyadır; kümülatif kaynak adresi 126. [Diyalog INDEX](sources/conversation/INDEX.md), [manifest](SOURCE-MANIFEST.json), [aktarım sınırı](checks/TRANSCRIPTION-NOTE.md). İlk yoğunlaştırmalar ayrı tarihsel dizinde; sonra görünen özgün yanıtlardan tam aktarım yapılmıştır. T08 türev notu S015 özgün yanıtıyla aynı belge değildir. Platform export'u veya bağımsız transkripsiyon doğrulaması iddiası yoktur.

Arşiv onarımı kapalıdır: PR #31, merge `b949fe66454a1943ac9c99827e79f68f962658be`, kapanış `e372ed7558b0b0ebbf388c864b0733382d1418ba`. [PUBLICATION](checks/PUBLICATION.md) bu onarımın tarihsel kaydı, MS01 yayını değil. MS01 kaynak sayısını artırmaz; kaynak/manifest/onarım dosyaları değişmez.

## 4. Yayın ve kanıt sınırı

MS01 A yayını `a0f3ab5f450b28d908a5a89d15a626637e322bfe`, B'nin başlangıcıdır. RV01 yayını `0dd58080eeea4ee8c7eaaaef0902d02fce825edc`. Önceki ana yayınlar: SY01 `000786d1f7742ac87937017ac9cea18a5e329865`; DQ01 `06dcefc2f192cb0cd4eb216d3f3194c2bfa48269`; DQ02 `3a9359a8bdf75203358dcda5b2fcdb2fb3eac3ef`; DQ03 `97627337ad622b715f3a9c562d62bb11ecda5d31`; DQ04 `49029c8ed9027745850627a529290e079c1f09a4`.

B yazma kapsamı yeni roman yürüyüşü, mevcut ana taslak/kapsam dosyası ve bu STATE/INDEX'tir. [A STATE](https://github.com/batuhanozgun/agentic-os-search/blob/a0f3ab5f450b28d908a5a89d15a626637e322bfe/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/STATE.md) ve önceki uzun girişler kendi immutable ref'lerinden korunur. Önceki kaynak ve araştırmalar yeniden yazılmadı.

B'de T12–T15 tam; Context/Memory/Harness META/STATE tam ve synthesis seçici; Re3/DOC primary HTML method bölümleri dar okundu. Gerçek okuma ve kaynak katkıları MS01 kapsam dosyasındadır. Hiçbir model/runtime/DB/hook/test suite çalıştırılmadı. Bu STATE gelecekteki commit/readback başarısını önceden ilan etmez; publication kontrolleri teknik güvence, içerik doğruluğu veya yeterlik kanıtı değildir.

## 5. Yeniden giriş ve dönüş noktası

Yeni devralış: **STATE → INDEX → RV01 → MS01 ana taslak → banka A → roman B → kapsama/birleşim/açıklar**. Mevcut araştırma birikiminin ilk devralışında SY01 ve DQ01–DQ04'ün tam okuma rotası korunur. Aynı konuşmada tam okunmuş değişmemiş kaynaklar yeniden okunmuş gibi raporlanmadan kullanılabilir. Karar-kritik noktada asıl T/kaynak ve research primary yüzeyine dönülür.

Bu checkpoint'te yetkili taslak teslimatı kullanıcıya döndürülür. EXP-004'ün taslakla kapanışı için kullanıcı değerlendirmesi beklenir. Kalan canlı/bilişsel deney yükleri gizlenmez ama sırf onlar açık diye sonsuz soyut araştırmaya dönülmez. Sonraki yetkili iş kullanıcının değerlendirmesi veya yeni yönüyle belirlenir; taslak metni kendiliğinden uygulama talimatı değildir.
