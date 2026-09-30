# Araştırma / kurulum ayrımı — depo bakım çalışması

**Kimlik:** REPO-SEPARATION-20260929  
**Durum:** DEVAM EDİYOR — A1 tamam. A2'de current başlangıç envanteri 41/41, reviews grubu 22/22 ve DEVOS-001 reading grubu 4/4 statü bakımından sonuçlandırıldı. EXP-006 P1/P2/P3 ve kalan doğrudan girişler, A3 arşivi ve A4/A5 açık.  
**Güncelleme:** 30 Eylül 2026. **Yazar:** ChatGPT, Batu'nun açık yetkisiyle.  
**Kaynak:** [Görev belgesinin değiştirilmemiş kopyası](maintenance/2026-09-29-research-installation-separation/REQUEST.md). İş, kullanıcının isteğiyle turlara bölünmüştür.

Bu dosya yalnız `agentic-os-search` deposunu güncelleme çalışmasının planı, ilerleme kaydı ve devir noktasıdır. Yeni DevOS kurulum planı, SOUL iş listesi, mimari veya agent-control dosyası değildir. Bu sürüm ilerleme ve devir kısmını günceller; önceki kayıt `bc015e2f97beb9c281bd54a071916324459bc502` commit'inde, blob `22ed921ad327ae735674617f3db3845aef85e532` olarak korunur.

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
| **A2 — Karar ve güncel yönler** | D030; EXP-006 ve deneme/bağlam girişleri; doğrudan eski devirler; eski kurulum bu yollardan güncel diye devralınamıyor | **DEVAM:** current 41/41 (reviews 22/22 dahil); DEVOS-001 reading 4/4. EXP-006 P1/P2/P3 ve kalan doğrudan girişler §4.9'da açık |
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

[A2-BRIEFS](maintenance/2026-09-29-research-installation-separation/A2-BRIEFS.md) dokuz dosyanın tam listesini, başlangıç blob'larını, gerekçeleri ve kontrol sınırını taşır. Envanterin **03–05 ve 10–15** satırlarıdır: COORD-01/02/03, G0-D1, G1, G1-R1, Stage-1, Stage-1A ve Stage-2/G0. **Gerçek yayın commit'i `9620dfdeda71f25580f6945c2bb3a11c19b78703`**.

Dokuz dosyanın tamamı sabit başlangıç commit'inden okundu. Düzeltilmiş içerik doğrulama adayı **`3a371a2b653b6eb37b0c78cd5921b8f24e3c510f`**, tree **`7cf7d124d62e06cc2a6f112dd9efafde0745755c`**, parent `cd35ef63d9a80dd6ff224726d2b083fa386a3c59`: her dosyada yalnız başlangıçta 6 ek satır, **toplam 54 ek satır ve 0 çıkarılan satır**. Tam birleşik diff'te bütün hunk'lar dosya başındadır; özgün gövdeler korunur. İlk yayımlanmamış `2369810...` adayındaki dört son-satır-sonu farkı giderildi.

Bu tur sonunda `briefs/` grubunun 13 dosyasının doğrudan giriş statüsü ele alınmış, current alanının 41 başlangıç dosyasından 19'u işlenmiş ve 22 review/kanıt dosyası açık kalmıştı. Bu tarihli sonuç, aşağıdaki yeni incelemelerin yerine geçmez.

### 4.5 İlk altı review/kanıt kaydı

[A2-REVIEWS](maintenance/2026-09-29-research-installation-separation/A2-REVIEWS.md)'ın korunmuş ilk küme bölümü, envanterin **20–25** satırlarının tam okumasını, beş not ve bir gerekçeli koruma kararını, kaynak kimliklerini ve doğrulama sınırını taşır. Direction, G0 ve Stage-1 çiftleridir; toplam başlangıç gövdesi **91.072 byte**. **Gerçek yayın commit'i `4e1eaee7f2e888cc8b51e67ace2edd2aebf9fef6`**.

Beş not; ham opening vision'ın eski Routing gate'ini, ham Codex tasarım cevabını ve üç REVIEW dosyasındaki eski güncel/sonraki önerileri tarihsel bağlama alır. G0 `EVIDENCE-EXTRACTS.md` ilk paragrafta zaten tarihli seçili kanıt olduğunu, talimat veya canlı durum olmadığını açıkça belirttiği için değiştirilmedi. Yeni not eklememek de gerekçeli inceleme sonucudur.

