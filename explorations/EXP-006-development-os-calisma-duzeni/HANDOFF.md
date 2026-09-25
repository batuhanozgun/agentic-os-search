# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **B8 — Süreklilik, değişim, toparlanma ve öğrenme kapasitesini geliştirmek.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [B8 — aktif Work](work/B8-continuity-change-recovery.md)
5. [ACTORS](ACTORS.md)
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

B1–B7 ayrıntısını rutin cold-start'ta tam okuma. B8'de dependency doğarsa ilgili Work dosyasına seçici in.

## Tamamlanan candidate ayrıştırmalar

- **B1:** R1–R3; M1.
- **B2:** R4–R6; M2.
- **B3:** R7–R9; M1 actor identity/role/grant enforcement'a genişledi.
- **B4:** R10–R12; M3.
- **B5:** R13–R15; M4–M5.
- **B6:** R16–R18; M6.
- **B7:** R19 Working System Formation Designer; R20 Working Configuration Assembly Steward; M7 Working Configuration binding/activation/lifecycle substrate. B7 için ayrı verifier açılmadı; R18 configuration joint-readiness/fit qualification'ına yeniden kullanıldı.

B7'nin kritik sonucu: SOUL işe göre büyürken her ihtiyaçta sıfırdan sistem veya yeni agent kurmaz. Gerekli capacity set'ini keşfeder; mevcut kapasiteyi reuse/configure/acquire/create/defer seçenekleriyle değerlendirir; birlikte uygulanabilir Working Configuration kurar; yeni işlev geldiğinde existing context/control/verification/recovery kapsamını da yeniden değerlendirir; gereksiz complexity'yi sınırlayıp kullanılmayan parçaları retire edebilir.

## Current Work — B8

Şimdi sorulacak ana soru:

> **Development OS, SOUL'un oturum/actor kaybında Work'ü kaybetmemesini, değişikliklerin etkisini doğru taşımasını, belirsiz/partial effect durumlarından toparlanmasını ve deneyimden yanlış genelleme yapmadan öğrenmesini nasıl geliştirebilmeli?**

### B8'de korunacak başlangıç ayrımları

- persistence ≠ currentness ≠ correctness.
- session continuity ≠ Work continuity.
- record exists ≠ next actor can find/use it.
- retry ≠ no prior effect occurred.
- rollback ≠ time reversal; compensation ≠ literal reversal.
- dependency changed ≠ all dependent conclusions false; re-evaluation may be needed.
- stored lesson ≠ learned/operative behavior.
- one successful repair ≠ generally reusable method.
- actor replacement can preserve Work/system continuity if required state/bindings survive.

## Drift korumaları

- B8'i yalnız memory/database problemi yapma.
- recovery'yi yalnız retry veya restore-from-backup diye daraltma.
- öğrenmeyi reflection dosyası yazmakla eşitleme.
- her change'de bütün sistemi yeniden başlatma veya tam tersine eski sonuçları frozen kabul etme.
- B9 end-to-end SOUL testini B8 içine çekme.

## Sonraki somut hareket

B8'i aç: continuity carriers, invalidation/change impact, recovery/reconciliation ve experience→persistent adaptation sorumluluklarını çıkar; existing R1–R20/M1–M7 ile karşılaştır; yalnız sahipsiz başarı yönü varsa yeni taşıyıcı türet.

## Yetki sınırı

Bu çalışma Development OS veya SOUL implementasyonunu başlatmaz.