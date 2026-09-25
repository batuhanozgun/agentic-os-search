# EXP-006 — WORK

**Rol:** EXP-006'nın üst iş haritası ve çalışma sırası.  
**Statü:** Diyalog ve araştırma çalışma haritası; Development OS mimarisi değildir.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Güncel iş:** **S1 — B1–B9 sonuçlarını araştırma örnekleri ve aktör özellikleriyle birlikte değerlendirmek.**

## Katman mantığı

```text
SOUL hedefi
  ↓
Development OS'un SOUL üzerinde yapacağı ana işler (B1–B9)
  ↓
Her iş için gerekli Development OS kabiliyet ve sorumlulukları
  ↓
Bunları taşıyabilecek yapay zekâ rolleri / mekanik sistemler / insan
  ↓
S1 — gerekçeli rol ve sorumluluk konsolidasyonu
  ↓
Development OS yapısı
  ↓
İhtiyaçtan türeyen mekanizma ve araç seçimleri
```

Roller işten önce icat edilmez. Bir kabiliyet veya sorumluluk adı otomatik ayrı rol, ajan, servis veya dosya anlamına gelmez. Rol ailesi de aynı model çağrısında birleştirilmiş görev demek değildir.

## Birinci seviye iş haritası

| ID | Development OS'un SOUL üzerinde yaptığı iş | Güncel statü | Ayrıntı |
|---|---|---|---|
| **B1** | SOUL'un ortak entelektüel çalışma tabanını geliştirmek | İlk ayrıştırma yapıldı / aday | [B1](work/B1-common-intellectual-baseline.md) |
| **B2** | SOUL'un bilgi kapasitesini geliştirmek | İlk ayrıştırma yapıldı / aday | [B2](work/B2-information-capacity.md) |
| **B3** | SOUL'un aktör kapasitesini geliştirmek | İlk ayrıştırma yapıldı / aday | [B3](work/B3-actors-capacity.md) |
| **B4** | SOUL'un iş kapasitesini geliştirmek | İlk ayrıştırma yapıldı / aday | [B4](work/B4-work-capacity.md) |
| **B5** | SOUL'un ortam kapasitesini geliştirmek | İlk ayrıştırma yapıldı / aday | [B5](work/B5-environment-capacity.md) |
| **B6** | Dört zemini birbirine doğru bağlayan düzeni geliştirmek | İlk ayrıştırma yapıldı / aday | [B6](work/B6-cross-ground-integration.md) |
| **B7** | SOUL'un işe göre çalışma sistemi kurma ve genişletme kapasitesini geliştirmek | İlk ayrıştırma yapıldı / aday | [B7](work/B7-system-formation.md) |
| **B8** | Süreklilik, değişim, toparlanma ve öğrenme kapasitesini geliştirmek | İlk ayrıştırma yapıldı / aday | [B8](work/B8-continuity-change-recovery.md) |
| **B9** | Ortaya çıkan SOUL'u bütün olarak birleştirmek ve gerçek görevlerle sınamak | İlk ayrıştırma yapıldı / aday | [B9](work/B9-integration-and-testing.md) |

## Statülerin anlamı

İlk ayrıştırma, alt sorumluluklar ve ilk taşıyıcı adaylarının çıkarılmasıdır; nihai rol/mimari kabulü veya uygulanmış kapasite değildir. Eski dal dosyalarındaki EXPLORED / candidate decomposition aynı statüyü taşır.

Kullanıcının devam izni teknik doğrulama değildir. Kabul, kaynak kanıtı ve gerçek uygulama ayrı tutulur. Eski B dosyalarındaki sıradaki B yönlendirmeleri tarihsel üretim anlarını taşır; güncel sıra STATE/HANDOFF'tan alınır.

## B1–B9 ilk ayrıştırmalarında kullanılan yöntem

1. İşin hedef çıktısını tanımla.
2. Development OS'un bunu yapabilmesi için gerekli kabiliyet ve sorumlulukları çıkar.
3. Her sorumluluğu kim/ne taşımalı diye ayır.
4. Yapay zekâ rolü, mekanik sorumluluk ve insan sınırını ayır.
5. Yeni adayı ACTORS içindeki adaylarla karşılaştır; gereksiz kopya üretme.
6. Ayrıntıyı ilgili B dosyasında, güncel konumu üst çalışma kayıtlarında tut.

## S1 — Araştırmaya dayalı konsolidasyon

**Yöntem ve kaynak rotaları:** [S1 çalışma dosyası](work/S1-role-responsibility-consolidation.md).

