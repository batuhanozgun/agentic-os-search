# Concepts — Güncel Durum

**Kayıt tarihi:** 2026-09-18.
**Faz:** repository hazırlığı; terim araştırması değil.
**Yayın durumu:** HAZIRLANIYOR — `setup/concepts-reference-20260918` branch'i; main yayını ve geri okuma henüz tamamlanmadı.
**Başlangıç main:** `3d93615ae51e4e85cd509e49f65b4c2afbad07c0`.

## Amaç ve yetki

Kullanıcı, kavramları SOUL'un henüz seçilmemiş yapısından türetmeden araştırma → birlikte değerlendirme → ortak referans programını kabul etti. İletişimde aynı kelimeyle farklı şeyleri anlayıp onay/ret verme riskini azaltmak amaçtır; sözcük yasağı veya yeni mimari katmanı kurmak değil.

Onaylanan mevcut iş: [PLAN](PLAN.md) içindeki 11 yeni dosya ve 7 sınırlı mevcut dosya değişikliği; eşzamanlı araştırmaları koruyan ayrı branch, kapsam kontrolü, main yayını ve geri okuma. Agent-control içinde yalnız `agent/protocols/candidate-research-library.md` yerleştirme/geri çağırma eki yetkilidir. AGENT.md, diğer protokoller, araştırma sonuçları ve hedef repository'ler bu işin dışında.

Kullanıcının bu hazırlığa verdiği son devam yönü: “anlaştık. hazırsan başla”. Bu, terim tanımlarının kabulü veya bütün araştırma listesini çalıştırma yetkisi değildir. Konuşma gerekçesi ve seçili kaynak ifadeler [PURPOSE](PURPOSE.md) içindedir.

## Durum ayrımları

| İş/sonuç | Durum |
|---|---|
| Amaç, üç seviye ve hazırlık kapsamı | Kullanıcı tarafından kabul edilmiş çalışma yönü. |
| Başlangıç terim gündemi | Kaynaklı başlangıç listesi; eksiksiz repository taraması değil. |
| Alanın dosyaları ve giriş bağlantıları | Hazırlanıyor; gerçek kontroller checks kaydında. |
| Agent terim araştırması | BAŞLAMADI. BRIEF yalnız kapsam hazırlığıdır. |
| Diğer terim araştırmaları | BAŞLAMADI; gündem olmak etkin iş olmak değildir. |
| İkinci seviye sentez | Yok. |
| Üçüncü seviye ortak referans kaydı | Yok; kabul edilmiş tanım bulunmuyor. |
| SOUL/Development OS mimari veya uygulama kararı | Bu programdan doğan karar yok. |

## Sonraki sorumluluk ve durma noktası

Assistant'ın mevcut sorumluluğu hazırlığı tamamlamak, onaylı 18 yolun dışına çıkılmadığını ve ortak dosyalardaki diğer kayıtların korunduğunu kontrol etmek, main yayınını doğrulamak ve kullanıcıya sonucu bildirmektir. Diğer oturumların çalışmalarını üstlenmez; branch sayısı hedefi veya genel branch temizliği yoktur.

Hazırlık bittiğinde dur. Kullanıcının araştırmaya yeni devam yönüyle ilk çalışma [research/agent/BRIEF.md](research/agent/BRIEF.md) üzerinden başlar; hazırlık planı yeniden icat edilmez. Belirsiz “devam” talebinde STATE, kullanıcının güncel yönü ve gerçek yayın durumu birlikte okunur.

Seviye 3'e kayıt için assistant'ın kaynaklı değerlendirmesi ile kullanıcının belirli kullanım/kapsama dair açık değerlendirmesi görünür olmalıdır. Genel memnuniyet veya plan onayı terim kabulüne çevrilmez. Tekrar edilme bağımsız doğrulama değildir.

## Yeni oturumda devam

[INDEX](INDEX.md) → bu STATE → [PURPOSE](PURPOSE.md) → [METHOD](METHOD.md) → [PLAN](PLAN.md) → ilgili [TERM-INVENTORY](TERM-INVENTORY.md) kaydı → etkin çalışmanın brief'i. İlk kurulum kontrolü için [SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md).

Main canonical birleşik kaynak olarak kalır. Branch hazırlığı main yayını sayılmaz. Yayın tamamlanmadan oturum kesilirse branch'in gerçek içeriğini ve main farkını geri kazan; yalnız bu kayda dayanarak yapılmamış kontrolleri yapılmış sayma. Kontrolü geçen tarihli snapshot da sonradan değişmiş bir main için otomatik garanti değildir.
