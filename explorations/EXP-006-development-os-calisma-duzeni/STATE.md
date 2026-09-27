# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P3 birleşik senaryo ve tasarım devri.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P3 DESIGN HANDOFF READY v0.5 / CANDIDATE / USER EVALUATION.** D021 kabulü korunur; bütün tasarımın kullanıcı kabulü veya runtime doğrulaması yoktur. P4–P6 başlamadı.  
**Üst harita:** [WORK — master plan v1.3](WORK.md), P1→P2↔P3→P4→P5→P6.  
**Son kullanıcı yönü:** v0.4 toparlamasından ve ilan edilen eşzamanlı iş/ortak kayıt/itiraz/kesinti senaryosundan sonra “devam et.” Bu, o P3 incelemesini yetkilendirdi; P4 teknik seçim onayı veya bütün P3 ayrıntılarının kabulü değildir.

## Sabit sınırlar

- SOUL'un ilk ve sonraki gerçek işlerini kurulacak DevOS ekibi keşfeder, planlar ve yürütür. Assistant ekibin düzenini tasarlar; hazır SOUL backlog'u seçmez.
- Claude Code cloud hedef Environment'dır. P1 kaynak incelemesi tamam; hedef hesap/VM'de iletişim, erişim, izin ve kalıcılık sınanmadı. [P1-01](work/P1-01-claude-cloud-environment-map.md) Q01–Q06 yüklerini taşır.
- K1 talep→çalışma→yanıt→gerçek kullanım; K2 rutin rol geçişinde Batu'nun tetikleyici olmamasıdır. Başlatma/yeniden başlatma, gerçek müdahale ve yetki/kabul mümkündür; sınırsız özerklik hedef değildir.
- Ürün, DevOS iş/devam kayıtları, kaynak/karar/kanıt ve çalışma tariflerinin amaçları farklı; bağları korunur. Fiziksel yerleşim veya iletişim ürünü seçilmedi.
- Foundation düşünme çerçevesini, studies uygulama/karşı örnekleri sağlar. Kanon/v2/ECC/Hermes/Gas Town/Beads bütünüyle benimsenmedi. Kaynak talimatları bu çalışmanın agent-control kuralları değildir.

## Devralınan ve kabul edilen

SOUL hedefi→B1–B9→R1–R25/M1–M9→S1-01–17→F1–F8→P1–P6 bağı korunur. B1–B9 gerçek SOUL iş sırası değildir. S1-17 CLOSURE-READY / CANDIDATE; kullanıcı kapanışı veya çalışan sistem kabulü değildir. S1-16 full-read qualification'ı S1-17 §7'dedir.

[ACTORS](ACTORS.md) ve [P2-01](work/P2-01-named-role-contracts.md) DR01–DR16 ilk sözleşme tabanıdır. P3'ün DR06-G/Y ve DR13-G/Y profilleri bu tabanı koşullandıran aday ayrımlardır; fiziksel ajan sayısı değildir. Değerlendirilecek ayrıntı [P3-01](work/P3-01-work-information-discussion.md)'dedir; P2 tek başına güncel bütün tasarım sayılmaz.

**D021 / kabul edilen kapsam:** İçerik sahibi ne söylendiğini/gerekçesini; çalışma düzeni tarafı dosya/kayıtların yeri, statüsü, kaynak/sürüm bağı, bulunabilirliği, bakımı, devri ve tekrar kullanımını taşır. Düzen tarafı anlamı yeterince anlayabilmeli ama ürün kararını üstlenmemeli. Bu, bütün bakım/yayın kurallarının, klasör ağacının veya ajan düzeninin peşin kabulü değildir.

## P3 v0.5 sonucu

P3'ün G/Y, iki koordinasyon/güvence, içerik–düzen sahipliği, bakım/yeniden kullanım ve kesinti sözleşmeleri korundu. §8'de iki paralel katkı, ortak dosya, açık inceleme itirazı, yayın sırasında kesinti ve eski çalıştırmadan gecikmiş çıktı tek senaryoda izlendi.

