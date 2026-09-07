# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / BACKGROUND-REVIEW, SKILL-CURATION AND U01B COMPONENT EVIDENCE RECORDED  
**Son kayıt tarihi:** 2026-09-07  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN.md](RESEARCH-PLAN.md), v0.4  
**Araştırma tamamlandı mı?** HAYIR. Kaynak ve dar bileşen kesitleri kaydedildi; bütün sistem sentezi, kalite doğrulaması ve kapanış incelemesi yapılmadı.

## Yetkilendirilmiş amaç ve kapsam

Kullanıcı HERMES araştırmasını başlatmamızı, önce bilgi toplayarak dipten yukarı bir araştırma planı geliştirmemizi, araştırmayı yürütmemizi ve yeni kanıta göre planı revize etmemizi istedi. Yetki araştırma ve bu study'nin kalıcı kaydı içindir; her iç okuma grubu için yeni izin gerekmez.

OpenClaw ayrı sonraki araştırma adayıdır; bu paketin genişleyen ikinci araştırma nesnesi değildir. HERMES'in OpenClaw migration kodu kendi ürün sınırı içinde gerekirse incelenebilir. Kurulum, provider çağrısı, hesap/credential kullanımı, Codex görevi, Foundation aktivasyonu veya benimseme bu yetkinin parçası değildir.

## Yapılan iş — birikimli kayıt

