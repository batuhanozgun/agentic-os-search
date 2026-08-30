# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 8 — SOUL Research question / evidence-dimension map — REVISED TAXONOMY VALIDATION  
**Son güncelleme:** 2026-08-30

> Bu dosya canonical **çalışma durumu ve next-action pointer**'ıdır; araştırma corpus'u değildir. Ayrıntılı kanıt ve muhakeme ilgili `notes/` ve repo defterlerinde yaşar.

## Ana hedef

SOUL'un neden yeniden kurulduğunu, önceki çalışma/ürün deneyimlerinden hangi problem sınıflarının açığa çıktığını ve **SOUL mimarisine geçmeden önce araştırılması gereken genel problem/evidence alanlarını** kanıta dayalı biçimde çıkarmak.

Bu çalışma SOUL mimarisi önermeyecek. Research output ile architecture decision ayrı tutulacak.

## Kaynak rolleri

### Omurga

- `soul`: birincil SOUL intent + Development OS + work/verification/review evidence.
- `os-architect`: tarihsel arıza, yöntem, araştırma, sahip düzeltmeleri ve KEEL'in üst-seviye yeniden değerlendirilmesi.
- `keel`: somut mekanizma/runtime yüzeyi; tarihsel iddiaların bugünkü mekanik karşılığını sınamak için.

### Sınırlı predecessor source

- `keel-research`: yalnız SOUL'un kendi source chain'i doğrudan işaret ettiğinde prior-art/evidence; SOUL authority veya dördüncü omurga kaynak değil.

## Tamamlanan ana geçişler

### A–D — predecessor problem / method / mechanism reconstruction

Doğrulanan ana failure alanları:
- depo/temsil ve source/view drift,
- çalışma-döngüsü / continuity / responsibility,
- epistemik süreç / correlated verification,
- amaç/framing kaybı,
- lesson→need-time köprüsü.

KEEL seçici mekanik karşı-okumasında state guards, hook wiring, role cage, verifier/card closure ve mutation-test definitions görüldü. Fresh execution üretilmedi; test definition ile current PASS ayrı tutuluyor.

Detay:
- `repos/os-architect/README.md`
- `repos/keel/README.md`

### E — KEEL → SOUL transition

2026-08-08..13 problem yalnız product-bug düzeyinde kalmadı; framing, intended outcome, work selection, verification, lesson retrieval ve system-level reasoning alanlarına çıktı.

2026-08-11 owner direction: `araştırma evi kurulacak`; research sonraki yeni geliştirme çalışmasına girdi olacak.

2026-08-25 SOUL bootstrap / Development OS:
- first-principles general-purpose system formation,
- product architecture Phase-0 non-scope,
- KEEL mapping / technology / runtime seçimleri ertelenmiş,
- predecessor lessons SHA-level evidence synthesis üzerinden SOUL-specific design'e taşınmış.

Detay:
- `notes/transition-to-soul.md`
- `repos/soul/README.md`

### F — Research ↔ Architecture boundary

Direct SOUL governance'tan doğrulandı:
- research ≠ decision,
- evidence package architecture truth ilan etmez,
- material findings auto-repair/backlog değildir,
- architecture commitment ayrı decision/work-selection/review path ister,
- prior art default architecture değildir,
- technology selection later phase'tir.

Bu geçiş tamamlandı.

## Faz 8 — dimension-map araştırması

### Stage 1 — foundation extraction

SOUL foundation/property surface'inden D1–D9 çıkarıldı.

Kritik ayrım:

**Foundation constraint ≠ research popularity question.**

Research current non-negotiable/property'leri sessizce oylamaz; contradiction/impossibility bulursa decision path için counter-evidence üretir.

### Stage 2 — historical-failure red team

Internal failure corpus D1–D9'a zorla map edilmedi.

İki bağımsız gap:
- static state survives but work movement/responsibility/next action does not;
- material result auto-routes to repair-shaped work.

Bunlar ilk aşamada geniş bir D10 `work selection / decomposition / orchestration / lifecycle` üretti.

### Stage 3 — external holdouts S1–S3

- **S1 NASA decision analysis:** D1/D4/D5 + work-selection/depth; value-of-information stopping.
- **S2 Cochrane/PRISMA:** D3/D5/D8 + search selection/stopping; source/entity/report distinction; no universal saturation rule.
- **S3 NIST/FEMA operations:** dynamic external state, situational awareness, operational periods, plan→execute→revise; D3 widened and old-D10 replanning pressure aldı.

