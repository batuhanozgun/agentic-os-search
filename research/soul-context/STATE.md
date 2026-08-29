# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 6 — SOUL'a geçiş kronolojisini yeniden kurma  
**Son güncelleme:** 2026-08-29

## Ana hedef

Üç kaynak repoyu sistematik okuyarak SOUL Research projesinin gerçek araştırma niyetini yeniden kurmak; erken mimari çözüm üretmemek.

## Kaynak repoların rolleri

- `soul`: current explicit intent anchor.
- `os-architect`: tarihsel arıza, karar, yöntem, araştırma ve KEEL geliştirme bağlamı.
- `keel`: bugünkü somut ürün/mekanizma yüzeyi.

## Tamamlanan geçişler

### A — çalışma düzeni ve araştırma yöntemi

Doğrulanan ana problem katmanları:
- depo/temsil failure'ı,
- çalışma-döngüsü failure'ı,
- epistemik süreç failure'ı.

### B — KEEL problem ve kanıt modeli

Kanıt statüleri ayrıldı:
- gözlenen arıza/saha olayı,
- ölçüm/tatbikat,
- tasarım hükmü,
- dış yakınsama.

KEEL güvenlik sınırı değil; savruk/onay-arayışlı ajan için işletim disiplini olarak çerçeveleniyor. Tarihsel doğrulama/koruma mekanizmaları davranış anti-defolarından daha güçlü.

### C — önceki araştırma ve dış-göz kayıtları

Araştırma seansının altı kaleminden yalnız 1, 2 ve 6'nın repo ayağı tamamlanmış; 3–5 araştırılmış sayılmıyor.

Önceki araştırmanın yönü:
- soru ≠ görev,
- gerçek amacı/öncülü icradan önce yeniden türetme,
- uzman–sahip asimetrisi,
- oturumların sonucu taşıyıp sebebi/amacı kaybetmesi,
- sorgulama için `üreteç + tetik + kanıt zinciri`,
- dersin ihtiyaç anına ulaşmaması.

2026-08-11 gstack kaydında sahibi tarafından "araştırma evi kurulacak" ve araştırmaların sonraki yeni geliştirme çalışmasına girdi olacağı yönü verilmiş; bu bir D-numaralı mühürlü karar değil.

### D — KEEL öz-anlatısını bugünkü mekanikle karşılaştırma — SEÇİCİ TAMAMLANDI

Doğrudan kod/sözleşme/test yüzeyinde görülenler:

1. **State / devam:** `GENESIS_DURUM` tek makine bloğu; `kurulum-surucu.sh` bozuk/eksik/atlanan state'i fail-closed engelliyor ve sıra tutarlılığını ölçüyor.
2. **Hook wiring:** `.claude/settings.json` file-guard, kurulum sürücüsü, açılış, kapanış, sevk ve SubagentStop zarf kapısını gerçek Claude Code hook olaylarına bağlıyor.
3. **Rol kafesi:** `file-guard.sh`, `yazamaz` rolün kendi evi dışına yazmasını ve kendi `ROL.md` sözleşmesini değiştirmesini engelliyor; bozuk rol damgasında yazma güvenli tarafta kesiliyor.
4. **Doğrulayıcı ayrımı:** `dogrulayici` yalnız Read/Grep/Glob araçlarına sahip; dosya-gerçeği ayağı salt-okur.
5. **Karne/kapanış:** `sevk.sh`, bu dönemde üretilmiş kapalı görev için taze YEŞİL karne arıyor; yok/bayatsa doğrulayıcı çağırıyor. Kapanış karnesi son iş zarfından sonra taze olmalı; YEŞİL/KIRMIZI/DOĞRULANAMADI ayrı akışlar.
6. **Falsification tasarımı:** `tools/bekci/test/bozma.test.mjs`, temiz yeşilden sonra 9 kasıtlı mutasyonda bekçinin kırmızı/kilit üretmesini bekliyor.
7. **İnsan↔makine ayrımı:** state, bekçi makine satırı/exit code ve zarf/karne tazeliği gibi kritik yüzeylerde salt düzyazıdan daha açık makine sözleşmeleri var.
8. **Ders→ihtiyaç köprüsü:** ilk plan kutusu rol ihtiyaçlarını/kayıt düzenini çıkarıyor ve role özel `Açılış ek-okumaları` işaretçilerini güncelliyor; SessionStart belirli olayları hatırlatıyor. Bu kısmi mekanik köprü, genel semantik lesson retrieval değildir.

### D doğrulama sınırları

- Mutation test dosyalarının tasarımı okundu, ancak bu oturumda fresh execution yapılamadı: geçici çalışma ortamında GitHub ağı yoktu.
- KEEL release commit mesajı "deneme kurulumu 1202 test yeşil" diyor; bu commit-yazarı beyanıdır, bağımsız CI değildir.
- Aynı release commit'i için GitHub Actions workflow run görünmedi.
- Büyük scriptler iddia taşıyan bölümlerden seçici okundu; exhaustive full-code audit yapılmadı.
- Claude Code hook/runtime davranışı canlı harness üzerinde yeniden ölçülmedi.

## Şu ana kadarki yapısal problem haritası

