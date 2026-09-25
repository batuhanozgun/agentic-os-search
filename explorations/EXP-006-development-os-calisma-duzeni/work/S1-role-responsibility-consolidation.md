# S1 — Araştırmaya dayalı rol ve sorumluluk konsolidasyonu

**Üst iş:** [WORK](../WORK.md)  
**Durum:** HAZIRLIK / kaynak seçimi ve yöntem netleştirmesi. Rol birleştirme veya ayırma kararı henüz verilmedi.  
**Amaç:** B1–B9'dan türeyen Development OS sorumluluklarını, R1–R25 rol adaylarını ve M1–M9 mekanik sorumluluklarını araştırma örnekleriyle sınayarak gerekçeli bir bütün oluşturmak.  
**Sınır:** SOUL veya Development OS mimarisi, ürün seçimi, ajan sayısı ya da kurulum kararı değildir.

## 1. Kullanıcı yönlendirmesi ve mevcut konum

25 Eylül 2026 tarihli bu konuşmadaki kullanıcı mesajı:

> Bu aşamada repodaki araştırmalardan da yararlanmak çok faydalı olur bence, repoda bir soul örneği olmasa da bir her bir araştırma bu rollerin uğraşacağı yapılarla ilgili bilgiler verebilir. S1 çalışmasında repodaki studies örnekleri çok yararlı olabilir.

Bu yönlendirme, mevcut araştırmaların S1'e girdi olmasını ister. Aşağıdaki okuma sırası ve karşılaştırma biçimi assistant'ın uygulama önerisidir; kullanıcı tarafından tek tek kabul edilmiş rol veya mimari kararları değildir.

Üst zincir değişmedi: SOUL hedefi → Development OS'un SOUL'u geliştirme işleri → gerekli kabiliyet ve sorumluluklar → bunları taşıyabilecek roller ve mekanik düzen → daha sonra Development OS yapısı.

B1–B9 ilk ayrıştırmaları ve R1–R25/M1–M9 adayları korunuyor. Bu tur onları doğrulanmış veya nihai saymaz; yeni rol de eklemez.

## 2. S1'in sorusu yalnız rol sayısı değildir

Araştırmalar iki yönden kullanılacak:

- **Sorumluluk ayrımı:** Hangi görevler birlikte taşınabilir, hangileri farklı bilgi, yetki, amaç veya hata denetimi gerektirir? Mevcut adaylarda eksik ya da yanlış düzeyde bir sorumluluk var mı?
- **Sorumluluğun gerçekleştirilebilmesi:** Bu işi taşıyan DevOS aktörü hangi bilgiye, yönteme, kaynağa, araca ve sınama yoluna ihtiyaç duyar? Araştırmanın var olması, aktörün onu bulacağı veya doğru kullanacağı anlamına gelmez.

Amaç 25 adı daha az ada indirmek değildir. Araştırma; birleştirmeyi, ayırmayı, mevcut ayrımı korumayı, yeni bir eksik sorumluluğu açmayı veya kararı ertelemeyi gerekçelendirebilir.

## 3. Analiz düzeyini koru

Bir örnek sistemin kendi işini yürütürken kullandığı rol, otomatik olarak Development OS geliştirme rolü değildir.

Her aktarımda şu soruyu cevapla:

> Bu örnekte gördüğümüz davranış veya mekanizmayı SOUL'a kazandırmak için Development OS'un neyi araştırması, tasarlaması, uygulaması, sınaması ve bakım altında tutması gerekir?

DevOS'un SOUL'u geliştirmesi, gelecekteki SOUL'un kullanıcı işini yürütmesi ve mevcut EXP-006 çalışmasının kayıt düzeni ayrı düzeylerdir. Benzer işlev bulunması aynı aktör veya tek uygulama gerektirmez.

M1–M9'u mekanik sorumluluk olarak adlandırmak, bunların kendiliğinden üretileceği anlamına gelmez. Bunları geliştirecek ve sınayacak DevOS sorumlulukları ayrıca izlenmelidir. Bu bir eksik-rol sonucu değil, S1'de kontrol edilecek açıklıktır.

