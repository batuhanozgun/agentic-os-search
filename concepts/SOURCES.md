# Kavram Çalışması — Kaynak Notları

Bu dosya taslaktan kanıta geri dönüş yoludur. **2026-09-18 sadeleştirmesinde dış kaynaklar tekrar okunmadı.** Aşağıdaki ilk bölüm, sonraki kullanım incelemesinde gerçekten açılan birincil belge bölümlerini kaydeder. U01–U06 ise bakım öncesi main commit'ine sabitlenmiş tarihsel kayıtlardır; onların bütün okuma iddiaları geriye dönük doğrulanmış sayılmaz.

<a id="model-degisimi-ve-devam-2026-09-18"></a>
## Model değişimi ve devam — 2026-09-18

**Soru:** “Agent'ın modelini değiştirelim” ve “Aynı agent yeni oturumda devam etsin” cümlelerinde yapılandırma, model, kimlik ve yürütmenin hangi sınırları ayrılmalı?

**Yöntem ve kapsam:** Aşağıdaki canlı HTML belge bölümleri web üzerinden açılıp okundu. Sayfa bütünü, kaynak kod, kurulu paket veya ürün davranışı çalıştırılarak doğrulanmadı. Tarih erişim tarihidir; sayfaların tamamının değişmez snapshot'ı ya da tüm iddiaların en yeni paket sürümünde sınandığı anlamına gelmez. Aynı kurumun sayfaları bağımsız deneyler olarak sayılmadı. Güncel ürün isimlerini sıralamak veya model önermek bu çalışmanın konusu değildir.

### OA-Agent — OpenAI Agents SDK, Agents

**Kaynak/bölüm:** https://openai.github.io/openai-agents-python/agents/ — giriş, Basic configuration, Cloning/copying agents.

**Gözlem:** Belgede Agent'ın ad, talimat, model ve araç gibi yapılandırma alanları ayrı; çalışma tanımının kopyalanması da ayrı işlem olarak yer alıyor.

**Katkı/sınır:** Tanım/yapılandırma ile tek çalışma ve kimliği ayırmak için uygulama örneği. SDK nesnesi bütün agent kullanımlarının ontolojisi değildir; kopyalamanın iş kimliğini nasıl belirleyeceği bizim yerel yorumumuzdur.

### OA-Run — OpenAI Agents SDK, Running agents

**Kaynak/bölüm:** https://openai.github.io/openai-agents-python/running_agents/ — The agent loop; Run config / Model, provider, and session defaults; State and conversation management / Conversations/chat threads.

**Gözlem:** RunConfig, tanımı değiştirmeden çalıştırma düzeyinde model seçimini etkileyebilir. Döngü model çıktısını işler, araçları yürütür veya hedef Agent'ı değiştirir. Bir mantıksal konuşma turu birden fazla Agent içerebilir.

**Katkı/sınır:** Model seçimi ile tanım değişikliğini, modelin araç isteği ile yürütmeyi ve Run ile Agent sayısını eşitlemiyoruz. Çalışabilirlik/performance testi yapılmadı.

### OA-Session — OpenAI Agents SDK, Sessions overview

**Kaynak/bölüm:** https://openai.github.io/openai-agents-python/sessions/ — Operational patterns: Memory persistence, Multiple sessions, Session sharing; geçmiş ile yeni girdinin birleştirilmesi açıklaması.

**Gözlem:** Aynı Agent tanımı farklı oturumlarda, farklı Agent'lar ortak oturumda kullanılabiliyor. Bellek içi ve dosya tabanlı depolama ayrılıyor; geçmiş çağrı girdisine hazırlanıyor.

**Katkı/sınır:** Session=Agent ve Session=zorunlu kalıcılık eşitliklerine somut karşı örnekler. Ortak oturumun erişim açısından her durumda uygun olduğunu veya bütün bilgilerin aktarıldığını göstermez.

### OA-Resume — OpenAI Agents SDK, Human-in-the-loop

