# Concepts — Çalışma yöntemi

Sürüm: v0.2-draft, 2026-09-19. Statü: ilk pilot değerlendirmesiyle açıklığa kavuşturulmuş taslak; revizyon ikinci pilotta sınanacak, genel olarak doğrulanmış yöntem değil. Amaç CHARTER.md, kaynak talep ORIGIN.md, güncel aşama/yetki STATE.md, yürütme sırası PLAN.md içindedir. Bu proje yöntemidir; agent-control kaynağı AGENT.md ve tetiklenen protokollerdir.

## 1. Çalışmanın birimi ve kapsamı

İlk aşamanın birimi, bir terimin belirli bir araştırmada belirli bağlamdaki kullanımıdır. Sözcük tek başına kavram kimliği değildir. Önceden hazırlanmış terim listesi, ürün sınıflandırması veya evrensel katman şeması başlangıç filtresi yapılmaz. Kullanıcının su/agent/ürün/arayüz örnekleri bu korpusa başlangıç girdisi değildir.

Kaynak araştırmalar research/studies/ altında yerinde kalır. Koleksiyon ve alt çalışmalarının ilişkisi korunur; aynı dosya veya türetilmiş sentezler bağımsız destekler gibi sayılmaz. Taşınma işaretçisi ayrı araştırma değildir. Bununla birlikte her mevcut dosya kapsam envanterinde hesabı verilerek ele alınır; kaynak taşınma notu da bağlam bakımından okunur.

Yeni bir araştırmaya girerken:

1. Güncel main kimliğini ve ilgili dosya ağacını kaydet. CATALOG keşif içindir; gerçek dosya envanterinin yerine geçmez.
2. Paket META/STATE/INDEX üzerinden amaç, kaynak sınırı, araştırma tamamlanma durumu ve gerekli okuma yolunu geri kazan.
3. Araştırma kapsamındaki bütün dosyaların listesini oluştur; iç içe dosyalar, kanıtlar, kaynak kayıtları, yöntem/ilerleme dosyaları ve ekleri gözden kaçırma.
4. Dosyaları tam oku; önceki araştırmanın kavramlarını yeni pakete varsayılan anlam olarak taşıma. Kaynak-native dil ile önceki araştırma yazarının açıklama dili ayrıca ayrılır.

İndeks okumak tam paket okuması değildir. Baytların indirilmesi, araç çıktısının getirilmesi veya anahtar sözcük araması da tam okuma değildir. Araç çıktısı kesilmişse eksik aralıklar tamamlanır. Görsel/işitsel/binary eklerde erişilebilen temsil ve sınır açık tutulur; yalnız transkript erişimi tam ses incelemesi sayılmaz. Okunamayan materyal sessizce atılmaz veya tamamlandı işaretlenmez.

## 2. İki ayrı iz: okuma ve yorum

Kalıcı çıkarım başladığında önerilen düzen:

- concepts/studies/<kaynak-araştırma-yolu>/READING.md: dosya/sürüm envanteri, okuma aralıkları, eksikler ve devam noktası.
- Aynı alanda TERMS.md: bağlamlı kullanım kayıtları ve değişiklik izleri.

Bunlar denemelerden sonra kesinleşecek yerleştirme seçimleridir. Büyük dosyalar kaynak/kullanım kimlikleri korunarak bölünebilir; tek dev dosya veya gereksiz dosya çoğaltma zorunlu değildir. Pilotların terim çıktıları sohbet içinde kalır; hazırlık aşamasında bu dizinler doldurulmaz.

Okuma kaydı en az kaynak repo/ref, dosya yolu, mümkünse blob SHA, gerçekten görülen aralık/temsil ve son tam okuma durumunu taşır. Tek dosya kısmen okunmuşsa son satır/bölüm nettir. Gözden geçirilmiş ile tam okunmuş ayrıdır. Dosya envanterinde bulunmak, içeriğinin okunmuş olması değildir.

Yorum kaydı ise aşağıdaki ayrımları taşır. Kolon adları esnektir; anlamların kaybolması esnek değildir.

