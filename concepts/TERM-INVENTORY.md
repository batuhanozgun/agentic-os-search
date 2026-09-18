# Terim Gündemi ve Keşif Bağlantıları

**Durum:** başlangıç gündemi ve kaynaklı keşif yönlendirmesi; tanım, eşanlamlılık listesi, zorunlu araştırma sırası, kavram hiyerarşisi veya eksiksiz repository taraması değildir. Listede olmak terimin benimsenmesi veya karşılığında bileşen kurulması anlamına gelmez. Güncel odak, yetki ve sıradaki iş yalnız [STATE](STATE.md)'tedir.

## Köken

G1: [EXP-002 kullanıcı mesajları](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/sources/conversation/USER-MESSAGES.md), özellikle U001 ve U009–U010.

G2: [EXP-002 geçici terim kaydı](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md).

G3: [Context/Memory/Harness araştırması](../research/studies/context-memory-harness-engineering/STATE.md). Kaydın bulunması buradaki tanımların ortak kullanım olarak kabulü değildir.

G4: Bu programı hazırlayan mevcut konuşmada assistant'ın önerdiği başlangıç listesi; kullanıcı yolu uygun buldu. Bu kökeni eski kaynağa yanlış atfetme.

G5: [Agent U01](research/agent/U01-SOURCE-USES.md); ilk sınırlı kaynak incelemesi. Buradaki bağlantı kaydı onun bulgularını yeniden araştırmaz veya yeni bir sentez yapmaz.

G6: U01 sonrası yöntem konuşmasındaki kullanıcı örnekleri ve assistant açıklamaları; [PURPOSE](PURPOSE.md) kökeni ve kabul sınırını taşır. Bu örnekler dış kaynak bulgusu, doğrulanmış ürün adı veya kabul edilmiş tanım değildir.

## Başlangıç odağı ve devralınan bağlantılar

**Agent** başlangıç terimidir; [BRIEF](research/agent/BRIEF.md) → [U01](research/agent/U01-SOURCE-USES.md). U01 korunur; kabul edilmiş ortak tanım yoktur. Yeni oturum bu kaydı otomatik “Agent U02'ye başla” veya “bütün komşuları sırayla bitir” komutu olarak okumaz.

| Bağlantı / soru | Köken ve okuma yolu | Bu kayıt neyi kararlaştırmıyor? |
|---|---|---|
| Çevrede eyleme, hedef ve özerklik anlatımları | G5, U01 S1–S2. | Bunların yerel Agent kullanımımız için gerekli/yeterli koşullarını belirlemiyor. |
| LLM/model, kullanılan araç/talimat ve bütün sistem arasındaki ayrım | G5, U01 S3–S5. | Agent'ın zorunlu bileşen listesini veya Model'in kabul edilmiş anlamını kurmuyor. |
| Workflow, süreç kontrolü, döngü ve orkestrasyon adları | G5, U01 S3/S6; dinamik kontrol sınırı açık. | Her döngüyü Agent veya her workflow'u Agent dışı ilan etmiyor. |
| Yapılandırma ile çalıştırma; `Agent(...)`, `Runner` ve run | G5, U01 S5 ve açık sorular. | Ürün/session/instance/identity ayrımlarını kapatmıyor; `Runner`ı genel referans maddesi yapmıyor. |
| Actor, role, identity ve belirli yürütme ilişkileri | G1/G2; G5'te açık sorular olarak anılır. | U01'in bunların tam dış kaynak araştırmasını yaptığı veya hepsinin zorunlu önkoşul olduğu iddiası yok. |
| “Hazır/özel agent” ve model/LLM/ürün/aile adı ayrımı | G6'daki yöntem örnekleri; gereken eski bağlam G2 üzerinden bulunur. | Hazır–özel ikiliğinin eksiksiz seçenek alanı, verilen adların doğrulanmış ürün bilgisi veya yerel tercih olduğu iddiası yok. |

Bu tablo bir komşuluk keşif kaydıdır; yeni kaynak araştırması, bağımlılık kararı veya seçilmiş öncelik değildir. Aynı soru birden fazla kökenden beslenebilir. Devamda yalnız güncel anlam sorusunu etkileyen bağlantı gerekçelendirilerek açılır; yararlı ama engel olmayan konu ertelenebilir, kaynağa özgü ad kendi bağlamında kalabilir. Karşılaşılan işlev için hemen yeni terim veya ayrı paket üretmek gerekmez.

## Korunan başlangıç grupları

Aşağıdaki satırlar yalnız gezinme gruplarıdır. Aynı satırda olmak eşdeğerlik, eş-seviye veya parça ilişkisi kurmaz.

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

Köken G1/G2/G3/G4. Örneğin loop ile loop engineering aynı araştırma sorusu değildir. Bileşik ifadenin yararlı bir ayrım taşıyıp taşımadığı araştırılır; zorunlu sözlük maddesi sayılmaz. Özgün kaynaktaki yazım korunur; bu listede arama için olağan yazım kullanılması anlam eşleme değildir.

## Gerektiğinde açılacak yardımcı ifadeler

Bunlar G4'te önerilmiştir; her birinin önceki araştırmada tam incelendiği iddia edilmez.

| İfadeler | Açılma nedeni |
|---|---|
| LLM; inference; model call | Model ile modelden yararlanma hakkında gereken ayrımlar. |
| Session; conversation; run; instance | Ürün, konuşma, belirli çalışma/yürütme ve örnek ayrımı. |
| Subagent | Başka/alt agent ifadesinin kullanımını anlamak. |
| Framework; SDK; API | Hazır sistem kullanımı ile geliştirme olasılıklarını açıklamak. |
| Prompt; instruction; skill; tool calling | Çalışma biçiminin tarif ve gerçekleştirilmesi soruları. |

## Ayrı tutulan adlar

Claude Code, Codex, ChatGPT, Hermes ve gstack gibi ürün/proje adları örnek veya kaynak olabilir; agent/model/harness ile otomatik eşitlenmez. Adın hangi tarihli ürün, model veya çalışma yüzeyini işaret ettiği ilgili araştırmada doğrulanır.

SOUL, Development OS, Baz SOUL, System Formation / Work-System Synthesis, SOUL-native intellectual baseline, intellectual inheritance, internalized core / recoverable deep knowledge ve benzeri projeye özgü geçici ifadeler ilk genel kavram araştırmasının dışında tutulur. Role-specific competence ve terminal amaç/motivasyon gibi eski konuşma ifadeleri gerektiğinde kaynak-bağlı komşu sorulardır; bugünkü ortak tanım değildir. Bunların gündemde ayrı tutulması eski görüşleri silmez veya yanlış ilan etmez.

## Güncelleme sınırı

Yeni terim/işlev/ilişki sorusu için nerede karşılaşıldığı, hangi anlam ayrımını etkilediği ve ne statüde olduğu kısa biçimde yazılır. Mevcut odak için engel olduğu, ertelendiği veya kaynak-yerel tutulduğu gerekçelendirilir; bunlar değişmez kavram sınıfları değildir. Güncel iniş/dönüş noktası ve yetki STATE'te, ayrıntılı kanıt kendi çalışma belgesinde kalır.

Eksik karşılık, mevcut tanıma zorlama veya otomatik paket açma gerekçesi değildir. Envanter büyüklüğü başarı ölçütü olmaz. İlgili küçük kümede yeterli zemin oluşursa bütün envanteri beklemeden ortak kullanım adayı [METHOD](METHOD.md) uyarınca tartışılabilir.
