# EXP-006 — DECISIONS

**Rol:** Kullanıcıyla netleşmiş çalışma kararlarını/kısıtları candidate fikirlerden ayırmak.  
**Güncelleme:** 27 Eylül 2026, P3 tasarım devrine hazır aday sonrası.  
**Sınır:** Buraya yazılması bir araştırma bulgusunu mimari gerçeğe veya bir gereksinimi gösterilmiş platform kabiliyetine dönüştürmez.

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

D011–D018 kaynak aktarımı [U002](sources/U002-cloud-plan-and-autonomy.md)'dedir. D019 P1 açıklamasından sonraki devam yönünün anlam kaydıdır. D020 ilk P3 kullanıcı isteğine dayanır. D021'in kullanıcı açıklaması ve kabul mesajı [P3-01 §1](work/P3-01-work-information-discussion.md#1-kullanıcı-yönü-ve-önerinin-sınırı)'de; assistant önerisi anlam özeti olarak ayrıdır. Örneklerdeki gerçek davranış bu kayıtla bağımsız doğrulanmaz.

## Açık kalanlar — karar veya uygulanmış özellik sayılmaz

- Nihai DevOS mimarisi, agent sayısı ve alt ajan/takım seçimi.
- P2-01/ACTORS'taki DR01–DR16 ilk sözleşmeler ve P3'ün DR06-G/Y, DR13-G/Y profilleri; kullanıcıca kabul edilmiş nihai kadro değildir.
- Aktör → aile → rol → motivasyon önerisi ve motivasyonu rolün başarı yönü olarak içeride tutma aday yorumu; motivasyon başına agent kararı verilmedi.
- P3 v0.5 mantıksal alanları, talep/itiraz/karar, bakım/yeniden kullanım, sürüme bağlı yayın ve kesinti sözleşmelerinin ayrıntıları. D021 bunların tümüne peşin kabul değildir.
- Expertise/izin, actual agent allocation, iletişim, bağlam/kalıcılık/tetik, fiziksel dosya biçimi, fiilî yayın/çakışma/eski-yazıcı mekanizmaları.
- Memory/RAG/KG/veritabanı/iş takip ürünü seçimi ve örneklerin bütün mimarisinin benimsenmesi.
- R1–R25/F1–F8'in nihai organizasyon olması; family/rol sayısının agent sayısı olması; Foundation ground'larının modül, mekanik M kimliklerinin servis olması.
- Cloud hedefi açıktır; P1 kaynak resmi ve P2/P3 taslakları hedef oturumun actual yeterliği değildir.

## Plan ve araştırma statüsü

[WORK](WORK.md) P1–P6 plan v1.3'ü taşır. Kullanıcının v0.4 sonrasındaki devamıyla birleşik eşzamanlılık/inceleme/kesinti senaryosu işlendi. Assistant P3'ü **DESIGN HANDOFF READY v0.5 / CANDIDATE / USER EVALUATION** düzeyinde değerlendirdi; bu değerlendirme accepted karar tablosuna eklenmedi. H1–H6 P4 için gereksinim devridir, çözüm seçimi değildir. P4–P6 başlamadı.

D021 kabulü ve yeni aday ayrıntılar ayrı kalır. Kullanıcı kapanışı, bütün P3 mimari onayı veya canlı çalışma başarısı uydurulmaz. Kısa sunum çalışma derinliğini küçültmez; her küçük ayrımda komut beklemek istenmez. D010'un önceki açık kalıcılık talebiyle eklenmiş agent-control karşılığı `agent/protocols/canonical-work-preflight.md` içindedir. Bu tur agent-control değiştirilmedi.
