# Araştırma / kurulum ayrımı — depo bakım çalışması

**Kimlik:** REPO-SEPARATION-20260929  
**Durum:** DEVAM EDİYOR — A1 ve A2'nin belge düzeyindeki doğrudan giriş denetimi tamam. A3'te beş geri kazanılmış ailenin repository gövde erişimi doğrulandı: 19 özgün dosya yüklenen ZIP'te, Academy ayrıca bağımsız dosyada. S00–S12 ile SOUL ve DevOS kaynaklarının erişimi açık. A4 depo geneli tarama ve A5 son denetim bekliyor.  
**Güncelleme:** 30 Eylül 2026. **Yazar:** ChatGPT, Batu'nun açık yetkisiyle.  
**Kaynak:** [Görev belgesinin değiştirilmemiş kopyası](maintenance/2026-09-29-research-installation-separation/REQUEST.md). İş, kullanıcının isteğiyle turlara bölünmüştür.

Bu dosya yalnız `agentic-os-search` deposunu güncelleme çalışmasının planı, ilerleme kaydı ve devir noktasıdır. Yeni DevOS kurulum planı, SOUL iş listesi, mimari veya agent-control dosyası değildir. Bu sürüm ilerleme ve devir kısmını günceller; önceki kayıt `93216f73ea565ed3ba22e4ba0e18e2144e1368c4` commit'inde, blob `dfde2901266b1587824fbd772a410e435761b957` olarak korunur.

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
- Eski rapor/paket kopyaları [archives/devos-pre-claude-2026-09-29/](archives/devos-pre-claude-2026-09-29/README.md) altındadır. Beş geri kazanılmış ailenin 19 özgün dosyası doğrulanmış repository ZIP'inde, Academy ayrıca bağımsız dosyadadır. **Eksiksiz arşiv değildir:** iki kaynağın erişimi açık. ZIP üyesi ile bağımsız repository yolu ayrı kaydedilir; özgün gövdeler değişmez.
- [MOVES.md](MOVES.md) gerçekleşen taşımaları tutar. **Taşıma yok.** Kopya ve kaynak bağı ayrı kaydedilir. Çok dosyalı taşıma gerekirse uygulamadan önce Batu'ya kısa plan sunulur.

## 3. Beş iş paketi ve kapanış koşulları

Paket gerektiğinde birkaç tur sürer; numarası otomatik tur sayısı değildir. Her tur doğrulanmış sonucu ve tek devam noktasını kaydeder.

| Paket | İş ve kapanış koşulu | Durum |
|---|---|---|
| **A1 — Başlangıç ve kalıcı plan** | Görev, başlangıç kimlikleri, yazar sınırı, dış plan adresi, kök yönlendirme; uzak yayın ve geri okuma | **TAMAM:** `ab8ef329aa4841fae2b836c91e74e68ad1c4c9e5` |
| **A2 — Karar ve güncel yönler** | D030; EXP-006 ve deneme/bağlam girişleri; doğrudan eski devirler; eski kurulum bu yollardan güncel diye devralınamıyor | **BELGE DÜZEYİNDE TAMAM:** §4.10–4.11 ve A2-CLOSE. Depo geneli yokluk veya bağımsız kurucu davranışı iddiası değildir |
| **A3 — Rapor ve paket arşivi** | Yedi kaynak ailesini gerçek gövde ve kimlikle arşivle; farklı P5 paketlerini karıştırma; erişilemeyeni yeniden üretme | **DEVAM:** §5. Beş ailenin gövdeleri repository ZIP'inde doğrulandı; yükleme engeli kapandı. İki kaynağın erişim açığı ve A3 kapanış/engel değerlendirmesi kaldı |
| **A4 — Depo geneli tarama** | Bütün izlenen yollar, metinler ve gerekli belge/ZIP içleri; riskli eşleşmeler için düzeltme veya gerekçeli koruma; okunmayan kapsam açık | BEKLİYOR. Araştırma anlamı değişmez; listeyle sınırlı tarama yetmez |
| **A5 — Son karşılaştırma ve teslim** | Başlangıçtan son commit'e fark; silme/taşıma/gövde ve bağlantı denetimi; yeni okuyucu yürüyüşü; tam değişiklik/gerekçe listesi | BEKLİYOR. Kapsamı aşmayan tamamlanma hükmü ve erişim açıkları teslim edilir |

## 4. A2 — tamamlanan alt kümeler ve kapanış

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

