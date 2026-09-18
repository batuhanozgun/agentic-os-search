# Core Terms — Working Local Reference v0.4

**Tarih:** 2026-09-18.  
**Statü:** WORKING LOCAL REFERENCE / EVOLVING; tek tek terim onayı beklenmez.  
**Kapsam:** Dört batch, toplam 40 bağlı terim. Evrensel sözlük, nihai ontoloji veya SOUL mimarisi değildir.  
**Dayanak:** U03–U06 batch araştırmaları, Agent U01/U02 ve ilgili studies/birincil kaynaklar.

Bu sürüm v0.3'ü supersede eder. Önceki sürümler tarihsel snapshot olarak korunur. Working map yeni kaynak, gerçek kullanım ve yeni çakışmalar çıktıkça fine-tune edilir.

## 40 çalışma tanımı — kısa görünüm

### Execution / Actor / Information / Control çekirdeği

1. **Agent** — Model/LLM etrafında yapılandırılmış, execution sırasında en az bazı yürütme seçimlerini modelin yaptığı AI yürütme birimi.
2. **Model** — inference sırasında girdilerden çıktılar üreten learned computational component.
3. **LLM** — language understanding/generation odaklı Model türü.
4. **Actor** — Work bağlamında sorumluluk/yetki/fiili katkı üstlenen participant/yürütücü.
5. **Role** — Actor'dan beklenen görev/sorumluluk ve katkı yönünü tarif eden atanabilir işlevsel konum.
6. **Run** — Agent/Workflow'un bounded tek execution olayı.
7. **Session** — birden fazla Run/etkileşim arasında history/state continuity sağlayan konteyner.
8. **Workflow** — Work'ü gerçekleştirmek için adım/koşul/Actor/Agent/Tool koordinasyon yapısı.
9. **Tool** — Model/Agent'ın bilgi edinmek, hesaplamak veya Environment'ta eylem yapmak için çağırdığı capability interface.
10. **Harness** — Model/Agent'ı güvenilir/sınırlı/devam ettirilebilir Work'e çeviren model-dışı operating/control substrate.
11. **Runtime** — Agent/Workflow tanımlarını fiili Run'lara dönüştüren execution katmanı.
12. **Context** — Model/Agent'ın mevcut karar anında görünür olan working information set.
13. **Memory** — gelecekteki Run/kararları etkileyebilmek için yaşam döngüsü yönetilen cross-time knowledge/state.
14. **Identity** — aynı Actor/Agent/entity'yi scope/zaman boyunca ayırt edip yeniden referanslamayı sağlayan identity attributes.
15. **Capability** — Actor/Agent/System'in Model/Tool/Runtime/Environment sayesinde fiilen yapabildiği şey.
16. **Authority** — Actor/Agent'ın owner/system adına hangi karar ve sorumlulukları meşru biçimde üstlenebileceği.
17. **Permission** — belirli resource/Tool/action üzerinde belirli işlemi yapmaya verilen somut izin.
18. **Orchestration** — execution sırasında kim/ne zaman/hangi sırada çalışacak ve next step nasıl seçilecek kontrol mantığı.
19. **Handoff** — active responsibility/execution control'ünün bir Agent'tan diğerine devri.
20. **Subagent** — daha geniş Work içinde başka Agent/Orchestrator'a göre alt sorumluluk taşıyan Agent.

### State / Environment / control surfaces

21. **State** — entity/process/system'in belirli anda continuation/decision/control açısından anlam taşıyan current condition representation'ı.
22. **Work state** — Work'ün identity/scope/standing/blockers/ownership/evidence/next-resume bilgisini taşıyan current/durable state.
23. **Environment** — Work'ün gerçekleştiği dış koşullar ve erişilebilir kaynaklar bütünü.
24. **Workspace** — Work materyallerinin/files/repos/artefacts/outputs düzenlendiği alan.
25. **Sandbox** — execution erişimini files/processes/network/credentials/resources açısından sınırlayan controlled boundary.
26. **Policy** — expected/allowed/forbidden/conditional davranışları tarif eden rules/principles.
27. **Guardrail** — execution event'ini Policy/criteria/risk açısından check edip block/reject/transform/escalate edebilen aktif kontrol.
28. **Verification** — specified claim/requirement/property'nin Evidence ve criteria karşısında gerçekten desteklenip desteklenmediğini değerlendirme.
29. **Observability** — System/Run/Workflow'un fiilen ne yaptığı hakkında yeterli traces/logs/events/state visibility'si.
30. **Persistence** — State/Memory/Work state/artefact/identity-linked bilginin Run/process/session/runtime sınırı sonrasında da korunabilmesi.

### Intent → Work → result → evidence hattı

