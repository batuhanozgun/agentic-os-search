# P3-01 — İş, çalışma alanı ve bilgi sürekliliği

**Üst iş:** [WORK/P3](../WORK.md). **Tarih:** 27 Eylül 2026.  
**Sürüm:** v0.4 — konsolide çalışma taslağı; başlangıç `a2ee26c615361f2c88f58ed2d695c03e9386c206`.  
**Statü:** CONSOLIDATED WORKING DRAFT / DISCUSSION. Kullanıcı içerik sorumluluğu ile çalışma alanının düzen/bakım sorumluluğu ayrımına katıldı; aşağıdaki ayrıntılı işletim sözleşmelerinin tamamını kabul etmiş sayılmaz. P3 kapanmadı; P4–P6 başlamadı.  
**Rolü:** P3'ün güncel tek ayrıntı yüzeyi. Önceki anlatımı tekrar tekrar büyütmek yerine iş, yapı, kayıt ve devam kuralları birlikte düzenlendi. [v0.3](https://github.com/batuhanozgun/agentic-os-search/blob/a2ee26c615361f2c88f58ed2d695c03e9386c206/explorations/EXP-006-development-os-calisma-duzeni/work/P3-01-work-information-discussion.md), rol konuşmaları ve o turların kaynak iziyle korunur.

## 1. Kullanıcı yönü ve önerinin sınırı

P3 başlangıcındaki istek araştırmadan beslenen bir yapı sunmak ve hemen karar vermeden birlikte değerlendirmekti. Kullanıcı ardından işin koordinasyonu ile yapının koordinasyonunun, ürün denetimi ile çalışma düzeni denetiminin ayrılmasını önerdi. v0.2 bu ayrımı, v0.3 kurgusal rol etkileşimini açtı.

Son netleştirme, görünür kullanıcı mesajıdır:

> “Ben belki detay bir noktaya takılacağım ama ben daha çok çalışma düzeninden bahsediyorum, yani etrafın derli toplu olmasından bahsediyorum, işin içeriği değil de işin yapılması aşamasında kullanılan yapının, dosyaların, klasörlerin, düzeninden falan ya da yeniden kullanılabilir olmasından falan. Ama doğru mu düşünüyorum emin değilim. Sen de buna benzer bir şeyden mi bahsediyorsun?”

Assistant içerik sahibinin ne söylendiği/nedeninden; düzen tarafının nerede, hangi statü ve ilişkilerle korunup yeniden kullanılacağından sorumlu olmasını önerdi. Kullanıcının sonraki görünür mesajı:

> “tamam evet aynı fikirdeyim.  
> şimdi bir toplarla P3'ü.  
> devam edelim.”

**Kabulün kapsamı:** Çalışma alanının düzeni, bulunabilirliği, güncelliği, bakımı, devri ve yeniden kullanımı asli sorumluluktur; içerik kararıyla aynı değildir. Bu D021 olarak kaydedilir. Fiziksel klasör ağacı, rol/ajan sayısı, bütün P3 hükümleri veya teknik topoloji kabul edilmiş değildir. Kaynak aktarımı bu görünür mesajlarla sınırlıdır; platform export'u değildir.

**Üst sınır:** Bu dosya SOUL geliştirme backlog'u değil, DevOS'un çalışma düzeni taslağıdır. İlk ve sonraki SOUL işlerini kurulacak ekip keşfeder. Cloud kullanıcı kısıtıdır; teknik seçim P4'te kalır. Kısa sunum, küçük miktarda iş yapmak veya her ayrımda kullanıcı komutu beklemek anlamına gelmez.

## 2. P3'ün birleşik modeli

**Ortak hedef ve iş ağı üzerinde, ihtiyaç etrafında işbirliği; bu işbirliğini sürdüren düzenli ve yeniden kullanılabilir çalışma alanı.**