[A2-READING](maintenance/2026-09-29-research-installation-separation/A2-READING.md), dört dosyanın tam listesini, başlangıç kimliklerini, statü gerekçelerini ve doğrulama sınırını taşır. COVERAGE, F00-CONTEXT-AND-USE, F08-FOUNDATION-FRAME ve F08-RECONCILIATION tam okundu; **4/4** sonuçlandırıldı. Bu grup current 41/41 sayısının dışındadır; sayılar birbiriyle toplanmaz. **Gerçek yayın commit'i `85700994390f7f0532678f759754cdd7f0b87ab2`**, bu turun başlangıcında uzak main/ref ve commit nesnesinden doğrulandı.

Başlangıç **`bc015e2f97beb9c281bd54a071916324459bc502`**. Doğrulanmış kaynak adayı **`0d8e4c6ef22df5ebe03e4e124f27f88364dff798`**, tree **`35536add43596d4a004af71be54826b9ecae52d7`**, aynı parent: yalnız dört dosyanın başına **24 ek satır, 0 çıkarılan satır**. F08'in ilk adayda düşen son LF'si yayından önce geri kondu. Özgün gövdeler, kaynak yorumları ve epistemik sınırlar aynen korundu.

F08'in eski tamlık beyanı mevcut düzeltme ekine; eski seri Foundation okuma yönleri de sonraki COVERAGE yöntem kaydına bağlandı. Bu tarihsel sıra güncel DevOS kurulumuna veya Foundation'ın kendi işlerine talimat vermez. Araştırma katkıları geçersiz sayılmadı. Yeni notların dokuz göreli bağlantısı çözüldü; hedefler ve D030 kimliği doğrudan okundu. Eski bütün gövde bağlantılarının denetimi A4/A5'tedir.

Kaynak adayı yayın değildir. Nihai commit yalnız dört reading kaydı, A2-READING ve bu planın ilerleme/devrini kapsar; development-os alt ağacı kaynak adayındaki `e3a104adc534aa5f4caf10f4252b000aae94731b` ile aynı kalmalıdır. Yayın öncesi main/yazar kontrolü ve yayın sonrası ref/dosya geri okuması ayrı yapılır. Önceki kapanmış dosyalar yeniden düzenlenmedi.

### 4.9 EXP-006 P1/P2/P3 — üç doğrudan giriş

[A2-P1-P3](maintenance/2026-09-29-research-installation-separation/A2-P1-P3.md), üç dosyanın tam listesini, başlangıç kimliklerini, gerekçelerini ve doğrulama sınırını taşır. P1-01, P2-01 ve P3-01 baştan sona okundu; **3/3** statü bakımından sonuçlandırıldı. Bu sayılar önceki current veya reading gruplarının paydasını değiştirmez. **Gerçek yayın commit'i `94799de0cd4ccf1396ad047a505162a2be2b2ca5`**, bu turun başlangıcında uzak main/ref ve commit nesnesinden doğrulandı.

Başlangıç **`85700994390f7f0532678f759754cdd7f0b87ab2`**. Kaynak doğrulama adayı **`4ef54ef101d2c866c619ef28f10882c775476a66`**, tree **`9e7412528e707ffb2784c841876ce0a7f9fecdd8`**, aynı parent: yalnız üç kaynağın başına **18 ek satır, 0 çıkarılan satır**. Birleşik diff ve üç patch okundu; özgün gövde ve dosya sonları korundu.

P1'in zaten Claude'u konu alması eski seçenekleri güncel yapmıyor. P2'nin ilk 16 sözleşmesi aday statüsünde; P3'te genişleyen G/Y profilleriyle tarihsel bağı görünür. P3'te D021'in sınırlı kullanıcı kabulü, bakım ve H1–H6 yükleri korunurken eski P4'e geçiş güncel görevden ayrıldı. Yeni notların yedi göreli bağlantısı çözüldü, D030 kimliği ayrıca okundu. Geçmiş platform ve deney beyanları yeniden doğrulanmış sayılmadı.

Kaynak adayı main yayını değildir. Nihai commit yalnız bu üç kaynak, A2-P1-P3 ve kök bakım planını kapsar; explorations alt ağacı kaynak adayındaki `e7d395aeb8d7afa73323af66f96003453559ecf3` ile aynı kalmalıdır. Yayın öncesi main/yazar kontrolü ve yayın sonrası ref/dosya geri okuması ayrı yapılır.

### 4.10 ACTORS ve Context — son iki doğrudan giriş

