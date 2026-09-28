# EXP-006 — WORK ve master plan

**Plan:** v1.8 — 28 Eylül 2026. **Current:** P4 v4 Codex hedef ortamı raporu hazır; sıradaki ayrı aşama P5 Codex kurulum rehberidir. [STATE](STATE.md) yetkiyi, [HANDOFF](HANDOFF.md) devri, [P4-05](work/P4-05-codex-environment-revision-v4.md) güncel rapor/environment transition ve kaynak erişimini taşır.

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

**Codex hedef Environment.** D027, D011'deki Claude Code cloud kararını current açısından supersede eder. K1 talep→çalışma→yanıt→gerçek kullanım. K2 rutin rol geçişlerinde Batu'nun mesaj taşıyan/tetikleyen kişi olmaması; başlangıç/yeniden başlatma, gerçek müdahale, yetki ve kabul mümkün.

D021 içerik sahibinin anlam/gerekçeyi, çalışma alanı tarafının yer/statü/bağ/bulunabilirlik/bakım/yeniden kullanımı taşımasıdır. Düzen yalnız klasör estetiği değildir. Ürün ve çalışma bilgisi ayrı amaçlı ve ilişkilidir. Foundation gereklilik keşfini, studies uygulama/karşı örnekleri besler; kaynak talimatları etkin kontrol değildir.

Kullanıcı önce SOUL hedefinden raporun baştan yazılmasını istedi; v2 bu görevin tarihsel teslimidir. Sonra v2'nin stres testi ve sayfa sınırı olmadan yeni rapor istendi. Önceki yarım çalışma P4-03 ile devredildi; yeni oturumdaki açık devam yönüyle v3 bu tur üretildi. Rapor teslimi hazırdır; mimari veya hedef yeterliği kabul edilmiş değildir. 200 sayfa hedefi kaldırılmıştır. Gereken kalite kolaylık veya hacim lehine düşürülmez; karmaşıklık ve uzunluk da kendi başına başarı değildir.

## 3. Bütün yol

| Aşama | Esas teslimat | Durum |
|---|---|---|
| P1 — Environment gerçekliği | Kaynaklı imkân/sınır haritası ve actual hedef soruları | P1-01 Claude için tarihsel; v4 current OpenAI Codex/Agents API kaynaklarını seçici tazeler; actual Codex qualification P5'te açık |
| P2 — Roller | Amaç/yeterlik/bilgi/teslimat/yetki/tüketici sözleşmeleri | P2-01 ilk taban; P3 G/Y ve v2/v3 profilleriyle değerlendirilir; son kadro kabulü değil |
| P3 — İş/bilgi/düzen | Keşif, katkı, karar, bakım, yeniden kullanım, kesinti/devri | P3-01 v0.5 kavramsal devir; v3 bütünleşmesi gerçek canlı yeterlik değil |
| **P4 — Bütünleşik tasarım** | SOUL gereksinimlerinden mimari ve sınama programı | **V4 CODEX HEDEF ORTAMI RAPORU HAZIR.** P4-05 current; v3 mekanik tabanı korunur |
| **P5 — Gerçekleştirme** | Codex hedefinde kurulabilir runbook, actual hizmet/dosya/izin/bağlantılar | **SIRADAKİ AYRI AŞAMA: Codex kurulum rehberi.** Kurulum henüz başlamadı |
| P6 — Hedef sınaması/devir | Gerçek otomatik akış, bilgi/etki/güvence, recovery ve bilişsel kalite | Hedefte yapılmadı; yerel model testleri yerine geçmez |

P1→P2↔P3→P4→P5→P6 bağı korunur. Somut ortam/rol/anlam kusurunda ilgili aşamaya dönülür; bütün taxonomy yeniden başlatılmaz. Raporun hazır olması gerçek sistem kurulumuna otomatik yetki değildir.

## 4. P4'te değerlendirilen yapı ve sonuç

[P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) eski Claude/Git ağırlıklı baseline; [P4-02](work/P4-02-soul-derived-report-v2.md) v2 teslimi; [P4-03](work/P4-03-unbounded-stress-test-handoff.md) yarım v3 devri; [P4-04](work/P4-04-unbounded-stress-test-report-v3.md) v3 stres testi/kanıt tabanı. **[P4-05](work/P4-05-codex-environment-revision-v4.md) current'tır.**

