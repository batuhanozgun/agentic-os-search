# Concepts — Güncel Durum

**Kayıt tarihi:** 2026-09-18.  
**Mevcut iş:** İkinci 10-terim batch'i tamamlandı; toplam 20 terim için working local reference v0.2 hazırlandı. Bu turun dönüş noktası sonucu kullanıcıya sunmaktır.  
**Yöntem:** [METHOD v0.2](METHOD.md) — bağlantılı batch + ilişki haritası + çakışma üzerinden fine-tune.  
**Mevcut araştırma:** [U03 batch 1](research/U03-CORE-TERMS-BATCH1.md) + [U04 batch 2](research/U04-CORE-TERMS-BATCH2.md); Agent U01/U02 gerektiğinde ayrıntılı kaynak geçmişidir.  
**Aktif working reference:** [CORE-TERMS-WORKING-v0.2](synthesis/CORE-TERMS-WORKING-v0.2.md).  
**ACCEPTED reference:** Henüz yok; tek tek terim onayı beklenmez.

## Working reference kapsamı — 20 terim

### Batch 1
Agent; Model; LLM; Actor; Role; Run; Session; Workflow; Tool; Harness.

### Batch 2
Runtime; Context; Memory; Identity; Capability; Authority; Permission; Orchestration; Handoff; Subagent.

## v0.2'nin en önemli yeni sınırları

- **Harness ≠ Runtime** — Harness geniş operating/control substrate; Runtime execution machinery.
- **Context ≠ Session ≠ Memory** — current visible working set / continuity container / cross-time retained knowledge-state.
- **Capability ≠ Authority ≠ Permission** — yapabilme / meşru-yetkili scope / spesifik action-resource izni.
- **Workflow ≠ Orchestration ≠ Runtime** — yapı / execution-time coordination / fiili execution machinery.
- **Agent ≠ Actor ≠ Role ≠ Identity** — AI execution unit / Work participant / expected function / distinguishing continuity-reference.
- **Subagent is-a Agent** ama ilişkisel statüdür.
- **Handoff ≠ Subagent** — biri control/responsibility transfer, diğeri Agent'ın decomposition içindeki ilişkisel konumu.

## Güncel birlikte kullanım haritası

```text
Model
└── LLM

Harness
├── contains/configures → Runtime
│   ├── executes → Agent / Workflow
│   ├── creates/manages → Run
│   ├── dispatches → Tool
│   ├── performs → Handoff
│   └── applies → Permission controls
├── manages → Context / Memory plumbing
├── may enforce → Authority / Permission
└── provides → Orchestration / Verification / Observability surfaces

Agent
├── uses → Model / LLM
├── may-call → Tool
├── executes-as → Run
├── may-be → Actor
└── may delegate-to → Subagent

Subagent
└── is-a → Agent

Actor
├── assumes → Role
├── identified-by → Identity
├── has → Capability
└── exercises-within → Authority
    └── maps-to → Permissions

Workflow
└── executed/coordinated-by → Orchestration
    ├── coordinates → Agents / Subagents / Actors / Tools
    └── may use → Handoff

Session
└── preserves continuity across → Runs

Memory
└── may feed → Context

Context
← assembled from — current input / Session / Memory / Tool results
```

## Yeni oturumda devam yolu

Güncel AGENT ve gereken protokoller → [INDEX](INDEX.md) → bu STATE → [METHOD](METHOD.md) → [working v0.2](synthesis/CORE-TERMS-WORKING-v0.2.md). Ayrıntılı kanıt gerekirse [U04](research/U04-CORE-TERMS-BATCH2.md) → [U03](research/U03-CORE-TERMS-BATCH1.md) → Agent U01/U02.

Yeni oturum bu 20 terimi tek tek kullanıcıya sormaz. v0.2'yi working map olarak kullanır ve yalnız yeni batch/gerçek kullanım çakışması olduğunda ilgili sınırları yeniden açar.

## Sonraki batch için doğal adaylar

- State
- Work state
- Environment
- Workspace
- Sandbox
- Policy
- Guardrail
- Verification
- Observability
- Persistence

Bunlar zorunlu sıra değildir; v0.2 haritasında en fazla ayrım temizleyecek kombinasyon seçilir.

## Yayın durumu

**Yayın:** [PR #24](https://github.com/batuhanozgun/agentic-os-search/pull/24); branch `research/concepts-core-terms-batch2-20260918`; exact head `7e452b0c9d8f81f1069fbe4bbaf8938f6e7346ab`; main merge commit `6198fa8195bbf56a83568b093f9bf23df2878140`.

Sekiz concepts yolu değişti: yeni U04 ve working v0.2; v0.1 historical snapshot işareti; research/synthesis/reference index, envanter ve bu STATE. Agent-control, Foundation, studies paketleri ve explorations değişmedi.

PR merge öncesi `mergeable=true` idi. Exact head'e bağlı normal merge başarılı oldu; head → merge karşılaştırması sıfır dosya farkı verdi. Working v0.2 ve U04 main üzerinden yayımlandı.

Bu yayın tanımların evrensel doğruluğunu veya ileride hiç değişmeyeceğini kanıtlamaz. v0.2 evolving working reference olarak kullanılacak ve sonraki batch/gerçek kullanım çakışmalarıyla fine-tune edilecektir. ACCEPTED reference hâlâ yoktur.

## Korunan geçmiş

- v0.1 ilk 10 terimin tarihsel snapshot'ı olarak korunur.
- Agent boundary adayı daha eski ara sentezdir.
- v0.2 yöntem, P0 ve yayın doğrulama geçmişleri checks/STATE kayıtlarında korunur.