| Sorumluluk alanı | Ne için var? | Başarı sorusu |
|---|---|---|
| **G — SOUL geliştirme** | Gereken işi keşfetmek, araştırmak, planlamak, tasarlamak, gerçekleştirmek ve değerlendirmek | Doğru işe yöneliyor ve SOUL hedefi için yeterli sonuç üretiyor muyuz? |
| **Y — DevOS işleyişi ve çalışma alanı** | Katılım, iletişim, erişim, bağlam, dosya/kayıt düzeni, bakım, yeniden kullanım ve devri sağlamak | Ekip, doğru çalışma koşullarını ve tekrar kullanılabilir bilgi düzenini gerçekten bulabiliyor mu? |

İkisi de DevOS içinde Work ve reasoning taşır. Y yalnız Claude teknik altyapısı veya Foundation ENVIRONMENT ground'u değildir. Her iki tarafta da WORK, INFORMATION, ACTORS ve ENVIRONMENT ilişkileri bulunur. SOUL'un hafızasını geliştirmek G; geliştiren ekibin kendi kayıtlarını işletmek Y'dir. Konunun adı değil hedef nesne belirleyicidir.

İki alan iki kapalı takım, iki repository veya zorunlu iki lead değildir. F1–F8 başarı yönleriyle G/Y hedefleri farklı eksenlerdir. Genel rol yetkinliği gerektiğinde iki hedefte ayrı görevlendirmelerle kullanılabilir; ortak isim, aynı uzmanlık veya bağımsızlık garantisi değildir.

## 3. Roller, sahiplik ve iki koordinasyon

[ACTORS](../ACTORS.md) ve [P2-01](P2-01-named-role-contracts.md) DR01–DR16 ilk sözleşme tabanını korur. Aşağıdaki profiller P3 taslak düzeltmesidir; yeni bir kabul edilmiş ajan sayımı değildir.

| Rol/taban | P3'te taşıdığı sorumluluk |
|---|---|
| DR01 İş Keşfi ve Planlama | Diğer rollerin de keşfettiği ihtiyaçları amaç, gerekçe, alternatif, önkoşul ve yaşayan planda bütünleştirir. İlk işi assistant dışarıdan vermez. |
| DR02 Kapasite / DR03 Sistem Bütünlüğü Tasarımcıları | Konuya uygun uzmanlıkla yerel tasarımı ve alanlar arası uyumu taşır. DevOS yapısına değişiklik gerekirse ayrı ve yetkili hedefle çalışırlar. |
| DR04 Sınama Tasarımcısı / DR05 Uygulama Geliştiricisi / DR11 Sınama Yürütücüsü | Sınama yolu, gerçek üretim ve koşu kanıtı ayrı katkılardır. Her birinin G veya Y hedefi, sürümü ve yetkisi açık olur. |
| **DR06-G SOUL Geliştirme Koordinatörü** | Hangi katkı neyi bekliyor, öncelik nedir, sonuçlar üst işe nasıl birleşecek? Ürün/plan sahipleriyle iş sırasını işletir; bütün teknik kararları üstlenmez. |
| **DR06-Y DevOS İşletim Koordinatörü** | Katkıyı uygun koşullarda etkinleştirme, çalışma denemesi, kapasite, bakım ve devamı koordine eder. Ürün önceliğini veya kalite ölçütünü sessizce değiştirmez. |
| **DR07 Bilgi Sorumlusu — çalışma alanı bakım kapsamıyla** | Dosya/kayıtların mantıksal yeri, tek yetkili kaynağı, statüsü, kaynak/sürüm bağı, indeksleri, arşiv ve tekrar kullanım bulunabilirliğini korur. İçeriğin doğruluk hakemi veya bütün dosyaların tek yazıcısı değildir. |
| DR08 Bağlam Kurucusu | İş sahibi/uzmanla gerekli görünümü oluşturur; kaynaklara dönüş, sürüm ve eksikleri korur. Herkese bütün geçmişi göndermek veya özeti yeterli saymak yoktur. |
| DR09 Rol ve Katılım / DR10 Ortam İşleticisi | Katılım bağını ve gerçek araç/erişim/ortam işlemlerini ayrı taşır. Assigned/active etiketi gerçek yeterlik, grant veya çalıştırma değildir. |
| DR12 Yetki ve Kontrol | Meşru kapsam/delegasyon/etki sınırları; her rutin işte müşteri onayı istemek değil. Teknik erişimden veya rol isminden yeni yetki çıkmaz. |
| **DR13-G SOUL Geliştirme İnceleyicisi** | İş seçiminin, tasarımın, uygulamanın ve sonuç iddiasının yeterliğini alan uzmanlığı ve uygun kanıtla sınar. |
| **DR13-Y DevOS İşleyiş İnceleyicisi** | Çalışma alanının gerçekten kullanılabilir, güncel, bulunabilir ve devralınabilir oluşunu; gereken iletişim/katılım/izin bağlarını sınar. Temiz görünen klasör yeterli değildir. |
| DR14 Teşhis / DR15 Öğrenme ve Yöntem / DR16 Araştırmacı | Olayın neden/etkisi, deneyimden yöntem değişikliği ve kaynaklı bilgi sonucu ayrı teslimatlardır. G/Y hedefi açık tutulur; öz-değişiklik veya ürün benimseme yetkisi kendiliğinden oluşmaz. |

