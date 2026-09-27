# EXP-006 — WORK ve master plan

**Rol:** DevOS tasarımının üst iş haritası, bağımlılıkları ve aşama teslimatları.  
**Plan:** v1.3 — 27 Eylül 2026; P1–P6 hedef ve sırası korunuyor. P3 ayrıntısı v0.4 konsolide çalışma taslağına ilerledi.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışabileceği düzeni ortaya koymak ve yetkilendirilen aşamalarda gerçekleştirmek/sınamak.  
**Current:** **P3 CONSOLIDATED WORKING DRAFT v0.4 / DISCUSSION.** İçerik–çalışma alanı sorumluluk ayrımı D021 ile kabul; P3'ün bütün ayrıntıları kabul edilmiş veya tamamlanmış değildir. P2 ilk sözleşme tabanı ve P1 kaynak sonucu/runtime açıkları korunur. P4–P6 başlamadı.  
**Kaynak:** [U002](sources/U002-cloud-plan-and-autonomy.md); kısıtlar [DECISIONS](DECISIONS.md), son netleştirme [P3-01 §1](work/P3-01-work-information-discussion.md#1-kullanıcı-yönü-ve-önerinin-sınırı). Current yetki STATE, devir HANDOFF'tadır.

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

## 2. Bu planın sınırı ve ana gereksinimler

Bu, **DevOS'u ortaya koyma planıdır; DevOS'un SOUL'u üretme planı değildir.** İlk ve sonraki gerçek SOUL işlerini kurulacak ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant bu işleri ekibin yerine seçmez. Tasarım senaryosu gerçek backlog veya bağımsız iş keşfi başarısı sayılmaz.

**K1 — İşlevsel iletişim:** Bir rol bilgi, araştırma, değerlendirme veya kontrol isteyebilmeli; talep uygun sorumluya ulaşmalı, iş etkinleşmeli, beklenen sonuç geri dönmeli ve sonraki kararda kullanılabilmelidir. Doğrudan mesaj, ana oturum aracılığı, ortak kayıt, olay veya başka yöntemler adaydır; iki seçenekli bir ikilem veya peşinen seçilmiş mekanizma yoktur. Talebi dosyaya yazmak, tüketildiğini göstermez.

**K2 — Rutin akışın elle tetiklenmemesi:** Yetkili çalışma başlatıldıktan sonra her rol değişiminde Batu'nun “şimdi sıra sende” demesi, mesaj taşıması veya sıradaki işi başlatması gerekmemelidir. Gerektiğinde kullanıcı müdahalesi, başlangıç/yeniden başlatma, gerçek yetki ihtiyacı ve kabul mümkündür. **Sonsuza kadar kesintisiz, bütçesiz veya bütünüyle insan-bağımsız çalışma gereksinimi yoktur.**

**D021 — Çalışma alanı düzeni:** Dosyaların/kayıtların yeri, güncelliği, tek yetkili kaynağı, bulunabilirliği, kaynak/sürüm ilişkileri, kontrollü bakımı, devri ve tekrar kullanımı asli işletim sorumluluğudur. İçerik sahibi ne söylendiği ve gerekçesini taşır; düzen tarafı onu korunabilir/kullanılabilir tutar, ürün kararının yerine geçmez. Bu yalnız görsel klasör temizliği değildir.

`loopinance-claude-code/kanon` manuel tetikleme sınırını; `loopinance_v2` ise kullanıcının rutin tetikleyici olmamasını anlatan karşılaştırma örnekleridir. İkinci örneğin bütün düzeni, ECC kurulumu veya ürün backlog'u benimsenmez.

SOUL ürün dosyaları ile DevOS'un kendi planı, bilgisi, kararları, kanıtları ve devam kayıtları farklı amaçlarla yönetilir; aralarındaki kaynak/sürüm/üretim ilişkisi korunur. Bu ayrım henüz iki ayrı repository veya belirli klasör şeması kararı değildir.

## 3. Master plan — baştan görünen bütün yol

| Aşama | Esas soru ve teslimat | Dayanak / önceki bağ | Geçiş ölçütü | Durum |
|---|---|---|---|---|
| **P1 — Claude cloud gerçekliği** | K1/K2 bakımından alt ajan, ana oturum ve ajan takımı imkân/sınırlarını kaynaklı Environment haritasına dönüştürmek | Güncel birincil Claude belgeleri; B5/B6/B8; Loopinance örneklerinin ilgili yolları | Belge, gözlenen davranış ve açık belirsizlik ayrılmış; iletişim/tetik/bağlam/yetki/süreklilik sınırları gösterilmiş | **KAYNAK İNCELEMESİ TAMAM / RUNTIME SINANMADI**; [P1-01](work/P1-01-claude-cloud-environment-map.md) |
| **P2 — Adlandırılmış roller** | Aile/sorumluluklardan açık rol isimleri ve sözleşme adayları; aile–rol–motivasyon–ajan bağının gerekçesi | P1; ACTORS; S1-02/03/17; Actors/Work Foundation ve seçilmiş çalışmalar | Kim ne için var, ne üretir, hangi başarı yönü/yetki/uzmanlıkla ve kimle etkileşir anlaşılır; sayıdan agent çıkarılmaz | **İLK TASLAK / CANDIDATE**; [P2-01](work/P2-01-named-role-contracts.md); P3 profilleri ve D021 kapsamıyla birlikte okunur |
| **P3 — WORK–INFORMATION işleyişi** | İş keşfi, tartışma, planlama, araştırma, üretim, bilgi/çalışma alanı bakımı, tekrar kullanım ve yeniden planlama döngüsü | P2; Work/Information Foundation; B2/B4/B6/B8; ilgili studies | İşin doğuşu/gerekçesi, plan/gerçek ayrımı, karar/kayıt sahipliği, bilgi kullanımı, çalışma alanı düzeni ve devir görünür | **KONSOLİDE TASLAK v0.4 / DISCUSSION / KAPANMADI**; [P3-01](work/P3-01-work-information-discussion.md) |
| **P4 — Bütünleşik DevOS tasarımı** | P1–P3 ile alt ajan/takım veya gerekçeli birleşimi seçmek; roller, iletişim, sahiplik, çalışma/ürün kayıtlarını bütünleştirmek | P1 kanıtı + P2 roller + P3 döngüsü; B6/B7/B9 | K1/K2 için uçtan uca yol ve sınırlar var; yük taşıyan Environment açıkları seçilen yol için doğrulanmış; tasarım gözden geçirilmiş | PLANNED / NOT STARTED; seçimin burada olması kullanıcıyla teyit edildi |
| **P5 — Dosyalar ve mekanizmalar** | Gözden geçirilmiş tasarımı Claude'un gerçekten tükettiği ajan tanımları, ortak talimatlar, bağlam/iş kayıtları ve kontrollerle gerçekleştirmek | P4; P1'de kaynaklanan ve gerektiğinde fiilen doğrulanan sözleşmeler | Dosya varlığı değil yükleme, rol etkinleşmesi, izin ve çıktı/tüketici bağlantısı gösterilir; gereksiz özel sistem kurulmaz | PLANNED / NOT STARTED |
| **P6 — Sınama ve devretme** | Ekibin hedef/birikimi devralması, iş keşfi, talep/cevap, normal otomatik ilerleme ve müdahale sonrası doğru devamı | P5; B9; S1 güvence/aktarım ayrımları; gerçek ortam | Rutin rol geçişlerinde kullanıcı tetiklemesi gerekmiyor; bilgi/karar/sürüm bağları korunuyor; başarısız/açık durumlar ve devir sınırı görünür | PLANNED / NOT STARTED |

**Bağımlılık:** P1 → P2 ↔ P3 → P4 → P5 → P6. Yeni yük taşıyan Environment ihtiyacı P1'e hedefli dönüş açar; P6 kusuru ilgili P aşamasına döndürür. Geri dönüş bütün planı baştan başlatma gerekçesi değildir.

Bu sıralama çalışma planıdır, katı waterfall veya kabul edilmiş nihai mimari değildir. Environment önce öğrenilir; yürütme topolojisi gerekli rol/iletişim yükleri görülmeden dondurulmaz. Planın varlığı gelecek bütün uygulama/erişim kararlarının yetkilendirildiği anlamına gelmez. Tasarım değerlendirme kapıları, kurulacak DevOS'un her iç adımında Batu onayı isteyeceği anlamına gelmez.

## 4. Sonuçlar ve aşamalar arası devir

### 4A. P1 ve P2

[P1-01](work/P1-01-claude-cloud-environment-map.md) resmî kaynak ve sabit Loopinance incelemesidir; canlı cloud yeterliği değildir. Tanım, çalıştırma, bağlam ve çıktı kullanımı farklıdır. İletişim tek topolojiye indirgenmedi; otomatik plan onayı güvence sayılmadı. Kalıcı Work/Information runtime hafızasına bırakılmadı. Cloud plugin belgelerindeki çelişki açık tutuldu.

**Q01–Q06:** Etkin cloud kip/araçları; talep→kullanım zinciri; plugin çelişkisi; kalıcı state; kaynak/yazma erişimi; durma/güvence. Yalnız seçilecek yol için yük taşıyan belirsizlik kaynak veya gerçek probe ile çözülür. P1-01'deki eski next=P2 ifadesi tarihsel checkpoint'tir.

[ACTORS](ACTORS.md) DR01–DR16 ilk isim/lineage registry'si; [P2-01](work/P2-01-named-role-contracts.md) ilk sözleşmelerdir. Motivasyon/başarı yönü, girdi/yeterlik, tetik, teslimat/tüketici ve yetki sınırı vardır. 16 ayrı agent veya nihai kadro değildir. R1–R25 mekanik eşleme kontrolü competence veya semantik doğruluk kanıtı değildir. P3 gerçek rol çakışması gösterirse P2'ye hedefli dönülür.

### 4B. P3 konsolidasyonu ve ilerleme

[P3-01 v0.4](work/P3-01-work-information-discussion.md), yaşayan iş ağı, ihtiyaca göre işbirliği ve kalıcı bilgi omurgasını korur. G SOUL geliştirmeyi; Y DevOS işleyişini ve çalışma alanının düzenini hedefler. İkisi de Work/reasoning taşır; Y yalnız teknik altyapı veya Foundation ENVIRONMENT değildir.

DR06-G/Y işin öncelik/bağımlılık koordinasyonunu gerçek çalıştırma/bakım/devrinden; DR13-G/Y içerik/sonuç güvencesini çalışma koşullarının güvencesinden ayıran aday profillerdir. D021 ile içerik sahibinin ve düzen sahibinin sınırı kabul edildi. Ancak fiziksel ayrı agent, tam profil sözleşmesi veya rol sayısı kabul edilmedi; P2 tabanı korunur.

**Bu tur yeni somut karşılık:** Mantıksal bilgi alanları; talep/itiraz/karar durumları; yeni çıktı→yerleştirme→güncelleme→devir→yeniden kullanım/arşiv bakım sözleşmesi. Her olayda içerik katkısı ile düzen katkısı ve devam koşulu gösterilir. Aynı nesnenin çift current kopyası, eski temelle ezme, arşivin aktif keşfe sızması ve yalnız kozmetik işin bütün ilerlemeyi durdurması önlenmesi gereken durumlar olarak görünürdür.

Hermes Note30, fiziksel arşiv/aktif keşif, bakım yetkisi ve yüklenme≠etkin kullanım ayrımları için hedefli kullanıldı. Work/Actors/Information, Revision M5, RPD, Work-management, Superpowers ve Gas Town'un önceki nitel kaynakları korunur. Gerçek okuma sınırı P3-01 §9'dadır. Yeni güncel ürün veya canlı runtime iddiası yoktur.

**Sonraki tek bütünlüklü P3 işi:** İki eşzamanlı iş, ortak kayıt değişikliği, açık inceleme itirazı ve oturum kesintisini tek senaryoda izlemek; sahip, yetki, tüketici, kalıcı durum ve tetik bağlarında kalan semantik açığı bulmak. Maddi açık kalmazsa P3 kapanış/P4 gereksinim devri hazırlanır; sırf daha fazla kontrol yapılabilir diye genel audit turları açılmaz. P4 bu tur başlamadı.

## 5. Foundation ve studies kullanım yolu

Foundation hazır reçete değildir: assistant'ın bakışını genişleterek atlanabilecek iş/bilgi/aktör/ortam ayrımlarını ve soruları ortaya çıkarmalıdır. Studies gerçek uygulama örnekleri, karşı örnekler ve sınırlar sağlar. İlgili Foundation metniyle düşünülür; sonra o çerçeveyle studies okunur. Kaynak isimlerini dosyaya eklemek yeterli değildir.

Başlangıç: [Foundation STATE](../../research/soul-foundations/STATE.md) → [REUSE](../../research/soul-foundations/08_foundation-sufficiency-reuse-review/REUSE.md). Somut soru için:
- [Work](../../research/soul-foundations/03_ground-deepening/grounds/work/INDEX.md): gerekli iş, plan, yürütme, bağımlılık, kapanış ve yeniden açma.
- [Information](../../research/soul-foundations/03_ground-deepening/grounds/information/INDEX.md): kaynak/statü/sürüm, bakım, seçim, görünürlük ve kullanım.
- [Actors](../../research/soul-foundations/03_ground-deepening/grounds/actors/INDEX.md), [Environment](../../research/soul-foundations/03_ground-deepening/grounds/environment/INDEX.md) ve [Composition](../../research/soul-foundations/05_relation-control-composition/INDEX.md): rol/yetki, gerçek koşullar ve bağlar.

[Studies CATALOG](../../research/studies/CATALOG.md) → ilgili META/STATE/INDEX → gerçek bulgu/kaynak. Adaylar: Work Management/Project Control ve RPD (iş keşfi/akış); Context–Memory–Harness ve Hermes (bilgi/bağlam/kütüphane bakımı/süreklilik); Superpowers, gstack ve ECC (rol/devir/kontrol/tüketici); Gas Town (iş ve çalıştırma/kapasite/liveness sınırı). Bütün korpus her tur yüklenmez; gerçek okuma/sürüm kapsamı korunur. Karar-kritik ayrım özetle kapanmıyorsa kaynağa inilir.

[Keel](../../research/soul-context/repos/keel/README.md), [OS Architect](../../research/soul-context/repos/os-architect/README.md) tarihsel örneklerdir. [Kanon](https://github.com/batuhanozgun/loopinance-claude-code/tree/main/kanon) ve [v2](https://github.com/batuhanozgun/loopinance_v2) yalnız ilgili tetik/iletişim/kayıt yollarıyla karşılaştırılır; P1'in sabit kaynakları P1-01'de. Kullanıcı bildirimi, dosya talimatı ve çalışan mekanizma ayrı kanıt statüleridir. Örneklerin backlog'u, insan kapıları veya ECC seçimi DevOS'a taşınmaz; bu depolara yazılmaz.

## 6. Açık tasarım kararları

P2-01'in aday yorumu familyayı sınıflandırma, rolü sözleşme, motivasyonu başarı yönü, gerçek agent binding'ini ayrı görevlendirme olarak tutar. Motivasyon başına agent seçilmedi.

D021 kabulü çalışma alanı sorumluluğunu netleştirir; P3 v0.4'teki dört mantıksal alanı veya tüm bakım/durma kurallarını peşinen onaylamaz. Somut expertise/izin, atomik yayın/çakışma, iletişim, dosya biçimi ve actual actor allocation P4/P5 ile; gerçek güvenilirlik P6 ile bağlanacaktır. P3 anlam sözleşmesi bu mekanizmaların kurulduğunu göstermez.

## 7. Yaşayan plan ve değişim kaydı

Her tur current işi P kimliğine/teslimata bağlar. Sonuç, kullanılan kaynak/sürüm, açık soru, sonraki bounded adım ve üst işe dönüş kaydedilir. Bütün yön her tur yeniden icat edilmez. Kısa sunum gerekli çalışma derinliğini veya bütünlüğünü azaltmaz.

Maddi değişiklikte current STATE, devir HANDOFF, üst plan WORK, gerçek kullanıcı kararı DECISIONS güncellenir. İlk rol sözleşmesini koşullandıran aday fark P3'te açıkça korunabilir; kabul edilmiş kadro gibi geçirilmez. Yeni dosya mevcut yüzey yetmediğinde açılır; boş aşama dosyaları oluşturulmaz.

- **27 Eylül 2026 / v1.0:** Önceki birikime bağlı P1–P6 master harita kuruldu; yalnız plan hazırlığı.
- **27 Eylül 2026 / v1.1:** P1 kaynak/Loopinance incelemesi; runtime sınanmadı, Q01–Q06 devredildi.
- **27 Eylül 2026 / v1.2:** Kullanıcının P4 sırasını anlayıp devam istemesiyle P2 ilk sözleşmeler ACTORS'a bağlandı. SOUL görevi veya topoloji seçilmedi.
- **27 Eylül 2026 / v1.3:** P3 araştırmaya dayalı tartışma bazı olarak açıldı; üst sıra değişmedi.
- **P3 v0.2:** İş–yapı, iki koordinasyon/güvence, rol yerleşimi ve bilgi sahipliği birleştirildi.
- **P3 v0.3:** Kurgusal rol konuşması, bağlam, araştırma/karar, itiraz, kayıt ve kesinti/yeni bilgi dönüşü; M5 hedefli okundu.
- **P3 v0.4:** Kullanıcının çalışma alanı düzeni açıklaması ve dar D021 kabulü işlendi. P3 konsolide edildi; bakım/yeniden kullanım ve talep/itiraz/karar sözleşmeleri ilerletildi. Hermes Note30 hedefli kullanıldı. Tek uçtan uca P3 birleşim sınaması sırada; master v1.3 ve P4–P6 sınırları korundu.
