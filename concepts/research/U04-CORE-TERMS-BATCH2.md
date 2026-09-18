# Core Terms — U04: İkinci 10 Terim İçin Bağlantılı İnceleme

**Tarih / erişim:** 2026-09-18.  
**Statü:** kaynak ve kavram incelemesi; ilk batch'i genişleten çalışma. Evrensel sözlük, nihai ontoloji veya SOUL/Development OS tasarımı değildir.  
**Dayanak:** [U03 batch 1](U03-CORE-TERMS-BATCH1.md), mevcut Context/Memory/Harness study, OpenAI Agents SDK canlı belgeleri ve NIST glossary kaynakları.

## Bu batch neden bu 10 terimi seçti?

İlk batch şu açık sınırları bıraktı:

- Harness ile fiili execution katmanı aynı mı?
- Session ile Context ve Memory nasıl ayrılır?
- Actor/Role tarafında Identity, Capability, Authority ve Permission nasıl ayrılır?
- Workflow'un yürütülmesiyle Orchestration aynı şey mi?
- Bir Agent'ın başka Agent'a iş vermesi ile kontrolü devretmesi aynı mı?
- “Subagent” başlı başına bir Agent türü mü, yoksa ilişkisel bir konum mu?

Bu nedenle ikinci batch:
**Runtime, Context, Memory, Identity, Capability, Authority, Permission, Orchestration, Handoff, Subagent**
üzerinden ilerler.

## Kaynak zemini

### OpenAI Agents SDK — context, sessions, memory, orchestration, handoffs
2026-09-18 canlı belgeler:
- Context: https://openai.github.io/openai-agents-python/context/
- Sessions: https://openai.github.io/openai-agents-python/sessions/
- Running agents: https://openai.github.io/openai-agents-python/running_agents/
- Agent orchestration: https://openai.github.io/openai-agents-python/multi_agent/
- Handoffs: https://openai.github.io/openai-agents-python/handoffs/
- Agents: https://openai.github.io/openai-agents-python/agents/
- Sandbox memory: https://openai.github.io/openai-agents-python/sandbox/memory/

OpenAI SDK, Context teriminin iki farklı şeyi anlatabildiğini açıkça söylüyor: kod/runtime tarafındaki local context ve LLM'nin gördüğü context. Sessions birden fazla run arasında conversation history tutuyor. Sandbox memory ise session memory'den ayrı olarak geçmiş run'lardan öğrenilmiş dersleri ileriki run'lara taşıyor. Orchestration, hangi Agent'ın ne sırada çalışacağını ve sonraki adımın nasıl seçileceğini düzenliyor. Handoff aktif kontrolü başka Agent'a devredebiliyor.

### NIST — Identity / Authorization / Permission / Capability
2026-09-18 erişimi:
- Identity: https://csrc.nist.gov/glossary/term/identity
- Authorization: https://csrc.nist.gov/glossary/term/authorization
- Permission: https://csrc.nist.gov/glossary/term/permission
- Capability: https://csrc.nist.gov/glossary/term/Capability

NIST identity için belirli bir context içinde subject'i ayıran attribute set'i; permission için bir action'ı yapma authorization'ı; authorization için entity'ye erişim/eylem hakkı verilmesi gibi çeşitli bağlama göre tanımlar sunar. Capability için daha genel “feature or function” kullanımı da vardır.

Bu kaynaklar repository'deki local anlamları birebir belirlemez; Identity/Authority/Permission/Capability sınırlarını dünyadan kopmadan kurmak için kullanılır.

### Existing Context/Memory/Harness study
Canonical bounded synthesis:

- Context Engineering = current model-visible working-set formation and maintenance
- Agent Memory Engineering = cross-time write/manage/read/update/forget lifecycle
- Harness Engineering = model-external runtime/control environment

Bu çalışma ikinci batch'te özellikle Context–Memory–Runtime–Harness ayrımını taşır.

## 11. Runtime

