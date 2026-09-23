# Claude Code ile Development OS hazırlığı — çalışma kaydı

**Kimlik:** CC-DEVOS-PREP-20260923 / v0.1  
**Kayıt tarihi:** 23 Eylül 2026. Kaynak kullanıcı mesajlarının kesin saatleri atanmamıştır.  
**Statü:** HAZIRLIK ÇALIŞMASI AÇILDI; ilk kaynak-bağlı ihtiyaç kaydı ve Claude görevi hazırlandı; Claude'a yeni görevin gönderildiği ve çalıştırıldığı henüz doğrulanmadı.  
**Hedef:** `batuhanozgun/soul-development-os3_claudecode`.  
**Rol:** SOUL Research içindeki cross-project hazırlık/devir kaydı; hedef repository'nin canlı iş/kanıt otoritesinin yerine geçmez. Yeni bir araştırma paketi, kabul edilmiş mimari veya agent-control değildir.

## 1. Amaç, güncel yetki ve sınır

Claude Code, cloud ortamında Development OS'u oluşturacak; daha sonra bu çalışma düzeniyle SOUL'un araştırılması, tasarlanması, geliştirilmesi ve doğrulanması yürütülecek. Bugünkü iş, Claude'a yalnız iyi talimat vermek değil, bu sorumluluğu üstlenebilmesi için gereken bilgi, muhakeme, uzmanlık, araştırma kullanımı, araç, çalışma yönetimi ve doğrulama koşullarını ortaya çıkarmak ve karşılanma durumlarını göstermektir.

Batu hazırlık yönünü benimsedi; küçüklüğü veya asgari yapıyı başlangıç hedefi yapmayı reddetti; RPD'nin yalnız protokolünün değil araştırmasının ve özgün metinlerinin kullanılmasını istedi; son mesajında açıklamaya ek olarak düşünülmüş aksiyon istedi. [OWNER-CONTEXT](OWNER-CONTEXT.md) görünür kullanıcı dayanaklarını korur.

Bu kayıt ve ilk devir paketi o hazırlığın fiilî başlangıcıdır. Claude'a yeni görev gönderilmesi ile görevin burada hazırlanması ayrıdır. Hedefte DevOS kodu, aktif protokol, hook/skill, ajan topolojisi, credential, ağ politikası veya otomasyon kurulumu bu Research turunda yapılmaz. `_02` bu deneyin çalışma hedefi veya zorunlu öncülü değildir; onun yetkisi/mimarisi/READY durumu miras alınmaz. Eski iptal edilmiş ihtiyaç-keşfi girişimi yeniden başlatılmaz.

"Ayrı Builder sistemi" dahil önceki yedi aşamalı öneri adaydır. İhtiyaçların bunu gerektirdiği gösterilmeden yeni bir üst sistem veya değişmez sıra seçilmez. Küçüklük de büyüklük de kabul ölçütü değildir. Ürün kapsamını bilerek sınırlamak, işi üstlenen tarafın hazırlık ve çalışma standardını eksiltmekle aynı şey değildir.

## 2. Şimdiki gerçek durum ve kanıt sınırı

- Bu tur Research `main` başlangıcı doğrudan okundu: `cee38caa970399fa4bf267cb484331e0c50164c9`.
- Hedef GitHub `contents/` çağrısı bu tur `404 / This repository is empty` döndü. Bu, o erişim yüzeyinde içerik görülmediği gözlemidir; Claude cloud çalışma ağacının, yerel commit'lerinin veya konuşma çalışmasının boş olduğunu göstermez. Hedefe yazılmadı.
- Önceki kullanıcı aktarımında Claude R01'i okuduğunu ve iki repoya yazmadığını bildirmişti. Bu, Claude'un beyanıdır; bugünkü runtime durumu değildir.
- RPD araştırmasının üç dosyası ve özgün iki metin bu conversation'da tam okundu. Özgün metinlerin runtime kopyaları bu tur yeniden SHA-256 kontrolünden geçti. Tamlık, kimlik ve kaynak sınıfları [SOURCE-REGISTER](SOURCE-REGISTER.md)'dadır. ZIP prototipi bu tur çalıştırılmadı veya bütünüyle yeniden okunmuş sayılmadı.
- Claude'un gerçek kaynak kullanımı, kontrol yüklemesi, yeni oturumdan devamı ve mühendislik kapasitesi bu Research turunda sınanmadı. Belge okumak veya dosya oluşturmak bu iddiaları kapatmaz.

