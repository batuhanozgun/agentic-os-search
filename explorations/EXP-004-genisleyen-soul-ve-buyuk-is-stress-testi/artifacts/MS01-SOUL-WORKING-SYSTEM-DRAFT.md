# MS01 — SOUL Çalışma Sistemi Taslağı v0.1

**Tarih:** 2026-09-21. **Checkpoint:** A — bütünleşik başlangıç taslağı ve soru-bankası yürüyüşü. **Statü:** PROVISIONAL MECHANISM DRAFT / PARTIAL SYNTHESIS. Bu metin bir yapı önerisidir; kurulmuş sistem, çalıştırılmış simülasyon, nihai mimari kabulü veya yeni T16 değildir. Romanın aynı kurgu üzerinde tam yürüyüşü ve son birleşim değerlendirmesi henüz yapılmadı.

**Başlangıç main:** `0dd58080eeea4ee8c7eaaaef0902d02fce825edc`. Kullanıcının «Anladım. Peki nasıl ilerleyeceksin bundan sonra?» sorusuna verilen MS01 planından sonra «anlaştık. devam et.» yönü bu taslağı başlatır. Yetki, EXP-004 içinde kavramsal mekanizma sentezi ve kaydıdır; gerçek ürün, model deneyi, Foundation/studies/concepts/agent-control değişikliği değildir.

**Birlikte okunacaklar:** [Soru-bankası yürüyüşü](MS01-QUESTION-BANK-WALKTHROUGH.md), [kapsama, açık mekanizmalar ve kaynak defteri](MS01-COVERAGE-AND-OPEN-MECHANISMS.md). [RV01](../reflections/RV01-DIRECTION-REVIEW-AND-MECHANISM-TARGET.md) dönüşün gerekçesi; [SY01](SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md) sorumluluk zemini. Önceki kaynaklar bu taslakla yeniden yazılmaz.

## 1. Birinci tercih: muhakeme ile yürütmenin birlikte kurulduğu SOUL

Bu taslak için **modelin yönlendirdiği, durum ve etki sınırlarının yürütme koduyla korunduğu hibrit düzeni** tercih ediyorum. Sadece uzun talimatla çalışan tek sohbeti de, bütün olası işi baştan tarif eden sabit workflow'u da başlangıç modeli seçmiyorum.

Model, amaç yorumunu, ihtiyaç/yöntem önerisini, kaynak seçimini ve alan üretimini yapar. Yürütme kodu kimlik, sürüm, ayrılmış kaynak, tanımlı izin ve kayıt geçişlerini denetler. Anlamsal kaliteyi bu koddan beklemeyiz. İnsan katkısı ancak gerçekten mevcut rol ve yetkisiyle plana girer. Böylece «SOUL düşünür» ile «hook kontrol eder» arasındaki iş bölümü açık olur.

Ortak kararların kayda geçirilmesi için **mission başına tek mantıksal commit otoritesi** seçiyorum. Birden fazla aktör paralel ürün/öneri hazırlayabilir; ancak shared current state'i birbirinden habersiz değiştiremez. Bu, tek LLM, tek makine, tek thread veya bütün görevlerin sırayla yapılması değildir. İlerideki dağıtık karşılığı ayrı tasarım ister. Şimdilik amaç, yarışan karar ve sonuçları anlaşılır bir kabul sınırında uzlaştırmaktır.

Alternatif olarak çok-yazarlı federatif karar düzeni mümkün; fakat ilk taslakta ortak yetki/sürüm uzlaştırmasını her aktöre dağıtmak yerine bu tek mantıksal sınırı seçiyorum. Bedeli bu sınırın darboğaz veya arıza noktası olabilmesidir. Devralma ve eski yürütücüden gelen geç yazımlar K7'de ele alınır; ölçek üstünlüğü iddia edilmez.

## 2. İlk işi kim başlatıyor? Bootstrap zemini

SOUL, henüz kendisinin oluşturacağı agent'lara ihtiyaç duymadan başlamak zorundadır. Bunun için bazda önceden hazırlanmış şu bileşim varsayılır:

