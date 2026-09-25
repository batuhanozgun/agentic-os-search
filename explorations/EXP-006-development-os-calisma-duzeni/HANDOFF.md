# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **B6 — Dört zemini birbirine doğru bağlayan düzeni geliştirmek.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [B6 — aktif Work](work/B6-cross-ground-integration.md)
5. [ACTORS](ACTORS.md)
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

B1–B5 ayrıntısını rutin cold-start'ta tam okuma. B6'nın belirli ilişkisi için ilgili Work dosyasına ve Foundation deferred/composition yüzeylerine seçici in.

## Tamamlanan candidate ayrıştırmalar

- **B1:** R1–R3; M1.
- **B2:** R4–R6; M2; R3 cross-domain diagnosis'a genişlemeye aday.
- **B3:** R7–R9; M1 identity/role/grant enforcement'a genişledi.
- **B4:** R10–R12; M3 Work identity/admission/transition mechanics.
- **B5:** R13 Environment & Capability Formation Designer; R14 Environment Operations & Readiness Steward; R15 Environment Reality & Effect Reviewer; M4 Environment provisioning/isolation; M5 effect execution/readback/observability.

B5'in kritik düzeltmesi: Environment yalnız technical host/tool alanı değildir. SOUL hem Work Conditions'ı hem de gerçek Domain Reality state/effect'ini gözleyebilmelidir. Tool success ≠ actual effect ≠ target outcome.

## Current Work — B6

Şimdi sorulacak ana soru:

> **Development OS, Information–Actors–Work–Environment ayrımlarını kaybetmeden bunların birlikte doğru çalışmasını SOUL'da nasıl geliştirebilmeli; bunun için hangi kabiliyet ve sorumlulukları taşımalıdır?**

B6 özellikle kullanıcının daha önce en az sezgisel bulduğu ve “buradan gol yememeliyiz” dediği alandır. Varsayımlar görünür kurulmalı; tek seferde soyut integration layer icat edilmemeli.

### B6'da korunacak başlangıç ilişkileri

- Work readiness + Actor competence/authority + Environment conditions + Information/context birlikte actionability yaratabilir; bunlardan biri tek başına yeterli değildir.
- technical effect power ≠ legitimate authority.
- Work completion ≠ Environment outcome ≠ evidence ≠ acceptance authority.
- role/grant kaydı ≠ actual standing; Environment config kaydı ≠ actual environment; Work status kaydı ≠ actual Work.
- actor assignment ≠ Work admission/execution.
- information exposure ≠ demonstrated use.
- tool invocation ≠ realized effect.
- change impact tek ground içinde kapanmayabilir.

## Drift korumaları

- Dört ground'u dört servis/modül varsayma.
- B6'yı hepsini birbirine bağlayan tek orchestrator agent diye peşinen çözme.
- ilişki semantiğini veri şemasıyla eşitleme.
- control/enforcement ile AI hükmünü aynı şey sayma.
- B6 içine B7 system-formation veya B8 continuity'nin tamamını çekme.
- müşterinin eksik teknik bilgisi nedeniyle cross-ground kararları ona geri bırakma.

## Sonraki somut hareket

B6'yı aç: load-bearing relation/control sınıflarını çıkar; her ground'un katkısını ayır; AI reasoning ile mechanical enforcement sınırını ayır; mevcut R1–R15 ve M1–M5'i yeniden kullan; yalnız gerekliyse yeni taşıyıcı türet.

## Yetki sınırı

Bu çalışma Development OS'un nihai composition architecture/data model/runtime'ını seçmez.