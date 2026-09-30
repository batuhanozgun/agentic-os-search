# Araştırma / kurulum ayrımı — depo bakım çalışması

**Kimlik:** REPO-SEPARATION-20260929  
**Durum:** DEVAM EDİYOR — A1 tamam. A2'nin önceki girişlerine ek olarak current/reviews içindeki ilk 6 kayıt sonuçlandırıldı: 5 statü notu, 1 gerekçeli koruma. Kalan 16 review/kanıt dosyası, A2'nin diğer doğrudan girişleri, A3 arşivi ve A4/A5 açık.  
**Güncelleme:** 30 Eylül 2026. **Yazar:** ChatGPT, Batu'nun açık yetkisiyle.  
**Kaynak:** [Görev belgesinin değiştirilmemiş kopyası](maintenance/2026-09-29-research-installation-separation/REQUEST.md). İş, kullanıcının isteğiyle turlara bölünmüştür.

Bu dosya yalnız `agentic-os-search` deposunu güncelleme çalışmasının planı, ilerleme kaydı ve devir noktasıdır. Yeni DevOS kurulum planı, SOUL iş listesi, mimari veya agent-control dosyası değildir. Bu sürüm ilerleme ve devir kısmını günceller; önceki kayıt `9620dfdeda71f25580f6945c2bb3a11c19b78703` commit'inde, blob `0ae2bb1431bb3c842d56062d8d08c9a08fc8bc52` olarak korunur.

## 1. Amaç ve yetki

Depoyu ilk kez okuyan Claude Code kurucusu araştırma kütüphanesini tarihsel DevOS kurulum kayıtlarından ayırabilmeli; eski Codex/P5/DEVOS-001/002 yönlerini güncel kurulum işi sanmamalıdır. Araştırma içeriği, özgün kararların tarihçesi ve kanıt sınırları korunur.

