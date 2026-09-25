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
5. [S1 çalışma dosyası](work/S1-role-responsibility-consolidation.md)
6. S1 sırasında yalnız gerekli B dosyalarına [work/](work/) üzerinden in
7. gerekiyorsa [DECISIONS](DECISIONS.md)
8. yön/metodoloji drift'i şüphesinde [EXP-006_Context](EXP-006_Context)

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

### Son yönlendirme — araştırmaları S1'e kat

Kullanıcı, studies araştırmalarının bu rollerin uğraşacağı yapılar hakkında bilgi sağlayacağını ve S1'de kullanılmasını istedi. Bu, örneklerin rol adlarını kopyalamak veya hepsini bir sisteme toplamak değildir.

[S1 dosyası](work/S1-role-responsibility-consolidation.md) ilk kaynak rotalarını, gerçek okuma kapsamını ve kaynak–çıkarım sınırlarını taşır. Bu hazırlık turunda rol adayları değiştirilmedi; S1 sonucu veya canlı doğrulama elde edilmedi.

İlk önerilen inceleme dilimi **üretim–inceleme–düzeltme sorumluluklarıdır**. Superpowers'ın ilgili kaynaklarına, ardından gerekliyse gstack karşılaştırmasına in; ilgili B tanımlarıyla aynı analiz düzeyinde karşılaştır. Her kümede yalnız birleşme/ayrılma değil, rolün ihtiyaç duyduğu bilgi, yöntem, erişim ve mekanik destek de görünür olsun.

Örnek sistemin işi yürütmesi ile Development OS'un o kapasiteyi SOUL için geliştirmesini ayır. M1–M9'un varlığı bunları üretecek ve sınayacak teknik sorumlulukları kendiliğinden karşılamaz; bu sınırı da S1'de kontrol et.

### S1 görevleri

1. İlgili araştırmayı önce kendi bağlamı ve kanıt sınırıyla oku; sorgulanan DevOS sorumluluğuna katkısını belirt.
2. R1–R25'i başarı yönüne göre cluster et; isim benzerliğine göre değil.
3. Designer / Steward / Reviewer / Diagnosis / Formation ayrımlarının hangileri substantive separation gerektiriyor test et.
4. Verification rollerini claim family ve independence ihtiyacına göre konsolide et.
5. R3'ün cross-domain diagnosis scope'unu netleştir.
6. R19/R20 system-formation'ın capability-owner rollerle ilişkisini normalize et.
7. M1–M9'u enforcement/state/runtime/effect/evaluation gibi substrate ailelerinde birleştirme olasılığını ve geliştirme sorumlularını test et.
8. B1–B9 coverage matrix çıkar; orphan ve duplicate responsibility ara.
9. Sonuç yeterliyse ancak ondan sonra DevOS structure/topology tartışmasına geç.

## Drift korumaları

- 25 rol = 25 agent deme.
- aynı isimli işler = aynı rol deme; başarı yönünü karşılaştır.
- farklı isim = farklı actor gerek demek değil.
- verifier'ları sırf sayıyı azaltmak için birleştirip independence'i yok etme.
- Araştırmaları mevcut 25 adayı yalnız doğrulamak için kullanma; karşı örnek ve eksikleri de koru.
- Tamamlanmış bulgu, kısmi araştırma ve yalnız araştırma sırasına alınmış aday birbirinden farklıdır.
- architecture/topology/tool seçimine S1 tamamlanmadan atlama.
- kullanıcıyı eksik role-merge kararlarının teknik oracle'ı yapma.

## Yetki sınırı

S1 architecture öncesi consolidation'dır; implementasyon veya host/tool seçimi değildir. Yeni dış ürün araştırması, kurulum veya bütün studies'i baştan okuma bu hazırlıkla otomatik başlamaz.