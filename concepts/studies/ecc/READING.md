# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-20 · **B6-T17-C5b / U11-A TRANSFER-COMPLETE / C5b-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya Concepts okuma ve devam durumudur. [TERMS.md](TERMS.md) kullanım girişidir; [global STATE](../../STATE.md) programın güncel işini taşır. ECC source-study kendi açısından ACTIVE/PARTIAL, U12-C / plan 0.29'a kadar yayımlanmış ve U13-A/Q07d1 NOT STARTED durumundadır. Concepts, source-study'nin next araştırmasını başlatmaz. §3–6 önceki C5a checkpoint'inin tarihsel kaydıdır; yeni U11-A çalışması §8'de, current-next §7'dedir.

## 1. Kaynak kimliği ve korunmuş geçmiş

- Research repository: batuhanozgun/agentic-os-search.
- C5a giriş main/snapshot: **753a4c6696740664d359a293ee8d300a45ade6d8**.
- C5b/U11-A giriş main/snapshot: **0d9430bb2854f72b9861e37802427cafec4c1e74**.
- Kaynak paket: research/studies/ecc/.
- ECC package tree kimliği: **b6df4013a0f8275da82d6f27a2cd354201c5c70b**. C5a'dan U11-A girişine değişmedi; source ve control bağlamı aynı konuşmanın tam okumalarından korundu.
- Research target: **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**. Research repository snapshot'ı ile upstream pin aynı nesne değildir.
- Yöntem: Concepts v0.3-working; global kapsam S1 ve açık post-S1 delta hesabı korunur.

**C1–C4 ayrıntılı okuma/kapanış kaydı bu dosyanın [değişmez önceki sürümünde](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/studies/ecc/READING.md) korunur** (blob a027c7cb71f06de5355fcb4783f9a0a88d581c0c). O sürüm C5a sırasında 1–110, 111–225, 226–EOF aralıklarıyla tam geri okundu. Tarihsel ayrıntı current-next ile karışmasın diye burada ikinci kez kopyalanmıyor; önceki kaynak listeleri, C1–C4 refinements, evidence istisnaları ve açık işler geçerliliğini korur. C6 package-wide reconciliation bu tarihsel kaydı da tam devralır; yalnız bu özetle kapanmaz.

Önceki inventory hesabı 60 root + 27 notes + 68 evidence + 4 inventory = 159 dosyadır. C5a veya bu U11-A turunda bağımsız, baştan sona yeni bir 159-yaprak census yapılmadı. Tree kimliği kaynak evrenini, aşağıdaki tablolar gerçek unit okumalarını bağlar. Dosya sayısı semantik tamlık veya ilerleme yüzdesi değildir.

## 2. Güncel partition ve çıktılar

| Bölüm | Concepts durumu | Kullanım kaydı |
|---|---|---|
| C1 — U01–U02 | Durable-complete, korunur | TERMS-SURFACES-INSTALLATION.md; ECC-S01–S56 |
| C2 — U03–U04 | Durable-complete, korunur | TERMS-WORK-EXECUTION-MEMORY.md; ECC-W01–W89 |
| C3 — U05–U06 | Durable-complete, korunur | TERMS-LEARNING-GOVERNANCE.md; ECC-L01–L104 |
| C4 — U07–U09 | Durable-complete, korunur | TERMS-REVIEW-RUNTIME-OPERATOR.md; ECC-R01–R176 |
| C5a — U10-A/U10-B | Source-local transfer complete, korunur | E01–E50 ve O01–O69 |
| C5b — U11-A | Source-local transfer complete | TERMS-NATIVE-REVIEW.md; N01–N77 |
| C5b — U11-B–U11-E | Sırada; Concepts aktarımı başlamadı | İlk giriş Note20/U11-B |
| C5c — U12-A/B1/B2/C | Bekliyor | Profiles/OpenCode/Python |
| C6 — package-wide reconciliation | Bekliyor | Kalan history/inventory/evidence, cross-TERMS ve delta |

C5a/b/c yalnız mevcut C5'in yürütme dilimleridir; yeni araştırma programı, kapsam dışlama veya yöntem geçişi değildir. **C5b bütünü, C5 bütünü ve ECC Concepts paketi tamamlanmadı.**

