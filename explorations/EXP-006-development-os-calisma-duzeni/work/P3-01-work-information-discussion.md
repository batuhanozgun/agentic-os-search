# P3-01 — İş, yapı ve bilgi akışı: bütünleşik tartışma taslağı

**Üst iş:** [WORK/P3](../WORK.md). **Güncelleme:** 27 Eylül 2026.  
**Sürüm:** v0.3; bu revizyonun başlangıcı `agentic-os-search@89ec8892697f7280caa54956066c7919fc2988b9`.  
**Statü:** DISCUSSION BASELINE / CANDIDATE / CONCRETE WALKTHROUGH. P3 tamamlanmadı; P4–P6 başlamadı. Kullanıcı yönü mantıklı buldu ve somutlaştırma istedi; bütün sözleşmelerin kabulü, seçilmiş mimari veya çalışan mekanizma sonucu çıkarılmaz.  
**Değişim:** v0.2'nin G/Y ayrımı ve rol yerleşimi korunur. §5, bağlam, görüş ayrılığı, karar, kayıt, yeni bilgi ve kesintiyi aynı örnekte birleştirir. [Önceki v0.2](https://github.com/batuhanozgun/agentic-os-search/blob/89ec8892697f7280caa54956066c7919fc2988b9/explorations/EXP-006-development-os-calisma-duzeni/work/P3-01-work-information-discussion.md) ve [ilk v0.1](https://github.com/batuhanozgun/agentic-os-search/blob/ed2bf6e2232b38c42b5d58d82f5b700fdd434e77/explorations/EXP-006-development-os-calisma-duzeni/work/P3-01-work-information-discussion.md) kendi kaynak izleriyle korunur.

## 1. Kullanıcı yönü ve önerinin sınırı

P3'ü açan görünür mesaj: “en önemli kısım burası. burada araştırma reposu sana bir çok örnek ve bir çok metodoloji verebilir. burayı biraz derin konuşalım. hemen karar verme, bana bir yapı sun, birlikte değerlendirelim. senin sunduğunu baz alalım.”

Sonraki iki görünür öneri:

> “burada şu ayrımı ortaya koy önce, ona göre konuşalım bence. işi yapanlar ile ortamı yönetenler ayrı olmalı. işi yapanların işle ilgili denetleyicileri ile ortamdan kaynaklı denetliyiciler farklı motivasyonlara sahip olacaklardır. bunu düşün benimki sadece öneri”

> “işi yapmanın koordinasyonu ile yapının koordinasyonu bence farklı. senin buradaki bu soruyu sorma sebebin nedir tam olarak? varsayımlarımızı çapıştıralım.”

Kullanıcı ardından gereksiz küçük turları eleştirdi ve bütünlüklü taslağa devam istedi. v0.2 sunulduktan sonraki mevcut mesaj:

> “Bu yön bana mantıklı geldi ama biraz daha somutlaştır bunu.”

Bunlar model-visible mesaj aktarımıdır; platform export'u değildir. Son ifade yön desteği ve somutlaştırma yetkisidir; bütün tasarım ayrıntıları için kabul değildir. Kısa sunum, küçük miktarda iş yapma veya her ayrımda yeni onay isteme şartı değildir.

**Aday ayrım:** İki hedef alanı vardır; her ikisi de DevOS'un içindedir.

- **G — SOUL geliştirme:** SOUL için gerekli işi keşfetmek, araştırmak, planlamak, tasarlamak, gerçekleştirmek ve sonucun yeterliğini değerlendirmek.
- **Y — DevOS işleyişi:** Bu ekibin çalışmasını mümkün kılan görevlendirme, bilgi/bağlam, iletişim, araç, erişim, süreklilik ve gerekli yapı bakımını işletmek ve sınamak.

Y de Work yapar ve reasoning gerektirebilir; yalnız shell komutu çalıştıran teknik hizmet değildir. Her iki alanda da WORK, INFORMATION, ACTORS ve ENVIRONMENT ilişkileri vardır. Y alanını Foundation'ın ENVIRONMENT ground'uyla eşitleme. SOUL'da bir ortam veya hafıza kapasitesi geliştirmek G işidir; DevOS'un kendi ortamını/hafızasını işletmek Y işidir. Sınıflandırmada dosya/konu adı değil, değiştirilen veya doğrulanan hedef belirleyicidir.

İki hedef alanı; iki kalıcı takım, iki repository, iki lead veya iki ayrı ürün kararı değildir. Claude topolojisi P4'te kalır. Gerçek ilk ve sonraki SOUL işlerini burada seçmiyoruz; bunları kurulacak ekip keşfeder.

## 2. Mevcut rollerin tamamına uygulama

[ACTORS](../ACTORS.md) ve [P2-01](P2-01-named-role-contracts.md), DR01–DR16'nın ilk sözleşme tabanıdır. Aşağıdaki G/Y profilleri bu tabana önerilen P3 düzeltmesidir; yeni kalıcı rol sayımı veya kabul edilmiş kadro değildir. DR06 ve DR13'ün iki hedefi ayrı isimle görünür kılınır. Diğer roller sırf iki alan var diye iki kez kurulmaz.

