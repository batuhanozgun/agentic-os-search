# EXP-006 — HANDOFF

**Güncelleme:** 27 Eylül 2026, P3 somut çalışma örneği.  
**Devralma:** **P3 DISCUSSION BASELINE v0.3 / CANDIDATE / USER DISCUSSION. P3 TAMAMLANMADI.** P2 ilk sözleşme tabanı ve P1 kaynak haritası/runtime açıkları korunur. P4–P6 başlamadı.  
**Üst amaç:** SOUL'u geliştirecek Claude Code cloud ekibinin çalışma düzeni; assistant'ın SOUL backlog'unu seçmesi değil.

## 1. Okuma yolu

[STATE](STATE.md) → HANDOFF → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) → [P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı conversation içinde tam unchanged içerik tekrar yüklenmez.

P2 ilk tabandır; P3-01 v0.3, G/Y hedef profillerini somut etkileşim ve kayıt örneğiyle ayrıntılandırır. S1/B gerekçe gerektiğinde açılır. Foundation/studies kullanım kapsamı P3-01 §9'dadır; her tur bütün korpus okunmuş sayılmaz.

## 2. Son konuşmadan devralınması gereken

Kullanıcı P3'te araştırmadan beslenen yapı ve birlikte değerlendirme istedi; işin koordinasyonu ile yapının koordinasyonunu ve bunların denetimlerini ayırmayı önerdi. Assistant ayrımı küçük turlarda tekrar etti; kullanıcı ilerlemenin gereksiz küçültülmesini eleştirdi. Kısa sunum ile az iş yapmanın aynı olmadığı korunmalıdır.

v0.2 bütünlüklü rol/karar/bilgi taslağını sundu. Son kullanıcı mesajı: “Bu yön bana mantıklı geldi ama biraz daha somutlaştır bunu.” Bu yön desteğidir; bütün tasarım ayrıntılarının kabulü değildir. Mevcut v0.3 bu talebe tek işte konuşma, bağlam, araştırma, itiraz, kayıt ve devam örneğiyle cevap verir.

Yeni oturum iki koordinasyonun farklı olduğunu yeniden açıklamakla veya dört isim için onay beklemekle yetinmemeli. Current tartışma malzemesi P3-01 §5'teki somut örnektir.

## 3. Korunan bütünlüklü öneri

İki hedef alanı aynı DevOS içindedir:
- **G:** SOUL ürününü geliştirme — gerekli iş/plan, araştırma/tasarım/üretim, ürün ve sonuç güvencesi.
- **Y:** DevOS işleyişi — katılım, iletişim, bilgi/bağlam, araç/erişim, kapasite, süreklilik ve yapı bakımı/güvencesi.

Y de Work/reasoning taşır; Foundation ENVIRONMENT'ına indirgenmez. G/Y hedef ekseni F1–F8 başarı yönü ekseni değildir. Bütün rolleri iki kez kurmak veya iki kapalı ekip yapmak önerilmez.

DR06-G ürün önceliği ve katkı bağımlılıklarını işletir; DR06-Y gerçek çalıştırma/kapasite/devri koordine eder. İş tarafı olmayan kapasiteyi varsayamaz, yapı tarafı ürün gereksinimini sessizce azaltamaz.

DR13-G ürün/iş seçimi/sonuç; DR13-Y gereken çalışma koşullarının fiilî sağlanması için güvence üretir. Aynı isimdeki veya iki ayrı ajandaki kontroller otomatik bağımsızlık sağlamaz; iddia, hedef, sürüm ve kanıt bağları korunur.

Diğer roller P3-01 §2'de tam eşlenmiştir. DR01–05 ağırlıklı geliştirme, DR07–10/12 işletim/destek; araştırma/sınama/teşhis/öğrenme gerektiğinde iki hedefe ayrı görevlendirmelerle katkı verir. Bu özet tam sözleşme yerine geçmez.

## 4. v0.3 somut örneği ve tasarım kazancı

**Örnek soru:** Ekip kendi keşfiyle “SOUL, kullandığı bilgi değiştiğinde önceki kararlarını nasıl ele almalı?” sorusuna gelmiş olsun. Bu gerçek ilk iş seçimi, tamamlanmış araştırma veya SOUL tasarım kararı değildir.

P3-01 §5'te:
- Tasarımcı öneri yapar; G inceleyicisi kaynak değişikliği ile kararın dayanağının geçersizleşmesini ayıran karşı soru getirir.
- G koordinasyonu araştırmanın hangi kararı beklettiğini tutar; Y araştırmacı/bağlam/erişim/yanıt yolunu sağlar.
- Örnek araştırma teslimatı tasarım seçeneğini değiştirir; eksik bağımlılık kaydı karşı vakası kararı açık bırakır.
- İş/katkı, çalıştırma/katılım ve karar/dayanak/kanıt kayıtları ayrı anlamlarla bağlı tutulur. Bunlar üç zorunlu dosya veya üç veri deposu değildir.
- Devir: araştırma teslim edildi, karar açık, beklenen karşı vaka ve dönüş noktası belli. Yeni oturum geçerli araştırmayı sebepsiz tekrar etmez; gerçek deneme/yan etki/güncellik ayrıca uzlaştırılır.
- Yeni bilgi geldiğinde bağımlı kayıtları bulmak ile kararın anlamını değiştirmek ayrı sorumluluklardır. Yeni mesaj eski kararı otomatik iptal etmez; gecikmiş yanıt güncel kaydı otomatik ezmez.

ÖR-İ01/A01/Ç01/K01/T01 kurgusal kimliklerdir; gerçek proje kuyruğuna alınmayacak. Örnekte sınama tasarlanabilir ama koşu yapılmış veya PASS elde edilmiş değildir. Yön desteği bütün G/Y hükümlerinin kullanıcı kabulü olarak genişletilmez.

## 5. Etkileşim, bilgi ve yetki sınırları

Talep sahibi açık soruyu ve sonucu kullanmayı; katkı sahibi bilgi/ürün teslimatını taşır. G akış ve önceliği, Y gerçekleşmiş çağrı/katılım/devri izler. Küçük ve kapsam içi danışmalar her mesajda iki koordinatörün onayını beklemez; ayrı sahip, bekleme, maliyet veya devir doğarsa izlenebilir katkı gerekir.

Alan sahibi içeriği ve karar gerekçesini üretir. DR07 kaynak/sürüm/statü/lifecycle bütünlüğünü işletir; domain doğruluk hakemi veya tüm dosyaların tek yazıcısı değildir. DR08 uzmanla birlikte role uygun görünümü hazırlar; tüketici eksikliği sorgulayabilir ve kaynağa dönebilir. Her rolün bütün geçmişi alması gerekmez.

K1 talep→çalışma→yanıt→kullanım; K2 rutin rol geçişinde Batu'ya ihtiyaç duymamaktır. Başlatma/yeniden başlatma ve gerçek yetki/kabul/müdahale mümkündür. Etki belirsizken kör retry, olguyu oylamayla doğru yapma veya her itirazı sınırsız veto yapma yoktur. Kesin işletim/permission mekanizması henüz kurulmadı.

## 6. Kaynak, devam ve kayıt

v0.3'te Information Revision M5 tam okundu; yeni girdi, alternatif destek, gelecekteki revizyon için durum koruma ve proposed/installed/observed/propagated ayrımları örneğe taşındı. Aynı konuşmadaki Work/Actors/Information, RPD, Superpowers ve seçici Gas Town/Work-management okumaları kullanıldı. Bütün dış kaynaklar veya bugünkü ürün sürümleri yeniden doğrulanmadı; P3-01 §9 kapsamı taşır.

P1 Q01–Q06 cloud/erişim/araç/plugin/kalıcılık/güvence açıkları korunur. Kanon/v2/ECC/Gas Town benimsenmedi. S1-16 full-read qualification'ı S1-17 §7'de kalır. Canlı Claude deneyi, mesaj teslimi veya recovery testi yoktur.

**Sonraki bütünlüklü P3 değerlendirmesi:** Örnekte talep/itiraz/kararın açık ve karşılanmış sayılma koşulları, küçük danışmanın ayrı Work'e dönüşmesi ve G/Y durdurma–devam sorumluluklarını birlikte netleştir. Kullanıcının örneğe tepkisi öncelikli girdidir. Aynı ayrımı yeniden anlatma veya her küçük adımda komut bekleme; tartışılabilir bütünlüklü parça üret.

P3 tamamlandı deme; P4–P6'ya geçme. P2 registry/sözleşmeleri ilk taban olarak korunur; G/Y farkı ve örneğin tek ayrıntı evi P3-01'dir. Bütün plan WORK, current STATE, devir HANDOFF'tadır. Bu tur agent-control değişmedi.
