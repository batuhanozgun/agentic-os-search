# Concepts — Güncel çalışma durumu

Tarih: 2026-09-19. Program: araştırma bazında terim/jargon kullanımlarının çıkarımı, ardından bütün çıkarımların ortak değerlendirilmesi. Bu dosya concepts çalışmasının güncel yetki/durum kaynağıdır; araştırmaların kendi STATE dosyalarının yerine geçmez.

## Durum

**PREPARED / PILOT-1-ACTIVE / PACKAGE-FULL-READ / EXTRACTION-PARTIAL / METHOD-DRAFT.**

Repo hazırlığı tamamlandı; tekrar yapılacak iş değildir. Kullanıcının hazırlık kapanışından sonraki “Anlaştık. Devam et.” mesajıyla PLAN/B1'in ilk konuşma içi turu yürütüldü. `context-memory-harness-engineering` paketinin gerçek dosya envanteri çıkarıldı ve sekiz mevcut Markdown dosyasının tamamı okundu. Bu, bağlantı verilen bütün dış kaynakların veya başka araştırma paketlerinin okunduğu anlamına gelmez. İlk bağlamlı kullanım dökümünün taşıyıcısı bu sohbetin P1-T1 cevabıdır; kalıcı terim dosyası oluşturulmadı. Tam okuma tamamlandı, fakat kullanım dökümünün eksiksizlik kontrolü ve pilot kapanışı tamamlanmadı.

| İş | Durum |
|---|---|
| Amaç/yetki/kısıtların ve iki riskin korunması | ORIGIN ve CHARTER'da; değişmedi. |
| Repo hazırlığı ve eski etkin yönlendirmelerin temizliği | Tamamlandı; SETUP-REVIEW kapsam ve sınırları geçerli. |
| İki taslak plan ve yöntem | v0.1-draft; METHOD ve PLAN bu tur değiştirilmedi. |
| Birinci pilot: gerçek paket envanteri ve tam okuma | Sekiz dosyanın tamamı okundu; aşağıdaki kaynak sürümüyle sınırlı. |
| Birinci pilot: bağlamlı kullanım çıkarımı | İlk konuşma içi döküm; eksiksizlik ve kullanım-bazlı kapsam kontrolü açık. |
| Birinci pilotun tamamlanması ve B2 yöntem değerlendirmesi | Tamamlanmadı; okuma bitişi pilot kapanışı değildir. |
| İkinci pilot / superpowers | Başlamadı; B1 ve B2'den sonra. |
| Kalıcı araştırma bazlı terim envanterleri | Yok; oluşturulmadı. |
| Bütün çıkarımlardan ortak tanım/referans | Başlamadı; kabul edilmiş ortak tanım yok. |

## Amaç ve korunacak ayrımlar

Önce studies araştırmalarının tümü, kendi bağlamlarıyla tam okunarak kullanımları çıkarılır. Sonra çıkarımların tamamı okunarak kapsamlar/alt kavramlar/adlandırmalar değerlendirilir. Seri çıkarımdan önce iki farklı araştırmada sohbet içi yöntem denemesi ve değerlendirmesi yapılır.

Okuma anındaki anlam seçimlerini kullanıcı denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişim görünür olmalı. Aynı terimle aynı anlamı kastettiğimiz varsayılamaz; kullanıcı onayı, kaynak ifadesi ve assistant yorumu teknik doğruluk bakımından ayrı tutulmalı. Her concepts turunda bu iki neden kısa ve açık biçimde hatırlatılır; somut maddi fark varsa belirtilir.

## Yetki ve sınırlar

Kaynak amaç/yetki: ORIGIN.md/U01–U05 ve hazırlık kapanışından sonraki devam talebi. Pilot çıktıları konuşmada gösterilir; hazırlığın veya tam okumanın tamamlanması kalıcı TERMS envanteri ya da erken ortak referans oluşturma izni değildir. Mevcut durum/yöntem kayıtlarının güncellenmesi onaylı plan içindedir.

Hazırlığın tarihsel yazma kapsamı: concepts altında yedi dosya; README.md; research/INDEX.md; research/studies/INDEX.md, CATALOG.md, PACKAGE-CONTRACT.md içindeki concepts bölümleri; AGENT.md R09 tetikleyicisi ve agent/protocols/candidate-research-library.md içindeki concepts bölümü. Bu önceki sınırlı değişiklikler sonraki turlara genel agent-control mutation yetkisi vermez. AGENT Mutation Rule geçerlidir.

P1-T1 turunun repo yazma kapsamı yalnız bu STATE dosyasıdır. Foundation, özgün studies paketleri ve onların META/STATE/INDEX'i, explorations, publications, kontrol dosyaları ve diğer concepts dosyaları değiştirilmez. Yeni dosya, branch, kalıcı TERMS/READING kaydı veya ortak tanım oluşturulmaz. Kaynak paketinin kendi araştırma tamamlanma/onay durumu bu pilotla değişmez.

