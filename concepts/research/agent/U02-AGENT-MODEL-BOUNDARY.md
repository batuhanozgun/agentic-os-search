# Agent — U02: Model/LLM, Run ve Workflow Sınırları

**Tarih / erişim:** 2026-09-18. **Seviye:** 1, bağlantılı kavram incelemesi. **Statü:** kaynak gözlemleri + açıkça ayrılmış yorumlar. U01'i tamamlar; ortak referans veya SOUL/Development OS tasarım kararı değildir. Güncel iş [program STATE](../../STATE.md), çalışma sorusu [BRIEF](BRIEF.md), ilk kaynak dilimi [U01](U01-SOURCE-USES.md)'dedir.

## Neden bu komşular açıldı?

U01 ve sonraki konuşma, Agent ile model/LLM, belirli bir run ve workflow arasındaki sınırın bizim iletişimimiz için yük taşıdığını gösterdi. Özellikle “agent tasarlamak”, “model seçmek” ve “agent'ı çalıştırmak” ifadeleri aynı nesneyi anlatıyormuş gibi kullanılabilir.

Bu tur bütün Model/LLM/Workflow terminolojisini araştırmaz. Soru sınırlıdır:

> **Agent dediğimiz şey, kullandığı modelden ve belirli yürütülmesinden nasıl ayrılıyor; workflow ile ilişkisi hangi noktada kaynaklara göre değişiyor?**

## S1 — OpenAI Agents SDK: Agent ile model aynı nesne değil

**Kaynaklar:** OpenAI Agents SDK Python — “Agents”, “Models”, “Running agents”; 2026-09-18 canlı belgeler.
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/models/
- https://openai.github.io/openai-agents-python/running_agents/

**Doğrudan gözlem:** Agents sayfası Agent'ı bir LLM'nin talimatlar, araçlar ve opsiyonel runtime davranışlarıyla yapılandırılmış hali olarak açıklar. Aynı sayfa model seçimini Agent'ın bir özelliği/kararı olarak gösterir. Models sayfası model adlarını, Model uygulamalarını ve bunları çözen ModelProvider katmanını ayrıca tanımlar. Running agents sayfasında yapılandırılmış Agent, Runner.run(...) ile ayrıca yürütülür.

**Yorum:** Bu sözleşmede üç ayrı şey görünür:
1. **model** — Agent'ın çağırdığı hesaplama/inference bileşeni;
2. **Agent yapılandırması** — model + talimatlar + opsiyonel araç/runtime davranışları;
3. **run** — bu yapılandırmanın belirli girdi ve durumla yürütülmesi.

Dolayısıyla Agent(...) oluşturmak model yaratmak/eğitmek değildir; Agent'ın varlığı da belirli bir run'ın başlamış olduğu anlamına gelmez.

**Sınır:** Bu, OpenAI SDK nesne modelinin doğrudan kanıtıdır; bütün endüstride Agent kelimesinin aynı seviyeye işaret ettiğini göstermez.

## S2 — OpenAI Models: LLM, model adı ve provider aynı şey değil

**Kaynak:** OpenAI Agents SDK — “Models”, 2026-09-18.

**Doğrudan gözlem:** Belge, Agent'ın sonunda bir LLM çağırdığını; SDK'da Model arayüzünün belirli bir API'ye istek yapmayı bildiğini ve ModelProvider'ın model adlarını Model örneklerine çözdüğünü belirtir. Agent'a string bir model adı veya somut Model uygulaması verilebilir.

**Yorum / çalışma değeri:** Bu kaynak, en azından geliştirme bağlamında şu ifadelerin otomatik eşanlamlı olmaması gerektiğini gösterir:
- **LLM** — model sınıfı/kategorisi;
- **model / model instance** — çağrılan model soyutlaması;
- **model name / model identifier** — provider'ın çözdüğü ad;
- **provider** — model adını/erişimini sağlayan çözümleme-servis katmanı.

Bu tur “model family”, “ürün”, “servis”, “API modeli” gibi daha geniş endüstri ayrımlarını kapatmıyor. Kullanıcının önceki örnek model adları doğrulanmış ürün bilgisi olarak kullanılmadı.

## S3 — Anthropic: “LLM + tools” tek başına Agent demek zorunda değil

**Kaynak:** Anthropic, “Building effective agents”, ilk yayın 2024-12-19; 2026-09-18 canlı sayfa.
https://www.anthropic.com/engineering/building-effective-agents

**Doğrudan gözlem:** Anthropic, agentic systems üst başlığı altında workflows ile agents'ı ayırır. Workflow'da LLM ve araçlar önceden yazılmış kod yollarıyla orkestre edilir; Agent'ta LLM kendi süreç ve araç kullanımını dinamik biçimde yönlendirir. Aynı yazı “augmented LLM”i retrieval, tools ve memory ile zenginleştirilmiş temel yapı taşı olarak ayrıca tanımlar.

**Yorum:** Bu kullanımda **LLM + tools** bileşiminin varlığı Agent olmak için yeterli değildir. Yük taşıyan ayrım, yürütmenin ne kadarının model tarafından dinamik yönlendirildiğidir.