| Başlangıç taşıyıcısı | İlk görevde fiilen yaptığı iş | Varsayım / açık sınır |
|---|---|---|
| **Host Runtime** | Kullanıcı girdisini alır; model çağrısını, araç isteklerini, kayıt işlemlerini ve yeniden giriş olayını yürütür. | Çalışan host ve aşağıdaki kontrol yolları önceden sağlanmış olmalı. Prompt bunları yoktan oluşturmaz. |
| **Bootstrap Actor B0** | Genel amaçlı modelin ilk çalışma rolü; talebi yorumlar, sınırlı kaynak incelemesini ve ilk Work önerisini üretir. | Alan uzmanlığı veya güvenilir açık-uçlu keşif otomatik verilmiş değildir. G01/G02 açıkları bu kapasiteye bağlıdır. |
| **Working State erişimi** | Mission, Work, kaynak ve kararları kayıt kimliği/sürümüyle okur; yetkili geçişleri kalıcılaştırır. | Kalıcılık, atomik yerel geçiş ve erişim ayrımı hostun sağlayacağı gerçek kabiliyetlerdir; bu tur kurulmadı. |
| **Başlangıç yöntemleri ve araç bağları** | Talep oluşturma, kaynak edinme, soru açma, sonuç bildirme ve tekrar giriş için sınırlı yöntemler; izinli kaynak okuma ve taslak yazma imkânı. | Arama, dosya erişimi veya hesap aracı kullanılabilirliği ayrı doğrulanır. Katalog girdisi çalışan bağlantı değildir. |
| **Owner/Operator yetki girdisi** | Keşif kapsamını, kaynak/bütçe sınırını, değiştirilemez koşulları ve karar delegasyonunu verir. | Amaç sahibi, teknik eksikleri sürekli tamamlayan görünmez araştırmacı değildir. Mevcut yetki yoksa B0 bunu kendisi üretemez. |

Bu bileşim gelecekte Development OS'un hazırlayıp değerlendireceği başlangıç adayıdır; Development OS'un bugün var olan uygulaması hakkında bir tespit değil. SOUL'un baz çekirdeğini yaratma işi, kullanıcı mission'ının içinde açıklanmadan varsayılan sonsuz bootstrap zincirine sokulmaz.

İlk `Mission formation` işi için izin, henüz tamamlanmamış Mission Contract'tan değil, **başlangıç yetki kapsamından** gelir. B0 dar keşif yapabilir ve amaç taslağı üretebilir; bu izin yayın, yeni dış hesap, sınırsız araç veya yeni ortak politika yetkisi değildir. Kalıcı kayıt ya da gerekli kaynak erişimi yoksa ilgili devam iddiası `unavailable` kalır; hayalî kapasite planlanmaz.

## 3. Baz ve işe özgü genişleme aynı düzen içinde

Baz SOUL'da genel koordinasyon, bağlam oluşturma, kontrollü yürütme, kayıt ve yeniden giriş yöntemleri bulunur. Yeni mission'da bunun üzerine **Working Configuration** kurulur: seçilen rol örnekleri, gerçek araç bağlantıları, alan yöntemleri, değerlendirme görevleri, kaynaklar ve bu işin karar sınırları.

B0 başlangıçta hem amaç oluşturma hem keşif rolünü taşıyabilir. İşin ihtiyacı gerekçelendirince ayrı araştırmacı, üretici veya inceleyici rolü bağlanabilir. Yeni rol, rol talimatı + gerçek model/insan/program taşıyıcısı + uygun bağlam + araç/etki kapsamı + ilgili yeterlik dayanağı birleşimidir. Yeni bir isim modelin eğitimini değiştirmez.

Yeni yetenek sadece bir role eklenmez: kayıt kimliği, bağlam yolu, etki kontrolü, sonuç kabulü ve recovery kapsamı da aynı genişlemeye katılır. Bitmiş görevde gereksiz rol kapatılabilir; rolün kapanması Work, kanıt ve gerekli geçmişi silmez. Bir görevin yerel yöntemi ortak baz davranışını kendiliğinden değiştirmez.

## 4. Kayıtlar: çalışan parça değil, parçaların ortak dayanağı

Aşağıdaki adlar yerel taslak sözlüğüdür; fiziksel tablo veya her işte ayrı dosya zorunluluğu değildir. Bir kayıtta birden fazla rol tutulabilir. Görünür gerekçeler karar dayanağı özetleridir; özel model düşünce dökümü değildir.