V4, v3'ün bilişsel ekip/korunan kontrol, live state/typed relations, Git ürün/release, source/evidence, memory/context, publication/recovery ve sekiz bulgu düzeltmelerini korur. Environment bağını Codex'e değiştirir. Current P5 blueprint adayı: DevOS application/control plane + Agents API managed Codex harness + root/subagent orkestrasyonu + başlangıçta OpenAI-hosted sandbox; protected effect'ler ayrı trusted tool/broker sınırından geçer. Self-hosted ve diğer alt seçimler P5 qualification konusudur.

Codex session/subagent geçmişi canonical Work state'inin yerine geçmez. Rol sayısı subagent sayısı değildir; role, agent instance ve principal ayrımı korunur.

## 5. Bu teslimde yapılan bütünlüklü iş

1. Kullanıcının Codex Environment kararı ayrı current decision olarak alındı; D011 tarihsel tutuldu.
2. Güncel OpenAI Agents API overview/architecture, multi-agent, hosted sandbox, sandbox security, lifecycle ve session webhook belgeleri seçici incelendi.
3. V3'ün ortak mimari ve mekanik kanıtı korunup Environment/topoloji, kimlik/secret, session/recovery ve H-ENV bölümleri Codex'e göre yeniden yazıldı.
4. V3 local test tabanı v4 çalışma kopyasında yeniden koşuldu; 53 candidate test ve önceki mutation sınırı korundu. Actual Codex test edilmiş sayılmadı.
5. 31 bölümlü v4 Markdown ve 51 sayfalık PDF üretildi; 675/675 metin birimi ve görsel/layout QA geçti; v4 kaynak/kanıt ZIP'si v3 exact baseline'ı içererek paketlendi.

Bu P4 Environment revizyonudur. Agents API/openai_hosted teknik blueprint'i P5'e başlangıç sağlar fakat target qualification yerine geçmez.

## 6. Gerçek devam durumu ve kaynak erişimi

**Güncel kaynak paketi:** `EXP-006_DevOS_v4_Codex_Kaynak_ve_Kanit_Paketi.zip`, SHA-256 `df895557d77c4585627615010ac5061cde95ce768f73cfdea59259d1e5726aff`. Tam rapor/kod konuşma eklerindedir; repository P4-05 ve erişim yolunu taşır. V3 package current değil, v4 içinde provenance baseline'dır.

**Şimdi yetkilendirilmiş sonuç:** P4 v4 Codex raporunu kullanıcıya döndürmek. **Sonraki ayrı aşama:** P5 Codex kurulum rehberini hazırlamak. Bu tur P5'i uygulamaz; actual hesap/environment seçimleri rehberin ve qualification planının parçası olacaktır.

P6 veya ilk gerçek SOUL backlog'u başlatılmaz.

## 7. Değişim izi

v1.0 plan; v1.1 P1; v1.2 P2; v1.3 P3 ve G/Y/D021; v1.4 P4-01; v1.5 SOUL odaklı v2 ve P4-02.

**v1.6 / 28 Eylül 2026:** Sayfa sınırının kaldırılması, doğrulanamayan v3 teslimi, v2 baseline ve yeni oturum devri P4-03'te kaydedildi. O tur yeni mimari/test üretmedi.

**v1.7 / 28 Eylül 2026:** Yeni oturumdaki devam yönüyle v3 stres testi/rapor ve yerel kanıt teslimi P4-04'te üretildi.

**v1.8 / 28 Eylül 2026:** Kullanıcı current Environment kararını Codex'e çevirdi. Güncel OpenAI Codex/Agents API kaynaklarıyla Environment/topoloji yeniden bağlandı, v3 mekanik kanıtı regresyon için yeniden koşuldu ve P4 v4 rapor/kaynak teslimi P4-05'te üretildi. Sıradaki ayrı aşama P5 Codex kurulum rehberidir; kurulum ve P6 başlamadı.