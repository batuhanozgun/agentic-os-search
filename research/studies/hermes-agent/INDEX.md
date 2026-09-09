# Hermes Agent — INDEX

Güncel çalışma/tamamlanma otoritesi [STATE](STATE.md); sınıflandırma/reuse otoritesi [META](META.md). Bu dosya retrieval rotasıdır.

| Soru | İlk kaynak |
|---|---|
| Amaç, kapsam, yöntem? | [00-WHY](00-WHY-THIS-RESEARCH.md), [METHOD](METHOD.md) |
| Neredeyiz, sıradaki yetkili iş? | [STATE](STATE.md) → [PLAN v0.9](RESEARCH-PLAN.md) |
| Okuma/kaynak/yürütme kapsamı? | [SOURCE-LEDGER](SOURCE-LEDGER.md) → ilgili yerel defter |
| Kaynak envanteri ve ilk keşif? | [STRUCTURE](inventory/STRUCTURE.md), [01](notes/01-ORIENTATION.md) |
| Deneyimden memory/skill değişikliğine geçiş? | [02 review](notes/02-BACKGROUND-LEARNING.md) |
| Beceri bakımı/merge/report/cron/geri alma? | [03 curator](notes/03-SKILL-CURATION.md) |
| Skill onayı, mutasyon ve normal/istisna rollback? | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md) |
| İlk iki-modül/10-durum deneyi ve yayını? | [U01B](evidence/2026-09-07-u01b/component-probe/README.md), [aktarım](evidence/2026-09-07-u01b/PUBLICATION.md) |
| İlk unpinned belge sözleşmeleri/K01–K09? | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md), [W defteri](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) |
| Ordinary caller/worker, ortak kontrol, sonuç kaydı? | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [D defteri](evidence/2026-09-08-context-transfer/SOURCES.md) |
| Memory mutator/kilit/reload/snapshot/pending replay? | [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md); yeni bounded yürütme için 11 |
| Önceki ContextVar/callback/sentetik-policy aktarım deneyi? | [Transport probe](evidence/2026-09-08-context-transfer/README.md) |
| Default-name payload/canlı diff/başka-yazar rollback? | [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [U01B2 kanıtı](evidence/2026-09-08-u01b2/README.md), [yayın](evidence/2026-09-08-u01b2/PUBLICATION.md) |
| Gerçek selected whitelist/executor + tam name-validator C/V deneyleri? | [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [worker-policy](evidence/2026-09-08-worker-policy/README.md), [yayın](evidence/2026-09-08-worker-policy/PUBLICATION.md) |
| Gerçek review constructor/ad-kümesi/round/Relay bağı? | [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) → [araştırma §3–5](evidence/2026-09-09-review-middleware/RESEARCH.md) |
| Eski seçkiler kaynakla karşılaştırıldı mı? | [RANGE-FIDELITY](evidence/2026-09-09-review-middleware/RANGE-FIDELITY.json): 22 manuel-range AST eşleşmesi; tam-original verifier değil |
| Gerçek middleware hata ve ikinci-call davranışı? | [MW01–MW08](evidence/2026-09-09-review-middleware/MIDDLEWARE-RESULT.json), [SPEC](evidence/2026-09-09-review-middleware/SPEC.md), [kod](evidence/2026-09-09-review-middleware/middleware_probe.py) |
| D3 kaynak pin/aralık/yerel byte sınırları? | [J defteri](evidence/2026-09-09-review-middleware/SOURCES.md), [erişim](evidence/2026-09-09-review-middleware/ACCESS.md), [yayın](evidence/2026-09-09-review-middleware/PUBLICATION.md) |
| M01/M02 artık gerçekten sınandı mı? | **[11 memory/pending](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md)** → [tam M2 araştırması](evidence/2026-09-09-memory-pending/RESEARCH.md), [N01–N12](evidence/2026-09-09-memory-pending/RESULT.json) |
| M2'nin gerçek modülleri ve taklit sınırları? | [M2 SOURCES](evidence/2026-09-09-memory-pending/SOURCES.md), [README](evidence/2026-09-09-memory-pending/README.md), [SPEC](evidence/2026-09-09-memory-pending/SPEC.md), [probe](evidence/2026-09-09-memory-pending/probe.py) |
| Son bellek/onay ZIP'i kaydedildi mi; eski NOT PUBLISHED ne demek? | [M2 PUBLICATION](evidence/2026-09-09-memory-pending/PUBLICATION.md), [TRANSFER-CHECK](evidence/2026-09-09-memory-pending/TRANSFER-CHECK.json); delivery altı özgün tarihsel teslimdir |
| M2 review notu D3'ün yerine mi geçiyor? | [M2 REVIEW-ADMISSION](evidence/2026-09-09-memory-pending/REVIEW-ADMISSION.md) ayrı statik kayıttır; J/MW ve bounded AST kanıtını ikame etmez |
| Açık sorular ve Q26 neden hâlâ açık? | [OPEN-QUESTIONS](OPEN-QUESTIONS.md), [10 araştırması §7–8](evidence/2026-09-09-review-middleware/RESEARCH.md) |

## Statü ayrımı ve yeni oturum

Pinned kaynak → mekanizma notları → sınırlı component/selected-function kanıtları. Native alt-sistem sentezleri, bütün ilişkiler, dört-alan/SOUL/DevOS ve CORE henüz yok. Toplam dosya/test sayısı tamamlanma ölçüsü değildir.

U01-D3, eski C/V deneylerini tekrarlamadı. Gerçek review kurulum kaynağı ile middleware çalıştırması farklı statülerdir. `canonical-ranges` tam canonical modül değil, yeni manuel transkripsiyondur. Büyük orijinallerle hash + eski verify_excerpts.py koşusu hâlâ açık; 22 AST eşleşmesi bunu kapatmaz.

U01-M2 ayrı beş-tam-modül/sentetik-çevre kaydıdır; yayın sırasında eski N01–N12 tekrarlanmadı. M01/M02 için bounded execution vardır; gerçek scanner, UI kimliği/config refresh ve API request doğrulaması yoktur. Gerçek dosya/live/snapshot/reload ayrımı actual UI/store binding yerine geçmez.

İlk aktif iş actual pending UI/caller/profil/store, ardından prompt/request görünümüdür. Q26 full integration yeni materyalizasyon/bağımlılık veya yük taşıyan reuse gerektiğinde yeniden açılır; aynı seçili fixture'ları çoğaltma. 09/10'un tarihsel ilk-iş listeleri current STATE/planın yerine geçmez. M2 taslağı 10 numarasıyla evidence/delivery altında korunur, doğru güncel giriş notes/11'dir. NOT PUBLISHED/eski erişim ifadeleri ilgili tarihsel tura aittir; paketler repo'da korunur, sohbet ZIP'i current çalışma yeri değildir.
