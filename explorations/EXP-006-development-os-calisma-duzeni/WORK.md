# EXP-006 — WORK ve master plan

**Rol:** DevOS tasarımının üst iş haritası, bağımlılıkları ve aşama teslimatları.  
**Plan:** v1.3 — 27 Eylül 2026; P1–P6 hedef ve sırası korunuyor. P3 ayrıntısı v0.5 tasarım devrine hazır aday düzeyine ilerledi.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışabileceği düzeni ortaya koymak ve yetkilendirilen aşamalarda gerçekleştirmek/sınamak.  
**Current:** **P3 DESIGN HANDOFF READY v0.5 / CANDIDATE / USER EVALUATION.** D021 kabul; bütün tasarım veya runtime kabulü değil. P2 ilk sözleşme tabanı ve P1 kaynak sonucu/runtime açıkları korunur. **P4–P6 başlamadı.**  
**Kaynak:** [U002](sources/U002-cloud-plan-and-autonomy.md); kısıtlar [DECISIONS](DECISIONS.md), son yön [P3-01 §1](work/P3-01-work-information-discussion.md#1-kullanıcı-yönü-ve-önerinin-sınırı). Current yetki STATE, devir HANDOFF'tadır.

## 1. Önceki çalışmadan devralınan zemin

SOUL hedefi → DevOS'un SOUL üzerinde yapacağı işler → gerekli kabiliyet/sorumluluklar → AI rolleri, mekanik destek ve insan sınırı → S1 konsolidasyonu → aşağıdaki DevOS tasarım planı.

İlk altı kök iş: hedefi belirlemek; gereken işi keşfetmek; yapılabilir kılmak; gerçekleştirmek; sınamak/yeniden çalışmak; zaman içinde sürdürmek. B1–B9 bunların yerine geçen sıra veya SOUL modülleri değildir.

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

B belgeleri reference/candidate decomposition'dır; uygulanmış kapasite veya yürütmeye alınmış SOUL backlog'u değildir. B1'in ilk sırada olması geliştirmeye onunla başlama kararı değildir.

[S1 master](work/S1-role-responsibility-consolidation.md) ve [S1-17](work/S1-17-consolidation-closure-audit.md), F1–F8 ailelerini/uzmanlık sınırlarını mevcut kapsam için CLOSURE-READY / CANDIDATE düzeyine getirdi. R1–R25/M1–M9 lineage ve ilk P2 modeli [ACTORS](ACTORS.md)'tadır. Nihai roller/agent sayısı, kullanıcı kapanışı veya çalışan DevOS kabulü çıkarılmaz. Yeni somut çelişki yoksa S1 isim incelemesi tekrarlanmaz.

F2 gerçekleştirme sorumluluğu örtük kalmaz; her dosya yazımı F2 değildir ve reusable olmak şart değildir. F3 Information Lifecycle ve Actor/Role Participation Lifecycle ayrı uzmanlıklardır; kayıt/katılım işletimi doğruluk, yetki veya gerçek etkiyi ikame etmez. Kaynak, yeterlik, tetik, devir ve güvence yükleri sonraki aşamalara taşınır. S1-16 full-read qualification'ı S1-17 §7'de korunur.

## 2. Bu planın sınırı ve ana gereksinimler

Bu, **DevOS'u ortaya koyma planıdır; DevOS'un SOUL'u üretme planı değildir.** İlk ve sonraki gerçek SOUL işlerini kurulacak ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant bunları ekibin yerine seçmez. Tasarım senaryosu gerçek backlog veya bağımsız iş keşfi başarısı sayılmaz.

**K1 — İşlevsel iletişim:** Bir rol başka rolden bilgi, araştırma, değerlendirme veya kontrol isteyebilmeli; talep uygun sorumluya ulaşmalı, çalışma etkinleşmeli, yanıt geri dönmeli ve sonraki kararda kullanılabilmelidir. Doğrudan mesaj, ana oturum, ortak kayıt, olay veya başka yöntemler adaydır. Talebi dosyaya yazmak tüketildiğini göstermez.

**K2 — Rutin akışın elle tetiklenmemesi:** Yetkili çalışma başladıktan sonra her rol/sonraki iş için Batu'nun komutu veya mesaj taşıması gerekmez. Başlangıç/yeniden başlatma, gerekli müdahale, gerçek yetki ihtiyacı ve kabul mümkündür. Sonsuza kadar kesintisiz, bütçesiz veya bütünüyle insan-bağımsız çalışma gereksinimi yoktur.

**D021 — Çalışma alanı düzeni:** Dosya/kayıtların yeri, güncelliği, tek yetkili kaynağı, bulunabilirliği, kaynak/sürüm ilişkileri, kontrollü bakımı, devri ve tekrar kullanımı asli sorumluluktur. İçerik sahibi ne söylendiği/gerekçesini taşır; düzen tarafı onu korunabilir/kullanılabilir tutar, ürün kararının yerine geçmez. Görsel klasör temizliği yeterli değildir.

Kanon manuel tetikleme sınırının; loopinance_v2 kullanıcının rutin tetikleyici olmamasının örneğidir. V2 veya ECC'nin bütünü benimsenmedi. SOUL ürün dosyaları ile DevOS'un kendi plan/bilgi/karar/kanıt/devam kayıtları ayrı amaçlı ve ilişkili yönetilir; iki ayrı repository veya belirli klasör şeması seçilmedi.

## 3. Master plan — baştan görünen bütün yol

| Aşama | Esas soru ve teslimat | Dayanak / önceki bağ | Geçiş ölçütü | Durum |
|---|---|---|---|---|
| **P1 — Claude cloud gerçekliği** | K1/K2 bakımından alt ajan, ana oturum ve ajan takımı imkân/sınırlarının kaynaklı Environment haritası | Birincil Claude belgeleri; B5/B6/B8; ilgili Loopinance kaynakları | Belge, gözlem ve açık belirsizlik ayrı; iletişim/tetik/bağlam/yetki/süreklilik sınırları görünür | **KAYNAK İNCELEMESİ TAMAM / RUNTIME SINANMADI**; [P1-01](work/P1-01-claude-cloud-environment-map.md) |
| **P2 — Adlandırılmış roller** | Açık rol isimleri ve amaç/başarı yönü, bilgi, teslimat, yetki sözleşmeleri | P1; ACTORS; S1-02/03/17; Actors/Work Foundation ve studies | Kim ne için var, ne üretir, kimle hangi koşulda etkileşir anlaşılır; sayıdan agent çıkarılmaz | **İLK TASLAK / CANDIDATE**; [P2-01](work/P2-01-named-role-contracts.md); P3 G/Y ve D021 farklarıyla birlikte okunur |
| **P3 — WORK–INFORMATION işleyişi** | İş keşfi, tartışma, planlama, araştırma/üretim, alan bakımı, tekrar kullanım ve devam döngüsü | P2; Work/Information Foundation; B2/B4/B6/B8; studies | İş/plan/gerçek ayrımı, karar/kayıt sahipliği, bilgi kullanımı, alan düzeni ve devir görünür | **DESIGN HANDOFF READY v0.5 / CANDIDATE / USER EVALUATION**; [P3-01](work/P3-01-work-information-discussion.md); canlı başarı veya bütün ayrıntıların kabulü değil |
| **P4 — Bütünleşik DevOS tasarımı** | P1–P3 ile alt ajan/takım veya gerekçeli birleşim; actor allocation, iletişim, fiziksel çalışma alanı ve sahiplik | P1 kanıtı + P2 tabanı + P3 G/Y, D021 ve H1–H6; B6/B7/B9 | K1/K2 ve alan düzeni için uçtan uca yol; seçimi taşıyan Environment açıkları doğrulanmış, tasarım gözden geçirilmiş | **NEXT LOGICAL PHASE / NOT STARTED**; kullanıcı değerlendirmesi/sonraki devamıyla |
| **P5 — Dosyalar ve mekanizmalar** | Seçilen tasarımın gerçekten tüketilen ajan tanımları, ortak talimatlar, kayıt/bağlam ve kontrollerle gerçekleştirilmesi | P4; gereken yerde yeniden doğrulanan P1 | Dosya varlığı değil yükleme, etkinleşme, izin ve tüketici bağı gösterilir; gereksiz özel sistem yok | PLANNED / NOT STARTED |
| **P6 — Sınama ve devretme** | Hedef devri, iş keşfi, talep/cevap, normal otomatik ilerleme ve müdahale sonrası devam | P5; B9; gerçek Environment ve güvence gereği | Rutin rol geçişinde kullanıcı tetiklemesi gerekmiyor; bilgi/karar/sürüm bağı ve başarısız/açık durumlar korunuyor | PLANNED / NOT STARTED |

**Bağımlılık:** P1 → P2 ↔ P3 → P4 → P5 → P6. Yeni yük taşıyan ortam sorusu P1'e; gerçek rol/anlam açığı ilgili P2/P3'e; P6 kusuru sorumlu aşamaya hedefli döner. Geri dönüş bütün planı yeniden başlatmaz.

Bu plan katı waterfall veya kabul edilmiş mimari değildir. Kaynaklı Environment bilgisi actual hedef yeterliği sayılmaz. Tasarımda kullanıcıya dönüş kapısı, kurulacak DevOS'un her rutin iç adımında Batu onayı isteyeceği anlamına gelmez.

## 4. Sonuçlar ve aşamalar arası devir

### 4A. P1 ve P2

[P1-01](work/P1-01-claude-cloud-environment-map.md) resmî kaynak ve sabit Loopinance incelemesidir; canlı cloud yeterliği değildir. Tanım, çalıştırma, bağlam ve çıktı kullanımı farklıdır. İletişim tek topolojiye indirgenmedi; otomatik plan onayı güvence sayılmadı. Kalıcı Work/Information runtime hafızasına bırakılmadı. Cloud plugin belgelerindeki çelişki açık tutuldu.

Q01–Q06: etkin cloud kip/araçları; talep→kullanım; plugin çelişkisi; kalıcı durum; kaynak/yazma erişimi; durma/güvence. Yalnız seçilecek yolun yük taşıyan belirsizliği kaynak veya gerçek probe ile çözülür. P1-01 içindeki eski next=P2 tarihsel checkpoint'tir.

[ACTORS](ACTORS.md) DR01–DR16 ilk isim/lineage registry'si, [P2-01](work/P2-01-named-role-contracts.md) ilk sözleşmelerdir. 16 ayrı agent veya nihai kadro değildir. R1–R25 mekanik eşleme kontrolü competence/semantik doğruluk kanıtı değildir. P4, bu ilk tabanı P3'ün DR06-G/Y, DR13-G/Y ve D021 bakım farkıyla birlikte değerlendirir; ilk listeyi doğrudan ajan dosyalarına çeviremez.

### 4B. P3 sonucu

[P3-01 v0.5](work/P3-01-work-information-discussion.md) yaşayan iş ağı, ihtiyaca göre işbirliği ve kalıcı bilgi omurgasını korur. G SOUL geliştirmeyi; Y DevOS işleyişi ve çalışma alanı düzenini hedefler. İkisi de Work/reasoning taşır. İçerik sahibinin ne söylendiği/nedenini, düzen tarafının yer/statü/bağ/bulunabilirlik/bakımı taşıması D021 kabulüdür; bütün yeni ayrıntılar değil.

v0.4 bakım tetiklerini ve mantıksal yerleşimi birleştirdi. v0.5, iki katkının aynı dosyaya yazması, birine açık inceleme itirazı, yayın sırasında kesinti ve eski çalıştırmadan geç çıktı durumunu tek yürüyüşte ele aldı. Paralel aday ile current yayın; temel sürüm ile maddi bağımlılık; açık itiraz ile değişen dosya adı; içerik yayını ile doğru tüketici görünümü; iş ile çalıştırma/yayın denemesi ayrıldı.

**Çalışma sonucu:** Kavramsal P3 teslimatı P4'e devre hazır bulundu. Bu, kullanıcı kapanışı veya canlı test sonucu değildir. Senaryonun sonunda bir katkının yayımlanıp diğerinin incelemesinin açık kalması doğru bir tasarım durumu olabilir. Yeni genel audit veya yeni rol ailesi gerektiren somut açıklık bulunmadı; teknik karşılıklar henüz gösterilmedi.

Beads META/FINDINGS hedefli reuse'u claim/liveness/reopen ve etkinin belirsizliği sınırlarını besledi. Information I1–I5/Revision M5, Hermes Note30 ve Gas Town'un önceki kapsamları kullanıldı. Gerçek okuma ve nitel kanıt sınırı P3-01 §9'dadır.

### 4C. P4'e giden gereksinimler

Tek ayrıntı matrisi [P3-01 §10](work/P3-01-work-information-discussion.md#10-p3-değerlendirmesi-ve-p4e-gereksinim-devri)'dedir: H1 rol/ilk etkinleşme; H2 fiziksel alan/current erişim; H3 değişiklik/yayın; H4 talep/tüketim; H5 kesinti/kısmi sonuç/eski yazıcı; H6 güvence/bakım/yeniden kullanım.

P4 bu yükleri gerçek Claude seçenekleri ve fiziksel çalışma alanı tasarımıyla birlikte karşılaştırır. P1 Q01/Q02/Q04/Q05/Q06 seçilen yolda doğrulanır; Q03 yalnız plugin'e dayanılırsa açılır. Karşılanamayan yük sessizce varsayılmaz: başka yol veya hedefli P2/P3 revizyonu gerekir. P5 uygular, P6 negatif yollarla fiilî davranışı sınar.

**Current dönüş:** P3 sonucu kullanıcıya sunulur. Sonraki kullanıcı devamında P4 açılabilir; bu tur açılmadı. Yeni karşı kanıt veya kullanıcı düzeltmesi yoksa aynı soyut P3 karşılaştırmaları tekrarlanmaz.

## 5. Foundation ve studies kullanım yolu

Foundation gereklilik keşfi/bakış açısı sağlar, hazır reçete değildir. Studies bu çerçevede uygulama örneği/karşı örnek sağlar; isim listesi gerçek kullanım değildir.

[Foundation STATE](../../research/soul-foundations/STATE.md) → [REUSE](../../research/soul-foundations/08_foundation-sufficiency-reuse-review/REUSE.md) → soruya göre [Work](../../research/soul-foundations/03_ground-deepening/grounds/work/INDEX.md), [Information](../../research/soul-foundations/03_ground-deepening/grounds/information/INDEX.md), [Actors](../../research/soul-foundations/03_ground-deepening/grounds/actors/INDEX.md), [Environment](../../research/soul-foundations/03_ground-deepening/grounds/environment/INDEX.md), [Composition](../../research/soul-foundations/05_relation-control-composition/INDEX.md).

[Studies CATALOG](../../research/studies/CATALOG.md) → ilgili META/STATE/INDEX → gerçek bulgu/kaynak. RPD ve Work Management iş/önkoşul/akışı; Context–Memory–Harness ve Hermes bilgi/bağlam/bakımı; Superpowers, gstack ve ECC rol/devir/kontrolü; Gas Town/Beads iş/çalıştırma/claim/liveness ayrımlarını besleyebilir. Tüm corpus her tur yüklenmez; gerçek okuma/sürüm kapsamı korunur. Güncel ürün iddiasına dayanılan teknik seçimde birincil kaynak ve gerektiğinde gerçek ortam tazelenir.

[Keel](../../research/soul-context/repos/keel/README.md), [OS Architect](../../research/soul-context/repos/os-architect/README.md), [Kanon](https://github.com/batuhanozgun/loopinance-claude-code/tree/main/kanon), [v2](https://github.com/batuhanozgun/loopinance_v2) yalnız ilgili sınırlarıyla örnektir. Kaynak talimatı, kullanıcı bildirimi ve çalışan mekanizma ayrı kanıtlardır. Örnek depolara yazılmaz; backlog, insan kapısı veya ECC seçimi aktarılmaz.

## 6. Açık tasarım kararları

P2 motivasyonu rolün başarı yönü, gerçek agent binding'ini ayrı görevlendirme olarak tutan adaydır; motivasyon başına agent seçilmedi. P3 H1–H6 ve G/Y profilleri P4 için çalışma gereksinimi adayıdır; D021 bütün şema/yetki/ajan kararlarına peşin onay değildir.

Actor allocation, alt ajan/takım, fiziksel dosya/klasör, çağrı/mesaj, güncel-sürüm yayın koruması, izin/kalıcılık ve ilk bootstrap henüz seçilmedi. Bunların karşılığını P4 tasarlar, P5 gerçekleştirir, P6 sınar. P3 tasarım devrine hazır olması bunları çözülmüş saydırmaz.

## 7. Yaşayan plan ve değişim kaydı

Her tur current işi P kimliğine/teslimata bağlar; sonucu, kaynağı/sürümü, açık yükü ve üst işe dönüşü korur. Kısa sunum gerekli çalışma bütünlüğünü azaltmaz. Maddi değişiklikte current STATE, devir HANDOFF, üst plan WORK ve gerçek kullanıcı kararı DECISIONS güncellenir. Aday fark kabul edilmiş kadro yapılmaz; yeni dosya ancak gerekli olduğunda açılır.

- **v1.0:** Önceki birikime bağlı P1–P6 master harita; yalnız plan hazırlığı.
- **v1.1:** P1 kaynak/Loopinance incelemesi; runtime sınanmadı, Q01–Q06 devredildi.
- **v1.2:** P2 ilk sözleşmeler ACTORS'a bağlandı; SOUL görevi veya topoloji seçilmedi.
- **v1.3:** P3 araştırmaya dayalı tartışma bazı; üst sıra korundu.
- **P3 v0.2:** İş–yapı, koordinasyon/güvence, rol ve bilgi sahipliği.
- **P3 v0.3:** Kurgusal rol etkileşimi, kaynak/karar/itiraz ve devir; Revision M5.
- **P3 v0.4:** D021 dar kullanıcı kabulü; konsolide alan bakımı/yeniden kullanım; Hermes Note30.
- **27 Eylül 2026 / P3 v0.5:** İki eşzamanlı iş/ortak kayıt/açık inceleme/kesinti senaryosu; sürüme bağlı yayın ve inceleme, kısmi sonuç uzlaştırması, eski-yazıcı sınırı. Beads hedefli reuse. P3 tasarım devrine hazır aday; H1–H6 P4'e bağlandı. P4–P6 başlamadı; kullanıcı kabulü veya canlı başarı uydurulmadı.
