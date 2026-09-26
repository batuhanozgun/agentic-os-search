# EXP-006 — HANDOFF

**Amaç:** Yeni oturumun EXP-006'yı son alt örnekten değil, current üst iş ve doğru dönüş noktasından devralması.  
**Güncelleme:** 26 Eylül 2026.  
**Güncel iş:** S1 — Development OS rol/sorumluluk konsolidasyonu.  
**Son tamamlanan dilim:** [S1-15](work/S1-15-research-discovery-synthesis-family.md), araştırma-family sınaması.  
**Sıradaki mantıksal iş:** F2 realization kapsamı ve F3'ün iki açık lifecycle specialization'ını netleştirmek. Bu dilim henüz yürütülmedi.

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

S1-01–S1-04:
- production/review/correction ayrımlarını açtı;
- fiilî gerçekleştirme/implementation sorumluluğunun görünmediğini buldu;
- actor-conditioned role purpose, activation ve knowledge transfer koşullarını ekledi.

S1-05–S1-13:
- yedi başarı-yönü familyası adayı çıkardı ve her birini ayrı ayrı sınadı;
- F2 gerçekleştirme coverage açığını doğruladı;
- F3 Information Lifecycle Operations specialization açığını buldu;
- R4'ü ağırlıklı F1 design tarafına çekti;
- R22'yi F6 recovery-routing olarak netleştirdi;
- human mandate source ile AI F4 governance'i ayırdı.

S1-14:
- B1–B9'u F1–F7'ye karşı yeniden projekte etti; hard duplicate familya bulmadığını kaydetti;
- F3 içinde **Actor / Role Lifecycle Operations** specialization açığını ekledi;
- decision'ı ayrı familya yapmadı; coordination'ı F3 içinde tuttu;
- research'ün esas teslimat olabileceğini göstererek family sınırını yeniden açtı;
- effective assignment'ın exact Work/claim/target/artifact/transition object'ine bağlanması gerektiğini belirginleştirdi.

S1-15:
- araştırmanın **ortak yöntem olması** ile **ayrı bilgi teslimatı taşıması**nın birbirini dışlamadığını belirledi;
- F1 specialization ve genişletilmiş F5 alternatiflerini değerlendirerek **F8 Araştırma/Keşif/Sentez** adayını ekledi;
- her retrieval, önkoşul keşfi, inceleme veya deneyi F8'e taşımadı;
- araştırmacı bulgusu, bağımsız assurance, tasarım/adoption ve adaptation ayrımlarını korudu;
- araştırmanın gerekçeli yeni belirsizlik ortaya çıkarabileceğini, yalnız kesinlik artışıyla ölçülmemesi gerektiğini belirtti.

Bunlar nitel kaynak karşılaştırması ve kavramsal sonuçlardır; bağımsız davranış doğrulaması veya sekiz familyanın optimal olduğunun kanıtı değildir.

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

- F2'nin initial R1–R25 içinde primary owner'ı yok; specialization kapsamı yalnız M1–M9'a indirgenmemeli.
- F3 Information Lifecycle Operations açık specialization.
- F3 Actor / Role Lifecycle Operations açık specialization.
- F8'in ayrı bilgi teslimatı tanımı var; gerçek yeterlilik, tetiklenme/devir ve assignment düzeni kurulmuş veya sınanmış değil.
- R1–R25'ten familyalara geçiş kullanıcıca nihai DevOS kadrosu olarak kabul edilmedi.
- Agent sayısı, model seçimi, topology, host/runtime, physical module/service yapısı açık.

Research-family sorusu S1-15 kapsamında cevaplandı; yeni karşı kanıt veya kullanıcı yönü olmadan baştan aynı familya araştırmasını yapma. S1 bütünü ise specialization ve devir açıklıkları varken kapanmış sayılmaz.

## 6. Sıradaki bounded iş ve yetki sınırı

Kullanıcının sonraki devam yönünde:

1. F2'nin hangi gerçek üretim/uyarlama teslimlerini taşıdığını, mekanik ve non-M çıktıları birlikte ele alarak netleştir.
2. F3 Information Lifecycle Operations'ın R5 context/retrieval ve diğer lifecycle işleriyle sınırını karşılaştır.
3. F3 Actor / Role Lifecycle Operations'ın R7 design, R9 governance, R20 assembly ve R21 continuity ile sınırını karşılaştır.
4. Normal işletim, değişiklik ve devirde sahipsiz veya duplicate teslimat kalıp kalmadığını incele. Birleştir/ayır/açık bırak kararını gerekçelendir; yeni isim üretmeyi başarı sayma.

Bu iş aynı S1 konsolidasyonunun devamıdır. Tam effective-assignment düzeni veya mimari değildir. S1-15 turu yalnız araştırma sorusunu çözüp sonucu kaydetti; bu sonraki dilimi fiilen başlatmadı.

S1 bitmeden mimari, agent topolojisi, host/runtime veya physical implementation seçme.