Batu amaç ve maddi aşama/kapsam değişikliği sahibidir. Assistant onaylı kapsamda kaynağa dayalı, belirsizlikleri korunan kullanım çıkarımını, yöntem değerlendirmesini ve izlenebilir yayını yürütür; kullanıcıyı teknik uzman verifier olarak kullanmaz. Mimari/uygulama/adoption kararı bu çalışmanın yetkisi değildir.

## P1-T1 — Gerçek okuma kapsamı

Repository: `batuhanozgun/agentic-os-search`.

Okuma snapshot'ı: `ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a` (tur başlangıcındaki main). Kontroller ve hazırlık girişleri aynı konuşmada tam okunmuş sürümlerdi; AGENT ve bu STATE güncel main'den tekrar tam okundu. Başlangıç main hazırlık kapanışıyla aynıydı. Pilot dosyaları aşağıdaki sabit ref üzerinden getirildi; yazma öncesi compare sonucu main ile snapshot arasında fark olmadığını gösterdi.

Paket dizininin GitHub contents envanteri sekiz dosya döndürdü; alt dizin veya binary ek yoktu. Uzun belgeler aşağıdaki bitişik aralıklarla getirildi; final parça dosya sonuna kadar okundu. Aralık üst sınırını dosyanın gerçek satır sayısı gibi yorumlama.

| Paket içi dosya | Blob SHA | Gerçek okuma |
|---|---|---|
| META.md | 55e8d5abe294e9c9b4ae0cd121c1cea3a74b7007 | Tam dosya. |
| STATE.md | 298c0b1c6af6523a1da6b9bb0be018c5579573b2 | Tam dosya. |
| INDEX.md | 72c9756038330a499077fe8a6abebda5f280c79e | Tam dosya. |
| 00-WHY-THIS-RESEARCH.md | be59481ee543f3b1244262664d8e01ac26dec030 | 1–180, 181–360, 361–EOF; son istek üst sınırı 560. |
| 01-CONTEXT-ENGINEERING.md | eed5603460ae9e74d4601b9204bf9502963b9be7 | 1–180, 181–360, 361–540, 541–EOF; son istek üst sınırı 760. |
| 02-AGENT-MEMORY-ENGINEERING.md | 6203b06fe56cad61354e9093d0b404a1ee3592c7 | 1–200, 201–400, 401–600, 601–820, 821–EOF; son istek üst sınırı 1040. |
| 03-HARNESS-ENGINEERING.md | 53f3cbcfbc934155553c9ae6c4ff931126b00876 | 1–200, 201–400, 401–600, 601–820, 821–EOF; son istek üst sınırı 1040. |
| 04-CROSS-LAYER-SYNTHESIS.md | 293ca01ac04952417d9d56b3c79c5f195dd6da35 | 1–200, 201–400, 401–600, 601–820, 821–EOF; son istek üst sınırı 1040. |

Kaynak belgelerin araştırma tarihi 2026-09-03; META daha sonraki kütüphane yerleştirmesini yansıtabilir. Belgelerdeki eski `research/<paket>/` yol yazımları güncel studies yolu üzerinden çözüldü; kaynak dosyalar düzeltilmedi. Dış kaynak bağlantılarının varlığı, kaynakların bu tur yeniden açıldığı/teyit edildiği anlamına gelmez. `ai-knowledge-strategies` ayrı paket olarak bu pilotun sekiz dosyasına eklenmedi; ona yapılan atıflar aktarılan önceki araştırma olarak tutuldu. Kod, benchmark, ürün veya canlı sistem çalıştırılmadı.

## P1-T1 — Yorum ve yöntem kontrolünün açık noktaları

Bu bölüm terim envanteri veya ortak tanım değildir; sonraki turun hangi yorum/coverage sorunlarını devralacağını kaydeder.

- Birincil kaynağa atfedilen kullanım, önceki araştırmanın genişletilmiş çalışma tanımı ve bu pilotun açıklaması ayrı tutuldu. Asıl kaynak bu tur okunmadığında atıf birinci-el doğrulama gibi gösterilmedi; kaynak belgenin kendi “high confidence” etiketleri extractor güveni olarak devralınmadı.
- Aynı etiketin mühendislik faaliyeti, çalışma zamanı nesnesi veya daha geniş operasyonel düzen için kullanılması dikkat gerektiriyor. Özellikle 03 §2 ile §31 arasındaki kapsam/nesne farkı sonraki kontrolde korunmalı; tek bir temiz tanıma indirgenmemeli.
- 02 §3'teki geniş iç/dış bellek kapsamı, §13'teki parametric adaptation ayrımı ve §5.5/§6/§21–22'deki canonical state konumu aynı sınıflandırma eksenine zorlanmamalı. Bunlar bu turda çözülmüş ontolojik çelişki veya yeni ortak karar değildir.
- Paket içindeki tarihli Development OS kullanımı, o tarihteki repository-control yaklaşımına da gönderme yapıyor. Bu anlatım bugünkü Development OS ürününün kurulmuş olduğu iddiasına çevrilmemeli.
- 01/02/03'teki kullanım ile 04 ve giriş dosyalarındaki tekrarı bağımsız kanıt olarak sayma. Aynı ifadeyi yeniden görmek yeni bir bağımsız doğrulama değildir.
- Genel adlar, yalnız listelenmiş alt mekanizmalar, örneklerde geçen API/alan adları ve source-ledger içindeki adlandırmalar henüz kullanım-bazlı eksiksizlik bakımından bütünüyle kapatılmadı. Okuma 8/8 olsa da konuşmadaki ilk döküm tüm terimlerin eksiksiz envanteri olarak sunulmaz.