**Çalışma tanımı:**  
> **Runtime:** Agent veya Workflow tanımını fiili Run'lara dönüştüren yürütme katmanı; agent loop/turn progression, model calls, Tool dispatch, Handoff, lifecycle, state/session integration ve stop/resume gibi execution mechanics'i işletir.

**Ayrımlar:**
- Runtime ≠ Harness.
- Runtime Harness'ın yürütmeye en yakın parçası olabilir; Harness daha geniş policy/control/observability/knowledge/verification zemini taşıyabilir.
- Runtime ≠ Run. Runtime çok sayıda Run'ı yürütür; Run tek execution olayıdır.
- Runtime ≠ Workflow. Workflow akış düzenini tarif eder; Runtime onu yürütür.

OpenAI Agents SDK'nin “higher-level runtime” ve Runner davranışı bu yerel ayrımı destekler.

## 12. Context

OpenAI'nin doğrudan uyarısı: “Context is an overloaded term.”

Yerel kullanımda çıplak **Context** için daha dar bir varsayılan seçiyoruz:

> **Context:** Bir Model/Agent'ın **mevcut karar veya üretim anında görünür olan çalışma bilgi seti**; talimatlar, conversation/input history, seçilmiş kaynaklar, Tool sonuçları ve o çağrıya dahil edilen diğer bilgilerden oluşabilir.

**Niteleme:** Uygulama kodunda Agent/Tool lifecycle'ına taşınan dependencies/state için gerektiğinde **runtime context** veya **local context** denir.

**Ayrımlar:**
- Context ≠ Memory.
- Context ≠ Session.
- Session ve Memory, Context'i besleyebilir.
- Context'te bulunmayan Memory o anda Model tarafından kullanılıyor sayılmaz.
- Local/runtime context ile model-visible context aynı şey değildir.

Bu seçim existing Context Engineering study'nin “current model-visible working set” senteziyle uyumludur.

## 13. Memory

**Çalışma tanımı:**  
> **Memory:** Bir Run'ın anlık Context'ini aşarak gelecekteki Run veya kararları etkileyebilmek üzere saklanan; gerektiğinde yazılan, okunan, güncellenen veya unutulan geçmiş bilgi/state birikimi.

**Ayrımlar:**
- Memory ≠ Context. Memory'den seçilen şey Context'e girebilir.
- Memory ≠ Session. Session belirli conversation/run continuity'si için bir memory mekanizması taşıyabilir ama bütün Memory kavramını kapsamaz.
- Memory ≠ store/database. Storage altyapısı Memory'nin yalnız bir gerçekleştirme yüzüdür.
- Her persistent veri anlamlı Memory değildir; ileriki karar/yürütmeyi besleme ilişkisi önemlidir.

OpenAI Sandbox memory'nin session history'den ayrı “lessons from prior runs” yaklaşımı ve existing study'nin cross-time lifecycle sentezi bu ayrımı destekler.

## 14. Identity

**Çalışma tanımı:**  
> **Identity:** Belirli bir kapsam içinde aynı Actor, Agent veya başka entity'yi diğerlerinden ayırıp zaman/Run değişse de ona yeniden referans verebilmemizi sağlayan ayırt edici kimlik ve nitelikler bütünü.

**Ayrımlar:**
- Identity ≠ Role. Aynı Identity farklı Role'ler üstlenebilir.
- Identity ≠ Agent definition. Agent'ın yapılandırması değişebilirken identity continuity korunabilir veya tersine yeniden kimliklendirilebilir.
- Identity ≠ authentication. Authentication bir identity claim'inin doğrulanmasıdır.
- Identity ≠ Session. Aynı Actor/Agent birden fazla Session'a katılabilir.

NIST'in “attributes that uniquely describe a subject within a given context” tanımı bu local kullanıma doğrudan dayanak sağlar.

## 15. Capability

**Çalışma tanımı:**  
> **Capability:** Bir Actor/Agent/System'in mevcut Model, Tool, Runtime, Environment ve diğer mekanizmaları sayesinde **fiilen gerçekleştirebildiği işlev veya eylem kapasitesi**.

