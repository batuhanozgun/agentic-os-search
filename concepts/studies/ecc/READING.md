# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-23 · **C1–C5 SOURCE-FAMILY TRANSFER COMPLETE / C6a COMPLETE / C6b E01–E05 RAW-EVIDENCE COMPLETE / C6 ACTIVE-PARTIAL / ECC PACKAGE PARTIAL.**

[TERMS](TERMS.md) bağlamlı kullanımları, [global STATE](../../STATE.md) amaç ve current/next işi taşır. C6a'nın envanter ve geçmiş okuma hesabı [C6-RECONCILIATION](C6-RECONCILIATION.md) ve [snapshot manifestinde](C6-SOURCE-MANIFEST.tsv) korunur. Bu current dosyanın §2–§4'ü E01–E03, §7 ise E04/E05 driver ve raw-recovery katmanıdır; C6a'nın tarihsel U/R kodlarının güncel karşılığı burada tutulur.

## 1. Amaç, kaynak ve korunmuş geçmiş

Mevcut research/studies/ecc araştırmasını kendi bağlamında tam okuyarak terim/kullanım ve ilişkilerini çıkarmak. Genel terim araştırması, ürünün yeniden çalıştırılması, ortak tanım veya SOUL/Development OS mimarisi yapılmaz. METHOD v0.3-working, SCOPE S1 ve açık post-S1 hesabı korunur. Kaynak araştırmasının next işi Concepts'e teknik araştırma yetkisi vermez.

Bu turun sabit okuma kaynağı **batuhanozgun/agentic-os-search@7ce22d478071be0863e7677bae280e2d648736d6**. Ayrı upstream research pin **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**. Son Concepts checkpoint'i **3acfa615092cfc264df126a800c8d7c74ed646fd** ile giriş arasında 218 commit vardı; karşılaştırma Concepts veya agent-control değişikliği göstermedi. Ayrı kaynak/explorations/context işleri korunur; bu turun çalışması sayılmaz.

