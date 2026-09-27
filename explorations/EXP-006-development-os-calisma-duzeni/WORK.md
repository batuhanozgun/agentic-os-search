# EXP-006 — WORK ve master plan

**Rol:** DevOS tasarımının üst iş haritası, bağımlılıkları ve aşama teslimatları.  
**Plan:** v1.3 — 27 Eylül 2026; P1–P6 hedef ve sırası korunuyor. P3 tartışma ayrıntısı v0.2'ye ilerledi.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışabileceği düzeni ortaya koymak ve yetkilendirilen aşamalarda gerçekleştirmek/sınamak.  
**Current:** **P3 DISCUSSION BASELINE v0.2 / CANDIDATE / USER DISCUSSION. P3 tamamlanmadı.** P2 ilk sözleşme tabanı korunur. P1 kaynak incelemesi tamam, runtime sınanmadı. P4–P6 başlamadı; teknik seçim P4'tedir.  
**Kaynak:** [U002-A/B/C](sources/U002-cloud-plan-and-autonomy.md); kısıtlar [DECISIONS](DECISIONS.md), P3 tartışma yönü [P3-01](work/P3-01-work-information-discussion.md). Current yetki [STATE](STATE.md), devir [HANDOFF](HANDOFF.md).

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

[S1 master](work/S1-role-responsibility-consolidation.md) ve [S1-17](work/S1-17-consolidation-closure-audit.md), F1–F8 sorumluluk ailelerini ve uzmanlık sınırlarını mevcut kapsam için CLOSURE-READY / CANDIDATE düzeyine getirdi. R1–R25/M1–M9 lineage ve ilk P2 aile/rol modeli [ACTORS](ACTORS.md)'ta korunur. Nihai roller/ajan sayısı, kullanıcı kapanışı veya çalışan DevOS kabulü çıkarılmaz. Yeni somut çelişki yoksa S1 isim incelemesi tekrarlanmaz.

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
| **P1 — Claude cloud gerçekliği** | K1/K2 bakımından alt ajan, ana oturum ve ajan takımı imkân/sınırlarını kaynaklı Environment haritasına dönüştürmek | Güncel birincil Claude belgeleri; B5/B6/B8; Loopinance örneklerinin ilgili yolları | Belge, gözlenen davranış ve açık belirsizlik ayrılmış; iletişim/tetik/bağlam/yetki/süreklilik sınırları gösterilmiş | **KAYNAK İNCELEMESİ TAMAM / RUNTIME SINANMADI**; [P1-01](work/P1-01-claude-cloud-environment-map.md) |
| **P2 — Adlandırılmış roller** | Aile/sorumluluklardan açık rol isimleri ve sözleşme adayları; aile–rol–motivasyon–ajan bağının gerekçesi | P1; ACTORS; S1-02/03/17; Actors/Work Foundation ve seçilmiş çalışmalar | Kim ne için var, ne üretir, hangi başarı yönü/yetki/uzmanlıkla ve kimle etkileşir anlaşılır; sayıdan agent çıkarılmaz | **İLK TASLAK HAZIR / CANDIDATE**; [P2-01](work/P2-01-named-role-contracts.md), isimler ACTORS'ta; P3'ün G/Y hedef-profili düzeltmesi değerlendirmede |
| **P3 — WORK–INFORMATION işleyişi** | İş keşfi, tartışma, planlama, araştırma, üretim, bilgi bakımı ve yeniden planlama döngüsü; doğru bilgi→doğru rol→sonraki kullanım | P2 taslağı; Work/Information Foundation; B2/B4/B6/B8; ilgili studies | İşin doğuşu/gerekçesi, plan/gerçek ayrımı, karar kaydı, bilgi seçimi/görünürlüğü/tüketimi, durma/devralma görünür | **DISCUSSION BASELINE v0.2 / CANDIDATE / TAMAMLANMADI**; [P3-01](work/P3-01-work-information-discussion.md) iş–yapı/koordinasyon/güvence/bilgi akışı bazı |
| **P4 — Bütünleşik DevOS tasarımı** | P1–P3 ile alt ajan/takım veya gerekçeli birleşimi seçmek; roller, iletişim, sahiplik, çalışma/ürün kayıtlarını bütünleştirmek | P1 kanıtı + P2 roller + P3 döngüsü; B6/B7/B9 | K1/K2 için uçtan uca yol ve sınırlar var; yük taşıyan Environment açıkları seçilen yol için doğrulanmış; tasarım gözden geçirilmiş | PLANNED / NOT STARTED; seçimin burada olması kullanıcıyla teyit edildi |
| **P5 — Dosyalar ve mekanizmalar** | Gözden geçirilmiş tasarımı Claude'un gerçekten tükettiği ajan tanımları, ortak talimatlar, bağlam/iş kayıtları ve kontrollerle gerçekleştirmek | P4; P1'de kaynaklanan ve gerektiğinde fiilen doğrulanan sözleşmeler | Dosya varlığı değil yükleme, rol etkinleşmesi, izin ve çıktı/tüketici bağlantısı gösterilir; gereksiz özel sistem kurulmaz | PLANNED / NOT STARTED |
| **P6 — Sınama ve devretme** | Ekibin hedef/birikimi devralması, iş keşfi, talep/cevap, normal otomatik ilerleme ve müdahale sonrası doğru devamı | P5; B9; S1 güvence/aktarım ayrımları; gerçek ortam | Rutin rol geçişlerinde kullanıcı tetiklemesi gerekmiyor; bilgi/karar/sürüm bağları korunuyor; başarısız/açık durumlar ve devir sınırı görünür | PLANNED / NOT STARTED |

