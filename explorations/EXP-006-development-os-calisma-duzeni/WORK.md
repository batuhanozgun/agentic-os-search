# EXP-006 — WORK ve master plan

**Plan:** v1.5 — 27 Eylül 2026. **Current:** P4 / SOUL odaklı 200 sayfalık rapor v2 hazır; yeni mimari öneri, hedefte kurulmadı. [STATE](STATE.md) current yetkiyi, [HANDOFF](HANDOFF.md) devri, [P4-02](work/P4-02-soul-derived-report-v2.md) teslimat kimliği/kanıtını taşır.

**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak. Bu plan SOUL'un teknik backlog'u değildir; ilk ve sonraki gerçek SOUL işlerini kurulacak ekip keşfeder.

## 1. Korunan zemin

SOUL hedefi → DevOS'un yapacağı işler → kabiliyet/sorumluluk → rol/mekanik/insan sınırı → S1 → P1–P6.

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

B1–B9 geliştirme sırası veya SOUL modül listesi değildir. [S1](work/S1-role-responsibility-consolidation.md), [S1-17](work/S1-17-consolidation-closure-audit.md) ve [ACTORS](ACTORS.md) ilk R/M ve F1–F8/DR lineage'ını taşır. Rol sayısı actor sayısı değildir. S1-16 kaynak-tamlığı qualification'ı S1-17 §7'de korunur.

## 2. Değişmeyen gereksinimler

Claude Code cloud hedef Environment'dır. K1, talep→rolün çalışması→yanıt→gerçek kullanımdır. K2, rutin rol geçişlerinde Batu'nun mesaj taşıyan/tetikleyen kişi olmamasıdır; başlangıç, yeniden başlatma, gerçek müdahale ve yetki/kabul mümkündür.

D021, içerik sahibinin anlam/gerekçeyi; düzen tarafının yer/statü/bağ/bulunabilirlik/bakım/yeniden kullanımı taşımasıdır. Düzen yalnız görsel klasör temizliği değildir. Ürün ve çalışma bilgisi ayrı amaçlı fakat ilişkilidir. Foundation gereklilik keşfini, studies uygulama/karşı örnekleri besler; kaynak talimatları etkin DevOS kontrolü değildir. Kabul edilmiş sınırlar [DECISIONS](DECISIONS.md) ve [U002](sources/U002-cloud-plan-and-autonomy.md)'dedir.

**Yeni teslimat yönü:** Kullanıcı eski raporu küçük eklerle düzeltmek yerine SOUL'un niteliğinden başlayarak baştan yeniden yazmayı istedi. Gerekli kalite kolay uygulama lehine düşürülemez; sırf karmaşık bir çözüm de üstün sayılmaz. Yeni raporun tamamlanması teknik tercihlerinin kullanıcı kabulü değildir.

## 3. Bütün yol

| Aşama | Esas teslimat | Durum |
|---|---|---|
| P1 — Claude gerçekliği | Kaynaklı imkân/sınır haritası; actual kip/araç/erişim testleri | [P1-01](work/P1-01-claude-cloud-environment-map.md) kaynak sonucu var; hedef kanıtı açık. V2 gerekli kaynakları tazeler. |
| P2 — Roller | Amaç, yeterlik, bilgi, teslimat, yetki ve tüketici sözleşmeleri | [P2-01](work/P2-01-named-role-contracts.md) ilk taban; P3 G/Y ve v2 hedef profilleriyle birlikte değerlendirilir. |
| P3 — İş/bilgi/düzen | Keşif, katkı, karar, bakım, yeniden kullanım, kesinti ve devir | [P3-01](work/P3-01-work-information-discussion.md) v0.5 kavramsal devir; canlı yeterlik değil. |
| P4 — Bütünleşik tasarım | Gerçek çalışma biçimi, veri otoritesi, graph/context/harness, yayın, yetki ve hedef kabul programı | **AKTİF / RAPOR v2 TESLİMATA HAZIR / ÖNERİ.** [P4-02](work/P4-02-soul-derived-report-v2.md); tam ayrıntı konuşmadaki PDF/kaynak ZIP. |
| P5 — Gerçekleştirme | Onaylanan mimarinin actual hizmet, dosya, izin ve bağlantıları | DevOS kurulumu başlamadı. Referans model üretim sistemi değildir. |
| P6 — Hedef sınaması/devir | Gerçek otomatik akış, bilgi/etki/güvence, recovery ve bilişsel kalite | Hedefte yapılmadı. V2 s.177–190 programı aday uygulama/kabul yoludur. |

