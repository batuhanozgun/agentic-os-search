# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 8 — SOUL Research question / evidence-dimension map  
**Son güncelleme:** 2026-08-30

## Ana hedef

SOUL'un neden yeniden kurulduğunu, önceki çalışma/ürün deneyimlerinden hangi problem sınıflarının açığa çıktığını ve **SOUL mimarisine geçmeden önce araştırılması gereken genel problem/evidence alanlarını** kanıta dayalı biçimde çıkarmak.

Bu çalışma SOUL mimarisi önermeyecek. Research output ile architecture decision ayrı tutulacak.

## Kaynak rolleri

### Omurga kaynaklar

- `soul`: birincil SOUL intent + Development OS + work/verification/review evidence.
- `os-architect`: tarihsel arıza, yöntem, araştırma, sahip düzeltmeleri ve KEEL'in üst-seviye yeniden değerlendirilmesi.
- `keel`: somut mekanizma/runtime yüzeyi; tarihsel iddiaların bugünkü mekanik karşılığını sınamak için.

### Sınırlı first-party predecessor source

- `keel-research`: yalnız SOUL'un kendi WP/source chain'i doğrudan işaret ettiğinde seçici prior-art/evidence olarak kullanılır; SOUL authority veya dördüncü omurga kaynak değildir.

## Tamamlanan geçişler

### A — çalışma düzeni ve araştırma yöntemi

Doğrulandı:
- depo/temsil failure'ı,
- çalışma-döngüsü failure'ı,
- epistemik süreç failure'ı.

### B — KEEL problem ve kanıt modeli

Kanıt statüleri ayrıldı:
- gözlenen arıza,
- ölçüm/tatbikat,
- tasarım hükmü,
- dış yakınsama.

### C — önceki araştırma ve dış-göz kayıtları

Doğrulandı:
- soru ≠ görev,
- amaç/öncül yeniden türetme ihtiyacı,
- uzman–sahip asimetrisi,
- session context'in sonuç taşırken amaç/neden kaybetmesi,
- sorgulama için `üreteç + tetik + kanıt zinciri`,
- ders→ihtiyaç köprüsü problemi.

Sınır: geçmiş altı kalemlik programın yalnız 1, 2 ve 6 repo ayağı tamamlanmış; 3–5 araştırılmış sayılmıyor.

### D — KEEL mekanik karşı-okuma

Seçici kod/sözleşme/test okuması doğruladı:
- fail-closed state/order parser,
- gerçek Claude Code hook wiring,
- role/write cage,
- salt-okur verifier yüzeyi,
- fresh card / fail-visible closure,
- mutation-test definitions,
- kısmi lesson→need işaretçi mekanizması.

Sınır: fresh execution üretilemedi; test tasarımı ile güncel pass ayrı tutuluyor.

### E — KEEL → SOUL geçişi

#### Tarihsel pivot

2026-08-08..13 os-architect/KEEL kayıtlarında problem product-bug seviyesinin üstüne çıktı:
- mekanizma gerçekten gerekli mi / doğru katmanda mı,
- sistem sahibini amacına taşıyor mu,
- koltuk-içi akıl güçlü iken koltuk-üstü akıl sahipsiz mi,
- gate biçim ölçerken değer/uyum/geçen-zaman ölçülüyor mu,
- owner hidden orchestrator oluyor mu,
- doğru ders ihtiyaç anında çağrılıyor mu,
- root cause yalnız mekanik kusur değil framing/çalışma biçimi olabilir mi.

2026-08-11: `araştırma evi kurulacak`; araştırmalar sonraki yeni geliştirmeye girdi olacak. Bu formal product decision değil, yön beyanı.

#### SOUL birincil amacı

SOUL preset workflow/team/template değil; temel işi **system formation**:

1. intended outcome'u anlamak,
2. gereken working system'i belirlemek,
3. gereken capability'leri yaratmak/organize etmek,
4. sistemi outcome'a doğru işletmek,
5. progress/correctness doğrulamak,
6. assumptions gerçeklikle bozulduğunda adapt etmek,
7. continuity/governance/state'i zaman içinde korumak.

Development OS, SOUL'un çözmeyi amaçladığı agentic failure class'larını SOUL'u geliştirirken yeniden üretmemek için ürün mimarisinden önce kuruluyor.

WP-000 açıkça product capability architecture, technology choice, KEEL folder mapping ve runtime code'u Phase-0 non-scope yapıyor.

#### Öncül → SOUL bağlantısı

`REASONING-POLICY-SYNTHESIS-2026-08-26.md`, KEEL-Work, keel-dev, oyun2, os-architect ve keel-research kaynaklarını SHA'larıyla listeliyor; source-derived principles ile SOUL-specific synthesis'i ayrı tutuyor.

Bu yüzden SOUL–öncül bağı yalnız benzerlik değil, birincil source-chain kanıtıdır.

### F — SOUL Research ↔ SOUL architecture boundary — TAMAMLANDI

#### Direct SOUL governance

Doğrudan doğrulandı:

- `ROLE_MODEL.md`: Researcher external/empirical evidence kurar; finding'i sessizce architecture decision'a çeviremez, conflicting evidence'i saklayamaz.
- `EVIDENCE_TEMPLATE.md`: question/source/method/findings/limitations/`what this does NOT prove`/decision relevance taşır; proper decision process olmadan architecture decision ilan etmez.
- `DECISION_POLICY.md`: açık ifade **Research is not decision**. Architecture decision ADR + independent review ister; foundation change daha güçlü gate taşır.
- `REASONING_POLICY.md`: primary/authoritative sources, date/version freshness, disagreement/limitations, similarity≠equivalence, popularity≠quality, tool/framework≠problem definition, analytical provenance `claim→method→inputs→source/version`.
- `development/02_architecture/README.md`: KEEL evidence/prior art'tır, default SOUL schema değildir.
- `ROADMAP.md`: Phase 1 Definition → Phase 2 Capability Architecture without KEEL organising principle → Phase 3 Failure Model; technology choice ancak Phase 11.

#### Verification ve adversarial review farklı kanıt yolları

- WP-006 exact-target verification tüm current Phase-0 kriterlerde PASS verdi.
- WP-007 ayrı adversarial review yine material F-AR-001 bulup `Requires repair` verdi.

Sonuç: **spec conformance PASS ≠ frame/design robustness**.

#### WP-021 lifecycle learning

WP-021 doğrudan şunu problemleştiriyor:

**material FAIL / Requires-repair evidence → otomatik repair-shaped work**.

Önerilen disiplin:
- substantive next-work selection, result integration ve implementation ayrı;
- repair conclusion olmalı, default route değil;
- next work design, reframe, investigation, research into another layer veya başka authorised path olabilir;
- research evidence-gap driven olmalı ve decision authority olmamalı;
- more analysis / more artefacts başarı metriği değil.

Not: WP-021 current proposal/design evidence'dır; accepted governance değildir.

#### Pre-build review lessons — F-AR-009..012

2026-08-29 exact-target pre-build adversarial review dört material design gap buldu:

1. **F-AR-009:** technical design acceptance / material finding disposition circular veya unowned olabilir.
2. **F-AR-010:** bundled replay permanent Planner necessity'sini causal identify edemez; ablation/simpler comparator yok.
3. **F-AR-011:** selective context metadata gerekli evidence'i omission detection olmadan gizleyebilir.
4. **F-AR-012:** rollback mitigation deniyor ama invariant/disable/partial-rollout/forward-restoration contract yok.

SOUL Research için handoff dersleri:
- evidence report kendi adoption kararını içeremez;
- package improvement component necessity kanıtı değildir;
- derived/curated view source completeness değildir;
- reversibility/recovery iddiası lifecycle contract gerektirir.

#### Sınırlı predecessor boundary evidence

SOUL WP-021'in doğrudan işaret ettiği `batuhanozgun/keel-research` scratch source seçici okundu.

- Scratch planning kendini exploratory/non-authoritative, SOUL architecture truth olmayan evidence/input olarak sınırlıyor.
- `PROMOTION.md` tarihsel research-house sınırını açıkça kuruyor: `research repo research üretir; product backlog üretmez`.
- `SUPPORT/GAP/RISK/CONTRADICTION/UNTESTED/ALTERNATIVE` epistemik sinyallerdir; TODO/feature/bug değildir.
- Product promotion ayrı değerlendirme kapısıdır.

Bu SOUL rule'u değildir; SOUL'un kendi current governance'iyle aynı yüksek-seviye ayrımın tarihsel öncülüdür.

## Artık doğrudan kurulabilen boundary modeli

**Research informs. Work selection decides what kind of next work is justified. Design/ADR converts evidence into a candidate technical commitment. Independent verification/challenge constrains the claim. Accepted governance changes status. Implementation is downstream.**

Özel ayrımlar:

- research finding ≠ requirement,
- requirement/capability hypothesis ≠ mechanism,
- mechanism candidate ≠ accepted architecture,
- verifier PASS ≠ adversarial robustness,
- historical replay ≠ generalisation,
- multi-model/same-model agreement ≠ independent ground truth,
- accepted design ≠ implementation proof.

## Bağımsız sentez notları

- `research/soul-context/notes/transition-to-soul.md`
- `research/soul-context/notes/research-to-architecture-boundary.md`

## SOUL Research amacı için güncel çalışma hükmü

### Doğrudan kanıtlanan arka plan

SOUL herhangi bir intended outcome için gereken controlled working system'i oluşturabilen general-purpose system formation architecture'a yöneliyor.

SOUL'un kendi development process'i, ürün mimarisini erken kapatmamak ve chat memory/self-certification/framing drift gibi failure'ları yeniden üretmemek için önce kontrol altına alınıyor.

Research ile architecture/decision açıkça farklı authority/state katmanlarıdır.

### Güçlü fakat hâlâ charter-level inference

SOUL Research büyük olasılıkla, architecture work'e **genel problem modeli + decision-oriented evidence base** sağlamak için ayrı tutuluyor:

- KEEL'e özgü mekanizmaları evrensel gereksinim sanmamak,
- mevcut araç/runtime affordance'larının mimariyi belirlemesini önlemek,
- tarihsel failure'ları generalisability testine sokmak,
- external/empirical evidence ve materially different scenarios ile problem/capability/failure hypotheses'i challenge etmek,
- architecture kararına dönüşmeden önce limitations/falsifiers/alternatives/provenance'i durable biçimde taşımak.

Checked `research/soul-context` tree içinde ayrı verbatim `SOUL Research charter` veya formal handoff schema yok. Bu nedenle yukarıdaki ifade hâlâ evidence-supported working judgment'tır.

## Provisional research output shape — SONUÇ DEĞİL, Faz-8'de sınanacak

Boundary evidence, future research artefact'in en az şu karar-yönelimli alanları taşımasının yararlı olacağını düşündürüyor:

- exact research question / decision dimension,
- uncertainty neden material,
- observation / inference / assumption ayrımı,
- primary/authoritative source + version,
- conflicting evidence / alternatives,
- source quality / omissions,
- supported claim,
- explicit non-proof,
- capability/failure/control-property hypothesis,
- alternative frame/layer,
- strongest falsifier,
- causal necessity identified mi değil mi,
- remaining uncertainty ve hangi evidence kararı değiştirir,
- downstream decision relevance without architecture verdict.

Bu henüz canonical schema değildir.

## Provisional stopping rule — Faz-8'de sınanacak

Henüz canonical SOUL Research completion rule bulunmadı.

Mevcut evidence'den türeyen provisional rule:

**Bir research line, tanımlı decision-critical uncertainty gereken risk seviyesinde additional evidence'in authorised next-work/design kararını değiştirme ihtimali düşük olacak kadar daraldığında; ya da kalan uncertainty açıkça bounded olup başka method/phase'e devredilmesi gerektiğinde kapanabilir.**

Bu `yeterince kaynak okuduk` kriterinden daha güçlüdür ama henüz formal research governance değildir.

## Şimdi — G geçişi / Faz 8: research question + evidence-dimension map

En yüksek bilgi değerli soru:

**SOUL'un Phase 1 Definition, Phase 2 Capability Architecture ve Phase 3 Failure Model çalışmalarına geçmeden önce SOUL Research hangi minimum problem/evidence boyutlarını araştırmalı; her boyut hangi kanıt sınıfıyla ve hangi falsifier/stopping condition ile sınanmalı?**

Amaç bir feature listesi veya architecture blueprint çıkarmak değil; **araştırma kapsamının gerekli ve yeterli boyutlarını** çıkarmak.

### Faz-8 çalışma sırası

1. SOUL foundation (`VISION / DEFINITION / SUCCESS_CRITERIA / NON_NEGOTIABLES`) içindeki yük taşıyan outcome/property'leri tekrar decision-dimension olarak çıkar.
2. ROADMAP Phase 1–3 gate'lerini araştırma yükümlülüklerine çevir — çözüm/mekanizma değil soru/evidence biçiminde.
3. A–F geçişlerinden çıkan failure class'ları deduplicate ederek `problem dimension` adaylarına map et.
4. Her dimension için:
   - neden material,
   - mevcut kanıt,
   - unknown/assumption,
   - gerekli evidence class,
   - strongest falsifier / counter-frame,
   - stopping condition,
   - downstream decision dimension
   tanımla.
5. General-purpose iddiası nedeniyle en az üç materially different scenario/domain family'nin hangi dimensions'i test ettiğini araştır; implementation pilot tasarlama.
6. Faz sonunda red-team et:
   - KEEL frame leakage var mı,
   - tool/framework anchoring var mı,
   - research scope unbounded mı,
   - missing dimension var mı,
   - evidence type yanlış claim'e terfi etmiş mi.

## Açık riskler

- **frame inheritance:** geçmiş failure haritasını SOUL'un tamamı sanmak;
- **research inflation:** her ilginç soruyu research requirement yapmak;
- **evidence mismatch:** popularity/similarity/history'yi causal necessity diye kullanmak;
- **derived-view omission:** sentezde karşı-kanıt veya bilinmeyen trigger'ı gizlemek;
- **premature requirement:** research signal'i requirement'a çevirmek;
- **architecture leakage:** soru haritasına mechanism/role/tool cevabı gömmek;
- **single-domain overfit:** software-development deneyimini general-purpose system formation diye genellemek;
- **false independence:** fresh same-model review'u independent ground truth saymak.

## Yeni oturumda devam

1. fresh canonical `AGENT.md` + routing protocols,
2. `research/soul-context/README.md`,
3. bu `STATE.md`,
4. `notes/research-to-architecture-boundary.md`,
5. `repos/soul/README.md`,
6. Faz-8: foundation outcome/property extraction ile devam.

## Henüz yapılmaması gerekenler

- SOUL architecture önermek.
- KEEL mechanisms = SOUL requirements eşitliği kurmak.
- Research finding'i requirement/feature/backlog item yapmak.
- Technology/framework selection'a geçmek.
- Same-model verifier/reviewer'ı true independent ground truth saymak.
- Provisional research package/stopping rule'u canonical kabul etmek.
- Phase 1–3 work package yokken roadmap description'ı operational evidence gibi sunmak.