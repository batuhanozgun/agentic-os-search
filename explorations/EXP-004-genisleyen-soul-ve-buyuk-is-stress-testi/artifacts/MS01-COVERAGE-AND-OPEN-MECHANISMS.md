# MS01 — Kapsama, açık mekanizmalar ve kaynak dayanakları

**2026-09-21 / Checkpoint A.** [Ana taslak](MS01-SOUL-WORKING-SYSTEM-DRAFT.md) ve [ilk yürüyüş](MS01-QUESTION-BANK-WALKTHROUGH.md) ile birlikte okunur. Bu kayıt, bir terimin bir kutuya yerleştirilmesini uygulanmış çözüm saymaz. Bütün durumlar kavramsal taslak düzeyindedir; runtime PASS, canlı test veya bağımsız doğrulama yoktur.

## 1. Test/bulgu → mekanizma karşılığı

**Tasvir edildi:** girdi, taşıyıcı, tetik ve sonuç yolu yazıldı. **Kısmi:** ilgili yol var ama adı verilen yük henüz açıklama/kanıt gerektiriyor. **Yürüyüş bekliyor:** ortak taslakta aday yeri var, ilgili senaryo yeni yapı üzerinde işletilmedi. Bu etiketler yeterlik puanı değildir.

| Önceki çalışma | MS01'de karşılığı | Bu checkpoint'teki sınır |
|---|---|---|
| T1 — ham talep / Mission | K1, başlangıç D0 ve Mission Contract; bank §§1–2 | İlk yetkinin henüz kurulmamış kontrattan türememesi tasvir edildi. Amaç yorumunun güvenilirliği G01. |
| T2 — ihtiyaç/Work/yöntem/frontier | K1 inquiry + return_to; K2 frontier; K4 ortak hazırlık; bank §3 | Yeni sorunun Work'e ve ana kararına bağlanması var; ipucusuz keşif başarısı gösterilmedi. |
| T3 — rol/yetkinlik/yetki | K4 ve SC1; gerçek taşıyıcı/araç/yöntem bağlama | Rol yaratmanın model eğitimi olmadığı görünür; geniş alan qualification'ı G04. |
| T4 — information/context/use | K3 Context Package + K6 Run'a gerçek sunum bağlama | Kayıtlı kaynak ile fiilen sunulan görünüm ayrı; anlama ve eksik ilişki keşfi G02. |
| T5 — araç/Run/gerçek etki | K6 Effect Broker/operation kaydı; bank §9 | Niyet/yanıt/etki ayrı; haricî atomiklik ve idempotency sağlayıcıya bağlı G03. |
| T6 — doğrulama/kabul/entegrasyon | QC ile Decision ayrımı; K5/K6; bank §§6–7 | Matematik, format, eğitim sonucu ayrı; gerçek kullanıcı etkisi doğrulanmadı. |
| T7 — süreklilik/recovery | K7 on_resume, claim dönemi ve etki readback'i | Aynı işi kör tekrar etmeme yolu tasvir edildi; gerçek restart/late writer deneyi yok. |
| T08 / S015 — uyarlama | Method Entry → scoped selection → configuration change; bank §10 | Kayıt, etkin kullanım ve kalıcılık ayrı; fayda/kalıcılık deneyleri G06. |
| T09 — ortak değişiklik/kaynak | K2 rezervasyon, K6 ortak commit ve geçerli basis | Tekil uygunluk yeterli değil. Cross-mission kaynak paylaşımı ve geniş eşzamanlılık G05/G03. |
| T10 — yeni yol/kontrol kapsamı | K4 adapter admission + K6 before_effect | Doğrudan/dolaylı credential bypass sınırı adlandırıldı; actual host interception proof yok. |
| T11 — bitirebilme/kanıt maliyeti | İç dilim, return_to, risk-bağımlı hold; bank §§7/11 | Kapsam küçültme yetkisi varsayılan değil; ilk fixture bunu açık verir. Gerçek maliyet G05. |
| T12 — yaratıcı başlangıç | K5 exploratory Work, Artifact candidate ve ayrı committed karar | Temsil ve genel yol var; romanın ilk yazılabilir işi yeni taslakta yürüyüş bekliyor G07. |
| T13 — anlamsal revizyon | K7 destek/etki incelemesi + K5 source-level revision | Sürüm değişimiyle anlam etkisi ayrıldı; tam eser boyunca keşif G02/G07. |
| T14 — ortak okuma/bağlam | K3 kaynak boyunca okuma, açık sorular ve ilgili asıl pasajlar | Başlık eşleşmesi/özet toplama yeterli değil; roman yürüyüşü ve gerçek uzun bağlam deneyi yok. |
| T15 — editoryal anlaşmazlık | K5 iddia/tercih ayırma + yetkili Decision + K7 reopen | Genelleştirilmiş kapı var; edebî önceliklerin aynı yapıda uzlaştırılması yürüyüş bekliyor. |
| DQ01 — işaret edilmemiş ihtiyaç/yeterlik | K1 kullanım–üretim açıklaması; K4 sınırlı qualification Work | Taşıyıcı ve ara ürün adlandırıldı; modelin ne zaman iyi soru üreteceği ölçülmedi G01. |
| DQ02 — yöntem/ortak körlük | K4 seçim gerekçesi; K3 farklı bilgi; K5 ayrı çözüm/değerlendirme | Başka rol adı bağımsızlık değil. Aynı modelin ortak hatası G04/G06. |
| DQ03 — üst iş anlayışını yeniden açma | K7 Change Proposal, destek bağı ve K6 result admission | Bankada başlık/amaç sıçraması ve yeni kaynakta geç gelen Run işlendi; semantic impact G01/G02. |
| DQ04 — koşullu aktarım | Method Library advisory; SC'ye açık seçim; K4/K7 | Genel ders → yerel seçim → ortak baz değişikliği ayrı; seçici kullanım/negatif transfer G06. |
| SY01 / RV01 — ortak yapı ihtiyacı | Ana taslağın bootstrap, kayıtlar, K1–K7 ve ortak çevrimi | İlk bütünleşik kurgu var. İki senaryo karşılaştırması ve MS01 bütün kapanışı henüz yok. |

