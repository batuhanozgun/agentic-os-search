# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **B7 — SOUL'un işe göre çalışma sistemi kurma ve genişletme kapasitesini geliştirmek.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [B7 — aktif Work](work/B7-system-formation.md)
5. [ACTORS](ACTORS.md)
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

B1–B6 ayrıntısını rutin cold-start'ta tam okuma. B7'de ihtiyaç duyulan kapasite için ilgili B dosyasına seçici in.

## Tamamlanan candidate ayrıştırmalar

- **B1:** R1–R3; M1.
- **B2:** R4–R6; M2.
- **B3:** R7–R9; M1 actor identity/role/grant enforcement'a genişledi.
- **B4:** R10–R12; M3.
- **B5:** R13–R15; M4–M5.
- **B6:** R16 Cross-Ground Composition Designer; R17 Cross-Ground Control & Transition Steward; R18 Composition Integrity Reviewer; M6 cross-ground binding/standing/guarded-transition substrate.

B6'nın kritik sonucu: dört ground ayrı ayrı doğru olsa bile birleşik hüküm yanlış olabilir. Exact binding, composite standing/readiness, authority-control-enforcement, realized transition/effect, verification/acceptance ve invalidation ilişkileri ayrı korunmalıdır.

## Current Work — B7

Şimdi sorulacak ana soru:

> **Development OS, verilen bir amaç için gereken çalışma sistemini SOUL'un keşfedip kurabilmesini ve ihtiyaç değiştikçe genişletip yeniden yapılandırabilmesini nasıl geliştirebilmeli; bunun için hangi kabiliyet ve sorumlulukları taşımalıdır?**

B7, B1–B6'da geliştirilmiş kapasite ailelerini belirli bir iş için seçme/instantiate etme problemidir. Ancak “hepsini her zaman kur” veya “tek meta-agent karar versin” sonucu peşinen verilmez.

### B7'de korunacak başlangıç ayrımları

- Work sistemi keşfetmek ≠ sabit template uygulamak.
- gerekli kapasite ≠ ayrı agent.
- mevcut kapasiteyi reuse etmek ≠ her şeyi sıfırdan kurmak.
- system configuration ≠ system actually ready/effective.
- genişleme ≠ yalnız yeni actor eklemek; Information/Work/Environment/control yüzeyleri de birlikte değişebilir.
- system formation decision ≠ runtime implementation/effect.

## Drift korumaları

- B7'yi “SOUL kendi harness'ını yaratır” sloganıyla bitirme; hangi sorumlulukların bunu mümkün kıldığını çıkar.
- B1–B6'yı modül kataloğu gibi mechanically instantiate etme.
- gereksiz complexity üretme; mevcut kapasiteyi önce değerlendir.
- sistem kurma kararını doğrulanmış readiness/effect sanma.
- B8 continuity/learning ve B9 end-to-end test işlerini B7 içine tamamen çekme.

## Sonraki somut hareket

B7'yi aç: hedef çıktısını tanımla; system need/configuration formation sorumluluklarını çıkar; existing R1–R18/M1–M6 ile karşılaştır; yalnız sahipsiz başarı yönü varsa yeni taşıyıcı türet.

## Yetki sınırı

Bu çalışma Development OS veya SOUL implementasyonunu başlatmaz.