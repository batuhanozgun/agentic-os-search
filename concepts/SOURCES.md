# Kavram Çalışması — Kaynak Notları

Bu dosya taslaktan kanıta geri dönüş yoludur. **2026-09-18 sadeleştirmesinde dış kaynaklar tekrar okunmadı.** Aşağıdaki tarihli bölümler, ilgili kullanım incelemesinde gerçekten açılan belge bölümlerini kaydeder. U01–U06 ise bakım öncesi main commit'ine sabitlenmiş tarihsel kayıtlardır; onların bütün okuma iddiaları geriye dönük doğrulanmış sayılmaz.

<a id="tamamlanma-ve-yayim-2026-09-18"></a>
## Tamamlanma ve yayımlama — 2026-09-18

**Soru:** “İşi bitirdi; sonucu yayımlayabilir” cümlesinde kapanış, kanıt ve eylem izni nasıl ayrılır? **Okuma:** Aşağıdaki HTML bölümleri bu tur web üzerinden açıldı; erişim tarihi 2026-09-18. Paket kurulumu, kaynak kod çalıştırması, gerçek deployment veya izin deneyi yapılmadı. Sayfa bölümleri okunmuştur; tüm bağlantılı standartlar ve bütün ürün belgeleri değil. Canlı sayfa erişimi değişmez sürüm/paket garantisi değildir.

| Anahtar / kaynak ve okunan bölüm | Kaynakta gözlenen kullanım | Yerel katkı ve sınır |
|---|---|---|
| **OA-End:** [OpenAI Agents SDK, Running agents](https://openai.github.io/openai-agents-python/running_agents/), The agent loop | Runner, çıktıyı final output saydığında döngüyü sonlandırıyor; bunun için biçim ve araç çağrısı durumu açıklanıyor. | Run'ın dönmesi ile işin anlamlı tamamlama koşulu ayrılır. İçerik doğruluğuna geçiş bu kuraldan çıkmaz; bütün guardrail seçenekleri araştırılmadı. |
| **NIST-VV:** [verification](https://csrc.nist.gov/glossary/term/verification) ve [validation](https://csrc.nist.gov/glossary/term/validation), Definitions ve kaynak etiketleri | NIST SP 800-160v1r1 / ISO 9000:2015 etiketli kullanımlar belirtilmiş gereklilik ve amaçlanan kullanım gerekliliğini ayırıyor. Aynı sayfalarda kimlik ve başka bağlamlara ait kullanımlar da var. | Verification/Validation için seçilen yerel ayrım bu girdilerle bağlantılıdır; NIST'in tek tanımı veya tüm standartların tam okuması diye sunulmaz. |
| **NIST-P:** [Permission](https://csrc.nist.gov/glossary/term/permission), NISTIR 7316 kaynaklı Definitions | Sistemde belirli eylemi yapma izni anlatılıyor. | Somut Permission kullanımına dayanak. İş düzeyindeki Authority ile ilişki bizim yerel açıklamamızdır; kaynak iki katmanlı zorunlu mimari tarif etmiyor. |
| **Scrum-DoD:** Ken Schwaber / Jeff Sutherland, [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html), Increment; Commitment: Definition of Done | Increment doğrulanmış ve kullanılabilir olmalı; Done ürünün gerekli kalite ölçütleriyle tanımlanıyor. Sprint Review yayımlama kapısı olarak tanımlanmıyor. HTML sayfası Kasım 2020 sürümünün aktarımı olduğunu belirtiyor. | Completion'ı doğrulamadan zorunlu olarak önceye koyan şemaya karşı örnek. Scrum rollerini/akışını benimsemiyoruz; bütün guide veya PDF okunmadı. |
| **GH-Deploy:** [GitHub, Reviewing deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments), Approving or rejecting a job | Onay ve diğer koruma kuralları sağlanınca iş ilerler; environment secrets'a erişim açılır. Ret işi başarısız yapar. | Bir sonuca ilişkin inceleme, işlemi yürütme izni ve gerçekleşen etki ayrı anlatılır. Özellik kullanılabilirliği plan/ortama bağlı; mevcut repository'de etkinliği kontrol edilmedi veya ayar değiştirilmedi. |
| **OA-Approval:** [OpenAI Agents SDK, Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/), giriş; How the approval flow works; Automatic approval decisions | Araç için gereken karar yürütmeden önce alınır; bazı araç türlerinde kodla karar verilip insan için duraklamadan devam edilebilir. | Her eylemde yeni insan onayı zorunlu sonucu çıkarılmaz. Approval'ın içerik kalitesi sertifikası olduğu veya bütün araçların aynı otomasyon desteğine sahip olduğu söylenmez. |

**WM-Closure — mevcut araştırmanın seçici yeniden kullanımı:** Katalogdaki ilgili satır → [META](../research/studies/work-management-project-control/META.md) → [STATE](../research/studies/work-management-project-control/STATE.md) → [METHOD](../research/studies/work-management-project-control/METHOD.md) → [U10 kapanış](../research/studies/work-management-project-control/10-CLOSURE-EVALUATION.md) okundu. Okuma tabanı `2a598bc881ecace8d5f2c36c2aeb626ada578778`; U10 blob `e140a0cac67d41af1d3b45dfdddf1eccedfcc860`. Katkısı: aktör beyanı, iş kapanışı, entegrasyon ve gerçekleşen sonucu tek status sanmamayı desteklemesi. Bu tur sekiz dış hedefin kaynakları yeniden doğrulanmadı; study'nin kapanışı veya yetkisi değişmedi.

**Yerel yorumlar:** İşin tamamlama ölçütleri doğrulamayı içerebilir; Authority iş kapsamını, Permission somut işlemi nitelemek için kullanılıyor. R1'e ait kanıt/izni değişmiş R2'ye veya başka hedefe taşımak ayrıca gerekçelendirilir. Bunlar [WORKING'de](WORKING.md#tamamlanma-ve-yayim) seçilmiş kullanım sınırlarıdır; kaynakların tamamı aynı terminolojiyi benimsemiş sayılmaz.

**İnceleme sonucu:** Taslak-var/kontrol-yok; kontrol tamamlama koşuluyken başarısız; iç paylaşım yetkisiyle kamusal yayım; sürüm veya hedef değişimi; izin-var/hizmet-yok; iptal edilmiş iş durumları metin üzerinde karşılaştırıldı. “Her duruş tamamlanmadır”, “her doğrulama kapanıştan sonradır” ve “olumlu kanıt yayımlama iznidir” yorumları bu karşılaştırmalarda korunamadı. Düzeltilen anlatım önceki model/oturum örneğiyle birleştirildi. Bu, bağımsız test veya ürün etkinliği bulgusu değil; sınırlı kaynak karşılaştırması ve yerel kavram düzeltmesidir.

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