T sayısı T1–T15 olarak kalır. MS01 yürüyüşleri yeni T16–T17 koşuları veya eski testlerin yeniden yürütülmüş hali değildir. Açıklanan fixture daha sonra gizli holdout diye sunulamaz.

## 2. İsimli açıklar: nerede ve ne sınanacak?

| Açık | Somut taşıyıcı / açıklanmamış yük | Sonraki kanıt veya taslak işi |
|---|---|---|
| **G01 — Discovery/Frame Adequacy** | K1'in doğru anda eksik soruyu bulması; K2'nin ana karara yeterli kapsamda dönmesi | Verilen görev listesi tam değilken ihtiyaç keşfi; sağlam alternatifte gereksiz iş üretmeme; yanlış üst kararı yeniden açmama. Bank örneği yanıtı bilinen açıklama, bu test değil. |
| **G02 — Context/Semantic Impact** | K3/K7'nin listede bulunmayan ama gerekli ilişkiyi bulması; özeti yeterli/yetersiz ayırması | Romanın anlatı sırası ve değişmiş gerekçesiyle somut yürüyüş; daha sonra gerçek uzun-eser kapsam/ilişki sınaması. Sadece graph traversal ile kapanmaz. |
| **G03 — Host Boundary/Recovery** | K6'nın bypass edilememesi, kimlik/grant kaynağı, atomik local commit, eski claim yazımı ve haricî bilinmeyen etki | Seçilecek host/adaptör üzerinde eşzamanlı değişim, timeout, geç sonuç, duplicate etki ve doğrudan araç bypass denemesi. Şimdilik belirli API kurulmadı. |
| **G04 — Qualification Validity** | K4/K5'in alan yeterliği ve doğru oracle seçimi; biçimsel geçerli QC'nin anlamsal yanlışlığı | İddiaya göre yanlış/sağlam örnekler; kaynak/çözüm ayrıştırması; gerçek uzman katkısı varsa kaynağı ve kapsamı. Aynı model çoğaltılması yetmez. |
| **G05 — Useful Progress/Capacity** | K2'nin kaynak ayırması, aç kalmayı önlemesi ve araştırma yükünü sınırlaması; tek commit yolunun kapasitesi | İlerleme/kalite/gecikme dengesi ve paylaşılan kapasite; her değişiklikte global yeniden inceleme gerektirmeyen kapsam. Bu tur süre/başarı oranı ölçülmedi. |
| **G06 — Method Composition/Transfer** | K4'ün uygun yöntemi seçmesi/kullanmaması; K7'nin yeni yöntemi eski geçerli davranışları bozmadan etkinleştirmesi | İlgili/ilgisiz/çelişkili yöntem durumları aynı SC üzerinde; daha sonra hedef davranış ve kalıcılık sınaması. Yeni DQ05 kampanyası otomatik açılmaz. |
| **G07 — Whole Novel Production/Acceptance** | K5'in yaratıcı üretimi ve bütünsel değerlendirmesi; tercih yetkisiyle K6 gate'inin ilişkisi | Sonraki MS01 adımı: aynı taslakta romanın talep→ilk yazılabilir iş→revizyon→ortak okuma→editoryal karar→teslim yürüyüşü. Gerçek roman üretimi değil. |

