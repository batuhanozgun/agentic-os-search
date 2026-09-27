# E3 — Batu'nun ilkeleri ve ortamda uygulanabilirlik: METHOD v1 taslağının eleştirisi

> **Tür:** eleştiri (P0.5, E3); alt ajan çıktısı, model üretimi · 27 Eylül 2026 · **İncelenen:** `phases/P0-calisma-duzeni/METHOD-v1-TASLAK.md` (dal `claude/hopeful-pascal-7bekcd`). **Sınır:** Taslağı yazan modelle aynı modelden geliyorum. Bu inceleme bağımsız doğrulama değil, taze gözle karşı-okumadır.

## Genel hüküm

1. Düzen, Batu'nun düşünme biçiminin çoğunu kural düzeyinde taşıyor: görev tanımında rota, hedef ve ölçüt; "repo bellektir"; söz ile yorumun ayrılması; "doğrulandı"nın sınırı; keşfin sistemin işi olması. En güçlü parçalar MB-04 ile CLAUDE.md taslağındaki soğuk başlangıç yolu.
2. Bu kuralların ilk uygulaması olan taslak onları kendisi çiğniyor. Batu'ya "yeter" denen §0 kapsamı çekincesiz anlatıyor; bu, U004'teki "anlatılan geniş, yapılan dar" kalıbıdır. Karar okuma yolu 4.616 kelime ve sahte seçenekler içeriyor. ZARF-v1 modelin yorumunu "Batu'nun içeriği" sayıyor.
3. Taslağın güvenlik dayanağı "aynı modelden olmayan tek denetçi Batu'dur" cümlesi. Bu işlev ilan edilmiş ama tasarlanmamış. Kalan risk Batu'ya sorulmadan kabul edilmiş.
4. AGENT.md ile öncelik tanımsız. A-01 varsayımında AGENT.md, CLAUDE.md'yi ve METHOD'u davranış kaynağı saymaz. Taslağın önerdiği uyarlama AGENT.md'nin değiştirilmesini gerektiriyor; taslak ise AGENT.md'yi hem kapsam dışı hem salt okunur ilan ediyor.
5. Listelenen dokuz ortam gerçeğinden hiçbiriyle doğrudan çelişki yok. Boşluklar: kurulum oturumunda hook'ların hemen devreye girmesi, Auto kipinin sınıflandırıcı sayacı, P1'deki `add_repo` ve koordinatörün bağlam × adım maliyeti.
6. Maliyet: Taslak yalnız P0'ın kalanını tahmin ediyor. Kendi sayılarıyla bir aşama ≈ 135–500 M işlenen token ve 11–20 alt ajan koşusu; P1–P6 ≈ 1,2–2,3 milyar. Brief'teki "6,5 M" tabanı geçersiz: bu oturum 11:53 UTC'de 461,7 M işlemişti.
7. Hüküm: Üç kritik bulgu (E3-01…E3-03) P0.6'da kapanmadan Batu'nun kabulü bilgili bir kabul olmaz. Önemli bulguların çoğu metin ya da sıra değişikliğiyle kapanır.

**Bulgu sayıları:** kritik 3 · önemli 9 · küçük 4 (toplam 16).

## Soru, kaynaklar, okuma kapsamı

- **Soru (E3):** Bu düzen Batu'nun düşünme biçimini gerçekten taşıyor mu? Bu ortamda (Claude Code cloud) gerçekten işler mi?
- **Tam okunan:**
  - `briefs/`: ORTAK, ORTAK-SENTEZ, E-ORTAK, E3.
  - `METHOD-v1-TASLAK.md` (1.514 satır).
  - R03.
  - `sources/conversation/`: U001–U006, A002, INDEX.
  - DECISIONS, STATE, EXP-007 README, AGENT.md.
  - `origin/main` üzerindeki P1-01 (`git show`).
- **Kısmi (hedefli) okunan:**
  - Ek T4: S1-M2, S1-M5, S2-M2, S2-M5 (kartların tamamı).
  - Ek T5: S20.6 (kartın tamamı); grep'le satır 39, 62, 741–742, 1779.
  - Ek T2: `omitClaudeMd`, `SubagentHandback` ve sınıflandırıcı satırları (grep).
  - R01: başlık listesi; C4, C5, C8, C12, C13, C14, C15; satır 6 ve 1014–1066.
  - R07: başlık listesi; §7 tablosu; satır 439 ve 719.
  - R11: E08, satır 206 ve 891 (grep).
  - `agent/protocols/`: yalnız boyut ve grep.
  - `tools/token-kullanimi.py`.
- **Okunmadı:**
  - T1 ve T3 kartları.
  - R02, R04–R06, R08–R10.
  - A001; A003'ten yalnız kelime sayısı alındı.
  - Hook betiklerinin gövdeleri.
  - code.claude.com sayfaları. Yeniden okunmadı; ortam iddiaları R01, R07 ve P1-01'deki aktarımlara dayanır.
- **Erişilemedi:** yok.
- **Bu oturumda yaptığım gözlem ve ölçümler (27.09.2026):**
  - kendi araç listem;
  - `git diff --stat HEAD origin/main -- AGENT.md agent/` ve `git log origin/main -- AGENT.md agent/`;
  - `wc -w` ve `wc -c` sayımları;
  - §5.1 zorlama sütununun `awk` ile sayımı;
  - `tools/token-kullanimi.py` koşusu (11:53 UTC).
  
  Okunan toplam metin ≈ 410 KB.
- **Kanıt dili:**
  - Etiketler: kaynak diyor / gözledim / çıkarım / varsayım / bilinmiyor.
  - Claude Code iddialarında taslağın bulut etiketleri kullanılır:
    - C+ bulut için belgeli;
    - C~ genel belge;
    - C! bulutta farklı;
    - C? belirsiz;
    - Cg bu oturumda gözlendi.
  - Kanıt gücü ayrıca yazılır: tedarikçi belgesi (çoğu alt ajan aktarımıyla), taslağın kendi metni, gözlem.

## 1. Batu'nun ilkelerine karşı

Kaynak kodları R03'teki gibidir: A4, A5 makaleler; P7† yazı; E6U2-A ve E5U Batu'nun konuşmaları; CH‡ bir asistan özeti.

| İlke (kaynak) | Taslak nerede karşılıyor | Nerede ihlal ediyor ya da zayıf | Hüküm |
|---|---|---|---|
| LLM düşünmez; yanlış cevaba kolayca ulaşılamayan bir düzen kurulmalı (A5) | İlke 10 (mekanik kapı > prosedür > öğüt); rol araç listeleri (M16.1); 9 hook; zorunlu şablon alanları (MB-04, MB-05, MB-12); "doğrulandı"nın sınırı | 157 kartın 113'ü yalnız tavsiye ya da yapısal. 29 kartın zorlaması yalnız tek repolu oturumdaki, hiç çalıştırılmamış hook'lara bağlı (E3-07). P0.7 pilotları rol ve araç sınırı olmadan koşuyor (E3-11). | kısmen |
| Rota, hedef ve ölçüt verilmezse ajan emir erine döner (A4) | MB-04: amaç zinciri, beslediği karar, işten önce bitti tanımı, kapsam, "bilerek verilmeyenler"; "beslediği karar yazılamıyorsa brief gönderilmez"; rol dosyasında "başarı ölçütü" (D1) | Ciddi ihlal bulamadım. Risk: 13 alanlı başlık ve 17 alanlı zarf, formu amacın önüne geçirebilir. Taslak bunu bozulma işareti olarak yazmış. | karşılanıyor |
| Yapan ile kontrol eden ayrılır (A4) | `e7-elestirmen` (B2), `e7-dogrulayici` (B3), gerekçesi görülmeden yapılan eleştiri, B0–B5 ölçeği | Kalem sınıflaması, kendiliğinden geçişte kapı hükmü ve soğuk başlangıç puanı ana oturumda. O-7 ile denetçinin ayarı denetlenen tarafta. L-001'i yazar kendisi "doğrulandı" saymış (E3-06). | kısmen |
| Sahte seçenek sunulmaz (A4; A2†) | MB-11 kural 4; CLAUDE.md §4; ortak sözleşme §7 madde 7 | §12'de elenmiş seçenekler ve üç seçenekli satırlar var (E3-04). | kural var; ilk uygulamada ihlal |
| Kısa iletişim (E6U2-A) | S2-M1: mesaj ≤200 kelime; KN özeti ≤250, aşama raporu özeti ≤400; dört bitiş satırı; S2-M5 dikkat bütçesi | Karar okuma yolu 4.616 kelime (E3-03). §12 kimliklerle dolu (E3-08). A-01 kararına kadar Batu'ya giden her mesaj ~10 satırlık routing bloğuyla başlar (E3-01). | kural var; ilk uygulamada ihlal |
| Kayma her kelimeden doğabilir (A4) | M10.1–M10.6; K-009'da söz ile yorum ayrıldı; D1 "başarı yönü" yerine "başarı ölçütü" | ZARF-v1'deki yorum "Batu'nun içeriği" sayılıyor (E3-05). Kimlikler çakışıyor (E3-08). "Göz takibi" eşlemesi benzetmeyi tersine çeviriyor (E3-14). Sözün birebir kaydı mekanik değil (E3-15). | kısmen |
| Bilgi, yazıldığı yerle sürer (P7†) | İlke 1–4; STATE devir bloğu (MB-08); GUNLUK; dosya görevleri tablosu | Yöntem metninin yetkili yeri METHOD ile dondurulmuş taslaklar arasında bölünmüş. Taslakların klasörü "türetilmiş görünüm" olarak tanımlı (E3-07). | durum bilgisi için güçlü, yöntem metni için zayıf |
| Önce bütün harita (E6U2-A) | §2'deki P0–P6 haritası: ana soru, teslimat, çıkış ölçütü, Batu'nun rolü, geçiş türü; V-H varsayımları | Haritanın maliyet boyutu yok. Bu yüzden V-H-5 sınanamıyor (E3-12). | karşılanıyor; maliyet eksik |
| Keşif AI'ın işidir; Batu gizli eksik bulucu değildir (E5U-02) | MK-4.1, MK-4.5, `e7-eksik-arayici`, "sistem yakalayabilir miydi" sorusu, HATIRLATMA kaydı | Yedek yollarda Batu tek dedektör (R-1, W9). P0 sonunda altı eylem onun. Güvenlik işlevindeki rolü tanımsız (E3-02). | kısmen |
| Batu'nun onayı teknik doğrulama değildir (CH‡) | B5; §3'teki S2 satırı: "teknik onayı Batu'ya götürmek" gereksiz | MB-14 hook, settings ve araç izni değişikliklerini Batu'ya bağlıyor. Commit kapısı "Onay: K-xxx" dizgesine bakıyor (E3-04). | kural var; tasarım çelişiyor |

## 2. Batu'nun yükü

| An | Okuması gereken | Karar | Eylem |
|---|---|---|---|
| Şimdi, P0.6'ya kadar | Taslağın kendi karar yolu: §0, §2, §12, §13, §14. Toplam 4.616 kelime (§0 530, §2 607, §12 2.153, §13 665, §14 661). | §0'da 7 karar; bunlar §12'de 12 maddeye bağlı, K-3'ün altı alt sorusu dahil. P0.6'da 6 madde daha gelir (O-7, K-5, K-7…K-10). | Altı eylem: ortam penceresinde ayar (O-8); `/goal` (CD-05); iki `/usage` okuması (CD-15); kontrollü `/compact`; deneme oturumlarını kapatmak; gerekirse oturumu dalda açmak |
| P0.7–P0.8 | Pilot notları ve kurulum sonucu (uzunluğu tanımsız) | Kurulum onayı (K-0xx) | PS-2'ye göre oturumu dalda açmak |
| Her aşama (P1–P6) | Zorunlu: aşama raporu ve durakta kabul paketi, toplam ≤~1.500 kelime; çerçeve soruları; kırmızı alarm | Çerçeve soruları hemen. Tercih soruları KN başına ≤3. MB-14'ün Batu satırları aşama sonunda toplu. Dikkat bütçesi iki aşamada bir gözden geçirilir. | Kırmızı alarma 24 saat içinde cevap; cevap yoksa geçişler durur |
| Her 5 kalem ya da 24 saat | KN özeti ≤250 kelime; okuması zorunlu değil | ≤3 tercih sorusu | — |
| Duraklar: P0, P4, P5, P6 | SHA'ya bağlı kabul paketi | kabul | — |
| PS-1 ya da PS-2 düşerse | — | — | oturumu açmak; "günlük bakış" (R-1) |

