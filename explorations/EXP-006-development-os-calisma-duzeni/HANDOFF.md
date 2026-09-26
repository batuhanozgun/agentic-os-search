# EXP-006 — HANDOFF

**Amaç:** Yeni oturumun EXP-006'yı son alt örnekten değil, current üst iş ve doğru dönüş noktasından devralması.  
**Güncelleme:** 26 Eylül 2026.  
**Güncel iş:** S1 — Development OS rol/sorumluluk konsolidasyonu.  
**Son tamamlanan dilim:** [S1-14](work/S1-14-full-model-coverage-overlap-audit.md), F1–F7 bütün-model coverage/overlap denetimi.  
**Sıradaki iş:** Research / Discovery / Synthesis success direction'ını bounded family testinde sınamak.

## 1. Fresh-session okuma

Sıra:

1. [STATE](STATE.md)
2. bu dosya
3. [WORK](WORK.md)
4. [ACTORS](ACTORS.md)
5. [S1 master](work/S1-role-responsibility-consolidation.md)
6. yalnız current sorunun gerektirdiği B veya S1 slice'ı

history/ ve eski S1/B "next step" cümleleri current sequencing authority değildir.

## 2. Neden buradayız?

SOUL'u yaratmak için DevOS çalışma düzenini arıyoruz. İnsan + AI geniş aktör sınıflarıyla başladık. İnsanın müşteri çekirdeğini **yetki + kabul** olarak tuttuk. AI rolleri jenerik unvanlardan çıkarılmasın diye önce DevOS Work'ünü; bunu anlamak için de SOUL hedefini yeterince somutlaştırdık.

B1–B9 DevOS'un SOUL üzerinde yapacağı ilk geliştirme Work alanlarını verdi. Bunlardan R1–R25 AI rol adayları ve M1–M9 mekanik sorumluluk adayları türedi. S1 şimdi bu ilk adayları konsolide ediyor.

## 3. S1'de bugüne kadar ne değişti?

İlk R1–R25 listesi current organizasyon değildir.

S1-01–S1-04:
- production/review/correction ayrımlarını açtı;
- fiilî gerçekleştirme/implementation sorumluluğunun görünmediğini buldu;
- actor-conditioned role purpose, activation ve knowledge transfer koşullarını ekledi.

S1-05–S1-13:
- yedi başarı-yönü familyası adayı çıkardı;
- her familyayı ayrı ayrı sınadı;
- F2 gerçekleştirme coverage açığını doğruladı;
- F3 Information Lifecycle Operations specialization açığını buldu;
- R4'ü ağırlıklı F1 design tarafına çekti;
- R22'yi F6 recovery-routing olarak netleştirdi;
- human mandate source ile AI F4 governance'i ayırdı.

S1-14:
- B1–B9'u F1–F7'ye karşı yeniden projekte etti;
- hard duplicate familya bulmadı;
- F3 içinde **Actor / Role Lifecycle Operations** specialization açığını ekledi;
- decision'ı ayrı familya yapmadı;
- coordination'ı F3 operational success direction içinde tuttu;
- research'ün bazı Work'lerde primary deliverable olabileceğini göstererek family sınırını yeniden açtı;
- effective assignment'ın exact Work/claim/target/artifact/transition object'ine bağlanması gerektiğini belirginleştirdi.

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

Aynı familya = aynı agent veya aynı prompt değildir. Familya ortak success direction; specialization domain/claim; effective assignment ise somut actor + context + tools + authority + trigger/handoff düzeyidir.

## 5. Current açıklar

- F2'nin initial R1–R25 içinde primary owner'ı yok.
- F3 Information Lifecycle Operations açık specialization.
- F3 Actor / Role Lifecycle Operations yeni açık specialization.
- Research / Discovery / Synthesis: method vs F1 specialization vs ayrı candidate family unresolved.
- R1–R25'ten familyalara geçiş henüz kullanıcıca nihai DevOS kadrosu olarak kabul edilmedi.
- Full B1–B9 audit yapıldı; hard duplicate familya bulunmadı, fakat research sınırı kapanmadan family consolidation closure-ready değil.
- Agent sayısı, model seçimi, topology, host/runtime, physical module/service yapısı açık.

## 6. Sıradaki bounded iş

S1-14'ün açtığı research sorusunu çözmeden effective-assignment düzenine geçme.

Önce bounded family testini yap:

1. Research'ün primary deliverable olduğu DevOS Work örneklerini seç.
2. Üç rivalı ayrı test et:
   - cross-family method/capability;
   - F1 specialization;
   - ayrı candidate family (`F8?`).
3. Research deliverable'ını F1 design, F5 assurance ve F6 diagnosis/investigation'dan ayır.
4. Yeni familya gerekmiyorsa nedenini; gerekiyorsa hangi success direction ve specialization sınırıyla gerektiğini açıkla.
5. Sonuçtan sonra B1–B9 coverage map'i yalnız gerekiyorsa düzelt.

Bu test bitmeden mimari, agent topolojisi veya physical implementation seçme.
