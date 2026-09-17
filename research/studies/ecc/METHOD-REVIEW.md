# ECC — Method Evaluation and Evolution

**Purpose:** araştırma yöntemini sonuçlardan bağımsız dokunulmaz kılmamak; iyi/kötü değişiklikleri gerçek etkileriyle gelecekte kullanılabilir vaka olarak korumak. Current method METHOD'dadır; burada revision rationale ve etki kaydı tutulur. Henüz effectiveness doğrulaması yoktur.

## What will be evaluated

| Boyut | Bakılacak somut işaret | Yanlış başarı ölçüsü |
|---|---|---|
| Amaç ve kapsam | Seçilen soru ana açıklamayı değiştirdi mi; kritik production/consumer/etki perspektifi kaçtı mı? | Çok dosya okumak veya çok yeni başlık açmak |
| Kaynak ve anlam | Bir üst sonucu exact kaynağa ve caveat'ine geri götürebiliyor muyuz? | Link bulunması veya özetin akıcılığı |
| Keşif / karşı-sınama | Yeni aile/alternatif eski frame'i düzeltti mi; aleyhte bulgu gerçekten arandı mı? | Her checklist satırına evet yazılması |
| Devralma | Repo-only girişte doğru amaç, yetki, açık iddia ve sonraki soru recover edildi mi? | Dosyaların yalnız var olması |
| Verim / yük | Tekrar okuma, gereksiz state kopyası veya kayıt gecikmesi bounded ilerlemeyi engelliyor mu? | Token/commit sayısını tek başına minimize etmek |
| Revizyon yararı | Değişiklikten sonraki birimde beklenen fark gerçekten gözlendi mi? | Yöntem dosyasının değiştirilmesi |

Bu boyutlar tek bir maturity skoru üretmez. Negatif veya inconclusive sonuç da korunur. Aynı assistant'ın gözlemi independent verification diye sunulmaz.

## MR00 — 2026-09-17 — Initial design review

**Trigger/evidence:** Kullanıcı repo merkezli süreklilik ve araştırmayla birlikte değerlendirilen yöntem istedi. gstack/Hermes/Superpowers yöntemleri full-read edildi. Foundation discussion handoff, mevcut bir araştırma perspektifinin ilk açıklamada yeterince kullanılmadığını ve owner müdahalesiyle düzeltildiğini kaydediyor. Bu tek olay yöntemimizin neden işe yarayacağını kanıtlamaz; salt kaynak varlığına güvenmemek için somut uyarıdır.

**Alternatives considered:**

- Flat file-by-file summary: coverage izi kolay, fakat aynı davranışın dağınık kaynakları ve ilişkileri kaybolabilir.
- Gstack yöntemini aynen kopyalama: iyi başlangıç, fakat ECC host/materialization farklarını ve bu yöntemin kendi gelişim kaydını yeterince ayırmaz.
- Baştan kapsamlı runtime/test kampanyası: bazı güçlü iddialar için yararlı, fakat mevcut planlama aşamasını aşar; source study'yi kurulum/ürün doğrulama işine çevirebilir.
- Seçilen: mekanizma-temelli sentez + host/lifecycle farkları + ayrı yöntem-değerlendirme döngüsü; testler iddia ve yetkiye orantılı.

**Pre-publication analytical challenges and resulting choices:**

| Challenge | v0.1'de karşılığı | Şu anda kanıtlanan sınır |
|---|---|---|
| İlk 'meta-harness' tanımı ilgisiz olmayan başka çalışma ailesini bastırırsa? | P1 native discovery; yedi aile provisional; holdout/reopen | Tasarım tercihi; gerçek omission azaltımı NOT YET OBSERVED |
| Gelecek oturum plan yazıldı diye U01'i veya installation'ı otomatik başlatırsa? | STATE'te next logical / next authorized ve açık non-authorized işler | Metinsel authority ayrımı; live-agent obedience NOT TESTED |
| Aynı skill üç kopyada görünürse üç bağımsız kanıt mı sayılacak? | Source identity/producer/consumer ve varyant test mantığı | Yöntem kuralı; actual ECC kopya taraması U01'de |
| Eski roadmap'teki bug veya alpha ifadesi bugünün gerçeği sayılırsa? | Dated screening ledger + exact source/current-path revalidation | Ön tarama overclaim riski düzeltildi; bug current state araştırılmadı |
| Bir schema testi yeşilse semantic başarı mı denecek? | Evidence class/oracle/negative-control ayrımı | Test stratejisi; ECC testi NOT RUN |
| Çok dosyalı kayıt kendi kendini kopyalayıp stale kalırsa? | Her current gerçeğe bir owner dosyası; derived index; append-only tarihçe | Yapısal tasarım; çok-tur bakım yükü NOT YET OBSERVED |

**Selected change:** METHOD/PLAN v0.1 ile baseline kuruldu; eski method sürümü varmış gibi gösterilmez. U00 review ileride bağımsız önceden-kayıtlı deney diye sayılmaz.

**Expected effect:** U01 daha az marketing-anchored bir source map üretsin; tur kapanışları claim/source/authority ayrımını korusun; yöntem sorunu çıktığında somut revizyon ve sonraki-etki kontrolü mümkün olsun.

