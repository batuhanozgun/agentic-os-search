# Core Terms — Working Local Reference v0.1

**Tarih:** 2026-09-18.  
**Statü:** SUPERSEDED WORKING SNAPSHOT; ilk 10 terimin tarihsel v0.1 görünümü.  
**Kapsam:** İlk 10 bağlı terim. Evrensel sözlük veya SOUL mimarisi değildir.  
**Dayanak:** [U03 linked research](../research/U03-CORE-TERMS-BATCH1.md), Agent [U01](../research/agent/U01-SOURCE-USES.md), [U02](../research/agent/U02-AGENT-MODEL-BOUNDARY.md), mevcut Harness study ve seçili birincil kaynaklar.

Bu dosya ilk 10 terimin çalışma snapshot'ıdır. Güncel working reference [v0.2](CORE-TERMS-WORKING-v0.2.md)'dir.

## İlk 10 çalışma tanımı

### 1. Agent
**Bir Model/LLM etrafında yapılandırılmış, belirli bir işi yürütürken yalnız çıktı üretmekten öte en az bazı yürütme seçimlerini modelin yaptığı AI yürütme birimi.**

Agent Model değildir; belirli Run da değildir. Tool kullanabilir ama Tool kullanmak tek başına Agent olma ölçütü değildir.

### 2. Model
**Eğitim sonucunda oluşmuş, inference sırasında girdilerden çıktılar üreten öğrenilmiş hesaplama bileşeni; Agent'ın reasoning/generation gibi kabiliyetleri için kullandığı temel learned model.**

Model provider, ürün veya Agent ile eşit değildir.

### 3. LLM
**Dil dizileri üzerinde büyük ölçekli öğrenmeyle language understanding/generation kabiliyeti edinmiş Model türü.**

Repo kullanımında: **LLM ⊂ Model**. Dil-merkezlilik önemli değilse daha güvenli üst terim `Model`dir.

### 4. Actor
**Belirli bir Work bağlamında sorumluluk, yetki veya fiili katkı üstlenen katılımcı/yürütücü birim.**

İnsan veya Agent Actor olabilir. Her Actor Agent değildir.

### 5. Role
**Bir Work bağlamında Actor'dan beklenen görev/sorumluluk, katkı yönü ve gerektiğinde authority/permission sınırlarını tarif eden atanabilir işlevsel konum.**

Actor Role'ü üstlenir; Role Actor değildir.

### 6. Run
**Bir Agent veya Workflow'un belirli başlangıç girdisi, durum ve yürütme ayarlarıyla başlatılan; bounded stop noktasına kadar süren tek yürütme olayı.**

Bir Run birden çok model call, Tool çağrısı veya Agent handoff'u içerebilir.

### 7. Session
**Birden fazla Run veya etkileşim arasında konuşma/geçmiş/state bilgisini ilişkilendirerek devamlılık sağlayan süreklilik konteyneri.**

Session Run değildir; uzun vadeli Memory ile de otomatik eşitlenmez.

### 8. Workflow
**Belirli bir işi/sonucu gerçekleştirmek için adımların, koşulların, Actor/Agent'ların ve Tool çağrılarının nasıl sıralanıp koordine edildiğini tarif eden çalışma akışı düzeni.**

Workflow deterministic veya model-directed olabilir. Workflow Agent değildir.

### 9. Tool
**Bir Model/Agent'ın bilgi edinmek, hesaplama yapmak veya dış/iç ortamda eylem gerçekleştirmek için çağırabildiği tanımlı capability/interface.**

Tool Agent değildir; bir Agent gerektiğinde Tool olarak expose edilebilir.

### 10. Harness
**Model ve Agent'ların güvenilir, sınırlı ve devam ettirilebilir Work'e dönüşmesini sağlayan model-dışı işletim ve kontrol zemini; yürütme lifecycle'ı, Tool arayüzleri, context/memory akışı, izin/yetki kontrolleri, orchestration, verification, observability ve work continuity gibi sorumlulukları taşıyabilir.**

Harness Agent veya Workflow değildir; onları işletebilir, bağlayabilir ve sınırlayabilir.

## Kısa ilişki kuralı

```text
LLM is-a Model

Agent uses Model
Agent executes-as Run
Agent may-call Tool
Agent may-be Actor when bound to Work

Actor assumes Role

Workflow coordinates steps / Actors / Agents / Tools
Run is one bounded execution of Agent or Workflow
Session preserves continuity across Runs

Harness operates/controls the surrounding execution system
```

## Kullanım örnekleri

- “Bu **Agent** hangi **Model**i kullanıyor?”
- “Bu **LLM**, Agent'ın reasoning için kullandığı Model.”
- “Reviewer **Role**'ünü bu **Actor** üstleniyor.”
- “Aynı Agent üç ayrı **Run** yaptı.”
- “Bu iki Run aynı **Session** içinde devam etti.”
- “Bu **Workflow** iki Agent ve bir deterministik kontrol adımı içeriyor.”
- “Agent dış API'yi bir **Tool** üzerinden çağırıyor.”
- “**Harness**, Agent'ların context, Tool, verification ve continuity düzenini işletiyor.”

## Şimdilik özellikle söylemeyeceğimiz şeyler

- “Agent = Actor”
- “Agent = Role”
- “Agent = Model”
- “Session = Agent instance”
- “Workflow = Agent”
- “Tool kullanıyorsa Agent'tır”
- “Harness = Agent”
- “Her Model LLM'dir”

## Statü

Bu batch, assistant tarafından araştırma ve çakışma kontrolüyle oluşturulmuş **çalışan v0.1 yerel referans adayıdır**. Kullanıcının tek tek terim değerlendirmesi beklenmez. Sonraki batch'ler ve gerçek kullanım çakışmaları bu tanımları fine-tune edebilir.

Bu snapshot ACCEPTED değildir; güncel kullanım için v0.2'ye dön.
