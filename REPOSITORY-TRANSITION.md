# Araştırma / kurulum ayrımı — depo bakım çalışması

**Kimlik:** REPO-SEPARATION-20260929  
**Durum:** DEVAM EDİYOR — A1 tamam. A2'de D030/13 ana giriş ile 21 doğrudan teslim, mesaj ve alan girişi ele alındı; kalan eski current/devir girişleri açık. A3 arşivi, A4 genel tarama ve A5 son denetim tamamlanmadı.  
**Güncelleme:** 29 Eylül 2026. **Yazar:** ChatGPT, Batu'nun açık yetkisiyle.  
**Kaynak:** [Görev belgesinin değiştirilmemiş kopyası](maintenance/2026-09-29-research-installation-separation/REQUEST.md). İş, kullanıcının isteğiyle turlara bölünmüştür.

Bu dosya yalnız `agentic-os-search` deposunu güncelleme çalışmasının planı, ilerleme kaydı ve devir noktasıdır. Yeni DevOS kurulum planı, SOUL iş listesi, mimari veya agent-control dosyası değildir.

## 1. Amaç ve yetki

Depoyu ilk kez okuyan Claude Code kurucusu araştırma kütüphanesini tarihsel DevOS kurulum kayıtlarından ayırabilmeli; eski Codex/P5/DEVOS-001/002 yönlerini güncel kurulum işi sanmamalıdır. Araştırma içeriği, özgün kararların tarihçesi ve kanıt sınırları korunur.

DevOS'un geçerli yönü **Claude Code cloud**; kurulum planının tek evi [batuhanozgun/devos — plan/](https://github.com/batuhanozgun/devos/tree/main/plan), görevde belirtilen devir sürümü **2.1**'dir. Planın kopyası bu depoya konulmaz. Yeni ürün deposu `batuhanozgun/soul-system`; eski `batuhanozgun/soul` ve görevde sayılan diğer eski denemeler değiştirilmez.

Yazma yalnız `batuhanozgun/agentic-os-search` içindedir. `AGENT.md` ve `agent/**` değiştirilmez. Başka depolara, Supabase projelerine, hesaplara veya erişim ayarlarına yazılmaz. Kurulum yapılmaz. Aktif araştırma paketlerinin kendi durumları korunur; bunlar Claude Code için kurulum talimatı değildir.

`batuhanozgun-devos` makine hesabının teknik yazma imkânı yazma yetkisi değildir. Bu hesapla ilişkilendirilmiş commit görülürse düzeltmeden önce Batu'ya bildirilir. Her yayın öncesi main delta ve yazar kontrolü yenilenir. Hesap erişimini kaldırma bu bakımın işi değildir.

Görev kaynağındaki tarihli platform karşılaştırmaları kullanıcıdan alınan bağlamdır; bu bakım onları yeni teknik yeterlik veya fiyat doğrulaması olarak onaylamaz. Verilmiş platform kararı yeniden açılmaz.

## 2. Ayrımın tasarımı

**Yerinde statü ve yönlendirme ayrımı; toplu taşıma yok.**

- Foundation, studies, concepts ve kavramsal explorations kendi yerinde kalır; araştırma anlamı değişmez.
- Eski kurulum/planlama ve devir dosyalarının başına tarihli statü notu konur; eski gövde, kaynak kullanıcı sözleri ve test/öneri sınırları korunur. “Tarihsel” statü, bulguyu hipoteze veya öneriyi karara dönüştürmez. Yeni ortamın da Claude olması eski Claude taslağını kendiliğinden etkinleştirmez.
- Kök ve alan girişlerinde araştırma, tarihsel kurulum, kontrol ve yayın ayrılır. Doğrudan alt dosya açılışları da incelenir; kök uyarısı tek başına son kabul değildir. Araştırma dizinindeki güncel araştırma rotaları topluca tarihsel ilan edilmez.
- Erişilebilir eski rapor/paket kopyaları için `archives/devos-pre-claude-2026-09-29/` A3'te hazırlanacaktır. Şu an oluşturulmuş ve eksiksiz arşiv sayılmaz. Özgün gövdeler değişmez; statü, erişim ve kimlik yan kayıtlarda tutulur.
- [MOVES.md](MOVES.md) gerçekleşen taşımaları tutar. **Taşıma yok.** Kopya ve kaynak bağı ayrı kaydedilir. Çok dosyalı taşıma gerekirse uygulamadan önce Batu'ya kısa plan sunulur.

## 3. Beş iş paketi ve kapanış koşulları

