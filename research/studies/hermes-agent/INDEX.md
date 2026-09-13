# Hermes Agent — INDEX

**Current U14 / plan v0.27.** [STATE](STATE.md) work/yetki, [META](META.md) study/reuse, [METHOD](METHOD.md) yöntem, [PLAN](RESEARCH-PLAN.md) sıra, [MAP](CURRENT-RESEARCH-MAP.md) derived büyük resim. ACTIVE PARTIAL, dört provisional synthesis; final CORE değil. [U14 PUBLICATION](evidence/2026-09-13-install-update/PUBLICATION.md).

## Güncel girişler

| İhtiyaç | Kaynak yolu |
|---|---|
| Kaynak nasıl kurulu komut/profil/çalışan sistem olur? | **[29/U14](notes/29-INSTALLATION-UPDATE-AND-ACTIVATION.md)**→[A INSTALL-AND-ACTIVATION](evidence/2026-09-13-install-update/INSTALL-AND-ACTIVATION.md)/[INSTALL-SOURCES S01–S06](evidence/2026-09-13-install-update/INSTALL-SOURCES.md) |
| Update neyi değiştirir, neyi reddeder, neyi yeniden başlatır? | [B UPDATE-AND-RECOVERY](evidence/2026-09-13-install-update/UPDATE-AND-RECOVERY.md)/[UPDATE-SOURCES S07–S14](evidence/2026-09-13-install-update/UPDATE-SOURCES.md) |
| U14'te ne gerçekten çalıştırılmadı? | [NOT RUN](evidence/2026-09-13-install-update/CHECKS-NOT-RUN.md): installer/updater/solver/DB/service/OS/model koşusu yok; lock/partial/receipt source inference |
| Q58 sonrası neden Q59? | [PLAN kapsam değerlendirmesi](RESEARCH-PLAN.md)→U14-B §11–12 ve [U13 coverage](inventory/SCOPE-REVIEW-2026-09-13-U13.md): actual skills-sync çağıranlarından library lifecycle; Q59 henüz yapılmadı |
| Child sonucu gerçek parent turuna nasıl girer? | [28/U13](notes/28-DELEGATION-COMPLETION-AND-PARENT-REENTRY.md)→[A RESEARCH](evidence/2026-09-13-delegation-reentry/RESEARCH.md)/[SOURCES](evidence/2026-09-13-delegation-reentry/SOURCES.md) |
| No-exception False ile ack ilişkisi ne kadar sınandı? | [B DIAGNOSTIC](evidence/2026-09-13-delegation-reentry/DIAGNOSTIC.md)→[SPEC](evidence/2026-09-13-delegation-reentry/SPEC.md)→[MANIFEST](evidence/2026-09-13-delegation-reentry/MANIFEST.json)→[raw archive](evidence/2026-09-13-delegation-reentry/diagnostic-evidence.tar.xz); exact D/N için source/input/probe/full RESULT/log. [Özet](evidence/2026-09-13-delegation-reentry/RESULT-SUMMARY.json) derived |
| U13 neyi doğrulamadı? | [NOT RUN](evidence/2026-09-13-delegation-reentry/CHECKS-NOT-RUN.md): full-parent fidelity/model/DB/gateway/OS yok; bu tur yeniden koşulmadı |
| Araç kabulü ve yeni child | [27/U12](notes/27-TOOL-ADMISSION-AND-DELEGATION.md)→[tool A](evidence/2026-09-13-tool-delegation/TOOL-ADMISSION.md)/[A SOURCES](evidence/2026-09-13-tool-delegation/TOOL-SOURCES.md)→[delegation B](evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md)/[B SOURCES](evidence/2026-09-13-tool-delegation/DELEGATION-SOURCES.md)/[NOT RUN](evidence/2026-09-13-tool-delegation/CHECKS-NOT-RUN.md) |
| Runtime seçimi ve gerçek control sahibi | [26/U11](notes/26-RUNTIME-BACKEND-AND-CONTROL-OWNERSHIP.md)→[A](evidence/2026-09-12-runtime-backend/RESEARCH.md)/[SOURCES](evidence/2026-09-12-runtime-backend/SOURCES.md)→[B](evidence/2026-09-12-runtime-backend/BACKEND-OWNERSHIP.md)/[B SOURCES](evidence/2026-09-12-runtime-backend/BACKEND-SOURCES.md)/[NOT RUN](evidence/2026-09-12-runtime-backend/CHECKS-NOT-RUN.md) |
| Cron snapshot gerçek iş/bağlama nasıl dönüşür? | [25/U10](notes/25-CRON-EXECUTION-AND-CONTEXT.md)→[RESEARCH](evidence/2026-09-12-cron-execution-context/RESEARCH.md)/[SOURCES](evidence/2026-09-12-cron-execution-context/SOURCES.md)/[NOT RUN](evidence/2026-09-12-cron-execution-context/CHECKS-NOT-RUN.md); exact C için [SPEC](evidence/2026-09-12-cron-execution-context/SPEC.md)/[full RESULT](evidence/2026-09-12-cron-execution-context/RESULT.json)/[MANIFEST](evidence/2026-09-12-cron-execution-context/MANIFEST.json) |
| Planlanmış occurrence ve fire kabul | [24/U09](notes/24-CRON-OCCURRENCE-AND-FIRE-ADMISSION.md)→[kanıt](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md)/[SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md) |
| Gerçek drainer/status/cancel | [23/U08](notes/23-CRON-DRAIN-RECEIPTS-AND-CANCELLATION.md)→[RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md)/[SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md); exact eski B için SPEC/RESULT/MANIFEST |
| Job/trigger/attempt/queue | [22/U07](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md)→[RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md)/[SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md); exact eski D için SPEC/RESULT/MANIFEST |
| Resume/lease/history/restart | [21/U06](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md)→[RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md)/[SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md); [20/U05](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md)→[RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md)/[SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md) |
| U04-A ve B ayrımı | [19](notes/19-U04-DELIVERY-RECONCILIATION.md)→[B README](evidence/2026-09-11-multiturn/README.md)/[RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json); [A RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md)/[A SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md)/[CONTINUITY COVERAGE](inventory/CONTINUITY-COVERAGE-2026-09-11.md) |
| Task/run/claim/terminal | [17/U03](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md)→[Kanban sources](evidence/2026-09-10-kanban-task/SOURCES.md) |
| Bütün açık disposition ve raw kanıt rotaları | [OPEN-QUESTIONS](OPEN-QUESTIONS.md)/[SOURCE-LEDGER](SOURCE-LEDGER.md) |

