# EXP-006 — WORK ve master plan

**Rol:** DevOS tasarımının üst iş haritası, bağımlılıkları ve aşama teslimatları.  
**Plan:** v1.0 çalışma planı — 27 Eylül 2026.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışabileceği düzeni ortaya koymak ve yetkilendirilen aşamalarda gerçekleştirmek/sınamak.  
**Current:** Plan ve repository sürekliliği hazırlığı tamamlandı. **P1 sırada / NOT STARTED; P2–P6 PLANNED / NOT STARTED.** Claude araştırması veya teknik kurulum bu tur başlamadı.  
**Kaynak:** [U002-A/B/C](sources/U002-cloud-plan-and-autonomy.md); kısıt/karar kaydı [DECISIONS](DECISIONS.md). Current yetki ve durma noktası [STATE](STATE.md), devir [HANDOFF](HANDOFF.md).

## 1. Önceki çalışmadan devralınan zemin

SOUL hedefi → DevOS'un SOUL üzerinde yapacağı işler → gerekli kabiliyet/sorumluluklar → AI rolleri, mekanik destek ve insan sınırı → S1 konsolidasyonu → aşağıdaki DevOS tasarım planı.

İlk altı kök iş korunur: hedefi belirlemek; gereken işi keşfetmek; yapılabilir kılmak; gerçekleştirmek; sınamak/yeniden çalışmak; zaman içinde sürdürmek. B1–B9 bu kök işlerin yerine geçen sıra veya SOUL modülleri değildir.

| ID | DevOS'un SOUL üzerinde yapacağı iş | Korunmuş ayrıştırma |
|---|---|---|
| B1 | Ortak entelektüel çalışma tabanını geliştirmek | [B1](work/B1-common-intellectual-baseline.md) |
| B2 | Bilgi kapasitesini geliştirmek | [B2](work/B2-information-capacity.md) |
| B3 | Aktör kapasitesini geliştirmek | [B3](work/B3-actors-capacity.md) |
| B4 | İş kapasitesini geliştirmek | [B4](work/B4-work-capacity.md) |
| B5 | Ortam kapasitesini geliştirmek | [B5](work/B5-environment-capacity.md) |
| B6 | Dört zeminin ilişkilerini doğru işletme kapasitesini geliştirmek | [B6](work/B6-cross-ground-integration.md) |
| B7 | İşe göre çalışma sistemi oluşturma ve genişletme kapasitesini geliştirmek | [B7](work/B7-system-formation.md) |
| B8 | Süreklilik, değişim, toparlanma ve öğrenme kapasitesini geliştirmek | [B8](work/B8-continuity-change-recovery.md) |
| B9 | Bütünü birleştirmek ve gerçek görevlerle sınamak | [B9](work/B9-integration-and-testing.md) |

B belgeleri reference/candidate decomposition'dır; ne uygulanmış kapasite ne de SOUL'un yürütmeye alınmış backlog'udur. B1'in ilk sırada yazılması, geliştirmeye onunla başlama kararı değildir.

[S1 master](work/S1-role-responsibility-consolidation.md) ve [S1-17](work/S1-17-consolidation-closure-audit.md), F1–F8 sorumluluk ailelerini ve uzmanlık sınırlarını mevcut kapsam için CLOSURE-READY / CANDIDATE düzeyine getirdi. R1–R25/M1–M9 lineage ve current aile modeli [ACTORS](ACTORS.md)'ta korunur. Nihai roller/ajan sayısı, kullanıcı kapanışı veya çalışan DevOS kabulü çıkarılmaz. Yeni somut çelişki yoksa S1 isim incelemesi tekrarlanmaz.

Korunan kritik sonuçlar: F2 gerçekleştirme sorumluluğu örtük kalmaz; her dosya yazımı F2 değildir ve reusable olması şart değildir. F3 Information Lifecycle ve Actor/Role Participation Lifecycle ayrı uzmanlıklardır; kayıt/katılım işletimi doğruluk, yetki veya gerçek etkiyi ikame etmez. Kaynak, yeterlik, tetik, devir ve güvence yükleri sonraki aşamalara açıkça taşınır. S1-16'nın tam-okuma iddiaları için S1-17 §7 qualification'ı geçerlidir.

## 2. Bu planın sınırı ve iki ana gereksinim

Bu, **DevOS'u ortaya koyma planıdır; DevOS'un SOUL'u üretme planı değildir.** İlk ve sonraki gerçek SOUL işlerini kurulacak ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant bu işleri ekibin yerine seçmez. Tasarım senaryosu gerçek backlog veya bağımsız iş keşfi başarısı sayılmaz.

