# EXP-006 — HANDOFF

**Güncelleme:** 27 Eylül 2026, P3 birleşik senaryo ve P4 gereksinim devri.  
**Devralma:** **P3 DESIGN HANDOFF READY v0.5 / CANDIDATE / USER EVALUATION.** D021 sorumluluk sınırı accepted; bütün ayrıntılar ve runtime başarısı kabul edilmedi. **P4–P6 NOT STARTED.**  
**Üst amaç:** SOUL'u geliştirecek Claude Code cloud ekibinin çalışma düzeni; assistant'ın SOUL backlog'unu seçmesi değil.

## 1. Okuma ve kayıt yolu

[STATE](STATE.md)→HANDOFF→[WORK](WORK.md)→[DECISIONS](DECISIONS.md)→[ACTORS](ACTORS.md)→[U002](sources/U002-cloud-plan-and-autonomy.md)→[P1-01](work/P1-01-claude-cloud-environment-map.md)→[P2-01](work/P2-01-named-role-contracts.md)→[P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı konuşmada tam unchanged içerik tekrar yüklenmez.

Üst plan WORK; current STATE; ayrıntılı P3 yalnız P3-01. P2/ACTORS ilk sözleşme tabanıdır; G/Y ve D021 farkları için P3'le birlikte okunur. 16 sözleşme 16 ajan değildir. Tarihsel S1/B current/next ifadeleri bu sırayı değiştirmez.

## 2. Kullanıcının yönü

Kullanıcı P3'te acele karar yerine araştırmayla beslenen bütünlüklü yapı ve birlikte değerlendirme istedi. İşin koordinasyonuyla yapının koordinasyonunu ayırmayı önerdi. Sonrasında özellikle dosyaların, klasörlerin ve çalışma alanının düzeni/bulunabilirliği/yeniden kullanımı üzerinde durdu. İçerik sahibi–düzen sahibi ayrımını kabul etti; bu D021'dir.

Kısa sunumun çok küçük miktarda iş yapmak veya her ayrımda kullanıcıdan yeni komut istemek anlamına gelmediği açıkça konuşuldu. Bu nedenle yeni oturum aynı ayrımı yeniden açıklayan turlara dönmemeli.

v0.4 toparlamasından sonra verilen “devam et.”, ilan edilmiş iki eşzamanlı iş/ortak kayıt/açık inceleme/kesinti senaryosunu açtı. v0.5 bu sınırlı incelemeyi ve P4 gereksinim devrini tamamlar. Kullanıcının bütün tasarımı kabul ettiği veya P4 teknik seçiminin yapıldığı sonucu çıkarılmaz.

## 3. Korunan çalışma resmi

- **G — SOUL geliştirme:** Gerekli iş/önkoşul keşfi ve plan, araştırma/tasarım/üretim, içerik/sonuç güvencesi.
- **Y — DevOS işleyişi ve çalışma alanı:** Katılım, iletişim, araç/erişim, bağlam, kalıcı alan düzeni, bakım/tekrar kullanım ve devir; bunların fiilî kullanılabilirliği.

İkisi de DevOS içinde Work/reasoning'dir. Y yalnız Foundation ENVIRONMENT'ı veya kozmetik temizlik değildir. G/Y hedef ekseni F1–F8 başarı yönü ekseninden ayrıdır; iki kapalı ekip veya her rolün iki kopyası değildir.

DR06-G işin öncelik/bağımlılıklarını; DR06-Y çalıştırma/kapasite/bakım/devrini koordine eder. G olmayan kaynağı varsayamaz, Y ürün kriterini sessizce düşüremez. DR13-G içerik/sonuç; DR13-Y çalışma koşulları/current erişim güvencesidir. Ayrı isim veya iki olumlu sonuç epistemik bağımsızlık kanıtı değildir.

DR07 yer/statü/sürüm/indeks/yaşam döngüsü bütünlüğünü; DR08 uzmanla birlikte tüketici bağlamını; içerik sahibi kendi sonucunu/gerekçesini taşır. Yayın sorumlusu ilgili değişiklik kapsamında belirlenir: bütün dosyaların tek yazıcısı DR07 varsayılmaz. Anlamsal uyuşmazlığı düzen görevlisi keyfî çözüp current yapamaz.

## 4. v0.5 birleşik senaryodan devir

**Örnek:** A ortak dosyanın iddiasını değiştiren aday üretirken B aynı dosyanın mevcut iddiasına bir sınama bağlantısı ekler. İkisi r0'dan başlar; A'ya yönelik İ-A inceleme itirazı açık kalır. B'nin dar kapsamı ayrıca yeterli bulunmuş olsun. Bu varsayımsal yürüyüştür; gerçek SOUL işi veya test sonucu değildir.

P3-01 §8, B yayını sırasında kesin sonuç alınmadan oturumun kesilmesini de işler. Yeniden girişte dosya r1, ilgili giriş hâlâ r0 görünüyorsa yapılacak iş yeni üretimi tekrarlamak değil kısmi yayını/deviri uzlaştırmaktır. A yeni bağlamla devam eder; r0 temelli geç çıktı r1'i ezemez. A'nın yeni iddiası B'nin kanıt bağını etkiliyorsa salt metinsel birleşme yeterli olmaz.

**Korunacak sonuçlar:**
- Paralel adaylar korunabilir; tek current nesnenin değişimi güncel temel, bağımlılık, inceleme ve yetkiyle bağlanmalıdır.
- İnceleme itirazı yeni ad/sürümle kaybolmaz. Olumlu eski hükmün yeni sürüme taşınması da ayrıca gerekçelendirilir.
- Kaynak, current designation ve tüketicinin gerçekten aldığı görünüm ayrı olabilir. Kısmi/unknown yayın ilgili tüketimi hazır yapmaz.
- Uygulandı/uygulanmadı/kısmi/bilinmiyor ayrımı, yeniden denemeden önce gerçek kaynaktan uzlaştırılır. Aynı işlem gereksizce tekrarlanmaz.
- İşin kimliği ile çalışma/yayın denemesinin kimliği ayrıdır. Görevlendirme değişince eski çalıştırmanın yazma yolu fiilen korunmalıdır; yalnız yeni bir kayıt yetmez.
- Yeni bir adayın itirazı, eski current'ın mutlaka yanlış olduğunu göstermez. Ancak eski current da yanlışlanmışsa sırf yayımlanmış diye güvenilir tutulamaz.
- Engelin etkisi kapsamlıdır: ilgili yayın/tüketim tutulur, bağımsız çalışmalar otomatik durmaz. Gerçek kullanıcı durdurması aşılmaz.

Senaryo bir katkının tamamlanıp diğerinin itirazının açık kaldığı meşru ara durumda biter. Bu sahte başarı üretmeme tasarım sonucudur; runtime'ın böyle davrandığı kanıtı değildir.

## 5. P3 yeterlik hükmü ve kalan yük

Kavramsal teslimat kapsamında sahip, kalıcı durum, tüketici ve sonraki tetik için açık aday karşılıklar bulundu. Yeni bir rol ailesi veya yeni genel audit kampanyası gerektiren somut açık bulunmadı. **P3 tasarım devrine hazır adaydır; kullanıcı kapanışı değildir.**

P4'e giden altı yükün tek ayrıntı kaydı P3-01 §10:
H1 rol/ilk etkinleşme; H2 fiziksel çalışma alanı ve current erişim; H3 değişiklik/yayın koruması; H4 talep/yanıt/tüketim; H5 kesinti/kısmi sonuç/eski-yazıcı; H6 güvence/bakım/yeniden kullanım.

P4, bunları tek tek yeni özel servis icat ederek değil, gerçek Claude seçenekleri ve gerektiğinde en uygun mevcut mekanizmalarla karşılaştırarak cevaplamalı. P2 registry + P3 farkı birlikte etkin görevlendirmeye bağlanmalı. Alt ajan/takım veya gerekçeli birleşim henüz seçilmedi. P1 Q01/Q02/Q04/Q05/Q06 ilgili yolda doğrulanacak; Q03 ancak plugin seçimi yük taşıyorsa açılacak.

## 6. Kaynak ve doğrulama sınırı

v0.5'te Beads META tam, FINDINGS 1–245 seçici okundu. Tarihsel kaynak study'sindeki claim/liveness/reopen ayrımları hedefli kullanıldı; claim dosya yazma yetkisi veya sonucun doğruluğu yapılmadı. Önceki Information I1–I5/Revision M5, Hermes Note30 ve Gas Town okumaları belirtilmiş kapsamla korundu. Gerçek iz P3-01 §9'dadır.

Yeni dış ürün özelliği araştırılmadı; canlı Claude, dosya yarışı, yayın timeout'u veya recovery deneyi yapılmadı. Masa başı senaryo bağımsız doğrulama değildir. S1-16 full-read qualification'ı S1-17 §7'de kalır; bütün Foundation/studies yeniden okundu iddiası yoktur.

## 7. Current dönüş

Bu tur kullanıcıya birleşik senaryonun neyi değiştirdiğini ve P3 taslağının P4'e devre hazır olduğunu kısa sun. Sonraki kullanıcı devamıyla P4'te çalışma biçimi/actor allocation ve fiziksel alanı H1–H6'ya karşı birlikte tasarla. P4 bu tur başlamadı; yeni dosya/klasör mekanizmaları kurulmadı.

Kullanıcı düzeltmesi veya somut teknik engel varsa ilgili P3/P2 kısmını hedefli aç. Bunlar yoksa yeni genel P3 audit'i, aynı örnek tekrarı veya rol taxonomy'sine dönüş yoktur. EXP-006 açık kalır; kısa sunum için çalışma bütünlüğü küçültülmez.