**Kaynak/bölüm:** https://openai.github.io/openai-agents-python/human_in_the_loop/ — giriş, Example: pause, approve, resume; Long-running approvals; Versioning pending tasks.

**Gözlem:** Askıdaki Run, RunState üzerinden saklanıp başka süreçte geri yüklenebilir. Belge bekleyen işler için tanım/SDK sürüm eşlemesini, model/prompt/araç değişikliklerindeki uyumsuzluk riskini belirtir.

**Katkı/sınır:** Duraklama veya çağrı dönüşü mantıksal Run'ın zorunlu bitişi değildir. Eski konuşma mesajları ile yürütmenin bütün devam durumu aynı sayılmaz. Gösterilen onay akışı bütün ürünlerde geçerli bir kurtarma garantisi değildir.

### OA-Model — OpenAI Agents SDK, Models

**Kaynak/bölüm:** https://openai.github.io/openai-agents-python/models/ — Mixing models in one workflow; Mixing models across providers; ilgili model/provider arayüz açıklamaları.

**Gözlem:** Model adı, ModelProvider çözümlemesi ve Model arayüzü ayrı seçeneklerdir. Sağlayıcılar arasında araç/girdi/çıktı desteği farklılaşabilir.

**Katkı/sınır:** Öğrenilmiş model, SDK erişim nesnesi ve servis birbirinin yerine kullanılmaz. Model değiştirme olanağından sınırsız ikame edilebilirlik çıkmaz. Tüm sağlayıcıların envanteri veya belirli model geçişi araştırılmadı.

### OA-Context — OpenAI Agents SDK, Context management

**Kaynak/bölüm:** https://openai.github.io/openai-agents-python/context/ — giriş, Local context, Agent/LLM context.

**Gözlem:** Kodun kullandığı context nesnesi modele otomatik gönderilmez. Modelin göreceği bilgi talimat, girdi veya araç sonucu gibi yollardan sunulur.

**Katkı/sınır:** Context maddesindeki kayıp kapsam geri getirildi. Depoda bulunma, uygulamanın erişebilmesi ve modelin o çağrıda görmesi farklı şeylerdir. Genel bellek yönetimi bu okumayla tamamlanmadı.

### AN-Patterns — Anthropic, Building effective agents

**Kaynak/bölüm:** https://www.anthropic.com/engineering/building-effective-agents — ilk yayın 2024-12-19; bu erişimde What are agents?, Routing, Orchestrator-workers, Evaluator-optimizer, Agents bölümleri.

**Gözlem:** Yazarlar modelin süreci yönlendirmesini öne çıkarırken bazı model kararları içeren örüntüleri workflow diye adlandırıyor. Çevreden sonuç alıp ilerlemeyi yeniden değerlendirme açıklanıyor.

**Katkı/sınır:** Agent çalışma tercihimiz için davranış dayanağı; her model kararı veya her döngü genel Agent testi yapılmadı. Sayfa güncellenmiş bir canlı metindir, değişmemiş 2024 arşivi değildir. SDK adlandırmasıyla tek standarda indirgenmez.

### CC-Agents — Claude Code, Create custom subagents

**Kaynak/bölüm:** https://code.claude.com/docs/en/sub-agents — giriş/Built-in subagents; Write subagent files; Supported frontmatter fields; Choose a model; Enable persistent memory; Resume subagents.

**Gözlem:** Yeniden kullanılabilir dosya tanımı, model seçimi ve belirli çağrı ayrılıyor. Yeni çağrı ile mevcut agent kimliğine devam farklı işlemler; bazı devamlar aynı kimlikle yeni Run olarak tarif ediliyor. Oturumlar arası bellek de ayrı yapılandırılabiliyor.

**Katkı/sınır:** Hazır/özelleştirilmiş tanımın yeni model eğitimiyle eşit olmadığını ve “resume”un ürünler arasında aynı yaşam döngüsünü göstermediğini örnekliyor. Bu ürünün tüm agent türlerinin devamını veya ChatGPT oturumlarını temsil etmiyor. Özelliklerin kurulu sürümde çalışması denenmedi.

