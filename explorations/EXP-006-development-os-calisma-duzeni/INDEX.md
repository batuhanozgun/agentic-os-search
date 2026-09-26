# EXP-006 — Development OS çalışma düzeni

**Tür:** Uzun soluklu kavramsal Development OS tasarım Work'ü; exploration kökenli yaşayan çalışma paketi.  
**Açılış:** 25 Eylül 2026.  
**Amaç:** SOUL'u yaratmak için Development OS'un yapacağı Work'ü, gereken kabiliyet/sorumlulukları ve bunlardan türeyen aktör/rol düzenini konuşarak ortaya çıkarmak.  
**Mimari statü:** Development OS kurulmuş veya nihai mimarisi kabul edilmiş değildir.

## Current authority sırası

Bir dosyada eski bir "sonraki adım", "dönüş" veya "current" ifadesi görülürse aşağıdaki sıra geçerlidir:

1. [STATE](STATE.md) — current phase, current result ve next responsibility.
2. [HANDOFF](HANDOFF.md) — fresh-session devir ve doğru devam noktası.
3. [WORK](WORK.md) — üst Work haritası ve active S1 durumu.
4. [ACTORS](ACTORS.md) — current **candidate** aktör/rol-family registry'si.
5. [S1 master](work/S1-role-responsibility-consolidation.md) — current rol-konsolidasyon yöntemi, dilimleri ve açık sorular.

Alt dal/slice dosyalarındaki eski sequencing cümleleri bu yüzeylerin önüne geçmez.

## Cold-start okuma yolu

Normal devam için:

1. STATE.md
2. HANDOFF.md
3. WORK.md
4. ACTORS.md
5. Active phase S1 ise work/S1-role-responsibility-consolidation.md
6. Yalnız current sorunun gerektirdiği work/B*.md veya work/S1-*.md ayrıntısı

Gerektiğinde:
- [DECISIONS](DECISIONS.md) — kullanıcıyla netleşmiş çalışma anlaşmaları.
- [EXP-006_Context](EXP-006_Context) — neden/nasıl çalıştığımızı ve tarihsel yön değişimlerini korur; current sequencing authority değildir.
- [sources/](sources/) — görünür kaynak aktarımları.
- [history/](history/) — superseded snapshot'lar; normal cold-start için okunmaz.

## Dosya sorumlulukları

| Yüzey | Tek işi |
|---|---|
| STATE.md | current state ve next responsibility |
| HANDOFF.md | yeni oturumun doğru current işi devralması |
| WORK.md | B1–B9 üst haritası + active S1 çalışma durumu |
| ACTORS.md | current candidate actor / role-family / mechanic registry |
| DECISIONS.md | kabul edilmiş çalışma anlaşmalarını candidate fikirlerden ayırmak |
| EXP-006_Context | kronolojik yön/metodoloji ve drift koruması |
| work/B*.md | B1–B9 reference decomposition; sequencing authority değildir |
| work/S1-role-responsibility-consolidation.md | active S1 master |
| work/S1-*.md | retained analytical slices; içlerindeki "next" cümleleri tarihsel olabilir |
| sources/ | kullanıcı/source aktarım kayıtları |
| history/ | current olmayan snapshot'lar; current karar/yön kaynağı değildir |

## Güncelleme disiplini

- current phase/next değiştiyse STATE.md + HANDOFF.md;
- üst Work/S1 durumu değiştiyse WORK.md;
- rol-family/sorumluluk modeli değiştiyse ACTORS.md;
- kullanıcıyla gerçekten netleşmiş karar oluştuysa DECISIONS.md;
- yön/metodoloji değiştiyse EXP-006_Context;
- ayrıntılı analiz kendi work/ slice'ında korunur.

Her mesaj repository mutation gerektirmez. Historical slice'lar current authority gibi güncellenmez.

## Sınır

Bu paket Development OS'un kendisi değildir. **Development OS'u tasarlama Work'ünün kalıcı çalışma sistemidir.** Rol familyası sayısı agent sayısı değildir; M1–M9 fiziksel servis/modül sayısı değildir.
