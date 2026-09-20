# Concepts — Güncel çalışma durumu

2026-09-20 · **B6-T17-C5b / U11-B tamamlandı; sıradaki iş ECC U11-C**.

Bu dosya global current-purpose/authorization/next-work yüzeyidir. Ayrıntılı ECC okuma durumu [yerel READING](studies/ecc/READING.md), kullanım kayıtları [TERMS](studies/ecc/TERMS.md) içindedir. Source-study STATE'leri Concepts next-work authority değildir.

## 1. Amaç ve güncel aşama

**PILOTS/B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / ECC-C1–C4-DURABLE-COMPLETE / ECC-C5a-U10-DURABLE-COMPLETE / ECC-U11-A-B-DURABLE-COMPLETE / ECC-C5b-PARTIAL / ECC-C5-PARTIAL / ECC-PACKAGE-PARTIAL / METHOD-v0.3-WORKING / B7-B8-NOT-STARTED.**

İlk aşama research/studies araştırmalarını kendi bağlamlarında tam okuyup kullanım/ilişkilerini çıkarmaktır. Bütün ilgili çıkarımlar ve kapsam/delta hesabı bitmeden ortak terim değerlendirmesine geçilmez. Bu iş genel sözlük araştırması, source-study'nin yeni teknik deneyleri, Foundation doğrusu veya SOUL/Development OS mimari kararı değildir.

Yeni oturum girişi değişmedi: AGENT ve tetiklenen protokoller → [INDEX](INDEX.md)'in STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE tam okuma yolu → etkin paketin READING/TERMS → gereken kaynak derinliği. Aynı konuşmada tam ve değişmemiş kaynaklar mekanik tekrar edilmez. Eski reset/pilot hazırlık kayıtları current-next sayılmaz.

## 2. Program ve paketlerin durumu

| İş | Güncel durum |
|---|---|
| CMH, Superpowers, AI Knowledge Strategies | Concepts durable-complete; korunur |
| Multi-Agent Patterns, Anthropic AI-Native SDLC, gstack | Concepts durable-complete; korunur |
| Hermes Agent Concepts | H1–H5 durable-complete / package-complete; korunur |
| Hermes source-study | ACTIVE PARTIAL; Q60 NOT RESEARCHED; Concepts bunu araştırmaz |
| ECC Concepts C1–C4 | U01–U09 durable-complete; korunur |
| ECC Concepts C5a | U10-A/U10-B bağlamlı aktarım tamamlandı; korunur |
| ECC Concepts C5b / U11-A | Native review/caller/outer decision + E08 aktarımı tamamlandı; korunur |
| ECC Concepts C5b / U11-B | Scheduled-work/admission/retry aktarımı tamamlandı |
| ECC Concepts C5b / U11-C–E | Sırada; ilk exact next U11-C |
| ECC Concepts C5c | U12-A/B1/B2/C bekliyor |
| ECC Concepts C6 | Package-wide reconciliation/final closure bekliyor |
| ECC source-study | ACTIVE/PARTIAL; U12-C / plan 0.29'a kadar yayımlanmış; U13-A/Q07d1 NOT STARTED |
| S1 sonrası additions | agentmemory, claude-swap, cli-continues, ponytail B7 öncesi scope hesabına alınacak |
| B7/B8 | Başlamadı |

C5a/b/c, mevcut C5'in kaynak-ailelerine göre yürütme dilimleridir. Yeni phase, kaynak dışlama veya sabit tur sayısı kararı değildir. U11-A–B'nin kapanması C5b'nin tamamı değildir. Paket sayıları ilerleme yüzdesi sayılmaz; post-S1 kapsam hâlâ reconcile edilmemiştir.

## 3. Korunmuş C5a / U10 sonucu

C5a giriş main: **753a4c6696740664d359a293ee8d300a45ade6d8**. ECC source package tree: **b6df4013a0f8275da82d6f27a2cd354201c5c70b**. Araştırma upstream pin'i **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a** olarak korundu.