Detay:
- `notes/scenario-holdout-matrix.md`

### Stage 4 — pre-architecture scope cut

Binary P0/P1 split reddedildi.

Doğru model:

**Her dimension Phase 1–3 öncesinde minimum bir modele ihtiyaç duyar; gerekli derinlik gate-dependent'tir.**

Implementation detail Phase 4+ alanlarına defer edilir.

Detay:
- `notes/prearchitecture-research-scope.md` — **Stage-5 öncesi D1–D10 baseline; D10/D11 + revised D6 için consolidation gerekiyor.**

### Stage 5 — taxonomy discrimination red-team

Amaç: dimensions gerçekten discriminating protected property mi, yoksa elastik catch-all mı?

Uygulananlar:
- omission test,
- overlap / distinguishing-counterexample test,
- control-loop counter-frame,
- roadmap-leak test,
- fourth external holdout,
- explicit negative-boundary test.

#### S4 — FAA aviation safety / physical operations

Property-first observations:
- operational decision içinde prospective hazard/risk,
- failure öncesi risk assessment,
- unacceptable risk → control/mitigation,
- continued-effectiveness assurance,
- changing operational environment,
- explicit risk authority/accountability,
- competency/lessons,
- consequence/risk-proportional control.

Result:
- ayrı `safety` dimension henüz gerekmedi;
- **D6 post-hoc failure dili dar çıktı → hazard/risk precursor surface eklenmeli**;
- V2 physical consequence/irreversibility ile güçlendi;
- Roadmap Phase-3 `Failure Model` wording'i hazard precursor coverage açısından research counter-evidence aldı; otomatik roadmap edit yok.

#### Old-D10 split

Old D10 iki bağımsız protected property taşıyordu:

1. **what work next?**
2. **how selected work progresses?**

Counterexamples:
- correct next work + broken progression/handoff;
- robust lifecycle + wrong substantive routing.

Independent support:
- historical auto-repair routing vs continuity/responsibility-loss failures,
- NASA work-selection/depth,
- FEMA/NIST lifecycle/replanning,
- SOUL Definition Genesis vs Runtime separation.

**Provisional correction: D10 → D10 + D11.**

#### D2 negative boundary

D2 owns capability/function necessity, coverage and task-specific composition requirements.

D2 does **not** own:
- next-work selection (D10),
- execution/handoff/replanning (D11),
- evidence sufficiency (D5),
- capability admission/evolution (D7),
- authority (D4),
- stable-core placement (D9).

#### D6 negative boundary

D6 owns hazard/failure/control/recovery/liveness semantics.

D6 does **not** automatically absorb:
- stale information (D3),
- wrong next-work choice (D10),
- routine progression/handoff (D11),
- proof/completion validity (D5),
- future-system admission/evolution (D7),
- risk acceptance authority (D4).

#### D11 negative boundary

D11 owns progression/continuity of **already selected** work.

D11 does **not** own:
- objective definition (D1),
- what substantive work to choose next (D10),
- capability necessity (D2),
- authority (D4),
- verification/completion (D5),
- hazard/failure control semantics (D6),
- evolution (D7),
- core placement (D9).

#### D8 result

D8 remains separate:
- correct/fresh truth can exist without reconstructability;
- rich visible trace can exist over stale/wrong truth.

SOUL foundation independently makes observability part of correctness.

Detailed Stage-5 notes:
- `notes/taxonomy-red-team-2026-08-30.md`
- `notes/dimension-boundary-test-2026-08-30.md`

## Current provisional dimension set — D1–D11

1. **D1 — Intended outcome → bounded work definition**
2. **D2 — Capability/function necessity, coverage and task-specific composition requirements**
3. **D3 — Internal/external state, memory, context, knowledge and retrieval**
4. **D4 — Authority, bounded agency and human governance**
5. **D5 — Evidence, provenance, verification and completion**
6. **D6 — Hazard/failure representation, prevention, containment, recovery and liveness**
7. **D7 — Learning, controlled evolution and capability admission**
8. **D8 — Observability and reconstructability**
9. **D9 — Core invariant ↔ task-specific system / system boundary**
10. **D10 — Work selection, decomposition, prioritisation and reasoning depth**
11. **D11 — Work lifecycle, orchestration, continuity and replanning**

