# Hermes Agent — Araştırma metaverisi

- **Study ID:** `hermes-agent`
- **Study type:** `external-target`
- **Araştırma nesnesi:** Nous Research `NousResearch/hermes-agent`; ajan sistemi, kullanıcıya açılan yüzeyleri ve yaşam döngüsü.
- **Keşif statüsü:** ACTIVE / BACKGROUND-REVIEW, SKILL-CURATION AND BOUNDED U01B COMPONENT EVIDENCE. Güncel iş/tamamlanma otoritesi [STATE.md](STATE.md)'dir. Bütün sistem araştırması tamamlanmadı.
- **Başlangıç / son kayıt tarihi:** 2026-09-07.
- **Birincil kaynak:** https://github.com/NousResearch/hermes-agent
- **Sabitlenen commit:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`.
- **Kaynak tree:** `f54f5e9d2682bf11f164de7b34ee10ec121b6434`.
- **Gözlenen dal / committer tarihi:** main / `2026-09-07T08:37:43Z`.
- **Manifest sürümü:** pyproject.toml `0.21.0`; kurulu binary veya release doğrulaması değil.
- **Freshness:** d8a077... curator ref'i ilgili aynı içeriklerle; 7874ef... U01B ref'i yalnız S01/S02/S04 blob'larıyla uzlaştırıldı. Primary pin değişmedi; tüm current upstream doğrulanmadı.

## Amaç

HERMES gerçekte hangi mekanizmaları birleştiriyor; işi, bağlamı, yetkiyi, kalıcı durumu, araç etkisini ve sonraki oturumları nasıl yönetiyor? Vaatler hangi kod, test ve gözlemle destekleniyor; koşullar ve karşı örnekler nerede?

Önce HERMES-native model; sonra Information, Work, Actors, Environment ve aralarındaki ilişkiler için ayrı açıklama. Dört alan başlangıç dosyalama kalıbı değildir.

## Olası yeniden kullanım

| Alan | Provisional ilişki |
|---|---|
| Foundation | Information: bellek/kaynak-temsil/oturum/beceri sürekliliği güçlü aday. Work/Actors/Environment ve relations/control: yetki, onay, mutation/rollback ve caller/runtime sınırları için olası geniş ilişki. Tamamlanmış projeksiyon değil. |
| SOUL | Deneyimden yeniden kullanılabilir davranışa geçiş, uyarlanma, çalışma sistemini sürdürme ve değişim kalitesi için mekanizma/karşı örnek. |
| Development OS | Ajan çalıştırma, kaynak/iş devri, kalıcı bilgi, doğrulama ve araçlarını değiştirme sınırları için uygulama referansı. |

**Reuse modes:** evidence/reference; falsifier/karşı örnek; mekanizma öğrenimi; design pressure; aday test senaryosu. Policy≠provenance, usage≠quality, approval preview≠applied operation, filesystem rollback≠all-effects rollback ve record ID≠durability ayrımları mevcut notlarda farklı kanıt güçleriyle incelenir.

**Revisit triggers:** öğrenme/kalıcı talimat veya runtime güvenliği tasarımı; skill onay/birleştirme/rollback; session/cron/gateway/caller varyantı; HERMES kullanma/entegrasyon önerisi; ilgili upstream değişimi; candidate bulgunun load-bearing tasarım girdisine yükselmesi.

## Yetki ve kanıt sınırı

Candidate study'dir; Foundation truth, kabul edilmiş mimari, ürün seçimi veya kurulum yetkisi değildir. HERMES'teki SOUL.md bizim SOUL projemizin kaynağı değildir; upstream AGENTS/skills/prompts bu asistanın kontrolü değil araştırma nesnesidir.

İlk review/curator turları statik; U01B iki exact modülün sentetik bağımlılıklı bileşen deneyi. Tüm uygulama, gerçek kullanıcı profili, provider, upstream suite veya bağımsız araştırmacı doğrulaması yoktur. U01B aktarımında eski koşu yeniden yapılmadı. Kaynak değiştiğinde current API/security/provider/install iddiaları yeniden doğrulanır; tarihli web görünümü pinned kodla karıştırılmaz.

## Girişler

[STATE](STATE.md) → [INDEX](INDEX.md) → [RESEARCH-PLAN](RESEARCH-PLAN.md). Yöntem: [METHOD](METHOD.md). Kanıt rotası: [SOURCE-LEDGER](SOURCE-LEDGER.md).

Mekanizmalar: [02 review](notes/02-BACKGROUND-LEARNING.md), [03 curator](notes/03-SKILL-CURATION.md), [04 onay/mutasyon](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md). [U01B kanıtı](evidence/2026-09-07-u01b/component-probe/README.md) ve [aktarım kaydı](evidence/2026-09-07-u01b/PUBLICATION.md).

İlgili çalışmalar: ../gstack, ../context-memory-harness-engineering, ../ai-knowledge-strategies, ../multi-agent-patterns. Bunlar seçici reuse adaylarıdır; varlıkları otomatik içerik yükleme veya adoption anlamına gelmez. OpenClaw ayrı sonraki çalışma adayı olarak kalır.
