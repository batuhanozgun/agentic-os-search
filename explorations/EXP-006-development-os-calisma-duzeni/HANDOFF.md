# EXP-006 — HANDOFF

**Güncelleme:** 27 Eylül 2026, P4 ilk teknik tasarım.  
**Devralma:** **P4 INITIAL TECHNICAL BASELINE / CONDITIONAL DESIGN / NOT DEPLOYED. P4 AÇIK; P5/P6 NOT STARTED.**  
**Üst amaç:** SOUL'u geliştirecek Claude Code cloud ekibinin düzeni. Assistant'ın SOUL backlog'unu seçmesi veya kullanıcının her rolü açması değil.

## 1. Okuma ve authority

[STATE](STATE.md)→HANDOFF→[WORK](WORK.md)→[DECISIONS](DECISIONS.md)→[ACTORS](ACTORS.md)→[U002](sources/U002-cloud-plan-and-autonomy.md)→[P1-01](work/P1-01-claude-cloud-environment-map.md)→[P2-01](work/P2-01-named-role-contracts.md)→[P3-01](work/P3-01-work-information-discussion.md)→[P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) tam okunur. Aynı konuşmada tam unchanged içerik tekrar yüklenmez.

WORK bütün harita; STATE current yetki; bu dosya devir; P4-01 güncel teknik tasarımın tek ayrıntı kaydıdır. P2/ACTORS ilk sözleşme tabanı, P3 G/Y ve H1–H6 devriyle birlikte kullanılır. P2 ilk 16 rolü otomatik 16 agent yapma. Eski P/S1/B dosyalarındaki next/not-started checkpoint'leri current yetkiyi değiştirmez.

## 2. Kullanıcı yönü ve geçiş

Kullanıcı P3'te işin koordinasyonu ile yapının koordinasyonunu, içerik denetimi ile alan düzeni denetimini ayırmayı önerdi. Özellikle dosyaların/klasörlerin yeri, güncelliği, bulunabilirliği, bakımı ve tekrar kullanılabilirliğini kastettiğini açıkladı. İçerik sahibi–düzen sahibi sınırı D021 ile dar biçimde kabul edildi.

P3 v0.5 iki iş/ortak dosya/açık itiraz/kesinti senaryosuyla kavramsal devre hazır bulundu. Kullanıcı bu sonuç ve P4 devam noktası sunulduktan sonra “devam et” dedi. Bu P4 teknik tasarım yetkisidir; bütün P3 detaylarının onayı, P4 önerisinin benimsenmesi veya P5 kurulum izni değildir.

Kısa cevap istenmesi az iş yapmak veya her küçük adımda kullanıcı komutu beklemek değildir. Bu tur bir rol adı daha eklemek yerine topoloji, dosya düzeni, çağrı ve yayın yolunu birlikte kuran taslak hazırlandı.

## 3. İlk teknik tercih

**Ana Claude cloud oturumu DR06-Y / DevOS İşletim Koordinatörü olsun; G koordinasyonu ve uzman katkılar adlandırılmış özel alt ajanlarla çalışsın.** Takımlar başlangıç zorunluluğu değil, açık alternatiftir.

Neden: İletişim yalnız takımlara özgü değil. Özel rol/girdi/araç sözleşmelerini ve merkezi olmayan teknik kararları koruyarak K1/K2'yi native yoldan kurma adayı var. Karşılığında gerçek alıcı/resume/background davranışı hedefte gösterilmelidir. Daha iyi çalıştığı deneysel olarak kanıtlanmadı.

Ana Y, çağırma/katılım/kapasite/kalıcı kayıt ve kontrollü yayını işletir. G koordinatörü ayrı bağlamda iş önceliği/bağımlılık/sonuç birleştirmeyi taşır. Planlama, araştırma, tasarım ve bilgi/bakım rollerinin gerekenleri etkinleşir. G/Y inceleyicileri ayrı, üreticinin geçmişini otomatik kopyalamayan ve doğrudan yazmayan çağrılardır. Uygulama/koşu gerekiyorsa ayrı üretim kanalı kullanılır.

Bir işi yapan uzman başka aktif uzmana soru sorabilir; henüz yoksa Y gerekli rolü etkinleştirir. Her mesaj Y'nin tekrar yazacağı özet değildir. Talep sahibi ve tüketici, native çağıranla otomatik eşitlenmez; Work/request ve dönüş kaydı korunur. G yeterliği yerine Y'nin mesaj başarı sinyali kullanılamaz.

**Tercih değişim koşulu:** Alt ajan yolu süregelen akran çalışmasını güvenilir taşıyamıyor, gereksiz kullanıcı tetiklemesi veya Y üzerinde anlam kaybettiren yeniden kurulum gerektiriyorsa takım yolu tekrar karşılaştırılır. Daha fazla agent veya takım etiketi tek başına üstünlük kanıtı değildir.

## 4. Fiziksel alan ve kalıcılık

Bir operasyon deposu içinde `soul/` ürün ve `devos/` iş/bilgi/karar/deneme/kütüphane alanları önerildi; gerçek repo seçilmedi veya açılmadı. Araştırma ayrı, ref'i bilinen salt-okur kaynaktır. Research erişimi hedefte doğrulanacak; Research kontrol dosyaları otomatik DevOS talimatı yapılmayacak.

