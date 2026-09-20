# Concepts — Güncel çalışma durumu

2026-09-20, **B6-T10**. Bu dosya araştırma bazlı terim/jargon çıkarımının global amaç, yetki, güncel iş ve devam kaynağıdır. Kaynak araştırmaların STATE dosyaları veya yerel READING/kullanım kayıtlarının yerine geçmez.

## 1. Güncel durum

**PILOTS-AND-B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / CMH-DURABLE-COMPLETE / SUPERPOWERS-DURABLE-COMPLETE / METHOD-v0.3-WORKING / POST-S1-ADDITIONS-PENDING-ACCOUNT.**

Kullanıcının “tamam. devam et lütfen.” talebiyle Superpowers'ın kalan S05/S06 ve U08-A/B/C kaynakları tam okundu; bütünsel/proje-karşılaştırmalı kullanım kaydı oluşturuldu ve 52 dosyalık package envanteri kaynak/pilot/delta açısından kapatıldı. **52/52 benzersiz package dosyası B6'da tam geri kazanılmıştır; Superpowers için bekleyen kullanım aktarımı yoktur.** Bu sayı ürün deposunun bütün dosyaları veya bağımsız doğrulama seviyesi değildir.

Final kontrolde yerel READING envanterinde `syntheses/S05-native-system-model.md` satırının iki kez yazıldığı bulundu. Duplicate kaldırıldı; gerçek kaynak ağacında eksik dosya yoktu. Tarihsel P2 SP150–SP160 satırlarının özgün metni durable repoda bulunmadığından birebir kimlik eşlemesi uydurulmadı; METHOD §8 ile S05/S06/U08 kaynaklarından U08-R01–R23 source-controlled regeneration yapıldı.

| İş | Güncel durum |
|---|---|
| Amaç, iki risk, başlangıç hazırlığı | Tamamlandı; ORIGIN/SETUP-REVIEW tarihsel kaynak. |
| B1/B2 ve B3/B4 | İki konuşma pilotu ve yöntem değerlendirmeleri tamam; yeni pilot yok. |
| B5 | SCOPE/S1 başlangıç kapsamı, sahiplik, sıra ve delta ilkeleri teslim edildi. |
| B6 — CMH | Durable-complete. |
| B6 — Superpowers | **Durable-complete; 52/52 kaynak, altı kullanım parçası + ana TERMS/READING.** |
| B6 — sıradaki paket | **ai-knowledge-strategies**; henüz concepts kalıcı çıkarımı başlamadı. |
| B6 — diğer S1 birimleri | Başlangıç sırası SCOPE'da; kalıcı çıkarımları kapanmadı. |
| S1 sonrası eklenen kaynaklar | agentmemory, claude-swap, cli-continues ve ponytail bilinen kapsam deltalarıdır; içerikleri bu çalışma adına henüz sınıflandırılmış/çıkarılmış sayılmaz. |
| B7/B8 | Küresel geçiş kontrolü ve ortak referans değerlendirmesi başlamadı. |

S1 başlangıcının 33 biriminden **CMH ve Superpowers** kalıcı çıkarım bakımından kapanmıştır. 33 güncel studies evreninin eksiksiz toplamı değildir; S1 sonrası yeni yolların sahiplik/dosya/okuma hesabı ayrıca yapılacaktır. Kaynak araştırmanın kabulü, pilot kapanışı ve concepts durable closure ayrı statülerdir.

## 2. Etkin giriş ve sıradaki yetkili iş

Superpowers artık etkin kısmi paket değil, kapanmış kaynak pakettir. Yeniden başlatılacak iş değildir. Gerekirse [READING.md](studies/superpowers/READING.md), [TERMS.md](studies/superpowers/TERMS.md) ve altı bağlı parça birlikte okunur: ENTRY, WORK, VERIFICATION-DELIVERY, EVOLUTION-EVALUATION, RUNTIME-DISTRIBUTION, SYSTEM-PROJECTION.

**Sıradaki yetkili iş B6-T11:** `research/studies/ai-knowledge-strategies/` paketine canonical preflight ile gir:
- güncel main ve gerçek package tree/file envanterini bağla;
- package META/STATE/INDEX ve package'in kendi cold-start/authority yolunu tam recover et;
- kaynak araştırmanın tamamlanma durumu ile concepts çıkarım durumunu ayır;
- bütün dosyaları tam okuyarak bu araştırmadaki terim/jargon kullanımlarını kendi bağlamında çıkar;
- gerekirse `concepts/studies/ai-knowledge-strategies/READING.md` ve `TERMS.md` oluştur; önceki CMH/Superpowers şemasını ontoloji olarak dayatma.

S1 sonrası eklenen dört bilinen study yolu kapsam dışında bırakılmaz; seri sıra ve B7 öncesi scope-delta hesabında gerçek ağaçlarıyla işlenecekler. Bu yolların varlığı, ai-knowledge-strategies'e geçmeyi yasaklayan yeni phase değildir; yalnız bütün seri tamamlanmadan B7/B8'e geçilemeyeceğini güçlendirir.