C5 çıktıları:
- [TERMS-EVALUATION-REGISTRY.md](TERMS-EVALUATION-REGISTRY.md): 50 adreslenebilir kullanım kaydı.
- [TERMS-OFFLINE-CAPSULES.md](TERMS-OFFLINE-CAPSULES.md): düzeltme sonrası 69 adreslenebilir kullanım kaydı.
- [TERMS-NATIVE-REVIEW.md](TERMS-NATIVE-REVIEW.md): 77 adreslenebilir kullanım kaydı; bu turun yeni dosyası.

C5a'nın 119 ve U11-A'nın 77 kullanım satırı bağımsız kavram veya kanıt sayısı değildir. Parent/cross-reference tekrarları yeni definition sayılmaz. Önceki C1–C4 ve C5a kullanım dosyaları U11-A turunda değiştirilmedi.

## 3. C5a exact okuma manifesti

Aşağıdaki yollar research/studies/ecc/ tabanına göredir ve C5a snapshot'ına bağlıdır. FULL bu research dosyasının tamamıdır; içinde atıf yapılan upstream dosyaların yeniden okunması değildir.

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| notes/17-RUST-EVALUATION-REGISTRY-AND-USE.md | f7b0101fa995e136e07a42515e4c47900fae3aea | FULL; 1–85 + 86–EOF |
| evidence/U10-A-SOURCES.md | 1196baf186518d978222585e97feac38eac196bb | FULL |
| ROUND-U10-A.md | bef1db911120e428f5f9037952fd6d43deaa5af9 | FULL |
| PUBLICATION-U10-A.md | 165a7cfd6078224b0ad65e724999c58974205319 | FULL |
| notes/18-OFFLINE-CAPSULES-REPLAY-AND-RECEIPT-SCOPE.md | d0372662e450a2021e637c5b11bd461f2a3e283f | FULL; 1–80 + 81–EOF |
| evidence/U10-B-SOURCES.md | 5e3d6a06eea2989c40b641f0153341c63ee7640c | FULL |
| ROUND-U10-B.md | 9f762ee370604778572593de0a27f089f3b18973 | FULL |
| PUBLICATION-U10-B.md | b3e69fec21917f42c1b9d47ff140d3758bd17a03 | FULL |

Aynı konuşmanın değişmemiş Concepts INDEX/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE ve ECC META/STATE/INDEX okumaları korundu; C5a giriş main önceki kapanışla aynıydı. AGENT yeniden alındı ve aynı router kimliği doğrulandı; R06 canonical tam metni C5a'da ayrıca yüklendi. Control dosyaları research korpusuna dahil edilmedi.

## 4. C5a source-to-record kontrolü ve epistemik roller

Her yeni kullanım satırı research note'un bölümüne ve gerektiğinde ledger kaynak kimliğine bağlandı. K/B/Y/T/P anahtarları hedef koddan raporlanmış kullanım, hedef belge beyanı, araştırmacı yorumu, incelenmiş test tasarımı ve yorumlanacak procedure'ü ayırır. Türkçe açıklamalar extractor paraphrase'idir; hedefin doğrudan alıntısı veya bağımsız doğrulama değildir.

N17'nin §1–11 ve N18'in §1–10 kapsamı yeni dosyaların source-side coverage bölümlerinden kullanım satırlarına geri eşlendi. Ledger/round/publication içerikleri atıf, kanıt sınıfı ve tarihsel yayın standing'ini kontrol eder; aynı mekanizmaya dört bağımsız destek sayılmaz. Upstream test, örnek, Rust/Node/SQLite kodu veya model/provider çalıştırılmadı; yeni E08 yoktur. E04/E07 ve iki E05 geçmişi kendi scope'larını, E06 NOT VERIFIED/EXCLUDED durumunu korur.

Maddi ayrımlar:
- Rust registry'nin expected-baseline koşulu ve transaction'ı, U09 session-state writer'larından farklıdır; önceki eleştiri otomatik taşınmadı.
- Candidate hash referans dizgelerini bağlar; referent truth/freshness doğrulanmış değildir.
- Distinct seed keys independent trials, saved policy preregistration değildir.
- Health callback ve snapshot aynı supplied health map'inden gelebilir; correspondence bağımsız health ölçümü değildir.
- Registry promotion/reversal, çalışan harness'ın rollout/rollback'i değildir.
- Standalone hash-chain geçerliliği tam tarih kanıtı değildir; retained receipt belirli checkpoint beklentisini ekler.
- Replay response'u tekrar verir; önceki effect/environment'ı geri kurmaz.
- Receipt generic ok sonucu yalnız gerçekten istenmiş optional witness kontrolleriyle yorumlanır.
- Disabled untrusted candidate gate, trusted record-mode implementation'ın çalışmadığı anlamına gelmez.
- Report-only counts, task outcome veya promotion sinyali değildir.