Paket gerektiğinde birkaç tur sürer; numarası otomatik tur sayısı değildir. Her tur doğrulanmış sonucu ve tek devam noktasını kaydeder.

| Paket | İş ve kapanış koşulu | Durum |
|---|---|---|
| **A1 — Başlangıç ve kalıcı plan** | Görev, başlangıç kimlikleri, yazar sınırı, dış plan adresi, kök yönlendirme; uzak yayın ve geri okuma | **TAMAM:** `ab8ef329aa4841fae2b836c91e74e68ad1c4c9e5` |
| **A2 — Karar ve güncel yönler** | D030; EXP-006 ve deneme/bağlam girişleri; doğrudan eski devirler; eski kurulum bu yollardan güncel diye devralınamıyor | **DEVAM:** 13 ana giriş + 21 doğrudan giriş. Kalan current/devir kapsamı §4'te |
| **A3 — Rapor ve paket arşivi** | Yedi kaynak ailesini gerçek gövde ve kimlikle arşivle; farklı P5 paketlerini karıştırma; erişilemeyeni yeniden üretme | BEKLİYOR. Her kaynak için doğrulanmış gövde veya açık erişim engeli gerekir |
| **A4 — Depo geneli tarama** | Bütün izlenen yollar, metinler ve gerekli belge/ZIP içleri; riskli eşleşmeler için düzeltme veya gerekçeli koruma; okunmayan kapsam açık | BEKLİYOR. Araştırma anlamı değişmez; listeyle sınırlı tarama yetmez |
| **A5 — Son karşılaştırma ve teslim** | Başlangıçtan son commit'e fark; silme/taşıma/gövde ve bağlantı denetimi; yeni okuyucu yürüyüşü; tam değişiklik/gerekçe listesi | BEKLİYOR. Kapsamı aşmayan tamamlanma hükmü ve erişim açıkları teslim edilir |

## 4. A2 — tamamlanan alt kümeler ve kalan

### 4.1 Ana girişler ve D030

[A2-CORE](maintenance/2026-09-29-research-installation-separation/A2-CORE.md) 13 dosyayı, başlangıç blob'larını ve gerekçeleri listeler. **Yayımlanmış commit:** `8612f1320dbfeeef089964d4c48025051f1bb0e6`; main geri okuması önceki turda ve bu turun başında doğrulandı. Kaynak dosyalarının farkı 160 ek satır, 0 çıkarılan satırdır. Aynı kayıttaki `0145e407...` yalnız içerik doğrulama adayıdır; yayın kimliğiyle karıştırılmaz.

D030; EXP-006 STATE/HANDOFF/INDEX/WORK/DECISIONS ve eski CODEX_START; development-os INDEX/001 WORK/002 README; soul-context README/INDEX/STATE/repos-soul girişleri bu kümededir. D027/D029'un ortam kararı geçersiz kılındı; özgün gövdeler ve yüksek kalite/sağlayıcı bağımsızlığı hedefinin tarihçesi korundu.

### 4.2 Doğrudan teslim, mesaj ve alan girişleri

[A2-DIRECT-ENTRIES](maintenance/2026-09-29-research-installation-separation/A2-DIRECT-ENTRIES.md) ikinci kümenin tam listesini, kaynak blob'larını, okuma ve kontrol sınırını taşır:

- EXP-006 work/P4-01–P4-05 ve P5-01: 6 dosya.
- DEVOS-001 BRIEF/METHOD/EXCHANGE/REVIEW: 4 dosya; R-001–R-006: 6 dosya.
- Eski Claude hazırlığı WORK ve CLAUDE-TASK-01: 2 dosya.
- research/INDEX, explorations/INDEX ve explorations/CATALOG: 3 dosya.

İçerik adayı **`ac026aba9de076dbf0181c748b51a1a279c01783`**, tree `93f422340cec206ca4efd802d3d77c50aa1a8f2e`, başlangıç parent `8612f1320dbfeeef089964d4c48025051f1bb0e6`. GitHub compare ve bütün kaynak patch'lerinin okuması: **21 dosya; her birinde yalnız başlangıçta 6 ek satır; toplam 126 ek satır, 0 çıkarılan satır**. Özgün gövdeler değişmedi. Bu doğrulama adayının varlığı tek başına main yayını değildir; kaynaklar ve bu bakım kaydı aynı son yayın ağacında bulunur, gerçek yayın kimliği main'den geri okunur.