**İçerik sahibi:** Araştırmacı bulgusunu, tasarımcı kararını, geliştirici uygulamasını, inceleyici hükmünü ve gerekçesini üretir. Y tarafı anlamı yeterince anlayarak düzenler; yerleştirme veya isim düzeltmesi bahanesiyle içerik hükmünü değiştirmez. Üreticiler de bakım işini bütünüyle başka role atıp sahipsiz çıktı bırakamaz.

**Karar sahibi işte belirtilir:** İş/önkoşul planını DR01, alan tasarımını ilgili DR02, alanlar arası tasarım uyuşmazlığını DR03 kendi yetki kapsamında ele alır. DR06-G öncelik ve iş ilişkilerini; DR06-Y verilmiş politika içindeki çalıştırma/bakım seçeneklerini işletir. DR13 kanıt hükmünü idari tercih uğruna olumluya çeviremez. Kapsamı aşan gerçek principal kararı DR12 üzerinden Batu'ya döner; her teknik anlaşmazlık müşteriye aktarılmaz.

## 4. Çalışma alanında ne nerede yaşar?

Bu tablo **mantıksal yerleşim önerisidir**, şu anda açılacak klasör ağacı veya depolama ürünü değildir. P4 gerçek erişim/yazma koşullarıyla fiziksel karşılığını seçecektir.

| Mantıksal alan | Korunan içerik | Karışmaması gereken |
|---|---|---|
| **SOUL ürün alanı** | Ürünün tasarım, tanım, kod ve diğer teslimatları; geçerli sürüm ve aday değişiklik bağı | DevOS'un kendi rol talimatı/işletim kuralı ürüne sessizce eklenmez. |
| **DevOS iş ve devam alanı** | Hedef/plan, aday ve etkin işler, talepler, beklemeler, itirazlar, çalışma denemeleri, devir | İşin durumu ile onu çalıştıran oturumun durumu aynı değildir. |
| **Kaynak, karar ve kanıt birikimi** | Araştırma rotaları, bulgular, karar gerekçeleri, inceleme ve test kanıtları | Erişilebilir yetkili kaynak gereksiz yere kopyalanmaz; üretilmiş yorum kaynakla eşitlenmez. |
| **DevOS çalışma tarifleri ve tekrar kullanım kütüphanesi** | Rol sözleşmeleri, yöntemler, şablonlar ve araç tarifleri; hangi koşulda kullanılacakları | Bir işte işe yarayan taslak otomatik genel kurala veya etkin agent talimatına yükselmez. |

