# DEVOS-002 — yeni konuşma için başlangıç kaydı

**Açılış:** 24 Eylül 2026.
**Durum:** KONUŞMA AKTİF / MİKRO-ADIMLI ÇERÇEVELEME. Yöntem, iş planı, mimari ve uygulama kararı hâlâ verilmedi.
**Şimdiki taraflar:** Batu ve ChatGPT / Research.
**Hedef yeni repo:** Kullanıcı Claude için yeni repo açacağını söyledi. Adı, adresi ve açıldığı bilgisi henüz verilmedi; burada repo oluşturulmadı.

## Neden buradayız?

Konu, Development OS'u kurabilecek çalışma düzeninin nasıl ele alınacağı. Kullanıcı önceki ilerlemeyi durdurdu ve 002'yi ayrı bir başlangıç olarak istedi. Önce yeni oturumda Batu ile ChatGPT konuşacak; ne yapılacağı birlikte belirlenecek. Bu dosya o konuşmanın bağlamıdır, çözümü veya planı değildir.

## Son kullanıcı mesajı — aynen

> Dur dur o çalışıyor şu anda. Böyle olmayacak ya. Çok büyük iş yapmaya çalışıyorsunuz. Ben claude’a yeni repo açacağım. Ve sen de yeni çalışma aç. Önce senine biz konuşalım ne yapacağımız. Attempts altında 002’ye başlıyoruz. Ama hiçbir karar vermedik sadece yeni oturumda seninle bu konuyu konuşacağımız şekilde işi bırak repoya yeni konuşmada birlikte karar vereceğiz konuşarak.

Hemen önceki soru, yalnız bağlam olarak korunur; kabul edilmiş bir ajanlar-arası yöntem değildir:

> Ya bu işi adım adım konuşarak ne yapsak nasıl kursak diye birbirnizle konuşarak yapamaz mısınız?

## Yeni oturumun devam noktası

Kullanıcının yeni mesajını bu kayıtla birlikte ele al; ne yapılacağını adım adım konuşarak belirle. Hazır bir mimari, görev dağılımı, okuma kampanyası veya uygulanacak planla başlama. Kullanıcıya önceki konuşmayı yeniden anlatma veya eski araştırmaları tekrar okuma yükü verme.

Henüz neyin kurulacağı, hangi kapsam/yöntemle ilerlenileceği, aktörlerin nasıl çalışacağı, hangi örneklerin seçileceği ve Claude'un ne zaman/nasıl dahil edileceği kararlaştırılmış değil. Bu konular için burada görev kuyruğu, aşama kapısı veya teknik tercih üretilmedi. Yeni repo adını tahmin etme; 001'in hedefini yeni hedefmiş gibi kullanma.

## 001 ile sınır

