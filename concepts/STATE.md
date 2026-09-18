# Concepts — Güncel Durum

**Kayıt tarihi:** 2026-09-18.
**Mevcut iş:** Kullanıcının onayladığı bağlantılı kavram inceleme biçimini repository'ye uyarlamak; yeni terim araştırması değil.
**Yöntem:** [METHOD v0.2](METHOD.md) ve [esnek PLAN v0.2](PLAN.md); üç kayıt düzeyi korunuyor, global terim kuyruğu kaldırılıyor.
**Yöntem yayını:** ÇALIŞMA BRANCH'İNDE ADAY; main birleşimi ve yayın sonrası geri doğrulama henüz tamamlanmadı.
**Korunan araştırma:** [Agent U01](research/agent/U01-SOURCE-USES.md), main üzerinde yayımlanmış ilk sınırlı kaynak incelemesi. Bu bakım turunda yeni kaynak bulgusu eklenmedi.
**Kabul edilmiş ortak anlam:** Yok. Yöntem onayı, Agent veya komşu terim tanımının kabulü değildir.

## Amaç ve son kullanıcı yetkisi

Amaç, kaynaklarla bağlantılı fakat kapsamı bize ait ortak kullanımlarla iletişimde aynı nesneyi konuşabilmektir. SOUL'un henüz seçilmemiş yapısı tanımın ölçütü değildir. Kaynakların kullanımını kendi tercihimize göre değiştirmeyiz.

U01 sonrasında kullanıcı, bir terim araştırılırken ortaya çıkan terim ve işlevleri gerektiği kadar birlikte irdeleyip kararlaştıran, katı olmayan bir çalışma istedi. “Agent budur” yerine “biz agent terimini bu anlama gelecek şekilde kullanıyoruz” hedefini belirtti. Son talebi, önce çalışma biçimini oturtmak ve repository dosyalarının uygunluğunu inceleyip gerekenleri düzeltmek oldu. Seçili özgün ifadeler ve yorum/kabul sınırı [PURPOSE](PURPOSE.md)'tedir.

**Bu turun yetkisi:** Yöntem uyumu incelemesi, gereken repository düzenlemesi, kapsam/bağlantı/yayın kontrolü ve sonucu kullanıcıya sunmak. Yeni dış kaynak araştırması, belirli ortak tanımın kabulü, SOUL/Development OS tasarımı veya implementasyon değil. Kontrol protokollerini değiştirmeyi gerektiren bir routing açığı saptanmadı; mevcut preflight ve concepts yönlendirmeleri kullanılıyor.

## Durum ayrımları

| İş/sonuç | Durum |
|---|---|
| P0 hazırlık | TAMAMLANDI; tarihsel yayın korunuyor. |
| U01 kaynak incelemesi | YAYIMLANDI / İLK SINIRLI DİLİM; bütün Agent literatürünün tamamlandığı iddiası yok. |
| Bağlantılı çalışma yöntemi | Kullanıcı yönüyle v0.2'ye uyarlandı; yayın adayı. |
| Envanterdeki komşular | Kaynaklı soru/keşif kaydı; araştırılmış veya zorunlu önkoşul listesi değil. |
| Agent için hangi komşuya girileceği | Henüz seçilmedi; mevcut anlam sorusuna etkisiyle değerlendirilecek. |
| Yeni sentez / referans adayı | Bu tur oluşturulmadı. Sohbetteki örnek tanım benimsenmedi. |
| Kabul edilmiş yerel referans | Yok; belirli kapsam için açık karşılıklı değerlendirme gerekiyor. |
| SOUL/Development OS kararı | Bu programdan doğan mimari/uygulama kararı yok. |

## Yeni oturumda devam yolu

Güncel AGENT ve gereken protokoller → [INDEX](INDEX.md) → bu STATE → [PURPOSE](PURPOSE.md) → [METHOD](METHOD.md) → [PLAN](PLAN.md) → ilgili [envanter/keşif kaydı](TERM-INVENTORY.md) → [Agent BRIEF](research/agent/BRIEF.md) → [U01](research/agent/U01-SOURCE-USES.md). Aktif aday veya kabul edilmiş referans ileride oluşursa ilgili kayda da inilir.

**Devralınacak açık soru:** Agent dediğimizde aynı şeyi konuşabilmek için eldeki hangi ayrımı açıklığa kavuşturmamız gerekiyor? U01 ve kullanıcının somut cümlesi üzerinden bu soru ele alınır. Bir komşuya inilirse neden açıldığı ve hangi soruya dönüleceği korunur. Şu anda aktif komşu araştırması/iniş noktası yoktur.

**Sıradaki mantıklı kavram işi:** U01'deki ayrımları ve kökeni ayrılmış bağlantıları birlikte değerlendirmek; gerekiyorsa belirli komşu soruya sınırlı inmek, zemin yeterliyse yerel kullanım adayı önermek. Ne otomatik U02 taraması ne de hemen Agent tanımı kabulü seçildi. “Agent oluşturmak” U01'in açık aday sorularından biridir; tek zorunlu sonraki iş değildir.