Taslak, geçerli, yerini yenisi almış ve arşivlenmiş olma **yaşam döngüsü statüleridir**; her alanın ayrı kopyasını açma emri değildir. Aynı bilgi için bir yetkili kaynak, gerektiğinde ona bağlı açıkça türetilmiş görünümler olmalıdır. Arşiv geçmiş gerekçe için bulunabilir kalabilir; current okuma yoluna yanlışlıkla karışmamalıdır.

Her kalıcı nesne için gerektiği ölçüde şu sorular cevaplanır: Neye ait? Sahibi kim? Taslak mı, geçerli mi? Hangi kaynak/karar/sürümle bağlı? Nereden bulunur? Kim kullanacak? Açık işse neyi bekliyor ve nereye dönülecek? Her dosyaya büyük bir zorunlu form doldurma kararı verilmez.

## 5. İş, talep ve karar nasıl ilerler?

### 5A. Hedeften işe; hazır backlog olmadan

Ekip yetkili hedefi, mevcut araştırmayı ve sonuçları devralır. Her rol ihtiyaç veya bilgi açığı gösterebilir; DR01 bunları gerekçeli iş ağına dönüştürür. Bir işten doğmak, onu engelleyen önkoşul olmak ve aynı hedefe katkı vermek farklı ilişkilerdir. Bütün gelecek plan bitmeden, önkoşulları sağlanmış sınırlı araştırma başlayabilir. Başlangıç rol/grant/okuma yolu P4/P5'te kurulur; roller birbirini sonsuz biçimde yetkilendirmez.

### 5B. Danışma ile ayrı katkı

Mevcut işin kapsamı ve yetkisi içinde sonuçlanacak kısa danışma aynı iş altında izlenebilir. Ayrı sorumlu, bekleme/devir, anlamlı kaynak yükü, başka işe bağımlılık veya ayrı kabul koşulu doğuyorsa katkı ayrı kimlikle izlenir. Her mesaj için dosya veya iki koordinatörden onay gerekmez.

Talep; soruyu, neden gerektiğini, bağlı işi/kararı, beklenen teslimatı, gerekli uzmanlığı, kaynak/target sürümünü, tüketiciyi ve dönüş noktasını taşır. Var olan kayda bağlantı yeterliyse yeniden kopyalanmaz. Yanıt farklı soruyu cevaplıyorsa veya kaynağa ulaşamadıysa talep sessizce karşılanmış sayılmaz.

### 5C. Tek bir DONE yerine ayrı anlamlar

| Değişen durum | Kim karşılığını taşır? | Hangi sonuç çıkarılamaz? |
|---|---|---|
| Katkı istendi / üst işle bağlandı | Talep sahibi ve DR06-G | Araştırma başladı denemez. |
| Atandı / çalıştırma denemesi başladı | DR06-Y ve katılım/ortam sorumluları | Gerekli bilgi gerçekten kullanıldı denemez. |
| Yanıt veya ürün teslim edildi | Katkı sahibi | Üst karar, ürün veya kullanım tamamlandı denemez. |
| Kullandım / gerekçeli reddettim / ek katkı gerekiyor | Talep sahibi; gereken iddiada inceleyici | Mesaj alındı onayı teknik yeterlik değildir. |
| Karar veya iş kapanışı gerekçelendirildi | Yetkili karar/iş sahibi ve gereken güvence | Müşteri kabulü veya bütün SOUL hedefinin tamamlanması değildir. |

Bunlar tek doğrusal zorunlu state machine değil, birbirine karıştırılmaması gereken durum iddialarıdır. Gerekçeli iptal/erteleme de mümkündür; erişim engeli veya zaman bitmesi başarılı tamamlanma yapılmaz. Üst işin kapanış koşulu ayrıca değerlendirilir.

### 5D. Görüş ayrılığı, durdurma ve devam

İtirazda hedef iddia, gerekçe/dayanak, beklenen cevap ve sahibi görünürdür. Eksik/çelişkili olgu kaynak veya uygun sınamayla araştırılır. Yalnız tasarım tercihleri çatışıyorsa yetkili alan sahibi alternatifleri ve trade-off'u kaydederek seçim yapabilir. Olgusal karşı kanıtı çoğunluk oyu veya teslim baskısıyla bertaraf edemez.

