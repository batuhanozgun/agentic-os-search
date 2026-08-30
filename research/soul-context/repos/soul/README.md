# soul — okuma defteri

Repo: `batuhanozgun/soul`  
Rol: SOUL'un current explicit intent'i + Development OS'nin birincil kuruluş/işletim kanıtı  
Okuma stratejisi: `main` intent anchor → yüksek-bilgi çalışma dalı → foundation → work/verification/review → yalnız araştırma niyetini değiştiren sonraki kanıt

## Düzeltme: repo yalnız `main` değildir

İlk okumada default `main` dalında yalnız `README.md` görülmüş ve repo küçük kabul edilmişti. Bu hüküm yalnız `main` görünümü için doğrudur.

Dal taraması sonrasında çok sayıda `work/*`, `verify/*`, `review/*`, `audit/*` ve özellikle `phase0/development-os` dalı bulundu. Bu nedenle SOUL artık yalnız explicit-intent anchor değil, SOUL'un kendi geliştirme işletim sistemine dair **birincil araştırma kaynağıdır**.

## Okuma kaydı — `main`

| Kaynak | SHA / commit | Tür | Maddi bulgu |
|---|---|---|---|
| `README.md` | `9dbded30` | full | SOUL first principles'tan genel amaçlı agentic architecture olarak yeniden kuruluyor; intended outcome → controlled, verifiable working system; `development/` ile `system/` ayrı; ilk paket Development OS |
| bootstrap commit | `7b2a9a4` | full diff | 2026-08-25'te yalnız README ile bilinçli yeniden başlangıç |

## Okuma kaydı — `phase0/development-os`

### Development OS amacı

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `development/README.md` | `e6a87f70` | full | SOUL geliştirmesini session length/context loss/model memory/single-model self-evaluation/undocumented decisions/unverified output'tan bağımsızlaştırmak; fresh session repo state'inden cold-start edip bounded work + evidence + handoff yapabilmeli |
| `development/00_foundation/VISION.md` | branch current | full | SOUL preset workflow/team/template değil; intended outcome için gereken çalışma sistemini kurabilen general-purpose agentic system |
| `development/00_foundation/DEFINITION.md` | branch current | full | SOUL'un işi `system formation`: outcome'u anla → gereken sistemi belirle → capability'leri kur/organize et → işlet → doğrula → adapt et → continuity/governance/state'i koru |
| `development/00_foundation/NON_NEGOTIABLES.md` | branch current | full | outcome-first, least privilege, independent verification, evidence-before-closure, explicit external state, governed capability acquisition, repair/adaptation, no hidden owner orchestration, fail-visible, scale-appropriate control, durable traceability |
| `development/00_foundation/SUCCESS_CRITERIA.md` | branch current | full | cold-session reconstructability, governance-before-product architecture, failed verification blocks closure, unresolved decisions visible, missing capability governance, recovery/adaptation, low hidden-owner orchestration, unbounded governance growth yok |

### İlk work/verification zinciri

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `development/04_work/WP-000-DEVELOPMENT-OS.md` | `6f5042ec` | full | Amaç: SOUL'u uzun fresh-session'larda tek chat/model memory/producer self-certification'a bağlı olmadan tasarlayacak durable repo OS. Böyle bir disiplin kurulmazsa SOUL, kontrol etmeyi hedeflediği aynı agentic failure class'ları kendi geliştirmesinde yeniden üretir. KEEL klasörlerini yeni sisteme map etmek ve ürün mimarisi Phase 0 non-scope |
| `development/04_work/WP-001-PHASE0-VERIFICATION.md` | `5f0b5bf3` | full | fresh verifier WP-000'ı exact commit'e karşı bağımsız değerlendirmekle görevli; verifier repair yapamaz; tarihsel sonuç `FAIL` |
| `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md` | `d95f4507` | full | İlk gerçek verification iki kusurla FAIL: cold-start mandatory read-order'ları birbirini tutmuyor; `NEXT_SESSION.md` current WP bilgisini stale duplicate olarak taşıyor. 9/11 criterion PASS olsa da criterion 1–2 FAIL olduğu için overall FAIL korunmuş |

