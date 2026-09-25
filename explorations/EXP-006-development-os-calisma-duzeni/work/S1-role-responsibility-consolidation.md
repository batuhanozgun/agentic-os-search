# S1 — Araştırmaya dayalı rol ve sorumluluk konsolidasyonu

**Üst iş:** [WORK](../WORK.md)  
**Durum:** DEVAM EDİYOR. Kaynak seçimi ve yöntem hazırlığından sonra S1-01 üretim–inceleme–düzeltme dilimi tamamlandı; sonuçları adaydır. S1'in bütünü ve nihai rol düzeni kabul edilmiş değildir.  
**Amaç:** B1–B9'dan türeyen Development OS sorumluluklarını, R1–R25 rol adaylarını ve M1–M9 mekanik sorumluluklarını araştırma örnekleriyle sınayarak gerekçeli bir bütün oluşturmak.  
**Sınır:** SOUL veya Development OS mimarisi, ürün seçimi, ajan sayısı ya da kurulum kararı değildir.

## 1. Kullanıcı yönlendirmesi ve mevcut konum

25 Eylül 2026 tarihli bu konuşmadaki kullanıcı mesajı:

> Bu aşamada repodaki araştırmalardan da yararlanmak çok faydalı olur bence, repoda bir soul örneği olmasa da bir her bir araştırma bu rollerin uğraşacağı yapılarla ilgili bilgiler verebilir. S1 çalışmasında repodaki studies örnekleri çok yararlı olabilir.

Bu yönlendirme, mevcut araştırmaların S1'e girdi olmasını ister. Kullanıcının sonraki “Güzel. Devam et lütfen.” mesajı üzerine ilk inceleme dilimi yürütüldü. Okuma sırası ve karşılaştırma sonuçları assistant'ın gerekçeli önerileridir; kullanıcı tarafından tek tek kabul edilmiş rol veya mimari kararları değildir.

Üst zincir değişmedi: SOUL hedefi → Development OS'un SOUL'u geliştirme işleri → gerekli kabiliyet ve sorumluluklar → bunları taşıyabilecek roller ve mekanik düzen → daha sonra Development OS yapısı.

B1–B9 ilk ayrıştırmaları ve R1–R25/M1–M9 adayları korunuyor. S1-01 bu kayıtların üstüne değerlendirme ekledi; eski kimlikleri silmedi, yeni R/M kimliği üretmedi.

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

M1–M9'u mekanik sorumluluk olarak adlandırmak, bunların kendiliğinden üretileceği anlamına gelmez. Bunları geliştirecek ve sınayacak DevOS sorumlulukları ayrıca izlenmelidir. Hazırlıkta kontrol sorusu olarak tutulan bu konu, S1-01'de **G1 — üretim/uygulama sorumluluğunun yeterince açık izlenmemesi** bulgusuna dönüştü. Bütün üretim işinin unutulduğu veya mutlaka yeni rol gerektiği sonucu çıkarılmadı.

## 4. Hazırlık turunda seçilen okuma rotaları

Aşağıdaki eşleştirmeler okuma adaylarıdır; rol eşitliği, ürün önerisi veya tamamlanmış karşılaştırma değildir. Araştırmalar önce kendi nesneleri, terimleri ve kanıt sınırlarıyla okunur. S1-01'in ek okumaları kendi dosyasındaki okuma izinde bulunur.