| Taban | G — SOUL geliştirme katkısı | Y — DevOS işleyişi katkısı / sınır |
|---|---|---|
| DR01 İş Keşfi ve Planlama | Hedef/birikimden iş ve önkoşul adaylarını bütünleştirir; yaşayan geliştirme planı | Yapıya yönelik ayrı ve yetkili değişiklikte aynı planlama yetkinliği kullanılabilir; ürün önceliğini Y'ye devretmez |
| DR02 Kapasite Tasarımcısı | SOUL kapasitesini gerekli alan uzmanlığıyla tasarlar | Eksik DevOS kapasitesi gerçek bir tasarım işi gerektiriyorsa hedefi açık ayrı görevlendirme |
| DR03 Sistem Bütünlüğü Tasarımcısı | SOUL tasarımlarının birlikte yeterli olmasını ele alır | DevOS yapısı değişecekse onun bütünlüğünü ayrı kapsamla ele alır; ürün ve üretim sistemi birbirine karışmaz |
| DR04 Sınama Tasarımcısı | G iddiaları için kriter, oracle ve sınama tasarımı | Y iddiaları için ayrı hedef/koşul/sınama tasarımı; tek test iki hedefin tamamını kanıtlamaz |
| DR05 Uygulama Geliştiricisi | SOUL uygulama ve mekanizmalarını gerçekleştirir | Yetkili DevOS mekanizma değişikliğini gerçekleştirebilir; bakım bahanesiyle sınırsız öz-değişiklik yapmaz |
| **DR06-G SOUL Geliştirme Koordinatörü** | Katkıların hangi sırada, hangi bağımlılıklarla üst sonuca birleşeceğini işletir | Kapasite ve engel bilgisi alır; oturum/erişim bakımını kendisi yapmak zorunda değildir |
| **DR06-Y DevOS İşletim Koordinatörü** | G'nin kapsamlı yürütme isteğini alır; ürün önceliği seçmez | Etkinleştirme, teknik bekleme, kapasite, devir ve kurtarmayı koordine eder; DR07–10/12'yi gerektiğinde kullanır |
| DR07 Bilgi Sorumlusu | Ürün bilgisinin domain doğruluğu üretici/karar sahibinde kalır | Ürün ve çalışma kayıtlarının kaynak, sürüm, statü ve lifecycle bütünlüğünü işletir; tüm dosyaların tek yazıcısı değildir |
| DR08 Bağlam Kurucusu | İş sahibi ve tüketici hangi soruya hangi bilginin gerektiğini belirlemeye katılır | Uygun kaynak/görünümü hazırlar, erişim ve eksikliği görünür kılar; anlam yeterliğini tek başına ilan etmez |
| DR09 Rol ve Katılım Sorumlusu | İşin ihtiyaç duyduğu katkı/yeterlik tarifini alır | Uygun aktörün role bağlanması, değişmesi ve katılım kaydı; yeterlik veya grant yaratmaz |
| DR10 Ortam İşleticisi | G'nin araç/koşul gereğini alır | Yetkili mevcut mekanizmalarla ortam/erişim/operasyon; yeni mekanizma gerekirse sınırlı değişiklik işi |
| DR11 Sınama Yürütücüsü | G hedefinde koşu ve gözlem üretir | Y hedefinde ayrı koşu/gözlem üretir; koşu tamamlanması güvence veya kabul değildir |
| DR12 Yetki ve Kontrol Sorumlusu | Ürün/kapsam yetkisinin sınırını gözetir; ürün gerçeğini belirlemez | Delegasyon ve etki sınırını işletir; her rutin eylemi insan onayına taşımaz |
| **DR13-G SOUL Geliştirme İnceleyicisi** | Gerekli işin, tasarımın, uygulamanın ve kapanış iddiasının SOUL hedefiyle uygunluğunu kanıtla değerlendirir | Operasyonel yeşili ürün doğruluğu saymaz; alan uzmanlığı gerekir |
| **DR13-Y DevOS İşleyiş İnceleyicisi** | G'nin gerçekten ihtiyaç duyduğu çalışma koşullarını sınama girdisi alır | Görevlendirme, bağlam, iletişim, yetki, kayıt ve devam koşullarının fiilen sağlanmasını sınar; yalnız process liveness ölçmez |
| DR14 Teşhis ve Etki Analisti | Ürün/plan/tasarım hatası ve etkilenen sonuçlar | İşleyiş arızası ve etkilenen çalışmalar; her olayda hedef ve kanıt kapsamı ayrı |
| DR15 Öğrenme ve Yöntem Sorumlusu | SOUL geliştirme yöntemine ilişkin deneyimi değerlendirir | DevOS işletim deneyimini değerlendirir; yeni kural veya kontrolü kendi başına yürürlüğe koymaz |
| DR16 Araştırmacı | SOUL'a ilişkin bilgi sorusu için kaynaklı bulgu | DevOS işleyiş sorusu için kaynaklı bulgu; soru/uzmanlık/tüketiciye göre ayrı görevlendirme |

