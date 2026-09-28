# EXP-006 — DECISIONS

**Rol:** Kullanıcıyla netleşmiş çalışma kararlarını/kısıtları candidate fikirlerden ayırmak.
**Güncelleme:** 28 Eylül 2026, yeni oturumdaki P4 devamı ve v3 rapor teslimi.
**Current:** P4 v3 rapor/yerel kanıt teslimi hazır; kullanıcı değerlendirmesi bekleniyor. Mimari kabulü değil. [STATE](STATE.md) ve [P4-04](work/P4-04-unbounded-stress-test-report-v3.md) current durumu taşır.
**Sınır:** Karar kaydı bir öneriyi teknik gerçeğe, gereksinimi gösterilmiş platform kabiliyetine veya dosya kimliğini yeterlik kanıtına dönüştürmez. Aşağıdaki tarihsel “bu tur/son yön” ifadeleri kendi kaynak turuna aittir; D026 sonraki devamı ayırır.

| ID | Karar / çalışma anlaşması | Statü |
|---|---|---|
| **D001** | EXP-006'nın üst amacı, SOUL'u yaratmak için Development OS'un nasıl bir çalışma düzeni olması gerektiğini konuşarak ortaya çıkarmaktır. | accepted working direction |
| **D002** | Şimdilik iki geniş aktör sınıfıyla ilerlenir: **insan** ve **yapay zekâ**. Alt ajan/model/oturum örnekleri otomatik yeni aktör sınıfı sayılmaz. | accepted working simplification |
| **D003** | İnsan/müşteri rolünün çekirdeği **yetki + kabul** olarak tutulur; teknik keşif ve koordinasyon yükü varsayılan olarak müşteriye bırakılmaz. | accepted working distinction |
| **D004** | Development OS yapay zekâ rolleri jenerik adlarla önce üretilmez; **Work'ten ve onun doğurduğu sorumluluklardan türetilir.** | accepted method |
| **D005** | Work keşfinde RPD kullanılır; ihtiyaç/iş önce, sorumluluk/rol sonra, mekanizma/araç en son gelir. | accepted method; D011'in belirlediği Environment önce tanınır, ayrıntılı çözüm seçimi ihtiyaçla karşılaştırılır |
| **D006** | EXP-001/002/004 okumalarından çıkan kapsamlı SOUL hedef tanımı bu aşama için **yeterince somut çalışma hedefi** kabul edilir; nihai SOUL tanımı/mimarisi olduğu iddia edilmez. | accepted stage gate |
| **D007** | B1–B9, SOUL modül listesi değil Development OS'un SOUL üzerinde yapacağı birinci seviye Work alanları olarak kullanılır. | working map accepted for continuation; taxonomy not final |
| **D008** | Her B dalı şu sırayla açılır: Work → gerekli DevOS kabiliyet/sorumlulukları → bunları taşıyan AI rolü / mekanik sorumluluk / insan sınırı → daha sonra sistem yapısı. | accepted method |
| **D009** | EXP-006, yalnız konuşma arşivi olarak büyütülmeyecek; fresh-session devrini sağlayacak WORK/ACTORS/DECISIONS/HANDOFF ve aktif Work dosyalarıyla yaşayan çalışma yüzeyine dönüştürülecek. | explicitly accepted |
| **D010** | EXP-006 cevapları ana sonucu örnekler, geçmiş özeti veya uzun muhakeme anlatısıyla gömmeyecek. Varsayılan çıktı kısa sonuç, gerekiyorsa karar-kritik belirsizlik ve plan içindeki tek devam noktasıdır. Ayrıntı repoda tutulur; kullanıcı ayrıca istediğinde açılır. | explicitly accepted communication rule; U002-A ile pekiştirildi |
| **D011** | DevOS, SOUL'u yaratmak için **Claude Code cloud** ortamında çalışacak. Tasarımdan önce bu Environment'ın gerçek imkân/sınırları Anthropic'in birincil kaynaklarıyla öğrenilecek. | explicit user constraint/direction; U002-A/B |
| **D012** | SOUL'un ilk ve sonraki işlerini kurulacak DevOS ekibi keşfedecek, değerlendirecek, planlayacak ve yürütecek. Assistant'ın işi bu ekibin çalışacağı düzeni ortaya koymaktır; ekibe hazır SOUL backlog'u seçmek değildir. | explicit scope boundary; U002-A ve önceki geçiş düzeltmesi |
| **D013** | Roller birbirinden bilgi, araştırma, değerlendirme veya kontrol isteyebilmeli; talep doğru çalışmaya ve geri dönüp kullanılan sonuca bağlanmalı. Mesajlaşma/repository veya başka bir yöntem seçimi açık. | explicit communication requirement; U002-B |
| **D014** | Normal çalışma akışında her rolü/sonraki işi Batu'nun elle tetiklemesi gerekmemeli. Gerektiğinde müdahale, başlangıç/yeniden başlatma ve yetki/kabul mümkündür; sonsuza kadar insan-bağımsız çalışma istenmiyor. | explicit autonomy boundary; U002-B/C |
| **D015** | SOUL ürün çıktıları ile DevOS'un kendi iş/bilgi/karar/devam kayıtları ayrı amaçlarla, ilişkileri korunarak yönetilecek. Fiziksel repository/dosya şeması henüz seçilmedi. | explicit requirement; U002-A |
| **D016** | Foundation, özellikle WORK ve INFORMATION, bakış açısını ve gereklilik keşfini besleyecek; studies bu çerçeveyle okunarak uygulama örnekleri/sınırları sağlayacak. | explicit research-use direction; U002-A |
| **D017** | Claude incelemesinden önce mevcut EXP-006'ya bağlı, yeni oturum/turlarda devralınabilir bütünsel plan kalıcılaştırılacak. Üst harita baştan görünür olacak; turlar ayrıntıyı açacak veya gerekçeli revizyon yapacak. | explicit planning/persistence authorization; U002-A/C |
| **D018** | Kanon/v2 karşılaştırmasının amacı manuel tetikleme farkıdır. `loopinance_v2`nin bütün düzeni veya ECC'nin DevOS'a aynen alınması istenmedi. | explicit example/adoption boundary; U002-C |
| **D019** | Alt ajan/takım ve bütünleşik teknik seçim P4'te değerlendirilecek; kullanıcı bu ayrımı anladığını belirterek P2'ye devam edilmesini istedi. | explicit sequencing confirmation; 27 Eylül 2026; belirli topoloji veya henüz üretilmemiş rol taslağı onayı değil |
| **D020** | P3'te araştırma örnekleri/metodolojileriyle derinleşilecek; assistant hemen karar vermek yerine bir başlangıç yapısı sunacak ve kullanıcıyla bu baz üzerinde değerlendirecek. | explicit discussion/return boundary; 27 Eylül 2026; P3-01 önerisinin kabulü değil |
| **D021** | İçerik sahibi ne söylendiğini ve gerekçesini; çalışma düzeni tarafı dosya/kayıtların yerini, statüsünü, kaynak/sürüm ilişkilerini, bulunabilirliğini, bakımını, devrini ve yeniden kullanımını taşır. Düzen tarafı anlamı yeterince anlayabilmeli, fakat ürün kararını üstlenmemeli. Düzen yalnız görsel klasör temizliği değildir. | Kullanıcının “aynı fikirdeyim” yanıtıyla kabul edilmiş sorumluluk sınırı; 27 Eylül 2026. Ayrıntılı şema, tüm P3 kuralları veya fiziksel ayrı ekip onayı değil. |
| **D022** | P3 tasarım devrine hazır sonucu ve P4 devam noktası sunulduktan sonra kullanıcının “devam et” yönü P4 bütünleşik teknik tasarımını açar. | 27 Eylül 2026, aşama yetkisi; P4-01 tercihinin kullanıcı kabulü, P3'ün bütün ayrıntılarına formal onay veya P5 kurulum izni değildir. |
| **D023** | Rapor yüzeysel tarama/küçük eklerle değil, SOUL'un ne olacağına göre DevOS gereksinimleri yeniden türetilerek baştan yazılacak; gerekli kalite uygulama kolaylığı lehine düşürülmeyecek. | Açık kullanıcı yeniden yazım yönü; v2 teslimi P4-02'de. Yeni teknoloji/mimari kabulü veya karmaşıklığın üstünlüğü değil. |
| **D024** | V2 yapı stres testine alınacak ve rapor **sayfa sınırı olmadan** yeniden hazırlanacak. Önceki 200 sayfa koşulu kaldırıldı. | Açık kullanıcı talebi; görünür kaynak P4-03 §1. Eksiklerin sayfa sınırından kaynaklandığının kanıtı veya v3 başarısı değil. |
| **D025** | Yarım kalan stres testi/yeniden yazıma yeni oturumda devam edilecek; mevcut tur repository durumunu ve kaynak devrini hazırlayıp duracak. | Son açık kullanıcı yönü; P4-03 §1. Bu tur yeni stres testi/rapor çalışması veya P5 kurulumu yapılmaz. |
| **D026** | Yeni oturumda eklenen gerçek devir paketi üzerinden aynı P4 sayfa sınırsız stres testi ve rapor çalışmasına devam edilecek. | 28 Eylül 2026 açık devam talebi; P4-04 §1. D025'in önceki turda durması tamamlandı. Yeni mimari kabulü, P5/P6 veya SOUL backlog seçimi yetkisi değil. |

