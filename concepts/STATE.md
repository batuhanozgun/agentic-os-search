# Concepts — Güncel çalışma durumu

Tarih: 2026-09-19. Program: araştırma bazında terim/jargon kullanımlarının çıkarımı, ardından bütün çıkarımların ortak değerlendirilmesi. Bu dosya concepts çalışmasının güncel yetki/durum kaynağıdır; araştırmaların kendi STATE dosyalarının yerine geçmez.

## Durum

**PREPARED / PILOT-1-BOUNDED-COMPLETE / B2-REVIEW-COMPLETE / METHOD-v0.2-DRAFT / PILOT-2-NEXT.**

İlk pilot, `context-memory-harness-engineering` paketinin aşağıdaki sekiz dosyalık sürümü üzerinde kaynak-kapsamlı yöntem denemesi olarak kapandı. P1-T1 tam okuma ve ilk kullanım dökümünü, P1-T2 yönelim kontrolü ile paket-içi ilişkileri, P1-T3 kaynak tarafından döküme geri kontrolü, ek kullanımları/niteleyici düzeltmesini ve B2 yöntem değerlendirmesini taşır. Bu kapanış, kaynakların bütün teknik iddialarının doğrulanması, sektördeki terimlerin çözümü veya hatasız sözcük-bazlı envanter sertifikası değildir. Somut aktarım eksiği sonradan bulunursa ilgili kayıt yeniden açılır.

Pilot kullanım çıktıları konuşma içindedir; yeni TERMS/READING dosyası veya kalıcı terim envanteri oluşturulmadı. Repo yalnız mevcut METHOD/PLAN/STATE üzerinden yöntem ve devam durumunu taşır. Yöntem v0.2-draft hâlâ taslaktır; ilk pilotta keşfedilen açıklıklar ikinci pilotta sınanacak, aynı veri bağımsız doğrulama sayılmayacaktır.

| İş | Durum |
|---|---|
| Amaç, kaynak talep ve iki risk | ORIGIN/CHARTER'da korunuyor; değişmedi. |
| Repo hazırlığı | Tamamlandı; SETUP-REVIEW tarihsel kontrol kapsamı geçerli. |
| B1 / birinci pilot | Sekiz dosyalık kaynak kapsamı içinde tamamlandı; P1-T1 + P1-T2 + P1-T3 birlikte çıktı. |
| B2 / ilk yöntem değerlendirmesi | Tamamlandı; sonuç METHOD §7 ve PLAN revizyon R3'te. |
| B3 / ikinci pilot — superpowers | Başlamadı; sıradaki yetkili iş. |
| B4 / ikinci değerlendirme | B3 sonrasında. |
| Kalıcı seri çıkarım | Başlamadı; iki pilot ve değerlendirmelerinden sonra. |
| Bütün çıkarımlardan ortak referans | Başlamadı; kabul edilmiş ortak tanım yok. |

## Amaç ve korunacak ayrımlar

Önce studies araştırmalarının tümü, kendi bağlamlarıyla tam okunarak kullanımları çıkarılır. Sonra çıkarımların tamamı okunarak kapsamlar/alt kavramlar/adlandırmalar değerlendirilir. Seri çıkarımdan önce iki farklı araştırmada sohbet içi yöntem denemesi ve değerlendirmesi yapılır.

Okuma anındaki anlam seçimlerini kullanıcı denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişim görünür olmalı. Aynı terimle aynı anlamı kastettiğimiz varsayılamaz; kullanıcı onayı, kaynak ifadesi ve assistant yorumu teknik doğruluk bakımından ayrı tutulmalı. Her concepts turunda bu iki neden kısa ve açık biçimde hatırlatılır; somut maddi fark varsa belirtilir.

Derinlik sınırı: incelenen araştırmanın kullanım ve ilişki düzenini mümkün olduğunca sadık çıkarmak. Kaynağın açıklamadığı bir genel kavramı ayrıca araştırıp çözmek kapanış koşulu değildir. Açıklanmamış anlamı doğru statüyle kaydetmek ile okunmamış dosya veya atlanmış açıklamayı bırakmak aynı şey değildir. Kullanıcının son kapsam açıklaması kaliteyi düşürme veya ilk pilotu denetimsiz kapatma talebi olarak alınmadı.

## Yetki ve yazma sınırı

Kaynak amaç/yetki: ORIGIN/U01–U05, hazırlık sonrası devam talepleri ve terimlerin bağımsız derin araştırmasına kaymama açıklaması. B1 → B2 → B3 → B4 sırası yürütülür; aynı amacı yeniden onaylatmak gerekmez. Maddi amaç/aşama/kapsam değişikliği ayrıca değerlendirilir.