**Bağımlılık:** P1 → P2 ↔ P3 → P4 → P5 → P6. Yeni yük taşıyan Environment ihtiyacı P1'e hedefli dönüş açar; P6 kusuru ilgili P aşamasına döndürür. Geri dönüş bütün planı baştan başlatma gerekçesi değildir.

Bu sıralama çalışma planıdır, katı waterfall veya kabul edilmiş nihai mimari değildir. Environment önce öğrenilir; yürütme topolojisi gerekli rol/iletişim yükleri görülmeden dondurulmaz. Planın varlığı gelecek bütün uygulama/erişim kararlarının yetkilendirildiği anlamına gelmez. Tasarım değerlendirme kapıları, kurulacak DevOS'un her iç adımında Batu onayı isteyeceği anlamına gelmez.

## 4. P1 sonucu ve sonraki tasarıma devir

P1'in yetkili sorusu: Claude Code cloud, K1/K2'yi hangi gerçek çalışma yollarıyla karşılayabilir; nerede destek, ek düzen veya insan müdahalesi gerekir?

**[P1-01 kaynak haritası](work/P1-01-claude-cloud-environment-map.md)** resmî belgeler ve sabit Loopinance kaynaklarıyla hazırlandı. Kaynak incelemesi tamam; canlı cloud yeterliği, mesaj teslimi, izin veya yeniden giriş testi yapılmadı. Eski sohbet feature beyanları sonuç kabul edilmedi; birincil kaynaklardan yeniden kuruldu.

P1'in P2/P3'e katkısı:
- İletişim yalnız takımlara özgü değil; alt ajan mesajlaşması da uygun araç/kimlikle kaynaklarda var. Topoloji hâlâ açık.
- Tanım dosyası, çalıştırma, yeterli bağlam ve çıktının kullanımı ayrı bağlar; aynı tanımın farklı çalışma kiplerinde aynı yüklenmesi garanti değil.
- Rutin devam imkânı, doğru Work keşfi veya gerçek kalite hükmü değildir. Otomatik takım plan onayı bağımsız değerlendirme sayılmaz.
- Kalıcı DevOS Work/Information düzeni runtime hafızasına sessizce bırakılamaz.
- Cloud plugin desteğinde resmî doküman çelişkisi ve gerçek hedef sürüm/erişim belirsizlikleri açık tutuldu.

**Q01–Q06:** Etkin cloud kip/araçları; talep→kullanım zinciri; plugin çelişkisi; kalıcı state; kaynak/yazma erişimi; durma/güvence. Ayrıntı ve sonraki probe taslakları P1-01 §5'tedir. Yalnız yük taşıdığı tercih için ilgili açık doğrulanır; plugin kullanımı seçilmeden plugin'i çözmek için ayrı kampanya açılmaz.

P1 kaynak sonucu kullanıcıya sunuldu. P2, kullanıcının P4 seçim sırasını anlayıp devam istemesiyle açıldı. P1'e dönüş yeni somut soru/teknik bağımlılığa bağlıdır; belgesel tamamlanma fiilî yeterlik gibi sunulmaz.

### 4A. P2 ilk rol taslağı ve P3'e devir

[ACTORS](ACTORS.md) DR01–DR16 ilk aday isim/lineage registry'sini; [P2-01](work/P2-01-named-role-contracts.md) ilk sözleşmeleri taşır. Her rol için motivasyon/başarı yönü, girdi/yeterlik, tetik, teslimat/tüketici ve yetki sınırı yazıldı. Bu 16 ayrı agent veya nihai kadro değildir.

Motivasyon rolün başarı yönü olarak sözleşmenin içinde tutulur; ayrı agent'a otomatik eşlenmez. Alan uzmanlıkları ve aynı actor'da birleşme koşulları korunur. R1–R25 primary lineage birer kez eşlenir; bu mekanik kontrol actual competence veya semantik doğruluk kanıtı değildir. Foundation Actors/Work, Superpowers S03, Work-management U10 ve tarihsel rol-sözleşmesi kayıtları bu ayrımları besledi; ayrıntılı kapsam P2-01 §7'dedir.