İtiraz; karşılandığında, gerekçeli reddi kaydedildiğinde, öncül geri çekildiğinde veya açık kapsamıyla ertelendiğinde bir karşılık bulur. Kararı taşıyan çözülmemiş ihlal/kanıt açığı olumlu kalite hükmüyle örtülemez. Her itiraz sınırsız veto değildir; durdurma yetkisi kapsamla tanımlanır.

G tarafı içerik/bağımlılık nedeniyle ilgili işi bekletir. Y tarafı yanlış girdi, kayıp kayıt, yetki veya gerçek ortam engelinde ilgili çalıştırmayı verilen yetki içinde tutar. İlgisiz işler otomatik durmaz. Y kapasite yetersizliğini ve seçenekleri bildirir; ürün önceliği G'de kalır. Gerçek kullanıcı durdurması normal ilerleme kuralıyla aşılmaz.

## 6. Çalışma alanı bakımı işin içine nasıl girer?

**Yeni somut çalışma sözleşmesi adayı:** Maddi bir çıktı yalnız üretilmiş olduğu için devredilmiş sayılmaz; doğru yeri, sahibi, statüsü, kaynak bağı ve tüketici yolu da korunmalıdır. Bu, her adımda ayrı bakım ajanı çağırma şartı değildir.

| Olay | İçerik/iş tarafının katkısı | Düzen tarafının katkısı ve devam koşulu |
|---|---|---|
| **İş açılması / görevlendirme** | Amaç, kapsam, katkı ve teslimat sahibi; gerekli bilgi ihtiyacı | Mevcut kayıt/kütüphane önce aranır; gerekirse yeni nesneye tek ev/kimlik verilir. Geçerli rol ve yeterli kaynak görünümü sağlanır. |
| **Taslak/yanıt üretimi** | İçerik, gerekçe, dayanak ve belirsizlik; hedef sürüm | İşle bağlantısı ve taslak statüsü korunur. Kalıcılaştırılmış olması kabul edilmiş anlamına gelmez. |
| **Geçerli kullanım / devir** | Gerekli içerik kararı ve uygun inceleme; sonucun kullanım karşılığı | Doğru sürüm, current giriş ve tüketici bağı birlikte güncellenir. Tamamlanmamış yayın ayrı açık durumdur; eski okuyucular yanıltılmaz. |
| **Yeni sürüm / eşzamanlı yazma** | Değişen anlam ve etkiyi ilgili alan sahibi çözer | Eski temele dayanan çıktı current kaydı körlemesine ezmez. Çatışma ayrılır; seçilen sürüm ve ona bağlı indeksler uzlaştırılır. Mekanik kilit/atomiklik P4/P5 seçimi olacaktır. |
| **İş kapanışı / kesinti** | Üst işin durumu, açık itiraz/katkı, sonraki ihtiyaç ve geri dönüş | Geçici çıktı, kalıcı dayanak, current kayıt ve arşiv ayrılır; bekleyen talep/deneme ve okuyucunun giriş yolu korunur. Kozmetik temizlik bütün ilerlemeyi bloke etmez. |
| **Yeniden kullanım** | DR15 ve ilgili uzman, hangi kullanımın gerekçeli olduğunu ve sınırını değerlendirir | DR07/08 bulunan tarifi, kaynak sürümünü ve uygun bağlamı sağlar. Sahibi, kapsamı ve yeniden kontrol koşulu olmayan çıktı genel kütüphane kuralı yapılmaz. |
| **Taşıma / sadeleştirme / arşiv** | Kaybolmaması gereken anlam, karar ve kanıt bağı belirlenir | Bağlantı/indeks/current okuma yolu onarılır; eski kopya yanlışlıkla yüklenmez. Geri alınabilirlik ve gerekli geçmiş korunur; yetkisiz silme yoktur. |

