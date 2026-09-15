# Aday Araştırma Kütüphanesi Sürekliliği ve Yeniden Kullanımı

## Amaç

SOUL Research sırasında `research/soul-context/**` ve `research/soul-foundations/**` dışında yapılan odaklı konu, belirli dış hedef veya hibrit araştırmaların tek seferlik konuşma çıktısı olarak kaybolmasını önle; bunları daha sonra Foundation derinleştirme, SOUL / Development OS tasarım, mimari, implementasyon veya build-vs-integrate kararlarında gerektiğinde geri çağrılabilir bir **candidate research library** olarak koru.

Bu protokolün amacı candidate study sonuçlarını Foundation truth, architecture decision veya implementation commitment haline getirmek değildir. Amaç iki yönlü sürekliliktir:

`yeni araştırma → candidate library'ye doğru statüyle kayıt`

ve

`Foundation / design / implementation sorusu → ilgili eski candidate studies'i seçici geri çağırma`.

## Temel İlke

> Foundation araştırması zemin ve yapısal araştırma otoritesidir; candidate studies ise gerektiğinde kanıt, falsifier, mekanizma bilgisi, dış capability bilgisi, implementation reference veya design pressure sağlayan ayrı araştırma kütüphanesidir.

Bir candidate study'nin mevcut olması onun Foundation altında bir düğüm, SOUL primitive'i, architecture component'i veya kullanılacak dependency olduğu anlamına gelmez.

## Araştırma Sınıfları

`research/` altında varsayılan üç üst seviye rol ayrılır:

1. `research/soul-context/**` — SOUL Research'in tarihsel/current bağlamını recover eden bounded context corpus. Candidate study değildir.
2. `research/soul-foundations/**` — SOUL / Development OS için foundational problem ground'larını first-principles biçimde araştıran ana zemin. Candidate study değildir.
3. `research/studies/**` — ileride yeniden kullanılabilecek candidate studies kütüphanesi.

Yeni bir durable araştırma bu iki özel sınıfa açıkça ait değilse, aksi ayrıca kararlaştırılmadıkça `research/studies/**` altında candidate study olarak konumlandırılır.

## Study Type Ayrımı

Candidate study'nin türünü kullanılan kaynakların dış/iç oluşuna göre değil, **araştırma nesnesine** göre belirle:

- **`focused-topic`** — araştırma nesnesi bir kavram, problem, mekanizma, yöntem, pattern, teknik alan veya karar uzayıdır. Dış kaynaklardan yoğun biçimde beslenebilir.
- **`external-target`** — araştırma nesnesi belirli bir dış repository, makale, ürün, servis, standard, dataset, provider, katalog veya başka tanımlı dış artefakttır.
- **`hybrid`** — çalışma belirli dış hedefi incelerken aynı zamanda hedefi aşan bounded konu/mekanizma araştırmasını birleştirir ve iki rol de maddidir.

Türü yalnız klasör adına veya tek bir kaynağa bakarak varsayma. Kararsızlık maddiyse `hybrid` veya explicit unresolved classification kullan.

## Protokol

### 1. Yeni / Güncellenen Candidate Study'yi Kaydet

Bir tur yeni candidate study yaratıyor veya mevcut bir study'nin anlamını, statüsünü ya da kullanım değerini maddi biçimde değiştiriyorsa:

1. package'i `research/studies/<slug>/` altında tut;
2. package-local `META.md` bulunduğunu doğrula; yoksa oluştur;
3. `META.md` içinde en az şu bilgileri taşı:
   - study id / title;
   - `study_type`;
   - current status;
   - research object / primary question;
   - potential Foundation relevance;
   - potential SOUL relevance;
   - potential Development OS relevance;
   - likely reuse stages / revisit triggers;
   - epistemic/authority boundary;
   - freshness / revalidation requirement;
   - package entrypoint(s);
   - external target/ref/date gerekiyorsa;
4. `research/studies/CATALOG.md` derived retrieval index'ini güncelle;
5. varsa package `STATE.md` / `INDEX.md` semantiğini koru; `META.md` bunların current work authority'sini ele geçirmez.

