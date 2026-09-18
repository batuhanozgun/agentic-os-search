# Concepts v0.2 — Dosya Uyum ve Yayın Kontrolü

**Tarih:** 2026-09-18. **Nesne:** U01 sonrası kullanıcı yönüyle bağlantılı kavram inceleme yönteminin repository'ye uygulanması. Araştırma bulgusu veya kabul edilmiş kavram tanımı değildir.
**Başlangıç main:** `a605ee34b45b68d9d2aece5bc815a602f4676081`.
**Başlangıç ağacı:** `3ed74c3514c05fb377d78c54ed605af7adaf26cb`.
**Çalışma branch'i:** `maintenance/concepts-connected-inquiry-20260918`.
**Yayın durumu:** ADAY; bu sürümde main birleşimi ve yayın sonrası geri doğrulama henüz tamamlanmadı. Gerçek sonuç bu kayda ve [STATE](../STATE.md)'e işlenecek.

## 1. Amaç, yetki ve değişiklik gerekçesi

Kullanıcı önce terim araştırmasının kaynaklar arasında savrulmaya dönüşmemesini, ardından bir terimden çıkan terim ve işlevlerin gerektiği kadar birlikte incelenip yerel referansa bağlanmasını istedi. Son mesaj repository dosyalarını bu çalışma biçimi açısından inceleyip gerekenleri düzeltmeyi yetkilendirdi. Seçili kullanıcı ifadeleri ve kapsam [PURPOSE](../PURPOSE.md)'te korunur.

Önceki yöntemde kaynak sadakati, üç kayıt düzeyi, sınırlı sentez ve karşılıklı kabul zaten vardı. Düzeltilen nokta; tek terim/büyük faz sırasının baskın okunabilmesi, keşfedilen komşuya neden girilip ne zaman dönüleceğinin yeterince açık olmaması ve U01 sonrası default devamın daha fazla araştırmaya kaymasıdır. Bu bir davranış hatası sıklığı ölçümü veya tek kök-neden kanıtı değil, belge/amaç uyum değerlendirmesidir.

v0.2, bir terim veya anlam sorusundan başlayıp gerekli bağlantıları açan, yeterli zeminde erken aday öneren ve kabulü ayrı tutan işleyişi belirginleştirir. Kavram grafiği veri modeli, zorunlu ağaç, genel terim yasağı, Agent tanımı veya SOUL mimarisi kurulmaz.

## 2. İnceleme kapsamı ve okuma yolu

Güncel AGENT tekrar alındı. Bu konuşmada tam okunmuş dokuz protokolün ve önceki concepts okumalarının kimlikleri güncel main ile karşılaştırıldı; `0743feae... → a605ee34...` karşılaştırması yalnız beş concepts yolu ile ECC `ROUND-U08-A.md` ekini gösterdi, kontrol dosyası değişmedi. Sonraki current-state okumaları ve ağaç kimlikleriyle aynı sürüme bağlandı. Hatırlanan önceki-oturum özeti kontrol kaynağı yapılmadı.

Kök Git ağacı; concepts alt ağacının recursive, `truncated=false` listesi; agent alt ağacı ve doğrudan bağlı router/contract dosyaları incelendi. Concepts başlangıç ağacı `3d7234c3e10d940f71a6e4a1cba106f3c4644c8f`, 12 dosyadan oluşuyor. Aşağıda 12/12 dosyanın sonucu var. Tam gövdeler bu konuşmada okundu; değişmeyen dosyalarda güncel blob kimliğiyle aynı okuma korundu, eksik kalan SETUP ve alt INDEX gövdeleri ayrıca tam açıldı.

Repository araması `concepts` için sonuç vermedi; doğrudan GitHub code-search yanıtı `incomplete_results=true` idi. Bu, başka başvuru olmadığına kanıt sayılmadı. Kapsam doğrudan ağaç ve mevcut giriş bağlantılarıyla kuruldu. Bu kayıt bütün Foundation/studies kaynak corpus'unun yeniden tam okunması veya kusursuz repository-geneli metin araması iddiası değildir.

## 3. Concepts — mevcut 12 dosyanın tamamı

