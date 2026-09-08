# Hermes Agent — INDEX

Bu dosya retrieval rotasıdır. Güncel iş/tamamlanma otoritesi [STATE.md](STATE.md), sınıflandırma ve reuse otoritesi [META.md](META.md)'dir.

| Soru | İlk kaynak |
|---|---|
| Neden araştırılıyor, kapsamı nedir? | [00-WHY-THIS-RESEARCH](00-WHY-THIS-RESEARCH.md) |
| Neredeyiz, sırada ne var? | [STATE](STATE.md) → [RESEARCH-PLAN](RESEARCH-PLAN.md) |
| Dipten yukarı yöntem ve kapanış nasıl işliyor? | [METHOD](METHOD.md) |
| Hangi kaynak gerçekten okundu, hangisi dar deneyde kullanıldı? | [SOURCE-LEDGER](SOURCE-LEDGER.md) |
| Kaynak alanları ve eksik envanter nerede? | [STRUCTURE](inventory/STRUCTURE.md); yeni D kaynak kapsamı için deftere dön |
| İlk keşif neyi değiştirdi? | [01-ORIENTATION](notes/01-ORIENTATION.md) |
| Deneyimden bellek/beceri değişikliğine geçiş nasıl işliyor? | [02-BACKGROUND-LEARNING](notes/02-BACKGROUND-LEARNING.md) |
| Beceri bakımı, birleştirme, rapor ve geri alma ne yapıyor? | [03-SKILL-CURATION](notes/03-SKILL-CURATION.md) |
| Onayda ne gösteriliyor; farklı hatalarda ne geri alınıyor? | [04-SKILL-WRITE-TRANSACTION-AND-APPROVAL](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md) |
| İlk bileşen deneyinin kodu, sonuçları ve sınırları? | [U01B](evidence/2026-09-07-u01b/component-probe/README.md) |
| Sohbetteki teslim paketi nasıl repo'ya birleştirildi? | [U01B aktarımı](evidence/2026-09-07-u01b/PUBLICATION.md) |
| Dispatch/bellek/replay için ilk ek belge sözleşmeleri? | [05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md); tarihsel K01–K09 tasarımı |
| Belge turunda kod neden ilerlememişti? | [W01–W08 / tarihsel erişim](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md); current erişim durumu değil |
| Gerçek caller, ortak kontrol, worker, hata ve sonuç kaydı? | [06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md) |
| Memory mutator, kilit/reload, snapshot ve pending replay? | [07-MEMORY-STORE-AND-PENDING-REPLAY](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) |
| ContextVar/callback/allowlist aktarımı gerçekten nasıl sınandı? | [Transport probe](evidence/2026-09-08-context-transfer/README.md) → CHALLENGE / harness / RESULT / MANIFEST |
| Bu tur hangi pinned modül ne derinlikte incelendi? | [D01–D22 kaynak defteri](evidence/2026-09-08-context-transfer/SOURCES.md) |
| Hangi soru hâlâ açık? | [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

## Sentez katmanları

```text
Pinned kaynak                 primary pin korunuyor; ordinary caller/memory kapsamı genişledi
  ↓
Mekanizma notları              U01 / U01-C / U01B + U01-D / U01-M kısmi kesitleri
Bileşen kanıtı                U01B: 2 exact modül/10 durum; transport: 3 exact modül/7 durum
Ek belge sözleşmesi           U01-DOC / W01–W08; pin'e eşitlenmedi
  ↓
Native alt-sistem sentezleri   henüz yok; notlar tam aile kapanışı değil
  ↓
Sistemler arası ilişkiler      yerel bağlantılar; genel sentez yok
  ↓
Dört-alan projeksiyonu         henüz yok
  ↓
SOUL / Development OS ve CORE henüz yok
```

Sayılar tamamlanma veya ürün PASS ölçüsü değildir. U01-C curator kimliği korunur; U01-D yeni caller/transfer notunu, U01-M memory notunu adlandırır. 04'ün S-ID'leri U01B'ye; 02/03'ün H-ID'leri ana deftere; 05'in W-ID'leri belge defterine; 06/07'nin D-ID'leri yeni kaynak defterine bağlanır. Eski notlardaki 'yazılamadı/429/ilk sonraki dosya' ifadeleri kendi tarihsel turunu anlatır; current STATE'in yerine geçmez. 05/K03'ün yalnız transport alt sorusu yeni probe ile kısmen sınandı; dokuz kontrol bütünüyle çalıştırılmış değildir.
