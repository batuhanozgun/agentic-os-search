# Concepts — Güncel çalışma durumu

Tarih: 2026-09-19, B6-T2. Program: araştırma bazında terim/jargon kullanımlarının çıkarımı, ardından bütün çıkarımların ortak değerlendirilmesi. Bu dosya global amaç/yetki/current-work kaynağıdır; özgün araştırmaların STATE dosyalarının veya yerel çıkarım READING kayıtlarının yerine geçmez.

## Durum

**PILOTS-AND-B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / CMH-CONTEXT-AND-D2-MEMORY-RECORDED / FIRST-PACKAGE-PARTIAL / METHOD-v0.3-WORKING.**

Kullanıcının “süper!. devam et” talebiyle B6-T2 yürütüldü. İlk paketin bellek kaynağı tam okundu, kullanımlar sabit kaynaktan yeniden çıkarılarak kalıcı kayda alındı ve kaynağın otuz bölümünden döküme kapsam kontrolü yapıldı. Context kayıtları korundu. D3 harness, D4 paket-geneli aktarım ve bütün paket kapanış kontrolü hâlâ açık; tamamlanmış kalıcı araştırma paketi henüz yok.

| İş | Güncel durum |
|---|---|
| Amaç, iki risk ve ilk repo hazırlığı | Tamamlandı; ORIGIN/SETUP-REVIEW tarihsel kayıtları korunur. |
| B1/B2 — İlk pilot ve değerlendirme | Tamamlandı; sekiz dosyalı context-memory-harness-engineering pilotu. |
| B3/B4 — İkinci pilot ve değerlendirme | Tamamlandı; 52 dosyalı Superpowers pilotu, v0.3-working ve kalıcı kayıt düzeni. |
| B5 — Seri kapsam hazırlığı | SCOPE/S1 teslim edildi; kapsam/sahiplik/sıra biliniyor, bütün kaynak içerikleri okunmuş değil. |
| B6 — Araştırma bazlı kalıcı çıkarım | Aktif; CMH context ve D2 bellek kayıtları mevcut. Bellek kısmı kaynak kontrollü yeniden üretimdir; özgün pilot yanıtıyla birebir eşleşme iddiası yok. |
| B7 — Bütün kapsam ve delta geçiş kontrolü | Başlamadı. |
| B8 — Ortak referans değerlendirmesi | Başlamadı; ortak tanım, Foundation veya mimari kabulü yok. |

## Şimdi okunacak yer ve sıradaki iş

**Etkin paket:** context-memory-harness-engineering.

1. [READING.md](studies/context-memory-harness-engineering/READING.md): sekiz dosyanın envanteri, gerçek okumalar, bölüm kapsam kontrolü, erişim sınırı ve devam.
2. [TERMS.md](studies/context-memory-harness-engineering/TERMS.md): korunan context kullanımları ve bağlı parça girişi.
3. [TERMS-MEMORY.md](studies/context-memory-harness-engineering/TERMS-MEMORY.md): D2 kaynak kontrollü bellek kullanımları; ayrıca tam okunur.
4. [SCOPE.md](SCOPE.md): global kaynak evreni, sahiplik, sıra ve delta ilkeleri.

**Sıradaki yetkili iş B6-T3:** aynı kaynak ref'indeki `research/studies/context-memory-harness-engineering/03-HARNESS-ENGINEERING.md` içeriğini tam geri kazan; harness kullanımlarını kaynak bağlamı, atıf/araştırma/yeni yorum ayrımı ve ilişki görünümüyle kalıcı kayda ekle. D2'nin bilgi/metadata handoff'unu aktör/iş/oturum devriyle birleştirme. Tarihsel K07 tasarım amacı ile gerçekten sağlanmış özellik düzeltmesini koru. Sonra D4 paket-geneli mekanizma/proje/ilişki kayıtları, özellikle tarihli Development OS kullanımı ve sekiz dosyadan son kapsam/delta kontrolü gelir.

D2'yi yapılmamış iş gibi yeniden başlatma. Pilot kapanışını da pilot yanıtının bütün satırlarının bugün görünür olması sanma. Gerekli özgün yanıt erişilemiyorsa METHOD §8'in sabit kaynaktan yeniden üretim yolunu kullan; eski numaralara tahmini anlam atama. Ayrıntılı kayıt kimlikleri ve açık kalan işler yerel READING'de; bu STATE ikinci terim arşivi değildir.

