# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-21 · **C1–C5 SOURCE-FAMILY TRANSFER COMPLETE / C6a CENSUS-RECONCILIATION COMPLETE / C6 ACTIVE-PARTIAL / PACKAGE-PARTIAL**.

[TERMS.md](TERMS.md) kullanımları, [global STATE](../../STATE.md) program yetkisini taşır. **Güncel ayrıntılı C6 kaydı [C6-RECONCILIATION.md](C6-RECONCILIATION.md); dosya bazlı hesap [C6-SOURCE-MANIFEST.tsv](C6-SOURCE-MANIFEST.tsv).** C6a'nın kapanışı bütün kaynakların tam okunması veya ECC paketinin kapanışı değildir.

## 1. Amaç, kaynak ve tarih

Amaç mevcut research/studies/ecc/ araştırmasını kendi bağlamında tam okuyarak kullanımları ve ilişkilerini çıkarmaktır. Yeni upstream araştırması, ürün testi, genel tanım veya SOUL mimarisi yapılmaz. METHOD v0.3-working, SCOPE S1 ve açık post-S1 hesabı korunur. Kaynak-study'nin current işi Concepts next-work değildir.

C6 census snapshot'ı **batuhanozgun/agentic-os-search@41f6603677ccbe81bb6a467d1bc39f0965794e06**; ECC package tree **d591a687899e39035393ef1dc107b5c56b33c92a**. Ayrı upstream research pin **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**. Eski 159-file tree **b6df4013a0f8275da82d6f27a2cd354201c5c70b** baseline'dır, current scope değildir.

