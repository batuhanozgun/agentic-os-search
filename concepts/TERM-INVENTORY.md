# Terim Gündemi ve Keşif Bağlantıları

**Durum:** başlangıç gündemi ve kaynaklı keşif yönlendirmesi; tanım, eşanlamlılık listesi, zorunlu araştırma sırası, kavram hiyerarşisi veya eksiksiz repository taraması değildir. Listede olmak terimin benimsenmesi veya karşılığında bileşen kurulması anlamına gelmez. Güncel odak, yetki ve sıradaki iş yalnız [STATE](STATE.md)'tedir.

## Köken

G1: [EXP-002 kullanıcı mesajları](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/sources/conversation/USER-MESSAGES.md), özellikle U001 ve U009–U010.

G2: [EXP-002 geçici terim kaydı](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md).

G3: [Context/Memory/Harness araştırması](../research/studies/context-memory-harness-engineering/STATE.md).

G4: Bu programı hazırlayan konuşmadaki başlangıç listesi; tanım kabulü değildir.

G5: [Agent U01](research/agent/U01-SOURCE-USES.md); ilk sınırlı kaynak incelemesi.

G6: U01 sonrası yöntem konuşmasındaki kullanıcı örnekleri ve assistant açıklamaları; [PURPOSE](PURPOSE.md) kökeni ve kabul sınırını taşır.

G7: [Agent U02](research/agent/U02-AGENT-MODEL-BOUNDARY.md); Model/LLM, run ve workflow sınırları için hedefli kaynak incelemesi.

G8: [Core Terms U03](research/U03-CORE-TERMS-BATCH1.md) ve [working local reference v0.1](synthesis/CORE-TERMS-WORKING-v0.1.md); ilk 10 bağlı terim için batch çalışması.

G9: [Core Terms U04](research/U04-CORE-TERMS-BATCH2.md) ve [working local reference v0.2](synthesis/CORE-TERMS-WORKING-v0.2.md); Runtime, Context, Memory, Identity, Capability, Authority, Permission, Orchestration, Handoff ve Subagent'i ekleyen ikinci batch.

## Başlangıç odağı ve devralınan bağlantılar

**Agent** başlangıç terimiydi; çalışma artık tek-terim odağından ilk bağlantılı batch'e ilerledi: [U01](research/agent/U01-SOURCE-USES.md) → [U02](research/agent/U02-AGENT-MODEL-BOUNDARY.md) → [U03](research/U03-CORE-TERMS-BATCH1.md) → [10-terim working reference](synthesis/CORE-TERMS-WORKING-v0.1.md). Kabul edilmiş ortak referans hâlâ yoktur.

| Bağlantı / soru | Köken ve güncel statü | Bu kayıt neyi kararlaştırmıyor? |
|---|---|---|
| Çevrede eyleme, hedef ve özerklik anlatımları | G5, U01 S1–S2; kaynak farkı olarak korunuyor. | Yerel Agent kullanımımız için gerekli/yeterli koşullar seçilmedi. |
| LLM/model ile Agent ayrımı | G5 + G7; **yük taşıyan sınır araştırıldı**. Model/LLM modern agent düzenlerinde Agent'ın kullandığı temel bileşen olarak ayrılabiliyor. | Model family/product/provider terminolojisinin tamamı veya Agent pozitif tanımı kabul edilmedi. |
| Workflow ve model-directed control | G5 + G7; Anthropic ve Google farklı sınırlar gösteriyor. | Evrensel workflow/Agent çizgisi kurulmadı. |
| Agent yapılandırması ile belirli run | G5 + G7; OpenAI SDK'da ayrım somut. | Run/session/conversation/instance eşitlenmedi. |
| Tool / action capability | G5 + G7; tek başına gerekli/yeterli Agent ölçütü olarak desteklenmiyor. | Yerel Agent tanımında eylem/control eşiği henüz kabul edilmedi. |
| Actor, role, identity | G1/G2; henüz aktif komşu araştırması değil. | U01/U02 bunların tam dış kaynak araştırmasını yapmış sayılmaz. |
| Hazır/custom agent | G6; yöntem örneği ve eski konuşma kökeni. | İki temel Agent türü olduğu veya tanımın parçası olduğu kabul edilmedi. |
| Model family / ürün / provider | G6 + G7'de provider ayrımının bir kısmı göründü. | Endüstri-geneli ürün/family şeması araştırılmadı. |