| Kayıt ihtiyacı | Anlamı |
|---|---|
| Kullanım kimliği ve özgün ifade | Yazım, kısaltma ve adlandırma korunur. Kimlik bir kullanım kaydını adresler; kabul edilmiş kavram kimliği değildir. |
| Kaynak noktası | Repo/ref + dosya + bölüm/satır; kısa alıntı veya kaynak bağlantılı bağlam. Haricî asıl kaynak biliniyorsa ayrı bağlanır. |
| Söyleyen/katman | İncelenen yapının kendi belgesi, aktarılan dış kaynak, önceki araştırma yorumu veya yeni çıkarım yorumu. Bir araştırmadaki cümle otomatik olarak ürünün kendi tanımı değildir. |
| Bu bağlamda karşılık | Ne anlatıldığı; biliniyorsa kapsam ve komşu kullanımlarla ilişki. Kaynağın tanımıyla assistant açıklaması ayrı tutulur. |
| Kanıt ve belirsizlik statüsü | Açık kaynak ifadesi / bağlamdan yorum / çözülememiş. Tanım varlığı, tanımın evrensel doğruluğu değildir. Kaynağın olgusal doğruluğu bu etiketle sertifikalanmaz. |
| Önceki kayıtla ilişki | Aynı kullanımın ek kaynak noktası, ayrı anlam, aday benzerlik veya çelişki. Eş anlamlılık erken kabul edilmez. |
| Maddi değişiklik | Önceki yorum, yeni yorum, kısa gerekçe/dayanak ve etkilenen kayıtlar. Sessiz yeniden yazma yapılmaz. |

Bu iz bir ham düşünce günlüğü değildir. Denetlenebilir gözlem, sonuç, önemli alternatif, belirsizlik ve kısa gerekçe yeterlidir. Her küçük cümle için kayıt yükü üretmeden karar bakımından önemli anlam değişiklikleri korunur.

## 3. Okurken çıkarım yapmak

Kaynakta adı verilen teknik yapılar, roller, işlevler, süreçler, durumlar ve ilişkiler terim/jargon adayı olabilir; bunlar zorunlu kategori listesi değildir. Yalnız kullanıcı örnekleri veya yaygın AI sözcükleri aranmaz. Yeni ad üretmeden, karşılaşılan kullanım çıkarılır. Adlandırılmamış bir ayrım görülürse adsız gözlem olarak not edilebilir; birinci aşamada yeni evrensel kavram ilan edilmez.

Kayıt okuma sırasında yapılır. Her şeyi sonradan hafızadan çıkarmak veya yeni bir terim nedeniyle bütün paketi genel kavram araştırmasına çevirmek bu yöntemin dışındadır.

Aynı ifade farklı bağlamlarda farklı şeyleri anlatıyorsa kullanımlar ayrı tutulur. Aynı kullanımı tekrarlayan pasajlar kaynak noktaları eklenerek ilişkilendirilebilir. Aynı yazım, aynı anlam kanıtı değildir; farklı yazım da farklı kavram kanıtı değildir. Çeviri/kısaltma birleştirmeleri gerekçesiz yapılmaz.

Kaynakta açık tanım yoksa sırf tamamlamak için dışarıdan tanım eklenmez. Dış kaynağa dönmek, mevcut kullanımın kritik anlamını geri kazanmak için sınırlı bir kaynak okuması olabilir; genel tanım araştırması veya kaynak yapının canlı davranış testi olmaz. Daha büyük ihtiyaç açık soru olarak korunur.

Araştırmalar arasındaki olası eşleşme sonraki değerlendirme için işaretlenebilir, ancak bütün çıkarımlar bitmeden ortak tanım, global taksonomi veya yerel kabul kararı üretilmez.

## 4. Her turda çalışma belleğini geri kazanma

Tur başında güncel STATE, mevcut araştırmanın okuma/yorum kayıtları ve gerekli kaynak derinliği geri kazanılır. Yeni oturumda INDEX'in tam cold-start yolu izlenir. Eski sohbette hatırlanıyor olması kayıt veya kaynak okumaya eşdeğer değildir.

İki neden görünür tutulur: kullanıcı anlam seçimlerini okuma anında denetleyemiyor; ortak sözcükler aynı anlamı ve teknik doğruluğu garanti etmiyor. O turdaki önemli yorum/eksik/değişim varsa somut olarak açıklanır. Hatırlatma bir kontrol sonucu değildir.

Sonraki okuma önceki yorumu değiştirirse:

1. Yeni kaynak noktasıyla fark belirlenir.
2. Eski kaydın hangi kapsamda değiştiği kısa gerekçeyle işaretlenir.
3. Ona dayanan ilgili kayıtlar kontrol edilir; yanlış yorumun yayılımı bırakılmaz.
4. Etki henüz kontrol edilmediyse açık iş olarak taşınır; tüm düzeltme bitmiş sayılmaz.