G ve Y inceleyicileri aynı kanıta sadakat ilkesini paylaşır; başarı nesneleri, uzmanlıkları ve muhtemel teşvik çatışmaları farklıdır. G inceleyicisi mutlaka kusur bulmakla, Y inceleyicisi de sistemi sürekli yeşil göstermekle başarılı sayılmaz. Kendi ürettiği şeyi farklı rol adıyla değerlendirmek bağımsızlık kanıtı değildir; actor/context ayrımı P4/P6'da gerekçelendirilir.

## 3. İki koordinasyon arasındaki karar sözleşmesi

**G koordinasyonu:** DR01 ve alan sorumlularının gerekçeli iş/plan kararlarını yürütmeye taşır. Hangi katkının hangi kararı beklettiğini, iş önceliğini, sonuç birleştirmeyi ve geliştirme engelinin disposition'ını takip eder. Bütün teknik kararların sahibi değildir.

**Y koordinasyonu:** Verilmiş iş isteğini uygun koşullarda yürütülebilir hâle getirir; çağırma, çalışma denemesi, erişim, kapasite ve geri dönüşü izler. İzinli eşdeğer çalışma seçenekleri arasında seçim yapabilir; istenen sonucu veya kalite ölçütünü değiştiremez.

Aradaki ilişki “emir veren üst akıl → düşünmeyen altyapı” değildir. Y gerçek kısıt, eksik yetkinlik ve alternatif yol bildirir; G bunun ürün/öncelik sonucunu değerlendirir. G yapı kapasitesini var sayamaz, Y ürün gereksinimini sessizce daraltamaz.

**Yürütme isteğinin gerekli anlamı:** Hangi iş/soru, neden gerekli, beklenen teslimat ve tüketici, bağlı karar/üst iş, ilgili kaynak ve hedef sürümleri, gerekli uzmanlık/yetki, gerçek bağımlılık ve geri dönüş noktası. Bunlar zorunlu ayrı dosya alanları değildir; mevcut kayıtlar yeterliyse yeniden kopyalanmaz.

**Geri dönüş:** Sonuç veya açık engel; çalışma denemesi kimliği/koşulu; değişen nesne ve dayanaklar; neyin eksik kaldığı; hangi karar veya çalışma tarafından tüketileceği. “Başlatıldı”, “yanıt geldi”, “sonuç yeterli bulundu”, “ürüne uygulandı” ve “üst iş kapandı” farklı standing'lerdir.

## 4. Uçtan uca çalışma önerisi

1. **Hedefi devralma ve iş keşfi:** Ekip hedef, sınırlar, araştırma birikimi ve mevcut sonuçları devralır. DR01 gerekli işleri diğer rollerin katkılarıyla keşfeder. DR06-G bağımlılıkları/önceliği koordine eder. B1–B9 sırası hazır backlog yapılmaz. Başlangıç grant/aktör/okuma yolunun kurulması P4/P5 yüküdür.
2. **Çalıştırma:** DR06-G gereken katkıyı ve teslim ilişkisini belirtir. DR06-Y mevcut yeterli koşulları kullanır veya gerekli katılım/ortam/bağlam işini koordine eder. Her çağrıda bütün işletim rollerinin ayrı ayrı çalışması zorunlu değildir.
3. **İş içi işbirliği:** Çalışan uzman eksik bilgi, karşı görüş veya kontrol isteyebilir. Yetki ve mevcut kapsam içindeki küçük danışmalar her mesajda iki koordinatörün onayını beklemez. Yeni bağımlılık, ayrı sorumlu, önemli maliyet, scope veya oturum devri oluşursa katkı izlenebilir ayrı Work hâline gelir. Bu eşik nitel adaydır; kesin sayısal tavan konmadı.
4. **Sonucu kullanma:** Araştırmacı bulgusunu kaynak/sınırla döndürür. Talep sahibi ilgili kararda nasıl kullandığını veya gerekçeli olarak neden kullanmadığını korur. Kritik bir çürütme yalnız istenmediği için yok sayılamaz. Koordinasyon, cevabın tüketicisine dönmesini izler; teknik hükmü onun yerine vermez.
5. **Üretim ve güvence:** G tarafı tasarım/uygulama/üretici kanıtını oluşturur; DR13-G ilgili doğruluk iddiasını sınar. DR13-Y yalnız ilgili ve risk taşıyan işleyiş koşullarını sınar. Her basit iş için zorunlu iki komite veya her seferinde bütün kontrolleri yeniden çalıştırma önerilmez; geçerli kanıtın kapsamı korunur.
6. **Kayıt, etki ve devam:** Alan sahibi içerik/karar/ürün katkısını; DR07 lifecycle ve kaynak/sürüm ilişkisini; DR08 sonraki tüketicinin görünümünü taşır. DR06-G sonuçtan doğan geliştirme durumunu/önceliği; DR06-Y çalışma denemesi/katılım/devri günceller. İşlevsel zincir normal durumda Batu'nun “şimdi sıra sende” komutunu gerektirmez; bu tasarım gereği henüz runtime başarısı değildir.

