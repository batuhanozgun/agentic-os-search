# Concepts — Güncel çalışma durumu

Tarih: 2026-09-19. Program: araştırma bazında terim/jargon kullanımlarının çıkarımı, ardından bütün çıkarımların ortak değerlendirilmesi. Bu dosya concepts çalışmasının güncel yetki/durum kaynağıdır; araştırmaların kendi STATE dosyalarının yerine geçmez.

## Durum

**PREPARED / PILOT-1-BOUNDED-COMPLETE / B2-REVIEW-COMPLETE / PILOT-2-ACTIVE / READING-15-OF-52 / EXTRACTION-PARTIAL / METHOD-v0.2-DRAFT.**

İlk pilot ve B2 değerlendirmesi tamamlanmıştır; yeniden yapılacak iş değildir. Kullanıcının son devam talebiyle Superpowers üzerinde ikinci konuşma içi pilotun P2-T1 turu başlatıldı. Gerçek dosya ağacı 52 dosya olarak çıkarıldı; bunların 15'i tam okundu. Bu sayı eşit ağırlıklı ilerleme yüzdesi, tam araştırma okuması veya tamamlanmış kullanım envanteri değildir. İkinci pilot ve B4 değerlendirmesi açık; kalıcı seri çıkarım ve ortak referans başlamadı.

Pilot kullanım çıktılarının taşıyıcısı görünür konuşma yanıtlarıdır. Bu tur yeni TERMS/READING veya başka dosya oluşturulmadı; yalnız mevcut STATE güncellenir. METHOD ve PLAN v0.2-draft olarak korunur. P2-T1, giriş/erişilebilirlik/hosta taşıma kullanımlarını ayrıntılandırır; CORE ve S02'de karşılaşılan daha sonraki ailelerin ayrıntılı kaynakları hâlâ sıradadır.

| İş | Durum |
|---|---|
| Amaç, kaynak talep ve iki risk | ORIGIN/CHARTER'da korunuyor; değişmedi. |
| Repo hazırlığı | Tamamlandı; SETUP-REVIEW tarihsel kontrol kapsamı geçerli. |
| B1 / ilk pilot ve B2 / ilk yöntem değerlendirmesi | Tamamlandı; kaynak-kapsamlı kapanış ve v0.2 dersleri korunur. |
| B3 / Superpowers ikinci pilot | Aktif; 52 dosyanın envanteri, 15 tam okuma ve ilk konuşma içi kullanım/ilişki dökümü. |
| B3 kalan okuma ve çıkarım kontrolü | 37 dosya henüz okunmadı; tüm paket için kaynak taraflı kapanış kontrolü yapılmadı. |
| B4 / ikinci yöntem değerlendirmesi | Başlamadı; B3 sonrasında. |
| Kalıcı seri çıkarım | Başlamadı; iki pilot ve değerlendirmelerinden sonra. |
| Bütün çıkarımlardan ortak referans | Başlamadı; kabul edilmiş ortak tanım yok. |

## Amaç, derinlik ve korunacak ayrımlar

Önce studies araştırmaları kendi bağlamlarıyla tam okunarak kullanım ve ilişkileri çıkarılır. Sonra bütün çıkarımlar okunarak kapsamlar, alt kavramlar ve adlandırmalar birlikte değerlendirilir. İlk pilotun terimleri veya ilişki şeması ikinci pakete başlangıç ontolojisi olarak taşınmaz.

Her concepts turunda iki neden kısa ve açık biçimde görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemiyor; bu nedenle önemli yorum, dayanak, belirsizlik ve değişiklik izlenebilir olmalı. Ortak sözcükler aynı anlamı garanti etmiyor; kullanıcı onayı, kaynak kullanımı ve assistant yorumu teknik doğruluk bakımından ayrı tutulmalı. Kullanıcının olumlu değerlendirmesi teknik uzman doğrulaması değildir.

