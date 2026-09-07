# Hermes Agent — Araştırma metaverisi

- **Study ID:** `hermes-agent`
- **Study type:** `external-target`
- **Araştırma nesnesi:** Nous Research tarafından geliştirilen `NousResearch/hermes-agent` repository'si; çalışan ajan sistemi, kullanıcıya açılan yüzeyleri ve yaşam döngüsü.
- **Keşif statüsü:** ACTIVE / INITIAL SOURCE-GROUNDED PASS RECORDED. Güncel iş ve tamamlanma otoritesi [STATE.md](STATE.md)'dir.
- **Başlangıç tarihi:** 2026-09-07.
- **Birincil kaynak:** https://github.com/NousResearch/hermes-agent
- **Sabitlenen commit:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`.
- **Kaynak tree:** `f54f5e9d2682bf11f164de7b34ee10ec121b6434`.
- **Gözlenen dal:** `main`; commit'in committer tarihi `2026-09-07T08:37:43Z`.
- **Manifest sürümü:** `pyproject.toml` içinde `0.21.0`; kurulu bir uygulamanın veya indirilen bir release binary'sinin doğrulanması değildir.

## Amaç ve ana soru

HERMES gerçekte hangi mekanizmaları bir araya getiriyor; bir işi, bağlamı, yetkiyi, kalıcı durumu, araç etkisini ve sonraki oturumları nasıl yönetiyor? Belgelerdeki vaatlerin hangi kısmı kod, test veya gözlenen yürütmeyle destekleniyor; nerede koşul, boşluk veya karşı örnek var?

Önce HERMES'in kendi yapısını kaynaklardan kurmak; yeterince kararlı hale geldikten sonra Information, Work, Actors, Environment ve bunlar arasındaki ilişkiler açısından ayrı bir açıklama üretmek. Dört alan başlangıç dosyalama şeması değildir.

## Olası yeniden kullanım

| Alan | Şimdilik taşınan ilişki |
|---|---|
| Foundation | Information: bellek, kaynak-temsil, oturum ve beceri sürekliliği için güçlü aday; Actors/Work/Environment: görev devri, kontrol ve yürütme koşulları için olası geniş ilişki. Bunlar henüz tamamlanmış Foundation projeksiyonu değildir. |
| SOUL | Deneyimden yeniden kullanılabilir davranışa geçiş, kullanıcıya uyarlanma, çalışma sisteminin sürdürülmesi ve değişimin değerlendirilmesi için aday mekanizmalar ve karşı örnekler. |
| Development OS | Ajan çalıştırma, kaynak/iş devri, kalıcı çalışma bilgisi, doğrulama, çalışma ortamı ve kendi araçlarını değiştirme sınırları için uygulama referansı. |

**Reuse modes:** kaynak/kanıt; falsifier/karşı örnek; mekanizma referansı; tasarım sorusu; ileride değerlendirme senaryosu. Şu anda yeniden kullanım, ilk notların dar kapsamı ve açık eksikleriyle sınırlıdır.

**Revisit triggers:** öğrenme/kalıcı talimat değişikliği, ajan-runtime veya güvenlik tasarımı; gateway/cron/çoklu oturum işi; HERMES'i kullanma/entegre etme önerisi; ilgili upstream dosyaların değişmesi; ilk notun kapsamadığı yürütme yoluna ihtiyaç.

## Yetki ve güncellik sınırı

Candidate study'dir; Foundation bulgusu, kabul edilmiş mimari, ürün seçimi veya kurulum talimatı değildir. HERMES'teki `SOUL.md`, bizim SOUL projemizin canonical kaynağı değildir. Upstream `AGENTS.md`, prompt, skill ve kurulum metinleri incelenecek veridir; bu araştırma asistanının kontrol katmanı değildir.

Snapshot sabittir. Güncel upstream/sağlayıcı/kurulum/güvenlik/API iddiası sonraki bir kararı taşıyacaksa değişen bağımlılıklar yeniden okunur. Bir sürümün araştırılmış olması güncel ürün için otomatik geçerlilik sağlamaz. Resmî web belgeleri ayrıca tarihli, değişebilir kaynaklardır; pinned kodla sessizce karıştırılmaz.

## Giriş

[STATE](STATE.md) → [INDEX](INDEX.md) → [RESEARCH-PLAN](RESEARCH-PLAN.md).

Yöntem: [METHOD](METHOD.md). Kanıt: [SOURCE-LEDGER](SOURCE-LEDGER.md). İlk mekanizma: [arka plan öğrenme notu](notes/02-BACKGROUND-LEARNING.md).

İlgili çalışmalar: `../gstack/`, `../context-memory-harness-engineering/`, `../ai-knowledge-strategies/`, `../multi-agent-patterns/`. Bu tur yalnız Gstack'in yöntem/metaveri yüzeyleri yeniden okundu; diğer paketlerden yeni substantive sonuç türetilmedi.