Önceki tam READING [597a7b1 sürümünde](https://github.com/batuhanozgun/agentic-os-search/blob/597a7b1ac0949c6505ce6227c6d4f4d1a46d4c5b/concepts/studies/ecc/READING.md), blob **3c165169f9daa9f2deebf8e0631d8437f4032c9e**, korunur. Bu tam dosya U12-C/E09 manifestini, gerçek read-only recovery kapsamını, kaynak/yorum ayrımlarını, yayın kimliklerini ve daha önceki yedi tam kayıt bağlantısını taşır. Hiçbir eski okuma veya maddi düzeltme bu kısa current entry ile silinmiş sayılmaz.

C6-RECONCILIATION §3 **H1–H8'in tamamını ayrı ref/blob ve gerçek devralma biçimiyle** listeler. H1–H5 bu tur canonical FULL yeniden alındı; H6/H7/H8'in aynı konuşmadaki tam ve değişmez içerikleri korundu. Sekiz yeni full read veya 167 source-body okuması iddia edilmez. Korunmuş TERMS router tarihleri ve bütün 15 kullanım dosyası C6 girdisidir; paket-geneli semantik kontrol henüz bitmedi.

## 2. Aktarım standing'i

| Dilim | Durum |
|---|---|
| C1–C4 / U01–U09 | Önceki bağlamlı source-family aktarımı korunur; aşağıdaki erken ham içerik/kayıt açıkları C6'da hedefli kapatılır |
| C5a / U10-A/B | Aktarım complete; E/O kayıtları korunur |
| C5b / U11-A–E | Aktarım complete; N/SC/RD/BC/TL kayıtları korunur |
| C5c / U12-A/B1/B2/C | Aktarım complete; EP/OC/OD/PY ve E09'un kayıtlı read-only incelemesi korunur |
| C6a | Snapshot census, baseline delta ve geçmiş okuma-dayanağı hesabı bu tur tamamlandı |
| C6b | Exact next: erken deney betikleri/ham kanıt recovery ve kaynak-kayıt karşılaştırması; başlamadı |
| C6 devamı | Kök geçmiş/current plan/questions, inventory, U13 ve sonraki delta, bütün TERMS/rol/ID/ilişki kontrolü açık |
| ECC Concepts package / B7 / B8 | Package PARTIAL; B7/B8 NOT STARTED |

C6a/b mevcut reconciliation'ın yürütme dilimleridir; yeni program veya genel araştırma aşaması değildir. Kullanım adedi kavram, bağımsız kanıt veya ilerleme yüzdesi sayılmaz.

## 3. Bu turun gerçek kapsamı ve önemli açıklık

167 source leaf: **64 root + 29 notes + 70 evidence + 4 inventory**. Baseline'a göre **8 added, 5 changed, 154 unchanged, 0 deleted**. Her yol/blob ve okuma-dayanağı TSV'dedir. Current ağaç ve 11 evidence alt ağacı dahil 15 tree yerelde yeniden hesaplanıp GitHub kimlikleriyle eşleşti; baseline tree de yeniden eşlendi. Eksik yaprak ve yanlış blob negatif örnekleri eşleşmedi. Bu metadata/temsil kontrolüdür; içerik/terim doğruluğu veya ürün deneyi değildir.

Census source STATE/META/INDEX FULL okundu; U13-B complete, sonraki source U14-A idi. H1–H5 FULL geri kazanıldı ve H6–H8 ile birlikte read-basis hesabına kullanıldı. Protocol/amaç kontrolü: AGENT fresh aynı aea3dd845e0f0bbcfb34465edb23782e99f95c80; R01–R09'un ve mandatory Concepts girişlerinin aynı konuşmadaki tam/değişmemiş canonical içerikleri korundu. Giriş compare'ı Concepts/control değişikliği göstermedi. Kontrol metinleri research corpus yapılmadı.

**Maddi açıklık:** H1 bazı compressed E04/E05 sonuçlarını README/not/kimlik/rol üzerinden ele almıştı. Bu, decoded ham dosyanın tamamının okunduğu anlamına gelmez. Ayrıca beş erken betik için açık FULL kayıt bulunmuyor; dört master-history dosyası selected bölümlerle kayıtlı. Önceki family closure, bu açıklıklar üzerinden package FULL hükmüne yükseltilmez. Eski tarihsel dosya veya önceki kullanım metni sessizce değiştirilmedi; bir TERMS anlamının yanlışlığı henüz gösterilmiş değildir.

TSV kodları ve sınırları C6-RECONCILIATION §2'de: P136 önceki raporlanmış aktarım, F3 yeni full source context, S4 selected history, D2 changed current root, N8 yeni U13, U5 betik full-read kaydı eksik, R3 decoded kapsam açık, Q2 E06 quarantine, I4 inventory reconciliation. P136 bağımsız doğrulanmış 136 full-read veya tamamlanma oranı değildir.

E07 runner, E08 decoded kayıtları ve E09'un beş arşiv üyesi önceki manifestlerde açıkça okunmuş olarak kayıtlıdır; erken betik açığı bunlara genellenmedi. E06 NOT VERIFIED/EXCLUDED, Node/Python iki E05 geçmişi ayrı kalır. Bu tur betik çalıştırma veya arşiv decode yapılmadı.

## 4. Census sonrasındaki açık delta

**41f6603→23e1b437bd255342edff8d61d0246f1e66444fb2** karşılaştırması ayrı source işinin ROUND-U14-A.md ve evidence/U14-A-SOURCES.md eklediğini, source STATE'i değiştirdiğini gösterdi. STATE bu ref'te FULL okundu: **a032f8b892b81171054ffbcae58538299d60f3a7**, U14-A IN PROGRESS; son completed U13-B. İki yeni U14 gövdesi Concepts'te okunmadı/aktarılmadı.

Bu yüzden 167 satırlık manifest **41f6603 için tamdır; son main için tamamlanmış census değildir**. C6 devamında bu ref'ten fresh main'e bütün ek/değişen/silinen yollar alınır. U13 veya U14 ilk C1–C5 planında yok diye dışlanmaz. Kaynak araştırması bu Concepts turunda yürütülmez; kendi next görevi devralınmaz. Yayın sırasında başka kaynak ilerlerse aynı delta zinciri korunur.

## 5. Exact next ve C6 çıkış koşulu

İlk gövde: **research/studies/ecc/evidence/u01-a-cache-probe/run-cache-probe.py** (census blob **589c9a31634df43fe96fc9f92c3e105b4ea4b163**). Ardından E02 **u03-a-work-item-probe/run-probe.js**, E03 **u03-b-worker-probe/run-probe.py**. Bunları FULL okuyup mevcut plan/sonuç ve S/W kullanımlarıyla karşılaştır; yeni target experiment çalıştırma.

Sonra U05-B/U06-A probe.cjs ve üç R taşıyıcısı: results.json.gz, results.json.xz, conversation-record/original-evidence.tar.xz. Exact-byte read-only recovery ve ham kapsam okuması; iki E05'i birleştirmeme, E06'yı yeniden aktive etmeme. Gerekli gövde erişilemiyorsa kaydedilmiş özetten içerik uydurma veya full-complete sayma.

Kalan kaynak geçmişi: METHOD-REVIEW.md, PUBLICATION.md, RESEARCH-LOG.md, SOURCE-LEDGER.md; current PLAN/QUESTIONS; dört inventory dosyası. U13-A/B sekiz yeni dosyanın aktarımı ve census sonrası tüm delta da açık. Bütün TERMS + router source-point/rol/ID/ilişki ve maddi düzeltme etki kontrolü ayrıca yapılır. C6 yalnız bu somut yükümlülükler karşılandığında version-qualified package closure verir; tekrar tekrar census yapmayı içerik okumasının yerine koymaz.

ECC sonrası seri paket **work-management-project-control**. Post-S1 agentmemory/claude-swap/cli-continues/ponytail B7 öncesi global kapsamda tutulur; B7 geçmeden B8 başlamaz. Kaynağın güçlü runtime/authority/acceptance soruları otomatik yeni Concepts deney borcu değildir.

## 6. Yayın, koruma ve iki risk

C6 TSV commit **908036f154c639cb0a6b24e5197c3d76fd06cc83**, prepared/remote blob **92d319d2863b3838b53ea326484e7dff65960864**, 13,484 bytes. C6 rapor commit **476683b0fb95cc3bf5aeaf1fe6a1b05d65b621c3**, FULL readback 1–92/93–EOF, blob **525733dbef7d4409b3ddb7c477b68cd852ed9c27**. Detaylı mekanik kontrol ve helper düzeltmesi rapor §5'tedir; başarısız ilk helper hesabı ECC arızası sayılmadı.

Yerel READING/TERMS/global STATE yayını sonrası final diff/ref ve readback ayrıca yapılır; bu metin gelecekteki kendi hash'ini veya yapılmamış kontrolü uydurmaz. Source/agent-control/diğer araştırmalar, eski TERMS, Foundation, explorations ve publications bu çalışma tarafından değiştirilmez. Yeni target execution, provider/model, install, release veya branch deletion yoktur.

Batu okuma anındaki anlam seçimlerini denetleyemediğinden kapsam ve yorum değişikliği izlenebilir tutulur. Ortak sözcük ortak anlamı garanti etmez; complete/read/verified ilgili nesne ve kapsamla yorumlanır. Kaynak kullanımı, araştırmacı/extractor yorumu ve kullanıcı onayı teknik doğruluk bakımından ayrı kalır. Same-assistant census/readback, bağımsız semantik veya ürün doğrulaması değildir.
