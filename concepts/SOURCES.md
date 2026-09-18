# Kavram Çalışması — Kaynak Notları

Bu dosya taslaktan kanıta geri dönüş yoludur; yeni bir kaynak araştırması değildir. **2026-09-18 sadeleştirmesinde dış kaynaklar tekrar okunmadı.** Aşağıdaki U01–U06 bağlantıları, bakım öncesi main commit'ine sabitlenmiş tarihsel araştırma kayıtlarıdır. Önceki “canlı belgeler okundu” ifadeleri bu bakımın doğrulaması sayılmaz.

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

Aşağıdakiler **U01'in eski okuma kaydının özeti**dir; bu tur yeniden gözlem değildir. Tam bölüm ve sınırlar yukarıdaki U01 bağlantısındadır.

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