Her citation veya kullanılan her dış kaynak candidate study değildir. Bu kayıt package seviyesindedir; ayrıntılı evidence kendi research dosyasında kalır.

### 2. Package-Local Authority ile Catalog'u Ayır

- `META.md` — package sınıflandırması, reuse semantiği ve cross-phase relevance için package-local canonical surface.
- `STATE.md` varsa — package'in current/completion/work state'i için authority.
- `INDEX.md` varsa — package retrieval router'ı.
- `CATALOG.md` — yüzlerce study arasında keşif için **derived index**; ayrıntılı truth veya current package state'in yerine geçmez.

Aynı gerçeğin iki authoritative kopyasını yaratma.

### 3. Foundation Relevance'i Many-to-Many ve Provisional Tut

Bir study birden fazla Foundation alanıyla ilişkili olabilir ve bu ilişki zamanla değişebilir.

Örneğin bir API discovery catalog'u Environment/capability, Information/data access ve Work/build-vs-integrate açısından farklı zamanlarda yararlı olabilir.

Bu nedenle metadata'daki Foundation relevance:

- retrieval hint / candidate relation'dır;
- Foundation taxonomy membership değildir;
- ontology relation değildir;
- architecture decision değildir.

Study bulgularını mevcut Foundation tree'ye zorla yerleştirme.

### 4. Eski Candidate Studies'i Geri Çağır

Mevcut Foundation, SOUL / Development OS design, architecture, implementation, benchmark veya build-vs-integrate işi daha önce araştırılmış candidate studies'den maddi fayda görebilecekse:

1. önce `research/studies/CATALOG.md` ile adayları daralt;
2. yalnız ilgili adayların `META.md` dosyalarını oku;
3. gerekiyorsa package `STATE.md` / `INDEX.md` üzerinden ilgili finding/evidence'e in;
4. load-bearing claim güncel dış olguya bağlıysa canonical external source'u yeniden doğrula;
5. candidate study'yi mevcut Foundation/current project authority ile birlikte değerlendir;
6. ilgisiz yüzlerce study'yi körlemesine context'e yükleme.

Retrieval miss study absence değildir; exact karar gerekiyorsa catalog/path/search derinliği yeterli mi kontrol et.

#### Problemden Araştırmaya ve Araştırmadan Hükme

İlgili araştırmayı yalnız kullanıcının kullandığı terim veya ürün adıyla değil, alttaki ihtiyaç, işlev, kısıt ve olası hata üzerinden de ara. Konuyla ilişkili bilgi başka bir başlıkta bulunabilir. Katalog mevcut kütüphaneye giriş sağlar; bütün bilgi veya çözüm alanının sınırı değildir. Seçenek kapsamı sorununu R01 ile değerlendir; katalogda bulamamak ne bilginin yokluğunu ne de otomatik yeni study gerekliliğini gösterir.

Geri çağrılan araştırmanın mevcut soruya katkısını değerlendir: bir varsayımı sınaması, çerçeveyi değiştirmesi, seçenek eklemesi veya elemesi, mevcut tercihi desteklemesi ya da kanıt gereksinimini ve kullanım sınırını belirginleştirmesi gibi. Yalnız “okudum” demek veya dosya adı sıralamak, bu değerlendirmenin yapıldığını göstermez.

Sonucun değişmemesi veya adayın ilgisiz bulunması meşru sonuçtur; araştırmayı kullanmış görünmek için zorla yenilik veya öneri üretme. Önemli katkı ve sınırları karar gerekçesinde gerektiği kadar görünür kıl; her yanıtta ayrı rapor veya her dosya için katkı kaydı zorunlu değildir. Kalıcı kayıt ihtiyacını R07 ve mevcut yazma yetkisiyle değerlendir. Yeniden kullanım, araştırmayı etkin kontrol, Foundation doğrusu veya benimsenmiş mimariye yükseltmez.

### 5. Foundation Research'in Bağımsızlığını Koru

Candidate library'nin varlığı first-principles Foundation research'i moda taxonomy'lere veya hazır çözümlere bağlamamalıdır.

