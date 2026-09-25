# EXP-006 — WORK

**Rol:** EXP-006'nın üst iş haritası ve çalışma sırası.  
**Statü:** Diyalog ve araştırma çalışma haritası; Development OS mimarisi değildir.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Güncel iş:** **S1 — B1–B9 sonuçlarını araştırma örnekleriyle birlikte değerlendirmek.**

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

Roller işten önce icat edilmez. Bir kabiliyet veya sorumluluk adı otomatik olarak ayrı rol, ajan, servis veya dosya anlamına gelmez.

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

İlk ayrıştırma yapılmış olması, alt sorumluluklar ve ilk taşıyıcı adaylarının çıkarıldığı anlamına gelir; nihai rol/mimari kabulü veya uygulanmış kapasite değildir. Önceki dal dosyalarındaki `EXPLORED / candidate decomposition` aynı statüyü taşır.

Kullanıcının devam izni, araştırma bulgusunun teknik doğrulaması değildir. Kabul, kaynak kanıtı ve gerçek uygulama ayrı tutulur. Eski B dosyalarındaki sıradaki B yönlendirmeleri kendi üretim anlarının kaydıdır; güncel sıra STATE/HANDOFF ve bu üst haritadan alınır.

## B1–B9 ilk ayrıştırmalarında kullanılan yöntem

1. İşin hedef çıktısını tanımla.
2. Development OS'un bunu yapabilmesi için gerekli kabiliyet ve sorumlulukları çıkar.
3. Her sorumluluğu kim/ne taşımalı diye ayır.
4. Yapay zekâ rolü, mekanik sorumluluk ve insan sınırını ayır.
5. Yeni adayı ACTORS içindeki mevcut adaylarla karşılaştır; gereksiz kopya rol üretme.
6. Ayrıntıyı ilgili B dosyasında, güncel konumu üst çalışma kayıtlarında tut.

## S1 — Araştırmaya dayalı konsolidasyon

**Yöntem ve kaynak rotaları:** [S1 çalışma dosyası](work/S1-role-responsibility-consolidation.md).

S1 yalnız R1–R25'i daha az isme indirme işi değildir. Araştırmalardaki mekanizmalar; sorumluluk ayrımını, gereken bilgi/kabiliyeti, yetkiyi, hata sınırlarını ve fiilî geliştirme yükünü sınamak için kullanılır. Birleştirme, ayırma, koruma, eksik sorumluluk açma ve açık bırakma sonuçları gerekçeli kalır.

### Güncel ilerleme

- Hazırlık ve kaynak seçimi tamamlandı.
- [S1-01 — üretim, inceleme ve düzeltme](work/S1-01-production-review-correction.md) sınırlı incelemesi tamamlandı. A1–A4 ve G1 sonuçları **adaydır**; kullanıcı tarafından henüz kabul edilmiş sayılmaz.
- Ortak inceleme ailesi önerisi R2/R6/R8/R12/R15/R18'in özel sorularını silmez. Üretim ile düzeltme birlikte düşünülebilir; teşhis, karar, değişiklik ve yeniden sınama ayrılır.
- **G1:** M1–M9'un ve ilgili prosedürlerin fiilî geliştirme sorumluluğu, tasarım ve kurulum/işletimden yeterince açık ayrılmıyor. Üretim hiç düşünülmedi veya zorunlu yeni rol var denmedi.
- R1–R25/M1–M9 ilk türetim kaydı [ACTORS](ACTORS.md) içinde korunur. Yeni R/M kimliği veya nihai birleştirme yapılmadı.

**Önerilen sonraki dilim:** G1 üzerinden tasarım → üretim/uyarlama → bütünleştirme → sınama zincirini netleştirmek. B1/B2/B5/B6 aktarım noktaları, R14/R20 kapsamları ve ilgili araştırma örneklerine inilecek. Bu dilim henüz yapılmadı; yeni kullanıcı yönüyle devam edilecek.

### S1 boyunca açık kalan sorular

- Hangi adaylar aynı üst rol ailesinin farklı uzmanlık veya görev kipleridir?
- Hangi inceleme iddiaları aynı görevlendirmede taşınabilir; nerede farklı bilgi veya yeterince bağımsız kanıt gerekir?
- Tasarım, üretim, kurulum ve işletim hangi noktalarda farklı sorumluluk doğurur?
- R3'ün alanlar arası teşhisinin bilgi/yeterlik sınırı nedir?
- R19/R20'nin diğer sorumlularla ilişkisi, DevOS geliştirmesi ile SOUL işletimini karıştırmadan nasıl kurulmalı?
- M1–M9 daha az sayıda teknik düzenle taşınabilir mi; bunları kim geliştirecek ve sınayacak?
- Her B1–B9 işi için açık geliştirme sorumlusu, sınama yolu ve gerekli mekanik destek var mı?
- İnsan yetki/kabul çekirdeği hangi kararlarda gerçekten gerekir?

S1 bitmeden mimariye geçilmez. Bu incelemenin kaynağa dayalı olması, bütün rol düzeninin bağımsız doğrulandığı anlamına gelmez.

## Önemli sınır

B1–B9, SOUL'un modül listesi değildir. Foundation'daki bilgi, aktör, iş ve ortam zeminleri de dört yazılım modülü olarak varsayılmamaktadır.

Örnek sistemin kendi işini işletmesi ile DevOS'un o kapasiteyi SOUL için geliştirmesi aynı sayılmaz. Mekanik sorumluluk tanımı onu geliştirecek aktörün yerine geçmez; kaynakların bulunması da bunlara erişme ve kullanma kabiliyetini kendiliğinden sağlamaz.
