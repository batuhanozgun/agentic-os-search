# EXP-004 — STATE

**Güncelleme:** 2026-09-21, U016 kaynak-sadakati onarımı.
**Arşiv:** SOURCE-CONTENT-REPAIRED / PUBLICATION-PENDING. Onarılan içerik çalışma dalında; main kapanışı henüz ilan edilmez.
**Kavramsal çalışma:** T1–T8 yapıldı; hepsi konuşma içi sentetik deneme. T09 bu tur başlatılmadı.
**Kaynak:** U001–U016 / S001–S015; 31 görünür mesaj, 16 kaynak dosyası. [Diyalog](sources/conversation/INDEX.md), [manifest](SOURCE-MANIFEST.json).
**Önceki yayın:** PR #29 `46ab3ff5993683c6124d7786533529e0f6147914`; PR #30 `882e0dfd271bd8c284df59f81c882a66a88f9933`. Bu teknik yayınlar önceki tamlık iddiasını doğrulamıyordu.

## Amaç ve son kullanıcı yönü

Foundation ve studies birikimini kullanarak SOUL'un büyük, uzun, çok aktörlü ve baştan tamamen bilinmeyen iş için ihtiyaç duyacağı çalışma düzenini sorgulamak; örnekleri otomatik modül/mimari kararına çevirmemek.

U014 önceki kesimi kaydetme yetkisiydi. U015 aynı kavramsal çalışmayı sürdürdü ve T08 oluştu. [U016](sources/conversation/USER-MESSAGES.md#u016) eksik varsa önce repository'yi düzeltmeyi istedi; kavramsal devam yönü bu onarımdan sonra korunur. Bu tur yeni test, dış araştırma kampanyası, SOUL/Development OS kurulumu veya kontrol dosyası değişikliği yapılmaz.

## Kaynak onarımının gerçek durumu

Önceki S001–S013 dosyaları özetlenmiş/yeniden ifade edilmişti; S013'e U014 sonrası yorum da eklenmişti. Bunlar [ayrı tarihsel görünüm dizininde](artifacts/condensed-before-repair/README.md) aynı Git alt-ağaç kimliğiyle korunur. Güncel kaynak yollarındaki S001–S013, görünür özgün yanıtlardan yeniden ve kısaltılmadan aktarıldı. S014 önceki hatalı tamlık cevabı; S015 tam T08 cevabı; U016 bu onarımın kaynağıdır. Bu turun henüz verilmemiş S016 cevabı kesime katılmadı.

Kaynak payload ref'i `f1e93a9f052fb98b3f2e28e987233f3b51193534`; assistant tree `ba3111b97927ebb231947b2a500eee1d534a5a16`; kullanıcı blob'u `1866f243b3771a2d0152bc6b20f67c1a7f3f80c3`. Kaynak dosyaları arşiv başlıkları dahil 182.486 byte. Kimlik/byte kontrolü kaynak doğruluğu veya bağımsız transkripsiyon doğrulaması değildir. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md) ve [onarım kontrolleri](checks/REPAIR-20260921.md) ayrıdır.

## Devralınan model — hipotez, mimari değil

T1: ham talep ve yeterince belirlenmiş Mission farklı. T2: ihtiyaç/koşul, Work, plan ve eylem ayrılır; keşif sürer. T3: rol, aktör, capability, competence ve authority ayrılır. T4: sistemdeki bilgi, uygun/erişilebilir bağlam ve fiilî kullanım farklıdır. T5: araç kataloğu, kullanılabilir yetenek, Run ve gerçek etki ayrı. T6: tamamlanma, kanıt desteği, kabul, entegrasyon ve amaç etkisi aynı değildir. T7: aktör, Run ve Work sürekliliği; kalıcılık, güncellik ve gerçek durumla uzlaştırma ayrılır.

[İlk konsolidasyon](artifacts/CONSOLIDATION.md) ve T1–T7 reflection'ları üretildikleri checkpoint'in türetilmiş eserleri olarak korunur. Güncel devamı tek başlarına belirlemezler. “Yeni ground gerekmedi” sözleri bu vakalardaki sınırlı yorumdur; uygulama yeterliliği veya bağımsız Foundation doğrulaması değildir.

## T08 ve U016'dan gelen güncel ayrımlar

[S015](sources/conversation/assistant/S015.md) ve [T08 notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md): kaydedilmiş ders, geri bildirimin kullanılması, korunmuş tepki değişimi, gösterilmiş fayda, yetki ve transfer farklı iddialar. Çalışma yöntemini değiştirmek de kapsamı/kanıtı/yetkisi/aktif kullanım yolu/geri dönüşü olan Work olabilir. Yeni zorunlu Learning Agent seçilmedi; sınama koşulları tartışıldı, deneyler çalıştırılmadı.

U016 “büyüme”yi yalnız ek parça sayısı değil; yeni işlevlerle birlikte mevcut işlevlerin yeni aktör ve kaynakları kapsaması olarak açıkladı. İki dosya/klasör/dikey-yatay ifadeleri örnektir, literal şema değildir. Branch çağrışımı açıkça yöntem/araç önerisi olarak verilmedi. [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) bu kaynak ve yorum sınırlarını korur; kullanıcının teknik oracle olduğunu veya bu sözcüklerin mimariyi seçtiğini varsaymaz.

## Sonraki sorumluluk

Bu turun işi kaynak/kapsam/yönlendirme onarımını main'e güvenli yayımlayıp doğrulamaktır. Ayrı çalışma dalı `repair/exp-004-source-fidelity-20260921`; başlangıç main `fb488942ddbd951f3ce5887c1acdab2c3aac8bc6`. Gerçek yayın [PUBLICATION](checks/PUBLICATION.md) ile kapatılır.

Onarım sonrasında aynı kavramsal çalışma T08 ve U016'dan devralınabilir. Doğal karşı-test eşzamanlı işlerin yöntem, kaynak, sürüm ve yetki çatışmalarıdır; branch benzetmesi o testi Git çözümüne sabitlemez. Yeni uygulama veya başka hedef repository'sini devralma yetkisi yoktur.
