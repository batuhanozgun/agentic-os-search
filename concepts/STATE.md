# Concepts — Güncel çalışma durumu

Tarih: 2026-09-19. Program: araştırma bazında terim/jargon kullanımlarının çıkarımı, ardından bütün çıkarımların ortak değerlendirilmesi. Bu dosya concepts çalışmasının global amaç/yetki/current-work kaynağıdır; özgün araştırmaların STATE dosyalarının veya yerel çıkarım READING kayıtlarının yerine geçmez.

## Durum

**PILOTS-AND-B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / FIRST-PACKAGE-PARTIAL / METHOD-v0.3-WORKING.**

İki konuşma pilotu ve yöntem değerlendirmeleri tamamlanmış olarak korunur. Kullanıcının “tamam. çalışmaya başlıyoruz artık sanırım. devam et lütfen.” talebiyle B5'in sürümlü kapsam/sahiplik/sıra kaydı oluşturuldu ve B6 kalıcı çıkarımı başladı. Bu tur ilk pilotun context bölümü kaynak kontrolüyle kalıcılaştırıldı; bütün ilk paketin veya bütün seri çıkarımın tamamlandığı iddia edilmez.

| İş | Güncel durum |
|---|---|
| Amaç, iki risk ve ilk repo hazırlığı | Tamamlandı; ORIGIN/SETUP-REVIEW tarihsel kayıtları korunur. |
| B1/B2 — İlk pilot ve değerlendirme | Tamamlandı; sekiz dosyalı context-memory-harness-engineering araştırması. |
| B3/B4 — İkinci pilot ve değerlendirme | Tamamlandı; 52 dosyalı Superpowers pilotu, v0.3-working ve kayıt düzeni. |
| B5 — Seri kapsam hazırlığı | SCOPE/S1 oluşturuldu: kaynak ağacı, bütün dosya evrenini bağlayan Git manifestleri, paket/çocuk/pointer sahipliği, pilot deltası ve sıra. Bütün araştırma içerikleri okunmuş değildir. |
| B6 — Kalıcı araştırma bazlı çıkarım | Aktif; ilk paketin TERMS ve READING dosyaları var, yalnız context bölümü aktarılmıştır. Tamamlanmış kalıcı paket henüz yoktur. |
| B7 — Bütün kapsam ve delta geçiş kontrolü | Başlamadı. |
| B8 — Ortak referans değerlendirmesi | Başlamadı; kabul edilmiş ortak tanım veya mimari yoktur. |

## Şimdi okunacak yer ve sıradaki iş

**Etkin paket:** context-memory-harness-engineering.

- [Yerel okuma ve aktarım durumu](studies/context-memory-harness-engineering/READING.md).
- [Kalıcı kullanım kayıtları](studies/context-memory-harness-engineering/TERMS.md).
- [Global kapsam, sahiplik ve sıra](SCOPE.md).

**Sıradaki yetkili iş B6-T2:** yerel READING ve TERMS'i tam geri kazan; aynı kaynak ref'indeki 02-AGENT-MEMORY-ENGINEERING.md ile P1'in ilgili görünür kullanım kayıtlarını kontrol ederek bellek bölümünü kalıcı kayda ekle. K03/K04/K08 ve M01–M28'in dayanak, kapsam, yorum ve gerekiyorsa alt kullanım adreslerini koru. Sonra D3 harness ve D4 paket-geneli ilişki/mekanizma kayıtları gelir. Ayrıntılı sıra, kalan kayıtlar ve bölüm kontrolü yerel READING'dedir; burada ikinci bir terim arşivi tutulmaz.

İlk paketin bütün kalıcı aktarımı ve kaynak taraflı son kapsam/delta kontrolü tamamlanınca SCOPE sırasındaki Superpowers aktarımına geçilir. İki pilotu baştan yapılacak yeni araştırma gibi açma. B5'i sırf önceki konuşma görünmüyor diye yeniden başlatma; gerekli kaynak/çıktı recovery'sini yap. B7/B8 bütün kapsam tamamlanmadan başlamaz.

## Amaç, derinlik ve iki risk