[001'in Research devamı duraklatıldı](../001/WORK.md). Onun D1/D2 tasarımı, yöntemleri, okuma yükümlülükleri, bekleyen R/C mesajları ve izinleri 002'ye taşınmadı. Önceki kayıtlar silinmedi; daha sonra gerekli bulunursa kaynak olarak ele alınabilir. 001'in tamamını yeniden okumak bu yeni konuşmanın başlangıç koşulu değil.

Kullanıcı Claude'un çalıştığını bildirdi. Bu tur Claude'un reposuna/oturumuna müdahale edilmedi ve yeni mesaj gönderilmedi; durmuş veya yeni yönü almış sayılmaz. 002 açılışı, 001 hakkında başarı/başarısızlık hükmü değildir.

## Bu açılışta yapılan tek iş

Bu başlangıç kaydı oluşturuldu; kök README ve development-os INDEX yeni konuşmaya yönlendirildi; 001 WORK Research duraklamasını kaydetti. Araştırma, tasarım, kod/kurulum, test, yeni GitHub reposu veya otomasyon başlatılmadı. Sonraki içerik, yeni konuşmada birlikte alınacak kararlara göre oluşacak.


## 24 Eylül 2026 — konuşma checkpoint'i

**Statü:** PROVISIONAL DISCUSSION STATE / NOT ARCHITECTURE / NOT IMPLEMENTATION AUTHORITY.

Kullanıcı üst amacı bu konuşmada açıkça **SOUL'u yaratmak** olarak yeniden sabitledi ve yönteme atlamadan önce SOUL'un ne olduğunun adının konmasını istedi. Repository'deki mevcut kaynaklar üzerinden kullanılan çalışma adı:

> **SOUL = genel amaçlı bir Çalışma Sistemi Kurucusu / general-purpose work-system former.**

Bu, nihai ürün tanımı veya kabul edilmiş mimari değildir; sonraki tartışmayı doğru problem seviyesinde tutan working label'dır.

**Kaybedilmemesi istenen açık soru:**

> **Bir şey gerçekten çalışma sistemi kurucusu olacaksa ne yapabilmesi gerekir?**

Kullanıcı bu soruyu cevaplamadan önce SOUL'un nerede çalışacağını, yani kendi Environment'ini konuşmayı seçti. Şimdiki ayrım:

- **SOUL Host Environment:** SOUL'un kendisinin fiilen çalıştığı teknik destek ortamı.
- **Task-specific Work Environment(s):** SOUL'un kullanıcı işi için oluşturduğu veya bağlandığı çalışma ortamları.

Foundation Environment araştırması nedeniyle host, yalnız bilgisayar/cloud/runtime/tool listesi olarak tanımlanmaz. Fiziksel olarak tek yerde bulunması da gerekmeyebilir. Bu turda ürün, provider, deployment modeli, model, database, container, sandbox veya başka teknoloji seçilmedi.

Host için minimum affordance/primitives listesi bu konuşmanın şu anki alt sorusudur; assistant'ın çıkaracağı aday liste kullanıcı değerlendirmesi öncesinde kabul edilmiş gereksinim sayılmaz. Önceki açık soru bunun ardından geri alınacaktır.


## 24 Eylül 2026 — yön düzeltmesi

**Kullanıcı düzeltmesi:** Bu konuşmanın amacı teknik ürünleri tek tek öğrenmek değildir. Batu teknik ayrıntıları bilmediği için assistant, seçenek alanını ve gerekli ayrımları görünür kılmalı; fakat her yeni terimi ayrı bir araştırma dalına dönüştürmeden ana amacı korumalıdır.

**Ana amaç:** SOUL'u yaratmak için önce SOUL'un ne olduğuna ve bundan hangi zorunlu özelliklerin çıktığına adım adım karar vermek.

**Korunan çalışma adı:** SOUL = genel amaçlı bir Çalışma Sistemi Kurucusu.

**Korunan ana açık soru:** “Bir şey gerçekten çalışma sistemi kurucusu olacaksa ne yapabilmesi gerekir?”

**Environment dalının amacı:** Bu ana soruya geçmeden önce SOUL'un fiilen hangi tür çalışma zemini üzerinde yaşayabileceğini anlamak. Tartışma üç kavramsal seçenek ortaya çıkardı: mevcut agent hostunu genişleten yapı (gstack/ECC tarafı), kendi agent runtime'ı olan bağımsız yapı (Hermes/OpenHands türü), veya hibrit düzen. Bunlardan hiçbiri seçilmedi.

**Drift kaydı:** ECC'nin hook/session/operator ayrıntılarına ilerlemek, Environment dalının karar ihtiyacını aştı. ECC burada yalnız seçenek alanını somutlaştıran örnek olmalı; ayrı ECC araştırmasına dönülmemeli.

**Sonraki doğru mikro-adım:** Batu'dan teknik tercih istemek yerine, üç runtime/host modelini SOUL'un “genel amaçlı Çalışma Sistemi Kurucusu” hedefi açısından karşılaştırıp hangi kararın şimdi verilmesi gerektiğini ve hangisinin ertelenebileceğini belirlemek. Ardından korunmuş ana soruya geri dönmek.
