# EXP-004 — STATE

**Güncelleme:** 2026-09-21, DQ04 yerel dersten koşullu aktarıma ve baz davranışa.
**Arşiv:** REPAIRED / MAIN-PUBLISHED. Önceki kaynak-kısaltma/yönlendirme eksikliği o kapsamda kapalıdır; platform export'u veya bağımsız transkripsiyon doğrulaması iddiası yok.
**Arşiv yayını:** PR #31; merge `b949fe66454a1943ac9c99827e79f68f962658be`, kapanış `e372ed7558b0b0ebbf388c864b0733382d1418ba`. [PUBLICATION](checks/PUBLICATION.md) onarımın tarihsel kontrol kaydıdır; sonraki devamların yayını değildir.
**Güncel kavramsal çalışma:** [DQ04 — Yerel dersten koşullu aktarıma ve baz davranışa](continuations/DQ04-CONDITIONAL-TRANSFER-AND-BASE-ADMISSION.md). Aktarım nesnesi, kaynak–hedef koşulları, geçerlilik/paylaşım-yetkisi/fiilî-uygulama kapsamları ve yöntemi doğru yerde seçme/kullanmama ayrıldı. T08/S015'in mevcut sınırları inceltildi; gerçek öğrenme, T16 veya mimari kabulü yoktur.
**Önceki iş anlayışı çalışması:** [DQ03 — İş anlayışını yeniden açmak, yetkiyi ve geçerli işi korumak](continuations/DQ03-WORK-FRAME-REVISION-AUTHORITY-AND-PRESERVATION.md), yayın `97627337ad622b715f3a9c562d62bb11ecda5d31`. Yeni bulgunun yerel görev yerine planın amaç yeterliği gerekçesini zedelediği durum incelendi. Epistemik düzeltme/yetkili değişiklik, desteğin çekilmesi/ters sonucun kabulü, eski iş/kanıtın kullanım-bağlı korunması ve ölçüt değişiminde karşılaştırılabilirlik ayrıldı. Tamamlanmış kavramsal çıktı yeniden yapılacak iş değildir.
**Önceki yöntem seçimi çalışması:** [DQ02 — Keşif yöntemini seçmek ve ortak körlükleri sınamak](continuations/DQ02-DISCOVERY-METHOD-SELECTION-AND-COMMON-BLIND-SPOTS.md), yayın `3a9359a8bdf75203358dcda5b2fcdb2fb3eac3ef`. DQ01'in açık sorusu Foundation ve seçili studies sonuçlarıyla karşılaştırıldı. Soru açan keşif/ayırt edici inceleme, uygulanabilir bilgi yolu, yöntem edinimi/gerçek kullanım ve gizli kusur/gizli kabul kuralı ayrımları inceltildi. Tamamlanmış kavramsal çıktı yeniden yapılacak iş değildir.
**Önceki kavramsal devam:** [DQ01 — İşaret edilmemiş ihtiyacın keşfi ve yetkinliğin gerekçelendirilmesi](continuations/DQ01-UNSIGNALED-NEED-DISCOVERY-AND-CAPABILITY-QUALIFICATION.md), yayın `06dcefc2f192cb0cd4eb216d3f3194c2bfa48269`. İhtiyaç adayı/gerekli koşul, eksik sonuç/yetkinlik açığı, denenebilir aday/kullanım-bağlı kapasite desteği/somut sonuç kabulü ayrıldı. Tamamlanan kavramsal çıktı yeniden yapılacak iş değildir; uygulamada açık kapasite sürer.
**Tamamlanmış ara sentez:** [SY01 — İki senaryodan çalışma sistemi sorumluluklarına](artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md), yayın `000786d1f7742ac87937017ac9cea18a5e329865`. T1–T15, ortak sorumluluklar, alana özgü yöntemler ve açık kapasite/kanıt yükleri üzerinden Development OS, SOUL ve kullanıcı işiyle ilişkilendirildi. SY01 yeniden yapılacak iş değildir.
**Son kavramsal test:** [T15 — Roman: editoryal anlaşmazlık, gerekçeli seçim ve kapanış](continuations/T15-NOVEL-EDITORIAL-DISAGREEMENT-AND-CHOICE.md), yayın `9ce108652e7383ef6a0390fd5272193925cf6fb5`. Olgusal itiraz, yorum/okur-etkisi tahmini, yaratıcı tercih, müdahale ve karar yetkisi ayrıldı. Gerçek roman, ayrı editör ajanları veya okur deneyi yapılmadı.
**Önceki roman çalışmaları:** [T14](continuations/T14-NOVEL-READING-COVERAGE-AND-JOINT-CONTEXT.md), yayın `2d0ac0a650f9f5055ea254b620c7518e78e7fb46`; [T13](continuations/T13-NOVEL-SEMANTIC-REVISION-AND-IMPACT.md), yayın `eaa125ef37090f06e65b829d32e1acd22e7c9406`; [T12](continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md), yayın `4794cf71c27c1d12d02034bc8891423647618570`; senaryo seçimi [SC02](continuations/SC02-NOVEL-SCENARIO-ASSESSMENT.md). T1–T15 konuşma içi kavramsal/sentetik denemelerdir; SY01 ve DQ01–DQ04 yeni T testi sayılmaz.
**Korunmuş kaynak kesimi:** U001–U016 / S001–S015; 31 görünür mesaj, 16 kaynak dosyası. [Diyalog](sources/conversation/INDEX.md), [manifest](SOURCE-MANIFEST.json). T09–T15, SC02, SY01 ve DQ01–DQ04 notları bu sayımı genişletmez; assistant kaynak transkripti değildir.
**Önceki teknik yayınlar:** PR #29 `46ab3ff5993683c6124d7786533529e0f6147914`; PR #30 `882e0dfd271bd8c284df59f81c882a66a88f9933`. Bunlar eski tamlık iddiasını doğrulamıyordu.