## 3. İlk RPD geçişi — açılmış ihtiyaçlar, tamamlanmış mimari değil

Kök ihtiyaç **N00**: Claude, kullanıcının gizli teknik koordinatör/eksik-bulucu rolüne dayanarak değil, gereken koşulları keşfedip karşılayarak Development OS inşasını yönetebilsin. Aşağıdaki kayıt ilk geçiştir; kapalı bir kapsam listesi veya tüm önkoşulların bulunduğu iddiası değildir. İlişkiler aksi kanıtla değişebilir.

| Kimlik / ihtiyaç | Üst bağ ve neden | Şimdiki durum | Dayanak / kapanma için gereken |
|---|---|---|---|
| N01 — Hedefin, başarı yönünün ve sorumlulukların ortak anlaşılması | N00; yanlış hedefe yetkin uygulama başarı olmaz | Kullanıcı niyeti kaydedildi; Claude'un yeni çerçeveyi devralması bekliyor | OWNER-CONTEXT; Claude kendi görev yorumunu, açık tercihleri ve varsayımlarını ayırmalı |
| N02 — Gerekli çalışma ve uzmanlık ihtiyaçlarının keşfi | N00; yalnız verilmiş işlerin iyi yapılması keşfedilmemiş yükleri karşılamaz | AÇIK | RPD kavramsal §§1–9, 13–15; EXP-001 U011, EXP-002 U012–U014; alternatif çerçeve ve kaynak katkısı görünmeli |
| N03 — Research birikiminin elde edilmesi ve gerçekten kullanılması | N02 ve N07; erişim, seçim, yorum ve uygulama ayrı | Research erişimi burada var; Claude'da güncel exact okuma ve kullanım doğrulanmadı | Foundation/studies/explorations ayrımı; yalnız dosya listesi değil değişen soru, seçenek veya karar dayanağı |
| N03a — Özgün RPD kaynaklarının gerçek tüketiciye ulaşması | N03; Research özeti tam kavramsal/süreklilik kaynağı yerine geçmez | İki kaynak kurtarıldı ve hash doğrulandı; aktarım paketiyle teslim; Claude readback BEKLİYOR | SOURCE-REGISTER'daki iki SHA-256; tam okuma aralıkları ve anlamı kullanım |
| N04 — Gerçek cloud çalışma koşulları ve mevcut işin korunması | N00'ın seçilen Claude-cloud yolu; isim/sürüm varsayımı yetmez | AÇIK; yalnız uzak repo gözlemi var | Görevi yapan Claude'un çalışma ağacı, erişim/yetki, etkin talimatlar, yürütme ve kalıcılık kanıtı |
| N05 — İstenen muhakeme disiplininin etkinleşmesi ve uygulanması | N02; iyi protokol metni tek başına davranış sağlamaz | R01 incelemesi mevcut girdi; portlama/aktivasyon seçilmedi | Güncel kontrol kaynakları + actual host; semantik kapsam, tetik, bypass ve davranış ayrımı |
| N06 — Bitmemiş keşfin, karar dayanaklarının ve işin sürekliliği | N00, N02; hazırlığın kendisi de oturumlara yayılabilir | Research hazırlık kaydı açıldı; Claude-devri gerçek koşuda sınanmadı | RPD kavramsal §§16–20; süreklilik tasarımı §§3–16; next-operation ile return-to ve değişen dayanaklar korunmalı |
| N07 — Anlama, keşif ve mühendislik sonucunun uygun değerlendirilmesi | N00; yeşil biçim testi veya self-review genel yeterlik değildir | Kabul soruları tanımlı; runtime/semantik kanıt AÇIK | RPD kavramsal §24; mekanik gözlemler; EXP-005 D05; yanlış durumda ayırt eden ve işe bağlı inceleme |
| N08 — Yetki, kaynak ve rol sınırlarının birlikte yönetilmesi | N00 ve her etkili eylem; gereklilik izin yaratmaz | Kullanıcının amacı/sınırları kayıtlı; actual etki yolları AÇIK | Owner kararları Batu'da; teknik keşif aktörlerde; credential/harcama/policy genişlemesi otomatik değil |
| N09 — Hazırlıktan gerçek DevOS işine dönüş ve yeniden planlama | N00; hazırlık yeni terminal hedefe dönüşmemeli | Bağ korundu; ilk inşa işinin başlanabilirliği HENÜZ belirlenmedi | Hazırlık bulgusu hangi DevOS kararını açıyor; açık dal nasıl sürüyor; sonucu görünmeyen bağımlılık kapatılmamalı |