Akış sabit bir altı aşamalı bant değildir. Karar, araştırma, destek ve kalıcı bakım da Work'tür; bazı adımlar birlikte, tekrar veya paralel gerçekleşebilir. Kayıt ve başarının sahipliği, workflow çizgisinden türetilmez.

## 5. Somut çalışma örneği — soru, karşı görüş, kayıt ve devam

**Tamamı kurgusal tasarım yürüyüşüdür.** Aşağıdaki rol sözleri, iş kimlikleri, durumlar ve karar adayları gerçek ajan çıktısı, deney veya SOUL backlog'u değildir. Gerçek DevOS ekibinin kendi keşfiyle bu soruya geldiğini varsayıyoruz: **“SOUL, kullandığı bilgi değiştiğinde önceki kararlarını nasıl ele almalı?”** Burada bu kapasitenin çözümünü seçmek değil, G/Y işleyişini görünür kılmak amaçlanır.

### 5A. Tek işte rol konuşmaları ve ayrı sorumluluklar

| Olay | G — işi yapan/koordine eden taraf | Y — çalışmayı mümkün kılan taraf | Kalıcı anlamı |
|---|---|---|---|
| Soru açılıyor | Bilgi alanındaki Kapasite Tasarımcısı: “İlk önerim, kaynak değişince ona bağlı kararları yeniden açmak.” Hedef ve seçenek henüz taslak. | İşletim Koordinatörü gerekli rolün atanmasını ve erişimini sağlar; Bağlam Kurucusu ilgili gereksinim, kaynak, eski karar/gerekçe ve sürümü getirir. | `ÖR-İ01`: karar gözden geçirme tasarımı; sahibi belli; uygulamaya alınmış politika değil. |
| Karşı görüş geliyor | Geliştirme İnceleyicisi: “Kaynağın değişmesi, kararın dayanağının geçersizleşmesiyle aynı mı? Aynı kararı destekleyen başka kanıt varsa?” Tasarımcı bu soruyu araştırma ihtiyacı olarak açar. | Y, itirazı yazarak çözülmüş saymaz; doğru işe ve tüketiciye bağlı tutar. İnceleyicinin sadece tasarımcının özetine kapatılmaması gerekir. | `ÖR-A01`: bu iki ayrımı araştır; tüketici tasarımcı, dönüş `ÖR-K01`. Yalnız bu cevaba bağımlı karar bekler. |
| Araştırma çalışıyor | Geliştirme Koordinatörü kapsam/öncelik ve bekleyen kararı izler. Araştırmacı soruyu kaynaklardan değerlendirir; bilgi açığı varsa ek talep üretebilir. | Y çalışma denemesini, katılımı, gerçek erişimi ve yanıt dönüşünü izler. Kaynak bulunmuş olması içeriğin okunması/kullanılması değildir. | `ÖR-Ç01 → ÖR-A01`: çalıştırma denemesi; araştırmanın kendisiyle aynı kimlik/durum değil. |
| Bilgi sonuca dönüyor | Örnek yanıt: “Kaynak güncellemesi, destek gerekçesinin geri çekilmesi ve kararın tersinin kanıtlanması farklıdır.” Tasarımcı: “O hâlde etkilenen gerekçeleri değerlendiren bir seçenek hazırlayayım.” | DR07 dayanak ve statüyü korur; DR08 yanıtı gerekli kaynak bağlarıyla tasarımcının bağlamına taşır. Sonucun gerçekten kullanılmasını isteyen rol gösterir. | Örnekte `ÖR-A01` kapsamı tamamlanabilir; `ÖR-K01` hâlâ öneri. Araştırma bir tasarım kararını otomatik onaylamaz. |
| Yeni açık bulunuyor | İnceleyici: “Bağımlılık kaydı eksikse hangi kararın etkilendiğini nasıl göreceğiz?” Tasarımcı eksikliği kabul eder; Sınama Tasarımcısı karşı vakayı kurar. G koordinasyonu bu katkıyı plana bağlar. | Y, bu yeni inceleme/sınama katkısını mevcut yetki ve kapasite içinde başlatılabilir hâle getirir. Her geçişte Batu'nun komutunu bekleme şartı konmaz. | `ÖR-T01`: eksik bağımlılık ve alternatif destek vakası. Sınama tasarımı/koşu/kanıt ayrı; burada hiçbiri çalıştırılmadı. |
| Karar ve uygulama eşiği | Yetkili alan sorumlusu, itirazı ve yeterli kanıtı ele aldıktan sonra kararını gerekçelendirir. Karşı vaka çözümsüzse “uygulamaya hazır” demez. Sonraki gerçek üretim işlerini DevOS ekibi türetir. | Y doğru sürüm ve izinlerle devir sağlar; olumlu dispatch veya teslim kaydından ürün yeterliği çıkarmaz. | Karar seçimi, güvence hükmü, yürütmeye alma ve uygulanmış ürün ayrı statülerde tutulur. Bu örnekte karar açık bırakıldı. |

