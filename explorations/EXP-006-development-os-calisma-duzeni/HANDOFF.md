# EXP-006 — HANDOFF

**Amaç:** Önceki konuşmayı görmeyen bir oturumun doğru işi, kaynakları ve karar statüsünü devralması.  
**Tarih:** 25 Eylül 2026.  
**Güncel iş:** **S1 — araştırmaya dayalı rol ve sorumluluk konsolidasyonu.**

## Yeni oturumda okuma

1. [STATE](STATE.md)
2. Bu dosya
3. [WORK](WORK.md)
4. [ACTORS](ACTORS.md)
5. [S1 yöntem ve dilim dizini](work/S1-role-responsibility-consolidation.md)
6. [S1-01](work/S1-01-production-review-correction.md): G1'e veya bu turun bulgularına devam edilecekse tam oku.
7. İhtiyaç doğan B dosyalarına ve ilgili studies kaynaklarına seçici in.

[DECISIONS](DECISIONS.md) kullanıcı kararlarını, [EXP-006_Context](EXP-006_Context) konuşmanın nedenini ve birlikte çalışma biçimini taşır. Bütün eski B ayrıntılarını her girişte yeniden yüklemek gerekmez.

## Üst zincir ve eldeki malzeme

Başlangıç sorusu Development OS'taki yapay zekâ rolleriydi. Jenerik rol listesi üretmemek için önce SOUL hedefi somutlaştırıldı; sonra DevOS'un bu hedef için yapacağı B1–B9 işleri ve gerekli sorumluluklar açıldı.

B1–B9'un ilk ayrıştırmaları tamamlandı; bunlar adaydır. [ACTORS](ACTORS.md), R1–R25 rol adaylarını ve M1–M9 mekanik sorumluluk kümelerini taşır. Bu sayılar ajan/servis sayısı değildir. Eski kimlikler S1'de izlenebilirlik için korunuyor.

İnsan müşterinin çekirdeği **yetki + kabul** olarak kalır. SOUL tanımı bu aşama için yeterince somut çalışma hedefi kabul edildi; nihai mimari veya teknik doğrulama değildir.

## Kullanıcı yönlendirmesi

Kullanıcı studies araştırmalarının S1'de kullanılmasını istedi. Ardından “Güzel. Devam et lütfen.” diyerek önerilen ilk üretim–inceleme–düzeltme diliminin yürütülmesine yön verdi.

Bu, hazır sistemlerin rol adlarını kopyalama veya bütün araştırmaları baştan okuma talebi değildir. Her karşılaştırmada DevOS sorusu, kaynağın kendi mekanizması, aktarım koşulu, sınır ve aday sonuç ayrı tutulur.

## S1-01'de yapılan ve yapılmayan

**Yapıldı:** Superpowers S03/S04 ve U03/kaynak kaydı tam; asıl üretici ve görev inceleyicisi tam; asıl SDD ilgili bölümleri seçici okundu. gstack CORE/INDEX ve teslim yeterliği araştırmasından ilgili kısımlar, asıl QA şablonunun ilgili bölümleri okundu. Eski ürün deneyleri yeniden çalıştırılmadı. Doğrudan dış okumalar sabit araştırma sürümlerindendir; güncel ürün veya etkin kurulum sertifikası değildir.

**Aday sonuçlar:**

- **A1:** R2/R6/R8/R12/R15/R18 ortak inceleme/doğrulama ailesinde düşünülebilir. Farklı iddialar, gerekli uzmanlık ve bağımsızlık korunur; tek genel inceleyici yeterli ilan edilmez.
- **A2:** Üretim ve düzeltme aynı sorumluluk ailesinde taşınabilir. İnceleyici düzeltirse o değişiklik bakımından üretici de olur; değişmiş nesne eski hükmü otomatik devralmaz.
- **A3:** R3 teşhisi, düzeltmeyi uygulama ve teknik karar verme ayrı sorumluluklardır. Aynı aktörün bunları taşıma koşulları ayrıca değerlendirilir.
- **A4:** Yerel inceleme ve düzeltme, bütünleştirilmiş sonucun yeterliğini veya müşteri kabulünü tek başına göstermez.
- **G1:** Tasarım ve kurulum/işletim ile mekanizmaların kodunu, prosedürünü ve bağlantılarını fiilen geliştirme sorumluluğu yeterince açık ayrılmıyor. B1/R1 → B5/B6; B5/R13/R14/M4/M5 ve B7/R20 üzerinden açıklık görüldü. Üretim hiç yok denmedi; bütün B1–B9 yeniden incelenmiş sayılmadı.

**Yapılmadı:** Nihai rol birleştirme, yeni R26 veya mekanik kimlik, canlı DevOS/SOUL testi, mimari, ürün/araç seçimi, kurulum. Kullanıcı S1-01 sonuçlarını henüz kabul etmiş sayılmaz.

## Sonraki inceleme ve dönüş sınırı

**Önerilen sonraki S1 dilimi:** G1'i aç; tasarım → üretim/uyarlama → bütünleştirme → sınama zincirinin DevOS tarafındaki sorumlularını belirle. B1/B2/B5/B6'daki aktarım noktalarını ve R14/R20'nin kurma/işletme sınırlarını, karar için gereken kaynak derinliğinde incele.

Yeni kullanıcı yönüyle devam ederken önce onun bu bulgulara yaptığı düzeltmeyi dikkate al. İlerlemenin sonucu mevcut rolü genişletmek, ortak geliştirme ailesi oluşturmak, farklı uzmanlıklara ayırmak veya belirsizliği açık bırakmak olabilir. Sırf açıklık bulundu diye otomatik yeni rol ekleme.

Bir sınırlı sorumluluk kümesini gerekçeleriyle sunup kullanıcıya dön; bütün S1'i veya mimariyi tek turda bitirmeye çalışma.

## Korunacak sınırlar

- DevOS'un SOUL'u geliştirmesi, SOUL'un müşteri işini işletmesi ve EXP-006'nın kendi kayıt düzeni ayrı düzeylerdir.
- Aynı aile, aynı uzmanlık, aynı rol görevlendirmesi ve aynı fiziksel aktör demek değildir.
- Farklı ajan etiketi bağımsız kanıt yaratmaz; aynı eksik bağlam birden fazla inceleyicide korunabilir.
- Bulguyu ertelemek veya yetkili karar vermek teknik doğruluk kanıtı değildir.
- Superpowers'ın kendi yetki ifadeleri arasındaki açık sorular burada çözülmüş sayılmaz; kaynak insana teknik yük bırakıyor diye bunu Batu'ya taşıma.
- M1–M9'un işlevini yazmak, onları geliştirecek tarafı sağlamaz.
- Araştırmalar mevcut adayları haklı çıkarmak kadar değiştirmek veya elemek için de kullanılır.

STATE/HANDOFF/S1 güncel ilerlemeyi taşır. ACTORS ilk R/M türetim kaydı olarak korunmuştur; S1-01 önerilerini kabul edilmiş nihai liste gibi okumama.
