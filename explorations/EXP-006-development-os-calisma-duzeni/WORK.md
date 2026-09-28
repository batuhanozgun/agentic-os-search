# EXP-006 — WORK ve master plan

**Plan:** v1.6 — 28 Eylül 2026. **Current:** P4 / v2'nin stres testi ve sayfa sınırsız v3 yeniden yazımı yarım kaldı; yeni oturum için duraklatıldı. [STATE](STATE.md) yetkiyi, [HANDOFF](HANDOFF.md) devri, [P4-03](work/P4-03-unbounded-stress-test-handoff.md) aktif iş/kaynak sınırını taşır.

**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak. Bu plan SOUL'un teknik backlog'u değildir; ilk/sonraki gerçek SOUL işlerini ekip keşfeder.

## 1. Korunan zemin

SOUL hedefi → DevOS işi → kabiliyet/sorumluluk → rol/mekanik/insan sınırı → S1 → P1–P6.

| Kapsam | Korunmuş kaynak |
|---|---|
| B1 Ortak entelektüel taban | [B1](work/B1-common-intellectual-baseline.md) |
| B2 Bilgi kapasitesi | [B2](work/B2-information-capacity.md) |
| B3 Aktör kapasitesi | [B3](work/B3-actors-capacity.md) |
| B4 İş kapasitesi | [B4](work/B4-work-capacity.md) |
| B5 Ortam kapasitesi | [B5](work/B5-environment-capacity.md) |
| B6 Dört zeminin ilişkileri | [B6](work/B6-cross-ground-integration.md) |
| B7 İşe göre sistem oluşturma | [B7](work/B7-system-formation.md) |
| B8 Süreklilik/değişim/toparlanma/öğrenme | [B8](work/B8-continuity-change-recovery.md) |
| B9 Bütünleşme ve gerçek sınama | [B9](work/B9-integration-and-testing.md) |

B1–B9 geliştirme sırası veya SOUL modül listesi değildir. [S1](work/S1-role-responsibility-consolidation.md), [S1-17](work/S1-17-consolidation-closure-audit.md) ve [ACTORS](ACTORS.md) ilk R/M ve F/DR lineage'ını taşır. Rol sayısı actor sayısı değildir. S1-16 kaynak-tamlığı qualification'ı S1-17 §7'de korunur.

## 2. Sabit gereksinimler ve değişen teslimat

Claude Code cloud hedef Environment. K1 talep→çalışma→yanıt→gerçek kullanım. K2 rutin rol geçişlerinde Batu'nun mesaj taşıyan/tetikleyen kişi olmaması; başlangıç/yeniden başlatma, gerçek müdahale, yetki ve kabul mümkün.

D021 içerik sahibinin anlam/gerekçeyi, çalışma alanı tarafının yer/statü/bağ/bulunabilirlik/bakım/yeniden kullanımı taşımasıdır. Düzen yalnız klasör estetiği değildir. Ürün ve çalışma bilgisi ayrı amaçlı ve ilişkilidir. Foundation gereklilik keşfini, studies uygulama/karşı örnekleri besler; kaynak talimatları etkin kontrol değildir.

Kullanıcı önce SOUL hedefinden raporun baştan yazılmasını istedi; v2 bu görevin teslimidir. Ardından **v2'nin stres testi ve sayfa sınırı olmadan yeni rapor** istendi. Bu ikinci görev tamamlanmış değildir. 200 sayfa hedefi kaldırılmıştır. Gerekli kalite kolaylık veya hacim lehine düşürülmez; karmaşıklık ve uzunluk da kendi başına başarı değildir.

## 3. Bütün yol

| Aşama | Esas teslimat | Durum |
|---|---|---|
| P1 — Claude gerçekliği | Kaynaklı imkân/sınır haritası ve actual hedef soruları | P1-01 tarihsel kaynak sonucu; seçimi taşıyan güncel hedef kanıtı açık |
| P2 — Roller | Amaç/yeterlik/bilgi/teslimat/yetki/tüketici sözleşmeleri | P2-01 ilk taban; P3 G/Y ve v2 profilleriyle değerlendirilir |
| P3 — İş/bilgi/düzen | Keşif, katkı, karar, bakım, yeniden kullanım, kesinti/devri | P3-01 v0.5 kavramsal devir; canlı yeterlik değil |
| **P4 — Bütünleşik tasarım** | SOUL gereksinimlerinden mimari ve sınama programı | **AKTİF İŞ DURAKLATILDI: sayfa sınırsız stres testi/rapor v3; teslim doğrulanmadı.** V2 doğrulanmış dosya tabanı; P4-03 devam kaydı |
| P5 — Gerçekleştirme | Onaylanan mimarinin actual hizmet/dosya/izin/bağlantıları | DevOS kurulumu başlamadı; referans model production sistem değil |
| P6 — Hedef sınaması/devir | Gerçek otomatik akış, bilgi/etki/güvence, recovery ve bilişsel kalite | Hedefte yapılmadı; yerel model testleri yerine geçmez |

