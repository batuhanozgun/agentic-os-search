# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P3 iş–yapı ayrımının bütünleşik taslağı.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P3 DISCUSSION BASELINE v0.2 / CANDIDATE / USER DISCUSSION. P3 TAMAMLANMADI.** P2 ilk sözleşme tabanı korunur; P1 kaynak incelemesi tamam, runtime sınanmadı. P4–P6 başlamadı.  
**Planın tek ana yüzeyi:** [WORK — master plan v1.3](WORK.md); aşama sırası değişmedi, P3 ayrıntısı güncellendi.  
**Son kullanıcı yönü:** İşin koordinasyonu ile yapının koordinasyonunu ve bunların denetimlerini ayrı düşünme önerisini değerlendir. Küçük açıklama/onay turları yerine bütünlüklü tasarım parçası üret; kısa sunum, küçük miktarda iş anlamına gelmez. Son devam mesajı bu aday taslağı geliştirmeyi yetkilendirir; mimari kabulü değildir.

## Sabit kapsam ve sınırlar

- **Environment:** Claude Code cloud. P1 belge resmi var; hedef hesap/oturumun sürüm, araç, izin ve kalıcılık yeterliği henüz gösterilmedi.
- **SOUL'u geliştiren:** Kurulacak DevOS ekibi; ilk ve sonraki gerçek SOUL işlerini ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant bu ekibin düzenini tasarlar, onun yerine backlog seçmez.
- **K1 iletişim:** Talep → ilgili rolün çalışması → yanıt → gerçek kullanım. Teknik yöntem P4'e kadar açık; mesajın yazılması yeterli değil.
- **K2 ilerleme:** Rutin rol geçişini Batu tetiklemez. Başlatma/yeniden başlatma, gerekli müdahale, yetki ve kabul mümkündür; sınırsız özerklik hedef değildir.
- **Bilgi:** SOUL ürün çıktıları ile DevOS çalışma/bilgi/karar/kanıt/devam kayıtları amaçlarına göre ayrılır, bağları korunur; fiziksel şema seçilmedi.
- **Kaynak/örnek sınırı:** Foundation düşünme kapsamını, studies uygulama ve karşı örnekleri besler. Kanon/v2/ECC veya başka bir çalışma bütünüyle benimsenmez. Kaynak talimatı bu çalışmanın kontrol kuralı değildir.