| Kayıt | Koruduğu ayrım / kim yazar? |
|---|---|
| **Mission Contract** | Kaynak kullanıcı amacı, B0 yorumu, kapsam, kabul ve delegasyon. B0 önerir; yetki kapsamındaki owner/karar yolu etkinleştirir. |
| **Work Model** | İhtiyaç/koşullar, henüz çözülmemiş sorular, yöntem alternatifleri, gerçek Work'ler, bağımlılıklar ve ana karara dönüş bağları. K1/K2 öneri ve kararlarıyla değişir. Plan bunun yaşayan bir görünümüdür, yürütmenin kendisi değildir. |
| **Work** | Hedef çıktı/etki, kabul yükü, sorumlu, başlangıç koşulları, açıklar ve `return_to`. Açık soru otomatik blocker değildir; engellediği karar/etki ayrıca belirtilir. |
| **Artifact / Source Record** | Asıl içerik veya konumu; kimlik/sürüm, referans zamanı, kaynak türü, erişim ve provisional/current gibi kullanıma ilişkin nitelikler. Özet asıl kaynak değildir. |
| **Qualification Case** | Belirli iddia + nesne/sürüm + kullanım + ölçüt + yöntem + kaynak/kanıt + inceleyen + sonuç/belirsizlik. İnceleme sonucu ile yetkili kabul ayrı tutulur. |
| **Decision / Authority Grant** | Yetkili karar ve sınırlı etki izni; karar sahibi, nesne/kapsam ve dayanak. Modelin bir metinde «onaylandı» demesi bu kaydı üretmez. |
| **Run / Effect Record** | Work'ün gerçek denemesi; aktör/claim, başlangıç dayanakları, sunulan context, çağrı/etki kimliği, gözlenen sonuç ve belirsiz etki. `Run returned` Work kabulü değildir. |
| **Context Package** | Work sorusu, aktör, yöntem ve gerçek çağrıya sunulacak kaynak/sürüm/status bileşimi; seçilen ve eksik kalan kapsam. Yalnız paket hazırlanması değil, hostun sunduğu içerik ayrıca bağlanır. |
| **Method Entry / Working Configuration** | Kaynak-bağlı yöntem adayı, uygunluk/uygunsuzluk koşulları; ayrıca belirli işte seçilmiş etkin sürüm/roller/araçlar. Kütüphane ile etkin yapılandırma aynı değildir. |
| **Change Proposal / Event Journal** | Önerilen değişiklik ile kabul/uygulama ayrımı; geçiş olayının üreticisi ve ilgili kimlikler. Günlük tüm gerçek dünyanın eksiksiz olay kaydı veya otomatik event-sourcing kararı değildir. |

Asıl metinler kaynak deposunda kalabilir; bütün eseri yapılandırılmış graph'a çevirmek gerekmiyor. Bilinen `requires`, `uses`, `supports`, `supersedes`, `discovered_from`, `return_to` ilişkileri farklı amaçlarla tutulur. Örneğin keşfin kökeni, keşfedilen işin eski işi engellediği anlamına gelmez. Keşfedilmemiş bağı grafın tamamlığıyla bulmuş saymayız.

## 5. Çalışan parçalar ve mekanizma sözleşmeleri

RV01'in sekizli iskeleti burada kayıtlar ve çalışan işlevler olarak ayrıldı. Method Selector, aktör/yöntem/araç ortak uygulanabilirliği nedeniyle K4'e bağlandı; Method Library kayıt yüzeyidir. Bunlar yedi zorunlu servis değildir. K1–K5 aynı modelin farklı çağrılarında kısmen birleşebilir; K6'nın mekanik yaptırımı yalnız talimata indirgenemez.

### K1 — Mission Interpreter / Discovery Driver

**Tetik:** yeni talep; maddi yeni bulgu; amaç–sonuç bağına itiraz. **Taşıyıcı:** B0 veya atanmış araştırma rolü, ilgili alan kaynaklarıyla model muhakemesi.

Talebi kaynak metinle bağlar; yorum ve yetkili koşulları ayırır. Amaçlanan sonucu üretim, kullanım ve değişim içinde izler. Mevcut planın açıklamadığı koşulları soru olarak açar. Bir soru doğduğunda rakip açıklamaları ayıracak izinli kaynak incelemesini veya üretim denemesini seçer. Çıktısı `need candidate`, `inquiry Work`, `frame-change proposal` veya gerekçeli `no change` olabilir.