- **Sıklık (çıkarım):**
  - S2-M2'ye göre kontrol noktası "her 5 kapanan iş kaleminde ya da 24 saatte bir, hangisi önce gelirse" yazılır.
  - §7'deki tipik günde öğlene kadar üç kalem kapanıyor.
  - Etkin çalışmada Batu'ya en az günde bir KN gider. Bir haftalık aşamada bu 5–7 KN ve en çok 15–21 tercih sorusu eder.
- **Yeterli mi, yorucu mu?** Toplam yük "kısa" isteğine göre makul ve K-7 değerleri Batu'ya ayarlatıyor. Sorun miktarda değil, yükün nereye konduğunda:
  - P0 sonunda yük en yüksek ve çoğu teknik: hook, ortam değişkeni, CD listesi, bütçe birimi. Bu maddelerde Batu'nun aynı modelden bağımsız bir bilgi katması beklenmez (U003: "bu başka teknik bilgim var anlamına gelmesin").
  - P1–P6'da güvenlik işlevinin taşınacağı yerde zorunlu okuma, ≤1.500 kelimelik ve modelin yazdığı bir özettir; bakılacak iki bağlantıyı da model seçer.
  - Bu turun en büyük düzeltmesi (K-007) Batu'nun 2.765 kelimelik A003'ü özgün haliyle okumasından çıktı. Taslağın bütçesi bu okumanın ancak yaklaşık yarısını, o da özet üzerinden karşılar.
  - R11 aynı gerilimi adlandırıyor: "Ama "kısa" ile "görünmez" aynı şey değildir."
- **Hüküm:** Yük yorucu değil, ama güvenlik işlevini taşımıyor. İçeriğin yeniden seçilmesi gerekiyor (E3-02, E3-03, E3-04).

## 3. Okunabilirlik: soğuk başlangıç

**Adım adım yürüyüş.**

- **(a) Bugün, kurulumdan önce, dalda açılan oturum:**
  - CLAUDE.md yok. Oturum README'yi okur, ardından STATE'teki "Yeni oturum ne yapar" adımlarını izler.
  - Taslak bu dönemi değiştirmiyor (W1 kırılma 2). Oturum doğru başlar; kurallar tavsiye düzeyindedir.
  - Gözledim: repo kökünde ve EXP-007 içinde `CLAUDE.md`, `.claude/`, `AGENTS.md` ya da `SKILL.md` yok.
- **(b) Kurulumdan sonra, dalda açılan oturum:**
  - CLAUDE.md taslağı 66 satır, kısa ve sıralı. Sıra şöyle:
    1. kanarya;
    2. `oturum-acilis`;
    3. dal doğrulaması;
    4. devir bloğunun `git log` ile karşılaştırılması;
    5. ≤50 KB okuma;
    6. yarım iş;
    7. alarm;
    8. yetkili iş.
  - Bu, taslağın en okunur parçası.
  - Kırılma: §2 madde 5 bu yola AGENT.md'yi ve LOAD edilen protokolleri ekliyor. Açılış seti ~50 KB'tan ~148 KB'a çıkıyor ve iki otorite çatışıyor (E3-01).
- **(c) main'den açılan oturum:**
  - EXP-007 ve CLAUDE.md yok. Kök README ve AGENT.md oturumu EXP-006'ya ve DEVOS-002'ye yöneltir (A-05).
  - Doğru başlangıç, Batu'nun dal adını vermesine bağlı (STATE adım 0; PS-2). Taslak bunu biliyor; yedeği Batu.
- **(d) Bir kartı uygulamak isteyen oturum:**
  - CLAUDE.md METHOD'u "dizin" olarak gösteriyor.
  - Değişmeyen kartların metni T1–T5 taslaklarında. Çelişkide METHOD geçerli, yani iki dosyanın uzlaştırılması gerekiyor (E3-07).

**Taslağın kendi içindeki çelişkiler (11):**

1. §0 "her kartın şablonu ve kabul testi var" diyor; R-6 ve §14.4 bunun doğrulanmadığını söylüyor (E3-03).
2. §0 "okuman gereken ≤~1.500 kelime" diyor; satır 5'teki karar yolu 4.616 kelime (E3-03).
3. §0 "dokuz hook yalnız gözlenmiş kayma noktalarında" diyor; T5'in hook tablosunda bazı hook'ların dayanağı risk (E3-03, E3-15).
4. MB-11 en çok 2 seçenek diyor; §12'de beş satır üç seçenekli (E3-04).
5. B5 Batu'yu "teknik doğrulayıcı değil" sayıyor; MB-14'ün yapılandırma satırları teknik değişiklikleri ona bağlıyor (E3-04).
6. §4.1 "doğrulandı"yı B3 ve üstüne ayırıyor; L-001 bu koşulu karşılamıyor (E3-06).
7. §1 ve CLAUDE.md §3 AGENT.md'yi dokunulmaz sayıyor; O-5 AGENT.md'yi değiştiren uyarlamayı öneriyor (E3-01).
8. MB-14 yürürlüğü "sonraki oturum" diye yazıyor; CLAUDE.md aynı oturumun ilk sıkıştırmasında yüklenir (E3-09).
9. CLAUDE.md §5 GUNLUK'a `IHLAL` yazdırıyor; bu ad MB-02'nin olay sözlüğünde yok (E3-08).
10. MB-15 "alt ajanlarda bu araçlar yoktur" diyor; pilot dönemindeki `general-purpose` alt ajanlarda var (E3-11).
11. W1 açılış seti için ≤50 KB diyor; AGENT.md ve LOAD edilen protokollerle ≈ 98 KB ekleniyor (E3-01).

**Boyut:**

- Taslak 31.421 kelime ve 157 kart içeriyor.
- GUNLUK'ta 36 olay türü var.
- §6.3'te 27 kimlik öneki tanımlı; kart ve kanıt kodlarıyla birlikte 30'u aşıyor.
- Çalışma anında yüklenen metin küçük:
  - CLAUDE.md 66 satır;
  - ortak sözleşme ≤120 satır;
  - her biri ≤120 satırlık en çok 10 skill;
  - rol açıklamaları toplamı ≤3.000 token.

**Hüküm:** Soğuk başlangıç yolu kısa ve doğru sıralı. Ama düzenin geri kalanı çalışma anında okunacak biçimde değil: yetkili metin dağınık, kimlikler çakışıyor ve taslak kendi kurallarıyla on bir yerde çelişiyor.

## 4. Ortamın gerçeğine karşı

| Gerçek | Kanıt | Taslakta karşılığı | Çelişki ya da açık | Sınıf |
|---|---|---|---|---|
| Alt ajan derinliği 1 | R01 satır 6: `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`. Bu alt ajanın araç listesinde Agent aracı yok (gözledim, Cg). Belgedeki varsayılan 3 (R01 C4; P1-01 E02). | §14.3 varsayımı; roller arası istek koordinatör üzerinden (M13.4) | Çelişki yok. Değer bir ortam ayarı, platform sınırı değil; kanaryaya eklenebilir. | bu kapta gözlendi |
| Hook'lar yalnız tek repolu oturumda | R01 cloud C8 (düzeltilmiş iddia): repo settings'teki hook ve izin kuralları "apply only in a session with one repository" (C!, tedarikçi belgesi) | zr¹ etiketi; kanarya; CLAUDE.md §5'teki elle kontroller | P1'deki `add_repo` oturumu çok repolu yapıyor mu? (E3-16) | belgeli; `add_repo` etkisi pilotta sınanmalı |
| Auto kipinde rolün izin kipi yok sayılır; kısıt araç listesiyle konur | R07 §7: "Rolün izin kipini yok sayar (SA)" (C+) | Rollerde `permissionMode` yok; `tools` ve `disallowedTools` var | Listede olmadan verilen araçlar: `SubagentHandback` (Ek T2 satır 265) ve ToolSearch ile yüklenen ertelenmiş araç (CD-20). Sınıflandırıcı sayacı (E3-10). | belgeli; delikler pilotta sınanmalı |
| `memory: project` alanının cloud'daki davranışı bilinmiyor | R07 §7: C~, "Denenmedi" | Kullanılmıyor (MB-03); CD-14 isteğe bağlı | Çelişki yok; tasarım buna dayanmıyor | belirsiz; yük taşımıyor |
| Bağlam %80'de sıkıştırılır | R01 satır 6: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80`. STATE: ana oturum 792 K'da sıkıştırıldı. | W4; Compact Instructions; SessionStart (compact) enjeksiyonu; ikinci sıkıştırmada taze oturum | Koordinatör kendi doluluğunu göremiyor (CD-10). Taze oturum CD-04'e bağlı. Koordinatörün bağlam bütçesi yok (E3-12). | gözlendi; sonrası pilotta (CD-12) |
| Oturum boşta kalınca makine geri alınır | R01 C5: "Background work that was still running when the VM was reclaimed, such as subagents and shell commands, isn't restored." (C+) | W5; KAYIP kaydı ve aynı brief'le yeniden dağıtım; nabız (PS-1) | Dalga kaybı ~150 M ile fiyatlanmadı. Workflow sonuçlarının geri almadan sağ çıktığı belgeli (R01 C12), taslakta "bilinmiyor". Scratchpad taslakları da kaybolur (MB-01). | belgeli; kurtarma pilotta (CD-03) |
| `/clear` cloud'da yok | R01 satır 374: cloud'da `/clear` yok, "Start a new session from the sidebar instead" (C!) | Taslak `/clear`'a dayanmıyor; temiz başlangıç `create_session` ile (CD-04) | Çelişki yok | belgeli |
| Oturum ortasında değişen CLAUDE.md o oturumda uygulanmaz | R07 satır 439: "The new content loads on the next `/clear`, `/compact`, or restart." (C~) | MB-06 ve MB-14: "sonraki oturum" | CLAUDE.md aynı oturumun ilk sıkıştırmasında yüklenir. Settings oturum içinde yeniden yüklenebilir (C~, denenmedi); bu kurulum oturumunu etkiler (E3-09). | CLAUDE.md belgeli; settings pilotta sınanmalı |
| Kullanım limitleri | R01 C14 ve C15: limitler hesapla paylaşılır, paralel iş onları orantılı tüketir; "a large workflow fanout, can exhaust the weekly allowance" (C+) | MB-10, S20.6, PS-3 (CD-15) | Haftalık limitin değeri ve işlenen token'la ilişkisi bilinmiyor. Bütün harita için tahmin yok (E3-12). | belirsiz; pilotta sınanmalı |

**ChatGPT hattının P1-01 dosyasıyla karşılaştırma.** Doğrudan çelişki bulmadım. P1-01 birkaç noktada daha temkinli ve taslakla uyumlu:

- İç içe alt ajanın belgede var olduğunu söylüyor: "eski 'alt ajan hiçbir alt ajan açamaz' genellemesi kullanılmaz". Bu kapta derinliğin 1 olması bununla çelişmez; taslağın varsayımı yalnız bu ortam içindir.
- "`CLAUDE.md` davranış girdisidir, teknik izin duvarı değildir." Taslak da CLAUDE.md'yi tavsiye düzeyinde sayıyor.
- `/goal` değerlendiricisi "Bağımsız ürün doğrulaması değildir." Taslak `/goal`'ü yalnız yedek olarak kullanıyor.
- VM'nin yeniden açılması "bütün dosyaların, süreçlerin ve alt aktörlerin aynen döneceğinin garantisi değildir." Bu, W5 ile uyumlu.
- P1-01'deki plugin çelişkisi (Q03) taslağı etkilemiyor; taslak plugin kullanmıyor.
- P1-01'in `SendMessage` notu CD-19'un denenebilir olduğunu destekliyor.

## 5. Maliyet

**Taban.** Brief'teki "P0.3'e kadar yaklaşık 6,5 milyon token" sayısı geçersiz:

- STATE bu sayının eksik sayan bildirim sayacından geldiğini yazıyor: "T4 için bildirim 77,9 K diyor; transcript'e göre T4 20,8 M token işledi."
- Ölçtüğüm değer (27.09 11:53 UTC, `tools/token-kullanimi.py`): 1.625 çağrı, 461,7 M işlenen token, girdi eşdeğeri 79–97 M.
- Bu, brief'teki sayının yaklaşık 70 katı.
- P0'da bugüne kadar yaklaşık 45 alt ajan koşusu yapıldı: R01 iş akışı 26–27, R02–R06 5, R07–R11 5, T1–T5 5, birleştirme 1, E1–E3 3.

