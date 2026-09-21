# EXP-004 — STATE

**Güncelleme:** 2026-09-21, T10 yeni katılım ve kontrol kapsamı devamı.
**Arşiv:** REPAIRED / MAIN-PUBLISHED. Bilinen kaynak-kısaltma/yönlendirme eksikliği önceki kapsamda kapatıldı; platform-export veya bağımsız transkripsiyon doğrulaması iddiası yok.
**Arşiv yayını:** PR #31; merge `b949fe66454a1943ac9c99827e79f68f962658be`, kapanış `e372ed7558b0b0ebbf388c864b0733382d1418ba`. [Onarım yayın/kontrol kaydı](checks/PUBLICATION.md) o tarihsel kapsamı taşır; devam notlarının yayınının yerine geçmez.
**Güncel kavramsal çalışma:** [T10 — Yeni katılım, etki yolları ve denetim kapsamı](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md). T1–T10 konuşma içi kavramsal/sentetik denemelerdir; canlı sistem testi değildir.
**Korunmuş kaynak kesimi:** U001–U016 / S001–S015; 31 görünür mesaj, 16 kaynak dosyası. [Diyalog](sources/conversation/INDEX.md), [manifest](SOURCE-MANIFEST.json). T09/T10 türetilmiş notlardır; bu sayımı genişletmez.
**Önceki yayın:** PR #29 `46ab3ff5993683c6124d7786533529e0f6147914`; PR #30 `882e0dfd271bd8c284df59f81c882a66a88f9933`. Teknik yayın önceki tamlık iddiasını doğrulamıyordu.

## Amaç ve son kullanıcı yönü

Foundation/studies birikimiyle SOUL'un büyük, uzun, çok aktörlü ve baştan tamamen bilinmeyen iş için ihtiyaç duyacağı çalışma düzenini sorgulamak; örnekleri otomatik modül/mimari kararına çevirmemek.

U014 kaynak kayıt yetkisi, U015 T08 devamı, U016 öncelikle arşiv onarımı ve büyüme/branch açıklamasıydı. Onarım kapandı. Sonraki «Harika. Devam et kaldığın yerden.» yönüyle T09 yapıldı. Güncel «Test bizi çok titiz bir yapıya doğru götürüyor, bu çok iyi. Devam et lütfen.» mesajı T10 kavramsal devamını yetkilendirir. Olumlu değerlendirme kontrol sayısını artırmaya teknik kanıt değildir. Bu tur uygulama, yeni SOUL/Development OS kurulumu veya agent-control değişikliği yetkilendirilmedi.

## Korunmuş kaynak onarımı

İlk S001–S013 özetlenmiş/yeniden ifade edilmişti; S013'e U014 sonrası yorum eklenmişti. Bunlar [tarihsel görünüm dizininde](artifacts/condensed-before-repair/README.md) aynı Git alt-ağaç kimliğiyle korunur. Güncel kaynak yollarına görünür özgün yanıtlar kısaltılmadan yeniden aktarıldı. S014 önceki yanlış tamlık bildirimi, S015 tam T08 cevabı, U016 onarım kaynağıdır. Sonraki onarım cevabı ve devam turları eski kesimde değildir.

Kaynak payload ref'i `f1e93a9f052fb98b3f2e28e987233f3b51193534`; assistant tree `ba3111b97927ebb231947b2a500eee1d534a5a16`; kullanıcı blob'u `1866f243b3771a2d0152bc6b20f67c1a7f3f80c3`; arşiv başlıkları dahil 182.486 byte. Bunlar kimlik/transfer göstergeleridir; doğal dil doğruluğu veya bağımsız transkripsiyon oracle'ı değildir. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md), [onarım kontrolleri](checks/REPAIR-20260921.md). Bu tur kaynaklar/manifest/onarım kanıtı değişmedi.

## T1–T9'dan devir — hipotez, mimari değil

T1: ham talep ve yeterince belirlenmiş Mission ayrı. T2: ihtiyaç/koşul, Work, plan ve eylem ayrılır; iş keşfi sürer. T3: rol/aktör/capability/competence/authority ayrılır. T4: bilgi varlığı, uygun/erişilebilir bağlam ve kullanım farklıdır. T5: araç kataloğu/kullanılabilir yetenek/Run/gerçek etki ayrı. T6: tamamlanma, kanıt, kabul, entegrasyon ve amaç etkisi aynı değildir. T7: Actor/Run/Work sürekliliği ile kayıt/güncellik/gerçek ortam uzlaştırması ayrılır.

[T1–T7 konsolidasyonu](artifacts/CONSOLIDATION.md) ve ilgili reflection'lar tarihsel türetilmiş eserlerdir. Güncel devamı tek başlarına belirlemezler. Geniş başlıklarda temsil edebilmek uygulama yeterliliği veya bağımsız Foundation doğrulaması değildir.

