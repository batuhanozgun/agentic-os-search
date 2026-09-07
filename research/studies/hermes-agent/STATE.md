# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / INITIAL ORIENTATION, BACKGROUND-REVIEW AND SKILL-CURATION SOURCE PASSES RECORDED  
**Son çalışma tarihi:** 2026-09-07  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN.md](RESEARCH-PLAN.md), v0.3  
**Araştırma tamamlandı mı?** HAYIR. U01 ve U01-C kısmi kaynak birimleridir; bütün sistem sentezi ve kapanış incelemesi yapılmadı.

## Yetkilendirilmiş amaç ve kapsam

Kullanıcı HERMES araştırmasını başlatmamızı, önce bilgi toplayarak dipten yukarı bir araştırma planı geliştirmemizi, araştırmayı yürütmemizi ve yeni kanıta göre planı revize etmemizi istedi. Yetki araştırma ve bu study'nin kalıcı kaydı içindir; her iç okuma grubu için yeni izin gerekmez.

OpenClaw ayrı sonraki araştırma adayıdır; bu paketin genişleyen ikinci araştırma nesnesi değildir. HERMES'in OpenClaw migration kodu kendi ürün sınırı içinde gerekirse incelenebilir. Kurulum, provider çağrısı, hesap/credential kullanımı, Codex görevi, Foundation aktivasyonu veya benimseme bu yetkinin parçası değildir.

## Yapılan iş — birikimli kayıt

1. İlk tur güncel araştırma durumu ve diğer hatların sınırlarını kontrol etti. İlk preflight araştırma ref'i `4cb42472e3e8391f91836c5f4518db3fc30b89af`; önceki `b62c9d...` ile fark yalnız context köprüsünün dört dosyasındaydı. Gstack METHOD/META tam okundu.
2. Upstream commit/tree sabitlendi. Kök tree ve `apps/` tree listeleri tam alındı; **recursive bütün repository envanteri çıkarılmadı**.
3. İlk tur README, mimari rehber, bellek rehberi ve güvenlik politikasını tam okudu; manifest ve memory-manager üzerinde seçici okuma yaptı.
4. İlk tur arka plan review, beceri yazma korumaları, yazım kökeni, yazma-onay altyapısı ve ortak onay komutlarını tam okudu; iki ilişkili test dosyasını tam kaynak olarak inceledi. [02-BACKGROUND-LEARNING](notes/02-BACKGROUND-LEARNING.md) bu kesiti korur.
5. Ek turda mevcut paket `e6bc6cd98e31922c4cfd1c3b46e88c04aec2ca00` üzerinden tam geri kazanıldı; ikinci paket açılmadı. İlk ek okumalarının ref'i `d8a077...`, mevcut pin ile bir-commit karşılaştırmasıyla uzlaştırıldı; ilgili dosya içerikleri değişmemişti. Birincil pin korunur.
6. Curator orchestrator, skill usage/policy/lifecycle, ilgili kullanıcı belgesi ve upstream geliştirici rehberleri tam okundu; skill guard yeniden açıldı. Curator testinde 1–440, skill-manager tool'da 1–200 ve 801–EOF seçildi. [03-SKILL-CURATION](notes/03-SKILL-CURATION.md) yeni bulguları, belge/guard farklarını ve açık kanıt sınırını taşır.
7. Yayın öncesi research HEAD `408ee3ce7b25e873d2537ad44950249aa213cb06` olarak yeniden okundu. e6bc6cd... sonrasındaki iki commit yalnız context köprüsündeydi; bu ek onların üzerine, onları koruyacak biçimde hazırlanmıştır. Hermes ve catalog dışındaki dosyalara değişiklik verilmez.

Tam/kısmi okuma ve ilk/ek tur ayrımı [SOURCE-LEDGER.md](SOURCE-LEDGER.md)'dedir. Eski kaydın yeniden okunması bütün eski upstream kaynaklarının yeniden okunması anlamına gelmez. Dosya sayısı veya kod satırı araştırma tamamlanma yüzdesi değildir.