Bu tablo çalışma sırası değildir. İlk iki batch toplam 20 terimi aynı working map üzerinde oturttu. Sonraki batch mevcut v0.2'de en fazla çakışma/boşluk temizleyecek kavramlardan seçilir.

## Korunan başlangıç grupları

| Gezinme grubu | Terimler | Köken |
|---|---|---|
| Agent çevresindeki ifadeler | Agent; Model; Actor; Role; Role-instance; Identity | G1/G2/G4 |
| Sistem ve çalışma düzeni adları | Agentic AI; Agentic system; Multi-agent system; Harness; Runtime | G1/G3/G4 |
| İşleyiş ve koordinasyon | Loop; Agent loop; Workflow; Graph; DAG; Orchestration; Multi-agent orchestration | G1/G3/G4 |
| Bilgi ve devam | Context; Memory; State; Work state; Persistence; Continuity; Recovery | G1/G2/G3/G4 |
| Araçlar ve ortam | Tool; Workspace; Environment; Sandbox; Data access; Capability | G1/G2/G4 |
| Amaç, yetki ve değerlendirme | Goal; Authority; Permission; Policy; Verification; Observability | G1/G2/G3/G4 |
| Bilgiyle çalışma mekanizmaları | RAG; Knowledge graph; Fine-tuning; CAG; Long context | G2/G3/G4 |

## Bileşik engineering / management ifadeleri

Harness engineering; Loop engineering; Graph engineering; Context engineering; Context management; Memory engineering; Memory externalization; Work state management; Goal maintenance; Tool selection; Authority control.

Köken G1/G2/G3/G4. Örneğin loop ile loop engineering aynı araştırma sorusu değildir. Bileşik ifadenin yararlı bir ayrım taşıyıp taşımadığı araştırılır; zorunlu sözlük maddesi sayılmaz.

## Gerektiğinde açılacak yardımcı ifadeler

| İfadeler | Açılma nedeni |
|---|---|
| LLM; inference; model call | Model ile modelden yararlanma hakkında gereken ayrımlar. |
| Session; conversation; run; instance | Ürün, konuşma, belirli çalışma/yürütme ve örnek ayrımı. |
| Subagent | Başka/alt agent ifadesinin kullanımını anlamak. |
| Framework; SDK; API | Hazır sistem kullanımı ile geliştirme olasılıklarını açıklamak. |
| Prompt; instruction; skill; tool calling | Çalışma biçiminin tarif ve gerçekleştirilmesi soruları. |

## Ayrı tutulan adlar

Claude Code, Codex, ChatGPT, Hermes ve gstack gibi ürün/proje adları örnek veya kaynak olabilir; agent/model/harness ile otomatik eşitlenmez. Adın hangi tarihli ürün, model veya çalışma yüzeyini işaret ettiği ilgili araştırmada doğrulanır.

SOUL, Development OS ve diğer projeye özgü geçici ifadeler ilk genel kavram araştırmasının dışında tutulur. Bunların gündemde ayrı tutulması eski görüşleri silmez veya yanlış ilan etmez.

## Güncelleme sınırı

Yeni terim/işlev/ilişki sorusu için nerede karşılaşıldığı, hangi anlam ayrımını etkilediği ve ne statüde olduğu kısa biçimde yazılır. Mevcut odak için engel olduğu, ertelendiği veya kaynak-yerel tutulduğu gerekçelendirilir. Güncel iniş/dönüş noktası STATE'te, ayrıntılı kanıt kendi çalışma belgesinde kalır.

Eksik karşılık, mevcut tanıma zorlama veya otomatik paket açma gerekçesi değildir. Envanter büyüklüğü başarı ölçütü olmaz. İlgili küçük kümede yeterli zemin oluşursa bütün envanteri beklemeden ortak kullanım adayı [METHOD](METHOD.md) uyarınca tartışılabilir.
