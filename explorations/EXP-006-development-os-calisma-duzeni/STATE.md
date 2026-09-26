# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu diyalog ve araştırma.  
**Güncelleme:** 26 Eylül 2026.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Başlangıçtan beri aranan:** DevOS yapay zekâ aktörünün gereken sorumlulukları ve rolleri.  
**Güncel aşama:** S1 rol/sorumluluk konsolidasyonu — S1-15 araştırma-family testi tamamlandı; F8 Araştırma/Keşif/Sentez ayrı aday olarak eklendi. S1'in bütünü kapanmadı.  
**Son kullanıcı yönü:** Hazırlık ve S1-14 ardından “Devam et.” — açık research-family sorusunu sınırlı olarak sınamak. Sonuç aday olarak kullanıcıya döndürülür; nihai kadro veya mimari onayı değildir.

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

Ayrıntı: [DECISIONS](DECISIONS.md). S1-15 sonucu bu kabul listesine otomatik eklenmedi.

## Current candidate S1 sonucu

1. **F1 — Tasarlama / Oluşturma**
2. **F2 — Gerçekleştirme / Uygulama**
3. **F3 — İşletim / Stewardship / Koordinasyon**
4. **F4 — Yönetişim / Yetki / Kontrol**
5. **F5 — Doğrulama / Güvence**
6. **F6 — Teşhis / Etki Analizi / Recovery Yönlendirme**
7. **F7 — Öğrenme / Adaptasyon Yönlendirme**
8. **F8 — Araştırma / Keşif / Sentez** — S1-15 ile eklenen aday.

Bunlar nihai DevOS rolleri veya fiziksel agent sayısı değildir. S1-14'te F1–F7 bütün-model denetimi yapıldı; S1-15 yalnız araştırma sınırını kaynak örnekleri ve kavramsal karşı vakalarla derinleştirdi. Bağımsız davranış doğrulaması yapılmadı.

### S1-15'in çözdüğü ayrım

Araştırma bütün familyalarda yöntem/kabiliyet olarak kullanılabilir. Esas teslimatı kaynaklı bilgi, açıklama veya sentez olan Work ise ayrı F8 görevlendirmesiyle temsil edilebilir. Her arama, context hazırlığı, önkoşul keşfi veya claim doğrulaması F8 değildir.

F1'i genişletmek veya F5'i geniş bir epistemik üst aile yapmak mantıken mümkün alternatiflerdir; mevcut başarı-yönü ayrıntı seviyesinde ayrı F8 daha açık aday olarak tercih edildi. Bu sınıflama zorunlu/optimal diye kanıtlanmadı. Araştırmacının kendi sonucu bağımsız assurance, ürün seçimi veya kalıcı adaptation değildir.

### Kalan coverage / specialization noktaları

- **F2:** İlk R1–R25 listesinde birincil gerçekleştirme/uygulama sahibi yok. Realization yalnız M1–M9 mekaniklerine indirgenmez; non-M artefaktlar da gerekebilir.
- **F3:** **Information Lifecycle Operations** açık specialization.
- **F3:** **Actor / Role Lifecycle Operations** açık specialization.
- **F8:** Ayrı bilgi teslimatını taşıyan aday familya var; ilk R-lineage değiştirilmedi, yeni R26 veya fiziksel actor atanmadı.
- Decision ayrı familya gerektirmiyor; coordination current aday modelde F3 içinde kalıyor.
- İlk R1–R25 ve M1–M9 kayıtları lineage/evidence'tır; current organization değildir.
- Effective assignment exact Work/claim/target/artifact/transition/araştırma sorusuna bağlanmalıdır. Actor binding, independence, competence, tool/context/authority ve assignment topology henüz nihai değildir.

## Current next responsibility

Repository drift cleanup, S1-14 full-model audit ve S1-15 research-family testi tamamlandı; ayrıntı [S1-15](work/S1-15-research-discovery-synthesis-family.md).

**Sıradaki mantıksal S1 işi:** F2 realization kapsamını ve F3'ün iki açık lifecycle specialization'ını mevcut sorumluluklarla netleştirmek.

Kontrol: Hangi teslimat sahipsiz; hangisi mevcut specialization ile birleşebilir; tasarlama/üretme/işletme/yetki/güvence devirleri nerede? Her açığa yeni familya veya fiziksel agent eklenmez.

**Tur sınırı:** Bu turun yetkili işi S1-15'ti. Sonraki specialization dilimi henüz yürütülmedi; kullanıcının devam yönüyle buradan ilerlenir. Research-family sorusu yeni karşı kanıt veya kullanıcı yönü yoksa baştan tekrarlanmaz.

S1 bitmeden agent sayısı, topology, host/runtime veya mimari seçimine geçilmez. Effective-assignment düzeninin ayrıntılı tasarımı da bu tur başlatılmadı.

## Authority / retrieval

Current yön: STATE → HANDOFF → WORK → ACTORS → S1 master.  
B/S1 slice dosyalarındaki eski “next” cümleleri local tarihsel kayıt olarak okunur. history/ current authority değildir.
