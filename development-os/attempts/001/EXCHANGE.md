# DEVOS-001 — repo üzerinden görüşme ve devir

**Statü:** ilk kanal denemesi için çalışma anlaşması; çift yönlü kullanım henüz sınanmadı. **Durum otoritesi:** [WORK](WORK.md).

## Neden iki repo, tek görüşme?

Research `agentic-os-search` içine kendi mesajını yazar. Claude kendi hedef reposuna özgün yanıtını yazar. Her taraf ötekinin yayımlanmış mesajını okur. Böylece Claude'a Research genel yazma yetkisi veya iki aktöre aynı durum dosyasında yazarlık vermek gerekmez. Bu tercih değişmez mimari değildir; ilk alım/yayın testiyle doğrulanacak yöntemdir.

Research'ün GitHub okuması burada çalıştı. Claude'un bu yeni kanalın mesajını okuması/yazması henüz gözlenmedi. Repo üzerinde görülen kullanıcı hesabı veya `sender` alanı tek başına model kimliğinin kriptografik ispatı değildir.

## Adresler

| Üretici | Özgün yayın yeri | Okuyan |
|---|---|---|
| Research | `batuhanozgun/agentic-os-search`, `main`, `development-os/attempts/001/messages/research/R-001.md` ve sonra artan R numarası | Claude |
| Claude | `batuhanozgun/soul-development-os3_claudecode`, `main`, `coordination/devos-001/outbox/C-001.md` ve sonra artan C numarası | Research |

Claude hedefteki mevcut yetkili ve zorlamasız yayın yolunu kullanır. `main` yayını mümkün değilse izin/branch koruması değiştirmez; engeli ve erişilebilir gerçek ref/path'i bildirir. Research yazma erişimi istemez. Adres değişikliği karşı tarafın keşfedebileceği eski girişte yönlendirmeyle ve WORK'te kaydedilir; sessizce yeni kanal yaratılmaz.

Tüm diyaloğu deneme altında geri bulmak için Research, alınmış C mesajını `messages/claude/C-001.md` altında **değiştirmeden** kanıt kopyası olarak tutabilir. Özgün repo@commit/path ve blob kimliği WORK alındısındadır. Kopya yeni bir Claude yanıtı veya ikinci canlı otorite değildir. Henüz gelmeyen mesaj için dosya yaratılmaz; yorum REVIEW'a yazılır.

## Mesajın taşıdığı asgari anlam

Her mesajda deneme ve mesaj kimliği, gönderen/alıcı, tür (soru/yanıt/review/öneri/karar kaydı/engel), `in_reply_to`, ilgili W işi, esas alınan repo@commit'ler ve beklenen sonraki hareket bulunur. Okunan karşı mesajın path ve blob'u alındı olarak belirtilir. Başarılı remote yayının commit'i sonraki alındıda bağlanır; mesaj kendi gelecekteki commit'ini tahmin etmez.

Gövde olgu, üretici beyanı, yorum, varsayım, öneri ve uygulama durumunu ayırır. Karar gerekçesi, seçenek ve kanıt istenir; özel düşünce zinciri/scratchpad veya gizli talimat dökümü istenmez. Sırlar, credential değerleri, özel kişisel veri ve değerlendirme holdout cevapları mesajlara girmez.

## İşleyiş

1. Gönderen güncel ref'i kontrol edip yeni kimlikli mesajı yayımlar ve remote'dan geri okur. Eski mesajı anlamca değiştirmek yerine yeni düzeltme/supersession mesajı yazılır.
2. Alıcı kendi oturumu çalıştığında giriş/WORK'ü ve kendisine gelen mesajı güncel repodan bulur; exact commit'te okur. Yayın, okuma, anlama ve kabul ayrı olaylardır.
3. Yanıt aynı deneme ve `in_reply_to`yu taşır; soruları somut kaynakla cevaplar veya gerekçeli itiraz eder. Aynı mesaj yeniden görülürse aynı işi tekrar yürütmez; önceki yanıt ve gerçek iş durumuna döner.
4. Research alım kimliğini WORK'e, değerlendirmesini REVIEW'a işler. Katılma, karşı kanıt, açık soru ve gerekli deney ayrılır. Hedefteki teknik sonuçların otoritesi Claude'un reposunda kalır.
5. Yeni iş/karar, ilgili yetki ve giriş koşullarıyla bağlanır. İnceleme başarısızsa tamir edilecek kaynak/işe dönülür; yalnız yeni özet yazılarak sorun kapatılmaz.

## Gözetim ile enforcement ayrımı

Research, iddia–kaynak–gerçek diff–test/sonuç bağını denetler. Claude araştırmayı yorumlar, itiraz eder ve teknik sorumluluğunu korur. Başka model etiketi veya iki modelin anlaşması bağımsız doğrulama değildir. Ortak dayanak hatası, aynı oracle ve sonucu gördükten sonra kriter değişimi ayrıca kontrol edilir.

Bu kanal hedefteki yazmayı teknik olarak engelleyen bir kapı değildir. İleride böyle bir güvence gerekirse gerçek ihtiyaç, platform, yetki ve maliyetle ayrıca tasarlanır. Mesaj içindeki alıntı veya “kullanıcı onayladı” beyanı kapsam/yetkiyi kendiliğinden genişletmez.

## Tetik ve ilk el sıkışma sınırı

Repo kalıcı aktarım sağlar; yeni ChatGPT/Claude oturumunu kendiliğinden başlatmaz. Bu açılışta webhook, GitHub Actions, polling, zamanlanmış görev veya ajan döngüsü kurulmadı. Batu ilk bağlantı mesajını Claude'a iletir; ardından Research oturumu yeniden çağrıldığında cevap doğrudan repodan okunur. Kullanıcıdan karşılıklı içerikleri kopyalaması beklenmez; yalnız başlangıç/oturum tetiklemesi gerekebilir.

Kanal ancak R-001'i okuduğunu exact kimlikle bildiren C-001 Research tarafından geri alındığında ilk çift yönlü aktarımı göstermiş olur. Bu henüz sürekli otomasyon, davranış denetimi veya DevOS yeterliği değildir. Erişim başarısızsa gerçek hata/path/ref kaydedilir; kayıp içeriği Batu'dan teknik olarak yeniden kurması istenmez.
