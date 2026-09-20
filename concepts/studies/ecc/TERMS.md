# ECC — Bağlamlı kullanım kayıtları

2026-09-20, **B6-T17-C5a / C1-C2-C3-C4-DURABLE-COMPLETE / U10-TRANSFER-COMPLETE / C5-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya `research/studies/ecc/` concepts girişidir. ECC source-study kendi açısından **ACTIVE / PARTIAL**; U12-C'ye kadar published, U13-A/Q07d1 not started. Concepts çalışması source-study research'ini sürdürmez.

Gerçek okuma/coverage: [READING.md](READING.md). C1–C4 ayrıntılı geçmiş ve mevcut C5a exact dosya/sürüm manifesti oradan geri kazanılır.

## 1. Current linked term groups

- [TERMS-SURFACES-INSTALLATION.md](TERMS-SURFACES-INSTALLATION.md) — U01–U02 — **C1 COMPLETE**.
- [TERMS-WORK-EXECUTION-MEMORY.md](TERMS-WORK-EXECUTION-MEMORY.md) — U03–U04 — **C2 COMPLETE**.
- [TERMS-LEARNING-GOVERNANCE.md](TERMS-LEARNING-GOVERNANCE.md) — U05–U06 — **C3 COMPLETE**.
- [TERMS-REVIEW-RUNTIME-OPERATOR.md](TERMS-REVIEW-RUNTIME-OPERATOR.md) — U07–U09 — **C4 COMPLETE**.
- [TERMS-EVALUATION-REGISTRY.md](TERMS-EVALUATION-REGISTRY.md) — U10-A — **C5a TRANSFER COMPLETE**, ECC-E01–E50.
- [TERMS-OFFLINE-CAPSULES.md](TERMS-OFFLINE-CAPSULES.md) — U10-B — **C5a TRANSFER COMPLETE**, ECC-O01–O69.

Bunlar source-local contextual inventories'dir; global ortak sözlük değildir. Yeni iki dosya toplam 119 adreslenebilir kullanım satırı taşır. Bu sayı kavram, bağımsız kanıt veya ilerleme yüzdesi değildir.

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

**C1–C4 ve C5a/U10-A–U10-B source-local aktarımı tamamlandı.** Exact next: **B6-T17-C5b / U11-A**, ardından U11-B–E. U12-A/B1/B2/C ve package-wide C6 daha sonra gelir.

ECC package **PACKAGE-COMPLETE değildir**. C5'in U11–U12 bölümü ve C6 açık; B7/B8 başlamadı. C5a/b/c mevcut C5'in yürütme dilimleri, yeni araştırma kapsamı değildir.

## 4. Yeni ilişki ve düzeltme girişleri

R09'un evaluation-registry işareti E serisiyle ayrıntılanır. L35–L57 skill evaluator, E serisi Rust recorded evaluator ve O serisi Node utility aynı evaluation/promotion mekanizması sayılmaz. R74/R75/R107/R125–R127 session-state bulguları E30–E32'nin gerçek conditional update/transaction kontrolünü geçersiz saymak için kullanılmaz.

R10 capsule ve R11 kısa static-gate anlatımı O serisiyle birlikte okunur: **O60 statik helper/inspection; O58/O59 public execution refusal**. Public gate'in açık olduğu çıkarılmaz. İlk yeni Node dökümündeki capsule/journal birleştirmesi düzeltildi: **O03 capsule, O69 journal**. Düzeltme ve etkilenmiş kayıt kontrolü aynı dosyanın §8'inde görünürdür.

Yeni kayıtlardaki K/B/Y/T/P source-role anahtarları, note bölüm referansları ve pinned repository snapshot'ı yorumun nereden geldiğini taşır. Upstream kod/testlerin eski araştırmada okunması veya dosyaya kaynak kimliği yazılması bu Concepts turunda yeniden çalıştırıldıkları/okundukları anlamına gelmez.