Kaynaklardan alınan ayrımlar gerçek research girdileridir; bunları konuşan kurgusal rollerin araştırma yaptığı veya karşı vakayı başarıyla sınadığı iddia edilmez. Tasarımcının ikinci seçeneği burada SOUL için benimsenmiş politika değildir.

### 5B. Rolün gerçekten alacağı girdi

Araştırmacıya yalnız “karar güncellemelerini araştır” denmez. Örnek bağlam paketi şunları taşır:

> **Bağlı iş:** ÖR-İ01. **Soru:** Kaynak değişikliği hangi durumda karar dayanağını etkiler? Alternatif destek varsa ne değişir? **Kullanım:** ÖR-K01 tasarım seçeneklerini karşılaştırmak. **Başlangıç kaynakları:** ilgili Foundation Revision/Selection bulguları ve uygun study örnekleri; sürüm ve özgün kaynağa dönüş yolu. **Sınır:** Bulguyu tasarım kabulüne çevirmeden teslim et. **Beklenen çıktı:** desteklenen ayrımlar, karşı örnekler ve eksik kalan kanıt. **Geri dönüş:** tasarımcı ve açık karar ÖR-K01.

Tasarımcı ayrıca mevcut seçenekleri ve ürün bağlarını; inceleyici bağımsız bakış kurabilmek için gereksinimi, hedef sürümü ve doğrudan kanıt yolunu alır. Her role aynı paket gönderilmez. DR08 ile uzman hangi bilginin gerekli olduğunu birlikte belirler; tüketici gerekli kaynağa daha derin dönebilir. Özet doğru olsa bile bu kullanım için yetersiz olabilir.

### 5C. Üç ayrı kayıt görünümü; üç dosya zorunluluğu değil

| Görünüm | Sahipliği taşıyan | Örnekteki içerik |
|---|---|---|
| **İş ve katkı kaydı** | İş sahibi + DR06-G | ÖR-İ01'in amacı, ÖR-A01'in sorusu/teslimatı, hangi kararın neyi beklediği, ÖR-T01'in neden açıldığı. |
| **Çalıştırma/katılım kaydı** | DR06-Y + ilgili işletim sorumluları | ÖR-A01'i yürütme denemesi ÖR-Ç01; kullanılan aktör/rol, girdi sürümü, başlatma/erişim/yanıt/engel ve yeniden giriş durumu. |
| **Karar, dayanak ve kanıt kaydı** | Alan karar sahibi ve inceleyici; DR07 bakım desteği | ÖR-K01'in seçenekleri, dayanakları, itirazın karşılığı, açık kalan koşul ve ayrı güvence hükmü; varsa hangi ürün sürümüne uygulandığı. |

Bunlar somutlaştırma için gösterilen anlam görünümleridir; seçilmiş şema, dosya adı veya üç canonical kopya değildir. İçerik sahibi kendi sonucu ve gerekçesini üretir; Bilgi Sorumlusu bütün rollerin yerine yazıp karar veren makam olmaz. Gerekli güncelleme kalıcılaşmadan veya tüketiciye ulaşmadan ilgili devir tamam sayılmaz. Atomik yazma/çakışma/yeniden deneme mekanizması P4/P5'te seçilecektir.

### 5D. Oturum burada kesilirse

Örnekte korunması gereken kısa devir şudur:

```text
İş: ÖR-İ01 — karar güncelleme davranışının tasarımı.
Araştırma: ÖR-A01 teslim edildi; kaynak ve bulgu referansları mevcut.
Karar: ÖR-K01 açık; ikinci seçenek henüz kabul edilmedi.
Açık itiraz: bağımlılık kaydı eksikken etkilenen karar nasıl bulunacak?
Beklenen katkı: ÖR-T01 karşı vaka; sahibi/sınırları iş kaydında.
Dönüş: sınama/inceleme sonucuyla tasarımcı ÖR-K01'i değerlendirecek.
Çalıştırma: ÖR-Ç01 ve varsa ÖR-T01 denemesinin gerçek son durumu ayrıca kontrol edilecek.
```

Y yeniden girişte hangi denemenin gerçekten bittiğini, girdilerin güncelliğini ve olası yan etkileri uzlaştırır. G korunmuş soruyu ve bağımlılığı devralır. Geçerli araştırma tekrar yapılmak zorunda değildir; fakat eski kaydın mevcut olması onun hâlâ uygulanabilir olduğunu tek başına göstermez. Kullanıcı gerekirse oturumu yeniden başlatabilir; hangi rolün sırada olduğunu elle tarif etmesi normal mekanizma yapılmaz. Kaybolmuş etki bilinmeden kör retry yoktur.

