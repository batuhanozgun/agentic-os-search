# Core Terms — U06: Dördüncü 10 Terim İçin Bağlantılı İnceleme

**Tarih / erişim:** 2026-09-18.  
**Statü:** kaynak ve kavram incelemesi; v0.3 working reference'ı Work'ün niyetten kanıta giden hattında genişletir. Evrensel sözlük, nihai ontoloji veya SOUL/Development OS tasarımı değildir.  
**Dayanak:** [U03](U03-CORE-TERMS-BATCH1.md), [U04](U04-CORE-TERMS-BATCH2.md), [U05](U05-CORE-TERMS-BATCH3.md), Work Management / Project Control bounded corpus, NIST verification/validation/evidence glossary entries ve güncel OpenAI evaluation material.

## Bu batch neden bu 10 terimi seçti?

v0.3 haritası Work'ün nasıl yürütüldüğünü, kontrol edildiğini ve state'inin nasıl korunduğunu açıklamaya başladı; fakat şu temel zincir açık kaldı:

- Kullanıcının/owner'ın neyi kastettiği ile sistemin açık hedefi aynı şey mi?
- Goal nasıl Plan'a dönüşüyor?
- Plan içindeki ayrı ayrı yönetilebilir Work nesnelerine ne diyeceğiz?
- Bir Work item ne zaman gerçekten başlanabilir?
- “Bitti” demek neyi kanıtlar?
- Verification, Validation ve Evaluation aynı değerlendirme faaliyeti mi?
- Bu değerlendirmelerin dayandığı Evidence nedir?

Bu nedenle dördüncü batch:
**Goal, Intent, Plan, Task / Work item, Dependency, Readiness, Completion, Validation, Evaluation, Evidence**
üzerinden ilerler.

## Kaynak zemini

### Work Management / Project Control study

[U08 Cross-Unit Synthesis](../../research/studies/work-management-project-control/08-CROSS-UNIT-SYNTHESIS.md) ve [U10 Closure](../../research/studies/work-management-project-control/10-CLOSURE-EVALUATION.md) şu ayrımları özellikle koruyor:

- one universal task object yetersizdir;
- hierarchy ≠ dependency;
- relation identity ≠ current control effect;
- planning-ready ≠ logically actionable ≠ workflow-enabled ≠ implementation-ready ≠ session-admitted ≠ dispatch-admissible;
- actor completion signal ≠ work-item closure ≠ aggregate completion ≠ implementation convergence ≠ integrated effect ≠ desired outcome;
- plan/spec completeness ≠ realized state;
- completion signal ≠ verified effect ≠ desired outcome.

Bu batch'te Work item, Dependency, Readiness ve Completion tanımları bu corpus'un üstüne kurulur.

### NIST — Verification / Validation / Evidence

2026-09-18 canlı glossary okumaları:

- Verification: https://csrc.nist.gov/glossary/term/verification
- Validation: https://csrc.nist.gov/glossary/term/validation
- Evidence: https://csrc.nist.gov/glossary/term/evidence
- Assurance evidence: https://csrc.nist.gov/glossary/term/assurance_evidence

NIST/ISO kaynaklı ayrımın bu çalışma için yararlı yönü:
- **Verification**: specified requirements / properties karşılanıyor mu?
- **Validation**: intended use / stakeholder need gerçekten karşılanıyor mu?
- **Evidence**: bir claim hakkında inanç/karar oluşturmayı destekleyen veri/zemin.

Repo local anlamı bunları daha geniş Work/AI bağlamına uyarlayacak; birebir standardizasyon iddiası yoktur.

### OpenAI — Evaluation

2026-09-18 güncel kaynaklar:

- OpenAI Evals: https://evals.openai.com/
- Trustworthy third-party evaluations: https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- Inside OpenAI's in-house data agent: https://openai.com/index/inside-our-in-house-data-agent/

Bu kaynaklar evaluation'ın:
- açık claim/task distribution,
- tested system/environment/harness,
- criteria/rubric/grader,
- validity checks,
- result/score + interpretation

gibi bir değerlendirme tasarımı taşıyabildiğini gösterir.

Evaluation burada yalnız “bir şey doğru mu?” testi olarak değil, belirli criteria altında performans/quality/capability hakkında ölçüm/judgment üreten daha geniş assessment olarak kullanılacaktır.

