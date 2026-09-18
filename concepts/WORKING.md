# Kavram Çalışması — Bu Sohbetin Temel Parçaları

**Tarih:** 2026-09-18. **Statü:** Bu ortamı açıklamak için seçilmiş, düzeltilebilir yerel kullanım. Evrensel sözlük, ChatGPT'nin iç mimarisinin dökümü veya kullanıcının her ifadeyi tek tek kabul ettiği kayıt değildir.

Güncel amaç ve devam [STATE](STATE.md)'te, yöntem [METHOD](METHOD.md)'te, kaynakların gerçek okuma kapsamı [SOURCES](SOURCES.md#sohbetin-temel-parcalari)'ndadır. Burada önce içinde bulunduğumuz sohbeti adlandırıyoruz; iş yönetimi ve tamamlanma kurallarıyla başlamıyoruz.

<a id="sohbetin-temel-parcalari"></a>
## Önümüzde ne var?

Batu, tarayıcı üzerinden ChatGPT kullanıyor ve uygulamanın sunduğu AI asistanıyla mesajlaşıyor. Asistan yanıtlarının üretiminde dil modeli kullanılıyor. Bu ilk tarifte şunlara işaret ediyoruz:

| Terim | Bu ortamda gösterdiği şey |
|---|---|
| **User — kullanıcı** | Sohbette isteğini yazan Batu. İnsan olmak ile bir uygulamanın kullanıcısı olmak farklı açıklamalardır. |
| **Browser — tarayıcı** | Batu'nun web uygulamasını açtığı yazılım. ChatGPT'nin veya modelin diğer adı değil. |
| **Web application — web uygulaması** | Tarayıcı üzerinden kullanılan ChatGPT uygulaması. |
| **User interface — kullanıcı arayüzü** | Mesaj kutusu, sohbet alanı ve düğmeler gibi etkileşim yüzeyi. Uygulamanın tamamı değil. |
| **ChatGPT — ürün/hizmet adı** | Bu sohbet deneyiminin sunulduğu ürün. Adı günlük dilde asistana hitap etmek için de kullanılabiliyor. |
| **Assistant — asistan** | Konuşmanın kullanıcıya yanıt veren AI tarafı; burada Batu'nun “sen” diye hitap ettiği taraf. |

Tarayıcıda uygulamanın web arayüzü bulunur; hizmetin geri kalanıyla internet üzerinden iletişim kurulur. Bu bir temel işlev tarifi, gerçek sunucuların, yönlendirme kararlarının veya iç servislerin keşfedildiği bir mimari şema değildir. Kullanıcının ekranı veya hesap ayarları doğrudan incelenmedi; tarayıcı bağlamı kullanıcının açıklamasından alındı. Kaynak zemini: O1–O3.

## Asistan, LLM ve Agent nasıl ilişkilidir?

**Model:** Eğitimle edinilmiş parametrelerle girdileri işleyip çıktı üreten öğrenilmiş hesaplama bileşeni. Model adı, ürünü ve ona erişim sağlayan hizmeti aynı nesne saymıyoruz.

**LLM — Large Language Model / büyük dil modeli:** Büyük ölçekli dil verisiyle eğitilmiş, dil anlama ve üretmede kullanılan model türü. Model daha genel terimdir. Çok kipli modellerin bütün sınıflandırmasını burada çözmüyoruz.

**Assistant — asistan:** Kullanıcının konuşmada etkileşim kurduğu yardımcı AI tarafı. Model bu tarafın yanıtlarını üretir; modelin yanında ikinci bir zihin veya mutlaka ayrı bir yazılım nesnesi varsaymıyoruz. O2, ChatGPT'yi LLM'ler üzerine kurulu bir asistan olarak anlatıyor. O3 kendi bağlamında model ve assistant sözcüklerini yaklaşık eşanlamlı kullanabiliyor; bu yerel açıklamada bileşen ile konuşmadaki tarafı ayırmak için niteliyoruz.

**Agent — bu çalışmada model tabanlı yazılım agent'ı:** Verilen işi ilerletmek için aldığı bilgi ve sonuçlara göre sonraki adımları model kullanarak seçebilen ve bu adımları yürütme olanaklarına sahip yazılım sistemi/birimi. Mevcut model destekli adım seçimi anlamı korunuyor; yalnızca araç bulunması veya bir kere araç çağrılması tek başına evrensel agent testi yapılmıyor.

**Agentic:** Böyle bir düzenin, her adımı kullanıcıya tek tek tarif ettirmeden sonraki adımı seçip işi ilerletebilmesini niteleyen sıfat. Yeni bir kişi, model veya ayrı bileşen adı değil. Bu, O4'teki modelle yürütme kontrolü anlatımına dayanan yerel kısa kullanım; bütün kaynaklar için kesin agency eşiği değil.

Dolayısıyla bu ortam için: **“LLM tabanlı, araç kullanabilen bir asistanla konuşuyoruz; bu çalışma düzeni agentic özellikler taşıyabiliyor.”** Asistan, LLM ve Agent birbirinden seçim yapmamız gereken üç rakip etiket değildir. Araç kullanmadan verilen bir cevap da düzenin agentic kapasitesini o anda yok etmez. Burada özel bir ChatGPT ürün kipinin etkin olduğu veya ChatGPT'nin tamamının tek bir agent olduğu ileri sürülmüyor.

## Konuşmanın bilgisi nerede?

| Terim | Bu sohbetten örnek / yerel kullanım |
|---|---|
| **Message — mesaj** | Batu'nun “tamam yap” iletisi veya asistanın buna verdiği yanıt gibi bir ileti. Mesajın içeriği ile kimden geldiği ayrılabilir. |
| **Conversation / chat — konuşma / sohbet** | Birbiriyle ilişkili mesajların oluşturduğu konuşma akışı. Her mesajı ayrı oturum saymıyoruz. |
| **Prompt — istem** | Bu örnekte asistana verilen istek/girdi. “Tamam yap” tek başına değil önceki konuşmayla anlam kazanıyor. Teknik kaynaklarda prompt daha geniş girdiyi de adlandırabilir; burada tüm Context ile eşitlenmiyor. |
| **Instruction — talimat** | Ne yapılacağını veya nasıl yanıtlanacağını yönlendiren ifade. Kullanıcının “temelden alalım” yönü örnektir. Her alıntı ve araç sonucu talimat değildir. |
| **Context — bağlam** | Belirli yanıt üretilirken modele gerçekten sunulan bilgi: mevcut istek, sunulan önceki mesajlar, ilgili talimatlar ve varsa araç sonuçları. |
| **Memory — hafıza** | Sonraki etkileşimlerde yeniden kullanılabilmesi için bilginin korunması ve gerektiğinde geri getirilmesi. Bu işlev, yalnız modelin mevcut girdisini veya eğitimle edinilmiş parametrelerini adlandırmaz. |
| **Tool — araç** | Asistanın çağırabildiği program/işlev. Bu oturumda GitHub'dan dosya okuma ve web arama araçları var. Çağrı seçimi ile programın işlemi yürütmesi ayrı şeyler. |

O2 prompt için kullanıcıya dönük kullanım sunar; O3 mesaj, asistan ve araçları ayırır. Context için mevcut yerel tanım korunur. Memory ifadesi anlaşılır Türkçeyle açıldı; O5'teki **ChatGPT Memory** bunun belirli ürün özelliğidir, genel kavramın tamamı değildir.

**Üç bilgi yüzeyini karıştırmıyoruz:** ekranda veya kayıtta bulunan geçmiş; bir sonraki kullanım için korunan bilgi; şu yanıtta modele gerçekten sunulan Context. Bir bilgi hafızadan getirilip bağlama katılabilir. Bu nedenle Memory ile Context iki rakip depo değil, farklı işlevlerdir. Uzun sohbetin kaydının bulunması bütün geçmişin her yanıtta modele sunulduğunu göstermez (O3).

Bu oturumda kalıcı kişisel hafızaya yeni kayıt ekleme aracı kapalı. Önceki mesajlara dayanarak cevap vermek bunun açık olduğunu kanıtlamaz. Bu gözlem, kullanıcının bütün hesap/proje hafıza ayarlarının denetlendiği anlamına gelmez.

## “Tamam yap” mesajında bunlar birlikte nasıl çalışıyor?

Kullanıcı mesajı iki sözcükten oluşuyor. Neyi yapacağımız, önceki konuşmanın sunulan bağlamından anlaşılıyor: bu sohbetin temel parçalarını adlandırmak ve repository'deki güncel başlangıcı buna bağlamak. Bu bağlantıyı kurmamız için yeni bir kişisel hafıza kaydı gerekmiyor.

GitHub'dan dosya okuduğumuzda **GitHub okuma işlevi araç**, repository **dış bilgi kaynağı**, dönen dosya metni ise **sunulduğunda Context'e katılan bilgi**. Repository erişiminin bulunması bütün dosyaların otomatik okunması demek değil. Dosyaları okuyup ilgili sonraki adımı seçmemiz, bu oturumdaki agentic işleyişe somut örnek; bir marka veya model adını agent diye yeniden adlandırmıyoruz.

```text
Batu / kullanıcı
    ↔ tarayıcıdaki ChatGPT arayüzü
    ↔ ChatGPT hizmeti üzerinden asistanla sohbet

Asistan yanıtı — üretilir → Model / LLM kullanılarak
Modelin bu yanıt için girdisi — içerir → Context

Mesajlar + ilgili talimatlar + varsa araç sonuçları
    — gerçekten sunulan kısım → Context

Memory — gerektiğinde geri getirilen bilgiyle besleyebilir → Context
Asistan — çağırabilir → Tool — sonuç döndürür → sonraki yanıtın bilgisi

Modelle adım seçimi + adımları yürütme olanağı
    — bu düzenin bir özelliği olarak nitelenir → agentic
```

Oklar işlevsel ilişkileri gösterir; her satır ayrı servis veya zihin değildir. “Model/LLM” yazımı da iki ayrı model gerektiği anlamına gelmez.

## Önceki incelemeler — arka plan, devam kuyruğu değil

Önceki kırk maddelik liste ve ayrıntılı incelemeler [13dbf32d sürümündeki WORKING.md](https://github.com/batuhanozgun/agentic-os-search/blob/13dbf32df3ce00a8e45739bfcc1c6a90fecab152/concepts/WORKING.md) içinde tam gövdeleriyle korunur. Güncel başlangıçtan çıkarılıp sabit geçmişe bağlandılar; hepsinin yanlış olduğu veya artık kabul edildiği söylenmiyor. Kaynak notları [SOURCES](SOURCES.md), daha eski dosya geçmişi [HISTORY](HISTORY.md)'dedir.

<a id="model-degisimi-ve-devam"></a>
**Model değişimi ve oturumda devam:** [Özgün inceleme](https://github.com/batuhanozgun/agentic-os-search/blob/13dbf32df3ce00a8e45739bfcc1c6a90fecab152/concepts/WORKING.md#model-degisimi-ve-devam). Bu ayrıntı temel ortamın açıklanmasının önkoşulu değil.

<a id="tamamlanma-ve-yayim"></a>
**Tamamlanma ve yayımlama:** [Özgün inceleme](https://github.com/batuhanozgun/agentic-os-search/blob/13dbf32df3ce00a8e45739bfcc1c6a90fecab152/concepts/WORKING.md#tamamlanma-ve-yayim). İş yönetimi, kalite ve yetki soruları bu temel sohbet tarifinin otomatik sonraki konusu değil.

## Bu değişikliğin sınırı

2026-09-18: Kullanıcı mevcut ortamın temel parçalarına dönülmesini istedi ve karşılaştırma sonrasında “tamam yap” dedi. Asistan/ürün/arayüz ve Agentic boşluğu bu örnekte karşılandı; Memory ve Context'in farklı işlevleri açıklandı. Agent'ın kapasitesi ile tek mesajdaki araç kullanımı eşitlenmedi. Bu, dar belge okumasıyla desteklenmiş açıklamadır; uygulama mimarisi testi, tüm hafıza düzenlerinin araştırması veya kırk kavramın kapanışı değildir. Sonraki konuşma burada gösterilen temel nesneler ve bilgiler üzerinden sürer.
