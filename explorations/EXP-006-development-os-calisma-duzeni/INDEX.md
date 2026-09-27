# EXP-006 — Development OS çalışma düzeni

**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini SOUL'un gerektirdiği kabiliyetlerden türetmek.
**Current:** [WORK](WORK.md) v1.5; **P4 / 200 SAYFALIK SOUL ODAKLI RAPOR v2 HAZIR / MİMARİ ÖNERİ / HEDEFTE KURULMADI.** P5/P6 gerçekleşmiş değildir.

## Güncel okuma yolu

AGENT ve gerekli kontrollerden sonra:

1. [STATE](STATE.md): son kullanıcı yetkisi, teslimat, yeni mimari farkı ve sınırlar.
2. [HANDOFF](HANDOFF.md): eski konuşmayı görmeyen oturumun devri.
3. [WORK](WORK.md): B/S1/P1–P6 bağı ve bütünsel harita.
4. [P4-02 — ikinci yazım kaydı](work/P4-02-soul-derived-report-v2.md): artefakt isim/hash'leri, yeni öneri, kaynak ve gerçek test sınırı.
5. **Gerçek v2 kaynak ZIP/PDF:** Ayrıntılı tasarım işi için gereken rapor gövdesi ve sözleşmeler. Dosyalar konuşma eklerinde; bu repository'ye tam gövdeleri yüklenmedi. Erişim yoksa ekteki kaynak dosya istenir, özetten yeniden uydurulmaz.
6. [DECISIONS](DECISIONS.md): kabul edilmiş D001–D022 sınırları. İçindeki P4-01 teknik tercih/next paragrafları eski checkpoint'tir; current v2 için STATE/WORK/P4-02 okunur.

Yeni rapor eski PDF'ye graph eki değildir; tüm tasarım SOUL hedefi üzerinden yeniden kurulmuştur. Raporun hazırlanmış olması yeni mimarinin kullanıcı kabulü veya runtime yeterliği değildir.

## Korunan kaynaklar ve lineage

| Yüzey | Rolü |
|---|---|
| [ACTORS](ACTORS.md), [P2-01](work/P2-01-named-role-contracts.md) | F1–F8/DR ilk adlandırılmış sözleşme tabanı; P3/v2 farklarından bağımsız son kadro değil |
| [P3-01](work/P3-01-work-information-discussion.md) | G/Y, içerik–düzen sahipliği, bakım ve H1–H6 kavramsal devir |
| [P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) | Önceki alt-ajan/Git ağırlıklı teknik baseline; current mimari değil |
| [P1-01](work/P1-01-claude-cloud-environment-map.md) | İlk platform kaynak haritası; hedef yeterliği kanıtı değil |
| [U002](sources/U002-cloud-plan-and-autonomy.md) | Cloud, iletişim, özerklik, plan ve kısa cevap kaynak mesajları |
| sources/U001.md, EXP-006_Context | Başlangıç ve tarihsel yön; current sequencing authority değil |
| work/B*.md, work/S1-*.md | İş kapsamı, sorumluluk türetimi ve kaynak izleri; SOUL'un actual backlog'u değil |
| history/ | Superseded snapshot; olağan açılışta gereksiz yüklenmez |

SOUL'un ilk/sonraki gerçek işlerini ekip keşfeder. Kullanıcı rutin dispatcher yapılmaz. İçerik sahibi ile çalışma alanı bakımının sorumluluğu ayrıdır. Claude cloud hedefi korunur; dış kontrol hizmetleri v2'nin değerlendirmeye sunulan tasarım önerisidir.

Kaynak ayrıntıları raporun kataloğundadır. Tekrar üretim paketi yerel referans modeli ve QA içerir; 40 test/dört guard denemesi hedef Claude/PostgreSQL kurulumu veya güvenlik ispatı değildir. Agent-control bu tur değişmedi.