## 4. İlk seçici okuma rotaları

Aşağıdaki eşleştirmeler okuma adaylarıdır; rol eşitliği, ürün önerisi veya tamamlanmış karşılaştırma değildir. Araştırmalar önce kendi nesneleri, terimleri ve kanıt sınırlarıyla okunur.

| Araştırma rotası | S1'de sorulacak soru | İlgili adaylar / alanlar | Bu turdaki okuma düzeyi |
|---|---|---|---|
| [Superpowers](../../../research/studies/superpowers/META.md) → STATE / CORE / CLOSURE-AUDIT → ilgili S01–S06 ve kaynak kaydı | Üretim, inceleme, uyuşmazlık çözümü ve yöntem geliştirme nasıl ayrılıyor? Birden fazla değerlendirme hangi koşulda aynı rolce taşınabiliyor? | R1–R3, R6/R8/R12/R18, R24–R25; B1/B3/B4/B9 | META, STATE, CORE ve CLOSURE-AUDIT tam okundu; alt kaynaklar bu tur yeniden okunmadı. |
| [gstack](../../../research/studies/gstack/META.md) → CORE / INDEX → ilgili sentez ve kaynak kaydı | Plan, üretim, inceleme, teslim ve gerçek sonuç arasındaki geçiş hangi bilgi, rol ve mekanik denetimi gerektiriyor? | B1/B4/B5/B6/B9; özellikle üretim–doğrulama ve karar–uygulama sınırları | META tam okundu; bu tur yeni ayrıntılı kaynak doğrulaması yapılmadı. |
| [İş yönetimi karşılaştırması](../../../research/studies/work-management-project-control/META.md) → STATE / METHOD / 10-CLOSURE-EVALUATION → seçilen hedefin META/FINDINGS | İş planı, bağımlılık, işi üstlenme, çalışan oturum, ilerleme ve bütünleştirme hangi farklı sorumlulukları doğuruyor? | R10–R12, R17, R21–R22; B4/B6/B8 | Üst paketin META, STATE, METHOD ve kapanış değerlendirmesi tam okundu. Sekiz hedef bu tur baştan okunmadı. |
| [Bağlam / bellek / çalıştırma düzeni](../../../research/studies/context-memory-harness-engineering/META.md) → STATE / INDEX → ilgili sentez | Bilginin yaşam döngüsü, aktöre sunulması ve talimatların gerçekten uygulanması nerede ayrılıyor? | R4–R6, R13–R15, R21/R23; B2/B5/B8 | META tam okundu; ayrıntılı yeniden kullanım seçilen soruda yapılacak. |
| [Hermes](../../../research/studies/hermes-agent/META.md) → STATE / INDEX → ilgili sınırlı bulgu ve kaynak | Bir yöntem/bilgi kaydı kim tarafından değiştiriliyor, nasıl bulunuyor ve hangi aktörün kullanımına gerçekten giriyor? | B2/B3/B7/B8; R4/R5/R9/R21/R23 | META tam okundu. Araştırma kısmi; tamamlanmış bulgu ile açık soru ayrılacak. |
| [ECC](../../../research/studies/ecc/META.md) → STATE / CORE / INDEX → ilgili bulgu ve kaynak | Taşınabilir yönerge, gerçek tüketici, iş kaydı, çalışan süreç ve denetim arasında hangi ilişkiler kurulmuş? | B1/B2/B4/B6/B8; talimat–uygulama ve kayıt–gerçek iş sınırları | META tam okundu. Araştırma kısmi; ayrı ECC araştırmasının sonraki işi burada başlatılmaz. |

İş yönetimi üst paketi; OpenProject, Flowable, Beads, OpenSpec, Spec Kit, Leantime, Gas Town ve ERPNext'e yönlendiriyor. Yalnız seçilen S1 sorusuna katkı veren hedefe inilecek. Bunların tamamını bir araya getirerek tek sistem kurmak önerilmiyor.

