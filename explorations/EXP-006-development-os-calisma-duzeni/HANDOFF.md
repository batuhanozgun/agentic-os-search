# EXP-006 — HANDOFF

**Amaç:** Fresh session'da önceki konuşmayı görmeden doğru çalışma noktasını devralmak.  
**Güncel tarih:** 25 Eylül 2026.  
**Current Work:** **S1 — B1–B9 rol/sorumluluk konsolidasyonu.**

## Cold-start

Normal devam için sırayla oku:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [ACTORS](ACTORS.md)
5. S1 sırasında yalnız gerekli B dosyalarına [work/](work/) üzerinden in
6. gerekiyorsa [DECISIONS](DECISIONS.md)
7. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

## Tamamlanan ana Work

B1–B9'un tamamı candidate decomposition seviyesinde açıldı. Sonuçlar:

- **B1 Intellectual baseline:** R1–R3; M1.
- **B2 Information:** R4–R6; M2.
- **B3 Actors:** R7–R9; M1 genişledi.
- **B4 Work:** R10–R12; M3.
- **B5 Environment:** R13–R15; M4–M5.
- **B6 Cross-ground integration:** R16–R18; M6.
- **B7 System formation:** R19–R20; M7; R18 joint-fit assurance için reused.
- **B8 Continuity/recovery/learning:** R21–R23; M8; existing verifiers reused.
- **B9 Integration/testing:** R24–R25; M9; R18 integrated verdict assurance için reused.

## B9'un kritik sonucu

SOUL testing component presence veya tek başarılı demo değildir. Capability claims exact/falsifiable olmalı; scenario portfolio failure-surface coverage taşımalı; hidden-requirement leakage önlenmeli; negative/mutation/change/recovery/adaptation tests bulunmalı; oracle/independence/error-sensitivity sınanmalı; exact target/version/environment bağlanmalı; generality claim'i tested scope ile sınırlanmalı; failed evaluation R3 ile ilgili B dalını reopen etmelidir.

## Current Work — S1

Şimdi yeni Work dalı açmak yerine B1–B9 boyunca türetilmiş adayları **normalize et**.

Temel soru:

> **Development OS'un gerçekten kaç farklı sorumluluk/rol ailesine ihtiyacı var; R1–R25'in hangileri aynı üst rolün farklı kipleri, hangileri epistemik veya yönetişim gerekçesiyle ayrı kalmalı; M1–M9 hangi gerçek substrate ailelerine sıkışıyor?**

### S1 ilk görevleri

1. R1–R25'i başarı yönüne göre cluster et; isim benzerliğine göre değil.
2. Designer / Steward / Reviewer / Diagnosis / Formation ayrımlarının hangileri substantive separation gerektiriyor test et.
3. Verification rollerini claim family ve independence ihtiyacına göre konsolide et.
4. R3'ün cross-domain diagnosis scope'unu netleştir.
5. R19/R20 system-formation'ın capability-owner rollerle ilişkisini normalize et.
6. M1–M9'u enforcement/state/runtime/effect/evaluation gibi substrate ailelerinde birleştirme olasılığını test et.
7. B1–B9 coverage matrix çıkar; orphan ve duplicate responsibility ara.
8. Sonuç yeterliyse ancak ondan sonra DevOS structure/topology tartışmasına geç.

## Drift korumaları

- 25 rol = 25 agent deme.
- aynı isimli işler = aynı rol deme; başarı yönünü karşılaştır.
- farklı isim = farklı actor gerek demek değil.
- verifier'ları sırf sayıyı azaltmak için birleştirip independence'i yok etme.
- architecture/topology/tool seçimine S1 tamamlanmadan atlama.
- kullanıcıyı eksik role-merge kararlarının teknik oracle'ı yapma.

## Yetki sınırı

S1 architecture öncesi consolidation'dır; implementasyon veya host/tool seçimi değildir.