N01 ve gerekli N03/N04 bilgileri olmadan kapsamlı hazırlık hükmü verilemez. N05 için önce ilgili davranış ihtiyacı ile gerçek host ayrı anlaşılmalı. N06 ürün kodundan önce de gerekebilir; bu durum otomatik yeni veritabanı veya custom runtime gerektirmez. N07 bütün dalların sonucuna uygulanır; en sonda eklenen törensel review değildir. Aynı anda gerekli dallar VE, gerçek alternatif yöntemler VEYA olarak korunur; bir dalın kapanması N00'ı kapatmaz.

Bu turun fiilî değişimi N01'in kaynak-bağlı kayda geçmesi, N03a'nın Research tarafındaki kaynak kurtarma adımının kapanması ve N06'nın hazırlık kaydının kurulmasıdır. Claude tarafında karşılanmış yeni kapasite iddia edilmez.

## 4. Aday yöntemler ve henüz seçilmeyenler

Mevcut host araçlarının bu koşulları karşılaması, mevcut araçlarla birlikte görev/protokol uyarlaması veya bazı karşılanmamış koşullar için yeni mekanizma oluşturulması ayrı olasılıklardır. Hiçbiri varsayılan kazanan değildir. Claude Code'un mevcut çalışma ortamına sahip olması N00'ın karşılandığını göstermez; her eksik için ayrı bir sistem kurmak da gerekmez.

R01–R09'un tümünü kopyalama, RPD'yi hook'a indirgeme, çoklu ajanı zorunlu sayma, her şeyi daima context'e yükleme, hafıza için peşinen RAG/DB seçme ve ilk kısa testten global READY çıkarma seçenekleri peşinen benimsenmez. Kaynakta geçen tasarım örneği veya test sayısı bu tercihleri yetkilendirmez.

## 5. İş sırası, somut çıktılar ve dönüş noktaları

| İş | Sorumluluk / durum | Çıktı ve bir sonraki bağ |
|---|---|---|
| W00 — Konuşma yönünü, kaynakları ve ilk açık ihtiyaçları kalıcılaştır | Research; TAMAMLANDI — main yayını, kaynak/bağlantı ve aktarım paketi bütünlük kontrolleri yapıldı | OWNER-CONTEXT, WORK, SOURCE-REGISTER, CLAUDE-TASK-01; yeni oturum doğru hedefe döner |
| W01 — Claude'un kaynak-bağlı hedef devralması ve mevcut koşulları gözlemesi | Claude; görev HAZIR, gönderim/koşu teyidi YOK | Actual-state raporu + ilk gereksinim/bağımlılık değerlendirmesi; N01–N04/N06/N08'i günceller |
| W02 — W01'i kaynaklar ve gerçek hedef karşısında değerlendirme | Research ve Claude; W01 sonucu gerekli | Anlaşma boşlukları, kritik eksikler, alternatifler, test edilebilir hazırlık gerekleri; N00'a döner |
| W03 — Seçilen hazırlık gereklerini karşılayan mekanizmaları tasarlama/uyarlama | Sonuçlara bağlı; henüz başlatılmadı | Gerekçeli kontrol, uzmanlık, bilgi/iş/ortam düzeni; önceden kabul edilmiş teknoloji/topoloji yok |
| W04 — Gerçek çalışma ve devirle hazırlık iddialarını sınama | Sonuç/yetki/kaynak koşullarına bağlı | Tanımlı sorumluluklar için kanıt; global başarı yerine açık sonuç ve kalan yükler |
| W05 — DevOS inşa işlerine geçiş ve süreğen keşif | N00'ın ilgili giriş koşullarına ve kullanıcı yönüne bağlı | Gerçek DevOS üretim işi; hazırlık ve yeni ihtiyaç keşfi durmaz, ürün hedefi küçülmez |

Bu tablo zorunlu waterfall değildir. Seçime bağlı olmayan kaynak/olgu incelemesi paralel ilerleyebilir; sonuçlar önceki ihtiyacı açabilir. W01'in görevi bütün DevOS mimarisini teslim etmek veya listedeki tüm açık ihtiyaçları bitmiş göstermektir denmez.

