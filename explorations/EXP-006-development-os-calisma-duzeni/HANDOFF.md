# EXP-006 — HANDOFF

**Amaç:** Eski sohbeti görmeyen oturumun yalnız son alt konuyu değil, o konunun üst iş içindeki nedenini ve doğru dönüş noktasını devralması.  
**Güncelleme:** 26 Eylül 2026.  
**Güncel iş:** S1 — araştırmaya dayalı Development OS rol ve sorumluluk konsolidasyonu.

## 1. Son kullanıcı yönü ve bu turun kapsamı

Kullanıcı, önceki zinciri yeniden çıkarmayı, konuyu toparlamayı ve devam etmeyi istedi; oturumun tam okunabileceğini önerdi. Bu tur erişilebilen konuşma akışı ile güncel proje kayıtları karşılaştırıldı. Yeni dış araştırma veya ayrı motivasyon çalışması başlatılmadı; G1'in geniş sorumluluk eşlemesi tamamlanmış sayılmadı.

**Okuma sınırı:** Görünür konuşma geçmişinde aktarılmamış mesaj bölümleri vardır. Files üzerinde iki sorguda ayrıca erişilebilir bir EXP-006 tam dökümü bulunamadı; bu sonuç böyle bir dökümün hiçbir yerde olmadığı anlamına gelmez. Dolayısıyla bu tur oturumun kelimesi kelimesine eksiksiz tam okuması diye kaydedilemez. Görünür akışın bütünü değerlendirildi; EXP-006_Context, STATE, HANDOFF, WORK, ACTORS, DECISIONS, S1 ve S1-03 güncel GitHub içerikleri tam okundu. Kesilen S1 yanıtının sonu ayrıca getirildi. S1-01/S1-02 bu konuşmadaki mevcut kaynak metinleriyle tekrar değerlendirildi; bütün B dosyaları ve dış araştırmalar bu tur yeniden okunmuş değildir.

## 2. Başlangıçtan bugüne ana zincir

1. **Üst amaç SOUL'u yaratmak.** Üretim, teknik uzmanlık, ortak düşünme, biriken bilgi ve değişen plan ihtiyacı nedeniyle bu işi taşıyacak çalışma düzenini Development OS olarak konuşmaya başladık.
2. **İlk soru aktörlerdi.** İnsan ve yapay zekâ ile ilerledik; aktörü rol ile eşitlemedik.
3. **İnsan/müşteri çekirdeğini yetki + kabul olarak ayırdık.** Teknik keşif, iş yönetimi ve doğrulama yükünü müşteriye bırakmıyoruz.
4. **Asıl aranan yapay zekâ aktörünün rolleriydi.** Jenerik unvan listesi üretmemek için önce DevOS'un ne iş yapacağını sorduk.
5. **İşi anlamak için üretilecek SOUL'u somutlaştırmak gerekti.** EXP-001/002/004 okumalarından çıkan geniş hedef bu aşama için yeterli kabul edildi; nihai mimari veya uygulanmış sistem olmadı.
6. **DevOS'un SOUL üzerinde yapacağı B1–B9 geliştirme alanları çıkarıldı.** Her birinden gereken kabiliyetler/sorumluluklar, ardından bunları taşıyabilecek R ve M adayları türetildi.
7. **B1–B9 ilk ayrıştırmasından sonra S1 açıldı.** R1–R25/M1–M9'u birlikte değerlendiriyoruz: aynı ailede neler olabilir, ne ayrı kalmalı, hangi iş açıkta, hangi bilgi ve mekanik destek gerekli?
8. **Araştırmalar ve aktör özellikleri S1'in değerlendirme girdileri oldu.** Superpowers/gstack, Keel ve OS Architect okumaları yeni amaç değil; bu rol sorusunu daha iyi cevaplamak içindi.
9. **Şimdi bu ölçütlerle somut geliştirme zincirine dönüyoruz.** DevOS'un rol/sorumluluk düzeni yeterince açıklanmadan mimariye veya kuruluma geçmiyoruz.

Bu zincir bir rol ontolojisi veya zorunlu doğrusal geliştirme takvimi değildir; konuşmanın neden bu sırayla ilerlediğini korur.

## 3. İlk altı kök iş ile B1–B9'u karıştırma

İlk harita: (1) neyin yapılacağını belirlemek, (2) gereken işleri keşfetmek, (3) işleri yapılabilir hâle getirmek, (4) gerçekleştirmek, (5) sınamak/yeniden çalışmak, (6) bütün bunları zaman içinde sürdürmek.

SOUL hedefi ilk başlık için çalışma düzeyinde somutlaştırıldı. B1–B9 ikinci başlıkta çıkarılan geliştirme alanlarıdır; bunların kabiliyet ve rol açılımı, işleri yapılabilir kılmak için nelerin gerektiğini de görünür yapıyor. Bu nedenle altılı ve dokuzlu liste rakip sınıflandırmalar veya art arda sayılan tek liste değildir.

