# EXP-006 — Development OS Work Map

**Statü:** DIALOGUE WORKING MAP / aday ayrıştırma.  
**Amaç:** SOUL'u yaratma hedefinden Development OS'un yapacağı işleri; ardından bu işler için gereken kabiliyet ve sorumlulukları katman katman çıkarmak.  
**Sınır:** Bu dosya SOUL modül listesi, Development OS mimarisi, rol listesi veya araç seçimi değildir.

## Katman mantığı

```text
SOUL hedefi
  ↓
Development OS'un SOUL üzerinde yapacağı ana işler (B1–B9)
  ↓
Her iş için Development OS'un gerekli kabiliyet ve sorumlulukları
  ↓
Bu sorumlulukları taşıyacak yapay zekâ rolleri / mekanik sistemler / insan
  ↓
Development OS yapısı
  ↓
İhtiyaçtan türeyen mekanizma ve araç seçimleri
```

Roller Work'ten önce icat edilmeyecek. Aynı şekilde bir kabiliyetin adı, otomatik olarak ayrı bir rol, agent, servis veya dosya anlamına gelmez.

## B — Birinci seviye Development OS Work haritası

### B1 — SOUL'un ortak entelektüel çalışma tabanını geliştirmek

İhtiyaç keşfi, sistem görüşü, araştırmadan yararlanma, kanıt–varsayım ayrımı, belirsizlik yönetimi, profesyonel çalışma standardı ve gerektiğinde derin bilgiye dönme davranışlarını oluşturmak ve sınamak.

### B2 — SOUL'un Information kapasitesini geliştirmek

Memory, context, kalıcı kayıtlar, kaynak ve sürüm takibi, retrieval, güncellik, değişiklik etkisi ve doğru bilginin doğru aktöre kullanılabilir biçimde ulaşmasını geliştirmek.

### B3 — SOUL'un Actors kapasitesini geliştirmek

İhtiyaçtan rol çıkarmak; uygun aktörü oluşturmak/bağlamak; yeterlilik, yetki, delegasyon, sorumluluk, insan–yapay zekâ ilişkisi ve aktör yaşam döngüsünü geliştirmek.

### B4 — SOUL'un Work kapasitesini geliştirmek

Amaçtan ihtiyaç ve iş keşfetmek; yaşayan planı, bağımlılıkları, başlanabilir işleri, koordinasyonu, ilerlemeyi, yeniden çalışmayı ve tamamlanma durumlarını yönetebilen kapasiteyi geliştirmek.

### B5 — SOUL'un Environment kapasitesini geliştirmek

Araçlar, runtime, çalışma alanları, sandbox, veri ve kaynak erişimi, credentials/network/tool availability, fiilî kullanılabilirlik ve gerçek dünyada etki yaratma kapasitesini geliştirmek.

### B6 — Dört zemini birbirine doğru bağlayan düzeni geliştirmek

Information–Actors–Work–Environment ilişkilerinin birlikte doğru işlemesini; readiness, context, authority, assignment, effect, verification, acceptance, change impact ve transition sınırlarını geliştirmek.

### B7 — SOUL'un işe göre çalışma sistemi kurma ve genişletme kapasitesini geliştirmek

Verilen amaç için hangi aktörlerin, bilgi düzeninin, Work yapısının, araçların, ortamın ve kontrollerin gerektiğini keşfedip kurabilmesini; ihtiyaç değiştikçe sistemi değiştirebilmesini geliştirmek.

### B8 — Süreklilik, değişim, toparlanma ve öğrenme kapasitesini geliştirmek

Oturum veya aktör kaybında Work'ü kaybetmemek; eskiyen sonuçları bulmak; belirsiz etkileri uzlaştırmak; yeni bilgiyle gerekli parçaları yeniden açmak; yöntem ve birikimi koşullarıyla korumak.

### B9 — Ortaya çıkan SOUL'u bütün olarak birleştirmek ve gerçek görevlerle sınamak

