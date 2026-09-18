# Concepts — Güncel Durum

**Kayıt tarihi:** 2026-09-18.
**Faz:** P1 / seviye 1; Agent araştırması başladı. U01 ilk sınırlı dilim hazır; araştırmanın bütünü tamamlanmadı.
**U01 yayın durumu:** MAIN ÜZERİNDE YAYIMLANDI; PR #19 birleşti, U01 ve STATE geri okundu. Yayın kimlikleri ve kontrol sınırları aşağıdadır. P0 hazırlığının tamamlanmış yayını ayrı ve korunuyor.
**Mevcut araştırma çıktısı:** [Agent U01 — kaynak kullanımları](research/agent/U01-SOURCE-USES.md).
**Dönüş noktası:** İlk kaynaklı kullanımları, somut farkları ve açık soruları kullanıcıya sunmak; ortak tanım veya tasarıma geçmemek.

## Amaç ve güncel yetki

Amaç, aynı sözcükle farklı şeylerin anlaşılmasını görünür kılacak araştırma → birlikte değerlendirme → ortak referans programıdır. SOUL'un henüz seçilmemiş yapısı terim tanımının ölçütü değildir; sözcük yasağı veya yeni mimari katmanı kurulmaz.

2026-09-18 tarihli yeni kullanıcı yönü: “Kavram çalışmasına devam et. Güncel `main` üzerinden `AGENT.md` ve gerekli protokolleri oku; ardından `concepts/INDEX.md` ve `STATE.md` içindeki devam yolunu izle. Hazırlığı tekrarlama. Agent teriminin farklı kaynaklardaki kullanımlarını araştırmaya başla; henüz ortak tanım veya SOUL tasarım kararı oluşturma.”

Bu yön P1 Agent araştırmasını açtı; P0 hazırlık yetkisinden otomatik geçiş yapılmadı. Bu turdaki yetki, ilk anlamlı sınırlı kaynak incelemesini ve bunun kayıt/yayın sürekliliğini kapsar. Bütün envanterin araştırılması, ortak kullanım kabulü veya tasarım yetkisi değildir.

## Durum ayrımları

| İş/sonuç | Durum |
|---|---|
| Amaç, üç seviye ve hazırlık kapsamı | Kullanıcı tarafından kabul edilmiş çalışma yönü. |
| P0 alan dosyaları ve giriş yolu | TAMAMLANDI; PR #12 ve tarihli SETUP-VERIFICATION kaydı korunuyor. |
| Agent terim araştırması | BAŞLADI / KISMİ; U01 ilk kaynaklı kullanım incelemesi hazır. |
| U01 kanıtı | Kaynak açıklamaları ve ayrılmış yorumlar; tam literatür taraması veya runtime testi değil. |
| Kullanıcının U01 bulgularını değerlendirmesi | Henüz kaydedilmedi; bu tur sonundaki sunum değerlendirme yerine geçmez. |
| Diğer terim araştırmaları | BAŞLAMADI; U01'deki gerekli komşu ayrımları ayrı araştırma yetkisi değildir. |
| İkinci seviye sentez | Yok; U01 içindeki kaynak karşılaştırmaları tekil Agent araştırmasının parçasıdır. |
| Üçüncü seviye ortak referans | Yok; kabul edilmiş tanım bulunmuyor. |
| SOUL/Development OS mimari veya uygulama kararı | Bu programdan doğan karar yok. |

## Yeni oturumda devam yolu

Güncel AGENT ve gereken protokoller → [INDEX](INDEX.md) → bu STATE → [PURPOSE](PURPOSE.md) → [METHOD](METHOD.md) → [PLAN](PLAN.md) → ilgili [TERM-INVENTORY](TERM-INVENTORY.md) kaydı → [Agent BRIEF](research/agent/BRIEF.md) → [U01](research/agent/U01-SOURCE-USES.md).

P0'ı veya U01'deki ilk kaynak taramasını yapılmamış iş sanma. U01'de kaynak, bölüm, tarih, gerçek okuma derinliği, örnek, yorum ve açık soru birlikte kayıtlıdır. Canlı belge okumalarını değişmez sürüm ya da çalıştırılmış teknik doğrulama sayma.

**Sıradaki mantıklı araştırma:** U01'in açık bıraktığı “Agent oluşturmak” ifadesini yapılandırma, çalıştırma ve daha kalıcı yürütme birimi ayrımlarıyla birkaç somut kaynak üzerinden derinleştirmek. S3'teki dinamik workflow/Agent kontrol sınırı da açık kalır; bütün komşu terimler aynı anda açılmaz.