## 5. C5a maddi düzeltme ve yayılım kontrolü

İlk Node TERMS yayını O03'te capsule/journal'ı birleştirdi. N18 §2/§4/§5 ve ilk readback bunu ortaya çıkardı. **O03 capsule'a daraltıldı, O69 journal olarak ayrıldı.** İlk yayın ve kısa gerekçe aynı dosyanın §8'inde korunur. O22/O26/O27/O41/O42 kayıtlarının metadata, projection, export ve receipt kapsamları kontrol edildi; bu kayıtların anlamını değiştirmek gerekmedi. Kaynak araştırmaya veya önceki C4 dosyasına müdahale edilmedi.

Correction commit diff'i O03, coverage eşlemesi ve yeni açıklama/O69'u gösterdi. Aynı diff'te O38'in locator'ı N18 §6 identity/freshness'tan N18 §6'ya kısalmıştı; aynı S224 ve aynı bölüm korunur, kullanım metni değişmez. Bu yüzden yalnız tek satır değiştiği veya kusursuz byte-preserving patch yapıldığı iddia edilmez.

R09 evaluation-registry işareti E serisiyle; R10/R11 capsule/static-inspection işaretleri O serisiyle ayrıntılanır. R11, O60'ın helper/public-gate ayrımıyla okunur. Bu çapraz-kayıt yolları ortak tanım kabulü değildir.

## 6. C5a gerçek yayın ve kontrol sınırı

- Rust TERMS ilk yayın: **153114995173de76a95772ed259eb982336bdbc4**, blob **b51c42d25ab984cbed81b79f02ff51c42be5a011**.
- Node TERMS ilk yayın: **4f002b274c7542c1861c392282e8fbc90195f464**, ilk blob **7ee111b756cab889fcf2567b1b6bfcd21d95e42e**.
- Node capsule/journal düzeltmesi: **3e4005d047b592eea06ed110681b51ccc8cce773**, düzeltilmiş blob **241a78f5fd420d3b8f14cee8bb40ed2deae6ead5**.
- C5a local READING: **be6f1bb3bf4d4719057c7460a96ee15a77f249e6**; TERMS router: **4207f22ea393af9d620f79d95fbe00c90f507d70**; global closure: **0d9430bb2854f72b9861e37802427cafec4c1e74**.

Rust TERMS 1–80 görünümünün kesilen kuyruğu 75–EOF ile tamamlandı; Node ilk metni 1–60/61–105/106–EOF olarak tam geri okundu. Düzeltmenin gerçek diff'i de okundu. ID aralıkları ve source-point/relative-path ilişkileri bu görülen kayıtlardan kontrol edildi; otomatik tüm-repo ID/link suite'i veya bağımsız aktör incelemesi yapılmadı. C5a'daki yardımcı raw indirmesi ConnectionError ile başarısız oldu; bağlı GitHub okumaları/yazmaları sürdü. O tur için yerel tam-byte download/hash-match başarısı iddia edilmez.

C5a final current-ref/diff/readback kontrolü 0d9430b kapanışında tamamlandı. Tarihsel kendi-gelecek-commit/readback uyarıları pending repair değildir. Bu statik correspondence kontrolü araştırmanın teknik doğruluğunu bağımsız doğrulamaz.

## 7. Exact next ve açık sınır

**B6-T17-C5b / sıradaki U11-B:** research/studies/ecc/notes/20-SCHEDULED-WORK-ADMISSION-AND-RETRY.md → evidence/U11-B-SOURCES.md → ROUND-U11-B.md → PUBLICATION-U11-B.md; bağlı evidence gerçek kapsamıyla devralınır. U11-A ve E08 aktarımı §8'de kapandı; tekrar yapılacak iş değildir. U11-B'nin gövde okuması bu tur yapılmadı. Sonra U11-C–E; ardından U12-A/B1/B2/C. Kaynak/sürüm deltası girişte kontrol edilir; önceki completed birimler sırf yeni tur diye yeniden yapılmaz.