1. **Depo/temsil:** bilgi şişiyor, kopyalanıyor, bulunamıyor veya farklı ömürler karışıyor.
2. **Çalışma yaşam döngüsü:** durum saklansa bile hareket, sorumluluk ve güncelleme yükümlülüğü taşınmayabiliyor.
3. **Epistemik süreç:** aynı kaynak/model/çerçeve sahte yakınsama; verifier körlüğü ve yalancı-yeşil sahte güven üretebiliyor.
4. **Amaç/çerçeve:** soru görev sanılıyor; öncül ve gerçek amaç icradan önce yeniden türetilmeyebiliyor. Oturumlar sonucu taşıyıp neden/amaç modelini kaybedebiliyor.
5. **Ders→mekanizma:** ders belge olarak kalıyor, ihtiyaç anına ulaşmıyor veya bir hatta uygulanıp kardeş hatta taşınmıyor.

## KEEL mekanik doğrulamasının ana anlamı

KEEL'deki temel ilkelerin önemli kısmı yalnız öz-anlatı değil; gerçek hook, parser, rol kafesi, karne akışı ve mutation test tanımlarıyla mekanikleşmiş.

Ama SOUL açısından üç sınır kritik:

- **runtime özgüllüğü:** birçok garanti Claude Code hook/tool modeline bağlı;
- **epistemik bağımsızlık:** ayrı koltuk ≠ ayrı model/ayrı çerçeve;
- **lesson retrieval:** işaretçi ve planlama disiplini güçlü ama geçmişteki doğru dersi yeni ihtiyaçta otomatik bulma genel problemi çözülmüş değil.

Bu yüzden KEEL'i SOUL'a kopyalamak yerine failure sınıflarını first principles'tan yeniden türetmek gerekebilir.

## Tarihsel yön sinyalleri — henüz nedensel sonuç değil

- 2026-08-08 dış-göz seansı: dünya standardı + alışılmadık/vizyoner problem çözme; KEEL akıl+teknik birlikte değerlendirilmeli.
- Aynı seans: daha fazla altyapı yerine görünmez varsayımları sözleşme/fixture/iz/kapsama ölçümüne dönüştürme yönü.
- 2026-08-10 araştırma seansı: çerçeve körlüğü ve "soru ≠ görev".
- 2026-08-11 gstack: "araştırma evi kurulacak"; araştırmalar sonraki yeni geliştirme çalışmasına girdi olacak (yön beyanı, mühürlü karar değil).
- 2026-08-12 KEEL v0.2 yayın commit'i.
- 2026-08-25 `soul` bootstrap: first-principles general-purpose agentic architecture; `development/` ve `system/` ayrımı; ilk paket Development OS.

## Çalışma hipotezleri — SONUÇ DEĞİL

H1. SOUL Research'ün temel niyeti yalnız yeni bir agent framework aramak değil; durumsuzluk, drift, öz-onaylama, bilgi ömrü, amaç kaybı ve doğrulama problemlerini daha genel bir agentic architecture seviyesinde first principles'tan yeniden ele almak olabilir.

H2. SOUL Development OS'nin problemi yalnız persistans değil; **amaç + iş yaşam döngüsü + güncelleme sorumluluğu + epistemik doğrulama + dersin ihtiyaç anına ulaşması** birlikte olabilir.

H3. KEEL'den SOUL'a aktarılabilir çekirdek, dosya/ritüel isimlerinden çok **failure → ölçüm → mekanizma → falsification → yaşam döngüsü** zinciri olabilir.

H4. Önceki araştırmalar "daha iyi düşün" öğüdünden çok sorgulamanın **üreteci + tetiği + kanıt zinciri** fikrine doğru ilerlemiş; SOUL bunun daha genel bir biçimini arıyor olabilir.

H5. 8–11 Ağustos dış-göz/araştırma çalışmaları ile 25 Ağustos SOUL bootstrap'ı arasında doğrudan tasarım devamlılığı olabilir; şimdi bu ara dönemin karar/commit/kayıt zinciri araştırılmalı.

## Şimdi — E geçişi: SOUL'a geçiş kronolojisi

En yüksek bilgi değerli soru:

**2026-08-11'deki "araştırma evi / sonraki yeni geliştirme" yönünden 2026-08-25 SOUL bootstrap'ına hangi olay, değerlendirme, karar veya yeniden-çerçeveleme zinciriyle gelindi?**

Öncelik:

1. `os-architect` 2026-08-11 → 2026-08-25 commit/kayıtlarında SOUL, araştırma evi, değerlendirme günü, KEEL'in yeniden değerlendirilmesi veya first-principles yeniden kuruluş sinyallerini bul.
2. İndekslerden işaret edilen `degerlendirme-gunu-*`, sahip seansları ve ilgili karar kayıtlarını seçici oku.
3. Gerekirse git'te yaşayan tarihî dosyalara yalnız kaynak zinciri işaret ettiğinde dön.
4. `soul` bootstrap ifadesinin geçmiş kayıtlardaki hangi probleme cevap verdiğini ayır.

## Yeni oturumda devam

1. Canonical `AGENT.md` + routing protokollerini yükle.
2. `research/soul-context/README.md` oku.
3. Bu `STATE.md` dosyasını oku.
4. `research/soul-context/repos/os-architect/README.md` aç.
5. E geçişi için 2026-08-11 → 2026-08-25 kronolojisini araştır.

## Henüz yapılmaması gerekenler

- SOUL mimarisi önermek.
- KEEL mekanizmalarını SOUL gereksinimi saymak.
- İkinci-el literatür özetlerini doğrulanmış dış kanıt saymak.
- Fresh execution yapılmadan "KEEL testleri bugün geçiyor" demek.
- "SOUL Research'ün amacı kesin olarak X" hükmü vermek.
