# Concepts — Esnek Çalışma Planı

**Sürüm:** 0.2 — 2026-09-18. Güncel iş/yetki [STATE](STATE.md), işleyiş [METHOD](METHOD.md), amaç [PURPOSE](PURPOSE.md)'dedir. Bu plan envanterdeki bütün işleri başlatma veya bir terimin anlamını kabul etme yetkisi değildir.

## İlerleme modeli

Bir terimden veya somut anlam sorusundan başlanır. Kaynak incelemesinde ortaya çıkan terim, işlev ve ilişki sorularından yalnız mevcut anlaşmayı maddi biçimde etkileyenler gerektiği kadar açılır. Yeterli zemin oluştuğunda ortak kullanım adayı değerlendirilir; tüm envanter veya bütün komşu araştırmalar beklenmez. Aynı küçük döngüde birden fazla bağlı kavram ele alınabilir.

| Çalışma hareketi | Ne zaman anlamlı? | Nerede durulur / nereye dönülür? |
|---|---|---|
| Mevcut odağı geri kazanmak | Yeni oturum veya çalışma devrinde. | STATE'teki açık soru, mevcut kanıt ve yetki anlaşılınca; eski hazırlığı/araştırmayı tekrarlamadan. |
| Kaynak kullanımlarını incelemek | Anlamı ayıracak kanıt eksikse. | Somut fark ve sınırlar görünür olduğunda; daha çok kaynak bulunabildiği için sürdürmeden. |
| Bağlantıyı açmak | Bir komşu terim/işlev/ilişki mevcut anlam kararını gerçekten etkiliyorsa. | Gerekli ayrım anlaşılınca asıl soruya dönmek; tüm komşu alanı bitirmeyi şart koşmadan. |
| Birlikte açıklamak ve aday önermek | Mevcut kanıtla kapsamlı bir yerel kullanım anlatılabiliyorsa. | Somut örnek üzerinde karşılıklı değerlendirme; engel varsa yalnız o hedefli soruya geri dönüş. |
| Yerel kullanımı kaydetmek | Belirli açıklama/kapsama açık kullanıcı değerlendirmesi varsa. | Kabul edilen kısmı referansa geçirmek; açık kısmı veya yönteme verilen onayı tanım kabulü saymadan. |
| Kullanımda gözden geçirmek | Yeni örnek/kanıt önemli bir anlam kaybını gösteriyorsa. | Yalnız etkilenen kaydı ve ilişkilerini yeniden değerlendirmek; her yeni kaynakla bütün sistemi açmadan. |

Bunlar sabit kapılar veya bir kez geçilecek büyük fazlar değildir. `research/`, `synthesis/`, `reference/` ayrımı kayıtların epistemik rolünü korur; çalışmanın doğrusal sırayla yapılmasını dayatmaz. Bağlantılı inceleme bir grafik veritabanı, zorunlu ağaç, düğüm şeması veya ağır iş takip sistemi kurma kararı değildir.

## Güncel uygulama sınırı

Bu yöntem uyarlaması kapsamında mevcut dosyalar denetlenir, gerekli yönlendirme/durum değişiklikleri yayımlanır ve kullanıcıya dönülür. U01 korunur. Yeni dış kaynak araştırması, referans tanımı veya SOUL/Development OS tasarımı bu bakım turunun işi değildir.

Sonraki kavram devamında [Agent BRIEF](research/agent/BRIEF.md) ve U01 üzerinden açık anlam sorusu ele alınabilir. “Agent oluşturmak”, “LLM/model” veya başka bir komşu peşinen sıradaki zorunlu araştırma değildir; önce mevcut soruya katkısı değerlendirilir. Bütün adayların öncelikleri [STATE](STATE.md)'ten bağımsız biçimde bu planda yönetilmez.

Yöntem değişiminin dosya bazlı kapsamı, korunacak kayıtlar ve gerçek kontroller [uyum kaydında](checks/METHOD-ALIGNMENT-2026-09-18.md)'dır. Önceki P0 hazırlığı tamamlanmıştır; aşağıdaki bölüm yalnız tarihsel planı korur.

## Yeni çalışmalar için yayın disiplini

