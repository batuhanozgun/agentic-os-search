# Core Terms — Working Local Reference v0.3

**Tarih:** 2026-09-18.  
**Statü:** SUPERSEDED WORKING SNAPSHOT; ilk 30 terimin tarihsel v0.3 görünümü.  
**Kapsam:** Üç batch, toplam 30 bağlı terim. Evrensel sözlük, nihai ontoloji veya SOUL mimarisi değildir.  
**Dayanak:** [U03](../research/U03-CORE-TERMS-BATCH1.md), [U04](../research/U04-CORE-TERMS-BATCH2.md), [U05](../research/U05-CORE-TERMS-BATCH3.md), Agent U01/U02 ve ilgili studies.

Bu sürüm v0.2'yi supersede etmiş tarihsel snapshot'tır. Güncel working reference [v0.4](CORE-TERMS-WORKING-v0.4.md)'tür.

## 30 çalışma tanımı

### 1. Agent
**Bir Model/LLM etrafında yapılandırılmış, belirli bir işi yürütürken yalnız çıktı üretmekten öte en az bazı yürütme seçimlerini modelin yaptığı AI yürütme birimi.**

### 2. Model
**Eğitim sonucunda oluşmuş, inference sırasında girdilerden çıktılar üreten öğrenilmiş hesaplama bileşeni.**

### 3. LLM
**Language understanding/generation odaklı Model türü.**

### 4. Actor
**Belirli bir Work bağlamında sorumluluk, yetki veya fiili katkı üstlenen participant/yürütücü birim.**

### 5. Role
**Actor'dan beklenen görev/sorumluluk ve katkı yönünü tarif eden atanabilir işlevsel konum.**

### 6. Run
**Bir Agent veya Workflow'un belirli başlangıç girdisi/state/configuration ile başlayıp bounded stop noktasına kadar süren tek execution olayı.**

### 7. Session
**Birden fazla Run/etkileşim arasında conversation/history/state continuity sağlayan konteyner.**

### 8. Workflow
**Belirli bir işi gerçekleştirmek için adımlar, koşullar ve Actor/Agent/Tool etkileşimlerinin koordinasyon yapısı.**

### 9. Tool
**Model/Agent'ın bilgi edinmek, hesaplama yapmak veya Environment'ta eylem gerçekleştirmek için çağırabildiği tanımlı capability interface.**

### 10. Harness
**Model/Agent'ların güvenilir, sınırlı ve devam ettirilebilir Work'e dönüşmesini sağlayan model-dışı operating/control substrate; Runtime, context/memory plumbing, Policy/control, Orchestration, Verification, Observability ve continuity yüzeylerini içerebilir/konfigüre edebilir.**

### 11. Runtime
**Agent/Workflow tanımlarını fiili Run'lara dönüştüren execution katmanı.**

### 12. Context
**Model/Agent'ın mevcut karar veya üretim anında görünür olan çalışma bilgi seti.**

### 13. Memory
**Bir Run'ın anlık Context'ini aşarak gelecekteki Run/kararları etkileyebilmek üzere yaşam döngüsü yönetilen geçmiş knowledge/state birikimi.**

### 14. Identity
**Belirli scope içinde aynı Actor/Agent/entity'yi diğerlerinden ayırıp zaman/Run değişse de ona yeniden referans vermeyi sağlayan ayırt edici kimlik/nitelikler bütünü.**

### 15. Capability
**Actor/Agent/System'in Model, Tool, Runtime, Environment ve diğer mekanizmaları sayesinde fiilen gerçekleştirebildiği işlev/eylem kapasitesi.**

### 16. Authority
**Actor/Agent'ın belirli Work/scope içinde hangi kararları/sorumlulukları owner/system adına meşru biçimde üstlenebileceğinin normatif sınırı.**

### 17. Permission
**Belirli entity'nin belirli resource/Tool/action üzerinde belirli işlemi yapmasına verilen somut izin.**

### 18. Orchestration
**Execution sırasında hangi Agent/Actor/Tool'un ne zaman ve hangi sırada çalışacağını, sonraki adımın nasıl seçileceğini koordine eden kontrol mantığı.**

### 19. Handoff
**Aktif Work/conversation responsibility veya execution control'ünün bir Agent'tan başka bir Agent'a devredildiği geçiş.**

### 20. Subagent
**Başka Agent/Orchestrator tarafından daha geniş Work içinde belirli alt sorumluluk için kullanılan Agent; ilişkisel konumdur.**

### 21. State
**Entity/process/system'in belirli anda continuation, decision veya control açısından anlam taşıyan mevcut durumunun temsil edilebilir bilgisi.**

### 22. Work state
**Belirli Work'ün identity/scope/current standing/blockers/ownership/evidence/next-resume bilgisini geri kazandıran current/durable state kümesi.**

### 23. Environment
**Actor/Agent/Runtime'ın Work'ü gerçekleştirdiği ve gözlem/eylem yaptığı dış çalışma koşulları ve erişilebilir kaynaklar bütünü.**