Derinlik sınırı, incelenen araştırmanın kullanım ve ilişki düzenini sadık aktarmaktır. Sonraki okuma yalnız terim hakkında genel bilgiyi artıracak fakat bu araştırmanın aktarımını değiştirmeyecekse ilk aşamaya eklenmez. Kaynağın açıklamadığı anlamı bu statüsüyle kaydetmek geçerli sonuçtur; okunmamış dosya veya atlanmış açıklama aynı şey değildir. Genel tanım araştırması, kurulum, canlı ürün deneyi ve erken ortak tanım üretimi yoktur.

Araştırma paketinin kendi METHOD/PLAN/STATE dosyaları bu pilot için okunan proje kaynaklarıdır; Superpowers talimatları veya eski araştırmanın deney planı etkin agent-control ya da yeniden deney çalıştırma yetkisi haline gelmez. Source-native terim, önceki araştırma yazarının açıklaması ve yeni extractor yorumu ayrı tutulur. Sentez tekrarı bağımsız kanıt değildir.

## Yetki ve yazma sınırı

Kaynak amaç/yetki ORIGIN/U01–U05, sonraki devam talepleri ve bağımsız derin terim araştırmasına kaymama açıklamasıdır. B1 → B2 → B3 → B4 sırası yetkilidir; aynı amacı tekrar onaylatmak gerekmez. Maddi amaç/aşama/kapsam değişikliği ayrıca değerlendirilir.

P2-T1'in repo yazma kapsamı yalnız concepts/STATE.md'dir. METHOD/PLAN/CHARTER/ORIGIN/INDEX/SETUP-REVIEW, AGENT ve protokoller, özgün studies paketleri ve onların META/STATE/INDEX'leri, Foundation, explorations ve publications değiştirilmez. Yeni dosya, branch, kalıcı terim envanteri veya ortak referans oluşturulmaz. Eşzamanlı ECC çalışması korunur.

Superpowers araştırmasının kendi durumu 2026-09-18'den itibaren BOUNDED-COMPLETE / USER-EVALUATED / ACCEPTED'dır. Concepts pilotu bunu yeniden açmaz veya kabulünü değiştirmez. Eski mekanizma notlarındaki ACTIVE/PARTIAL ve CORE/S02'deki eski değerlendirme ifadeleri üretildikleri checkpoint'e aittir; current study STATE üstündedir. Ürünün benimsenmesi, kaynakların tüm iddialarının doğrulanması ve bu terim çıkarımının tamamlanması ayrı konulardır.

## Korunan ilk pilot

B1, context-memory-harness-engineering paketinin sekiz Markdown dosyası üzerinde kaynak snapshot'ı ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a ile tamamlandı. P1-T1 ilk döküm, P1-T2 ilişki eki, P1-T3 ekler/düzeltmeler ve B2 değerlendirmesidir. Faaliyet/nesne, tekil kayıt/sistem, farklı handoff kullanımları ve tasarım amacı/garanti ayrımları korunur; açık kaynak gerilimleri ortak ontolojik karar haline getirilmedi.

