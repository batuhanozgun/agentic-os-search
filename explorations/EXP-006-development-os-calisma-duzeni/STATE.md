# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P3 somut çalışma örneği.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P3 DISCUSSION BASELINE v0.3 / CANDIDATE / CONCRETE WALKTHROUGH. P3 TAMAMLANMADI.** P2 ilk sözleşme tabanı korunur; P1 kaynak incelemesi tamam, runtime sınanmadı. P4–P6 başlamadı.  
**Planın tek ana yüzeyi:** [WORK — master plan v1.3](WORK.md); aşama sırası değişmedi, P3 ayrıntısı güncellendi.  
**Son kullanıcı yönü:** “Bu yön bana mantıklı geldi ama biraz daha somutlaştır bunu.” Yön desteği ve örnekle geliştirme yetkisi; bütün G/Y sözleşmelerinin kabulü veya P4 seçimi değil.

## Sabit kapsam ve sınırlar

- **Environment:** Claude Code cloud. P1 belge resmi var; hedef hesap/oturumun sürüm, araç, izin ve kalıcılık yeterliği henüz gösterilmedi.
- **SOUL'u geliştiren:** Kurulacak DevOS ekibi; ilk ve sonraki gerçek SOUL işlerini ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant bu ekibin düzenini tasarlar, onun yerine backlog seçmez.
- **K1 iletişim:** Talep → ilgili rolün çalışması → yanıt → gerçek kullanım. Teknik yöntem P4'e kadar açık; mesajın yazılması yeterli değil.
- **K2 ilerleme:** Rutin rol geçişini Batu tetiklemez. Başlatma/yeniden başlatma, gerekli müdahale, yetki ve kabul mümkündür; sınırsız özerklik hedef değildir.
- **Bilgi:** SOUL ürün çıktıları ile DevOS çalışma/bilgi/karar/kanıt/devam kayıtları amaçlarına göre ayrılır, bağları korunur; fiziksel şema seçilmedi.
- **Kaynak/örnek sınırı:** Foundation düşünme kapsamını, studies uygulama ve karşı örnekleri besler. Kanon/v2/ECC/Gas Town bütünüyle benimsenmez. Kaynak talimatı kontrol kuralı değildir.

