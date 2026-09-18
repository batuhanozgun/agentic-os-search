# Kavram Çalışması — Yöntem v0.2

**Tarih:** 2026-09-18. Bu belge yalnız `concepts/` çalışma programının yöntemidir. Güncel iş/yetki [STATE](STATE.md), amaç ve kullanıcı yönü [PURPOSE](PURPOSE.md), yürütme planı [PLAN](PLAN.md)'dedir. Agent-control veya nihai kavram şeması değildir.

## Amaç ve çalışma birimi

Amaç terim listesini tüketmek veya dünyanın tek doğru tanımını bulmak değil; kaynaklarla bağlantılı, karşılıklı anlaşılmış ve yeni oturumlarda geri bulunabilir yerel kullanımlar oluşturmaktır: **“Biz bu ifadeyi, şu bağlamda, şu anlamda kullanıyoruz.”**

Başlangıç bir terim, ifade, somut cümle veya anlam uyuşmazlığı olabilir. Çalışma birimi gerektiğinde bunun etrafındaki küçük bağlantılı kavram kümesidir. Bir terimi bütün komşularından bağımsız bitirme veya bütün terimleri bitirdikten sonra referansa geçme zorunluluğu yoktur. Kaynaklar farklılaşabilir; her terimin her kaynakta farklı olduğu da peşinen varsayılmaz.

## Üç kayıt düzeyi; tek yönlü üç büyük faz değil

| Yüzey | Ne taşır? | Neye dönüşmez? |
|---|---|---|
| `research/` | Kaynak kullanımı, örnekler, karşı örnekler, okuma sınırı ve ortaya çıkan sorular. | Kaynağın sözü kendiliğinden bizim tercihimiz olmaz. |
| `synthesis/` | İlgili kullanımların/işlevlerin karşılaştırılması, gerekçeli ilişki yorumları ve ortak kullanıma yönelik aday açıklamalar. | Sentez veya aday, kabul edilmiş referans değildir. |
| `reference/` | Belirli kapsamı ve açık karşılıklı değerlendirmesi kayıtlı yerel kullanımlar. | Evrensel tanım, kaynak düzeltmesi veya SOUL mimarisi değildir. |

Bu ayrımlar aynı küçük çalışma döngüsünde korunabilir. Her adımda ayrı dosya, her bağlantıda yeni paket, her geçişte ayrı oturum gerekmez. Ayrı kayıt gerektiğinde mevcut yüzeyden bağlantı verilir; aynı bulgu veya current state bağımsız kopyalarla yönetilmez.

## İşleyiş: odak → keşif → gerekli ayrımlar → ortak kullanım

### 1. Açık anlam sorusundan başla

Güncel STATE ve eldeki çalışmayı geri kazan. Hangi cümlede neyin karışabileceğini belirt: nesne mi, işlev mi, kapsam mı, teknik ad mı, belirli yürütme mi? Araştırmayı SOUL'un henüz seçilmemiş yapısından veya hazır bir kelime ağacından türetme.

İlgili mevcut araştırma varsa katalog → seçilen META/STATE/INDEX → gereken bulgu/kaynak yolunu kullan. Geçmiş diyalog, bizim neyi kastetmiş olabileceğimize dayanak olabilir; dış dünyanın tanımı için kanıt değildir. Mevcut sonuçları sırf yeni oturum açıldı diye yeniden üretme.

### 2. Kaynakları ve ortaya çıkan bağlantıları birlikte incele

Soruyu aydınlatacak ilgili gelenek ve uygulamalara başvur. Gerektiğinde akademik birincil kaynak, standardın özgün metni, ürün belgesi veya gerçek uygulama kullan. Aynı kaynağı tekrar eden sayfalar bağımsız destek değildir. Sabit kaynak sayısı veya tur kotası yoktur; ilk tur sonunda mutlaka tanım kabul etme zorunluluğu da yoktur.

Terim araştırılırken başka terimler, işlevler, ayrımlar ve ilişki soruları çıkabilir. Bunları peşinen bileşen, tür veya zorunlu bağımlılık sayma. Örneğin bir işlevin görülmesi onun ayrı bir agent, servis ya da dosya olması gerektiğini göstermez. Gerekirse henüz isim koymadan açık bir cümleyle tarif et.

Bir bağlantıyı kısa biçimde geri bulunabilir tut: **nerede karşılaşıldı; neyi ayırmaya yarıyor; mevcut anlam sorusuna etkisi ne; hangi statüde?** Yeni isim keşfetmek, araştırılmış kavram veya kabul edilmiş karşılık üretmek değildir.

