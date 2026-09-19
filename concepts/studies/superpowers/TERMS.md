# Superpowers — Bağlamlı kullanım kayıtları

2026-09-19, **B6-T5 / KALICI-AKTARIM-KISMİ**. İlk kalıcı grup, giriş/skill seçimi/host aktarımıdır. **[TERMS-ENTRY.md](TERMS-ENTRY.md) bu dosyayla birlikte tam okunur.** Gerçek 52 dosyalık kapsam, okumalar ve devam noktası [READING.md](READING.md)'dedir. Yöntem [v0.3-working](../../METHOD.md); global kapsam [S1](../../SCOPE.md); güncel çalışma yetkisi [concepts/STATE.md](../../STATE.md).

Bu dosya araştırmanın terimleri ne için kullandığını kaydeder. Terimin genel doğrusu, güncel ürün rehberi, kurulmuş sistem, benimsenmiş mimari veya bütün araştırmaların ortak sözlüğü değildir. CMH'nin kapanmış çıkarımı yeniden açılmadı; onun şeması bu pakete dayatılmadı.

## 1. Kaynak ve aktarım kimlikleri

- Araştırma repository'si: **batuhanozgun/agentic-os-search**.
- Sabit kaynak/pilot ref'i: **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847**.
- Kaynak yolu: **research/studies/superpowers/**.
- Paket tree: **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12**; 19 kök dosya, 11 mekanizma notu, 6 sentez ve 16 betik/sonuç dosyası = 52.
- B6-T5 başlangıç main'i: **1108a483a811c3d5e22595f99179e51da8479f16**. Kök → research → studies ağaçlarından aynı paket kimliği doğrulandı; S1 ve P2 kaynak kapsamı değişmemiştir.
- Araştırmanın incelediği dış ürün: **obra/superpowers@b36e0829c6d0140e93cfef2ca599b1b07d4a7797**, manifest bağlamı 6.3.0. Bu araştırma ref'iyle aynı kimlik değildir.
- Araştırmadaki lab ve tarihsel assessor ayrı sabit kaynaklardır; gerçek bir son kullanıcı kurulumunun zorunlu bileşenleri sayılmaz. Kimlikleri kaynak META/STATE'dedir; bu tur dış kaynak doğrulaması yapılmadı.

Kaynak araştırmanın kendi durumu **BOUNDED-COMPLETE / USER-EVALUATED / ACCEPTED**. Bu, P2 concepts pilotunun kapanmasıyla veya bu kalıcı aktarımın tamamlanmasıyla aynı durum değildir. Kaynak not/sentez/CORE içindeki eski ACTIVE/PARTIAL/pending sözleri araştırmanın üretim anına aittir; güncel kaynak STATE bunları açıklamaktadır.

## 2. Açıklama ve kimlik anahtarı

Türkçe karşılıklar kaynak bağlantılı parafrazdır. Kaynak içinde ürün talimatı, kod gözleminin anlatımı, araştırmacının yerel deneyi, kamuya açık rapor, sentez ve proje yorumu birlikte bulunabilir. Söyleyen kaynak/rol ile ifadenin tanım, talimat, gözlem veya yorum oluşu ayrı belirtilir. Bir atfı okumak, atfedilen dış dosyayı bu tur okumuş olmak değildir.

SP01–SP179 görünür P2-T1–T5 pilot kayıtlarının adresleridir; bağımsız kavram sayısı değildir. Seçili parçalarda pilot kimlikleri korunur; farklı kullanım/nesne varsa alt adres verilir. Aynı satırdaki karşılaştırma eş anlamlılık kabulü değildir. Henüz aktarılmayan kimlikler yok sayılmaz veya hafızadan tanımlanmaz. P2'nin görünür metni bu tur erişilebilirdi; yalnız durum özetinden kayıt uydurulmadı.

İki neden çalışma boyunca görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemediği için önemli dayanak/yorum/belirsizlik/değişiklik izlenebilir olmalı; aynı sözcük ortak anlamı garanti etmediği için kullanıcı onayı, kaynak kullanımı ve çıkarıcı yorumu teknik doğruluk yerine konmamalı.

## 3. Genel görünüm ve araştırmanın kendi dili

Bu bölümün kaynakları aşağıdaki sabit araştırma dosyalarıdır:

[CORE](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/CORE.md), [METHOD](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/METHOD.md), [META](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/META.md), [STATE](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/STATE.md), [INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/INDEX.md), [PLAN](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/PLAN.md), [CLOSURE-AUDIT](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/CLOSURE-AUDIT.md). Hepsi bu tur tam geri okundu; bütün referans verdikleri mekanizmalar tamamlandı sayılmaz.

| Pilot adresi / ifade | Araştırmadaki kullanım | Kaynak rolü ve sınır |
|---|---|---|
| SP01 — Superpowers | Skill/rol sözleşmeleriyle ifade edilen, host aktörleri ve araçlarınca yorumlanan, adapter'lar, dosya/Git yardımcıları ve isteğe bağlı görsel runtime ile desteklenen geliştirme yöntemi; yöntemin geliştirilmesi/değerlendirilmesi/dağıtılması ayrı süreç. | CORE §1/§6 ve META. Araştırmacının bütün açıklaması; ne yalnız prompt listesi ne kendi başına eksiksiz otonom runtime. Yeni genel agent tanımı değil. |
| SP177a — Semantic synthesis pyramid | Kaynak ve mekanizma okumalarından alt sistem/sistem açıklamasına ve yoğun CORE'a ilerleyen araştırma/yazım düzeni. | Kaynak METHOD giriş ve §3–4. Ürün bileşeni veya concepts'in yeni yöntemi değil. |
| SP177b — Evidence graph | Aynı kaynağın birden çok mekanizma ve senteze bağlanabildiği, kimlik ve sınırlamaları taşıyan kanıt ilişkisi. | Kaynak METHOD §4. Okuma hiyerarşisiyle aynı tür yapı değil; sentez tekrarı bağımsız destek olmaz. |
| SP177c — CORE | Alt araştırmayı kasıtlı olarak yoğunlaştıran kısa sonuç belgesi. | CORE giriş; METHOD §3.F. Kayıplı üst görünüm, alt kaynakların yerine geçmez. |
| SP178a — external-target | Araştırma nesnesinin belirli bir dış yapı olduğunu gösteren study sınıfı. | Kaynak META. Superpowers'ın kendi mimari modülü veya ürün kategorisi değil. |
| SP178b — BOUNDED-COMPLETE | Belirlenen kaynak ve açıklama sorusu için araştırmanın kapanış durumu. | Kaynak STATE; CLOSURE-AUDIT §1/§8. Bütün tarih/host davranışı veya ürün etkinliği doğrulanmış değil. |
| SP178c — USER-EVALUATED / ACCEPTED | Kullanıcının sınırlı araştırma teslimini ve amacına hizmetini değerlendirmiş/kabul etmiş olması. | Kaynak STATE, owner evaluation bölümü. Her kaynağın insan tarafından okunması, yeniden deney veya ürünün benimsenmesi iddiası değil. |

**Diğer yönetim/kanıt dili:** Kaynak METHOD §5'in target claim, instruction contract, implementation observation, local execution observation, host/model behavior, effectiveness ayrımı bu çıkarımda ürün terimleriyle karıştırılmaz. SOURCE-LEDGER'ın S/E kimlikleri dış kaynak/deney kayıtları; notlardaki F/Q kimlikleri araştırma bulgusu/sorusu; CLOSURE-AUDIT'teki LC1/LC2 final kaynak kontrolü açıklıklarıdır. SP kullanım adreslerinin yerine geçmezler.

CLOSURE-AUDIT §3–4 ve CORE §3/§7'nin route-specific alt aktör kuralı ve dört durma sınıfı sonraki U03 aktarımında korunacak. Güncel kapanışın eski notlardan daha sonra gelmesi, eski yerel deneyin başka sürümde yeniden çalıştırıldığı anlamına gelmez.

## 4. Kalıcı gruplar ve açık aktarım

| Grup | Şu anki durum / adresler |
|---|---|
| Giriş, skill seçimi, host aktarımı | [TERMS-ENTRY.md](TERMS-ENTRY.md): SP02–SP29, SP35–SP38, SP12a/b, SP161–SP166; kaynak notları, iki betik/çıktı çifti ve girişle ilgili S02 karşılıkları kontrol edildi. |
| Araştırmanın bütün/kanıt dili | Bu dosya: SP01 ve SP177a–c/SP178a–c. Root dosyaların diğer mekanizma ve proje açıklamaları ilgili sonraki gruplarla kapanacak. |
| Plan, çalışma alanı, görev, inceleme, test ve teslim | SP30–SP34, SP39–SP79, SP167–SP174; kalıcı ayrıntı aktarımı bekliyor. U02 ilk sırada. |
| Skill yazımı ve değerlendirme | SP80–SP121 ve SP179; U06 kaynak/kanıt zinciriyle birlikte aktarılacak. |
| Görsel yardımcı ve dağıtım | SP122–SP149, SP175–SP176; U07 notları ve ilgili betik/sonuçlarla aktarılacak. |
| Bütünsel ve proje-karşılaştırmalı sentez | SP150–SP160 ve diğer kayıtların ek kaynak ilişkileri; S05/S06/U08 kaynakları ve paket kapanışında kontrol edilecek. |

Bu tablo kalıcı dosyaları henüz bulunmayan gruplara dosya varlığı atfetmez. Başlangıç kapsamı 52 kaynak dosyasıdır; bu tur kalıcılaştırma için 15'i tam geri okundu. Tam okunmuş bir sentez ya da register, atıf yaptığı bütün alt mekanizmaların kayıtlarını otomatik kapatmaz.

## 5. İlk grubun ilişki görünümü

Araştırmanın giriş modeli: **ortak yöntem içeriği → hosta özgü keşif/taşıma → görünür talimat → mevcut isteğe uygun çağırma → host araçlarıyla eylem → sonuç**. Her ok zorunlu ayrı bileşen, tek sıra veya mekanik garanti değildir. N01/N01B ve S02 farklı yolların aynı işlevi değişik biçimde taşıdığını anlatır.

İkinci ilişki, yeniden giriş ile işe devam arasındadır. Bir prosedürün yeniden eklenmesi, etkin dosya sürümünün yenilenmesi ve önceki işin kabul/plan/kanıt durumuyla geri kazanılması ayrı sorulardır. U02/U03 bu son sorunun gerçek kayıtlarını açıklayacaktır. Buradan Superpowers'ın hiç süreklilik mekanizması olmadığı çıkarılmaz.

CORE'un geliştirme işi ile yöntemin değiştirilmesi için iki süreç anlatması başlangıç görünümüdür; bütün ayrıntıların kaynak-kapsamlı aktarımı tamamlandığında paket düzeyinde yeniden bağlanacaktır. İlk CMH çıkarımının Context/Memory/Harness düzeni bu paketin zorunlu bölümlendirmesi değildir.

## 6. B6-T5 aktarım/değişiklik kaydı

P2-T1 ve P2-T5'in görünür ilgili satırları kaynakla karşılaştırıldı. İlk kapanıştaki bootstrap istisnası ve hook/event-registration ayrımı erken satıra taşındı; yalnız ilk taslak kopyalanmadı. İki wrapper, mapping'in iş düzeni etkisi, cache/registration/session/message ömürleri, marker ile gerçek gövde, procedure re-entry/work recovery ve ölçüt-bağımlı PASS kayıt içinde görünürdür.

Kaynak rolü veya niteleyicide maddi bir tersine dönüş saptanmadı. Bu tur kullanılan tablo/parça düzeni METHOD v0.3-working içindedir; yeni yöntem sürümü veya üçüncü pilot oluşturulmadı. Kaynağın tanımlamadığı genel anlamlar genel literatürle doldurulmadı. Eski P2 satırlarına erişim yokmuş gibi yeniden üretim iddiası verilmedi; bu tur görünür ilgili pilot çıktısıyla kaynak kontrollü aktarım yapıldı.

Paket bütünlüğü kapanmadı. Bir sonraki iş, U02 ve ardından U03/U04/U05 kaynak/kanıtları üzerinden görevden teslimata kalan kayıtların aktarılmasıdır. Ayrıntılı dosya durumları ve kaynak kapsam hesabı READING'dedir. Ürün/host/API testi, bağımsız kavram doğrulaması veya ortak referans kabulü yapılmadı.