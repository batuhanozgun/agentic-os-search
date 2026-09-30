# Tarihsel DevOS kaynak arşivi — kısmi

**30 Eylül 2026 / A3 devam ediyor.** Burası güncel DevOS kurulum planı değildir. Tek kurulum planı [devos/plan/](https://github.com/batuhanozgun/devos/tree/main/plan) altındadır; devir sürümü 2.1. [D030](../../explorations/EXP-006-development-os-calisma-duzeni/DECISIONS.md#d030--claude-code-cloud-kurulum-devri) ve [bakım planı](../../REPOSITORY-TRANSITION.md) yetki ve devam sınırını taşır.

## Gerçek içerik ve kalanlar

**Repository'de özgün kaynak gövdesi olarak yalnız Academy bulunuyor.** Dört rapor/paket ailesinin gerçek dosyaları konuşma ortamında geri kazanılıp doğrulandı; onların repository yayını henüz yapılmadı. Aşağıdaki kimlik envanteri, bulunmayan kaynak gövdelerinin yerine geçmez. İki aile henüz geri kazanılmadı.

| Kaynak ailesi | Kaynak / kimlik sonucu | Bu repository'deki gövde | Statü |
|---|---|---|---|
| P4 v3 | Markdown, PDF, ZIP ve teslim kimliği eşleşti | Yayın bekliyor | Tarihsel; uygulama kaynağı değil |
| P4 v4 | Markdown, PDF, ZIP ve teslim kimliği eşleşti | Yayın bekliyor | Tarihsel; Codex ortam kararı geçersiz |
| P5 K00–K15 | Rehber, ZIP, başlangıç metni ve teslim kimliği eşleşti | Yayın bekliyor | Tarihsel; yeni kurulum talimatı değil |
| P5 S00–S12 | Yalnız eski teslim kaydındaki beklenen kimlikler var | Yok; geri kazanılmadı | Tarihsel; senaryolar ileride sınav fikri olabilir |
| P5 v2 Codex arayüzü | Rehber, ZIP, başlangıç metni ve teslim kimliği eşleşti | Yayın bekliyor | Tarihsel; yeni kurulum talimatı değil |
| SOUL ve DevOS | İstenen rapor doğrulanmış kimliğiyle bulunamadı | Yok | Tarihsel kaynak; başka metinle ikame edilmedi |
| SOUL Academy | Library v1 ham dosyası geri alındı; byte kimliği korundu | [Özgün metin](academy/SOUL_ACADEMY_EXPLORATORY_CONCEPT_NOTE.md) | Keşif notu; karar veya iş açma yetkisi değil |

Dosya başına boyut, SHA-256, Git blob kimliği ve yayın durumu [SOURCE-IDENTITIES.json](SOURCE-IDENTITIES.json) içindedir. `PENDING_PUBLICATION` satırlarındaki yollar hedef arşiv yerleridir; dosyanın şu anda GitHub'da bulunduğunu göstermez. S ailesindeki `expected_unverified` değerleri özgün dosyadan yeniden hesaplanmış değildir.

## Kullanım sınırı

Özgün gövdeler değiştirilmez; bu README ve kimlik kaydı onların yan kayıtlarıdır. Arşive almak mimari benimseme, canlı sistem yeterliği veya geçmiş testleri yeniden çalıştırma değildir. Kaynaklardaki eski current/next, rol ve kontrol metinleri pasif tarihsel malzemedir. Platformdan bağımsız bulgu veya kullanıcı kararının tarihçesi sırf tarihsel olduğu için geçersiz sayılmaz.

Görev, P4/P5'in bazı bölümlerinin yeni plana aktarıldığını bildirir; A3 bu aktarımın eksiksizliğini yeniden doğrulamıyor. Academy'nin kendi başlangıç statüsü ve §24/§27 sınırları korunur: notun karar yolundan geçmeden doğrudan iş veya kurulum açılmaz. Metindeki eski `soul` bağlamı tarihsel kaynaktır; yeni ürün deposu `soul-system`'dir.

Bu çalışma yalnız özel araştırma deposuna yazar; kaynakları açık ürün depolarına taşımaz. Hiçbir özgün dosya silinmedi veya taşınmadı. [A3 okuma, kimlik ve yayın kaydı](../../maintenance/2026-09-29-research-installation-separation/A3-INTAKE.md) kapsamı ve erişim sınırlarını açıklar.

## 30 Eylül 2026 — gövde aktarım engeli ve devam koşulu

**Başlangıç main:** `323e38d288b6760ab70e15744c86678fcbc9d125`. Kök bakım planı, A3-INTAKE ve arşiv giriş/kimlik kayıtları esas alındı. A2 yeniden açılmadı; A4/A5'e geçilmedi. Bu güncelleme yalnız aktarımın gerçek durumunu kaydeder; yeni bir kaynak gövdesinin yayınlandığını söylemez.

Konuşmaya yeniden bağlanan `A3_Dogrulanmis_Tarihsel_Kaynaklar_2026-09-30.zip` gerçek byte'larıyla açıldı. İçindeki SOURCE-IDENTITIES, repository'deki `db2fb9829de6ce39888dde65aca045c081e10ba1` blob'uyla eşleşti. **19/19 özgün dosya** kayıtlı boyut, SHA-256 ve Git blob kimliğiyle yeniden eşleşti; P4 v3'ün dört dosyası bu kapsamdadır. ZIP üyeleri, iç ZIP'ler, CRC, güvenli yollar ve bağımsız yazı tipi dosyası bulunmaması denetlendi. Tarihsel kod/testler çalıştırılmadı; PDF görünümü, içerik doğruluğu veya aktarım sadakati yeniden değerlendirilmedi.

**Engelin kapsamı:** Bu oturumun terminalinde `github.com` ve `api.github.com` ad çözümlemesi başarısız. Bağlı GitHub eylemleri UTF-8/base64 içerikle yazmayı destekliyor; fakat yerel dosya yolunu alıp büyük ikili gövdeyi doğrudan yükleyen bir eylem bulunmadı. Kurulu GitHub için ek dosya yükleme yolu araması da böyle bir eylem sağlamadı. Dolayısıyla bütün GitHub yazmalarının kapalı olduğu veya API'nin ikili veri kabul etmediği söylenmiyor; **büyük gövdelerin aktarımı bu oturumda tamamlanamadı**. P4 v3 Markdown'ının bilinen blob kimliğini okuma denemesi de 404 döndü; hash, uzakta mevcut gövde yerine kullanılmadı.

**Tek seferlik aktarım yolu:** Batu, zaten teslim edilmiş aşağıdaki ZIP'i açmadan bu özel arşiv dizinine yükleyebilir. Dört aileyi yeniden üretmeye, tek tek dosya seçmeye veya başka bir depoya yazmaya gerek yoktur. Bu yalnız kaynak taşımasıdır; kurulum işi değildir. Dosya henüz bu dizinde bulunmuş ya da yayınlanmış sayılmaz.

| Beklenen yükleme | Değer |
|---|---|
| Repository yolu | `archives/devos-pre-claude-2026-09-29/A3_Dogrulanmis_Tarihsel_Kaynaklar_2026-09-30.zip` |
| Byte | `20275988` |
| SHA-256 | `8b06cb2b3dca5875cab0ad72595701e3e0d4d756d0c80fa2f49041df48aa9b17` |
| Git blob SHA-1 | `547522120893c25d5c709deb5c0e18f57ebe7806` |
| Üyeler | 19 özgün kaynak + tarihli kimlik anlık görüntüsü + açıklama; toplam 21 |

**Devralma:** Yeni oturum önce bu uzak dosyanın gerçekten yüklenip yüklenmediğini ve kimliğini kontrol eder. Doğru gövde mevcutsa önce P4 v3'ün, sonra diğer üç ailenin kaynak erişimini ZIP içindeki kesin üye yollarına bağlar; erişim/yayın kayıtlarını buna göre günceller. Bir kaynağın ZIP içinde bulunması, bağımsız dosya yolunun GitHub'da oluştuğu anlamına gelmez; iki erişim biçimi ayrı gösterilir. ZIP içindeki eski SOURCE-IDENTITIES anlık görüntüsü, güncel repository envanterinin üstüne yazılmaz. Uzak yükleme yoksa veya kimlik uyuşmuyorsa `PENDING_PUBLICATION` korunur; aynı başarısız sorguları yeni ilerleme diye tekrarlamak yerine engel belirtilir. Desteklenen yeni bir doğrudan yükleme kabiliyeti gelirse mevcut özgün byte'larla o yol kullanılabilir.

S00–S12 ve “SOUL ve DevOS” bu ZIP'te yoktur; bu aktarım onların erişim açığını kapatmaz. A3'ün kalan kaynak erişimi, A4 genel tarama ve A5 son denetim yükleri aynen sürer. Bu tur yalnız bu README'nin durum/devralma açıklaması değişir; kaynaklar, kimlik envanteri, araştırma ve kontrol dosyaları değiştirilmez.
