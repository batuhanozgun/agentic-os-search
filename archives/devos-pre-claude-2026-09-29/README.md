# Tarihsel DevOS kaynak arşivi — kısmi

**30 Eylül 2026 / A3 devam ediyor.** Burası güncel DevOS kurulum planı değildir. Tek kurulum planı [devos/plan/](https://github.com/batuhanozgun/devos/tree/main/plan) altındadır; devir sürümü 2.1. [D030](../../explorations/EXP-006-development-os-calisma-duzeni/DECISIONS.md#d030--claude-code-cloud-kurulum-devri) ve [bakım planı](../../REPOSITORY-TRANSITION.md) yetki ve devam sınırını taşır.

## Gerçek içerik ve kalanlar

**Bu commit grubunda yalnız Academy'nin özgün gövdesi repository'ye alınır.** Dört rapor/paket ailesinin gerçek dosyaları konuşma ortamında geri kazanılıp doğrulandı; onların repository yayını henüz yapılmadı. Aşağıdaki kimlik envanteri, bulunmayan kaynak gövdelerinin yerine geçmez. İki aile henüz geri kazanılmadı.

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