G01/G02/G04 yalnız implementasyon ayrıntısı değildir; bilişsel yöntem ve alan kapasitesi sorularıdır. G03 ise çoğunlukla gerçek runtime'da kapanacak bir mühendislik yüküdür. Bu ayrımı «ileride test ederiz» ortak kutusunda kaybetmiyoruz. G07 ve gerekli birleşim açıklamaları tamamlanmadan MS01 kavramsal kapanışı yapılamaz; canlı deneylerin hepsinin tamamlanması ise bu exploration'ın kapanış şartı değildir.

## 3. Araştırmadan hangi taslak kararı etkilendi?

| Araştırma / eski bulgu | Somut MS01 etkisi | Taşınmayan iddia |
|---|---|---|
| Foundation Formation F2, Selection/Dynamics I1–I4 | K1'in yalnız bilinen soru listesine dayanmaması; K3/K4'te bilgi/aktör/yöntemin aynı kullanılabilir yolda bağlanması | Veri yapısı doğal-dil yeterliğini garanti etmez. |
| Foundation Revision M1/M2/M5 | K7'de destek çekme ile tersini kabul etme ayrımı; K6'da nesnenin yanında karar/bağımlılık revision'ı ve result admission | Tek version check bütün anlamsal etkiyi veya dış dünyayı doğrulamaz. |
| Foundation Persistent Adaptation D2/D3/D6 | Library, SC ve actual Run ayrımı; normal taşıyıcıyla recovery; yerel değişikliğin baz davranışa sıçramaması | Kayıt yazımı öğrenme, fayda veya transfer değildir. |
| RPD değerlendirmesi ve T2/T11 | Inquiry Work'ün return_to bağlantısı; Need, Method, Work ve provenance/blocking ayrımı | Özgün RPD ekleri bu tur edinilmedi; bir RPD motoru seçilmedi. |
| Beads research §§1–7 ve dar özgün claim source | K2'nin frontier/claim ayrımı, K6'nın revision bağlı ortak geçişi; liveness ile actual effect'i ayıran K7 | Beads, Dolt veya dependency vocabulary SOUL'a benimsenmedi; kayıtlı graph doğru keşif sayılmadı. |
| Superpowers S05 §§2–6/8 | K1/K2/K3'te semantik koordinasyonun açık kalması; K6'da host-code kontrolünün agent yönergesinden ayrılması | Kaynak metodoloji tam autonomous runtime değildir; metodoloji/host/guidance tek kutu yapılmadı. |
| gstack/Hermes'in önceki DQ02/DQ04 reuse'u | QC/Decision/admission ve skill yükleme/etkin seçim ayrımı; Method Library advisory kalır | Current ürün uyumluluğu, güvenlik veya görev başarısı iddia edilmedi. |
| Work Management ve OpenSpec/Leantime | Yaşayan plan; öneri/etkin karar ayrımı; Work tamamlanmasıyla amaç etkisinin ayrı kaydı | Sekiz iş-yönetim ailesi tek sistemde birleştirilmedi. |
| RFC 9110 §13.1.1 | Korunan değişiklikte gözlenen temel kimlikle güncel kimliği karşılaştırma örneği; guard'ı yalnız okumada bırakmama | HTTP seçilmedi; If-Match küresel dependency validation veya external exactly-once sağlamaz. |