**Observed effect so far:** Ön taramadaki bazı güçlü sınıflandırmalar soru/hipotez statüsüne çekildi; current HEAD direct ref ile sabitlendi; partial okumalar full'den ayrıldı. Bu, araştırma disiplininin başlangıçta uygulanmasıdır; uzun dönem odak, öğrenme veya genel yöntem başarısı değildir.

**Next effect check:** U01 sonunda actual family map başlangıç şemasından farklı mı; method değişimi gerekli mi; kayda ayrılan yük üretkenliği engelledi mi; başka oturumda repo-only devam denenirse doğru work/authority recovery oldu mu? Gerçek sonuç geldiğinde MR00'a bağlı yeni kayıt eklenir.

## Future revision record

`MR-ID / date / related unit and Q / old→new method or plan version`

Tetikleyici gözlem ve kaynak; değişen varsayım; gerçek alternatifler; seçilen değişiklik ve kapsam; korunacak eski bulgular; beklenen etki; nasıl/nerede gözleneceği; sonraki actual sonuç; confound/bağımsızlık sınırı; retain/revert/split/unknown kararı.

Bir tur yöntemi değiştirmediyse gerekçeli 'mevcut birim için yeterli' kısa kaydı RESEARCH-LOG'da yeterlidir. Her tur zorunlu yenilik veya method version artışı yoktur.

## Reusable case output, later

P6'da yalnız sonuçları değil, başarısız ilk çerçeveyi, gerekli source reopen'ı, boşa çıkan prosedürü ve continuity sınırını da içeren birkaç gerçek örnek seçilecek. Genel aktarılabilir çekirdek, ECC'ye özgü host/memory/installation ekleri ve henüz doğrulanmamış varsayımlar ayrılacak. Kendi örneğimizden evrensel 'en iyi yöntem' sonucu çıkarılmayacak; global control değişikliği ayrıca yetkilendirilmeli.

## MR01 — 2026-09-17 — U01-A

**Related questions:** Q01/Q02/Q03/Q08/Q10. **Versions:** METHOD 0.1 retained; PLAN 0.1 → 0.2. MR00's earlier NOT YET OBSERVED statements remain historical, not competing current assessments.

**Trigger and evidence:** [Note 01](notes/01-SURFACES-AND-CODEX-CACHE.md) and [S02–S25/E01](evidence/U01-A-SOURCES.md). The source map separated npm/Node dispatch, Rust ecc2 and a native Workflow pilot. S02's host-wide Codex instruction-backed label conflicted with the provider manifest/local README's specific SessionStart projection. S25's verifier collected four manifest reference fields while the actual manifest contained a hooks reference outside that set.

**Alternatives and decision:** Continuing the broad tree scan without resolving this seam would leave the initial host label carrying the model. Calling Codex wholly native would invert rather than fix that overgeneralization. A full live-host/installation campaign would exceed the current evidence need and practical authority. The selected path was to follow the declaration and wrappers, inspect the upstream test's oracle, then run a three-case presence-only cache probe in temporary fixtures. U01 was split so that a publishable bounded result did not masquerade as the complete inventory.

**Observed effect in this unit:** The earlier instruction-only description was corrected to an event/channel/source-specific projection with host trust/consumption still untested. A source prediction of the omitted-hook path became an observed local false-green: C1 missing hook exited 0, while C2 missing checked MCP exited 1. This demonstrates one substantive correction and a bounded falsifier produced while applying the method. It does not establish that this method is superior to alternatives, that all relevant omissions were found or that long-run research focus improved.

**What changed and what did not:** PLAN now carries U01-A/U01-B and Q01a/Q01b. The existing METHOD already required source/consumer distinctions, proportional tests and honest coverage; no new method version is manufactured for this sequencing change. Broad U01 discovery remains PARTIAL. The original full recursive discovery objective is not retrospectively counted as satisfied by a shallow map. Unexpanded regions are preserved in TREE-FRONTIER rather than silently discarded.

**Cost and limitations observed:** Connector display truncation required recovering the full root response. A direct container acquisition failed at DNS while the connector worked; offline execution was still possible. Exact checker/manifest materialization required blob identity checks. Entry/log maintenance and multi-file publication add real work; this unit supplies no timing comparison or proven optimal record count. We should not repeat unchanged full entry files merely to demonstrate activity; stable identities and selective re-entry preserve the existing progressive-retrieval method.

**Causal and verification boundary:** The checker omission is directly visible and locally exercised. A wider story about manifest evolution outrunning verifier maintenance remains a hypothesis, not an established historical root cause. The local probe was designed after reading source and used a pre-execution criterion; it is source-informed exploratory work by the same assistant, not blind independent replication. This was same-conversation re-entry, not a fresh-session comprehension test.

**Next effect check — U01-B:** Does the next map preserve all known delivery/runtime families instead of turning into a Codex bug hunt? Do source→materialization→consumer paths actually explain the distinction, or require another question split? Can U01-A's tested/unexamined boundary be recovered without rerunning and double-counting E01? Record actual outcomes, including an inconclusive result; do not reward method revision merely because it exists.
