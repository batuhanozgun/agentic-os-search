# Concepts — Aşamalı Çalışma ve Hazırlık Planı

**Sürüm:** 0.1 — 2026-09-18. Güncel iş/yetki [STATE](STATE.md)'dedir. Plan, listelenen bütün işleri başlatma yetkisi değildir.

## Aşamalar

| Aşama | Amaç | Dönüş/durma koşulu |
|---|---|---|
| P0 — Repository hazırlığı | Amaç, yöntem, envanter, üç seviye, kök bağlantıları ve yeni oturum devam yolunu kurmak. | Onaylı kapsamın yayını ve geri okuması; kullanıcıya sonucu bildirip durmak. |
| P1 — İlk tekil araştırma | Kullanıcının yeni devam yönüyle Agent BRIEF üzerinden farklı kullanımları araştırmak. | Kaynaklı, sınırlı bir sonuç ve açık sorular; tek cümlelik tanıma zorlamadan kullanıcıya dönmek. |
| P2 — Sonraki tekil araştırmalar | Envanter ve ortaya çıkan gerçek bağımlılıklardan sıradaki sınırlı soruyu seçmek. | Her çalışmanın kendi sorusu ve anlamlı değerlendirme noktası. |
| P3 — Sınırlı sentezler | Yeterli zemini oluşan ilgili kullanımları karşılaştırmak. | Ayrım ve ilişkiler gerekçeli; açık eksikler tekil araştırmaya geri bağlanmış. |
| P4 — Ortak referans | Kaynaklı açıklama ve karşılıklı değerlendirmeyle kapsamlı kullanım kararı. | Exact açıklama ve açık kullanıcı değerlendirmesi korunmuş; anlaşılmayan kısım zorla kapatılmamış. |
| P5 — Kullanımda gözden geçirme | Referansın iletişime katkısını ve eksiklerini değerlendirmek. | Gerekli yerel düzeltme; yeni protokol veya bütünsel yeniden tasarım otomatik değil. |

P2/P3/P4 tüm envanterin seri tamamlanmasını gerektirmez; yeterli zemini olan küçük kümelerle ilerleyebilir. Henüz bilinmeyen ilişki zorla çizilmez. Önceki SOUL-merkezli konuşma incelemesi P1 araştırmasının yerine geçmez.

## P0 — Onaylanan yazma kapsamı

### Yeni 11 dosya

- `concepts/INDEX.md`
- `concepts/STATE.md`
- `concepts/PURPOSE.md`
- `concepts/METHOD.md`
- `concepts/PLAN.md`
- `concepts/TERM-INVENTORY.md`
- `concepts/research/INDEX.md`
- `concepts/research/agent/BRIEF.md`
- `concepts/synthesis/INDEX.md`
- `concepts/reference/INDEX.md`
- `concepts/checks/SETUP-VERIFICATION.md`

### Sınırlı değişecek 7 dosya

| Yol | İzinli değişiklik |
|---|---|
| `README.md` | Beşinci alanı tanıtmak, concepts girişini ve otorite ayrımını eklemek. |
| `research/INDEX.md` | Bu program için özel yerleştirme ve geri çağırma yolu; araştırma içerikleri yerlerinde. |
| `research/studies/INDEX.md` | Studies ile concepts ayrımı ve çapraz erişim. |
| `research/studies/CATALOG.md` | Tablo dışında kısa yönlendirme; mevcut study satırlarını aynen korumak. |
| `research/studies/PACKAGE-CONTRACT.md` | Ayrı programın kendi giriş/yöntemini kullanacağını ve sahte ikinci study paketi gerekmediğini belirtmek. |
| `explorations/INDEX.md` | Geçmiş geçici kullanımlardan yeni programa erişim; özgün denemeler değişmez. |
| `agent/protocols/candidate-research-library.md` | Yalnız yerleştirme/geri çağırma istisnası; yeni sözlük zorlaması veya routing sorusu yok. |

Silme/taşıma yok. AGENT.md ve diğer protokoller, Foundation/soul-context, bütün study paketleri, EXP-001/EXP-002 ve publications içerikleri korunur. Hedef SOUL/Development OS repository'lerine yazılmaz. Başka terimler için boş paket, kabul edilmiş tanım veya sözde araştırma sonucu açılmaz.

## Eşzamanlı çalışma ve yayın

Başlangıç main: `3d93615ae51e4e85cd509e49f65b4c2afbad07c0`. Hazırlık branch'i: `setup/concepts-reference-20260918`. Başlangıç değeri sonraki main'in güncel olduğu iddiası değildir.

1. Kendi alanını bu branch'te hazırla. Başka oturumun branch'ini taban, ortak yazma alanı veya temizlenecek artık sayma.
2. Ortak dosyaların exact gövdelerini ve kimliklerini geri kazan. Yalnız gerekli yerleştirme/yönlendirme eklerini yap; katalog satırlarını yeniden üretme.
3. Güncel main'i yayına yakın tekrar oku. İlerlemişse delta'yı kontrol et; yalnız bizim değişikliğimizi yeni tabanla uzlaştır. Eski bütün dosyayı güncel sürümün üzerine yazma.
4. Hem 18 yol kapsamını hem ortak dosyalardaki bölüm kapsamını karşılaştır. Katalogda mevcut satırların bayt korunmasını ve diğer içerikte ilgisiz değişiklik olmadığını denetle.
5. Yeni dosyalarla giriş eklerini birlikte yayımla. Main'e force uygulama; çakışmayı zorla bastırma. Koşullar uygunsa non-force fast-forward veya exact head'e bağlı anlık PR merge; belirsizlikte yalnız etkilenen yayını durdur.
6. Main commit/ref ve ilgili içerikleri geri oku. Branch'te hazırlanmış olmayı main yayını sayma. Canonical kontrol dosyası değiştiyse yeniden tam oku.
7. Gerçek kontrolleri [SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md)'da kaydet, STATE'i gerçek duruma getir. Yayın engelliyse yeri ve eksik kontrol açık kalsın.

Bu plan diğer oturumlarda kilit oluşturmaz veya onların henüz yayımlamadığı işleri görünür yapmaz. Repository koruma ayarı, genel koordinasyon sistemi, otomatik merge ve eski branch temizliği bu yetkinin dışında.

## P0 kabul kontrolü

Giriş bağlantıları mevcut dosyalara ulaşmalı; yöntem/plan/durum çelişmemeli; concepts ikinci studies deposuna dönüşmemeli; araştırma/sentez/kabul edilmiş referans başlangıçta yok olarak kalmalı. Yeni oturum yalnız giriş yoluyla amaç, mevcut iş, ilk soru ve durma sınırını bulabilmeli.

Bu kontrol erişim, içerik kimliği, kapsam ve tutarlılık içindir. Gelecekteki iletişim kalitesinin veya model davranışının bağımsız doğrulaması değildir.
