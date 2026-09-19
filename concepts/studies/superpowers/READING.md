# Superpowers — Okuma ve kalıcı aktarım durumu

2026-09-19, **B6-T5 / P2-PILOT-CLOSED / DURABLE-TRANSFER-ACTIVE / ENTRY-GROUP-RECORDED / PACKAGE-PARTIAL**. Bu, concepts içindeki yerel kapsam/okuma kaydıdır. Kaynak araştırmanın STATE'i ve global concepts/STATE.md ayrı yetki/durum yüzeyleridir.

## 1. Güncel iş ve devam

[TERMS.md](TERMS.md) ve [TERMS-ENTRY.md](TERMS-ENTRY.md) birlikte tam okunur. Giriş/skill seçimi/host aktarımı, ilgili deney dili ve araştırma yönteminin genel adları kalıcı kayıttadır. **Superpowers kalıcı paketi tamamlanmadı.** Kaynak araştırmanın ve 52 dosyalık P2 pilotunun tamamlanmış oluşu korunur; onlar yeniden yapılacak deneme değildir.

**Sıradaki yetkili iş B6-T6:** `notes/U02-approval-plan-workspace-handoff.md` ile `evidence/U02-handoff-probes.py` ve sonuç JSON'unu tam geri kazan; L0/S28–S36'nın ilgili bağlarını, görünür P2-T2 ve P2-T5 eklerini birlikte kontrol ederek plan, çalışma alanı, görev/bağlam ve kayıt kullanımlarını kalıcılaştır. Ardından U03 görevlendirme/inceleme/kabul ve kendi kaynak/kanıtları; U04 test/teşhis; U05 teslim/koruma gelir. Gerçek operasyonel kapasiteye göre bölünebilir; durum kaydı somut devam noktasını taşır.

İlk grubun SP28 onayı veya SP24 work recovery açıklaması sonraki role/aşama otomatik yayılmaz. CORE'un SP30–SP34 ilk rol görünümü U02/U03'le genişletilecek. P2-T5'in SP167–SP174 ekleri unutulmaz. Kaynaklı aktarım yapılır; ürünün yeni araştırması, host kurulumu, deney veya ortak tanım yapılmaz.

## 2. Kaynak bağlama ve gerçek kapsam