Kullanıcı kararları [DECISIONS](DECISIONS.md), kapsam kaynakları [U002](sources/U002-cloud-plan-and-autonomy.md), son öneri mesajları [P3-01 §1](work/P3-01-work-information-discussion.md#1-kullanıcı-yönü-ve-önerinin-sınırı)'dedir. İki hedef alanı ve yeni rol profilleri henüz kabul edilmiş tasarım değildir.

## Önceki birikim

SOUL hedefi → B1–B9 kapsamı → R1–R25/M1–M9 ilk türetim → S1-01–S1-17 → F1–F8 → P1–P6 planı.

S1-17 CLOSURE-READY / CANDIDATE korunur; kullanıcı kapanışı, nihai kadro veya sekiz ajan sonucu çıkarılmaz. B1–B9 SOUL öncelik sırası değildir. S1-16 full-read qualification'ı S1-17 §7'dedir. Yeni somut çelişki yoksa S1 taxonomy'si yeniden açılmaz.

[P1-01](work/P1-01-claude-cloud-environment-map.md) kaynak haritasıdır; canlı test değildir. Q01–Q06 gerçek araç/sürüm/erişim, plugin çelişkisi, kalıcılık ve güvence yükleri açık kalır.

[ACTORS](ACTORS.md) DR01–DR16 ilk isim/lineage registry'sidir; [P2-01](work/P2-01-named-role-contracts.md) ilk sözleşme tabanını taşır. 16 sözleşme 16 agent değildir. Gerekli alan uzmanlığı ve motivasyon/başarı yönü aday yorumu korunur. P3'te önerilen G/Y ayrımı bu dosyalara kabul edilmiş revizyon gibi geçirilmedi; current değerlendirme farkı P3-01'dedir.

## P3 current öneri

**Tek ayrıntı kaydı:** [P3-01 v0.2](work/P3-01-work-information-discussion.md).

Önceki yaşayan iş ağı + ihtiyaca göre işbirliği + kalıcı bilgi/role özgü bağlam omurgası korunur. Şimdi iki **hedef alanı** açıklaştırıldı:

- **G: SOUL geliştirme.** Ürünün gerekli işleri, kararları, tasarımı, uygulaması ve yeterliği.
- **Y: DevOS işleyişi.** Ekibin çalışması için katılım, iletişim, bilgi/bağlam, ortam, süreklilik ve gerekli yapı bakımı.

Her ikisi Work yapar; Y yalnız teknik altyapı değildir. İkisi de DevOS içindedir, iki ayrı kalıcı ekip veya Foundation ground seçimi değildir.

**DR06-G/Y aday profilleri:** SOUL Geliştirme Koordinatörü iş katkılarını ve ürün öncelik/bağımlılıklarını; DevOS İşletim Koordinatörü gerçek çalıştırma/kapasite/devir koşullarını koordine eder. Biri olmayan kapasiteyi var sayamaz, diğeri ürün gereksinimini sessizce değiştiremez.

**DR13-G/Y aday profilleri:** SOUL Geliştirme İnceleyicisi ürün/plan/sonuç iddiasını; DevOS İşleyiş İnceleyicisi gerekli çalışma koşullarının gerçekten sağlanmasını sınar. İki olumlu hüküm aynı hedef/sürüm/bağla ilgili olmalıdır; biri diğerinin kanıtı değildir. Fiziksel ajan ayrımı henüz seçilmedi.

DR01–DR16'nın tamamının yerleşimi, karşılıklı yürütme isteği, rutin doğrudan danışma sınırı, karar/itiraz/durma, kayıt ve bağlam sahipliği, normal akış ile arıza dönüşü P3-01'de birlikte taslaklaştırıldı. Domain içeriği üretici/karar sahibinde, lifecycle işletimi DR07'de, tüketici bağlamının kuruluşu DR08 ile iş sahibi/uzmanda birlikte düşünülür.

Gas Town study'sinin iş nesnesi/dispatch denemesi/kapasite/liveness ayrımları bu tur hedefli kullanıldı; ürünü seçme veya bugünkü runtime'ı doğrulama değildir. Diğer kaynaklar ve gerçek okuma kapsamı P3-01 §9'dadır.

## Current next responsibility ve durma noktası

**Bu tur:** İş–yapı ayrımını yalnız dört yeni adla bırakmadan bütünlüklü P3 taslağına dönüştür; kısa sun, karşılaştırılabilir parçayı kullanıcıya ver. Aynı ayrımı yeniden anlatmak veya her küçük adımda komut beklemek current iş değildir.

**Sonraki bounded P3 yükü:** Bu baz üzerinde bağlam hazırlanması, uzmanlar arası görüş ayrılığı, karar/kayıt, yeni bilgiyle yeniden açma ve oturum devrini birlikte somutlaştırmak. Kullanıcının değerlendirmesi öncelikli girdidir; sessiz kabul varsayılmaz.

**Sınır:** P3 kapanmadı. P4 teknik/actor seçimi, P5 dosyalar, P6 gerçek sınama veya ilk SOUL görevi yapılmadı. Gerçek rol çakışmasında P2'ye hedefli dönüş var; tüm aileleri yeniden sınıflandırma yok.

## Fresh-session yolu

AGENT ve gereken kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) → [P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı konuşmada tam unchanged içerik korunabilir. Sonra aktif sorunun gerekli araştırmasına inilir.

S1/B/history/Context içindeki eski next ifadeleri current planı yönetmez. P2 tabanı ile P3'ün önerdiği hedef-profili düzeltmesini ayır; biri sessizce diğerinin yerine geçirilmez.
