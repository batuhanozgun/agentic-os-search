# Hermes Agent — INDEX

Bu dosya retrieval rotasıdır. Güncel iş/tamamlanma otoritesi [STATE.md](STATE.md), sınıflandırma ve reuse otoritesi [META.md](META.md)'dir.

| Soru | İlk kaynak |
|---|---|
| Neden araştırılıyor, kapsamı nedir? | [00-WHY-THIS-RESEARCH](00-WHY-THIS-RESEARCH.md) |
| Neredeyiz, sırada ne var? | [STATE](STATE.md) → [RESEARCH-PLAN](RESEARCH-PLAN.md) |
| Dipten yukarı yöntem ve kapanış nasıl işliyor? | [METHOD](METHOD.md) |
| Hangi kaynak gerçekten okundu, hangisi dar deneyde kullanıldı? | [SOURCE-LEDGER](SOURCE-LEDGER.md) |
| Kaynak alanları ve eksik envanter nerede? | [STRUCTURE](inventory/STRUCTURE.md) |
| İlk keşif neyi değiştirdi? | [01-ORIENTATION](notes/01-ORIENTATION.md) |
| Deneyimden bellek/beceri değişikliğine geçiş nasıl işliyor? | [02-BACKGROUND-LEARNING](notes/02-BACKGROUND-LEARNING.md) |
| Birikmiş becerilerin bakımı, birleştirme, rapor ve geri alma ne yapıyor? | [03-SKILL-CURATION](notes/03-SKILL-CURATION.md) |
| Onayda hangi değişiklik gösteriliyor; farklı hatalarda ne geri alınıyor? | [04-SKILL-WRITE-TRANSACTION-AND-APPROVAL](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md) |
| Bileşen deneyinin kodu, sonuçları ve sınırları nerede? | [U01B deney girişi](evidence/2026-09-07-u01b/component-probe/README.md) → RESULT / harness / upstream |
| Sohbetteki teslim paketi neden vardı, repo'ya nasıl birleştirildi? | [U01B aktarım kaydı](evidence/2026-09-07-u01b/PUBLICATION.md) |
| Hangi soru hâlâ açık? | [OPEN-QUESTIONS](OPEN-QUESTIONS.md) |

## Sentez katmanlarının durumu

```text
Pinned kaynak                 mevcut; primary pin korunuyor
  ↓
Mekanizma notları              U01 + U01-C + U01B kısmi kesitleri
Bileşen kanıtı                iki exact modül, sentetik bağımlılıklar; tüm ürün değil
  ↓
Native alt-sistem sentezleri   henüz yok
  ↓
Sistemler arası ilişkiler      yerel bağlantı adayları var; genel sentez yok
  ↓
Dört-alan projeksiyonu         henüz yok
  ↓
SOUL / Development OS karşılığı ve çekirdek sonuç  henüz yok
```

CORE henüz üretilmedi. Aile tablosu araştırma planıdır, kabul edilmiş mimari değildir. U01-C, mevcut curator biriminin kimliğidir; eski yerel v0.3 taslağındaki U01C caller adı onun yerine geçmez. Kaynağa dönüş için 04 notunun S-ID'leri U01B defterine, 02/03 notlarının H-ID'leri ana kaynak defterine bağlanır. Aktarılan eski SOURCES/RESULT içindeki yayın-yok ifadeleri ilk araştırma turunun tarihsel kaydıdır; güncel STATE'e alternatif değildir.