**Mevcut dönüş işi:** Yayın ve geri okuma tamamlandı; U01 sonucunu kullanıcıya sunmak. Bu dönüşten sonraki yeni dilim kullanıcı devam yönüyle açılır; burada aday gösterilmesi yeni aşama yetkisi değildir. Ortak tanım veya tasarım yetkisi yoktur.

Kullanıcı araştırma yönünü ve ortak kullanım değerlendirmesini taşır; assistant yetkili araştırmayı, kaynak doğruluğunu, kayıt ve yayın tutarlılığını yürütür. Seviye 3 için belirli açıklama/kapsam, assistant'ın gerekçeli önerisi ve kullanıcının o açıklamaya dair açık değerlendirmesi görünür olmalıdır. Genel memnuniyet veya plan onayı terim kabulüne çevrilmez.

## U01 kapsamı ve gerçekleşen yayın

Kontrol ve proje başlangıç okumaları main `0743feae8728faebb48982ec22c447b06f2a0eaa` üzerinden yapıldı. Yayın hazırlığında main `a3c208905560e0f998c0af019b235825a276969e` oldu; karşılaştırma yalnız ECC `ROUND-U08-A.md` ekini gösterdi. U01 bu güncel tabanı korudu.

Yazma kapsamı beş yoldur: yeni `concepts/research/agent/U01-SOURCE-USES.md`; mevcut Agent BRIEF, seviye 1 INDEX, TERM-INVENTORY ve bu STATE. BRIEF kapsamı ve envanter listesi yeniden yazılmadı; bu üç giriş/envanter dosyasında yalnız birer giriş/durum satırı değişti. Agent-control, Foundation, studies, explorations, publications, ortak referans ve sentez dosyaları değiştirilmedi.

**Yayın:** [PR #19](https://github.com/batuhanozgun/agentic-os-search/pull/19), çalışma branch'i `research/concepts-agent-u01-20260918`, exact head `75179c8fd73411a0be8c5ac2b379ec47197c5afb`, main merge commit `2a3eeb1fe0853b408d07c1fbd83828e33439efbf`. Normal merge kullanıldı; force veya başka oturumun branch'ine yazma yok. Branch artık bekleyen araştırma yayını veya alternatif current state değildir; main canonical kaynaktır.

**Gerçekleşen kontroller:** PR diff'i tam okunarak beş yol kapsamı, mevcut üç küçük dosyada tek-satır değişimi ve yeni kaynak kaydı kontrol edildi. Merge öncesi PR head/base yeniden okundu. Yayın head'i ile merge commit'i karşılaştırması sıfır dosya farkı verdi; incelenen içerik ve eşzamanlı ECC tabanı korundu. Main üzerinden U01'in 1–48 ve 49–92 satırları ile STATE tam geri okundu; U01 blob kimliği `22f04d1c120afa91781f680af32bf3b5944c3d30`. Yeni devam bağlantıları yayımlanan U01'e yöneliyor. Bu kayıt, gerçekleşmiş yayını STATE'e işleyen kapanıştır; yeni araştırma sonucu eklemez.

Bunlar kapsam, içerik aktarımı ve çalışma sürekliliği kontrolleridir; bağımsız bilimsel doğrulama, kod yürütme testi, bütün repository için link taraması veya gelecekteki iletişim kalitesinin kanıtı değildir. Kullanıcının elle upload veya merge yapması gerekmiyor.

## Korunan P0 yayın geçmişi

P0 hazırlığı [PR #12](https://github.com/batuhanozgun/agentic-os-search/pull/12), merge commit `ed01a591059ea8f8dd17dc5622eb314f92d2c3d9` ile main üzerinde yayımlandı. [PLAN](PLAN.md)'daki 11 yeni dosya ve 7 sınırlı mevcut dosya değişikliği tamamlandı. Agent-control içinde yalnız `agent/protocols/candidate-research-library.md` yerleştirme/geri çağırma eki değişmişti; bu tur kontrol dosyası değiştirilmedi.

Hazırlık branch'i `setup/concepts-reference-20260918`, `3d93615ae51e4e85cd509e49f65b4c2afbad07c0` main sürümünden açılmıştı. Çalışırken main ECC U06-B ile `34ebc13e87fc7f42f882472eced2a576bb4d27a1` oldu. PR #12, bu güncellemeyi koruyarak exact head `bb19c2f9d77d85dcb05ba0d97a14792cbf1031e6` üzerinden birleşti. Hazırlık branch'i bekleyen kurulum işi veya alternatif current state değildir.

[SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md) yalnız P0'ın tarihli yayın/geri okuma kanıtını taşır; U01'in veya gelecekteki iletişim başarısının doğrulaması değildir. Genel branch temizliği, başka oturumun branch'ine yazma, force push veya repository koruma ayarı değişikliği bu tur kapsamı değildir.