Keşif Work'ü «araştır» diye açık uçlu bırakılmaz: hangi ana kararı beslediği, neyin öğrenilmesinin kararı değiştireceği, eldeki kaynak yolu ve bu incelemeden dönüş noktası yazılır. İlgili kaynak ilk çerçevenin dışındaki ihtiyacı gösterebilir; yalnız mevcut anahtar sözcüklerle kontrol listesi doldurmak yeterli sayılmaz. Bu işlem anlamlı soruyu her seferinde bulduğu kanıtlanmış algoritma değildir; fakat görevi adı konmuş tek sihirli karara bırakmak yerine hangi girdilerle hangi ara ürünlerin üretileceğini belirler.

**Yetki:** öneri/inceleme kendi grant'i içinde; kullanıcı amacını veya ortak kontrolü kendiliğinden değiştiremez. **Hata:** yanlış alan varsayımı, zayıf kaynak, aynı çerçeveye kapanma. K5 iddiaya uygun inceleme yapar; çözülmeyen açık G01'de kalır.

### K2 — Work Coordinator

**Tetik:** yeni/sonuçlanmış Work, karar veya kaynak değişikliği, kapasite geri dönüşü, yeniden giriş. **Taşıyıcı:** durumdan aday çıkaran kod + öncelik/method muhakemesi.

Önce Work Model'den açık ve engelli işleri ayırır. Bilinen koşullara göre aday frontier çıkarır. K4 ile aktör, bilgi, ortam ve yetki aynı yolda birleştiğinde gerçekten başlatılabilir aday olur. Öncelik; sonraki anlamlı teslimat, kritik bağımlılık, keşfin karar katkısı ve gerçek kaynak sınırına göre seçilir; tek uydurma fayda puanı kullanılmaz.

Seçimden sonra K6, Work revision'ını ve kaynak ayırmasını aynı yerel geçişte kontrol edip claim verir. İki aktörün aynı işi sahiplenmesi salt iki liste güncellemesiyle çözülmez. Keşif sonucu geldiğinde `return_to` kararını yeniden değerlendirir; yeni ilginç soru otomatik ana hedef haline gelmez. Başarılı iş dilimi, yetkili bütün hedefle ilişkisi korunarak ilerler.

**Yetki:** atanmış kapsamda dispatch/hold/reopen önerileri; kabul koşulunu gevşetmez. **Hata:** kayıtlı ama gerçek olmayan readiness, kaynak açlığı, sonsuz keşif. Sınırlı inquiry dönüşü ve K6 gerçek koşul kontrolü bu hata yollarının bir kısmını hedefler; G01/G05 açıktır.

### K3 — Context Builder

**Tetik:** bir Work için çağrı kurulması, inceleme bulgusu veya yeniden giriş. **Taşıyıcı:** kaynak erişim/kesit araçları + seçim yapan model.

Mission'ın ilgili kısıtını, Work sorusunu, yöntem kapsamını ve kaynak/sürüm bağlarını birlikte alır. İstenen hükmü taşıyan kaynakları seçer; kimlik, izin ve sürüm tutarlılığını mekanik kontrol eder. Özet bir ilişkiyi göstermiyorsa ilişkili asıl pasajları getirir. Alan rolü eksik ilişki bildirirse yeni okuma Work'üyle tekrar kurar. Sonuç Context Package'tır; gerçek model isteğine konulan paket/ek okumalar Run'a bağlanır.

Uzun kaynaklarda okunan kapsam ve açık sorular taşınır; gerektiğinde önceki pasajlara geri dönülür. Yalnız iki bilinen pasajı aramak genel eser okumasının yerine geçmez. Hangi ilişkili pasajın gerektiğini bulmak G02'nin bilişsel yüküdür.

**Yetki:** izin verilen bilgi görünümü. Plan–metin incelemesiyle yalnız metnin sunduğunu inceleme farklı paketlerdir. Önceden finali görmüş aktöre «unut» demek izolasyon değildir. **Hata:** doğru kaynağın yanlış görünümü, atlanan statü, karışık sürüm; okuma izi anlamayı kanıtlamaz.

### K4 — Capability Binder / Method Selector

**Tetik:** yeni Work veya yeni yeterlik/araç ihtiyacı. **Taşıyıcı:** rol/yöntem kataloğu + uygulanabilirlik incelemesi + host erişim kontrolü.

