# EXP-006 — STATE

**Durum:** OPEN / LONG-RUNNING DIALOGUE WORK.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Current phase:** B1–B9 Work ayrıştırması tamamlandı; architecture öncesi rol/sorumluluk konsolidasyonu.  
**Current Work:** **S1 — B1–B9 sonuçlarını çapraz konsolide etmek.**  
**Next:** R1–R25 ve M1–M9'u role family / responsibility / assurance / mechanical substrate açısından normalize etmek; coverage boşluklarını bulmak; sonra Development OS yapısına geçiş kriterini değerlendirmek.

## Current çalışma modeli

```text
SOUL hedefi
  → DevOS B1–B9 Work
  → her Work için DevOS kabiliyet/sorumlulukları
  → aday AI rolleri / mekanik sorumluluklar / insan sınırı
  → S1 cross-B consolidation
  → DevOS yapısı
  → sonra mekanizma ve araç seçimleri
```

## Güncel durum

- B1–B9'un tamamı **EXPLORED / candidate decomposition**.
- R1–R25 aday AI rolleridir; 25 fiziksel agent anlamına gelmez.
- M1–M9 aday mekanik sorumluluk kümeleridir; 9 ayrı servis/modül anlamına gelmez.
- İnsan/müşteri çekirdeği **yetki + kabul** olarak korunur.
- R18 B6/B7/B9 integrated assurance için yeniden kullanılmıştır; yeni verifier her B dalında otomatik üretilmemiştir.
- B9 testing sonucu canlı SOUL doğrulaması değildir; Development OS testing capacity requirement'ıdır.
- Nihai Development OS mimarisi hâlâ seçilmedi.

## Canonical yüzeyler

- [HANDOFF](HANDOFF.md) — fresh-session devir kaydı.
- [WORK](WORK.md) — B1–B9 ve S1 current sequencing.
- [ACTORS](ACTORS.md) — R1–R25 ve M1–M9 registry'si.
- [DECISIONS](DECISIONS.md) — kullanıcıyla netleşen kararlar.
- [EXP-006_Context](EXP-006_Context) — yön ve çalışma metodolojisi.

## S1 stop condition

S1 tamamlanmış sayılabilmesi için en azından:
1. rol adayları anlamlı üst ailelerde konsolide edilmiş;
2. merge/separation gerekçeleri görünür;
3. her B1–B9 Work alanının owner/assurance/mechanical coverage'ı kontrol edilmiş;
4. insan authority/acceptance sınırları korunmuş;
5. aynı sorumluluğun duplicate owner'ları veya sahipsiz sorumluluklar belirlenmiş;
6. architecture'a geçiş için yeterli normalleştirilmiş rol/control resmi oluşmuş olmalıdır.

## Non-decisions

Henüz nihai Development OS agent sayısı, host/runtime, topology, DB/memory ürünü, toolchain veya fiziksel deployment yapısı seçilmedi.