[A2-CLOSE](maintenance/2026-09-29-research-installation-separation/A2-CLOSE.md), iki dosyanın tam okumasını, bir statü notunu, bir gerekçeli korumayı ve A2 kapanış değerlendirmesini taşır. ACTORS'ın ilk rol taslağını “current tasarım” diye gösteren başlığı ve eski P3–P5 sırası tarihsel statüye bağlandı. Context'in mevcut Authority notu zaten kronoloji ile güncel yetkiyi ayırdığı; yönlendirdiği STATE/HANDOFF/WORK de D030'u taşıdığı için Context değiştirilmedi. **Gerçek yayın commit'i `58eaaf5f1dfe2f22deecdc07420deb503e95f7d6`**, A3 başlangıcında uzak main/ref'ten doğrulandı.

Başlangıç **`94799de0cd4ccf1396ad047a505162a2be2b2ca5`**. Doğrulanmış kaynak adayı **`bea42b62c23723f61d7624a9c034598d54725020`**, tree **`e1d3760f1efa397b1ae599b1cebb3c22b9cb8e2e`**, aynı parent: yalnız ACTORS başında **6 ek satır, 0 çıkarılan satır**. İlk adayda düşen bölüm boş satırı ve son LF yayından önce geri kondu. Context blob'u `d368b3cb9ce90a2279fff077da4125557ce71551` olarak korunur. Yeni notun üç göreli bağlantısı çözüldü; D030 kimliği ve Context'in üçlü durum/devralma yolu doğrudan okundu.

Kaynak adayı main yayını değildir. Nihai yayın yalnız ACTORS, A2-CLOSE ve bu planın ilerleme/devrini içerir. Yayın öncesi main/yazar kontrolü, yayın sonrası ref/dosya geri okuması ve kontrol kimliklerinin korunması ayrıca denetlenir. Yeni bir kurulum veya araştırma görevi başlatılmaz.

### 4.11 A2 kapanışı ve açık kalan kapsam

**A2 belge düzeyinde tamamlandı.** D030, kök/alan girişleri, eski deneme/devir/mesajlar, current başlangıç envanteri 41/41 (reviews 22/22 dahil), DEVOS-001 reading 4/4, P1/P2/P3 3/3 ve son ACTORS/Context 2/2 dosya sonuçları A2-CLOSE'daki kapanış tablosunda bağlandı. Örtüşen gruplar toplanarak yeni toplam üretilmedi. Önceki tamamlanmış kaynaklar sırf tur değişti diye yeniden düzenlenmedi.

Bu kapanış mevcut doğrudan giriş ölçütüne ilişkindir; bağımsız Claude davranış deneyi değildir. B/S1/history/sources dahil bütün kalan içeriklerin, arama sonucunda başlık dışından girişin ve eski gövde bağlantılarının kapsamlı taraması A4'te; başlangıçtan bütün fark ve yeni okuyucu değerlendirmesi A5'tedir. **“Eski yönü güncel gösteren hiçbir kayıt kalmadı” henüz söylenemez.** Bu kalan yükler A2 kapanışıyla kaldırılmadı.

**Tek sonraki iş A3'tür:** §5'teki yedi kaynak ailesinin gerçek gövde/kimlik ve erişim envanteri; ardından özgün kopyaların statü yan kayıtlarıyla arşivlenmesi. A3, A4 ve A5 sırası korunur. Eski Python/deney kaydı bulmak çalıştırma talimatı değildir.

## 5. A3 kaynak matrisi ve doğrulanmış ZIP erişimi

[A3-INTAKE](maintenance/2026-09-29-research-installation-separation/A3-INTAKE.md), ilk kaynak erişiminin ve kimlik denetiminin tarihli kaydıdır. İlk yayın `323e38d288b6760ab70e15744c86678fcbc9d125` yalnız Academy gövdesini ve yan kayıtları getirdi. `0548bd4a55ef3b87fbb3674cf075c2f6d8e639ec` aktarım engelini ve tek ZIP yükleme yolunu kaydetti. **Bu iki kayıttaki yayın bekleme durumu, aşağıdaki doğrulanmış yüklemeyle aşılmıştır.**

