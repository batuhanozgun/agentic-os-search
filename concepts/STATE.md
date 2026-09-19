# Concepts — Güncel çalışma durumu

Tarih: 2026-09-19. Program: araştırma bazında terim/jargon kullanımlarının çıkarımı, ardından bütün çıkarımların ortak değerlendirilmesi. Bu dosya concepts çalışmasının güncel yetki/durum kaynağıdır; araştırmaların kendi STATE dosyalarının yerine geçmez.

## Durum

**PREPARED / METHOD-DRAFT / PILOT-1-NEXT.**

Repo hazırlığı main üzerinde tamamlandı. Kaynak talep, amaç, iki riskin nedenleri, iki taslak plan, taslak yöntem ve yeni oturum yolu kaydedildi; eski etkin concepts yönlendirmeleri yenilendi. Yedi yeni dosya geri okundu, mevcut dosyaların diff'leri ve kapsam kontrol edildi. Bu, statik hazırlık incelemesidir; gerçek yeni-oturum davranış testi veya yöntem doğrulaması değildir. Ayrıntı SETUP-REVIEW.md'de.

| İş | Durum |
|---|---|
| Bu konuşmanın amaç/yetki/kısıtlarının geri kazanılması | Yapıldı; ORIGIN ve CHARTER'a yansıtıldı. |
| İki taslak plan ve iki riskle yöntem revizyonu | Hazır; v0.1-draft, pilotlarla sınanmadı. |
| Eski etkin concepts yönlendirmelerinin temizliği ve yeni giriş yolu | Hazır; incelenen etkin yüzeylerde yeni kapsam/aşama sırası tutarlı. |
| Birinci konuşma içi deneme | Başlamadı; sıradaki yetkili iş. |
| İkinci konuşma içi deneme | Başlamadı; birinci deneme/değerlendirme sonrasında. |
| Kalıcı araştırma bazlı terim envanterleri | Yok; oluşturulmadı. |
| Bütün çıkarımlardan ortak tanım/referans | Başlamadı; kabul edilmiş tanım yok. |

## Amaç ve korunacak ayrımlar

Önce studies araştırmalarının tümü, kendi bağlamlarıyla tam okunarak kullanımları çıkarılır. Sonra çıkarımların tamamı okunarak kapsamlar/alt kavramlar/adlandırmalar değerlendirilir. Seri çıkarımdan önce iki farklı araştırmada sohbet içi yöntem denemesi ve değerlendirmesi yapılır.

Okuma anındaki anlam seçimlerini kullanıcı denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişim görünür olmalı. Aynı terimle aynı anlamı kastettiğimiz varsayılamaz; kullanıcı onayı, kaynak ifadesi ve assistant yorumu teknik doğruluk bakımından ayrı tutulmalı. Her concepts turunda bu iki neden kısa ve açık biçimde hatırlatılır; somut maddi fark varsa belirtilir.

## Yetki ve sınırlar

Güncel kaynak: ORIGIN.md/U05, önceki U01–U04 ve onaylanmış amaçla birlikte. Son kullanıcı mesajı hazırlığın şimdi yazılmasını ve onaylı planın uygulanmasını yetkilendirdi. Bu, başlangıçtaki yazmama sınırının hazırlık için değiştirilmesidir; yapılmamış pilotlar veya ortak tanımlar onaylanmış değildir. Pilot çıktıları konuşmada gösterilir; sırf hazırlık tamamlandı diye kalıcı TERMS envanteri başlatılmaz.

Hazırlık uygulamasının gerçekleşen yazma kapsamı: concepts altında yedi dosya; README.md; research/INDEX.md; research/studies/INDEX.md, CATALOG.md, PACKAGE-CONTRACT.md içindeki concepts bölümleri; AGENT.md R09 tetikleyicisi ve agent/protocols/candidate-research-library.md içindeki concepts bölümü. Diğer sekiz protokol, Foundation, studies paket araştırmaları, explorations ve publications korundu. Kaynaklarda geçen concepts sözcükleri topluca silinmedi. Yeni branch oluşturulmadı.

