# Concepts — Güncel Durum

**Kayıt tarihi:** 2026-09-18.  
**Mevcut iş:** Üçüncü 10-terim batch'i tamamlandı; toplam 30 terim için working local reference v0.3 hazırlandı. Bu turun dönüş noktası sonucu kullanıcıya sunmaktır.  
**Yöntem:** [METHOD v0.2](METHOD.md) — bağlantılı batch + ilişki haritası + çakışma üzerinden fine-tune.  
**Mevcut araştırma:** [U03 batch 1](research/U03-CORE-TERMS-BATCH1.md) + [U04 batch 2](research/U04-CORE-TERMS-BATCH2.md) + [U05 batch 3](research/U05-CORE-TERMS-BATCH3.md).  
**Aktif working reference:** [CORE-TERMS-WORKING-v0.3](synthesis/CORE-TERMS-WORKING-v0.3.md).  
**ACCEPTED reference:** Henüz yok; tek tek terim onayı beklenmez.

## Working reference kapsamı — 30 terim

### Batch 1
Agent; Model; LLM; Actor; Role; Run; Session; Workflow; Tool; Harness.

### Batch 2
Runtime; Context; Memory; Identity; Capability; Authority; Permission; Orchestration; Handoff; Subagent.

### Batch 3
State; Work state; Environment; Workspace; Sandbox; Policy; Guardrail; Verification; Observability; Persistence.

## v0.3'ün en önemli yeni sınırları

- **State ≠ status ≠ Memory** — State current condition representation; status yalnız bir alan olabilir; Memory cross-time knowledge/state lifecycle.
- **Work state ≠ Session history ≠ RunState** — Work continuation/control truth'u, conversation continuity veya tek execution snapshot'ına indirgenmez.
- **Environment ≠ Workspace ≠ Sandbox** — geniş çalışma koşulları/kaynakları / Work materyal alanı / controlled execution boundary.
- **Policy ≠ Guardrail ≠ Sandbox** — rule/expectation / execution-time semantic check-control / capability-resource containment.
- **Verification ≠ Observability** — doğruluk/uygunluk değerlendirmesi / ne olduğunu görünür kılma.
- **Persistence ≠ Memory ≠ Session** — boundary ötesinde saklanabilme / retained knowledge-state / continuity container.

## Güncel birlikte kullanım haritası

```text
                         ┌────────── Policy ──────────┐
                         │                            │
                         ▼                            ▼
Authority ───────► Permissions                 Guardrails
    ▲                    │                          │
    │                    ▼                          ▼
Actor ─assumes→ Role   Runtime ◄────────────── Sandbox
  │                     │  ▲                      ▲
  │                     │  │                      │
  │                     │  └── operates in ── Environment
  │                     │
  │                     ├── executes → Agent / Workflow
  │                     ├── creates/manages → Run
  │                     ├── dispatches → Tool
  │                     └── performs → Handoff
  │
  ├── identified-by → Identity
  └── has → Capability
                  ▲
                  └── depends on → Model / Tool / Runtime / Environment

Model
└── LLM

Agent
├── uses → Model
├── may-call → Tool
├── may-be → Actor
└── may delegate-to → Subagent
                         └── is-a → Agent

Workflow
└── coordinated-by → Orchestration
      └── coordinates → Agents / Actors / Tools / Handoffs

State
├── specialization → Work state
├── may persist via → Persistence
└── selected portion may enter → Context

Session ─preserves→ continuity across Runs
Memory ─may feed→ Context
Work state ─persists across→ Runs / Sessions / Actors

Environment
├── contains/supports → Workspace
└── may contain → Sandbox

Workspace ─holds→ artefacts / outputs / persisted Work state

Observability ─provides evidence/events→ Verification
Verification ─qualifies→ claims / completion / effects

Harness
└── configures/connects → Runtime / Context / Memory / Policy controls /
                         Sandbox / Orchestration / Verification /
                         Observability / Persistence surfaces
```

## Yeni oturumda devam yolu

Güncel AGENT ve gereken protokoller → [INDEX](INDEX.md) → bu STATE → [METHOD](METHOD.md) → [working v0.3](synthesis/CORE-TERMS-WORKING-v0.3.md). Ayrıntılı kanıt gerekirse [U05](research/U05-CORE-TERMS-BATCH3.md) → U04 → U03 → Agent U01/U02.

Yeni oturum bu 30 terimi tek tek kullanıcıya sormaz. v0.3'ü working map olarak kullanır ve yalnız yeni batch/gerçek kullanım çakışması olduğunda ilgili sınırları yeniden açar.

## Sonraki batch için doğal adaylar

- Goal
- Intent
- Plan
- Task / Work item
- Dependency
- Readiness
- Completion
- Validation
- Evaluation
- Evidence

Bunlar zorunlu sıra değildir; v0.3 haritasında en fazla ayrım temizleyecek kombinasyon seçilir.

## Yayın durumu

Bu tur için çalışma branch'i `research/concepts-core-terms-batch3-20260918`.

U05 ve working v0.3 oluşturuldu; research/synthesis/reference routing, envanter ve STATE v0.3'e bağlanıyor. Main yayını ve geri doğrulama tamamlanmadan branch canonical yayın sayılmaz.

## Korunan geçmiş

- v0.1 ve v0.2 tarihsel snapshots olarak korunur.
- Agent boundary adayı daha eski ara sentezdir.
- v0.2 yöntem, P0 ve yayın doğrulama geçmişleri checks/STATE kayıtlarında korunur.
