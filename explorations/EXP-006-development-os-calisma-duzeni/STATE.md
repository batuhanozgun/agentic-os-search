# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P3 konsolidasyonu ve çalışma alanı bakım sözleşmesi.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P3 CONSOLIDATED WORKING DRAFT v0.4 / DISCUSSION.** D021 sorumluluk ayrımı kabul edildi; bütün P3 ayrıntıları veya mimari kabul edilmedi. P3 kapanmadı; P4–P6 başlamadı.  
**Üst harita:** [WORK — master plan v1.3](WORK.md), P1→P2↔P3→P4→P5→P6 sırası korunur.  
**Son kullanıcı yönü:** Çalışma alanının düzen/bulunabilirlik/bakım/yeniden kullanım sorumluluğuyla içerik kararının ayrılmasına katıldı; P3'ü toparlayıp devam etmemizi istedi. Bu yalnız tekrar özetleme veya her ayrımda komut bekleme talebi değildir.

## Sabit sınırlar

- SOUL'un ilk ve sonraki gerçek işlerini kurulacak DevOS ekibi keşfeder, planlar ve yürütür. Assistant ekibin düzenini tasarlar; hazır SOUL backlog'u seçmez.
- Claude Code cloud hedef Environment'dır. P1 kaynak incelemesi tamam; hedef hesap/VM'de iletişim, erişim, izin ve kalıcılık sınanmadı. Q01–Q06 yükleri [P1-01](work/P1-01-claude-cloud-environment-map.md)'de açık.
- K1: talep→çalışma→yanıt→gerçek kullanım. K2: rutin rol geçişinde Batu'nun tetikleyici olması gerekmez. Başlatma/yeniden başlatma, gerçek müdahale ve yetki/kabul mümkündür; sınırsız özerklik hedef değildir.
- SOUL ürünleri ile DevOS iş/bilgi/karar/kanıt/devam kayıtlarının amaçları farklı, bağları korunmuş olmalıdır. Fiziksel depolama veya iletişim yöntemi P4'te seçilir.
- Kanon/v2/ECC/Hermes/Gas Town hazır mimari olarak alınmaz. Foundation düşünme kapsamını, studies uygulama ve karşı örnekleri besler; talimatları burada etkin kontrol olmaz.

## Devralınan ve kabul edilen

SOUL hedefi→B1–B9→R1–R25/M1–M9→S1-01–17→F1–F8→P1–P6 bağı korunur. B1–B9 gerçek SOUL iş sırası değildir. S1-17 CLOSURE-READY / CANDIDATE; kullanıcı kapanışı veya çalışan sistem kabulü çıkarılmaz. S1-16 full-read qualification'ı S1-17 §7'de kalır.

[ACTORS](ACTORS.md) ve [P2-01](work/P2-01-named-role-contracts.md) DR01–DR16 ilk sözleşme tabanıdır. P3'ün DR06-G/Y ve DR13-G/Y profilleri bu tabana aday düzeltmedir; fiziksel ajan sayısı değil. Tek ayrıntı evi [P3-01](work/P3-01-work-information-discussion.md)'dir.

**D021 / kabul edilen kapsam:** İçerik sahibi ne söylendiğini ve gerekçesini; çalışma düzeni tarafı dosya/kayıtların yeri, statüsü, kaynak/sürüm bağı, bulunabilirliği, bakımı, devri ve tekrar kullanımını taşır. Düzen tarafı anlamı yeterince anlayabilmeli ama ürün kararını üstlenmemeli. Görsel klasör temizliği yeterli değildir. Bu, bütün yeni P3 kurallarına veya özel klasör ağacına peşin onay değildir.

## P3 v0.4 sonucu

- G: SOUL geliştirme ve içerik/sonuç güvencesi. Y: DevOS işleyişi ile çalışma alanının düzeni ve bunun güvencesi. İkisi de Work/reasoning; iki kapalı takım veya Foundation ground'u değildir.
- G koordinasyonu iş önceliği/bağımlılık/katkıyı; Y koordinasyonu çalıştırma/kapasite/bakım/devri taşır. Biri olmayan kapasiteyi varsaymaz, diğeri ürün kriterini düşürmez.
- Mantıksal alanlar: SOUL ürünü; DevOS iş/devam kayıtları; kaynak/karar/kanıt birikimi; çalışma tarifleri/tekrar kullanım kütüphanesi. Bunlar fiziksel dört klasör veya dört kopya değildir.
- Yeni çıktı, güncelleme, devir, yeniden kullanım ve arşiv için olay→sorumlu→kalıcı karşılık→devam koşulu yazıldı. Yalnız dosya üretmek devir değildir; her mesaj ayrı bakım töreni de değildir.
- Talep teslimi/kullanımı, karar/inceleme/yürütme durumları ayrı. Önemli doğruluk/yetki/kayıp kayıt engeliyle kozmetik bakım ayrıldı. Eski sürümlü veya çakışan çıktı current kaydı körlemesine ezmez.
- Arşiv/yedek aktif keşfe karışmamalı; yeniden kullanım sahibini/kapsamını/kanıtını korumalı. Hermes Note30 bu hedefli ayrımları besledi; eski study yorumu yeniden kullanıldı, canlı ürün iddiası üretilmedi.

**Kanıt:** Aynı-assistant kavramsal tasarım ve kaynak karşılaştırması; örnekler canlı test değildir. Koşu, mesaj teslimi, izin, restore veya çakışma mekanizması gösterilmiş değildir.

## Current next responsibility

**Bu tur:** P3 tek taslakta toplandı; kullanıcıya çalışma alanı vurgusunun ve yeni bakım sözleşmesinin somut sonucunu kısa ver. D021'i bütün tasarım kabulü diye sunma.

**Sonraki bütünlüklü P3 işi:** İki eşzamanlı iş, ortak kayıt değişikliği, açık inceleme itirazı ve oturum kesintisini tek uçtan uca senaryoda izlemek. Her adımda yetkili sahip, tüketici, kalıcı durum ve sonraki tetik belirli mi? Yeni rol üretmek veya aynı ayrımı tekrar anlatmak değil, kalan semantik devir açıklığını kapatmak hedeflenir. Maddi açık kalmazsa P3 tasarım kapanışı/P4 gereksinim devri hazırlanır; genel audit döngüsü açılmaz.

P4 teknik/actor seçimi, P5 dosya/mekanizma ve P6 runtime sınaması henüz başlamadı. Kullanıcının yeni değerlendirmesi aynı taslağa işlenir; mevcut üst harita yeniden icat edilmez.

## Fresh-session yolu

AGENT ve gerekli kontroller→[INDEX](INDEX.md)→STATE→[HANDOFF](HANDOFF.md)→[WORK](WORK.md)→[DECISIONS](DECISIONS.md)→[ACTORS](ACTORS.md)→[U002](sources/U002-cloud-plan-and-autonomy.md)→[P1-01](work/P1-01-claude-cloud-environment-map.md)→[P2-01](work/P2-01-named-role-contracts.md)→[P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı konuşmada tam unchanged içerik korunabilir; sonra yalnız aktif sorunun gerekli araştırmasına inilir.

Tarihsel S1/B/Context next ifadeleri current planı yönetmez. P2 ilk tabanı, P3 aday ayrıntıları ve D021 kabul kapsamı birbirine karıştırılmaz. Kısa cevap, küçük çalışma birimi değildir.