**K1 — İşlevsel iletişim:** Bir rol bilgi, araştırma, değerlendirme veya kontrol isteyebilmeli; talep uygun sorumluya ulaşmalı, iş etkinleşmeli, beklenen sonuç geri dönmeli ve sonraki kararda kullanılabilmelidir. Doğrudan mesaj, ana oturum aracılığı, ortak kayıt, olay veya başka yöntemler adaydır; iki seçenekli bir ikilem veya peşinen seçilmiş mekanizma yoktur. Talebi dosyaya yazmak, tüketildiğini göstermez.

**K2 — Rutin akışın elle tetiklenmemesi:** Yetkili çalışma başlatıldıktan sonra her rol değişiminde Batu'nun “şimdi sıra sende” demesi, mesaj taşıması veya sıradaki işi başlatması gerekmemelidir. Gerektiğinde kullanıcı müdahalesi, başlangıç/yeniden başlatma, gerçek yetki ihtiyacı ve kabul mümkündür. **Sonsuza kadar kesintisiz, bütçesiz veya bütünüyle insan-bağımsız çalışma gereksinimi yoktur.**

`loopinance-claude-code/kanon` manuel tetikleme sınırını; `loopinance_v2` ise kullanıcının rutin tetikleyici olmamasını anlatan karşılaştırma örnekleridir. İkinci örneğin bütün düzeni, ECC kurulumu veya ürün backlog'u benimsenmez.

SOUL ürün dosyaları ile DevOS'un kendi planı, bilgisi, kararları, kanıtları ve devam kayıtları farklı amaçlarla yönetilir; aralarındaki kaynak/sürüm/üretim ilişkisi korunur. Bu ayrım henüz iki ayrı repository veya belirli klasör şeması kararı değildir.

## 3. Master plan — baştan görünen bütün yol

| Aşama | Esas soru ve teslimat | Dayanak / önceki bağ | Geçiş ölçütü | Durum |
|---|---|---|---|---|
| **P1 — Claude cloud gerçekliği** | K1/K2 bakımından alt ajan, ana oturum ve ajan takımı imkân/sınırlarını kaynaklı bir Environment haritasına dönüştürmek | Claude'un güncel birincil belgeleri; B5/B6/B8; iki Loopinance örneği yalnız ilgili çalışma yolu için | Belge beyanı, gözlenen davranış ve açık belirsizlik ayrılmış; iletişim/tetik/bağlam/yetki/süreklilik sınırları gösterilmiş | **NEXT / NOT STARTED** |
| **P2 — Adlandırılmış roller** | ACTORS'taki aile/sorumluluklardan açık rol isimleri ve sözleşme adayları üretmek; aile–rol–motivasyon–ajan bağını gerekçelendirmek | P1; ACTORS; S1-02/03/17; ilgili Actors ve Work Foundation'ı, seçilmiş çalışmalar | Kim ne için var, ne üretir, hangi başarı yönünü taşır, hangi yetki/uzmanlığı ister, kimle etkileşir anlaşılır; ajan sayısı etiketlerden türetilmez | PLANNED / NOT STARTED |
| **P3 — WORK–INFORMATION işleyişi** | Rollerin iş keşfi, tartışma, planlama, araştırma, üretim, bilgi bakımı ve yeniden planlama döngüsünü; doğru bilgi→doğru rol→sonraki kullanım bağını tasarlamak | P2 taslağı; Work/Information Foundation; B2/B4/B6/B8; ilgili studies | İşin doğuşu, gerekçesi, plan/gerçek yürütme ayrımı, karar kaydı, bilgi seçimi/görünürlüğü/tüketimi, durma/devralma yolları görünür | PLANNED / NOT STARTED |
| **P4 — Bütünleşik DevOS tasarımı** | P1–P3'ü birlikte karşılaştırıp alt ajan/takım veya gerekçeli başka birleşimi seçmek; roller, iletişim, sahiplik ve çalışma/ürün kayıtlarının bütünleşik düzenini tanımlamak | P1 Environment kanıtı + P2 roller + P3 iş/bilgi döngüsü; B6/B7/B9 | K1/K2 için uçtan uca yol, sınırlar ve gerekçeli seçim var; somut dosya/mekanizma gerçekleştirmesine geçilecek tasarım gözden geçirilmiş | PLANNED / NOT STARTED |
| **P5 — Dosyalar ve mekanizmalar** | Gözden geçirilmiş tasarımı Claude'un gerçekten tükettiği ajan tanımları, ortak talimatlar, bağlam/iş kayıtları ve gerekli kontrollerle gerçekleştirmek | P4; P1'de doğrulanmış dosya yükleme ve çalıştırma sözleşmeleri | Dosya varlığı değil yükleme, rol etkinleşmesi, izin ve çıktı/tüketici bağlantısı gösterilir; gereksiz özel sistem kurulmaz | PLANNED / NOT STARTED |
| **P6 — Sınama ve devretme** | Ekibin hedef/birikimi devralmasını, iş keşfini, rol arası talep/cevabı, normal otomatik ilerlemeyi ve müdahale sonrası doğru devamı sınamak | P5; B9; S1 doğrulama/aktarım ayrımları; gerçek ortamda uygun kanıt | Rutin rol geçişlerinde kullanıcı tetiklemesi gerekmiyor; bilgi/karar/sürüm bağları korunuyor; başarısız/açık durumlar görünür; devir ve yetki sınırı belirli | PLANNED / NOT STARTED |