C5a'da tam okunan sekiz research dosyası: Note17, U10-A source ledger, ROUND-U10-A, PUBLICATION-U10-A; Note18, U10-B source ledger, ROUND-U10-B, PUBLICATION-U10-B. Exact path/blob/read-range manifesti yerel READING'dedir. Bu okumalar upstream kod/test/SDK'nin o tur yeniden okunması veya çalıştırılması değildir.

İki kalıcı çıktı:
- [TERMS-EVALUATION-REGISTRY.md](studies/ecc/TERMS-EVALUATION-REGISTRY.md): **ECC-E01–E50**, 50 kullanım satırı.
- [TERMS-OFFLINE-CAPSULES.md](studies/ecc/TERMS-OFFLINE-CAPSULES.md): **ECC-O01–O69**, 69 kullanım satırı.

Toplam 119 source-local adreslenebilir kullanım satırı vardır; bağımsız kavram/kanıt sayısı değildir. Kaynak notunun bölümüne ve ledger kimliğine atıf, söyleyen/ifade rolü ve açıklamanın sınırı her kayıtta korunur. Kaynak tarafından bölüm-kayıt eşlemesi iki dosyada ayrı bulunur.

Önemli anlam sınırları:
- Rust registry'nin conditional pointer update/transaction kontrolü, önceki session-state writer'ına eşitlenmedi.
- Promotion/rollback burada registry seçimi/geri alma olabilir; runtime rollout ve gerçek yarar ayrı sorulardır.
- Distinct seed labels bağımsız deneme, saved criteria preregistration değildir.
- Health snapshot ile callback aynı assertion'a dayanabilir; integrity/correspondence bağımsız sağlık ölçümü değildir.
- Capsule bütünlüğü, tarihin eksiksizliği veya kayıtlı görevin başarısı değildir.
- Replay yanıtı korur; önceki environment/effect'i kendiliğinden geri kurmaz.
- Receipt generic ok sonucu artifact/signature/gate kontrollerinin hangilerinin gerçekten istendiğiyle sınırlıdır.
- Disabled candidate gate, trusted record-mode tool implementation'ının çalışmadığı anlamına gelmez.

**C5a extractor düzeltmesi:** İlk O03 capsule/journal'ı birleştirdi. Source-side/readback kontrolü sonrasında O03 yalnız capsule, O69 journal olarak ayrıldı. İlk sürüm, gerekçe ve O22/O26/O27/O41/O42 etki kontrolü Node TERMS §8'de kayıtlıdır. Önceki C4 source/use kayıtları veya araştırma bulguları bu nedenle yeniden yazılmadı. R10/R11 için ayrıntılı capsule/static-inspection karşılığı O serisine bağlandı; ortak tanım ilan edilmedi.

## 3A. Korunmuş C5b / U11-A sonucu

Bu bölüm U11-A turunun tarihsel sonucudur; current-next §4, yeni U11-B sonucu §3B'dedir.

Giriş main **0d9430bb2854f72b9861e37802427cafec4c1e74**, önceki kapanışla aynı bulundu. Fresh AGENT kimliği değişmedi; aynı konuşmadaki tam protokol ve proje girişleri korundu. Source-study ve control değişikliği olmadan mevcut yetkili Concepts işine devam edildi.

**11 kaynak dosyası:** Note19, U11-A-SOURCES, ROUND-U11-A, PUBLICATION-U11-A; E08'in README/PRECHECK/probe ve dört encoded raw parçası. İlk yedi metin tam okundu; dört parça exact-byte/hash kontrolüyle birlikte decode edilip içerikleri okundu. Yerel READING §8 bütün path/blob/temsil ve verification kapsamını taşır.

E08 verisi **101725 bayt**, SHA-256 **45d8c8f409d51d0c7e01dd63168b833dffd86a9ced844deb700472bba4874f9e** olarak geri kazanıldı. Metadata, 18 senaryonun girdileri/replies/errors/logs/outcomes, tekrarlar ayrıştırılarak 8 farklı prompt, 2 farklı schema ve 6 farklı call-options görünümü okundu. Saklanmış 38 non-null yanıtın Draft7 kontrolü tekrarlandı ve hepsi şemaya uydu. **Target workflow veya E08 probe yeniden çalıştırılmadı.** Bu recovery/schema kontrolü native host veya model doğrulaması değildir; 18 senaryo tek tarihsel adapted run kapsamındadır.

