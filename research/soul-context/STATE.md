# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 8 — SOUL Research question / evidence-dimension map — EXTERNAL HOLDOUT + SCOPE RED-TEAM  
**Son güncelleme:** 2026-08-30

## Ana hedef

SOUL'un neden yeniden kurulduğunu, önceki çalışma/ürün deneyimlerinden hangi problem sınıflarının açığa çıktığını ve **SOUL mimarisine geçmeden önce araştırılması gereken genel problem/evidence alanlarını** kanıta dayalı biçimde çıkarmak.

Bu çalışma SOUL mimarisi önermeyecek. Research output ile architecture decision ayrı tutulacak.

## Kaynak rolleri

### Omurga

- `soul`: birincil SOUL intent + Development OS + work/verification/review evidence.
- `os-architect`: tarihsel arıza, yöntem, araştırma, sahip düzeltmeleri ve KEEL'in üst-seviye yeniden değerlendirilmesi.
- `keel`: somut mekanizma/runtime yüzeyi; tarihsel iddiaların bugünkü mekanik karşılığını sınamak için.

### Sınırlı first-party predecessor source

- `keel-research`: yalnız SOUL'un kendi WP/source chain'i doğrudan işaret ettiğinde prior-art/evidence; SOUL authority veya dördüncü omurga kaynak değil.

## Tamamlanan geçişler — özet

### A — çalışma düzeni / araştırma yöntemi

- depo/temsil failure,
- çalışma-döngüsü failure,
- epistemik süreç failure
ayrıldı.

### B — KEEL problem / evidence modeli

Gözlenen arıza, ölçüm/tatbikat, tasarım hükmü ve dış yakınsama ayrıldı. KEEL mekanizmalarının önemli kısmının gerçek arıza→sertleştirme döngüsünden doğduğu görüldü; davranış/epistemik etkilerde kanıt gücü daha sınırlı.

### C — önceki araştırma / dış-göz

Doğrulanan temalar:
- soru ≠ görev,
- amaç/öncül yeniden türetme,
- uzman–sahip asimetrisi,
- session result taşırken purpose/reason kaybı,
- `soru üretici + tetik + kanıt zinciri`,
- ders→ihtiyaç köprüsü.

Geçmiş altı-kalem programın 3–5 kalemleri için tamamlanmış ayrı koşu yok; araştırılmış sayılmıyor.

### D — KEEL seçici mekanik karşı-okuma

Hook wiring, fail-closed state parser, role/write cage, read-only verifier yüzeyi, fresh-card closure ve mutation-test definitions görüldü. Fresh execution bu oturumda üretilemedi; test definition ile current PASS ayrı tutuluyor.

### E — KEEL → SOUL transition

2026-08-08..13'te problem product-bug düzeyinden sistem-üstü framing/goal/work-selection/verification/lesson-retrieval düzeyine çıktı.

2026-08-11 owner direction: `araştırma evi kurulacak`, araştırmalar sonraki yeni geliştirme çalışmasına girdi olacak.

2026-08-25 SOUL bootstrap + Phase-0 Development OS:
- first-principles general-purpose `system formation`,
- product architecture Phase-0 non-scope,
- KEEL mapping/technology/runtime seçimleri ertelenmiş,
- predecessor lessons explicit SHA-level evidence synthesis üzerinden SOUL-specific design'e taşınmış.

### F — Research ↔ Architecture boundary — TAMAMLANDI

Direct SOUL governance:
- `Research is not decision`;
- Researcher evidence kurar, architecture truth ilan etmez;
- Evidence package `what this does NOT prove` taşır;
- architecture commitment ADR/work-selection/independent review üzerinden geçer;
- KEEL evidence/prior art, default schema değil;
- technology choice Phase 11'e kadar ertelenir.

WP-006 PASS + WP-007 `Requires repair` gösterdi:
**spec conformance verification ≠ adversarial/frame robustness**.

WP-021/022 ve pre-build review gösterdi:
- material finding auto-repair olmamalı;
- work selection ayrı problem;
- research evidence-gap driven olmalı;
- historical replay ≠ generalisation;
- review ≠ replay;
- bundled treatment component necessity kanıtı değildir;
- selective context omission-aware olmalı;
- rollback claim lifecycle contract ister;
- acceptance authority circular/unowned olamaz.

`keel-research/PROMOTION.md` tarihsel prior-art olarak aynı high-level ayrımı taşıyor: research epistemik sinyal üretir, backlog/ürün işi otomatik üretmez. Bu SOUL authority değil.