**Bağımlılık:** P1 → P2 ↔ P3 → P4 → P5 → P6. P2/P3 yeni bir Environment ihtiyacı açarsa P1'e hedefli dönüş yapılır. P6 kusuru ilgili P aşamasına döndürür. Geri dönüş bütün planı baştan başlatma gerekçesi değildir.

Bu sıralama çalışma planıdır, katı waterfall veya kabul edilmiş nihai mimari değildir. Environment gerçeği önce öğrenilir; yürütme topolojisi gerekli rol/iletişim yükleri görülmeden sırf ürün özelliği var diye dondurulmaz. Planın varlığı P1–P6'nın bu tur yürütüldüğü veya bütün gelecek uygulama/erişim kararlarının yetkilendirildiği anlamına gelmez. Tasarım değerlendirme kapıları, kurulacak DevOS'un her iç adımında Batu onayı isteyeceği anlamına gelmez.

## 4. P1'in hazır araştırma çerçevesi — henüz yürütülmedi

**Soru:** Claude Code cloud, K1/K2'yi hangi gerçek çalışma yollarıyla karşılayabilir; nerede destek, ek düzen veya insan müdahalesi gerekir?

Önce Anthropic'in güncel Claude Code cloud, subagents, agent teams ve ilgili context/memory/settings/hooks belgeleri okunur. Exact URL, erişim tarihi, sürüm/scope ve karar taşıyan bölüm kaydedilir. Yerel terminal özelliği otomatik cloud desteği sayılmaz. Önceki chat cevaplarındaki destek/mesajlaşma hükümleri bu planın doğrulanmış Environment bulgusu değildir; P1 bunları birincil kaynak üzerinden yeniden kurar.

İnceleme eksenleri:
- Talebin iletilmesi, doğru aktörün etkinleşmesi, bağımlı bekleme, yanıtın dönmesi ve işe tüketilmesi; doğrudan veya aracılı iletişimin koşulları.
- Ana oturum/alt ajan/takımın bağlamları, talimat ve dosya yükleme biçimleri; ortak ve role özgü bilgi, çıktıların sonraki girdilere dönüşmesi.
- Araç/izin sınırları, repository erişimi, yazma sahipliği, eşzamanlı değişiklik ve sürüm uyuşmazlıkları.
- Normal akışta sıradaki işin/rolün tetiklenmesi; durma, hata, kullanım sınırı, oturum sonu ve kullanıcı müdahalesinden sonra devralma. Kullanıcıdan tamamen bağımsız yeni oturum açmak başarı şartı değildir.
- Platformun yerleşik sağladığı, yalnız talimatla beklenen, ek mekanizma gerektiren ve fiilen henüz sınanmayan kabiliyetlerin ayrımı.

**Teslimat:** K1/K2 ile ilişkili seçenekler, imkân/sınırlar ve açık sorular; her yük taşıyan sonuç için kaynak veya uygun gözlem. Doküman okuması canlı test değildir. Fiilî cloud erişimi/probe ayrı yetki ve uygun ortam gerektiriyorsa açık kalır; yapılmış gibi yazılmaz.

**Dönüş:** P1 yeterli Environment resmi sağladığında kısa sonucu kullanıcıya döndür; P2/P3 için etkileri göster. Bu aşamada SOUL backlog'u, nihai rol listesi veya kurulum üretme. Araştırma ayrıntısı açıldığında mevcut `work/` altında P1'e bağlı tutulur; yeni EXP/deneme veya kopuk araştırma hattı açılmaz.

## 5. Foundation ve studies kullanım yolu