S1 yalnız R1–R25'i daha az isme indirme işi değildir. Araştırmalar sorumluluk ayrımını, gereken bilgi/kabiliyeti, yetkiyi, hata sınırlarını ve fiilî geliştirme yükünü sınar. Aktörün özellikleri, etkin rolün başarı yönü, bağlam/araç koşulları ve gerektiğinde çağrılması da değerlendirilir.

### Güncel ilerleme

- Hazırlık ve kaynak seçimi tamamlandı.
- [S1-01](work/S1-01-production-review-correction.md): A1–A4/G1 adayları. Ortak inceleme ailesi, üretim–düzeltme, teşhis/karar ayrımı, sürüme bağlı kanıt.
- [S1-02](work/S1-02-actor-conditioned-role-purpose.md): kullanıcının aktör türü/motivasyon/uyarlama yönü ve Keel kaynakları. Ailede gruplamak ile aynı etkin görevlendirmede çalıştırmak ayrıldı; çoklu ölçüt ile çatışan başarı yönü eşitlenmedi.
- [S1-03](work/S1-03-role-purpose-activation-and-transfer.md): kullanıcının aynı konuda bir tur daha isteği üzerine OS Architect'in Keel geliştirme kayıtları okundu. Rolün fiilî başarı yönü, ortak düşünsel taban, tetiklenme/sonuç tüketimi ve geliştiren→kurucu→kurulmuş role aktarım yükleri görünür kılındı. Sonuçlar aday; ham deney ve güncel araç davranışı doğrulanmadı.
- **G1:** Kod/prosedür/bağlantının geliştirilmesini, hazır mekanizmayı kurma/işletmeden ayıran sorumluluk eşlemesi açık. S1-02 bellek, S1-03 rolün yazma sınırı örneğiyle açıklama sağladı; bütün M1–M9 için eşleme yapılmadı.
- R1–R25/M1–M9 ilk türetimleri ACTORS içinde korunur. Yeni R/M kimliği veya nihai birleştirme yok.

**Güncel dönüş:** S1-03 katkıları kullanıcıya sunulur. Sonraki kullanıcı yönüyle G1'in tasarım → üretim/uyarlama → bütünleştirme → sınama zinciri bu aktör/rol ölçütleriyle değerlendirilebilir. Model eğitimi, tüm aktör türlerinin envanteri veya mimari çalışması otomatik başlamaz.

### S1 boyunca açık kalan sorular

- Hangi adaylar aynı ailenin farklı uzmanlık veya görev kipleri?
- Hangi sorumluluklar aynı etkin görevlendirmede tutarlı başarı yönü taşıyabilir; hangi yerel başarı üst amacı bozabilir?
- Ortak düşünsel taban korunurken role hangi bağlam, araç, yetki, tetik ve devir koşulları sağlanmalı?
- Rolün gerçekten çağrılması ve sonucunun sonraki işte kullanılması nasıl görülecek?
- Geliştirenin birikimi kurucuya ve kurulmuş role aktarılırken ne kaybolabilir?
- Nerede farklı bilgi/yeterlik veya yeterince bağımsız kanıt gerekir?
- Tasarım, üretim, kurulum ve işletim nerede farklı sorumluluk doğurur?
- R3'ün alanlar arası teşhisinin bilgi/yeterlik sınırı nedir?
- R19/R20'nin ilişkisi DevOS geliştirmesi ile SOUL işletimini karıştırmadan nasıl kurulmalı?
- M1–M9 daha az teknik düzenle taşınabilir mi; bunları kim geliştirecek ve sınayacak?
- Her B1–B9 işi için geliştirme sorumlusu, sınama yolu ve mekanik destek var mı?
- İnsan yetki/kabul çekirdeği hangi kararlarda gerçekten gerekir?

S1 bitmeden mimariye geçilmez. Kaynaklara dayalı değerlendirme, bütün rol düzeninin bağımsız doğrulandığı anlamına gelmez.

## Önemli sınır

B1–B9 SOUL modülleri değildir; Foundation'ın bilgi, aktör, iş ve ortam zeminleri dört yazılım modülü sayılmaz. Keel ve OS Architect kendi bağlamlarında kaynak örnekleridir; eski kuralları, kuyrukları ve kullanıcı kapıları DevOS'a veya EXP-006'ya ithal edilmez.

Örnek sistemin işletimi ile DevOS'un o kapasiteyi SOUL için geliştirmesi aynı şey değildir. Mekanik sorumluluk onu geliştirecek aktörün yerine geçmez; kaynakların bulunması erişme/kullanma kabiliyetini kendiliğinden sağlamaz. S1-03 yalnız bu ayrımları değerlendiren kayıt/devir yüzeylerini değiştirdi; kaynak depolar ve ilk rol kayıtları korunur.
