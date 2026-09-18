# Agent — Çalışma Kapsamı ve Dönüş Sorusu

**Statü:** [U01](U01-SOURCE-USES.md) ilk kaynak kullanımları ve [U02](U02-AGENT-MODEL-BOUNDARY.md) Model/LLM–run–workflow sınırları hazırlandı. İlk yerel kullanım adayı [Agent çekirdek sınırlar sentezinde](../../synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md) bulunuyor; **kabul edilmiş değildir**. Güncel odak, yetki ve yayın durumu [program STATE](../../STATE.md)'dedir.

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

Böylece artık bütün komşuları bitirmeden ilk yerel kullanım adayı tartışılabilir. Aktif değerlendirme [AGENT-BOUNDARY-CANDIDATE-v0.1](../../synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md)'dedir.

## Değerlendirilmesi gereken somut nokta

Aday iki kapsamı ayırır:

1. **Geniş:** yapılandırılmış AI yürütme birimi.
2. **Daha dar:** bir model/LLM etrafında yapılandırılmış ve yürütmede en az bazı seçimleri modele bırakan AI yürütme birimi.

Assistant şu anda ikinci adayı daha işlevsel buluyor; bu bir repository kabulü değildir. Kullanıcı kısmi olarak yalnız “model Agent değildir” veya “Agent/run ayrıdır” gibi sınırları kabul edip pozitif tanımı açık da bırakabilir.

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

Açık soru kalması tek başına daha fazla araştırma emri değildir. Şu anda anlamlı dönüş noktası ilk yerel Agent adayının kullanıcı tarafından değerlendirilmesidir. Belirli açıklama/kapsama açık kullanıcı değerlendirmesi olmadan reference kaydı oluşturulmaz.

Kaynak araştırması, sentez adayı, kabul edilmiş yerel kullanım ve SOUL/Development OS tasarımı ayrı statülerdir. [METHOD](../../METHOD.md) işleyişi, STATE mevcut turun sınırını taşır.
