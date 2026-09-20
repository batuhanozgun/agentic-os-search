# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-20 · **B6-T17-C5a / U10-A–U10-B TRANSFER-COMPLETE / C5-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya Concepts okuma ve devam durumudur. [TERMS.md](TERMS.md) kullanım girişidir; [global STATE](../../STATE.md) programın güncel işini taşır. ECC source-study kendi açısından ACTIVE/PARTIAL, U12-C / plan 0.29'a kadar yayımlanmış ve U13-A/Q07d1 NOT STARTED durumundadır. Concepts, source-study'nin next araştırmasını başlatmaz.

## 1. Kaynak kimliği ve korunmuş geçmiş

- Research repository: batuhanozgun/agentic-os-search.
- C5a giriş main/snapshot: **753a4c6696740664d359a293ee8d300a45ade6d8**.
- Kaynak paket: research/studies/ecc/.
- Bu snapshot'ın ECC package tree kimliği: **b6df4013a0f8275da82d6f27a2cd354201c5c70b**; bağlı GitHub studies-tree girdisinden alındı.
- Research target: **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**. Research repository snapshot'ı ile upstream pin aynı nesne değildir.
- Yöntem: Concepts v0.3-working; global kapsam S1 ve açık post-S1 delta hesabı korunur.

**C1–C4 ayrıntılı okuma/kapanış kaydı bu dosyanın [değişmez önceki sürümünde](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/studies/ecc/READING.md) korunur** (blob a027c7cb71f06de5355fcb4783f9a0a88d581c0c). O sürüm C5a sırasında 1–110, 111–225, 226–EOF aralıklarıyla tam geri okundu. Tarihsel ayrıntı current-next ile karışmasın diye burada ikinci kez kopyalanmıyor; önceki kaynak listeleri, C1–C4 refinements, evidence istisnaları ve açık işler geçerliliğini korur. C6 package-wide reconciliation bu tarihsel kaydı da tam devralır; yalnız bu özetle kapanmaz.

Önceki inventory hesabı 60 root + 27 notes + 68 evidence + 4 inventory = 159 dosyadır. Bu tur bağımsız, baştan sona yeni bir 159-yaprak census yapılmadı. Yukarıdaki tree kimliği kaynak evrenini, aşağıdaki tablo ise bu turun gerçek sekiz-dosya okumasını bağlar. Dosya sayısı semantik tamlık veya ilerleme yüzdesi değildir.

## 2. Güncel partition ve çıktılar

| Bölüm | Concepts durumu | Kullanım kaydı |
|---|---|---|
| C1 — U01–U02 | Durable-complete, korunur | TERMS-SURFACES-INSTALLATION.md; ECC-S01–S56 |
| C2 — U03–U04 | Durable-complete, korunur | TERMS-WORK-EXECUTION-MEMORY.md; ECC-W01–W89 |
| C3 — U05–U06 | Durable-complete, korunur | TERMS-LEARNING-GOVERNANCE.md; ECC-L01–L104 |
| C4 — U07–U09 | Durable-complete, korunur | TERMS-REVIEW-RUNTIME-OPERATOR.md; ECC-R01–R176 |
| C5a — U10-A/U10-B | Bu tur source-local transfer complete | E01–E50 ve O01–O69; aşağıdaki iki dosya |
| C5b — U11-A–U11-E | Sırada; Concepts aktarımı başlamadı | İlk giriş Note19/U11-A |
| C5c — U12-A/B1/B2/C | Bekliyor | Profiles/OpenCode/Python |
| C6 — package-wide reconciliation | Bekliyor | Kalan history/inventory/evidence, cross-TERMS ve delta |

C5a/b/c yalnız mevcut C5'in yürütme dilimleridir; yeni araştırma programı, kapsam dışlama veya yöntem geçişi değildir. **C5 bütünü ve ECC Concepts paketi tamamlanmadı.**

Yeni dosyalar:
- [TERMS-EVALUATION-REGISTRY.md](TERMS-EVALUATION-REGISTRY.md): 50 adreslenebilir kullanım kaydı.
- [TERMS-OFFLINE-CAPSULES.md](TERMS-OFFLINE-CAPSULES.md): düzeltme sonrası 69 adreslenebilir kullanım kaydı.

Toplam 119 yeni kullanım satırı, 119 bağımsız kavram veya kanıt demek değildir. Parent/cross-reference tekrarları yeni definition sayılmaz. Önceki C1–C4 kullanım dosyaları bu tur değiştirilmedi.

## 3. C5a exact okuma manifesti

Aşağıdaki yollar research/studies/ecc/ tabanına göredir ve §1'deki snapshot'a bağlıdır. FULL bu research dosyasının tamamıdır; içinde atıf yapılan upstream dosyaların bu tur yeniden okunması değildir.

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