Etkin rol tanımları `.claude/agents/`; ortak kısa giriş `CLAUDE.md`; aktif yöntemler `.claude/skills/`; izin/olay bağlantıları settings/hooks. Sırf aile–rol ayrımı var diye bütün tanımların ikinci `rol.md` kopyası yaratılmaz. Kütüphanedeki aday ve etkin skill aynı anda iki authoritative metin olmaz. Arşiv/yedek otomatik aktif keşfin dışında tutulur.

Geçici üretim kopyaları native worktree adayıdır; başlangıç SHA'sı açıkça kontrol edilir. Aday değişiklik ile geçerli içerik, iş kaydı ile çalışma denemesi ayrı kalır. Okuyucu uygun commit/snapshot'a bağlanır. Git commit varlığı içerik onayı değildir.

Dayanıklı checkpoint, cloud'un izinli session branch'ine doğrulanmış yayındır; her rol geçişinde main merge'i veya Batu onayı beklenmez. Yerel worktree/auto-memory tek otorite değildir. Son dayanıklı kayıttan sonraki kaydedilmemiş çalışma kaybolabilir; sınırsız kayıpsızlık garanti edilmedi.

## 5. Yayın ve gerçek açık

**Paralel aday üretimi, aynı branch'e sıralı kontrollü yayın** ilk tercihtir. Y yayın kanalını işletir; içerik kararı ilgili alan sahibi ve uygun inceleyicide kalır. Bu, DR07 bütün dosyaları yazsın anlamına gelmez.

Yayın hedefi/temeli, maddi bağımlılıkları, etkin görevlendirmeyi, değişen yol kapsamını ve inceleme/itiraz bağlarını karşılaştırmalıdır. Ürün ve ilişkili çalışma/index değişikliği aynı anlamlı commit'e bağlanabilir. Beklenen eski SHA, aradaki değişiklikleri yakalamak için mekanik adaydır.

**Kapanmamış H3/H5:** Worktree, tool etiketi, prompt veya Git old-SHA kontrolü tek başına izin duvarı değildir. Genel Bash, paylaşılan Git alanı, API/MCP ve kontrol dosyası değişimi bunu atlayabilir. Hedef cloud'da sınırlı yazıcı/eski-görevli koruması gösterilmeden paralel mutasyon güvenli denmez. Güvenli alternatif gerekirse salt-okur uzmanlar + dar mutasyon kanalı veya farklı izolasyondur; gereksinim sessizce azaltılmaz.

Kesintide önce remote/local checkpoint, gerçek yayın ve yetkili görevlendirme uzlaştırılır; uygulanmış işlem sırf ACK kaybolduğu için tekrarlanmaz. Eski alıcı adı/actor ID yeni yetki sayılmaz. Açık iş, itiraz, kaynak sürümü ve tüketici bağlantısı korunur.

## 6. Kanıt ve açık kabul kapıları

Resmî Claude subagent/team/cloud/worktree/permission/hook/memory belgeleri ile Git update-ref/worktree belgeleri hedefli tazelendi. Tüm sayfalar veya tüm product davranışı doğrulandı denmez. Teknik tasarım çıkarımı kaynak olgusundan ayrıdır; ayrıntı P4-01 §8.

Yerel Git 2.47.3 probe'u: beklenen r0 ile A yayını başarılı; aynı r0 ile B güncellemesi reddedildi ve A korundu. Beklenen eski değer kaldırılınca B yazılabildi. Bu, yalnız mekanik sürüm kontrolünü ve atlanabilirliğini gösterir. Hedef Claude, gerçek iki-agent yarış, ağ kesintisi veya sandbox/izin testi değildir.

P1 Q01/Q02/Q04/Q05/Q06 hâlâ seçilen yolda hedef kanıtı ister. Plugin'e dayanmayan taslakta Q03 çözülmüş sayılmaz ama gereksiz plugin araştırması açılmaz. P4 H1–H6 matrisi tasarım karşılıklarını ve canlı kabul gereğini birlikte taşır; metnin yazılması geçiş ölçütünü tamamlamaz.

S1-16 kaynak-tamlığı qualification'ı ve P3'ün nitel/same-assistant sınırı korunur. Research repo yayını DevOS'un kendi publication yolunun deneyi değildir.

## 7. Sıradaki anlamlı P4 işi

Rol→araç→okuma/yazma/yayın yetki matrisini ve hedef cloud için bir kabul denemesi paketini tamamla. Tanım/araç yüklenmesi, A→B→A ve sonucun kullanımı, checkpoint/yeniden giriş, doğrudan/dolaylı eski-yazıcı karşı vakaları birlikte bulunmalı.

İlgili gerçek target repo, Research erişimi, araç/sürüm veya çalıştırma kanıtı gerektiğinde bunu görünür açık olarak tut. Kullanıcıya kendisinde olmayan teknik kararı çözdürme; fakat var olmayan hesabı/erişimi de varsayma. Hedef koşulu seçim yönünü değiştirirse P4 alternatifini gerekçeli değiştir.

P4 açık kalır; bu tur P5 actual ajan/skill/hook dosyası veya hedef repo oluşturulmadı. Yeni genel P3 audit'i, aynı örnek tekrarı veya tüm familyaları yeniden sınıflandırma yapılmaz. Kullanıcıya başlangıç tercihi, fiziksel karşılığı ve kapanmamış kritik kanıtı kısa sun.
