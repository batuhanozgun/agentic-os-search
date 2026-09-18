# Agent — U01: Kaynaklara Bağlı İlk Kullanım İncelemesi

**Tarih / erişim:** 2026-09-18. **Seviye:** 1, tekil terim araştırması. **Sonuç statüsü:** ilk sınırlı araştırma dilimi; kaynak kullanımı gözlemleri ve açıkça ayrılmış yorumlar. Agent araştırmasının bütünü tamamlanmadı. Ortak tanım, seviye 2 sentezi, kabul edilmiş referans veya SOUL/Development OS kararı değildir. Güncel iş ve yayın otoritesi [program STATE](../../STATE.md); kapsam [BRIEF](BRIEF.md).

## Soru ve kapsam

Agent sözcüğünün kaynaklarda hangi nesneyi veya davranışı adlandırdığı araştırıldı. Bir tanım seçilip diğerleri ona göre elenmedi. Genel AI ders kitabı, erken yazılım-agent tartışması, LLM uygulama rehberi ve geliştirme belgeleri yan yana okundu. Aşağıdaki başlıklar evrensel agent türleri değil, belirli kaynakların kullanımlarıdır.

Bu dilim, aynı kelimenin aynı teknik sözleşmeye işaret etmediğini somut örneklerle göstermek için yeterlidir; bütün alanı temsil ettiği veya gerekli/yeterli koşulları kapattığı iddia edilmez. Standartlar, reinforcement learning geleneği, gündelik ürün adlandırmaları ve role/identity/instance ilişkileri kapsamlı araştırılmadı.

## Mevcut araştırmadan geri kazanılanlar

[Studies kataloğu](../../../research/studies/CATALOG.md) üzerinden iki aday daraltıldı. [Context/Memory/Harness META](../../../research/studies/context-memory-harness-engineering/META.md), STATE ve INDEX tam; [Harness incelemesinin](../../../research/studies/context-memory-harness-engineering/03-HARNESS-ENGINEERING.md) ilk 120 satırı seçici okundu. Katkısı model, çevresindeki yürütme düzeni ve kontrol sorumluluklarını peşinen eşitlememe uyarısıdır. Oradaki çalışma tanımı genel Agent tanımı olarak alınmadı; study yeniden açılmadı.

[Multi-agent patterns META](../../../research/studies/multi-agent-patterns/META.md) tam okundu; koordinasyon odaklı keşif statüsü nedeniyle Agent tanımının kanıtı yapılmadı. EXP-002'nin rolü [PURPOSE](../../PURPOSE.md) üzerinden iletişim sorusunun geçmişi olarak korundu; eski SOUL diyaloğu dış-kaynak incelemesinin yerine geçirilmedi. Bu kayıtlar aynı eski çalışmayı bağımsız doğrulama saymaz.

## S1 — Genel AI anlatımında çevrede eyleyen varlık

**Kaynak:** David L. Poole ve Alan K. Mackworth, *Artificial Intelligence: Foundations of Computational Agents*, 3. basım, §1.1 “What is Artificial Intelligence?” [S1]. Sayfada telif yılı 2023, HTML üretim tarihi 2025-06-28. **Okuma:** §1.1'in açılış tanımı ve insanla birlikte çalışma açıklaması; kitabın tamamı değil.

**Doğrudan kullanım:** Agent çevrede eyleyen şey olarak geniş tutulur; termostat kaynakta verilen örneklerdendir. Zekânın derecesi ve akıllıca davranışın nitelikleri ayrıca ele alınır. “Computational agent” için eylem kararlarının hesaplama ile açıklanabilmesi belirtilir.

**Yorum / sınır:** Bu kullanımdan LLM zorunluluğu çıkmaz. Termostatı yalnız LLM kullanmadığı için dışlamak kaynağın kendi örneğiyle çelişir. Buna karşılık bu geniş kullanım, termostatın güncel LLM rehberlerindeki Agent ölçütünü karşıladığını göstermez.

## S2 — Yazılım-agent tartışmasında zayıf ve güçlü agency

**Kaynak:** Michael Wooldridge ve Nicholas R. Jennings, “Intelligent agents: theory and practice”, *The Knowledge Engineering Review* 10(2), 115–152, 1995 [S2]. **Okuma:** PDF'nin ilk beş sayfası görsel olarak açıldı; tanım dayanağı §1.1–1.1.3, basılı s.116–117. Makalenin bütünü okunmadı.

**Doğrudan kullanım:** Zayıf agency anlatımı özerklik, sosyal etkileşim yeteneği, çevreye tepki ve hedefe dönük inisiyatif özelliklerini birlikte verir. Güçlü kullanım bunlara inanç, bilgi ve niyet gibi zihinsel kavramlarla anlatımı ekler. Mobilite gibi başka nitelikler ayrıca tartışılır; aynı zorunlu liste değildir.