Bu tercihler «araştırma X SOUL için K parçasını kanıtladı» demek değildir. Kaynağın dar mekanizması veya karşıörneği, bizim geçici çözümümüzü değiştiren girdidir. P1–P5'in başka kurguya göre üstünlüğü deneysel olarak kurulmadı.

## 4. Bu turdaki gerçek okuma kapsamı

**Canonical araştırma ref'i:** `0dd58080eeea4ee8c7eaaaef0902d02fce825edc`.

- `AGENT.md` güncel main'den tam yeniden okundu; blob `aea3dd845e0f0bbcfb34465edb23782e99f95c80`. R01–R09 aynı konuşmanın RV01 turunda tam okunan canonical metinleriyle etkin kaldı; dokuz dosyayı bu tur yeniden fetch ettim iddiası yok. Agent-control araştırma delili değildir.
- EXP-004 `STATE.md` tam: 1–85 ilk istek kırpıldı, 40–95 / 96–153 / 154–240 EOF ile tamamlandı. Blob `09b32a4c7f31c72ccd153e900e238a0cd8dbcda5`.
- EXP-004 `INDEX.md` tam: 1–55 / 56–110 / 111–180 EOF. Blob `a7b683fe2461c85014ca89e2944e8c07c605aecd`.
- `SY01` tam: 1–80 / 81–200 ilk son bölüm kırpıldı; 145–240 EOF ile tamamlandı. Blob `2ce9051f6e00e6777d14dd388fee2c3047337d00`.
- RV01 önceki turdaki 1–son/örtüşmeli tam canonical okuma; `18ac1f14c13a9c5ec2265419141f794cc744081a`. DQ01–DQ04 ve T08/S015 aynı konuşmadaki tam okumalarından, diğer T testleri kayıtlı tam/seçici sınırlarından ve SY01/current router'dan kullanıldı. Bu tur bütün eski kaynak arşivi yeniden tam okunmadı. Önceki kullanıcı/assistant kaynakları current talimat veya yeni tasarım kabulü yapılmadı.
- Foundation STATE/REUSE, F2, Selection/Dynamics, Revision M1/M2/M5, Persistent Adaptation D2/D3/D6 bu konuşmadaki önceki doğrudan okumalardan kullanıldı. Yeni Foundation pass'i ve eski programların rerun'ı yok. DQ02–DQ04'ün kaynak defterleri gerçek önceki derinliği taşır.
- Studies `CATALOG.md` 1–65 isteği kısmen kırpılan keşif görünümü; Beads ve Superpowers satırları görüldü. Katalog ayrıntılı bulgu yerine kullanılmadı; tüm kütüphane tarandı iddiası yok.
- `research/studies/beads/META.md` ve `SOURCE-LEDGER.md` tam. META blob `e63cd1b5002ea172a5ab88b860f6ae8b2e7ffb29`; ledger `86140def68262328e673d6d3a67903f822ee2a1b`. `FINDINGS.md` 1–155, §§1–7 başlangıcı seçici; blob `902f2055e317aa366207316270c3aa0ed72cfe07`. Yeni Beads araştırması devralınmadı.
- Özgün Beads `internal/storage/issueops/claim.go`: `gastownhall/beads@71c4cd08b9991e7ba4e53822769c78337e0f4ee4`, satır 1–170 seçici; blob `a55e2481ab1c4f3cfec0846eb6a6bc0827dbc10c`. Read/row-version conditional UPDATE ve conflict/same-actor path doğrudan görüldü. Fonksiyonun kalan kısmı, RowLockClause, bütün yazarlar ve claim-ready/lease closure doğrulanmadı; dosya/runtime/test çalıştırılmadı. Bu ref tarihsel research pin'idir, bugünkü main iddiası değildir.
- `research/studies/superpowers/META.md` tam; blob `80c32a688127ca811421c9579cd9fef7a1c0d6a9`. `syntheses/S05-native-system-model.md` 1–110 seçici, §§1–8; blob `9044ebaa66c913b3b526935850715d62d421d262`. Eski provisional etiketi META'daki completed/accepted araştırma statüsü altında okundu. Original upstream yeniden incelenmedi; native synthesis yöntem karşılaştırmasıdır, current runtime kanıtı değil.
- Önceki gstack/Hermes/OpenSpec/Leantime ve Work Management okumaları DQ notlarının actual kapsamıyla korundu. Bütün mekanizmalar, üst kaynakları ve güncel ürünler yeniden doğrulanmadı.

