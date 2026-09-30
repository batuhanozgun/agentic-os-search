# A2 — tarihsel inceleme ve kanıt kayıtları

**İş:** REPO-SEPARATION-20260929 / A2. **Kayıt tarihi:** 30 Eylül 2026. **Durum:** Kısmi; `current/reviews/` içindeki 22 dosyanın ilk 6'sının statü incelemesi tamamlandı. Bu, A2'nin veya depo genelindeki denetimin kapanışı değildir. Güncel bakım devamı yalnız [REPOSITORY-TRANSITION](../../REPOSITORY-TRANSITION.md)'dedir.

## 1. Yetki ve başlangıç

[Batu'nun görev belgesi](REQUEST.md) §3.2, §4–§6 ve bu konuşmadaki “devam et” mesajı kapsamında yalnız `batuhanozgun/agentic-os-search` içinde yerinde statü/yönlendirme bakımı yapıldı. Yeni DevOS planı, kurulum, mimari veya SOUL işi oluşturulmadı. Güncel Claude planının kopyası alınmadı; diğer depolara, hesaplara veya hizmetlere yazılmadı.

Başlangıç main'i **`9620dfdeda71f25580f6945c2bb3a11c19b78703`**, root tree **`178787b9f8fe7b1f48df8c304f594c1a7242fcf3`**. Önceki dokuz brief'in yayını bu commit'te doğrulandı; main arada ilerlememişti. Bütün bakımın karşılaştırma tabanı `8cd01e4afdcd0d37960b05930c91e1244678be6e` olarak kalır.

`reviews/` başlangıç alt ağacı `2c15d63ca63812f00dbca0b3447d8ab8efcbefd9`, recursive yanıtta `truncated=false`; 22 dosyanın yol/blob/boyut envanteri yeniden görüldü. Bunun bütün içeriklerin okunduğu anlamına gelmediği korunur. [A2-CURRENT-INVENTORY](A2-CURRENT-INVENTORY.md) tarihli başlangıç envanteridir; eski T/Ö/A işaretleri kendi kaydedildikleri turun durumudur. Sonraki sonuçlar bu kayıt ve kök bakım planıyla takip edilir; eski envanter tekrar yazılmadı.

## 2. İlk altı dosyanın sonuçları

Ortak yol öneki: **`research/soul-context/current/reviews/`**. Numaralar başlangıç envanterinin numaralarıdır. `NOT` = başa altı satırlık tarihli statü notu eklendi; `KORU` = tam okundu, mevcut statü açıklığı yeterli bulundu, dosya değiştirilmedi.

| # | Dosya | Başlangıç blob'u | Byte | Sonuç ve gerekçe |
|---|---|---|---:|---|
| 20 | `2026-09-06-direction/OPENING-VISION-SOURCE.md` | `f8d4aa7c5fb6b09dc3e49ba5f336bb30bc5c4825` | 13690 | NOT — Ham aktarım doğrudan Routing gate ile açılıyordu. Bunun önceki assistant cevabı olduğu, aktif kontrol sonucu veya kabul edilmiş mimari olmadığı doğrudan girişte ayrıldı. |
| 21 | `2026-09-06-direction/REVIEW.md` | `d7ea6a8b664ee9f973a8ec9b78c3bcaf14a03222` | 13345 | NOT — C1/D1 durumu, önerilen yön düzeltmesi ve sonraki iş yalnız eski incelemeye bağlandı. Vizyonun daralmamasıyla ilgili kaynak ayrımları reddedilmedi. |
| 22 | `2026-09-06-g0/EVIDENCE-EXTRACTS.md` | `f66e20322e8fa3b27aeed4c68331d20cdafd36b3` | 9410 | KORU — İlk bölüm zaten 6 Eylül'de alınmış seçili kanıt olduğunu; çalıştırılacak talimat, kabul edilmiş kontrol veya canlı DevOS durumu olmadığını açıkça söylüyor. Komutlar ve devir alıntıları etiketli/fenced; yeni not gerekli görülmedi. |
| 23 | `2026-09-06-g0/REVIEW.md` | `bb95618266b8d5d31a2b0d327af09331fe1801ad` | 14308 | NOT — Eski G0 hükmü ve D1 önerisi güncel teşhis/deney sırası olmaktan ayrıldı. Yapılmamış T1–T4/R(C1), gerçek gözlem ile yerel nedensel hipotez ayrımı aynen korundu. |
| 24 | `2026-09-06-stage-1/CODEX-RESPONSE.md` | `4f64d7a5178ad639c2052a0f144653971b947295` | 21046 | NOT — Ham yanıtın üç yüzeyli başlangıç, eski depo ve sonraki uygulama önerileri bugünkü kurucunun talimatı olmaktan ayrıldı. Okuma/işlem beyanları kaynak yanıtın beyanı olarak kaldı. |
| 25 | `2026-09-06-stage-1/REVIEW.md` | `b788ee43c01dd8f375c5a02274d29191310f5cd3` | 19273 | NOT — S1A sonraki iş önerisi ve C1–C4 açıklıkları eski tasarımın değerlendirmesi olarak sınırlandı; bugün aynı kurulumun yapılması veya aynı kalite kapsamının seçilmesi anlamına gelmez. |

Altı kaynağın toplam başlangıç büyüklüğü **91.072 byte**; not eklenen beşinin özgün gövdeleri toplam **81.662 byte**. Bu sayılar kaynak metadata toplamıdır; kanıtın niteliğini veya hedef sistem yeterliğini ölçmez.

## 3. Okuma ve anlamı koruma sınırı

Altı dosya başlangıç commit'inden tam okundu. Opening vision 1–150, 151–400 ve 401–son; direction review 1–80 ve 81–son; G0 review 1–85 ve 86–son; Stage-1 review 1–100 ve 101–son aralıklarıyla tamamlandı. G0 kanıt seçkisinin tam görünümü okundu. Stage-1 yanıtının ilk kesilmiş görünümü 70–125 örtüşen aralığıyla tamamlandı; özgün yanıt 119 satırdır. Kesilmiş araç görünümü tek başına tam okuma sayılmadı.

Kaynakların atıf yaptığı bütün Foundation/studies metinleri, önceki ZIP'ler, Mac günlükleri ve resmî ürün belgeleri yeniden incelenmedi. Kaynaklarda anlatılan geçmiş testler çalıştırılmadı; yeni platform, güvenlik veya davranış doğrulaması yapılmadı. `PARSER-REGRESSION.py` bu alt kümeye dahil değildir, okunmuş ya da çalıştırılmış sayılmaz.

Notlar, kaynağın epistemik statüsünü değiştirmiyor: gözlem hipoteze, öneri kullanıcı kararına, geçmiş sınırlı PASS yeni hedefin kabulüne dönüşmüyor. Tarihsel statü platformdan bağımsız ilkeleri değersiz veya yanlış ilan etmiyor. Özgün metindeki biçim kusurları dahil bütün gövde korunuyor.

İki ham aktarımın yeni notunda **başlangıç commit'indeki byte-sadık özgün kopyaya** bağlantı verildi. Eski incelemelerdeki satır, byte ve hash kimlikleri yeni altı satırlık notu değil özgün gövdeyi tanımlar. Öneksiz eski kaynağa dönmek bugünkü işlem yetkisini geri getirmez; o bağlantı kaynak karşılaştırması içindir.

## 4. İçerik doğrulaması ve bağlantılar

Doğrulanmış içerik adayı **`50e4dcd27ac8a9025d4778a1148c8eb6c321ac8c`**, tree **`eb90660ac6aade7e7fc892d03467e3c18090a1af`**, parent başlangıç main'idir. GitHub compare **beş dosyanın her birinde 6 ek satır ve 0 çıkarılan satır** gösterdi: toplam 30 satır. Birleşik patch tam okundu; bütün hunk'lar yalnız `@@ -1,3 +1,9 @@` başlangıç ekleridir. Özgün gövde ve dosya sonlarında fark kalmadı.

İlk yayımlanmamış aday `3554ab83b64ac7c88a1768b29527e98c44cd4a5b` üç REVIEW dosyasının son LF'sini düşürmüştü. Compare/patch denetimi bunu yakaladı; LF'ler geri kondu ve düzeltilmiş aday tekrar karşılaştırıldı. Hatalı aday main'e bağlanmadı. İçerik doğrulama adayı da tek başına yayın değildir; bakım kayıtlarını taşıyan nihai commit'in main'e bağlanması ve geri okunması ayrı işlemdir.

Yeni notların **8 göreli bağlantısı** yerelde yol çözümüyle denetlendi: beş D030, bir kök bakım planı, iki yerel REVIEW bağlantısı. D030'un açık HTML kimliği sabit başlangıç commit'inden ayrıca okundu. İki öneksiz kaynak bağlantısı bu tur tam okunan sabit kaynaklara gider. Dış Claude planı adresi kullanıcı görevindeki adrestir; planın içeriği veya platform iddiaları burada yeniden değerlendirilmedi. Bütün eski gövde bağlantılarının taraması A4/A5 kapsamındadır.

Bu denetim, kaynak/diff karşılaştırması ve sınırlı okuyucu kontrolüdür; bağımsız aktörle yapılmış davranış deneyi değildir. Arama görünümünün yeni notu atlaması gibi erişim kipleri A4/A5'te ayrıca ele alınır.

## 5. Korunan alanlar ve yayın sınırı

Kaynak dosyası silinmedi veya taşınmadı; `MOVES.md` değişmedi. G0 kanıt seçkisi aynı blob olarak korundu. Kontrol dosyaları, Foundation/studies/concepts araştırma gövdeleri ve diğer eski görevler bu alt kümede değiştirilmedi. Kaynak düzeltmelerinin yanında yalnız bu bakım kaydı eklendi ve kök `REPOSITORY-TRANSITION.md` ilerletildi.

Başlangıçta sabit main için `author=batuhanozgun-devos` ve `committer=batuhanozgun-devos` sorguları boş döndü. Bu bütün dal ve kimliklerde yokluk kanıtı değildir. Yayından önce main/delta ve yazar kontrolü tekrar yapılır; çakışan çalışma ezilmez, force push kullanılmaz. Nihai ref ve kaynak/bakım dosyaları yayın sonrasında geri okunur; gerçekleşmemiş yayına başarılı denmez.

## 6. Kalan kapsam

`current/reviews/` içindeki **6/22 dosya** sonuçlandırıldı; **16 dosya**, başlangıç envanterinin **26–41** satırları, henüz bu bakımda içerik/statü bakımından okunmadı. İlk kalan grup `2026-09-06-stage-1a/CODEX-RESPONSE.md` ve `REVIEW.md`dir; ardından 28–41 gelir. Kaydın varlığı kusur veya değişiklik zorunluluğu değildir; gerekçeli koruma da sonuç olabilir.

Böylece current alanının başlangıçtaki 41 dosyasından **25'i** ilgili turlarda statü bakımından sonuçlandırılmıştır: önceki 19 ve bu 6. Bu, 25 dosyanın hepsine yeni not eklendiği veya bütün A2'nin bittiği anlamına gelmez. DEVOS-001 `reading/`, EXP-006 P1/P2/P3 doğrudan girişleri, A3 arşivi ve A4/A5 açık kalır. Tek güncel devam kaydı kök bakım planıdır; burada korunan eski “sonraki” ifadeleri yeni görev değildir.
