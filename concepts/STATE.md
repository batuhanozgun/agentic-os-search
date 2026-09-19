# Concepts — Güncel çalışma durumu

Tarih: 2026-09-19. Program: araştırma bazında terim/jargon kullanımlarının çıkarımı, ardından bütün çıkarımların ortak değerlendirilmesi. Bu dosya concepts çalışmasının güncel yetki/durum kaynağıdır; araştırmaların kendi STATE dosyalarının yerine geçmez.

## Durum

**PREPARATION-IN-PROGRESS / METHOD-DRAFT / PILOTS-NOT-STARTED.**

Amaç ve iki riskin ele alınışı kullanıcı tarafından onaylandı. Son kullanıcı talebi repo hazırlığının şimdi uygulanmasını yetkilendirdi. ORIGIN.md, CHARTER.md, METHOD.md ve PLAN.md oluşturuldu; giriş/denetim dosyaları ve eski yönlendirmelerin uyumlandırılması henüz tamamlanma kontrolünde. Bu checkpoint hazırlığın bitmiş olduğu iddiası değildir.

| İş | Durum |
|---|---|
| Bu konuşmanın amaç/yetki/kısıtlarının geri kazanılması | Yapıldı; ORIGIN ve CHARTER'a yansıtıldı. |
| İki taslak plan ve iki riskle yöntem revizyonu | Hazır; v0.1-draft, pilotlarla sınanmadı. |
| Eski etkin concepts yönlendirmelerinin temizliği | Yayın/verification sürüyor. |
| Birinci konuşma içi deneme | Başlamadı. |
| İkinci konuşma içi deneme | Başlamadı; birinci deneme/değerlendirme sonrasında. |
| Kalıcı araştırma bazlı terim envanterleri | Yok; oluşturulmadı. |
| Bütün çıkarımlardan ortak tanım/ref­erans | Başlamadı; kabul edilmiş tanım yok. |

## Amaç ve korunacak ayrımlar

Önce studies araştırmalarının tümü, kendi bağlamlarıyla tam okunarak kullanımları çıkarılır. Sonra çıkarımların tamamı okunarak kapsamlar/alt kavramlar/adlandırmalar değerlendirilir. Seri çıkarımdan önce iki farklı araştırmada sohbet içi yöntem denemesi ve değerlendirmesi yapılır.

Okuma anındaki anlam seçimlerini kullanıcı denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişim görünür olmalı. Aynı terimle aynı anlamı kastettiğimiz varsayılamaz; kullanıcı onayı, kaynak ifadesi ve assistant yorumu teknik doğruluk bakımından ayrı tutulmalı. Her concepts turunda bu iki neden kısa ve açık biçimde hatırlatılır; somut maddi fark varsa belirtilir.

## Yetki ve sınırlar

Güncel kaynak: ORIGIN.md/U05, önceki U01–U04 ve onaylanmış amaçla birlikte. Hazırlık dosyaları ve eski concepts yönlendirmelerinin sınırlı temizliği yetkili. Bu, başlangıçtaki yazmama sınırının hazırlık için değiştirilmesidir; yapılmamış pilotlar veya ortak tanımlar onaylanmış değildir.

Bu uygulamanın yazma kapsamı: concepts/**; README.md; research/INDEX.md; research/studies/INDEX.md, CATALOG.md, PACKAGE-CONTRACT.md içindeki concepts bölümleri; AGENT.md R09 tetikleyicisi ve agent/protocols/candidate-research-library.md içindeki concepts bölümü. Genel R01–R08, Foundation, studies paket araştırmaları, explorations ve publications korunur. Kaynaklarda geçen concepts sözcükleri topluca silinmez. Yeni branch oluşturulmaz.

Batu amaç ve maddi aşama/kapsam değişikliği sahibidir. Assistant onaylı kapsamda okuma, kaynak doğruluğuna bağlı çıkarım, yöntem değerlendirmesi ve izlenebilir yayını yürütür; kullanıcıyı teknik uzman verifier olarak kullanmaz. Mimari/uygulama/adoption kararı bu çalışmanın yetkisi değildir.

## Current work ve next authorised work

**Şimdi:** hazırlık dosyalarını ve etkin yönlendirmeleri tamamla, değişen kontrol dosyalarını yeniden oku, bağlantı/diff/kapsam kontrolünü yap ve hazırlığın gerçek durumunu kaydet.

**Hazırlık doğrulandıktan sonra:** PLAN/B1, research/studies/context-memory-harness-engineering üzerinde konuşma içi ilk deneme. Güncel paketin gerçek dosya envanteri ve gerekli giriş okumalarıyla başla; önceki sohbetin META okumasını tam araştırma okuması sayma. İkinci deneme superpowers; birinci denemenin yöntem değerlendirmesi önce gelir.

Mevcut hazırlık okumasında study META/INDEX/CATALOG görülmüş olması pilotun başlaması veya terim çıkarım kapsamı değildir. Tam paket/dosya okuma envanteri henüz oluşturulmadı; tam araştırma okundu iddiası yoktur.

## Yeni oturum yolu

AGENT.md ve tetiklenen protokoller → concepts/INDEX.md → bu STATE → CHARTER.md → ORIGIN.md → METHOD.md → PLAN.md → SETUP-REVIEW.md → yalnız sıradaki araştırmanın current META/STATE/INDEX ve gerçek dosya envanteri.

Bu giriş dosyaları yeni oturumda tam okunur. Aynı oturumda ilgili dosyalar değişmemişse yeniden tam okuma mekanik tekrar değildir; maddi değişiklikte ilgili canonical içerik geri kazanılır. Arşivlenmiş eski concepts kararları devam noktası değildir. Kaynak veya zorunlu kontrol eksikse bilgi uydurulmaz.

## Yayın bağlamı

Başlangıç main: c7e5d02a5be15b4b938c2796e3c274b04aa4bca4. Hazırlık mevcut main üzerinde sıralı, SHA kontrollü işlemlerle yapılıyor. Ayrıntılı doğrulama SETUP-REVIEW.md'de kapanacak. Kesinti halinde bu dosyadaki IN-PROGRESS durumunu koru; var olan birkaç dosyayı tamamlanmış hazırlık sanma.