Aktif Foundation package/method:

- candidate studies'i ne zaman external evidence, falsifier veya boundary check olarak kullanabileceğini;
- ne zaman önce independent problem discovery yapması gerektiğini;
- hangi node/phase'in aktif olduğunu

belirlemeye devam eder.

R09 candidate study'leri **bulunabilir** kılar; Foundation metodunu override etmez.

### 6. Revalidation Kuralı

External-target ve zamanla değişebilen teknik focused-topic çalışmalarında eski research sonucu ile current adoption kararını ayır.

Özellikle şu olgular eski olabilir:

- provider availability;
- version / API contract;
- pricing / free tier;
- licensing / terms;
- security/privacy properties;
- model/library behavior;
- benchmark leaderboards;
- repository HEAD / maintenance state.

Karar bunlara dayanıyorsa authoritative current source'a dön.

### 7. Epistemik Statüyü Koru

Candidate study şu rollerden birini veya birkaçını taşıyabilir:

- evidence/reference;
- falsifier/counterexample;
- design pressure;
- capability/discovery source;
- implementation-learning reference;
- benchmark/test-case source;
- candidate mechanism/pattern;
- negative/rejected option.

Bunların hiçbiri tek başına `adopted` anlamına gelmez.

Study rejected, superseded veya adopted olursa metadata'da açık statü taşı; geçmiş tekrar aynı araştırmayı yaptırmayacak kadar recoverable kalsın.

### 8. Fresh-Session Testi

Material candidate research turu kapanmadan önce sor:

> Önceki konuşmayı görmeyen yeni oturum `AGENT.md → R09 → research/INDEX.md → research/studies/CATALOG.md → package META/STATE/INDEX` yolu ile bu study'nin ne olduğunu, neden saklandığını, ne zaman yeniden bakılması gerektiğini ve neyi **kanıtlamadığını** recover edebilir mi?

Hayırsa continuity eksiktir.

## Root Router ve Package Contract

Project-work retrieval surfaces:

- `research/INDEX.md` — research root sınıflandırma ve routing yüzeyi;
- `research/studies/INDEX.md` — candidate library router;
- `research/studies/CATALOG.md` — derived study catalog;
- `research/studies/PACKAGE-CONTRACT.md` — yeni candidate study minimum package semantiği.

Bu dosyalar project-work layer'dır; agent-control authority değillerdir. Bu protokol onları çalışma verisi/router'ı olarak kullanır.

## Diğer Protokollerle Ayrım

- **R01** classification/relevance varsayımlarını sorgular.
- **R03** candidate research kullanımının latest end goal ve authorized phase ile uyumunu korur.
- **R05** catalog/metadata'nın detailed research veya external source'u eksik temsil etmesi riskini sınar.
- **R07** tur sonunda material study/state değişikliğinin canonical repository'de recoverable kalmasını sağlar.
- **R08** substantive work başlamadan current canonical project state'i recover eder.
- **R09** candidate research library'nin iki yönlü kayıt ve yeniden kullanım yaşam döngüsünü yönetir.

## Nihai Kontrol

R09 yüklendiğinde ilgili tur için şunları değerlendir:

1. Bu çalışma context, foundations veya candidate study mi?
2. Candidate ise study type araştırma nesnesine göre doğru mu?
3. Package `META.md` var ve current relevance/statüyü doğru taşıyor mu?
4. CATALOG derived index güncel mi?
5. Foundation relevance yalnız retrieval hint olarak mı tutuluyor?
6. Mevcut çalışma eski studies'den fayda görebilir mi; hangileri gerçekten ilgili?
7. Detailed evidence / current external source'a inmek gerekiyor mu?
8. Candidate finding yanlışlıkla architecture/Foundation truth'a promote edildi mi?
9. Fresh session bu study'yi ve kullanım sınırını geri bulabilir mi?

## Temel İlke

**Foundation zemindir; candidate studies hazır cevap değildir. Araştırmaları kaybetme, fakat onları zamansız veya yetkisiz biçimde mimariye de dönüştürme.**