Yeni çıktı [TERMS-NATIVE-REVIEW.md](studies/ecc/TERMS-NATIVE-REVIEW.md): **ECC-N01–N77**, 77 bağlamlı kullanım kaydı. Kaynak notunun §1–9 kapsamı, ledger, prosedür/host atıfları ve raw evidence role'leri kayıtlarla eşlendi. Geçmiş yayın hataları target-experiment failure sayılmadı.

Önemli ayrımlar:
- Interpreted pipeline procedure, native review segment ve external host aynı nesne değildir.
- Safe PR argument, repository/revision binding değildir.
- Selected-dimension completion, gerekli bütün review kapsamının tamamlanması değildir.
- Merged severity'nin korunması güçlü proof/title/location'ın korunduğu anlamına gelmez.
- Reviewer verdict, aggregate APPROVE ve insan commit onayı ayrı kullanımlardır.
- Low-confidence true blocking kalabilir ama confirmed sayılabilir; sayaç güçlü epistemik doğrulama diye çevrilmez.
- failedDimensions ile blocking finding array'i ayrıdır; unverified false/0 placeholder kesin refutation değildir.
- Source discovery, packed delivery ve installed/native-host conformance birbirine yükseltilmedi.

**Bu turun extractor düzeltmesi:** N21 trigger/dimension ve N32 dimension/dimensions ilk metinde tek ID altında açıklanıyordu. Ayrı adreslenmeleri için N21 trigger, N76 security dimension; N32 tekil dimension, N77 dimensions listesi yapıldı. N25'te proof'un koşullu zorunluluğu netleştirildi. İlk sürüm, gerekçe ve etki kontrolü TERMS §10'da korunur. Source-study veya önceki C4/C5a kullanım dosyaları değiştirilmedi. R16'nın genel durdurucu standing'i typed blocking dizisi sayılmasın diye yeni TERMS router ve N23/N48–N51 ayrımı gösterir.

Bu source-local aktarım Q04h2'yi, native model kalitesini, gerçek PR/consent veya canlı commit/recovery davranışını araştırmış sayılmaz. U11-B gövdesi o tur okunmadı; C5b'nin kalanı tamamlanmış sayılmadı.

## 3B. Bu turun gerçek sonucu — C5b / U11-B

Giriş main **04213d5be3d7655fcd55ee20d9f60be3cd44a8c5**, önceki kapanışla compare-identical. AGENT ve gerekli canonical protokol içerikleri geri kazanıldı; Concepts INDEX yeniden tam okundu. Aynı konuşmanın tam/değişmemiş amaç, yöntem, current-state ve kaynak bağlamı korundu. Yeni phase veya source-study araştırması başlatılmadı.

**Dört research dosyası tam okundu:** Note20, U11-B-SOURCES, ROUND-U11-B ve PUBLICATION-U11-B. Exact path/blob/okuma aralıkları yerel READING §9'da. Upstream Rust/cron/testler yeniden okunmadı veya çalıştırılmadı; eski deneyler scheduling kanıtına çevrilmedi.

Yeni çıktı [TERMS-SCHEDULED-WORK.md](studies/ecc/TERMS-SCHEDULED-WORK.md): **ECC-SC01–SC61**, 61 bağlamlı kullanım/ilişki kaydı. Kaynak notunun §1–10 kapsamı kayıtlara eşlendi; code-report, araştırmacı yorumu, inspected test ve tarihli dependency contract rolleri K/Y/T/H olarak ayrıldı. Bu sayı bağımsız kavram, deney veya ilerleme yüzdesi değildir.

Önemli ayrımlar:
- Recurring instruction, due occurrence, session, wrapper ve completed/accepted task aynı kimlik değildir.
- last_run_at, admission sonrasında kaydedilen **captured pass time**; gerçek process start veya completion zamanı değildir.
- Daemon max_parallel_sessions bu yolda batch limit'tir; live-work kapasitesinden düşen reservation veya per-schedule non-overlap değildir.
- Pending worktree admission'ı schedule'ı ilerletebilir; queue'da kalmak running/readiness değildir.
- Admission ve schedule advancement ayrı etkiler olduğundan error, önceki etkilerin rollback edildiğini göstermez.
- Finite schedule'da son occurrence admit edildikten sonra no-future hatasıyla eski due kaydın korunması koşullu source counterexample'dır; yeni gözlenmiş duplicate olay değildir.
- Schedule removal sonraki fresh selection'ı etkiler; önceden seçilmiş/admitted work'ün revocation'ı değildir.
- Returned schedule/session association, durable occurrence/result provenance değildir.