Aynı konuşmanın değişmemiş Concepts INDEX/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE ve ECC META/STATE/INDEX okumaları korundu; giriş main önceki kapanışla aynıydı. AGENT yeniden alındı ve aynı router kimliği doğrulandı; R06 canonical tam metni bu tur ayrıca yüklendi. Control dosyaları research korpusuna dahil edilmedi.

## 4. Source-to-record kontrolü ve epistemik roller

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

## 5. Maddi düzeltme ve yayılım kontrolü

İlk Node TERMS yayını O03'te capsule/journal'ı birleştirdi. N18 §2/§4/§5 ve ilk readback bunu ortaya çıkardı. **O03 capsule'a daraltıldı, O69 journal olarak ayrıldı.** İlk yayın ve kısa gerekçe aynı dosyanın §8'inde korunur. O22/O26/O27/O41/O42 kayıtlarının metadata, projection, export ve receipt kapsamları kontrol edildi; bu kayıtların anlamını değiştirmek gerekmedi. Kaynak araştırmaya veya önceki C4 dosyasına müdahale edilmedi.

Correction commit diff'i O03, coverage eşlemesi ve yeni açıklama/O69'u gösterdi. Aynı diff'te O38'in locator'ı N18 §6 identity/freshness'tan N18 §6'ya kısalmıştı; aynı S224 ve aynı bölüm korunur, kullanım metni değişmez. Bu yüzden yalnız tek satır değiştiği veya kusursuz byte-preserving patch yapıldığı iddia edilmez.

R09 evaluation-registry işareti E serisiyle; R10/R11 capsule/static-inspection işaretleri O serisiyle ayrıntılanır. R11, O60'ın helper/public-gate ayrımıyla okunur. Bu çapraz-kayıt yolları ortak tanım kabulü değildir.

## 6. Gerçek yayın ve kontrol sınırı

- Rust TERMS ilk yayın: **153114995173de76a95772ed259eb982336bdbc4**, blob **b51c42d25ab984cbed81b79f02ff51c42be5a011**.
- Node TERMS ilk yayın: **4f002b274c7542c1861c392282e8fbc90195f464**, ilk blob **7ee111b756cab889fcf2567b1b6bfcd21d95e42e**.
- Node capsule/journal düzeltmesi: **3e4005d047b592eea06ed110681b51ccc8cce773**, düzeltilmiş blob **241a78f5fd420d3b8f14cee8bb40ed2deae6ead5**.

Rust TERMS 1–80 görünümünün kesilen kuyruğu 75–EOF ile tamamlandı; Node ilk metni 1–60/61–105/106–EOF olarak tam geri okundu. Düzeltmenin gerçek diff'i de okundu. ID aralıkları ve source-point/relative-path ilişkileri bu görülen kayıtlardan kontrol edildi; otomatik tüm-repo ID/link suite'i veya bağımsız aktör incelemesi yapılmadı. Yardımcı raw indirmesi ConnectionError ile başarısız oldu; bağlı GitHub okumaları/yazmaları sürdü. Yerel tam-byte download/hash-match başarısı iddia edilmez.

Bu dosya ve güncel router/STATE yazımları sonraki checkpoint işlemleridir; kendi gelecekteki commit kimliği veya henüz yapılmamış readback sonucu uydurulmaz. Final current-ref/diff/readback, turun kapanışında kontrol edilir. Bu statik correspondence kontrolü araştırmanın teknik doğruluğunu bağımsız doğrulamaz.

## 7. Exact next ve açık sınır

**B6-T17-C5b / ilk U11-A:** research/studies/ecc/notes/19-NATIVE-REVIEW-CALLER-AND-DECISION-BOUNDARIES.md → evidence/U11-A-SOURCES.md → ROUND-U11-A.md → PUBLICATION-U11-A.md; bağlı E08 kaydı kendi adapted-run kapsamıyla devralınır. Bu tur Note19/E08 içeriği okunmuş veya Concepts'e aktarılmış sayılmadı. Sonra U11-B–E; ardından U12-A/B1/B2/C. Kaynak/sürüm deltası girişte kontrol edilir; U10 sırf yeni tur diye yeniden yapılmaz.

C6 için halen açık: notes19–27'nin C5 aktarımı, U11–U12 ledgers/rounds/receipts ve bağlı evidence; önceki tarihsel READING'deki master-history/inventory/remaining-evidence hesabı; package-wide source-to-TERMS, ID/role ve kaynak delta kontrolü. Daha önce açıklanmış fakat canlı doğrulaması açık Q06d1b/Q06d2b source soruları otomatik yeni Concepts deney borcu değildir.

Her Concepts turunun iki riski sürer: Batu okuma anındaki anlam seçimlerini denetleyemediği için önemli yorum/dayanak/değişiklik görünür olmalıdır; aynı sözcük ortak anlamı garanti etmez ve kullanıcı onayı teknik oracle değildir. Kaynak kullanımı, araştırmacı yorumu ve extractor yorumu birbirinin yerine geçmez. Ortak B7/B8, Foundation/SOUL/Development OS ve source-study U13-A bu checkpoint'in işi değildir.