**Yorum / örnek:** Makalenin yazılım ortamındaki komut ve geri bildirim örneği fiziksel robotu zorunlu kılmaz. İnanç/niyet dilinin bu gelenekte bulunması, bütün agent'lara bilinç veya kişilik atfetmeye yetmez. Makalenin tanım uzlaşmazlığı gözlemi 1995 bağlamına aittir; bugünün tam taraması sayılmaz.

## S3 — Anthropic yazısında workflow ile Agent ayrımı

**Kaynak:** Erik S. ve Barry Zhang / Anthropic, “Building effective agents”, sayfada ilk yayın 2024-12-19 [S3]. **Okuma:** “What are agents?”, augmented LLM, workflow örüntüleri ve “Agents” bölümleri. Erişilen canlı sayfa değişmiş araç ekosistemine dair not içerir; değişmemiş 2024 arşivi veya bugünkü bütün Anthropic ürünlerinin sözleşmesi değildir.

**Doğrudan kullanım:** Önceden yazılmış akışla LLM ve araçları yöneten sistem workflow; kendi sürecini ve araç kullanımını dinamik yöneten LLM'li sistem Agent olarak ayrılır. Reklam metni üretip çevirmek workflow örneğidir. İnsan kontrol noktaları Agent anlatımıyla bağdaşır.

**Önemli sınır:** Aynı yazı, LLM'nin alt işleri dinamik belirlediği orchestrator-workers düzenini ve geri bildirim döngülü evaluator-optimizer düzenini de workflow adlandırır. Bu nedenle “her dinamik karar” veya “her döngü” yeterli ayırıcı sayılamaz. Kontrolün kapsamını kesinleştiren koşul bu dilimde açık bırakıldı.

## S4 — OpenAI rehberinde kullanıcı adına işi yürüten LLM sistemi

**Kaynak:** OpenAI, *A practical guide to building agents* [S4]. **Okuma:** basılı s.4 “What is an agent?” ve s.7 “Agent design foundations”; PDF görüntüleri ve ilgili metin. İncelenen sayfalarda yayın tarihi/sürüm saptanmadı; tüm rehber okunmadı.

**Doğrudan kullanım:** Kullanıcı adına işi belirli bağımsızlıkla gerçekleştiren sistem anlatılır; LLM'nin workflow yürütmesini ve kararlarını yönetmesi, araçlar ve koruyucu sınırlar öne çıkar. Yürütmeyi LLM'nin kontrol etmediği basit sohbet/sınıflandırma uygulamaları bu kapsamın dışında tutulur. Model, araçlar ve talimatlar rehberin tasarım bileşenleridir.

**Yorum / sınır:** LLM'nin yalnız duygu sınıflandırdığı, sonraki adımların kodca belirlendiği uygulama bu rehberin dışlama örneğine uyar. Kontrolü insana geri verme Agent ile çelişmez; bağımsızlık sınırsız izin anlamına gelmez. Bileşen anlatımı zorunlu SOUL mimarisi veya güvenilirlik kanıtı yapılmadı.

## S5 — OpenAI Agents SDK'da yapılandırma ile çalıştırma

**Kaynak:** OpenAI Agents Python SDK, “Agents” [S5a] ve “Running agents” [S5b]. **Okuma:** giriş/temel yapılandırma; Runner çalıştırma arayüzleri ve “The agent loop”. Canlı belgeler 2026-09-18'de okundu; kurulu paket sürümü veya kaynak-kod commit'i sabitlenmedi. Kod çalıştırılmadı.

**Doğrudan kullanım:** `Agent`, talimatlar, model ve araçlar gibi alanlarla yapılandırılan SDK nesnesidir; `tools` zorunlu constructor alanı değildir. Çalıştırma `Runner.run`, `run_sync` veya `run_streamed` ile ayrıdır. Belgelenen döngü final output, handoff ve araç sonuçlarına göre ilerler; ilk model adımında final output ile de bitebilir.

**Yorum / sınır:** `Agent(...)` oluşturmak yeni model eğitmekle veya yürütmeyi başlatmakla aynı işlem değildir. Bir SDK nesnesinin bulunması S4'teki davranış ölçütlerinin karşılandığını kanıtlamaz. Tersine, tek çalışmanın kısa sürmesi de yapılandırılmış sistemin bütün yeteneklerini göstermez. Kalıcı kimlik/ayrı süreç sonucu çıkarılmadı.

## S6 — Google ADK'da Agent ve deterministik workflow-agent adı

