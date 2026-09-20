# ECC — Bağlamlı kullanım kayıtları

2026-09-20, **B6-T17-C5c / C1-C2-C3-C4-DURABLE-COMPLETE / U10-TRANSFER-COMPLETE / U11-A-B-C-D-E-TRANSFER-COMPLETE / C5b-COMPLETE / U12-A-TRANSFER-COMPLETE / C5c-PARTIAL / C5-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya `research/studies/ecc/` concepts girişidir. ECC source-study kendi açısından **ACTIVE / PARTIAL**; U12-C'ye kadar published, U13-A/Q07d1 not started. Concepts çalışması source-study research'ini sürdürmez.

Gerçek okuma/coverage: [READING.md](READING.md). C1–C4 ayrıntılı geçmiş, C5a/C5b ve U12-A exact dosya/sürüm manifestleri oradan geri kazanılır.

## 1. Current linked term groups

- [TERMS-SURFACES-INSTALLATION.md](TERMS-SURFACES-INSTALLATION.md) — U01–U02 — **C1 COMPLETE**.
- [TERMS-WORK-EXECUTION-MEMORY.md](TERMS-WORK-EXECUTION-MEMORY.md) — U03–U04 — **C2 COMPLETE**.
- [TERMS-LEARNING-GOVERNANCE.md](TERMS-LEARNING-GOVERNANCE.md) — U05–U06 — **C3 COMPLETE**.
- [TERMS-REVIEW-RUNTIME-OPERATOR.md](TERMS-REVIEW-RUNTIME-OPERATOR.md) — U07–U09 — **C4 COMPLETE**.
- [TERMS-EVALUATION-REGISTRY.md](TERMS-EVALUATION-REGISTRY.md) — U10-A — **C5a TRANSFER COMPLETE**, ECC-E01–E50.
- [TERMS-OFFLINE-CAPSULES.md](TERMS-OFFLINE-CAPSULES.md) — U10-B — **C5a TRANSFER COMPLETE**, ECC-O01–O69.
- [TERMS-NATIVE-REVIEW.md](TERMS-NATIVE-REVIEW.md) — U11-A — **TRANSFER COMPLETE**, ECC-N01–N77.
- [TERMS-SCHEDULED-WORK.md](TERMS-SCHEDULED-WORK.md) — U11-B — **TRANSFER COMPLETE**, ECC-SC01–SC61.
- [TERMS-REMOTE-REQUESTS.md](TERMS-REMOTE-REQUESTS.md) — U11-C — **TRANSFER COMPLETE**, ECC-RD01–RD70.
- [TERMS-BACKLOG-COORDINATION.md](TERMS-BACKLOG-COORDINATION.md) — U11-D — **TRANSFER COMPLETE**, ECC-BC01–BC70.
- [TERMS-TEMPLATE-LAUNCH.md](TERMS-TEMPLATE-LAUNCH.md) — U11-E — **TRANSFER COMPLETE**, ECC-TL01–TL74.
- [TERMS-EXECUTION-PROFILES.md](TERMS-EXECUTION-PROFILES.md) — U12-A — **TRANSFER COMPLETE / C5c PARTIAL**, ECC-EP01–EP84.

Bunlar source-local contextual inventories'dir; global ortak sözlük değildir. C5a'nın iki dosyası 119, U11-A dosyası 77, U11-B dosyası 61, U11-C dosyası 70, U11-D dosyası 70, U11-E dosyası 74 ve U12-A dosyası 84 adreslenebilir kullanım satırı taşır. Bu sayılar kavram, bağımsız kanıt veya ilerleme yüzdesi değildir. Bağlı eski dosyalardaki C5b-PARTIAL ifadeleri kendi yayın checkpoint'lerini anlatır; güncel dilim durumu bu giriş ve READING'dedir.

## 2. Package-level expressions

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-P01 — ECC | Procedural assets, install/distribution, work/runtime, memory/learning, evaluation and governance surfaces taşıyan external target. | Tek uniformly integrated runtime olarak varsayılmaz. |
| ECC-P02 — source surface | Repo'daki authored/configured mechanism surface. | Installed/live/effective behavior değil. |
| ECC-P03 — mechanism slice | Bounded trigger→selection→effect→acceptance/failure chain araştırma birimi. | Whole subsystem veya whole product değil. |
| ECC-P04 — bounded source answer | Exact pinned source + declared evidence class altında answered question. | Product-wide/current empirical closure değil. |
| ECC-P05 — local execution | Exact isolated fixture'da unchanged source behavior observation. | Live host/model/product validation değil. |
| ECC-P06 — source-derived counter-path | Multiple code paths together imply a reachable contrast/failure condition. | Observed production incident değil. |
| ECC-P07 — evidence class | Target claim/source observation/test inspected/local execution gibi claim-strength qualifier. | Tek eksenli confidence score değil. |
| ECC-P08 — installed ≠ discoverable ≠ selected ≠ followed ≠ effective | ECC METHOD'in recurring distinction. | Universal ontology değil; source-study methodological boundary. |
| ECC-P09 — recorded ≠ accepted | Stored/report state ile governance/work acceptance ayrımı. | Every record untrusted demek değil. |
| ECC-P10 — test-green ≠ valid oracle | Passing/expected test result'in measured claim'e uygun oracle olma gereği. | Tests useless demek değil. |

