# Superpowers — Okuma ve kalıcı aktarım durumu

2026-09-19, **B6-T6 / P2-PILOT-CLOSED / DURABLE-TRANSFER-ACTIVE / ENTRY-AND-U02-U03-RECORDED / PACKAGE-PARTIAL**. Bu, concepts içindeki yerel kapsam/okuma kaydıdır. Kaynak araştırmanın STATE'i ve global concepts/STATE.md ayrı yetki/durum yüzeyleridir.

## 1. Güncel iş ve devam

[TERMS.md](TERMS.md), [TERMS-ENTRY.md](TERMS-ENTRY.md) ve [TERMS-WORK.md](TERMS-WORK.md) birlikte tam okunur. Giriş/skill seçimi/host aktarımı ile onay/plan/çalışma alanı/görevlendirme/inceleme grupları kalıcı kayıttadır. **Superpowers kalıcı paketi tamamlanmadı.** Kaynak araştırmanın ve 52 dosyalık P2 pilotunun tamamlanmış oluşu korunur; yeniden yöntem denemesi yapılmaz.

**Sıradaki yetkili iş B6-T7:** `notes/U04-testing-diagnosis-and-verification.md`, `SOURCE-LEDGER-U04.md`, `evidence/U04-diagnostic-probes.py` ve sonuç JSON'unu tam geri kazan. P2-T2/P2-T5'in SP62–SP71/SP171–SP173 kullanımlarını; test kronolojisi, oracle, mevcut kanıtın uygulanabilirliği ve clean/exit niteleyicilerini kaynakla kontrol ederek kalıcılaştır. Sonra U05 teslim/entegrasyon/temizlik/koruma notu, kaynak kaydı, betik ve sonuç gelir: SP72–SP79/SP174, koşullu no-force kuralı ve karar bildirimi/ayrıntılı kanıt saklama ayrımı korunur. S04 sentezi ilgili alt kaynaklar tamamlanınca bağlanır. Kapasiteye göre bölünebilir; gerçek devam noktası kaydedilir.

U02/U03'ün tamamlanmış aktarımı yeniden yapılmaz. ENTRY'nin eski U02-next cümleleri B6-T5 checkpoint'idir; ana TERMS bunları WORK'e bağlar. SP28'in yeni onay bağlamları ve SP24'ün work recovery ilişkisi WORK'te açık. Bütün gruplar/kaynak kontrolü bitmeden paket kapanmaz; B7/B8 başlamaz.

## 2. Kaynak bağlama ve kapsam