### 5E. Yeni bilgi veya gecikmiş yanıt gelirse

Yeni kaynak ile mevcut kararı birbirine karıştırmamak için aday yol:

1. DR07 değişikliği ve hangi kayıtların onunla ilişkili olduğunu görünür kılar; bu, bütün sonuçları otomatik yanlış ilan etmek değildir.
2. G tarafındaki ilgili uzman yeni girdinin dayanağı ve kararın geçerliliği üzerindeki anlamını değerlendirir: koruma, yeniden araştırma, düzeltme veya kapsamlı inceleme farklı olası sonuçlardır. Bağımlılık kaydı eksikse etki alanı “yok” değil, “henüz bilinmiyor” olabilir.
3. Y etkilenen tüketiciye güncel bağlamı/uyarıyı ulaştırır. G gerekli karar ve işleri yeniden açar; yalnız ilgili işler bekletilir. Eski girdilerle üretilmiş geç yanıt izden silinmez, fakat güncel kararın yerine otomatik yazılmaz.

**İki denetimin somut farkı:** Örnekte Y inceleyicisi yanlış kaynak sürümünün gösterilmesini veya yanıtın yanlış işe bağlanmasını bulur; G inceleyicisi doğru gelen bilginin yanlış yorumlanmasını ya da yetersiz tasarım seçeneğini sorgular. Aynı olay iki kusur da taşıyabilir. İddialar doğru iş/sürüm/consumer ile bağlı olmalı; “iki taraf da yeşil” bağımsız ve bütünleşik yeterliğin kanıtı değildir.

## 6. Karar, itiraz ve durdurma sınırları

| Durum | G tarafının sorumluluğu | Y tarafının sorumluluğu / dönüş |
|---|---|---|
| Aynı anda iki iş için kapasite yok | Hedef ve bağımlılığa göre öncelik/yeniden planlama | Gerçek kapasiteyi ve uygulanabilir seçenekleri bildir; ilan edilmiş politika içinde sıraya al, ürün önceliğini gizlice değiştirme |
| Tasarım veya bulgu kanıtla desteklenmiyor | İlgili karar sahibi düzeltme/araştırma/alternatif değerlendirme yapar; zorunlu kalite itirazı çözümsüzken olumlu kapanış üretmez | Teknik olarak çağrı başarılı diye işin sonucunu yeterli ilan etmez |
| İzin, kayıp kayıt veya yanlış bağlam sorunu | Etkilenen karar/işin geçerliliğini yeniden değerlendir | Verilmiş kontrol yetkisi içinde ilgili çalışmayı tutar; düzeltme/recovery yolu açar. Acil güvenlik sınırı ilgisiz ürün kararı verme yetkisi değildir |
| Kaynak veya ürün sürümü değişti | Hangi tasarım/karar/kanıtın yeniden açılacağını ilgili uzman belirler | Bağları ve tüketicileri bulur, doğru yeni görünümü/uyarıyı iletir; bütün ekibi sebepsiz baştan çalıştırmaz |
| DevOS'ta yeni mekanizma gerekiyor | Ürüne etkisi ve geliştirme önceliğiyle uzlaştırılır | Mevcut politika içi onarım veya ayrı scope'lu meta-iş ayrılır; tasarım/uygulama/güvence ilgili rollerce yürütülür. Kendi denetimini gevşeterek kapanış yapılmaz |

Olgusal anlaşmazlık kaynak/deney gerektirebilir; tasarım trade-off'u yetkili alan kararını, üst mandate/tercih açığı müşteriyi gerektirebilir. Ne her itiraz otomatik veto ne de çoğunluk oyu doğruluk ölçütüdür. Koordinatör açık itirazın disposition'ını izler; kanıtı idari kararla olumluya çeviremez. Kesin durdurma/grant şeması P4/P5'te bağlanacak; burada sınırsız yeni yetki yaratılmadı.

## 7. INFORMATION sahipliği: içerik, bakım ve kullanım

**İçeriğin sorumlusu:** Araştırmacı bulgusunu, tasarımcı karar/gerekçesini, geliştirici uygulama değişikliğini ve inceleyici hükmünü taşır. Bilgi Sorumlusu bu içeriklerin tümünü doğru ilan eden makam değildir.

**Kaydın işletimi:** Kaynak/gözlem, öneri, kabul edilmiş karar, uygulama ve kanıt ayrı statülerle birbirine bağlanır. İşin kalıcı kimliği, bir çalışma denemesinin kimliğiyle eşitlenmez. SOUL ürün bilgisinin ve DevOS çalışma bilgisinin farklı kullanım amaçları korunur; aynı bilginin iki canonical kopyası açılmaz.