## 31. Intent

**Çalışma tanımı:**  
> **Intent:** Bir kullanıcı, owner veya Actor'ın ifade ettiği isteğin arkasındaki **asıl yön, amaçlanan anlam ve neden**; henüz tam ölçülebilir hedefe veya Work tanımına çevrilmemiş olabilir.

Intent:
- doğal dilde,
- eksik,
- örtük,
- birbiriyle gerilimli
olabilir.

**Ayrımlar:**
- Intent ≠ Goal. Goal, intent'in daha açık target/outcome ifadesine dönüştürülmüş halidir.
- Intent ≠ Plan. Plan nasıl ilerleyeceğimizi tarif eder.
- Intent ≠ literal request text. Kullanıcının cümlesi intent'i ifade eder ama onun tamamı olmayabilir.
- Intent ≠ inferred motive. Açık dayanak olmadan psikolojik neden uydurulmaz.

Bu local kullanım Goal-method alignment disiplinimizle uyumludur: literal method/request ile intended end goal ayrılabilir.

## 32. Goal

**Çalışma tanımı:**  
> **Goal:** Work'ün yöneldiği, ulaşılması amaçlanan **açık target state, outcome veya başarı koşulu**.

Goal:
- ölçülebilir olabilir ama olmak zorunda değildir;
- birden fazla alt-goal'a ayrılabilir;
- zamanla daha açık hale gelebilir;
- Intent'ten türetilir ama onunla eşit değildir.

**Ayrımlar:**
- Goal ≠ Intent.
- Goal ≠ Plan.
- Goal ≠ success metric. Metric goal hakkında ölçüm sağlar.
- Goal ≠ Completion. Work item'ların bitmesi Goal'e ulaşıldığını garanti etmez.

Work-management corpus'taki “delivery progress ≠ outcome progress” ayrımı bu sınırı destekler.

## 33. Plan

**Çalışma tanımı:**  
> **Plan:** Bir Goal'e ulaşmak için şu anda makul görülen Work decomposition, yaklaşım, sıra, dependency, resource/actor ve kontrol varsayımlarının **önerilen ve revize edilebilir temsili**.

Plan:
- current truth değil, proposed route'tur;
- execution sırasında değişebilir;
- yeni prerequisite/evidence ile revize edilebilir;
- bütün Work'ün aynı anda task listesine indirgenmesini gerektirmez.

**Ayrımlar:**
- Plan ≠ Goal.
- Plan ≠ Work state. Work state current standing'i de içerir; Plan proposed future route'tur.
- Plan ≠ Workflow. Workflow executable/coordination structure olabilir; Plan daha geniş ve daha erken olabilir.
- Plan ≠ realized state.

OpenSpec/Spec Kit/Flowable/Beads corpus'u progressive planning ve living representation sınırlarını destekler.

## 34. Task / Work item

İlk üç batch'te “Work” üst kavram olarak kullanılıyordu; bu turda ayrı ayrı track/assign/control edilebilir birimi adlandırmak gerekiyor.

**Yerel tercih:** çıplak üst terim olarak **Work item** kullanmak; **Task** kelimesini source-local veya gerçekten action-like unit olduğunda kullanmak.

> **Work item:** Daha geniş Work içinde ayrı identity, scope ve standing ile izlenebilen; assign/claim/depend/verify/close/reopen gibi işlemlere konu olabilen yönetilebilir Work birimi.

> **Task:** Bu repo kullanımında genellikle eylem odaklı bir Work item; ancak dış kaynakta farklı lifecycle/semantics taşıyorsa kaynağın anlamı korunur.

**Ayrımlar:**
- Work item ≠ universal Task schema.
- Work item ≠ Plan artifact.
- Work item ≠ Run. Bir Work item birden fazla Run gerektirebilir.
- Work item ≠ Actor assignment.
- Work item ≠ business transaction.

Work-management corpus “task” kelimesinin project work package, human wait state, case item, issue, planning artifact, implementation checklist vb. farklı nesnelere verildiğini gösterir.

## 35. Dependency