| Araştırma rotası | S1'de sorulacak soru | İlgili adaylar / alanlar | Hazırlık turundaki okuma düzeyi |
|---|---|---|---|
| [Superpowers](../../../research/studies/superpowers/META.md) → STATE / CORE / CLOSURE-AUDIT → ilgili S01–S06 ve kaynak kaydı | Üretim, inceleme, uyuşmazlık çözümü ve yöntem geliştirme nasıl ayrılıyor? Birden fazla değerlendirme hangi koşulda aynı rolce taşınabiliyor? | R1–R3, R6/R8/R12/R18, R24–R25; B1/B3/B4/B9 | META, STATE, CORE ve CLOSURE-AUDIT tam okundu; alt kaynaklar hazırlıkta yeniden okunmadı. |
| [gstack](../../../research/studies/gstack/META.md) → CORE / INDEX → ilgili sentez ve kaynak kaydı | Plan, üretim, inceleme, teslim ve gerçek sonuç arasındaki geçiş hangi bilgi, rol ve mekanik denetimi gerektiriyor? | B1/B4/B5/B6/B9; özellikle üretim–doğrulama ve karar–uygulama sınırları | META tam okundu; hazırlıkta yeni ayrıntılı kaynak doğrulaması yapılmadı. |
| [İş yönetimi karşılaştırması](../../../research/studies/work-management-project-control/META.md) → STATE / METHOD / 10-CLOSURE-EVALUATION → seçilen hedefin META/FINDINGS | İş planı, bağımlılık, işi üstlenme, çalışan oturum, ilerleme ve bütünleştirme hangi farklı sorumlulukları doğuruyor? | R10–R12, R17, R21–R22; B4/B6/B8 | Üst paketin META, STATE, METHOD ve kapanış değerlendirmesi tam okundu. Sekiz hedef hazırlıkta baştan okunmadı. |
| [Bağlam / bellek / çalıştırma düzeni](../../../research/studies/context-memory-harness-engineering/META.md) → STATE / INDEX → ilgili sentez | Bilginin yaşam döngüsü, aktöre sunulması ve talimatların gerçekten uygulanması nerede ayrılıyor? | R4–R6, R13–R15, R21/R23; B2/B5/B8 | META tam okundu; ayrıntılı yeniden kullanım seçilen soruda yapılacak. |
| [Hermes](../../../research/studies/hermes-agent/META.md) → STATE / INDEX → ilgili sınırlı bulgu ve kaynak | Bir yöntem/bilgi kaydı kim tarafından değiştiriliyor, nasıl bulunuyor ve hangi aktörün kullanımına gerçekten giriyor? | B2/B3/B7/B8; R4/R5/R9/R21/R23 | META tam okundu. Araştırma kısmi; tamamlanmış bulgu ile açık soru ayrılacak. |
| [ECC](../../../research/studies/ecc/META.md) → STATE / CORE / INDEX → ilgili bulgu ve kaynak | Taşınabilir yönerge, gerçek tüketici, iş kaydı, çalışan süreç ve denetim arasında hangi ilişkiler kurulmuş? | B1/B2/B4/B6/B8; talimat–uygulama ve kayıt–gerçek iş sınırları | META tam okundu. Araştırma kısmi; ayrı ECC araştırmasının sonraki işi burada başlatılmaz. |

İş yönetimi üst paketi; OpenProject, Flowable, Beads, OpenSpec, Spec Kit, Leantime, Gas Town ve ERPNext'e yönlendiriyor. Yalnız seçilen S1 sorusuna katkı veren hedefe inilecek. Bunların tamamını bir araya getirerek tek sistem kurmak önerilmiyor.

Katalogda yalnız araştırılacak olarak kayıtlı paketler, tamamlanmış bulgu kaynağı sayılmayacak. İlk rota listesi kapalı bir evren değildir; somut açıklık çıkarsa diğer ilgili çalışmalar seçilebilir.

## 5. Hazırlıkta görünür olan iki karşılaştırma girdisi

**Superpowers CORE §3:** İncelenen kaynak düzeninde tek görev inceleyicisi hem gereksinime uygunluk hem kalite hükmü veriyor. CORE, iki hükmün iki bağımsız inceleyici anlamına gelmediğini açık tutuyor. Hazırlık çıkarımı: farklı değerlendirme başlıkları tek başına ayrı rol zorunluluğu doğurmaz. S1-01 bunu asıl kaynakta yeniden kontrol etti; uzmanlık ve bağımsızlık koşulları korunarak ortak aile önerisi geliştirdi.

