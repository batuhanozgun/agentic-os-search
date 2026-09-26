# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu diyalog ve araştırma.  
**Güncelleme:** 26 Eylül 2026.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Başlangıçtan beri aranan:** DevOS yapay zekâ aktörünün gereken sorumlulukları ve rolleri.  
**Güncel aşama:** S1 rol/sorumluluk konsolidasyonu — F1–F7 ayrı ayrı sınandı; S1-14 bütün-model coverage/overlap denetimi tamamlandı. F1–F7 reddedilmedi, fakat research/discovery success-direction sınırı açık.  
**Son kullanıcı yönü:** EXP-006 yapısını drift açısından denetle ve temizle. Yapısal audit tamamlandı; current authority ve historical sınırlar yeniden düzenlendi.

## Ana zincir

SOUL'u yaratma amacı → DevOS → insan + yapay zekâ → müşteride yetki + kabul → AI rollerini bulmak için Work'ü keşfetmek → SOUL hedefini yeterince somutlaştırmak → B1–B9 geliştirme işleri → R1–R25/M1–M9 ilk adayları → S1 konsolidasyonu → daha sonra DevOS yapısı.

İlk altı kök iş korunur: hedefi belirleme; gerekli işi keşfetme; yapılabilir kılma; gerçekleştirme; sınama/yeniden çalışma; zaman içinde sürdürme. B1–B9 bunların yerine geçen sıra değildir.

## Kabul edilmiş çalışma anlaşmaları

- İki geniş aktör sınıfı: insan + yapay zekâ.
- İnsan/müşteri çekirdeği: **yetki + kabul**.
- Teknik keşif/koordinasyon varsayılan olarak müşteriye bırakılmaz.
- Roller Work ve sorumluluklardan türetilir.
- SOUL hedefi bu aşama için yeterince somut kabul edildi.
- B1–B9 current çalışma haritasıdır; nihai taxonomy değildir.
- EXP-006 cevapları kısa ve doğrudan ana hattı göstermelidir.

Ayrıntı: [DECISIONS](DECISIONS.md).

## Current candidate S1 sonucu

Ayrı ayrı sınanan role-family adayları:

1. **F1 — Tasarlama / Oluşturma**
2. **F2 — Gerçekleştirme / Uygulama**
3. **F3 — İşletim / Stewardship / Koordinasyon**
4. **F4 — Yönetişim / Yetki / Kontrol**
5. **F5 — Doğrulama / Güvence**
6. **F6 — Teşhis / Etki Analizi / Recovery Yönlendirme**
7. **F7 — Öğrenme / Adaptasyon Yönlendirme**

Bunlar nihai DevOS rolleri veya fiziksel agent sayısı değildir.

### Açık coverage noktaları

S1-14 sonucu:
- **F2:** İlk R1–R25 listesinde birincil gerçekleştirme/uygulama sahibi yok.
- **F3:** **Information Lifecycle Operations** açık specialization.
- **F3:** **Actor / Role Lifecycle Operations** yeni açık specialization.
- **Research / Discovery / Synthesis:** bazı Work'lerde primary deliverable olabildiği için yalnız cross-family yöntem sayılması artık yeterince güvenli değil; ayrı familya gereksinimi henüz sınanmadı.
- Decision ayrı familya gerektirmiyor; coordination current evidence altında F3 içinde kalabiliyor.
- İlk R1–R25 ve M1–M9 kayıtları lineage/evidence'tır; current organization değildir.
- Effective assignment modeli exact Work/claim/target/artifact/transition object'ine bağlanmalıdır; actor binding, independence, competence, tool/context/authority ve assignment topology henüz nihai değildir.

## Current next responsibility

Repository drift cleanup ve S1-14 full-model audit tamamlandı.

> **Research / Discovery / Synthesis success direction'ını bounded testte sınamak.**

Rival seçenekler:
1. yalnız cross-family method/capability;
2. F1 içinde specialization;
3. ayrı candidate family (`F8?`).

Test ayrıca research deliverable ile F1 design, F5 assurance ve F6 investigation arasındaki sınırı açmalıdır.

Bu soru çözülmeden effective-assignment düzenine geçilmez. S1 bitmeden agent sayısı, topology, host/runtime veya mimari seçimine geçilmez.

## Authority / retrieval

Current yön: STATE → HANDOFF → WORK → ACTORS → S1 master.  
B/S1 slice dosyalarındaki eski "next" cümleleri local tarihsel kayıt olarak okunur. history/ current authority değildir.