**Bakımın tetikleri:** Yeni kalıcı çıktı, ilgili statü/karar değişimi, taşınan kaynak, bulunan çelişki, iş kapanışı, oturum devri ve tekrar kullanım isteği. Bunlar semantik tetiklerdir; hook/daemon seçilmedi. Aynı konu için her tur tüm depoyu taramak veya dosya sayısını azaltmayı başarı ölçütü yapmak önerilmez.

**İki bakım yoğunluğu:** Yanlış current kaynak/izin, açık işi kaybettiren devir veya zorunlu kanıt bağı sorunu ilgili tüketimi durdurabilir. Adlandırma estetiği veya zararsız fazlalık sınırlı bakım kuyruğuna alınabilir. Düzen ürünü geliştirme işinin yerine geçmez; fakat işleyişi bozduğu yerde isteğe bağlı dekorasyon da değildir.

**Yeniden kullanılabilir kayıt:** Ne işe yarar; hangi koşulda işe yaramaz; kaynak/sürüm/kanıt; kim bakar; nasıl çağrılır; hangi değişiklikte yeniden değerlendirilir? Aranabilirlik ve başarılı yükleme, yararlı yöntem olduğunun kanıtı değildir. Mevcut iyi şablonu kullanmak, her işte yeni şablon üretmekten önce değerlendirilir.

## 7. Girdi, güncelleme ve oturum devri

Bir rolün girdisi, bütün konuşmanın kopyası değil; rol sözleşmesi + yetkili hedef/kısıt + mevcut iş/soru + gerekli karar/kaynak/ürün sürümleri + açık eksikler + çıktı/tüketici/dönüş bağıdır. DR08 ile uzman birlikte yeterliği kurar. İnceleyici üreticinin özetine hapsedilmez; gereken asıl kaynağa erişebilmelidir. Kaydın varlığı, exposure ve actual kullanım ayrı kalır.

Yeni bilgi geldiğinde DR07 ilişkili kayıt ve tüketicileri belirler; uzman hangi gerekçenin veya kararın değiştiğini değerlendirir. Bir dayanak çekildi diye alternatif destekle geçerli kalan karar otomatik iptal olmaz. Eksik bağımlılık kaydı, etki yok demek değildir. DR08 yeni görünümü ulaştırır; ilgili G/Y işleri yeniden açılır. Eski veriye dayanan geç yanıt korunabilir ama current sonucu sessizce ezemez.

**Kesinti için yeterli devam kaydı:** Mevcut amaç ve iş; kaynak/sürüm; yapılan/henüz yapılmayan; açık itiraz ve beklenen katkı; sahip; dönüş noktası; çalışma denemesi ve belirsiz yan etki; devam/durma sınırı. Sadece “sıradaki adım” cümlesi veya bütün sohbet dökümü bunun yerine geçmez.

Y yeniden girişte gerçek deneme, erişim, girdi ve etki durumunu uzlaştırır; G amaç, plan ve açık hükmü devralır. Kayıt geri getirmek dış etkiyi geri almış olmak değildir; belirsiz etkiyle kör retry yapılmaz. Batu gerekirse yeniden başlatır, her rolün sırasını yeniden tarif etmez.

## 8. Bir bütünlük kontrolü — canlı test değil