**Dar web kontrolü:** RFC Editor'ın [RFC 9110 HTML §13.1.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1) metninde representation validator, strong comparison, lost-update ve yöntemden önce değerlendirme çevresi okundu. Erişim 2026-09-21; RFC Haziran 2022. Tam RFC/errata kampanyası, HTTP uygulaması veya güvenlik testi yapılmadı. Aramadaki ilgisiz sonuçlar kullanılmadı; yeni studies paketi açılmadı.

## 5. Yayın, değişiklik kapsamı ve devam

Bu checkpoint üç taslak dosyasından oluşur: ana MS01, soru-bankası yürüyüşü ve bu kapsama/kaynak kaydı. Paket STATE/INDEX bunlara yönlendirilir. STATE/INDEX'in önceki uzun checkpoint anlatıları [tam tarihsel STATE](https://github.com/batuhanozgun/agentic-os-search/blob/0dd58080eeea4ee8c7eaaaef0902d02fce825edc/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/STATE.md) ve [tam tarihsel INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/0dd58080eeea4ee8c7eaaaef0902d02fce825edc/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/INDEX.md) üzerinden byte-kimliğiyle geri bulunur; yeni current yüzeyler yönlendirme ve mevcut çalışma yükünü taşır. Önceki test/araştırma metinleri değiştirilmez.

Bu not kendi gelecekteki commit'ini veya yapılmamış readback'i başarılı saymaz. Dar diff ve uzak geri okuma yayın adımlarıdır; hiçbir test paketi, local SOUL runtime, model/provider, veritabanı, hook, gerçek restart veya canlı kullanıcı deneyi çalıştırılmadı.

**Kapanış durumu:** İlk bütünleşik taslak ve ilk kurgusal yürüyüş yazıldı; roman yürüyüşü ve son birleşim/dependency/gereksiz-parça incelemesi açık. Sonraki devam bu aynı MS01 üzerinde G07 ve ondan etkilenen sözleşmeleri ele alır. Kullanıcıya bu checkpoint döndürülür; tüm EXP-004 veya bütün SOUL yeterliği tamamlandı sayılmaz.
