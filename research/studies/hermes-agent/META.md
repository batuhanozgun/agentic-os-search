# Hermes Agent — Araştırma metaverisi

- **Study ID:** `hermes-agent`
- **Study type:** `external-target`
- **Araştırma nesnesi:** Nous Research `NousResearch/hermes-agent`; ajan sistemi, kullanıcıya açılan yüzeyleri ve yaşam döngüsü.
- **Keşif statüsü:** ACTIVE / PINNED PARTIAL CALLER-MEMORY ANALYSIS + SEPARATE BOUNDED RECORDS + RECOVERED U01-D2 SOURCE-SELECTED INTEGRATION. Güncel iş/tamamlanma otoritesi [STATE.md](STATE.md)'dir. Bütün sistem araştırması tamamlanmadı.
- **Başlangıç / son kayıt tarihi:** 2026-09-07 / 2026-09-09. Son tarih, 2026-09-08 worker-policy deneyinin yayın/continuity tarihidir; yeni deney değildir.
- **Birincil kaynak:** https://github.com/NousResearch/hermes-agent
- **Sabitlenen commit:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`.
- **Kaynak tree:** `f54f5e9d2682bf11f164de7b34ee10ec121b6434`.
- **Gözlenen dal / committer tarihi:** main / `2026-09-07T08:37:43Z`.
- **Manifest sürümü:** pyproject.toml `0.21.0`; kurulu binary veya release doğrulaması değil.
- **Freshness:** d8a077... curator ref'i ilgili aynı içeriklerle; 7874ef... U01B ref'i yalnız S01/S02/S04 blob'larıyla uzlaştırıldı. Primary pin değişmedi. W01–W08 web belgeleri pin'e bağlanmadı. D/E kaynakları primary'ye bağlı; E01/E02 yerel deneyde tam modüller değil manuel seçkilerdir. U01B2 arşivdeki aynı S02/S04 içeriklerini kullanır. Son yayın current upstream HEAD veya bağımlılık tazeliği doğrulaması değildir.

## Amaç

HERMES gerçekte hangi mekanizmaları birleştiriyor; işi, bağlamı, yetkiyi, kalıcı durumu, araç etkisini ve sonraki oturumları nasıl yönetiyor? Vaatler hangi kod, test ve gözlemle destekleniyor; koşullar ve karşı örnekler nerede?

Önce HERMES-native model; sonra Information, Work, Actors, Environment ve aralarındaki ilişkiler için ayrı açıklama. Dört alan başlangıç dosyalama kalıbı değildir.

## Olası yeniden kullanım

| Alan | Provisional ilişki |
|---|---|
| Foundation | Information: bellek/kaynak-temsil/oturum/beceri sürekliliği güçlü aday. Work/Actors/Environment ve relations/control: çağrı kabulü, yetki/policy aktarımı, onay, effect/persistence/delivery ve rollback sınırları için olası geniş ilişki. Tamamlanmış projeksiyon değil. |
| SOUL | Deneyimden yeniden kullanılabilir davranışa geçiş, uyarlanma, çalışma sistemini sürdürme ve değişim kalitesi için mekanizma/karşı örnek. |
| Development OS | Ajan çalıştırma, kaynak/iş devri, kalıcı bilgi, kontrol durumunun worker'a taşınması, hata/kalıcılık/readback ve araçlarını değiştirme sınırları için uygulama referansı. |

**Reuse modes:** evidence/reference; falsifier/karşı örnek; mekanizma öğrenimi; design pressure; aday test senaryosu. Policy≠provenance, usage≠quality, approval preview≠applied operation, filesystem rollback≠all-effects rollback, record ID≠durability, ContextVar transfer≠all control-state transfer, live store≠prompt snapshot ayrımları farklı kanıt güçleriyle incelenir. 08/U01B2, default-name/serialized-payload, canlı önizlem/hedef-sürümü ve rollback/başka-yazar izolasyonu ayrımlarını ekler. 09/U01-D2: geçerli araç-adı≠dar görev yetkisi; policy'nin varlığı≠worker'da aynı state; callback kabulü/`dispatched`≠gerçek handler etkisi.

**Revisit triggers:** öğrenme/kalıcı talimat veya runtime güvenliği tasarımı; thread/worker/middleware değişimi; callback/effect ölçümü; skill onay/birleştirme/rollback; session/cron/gateway/caller varyantı; HERMES kullanma/entegrasyon önerisi; ilgili upstream değişimi; candidate bulgunun load-bearing tasarım girdisine yükselmesi.

## Yetki ve kanıt sınırı

Candidate study'dir; Foundation truth, kabul edilmiş mimari, ürün seçimi veya kurulum yetkisi değildir. HERMES'teki SOUL.md bizim SOUL projemizin kaynağı değildir; upstream AGENTS/skills/prompts bu asistanın kontrolü değil araştırma nesnesidir.

İlk review/curator turları statik. U01B iki exact modül + sentetik bağımlılıklarla 10 durum; transport üç başka exact modül + sentetik callback/profil/allowlist ile 7 durum; U01B2 arşiv S02/S04 + sentetik adapter/reentry/config/guard/mutator ile 12 senaryodur. G01 içindeki 10 varyant ürün testi toplamı değildir.

**U01-D2 ayrı kapsamdır:** C01–C14 tam pool/context modülleri ile elle aktarılmış büyük executor/plugins seçkilerini birleştirir; V01–V05 tam name-validator'ı ekler. Gerçek AIAgent/review kurulumu, valid-name kümesinin gerçek üretimi, tam executor/PluginManager/middleware veya alternatif caller zinciri çalıştırılmadı. Diğer sınırlar E defterinde açıktır. Gerçek kaynak-kimliği ret kontrolü ayrı kayıttır; seçki AST eşitliği kontrolü NOT RUN. U01-D2'nin 2026-09-09 aktarımında hiçbir deney yeniden çalıştırılmadı.

Bu deneyler toplanarak ürün PASS sayısı üretilmez. Tam uygulama, gerçek profil, provider, upstream suite, current HEAD ve bağımsız araştırmacı doğrulaması yoktur. Kontrol bağlamı süreksizliği, memory failure/alias ve caller-izolasyon adayları genel ürün kusuru veya gerçekleşmiş güvenlik olayı diye aktarılmamalıdır.

Sonraki ilk iş, tam pinned E01/E02 içerikleriyle seçki sadakati ve ardından gerçek review/worker erişilebilirliğidir. Devamın otoritesi plan v0.7/STATE'tir. Kaynak değiştiğinde current API/security/provider/install iddiaları yeniden doğrulanır; geçmiş 429 veya write-tool hataları kalıcı erişim hükmü değildir. Yayın başarısı gelecekteki tool kullanılabilirliğine garanti vermez.

## Girişler

[STATE](STATE.md) → [INDEX](INDEX.md) → [RESEARCH-PLAN](RESEARCH-PLAN.md). Yöntem [METHOD](METHOD.md); kanıt rotası [SOURCE-LEDGER](SOURCE-LEDGER.md).

[02 review](notes/02-BACKGROUND-LEARNING.md), [03 curator](notes/03-SKILL-CURATION.md), [04 onay/mutasyon](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [05 belge kontratları](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md), [06 caller/aktarım](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [07 memory/replay](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md), [08 U01B2](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), **[09 worker-policy](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md)**.

[U01B kanıtı](evidence/2026-09-07-u01b/component-probe/README.md), [U01B aktarımı](evidence/2026-09-07-u01b/PUBLICATION.md), [W01–W08](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md), [D kaynakları](evidence/2026-09-08-context-transfer/SOURCES.md), [transport probe](evidence/2026-09-08-context-transfer/README.md), [U01B2](evidence/2026-09-08-u01b2/README.md), [U01B2 yayını](evidence/2026-09-08-u01b2/PUBLICATION.md), [E kaynakları](evidence/2026-09-08-worker-policy/SOURCES.md), [worker-policy yayını](evidence/2026-09-08-worker-policy/PUBLICATION.md).

Özgün teslimlerin NOT PUBLISHED/NOT APPLIED ifadeleri tarihsel metindir; ilgili PUBLICATION ve current STATE ile okunur. Önceki notlar/kanıtlar korunur. İlgili çalışmalar: ../gstack, ../context-memory-harness-engineering, ../ai-knowledge-strategies, ../multi-agent-patterns. Bunlar seçici reuse adaylarıdır; otomatik içerik yükleme veya adoption değildir. OpenClaw ayrı aday olarak kalır.
