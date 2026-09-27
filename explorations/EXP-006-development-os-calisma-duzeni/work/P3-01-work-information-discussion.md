# P3-01 — İş merkezli işbirliği ve bilgi döngüsü: tartışma taslağı

**Üst iş:** [WORK/P3](../WORK.md). **Tarih:** 27 Eylül 2026.  
**Başlangıç:** `agentic-os-search@6a55f90948d0d8b0e78059f6d404e11e550b4161`.  
**Statü:** DISCUSSION BASELINE / CANDIDATE / NOT ACCEPTED. P3 açıldı; tamamlanmadı. Bu metin konuşacağımız başlangıç önerisidir; seçilmiş mimari, kurulmuş mekanizma veya çalışan DevOS değildir. P4–P6 başlamadı.  
**Kaynak kullanıcı yönü:** “en önemli kısım burası. burada araştırma reposu sana bir çok örnek ve bir çok metodoloji verebilir. burayı biraz derin konuşalım. hemen karar verme, bana bir yapı sun, birlikte değerlendirelim. senin sunduğunu baz alalım.” Bu, görünür tek mesajın aktarımıdır; bütün konuşma export'u değildir.

## 1. Önerinin omurgası

**Ortak bir iş ve bilgi zemini üzerinde, ihtiyaç etrafında kurulan çalışma halkaları.**

Sabit sırayla 16 rolü çalıştıran bir bant veya bütün kararları veren bir ana yönetici önermiyorum. Ortak amaç ve çalışma durumu korunur; gereken katkılar ilgili iş/soru etrafında toplanır. Araştırma, planlama, tartışma, uygulama, inceleme ve bilgi bakımı gerçek çalışma biçimleridir. Aynı kalıptan geçmeleri veya hepsinin ayrı ajan olması gerekmez.

Bu öneri P2'nin DR01–DR16 sözleşmelerini başlangıç girdisi yapar; değiştirilmez kadro kabul etmez. SOUL'un ilk teknik işini seçmez. Hangi ihtiyacın önce açılacağını hedefi ve birikimi devralacak DevOS düzeni keşfeder. K1 talep→çalışma→yanıt→kullanım ve K2 rutin insan tetiklemesi olmaması sınırları korunur.

## 2. Birlikte çalışan üç mantıksal unsur

| Unsur | Ne taşır? | P2 rollerinin aday katkısı |
|---|---|---|
| **Yaşayan iş ağı** | Amaç, gerekli koşullar, aday/etkin işler, açık sorular, bağımlılıklar, kararlar ve üst hedefe katkı. Hazır backlog veya yalnız görev listesi değil. | DR01 planı bütünleştirir; her rol ihtiyaç/itiraz üretebilir. DR06 yürütme, bekleme ve devir durumunu izler. |
| **İşe özgü çalışma halkası** | Bir sorunun veya teslimatın sahibi ve o iş için gereken uzman katkıları. Halkadaki roller araştırabilir, birbirini sorgulayabilir, iş açılması önerebilir. | İlgili DR02/03/04/05 vb. teslimat sahibi; DR16 araştırma, DR13 güvence; DR06 akış koordinasyonu. Her iş bütün rolleri çağırmaz. |
| **Kalıcı bilgi ve role özgü bağlam** | Kaynaklar, öneriler, karar gerekçeleri, ürün sürümleri, kanıtlar ve bitmemiş çalışmanın devam noktası. Bunlardan her tüketiciye yeterli ve yetkili görünüm hazırlanır. | Üretici kendi içeriğinden; DR07 yaşam döngüsü bütünlüğünden; DR08 o işteki bilgi görünümünden sorumludur. |

Bunlar üç servis, klasör, veri tabanı veya üç ajan değildir. Aynı bilginin üç ayrı canonical kopyasını üretme önerisi de değildir. Ortak zemin, bütün ajanlara bütün geçmişin gönderilmesi anlamına gelmez.

İş ağındaki **bir işten keşfedilme**, **onu engelleyen önkoşul olma**, **bir karardan etkilenme** ve **aynı üst sonuca katkı verme** ilişkileri eşitlenmez. Yeni araştırma ihtiyacı mevcut işten doğabilir fakat yalnız gerçekten gerekli olduğu karar/işi bekletir; bütün ekibi otomatik durdurmaz.

