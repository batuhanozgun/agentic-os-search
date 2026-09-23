# SOUL Research

Bu repository altı farklı rolü birbirine karıştırmadan taşır.

| Alan | Amaç | Giriş |
|---|---|---|
| Agent control | Assistant'ın muhakeme ve davranış kuralları | [AGENT.md](AGENT.md) |
| Araştırma | Foundation, bağlam ve aday araştırma kütüphanesi | [research/INDEX.md](research/INDEX.md) |
| Terim çıkarımı ve ortak referans | Önce studies araştırmalarındaki kullanımların kendi bağlamlarında tam okumayla çıkarılması; bütün çıkarımlar tamamlandıktan sonra ortak değerlendirme | [concepts/INDEX.md](concepts/INDEX.md) |
| Düşünce ve Model Denemeleri | Diyalog, kavramsal prova, taslak model, görselleştirme ve öğrenme izleri | [explorations/INDEX.md](explorations/INDEX.md) |
| Development OS denemeleri | Development OS'u kuracak çalışma düzeninin deneme bazında yönetimi, aktörler arası görüşme, kanıtlı değerlendirme ve öğrenme | [development-os/INDEX.md](development-os/INDEX.md) |
| Yayınlar | Batuhan Özgün’ün yayımlanmış AI yazılarının kaynak bağlantılı metin arşivi | [publications/linkedin/README.md](publications/linkedin/README.md) |

## Otorite ayrımı

`AGENT.md` ve `agent/**` kontrol alanıdır. `research/**`, `concepts/**`, `explorations/**` ve `development-os/**` proje çalışma malzemesidir. `publications/**` yayımlanmış metinlerin kaynak arşividir; içerikleri kendiliğinden agent talimatı veya kabul edilmiş araştırma sonucu olmaz. Bir denemedeki öneri, rol canlandırması veya örnek yönerge kendiliğinden etkin sistem kuralı değildir.

Araştırmanın güncel yetkisi ilgili STATE dosyalarından okunur. Development OS denemelerinin koordinasyonu kendi WORK kaydında, hedefteki gerçek teknik iş kendi reposunda kalır. Bir denemenin arşivlenmesi Foundation'ın kabul durumunu, Development OS'nin görevini veya SOUL'un mimarisini değiştirmez.

## Development OS — deneme-001

[DEVOS-001](development-os/attempts/001/WORK.md), kullanıcının son 23 Eylül yönüyle bütün korpus okumasına yeniden yönlendirildi: önce bütün repo incelenir, her tur katkı sağlayacak fikir ve örnekler kaynak-bağlı kaydedilir; bütün kayıtlar tamamlandıktan sonra birlikte değerlendirilerek Development OS'u kuracak çalışma yapısına karar verilir. [METHOD](development-os/attempts/001/METHOD.md) bu sırayı, [COVERAGE](development-os/attempts/001/reading/COVERAGE.md) gerçek okuma kapsamını taşır. Önceki R-003/M1–M3/E19 revizyon zinciri aktif iş değildir; tarihçe korunur. Güncel durum yalnız WORK'ten alınır. Yeni hedef repo veya 002/003 açılmadı.

## Concepts — yeni başlangıç

2026-09-19 konuşmasıyla yeni çalışma sıfırdan kurulur. Önceki concepts tanımları, sınıflandırmaları, yöntem kararları ve ilerleme kayıtları geçerli başlangıç veya devam noktası değildir. Kaynak talep [ORIGIN](concepts/ORIGIN.md), amaç ve iki çalışma riskinin nedenleri [CHARTER](concepts/CHARTER.md), güncel aşama/yetki [STATE](concepts/STATE.md) içindedir.

Yeni oturumda [INDEX](concepts/INDEX.md) içindeki tam okuma yolu izlenir. Hazırlık, iki konuşma içi deneme, yöntem revizyonları, kalıcı araştırma bazlı çıkarım ve bütün çıkarımlardan ortak değerlendirme ayrı aşamalardır. Dosyaların varlığı denemelerin yapıldığı veya ortak tanımların kabul edildiği anlamına gelmez. Özgün studies araştırmaları ve tarihsel arşivler yeni yönteme uydurulmak için yeniden yazılmaz.

## İlk kavramsal deneme

[EXP-001 — SOUL'un çalışma modeli](explorations/EXP-001-soul-calisma-modeli/INDEX.md): A–B–C, Work–Information etkileşimi, aktör hazırlığı, uzmanlık sürekliliği, Mekanizma Atlası ve yaşayan katmanlı plan ihtiyacı.

Arşivin tamlığı için her zaman paket [STATE](explorations/EXP-001-soul-calisma-modeli/STATE.md) kaydına bakılır; dizinin bulunması bütün kaynakların yayımlandığı anlamına gelmez.