Foundation hazır reçete değildir: araştırma, assistant'ın bakışını genişleterek atlanabilecek iş/bilgi/aktör/ortam ayrımlarını ve soruları ortaya çıkarmalıdır. Studies, bu sorular için gerçek uygulama örnekleri, karşı örnekler ve sınırlar sağlar. Her aşamada ilgili Foundation metniyle düşünülür; sonra o çerçeveyle seçilmiş studies okunur. İsimleri dosyaya eklemek bu kullanımın yerine geçmez.

Başlangıç rotası: [Foundation STATE](../../research/soul-foundations/STATE.md) → [REUSE](../../research/soul-foundations/08_foundation-sufficiency-reuse-review/REUSE.md). Somut soru için:
- [Work](../../research/soul-foundations/03_ground-deepening/grounds/work/INDEX.md): gerekli iş, plan, yürütme, bağımlılık, kapanış ve yeniden açma.
- [Information](../../research/soul-foundations/03_ground-deepening/grounds/information/INDEX.md): kaynak/statü/sürüm, bakım, seçim, görünürlük ve kullanım.
- [Actors](../../research/soul-foundations/03_ground-deepening/grounds/actors/INDEX.md), [Environment](../../research/soul-foundations/03_ground-deepening/grounds/environment/INDEX.md) ve [Composition](../../research/soul-foundations/05_relation-control-composition/INDEX.md): rol/yetki, gerçek koşullar ve aralarındaki bağlar gerektiğinde.

[Studies CATALOG](../../research/studies/CATALOG.md) → yalnız ilgili META/STATE/INDEX → gerçek bulgu/kaynak. İlk reuse adayları: Work Management/Project Control ve RPD (iş keşfi/akış); Context–Memory–Harness ve Hermes (bilgi/bağlam/süreklilik); Superpowers, gstack ve ECC (rol, devir, kontrol, gerçek tüketici). Hepsinin bütün içeriği her tur okunmaz; kullanılan kısmın gerçek okuma/sürüm kapsamı izlenir. Kaynakta kalan önemli belirsizlik derinleşmeyle çözülür; mevcut özet yeterli diye varsayılmaz.

[Keel kaydı](../../research/soul-context/repos/keel/README.md) ile [OS Architect kaydı](../../research/soul-context/repos/os-architect/README.md) tarihsel karşılaştırma kaynaklarıdır. [Loopinance kanon](https://github.com/batuhanozgun/loopinance-claude-code/tree/main/kanon) ve [Loopinance v2](https://github.com/batuhanozgun/loopinance_v2) yalnız ilgili tetik/iletişim/kayıt yolları için incelenir. Kullanıcı bildirimi, dosyadaki talimat ve çalışan mekanizma üç ayrı kanıt statüsüdür. Örneklerin backlog'u, insan kapıları veya ECC seçimi DevOS'a taşınmaz; bu depolara yazılmaz.

## 6. Açık tasarım kararları

Aktör → aile → rol → motivasyon hiyerarşisi ve motivasyon başına ajan kullanımı kullanıcı önerisidir; P2'de sınanacak. Alt ajan/takım seçimi, gerçek agent sayısı, rol dosyalarının biçimi/konumu, mesajlaşma/ortak kayıt/olay düzeni ve depolama/iş takip mekanizmaları açık. Claude Code cloud hedef Environment'ı ise kullanıcı tarafından belirlenmiştir; hedefin verilmiş olması yeterliliğin kanıtı değildir.

## 7. Planı yaşayan ama yönü sabit tutma

Her tur başında current işi bu haritadaki P kimliğine ve teslimata bağla. Tur sonunda o aşamanın sonucu, kullanılan kaynak/sürüm, açık soru, sonraki bounded adım ve üst işe dönüş kaydedilir. Bütün yön her tur yeniden icat edilmez.

Maddi değişiklikte: neden, kaynak/kullanıcı yönü, etkilenen aşama ve geri dönüş bu WORK planına; current durum STATE'e; devralma HANDOFF'a; gerçek karar DECISIONS'a; rol anlamı değiştiyse ACTORS'a yazılır. Ayrıntı mevcut `work/` içinde aşamayla bağlı kalır. Yeni dosya ancak mevcut yüzey yetmiyorsa açılır; boş aşama dosyaları oluşturulmaz.

**27 Eylül 2026 değişim kaydı:** S1-17 ve önceki analizler korundu. Sonraki yönü yalnız tur sonlarından türetmek yerine P1–P6 haritası burada kuruldu. Cloud hedefi ve K1/K2 kaydedildi; sınırsız gözetimsizlik kapsam dışı bırakıldı. Plan hazırlığı tamamlandı; P1–P6 henüz yürütülmedi. Sıradaki kullanıcı devamında P1'den başlanır, bugün burada durulur.