Batu'nun `93216f73ea565ed3ba22e4ba0e18e2144e1368c4` commit'i [A3_Dogrulanmis_Tarihsel_Kaynaklar_2026-09-30.zip](archives/devos-pre-claude-2026-09-29/A3_Dogrulanmis_Tarihsel_Kaynaklar_2026-09-30.zip) dosyasını özel arşive ekledi. Uzak yol, **20.275.988 byte** boyut ve **`547522120893c25d5c709deb5c0e18f57ebe7806`** Git blob kimliği, yerelde gerçek byte'ları açılan özgün ZIP ile eşleşti. Yerel SHA-256 **`8b06cb2b3dca5875cab0ad72595701e3e0d4d756d0c80fa2f49041df48aa9b17`**. 19 özgün dosyanın her birinin boyut/SHA-256/Git blob kimliği yeniden doğrulandı; toplam 21 üye benzersiz ve güvenli, CRC geçerli.

| Kaynak | Statü | Gerçek erişim / kalan iş |
|---|---|---|
| P4 v3 | Tarihsel; uygulama kaynağı değil | Dört özgün dosya repository ZIP'inde doğrulandı; bağımsız repository dosyaları oluşturulmadı |
| P4 v4 | Tarihsel; mimari kaynak; Codex ortam kararı geçersiz | Dört özgün dosya repository ZIP'inde doğrulandı; bağımsız repository dosyaları oluşturulmadı |
| P5 K00–K15 | Tarihsel; rol/veri modeli aktarımının kaynağı | Beş özgün dosya repository ZIP'inde doğrulandı; S ailesinin yerine geçmez |
| P5 S00–S12 | Tarihsel; senaryolar gelecekte sınav fikri olabilir | Eski teslimin beklenen kimlikleri kayıtlı; özgün gövdeler hâlâ bulunamadı. Yüklenen ZIP bu paketi içermez |
| P5 v2 Codex arayüzü | Tarihsel; veri modeli aktarımının kaynağı | Beş özgün dosya repository ZIP'inde doğrulandı; bağımsız repository dosyaları oluşturulmadı |
| SOUL ve DevOS | Tarihsel kaynak; SOUL tanımı yeni planda güncellendi | İstenen tam rapor hâlâ doğru kimliğiyle bulunamadı; yüklenen ZIP'te yok; başka metinle ikame edilmez |
| SOUL Academy | Keşif notu; karar veya doğrudan iş açma yetkisi değil | Özgün gövde hem repository ZIP'inde hem bağımsız Markdown dosyasında; iki kopya aynı kimlikte |

[Arşiv README](archives/devos-pre-claude-2026-09-29/README.md) yükleme kanıtını ve erişim biçimini; [SOURCE-IDENTITIES](archives/devos-pre-claude-2026-09-29/SOURCE-IDENTITIES.json) sürüm 2 ise bütün dosyaların özgün kimliklerini ve kesin ZIP üye yollarının kuralını taşır. Üye yolu `archive_container.member_prefix + artifact.path`'tir; 19 eşleşme gerçek ZIP'te denetlendi. Bağımsız repository yolu yalnız gerçekten oluşturulduğu yerde ayrıca belirtilir. ZIP içindeki eski kimlik listesi güncel envanterin üstüne yazılmaz.

**Doğrulama sınırı:** Uzak ikili dosya bu tur yeniden indirilmedi; uzak Git nesne kimliği ve boyut, yerelde açılan özgün byte'larla eşleştirildi. Önceki A3-INTAKE'in 14 teslim girdisi ve 349 iç manifest girdisi denetimleri kendi tarihli sonuçlarıdır; bu tur yeni hedef testi gibi sayılmaz. Tarihsel kod/testler çalıştırılmadı; PDF görünümü, kaynak iddiaları, tam aktarım sadakati veya Claude'un hedefte içe alma davranışı doğrulanmış değildir.

**Yükleme engeli kapalı; A3 bütünü açık.** Beş geri kazanılmış aile için yeniden yükleme veya ayrı dosya üretimi beklenmez. Tek sonraki alt iş, S00–S12 ve SOUL ve DevOS erişim açıklarını yeni somut referans veya kapsam kazandıran aramayla sonuçlandırmaktır; sonuçsuz sorgular yinelenmez. Bulunamazsa arama kapsamı ve erişim engeli açıkça korunur, bu iki kaynak için tamamlanma iddiası kurulmaz. Sonrasında A3 kapanış/engel değerlendirmesi yapılır; A4/A5 bu tur yapılmadı.