D011–D018 [U002](sources/U002-cloud-plan-and-autonomy.md)'ye; D019 P1 açıklamasından sonraki devam yönüne; D020 ilk P3 isteğine dayanır. D021 kaynak açıklama/kabulü [P3-01 §1](work/P3-01-work-information-discussion.md#1-kullanıcı-yönü-ve-önerinin-sınırı)'de, D022 P3→P4 devam bağlamındadır. D023 [P4-02 §1](work/P4-02-soul-derived-report-v2.md#1-yetki-ve-neden-yeniden-yazıldı), D024/D025 [P4-03 §1](work/P4-03-unbounded-stress-test-handoff.md#1-kullanıcı-yönü--görünür-konuşma-kaynağı) ile izlenir. D023–D025 kayıtlarının eklenme tarihi 28 Eylül 2026'dır; daha önceki mesajlara kesin zaman damgası uydurulmaz. D026'nın görünür kaynak ifadesi P4-04 §1'de korunur.

## Teknik öneriler — kabul edilmiş kullanıcı kararları değildir

P4-01'in ana Y + özel alt ajanlar/Git ağırlıklı tercihi eski baseline'dır. V2'nin takım ağırlıklı bilişsel ekip, dış korunan kontrol, PostgreSQL canlı durum/typed graph, Git ürün, memory/context compiler ve kontrollü publisher/recovery önerisi P4-02 ve gerçek v2 kaynaklarında bulunur. V3 bu yönü koşullu değerlendirip sözleşme/model sınırlarını güçlendirdi; sonuç ve sekiz karşı örnek P4-04'tedir.

**Current: P4 v3 rapor/kanıt teslimi hazır, kullanıcı değerlendirmesi bekleniyor.** PostgreSQL, graph store, takım veya bileşenler otomatik kabul edilmiş sayılmaz. Gereken kabiliyet ne kolaylık lehine atlanır ne daha karmaşık gösterilerek sağlanmış sayılır.

D013/D015 içindeki başlangıç “seçimi açık/henüz seçilmedi” ifadeleri kullanıcı kısıtının o zamanki durumudur; assistant tercihleri bunlardan ayrı tutulur. Actual hedefte gerçekleşme/uygulanabilirlik ayrıca kanıtlanacaktır.

## Açık kalanlar ve kanıt sınırı

Nihai mimari, gerçek actor allocation, actual cloud/servis yetkileri, bağımsız güvence, PostgreSQL concurrency, korunan DB–Git publication, dağıtık restore ve SOUL bilişsel yeterliği açık. P2/P3/v2/v3 nihai kadro veya çalışan DevOS değildir. Motivasyon başına agent ve belirli graph/iş takip ürünü kabul edilmedi.

V2 40 test/dört guard bu tur yeniden koşuldu. Önceki dört ipucu yeni v2 karşı örnekleriyle kapsamlandırıldı; toplam sekiz bulgu vardır. V3 53 yerel test geçti; yeni sekiz bozma yedi assertion/tek KeyError olarak ayrılır. Eski “88 test geçti” iddiası hâlâ teyitsiz tarihsel beyandır; yeni sonuçlar onun doğrulaması değildir.

**Plan v1.7 / P4 V3 RAPOR TESLİMİ HAZIR / DEĞERLENDİRME BEKLİYOR.** P5/P6 başlamadı. Tam rapor/kod kaynak paketindedir; repository current state ve devam yolunu taşır. D010'un agent-control karşılığı önceki yetkili değişiklikle canonical-work-preflight protokolündedir; bu tur agent-control değişmedi.
