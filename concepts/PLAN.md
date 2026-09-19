# Concepts — Hazırlık ve yürütme planları

Sürüm: v0.1-draft, 2026-09-19. Amaç onaylı; yöntem denemeleri yapılmadı. Güncel tamamlanma/yetki yalnız STATE.md'dedir. Bu plan eski concepts çalışmasının devamı değildir. Kaynak yetki ORIGIN.md/U01–U05; gerekçe CHARTER.md.

## Plan A — Repo hazırlığı

### A1. Yeni başlangıcı ve kapsamı kaydet

ORIGIN.md kaynak kullanıcı mesajlarını, CHARTER.md amaç ve iki riskin nedenlerini taşır. METHOD.md ve bu plan taslak statüsünde kalır. STATE.md hazır olanla yapılmamış işi ayırır; INDEX.md yeni oturum girişidir.

Son kullanıcı talebiyle hazırlık şimdi kalıcılaştırılır. Bu, ilk taslaktaki bütün yazıları denemeler sonrasına bırakma sırasının yalnız hazırlık bakımından değişmesidir; iki deneme, yöntem değerlendirmeleri ve seri çıkarımın daha sonra başlaması korunur. Hazırlık yazma yetkisi, yapılmamış denemeyi tamamlandı işaretleme yetkisi değildir.

### A2. Eski etkin yönlendirmeleri kaldır

Değişiklik kapsamı: README.md; research/INDEX.md; research/studies/INDEX.md; research/studies/CATALOG.md; research/studies/PACKAGE-CONTRACT.md içindeki concepts bölümleri. Araştırma satırları, bulguları, mevcut araştırma yetkileri ve paket durumları bu nedenle değiştirilmez.

Kontrol değişikliği yalnız concepts için: AGENT.md'de R09 sorusunun bu ayrı programı açıkça kapsaması; agent/protocols/candidate-research-library.md içindeki concepts istisnasının yeni aşama sırası, iki riskin görünürlüğü ve giriş okumalarıyla uyumlandırılması. Genel candidate-study kuralları ve R01–R08 korunur. Kontrol dosyaları değiştikten sonra canonical sürümleri yeniden okunur.

Eski concepts dosyaları geri getirilmez. Araştırmalardaki aynı adlı dış dosyalar veya sözcükler topluca silinmez. Tarihsel konuşma/kanıt kayıtları, zaten tarihsel statüleri korunarak bırakılır; güncel yöntemin kaynağı sayılmaz. Başlangıç taraması ve koruma sınırı SETUP-REVIEW.md'de raporlanır.

### A3. Yayın ve devralma kontrolü

Mevcut main üzerinde SHA kontrollü, sınırlı dosya güncellemeleri kullanılır; yeni branch veya geçmişi yeniden yazma yoktur. Eşzamanlı değişiklik varsa son içerik geri kazanılmadan üstüne yazılmaz. Yeni çalışma dosyaları önce, onları gösteren router'lar sonra yayınlanır. Kesinti varsa STATE hazırlığı tamamlandı göstermez.

Son karşılaştırmada yalnız izin verilen dosyaların değiştiği; eski etkin yöntem parçalarının kaldırıldığı; yeni bağlantıların çözüldüğü; amaç/taslak/yetki/durum ayrımlarının tutarlı olduğu kontrol edilir. Bu inceleme statik ve aynı assistant tarafından yapılan bir kontroldür; gerçek yeni-oturum davranış başarısı veya bağımsız doğrulama değildir.

## Plan B — Çalışmanın uygulanması