Önceki tam okuma ve kontrol kaydı [3acfa615 READING](https://github.com/batuhanozgun/agentic-os-search/blob/3acfa615092cfc264df126a800c8d7c74ed646fd/concepts/studies/ecc/READING.md), blob **55872549b7f5d910497c58d9c69550be783fb361**, olarak korunur. [C6a raporu](https://github.com/batuhanozgun/agentic-os-search/blob/3acfa615092cfc264df126a800c8d7c74ed646fd/concepts/studies/ecc/C6-RECONCILIATION.md), blob **525733dbef7d4409b3ddb7c477b68cd852ed9c27**, H1–H8'in tam değişmez sürümlerini, kaynak-aile kapanışlarının sınırlarını ve tarihsel düzeltmeleri bağlar. Bunlar kısaltılmış özetle ikame edilmez. Bu tur H1–H8'in tamamının yeniden okunduğu iddia edilmez.

**C6-SOURCE-MANIFEST.tsv**, **41f6603677ccbe81bb6a467d1bc39f0965794e06** snapshot'ının 167 yaprağını ve C6a anındaki read_basis'i taşır; canlı güncel okuma tablosu değildir. Dosya değiştirilmedi. Aşağıdaki exact path/blob tablosu üç U kaydının kapanışını bu tarihi manifestin üzerine ekler. Kalan U2/R3 ve diğer açıklar silinmez. 167 sayısı bugünkü kaynak dosya sayısı olarak kullanılmaz.

## 2. E01–E03 gerçek okuma manifesti

Aşağıdaki yollar **research/studies/ecc/** tabanına ve bu turun snapshot'ına bağlıdır. On iki mevcut dosyanın tamamı doğrudan okundu. Üç driver C6a'daki açık betik kapsamını kapatır; dokuz plan/sonuç/README yeniden tam karşılaştırma girdisidir. FULL, atfedilen upstream dosyaların bu tur ayrıca okunması veya çalıştırılması değildir.

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| evidence/u01-a-cache-probe/run-cache-probe.py | 589c9a31634df43fe96fc9f92c3e105b4ea4b163 | FULL; tek canonical gövde |
| evidence/u01-a-cache-probe/PROBE-PLAN.json | 223222466e1d23b2665014b01019a9ae42a9033b | FULL |
| evidence/u01-a-cache-probe/RESULTS.json | de5989d3c0bcfba1d1614cb2749b961267d26249 | FULL; üç vaka ve bütün metadata/raw çıktılar |
| evidence/u01-a-cache-probe/README.md | 5b26e6075773cc1e41ed1d3d7ec21c19218fbed5 | FULL |
| evidence/u03-a-work-item-probe/run-probe.js | 70b085de4e53ca56952cd223d6ee55125c233165 | FULL; tek canonical gövde |
| evidence/u03-a-work-item-probe/PROBE-PLAN.json | f85e0407f0fa558bc2f6f1f1854e02412b8e7bfb | FULL |
| evidence/u03-a-work-item-probe/RESULTS.json | 48b4a5e6f3bd4b399731937947ab51c25e4937da | FULL; altı vaka ve bütün metadata/observation |
| evidence/u03-a-work-item-probe/README.md | 7c4301b6d5a5aba4440a3ec76367f3a66f6628ce | FULL |
| evidence/u03-b-worker-probe/run-probe.py | 425eedbeaa78cf1274c94d4dbe38b96b4b31f81e | FULL; tek canonical gövde |
| evidence/u03-b-worker-probe/PROBE-PLAN.json | a1b94660cd5fe969b2612eb8cb577a5a4be21887 | FULL |
| evidence/u03-b-worker-probe/RESULTS.json | 33d00a3d8653c674ad6d33163875804657d7979f | FULL; 1–140 + 141–EOF, beş vaka/bütün raw alanlar |
| evidence/u03-b-worker-probe/README.md | 6af0f88ac7bd378e854e115a1035e883a6c30acb | FULL |

On iki blob C6a manifestindeki kimliklerle aynıdır. İçeriğin okunmuş olması tarihsel deneyin yeniden gerçekleşmesi değildir; hiçbir driver/import/checker/helper/wrapper/collector çalıştırılmadı. Original upstream source snapshots bu evidence dizinlerinde yoktur; yeniden edinilmedi. Bu tur byte-hash reperformance, schema suite veya bağımsız aktör doğrulaması yapılmadı.

**Karşılaştırılan mevcut Concepts dosyaları:** TERMS-SURFACES-INSTALLATION.md, blob **1c7863d2baeaa840c4fba999a4e9d5a0843e1f4f**, FULL; TERMS-WORK-EXECUTION-MEMORY.md, blob **8b6b5aa7db69ff929aae15d8bee9b1f2cf6ac020**, FULL 1–85 + 86–EOF. Bütün dosyaların okunması, bu tur yalnız erken-evidence ilişkileri üzerinden yapılan kontrolü bütün memory/installation kaynaklarının yeni doğrulamasına genişletmez.

**Preflight/source context:** Fresh AGENT full aynı aea3dd845e0f0bbcfb34465edb23782e99f95c80 idi. R01/R02/R03/R04/R05/R07/R08/R09 canonical metinleri full yeniden okundu; kesilen R01/R03/R04/R09 kuyrukları örtüşmeyle tamamlandı. R06'nın aynı konuşmada tam okunmuş ve değişmemiş sürümü korundu. Concepts giriş/amaç/yöntem/SCOPE ve C6a'nın aynı konuşmadaki tam içerikleri, unchanged comparison ve current STATE ile devralındı. Bunlar araştırma korpusuna katılmadı.

## 3. Aktarım ve kaynak taraflı kontrol

Yeni dosya [TERMS-EARLY-PROBE-EVIDENCE.md](TERMS-EARLY-PROBE-EVIDENCE.md), **ECC-PE01–PE17**. Bunlar araştırma-düzeneği ve kanıt alanlarıdır; ECC ürününde 17 yeni yetenek veya ortak kavram değildir. Kaynak locator/roller, 14 kayıtlı vakanın S/W/PE karşılıkları ve önemli sınırlar dosyanın §1–§6'sında bulunur.

Üç ayrı ilişkinin hesabı verildi:

- E01: exact-source guard → varlık/tür fixture'ı → checker exit → kaynak tahmini ile normatif bütünlük ölçütünün ayrımı. C1 false-green ve C2 gerçek sensitivity kontrolü birlikte korunur.
- E02: unchanged helper → in-memory store double → claim/move ve calls/writes. BlockedBy illustrative, newest-first input order stipulated; SQL, dependency engine, authentication veya concurrency çalıştırılmış sayılmaz.
- E03: gerçek wrapper/collector → sahte codex'in argv/prompt/output/exit kaydı → raw ve parsed handoff → status/diagnostic/temporary-file gözlemleri. Completed ile metinsel başarısızlık, raw retention ile parsed boşluk ve partial-output kaybıyla stderr korunması ayrı tutulur.

Plan/kriter ayrımı özellikle kontrol edildi: E01 driver plan cases/expected exit tüketir; E02 plan dosyasını okumaz ve vaka/assertion'ları kodda tutar; E03 plan baytlarını hash/eşlik için okur fakat specifications/check'leri ayrıca kodlar. Plan metinleri ile gerçek check ve raw sonuçlar bu nedenle birlikte karşılaştırıldı. PlanUnchanged veya hash tek başına semantik kriter eşliği değildir. E03 C0'daki check, kayıttaki her parsed alanı otomatik sınamıyor; raw kayıt ayrıca okunmuştur.

**S/W etkisi:** S12–S14, W01–W11 ve W42–W52 için açıklamaları değiştirmeyi gerektiren maddi çelişki saptanmadı. W11 zaten deney metadata'sını doğru ayırıyordu. Eski kullanım metinleri değiştirilmedi. W37/W39 veya W53–W55 gibi setup/rollback/live observation alanları bu deneylerden doğrulanmış sayılmadı. Yeni PE kayıtları ve bağlam sınırları eklenmiştir; sorun varmış gibi eski düzeltme hikâyesi üretilmedi.

**Durum değişimi:** C6a'nın ilk üç U kaydı E01/E02/E03 için burada kapanmıştır. E04/E05 driver ve compressed-recovery kapanışı §7'de kayıtlıdır. E06 quarantine davranış kanıtı değildir; iki E05 birleştirilmez.

## 4. Güncel kaynak delta'sı

Giriş snapshot'ında source STATE FULL: **31eadc2b3d3e128458bbb42f9d0b3eb663783cce**, U18-F IN PROGRESS/son completed U18-E; source META FULL **e7d13368ce88c00826121e754ff7d90ecc925d98**; INDEX FULL **a8a44b1bfbfc62dcca3c699fea5c44955882905f** (kesilen son alan 100–EOF ile tamamlandı). META/INDEX'in activation öncesi NOT STARTED dili source STATE yerine geçmedi. Kaynak dosyaları Concepts adına düzeltilmedi.

3acfa615→7ce22d4 farkında U14 devamı, U15/U16/U17/U18 çıktıları, U17 E10 evidence/recovery, inventory/U15-A-COVERAGE-RECONCILIATION.md ve source girişleri görünüyor. Note45 yolu da karşılaştırmada var; gövdesi burada okunmadı, yayımlanmış tam inquiry diye sınıflandırılmadı. Uzun compare'daki bazı sıfır değişim istatistikleri boş kaynak veya yokluk kanıtı yapılmadı. Bu tur yeni whole-package tree census veya bütün yeni yolların içerik aktarımı yapılmadı.

C6a'nın 41f6603 snapshot'ından fresh main'e bütün kaynak delta'sının yaprak hesabı ve aktarımı hâlâ gereklidir. Şimdilik diff ve source-entry okuması kuyruk görünürlüğü sağlar; U13–U18 veya E10 burada tamamlanmış sayılmaz. E10'un recovery yönü öğrenildi fakat ham taşıyıcı/restore betiği çalıştırılmadı. Her tur yeniden sayım yapıp erken ham içerik açıklarını ertelemek yerine bu tur üç somut betik açığı kapatıldı.

## 7. C6b E04/E05 — driver + raw evidence recovery

Sabit evidence snapshot'i driver/raw karşılaştırması için **7ce22d478071be0863e7677bae280e2d648736d6**. Source-study daha sonra ilerlemiştir; bu historical evidence dosyalarının blobları current main'de değişmemiştir.

Tam okunan driver/control surfaces:
- `evidence/u05-b-evaluation-probe/probe.cjs` — **16333fcf9d2bbe208fee061044a997d7aa06e2d3**
- E04 PLAN/README — **ac291d5... / 0e56aec...**
- `evidence/u06-a-config-probe/probe.cjs` — **7d855c5960636925e97da6b2cbffa9c20b673bea**
- main-path E05 PLAN/README — **66a89a78... / 9c0333...**
- conversation-E05 reconciliation README — **fd078797...**
- Note08/U05-B ledger/round/receipt and Note09/U06-A ledger/round/receipt, mevcut source-local interpretation ve publication identity kontrolü için tam/ilgili gövde düzeyinde devralındı.
- `TERMS-LEARNING-GOVERNANCE.md` tam karşılaştırıldı.

Read-only exact-byte recovery:
- E04 `results.json.gz`: Git blob **8a3796d5523276ea9366a1cc1535d9e127985dfe**; compressed 2,407 bytes / SHA-256 **146bf000882a9433d1c95ad720619bd453153d7ef879506381d7549c92450a1a**; decompressed JSON 29,810 bytes / SHA-256 **38c73adf0f4b57df3f98876bc58180cf5feb677fe9e8a8522d1c6716e57a6ad4**.
- Node E05 `results.json.xz`: Git blob **e2838d28f0a3a6bf6e36561569f8bc03215792d9**; compressed 2,276 bytes / SHA-256 **0c8d7947ff27614ceaebcd432852571a8d8c42ede4d33b0fa22e493ee37783f9**; decompressed JSON 1,065,861 bytes / SHA-256 **a63c2e5b624463c1c16af2cb6931c68b78f9232edcfb3339795bd58dacd3f6d0**.
- Conversation E05 `original-evidence.tar.xz`: Git blob **3257a0c22d9a4809b0291e3678389182c29675d0**; archive 7,116 bytes / SHA-256 **c12d0603d952bfe33c027c6a3bf5f804ebc0063a27d454516fce2627519f5275**. Beş member tam açıldı: PLAN, README, probe.py, results.json, stderr.txt; member hashes reconciliation README ile eşleşti.

Raw sonuç standing'i:
- E04: tek recorded run, 9 case / 9 driver-local expectation match. Duplicate-ID, unmatched-task, mixed-amendment ve single-failure proposal sınırları raw JSON'da görüldü; **9/9 quality score değildir**.
- main-path E05: Node driver, 15 case / 15 driver-local match. Alias realpath/inode, profile/disable/dry-run, malformed/non-string/truncated input ve fixture invariants raw kayıtta korundu; **15/15 security score değildir**.
- conversation E05: Python driver, 16 case / 16 recorded match. Aynı dört upstream source blob'una bağlıdır fakat driver, case seti, timestamp, plan ve result identity'si ayrıdır; **main-path E05 ile pool edilmez veya independent replication sayılmaz**. Case IDs campaign-local'dır.
- Campaign-level empty stderr ile per-case child stderr aynı alan değildir.
- Hiçbir driver/target yeniden çalıştırılmadı; decode/decompression historical evidence readback'tir.

Concepts etkisi:
- `TERMS-EARLY-PROBE-EVIDENCE.md` artık **PE01–PE34** ile driver/raw-evidence kullanımlarını taşır.
- `TERMS-LEARNING-GOVERNANCE.md` C6b refinement'iyle **L01–L114**; L105–L114 config guard source-local ayrımlarını ekler, L66'nın oversized/admission sınırını keskinleştirir.
- E04 raw evidence L45–L55'in temel anlamını değiştirmedi.
- E05 raw/source comparison L58–L68 çekirdeğini bozmadı; yeni refinements mixed-purpose exclusion, non-ENOENT refusal, hook-ID exclusion, config precedence, invalid-profile fallback, runner exception/no-objection, truncation/admission, content-insensitive refusal, case-folded selection ve dangling protected symlink ayrımlarını adresler.

Bu closure **C6b raw-evidence slice complete** demektir; whole C6/package closure değildir. E06 NOT VERIFIED/EXCLUDED kalır; E07/E08/E09/E10 kendi evidence kapsamlarında kalır.

## 8. Exact next — master history / current planning / inventory reconciliation

Dört master-history dosyasını **FULL** kapat: METHOD-REVIEW.md, PUBLICATION.md, RESEARCH-LOG.md, SOURCE-LEDGER.md. Ardından current PLAN.md ve QUESTIONS.md ile inventory/STRUCTURE.md, TREE-FRONTIER.tsv, U01-B-DISCOVERY.md, U07-A-FAMILY-MAP.md ve güncel source delta'daki yeni inventory materyalini kendi version scope'uyla ele al.

Bundan sonra fresh source delta manifesti ve U13+ published source-family transferi; bütün linked TERMS için source/role/ID/relation kontrolü; final fresh census gerekir. Yeni source-study technical inquiry yürütülmez.

## 5. Historical next — superseded by §8

**C6b / E04–E05:** ilk dosya **research/studies/ecc/evidence/u05-b-evaluation-probe/probe.cjs**, beklenen mevcut blob **16333fcf9d2bbe208fee061044a997d7aa06e2d3**; ardından **evidence/u06-a-config-probe/probe.cjs**, blob **7d855c5960636925e97da6b2cbffa9c20b673bea**. Bunların plan/README ve L kullanım kayıtlarıyla karşılaştırması yapılacak.

Üç R taşıyıcısı exact-byte read-only recovery ile tam incelenecek: **u05-b-evaluation-probe/results.json.gz**, **u06-a-config-probe/results.json.xz**, **u06-a-conversation-record/original-evidence.tar.xz**. Önce güncel kimlikler ve ilgili recovery açıklamaları alınır; bozuk/erişilemeyen içerik tahminle doldurulmaz. Node E05'in 15 ve Python E05'in 16 vakası kendi geçmişleriyle ayrı tutulur. E01/E02/E03 yeniden koşulmaz; E04/E05 de yeni deney olarak başlatılmaz.

Kalan C6: dört selected master-history, changed PLAN/QUESTIONS, inventory; U13 ve bütün sonraki kaynak delta'sı; şimdi **16 bağlı kullanım dosyası + router** için source/atıf/rol/ID/ilişki ve maddi değişiklik kontrolü; final fresh inventory. Her dosyanın kendi scope'u karşılanmadan paket kapanmaz. B7/B8 başlamadı; ECC sonrası sıra work-management-project-control. Güçlü runtime soruları otomatik Concepts deney borcu değildir.

## 6. Yayın ve doğrulama sınırı

Yeni PE dosyası commit **5c6b303d8669ed050ddcf1f0ac4e40d643516674**, blob **685c5f52cfbc1fa4f0cda4c015d9fcad1d856f01**; 1–60 ve 61–EOF canonical readback ile tamamı görüldü. On yedi ayrı PE kullanım adresi ve vaka/rol/sınır bölümleri kontrol edildi. Yerel tam-byte eşliği, otomatik repository-wide ID/link suite'i veya bağımsız review yapıldığı iddia edilmez.

Bu READING, TERMS router ve global STATE yayını sonrası actual diff ve current readback ayrıca yapılır; gelecekteki kendi hash'i veya yapılmamış kontrol önceden yazılmaz. Kaynak research, C6a manifest/raporu, eski TERMS, Foundation, agent-control ve bağımsız proje çalışmaları korunur. New branch/PR, force update, target execution, model/provider/credential, installation veya release yoktur.

Batu okuma anındaki anlam seçimlerini denetleyemediğinden kaynak ve önemli yorum sınırları izlenebilir kalır. Ortak sözcükler ortak anlamı garanti etmez; kullanıcı onayı, kaynak kullanımı ve extractor yorumu teknik doğrulama bakımından ayrı tutulur. Bu turun kontrolü kaynak-kayıt karşılaştırması ve yayın tutarlılığıdır, bağımsız deney doğrulaması değildir.