P1→P2↔P3→P4→P5→P6 bağı korunur. Somut ortam/rol/anlam kusurunda ilgili aşamaya dönülür; bütün taxonomy yeniden başlatılmaz. Yeni rapor talebi gerçek sistem kurulumuna otomatik yetki değildir.

## 4. P4'te korunacak taban ve sınanacak yapı

[P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) eski alt-ajan/Git ağırlıklı baseline. [P4-02](work/P4-02-soul-derived-report-v2.md) v2'nin teslimat ve mimari fark kaydıdır. Current sıra bunların tarihsel next'lerinden alınmaz.

V2: takım ağırlıklı Claude işbirliği + korunan kontrol; PostgreSQL canlı durum/typed relations; Git ürün/release; hash'li kanıt; hybrid retrieval/context compiler; publisher, outbox/inbox, read-set ve generation/fencing, DB–Git uzlaştırması. G/Y sorumluluğu ve shared runtime kimlik sınırı korunur. Bunlar stres testinin nesnesidir; kullanıcıca kabul edilmiş üstün çözüm veya kurulmuş mekanizma değildir.

Yeni inceleme yalnız graph, kod hataları veya dört bildirilmiş kusurla sınırlı değildir. SOUL'un ipucusuz iş keşfi, sistem oluşturma, araştırma kullanımı, uzun/bileşik iş ve yöntem aktarımı yükleri; teknik kontrol, memory/context, iletişim ve çalışma alanı düzeniyle birlikte ele alınır.

## 5. Devam haritası ve teslim koşulu

Tek ayrıntı evi [P4-03 §5](work/P4-03-unbounded-stress-test-handoff.md#5-yeni-oturumda-yapılacak-bütünlüklü-iş)'tir:

1. Gerçek v2 kaynaklarını hash'le doğrula; tam rapor/sözleşme/model bağlamını oku. Gerçek v3 dosyaları bulunursa kurtar, bulunamazsa eksik çalışmayı v2'den yeniden kur.
2. SOUL gereklilikleri ile mimari vaatleri, açık varsayımlar ve başarısızlık sınıflarını karşılaştır. Eksikliği sayfa sınırına peşinen bağlama.
3. V2 testlerini baseline olarak yeniden koş; yeni karşı örnekleri, gerekli concurrency/restore/graph/context ve bilişsel değerlendirme yollarını ayrı kanıt statüsüyle uygula.
4. Bulgu→kaynak/sürüm→yeniden üretim→tasarım düzeltmesi→yeniden sınama izini tut. Test sayısını yeterlik yerine geçirme.
5. Sayfa sınırsız bütünleşik raporu, düzenlenebilir metni, sözleşmeleri, ham test/QA ve yapılmayanlar kaydını birlikte üret; erişim ve readback ile teslim et.

Sadece raporu uzatmak veya 200 sayfalık yapıya ekler yapıştırmak görevi karşılamaz. Eski renderer'ın sabit sayfa/kapasite sınırı yeni yazıma aktarılmaz. Ortamda koşturulamayan testler başarı olarak sunulmaz; actual hedef yükleri açık kalır.

## 6. Gerçek devam durumu ve kaynak erişimi

Bu devir turunda v2 ZIP/PDF kimlikleri ve 22 manifest üyesi doğrulandı; test koşturulmadı. V3 rapor/kod/ham log mevcut mounted dosyalarda bulunamadı. Önceki dört kusur iddiası tekrar doğrulanacak ipucu; “88 test geçti” teyit edilmedi. Ayrıntı P4-03 §4'te.

`EXP-006_Yeni_Oturum_Devir_Paketi.zip` konuşma teslimidir; v2 PDF/kaynaklar ve devir notları içerir. **Tam kaynaklar repository'de değil, ekte.** Yeni oturumda bu ek veya hash-eşit kaynak gerekir. Kaynak olmadan özetten rapor incelemesi yapılmaz.

**Bu turun yetkisi:** Yeni oturum için devir hazırlığı; araştırma/yeniden yazımı burada durdur. **Sonraki yetkilendirilmiş devam:** Kullanıcının yeni oturumdaki devam yönüyle aynı P4 stres testi/rapor işi. P5/P6 ve eski izin-matrisi next'i değil.

## 7. Değişim izi

v1.0 plan; v1.1 P1; v1.2 P2; v1.3 P3 ve G/Y/D021; v1.4 P4-01; v1.5 SOUL odaklı v2 ve P4-02.

**v1.6 / 28 Eylül 2026:** Sayfa sınırının kaldırılması, doğrulanamayan v3 teslimi, kaynağı korunmuş v2 baseline ve yeni oturum devri kaydedildi. P4-03 aktif devamı taşır. Bu onarım yeni mimari veya yeni test sonucu üretmedi; eski doğrulanmamış başarıyı kalıcılaştırmadı.
