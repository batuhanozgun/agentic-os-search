# DEVOS-001 — yönetilen iş ve devam kaydı

**Güncelleme:** 24 Eylül 2026. **Aşama:** bütünsel çalışma düzeni TASARIMI AÇILDI; ihtiyaç odaklı kaynak okuması ve mevcut kayıtların değerlendirilmesi birlikte ilerler.
**Amaç:** Development OS'u kurabilecek bilgi, iş, aktör ve ortam düzenini tasarlamak; tekil dosya/denetçi onarımı değil.
[BRIEF](BRIEF.md) → [METHOD v2](METHOD.md) → [COVERAGE](reading/COVERAGE.md). Kanal [EXCHANGE](EXCHANGE.md).

## Yeni yön ve eski kapının durumu

Kullanıcı Foundation'ın tam yeniden okuması beklenmeden çalışma yapısı tasarımına geçilmesini, gerektiğinde Foundation'a drill-down yapılmasını istedi; tam söz BRIEF'te. Önceki P1 bütün-Foundation-okuması → P2 → P3 seri giriş koşulu **YERİNİ ALDI: tasarım + gerekçe için gerekli kaynak okuması**. P1 tamamlandı sayılmıyor. Önceki 'sıradaki 01_verticals tam okuması' artık otomatik sonraki iş değil.

Bu tur yöntem/geçiş kararı ve Claude'a R-006 oluşturuldu. Bütün çalışma yapısı henüz seçilmedi, kod/kurulum yapılmadı. Research'ün yazarlığı, bugünkü bütün ayrıntıları bildiğinin kanıtı sayılmadı. Foundation REUSE mevcut ihtiyaca göre kaynak derinliği kullanımını destekler; kaynak otomatik mimari değildir.

## Güncel işler

| İş | Sorumlu | Durum / beklenen çıktı |
|---|---|---|
| D1 Bütünsel çalışma düzeni tasarımı | Research; Claude örnek/ortam katkısı ve karşı görüş | AKTİF AŞAMA; ilk bütünsel tasarım çıktısı sırada. DevOS üretim işinin rol, iş, bilgi ve ortam ilişkilerini bir arada açıklamak |
| D2 Kaynak ve alternatifleri tasarıma bağlama | Research + Claude | D1 ile birlikte: mevcut kayıtlar, Foundation genel sentezleri ve kararın gerektirdiği özgün ayrıntılar; kaynak/karar/boşluk izi |
| P1-S/X Mevcut Claude okuma ve kayıt işleri | Claude; Research karşı okuma | Devam noktaları korunur; bitişler/engeller yayımlanmış kayıtla teyit edilir, yeni toplu Foundation turu otomatik açılmaz |
| P2 Oluşmuş kayıtların ortak değerlendirilmesi | Research + Claude | İptal değil; D1/D2 ile birlikte ilerleyecek. Tüm kayıtlar bu tur okunmadı; paket özeti tam kayıt okuması sayılmaz |
| P3 Gerekçeli yapı seçimi | Research + Claude; gerçek owner tercihleri Batu | HENÜZ YOK. Alternatifler ve yük taşıyan kaynaklar değerlendirilmeden kurulmuş/seçilmiş yapı ilan edilmez |
| P4 Kurulum ve gerçek kullanım | Sonraki uygulama planı | BAŞLAMADI; yeni repo, geniş deney, hook/izin değişikliği veya otomasyon yetkisi yok |

Eski E19/M1–M3 ve test-repo ayrıntıları yeniden kritik yol olmadı. İlk tasarım çıktısı başka bir genel plan değil; aşağıdaki üretim yürüyüşünün nasıl işleyeceği olmalı.

## D1'in somut teslimatı

Development OS'u kurma amacı → gereken iş ve önkoşulları keşfetme → uzmanlık/sorumluluk ve ortamı hazırlama → göreve uygun kaynak/bağlam oluşturma → işi yürütme/koordine etme → sonuçları değerlendirme → planı ve bilgi durumunu güncelleme → kesintiden devam.

