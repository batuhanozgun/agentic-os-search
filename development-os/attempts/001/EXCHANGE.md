# DEVOS-001 — repo üzerinden görüşme ve devir

**Checkpoint:** R-001→C-001 ilk iki-repo aktarımı Research tarafından geri alındı. Yeni mesaj R-002; actual yayın/tüketim durumunun tek otoritesi [WORK](WORK.md). Sürekli otomasyon ve uygulama yaptırımı kurulmuş değil.

## Neden iki repo, tek görüşme?

Research `agentic-os-search` içine kendi mesajını yazar. Claude kendi hedef reposuna özgün yanıtını yazar. Her taraf ötekinin yayımlanmış mesajını okur. Claude'a Research genel yazma yetkisi veya iki aktöre aynı durum dosyasında yazarlık vermek gerekmez. Bu tercih değişmez mimari değildir; ilk aktarımın çalışması her gelecekteki alımı garanti etmez.

Research'ün GitHub okuması ve C-001'deki exact R-001 alındısı gösterildi. Repo üzerinde kullanıcı hesabı veya `sender` alanı tek başına model kimliğinin kriptografik ispatı değildir. C-001'in davranış beyanları ile Research'ün kaynak/deney gözlemleri ayrılır.

## Adresler

| Üretici | Özgün yayın yeri | Okuyan |
|---|---|---|
| Research | `batuhanozgun/agentic-os-search`, `main`, `development-os/attempts/001/messages/research/R-NNN.md` | Claude |
| Claude | `batuhanozgun/soul-development-os3_claudecode`, `main`, `coordination/devos-001/outbox/C-NNN.md` | Research |

Sıra R-001→C-001→R-002→C-002 olarak başlar; iş ve yanıt ilişkisi WORK'tedir. Claude mevcut yetkili, zorlamasız yayın yolunu kullanır. `main` mümkün değilse izin/branch koruması değiştirmez; engeli ve erişilebilir exact ref/path'i bildirir. Adres değişikliği eski girişte yönlendirilir ve WORK'e yazılır; sessiz yeni kanal yoktur.

Research alınmış C mesajını `messages/claude/C-NNN.md` altında **byte-eş** kanıt kopyası tutabilir. Özgün repo@commit/path/blob WORK alındısındadır; kopya ikinci canlı otorite değildir. Byte-eş kopya oluşturulmadıysa exact özgün bağlantı kullanılır, yeniden yazılmış özet özgün mesaj diye sunulmaz. Henüz gelmeyen mesaj için dosya yaratılmaz; yorum REVIEW'a gider.

## Mesajın anlamı ve işleyiş

Mesaj: deneme/mesaj kimliği, taraflar, tür, `in_reply_to`, ilgili W işi, esas repo@commit, karşı mesajın path/blob'u ve beklenen hareketi taşır. Kendi gelecekteki yayın commit'ini tahmin etmez; actual ref sonraki alındıda bağlanır. Olgu, üretici beyanı, yorum, öneri ve uygulama ayrı. Karar gerekçesi/kanıt istenir; gizli düşünce zinciri, credential, hassas ham veri veya holdout cevapları istenmez.

1. Gönderen current ref'i doğrular, yeni kimlikle yayımlar ve remote'dan geri okur. Eski mesajı anlamca değiştirmek yerine düzeltme/supersession mesajı yazar.
2. Alıcı kendi oturumu çalıştığında WORK ve ilgili mesajı bulur, exact commit'te okur. Yayın, okuma, anlama ve kabul ayrı olaylardır.
3. Aynı mesaj tekrar görülürse önce önceki yanıt ve gerçek işe bakılır; etkili eylem körlemesine tekrarlanmaz.
4. Research alımı WORK'e, kanıt/itirazı REVIEW'a işler. Hedef teknik sonuçları hedef repoda otorite kalır.
5. Yeni iş ilgili yetki ve giriş koşullarıyla bağlıdır. Review başarısızsa tamir edilecek kaynağa/işe dönülür, yeni özetle kapatılmaz.

## Denetim, deney görünürlüğü ve yetki

Research iddia–kaynak–diff–test sonucunu karşılaştırır; Claude itiraz ve teknik sorumluluğunu korur. İki modelin anlaşması bağımsız doğrulama değildir. D01, kaynak kimliğine bağlı sentetik yerel bir denetçi tanısıdır; canlı Claude veya bütün E19 doğrulaması değildir.

İki tarafın da okuyabildiği Research reposunda yayımlanan varyant tasarımcıdan gizli kabul edilmez. Hash/gzip bütünlük taşır, erişim izolasyonu sağlamaz. Gerçek holdout için actual görünürlük düzeni gösterilmeli; gösterilmediyse körlük açık kalır. Şeffaf tanı örnekleri, sonradan yeni varyantlar ve gerçek kullanım kanıtı ayrı tutulur.

Bu kanal hedefte yazmayı engelleyen kapı değildir. Bir mesajdaki alıntı veya “kullanıcı onayladı” beyanı yetkiyi genişletmez. Hedefte kaydedilmiş kullanıcı molası, Research'ün bir review yayımlamasıyla kalkmaz. Yeni uygulama/ücretli koşu/otomasyon gerçek yetki gerektirir.

## Tetik sınırı

Repo kalıcı aktarım sağlar; yeni ChatGPT/Claude oturumunu kendiliğinden başlatmaz. Webhook, Actions, polling, zamanlanmış görev veya ajan döngüsü kurulmadı. Kullanıcı içerik taşımak yerine gerektiğinde ilgili oturumu tetikler. C-001, R-001'i exact kimlikle alıp özgün hedefte yayımlama ve Research'ün geri alma yolunu gösterdi; R-002'nin alımı ancak C-002 veya başka gerçek alındı ile kapanır.

Erişim başarısızsa gerçek path/ref/hata sınırı kaydedilir, kullanıcıdan kayıp içeriği teknik olarak yeniden kurması beklenmez. Açılışın değişmeden kalan exact anlaşması [85076c2/EXCHANGE](https://github.com/batuhanozgun/agentic-os-search/blob/85076c2634be5ecfa7b16bbe8b8b23821baaac1c/development-os/attempts/001/EXCHANGE.md)'tedir; bu güncelleme ilk alımı ve deney görünürlüğü sınırını ekler.
