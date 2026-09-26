# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** Kalıcı master plan ve repository devri hazırlandı; **P1 NEXT / NOT STARTED**. P2–P6 PLANNED / NOT STARTED.  
**Planın tek ana yüzeyi:** [WORK — master plan v1.0](WORK.md).  
**Son kullanıcı yönü:** Claude imkânlarını araştırmadan önce mevcut EXP-006 ile bütünleşik çalışma planını kalıcılaştır. Özerklik, her rol geçişini Batu'nun tetiklememesi demektir; sonsuza kadar müdahalesiz çalışma değildir. Kaynak: [U002-A/B/C](sources/U002-cloud-plan-and-autonomy.md).

## Sabit kapsam ve sınırlar

- **Environment:** Kullanıcının seçimi Claude Code cloud. Gerçek özellik/sınırların yeterliliği henüz P1'de araştırılmadı.
- **SOUL'u geliştiren:** Kurulacak DevOS ekibi. İlk ve sonraki SOUL işlerini ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant burada o ekibin çalışma düzenini tasarlar; onun yerine gerçek SOUL backlog'u seçmez.
- **K1 iletişim:** Rol başka rolden bilgi/araştırma/değerlendirme/kontrol ister; talep etkin işe ve geri dönen, kullanılan sonuca bağlanır. İletişim yöntemi açık.
- **K2 normal ilerleme:** Her adımda Batu'nun “şimdi sıra sende” demesi gerekmez. Başlatma/yeniden başlatma, gerekli müdahale, meşru yetki ve kabul mümkündür. Sınırsız kesintisiz özerklik şartı yok.
- **Loopinance örnekleri:** Kanon manuel tetikleme karşı örneği; v2 yalnız rutin kullanıcı tetiklemesi gerekmemesinin örneği. V2'nin bütün düzeni veya ECC seçimi benimsenmedi.
- **Bilgi:** SOUL ürün çıktıları ile DevOS'un kendi plan/bilgi/karar/kanıt/devam kayıtları ayrı amaçlarla, ilişkileri korunarak yönetilir. Fiziksel depolama şeması seçilmedi.
- **Çalışma standardı:** Foundation düşünme kapsamını genişletir; studies uygulama ve karşı örnekleri sağlar. Yalnız kaynak isimlerini saymak yeterli kullanım değildir.

Kabul edilmiş çalışma anlaşmaları ve yeni kullanıcı kısıtları [DECISIONS](DECISIONS.md)'ta; kaynak mesajlar U002'de. Buradaki gereksinimler gösterilmiş platform kabiliyeti değildir.

## S1'den devralınan

SOUL hedefi → B1–B9 geliştirme kapsamı → R1–R25/M1–M9 ilk türetim → S1-01–S1-17 → F1–F8 aday aile/specialization modeli → mevcut P1–P6 planı.

S1-17 **CLOSURE-READY / CANDIDATE** sonucu korunur; nihai rol kadrosu, sekiz ajan, bütün SOUL işlerinin keşfi veya çalışan sistem kabulü değildir. S1 kullanıcı kapanışı kaydedilmedi; buna rağmen sonraki tasarımın planlanması artık kullanıcıca istenmiştir. Her devamda kapanış sorusu veya aile incelemesi yeniden başlatılmaz.

Current aileler ve lineage [ACTORS](ACTORS.md)'ta. F2 gerçek uygulama yükünü görünür tutar; her dosya yazımı F2 değildir, reusable olması şart değildir. F3 Information Lifecycle ve Actor/Role Participation Lifecycle uzmanlıkları korunur; kayıt doğruluk/yetki/etki yerine geçmez. S1-16'nın kesilmiş kaynaklara ilişkin tam-okuma etiketleri [S1-17 §7](work/S1-17-consolidation-closure-audit.md#7-okuma-izi-kaynak-katkısı-ve-önceki-kayıt-düzeltmesi) ile nitelendirilmiştir.

B1–B9 referans kapsamdır; gerçek SOUL öncelik sırası değildir. Eski altı kök iş ve S1 sonuçları WORK içinde yeni planla bağlıdır.

## Açık tasarım kararları

Aktör → aile → rol → motivasyon hiyerarşisi; motivasyon başına ajan; nihai rol isimleri/sözleşmeleri; alt ajan/takım ve iletişim yöntemi; gerçek agent sayısı; dosya yükleme/kalıcılık/işletim mekanizmaları açık. Bunlar P1–P4'ün konusudur; cloud hedefinin belirlenmesiyle kendiliğinden çözülmez.

Önceki sohbetlerdeki Claude alt ajan/takım özellikleri bu paket için doğrulanmış platform bulgusu değildir. P1 birincil Anthropic kaynaklarından, cloud kapsamını ayrıca kontrol ederek ilerler.

## Current next responsibility ve durma noktası

**Bu tur tamamlanan:** U002 yönünü kaydetmek; WORK içinde bütün master planı kurmak; giriş, karar ve devir dosyalarını uyumlamak. Claude araştırması, ajan dosyaları veya kurulum yapılmadı.

**Sonraki kullanıcı devamında:** WORK/P1 kapsamında Claude cloud'u K1/K2'ye karşı araştır. Önce güncel birincil belgeler; Loopinance kanon/v2 yalnız ilgili çalışma yolları için karşılaştırma. Çıktı destek/sınır/açık soru haritası; henüz nihai topoloji seçimi değil.

**Şimdiki duruş:** Plan hazırlığında dur. P1'i aynı tur içinde otomatik başlatma. P1 yeterli kaynaklı Environment resmi sağladığında kısa sonucu ve P2/P3 etkilerini kullanıcıya döndür.

**Daha sonraki harita:** P1 Environment → P2 roller ↔ P3 WORK–INFORMATION → P4 bütünleşik tasarım → P5 gerçekleştirme → P6 sınama/devir. Teslimatlar, geçiş ve geri dönüş ölçütleri WORK'tedir; buraya ikinci ayrıntılı plan kopyası yazılmaz. P5/P6'nın varlığı kurulum/erişim/üretim yürütmesi için sınırsız yetki değildir.

## Fresh-session yolu

AGENT ve gereken kontrollerden sonra [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) tam okunur. Aynı konuşmada unchanged tam içerikler korunabilir. Ardından yalnız aktif aşamanın gerektirdiği kaynaklara inilir.

S1 master ve B/slice ayrıntıları bu yolun dayanağıdır; tarihsel “next” ifadeleri yeni planı yönetmez. `history/` ve Context içindeki eski “host seçilmedi”/sıra kayıtları kendi zamanlarına aittir. Yeni plan ayrı EXP, deneme veya kopuk araştırma programı değildir.
