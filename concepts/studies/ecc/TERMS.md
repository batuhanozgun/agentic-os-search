# ECC — Bağlamlı kullanım kayıtları

2026-09-20, **B6-T17-C5b / C1-C2-C3-C4-DURABLE-COMPLETE / U10-TRANSFER-COMPLETE / U11-A-B-TRANSFER-COMPLETE / C5b-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya `research/studies/ecc/` concepts girişidir. ECC source-study kendi açısından **ACTIVE / PARTIAL**; U12-C'ye kadar published, U13-A/Q07d1 not started. Concepts çalışması source-study research'ini sürdürmez.

Gerçek okuma/coverage: [READING.md](READING.md). C1–C4 ayrıntılı geçmiş, C5a ve C5b/U11-A–B exact dosya/sürüm manifestleri oradan geri kazanılır.

## 1. Current linked term groups

- [TERMS-SURFACES-INSTALLATION.md](TERMS-SURFACES-INSTALLATION.md) — U01–U02 — **C1 COMPLETE**.
- [TERMS-WORK-EXECUTION-MEMORY.md](TERMS-WORK-EXECUTION-MEMORY.md) — U03–U04 — **C2 COMPLETE**.
- [TERMS-LEARNING-GOVERNANCE.md](TERMS-LEARNING-GOVERNANCE.md) — U05–U06 — **C3 COMPLETE**.
- [TERMS-REVIEW-RUNTIME-OPERATOR.md](TERMS-REVIEW-RUNTIME-OPERATOR.md) — U07–U09 — **C4 COMPLETE**.
- [TERMS-EVALUATION-REGISTRY.md](TERMS-EVALUATION-REGISTRY.md) — U10-A — **C5a TRANSFER COMPLETE**, ECC-E01–E50.
- [TERMS-OFFLINE-CAPSULES.md](TERMS-OFFLINE-CAPSULES.md) — U10-B — **C5a TRANSFER COMPLETE**, ECC-O01–O69.
- [TERMS-NATIVE-REVIEW.md](TERMS-NATIVE-REVIEW.md) — U11-A — **TRANSFER COMPLETE / C5b PARTIAL**, ECC-N01–N77.
- [TERMS-SCHEDULED-WORK.md](TERMS-SCHEDULED-WORK.md) — U11-B — **TRANSFER COMPLETE / C5b PARTIAL**, ECC-SC01–SC61.

Bunlar source-local contextual inventories'dir; global ortak sözlük değildir. C5a'nın iki dosyası 119, U11-A dosyası 77, U11-B dosyası 61 adreslenebilir kullanım satırı taşır. Bu sayılar kavram, bağımsız kanıt veya ilerleme yüzdesi değildir.

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

**C1–C4, C5a/U10-A–U10-B ve C5b/U11-A–U11-B source-local aktarımı tamamlandı.** Exact next: **B6-T17-C5b / U11-C**, ardından U11-D–E. U12-A/B1/B2/C ve package-wide C6 daha sonra gelir.

ECC package **PACKAGE-COMPLETE değildir**. C5'in U11-C–U12 bölümü ve C6 açık; B7/B8 başlamadı. C5a/b/c mevcut C5'in yürütme dilimleri, yeni araştırma kapsamı değildir.

## 4. İlişki ve düzeltme girişleri

R09'un evaluation-registry işareti E serisiyle ayrıntılanır. L35–L57 skill evaluator, E serisi Rust recorded evaluator ve O serisi Node utility aynı evaluation/promotion mekanizması sayılmaz. R74/R75/R107/R125–R127 session-state bulguları E30–E32'nin gerçek conditional update/transaction kontrolünü geçersiz saymak için kullanılmaz.

R10 capsule ve R11 kısa static-gate anlatımı O serisiyle birlikte okunur: **O60 statik helper/inspection; O58/O59 public execution refusal**. Public gate'in açık olduğu çıkarılmaz. İlk yeni Node dökümündeki capsule/journal birleştirmesi düzeltildi: **O03 capsule, O69 journal**. Düzeltme ve etkilenmiş kayıt kontrolü aynı dosyanın §8'inde görünürdür.

R13–R18'in erken native-review işaretleri N serisiyle ayrıntılanır. **R16 genel durdurucu standing; N23 failedDimensions; N48 typed blocking findings** farklı kapsamları taşır. Reviewer failure sonucu, finding dizisi boşken de aggregate CHANGES_REQUESTED olabilir. Reviewer verdict N39, aggregate APPROVE N50, dış insan onayları N55/N56 birbirinin yerine kullanılmaz. Confirmed N46 güçlü doğruluk sertifikası değildir.

N dosyasının ilk readback ayrımı: **N21 trigger / N76 security dimension; N32 dimension / N77 dimensions listesi**. N25'te proof'un koşullu zorunluluğu açıklaştırıldı. İlk sürüm/gerekçe/etki kontrolü TERMS-NATIVE-REVIEW §10'da kalır. Source-study veya önceki TERMS bu ayrım için yeniden yazılmadı.

SC dosyası recurring instruction/occurrence/session/admission ayrımını ekler. **SC21 last_run_at captured pass time; SC28 daemon batch limit; SC33 queue admission; SC49 removal; SC51 revocation** aynı başarı/otorite hükmünü taşımaz. E30–E32 registry transaction'ı SC38 schedule writer'ın kontrolü gibi gösterilmez; R125–R127 eski-attempt finalizer'ı SC46 competing due snapshots ile aynı hata yolu sayılmaz.

U11-B ilk readback açıklığı: **SC47 finite schedule / SC61 terminal schedule handling** ayrı adreslendi; SC02'de due olmanın gerçek execution olmadığı netleştirildi. Gerekçe ve etki kontrolü TERMS-SCHEDULED-WORK §8'de korunur. Source study, R/E/N veya diğer eski kullanım dosyaları değiştirilmedi.

K/B/Y/T/P, N dosyasındaki H/D/F ve SC dosyasındaki K/Y/T/H source-role anahtarları, note bölüm referansları ve pinned repository snapshot'ı yorumun nereden geldiğini taşır. Upstream kod/testlerin eski araştırmada okunması veya dosyaya kaynak kimliği yazılması bu Concepts turunda yeniden çalıştırıldıkları/okundukları anlamına gelmez. U11-A'daki E08 raw verisinin read-only recovery/schema kontrolü yeni native Workflow/model deneyi değildi; U11-B'de yeni deney veya eski E08/E07 yeniden koşusu yoktur.