P1→P2↔P3→P4→P5→P6 bağlantısı korunur. Somut ortam/rol/anlam kusurunda ilgili aşamaya hedefli dönülür; genel audit döngüsü veya taxonomy yeniden başlatılmaz.

## 4. V2'nin tasarım farkı

[Eski P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) alt-ajan/Git ağırlıklı ilk baseline olarak korunur; current seçim değildir. V2, SOUL'un keşif, sistem oluşturma, entelektüel süreklilik, uzun eser ve yöntem aktarımı yüklerinden yeniden türetilmiştir.

Yeni öneri: takım ağırlıklı Claude işbirliği + korunan mekanik kontrol; PostgreSQL canlı durum/typed graph; Git ürün ve release içerikleri; hash'li kanıt; hybrid retrieval/context compiler; ayrı publisher; outbox/inbox, read-set/revision ve generation/fencing; DB–Git uzlaştırması. Bu ayrımlar birinci sınıf tasarımdır, ileride belki eklenecek etiketler değildir.

G/Y içerik/iş koordinasyonu ile yapı koordinasyonu ayrılır. Shared runtime agent adları ayrı güvenlik principal'ı sayılmaz. Etki sorgusu otomatik doğruluk hükmü vermez. Sekizli aile veya 18 hedef profili fiziksel kadro sayısı değildir.

**Kanıt:** 40 yerel Python/SQLite testi, dört hedefli guard kaldırma kontrolü; same-author sınırlı gözlem. PostgreSQL/Claude/gerçek auth/yayın/sandbox/restore veya bilişsel kalite gösterilmedi. 200 sayfa PDF düzen/kaynak/link kontrolleri ayrı yapıldı. Ayrıntılı iz P4-02 ve kaynak ZIP içindedir.

## 5. Kaynak erişimi ve devam

PDF/ZIP tam gövdeleri konuşma eklerindedir, repository'ye yüklenmedi. P4-02 isim/hash, mimari fark ve kanıt sınırını taşır. Yeni oturum tam rapor işi için gerçek v2 eki recover etmeli; yoksa istemeli. Repository özetinden 200 sayfa okunmuş gibi devam edilmez.

**Bu turun dönüşü:** Yeniden yazılmış PDF ve kaynak paketini teslim etmek. **Sonraki mantıksal iş:** Kullanıcı değerlendirmesinin ardından v2 uygulama/qualification programını gerçek hedef koşullarına bağlamak. P5 yetkisi veya yeni mimari kabulü varsayılmaz.

Foundation [REUSE](../../research/soul-foundations/08_foundation-sufficiency-reuse-review/REUSE.md), [Studies CATALOG](../../research/studies/CATALOG.md), EXP-002/004 SOUL hedefi ve ilgili kaynaklar kararın gerektirdiği derinlikte okunur. Tüm literatür her tur körlemesine yüklenmez; yüzeysel arama da gerekli tam bağlamı ikame etmez.

## 6. Değişim izi

v1.0 plan; v1.1 P1; v1.2 P2; v1.3 P3 ve G/Y/D021; v1.4 P4-01 ilk teknik tercih; **v1.5 yeni 200 sayfalık SOUL odaklı yazım ve P4-02 teslimat/devralma kaydı**. Önceki planın tam ayrıntısı `e3856a4` kesitindeki WORK.md'de korunur. Bu revizyon başka çalışma paketi veya yeni üst amaç açmaz.