## Henüz kurulmamış olan

- Tüm önemli kaynak ailelerinin alt envanteri ve bağımlılık kapanışı.
- Review tetiklenmesi → gerçek dispatch → mutasyon → onay sonrası replay → sonraki oturumda yeniden kullanım zincirinin bütün ilgili yolları.
- Curator prompt/guard farklarının actual single-op/batch/apply yollarındaki sonucu; backup/ledger/cron/sync bağımlılıklarının bütünlüğü.
- Öğrenilmiş veya birleştirilmiş becerilerin gerçekten daha doğru/yararlı olduğuna dair sonuç değerlendirmesi.
- Gateway, cron, delegation, provider, UI ve kurulum yaşam döngülerinin kaynak temelli sentezi.
- Native sistem modeli, dört-alan projeksiyonu, SOUL/Development OS değerlendirmesi ve omission/distortion kapanışı.

## Sıradaki yetkili iş

**U01 devamı + U01-C'nin mutasyon bağlantısı.** İlk somut kaynak adımı `tools/skill_manager_tool.py` 201–800 aralığıdır; ardından çağrılan `tools/skill_manager_batch.py`, gerçek dispatch, `apply_skill_pending` ve ilgili testler izlenir. Şemadaki batch `operations` biçimi ile curator raporunun argüman yorumunun ilişkisi ayrıca sınanır.

Sonra ilk U01'de açık kalan trigger/caller, memory mutator, pending replay, source-origin, cancellation/store, ledger/backup ve sonraki session/skill-load yollarına dönülür. Curator'ın cron referansı ve update/sync etkileri ilgili ailelere bağlanır. Bu sıranın değişmesi gerektiğinde neden kaynakla kaydedilir; diğer büyük aileler U01'in ayrıntıları haline getirilmez.

Son H22 201–400 okuması GitHub 429/fail-fast yanıtıyla içerik getirmedi; 201–800 hâlâ okunmamıştır. Bu, kalıcı GitHub erişim yokluğu veya HERMES'in çalışmadığı iddiası değildir; daha sonra research-repo yayın preflight'ı başarıyla yapılmıştır. Yeni oturum kaldığı aralığı biliyor, eksik kaynağı tahmin ederek devam etmiyor.

Her birimde kod + ilgili test + en güçlü karşı yol incelenir. Yeni bir birincil mekanizma görülürse planın aileleri bölünebilir/birleşebilir; sabit başlık sayısı korunmaya çalışılmaz.

## Yeni oturum girişi

Canonical agent bootstrap → `research/INDEX.md` → `research/studies/CATALOG.md` → bu paketin META/STATE/INDEX dosyaları. Sonra METHOD, güncel plan, ilgili mekanizma notu ve kaynak defterindeki ilgili kayıtlar okunur; iddia taşıyan kaynaklar pinned ref'ten geri açılır. Diğer çalışma hatlarının güncel yetkisi yalnız kendi STATE dosyalarındadır, burada kopyalanmaz.

## Doğrulama ve durma sınırı

Kayıtlı araştırma statik kaynak okumasıdır. Upstream yazılım kurulmadı, çalıştırılmadı; test suite veya canlı model görevi yürütülmedi. Test dosyalarının varlığı başarılı test koşusu değildir. Değerlendirme aynı asistanın source review'udur; bağımsız yeniden araştırma değildir. Curation notundaki koşul uyuşmazlığı ve değişiklik baskısı farklı epistemik statülerdedir; canlı hata veya kalite kaybı oranına yükseltilmez.

Bir araştırma birimi kanıt sınırıyla kaydedilmeden daha üst senteze yükseltilmez. Bütün araştırmanın bitiş koşulları METHOD'dadır. Maddi erişim veya yetki çelişkisi çıkarsa etkilenmeyen bulgular korunur ve sorun açık bırakılır. Bu STATE arka planda çalışan bir ajan veya geleceğe zamanlanmış işlem başlatmaz.
