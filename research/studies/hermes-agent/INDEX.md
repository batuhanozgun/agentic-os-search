# Hermes Agent — INDEX

Current Work/completion authority [STATE](STATE.md); classification/reuse [META](META.md); method [METHOD](METHOD.md); current plan [v0.17](RESEARCH-PLAN.md). Bu router bağımsız çalışma yetkisi değildir. V0.17 ayrı U04 teslimini uzlaştırır, yeni araştırma/deney değildir.

## Güncel açıklama ve kanıt yolları

| Soru | İlk okuma |
|---|---|
| Kalıcı iş, devam kararı ve yeni tur nasıl birleşir? | [synthesis/03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md) → [18/U04-A](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) |
| Bekleyen 21-durumlu teslim nerede, diğer U04 ile farkı ne? | **[19/U04-B](notes/19-U04-DELIVERY-RECONCILIATION.md)** → [README](evidence/2026-09-11-multiturn/README.md) → [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) |
| A'nın 15 grubu ve tam ham girdileri? | [A SPEC](evidence/2026-09-11-multi-turn-continuity/SPEC.md), [A SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [A raw archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz); [summary](evidence/2026-09-11-multi-turn-continuity/RESULT-SUMMARY.json) yalnız gezinme |
| B'nin 21 durumu ve tam ham girdileri? | [B SPEC](evidence/2026-09-11-multiturn/delivery/evidence/SPEC.md), [B RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json), [B probe](evidence/2026-09-11-multiturn/delivery/evidence/probe.py), [33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json) |
| Bir normal girdi bağlam, yürütme, kayıt ve teslime nasıl dönüşür? | [synthesis/02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) → [16/U02](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md) |
| Kalıcı task/run/claim ve terminal kabul? | [17/U03](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md) → [RESEARCH](evidence/2026-09-10-kanban-task/RESEARCH.md), [SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md) |
| Öğrenme/değişim bu çekirdekte nasıl yer alır? | [synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md); normal compaction karşı okuması için 02/U02 |
| Sonraki iş ne? | [STATE](STATE.md) ve [PLAN](RESEARCH-PLAN.md): actual turn facade lease/history/SessionDB, ardından gerekli rotation/restart driver bağı |
| Bütün sistem tamamlandı mı? | Hayır; [CONTINUITY-COVERAGE](inventory/CONTINUITY-COVERAGE-2026-09-11.md), [CORE-COVERAGE](inventory/CORE-COVERAGE-2026-09-10.md), [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

## Mekanizma ve tarihsel kayıtlar

| Alan | Giriş |
|---|---|
| Neden/yöntem/topoloji | [00-WHY](00-WHY-THIS-RESEARCH.md), [METHOD](METHOD.md), [STRUCTURE](inventory/STRUCTURE.md), [01](notes/01-ORIENTATION.md) |
| Review snapshot/fork/ownership | [02](notes/02-BACKGROUND-LEARNING.md) |
| Curator/maintenance/report/cron | [03](notes/03-SKILL-CURATION.md) |
| Skill transaction/approval | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [U01B](evidence/2026-09-07-u01b/component-probe/README.md) |
| Eski mutable doküman kontratları | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md), [W](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| Caller/worker/context transfer | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [D](evidence/2026-09-08-context-transfer/SOURCES.md) |
| MemoryStore/pending replay | [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) |
| Roundtrip/diff/rollback | [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [U01B2](evidence/2026-09-08-u01b2/README.md) |
| Selected worker policy/validator | [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [E/C/V](evidence/2026-09-08-worker-policy/README.md) |
| Review/middleware/manual AST | [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md), [J/MW](evidence/2026-09-09-review-middleware/README.md) |
| Memory/pending state | [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md), [M2/N](evidence/2026-09-09-memory-pending/README.md) |
| Eski UI/A caller/profile | [12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md), [UI/A](evidence/2026-09-10-ui-profile/SOURCES.md) |
| SA ayrı pending teslimi | [13](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md), [M3-S/SA](evidence/2026-09-10-pending-caller/SOURCES.md) |
| AP ayrı altı-durumlu teslim | [14](notes/14-AP-DELIVERY-RECONCILIATION.md), [AP](evidence/2026-09-10-ui-profile-approval/README.md) |
| M4 fresh store/stored prompt | [15](notes/15-MEMORY-PROMPT-RESTORE-BOUNDARIES.md), [M4 RESULT](evidence/2026-09-10-prompt-restore/RESULT.json); actual compaction sırası 16/C13 |
| Genel turn/context/session | [16](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md), [U02 RESEARCH](evidence/2026-09-10-turn-lifecycle/RESEARCH.md) |
| Kanban task/run/claim/acceptance | [17](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md), [U03 archive](evidence/2026-09-10-kanban-task/original-evidence.tar.xz), [recovery](evidence/2026-09-10-kanban-task/PUBLICATION.md) |
| U04-A çok turlu kaynak/model | [18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md), [A RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md) |
| U04-B ayrı teslim yayını | [19](notes/19-U04-DELIVERY-RECONCILIATION.md), [B RESEARCH](evidence/2026-09-11-multiturn/delivery/RESEARCH.md), [B SOURCES](evidence/2026-09-11-multiturn/delivery/SOURCES.md) |
| Kapsam/kanıt rotası | [SCOPE-REVIEW](inventory/SCOPE-REVIEW-2026-09-10.md), [SOURCE-LEDGER](SOURCE-LEDGER.md), [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

## Yeni oturum için ayrımlar

U04-A/B etiketleri yalnız iki U04 paketini ayırır; eski UI/A ile karıştırılmaz. B'nin `delivery/repo-updates/` içindeki v0.16, note18, synthesis03 ve Q40–Q45 önerileri historical candidate dosyalardır. Onlar current root dosyalarının yerine uygulanmadı; current soru eşlemesi RECONCILIATION'dadır. Özgün metinlerin “yayımlanmadı” cümlesi tek başına güncel yayın engeli değildir.

Kayıtlar hash/byte düzeyinde korunur; bu yeni davranış deneyi veya independent replication değildir. Tam heartbeat kimliği, seçili Kanban'ın parent sadakatini veya full SessionDB/OS/driver/model doğruluğunu sağlamaz. A:S10 history substitution korunur, actual lower lease açık. Q07/Q22 normal compaction→API-message source bağı, M4 artificial V04 sırasının gerçek compression bug'ı olmadığı sınırı ve Q26/Q29 full-worker/original borcu sürer. Üç merkezi sentez provisional; nihai CORE/dört-alan/adoption yoktur.
