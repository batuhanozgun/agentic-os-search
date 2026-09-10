# Hermes Agent — INDEX

Current work/completion authority [STATE](STATE.md); classification/reuse [META](META.md); method [METHOD](METHOD.md). This file is the retrieval router, not independent work authority.

| Soru | İlk kaynak |
|---|---|
| Amaç/kapsam ve dipten yukarı yöntem? | [00-WHY](00-WHY-THIS-RESEARCH.md), [METHOD](METHOD.md) |
| Nerede kaldık, sıradaki yetkili iş? | [STATE](STATE.md) → [plan v0.10](RESEARCH-PLAN.md) |
| Kaynak ve yürütme kayıtları? | [SOURCE-LEDGER](SOURCE-LEDGER.md): yeni UI defteri + exact donmuş v0.9 birikimli defter |
| İlk envanter/keşif? | [STRUCTURE](inventory/STRUCTURE.md), [01](notes/01-ORIENTATION.md) |
| Review öğrenmesi, snapshot/fork/köken? | [02](notes/02-BACKGROUND-LEARNING.md) |
| Curator bakım/merge/report/cron? | [03](notes/03-SKILL-CURATION.md) |
| Skill onayı/normal ve exception rollback? | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [U01B](evidence/2026-09-07-u01b/component-probe/README.md) |
| Unpinned belge kontratları/K01–K09? | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md), [W defteri](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| Ordinary caller/worker/ortak kontrol/persistence? | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [D kaynakları](evidence/2026-09-08-context-transfer/SOURCES.md) |
| Store/lock/reload/frozen snapshot/pending replay? | [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) |
| Önceki sentetik-policy transport deneyi? | [Transport probe](evidence/2026-09-08-context-transfer/README.md) |
| Default-name payload/canlı diff/başka-yazar rollback? | [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [U01B2](evidence/2026-09-08-u01b2/README.md) |
| Selected worker/executor/whitelist ve tam validator? | [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [E/C/V](evidence/2026-09-08-worker-policy/README.md) |
| Gerçek review kurulum/round/Relay; middleware hataları? | [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md), [J/MW](evidence/2026-09-09-review-middleware/README.md) |
| M2 beş-modül memory failure/alias/pending kanıtı? | [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md), [M2/N](evidence/2026-09-09-memory-pending/README.md) |
| **Gerçek CLI/gateway onayı hangi store/profil/yetki üzerinden gider?** | **[12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md)** → [RESEARCH](evidence/2026-09-10-ui-profile/RESEARCH.md) |
| Yeni kaynakların path/blob/aralık ve full/selected ayrımı? | [UI01–UI13](evidence/2026-09-10-ui-profile/SOURCES.md) |
| Komut-izin modülünün yeni sekiz tanılayıcı koşusu? | [RESULT](evidence/2026-09-10-ui-profile/RESULT.json), [SPEC](evidence/2026-09-10-ui-profile/SPEC.md), [kod](evidence/2026-09-10-ui-profile/policy_probe.py) |
| Yeni kanıtın yayını ve içerik kimliği? | [PUBLICATION](evidence/2026-09-10-ui-profile/PUBLICATION.md), [MANIFEST](evidence/2026-09-10-ui-profile/MANIFEST.json) |
| Açık sorular ve ileri doğrulama? | [OPEN-QUESTIONS](OPEN-QUESTIONS.md), STATE ve plan |

## Yeni oturumda doğru devam

İlk aktif iş **onaydan sonraki gerçek prompt/prepared-request görünürlüğü**. CLI live/fresh, gateway fresh apply ile cached agent reuse'u ayrı izle. Yeni A01–A08 sadece slash policy modülüdür; UI/profile end-to-end testi değildir. M2/N ve D3/MW bu tur tekrar çalıştırılmadı.

Q26/Q29 full worker/runtime ve legacy full-original verifier açık. 22 manuel-range AST eşitliği tam-original fidelity değildir. Yeni tam-source/bağımlılık veya load-bearing reuse olmadan aynı selected fixture'ları çoğaltma.

Donmuş SOURCE-LEDGER-THROUGH-V0.9, eski notlar ve teslim PUBLICATION metinleri kendi tarihsel next-work/access sınırlarını taşır; current STATE/plan yerine geçmez. Eski bütün ZIP kanıtları repodadır, tekrar aktarım gerekmiyor. Native alt-sistem/genel ilişkiler/dört-alan/SOUL/DevOS/CORE tamamlanmadı; dosya/test sayısı tamamlanma veya ürün PASS ölçüsü değildir.
