# Hermes Agent — INDEX

Current work [STATE](STATE.md), yöntem [METHOD](METHOD.md), sıra [plan v0.22](RESEARCH-PLAN.md), sınıflandırma [META](META.md), derived [MAP](CURRENT-RESEARCH-MAP.md). **U09 source-only; U08 yayını tamamlandı.** Genel HERMES araştırması partial'dır.

| İhtiyaç | Okuma yolu |
|---|---|
| İş kimliği, planlanan occurrence ve geç tetikleme | **[24/U09](notes/24-CRON-OCCURRENCE-AND-FIRE-ADMISSION.md)** → [RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md) → [SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md) |
| Belge–kod farkı / gerçekten yapılmamış deney | U09 RESEARCH §5–8 → [NOT RUN](evidence/2026-09-12-cron-occurrence-admission/CHECKS-NOT-RUN.md); source trace ≠ execution |
| Gerçek yayın ve sonraki iş | [U09 PUBLICATION](evidence/2026-09-12-cron-occurrence-admission/PUBLICATION.md), [U08 PUBLICATION](evidence/2026-09-12-cron-drain-receipts/PUBLICATION.md), STATE/PLAN; ilk yeni source Q49 |
| Gerçek cron göndericisi, CLI durumu ve iptal | [23/U08](notes/23-CRON-DRAIN-RECEIPTS-AND-CANCELLATION.md) → [U08 RESEARCH/SOURCES](evidence/2026-09-12-cron-drain-receipts/README.md) → [coverage](inventory/DELIVERY-RECEIPT-COVERAGE-2026-09-12.md) |
| Job/trigger/attempt/teslim ayrımı | [22/U07](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md) → [U07 RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md)/[SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md) → [coverage](inventory/CRON-COVERAGE-2026-09-11.md) |
| Devamda history/hak/driver | [21/U06](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md) → [U06 RESEARCH/SOURCES](evidence/2026-09-11-resume-admission/README.md) → [coverage](inventory/RESUME-ADMISSION-COVERAGE-2026-09-11.md) |
| DB lease, quiet history, rotation | [20/U05](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md) → [U05 RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md)/[SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[NOT RUN](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md) |
| Kalıcı iş/devamın üst açıklaması | [synthesis03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md) → [18/U04-A](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → notes20–24 amendments |
| Genel turn/context/session | [synthesis02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) → [16/U02](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md) |
| Öğrenme/değişim | [synthesis01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) → notes02–15; normal compaction için U02 karşı okuması |
| Task/run/claim/terminal kabul | [17/U03](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md) → [U03 RESEARCH](evidence/2026-09-10-kanban-task/RESEARCH.md)/[SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md) |
| U04-A/B ayrı yayın ve kanıt kimlikleri | **[19](notes/19-U04-DELIVERY-RECONCILIATION.md)** → [B README](evidence/2026-09-11-multiturn/README.md)/[RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json) |

## Exact eski deneylere erişim

U08 B: [SPEC](evidence/2026-09-12-cron-drain-receipts/SPEC.md) / [RESULT](evidence/2026-09-12-cron-drain-receipts/RESULT.json) / [MANIFEST](evidence/2026-09-12-cron-drain-receipts/MANIFEST.json) → raw archive source/probe/effect. U07 D: [SPEC](evidence/2026-09-11-cron-scheduling-delivery/SPEC.md) / [RESULT](evidence/2026-09-11-cron-scheduling-delivery/RESULT.json) / [MANIFEST](evidence/2026-09-11-cron-scheduling-delivery/MANIFEST.json). U06 L: [SPEC](evidence/2026-09-11-resume-admission/SPEC.md) / [RESULT](evidence/2026-09-11-resume-admission/RESULT.json) / [MANIFEST](evidence/2026-09-11-resume-admission/MANIFEST.json).

U04-A: [SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md)/[RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md)/[SPEC](evidence/2026-09-11-multi-turn-continuity/SPEC.md) → diagnostic-evidence.tar.xz. U04-B: [SOURCES](evidence/2026-09-11-multiturn/delivery/SOURCES.md)/[SPEC](evidence/2026-09-11-multiturn/delivery/evidence/SPEC.md)/[RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json)/[probe](evidence/2026-09-11-multiturn/delivery/evidence/probe.py). Aynı G/H ID'si eş vaka değildir.

## Önceki tam router ve kapsam

[Exact v0.21 INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/c370cbc88823f7ee4d07aa6c97b75cf509129254/research/studies/hermes-agent/INDEX.md), eski notes02–15 ve evidence yollarının ayrıntılı tablosunu korur. Hiçbiri taşınmadı/silinmedi. [SOURCE-LEDGER](SOURCE-LEDGER.md), [OPEN-QUESTIONS](OPEN-QUESTIONS.md), [WHY](00-WHY-THIS-RESEARCH.md), [ilk STRUCTURE](inventory/STRUCTURE.md), [F01–F12](inventory/CORE-COVERAGE-2026-09-10.md) ve STATE cold-start yolu current retrieval'ın parçalarıdır.

Eski unpublished/first-next cümleleri tarihsel birimlere aittir. U08 yayını artık tamamdır; U09'dan sonra ilk yeni source Q49'dur. Q47 gerçek-runtime, Q40/Q42 ve Q48/Q50 doğrulama borçları açık. U09 kaynak incelemesi için RESULT/koşu arşivi yoktur. Üç sentez provisional; final CORE/dört-alan/adoption yoktur.