### 24. Workspace
**Belirli Work için files/repos/artefacts/outputs gibi çalışma materyallerinin düzenlendiği mantıksal veya fiziksel alan.**

### 25. Sandbox
**Execution'ın file/process/network/credential/resource/host surfaces'e erişimini sınırlandırmak üzere tasarlanmış controlled/isolation environment boundary.**

### 26. Policy
**Belirli scope'ta expected/allowed/forbidden/conditional davranış ve kararları tarif eden rule/principle seti.**

### 27. Guardrail
**Input/output/Tool/execution event'ini Policy/criteria/risk koşullarına göre check edip gerektiğinde block/reject/transform/escalate eden aktif kontrol mekanizması.**

### 28. Verification
**Claim/artefact/completion/state transition/observed effect'in tanımlı criteria/evidence/oracle karşısında gerçekten desteklenip desteklenmediğini değerlendirme süreci.**

### 29. Observability
**System/Run/Workflow'un fiilen ne yaptığı hakkında telemetry/traces/logs/inspectable state üzerinden yeterli görünürlük elde edebilme özelliği.**

### 30. Persistence
**State/Memory/Work state/artefact/identity-linked bilginin Run/process/session/runtime sınırı sonrasında da saklanıp geri alınabilmesini sağlayan süreklilik özelliği/mekanizması.**

## Birlikte kullanım haritası

```text
                         ┌────────── Policy ──────────┐
                         │                            │
                         ▼                            ▼
Authority ───────► Permissions                 Guardrails
    ▲                    │                          │
    │                    ▼                          ▼
Actor ─assumes→ Role   Runtime ◄────────────── Sandbox
  │                     │  ▲                      ▲
  │                     │  │                      │
  │                     │  └── operates in ── Environment
  │                     │
  │                     ├── executes → Agent / Workflow
  │                     ├── creates/manages → Run
  │                     ├── dispatches → Tool
  │                     └── performs → Handoff
  │
  ├── identified-by → Identity
  └── has → Capability
                  ▲
                  └── depends on → Model / Tool / Runtime / Environment

Model
└── LLM

Agent
├── uses → Model
├── may-call → Tool
├── may-be → Actor
└── may delegate-to → Subagent
                         └── is-a → Agent

Workflow
└── coordinated-by → Orchestration
      └── coordinates → Agents / Actors / Tools / Handoffs

State
├── specialization → Work state
├── may persist via → Persistence
└── selected portion may enter → Context

Session ─preserves→ continuity across Runs
Memory ─may feed→ Context
Work state ─persists across→ Runs / Sessions / Actors

Environment
├── contains/supports → Workspace
└── may contain → Sandbox

Workspace ─holds→ artefacts / outputs / persisted Work state

Observability ─provides evidence/events→ Verification
Verification ─qualifies→ claims / completion / effects

Harness
└── configures/connects → Runtime / Context / Memory / Policy controls /
                         Sandbox / Orchestration / Verification /
                         Observability / Persistence surfaces
```

## Kritik ayrım grupları

### State / Work state / RunState
- **State:** genel current condition representation.
- **Work state:** Work continuation/control açısından gerekli state.
- **RunState:** belirli Runtime/framework'teki Run snapshot'ı; generic Work state ile aynı değildir.

### Environment / Workspace / Sandbox
- **Environment:** geniş dış çalışma koşulları/kaynakları.
- **Workspace:** Work materyallerinin düzenlendiği alan.
- **Sandbox:** execution access/containment boundary.

### Policy / Guardrail / Sandbox
- **Policy:** ne bekleniyor/izinli/yasak?
- **Guardrail:** belirli execution point'te check/enforcement.
- **Sandbox:** capability/resource containment boundary.

### Verification / Observability
- **Observability:** ne oldu?
- **Verification:** olan/iddia edilen şey criteria'yı gerçekten karşılıyor mu?

### Persistence / Session / Memory / Work state
- **Persistence:** boundary aşarak saklanabilme.
- **Session:** conversation/run continuity container.
- **Memory:** geleceği etkileyen retained knowledge/state.
- **Work state:** Work'ün current standing ve continuation truth'u.

## v0.2'den değişenler

- Harness artık Policy/Guardrail/Sandbox/Verification/Observability/Persistence yüzeylerini daha açık şekilde çevreleyen operating/control substrate olarak okunuyor.
- Capability tanımı Environment bağımlılığını görünür hale getirdi.
- Authority/Permission ilişkisi Policy ve enforcement ayrımıyla netleşti.
- Session/Memory ayrımına Persistence ve Work state eklendi.
- Workspace, Environment ve Sandbox ayrıldı.
- Verification ile Observability birbirinden ayrıldı.

## Sonraki güçlü kavramlar

Goal, Intent, Plan, Task/Work item, Dependency, Readiness, Completion, Validation, Evaluation, Evidence.

Bu liste U06 batch'inde işlendi. Güncel devam için v0.4 ve STATE'e dön.
