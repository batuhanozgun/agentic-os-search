# Superpowers — Bağlamlı kullanım kayıtları

2026-09-19, **B6-T6 / KALICI-AKTARIM-KISMİ**. Giriş/skill seçimi/host aktarımı ile U02–U03 plan/çalışma alanı/görevlendirme/inceleme grupları kayıtlıdır. **[TERMS-ENTRY.md](TERMS-ENTRY.md) ve [TERMS-WORK.md](TERMS-WORK.md) bu dosyayla birlikte tam okunur.** Gerçek 52 dosyalık kapsam, okumalar ve devam noktası [READING.md](READING.md)'dedir. Yöntem [v0.3-working](../../METHOD.md); global kapsam [S1](../../SCOPE.md); güncel çalışma yetkisi [concepts/STATE.md](../../STATE.md).

Bu dosya araştırmanın terimleri ne için kullandığını kaydeder. Terimin genel doğrusu, güncel ürün rehberi, kurulmuş sistem, benimsenmiş mimari veya bütün araştırmaların ortak sözlüğü değildir. CMH'nin kapanmış çıkarımı yeniden açılmadı; onun şeması bu pakete dayatılmadı. ENTRY'nin B6-T5 tarihli U02 sırada ve erken rol görünümü henüz aktarılmadı ifadeleri tarihsel checkpoint'tir; güncel karşılık WORK ve bu dosyanın §4/§7'sindedir. ENTRY'nin kullanım gövdesi sırf eski durum cümlelerini silmek için yeniden yazılmadı.

## 1. Kaynak ve aktarım kimlikleri