B1 ortak düşünsel taban; B2 bilgi; B3 aktör; B4 iş; B5 ortam; B6 dört zemin arasındaki ilişkiler; B7 işe göre çalışma sistemi oluşturma; B8 süreklilik/değişim/toparlanma/öğrenme; B9 bütünleştirme ve sınamadır. Bunların hepsi **SOUL'a bu kapasiteleri kazandırma işidir**; hazır SOUL modülleri değildir.

B1–B9'un yazılması, gerçekleştirme veya gerçek sistem sınamasının bitmesi demek değildir. EXP-006 için kurduğumuz dosya düzeni bu araştırmanın sürekliliğini destekler; DevOS'un kurulmuş veya SOUL sürekliliğinin doğrulanmış hâli değildir.

## 4. Son üç S1 dilimini ana soruya geri bağla

- **S1-01:** İnceleme/doğrulama ortak ailede düşünülebilir; üretim ve düzeltme ilişkili; teşhis, teknik karar, uygulama ve kanıt ayrı sorumluluklar. G1: gerekli kod/prosedür/bağlantıyı geliştirmenin açık taşıyıcısı yeterince izlenmiyor.
- **S1-02:** Kullanıcı, insan ile dil modelinin rolü farklı koşullarda üstlenmesine ve çatışan motivasyona dikkat çekti. Ortak aile aynı etkin görevlendirme değildir. Tutarlı başarı yönü; tek görev veya tek ölçüt zorunluluğu değildir. Uyarlama, model ağırlıklarını eğitme kararı değildir.
- **S1-03:** OS Architect geliştirme kayıtları, rolün yazılı amacından başka fiilî başarı beklentisini, ortak düşünsel tabanı, gerektiğinde tetiklenmesini, katkısının kullanılmasını ve bilginin geliştiren→SOUL→kurulmuş role aktarımını değerlendirme ihtiyacını gösterdi.

Bunlar aday S1 sonuçlarıdır. Tek motivasyonun evrensel üstünlüğü, aynı amaçlı her rolün eşitliği veya ayrı çağrının bağımsız kanıt olduğu ispatlanmadı. R/M kimlikleri henüz birleştirilmedi. Müşterinin yetki/kabul çekirdeği değişmedi.

## 5. Devam: G1'i tek somut geliştirme zincirinde aç

**Sorulacak soru:** Bir davranışı SOUL'a kazandırmak için gereksinimi araştıran/tanımlayan, kod veya prosedürü üreten/uyarlayan, kuran/bütünleştiren ve sınayan DevOS sorumlulukları nasıl açıkça bağlanır?

Başlangıç örneği olarak **salt-okur inceleme gereken bir durumda inceleyicinin incelenen ürünü değiştirememesi** kullanılabilir. Bu, bütün inceleyicilerin her işte yazamaz olması veya Keel mekanizmasının benimsenmesi kararı değildir.

Her halka için somut çıktı, bilgi/yeterlik, araç/izin, başarı yönü, mevcut rol adayının kapsamı, sonraki tüketici ve kanıt aranır. Mekanizma işletilirken ne yaptığı ile o mekanizmanın geliştirilmesi ayrı tutulur. R14/R20'nin kurma/işletme tanımları bütün üretimin otomatik sahibi kabul edilmez. Önce ilgili B/R kaynaklarına in; yalnız ad benzerliğiyle atama yapma.

**Sınırlı dönüş koşulu:** Bir örnekte hangi geliştirme sorumluluğunun mevcut adayla açık eşleştiği, hangisinin eksik/örtük kaldığı ve birlikte taşımanın hangi koşullara bağlı olduğu gösterilsin. Bu ilk örnek bütün M1–M9 kapsamı, nihai aile sayısı, ajan sayısı veya mimari değildir.

Bu toparlama turu G1 eşlemesini yapmış sayılmaz. Sonraki devam bu sınırlı sorudan ilerler; kullanıcı yönü değişirse önce onu dikkate al. Bağımsız motivasyon araştırması veya bütün OS Architect okuması otomatik açılmaz.

## 6. Okuma ve kayıt rotası

Yeni oturum: STATE → bu dosya → WORK → ACTORS → S1. Başlangıç gerekçesi veya altı kök iş için EXP-006_Context; kabul edilmiş çalışma ayrımları için DECISIONS. G1'e girerken S1-01 tam; aktöre göre koşullar için S1-02/S1-03 gerekli kapsamda okunur. Sonra yalnız ilgili B ve asıl araştırma kaynaklarına inilir.

S1, S1-01/02/03 ve B dosyalarındaki önceki dönüş cümleleri kendi üretim anlarının kaydıdır; güncel sıra STATE/HANDOFF'tan alınır. S1 yöntemindeki kaynak rotaları korunur. Yeni bir araştırma dilimi doğmadığı için sırf toparlama amacıyla S1-04 üretilmedi; mevcut kayıtların görev ayrımı korunur.

Kaynak okuması, yorum, aday öneri ve kullanıcı kabulü ayrı tutulur. DevOS geliştirmesi, SOUL'un gelecekteki kullanıcı işini yürütmesi ve EXP-006'nın kendi kayıt düzeni birbirine karıştırılmaz. Bu tur ACTORS, DECISIONS, EXP-006_Context, Foundation, kaynak depolar ve agent-control değiştirilmedi.
