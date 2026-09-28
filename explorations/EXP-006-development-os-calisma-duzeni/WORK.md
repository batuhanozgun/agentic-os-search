# EXP-006 — WORK ve master plan

**Plan:** v1.7 — 28 Eylül 2026. **Current:** P4 sayfa sınırsız stres testi/rapor v3 teslimi hazır; kullanıcı değerlendirmesi bekleniyor. [STATE](STATE.md) yetkiyi, [HANDOFF](HANDOFF.md) devri, [P4-04](work/P4-04-unbounded-stress-test-report-v3.md) güncel rapor/kanıt ve kaynak erişimini taşır.

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

Kullanıcı önce SOUL hedefinden raporun baştan yazılmasını istedi; v2 bu görevin tarihsel teslimidir. Sonra v2'nin stres testi ve sayfa sınırı olmadan yeni rapor istendi. Önceki yarım çalışma P4-03 ile devredildi; yeni oturumdaki açık devam yönüyle v3 bu tur üretildi. Rapor teslimi hazırdır; mimari veya hedef yeterliği kabul edilmiş değildir. 200 sayfa hedefi kaldırılmıştır. Gereken kalite kolaylık veya hacim lehine düşürülmez; karmaşıklık ve uzunluk da kendi başına başarı değildir.

## 3. Bütün yol

| Aşama | Esas teslimat | Durum |
|---|---|---|
| P1 — Claude gerçekliği | Kaynaklı imkân/sınır haritası ve actual hedef soruları | P1-01 tarihsel sonuç; v3'te ilgili güncel resmî kaynaklar seçici tazelendi, actual hedef kanıtı açık |
| P2 — Roller | Amaç/yeterlik/bilgi/teslimat/yetki/tüketici sözleşmeleri | P2-01 ilk taban; P3 G/Y ve v2/v3 profilleriyle değerlendirilir; son kadro kabulü değil |
| P3 — İş/bilgi/düzen | Keşif, katkı, karar, bakım, yeniden kullanım, kesinti/devri | P3-01 v0.5 kavramsal devir; v3 bütünleşmesi gerçek canlı yeterlik değil |
| **P4 — Bütünleşik tasarım** | SOUL gereksinimlerinden mimari ve sınama programı | **V3 RAPOR/KAYNAK TESLİMİ HAZIR; kullanıcı değerlendirmesi bekleniyor.** P4-04 güncel sonuç ve açık H kapıları |
| P5 — Gerçekleştirme | Onaylanan mimarinin actual hizmet/dosya/izin/bağlantıları | DevOS kurulumu başlamadı; referans model production sistem değil |
| P6 — Hedef sınaması/devir | Gerçek otomatik akış, bilgi/etki/güvence, recovery ve bilişsel kalite | Hedefte yapılmadı; yerel model testleri yerine geçmez |

P1→P2↔P3→P4→P5→P6 bağı korunur. Somut ortam/rol/anlam kusurunda ilgili aşamaya dönülür; bütün taxonomy yeniden başlatılmaz. Raporun hazır olması gerçek sistem kurulumuna otomatik yetki değildir.

## 4. P4'te değerlendirilen yapı ve sonuç

[P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) eski alt-ajan/Git ağırlıklı baseline; [P4-02](work/P4-02-soul-derived-report-v2.md) v2 teslimi; [P4-03](work/P4-03-unbounded-stress-test-handoff.md) yarım v3 ve kaynak devri. Current bunların tarihsel next'lerinden alınmaz.

V3; bilişsel ekip ve korunan kontrol, PostgreSQL canlı durum/typed relations önerisi, Git ürün/release, kaynak/kanıt, memory/context ve kontrollü publication/recovery yönünü koşullu korur. Tam işlem niyeti, tüketici context yükleri/actual view, scope, epoch/assignment, state/event, etki tarihçesi, güncel önkoşul ve graph sorgu tamlığı ayrımlarını güçlendirir. Bunlar benimsenmiş/kurulmuş mekanizmalar değil, yeni raporun sınanacak önerileridir.

