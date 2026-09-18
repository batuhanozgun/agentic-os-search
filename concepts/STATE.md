# Concepts — Güncel Durum

**Tarih:** 2026-09-18. **Durum:** dosya ve branch temizliği tamamlandı. Bakım engeli kalmadı; kavram çalışmasına mevcut taslağı somut kullanımlarda sağlamlaştırarak dönülecek. Bu tur durum ve devam planı açıklanır; yeni kaynak araştırması veya tanım değişikliği yapılmadı.

## Son kullanıcı yönü

Kullanıcı dokuz eski concepts branch'ini temizlediğini bildirdi; kalan repository kayıtlarının güncellenmesini, ardından kavram çalışmasında ne elde edildiğinin ve bunlarla nasıl ilerlenmesinin planlandığının açıklanmasını istedi. Bu yön, yeni onlu üretme veya SOUL tasarlama yetkisi değildir. Çalışma tanımlarını seçme ve gerektiğinde birlikte düzeltme sorumluluğu assistant'ta kalır; tek tek teknik onay kuyruğuna dönülmez.

## Repository durumu

Güncel çalışma alanı `main`; concepts altındaki altı dosya korunuyor: [INDEX](INDEX.md), [METHOD](METHOD.md), bu STATE, [WORKING](WORKING.md), [SOURCES](SOURCES.md), [HISTORY](HISTORY.md).

2026-09-18 branch listesi yeniden okundu: main ve başka çalışmalara ait on branch var; silinmesi istenen dokuz concepts branch'inin hiçbiri yok. Diğer branch adları/uçları önceki kontrolle aynı; açık PR listesi boş. Kullanıcının silme işlemi doğrulandı, assistant silmiş gibi kaydedilmedi. Ayrıntı ve silme öncesi main'e dahil olma kanıtı HISTORY'dedir.

Eski 23 dosya sabit Git geçmişinden erişilebilir. Yeni branch, klasör veya sürüm dosyası açılmadı. Bu kapanış yalnız STATE ve HISTORY'yi günceller; yöntem, taslak, kaynak notları ve başka araştırmalar değişmez.

## Elimizde ne var?

WORKING, 40 numaralı madde ve Task alt kullanımından oluşan ilk bağlı anlam taslağıdır. Birlikte kullanım haritası ve karışabilecek anlamlara ilişkin ilk ayrımlar vardır. Bunlar hazır bir mimari, bütün maddeleri eşit güçte doğrulanmış sözlük veya kullanıcının tek tek benimsediği tanımlar değildir.

SOURCES eski kaynak kayıtlarına geri dönüşü, kaynak gözlemi ile yerel tercih arasındaki farkı ve kanıt eksiklerini taşır. Özellikle U03–U06'nın URL/tarih listeleri tek başına bütün okuma iddialarını doğrulamaz. Mevcut tanımlar araştırma girdisidir; sıfırdan başlanmaz, yanlış veya eksik olan kısım gerekçeyle düzeltilir.

## Devam planı

İlk incelemede “Agent'ın modelini değiştirelim” ve “Aynı agent yeni oturumda devam etsin” cümlelerini birlikte ele al. Agent–Model/LLM–yapılandırma–Role/Identity–Run/Session çevresinde neyin değiştiğini ve neyin aynı kaldığını açıkla. Model/ürün/sağlayıcı veya hazır/özelleştirilmiş kullanım ayrımı bu açıklamayı etkiliyorsa gerektiği kadar aç; bunların her biri için ayrı tam araştırma başlatma.

Ardından veya ilk inceleme gerektiriyorsa “İşi bitirdi; yayımlayabilir” örneğiyle Work state–Completion–Verification–Authority/Permission ilişkisini sınayabilirsin. Örnekler henüz uygulanmış test değildir; değişmez sıra veya yeni paket kotası da değildir.

Her incelemede gerekli kaynak dayanağına dön; kaynak kullanımı ile seçilen yerel anlamı ayır; ilgili tanımları ve okları aynı WORKING dosyasında düzelt; bir karşı örnekte yeniden dene. Gerçekten açıklama sağlayan yeni terim eklenebilir, gereksiz ayrım kaldırılabilir. Başarı terim sayısının artması değil, aynı somut anlatımın daha az varsayımla anlaşılmasıdır.

**Sonraki kavram turunun yeterli çıktısı:** seçilen bağlı küme için kaynak dayanağı belirtilmiş kullanım, anlaşılır ilişki haritası, örnek/karşı örnek sonucu ve değişen/açık kalan sınırlar. Bütün 40 maddeyi bitirmeyi veya kullanıcıdan her tanımı onaylamasını bekleme. Anlam yeterince açıklanabildiğinde başka gerçek kullanım ihtiyacına geç.

## Bu turun kapanış sınırı

Branch doğrulaması ve kayıt güncellemesi tamamlanıp kullanıcıya mevcut kazanım ve devam planı sunulur. Bu planın açıklanması örneklerin sınandığı, kaynakların yeniden doğrulandığı veya tanımların kesinleştiği anlamına gelmez. Sonraki çalışma yukarıdaki somut kullanımdan devam eder; repository hazırlığı tekrar edilmez.