### CC-Models — Claude Code, Model configuration

**Kaynak/bölüm:** https://code.claude.com/docs/en/model-config — Available models ve Model aliases.

**Gözlem:** Üründeki model seçim alanı takma ad veya sağlayıcıya özgü seçim değeri alabiliyor; alias çözümlemesi zaman/sağlayıcıyla değişebiliyor.

**Katkı/sınır:** Ürün, seçim etiketi ve gerçek model sürümünün ayrı konuşulması gerekiyor. Bu okuma eski konuşmadaki bütün örnek model adlarını doğrulamıyor; güncel model önerisi veya fiyat/kabiliyet araştırması değil.

### Yerel sonuç ve karşı örneklerin statüsü

[WORKING'deki kullanım incelemesi](WORKING.md#model-degisimi-ve-devam), yukarıdaki belge örneklerinden hareketle aynı tanım, aynı kimlik, aynı rol, aynı oturum ve aynı Run'ı ayrı iddialar olarak ele alır. Kimliğin hangi değişikliklerde korunacağı yerel izleme tercihidir; belgelerden evrensel özdeşlik ölçütü çıkarılmadı.

Aynı tanımdan iki ayrı katılımcı, ortak oturum kullanan iki Agent, boş yeni oturum ve duraklatılıp sürdürülen yürütme örnekleri metin üzerinde karşılaştırıldı. Bunlar çalıştırılmış entegrasyon testleri değildir. Önceki “bütün terimler oturdu” sonucu yenilenmedi; bu tur yalnız iki başlangıç cümlesini açıklayacak sınırlı yerel düzeltme yaptı.

## Devralınan kayıtlar ve kapsamları

| Kayıt | İlgili taslak alanı | Nasıl kullanılmalı? |
|---|---|---|
| [U01 — Agent kaynak kullanımları](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/agent/U01-SOURCE-USES.md) | Agent; farklı geleneklerin kullandığı nesne ve davranış düzeyleri. | Kaynak/bölüm, yorum ve gerçek okuma kapsamı ayrıntılı kayıtlıdır. Kaynak açıklaması ile yerel tanım yine ayrı kalır; bu bakım güncel dış doğrulama yapmaz. |
| [U02 — Agent/Model sınırı](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/agent/U02-AGENT-MODEL-BOUNDARY.md) | Agent, Model/LLM, yapılandırma/çalıştırma, Workflow ve Tool. | SDK kullanımından genel tanıma geçiş bir yorumdur. ModelProvider nesnesi veya model adı, gerçek model ile otomatik eşitlenmez. |
| [U03 — İlk bağlı küme](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U03-CORE-TERMS-BATCH1.md) | WORKING 1–10: Agent–Harness. | Kaynak listesi ile yerel çalışma tercihleri iç içedir. Her madde bağımsız doğrulanmış bulgu sayılamaz; eski Agent A/B seçimi ve EXP-002 etkisi burada izlenebilir. |
| [U04 — İkinci bağlı küme](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U04-CORE-TERMS-BATCH2.md) | WORKING 11–20: Runtime–Subagent. | Context'in iki kullanımı, yetki/yapabilme ve kontrol devri sınırları burada ayrıntılıdır. Kaynağın anlamı ve bizim tercihimiz gerekli bölümden ayrıştırılmalıdır. |
| [U05 — Üçüncü bağlı küme](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U05-CORE-TERMS-BATCH3.md) | WORKING 21–30: State–Persistence. | Study sentezi ile SDK/ürün açıklamaları birlikte kullanılmıştır. Kayıt varlığı sandbox güvenliği, doğrulama veya süreklilik başarısının kanıtı değildir. |
| [U06 — Dördüncü bağlı küme](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U06-CORE-TERMS-BATCH4.md) | WORKING 31–40: Intent–Evidence; Task alt kullanımı. | NIST ve evaluation atıfları, yerel Work yorumunun tamamını kendiliğinden desteklemez. Güncel dış iddiada ilgili sayfa/bölüm yeniden kontrol edilmelidir. |

U03–U06'nın URL/tarih listeleri, her cümle için teyit edilmiş okuma/kanıt zinciri yerine geçmez. Bu dosyaları ne bütünüyle yanlış ilan ediyoruz ne de tam doğrulanmış kabul ediyoruz. Somut bir kullanımda yük taşıyan iddia seçildiğinde onun kaynak dayanağı onarılır; bütün literatürü yeniden taramak otomatik önkoşul değildir.

## U01'deki kaynak çeşitliliğine kısa dönüş

Aşağıdakiler **U01'in eski okuma kaydının özeti**dir; bu tur yeniden gözlem değildir. Tam bölüm ve sınırlar yukarıdaki U01 bağlantısındadır. AN-Patterns ve OA-Agent/OA-Run için bu turun seçici tekrar okuması yukarıda ayrıca kayıtlıdır.

| Kaynak | U01'in kaydettiği ayrım | Eski okuma sınırı |
|---|---|---|
| Poole–Mackworth, [Artificial Intelligence, §1.1](https://artint.info/3e/html/ArtInt3e.Ch1.S1.html) | Çevrede eyleyen varlık; LLM zorunluluğu yok. | §1.1'in ilgili giriş açıklaması; kitabın tamamı değil. |
| Wooldridge–Jennings, [1995 makalesi](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95.pdf) | Zayıf/güçlü agency kullanımları. | İlk beş PDF sayfası; tanım dayanağı basılı 116–117. |
| Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Workflow/Agent ve süreç kontrolü; her dinamik karar yeterli eşik değil. | İlgili Agent ve workflow bölümleri; değişmez 2024 arşivi değil. |
| OpenAI, [Practical guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | Kullanıcı adına işi yürüten LLM sistemi; model/araç/talimat bileşenleri. | Basılı 4 ve 7; rehberin tamamı değil. |
| OpenAI [Agents SDK](https://openai.github.io/openai-agents-python/agents/) ve [Running agents](https://openai.github.io/openai-agents-python/running_agents/) | Yapılandırma ile belirli yürütme farklı. | İlgili belge bölümleri; kurulu paket/kod testi yok. |
| Google ADK [Agents](https://adk.dev/agents/) ve [Workflow agents](https://adk.dev/agents/workflow-agents/) | Agent etiketi deterministik kontrol birimlerine de verilebiliyor. | Belgelenen adlandırma; güncel ürün tercihi veya çalışma testi değil. |

## Mevcut araştırmayı yeniden kullanma

[Studies kataloğu](../research/studies/CATALOG.md) → ilgili META/STATE/INDEX → gerekli bulgu ve özgün kaynak yolu izlenir. Önceki concepts kayıtlarının dayandığı başlıca çalışmalar:

- [Context/Memory/Harness](../research/studies/context-memory-harness-engineering/META.md): model-dışı işletim, bilgi ve devam ayrımları.
- [Work Management / Project Control](../research/studies/work-management-project-control/META.md): çalışma durumu, bağımlılık, hazır olma ve tamamlanma ayrımları.
- [Carbon Layer sandboxing](../research/studies/the-carbon-layer/videos/-01_NB4SbBY-agent-sandboxing/META.md): çalışma alanı ile gerçek erişim/etki sınırı.
- [EXP-002 terim kaydı](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md): eski konuşmada neyin kastedildiğine dayanak; dış dünya tanımı değil.

Bu çalışmaların kapsamı veya yetkisi değiştirilmez. Erişilebilir kayıt, bugün gerçekten okunmuş kaynakla aynı değildir.

## Yeni kaynak notu nasıl eklenir?

Gerektiğinde aynı dosyaya kısa bir not ekle: hangi somut soruyu çözmek için okundu; kaynak/bölüm ve tarih/sürüm; gerçekten görülen kullanım; bundan çıkarılan yerel yorum; WORKING'de etkilenen madde/ilişki; açık sınır. Doğrudan gözlem, eski kayıt özeti ve assistant tercihi ayrı belirtilir. Yalnız link listesi, kaynak okuması diye adlandırılmaz.