- Araştırma repository'si: **batuhanozgun/agentic-os-search**.
- Sabit kaynak/pilot ref'i: **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847**.
- Kaynak yolu: **research/studies/superpowers/**.
- Paket tree: **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12**; 19 kök dosya, 11 mekanizma notu, 6 sentez ve 16 betik/sonuç dosyası = 52.
- B6-T5 başlangıç main'i **1108a483a811c3d5e22595f99179e51da8479f16**, kök → research → studies ağaçlarından aynı paket kimliğiyle doğrulanmıştı. B6-T6 başlangıcı **4b8c87486cebf0b80cac5dba39699e72e09ccc2f**; önceki kapanışla fark yalnız ECC kaydıdır. P2/S1 kaynak kapsamı bu kontrolde değişmedi.
- Araştırmanın incelediği dış ürün: **obra/superpowers@b36e0829c6d0140e93cfef2ca599b1b07d4a7797**, manifest bağlamı 6.3.0. Bu araştırma ref'iyle aynı kimlik değildir.
- Araştırmadaki lab ve tarihsel assessor ayrı sabit kaynaklardır; gerçek bir son kullanıcı kurulumunun zorunlu bileşenleri sayılmaz. Kimlikleri kaynak META/STATE'dedir; bu tur dış kaynak doğrulaması yapılmadı.

Kaynak araştırmanın kendi durumu **BOUNDED-COMPLETE / USER-EVALUATED / ACCEPTED**. Bu, P2 concepts pilotunun kapanmasıyla veya bu kalıcı aktarımın tamamlanmasıyla aynı durum değildir. Kaynak not/sentez/CORE içindeki eski ACTIVE/PARTIAL/pending sözleri araştırmanın üretim anına aittir; güncel kaynak STATE bunları açıklamaktadır.

## 2. Açıklama ve kimlik anahtarı

Türkçe karşılıklar kaynak bağlantılı parafrazdır. Kaynak içinde ürün talimatı, kod gözleminin anlatımı, araştırmacının yerel deneyi, kamuya açık rapor, sentez ve proje yorumu birlikte bulunabilir. Söyleyen kaynak/rol ile ifadenin tanım, talimat, gözlem veya yorum oluşu ayrı belirtilir. Bir atfı okumak, atfedilen dış dosyayı bu tur okumuş olmak değildir.

SP01–SP179 görünür P2-T1–T5 pilot kayıtlarının adresleridir; bağımsız kavram sayısı değildir. Seçili parçalarda pilot kimlikleri korunur; farklı kullanım/nesne varsa alt adres verilir. Aynı satırdaki karşılaştırma eş anlamlılık kabulü değildir. Henüz aktarılmayan kimlikler yok sayılmaz veya hafızadan tanımlanmaz. P2'nin görünür metni bu turlarda erişilebilirdi; yalnız durum özetinden kayıt uydurulmadı. WORK'teki U02/U03/S03 ek adresleri ilgili kaynakta bulunan yerel kullanımları taşır, yeni evrensel terim tanımı değildir.

İki neden çalışma boyunca görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemediği için önemli dayanak/yorum/belirsizlik/değişiklik izlenebilir olmalı; aynı sözcük ortak anlamı garanti etmediği için kullanıcı onayı, kaynak kullanımı ve çıkarıcı yorumu teknik doğruluk yerine konmamalı.

## 3. Genel görünüm ve araştırmanın kendi dili

Bu bölümün kaynakları aşağıdaki sabit araştırma dosyalarıdır:

[CORE](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/CORE.md), [METHOD](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/METHOD.md), [META](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/META.md), [STATE](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/STATE.md), [INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/INDEX.md), [PLAN](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/PLAN.md), [CLOSURE-AUDIT](https://github.com/batuhanozgun/agentic-os-search/blob/75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847/research/studies/superpowers/CLOSURE-AUDIT.md). Hepsi B6-T5'te tam geri okunmuştu; atıf verdikleri bütün mekanizmalar bununla tamamlanmış sayılmadı.

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

CLOSURE-AUDIT §3–4 ve CORE §3/§7'nin route-specific alt aktör kuralı ve dört durma sınıfı WORK'te U02/U03 kaynaklarıyla korundu. U05'e ilişkin koşullu cleanup sınırı sonraki grupta ayrıca kontrol edilecek. Güncel kapanışın eski notlardan daha sonra gelmesi, eski yerel deneyin başka sürümde yeniden çalıştırıldığı anlamına gelmez.

## 4. Kalıcı gruplar ve açık aktarım

| Grup | Güncel durum / adresler |
|---|---|
| Giriş, skill seçimi, host aktarımı | [TERMS-ENTRY.md](TERMS-ENTRY.md): SP02–SP29, SP35–SP38, SP12a/b, SP161–SP166. B6-T5'te kaynağa karşı kontrol edildi; bu tur gövdesi değişmedi. |
| Plan, çalışma alanı, görevlendirme ve inceleme | [TERMS-WORK.md](TERMS-WORK.md): SP30–SP34, SP39–SP61, SP167–SP170; SP28'in yeni aşama bağları ve yerel ek adresler. U02/U03, iki betik/sonuç çifti ve ilgili kaynaklar B6-T6'da karşılaştırıldı. |
| Araştırmanın bütün/kanıt dili | Bu dosya: SP01 ve SP177a–c/SP178a–c. Kök belgelerin diğer mekanizma ve proje açıklamaları sonraki gruplarla kapanacak. |
| Test, teşhis, doğrulama ve teslim/koruma | SP62–SP79, SP171–SP174; U04/U05 ve ilgili kanıtlar sırada. İnceleme grubundaki atıflar bu aktarımın tamamı değildir. |
| Skill yazımı ve değerlendirme | SP80–SP121 ve SP179; U06 kaynak/kanıt zinciriyle birlikte aktarılacak. |
| Görsel yardımcı ve dağıtım | SP122–SP149, SP175–SP176; U07 notları ve ilgili betik/sonuçlarla aktarılacak. |
| Bütünsel ve proje-karşılaştırmalı sentez | SP150–SP160 ve diğer kayıtların ek kaynak ilişkileri; S05/S06/U08 kaynakları ve paket kapanışında kontrol edilecek. |

Bu tablo henüz bulunmayan dosyaları mevcut göstermez. B6-T5'te 15, B6-T6'da sekiz ek araştırma dosyası tam geri kazanıldı: toplam 23/52. Diğer 29 dosyanın B6 geri kazanımı/aktarımı ve son kapsam kontrolü bekliyor. Tam okunmuş bir sentez/register, atıf yaptığı bütün alt mekanizmaların kayıtlarını otomatik kapatmaz. S02'nin U07 bağları ve S03'ün U05/U07/U08 bağları açıkça izlenir.

## 5. Kaynak-içi ilişki görünümü

Giriş modeli: **ortak yöntem içeriği → hosta özgü keşif/taşıma → görünür talimat → mevcut isteğe uygun çağırma → host araçlarıyla eylem → sonuç**. Her ok zorunlu ayrı bileşen, tek sıra veya mekanik garanti değildir. N01/N01B ve S02 farklı yolların aynı işlevi değişik biçimde taşıdığını anlatır.

B6-T6 bunu planlı SDD tarafında şu ilişkiyle bağlar: **uygun anlaşma → spec/plan ve ortak kısıtlar → erişilebilir çalışma alanı/brief → uygulayıcı raporu → inceleme ve kapsamın sonuçlandırılması → düzeltme veya gerekçeli açık-bulgu kararı → nitelendirilmiş kabul**. Sonraki entegrasyon ve kanıt koruma başka işlemlerdir; U05'e aittir. Üç giriş yolunu tek yazılı-plan/SDD hattına indirmiyoruz.

Prosedürün yeniden eklenmesi, etkin dosya sürümünün yenilenmesi ve işin kabul/plan/kanıt durumuyla geri kazanılması ayrı sorulardır. U02/U03 gerçek ledger, brief, rapor ve commit referanslarını anlatır; ENTRY'nin giriş-katmanı sınırı artık bu kayıtlara bağlanır. Bundan bütün devam sorunlarının çözüldüğü veya önceki açıklamada hiçbir kurtarma mekanizması bulunmadığı sonucu çıkarılmaz.

CORE'un geliştirme işiyle yöntemin değiştirilmesi için iki süreç anlatması başlangıç görünümüdür; bütün ayrıntılar aktarıldığında paket düzeyinde yeniden bağlanacaktır. CMH'nin Context/Memory/Harness düzeni bu paketin zorunlu bölümlendirmesi değildir.

## 6. B6-T5 — Korunan aktarım kaydı

P2-T1 ve P2-T5'in görünür ilgili satırları kaynakla karşılaştırılmıştı. Bootstrap istisnası ve hook/event-registration ayrımı erken satıra taşındı. İki wrapper, mapping'in iş düzeni etkisi, cache/registration/session/message ömürleri, marker ile gerçek gövde, procedure re-entry/work recovery ve ölçüt-bağımlı PASS kayıt içinde görünürdür.

ENTRY §6'nın başlığındaki ilk pilot ifadesi o tur P2 pilotu diye düzeltilmişti; kullanım anlamı değişmedi. B6-T5'in 15 tam geri okuması [yerel checkpoint'te](https://github.com/batuhanozgun/agentic-os-search/blob/53cc0647266228e3f5446bbe69a6d55b573a19a4/concepts/studies/superpowers/READING.md) korunur. Eski U02-next ifadesi bugünkü sıranın yerine geçmez.

## 7. B6-T6 — Maddi aktarım ve güncel devam

Görünür P2-T2 ile P2-T5'in kapanış ekleri N02/N03, kaynak kayıtları ve dört deney dosyası üzerinden karşılaştırıldı. SP28 aşama/nesneyle açıldı; task/step, worktree/scratch, brief/yeterli bağlam, rapor/kabul, tek reviewer/iki hüküm, deferred/parked/complete ve farklı inceleme uçları ayrı tutuldu. SDD alt aktör sınırı bütün paralel yollara genişletilmedi. Kaynaktaki dört durma sınıfı kısa sürüm anlatımıyla daraltılmadı.

SP167–SP170 kapanış ekleri ilgili yere dahil edildi. U02'nin plan adı/yolu/sürümü ve U03'ün commit farkı/çalışma kopyası gözlemleri eski kayıtla birlikte korundu. Geri çağırma güçlüğü gerçek kanıt yokluğuyla eşitlenmedi; gözlenen yardımcı davranışı gerçek model kararı gibi aktarılmadı. Maddi bir anlam tersine dönüşü saptanmadı; amaç/nesne ve koşul nitelemeleri daha ayrı adreslendi.

Bu kaynak ve görünür pilot karşılaştırması aynı assistant tarafından yapıldı; bağımsız doğrulama veya sıfır atlama garantisi değildir. Yöntem v0.3-working değişmedi. Kaynağın genel tanım vermediği veya açık bıraktığı mesele için yeni literatür/ürün kampanyası açılmadı. **Sıradaki iş U04 test/teşhis/doğrulama, ardından U05 teslim/koruma kayıtlarıdır.** Tam paket kapanışı, kalan kaynak/çıkarım grupları ve kaynak-delta kontrolünden sonra verilir.
