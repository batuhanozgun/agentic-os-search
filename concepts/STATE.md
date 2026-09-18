# Concepts — Güncel Durum

**Tarih:** 2026-09-18. **Durum:** Model değiştirme ve yeni oturumda devam üzerine ilk sınırlı birlikte-kullanım incelemesi tamamlandı. Güncel yerel tercihler WORKING'de; gerçekten okunan belge bölümleri SOURCES'ta. Bütün kavramların kapanışı veya canlı sistem doğrulaması değildir.

## Amaç ve son yetki

Amaç kaynaklarla bağlantılı ortak konuşma zemini kurmak; terim sayısı büyütmek veya SOUL mimarisi tasarlamak değildir. Kullanıcının “Tamam. devam et.” yönü, önceki plandaki model değişimi ve oturumda devam örneklerini incelemeyi açtı. Çalışma tanımlarını seçip gerekçeli düzeltme sorumluluğu assistant'tadır; tek tek terim onayı kuyruğu yoktur.

## Bu turda ne değişti?

[WORKING](WORKING.md#model-degisimi-ve-devam) içinde aynı tanım/yapılandırma, aynı kimlik, aynı rol, aynı Session ve aynı Run ayrı iddialar olarak açıklandı. Model seçimi değişirken katılımcı kimliğinin hangi anlamda korunabileceği; yeni Session'a iş bilgisi aktarımı ile askıdaki Run'ın sürdürülmesinin farklı olduğu ele alındı.

Run'ın herhangi bir durma noktasında zorunlu bittiği ifadesi düzeltildi. Session'ın tek Agent veya zorunlu kalıcılık anlamına gelmediği açıklandı. Context'in modele sunulan bilgi ile yerel kod verisi ayrımı geri getirildi. Agent/Model/LLM/Actor/Role/Identity ve Tool/Runtime ifadeleri bu küme için sadeleştirildi; kalan numaralı taslaklar yerlerinde korunuyor, topluca doğrulanmış sayılmıyor.

[SOURCES](SOURCES.md#model-degisimi-ve-devam-2026-09-18) bu tur gerçekten açılan OpenAI Agents SDK, Anthropic örüntü yazısı ve Claude Code belge bölümlerini; gözlem, yerel yorum ve sınırlarıyla taşır. Önceki U03–U06 kayıtlarının tamamı bu okumayla onarılmış değildir.

## Gerçek sonuç ve açık sınır

İki başlangıç cümlesi artık hangi şeyin değiştiği veya sürdürüldüğü belirtilerek açıklanabiliyor. Kaynaklardaki farklı yaşam döngüleri tek şemaya zorlanmadı. Örnek/karşı örnekler metin ve belge karşılaştırmasıdır; SDK çalıştırması, model geçiş performansı, bağımsız reviewer veya kullanıcı-anlama deneyi yapılmadı.

Kimlik devamının bütün ürünlerde nasıl sağlanacağı, her modelin ikame edilebilirliği, uzun işin devam bilgisinin tam şeması ve evrensel agency eşiği açık. Bunlar otomatik yeni araştırma kuyruğu değil, ilgili kullanımda gerektiğinde açılacak sınırlar. Bir sonraki tur bu tamamlanmış dar incelemeyi baştan tekrarlamaz.

## Devam noktası

Sonraki olağan kavram devamında önce bu sonucu devral; ardından “İşi bitirdi; sonucu yayımlayabilir” cümlesiyle Work state–Completion–Verification–Authority/Permission ilişkisini gerektiği kadar incele. Bu örneği henüz sınanmış sayma. Başka somut kullanıcı ihtiyacı yönü değiştirebilir; yeni onlu liste veya bütün taslağı yeniden kurma zorunluluğu yok.

Tanımın açık kalan genel sorularını tamamen kapatmayı beklemeden kullanılabilir yerel anlamla ilerle. Kaynak farklı bir sözcük kullanırsa onu yeniden adlandırma; eşlemeyi ve kapsamı açıkla. Düzeltmeler aynı WORKING/SOURCES dosyalarına, mevcut iş STATE'e işlenir.

## Repository ve kapanış

Altı dosyalı düz yapı ve `main` tek güncel çalışma alanı olarak korunur. Önceki branch temizliği [HISTORY](HISTORY.md)'de tamamlanmış kayıttır; bu tur yeniden bakım veya yeni branch açılmaz. Değişiklik kapsamı yalnız WORKING, SOURCES ve bu STATE'tir; INDEX, METHOD, HISTORY ve diğer araştırmalar korunur.

Başlangıç main `4a2c5f7b5ad887b7da5946953b94576ed53105ed`. Yayın aynı parent üstünde hazırlanan üç dosyalık commit'in force kullanılmadan ilerletilmesi ve main geri okumasıyla kontrol edilir; gerçek commit kimliği Git geçmişinden bulunur. Bu kontrol kavram doğruluğu değil aktarım/kapsam kontrolüdür.

**Bu turun dönüş koşulu:** kaynaklı bulgular, yerel tanım düzeltmeleri, iki cümlenin yeni açıklaması, karşı örneklerin sonucu ve açık sınırlar kullanıcıya sunulur. Bunun ardından otomatik yeni araştırma dalına geçilmez.