## Faz 8 — yapılan işler

### Stage 1 — foundation extraction

SOUL primary foundation tekrar okundu:
- `VISION.md`
- `DEFINITION.md`
- `SUCCESS_CRITERIA.md`
- `NON_NEGOTIABLES.md`
- `ROADMAP.md`

Önemli ayrım:

**Foundation constraint ≠ research popularity question.**

Örneğin repository state'in chat memory'den üstün olması, producer self-certification'ın yetersizliği, bounded authority, failure representability ve domain leakage yasağı current non-negotiable/property'dir. Research bunları sessizce oylamaz; contradiction/impossibility bulursa proper foundation-decision path için counter-evidence üretir.

Stage-1 foundation clustering D1–D9 üretti.

### Stage 2 — historical-failure red team

Known KEEL/os-architect/SOUL failure corpus, D1–D9'a zorla map edilmedi.

İki failure class açık gap gösterdi:
- static state survives but work movement/responsibility/next action does not;
- material result auto-routes to repair-shaped work.

Bu nedenle **D10 — Work selection / decomposition / orchestration / lifecycle** eklendi.

### Current ten dimensions

1. **D1 — Intended outcome → bounded work definition**
2. **D2 — Task-specific system formation / capability derivation**
3. **D3 — Internal/external state, memory, context, knowledge, retrieval**
4. **D4 — Authority / bounded agency / human governance**
5. **D5 — Evidence / provenance / verification / completion**
6. **D6 — Failure representation / containment / recovery / liveness**
7. **D7 — Learning / controlled evolution / capability admission**
8. **D8 — Observability / reconstructability**
9. **D9 — Generality / domain transfer / task-specific architecture**
10. **D10 — Work selection / decomposition / orchestration / lifecycle**

Independent note:
- `notes/research-dimension-map.md`

### Stage 3 — external/domain holdout

Internal corpus haritayı hem üretip hem doğrulamasın diye üç external holdout family seçildi.

#### S1 — analytical decision support

Primary source: NASA Systems Engineering Handbook / Decision Analysis.

Observed properties:
- intended outcome + decision context,
- criteria + alternatives,
- uncertainty/sensitivity,
- explicit decision authority,
- risk/consequence-proportional analysis depth,
- value of reducing uncertainty versus cost/delay.

Result:
- new core dimension zorlamadı;
- D1/D4/D5/D10'u bağımsız biçimde destekledi;
- stopping rule'u güçlendirdi: more research yalnız uncertainty reduction downstream decision'ı credibly değiştirebilecek ve maliyetine değecekse gerekçeli.

#### S2 — systematic evidence synthesis

Primary/authoritative sources: Cochrane Handbook current Chapter 4 + PRISMA 2020 official reporting guidance.

Observed:
- study/entity ≠ multiple reports/representations,
- search completeness/method documentation,
- stopping method/context/evidence scarcity dependent,
- relative recall/citation search/saturation gibi farklı completion evidence'ları,
- stopping rationale must be documented.

Result:
- universal saturation/source-count stopping rule reddedildi;
- D3/D5/D8/D10 güçlendi;
- source coverage / omission trace ihtiyacı güçlendi.

#### S3 — dynamic incident/operations

Primary/authoritative sources: NIST SP 800-61 Rev.3 + FEMA NIMS/Incident Action Planning.

Observed:
- dynamic external state,
- ongoing situational awareness,
- operational periods,
- plan → execute → evaluate → revise,
- changing conditions shorten plan validity,
- resource/accountability state,
- lessons/improvement can feed while operations continue.

Result:
- yeni dimension henüz gerekmedi;
- **D3 wording internal-repo centric idi; external-world state freshness/validity eklenmeli**;
- **D10 static backlog gibi okunmamalı; assumption-invalidating external change → replan içermeli**.

Independent note:
- `notes/scenario-holdout-matrix.md`

### Stage 4 — pre-architecture scope cut

İlk `P0/P1` priority split red-team'de reddedildi.

Roadmap exact gate dili:
- Phase 1 doğrudan lifecycle, completion, autonomy/human governance ve system boundary ister;
- Phase 2 missing-capability governance dahil complete capability map ister;
- Phase 3 her failure'ı observable signal + prevention/detection/containment/recovery/regression + control ownership'e bağlar.

Bu nedenle doğru model:

**all D1–D10 need a minimum pre-architecture model; required depth is gate-dependent.**

