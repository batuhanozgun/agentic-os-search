# Concepts — Güncel Durum

**Tarih:** 2026-09-18. **Güncel odak:** İçinde bulunduğumuz sohbetin temel parçaları. Önceki tamamlanma/yayımlama ve dış-kaynak aktarımı rotası durduruldu; bunlar sıradaki iş değildir.

## Kullanıcının son yönü

Kullanıcı soyut iş yönetimi tartışmasına kayışı durdurdu. Önce LLM, Agent, Context, Memory ve Agentic gibi temel kavramları; “Ben varım, sen varsın, arayüz var” diyerek mevcut sohbet ortamı üzerinden yerleştirmeyi istedi. Son açıklama ile repository tanımları karşılaştırıldı; kullanıcı “tamam yap” diyerek temel parçaları birlikte gösterme adımını açtı.

Bu görev yeni bir araştırma programı, bütün sözlüğü tamamlama, mimari/iş yönetimi tasarlama veya her kelimeyi kullanıcıya teknik onaylatma işi değil. Yanlış yönün yalnız dosyadan kaynaklandığı kanıtlanmış değildir; assistant'ın önceki örnek seçimleri de bu yönü üretmişti.

## Mevcut çıktı

[WORKING](WORKING.md#sohbetin-temel-parcalari) artık mevcut sohbetin tarifinden başlıyor: kullanıcı, tarayıcı, ChatGPT uygulaması/arayüzü, asistan ve yanıt üretiminde kullanılan Model/LLM; bunların yanında mesaj, prompt/talimat, Context, Memory ve Tool. Agent iş yürütme düzenini, Agentic onun modelle adım seçebilme özelliğini niteliyor. Bunlar ayrı zihinler veya birbirini dışlayan etiketler olarak kurulmadı.

“Tamam yap” mesajının önceki konuşmayla anlam kazanması ve GitHub'dan dönen dosyanın bağlama bilgi sağlaması bu ortamın somut örnekleri. Asistanın araç kullanabildiği gözlemi, belirli bir ChatGPT ürün kipinin etkin olduğuna veya görünmeyen iç mimariye ilişkin iddia değil.

[Kaynak notları](SOURCES.md#sohbetin-temel-parcalari) dar resmi belge okumalarını, yerel tercihleri ve gözlem sınırını ayırır. Kullanıcının ekranı/hesap ayarları incelenmedi; mevcut araç olanakları ve kullanıcının tarayıcı açıklaması esas alındı. Genel Memory ile ürünün Memory özelliği eşitlenmedi.

## Önceki çalışmanın yeri

Eski kırk maddelik çalışma ve iki ileri örnek, WORKING'de sabit `13dbf32df3ce00a8e45739bfcc1c6a90fecab152` geçmişine bağlandı. Tanım/kanıt gövdeleri o commit'te erişilebilir; günlük başlangıçta ayrı otorite veya tamamlanacak kuyruk değil. Önceki araştırmayı yanlış ilan ederek sıfırlamıyoruz; aktif sorunun önüne geçmesini engelliyoruz.

## Devam

Önce bu ortamı aynı terimlerle anlaşılır biçimde konuş. Kullanıcı bir parça veya ilişkiyi açtığında ona cevap ver; kendi kendine yeni onlu, yayın yetkisi, kimlik göçü, kapanış programı veya geniş kaynak taraması başlatma. Temel açıklamanın kendisini sürekli yeniden kurma da gerekmez.

Kullanıcıdan bütün maddeleri tek tek onaylaması beklenmez. Bu turdaki açıklama toplu kullanıcı kabulü değildir. Yetki belirsiz değilse kısa, somut anlatımla ilerle; ancak açıklama için gerçekten gereken kaynak kontrolünü yap.

## Repository

Main tek güncel çalışma alanı; altı dosya korunur. Bu değişiklik yalnız WORKING, SOURCES ve STATE'i kapsar. INDEX ve METHOD genel giriş/yöntem olarak, HISTORY önceki sadeleştirme kaydı olarak korunur. Agent-control ve başka araştırmalara yazılmaz. Yeni dosya, klasör veya branch açılmaz.

Yayın tabanı `13dbf32df3ce00a8e45739bfcc1c6a90fecab152`. Değişiklik önce diff/kapsamla, ardından main içeriğiyle kontrol edilir; force kullanılmaz. Bu kontrol anlamların evrensel doğruluğunu veya gerçek ChatGPT iç mimarisini doğrulamaz.