**Extractor açıklığı:** SC47 finite schedule ile terminal handling'i ilk metinde tek adreste taşıyordu; SC47 nesneye daraltıldı, SC61 işlem/durum-geçişi sorusu olarak eklendi. SC02'de due olmanın gerçekleşmiş execution olmadığı netleştirildi. İlk sürüm, gerekçe ve SC17/SC19–SC24/SC37/SC42/SC48 etki kontrolü yeni TERMS §8'de korunur. Önceki kullanım dosyaları veya source-study değiştirilmedi.

Source-study'nin invalid/no-future creation reddi, explicit profile doğrulaması, Pending queue retention, successful advancement, fresh-selection removal ve daemon error reporting kontrolleri de korundu. U10 registry transaction'ı veya U09 stale-attempt bulgusu bu başka yola taşınmadı. Q04e1b'nin daha güçlü runtime, concurrency, terminal handling, cancellation/fairness ve accepted-result soruları açık kalır. U11-C içeriği bu tur okunmadı.

## 4. Exact next — C5b / U11-C

İlk dosya: **research/studies/ecc/notes/21-REMOTE-INTAKE-DISPATCH-AND-RESULT-BOUNDARIES.md**.

Ardından U11-C-SOURCES, ROUND-U11-C, PUBLICATION-U11-C ve ilişkili evidence gerçek source-study kapsamıyla devralınır. Amaç mevcut araştırmanın remote request, intake/authentication, hedef bağlama, kalıcı request status, targeted/new-session dispatch ve result/failure/retry kullanımlarını çıkarmaktır. Canlı endpoint kurmak, dış talepler göndermek veya source research'ünü sürdürmek değildir.

U11-D backlog coordination ve U11-E template/launch composition aynı C5b hattında sonraki işlerdir. U12 profiles/OpenCode/Python C5c'dir. Kaynak/sürüm değişiklikleri girişte kontrol edilir; yalnız özet veya önceki verdict yeni kaynak okumasının yerine geçmez. U10 ve U11-A–B sırf yeni tur diye tekrar yapılmaz.

C5 tamamlandıktan sonra C6; kalan root history/inventory/evidence hesapları, bütün ECC TERMS, kaynak değişimleri ve nihai package coverage kontrolünü yapar. ECC'den sonraki paket work-management-project-control'dür; SCOPE sırası korunur. B7 tamamlanmadan B8 ortak referans başlamaz.

## 5. İki risk ve yetki sınırı

Batu okuma anındaki anlam seçimlerini denetleyemiyor; bu nedenle önemli yorum, dayanak, belirsizlik ve değişiklik denetlenebilir kayıtta görünür olmalıdır. Aynı sözcük ortak anlamı garanti etmez: kaynak kullanımı, eski araştırmacı yorumu, extractor yorumu ve kullanıcı onayı ayrı tutulur; kullanıcı teknik uzman oracle değildir. Bu turun somut karşılığı run/admission/occurrence/time alanlarının ayrılması, sonlu schedule ile terminal handling'in ayrı adreslenmesi ve koşullu failure örneklerinin gözlenmiş olaya yükseltilmemesidir. C5a ve U11-A düzeltmeleri kendi tarihlerinde korunur.

Kaynakta açıklanmayan etiket genel bilgiyle doldurulmaz; kaynakta açık ayrımın atlanması da belirsizlik bahanesiyle kapatılmaz. Q06d1b/Q06d2b/Q04h2/Q04e1b gibi daha güçlü doğrulama soruları araştırılmış sayılmaz ve otomatik yeni Concepts deney borcu değildir. E04/E07 ve iki E05 geçmişi korunur, E06 NOT VERIFIED/EXCLUDED kalır. Yeni fixture, upstream test, model/provider, installation, DB/runtime, canlı schedule/endpoint, release veya upstream mutation yapılmadı. Önceki E08 read-only recovery/schema kontrolü de bu tur yeniden yapılmadı.