Önce research/studies araştırmaları kendi bağlamlarında tam okunarak kullanımları ve ilişkileri çıkarılır. Bütün çıkarımlar tamamlanınca kayıtların tamamı okunarak ortak değerlendirme yapılır. Bir pilotun şeması sonraki araştırmanın başlangıç ontolojisi değildir. Dosyada terim bulunması ortak tanım kabulü değildir.

Her concepts turunda iki neden kısa ve açık görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemiyor, dolayısıyla önemli yorum/dayanak/belirsizlik/değişiklik izlenebilir olmalı; ortak sözcükler aynı anlamı garanti etmiyor, dolayısıyla kullanıcı onayı, kaynak kullanımı ve assistant yorumu teknik doğruluk bakımından ayrı tutulmalı. Kullanıcı teknik uzman oracle değildir. Ham düşünce dökümü değil, denetlenebilir sonuç ve kısa gerekçe gerekir.

Derinlik sınırı kaynak araştırmanın kullanım/ilişki düzenini sadık aktarmaktır. Yeni okuma yalnız terim hakkındaki genel bilgiyi artıracak ama bu aktarımı değiştirmeyecekse ilk aşamaya eklenmez. Kaynağın tanımlamadığı anlamı açık bırakmak geçerli çıktı; atlanmış dosya veya açıklama ise gerçek eksiktir. Genel sözlük, bağımsız terim araştırması, ürün kurulumu, canlı deney veya mimari seçimi yoktur.

Ürün talimatı, kod/gözlem aktarımı, araştırmacının yerel deneyi, kamuya açık geçmiş rapor, başka study'den karşılaştırma, araştırma sentezi ve yeni çıkarım yorumu ayrı tutulur. Sentez tekrarı bağımsız destek değildir. Atfı okumak, dış bağımlılığın veya başka study'nin kendi concepts çıkarımını tamamlamaz. Araştırma dosyalarındaki eski next/deney/agent talimatları etkin kontrol veya yeni çalışma yetkisi değildir.

## Yetki ve yazma sınırı

Kaynak yetki ORIGIN/U01–U05, sonraki devam talepleri ve kaynakla sınırlı derinlik açıklamasıdır. Pilotlar, değerlendirmeler ve kalıcı seri çıkarım özgün kullanıcı sırasının parçalarıdır. Aynı amacı tekrar onaylatmak gerekmez. Maddi amaç, kapsam veya aşama değişikliği ayrıca değerlendirilir.

Bu B5/B6-T1 turunun yazdığı altı yol: concepts/SCOPE.md; concepts/studies/context-memory-harness-engineering/TERMS.md ve READING.md; concepts/INDEX.md, PLAN.md ve bu STATE.md. Üç dosya yeni, üçü mevcut güncellemedir. METHOD v0.3-working, CHARTER, ORIGIN ve SETUP-REVIEW değişmedi. AGENT/protokoller, özgün studies paketleri, Foundation, explorations, publications ve diğer oturumların ECC/katalog değişiklikleri korunur. Yeni branch, upstream değişiklik, ürün çalıştırma veya dış kaynak kampanyası yoktur.

Özgün CMH araştırması kendi STATE'inde complete/değerlendirme bekliyor; Superpowers kendi STATE'inde complete/user-accepted. Bu farklı statüler, concepts pilotu veya kalıcı aktarımın durumu değildir ve bu çalışma nedeniyle değiştirilmez.

## B5 — Teslim edilen kapsam ve sınırı

S1 kaynak commit'i **9b46155e904560c90b89e657f3d0d4e00e2e46cf**; research/studies tree **f51a44bf86ca25a0025f248e5116faae1ed3933a**. Kapsam yalnız bitmiş araştırmalar değil, bu ağacın tamamıdır. Bütün kaynak dosyaları tam ve değişmez Git ağaçlarıyla hiyerarşik olarak bağlandı; her paketin bütün yaprak dosyaları B6 sırasında yerel READING'de ayrı açılır. Global dosyada bütün yaprak adlarının ikinci kopyası veya bütün dosyaların okunduğu iddiası yoktur.