Turu kapatmadan gerçekten okunan kapsam, üretilen/değişen kayıtlar, açık eksikler ve tam devam noktası görünür hale getirilir. Operasyonel sınır, kaydı ve handoff'u kaybetme gerekçesi değildir; bunun için pay bırakılır.

## 5. Tamamlanma ve değişen korpus

Bir araştırmanın terim çıkarımının tamamlanması şu koşullara bağlıdır: envanterdeki her dosyanın durumu açıklanmış; ilgili içerik tam okunmuş; kullanım kayıtları kaynaklarına bağlanmış; maddi yorum değişikliklerinin etkisi kontrol edilmiş; okunamayan kapsam açıkça çözülmüş olmalıdır. Terimin anlamının çözülememesi doğru kaydedilmişse bu, kaynağın okunmadığı anlamına gelmez.

Kaynak araştırmasının kendisi planlı veya kısmi olabilir. Mevcut dosyalarından çıkarım yapmak, o yapının tamamını bilmek değildir. Kaynak araştırmasının STATE'i ile concepts çıkarım durumu ayrı tutulur. İlgili tüm araştırma materyali okunur; henüz yapılmamış araştırma varsayılarak doldurulmaz.

Tamamlanma iddiasından önce envanter yeniden kontrol edilir. Eklenmiş/değişmiş dosyalar delta listesine alınır; eski kayıtlar yeni sürüme sessizce yükseltilmez. Sürüm kapsamı kullanıcı açısından maddi biçimde değişiyorsa aşama/kapsam kararı görünür kılınır. Okunamayan dosya veya bekleyen araştırma kapsamı yüzünden bilinmeyen şey, sıfır terim veya eksiksiz yapı bilgisi sayılmaz.

Bütün araştırmalar için ikinci aşama giriş kontrolü: kapsam sürümü açık; tüm paket/alt paketler hesaba katılmış; maddi yeni/değişmiş içerik işlenmiş; engeller kapatılmış veya açıkça yetkilendirilmiş kapsam kararıyla sınırlandırılmış; tüm çıkarım kayıtları okunabilir. Yalnız dosya sayısı veya terim sayısı başarı ölçütü değildir.

## 6. Yöntemi sınamak ve ikinci aşama

İki pilot, gösterim değil yöntem sınamasıdır. Kaynak tarafına geri dönüp çıktıdan bağımsız seçilmiş bölümlerde atlanmış kullanım, yanlış atıf, anlam birleştirme ve yorum değişimi kaybı aranır. Aynı assistant'ın ikinci okuması bağımsız doğrulama diye sunulmaz. Pilot sonrası değişmiş yöntem, aynı pilot tarafından geriye dönük doğrulanmış sayılmaz; ikinci pilot yeni bir sınama sağlar, evrensel yeterlilik kanıtı değil.

İkinci aşamada bütün çıkarımlar tam okunur; hangi anlamların ayrılacağı, hangi adların kullanılacağı ve nerede ortak kapsam kurulabileceği değerlendirilir. Örnek, karşı örnek, kapsam dışı durum, komşu kavram ve bağlama bağlı kullanım sınanır. Basitleştirme önemli ayrımları gizleyemez. Kullanıcıya gerekli somut ayrımlar açıklanır; onayı teknik uzman testi sayılmaz. Öneri, sınanmış açıklama, yerel kabul ve hâlâ açık durum ayrı kaydedilir.

İkinci aşamanın ayrıntılı kayıt şeması ilk aşama çıktıları oluşmadan dondurulmaz. Kaynak anlamı hiçbir yerel kabul nedeniyle değiştirilmez; mimari ve uygulama kararı ayrıca yetki/kanıt gerektirir.

## 7. İlk pilotun B2 değerlendirmesi — v0.2 açıklıkları

Bu bölüm ilk pilotun P1-T1/P1-T2/P1-T3 konuşma çıktıları ve kaynak taraflı kontrolünden doğmuştur. Sonradan açıklığa kavuşturulan kayıt yöntemi aynı veride bağımsız doğrulanmış sayılmaz. İlk pilotun kapanışı §5'in önceki koşulları ve kaynakla sınırlı çıkarım amacı üzerinden verilir; bu ek eksikleri gizleyen yeni bir başarı eşiği değildir.

