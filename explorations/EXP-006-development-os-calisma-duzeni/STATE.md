# EXP-006 — Güncel durum ve konuşma planı

**Açılış:** 25 Eylül 2026.  
**Durum:** OPEN / DIALOGUE IN PROGRESS.  
**Kaynak yetki:** [U001](sources/U001.md).  
**Üst amaç:** SOUL'u geliştirecek Development OS'un nasıl bir çalışma düzeni olması gerektiğini karşılıklı konuşarak ortaya çıkarmak.  
**Şimdiki soru:** Development OS'un SOUL'u yaratmak için yaptığı Work nedir; bu Work'ten hangi yapay zekâ rolleri türemelidir?

## Kullanıcı tarafından verilmiş yön

Kullanıcı beş gerekçe sundu: insanın tek başına dosya üretim yükü; kod üretme ihtiyacı; dosyaların ne olacağı/içeriği hakkında düşünce ortaklığı; konuşmaları aşan bilgi ve okuma sürekliliği; çalışma sırasında büyüyen planın, ana ve alt işlerin yönetimi. Foundation'ın dört zemini SOUL kadar onu üretme faaliyeti için de önemlidir.

Bunlar bu konuşmanın başlangıç girdileridir. Kullanıcının gstack/piramit örneği seçilmiş bilgi mimarisi değildir. “Sen ya da Claude Code” ifadesi iki ürünün birlikte kullanılmasını zorunlu kılan karar değildir.

Yetkilendirilen aşama: repodan seçici yararlanarak diyalog ve düşünce geliştirme; önce aktörler. SOUL implementasyonu, Development OS kurulumu, ECC benimseme, runtime/hosting/iletişim yöntemi veya bütün bir görev şeması henüz seçilmedi.

## İlk assistant katkısı — öneri, kullanıcı kararı değil

1. Bu gerekçeler düşünme/üretme ve sürekliliği olan bir çalışma düzenine ihtiyaç gösterir; ayrı ve büyük bir yazılım ürününün önceden tamamlanması gerektiğini tek başına göstermez.
2. Aktör ile rol ayrılmalı. Araştırma, tasarım, yazma, planlama, kayıt ve değerlendirme sorumluluklarının her biri otomatik olarak ayrı aktör gerektirmez. Bu dar konuşmada önce geliştirme işine katılan ana taraflar sayılır; Foundation'ın bütün paydaş alanının tüketildiği iddia edilmez.
3. Kullanıcı ve bir yapay çalışma ortağı, gerekçelerden çıkan başlangıç ikilisidir. Bu, iki aktörün bütün geliştirmeye yeterli olduğunun gösterilmesi değildir. Yapay çalışma ortağı yalnız yazıcı/kodlayıcı olarak düşünülmez; ihtiyaç keşfi ve tartışmaya da katılmalıdır.
4. Ayrı bir değerlendiren/sorgulayan yapay aktör üçüncü adaydır. Kullanıcının üçüncü maddesi tek başına ikinci AI aktörü gerektirmez: düşünce ortaklığı ilk AI ile de kurulabilir. Ayrı değerlendiricinin gerekliliği, hangi hatayı nasıl yakalayacağı ve sürekliliği ayrıca konuşulmalıdır.
5. İnsan amaç/tercih ve anlam değerlendirmesine katılır; kod bilmediğini söylediği kullanıcıyı sistemin teknik doğruluğunu garanti eden son kontrol noktası saymak uygun başlangıç değildir. Yetki ve teknik yeterlik birbirine geçirilmez.
6. ChatGPT/Claude Code adlarından sabit “biri düşünür, öteki uygular” dağılımı veya bağımsız doğrulama sonucu çıkarılmaz. Aynı modelin farklı rollerdeki çalışmaları ile ayrı ürün adları, aktör/rol/bağımsızlık bakımından ayrıca ayrıştırılacaktır.

**Güncel aktör çerçevesi:** Kullanıcı iki aktörle ilerlemeyi seçti: **insan** ve **yapay zekâ**. Alt ajanlar veya farklı model/oturum örnekleri şimdilik yeni aktör sınıfları sayılmıyor; ihtiyaç olursa bu ayrım yeniden açılabilir. Roller aktörlerden ayrı ve Work'e göre türetilecek.

## Çalışma planı ve sonraki yetkili hareket

- Başlangıç: U001'in görünür kaynak aktarımını korumak ve bu pakete keşif yolu açmak.
- Şimdiki iş: aktörleri ve onları ayırma gerekçelerini kullanıcıyla konuşmak. Özellikle çalışma ortağı ile ayrı değerlendirme sorumluluğu arasındaki ayrımı açmak; önceden çok-ajanlı kadro kurmamak.
- Sonraki yetkili hareket: kullanıcının bu çerçeveye cevabından devam etmek; maddi değişen görüşleri öneri/itiraz/kabul ayrımıyla korumak.
- Yeni soru ortaya çıkarsa konuşmanın çalışma planına eklenebilir; bu, otomatik uygulama veya ayrı araştırma kampanyası yetkisi değildir.

