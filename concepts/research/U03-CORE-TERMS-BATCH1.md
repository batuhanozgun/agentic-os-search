# Core Terms — U03: İlk 10 Terim İçin Bağlantılı İnceleme

**Tarih / erişim:** 2026-09-18.  
**Statü:** kaynak ve kavram incelemesi; yerel çalışma tanımlarının kanıt zemini. Evrensel sözlük, nihai ontoloji veya SOUL/Development OS tasarımı değildir.  
**Dayanak:** Agent U01/U02, EXP-002 geçici terim kayıtları, mevcut Harness study ve aşağıdaki sınırlı birincil kaynaklar.

## Neden tek terim değil 10 terim birlikte?

Agent üzerinde iki tur çalışınca Model/LLM, Actor/Role, Run/Session, Workflow/Tool ve Harness ayrımlarının birbirini doğrudan etkilediği görüldü. Tek tek kapanış istemek yerine bu turda küçük bir bağlantılı küme ele alındı.

Amaç her kavramın bütün literatürünü bitirmek değil; repo ve konuşmalarda birbirine karışmadan kullanılabilecek ilk tutarlı yerel referans çekirdeğini kurmaktır.

## Kaynak zemini

### OpenAI Agents SDK
2026-09-18 canlı belgeler:
- Agents: https://openai.github.io/openai-agents-python/agents/
- Models: https://openai.github.io/openai-agents-python/models/
- Running agents: https://openai.github.io/openai-agents-python/running_agents/
- Sessions: https://openai.github.io/openai-agents-python/sessions/
- Tools: https://openai.github.io/openai-agents-python/tools/
- Handoffs: https://openai.github.io/openai-agents-python/handoffs/

Bu belgeler Agent, Model, Run, Session ve Tool arasındaki uygulama sözleşmesini somut biçimde ayırmak için kullanıldı. SDK sözleşmesi evrensel kavram standardı değildir.

### Anthropic
- “Building effective agents”, 2024-12-19: https://www.anthropic.com/engineering/building-effective-agents

Workflow ve Agent arasındaki predefined-path vs model-directed-process ayrımı için kullanıldı. Anthropic'in kendi terminolojisi repo tanımına otomatik taşınmadı.

### NIST / RBAC geleneği
- Role glossary: https://csrc.nist.gov/glossary/term/role
- RBAC glossary: https://csrc.nist.gov/glossary/term/role_based_access_control
- Role engineering process: https://csrc.nist.gov/csrc/media/projects/role-based-access-control/documents/healthcarerbactfroleengineeringprocessv3_0.pdf

Role için görev/fonksiyon, sorumluluk ve authority/permission ilişkisini ayırmakta kullanıldı. Actor örneği domain-specific olduğundan genel Actor tanımının tek kaynağı yapılmadı.

### Harness
- OpenAI, “Harness engineering: leveraging Codex in an agent-first world”, 2026-02-11: https://openai.com/index/harness-engineering/
- Existing study: `research/studies/context-memory-harness-engineering/`

Harness terimi için mevcut bounded study'nin model-external operating/control substrate sentezi korundu; güncel OpenAI yazısı repository knowledge, environment legibility, feedback/observability ve enforceable constraints yönünü destekleyen güncel engineering örneği olarak kullanıldı.

## 1. Agent

**Yerel ihtiyaç:** Model, role, actor ve run ile karışmamalı.

**Çalışma tanımı:**  
> **Agent:** Bir Model/LLM etrafında yapılandırılmış, belirli bir işi yürütürken yalnız çıktı üretmekten öte en az bazı yürütme seçimlerini modelin yaptığı AI yürütme birimi.

**Neden böyle?**
- U01/U02 kaynakları Model ile Agent'ı ayırıyor.
- Anthropic model-directed execution ayrımını taşıyor.
- Tools zorunlu tutulmuyor; tool-capability tek başına yeterli sınır değil.
- Run ile Agent ayrılıyor: Agent yürütme biriminin tanımı/configuration'ı, Run onun belirli yürütmesi.

**Açık sınır:** Modelin ne kadar yürütme kontrolü taşıması gerektiği daha sonra karşı örneklerle inceltilebilir.

## 2. Model

