# DEVOS-001 — bütün korpustan çalışma düzenine

**Sürüm:** 1 / 23 Eylül 2026. **Rol:** bu denemenin okuma, çıkarım ve daha sonraki karar yöntemi; agent-control veya çalışma sistemi mimarisi değil.
**Yetki ve amaç:** [BRIEF](BRIEF.md). **İş ve sıra:** [WORK](WORK.md). **Kapsam:** [COVERAGE](reading/COVERAGE.md).

## 1. Korunan amaç ve zorunlu sıra

Development OS'u araştırıp tasarlayacak, kuracak ve geliştirecek aktörlerin çalışma düzenini oluşturmak. Mevcut Claude dosyalarını düzeltmek, bir denetçi kurmak veya test geçmek ana hedef değildir. Son kullanıcı talebi şu sırayı belirledi:

**Bütün Research reposunu gözden geçir → her tur ilgili fikirleri ve örnek sistemleri kaynak-bağlı kaydet → bütün okuma/kayıt kapsamını tamamla → kayıtların tamamını birlikte oku/değerlendir → çalışma yapısına karar ver → ayrı uygulama aşaması.**

Okuma sırasında açıklama, karşılaştırma sorusu ve tasarım olasılığı kaydedilir; bileşen seçimi, M1–M3 kurulumu veya bir ürünü mimari olarak benimseme yapılmaz. Yeni belirlenen kaynaklar, karşı örnekler ve yöntem eksikleri sırayı gerekçeyle revize edebilir; kullanıcının toplu değerlendirme öncesi karar vermeme sınırı korunur.

## 2. Kapsam ve kaynak sınırı

Başlangıç kaynak anlık görüntüsü: `batuhanozgun/agentic-os-search@dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb`. Kökten bütün izlenen dosyalar envantere girer: research, concepts, explorations, publications, development-os, giriş dosyaları ve kontrol alanı. Katalog ile ağaç uzlaştırılır; katalogda görünmeyen dosya atlanmaz.

- Foundation: bütün zeminler, önceki dikeyler, bütünleşme/composition, yöntemler, kaynak defterleri, karşı değerlendirmeler, kabul/sınır ve tarihsel düzeltmeler.
- Studies: yalnız gstack/Hermes/ECC değil, ağaçtaki her paket; bitmemiş ve bekleyen paketler de mevcut içerikleri ve kanıt eksikleriyle kaydedilir. Bekleyen repo önerisi yapılmış araştırma sayılmaz.
- Explorations/context/publications: kullanıcı amacı, sistem taslakları, iyi örnekler, başarısız girişimler ve aktör yorumları yazarlık/statü ayrımıyla.
- Concepts: kaynaklardaki terim kullanımlarını ve açık anlam ayrımlarını koruyan girdi; bu çalışma terim programını devralmaz veya yeniden başlatmaz.
- `AGENT.md` ve `agent/**`: kontrol kapsamı; Research için yüklenir, araştırma sonucu diye çıkarılmaz ve değiştirilmez. Claude'a kendi kontrolünün yerine import ettirilmez.
- Bu denemenin yeni ürettiği kayıtlar yeniden kaynak kuyruğuna girip sonsuz öz-okuma yaratmaz. Başlangıçtaki eski deneme malzemesi korunur; yeni kayıtlar tüketici/karar korpusudur.

Özgün anlam taşıyan her metin dosyası tam okunur. Tam okunmamış aralık açık kalır. Tekil görsel, tablo veya başka medya yalnız adıyla geçilmiş sayılmaz; kullanılabilir içerik okunur/görülür, erişim engeli kaydedilir. Aynı içeriğin üretilmiş kopyası ancak özgün eşdeğeri ve fark sınırı gösterilerek ayrı tekrar okumadan çıkarılabilir. Hiçbir eksik dosya sessizce kapsam dışı yapılmaz.

