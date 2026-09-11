# Hermes Agent — INDEX

Current work/completion [STATE](STATE.md), classification/reuse [META](META.md), method [METHOD](METHOD.md), plan [v0.20](RESEARCH-PLAN.md). U07 yayın checkpoint'i; güncel ref/content makbuzu PUBLICATION'dadır. Whole-system completion değildir. Eski yayınlar tamamlanmış iş olarak korunur.

## Güncel ilerleme ve evidence route

| İhtiyaç | Okuma yolu |
|---|---|
| Cron job/trigger/deneme/teslim nasıl ayrılıyor? | **[22/U07](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md)** → [RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md) → [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md) |
| U07'nin gerçek yeni koşusu ve açık kapsamı? | [SPEC](evidence/2026-09-11-cron-scheduling-delivery/SPEC.md) → [RESULT](evidence/2026-09-11-cron-scheduling-delivery/RESULT.json) → [MANIFEST/raw](evidence/2026-09-11-cron-scheduling-delivery/MANIFEST.json); full queue + gerçek temp SQLite, synthetic transport |
| U07 main'de mi? | **[Güncel yayın makbuzu](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md)**. İlk girişimin unpublished kayıtları tarihsel bölümde korunur; U06 ayrı tamamlanmış yayındır. |
| U07 sonrasında teknik devam? | [STATE](STATE.md)/[PLAN](RESEARCH-PLAN.md) → [CRON-COVERAGE](inventory/CRON-COVERAGE-2026-09-11.md): actual gateway drainer/status consumer, occurrence/rearm, run_job bağlamı |
| Devam hangi history/hak/driver ile gerçek tura dönüşür? | **[21/U06](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md)** → [RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md) → [SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md) |
| U06 kaydındaki önceki koşu neyi sınadı? | [U06 SPEC](evidence/2026-09-11-resume-admission/SPEC.md) → [tam RESULT](evidence/2026-09-11-resume-admission/RESULT.json) → [MANIFEST/archive](evidence/2026-09-11-resume-admission/MANIFEST.json) → [README/reproduction](evidence/2026-09-11-resume-admission/README.md) |
| Önceki U06 yayını gerçekleşti mi? | [U06 PUBLICATION](evidence/2026-09-11-resume-admission/PUBLICATION.md); publication test ≠ behavior test |
| U05'in katkısı ve açık kontrolleri? | [20](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md) → [U05 source/research](evidence/2026-09-11-session-lease-recovery/RESEARCH.md), [CHECKS-NOT-RUN](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md); eski messages429 artık current değil |
| Kalıcı iş/devamın üst açıklaması? | [synthesis/03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md) → [18/U04-A](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → **20 + 21 + 22 source amendments** |
| Genel turn/context/session? | [synthesis/02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) → [16](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md) |
| Öğrenme/değişim? | [synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) → notes02–15; normal compaction counter-reading için 02/U02 |
| Task/run/claim/acceptance? | [17](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md) → [U03 RESEARCH](evidence/2026-09-10-kanban-task/RESEARCH.md)/[SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md) |
| U04-A/B aynı çalışma mı? | **[19](notes/19-U04-DELIVERY-RECONCILIATION.md)** → [B README](evidence/2026-09-11-multiturn/README.md) → [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) → [33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json) |
| A exact raw | [SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md)/[SPEC](evidence/2026-09-11-multi-turn-continuity/SPEC.md) → [raw archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz); summary yerine raw |
| B exact raw | [SOURCES](evidence/2026-09-11-multiturn/delivery/SOURCES.md) → [SPEC](evidence/2026-09-11-multiturn/delivery/evidence/SPEC.md) → [RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json) → [probe](evidence/2026-09-11-multiturn/delivery/evidence/probe.py) |
| Sonraki iş / bütünlük | [STATE](STATE.md)/[PLAN](RESEARCH-PLAN.md) → [U06 coverage](inventory/RESUME-ADMISSION-COVERAGE-2026-09-11.md); bütün HERMES hâlâ partial |

## Önceki notlara seçici erişim

| Alan | Giriş |
|---|---|
| Amaç/yöntem/topoloji | [00-WHY](00-WHY-THIS-RESEARCH.md), [STRUCTURE](inventory/STRUCTURE.md), [01](notes/01-ORIENTATION.md) |
| Review snapshot/fork | [02](notes/02-BACKGROUND-LEARNING.md) |
| Curator/maintenance/cron | [03](notes/03-SKILL-CURATION.md) |
| Skill transaction/approval | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md) |
| Mutable doc contracts | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) |
| Caller/worker transfer | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md) |
| MemoryStore/pending replay | [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) |
| Roundtrip/diff/rollback | [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md) |
| Selected worker policy | [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md) |
| Middleware/admission | [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) |
| Memory/pending state | [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md) |
| UI/profile caller | [12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md) |
| SA delivery | [13](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md) |
| AP delivery | [14](notes/14-AP-DELIVERY-RECONCILIATION.md) |
| M4 prompt/restore | [15](notes/15-MEMORY-PROMPT-RESTORE-BOUNDARIES.md) |
| Kaynak/tüm soru rotası | [SOURCE-LEDGER](SOURCE-LEDGER.md), [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

[V0.18 exact router](https://github.com/batuhanozgun/agentic-os-search/blob/0a475b5d7c50f47689c72cd31f954f5b2303ced6/research/studies/hermes-agent/INDEX.md) eski ayrıntılı evidence kısa yollarını da korur. Eski not/evidence dosyaları taşınmadı veya değişmedi.

## Cold-start uyarıları

STATE'teki zorunlu yol current'tır. U04-B delivery/repo-updates historical candidate'dır; eski 'yayımlanmadı' ifadesi current blocker değildir. A/B aynı G/H numaraları eş vaka değildir. U06 L testleri onlara eklenen ürün/bağımsız tekrar skoru değildir. Üç merkezi synthesis 20/21/22 ile birlikte okunur; final CORE/dört-alan/adoption yok.

U06'nın önceki ilk hedefi Q42 idi; U07'de alt source429 sonrasında açıkça ertelendi. Q40 actual-DB/quiet-history validation da açık. Cron/scheduler→run→delivery U07 ile başlatıldı; yeni ilk consumer STATE/PLAN'dadır. U05 source429 açılmıştır; actual DB/host testleri yapılmış değildir. Q07/Q22 wire/variants, Q26/Q29 full-worker, Q38 selection fidelity ve quality/delivery sınırları korunur.