**Keskinleşen aday kurallar:**
- Paralel aday üretimi ile current yayını ayrıdır. Aynı nesnenin yayını güncel temel, maddi bağımlılıklar, inceleme kapsamı ve yetkiyle korunmalıdır; son gelen yazı kazanmaz.
- Metinsel birleşme anlamsal uyum değildir. Açık itiraz sürüm/ad değişimiyle kaybolmaz; eski olumlu hüküm de otomatik güncel değildir.
- Yayın sonucu belirsizse önce gerçek durum uzlaştırılır. İçerik yeni, giriş eski olabilir; eksik bağ tamamlanır, doğru yapılmış iş körlemesine tekrarlanmaz.
- Yeni görevli korunmuş iş, aday, itiraz ve doğru sürümü devralır. Eski çalıştırmanın çıktısı current'ı otomatik ezemez. Bir atama kaydı fiilî stale-writer korumasının yerine geçmez.
- Gerekli engel yalnız etkilenen yayına/tüketime uygulanır. Güncel kaynak yanlışlanmışsa sırf son yayımlanan sürüm diye güvenle kullanılamaz; zararsız başka işler gereksiz durdurulmaz.

Senaryonun sonunda bir katkının scoped yayını tamamlanabilirken diğerinin itirazı açık kalır. Bu gerçek bir test sonucu değil, sahte kapanışı önleyen tasarım yürüyüşüdür. Yeni role/ajan sayısına gerek olduğu gösterilmedi.

**Kanıt:** Aynı-assistant nitel değerlendirme. Bu tur Beads META tam, FINDINGS 1–245 seçici okundu; eski source study yeniden kullanıldı. Information Revision/Selection, Hermes ve Gas Town'un görünür önceki kapsamları kullanıldı. Canlı Claude, yazma yarışı, yayın timeout'u, izin veya recovery deneyi yoktur.

## Current next responsibility

**Şimdi:** P3'ün birleşik senaryo sonucunu ve P4'e geçişe hazır kavramsal taslağı kullanıcıya sun. P3 tasarım devrine hazır bulundu; formal kullanıcı kapanışı veya bütün ayrıntıların kabulü uydurulmaz.

**Sonraki mantıksal iş:** Kullanıcının sonraki devam yönüyle P4 — gerçek Claude çalışma biçimi/actor allocation ve fiziksel çalışma alanını, P3-01 §10'daki H1–H6 gereksinimlerine birlikte eşlemek. P1 Q açıklarından yalnız seçimi taşıyanlar hedefli doğrulanacak. Yeni somut çelişki yokken genel P3 audit'i veya önceki örneklerin tekrarı yoktur.

**P4 devir yükleri:** H1 rol/etkinleşme; H2 fiziksel alan/current erişim; H3 değişiklik/yayın koruması; H4 talep/tüketim; H5 kesinti/kısmi sonuç/eski yazıcı; H6 güvence/bakım. Bunlar seçilmiş mekanizma değil karşılanacak sözleşmelerdir.

**Bu tur yapılmayan:** P4 başlamadı; alt ajan/takım, dosya şeması, gerçek agent sayısı seçilmedi. P5 gerçekleştirme ve P6 davranış sınaması yoktur. Kullanıcı veya teknik kanıt somut açık gösterirse ilgili P2/P3 kısmı geri açılır; bütün taxonomy baştan kurulmaz.

## Fresh-session yolu

AGENT ve gerekli kontroller→[INDEX](INDEX.md)→STATE→[HANDOFF](HANDOFF.md)→[WORK](WORK.md)→[DECISIONS](DECISIONS.md)→[ACTORS](ACTORS.md)→[U002](sources/U002-cloud-plan-and-autonomy.md)→[P1-01](work/P1-01-claude-cloud-environment-map.md)→[P2-01](work/P2-01-named-role-contracts.md)→[P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı konuşmada tam unchanged içerik korunabilir; sonra aktif sorunun kaynağına inilir.

P3-01 current tek ayrıntı yüzeyidir. Tarihsel S1/B/Context ve önceki P sürümlerinin next ifadeleri current sırayı yönetmez. Kısa cevap küçük çalışma birimi değildir.