**Ayrımlar:**
- Capability ≠ Authority. Yapabilmek, yapmaya yetkili olmak değildir.
- Capability ≠ Permission. Bir Tool mevcut olabilir fakat belirli aksiyona izin verilmeyebilir.
- Tool, Capability sağlayan bir mekanizma olabilir; Capability Tool'un kendisi değildir.
- Model capability ile system capability aynı ölçek değildir.

NIST'in genel “feature or function” kullanımı ve existing Harness study'deki environment/tool capability ayrımlarıyla uyumludur.

## 16. Authority

**Çalışma tanımı:**  
> **Authority:** Bir Actor/Agent'ın belirli Work ve scope içinde **hangi kararları almasının, hangi sorumluluğu üstlenmesinin ve hangi etkileri owner/system adına meşru biçimde üretmesinin yetkilendirildiğini** belirleyen normatif sınır.

**Ayrımlar:**
- Authority ≠ Capability.
- Authority ≠ Permission. Authority daha geniş sorumluluk/karar yetkisi olabilir; Permission bunun belirli teknik action/resource düzeyindeki gerçekleştirme iznidir.
- Role Authority'yi etkileyebilir veya taşıyabilir ama Role = Authority değildir.
- Prompt içinde “sen yetkilisin” denmesi runtime enforcement olmadan actual Authority/Permission garantisi değildir.

Bu yerel anlam NIST authorization/access-right kavramından yararlanır fakat yalnız erişim kontrolüne indirgenmez; Work responsibility ve owner-sanction boyutunu da taşır.

## 17. Permission

**Çalışma tanımı:**  
> **Permission:** Belirli bir entity'nin belirli bir resource, Tool veya action üzerinde belirli bir işlemi yapmasına verilen somut izin.

**Ayrımlar:**
- Permission ≠ Authority. Authority “bu kararı/işi sen sahiplenebilirsin” düzeyinde olabilir; Permission “şu API çağrısını yapabilirsin” düzeyindedir.
- Permission ≠ Capability. Capability fiziksel/teknik imkan; Permission izin.
- Permission runtime'da enforce edilebilir veya yalnız policy/prose olarak temsil edilebilir; bu ikisi aynı güvence seviyesi değildir.

NIST: “Authorization to perform some action on a system.”

## 18. Orchestration

**Çalışma tanımı:**  
> **Orchestration:** Bir Run veya çoklu-Agent çalışma sırasında **hangi Agent/Actor/Tool'un ne zaman devreye gireceğini, hangi sırada/parallel biçimde çalışacağını ve sonraki adımın nasıl seçileceğini fiilen koordine eden kontrol mantığı**.

**Ayrımlar:**
- Orchestration ≠ Workflow. Workflow akış yapısını tarif eder; Orchestration bu yapının execution-time koordinasyonudur.
- Orchestration code-directed veya model-directed olabilir.
- Orchestration ≠ Harness. Harness orchestration'ı barındırabilir ama verification, context/memory, permissions, observability gibi daha geniş sorumluluklar taşır.
- Orchestration ≠ Agent. Bir Agent orchestration kararı verebilir; yine de kavramlar aynı değildir.

OpenAI Agents SDK doğrudan orchestration'ı “which agents run, in what order, and how next step is decided” şeklinde tarif eder.

## 19. Handoff

**Çalışma tanımı:**  
> **Handoff:** Aktif Work/conversation responsibility'sinin veya execution control'ünün bir Agent'tan başka bir Agent'a devredildiği geçiş.

**Ayrımlar:**
- Handoff ≠ subtask delegation. Manager Agent bir Subagent'ı Tool gibi çağırıp kontrolü elinde tutabilir; bu Handoff olmak zorunda değildir.
- Handoff sırasında hedef Agent aktif Agent haline gelebilir.
- Handoff ≠ Orchestration. Handoff orchestration mekanizmalarından biridir.
- Handoff'ta hangi Context/state'in devredildiği ayrı contract'tır.

OpenAI Agents SDK handoff pattern'i specialist'in konuşmanın kontrolünü devralmasıyla manager-as-tool pattern'inden ayırır.

