# Hermes Agent — INDEX

Work/completion [STATE](STATE.md); classification/reuse [META](META.md); yöntem [METHOD](METHOD.md). Current plan v0.12. Bu dosya bağımsız iş otoritesi değildir.

| Soru | Rota |
|---|---|
| Amaç ve yöntem | [00-WHY](00-WHY-THIS-RESEARCH.md), [METHOD](METHOD.md) |
| Nerede kaldık / neden bu sonraki adım? | [STATE](STATE.md), [PLAN](RESEARCH-PLAN.md), [kapsam değerlendirmesi](inventory/SCOPE-REVIEW-2026-09-10.md) |
| İlk topoloji | [STRUCTURE](inventory/STRUCTURE.md), [01](notes/01-ORIENTATION.md) |
| Review/snapshot/fork | [02](notes/02-BACKGROUND-LEARNING.md) |
| Curator bakım/report/cron | [03](notes/03-SKILL-CURATION.md) |
| Skill mutasyon/onay/rollback | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md) |
| Unpinned belge kontratları | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) |
| Caller/worker/persistence | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) |
| Memory/store/lock/frozen/pending | [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md), [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md) |
| Normal CLI/gateway onay caller/profil/store | [12/UI](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md), [13/M3-S-SA](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md) |
| Sonradan bulunan üçüncü AP teslimi | [14](notes/14-AP-DELIVERY-RECONCILIATION.md), [arşiv/README](evidence/2026-09-10-ui-profile-approval/README.md) |
| A, SA, AP neden aynı sonuç değildir? | [AP PUBLICATION](evidence/2026-09-10-ui-profile-approval/PUBLICATION.md) |
| AP özgün araştırma ve deney | [RESEARCH](evidence/2026-09-10-ui-profile-approval/original/evidence/RESEARCH.md), [SOURCES](evidence/2026-09-10-ui-profile-approval/original/evidence/SOURCES.md), [RESULT](evidence/2026-09-10-ui-profile-approval/original/evidence/ACCESS-RESULT.json), [SPEC](evidence/2026-09-10-ui-profile-approval/original/evidence/SPEC.md) |
| Bütün kaynak/koşu kimlikleri | [SOURCE-LEDGER](SOURCE-LEDGER.md) → paket defterleri ve exact [v0.9 arşivi](SOURCE-LEDGER-THROUGH-V0.9.md) |
| Açık sorular | [OPEN-QUESTIONS](OPEN-QUESTIONS.md); prior detailed table Git snapshot'ında korunur |

## Devam

İlk aktif teknik soru Q07/Q22: onaydan store/frozen/stored-cached prompt/prepared request'e. `_restore_or_build_system_prompt`, invalidation/rebuild/compression/keep-prompt ve cache reuse/eviction kaynakla bağlanır. A/SA/AP/N fixture çoğaltmak bu köprüyü kapatmaz. Sonra kanıt statülü geçici alt-sistem sentezi ve geniş topoloji/omission kontrolü.

AP original 12 taslağı current 12 değildir; 14 girişini kullan. `original/` içindeki NOT PUBLISHED/plan v0.9 ve önceki evidence'deki tarihsel next-work ifadeleri current authority değildir. 12/A ve 13/SA aynen korunmuştur; AP bunların yerine geçmez.

Q26/Q29 full worker ve full-original legacy verifier açık. Genel HERMES, dört-alan ve CORE tamamlanmadı. [V0.11 tam router](https://github.com/batuhanozgun/agentic-os-search/blob/634ab66f195130d551d58dfc062639e0feec23fa/research/studies/hermes-agent/INDEX.md) eski ayrıntılı yolları da korur.
