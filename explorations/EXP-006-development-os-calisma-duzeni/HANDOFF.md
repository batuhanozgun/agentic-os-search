# EXP-006 — HANDOFF

**Amaç:** Yeni oturumun EXP-006'yı son alt örnekten değil, current üst iş ve doğru dönüş noktasından devralması.  
**Güncelleme:** 26 Eylül 2026.  
**Güncel iş:** S1 — Development OS rol/sorumluluk konsolidasyonu.  
**Son tamamlanan dilim:** [S1-13](work/S1-13-learning-adaptation-direction-family.md), F7 family review.  
**Sıradaki iş:** F1–F7 bütün model coverage/overlap denetimi.

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
- F3 Information Lifecycle Operations yeni açık specialization.
- R1–R25'ten familyalara geçiş henüz kullanıcıca nihai DevOS kadrosu olarak kabul edilmedi.
- Family overlap, full B1–B9 coverage ve orphan-responsibility audit henüz yapılmadı.
- Agent sayısı, model seçimi, topology, host/runtime, physical module/service yapısı açık.

## 6. Sıradaki bounded iş

Yeni familya icat etmeye başlama.

Önce tek konsolide denetim yap:

1. B1–B9 sorumluluklarını F1–F7 üstüne yeniden projekte et.
2. Orphan ve duplicate sorumlulukları bul.
3. Initial R1–R25'in current lineage eşlemesini kontrol et.
4. Research, decision, coordination gibi kavramların ayrı familya gerektirip gerektirmediğini yeniden test et.
5. Family-model yeterliyse ancak ondan sonra effective role/assignment düzenine geç.

Bu denetim bitmeden mimari veya agent topolojisine geçme.
