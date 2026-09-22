# EXP-005 — STATE

**Güncelleme:** 2026-09-22.  
**Arşiv durumu:** Kaynak aktarımı, özgün görev eseri, dersler ve okuma yolları hazırlanmıştır; paket/keşif denetimi ve main yayın makbuzu bu aşamada henüz kapanmamıştır.  
**Geliştirme durumu:** **DEVOS02-NEED-DISCOVERY-20260922 / USER-CANCELLED.**  
**Araştırma sorusu:** **AÇIK.** Genel ihtiyaç keşfi sorunu çözülmüş sayılmaz.  
**Güncel yetki:** U048'in EXP-005 arşivleme talebi; yalnız bu paket ve explorations INDEX/CATALOG yayını. Yeni geliştirme, deney, erişim kurulumu veya kontrol değişikliği yoktur.

## 1. Son kullanıcı kararları

[U045](sources/conversation/09-IPTAL-VE-KONU-OZETI.md#U045), plansız/önkoşulları ve devri kullanıcıya hatırlatan yürütmeye itiraz ederek bu çalışma hattını iptal etti. [U048](sources/conversation/10-PROTOKOL-DEGERLENDIRMESI-VE-ARSIV-TALEBI.md#U048), konu açıkken deneyimin ders olarak arşivlenmesini ayrıca yetkilendirdi.

İptal edilen şey bütün SOUL vizyonu veya tüm Development OS değil, bu konuşmadan başlatılan ihtiyaç-keşfi geliştirme hattıdır. Eski devam mesajları, görev sözleşmesi, deney ve PR kayıtları tarihsel malzemedir. Buradaki arşiv yetkisi onları yeniden etkinleştirmez. Assistant'ın iptal beyanı ayrıca dış Codex sürecinin kapatıldığını veya PR'nin GitHub'da kapandığını kanıtlamaz.

## 2. Korunan içerik

- [Kaynak konuşma](sources/conversation/INDEX.md): On dosyada U001–U048 / A001–A047; 95 görünür mesaj. Başlangıç görsel/kapsam sorusundan iptal ve arşiv yetkisine kadar.
- [Özgün görev belgesi](artifacts/DEVOS02-NEED-DISCOVERY-20260922.md): Tarihsel sürüm 1.0; değiştirilmeden saklanır, bugün etkin görev değildir.
- [Dersler ve açık sorular](reflections/LESSONS-AND-OPEN-QUESTIONS.md): Erken teşhis, fiilî hazırlık, Research erişimi/kullanımı, sınırlı deney, yayın/devir ve kullanıcıya yük aktarımı. Önceki öz değerlendirme de eleştirel biçimde nitelendirilir.
- [Konu haritası](retrieval/TOPIC-MAP.md), [kümülatif okuma](retrieval/CUMULATIVE-READING.md), [köken/ekler](sources/ORIGIN-AND-ATTACHMENTS.md), [manifest](SOURCE-MANIFEST.json), [arşiv denetimi](checks/ARCHIVE-REVIEW.md).

Bu arşivin tamamlanması ne açık araştırma sorusunun ne de iptal edilmiş uygulama görevinin tamamlanmasıdır. Kullanıcının ders kaydı talebi, bütün retrospektif yorumları teknik olarak kabul ettiği anlamına gelmez.

## 3. Kanıt düzeyi ve aktarım sınırı

Konuşma **model-visible, normalize edilmiş aktarım**dır; byte-perfect platform export'u değildir. Kullanıcının aktardığı Codex raporları, assistant yorumları ve gerçek repository gözlemleri ayrı tutulur. Eksik/atlanmış araç mesajları veya tam Cloud/CLI transkriptleri uydurulmadı. Dersler aynı assistant'ın kaynak karşılaştırmalı self-review'üdür; bağımsız doğrulama değildir.

Özgün görev belgesinin Git blob kimliği, gerçek konuşma ekinden hesaplanan kimlikle karşılaştırılır. İki başlangıç görselinin metin envanteri ve hash bilgisi repodadır; **PNG asılları bu Git paketine yüklenmiş değildir**. PNG'ler ve görev belgesi ayrıca konuşma teslimindeki `EXP-005-original-attachments.zip` paketinde korunur; bu sandbox eki kalıcı GitHub kaynağı yerine geçmez.

V2 raporunda iki yöntem dört görevde aynı puanı aldı ve aday geri alındı. Bu yalnız sınanan aday/vaka kapsamının raporudur; genel eşdeğerlik, tüm kuralların etkisizliği veya mevcut RPD'nin genel yeterliği değildir. Research'ün gerçek kullanım yükü o deneyde kapanmadı. Ayrıntılı sınırlar dersler §7'de.

## 4. Yayın ve çalışma sınırı

Arşivleme başlangıç main'i `4d8b8b1aba963d5503676bdcb73b7d68b40045d7`; çalışma branch'i `archive/exp-005-ihtiyac-kesfi-dersleri-20260922`. Tek arşiv yazıcısı bu ChatGPT oturumudur. Ayrı native reviewer veya bağımsız arşiv doğrulayıcı çalıştırılmadı.

Yazma kapsamı bu paket ile `explorations/INDEX.md` ve `explorations/CATALOG.md`dir. Önceki EXP paketleri, agent-control, Research bulguları ve DevOS repository'si korunur. Diğer çalışmaların main değişiklikleri geri alınmaz. Arşiv PR'si, DevOS PR #1 değildir.

**Şimdiki arşiv işi:** Manifest/keşif denetimini ve normal main yayını/geri okumayı tamamlamak. Gerçek yayın sonucu ve exact referans [checks/ARCHIVE-REVIEW.md](checks/ARCHIVE-REVIEW.md) içinde, gelecekteki commit'i önceden başarılı saymadan kaydedilecektir.

## 5. Sonraki kullanım

Geliştirme için **next authorised work: NONE — bu hat iptal edildi**. Açık sorular yeni iş kuyruğu değildir. Sonraki ayrıca yetkilendirilmiş konuşma bu deneyimi yeniden kullanabilir, yorumlarını sorgulayabilir ve araştırma/çalışma yöntemini ele alabilir; aynı testleri otomatik yeniden koşmaz, eski talimatları uygulamaz. Mevcut kaynaklar yeni görüşe uydurularak silinmez.