## 3. Current status ve devam

**C1–C4, C5a/U10-A–U10-B, C5b/U11-A–U11-E ve C5c/U12-A source-local aktarımı tamamlandı.** Exact next: **B6-T17-C5c / U12-B1**, ardından U12-B2, U12-C ve package-wide C6.

ECC package **PACKAGE-COMPLETE değildir**. C5c'nin U12-B1/B2/C bölümü ve C6 açık; B7/B8 başlamadı. C5a/b/c mevcut C5'in yürütme dilimleri, yeni araştırma kapsamı değildir. Bir source-family aktarımının kapanışı paket geneli kaynak/ID/coverage reconciliation veya source-study closure sayılmaz.

## 4. İlişki ve düzeltme girişleri

R09'un evaluation-registry işareti E serisiyle ayrıntılanır. L35–L57 skill evaluator, E serisi Rust recorded evaluator ve O serisi Node utility aynı evaluation/promotion mekanizması sayılmaz. R74/R75/R107/R125–R127 session-state bulguları E30–E32'nin gerçek conditional update/transaction kontrolünü geçersiz saymak için kullanılmaz.

R10 capsule ve R11 kısa static-gate anlatımı O serisiyle birlikte okunur: **O60 statik helper/inspection; O58/O59 public execution refusal**. Public gate'in açık olduğu çıkarılmaz. İlk yeni Node dökümündeki capsule/journal birleştirmesi düzeltildi: **O03 capsule, O69 journal**. Düzeltme ve etkilenmiş kayıt kontrolü aynı dosyanın §8'inde görünürdür.

R13–R18'in erken native-review işaretleri N serisiyle ayrıntılanır. **R16 genel durdurucu standing; N23 failedDimensions; N48 typed blocking findings** farklı kapsamları taşır. Reviewer failure sonucu, finding dizisi boşken de aggregate CHANGES_REQUESTED olabilir. Reviewer verdict N39, aggregate APPROVE N50, dış insan onayları N55/N56 birbirinin yerine kullanılmaz. Confirmed N46 güçlü doğruluk sertifikası değildir.

N dosyasının ilk readback ayrımı: **N21 trigger / N76 security dimension; N32 dimension / N77 dimensions listesi**. N25'te proof'un koşullu zorunluluğu açıklaştırıldı. İlk sürüm/gerekçe/etki kontrolü TERMS-NATIVE-REVIEW §10'da kalır. Source-study veya önceki TERMS bu ayrım için yeniden yazılmadı.

SC dosyası recurring instruction/occurrence/session/admission ayrımını ekler. **SC21 last_run_at captured pass time; SC28 daemon batch limit; SC33 queue admission; SC49 removal; SC51 revocation** aynı başarı/otorite hükmünü taşımaz. E30–E32 registry transaction'ı SC38 schedule writer'ın kontrolü gibi gösterilmez; R125–R127 eski-attempt finalizer'ı SC46 competing due snapshots ile aynı hata yolu sayılmaz.

U11-B ilk readback açıklığı: **SC47 finite schedule / SC61 terminal schedule handling** ayrı adreslendi; SC02'de due olmanın gerçek execution olmadığı netleştirildi. Gerekçe ve etki kontrolü TERMS-SCHEDULED-WORK §8'de korunur. Source study, R/E/N veya diğer eski kullanım dosyaları değiştirilmedi.

K/B/Y/T/P, N dosyasındaki H/D/F ve SC dosyasındaki K/Y/T/H source-role anahtarları, note bölüm referansları ve pinned repository snapshot'ı yorumun nereden geldiğini taşır. Upstream kod/testlerin eski araştırmada okunması veya dosyaya kaynak kimliği yazılması bu Concepts turunda yeniden çalıştırıldıkları/okundukları anlamına gelmez. U11-A'daki E08 raw verisinin read-only recovery/schema kontrolü yeni native Workflow/model deneyi değildi; U11-B'de yeni deney veya eski E08/E07 yeniden koşusu yoktur.