CMH'nin bütün kalıcı kaynak kapsamı kapandıktan sonra SCOPE sırasındaki Superpowers aktarımına geçilir. Yeni üçüncü pilot, genel harness araştırması veya ürün testi açılmaz. B7/B8 tüm kapsamdan önce başlamaz. B5 ve tamamlanmış pilotlar sırf eski sohbet görünmüyor diye tekrar yapılmaz.

## Amaç, derinlik ve iki risk

Önce research/studies araştırmaları kendi bağlamlarında tam okunarak kullanımları ve ilişkileri çıkarılır. Bütün çıkarımlar tamamlanınca kayıtların tamamı okunarak ortak değerlendirme yapılır. Bir pilotun şeması sonraki araştırmanın başlangıç ontolojisi değildir. Kaynakta tanım bulunması veya concepts dosyasına yazılması ortak tanım kabulü değildir.

Her concepts turunda iki neden kısa ve açık görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemiyor, dolayısıyla önemli yorum/dayanak/belirsizlik/değişiklik izlenebilir olmalı; ortak sözcükler aynı anlamı garanti etmiyor, dolayısıyla kullanıcı onayı, kaynak kullanımı ve assistant yorumu teknik doğruluk bakımından ayrı tutulmalı. Kullanıcı teknik uzman oracle değildir. Ham düşünce dökümü değil, denetlenebilir sonuç ve kısa gerekçe gerekir.

Derinlik sınırı, kaynak araştırmanın kullanım/ilişki düzenini sadık aktarmaktır. Kaynakta tanımlanmamış genel anlamı açık bırakmak geçerli çıktı; okunmamış dosya veya atlanmış açıklama gerçek eksiktir. Yeni okuma yalnız genel kavram bilgisini artıracak, mevcut aktarımı değiştirmeyecekse ilk aşamaya eklenmez. Bağımsız terim araştırması, genel sözlük, ürün kurulumu, canlı deney veya mimari seçimi yoktur.

Ürün talimatı, kaynak gözlemi, araştırmacının yerel deneyi, kamuya açık geçmiş rapor, başka study'den aktarım, araştırma sentezi ve yeni çıkarım yorumu ayrı tutulur. Kaynak atfı dış çalışmanın bu tur okunduğunu göstermez; tekrar eden sentez bağımsız destek değildir. Araştırma dosyalarının eski next/deney/agent talimatları etkin kontrol veya yeni çalışma yetkisi değildir.

## Yetki ve bu turun değişiklik kapsamı

Kaynak yetki ORIGIN/U01–U05, sonraki devam talepleri ve kaynakla sınırlı derinlik açıklamasıdır. Pilotlar, değerlendirmeler ve kalıcı seri çıkarım özgün kullanıcı sırasının parçalarıdır. Aynı amaç yeniden onaylatılmaz; maddi amaç/kapsam/aşama değişikliği ayrıca değerlendirilir.

B6-T2 yalnız dört yolu yazar: yeni `concepts/studies/context-memory-harness-engineering/TERMS-MEMORY.md`; aynı yerde mevcut `TERMS.md` ve `READING.md`; bu `concepts/STATE.md`. Büyük kaydı bağlı parça halinde tutmak mevcut METHOD/INDEX düzeninin izin verdiği yerleşimdir. Global INDEX → TERMS → bellek parçası tam-okuma yolu korunur; duplicate study, META veya CATALOG satırı yaratılmaz.

METHOD v0.3-working, PLAN, INDEX, SCOPE, CHARTER, ORIGIN ve SETUP-REVIEW bu tur değişmedi. AGENT/protokoller, özgün studies paketleri, Foundation, explorations, publications ve diğer oturumların ECC/katalog değişiklikleri concepts adına değiştirilmedi. Yeni branch, upstream mutation, ürün çalıştırma veya dış kaynak kampanyası yoktur. Özgün CMH araştırmasının complete/değerlendirme bekliyor, Superpowers'ın complete/user-accepted statüleri concepts ilerlemesiyle karıştırılmaz.

## Kaynak kapsamı ve korunan geçmiş