Doğrudan kök manifesti 31 dizin + 3 destek dosyası taşır. Bunlar 29 ayrı araştırma, bir Carbon koleksiyonu ve bir emekli pointer dizinidir. Carbon'un üç video çocuğuyla birlikte 33 çıkarım birimi vardır; bu sayı bağımsız kanıt veya tamamlanma yüzdesi değildir. En özel kaynak öneki dosyanın çıkarım sahibidir. Koleksiyon ve çocukları, aynı bulguyu bağımsız destek olarak çoğaltmaz. Karşılaştırmalı work-management paketi ile ilgili kardeş hedefler de birbirinin tam okuması yerine geçmez.

CATALOG, library INDEX ve PACKAGE-CONTRACT tam okundu. SCOPE'taki araştırma olgunluğu sütunu katalogdan türetilmiş başlangıç keşif bilgisidir; her paketin META/STATE'ini okumak yerine geçmez. Planlı sekiz paket kapsamda kalır: mevcut kayıtlar okunacak, yapılmamış ürün araştırması uydurulmayacak. Library INDEX'in eski Superpowers active/partial satırı kaynak paketinin accepted STATE'inden üstün sayılmadı; studies dosyaları yeniden yazılmadı.

Carbon META/STATE ve üç çocuklu videos ağacı tam kontrol edildi. Emekli harness-engineering-and-evolution dizininin dokuz pointer dosyası kapsamda; README tam okundu, kalan sekiz pointer Carbon'un destek okumasında hesaba katılacak. Önceki konuşmalardaki Git dışı medya varlığı/hash'i canlı erişim değildir; gerekli temsil ve erişim sınırı ilgili paket işlenirken açıkça tutulur.

Kök 34 girdinin, Carbon videos'un üç girdisinin ve CMH'nin sekiz girdisinin kip/ad/SHA verileriyle yerel Git tree yeniden hesaplamaları canonical tree kimlikleriyle eşleşti. Bu mekanik manifest aktarım kontrolüdür; bağımsız anlam doğrulaması veya ürün testi değildir. Kesilmiş recursive araç çıktısı bütün yaprakların okunması sayılmadı.

## B6-T1 — Gerçek kalıcı çıktı

CMH kaynak ref'i **ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a**; paket tree **e32d7736c4a3b31f123ab84eaafe053b0b2ca08e**. P1'in sekiz kaynak blob'u S1 ile aynı. P2'nin **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847** ref'indeki Superpowers tree'si **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12** de S1'de değişmemiştir. Bu kontroller dış ürünlerin bugün güncelliğini veya davranışını yeniden doğrulamaz.

B6-T1'de CMH META, STATE, INDEX, D0 gerekçe ve D1 Context Engineering tam geri okundu. D0: 1–160, 161–340, 341–EOF; D1: 1–190, 191–390, 391–620, 621–EOF. D2/D3/D4 bu tur yeniden içerik kontrolü yapılmadı; önceki pilotta okunmuş olmaları yeni okuma diye sayılmadı. Tam sekiz dosya manifesti ve ayrıntılı okuma/aktarım tablosu yerel READING'dedir.

TERMS'e K01/K02, C01–C28 ve önceden açıklanmış on değerlendirme başlığı E-CTX-01–10 aktarıldı. Farklı kullanımlar bazı .a/.b alt adresleriyle ayrıldı. Bunlar bağımsız kavram sayısı değildir. D0/D1 kaynak noktaları, söyleyen ve açıklama niteliği korunur. Context bölümünün ilişki görünümü ve kaynak tarafından bölüm hesabı yazıldı; bu, D4'ün bütün paket sentezi değildir.

Maddi sınırlar: atfedilen dar tanım ile araştırmanın operasyonel genişletmesi; saklama/erişim/görünürlük; kaynak/türetilmiş görünüm; araç arayüzü/sonucu; kapasite/işte etkili kullanım; bilgi düzeni/gerçek yükleme ayrıldı. Önceki kaynak güven etiketleri yeni teknik doğrulama sayılmadı. Genel tanımı verilmemiş adlar bu statüleriyle kaldı. Bellek, harness, genel mekanizma/proje kullanımları ve P1 ilişki eklerinin aktarımı hâlâ bekliyor.

## Kaynak deltası ve eşzamanlı çalışma