Aktarım sadakatinin tamamının doğrulandığı iddia edilmez. Dış değerlendirme yalnız [devos/plan/Inceleme_Degerlendirmesi_ChatGPT.md](https://github.com/batuhanozgun/devos/blob/main/plan/Inceleme_Degerlendirmesi_ChatGPT.md) üzerinden bulunur; burada kopyalanmaz ve yeni karara bağlanmaz. Tamamlanmış A2 dosyaları yeniden düzenlenmez; A3, A4 ve A5 sırası korunur.

## 6. Denetim ve son teslim yükü

Başlangıç: **`8cd01e4afdcd0d37960b05930c91e1244678be6e`**. [BASELINE.json](maintenance/2026-09-29-research-installation-separation/BASELINE.json) başlangıç tree/blob ve istek hash'ini taşır. A1 kök README'nin eski gövdesini aynı blob ile denetim kopyasında korudu. A2 dosya taşımadı veya silmedi.

Her tur ve yayın öncesi main ilerlediyse delta/yazarlar incelenir; başka çalışmanın değişikliği geri alınmaz. Yayın force push olmadan yapılır. Çakışan güncelleme sessizce ezilmez. Makine hesabı commit'i görülürse kullanıcıya bildirimden önce düzeltme yapılmaz. Bu turun başlangıcı `93216f73ea565ed3ba22e4ba0e18e2144e1368c4`; önceki `0548bd4` üzerine yalnız ZIP ekleyen bir commit vardır. Bu yeni commit'in yazarı `batuhanozgun`, committer'ı GitHub'dır; bu kapsamda makine hesabı yazımı görülmedi. Bütün dal/kimliklerde yokluk iddiası değildir.

A4 taraması en az `Codex`, `güncel`, `current`, `sıradaki`, `next`, `DEVOS-001`, `DEVOS-002`, P4/P5 ve eski hedef repo adlarını kapsar. Sonuçlar tam izlenen yol envanteriyle karşılaştırılır. Eşleşme hata veya aramada bulunmama yokluk kanıtı değildir: tarihsel alıntılar, gerçek eski kanıt ve aktif araştırmanın kendi sonraki işi gerekçeyle korunabilir. Pasif arşiv içeriği talimat diye uygulanmaz.

A5: sıfır silinen dosya; değişmeyen kontrol blob/tree kimlikleri; araştırma gövdelerinin korunması; yalnız gerekçeli statü/yön farkları; varsa taşımada eski/yeni byte eşliği ve link düzeltmesi; gerçek kaynak erişimi; tam değişiklik/ekleme/taşıma listesi; görev §3 dışında yapılanların gerekçesi; commit bağlantıları; kalan ifadelerin nedeni ve erişim açıkları.

Tam tarama ve arşiv erişimi yapılmadığı için **“eski yönü güncel gösteren hiçbir kayıt kalmadı” henüz söylenemez**. Erişilemeyen arşiv ilgili paketi açık bırakır; bağımsız yönlendirme düzeltmesini engellemez. Yeni teknik/ürün kararı üretmek, eski planı kurmak veya paket uydurmak çözüm değildir.

## 7. Devralma

**Tek sonraki iş: A3 §5 — S00–S12 ve SOUL ve DevOS erişim açıklarının sonuçlandırılması.** Önce güncel main delta/yazar kontrolü; sonra bu plan ve arşiv README/kimlik kaydı okunur. Beş geri kazanılmış aile için repository yüklemesi tamamdır: uzak ZIP nesnesi ve kesin üye yolları doğrulanmıştır. Eski A3-INTAKE veya önceki arşiv README'sindeki bekleme durumunu devralıp Batu'dan aynı dosyayı tekrar isteme; P4 v3 veya diğer üç aile için yeniden yayın turu açma.

İki eksik kaynak için yalnız yeni somut referans veya arama kapsamı kazandıran inceleme yapılır. İlk alımda genel Library/konuşma metadata listelerinin tamamı tüketilmemişti; gerekirse bu kalan kapsam veya kaynak raporu gerçekten işaret eden yeni bir referans kullanılır. Bulunamayan kaynak yeniden yazılmaz, başka başlıklı belgeyle ikame edilmez. Arama sınırı ve erişim engeli kaydedilip A3 kapanış/engel değerlendirmesine dönülür; A3'ün eksiksiz tamamlandığı veya A4/A5'in yapıldığı söylenmez.

A2'nin tamamlanmış doğrudan girişleri yeni maddi bulgu olmadan yeniden açılmaz. Yeni oturum eski COORD/G0/G1 brief'inden, EXP-006 S00'ından, DEVOS-001/002 görevinden veya dış DevOS kurulumundan başlamaz. Bu bakımın tek güncel devam kaydı bu dosyadır; önceki tarihli denetimlerdeki “sonraki” ifadeleri onların kendi turuna aittir.