Kullanıcı kararları [DECISIONS](DECISIONS.md), kapsam kaynakları [U002](sources/U002-cloud-plan-and-autonomy.md), son öneri mesajları [P3-01 §1](work/P3-01-work-information-discussion.md#1-kullanıcı-yönü-ve-önerinin-sınırı)'dedir. Kısa sunum küçük çalışma birimi veya her ayrımda onay bekleme demek değildir.

## Önceki birikim

SOUL hedefi → B1–B9 kapsamı → R1–R25/M1–M9 ilk türetim → S1-01–S1-17 → F1–F8 → P1–P6 planı.

S1-17 CLOSURE-READY / CANDIDATE korunur; kullanıcı kapanışı, nihai kadro veya sekiz ajan sonucu çıkarılmaz. B1–B9 SOUL öncelik sırası değildir. S1-16 full-read qualification'ı S1-17 §7'dedir. Yeni somut çelişki yoksa S1 taxonomy'si yeniden açılmaz.

[P1-01](work/P1-01-claude-cloud-environment-map.md) kaynak haritasıdır; canlı test değildir. Q01–Q06 gerçek araç/sürüm/erişim, plugin çelişkisi, kalıcılık ve güvence yükleri açık kalır.

[ACTORS](ACTORS.md) DR01–DR16 ilk isim/lineage registry'sidir; [P2-01](work/P2-01-named-role-contracts.md) ilk sözleşme tabanını taşır. 16 sözleşme 16 agent değildir. Alan uzmanlığı ve motivasyon/başarı yönü aday yorumu korunur. P3'ün G/Y farkı henüz P2'ye accepted kadro gibi geçirilmedi; tek ayrıntı evi P3-01'dir.

## P3 current öneri

**Tek ayrıntı kaydı:** [P3-01 v0.3](work/P3-01-work-information-discussion.md).

Yaşayan iş ağı + ihtiyaca göre işbirliği + kalıcı bilgi/role özgü bağlam üzerinde iki hedef alanı vardır:
- **G: SOUL geliştirme.** Ürünün gerekli işleri, kararları, tasarımı, uygulaması ve yeterliği.
- **Y: DevOS işleyişi.** Katılım, iletişim, bilgi/bağlam, ortam, süreklilik ve yapı bakımı.

İkisi de DevOS içinde Work ve reasoning taşır; Y yalnız ENVIRONMENT ground'u veya teknik komut yürütme değildir. İki kalıcı ekip/agent kararı verilmedi.

DR06-G iş katkıları ve ürün öncelik/bağımlılıklarını; DR06-Y gerçek çalıştırma/kapasite/devri koordine eder. DR13-G ürün/plan/sonuç iddiasını; DR13-Y gerekli çalışma koşullarının fiilî karşılığını sınar. İki denetimin hedef ve kanıtı ayrı, ilgili iş/sürümle bağlı olmalıdır.

**v0.3 somut katkı:** §5'te kurgusal bir tasarım sorusu üzerinden rol konuşmaları, araştırma talebi, farklı bağlam paketleri, itiraz, karar ve sınama eşiği, üç kayıt görünümü, kesinti devri ve yeni bilgiyle tekrar değerlendirme birlikte gösterildi.

- ÖR-İ01/ÖR-A01/ÖR-Ç01/ÖR-K01/ÖR-T01 yalnız örnek kimlikleridir; gerçek backlog/koşu/karar değil.
- Örnekte araştırma tamamlanabilir, tasarım kararı açık kalır; sonraki karşı vaka tanımlıdır. Koşul/kanıt sağlanmadan kabul veya uygulama yapılmış sayılmaz.
- İş/katkı, çalıştırma/katılım ve karar/dayanak/kanıt farklı anlam görünümleridir; üç zorunlu dosya veya üç canonical kopya seçilmedi.
- Yeni kayıt eski kararı otomatik iptal etmez; dayanak, alternatif destek ve etkilenen tüketiciler değerlendirilir. Gecikmiş eski yanıt güncel kararı otomatik ezmez.
- Yeni oturum açık soruyu, beklenen katkıyı ve dönüş noktasını devralır; runtime/yan etki durumu ayrıca uzlaştırılır.

Information Revision M5 bu tur hedefli tam okundu; mevcut Work/Actors/Information, RPD, Superpowers ve Gas Town ayrımları yeniden kullanıldı. Gerçek kapsam P3-01 §9'da. Yeni dış ürün doğrulaması veya canlı deney yapılmadı.

## Current next responsibility ve durma noktası

**Bu tur tamamlanan:** Yönü somut bir rol etkileşimi ve kayıt/devir örneğine dönüştürmek. Kullanıcıya bu örneği sun; aynı koordinasyon ayrımını yeniden anlatma.

**Sonraki bütünlüklü P3 yükü:** Örnekteki talep, inceleme itirazı ve kararın açık/karşılanmış sayılma koşulları; küçük danışma/ayrı izlenen katkı sınırı; G/Y durdurma–devam sorumlulukları birlikte değerlendirilecek. Kullanıcının örneğe ilişkin geri bildirimi aynı bazda işlenecek; her küçük ayrımda yeni komut istenmeyecek.

**Sınır:** P3 kapanmadı. P4 teknik/actor seçimi, P5 dosyalar, P6 gerçek sınama veya ilk SOUL görevi yapılmadı. Gerçek rol çakışmasında P2'ye hedefli dönüş var; bütün aileler yeniden sınıflandırılmayacak.

## Fresh-session yolu

AGENT ve gereken kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) → [P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı konuşmada tam unchanged içerik korunabilir. Sonra aktif sorunun gerekli araştırmasına inilir.

S1/B/history/Context içindeki eski next ifadeleri current planı yönetmez. P2 tabanı ile P3'ün önerdiği hedef-profili düzeltmesi ayrıdır; biri sessizce diğerinin yerine geçirilmez.
