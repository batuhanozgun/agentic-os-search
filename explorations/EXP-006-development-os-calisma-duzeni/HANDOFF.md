# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **B4 — SOUL'un Work kapasitesini geliştirmek.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [B4 — aktif Work](work/B4-work-capacity.md)
5. [ACTORS](ACTORS.md)
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

B1–B3 ayrıntısını rutin cold-start'ta tam okuma. B4'te dependency doğarsa ilgili Work dosyasına in.

## Nereden geldik?

Başlangıç sorusu Development OS'ta hangi aktörlerin/rollerin bulunması gerektiğiydi. Jenerik rol listesi üretmemek için önce Development OS'un Work'ünü keşfetmeye geçildi. SOUL yeterince somut hedef değilse DevOS Work'ünün çıkarılamayacağı görüldü; EXP-001/002/004 tam okumalarıyla kapsamlı SOUL hedefi oluşturuldu ve kullanıcı bunu bu aşama için yeterince somut kabul etti.

Ardından Development OS'un SOUL üzerinde yapacağı B1–B9 birinci seviye Work haritası çıkarıldı. Rol türetim yöntemi:

> **B Work → DevOS kabiliyet/sorumlulukları → kim/ne taşır? → aday roller/mekanik sorumluluklar**

## Tamamlanan candidate ayrıştırmalar

### B1 — ortak entelektüel çalışma tabanı
R1 Ortak Çalışma Tabanı Tasarımcısı; R2 Davranış Doğrulayıcısı; R3 Davranış Teşhisçisi / Değişiklik Analisti. M1 enforcement gereksinimi.

### B2 — Information kapasitesi
R4 Information Steward; R5 Context & Retrieval Curator; R6 Information Integrity Reviewer. M2 Information persistence/retrieval/exposure. R3 cross-domain diagnosis'a genişlemeye aday.

### B3 — Actors kapasitesi
R7 Role & Actor Formation Designer; R8 Actor Qualification Reviewer; R9 Actor Governance Steward. Yeni bağımsız mekanik M açılmadı; M1 identity/role/grant enforcement'a genişledi, M2 actor/role/grant kayıtlarını destekler.

B3'ün kritik sonucu: SOUL'un Actors kapasitesi “agent spawn etmek” değildir; Work ihtiyacından rol/katılım çıkarmak, role contract kurmak, uygun bearer'ı bağlamak, competence'i ayrı doğrulamak, authority/delegation/obligation ilişkilerini korumak, active participation/lifecycle/attribution'ı yönetmektir.

## Current Work — B4

Şimdi sorulacak ana soru:

> **Development OS, SOUL'un Work kapasitesini geliştirebilmek için neyi yapabilir olmalı ve hangi sorumlulukları taşımalıdır?**

B1–B3 ile aynı yöntem uygulanacak. Foundation Work burada ana araştırma dayanaklarından biridir.

### B4'te korunacak kritik ayrımlar

- actual Work state ≠ Work hakkında yazılan bilgi;
- candidate/eligible/admitted/active/completed Work birbirine eşit değil;
- Work readiness ≠ Environment capability;
- Work admission ≠ Actor obligation/authorization;
- Work completion ≠ target achieved ≠ evidence says achieved ≠ authorized acceptance;
- plan ≠ actual Work;
- discovery/investigation/decision hazırlığı da Work olabilir;
- Work zaman içinde değişebilir, yeniden açılabilir, recovery gerektirebilir.

## Drift korumaları

- SOUL'un iç Work sistemi ile Development OS'un SOUL'u geliştirme Work'ünü karıştırma.
- B1–B9'u SOUL modülleri sayma.
- Yeni sorumluluk gördüğünde otomatik yeni agent/rol üretme.
- İş kaydı ile gerçek Work durumunu eşitleme.
- İnsan müşteriyi project manager veya teknik work coordinator yapma.
- Eski EXP/DevOS denemelerini current mimari diye ithal etme.
- B4 içine B5/B6/B8'in bütün işini çekme.

## Sonraki somut hareket

B4'ü aç:
1. hedef çıktısını tanımla;
2. gerekli DevOS kabiliyet/sorumluluklarını çıkar;
3. AI rolü / mekanik sorumluluk / insan sınırı açısından sınıflandır;
4. [ACTORS](ACTORS.md) içindeki R1–R9 ile karşılaştır;
5. yalnız gerekliyse yeni rol türet;
6. B4 dosyası + ACTORS + current STATE/HANDOFF'u material değişiklik kadar güncelle.

## Yetki sınırı

Bu çalışma Development OS'un implementasyonunu başlatmaz. Host, tool, dosya formatı veya agent topolojisi seçimi henüz yetkilendirilmiş sonuç değildir.