## 6. İlk görev için kabul ve başarısızlık ayrımı

W01 raporu; hedef/rol anlayışını kaynakla bağlamalı, gözlenen durum ile varsayımı ayırmalı, gerçek tüketicide kaynak erişimini göstermeli, eksik donanımı ürün adlarına atlamadan gerekçelendirmeli ve daha sonra hangi incelemeye dönüleceğini belirtmelidir. Research readback, SHA eşleşmesi ve etkisiz marker deneyi kendi dar iddialarını destekler; anlamlı araştırma kullanımı veya fresh-session kapasitesi için ayrı kanıt gerekir.

Kritik kaynak eksikse ilgili sentez bekler; mevcut işi ve açık engeli kaydetmek devam eder. Shell yolunun başarısızlığı hizmetin bütün yayın yollarının yokluğu değildir. Yeni oturumdan devam edilmediyse o satır NOT TESTED kalır. Genel durum açıklaması, modelin bütün davranışını bağımsız doğrulamaz.

Bütçe/bağlam bitmesi, okunmuş dosya sayısı, dolu tablo veya "kontrol uygulandı" ifadesi yeterlik hükmü değildir. Aynı zamanda yeni bir soru bulunması tek başına sınırsız hazırlık gerekçesi değildir: üst ihtiyaç, karar etkisi, gerekli kanıt ve dönüş noktası korunur.

## 7. Devir ve devam

**Sıradaki somut adım:** Batu, tek aktarım paketiyle [CLAUDE-TASK-01](CLAUDE-TASK-01.md)'i mevcut Claude cloud oturumuna iletir. Mesajın taşınması teknik yöntemi Batu'ya seçtirmez. Research burada doğrudan Claude oturumu başlatmadı veya onunla otomatik kanal kurmadı.

**Next authorised Research work:** Claude gönderim teyidi veya yanıtı geldiğinde bu hazırlık kapsamında değerlendirmek; W00'ı yeniden hazırlama görevi olarak açmamak. Gönderim teyidi veya gerçek sonuç geldiğinde bu kayıt güncellenir. Arka planda izleme başlatılmadı. **Next logical implementation work** ile **bugün gönderilmiş iş** ayrı kalır.

## 8. Gerçek yayın ve kontrol makbuzu

İlk aday `238cb5893f67c44e283d9d217bc9976feb619d16` main'e fast-forward edilemedi; GitHub 422 verdi. Force kullanılmadı. Başlangıçtan yeni main `76da2197e669b7c278e0b82a831e61f74e9adf95`e yedi commit farkı yalnız altı ECC dosyasındaydı. Aynı yedi hazırlık dosyası bu yeni ağacın üzerine taşındı; ECC ve diğer alanlar korundu.

**Gerçek ana yayın:** `74abce21bf17e278eec331b2b7beadd482b32f62`. GitHub main ref güncellemesi başarılı döndü; ardından main STATE ve bu WORK doğrudan geri okundu. Paket dört kaynak/iş/görev dosyası ile soul-context STATE/INDEX/README yönlendirmelerinden oluşur. Agent-control, Foundation, studies içerikleri, explorations ve hedef Claude repository'sine yazılmadı. Çalışma branch'i veya PR açılmadı.

Dört paket dosyasının remote Git blob'ları yerel byte'lardan hesaplanan kimliklerle eşleşti; 14 yerel yönlendirme bağlantısı kontrol edildi. İlk aktarım ZIP'inin sekiz üyesi, CRC'si, manifest SHA-256 değerleri ve güvenli dosya yolları kontrol edildi. RPD'nin iki özgün metni eski değerlendirmedeki hash'lerle eşleşiyor. Makbuz güncellemesi sonrasında teslim ZIP'i aynı görev ve kaynaklarla, yeni WORK sürümü ve exact ref'iyle yeniden paketlenir; kendi manifesti ve nihai teslim bu sürümü bağlar.

Bu makbuz yalnız WORK'ün W00/yayın/next-work durumunu kapatır. Claude görev blob'u `f61daabf85606a35a7c031387cf85f51b37cf7a9` ve kaynak dayanakları değişmez. Dosya/bağlantı/ZIP kontrolü ile içerik self-review'ü yapılmıştır; bağımsız actor, Claude runtime veya fresh-session yeterlik deneyi yapılmış sayılmaz. W01 hâlâ gönderim/yanıt bekler; DevOS hazırlığının bütünü tamamlandı denmez.