C6 için halen açık: notes20–27'nin C5 aktarımı, U11-B–U12 ledgers/rounds/receipts ve bağlı evidence; önceki tarihsel READING'deki master-history/inventory/remaining-evidence hesabı; package-wide source-to-TERMS, ID/role ve kaynak delta kontrolü. Daha önce açıklanmış fakat canlı doğrulaması açık Q06d1b/Q06d2b/Q04h2 soruları otomatik yeni Concepts deney borcu değildir.

Her Concepts turunun iki riski sürer: Batu okuma anındaki anlam seçimlerini denetleyemediği için önemli yorum/dayanak/değişiklik görünür olmalıdır; aynı sözcük ortak anlamı garanti etmez ve kullanıcı onayı teknik oracle değildir. Kaynak kullanımı, araştırmacı yorumu ve extractor yorumu birbirinin yerine geçmez. Ortak B7/B8, Foundation/SOUL/Development OS ve source-study U13-A bu checkpoint'in işi değildir.

## 8. C5b/U11-A gerçek okuma, aktarım ve doğrulama

### 8.1 Giriş ve exact manifest

Giriş main 0d9430bb2854f72b9861e37802427cafec4c1e74, önceki kapanışla compare-identical bulundu. AGENT fresh okundu, aea3dd845e0f0bbcfb34465edb23782e99f95c80 kimliği değişmedi. Aynı konuşmada tam okunmuş R01–R09 ve Concepts/current ECC girişleri korundu. Bu preflight yeni oturum deneyi veya bağımsız review değildir.

Aşağıdaki 11 mevcut dosya research/studies/ecc/ altında ve bu giriş snapshot'ına bağlıdır. E08 dizini ayrıca listelendi; yedi girdisi aşağıdaki yedi evidence dosyasıyla eşleşti. Bu yalnız U11-A kapsam hesabıdır, yeni whole-package census değildir.

| Yol | Git blob | Gerçek okuma / temsil |
|---|---|---|
| notes/19-NATIVE-REVIEW-CALLER-AND-DECISION-BOUNDARIES.md | 5e9f7a923896a377882e7cb5fb0857fb3804b8cf | FULL; 1–85 ve 86–EOF |
| evidence/U11-A-SOURCES.md | 0cff0640065f6343131f361645659d996f90d77c | FULL |
| ROUND-U11-A.md | 316ab5f0e07575b35bcb7ff81dce0b990c871340 | FULL |
| PUBLICATION-U11-A.md | cba526815e9d9f8803da50a9349fceda89f43957 | FULL |
| evidence/u11-a-review-flow-probe/README.md | 2edb53a5c12ddbc03f5671bead55cb3cde82dce0 | FULL |
| evidence/u11-a-review-flow-probe/PRECHECK.md | 42f3365fc14a8b8f83312352ab0039a43c9ca9f1 | FULL; tarihsel prerecord |
| evidence/u11-a-review-flow-probe/probe.cjs | 289e2159c9ab5864bbaa8955e5eb95be3ff7ca89 | FULL; yürütülmedi |
| evidence/u11-a-review-flow-probe/raw-results.part01.b64 | 3e05fe64c308251ae824fa88ab9ac794c1cdbd3a | Tam encoded baytlar; decoded kayıtta okundu |
| evidence/u11-a-review-flow-probe/raw-results.part02.b64 | 88dd6c75a077453618e5b221594c93dd50ed6767 | Tam encoded baytlar; decoded kayıtta okundu |
| evidence/u11-a-review-flow-probe/raw-results.part03.b64 | faf7d1aae3788cd482a3d71e81db2116322bd4be | Tam encoded baytlar; decoded kayıtta okundu |
| evidence/u11-a-review-flow-probe/raw-results.part04.b64 | e9b8056c749104c1cc173134fed66ba2f9281588 | Tam encoded baytlar; decoded kayıtta okundu |

### 8.2 E08 recovery ve kanıt sınırı

