# DEVOS-001 — yönetilen iş ve devam kaydı

**Durum:** AKTİF / açılış ve ilk doğrudan görüşme hazırlığı.
**Tarih:** 23 Eylül 2026. **Tek otorite:** bu denemenin koordinasyon durumu; hedefteki teknik işin ikinci kopyası değil.
**Amaç/yetki:** [BRIEF](BRIEF.md). **Kanal:** [EXCHANGE](EXCHANGE.md). **Bulgular:** [REVIEW](REVIEW.md).

## Şu anki gerçek durum

Research ana alanı ve R-001 hazırlanmıştır; bu ilk sürümde remote yayın/geri-okuma henüz tamamlanmış sayılmaz. Açılış makbuzu aşağıya gerçek kontrollerden sonra işlenir.

İlk sahibi beklenen iş: Batu'nun tek bağlantı mesajını Claude'a iletmesi; ardından Claude'un C-001 yanıtını kendi reposunda yayımlaması. Bağlantı mesajının gönderildiği, R-001'in Claude tarafından okunduğu ve C-001'in oluştuğu henüz doğrulanmadı. Otomatik izleme/uyandırma kurulmadı.

Hedefteki son bu tur gözlenen snapshot: `411a5ee38a997ba0ba93b81fea0411a134a50adc`. STATE tam, PLAN'ın ilgili E12–E20 ve aşama kesimleri doğrudan okundu. STATE, E20'yi tamamlanmış ve E17'yi başlangıç kapısında gösteriyor; bu Claude'un kaydıdır, burada yeniden çalıştırılmış davranış kanıtı değildir. Sonraki review'da HEAD ve değişen dosyalar yeniden alınır.

## İşler, bağımlılıklar ve dönüş

| İş | Sorumlu | Durum / giriş koşulu | Sonuç ve üst amaca dönüş |
|---|---|---|---|
| W00 — deneme alanı, kaynak sınırı, kanal ve ilk mesaj | Research | YAYIN/GERİ-OKUMA BEKLİYOR | Yeni oturum denemeyi bulur; W01'in exact mesajı mevcut olur |
| W01 — kanalı devralma ve güncel gerekçeli cevap | Claude; ilk bağlantı Batu | R-001 hazır; gönderim ve okunma TEYİTSİZ | C-001 + exact kaynak/ref; dosya/iş düzeni teşhisine dayanak |
| W02 — cevabı iddia ve kaynak karşısında değerlendirme | Research | C-001 bekleniyor | İtirazlar uzlaştırılır veya açık tutulur; W03 için karar sorusu netleşir |
| W03 — gerekçeli düzenleme ve çalışma sistemi planını seçme | Claude önerir, Research değerlendirir; maddi owner tercihleri Batu | W02'ye bağlı; BAŞLATILMADI | Yerinde düzenleme / seçici yeni-repo aktarımı / başka seçenek; kayıp ve deney planı |
| W04 — seçilen değişikliği uygulama ve gerçek kullanımı sınama | Claude; Research kanıt incelemesi | Plan, yetki ve giriş koşulları gerekli; BAŞLATILMADI | Retrieval, güncellik, kullanım, devam ve geri dönüş davranışı; başarısızlık W02/W03'e döner |
| W05 — sonuç, ders ve sonraki deneme/DevOS işine geçiş | Research + Claude; yön kararı Batu | W04 kanıtı veya durdurma kararı; BAŞLATILMADI | Başarı kapsamı, başarısızlık/iptal/belirsizlik ve aktarılabilir dersler |

Bu tablo hedefteki E numaralarını yeniden yönetmez. Bir mesaj gelmesi işi otomatik tamamlamaz; bir review sonucu yeni uygulama yetkisi yaratmaz. Bekleyen işin yeniden denenmesi önceki mesajı veya etkili eylemi körlemesine tekrar çalıştırmaz.

## Mesaj / alındı kaydı

| Kimlik | İlişki / rol | Yayın ve tüketici durumu |
|---|---|---|
| [R-001](messages/research/R-001.md) | W01; Research → Claude, ilk soru | Hazır; remote yayın kontrolü W00; Claude okuma teyidi YOK |

Beklenen özgün yanıt yeri: hedef `coordination/devos-001/outbox/C-001.md`, normal görünür `main` yayını. Başka branch/path gerekirse önce kanal engeli bildirilir; bulunmayan yanıt uydurulmaz. Başarılı alımda bu kayda exact commit + path + blob ve `in_reply_to` işlenir; gerekirse EXCHANGE'e göre byte-eş kopya tutulur. C-001 dosyası bu açılışta oluşturulmadı.

## Açık kararlar ve durma sınırı

- Claude bu kanalı okuyup yanıtını kalıcı yayımlayabiliyor mu? Henüz sınanmadı.
- Mevcut bilgi düzeninin hangi açığı gerçekten iş sonucunu bozuyor? REVIEW başlangıç hipotezleri; toplu başarısızlık hükmü yok.
- E15/E16/E17 sırası ve KR1 temsili güncel kaynakla nasıl uzlaştırılıyor? Claude yanıtı gerekli.
- İlk ayırt edici çalışma deneyi ne? C-001 sonrası seçilecek; soru-bankası doğruluğu tek başına yeterli değil.
- Yeni hedef repo açılması kararlaştırılmadı. Bu açılış yalnız yönetim ve diyalogdur.

Eksik zorunlu kaynak, belirsiz yetki veya çözülemeyen güncel kayıt çelişkisi varsa ona bağlı karar bekler. Diğer güvenli ve yetkili işleri bütünüyle durdurma emri çıkarılmaz. Diyalog iki modelin birbirini onayladığı tekrar döngüsüne dönerse yeni mesaj yerine ayırt edici kanıt/deney veya gerçek owner kararı istenir.

## Sonraki Research oturumu

BRIEF/WORK/EXCHANGE'i devral → Research main ve hedef main'i doğrula → beklenen C-001 yolunu doğrudan kontrol et → varsa exact sürümden oku, kaynak ve yanıt ilişkisini kaydet, REVIEW'daki ilgili soruları değerlendir → gereken R-002'yi yaz → bu WORK'ü gerçek next-owner ve engelle güncelle.

Yanıt yoksa yokluğu yalnız kontrol edilen ref/path için kaydet; Claude'un hiçbir yerde çalışmadığını söyleme. Geçmiş uzun görev mesajını tekrar hazırlama. Oturum burada çağrılmadıkça okuma veya otomatik cevap gerçekleşmiş sayılmaz.

## Açılış / yayın makbuzu

Başlangıç Research main: `1be22a362df2aa527da09b50a19389d167fcf98e`; base tree `ccc9621cbd1c4b3e1c0db5b6a968ee5316822e2c`.
Planlanan kapsam: altı yeni development-os dosyası; kök README, soul-context girişleri ve iki tarihsel hazırlık girişinin yönlendirilmesi. Agent-control, Foundation, studies, concepts, explorations ve hedef repo değişmez.
Gerçek commit, diff ve readback sonuçları yayın sonrası buraya eklenir. Dosya/bağlantı kontrolü, Claude readback veya çalışma sistemi yeterliği değildir.
