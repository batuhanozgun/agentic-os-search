# EXP-006 — STATE

**Durum:** AÇIK / DevOS tasarım çalışması. **Güncelleme:** 27 Eylül 2026.
**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini, SOUL'un gerektirdiği gerçek kabiliyetlere göre ortaya koymak.
**Current:** **P4 / SOUL ODAKLI RAPOR v2 HAZIR / MİMARİ ÖNERİ / KULLANICI DEĞERLENDİRMESİ.** Gerçek DevOS kurulmadı; P5/P6 tamamlanmış değildir.
**Üst plan:** [WORK](WORK.md). **Yeni ayrıntı/artefakt kaydı:** [P4-02](work/P4-02-soul-derived-report-v2.md).

## Son yetki ve teslimat

Kullanıcı ilk 200 sayfalık raporu yüzeysel tarama veya küçük eklerle düzeltmek yerine baştan yeniden yazmayı istedi. Esas yön, SOUL'un ne olacağına göre DevOS gereksinimlerini türetmek; gerekli kaliteyi daha kolay uygulamaya sığdırmak için düşürmemektir. Bu, yeni teknoloji/mimari tercihlerinin kullanıcı kabulü değildir.

Yeni rapor **tam 200 sayfa** ve düzenlenebilir kaynak paketi olarak konuşmada teslim edilir. PDF, Markdown ve ZIP'nin adları/hash'leri P4-02 §2'de. **Dosyaların tamamı GitHub'a yüklenmedi; bu repository yalnız teslimat ve current mimari farkını kaydeder.** Ayrıntılı yeni çalışmada gerçek ekler okunmalıdır; bu özet raporun yerine geçmez.

## Değişen mimari öneri

- Claude cloud bilişsel ekibi ile korunan deterministik kontrol hizmetleri ayrılır; takım ağırlıklı sürekli işbirliği ve gerektiğinde odaklı alt ajan profilleri önerilir. Hedefte yeterlik gösterilmedi.
- PostgreSQL canlı iş/atama/inceleme/yetki/yayın ve typed relation kayıtlarını; Git ürün ve yayımlanmış rol/yöntem/politika içeriklerini taşır. Hash'li kaynak/kanıt gövdeleri korunur. Aynı nesnenin iki bağımsız yazma otoritesi olmaz.
- Graph engineering birinci sınıf tasarımdır: tür/sürüm/scope, AND/OR destek, invariant, sorgu, concurrency ve etki değerlendirme yolu açık. Graph sonucu anlamsal doğruluğu otomatik ilan etmez.
- Memory yaşam döngüsü ile exact/lexical/semantic/graph retrieval ve context compiler birlikte tasarlanır. Gerekli bilgiyi azaltmak token optimizasyonu diye meşrulaştırılmaz.
- Korunan publisher, read-set/revision, claim generation, outbox/inbox ve DB–Git uzlaştırması vardır. Shared Claude runtime agent adları bağımsız güvenlik kimliği sayılmaz.
- Mekanik doğruluğa ek iş keşfi, bağlam yeterliği, uzun/bileşik eser ve yöntem aktarımının gerçek değerlendirmesi gerekir.

Bu farklar yalnız graph eki değildir. Önceki [P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) teknik baseline olarak korunur; **current seçim ve next-work authority değildir**. Eski salt Git çalışma kaydı/alt-ajan tercihi yeni rapora otomatik taşınmaz.

## Korunan kararlar

Claude Code cloud hedefi; SOUL'un ilk ve sonraki gerçek işlerini ekibin keşfetmesi; K1 talep→çalışma→yanıt→kullanım; K2 rutin rol geçişlerinde Batu'nun tetikleyici olmaması; gerçek müdahale/yetki/kabulün korunması değişmedi.

D021 içerik–çalışma alanı sahipliği korunur. G SOUL içeriğini/sonucunu, Y DevOS işleyişini ve düzenini hedefler. İkisi de Work/reasoning taşır. Rol sayısı agent sayısı değildir. Research talimatları otomatik DevOS kontrolü yapılmaz.

B1–B9/S1/F1–F8/P2/P3 birikimi provenance'dır; gerçek SOUL backlog'u veya çalışan kapasite değildir. [DECISIONS](DECISIONS.md) kabul edilmiş sınırları taşır; yeni raporun teknik seçimleri öneri olarak ayrı kalır.

## Gerçek kanıt

Yerel Python/SQLite modelinde 40 test geçti; dört hedefli kontrol kaldırma denemesinde ilgili testler hata yakaladı. Aynı yazarlı, sınırlı semantik deneydir. Gerçek PostgreSQL, Claude, kimlik doğrulama, Git/cloud yayını, sandbox, production restore veya SOUL bilişsel yeterliği kanıtı değildir. Ham kayıtlar kaynak ZIP içindedir.

PDF'nin 200 sayfa/bağlantı/kaynak/glyph/bbox kontrolü ve görsel düzen incelemesi yapıldı; bu belge kalitesi kontrolüdür.

## Current next ve sınır

**Şimdi teslim:** Yeni PDF ve kaynak paketini kullanıcıya ver. Rapor üretimi tamam; yeni mimari kabulü veya hedef kurulumu değil.

**Sonraki mantıksal iş:** V2 değerlendirmesinden sonra rapordaki uygulama ve qualification programını gerçek cloud/operasyon deposu/kontrol hizmeti koşullarına bağlamak. Yeni kullanıcı yönü olmadan P5 kurulumu başlatılmaz. Eski P4-01'in izin matrisi next'ine veya genel P3 audit döngüsüne dönülmez.

## Fresh-session yolu

AGENT ve gereken kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [P4-02](work/P4-02-soul-derived-report-v2.md) → **gerçek v2 PDF/kaynak ZIP**. Ayrıntılı tasarım işi öncesi raporun gerekli tam bağlamı ve sözleşmeleri okunur; erişim yoksa ek dosya istenir, hafızadan yeniden kurulmaz.

ACTORS/P2/P3 ve eski P4 yalnız lineage/karşılaştırma gerektiğinde, kendi statüleriyle okunur. Önceki PDF ile v2 karıştırılmaz. Kısa kullanıcı cevabı çalışma derinliğini küçültmez.