Connector'dan alınan dört text parçası yerelde aktarıldı; 1515/1515/1515/1394 bayt ve dört Git blob değeri tam eşleşti. Doğrulanmış parçalar birlikte çözüldü: **101725 bayt**, SHA-256 **45d8c8f409d51d0c7e01dd63168b833dffd86a9ced844deb700472bba4874f9e**. Parse edilen JSON'un run/schema_check alanları, 18 scenario'nun girdileri, response/error/log/outcome'ları okundu. Tekrarlanan 8 farklı prompt, 2 farklı schema, 6 farklı schema-hariç options temsili ayrı gösterilip bütün scenario-call bağlantılarıyla eşlendi. Kapsam dışına gizlice alan atılmadı; aynı metnin kopyaları bağımsız destek sayılmadı.

İlk uzun yerel gösterimin başlangıcı kesildi; metadata, ilk üç scenario ve schema-check kaydı daha küçük çıktılarla tamamlandı. Saklanmış 38 non-null yanıtın Draft7 doğrulaması read-only tekrarlandı: 38 valid, 0 schema error. Bu yalnız schema/data correspondence kontrolüdür; native host schema dialect'i, model doğruluğu veya merged-record geçerliliği değildir. Target workflow, probe.cjs veya fake agent/parallel yeniden çalıştırılmadı; yeni E08 koşusu yok.

N19'un order-sensitive proof-loss sonucu, pozitif/negatif kontrolleri ve düşük güvenli confirmed ayrımı ham kayıtla tutarlı bulundu. Prosedür/host beyanları ham fixture sonucu diye sunulmadı. E08 tek tarihsel adapted run, 18 controlled case; 18 bağımsız trial veya live benchmark değildir. E04/E07 ve iki E05 ayrı, E06 excluded kalır. Dated host/gh kayıtları güncel dış olgu olarak yeniden sertifikalanmadı.

### 8.3 Kullanım, yorum ve kaynak kontrolü

Yeni dosya TERMS-NATIVE-REVIEW.md, **ECC-N01–N77** kullanımlarını note bölümü/source role ile bağlar. N19 §1–9 ve ledger/round/receipt ile kaynak tarafından kontrol aynı dosyanın §9'undadır. Research author'ın kod açıklaması, hedef prosedürü, tarihli host beyanı, doğrudan decoded record ve yeni extractor paraphrase'i ayrıldı.

Korunan başlıca ayrımlar: interpreted procedure / executable review / host; safe arguments / exact repo-revision; selected / required coverage; first finding / merged severity and proof; reviewer verdict / aggregate verdict / human consent; blocking decision / reporting certainty; source discovery / packed delivery; adapted fixture / native execution.

İlk kayıt kontrolünde N21'in trigger/dimension ve N32'nin dimension/dimensions birleşik ID'leri ayrıldı: N21 yalnız seçim kuralı, N76 seçilen eksen; N32 ilk kaynak alanı, N77 kaynak eksenleri listesi. N25'in proof alanı koşullu zorunlu diye netleştirildi, N28 zaten aynı koşulu taşıyordu. Kaynak, C4 veya C5a TERMS değiştirilmedi. İlk metin, gerekçe ve etkilenen kullanım kontrolü TERMS §10'da korunur. R16'nın genel durdurucu standing'i typed blocking dizisi sayılmaz; N23/N48–N51 ve TERMS router bunu açıklar.

### 8.4 Gerçek yayın checkpoint'i

- İlk TERMS-NATIVE-REVIEW: **091d7c932da64c474b678dbe249e5785a8bbb520**, blob **94e39e504559ca2870f6cd38368601e160963968**; 1–65/66–120/121–EOF tam readback.
- Kayıt ayrımı: **e7ce902c5e550be524ddd0bbc87c1dc5968edf8c**, blob **5ddaf013edca63626d330a3dbdd754b8c6de20a8**. Tam correction diff'i okundu: N21/N25/N32, coverage, düzeltme izi/N76/N77 ve 75→77 sayısı; başka satır değişimi yok.
- Giriş0d9430b→e7ce902 karşılaştırması iki commit/yalnız yeni TERMS dosyası gösterdi. Source-study, control, Foundation ve önceki Concepts kaynakları değişmedi.

Bu READING, router ve global STATE yazıları sonraki yayın adımlarıdır; final diff/ref/readback kontrolü kapanışta yapılır. Sayım/adresleme ve aynı-assistant source-to-record kontrolü bağımsız semantik doğrulama değildir; bütün repo için otomatik ID/link suite'i koşulmadı. C5b-U11-A aktarımı kapanır, fakat C5b'nin U11-B–E bölümü, C5c, C6 ve B7/B8 açık kalır.