**Çalışma tanımı:**  
> **Dependency:** Bir Work item, artefact, decision veya action'ın **başlanabilirliği, geçerliliği, zamanlaması, kapanışı veya anlamlı sonucu** başka bir şeyin durumuna/çıktısına bağlı olduğunda bu bağı taşıyan ilişki.

Dependency türü açık olmalıdır. Örnek:
- prerequisite/blocking,
- temporal predecessor,
- information/artifact requirement,
- closure dependency,
- external condition.

**Ayrımlar:**
- Dependency ≠ hierarchy/decomposition.
- Dependency ≠ mere relation/reference.
- Dependency ≠ provenance.
- Dependency'nin varlığı ile current control effect'i aynı şey değildir.
- “A before B” her zaman blocker değildir.

Work Management U08'deki “relation meaning / current control effect / enforcement point” üçlüsü bu tanımı doğrudan sınırlar.

## 36. Readiness

**Çalışma tanımı:**  
> **Readiness:** Belirli bir Work item/action'ın, **belirli bir sonraki hareket için**, gereken prerequisites, information, authority, capacity, environment ve control conditions açısından kabul edilebilir/başlanabilir durumda olduğuna ilişkin derived standing.

Readiness çıplak boolean olarak kullanılmamalıdır; mümkün olduğunda **“ready for what?”** belirtilir.

Örnek:
- planning-ready,
- logically actionable,
- implementation-ready,
- workflow-enabled,
- session-admitted,
- dispatch-admissible.

**Ayrımlar:**
- Readiness ≠ priority.
- Readiness ≠ open status.
- Readiness ≠ Permission.
- Readiness ≠ Capability.
- Readiness ≠ Goal progress.

Readiness birçok state/relation/condition'dan türetilen standing'dir.

## 37. Completion

**Çalışma tanımı:**  
> **Completion:** Belirli bir Work item, scope veya execution'ın kendi tanımlı lifecycle/acceptance koşulları açısından **artık normal ilerleme gerektirmediğini belirten kapanış standing'i veya claim'i**.

Completion farklı seviyelerde olabilir:
- local actor completion signal,
- Work item closure,
- aggregate completion,
- integration completion.

**Ayrımlar:**
- Completion ≠ Verification.
- Completion ≠ Validation.
- Completion ≠ Goal achievement.
- Completion ≠ desired outcome.
- Completion ≠ irreversible finality; reopen/repair mümkün olabilir.

Bu nedenle çıplak “done” yerine mümkün olduğunda **hangi scope'un ne anlamda complete olduğu** belirtilir.

## 38. Validation

**Çalışma tanımı:**  
> **Validation:** Üretilen result/system/artefact'ın yalnız specified requirements'ı değil, **amaçlanan kullanımda gerçek stakeholder need/Intent/Goal'i karşılayıp karşılamadığını** değerlendirme süreci.

Yerel kısa soru:
> **Doğru şeyi mi yaptık / amaçlanan kullanımda işe yarıyor mu?**

NIST/ISO validation tanımları “specific intended use/application” ve stakeholder needs boyutunu açıkça taşır.

**Ayrımlar:**
- Validation ≠ Verification.
- Validation ≠ Evaluation. Evaluation daha geniş measurement/judgment faaliyeti olabilir.
- Validation ≠ user approval alone. Approval evidence olabilir ama her durumda yeterli değildir.
- Validation ≠ Completion.

## 39. Evaluation

**Çalışma tanımı:**  
> **Evaluation:** Bir Model, Agent, System, Work result veya process'i belirli **criteria, task distribution, rubric, metric veya benchmark** altında sistematik olarak değerlendirip performance/quality/capability/risk hakkında ölçüm veya judgment üretme faaliyeti.

Evaluation:
- comparative veya absolute,
- online/offline,
- human/automated,
- deterministic/model-graded
olabilir.

**Ayrımlar:**
- Evaluation ≠ Verification. Eval ölçebilir/sıralayabilir; verification belirli claim/requirement hakkında yeterli evidence arar.
- Evaluation ≠ Validation. Eval intended-use validity'yi test edebilir ama her eval validation değildir.
- Evaluation ≠ benchmark score alone.
- Evaluation sonucu test setup/harness/environment'tan bağımsız değildir.

OpenAI 2026 third-party evaluation guidance özellikle tested system, environment/harness, task distribution ve validity checks'in claim interpretation'ını değiştirdiğini vurgular.