Dış kaynaklara sınırsız yeni araştırma başlatılmaz. Mevcut araştırma claim'i için zorunlu eksik kaynak veya gelecekte load-bearing güncel davranış gerektiğinde exact kaynak tekrar açılır; erişilemiyorsa kayıt açık kalır. Bütün repo incelemesi bütün upstream ürünlerin baştan sona yeniden araştırılması demek değildir.

## 3. İş bölümü — okuma ve doğrulama ayrı

Research bu alanın kapsamını, sentez öncesi kayıt düzenini, kendi okumalarını ve toplam ilerlemeyi yönetir; sadece Claude'un son mesajına kusur aramaz. Claude kendi okuma/çıkarımını kendi reposunda yayımlar. İki aktör de bütün kapsam haritasını devralır.

Başlangıç birincil okuma dağılımı:
- Research: Foundation'ın tamamı; sonra explorations, soul-context ve publications.
- Claude: studies'in tamamı; sonra concepts ve kendi gerçek çalışma ortamı/korunması gereken kaynaklar.
- Ortak yön bağlamı: kullanıcı talebi, bu METHOD, Foundation genel sonuçları ve RPD/iş yönetimi. İkinci aktörün kaydını okumak özgün kaynak tam okuması diye etiketlenmez.

Bu dağılım kapsamı daraltmaz. Her kaydın yazarı, gerçek kaynak okuma derinliği ve karşı okuyucunun durumu ayrıdır. Her iki aktör bütün kayıtlar tamamlandığında kayıtların tamamını okuyup ortak değerlendirmeye girer; karar taşıyan veya tartışmalı yerlerde özgün kaynaklara döner. Atanmış sorumluluk, Claude'un aldığı veya bitirdiği anlamına gelmez. Alındı EXCHANGE/WORK'te doğrulanır.

## 4. Her okuma turunun çıktısı

Bir tur sıradaki anlamlı kaynak kümesini açar. Büyük bir paketin tamamı tek tura sığmazsa, gerçek aralıkta kalıcı checkpoint yayımlanır; sonraki tur o aralıktan sürer. Yarım okuma karşı taraftan onay beklemek için durdurulmaz.

Her kümenin tek kaynak-bağlı kaydı şu içeriği taşır:

1. **Kaynak/okuma defteri:** repo, commit, dosya/blob, tam veya seçili aralık, gerçek okuyucu; görülmeyen dosyalar ve erişim sınırları. Önceki oturumun okudum beyanı yeni tam okuma değildir. Aynı konuşmadaki gerçekten mevcut tam okuma yeniden kullanılabilir; bunu yeni okuma diye sayma.
2. **Kaynağın kendi bütünsel modeli:** hangi problemi çözüyor, normal çalışma döngüsü ne, parçaları birbirine nasıl bağlanıyor? Bir sistemi yalnız hata veya üç popüler özellik listesine indirme.
3. **Katkı kayıtları:** Development OS'u kuracak çalışma düzenine katkı sağlayabilecek bütün maddi fikir, işlev, mekanizma, yöntem ve örnek yapı. Her kayıt için aşağıdaki anlam korunur.
4. **Karşı örnek/sınır ve boşluklar:** hangi koşulda işe yaramaz; hangi destek yalnız belge, kod, deney veya çıkarım; farklı kaynaklar nerede ayrılıyor?
5. **Sonraki okuma ve dönüş:** hangi dosya/aralık kaldı, hangi ilişkiyi açıklamak gerekiyor, üst çalışma için ne elde edildi? Tasarım kararı değil, toplu değerlendirme girdisi.

Katkı başına korunacak anlam:
- kaynakta bulunan fikir ve özgün terminolojisi;
- çözdüğü ihtiyaç ve çalışma biçimi;
- iş, bilgi, aktör, ortam ve aralarındaki ilişkiler;
- tetik, girdi/çıktı, sahip/rol/yetki, yaşam döngüsü, takip ve geri dönüş, gerektiği ölçüde;
- bağımlı yetenekler, kaynak/maliyet koşulları, normal yol ve hata yolu;
- olumlu kullanım örneği ve önemli sınır;
- bu çalışmaya olası katkı ile kaynak bulgusu arasındaki ayrım;
- tekrar açılabilecek exact kaynak bağlantısı; ilişkili kayıt kimlikleri.

