# EXP-006 — HANDOFF

**Amaç:** Yeni oturumun EXP-006'yı son alt örnekten değil, current üst iş ve doğru dönüş noktasından devralması.  
**Güncelleme:** 26 Eylül 2026.  
**Güncel iş:** S1 — Development OS rol/sorumluluk konsolidasyonu.  
**Son tamamlanan dilim:** [S1-16](work/S1-16-realization-and-lifecycle-specializations.md), F2 realization ve F3 lifecycle specialization sınaması.  
**Sıradaki mantıksal iş:** F1–F8 + specialization + handoff modelinin final S1 consolidation/closure audit'i.

## 1. Fresh-session okuma

Sıra:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [ACTORS](ACTORS.md)
5. [S1 master](work/S1-role-responsibility-consolidation.md)
6. yalnız current sorunun gerektirdiği B veya S1 slice'ı

S1-15 araştırma sınırının ayrıntısıdır; sıradaki specialization işi için S1-09/S1-10/S1-14 ve ilgili B sorumluluklarına gerektiğinde dön. history/ ve eski S1/B “next step” cümleleri current sequencing authority değildir.

## 2. Neden buradayız?

SOUL'u yaratmak için DevOS çalışma düzenini arıyoruz. İnsan + AI geniş aktör sınıflarıyla başladık. İnsanın müşteri çekirdeğini **yetki + kabul** olarak tuttuk. AI rolleri jenerik unvanlardan çıkarılmasın diye önce DevOS Work'ünü; bunu anlamak için de SOUL hedefini yeterince somutlaştırdık.

B1–B9 DevOS'un SOUL üzerinde yapacağı ilk geliştirme Work alanlarını verdi. Bunlardan R1–R25 AI rol adayları ve M1–M9 mekanik sorumluluk adayları türedi. S1 şimdi bu ilk adayları konsolide ediyor. DevOS'un araştırma sorumluluğu, Research reposunun mevcut düzeni veya SOUL'un gelecekteki müşteri araştırmasıyla özdeş değil.

## 3. S1'de bugüne kadar ne değişti?

İlk R1–R25 listesi current organizasyon değildir.

S1-01–S1-04 production/review/correction, realization açığı, actor-conditioned role purpose ve transfer koşullarını açtı.

S1-05–S1-13 yedi başarı-yönü familyasını çıkarıp ayrı ayrı sınadı; F2 coverage açığını ve F3 Information Lifecycle Operations açığını görünür kıldı.

S1-14 bütün modeli B1–B9'a karşı denetledi; Actor / Role Lifecycle Operations açığını ekledi, decision'ı ayrı familya yapmadı, coordination'ı F3 içinde tuttu ve research-family sorusunu yeniden açtı.

S1-15 research'ün ortak yöntem olması ile ayrı bilgi teslimatı taşımasını ayırdı; **F8 Araştırma/Keşif/Sentez** adayını ekledi.

S1-16:
- F2 realization specialization'ını M1–M9'a bire bir bağlamadı; exact realization object + domain competence ile koşullandırdı;
- Information Lifecycle Operations'ı R5 context/retrieval'dan ayrı F3 specialization olarak korudu;
- Actor / Role Lifecycle Operations'ı **Actor / Role Participation Lifecycle Operations** diye daraltıp binding/activation/reassignment/retirement state'ine bağladı;
- bu specialization'ı R7 design, R9 governance, R20 configuration assembly ve R21 continuity'den ayırdı;
- yeni familya, R numarası veya fiziksel actor üretmedi.

Bunlar nitel kaynak karşılaştırması ve kavramsal sonuçlardır; bağımsız davranış doğrulaması veya family modelinin optimal olduğunun kanıtı değildir.

## 4. Current candidate family modeli

| Family | Başarı yönü |
|---|---|
| F1 Tasarlama/Oluşturma | ihtiyacı uygulanabilir ve sınanabilir tasarıma dönüştürmek |
| F2 Gerçekleştirme/Uygulama | tasarımı gerçek artefakt/mekanizmaya dönüştürmek |
| F3 İşletim/Stewardship/Koordinasyon | aktif Work/system/capability'yi doğru durumda yürütmek |
| F4 Yönetişim/Yetki/Kontrol | mandate, delegation ve governed-effect sınırlarını korumak |
| F5 Doğrulama/Güvence | claim için kanıtın gerçekten neyi desteklediğini hükmetmek |
| F6 Teşhis/Etki Analizi/Recovery Yönlendirme | failure/change sonrası doğru neden, etki ve geri dönüş yolunu bulmak |
| F7 Öğrenme/Adaptasyon Yönlendirme | experience'in reusable change'e yükseltilip yükseltilmeyeceğini yönetmek |
| F8 Araştırma/Keşif/Sentez | yetkili bilgi sorusunu kaynak/gözlemle aydınlatıp desteklenen bulgu, sınır ve açık soruları teslim etmek |

Aynı familya = aynı agent veya aynı prompt değildir. Familya ortak success direction; specialization alan/yöntem/claim farkı; effective assignment ise exact nesne ve somut actor + context + tools + authority + trigger/handoff düzeyidir.

F8, “bütün aramaları araştırmacıya gönder” kuralı değildir. Birleşik epistemik aile alternatifi mantıken mümkün kalır; current tercih ayrı F8'dir. Bu bir kullanıcıca kabul edilmiş nihai kadro değildir.

## 5. Current açıklar

- F2 specialization mantığı net: exact realization object + domain competence; initial R-lineage'da primary F2 owner yokluğu tarihsel lineage açığı olarak kalıyor.
- F3 Information Lifecycle Operations ayrı specialization olarak netleşti.
- F3 Actor / Role Participation Lifecycle Operations ayrı specialization olarak netleşti.
- F8'in ayrı bilgi teslimatı tanımı var; gerçek effective-assignment düzeni kurulmuş veya sınanmış değil.
- R1–R25'ten familyalara geçiş kullanıcıca nihai DevOS kadrosu olarak kabul edilmedi.
- Agent sayısı, model seçimi, topology, host/runtime, physical module/service yapısı açık.

Research-family ve lifecycle-specialization soruları, yeni karşı kanıt yoksa baştan açılmaz. S1 bütünü final consolidation/closure audit yapılmadan kapanmış sayılmaz.

## 6. Sıradaki bounded iş ve yetki sınırı

Kullanıcının sonraki devam yönünde **final S1 consolidation/closure audit** yap:

1. F1–F8 ve current specialization'ları B1–B9 responsibility/deliverable'larına son kez projekte et.
2. Yalnız sahipsiz exact teslimat, belirsiz primary ownership veya gerçek success-direction çakışması varsa S1'i yeniden aç.
3. R1–R25/M1–M9 lineage'ının current model sanılmasını önle; historical evidence olarak doğru bağla.
4. Kalan soruların S1 family/specialization problemi mi, yoksa sonraki effective-assignment/topology problemi mi olduğunu ayır.
5. S1 closure-ready ise sonucu kullanıcıya döndür; adjoining effective-assignment aşamasını otomatik başlatma.

Bu iş aynı S1 konsolidasyonunun son denetimidir. Mimari, agent topolojisi, host/runtime veya physical implementation değildir.