Düzeltilmiş içerik adayı **`50e4dcd27ac8a9025d4778a1148c8eb6c321ac8c`**, tree **`eb90660ac6aade7e7fc892d03467e3c18090a1af`**, parent `9620dfdeda71f25580f6945c2bb3a11c19b78703`: beş dosyada yalnız başa toplam **30 ek satır, 0 çıkarılan satır**. Özgün gövdeler ve dosya sonları korundu. Ham aktarımların eski hash/satır kimliklerinin not hariç gövdeye ait olduğu ve öneksiz sabit kaynak bağlantıları açıkça yazıldı.

Bu kümenin sonunda current alanında **25/41**, reviews grubunda **6/22** başlangıç dosyası sonuçlandırılmıştı. Önceki denetim kayıtları tarihli tutulur; her tur yeni bir yetkili durum kaynağına dönüştürülmez. Yeni platform, eski deney veya bağımsız Claude davranış doğrulaması yapılmadı.

### 4.6 Stage-1A ve COORD zinciri — dokuz kayıt

[A2-REVIEWS](maintenance/2026-09-29-research-installation-separation/A2-REVIEWS.md)'ın ikinci küme bölümü, envanterin **26–34** satırlarının tam listesini, başlangıç blob'larını, gerekçelerini ve okuma/denetim sınırlarını taşır. Stage-1A yanıtı ve incelemesi; collaboration incelemesi; COORD-01 yanıtı ve incelemesi; COORD-02'nin üç kaydı; COORD-03 incelemesi: **dokuz dosya, 101.729 byte özgün kaynak metadata toplamı**. **Gerçek yayın commit'i `67fd24ec4574dbb3d5024cd9acd10d522ee11d00`**, bu turun başında uzak main/ref ve commit nesnesinden doğrulandı.

Kaynakların tamamı bu turun sabit başlangıcı `4e1eaee7f2e888cc8b51e67ace2edd2aebf9fef6` üzerinden okundu. Kaynak-only doğrulama adayı **`8e1f747fc64aed68710b0d867f53dcf86241b99b`**, tree **`0bf08586887d3da5fa23e111fc4aec087fc0a1f5`**, parent aynı başlangıçtır. Her dosyada yalnız altı satırlık başlangıç notu; **toplam 54 ek satır ve 0 çıkarılan satır**. Birleşik patch ve dosya farklarında özgün gövde/EOF değişikliği yoktur.

Eski kontrol taslakları ve G0 önerisi güncel talimat olmaktan ayrıldı. COORD-02'nin ilk dosya talebi → kimlik çözümü → yeni oturum raporu → COORD-03 erişim/bellek sınırı zinciri, eski kaynakları yeniden yazmadan doğrudan girişlerden bulunur. Sonradan karşılanmış eski bir talep, yeni eksik iş sanılarak tekrar açılmaz. Gözlem/aktarım/yorum ayrımları ve platformdan bağımsız ilkeler korunur.

Bu kümenin sonunda reviews **15/22**, current başlangıç envanteri **34/41** sonuçlandırılmıştı. Bu sayılar dosya inceleme kapsamıdır; bütün A2, arşiv, depo geneli tarama veya hedef sistem yeterliği değildir. Önceki altı kaynak ve başlangıç envanteri o tur yeniden düzenlenmedi. Yeni bir bakım alt sistemi veya DevOS iş listesi oluşturulmadı; mevcut bakım kaydı ve plan ilerletildi.

### 4.7 D1, G1, yöntem ve DevOS-02 — son yedi kayıt

[A2-REVIEWS-CLOSE](maintenance/2026-09-29-research-installation-separation/A2-REVIEWS-CLOSE.md), başlangıç envanterinin **35–41** satırlarının tam okumasını, dört not ve üç gerekçeli korumayı, kaynak kimliklerini ve kontrol sınırını taşır. D1 kanıt/inceleme çifti, G1'in iki Markdown kaydı ve Python örneği, yöntem incelemesi, DevOS-02/RPD incelemesi: **yedi dosya, 88.517 byte özgün kaynak metadata toplamı**. **Gerçek yayın commit'i `bc015e2f97beb9c281bd54a071916324459bc502`**, bu turun başlangıcında uzak main'den doğrulandı.