Her alana zorla içerik yazılmaz: kaynak söylemiyorsa 'kaynakta kurulmadı' denir. Bir kayıt dört zemine birden dokunabilir. Dört zemin zorunlu dört klasör/servis/ajan değildir. Kayıtlar kaynak sırasıyla kimlik alır; erken ortak terim veya mimari altında birleştirilmez. Kopya pasaj biriktirmek yerine yeterli ayrıntı ve kaynağa dönüş yolu korunur.

## 5. Bağlamın oturumlar arasında yeniden kurulması

Başlangıç: root → development-os INDEX → BRIEF → WORK → METHOD → COVERAGE → etkin kayıt ve onun özgün kaynakları. Geçmiş R/C yazışmasının tamamı olağan başlangıç bağlamı yapılmaz. R-001–R-003 ve E19 yalnız tarihsel yan dal/kanıt olarak korunur.

COVERAGE konu/paket ve soru→kayıt yollarını verir; ayrıntı kendi kayıt dosyasındadır. Yeni oturum sadece son mesajı değil, ana amacı ve kalan bütün korpusu görür. Her tur kaynak kapsamı, yeni kayıt kimlikleri, dört zemin/ilişki kapsamındaki katkı ve kalan okuma güncellenir. Bu iz bir token/okuma yarışması veya her tur aynı tören değildir.

## 6. Okuma ve kayıt aşamasının kapanışı

Toplu değerlendirme başlamadan:
- başlangıç ağacındaki her dosya bir okuma kümesine veya gerekçeli kaynak/kopya/kontrol durumuna bağlanmış;
- özgün anlam taşıyan dosyaların gerekli tam okumaları tamamlanmış, erişim engelleri açık ve çözülmüş ya da owner'a gerçek kapsam etkisiyle sunulmuş;
- her kümenin maddi olumlu fikirleri, mekanizmaları, bütünsel modeli ve sınırları kayıtlı;
- karşı okuyucu kayıt→kaynak izini ve atlanan önemli aile/ilişkiyi incelemiş;
- iki reponun kayıt adresleri bulunabilir; eski not ve tarihsel karar güncel sonuç gibi görünmüyor;
- source snapshot sonrası maddi farklar ayrı delta kuyruğunda uzlaştırılmış olmalı.

Dosya sayısını tamamlamak, bütün fikirlerin eksiksiz anlaşıldığının kanıtı değildir. Tersine konu örtüşüyor diye özgün mekanizma/sınır düşürülmez. Kapanışta içerik eksikliği karşı incelemesi yapılır; bu bağımsız doğrulama diye abartılmaz.

## 7. Ancak bundan sonra çalışma yapısına karar

Kayıtların tamamı yeniden okunur. İşin kabulü ve keşfi, planlama/takip, roller/uzmanlık/katılım/yetki, bilgi/bağlam/bellek, ortam/kabiliyet/araçlar, değerlendirme, değişim/öğrenme ve bunların bütünsel yürüyüşü birlikte karşılaştırılır. Bu liste ilk mercektir, kapalı feature listesi değil; kayıtların açtığı başka ihtiyaçlar dahil edilir.

Alternatif bütünsel düzenler, mekanizma seçimleri, uyumsuzluklar, ihtiyaç karşılığı ve eksik kanıtlar birlikte değerlendirilir. Her seçimin kayda dayanağı olur; kullanılmayan fikir kaybolmaz, neden kullanılmadığı görünür kalır. Mevcut Claude yapısı veya M1–M3 ayrıcalıklı başlangıç mimarisi değildir. Kayıtlar bitmeden parça kurarak seçimi fiilen dayatma yapılmaz.

Bu aşamadan sonra uygulama planı, gerçek yetki ve ortamla ayrıca bağlanır. Kullanıcının şu anki emri inceleme/kayıt/toplu karar sırasını yetkilendirir; yeni repository, izin genişletme, ücretli geniş koşu veya kod kurulumu kendiliğinden yetkilenmez.