| Dosya | Sonuç | Gerekçe / korunan sınır |
|---|---|---|
| `concepts/INDEX.md` | Güncelle | Yeni oturum girişini, üç kayıt düzeyini ve tarihsel/current ayrımını yeni işleyişe bağla. |
| `concepts/STATE.md` | Güncelle | Son kullanıcı yetkisi, yöntem bakımı, gerçek yayın, açık anlam sorusu ve otomatik olmayan devam. U01/P0 tarihi korunur. |
| `concepts/PURPOSE.md` | Ekle | İlk gerekçeyi koru; U01 sonrası seçili kullanıcı ifadelerini ve yöntem onayı/terim kabulü ayrımını ekle. |
| `concepts/METHOD.md` | Yeniden düzenle | Bağlantılı inceleme, komşuya gerekçeli iniş/dönüş, erken aday, kaynak eşleme, kısmi kabul ve kontrollü yeniden açma. |
| `concepts/PLAN.md` | Yeniden düzenle | Global faz kuyruğu yerine esnek hareketler; eski 11/7 P0 kapsamı ve yayın adımları tarihsel bölümde korunur. |
| `concepts/TERM-INVENTORY.md` | Güncelle | Başlangıç listesini koru; U01 ve sohbet örneklerinin kökenlerini ayıran keşif yönlendirmesi ekle. Öncelik veya zorunlu bağımlılık seçme. |
| `concepts/research/INDEX.md` | Güncelle | Kaynak çalışmasını tekil terim kuyruğu olmaktan ayır; U01'i ve gerektiği kadar komşu incelemesini yönlendir. |
| `concepts/research/agent/BRIEF.md` | Güncelle | U01'i devral; “aynı şeyi konuşmak için hangi ayrım gerekiyor?” sorusuna dön. Otomatik U02 veya örnek tanım kabulü yok. |
| `concepts/research/agent/U01-SOURCE-USES.md` | Değiştirme | Tarihli kaynak gözlemleri, sınırlamalar ve devam adayı korunur. Yeni yöntem geçmiş kanıtı yeniden yazmaz. Blob `22f04d1c120afa91781f680af32bf3b5944c3d30`. |
| `concepts/synthesis/INDEX.md` | Güncelle | Küçük bağlantılı kümelerin karşılaştırılması ve erken yerel kullanım adayları; kabulden ayrı. |
| `concepts/reference/INDEX.md` | Güncelle | Kapsamlı yerel kullanım, somut karşılıklı değerlendirme, kaynak eşleme ve değişiklik izi; henüz kabul edilmiş kayıt yok. |
| `concepts/checks/SETUP-VERIFICATION.md` | Değiştirme | P0 tarihli kanıt kaydıdır; bugünkü yokluk veya devam otoritesi değildir. INDEX/STATE bu sınırı açıklar. Blob `dafe403877eec4b9a6d430a8054bfe1c0f942a11`. |

Bu denetim dosyası tek yeni concepts dosyasıdır. Yeni Agent/Model tanımı, komşu araştırma paketi veya mimari dosyası açılmaz.

## 4. Doğrudan bağlı altı giriş/sözleşme dosyası

| Dosya | Sonuç | Gerekçe |
|---|---|---|
| `README.md` | Sınırlı ek | Bağlantılı inceleme ve yerel referans amacını ana girişte görünür kıl; diğer alanları değiştirme. |
| `research/INDEX.md` | Değiştirme | Concepts'in kendi STATE/METHOD yolunu ve üç rolün ayrımını zaten taşır; zorunlu global sıra dayatmaz. |
| `research/studies/INDEX.md` | Tek paragrafta sınırlı düzeltme | “three-stage method” ifadesini iterative yöntem ve üç kayıt düzeyi olarak netleştir. Study rotaları/listesi korunur. |
| `research/studies/CATALOG.md` | Değiştirme | Derived study kataloğudur; concepts dış-program yönlendirmesi yeterli. İkinci study satırı veya bulgu kopyası eklenmez. |
| `research/studies/PACKAGE-CONTRACT.md` | Değiştirme | Concepts'in kendi STATE/METHOD sözleşmesine açık istisna zaten var; ok işareti burada yerleştirme açıklamasıdır, yöntem sırası dayatmaz. |
| `explorations/INDEX.md` | Değiştirme | Concepts geçişi ve geçmiş anlamların korunması zaten uygun; eski diyaloglar yeniden yazılmaz. |

