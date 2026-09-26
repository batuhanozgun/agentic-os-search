# EXP-006 — DECISIONS

**Rol:** Kullanıcıyla netleşmiş çalışma kararlarını/kısıtları candidate fikirlerden ayırmak.  
**Güncelleme:** 27 Eylül 2026.  
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

Yeni kararların kaynak aktarımı: [U002](sources/U002-cloud-plan-and-autonomy.md). Bu kayıt kullanıcı açıklamalarını korur; örneklerdeki gerçek çalışma davranışını bağımsız doğrulamaz.

## Açık kalanlar — karar veya uygulanmış özellik sayılmaz

- Nihai DevOS mimarisi, somut rol listesi, agent sayısı ve alt ajan/takım seçimi.
- Kullanıcının önerdiği aktör → aile → rol → motivasyon hiyerarşisi; motivasyonun ayrı ajan mı yoksa rolün başarı yönü mü olduğu.
- İletişim yöntemleri, bağlam/kalıcılık/tetik düzeni, role özgü dosya formatı ve fiilî yetki sınırları.
- Memory/RAG/KG/veritabanı/iş takip ürünü seçimi; örnek projelerin bütün mimarisinin benimsenmesi.
- R1–R25 veya F1–F8'in nihai organizasyon olması; aile sayısının agent sayısı olması.
- Foundation ground'larının modül olması; mekanik M kimliklerinin servis veya ayrı ekip olması.
- Claude cloud hedefi artık açıktır; ancak gerçek cloud özelliklerinin bu gereksinimlere yeterliliği henüz gösterilmedi.

## Planın statüsü

[WORK](WORK.md)'teki P1–P6, kullanıcının istediği bütünsel planın **v1.0 çalışma düzenlemesidir**; bütün aşama ayrıntıları veya nihai mimari için verilmiş peşin onay değildir. Bu tur plan/kayıt hazırlığıyla sınırlıdır. P1 NOT STARTED; P5 teknik gerçekleştirme ve P6 fiilî sınama henüz yürütülmedi. S1 kavramsal sonucu korunur; kullanıcı kapanışı uydurulmaz.

D010'un agent-control karşılığı, kullanıcının açık kalıcılık talebi kapsamında `agent/protocols/canonical-work-preflight.md` dosyasındaki EXP-006 kısa iletişim bölümüdür. Diğer proje-work dosyaları genel kontrol kuralına yükseltilmez.