Bu yürüyüşte: ne iş yapılır; kim hangi yetki/yeterlikle devralır; hangi bilgiye nasıl ulaşır; nerede ve hangi araçlarla yapar; sonuç sonraki işi nasıl değiştirir? Örneklere dayalı mekanizma seçenekleri birlikte değerlendirilecek. Dört zemin ayrı dört ürün, her rol ayrı ajan, her gereksinim ayrı dosya sayılmaz. Burada henüz bu mekanizmalar seçilmiş değildir.

## Bilinen kaynak durumu

Son tam devralınmış Claude mesajları C-003/C-004/C-005, alım ref'i `9866feb1127313394a3d1bd50bfd4b862a91567f`; exact kimlikleri [önceki WORK](https://github.com/batuhanozgun/agentic-os-search/blob/3c809d9691643b6183bc035cd344f12efb3f4c87/development-os/attempts/001/WORK.md)'te. 74 studies birim kaydı, 9 concepts kaydı ve ORT1 üretici bildirimi olarak korunur; Research bunların tamamını henüz okumadı. E23 bitişi ve erişim/karşı okuma açıkları bu yöntem kararıyla kapanmaz.

Research kayıtları F08 + ek ve F00; 18 özgün Foundation dosyası. Kalanlar yeni okumada otomatik tamamlandı değildir; ancak hepsi tekrar okunmadan tasarım başlayabilir. F08 S07 tamlık düzeltmesi ve dört eksik kaydı korunur.

Bu tur güncel Research main `3c809d9691643b6183bc035cd344f12efb3f4c87`, hedef main `0b0b4f86230c7f5b46f98532ad96718a82a28819` olarak okundu. Hedef STATE tam okundu; O-26 paylaşımın aktörler arasında çözülmesini kaydediyor. Hedef canlı workflow'ları gözlenmedi. Foundation REUSE doğrudan yeniden tam okundu (`b92c29d85055c70536392c0804a7a621efc9caff`); aynı konuşmadaki diğer değişmemiş kontrol/giriş/kaynak okumaları kullanıldı. Bütün Foundation yeniden okunmadı.

## İletişim ve sonraki sorumluluk

[R-006](messages/research/R-006.md), yeni kullanıcı yönünü ve değişen yöntem/giriş koşulunu taşır. Eski mesajlar yeniden yazılmaz. Bu checkpoint'te Claude'un R-005 veya R-006'yı aldığı doğrulanmadı. Sonraki C mesajı mevcut yanıt kimliğini koruyarak güncel yönü alabilir; sırf numara için yeni cevap turu gerekmez.

Research sıradaki turda D1'i kendi işi olarak yürütür; bütün Foundation bitişi ya da Claude'un alındısı beklenmez. Claude devam eden okuma kayıtlarını korur; yeni yönü gördüğünde bütünsel tasarıma kaynaklı örnek/ortam katkısı verir. İlk task, kullanıcıya tekrar teknik paylaşım seçtirmek veya başka bir tam-okuma kampanyası planlamak değildir.

Repo mesajı oturumu kendiliğinden uyandırmaz; alım ve uygulama yayımdan ayrıdır. Kullanıcıdan Foundation'ı tekrar okuyup açıklaması istenmez.

## Koruma ve yayın kapsamı

Başlangıç source inventory `dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb` değişmedi. Önceki kanıt, C mesajları, kaynak araştırmalar ve R-001–R-005 korunur. Bu yayın yalnız root README, development-os INDEX, BRIEF, METHOD, WORK, COVERAGE ve R-006'yı değiştirir/ekler. Kontrol, özgün araştırma, concepts çalışması ve hedef repo değişmez. Yayın/ref ve geri okuma commit oluşturulduktan sonra kontrol edilir; bu dosya kendi gelecekteki commit'ini uydurmaz.
