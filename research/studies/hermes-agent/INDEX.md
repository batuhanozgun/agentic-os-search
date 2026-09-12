# Hermes Agent — INDEX

**Current U12 / plan v0.25.** Work/yetki [STATE](STATE.md), sınıflandırma/reuse [META](META.md), yöntem [METHOD](METHOD.md), sıra [PLAN](RESEARCH-PLAN.md), büyük resim [MAP](CURRENT-RESEARCH-MAP.md). ACTIVE PARTIAL; dört provisional sentez, final CORE değil. [U12 yayın makbuzu](evidence/2026-09-13-tool-delegation/PUBLICATION.md).

## Güncel soru ve kanıt rotaları

| İhtiyaç | Yol |
|---|---|
| Araç teklifi gerçek handler'a hangi kapılarla ulaşır? | **[27/U12](notes/27-TOOL-ADMISSION-AND-DELEGATION.md)** → [A araç kabulü](evidence/2026-09-13-tool-delegation/TOOL-ADMISSION.md) → [A kaynakları S01–S07](evidence/2026-09-13-tool-delegation/TOOL-SOURCES.md) |
| Alt ajan hangi bağlam/yetkiyle çalışır, sonucu kime döner? | [B delegation lifecycle](evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md) → [B kaynakları S08–S15](evidence/2026-09-13-tool-delegation/DELEGATION-SOURCES.md) |
| U12'de gerçekte hangi doğrulamalar yapılmadı? | [NOT RUN](evidence/2026-09-13-tool-delegation/CHECKS-NOT-RUN.md). Yeni execution/RESULT yok; source/readback ile behavioral validation ayrı |
| Completion kuyruğundan parent turuna kalan iş | [PLAN Q57](RESEARCH-PLAN.md) → U12-B §10–11 ve S15 delivery helper'ları → actual host consumers; henüz yapılmış sayılmaz |
| Runtime seçimi gerçek yürütme sahibine nasıl dönüşür? | [26/U11](notes/26-RUNTIME-BACKEND-AND-CONTROL-OWNERSHIP.md) → [A seçim/dispatch](evidence/2026-09-12-runtime-backend/RESEARCH.md) + [B sahiplik](evidence/2026-09-12-runtime-backend/BACKEND-OWNERSHIP.md) |
| U11 ne kadar okundu/çalıştırıldı? | [A kaynakları](evidence/2026-09-12-runtime-backend/SOURCES.md), [B kaynakları](evidence/2026-09-12-runtime-backend/BACKEND-SOURCES.md), [NOT RUN](evidence/2026-09-12-runtime-backend/CHECKS-NOT-RUN.md); source-only |
| Scheduled snapshot nasıl gerçek işe/bağlama dönüşür? | [25/U10](notes/25-CRON-EXECUTION-AND-CONTEXT.md) → [RESEARCH](evidence/2026-09-12-cron-execution-context/RESEARCH.md) → [SOURCES](evidence/2026-09-12-cron-execution-context/SOURCES.md) |
| Selector koşusu neyi gerçekten ölçtü? | [SPEC](evidence/2026-09-12-cron-execution-context/SPEC.md) → [tam RESULT](evidence/2026-09-12-cron-execution-context/RESULT.json) → [MANIFEST/raw](evidence/2026-09-12-cron-execution-context/MANIFEST.json) → [README](evidence/2026-09-12-cron-execution-context/README.md); C yalnız local-file selector |
| Scheduled-work büyük açıklaması | [synthesis04](synthesis/04-SCHEDULED-WORK-AND-CONTEXT-PROVISIONAL.md) → notes22–25; backend için26, araç/delegation için27 birlikte okunur |
| Cwd, monitor, first request ne kadar doğrulandı? | [U10 coverage](inventory/EXECUTION-CONTEXT-COVERAGE-2026-09-12.md) / [NOT RUN](evidence/2026-09-12-cron-execution-context/CHECKS-NOT-RUN.md) |
| Planlanmış occurrence / HTTP kabul | [24/U09](notes/24-CRON-OCCURRENCE-AND-FIRE-ADMISSION.md) → [RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md)/[SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md)/[NOT RUN](evidence/2026-09-12-cron-occurrence-admission/CHECKS-NOT-RUN.md); source-only |
| Drainer / status / cancellation | [23/U08](notes/23-CRON-DRAIN-RECEIPTS-AND-CANCELLATION.md) → [RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md)/[SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md); exact B için SPEC/RESULT/MANIFEST |
| Cron job/trigger/attempt/queue | [22/U07](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md) → [RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md)/[SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md); exact D için SPEC/RESULT/MANIFEST |
| Devamın history/hak/driver kabulü | [21/U06](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md) → [RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md)/[SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md); exact L için SPEC/RESULT/MANIFEST |
| Durable lease/quiet-history/rotation | [20/U05](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md) → [RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md)/[SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md) |
| U04-A ve B aynı mı? | [19](notes/19-U04-DELIVERY-RECONCILIATION.md) → [B README](evidence/2026-09-11-multiturn/README.md)/[RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json) |
| Kalıcı iş/çok-turlu devam | [synthesis03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md) → [18/U04-A](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) +20/21 amendments; cron/delegation ile eşitlenmez |
| Genel turn/context/session | [synthesis02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) → [16](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md); U11/U12 varyantları ayrı |
| Öğrenme/değişim | [synthesis01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) → notes02–15 |
| Task/run/claim/acceptance | [17](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md) → [U03 kaynakları](evidence/2026-09-10-kanban-task/SOURCES.md) |
| Bütün sorular / kaynak defteri | [OPEN-QUESTIONS](OPEN-QUESTIONS.md), [SOURCE-LEDGER](SOURCE-LEDGER.md) |

## Önceki erişim ve cold-start

[Exact U11 index](https://github.com/batuhanozgun/agentic-os-search/blob/6a9a8c48204102d592780971a212b363ec97bc98/research/studies/hermes-agent/INDEX.md) → U10/U09 ve eski router zinciri. Eski not/evidence taşınmadı. STATE mandatory cold-start uygulanır. Exact A/B/L/D/B/C iddiası kendi SPEC/tam RESULT/raw source-probe'una döner; aynı numara eş vaka değildir. U11/U12 A/B kaynak karşılaştırmaları runtime deneyi değildir.

[U08](evidence/2026-09-12-cron-drain-receipts/PUBLICATION.md), [U09](evidence/2026-09-12-cron-occurrence-admission/PUBLICATION.md), [U10](evidence/2026-09-12-cron-execution-context/PUBLICATION.md) ve [U11](evidence/2026-09-12-runtime-backend/PUBLICATION.md) tamamlanmış yayın makbuzlarıdır. Tarihsel prepared/capability açıklamaları current engel sayılmaz. U12 başlangıç/A/B sırası kendi PUBLICATION dosyasındadır.

Q54 kaynakla ilerledi; **ilk sonraki dar source Q57 actual completion/parent re-entry**. Q54 residual, Q55/Q56, U10 Q49/Q51/Q52, Q40/Q42/Q47/Q48/Q50 ve bütün eski validation borçları korunur. MAP/catalog/synthesis ham kanıtın yerine geçmez; dört provisional synthesis dört-alan/adoption değildir.