**Sınır:** Bu Anthropic'in mimari ayrımıdır. Aynı yazı bazı dinamik alt görev/feedback örüntülerini yine “workflow” diye adlandırır; dolayısıyla “bir yerde model karar verdi → artık Agent” şeklinde basit eşik çıkarılamaz.

## S4 — Google ADK: LlmAgent model kullanır; ama “workflow agent” etiketi daha geniştir

**Kaynaklar:** Google ADK — “Technical Overview”, “Simple agents with LlmAgent”, “Template agent workflows”; 2026-09-18 canlı belgeler.
- https://adk.dev/get-started/about/
- https://adk.dev/agents/llm-agents/
- https://adk.dev/agents/workflow-agents/

**Doğrudan gözlem:** ADK, LlmAgent'ı (çoğu yerde Agent alias'ı) LLM/generative AI modelini reasoning, karar verme ve araç etkileşimi için kullanan bileşen olarak açıklar. Model, talimat ve opsiyonel araçlar Agent'ın bileşenleri olarak anlatılır. Buna karşılık “workflow agents” adı verilen SequentialAgent, ParallelAgent, LoopAgent gibi kontrol bileşenleri orkestrasyon kararında AI modeline danışmadan deterministik çalışabilir.

**Yorum:** Bu kaynak iki şeyi birlikte gösterir:
- LLM-agent bağlamında **model Agent'ın içindeki/altındaki bir bileşendir**;
- framework etiketi olarak **Agent** kelimesi model-kullanan birimden daha geniş nesnelere de verilebilir.

Bu yüzden dış kaynağın sınıf adına bakıp bizim yerel agent kullanımımızı otomatik eşlemek güvenli değildir.

## İlk bağlantılı sonuçlar

### 1. Model/LLM ayrımı artık Agent için gerçek bir sınır

Bu turdaki kaynaklar arasında güçlü ortaklık şudur: model/LLM, modern LLM-agent düzenlerinde **Agent'ın kullandığı hesaplama bileşeni** olarak ayrılabilir. Agent ise model seçimi yanında talimat, araç/capability ve runtime/orchestration davranışı gibi ek sözleşmeler taşıyabilir.

Bu, henüz “Model” teriminin bütün endüstri tanımı değildir. Ancak Agent konuşmasında **model = agent** eşitliğini kullanmamak için yeterli kaynaktır.

### 2. Agent ile run ayrımı kaynakta somut

OpenAI SDK'da Agent'ın tanımı ve Runner ile yürütülmesi ayrı. Bu nedenle repo konuşmalarında en azından şu ambiguity'yi önlemek yararlı görünüyor:

- “Agent'ı tasarladık/yapılandırdık” → bir yürütme tanımı/konfigürasyonu hakkında olabilir.
- “Agent çalıştı / bu run'da ne yaptı?” → belirli yürütme olayı/state'i hakkındadır.

Run, session, conversation ve instance henüz eşitlenmedi; yalnız Agent yapılandırması ile belirli yürütmenin aynı şey olmadığı açık.

### 3. Workflow sınırı hâlâ source-dependent

Anthropic'in dar ayrımında workflow = önceden tanımlı orchestration, Agent = model-directed process. Google ADK ise deterministic orchestration bileşenlerine de “workflow agents” diyebilir.

Dolayısıyla workflow ile agent arasına evrensel tek çizgi çekmek için bu kaynaklar uygun değil. Yerel kullanımımız, dış kaynaktaki özgün etiketi değiştirmeden kendi sınırını açıkça seçebilir.

### 4. “Tool kullanabiliyor” tek başına yeterli ayırıcı değil

OpenAI'de tools Agent yapılandırmasında opsiyonel; Anthropic'te tools “augmented LLM”de de bulunabilir. Bu nedenle “aksiyon/tool kullanabiliyor → Agent” formülü bizim için başlangıç sezgisi olabilir ama kaynaklar bunu genel gerekli/yeterli koşul olarak taşımıyor.

## Bu tur neyi açmadı?

- Actor / Role / Identity dış kaynak araştırması yapılmadı.
- Hazır agent / custom agent ayrımı araştırılmadı.
- Model family / ürün / provider / API adlandırmalarının bütün endüstri haritası çıkarılmadı.
- Session / conversation / instance ayrımları kapatılmadı.
- “Agentic system” için yerel kullanım seçilmedi.
- SOUL'da agent kullanımı veya sayısı hakkında tasarım yapılmadı.

Bu sorular ancak mevcut yerel Agent adayını gerçekten değiştirecekleri noktada açılmalıdır.

## Kaynak listesi

- OpenAI Agents SDK — Agents: https://openai.github.io/openai-agents-python/agents/
- OpenAI Agents SDK — Models: https://openai.github.io/openai-agents-python/models/
- OpenAI Agents SDK — Running agents: https://openai.github.io/openai-agents-python/running_agents/
- Anthropic — Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Google ADK — Technical Overview: https://adk.dev/get-started/about/
- Google ADK — LlmAgent: https://adk.dev/agents/llm-agents/
- Google ADK — Template agent workflows: https://adk.dev/agents/workflow-agents/