Bu küme sabit başlangıç **`67fd24ec4574dbb3d5024cd9acd10d522ee11d00`** üzerinden okundu. Doğrulanmış kaynak adayı **`62b69e4e91e6d99e468fac9a6e818f634f790b99`**, tree **`19841993cceb2eec63457d7170ef246af7cd5bc5`**, parent aynı başlangıçtır. Dört inceleme dosyasında yalnız başa toplam **24 ek satır, 0 çıkarılan satır** vardır. İlk adayda saptanan iki son-LF farkı yayın öncesinde giderildi. İki kanıt seçkisi ve sentetik Python dosyası mevcut statü açıklıkları yeterli olduğu için değiştirilmedi; Python çalıştırılmadı.

D1→G1 sonucu ve G1→yöntem askıya alma zinciri doğrudan girişte bulunur. DevOS-02 kaydındaki “tek güncel sözleşme”, RPD01/AGENTS değişikliği ve eski hedefe çalışma grant'ı bugünkü yetkiden ayrıldı. RPD kavramı ve platformdan bağımsız güvence/muhakeme içeriği korunur; eski deney veya kontrol görevi uygulanmaz.

**Yeni toplam:** reviews **22/22**, current başlangıç envanteri **41/41** dosya statü bakımından sonuçlandırıldı. Reviews grubunda toplam 18 not, 4 gerekçeli koruma vardır. Sonradan eklenen current README başlangıç sayısına dahil değildir. Bu, bütün depo taramasının veya A2'nin tamamlandığı anlamına gelmez. Önceki kaynaklar ve tarihli denetim kayıtları yeni bir bulgu olmadan yeniden düzenlenmedi.

Kaynak doğrulama adayı tek başına main yayını değildir. Dört kaynak, bu yeni kapanış denetim kaydı ve kök bakım planı aynı nihai ağaçta yayımlanır; gerçek ref ve dosya geri okuması ayrıca doğrulanır. Nihai research alt ağacı kaynak adayındaki `be054da53003bfa4bf9baac4dfae19ee3c8c8acb` ile aynı kalmalı; kontrol dosyaları, silme/taşıma sınırı ve başka çalışma korunmalıdır.

### 4.8 DEVOS-001 reading — dört kayıt

[A2-READING](maintenance/2026-09-29-research-installation-separation/A2-READING.md), dört dosyanın tam listesini, başlangıç kimliklerini, statü gerekçelerini ve doğrulama sınırını taşır. COVERAGE, F00-CONTEXT-AND-USE, F08-FOUNDATION-FRAME ve F08-RECONCILIATION tam okundu; **4/4** sonuçlandırıldı. Bu grup current 41/41 sayısının dışındadır; sayılar birbiriyle toplanmaz.

Başlangıç **`bc015e2f97beb9c281bd54a071916324459bc502`**. Doğrulanmış kaynak adayı **`0d8e4c6ef22df5ebe03e4e124f27f88364dff798`**, tree **`35536add43596d4a004af71be54826b9ecae52d7`**, aynı parent: yalnız dört dosyanın başına **24 ek satır, 0 çıkarılan satır**. F08'in ilk adayda düşen son LF'si yayından önce geri kondu. Özgün gövdeler, kaynak yorumları ve epistemik sınırlar aynen korundu.

F08'in eski tamlık beyanı mevcut düzeltme ekine; eski seri Foundation okuma yönleri de sonraki COVERAGE yöntem kaydına bağlandı. Bu tarihsel sıra güncel DevOS kurulumuna veya Foundation'ın kendi işlerine talimat vermez. Araştırma katkıları geçersiz sayılmadı. Yeni notların dokuz göreli bağlantısı çözüldü; hedefler ve D030 kimliği doğrudan okundu. Eski bütün gövde bağlantılarının denetimi A4/A5'tedir.

Kaynak adayı yayın değildir. Nihai commit yalnız dört reading kaydı, A2-READING ve bu planın ilerleme/devrini kapsar; development-os alt ağacı kaynak adayındaki `e3a104adc534aa5f4caf10f4252b000aae94731b` ile aynı kalmalıdır. Yayın öncesi main/yazar kontrolü ve yayın sonrası ref/dosya geri okuması ayrı yapılır. Önceki kapanmış dosyalar yeniden düzenlenmedi.

### 4.9 Kalan A2 kapsamı