[v0.3 §5](https://github.com/batuhanozgun/agentic-os-search/blob/a2ee26c615361f2c88f58ed2d695c03e9386c206/explorations/EXP-006-development-os-calisma-duzeni/work/P3-01-work-information-discussion.md#5-somut-çalışma-örneği--soru-karşı-görüş-kayıt-ve-devam) kurgusal araştırma→itiraz→karar→devri ayrıntılı gösterir. ÖR kimlikleri hâlâ gerçek backlog değildir. Bu revizyon çalışma alanı bakımını şu karşı vakalarla nitel olarak karşılaştırdı:

| Karşı vaka | Taslağın vermesi gereken karşılık |
|---|---|
| İçerik doğru, current giriş hâlâ eski sürüme gidiyor | İçerik güvencesi Y kusurunu kapatmaz. Giriş/bağ onarılır; ilgili tüketim hazır sayılmaz. |
| Dosyalar düzenli, kanıtsız tasarım onaylanmış | Y düzeni G doğruluğu değildir; kanıt ve yetkili içerik kararı tekrar açılır. |
| İki rol aynı eski sürümden farklı güncelleme getiriyor | İki aday korunur; anlamsal çatışmayı alan sahibi çözer, Y seçilmiş yayını/indeksi uzlaştırır. Son gelen kazanır yoktur. |
| Arşiv/yedek kopya aktif aramada tekrar seçiliyor | Fiziksel taşıma yeterli değildir; current keşif/yükleme ve eski referanslar kontrol edilir. |
| Bir kere işe yarayan yöntem bütün işlere zorlanıyor | Kullanım kapsamı ve karşı örnek/kanıt değerlendirilir; kullanılma sayısı genel etkinlik değildir. |
| Araştırma teslim edilmiş, onu isteyen rol kesilmiş | Açık tüketim/dönüş bağı yeni görevlendirmeye taşınır; geçerli araştırma gereksiz tekrarlanmaz. |
| Kozmetik düzenleme beklediği için bütün SOUL geliştirme durmuş | Y kusuru risk ve etkiyle sınırlanır; ilgili olmayan işler ilerler. |

Bu tablo beklenen davranış sözleşmesidir; koşulmuş test veya bağımsız doğrulama değildir. Doğru klasör isimleri, ayrı ajan etiketleri veya iki yeşil inceleme bütünleşik başarıyı kanıtlamaz.

## 9. Araştırma katkısı ve okuma sınırı

**Yeni hedefli reuse:** [Hermes META](../../../research/studies/hermes-agent/META.md) ve [Note30](../../../research/studies/hermes-agent/notes/30-SKILL-LIBRARY-LIFECYCLE.md) bu tur tam okundu; blob'lar `03c10aeac8e16ac738b29e9c53bafcc145a88baa`, `26b9773cce8e3bb40cbc845df1b538f735fc698d`. CATALOG'un daha önce görülen ilgili Hermes satırıyla seçildi. Note30, eski `c4a5dee` incelemesinin türetilmiş kaydıdır; bugün Hermes/Claude ürünü yeniden doğrulanmadı, bağlı alt kaynakların hepsi yeniden okunmadı.

**Somut katkı:** Arşiv/yedek dosyasının fiziksel yer değiştirmesi ile aktif list/index/load'dan çıkması ayrı; bakım yetkisi yazarlıkla aynı değil; geri alma yalnız geri yüklenen kapsamı kapsar; bir becerinin yüklenmesi yararlı kullanım kanıtı değildir. Bu nedenle §6'ya aktif keşif kontrolü, sahip/kapsam ve yeniden kullanım yeterliği eklendi. Hermes kurulmadı veya seçilmedi.

Önceki P3'ün görünür kaynak okumaları yeniden kullanıldı: [Work synthesis](../../../research/soul-foundations/03_ground-deepening/grounds/work/synthesis/WORK-GROUND-AUDIT-SYNTHESIS.md), [Actors synthesis](../../../research/soul-foundations/03_ground-deepening/grounds/actors/synthesis/ACTORS-GROUND-AUDIT-SYNTHESIS.md), [Information I1–I5](../../../research/soul-foundations/07_selection-dynamics-integration-review/SYNTHESIS.md), [Revision M5](../../../research/soul-foundations/03_ground-deepening/grounds/information/informational-dynamics/derivation-transformation/maintained-information-revision/M5-SYNTHESIS-DECISION-AND-PARENT-DELTA.md), [RPD assessment](../../../research/studies/recursive-prerequisite-discovery/ASSESSMENT.md), [Superpowers S03](../../../research/studies/superpowers/syntheses/S03-intent-planning-and-context-handoff.md), Work-management U08 ve Gas Town'un önceki seçici kapsamı. Tamlık, tarih ve özgün kaynak sınırları [v0.3 §9](https://github.com/batuhanozgun/agentic-os-search/blob/a2ee26c615361f2c88f58ed2d695c03e9386c206/explorations/EXP-006-development-os-calisma-duzeni/work/P3-01-work-information-discussion.md#9-araştırma-katkısı-ve-gerçek-okuma-kapsamı)'da korunur; yeni tam corpus okuması iddiası yoktur.

Work: bakım da iş; kayıt işin gerçekliği değil. Actors: sorumluluk/katılım/yetki ayrı. Information: source→view→use, sürüm ve gelecekteki revizyon durumu ayrı. RPD: bitmemiş sorgu/dönüş. Superpowers: anlamlı brief ve devir. Gas Town: iş ile çalıştırma denemesi farklı. Bu girdiler öneri üretir; kurulum seçimi veya yöntem üstünlüğü kanıtı değildir.

**Canonical kapsam:** Başlangıç main `a2ee26c`. AGENT güncel tam okundu; gerekli protokollerin aynı konuşmadaki tam içerikleri korundu. STATE/HANDOFF/WORK, U002 ve P1-01 yeniden tamamlandı; P1'in kesilen geçişi 78–89 ile kapatıldı. P3'ün yeni baş/son bölümleri ile aynı sürümün önceki görünür gövdesi birlikte kullanıldı. INDEX/DECISIONS/ACTORS/P2'nin değişmemiş görünür içerikleri korundu. Kontrol dosyaları araştırma kanıtı değildir. Canlı runtime, mesaj, izin, dosya yarışı veya restore deneyi yapılmadı.

## 10. P3'ün durumu ve bir sonraki bütünlüklü iş

**Toparlanan:** G/Y sorumlulukları; iki koordinasyon ve güvence; içerik sahibi–düzen sahibi ayrımı; mantıksal bilgi alanları; talep/itiraz/karar durumları; çalışma alanı bakım tetikleri; yeniden kullanım ve kesinti devri. Bunlar tek taslakta bulunur, yeni yan çalışma paketi açılmadı.

**Bu tur ilerletilen:** Kullanıcının dosya/klasör/düzen vurgusu, olay→sorumlu→kalıcı karşılık→devam koşulu sözleşmesine dönüştürüldü. Talep teslimi ile kullanımı; önemli engel ile kozmetik bakım; arşiv ile aktif keşiften çıkma; içerik çatışması ile yayın çatışması ayrıldı. D021 dışındaki yeni ayrıntılar adaydır.

**P3'te kalan tek bütünlüklü sınama:** İki eşzamanlı işin ortak kaydı değiştirdiği, bir inceleme itirazı açıkken oturumun kesildiği durumu bu sözleşmelerle baştan sona izlemek. Amaç yeni rol/şema üretmek değil; her geçişte yetkili sahip, tüketici, kalıcı durum ve sonraki tetik var mı; gerekli bilgi ve karar yolda kayboluyor mu sorusunu kapatmaktır. Bu sınırlı karşılaştırmada maddi semantik açık kalmazsa P3 tasarım kapanışına hazırlanır ve P4 seçim gereksinimleri sabitlenir. Yeni karşı kanıt yokken art arda genel audit turları açılmaz.

**P4'e devredilecek teknik yükler:** Gerçek actor allocation ve alt ajan/takım; fiziksel dosya/klasör yerleşimi; çağrı/mesaj/yayın mekanizması; çakışma/izin/kalıcılık; ilk başlatma. P5 bunları gerçekleştirir, P6 davranış ve başarısızlık yollarını sınar. P3 metnindeki requirement'lar kendiliğinden çalışan kontroller değildir. P4 bu tur açılmadı; kullanıcı tarafından seçilmiş SOUL görevi veya mimari uydurulmadı.