P3'ün ilk kapsamı hedef/birikimin devri → gerekli iş/bilgi açıklarının keşfi ve sorgulanması → rol talebi/yanıtı → gerekçeli plan/admission idi. Kullanıcı bunun içinde iş koordinasyonu ile yapı koordinasyonunu ayırmayı önerdi; current ayrıntı aşağıdadır. Hazır SOUL teknik görevi seçilmeyecek.

P3 farklı expertise, yetki veya sahiplik gereği gösterirse P2 sözleşmeleri hedefli güncellenir. P3'ün henüz kabul edilmemiş düzeltmesi P2'ye nihai kadro gibi geçirilmez; current tartışma farkı açık bağla korunur.

### 4B. P3 current öneri — iki hedef alanı, bütünleşik işleyiş

[P3-01 v0.2](work/P3-01-work-information-discussion.md) yaşayan iş ağı, ihtiyaca göre işbirliği ve kalıcı bilgi/role özgü bağlam omurgasını korur. Kullanıcının önerisiyle iki hedef alanını ayırır: **G — SOUL geliştirme** ve **Y — DevOS işleyişi**. İkisi de DevOS içindedir; Y de Work/Reasoning taşır, yalnız teknik altyapı veya Foundation ENVIRONMENT ground'u değildir.

DR01–DR16'nın tümü bu iki hedefe yerleştirildi. **DR06-G/Y** geliştirme katkılarının öncelik/bağımlılık koordinasyonu ile ekibin gerçek çalıştırma/kapasite/devir koordinasyonunu; **DR13-G/Y** ürün/iş doğruluğu ile gereken çalışma koşullarının güvencesini ayıran aday profillerdir. Fiziksel ajan sayısı veya P4 seçimi değildir. ACTORS/P2 ilk taban olarak bu tur korunur; önerilen farkın tek ayrıntı evi P3-01'dir.

Karşılıklı yürütme isteği, rutin danışma/ayrı Work sınırı, alan kararı ve engel, kaynak/karar/ürün sürümü, kayıt bakımının sahibi, tüketicinin bağlamı ve kesinti sonrası dönüş birlikte taslaklaştırıldı. G olmayan kapasiteyi varsaymaz; Y kısıtı çözmek için ürün kriterini sessizce değiştirmez. İş içindeki her mesaj iki koordinatörden onay almak zorunda değildir. İki denetim her küçük işte iki zorunlu komite demek değildir.

Dayanaklar: Work/Actors Foundation; Information integration I1–I5; RPD; Work-management; Superpowers S03. Bu revizyonda Gas Town META ve FINDINGS'in 1–280 aralığı, iş nesnesi/dispatch denemesi, kapasite/liveness ve entegrasyon farkını somutlaştırmak için ayrıca okundu. Kaynak kullanımının gerçek kapsamı P3-01 §9'dadır. Hiçbiri platform benimseme veya canlı DevOS başarısı sayılmaz.

**Current dönüş:** Bu bütünlüklü taslağı kısa sun, kullanıcı değerlendirmesini aynı bazda işle. Sonraki anlamlı P3 parçası bağlam hazırlanması, uzman görüş ayrılığı, kararın kaydı, yeni bilgiyle yeniden açma ve oturum devrinin birlikte somutlaştırılmasıdır. Küçük adımların her birinde onay/komut beklemek veya aynı ayrımı yeniden açıklamak ilerleme değildir. P3 tamamlanmadı; P4'e geçiş yok.

## 5. Foundation ve studies kullanım yolu

Foundation hazır reçete değildir: assistant'ın bakışını genişleterek atlanabilecek iş/bilgi/aktör/ortam ayrımlarını ve soruları ortaya çıkarmalıdır. Studies gerçek uygulama örnekleri, karşı örnekler ve sınırlar sağlar. İlgili Foundation metniyle düşünülür; sonra o çerçeveyle studies okunur. Kaynak isimlerini dosyaya eklemek yeterli değildir.

Başlangıç: [Foundation STATE](../../research/soul-foundations/STATE.md) → [REUSE](../../research/soul-foundations/08_foundation-sufficiency-reuse-review/REUSE.md). Somut soru için:
- [Work](../../research/soul-foundations/03_ground-deepening/grounds/work/INDEX.md): gerekli iş, plan, yürütme, bağımlılık, kapanış ve yeniden açma.
- [Information](../../research/soul-foundations/03_ground-deepening/grounds/information/INDEX.md): kaynak/statü/sürüm, bakım, seçim, görünürlük ve kullanım.
- [Actors](../../research/soul-foundations/03_ground-deepening/grounds/actors/INDEX.md), [Environment](../../research/soul-foundations/03_ground-deepening/grounds/environment/INDEX.md) ve [Composition](../../research/soul-foundations/05_relation-control-composition/INDEX.md): rol/yetki, gerçek koşullar ve bağlar.