| Adım | Yapılacak iş | Çıkış koşulu |
|---|---|---|
| B1 — İlk deneme | research/studies/context-memory-harness-engineering araştırmasının güncel dosya envanterini çıkar; paket girişlerini ve tüm araştırma dosyalarını oku; kullanımları sohbet içinde göster. | Dosya/temsil kapsamı açık; kullanım ve yorum izleri görünür; pilot tamamlanma iddiası kapsamı aşmıyor. |
| B2 — İlk değerlendirme | Şema, kaynak atfı, belirsizlik, okuma devamı, eski-yeni yorum ilişkisi ve kullanıcıya açıklanabilirliği değerlendir. | Ne değişti/ne korunuyor ve neden belli; başarısız ölçütler silinmemiş. |
| B3 — İkinci deneme | research/studies/superpowers araştırmasında revize yöntemi aynı disiplinle, yine sohbet içinde uygula. | İlk pilota göre farklı korpusta sınama; sentez tekrarları bağımsız destek sayılmıyor; gereken tüm okumalar tamamlanmış. |
| B4 — İkinci değerlendirme | Yöntemi yeniden değerlendir, gerekli değişiklikleri yap; kalıcı çıkarım dosya düzenini kesinleştir. | İki pilotun gerçek sonucu ve yöntem değişiklikleri erişilebilir; görülmeyen pilot veya sonraki değişmiş yöntem doğrulanmış sayılmıyor. |
| B5 — Seri çıkarım hazırlığı | Studies'in gerçek paket/dosya envanterini tamamla; koleksiyon/alt çalışma/taşınma ilişkilerini kaydet; kaynak sürümü ve güncelleme takibini kur. | Katalogla yetinilmeyen kapsama ve net sıraya sahip başlangıç. |
| B6 — Araştırma bazında çıkarım | Her araştırmayı tam okuyarak concepts/studies/<araştırma-yolu>/ içinde kullanımları ve okuma/yorum değişimlerini kaydet. | Tüm paketler hesaba katılmış; kaynaklar, okumalar, belirsizlikler ve delta kontrolleri açık. |
| B7 — Küresel geçiş kontrolü | Yeni/değişmiş/okunamamış kapsamı kontrol et; bütün çıkarımların birlikte okunmaya hazır olup olmadığını değerlendir. | METHOD §5 koşulları karşılanmış; tamamlanmamış kapsam sessizce kapatılmamış. |
| B8 — Ortak değerlendirme | Concepts çıkarımlarının tamamını oku; anlamları/sınırları ayır; gerekirse alt kavram ve ad öner; örnek/karşı örnekle yerel ortak anlayışı sınayarak referans üret. | Kaynak kullanımından ayrı, gerekçeli ve sınırları açık yerel referans; çözülmeyen ayrımlar görünür. |

B1/B3 paket seçimleri bu konuşmadaki taslakta önerildi ve çalışma sırası olarak benimsendi; kaynakların tanımlarının doğru kabulü değildir. Pilot sırasında daha uygun bir yöntem veya kapsam ihtiyacı ortaya çıkarsa gerekçeli revizyon mümkündür; iki farklı araştırmada sınama sessizce atlanmaz.

## Pilotların yürütme sınırı

Pilot bir tura sığmak zorunda değildir. Tamamlanmadan sıradaki pilota geçilmez; yalnız küçük bir örnek gösterip bütün araştırmada yöntem sınandı denmez. Pilot terim çıktıları sohbet içinde kalır; hazırlık dosyalarının oluşturulması kalıcı TERMS üretimini başlatmaz.

Mevcut STATE/PLAN/METHOD yüzeylerine durum ve yöntem değişikliği kaydetmek, pilot kullanım envanterini doğrulanmış kalıcı referansa yükseltmek değildir. Yeni oturuma geçilirse görünür pilot sonucu erişilebilir değilken hafızadan devam/tamamlanma üretilmez: gerekli kaynak ve sonuç yeniden geri kazanılır; gerekirse ilgili okuma tekrarlanır. Kalıcı seri çıkarıma aktarım, pilot kayıtlarının yeniden kaynağa karşı kontrolünden sonra olur.

İki pilot farklı çalışma düzenlerini sınar; iki çalışmadan ortak terim tanımları üretme aşaması değildir. B8 bütün çalışmaların çıkarımı bitmeden başlayamaz. B8'in ayrıntılı kayıt düzeni şimdiden dondurulmaz.

## Taslak değerlendirme ölçütleri

Kaynak tarafındaki okumadan çıkarıma geri kontrol: atlanan jargon/kullanım; özgün anlamın yorumla karışması; eşit olmayan anlamların birleştirilmesi; aynı kaynağın tekrarının bağımsız delil sayılması; değişen yorumun eski kayıtlara yayılmaması; kullanıcıya basitleştirirken ayrım kaybı; yeni oturumda belirsizlik veya devam noktası kaybı. Terim sayısı tek başına başarı değildir.

Bu ölçütler sonucu kolaylaştırmak için sonradan sessizce değiştirilmez. Pilot bulguları yöntem revizyonu için kullanılabilir; aynı veri, revize yöntemin bağımsız doğrulaması sayılmaz.

## Revizyon kaydı

- R0, 2026-09-19: U01 sonrası iki taslak plan ve iki farklı araştırmada konuşma içi deneme sırası.
- R1, 2026-09-19: U04 sonrası yorum izi/okuma izi ayrımı, iki nedenin her tur görünürlüğü ve kullanıcının teknik oracle olmaması gereksinimleri.
- R2, 2026-09-19: U05 ile repo hazırlığı şimdi yetkili; yöntem taslak, pilotlar bekliyor. Eski etkin yönlendirmeler kaldırılarak yeni oturum yolu kuruluyor. Bu kayıtlar konuşma konsolidasyonudur; gerçekleştirilmiş pilot bulgusu değildir.