**Bağlamın kuruluşu:** Hangi bilgi gerektiğinin keşfi iş sahibinin/uzmanın ve Bağlam Kurucusunun karşılıklı işidir. DR08 kaynakları anlamaya yetecek uzmanlık veya uzman yardımı olmadan salt anahtar kelimeyle yeterlik ilan etmez. Tüketici erişimi, sürümü ve önemli eksikleri kontrol edebilir; yalnız merkezi özetle sınırlanmaz.

**Kalıcılık:** Maddi soru, kapsam, karar gerekçesi, dayanak sürümü, beklenen katkı ve geri dönüş korunur. Her token/mesaj ayrı kalıcı Work değildir. Kesinti, farklı sahip, kritik sonuç veya pahalı yeniden üretim varsa daha ayrıntılı kayıt gerekebilir. Bu kayıt özel iç düşünce dökümü değil, tekrar kullanılabilir çalışma sonucudur.

**Denetim ayrımı:** Araştırma mantıken yeterli mi sorusu G güvencesine; gereken kaynağın doğru sürümü doğru tüketiciye ulaştı mı sorusu Y güvencesine gider. Sınırın semantik yükü ortak olduğunda iddia parçaları ve tüketici açıkça bağlanır; sadece iki bağımsız yeşil etiket toplanmaz.

## 8. Alternatif ve kapsam kontrolü

En güçlü alternatif, tek koordinatörün G/Y görevlerini açık şapkalarla taşımasıdır. Bu, çağrı maliyetini azaltabilir; fakat bağlam/teşvik/yetki ayrımının korunması gerekir. İki ayrı actor kullanmak da fazladan devir ve çelişki riski yaratabilir. **Şimdiki öneri sorumluluk sözleşmelerini ayırır; fiziksel ayrı actor kararı vermez.**

Aynı şekilde yalnız üretim tarafı düşünür/yapı tarafı mekaniktir veya bütün uzmanlar her iki alanı otomatik bilir varsayımları alınmadı. Yapının değişmesi ayrı Work olabilir; ama her düzenleme için sonsuz bir meta-ekip kurulmaz. İlk yetki ve kontrol yolu dış başlangıç kurulumu olarak P4/P5'te belirlenir; roller birbirlerini sonsuz biçimde yetkilendirmez.

F1–F8 başarı yönleri ile G/Y hedef ayrımı aynı eksen değildir. Yeni F9/F10, ground, zorunlu 18/32 agent veya yeni platform seçilmedi. DR06-G/Y ve DR13-G/Y aday profillerdir; ilk 16 P2 sözleşmesinin yerine kabul edilmiş yeni registry henüz geçirilmedi.

## 9. Araştırma katkısı ve gerçek okuma kapsamı

Aşağıdakiler tasarım gerekçesidir; ürün benimseme veya davranış ispatı değildir. v0.2 okuma başlangıcı `ed2bf6e2232b38c42b5d58d82f5b700fdd434e77`, v0.3 başlangıcı `89ec8892697f7280caa54956066c7919fc2988b9`'dur.

