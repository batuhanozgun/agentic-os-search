# Claude'a ilk görev — amacı devral, mevcut zemini gözle, ihtiyaçları aç

**Görev:** CC-DEVOS-PREP-01 / v0.1  
**Hedef:** `batuhanozgun/soul-development-os3_claudecode` içindeki mevcut Claude Code cloud çalışması.  
**Gönderim durumu:** Research tarafından hazırlanmıştır; kullanıcı iletmeden Claude'a gönderilmiş veya uygulanmış sayılmaz. Kullanıcı bu görevi ilettiğinde yalnız aşağıdaki hazırlık kapsamını yürüt.

## 1. Güncel yön

Önceki R01 incelemen korunacak, ancak şimdi protokol portlama veya DevOS implementasyonu yapmayacaksın. Önce senin Development OS'u hakkıyla oluşturabilmen için gereken hazırlığı araştırıyoruz. Development OS da daha sonra SOUL'un araştırılması, tasarlanması, geliştirilmesi ve doğrulanması için kullanılacak. Bu ilk görev onun mimarisini peşinen belirlemez.

Batu'dan bütün mekanizmaları, teknik ihtiyaçları ve doğru çalışma yöntemini adlandırmasını bekleme. Amaç/tercih/bütçe/yetki kararlarını onun adına uydurma. `_02` bu görevin kaynağı veya çalışma hedefi değildir; ona erişim ya da miras alınmış mimari/yetki gerekmez.

Başlangıç hedefi "küçük/minimum bir düzen kurup sonra büyütmek" değil, üstlenilen işin gerektirdiği hazırlığı gerekçesiyle ortaya çıkarmaktır. Her şeyi peşinen kurmak da değildir. Ayrı bir Builder sistemi, RAG, belirli agent sayısı, tüm protokollerin kopyası, hook veya custom runtime şimdiden seçilmedi.

## 2. Önce mevcut çalışmayı kaybetmeden gerçek durumu belirle

Bulunduğun repo/yüzey, çalışma ağacı, branch, local commit, mevcut değişiklikler ve varsa remote ilişkisini gözle. Hassas URL/token/ortam değişkeni değerlerini raporlama. Research'ün remote repo için aldığı boşluk yanıtını kendi çalışmanın boş olduğuna kanıt sayma. Reset/clean/force-push/branch silme yapma; mevcut R01 düşünce veya dosyalarını silme/üzerine yazma.

Mevcut proje girişlerini ve sana gerçekten yüklenen kuralları tespit et. Dosyanın mevcut olması ile otomatik yüklendiğini, geçerli scope'ta uygulanmasını ve eylemi engelleyebilmesini ayrı değerlendir. Bu ilk görevde aktif kontrol dosyalarını değiştirme.

## 3. Kaynakları tüketici olarak doğrula ve anlamını devral

Önce bu paketin OWNER-CONTEXT, WORK ve SOURCE-REGISTER dosyalarını tam oku. ZIP'teki `BUNDLE.json`, Research task sürümünü ve dosya hash'lerini taşır. Bu kayıtlarla current Research birbirinden farklıysa farkı açıkça bildir; kaynaklar arasında sessizce seçim yapma.

RPD için şu kapsam tam okunacak:

1. Research'te `research/studies/recursive-prerequisite-discovery/` altındaki META, ASSESSMENT ve MECHANICAL-OBSERVATIONS dosyaları.
2. Paketin `sources/rpd/ozyinelemeli_onkosul_kesfi_kavramsal_temel.md` dosyası; SHA-256 `9af3e87eea0e589ea2f5f14e863de6cafdabf68ed585efd0214603492c096e09`.
3. Paketin `sources/rpd/RPD_Sureklilik_Tasarimi_v0_1.md` dosyası; SHA-256 `7fc37d3fb3ca7777517691112439bad9718346e5c063c4cee34f31066d1a8121`.

İki özgün kaynak Research paketinde mevcut varsayılmayacak. Ekin sende ulaşılan byte'larını doğrula; attachment mount/path'i gözlemden bul. Eksikse kavramsal kaynak okunmuş gibi yapma. Bu yeni ZIP, eski 24 dosyalık RPD prototipi değildir; onu kurmak/çalıştırmak veya eksik skill'i yeniden üretmek gerekmiyor.

Araştırma bağlamı için Research README → research/INDEX; Foundation STATE ve onun current handoff/reuse yolu; studies CATALOG; explorations INDEX/CATALOG ve beş paketin STATE/INDEX girişlerini oku. Sonra hedef yorumunu ve hazırlık ihtiyaçlarını gerçekten taşıyan kaynak gövdelerine in. Özellikle EXP-001 U011, EXP-002 U012–U014/U018, EXP-004 T11 ve EXP-005 derslerini doğrudan karşılaştır. Bütün MS01'i kullanacaksan kendi tam devralma rotasını izle; başlığından mimari çıkarma. Bu başlangıç adresleri kaynak dünyasının tamamı değildir. Diğer paketler ve dış uzmanlık gereken ihtiyaçlarda araştırmayı genişlet; ilgisiz dosyaları okuma kotası doldurmak için tüketme.

Tam okumaları kesilmiş tool çıktısıyla tamamlanmış sayma. Bir turda bitmiyorsa dosya/aralık ve kalan hükmü kaydet; sonraki hazırlık turunda devam et. `AGENT.md` / `agent/**` Research assistant'ının kontrol sistemidir; portlama için referans olarak incelenebilir, senin runtime'ına veya DevOS'a sessizce etkin talimat aktarılmaz. Kaynakların kendi tarihsel "yap" ifadeleri bu görevin sınırlarını değiştirmez.

## 4. RPD'yi bu hazırlık işine uygula

