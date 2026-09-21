# Düşünce ve Model Denemeleri

**Alan:** `explorations/` — `agent/` ve `research/` ile aynı seviyede, araştırmadan ayrı çalışma kütüphanesi.

Burada kullanıcı ile assistant'ın araştırmaları ve kendi düşüncelerini kullanarak yaptığı beyin jimnastikleri, kavramsal provalar, örnek modeller, sentetik demolar ve bunların değerlendirmeleri korunur. Amaç yalnız son cümleyi değil, ona nasıl gelindiğinin görünür diyalog izini ve değişen görüşleri geri bulabilmektir.

## Okuma yolu

[CATALOG.md](CATALOG.md) → seçili paketin INDEX/STATE dosyası → konu haritası veya öğrenme kaydı → özgün konuşma, eser ve araştırma kaynağı.

Yeni paket düzeni: [PACKAGE-CONTRACT.md](PACKAGE-CONTRACT.md).

İlk paket: [EXP-001 — SOUL'un çalışma modeli](EXP-001-soul-calisma-modeli/INDEX.md).

İkinci paket: [EXP-002 — SOUL'un baz yapısı ve ortak entelektüel tabanı](EXP-002-soul-baz-yapi-ve-entelektuel-taban/INDEX.md).

Üçüncü paket: [EXP-003 — Ek hafıza ve araştırma temelli güvenilirlik](EXP-003-ek-hafiza-ve-arastirma-temelli-guvenilirlik/INDEX.md). İşlem–nesne–mekanizma ayrımları, seçici erişim, Foundation/studies kullanımı ve daha sağlam yapı hedefi; gerçekleşmiş mimari/üstünlük değil. Önceki ölçülmemiş puanlar ayrı nitelendirmelerle korunur.

Dördüncü paket: [EXP-004 — Genişleyen SOUL ve büyük-iş stress testi](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/INDEX.md). T1–T12; Mission/Work keşfi, rol→Actor, bağlam, gerçek etki, qualification/kabul, süreklilik, kontrollü uyarlama, ortak koşullar, yeni katılımın kapsamı ve gerekçeli ilerleme. [T09](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md) eşzamanlı değişimi, [T10](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md) yeni katılımı, [T11](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md) kanıt yeterliliği/araştırma maliyeti/sınırlı kapanışı, [T12](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md) roman senaryosunda yaratıcı state, exploratory draft ve ilk yazılabilir Work'ü işler. Türetilmiş notlar kaynak sayımını artırmaz. U016'nın yatay/dikey kapsama ve branch açıklaması araç/mimari kararı değildir. Aday nesneler benimsenmiş mimari sayılmaz. [STATE](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/STATE.md) güncel devamı, [onarım kaydı](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/checks/REPAIR-20260921.md) kapanmış onarımın içerik/yayın/kontrol durumunu taşır.

Birlikte okuma: [EXP-001 → EXP-002 → EXP-003 → EXP-004](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/retrieval/CUMULATIVE-READING.md). Adreslenen kesim 37 + 37 + 21 + 31 = **126 mesajdır**; sayı bağımsız kaynak sadakati garantisi değildir. EXP-004 görünür tam kaynakları ve eski yoğunlaştırılmış görünümleri ayrı bulundurur. Sonraki devam notları kaynak transkripti sayılmaz; güncel yola STATE/INDEX yönlendirir. Önceki üç paketin kaynak/aktarımı bu onarım turunda yeniden denetlenmedi. Önceki [üç-deneme yolu](EXP-003-ek-hafiza-ve-arastirma-temelli-guvenilirlik/retrieval/CUMULATIVE-READING.md) 95 mesajlık, [iki-deneme yolu](EXP-002-soul-baz-yapi-ve-entelektuel-taban/retrieval/CUMULATIVE-READING.md) 74 mesajlık kapsamıyla korunur. Konsolidasyonlar kaynak yerine geçmez; eser incelemesi diyalog okumasından ayrıdır.

## Sınırlar

- Deneme, gerçek ajan deneyi veya bilimsel doğrulama olmak zorunda değildir. Türü ve kanıt seviyesi paket içinde belirtilir.
- Konuşmada benimsenen çalışma tercihi, Foundation bulgusu ve kabul edilmiş mimari kararla aynı şey değildir.
- Buradaki yönerge örnekleri çalışma malzemesidir; `AGENT.md` yerine geçmez.
- Öğrenme, önceki konuşmayı otomatik olarak haklı çıkarma değildir. Geri çekilen görüşler ve karşı örnekler korunur.
- Yeni denemeler eski kaynakları yeniden yazmaz; yeni kimlik ve açık türetim ilişkisiyle eklenir.
- Kullanıcı bu alanı araştırma dışında özellikle yetkilendirmiştir. Candidate-study kütüphanesine sahte bir araştırma kaydı eklenmez.

## Yeniden kullanım

Bir sonraki deneme, hangi önceki kayıttan neyi devraldığını ve neyi yeniden sorguladığını belirtir. EXP-002'nin [devir haritası](EXP-002-soul-baz-yapi-ve-entelektuel-taban/sources/PREDECESSOR-EXP001.md), EXP-001 ile bu ilişkiyi kaynak seviyesinde kurar. EXP-003'ün [öncül kaydı](EXP-003-ek-hafiza-ve-arastirma-temelli-guvenilirlik/sources/PREDECESSORS.md) uzmanlık sürekliliği ve ortak entelektüel taban ile ek hafıza konuşmasını bağlar; gerçek okuma derinliğini ayrıca belirtir. EXP-004'ün [öncül kaydı](EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/sources/PREDECESSORS.md) bu zinciri büyük-iş çalışma sistemi stress testine taşır.

Araştırma ihtiyacı doğarsa araştırma ayrı yetkilendirme ve kendi paketinde yürür. Mimari benimseme de ayrı karardır. Denemelerin topluca okunması Development OS hazırlığını besleyebilir; bu okuma tek başına kurulum veya yeni araştırma yetkisi değildir. Gerçek geçişte güncel proje/target state'i ayrıca ele alınır.

Bu dosya kütüphanenin okuma ve kayıt semantiğini açıklar; yeni agent-control protokolü değildir.