S1 kaynak commit'i **9b46155e904560c90b89e657f3d0d4e00e2e46cf**, studies tree **f51a44bf86ca25a0025f248e5116faae1ed3933a**. Bu ağacın tamamı kapsamda: 29 kök araştırma, bir Carbon koleksiyon düzeyi ve üç video çocuğu olmak üzere 33 çıkarım birimi. Planlı paketler, kütüphane destek dosyaları ve emekli taşınma pointer'ları dışlanmaz. En özel kaynak öneki dosyanın çıkarım sahibidir; koleksiyon/çocuk ve türetilmiş sentezler bağımsız kanıt diye çoğaltılmaz. Kesilmiş araç görünümü tam dosya envanteri veya tam okuma değildir. Bütün yaprakların durumu yerel READING'de açılır; SCOPE başlangıç keşif sütunu kaynak paketinin güncel STATE'inin yerine geçmez.

CMH/P1 kaynak ref'i **ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a**, paket tree **e32d7736c4a3b31f123ab84eaafe053b0b2ca08e**. P1 ile S1'deki sekiz Markdown blob'un eşitliği B6-T1'de kontrol edildi; bu turki compare'larda ilgili kaynak değişmedi. P2 Superpowers kaynak ref'i **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847**, tree **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12**. Bu sürümler dış ürünün bugünkü davranışı veya güncelliği konusunda yeni doğrulama değildir.

- [P1 kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/53c29b54a355742960f466a06a5d9bba0a42f412/concepts/STATE.md): sekiz dosyalık pilot, P1-T1–T3, B2 ve eski çıktı erişim sınırı.
- [P2/B4 kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/29b07b6529618f9a654d44a86e3ed6b05b8b40f9/concepts/STATE.md): 52 dosya ve tüm P2 okuma checkpoint'leri, v0.3 kararı.
- [B5/B6-T1 kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/d5c337386a9ff1d44a96b803b066df79550d4331/concepts/STATE.md): kapsam/sahiplik, manifest kontrolleri, context aktarımı, yayınlar ve o andaki ECC deltası.

Bu kayıtların eski next durumları tarihsel; bugünkü çalışma talimatı değildir. Carbon'un kalan sekiz pointer'ı ilgili koleksiyon okumasında ele alınacak; Git dışı medya hash'i veya eski konuşma varlığı canlı erişim sayılmayacak. B6-T1'in manifest yeniden hesaplaması bu tur tekrar yapılmış sayılmaz.

## B6-T2 — Gerçek çıktı ve yorum sınırı

D2 `02-AGENT-MEMORY-ENGINEERING.md`, blob **6203b06fe56cad61354e9093d0b404a1ee3592c7**, bu tur **1–220, 221–440, 441–660, 661–880, 881–EOF** aralıklarıyla tam okundu; son istek üst sınırı 1040 gerçek satır sayısı değildir. D0/D1 ve girişlerin önceki tam erişilebilir metinleri kullanıldı; D3/D4 bu tur yeni okunmuş sayılmadı. Okuma sırasında kullanım notları tutuldu, sonra D2 §1–30'dan kalıcı kayda kapsam kontrolü yapıldı. Ayrıntılı karşılık tablosu READING'dedir.

TERMS-MEMORY, D2-U01–U37 ile ana kullanım gruplarını; temsil/statü/güncelleme/çağırma seçeneklerini, zaman ve metadata alanlarını, değerlendirme sorularını, aday proje sınıflarını, işletim/bağlama seçimlerini ve yalnız adı geçen kaynak/açık-soru dilini ayrı adreslerle taşır. Bunlar bağımsız kavram sayısı veya benimsenmiş şema değildir. Context'in K01/K02, C01–C28 ve E-CTX kayıtları değiştirilmedi; D2'nin aynı sözcük kullanımları ayrı kaynak bağlamında eklendi.

**Özgün pilot aktarımı sınırı:** P1 bellek dökümünün özgün yanıt metni bu turun erişilebilir görünümünde yoktu. METHOD §8 uyarınca kaynak kontrollü yeniden üretim yapıldı. K03/K04/K08, M01–M28 ve H17 eski referanslar olarak korunur; yeni D2 adresleriyle birebir eşleşmeleri tahmin edilmedi. Tekil memory ve bilgi/metadata handoff gibi kaydedilmiş konular D2'den yeniden ele alındı; bu konu bağlantısı eski satır metninin kurtarılması değildir. D2 kaynak çıkarımının tamamlanması, eski pilotun birebir arşivlenmesi veya bütün CMH aktarımı değildir. Kaynağa erişim ile eski yanıta erişim farklı sınırlardır.

