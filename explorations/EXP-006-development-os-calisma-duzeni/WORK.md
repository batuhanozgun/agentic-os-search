# EXP-006 — WORK

**Rol:** EXP-006 içindeki current Work haritası ve sequencing yüzeyi.  
**Statü:** DIALOGUE WORK SYSTEM / çalışma haritası; Development OS mimarisi değildir.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Current Work:** **B8 — Süreklilik, değişim, toparlanma ve öğrenme kapasitesini geliştirmek.**

## Katman mantığı

```text
SOUL hedefi
  ↓
Development OS'un SOUL üzerinde yapacağı ana işler (B1–B9)
  ↓
Her iş için gerekli Development OS kabiliyet ve sorumlulukları
  ↓
Bu sorumlulukları taşıyacak yapay zekâ rolleri / mekanik sistemler / insan
  ↓
Development OS yapısı
  ↓
İhtiyaçtan türeyen mekanizma ve araç seçimleri
```

Roller Work'ten önce icat edilmez. Bir kabiliyet veya sorumluluk adı otomatik olarak ayrı rol, agent, servis veya dosya anlamına gelmez.

## Birinci seviye Work haritası

| ID | Development OS'un SOUL üzerinde yaptığı iş | Güncel statü | Ayrıntı |
|---|---|---|---|
| **B1** | SOUL'un ortak entelektüel çalışma tabanını geliştirmek | **EXPLORED / candidate decomposition** | [B1](work/B1-common-intellectual-baseline.md) |
| **B2** | SOUL'un Information kapasitesini geliştirmek | **EXPLORED / candidate decomposition** | [B2](work/B2-information-capacity.md) |
| **B3** | SOUL'un Actors kapasitesini geliştirmek | **EXPLORED / candidate decomposition** | [B3](work/B3-actors-capacity.md) |
| **B4** | SOUL'un Work kapasitesini geliştirmek | **EXPLORED / candidate decomposition** | [B4](work/B4-work-capacity.md) |
| **B5** | SOUL'un Environment kapasitesini geliştirmek | **EXPLORED / candidate decomposition** | [B5](work/B5-environment-capacity.md) |
| **B6** | Dört zemini birbirine doğru bağlayan düzeni geliştirmek | **EXPLORED / candidate decomposition** | [B6](work/B6-cross-ground-integration.md) |
| **B7** | SOUL'un işe göre çalışma sistemi kurma ve genişletme kapasitesini geliştirmek | **EXPLORED / candidate decomposition** | [B7](work/B7-system-formation.md) |
| **B8** | Süreklilik, değişim, toparlanma ve öğrenme kapasitesini geliştirmek | **CURRENT / not yet decomposed** | [B8](work/B8-continuity-change-recovery.md) |
| **B9** | Ortaya çıkan SOUL'u bütün olarak birleştirmek ve gerçek görevlerle sınamak | NOT OPENED | [B9](work/B9-integration-and-testing.md) |

## Statülerin anlamı

- **NOT OPENED:** yalnız birinci seviye Work olarak tanımlı; alt gereksinimleri henüz çıkarılmadı.
- **CURRENT:** şu anda ayrıştırılan Work.
- **EXPLORED / candidate decomposition:** alt sorumluluklar ve ilk taşıyıcı adayları çıkarıldı; nihai rol/mimari kabulü değildir.
- Daha güçlü bir “accepted/validated” statüsü, yalnız kullanıcı kararı veya uygun doğrulama sonrasında kullanılabilir.

## Current sequencing

B1 ve B2 aynı yöntemle açıldı:

1. Work'ün hedef çıktısını tanımla.
2. Development OS'un bu Work'ü yapabilmesi için gerekli kabiliyet/sorumlulukları çıkar.
3. Her sorumluluğu “kim/ne taşımalı?” diye ayır.
4. Yapay zekâ rolü, mekanik sorumluluk ve insan sınırını ayır.
5. Yeni rolleri [ACTORS](ACTORS.md) içindeki mevcut adaylarla karşılaştır; gereksiz kopya rol üretme.
6. Work ayrıntısını kendi B dosyasında, current konumu burada tut.

**Sıradaki işlem:** B8'i bu yöntemle açmak. B1–B7 ancak sonraki dallar maddi bir bağımlılık/revizyon doğurursa yeniden açılır.

## Önemli sınır

B1–B9, SOUL'un modül listesi değildir. Foundation'daki Information / Actors / Work / Environment zeminleri de dört yazılım modülü olarak varsayılmamaktadır. Bunlar Development OS'un SOUL'da geliştirmesi gereken problem/kabiliyet alanlarını takip etmek için kullanılan Work ayrımlarıdır.
