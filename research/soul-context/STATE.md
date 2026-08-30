# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 8 — SOUL Research question / evidence-dimension map — CONSOLIDATION  
**Son güncelleme:** 2026-08-30

> Canonical çalışma durumu ve next-action pointer. Ayrıntılı araştırma kanıtı `notes/` ve repo defterlerinde yaşar; bu dosya corpus değildir.

## Ana hedef

SOUL'un neden yeniden kurulduğunu, önceki çalışma/ürün deneyimlerinden hangi problem sınıflarının açığa çıktığını ve **SOUL mimarisine geçmeden önce araştırılması gereken genel problem/evidence alanlarını** kanıta dayalı biçimde çıkarmak.

Research output ile architecture decision ayrı tutulacak; bu çalışma mekanizma/teknoloji seçmeyecek.

## Kaynak rolleri

- `soul`: birincil SOUL intent + Development OS + work/verification/review evidence.
- `os-architect`: tarihsel arıza, yöntem, araştırma, sahip düzeltmeleri ve KEEL üst-seviye yeniden değerlendirmesi.
- `keel`: somut mekanizma/runtime yüzeyi; tarihsel iddiaların mekanik karşı-okuması.
- `keel-research`: yalnız SOUL source chain'i işaret ettiğinde sınırlı predecessor prior-art; SOUL authority değil.

## Tamamlanan bağlam geçişleri

### A–D — predecessor reconstruction

Ana problem sınıfları ayrıldı:
- source/view ve state drift,
- work continuity / responsibility,
- epistemik / correlated-verification failure,
- goal/framing loss,
- lesson→need-time failure.

KEEL'de seçici mekanik karşı-okuma yapıldı; fresh execution üretilmedi.

Detay:
- `repos/os-architect/README.md`
- `repos/keel/README.md`

### E — KEEL → SOUL transition

2026-08-08..13 problem product-bug düzeyinden framing, goal, work selection, verification, lesson retrieval ve system-level reasoning düzeyine çıktı.

2026-08-11 owner direction: `araştırma evi kurulacak`; research sonraki yeni geliştirme çalışmasına girdi olacak.

2026-08-25 SOUL bootstrap / Development OS:
- first-principles general-purpose system formation,
- product architecture Phase-0 non-scope,
- KEEL mapping/technology/runtime seçimleri ertelenmiş,
- predecessor lessons explicit evidence synthesis üzerinden SOUL-specific design'e taşınmış.

Detay:
- `notes/transition-to-soul.md`
- `repos/soul/README.md`

### F — Research ↔ Architecture boundary

Direct SOUL governance'tan doğrulandı:
- research ≠ decision,
- evidence architecture truth değildir,
- material finding auto-repair/backlog değildir,
- architecture commitment ayrı decision/work-selection/review path ister,
- prior art default architecture değildir,
- technology selection later phase'tir.

## Faz 8 — taxonomy construction / challenge history

### Stage 1 — foundation extraction

SOUL foundation property surface'inden D1–D9 çıkarıldı.

**Foundation constraint ≠ research popularity question.** Research contradiction/impossibility bulabilir ama current non-negotiable'ı sessizce oylamaz.

### Stage 2 — historical failure red-team

İki gap ilk geniş D10'u doğurdu:
- static state survives but work movement/responsibility/next action does not;
- material result auto-routes to repair-shaped work.

### Stage 3 — external holdouts S1–S3

- **S1 NASA decision analysis:** decision context, authority, uncertainty, work-depth/value-of-information.
- **S2 Cochrane/PRISMA:** source/entity/report, search coverage, method-specific stopping, reconstructable evidence selection.
- **S3 NIST/FEMA operations:** dynamic external state, operational periods, plan→execute→revise, replanning.

Forced changes:
- D3 external-world freshness içerecek şekilde genişledi;
- universal stopping formula reddedildi;
- risk/method/decision-sensitive stopping benimsendi.

Detay:
- `notes/scenario-holdout-matrix.md`

### Stage 4 — pre-architecture scope cut

Binary P0/P1 split reddedildi.

**Her dimension Phase 1–3 öncesinde minimum modele ihtiyaç duyar; gerekli derinlik gate-dependent'tir.**

Baseline note:
- `notes/prearchitecture-research-scope.md` — Stage-5 öncesi D1–D10 sürümü; consolidation gerekiyor.

### Stage 5 — taxonomy discrimination red-team

Applied:
- property-first omission mapping,
- distinguishing counterexamples,
- negative dimension boundaries,
- counter-frame,
- roadmap-leak test,
- physical-operations holdout S4.

#### S4 — FAA aviation safety / physical operations

Observed:
- failure öncesi hazard/risk,
- risk assessment/control,
- continued-effectiveness assurance,
- changing operational environment,
- authority/accountability,
- competency/lessons,
- consequence-proportional control.

Forced changes:
- **D6 post-hoc failure dili dar çıktı → hazard/risk precursor surface eklendi.**
- V2 physical consequence/irreversibility ile güçlendi.
- Roadmap Phase-3 `Failure Model` hazard precursor coverage açısından research counter-evidence aldı; otomatik roadmap edit yok.

#### Old-D10 did not survive

Old D10 two independent properties taşıyordu:
- what work next?
- how selected work progresses?

Counterexamples and external evidence supported split:
- **D10 — work selection / decomposition / prioritisation / reasoning depth**
- **D11 — work lifecycle / orchestration / continuity / replanning**

#### D2 / D6 / D11 negative boundaries

Explicit `must NOT absorb` boundaries written and tested.