## 3. Başlangıç ve tekrar eden çalışma mantığı

Başlangıçta hedef, kısıtlar, mevcut araştırma ve yetki kapsamı ekibe devredilir. DR06 devralma/etkinleşme işini; DR08 ilgili bilgi görünümünü; DR01 gereken işleri keşfetme ve bütünleştirmeyi taşımaya adaydır. Gerekli uzmanlar ve inceleme bu keşfe katılır. Bu sorumlulukların ilk kez nasıl yetkilendirildiği ve çalıştırıldığı P4/P5 bootstrap tasarımının yüküdür; birbirini sonsuz döngüyle yetkilendiren roller varsayılmaz.

Sonraki çalışma her seferinde sıfırdan hedef tanımı istemez. Yeni ihtiyaç, sonuç, itiraz veya değişiklik ilgili işi yeniden etkinleştirebilir. Mevcut bilgi yeterliyse doğrudan ilerlenir; bilgi açığı varsa araştırma, belirsiz tercih varsa gerekçeli karar, uygulama gerekiyorsa üretim, kanıt gerekiyorsa sınama devreye girer.

Aday ortak döngü:

**ihtiyacı fark et → hangi katkının gerektiğini belirle → uygun bilgi ve sorumlu ile çalış → sonucu değerlendir → gerekçeli karara/ürüne yansıt → etkilenen iş ve bilgiyi güncelle.**

Bu zorunlu altı aşamalı workflow değildir. Birkaç halka birlikte gerçekleşebilir, tekrar edebilir veya ilgili işte gerekmeyebilir. P3'ün bütün üretim/recovery/devralma ayrıntıları bu ilk taslakla çözülmüş değildir.

## 4. Somutlaştırma: bir tasarım sırasında araştırma ihtiyacı

Bu bir **varsayımsal tasarım örneğidir**; SOUL'un ilk işi veya gerçek deney değildir.

1. Kapasite Tasarımcısı, üzerinde çalıştığı karar için eksik bir bilgi saptar. Talebi yalnız “araştır” diye değil, **hangi soruya, hangi karar için, hangi kapsamda cevap gerektiği** ile açar. Üst iş ve geri dönülecek nokta korunur.
2. Çalışma Koordinatörü talebin uygun sorumluya ulaşmasını ve kaybolmamasını sağlar. Bağlam Kurucusu mevcut kaynakları/kararları hazırlar. Rol/Katılım ve Ortam katkıları gerçekten gerekli oldukları yerde etkinleşir; her soru için ayrı bir tören yapılmaz.
3. Araştırmacı bulguyu kaynak, sürüm/zaman, sınır ve belirsizlikle döndürür. Kaynağa ulaşamadıysa eksikliği bildirir. İletim doğrudan veya aracılı olabilir; teknik yol P4'tedir.
4. Talep sahibi sonucu ilgili kararda **nasıl kullandığını veya neden kullanmadığını** gerekçesiyle gösterir. Araştırma teslimatı kapanmış olsa da üst karar/iş açık kalabilir. Kararı etkileyen güvence gerekiyorsa uygun inceleme ayrıca yapılır.
5. Karar ve dayanak kaydı korunur; etkilenen plan, ürün ve bağlam görünümü güncellenir. DevOS normal devamı işletir; Batu'nun “şimdi tasarımcıya dön” demesi gerekmez. Bu son iddia gereksinimdir, gösterilmiş çalışma başarısı değil.

Talep sahibi açık ihtiyacın sonucunu takip eder; araştırmacı bilgi teslimatını; koordinatör çağrı/devir/bekleme yükünü taşır. Bunlar tek bir “her şeyden sorumlu” role eritilmez. Mevcut iş içinde çözülen küçük danışma mutlaka ayrı kalıcı Work dosyası gerektirmez; ayrı sahibi, beklemesi, bütçesi, bağımlılığı veya devri olan katkı ayrı izlenmeye adaydır. Kesin eşik tartışmaya açıktır.

## 5. Akış sahipliği ile karar sahipliği

