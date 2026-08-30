# SOUL Context Research

## Amaç

Bu çalışma alanının amacı, `batuhanozgun/os-architect`, `batuhanozgun/keel`, `batuhanozgun/soul` ve gerektiğinde sınırlı predecessor kanıtı olarak `batuhanozgun/keel-research` depolarını sistematik biçimde okuyarak **SOUL Research projesinin neden açıldığını, hangi tür sistemi araştırmanın beslemesi beklendiğini ve sonraki araştırmanın hangi niyetle yürütüleceğini kanıta dayalı biçimde anlamaktır.**

Bu klasör proje-geneli araştırma metodolojisinin kendisi değildir; uzun soluklu okuma, iz sürme, sentez ve oturumlar-arası devamlılık için **bounded context workspace**'tir.

Bu çalışma sırasında erken geliştirilen taxonomy, holdout, stopping ve research-package fikirleri yalnız `research/soul-context/**` altında **provisional context hypotheses** statüsündedir. Bunlar `AGENT.md`, `agent/**`, proje-geneli araştırma governance'ı veya SOUL mimarisi değildir.

## Navigasyon

- `CONTEXT-SYNTHESIS.md` — bu context çalışmasının bounded sonucu, non-proofs ve stop/handoff sınırı.
- `STATE.md` — current status ve yeniden açılırsa continuation pointer.
- `repos/os-architect/README.md` — tarihsel yöntem/araştırma/KEEL geliştirme okuma defteri.
- `repos/keel/README.md` — bugünkü KEEL mekanik karşı-okuma defteri.
- `repos/soul/README.md` — SOUL `main` + yüksek-bilgi work/verification branch okuma defteri.
- `repos/keel-research/README.md` — yalnız SOUL source chain'i işaret ettiğinde kullanılan bounded predecessor ledger.
- `notes/transition-to-soul.md` — KEEL/os-architect → SOUL geçişinin bağımsız sentez notu; direct evidence ile inference ayrı tutulur.
- `notes/research-to-architecture-boundary.md` — research finding ile architecture commitment ayrımının kaynak sentezi.
- diğer `notes/` — bu context hattında oluşmuş provisional challenge/taxonomy/holdout notları; proje-geneli karar değillerdir.

## Kaynak rolleri — güncel model

- `soul` — SOUL'un explicit amacı, Development OS'si, work package'ları ve verification davranışı için birincil kaynak. `main` minimaldir; repo-geneli yalnız default branch değildir.
- `os-architect` — KEEL'in ve onu üreten çalışma disiplininin karar, araştırma, hata, doğrulama, sahip düzeltmesi ve yöntem geçmişi.
- `keel` — bu geçmişin somutlaşmış ürün/mekanizma yüzeyi; tarihsel mekanizma iddialarının bugünkü karşılığını sınamak için.
- `keel-research` — SOUL'un kendi source chain'i doğrudan işaret ettiğinde kullanılan predecessor prior-art; SOUL authority veya dördüncü eşit omurga kaynak değildir.

## Ana context sorusu

> Bu kaynaklar birlikte okunduğunda SOUL neden yeniden kuruluyor; önceki çalışma ve ürün deneyimleri hangi problem alanlarını açığa çıkarıyor; Batu araştırma sonrasında nasıl bir yapının kurulmasını amaçlıyor?

Bu soru erken tek-cümlelik bir cevaba zorlanmadı. Gözlem, çıkarım ve hipotez ayrı tutuldu.

## Okuma yöntemi

### 1. Giriş kapıları önce

Her repoda önce README, durum/indeks, genesis veya benzeri navigasyon dosyaları okunur. Büyük ağaca doğrudan toplu okuma yapılmaz.

### 2. Repo başına farklı strateji

- `soul`: önce `main` explicit intent; ardından dal haritasından yalnız yüksek-bilgi work/verification hattı. Foundation → active/first work package → verification/evidence sırası; bütün work branch'leri körlemesine tüketilmez.
- `os-architect`: indekslerden konu kümeleri seçilir; canlı bilgi, arşiv ve git geçmişi birbirine karıştırılmaz.
- `keel`: ürünün öz-anlatısı ile mekanik gerçekliği ayrılır; README/GENESIS/DEFO_MODELİ sonrasında yalnız yük taşıyan mekanizmalar ve test/guard yüzeyleri okunur.
- `keel-research`: yalnız primary SOUL/predecessor source chain'i maddi bir iddiayı ona bağladığında açılır; bağımsız SOUL authority sayılmaz.

### 3. Tematik geçişler

Okumalar şu problem temalarında gruplanmıştır:

1. problem ve defo modeli,
2. oturumlar-arası süreklilik / kanonik durum,
3. amaç–yöntem ayrımı ve drift,
4. roller, motivasyon ayrımı ve karar sınırları,
5. doğrulama, bağımsızlık ve öz-onaylama,
6. insan/sahip kontrol yüzeyi,
7. mekanik kapılar, iz ve falsifiability,
8. araştırma ve dış-göz yöntemleri,
9. ürün ile geliştirme işletim sisteminin ayrımı,
10. KEEL'e özgü olan ile genel amaçlı SOUL'a taşınabilecek olanın ayrımı,
11. research/evidence'in architecture kararlarına giriş sınırı.

### 4. Her okuma iz bırakır

Her okunan kaynak repo defterine şu bilgilerle işlenir:

- yol,
- ref/SHA,
- okuma türü (`full`, `partial`, `index`, `history`),
- neden okunduğu,
- maddi bulgu,
- açtığı soru / sonraki işaretçi.

Her dosya için ayrı not dosyası açılmaz. Yeni not dosyası yalnız bir tema veya iddia bağımsız yaşamaya başladığında oluşturulur; aksi halde klasör gereksiz şişirilmez.

### 5. Kanıt dili

Sentezde üç statü kullanılır:

- **Gözlem:** kaynakta doğrudan görülen olgu.
- **Çıkarım:** bir veya daha fazla gözlemden türetilen yorum.
- **Hipotez:** henüz yeterli karşı-okuma yapılmamış açıklama.

Bir kaynağın kendi öz-anlatısı, mekanizmanın gerçekten çalıştığına tek başına kanıt sayılmaz. İddia mekanik etkililik taşıyorsa gerektiğinde kod, guard, test, fixture, tarihsel arıza veya bağımsız değerlendirme yüzeyine inilir.

Derived dış-literatür özetleri, geçmiş araştırmanın ne düşündüğünü gösterebilir; SOUL için load-bearing dış iddia olacaksa primary source recovery gerekir.

### 6. Erken sentez / promotion sınırı

Bir repodaki güçlü anlatı diğer kaynaklara genellenmez. Özellikle KEEL'in kendi problem çerçevesi, SOUL'un araştırma sonucu veya mimarisi sayılmaz.

SOUL'un foundation metinleri ürün hedefi için birincil kaynaktır; fakat bu context hattında oluşmuş D1–D11, V1–V4, stopping logic veya package fikirleri **yalnız local provisional synthesis**'tir.

Bu klasördeki bir bulgu şu alanlara kendiliğinden promotion yapmaz:

- `AGENT.md`,
- `agent/**`,
- proje-geneli araştırma yöntemi/governance'ı,
- SOUL architecture/requirements/backlog,
- canonical stopping veya evidence-package standardı.

## Ölçeklenme kuralı

Repo başına okuma defterleri ve bağımsız temalar için `notes/` kullanılır. İçerik kopyalanmaz; bir yerde gövde, diğer yerde işaretçi tutulur.

Yapı, ilerideki büyüklüğü tahmin ederek baştan şişirilmez; gerçek yük yeni katmanı gerektirdiğinde evrilir.

## Oturumlar arası devamlılık

Bu context hattı yeniden açılırsa çalışma şu sırayla devam eder:

1. canonical `AGENT.md` ve routing'in yüklediği protokoller okunur.
2. Bu dosya okunur.
3. `CONTEXT-SYNTHESIS.md` okunur.
4. `STATE.md` okunur.
5. Yalnız belirli bir claim/question gerekiyorsa ilgili repo ledger veya note açılır.

Chat geçmişi bu araştırmanın durum kaynağı değildir. Canonical çalışma durumu bu klasörde tutulur.

## Context hattının kapanış ölçütü

Bu hazırlık/context okuması aşağıdakiler kanıtla kurulabildiğinde yeterli sayılır:

- SOUL'un yeniden başlangıç gerekçesi,
- önceki sistem/çalışma düzeninden taşınmak istenen problem dersleri,
- taşınmaması gereken ürün/runtime-özel varsayımlar,
- araştırmanın beslemesi beklenen sistem yönü,
- research/evidence ile architecture decision arasındaki sınır,
- erken geliştirilen research-method fikirlerinin context-local/provisional olduğu.

Bu ölçütler için bounded synthesis `CONTEXT-SYNTHESIS.md` içinde bulunmaktadır. Proje-geneli **"araştırmayı nasıl yapacağız?"** kararı bu klasörün kapanışından sonra ayrıca ve yeniden türetilmelidir.