# EXP-004 — STATE

**Güncelleme:** 2026-09-21, T09 eşzamanlı değişiklik ve ortak koşul devamı.
**Arşiv:** REPAIRED / MAIN-PUBLISHED. Bilinen kaynak-kısaltma ve yönlendirme eksikliği önceki kapsamda kapatıldı. Platform-export veya bağımsız transkripsiyon doğrulaması iddiası yoktur.
**Arşiv yayını:** PR #31; merge `b949fe66454a1943ac9c99827e79f68f962658be`, kapanış `e372ed7558b0b0ebbf388c864b0733382d1418ba`. [Onarım yayın/kontrol kaydı](checks/PUBLICATION.md) bu tarihsel kapsamı taşır; T09 yayınının yerine geçmez.
**Güncel kavramsal çalışma:** [T09 — Eşzamanlı değişiklikler ve ortak koşullar](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md). T1–T9 konuşma içi sentetik/kavramsal denemelerdir; canlı sistem testi değildir.
**Kaynak arşivi kesimi:** U001–U016 / S001–S015; 31 görünür mesaj, 16 kaynak dosyası. [Diyalog](sources/conversation/INDEX.md), [manifest](SOURCE-MANIFEST.json). T09 türetilmiş nottur; bu eski kaynak sayımını genişletmez.
**Önceki yayın:** PR #29 `46ab3ff5993683c6124d7786533529e0f6147914`; PR #30 `882e0dfd271bd8c284df59f81c882a66a88f9933`. Bu teknik yayınlar önceki tamlık iddiasını doğrulamıyordu.

## Amaç ve son kullanıcı yönü

Foundation ve studies birikimini kullanarak SOUL'un büyük, uzun, çok aktörlü ve baştan tamamen bilinmeyen iş için ihtiyaç duyacağı çalışma düzenini sorgulamak; örnekleri otomatik modül/mimari kararına çevirmemek.

U014 önceki kesimi kaydetme yetkisiydi. U015 aynı kavramsal çalışmayı sürdürdü ve T08 oluştu. [U016](sources/conversation/USER-MESSAGES.md#u016) eksik varsa önce repository'yi düzeltmeyi istedi; onarım kapatıldı. Onarım cevabından sonraki «Harika. Devam et kaldığın yerden.» mesajı bu kavramsal devamı yetkilendirir. T09 aynı büyük-iş denemesidir; SOUL/Development OS kurulumu, kaynak studies araştırmasının yeniden başlatılması veya kontrol dosyası değişikliği değildir.

## Kaynak onarımının korunmuş durumu

Önceki S001–S013 dosyaları özetlenmiş/yeniden ifade edilmişti; S013'e U014 sonrası yorum da eklenmişti. Bunlar [ayrı tarihsel görünüm dizininde](artifacts/condensed-before-repair/README.md) aynı Git alt-ağaç kimliğiyle korunur. Güncel kaynak yollarındaki S001–S013, görünür özgün yanıtlardan yeniden ve kısaltılmadan aktarıldı. S014 önceki hatalı tamlık cevabı; S015 tam T08 cevabı; U016 onarımın kaynağıdır. Sonraki arşiv-onarım cevabı ve devam turları bu eski kesimde değildir.

Kaynak payload ref'i `f1e93a9f052fb98b3f2e28e987233f3b51193534`; assistant tree `ba3111b97927ebb231947b2a500eee1d534a5a16`; kullanıcı blob'u `1866f243b3771a2d0152bc6b20f67c1a7f3f80c3`. Kaynak dosyaları arşiv başlıkları dahil 182.486 byte. Kimlik/byte kontrolü kaynak doğruluğu veya bağımsız transkripsiyon doğrulaması değildir. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md) ve [onarım kontrolleri](checks/REPAIR-20260921.md) ayrıdır. Bu tur kaynaklar/manifest yeniden yazılmadı.

## Devralınan model — hipotez, mimari değil

T1: ham talep ve yeterince belirlenmiş Mission farklı. T2: ihtiyaç/koşul, Work, plan ve eylem ayrılır; keşif sürer. T3: rol, aktör, capability, competence ve authority ayrılır. T4: sistemdeki bilgi, uygun/erişilebilir bağlam ve fiilî kullanım farklıdır. T5: araç kataloğu, kullanılabilir yetenek, Run ve gerçek etki ayrı. T6: tamamlanma, kanıt desteği, kabul, entegrasyon ve amaç etkisi aynı değildir. T7: aktör, Run ve Work sürekliliği; kalıcılık, güncellik ve gerçek durumla uzlaştırma ayrılır.