## 40. Evidence

**Çalışma tanımı:**  
> **Evidence:** Bir claim, standing, decision, Verification, Validation veya Evaluation sonucunu desteklemek, zayıflatmak ya da sınırlandırmak için kullanılabilen **izlenebilir bilgi, observation, artefact, test result, record veya diğer dayanak**.

Evidence:
- doğrudan veya dolaylı,
- güçlü veya zayıf,
- güncel veya stale,
- bağımsız veya aynı kaynaktan türemiş
olabilir.

**Ayrımlar:**
- Evidence ≠ proof/truth.
- Evidence ≠ Observability. Observability evidence üretebilir.
- Evidence ≠ claim.
- Evidence ≠ source authority.
- Evidence ≠ evaluation score alone.

NIST evidence'ı “grounds for belief or disbelief; data on which to base proof or establish truth/falsehood” olarak tanımlar. Assurance evidence ise trustworthiness/risk kararlarını destekleyen information olarak ele alınır.

## Dördüncü batch ilişki haritası

```text
Intent
└── clarified-as → Goal
      ├── guides → Plan
      ├── provides target-for → Validation
      └── may be measured-by → Evaluation

Plan
├── decomposes into → Work items
├── proposes → Dependencies / sequencing / Actors
└── is revised-by → new Evidence / State / discovered Work

Work item
├── may depend-on → Work item / Artefact / Decision / external condition
├── has-derived → Readiness
├── progresses through → Work state
└── may reach → Completion
                   │
                   ├── may trigger → Verification
                   └── does NOT imply → Validation / Goal achievement

Dependency
└── contributes-to → Readiness

Readiness
└── qualifies → admission / execution / transition

Observability
└── generates → Evidence

Evidence
├── supports/challenges → Verification
├── supports/challenges → Validation
└── feeds → Evaluation

Verification
└── asks → specified claim/requirement satisfied?

Validation
└── asks → intended use / Goal / stakeholder need satisfied?

Evaluation
└── measures/judges → performance / quality / capability / risk
    under → criteria / tasks / rubric / environment
```

## v0.3 üzerinde yapılan fine-tune'lar

### Work state
Work state artık daha açık olarak:
- current Work items,
- dependencies/readiness,
- plan revisions,
- completion/verification standing,
- evidence/next-resume
ilişkilerini taşıyabilir.

### Verification
v0.3'te Verification genel claim/effect qualification olarak tanımlanmıştı. Bu batch ile üçlü netleşti:
- **Verification:** specified claim/requirement gerçekten karşılanıyor mu?
- **Validation:** intended use/Goal gerçekten karşılanıyor mu?
- **Evaluation:** criteria altında nasıl perform ediyor / ne ölçüyoruz?

### Evidence / Observability
Observability doğrudan truth üretmez; inspectable events/records üzerinden Evidence sağlayabilir. Evidence de tek başına conclusion değildir; interpretation + verifier/evaluator gerekir.

### Goal / Completion
Work item'ların kapanması Goal'e ulaşıldığını göstermez. Bu, daha önceki:
`completion signal ≠ verified effect ≠ desired outcome`
ayrımını local vocabulary'ye yerleştirir.

### Plan / Work state
Plan proposed route; Work state current standing. Plan Work state'in parçası olabilir ama aynı şey değildir.

## Çakışma kontrolleri

1. Intent ≠ Goal.
2. Goal ≠ Plan.
3. Plan ≠ Work state.
4. Task/Work item ≠ Run.
5. Dependency ≠ hierarchy.
6. Dependency ≠ generic relation.
7. Readiness ≠ priority.
8. Readiness ≠ open status.
9. Completion ≠ Verification.
10. Completion ≠ Goal achievement.
11. Verification ≠ Validation.
12. Validation ≠ Evaluation.
13. Evaluation ≠ score.
14. Evidence ≠ truth/proof.
15. Observability ≠ Evidence ≠ Verification.

## Bu batch'in açtığı sonraki kavramlar

- Outcome
- Success criterion
- Requirement
- Constraint
- Acceptance criterion
- Metric
- Benchmark
- Oracle
- Review
- Approval

Bunlar sonraki batch için adaydır; zorunlu sıra değildir.