## Amaç ve yetki

Foundation/studies birikimiyle SOUL'un büyük, uzun, çok aktörlü ve baştan tamamen bilinmeyen bir iş için ihtiyaç duyacağı çalışma düzenini sorgulamak. Örnekler otomatik modül, yöntem, kavram tanımı veya mimari kararı değildir.

U014 arşiv yetkisi, U015 T08 devamı, U016 önce arşiv onarımı ve büyüme/branch açıklamasıydı. Onarım kapandı. Sonraki devam yönleriyle T09–T11 yapıldı. Roman SC02'de alternatiflerle değerlendirilip öncelikli ikinci senaryo önerisi oldu; sonraki onaylarla T12–T15 ele alındı. Kullanıcının Development OS, SOUL ve kullanıcı işi bakımından katkıyı vurgulamasının ardından gelen «devam et lütfen» yönü, önerilmiş SY01 ara sentezini yetkilendirdi. Gerçek roman üretimi, yayıncılık girişimi, SOUL/Development OS kurulumu veya agent-control değişikliği yoktur. Olumlu kullanıcı değerlendirmesi modele veya yeni yaratıcı fikre doğruluk/üstünlük kanıtı değildir.

DQ01 için yeni kullanıcı yönü, güncel main ve zorunlu protokoller üzerinden devralmayı; SY01 sonrasındaki işaret edilmemiş gereksinim/yetkinlik açığı sorusunu kavramsal olarak sürdürmeyi; önemli sonuçları yalnız EXP-004 içinde korumayı açıkça yetkilendirdi. Güncel state önceki devirle uyumlu bulundu. Foundation, studies, concepts ve agent-control yazma kapsamı dışındadır. Keşif algoritması benimseme, canlı değerlendirme kampanyası veya implementasyon yetkisi oluşmaz.

DQ01 sonrasında kullanıcı araştırma kullanımını sordu. Önceki doğrudan kullanımın EXP-004 ve seçici RPD ağırlıklı olduğu açıklandı. Ardından gelen çalışma devamı DQ02'nin kaynak-beslemeli kavramsal karşılaştırmasını yetkilendirir; Foundation/studies'i değiştirme veya gerçek deney/implementasyon izni değildir. Önceki dar kullanımın bağlam dolmasından kaynaklandığı doğrulanmış neden sayılmaz. Bu paragraf yetki özetidir, kaynak arşivine eklenmiş transkript değildir.

DQ02 sonrasındaki «güzel. devam et.» yönü, yeni keşfin iş/başarı/yöntem anlayışını değiştirmesi sorusunun DQ03'te aynı kavramsal kapsamda ilerletilmesini yetkilendirdi. Yeni soru-bankası amacı yalnız düşünsel varyanttır; eski brief'e gerçek kabul şartı olarak eklenmez. Bu tur da Foundation, studies, concepts, agent-control ve target implementation yazılmaz.

DQ03 sonrasındaki «peki devam et.» yönü, yerel dersin başka işe veya baz SOUL'a aktarılması sorusunu DQ04'te aynı exploration kapsamıyla sürdürür. Gerçek yerel yöntem başarısı varsayılmaz; kavramsal bulgular ile olası gelecek davranış kanıtı ayrıdır. Yazma yalnız EXP-004 içindedir; baz SOUL veya agent-control davranışı değiştirilmez.

## Korunmuş kaynak onarımı

İlk S001–S013 yoğunlaştırılmış/yeniden ifade edilmişti; S013'e sonraki kullanıcı kararına atıf eklenmişti. Bu eski görünümler [tarihsel dizinde](artifacts/condensed-before-repair/README.md) aynı Git kimlikleriyle korunur. Güncel kaynak yollarına görünür özgün yanıtlar kısaltılmadan yeniden aktarıldı. S014 eski yanlış tamlık bildirimi, S015 tam T08 cevabı, U016 onarım kaynağıdır. Sonraki onarım cevabı ve devam turları eski kesimin dışındadır.

Kaynak payload ref'i `f1e93a9f052fb98b3f2e28e987233f3b51193534`; assistant tree `ba3111b97927ebb231947b2a500eee1d534a5a16`; kullanıcı blob'u `1866f243b3771a2d0152bc6b20f67c1a7f3f80c3`; arşiv başlıkları dahil 182.486 byte. Bunlar kimlik/transfer göstergeleridir, bağımsız doğal-dil sadakati kanıtı değildir. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md), [onarım kontrolleri](checks/REPAIR-20260921.md). Bu tur kaynaklar/manifest/onarım kanıtı değişmez.

## T1–T10'dan devir — hipotez, mimari değil

T1 ham talep/Mission; T2 ihtiyaç-koşul/Work/plan/eylem ve sürekli keşif; T3 rol/aktör/capability/competence/authority; T4 bilgi/bağlam/kullanım; T5 araç/Run/gerçek etki; T6 tamamlanma/kanıt/kabul/entegrasyon/amaç etkisi; T7 kayıt, Actor/Run/Work sürekliliği ve gerçek durumla uzlaştırma ayrımlarını açtı.