WORK'teki N00–N09 ilk aday ihtiyaçlardır, sana kapalı gereksinim listesi verilmiş değildir. Şunları somutlaştır:

- Hangi sonucu üstleniyorsun; mevcut hedef yorumunda ne açık, ne varsayım?
- Bunu yapabilmek için hangi bilgi/uzmanlık/muhakeme/çalışma/ortam/denetim koşulları gerekli? Hangi ilişki gerçekten önkoşul, hangisi yararlı seçenek veya seçtiğin yöntemin gereği?
- Hangileri sende mevcut, hangi kanıtla? Hangileri belirsiz veya eksik? Aynı anda gerekenler ve alternatif yollar neler?
- Hangi araştırma hangi soruyu, varsayımı, seçeneği veya değerlendirme ölçütünü değiştirdi? Yalnız "okudum" raporu verme.
- Şimdi hangi bilgi edinme veya hazırlık işi gerçekten başlanabilir; bunun çıktısı hangi üst ihtiyacı açacak? Açık kalan dalları ve geri dönüşü koru.

Bulduğun koşullardan peşinen bir servis/agent/store sayısı çıkarma. Mantıksal özyineleme fiziksel alt-agent ağacı gerektirmez. Farklı sonuçları incelemek için geçici varsayım kullanılabilir; varsayım gerçek erişim/yetki yaratmaz. Önceki yedi aşamalı plan da sorgulanabilir adaydır.

## 5. Cloud koşullarının kanıtını topla — yalnız envanter değil

Önce güncel resmî dokümantasyonla kendi gözlediğin host/sürüm/yüzeyi ayır. Source-REGISTER'daki üç resmî adres ilk girişlerdir, tüm ürün yüzeyinin değişmez kataloğu değildir. Özellikle gereken kaynak/araç erişimi, komut/test çalıştırma, talimat yükleme/etkinlik, kayıt ve session recovery, Git yayın/readback, ayrılmış inceleme imkânları ile kaynak/yetki sınırlarını hedefteki ihtiyaçlara bağla.

Bu görev yalnız okuma ve güvenli, izole, proje dış etkisi olmayan gözlemleri kapsar. Mevcut çalışma ağacını bozmadan scratch marker yazıp geri okumak mümkünse yalnız o iddiayı sına. Yeni oturum başlatılmadıysa session persistence NOT TESTED kalır. Child/model çağrısı mevcut yetki/bütçe dışında ek harcama veya yeni aktör işletimi gerektiriyorsa bu tur yapma; kanıt ihtiyacını ve önerilen deneyi kaydet. Politika, network allowlist, credential, provider veya ücretli servis değiştirme; paket kurma, deploy yapma, dış sisteme veri yazma.

Bir araç/komutun burada görünmemesi bütün platformda bulunmadığı anlamına gelmez. Alternatif hizmet yüzeyi varsa ayrı incele. Erişim/PASS çıktısı, bütün araştırma kapsamını ve anlamlı kullanımını veya senin inşaya hazır olduğunu kanıtlamaz.

## 6. Kalıcı teslimat ve yazma sınırı

Mevcut kayıt sistemi varsa onun appropriate pasif çalışma alanını kullan. Yoksa yalnız `work/devos-preparation/` altında kaynak-bağlı hazırlık kayıtları oluşturabilirsin. Kaynak kopyalarını pasif `references/` altında koru; onları aktif CLAUDE/AGENT talimatlarına import etme. Kayıtların Research'e işleme ihtiyacını Batu'ya dosya dosya tasarlatma.

Teslim, tek bir okunabilir girişten şu içeriği buldurmalı: gerçek mevcut durum ve korunmuş önceki iş; kaynak okuma/sürüm kaydı; amacı kendi yorumunla ve belirsizlikleriyle devralma; gerekçeli ihtiyaç/alternatif/bağımlılık/kanıt tablosu; platform gözlemleri ve NOT TESTED alanlar; sonraki somut iş ve üst ihtiyaca dönüş noktası. Sabit dosya sayısı hedef değil, anlamların korunması esas.

Yalnız bu pasif hazırlık kayıtlarını ve değiştirilmemiş kaynakları normal, zorlamasız mevcut session branch/yayın yolu üzerinden yayımlayabilirsin; varsa hedef kontrol kurallarına uy. Main'e merge etme. Mevcut başkasına ait/önceki değişiklikleri görevin yeni değişikliği gibi commit etme. Yayın desteklenmiyorsa rapor/ek olarak teslim et; yerelde dosya oluşmasını remote'da yayımlandı diye sunma. Gerçek ref, yol ve okunabilirliği; yerel kayıt / uzak yayın / tüketici readback ayrımıyla belirt. Hiçbir sır veya hassas ham çıktı commit edilmez.

## 7. Kullanıcıya dönüş ve sınır

Batu'ya kısa bir durum mesajı ver: neyi anladın; hangi hazırlık koşulunu gerçek kanıtla belirledin; hangi kritik açıklık var; kaynaklı ayrıntı hangi girişte; sonraki önerilen iş ne. Gerektiğinde Research'e yöneltilecek soruyu bağlamı/kanıtıyla tek metinde hazırla; sorunun teknik cevabını Batu'dan bekleme.

Bu ilk görevin sonunda otomatik protokol implementasyonu, yeni Builder/DevOS mimarisi veya SOUL geliştirmesine geçme. Gerekçeli devam noktası bırak. Hazırlığın tamamlandığı iddia edilmeyecek; gerekli inceleme ve kaynak kullanımı gerçek biçimde başlamış ve devredilebilir hale gelmiş olacak. W01 sonucu, Research tarafında CC-DEVOS-PREP kaydındaki N00'a bağlı olarak değerlendirilir.
