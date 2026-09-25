# EXP-006 — Development OS çalışma düzeni

**Tür:** Uzun soluklu kavramsal Development OS tasarım Work'ü; exploration kökenli yaşayan çalışma paketi.  
**Açılış:** 25 Eylül 2026.  
**Amaç:** SOUL'u yaratmak için Development OS'un yapacağı Work'ü, gereken kabiliyet/sorumlulukları ve bunlardan türeyen aktör/rol düzenini konuşarak ortaya çıkarmak.  
**Mimari statü:** Development OS kurulmuş veya nihai mimarisi kabul edilmiş değildir.

## Cold-start okuma yolu

Yeni oturumda normal devam için:

1. [STATE](STATE.md) — current purpose, phase ve active Work.
2. [HANDOFF](HANDOFF.md) — tam devralma noktası ve sıradaki işlem.
3. [WORK](WORK.md) — B1–B9 haritası.
4. [ACTORS](ACTORS.md) — current rol/taşıyıcı registry'si.\n5. Aktif faz ve gerekiyorsa ilgili `work/B*.md` yolu — exact yön için [STATE](STATE.md) ve [HANDOFF](HANDOFF.md) current kaynaktır.

Gerektiğinde:
- [DECISIONS](DECISIONS.md) — kullanıcıyla netleşmiş çalışma kararları.
- [EXP-006_Context](EXP-006_Context) — yön/metodoloji ve drift koruması.
- [work/](work/) — B1–B9 dal dosyaları; yalnız active veya dependency-relevant dalı oku.
- [sources/U001](sources/U001.md) — açılış kaynağı.
- [history/](history/) — migration öncesi büyük current yüzeylerin tarihsel snapshot'ları; normal cold-start için okunmaz.

## Dosya sorumlulukları

| Yüzey | Tek işi |
|---|---|
| `STATE.md` | yalnız current state |
| `HANDOFF.md` | yeni oturumun doğru işi devralması |
| `WORK.md` | üst Work haritası ve sequencing |
| `work/B*.md` | B1–B9 ayrıntılı Work decomposition; S1'de yalnız dependency-relevant dallar okunur |
| `ACTORS.md` | aktör/rol/mekanik taşıyıcı registry'si |
| `DECISIONS.md` | kabul edilmiş çalışma kararlarını candidate fikirlerden ayırmak |
| `EXP-006_Context` | neden/nasıl çalıştığımızı ve drift korumasını taşımak |
| `sources/` | görünür kaynak aktarımları |
| `history/` | artık current olmayan büyük yüzeylerin snapshot'ları |

## Güncelleme disiplini

Material bir turda yalnız semantik olarak etkilenen yüzeyler güncellenir:

- aktif Work değiştiyse ilgili `work/B*.md` + `WORK.md`;
- rol/sorumluluk değiştiyse `ACTORS.md`;
- kullanıcı kararı oluştuysa `DECISIONS.md`;
- current phase/next değiştiyse `STATE.md` + `HANDOFF.md`;
- yön/metodoloji değiştiyse `EXP-006_Context`.

Her mesaj repository mutation gerektirmez.

## Sınır

Bu paket Development OS'un kendisi değildir. **Development OS'u tasarlama Work'ünün kalıcı çalışma sistemi**dir. Foundation terimleri dosya yapısına ontoloji olarak zorlanmamıştır.