Bu STATE yazılmadan önce gözlenen main **7f65dc36a6a9a2c9990d020bb4e70f6fed9f9d0d**. S1 kaynağından bu commit'e tam compare, beş mevcut concepts yazımızın yanında şu studies değişikliklerini gösterdi: CATALOG.md; ecc/INDEX.md, META.md, PLAN.md, QUESTIONS.md, ROUND-U11-D.md; yeni ecc/notes/22-BACKLOG-COORDINATION-AND-CONSUMPTION.md. Kaynak kontrol veya iki pilot paketi değişmedi.

Bu ECC/katalog deltaları S1'e sessizce karıştırılmadı ve geri alınmadı. ECC işlenirken S1 ile o günün canonical paketi arasındaki fark tam geri kazanılacak; yeni bulgular o paketin kayıtlarına uygun sürümle dahil edilecek. Bu liste yukarıdaki compare anına aittir; sonraki değişiklikler ayrıca kontrol edilir. B7 öncesinde bütün studies ağacı yeniden karşılaştırılır; yeni veya taşınmış paket/dosyalar dışlanmaz.

## Korunan pilotlar ve tarihsel kayıtlar

- [P1 kapanış STATE'i](https://github.com/batuhanozgun/agentic-os-search/blob/53c29b54a355742960f466a06a5d9bba0a42f412/concepts/STATE.md): sekiz dosyalık pilot, P1-T1–T3 ve B2.
- [P2/B4 kapanış STATE'i](https://github.com/batuhanozgun/agentic-os-search/blob/29b07b6529618f9a654d44a86e3ed6b05b8b40f9/concepts/STATE.md): P2-T1–T5'in bütün okuma checkpoint'leri, 52 dosya, kapanış, B4 ve v0.3 kararı.

Bu bağlantılardaki eski next-B5 veya dosyalar henüz yok ifadeleri tarihsel checkpoint'lerdir. Pilotun özgün kullanım çıktıları konuşmadadır; yerel TERMS yalnız gerçekten aktarılan kısmı taşır. Kaydedilmiş pilot sonucu sırf eski sohbet yok diye yeniden aktif yapılmaz. Henüz aktarılmamış kullanım gerekliyse görünür özgün yanıt ve kaynaklar geri kazanılır; yanıt erişilemiyorsa sabit kaynaktan yeniden çıkarılır ve yeniden üretim olduğu belirtilir. Global STATE özeti terim arşivi yerine kullanılamaz.

## Yeni oturum ve kapanış kontrolü

AGENT ve tetiklenen protokoller → concepts/INDEX → STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE → etkin yerel READING ve TERMS → gerekli kaynaklar. Yeni oturumda girişler ve etkin kayıtlar tam okunur. Aynı konuşmada tam, erişilebilir ve değişmemiş kaynaklar mekanik biçimde tekrar okunmaz. Zorunlu kontrol/kaynak erişilemezse içeriği tahmin edilmez.

Yazılan dosyaların commitleri: SCOPE **2d2d4aeb3df6923f87346e5eb810de65fd36c87c**; TERMS **68e1db7125150a44047adaf468e424c225e8462c**; READING **faea7163b3ac72a2d9ec80182cd9b79eb907f798**; INDEX **b86e961a82fe1d21545eb840deb4d3287f014d92**; PLAN **e324e7aec89ee482d46e5c6362769287ebb4de7f**. Bu beş dosya yayımlanan sürümlerinden tam geri okundu. PLAN'ın gerçek diff'i yalnız güncel başlangıç cümlesi ve R5 yürütme kaydı ekini gösterdi; yöntem değişikliği yapılmadı.

Bu STATE mevcut blob ce8650d18cb324ef59b4d073361b6d172e9da5a3 üzerinden güncellenir. Sonrasında kendi tam geri okuması, gerçek parent→commit kapsamı ve main'e yerleşimi kontrol edilir; henüz bilinmeyen kendi commit'i veya yapılmamış kontrol sonucu uydurulmaz. Yayın/manifest kontrolleri yerleşim ve süreklilik içindir; ürün etkinliği, bağımsız kavram doğrulaması veya drift'in ortadan kalktığına dair deney değildir.