| Dayanak | Bu taslağa somut etkisi | Gerçek kapsam / sınır |
|---|---|---|
| Work Foundation — [ground synthesis](../../../research/soul-foundations/03_ground-deepening/grounds/work/synthesis/WORK-GROUND-AUDIT-SYNTHESIS.md), özellikle §§2,5–7 | Yapı bakımı ve meta-iş de Work; plan/actual/sonuç ayrı. Örnekte araştırma bittiği hâlde karar açık kalır. | Aynı konuşmadaki tam içerik; özgün dış corpus yeniden okunmadı. |
| Actors Foundation — [ground synthesis](../../../research/soul-foundations/03_ground-deepening/grounds/actors/synthesis/ACTORS-GROUND-AUDIT-SYNTHESIS.md), §§2,5,7–8 | Kalıcı sorumluluk, aktör, katılım, competence ve authority ayrı; koordinatör teknik erişimden ürün karar yetkisi çıkaramaz. | Aynı konuşmadaki tam içerik; bağımsız ajan deneyi değil. |
| Information — [integration I1–I5](../../../research/soul-foundations/07_selection-dynamics-integration-review/SYNTHESIS.md) | İçerik yeterliği, consumer erişimi ve actual kullanım ayrılır; bağlam paketleri aynı geçmişin kopyası değildir. | Aynı konuşmadaki tam içerik; doğal dil bağlam yeterliğinin otomatik oracle'ı yok. |
| Information — [Revision M5](../../../research/soul-foundations/03_ground-deepening/grounds/information/informational-dynamics/derivation-transformation/maintained-information-revision/M5-SYNTHESIS-DECISION-AND-PARENT-DELTA.md), §§2–5 | Yeni kayıt≠kabul edilmiş girdi; bir gerekçenin çekilmesi≠sonucun otomatik iptali; şimdiki özeti korumak≠gelecekteki revizyon için yeterli durumu korumak. §5'in itiraz, alternatif destek ve devir örneğini keskinleştirdi. | v0.3'te tam, 1–95 ile EOF; blob `13d23ff0f67e852f061d66000830b587059117c6`. Sentezin tarihsel proposed etiketi Information STATE'in accepted kapsamıyla birlikte okunur. Araştırmanın dış makaleleri ve deneyleri yeniden açılmadı. |
| [Gas Town META](../../../research/studies/gastown/META.md) → [FINDINGS](../../../research/studies/gastown/FINDINGS.md), §§1–16 | İş, çalıştırma denemesi, kapasite/liveness ve entegrasyon ayrımı; §5C'de farklı kayıt görünümleri. | v0.2'de META tam, FINDINGS 1–280 seçici; v0.3'te aynı görünür içerik kullanıldı. Source pin `649b832`, güncel ürün veya Claude doğrulaması değil. |
| [Superpowers S03](../../../research/studies/superpowers/syntheses/S03-intent-planning-and-context-handoff.md) | Göreve göre brief, global kısıt, kaynak erişimi ve anlamsal devir; inceleyiciyi üreticinin özetine kapatmama. | Aynı konuşmada tam okunmuş study sentezi; insan kapıları ve SDLC aynen alınmadı. |
| [RPD assessment](../../../research/studies/recursive-prerequisite-discovery/ASSESSMENT.md) | Önkoşul keşfi ve kesilmiş sorgunun dönüş noktası; §5D yalnız “devam et” yerine açık soruyu ve beklenen sonucu korur. | Aynı konuşmadaki tam assessment; özgün ekler/prototip yeniden okunmuş veya çalıştırılmış değildir. |
| [Work-management U08](../../../research/studies/work-management-project-control/08-CROSS-UNIT-SYNTHESIS.md) | Farklı bağımlılık, ready/claim/running/done ve geri dönüş anlamları. | Önceki 1–320 seçici kapsam; son enterprise/kapanış bölümü tam okuma sayılmaz. |

v0.2 Gas Town META blob'u `dfe8dd29a38ef7e4f686b358dac77ec8fdfe6fe6`, FINDINGS blob'u `4e376aaf3f45936637125496451d1258325fe310`. CATALOG'un ilgili satırları aday seçiminde kullanıldı; kesilmiş tüm katalog tam okunmuş sayılmadı. v0.3 yeni candidate study veya güncel dış ürün iddiası üretmedi.

**v0.3 preflight:** AGENT ve canonical-work-preflight güncel canonical tam okundu; diğer gerekli protokollerin aynı konuşmadaki görünür tam içerikleri kullanıldı. STATE/HANDOFF yeniden tam; WORK ilk 1–75 görünümünün kesilen sonu 65–170 ile tamamlandı. P3-01 v0.2'nin önceki görünür §§1–8 metni, bu tur 115–EOF ile kalan kısmı tamamlanarak kullanıldı. INDEX/DECISIONS/ACTORS/U002/P1-01/P2-01'in aynı konuşmadaki tam ve değişmemiş içerikleri korundu. Kontrol dosyaları araştırma kanıtı değildir.

**Kanıt sınırı:** Aynı-assistant kaynak yeniden kullanımı ve kurgusal yürüyüş. Yeni runtime, ürün veya çoklu ajan deneyi yoktur. ÖR kimlikleri gerçek iş/koşu/karar kaydı değildir. Mesaj teslimi, kaynak okuması, araç izni, kesinti kurtarma veya bağımsız değerlendirme fiilen doğrulanmadı. Teknik seçim için P1/P4/P6 yükleri sürer.

## 10. Dönüş ve devam

v0.3, mevcut G/Y ayrımını tek bir soru etrafında bağlam paketi, karşı görüş, araştırma katkısı, açık karar, üç kayıt görünümü, kesinti devri ve yeni bilgiyle yeniden değerlendirme boyunca somutlaştırır. Örneğin sonunda araştırma tamamlanabilirken tasarımın açık kalması özellikle korunur. Bu eksiklik kapatılmış deney veya seçilmiş SOUL davranışı değildir.

Kullanıcının yönü olumlu değerlendirmesi kaydedildi; tüm profiller/sözleşmeler accepted yapılmadı. P2/ACTORS ilk taban olarak korunur. P3 kapsamı devam eder, P4'e geçiş yoktur.

**Sonraki bütünlüklü P3 değerlendirmesi:** Bu örnekteki talep, inceleme itirazı ve kararın ne zaman açık/karşılanmış sayılacağı; küçük danışma ile ayrı izlenen katkının sınırı; G/Y arasında hangi gerekçeyle durdurma veya devam hükmü kurulacağı birlikte netleştirilir. §5'teki kayıt görünümleri üzerinden konuşulur; aynı iki koordinasyon ayrımı yeniden anlatılmaz ve örnek gerçek SOUL görevine çevrilmez. Kullanıcının örneğe dair değerlendirmesi öncelikli girdidir.