B7/B8 ortak değerlendirmesi yetkili sıradaki iş değildir. Bütün research/studies kaynak kapsamı ve maddi deltalar tamamlanmadan ikinci aşama başlamaz.

## 3. Amaç, derinlik ve iki risk

İlk aşama research/studies araştırmalarını tam okuyarak her birinin kendi bağlamında kullanım ve ilişkilerini çıkarmaktır. İkinci aşama bütün çıkarımları tam okuyup ortak referansı değerlendirmektir. İlk pilotun/CMH'nin şeması, hazır sözlük veya kullanıcının açıklayıcı örnekleri sonraki paketlere başlangıç ontolojisi yapılmaz. Kaynakta tanım bulunması veya concepts'e yazılması ortak kabul değildir.

Her concepts turunda iki neden kısa ve görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişiklik izlenebilir olmalı. Ortak sözcükler aynı anlamı garanti etmiyor; kullanıcı onayı, kaynak kullanımı ve assistant yorumu teknik doğruluk yerine geçmemeli. Kullanıcı teknik uzman oracle değildir; ham düşünce değil, denetlenebilir sonuç ve kısa gerekçe gerekir.

Kaynağın genel tanım vermediği kullanımı açık bırakmak geçerli çıktıdır; okunmamış dosya veya atlanmış açıklama gerçek eksiktir. Yalnız genel bilgiyi artıracak ve mevcut aktarımı değiştirmeyecek okuma eklenmez. Açık kaynak soruları kendiliğinden yeni deney/literatür borcu olmaz. Talimat, kod anlatımı, geçmiş yerel deney, dış yazar raporu, sentez ve yeni yorum ayrılır; tekrar bağımsız destek değildir.

P2'nin önceki gruplarındaki özgün satırlar kalıcı aktarım sırasında erişilebilir olduğu ölçüde kullanıldı; B6-T10'da tarihsel SP150–SP160 satır metni güvenilir biçimde recover edilemedi. METHOD §8 uygulanarak sabit kaynaktan U08-R regeneration yapıldı; STATE/summary'den birebir SP anlamı uydurulmadı. Tam ve değişmemiş gerçek içerik sırf yeni tur diye mekanik tekrarlanmaz; eksik zorunlu kontrol veya kaynak canonical yoldan geri kazanılır.

## 4. B6-T10 gerçek çalışma ve Superpowers kapanışı

Superpowers araştırma ref'i **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847**, package tree **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12**. B6-T10 başlangıç main'i **9fdbb21779647ff84bdd2354a7c1cb15b4392f4e** idi. Pinned research ref → başlangıç main karşılaştırmasında `research/studies/superpowers/**` altında source delta yoktu.

Kalan beş tam kaynak: `syntheses/S05-native-system-model.md`, `syntheses/S06-project-facing-contribution-and-comparison.md`, `SOURCE-LEDGER-U08A.md`, `SOURCE-LEDGER-U08B.md`, `SOURCE-LEDGER-U08C.md`. Böylece B6 okuma hesabı **52/52 benzersiz dosya** oldu. 19 kök + 11 notes + 6 syntheses + 16 evidence yapısı yeniden kontrol edildi.

Yeni [SYSTEM-PROJECTION](studies/superpowers/TERMS-SYSTEM-PROJECTION.md) parçası S05/S06/U08 dilini ürün-native terminology'den ayırır: native whole-system model, development-work loop/method-change loop, composition register, stage/action authority, selected-task vs pursuit coverage, common adequate+available view, side information, authority/capability, qualification/adaptation ve selective comparator dili burada araştırmacı sentezi olarak tutulur.

P2'nin tarihsel SP150–SP160 aralığı birebir recovery edilemedi. Exact legacy mapping yapılmadı; U08-R01–R23 source-controlled regeneration kullanıldı. Bu, pilot kaydının kaybolduğu sınırı görünür tutar ve kaynakta olmayan eşleme üretmez.

Final source-side coverage check:
- bütün 52 benzersiz package yolu T5–T10 okuma turuna bağlı;
- P bekleyen dosya yok;
- kalıcı ana TERMS + altı kullanım parçası bütün kullanım gruplarını adresliyor;
- U08-C challenge ve Q13/Q20/Q24/Q47 gibi açık sınırlar çözülmüş diye işaretlenmedi;
- özgün research/studies/superpowers dosyaları concepts yazılarıyla değiştirilmedi;
- somut açık kullanım aktarım borcu bulunmadı.

READING tablosundaki duplicate S05 satırı source omission değil yerel kayıt hatasıydı ve düzeltildi. Aynı-assistant kontrol bağımsız verification veya sıfır-atlama garantisi değildir; yine de METHOD'in mevcut kapanış eşiğinde paketi sürekli açık tutacak somut borç kalmadı.

## 5. Yetki ve yazma kapsamı

Yetki ORIGIN/U01–U05, sonraki devam talepleri ve kaynakla sınırlı derinlik açıklamasıdır. Superpowers kapanışı yeni ortak tanım, ürün adoption, Foundation mutation veya mimari yetki üretmez.