Maddi ayrımlar: sistem/yaşam döngüsü, disiplin ve tekil kayıt; gözlem/kayıt/geçerlilik zamanı; kalıcılık ve kaynak otoritesi; geniş internal/external tanımı ile parametrik uyarlama karşılaştırması; dış benchmark'a atfedilen yetenekler ile araştırmacının önerdiği değerlendirme matrisi; bellekten bağlama bilgi devri ile oturum devamı; kullanım yolundan çıkarma ile türetilmiş kopya silme. Son üç kapsam açıklamasının ilgili yeni yorumları kullanım dosyasında etiketlidir; evrensel kavram çözümü ilan edilmez.

Geri okumada trajectory karşılığı eylem/gözlem dizisi olarak, scoped memory ilgili kişi/proje ile sınırlandırılmış bellek olarak netleştirildi; U26'nın yerel bölüm atfı kaynak D2 bölüm numarasıyla karışmayacak biçimde düzeltildi. İki çeviri açıklığı ve atıf düzeltmesi kayıtta izlenir; eski kaynak veya context kayıtları değiştirilmedi.

## Kaynak deltası ve eşzamanlı çalışma

Başlangıç main **045a6b9ead784f4e59b0b035f1ae6d5534fb7f26**. Önceki d5c3373… kapanışından buraya compare yalnız ECC PLAN/QUESTIONS/STATE/ROUND-U11-E, yeni evidence/U11-E-SOURCES ve Note23 değişikliklerini gösterdi.

Bu STATE öncesi son gözlenen main **cd2e8f5ab00bfae915f97336778c24946848a85a**. Başlangıçtan bu commit'e compare on commit ve dokuz yol gösterdi: üç yerel concepts dosyamız; studies/CATALOG; ecc/INDEX, META, yeni PUBLICATION-U11-E, ROUND-U11-E ve STATE. Kontrol dosyaları ve CMH/Superpowers kaynakları değişmedi. Bu compare anındaki farktır; sonraki değişiklikler ayrıca kontrol edilir.

ECC/katalog değişiklikleri geri alınmadı ve S1'e sessizce karıştırılmadı. ECC işlenirken S1'den o günün gerçek paketine tam delta geri kazanılacak; B7 öncesinde bütün studies ağacı tekrar karşılaştırılacak. Yeni/değişmiş/taşınmış dosyalar veya paketler sessizce kapsam dışına çıkmaz. Bu iş, ECC'nin araştırma devamını veya kaynak findings'ini concepts adına yönetmez.

## Yayın ve yeni oturum kontrolü

Yayınlar: bellek parçasının ilk içeriği **06803d350a9ce76138bfb0886fb4c55f46655a10**; ana TERMS yönlendirmesi **e5c5ac6a26900bf10af5e9fcc61b9d723f7fd73d**; READING **429990ceb7e1ef6b328f16a9fd97dceba3724e7b**; bellek açıklık düzeltmesi **cd2e8f5ab00bfae915f97336778c24946848a85a**. Belleğin ilk içeriği kesilen görünümü örtüşen aralıklarla tamamlayarak tam geri okundu. Düzeltmenin gerçek diff'i ve değişmiş canonical bölümleri ayrıca okundu. TERMS 1–50, 51–90, 91–EOF; READING 1–60 ve 61–EOF tam geri okundu. TERMS gerçek diff'i context kullanım gövdesinin korunduğunu ve yalnız giriş/kaynak durumları/tarihsel iz/yeni parça bağlantısının değiştiğini gösterdi.

Cold start: AGENT ve tetiklenen protokoller → concepts/INDEX → STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE → etkin READING → TERMS ve bağlı bütün kullanım parçaları → gerekli sabit kaynaklar. Yeni oturumda zorunlu girişler ve etkin kayıtlar tam okunur. Aynı konuşmada erişilebilir ve değişmemiş tam okumalar mekanik tekrarlanmaz. Eksik zorunlu kontrol/kaynak içerikleri tahmin edilmez.

Bu STATE, önceki blob **f7bd4f7e2c893dae8fbce2ed526ec8cca0081d6f** üzerine yazılır. Kendi henüz bilinmeyen commit'i veya yapılmamış kontrol sonucu burada üretilmez; yayın sonrasında tam geri okuma, gerçek parent→commit değişiklik kapsamı ve main'e yerleşim kontrol edilir. Bu kontroller kaynak/temsil ve devam tutarlılığına ilişkindir; bağımsız kavram doğrulaması, gerçek yeni-oturum deneyi, ürün etkinliği veya drift'in önlendiğinin kanıtı değildir.
