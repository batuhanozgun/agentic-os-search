# Agent — Çalışma Kapsamı ve Dönüş Sorusu

**Statü:** Agent U01/U02 araştırmaları tamamlandı ve Agent artık tek başına aktif karar yüzeyi değildir. Agent'ın working tanımı [ilk 10-terim batch'inde](../../synthesis/CORE-TERMS-WORKING-v0.1.md) Model, LLM, Actor, Role, Run, Session, Workflow, Tool ve Harness ile birlikte yer alır; **kabul edilmiş değildir**. Güncel odak [program STATE](../../STATE.md)'dedir.

## Ana soru

Agent sözcüğü ilgili kaynaklarda hangi şeyleri adlandırıyor ve bizim teknik konuşmalarımızda hangi kapsamı kastettiğimizi nasıl açık tutabiliriz?

Amaç “Agent'ın evrensel doğru tanımı”nı seçmek veya SOUL'da hangi agent'ların bulunacağını tasarlamak değildir. Kaynaklarla bağlantılı, gerekçeli ve karşılıklı anlaşılmış yerel kullanıma ulaşmak hedeflenir. Gerekirse tek bir varsayılan anlam yerine nitelemeli birkaç kullanım ele alınır.

## Mevcut dayanak ve dönüş noktası

[U01](U01-SOURCE-USES.md), Agent kelimesinin genel AI, yazılım-agent geleneği, güncel LLM uygulama rehberleri ve framework belgelerinde farklı seviyelerde nesnelere işaret edebildiğini gösterdi.

[U02](U02-AGENT-MODEL-BOUNDARY.md), bizim konuşmalarımız için ilk yük taşıyan komşuyu açtı:
- model/LLM ile Agent aynı şey değildir;
- Agent yapılandırması ile belirli run aynı şey değildir;
- tool kullanabilmek tek başına genel Agent sınırı değildir;
- workflow/Agent çizgisi kaynaklara göre değişebilir ve source-local etiket korunmalıdır.

Bu iki araştırma ilk batch'in zeminidir. Önceki [AGENT-BOUNDARY-CANDIDATE-v0.1](../../synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md) ara sentez olarak korunur; aktif working tanım [CORE-TERMS-WORKING-v0.1](../../synthesis/CORE-TERMS-WORKING-v0.1.md)'dedir.

## Batch içinde seçilen çalışma tanımı

U03 batch'i, önceki A/B ayrımından daha dar seçeneği working tanım olarak aldı: Agent, bir Model/LLM etrafında yapılandırılmış ve yürütmede en az bazı seçimleri modelin yaptığı AI yürütme birimidir.

Bu seçim accepted reference değil; Actor/Role, Run/Session, Workflow/Tool ve Harness ile çakışma kontrolü yapılabilen çalışma tanımıdır. Yeni çakışma çıkarsa fine-tune edilir.

## Henüz zorunlu olmayan komşular

Actor/Role/Identity, hazır/custom agent, model family/product/provider ve session/conversation/instance soruları açık kalır. Bunlardan biri ancak Agent adayının kapsamını maddi biçimde değiştiriyorsa sonraki sınırlı komşu araştırması olur.

Özellikle:
- Agent “sorumluluk üstlenen actor/role-instance” anlamında kullanılmak istenirse Actor/Role sınırı;
- hazır/custom ayrımı tanımın parçası görülürse construction/provenance;
- model adları üzerinden family/product/provider farkı karar taşıyorsa Model terminolojisi
açılabilir.

Bunlar sabit sıra veya checklist değildir.

## Kaynağa dönüş

[Studies kataloğu](../../../research/studies/CATALOG.md) → seçilen META/STATE/INDEX → gereken bulgu ve birincil kaynak yolu kullanılır. [EXP-002 TERMS](../../../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md) eski konuşmada Agent/Model/Actor/Role karışıklığını gösterir; dış dünya tanımının kanıtı değildir.

U01 ve U02'nin kaynakları kendi dosyalarında tutulur. Güncel model/ürün davranışı veya adı yük taşıdığında tarihli birincil kaynak yeniden doğrulanır.

## Dönüş ve kabul sınırı

Açık soru kalması tek başına daha fazla araştırma emri değildir. Agent için sıradaki iş artık tek-terim onayı değil; batch düzeyinde gerçek kullanım ve komşu tanımlarla çakışma görürsek ilgili sınırı düzeltmektir.

Kaynak araştırması, sentez adayı, kabul edilmiş yerel kullanım ve SOUL/Development OS tasarımı ayrı statülerdir. [METHOD](../../METHOD.md) işleyişi, STATE mevcut turun sınırını taşır.