**Şu andaki yetkili kapanış işi:** Yöntem uyarlamasının yayınını ve gerçek kontrollerini tamamlayıp kullanıcıya dönmek. Sonraki kavram çalışması kullanıcı devam yönüyle açılır. Böyle bir devamda gerekli komşu incelemesi, karşılaştırma ve aday önerme aynı işin adımları olabilir; her küçük adımda ayrı faz onayı istenmez. Bir yerel anlamın kabulü ise belirli açıklamaya verilen açık kullanıcı değerlendirmesini gerektirir.

P0'ı, U01'i veya önceki sohbetin geçici örneklerini yanlış statüyle devralma. Envanter bir checklist değildir. “Yöntem uygun” ifadesi örnek Agent tanımını, “zorunlu komşular” listesini, hazır/özel ikiliğini veya model/ürün adı örneklerini doğrulamaz. U01 ve SETUP-VERIFICATION içindeki tarihli durum/sonraki-iş anlatımları bu güncel STATE'i geçersiz kılmaz.

## v0.2 değişiklik ve yayın kaydı

**İncelenen main:** `a605ee34b45b68d9d2aece5bc815a602f4676081`.
**Çalışma branch'i:** `maintenance/concepts-connected-inquiry-20260918`.
**Ayrıntılı kapsam / kontrol:** [METHOD-ALIGNMENT-2026-09-18](checks/METHOD-ALIGNMENT-2026-09-18.md).

Concepts içindeki mevcut 12 dosya ve programın kontrol/giriş bağlantıları değerlendirildi. On concepts dosyası güncelleniyor; U01 ve tarihsel SETUP-VERIFICATION korunuyor. Kök README ile studies INDEX'te yalnız concepts açıklaması değişiyor; bir uyum/kontrol kaydı ekleniyor. İlgili olup değişmeden bırakılan dosyaların gerekçeleri aynı kayıtta bulunur. Araştırma içerikleri ve agent-control değişmiyor.

Branch'te hazırlanmış olmak main yayını değildir. Gerçek PR, merge kimliği ve yayın sonrası geri okuma tamamlanınca bu bölüm ile kontrol kaydı gerçekleşen sonuca güncellenecek. Yerel anlamın iletişimde işe yaradığına dair bağımsız davranış deneyi yapılmadı.

## Korunan U01 yayın geçmişi

U01 araştırması 2026-09-18'de kullanıcının açık Agent araştırma yönüyle başladı; P0 yetkisinden otomatik geçiş yapılmadı. Başlangıç okumaları main `0743feae8728faebb48982ec22c447b06f2a0eaa` üzerinden, yayın tabanı `a3c208905560e0f998c0af019b235825a276969e` üzerinden yürütüldü; eşzamanlı ECC `ROUND-U08-A.md` eki korundu.

[PR #19](https://github.com/batuhanozgun/agentic-os-search/pull/19), `research/concepts-agent-u01-20260918` branch'i, exact head `75179c8fd73411a0be8c5ac2b379ec47197c5afb`, merge commit `2a3eeb1fe0853b408d07c1fbd83828e33439efbf`; yayın kapanışı `a605ee34b45b68d9d2aece5bc815a602f4676081`. U01 blob'u `22f04d1c120afa91781f680af32bf3b5944c3d30` idi ve bu yöntem uyarlamasında korunur.

O tur yalnız U01, STATE, Agent BRIEF, research INDEX ve TERM-INVENTORY değişti. PR diff'i ve main geri okumaları yapıldı; head ile merge arasında dosya farkı yoktu. Bu kontroller kaynak doğruluğunun bağımsız testi değildi. U01'in kendi okuma ve kanıt sınırları dosyasında kalır; yöntem değişimi yeni bulgu üretmez.

## Korunan P0 yayın geçmişi

P0 hazırlığı [PR #12](https://github.com/batuhanozgun/agentic-os-search/pull/12), merge commit `ed01a591059ea8f8dd17dc5622eb314f92d2c3d9` ile main üzerinde yayımlandı. [PLAN](PLAN.md)'daki tarihsel 11 yeni dosya ve 7 sınırlı mevcut dosya değişikliği tamamlandı. Agent-control içinde yalnız `agent/protocols/candidate-research-library.md` yerleştirme/geri çağırma eki değişmişti; bu tur kontrol dosyası değiştirilmedi.

Hazırlık branch'i `setup/concepts-reference-20260918`, `3d93615ae51e4e85cd509e49f65b4c2afbad07c0` main sürümünden açılmıştı. Çalışırken main ECC U06-B ile `34ebc13e87fc7f42f882472eced2a576bb4d27a1` oldu. PR #12, bu güncellemeyi koruyarak exact head `bb19c2f9d77d85dcb05ba0d97a14792cbf1031e6` üzerinden birleşti. Hazırlık branch'i bekleyen kurulum işi veya alternatif current state değildir.

[SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md) yalnız P0'ın tarihli yayın/geri okuma kanıtını taşır; sonraki araştırmanın veya gelecekteki iletişim başarısının doğrulaması değildir. Genel branch temizliği, başka oturumun branch'ine yazma, force push veya repository koruma ayarı değişikliği bu tur kapsamı değildir.