Katalogda yalnız araştırılacak olarak kayıtlı paketler, tamamlanmış bulgu kaynağı sayılmayacak. İlk rota listesi kapalı bir evren değildir; somut açıklık çıkarsa diğer ilgili çalışmalar seçilebilir.

## 5. Bu turda görünür olan iki somut karşılaştırma girdisi

**Superpowers CORE §3:** İncelenen kaynak düzeninde tek görev inceleyicisi hem gereksinime uygunluk hem kalite hükmü veriyor. CORE, iki hükmün iki bağımsız inceleyici anlamına gelmediğini de açık tutuyor. **S1 çıkarımı:** farklı değerlendirme başlıkları tek başına ayrı rol zorunluluğu doğurmaz. Bu, mevcut doğrulayıcı adaylarımızın birleşmesi gerektiğinin kanıtı değildir; kaynak kapsamı, uzmanlık ve bağımsızlık ihtiyaçları ayrıca sınanacak.

**İş yönetimi kapanış değerlendirmesi §§2–4:** Yetki, atama, işi üstlenme, çalışan oturumun varlığı ve bütünleştirme yetkisi; ayrıca plan, kalıcı iş durumu ve yürütme durumu ayrılıyor. **S1 çıkarımı:** üst rol ailesi oluştursak bile bu sorumlulukları tek bir belirsiz “yönetici” adıyla kaybetmemeliyiz. Ayrımın korunması mutlaka ayrı fiziksel aktör gerektirmez.

Bunlar repository araştırmalarının yeniden okunmasından çıkan sınırlı girdilerdir. Bu tur dış ürünler, canlı aktörler veya yeni deneyler çalıştırılmadı; güncel ürün sürümleri doğrulanmış sayılmaz.

## 6. Her sorumluluk kümesinde tutulacak karşılaştırma kaydı

1. **DevOS sorusu:** Hangi B işi, hangi R/M adayı ve hangi açık ayrım değerlendiriliyor?
2. **Kaynak gözlemi:** Örnek kendi bağlamında ne yapıyor; bunu kim/ne taşıyor; hangi belge/kod/deney destekliyor?
3. **Aktarım koşulu:** DevOS aktörünün gereken bilgisi, erişimi, yetkisi, yöntemi ve mekanik desteği ne? Kaynağın insana bıraktığı teknik yük var mı?
4. **Karşı örnek ve sınır:** Örneğin hangi açığı, başarısızlığı veya araştırılmamış bölümü var? Bizde aynı sonucun geçerli olmamasına ne yol açabilir?
5. **S1 sonucu:** Birleştir / ayır / koru / eksik sorumluluk aç / açık bırak. Her sonucun gerekçesi ve dayanağı görünür kalır.

Asıl kaynak, önceki araştırmacının yorumu ve bu S1 çalışmasının çıkarımı ayrı tutulur. Güncel dış ürün davranışına veya uygulanabilirliğine dayanacak karar öncesinde ilgili birincil kaynak yeniden doğrulanır.

## 7. Devam ve dönüş noktası

**Bu tur tamamlanan:** kaynak kullanımının amacı, ilk okuma rotaları ve sınırlı iki karşılaştırma girdisi. S1 konsolidasyonu tamamlanmadı.

**Önerilen ilk inceleme dilimi:** üretim–inceleme–düzeltme ilişkisinde hangi sorumlulukların birlikte taşınabileceği ve hangilerinin ayrı kalması gerektiği. Superpowers'ın ilgili ayrıntılı kaynaklarına, sonra karar açısından gerekli gstack karşılaştırmasına in; sonuçları ilgili B tanımlarıyla aynı analiz düzeyinde karşılaştır.

**Dönüş noktası:** gerekçeli ilk sorumluluk kümesini kullanıcıya sun; tüm R1–R25'i tek turda nihai düzene dönüştürme. Ürün, mimari ve ajan sayısı seçimi bu dilimin sonucu değildir.