B6-T10 dört concepts yolunu değiştirir: yeni `concepts/studies/superpowers/TERMS-SYSTEM-PROJECTION.md`; mevcut `TERMS.md`, `READING.md` ve bu `concepts/STATE.md`. Önceki beş kullanım parçası, global INDEX, METHOD/PLAN/SCOPE/CHARTER/ORIGIN/SETUP-REVIEW, CMH, özgün studies, Foundation ve agent-control bu iş adına değiştirilmedi. Yeni branch, duplicate study/META/CATALOG kaydı, kurulum veya dış ürün mutation'ı yoktur.

Normal B6 devamında ai-knowledge-strategies için gerekli concepts dosyalarının oluşturulması mevcut seri çıkarım yetkisinin içindedir; yeni phase onayı değildir.

## 6. Değişen korpus ve değişmez devam kayıtları

SCOPE/S1 ref'i **9b46155e904560c90b89e657f3d0d4e00e2e46cf**, studies tree **f51a44bf86ca25a0025f248e5116faae1ed3933a**. Başlangıç kapsamı 29 kök araştırma, Carbon koleksiyonu ve üç video idi; bu tablo current bütün-evren sayacı değildir.

B6-T10 başlangıcı **9fdbb21779647ff84bdd2354a7c1cb15b4392f4e**. Concepts yazımlarından önce main bu commit ile aynıydı. SYSTEM-PROJECTION **2b15badd54eaa0928d18b361f684a80eaf122b1d**, ana TERMS kapanışı **6b3bc091d8c110f73f20c05ec8fd7ba0af422249**, local READING kapanışı **ffc3ef85cdac99c5862ea9463b87203353baa793** commit'leriyle yayımlandı. Bu STATE öncesi main **ffc3ef85cdac99c5862ea9463b87203353baa793**; başlangıçtan fark yalnız bu üç Superpowers concepts yoluydu.

**Bekleyen kapsam deltası:** `agentmemory/META.md`, `claude-swap/META.md`, `cli-continues/META.md`, `ponytail/META.md`. İçerikleri concepts açısından henüz çıkarılmış sayılmaz. Bunlar eski S1'de yok diye dışlanmayacak; bütün seri ve B7 öncesi tree/META/STATE/INDEX hesabına girecek. Sonradan eklenen başka study yolları da aynı ilkeye tabidir.

Önceki ECC/katalog ve başka oturum değişiklikleri korunmuştur; Superpowers kapanışı bunları concepts adına geri almaz veya okunmuş saymaz. Açık maddi kapsam deltası varken B8 ortak referansa geçilmez.

| Değişmez kayıt | Korunan kapsam |
|---|---|
| [P1 kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/53c29b54a355742960f466a06a5d9bba0a42f412/concepts/STATE.md) | Sekiz kaynaklı ilk pilot/B2. |
| [P2/B4 kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/29b07b6529618f9a654d44a86e3ed6b05b8b40f9/concepts/STATE.md) | 52 kaynaklı pilot, checkpoint'ler ve v0.3 yöntemi. |
| [CMH kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/382cda3e653d802f461bad745f59bbea39bdbaa7/concepts/STATE.md) | İlk durable-complete paket. |
| [Superpowers B6-T9](https://github.com/batuhanozgun/agentic-os-search/blob/9fdbb21779647ff84bdd2354a7c1cb15b4392f4e/concepts/STATE.md) | 47/52 checkpoint ve U07 kapanışı. |
| [Superpowers B6-T10 READING](https://github.com/batuhanozgun/agentic-os-search/blob/ffc3ef85cdac99c5862ea9463b87203353baa793/concepts/studies/superpowers/READING.md) | 52/52 benzersiz dosya, duplicate düzeltmesi, source regeneration ve package closure. |

Eski checkpoint next'leri güncel iş değildir.

## 7. Yayın kontrolü ve yeni oturum

SYSTEM-PROJECTION, TERMS ve READING yayımlanan sürümlerinden geri okunup makinece kapsam kontrolüne tabi tutuldu: inventory satırları **52**, benzersiz yollar **52**, duplicate **0**, bekleyen `P` **0**. Ana TERMS yeni parçaya bağlı ve READING durable-complete durumunu taşıyor. Pinned Superpowers research ref → current main karşılaştırmasında özgün `research/studies/superpowers/**` değişikliği yoktu.

Bu STATE önceki blob **3a40286588c38a93e9f4171004c20bb91be4a7fd** üzerine yazılır. Kendi henüz bilinmeyen commit'ini uydurmaz. Yayından sonra gerçek parent/diff ve main'e yerleşim kontrol edilir. Bu kontroller aktarım/continuity içindir; bağımsız kavram doğrulaması veya ürün testi değildir.

Yeni oturum: AGENT/tetiklenen protokoller → concepts/INDEX zorunlu okumaları → bu STATE. Normal devam **ai-knowledge-strategies preflight ve kalıcı çıkarımıdır**. Superpowers yalnız gerektiğinde durable-complete kaynak olarak geri çağrılır; tekrar current work yapılmaz. B7/B8 hâlâ gelecekteki aşamalardır.

