# EXP-006 — HANDOFF

**Güncelleme:** 27 Eylül 2026, P3 iş–yapı koordinasyonu ve güvence taslağı.  
**Devralma:** **P3 DISCUSSION BASELINE v0.2 / CANDIDATE / USER DISCUSSION. P3 TAMAMLANMADI.** P2 ilk sözleşme tabanı; P1 kaynak haritası/runtime açıkları korunur. P4–P6 başlamadı.  
**Üst amaç:** SOUL'u geliştirecek Claude Code cloud ekibinin çalışma düzeni; assistant'ın SOUL backlog'unu seçmesi değil.

## 1. Okuma yolu

[STATE](STATE.md) → HANDOFF → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) → [P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı conversation içinde tam unchanged içerik tekrar yüklenmez.

P2 ilk tabandır; P3-01 v0.2, DR06/DR13 için iki hedef profili önerir. Bunları kabul edilmiş yeni registry veya fiziksel ajan sayısı sanma. S1/B ayrıntıları gerekçe gerektiğinde açılır. Foundation/studies'in gerçek kullanım ve okuma kapsamı P3-01 §9'dadır; her tur tüm korpus okunmuş sayılmaz.

## 2. Son konuşmadan devralınması gereken

P3'te kullanıcı araştırma örneklerinden beslenen yapı önerisi ve birlikte değerlendirme istedi. İlk taslak iş ağı/çalışma halkası/kalıcı bilgi omurgasını sundu. Kullanıcı daha sonra işi yapanlarla yapıyı işletenlerin koordinasyon ve denetimlerini ayırmayı önerdi.

Assistant bu ayrımı birkaç turda tekrar ederek gereksiz küçük adımlarla ilerledi. Kullanıcı bunu eleştirdi; kısa çıktı ile küçük çalışma biriminin aynı olmadığı açıklaştı. Son devam yönü, bu ayrımı bir bütün taslağa taşımayı yetkilendirdi. Kaynak mesajlar ve kapsam P3-01 §1'de; tasarımın kabulü yoktur.

Bu nedenle sonraki oturum yeniden “iki koordinasyon farklıdır” açıklamasına veya dört isim için küçük onay turuna dönmemeli. Current malzeme artık roller, karar sınırları, bilgi akışı ve normal/bozuk çalışma zinciri birlikte verilmiş v0.2'dir.

## 3. Current bütünlüklü öneri

İki hedef alanı **aynı DevOS içinde** düşünülür:

- G: SOUL ürününü geliştirme — gerekli işi keşif/plan, tasarım/araştırma/üretim, ürün/sonuç güvencesi.
- Y: DevOS işleyişi — katılım, iletişim, bilgi/bağlam, araç/erişim, kapasite, süreklilik ve gerekçeli yapı bakımının işletimi/güvencesi.

Y de Work ve reasoning taşır; Foundation ENVIRONMENT'ına indirgenmez. G/Y hedef ekseni, F1–F8 başarı yönü ekseniyle aynı şey değildir. Bütün rolleri iki kez kurmak veya iki kapalı ekip yapmak önerilmiyor.

**DR06-G/Y:** İş koordinasyonu hangi katkının neye bağlı olduğunu ve önceliği işletir; yapı koordinasyonu bu katkının mevcut koşullarda nasıl etkinleşip geri döneceğini yönetir. Yapı kısıtı ürüne geri besleme yapar, fakat ürün kriterini sessizce değiştiremez. İş tarafı da olmayan kaynağı/izni var sayamaz.

**DR13-G/Y:** Geliştirme İnceleyicisi ürün/iş seçimi/sonuç iddiasını; İşleyiş İnceleyicisi gereken çalışma koşullarının gerçek karşılığını sınar. İki kapsamın kanıtı ayrı ve doğru hedef/sürümle bağlıdır. Ayrı isim epistemik bağımsızlık garantisi değildir.

Diğer roller hedefe göre yerleşir: DR01–05 ağırlıklı geliştirme; DR07–10/12 işleyiş ve destek; DR04/11/14/15/16 gibi yetkinlikler gerektiğinde iki hedefe ayrı görevlerle katkı verebilir. Bu özet, P3-01 §2'deki tam eşlemenin yerine geçmez.

## 4. Etkileşim ve bilgi sahipliği

İş sahibi soru, karar bağı, gereken katkı/uzmanlık, kaynak/target ve dönüş noktasını tanımlar. G koordinasyonu ihtiyaç ve bağımlılığı; Y koordinasyonu gerçek çalıştırma/erişim/katılımı işletir. Yetkili iş içindeki küçük danışmalar her mesajda iki koordinatörün onayını beklemez. Kapsam, maliyet, ayrı sahip/bekleme veya devir doğarsa izlenebilir Work'e dönüşür.

Katkı sahibi sonucunu ve sınırlarını; talep sahibi kullanımını veya gerekçeli reddini taşır. Araştırma tamamlanması üst kararın kapanması değildir. Ürün/plan koşullarını G, gerçekleşmiş çağrı/devir/bağlam koşullarını Y güvencesi ilgili riskte sınar; her küçük iş için iki zorunlu komite kurulmaz.

Alan sahibi içerik ve kararın gerekçesini korur. DR07 kaynak/sürüm/statü/lifecycle bütünlüğünü işletir; bütün dosyaların tek yazıcısı veya domain doğruluk hakemi değildir. DR08, iş sahibi ve uzmanla birlikte yeterli görünümü hazırlar; tüketici eksikliği sorgulayıp asıl kaynağa dönebilir. Ortak zemin herkese bütün geçmişin verilmesi değildir.

Arıza/kapasite/bayatlarsa: Y gerçek kısıt ve etkiyi bildirir, koşulları uzlaştırır; G etkilenen karar/öncelik/işi yeniden değerlendirir. Etki belirsizken kör retry yapılmaz. Meşru durdurma yalnız ilgili çalışma/kapsama uygulanır; otomatik her itiraz veto veya her anlaşmazlık Batu sorusu değildir.

## 5. Sabit sınırlar ve kanıt

K1 talep→çalışma→yanıt→kullanım; K2 rutin rol geçişinde Batu'ya ihtiyaç duymamaktır. Başlangıç/yeniden başlatma, gerçek müdahale ve yetki/kabul mümkündür. SOUL'un ilk teknik işi assistant tarafından seçilmez. Test örneği backlog değildir.

P1 Q01–Q06 gerçek cloud araç/sürüm/erişim, plugin çelişkisi, kalıcılık ve güvence açıklarıdır; P3 taslağı bunları kapatmaz. P4'te yük taşıyan seçim tazelenir/sınanır. Kanon/v2/ECC/Gas Town hazır mimari olarak alınmadı.

Bu tur Gas Town META tam, FINDINGS 1–280 seçici okundu. İş nesnesi, dispatch denemesi, kapasite, liveness ve entegrasyon ayrımları kullanıldı; güncel dış ürün veya canlı Claude deneyi yapılmadı. Diğer load-bearing Foundation/study içerikleri aynı konuşmanın görünür okumalarından yeniden kullanıldı. S1-16 full-read qualification'ı S1-17 §7'de korunur.

## 6. Devam ve kayıt

Current P3-01 v0.2'yi kısa ama değerlendirilebilir bütünlükte kullanıcıya sun. Karar bekleyen yerleri aday tutmak, her küçük ayrımda yeni komut istemek değildir. Sonraki anlamlı P3 parçası bağlam, uzman görüş ayrılığı, karar kaydı, yeni bilgiyle yeniden açma ve oturum devrinin birlikte somutlaştırılmasıdır. Kullanıcı değerlendirmesi aynı taslağa işlenir; üst plan yeniden icat edilmez.

P3 tamamlandı deme; P4–P6'ya otomatik geçme. P2 registry/sözleşmeleri bu tur değiştirilmedi; önerilen DR06/13 hedef-profili farkının tek ayrıntı evi P3-01'dir. Yerleşen değişiklik ileride ACTORS/P2'ye açık statüyle yansıtılır.

Bütün plan WORK, current STATE, devir HANDOFF, tartışma P3-01'dir. Bu güncelleme agent-control değişikliği değildir. Kullanıcıya uzun iç değerlendirme veya tüm kaynak geçmişi yerine anlamlı tasarım parçasının sonucu verilir.