## 20. Subagent

**Çalışma tanımı:**  
> **Subagent:** Başka bir Agent veya Orchestrator tarafından daha geniş Work içinde belirli bir alt sorumluluk için çağrılan/delege edilen **Agent**; “sub” onun intrinsic türünü değil, mevcut decomposition içindeki ilişkisel konumunu belirtir.

**Ayrımlar:**
- Subagent is-a Agent.
- Her Agent Subagent değildir; aynı Agent başka bir Work topolojisinde primary/manager olabilir.
- Subagent Handoff ile veya Tool-like invocation ile kullanılabilir.
- Subagent ≠ Tool; fakat Agent bir Tool interface üzerinden expose edilebilir.
- Subagent ≠ Role. “Reviewer” Role olabilir; o Role'ü üstlenen specialized Agent o anda Subagent olabilir.

OpenAI orchestration belgelerindeki manager + specialized sub-agents ve handoff patterns bu ilişkisel kullanımı destekler.

## İkinci batch ilişki haritası

```text
Harness
├── contains / configures → Runtime
│   ├── executes → Workflow
│   ├── executes → Agent
│   ├── creates/manages → Run
│   ├── dispatches → Tool
│   ├── performs → Handoff
│   └── applies → Permission controls
├── manages → Context / Memory plumbing
├── may enforce → Authority / Permission boundaries
└── provides → Orchestration / Verification / Observability surfaces

Context
← assembled from — Session / Memory / current input / Tool results

Memory
└── may feed → Context

Identity
└── distinguishes → Actor / Agent across relevant scope

Actor
├── assumes → Role
├── has → Capability
└── exercises-within → Authority
        └── may map to → Permissions

Orchestration
├── coordinates → Agents / Subagents / Tools / steps
├── may use → Handoff
└── executes a → Workflow

Subagent
└── is-a → Agent
    └── relative-to → parent/manager/orchestrator
```

## İlk batch üzerinde yapılan fine-tune'lar

### Harness
v0.1'de Harness'ın “yürütme lifecycle'ı” taşıyabileceği söyleniyordu. Runtime tanımlanınca sınır netleşti:
- **Harness** = daha geniş operating/control substrate
- **Runtime** = tanımları Run'a çeviren execution machinery

Harness Runtime'ı içerebilir/konfigüre edebilir ama ikisi eşit değil.

### Session
İlk tanım korunuyor fakat artık:
- Session = continuity container
- Memory = daha genel cross-time retained knowledge/state
- Context = current visible working set

şeklinde üçlü ayrım netleşti.

### Role
Role tanımındaki authority/permission yüzü korunuyor; fakat Role artık bunların kendisi değil:
- Role expected function/responsibility
- Authority sanctioned decision/responsibility scope
- Permission concrete action/resource allowance

### Workflow
Workflow'un “coordination arrangement” anlamı korunuyor; Orchestration ile sınır:
- Workflow = structure/plan
- Orchestration = execution-time coordination/control

### Tool
Tool definition korunuyor; Capability ile sınır:
- Tool = callable interface/mechanism
- Capability = actual ability/function that may arise from model/tool/runtime/environment composition

## Çakışma kontrolleri

1. Runtime ≠ Harness.
2. Runtime ≠ Run.
3. Context ≠ Memory.
4. Context ≠ Session.
5. Memory ≠ Session.
6. Identity ≠ Role.
7. Identity ≠ Authentication.
8. Capability ≠ Authority.
9. Capability ≠ Permission.
10. Authority ≠ Permission.
11. Workflow ≠ Orchestration.
12. Orchestration ≠ Harness.
13. Handoff ≠ Subagent.
14. Handoff ≠ generic delegation.
15. Subagent is-a Agent, fakat ilişkisel statüdür.

## Bu batch'in açtığı sonraki kavramlar

- State
- Work state
- Environment
- Workspace
- Sandbox
- Policy
- Guardrail
- Verification
- Observability
- Persistence

Bunlar sonraki batch için adaydır; zorunlu sıra değildir.
