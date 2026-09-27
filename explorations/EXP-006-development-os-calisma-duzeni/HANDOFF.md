# EXP-006 — HANDOFF

**27 Eylül 2026 / P4 RAPOR v2 TESLİMATA HAZIR / YENİ MİMARİ ÖNERİ.**

## Önce okunacaklar

[STATE](STATE.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [P4-02](work/P4-02-soul-derived-report-v2.md) → gerçek **v2 kaynak ZIP/PDF**.

P4-02 yalnız current fark, kanıt ve artefakt kimliği kaydıdır; 200 sayfanın yerine geçmez. Dosyalar bu konuşmada teslim edilmiştir, tam gövdeleri repository'de değildir. Erişim yoksa `EXP-006_DevOS_v2_Kaynak_Paketi.zip` istenir; eski report veya bu özetten ayrıntı uydurulmaz.

## Neden yeni yazım var?

İlk 200 sayfalık rapordan sonra kullanıcı memory/context/graph/harness derinliğini sorguladı. Assistant'ın graph ve sadeleştirme hakkındaki değişken önerileri, diğer seçimlerin de azla yetinerek yapılmış olabileceği kaygısı doğurdu. Kullanıcı yüzeysel taramayı durdurup **SOUL hedefinden başlayarak raporun tamamını yeniden yazma** yetkisi verdi.

Bu görev tamamlandı: 200 sayfa, 52 kaynak, bütünleşik gereksinim/mimari/sözleşme/deney programı. Yalnız graph bölümü eklenmedi. Eski raporun bütün cümleleri yanlış sayılmadı; kolaylık lehine örtük tercih korunmadı. Daha fazla bileşen kendi başına kalite kanıtı değildir.

## Devralınacak yeni öneri

SOUL gerekli işi keşfeden, işe göre çalışma sistemi kuran/işleten, araştırmayı kullanan, uzun/bileşik çıktıları değerlendiren ve yöntemlerini değiştirebilen hedef yapıdır. DevOS bunu geliştirme ve sınama gereksinimlerine göre kurulmalıdır; assistant SOUL backlog'unu ekibin yerine seçmez.

V2; Claude cloud bilişsel ekip + korunan mekanik kontrol, takım ağırlıklı süren işbirliği ve odaklı görev profilleri önerir. PostgreSQL canlı iş/atama/inceleme/grant/yayın/typed relation otoritesi; Git ürün ve release içerik sürümü; hash'li kaynak/kanıt ayrı korunur. Markdown çalışma görünümleri türetilmiştir. Graph contract, AND/OR destek, invariant ve query'ler; hybrid retrieval/context compiler; protected publisher, outbox/inbox, read-set ve fencing birlikte tanımlıdır.

Shared runtime'da aynı credential'ı kullanan agent adları ayrı güvenlik principal'ı değildir. DB–Git tek transaction değildir. Impact sorgusu aday etkiyi bulur; her downstream kararı otomatik yanlış ilan etmez. Superseded içerik tarihsel kullanımda hâlâ gerekli olabilir.

G/Y içerik–düzen ayrımı, K1/K2, müşteri yetki/kabulü korunur. 18 hedef profili 18 sürekli çalışan süreç değildir. Eski P4-01 alt-ajan/Git ağırlıklı başlangıç tercihi **önceki baseline** olarak kalır; yeni ayrıntı v2'dedir.

## Kanıt ve paket

P4-02 §2 artefakt adları ve SHA-256 kimliklerini taşır. ZIP tek Markdown kaynak, kaynak kataloğu, PDF renderer, graph/context/API/DDL taslakları, referans model ve QA içerir. Font içermez.

40 yerel Python/SQLite testi geçti; dört seçilmiş kontrol kaldırıldığında ilgili testler bozuldu. Bu same-author sınırlı referans modeldir. PostgreSQL kurulumu, Claude rol iletişimi, gerçek auth, yayın/timeout, sandbox, restore, büyük workload veya bilişsel kalite testi değildir. Testlerde dış yayın gözlemi ve principal bilgisi fixture'dır. P5/P6 başarısı çıkarılmaz.

200 sayfalık PDF render edildi; tüm sayfalar temas görünümlerinde, yoğun örnekler yüksek çözünürlükte incelendi. Bağlantı, sayfa, kaynak kimliği ve metin sınırı kontrolleri geçti. Bu teknik mimari doğrulaması değildir.

## Sonraki iş ve durma sınırı

Mevcut tur rapor ve kaynak paketinin teslimiyle biter. Kullanıcının değerlendirmesi veya sonraki yönü v2 üzerinde ele alınır. Uygulama açıldığında rapor s.177–190 programı gerçek hedef cloud, operasyon deposu ve dış kontrol hizmetiyle bağlanır; gerekiyorsa kaynaklar tazelenir.

Eski permission-matrix next'ini kör sürdürme; yeni raporu bütün kullanıcı kabulü sayma; P5 kurulumunu otomatik başlatma. Yüzeysel anahtar sözcük taraması yeni rapor değerlendirmesinin yerine geçmez. Bütün research korpusu da her tur körlemesine tekrar okunmaz; kararın gerektirdiği kaynak derinliği kullanılır.

Önceki ayrıntılı P4 handoff'u `e3856a4` Git kesitinde korunur. Yeni rapor birikimi repository'deki eski tasarımın üzerine sessizce doğrulanmış gerçek olarak yazılmadı. Agent-control bu tur değişmedi.