- Repository: **batuhanozgun/agentic-os-search**.
- Kaynak öneki: **research/studies/superpowers/**.
- P2 kaynak ref'i: **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847**.
- S1 başlangıç ref'i: **9b46155e904560c90b89e657f3d0d4e00e2e46cf**.
- Bu turun başlangıç main'i: **1108a483a811c3d5e22595f99179e51da8479f16**.
- Paket tree: **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12**; üç sürümde aynı.
- Güncel ana ağaçtan araştırmaya bağ: `research` tree **5d0efc37a85722f988937226270aa7a7f88c090e** → `studies` tree **0693c76d133d256df60b412a07c8481da41ae33d** → aynı Superpowers tree.

[19 dosyalı kök ve üç alt ağaç](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/56c19a5e2c0deb7b0f5164aac818ed2ba98baf12), [11 not](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/cc9611a59f65ec1175fd99885c01a6efebc202ed), [6 sentez](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/bfb0603d70683e512df789bfa52c929caa67d9ea), [16 betik/sonuç](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/7a5af9c7cf94551a42102bcfd9e2ddd36434cd9a) doğrudan alındı. İlk JSON içerikleri bütün girdileri ve truncated=false durumunu taşıyordu; tekrarlanan wrapper kopyasının kesilmesi dosya içeriği okuması gibi sayılmadı. Ağaç içeriği bu tur yeniden Git hash'ine hesaplanmış değildir.

Toplam **52 dosya: 36 Markdown, 8 betik, 8 JSON sonucu**. Bu ağaçta binary veya ek alt dizin yok. 19+11+6+16 hesabı gerçek yaprak envanteridir; dış Superpowers deposunun tüm dosya sayısı veya genel çalışma yüzdesi değildir. Atfedilen dış dosyalar ve diğer studies bu 52 araştırma dosyasının yerine sayılmaz.

Araştırmanın dış hedefi `obra/superpowers@b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, manifest bağlamı 6.3.0; lab `prime-radiant-inc/superpowers-evals@e64684cd1fa270c464ac797747e45bbe8d127e8b`; tarihsel assessor `prime-radiant-inc/gauntlet@db6c8e0fcf80889aa6d9631c99adec698f6c0caa` ve ayrı `25a2e3e00431f8d8eb63781162ccb974d43d5405` deltasıdır. Bu kimlikleri kaynak META/STATE'den okumak güncel dış ürün veya kampanya doğrulaması değildir.

## 3. Bütün dosyaların yerel envanteri

Bütün kaynak dosya kipleri **100644**. Yollar yukarıdaki kaynak önekine göredir. **R** = B6-T5'te tam içerik geri okundu; **P** = P2'deki tam okuma tarihsel olarak kayıtlı, bu tur içeriği yeniden geri kazanılmadı. P, kaynağın yapılmamış araştırma olduğu veya pilotun iptali değildir. R de o dosyanın bütün mekanizma atıflarının kalıcı aktarımı kapandı demek değildir. Daha ayrıntılı aralıklar §4'te.

### Kök — 19 dosya

| Yol | Blob SHA | Bu tur |
|---|---|---|
| CLOSURE-AUDIT.md | b6178fdc2817eaf93c447434a014ca971a972348 | R |
| CORE.md | 0986da960a4b3db5d1e09894c2abfd6d6ca114be | R |
| INDEX.md | c170993756d19c2d98831ca1dd371c5aadf3c53a | R |
| META.md | 80c32a688127ca811421c9579cd9fef7a1c0d6a9 | R |
| METHOD.md | 95f684306f92373dbb51f4ceedaff885394e950b | R |
| PLAN.md | ea86caa9144bfd462428a3c8ef3ffb6ab7d5ca00 | R |
| SOURCE-LEDGER-U03.md | 76075ba19f8012d9d2b582887a22c9edf2362d2d | P |
| SOURCE-LEDGER-U04.md | 113f818cbc47a28105b00a0d5578b73567a18be6 | P |
| SOURCE-LEDGER-U05.md | 3066325dda3a9d6f10b4181863ea642ece5eb59f | P |
| SOURCE-LEDGER-U06A.md | 3122010a6494f5a8d9b98a8d1a1edc39594a3aa9 | P |
| SOURCE-LEDGER-U06B1.md | 90e75d48a02e02c7a6aa55e6b3a8123469dfb690 | P |
| SOURCE-LEDGER-U06B2.md | 1e315c6bb3575a0f299d9c5d322fe5c60452c0b5 | P |
| SOURCE-LEDGER-U07A.md | d909ec43c39a7810eb5f4d27f8094d158f7c0610 | P |
| SOURCE-LEDGER-U07B.md | b91571c78b7152f4f4cb68d480662a3f4b2b1004 | P |
| SOURCE-LEDGER-U08A.md | 7d34445f2f1d3defd9af1d33d8c7df39df5822eb | P |
| SOURCE-LEDGER-U08B.md | 0213fce532c82b132decbfb95ed35a494fab71ae | P |
| SOURCE-LEDGER-U08C.md | fbca2a3b8ac21cc9849216682c95649bd969263f | P |
| SOURCE-LEDGER.md | a09cd522f1b51cec1d3fc9c30a017f8931e35dd2 | R |
| STATE.md | 472b9f16bd68d0e05a4108fb1b2155ee2b7a2d2f | R |

### notes/ — 11 dosya

| Yol | Blob SHA | Bu tur |
|---|---|---|
| notes/U01-entry-routing-and-bootstrap.md | 8b8e63451e77d78e7b9be4de190944157a8120f2 | R |
| notes/U01B-host-delivery-and-continuity.md | cc2c0ba68f8d90ec6680b9b4b2d7cc0bc3405620 | R |
| notes/U02-approval-plan-workspace-handoff.md | 20568d3bfe398e7e0ff43abf2cb29e84925834ae | P |
| notes/U03-delegation-review-and-acceptance.md | 4dfe415cf35386650a30fa7104e5537355276977 | P |
| notes/U04-testing-diagnosis-and-verification.md | 975d935ad98634624537571e77e38e4ec5268ee7 | P |
| notes/U05-delivery-cleanup-and-retention.md | d3e797780ffb14781361194e5d82799033f14b49 | P |
| notes/U06A-skill-authoring-and-change-admission.md | 469dbea119e410a11c2130bb94ff4e90ed34a7fc | P |
| notes/U06B1-evaluation-evidence-and-verdict.md | 54418ac55a5129cde6f0ee1ddf0c471f361a6a1d | P |
| notes/U06B2-assessor-contracts-and-evidence-qualification.md | adb00736fc90b481568a73288c81ce6929ad1f1a | P |
| notes/U07A-visual-companion-lifecycle.md | cb87245b449ff383af55af5f9e4dd50a15532c94 | P |
| notes/U07B-distribution-versioning-and-support.md | 2de6f304f2d7c3630b27cfdbe7291fe2e7f1b3fc | P |

### syntheses/ — 6 dosya

| Yol | Blob SHA | Bu tur |
|---|---|---|
| syntheses/S01-skill-evolution-and-evaluation.md | df93d7bcd127f3d31e82ab8dcc80b9668b0c7231 | P |
| syntheses/S02-availability-runtime-and-distribution.md | 0546c46231ef17da3cdb204520d7846176c27cfe | R |
| syntheses/S03-intent-planning-and-context-handoff.md | f69f5c99aefa2a6a13b4233ae49afd73dc2ce0ca | P |
| syntheses/S04-execution-verification-and-delivery.md | 54c77cc04e9d7f88900918f8ee63dd07dadb0e54 | P |
| syntheses/S05-native-system-model.md | 9044ebaa66c913b3b526935850715d62d421d262 | P |
| syntheses/S06-project-facing-contribution-and-comparison.md | 8ab988debc34b70efd55b4c6145a06a96c70b256 | P |

### evidence/ — 16 dosya

| Yol | Blob SHA | Bu tur |
|---|---|---|
| evidence/U01-hook-probes-results.json | 0a21d98568b71a7c1d99385b9d8ae88611ebed78 | R |
| evidence/U01-hook-probes.py | 9ca0b43739e69c930d1241601bb61b7ef1872ff1 | R |
| evidence/U01B-opencode-probes-results.json | fae46fb808c5814fc7039f874f7d9aae5e5b34f3 | R |
| evidence/U01B-opencode-probes.mjs | 6a99be598bac4d60943c816857124c907882c089 | R |
| evidence/U02-handoff-probes-results.json | c95be67a743b7e8526e9fe30a2198117aee61d50 | P |
| evidence/U02-handoff-probes.py | 5cf7d9dd25ade628743a3250158486c8349a6fb5 | P |
| evidence/U03-review-probes-results.json | 48ba0976e661c74fe20f9232836fcc2dc2debb19 | P |
| evidence/U03-review-probes.py | a1982668d06c8cf22783af60bfb5430839eb1b5c | P |
| evidence/U04-diagnostic-probes-results.json | 875f03b27e53b8a6013f2facbace833fd7478cb9 | P |
| evidence/U04-diagnostic-probes.py | 37ca1fe7d2ee6c0390e51f9eb56b281a26138eee | P |
| evidence/U05-lifecycle-probes-results.json | 565da2eaf7aa293eea5663dce74436c71bb7595b | P |
| evidence/U05-lifecycle-probes.py | a59ca7af17737f64fa8ed54c214b77ceecd522a5 | P |
| evidence/U07A-companion-client-probes-results.json | 2ceef31098d65cfda54bfa708ab0ed002632f37e | P |
| evidence/U07A-companion-client-probes.mjs | 27082457c9e782cfec1e392aa78e02677d54b735 | P |
| evidence/U07B-version-probes-results.json | be459537a1e14bbf5f75f4823b5e33d4db88644b | P |
| evidence/U07B-version-probes.py | 63763cce58982ab0c22002ca767765eaaec16f9f | P |

## 4. B6-T5 gerçek okuma aralıkları

**15 tam kaynak geri okuması; 37 dosyanın B6 geri kazanımı/aktarımı bekliyor.** Bu, ikinci kez 15 yeni araştırma yapılması veya bütün pilotun yeniden açılması değildir. Aralıklar gerçek içerik dönüşlerine göredir; EOF, içerik sonunun görüldüğünü belirtir, istek üst sınırı gerçek satır sayısı değildir.

| Dosya/kod | Tamamlanan okuma | Kalıcı kullanım durumu |
|---|---|---|
| META / INDEX / METHOD / PLAN | Her biri 1–EOF | Amaç/statü/araştırma dili; ilgili sonraki mekanizma atıfları açık. |
| Kaynak STATE | 1–65, 66–EOF | Güncel araştırma kabulü ve tarihsel/gerçek durum ayrımı. |
| CORE | 1–60, 61–EOF | SP01 genel görünüm; sonraki roller ve bütünsel sentez yeniden araştırılmadan kendi kaynaklarıyla aktarılacak. |
| CLOSURE-AUDIT | 1–55, 56–EOF | LC1/LC2 sınırları ve kaynak araştırma kapanışının doğrulama gücü; ilgili U03/U05 ekleri açık. |
| SOURCE-LEDGER / L0 | 1–48, 49–110, 111–EOF | S00–S27/E01–E04 kaynak rolleri; S28–S36/E05–E06 sonraki U02'ye bağlı. |
| N01 | 1–90, 91–EOF | §1–9 kaynak tarafından kullanım kontrolü tamam. |
| N01B | 1–70, 71–EOF | §1–10 kaynak tarafından kullanım kontrolü tamam. |
| S02 | 1–70, 71–EOF | Giriş/aktarımı ilgilendiren kısımlar bağlandı; U07 kaynaklı dağıtım/görsel ayrıntıları sonraki grupta. |
| E01-R, E01-O, E03-R, E03-O | Dört dosyanın her biri 1–EOF | Betik/ölçüt/çıktı birlikte okundu; hiçbir betik çalıştırılmadı. |

Diğer 37 içerik bu tur okunmuş gibi yazılmaz. Önceki P2 tam okumaları [P2/B4 kapanış STATE'i](https://github.com/batuhanozgun/agentic-os-search/blob/29b07b6529618f9a654d44a86e3ed6b05b8b40f9/concepts/STATE.md) ve oradaki değişmez checkpoint'lerle kayıtlıdır. Aynı konuşmadaki gerçek içerik kaybolmuşsa gerekli aralık tekrar geri kazanılır; yalnız geçmiş okuma iddiası yeni aktörün okuması yerine geçmez.

## 5. Kaynaktan kayda ilk grup kapsam kontrolü

| Kaynak bölümü | Kalıcı karşılık / sonuç |
|---|---|
| N01 §1–2 | TERMS-ENTRY SP25–29; üç giriş yolu, hazırlık/onay farkı, atılabilir kod ve plan sınırı. |
| N01 §3 | SP02–05, SP161/162; skill seçimi, process önceliği, görevlendirilmiş alt aktörün yalnız bootstrap istisnası ve kaynakta kullanıcı önceliği. |
| N01 §4 | SP09–15, SP163a, host/alan tablosu; kayıt, JSON biçimi, olay/ortam dalı ile tüketim ayrı. |
| N01 §5–7 | SP35–38, E01-R/O; fixture, ölçüt ve geçmiş sonuç; sağlık koşulu ürün vaadi yapılmadı. |
| N01 §8–9 | Kaynak-içi ilişki ve açık sonraki mekanizmalar; Q kimlikleri yeni yetki veya tanım araştırması değil. |
| N01B §1–2 | SP03/04/06–13, sekiz host satırı; native keşif/include/manifest/callback aynı uygulanmış garanti değil. |
| N01B §3 | SP18–22/SP165, Pi/Hermes ekleri; kaynak/modül/kayıt/oturum/mesaj ömürleri ayrı. |
| N01B §4 | SP15/SP166; eksik dosya, okunamama ve boş gövde yolları; tek evrensel fail-open/closed hükmü yok. |
| N01B §5 | SP16/17/164; araç eşlemesi iş düzeni değiştirebilir, namespace/path uyuşması varsayılmadı. |
| N01B §6–7 | SP35–38, E03-R/O; yerel fixture/elle callback, mechanism/health/oracle ayrımı, eksik/onarılmış ve aynı/yeni modül kontrolleri. |
| N01B §8 | SP23/24; prosedüre yeniden giriş ile iş kurtarma ayrımı. |
| N01B §9–10 | Dağıtım/host kalifikasyonunun sınırları, soru/geçiş adları; U02/U06/U07 kalıcı gruplarına bağlandı. |
| S02 §1–2, §4'ün giriş kısmı, §6–7 | Aktarım/etkinleştirme ve doğru tüketim ilişkileri; U07 alt kaynaklarıyla ilgili kısımlar tamamen aktarıldı sayılmadı. |
| Kaynak METHOD §1–9 | TERMS SP177, kanıt/statü dili ve ENTRY/SP162; ürün yöntemiyle araştırma yöntemi ayrıldı. |
| META/STATE/INDEX/PLAN/CORE/closure | TERMS SP01/SP178; kaynak kabulü, kayıplı üst görünüm, tarihsel sonraki işler; mekanizma/proje ayrıntıları sonraki kayıtlarla kontrol edilecek. |
| L0 + E01/E03 | Kaynak ve deney kimlikleri ayrıldı; S00–S27 mevcut giriş grubunu destekler, S28–S36'nın görevlendirme mekanizmaları sıradadır. |

Bu kontrol çıktıdan kelime saymak yerine kaynak tarafındaki bölüm/tablo/liste/örnek ve kod/sonuç alanlarından yapılmıştır. N01/N01B giriş grubu için bulunan açıklanmış aktarım eksiği açık bırakılmadı. Kaynakta yalnız adlandırılmış alanlar ve skill kataloğu bağlamıyla korunur; bağımsız genel tanımı bulunmayan terimler sözlükten doldurulmaz. U02 ve sonraki grupların açık oluşu giriş grubunun genel terim araştırmasına çevrilmesini gerektirmez.

## 6. Pilot bağı, yorum ve sınırlar

P2-T1/T5'in ilgili özgün satırları bu tur görünürdü; SP01–29, SP35–38, SP12a/b, SP161–166 ve SP177–178 kaynakla karşılaştırılarak kaydedildi. SP30–34 erken rol görünümü U02/U03'e bırakıldı. Bütün SP satırlarının kalıcı aktarımı yapılmış sayılmaz. Gelecekte özgün yanıt erişilemezse METHOD §8'in kaynak kontrollü yeniden üretimi uygulanır; STATE özetinden anlam tahmin edilmez.

Önemli korunmuş ayrımlar: talimat/yardımcı/host; discovery/invocation/delivery; wrapper metni/betiği; mapping/fallback'ın anlamı; kaynak/modül/kayıt/oturum ömürleri; generic marker/güncel gövde; procedure re-entry/work recovery; ölçütün sonucuyla deney toplama başarısı. Kuralın zorunlu dili veya kullanıcının kabulü gözlenmiş etkinliğe dönüştürülmedi. Kaynağın önbellek davranışını bilinçli tercih olarak ele alabilmesi korundu.

Kontrol aynı assistant'ın kaynak/pilot karşılaştırmasıdır; bağımsız doğrulama veya bütün anlamlar için sıfır atlama garantisi değildir. Yeni ürün testi, upstream tarama, model çağrısı, kurulum veya kaynak düzeltmesi yapılmadı. Kaynak araştırmanın kabul durumu değişmez.

## 7. Yayın ve kapsam korunması

Bu turun planlanan yazma kapsamı yeni TERMS-ENTRY.md, TERMS.md ve bu READING.md; mevcut global concepts/INDEX.md ve STATE.md'dir. Yöntem, plan, SCOPE/S1, CHARTER/ORIGIN, CMH'nin kapanmış dosyaları, kaynak studies, Foundation, agent-control ve diğer çalışmalar değiştirilmez. Yeni branch veya ikinci study/META/CATALOG satırı yok.

İlk içerik commitleri: TERMS-ENTRY **210b40e70291680b016ea8353968c97f6c40b3d6**; TERMS **0179671bd79d9d0f31a37d2d16b9a6f687ba7149**. ENTRY yayımlanan sürümünden 1–60, 61–120, 121–EOF ile tam geri okundu. Diğer yayın geri okumaları ve gerçek değişiklik kapsamı global STATE ve sonuç mesajında kontrol anına göre yer alacak; henüz bilinmeyen kendi commit'i veya yapılmamış kontrol burada yazılmıyor.

Önceki CMH kapanışı 382cda3e… ile 1108a483… başlangıcı arasındaki on commit yalnız CATALOG ve ECC dosyalarını etkiledi: INDEX/META/PLAN/QUESTIONS/ROUND-U12-A/STATE ile yeni PUBLICATION-U12-A, evidence/U12-A-SOURCES, notes/24-EXECUTION-PROFILES-AND-HARNESS-CONSUMERS. Bunlar korunur; ECC'ye girerken S1'den güncel kaynağa tam fark ve B7'de bütün studies delta'sı tekrar hesaba katılır.

Global INDEX → STATE → bu READING → TERMS ve bağlı parça yolu yeni oturuma gerçek kısmi kaydı verir. Paket kapanışı bütün kaynak/çıkarım grupları ve değişiklik kontrolünden sonra ayrıca verilir. Ardından SCOPE sırasındaki ai-knowledge-strategies gelir; bu tur başlamaz. B7/B8 bütün kapsam tamamlanmadan başlamaz.