**Kaynak:** Google ADK “Agents” [S6a] ve “Template agent workflows” [S6b]; eski `google.github.io/adk-docs` adresleri erişimde `adk.dev` alanına yönlendi. **Okuma:** agent giriş açıklaması ve template-workflow sayfasının asıl içeriği. Kurulum veya çalışma testi yok.

**Doğrudan kullanım:** Genel giriş Agent'ı bir hedefe yönelik yürütme birimi olarak sunar. Template workflow'lar, workflow agents adıyla da anılan kontrol bileşenleridir; sıralı/paralel/döngülü yürütmenin orkestrasyonu için AI modeline danışmak zorunda değildir. Alt agent'lar yine LLM kullanabilir.

**Sürüm sınırı / yorum:** Sayfa, Python ve Go için ADK 2.0'dan itibaren bu şablonların graph/dynamic workflow'larla yer değiştirdiğini açıkça belirtir. Korunan `SequentialAgent` örneği adlandırma kanıtıdır, güncel önerilen mimari değildir. “Agent adı taşıyan her bileşende akışı LLM seçer” genellemesine karşı örnektir; bütün uygulamanın LLM'siz olduğunu göstermez.

## Bu dilimin kazandırdığı ayrım

**Kaynaklar arası sınırlı yorum:** Kullanımdaki farklılık yalnız bir özelliğin var/yok oluşundan ibaret değildir; sözcüğün işaret ettiği şey de değişebilir. S1'in geniş eyleyen varlığı, S2'nin nitelik kümesi, S3/S4'ün LLM ile yönetilen uygulaması ve S5/S6'nın geliştirme birimleri aynı ölçekte eşanlamlı kabul edilemez. Bu, benimsenmiş sınıflandırma değil, inceleme uyarısıdır.

Adlandırma, yapılandırmanın neler yapabildiği ve belirli çalışmada gerçekten ne olduğu ayrı kanıt ister. Kaynak açıklaması kendi kullanımına doğrudan kanıttır; ürünün etkili veya güvenilir çalıştığının bağımsız doğrulaması değildir. OpenAI rehberi ile SDK belgeleri veya aynı kurumun farklı sayfaları bağımsız oylar olarak sayılmadı.

## Açık sorular ve sınırlı devam adayı

**Öncelikli devam adayı:** “Agent oluşturmak” belirli kaynakta neye karşılık geliyor: yapılandırma nesnesi hazırlamaya mı, bunu çalıştırmaya mı, daha kalıcı bir yürütme birimine mi? S5 ilk ikisinin ayrımını açtı; ürün/run/session/instance/role/identity ilişkisini kapatmadı. Sonraki araştırma bu ifadeyi birkaç somut kaynak örneği üzerinden derinleştirebilir; terimler için ayrı birer tam araştırma otomatik başlatılmaz.

S3'te dinamik alt görev seçimi ile bütün sürecin kontrolü arasındaki sınır ayrıca açık. Bu ayrımı keskinleştiren yeni birincil açıklama mevcut yorumu değiştirebilir. S2'deki farklı agency kullanımlarını modern ürünlere taşımak da ek gerekçe ister; kendiliğinden eşleme yapılmadı.

İlk bounded dönüş koşulu karşılandı: kaynaklı kullanımlar, somut ayrımlar ve açık sorular var. Bir sonraki dilim, ortak tanım veya tasarım bu belgenin varlığından yetki almaz; güncel yön [STATE](../../STATE.md)'dedir.

## Kanıt ve okuma sınırları

Bu çalışma kaynak okumasıdır; canlı agent deneyi, benchmark, bağımsız reviewer veya iletişim-etkililiği testi değildir. Yukarıdaki karşı örnekler kaynak anlamını sınayan okumalar; çalıştırılmış testler değildir. AIMA PDF adayları bu oturumda açılamadığı için kanıt listesine alınmadı. Erişim başarısızlığı kaynakta bilgi yokluğu değildir.

Canlı belgelerin gelecekte değişmeyeceği garanti edilmez. Tarih ve bölüm işaretleri okuma kaydını taşır, değişmez tam snapshot sağlamaz. Güncel ürün davranışına ilişkin sonraki bir karar kaynak/sürüm doğrulaması gerektirir. Bu sınırlı tarama evrensel Agent tanımı kurmaz.

[S1]: https://artint.info/3e/html/ArtInt3e.Ch1.S1.html
[S2]: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95.pdf
[S3]: https://www.anthropic.com/engineering/building-effective-agents
[S4]: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
[S5a]: https://openai.github.io/openai-agents-python/agents/
[S5b]: https://openai.github.io/openai-agents-python/running_agents/
[S6a]: https://adk.dev/agents/
[S6b]: https://adk.dev/agents/workflow-agents/
