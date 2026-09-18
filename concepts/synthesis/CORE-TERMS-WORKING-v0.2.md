# Core Terms — Working Local Reference v0.2

**Tarih:** 2026-09-18.  
**Statü:** WORKING LOCAL REFERENCE / EVOLVING; tek tek terim onayı beklenmez.  
**Kapsam:** İlk iki batch, toplam 20 bağlı terim. Evrensel sözlük, nihai ontoloji veya SOUL mimarisi değildir.  
**Dayanak:** [U03 batch 1](../research/U03-CORE-TERMS-BATCH1.md), [U04 batch 2](../research/U04-CORE-TERMS-BATCH2.md), Agent U01/U02 ve mevcut Context/Memory/Harness study.

Bu sürüm v0.1'i supersede eder. Önceki dosya tarihsel snapshot olarak korunur. Tanımlar gerçek kullanım, yeni kaynak ve sonraki komşu batch'lerde çakışma çıktıkça birlikte fine-tune edilir.

## 20 çalışma tanımı

### 1. Agent
**Bir Model/LLM etrafında yapılandırılmış, belirli bir işi yürütürken yalnız çıktı üretmekten öte en az bazı yürütme seçimlerini modelin yaptığı AI yürütme birimi.**

### 2. Model
**Eğitim sonucunda oluşmuş, inference sırasında girdilerden çıktılar üreten öğrenilmiş hesaplama bileşeni; Agent'ın reasoning/generation gibi kabiliyetleri için kullandığı temel learned model.**

### 3. LLM
**Dil understanding/generation odaklı Model türü.**  
Yerel ilişki: **LLM is-a Model**.

### 4. Actor
**Belirli bir Work bağlamında sorumluluk, yetki veya fiili katkı üstlenen katılımcı/yürütücü birim.**

### 5. Role
**Bir Work bağlamında Actor'dan beklenen görev/sorumluluk ve katkı yönünü tarif eden atanabilir işlevsel konum; Authority/Permission sınırları Role'e bağlanabilir ama Role bunlarla eşit değildir.**

### 6. Run
**Bir Agent veya Workflow'un belirli başlangıç girdisi/state/configuration ile başlayıp bounded stop noktasına kadar süren tek execution olayı.**

### 7. Session
**Birden fazla Run/etkileşim arasında conversation/history/state continuity sağlayan konteyner.**  
Session Memory değildir; Memory/Context yönetimini destekleyebilir.

### 8. Workflow
**Belirli bir işi gerçekleştirmek için adımlar, koşullar, Actor/Agent ve Tool etkileşimlerinin koordinasyon yapısı.**  
Workflow structure'dır; Orchestration execution-time coordination'dır.

### 9. Tool
**Model/Agent'ın bilgi edinmek, hesaplama yapmak veya ortamda eylem gerçekleştirmek için çağırabildiği tanımlı capability interface.**

### 10. Harness
**Model/Agent'ların güvenilir, sınırlı ve devam ettirilebilir Work'e dönüşmesini sağlayan model-dışı işletim ve kontrol zemini; Runtime, context/memory plumbing, authority/permissions, orchestration, verification, observability ve continuity gibi yüzeyleri içerebilir/konfigüre edebilir.**

### 11. Runtime
**Agent/Workflow tanımlarını fiili Run'lara dönüştüren execution katmanı; loop/turn progression, model calls, Tool dispatch, Handoff, lifecycle ve state/session integration gibi mechanics'i işletir.**

### 12. Context
**Model/Agent'ın mevcut karar veya üretim anında görünür olan çalışma bilgi seti.**  
Kod tarafındaki dependency/state nesneleri gerekiyorsa **runtime context/local context** diye nitelenir.

### 13. Memory
**Bir Run'ın anlık Context'ini aşarak gelecekteki Run veya kararları etkileyebilmek üzere saklanan, geri çağrılabilen ve yaşam döngüsü yönetilebilen geçmiş bilgi/state birikimi.**

### 14. Identity
**Belirli bir scope içinde aynı Actor/Agent/entity'yi diğerlerinden ayırıp zaman/Run değişse de ona yeniden referans vermeyi sağlayan ayırt edici kimlik/nitelikler bütünü.**