EXP-002 `reflections/TERMS.md` ve `QUALIFICATIONS.md` bu konuşmada tam okunmuş tarihsel dayanaklardır. Onlar ve U01'de seçici kullanılan study kayıtları yöntem değişimiyle güncellenmez veya dış tanım kanıtına terfi ettirilmez.

## 5. Kontrol katmanı — inceleme sonucu

Aşağıdaki dosyaların tamamı konuşmada tam canonical okumayla yüklendi; güncel ağaç ve commit karşılaştırması aynı sürümleri doğruladı. Bu dosyalar araştırma corpus'u değildir ve hiçbirine yazılmaz.

| Kontrol dosyası | Uyum sonucu |
|---|---|
| `AGENT.md` | Kontrol/iş ayrımı ve mevcut yönlendirme yeterli. |
| `agent/protocols/decision-critical-assumptions.md` | Komşunun gerçekten gerekli olması ve alternatif kapsam değerlendirmesiyle uyumlu. |
| `agent/protocols/user-independent-reasoning.md` | Önceki assistant örneğini/onay baskısını kanıt saymama ile uyumlu. |
| `agent/protocols/goal-method-end-to-end-validation.md` | Kullanıcı amacı ve mevcut bakım turu sınırı korunuyor; yeni mimari faz açılmıyor. |
| `agent/protocols/verification-independence.md` | Belge/diff kontrolü davranışsal veya bağımsız bilimsel doğrulama yapılmıyor. |
| `agent/protocols/source-view-fidelity.md` | Kaynak gözlemi, özet, sohbet örneği ve yerel kullanım ayrımı korunuyor. |
| `agent/protocols/causal-depth-root-cause-validation.md` | Belge değişikliğinin gelecekteki bütün drift'i çözdüğü iddia edilmiyor. |
| `agent/protocols/work-system-continuity.md` | Güncel odak/yetki ve sonraki sorumluluk STATE'te. |
| `agent/protocols/canonical-work-preflight.md` | Yeni oturum METHOD ve ilgili çalışma yolunu tam geri kazanır; yeni kontrol protokolü gerekmiyor. |
| `agent/protocols/candidate-research-library.md` | Concepts için yerleştirme/geri çağırma istisnası mevcut; çalışma kendi METHOD'una yönlenir. Genel sözlük veya ikinci study gerekmiyor. |

## 6. Yayın öncesi kontrol hedefleri

Beklenen delta: **12 mevcut dosya değişikliği + bu tek yeni kayıt = 13 yol.** Concepts dışında yalnız README ve studies INDEX. U01, SETUP, AGENT/agent, Foundation/soul-context, study paketleri, explorations ve publications içerikleri korunmalı.

PR diff'inde dosya kapsamı ve ortak dosyaların bölüm kapsamı kontrol edilecek. Özellikle studies INDEX'in concepts paragrafı dışındaki satırları ile README'nin ek dışındaki gövdesi korunmalı. Bağlantılar mevcut dosyaya veya bu yayında eklenen uyum kaydına gitmeli. Main ilerlerse yeni katkıları koruyacak delta kontrolü yapılacak.

Manuel devam senaryoları: U01'i tekrar araştırma sanmamak; Model/Role'u otomatik önkoşul seçmemek; yeterli zeminde bütün envanteri beklememek; yeni kaynağın farklı adını kabul değişikliğine çevirmemek; yöntem onayını örnek tanım onayı saymamak; işlev keşfinden mimari bileşen çıkarmamak. Bunlar belgeye karşı self-review senaryolarıdır; bağımsız yeni-oturum veya canlı agent deneyi değildir.

## 7. Gerçekleşen yayın ve geri doğrulama

Bu aday sürümde tamamlanmadı. PR/merge kimliği, exact head/base kontrolü, korunmuş blob'lar, gerekli geri okumalar ve varsa düzeltilen kapsam farkları gerçekleşince buraya işlenecek. Kendi gelecek commit kimliği tahmin edilmeyecek.

Başarı iddiası dosya uyumu, izlenebilirlik, kapsam ve erişimle sınırlı tutulur. Referansların gelecekte her tur doğru kullanılacağı veya anlam karmaşasının sıfırlanacağı garanti edilmez.