U11-C'nin RD kayıtları **HTTP acceptance / dispatch / completion**, **requested target / lead / receiver**, **never-targeted / disappeared-target**, **valid profile name / reused effective policy** ayrımlarını ekler. RD29 kalıcı result_session_id ilişkisi taşır; SC53–SC54 scheduler sınırı buraya aynen aktarılmaz. RD56 per-request failure isolation, SC44 first-error davranışından farklıdır. RD50 DeferredSaturated current outcome'dur, request Pending kalır; RD49 Failed aynı retry yoluna girmez. RD64 read marker, RD66 per-request completion değildir.

RD dosyası kaynak §1–10 ve K/Y/T/H rolleriyle bağlıdır. U11-C turunda eski kayıtları değiştirmeyi gerektiren maddi çelişki saptanmadı; aynı isimlerden eş anlamlılık üretilmedi. Yeni endpoint/test/deney yapılmadı. Ayrıntılı eski okuma/yayın geçmişi READING'nin immutable bağlantılarında korunur; U11-C'nin o tarihteki next'i U11-D artık tamamlanmış aktarımdır.

U11-D'nin BC kayıtları **mesaj yönlendirme / task decomposition / accepted result**, **launch arguments / companion unread handoff**, **drain routing guard / rebalancer destination check**, **all-unread / task-handoff load**, **persistent cooloff / timed backoff**, **current capacity / old controller history** ayrımlarını ekler. BC04 otomatik dağıtımın default false sınırını; BC22 koşullu tekrar-forwarding'i taşır. BC45/BC47/BC48 birlikte süre dolmasını değil kalıcı koşulla dispatch'in atlanmasını anlatır.

RD64/65'in tüketim işaretleri BC62/63 ve BC11/18/27 ile ayrıntılanır. Inbox'ta gösterilen sınırlı küme ile read işaretlenen bütün incoming unread kümesi farklıdır. RD56 remote hata izolasyonu BC40 backlog first-error yoluna taşınmaz; RD50 request Pending ile BC17 handoff unread aynı kalıcı nesne değildir. BC dosyası note §1–8, ledger/test ve publication rollerine bağlıdır. Önceki TERMS dosyaları U11-D turunda değiştirilmedi; yeni daemon/SQL/model/test çalıştırılmadı. O checkpoint'in next'i U11-E daha sonra tamamlandı.

U11-E'nin TL kayıtları **text variable / actual environment**, **explicit default agent / omission**, **all-step resolution / all-effect atomicity**, **observed slots / reserved capacity**, **ordered admission / predecessor completion / accepted output**, **common anchor / dependency edges**, **fresh retry / resume checkpoint** ayrımlarını taşır. TL36 mevcut session'ları gerçekten düşer; SC28'in yalnız batch limit kullanımına eşitlenmez. TL47 yeni session yaratır, RD reuse yolu değildir. TL48/TL49, BC20/BC21'in launch-input/companion-message ayrımını korur.

TL ilk aktarımının ilişki özeti düzeltildi: global default hazırlığı ile her step'in loop içi profil seçimi ayrı gösterildi. **TL38 miktar / TL74 ret; TL50 process completion / TL73 accepted predecessor output** ayrı adreslendi; ledger'daki dependency-sync warning TL72 eklendi. İlk sürüm/gerekçe/etki kontrolü TERMS-TEMPLATE-LAUNCH §10'dadır. Önceki kullanım dosyaları veya source-study değiştirilmedi. TL35 profilin seçilip saklanmasını anlatır; U12-A bunun ayrı consumer kaynak aktarımı olarak şimdi tamamlandı, gerçek host enforcement hâlâ Q02a2 sınırındadır.

U12-A'nın EP kayıtları **profile representation / effective host enforcement**, **preapproval / tool availability**, **native option / task text**, **configured replacement / additive customization**, **profile token budget / global USD / per-profile USD**, **sampled control / pre-spend admission**, **decoded-empty / explicit-empty** ve **environment label / runtime identity** ayrımlarını ekler. EP44/EP47/EP50–EP51 gerçek ayrı token-control tüketicisini korur; EP43'ün profil dolar tavanı aynı ECC kontrolüne taşınmaz. EP09 agent=None, session'daki EP08 harness seçimi kaybı değildir.

EP ilk aktarımında birleşik adresler ayrıldı: **EP29 OpenCode / EP84 Gemini permission; EP33 program / EP83 base_args**. Gerekçe ve ilgili kayıt kontrolü TERMS-EXECUTION-PROFILES §11'dedir. TL37'nin Stale kapasite nüfusu EP58'in stop nüfusuna eşitlenmez; RD reuse yolu bu aktarım sayesinde yeni profil uygulaması kazanmaz. Önceki TERMS ve source-study değişmedi. Dated host sözleşmeleri 2026-09-19 kaynak atfıdır; bu tur yeni host/web/test doğrulaması yapılmadı. Exact next **C5c/U12-B1**'dir.
