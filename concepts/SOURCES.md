# Kavram Çalışması — Kaynak Notları

Güncel çalışma [WORKING](WORKING.md), amaç ve devam [STATE](STATE.md)'tedir. Kaynak açıklaması ile bizim yerel sözcük tercihimiz ayrı tutulur. Bir kaynağın kullanımını aktarmak, bütün ürünlerin aynı sözleşmeye sahip olduğunu söylemek değildir.

<a id="sohbetin-temel-parcalari"></a>
## Bu sohbetin temel parçaları — 2026-09-18

**Dar soru:** Kullanıcı, ChatGPT, asistan, Model/LLM, mesaj, Context, Memory, Tool ve Agent/Agentic sözcükleri bu oturumda hangi şeyi gösteriyor?

**Okuma kapsamı:** Aşağıdaki resmi HTML sayfalarının ilgili bölümleri web üzerinden açıldı veya arama sonucunda tam ilgili bölüm metni alındı. Erişim tarihi 2026-09-18; bütün bağlantılı belgeler okunmadı. Teknik mimari, hesap ayarı, tarayıcı ekranı veya paket davranışı testi yapılmadı. Model Spec'in belirtilen sürümü yalnız kaynak terminolojisi için kullanıldı; repository kontrol dosyası yapılmadı.

| Anahtar | Kaynak / okunan bölüm | Gözlem ve sınır |
|---|---|---|
| **O1** | [What is ChatGPT: FAQ](https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq), What is ChatGPT / Where can I use ChatGPT / How do I start my first chat | Asistanın web erişimini, mesaj kutusunu ve sohbet kullanımını anlatır. Kullanıcının hangi tarayıcıyı veya ürün kipini seçtiğini göstermez. |
| **O2** | [Getting started with ChatGPT](https://openai.com/academy/getting-started/), What is ChatGPT / Start your first conversation | ChatGPT'yi LLM tabanlı konuşma asistanı, prompt'u kullanıcı girdisi olarak anlatır. Model–asistan ilişkisine giriş sağlar; özel model sürümü veya sunucu topolojisi açıklaması değil. |
| **O3** | [Model Spec, 2025-12-18](https://model-spec.openai.com/2025-12-18.html#definitions), Definitions: Assistant, Conversation, Tool ve uzun sohbet sınırı | Modelin asistan tarafını üretmesi, araç sonucunun modele dönmesi ve uzun geçmişin eksik sunulabilmesi açıklanır. Model/assistant o belgenin bağlamında yaklaşık eşanlamlıdır; ayrı zihinler varsaymıyoruz. Genel Context kapsamı bizim açıklama tercihimizdir. |
| **O4** | [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/), What is an agent / Agent design foundations | Modelin yalnız çıktı üretmesi ile işin yürütülmesini yönlendirmesini ayırır. Agentic'i bu özellik için kullandığımız sıfat olarak seçiyoruz; bu kaynağı evrensel agency standardı veya mevcut ChatGPT kipinin kanıtı yapmıyoruz. PDF yerine HTML bölümleri okundu. |
| **O5** | [Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq), How memory works / memory summary açıklamaları | Etkin ürün hafızasının sonraki yanıtlar için önceki bilgiden yararlanmasını anlatır. Genel Memory işlevi bununla ilişkili ama bu ürün özelliğiyle eşanlamlı değildir. Kullanıcının Memory ayarları bu sayfadan çıkarılamaz. |

**Bu oturumdan doğrudan gözlenenler:** Kullanıcı mevcut ortamı tarayıcı olarak tarif etti. GitHub dosya okuma ve web arama araçları kullanılabilir ve bu tur kullanıldı. Kalıcı kişisel hafızaya yeni kayıt ekleme aracı kapalıdır. Bunlar bütün ürün altyapısını veya hesap ayarlarını denetlemiş olduğumuz anlamına gelmez.

**Yerel anlatım tercihleri:** Ürün, arayüz, konuşmadaki asistan ve öğrenilmiş model birbirine bağlanarak fakat aynı sözcük yapılmadan anlatıldı. Agentic ayrı nesne değil özellik; tek bir araçsız yanıt bu kapasitenin yokluğu sayılmadı. “Tamam yap” mesajı önceki konuşmayla açıklanabildi; bunun için ayrıca kişisel hafıza kaydı iddia edilmedi. Bu açıklama bağımsız bir anlama deneyi veya bütün tanımların doğrulanması değildir.

## Önceki kayıtlar — korunmuş kaynak geçmişi

Önceki kaynak notlarının tam metni [13dbf32d sürümündeki SOURCES.md](https://github.com/batuhanozgun/agentic-os-search/blob/13dbf32df3ce00a8e45739bfcc1c6a90fecab152/concepts/SOURCES.md)'de korunur. Bu tarihsel bağlantı eski kaynak/bölüm/yorum/sınır kayıtlarına götürür; kullanıcı tarafından durdurulan araştırma rotasını yeniden etkinleştirmez. Yeni temel açıklama eski U01–U06'nın bütün okuma iddialarını geriye dönük doğrulamaz.

<a id="model-degisimi-ve-devam-2026-09-18"></a>
### Model değişimi ve devam

[Özgün kaynak notu](https://github.com/batuhanozgun/agentic-os-search/blob/13dbf32df3ce00a8e45739bfcc1c6a90fecab152/concepts/SOURCES.md#model-degisimi-ve-devam-2026-09-18): OA-Agent, OA-Run, OA-Session, OA-Resume, OA-Model, OA-Context, AN-Patterns, CC-Agents ve CC-Models. Yapılandırma/kimlik/çalıştırma ayrımlarının geçmiş dayanağıdır. Bu turun temel ortam açıklaması için yeniden tam SDK araştırması yapılmadı.

<a id="tamamlanma-ve-yayim-2026-09-18"></a>
### Tamamlanma ve yayımlama

[Özgün kaynak notu](https://github.com/batuhanozgun/agentic-os-search/blob/13dbf32df3ce00a8e45739bfcc1c6a90fecab152/concepts/SOURCES.md#tamamlanma-ve-yayim-2026-09-18): OA-End, NIST-VV, NIST-P, Scrum-DoD, GH-Deploy, OA-Approval ve WM-Closure. Güncel temel kavramların otomatik devam işi değildir.

### İlk U01–U06 kayıtları

[Özgün kaynak envanteri ve nitelemeleri](https://github.com/batuhanozgun/agentic-os-search/blob/13dbf32df3ce00a8e45739bfcc1c6a90fecab152/concepts/SOURCES.md#devralınan-kayıtlar-ve-kapsamları), sadeleştirme öncesindeki her U01–U06 dosyasına sabit commit'le döner. Eski URL/tarih listeleri her iddianın gerçekten okunmuş ve doğrulanmış olduğunu kanıtlamaz; gerektiğinde yalnız kullanılacak iddianın dayanağı kontrol edilir.

[Studies kataloğu](../research/studies/CATALOG.md) ve [EXP-002 terim kaydı](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md) arka plandadır. Bu tur yeni study açılmadı veya mevcut study tekrar araştırılmadı. Eski dosyaların diğer sabit yolları [HISTORY](HISTORY.md)'dedir.

## Kayıt kuralı

Gerekli bir kaynak kontrolünde soru, kaynak/bölüm, tarih/sürüm, görülen kullanım, yerel yorum ve sınır aynı dosyada kısaca tutulur. Yalnız bağlantı eklemek okuma sayılmaz. Her terim için ayrı çalışma paketi açılmaz; kapsam dışı eski bulgu güncel referans gibi sunulmaz.