Parçaların ayrı ayrı varlığını değil, SOUL'un gerçekten amaç alıp gerekli çalışma sistemini kurabildiğini, işi ilerletebildiğini, gerçek sonuç üretebildiğini ve bunu uygun kanıtla sınayabildiğini göstermek.

## Güncel odak

Şimdi yalnız **B1** açılacaktır.

Sorulan soru:

> **Development OS, SOUL'un ortak entelektüel çalışma tabanını geliştirebilmek için neyi yapabilir olmalı ve hangi sorumlulukları taşımalıdır?**

Bu sorunun cevapları henüz rol isimleri değildir. Bir cevap ancak daha sonra “bunu kim/ne taşımalı?” sorusuyla role, mekanik sisteme veya insan sorumluluğuna bağlanacaktır.


---

## B1 açılımı — SOUL'un ortak entelektüel çalışma tabanını geliştirmek

### B1'in hedef çıktısı

Development OS'un burada üretmeye çalıştığı şey, yalnız bir ilke veya prompt listesi değildir.

Hedef; yeni bir SOUL rolü/aktörü oluşturulduğunda ona aktarılabilen, role özgü uzmanlıktan ayrı duran, hangi derin bilgiye ne zaman dönüleceğini fark ettiren ve gerçek davranışta sınanabilen **ortak çalışma tabanıdır**.

Bu taban örneğin şu davranış yönlerini taşıyabilir:

- görünür talebi doğrudan yeterli iş tanımı saymama;
- amaç, yöntem, varsayım, kanıt ve gerçek sonucu ayırma;
- sistemin bütününü ve kendi yerini görebilme;
- belirsizliği ve eksik önkoşulu fark etme;
- gerektiğinde araştırma veya başka uzmanlık ihtiyacını yükseltme;
- var olan araştırma/bilgi kütüphanesinin farkında olma ve ne zaman derine inileceğini bilme;
- rol ve yetki sınırını aşmama;
- yeni bilgi karşısında hükmünü güncelleme;
- iş küçük diye profesyonel çalışma standardını terk etmeme;
- uzun işte amaç ve çalışma durumunu kaybetmeme.

Bunlar nihai checklist değildir; B1'in geliştireceği ortak tabanın yönünü tarif eder.

### Development OS'un B1 için gerekli kabiliyet ve sorumlulukları

#### B1-C1 — Ortak tabanı keşfetmek ve tanımlamak

Development OS, hangi çalışma davranışlarının bütün akıl yürüten SOUL aktörlerinde ortak olması gerektiğini araştırıp gerekçelendirebilmelidir.

Aynı anda şunları ayırmalıdır:

- ortak entelektüel taban;
- role özgü uzmanlık;
- role özgü amaç/sorumluluk;
- projeye özgü güncel bağlam;
- yalnız belirli bir mekanizmaya ait uygulama ayrıntısı.

Amaç bütün rolleri aynılaştırmak değil, rol uzmanlaşırken kaybolmaması gereken ortak çalışma niteliğini belirlemektir.

#### B1-C2 — Ortak tabanı aktöre taşınabilir hâle getirmek

Tanımlanan çalışma tabanı yalnız Development OS'un araştırma dosyalarında kalmamalıdır.

Development OS, farklı SOUL aktörlerinin/rollerinin bu tabanı fiilen kullanabileceği bir karşılığa dönüştürebilmelidir. Bunun teknik biçimi henüz seçilmez; instruction, protokol, skill, seçilmiş context, model uyarlaması veya başka mekanizmalar aday olabilir.

Buradaki sorumluluk mekanizmayı erken seçmek değil, **tanımdan gerçek aktör davranışına aktarım problemini çözmektir.**

#### B1-C3 — Derin bilginin varlığını ve ne zaman gerektiğini aktöre fark ettirmek

Her aktör bütün araştırma ve kaynakları sürekli taşımak zorunda değildir.

Fakat ortak taban, aktörün:

- hangi tür sorunlarda daha derin bilgi gerekebileceğini;
- ilgili bilgi veya araştırmanın mevcut olabileceğini;
- kendi mevcut bilgisinin ne zaman yetersiz olduğunu;
- ne zaman kaynak/araştırma/uzmanlık çağırması gerektiğini