## Current work ve next authorised work

**Tamamlanan:** hazırlık; ilk pilot için gerçek sekiz dosyalık envanter; bu snapshot'taki tam paket okuması; konuşma içi ilk kullanım dökümüne dayanak olan bağlam ve önemli kapsam ayrımlarının çıkarılması.

**Sıradaki yetkili iş hâlâ PLAN/B1:** P1-T1 konuşma dökümünü geri kazan ve kaynak tarafındaki bölüm/listelerden başlayarak kullanım-bazlı kapsama kontrolü yap. Özellikle 00 başlangıç kaynakları/haritası, 01 §5/§6–17, 02 §4–5/§8/§18/§22–23/§29, 03 §4/§10/§20–21/§30 ve 04 §10–12/§20'deki adlandırmaları döküme karşı sınayarak atlanan veya fazla birleştirilen kullanımları tamamla. Yalnız mevcut dökümü tekrar okuyup eksiksiz ilan etme. Yeni anlam gerekirse kaynağa dön; sözlük bilgisinden boşluk doldurma.

B1 kapanışında gerçek kapsam, açık anlam belirsizlikleri ve gerekli düzeltmeler ayrılacak. Sonra B2 yöntem değerlendirmesi/revizyon kararı; ardından superpowers üzerinde B3 ikinci pilot ve B4 değerlendirmesi gelecek. Bu sırayı yürütmek için amacı yeniden onaylatmak gerekmez. İki pilot tamamlanmadan seri çıkarım, bütün araştırmaların çıkarımı bitmeden ortak tanım aşaması başlamaz.

## Konuşma içi pilotun devralma sınırı

Pilot kullanım kayıtları repo içinde değildir. P1-T1 görünür cevabı ve bu turdaki kaynak bağlantılı ara bulgular erişilebiliyorsa tamamı okunur; yalnız STATE'teki bu özet veya kayıt adedi bunların yerine geçmez. Görünür cevabın erişilebilir olduğu ayrıca kontrol edilir; STATE'in onu anması cevabın teslim/alım doğrulaması değildir.

Yeni oturum konuşma dökümüne erişemiyorsa onu hafızadan yeniden oluşturma veya kullanım listesi tamamlanmış kabul etme. Sabit kaynak ref ve yukarıdaki dosyalardan gerekli okumayı/çıkarımı yeniden yap; bunun yeniden üretim olduğunu açık tut. Daha önceki actor'ın tam okuma kaydı, yeni actor'ın kaynakları gerçekten gördüğü anlamına gelmez. Pilotun chat-only sınırını aşarak sessizce yeni TERMS arşivi oluşturma.

## Yeni oturum yolu

AGENT.md ve tetiklenen protokoller → concepts/INDEX.md → bu STATE → CHARTER.md → ORIGIN.md → METHOD.md → PLAN.md → SETUP-REVIEW.md → mevcut pilotun görünür P1-T1 çıktısı ve gerekli kaynak dosyaları.

Bu giriş dosyaları yeni oturumda tam okunur. Aynı oturumda tam okunmuş ve değişmemiş içeriklerin yeniden okunması mekanik zorunluluk değildir; maddi değişiklikte canonical içerik geri kazanılır. Önce main ile okuma snapshot'ı arasındaki ilgili dosya değişimini kontrol et; eski kullanımları yeni sürüme sessizce yükseltme. Arşivlenmiş eski concepts kararları devam noktası değildir. Zorunlu kontrol veya gerekli kaynak erişilemiyorsa eksik bilgi uydurulmaz.

## Yayın ve doğrulama bağlamı

Hazırlık başlangıcı: c7e5d02a5be15b4b938c2796e3c274b04aa4bca4. Hazırlık statik incelemesi: 0ab0a7759fba6c680cd4ab0cae5ba21d001b4be6; hazırlık STATE kapanışı / bu pilotun okuma snapshot'ı: ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a. Hazırlığın iki kapsam dışı satır düzeltmesi ve kontrol sınırları SETUP-REVIEW'de korunur.

P1-T1'de paket içeriği kaynak üzerinden okundu, ancak external factual revalidation, bağımsız aktör incelemesi, tam extraction-coverage testi veya yeni-oturum davranış deneyi yapılmadı. Bu turun yalnız STATE güncellemesi yayınlandıktan sonra geri okuma ve commit kapsamı kontrolü yapılır; başarısızlık halinde mevcut pilot kapanmış sayılmaz. METHOD v0.1-draft henüz doğrulanmış yöntem değildir.