1. İlk tur güncel araştırma durumu ve diğer hatların sınırlarını kontrol etti. İlk preflight ref'i `4cb42472e3e8391f91836c5f4518db3fc30b89af`; önceki b62c9d... ile fark yalnız context köprüsünün dört dosyasındaydı. Gstack METHOD/META tam okundu.
2. Upstream pin/tree sabitlendi. Kök ve apps tree listeleri alındı; recursive bütün repository envanteri henüz yok. README, mimari/bellek/güvenlik belgeleri; background review, guard, provenance, approval ve ilgili iki testin kaynakları okundu. [02-BACKGROUND-LEARNING](notes/02-BACKGROUND-LEARNING.md) bu kısmi mekanizmayı taşır.
3. Curator turu mevcut paketi e6bc6cd... üzerinden geri kazandı; d8a077... ek kaynak ref'i ilgili aynı blob'larla uzlaştırıldı. Curator, skill usage/policy/lifecycle, kullanıcı/geliştirici rehberleri tam; curator testi 1–440 ve skill mutator'ın iki dış kesiti seçili okundu. [03-SKILL-CURATION](notes/03-SKILL-CURATION.md) korunur. O turun son H22 201–400 isteği 429 ile içerik getirmemişti; bu tarihsel erişim sonucu kalıcı kabiliyet yokluğu değildir.
4. Ayrı U01B çalışma dilimi S01/H22 skill mutator'ı bütünüyle, batch kaynağını ve testini tam okudu; approval/komut yollarını yeniden açtı. İki exact upstream modülü ve açık dependency stub'larıyla 10 sentetik tanılayıcı durum çalıştırdı. O tur GitHub yazma eylemi sunulmadığını bildirerek sonucu sohbet dosyası/ZIP olarak teslim etti. Araştırma bulgusu vardı; repository yayın halkası açıktı.
5. Bu kayıt turunda mevcut main `000f691b9a94607c9a8219961b4618eda0f1014f` ve güncel HERMES yüzeyleri okundu. Teslim ZIP'inin 13 manifest girdisi byte/SHA-256 ile kontrol edildi. Yazma eylemleri yeniden keşfedilip kullanıldı; eksik U01B not/kanıtları mevcut curator çalışmasının üzerine, onu koruyarak birleştirildi. Yerel önerinin v0.3 adı mevcut v0.3'ü ezmedi; canonical plan v0.4 oldu. [04-SKILL-WRITE-TRANSACTION-AND-APPROVAL](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [kanıt](evidence/2026-09-07-u01b/component-probe/README.md), [aktarım](evidence/2026-09-07-u01b/PUBLICATION.md).

Birikimli okuma defteri [SOURCE-LEDGER.md](SOURCE-LEDGER.md)'dir. Eski kaynak okuması veya deney, aktarım turunda yeniden yapılmış gibi sayılmaz. Dosya/test sayısı araştırma tamamlanma yüzdesi değildir.

## Yeni kanıtın statüsü

U01B'de normal hata/bozuk JSON rollback'i, fırlatılan istisna ve restore hatası farklı sonuç verdi; ortak preview fonksiyonunda batch ve full-rewrite biçimleri farklı karşılandı; pending rename hatasında kimlik dönmesi geri bulunabilir kayıt üretmedi. Bunlar exact iki bileşen + sentetik bağımlılıklar kapsamındadır. Dış caller, tüm UI'ler, gerçek ledger/sync veya üretim hata oranı doğrulanmadı.

Deney kaydı UTC `2026-09-07T09:35:13.772427+00:00`, Python 3.13.5/Linux'tur. Bu aktarım turunda yeniden koşturulmadı. Önceki statik curator/review turları statik kalır; bu ayrı bileşen deneyi onları veya tüm sistemi runtime-verified yapmaz. Hash kontrolü aktarım bütünlüğünü destekler, bağımsız yürütme doğrulaması değildir.

## Sıradaki yetkili iş

**U01'in gerçek caller/dispatch/context zinciri ve U01-C curator bağlantısı.** H22'nin 201–800 aralığı artık birikimli kayıtta eksik değildir: U01B/S01 tam okumaya bağlanır. Aynı bölümü sırf eski STATE öyle diyordu diye ilk kez okuyormuş gibi başlatma; yük taşıyan iddia için gerektiğinde kaynağa geri dön.

İlk somut soru: review/foreground/curator → gerçek tool invoke → exception handling → pending apply sırasında hangi origin/profile/authority bağlamı taşınıyor? U01B'nin bileşen sınırlarını gerçek caller'a bağla; U01-C raporunun batch operations diliyle ilişkisini de burada sına. Ardından memory mutator, trigger/cancellation/store, ledger/backup/restore/sync ve sonraki session/skill/cache-load yollarını tamamla. Kaynak bağımlılığı sıra değiştirmeyi gerektirirse gerekçe plana yazılır.

## Henüz kurulmamış olan

- Tüm önemli kaynak ailelerinin alt envanteri ve bağımlılık kapanışı.
- Review → dispatch → mutation → approval replay → sonraki kullanım zincirinin bütün ilgili yolları.
- Curator prompt/guard/report farklarının bütün gerçek caller ve etkilerdeki sonucu.
- Öğrenilmiş veya birleştirilmiş becerilerin gelecek görev kalitesini artırdığına dair yeterli değerlendirme.
- Gateway, cron, delegation, provider, UI, environment ve kurulum/değerlendirme yaşam döngülerinin sentezi.
- Native sistem modeli, dört-alan projeksiyonu, SOUL/Development OS değerlendirmesi ve omission/distortion kapanışı.

## Yeni oturum girişi ve durma sınırı

Canonical agent bootstrap → research root → studies katalog → bu paketin META/STATE/INDEX → METHOD ve güncel plan → ilgili 02/03/04 notu ve kaynak defteri. Notların iddiaları gerektiğinde pinned kaynaktan yeniden açılır. Diğer çalışma hatlarının yetkisi yalnız kendi STATE dosyalarındadır; burada kopyalanmaz.

Yazma erişiminin önceki turda neden farklı sunulduğu doğrulanmadı; kullanıcı ayarı veya izin hatası varsayılmaz. Sohbet ekleri bir kurtarma teslimiydi, yeni canonical çalışma yeri değildir. Kullanıcının ZIP'i elle taşıması, Codex'te işlem yapması veya kurulum yapması gerekmez. Araştırma için mevcut yetki sürer; yanıtlar arasında otomatik/background çalışma başlatılmaz.

Bir birim açık kanıt sınırlarıyla kaydedilmeden üst senteze yükseltilmez. Erişim/yetki çelişkisinde etkilenen kısım durur, diğer kanıtlar korunur. Çalışmanın bitiş ölçütü METHOD'dadır. Bu yayın Foundation, context/Codex, agent-control veya başka study'leri değiştirmez.