### 3. Komşuyu gerektiği kadar aç; asıl soruya dön

Şunu değerlendir: **“Bu ayrımı çözmeden şu anda aynı şeyi konuşabilir veya kapsamı açık bir yerel kullanım önerebilir miyiz?”**

- Cevap hayırsa ya da sonuç açısından maddi belirsizlik varsa komşuyu belirli bir soruyla aç. Neyi çözmek için açıldığını ve hangi soruya dönüleceğini kaybetme.
- Ayrım yararlı ama şu an engel değilse, neden ertelendiği ve ne zaman geri çağrılacağıyla gündemde tut.
- İfade yalnız kaynağa özgü API/sınıf/ürün adıysa onu özgün bağlamında koru; sırf karşılaşıldı diye genel referans maddesi yapma.

Bunlar iş yönlendirme seçenekleridir, değişmez kavram sınıfları değildir. Aynı ifade farklı sorularda farklı önem taşıyabilir. Önceki assistant'ın “zorunlu komşu” dediği listeye ayrıcalık verme; gerekliliği mevcut soruda gerekçelendir.

Dairesel bağımlılık görünürse bütün düğümleri sırayla bitirmeye çalışma. Küçük kümeyi birlikte açıkla; ayrılabilen kısmı değerlendir, kalan sınırı görünür bırak. Bir komşunun tam araştırmasını sessizce yeni ana işe dönüştürme.

### 4. Yeterli zeminde erken aday üret ve birlikte değerlendir

Araştırılabilir başka soru bulunması tek başına devam gerekçesi değildir. Somut kullanım farkları görünürse, önerilecek anlamın kapsamı açıklanabiliyorsa ve kalan belirsizlik açık sınır/niteleme ile taşınabiliyorsa yerel referans adayını tartışmaya getir. Yeterlilik yalnız başlık sayısıyla veya “bir tur yaptık” diye ilan edilmez.

Adayı kaynak kullanımlarından ayır. Bir varsayılan anlam, birden çok nitelenmiş anlam, başka bir ifade tercihi veya şimdilik açık bırakma mümkün sonuçlardır. Belirsizliği azaltmak için her şeye yeni ad verme; sıradan açıklayıcı bir cümle yeterliyse onu kullan.

Kullanıcıyla somut bir cümle/örnek üzerinden aynı nesne ve kapsamın konuşulduğunu değerlendir. Gerekli komşu kavramlar da aynı görüşmede ele alınabilir; önce Agent tamamen bitsin, sonra Model başlasın gibi bir sıra dayatılmaz. Ortak anlamda anlaşmak, önerilen sistemi beğenmek veya tasarımını onaylamakla aynı şey değildir.

### 5. Kabul edilen kapsamı kaydet; kaynağı yeniden adlandırma

Kabul edilmiş kayıt için belirli açıklama/kapsam, kaynak ve sentez dayanakları, assistant'ın gerekçeli önerisi ve kullanıcının **o açıklamaya yönelik** açık değerlendirmesi bulunmalıdır. Yönteme onay, genel memnuniyet, sessizlik veya bir kelimenin tekrar kullanılması tanım kabulü değildir. Kısmi uzlaşmada yalnız üzerinde anlaşılan kısım kabul edilmiş gösterilir.

Yerel tercihle dış dünyaya ilişkin teknik hata doğrulanmış olmaz. Örneğin bir sistem ile onun kullandığı şeyin aynı olduğu iddiası, yalnız o kelimeyi tercih ettiğimiz için doğru sayılmaz. Kaynağa aykırılık varsa kapsamı/nitelemeyi düzelt veya iddiayı yeniden araştır.

Kaydın gerektirdiği kadar bilgi tut: anlam ve kullanım bağlamı; neyi kapsamadığı; somut örnek; önemli komşu ayrımları; kaynaklara eşleme; açık kalanlar; tam öneri/değerlendirme bağı ve değişiklik tarihi. Ağır şema veya puanlama zorunlu değildir. Aday açıklama `synthesis/` içinde veya ilgili çalışma belgesinde aday olarak kalabilir; `reference/INDEX.md` kabul durumunu açıkça ayırır.

### 6. Kullanımda sınayıp gerekirse yerel olarak yeniden aç

Kendi açıklamalarımızda ilgili kabul edilmiş kullanım referans alınır. Dış kaynağı aktarırken kaynağın kendi anlamı korunur; farklıysa ilişki, ilgili belge/bölüm/sürüm üzerinden açıklanır. Kod/API adı, alıntı ve özgün dosya adı değiştirilmez. Eşleme daha geniş/dar, kısmi veya çözülememiş olabilir; her kaynak aynı anlama zorlanmaz.