**Başlangıç tercihim: koordinatör akışın sahibi olsun; bütün teknik kararların sahibi olmasın.** Bu, tek merkezi mesaj sunucusu veya tek lead-agent kararı değildir. Koordinasyon sorumluluğu ile iletişimin fiziksel topolojisi ayrıdır.

Aday ayrım:
- İş gerekliliği ve planın bütünü: DR01, diğer rollerin katkılarıyla.
- Belirli kapasite tasarımı: ilgili uzmanlıkla DR02; alanlar arası bütünlük: DR03.
- Bilgi sorusunun sonucu: DR16; bunun ürün/tasarım tercihi olarak kullanımı ilgili karar sahibinde.
- Kanıtın desteklediği hüküm: DR13; idari onay veya çoğunluk oyu olguyu doğru yapmaz.
- Kapsam/yetki çatışması: DR12; yalnız gerçek principal yetki/tercih ihtiyacı Batu'ya döner.

Roller anlaşamadığında ilk aday yol daha fazla konuşmayı zorlamak değil, anlaşmazlığın türünü ayırmaktır: eksik/çelişkili olgu için kaynak veya deney; tasarım trade-off'u için yetkili alan kararı; açık kalite/izin ihlali için ilgili durdurma/geri dönüş. Görüş birliği otomatik kanıt değildir. Her itiraz veto değildir; her itirazın kaybolmadan bir karşılığı olmalıdır. Kesin karar/veto/itiraz sözleşmesi henüz seçilmedi.

**Risk:** Çok merkezi düzen, koordinatörü darboğaz ve görünmez düşünce filtresi yapabilir. Sınırsız serbest iletişim ise çelişkili karar, yinelenen iş ve iz kaybı yaratabilir. Öneri, ortak çalışma durumu ve açık sorumluluklarla izlenen, iş içinde uygun doğrudan/aracılı etkileşimdir. Bunun yeterliği henüz sınanmadı.

## 6. Bilginin sonraki işe dönüşmesi

Bilgi düzeninde en az şu ayrımlar korunmalı: kaynak/gözlem, yorum/öneri, yetkili karar, uygulanmış ürün ve bunlara ait kanıt. Ayrım ayrı klasör zorunluluğu değildir.

Her önemli sonuç, hangi soru/işten geldiğini ve hangi kaynak/karar/ürün sürümü için geçerli olduğunu taşımalı. Bir kayıt güncellendiğinde eski bilgiyle çalışan tüketicilerin etkilenip etkilenmediği ayrıca değerlendirilmelidir. İlgili güncellemenin o role görünür olması ve gerekçesinde kullanılması, kaydı güncellemekten farklıdır. Her değişiklik bütün ajanları yeniden başlatmayı gerektirmez.

SOUL ürün dosyaları ile DevOS'un kendi çalışma kayıtlarının amaçları ayrıdır; aralarında iz sürülebilir ilişki bulunur. Bitmemiş keşif, açık soru, beklenen yanıt ve geri dönüş noktası oturum devrinde korunmalıdır. Bu, bütün sohbeti her yeni role yığmak veya tek bir kısa özetin yeterli olduğunu varsaymak değildir. Kaynak, karar ve kanıt ilişkisini saklamak da bağımsız nedensellik kanıtı sayılmaz.

## 7. Araştırmalar öneriyi nasıl değiştirdi?

| Dayanak | Taslağa somut katkısı | Alınmayan/kanıtlanmayan |
|---|---|---|
| Work Foundation | Araştırma, karar, bakım ve meta-işin Work olması; plan/actual ve completion/outcome ayrımı | Tek evrensel workflow veya bütün dallara birer modül |
| Information integration I1–I5 | Yeterli bilginin varlığı ile aynı tüketiciye erişmesi/kullanılması ayrı; başka ajanın bilgisi otomatik bu ajanın bağlamı değil | Her göreve bütün kaynakları verme veya özetin genel yeterliği |
| RPD assessment | İş parçalamadan önce gereklilik/önkoşul keşfi; yöntem koşulu ile hedef gereği; bitmemiş sorgu ve return-to | Prototip store, fiziksel agent ağacı, yöntem üstünlüğü veya asıl eklerin yeniden okunması |
| Work-management U08/U10 | Yaşayan ağ, anlamı farklı ilişkiler, duruma bağlı etkinleşme, ready/claim/running/done ayrımı | Beads, Flowable, OpenSpec veya Gas Town'u seçmek/birleştirmek |
| Superpowers S03 | İş brief'i, global kısıt, consumer ve kaynak erişimini birlikte taşıyan anlamsal devir | Hazır görev seçiminin doğru olduğu varsayımı, sabit SDLC ve kaynak insan kapıları |