## Diğer çalışmalarla sınır

EXP-001–005 düşünce ve ders girdileridir; eski görevler otomatik yeniden başlamaz. [DEVOS-002](../../development-os/attempts/002/README.md) ayrı denemenin kendi kayıt alanıdır; EXP-006 onu silmez, tamamlandı saymaz veya kurulumunu sürdürmez. Bu konuşmanın devamı önce buradaki aktör sorusudur, 002'nin eski next-step'i değildir. Foundation, studies, concepts ve agent-control durumları bu paketle değiştirilmez.

## Arşiv kapsamı ve sınırlamalar

Başlangıç kaynak kapsamı yalnız U001'dir. Assistant önerileri yukarıda türetilmiş çalışma notudur; nihai yanıtın birebir transkripti, tüm ara bildirimler veya araç günlükleri arşivlenmiş değildir. Bu paket henüz kapanmış/tam konuşma arşivi değildir. Önceki explorations topluca tam okunmadı; gerçek seçici okuma kapsamı [INDEX](INDEX.md)'tedir. Canlı çok-aktör yürütmesi, ortam yeterliği veya bağımsız değerlendirme testi yapılmadı.


## İlk netleşen rol ayrımı — insan / müşteri

Kullanıcı ile yapılan tartışmada, insan aktörünün **müşteri** rolündeki çekirdeği iki başlıkta netleşti:

- **Yetki:** Yapay zekânın hangi amaç ve sınırlar içinde hareket edebileceğinin meşru kaynağı insandır. Bu, insanın bütün önemli kararları tek tek vermesi gerektiği anlamına gelmez; Development OS mümkün olduğunca bu karar yükünü üstlenebilir, fakat kendi yetkisini kendisi üretemez.
- **Kabul:** Ortaya çıkan sonucun teknik olarak doğrulanması ayrı bir konudur; “bu benim ihtiyacımı karşılıyor ve teslimi kabul ediyorum” hükmü müşteride kalır.

Önceki “amaç, tercih, yön, kapsam, trade-off” gibi başlıklar müşteri rolünün ayrı ayrı devredilemez sorumlulukları olarak tutulmuyor. Bunların büyük bölümü Development OS tarafından hazırlanabilir, çözümlenebilir veya kararlaştırılabilir; kritik sınır yetkinin kaynağı ve nihai kabul makamıdır.

Bu, insan aktörünün bütün olası rollerinin tanımı değildir. Partner, yönetici, uzman, sahip/principal benzeri başka insan rolleri ayrıca tartışılabilir. `EXP-006_Context` kullanıcıyla içeriği birlikte kararlaştırılana kadar boş tutulacaktır.


## RPD ile Work keşfine geçiş — 25 Eylül 2026

Kullanıcı, yapay zekâ rollerini jenerik adlarla çıkarmak yerine önce Development OS'un yaptığı işi tanımlamayı istedi. Bu nedenle konuşma Actors'tan Work keşfine geçti; roller daha sonra Work–Actors ilişkilerinden türetilecek.

Yöntem olarak Özyinelemeli Önkoşul Keşfi (RPD) kullanılacak. Kullanıcının bu turda yeniden sağladığı `ozyinelemeli_onkosul_kesfi_kavramsal_temel.md` ve `RPD_Sureklilik_Tasarimi_v0_1.md` tam kaynak olarak okundu; Research'teki `research/studies/recursive-prerequisite-discovery/META.md`, `ASSESSMENT.md` ve ilgili 2026-09-08 RPD entegrasyon sözleşmesi de geri çağrıldı. RPD burada doğrulanmış standart değil; hedeften gerekli koşullara ve başlanabilir işe doğru ilerleyen çalışma yöntemi olarak kullanılacak. Süreklilik tasarımı hazır Development OS mimarisi olarak ithal edilmeyecek.

**Kök hedef:** Development OS, müşterinin yetki sınırları içinde çalışarak SOUL'u ortaya çıkarabilecek bir çalışma düzeni olmalıdır.

**Çalışma kuralı:** Development OS tek turda tamamlanmaya çalışılmayacak. Önce kök hedefin hemen altındaki gereklilikler çıkarılacak; kullanıcıyla değerlendirildikten sonra seçilen gerekliliklere katman katman inilecek. Erken rol, araç, dosya yapısı, çoklu-agent veya runtime seçimi yapılmayacak.

**Sonraki yetkili hareket:** kök hedef için ilk önkoşul katmanını kullanıcıyla tartışmak. `EXP-006_Context` hâlâ boş tutulacaktır.
