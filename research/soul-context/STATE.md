# SOUL Context — STATE

**Durum:** RPD-INFORMED FINAL HANDOFF PREPARED; OWNER ADOPTION / TARGET IMPLEMENTATION NOT OBSERVED  
**Son güncelleme:** 2026-09-08  
**Güncel hedef:** `batuhanozgun/soul-development-os_02`, `main`.

## En son kullanıcı yönü

Kullanıcı önceki uygulama mesajını göndermeden, başka oturumda hazırlattığı RPD kavramsal metnini, RPD süreklilik mimarisi ÖNERİSİNİ ve tamamen uydurma/sentetik ZIP denemesini verdi. Codex'in de RPD uygulamasını ve önceki yanıtın mevcut araştırmalarla birlikte yeniden değerlendirilmesini istedi. Dışarıda yeni plan-review döngüsü istemiyor; Codex iç planlama/eleştiri/test/onarımı kendisi yapacak.

Bu nedenle eski `DEVOS02-KERNEL-IMPLEMENT-AND-CONTINUE-v1` mesajı gönderilmiş veya benimsenmiş sayılmaz. Önceki üç düzeltmeli review, yeni RPD yönünü tek başına karşılayan güncel şartname değildir. Güncel sözleşme aşağıdaki konsolide REVIEW'dur. Eski sürümler Git geçmişinde korunur; yeni görevin üstüne ayrı etkin talimatlar olarak eklenmez.

## Amaç ve kaynak sınırı

SOUL, istenen sonuç için uygun çalışma sistemi oluşturma/işletme/etkisini değerlendirme/uyarlama ürün hedefidir. Development OS bu ürünü araştırmak, tasarlamak, geliştirmek ve doğrulamak için çalışma düzenidir. İlk Codex çekirdeği, bütün Development OS veya SOUL'un tamamlanması değildir.

Araştırma ilk günden tüm aktör, iş, bilgi/context, kontrol, doğrulama ve ortam kararlarına seçici girdi olur. RPD bu dört ground'ın yerine geçmez veya beşinci ground değildir. Araştırma bulguları kanıt/tasarım girdisidir; işlem yetkisi üretmez. Ham RPD kavramsal tanımı, süreklilik mimarisi önerisi ve sentetik prototip ayrı statülerdedir. Mimari/prototipin tümü otomatik benimsenmez.

RPD için son kullanıcı yönü: ana ve alt ajanlar yalnız seçilmiş işi iyi yürütmez; hedefin gerçekleşebilmesi için söylenmemiş önkoşulları ve gerekli işleri de keşfeder. İhtiyaç/koşul/yöntem/karar/eylem, VE/VEYA, yöntem koşulları, mevcut zemin/başlanabilir iş, kaynak kapasitesi, ileri sınama, bitmemiş keşif ve parent'a dönüş bağı korunur. Kullanıcı gizli eksik-bulucu, teknik mesaj taşıyıcı veya test operatörü olmaz. Gerçek owner kararları korunur.

## Son doğrulanmış target

Bu tur GitHub'dan `main` yeniden okundu: `a91c7a956734580106139d5ce0ba8dd74660f161`; önceki incelenmiş plan snapshot'ı değişmemiştir.

- PLAN: `work/devos-bootstrap/PLAN.md`; blob `7cd3dc1c303beb1e1b7cb1bd4a63ce23f224433d`.
- EVIDENCE: aynı dizin; blob `98b74acee2426599c80343c2e4677320ac19193c`.
- AGENTS: blob `95296d64c523803d4e3d1b628579327559cadbbf`; bu tur tam okundu.
- Mevcut hedef kontrolü: R01–R08 ve W01–W04; iki grup ve kullanıcı istediği `ID–Soru | Yanıt | Karar | Cevap` tablosu.

Yerel Codex durumu/izin/süreçler bu tur yeniden çalıştırılmadı. Önceki native denemeler producer kayıtlarıdır. K01–K12 kurulum testleri ve yeni RPD davranışı henüz hedefte doğrulanmış sayılmaz. Research hedefe yazmadı.

## Tek güncel konsolide devir

**Review ID:** `DEVOS02-RPD-INTEGRATION-2026-09-08-v2`.  
**Canonical dosya:** `current/reviews/2026-09-08-devos02-plan/REVIEW.md`.  
**Owner benimsemesine sunulan grant:** `DEVOS02-RPD-IMPLEMENT-AND-CONTINUE-v2`.

Ayrıntılı karar ve kapsamın tek evi REVIEW'dur. Retrieval özeti:

- Mevcut native üretici/değerlendirici/integrator ve yetki/kanıt/etki sınırları korunur.
- RPD her kullanıcı hedefi ve devredilen ihtiyaçta uygulanır; küçük işte kısa sürer, karmaşıklık eşiğiyle kapatılmaz; her küçük iş dosya veya graph gerektirmez.
- Hedefte dar AGENTS eki + `devos-agent/protocols/reasoning/prerequisite-discovery.md` için sınırlı yeni kontrol değişikliği önerilir; registry'ye RPD01 eklenir. Mevcut 12 protokol/soru değiştirilmez. Research kontrolü değişmez.
- Önceki iki araç isimleri ve sırası zorunlu olmaktan çıkar; RPD gerçek ihtiyaç, yeterli mevcut mekanizma ve başlangıç frontier'ını değerlendirir. Native gerçek üretim ve yararlı çıktı şartı korunur.
- STATE/WORK/EVIDENCE ve gerekçeli attempt-private checkpoint'ler ilk kayıt adayıdır; ikinci canonical store/HEAD, lease altyapısı, hook, skill veya scheduler otomatik kurulmaz.
- F01 expected-check eksiksizliği, F02 fiilî kontrol/rol/girdi bağı ve F03 gerçek yazıcı kesintisini üretimden önce sınama korunur. Lease expiry eski writer'ın durduğu anlamına gelmez.
- K01–K12 güvence amaçları korunur, yeni kontrol/pilotla exact bağları iç uyarlamada güncellenir. RP1–RP6 davranış aileleri eklenir: kısa giriş, söylenmemiş ihtiyaç, koşullu ağ/kapasite, ileri sınama, bitmemiş keşfin devri ve gerçek yarar/durma.
- Owner-benimsenmiş tek mesaj sonrasında Codex kendi iç RPD uyarlamasını, ayrı-start eleştiriyi, bounded kurulumu/test/onarımı ve başarılı kapı sonrası normal devamı yönetir. Baştan browser'a plan göndermesi beklenmez.

Sözleşme, mevcut target PLAN/EVIDENCE'ı tarihsel baseline olarak korur. Yeni amaç/grant/delta hedef kernel WORK/STATE'e, actual sonuçlar EVIDENCE'a yazılır. Kabul edilmiş snapshot, kısmi kayıt ve türetilmiş görünüm ayrılır; kayıtlar farklı sürümlerden tek güncel gerçekmiş gibi birleştirilmez.

## Eklerin kimliği ve yerel inceleme

- Kavramsal metin SHA-256: `9af3e87eea0e589ea2f5f14e863de6cafdabf68ed585efd0214603492c096e09`.
- Süreklilik önerisi SHA-256: `7fc37d3fb3ca7777517691112439bad9718346e5c063c4cee34f31066d1a8121`.
- ZIP SHA-256: `0a1167a5e51123c22a006e7222441b99567e77ad3b8f02c57ede1fe5fd5cde56`.

İki Markdown ve ZIP'teki 24 dosya okundu; iki tekrar kaynak byte-identical, 23 manifest hash'i eşleşti. Yerel Linux/Python'da 25 mekanik test ve demo çalıştı. İki ek sınırlı probe, semantik önkoşul/kabul denetiminin ve zorunlu kimlik/lease enforcement'ın prototipte olmadığını gösterdi; rapor bunları production veya RPD doğrulaması saymaz. Hiçbir LLM/Codex/Claude deneyi veya kullanıcı ortamı kurulumu bu yerel testlere dahil değildir.

Tam ham ekler Research repository'sinde yayımlanmış sayılmaz. Kullanıcıya sunulan devir paketi orijinal üç eki içerir; Codex'e birlikte verilmesi gerekir. Review, benimseme sonrasında hedefin izinli references alanında exact/pasif kaynak kopyalarını ve manifestini tutmayı kapsar. Gelecekte ham RPD claim'i için kaynak gerekirse gerçek kopya/ref bulunmalı; yalnız bu özetten tam metin üretilmemelidir. Eksik SKILL.md v0.1.1-draft'ın okunduğu veya kurulduğu iddia edilmez.

## Sıradaki sorumluluk

Research bu yeniden değerlendirmeyi kullanıcıya tek yeni mesaj olarak sunar. **Benimsenme/gönderim/uygulama henüz gözlenmedi.** User relay gerçekleşirse target kendi actual yetki/state/iş otoritesidir; Research ikinci operasyon kaydı tutmaz. Normal Research rolüne dönüş, kurulmuş sistemin peşin başarı ilanı değildir.

Yeni gelişme olursa önce bu STATE → current REVIEW → target actual STATE/WORK/EVIDENCE yolu kullanılır. Eski v1 grant veya önceki repo görev zinciri yeniden current yapılmaz. Gerçek owner scope/bütçe/güvenlik kararları doğrudan Batu'dadır. Rutin plan/araştırma/test/repair için browser'a geri dönüş zorunluluğu yaratılmaz.

Bu tur Research'te yalnız context review ve continuity güncellendi; agent-control, Foundation ve studies içerikleri değiştirilmedi. Eski değerlendirme `6546e6a3f6786bd6360ef811b3b7fa799578f499` ref'inde korunur. Sıfır hata, bilimsel RPD üstünlüğü, hostile izolasyon veya gözetimsiz çalışma iddiası yoktur.