**Okuma izi:** Bu tur Information INDEX/STATE ve `07_selection-dynamics-integration-review/SYNTHESIS.md` (blob `c2b1138ee898d9be8c829c5aa0f160c86eb58aba`) tam; RPD META ve ASSESSMENT (blob `ffd95e71c6f49192d3cdf6ffc2a4d13b1b7a10d0`) tam okundu. ASSESSMENT ilk çıktısındaki kesim son bölüm yeniden getirilerek tamamlandı. U08 synthesis (blob `9bb0886b4bc051240a213bde67e7bc6642da8755`) 1–320 seçici okundu; sonraki enterprise gap/kapanış kısmı bu turun tam okuması sayılmadı.

Work Foundation STATE ve synthesis (`5967c60b7650c0493cfb21813ff894b678a54138`), Foundation STATE/REUSE, studies CATALOG, Work-management META/U10 (`e140a0cac67d41af1d3b45dfdddf1eccedfcc860`) ve Superpowers META/S03 (`f69f5c99aefa2a6a13b4233ae49afd73dc2ce0ca`) bu aynı konuşmadaki tam içeriklerden yeniden kullanıldı. Foundation'ın daha eski synthesis başlıklarındaki pending ifadeleri current STATE'in kabul kapsamıyla birlikte yorumlandı. Bu kaynaklar değişmez araştırma başlangıcı `6a55f90` kapsamındadır; bugünkü dış ürün davranışı ayrıca yeniden doğrulanmadı. Yeni teknik ürün özelliğine veya performans iddiasına dayanılmadı.

Yollar: [Work synthesis](../../../research/soul-foundations/03_ground-deepening/grounds/work/synthesis/WORK-GROUND-AUDIT-SYNTHESIS.md), [Information integration](../../../research/soul-foundations/07_selection-dynamics-integration-review/SYNTHESIS.md), [RPD](../../../research/studies/recursive-prerequisite-discovery/ASSESSMENT.md), [U08](../../../research/studies/work-management-project-control/08-CROSS-UNIT-SYNTHESIS.md), [U10](../../../research/studies/work-management-project-control/10-CLOSURE-EVALUATION.md), [Superpowers S03](../../../research/studies/superpowers/syntheses/S03-intent-planning-and-context-handoff.md).

Bu aynı-assistant kaynak yeniden kullanımı ve aday tasarımdır; bağımsız doğrulama, canlı Claude deneyi veya K1/K2 başarı kanıtı değildir. Aktif kontrol protokolleri araştırma kanıtı yapılmadı. Yeni study/ürün benimseme kararı verilmedi.

## 8. Birlikte değerlendirme ve dönüş

Önce bu başlangıç yapısını kullanıcıyla değerlendir. İlk odak **bir rolün açtığı katkı talebinin nasıl işe dönüştüğü ve akış sahibiyle karar sahibinin nasıl ayrıldığı** olsun. Sonraki tartışmalar bu bazın üzerinde, gerekçeli revizyonla ilerlesin; her tur bütün sistem yeniden tasarlanmasın.

Açıklar: küçük danışma/ayrı Work sınırı; karar ve veto dağılımı; kaynak/brief yeterliği; sürüm değişikliğinin tüketicilere yayılması; kesilmiş/bekleyen taleplerin devri; bootstrap önkoşulları ve gerçek mekanizma. Bunlar çözüldü sayılmaz. P2'ye yalnız somut rol çakışmasında dönülür.

**Durma:** P3 tamamlandı deme; P4'e geçme; alt ajan/takım, dosya şeması veya gerçek SOUL işi seçme. Bu öneriyi kalıcılaştırmak onu accepted karar yapmaz. Registry ve P2 sözleşmeleri bu tur değiştirilmedi.
