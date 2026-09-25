# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **B3 — SOUL'un Actors kapasitesini geliştirmek.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [B3 — aktif Work](work/B3-actors-capacity.md)
5. [ACTORS](ACTORS.md)
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

B1/B2 ayrıntısını rutin cold-start'ta tam okuma. B3'te bir dependency doğarsa ilgili [B1](work/B1-common-intellectual-baseline.md) veya [B2](work/B2-information-capacity.md) dosyasına in.

## Nereden geldik?

Başlangıç sorusu Development OS'ta hangi aktörlerin/rollerin bulunması gerektiğiydi. Jenerik rol listesi üretmemek için önce Development OS'un Work'ünü keşfetmeye geçildi. SOUL yeterince somut hedef değilse DevOS Work'ünün çıkarılamayacağı görüldü; EXP-001/002/004 tam okumalarıyla kapsamlı SOUL hedefi oluşturuldu ve kullanıcı bunu bu aşama için yeterince somut kabul etti.

Ardından Development OS'un SOUL üzerinde yapacağı B1–B9 birinci seviye Work haritası çıkarıldı. Rol türetim yöntemi:

> **B Work → DevOS kabiliyet/sorumlulukları → kim/ne taşır? → aday roller/mekanik sorumluluklar**

## Tamamlanan çalışma

### B1 — ortak entelektüel çalışma tabanı

Alt sorumluluklar ve ilk taşıyıcılar çıkarıldı.

Aday roller:
- R1 Ortak Çalışma Tabanı Tasarımcısı
- R2 Davranış Doğrulayıcısı
- R3 Davranış Teşhisçisi / Değişiklik Analisti

Mekanik gereksinim:
- M1 davranış/enforcement sınırı

### B2 — Information kapasitesi

Alt sorumluluklar ve ilk taşıyıcılar çıkarıldı.

Aday roller:
- R4 Information Steward
- R5 Context & Retrieval Curator
- R6 Information Integrity Reviewer

Mekanik gereksinim:
- M2 Information persistence/retrieval/exposure

R3, B2 failure diagnosis için de genişlemeye adaydır; yeni kopya teşhis rolü açılmadı.

## Current Work — B3

Şimdi sorulacak ana soru:

> **Development OS, SOUL'un Actors kapasitesini geliştirebilmek için neyi yapabilir olmalı ve hangi sorumlulukları taşımalıdır?**

B1/B2 ile aynı yöntem uygulanacak. Foundation Actors burada ana araştırma dayanaklarından biridir.

### B3'te korunacak kritik ayrımlar

- actor ≠ role;
- identity/bearer ≠ role/position ≠ participation;
- capability/competence ≠ permission/authority ≠ obligation;
- performer ≠ decider ≠ authorizer ≠ principal/representative ≠ accountable party;
- actor capability ≠ Environment access/actionability;
- Work admission/requiredness ≠ Actor obligation/authorization;
- Work acceptance state ≠ authority to accept.

## Drift korumaları

- SOUL'un iç rollerini tasarlamak ile Development OS rollerini türetmeyi karıştırma.
- B1–B9'u SOUL modülleri sayma.
- Yeni sorumluluk gördüğünde otomatik yeni agent/rol üretme.
- Mekanik enforcement ile AI muhakemesini aynı şey sayma.
- İnsan müşteriyi gizli teknik koordinatöre dönüştürme.
- Eski EXP/DevOS denemelerini current mimari diye ithal etme.
- Bir B dalına inerken diğer B dallarının bütün işini içine çekme.

## Sonraki somut hareket

B3'ü aç:
1. hedef çıktısını tanımla;
2. gerekli DevOS kabiliyet/sorumluluklarını çıkar;
3. AI rolü / mekanik sorumluluk / insan sınırı açısından sınıflandır;
4. [ACTORS](ACTORS.md) içindeki R1–R6 ile karşılaştır;
5. yalnız gerekliyse yeni rol türet;
6. B3 dosyası + ACTORS + current STATE/HANDOFF'u material değişiklik kadar güncelle.

## Yetki sınırı

Bu çalışma Development OS'un implementasyonunu başlatmaz. Host, tool, dosya formatı veya agent topolojisi seçimi henüz yetkilendirilmiş sonuç değildir.