**Tek sonraki iş: EXP-006 P1/P2/P3 doğrudan girişlerinin tam içerik ve statü incelemesi.** `explorations/EXP-006-development-os-calisma-duzeni/work/` ağacından üç yol doğrulandı: `P1-01-claude-cloud-environment-map.md`, `P2-01-named-role-contracts.md`, `P3-01-work-information-discussion.md`. Blob/boyutları A2-READING'de; bu tur yalnız envanterlendiler, gövdeleri okunmuş veya kusurlu ilan edilmedi. Bunlardan sonra kalan doğrudan girişlerde statü/yön gerekip gerekmediği değerlendirilir. Araştırma ve özgün kaynak gövdeleri yeniden yazılmaz.

Current başlangıç envanterinin 41 dosyası, reviews grubunun 22 dosyası ve DEVOS-001 reading grubunun dört dosyası yeni maddi bulgu olmadan tekrar düzenlenmez. Önceki tamamlanan alt kümeler sırf tur değişti diye yeniden açılmaz. Eski Python/deney kaydı bulmak çalıştırma talimatı değildir.

A2 kapanışı, A4'ün bütün depo taramasını ve A5'in yeni okuyucu/bağlantı değerlendirmesini ikame etmez. Arama çıktısının tarihsel başlığı atladığı durumlar ve eski gövde bağlantıları son değerlendirmede ayrıca ele alınır. Current alanının statü incelemesinin bitmesi bütün kütüphanenin aktarım ve erişim doğrulaması değildir.

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

Her tur ve yayın öncesi main ilerlediyse delta/yazarlar incelenir; başka çalışmanın değişikliği geri alınmaz. Yayın force push olmadan yapılır. Çakışan güncelleme sessizce ezilmez. Makine hesabı commit'i görülürse kullanıcıya bildirimden önce düzeltme yapılmaz. Bu turun başlangıç main'i `bc015e2` üzerinde author/committer kapsamındaki makine hesabı sorguları boştu; bu bütün dal ve kimliklerde yokluk ispatı değildir.

A4 taraması en az `Codex`, `güncel`, `current`, `sıradaki`, `next`, `DEVOS-001`, `DEVOS-002`, P4/P5 ve eski hedef repo adlarını kapsar. Sonuçlar tam izlenen yol envanteriyle karşılaştırılır. Eşleşme hata veya aramada bulunmama yokluk kanıtı değildir: tarihsel alıntılar, gerçek eski kanıt ve aktif araştırmanın kendi sonraki işi gerekçeyle korunabilir. Pasif arşiv içeriği talimat diye uygulanmaz.

A5: sıfır silinen dosya; değişmeyen kontrol blob/tree kimlikleri; araştırma gövdelerinin korunması; yalnız gerekçeli statü/yön farkları; varsa taşımada eski/yeni byte eşliği ve link düzeltmesi; gerçek kaynak erişimi; tam değişiklik/ekleme/taşıma listesi; görev §3 dışında yapılanların gerekçesi; commit bağlantıları; kalan ifadelerin nedeni ve erişim açıkları.

Tam tarama ve arşiv erişimi yapılmadığı için **“eski yönü güncel gösteren hiçbir kayıt kalmadı” henüz söylenemez**. Erişilemeyen arşiv ilgili paketi açık bırakır; bağımsız yönlendirme düzeltmesini engellemez. Yeni teknik/ürün kararı üretmek, eski planı kurmak veya paket uydurmak çözüm değildir.

## 7. Devralma

**Tek sonraki iş: A2 §4.9 — EXP-006 P1/P2/P3 doğrudan girişleri.** Önce main delta/yazar kontrolü; sonra bu dosya ve A2-READING okunur. İlk kaynak `work/P1-01-claude-cloud-environment-map.md`, ardından `work/P2-01-named-role-contracts.md` ve `work/P3-01-work-information-discussion.md`; üçü de EXP-006 dizinindedir. Kaynaklar tam okunur, eski görevler uygulanmadan statü/yön değerlendirmesi yapılır. Kalan doğrudan girişler sonuçlandırılınca A3, A4 ve A5 sırası korunur. DEVOS-001 reading grubu yeniden başlatılmaz.

Yeni oturum eski COORD/G0/G1 brief'inden, EXP-006 S00'ından, DEVOS-001/002 görevinden veya dış DevOS kurulumundan başlamaz. Bu bakımın tek güncel devam kaydı bu dosyadır; önceki tarihli denetimlerdeki “sonraki” ifadeleri onların kendi turuna aittir.
