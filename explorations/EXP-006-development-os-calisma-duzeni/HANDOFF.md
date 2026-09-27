# EXP-006 — HANDOFF

**Güncelleme:** 27 Eylül 2026, P3 konsolidasyonu.  
**Devralma:** **P3 CONSOLIDATED WORKING DRAFT v0.4 / DISCUSSION.** D021 içerik–çalışma alanı sorumluluk ayrımı kabul; bütün P3 detayları aday. P3 kapanmadı, P4–P6 başlamadı.  
**Üst amaç:** SOUL'u geliştirecek Claude Code cloud ekibinin çalışma düzeni; assistant'ın SOUL backlog'unu seçmesi değil.

## 1. Okuma ve kayıt yolu

[STATE](STATE.md)→HANDOFF→[WORK](WORK.md)→[DECISIONS](DECISIONS.md)→[ACTORS](ACTORS.md)→[U002](sources/U002-cloud-plan-and-autonomy.md)→[P1-01](work/P1-01-claude-cloud-environment-map.md)→[P2-01](work/P2-01-named-role-contracts.md)→[P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı konuşmada tam unchanged içerik tekrar yüklenmez.

Üst plan yalnız WORK; current STATE; ayrıntılı P3 taslağı yalnız P3-01. ACTORS/P2 ilk sözleşme tabanıdır; P3 hedef-profili düzeltmeleriyle birlikte değerlendirilir. İlk 16 sözleşme 16 ajan değildir. Tarihsel S1/B current/next metinleri bu sırayı değiştirmez.

## 2. Son konuşmanın yönü

Kullanıcı iki koordinasyonu ve iki denetim hedefini ayırmamızı istedi. Assistant bunu çok küçük turlarda tekrar etti; kullanıcı, kısa sunumun az ilerleme veya her adımda yeni komut anlamına gelmediğini açıklaştırdı. v0.2 bütünlüklü G/Y taslağı, v0.3 rol konuşmaları ve kayıt/devir örneği üretti.

Sonra kullanıcı asıl vurgusunun iş içeriğinden ziyade kullanılan yapının, dosya/klasörlerin düzeni ve yeniden kullanılabilirliği olduğunu açıkladı. Assistant'ın içerik sahibi–düzen sahibi sınırına “aynı fikirdeyim” diyerek katıldı ve P3'ü toparlayıp devam istedi. Görünür kaynak P3-01 §1'de, kabul kapsamı D021'de.

**Artık yeniden sorulmayacak:** Düzen yalnız teknik runtime veya klasör estetiği değildir. Dosyaların yeri, current/taslak/eski ayrımı, bulunması, kaynak/karar bağı, bakımı, yeniden kullanımı ve yeni oturumda işe yaraması asli sorumluluktur. İçeriğin doğruluğu ve ürün kararı alan sahibinde kalır. Kullanıcı bütün şema/ajan/işletim ayrıntılarını kabul etmiş sayılmaz.

## 3. P3'ün birleşmiş çalışma resmi

- **G:** SOUL için doğru işi keşif/planlama, araştırma, tasarım/üretim ve içerik/sonuç güvencesi.
- **Y:** Bu çalışmanın katılım, iletişim, araç/erişim, bağlam, kalıcı alan düzeni, bakım, tekrar kullanım ve devri; bunların fiilî kullanılabilirliğinin güvencesi.

İkisi de DevOS içinde Work/reasoning'dir; G/Y, F1–F8 ile aynı sınıflama veya iki kapalı ekip değildir. DR06-G öncelik/bağımlılıkları, DR06-Y gerçek çalıştırma/bakım/devri koordine eder. DR13-G içerik/sonuç iddiasını, DR13-Y çalışma koşulları ve çalışma alanı kullanılabilirliğini sınar. Aynı olumlu sonuç veya farklı ajan ismi bağımsızlık sağlamaz.

DR07 yer/statü/sürüm/indeks/yaşam döngüsü bütünlüğünü; DR08 uzmanla birlikte gerekli bağlamı; içerik sahibi kendi sonuç ve gerekçesini taşır. DR07 tüm dosyaların tek yazıcısı veya domain doğruluk hakemi değildir. Araştırma/sınama/teşhis/öğrenme iki hedefte gerektiği ölçüde kullanılabilir; otomatik çift kadro kurulmaz.

## 4. v0.4 ile eklenen somut işletim kuralları

P3-01 §4 mantıksal alanları gösterir: SOUL ürünü, DevOS iş/devamı, kaynak/karar/kanıt, çalışma tarifleri/tekrar kullanım. Taslak/current/arşiv yaşam durumlarıdır; fiziksel klasör ağacı P4'te seçilir.

§5 talep/çalıştırma/teslim/kullanım/karar durumlarını ve itirazın karşılığını ayırır. Her küçük danışma ayrı Work değildir; farklı sahip, bekleme/devir, önemli kaynak veya bağımlılık doğarsa izlenir. Kanıt açığı idari onayla kapatılamaz; tasarım tercihi yetkili alan kararıyla gerekçelendirilebilir. Y kısıtı bildirir, ürün önceliğini seçmez.

§6 olay→sorumlu→kalıcı karşılık→devam koşulu bakım sözleşmesidir. Üretim, current yayını, devir, eşzamanlı değişiklik, yeniden kullanım ve arşiv tek döngüde ele alınır. Önemli yanlış kaynak/yetki/devir kusuru ilgili tüketimi tutabilir; kozmetik bakım bütün ekibi durdurmaz. Fiziksel arşivleme aktif keşiften çıkarmakla aynı değildir. Yeni dosya/kural sayısı ilerleme ölçütü değildir.

§7 bitmemiş soru, dayanak, açık itiraz, beklenen katkı, sahip ve dönüşü korur. Gecikmiş yanıt current sonucu ezmez. Kayıt restore'u dış etki restore'u değildir; belirsiz etkide kör retry yoktur. Kaynak güncellendi diye alternatif destekle geçerli kalan karar otomatik iptal edilmez.

v0.3 kurgusal örneği sabit Git sürümünde korunur; ÖR kimlikleri gerçek backlog/koşu/karar değildir. Bu toparlama yeni P3 dosyası veya paralel plan oluşturmadı.

## 5. Sabit sınırlar ve kanıt

K1 talep→çalışma→yanıt→kullanım, K2 rutin rol değişimini Batu'nun tetiklememesidir. Başlatma/yeniden başlatma, gerçek müdahale, yetki ve kabul mümkündür. İlk/sonraki SOUL işini ekip keşfeder; assistant'ın örneği gerçek görev seçimi değildir.

P1 Q01–Q06 cloud araç/erişim/izin/kalıcılık ve güvence yükleri açık. P4 seçiminde yük taşıyan yol hedefli doğrulanır. Kanon/v2/ECC/Hermes/Gas Town bütünü benimsenmedi. S1-16 full-read qualification'ı S1-17 §7'de korunur.

Bu tur Hermes META ve Note30 tam okundu; arşiv/aktif keşif, bakım yetkisi, sınırlı restore ve yükleme≠etkin kullanım ayrımları kullanıldı. Eski study yorumu, güncel ürün testi değildir. Önceki Foundation/Studies kapsamı P3-01 §9 ve bağlantılı v0.3 kaynak izindedir. Yeni runtime/mesaj/restore/yazma yarışı deneyi yoktur.

## 6. Sonraki bütünlüklü P3 işi

**İki eşzamanlı iş + ortak kayıt değişikliği + açık inceleme itirazı + oturum kesintisi** tek senaryoda izlenecek. Her adımda hangi yetkili sahip, tüketici, kalıcı durum ve sonraki tetik var? Hangi bilgi geçerli; hangi sonuç yalnız aday; kim neyi yeniden açabilir? Bu, aynı G/Y ayrımını yeniden anlatmak değil, mevcut kuralların birleşiminde kalan semantik açığı aramaktır.

Yeni rol veya yeni ürün şeması varsayılan çıktı değildir. Maddi açık kalmazsa P3'ün tasarım kapanışı ve P4'e taşınacak gereksinimler hazırlanır. Genel auditler çoğaltılmaz. P4/P5 mekanizma ve ilk bootstrap karşılıklarını, P6 gerçek davranışı sınayacaktır; P3 metninin varlığı bunları doğrulamaz.

Son kullanıcı yönüyle P3 toparlandı ve bakım sözleşmesi ilerletildi; bunu kısa ama bütünlüklü sun. Kullanıcının değerlendirmesi aynı taslağa işlenir. Her küçük ayrımda onay bekleme; P4'e de sessizce atlama. Bu güncelleme agent-control değişikliği değildir.
