# Hermes Agent — INDEX

Bu dosya retrieval rotasıdır. Güncel iş/tamamlanma otoritesi [STATE.md](STATE.md), sınıflandırma ve reuse otoritesi [META.md](META.md)'dir.

| Soru | İlk kaynak |
|---|---|
| Neden araştırılıyor, kapsamı nedir? | [00-WHY-THIS-RESEARCH](00-WHY-THIS-RESEARCH.md) |
| Neredeyiz, sırada ne var? | [STATE](STATE.md) → [RESEARCH-PLAN](RESEARCH-PLAN.md), v0.7 |
| Dipten yukarı yöntem ve kapanış nasıl işliyor? | [METHOD](METHOD.md) |
| Hangi kaynak gerçekten okundu veya çalıştırıldı? | [SOURCE-LEDGER](SOURCE-LEDGER.md) → ilgili H/S/W/D/E defteri |
| Kaynak alanları ve eksik envanter nerede? | [STRUCTURE](inventory/STRUCTURE.md); güncel kaynak kapsamı için deftere dön |
| İlk keşif neyi değiştirdi? | [01-ORIENTATION](notes/01-ORIENTATION.md) |
| Deneyimden bellek/beceri değişikliğine geçiş nasıl işliyor? | [02-BACKGROUND-LEARNING](notes/02-BACKGROUND-LEARNING.md) |
| Beceri bakımı, birleştirme, rapor ve geri alma ne yapıyor? | [03-SKILL-CURATION](notes/03-SKILL-CURATION.md) |
| Onayda ne gösteriliyor; farklı hatalarda ne geri alınıyor? | [04-SKILL-WRITE-TRANSACTION-AND-APPROVAL](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md) |
| İlk bileşen deneyinin kodu, sonuçları ve sınırları? | [U01B](evidence/2026-09-07-u01b/component-probe/README.md) |
| İlk sohbet paketi nasıl repo'ya birleştirildi? | [U01B aktarımı](evidence/2026-09-07-u01b/PUBLICATION.md) |
| Dispatch/bellek/replay için ilk ek belge sözleşmeleri? | [05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md); tarihsel K01–K09 tasarımı |
| Belge turunda kod neden ilerlememişti? | [W01–W08 / tarihsel erişim](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md); current erişim durumu değil |
| Gerçek caller, ortak kontrol, worker, hata ve sonuç kaydı? | [06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md) |
| Memory mutator, kilit/reload, snapshot ve pending replay? | [07-MEMORY-STORE-AND-PENDING-REPLAY](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) |
| İlk context/callback/allowlist aktarımı nasıl sınandı? | [Transport probe](evidence/2026-09-08-context-transfer/README.md) → CHALLENGE / harness / RESULT / MANIFEST |
| Caller turunda hangi pinned modül ne derinlikte incelendi? | [D01–D22 defteri](evidence/2026-09-08-context-transfer/SOURCES.md) |
| Onay payload'ı hedefi koruyor mu; canlı diff ve rollback sınırları? | [08 U01B2 girişi](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md) → özgün araştırma / RESULT / SPEC / probe |
| U01B2 ZIP'i yayımlandı mı? | [U01B2 yayın kaydı](evidence/2026-09-08-u01b2/PUBLICATION.md) |
| Gerçek seçili policy tüketicisi ile worker birlikte nasıl sınandı? | **[09-WORKER-POLICY-EXECUTION-BOUNDARY](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md)** → [tam araştırma](evidence/2026-09-08-worker-policy/RESEARCH.md) |
| Son deneyde tam modül, seçki ve taklit sınırı nedir? | [E01–E07 kaynak defteri](evidence/2026-09-08-worker-policy/SOURCES.md), [README](evidence/2026-09-08-worker-policy/README.md) |
| 14 ana / 5 ek gözlem ve kimlik ret kontrolü nerede? | [RESULT](evidence/2026-09-08-worker-policy/RESULT.json), [VALIDATION-RESULT](evidence/2026-09-08-worker-policy/VALIDATION-RESULT.json), [IDENTITY-CHECK](evidence/2026-09-08-worker-policy/IDENTITY-CHECK.json) |
| Son worker-policy ZIP'i repo'ya aktarıldı mı? | [PUBLICATION](evidence/2026-09-08-worker-policy/PUBLICATION.md) → [TRANSFER-CHECK](evidence/2026-09-08-worker-policy/TRANSFER-CHECK.json) |
| Yeni oturumda ilk teknik kontrol nedir? | STATE → plan §4: tam pinned E01/E02 ile seçki sadakati; ardından gerçek review/worker erişilebilirliği. Aynı 14/5 fixture'ı tekrar üretmek değil. |
| Hangi sorular hâlâ açık? | [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

## Sentez katmanları

```text
Pinned kaynak                 primary pin korunuyor; caller/memory ve selected worker-policy
  ↓
Mekanizma notları              U01 / U01-C / U01B / U01-D / U01-M / U01B2 / U01-D2
Ayrı bileşen kanıtları         U01B, transport, U01B2; D2 selected-function + name-validator
Ek belge sözleşmesi           U01-DOC / W01–W08; pin'e eşitlenmedi
  ↓
Tam review/worker entegrasyonu D2'nin artık sorusu; manuel excerpt AST kontrolü NOT RUN
Native alt-sistem sentezleri   henüz yok; notlar tam aile kapanışı değil
  ↓
Sistemler arası ilişkiler      yerel bağlantılar; genel sentez yok
  ↓
Dört-alan projeksiyonu         henüz yok
  ↓
SOUL / Development OS ve CORE henüz yok
```

Sayılar tamamlanma veya ürün PASS ölçüsü değildir. U01-C curator kimliği korunur; D2 önceki kaynak notlarını ve transport deneyini ikame etmez. 04'ün S-ID'leri U01B'ye; 02/03'ün H-ID'leri ana deftere; 05'in W-ID'leri belge defterine; 06/07'nin D-ID'leri D defterine; 09'un E/C/V kimlikleri worker-policy paketine bağlanır. U01B2'nin yerel deney kimlikleri bu defterlerle karıştırılmaz.

Eski notlardaki 'yazılamadı/429/ilk sonraki dosya' ifadeleri kendi tarihsel turunu anlatır. U01B2 ve worker-policy özgün teslimlerindeki NOT PUBLISHED/NOT APPLIED ile eski plan ifadeleri ilgili PUBLICATION dosyalarıyla tarihsel bağlama alınır; current STATE'in yerine geçmez. Worker-policy/REPO-NOTE-09.md evidence içinde tarihsel taslaktır; güncel ve doğru göreli bağlantılı giriş notes/09'dur. Dokuz K kontrolünün tümü çalıştırılmış değildir. Son yayın yeni deney veya tamamlanmış HERMES sistemi değildir.