[T1–T7 konsolidasyonu](artifacts/CONSOLIDATION.md) ve reflection'lar kendi checkpoint'lerinin tarihsel türevleridir. Geniş kategorilere yerleştirebilmek uygulama yeterliliği veya bağımsız Foundation doğrulaması değildir.

[T08](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) / [S015](sources/conversation/assistant/S015.md): ders kaydı, fiilî geri bildirim, kalıcı değişim, fayda, yetki ve transfer ayrı. Yöntem değişimi de kanıtı/etki yolu/geri dönüşü olan Work olabilir.

[U016](sources/conversation/USER-MESSAGES.md#u016) yeni işlevlerle mevcut işlevlerin yeni katılımı kapsamasını birlikte düşünür. Dikey/yatay, iki dosya ve klasör açıklayıcı örneklerdir; branch çağrışımı araç seçimi değildir. [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) kaynak/yorum sınırını korur.

[T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md): tekil uygunluk ortak uygunluk değildir; tekil hazırlık ortak kapasite taahhüdü değildir; güvenli uçlar güvenli geçişi garanti etmez. T09 yayını `7de46ddbae29366cb4338b41f57d844a611a43d8`.

[T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md): yeni yol eski kontrol bozulmadan kapsam dışına çıkabilir. Yetenek oluşturma/etkilere kabul, yükümlülük/kontrol tekniği, doğrudan/dolaylı etki, gerekli/uygulanmış/gözlenmiş kapsam ayrılır. Kritik etki beklerken gerçekten sınırlanmış yararlı işler sürebilir. T10 yayını `42ee649f9dfb0809f76555f70b4694297a5e8a8c`. C10 karşı durumları çalıştırılmış deney değildir.

## T11 — Yeni katkı ve sınırı

[T11](continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md) kontrol/araştırma yüzünden teslim edememeyi karşı-test yapar. Kurulu vakada, ilk kullanım için bağımsız yararlı kademeli teslimat önceden izinlidir; 40 metin sorusu o dilimin gerekli şartlarını karşılar, 10 ek görselin güvencesi açık kalır. Uygun dilim ilerleyebilir; görseller ve yıllık program tamamlandı sayılmaz. Görsel zorunluysa veya bölme yetkisi yoksa aynı karar çıkmaz.

Açık soru her karar için blocker değildir; hedefin gereği ile seçilmiş yöntemin gereği, bugünkü koşulla gelecekteki ihtiyaç ayrılır. Kanıt yeterliliği belirli sonraki etki/kullanım/sürüm içindir; en iyi yöntemi bulmuş olma veya kusursuzluk iddiası değildir. Aynı-kör incelemenin tekrarı kanıt üretmez; kritik karşı kanıt ise yorgunluk/bütçe nedeniyle bastırılamaz.

Ek araştırmanın karar/güvence katkısı ile gecikme/kaynak/fırsat maliyeti birlikte düşünülür. Kesin olasılık veya skor uydurulmaz, zorunlu yetki/kabul şartı tek fayda puanına eritilmez. Tek araştırma adımıyla sınırlı bakmak da yetersiz olabilir; tamamlayıcı sınırlı araştırma dizisi değerli olabilir. Metareasoning maliyeti ikinci sonsuz süreç haline getirilmez.

Araştırmayı durdurmak, bütçede kesilmek, eseri kabul etmek ve işi başarıyla bitirmek ayrı sonuçlardır. Yerel kapanışın kapsamı/dayanağı/kalan belirsizliği ve yeniden açma koşulları korunabilir. Bekleyen işler sorumlusu ve geri dönüş koşuluyla açık kalır. Her yeni oturum kapalı işleri yeniden açmaz; maddi yeni kanıt açabilir.

C11-1–8 tasarlanmış karşı durumlardır; gerçek model veya runtime'da çalıştırılmadı. RPD repository değerlendirmesi ve Foundation REUSE seçici kullanıldı. Callaway ve diğerlerinin 2018 metareasoning yazısı HTML §§2.1–2.2 ve Horvitz abstract'ı dar dış dayanak olarak okundu. RPD asıl ekleri yeniden edinilmedi; BMPS/yeni mekanizma/ürün veya architecture adoption yoktur.

## SC02 — İkinci senaryo değerlendirmesi

[SC02](continuations/SC02-NOVEL-SCENARIO-ASSESSMENT.md), romanı araştırma kitabı ve müze sergisi alternatifleriyle nitel olarak karşılaştırır. Öncelikli öneri romandır: uzun bağlam yanında parça-bütün niteliği, kurmaca olay/karakter inancı/anlatıcı/okur ayrımı, yaratıcı keşif, geriye etkili yeniden yazım ve editoryal/okur değerlendirmesi için güçlü adaydır. Fiziksel etki ve bağımsız dış aktör kapsamını tek başına sınamaz; bütün SOUL için yeterlilik testi değildir.

Kullanıcının 'tek oturuma sığmayacak' ifadesi bütün güncel modellere dair teknik olgu yapılmaz. Sınırlı çalışma bağlamı bir deney koşulu olabilir; kaynağa geri erişim ve bütünsel değerlendirme açık kalır. Hazırlık, bütün yaratıcı kararları baştan kilitleme değildir. Her karakter/bölüm için ajan veya tek yazarlık mimarisi seçilmez. Yaratıcı belirsizliği düzeltilecek hata sanmak ile gerçek hatayı belirsizlik diye korumak iki ayrı failure adayıdır.

EXP-001'in roman/yaşayan plan izi seçici geri çağrıldı. Re3, DOC ve Lost in the Middle abstract'ları ile Kukkonen'in Plot maddesinin ilgili bölümleri dar dış kaynak olarak kullanıldı; tam roman ölçeğinde etkinlik, güncel bütün modellerin performansı veya yöntem üstünlüğü iddia edilmedi. Ayrıntılı kaynak/okuma sınırları SC02'dedir. SC02 içinde son kullanıcı mesajının ayrı kaynak alıntısı bulunur; bu, korunmuş arşivin veya assistant transkriptinin genişletildiği anlamına gelmez.

## T12 — Romanın ilk yazılabilir işi

[T12](continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md), yaratıcı hazırlık ile yazmaya başlama eşiğini sınar. Hazırlığın bütün romanı kilitlemesi veya ham brief'ten doğrudan Chapter 1 üretimine geçilmesi iki uç risk olarak ayrıldı.

Roman Information'ında kullanıcı yaratıcı sınırı, committed story state, provisional design hypothesis, deliberately unresolved, undecided, character belief/knowledge, reader exposure ve draft text'in aynı statü olmadığı görüldü. Bunlar yeni zorunlu schema/servis değildir; yaratıcı continuity için non-collapse baskılarıdır.

İlk Work'ün nihai bölüm olmak zorunda olmadığı; decision-critical yaratıcı belirsizliği sınayan exploratory scene/probe olabileceği ortaya çıktı. Exploratory draft → observation → candidate decision → accept/reject/open → committed state akışı adaydır; yazılan fikir sırf metinde bulundu diye kanonlaşmaz. Rejected/superseded olasılıkların sonraki özet/context'te current fact'e dönüşmesi ayrıca failure mode'dur.

Creative/story state, narrative/work plan ve manuscript ayrıldı. Plan değişikliği prose'un değiştiğini, prose'daki character/reader state'inin world truth olduğunu göstermez. Working context gerektiğinde asıl prose'a dönmelidir; özet voice/ima/ritim için source yerine geçmeyebilir.

C12-1–8 sentetik karşı durumlardır; canlı model/roman testinde çalıştırılmadı. Yeni Foundation ground veya roman-özel zorunlu mimari kabul edilmedi.

## T13 — Yeni katkı ve açık sınır

[T13](continuations/T13-NOVEL-SEMANTIC-REVISION-AND-IMPACT.md), Derya'nın kendi suçunu sakladığı A yönüyle Selin'i korumak için sustuğu B adayını karşılaştırır. B, Derya'nın Selin'e ilişkin inancını gerçek olayla eşitlemez. Yeni aday daha iyi veya benimsenmiş sayılmadı; gerçek romanın üçte birinin mevcut olduğu iddiası yoktur.

Kurulan P02 defteri saklama davranışı iki motivasyonla da uyumlu olabilir; gerekçe değişince metin otomatik silinmez. P04 güvenilir açık olay bildirimi B ile çelişir. P07, Derya adı geçmeden şüpheyi doğuracak olanak/gerekçe sorununu açabilir. Yeni motivasyonu hazırlayan ilişki hiç yazılmamışsa yeni Work doğar. Etki haritası mevcut dosya/ad listesinden ibaret değildir.

Tutarlılık, gerekçelendirme ve bütünsel edebî etki ayrı: erken açıklama çelişkiyi giderirken sırrı bozabilir. Aynı metnin kullanım/tema bağlamı değiştiğinde önceki editoryal hüküm otomatik güncel değildir. Geçerli etkilenmemiş içerik/kanıt korunabilir; minimum kelime değişimi veya toptan yeniden yazım zorunlu kural değildir.

Aday yönü incelemeye alma, revizyon yönünü benimseme, metnin fiilen değişmesi ve bütünsel kabul ayrı tutulur. Eski/yeni plan-özet-metin karışımı kontrol edilir; bütün bağımsız işler otomatik durmaz. Yazar açıklamasını bilen okuma, yalnız metinden edinilen okur izlenimini ölçmüş sayılmaz.

C13-1–10 tasarlanmış karşı durumlardır. Foundation Revision M5, OpenSpec'in pin'e bağlı bulguları, Qin ve diğerlerinin 2019 counterfactual rewriting abstract'ı ve Kukkonen'in Plot maddesi seçici dayanak oldu. Asıl roman, canlı sistem, okur deneyi veya yeni mimari yoktur; mikro-parçalardan roman ölçeği yeterliliği çıkarılmadı.

## T14 — Okuma kapsamı ve ortak değerlendirme bağlamı

[T14](continuations/T14-NOVEL-READING-COVERAGE-AND-JOINT-CONTEXT.md), bir mektubu Derya'nın okuduğu V+ ile yalnız Selin'in gördüğü V− varyantlarının aynı kaba özete dönüşebildiğini gösterir. Derya'nın sonraki inanç değişimini gerekçelendirme sorusu bu farkı gerektirir. Başka aktarım olmadığı küçük fixture koşuludur; görülmemiş romanda yokluk iddiası değildir. B yönü hâlâ koşullu adaydır.

Bölümlerin ayrı ayrı okunması, karar için gereken ilişkilerin birlikte değerlendirilmesi değildir. Yeterli özet kullanılabilir; yetersiz görünümde kaynağa dönülür. Anlatı sırası, karakter inancı, anlatıcı iddiası, okura açılan metin ve yorum ayrılır. Okura gösterilen bilgi gerçek okur öğrenmesi sayılmaz. Kaynak konumu ve okuma izi anlama kanıtı değildir.

Aday okuma düzeni; nesne/sürüm kapsamı, kaynak boyunca okuma, açık soruların taşınması, gerektiğinde ilişkili pasajların birlikte görülmesi ve geniş iddialar için bütünsel geri dönüşü içerir. Bunlar zorunlu modül, her tur tam okuma veya bütün sahne çiftlerini karşılaştırma talebi değildir. Kısmi/özet/karışık sürüm incelemesi tam-eser kabulüne yükseltilmez.

Foundation Use-Conditioned Selection U5'in kabul edilmiş sınırları ve Context/Memory/Harness STATE seçici kullanıldı. FABLES 2024 v2 ve NoLiMa 2025 v3 abstract/kayıtları dar dış dayanak oldu; model sıralaması veya roman ölçeği başarısı çıkarılmadı. C14-1–10 tasarlanmış karşı durumlardır; gerçek runtime/okur deneyinde çalıştırılmadı.

## T15 — Editoryal anlaşmazlık, seçim ve kapanış

[T15](continuations/T15-NOVEL-EDITORIAL-DISAGREEMENT-AND-CHOICE.md), aynı sahneyi inceleyen açıklık/örtüklük yönlü eleştirileri karşılaştırır. Kaynak/sürüm farkı, yorum veya okur-etkisi öngörüsü, yaratıcı değer ve karar yetkisi ayrıdır; karma itirazlar tek sınıfa zorlanmaz. Doğru tespit, önerilen müdahalenin doğru veya tek çözüm olduğunu göstermez.

Çoğunluk otomatik bağımsız kanıt veya kullanıcı tercihi değildir. Skor/ağırlık seçimleri ve zorunlu sınırlar görünür tutulur; uzlaşma veya bütün itirazları sıfırlama amaç değildir. Kapsam içi yaratıcı takdir verilmişse her karar kullanıcıya geri havale edilmez; verilmemiş yetki sessizce varsayılmaz.

Yerel fixture, ilişkisel dönüşümün görünür olmasını ve ahlaki hükmün açık bırakılabilmesini varsayar. Derya'nın belgeyi teslim ederken müdahaleden geri çekildiği küçük pasaj, denenecek revizyon yönüdür; tüm B yönü veya roman benimsenmedi. Açıklık eleştirisinin kaygısı korunur, uzun açıklama reçetesi zorunlu sayılmaz. Başka yaratıcı sözleşmede seçim değişebilir.

Karar, gerçek uygulama, değerlendirme ve teslim ayrı. Seçilmeyen tercih çürütülmüş sayılmaz; geçerli itirazın sınırı ve yeniden açma koşulu korunabilir. Aynı itirazın tekrarı otomatik yeni kanıt değildir; maddi karşı kanıt eski kapanıştan muaf tutulmaz. C15-1–12 tasarlanmış karşı durumlardır; ayrı ajan/okur deneyinde çalıştırılmadı.

Foundation Composite Standing STATE, Multi-Agent Patterns'ın seçili tarihsel değerlendirmesi, Editors Canada 2024 HTML bölümleri ve Zheng ve diğerlerinin 2023 LLM-judge yazısının ilgili metni kullanıldı. Mesleki rehber estetik oracle, eski model verisi bugünkü performans, eski target mimarisi current yetki yapılmadı. Yeni Decision Agent veya evrensel puanlama sistemi seçilmedi.

## SY01 — İki senaryonun ara sentezi

[SY01](artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md), T1–T15'i sekiz geçici sorumluluk grubunda toplar: amaç/kapsam/takdir; ihtiyaç ve Work keşfi; işin konusu/bilgi/bağlam; yeterli yetkinlik ve ortam; ortak koşullarla yürütme; değerlendirme/seçim/teslim; süreklilik/değişim/onarım; çalışma düzenini kontrollü geliştirme. Bu sekiz-modüllü architecture veya yeni Foundation hiyerarşisi değildir.

İşin takibi ile işin konusunu anlama ayrılır. Sorumluluk, temsil, mekanizma adayı, gerçek kapasite ve gösterilmiş sonuç birbirine yükseltilmez. Ortak yükümlülük her alanda aynı yöntemi gerektirmez; soru-bankası tümüyle nesnel, roman tümüyle öznel diye ayrılmadı.

Kullanıcı işinde gerekli sonuç, SOUL'un bunu fark edip karşılayacak kapasitesi ve Development OS'un ileride o kapasiteyi geliştirme/doğrulama yükü ayrı ilişkilendirildi. Bunlar birbirinden kopuk üç yazılım katmanı değildir; başarı bir düzeyden diğerine otomatik aktarılmaz. Gerçek target-repository uygulama durumu SY01 turunda araştırılmadı.

Üç söyleyiş inceltildi: Work-first zorunlu zaman sırası değil; aktör/bilgi/ortamla karşılıklı keşif var. Aktör/ortam doğrulanmamış frontier koşullu adaydır. Plan gerçek Work değildir ama kabul/bağlar üzerinden denetim etkisi taşıyabilir. Her keşif meta-work değildir; nesnesine göre kullanıcı işinin doğrudan parçası olabilir. Eski kaynaklar bu yeni yorumla yeniden yazılmaz.

En belirgin açık kapasite, işaret edilmemiş yük taşıyan ihtiyacı/ilişkiyi fark etmek ve gereken yeterliği gerçekten sağlamaktır. Karşıörnekleri açıklamak bunu başarmak değildir. SY01 turunda yeni canlı deney, gerçek roman, başarı ölçümü veya T16 yapılmadı. Yeni dış araştırma yapılmadı; mevcut kaynaklar seçici yeniden kullanıldı, o turun tam okuma sınırları SY01'de kayıtlıdır.

## DQ01 — Yeni katkı ve açık kapasite

[DQ01](continuations/DQ01-UNSIGNALED-NEED-DISCOVERY-AND-CAPABILITY-QUALIFICATION.md) SY01'in açık sorusunu ilerletir. Kullanıcı tarafından söylenmemiş, başka kaynakta açık, mevcut görünümde eksik, ilişkilerde örtük ve yeni yöntem/kararla doğan ihtiyaçlar aynı durum değildir. T14'ün aynı özete dönüşen V+/V− farkı, görünümde gerçekten bulunmayan ayrım için kaynak/gözlem veya koşullu hüküm gerektiğini gösterir. Eksik cevabı bilmeden araştırılacak soruyu fark etmek ayrı bir kapasitedir.

Aday keşif, amaçlanan sonuç ile yapılan iş/çıktı arasındaki dayanağı; gerçek kullanım, etkileşim ve değişiklikler karşısında sorgular. Geriye koşul araştırması, ileriye kullanım/etki takibi, sınırlı kaynak okuması ve farklı dayanaklı inceleme birbirini tamamlayabilir. İhtiyaç adayı otomatik zorunlu koşul değildir; alternatif yöntem, yaratıcı tercih ve yetki ayrıca değerlendirilir. Bu hareketlerin güvenilir keşif sağladığı ölçülmedi.

Eksik sonuç; edinilmemiş bilgi, yanlış/eski görünüm, kullanmama, yöntem/ölçüt kusuru, alan yeterliği, erişim/kaynak/yetki veya değerlendirme hatasından kaynaklanabilir. Tek başarısızlık doğrudan yeni uzman ajan gereğini göstermez. Yeterlik, belirli aktör-yöntem-bilgi-ortam-kullanım birleşimi için düşünülür; yeni zorunlu şema değildir.

Denemeye değer aday, belirli kullanım için desteklenmiş kapasite ve somut çıktının/etkinin kabulü ayrı. Gereksinim üretimi ile değerlendirmenin aynı eksik çerçeveyi paylaşması yeşil sonuçları yanıltabilir. Aynı T14 kusurunu zaten bilerek yeniden açıklamak işaretlenmemiş keşif kanıtı değildir. Sağlam durumları reddetmeme, yeterli kaynak bulunmayan durumda belirsizliği koruma, gereksiz gereksinim üretmeme ve yararlı ilerleme de sınama yüküdür; bu tur ölçülmedi.

Baz SOUL'un bütün alanları bilmesi varsayılmaz; fakat araştırılacak soruyu ve uygun yardım/değerlendirme yolunu bulma kapasitesi de hazır sayılmaz. Alan yetkinliği yalnız keşiften sonra edinilen sonuç değil, keşfi mümkün kılan başlangıç katkısı olabilir. Kullanıcı gizli teknik keşif işçisi yapılmaz; meşru amaç/tercih soruları ise otomatik başarısızlık değildir. T11'in bitirebilme, kullanım-bağlı kanıt ve yeniden açma sınırları korunur.

DQ01 çalışma hipotezidir; yeni T16 veya canlı deney değildir. STATE/INDEX/SY01 ve kaynak kullanıcı mesajları tam; S008/S009, T10/T11/T14 ve RPD assessment ilgili derinlikte seçici okundu. RPD'nin özgün ekleri yeniden edinilmedi; assessment kaynak yerine geçirilmedi. NASA resmî HTML §4.1/§5.4 dar dış dayanak olarak kullanıldı; el kitabı yöntemi, mimari veya yeterlik sertifikası benimsenmedi. Ayrıntılı okuma ve iddia sınırları DQ01 §10'dadır.

## DQ02 — Yöntem seçimi, uygulanabilir inceleme ve ortak körlük

[DQ02](continuations/DQ02-DISCOVERY-METHOD-SELECTION-AND-COMMON-BLIND-SPOTS.md) DQ01'in sonraki sorusunu kavramsal olarak ilerletir. Henüz soru açan keşifle belirgin rakipleri ayıran inceleme farklı olabilir; birbiri arasında dönüş vardır. Yöntem, hangi belirsizliği/ilişki alanını açabileceği, hangi bulgunun hangi kararı değiştireceği ve gerçek aktör-bilgi-ortam-yetki koşullarıyla birlikte değerlendirilir. Yeterli kaynak ve yöntem ayrı ayrı var diye uygulanabilir ortak inceleme oluşmaz.

Foundation Formation F2 ile Selection/Dynamics I1–I4 doğrudan; Work Management METHOD/U10, gstack eval sentezi ve Hermes Note30 seçici yeniden kullanıldı. gstack structural floor testi kendi pin'inde tam, Hermes skill_view wrapper'ı kendi pin'inde seçici yeniden açıldı. Structural kontrol ve yükleme/kullanım sayacı davranış yeterliği değildir. Hiçbir runtime veya model deneyi çalıştırılmadı; current upstream iddiası yoktur.

Romanın plan–metin uyumu, yalnız metnin sunduğu dayanak ve gerçek okur etkisi için farklı inceleme yolları karşılaştırıldı. Bunlar sabit üç ajan veya bir yeni kabul edilmiş yaratıcı yön değildir. Farklı model/rol tek başına hata bağımsızlığı sağlamaz; aynı modelle farklı inceleme de otomatik değersiz değildir. Huang/Wu 2024 abstract'ları bu iki aşırı hükme dar karşı baskı sağladı; yöntem üstünlüğü veya 2026 model performansı çıkarılmadı.

Gizli kusuru keşfetmek, erişilebilir amaç/kaynaklardan çıkarılamayan gizli kabul kuralını tahmin etmek değildir. Sağlam/alışılmadık çözümleri korumak, belirsizliği doğru taşımak ve gereksiz keşfi sınırlamak da değerlendirme yüküdür. Anthropic'in 2026 eval rehberi sınırlı kaynak karşılaştırmasıdır; örnekler bağımsız holdout, T16 veya canlı deney değildir.

Yöntem seçimi bir sonraki meşru inceleme ve karara bağlanabilir; bu evrensel algoritma veya otomatik yeterlik değildir. İlk uygun bakışı seçme, gerçek koşullarda gerçekleştirme, yeni bulguyu üst karara taşıma ve durmayı kalibre etme kapasitesi açıktır. DQ02 §12 tam/seçici okumaları, özgün kaynaklara dönüşü ve sınırları kaydeder. Daha geniş kaynak kullanımı tek başına SOUL/asistan keşif başarısı kanıtı sayılmaz.

## DQ03 — Üst gerekçeyi yeniden açma ve geçerli kapsamı koruma

[DQ03](continuations/DQ03-WORK-FRAME-REVISION-AUTHORITY-AND-PRESERVATION.md), doğru yerel üretimden amaç yeterliğine geçişin zedelenebileceğini kurulu soru-bankası varyantıyla inceler. İşlemi söyleyen başlık altında aynı doğru cevaplar, bağımsız yaklaşım seçimi ile başlıktan yararlanmayı ayırmayabilir. Bu bir öğrenci/öğrenme bulgusu değil, kanıt kapsamı karşıörneğidir. Eski brief'e yeni gerçek hedef eklenmez; gerçek amaç işlem pratiğiyse aynı değerlendirme çıkmaz.

Amaç, SOUL'un yorumu, yöntem, gösterge ve yetkili kabul ayrıdır. Yeni bulgu yerel uygulamayı, yöntemin koşulunu, başarı çıkarımını, yanlış ilk yorumu veya gerçekten değişen amacı etkileyebilir; karma durumlar korunur. Geriye zedelenen dayanağa, ileriye o dayanağı kullanan karar ve etkilere dönülür. Otomatik bütün projeyi yeniden açma veya yalnız değişen dosyayı düzeltme yoktur.

Foundation Revision M1/M2/M5 tam yeniden kullanıldı: destek çekme ters sonucu kabul etme değildir; bağımsız destek korunabilir; eski türevin yeni öncüle dönüşmesi geri çekilen gerekçeyi diriltebilir. Koruma ölçütü minimum kelime/sayı değildir; amaç, gerçek maliyet ve yetki önemlidir. Leantime'ın hedef/teslimat ve ölçüm/strateji geçmişi ayrımları ile OpenSpec'in özgün editing rehberindeki aynı-amaç/yeni-niyet ayrımı doğrudan karşılaştırıldı. Güncel ürün davranışı veya canlı workflow doğrulanmadı.

SOUL kendi dayanaksız iddiasını sınırlamak için onay beklememeli; fakat bunu hedefi, kabul şartını veya dış taahhüdü değiştirme yetkisi saymamalı. Yetkili takdir varsa kullanılır; maddi sınır değişimi ilgili karar sahibine taşınır. Yeni adayın onaysızlığı, eski güvencenin yeterliliğini geri getirmez; ilgili etki bekletilebilir veya yetkili durdurma yoluna taşınabilir. Kontrol dışı aktörün durduğu varsayılmaz.

Eski doğru materyal, tarihsel ölçüm ve dar kanıt korunabilirken geniş başarı hükmü yeniden açılabilir. Yeni ölçütü aynı veriye göre seçmek bağımsız doğrulama değildir; eski/yeni skorlar otomatik kıyaslanmaz. Yeni planın kabulü, gerçek uygulama ve aktörlerin o kararla çalışması ayrı. NASA §6.2/§6.5 resmî HTML dar değişiklik/uygulama kontrolü karşılaştırmasıdır; NASA süreçleri, kurulları veya standarda uyum benimsenmedi.

Bu tur sekiz kurulu karşı durum tasvir edildi; T16, gerçek öğrenci/okur/model deneyi veya yeni mekanizma çalıştırılmadı. DQ03 §12 tam/seçici okuma ve yardımcı yerel indirme sınırını kaydeder. Açık kapasite, doğru üst kararı ve etki kapsamını gerçekten keşfetmek, yetkiyi korumak ve yeterli değişikliği gerçek çalışma içinde gerçekleştirmektir.

## DQ04 — Koşullu aktarım ve seçici baz kullanımı

[DQ04](continuations/DQ04-CONDITIONAL-TRANSFER-AND-BASE-ADMISSION.md), T08/S015'in yerel uygulama, aday bilgi ve baz davranış ayrımlarını yeniden keşfetmez; geçişin dayanak yükünü açar. EXP-004'te gerçek yerel yöntem başarısı yoktur. DQ03'ün karşıörneğinden somut «başlığı kaldır» müdahalesi ile daha genel kanıt-kapsam sorusu aynı statüyle çıkarılamaz.

Romanın anlatı ipuçlarını silmek hatalı aktarım adayıdır; buna karşılık değerlendiriciye verilen ek bilginin gerçek kullanım katılımcısında bulunup bulunmadığını sorgulamak alanlar arası aday katkıdır. Yüzey benzerliği yerine yük taşıyan ilişki, amaç ve koşullar değerlendirilir. Genel bir mantıksal ayrımın gerekçesiyle belirli yöntemin hedefteki faydası farklı kanıt ister; sabit sayıda başarılı iş evrensel terfi kuralı değildir.

Foundation Persistent Adaptation D2/D3/D6 doğrudan tam kullanıldı: edinim/kalıcılık/fayda/transfer, normal destekli devam ve probe sırasında öğrenme ayrımları korundu. Kaynak defterindeki Pearl–Bareinboim transportability metninin ilgili HTML bölümleri doğrudan geri açıldı; varsayılan ortak/farklı mekanizmalar kavramsal dayanak sağladı, nedensel algoritma benimsenmedi.

gstack memory/learnings sentezi seçici, özgün `bin/gstack-learnings-search` kendi pin'inde tam okundu. Başka projeden gelen `trusted === true` kaydının içeri alınması, hedefte doğru veya yararlı olduğunun sınanması değildir. Paylaşım/değişiklik yetkisi, dersin geçerlilik kapsamı ve fiilî uygulama/kalıcılık ayrı kalır. Ortak kütüphaneye yazmak etkin kontrol değişikliği değildir; okunmuş dersin sessizce kurala dönüşmesi de değerlendirme konusudur.

Baz kapasite her yöntemi her işte çalıştırmakla eşitlenmedi. Doğru uygulama yanında doğru yerde seçme/kullanmama, yöntemlerin etkileşimi, eski geçerli davranışların korunması ve maliyet ayrı yüklerdir. Hedefte uygulanmayan veya başarısız aktarılan dersin kaynak bağlı değeri kalabilir. Sekiz kurulu karşı durum canlı/bağımsız test değildir. DQ04 §12 okuma ve erişim sınırlarını taşır; gerçek öğrenme, regresyon oranı veya transfer faydası ölçülmedi.

## Repository etkisi

SY01 başlangıç main `9ce108652e7383ef6a0390fd5272193925cf6fb5`, yayını `000786d1f7742ac87937017ac9cea18a5e329865`'tir; o tur SY01 notu, STATE ve INDEX değişti. DQ01 bu yayından başladı, `06dcefc2f192cb0cd4eb216d3f3194c2bfa48269` ile yayımlandı. DQ02 bu ref'ten başladı ve `3a9359a8bdf75203358dcda5b2fcdb2fb3eac3ef` ile yayımlandı. DQ03 bu yayından başladı ve `97627337ad622b715f3a9c562d62bb11ecda5d31` ile yayımlandı. DQ04 başlangıcı DQ03 yayın commit'idir; dar değişiklik yeni DQ04 notu ile bu STATE ve paket INDEX'tir.

Korunmuş kaynaklar/manifest, onarım kayıtları, T1–T15, SC02, SY01, DQ01–DQ03, eski CONSOLIDATION, Foundation, studies, concepts, önceki EXP ve agent-control değişmez. Kütüphane INDEX/CATALOG'daki T1–T15 sayımı ve paket girişine yönlendirme geçerlidir; SY01 ve DQ01–DQ04 bu paketin current STATE/INDEX'inden bulunur. 31 kaynak mesajı ve 126 kümülatif kaynak adresi artmaz.

Bu metin kendi gelecekteki commit'ini veya yapılmamış readback'i ilan etmez. Git ref/diff ve uzak içerik kontrolü yayın sonrasında ayrı yapılır. Teknik transfer, kavramsal yeterlilik veya bağımsız doğrulama değildir.

## Sonraki sorumluluk

DQ04'ün sınırlı kavramsal sonucu kullanıcıya döndürülür. T1–T15, SY01 ve DQ01–DQ03 yeniden yapılacak iş değildir; keşif, yöntem seçimi, üst karara dönüş ve koşullu aktarım gerçek SOUL kapasitesi olarak doğrulanmış sayılmaz.

Sonraki mantıklı dar soru: biriken dersler/yöntemler örtüştüğünde veya çatıştığında SOUL hangisini seçmeli, birleştirmeli ya da devreden çıkarmalı; sadece daha fazla kontrol ekleyerek işi hantallaştırmadan bu kararı neye dayandırmalı? T09'un eşzamanlı değişimiyle aynı test değildir; birikmiş yöntemlerin uygunluk ve birleşimi hedeflenir. Sonraki yetkili iş güncel kullanıcı yönü/kapsamıyla belirlenir; yeni deney kampanyası, gerçek roman/soru-bankası, basım/dağıtım/reklam, mimari kabulü, baz davranış değişikliği veya implementasyon yetkisi oluşmaz.
