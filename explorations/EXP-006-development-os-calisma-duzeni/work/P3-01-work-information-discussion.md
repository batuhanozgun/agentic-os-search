# P3-01 — İş, yapı ve bilgi akışı: bütünleşik tartışma taslağı

**Üst iş:** [WORK/P3](../WORK.md). **Güncelleme:** 27 Eylül 2026.  
**Sürüm:** v0.2; başlangıç `agentic-os-search@ed2bf6e2232b38c42b5d58d82f5b700fdd434e77`.  
**Statü:** DISCUSSION BASELINE / CANDIDATE / NOT ACCEPTED. P3 tamamlanmadı; P4–P6 başlamadı. Bu, seçilmiş mimari veya çalışan mekanizma değildir.  
**Değişim:** İlk önerinin yaşayan iş ağı, ihtiyaca göre işbirliği ve kalıcı bilgi/role özgü bağlam omurgası korunur. Kullanıcının iş–yapı ayrımı, koordinasyon ve denetimin hedeflerini açıklaştıran bu revizyonu doğurdu. [Önceki v0.1](https://github.com/batuhanozgun/agentic-os-search/blob/ed2bf6e2232b38c42b5d58d82f5b700fdd434e77/explorations/EXP-006-development-os-calisma-duzeni/work/P3-01-work-information-discussion.md) kendi kaynak iziyle korunur.

## 1. Kullanıcı yönü ve önerinin sınırı

P3'ü açan görünür mesaj: “en önemli kısım burası. burada araştırma reposu sana bir çok örnek ve bir çok metodoloji verebilir. burayı biraz derin konuşalım. hemen karar verme, bana bir yapı sun, birlikte değerlendirelim. senin sunduğunu baz alalım.”

Sonraki iki görünür öneri:

> “burada şu ayrımı ortaya koy önce, ona göre konuşalım bence. işi yapanlar ile ortamı yönetenler ayrı olmalı. işi yapanların işle ilgili denetleyicileri ile ortamdan kaynaklı denetliyiciler farklı motivasyonlara sahip olacaklardır. bunu düşün benimki sadece öneri”

> “işi yapmanın koordinasyonu ile yapının koordinasyonu bence farklı. senin buradaki bu soruyu sorma sebebin nedir tam olarak? varsayımlarımızı çapıştıralım.”

Bunlar model-visible mesaj aktarımıdır; platform export'u değildir. Kullanıcı ardından ilerlemenin gereksiz küçük turlara bölünmesini eleştirdi ve bütünlüklü taslağa devam edilmesini istedi. Kısa sunum, küçük miktarda iş yapma veya her ayrımda yeni onay isteme şartı değildir. Bu yön, aşağıdaki tasarımı kabul edilmiş yapmaz.

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

## 5. Tek örnekte normal akış ve bozulma

**Varsayımsal durum:** SOUL için bir kapasite tasarımı yürürken uzman, kararının kritik bir araştırma bulgusuna bağlı olduğunu fark eder. Bu, gerçek ilk SOUL işi olarak seçilmemiştir.

- İş sahibi soruyu ve bekleyen kararı belirtir; DR06-G yalnız bağımlı kararı beklemeye alır, bağımsız işler ilerleyebilir.
- DR06-Y araştırma katkısının çalışmasını sağlar. DR08 kaynak/karar görünümünü hazırlar; araştırmacı kendi bilgi açığını fark edip kaynağa daha derin dönebilir.
- Araştırmacı yanıtı getirir; tasarımcı anlamını değerlendirir. DR13-G bulgunun ve tasarımda kullanımının yeterliğini gereken kapsamda sınar.
- DR13-Y incelemesi, yanlış sürümün gösterildiğini veya cevabın yanlış işe bağlandığını bulursa yalnız “mesaj teslim edildi” kaydıyla başarılı sayılmaz. Etkilenen bilgi görünümü düzeltilir; G tarafı bundan hangi kararların geçersizleştiğini değerlendirir.
- Araştırmacı oturumu kaybolursa Y tarafı denemeyi/etkiyi uzlaştırır ve gerektiğinde doğru kayıtla yeniden görevlendirir. G tarafının sorusu ve karar gerekçesi korunur; yeni oturum yeni bir amaç icat etmez. Yan etki belirsizse kör yeniden çalıştırma yapılmaz.

Böylece hem araştırma yanlışken kusursuz çağrı yolu hem araştırma doğruyken bozuk devir yolu ayrı ayrı görülebilir. İki yeşil kontrolü ilgisiz hedef/sürümle birleştirmek de birleşik yeterlik vermez.

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

Bu revizyon önce mevcut Foundation ayrımlarıyla, sonra bu soruya uyan study örneğiyle kuruldu. Aşağıdakiler tasarım gerekçesidir; ürün benimseme veya davranış ispatı değildir.

| Dayanak | Bu taslağa somut etkisi | Sınır |
|---|---|---|
| Work Foundation — [ground synthesis](../../../research/soul-foundations/03_ground-deepening/grounds/work/synthesis/WORK-GROUND-AUDIT-SYNTHESIS.md), özellikle §§2,5–7 | Yapı bakımı ve meta-iş de Work; plan/actual/sonuç ayrı. G/Y iki Work türünün evrensel taxonomy'si yapılmadı | Aynı konuşmada görülen tam değişmemiş içerik yeniden kullanıldı; özgün dış corpus yeniden okunmadı |
| Actors Foundation — [ground synthesis](../../../research/soul-foundations/03_ground-deepening/grounds/actors/synthesis/ACTORS-GROUND-AUDIT-SYNTHESIS.md), §§2,5,7–8 | Kalıcı sorumluluk, aktör, katılım, competence ve authority ayrı; koordinatör teknik erişimden ürün karar yetkisi çıkaramaz | Aynı konuşmadaki tam içerik; bağımsız ajan deneyi değil |
| Information — [integration I1–I5](../../../research/soul-foundations/07_selection-dynamics-integration-review/SYNTHESIS.md) | İçerik yeterliği, consumer erişimi ve actual kullanım ayrıldı; ortak hedef/sürümle bağlanmayan iki olumlu hüküm birleştirilmedi | Aynı konuşmadaki tam içerik; doğal dil bağlam yeterliğinin otomatik oracle'ı yok |
| [Gas Town META](../../../research/studies/gastown/META.md) → [FINDINGS](../../../research/studies/gastown/FINDINGS.md), §§1–16 | İş nesnesi ile dispatch denemesi/kapasite/liveness ve ürün entegrasyonu ayrımı; yapı koordinasyonu ile G iş sırasının sözleşmesi; maliyete göre seçici kalıcılık | Bu tur META tam; FINDINGS 1–280 seçici okundu, §18 tablosunun devamı/sonrası tam sayılmadı. Source pin `649b832` üzerine eski study bulgusu; bugünkü Gas Town veya Claude doğrulaması değil |
| [Superpowers S03](../../../research/studies/superpowers/syntheses/S03-intent-planning-and-context-handoff.md) | Koordinasyonun anlamsal işini kaybetmeden bağlam sorumluluğunu paylaşma; worker brief'i ürün niyetinin yerine geçmez | Aynı konuşmada tam okunmuş study sentezi; insan kapıları ve SDLC aynen alınmadı |
| [RPD assessment](../../../research/studies/recursive-prerequisite-discovery/ASSESSMENT.md) | Önkoşul keşfi, yöntem/amaç ayrımı ve kesilmiş sorgunun return-to'su; Y engeli G amacını değiştirmez | Aynı konuşmada tam okunmuş assessment; özgün ekler ve prototip yeniden okunmuş/çalıştırılmış değildir |
| [Work-management U08](../../../research/studies/work-management-project-control/08-CROSS-UNIT-SYNTHESIS.md) | Farklı bağımlılık, ready/claim/running/done ve geri dönüş anlamları korunur | Önceki 1–320 seçici kapsam yeniden kullanıldı; son enterprise/kapanış bölümü yeni tam okuma sayılmaz |

**Bu turun sabit kaynağı:** Research main `ed2bf6e2232b38c42b5d58d82f5b700fdd434e77`. Yeni Gas Town META blob'u `dfe8dd29a38ef7e4f686b358dac77ec8fdfe6fe6`, FINDINGS blob'u `4e376aaf3f45936637125496451d1258325fe310`. CATALOG görünümünün ilgili satırları aday seçimi için okundu; kesilmiş tüm katalog tam okundu denmedi.

AGENT güncel canonical okundu; aynı konuşmada tam görülen gerekli kontrol protokolleri korundu, araştırma kanıtı yapılmadı. Current INDEX/HANDOFF/WORK/DECISIONS bu tur yeniden okundu; WORK'ün kesilen ilk görünümü 70–170 ile tamamlandı. STATE, ACTORS, U002, P1-01, P2-01 ve önceki P3-01'in görünür tam içerikleri aynı konuşmadan kullanıldı. Bütün research korpusu veya canlı Claude yeniden doğrulanmadı.

**Kanıt sınırı:** Bu bir aynı-assistant kaynak karşılaştırması ve aday tasarımdır. Yeni runtime, ürün veya çoklu ajan deneyi yoktur. Masa başı senaryoları doğrulanmış çalışma başarısı sayılmaz. İlgili mekanizma güncel seçime dayanak olduğunda P1/P4/P6 doğrulama yükü sürer.

## 10. Dönüş ve devam

Bu tur dört rol adı söylemekle sınırlı kalmadı: mevcut roller iki hedefle eşlendi; koordinasyon, denetim, karşılıklı istek, karar/yetki, bilgi sahipliği ve bir normal/bozuk akış birlikte taslaklaştırıldı. Kullanıcıya bu bütünlük kısa sunulur; her cümlede onay veya yeni ilerleme komutu istenmez.

P3 içinde sıradaki bütünlüklü derinleştirme, bu bazın **bağlam hazırlanması → uzmanlar arası görüş ayrılığı → kararın kaydı → yeni bilgiyle yeniden açma → oturum devri** boyunca somut çalışma sözleşmesine dönüşmesidir. Kullanıcının değerlendirmesi varsa bu revizyona işlenir; kabul edilmemiş tercih accepted yapılmaz. Her tur bütün sistemi yeniden icat etmek veya P4'e geçmek değildir.

P2/ACTORS bu tur ilk sözleşme tabanı olarak korunur; önerilen hedef-profili düzeltmesi burada tek yerde durur. Gerekçeli yerleşme sonrasında registry/sözleşme değişikliği yapılabilir. P3 tamamlanmadı; gerçek SOUL işi, topoloji ve actual ajan dosyası seçilmedi.