P1-T1/P1-T2 yalnız STATE'i güncelledi. P1-T3/B2 yalnız mevcut concepts/METHOD.md, PLAN.md ve STATE.md'yi günceller. Yeni dosya, branch, TERMS/READING, ortak tanım veya seri çıkarım başlatılmaz. Foundation, studies paketleri ve kendi META/STATE/INDEX'leri, explorations, publications, AGENT ve agent protokolleri bu pilotta değiştirilmez. Eşzamanlı ECC çalışmasının değişiklikleri korunur.

Batu amaç ve maddi aşama/kapsam değişikliği sahibidir. Assistant kaynak-kapsamlı çıkarım, yöntem değerlendirmesi ve izlenebilir yayını yürütür; kullanıcıyı teknik uzman verifier olarak kullanmaz. Kaynak paketinin araştırma kabul durumu, ürün/mimari/adoption veya genel agent-control yetkisi bu pilotla değişmez.

## Kaynak envanteri ve gerçekten okunan kapsam

Repository: `batuhanozgun/agentic-os-search`. Pilot kaynak snapshot'ı: `ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a`. Paket dizininde sekiz Markdown dosyası; alt dizin/binary ek yok. Tam okuma P1-T1'de aynı konuşmada yapıldı; aşağıdaki kimlikler ve bitişik aralıklar korunur. Aralıkların son istek üst sınırı dosyanın gerçek satır sayısı değildir.

| Paket içi dosya | Blob SHA | P1-T1 tam okuma |
|---|---|---|
| META.md | 55e8d5abe294e9c9b4ae0cd121c1cea3a74b7007 | Tam dosya. |
| STATE.md | 298c0b1c6af6523a1da6b9bb0be018c5579573b2 | Tam dosya. |
| INDEX.md | 72c9756038330a499077fe8a6abebda5f280c79e | Tam dosya. |
| 00-WHY-THIS-RESEARCH.md | be59481ee543f3b1244262664d8e01ac26dec030 | 1–180, 181–360, 361–EOF; son istek üst sınırı 560. |
| 01-CONTEXT-ENGINEERING.md | eed5603460ae9e74d4601b9204bf9502963b9be7 | 1–180, 181–360, 361–540, 541–EOF; son istek üst sınırı 760. |
| 02-AGENT-MEMORY-ENGINEERING.md | 6203b06fe56cad61354e9093d0b404a1ee3592c7 | 1–200, 201–400, 401–600, 601–820, 821–EOF; son istek üst sınırı 1040. |
| 03-HARNESS-ENGINEERING.md | 53f3cbcfbc934155553c9ae6c4ff931126b00876 | 1–200, 201–400, 401–600, 601–820, 821–EOF; son istek üst sınırı 1040. |
| 04-CROSS-LAYER-SYNTHESIS.md | 293ca01ac04952417d9d56b3c79c5f195dd6da35 | 1–200, 201–400, 401–600, 601–820, 821–EOF; son istek üst sınırı 1040. |

Araştırma belgelerinin tarihi 2026-09-03'tür. Eski research/<paket>/ yol yazımları güncel studies konumundan çözüldü; özgün belgeler değiştirilmedi. Dış makaleler, SDK belgeleri ve ai-knowledge-strategies bu pilotta ayrıca tam okunmuş veya güncel teknik doğruluğu teyit edilmiş sayılmaz. Dış kaynak atıfları aktarılmış kullanım statüsündedir. Kod, benchmark veya canlı ürün çalıştırılmadı.

P1-T2'de 04 dosyasının 1–125, 201–400, 401–448 aralıkları ilişki kontrolü için yeniden okundu. P1-T3'te aynı konuşmada erişilebilir P1-T1/P1-T2 çıktıları ve önceki tam kaynak okumaları birlikte değerlendirildi; özellikle aşağıdaki bölümler sabit ref'ten yeniden getirildi:

| Dosya | P1-T3 yeniden okuma aralıkları | Kontrolün rolü |
|---|---|---|
| 00 | 60–180, 361–EOF (istek 560'a kadar) | Başlangıç haritası, terim olgunluğu iddialarının atfı, kaynak adları ve roller. |
| 01 | 105–360, 361–570 | Kaynak sınıfları, retrieval/assembly seçenekleri, niteleyiciler, güvenlik ve değerlendirme boyutları. |
| 02 | 45–300, 405–705, 821–EOF (istek 1040'a kadar) | Yazma/temsil/güncelleme seçenekleri, zaman alanları, tekil kayıt kullanımı, metadata devri, ölçütler ve kaynak adları. |
| 03 | 26–210, 230–400, 445–645 | Tasarım amacı niteleyicisi, alt mekanizmalar, kontrol/aktör rolleri, hata ve değerlendirme grupları. |
| 04 | 625–780 | Karar soruları, mekanizma/sorumluluk ayrımı ve anti-pattern adları; önceki ilişki okumalarıyla birlikte. |

Bu satırlar yeni bir tam-paket okuması iddiası değil, aynı konuşmadaki tam okuma üzerine kaynak taraflı kontroldür. Snapshot'tan yayın öncesi `6f248ca8b42914a1c3a0a50904a72736bd5373d8` main'ine compare, bu pilotun kaynak dosyalarında değişiklik olmadığını gösterdi; farklar concepts/STATE ve ECC çalışmasıyla sınırlıydı. AGENT ve current STATE yeniden okundu; aynı konuşmada tam okunmuş, değişmemiş R01–R09/CHARTER/ORIGIN/INDEX/SETUP bağlamı korundu. METHOD/PLAN güncel main'den tekrar tam okundu.

## P1-T3 — Kapanışın gerekçesi ve sınırı

P1-T1'in ana kullanım kayıtları ve P1-T2'nin kaynak-içi ilişkileri, kaynak başlıkları/listeleri/örnekleriyle karşılaştırıldı. İlk dökümde yalnız sayılan mekanizmalar, niteleyiciler, metadata ve değerlendirme adları bağlamlarıyla tamamlandı. Tekil kayıt, faaliyet, bütün sistem veya aktarım arayüzü gibi farklı göndermeler ayrı tutuldu. Kaynak adları, örnek değerleri ve yalnız soru/listede geçen adlar ayrıntılı tanımmış gibi doldurulmadı.

Kapanış yanıtının önemli değişiklikleri: önceki K07 açıklaması kaynakta kullanılan güvenilir/bounded/recoverable tasarım amacı niteleyicilerine yaklaştırılır; amaç doğrulanmış davranış sayılmaz. K03'ün yaşam döngüsü kullanımı korunurken kaynaktaki tekil memory kaydı kullanımı ayrıca görünür kılınır. H05/H06 dışında D2 §23'teki bilgi/metadata aktarımı anlamındaki handoff ayrıca ayrılır. Bu kontrol notu terim envanteri değildir; asıl kullanım kayıtları P1-T3 konuşma yanıtındadır.

Kaynak-içi gerilimler açık sonuç olarak korunur: harness faaliyeti/nesnesi kapsamı; iç/dış/parametrik bellek sınırı; canonical state'in kalıcılık ve otorite açısından farklı konumu; tarihli Development OS adının bugünkü ürün durumuna taşınmaması. Bunlar çözülmüş ontolojik kararlar değildir ve bağımsız terim araştırmasına geçme gerekçesi yapılmaz.

B1 kapanışı için önceki METHOD §5 esas alındı: envanter/tam okuma görünür; kaynak sürümü sabit ve değişiklik kontrolü yapılmış; kullanım/ilişki kayıtları kaynaklarına bağlı; bulunan maddi aktarım eksikleri ve niteleyici farkı açıklanmış; okunamamış paket dosyası yok; kaynakta açıklanmayan anlamlar tanımlanmamış olarak korunuyor. Birinci pilot için açık kalan somut aktarım işi bırakılmadı. Bu, bütün sözcükler için tanım bulunduğu veya aynı assistant'ın kontrolünün bütün olası hataları dışladığı iddiası değildir.

## B2 — İlk yöntem değerlendirmesi

Tam okuma, araştırma-bazlı sınır, kaynak–yorum ayrımı, yorum değişimi izi ve iki aşama sırası korundu. Yöntem denemesi kaynak tarafına dönüşün gerçekten ek/ayrılmış kullanım ve niteleyici farkı yakaladığını gösterdi; kontrol sadece önceki metni onaylama değildi. Ancak bu aynı assistant'ın source-side cross-check'idir; bağımsız aktör veya formal recall benchmark'ı değildir.

V0.2-draft açıklıkları METHOD §7'dedir: kullanım ve ilişki görünümünün birlikte tutulması; konuşan/kaynak rolü ile yeni açıklamanın statüsünün ayrılması; faaliyetin nesneyle ve tasarım amacının garantiyle karışmaması; kaynak bölümünden döküme sonlu kapsam hesabı; kaynak belirsizliğinin yeni genel araştırma borcu olmaması. PLAN/R3 ikinci pilotun bu açıklıkları sınamasını taşır. Revize yöntem aynı ilk pilot tarafından geriye dönük bağımsız doğrulanmış sayılmaz.

Açık sınırlar: gerçek yeni-oturum davranış testi yapılmadı; pilot çıktıları chat-only olduğundan bağımsız yeni oturumda erişim ayrıca doğrulanmalı; dış kaynakların teknik doğruluğu bu çalışmanın sonucu değil. Kullanıcının olumlu değerlendirmesi bunların yerine kullanılmadı. Yeni dosya şeması veya kavram ontolojisi dondurulmadı.

## Current work ve next authorised work

**Tamamlanan:** repo hazırlığı; ilk kaynak-kapsamlı pilot B1 ve ilk yöntem değerlendirmesi B2. Eski P1-T1/P1-T2 checkpoint'lerindeki B1-açık ve B2-yapılmadı durumları tarihseldir; bu STATE'in güncel durumunu ikame etmez.

**Sıradaki yetkili iş PLAN/B3:** `research/studies/superpowers` üzerinde ikinci konuşma içi pilot. Güncel main/dosya envanteri ve paketin current META/STATE/INDEX'inden başla; gerekli kaynakları tam okumayla devral. İlk pilotun terim listesini veya ilişki şemasını Superpowers'a zorla uygulama. Yöntem v0.2-draft sınanır; kaynağın kendi kullanımları ve ilişkileri çıkarılır. Önceki hazırlıkta Superpowers META'sının görülmesi B3 okuması/tamamlanması sayılmaz.

B3 tam okuma ve çıkarım için turlara yayılabilir. Sonra B4, kalıcı düzenin kesinleştirilmesi ve B5–B7 seri çıkarım işleri gelir. B8 ortak referans, bütün araştırmaların çıkarımı bitmeden başlamaz. Bu kapanış turunda B3 başlatılmadı; yeni kapsam veya mimari işi yoktur.

## Konuşma çıktısının devralma sınırı

Pilotun kullanım kayıtlarının taşıyıcısı P1-T1, P1-T2 ve P1-T3 görünür yanıtlarıdır. Bu STATE bir terim arşivi veya yanıt teslim/alım makbuzu değildir. Yeni oturum bu üç çıktıya erişebiliyorsa tamamını okur; yalnız buradaki özeti onların yerine koymaz. Erişilemiyorsa hafızadan liste/tanım yeniden kurulmaz. İlk pilotun belgelenmiş yöntem dersleriyle B3'e geçilebilir; ancak ilk pilot terimlerini yeniden kullanmak veya kalıcı seri kayda almak gerekirse sabit kaynaklardan yeniden kaynak-kontrollü çıkarım yapılır ve bunun yeniden üretim olduğu belirtilir. B1 sırf önceki sohbet görünmüyor diye yapılmamış sayılmaz; önceki aktörün okuması da yeni aktörün okuması sayılmaz.

Yeni oturum yolu: AGENT ve tetiklenen protokoller → concepts/INDEX → bu STATE → CHARTER → ORIGIN → METHOD → PLAN → SETUP-REVIEW → B3'ün güncel araştırma girişleri ve gerçek dosya envanteri. Bunlar yeni oturumda tam okunur. Aynı konuşmada değişmemiş tam okumalar mekanik olarak tekrarlanmaz. Zorunlu kaynak/kontrol erişilemezse eksik bilgi uydurulmaz.

## Yayın ve önceki checkpoint'ler

Hazırlık başlangıcı `c7e5d02a5be15b4b938c2796e3c274b04aa4bca4`; hazırlık incelemesi `0ab0a7759fba6c680cd4ab0cae5ba21d001b4be6`; hazırlık kapanışı/pilot kaynak ref'i `ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a`. SETUP-REVIEW'in kapsam dışı iki satır düzeltmesi ve statik kontrol sınırı korunur.

P1-T1 STATE checkpoint'i `6031f8c5a044ebbbe2959b8483e432535f631171`; P1-T2 `ca8be1b5f3fad60905a13ef8556d26af01b6643d`. Ayrıntılı eski ilerleme/yönelim kayıtları bu commitlerdeki concepts/STATE.md'den geri alınabilir; tarihsel aşama yetkisi değildir. Bu kapanış mevcut kaynak envanterini ve açık epistemik sınırları yukarıda korur.

P1-T3 yayın öncesi main checkpoint'i `6f248ca8b42914a1c3a0a50904a72736bd5373d8`; eşzamanlı ECC değişiklikleri korunur. METHOD v0.2 commit'i `839e760a2e306e0011826501f4580b841ecc2f04`; PLAN v0.2 commit'i `67351f0808dd8175d3297f03258d49379a23ad56`. Bu STATE yayını onları takip eder. Yayın doğrulaması dosyaların geri okunması ve kendi commitlerinin fark/kapsam kontrolüdür; gerçek yeni-oturum veya bağımsız araştırma doğrulaması değildir.