- Phase 1 direct surface: D1, D4, D5, D7, D9, D10; D2/D3/D6/D8 enough to avoid hidden assumptions.
- Phase 2: D2/D9 central but capabilities must cover properties implied by all D1–D10.
- Phase 3: D6 central but failure analysis attacks all D1–D10 and needs their observable/control semantics.

Detailed implementation architecture remains Phase 4–10.

Independent note:
- `notes/prearchitecture-research-scope.md`

## Current provisional research stopping principle

Not canonical yet:

**Continue while a material uncertainty remains for which plausible additional evidence could change the authorised next-work/design decision enough to justify evidence-collection cost/delay. Stop or defer when remaining uncertainty is decision-insensitive at the required risk level, when the relevant research method's stopping/completeness tests are satisfied, or when the uncertainty requires a different method/phase rather than more of the same search.**

Every package should preserve stopping rationale + residual uncertainty.

## Current research-output hypothesis — NOT canonical schema

Decision-oriented evidence package may need:
- exact question / downstream decision dimension,
- material uncertainty,
- observation/inference/assumption,
- primary source/version,
- conflicting evidence/alternatives,
- source quality/coverage/known omissions,
- supported claim,
- explicit non-proof,
- capability/failure/control-property hypothesis,
- alternative frame/layer,
- strongest falsifier,
- causal necessity identified or not,
- residual uncertainty + what evidence would change the decision,
- decision relevance without embedded architecture verdict.

## Faz-8 mevcut validity status

### What changed under challenge

- D1–D9 → **D1–D10** after internal failure red-team.
- D3 widened after external operations holdout.
- D10 widened to external-state-triggered replanning.
- one global stopping rule → method/risk/decision-sensitive stopping.
- binary P0/P1 scope → gate-dependent minimum depth.

### What has NOT been established

- D1–D10 completeness;
- any architecture mechanism;
- causal optimality of NASA/Cochrane/NIST/FEMA processes;
- three holdouts = proof of SOUL generality;
- formal canonical SOUL Research package schema;
- formal canonical stopping/promotion gate;
- true model-level independence.

## Şimdi — next Phase-8 adversarial gate

Highest-information question:

**Are D1–D10 genuinely discriminating dimensions, or have some been written broadly enough that any missing problem can be made to fit after the fact?**

### Next actions

1. **Omission test:** for each external holdout, name the domain property first, then map it to D1–D10; flag any property that requires reinterpretation/stretching.
2. **Overlap test:** identify dimensions whose stopping/evidence obligations cannot be distinguished in practice; merge only if protected properties really coincide.
3. **Counter-frame test:** ask whether a materially different top-level organisation (e.g. decision lifecycle / information lifecycle / control loop) explains the same evidence with fewer arbitrary categories.
4. **Roadmap-leak test:** identify dimensions that exist only because current SOUL roadmap names a later architecture phase; demand independent property/failure evidence for them.
5. **Scope-stop test:** for each D1–D10 derive the smallest pre-Phase1/2/3 research question set; anything else routes later.
6. If D1–D10 survive, then derive formal **research question inventory + evidence class + falsifier + stopping condition** per dimension.

## Açık riskler

- **taxonomy elasticity:** dimensions become unfalsifiably broad;
- **roadmap circularity:** research map merely mirrors roadmap;
- **frame inheritance:** predecessor failures become whole SOUL problem space;
- **research inflation:** every interesting subtopic becomes pre-architecture blocker;
- **evidence mismatch:** historical/prior-art evidence promoted to causal necessity;
- **derived-view omission:** synthesis hides counter-evidence or unknown-needed sources;
- **architecture leakage:** role/tool/mechanism answers embedded into research questions;
- **single-domain overfit:** general-purpose claim inferred from agent/software work;
- **false independence:** same-model review treated as independent ground truth.

## Yeni oturumda devam

1. fresh `AGENT.md` + triggered protocols,
2. `research/soul-context/README.md`,
3. this `STATE.md`,
4. `notes/research-dimension-map.md`,
5. `notes/scenario-holdout-matrix.md`,
6. `notes/prearchitecture-research-scope.md`,
7. run omission/overlap/counter-frame red-team.

## Henüz yapılmaması gerekenler

- SOUL architecture veya mechanism önermek.
- D1–D10'u canonical kabul etmek.
- KEEL mechanisms = SOUL requirements eşitliği.
- Research finding'i requirement/feature/backlog item yapmak.
- Technology/framework selection.
- External domain guidance'ı agentic effectiveness proof saymak.
- Provisional stopping/package modelini canonical governance kabul etmek.