[İlk konsolidasyon](artifacts/CONSOLIDATION.md) ve T1–T7 reflection'ları üretildikleri checkpoint'in türetilmiş eserleri olarak korunur. Güncel devamı tek başlarına belirlemezler. «Yeni ground gerekmedi» sözleri bu vakalardaki sınırlı yorumdur; uygulama yeterliliği veya bağımsız Foundation doğrulaması değildir.

## T08 ve U016'dan gelen ayrımlar

[S015](sources/conversation/assistant/S015.md) ve [T08 notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md): kaydedilmiş ders, geri bildirimin kullanılması, korunmuş tepki değişimi, gösterilmiş fayda, yetki ve transfer farklı iddialar. Çalışma yöntemini değiştirmek de kapsamı/kanıtı/yetkisi/aktif kullanım yolu/geri dönüşü olan Work olabilir. Yeni zorunlu Learning Agent seçilmedi; sınama koşulları tartışıldı, deneyler çalıştırılmadı.

U016 «büyüme»yi yalnız ek parça sayısı değil; yeni işlevlerle birlikte mevcut işlevlerin yeni aktör ve kaynakları kapsaması olarak açıkladı. İki dosya/klasör/dikey-yatay ifadeleri örnektir, literal şema değildir. Branch çağrışımı açıkça yöntem/araç önerisi olarak verilmedi. [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) bu kaynak ve yorum sınırlarını korur.

## T09 — Yeni katkı ve sınırı

[T09 notu](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md), iki ayrı kontrolün birbirine güvenilerek kaldırılmasını karşıörnek yapar. X tek başına veya Z tek başına korunan koşulu taşırken X+Z birlikte denetimi kaldırabilir. Yerel PASS, başka bileşenin kalacağı varsayımıyla koşulludur; değişikliklerin birbirinin okuma/dayanak koşulunu bozması görünür olmalıdır.

Ayrı bir kapasite varyantında 60 dakikalık pencerede 40 ve 35 dakikalık bölünemez işler ayrı ayrı yapılabilir ama birlikte taahhüt edilemez. Actionable frontier ile birlikte başlatılabilir/ayrılmış iş kümesi ayrılır. Tek Work üzerinde atomik claim, bütün ortak kaynak/iş kuralı sorunlarını çözmez.

Aday koruma: yük taşıyan ortak koşul kapsamında güncel durumla kabulü ilişkilendirmek, ilgili değişiklikleri yeniden değerlendirmek ve aktif geçişte kontrol boşluğu bırakmamak. Her işi tek merkezi aktöre taşımak veya bütün sistemi kilitlemek zorunlu sonuç değildir. Eski onay ve dur mesajı fiilî dış etki kontrolüne eşit değildir. Çözümsüz kritik aday açık bekleyebilir; ilgisiz işler devam edebilir.

Kanıt sınıfı: açık öncüllerden mantıksal/aritmetik karşıörnek ve kaynak-informed tasarım baskısı. C01–C07 canlı testler değildir. Beads/Gas Town önceki pinli araştırmaları ve Foundation Control ayrımları seçici kullanıldı; PostgreSQL ve Kubernetes resmî dokümanlarına dar mekanizma kontrolü için bakıldı. Yeni product adoption/benchmark, tüm upstream denetimi, bağımsız SOUL doğrulaması veya yeni zorunlu primitive yoktur.

## Repository etkisi ve yayın sınırı

Başlangıç main: `e372ed7558b0b0ebbf388c864b0733382d1418ba`. Bu tur yalnız yeni T09 notu, bu STATE, paket INDEX'i ve explorations INDEX/CATALOG yönlendirmeleri güncellenir. Kaynak arşivi, manifest, onarım kayıtları, T08, T1–T7 eserleri, Foundation, studies, concepts ve agent-control korunur. Küçük devam notu tam konuşma transkripti diye sunulmaz.

Bu dosya kendi gelecekteki commit'ini veya henüz yapılmamış uzak kontrolü ilan etmez. Git yayını sonrası main ref, değişen yollar ve kritik içerikler geri okunur; aynı-assistant transfer kontrolü modelin etkinliğini kanıtlamaz.

## Sonraki sorumluluk

Bilinen arşiv onarımı kapalıdır; T09 aynı kavramsal programda ele alındı. Bir sonraki doğal soru, yeni aktör/araç/yol eklendiğinde mevcut ortak yükümlülüklerin gerçek kapsamasının nasıl korunacağıdır. T10 henüz yapılmadı; bu öneri yeni uygulama veya başka hedef repository'sini devralma yetkisi değildir. Güncel kullanıcının devam yönü ve ilgili kaynaklar birlikte değerlendirilir.
