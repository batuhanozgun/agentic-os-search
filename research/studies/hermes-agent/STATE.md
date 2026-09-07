# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / INITIAL ORIENTATION AND FIRST MECHANISM PASS RECORDED  
**Son çalışma tarihi:** 2026-09-07  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN.md](RESEARCH-PLAN.md), v0.2  
**Araştırma tamamlandı mı?** HAYIR. İlk kaynak turu kaydedildi; bütün sistem sentezi ve kapanış incelemesi yapılmadı.

## Yetkilendirilmiş amaç ve kapsam

Kullanıcı HERMES araştırmasını başlatmamızı, önce bilgi toplayarak dipten yukarı bir araştırma planı geliştirmemizi, araştırmayı yürütmemizi ve yeni kanıta göre planı revize etmemizi istedi. Yetki araştırma ve bu study'nin kalıcı kaydı içindir; her iç okuma grubu için yeni izin gerekmez.

OpenClaw ayrı sonraki araştırma adayıdır; bu paketin genişleyen ikinci araştırma nesnesi değildir. HERMES'in OpenClaw migration kodu kendi ürün sınırı içinde gerekirse incelenebilir. Kurulum, provider çağrısı, hesap/credential kullanımı, Codex görevi, Foundation aktivasyonu veya benimseme bu yetkinin parçası değildir.

## Yapılan iş

1. Güncel araştırma durumu ve diğer hatların sınırları kontrol edildi. Preflight araştırma ref'i `4cb42472e3e8391f91836c5f4518db3fc30b89af`; önceki `b62c9d...` ile fark yalnız context köprüsünün dört dosyasındaydı. Gstack METHOD/META tam okundu.
2. Upstream commit/tree sabitlendi. Kök tree ve `apps/` tree listeleri tam alındı; **recursive bütün repository envanteri çıkarılmadı**.
3. README, mimari rehber, bellek rehberi ve güvenlik politikası tam okundu. Manifest ve memory-manager üzerinde seçici okuma yapıldı.
4. Arka plan review, beceri yazma korumaları, yazım kökeni, yazma-onay altyapısı ve ortak onay komutları tam okundu. İki ilişkili test dosyası tam kaynak olarak incelendi.
5. İlk mekanizma notu, kaynak defteri, kapsam haritası ve planın ilk revizyonu kaydedildi.

Tam/kısmi okuma ayrımının kaydı [SOURCE-LEDGER.md](SOURCE-LEDGER.md)'dir. Dosya sayısı veya kod satırı araştırma tamamlanma yüzdesi değildir.

## Henüz kurulmamış olan

- Tüm önemli kaynak ailelerinin alt envanteri ve bağımlılık kapanışı.
- Review tetiklenmesi → gerçek dispatch → mutasyon → onay sonrası replay → sonraki oturumda yeniden kullanım zincirinin bütün ilgili yolları.
- Öğrenilmiş becerilerin gerçekten daha doğru/yararlı olduğuna dair sonuç değerlendirmesi.
- Gateway, cron, delegation, provider, UI ve kurulum yaşam döngülerinin kaynak temelli sentezi.
- Native sistem modeli, dört-alan projeksiyonu, SOUL/Development OS değerlendirmesi ve omission/distortion kapanışı.

## Sıradaki yetkili iş

**U01 devamı — arka plan öğrenmesinin uçtan uca çağrı ve kalıcılık zinciri.**

Önce tetikleyici/caller ve ana tool-dispatch yolunu izle; ardından `tools/skill_manager_tool.py`, `tools/memory_tool.py`, ilgili store/provenance/ledger yardımcıları ve `apply_*_pending` yollarına in. Onay anında hedefin/kökenin nasıl yeniden değerlendirildiğini ve sonraki oturumun neyi gerçekten yüklediğini araştır. Sonra curator ve paylaşım/sync yollarını ayrı birimler olarak aç. Kaynaklar [plan](RESEARCH-PLAN.md) ve [açık sorularda](OPEN-QUESTIONS.md) adlandırılmıştır; dosya adı henüz okunmuş olmak değildir.

Her birimde kod + ilgili test + en güçlü karşı yol incelenir. Yeni bir birincil mekanizma görülürse planın aileleri bölünebilir/birleşebilir; sabit başlık sayısı korunmaya çalışılmaz.

## Yeni oturum girişi

Canonical agent bootstrap → `research/INDEX.md` → `research/studies/CATALOG.md` → bu paketin META/STATE/INDEX dosyaları. Sonra METHOD, güncel plan, ilgili not ve kaynak defterindeki ilgili kayıtlar okunur; iddia taşıyan kaynaklar pinned ref'ten geri açılır. Diğer çalışma hatlarının güncel yetkisi yalnız kendi STATE dosyalarındadır, burada kopyalanmaz.

## Doğrulama ve durma sınırı

Bu tur statik kaynak okumasıdır. Upstream yazılım kurulmadı, çalıştırılmadı; test suite veya canlı model görevi yürütülmedi. Test dosyalarının varlığı başarılı test koşusu değildir. Değerlendirme aynı asistan tarafından yapılmıştır; bağımsız yeniden araştırma değildir.

Bir araştırma birimi kanıt sınırıyla kaydedilmeden daha üst senteze yükseltilmez. Bütün araştırmanın bitiş koşulları METHOD'dadır. Maddi erişim veya yetki çelişkisi çıkarsa etkilenmeyen bulgular korunur ve sorun açık bırakılır. Bu STATE arka planda çalışan bir ajan veya geleceğe zamanlanmış işlem başlatmaz.