[Studies CATALOG](../../research/studies/CATALOG.md) → ilgili META/STATE/INDEX → gerçek bulgu/kaynak. Adaylar: Work Management/Project Control ve RPD (iş keşfi/akış); Context–Memory–Harness ve Hermes (bilgi/bağlam/süreklilik); Superpowers, gstack ve ECC (rol/devir/kontrol/tüketici); Gas Town (iş ve çalıştırma/kapasite/liveness sınırı). Bütün korpus her tur yüklenmez; gerçek okuma/sürüm kapsamı korunur. Karar-kritik ayrım özetle kapanmıyorsa kaynağa inilir.

[Keel](../../research/soul-context/repos/keel/README.md), [OS Architect](../../research/soul-context/repos/os-architect/README.md) tarihsel örneklerdir. [Kanon](https://github.com/batuhanozgun/loopinance-claude-code/tree/main/kanon) ve [v2](https://github.com/batuhanozgun/loopinance_v2) yalnız ilgili tetik/iletişim/kayıt yollarıyla karşılaştırılır; P1'in sabit kaynakları P1-01'de. Kullanıcı bildirimi, dosya talimatı ve çalışan mekanizma ayrı kanıt statüleridir. Örneklerin backlog'u, insan kapıları veya ECC seçimi DevOS'a taşınmaz; bu depolara yazılmaz.

## 6. Açık tasarım kararları

P2-01'in aday yorumu, familyayı sınıflandırma, rolü sözleşme, motivasyonu onun başarı yönü ve gerçek agent binding'ini ayrı görevlendirme olarak tutar. Kullanıcı bu yorumu henüz kabul etmiş değildir; motivasyon başına agent seçilmedi.

DR01–DR16 ilk tabandır. P3'ün G/Y hedef ayrımı ve DR06/13 profilleri değerlendirme adayıdır; kullanıcı kararı veya otomatik yeni rol/ajan sayısı değildir. Expertise, yetki, context/kalıcılık, dosya biçimi, iletişim ve actual allocation P2↔P3 ve sonra P4–P6 ile gerekçelenecektir. Claude hedefi kullanıcı kısıtıdır; P1/P2/P3 çıktıları actual kurulumun yeterliğini kanıtlamaz.

## 7. Yaşayan plan ve değişim kaydı

Her tur current işi P kimliğine/teslimata bağlar. Sonuç, kullanılan kaynak/sürüm, açık soru, sonraki bounded adım ve üst işe dönüş kaydedilir. Bütün yön her tur yeniden icat edilmez. Kısa sunum gerekli çalışma derinliğini veya bütünlüğünü azaltmaz.

Maddi değişiklikte neden, kaynak/kullanıcı yönü, etkilenen aşama ve geri dönüş bu WORK planına; current STATE'e; devir HANDOFF'a; gerçek karar DECISIONS'a; yerleşen rol anlamı ACTORS ve ilgili sözleşmeye yazılır. Aday düzeltme, hangi ilk sözleşmeyi koşullandırdığı açık olarak P3'te tutulabilir; kabul uydurulmaz. Yeni dosya mevcut yüzey yetmediğinde açılır; boş aşama dosyaları oluşturulmaz.

- **27 Eylül 2026 / v1.0:** S1 ve önceki analizler korundu; P1–P6 master harita kuruldu. Cloud, K1/K2 ve sınırsız gözetimsizlik dışı sınır kaydedildi. Yalnız plan hazırlığı tamamlandı.
- **27 Eylül 2026 / v1.1:** Kullanıcı devamıyla P1 kaynak/Loopinance incelemesi yapıldı; runtime sınanmadı, Q01–Q06 devredildi.
- **27 Eylül 2026 / v1.2:** Kullanıcının P4 sırasını anlayıp devam istemesiyle P2 ilk adlandırılmış sözleşmeler ACTORS'a bağlandı. SOUL görevi, topoloji veya actual ajan dosyası üretilmedi.
- **27 Eylül 2026 / v1.3:** P3 araştırmaya dayalı başlangıç yapısı ve birlikte değerlendirme statüsüyle açıldı; planın sırası değişmedi.
- **27 Eylül 2026 / P3 v0.2 ayrıntı revizyonu:** İş–yapı, iki koordinasyon/güvence, tüm rol yerleşimi, karşılıklı istek ve bilgi sahipliği tek taslakta birleştirildi. Master aşama haritası v1.3 kaldı; P3 açık. Kısa cevap isteği küçük ilerleme/onay turlarına çevrilmez. Registry/ilk P2 sözleşmeleri korunur; önerilen fark P3-01'de görünür. Runtime veya kullanıcı tasarım kabulü yoktur.