### Kullanım ile ilişki düzenini birlikte korumak

Terim dökümü, araştırmanın kendi ayrımlarını ve ilişkilerini görünmez bırakmamalı. Kaynağın ortaya koyduğu ilişki düzeni kısa bir eşlik eden görünümde, kullanım kayıtlarına ve kaynak noktalarına bağlı tutulur. Bir konu araştırmasının ilişki çerçevesi zorunlu ürün mimarisi değildir; bir ürün araştırması da önceki pilotun şemasına zorlanmaz. Bu görünüm ayrı kalıcı dosya zorunluluğu veya erken araştırmalar-arası sentez yaratmaz.

### Kaynak rolü, açıklama statüsü ve niteleyiciler

Söyleyen/katman ile açıklamanın kesinliği ayrı izlenir. Önceki pilotun A/R gibi birleşik gösterimleri, dış kaynağa atfedilen kısım ile araştırma yazarının genişletmesini ayırmayı gerektirebilir. Yeni açıklama çıkarıcının bağlamsal yorumuyken doğrudan kaynak tanımı gibi yazılmaz. Kaynak yalnız ad sayıyorsa bu da kaydedilebilir; ayrıntılı tanım yokluğu görünür kalır.

Aynı satırda birkaç ad göstermek onların eş anlamlı olduğuna karar vermek değildir. Ayrı işlem veya farklı anlam oldukları kayboluyorsa satır/kullanım ayrılır. Faaliyet, tasarlanan nesne, tekil kayıt ve daha geniş düzen arasında aynı etiketin kullanımı özellikle korunur. Kaynaktaki olasılık, koşul, amaç ve doğrulanmış sonuç ayrımları özetlemede kaybolmaz; bir tasarımın amaçladığı güvenilirlik gözlenmiş başarı gibi sunulmaz.

### Kaynak taraflı kapsam kontrolü ve durma sınırı

Tam okumadan sonra kaynak bölüm, tablo, liste, örnek ve kaynak kayıtlarından döküme geri gidilir. Her ilgili bölümün karşılığı; mevcut kullanım, yeni/ayrılan kullanım, aynı kullanımın tekrarı, yalnız adı geçen kullanım veya açıklayıcı kaynak/örnek metadatası olarak hesabı verilir. Bu bir doğal-dil sözcüklerinin tamamına tanım üretme veya her örnek değerini bağımsız kavramlaştırma işi değildir. Ayrı kayıt gerekmeyen örnek değerleri ve kaynak adları, taşıdıkları teknik ayrım kaybolmadan bağlamında korunur. Bulunan maddi aktarım hataları ve eksikler kapanmadan sonraki pakete geçilmez.

Bir sonraki okuma yalnız terim hakkındaki genel bilgiyi artıracak, mevcut araştırmadaki kullanımın aktarımını değiştirmeyecekse ilk aşamaya eklenmez. Kaynağın tanımlamadığı/belirsiz bıraktığı kullanımı bu statüsüyle kaydetmek geçerli sonuçtur; bunu sırf belirsizlik var diye derin araştırma borcuna çevirme. Aynı biçimde kaynakta açıkça açıklanan bir şeyi atlamayı bu ilkeyle mazur gösterme.

Kapanış, incelenen dosya/sürüm kapsamında bağlamlı aktarımın yeterliliği hükmüdür; sektörün bütün kavramlarının çözümü veya hatasız/evrensel eksiksizlik sertifikası değildir. Sonradan somut atlama veya anlam bozulması bulunursa ilgili kayıt yeniden açılır; soyut biçimde daha fazlası olabilir diye bütün paketi sürekli açık tutma.

### Denemeler arasında taşınacak sınama

İkinci pilot v0.2-draft'ı farklı araştırma düzeninde sınar. Özellikle atıf–yorum ayrımı, aynı adın farklı kullanımını koruma, kaynak-içi ilişki görünümü, dosya kapsamı ve kapanış sınırı gözlenir. İlk pilotun iyi görünen çıktısı ikinci pilotun başarı kanıtı değildir. Gerçek yeni-oturum deneyi ve bağımsız aktör incelemesi yapılmış sayılmaz. Pilot içerikleri hâlâ konuşmada kalır; mevcut durum/yöntem kayıtlarını güncellemek kalıcı terim envanteri başlatmaz.
