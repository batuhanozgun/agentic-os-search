# Hermes Agent — INDEX

Current work/completion [STATE](STATE.md); classification/reuse [META](META.md); yöntem [METHOD](METHOD.md); plan v0.13. Bu retrieval router bağımsız iş otoritesi değildir.

| Soru | Rota |
|---|---|
| Amaç ve yöntem | [00-WHY](00-WHY-THIS-RESEARCH.md), [METHOD](METHOD.md) |
| Nerede kaldık ve neden kapsam genişliyor? | [STATE](STATE.md), [PLAN](RESEARCH-PLAN.md), [SCOPE-REVIEW](inventory/SCOPE-REVIEW-2026-09-10.md) |
| **İlk birleşik learning/change açıklaması** | **[Synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md)**; provisional, bütün HERMES değil |
| İlk kaynak topolojisi | [STRUCTURE](inventory/STRUCTURE.md), [01](notes/01-ORIENTATION.md); alt envanter hâlâ kısmi |
| Review/snapshot/fork | [02](notes/02-BACKGROUND-LEARNING.md) |
| Curator bakım/report/cron | [03](notes/03-SKILL-CURATION.md) |
| Skill mutasyon/onay/rollback | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md) |
| Unpinned belge kontratları | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) |
| Caller/worker/persistence | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) |
| Memory/store/lock/frozen/pending | [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md), [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md) |
| Normal CLI/gateway onay caller/profil/store | [12/UI](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md), [13/M3-S-SA](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md) |
| Üçüncü AP teslimi ve ayrı kayıtlar | [14](notes/14-AP-DELIVERY-RECONCILIATION.md), [AP PUBLICATION](evidence/2026-09-10-ui-profile-approval/PUBLICATION.md) |
| **Fresh bellek neden eski stored prompt ile birleşebilir?** | **[15/M4](notes/15-MEMORY-PROMPT-RESTORE-BOUNDARIES.md)** → [RESEARCH](evidence/2026-09-10-prompt-restore/RESEARCH.md) |
| Yeni seçki/full-module/synthetic sınırı | [M4 SOURCES](evidence/2026-09-10-prompt-restore/SOURCES.md), [SPEC](evidence/2026-09-10-prompt-restore/SPEC.md) |
| V01–V08 ve karşı kontroller | [RESULT](evidence/2026-09-10-prompt-restore/RESULT.json), [probe](evidence/2026-09-10-prompt-restore/probe.py); actual request testi değildir |
| Yeni kanıt aktarım kimliği | [M4 MANIFEST](evidence/2026-09-10-prompt-restore/MANIFEST.json), [PUBLICATION](evidence/2026-09-10-prompt-restore/PUBLICATION.md) |
| Bütün kaynak/koşu kimlikleri | [SOURCE-LEDGER](SOURCE-LEDGER.md) → paket defterleri + exact [v0.9 arşivi](SOURCE-LEDGER-THROUGH-V0.9.md) |
| Açık sorular | [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

## Devam

İlk aktif iş genel turn/context/session çekirdeği ve geniş kaynak-topoloji karşı okumasıdır. M4 ordinary loop source bağı ilk rota; turn_context/request/compression ve gateway cache integration açık. Q07/Q22 bounded selector düzeyinde ilerledi, gerçek son istekte kapanmadı. Synthesis/01 bu açık kenarı taşır; onu final CORE sanma.

A/SA/AP/N/V farklı kayıt ve kapsamlar; sayıları ürün başarısına toplama. AP original 12 taslağı current 12 değildir; 14 current girişidir. Original NOT PUBLISHED/eski next-work cümleleri current STATE yerine geçmez. Q26/Q29 full-worker/full-original verifier açık. Bütün U01 residual'larını çözmek geniş araştırmanın ön koşulu değildir.