fark edebilmesini sağlamalıdır.

Derin bilginin saklanması, bulunması ve context'e taşınması B2 ile kesişir; B1'in sorumluluğu **bu bilgiye dönme ihtiyacını fark eden çalışma davranışını** geliştirmektir.

#### B1-C4 — Davranış beklentisini uygun kontrol türüne çevirmek

Development OS, her çalışma ilkesinin yalnız “aktöre söylemekle” güvenilir biçimde sağlanabileceğini varsaymamalıdır.

Her kritik beklenti için şu ayrımı yapabilmelidir:

- aktör muhakemesi / talimat yeterli mi;
- gözlem ve değerlendirme yeterli mi;
- yoksa yanlış davranışı gerçekten engelleyen mekanik bir kontrol mü gerekiyor?

B1 burada kontrol ihtiyacını ve beklenen davranışı tanımlar. Gerçek host/runtime/enforcement mekanizmasının geliştirilmesi özellikle B5/B6 ile kesişir.

#### B1-C5 — Aktörün gerçekten bu tabanla çalıştığını sınamak

“Kuralları okudum”, “araştırmadan haberdarım” veya “SOUL-native çalışıyorum” beyanı yeterli değildir.

Development OS, ortak tabanın gerçek davranışta ortaya çıkıp çıkmadığını sınayabilmelidir. Örneğin:

- söylenmemiş kritik ihtiyacı fark ediyor mu;
- varsayımı kanıt gibi kullanıyor mu;
- ilgili araştırmaya gerektiğinde dönüyor mu;
- rolünün dışında kalan ihtiyacı görünür kılıyor mu;
- küçük işte gereksiz sistem kuruyor mu;
- yeni kanıt geldiğinde eski hükmü değiştirebiliyor mu?

Test yöntemi tek bir benchmark veya aynı-model self-review olmak zorunda değildir; iddiaya uygun değerlendirme gerekir.

#### B1-C6 — Başarısızlığın nedenini teşhis etmek

Bir aktör ortak tabana uygun davranmadığında Development OS bunu yalnız “daha iyi prompt yazalım” sorunu saymamalıdır.

Sorunun kaynağını ayırabilmelidir:

- temel model kapasitesi yetersiz mi;
- gerekli bilgi/context verilmedi mi;
- bilgi vardı ama kullanma davranışı oluşmadı mı;
- rol amacı yanlış mı kuruldu;
- talimat zayıf mı;
- araç/Environment yetersiz mi;
- yetki veya kontrol sınırı yanlış mı;
- değerlendirme yöntemi hatalı mı?

Bu teşhis sonraki düzeltmenin hangi B dalına ait olduğunu belirler.

#### B1-C7 — Ortak tabanı kanıta bağlı biçimde değiştirmek

Yeni araştırma, gerçek çalışma deneyimi veya başarısızlık ortak çalışma tabanında değişiklik gerektirebilir.

Development OS:

- yeni dersi doğrudan kalıcı kurala çevirmemeli;
- hangi davranışın neden değişeceğini göstermeli;
- değişikliğin hangi aktör/rol kullanımlarını etkilediğini belirlemeli;
- eski yararlı davranışları gereksiz yere kaybetmemeli;
- değişmiş tabanı yeniden sınamalıdır.

Kalıcılık, sürüm ve yeniden kullanım mekanikleri B2/B8 ile kesişir; B1'in sorumluluğu ortak çalışma standardının **epistemik ve davranışsal olarak kontrollü evrimi**dir.

### B1 sınırı

B1 tek başına:

- memory sistemi kurmaz;
- rol uzmanlıklarını çözmez;
- host/runtime seçmez;
- bütün mekanik kontrolleri implemente etmez;
- Work yönetimini çözmez.

B1, diğer dallarda geliştirilecek kapasiteleri kullanacak aktörlerin **nasıl bir ortak çalışma zekâsı ve davranış standardı taşıması gerektiğini ve Development OS'un bunu nasıl oluşturup sınayacağını** ele alır.

Bu açılım henüz rol listesi değildir.
