# DEVOS-001 — yönetilen iş ve devam kaydı

**Durum:** YENİDEN YÖNLENDİRİLDİ / bütün-korpus okuma ve çıkarım hazırlığı aktif.
**Güncel amaç:** Development OS'u kuracak çalışma düzenini, Research korpusunun tamamından çıkarılan fikir ve örneklerin birlikte değerlendirilmesiyle belirlemek.
**Yetki:** kullanıcının son açık yönü [BRIEF](BRIEF.md). **Yöntem:** [METHOD](METHOD.md). **Kapsam ve kayıt rotaları:** [COVERAGE](reading/COVERAGE.md). **Kanal:** [EXCHANGE](EXCHANGE.md).

## Yön değişikliği — 23 Eylül 2026

Kullanıcı, ilk hedeften kopulduğunu belirtti ve önce bütün repo incelemesi, her tur kaynak-bağlı kayıt, bütün kayıtlar tamamlandıktan sonra çalışma yapısına karar verilmesini istedi. Bu kayıt, önceki W03b/C-003 revizyonu→M1–M3 sırasını güncel iş olmaktan çıkarır. Deneme numarası 001 kalır; yeni repo veya Deneme-002 açılmaz.

Research'ün hatası: tekil denetim sorunları ve test tasarımı, bütün çalışma yapısını hazırlama işinin önüne geçirildi. Bunu yalnız iletişim eksikliği diye adlandırmıyoruz. Önceki bulgular korunur; onların varlığı yön sapmasını haklı çıkarmaz.

E19, D01, M1–M3, yeni test deposu ve R-003'teki dar revizyonlar **ERTELENDİ / aktif ana iş değil**. Başarılı veya yanlış ilan edilmedi. İleride bütün kayıtlar değerlendirildiğinde gerçekten gereken adaylar olarak yeniden ele alınabilirler; okuma aşamasının kapısı değiller.

## Aşamalar, sorumlular ve geçiş koşulları

| Kimlik | İş | Sorumlu | Güncel durum / kapanış koşulu |
|---|---|---|---|
| P0 | Bütün kaynak kapsamı, yöntem, kaynak kimliği ve iş bölümü | Research; dosya manifesti Claude katkısı | BAŞLADI. Kök/research/Foundation/studies doğrudan ağaçları görüldü; bütün leaf-file manifesti henüz yok |
| P1 | Korpusun tam okuması ve her tur katkı kayıtları | Research + Claude, METHOD'teki birincil dağılımla | AKTİF. Okunmayan her paket açık; ilk Research kümesi Foundation genel girişleri ve 08 paketi |
| P2 | Bütün kayıtların iki aktörce tam okunması ve ortak karşılaştırma | Research + Claude | BAŞLAMADI. P1'in bütün kapsamı ve maddi boşlukları kapanmadan başlamaz |
| P3 | Çalışma yapısı seçenekleri, gerekçeli seçim ve bütünsel işleyiş | Research + Claude; owner tercihleri Batu | BAŞLAMADI. P2'ye dayanır; mevcut Claude yapısı veya M1–M3 varsayılan sonuç değil |
| P4 | Seçilen düzenin kurulumu ve gerçek işte değerlendirme | Sonradan belirlenecek uygulama sorumluları | BAŞLAMADI. Seçilmiş yapı, gerçek ortam ve uygulama yetkisi gerekir |

Bu plan, son kullanıcı talebinin sırasıdır; sıfırdan Development OS mimarisi seçimi değildir. Her tur yeni plan üretmek yerine P1 kuyruğu ilerler. Alt kaynakta hata bulunması otomatik yeni debug işi açmaz; kayıt ve üst amaca katkı korunur.

## Bu turun kaynak ve yayın durumu

Başlangıç Research main `dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb`, tree `b17da2eb4cdb3a4e8ff26ade2621825047ae9632`. Kaynak okuma tabanı bu commit'tir; bu denemenin yeni kayıtları source corpus'a geri beslenmez.
Son kontrol edilen hedef main `21ff74268f22c23553fa5b1cc9a55c68904f1f0b`, önceki C-002 değerlendirmesiyle aynı. Bu tur C-003 üzerinde yeni denetim başlatılmadı.

Yöntem/kapsam/yön düzeltmesi ve [R-004](messages/research/R-004.md) hazırlanıyor. Yayın/alım henüz tamamlandı sayılmaz; actual kontrollerden sonra bu paragraf güncellenecek. İlk kaynak çıkarımı bu açılış yayınından sonra kaydedilecek; henüz bütün repo veya Foundation okunmuş sayılmaz.

## Sonraki gerçek işler

**Research:** Foundation STATE/INDEX ve 08 paketinin dosya envanteri üzerinden ilk tam kaynak kümesini oku, `reading/` altında kaynak-bağlı kayıt çıkar; kapsamı ve sıradaki dosyayı güncelle. Yalnız Claude'dan yanıt bekleme.
**Claude:** R-004 alındısından sonra kendi PLAN/STATE yönünü uzlaştır; bütün kaynak dosya manifestini çıkar; studies girişleri ve gstack'ten başlayarak bütün paketleri METHOD uyarınca oku/kaydet. Kendi kalıcı kayıtları `coordination/devos-001/reading/`; C mesajı kayıtlara bağlantı ve gerçek kapsam taşır. Atama alım veya tamamlanma değildir.
**Batu:** teknik yöntem seçimi, dosya adı bulma veya mesaj içeriği taşıma işi yok. Repo kanalı oturumları kendiliğinden uyandırmadığı için gerektiğinde yalnız 'R-004'ü oku' tetiklemesi gerekebilir.

Sonraki oturum BRIEF/WORK/METHOD/COVERAGE'den başlar; eski 'C-003 bekleniyor, ardından ilk dilim kurulur' zincirini devam ettirmez. Her okuma dilimi remote'da yayımlanıp geri okunur; yeni bulgu yığıp güncel bağlamı yalnız sohbette bırakma.

## Tarihsel işler ve mesajlar

W00/W01 kanal açılışı ve R-001/C-001 aktarımı, W02 sınırlı inceleme ve D01 gerçekleşti. W03a ilk dar dilim seçimi ve W03b revizyonu eski yöndür; P0–P3 tarafından sıra bakımından geçersiz kılındı. W04 kurulumu başlamadı; W05 kapanışı yapılmadı.

Özgün R-001, R-002, R-003 ve C-001/C-002 bağlantıları ile yayın makbuzları [önceki WORK](https://github.com/batuhanozgun/agentic-os-search/blob/dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb/development-os/attempts/001/WORK.md)'te korunur. Aynı yanıt ilişkileri yeni yöne onay diye taşınmaz.

R-004 yeni kullanıcı yönünü taşır. Claude'un R-004'ü okuması henüz teyitsizdir; henüz oluşmamış C yanıtı üretilmez. R-003'e sonradan gelen cevap varsa kaybolmaz, fakat eski kapsamı otomatik yeniden açmaz.
