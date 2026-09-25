# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **B9 — Ortaya çıkan SOUL'u bütün olarak birleştirmek ve gerçek görevlerle sınamak.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [B9 — aktif Work](work/B9-integration-and-testing.md)
5. [ACTORS](ACTORS.md)
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

B1–B8 ayrıntısını rutin cold-start'ta tam okuma. B9 test kapsamı bir kapasiteyi açarsa ilgili B dosyasına seçici in.

## Tamamlanan candidate ayrıştırmalar

- **B1:** R1–R3; M1.
- **B2:** R4–R6; M2.
- **B3:** R7–R9; M1 genişledi.
- **B4:** R10–R12; M3.
- **B5:** R13–R15; M4–M5.
- **B6:** R16–R18; M6.
- **B7:** R19–R20; M7; R18 configuration joint-fit için yeniden kullanıldı.
- **B8:** R21 Continuity & Re-entry Steward; R22 Change Impact & Recovery Steward; R23 Learning & Adaptation Steward; M8 durable continuity/re-entry/recovery substrate. Ayrı learning verifier açılmadı; R2/R6/R18 uygun claim seviyelerinde yeniden kullanılır.

B8'in kritik sonucu: continuity yalnız persistence değildir. Fresh actor'un current Work/authority/configuration/evidence ile gerçekten yeniden runnable hale gelmesi; change impact'in selective invalidation üretmesi; unknown effect öncesi reconciliation yapılması; recovery sonrası requalification; ve experience'in acquisition→retention→expression ile davranışa gerçekten yansıması gerekir.

## Current Work — B9

Şimdi sorulacak ana soru:

> **Development OS, B1–B8'de geliştirilen SOUL kapasitelerinin tek tek varlığını değil, gerçek görevlerde birlikte doğru çalışarak SOUL hedefini gerçekten karşılayıp karşılamadığını nasıl sınayabilmeli?**

### B9'da korunacak başlangıç ayrımları

- architecture completeness ≠ behavioral efficacy.
- component test ≠ integrated SOUL capability.
- same-model self-review ≠ independent verification.
- one successful task ≠ generality.
- benchmark success ≠ real-world effect/acceptance.
- end-to-end success ≠ doğru failure/recovery davranışı.
- test prompt'u hidden requirement'i öğretmemeli.
- test environment/target/version/evidence exact olmalı.

## Drift korumaları

- B9'u yalnız test suite listesi yapma.
- “SOUL nedir?” kriterini test sonunda sessizce değiştirme.
- yalnız happy-path task kullanma; failure/change/continuity/control yollarını da sınama.
- tek domain başarısını general-purpose yeterlik sayma.
- verifier sayısını bağımsızlık sanma.
- müşteriyi teknik test oracle'ı yapmak zorunda bırakma.

## Sonraki somut hareket

B9'u aç: test claims/coverage axes, scenario selection, oracle/evidence, independence, negative/change/recovery tests ve acceptance sınırlarını çıkar; mevcut R1–R23/M1–M8 ile karşılaştır; yalnız sahipsiz başarı yönü varsa yeni taşıyıcı türet.

## Yetki sınırı

Bu çalışma canlı SOUL testini başlatmaz; Development OS'un hangi testing capacity'yi geliştirmesi gerektiğini keşfeder.