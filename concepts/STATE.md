# Concepts — Güncel Durum

**Kayıt tarihi:** 2026-09-18.  
**Mevcut iş:** İlk 10 bağlı terim batch'i tamamlandı; working local reference v0.1 hazırlandı. Bu turdaki dönüş noktası batch sonucunu kullanıcıya sunmaktır.  
**Yöntem:** [METHOD v0.2](METHOD.md) — tek terim kapanışı yerine bağlantılı batch ve çakışma üzerinden fine-tune.  
**Mevcut araştırma:** Agent [U01](research/agent/U01-SOURCE-USES.md), [U02](research/agent/U02-AGENT-MODEL-BOUNDARY.md), ardından [Core Terms U03](research/U03-CORE-TERMS-BATCH1.md).  
**Aktif working reference:** [CORE-TERMS-WORKING-v0.1](synthesis/CORE-TERMS-WORKING-v0.1.md).  
**ACCEPTED reference:** Henüz yok; working batch kullanıcıya sunulduktan ve yön/itiraz görüldükten sonra statü ayrıca güncellenir.

## Bu turda oturtulan ilk 10 terim

1. Agent
2. Model
3. LLM
4. Actor
5. Role
6. Run
7. Session
8. Workflow
9. Tool
10. Harness

Bu terimler tek tek bağımsız sözlük maddeleri olarak değil, birbirlerini ayıracak şekilde tek ilişki sistemi içinde çalışıldı.

## Çalışan temel ilişkiler

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

## Current working definitions — kısa görünüm

- **Agent:** Model/LLM etrafında yapılandırılmış, yürütmede en az bazı seçimleri modelin yaptığı AI yürütme birimi.
- **Model:** Inference sırasında girdiden çıktı üreten learned computational component; Agent'ın kullandığı temel model capability.
- **LLM:** Dil understanding/generation odaklı Model türü; repo kullanımında LLM ⊂ Model.
- **Actor:** Belirli Work bağlamında sorumluluk, yetki veya fiili katkı üstlenen yürütücü/katılımcı.
- **Role:** Actor'dan beklenen görev/sorumluluk ve gerektiğinde authority/permission sınırlarını tarif eden atanabilir işlevsel konum.
- **Run:** Agent veya Workflow'un tek bounded yürütme olayı.
- **Session:** Birden fazla Run/etkileşim arasında history/state continuity taşıyan konteyner.
- **Workflow:** Adım, koşul, Actor/Agent ve Tool'ların koordinasyon düzeni.
- **Tool:** Model/Agent'ın bilgi edinmek, hesaplama yapmak veya eylem gerçekleştirmek için çağırdığı capability/interface.
- **Harness:** Model/Agent'ların güvenilir, sınırlı ve devam ettirilebilir Work'e dönüşmesini sağlayan model-dışı işletim/kontrol zemini.

Tam tanımlar ve sınırlar [working batch](synthesis/CORE-TERMS-WORKING-v0.1.md)'tedir.

## Çakışma düzeltmeleri

Bu batch aşağıdaki eşitlemeleri bilinçli olarak reddeder:

- Agent = Model
- Agent = Actor
- Agent = Role
- Agent = Run
- Run = Session
- Workflow = Agent
- Tool = Agent
- Harness = Agent
- Harness = Workflow
- Model = LLM

Bunlar evrensel ontoloji iddiaları değildir; repo içi iletişimde kaygan zemini azaltan çalışma ayrımlarıdır.

## Yeni oturumda devam yolu

Güncel AGENT ve gereken protokoller → [INDEX](INDEX.md) → bu STATE → [METHOD](METHOD.md) → [U03](research/U03-CORE-TERMS-BATCH1.md) → [CORE-TERMS-WORKING-v0.1](synthesis/CORE-TERMS-WORKING-v0.1.md).

U01/U02, Agent'ın ayrıntılı kaynak geçmişi gerektiğinde geri açılır; her oturumda tamamını tekrar okumak zorunlu değildir.

Yeni oturum tek tek bu 10 terim için kullanıcı onayı istemez. Batch'i working reference olarak kullanır; gerçek kullanımda çakışma, ambiguity veya yeni kaynak baskısı çıkarsa ilgili terim(ler) birlikte fine-tune edilir.

## Sonraki batch için keşif adayları

U03 doğal olarak şu güçlü komşuları açtı:

- Runtime
- Context
- Memory
- Identity
- Capability
- Authority
- Permission
- Orchestration
- Handoff
- Subagent

Bu liste sonraki 10 terim için olası seed'dir; zorunlu sıra değildir. Sonraki turda en çok çakışma/boşluk temizleyecek bağlantılardan batch seçilebilir.

## Yayın durumu

Bu tur için çalışma branch'i `research/concepts-core-terms-batch1-20260918`.

Yeni U03 araştırması ve working reference v0.1 oluşturuldu; research/synthesis/reference routing, Agent BRIEF, envanter ve bu STATE yeni batch'e bağlandı. Main yayını ve geri doğrulama tamamlanmadan branch canonical yayın sayılmaz.

## Korunan geçmiş

- v0.2 yöntem uyarlaması PR #20 ile main'e yayımlandı.
- Agent U01/U02 ve ilk Agent boundary adayı PR #19/#21 geçmişinde korunur.
- [AGENT-BOUNDARY-CANDIDATE-v0.1](synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md) artık active candidate değil, U03 batch'ine giden tarihsel ara sentezdir.
- P0 ve yöntem doğrulama kayıtları kendi checks dosyalarında korunur.