DevOS'un geçerli yönü **Claude Code cloud**; kurulum planının tek evi [batuhanozgun/devos — plan/](https://github.com/batuhanozgun/devos/tree/main/plan), görevde belirtilen devir sürümü **2.1**'dir. Planın kopyası bu depoya konulmaz. Yeni ürün deposu `batuhanozgun/soul-system`; eski `batuhanozgun/soul` ve görevde sayılan diğer deneme depoları değiştirilmez. [D030](explorations/EXP-006-development-os-calisma-duzeni/DECISIONS.md#d030--claude-code-cloud-kurulum-devri) bu yetki/statü değişimini taşır.

Yazma yalnız `batuhanozgun/agentic-os-search` içindedir. `AGENT.md` ve `agent/**` değiştirilmez. Başka depolara, Supabase projelerine, hesaplara veya erişim ayarlarına yazılmaz. Kurulum yapılmaz. Aktif araştırma paketlerinin kendi durumları korunur; bunlar Claude Code için kurulum talimatı değildir.

`batuhanozgun-devos` makine hesabının teknik yazma imkânı yazma yetkisi değildir. Bu hesapla ilişkilendirilmiş commit görülürse düzeltmeden önce Batu'ya bildirilir. Her yayın öncesi main delta ve yazar kontrolü yenilenir. Hesap erişimini kaldırma bu bakımın işi değildir.

Görev kaynağındaki tarihli platform karşılaştırmaları kullanıcıdan alınan bağlamdır; bu bakım onları yeni teknik yeterlik veya fiyat doğrulaması olarak onaylamaz. Verilmiş platform kararı yeniden açılmaz.

## 2. Ayrımın tasarımı

**Yerinde statü ve yönlendirme ayrımı; toplu taşıma yok.**

- Foundation, studies, concepts ve kavramsal explorations kendi yerinde kalır; araştırma anlamı değişmez.
- Eski kurulum/planlama ve devir dosyalarının başına tarihli statü notu konur; eski gövde, kaynak kullanıcı sözleri ve test/öneri sınırları korunur. “Tarihsel” statü, bulguyu hipoteze veya öneriyi karara dönüştürmez. Yeni ortamın da Claude olması eski bir Claude taslağını etkinleştirmez.
- Kök ve alan girişlerinde araştırma, tarihsel kurulum, kontrol ve yayın ayrılır. Doğrudan alt dosya açılışları da incelenir; kök uyarısı tek başına son kabul değildir. Araştırma dizinindeki güncel araştırma rotaları topluca tarihsel ilan edilmez.
- Erişilebilir eski rapor/paket kopyaları için `archives/devos-pre-claude-2026-09-29/` A3'te hazırlanacaktır. Şu an oluşturulmuş ve eksiksiz arşiv sayılmaz. Özgün gövdeler değişmez; statü, erişim ve kimlik yan kayıtlarda tutulur.
- [MOVES.md](MOVES.md) gerçekleşen taşımaları tutar. **Taşıma yok.** Kopya ve kaynak bağı ayrı kaydedilir. Çok dosyalı taşıma gerekirse uygulamadan önce Batu'ya kısa plan sunulur.

## 3. Beş iş paketi ve kapanış koşulları

Paket gerektiğinde birkaç tur sürer; numarası otomatik tur sayısı değildir. Her tur doğrulanmış sonucu ve tek devam noktasını kaydeder.

| Paket | İş ve kapanış koşulu | Durum |
|---|---|---|
| **A1 — Başlangıç ve kalıcı plan** | Görev, başlangıç kimlikleri, yazar sınırı, dış plan adresi, kök yönlendirme; uzak yayın ve geri okuma | **TAMAM:** `ab8ef329aa4841fae2b836c91e74e68ad1c4c9e5` |
| **A2 — Karar ve güncel yönler** | D030; EXP-006 ve deneme/bağlam girişleri; doğrudan eski devirler; eski kurulum bu yollardan güncel diye devralınamıyor | **DEVAM:** önceki girişler ve current/reviews 6/22; current başlangıç envanterinde 25/41 sonuçlandırıldı. Kalan §4.6'da |
| **A3 — Rapor ve paket arşivi** | Yedi kaynak ailesini gerçek gövde ve kimlikle arşivle; farklı P5 paketlerini karıştırma; erişilemeyeni yeniden üretme | BEKLİYOR. Her kaynak için doğrulanmış gövde veya açık erişim engeli gerekir |
| **A4 — Depo geneli tarama** | Bütün izlenen yollar, metinler ve gerekli belge/ZIP içleri; riskli eşleşmeler için düzeltme veya gerekçeli koruma; okunmayan kapsam açık | BEKLİYOR. Araştırma anlamı değişmez; listeyle sınırlı tarama yetmez |
| **A5 — Son karşılaştırma ve teslim** | Başlangıçtan son commit'e fark; silme/taşıma/gövde ve bağlantı denetimi; yeni okuyucu yürüyüşü; tam değişiklik/gerekçe listesi | BEKLİYOR. Kapsamı aşmayan tamamlanma hükmü ve erişim açıkları teslim edilir |

## 4. A2 — tamamlanan alt kümeler ve kalan

### 4.1 Ana girişler ve D030

[A2-CORE](maintenance/2026-09-29-research-installation-separation/A2-CORE.md) 13 dosyayı, başlangıç blob'larını ve gerekçeleri listeler. **Yayımlanmış commit:** `8612f1320dbfeeef089964d4c48025051f1bb0e6`. Kaynak dosyalarının farkı 160 ek satır, 0 çıkarılan satırdır. Aynı kayıttaki `0145e407...` yalnız içerik doğrulama adayıdır; yayın kimliğiyle karıştırılmaz.

D030; EXP-006 STATE/HANDOFF/INDEX/WORK/DECISIONS ve eski CODEX_START; development-os INDEX/001 WORK/002 README; soul-context README/INDEX/STATE/repos-soul girişleri bu kümededir. D027/D029'un ortam kararı geçersiz kılındı; özgün gövdeler ve yüksek kalite/sağlayıcı bağımsızlığı hedefinin tarihçesi korundu.

### 4.2 Doğrudan teslim, mesaj ve alan girişleri

[A2-DIRECT-ENTRIES](maintenance/2026-09-29-research-installation-separation/A2-DIRECT-ENTRIES.md) ikinci kümenin tam listesini, kaynak blob'larını, okuma ve kontrol sınırını taşır. **Yayımlanmış commit:** `f690aa6bf5398d90bef2b7ee0b1b74ff52ba96c7`.

EXP-006 P4-01–P4-05 ve P5-01 (6); DEVOS-001 BRIEF/METHOD/EXCHANGE/REVIEW (4) ve R-001–R-006 (6); eski Claude hazırlığı WORK/TASK (2); research/INDEX, explorations/INDEX ve CATALOG (3): **21 dosya**. Her birinde yalnız başlangıçta 6 ek satır; toplam 126 ek satır, 0 çıkarılan satır. İçerik doğrulama adayı `ac026aba9de076dbf0181c748b51a1a279c01783`, tree `93f422340cec206ca4efd802d3d77c50aa1a8f2e`, gerçek yayınla aynı kavram değildir.

Bu iş statü/yönlendirmedir; rapor gövdelerinin arşivlenmesi veya içlerindeki test iddialarının yeniden doğrulanması değildir. S paketi ile K paketi ayrı kimlikler olarak kalır.

### 4.3 Eski current envanteri ve sekiz ana devir girişi

[A2-CURRENT-INVENTORY](maintenance/2026-09-29-research-installation-separation/A2-CURRENT-INVENTORY.md), `research/soul-context/current/` altındaki **41 başlangıç dosyasının** yol/blob/boyut listesini taşır: 2 kök, 13 brief, 4 Claude hazırlık, 22 review/kanıt dosyası. Önceki kesilmiş envanter sorunu, kök dizin ve üç ayrı recursive alt-ağaç okumasıyla kapatıldı. Envanter tamlığı içerik okuma tamlığı değildir. Bu dosyanın tarihli tablo ve ilerleme notları kendi turlarının anlık görüntüsüdür; güncel toplam ve devam burada tutulur.

Sekiz kaynak dosyası işlendi: COORDINATION-TRANSFER-PLAN ve DEVELOPMENT-OS-BOOTSTRAP; dört brief (COORDINATION-HANDOFF, DESIGN-01, DEVOS-AGENT-CONTROL, DEVOS-CONSTRUCTION-PLAN); OWNER-CONTEXT ve SOURCE-REGISTER. Ayrıca yeni `current/README.md` eklendi. **Gerçek yayın commit'i `cd35ef63d9a80dd6ff224726d2b083fa386a3c59`**.

İçerik doğrulama adayı `ff395e0eefbbc8b1e4de7af609ada4bfa84be1e9`, tree `1407d2d265f88c1773256a681df056cb799b0592`: sekiz kaynakta toplam 48 ek satır, 0 çıkarılan satır; yeni README 22 satır. İlk adayın iki dosya-sonu farkı düzeltilmeden yayına alınmadı.

### 4.4 Son dokuz brief

[A2-BRIEFS](maintenance/2026-09-29-research-installation-separation/A2-BRIEFS.md) dokuz dosyanın tam listesini, başlangıç blob'larını, gerekçeleri ve kontrol sınırını taşır. Envanterin **03–05 ve 10–15** satırlarıdır: COORD-01/02/03, G0-D1, G1, G1-R1, Stage-1, Stage-1A ve Stage-2/G0. **Gerçek yayın commit'i `9620dfdeda71f25580f6945c2bb3a11c19b78703`** bu turun başında main'den doğrulandı.

Dokuz dosyanın tamamı sabit başlangıç commit'inden okundu. Düzeltilmiş içerik doğrulama adayı **`3a371a2b653b6eb37b0c78cd5921b8f24e3c510f`**, tree **`7cf7d124d62e06cc2a6f112dd9efafde0745755c`**, parent `cd35ef63d9a80dd6ff224726d2b083fa386a3c59`: her dosyada yalnız başlangıçta 6 ek satır, **toplam 54 ek satır ve 0 çıkarılan satır**. Tam birleşik diff'te bütün hunk'lar dosya başındadır; özgün gövdeler korunur. İlk yayımlanmamış `2369810...` adayındaki dört son-satır-sonu farkı giderildi.

Bu tur sonunda `briefs/` grubunun 13 dosyasının doğrudan giriş statüsü ele alınmış, current alanının 41 başlangıç dosyasından 19'u işlenmiş ve 22 review/kanıt dosyası açık kalmıştı. Bu tarihli sonuç, aşağıdaki yeni incelemenin yerine geçmez.

### 4.5 İlk altı review/kanıt kaydı

[A2-REVIEWS](maintenance/2026-09-29-research-installation-separation/A2-REVIEWS.md), envanterin **20–25** satırlarının tam okumasını, beş not ve bir gerekçeli koruma kararını, kaynak kimliklerini ve doğrulama sınırını taşır. Direction, G0 ve Stage-1 çiftleridir; toplam başlangıç gövdesi **91.072 byte**.

Beş not; ham opening vision'ın eski Routing gate'ini, ham Codex tasarım cevabını ve üç REVIEW dosyasındaki eski güncel/sonraki önerileri tarihsel bağlama alır. G0 `EVIDENCE-EXTRACTS.md` ilk paragrafta zaten tarihli seçili kanıt olduğunu, talimat veya canlı durum olmadığını açıkça belirttiği için değiştirilmedi. Yeni not eklememek de gerekçeli inceleme sonucudur.

Düzeltilmiş içerik adayı **`50e4dcd27ac8a9025d4778a1148c8eb6c321ac8c`**, tree **`eb90660ac6aade7e7fc892d03467e3c18090a1af`**, parent `9620dfdeda71f25580f6945c2bb3a11c19b78703`: beş dosyada yalnız başa toplam **30 ek satır, 0 çıkarılan satır**. Özgün gövdeler ve dosya sonları korundu. Ham aktarımların eski hash/satır kimliklerinin not hariç gövdeye ait olduğu ve öneksiz sabit kaynak bağlantıları açıkça yazıldı.

Current alanındaki **25/41** başlangıç dosyası statü bakımından sonuçlandırıldı; bunun 6'sı reviews grubundadır. Bu sayı 25 yeni değişiklik veya bütün A2'nin tamamlanması değildir. Önceki denetim kayıtları tarihli tutulur, her tur yeni “güncel” kopyaya dönüştürülmez. Yeni platform, eski deney veya bağımsız Claude davranış doğrulaması yapılmadı.

İçerik adayı tek başına main yayını değildir. Kaynaklar ve bakım kayıtları nihai ağaçta birlikte yayımlanır; gerçek commit/ref ve dosya geri okuması ayrıca doğrulanır.

### 4.6 Kalan A2 kapsamı

**Tek sonraki iş: `research/soul-context/current/reviews/` içindeki kalan 16 dosyayı incelemek.** Başlangıç envanterinin **26–41** satırlarıdır; ilk kalan grup `2026-09-06-stage-1a/CODEX-RESPONSE.md` ve `REVIEW.md`. Ardından 28–41 gelir. Bu 16 dosya yalnız envanterlenmiştir; bu bakımda içerik/statü incelemesi tamam veya kusurlu oldukları gösterilmiş sayılmaz. Python/deney kaydı bulunması çalıştırma talimatı değildir. Önceki altı dosya tekrar düzenlenmez; yeni maddi bulgu çıkarsa nedeni ayrıca kaydedilir.

Ardından DEVOS-001 `reading/` girişleri ile EXP-006 P1/P2/P3 gibi diğer doğrudan yollarında statü/yön gerekip gerekmediği kontrol edilir. Araştırma veya özgün kaynak gövdesi yeniden yazılmaz. Önceki tamamlanan alt kümeler sırf tur değişti diye tekrar düzenlenmez.

A2 kapanışı, A4'ün bütün depo taramasını ve A5'in yeni okuyucu/bağlantı değerlendirmesini ikame etmez. Arama çıktısının tarihsel başlığı atladığı durumlar ve eski gövde bağlantıları son değerlendirmede ayrıca ele alınır. Yeni current README kalan bireysel incelemeleri kapatmaz.

## 5. A3 kaynak matrisi

| Kaynak | Statü | Gerçek erişim / kalan iş |
|---|---|---|
| P4 v3 | Tarihsel; uygulama kaynağı değil | Yerel adlar görüldü; bütünlük ve arşiv yayını A3'te |
| P4 v4 | Tarihsel; mimari kaynak; Codex ortam kararı geçersiz | Yerel MD/PDF/ZIP adları görüldü; A3'te kimlik kontrolü |
| P5 K00–K15 | Tarihsel; rol/veri modeli aktarımının kaynağı | `EXP-006_P5_Codex_Kurulum_ve_Devir_Paketi.zip` yerelde görüldü; bu bakımda üye/hash doğrulaması henüz yok |
| P5 S00–S12 | Tarihsel; senaryolar gelecekte sınav fikri olabilir | Repository'de teslim kaydı var; gerçek paket bu bakımda bulunmuş sayılmaz. Alt dizin/ZIP, Files/Library ve repository araması A3'te |
| P5 v2 Codex arayüzü | Tarihsel; veri modeli aktarımının kaynağı | Yerel MD/PDF/ZIP adları görüldü; A3'te kimlik kontrolü |
| SOUL ve DevOS | Tarihsel kaynak; SOUL tanımı yeni planda güncellendi | Tam/doğru kaynak kimliği henüz doğrulanmadı; başka başlıklı metin yerine konulmaz |
| SOUL Academy | Keşif notu; karar veya doğrudan iş açma yetkisi değil | Önceki Library okuması var; A3'te gerçek gövde ve kimlik bağlanacak |

Aktarım sadakatinin tamamının doğrulandığı iddia edilmez. Dış değerlendirme yalnız [devos/plan/Inceleme_Degerlendirmesi_ChatGPT.md](https://github.com/batuhanozgun/devos/blob/main/plan/Inceleme_Degerlendirmesi_ChatGPT.md) üzerinden bulunur; burada kopyalanmaz ve yeni karara bağlanmaz. Önceki yerel dosya gözlemleri bugün otomatik erişim kanıtı değildir; A3 gerçek byte'ları yeniden doğrular.

## 6. Denetim ve son teslim yükü

Başlangıç: **`8cd01e4afdcd0d37960b05930c91e1244678be6e`**. [BASELINE.json](maintenance/2026-09-29-research-installation-separation/BASELINE.json) başlangıç tree/blob ve istek hash'ini taşır. A1 kök README'nin eski gövdesini aynı blob ile denetim kopyasında korudu. A2 dosya taşımadı veya silmedi.

Her tur ve yayın öncesi main ilerlediyse delta/yazarlar incelenir; başka çalışmanın değişikliği geri alınmaz. Yayın force push olmadan yapılır. Çakışan güncelleme sessizce ezilmez. Makine hesabı commit'i görülürse kullanıcıya bildirimden önce düzeltme yapılmaz. Bu turun başlangıç main'i `9620dfd` üzerinde author/committer kapsamındaki makine hesabı sorguları boştu; bu bütün dal ve kimliklerde yokluk ispatı değildir.

A4 taraması en az `Codex`, `güncel`, `current`, `sıradaki`, `next`, `DEVOS-001`, `DEVOS-002`, P4/P5 ve eski hedef repo adlarını kapsar. Sonuçlar tam izlenen yol envanteriyle karşılaştırılır. Eşleşme hata veya aramada bulunmama yokluk kanıtı değildir: tarihsel alıntılar, gerçek eski kanıt ve aktif araştırmanın kendi sonraki işi gerekçeyle korunabilir. Pasif arşiv içeriği talimat diye uygulanmaz.

A5: sıfır silinen dosya; değişmeyen kontrol blob/tree kimlikleri; araştırma gövdelerinin korunması; yalnız gerekçeli statü/yön farkları; varsa taşımada eski/yeni byte eşliği ve link düzeltmesi; gerçek kaynak erişimi; tam değişiklik/ekleme/taşıma listesi; görev §3 dışında yapılanların gerekçesi; commit bağlantıları; kalan ifadelerin nedeni ve erişim açıkları.

Tam tarama ve arşiv erişimi yapılmadığı için **“eski yönü güncel gösteren hiçbir kayıt kalmadı” henüz söylenemez**. Erişilemeyen arşiv ilgili paketi açık bırakır; bağımsız yönlendirme düzeltmesini engellemez. Yeni teknik/ürün kararı üretmek, eski planı kurmak veya paket uydurmak çözüm değildir.

## 7. Devralma

**Tek sonraki iş: A2 §4.6 — current/reviews içindeki kalan 16 dosya.** Önce main delta/yazar kontrolü; sonra bu dosya, A2-REVIEWS ve başlangıç envanterinin 26–41 satırları. İlk kalan iki dosya `2026-09-06-stage-1a/` altındaki CODEX-RESPONSE ve REVIEW'dır. Kaynaklar tam okunur; durum ve gerekçeler dosya bazında kaydedilir. A2'nin diğer açık doğrudan girişleri bundan sonra gelir.

Yeni oturum eski COORD/G0/G1 brief'inden, EXP-006 S00'ından, DEVOS-001/002 görevinden veya dış DevOS kurulumundan başlamaz. Bu bakımın tek güncel devam kaydı bu dosyadır; önceki tarihli denetimlerdeki “sonraki” ifadeleri onların kendi turuna aittir.