**Bir aşama ne tutar (çıkarım; tür bütçeleri MB-10'dan, koşu sayıları benim varsayımım):**

| Kalem (tür bütçesi) | Hafif aşama (ör. P1) | Ağır aşama (ör. P2↔P3, P4) |
|---|---|---|
| Aşama başı keşif (~6 M) | 1 → 6 M | 1 → 6 M |
| Kaynak okuma (~6 M) | 4 → 24 M | 4 → 24 M |
| Derin not ya da tasarım (20–35 M) | 1 → 20–35 M | 5 (bir dalga) → 100–150 M |
| Birleştirme (20–35 M) | — | 1 → 20–35 M |
| R2/R3 eleştirisi (~15 M) | 2 → 30 M | 3 → 45 M |
| Doğrulama (~6 M; varsayım) | — | 2 → 12 M |
| Aşama kapısı (3–5 koşu, 25–45 M; §11.2) | 4 → 25–45 M | 4 → 25–45 M |
| **Alt ajan toplamı** | **12 koşu · 105–140 M** | **20 koşu · 232–317 M** |
| Koordinatör (kalem × 20–30 çağrı × 0,15–0,4 M bağlam) | 10 kalem → 30–120 M | 15 kalem → 45–180 M |
| **Toplam** | **135–260 M** | **277–497 M** |

**Bütün harita:**

- P1–P6'yı üç hafif, üç ağır aşama sayarsam: ≈ 1,2–2,3 milyar işlenen token, ≈ 96 alt ajan koşusu.
- P0'daki orana (%17–21) göre girdi eşdeğeri ≈ 0,21–0,48 milyar.
- Karşılaştırma: taslağa göre P0'ın kalanı 135–220 M, yani P0'ın toplamı ≈ 0,6–0,7 milyar.
- Haritanın geri kalanı P0'ın yaklaşık 2–3,5 katı.

**Gerçekçi mi?**

- Tür başına sayılar gerçekçi, çünkü ölçülmüş koşulardan geliyor.
- Gerçekçi olmayan iki şey var:
  - Harita düzeyinde tahmin yok.
  - Koordinatörün maliyeti bütçelenmemiş. Taslağın kendi formülünü ("işlenen ≈ ortalama bağlam × adım") uygularsam koordinatörün payı aşama başına %15 ile %100'ün üstü arasında çıkıyor. ≤%15 hedefi ancak koordinatör bağlamı düşük tutulursa tutar (E3-12).

## 6. Özellikle bakılanlar

- **AGENT.md kontrol katmanı düzenle çakışıyor mu?**
  - Evet. A-01 varsayımında öncelik tanımsız ve taslak kendi içinde çelişiyor.
  - Bugün dal ile main arasında kontrol katmanı aynı (gözledim). Ama ChatGPT hattı kontrol katmanını main'de değiştiriyor; son değişiklik `773cfcd`.
  - Ayrıntı ve öneri: E3-01.
- **Batu "başla" demeden yürürlüğe girecek bir şey var mı?**
  - Nasıl aradım:
    - §13.3'teki yürürlüğe giriş tablosu;
    - §12.3'teki kurulum adımları;
    - §2'deki P0 satırı;
    - MB-14'ün "hemen" satırları;
    - ZARF-v1'in "kendiliğinden" listesi;
    - CLAUDE.md taslağının yeri (yalnız kod bloğunda);
    - K-4 denemeleri;
    - repoda yapılandırma dosyası olup olmadığı (`find`).
  - Sonuç: Batu'nun sözü olmadan yürürlüğe giren bir şey bulmadım.
    - Şimdi (P0.4–P0.6) yalnız K-008 kaydı ve tek seferde yazım sürüyor.
    - P0.7, K-2 ve K-4'e bağlı; P0.8, K-1'e ve O-1…O-8'e bağlı.
    - Sihirli adlı dosya yok.
  - İki ayrıntı küçük bulgu oldu (E3-13): K-1 "başla"yı kurulum ve doğrulamadan önce istiyor; CD-18'in `.claude/` kurulumu A-04 kapsamında tanımlanmamış.

## 7. Bulgular

### E3-01 · kritik · AGENT.md ile düzen arasında öncelik tanımsız; taslak kendi içinde çelişiyor

- **Yer:** §1 Kapsam; §12.1 O-5; §12.4 CLAUDE.md §2 madde 5, §3, §7; W1 adım 3; Ek T4 S1-M5.
- **Sorun:** A-01'in varsayımı "AGENT.md kalır". Bu durumda AGENT.md kendini davranış kurallarının tek kanonik girişi sayar ve `agent/**` dışındaki her yolu proje işi (project-work) katmanına koyar; oradan davranış kuralı çıkarılmasını yasaklar. Bu tanıma göre kök CLAUDE.md, `E7/METHOD.md`, `.claude/agents` ve skill'ler kontrol malzemesi değildir. Taslağın çözümü uyarlama paketi U1–U8'dir; O-5'te önerilen seçenek budur. U7, CLAUDE.md'yi "AGENT.md'ye yönlendiren kayıtlı kontrol malzemesi" yapıyor. AGENT.md'nin Mutation Rule'u ise değişikliğin kanonik AGENT.md'ye yazılmasını, başka yerde ayrı kopya tutulmamasını istiyor. Yani U1–U8 ancak AGENT.md değiştirilerek yürürlüğe girer. Taslak ise aynı anda kontrol katmanını değiştirmeyi kapsam dışı sayıyor (§1). Kurulacak CLAUDE.md AGENT.md'yi "salt okunur" ilan ediyor (§3). Kurulum adımlarında (§12.3) AGENT.md değişikliği yok. Kurulumdan sonra iki sonuçtan biri çıkar. (i) İki davranış kaynağı öncelik kuralı olmadan yan yana durur: CLAUDE.md her oturumda platformca yüklenir; AGENT.md, CLAUDE.md §2 madde 5 gereği her açılışta ve sıkıştırmadan sonra okunur ve kendini tek otorite sayar. (ii) AGENT.md bu dalda değiştirilir ve kontrol katmanı main'deki ChatGPT hattından ayrışır; o hat kontrol katmanını değiştirmeyi sürdürüyor. O-5'teki "Tasarım iki cevaba da dayanıklıdır" iddiası bu önceliği göstermiyor: "harfiyen sürsün" cevabında METHOD, AGENT.md'ye göre davranış kaynağı değildir. Yan etki: W1'deki ≤50 KB açılış bütçesine AGENT.md ve LOAD edilen protokoller eklenir. A002'deki gerçek routing bloğunda sekiz rota LOAD edilmişti; bu, açılışı yaklaşık 148 KB'a, yani bütçenin üç katına çıkarır.
- **Kanıt:**
  - AGENT.md, Purpose: "All other repository paths belong to the project-work layer unless this file explicitly says otherwise."
  - AGENT.md, Separation: "Do not infer new behavioral instructions from project-work files unless `AGENT.md` explicitly routes to them as control material."
  - AGENT.md, Mutation Rule: "update the canonical repository version rather than maintaining divergent copies elsewhere."
  - Etiket: kaynak diyor (kontrol katmanı metni; veri olarak okundu).
  - Ek T4 S1-M5: "Uyarlama paketi onaya kadar yalnız öneri metnidir; AGENT.md'ye yazılmaz." U7: "Kök CLAUDE.md, AGENT.md'ye yönlendiren kayıtlı kontrol malzemesidir" — kaynak diyor.
  - METHOD §1: "Dışında: … kontrol katmanını (AGENT.md, `agent/`) değiştirmek." — kaynak diyor.
  - CLAUDE.md taslağı §3: "`AGENT.md`, `agent/`, EXP-006, `research/`, `concepts/`, `development-os/` salt okunur." §7: "Bu dosya onları içe aktarmaz." — kaynak diyor.
  - O-5 "Onay verilmezse": "Kural harfiyen sürer: her otomatik turda tam gate ve ~10 satırlık blok; bootstrap ChatGPT'ye göre kalır. Tasarım iki cevaba da dayanıklıdır" — kaynak diyor.
  - `git log origin/main -- AGENT.md agent/`: son değişiklik `773cfcd` "EXP-006: persist integrated DevOS master plan and bounded autonomy requirements". `git diff --stat HEAD origin/main -- AGENT.md agent/` boş, yani bugün fark yok. `canonical-work-preflight.md` satır 114 EXP-006'ya özgü: "EXP-006 — kalıcı kısa iletişim sınırı". — gözledim.
  - Boyutlar:
    - AGENT.md 12.369 bayt.
    - A002'nin routing bloğunda LOAD edilen R01–R08 protokolleri 86.095 bayt.
    - Dokuz protokolün toplamı 101.754 bayt.
    - Etiket: gözledim.
  - İki kaynağın çatışacağı ve modelin önceliği kendi yargısıyla çözeceği — çıkarım.
- **Öneri:** O-5'i tek gerçek çatal olarak yeniden yaz ve kurulum paketine bağla. Batu'ya şu sorulsun: "EXP-007 dalında davranışın kontrol kaynağı hangisi?"
  1. **AGENT.md bu dalda değişir.** U1–U8'e ek olarak AGENT.md'ye, CLAUDE.md'yi ve METHOD'u kontrol malzemesi olarak gösteren tek bir yönlendirme satırı eklenir. §1 kapsamı, CLAUDE.md §3'teki "salt okunur" ifadesi ve §12.3'teki kurulum listesi buna göre düzeltilir. Dalın kontrol katmanının main'den ayrışacağı ve birleştirmede (A-07) ne olacağı yazılır.
  2. **A-01'e "hayır" cevabı verilir.** Bu dalda kontrol kaynağı CLAUDE.md ve METHOD olur. AGENT.md'nin kendi kuralı gereği bu da kanonik dosyada bir satırla kaydedilmelidir.

  Her iki yolda da:
  - CLAUDE.md'ye bir öncelik satırı eklenmeli.
  - W1'in açılış bütçesi AGENT.md ve protokoller sayılarak yeniden hesaplanmalı.
  - Root dosya değişikliği A-04 paketine girmeli.

### E3-02 · kritik · Batu'nun "aynı modelden olmayan tek denetçi" işlevi ilan edilmiş ama tasarlanmamış; kalan risk onun adına kabul edilmiş

- **Yer:** §1 ilke 9; §4.1 B5; §14.1 R-4; §7 "tipik gün"; Ek T4 S2-M2 ve S2-M5; W9.
- **Sorun:** Taslak, aynı modelin ortak kör noktalarına karşı güvenliğini Batu'nun dikkatine dayandırıyor (ilke 9, R-4). Ama bu kanalın neyi, hangi kanıtla ve ne sıklıkla denetleyeceğini tanımlamıyor. Batu'nun zorunlu okuması, aşama başına ≤~1.500 kelimelik ve aynı modelin yazdığı özetlerdir. "Nereye bakmalısın" bağlantılarını da aynı model seçiyor. Kontrol noktası raporları için "Batu okumak zorunda değildir" deniyor. Böylece ortak kör noktayı taşıyan model, bağımsız denetçinin neye bakacağını da seçmiş oluyor. Geçmiş kanıt ters yönü gösteriyor. Bu turun en büyük düzeltmesi (K-007, "yapı küçük") Batu'nun A003'ü özgün haliyle okumasından çıktı. R11'e göre beş olayın dördünde hatayı Batu yakaladı. B5 ise Batu'yu "teknik doğrulayıcı değil" sayıyor. Böylece taslak Batu'ya aynı anda hem tek bağımsız denetçi hem de teknik denetçi olmayan kişi rolünü veriyor, ama ikisinin buluştuğu işi tanımlamıyor. Bu iş şudur: sözünün çıktıda nerede ve nasıl karşılandığını birincil metinden görmek. R-4 kalan riski "kabul edilir" diye kapatıyor; oysa risk kabulü Batu'nun yetkisi ve §12'de ona sorulmuyor. PS-1 düşerse Batu "tek dedektör" oluyor; bu, R03'teki "Batu gizli eksik bulucu değildir" ilkesine terstir.
- **Kanıt:**
  - METHOD §1 ilke 9: "Aynı modelden olmayan tek denetçi Batu'nun dikkatidir; onu korumak güvenlik işidir" — kaynak diyor.
  - §14.1 R-4: "tek bağımsız denetçi Batu'nun dikkatidir. Kalan risk kabul edilir" — kaynak diyor.
  - §4.1: "B5 Batu (kabul; teknik doğrulayıcı değil)" — kaynak diyor.
  - Ek T4 S2-M5: "Okuması gerekmeyenler: çalışma günlüğü, alt ajan dönüşleri, araştırma notları, küme taslakları, bulgu kayıtları." — kaynak diyor.
  - Ek T4 S2-M2 şablonu: "## Nereye bakmalısın (en fazla 2 bağlantı)" — kaynak diyor.
  - METHOD §7: "Oturum mesajı olarak gider; Batu okumak zorunda değildir." — kaynak diyor.
  - R11 E08 (satır 635): "Batu'nun dikkati tükenirse çerçeve hatalarını yakalayan tek aynı-model-olmayan kanal kapanır; beş olayın dördünde hatayı Batu yakaladı ya da onarımı o başlattı." — kaynak diyor (alt ajan notu; sayımı kaynağından doğrulamadım).
  - U004, A003'e cevap: "evet çok iyi anlamışsın. ama yapıyı basit tutmuşsun." — kaynak diyor.
  - `wc -w A003.md` = 2.765 — gözledim.
  - R03 §4 madde 8: "He is not an expert, yet he is the only one who accepts the work. … This is unresolved." — kaynak diyor (alt ajan notu).
  - W9 kırılma: "o arada Batu tek dedektördür (§14, R-1)" — kaynak diyor.
  - Model tarafından seçilen işaretçinin ortak kör noktayı yeniden ürettiği — çıkarım.
- **Öneri:** Batu'nun denetim penceresini S2'de ayrı bir kart olarak tasarla. Her aşama raporunda toplam ≤1.500 kelime içinde sabit üç bölüm olsun:
  1. **"Senin sözlerin":** O aşamayı etkileyen Batu sözleri birebir. Her birinin karşısında çıktıdan birebir alıntı durur; iddia değil. "Karşılandı" yazılmaz; hükmü Batu verir.
  2. **"Senin adına verdiklerim":** T katmanı tercihleri ile kabul edilen riskler (R-4 türü) ayrı listelerde; her biri itiraz edilebilir.
  3. **"Rastgele örnek":** Aşamanın çıktılarından ~500 kelimelik birincil metin parçası. Seçimi model yapmaz; mekanik bir kural yapar, örneğin kapanış SHA'sının son onaltılık hanesi.

  R-4'ü §12'ye Batu kararı olarak ekle. Batu'nun bu pencereyi okumadığı aşamalar sayılsın. İki aşama üst üste okunmazsa devir bloğuna "bağımsız kanal kapalı" uyarısı girsin.

### E3-03 · kritik · Batu'ya giden özet ve karar paketi, U004'te adı konan hatayı yineliyor

- **Yer:** §0 (satır 9, 19, 21); satır 5; §10'un başı; §12; dosyanın son satırı.
- **Sorun:** Batu'ya "§0 yeter" deniyor. §0 kapsamı çekincesiz anlatıyor: "157 mekanizma kartıyla kuruldu; her kartın sahibi, tetiği, şablonu ve kabul testi var"; "dokuz hook yalnız gözlenmiş kayma noktalarında". Taslak başka yerlerde bunun tersini söylüyor. Altı skill'in metni yok, birleşik `bash-kapisi.sh` yazılmadı, hook gövdeleri okunmadı ve hiçbiri çalıştırılmadı (R-6). §3 ve §5.1 betikle çıkarılmış kısaltmalardır ve kart gövdeleriyle karşılaştırılmadı (§14.4). En az iki hook'un dayanağı gözlenmiş bir olay değil, risk tahmini. §10, "Karşılanmadı: 0 madde" diyerek kendi kapsamına kendisi not veriyor. Batu'nun karar vereceği §12, sıkıştırma eşiğine yakın ve yeni okuma yapılmadan yazılmış bölümlerde. Taslak bu bölümlerdeki doğrulanamayan her ayrıntının "doğrulanmadı" sayılmasını istiyor, ama bu uyarı §0'da değil, yalnız dosyanın son satırında. §0 ayrıca "Aşama başına okuman gereken metin yaklaşık 1.500 kelimenin altında kalır" diyor; taslağın kendi karar okuma yolu ise 4.616 kelime. Bu, Batu'nun U004'teki eleştirisinin ta kendisi ve kabul kapısını (K-005) çekincesiz bir özete dayandırıyor.
- **Kanıt:**
  - METHOD satır 9: "Eksik olan "nasıl" burada 21 alt sistem ve 157 mekanizma kartıyla kuruldu; her kartın sahibi, tetiği, şablonu ve kabul testi var." — kaynak diyor.
  - Satır 19: "dokuz hook yalnız gözlenmiş kayma noktalarında" — kaynak diyor.
  - Satır 21: "Aşama başına okuman gereken metin yaklaşık 1.500 kelimenin altında kalır." — kaynak diyor.
  - Satır 5: "Batu için §0 yeter. Karar için §0, §2, §12, §13, §14." — kaynak diyor.
  - §14.1 R-6: "altı skill'in tam metni yok; birleşik `bash-kapisi.sh` yazılmadı; hook gövdeleri bu adımda okunmadı ve hiçbiri çalıştırılmadı" — kaynak diyor.
  - §14.4: "§3 ve §5.1 kartların tam gövdesiyle satır satır karşılaştırılmadı." — kaynak diyor.
  - Son satır: "Sıkıştırma eşiğine yakın olunduğu için §11–§14 ve Ek, yeni okuma yapılmadan elde edilmiş bilgiyle yazıldı. Buralardaki doğrulanamayan her ayrıntı "doğrulanmadı" sayılmalıdır." — kaynak diyor.
  - Ek T5 hook tablosu (satır 741–742): StopFailure için "Limit riski [R11 K22]"; ConfigChange için "Ajanın kendi kurallarını yeniden yazması [R11 K112]" — kaynak diyor. Bunların EXP-007'de gözlenmiş bir kayma olmadığı — çıkarım.
  - `wc -w` ile bölüm sayımı: 530 + 607 + 2.153 + 665 + 661 = 4.616 — gözledim.
  - U004: "cevaplarında konuyu iyi anlamış gibi ifade ediyorsun ama iş aksiyona gelince o anlattıklarına göre sonuç çok daha dar kapsamlı oluyor" — kaynak diyor (Batu'nun sözü).
- **Öneri:**
  - §0'ı üç bölüme ayır:
    - **"Var":** yazılmış ve okunmuş şablonlar.
    - **"Yok ya da yazılmadı":** altı skill, `bash-kapisi.sh`, okunmamış hook gövdeleri; §3 ve §5.1'in doğrulanmamış kısaltmalar olduğu.
    - **"Hiç sınanmadı":** her şey.
  - "Dokuz hook yalnız gözlenmiş kayma noktalarında" cümlesinin yerine hook başına dayanak yaz.
  - §10'daki "Karşılanmadı: 0" satırını kaldır ya da "aynı modelin öz-notu" diye etiketle.
  - §12'yi P0.6'da kaynaktan yeniden okuyarak yeniden yaz.
  - Batu'nun karar okuma yolunu ölç ve ≤1.500 kelimeye indir. İndiremiyorsan bu kez aşıldığını ve nedenini §0'da söyle.

### E3-04 · önemli · Karar paketinde sahte seçenekler var ve Batu'nun onayı teknik bir kapıya dönüşüyor

- **Yer:** §12.1 (O-1…O-8); §12.2; MB-14 tablosu; MB-07'de `bash-kapisi.sh`.
- **Sorun:** İki ayrı sorun var.
  1. **Sahte seçenekler.** MB-11 "tek soru, tek öneri; gerçek çatalda en çok 2 seçenek" diyor. §12.1'de ise beş satır (O-1, O-3, O-4, O-5, O-6) üç seçenekli ve bazı seçenekler zaten elenmiş. O-1'in (c) seçeneği "@AGENT.md'yi içe aktaran dosya" §3'te "gereksiz" sayılmış. O-2'nin (b) seçeneği "general-purpose ve rol metni brief'te", K-007'nin reddettiği "her seferinde rol biçmek"in kendisi. Seçilemeyecek seçenekler menüyü dolduruyor; bu, R03'teki sahte seçenek tanımına uyar.
  2. **Teknik onay.** Batu'ya teknik uygulama seçenekleri soruluyor: O-4 (deny kuralları, `env`, `effortLevel`, 9 hook), O-8 (ortam değişkeni ve izin kipi), K-4 (CD listesi). MB-14 hook, settings, araç izni ve CLAUDE.md kural içeriğindeki değişiklikleri Batu'ya bağlıyor. `bash-kapisi.sh` bunu commit mesajındaki "Onay: K-xxx" dizgesiyle denetliyor. Batu teknik doğrulayıcı olmadığını açıkça söyledi ve izinleri toptan vermeye hazır olduğunu yazdı. Bu yapı onun onayını teknik değişikliklerin kapısına çeviriyor. Kapı da onayın içeriğine değil, dizgenin varlığına bakıyor; dizgeyi yazan ise koordinatör. B5 ile çelişki budur.
- **Kanıt:**
  - MB-11: "4) Tek soru, tek öneri; gerçek çatalda en çok 2 seçenek." — kaynak diyor.
  - §12.1 O-1: "a) kur · b) kurma · c) `@AGENT.md`'yi içe aktaran dosya" — kaynak diyor.
  - §3, S7 satırı: "Vektör indeks; AGENT.md'nin K0'a içe aktarılması | gereksiz" — kaynak diyor.
  - O-2: "a) kur · b) `general-purpose` ve rol metni brief'te" — kaynak diyor.
  - U004: "her seferinde yeninden alt ajana rol biçmek doğru değil" — kaynak diyor.
  - U002: "Diğer onay bekleyen konular şu an detay, izinleri veririm sana" — kaynak diyor.
  - U003: "bu başka teknik bilgim var anlamına gelmesin" — kaynak diyor.
  - MB-14: "Araç izni, yetki, yazma yolu; hook; settings; CLAUDE.md'nin kural içeriği; rol açma, kapama, birleştirme | Batu (A-04; Mutation Rule) | `Onay: K-nnn`" — kaynak diyor.
  - MB-07, `bash-kapisi.sh`: "yapılandırmada `Onay: K-xxx`" — kaynak diyor. Dizge kontrolünün içerik kontrolü olmadığı — çıkarım.
  - A4 (R03 ilke 13): "Alternatifleri göstermekten çekinme; fakat belirsizlik anlarında sahte seçenekler üretme." — kaynak diyor.
- **Öneri:**
  - §12'yi Batu'nun yetkisine göre yeniden kur. Teknik paket tek bir yetki sorusu olsun: "Claude şu yolları bu dalda kurabilir; şu sınırlar içinde değiştirebilir; şunları sana sormadan asla yapamaz." Her üç liste açıkça yazılsın.
  - Teknik doğruluğu Batu'nun onayına değil, CD-01'e ve eleştiriye bağla.
  - Elenmiş seçenekleri (O-1 c, O-2 b, O-4 c) menüden çıkar; "Onay verilmezse" sütunu sonucu zaten anlatıyor.
  - Commit kapısı dizgeye değil, onayın kapsamına baksın: K kaydında birebir onaylanan yol listesi durur; commit'teki yollar bu listenin alt kümesi mi, denetlenir.

### E3-05 · önemli · ZARF-v1 "Batu'nun içeriği" sayılıyor, oysa Batu'nun onayladığı metnin genişletilmiş yorumu

- **Yer:** MB-08 (ZARF-v1; "Ne zaman / Kim"); MB-11 kural 2; §0 madde 6; §12.2 K-3.
- **Sorun:** Batu'nun onayladığı sürekli yetki dört cümledir (A002 → U003 madde 1 → K-002). ZARF-v1 bu metni altı madde, 12 yükseltme tetiği, frenler ve bir çözülemezlik kuralıyla genişletiyor ve bir noktada değiştiriyor. Onaylanan metin "Sorular biriksin, iş durmasın" diyor; ZARF-v1'deki YT-6 ve MB-11 ise "çerçeve sorusu biriktirilmez; etkilediği kalemler park" diyor. "M ve T kararları" da kendiliğinden verilecekler listesine eklenmiş. Eklemelerin çoğu makul; örneğin YT-6, R11'in Y11 zayıflığının dengeleyicisi. Ama MB-08 "zarfın içeriği Batu'nun" diyor ve §12 ZARF-v1 metnini Batu'ya ayrı bir onay olarak sunmuyor. K-3 yalnız haritaya eşlemeyi soruyor; §0 madde 6 "aynen uygulansın" öneriyor. Batu "aynen" derse modelin yorumu onun sözü olarak kayda geçer. Bu, taslağın ilke 11'iyle (söz ile yorum ayrı durur) ve M10.2'deki "gösterilmemiş yorumlar raporda" kuralıyla çelişir. K-009'da ana oturumun kendi formülasyonu Batu'nun sözünden ayrılmıştı; aynı düzeltme burada yapılmamış.
- **Kanıt:**
  - A002: "Kapsam değişikliği, yeni erişim ve cevaplayamadığım tercih soruları sana gelsin. Sorular biriksin, iş durmasın." — kaynak diyor (U003'te onaylanan metin).
  - MB-08: "YT-5 cevaplanamayan tercih sorusu (birikir) · YT-6 çerçeve sorusu (biriktirilmez)" — kaynak diyor.
  - MB-08: "1) Kendiliğinden: … M ve T kararları" — kaynak diyor.
  - MB-08: "Yazan yalnız ana oturum; zarfın içeriği Batu'nun." — kaynak diyor.
  - Ek T4 S1-M2, kabul testi: "K-002 eşlemesinin Batu kararı olarak kaydı." — kaynak diyor. T4 zarfın Batu kararı olarak kaydedilmesini istiyordu; METHOD §12 bunu bir onay satırına çevirmemiş — çıkarım.
  - DECISIONS K-009: "27 Eylül'de söz ile yorum ayrıldı (METHOD taslağı §0 madde 4'ün tespiti)." — kaynak diyor (iyi örnek).
- **Öneri:**
  - §12.2'ye ayrı bir satır ekle: "ZARF-v1: onayladığın dört cümle ve benim eklediklerim". İki sütunlu olsun:
    - senin sözün, birebir;
    - benim eklemem ve nedeni.
  - "Çerçeve soruları biriktirilmez, bağlı kalemler park edilir" değişikliğini özellikle görünür yaz.
  - MB-08'deki "zarfın içeriği Batu'nun" ifadesini düzelt: "Zarfın içeriğini Batu onaylar; onaylanana kadar ZARF-v1 ana oturumun önerisidir."

### E3-06 · önemli · Yapan ile kontrol eden birkaç kilit noktada aynı aktör

- **Yer:** MB-12 (sınıflama); MB-13 (kapı hükmü); MB-16 (soğuk başlangıç puanı); MB-14 ve O-7 (sürekli izin); MB-17 ve W10 (L-001).
- **Sorun:** Taslak üretimi eleştiriden ayırıyor: `e7-elestirmen` B2, `e7-dogrulayici` B3. Ama kontrolün ağırlığını, geçiş kararını ve denetçinin ayarını denetlenen aktöre bırakıyor. Beş nokta:
  1. Kalemin R0–R3 sınıfını, yani eleştirmenin çağrılıp çağrılmayacağını, işi planlayan ve birleştirecek olan ana oturum belirliyor. R0'da "ana oturumun kaynak kontrolü" yetiyor.
  2. Kendiliğinden geçen aşamalarda (P1→P2↔P3→P4) kapı hükmünü aşamayı yürüten ana oturum veriyor.
  3. Soğuk başlangıç testinin soruları, beklenen cevapları ve puanlaması ana oturumda. Sınanan şey ise ana oturumun kendi devir yazımı.
  4. O-7 kabul edilirse ana oturum, denetleyici rollerin gövdesindeki yöntem metnini ve `model`, `effort`, `maxTurns` değerlerini Batu'ya sormadan değiştirebilir. MB-14'teki "denetleyici rolün ölçütü ya da eşiği" satırı yöntem metnini ve modeli kapsamıyor. Denetlenen, denetçisini hafifletebilir.
  5. Taslağın tek "doğrulandı" örneğini (L-001) yazar kendisi doğrulanmış sayıyor. Oysa taslağın kuralı "doğrulandı"yı B3 ve üstüne ayırıyor (taze ve gerekçeyi görmeyen bağlam artı ayrı kanıt yolu); W10 da tarafsız gözlem istiyor ("sınama dersin adını anmaz"). L-001'in taşıyıcısı ise dersi adıyla anan bir brief kuralı.
- **Kanıt:**
  - A4 (R03 ilke 12): "Yapan ile kontrol eden ayrılmalı ve her ikisi de başarı kriterlerini çok net bilmelidir." — kaynak diyor.
  - MB-12: "Ne zaman / Kim: kalem açılırken ve kapsam değişince; ana oturum." — kaynak diyor.
  - MB-12: "**R0** hepsi hayır → yoklama töreni: brief, dönüş, ana oturumun kaynak kontrolü" — kaynak diyor.
  - MB-13: "hüküm kendiliğinden aşamada ana oturumun, durakta Batu'nun" — kaynak diyor.
  - MB-16: "ana oturum başlatır ve puanlar" — kaynak diyor.
  - MB-14: "Rol gövdesinde yöntem metni; rolün `model`, `effort`, `maxTurns` değeri; skill'de yöntem adımı … | ana oturum, Batu'nun P0.8'de vereceği **sürekli izinle**" — kaynak diyor.
  - MB-14: "Denetleyici rolün ölçütü ya da eşiği | Batu ya da denetlenen işten bağımsız bir onay" — kaynak diyor.
  - §4.1: "\"Doğrulandı\" kelimesi yalnız B3 ve üstünde kullanılır." — kaynak diyor.
  - MB-17: "taşıyıcı: görev tanımı kuralı "çıktıyı tek seferde yaz"" ve "→ **doğrulandı (gözlem, 27.09.2026)**" — kaynak diyor.
  - W10 adım 4: "sınama dersin adını anmaz" — kaynak diyor.
  - L-001'in B3 koşulunu karşılamadığı — çıkarım.
- **Öneri:**
  1. Kapıda eleştirmen sınıflamadan örnek alsın: her aşamada R0 ya da R1 sayılan kalemlerden en az ikisi, sınıf gerekçesiyle eleştirmene gitsin. Yanlış düşük sınıf ders kaydına (L) girsin.
  2. Kendiliğinden geçişte GEÇ hükmünün ön koşulu, eleştirmenin `butun-inceleme` dosyasındaki hüküm satırı olsun. `bash-kapisi.sh` Z4 yalnız KAPI.md'yi değil, bu dosyayı da arasın.
  3. Soğuk başlangıcı `e7-dogrulayici` puanlasın. Beklenen cevapların önceden özetiyle kaydı zaten var.
  4. MB-14'te dört denetleyici rolün (`elestirmen`, `dogrulayici`, `eksik-arayici`, `taze-okuyucu`) gövde yöntem metni, modeli ve eforu sürekli iznin dışında kalsın.
  5. L-001'i "gözlendi (B0, yazarın git gözlemi)" diye yeniden etiketle. W10'daki "canlı örnek" iddiasını buna göre düzelt.

### E3-07 · önemli · Yöntemin çoğu çalışma anında yüklenen bir taşıyıcıya bağlı değil; yetkili metin dağınık

- **Yer:** Başlık notu (satır 4); §5.1; §6.1–§6.2; MB-09; §12.3; ilke 3.
- **Sorun:** İlke 3 "Kalıcı olan, yüklenmedikçe işe yaramaz" diyor. §5.1'deki 157 kartın zorlama düzeyi şöyle dağılıyor:
  - 113 kart yalnız tavsiye ya da yapısal düzeyde.
  - 29 kartın zorlayıcı öğesi yalnız tek repolu oturumdaki, hiç çalıştırılmamış bir hook'a bağlı.
  - Her oturumda geçerli bir zorlayıcı öğe yalnız 15 kartta var.

  Tavsiye ve yapısal kartlar ancak tetik anında modelin bağlamına girerse işler. Çalışma anında yüklenen metin şunlardır: kök CLAUDE.md (66 satır), ortak sözleşme (≤120 satır), rol dosyaları, hook enjeksiyonları ve skill'ler. 10 skill'in 6'sının metni yok. Kart ile taşıyıcı arasında bir eşleme de yok: hangi kartın hangi skill adımı, şablon alanı ya da hook ile tetik anında yüklendiği yazılmamış. Kartların yetkili metni altı dosyaya dağılmış: METHOD (218 KB) ve değişmeyen kartlar için dondurulmuş T1–T5 (≈947 KB). §6'da taslakların klasörü "alt ajan çıktıları (türetilmiş görünüm)" ve K3 katmanı sayılıyor. Çelişkide METHOD geçerli olduğundan bir kartı okumak iki dosyanın uzlaştırılmasını gerektiriyor; R-7 bunun farkında olmadan ezilmiş kararlar üretebileceğini kabul ediyor. Yöntemin kendi bütçeleriyle (açılış seti ≤50 KB, alt ajan zorunlu okuması ≤120 KB) bu metnin tamamını hiçbir aktör okuyamaz. Brief'in sorusu buydu: metin fazla karmaşıksa düzen kâğıtta kalır.
- **Kanıt:**
  - §1 ilke 3: "Kalıcı olan, yüklenmedikçe işe yaramaz. Kural yeniden yüklenen bir taşıyıcıya bağlanır: CLAUDE.md, skill, rol dosyası, hook enjeksiyonu" — kaynak diyor.
  - §5.1'deki zorlama sütunu, `awk` ile sayıldı (satır 435–591): — gözledim.
    - 157 kart;
    - zr içermeyen 113;
    - zr¹ içeren 31, bunların 29'unda her oturumda geçerli bir zr yok;
    - her oturumda geçerli zr taşıyan 15.
  - Satır 4: "Bu metin bir taslakla çelişirse bu metin geçerlidir; değişmeyen kartların tam metni taslaktadır." — kaynak diyor.
  - STATE: "Beş taslak toplam ≈ 947 KB." — kaynak diyor.
  - §6.1: "research/ drafts/ reviews/   alt ajan çıktıları (türetilmiş görünüm; son bölüm dönüş zarfı)" — kaynak diyor.
  - §12.3: altı skill için "**metin yok**; P0.6'da yazılır" — kaynak diyor.
  - Taşıyıcısı olmayan kartların tetik anında uygulanmayacağı — çıkarım; taslağın kendi ilke 3'ünün doğrudan sonucu.
- **Öneri:**
  - P0.6'da §5.1'e bir "taşıyıcı" sütunu ekle. Değerleri: CLAUDE.md §n · skill ve adımı · şablon alanı · hook · rol dosyası · yok.
  - "Gerekli" olup taşıyıcısı "yok" olan her kart için üç yoldan biri seçilsin: bir taşıyıcıya bağlanır, başka kartla birleştirilir ya da gerekçesiyle ertelenir.
  - METHOD-v1.md her kartın işletim metnini kendisi taşısın. Dondurulmuş taslaklar yalnız gerekçe ve kanıt için okunsun; çalışma anındaki hiçbir adım bir taslak satırına işaret etmesin.
  - Kabul ölçütü: bir kartı uygulamak için gereken metin tek dosyada ve tetik anında yüklenen bir taşıyıcıda durur.

### E3-08 · önemli · Kimlik çakışmaları kaymayı ve soğuk başlangıcı zorlaştırıyor

- **Yer:** §6.3; §0; §12.2; W4; Ek T4 S1-M5; CLAUDE.md taslağı §5; MB-02'deki olay sözlüğü.
- **Sorun:** Taslak 30'u aşkın kimlik ailesi kullanıyor ve bunların bir kısmı çakışıyor. Batu'nun okuyacağı karar paketinde bu turun öneri kimlikleri (K-1…K-10) Batu'nun kendi kararlarıyla (K-001…K-010) yan yana duruyor:
  - K-3 K-002'nin uygulanmasıdır; K-003 main'e birleştirme kararıdır.
  - K-8 dal politikasıdır; K-008 kayıt iznidir.
  - K-9 "sonraki söz öncekinin yerine geçer" kuralıdır; K-009 ayrı dal kararıdır.
  - K-10 A-05 ve A-07'nin açık kalmasıdır; K-010 ChatGPT ile bağlantı olmamasıdır.

  Diğer çakışmalar:
  - "A-02" (pilot sorusu) ile "A002" (sürekli yetki metni) aynı paragrafta geçebiliyor.
  - "R01" hem bir araştırma notu hem AGENT.md'nin "R01 Varsayımlar" rotası. "R1" bir risk sınıfı, "R-1" bir risk.
  - W4'teki "M7.5'in S1–S5 soruları" S1–S5 alt sistemleriyle çakışıyor.
  - "U1–U8" uyarlama maddeleri U001–U006 ile çakışıyor.
  - "G1–G4" sınamaları G-<Pn>-nnn dağıtımlarıyla çakışıyor.
  - "D1–D6" rol farkları dönüş zarfının D1–D3 alanlarıyla çakışıyor.
  - "K" hem Batu kararı, hem K0–K3 bağlam katmanı, hem K tamamlanma katı.

  Taslak bu riski biliyor: Y yerine YT, D- yerine L- yeniden adlandırması yapıldı (BK-10, BK-03). Ama çakışmaların çoğu duruyor. Ayrıca CLAUDE.md §5 GUNLUK'a `IHLAL` yazdırıyor; bu olay adı MB-02'deki tek olay sözlüğünde yok. Böylece "sözlük dışı statü 0" ölçütünü taslağın kendisi ilk kurulumda bozuyor. Batu'nun ilkesi "kayma her kelimeden doğabilir"; soğuk başlangıçtaki oturum bu kimlikleri ancak bağlamdan ayırt edebilir.
- **Kanıt:**
  - §12.2: "K-3 | K-002'nin yeni haritaya uygulanması" — kaynak diyor.
  - §12.2: "K-8 | Dal politikası" — kaynak diyor.
  - §12.2: "K-9 | "Batu'nun sonraki sözü öncekinin yerine geçer" kuralı" — kaynak diyor.
  - §12.2: "K-10 | A-05 ve A-07 açık kalır" — kaynak diyor.
  - DECISIONS: "K-003 | Main'e birleştirmeyi Claude yapar."; "K-008 | EXP-007 altında Claude'un kendi süreklilik kaydını tutma izni" — kaynak diyor.
  - §0 madde 2: "Pilotlar (A-02)" — kaynak diyor.
  - A002.md: "Aşağıdaki "Sürekli yetki" önerisi, U003 1. maddede kullanıcı tarafından onaylanan metindir." — kaynak diyor.
  - W4: "M7.5'in S1–S5 soruları" — kaynak diyor.
  - CLAUDE.md taslağı §5: "İhlal görülürse GUNLUK'a `IHLAL` yaz." — kaynak diyor.
  - `IHLAL` METHOD'da yalnız bir kez geçiyor ve MB-02'nin 36 olaylık sözlüğünde yok (grep) — gözledim.
  - A4 (R03 ilke 9): "Her kelimeden drift yapabilir." — kaynak diyor.
- **Öneri:**
  - Karar paketindeki öneri kimliklerini Batu kararlarıyla karışmayacak bir öneke çevir. Örneğin O- ve K- maddelerini birlikte "Ö-1…Ö-18" yap.
  - §6.3'e bir çakışma yasağı ve kullanılan tek harfli öneklerin listesini ekle. Örnek yeniden adlandırmalar:
    - R-1…R-7 → RİSK-1…RİSK-7;
    - M7.5'in soruları → SS-1…SS-5;
    - U1–U8 → UY-1…UY-8.
  - `IHLAL`'i sözlüğe ekle ya da CLAUDE.md §5'te mevcut bir olay adını kullan (HATA).
  - `tools/hijyen.sh`'e sözlük dışı olay adı taraması koy.

### E3-09 · önemli · Kurulum commit'i, sınanmamış hook'ları kurulumu yapan oturumda hemen devreye sokabilir

- **Yer:** §12.3 adım 3–7; MB-14'ün "Yürürlük" sütunu; MB-06; MB-07'de `yapilandirma-dondurma.sh`; §13.3.
- **Sorun:** Taslak yapılandırmanın "kurulum commit'inden sonraki oturumda" yürürlüğe girdiğini varsayıyor ve doğrulamayı yeni oturumda yapıyor (adım 6). Belge ise iki şey söylüyor: settings dosyasındaki `permissions` ve `hooks` düzenlemeleri çalışan oturuma yeniden yüklenir (cloud'da denenmedi); CLAUDE.md bir sonraki `/compact`'ta, bulutta yani bir sonraki sıkıştırmada yüklenir. Bu doğruysa P0.8 commit'iyle dokuz hook, hiçbiri çalıştırılmamışken (R-6), kurulumu yapan oturumda devreye girer. Olası sonuçlar:
  - `bash-kapisi.sh` koordinatörün sonraki commit'ini reddedebilir: adım 5'teki METHOD bloklarını işaretçiye çeviren ikinci commit ya da adım 7'deki `git revert`. Ret, "Onay: K-xxx" ya da yol kuralından gelebilir.
  - `durma-kapisi.sh` tur bitişini engelleyebilir.
  - Settings değişikliğini donduran `yapilandirma-dondurma.sh` aynı commit'le geldiği için ilk kurulumu koruyamaz.
  - MB-14'ün acil geri alma satırı böyle bir kilitte Batu'nun onayını gerektiriyor.

  Ayrıca MB-14'teki "sonraki oturum" yürürlüğü CLAUDE.md için doğru değil: yeni metin aynı oturumun ilk sıkıştırmasında yüklenir.
- **Kanıt:**
  - R07 satır 719: "C~: Ayar dosyası oturum ortasında değişirse yeniden yüklenir: "applies most edits to the running session without a restart, including edits to `permissions`, `hooks`" (SET). … cloud'da denenmedi." — kaynak diyor (tedarikçi belgesi, alt ajan aktarımı; C~).
  - R07 satır 439: "Editing them mid-session does not invalidate the cache, but the edit also doesn't apply. … The new content loads on the next `/clear`, `/compact`, or restart." (PC) — kaynak diyor (C~).
  - Ek T5 satır 62: "settings ve skill değişiklikleri ConfigChange hook'uyla dondurulur" — kaynak diyor.
  - MB-14: "… hook; settings; CLAUDE.md'nin kural içeriği … | kurulum commit'inden sonraki oturum" — kaynak diyor.
  - MB-14: "Acil geri alma (bozuk hook işi durduruyor) | ana oturum `DURAK: hata` yazar; Batu tek satırla onaylar" — kaynak diyor.
  - Dondurma hook'unun ilk kurulumda kendini koruyamayacağı ve kurulum oturumunun kilitlenebileceği — çıkarım.
- **Öneri:**
  - Kurulumu atılacak bir oturumda yap. O oturum yalnız yazar, commit eder, push eder ve biter; doğrulamayı yeni oturum yapar.
  - Ya da hook'ları iki commit'le kur: önce yalnız `yapilandirma-dondurma.sh`, sonra kalanlar.
  - CD listesine "settings oturum içinde yeniden yükleniyor mu" denemesini ekle; CD-18 ile aynı atılacak dalda koşulabilir.
  - MB-14'ün yürürlük sütununu düzelt: "sonraki oturum ya da sonraki sıkıştırma, hangisi önce gelirse".

### E3-10 · önemli · Auto kipinin sınıflandırıcı sayacı uzun ömürlü koordinatörü sessizce istemde bekletebilir; taslakta yok

- **Yer:** §14.2; §13.1 (pilot soruları); MB-15; S19.5; Ek T5'in açık soruları.
- **Sorun:** K-001'in amacı Batu "devam" yazmadan ilerlemek; taslak bunu nabız, durma kapısı ve alarmla kuruyor. Belgeye göre Auto kipi, 3 ardışık ya da toplam 20 sınıflandırıcı engelinden sonra durur ve istem açmaya döner. Bu oturumda sınıflandırıcı en az bir kez engelledi. Günlerce süren, çok sayıda push, tetik ve oturum çağrısı yapan tek bir koordinatör oturumunda toplam 20 engele ulaşmak mümkün. Bundan sonra her riskli çağrı istemde bekler; oturum Batu'yu bekler. Bu bekleme ne durma kapısına görünür (tur bitmez, istemde asılı kalır) ne de takılma alarmına (alarmı gönderecek aktör istemde bekliyor). İlk işaret Batu'nun fark etmesi olur. T5 bu sayacı açık soru olarak yazmıştı: deny kuralına takılan çağrılar sayaca giriyor mu? METHOD'un açık sorularına ve pilot sorularına bu geçmemiş.
- **Kanıt:**
  - R01 cloud C13'ün "İlgisi" (satır 550): "Auto mode pauses and returns to prompting after 3 consecutive or 20 total classifier blocks (same page)." — kaynak diyor (tedarikçi belgesi, alt ajan aktarımı).
  - Ek T5 satır 1779: "**Deny kuralına takılan çağrılar**, Auto kipinin "3 ardışık ya da 20 toplam engel" sayacına giriyor mu?" — kaynak diyor.
  - Ek T5 satır 39: "Otomatik kip sınıflandırıcısı "Credential Exploration" gerekçesiyle reddetti" — kaynak diyor (T5'in bu oturumdaki gözlemi).
  - R01 satır 291: "Otherwise shell, network and push commands prompt, and the loop stalls until the user answers. Background subagent prompts surface in the main session." — kaynak diyor.
  - METHOD'da "sınıflandırıcı" ya da "classifier" hiç geçmiyor (grep) — gözledim.
  - Sayaç dolunca özerkliğin sessizce durduğu — çıkarım.
- **Öneri:**
  - PS-1'e "sınıflandırıcı sayacı" alt sorusunu ekle ve Batu'nun izniyle bir deneme tanımla; örneğin bilerek engellenecek zararsız bir çağrı dizisiyle sayacın davranışını gözle.
  - Nabızla uyanan tur, bir önceki turun istemde asılı kalıp kalmadığına baksın; asılıysa alarm yazsın.
  - Koordinatör her sınıflandırıcı engelini GUNLUK'a HATA satırıyla yazsın.
  - Planlı taze oturumu (M7.6) yalnız sıkıştırmaya değil, bu sayaca da bağla; örneğin GUNLUK'tan sayılan 10 toplam engelde taze oturuma geçilsin.

### E3-11 · önemli · Pilotlar kalıcı rolleri ve araç sınırını sınamıyor

- **Yer:** §13.2 adım 1; MB-18 madde 2; MB-15; K-4 (CD-18); §13.3.
- **Sorun:** Pilot-1, "roller kurulu olmadığı için" `general-purpose` ajan ve brief'e konmuş rol metniyle koşuyor. Bu, Batu'nun U004'te reddettiği "her seferinde rol biçmek" düzeninin kendisi. Tasarımın en çok güvendiği iki öğeyi de dışarıda bırakıyor: kalıcı rol dosyası ve rol başına araç listesi. O-2 araç listesini "her oturumda geçerli tek gerçek zorlama" sayıyor. Gözlemim: bu turda `general-purpose` olarak çalışan bu alt ajanın araç listesinde `send_later`, `create_trigger`, `create_session`, `add_repo` ve GitHub yazma araçları (`push_files`, `merge_pull_request`) var. Dolayısıyla MB-15'teki "Alt ajanlarda bu araçlar yoktur" cümlesi pilot döneminde yalnız brief metniyle korunuyor. Pilotlar hem bu değişmezi sınamadan geçiyor hem de değişmezin geçerli olmadığı bir ortamda koşuyor. Oysa CD-18 rol dosyalarını zaten bir atılacak dala kurmayı öngörüyor; sıra değişirse pilotlar gerçek rol dosyalarıyla koşabilir.
- **Kanıt:**
  - §13.2: "Roller kurulu olmadığı için `general-purpose` ve birebir rol metni kullanılır (MB-18)." — kaynak diyor.
  - MB-18: "araç zorlaması olmadığı için pilotlar düşük riskli tutulur." — kaynak diyor.
  - MB-15: "Alt ajanlarda bu araçlar yoktur." — kaynak diyor.
  - O-2: "Araç listesi her oturumda geçerli tek gerçek zorlamadır" — kaynak diyor.
  - Bu alt ajanın araç listesi (27.09.2026, bu oturum): `mcp__Claude_Code_Remote__send_later`, `…create_trigger`, `…create_session`, `…add_repo`, `mcp__github__push_files`, `mcp__github__merge_pull_request` var; Agent aracı yok — gözledim (Cg).
  - U004: "her seferinde yeninden alt ajana rol biçmek doğru değil" — kaynak diyor.
  - MB-19: CD-18 rollerin, skill'lerin ve CLAUDE.md'nin görünüp görünmediğini sınar, "(atılacak dalda, Batu izniyle)" — kaynak diyor.
- **Öneri:**
  - P0.7'nin sırasını değiştir. Önce CD-18: atılacak dala rol dosyaları, ortak sözleşme skill'i ve CLAUDE.md kurulsun; hook'ların dahil olup olmadığı açıkça yazılsın.
  - Sonra pilotları o dalda açılan oturumda, gerçek e7 rolleriyle koş. Böylece pilotlar O-2'yi, M16.1'i ve PS-2'yi aynı anda sınar. Atılacak dal pilottan sonra silinir.
  - Bu mümkün değilse Pilot-1'in sınanan kartlarından MB-04'ü çıkar: rol tarifi brief'e girdiği için MB-04'ün "brief'te rol yok" ölçütü pilotta zaten ihlal edilir. Sonuç raporuna "kalıcı roller sınanmadı" yaz.

### E3-12 · önemli · Maliyet: bütün haritanın tahmini yok; koordinatörün bağlam × adım maliyeti sınırsız

- **Yer:** §11.1, §11.3, §11.5; MB-09; MB-10; §2'deki V-H-5; W5.
- **Sorun:** Taslak ölçü birimini doğru düzeltmiş (işlenen token, transcript kaynağı) ve tür bütçeleri ölçülmüş koşulardan geliyor. Dört boşluk kalıyor:
  1. **Harita tahmini yok.** Tahmin yalnız P0'ın kalanını kapsıyor (135–220 M). P1–P6 için aşama ya da harita tahmini yok; bu yüzden V-H-5 ("haftalık limit aşama bütçelerini taşır") sınanamıyor. Taslağın kendi sayılarıyla bir aşama kabaca 135–500 M işlenen token ve 11–20 alt ajan koşusu tutar; P1–P6 ≈ 1,2–2,3 milyar (§5).
  2. **Koordinatör bütçesi yok.** MB-09'un bağlam × adım disiplini yalnız alt ajanlara bütçe koyuyor (tepe ≤300 K). Taslağın maliyet formülü ("işlenen ≈ ortalama bağlam × adım") en büyük bağlamı taşıyan koordinatöre uygulanmıyor. Yeni ritüellerle koordinatör kalem başına ~20–30 araç çağrısı yapıyor: brief, `wc -c`, commit'ler, DAGITIM, dönüş kontrolü, en az iki iddianın kaynakta okunması, GUNLUK, ölçüm betiği, ISLER, STATE, push, nabız silme ve kurma. 150–400 K ortalama bağlamla bu, kalem başına 3–12 M ve aşama başına 30–180 M eder. P0'daki %15'lik koordinatör payı bu ritüeller yokken ölçüldü; ≤%15 tören payı hedefi bu yüzden gerçekçi değil.
  3. **VM kaybı fiyatlanmamış.** W5'te VM geri alınmasındaki dalga kaybı "kabul edilen kayıp" sayılıyor, ama ölçülmüş dalga maliyetiyle (~150 M) fiyatlanmıyor. Sonuçlarının VM geri alınmasından sağ çıktığı belgelenmiş tek çok ajanlı yol olan Workflow ise "bilinmiyor" bırakılmış.
  4. **Taban geçersiz.** Brief'teki karşılaştırma tabanı ("P0.3'e kadar yaklaşık 6,5 milyon token") eksik sayan bir sayaçtan geliyor.
- **Kanıt:**
  - STATE, "Maliyet": "Eski rakam yanlıştı. "Yaklaşık 6,5 milyon token" görev bildirimlerindeki `subagent_tokens` alanından toplanmıştı." — kaynak diyor.
  - `tools/token-kullanimi.py` (27.09.2026 11:53 UTC): "TOPLAM: çağrı=1625 işlenen=461.7M (önbellekten okuma 436.5M, önbelleğe yazma 24.3M, çıktı 1.0M); girdi eşdeğeri ≈ 79.0M–97.2M" — gözledim. Transcript'lerin ne kadarının VM'de korunduğu bilinmiyor.
  - MB-09: "alt ajan hedef tepe bağlamı ≤300 K token" — kaynak diyor.
  - MB-09: "Kaba ilişki: işlenen token ≈ ortalama bağlam × adım sayısı (çıkarım)" — kaynak diyor.
  - MB-09: "tepe bağlam için zorlayıcı araç yok" — kaynak diyor.
  - §11.1: "Ana oturum | 792 K'da sıkıştırıldı" — kaynak diyor.
  - §11.3: "Başlangıç hedefi ≤%15 (varsayım; T5 S21.5)." — kaynak diyor.
  - R01 multiagent C12: "In a cloud session, Claude Code also saves the run's results with the session's conversation history, which survives when the session's VM is reclaimed." — kaynak diyor (C+).
  - METHOD §3, S12: "Dinamik workflow | bilinmiyor" — kaynak diyor.
  - R01 cloud C15: "'A single burst of heavy activity, such as a large workflow fanout, can exhaust the weekly allowance'" (errors.md aktarımı) — kaynak diyor.
  - Aşama tahmini ve koordinatör maliyeti — çıkarım (varsayımlar §5'teki tabloda).
- **Öneri:**
  - §11'e aşama başına ve bütün harita için bir tahmin tablosu ekle: tür bütçesi × beklenen koşu sayısı, artı bir koordinatör satırı. V-H-5'i bu tabloya bağla.
  - MB-09'a koordinatör bütçesi ekle: ortalama bağlam hedefi (örneğin ≤300 K) ve kalem başına araç çağrısı sayısı GUNLUK'tan ölçülsün; aşılınca planlı taze oturuma geçilsin.
  - Kalem kapanışındaki çağrıları birleştir; örneğin GUNLUK, ISLER ve STATE'i tek betikle güncelleyip tek commit atan bir `kalem-kapanisi` yardımcısı.
  - Workflow'u dalga taşıyıcısı olarak PS-1'e bir deneme olarak ekle.
  - Haftalık limit için CD-15'i beklemeden bu oturumun verisini kaydet: 26–27 Eylül'de ~79–97 M girdi eşdeğeri harcandı ve STATE'te limit olayı kaydı yok. Bu yalnız zayıf bir alt sınır ipucudur.

### E3-13 · küçük · K-1 "başla"yı kurulumdan önce istiyor; kurulum commit'leri SHA'ya bağlı kabulü bayatlatıyor; CD-18'in yetki dayanağı belirsiz

- **Yer:** §2'deki P0 satırı; §12.2 K-1; §12.3 adım 3–5; §13.3; §3'teki S2 satırı ("SHA'ya bağlı kabul paketi"); K-4.
- **Sorun:** Üç ayrı sorun var.
  1. K-1, METHOD kabulünü ve "başla"yı tek karar yapıyor ve kurulumdan önce istiyor. Kurulum ise METHOD'u değiştiriyor: bloklar işaretçiye dönüyor, göç yapılıyor. S2-M4'e göre SHA'ya bağlı kabulden sonraki her değişiklik kabulü "bayat" yapar.
  2. "Başla", CD-01 ve soğuk başlangıç geçmeden verilmiş oluyor. K-005'in "nasıl net ortaya konmadan başlanmaz" koşulu, kurulumun çalıştığı görülmeden karşılanmış sayılıyor.
  3. CD-18 atılacak dala `.claude/` kuruyor ve bunu K-4'ün deneme izniyle yapıyor. A-04 ise yapılandırmanın Batu onayı olmadan kurulmamasını söylüyor. Atılacak daldaki bu kurulumun A-04 kapsamına girip girmediği yazılmamış.
- **Kanıt:**
  - §12.2 K-1: "METHOD v1'in kabulü ve "başla" (P0 çıkışı; SHA'ya bağlı; K-005)" — kaynak diyor.
  - §12.3 adım 5: "METHOD blokları işaretçiye döner (ikinci commit)." — kaynak diyor.
  - §3, S2 satırı: "SHA'ya bağlı kabul paketi | … her kabulde SHA; sonraki değişiklik "bayat"" — kaynak diyor.
  - DECISIONS A-04: "Batu onaylamadan kurulmaz." — kaynak diyor.
  - MB-19, CD-18: "(atılacak dalda, Batu izniyle)" — kaynak diyor.
- **Öneri:**
  - K-1'i ikiye böl:
    - (a) METHOD kabulü ve kurulum yetkisi. Kurulumun yapacağı mekanik farklar kabul paketinde önceden listelenir; bunlar kabulü bayatlatmaz.
    - (b) "Başla". CD-01 ve soğuk başlangıç geçtikten sonra, kurulu yapılandırmanın SHA'sına bağlı, tek satırlık ayrı bir soru olarak sorulur.
  - K-4 metnine şu cümleyi ekle: "CD-18 atılacak dalda `.claude/` dosyaları yazar; bu, A-04 kapsamında sınırlı bir kurulumdur."

### E3-14 · küçük · "Sürücünün gözlerini takip eden sistem" öz-denetime eşlenmiş; benzetme tersine dönmüş

- **Yer:** §10.2, U004-11.
- **Sorun:** Batu'nun benzetmesinde göz takip sistemi, sürücüyü dışarıdan izleyen ayrı bir aygıttır. Taslak bunu S15-M5 öz-denetimine, yani sürücünün kendi kendini denetlemesine, ve S17-M3'e eşliyor. Doğru karşılık, ana oturumu dışarıdan izleyen bir mekanizmadır: hook'lar, GUNLUK'tan mekanik olarak hesaplanan alarm, eleştirmenin iz denetimi. Bu eşleme benzetmenin güvenlik anlamını zayıflatıyor ve söz karşılanmış gibi görünüyor.
- **Kanıt:**
  - U004: "ne sürücünün gözlerini takip eden sistem" — kaynak diyor.
  - §10.2: "göz takibi: S15-M5 öz-denetim, S17-M3" — kaynak diyor.
  - Eşlemenin tersine döndüğü — çıkarım.
- **Öneri:**
  - Göz takibinin karşılığını "dışarıdan izleme" olarak yeniden kur: GUNLUK'tan betikle hesaplanan ilerleme ve takılma göstergesi (S17-M2 ve S17-M3'ün mekanik kısmı) ile aşama sonunda öz-denetim satırlarının eleştirmence okunması.
  - S15-M5'i "yorgunluk uyarısı" satırına ya da ayrı bir satıra taşı.

### E3-15 · küçük · İlke 10 tutarsız uygulanıyor: gözlenmemiş riskler için hook var, Batu'nun sözünün birebir kaydı için yok

- **Yer:** §1 ilke 10; MB-07; §3'teki S19 satırı ("Ham söz kaydı hook'u").
- **Sorun:** İlke 10 "Hook yalnız gözlenmiş bir kayma noktasına konur" diyor. Ama `hata-kaydi.sh` (StopFailure) ve `yapilandirma-dondurma.sh` (ConfigChange), EXP-007'de gözlenmemiş risklere dayanıyor. Buna karşılık Batu'nun sözünü birebir kaydedecek hook (UserPromptSubmit) "gözlenince" diye ertelenmiş. Bu hook, taslağın ilke 11'inin ve Batu'nun "kayma her kelimeden" ilkesinin mekanik taşıyıcısı olabilirdi. U-dosyaları bugün modelin kendi aktarımı; platform dışa aktarımı değil. Öncelik ters: düşük değerli olay kaydı zorlanıyor, aynı modelden olmayan tek kanalın sözü ise tavsiyeye bırakılıyor.
- **Kanıt:**
  - §1 ilke 10: "Hook yalnız gözlenmiş bir kayma noktasına konur" — kaynak diyor.
  - §3, S19 satırı: "Ham söz kaydı hook'u (UserPromptSubmit) | bilinmiyor (ertelendi) | söz yalnız parafrazda yaşar | pilotta U-dosyası eksik çıkarsa eklenir" — kaynak diyor.
  - Ek T5 satır 741: "Limit riski [R11 K22]" — kaynak diyor.
  - `sources/conversation/INDEX.md`: "Platform dışa aktarımı değildir." — kaynak diyor.
- **Öneri:**
  - İki yoldan birini seç: ilke 10'u açıkça "gözlenmiş kayma ya da düşük bedelli olay kaydı" diye genişlet ya da risk dayanaklı hook'ları çıkar.
  - Batu'nun mesajını `sources/conversation/` altına ham olarak yazan bir UserPromptSubmit hook'unu (tek repolu oturumda) dokuz hook'tan birinin yerine koymayı değerlendir. Hook sınırı ≤9 korunur.

### E3-16 · küçük · P1'deki `add_repo`, koordinatör oturumunu çok repolu yapıp hook katmanını düşürebilir

- **Yer:** §12.2 K-4; §14.2 soru 10; §14.3.
- **Sorun:** Taslak P1'de Loopinance repolarını salt okuma `add_repo` ile bağlamayı planlıyor. Belgeye göre çok repolu cloud oturumunda repo settings dosyasının hook'ları ve izin kuralları okunmaz. `add_repo`'nun bunu oturum ortasında tetikleyip tetiklemediği bilinmiyor. Taslak bunu açık soru olarak yazmış, ama işi koordinatör oturumunda yapmayı öngörüyor. Tetiklerse P1 boyunca zr¹ katmanı sessizce tavsiyeye düşer; bu katman 29 kartın tek zorlayıcı öğesi. Kanarya bunu ancak bir sonraki açılışta görür. Bu oturuma da iki Loopinance reposu bağlanmıştı; bu oturumun tek repolu sayılıp sayılmadığı bilinmiyor.
- **Kanıt:**
  - R01 satır 364: "In a multi-repo cloud session, hooks and other keys in repository settings files are not read." — kaynak diyor.
  - §12.2 K-4: "P1'de CD-10, CD-13 ve Loopinance repoları için salt okuma `add_repo`" — kaynak diyor.
  - STATE: "İki Loopinance reposu bu oturuma salt okuma için bağlandı ve klonlanmadı." — kaynak diyor.
- **Öneri:**
  - Loopinance okumalarını koordinatör oturumunda yapma; bu iş için açılan ayrı bir oturumda (CD-04) ya da atılacak bir oturumda yap.
  - CD-13'ün ilk ölçütü şu olsun: `add_repo`'dan sonra kanarya ve bir test hook'u hâlâ çalışıyor mu?

## 8. Çürütmeye çalışıp tutan yanlar

- **MB-04 görev tanımı.** Amaç zinciri, beslediği karar, işten önce yazılan bitti tanımı ve "bilerek verilmeyenler" alanı, "rota, hedef, ölçüt" ilkesini doğrudan taşıyor. "Beslediği karar yazılamıyorsa brief gönderilmez" kuralı emir erliğine karşı yapısal bir kapı.
  - Denediğim çürütme: 13 alanlı başlık formu amacın önüne geçirir mi?
  - Sonuç: Taslak bunu bozulma işareti olarak yazmış ("brief uzuyor"). Tuttu.
- **Soğuk başlangıç yolu.** CLAUDE.md taslağının §2'sinde sıra kısa, devir notu git'e karşı sınanıyor ve "yetki çözülemezse yeni iş başlamaz" kuralı açık. AGENT.md çakışması (E3-01) dışında tuttu.
- **ZARF madde 6.** "Otomatik istemler yetki değildir" kuralı platformun kendi kuralıyla uyumlu (R01 SP12). Tuttu.
- **K-009'da söz ile yorumun ayrılması.** Ana oturumun formülasyonu Batu'nun sözünden ayrılıp DECISIONS'a işlendi. Bu, "kayma" ilkesinin iyi bir uygulaması.
- **"Batu vekili" rolünün reddi.** Aynı modelden bir "Batu"nun bağımsız kanalın yerine geçmesini önlüyor (§4.1).
- **Dürüst sınırlar ve sayaç düzeltmesi.** §14.4 taslağın neyi kanıtlamadığını açıkça yazıyor. Yanlış sayaç olayı ölçüm sözleşmesine dönüştürülmüş (MB-10).
- **Dokuz ortam gerçeği.** Hiçbiriyle doğrudan çelişki bulamadım; her birinin taslakta bir karşılığı var. Boşluklar E3-09, E3-10, E3-12 ve E3-16'da.

## 9. Nasıl aradım; neyi aramadım

- **İlkeler:** R03'teki 18 ilkeyi ve U001–U006'yı okudum. Brief'teki on ilkenin her biri için taslağın §0–§14 bölümlerinde karşılayan ve ihlal eden yerleri aradım. Her ihlal iddiasını taslağın kendi satırıyla karşılaştırdım.
- **Batu'nun yükü:** Batu'ya yönelik bölümleri `wc -w` ile saydım. §12'nin maddelerini ve "Batu'nun eylemleri"ni saydım. Ek T4'ten S2-M2 ve S2-M5'i okudum.
- **Okunabilirlik:** Soğuk başlangıcı dört açılış biçiminde adım adım yürüttüm: kurulumdan önce, kurulumdan sonra dalda, main'den ve kart uygularken. Kimlik ailelerini grep'le çıkardım. Olay sözlüğünü CLAUDE.md'deki olay adlarıyla karşılaştırdım.
- **Ortam:** Dokuz gerçeğin her biri için kaynağı R01 ve R07'de buldum. P1-01'i tam okudum. Kendi araç listemi gözlem olarak kullandım.
- **Maliyet:** Taslağın tür bütçelerini ve ritüel tablosunu kullandım. Bu oturumun ölçümünü aldım.
- **Aramadım:**
  - T1 ve T3 kartlarının iç tutarlılığı;
  - E1'in konusu olan söz–çıktı ve standart seviye;
  - E2'nin konusu olan etkileşim matrisi;
  - hook betiklerinin doğruluğu.

## 10. Açık sorular

1. A-01, iki hatlı durumda hangi AGENT.md'yi kastediyor: ChatGPT hattının değiştirdiği main'deki mi, dalınki mi? (E3-01)
2. Batu, dikkatinin bir güvenlik kanalı olarak kullanılmasını istiyor mu, yoksa yalnız kabul mü veriyor? E3-02'deki önerinin kapsamını bu belirler; Batu'ya bir çerçeve sorusu olarak gitmeli.
3. Settings dosyası cloud'da oturum içinde yeniden yükleniyor mu? (E3-09; denenmedi)
4. Auto kipinin sınıflandırıcı sayacı deny kurallarını ve hook retlerini sayıyor mu? Sayaç oturum boyunca mı tutuluyor? (E3-10)
5. Arka planda alt ajan çalışırken oturum "boşta" sayılıyor mu? Bu oturumda uzun dalgalar tamamlandı (STATE); ama belge, geri alma sırasında çalışan alt ajanların kaybolduğunu söylüyor.
6. `add_repo` oturum ortasında settings okumasını değiştiriyor mu? (E3-16)
7. Haftalık limit, işlenen token'la nasıl ilişkili? (PS-3)

## 11. Bu notun kanıtlamadıkları

- Aynı modelden geldiğim için bu bir karşı-okumadır; hiçbir bulgu bağımsız doğrulanmadı.
- Ortam iddialarının kaynağı R01 ve R07'deki tedarikçi belgesi aktarımlarıdır. code.claude.com'u yeniden okumadım. Kendi araç listem ve ölçüm betiği dışında hiçbir şeyi canlı denemedim.
- §5'teki aşama maliyeti bir çıkarımdır: taslağın tür bütçeleri ile benim kalem ve koşu sayısı varsayımlarım birleştirildi. Ölçüm değildir.
- E3-07'deki sayım §5.1'in kısaltılmış zorlama sütununa dayanır; 157 kartı taslakların tam gövdeleriyle karşılaştırmadım.
- R11'in "beş olayın dördü" sayımını kaynağından doğrulamadım.
- Ölçüm betiği yalnız bu makinede kalan transcript'leri sayar; VM daha önce geri alındıysa gerçek harcama daha yüksek olabilir.