Work'ün ne yapmayı ve neyi göstermeyi gerektirdiğini çıkarır. Mevcut aktörle, başka yöntemle, araç desteğiyle veya gerçekten sağlanmış insan katkısıyla karşılamayı karşılaştırır. Yöntem kaydını emir değil aday girdi olarak kullanır. Seçim, uygunluk koşulu ve dayanağıyla Working Configuration'a bağlanır; kapsam dışı veya belirsiz seçim dar deneme/qualification Work'ü gerektirebilir.

Yeterlik iddiası zayıfsa üretimden önce gerekli olan küçük, karşılaştırılabilir bir işi K5'e verir: uygulama + ayrı değerlendirme; sadece skill okuma sayısı değil. Tek başarılı örnek geniş uzmanlık sertifikası değildir. Hiçbir uygulanabilir seçenek yoksa bağımlı etki `capability unavailable` olarak bekler. Kullanıcıya seçenek/maliyet/karar ihtiyacı taşınabilir; ondan gizlice teknik çözüm üretmesi beklenmez.

Çelişen yöntemlerde önce farklı kullanım/sürüm/amaç olup olmadığını ayırır. Gerçek çatışmada geçerli üst yükümlülüğü korur; bir yöntem daha ucuz diye zorunlu kontrolü kaldıramaz. Eşdeğer işlevli kontroller birleştirilebilir, fakat gerekli hata kapsamasının kaybolmadığı ayrıca değerlendirilir. Çözülmeyen yöntem seçimi ilgili Work'ü bekletir veya değişiklik önerisine gider; bütün kütüphane her çağrıya yüklenmez.

### K5 — Domain Workbench

**Tetik:** atanmış araştırma, üretim, inceleme, revizyon veya bütünleştirme Work'ü. **Taşıyıcı:** bağlanmış model/insan/program ve alan yöntemi.

Soru-bankasında kaynaklardan kapsam çıkarma, amaca göre soru üretme, bağımsız çözüm türetme, dil/uygunluk incelemesi ve program bütünleştirmesi farklı işlerdir. Örneğin üretici hedef beceri, verilen koşullar, soru metni ve çözüm taslağı üretir; çözüm inceleyicisi gerektiğinde hazır cevap anahtarı verilmeden çözer; hesap aracı aritmetiği kontrol edebilir. Bu araç pedagojik yeterliği ölçmez. Bütünleştirme rolü grup sonuçlarını programın ihtiyacıyla karşılaştırır ve eksik kalan Work'ü önerir.

Roman için aynı yer, yazım denemesi, anlatı sırasıyla okuma, karakter bilgi ilişkisi incelemesi, yerel revizyon ve bütünsel editoryal Work taşıyacaktır. Yöntemler soru-bankasından kopyalanmaz. Tam roman yürüyüşü sonraki MS01 checkpoint'idir.

Çıktı `Artifact candidate`, `Qualification Case`, `problem/inquiry candidate` veya `need more context` olabilir. Değerlendiren rol kanıtı/yorumunu bildirir; bağlayıcı karar sadece verilmiş yetkiyle alınır. Farklı rol/model adı bağımsızlık sağlamaz. Genel kod denetimi, alan kaynakları, ayrı çözüm yolu veya gerçek insan görüşü hangi iddiayı taşıyorsa o kapsamda kullanılır.

### K6 — Run Controller / State Committer / Effect Broker

**Taşıyıcı:** host tarafında deterministik yürütme; anlamsal kararı modelden ayıran geçiş sınırı. **Tetik:** iş başlatma, etki isteği, sonuç/karar kabulü.

K6, kimliği host tarafından bağlanan aktörün grant'ini, Work/claim'i, kaynak/karar sürümlerini ve gerekli Qualification Case bağlantılarını kontrol eder. Model kendi kimliğini veya grant'ini serbest metinle genişletemez. Değerlendirme sonucu ile yetkili Decision'ı ayrı kaydeder. Kayıt tipinin doğru olması içeriğin doğru olduğunu göstermez; K5'in anlamsal hatası G04 olarak kalır.

Aşağıdaki kontrol noktaları **SOUL taslağının hosttan bağımsız adlarıdır**, gerçek bir ürün API'si değildir:

| Kontrol noktası | Çağıran / girdi | Sonuç |
|---|---|---|
| `before_work_start` | Dispatcher; Work revision, aktör, yöntem, context ve kaynak rezervasyonu | Claim + Run oluştur veya açık ret/bekleme nedeni dön. |
| `before_effect` | Araç adaptörü; hedef, işlem, payload revision, grant ve gerekli karar dayanağı | Tam bu etkiye izin ver; yetersiz/uyumsuz durumda çağrıyı gerçekleştirme. |
| `before_result_admission` | Sonuç kabul yolu; Run, başlangıç dayanakları, yeni artifact/QC/karar | Adayı kaydet; güncel kabul için uyumu denetle; gerekirse yeniden incelemeye ayır. |
| `after_state_change` | Başarılı State Committer; değişen kimlik/sürüm ve geçiş türü | İlgili readiness/context/qualification projeksiyonlarını yeniden incelemeye işaretle. |
| `on_resume` | Host yeniden giriş veya liveness olayı | K7 uzlaştırmasını tamamlamadan ilgili belirsiz etkili işi yeniden dispatch etme. |

Her model token'ında global kontrol yapılmaz. Yöntem içinde izinli yerel draft işlemleri paketlenebilir; ortak kabul, erişim genişletme ve dış etki sınırları atlanamaz olmalıdır. Bu atlanamazlık **taslağın uygulama yüküdür**, şu anda verilmiş güvence değildir.

Worker'lara doğrudan kontrolü aşan ortak yazma/yayın credential'ı verilirse Effect Broker yalnız tavsiye katmanına düşer. Bu nedenle araç bağlama, sadece isim kaydı değil gerçek kapsamlandırma ve çağrı yolları incelemesi içerir. Yeni araç veya dolaylı araç zinciri bu sınırı koruyamıyorsa o etkiyle devreye alınmaz; izinli inceleme kapasitesi ayrı kalabilir.

Yerel commit, gözlenen temel revision ve ilgili karar/bağımlılık revision'ları hâlâ uyumluysa uygulanır. Sadece yazılan dosyanın değişmemesi yeterli değildir. Etkisiz kalan değişiklikler için eski içerik yeniden kullanılabilir; uyumluluğu anlamsal olarak kurulamıyorsa aday açık kalır. Bu taslakta şart denetimi ile yerel yazım aynı korunan işlem içinde düşünülür.

Dış sistemle tek atomik işlem garantisi varsayılmaz. İşlemden önce intention/operation kimliği tutulur; destekleniyorsa koşullu yazım ve aynı etkiyi çoğaltmayan çağrı kullanılır. Zaman aşımı `effect unknown` üretir; kör retry değil hedef durumun okunması gerekir. Haricî sistem bu imkânları vermiyorsa grant, gözlem ve tekrar sınırı o sağlayıcıya göre daraltılır; evrensel exactly-once iddiası yoktur.

### K7 — Change & Recovery Manager

**Tetik:** kaynak/ölçüt/yöntem değişimi; itiraz; kayıp aktör; host yeniden girişi. **Taşıyıcı:** kayıt/gözlem araçları + etkiyi inceleyen model/rol + K6 geçişleri.

Değişiklikte bilinen `uses/supports/requires` bağlarını takip eder; etki adayı olan Work ve hükümleri işaretler. Yeni iddiayı doğrudan gerçek yapmaz. Eksik anlamsal ilişkiler için K1/K5'e etki incelemesi açar. Etkilenmiş dayanakla kabul edilmiş hükmün gelecekteki kullanımını daraltır; bağımsız destek ve geçerli eski materyali korur. Eski kanıt tarihsel koşullarıyla tutulur.

Yeni aday karar beklerken zedelenmiş eski güvenceyi geçerli saymaz. Yetki içinde bağımlı dış etki bekler; diğer yararlı işler ortak kaynak koşullarıyla devam edebilir. Kabul edilmiş yeni configuration mevcut Run'lara otomatik sızmaz: uygun olanlar eski bağlamda sınırlı tamamlanır, bazıları yeniden bağlanır, bazıları durdurulur. Geç gelen sonuç `before_result_admission` yolunda tekrar değerlendirilir.

