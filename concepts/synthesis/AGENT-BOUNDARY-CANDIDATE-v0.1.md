# Agent — Çekirdek Sınırlar ve Yerel Kullanım Adayı v0.1

**Tarih:** 2026-09-18. **Statü:** HISTORICAL INTERMEDIATE SYNTHESIS; **KABUL EDİLMEDİ / ACTIVE CANDIDATE DEĞİL.**
**Dayanak:** [U01](../research/agent/U01-SOURCE-USES.md) + [U02](../research/agent/U02-AGENT-MODEL-BOUNDARY.md) + yalnız konuşma kökeni için [EXP-002 TERMS](../../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md).
Bu belge evrensel Agent tanımı, SOUL tasarımı veya framework sözleşmesi değildir. A/B ayrımı daha sonra [ilk 10-terim batch'inde](CORE-TERMS-WORKING-v0.1.md) diğer kavramlarla birlikte çalışılarak dar/model-yönlendirmeli seçenek yönünde working tanıma dönüştürüldü; tarihsel gerekçe için korunur.

## 1. Şu anda hangi problemi çözebiliyoruz?

U01 kaynaklar arasında Agent kelimesinin farklı seviyelerde nesnelere verildiğini gösterdi. U02 ise bizim konuşmalarımız için en yük taşıyan ilk sınırı yeterince açıklığa kavuşturdu:

> **Model/LLM ile Agent'ı aynı nesne olarak konuşmamalıyız.**

Ayrıca Agent yapılandırması ile belirli run aynı şey değildir. Workflow sınırı ise kaynaklar arasında tek biçimli olmadığı için yerel tercihle açık tutulmalıdır.

Bu nedenle artık bütün Agent literatürünü veya bütün komşu terimleri bitirmeden ilk yerel kullanım adayını tartışabilecek kadar zemin vardır.

## 2. Kaynaklardan korunması gereken dört sınır

### A. Model/LLM ≠ Agent

OpenAI Agents SDK ve Google ADK, model seçimini/AI modelini Agent'ın kullandığı temel bileşen olarak ayrı gösteriyor. OpenAI ayrıca model adı, Model uygulaması ve ModelProvider katmanlarını ayırıyor.

**Aday repo sonucu:** çıplak model veya LLM kelimesini Agent'ın kendisi yerine kullanmayalım.

### B. Agent tanımı ≠ belirli run

OpenAI SDK'da Agent yapılandırılır, sonra Runner ile yürütülür.

**Aday repo sonucu:** bir Agent'ın ne olduğu/yapılandırıldığı ile belirli bir yürütmede ne yaptığı ayrı konuşulsun. Run için henüz daha ayrıntılı ortak tanım seçmek zorunda değiliz.

### C. Tool-capability tek başına Agent sınırı değil

OpenAI'de tools opsiyonel; Anthropic'te tools “augmented LLM”de de bulunabilir.

**Aday repo sonucu:** “tool kullanabiliyor” veya “aksiyon alabiliyor” ifadesi tek başına Agent tanımımızın gerekli/yeterli koşulu yapılmasın.

### D. Kaynağın Agent etiketi bizim yerel anlamımızı belirlemez

Google ADK deterministik orchestration bileşenlerine “workflow agents” diyebilir; Anthropic ise workflow ve agent arasında farklı bir sınır çizer.

**Aday repo sonucu:** dış kaynakta Agent adı geçiyorsa o kaynağın anlamını koruyalım; bizim varsayılan anlamımıza otomatik çevirmeyelim.

## 3. Yerel kullanım için iki makul aday

### Aday A — geniş “yapılandırılmış AI yürütme birimi”

> **Agent:** Bir modeli/LLM'i, talimatları ve gerektiğinde araçlar ile runtime davranışlarını belirli bir işi yürütmek üzere bir araya getiren yapılandırılmış AI yürütme birimi.

**Artısı:** OpenAI Agents SDK ve Google LlmAgent kullanımına yakın; modelden açıkça ayrılıyor; tools zorunlu değil.

**Riski:** Çok basit bir tek-model çağrısı veya yalnız prompt'la yapılandırılmış LLM de bu ifadeye kolayca Agent sayılabilir. Bizim “agentic” diye konuşmak istediğimiz daha aktif yürütme davranışını yeterince ayırmayabilir.

### Aday B — daha dar “model-yönlendirmeli yürütme birimi”

> **Agent:** Bir model/LLM etrafında yapılandırılmış, belirli bir işi yürütürken yalnız çıktı üretmekten öte **en az bazı yürütme seçimlerini** modelin yaptığı AI yürütme birimi; talimat, araç, bağlam, handoff veya diğer runtime imkanları bu birimin sözleşmesine göre eklenebilir.

**Artısı:** Model ile Agent'ı ayırırken Anthropic'in “process/tool use üzerinde model kontrolü” ayrımının önemli kısmını korur. Basit “LLM çağrısı = Agent” genişlemesini azaltır.

**Riski:** “En az bazı yürütme seçimleri” eşiğinin ne kadar güçlü olması gerektiği henüz kesin değil. Google'ın deterministic workflow agent sınıfları bizim çıplak Agent kullanımımızın dışında kalır; bu bilinçli bir yerel tercih olur, onların adlandırmasının yanlış olduğu iddiası değil.

## 4. Assistant'ın mevcut önerisi

**Aday B'yi repo-içi varsayılan çıplak Agent kullanımı için daha işlevsel buluyorum**, fakat henüz kabul edilmiş değildir.

Gerekçe:

1. Kullanıcının önceki kaba sezgisindeki “LLM + eyleyebilme” yönünü koruyor ama tool kullanımını zorunlu koşul yapmıyor.
2. Model, Agent konfigürasyonu ve run seviyelerini birbirinden ayırıyor.
3. “Bir prompt verdim, model cevapladı” durumunu otomatik olarak Agent diye adlandırma baskısını azaltıyor.
4. Kaynakların farklı kullanımlarını yanlış ilan etmiyor; yalnız bizim çıplak kelime kullanımımızı daraltıyor.
5. Sonradan Actor/Role, run/session veya hazır/custom ayrımları açıldığında bu çekirdeği tamamen yıkmadan niteleme eklemeye elverişli.

## 5. Bu aday kabul edilirse şimdilik nasıl konuşuruz?

Aşağıdaki örnekler **öneridir**, kabul kaydı değildir.

- “Bu agent hangi modeli kullanıyor?” → anlamlı; Agent ile model ayrı.
- “Agent'ı başka modele taşıyalım.” → model seçimi değişebilir, Agent'ın diğer sözleşmesi aynı kalabilir.
- “Agent'ı tanımladık ama henüz çalıştırmadık.” → yapılandırma ile run ayrı.
- “Bu workflow iki agent ve deterministik kontrol adımları içeriyor.” → workflow ve Agent aynı şey olmak zorunda değil.
- “Google ADK bunu workflow agent diye adlandırıyor.” → source-local ad korunur; bizim çıplak Agent kullanımımıza zorla çevrilmez.

Şu ifadeler ise şimdilik fazla belirsiz kalır:
- “Role bir agent'tır.”
- “Her actor bir agent'tır.”
- “Agent instance = session.”
- “Hazır agent ile custom agent iki temel agent türüdür.”

Bunların hiçbiri bu adayla kabul edilmiş olmaz.

## 6. Kullanıcı değerlendirmesi gereken exact nokta

Bu turda ortak referansa geçirilecek bir kayıt yok. Değerlendirilmesi gereken somut tercih şudur:

> **Bizim repo ve konuşmalarımızda çıplak Agent kelimesi Aday B'deki daha dar, model-yönlendirmeli yürütme birimini mi anlatsın; yoksa Aday A'daki daha geniş yapılandırılmış AI yürütme birimini mi?**

Kısmi değerlendirme mümkündür. Örneğin “model Agent değildir” ve “Agent/run ayrıdır” kabul edilip Agent'ın pozitif tanımı açık bırakılabilir.

## 7. Sonraki araştırmayı ne tetikler?

Adayı değerlendirmek için şu anda Actor/Role veya hazır/custom araştırmasının tamamlanması zorunlu görünmüyor.

Ancak kullanıcı Agent'ı “sorumluluk üstlenen actor” veya “role-instance” düzeyinde kullanmak istiyorsa **Actor/Role sınırı** yük taşıyan komşu olur. Kullanıcı “hazır agent mı custom agent mı?” ayrımını Agent'ın tanımının parçası görüyorsa **construction/provenance** sorusu açılır. Model adları üzerinden konuşurken family/product/provider ayrımı karar taşıyorsa **Model terminolojisi** bir sonraki sınırlı komşu olur.

Bu tetikler önceden seçilmiş sıra değildir.
