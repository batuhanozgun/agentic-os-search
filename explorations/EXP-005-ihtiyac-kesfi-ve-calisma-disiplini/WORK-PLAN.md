# EXP-005 — Arşivleme çalışma planı

**Başlangıç:** 2026-09-22. **İş:** Bu konuşmayı ders niteliğinde explorations'a almak. **Durum:** Kaynak aktarımı ve işleme sürüyor; henüz tam arşiv/yayın iddiası yok.

## Yetki ve sınır

Kullanıcının bu konuşmadaki son talebi: “Bu konuşmayı EXP-005 olarak ders niteliğinde repoya alır mısın? Konunun ortada kaldığının farkındayım ama explorations klasörü zaten deneyimleri kayıt altına almak amacıyla var.”

Bu yetki yalnız arşivleme, kaynak/yorum ayrımı, keşif bağlantıları ve bunların Research repository'sinde yayımlanması içindir. Daha önce iptal edilen DEVOS02-NEED-DISCOVERY-20260922 çalışmasını yeniden başlatmaz. DevOS repository'sine, PR #1'e, başka branch'lara, yerel Codex'e veya kontrol dosyalarına müdahale edilmez. Araştırma sorusunun açık olması arşivlemeyi engellemez; arşivin tamamlanması araştırmanın çözüldüğü anlamına gelmez.

## Başlangıç ve yazıcı

- Repository: `batuhanozgun/agentic-os-search`.
- Başlangıç main: `4d8b8b1aba963d5503676bdcb73b7d68b40045d7`.
- Başlangıç tree: `b8cf6a4398d6fa0dba8c31ffa7bc171d231f7f41`.
- Çalışma branch'i: `archive/exp-005-ihtiyac-kesfi-dersleri-20260922`.
- Tek yazıcı: Bu arşiv talebini yürüten ChatGPT oturumu. Ayrı native değerlendirici görevlendirilmedi; inceleme self-review ve deterministik arşiv denetimi olarak etiketlenecek.
- Mevcut `explorations/INDEX.md`, `CATALOG.md`, `PACKAGE-CONTRACT.md` ve EXP-004 STATE'i okundu. EXP-005 başlangıç dizininde bulunmuyordu. Önceki dört EXP'nin tam kaynaklarını yeniden okuduğumuz iddia edilmeyecek.
- Aynı konuşmada tam görünür R01–R09 protokolleri uygulama dayanağıdır; protokoller bu pakete araştırma bulgusu veya yeni etkin talimat olarak kopyalanmayacak.

## Kesin yazma kapsamı

Bu paketin `INDEX.md`, `STATE.md`, `WORK-PLAN.md`, `SOURCE-MANIFEST.json`; `sources/conversation/` altında sıralı kaynak aktarımı ve INDEX; `sources/ORIGIN-AND-ATTACHMENTS.md`; `artifacts/DEVOS02-NEED-DISCOVERY-20260922.md`; `reflections/LESSONS-AND-OPEN-QUESTIONS.md`; `retrieval/TOPIC-MAP.md` ve `CUMULATIVE-READING.md`; `checks/ARCHIVE-REVIEW.md`. Kütüphane keşfi için yalnız `explorations/INDEX.md` ve `explorations/CATALOG.md` güncellenecek. Önceki paketler ve agent-control değiştirilmez.

## İş sırası

1. Görünür konuşmayı başlangıç görseli/kapsam sorusundan iptal, protokol değerlendirmesi ve arşiv talebine kadar konuşmacı ve sıra kimlikleriyle koru. Özet, tam aktarım ve kaynakta erişilemeyen kesimleri açıkça ayır. Sistem/developer mesajları, gizli muhakeme ve token içeren araç yanıtları aktarılmaz.
2. Gerçekten mevcut görev belgesini değiştirmeden koru. Görsellerin mevcut byte kimliğini ve arşivdeki temsil düzeyini belirt. İçeriği olmayan bir bağlantıyı okunmuş kaynak sayma.
3. Konunun kavramsal değerini, hatalı/geri çekilen teşhisleri, uygulama girişimini, kullanıcı müdahalelerini, sınırlı deney sonucunu ve iptali ayrı kaydet. Önceki assistant öz değerlendirmesini otomatik doğru kabul etme.
4. Kaynak mesajlarına bağlı dersler ve açık sorular üret; yeni yöntem, ürün, mimari veya uygulama kararı üretme. Başka araştırma programı başlatma.
5. İndeks/manifest/link/kimlik/kapsam ve hassas içerik kontrolleri; kritik iddialarda kaynak karşılaştırması. Gerçek bağımsız doğrulama ile self-review ayrılır.
6. Yalnız bu kapsamı güncel main ile uzlaştırarak yayımla; exact uzak geri okuma ve değişen dosya kontrolüyle teslim et. Başka çalışmaların yeni commit'leri geri alınmaz. Force push ve tarih silme yoktur.

## Arşiv kabul ölçütleri

- Konuşmanın yalnız son özrü değil, başlangıç sorusu ve bütün önemli yön değişimleri geri bulunabilir.
- Kullanıcının sözleri, assistant önerileri ve kullanıcı tarafından aktarılan Codex raporları karıştırılmaz.
- “Yeni motor eksik”, “RPD yeterli”, “küçük değişiklik faydasız”, “Cloud uygun değil”, “hiç plan yoktu” gibi hükümler kanıt sınırları ve karşı açıklamalarıyla korunur.
- Plan belgesinin varlığı saklanır; planın fiilen uygulanmış/hazırlığın doğrulanmış olduğu varsayılmaz.
- Dört vakalık sonuç bütün problem için yeterlik veya etkisizlik kanıtı sayılmaz. Shell erişimi, hizmetin yayın yolu, local commit ve remote içerik ayrı kalır.
- Son kullanıcı iptali açık ve bulunabilir; eski devam mesajları etkin talimat değildir.
- Kaynak aktarımının türü, eksikleri ve bağımsız doğrulanmayan unsurları STATE ve kaynak notunda görünürdür.
- Kütüphane girişleri pakete yönlendirir; payload gelmeden tamamlandı denmez.

## Durma ve devir

Şimdiki sonraki işlem kaynak aktarımıdır. Arşiv yayımlanıp geri okunduğunda bu kayıt işi kapanır. DevOS geliştirme, yeni deney ve Research erişimi onarımı bu işin devamı değildir. Arşivin dersleri henüz kullanıcı tarafından ayrı değerlendirilmiş veya kontrol değişikliği olarak benimsenmiş sayılmaz.
