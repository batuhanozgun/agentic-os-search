# EXP-007 — DECISIONS

**Rol:** Batu'nun bu pakette verdiği kararları ve koyduğu gereksinimleri, kaynak mesajına bağlı olarak tutmak. Açık soruları kararlardan ayırmak.  
**Güncelleme:** 27 Eylül 2026.  
**Kural:** Bir karar yalnız Batu'nun sözüne dayanır; kaynak mesaj birebir `sources/conversation/` altındadır. Claude'un tasarım kararları buraya değil, ilgili aşama dosyasına gerekçesiyle yazılır.

## Kararlar ve gereksinimler

| ID | Karar / gereksinim | Kaynak | Durum |
|---|---|---|---|
| K-001 | Devralmanın amacı: EXP-006'daki işi Claude'un alt ajanlarıyla, Batu her turda "devam" yazmadan, uzun soluklu yürütebilecek bir ortamda sürdürmek. | [U002](sources/conversation/U002.md) | Yön; geçerli |
| K-002 | **Sürekli yetki onaylandı.** Onaylanan metin A002'deki öneridir: P1→P2↔P3→P4 geçişleri kendiliğinden olur; P4'te tasarım kabulü için durulur; kapsam değişikliği, yeni erişim ve Claude'un cevaplayamadığı tercih soruları Batu'ya gelir; sorular birikir, iş durmaz. | [U003](sources/conversation/U003.md) madde 1 → [A002](sources/conversation/A002.md) | Onaylı; P1 başlayınca işler (P1 henüz başlamadı) |
| K-003 | Main'e birleştirmeyi Claude yapar. Birleşen dal silinir; dallar birikmez. | [U003](sources/conversation/U003.md) madde 2 | Onaylı; uygulanıyor |
| K-004 | Çalışma EXP-007'de sürer. Claude, ChatGPT ile yürütülen sürecin üzerinden geçip kendi yapısını kurar. EXP-006'daki ChatGPT dönemi dosyaları Claude'da kaymaya yol açmamalı. | [U003](sources/conversation/U003.md) madde 3 | Onaylı |
| K-005 | U003 "başla" değildir. Önce EXP-006'nın amacı, niyeti, düşünme ve değerlendirme yaklaşımları anlaşılmalı; nasıl çalışılacağı (alt ajanların nasıl düşüneceği, repodan nasıl yararlanacağı, Foundation ve studies'e ne zaman ve nasıl başvuracağı, planın nasıl yönetilip revize edileceği vb.) net biçimde ortaya konmadan başlanmaz. | [U003](sources/conversation/U003.md) | Geçerli |
| K-006 | Claude'un EXP-006 anlayışı ([A003](sources/conversation/A003.md) §1) doğru bulundu. | [U004](sources/conversation/U004.md) | Onaylı |
| K-007 | **A003'teki yapı küçük, yani bu işi yönetebilecek kapsamda değil.** Gereksinimler: bağlam (context) yönetimi; bellek (memory) yönetimi; alt ajanlar için kalıcı rol yapısı (her seferinde yeniden rol biçmek doğru değil); en iyi uygulamalara (best practice) dayalı metodoloji; A003'te söylenenlerin hepsinin **nasıl** yapılacağının ortaya dökülmesi. Seviye "yeterli seviye" değil **standart seviye** olmalı. Bütünsel bakılmalı: bir alanda yeterli görünen seçim, diğer mekanizmaları yetersizleştirebilir. Studies farklı arabalardır, Foundation ayrıntılı araştırmadır; bu işi dünyada ilk kez kuran biz değiliz. | [U004](sources/conversation/U004.md) | Gereksinim; P0'ın ölçütü |
| K-008 | EXP-007 altında Claude'un kendi süreklilik kaydını tutma izni; amaç, bağlam dolarsa ya da yeni bir konuşmaya geçilirse tartışmanın kaldığı yerden sürmesi. | [U004](sources/conversation/U004.md) | Onaylı; bu kayıtla uygulandı |

## Açık sorular — karar değildir

| ID | Soru | Nereden | Claude'un şimdiki varsayımı |
|---|---|---|---|
| A-01 | AGENT.md ve `agent/protocols/` kontrol katmanı olarak kalıyor mu? | [A003](sources/conversation/A003.md) §7 soru 2; cevaplanmadı | Kalıyor. K-004'teki "ChatGPT dosyaları" EXP-006'nın içini kastediyor. ChatGPT'ye özgü kısımların Claude'a uyarlanması ayrı bir öneri olarak getirilecek. |
| A-02 | P0'da, metodoloji yazılmadan önce konuşma içinde iki pilot yapılması (Batu'nun concepts'teki yöntemi) uygun mu? | A003 §5 ve §7 soru 3; cevaplanmadı | Metodoloji taslağı Batu'ya sunulurken yeniden sorulacak. |
| A-03 | ChatGPT'nin rolü: tamamen bırakılıyor mu, aşama sonlarında eleştirmen olarak kalıyor mu? | [A001](sources/conversation/A001.md) soru 2; doğrudan cevaplanmadı | K-004 işi Claude'a veriyor; eleştirmen rolü açık. |
| A-04 | Kontrol ve yapılandırma değişiklikleri: kök CLAUDE.md, `.claude/agents/` (kalıcı roller), `.claude/skills/`, `.claude/settings.json` hook'ları, AGENT.md'nin Claude'a uyarlanması. | A001, A002, A003; K-007 kalıcı rol gereksinimi | Metodoloji taslağıyla tek paket halinde önerilecek; Batu onaylamadan kurulmaz. |
| A-05 | Kök README ve `development-os/INDEX.md` hâlâ DEVOS-002'yi güncel iş gösteriyor; `explorations/INDEX.md` EXP-006'yı ve EXP-007'yi anmıyor. | A001; EXP-007 açılışı | Başlangıçta (P0 sonu) düzeltilecek; şimdilik yalnız `explorations/CATALOG.md`'ye EXP-007 satırı eklendi. |