İlk pilotun ayrıntılı dosya SHA'ları, okuma aralıkları, kapanış gerekçesi ve yayın kayıtları [P1 kapanış STATE'inde](https://github.com/batuhanozgun/agentic-os-search/blob/53c29b54a355742960f466a06a5d9bba0a42f412/concepts/STATE.md) korunur. Bu tarihsel kayıt B1'i tekrar aktif yapmaz. METHOD §7 ve PLAN/R3 yöntemdeki dersleri taşır. Aynı veride öğrenilmiş v0.2 değişiklikleri bağımsız doğrulanmış yöntem sayılmaz.

## P2 kaynak bağlama ve gerçek envanter

Repository: batuhanozgun/agentic-os-search.

- Araştırma paketi: research/studies/superpowers/.
- P2 okuma snapshot'ı: **75bc6787844e9b1a8fed76ff5cfa4ca8ce63d847**, P2-T1 başlangıcında gözlenen main.
- Paket tree SHA: **56c19a5e2c0deb7b0f5164aac818ed2ba98baf12**.
- Alt ağaçlar: notes cc9611a59f65ec1175fd99885c01a6efebc202ed; syntheses bfb0603d70683e512df789bfa52c929caa67d9ea; evidence 7a5af9c7cf94551a42102bcfd9e2ddd36434cd9a.
- Paket kökünde 19 Markdown; notes altında 11 Markdown; syntheses altında 6 Markdown; evidence altında 8 runner ve 8 JSON sonuç dosyası. Toplam **52 dosya: 36 Markdown, 8 betik, 8 JSON**. Bu ağaçlarda başka alt dosya/binary ek yok.

İlk contents görünümü kesildiği için envanter onunla kapatılmadı. Sabit commit'in kök → research → studies → superpowers ağaç zinciri takip edildi. Paket kökü nonrecursive, üç alt ağaç recursive olarak tam döndü; her birinin ilk JSON kopyası truncated:false ile sonuna kadar görüldü. Tekrarlanan structuredContent kopyasının araçta kesilmesi, ilk tam ağacın yerine geçmez. Envanter içeriğin okunmuş olması değildir.

Bu research snapshot'ı, araştırmanın incelediği dış ürün pininden farklıdır: obra/superpowers@b36e0829c6d0140e93cfef2ca599b1b07d4a7797, manifest bağlamı 6.3.0. Dış ürünün bugünkü main'i, kurulu dosyaları veya güncel host API'leri bu pilotta yeniden doğrulanmadı. Lab/assessor pinleri de research içindeki atıf kimlikleridir; onların yeni araştırmasına başlanmadı.

## P2-T1 — Tam okunan 15 dosya

Aşağıdaki yollar research/studies/superpowers/ tabanına göredir. Tam okuma dosya sonuna kadar görülen içeriği ifade eder; belirtilen son istek üst sınırı gerçek satır sayısı değildir.

| Dosya | Blob SHA | Okuma |
|---|---|---|
| STATE.md | 472b9f16bd68d0e05a4108fb1b2155ee2b7a2d2f | Tam, tek dosya yanıtı. |
| META.md | 80c32a688127ca811421c9579cd9fef7a1c0d6a9 | Tam, önceki hazırlık okuması yerine P2'de tekrar. |
| INDEX.md | c170993756d19c2d98831ca1dd371c5aadf3c53a | Tam. |
| CORE.md | 0986da960a4b3db5d1e09894c2abfd6d6ca114be | 1–100 ve 101–EOF; son istek 220. |
| CLOSURE-AUDIT.md | b6178fdc2817eaf93c447434a014ca971a972348 | 1–100 ve 101–EOF; son istek 240. |
| METHOD.md | 95f684306f92373dbb51f4ceedaff885394e950b | Tam; kaynak araştırmasının yöntemi, concepts v0.2 ile aynı dosya değil. |
| PLAN.md | ea86caa9144bfd462428a3c8ef3ffb6ab7d5ca00 | Tam; kaynak araştırmasının kapanmış planı. |
| SOURCE-LEDGER.md | a09cd522f1b51cec1d3fc9c30a017f8931e35dd2 | İlk 1–115 isteğinin sonu kesildi; 105–EOF örtüşmesiyle tamamlandı, son istek 230. |
| notes/U01-entry-routing-and-bootstrap.md | 8b8e63451e77d78e7b9be4de190944157a8120f2 | 1–130 ve 131–EOF; son istek 280. |
| notes/U01B-host-delivery-and-continuity.md | cc2c0ba68f8d90ec6680b9b4b2d7cc0bc3405620 | 1–120 ve 121–EOF; son istek 260. |
| syntheses/S02-availability-runtime-and-distribution.md | 0546c46231ef17da3cdb204520d7846176c27cfe | Tam. |
| evidence/U01-hook-probes.py | 9ca0b43739e69c930d1241601bb61b7ef1872ff1 | Tam kaynak okuması; çalıştırılmadı. |
| evidence/U01-hook-probes-results.json | 0a21d98568b71a7c1d99385b9d8ae88611ebed78 | Tam tarihsel sonuç okuması; yeni koşu değil. |
| evidence/U01B-opencode-probes.mjs | 6a99be598bac4d60943c816857124c907882c089 | Tam kaynak okuması; çalıştırılmadı. |
| evidence/U01B-opencode-probes-results.json | fae46fb808c5814fc7039f874f7d9aae5e5b34f3 | Tam tarihsel sonuç okuması; yeni koşu değil. |

Bu 15 dosya 11 Markdown, iki runner ve iki sonuç dosyasıdır. Runner'ların kullandığı upstream betik/modül bu tur ayrıca edinilip çalıştırılmadı. SOURCE-LEDGER içindeki upstream FULL etiketleri önceki araştırmanın kapsama kayıtlarıdır, P2 actor'ının bütün o dış dosyaları okuduğu iddiası değildir.

## Henüz okunmamış 37 dosya

Aynı paket tabanına göre, sabit tree üzerinden geri kazanılacak tam kalan liste:

**Kök kaynak kayıtları — 11:** SOURCE-LEDGER-U03.md; SOURCE-LEDGER-U04.md; SOURCE-LEDGER-U05.md; SOURCE-LEDGER-U06A.md; SOURCE-LEDGER-U06B1.md; SOURCE-LEDGER-U06B2.md; SOURCE-LEDGER-U07A.md; SOURCE-LEDGER-U07B.md; SOURCE-LEDGER-U08A.md; SOURCE-LEDGER-U08B.md; SOURCE-LEDGER-U08C.md.

**Mekanizma notları — 9:** notes/U02-approval-plan-workspace-handoff.md; notes/U03-delegation-review-and-acceptance.md; notes/U04-testing-diagnosis-and-verification.md; notes/U05-delivery-cleanup-and-retention.md; notes/U06A-skill-authoring-and-change-admission.md; notes/U06B1-evaluation-evidence-and-verdict.md; notes/U06B2-assessor-contracts-and-evidence-qualification.md; notes/U07A-visual-companion-lifecycle.md; notes/U07B-distribution-versioning-and-support.md.

**Sentezler — 5:** syntheses/S01-skill-evolution-and-evaluation.md; syntheses/S03-intent-planning-and-context-handoff.md; syntheses/S04-execution-verification-and-delivery.md; syntheses/S05-native-system-model.md; syntheses/S06-project-facing-contribution-and-comparison.md.

**Deney betikleri/sonuçları — 12:** evidence/U02-handoff-probes.py; evidence/U02-handoff-probes-results.json; evidence/U03-review-probes.py; evidence/U03-review-probes-results.json; evidence/U04-diagnostic-probes.py; evidence/U04-diagnostic-probes-results.json; evidence/U05-lifecycle-probes.py; evidence/U05-lifecycle-probes-results.json; evidence/U07A-companion-client-probes.mjs; evidence/U07A-companion-client-probes-results.json; evidence/U07B-version-probes.py; evidence/U07B-version-probes-results.json.

Kalan liste yalnız metadata/okuma hesabıdır; terim envanteri veya bu dosyaların ayrıntılı sonuç özeti değildir. Dosyaların kronolojik eski açık işleri mevcut concepts görevi diye otomatik çalıştırılmaz.

## P2-T1 — Yorum, yöntem ve kapsam notları

Kullanım kayıtları bu STATE'e taşınmadı; görünür P2-T1 yanıtı ilk taşıyıcıdır. Bu devam notları, hangi ayrımların sonraki turda kaybolmaması gerektiğini belirtir:

- Giriş metinleri genel sistem açıklamasıdır. U01-A/U01-B ve ilk kaynak kaydı üzerinden başlangıç/host-delivery adları daha ayrıntılı ele alındı. CORE'daki bütün rol, review, distribution ve evaluation adları alt kaynakları da incelenmiş nihai kullanım kayıtları sayılmaz.
- Ürünün kendi adları ve atfedilen talimatları, önceki araştırmanın açıklayıcı zincirleri, araştırmaya ait deney dili ve bu pilotun Türkçe açıklamaları ayrı tutulur. Yazılı yükümlülük ile gözlenmiş çalışma başarısı birleştirilmez.
- Bootstrap'ın aktarılması, güncel dosyanın yeniden okunması ve mevcut işin geri kazanılması aynı olay değildir. Modül, registration, oturum ve message-array ömürlerinin ayrımı sonraki kaynaklarda da kaybolmamalı.
- Host tool mapping yalnız isim çevirisi gibi anlatılmamalı; kaynak bazı fallbacks'in işin aktörünü/bağlam ayrımını değiştirdiğini söylüyor. Bu, herhangi bir hostun güncel davranışını bu tur doğruladığımız anlamına gelmez.
- Araştırma runner'larında kriter ve result alanları incelendi: mechanism PASS, health-challenge FAIL ve oracle-negative-control ayrı sınıflar. Kaydedilmiş bir davranışın tekrarlandığını bildiren PASS, o davranışın güvenli/yararlı olduğunu sertifikalamaz. Bu kaynak/çıktı çapraz okumasıdır; yeni deney veya bağımsız doğrulama değildir.
- S02 tam okundu, ancak onun U07 paketleme/visual-companion kaynak notları henüz okunmadı. Bu kısımların kullanım adayları kendi kaynaklarına bağlı bekler; sentezin okunması alt dosyaların okunmuş olması değildir.
- Scope/approval, controller/worker/reviewer ve qualified completion üzerine ilk genel kullanım gözlemleri U02/U03/U05 ayrıntıları geldikçe netleşebilir. İlk görünüm kaynakların açıklamadığı sınırlara genel tanım eklemez.
- Her dosyada kullanılan her doğal dil sözcüğüne tanım üretme veya bütün belirsizlikleri çözme hedefi yoktur. Bununla birlikte 37 okunmamış dosya ve paket genelindeki kapanış kontrolü gerçek açık iştir; kaynak belirsizliği gerekçesiyle kapatılmaz.

V0.2 yönteminin bu turdaki ilk uygulaması, önceki paketin üçlü çerçevesini taşımadan kaynak-içi ilişki görünümü kurmaktır. B4 sonucu verilmedi; ikinci pilotun başarı hükmü veya yeni yöntem sürümü üretilmedi. Karşılaşılan ek terminoloji bağımsız dış araştırma dalına çevrilmedi.

## Current work ve next authorised work

**Tamamlanan:** hazırlık; B1/B2; B3 için 52 dosyalık source-bound envanter; yukarıdaki 15 tam okuma ve giriş/host-delivery odağındaki ilk konuşma içi kullanım dökümü.

**Sıradaki yetkili iş hâlâ B3:** P2-T1 görünür dökümünü ve bu okuma hesabını geri kazan. Önce notes/U02-approval-plan-workspace-handoff.md ile evidence/U02-handoff-probes.py ve sonuç JSON'unu tam oku. İlk SOURCE-LEDGER zaten okundu; U02 S28–S36 kısımlarına gerektiğinde geri dön. Sonra notes/U03-delegation-review-and-acceptance.md, SOURCE-LEDGER-U03.md ve U03 runner/sonuçlarını ele al. İhtiyaç/approval → spec/plan → workspace/task brief → delegation/review ilişkisini kendi kaynak kullanımlarıyla çıkar; önceki giriş özetinin tanımlarını dayatma.

Ardından kalan U04–U07 notları/kaynak kayıtları/deney dosyaları ve okunmamış sentezler tamamlanır; U08-A/B/C kaynak kayıtları da atlanmaz. Tam paket okuması birden fazla tura yayılır. Okuma sırasında kullanım çıkarımı yapılır; bütün paket bitince hafızadan liste kurulmaz. Paket sonunda kaynak bölüm/liste/tablo/örneklerinden döküme kapsam kontrolü ve gerekli düzeltmeler yapılır. Sonra B4 değerlendirmesi gelir. B3 veya B4 tamamlanmadan kalıcı seri çıkarım; bütün araştırmaların çıkarımı bitmeden ortak referans başlamaz.

## Yeni oturum ve pilot çıktılarının devralınması

AGENT ve tetiklenen protokoller → concepts/INDEX → bu STATE → CHARTER → ORIGIN → METHOD → PLAN → SETUP-REVIEW → P2'nin mevcut görünür yanıtları → kaynak paketin current STATE/META/INDEX ve gereken source-bound dosyalar.

Yeni oturumda zorunlu girişler tam okunur. Aynı konuşmadaki tam ve değişmemiş okumalar mekanik biçimde tekrarlanmaz. Görünür P2-T1 yanıtına gerçekten erişilebiliyorsa tamamı okunur; yalnız STATE özeti veya okuma sayısı yerine konmaz. Erişilemiyorsa kaynak snapshot'ından gerekli kullanım yeniden çıkarılır ve yeniden üretim olduğu belirtilir; yeni actor önceki actor'ın okuma kaydını kendi okuması saymaz. Pilotun chat-only sınırı sessiz yeni TERMS arşiviyle aşılmaz.

B1 sırf eski sohbet görünmüyor diye tekrar aktif sayılmaz. İlk pilot terimleri yeniden kullanılacak veya kalıcılaştırılacaksa P1-T1/T2/T3 görünür kayıtlarına ve sabit kaynaklarına geri dönülür. Bu STATE yanıtın teslim/alım makbuzu değildir.

Önce main ile P2 snapshot'ının ilgili dosya değişimini kontrol et. Yeni/değişen kaynaklar eski kayda sessizce yükseltilmez; delta açık tutulur. Zorunlu kontrol veya gerekli kaynak erişilemiyorsa eksik bilgi tahmin edilmez.

## Yayın ve doğrulama bağlamı

P1 kapanışı 53c29b54a355742960f466a06a5d9bba0a42f412; METHOD v0.2 commit'i 839e760a2e306e0011826501f4580b841ecc2f04; PLAN v0.2 commit'i 67351f0808dd8175d3297f03258d49379a23ad56. Önceki hazırlık ve ilk pilot ayrıntıları bu kaynaklardan ve SETUP-REVIEW'den geri kazanılır.

P2-T1'de AGENT ve R01–R09 canonical içerikleri tam okundu; concepts STATE tekrar tam okundu. Aynı konuşmada tam okunmuş diğer concepts girişleri/v0.2 yöntem-plan, ilk pilot kapanışından güncel main'e karşılaştırmada değişmemişti. Superpowers kaynak dosyaları P2 snapshot'ına bağlandı. Yayın öncesi snapshot→main karşılaştırması yalnız ECC dosyalarında değişiklik gösterdi; concepts ve Superpowers değişmedi. Eşzamanlı ECC içeriği yeniden yazılmaz.

Bu tur yalnız STATE'e SHA kontrollü güncelleme yapılır; yayın sonrasında dosya geri okunur ve kendi commitinin parent→commit farkı kontrol edilir. Bu kontroller kalıcı yerleşim ve kapsamı doğrular, araştırma doğruluğu/host davranışı veya drift'in önlenmesini bağımsız olarak kanıtlamaz. Yeni dış kaynak araştırması, canlı deney, kurulum, credential kullanımı veya upstream yazma yapılmadı.