**İş yönetimi kapanış değerlendirmesi §§2–4:** Yetki, atama, işi üstlenme, çalışan oturumun varlığı ve bütünleştirme yetkisi; ayrıca plan, kalıcı iş durumu ve yürütme durumu ayrılıyor. Hazırlık çıkarımı: üst rol ailesi oluştursak bile bunları tek bir belirsiz yönetici adıyla kaybetmemeliyiz. Ayrımın korunması mutlaka ayrı fiziksel aktör gerektirmez.

Bunlar repository araştırmalarından çıkarılan sınırlı girdilerdir. Hazırlık ve S1-01 güncel ürün sertifikası veya yeni canlı deney değildir.

## 6. Her sorumluluk kümesinde tutulacak karşılaştırma kaydı

1. **DevOS sorusu:** Hangi B işi, hangi R/M adayı ve hangi açık ayrım değerlendiriliyor?
2. **Kaynak gözlemi:** Örnek kendi bağlamında ne yapıyor; bunu kim/ne taşıyor; hangi belge/kod/deney destekliyor?
3. **Aktarım koşulu:** DevOS aktörünün gereken bilgisi, erişimi, yetkisi, yöntemi ve mekanik desteği ne? Kaynağın insana bıraktığı teknik yük var mı?
4. **Karşı örnek ve sınır:** Örneğin hangi açığı, başarısızlığı veya araştırılmamış bölümü var? Bizde aynı sonucun geçerli olmamasına ne yol açabilir?
5. **S1 sonucu:** Birleştir / ayır / koru / eksik sorumluluk aç / açık bırak. Her sonucun gerekçesi ve dayanağı görünür kalır.

Asıl kaynak, önceki araştırmacının yorumu ve bu S1 çalışmasının çıkarımı ayrı tutulur. Güncel dış ürün davranışına veya uygulanabilirliğine dayanacak karar öncesinde ilgili birincil kaynak yeniden doğrulanır.

## 7. İnceleme dilimleri ve güncel dönüş noktası

| Dilim | Durum | Sonuç / devam |
|---|---|---|
| Hazırlık | Tamamlandı | Kaynak rotaları, yöntem ve iki sınırlı karşılaştırma girdisi. |
| [S1-01 — üretim, inceleme ve düzeltme](S1-01-production-review-correction.md) | Sınırlı inceleme tamamlandı; A1–A4 ve G1 aday | İnceleme ailesi; üretim–düzeltme ilişkisi; teşhis/karar ayrımı; sürüme bağlı yeniden sınama; geliştirme sorumluluğunun açıklığı. |
| Sonraki dilim | Önerildi; henüz yapılmadı | Tasarım–üretim–bütünleştirme zincirini, ilgili B ve R/M kapsamlarını somutlaştırmak. |

**S1-01'in özeti:** R2/R6/R8/R12/R15/R18 ortak bir inceleme ailesinde düşünülebilir; özel iddialar ve uzmanlıklar korunur. Üretim ve düzeltme aynı ailede taşınabilir; bağımsızlık gereken kapanışta kendi kontrolü yeterli sayılmaz. R3 teşhisi ile teknik karar ayrıdır. Kod/prosedür/bağlantı üretimini, hazır mekanizmayı kurma ve işletmeden ayıran sorumluluk eşlemesi eksiktir; G1 sonraki dilimin odağıdır.

R1–R25 ve M1–M9 ilk aday kayıtları henüz yeniden numaralanmadı veya nihai olarak birleştirilmedi. [ACTORS](../ACTORS.md) başlangıç türetimlerini, bu dosya ve alt dilimler S1 değerlendirmesini taşır.

**Dönüş noktası:** İlk aday kümesini kullanıcıya sun. Sonraki turda verilen yönle G1'e odaklan; bütün S1'i tek turda bitirme, mimari veya ajan sayısına geçme. Yeni bulguların kullanıcı tarafından kabul edildiğini varsayma.