Yazma kapsamı yalnız ilgili Concepts kullanım/READING/TERMS/global STATE dosyalarıdır. Agent-control, Foundation, studies source packages, CATALOG, diğer Concepts paketleri, explorations ve publications bu işin mutation scope'u değildir.

## 6. Korunmuş devam geçmişi ve yayın kanıtı

Önceki uzun Hermes H1–H5/C4 kapanış anlatıları ve bütün commit listeleri [753a4c6 checkpoint'indeki önceki STATE'in tam içeriğinde](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/STATE.md) korunur (blob 0a9d147c5c8a206964ea99e5e199d76e211b0a98). Güncel dosyada current authority ve gerektiğinde geri dönüş yolu tutulur; tarihsel içeriğin artık current-next olmadığı açıktır. Eski package-local kullanım kayıtları yerinde kalır. ECC C1–C4 ayrıntılı READING kaydının değişmez bağlantısı yerel READING'dedir; C6 bunu tam recover eder.

Korunan C5a checkpoints:
- Rust TERMS: **153114995173de76a95772ed259eb982336bdbc4**.
- Node TERMS ilk yayın: **4f002b274c7542c1861c392282e8fbc90195f464**.
- Capsule/journal düzeltmesi: **3e4005d047b592eea06ed110681b51ccc8cce773**.
- Yerel READING: **be6f1bb3bf4d4719057c7460a96ee15a77f249e6**.
- TERMS router: **4207f22ea393af9d620f79d95fbe00c90f507d70**.
- C5a global closure/readback: **0d9430bb2854f72b9861e37802427cafec4c1e74**.

U11-A gerçek checkpoints:
- Yeni native-review TERMS: **091d7c932da64c474b678dbe249e5785a8bbb520**.
- Kayıt ayrımı: **e7ce902c5e550be524ddd0bbc87c1dc5968edf8c**, blob **5ddaf013edca63626d330a3dbdd754b8c6de20a8**.
- Yerel READING: **d42f804c66ae299b1bc4a80dca4dc2119f26cc2a**.
- TERMS router: **44919a99e7b2754f7f04d3f6ee97f2788757b378**.
- Global closure ve final main/readback: **04213d5be3d7655fcd55ee20d9f60be3cd44a8c5**.

U11-A TERMS ilk metni tam source aralıklarıyla geri okundu; düzeltmenin tam actual diff'i yalnız N21/N25/N32, source mapping, açıklama/N76/N77 ve sayım değişikliğini gösterdi. Bu tarihsel kontroller yeni U11-B davranış kanıtı değildir.

U11-B gerçek checkpoints:
- Yeni scheduled-work TERMS: **a07d95af0af34858055cec2f118ecf4940b8214f**.
- Finite/terminal ayrımı: **91236352f1d7171cff13a09c33b78a886d202748**, blob **eeba5fbb887a83e1faf7d8609cfdb4926e2fc7cf**.
- Yerel READING: **c1fbc7e20de498437b04d0dd9ae168116604945a**.
- TERMS router: **240de5b34a57689d3eacd51a1995be3fecd40baa**.

Yeni TERMS ilk içeriği 1–65/66–EOF aralıklarıyla tam geri okundu. Düzeltmenin actual diff'i SC02/SC47, yeni SC61, coverage, yorum izi ve 60→61 sayımıyla sınırlıydı. Yardımcı raw-byte indirme DNS hatası verdi; bağlı GitHub çalıştı, yerel tam-byte transfer/hash başarısı iddia edilmez. Otomatik bütün-repository ID/link testi veya bağımsız aktör doğrulaması yapılmadı.

Son main/ref/diff ve current readback kontrolü bu STATE yayınından sonra yapılır; bu chronological uyarı ayrı next-work üretmez ve dosya kendi gelecekteki hash'ini uydurmaz. Kaynak-kayıt/readback kontrolü bilimsel veya ürün düzeyi bağımsız doğrulama değildir.