Yeni kaynağın yalnız başka bir sözcük kullanması otomatik yeniden araştırma veya kabul değişikliği gerektirmez. Yeni kanıt ya da somut kullanım, mevcut referansın yanıltıcı olduğunu, önemli bir ayrımı gizlediğini veya iki tarafı farklı sonuçlara götürdüğünü gösteriyorsa etkilenen kısmı yeniden aç. Önceki anlamı, değişiklik nedenini ve etkilenen bağlantıları koru; geçmiş belgeleri sessizce bugünkü anlama çevirme.

Bir referansın bulunması fiilen doğru kullanıldığını kanıtlamaz. Her tur bütün corpus'u yüklemek yerine ilgili anlamı ve gerektiğinde kaynağını geri çağır. Referansı olmayan kelime yasak değildir; önemli belirsizliği açıklayarak konuşmaya devam edilebilir.

## Kanıt ve kayıt disiplini

Kaynak kaydı; yazar/kurum, tarih/sürüm, bölüm ve gerçek okuma derinliğini; doğrudan tanım ile kullanım yorumunu; zorunlu görülen nitelik ile örnek/sık rastlanan niteliği; somut örnek/karşı örneği ve araştırılmayan sınırı ayırır. Kaynağa sadakat kaynağın doğruluğu veya sistemin etkililiği değildir. Güncel ürün davranışı yük taşıyorsa birincil kaynak yeniden doğrulanır.

Kökenleri karıştırma: doğrudan dış kaynak gözlemi, mevcut study bulgusu, eski diyalog kullanımı, yeni kullanıcı örneği, assistant çıkarımı ve kabul edilmiş yerel tercih ayrı statülerdir. Gündem kaydı kaynak araştırmasının yerine geçmez. Keşfedilen bağlantının adlandırma mı, benzerlik mi, parça mı, kullanım mı, gerçekleştirme mi olduğu ayrıca gerekçelendirilir; bunlar peşinen bir ilişki taksonomisi değildir.

## Yetki, durma ve oturumlar arası devam

Bu programın olağan araştırma/değerlendirme devamı yetkilendirildiğinde, gereken komşuya sınırlı inmek, karşılaştırmak ve aday önermek aynı işin adımları olabilir; her küçük adım için ayrı onay istenmez. Buna karşılık yerel kullanımın kabulü görünür kullanıcı değerlendirmesi ister. Yeni ana araştırma programı, SOUL/Development OS tasarımı, implementasyon ve agent-control değişikliği otomatik devam değildir. Mevcut turun daha dar sınırı STATE'te korunur.

Anlamlı bir ara sonuçta kullanıcıya dön. Uygun olduğunda referans adayı getir; yeterli değilse yalnız hangi somut belirsizliğin bunu engellediğini ve hedefli sonraki soruyu göster. “Başka kaynak var” veya “bütün komşular bitmedi” tek başına erteleme nedeni değildir.

Tur sonu STATE; mevcut odak, kullanılan sonuç, açık anlam sorusu, gerekiyorsa komşuya iniş/dönüş noktası, öneri/kabul ayrımı ve sonraki yetkili sorumluluğu taşır. Ayrıntıyı kendi kaydına bağlar; her düzeyi STATE'e kopyalamaz. Envanter iş sırası değildir. Yeni oturum bu durumu devralır; kendiliğinden daha fazla kaynak taramaya veya önceki örnek tanımı benimsemeye başlamaz.

## Yöntemin değerlendirilmesi ve değişikliği

Başarı ölçütü terim/dosya sayısı değil; yeni bir somut örnekte anlam farkını fark edebilmek, kaynağı bozmadan anlatabilmek ve değerlendirmeyi aynı öneriye bağlayabilmektir. Aynı assistant'ın tekrar okuması bağımsız davranış deneyi değildir; ölçülmemiş iletişim başarısı garanti edilmez.

v0.2, U01 sonrasındaki kullanıcı düzeltmesini işler: tekil terim kuyruğu yerine gerekçeli bağlantılı inceleme, ihtiyaca göre komşu derinliği ve yeterli zeminde erken yerel referans. Üç kayıt düzeyi, kaynak sadakati, karşılıklı kabul ve tasarım sınırı korunur. Önceki örnek Agent tanımı, model adları ve komşu öncelikleri benimsenmedi. Değişiklik kapsamı ve gerçek kontroller [uyum kaydında](checks/METHOD-ALIGNMENT-2026-09-18.md) tutulur.