## Korunan dört provisional sentez

[01 öğrenme/değişim](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md)→notes02–15; [02 normal turn/context/session](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md)→note16/U02; [03 persistent work/continuation](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md)→notes17–21; [04 scheduled work/context](synthesis/04-SCHEDULED-WORK-AND-CONTEXT-PROVISIONAL.md)→notes22–25. U11–14 notes26–29 ile birlikte okunur; yeni source amendment eski runtime borcunu kapatmaz. Q59 için synthesis01 eski öğrenme/approval kapsamını yeniden kullan; yeniden deney sayma.

## Retrieval ve yayın sınırı

STATE mandatory cold-start uygulanır. [Exact U13 INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/93d6b14438802163ed3f542beded218e14cc51cf/research/studies/hermes-agent/INDEX.md)→U12 eski source/coverage/yayın rotalarını korur. Not/evidence taşınmadı. U04-A/B ve eski D/B ile U13 D/N eş numaraları aynı deney değildir.

U08–U13 tamamlanmış yayınlar bekleyen ZIP değildir. U13 final receipt current main'den uzlaştırıldı. U14 opening/A/B ve final routes kendi PUBLICATION'ında. Q58 source-advanced; **Q59 library lifecycle ilk next**, henüz araştırılmadı. Q54–58 ve eski runtime/fidelity/quality residual'ları korunur. Catalog/MAP/synthesis raw kanıt yerine geçmez; final CORE/dört-alan/adoption yoktur.