[T08](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) / [S015](sources/conversation/assistant/S015.md): ders kaydı, geri bildirim kullanımı, kalıcı tepki değişimi, fayda, yetki ve transfer ayrı. Yöntem değişimi de kapsam/kanıt/yetki/aktif kullanım/geri dönüş koşullarıyla Work olabilir; deney yapılmadı.

[U016](sources/conversation/USER-MESSAGES.md#u016) yeni işlevlerle mevcut işlevlerin yeni aktör/kaynakları kapsamasını birlikte düşündüğünü açıklar. Dikey/yatay, iki dosya ve klasör örnektir; branch çağrışımı araç önerisi değildir. [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) kaynak/yorum sınırlarını korur.

[T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md): birbirinin kalmasını varsayan iki denetim aynı anda kaldırılabilir. Yerel PASS'lerin toplamı ortak uygunluk değildir. 60 dakika kapasiteye karşı 40+35 dakika iş tekil hazırlık ile ortak taahhüdü ayırır. Kabulün dayanak duruma bağlanması ve aktif geçişte boşluk bırakmama tasarım baskısıdır. Bu, merkezi her-şeyi-kilitleyen sistem veya canlı güvence sonucu değildir. T09 yayını `7de46ddbae29366cb4338b41f57d844a611a43d8`; tarihsel kaynak ve sınamalar kendi notunda korunur.

## T10 — Yeni sonuç ve sınır

Yeni görsel düzenleme aktörü/aracı doğrudan yayın yolu eklediğinde eski kontrol hiç bozulmadan kapsam dışında kalabilir. Bir parçanın görevini yapabilmesi, ortak düzene ilgili yükümlülükleriyle kabul edildiğini göstermez. Yükümlülük yeni çıktıya uygulanabilir; eski kontrol tekniği yeni biçime yeterli olmayabilir. Mevcut uygun güvence yeniden kullanılabilir; kör kontrol kopyası zorunlu değildir.

Doğrudan araç yetkisi, dolaylı başka aktör/servis üzerinden etki ve meşru delegasyon ayrılır. Aktörün varlığı veya bağlı araç, otomatik geniş yetki değildir. Yeni katılımın iş/rol/veri/çıktı/sürüm/etki yolu için uygun kabul kapsamı düşünülür. Taslak üretimi gibi gerçekten sınırlanmış işler canlı etki yetkisi açılmadan yürüyebilir.

Gerekli kapsama, fiilî uygulama ve gözlem/sınama kanıtı üç ayrı soru. Yalnız eski yolun izlerini saymak tüm etki yollarını ölçmez. Normal işlem kadar ilgili retry/bakım/yeniden başlatma yolları da dikkate alınır; bilinmeyen kapsam açık tutulur. Kontrol arızası sessiz bypass veya bütün sistemi durdurma ikilemi değildir; kritik etki sınırlandırılırken uygun güvenli işler sürebilir.

C10-1–8 karşı durumları tasarlanmış, uygulamada çalıştırılmamıştır. Foundation Control ve SDLC candidate study seçici geri çağrıldı; Anthropic'in birinci taraf dolaylı-aktör örneği, Saltzer–Schroeder'in erişim-koruma ilkeleri ve MCP token-passthrough sınırı dar birincil kaynak okumasıyla kullanıldı. Yeni servis/şema, protokol seçimi, gerçek güvenlik sertifikası veya bağımsız SOUL doğrulaması yok.

## Repository etkisi ve yayın sınırı

Başlangıç main: `7de46ddbae29366cb4338b41f57d844a611a43d8`. Dar değişiklik: T10 notu, STATE, paket INDEX ve iki explorations kütüphane girişi. T1–T9 eserleri, tam kaynak kesimi, manifest, onarım kayıtları, Foundation, studies, concepts, agent-control ve önceki EXP kaynakları korunur.

Bu dosya kendi gelecekteki commit'ini/yapılmamış uzak kontrolü ilan etmez. Yayın sonrası exact ref/diff ve kritik içerik readback ayrı yapılır; teknik yayın conceptual efficacy kanıtı değildir. Yeni not tam konuşma aktarımı sayılmaz.

## Sonraki sorumluluk

Arşiv onarımı kapalı, T10 bu kavramsal turda ele alındı. Bir sonraki doğal karşı-test: gerekli kontrolleri korurken araştırma/denetim yükü yüzünden işin bitirilememesi; kanıt yeterliliği, öncelik, zaman/bütçe, bekleme ve karar kapatma koşulları. Bu test burada yapılmadı. Daha sonra farklı büyük-domain karşı testi açık kalır. Mevcut kullanıcı yönü ve kanıt tekrar değerlendirilmeden uygulama/ürün seçimine geçilmez.