Bu turun yaptığı iş statü/yönlendirmedir; raporların kendilerinin arşivlenmesi veya içlerindeki platform/test iddialarının yeniden doğrulanması değildir. S paketi ile K paketi ayrı kimlikler olarak kalır. Güncel dış kurulum planı bu depoya kopyalanmadı.

### 4.3 Tek kalan A2 çalışma paketi

**Önce `research/soul-context/current/**` altındaki kalan eski bootstrap, koordinasyon, brief ve review girişlerini eksiksiz envanterle ve kapat.** Yalnız yukarıdaki iki Claude hazırlık dosyası ele alındı. `OWNER-CONTEXT.md`, `SOURCE-REGISTER.md`, diğer current dosyaları ve alt dizinleri bu tur tam okunmuş/düzeltilmiş değildir. API ağaç çıktısının kesilmiş olması yüzünden görünen yollar tam envanter sayılmadı; sonraki tur bunu tamamlar.

DEVOS-001 `reading/` girişleri ile EXP-006'nın P1/P2/P3 gibi diğer doğrudan yollarında statü/yön gerekip gerekmediği aynı kalan kapsamda kontrol edilir. Araştırma veya özgün kaynak gövdesi yeniden yazılmaz; gerekçeli koruma da sonuçtur. Bu tur tamamlanan 21 dosya tekrar baştan düzenlenmez.

A2 kapanışı, A4'ün bütün depo taramasını ve A5'in yeni okuyucu/bağlantı değerlendirmesini ikame etmez. Özellikle arama çıktısının tarihsel başlığı atladığı durumlar son değerlendirmede gözden kaçırılmaz.

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

Aktarım sadakatinin tamamının doğrulandığı iddia edilmez. Dış değerlendirme yalnız [devos/plan/Inceleme_Degerlendirmesi_ChatGPT.md](https://github.com/batuhanozgun/devos/blob/main/plan/Inceleme_Degerlendirmesi_ChatGPT.md) üzerinden bulunur; burada kopyalanmaz ve yeni karara bağlanmaz.

## 6. Denetim ve son teslim yükü

Başlangıç: **`8cd01e4afdcd0d37960b05930c91e1244678be6e`**. [BASELINE.json](maintenance/2026-09-29-research-installation-separation/BASELINE.json) başlangıç tree/blob ve istek hash'ini taşır. A1 kök README'nin eski gövdesini aynı blob ile denetim kopyasında korudu. A2 dosya taşımadı veya silmedi.

Her tur ve yayın öncesi main ilerlediyse delta/yazarlar incelenir; başka çalışmanın değişikliği geri alınmaz. Yayın force push olmadan yapılır. Çakışan güncelleme sessizce ezilmez. Makine hesabı commit'i görülürse kullanıcıya bildirimden önce düzeltme yapılmaz.

A4 taraması en az `Codex`, `güncel`, `current`, `sıradaki`, `next`, `DEVOS-001`, `DEVOS-002`, P4/P5 ve eski hedef repo adlarını kapsar. Sonuçlar tam izlenen yol envanteriyle karşılaştırılır. Eşleşme hata veya aramada bulunmama yokluk kanıtı değildir: tarihsel alıntılar, gerçek eski kanıt ve aktif araştırmanın kendi sonraki işi gerekçeyle korunabilir. Pasif arşiv içeriği talimat diye uygulanmaz.

A5: sıfır silinen dosya; değişmeyen kontrol blob/tree kimlikleri; araştırma gövdelerinin korunması; yalnız gerekçeli statü/yön farkları; varsa taşımada eski/yeni byte eşliği ve link düzeltmesi; gerçek kaynak erişimi; tam değişiklik/ekleme/taşıma listesi; §3 dışında yapılanların gerekçesi; commit bağlantıları; kalan ifadelerin nedeni ve erişim açıkları.

Tam tarama ve arşiv erişimi yapılmadığı için **“eski yönü güncel gösteren hiçbir kayıt kalmadı” henüz söylenemez**. Erişilemeyen arşiv ilgili paketi açık bırakır; bağımsız yönlendirme düzeltmesini engellemez. Yeni teknik/ürün kararı üretmek, eski planı kurmak veya paket uydurmak çözüm değildir.

## 7. Devralma

**Tek sonraki iş: A2 §4.3 — kalan eski current/devir girişleri.** Önce main delta/yazar kontrolü; sonra bu dosya ve A2-DIRECT-ENTRIES; ardından eksiksiz current alt-ağaç envanteri ve ilgili dosyaların tam okuması. Yeni oturum eski EXP-006 S00'ından, DEVOS-001/002 görevinden veya dış DevOS kurulumundan başlamaz.