Cross-cutting validation axes:
- **V1 — Domain transfer / scenario diversity**
- **V2 — Risk / materiality / proportionality / value of information**
- **V3 — Source/view fidelity / omission awareness**

## Current validity judgement

### Changed under challenge

- D1–D9 → D1–D10 after internal failure red-team.
- D3 widened after external operations holdout.
- universal stopping rule → method/risk/decision-sensitive stopping.
- binary P0/P1 scope → gate-dependent minimum depth.
- **D1–D10 → provisional D1–D11** after discrimination red-team.
- **old D10 split → D10 work-selection + D11 work-lifecycle.**
- **D6 widened → prospective hazard/risk + failure/control.**
- **D2 narrowed with explicit anti-catch-all boundary.**
- D8 survived attempted demotion to validation axis.
- V1–V3 survived S4; no V4 yet.

### Not established

- D1–D11 completeness,
- architecture mechanisms,
- causal optimality of external-domain processes,
- four holdouts = generality proof,
- formal canonical Research package schema,
- formal canonical stopping/promotion gate,
- true model-level independence,
- whether SOUL Roadmap Phase 3 should formally include hazard/risk precursors.

## Current provisional research stopping principle

Not canonical:

**Continue while a material uncertainty remains for which plausible additional evidence could change the authorised next-work/design decision enough to justify evidence-collection cost/delay. Stop or defer when remaining uncertainty is decision-insensitive at the required risk level, when the relevant research method's stopping/completeness tests are satisfied, or when the uncertainty requires a different method/phase rather than more of the same search.**

Every package should preserve stopping rationale + residual uncertainty.

## Şimdi — next Phase-8 gate

Highest-information question:

**Is there a specific materially different frame that D1–D11 has not yet been attacked with, or would adding more holdouts now be source-count ritual rather than decision-relevant evidence?**

### Candidate remaining frame risks

Do not add a fifth holdout by default. First test whether any of these can plausibly change the map:

- strategic / multi-stakeholder interaction with partially conflicting incentives,
- embodied resource production / irreversible physical transformation,
- market/transaction work with external actors and incentive/trust boundaries.

### Next actions

1. Evaluate candidate frame risks against current S1–S4 coverage and SOUL's intended generality.
2. Add **one** fifth holdout only if a candidate has a credible path to exposing a new protected property or falsifying a current boundary.
3. If no fifth holdout is justified, consolidate:
   - `notes/research-dimension-map.md` → D1–D11,
   - `notes/prearchitecture-research-scope.md` → revised D6 + split D10/D11.
4. Then derive bounded per-dimension research packages:
   - exact question,
   - evidence class,
   - strongest falsifier,
   - stopping condition,
   - residual uncertainty,
   - explicit non-proof.
5. Run final architecture-leak review before any Phase-8 freeze.

## Açık riskler

- taxonomy elasticity,
- roadmap circularity,
- predecessor-frame inheritance,
- research inflation,
- historical/prior-art evidence promoted to causal necessity,
- source/view omission,
- architecture leakage into research questions,
- domain overfit,
- false verifier independence,
- safety/hazard language turning D6 or V2 into catch-all buckets.

## Yeni oturumda devam

1. fresh `AGENT.md` + triggered protocols,
2. `research/soul-context/README.md`,
3. this `STATE.md`,
4. `notes/taxonomy-red-team-2026-08-30.md`,
5. `notes/dimension-boundary-test-2026-08-30.md`,
6. inspect candidate remaining frame risks; justify or reject S5,
7. only then consolidate the older dimension/scope notes.

## Henüz yapılmaması gerekenler

- SOUL architecture veya mechanism önermek.
- D1–D11'u canonical kabul etmek.
- KEEL mechanisms = SOUL requirements eşitliği.
- Research finding'i requirement/feature/backlog item yapmak.
- Technology/framework selection.
- External domain guidance'ı agentic effectiveness proof saymak.
- Provisional stopping/package modelini canonical governance kabul etmek.
- FAA SMS process/roles'u SOUL safety architecture diye kopyalamak.
- Phase-3 roadmap wording'ini research finding üzerinden otomatik değiştirmek.