### Öncül repoların SOUL'a açık aktarımı

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md` | `fa9b281e` | full | KEEL-Work, keel-dev, oyun2, os-architect ve keel-research kaynakları SHA'larıyla okunmuş; source-derived principles ile SOUL-specific synthesis decisions ayrı tutulmuş |

Bu synthesis'in doğrudan taşıdığı tekrar eden ilkeler:

1. project truth chat/model memory dışında yaşar;
2. objective/method/state/evidence/decision authority ayrılır;
3. observation/inference/assumption/verified result ayrılır;
4. producer confidence/tool success/repeated-model agreement/retrieved content proof değildir;
5. mevcut plan/mekanizma/tool ayrıcalıklı default değil, hipotezdir;
6. material architecture framing/necessity/alternative-layer/falsification testinden geçer;
7. owner value/scope ile teknik araştırılabilir karar ayrılır;
8. failure'da hem immediate defect hem neden anticipate/prevent/detect edilemediği incelenir;
9. mümkünse öğüt yerine observable trace/mechanical control;
10. risk/ambiguity/novelty/irreversibility ile orantılı derin reasoning;
11. independent verification + exact-target freshness;
12. decision-relevant rationale/evidence kaydedilir, private chain-of-thought istenmez.

SOUL'a özgü synthesis bunları mekanik olarak kopyalamıyor; tek canonical reasoning policy, tek cold-start sequencing authority, trigger-based deeper checks ve architecture/failure/provenance kontrolleri gibi yeni tasarım seçimlerine dönüştürüyor.

## Phase 7 — research → architecture boundary

### Governance sınırı

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `development/01_governance/DECISION_POLICY.md` | `d26c1739` | full | Explicit: **Research is not decision**. External evidence SOUL'a otomatik doğru seçim olmaz; architecture decision ADR + independent review, foundation decision daha güçlü gate ister |
| `development/05_evidence/EVIDENCE_TEMPLATE.md` | `ecbdb486` | full | Evidence: question, exact source/method, supported findings, quality/limitations, `what this does NOT prove`, decision relevance. Evidence dosyası proper decision process olmadan architecture decision ilan edemez |
| `development/01_governance/ROLE_MODEL.md` | `f1b704bf` | full | Researcher evidence kurar; conflicting evidence'i saklayamaz ve finding'i sessizce architecture decision'a çeviremez. Designer, Verifier, Adversarial Reviewer, Integrator ve Human Owner ayrı authority/motivation taşır |
| `development/01_governance/REASONING_POLICY.md` | `94f5368e` | full | Primary/authoritative sources, date/version freshness, disagreement/limitations, similarity≠equivalence, popularity≠quality, tool/framework≠problem definition, analytical provenance `claim→method→inputs→source/version`; completion condition karşılandıysa sırf daha fazla bilgi var diye research açık tutulmaz |
| `development/02_architecture/README.md` | `a0a0d63a` | full | KEEL **evidence/prior art**, default SOUL schema değil. Bir mekanizma ancak yeni tasarımda required capability/property'ye bağlanırsa taşınabilir |
| `development/03_plan/ROADMAP.md` | `831d34dd` | full | Phase 1 Definition → Phase 2 capability map without KEEL organisation → Phase 3 failure taxonomy/control ownership; technology choices ancak Phase 11. Erken research framework-selection değil problem/capability/failure evidence beslemeli |

### Reasoning-policy verification ve ayrı adversarial challenge

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `WP-005-DEVELOPMENT-REASONING-POLICY.md` | `74240dfd` | full | predecessor synthesis'ten canonical reasoning policy üretildi; builder checks proof değil; independent verification + adversarial review ayrı kalıyor |
| `WP-006-PHASE0-REASONING-REVERIFICATION.md` | `71736914` | full | exact-target verification tüm current kriterlerde PASS; fakat bu Phase/ADR acceptance değil ve ayrı adversarial review hâlâ zorunlu |
| `WP-007-PHASE0-ADVERSARIAL-REVIEW.md` | `1be6e582` | full | WP-006 PASS sonrasında yeni F-AR-001 bulundu; overall `Requires repair`. Sonuç: conformance PASS, frame/failure robustness yerine geçmiyor |

### Work-selection / pre-build lifecycle öğrenimi

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `WP-021-DEVELOPMENT-LIFECYCLE-WORK-SELECTION-IMPROVEMENT.md` | `79442e5e` | full | Material evidence/failure otomatik repair-shaped work olmamalı; doğru next unit of work ayrıca seçilmeli. Research yalnız evidence gap olduğunda açılır, evidence olarak kalır. Repair conclusion olmalı. Pre-build design freeze + independent design challenge + historical replay + synthesis + build-ready design + post-build fresh assurance öneriliyor; current stage design revision |
| `WP-022-WP021-DEVELOPMENT-LIFECYCLE-PREBUILD-ADVERSARIAL-REVIEW.md` | `5fc8d7e0` | full | design implementation'dan önce exact-target adversarial review'a sokulmuş; review ve replay birbirinin yerine geçmez; result `Requires design revision` |
| `PREBUILD-ADVERSARIAL-REVIEW-WP-021-acf6ddc6-2026-08-29.md` | `3926b33e` | full | F-AR-009..012: technical acceptance/finding disposition circular-or-unowned; bundled replay Planner necessity'sini causal identify edemez; selective-context omission detection yok; rollback mitigation contract'sız |

## Phase-7 maddi çıkarımları

### 1. Research → architecture otomatik terfi değildir — DOĞRUDAN

SOUL'un kendi governance'i bu sınırı açıkça tanımlar:

`Researcher/evidence → decision relevance`, fakat **architecture commitment ayrı ADR/work-selection/independent-review state transition'ıdır**.

### 2. Research'in açılma nedeni evidence gap olmalıdır — DOĞRUDAN / WP-021 candidate discipline

WP-021, research'i varsayılan adım değil evidence-gap driven iş olarak konumluyor. Material finding'in next step'i repair, reframe/design, investigation, başka layer için research veya başka authorised path olabilir.

Not: WP-021 henüz accepted governance değildir; bu madde current proposal/process evidence statüsündedir.

### 3. Research evidence türleri birbirinin yerine geçmez — GÜÇLÜ KANIT

- literature/synthesis ≠ causal effectiveness,
- historical replay ≠ generalisation,
- verifier PASS ≠ adversarial robustness,
- same-model convergence ≠ independent ground truth.

### 4. Handoff riskleri

F-AR-009..012, research output'un downstream kullanımında dört özel risk gösteriyor:

- acceptance authority explicit değilse evidence producer self-acceptance veya deadlock üretebilir;
- bundled experiment durable mechanism necessity'sini kanıtlayamaz;
- selective derived context omission-aware değilse compliant actor karşı-kanıdı hiç görmeyebilir;
- rollback/reversibility claims lifecycle semantics olmadan boş güven üretir.

## Şu anda doğrudan söylenebilenler

### SOUL ürününün amacı — BİRİNCİL KAYNAKLA DOĞRULANDI

SOUL'un hedefi bir workflow şablonu veya KEEL'in genel sürümü değildir. Kullanıcının intended outcome'unu alıp **o hedef için gereken kontrollü çalışma sistemini oluşturabilen, işletebilen, doğrulayabilen ve gerçeklik değiştiğinde adapte edebilen genel amaçlı agentic operating architecture** olmaktır.

### Development OS'nin amacı — BİRİNCİL KAYNAKLA DOĞRULANDI

SOUL'u tasarlama süreci, SOUL'un çözmeye çalıştığı failure class'ları kendi içinde yeniden üretmemelidir. Bu nedenle ürün mimarisinden önce repo-authoritative, cold-startable, bounded, independently verified, fail-visible bir development operating system kuruluyor.

### Tarihsel öncüllerle bağ — BİRİNCİL KAYNAKLA DOĞRULANDI

SOUL Phase 0 kendi evidence dosyasında KEEL/os-architect ve diğer öncül alanlardan hangi reasoning/governance ilkelerini aldığını SHA seviyesinde belgeliyor. Bu nedenle bağ yalnız benzerlik veya tarih sırası değil.

### Research ↔ architecture sınırı — BİRİNCİL SOUL KAYNAKLARIYLA DOĞRULANDI

Research SOUL'da ayrı evidence üretim sorumluluğudur; architecture decision değildir. Evidence'in architecture'a etkisi decision/work-selection/ADR ve bağımsız challenge üzerinden kurulmalıdır.

## Açık sorular

- SOUL Research projesinin formal package schema'sı ve stopping rule'u ne olmalı?
- Phase 1 Definition, Phase 2 Capability Architecture ve Phase 3 Failure Model başlamadan hangi **research dimensions/evidence classes** kapsanmalı?
- Research kapsamı nasıl yeterince geniş tutulup unbounded programme'a dönüşmeden kapatılmalı?
- General-purpose iddiasını test etmek için hangi materially different problem domains/scenarios araştırmaya girmeli?
- Selective context omission riskine karşı research handoff hangi provenance/completeness yüzeyini taşımak zorunda?
- Causal necessity hangi iddialarda ablation/experiment gerektirir, hangi iddialarda triangulated evidence yeterlidir?

## Bağımsız sentez notları

- `research/soul-context/notes/transition-to-soul.md`
- `research/soul-context/notes/research-to-architecture-boundary.md`

## Sonraki okuma

Geniş Phase-0 dal tüketimi yapılmayacak. Boundary artık yeterince doğrudan kurulmuştur.

Sonraki yüksek-bilgi işi:

1. foundation + roadmap gates + predecessor failure map'ten Phase 1–3 öncesi **research question/dimension map** türetmek;
2. her boyut için hangi evidence class'ın gerekli olduğunu ve neyin falsifier olacağını ayırmak;
3. bunu architecture proposal'a çevirmeden SOUL Research'ün kapsam/stopping/handoff modelini sınamak.