#### D8

Remains independent: truth/freshness and reconstructability can fail separately; SOUL foundation also makes observability part of correctness.

Detailed notes:
- `notes/taxonomy-red-team-2026-08-30.md`
- `notes/dimension-boundary-test-2026-08-30.md`

### Stage 6 — S5 external dependency / trust holdout

Reason opened:
S1–S4 mostly assumed one organisation/shared command or broadly cooperative work. Remaining frame risk was critical dependency on actors/artifacts outside system authority under asymmetric information and possible malicious/strategic behaviour.

Sources:
- NIST SP 800-161 Rev.1 update,
- NIST SP 1326 Due Diligence Quick-Start Guide (July 2026).

Observed before mapping:
- external suppliers outside direct authority,
- limited visibility into development/integration and upstream tiers,
- malicious/counterfeit/vulnerable inputs,
- provenance/resilience/ownership-control due diligence,
- multi-tier dependency risk,
- bounded investigative rigor before acquisition.

Result:
- **No D12 yet.** D1–D11 can represent the property surfaces without a new bucket.
- **V1–V3 did not survive.** External dependency/trust asymmetry is not equivalent to domain diversity, risk magnitude or source fidelity.

New validation axis:

### V4 — External dependency / trust / adversarial counterparty exposure

Challenge:

**Do the protected properties and research conclusions still hold when critical actors, tools, services, data or artefacts are outside direct system authority, only partially observable, and potentially unreliable, strategically misaligned or adversarial?**

Detailed note:
- `notes/scenario-holdout-s5-supply-chain-trust.md`

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

## Current provisional validation axes — V1–V4

- **V1 — Domain transfer / scenario diversity**
- **V2 — Risk / materiality / proportionality / value of information**
- **V3 — Source/view fidelity / omission awareness**
- **V4 — External dependency / trust / adversarial counterparty exposure**

## Validity status

### Taxonomy changed under every major challenge

- D1–D9 → D1–D10 after historical failure challenge.
- D3 widened after dynamic operations.
- stopping logic changed after NASA/Cochrane.
- P0/P1 scope model changed after roadmap gate check.
- D1–D10 → **D1–D11** after discrimination test.
- D6 widened after physical-safety holdout.
- D2 narrowed by negative boundary.
- D8 survived attempted demotion.
- V1–V3 → **V1–V4** after external-dependency/trust holdout.

This is evidence against pure confirmation, **not completeness proof**.

### Not established

- D1–D11 completeness,
- V1–V4 completeness,
- any architecture mechanism,
- causal optimality of external-domain processes,
- five holdouts = proof of SOUL generality,
- formal canonical Research package schema,
- formal canonical stopping/promotion gate,
- true model-level independence,
- formal roadmap changes from hazard/trust findings.

## Provisional research stopping principle

Not canonical:

**Continue while a material uncertainty remains for which plausible additional evidence could change the authorised next-work/design decision enough to justify evidence-collection cost/delay. Stop or defer when remaining uncertainty is decision-insensitive at the required risk level, when the relevant research method's stopping/completeness tests are satisfied, or when the uncertainty requires a different method/phase rather than more of the same search.**

Every package should preserve stopping rationale + residual uncertainty.

## Şimdi — consolidation gate

Highest-information question:

**Can the challenged D1–D11 + V1–V4 set be converted into a bounded pre-architecture research inventory without reintroducing architecture answers, duplicate questions or indefinite evidence demands?**

### Next actions

1. Consolidate `notes/research-dimension-map.md` from old D1–D10/V1–V3 to **D1–D11/V1–V4**; preserve history/challenge trail.
2. Consolidate `notes/prearchitecture-research-scope.md`:
   - hazard-aware D6,
   - split D10/D11,
   - V4 challenge obligation.
3. For each D1–D11 derive the smallest pre-Phase1/2/3 research package:
   - exact property question,
   - decision/gate relevance,
   - evidence classes,
   - strongest falsifier/counter-frame,
   - stopping condition,
   - residual uncertainty,
   - explicit `does NOT prove`.
4. Run V1–V4 against each package; a package that cannot state how it is challenged is not ready.
5. Run final overlap + architecture-leak review.
6. Do **not** add more holdouts by count; reopen only when a concrete unmapped frame risk appears.

## Açık riskler

- taxonomy elasticity,
- roadmap circularity,
- predecessor-frame inheritance,
- research inflation,
- prior-art evidence promoted to causal necessity,
- source/view omission,
- architecture leakage,
- domain overfit,
- false verifier independence,
- D6/V2 becoming safety catch-all,
- V4 becoming generic security/trust catch-all.

## Yeni oturumda devam

1. fresh `AGENT.md` + triggered protocols,
2. `research/soul-context/README.md`,
3. this `STATE.md`,
4. `notes/dimension-boundary-test-2026-08-30.md`,
5. `notes/scenario-holdout-s5-supply-chain-trust.md`,
6. consolidate old dimension/scope notes,
7. derive bounded research packages.

## Henüz yapılmaması gerekenler

- SOUL architecture/mechanism önermek.
- D1–D11 veya V1–V4'ü canonical kabul etmek.
- KEEL mechanisms = SOUL requirements eşitliği.
- Research finding'i requirement/feature/backlog item yapmak.
- Technology/framework selection.
- External guidance'ı agentic effectiveness proof saymak.
- Provisional stopping/package modelini canonical governance kabul etmek.
- FAA/NIST process/roles'u SOUL architecture diye kopyalamak.
- Research finding üzerinden roadmap'i otomatik değiştirmek.