**Çalışma tanımı:**  
> **Model:** Eğitim sonucunda oluşmuş, inference sırasında girdilerden çıktılar üreten öğrenilmiş hesaplama bileşeni; repo konuşmalarında Agent'ın reasoning/generation gibi kabiliyetleri için kullandığı temel learned model.

**Ayrımlar:**
- Model ≠ Agent.
- Model ≠ provider.
- Model ≠ ürün arayüzü.
- Model adı/identifier ile somut Model uygulaması aynı şey olmak zorunda değil.

**Yerel kullanım tercihi:** Bir sağlayıcı/model ailesi/ürün düzeyi belirsizse daha güvenli üst terim olarak `Model` kullanılabilir; exact ürün/ID gerektiğinde ayrıca nitelendirilir.

## 3. LLM

**Çalışma tanımı:**  
> **LLM (Large Language Model):** Dil dizileri üzerinde büyük ölçekli öğrenmeyle language understanding/generation kabiliyeti edinmiş Model türü.

**Yerel ilişki:**  
`LLM ⊂ Model`

Her Model LLM değildir. Multimodal veya başka learned models için dil-merkezlilik karar taşımıyorsa `Model` üst terimi tercih edilir.

**Açık sınır:** Modern multimodal modellerin ürün pazarlamasında “LLM” diye adlandırılması kaynak-yerel olabilir; repo kullanımında gereksiz genişletme yapılmaz.

## 4. Actor

**Çalışma tanımı:**  
> **Actor:** Belirli bir Work bağlamında bir sorumluluğu, yetkiyi veya fiili katkıyı üstlenen katılımcı/yürütücü birim.

Actor insan olabilir; Agent olabilir; uygun bağlamda başka bir otomatik yürütücü de Actor olarak modellenebilir.

**Ayrımlar:**
- Actor ≠ Role.
- Agent, belirli Work'e sorumlulukla bağlandığında Actor olabilir.
- Her Actor Agent değildir.

Bu, EXP-002'deki “çalışma sorumluluğunu üstlenen katılımcı/birim” kullanımını daha açık hale getirir.

## 5. Role

**Çalışma tanımı:**  
> **Role:** Bir Work bağlamında Actor'dan beklenen görev/sorumluluk, katkı yönü ve gerektiğinde authority/permission sınırlarını tarif eden atanabilir işlevsel konum.

**Ayrımlar:**
- Role işi kendi başına yürütmez; Actor Role'ü üstlenir.
- Bir Actor birden fazla Role taşıyabilir.
- Aynı Role farklı Actor'larca üstlenilebilir.
- Role yalnız permission set değildir; permission/authority rolün bir yüzü olabilir.

NIST'in job function ve permission ilişkisi bu ayrımı destekler; repo tanımı yalnız RBAC'a indirgenmez.

## 6. Run

**Çalışma tanımı:**  
> **Run:** Bir Agent veya Workflow'un belirli başlangıç girdisi, durum ve yürütme ayarlarıyla başlatılan; completion, pause, cancellation veya başka bir bounded stop noktasına kadar süren tek yürütme olayı.

**Önemli sonuç:** Tek bir Run içinde birden fazla model çağrısı, tool call veya handoff olabilir; hatta birden fazla Agent sırayla yer alabilir.

**Ayrımlar:**
- Run ≠ Agent.
- Run ≠ Session.
- Run, Agent tanımının bir örneği/çalıştırılmasıdır; Agent'ın kendisi değildir.

## 7. Session

**Çalışma tanımı:**  
> **Session:** Birden fazla Run veya etkileşim arasında devamlılık sağlamak için konuşma/geçmiş/state bilgisini ilişkilendiren süreklilik konteyneri.

OpenAI Agents SDK Sessions, conversation history'yi birden fazla agent run arasında korur.

**Ayrımlar:**
- Session bir Run değildir; birden fazla Run'ı bağlayabilir.
- Session her türlü uzun vadeli Memory ile eşit değildir.
- Session kimlik/actor/agent anlamına gelmez.

## 8. Workflow

**Çalışma tanımı:**  
> **Workflow:** Belirli bir işi/sonucu gerçekleştirmek için adımların, koşulların, Actor/Agent'ların ve Tool çağrılarının nasıl sıralanıp koordine edildiğini tarif eden çalışma akışı düzeni.