Recovery'de yeni B0 önce Mission/current karar, Work, Run/claim, son etki kayıtları ve pending Work'ü okur. Liveness kaybı işin etkisiz kaldığını göstermez. Bilinmeyen etkiyi gözlemlemeden aynı iş yinelenmez. Yerel claim dönemi değiştirilerek eski aktörün sonraki ortak yazımı reddedilir; haricî etki zaten oluşmuşsa silinmez. Yeniden giriş bağlamı bu uzlaştırmadan türetilir, sohbetin kaldığı cümlenin kör devamı değildir.

K6'nın değişiklik olayı tek keşif kaynağı değildir: dış kaynak sessiz değişebilir. İlgili kullanımdan önce tazelik okuması, izinli kaynak gözlemi veya tanımlı periyodik Work gerekir. Zamanlayıcı kullanılacaksa gerçek host kabiliyeti olmalıdır; bu not arka planda izleme başlatmaz.

## 6. Bütünün çalışması: ortak dispatch çevrimi

1. Host bir talep, sonuç, değişiklik veya yeniden giriş olayı alır; olayın kimliği/kaynağı korunur.
2. K1/K7 gereken yorum/uzlaştırmayı üretir. K2 bu sonuçtan bir sonraki anlamlı Work adayını seçer; sırf yeni soru var diye yeni ana program açmaz.
3. K4 yöntem/aktör/araç bileşimini bağlar; K3 gerekli context'i kurar. Eksik yetenek veya bağlam, hazır iş gibi sunulmaz.
4. K6 start denetimi ve claim yapar. K5 alan işini yürütür; araç etkileri K6 üzerinden geçer.
5. Sonuç, kanıt ve yeni soru ayrı kaydedilir. K6 sonuç dayanağını uzlaştırır; gerektiğinde K5 inceleme, yetkili Decision ve K7 revizyon yolu işler.
6. K2 `return_to` sorusuna veya teslimat kararına döner. Yetkili sonuç dilimi kabul edilip hedefte gözlenirse o dilim kapanır; yıllık mission ve kullanım etkisi ayrıca açık olabilir.

Bu çevrim tek donmuş phase sırası değildir. Alan üretimi yeni ihtiyacı açabilir; birden fazla izinli Run paralel olabilir. Ancak ortak durum ve etki değişikliklerinin kimliği, yetkisi ve kabul yolu belirli kalır.

## 7. Bu checkpoint'te taslak tercihleri ve neyin seçilmediği

**P1:** Model yönlendirmesi + host yaptırımı; salt prompt veya tam statik süreç değil. **P2:** Mission başına tek mantıksal commit sınırı; paralel aday üretimi serbest. **P3:** Aktör/yöntem/context ayrı ayrı var diye hazırlık kabul edilmiyor; Run için birlikte bağlanıyor. **P4:** Başlangıç, sonuç kabulü ve dış etki ayrı kontrol noktaları; tek start hook yeterli değil. **P5:** Yöntem kütüphanesi pasif/advisory kaynak; etkin configuration'a geçiş kayıtlı seçim/değişiklik gerektiriyor.

Belirli model, framework, veritabanı, mesaj kuyruğu, hook API'si, ayrı agent sayısı, dağıtım topolojisi veya evrensel ontology seçilmedi. Bunların ertelenmesi yukarıdaki mekanizma tercihlerini silmez. Yerel prosedürler somutlaştırıldı; keşif, alan üretimi ve değerlendirme yeterliği bu isimlerle kazanılmış sayılmadı.

## 8. Devam ve kapanış

[Soru-bankası yürüyüşü](MS01-QUESTION-BANK-WALKTHROUGH.md) bu taslağı belirli Work/Run/kaynak/karar kimlikleriyle işletir; kontrol noktalarının neyi değiştirdiğini gösterir. [Kapsama kaydı](MS01-COVERAGE-AND-OPEN-MECHANISMS.md), T1–T15/DQ01–DQ04 karşılıklarını ve G01–G07 açıklarını korur.

Bu ilk MS01 teslimatı ayrı ayrı yeni DQ makaleleri değil, aynı taslağın başlangıcıdır. Sonraki bounded iş romanın aynı mekanizmalar üzerindeki yürüyüşüdür; değişmesi gereken parça veya sözleşme MS01'de güncellenir. Roman ve birleşim değerlendirmesi tamamlanmadan MS01 v0.1/EXP-004 kapanmış sayılmaz. Öte yandan gerçek runtime ve bütün bilişsel yeterlik deneyleri kavramsal taslağın tamamlanmasıyla karıştırılmaz.
