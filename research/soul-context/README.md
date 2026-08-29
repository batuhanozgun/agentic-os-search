# SOUL Context Research

## Amaç

Bu çalışma alanının amacı, `batuhanozgun/os-architect`, `batuhanozgun/keel` ve `batuhanozgun/soul` depolarını sistematik biçimde okuyarak **SOUL Research projesinin neden açıldığını, hangi problem sınıfını araştıracağını ve sonraki araştırmanın hangi niyetle yürütülmesi gerektiğini kanıta dayalı biçimde anlamaktır.**

Bu klasör araştırma sonucunun kendisi değil; uzun soluklu okuma, iz sürme, sentez ve oturumlar-arası devamlılık için çalışma evidir.

## Navigasyon

- `STATE.md` — current phase, verified findings, open hypotheses and exact next reading.
- `repos/os-architect/README.md` — tarihsel yöntem/araştırma/KEEL geliştirme okuma defteri.
- `repos/keel/README.md` — bugünkü KEEL mekanik karşı-okuma defteri.
- `repos/soul/README.md` — SOUL `main` + yüksek-bilgi work/verification branch okuma defteri.
- `notes/transition-to-soul.md` — KEEL/os-architect → SOUL geçişinin bağımsız sentez notu; direct evidence ile inference ayrı tutulur.

## Kaynak rolleri — güncel model

- `soul` — SOUL'un explicit amacı, Development OS'si, work package'ları ve verification davranışı için birincil kaynak. `main` minimaldir; repo-geneli yalnız default branch değildir.
- `os-architect` — KEEL'in ve onu üreten çalışma disiplininin karar, araştırma, hata, doğrulama, sahip düzeltmesi ve yöntem geçmişi.
- `keel` — bu geçmişin somutlaşmış ürün/mekanizma yüzeyi; tarihsel mekanizma iddialarının bugünkü karşılığını sınamak için.

## Araştırma sorusu

Ana soru:

> Bu üç repo birlikte okunduğunda SOUL neden yeniden kuruluyor; önceki çalışma ve ürün deneyimleri hangi problem alanlarını açığa çıkarıyor; SOUL Research hangi soruları cevaplamadan SOUL mimarisine geçmemeli?

Bu soru erken tek-cümlelik bir cevaba zorlanmayacaktır. Gözlem, çıkarım ve hipotez ayrı tutulacaktır.

## Okuma yöntemi

### 1. Giriş kapıları önce

Her repoda önce README, durum/indeks, genesis veya benzeri navigasyon dosyaları okunur. Büyük ağaca doğrudan toplu okuma yapılmaz.

### 2. Repo başına farklı strateji

- `soul`: önce `main` explicit intent; ardından dal haritasından yalnız yüksek-bilgi work/verification hattı. Foundation → active/first work package → verification/evidence sırası; bütün work branch'leri körlemesine tüketilmez.
- `os-architect`: indekslerden konu kümeleri seçilir; canlı bilgi, arşiv ve git geçmişi birbirine karıştırılmaz.
- `keel`: ürünün öz-anlatısı ile mekanik gerçekliği ayrılır; README/GENESIS/DEFO_MODELİ sonrasında yalnız yük taşıyan mekanizmalar ve test/guard yüzeyleri okunur.

### 3. Tematik geçişler

Okumalar şu problem temalarında gruplanır:

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
11. research/evidence'in architecture kararlarına giriş sözleşmesi.

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

Derived dış-literatür özetleri, geçmiş araştırmanın ne düşündüğünü gösterebilir; SOUL için load-bearing dış iddia olacaksa primary source recovery yapılır.

### 6. Erken sentez yasağı

Bir repodaki güçlü anlatı diğer iki repoya genellenmez. Özellikle KEEL'in kendi problem çerçevesi, SOUL'un araştırma sonucunu peşinen belirlemiş sayılmaz.

SOUL'un kendi foundation metinleri ürün hedefi için birincil kaynaktır; fakat ayrı **SOUL Research projesinin** charter'ı bulunmadan research amaç cümlesi çalışma hükmü olarak tutulur.

## Ölçeklenme kuralı

Başlangıçta repo başına tek `README.md` okuma defteri tutulur. Bağımsız bir tema repo sınırını aşmaya başladığında `notes/` altında tek canonical gövde açılır ve repo defterleri ona işaret eder.

Defter büyüyüp navigasyonu zorlaştırırsa:

1. önce `ledger.md` (kaynak envanteri) ile `notes/` (maddi tematik notlar) ayrılır,
2. sonra yalnız gerekirse tematik alt klasör açılır,
3. içerik kopyalanmaz; bir yerde gövde, diğer yerde işaretçi tutulur.

Yapı, ilerideki büyüklüğü tahmin ederek baştan şişirilmez; gerçek yük yeni katmanı gerektirdiğinde evrilir.

## Oturumlar arası devamlılık

Yeni bir konuşmada çalışma şu sırayla devam eder:

1. canonical `AGENT.md` ve routing'in yüklediği protokoller okunur.
2. Bu dosya okunur.
3. `STATE.md` okunur.
4. `STATE.md` bağımsız bir sentez notuna işaret ediyorsa o not açılır.
5. Yalnız `STATE.md`'nin işaret ettiği repo defteri ve kaynaklar açılır.
6. Yeni okuma yapıldıkça repo defteri, ilgili note ve `STATE.md` aynı oturumda güncellenir.

Chat geçmişi bu araştırmanın durum kaynağı değildir. Canonical çalışma durumu bu klasörde tutulur.

## Kapanış ölçütü

Bu hazırlık okuması, üç repo hakkında "yeterince dosya okundu" denildiğinde değil; aşağıdakiler kanıtla kurulabildiğinde tamamlanmış sayılır:

- SOUL'un yeniden başlangıç gerekçesi,
- önceki sistem/çalışma düzeninden taşınmak istenen problem dersleri,
- taşınmaması gereken ürün/runtime-özel varsayımlar,
- SOUL Research'ün cevaplaması gereken ana araştırma soruları,
- research/evidence'in architecture kararlarını nasıl kısıtlayacağı,
- bu soruların hangi primary sources, independent evidence ve karşı-kanıtlarla sınanacağı.
