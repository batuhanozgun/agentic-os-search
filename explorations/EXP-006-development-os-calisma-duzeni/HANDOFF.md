# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **B5 — SOUL'un Environment kapasitesini geliştirmek.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [B5 — aktif Work](work/B5-environment-capacity.md)
5. [ACTORS](ACTORS.md)
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

B1–B4 ayrıntısını rutin cold-start'ta tam okuma. B5'te dependency doğarsa ilgili Work dosyasına in.

## Nereden geldik?

Başlangıç sorusu Development OS'ta hangi aktörlerin/rollerin bulunması gerektiğiydi. Jenerik rol listesi üretmemek için önce Development OS'un Work'ünü keşfetmeye geçildi. SOUL yeterince somut hedef değilse DevOS Work'ünün çıkarılamayacağı görüldü; EXP-001/002/004 tam okumalarıyla kapsamlı SOUL hedefi oluşturuldu ve kullanıcı bunu bu aşama için yeterince somut kabul etti.

Ardından Development OS'un SOUL üzerinde yapacağı B1–B9 birinci seviye Work haritası çıkarıldı. Rol türetim yöntemi:

> **B Work → DevOS kabiliyet/sorumlulukları → kim/ne taşır? → aday roller/mekanik sorumluluklar**

## Tamamlanan candidate ayrıştırmalar

### B1 — ortak entelektüel çalışma tabanı
R1–R3; M1 enforcement gereksinimi.

### B2 — Information kapasitesi
R4–R6; M2 Information persistence/retrieval/exposure. R3 cross-domain diagnosis'a genişlemeye aday.

### B3 — Actors kapasitesi
R7 Role & Actor Formation Designer; R8 Actor Qualification Reviewer; R9 Actor Governance Steward. M1 identity/role/grant enforcement'a genişledi.

### B4 — Work kapasitesi
R10 Work Formation & Planning Designer; R11 Work Admission & Coordination Steward; R12 Work Progress & Closure Reviewer. M3 Work identity/admission/claim/transition mekanik sorumluluğu çıktı.

B4'ün kritik sonucu: Work, task listesi + scalar status değildir. Purpose/Work/method; candidate/admitted/active; living plan/actual Work; dependency/coordination/flow; execution/verification/fitness/acceptance; bounded/continuing Work ayrımları korunmalıdır.

## Current Work — B5

Şimdi sorulacak ana soru:

> **Development OS, SOUL'un Environment kapasitesini geliştirebilmek için neyi yapabilir olmalı ve hangi sorumlulukları taşımalıdır?**

B1–B4 ile aynı yöntem uygulanacak. Foundation Environment burada ana araştırma dayanaklarından biri olacaktır.

### B5'te korunacak başlangıç ayrımları

- Actor capability ≠ actual tool/resource/access availability;
- kayıtlı capability ≠ gerçek çalışırlık;
- permission/authority ≠ credential possession/effect power;
- Work readiness ≠ Environment actionability;
- tool invocation ≠ realized external effect;
- workspace/sandbox/config tanımı ≠ gerçekten provision edilmiş çalışma ortamı.

## Drift korumaları

- Environment'ı yalnız “tools listesi”ne daraltma.
- Claude Code/Codex/Hermes gibi hazır hostları erken mimari seçime dönüştürme.
- erişim varlığını authority sayma.
- config dosyasını actual environment state sayma.
- B5 içine B6 cross-ground integration'ın bütününü çekme.
- insan müşteriyi credential/runtime operator yapmak zorunda varsayma.

## Sonraki somut hareket

B5'i aç:
1. hedef çıktısını tanımla;
2. gerekli DevOS kabiliyet/sorumluluklarını çıkar;
3. AI rolü / mekanik sorumluluk / insan sınırı açısından sınıflandır;
4. [ACTORS](ACTORS.md) içindeki R1–R12 ile karşılaştır;
5. yalnız gerekliyse yeni rol türet;
6. B5 dosyası + ACTORS + current STATE/HANDOFF'u material değişiklik kadar güncelle.

## Yetki sınırı

Bu çalışma Development OS'un implementasyonunu başlatmaz. Host/provider/tool seçimi henüz sonuç değildir.