### 15. Capability
**Actor/Agent/System'in mevcut Model, Tool, Runtime, Environment ve diğer mekanizmaları sayesinde fiilen gerçekleştirebildiği işlev veya eylem kapasitesi.**

### 16. Authority
**Actor/Agent'ın belirli Work/scope içinde hangi kararları almasının, sorumlulukları üstlenmesinin ve owner/system adına hangi etkileri üretmesinin meşru/yetkili olduğunu belirleyen normatif sınır.**

### 17. Permission
**Belirli bir entity'nin belirli resource, Tool veya action üzerinde belirli bir işlemi yapmasına verilen somut izin.**

### 18. Orchestration
**Execution sırasında hangi Agent/Actor/Tool'un ne zaman devreye gireceğini, hangi sıra/paralellikte çalışacağını ve sonraki adımın nasıl seçileceğini koordine eden kontrol mantığı.**

### 19. Handoff
**Aktif Work/conversation responsibility'sinin veya execution control'ünün bir Agent'tan başka bir Agent'a devredildiği geçiş.**

### 20. Subagent
**Başka bir Agent/Orchestrator tarafından daha geniş Work içinde belirli alt sorumluluk için çağrılan/delege edilen Agent; “sub” intrinsic type değil ilişkisel konumdur.**

## Birlikte kullanım haritası

```text
Model
└── LLM

Harness
├── contains/configures → Runtime
│   ├── executes → Agent / Workflow
│   ├── creates/manages → Run
│   ├── dispatches → Tool
│   ├── performs → Handoff
│   └── applies → Permission controls
├── manages → Context / Memory plumbing
├── may enforce → Authority / Permission
└── provides → Orchestration / Verification / Observability surfaces

Agent
├── uses → Model / LLM
├── may-call → Tool
├── executes-as → Run
├── may-be → Actor
└── may delegate-to → Subagent

Subagent
└── is-a → Agent

Actor
├── assumes → Role
├── identified-by → Identity
├── has → Capability
└── exercises-within → Authority
    └── maps-to → Permissions

Workflow
└── executed/coordinated-by → Orchestration
    ├── coordinates → Agents / Subagents / Actors / Tools
    └── may use → Handoff

Session
└── preserves continuity across → Runs

Memory
└── may feed → Context

Context
← assembled from — current input / Session / Memory / Tool results
```

## Kritik ayrım üçlüleri

### Context / Session / Memory
- **Context:** şu anda görünür çalışma seti.
- **Session:** birden fazla Run arasında continuity konteyneri.
- **Memory:** zamanlar arası tutulup geleceği etkileyen knowledge/state birikimi.

### Capability / Authority / Permission
- **Capability:** yapabiliyor mu?
- **Authority:** bunu owner/system adına yapmaya yetkili mi?
- **Permission:** bu spesifik action/resource üzerinde izin var mı?

### Workflow / Orchestration / Runtime
- **Workflow:** hangi yapı/adımlar?
- **Orchestration:** execution sırasında kim/ne, ne zaman, hangi sırada?
- **Runtime:** bütün bunları fiilen çalıştıran execution machinery.

### Agent / Actor / Role / Identity
- **Agent:** AI execution unit.
- **Actor:** Work'te sorumluluk üstlenen participant.
- **Role:** participant'tan beklenen işlev/sorumluluk.
- **Identity:** hangi participant/entity olduğunu ayırt eden continuity/reference.

### Subagent / Handoff
- **Subagent:** parent/manager'a göre ilişkisel Agent konumu.
- **Handoff:** active control/responsibility transfer mekanizması.

## v0.1'den değişenler

- Harness artık Runtime ile eşit okunamaz; Runtime onun execution-facing alt yüzeyi olarak ayrıldı.
- Session tanımı Context ve Memory'den daha açık ayrıldı.
- Role içindeki authority/permission ifadesi inceltildi; bunlar ayrı kavram oldu.
- Workflow, Orchestration'dan ayrıldı.
- Tool, Capability'den ayrıldı.
- Agent→Subagent ve Agent→Handoff ilişkileri ayrı tutuldu.

## Henüz dışarıda kalan güçlü kavramlar

State, Work state, Environment, Workspace, Sandbox, Policy, Guardrail, Verification, Observability, Persistence.

Bu liste sonraki batch seed'idir; sabit sıra değildir.