İnceleme sekiz teknik karşı örnekle sınırlı değildir. SOUL'un ipucusuz iş keşfi, sistem oluşturma, araştırma kullanımı, uzun/bileşik iş ve yöntem aktarımı yükleri de rol, iletişim ve çalışma alanı düzeniyle birlikte ele alınır. On iki senaryo masa başı tasarım değerlendirmesidir; bağımsız gerçek görev başarısı değildir.

## 5. Bu teslimde yapılan bütünlüklü iş

1. V2 kaynak kimlikleri ve manifest doğrulandı; 200 bölüm/sayfa işaretli gövde, sözleşmeler, model ve test bağlamı okundu.
2. SOUL gereklilikleri ile mimari vaatler, açık varsayımlar ve başarısızlık yolları karşılaştırıldı; RPD/EXP-004 kaynakları ve dört resmî teknik belge gereken kapsamda kullanıldı.
3. V2 baseline yeniden koşuldu; sekiz karşı örnek üretildi. V3 yerel model/testleri ve kasıtlı kontrol bozma kanıtı ayrı statüyle kaydedildi.
4. Bulgu→kaynak→yeniden üretim→sözleşme/model değişimi→yeniden sınama bağı rapor ve pakette kuruldu. Yedi assertion/tek KeyError ayrımı korundu.
5. 31 bölümlü sayfa sınırsız rapor, PDF, kaynak kataloğu, sözleşmeler, model, ham QA ve manifest paketlendi. PDF metin/link/geometri ve görsel kontrolü ile ZIP kimlik kontrolü yapıldı.

Bu, rapor tesliminin tamamlanmasıdır. Claude/PG/korunan service/restore/bağımsız bilişsel kanıt yokluğu giderilmiş sayılmaz. Test sayısı yeterliğin yerine geçmez.

## 6. Gerçek devam durumu ve kaynak erişimi

**Güncel kaynak paketi:** `EXP-006_DevOS_v3_Kaynak_ve_Kanit_Paketi.zip`. Tam rapor/kod konuşma eklerindedir; repository P4-04, durum ve erişim yolunu taşır. Hash/byte ve kanıt ayrıntısı P4-04'tedir. Yeni oturum bu pakete veya aynı gerçek kaynaklara erişmeden ayrıntılı incelemeye özetten başlamaz. Eski devir ZIP'si yalnız v2'dir.

**Şimdi yetkilendirilmiş sonuç:** P4 v3 rapor/kanıt teslimini kullanıcıya döndürmek ve değerlendirmesini almak. İtiraz/revizyon varsa aynı P4 kaynağından ilgili yüzeye inilerek sürdürülür.

**Sonraki mantıksal iş:** Açık H kapılarının, özellikle actual cloud/K1/K2'nin, gerçek erişim ve uygun kullanıcı yönüyle somutlaştırılması. Bu iş raporun varlığıyla otomatik yetkilendirilmiş değildir. P5/P6 veya ilk SOUL backlog'u başlatılmaz; EXP-006/mimari kabulü kapanmadı.

## 7. Değişim izi

v1.0 plan; v1.1 P1; v1.2 P2; v1.3 P3 ve G/Y/D021; v1.4 P4-01; v1.5 SOUL odaklı v2 ve P4-02.

**v1.6 / 28 Eylül 2026:** Sayfa sınırının kaldırılması, doğrulanamayan v3 teslimi, v2 baseline ve yeni oturum devri P4-03'te kaydedildi. O tur yeni mimari/test üretmedi.

**v1.7 / 28 Eylül 2026:** Yeni oturumdaki devam yönüyle v2 yeniden okundu/koşuldu, sekiz karşı örnek, 53 testli sınırlı v3 model, yedi assertion/tek error bozma ve sayfa sınırsız rapor üretildi. P4-04 current teslimi taşır. Önceki pause ve teyitsiz sonuç tarihsel korunur; hedefte kurulmuş sistem veya kabul edilmiş mimari yapılmaz.