Güncel main'den kendi sınırlı çalışma branch'ini kullan; aşağıdaki eski hazırlık branch'ini veya başka oturumun branch'ini yeniden çalışma alanı sayma. Değişiklikten önce ilgili dosyanın tam gövdesini ve kimliğini geri kazan. Yalnız gerekli içeriği değiştir; değiştirmeden bıraktığın ilgili dosyanın gerekçesini de denetimde göster.

Yayına yakın main ilerlemesini kontrol et. Eski bütün dosyayı yeni katkıların üzerine yazma; çakışma varsa etkilenen yayını durdurup uzlaştır. Dosya ve bölüm kapsamını incele; yayın head'ine bağlı normal PR birleşimi veya güvenli non-force yol kullan. Main'den içerik/kimlik ve giriş bağlantılarını geri doğrula. Gerçek yayın sonucunu STATE ve ilgili kontrol kaydına işle; branch'te hazırlanmış olmayı main yayını sayma.

Bu disiplin bütün repository için kilit, genel branch temizliği, otomatik arka plan işi veya diğer oturumların henüz yayımlamadığı işlerinin doğrulaması değildir.

## Tarihsel P0 — Onaylanan hazırlık kapsamı

Aşağıdaki 11 yeni / 7 mevcut dosyalı kapsam ve eski yayın adımları v0.1 hazırlığına aittir. Tamamlanmış işin kaydıdır; bugünkü yapılacaklar veya kullanılacak branch değildir. P1–P5'in eski faz numaraları yeni bir küresel yürütme sırası olarak sürdürülmez. Gerçek P0 yayını [SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md)'dadır.

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

### P0'ın tarihsel eşzamanlı çalışma ve yayın adımları

Başlangıç main: `3d93615ae51e4e85cd509e49f65b4c2afbad07c0`. Hazırlık branch'i: `setup/concepts-reference-20260918`. Başlangıç değeri sonraki main'in güncel olduğu iddiası değildir.

1. Kendi alanını bu branch'te hazırla. Başka oturumun branch'ini taban, ortak yazma alanı veya temizlenecek artık sayma.
2. Ortak dosyaların exact gövdelerini ve kimliklerini geri kazan. Yalnız gerekli yerleştirme/yönlendirme eklerini yap; katalog satırlarını yeniden üretme.
3. Güncel main'i yayına yakın tekrar oku. İlerlemişse delta'yı kontrol et; yalnız bizim değişikliğimizi yeni tabanla uzlaştır. Eski bütün dosyayı güncel sürümün üzerine yazma.
4. Hem 18 yol kapsamını hem ortak dosyalardaki bölüm kapsamını karşılaştır. Katalogda mevcut satırların bayt korunmasını ve diğer içerikte ilgisiz değişiklik olmadığını denetle.
5. Yeni dosyalarla giriş eklerini birlikte yayımla. Main'e force uygulama; çakışmayı zorla bastırma. Koşullar uygunsa non-force fast-forward veya exact head'e bağlı anlık PR merge; belirsizlikte yalnız etkilenen yayını durdur.
6. Main commit/ref ve ilgili içerikleri geri oku. Branch'te hazırlanmış olmayı main yayını sayma. Canonical kontrol dosyası değiştiyse yeniden tam oku.
7. Gerçek kontrolleri [SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md)'da kaydet, STATE'i gerçek duruma getir. Yayın engelliyse yeri ve eksik kontrol açık kalsın.

Bu plan diğer oturumlarda kilit oluşturmaz veya onların henüz yayımlamadığı işleri görünür yapmaz. Repository koruma ayarı, genel koordinasyon sistemi, otomatik merge ve eski branch temizliği bu yetkinin dışında.

### P0'ın tarihsel kabul kontrolü

Giriş bağlantıları mevcut dosyalara ulaşmalı; yöntem/plan/durum çelişmemeli; concepts ikinci studies deposuna dönüşmemeli; araştırma/sentez/kabul edilmiş referans başlangıçta yok olarak kalmalı. Yeni oturum yalnız giriş yoluyla amaç, mevcut iş, ilk soru ve durma sınırını bulabilmeli.

Bu kontrol erişim, içerik kimliği, kapsam ve tutarlılık içindir. Gelecekteki iletişim kalitesinin veya model davranışının bağımsız doğrulaması değildir.