Sonraki concepts işi, PLAN sırası ve METHOD sınırları içinde okuma, konuşma içi denemeler, yöntem değerlendirmesi ve mevcut durum/yöntem kayıtlarının güncellenmesidir. Hazırlıkta kontrol dosyalarının değiştirilmiş olması sonraki turlara sınırsız agent-control mutation yetkisi vermez. Genel kontrol değişiklikleri AGENT Mutation Rule'a tabidir.

Batu amaç ve maddi aşama/kapsam değişikliği sahibidir. Assistant onaylı kapsamda kaynağa dayalı, belirsizlikleri korunan kullanım çıkarımını, yöntem değerlendirmesini ve izlenebilir yayını yürütür; kullanıcıyı teknik uzman verifier olarak kullanmaz. Mimari/uygulama/adoption kararı bu çalışmanın yetkisi değildir.

## Current work ve next authorised work

**Tamamlanan iş:** yeni oturumların aynı amaç ve bakış açısıyla devralabilmesi için repo hazırlığı ve sınırlı statik yayın kontrolü. Kaynak değişmedikçe hazırlığı yeniden yapılacak iş sanma.

**Sıradaki yetkili iş:** PLAN/B1, research/studies/context-memory-harness-engineering üzerinde konuşma içi ilk deneme. Güncel paketin gerçek dosya envanteri ve gerekli META/STATE/INDEX okumalarıyla başla; ardından bütün araştırma dosyalarını tam okuyarak kullanımları sohbet içinde çıkar. Bir tura sığmazsa tam devam noktasıyla sürdür. Önceki sohbetin META okumasını tam araştırma okuması veya pilot sonucu sayma.

İlk pilotun ardından yöntem değerlendirilecek; sonra superpowers üzerinde ikinci pilot ve yeniden yöntem değerlendirmesi gelecek. Bütün araştırmalardan çıkarım tamamlanmadan ortak tanım aşamasına geçilmeyecek. Bu sırayı yürütmek için daha önce verilmiş amacı tekrar onaylatmak gerekmez; maddi amaç/aşama/kapsam değişikliği ayrıca değerlendirilir.

Hazırlık sırasında study META/INDEX/CATALOG görülmüş olması pilotun başlaması veya terim çıkarım kapsamı değildir. Tam paket/dosya okuma envanteri henüz oluşturulmadı; tam araştırma okundu iddiası yoktur. Henüz pilot sonucu veya kalıcı terim kaydı bulunmuyor.

## Yeni oturum yolu

AGENT.md ve tetiklenen protokoller → concepts/INDEX.md → bu STATE → CHARTER.md → ORIGIN.md → METHOD.md → PLAN.md → SETUP-REVIEW.md → sıradaki araştırmanın current META/STATE/INDEX ve gerçek dosya envanteri.

Bu giriş dosyaları yeni oturumda tam okunur. Aynı oturumda tam okunmuş ve değişmemiş içeriklerin yeniden okunması mekanik bir zorunluluk değildir; maddi değişiklikte ilgili canonical içerik geri kazanılır. Arşivlenmiş eski concepts kararları devam noktası değildir. Zorunlu kontrol veya gerekli kaynak erişilemiyorsa eksik bilgi uydurulmaz.

## Yayın ve doğrulama bağlamı

Başlangıç main: c7e5d02a5be15b4b938c2796e3c274b04aa4bca4. İncelenen içerik checkpoint'i: 2a5a146c54739116799a00e5b442908d3870cc73. Karşılaştırmada yalnız hedeflenen 14 dosya değişti. Statik inceleme kapanışı: 0ab0a7759fba6c680cd4ab0cae5ba21d001b4be6; bu STATE kapanışı onu takip eder.

İki istenmeyen kapsam dışı satır farkı diff incelemesinde yakalandı ve geri alındı; kontrol kaydı SETUP-REVIEW.md'dedir. Değişen AGENT/R09 canonical içerikleri tekrar tam okundu. Bu sonuç bütün repository baytlarının anlamsal tarandığı, tarihsel izlerin silindiği veya sonraki oturumlarda drift'in imkânsız olduğu iddiası değildir. Yöntem başarısı henüz iki pilotta sınanacaktır.