**Yerel tercih:** Workflow kelimesini Anthropic'in yalnız “predefined code paths” anlamına daraltmıyoruz. Repo kullanımında workflow daha geniş coordination structure'dır; gerektiğinde `deterministic workflow`, `model-directed workflow` gibi niteleme eklenir.

**Ayrımlar:**
- Workflow ≠ Agent.
- Bir Workflow hiç Agent içermeyebilir.
- Bir Workflow bir veya daha fazla Agent içerebilir.
- Bir Agent kendi Run'ı içinde alt-workflow benzeri adımlar oluşturabilir.

## 9. Tool

**Çalışma tanımı:**  
> **Tool:** Bir Model/Agent'ın bilgi edinmek, hesaplama yapmak veya dış/iç ortamda eylem gerçekleştirmek için çağırabildiği tanımlı capability/interface.

OpenAI SDK'da tools veri çekme, kod çalıştırma, API çağırma ve computer-use gibi eylemleri kapsar; başka bir Agent da tool olarak expose edilebilir.

**Ayrımlar:**
- Tool ≠ Agent.
- Bir Agent başka bir bağlamda Tool olarak sunulabilir; bu, Agent ve Tool kavramlarını eşitlemez.
- Tool capability sağlar; authority/permission ayrı sorudur.

## 10. Harness

**Çalışma tanımı:**  
> **Harness:** Model ve Agent'ların güvenilir, sınırlı ve devam ettirilebilir Work'e dönüşmesini sağlayan model-dışı işletim ve kontrol zemini; yürütme döngüsü/lifecycle, Tool arayüzleri, context/memory akışı, izin/yetki kontrolleri, orchestration, verification, observability ve work continuity gibi sorumlulukları taşıyabilir.

**Ayrımlar:**
- Harness ≠ Agent.
- Harness ≠ Workflow.
- Harness bir veya daha fazla Agent/Workflow/Run'ı işletebilir ve sınırlayabilir.
- Repository talimatları harness-benzeri control surface olabilir; deterministik runtime enforcement olduğu ayrıca kanıtlanmalıdır.

## İlk ilişki haritası

```text
Model
└── LLM  (Model'in bir türü)

Harness
├── Agent
│   ├── uses → Model / LLM
│   ├── may call → Tool
│   └── executes as → Run
├── Workflow
│   ├── may coordinate → Agent
│   ├── may coordinate → Actor
│   └── may call → Tool
└── Session
    └── may preserve continuity across → Runs

Actor
└── assumes → Role

Agent
└── may become → Actor
    when bound to Work responsibility/authority
```

Bu harita ontoloji kararı değildir; ilk 10 tanımın birbirini çelişkisiz taşıyıp taşımadığını kontrol etmek için kullanılan yerel ilişki görünümüdür.

## Çakışma kontrolleri

1. **Agent/Actor:** eşitlenmedi. Agent teknik AI yürütme birimi; Actor Work'e bağlanan katılımcı statüsüdür.
2. **Actor/Role:** eşitlenmedi. Actor üstlenir, Role beklenen işlev/sorumluluğu tarif eder.
3. **Agent/Run:** eşitlenmedi. Agent yapılandırılmış birim; Run belirli execution.
4. **Run/Session:** eşitlenmedi. Session birden fazla Run boyunca continuity taşıyabilir.
5. **Workflow/Agent:** eşitlenmedi. Workflow coordination structure; Agent participant/execution unit olabilir.
6. **Tool/Agent:** eşitlenmedi. Tool callable capability; Agent tool olarak expose edilebilir.
7. **Harness/Workflow:** eşitlenmedi. Harness operating/control substrate; workflow iş akışı düzenidir.
8. **Model/LLM:** eşitlenmedi. LLM Model'in alt türü olarak kullanılır.
9. **Model/Agent:** eşitlenmedi. Agent Model'i kullanır.
10. **Role/Permission:** eşitlenmedi. Permission Role'ün authority yüzlerinden biri olabilir.

## Henüz açılmayan sonraki güçlü komşular

Bu batch doğal olarak şu adayları açıyor, fakat bu turda tanımlanmıyor:
- Runtime
- Context
- Memory
- Identity
- Capability
- Authority
- Permission
- Orchestration
- Handoff
- Subagent

Bir sonraki batch'te bunların hangisinin daha çok çakışma temizlediğine göre seçim yapılabilir; liste sabit sıra değildir.