- Repository: **batuhanozgun/agentic-os-search**.
- Kaynak öneki: **research/studies/superpowers/**.
- P2 kaynak ref'i: **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847**.
- S1 başlangıç ref'i: **9b46155e904560c90b89e657f3d0d4e00e2e46cf**.
- Paket tree: **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12**.
- B6-T5 başlangıcı: **1108a483a811c3d5e22595f99179e51da8479f16**; research tree **5d0efc37a85722f988937226270aa7a7f88c090e**, studies tree **0693c76d133d256df60b412a07c8481da41ae33d** üzerinden aynı paket kimliği doğrudan doğrulanmıştı.
- B6-T6 başlangıcı: **4b8c87486cebf0b80cac5dba39699e72e09ccc2f**. Önceki concepts kapanışı **11709624149ae45c5f5f421c5b8930d0e13d859d** ile karşılaştırmada yalnız ECC/ROUND-U12-B.md değişti. Superpowers, concepts ve agent-control farkı yoktu; tam ağaç keşfi bu tur yeniden yapılmış sayılmaz.

Değişmez manifestler: [19 kök dosya ve üç alt ağaç](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/56c19a5e2c0deb7b0f5164aac818ed2ba98baf12), [11 not](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/cc9611a59f65ec1175fd99885c01a6efebc202ed), [6 sentez](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/bfb0603d70683e512df789bfa52c929caa67d9ea), [16 betik/sonuç](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/7a5af9c7cf94551a42102bcfd9e2ddd36434cd9a). B6-T5'te bütün girdileriyle doğrudan alındılar; tree hash'i yeniden hesaplanmadı.

**52 dosya: 36 Markdown, 8 betik, 8 JSON sonucu.** Bu ağaçta binary veya ek alt dizin yok. Bu dış ürün deposunun bütün dosya sayısı veya iş yüzdesi değildir. Atfedilen dış kaynaklar/diğer studies bu araştırma dosyalarının yerine sayılmaz. B6 kontrol/giriş okumaları da araştırma dosyası sayacına eklenmez.

Dış hedef `obra/superpowers@b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, manifest bağlamı 6.3.0; lab `prime-radiant-inc/superpowers-evals@e64684cd1fa270c464ac797747e45bbe8d127e8b`; tarihsel assessor `prime-radiant-inc/gauntlet@db6c8e0fcf80889aa6d9631c99adec698f6c0caa`, ayrı `25a2e3e00431f8d8eb63781162ccb974d43d5405` deltası. Bu kimlikleri araştırma kaydından almak güncel ürün/kampanya doğrulaması değildir. Kaynak araştırma user-evaluated/accepted kalır; notların eski next/partial sözleri current concepts işi değildir.

## 3. Bütün kaynak dosyalarının yerel envanteri

Tüm kipler 100644; yollar kaynak önekine göre. **T5/T6**, kalıcı aktarım için dosyanın tam geri kazanıldığı turdur. **P**, P2'de tam okuması kayıtlı fakat B6 içeriği henüz geri kazanılmamış dosyadır. Dosyanın tam okunması onun bütün çapraz atıflarının kalıcı aktarımının kapanması değildir. İlk 15 T5 ve sekiz ek T6 = **23 dosya**; 29 P kalır.

| Yol | Blob SHA | B6 tam geri okuma |
|---|---|---|
| CLOSURE-AUDIT.md | b6178fdc2817eaf93c447434a014ca971a972348 | T5 |
| CORE.md | 0986da960a4b3db5d1e09894c2abfd6d6ca114be | T5 |
| INDEX.md | c170993756d19c2d98831ca1dd371c5aadf3c53a | T5 |
| META.md | 80c32a688127ca811421c9579cd9fef7a1c0d6a9 | T5 |
| METHOD.md | 95f684306f92373dbb51f4ceedaff885394e950b | T5 |
| PLAN.md | ea86caa9144bfd462428a3c8ef3ffb6ab7d5ca00 | T5 |
| SOURCE-LEDGER-U03.md | 76075ba19f8012d9d2b582887a22c9edf2362d2d | T6 |
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
| SOURCE-LEDGER.md | a09cd522f1b51cec1d3fc9c30a017f8931e35dd2 | T5 |
| STATE.md | 472b9f16bd68d0e05a4108fb1b2155ee2b7a2d2f | T5 |
| notes/U01-entry-routing-and-bootstrap.md | 8b8e63451e77d78e7b9be4de190944157a8120f2 | T5 |
| notes/U01B-host-delivery-and-continuity.md | cc2c0ba68f8d90ec6680b9b4b2d7cc0bc3405620 | T5 |
| notes/U02-approval-plan-workspace-handoff.md | 20568d3bfe398e7e0ff43abf2cb29e84925834ae | T6 |
| notes/U03-delegation-review-and-acceptance.md | 4dfe415cf35386650a30fa7104e5537355276977 | T6 |
| notes/U04-testing-diagnosis-and-verification.md | 975d935ad98634624537571e77e38e4ec5268ee7 | P |
| notes/U05-delivery-cleanup-and-retention.md | d3e797780ffb14781361194e5d82799033f14b49 | P |
| notes/U06A-skill-authoring-and-change-admission.md | 469dbea119e410a11c2130bb94ff4e90ed34a7fc | P |
| notes/U06B1-evaluation-evidence-and-verdict.md | 54418ac55a5129cde6f0ee1ddf0c471f361a6a1d | P |
| notes/U06B2-assessor-contracts-and-evidence-qualification.md | adb00736fc90b481568a73288c81ce6929ad1f1a | P |
| notes/U07A-visual-companion-lifecycle.md | cb87245b449ff383af55af5f9e4dd50a15532c94 | P |
| notes/U07B-distribution-versioning-and-support.md | 2de6f304f2d7c3630b27cfdbe7291fe2e7f1b3fc | P |
| syntheses/S01-skill-evolution-and-evaluation.md | df93d7bcd127f3d31e82ab8dcc80b9668b0c7231 | P |
| syntheses/S02-availability-runtime-and-distribution.md | 0546c46231ef17da3cdb204520d7846176c27cfe | T5 |
| syntheses/S03-intent-planning-and-context-handoff.md | f69f5c99aefa2a6a13b4233ae49afd73dc2ce0ca | T6 |
| syntheses/S04-execution-verification-and-delivery.md | 54c77cc04e9d7f88900918f8ee63dd07dadb0e54 | P |
| syntheses/S05-native-system-model.md | 9044ebaa66c913b3b526935850715d62d421d262 | P |
| syntheses/S06-project-facing-contribution-and-comparison.md | 8ab988debc34b70efd55b4c6145a06a96c70b256 | P |
| evidence/U01-hook-probes-results.json | 0a21d98568b71a7c1d99385b9d8ae88611ebed78 | T5 |
| evidence/U01-hook-probes.py | 9ca0b43739e69c930d1241601bb61b7ef1872ff1 | T5 |
| evidence/U01B-opencode-probes-results.json | fae46fb808c5814fc7039f874f7d9aae5e5b34f3 | T5 |
| evidence/U01B-opencode-probes.mjs | 6a99be598bac4d60943c816857124c907882c089 | T5 |
| evidence/U02-handoff-probes-results.json | c95be67a743b7e8526e9fe30a2198117aee61d50 | T6 |
| evidence/U02-handoff-probes.py | 5cf7d9dd25ade628743a3250158486c8349a6fb5 | T6 |
| evidence/U03-review-probes-results.json | 48ba0976e661c74fe20f9232836fcc2dc2debb19 | T6 |
| evidence/U03-review-probes.py | a1982668d06c8cf22783af60bfb5430839eb1b5c | T6 |
| evidence/U04-diagnostic-probes-results.json | 875f03b27e53b8a6013f2facbace833fd7478cb9 | P |
| evidence/U04-diagnostic-probes.py | 37ca1fe7d2ee6c0390e51f9eb56b281a26138eee | P |
| evidence/U05-lifecycle-probes-results.json | 565da2eaf7aa293eea5663dce74436c71bb7595b | P |
| evidence/U05-lifecycle-probes.py | a59ca7af17737f64fa8ed54c214b77ceecd522a5 | P |
| evidence/U07A-companion-client-probes-results.json | 2ceef31098d65cfda54bfa708ab0ed002632f37e | P |
| evidence/U07A-companion-client-probes.mjs | 27082457c9e782cfec1e392aa78e02677d54b735 | P |
| evidence/U07B-version-probes-results.json | be459537a1e14bbf5f75f4823b5e33d4db88644b | P |
| evidence/U07B-version-probes.py | 63763cce58982ab0c22002ca767765eaaec16f9f | P |

## 4. Gerçek okuma ve kaynak kapsamı

[B6-T5 değişmez yerel kayıt](https://github.com/batuhanozgun/agentic-os-search/blob/53cc0647266228e3f5446bbe69a6d55b573a19a4/concepts/studies/superpowers/READING.md) ilk 15 tam okumayı, gerçek aralıkları ve giriş grubunun kaynak kontrolünü korur. O dosyadaki U02-next ve 37-bekliyor ifadeleri tarihseldir. [P2/B4 kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/29b07b6529618f9a654d44a86e3ed6b05b8b40f9/concepts/STATE.md) pilotun 52 dosyalık okumasını ve önceki checkpoint'leri taşır; bu kayıtlar yeni okumanın yerine geçmez.

| B6-T6 yeni tam kaynak okuması | Gerçek aralık | Bu turun kullanım karşılığı |
|---|---|---|
| N02 / notes/U02-approval-plan-workspace-handoff.md | 1–100, 101–EOF; son istek 240 | WORK §2–3 ve §7–8; SP28/39–51/167, onay/kimlik/maddi erişim ve sınırlar. |
| N03 / notes/U03-delegation-review-and-acceptance.md | 1–95, 96–EOF; son istek 240 | WORK §4–8; SP30–34/52–61/168–170, roller/inceleme/aralık ve bileşim. |
| SOURCE-LEDGER-U03.md / L03 | 1–EOF | Dış S37–S43 ve önceki S30/S34/S35 kaynak rolleri, E07/E08 ve ayrı belge atıfları. |
| evidence/U02-handoff-probes.py | 1–145, 146–EOF; son istek 310 | E05 runner'ın kaynak kimliği, fixture, 13 vaka ve alanları. |
| evidence/U02-handoff-probes-results.json | 1–EOF | 11 belirtilmiş gözlem karşılandı, iki sağlık ölçütü başarısız; roller korunur. |
| evidence/U03-review-probes.py | 1–140, 141–EOF; son istek 260 | E07 runner'ın açık OUTFILE, commit aralığı, dosya oracle'ı ve sentetik metin koşulu. |
| evidence/U03-review-probes-results.json | 1–EOF | Yedi gözlem/koşul karşılandı, iki verbal-oracle sağlık ölçütü başarısız. |
| syntheses/S03-intent-planning-and-context-handoff.md | 1–EOF; istek üst sınırı 115 | U02/U03 ilişkileri; §6'nın kamu raporu aktarımı ayrıca sınırlı, U08 kaydı sonraki grupta. |

EOF görülen gerçek içerik sonudur; istek üst sınırı dosya satır sayısı değildir. Hiçbir araştırma betiği bu tur çalıştırılmadı. Kaynak yazarının deneyi yeni runtime/test başarısı yapılmadı. L0, CORE, CLOSURE-AUDIT, giriş parçaları ve P2-T1/T2/T5 metinleri bu konuşmada erişilebilirdi; aynı içerikler sekiz yeni dosyanın üstüne yeni okuma diye sayılmadı. Kaynak kontrol/giriş dosyalarının eksik gerçek metinleri canonical okumayla geri kazanıldı, araştırma korpusuna eklenmedi.

## 5. U02/U03 kaynaklarından kalıcı kayda kontrol

Kontrol mevcut kelime listesini yeniden onaylamak yerine kaynak bölüm/tablo/liste/örnek ve deney alanlarından yapıldı. WORK'ün kaynak anahtarı N02/N03/L0/L03/E05/E07/S03'ü tanımlar; aşağıdaki adresler oradadır.

| Kaynak bölümü | Kalıcı karşılık / korunan sınır |
|---|---|
| N02 §1–2 | SP28/30/44, U02-U01; üç istek yolu ve farklı yürütme sözleşmeleri, dört durma sınıfı, Q13. Onay token'ı/digest bağı varsayılmadı. |
| N02 §3 | SP39–44, öz inceleme ve giriş ledger'ı; spec gerekçe yönü, task/step, yol/sürüm, geçici ruling. |
| N02 §4 | SP45–51; producer/consumer ve saklama bağları ilişki görünümüyle korunur. |
| N02 §5 | SP28.c/SP45; host/mevcut worktree/in-place, test baseline'ı ile temiz dosya durumu ayrımı. |
| N02 §6 | SP46/47; basename/tam yol/sürüm/tamamlanma, farklı yol aynı ad ve aynı yol yeni içerik kontrolleri. |
| N02 §7 | SP41/42/48/31; görev bölümü ile globals/arayüz/bağlam aktarımı; fenced örnek ve eksik görev çıkışı. |
| N02 §8 | SP167; saved/committed ve yeni worktree'de gerçek erişim; commit tek evrensel çözüm yapılmadı. |
| N02 §9 | WORK §3 son açıklama; selected-directory kontrolü ve alternatif OR, olumlu/olumsuz fixtures. |
| N02 §10–11 | E05-R/O alanları ve kaynak sınırları; Q13–17, sonraki kaynak ihtiyaçları yeni iş yetkisi değildir. |
| N03 §1–2 | SP31–33/49–51/56/60; tek reviewer/iki hüküm, farklı giriş/çıktı/tüketiciler. |
| N03 §3 | SP33.d/52/53/168/169; diff-first, kaynak recovery, raporun iddia olması, kanıtın yeniden kullanılması, read-only talimat/izin farkı. |
| N03 §4 | SP32/34/54–60; değişmiş yanıt, fix turu, 1–3/4–5/sınır, parked/deferred/unblocking ve bütün-dal son düzeltmesi. |
| N03 §5 | SP47/49/44 ve WORK §5; rapor, ledger, agent identity/resume, Ruling'in insana taşınması. U05 gerçek koruma kapsamı açık. |
| N03 §6 | SP61/169; SDD seri uygulama, batching ve bağımsız-domain paralel yol farklı. LC1'in no-child kapsamı korunur. |
| N03 §7 | SP50/51, U03-U01; doğru/dar/fix aralığı, net diff ile çalışma kopyası, negatif dosya-kapsam kontrolü. |
| N03 §8 | SP170/U03-U02; description/drill ve literal koşulun sentetik karşı örnekleri. Gerçek model/CI başarısızlığı denmez. |
| N03 §9 | WORK §7; HEAD~1 genellemesi, human/controller, Important/parked, genel final template ve özel ledger girdileri. |
| N03 §10–11 | E07'nin dokuz vakası, kaynak/kullanım/deney ayrımı; Q18–22 ve gelecekteki U04/U05/U06 çalışma rolü. |
| L0/S28–S36 ve L03 | Atfedilen dış dosya kimliği/okuma/yürütme sınırı; önceki S34 not-executed ile sonraki E07 geçmiş yürütme karıştırılmaz. |
| E05-R/O + E07-R/O | Tüm vaka aileleri ve kind/criterion/observed/result/exit alanları; ölçüt karşılanması ürün kabulü değildir. |
| S03 §1–5 | ENTRY ilişkileri ve WORK §2–5/§7; amaçtan göreve, controller'ın anlam taşıması, ayrı otorite ve kimlikler. U05'e bağlı fiilî bitiş/koruma sonraki grupta. |
| S03 §6–7 | S03-U01 ve kaynak-içi ilişki; süreç ağırlığı/koordinasyon/çıktı kalitesi ayrı, issue2203 atıf sınırı. U07/U08 kanıt zinciri ve bütünsel yeniden kullanım henüz kapanmadı. |

Kaynakta açıklanmış U02/U03 kullanımının bu kontrolde açık aktarım eksiği bırakılmadı. Kaynağın kendi genel tanım vermediği veya açık soru yaptığı şeyler çözülmeden de doğru statüyle aktarılabilir; yeni derin araştırma borcuna çevrilmez. S03 tam okuması, başka gruplara ait kalan kaynakları yapılmış göstermez.

## 6. Pilot bağı ve yorum etkisi

Görünür P2-T2'nin SP30–SP34/SP39–SP61 kayıtları, P2-T1'in erken rol görünümü ve P2-T5'in SP167–SP170 ekleri birlikte kontrol edildi. SP35–38'in deney dili ENTRY'de korunup E05/E07'ye uygulanır. SP28'in onay bağlamları WORK alt adreslerine açıldı. SP171–SP174 U04/U05'tedir; aktarılmış sayılmadı. Kaynakta bulunan ek executing-plans/committed diff/process-weight kullanımları ayrı yerel adreslerle belirtildi.

Maddi anlam tersine dönüşü bulunmadı. Kaynakla sınırlı ayrımlar daha açık adreslendi: task/step; worktree/scratch; plan yolu/sürümü/tamamlanma; brief/yeterli bağlam; implementer DONE/kabul; reviewer sayısı/hüküm sayısı; read-only talimat/yetki; düzeltme denemesi/ADDRESSED; parked/deferred; context isolation/ortak kaynak bağımsızlığı. E05/E07 olumlu gözlemleri ve başarısız daha güçlü koşulları birlikte taşındı.

SDD'nin no-child talimatı yalnız ilgili rota/roller için; dört durma sınıfı eksiksiz koşullarıyla korundu. Genel ve özel talimatlar arasındaki Q13/Q20/Q24 sınırları çözülmüş ilan edilmedi. N01B'nin girişte iş kurtarma göstermemesi tüm sistemde kurtarma yokluğuna çevrilmedi; U02/U03 gerçek kayıt mekanizmalarıyla bağlandı.

P2 özgün metinleri bu tur erişilebilirdi; kayıtlar salt eski STATE özetinden üretilmedi. İleride görünmezse METHOD §8'in kaynak kontrollü yeniden üretimi uygulanır ve erişim sınırı belirtilir. Bu same-assistant kaynak/pilot karşılaştırması bağımsız doğrulama, sıfır atlama garantisi veya güncel ürün testi değildir.

## 7. Yayın, delta ve korunmuş kayıtlar

B6-T6 yazma kapsamı: yeni TERMS-WORK.md, mevcut TERMS.md, bu READING.md ve global concepts/STATE.md. ENTRY, global INDEX, METHOD/PLAN/SCOPE, CHARTER/ORIGIN/SETUP-REVIEW, CMH, kaynak studies, Foundation ve agent-control değişmez. Global INDEX zaten gerçek Superpowers TERMS/READING'ine bağlıdır; yeni parça ana TERMS üzerinden bulunur. Yeni branch veya ikinci study/META/CATALOG kaydı oluşturulmaz.

WORK içerik commit'i **9cd3fb1953f4ac0a193e0c27303cf52304476dc8**. Geri okuma 1–65 isteğinde görünüm kesildi; 55–105 ve 106–EOF aralıklarıyla eksik yerler örtüşmeli tamamlandı. Ana TERMS commit'i **5ec168217125fd0ac00855ab25dc1aa6cc1e2f95**. Bu dosya kendi henüz bilinmeyen commit'ini veya yapılmamış son kontrolü yazmaz. Yayınlanan TERMS/READING ve global STATE geri okumalarıyla gerçek kapsam son yanıtta kontrol edilir.

B6-T5 kapsam ve yayın ayrıntıları yukarıdaki değişmez yerel kayıt ve [11709624 global kapanışı](https://github.com/batuhanozgun/agentic-os-search/blob/11709624149ae45c5f5f421c5b8930d0e13d859d/concepts/STATE.md) üzerinden korunur. Başlangıçta tek yeni ECC/ROUND-U12-B.md deltası görüldü; önceden kaydedilmiş S1-sonrası ECC/katalog farkları ortadan kalkmış sayılmaz. ECC'ye girerken ve B7'de tam delta tekrar değerlendirilir. Başka oturumun çalışması concepts adına değiştirilmez.

## 8. Devralma ve durma noktası

Global INDEX → güncel STATE → bu READING → TERMS ve iki bağlı kullanım parçası → U04'ün gerçek kaynakları. Kontrol/proje girişlerinin tam okuma yolu global INDEX'te korunur. U02/U03 tamamlanan grubunu tekrar yeni araştırma sanma; kaynak değişirse etkilenen kaydı aç. Paket bütün kaynak/çıkarım grupları ve son delta kontrolüyle kapanınca SCOPE sırasındaki ai-knowledge-strategies gelir. Şimdi ortak referans, mimari veya yeni ürün araştırması başlamaz.
