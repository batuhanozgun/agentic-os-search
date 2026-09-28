# EXP-006 — STATE

**Durum:** AÇIK / P4 v3 rapor ve kanıt teslimi hazır / kullanıcı değerlendirmesi bekleniyor.
**Güncelleme:** 28 Eylül 2026. **Üst plan:** [WORK](WORK.md) v1.7.
**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini SOUL'un gerektirdiği gerçek kabiliyetlerden türetmek.
**Current:** [P4-04 — sayfa sınırsız stres testi ve v3 raporu](work/P4-04-unbounded-stress-test-report-v3.md). Rapor teslimi tamamlandı; mimari/DevOS/SOUL yeterliği kabul edilmiş veya hedefte gösterilmiş değildir. P5 kurulumu ve P6 hedef kabulü yapılmadı.

## Son kullanıcı yönü ve karşılığı

Kullanıcı yeni oturumda “EXP-006’nın sayfa sınırsız stres testi ve rapor çalışmasına devam et” dedi ve gerçek devir ZIP'sini ekledi. D025'in önceki turda durma sınırı tamamlandı; aynı P4 işi D026 ile sürdürüldü. Sayfa sınırı yoktur. İş gerçek v2 kaynaklarından yeniden kuruldu; eski teyitsiz “88 test/v3 hazır” beyanı kanıt sayılmadı.

31 bölümlü bütünleşik v3 raporu, düzenlenebilir Markdown, sözleşmeler, referans model, ham test/QA ve kaynak paketi üretildi. PDF doğal akışta 50 sayfadır; uzunluk yeterlik ölçüsü değildir. Amaç, kapsam, rol, keşif, bilgi/bağlam, ilişkiler, kontrol, yayın, recovery, uzun ürün ve yöntem aktarımı birlikte işlendi.

## Doğrudan gözlenen ve açık kalan

Sekiz sınırlı v2 karşı örneği yeniden üretildi; eski dört ipucu bunların içindedir. V2'nin 40 testi/dört guard deneyi ayrıca yeniden koşuldu. V3 yerel modelinde 53 test geçti. Sekiz yeni bozmanın yedisi hedefli assertion, biri sonraki KeyError ile sonuçlandı; ikincisi eşdeğer doğrulama sayılmadı. Kod/sözleşme farkları ve düzeltme sınırları P4-04'te.

Yerel Python/SQLite ve geçici bare Git koşuları vardır. Gerçek Claude cloud, PostgreSQL, bağımsız güvence, korunan principal/publication, dağıtık restore ve SOUL bilişsel yeterliği **açıktır**. On iki senaryo masa başıdır. Tasarım önerisi, şema, yerel kod ve hedef davranış aynı kanıt değildir.

PDF 666/666 metin birimi, glif/geometri/dahili bağlantı kontrolünden geçti; tüm sayfalar görsel gözden geçirildi. ZIP CRC ve 76 manifest üyesi hash/boyut eşleşti. Bu kimlik/düzen kontrolüdür; genel doğruluk sertifikası değildir.

## Gerçek kaynak erişimi

Güncel kaynak: **`EXP-006_DevOS_v3_Kaynak_ve_Kanit_Paketi.zip`**, 1776487 byte; SHA-256 `df9e1ef363b649e82dc88341aaeba2028852878d4e36131f30738a7d548ee100`.

Tam rapor ve kod konuşma teslim eklerindedir; repository P4-04 ve devam durumunu taşır, ZIP'nin tam gövdesini değil. Yeni oturumda ayrıntılı inceleme için bu gerçek paket veya aynı hash'li kaynaklar gerekir. Kaynak yoksa özetten rapor/kod yeniden kurulmaz. Eski `EXP-006_Yeni_Oturum_Devir_Paketi.zip` yalnız v2 tabanını taşır; v3 yerine kullanılamaz.

## Korunan sınırlar

Claude Code cloud hedefi, K1 talep→çalışma→yanıt→kullanım, K2 rutin geçişlerde Batu'nun taşıyıcı/tetikleyici olmaması, gerçek insan müdahalesi/yetki/kabul, G/Y ve D021 içerik–düzen sahipliği korunur. SOUL'un ilk ve sonraki gerçek işlerini ekip keşfeder; assistant hazır backlog seçmez. Rol sayısı agent sayısı değildir. V3 teknik tercihleri kullanıcı kabulü değil, sınanacak öneridir.

## Current devam

AGENT ve gerekli kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → WORK → DECISIONS → P4-04 → gerçek v3 kaynak paketi. P4-03 yarım çalışma/devrin tarihsel kaydı, P4-02 v2 provenance, P4-01 eski baseline'dır; kendi eski next'leri current olmaz.

**Bu teslimden sonra kullanıcıya dönüş:** P4 v3 değerlendirmesi. Açık H kapıları raporda görünürdür; actual cloud/K1/K2 yeterliğini somutlaştırmak sonraki mantıksal iştir, otomatik P5/P6 yetkisi değildir. EXP-006 veya mimari kabulü kapatılmadı.
