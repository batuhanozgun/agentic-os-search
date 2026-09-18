# Kavram Çalışması — Yöntem

Bu, yalnız concepts programının çalışma yöntemidir; agent-control kuralları değildir. Güncel amaç/yetki ve devam [STATE](STATE.md)'te, tek taslak [WORKING](WORKING.md)'dedir.

## Amaç ve iş bölümü

Kaynaklarla bağlantılı, konuşurken başvurabileceğimiz yerel anlamlar geliştiriyoruz; bütün AI terminolojisini tamamlama veya tek doğru ontolojiyi bulma işi yapmıyoruz.

Kullanıcı, “Agent'a bir tanım ver, sonra diğer terimlerine tanımlarını verdikçe çakışmalara göre finetune edeceksin” diyerek çalışma tanımlarını seçme ve düzeltme işini assistant'a bıraktı. “Bu turda ... 10 terim” isteği bir denemeydi; her turun kotası veya bitirilecek sonsuz kuyruk değildir. Sonraki mola ve sadeleştirme yönü, yeni kavram sayısını büyütmek yerine mevcut anlamların birlikte kullanımına dönmeyi gerektirir.

Assistant gerekli kaynak incelemesini yapar, bir çalışma anlamı seçer, kapsamını açıklar ve komşu kavramlar onu zorladığında düzeltir. Kullanıcıdan her sözcük için A/B tercihi veya teknik onay istenmez. Kullanıcının amacı/kapsamı gerçekten belirsizse gereken kısa soru yine sorulabilir; araştırma yükü kullanıcıya aktarılmaz.

## Çalışma döngüsü

1. **Somut kullanım seç.** Hangi cümlede hangi nesne, davranış veya kapsam karışıyor? Yeni kelime arayarak değil bu soruyla başla. Mevcut sonuçları tekrar üretme.
2. **Mevcut taslakla açıkla.** Bağlı terimleri aynı örnekte kullan; gerektiğinde birkaçını birlikte değiştir. Bir terimi bütün komşularından bağımsız kapatmaya çalışma.
3. **Boşluğu sınırla ve kaynağa dön.** Kaynak kullanımı mı farklı, tanım mı fazla geniş/dar, ilişki mi yanlış, önemli bilgi mi eksik? [SOURCES](SOURCES.md) ve gerekiyorsa studies kataloğu üzerinden yalnız gerekli kanıtı geri kazan. Güncel teknik iddiayı eski linkin varlığından doğrulanmış sayma.
4. **Gerekçeli düzeltme yap.** Aynı WORKING dosyasında anlamı, kapsamı ve ilgili ilişkiyi güncelle. Neden değiştiğini kısa bir notla belirt; yeni terim veya ayrı dosya ancak gerçek açıklama ihtiyacı varsa eklenir.
5. **Aynı örneğe dön.** Düzeltilmiş anlatım başlangıçtaki karışıklığı gideriyor mu? Bir farklı örnek veya karşı örnek hâlâ sınırı bozuyor mu? Yapılmamış incelemeye “test geçti” deme.

Yeterli ara sonuçta kullanıcıya anlaşılır anlatımla dön. Daha fazla kaynak, yeni komşu veya temiz bir şema bulunabilmesi tek başına devam nedeni değildir. Tanımlardaki önemli ayrımlar açıklanabiliyor ve açık kalanlar nitelenebiliyorsa bu tur için yeterli zemin olabilir.

## Üç farklı kayıt statüsü

**Kaynak gözlemi:** Belirli kaynak/bölüm/sürümde gerçekten ne görüldü? Okuma sınırı, iddia ve yorum ayrılır. Kayıt veya alıntı, kaynağın doğru olduğunu ya da bir mekanizmanın çalıştığını kendiliğinden kanıtlamaz.

**Çalışma tercihi:** “Biz şimdilik şu kapsamda kullanıyoruz.” Assistant'ın gerekçeli, düzeltilebilir önerisidir. Kullanıcının tek tek kabulü beklenmeden çalışma içinde kullanılabilir; dünya standardı veya ortak kabul diye sunulmaz.

**Açık kullanıcı değerlendirmesi:** Kullanıcı belirli anlam/kapsamı değerlendirdiyse bunun hangi öneriye ilişkin olduğu kaydedilir. Genel memnuniyet veya devam izni bütün taslak maddelerinin kabulü değildir. Bu ayrımı korumak için ayrı bir kabul klasörü veya zorunlu onay kuyruğu kurulmaz.

## Tanım ve harita disiplini

Kısa açıklama, kapsamı kaybetme gerekçesi değildir. Teknik adı korurken anlaşılır Türkçe kullan. SDK sınıfı, ürün adı, öğrenilmiş model, çalıştırma ve rol gibi farklı düzeyleri tek sözcük altında sessizce birleştirme.

Haritadaki her ok anlaşılır bir ilişki taşımalıdır: “bir türüdür”, “kullanır”, “içerebilir”, “belirli bağlamda üstlenir” aynı ilişki değildir. Çizim yerel anlamı açıklar; zorunlu mimari, servis veya dosya düzeni seçmez. Bir ilişkideki “olabilir” koşulunu kesin bağlantıya yükseltme.

“A ile B aynı kavram değildir” demek, aynı somut şeyin iki farklı açıdan A ve B olarak nitelenemeyeceğini göstermez. Sadece `≠` listesi yazmak çakışma testi sayılmaz. Somut örnek, yanlış okuma ihtimali ve neden yapılan düzeltmenin işe yaradığı görünür olmalıdır.

## Kaynak ve kayıt düzeni

SOURCES kaynak kullanımı/okuma sınırını; WORKING güncel yerel taslağı taşır. Özgün kaynak dilini, kod/API adını veya geçmiş konuşmayı yerel tercihle yeniden yazma. Mevcut studies ve explorations yerinde kalır; seçici bağlantıyla kullanılır.

Her tur yeni `Uxx`, `v0.x`, boş terim paketi veya arşiv klasörü açılmaz. Önce mevcut dosya güncellenir. Git değişiklik geçmişi sürümleri korur. Kapsam gerçekten dosyayı ayrı okumayı gerektirecek ölçüde büyürse yapı ayrıca değerlendirilir; altı dosya da değişmez bir kota değildir.

Güncel iş yalnız STATE'te, amaç/giriş INDEX'te bulunur. Eski amaç-plan-envanter kopyaları ve sonraki-onlu listeleri ayrı otoriteler olarak tutulmaz. Tarihsel iz [HISTORY](HISTORY.md)'den sabit commit'e gider; geçmiş sürüm current çalışma yüzeyi değildir.

## Yayın ve doğrulama

Main temel alınır; değiştirilmeden önce dosyanın gövdesi/kimliği ve ilgili branch farkı okunur. Yalnız yetkili kapsam değiştirilir. Yayın öncesi içerik, bağlantılar, eski kaydın geri bulunabilirliği ve dosya kapsamı incelenir. Main ilerlediyse eski bütün ağaç üzerine yazılmaz; force kullanılmaz. Yayından sonra main geri okunur.

Branch, PR veya hash karşılaştırması içerik aktarımını gösterebilir; kavramların doğruluğunu ya da iletişim başarısını göstermez. Aynı assistant'ın metni yeniden değerlendirmesi bağımsız davranış deneyi değildir. Yapılmamış kaynak okuması, kullanım testi veya branch silme işlemi tamamlanmış yazılmaz.

Başarı, yeni bir cümlede aynı şeyi daha az varsayımla konuşabilmektir; terim, sürüm, dosya veya commit sayısı değildir.