31. **Intent** — user/owner isteğinin arkasındaki asıl yön, amaçlanan anlam ve neden; henüz operational Goal olmayabilir.
32. **Goal** — Work'ün yöneldiği açık target state/outcome/success condition.
33. **Plan** — Goal'e ulaşmak için önerilen ve revize edilebilir decomposition/approach/sequence/dependency/actor/control representation.
34. **Work item** — daha geniş Work içinde ayrı identity/scope/standing ile track/assign/depend/verify/close/reopen edilebilen yönetilebilir Work birimi.
    - **Task** — genellikle action-like Work item; source-local semantics varsa korunur.
35. **Dependency** — bir Work/artefact/action'ın start/validity/timing/closure/outcome'ının başka bir condition/state/output'a bağlı olduğu ilişki.
36. **Readiness** — belirli next action için prerequisites/information/authority/capacity/environment/control koşullarının yeterli olduğuna ilişkin derived standing.
37. **Completion** — belirli scope'un kendi lifecycle/acceptance koşullarına göre artık normal progression gerektirmediğini belirten closure standing/claim.
38. **Validation** — result/system/artefact'ın intended use, stakeholder need, Intent/Goal açısından gerçekten uygun/yararlı olup olmadığını değerlendirme.
39. **Evaluation** — Model/Agent/System/result/process'i criteria/tasks/rubric/metric/benchmark altında sistematik ölçüp performance/quality/capability/risk judgment üretme.
40. **Evidence** — claim/standing/decision/Verification/Validation/Evaluation sonucunu destekleyen veya sınırlandıran traceable information/observation/artefact/test result/record.

## Güncel ilişki haritası

```text
Intent
└── clarified-as → Goal
      ├── guides → Plan
      ├── target-for → Validation
      └── measured/judged-by → Evaluation

Plan
├── decomposes → Work items
├── proposes → Dependencies / sequencing / Actors
└── revised-by → Evidence / State / discovered Work

Work item
├── may depend-on → Work item / Artefact / Decision / external condition
├── has-derived → Readiness
├── progresses-through → Work state
└── may reach → Completion
                    │
                    ├── may trigger → Verification
                    └── does NOT imply → Goal achievement / Validation

Dependency ─contributes-to→ Readiness

Observability ─produces→ Evidence
Evidence
├── supports/challenges → Verification
├── supports/challenges → Validation
└── feeds → Evaluation

Verification ─asks→ specified claim/requirement satisfied?
Validation ─asks→ intended use / Goal / need satisfied?
Evaluation ─asks→ how well / under what criteria / at what risk?

State
├── specialization → Work state
├── may persist-via → Persistence
└── selected portion → Context

Work state
├── contains → Work item standing / Dependency / Readiness /
│              Completion / Evidence / next-resume
└── may persist-across → Runs / Sessions / Actors

Harness
└── connects/configures → Runtime / Context / Memory / Policy /
                         Sandbox / Orchestration / Verification /
                         Observability / Persistence

Runtime ─executes→ Agent / Workflow ─within→ Environment
Actor ─assumes→ Role
Actor ─operates-within→ Authority → Permissions
Agent ─may-be→ Actor
```

## Kritik ayrım zincirleri

### Intent / Goal / Plan
- **Intent:** neyi/neden istiyoruz?
- **Goal:** hangi target state/outcome'a ulaşmak istiyoruz?
- **Plan:** oraya nasıl gitmeyi şu anda öneriyoruz?

### Work item / Dependency / Readiness
- **Work item:** ayrı yönetilen Work birimi.
- **Dependency:** başka bir condition/state/output'a bağ.
- **Readiness:** belirli next action için şu anda admissible/actionable mı?

### Completion / Verification / Validation
- **Completion:** scope kapandı mı?
- **Verification:** specified claim/requirement doğru mu?
- **Validation:** amaçlanan kullanım/Goal gerçekten karşılandı mı?

### Evaluation / Evidence
- **Evaluation:** criteria altında performans/quality/capability/risk judgment.
- **Evidence:** bu judgment/claim'leri dayandırdığımız traceable ground.

## v0.3'ten değişenler

- Work state artık Work item/dependency/readiness/completion/evidence ilişkileriyle daha somut hale geldi.
- Verification, Validation ve Evaluation ayrıldı.
- Observability → Evidence → Verification/Evaluation hattı kuruldu.
- Goal ile Completion birbirinden açık ayrıldı.
- Plan current truth değil, revize edilebilir proposed route olarak konumlandı.
- “Task” yerine local umbrella olarak “Work item” tercih edildi; source-local Task semantics korunuyor.

## Sonraki güçlü kavramlar

Outcome, Success criterion, Requirement, Constraint, Acceptance criterion, Metric, Benchmark, Oracle, Review, Approval.

Bu liste sonraki batch seed'idir; sabit sıra değildir.
