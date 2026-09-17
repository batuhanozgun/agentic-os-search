# ECC — STATE

**Updated:** 2026-09-17
**Current unit:** U00 — araştırma yöntemi, uyarlanabilir plan ve kalıcı çalışma paketi
**Work status:** U00 COMPLETE / PUBLISHED; yöntem/plan ve katalog/index yolları main'e yayımlandı, temel girişler ve diff kapsamı geri kontrol edildi. Yöntem/plan kullanıcı değerlendirmesine sunuluyor. [PUBLICATION](PUBLICATION.md) exact commit, eşzamanlılık ve doğrulama sınırlarını taşır.
**Study status:** METHOD / PLAN PREPARED; U01 ve derin kaynak araştırması NOT STARTED
**Method / plan:** v0.1 / v0.1
**Pinned target:** affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a

## Latest authorized goal

Kullanıcı ECC'nin studies'e alınmasını uygun karşıladı; repo merkezli, turlar/oturumlar boyunca odağını koruyan bir disiplin istedi. Bu tur için açık teslimat: önce metodolojiyi ve değişebilir planı kurmak, araştırma ile yöntemin gelişimini gelecekte kullanılabilir bir örnek olarak repoya yansıtmak.

Bu çalışma yalnız bir planın konuşmada sunulmasıyla kapanmaz; package ve keşif yolları yayımlanmalı ve geri okunmalıdır. Ancak plan hazırlığından derin ECC incelemesine bu tur sessizce geçilmez.

- **Next logical work:** U01 — pinned corpus sınırı, dağıtım/yürütme haritası ve ilk mekanizma diliminin seçimi.
- **Next authorized work after this delivery:** kullanıcının yönteme geri bildirimi veya devam yönü; bir sonraki açık devam isteği mevcut sınırlar içinde U01'e giriş olur.
- **Not authorized:** ECC kurulumu, kullanıcı ortamı/config değişikliği, credential/ücretli model kullanımı, upstream mutation, SOUL/Development OS tasarım veya implementasyonu, agent-control değişikliği.

## What is established, and what is not

Established: exact upstream main ref'i ve seçili kaynak kimlikleri doğrulandı; önceki studies yöntemleri okundu; kaynak-temelli ve iki-döngülü yöntem/plan oluşturuldu. [SOURCE-LEDGER](SOURCE-LEDGER.md) okuma kapsamını taşır.

Open: ECC-native sistem ayrıştırması, gerçek entrypoint/call graph, adapter eşdeğerliği, kurulum sahipliği, uçtan uca çalışma, memory/learning, güvenlik ve etkililik. Ön taramadaki olumlu değerlendirme bunları kanıtlamaz. Yeni ECC runtime testi, live-host/model koşusu veya kurulum yapılmadı.

Yöntem v0.1 önerilmiş/yerel olarak değerlendirilmiştir; odağı koruduğu veya cold-start davranışını güvenceye aldığı henüz gösterilmemiştir. [METHOD-REVIEW](METHOD-REVIEW.md) bu ayrımı korur.

## Canonical responsibilities

Batu amaç, kapsam, kullanıcı değerlendirmesi ve maddi aşama değişikliğinin sahibi. Assistant mevcut yetki içinde kaynak okuma, analitik sentez, yöntem/plan revizyon gerekçesi ve doğru yayın/devralma kaydından sorumlu. Plan sıralaması veya soru bölme/birleştirme gerekçeli biçimde uyarlanabilir; bu, yeni bir proje aşamasını kendiliğinden yetkilendirmez.

Yazma alanı `research/studies/ecc/**` ve yalnız ECC'yi keşfettiren `research/studies/CATALOG.md` / `INDEX.md` ekleridir. Diğer studies, Foundation, soul-context, explorations ve control dosyaları korunur.

## Cold-start — full entry reads, then selective source recovery

Canonical AGENT/protocol bootstrap sonrasında:

1. Bu [STATE](STATE.md), [INDEX](INDEX.md), [META](META.md), [00-WHY-THIS-RESEARCH](00-WHY-THIS-RESEARCH.md).
2. Güncel [METHOD](METHOD.md), [PLAN](PLAN.md), [QUESTIONS](QUESTIONS.md).
3. [SOURCE-LEDGER](SOURCE-LEDGER.md) entry/freshness kısmı ve seçilen birimin kayıtları; U00'da dosya küçüktür, tamamı okunur.
4. [RESEARCH-LOG](RESEARCH-LOG.md) son birim ve [METHOD-REVIEW](METHOD-REVIEW.md) güncel yöntem değişiklikleri. U00'da ikisi tam okunur; büyüdüğünde son durumdan ilgili eski karara geri gidilir.
5. İlgili mekanizma notu, alt-sentez ve yük taşıyan pinned kaynaklar. Özet exact iddiayı taşımıyorsa asıl kaynağa dönülür. [PUBLICATION](PUBLICATION.md) gerçek yayın/geri-okuma durumunu ve korunmuş eşzamanlı Superpowers güncellemesini gösterir; eski unreferenced commit bekleyen upload/merge işi değildir.

Yeni oturum kısa biçimde devralınan soru, kapsam/yetki, son bulgu ve açıklığı belirtir; kullanıcıdan projeyi yeniden anlatması istenmez. Mandatory giriş erişimi/tutarlılığı eksikse etkilenen işe devam edilmez.

## First continuation boundary

U01 yalnız dış hedefin sınırını ve doğal ailelerini kuracak; ilk önce mevcut yedi ön-tarama başlığını doğrulamaya çalışmayacak. Tam tree/manifest/distribution keşfinden sonra bir source→materialization→host consumption dilimi seçilecek. PLAN'daki sıra bağlayıcı takvim değildir. U01 dönüşü envanter, bounded orientation bulgusu, kaynak kapsamı ve revize edilmiş sıradaki birimdir; tüm repo anlaşılmış sayılmaz.

## Current environment and project context

GitHub bağlantısıyla canonical okuma ve repo nesnesi/yayın araçları kullanılabilir. Bu tur container'dan doğrudan GitHub'a yardımcı erişim denemesi DNS çözümlemesinde başarısız oldu; bu GitHub connector'ın başarısızlığı değildir. Yerel ECC checkout/runtime hazır varsayılmaz; gelecekte gerekiyorsa capability tekrar kontrol edilir.

Foundation'ın 2026-09-17 STATE'i genel derinleştirmede yeterli durma noktasını, somut hedefte seçici kullanım ve yeniden açılabilirliği kaydeder; bu ECC çalışması Foundation veya Development OS'u devralmaz. Geç projeksiyonda o günün durumu yeniden okunur.
