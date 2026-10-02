# O4 — Loopinance: Claude Code'da gerçekten çalışan düzen

Okuyan: O4 · Kaynak: `/home/user/loopinance-claude-code` (salt-okunur klon, tek commit `e54b69f`, 2 Eyl 2026) · Kanıt dili: **kaynak diyor / gözledim / çıkarım / bilinmiyor**. Aşağıda "gözledim" = dosyada ya da tutanakta kendim okudum/ölçtüm.

## DevOS için en önemli çıkarımlar

1. **Çekirdek iskelet işe yaradı ve buluta taşınabilir:** tek kural kaynağı (`EL_KITABI.md`, 12,5 KB) + rol başına kısa sözleşme (`SOZLESME.md`, 3,7–6,3 KB, kural kopyası yok, ID ile atıf) + rol başına yerinde yeniden yazılan durum (`DURUM.md` ≤2 KB) + tek gündem (`PANO.md`). Hiçbiri plugin'e dayanmıyor (kullanıcı ayarında 22 plugin etkindi ama düzen hiçbirini çağırmıyor); yalnız md + bash + python. → **Uyarlayarak al.**
2. **En büyük zayıflık insan rölesiydi:** her rol ayrı Claude Code oturumuydu; Batu panoya bakıp oturumu elle açtı ve "sıra sende" yazdı. Seri koşum → "dayanaksız her ok doğrudan gecikmedir" (serbest iş 5 gün bekledi), yanlış rolün açılması, "Bitirdin mi bu oturumdaki işini? sıradaki oturum kim, koordinatör mü?" soruları (gözledim). → DevOS'ta sevk **orkestratör oturumunda** olmalı, Batu röle değil.
3. **"Metin hatırlatır; mekanizma zorlar."** Üç gerçek arıza kural metni varken oldu: paylaşılan git index süpürmesi (B4, `8224c11`), elle taranan erteleme uyanmasının kaçması (ERT-14), iskeleti açılmamış görevin panoda hiç görünmemesi. Üçü de ancak deterministik betik kontrolüyle kapandı. → Her kritik kurala mekanik karşılık (betik/hook/test).
4. **Deterministik bekçi (`bekci.sh`) en sağlam parçaydı:** 17+ kontrol, `--test` 61/61, koşu kilidi, 2 Eyl'de koşu #713. Ama: hook danışmandı (`--hook` her zaman `exit 0`), SAGLIK anlık görüntülerinin yalnız ~%6–12'si commit'lendi, **DAVRANIŞ ışığı hiç ölçülmedi** (betikte sabit `VERİ-YOK`). → Al; kapanış adımında senkron + CI'da koştur; ölçemediğini ışık diye gösterme.
5. **Doğrulama zinciri gerçek hata yakaladı:** "350 yeşil testin arkasında hiç inşa edilmemiş bir motor"; KT-000 retrosu "kapanış uygun değil" (4 eksik); PO kararına 8 çürütücünün 8'i haklı vurdu. Araçlar: yeşil ref'e (commit'li) koşma, Testçi çiti (ayrı dizin/port/DB/distDir), golden beklenen değer karardan (import-ban lint), Denetçi kör-türetme. → **Al.**
6. **Maliyet ve bürokrasi patladı:** kapı başına 9–13 ajanlı çekişmeli workflow, çoğu 0,7–2,0 M token, 22–78 dk; KT-003 22 Tem'de açıldı, 2 Eyl'de hâlâ açıktı (G-01…G-29; tek bir ürün sorusu — kart alt-toplamı neyi sayar — G-21'den G-29'a kadar yeni görevler doğurdu). `KUTU.md` 54,5 KB (tavan 10), `OLCUTLER.md` 79 KB (tavan 12), açılış seti 86,9 KB (tavan 50). → Süreç ağırlığını işe orantıla; tavan aşımı yeniden yapılandırmayı tetiklesin.
7. **Jargon Batu dili kuralını yendi:** PANO yargı bloğu: "MÜHÜR: 2. (son) şık ATEŞLEDİ — ÖLÇTÜM, söz DÜŞMEDİ, tetik TÜKENDİ, Ç-NN doğmadı". Sade özet yalnız sorulunca geldi (ve iyiydi). → Batu'ya giden yüzeyi ayrı, kısa, şablonlu tut; mekanik kontrol et.
8. **Gizli hafıza drift kaynağıydı:** eski rollerin `~/.claude/projects` altında 10 gizli hafıza deposu (~700 KB). Yeni düzende `autoMemoryEnabled: false`; hafıza = görünür dosyalar. → Al.
9. **Canlı oturumlar-arası mesajlaşma kötü çalıştı:** her gönderim Batu onayı ister, bypass modda kapalı; Code↔Tester döngüsü ("Siz bir döngüye girdiniz, sizi çıkardım"). Koordinasyon "yapı üzerinden" aktı: commit'li ref + dosya + açılışta "çek+atıfla". → Al (dosya/commit üzerinden koordinasyon).
10. **Batu konumu (027 → D1/D2):** kalite yapıda, uzmanlık rolde, yalnız gerçek çatal (üç şart) Batu'ya; sahte menü yasak. Retrolarda Batu sahte menü görmediğini, jargonlu soru gelmediğini söyledi (öz-bildirim). → Al (K-015 ile birebir uyumlu).
11. **Aşırı yapı hastalığı tekrarladı:** `architect/meta-os` (hash zincirli journal, HALT, 4 aktör) yalnız 1 olay (genesis, 1 Tem 19:07Z) kaydetti; KT-000/G-01'de (2 Tem) CLAUDE.md'si arşiv işaretçisiyle değiştirildi; 150 KB'lık "Hizalama Öğretici" kendi §10.6'sında "Aşırı yapı da bir hastalıktır" diyor. → Alma; yapıyı işi yaparken, küçük kur.
12. **Mac'e bağlı parçalar alınamaz:** `/Users/Batu/...` mutlak yolları, kullanıcı kapsamlı (`~/.claude`) `SessionEnd` hook'u, `127.0.0.1:4173` yerel kokpit, `.command` başlatıcı, uzak depo olmayan vault, üç ayrı kök (vault + kod + pano) ve Testçi worktree'si. → Bulutta tek repo, göreli yol, proje `.claude/settings.json` (tek repolu oturumda hook ve izinler yükleniyor — brief), dal+push, repo içi durum sayfası.

## Kapsam

**Harita:** 2.400 dosya / ~114 MB. `_makine` 526 dosya 76 MB (tutanaklar 367), `kanon` 331 / 16 MB, `arsiv` 1.233 / 17,8 MB, `pano` 40, `architect` 25, `kod` 237. Klon sığ (tek commit); README'nin "233 commit" dediği kanon geçmişi ve commit mesajları **okunamadı (bilinmiyor)**.

**Tam okunan:** `README.md`, `.gitignore`; `kanon/EL_KITABI.md`, `kanon/CLAUDE.md`, `kanon/.claude/settings.json`, `00_pano/*` (5 dosya), `03_roller/*/{CLAUDE,SOZLESME,DURUM}.md` (9 rol, 27 dosya); `01_kutular/_arsiv/KT-000-goc/` (KUTU + G-00.spec + G-01…06); `KT-002/gorevler/G-22.md` (retro); `KT-001/gorevler/G-41.md` (retro); `_makine/claude-config/*` (4), `_makine/denetim-araclari/*` (2); `pano/{README,PANO_SOZLESMESI}.md`, `kokpit.config.json`, `package.json`, `.claude/launch.json`; `architect/` küçük dosyaların tümü (CLAUDE, manifestler, journal, kernel CONSTITUTION/ROLES/AUTHORITY/DONE_CRITERIA/INVARIANTS, protocol AGENT_BOOTUP/TASK_LIFECYCLE/HANDOFF/SCRATCH/DECISION/REVIEW/PROJECTION); `arsiv/loopinance_setup/99_agent_exchange/org_redesign_2026-06-23/` 001, 002, 003, 005; `01 setup_decisions/027`; `04 K3 Installer Pack/01,02`; `03_Code Phase/CLAUDE_eski_arsiv.md`; `Loopinance_Root/.../08_Setup/CLAUDE.md`; `kod/` sürücü dosyaları (CLAUDE, eski talimatlar, README, package.json, eslint/playwright/vitest tester configleri, `tests/tester/README.md`); `_makine/tutanaklar` altındaki 11 `MEMORY.md` dizini + 19 tekil hafıza dosyası.

**Kısmen okunan:** `bekci.sh` (1.065 satır; başlık, `--hook`, §0–§16 başı, §17 sonu, SAGLIK/PANO yazıcıları; `--test` gövdesi okunmadı); `KT-003/KUTU.md` (başlıklar + satır 1–100), `OLCUTLER.md` (ilk 20 satır), `G-28.md` (ilk 25 satır), `KT-002/KUTU.md` (1–12, 126–200: kurulum kararları, retro girdileri, kapanış), `KT-001/KUTU.md` (baş + grep), `KARAR_INDEKSI.md` (ilk 25 satır); `_makine/is-akislari`: `koordinator--wf_6b585473.js` çoğu, 13 `.json` koşu kaydının özet/log/sonuç alanları (betik ile), setup wf'nin 49 maddelik sonucu; tutanaklar: 16 `.jsonl` betikle profillendi, 6'sının insan mesajları, 3'ünün son asistan metinleri okundu; `architect` JOURNAL/GENESIS/VIOLATION/AMENDMENT yalnız başlıklar; `pano/lib/status.mjs` grep, `pano-alanlari.txt` başı; `arsiv`: 004 başlıklar, `Hizalama_Ogretici.md` (150 KB) başlıklar + §9–§10, `arastirma_tamamlama_disiplini` §0/§4/§6, `eski_proje_planlama_...` başlıklar + Gözlem 1/7/24–27, `loopinance_gozlemci/{DURUM,ORYANTASYON}` baş.

**Okunmayan (gerekçe):** `kanon/02_kanon/**` (karar, domain, senaryo, tasarım — ürün içeriği, soru dışı), arşiv kutularının ~150 görev dosyası (format G-28/G-22/G-41 ile görüldü), diğer 11 workflow `.js`'i (desen aynı; özetleri okundu), `subagents/` iç dosyaları ve tam tutanaklar (1,4–2,9 MB), ~110 hafıza dosyası (dizin satırları okundu), `_makine/veri` (SQLite + audit jsonl), 73 setup handoff'u, setup kararları 001–026/028, Audit raporları 00–42, Chat/Cowork/Design faz arşivleri, `loopinance_project`, `_bundles` (git bundle), `kod/src` kaynak kodu (brief gereği yalnız yapı).

## Zaman çizelgesi (kaynak: README, KUTU başlıkları, tutanak zaman damgaları)

- **Dönem 0 — `loopinance_project`:** tek sohbet projesi, oturum 001–025+, "Knowledge Files + Project Instructions". Ders dosyası: `eski_proje_planlama_acisindan_gozlemler.md`.
- **Dönem 1 — "K3" (Haziran 2026):** faz klasörleri ayrı oturumlar: Chat/Planner, Cowork (spec), Code, Design, Bankacı; üstte Setup (K1), Audit (=santral), Gözlemci, Tester, Governance Sparring Partner. Chat closure s001–s057, Setup handoff 001–073, Audit raporu 00–42. V1 nakit çıktı (`8a3f4bd`), V2 banka/KMH inşa edildi (`4805590`, vitest 350/350, e2e 146/146). 30 Haz kriz; 1 Tem "defo mekanizmaları" workflow'u, Hizalama Öğretici, `meta-os` genesis.
- **Dönem 2 — `Loopinance-Project` / kanon (2 Tem →):** 9 rol, EL_KITABI, bekçi. KT-000 göç (2 Tem), KT-001 banka/KMH devri (2–10 Tem), KT-002 sağlamlaştırma (13–21 Tem, 43 görev), KT-003 kredi kartı KK-A (22 Tem →, açık). Son rol oturumları 10 Ağu; bekçi #713 2 Eyl; aynı gün inceleme deposuna taşındı ("Bu depo **çalışmayı sürdürmek için değil, incelenmek için** kuruldu").

## Mekanizmalar (Dönem 2 — gerçekten koşan düzen)

### M1 — Rol = açıldığın klasör
- **Sorun:** oturum hangi roldür; hafızasız ajan kimliğini nereden alır.
- **Nasıl:** `kanon/03_roller/<rol>/CLAUDE.md` 5 satır: "Bu klasörde açılan her oturum **Koordinatör** rolüdür. Açılış sırası (EL_KITABI §2): `../../EL_KITABI.md` → `SOZLESME.md` → `../../00_pano/PANO.md` → `DURUM.md` → aktif kutu ve atanmış görevin." Kök `CLAUDE.md`: "Bu kökte rolsüz açıldıysan salt-okunursun; Batu'ya tek cümleyle sor: "Hangi rol olarak açıldım?"" Kod deposunda açılan oturum Yazılımcı (`kod/CLAUDE.md`, 3 satır işaretçi; bekçi §9 >1 KB ise "yerel kural büyümesi" SARI). Rol klasörlerinde `.claude → ../../.claude` symlink (tek izin dosyası).
- **Kanıt:** gözledim — yazılımcı oturumu (10 Ağu) açılış setini okuyup "**Sıra bende değil.** … D1 gereği tek satır durum raporu bırakıp duruyorum" dedi. 27 Haz (Dönem 1) Batu yanlış çalışma dizininde açtı, CLAUDE.md yüklenmedi ("evet burada "Working directory" sanırım yanlış açmışım").
- **DevOS:** uyarlayarak al. Bulutta tek oturum/tek repo: rol kimliği alt ajan tanımına ya da görev paketine taşınır; "rolsüz = salt-okunur" guard'ı korunur; oturum başında cwd/talimat yüklendi mi kontrolü eklenir.

### M2 — Tek kural kaynağı + rol deltası
- **Nasıl:** "Bu dosya bu projedeki TEK kural kaynağıdır. Rol sözleşmeleri yalnız role özgü farkları taşır ve buradaki kurallara ID ile atıf yapar. Bu dosya ancak bir kutunun kapanış retrosunda, Batu onayıyla, aynı commit içinde değişir." SOZLESME bölümleri sabit: Motivasyon · Yazma yetkisi · Açılışta ek okumalar · İş akışı · Sınırlar · Kural atıfları. Bekçi §9c: EL_KITABI'nın son commit mesajı "retro"/"iskelet" içermiyorsa KIRMIZI; §17 sözleşmelerde kural kopyasını ölçer (son ölçüm "en uzun ortak-dizi 4 kelime").
- **Kanıt:** KT-001 retrosu 13, KT-002 retrosu 6+2 ders üretti; Batu onayıyla aynı commit'te EL_KITABI'ya işlendi (kaynak diyor: `a6938d6`, `fb9c213`). KT-000 retrosu EL_KITABI'nın "2 kez kapanış-dışı değişmiş, sessiz kalmış" olduğunu yakaladı → §9c eklendi.
- **DevOS:** al. Kural değişikliği yalnız retro + Batu onayı; ID'li kural (D1…, F1…) atıfla kısa sözleşme.

### M3 — Açılış seti ve kapanış adımları
- **Nasıl:** "**Açılış seti (≤50KB, sırayla):** EL_KITABI → kendi SOZLESME → PANO → kendi DURUM → aktif KUTU.md → atanmış görev dosyası. … **Append (sürekli büyüyen) dosya açılış setine giremez.**" Kapanış: "(1) görev dosyanı güncel duruma YENİDEN DERLE (F2), (2) kendi DURUM.md'ni yeniden yaz (≤2KB), (3) yalnız kendi dosyalarını git'e ekle ve commit et (Bölüm 7), (4) bekçi betiği koşar (hook)." Bekçi §2 bütçeyi ölçer (EL_KITABI + en büyük SOZLESME + PANO + en büyük DURUM + aktif KUTU + en büyük görev).
- **Kanıt:** DURUM dosyaları 1,6–2,0 KB tuttu (gözledim). Ama açılış bütçesi KT-002'de 50,8→54,6 KB, KT-003'te 86,9 KB (KIRMIZI) oldu; kural "Kırmızı yalnız KAPANIŞI kilitler, günlük işi değil" olduğu için büyüme durmadı.
- **DevOS:** al (bağlam %80'de sıkışıyor, küçük açılış seti şart); bütçe aşımı günlük işi de uyarmalı ve kutu/ölçüt dosyası bölünmeli.

### M4 — PANO: mekanik blok + yargı bloğu + "SIRADAKİ OTURUM"
- **Nasıl:** `00_pano/PANO.md` iki bölge: `## MEKANİK BLOK — yalnız bekci.sh yazar` (son koşu, ışıklar, görev durumları, bekleyen sorular, sayaçlar) ve `## YARGI BLOĞU — yazar: koordinator`. EL_KITABI §1: "`00_pano/PANO.md`'yi aç → "SIRADAKİ OTURUM: <rol>" satırını gör → o rolün klasöründe oturum aç → "devam" yaz. Hepsi bu." Batu'nun tek yazı alanı `BATU_NOTLARI.md` (PO her açılışta işler, siler).
- **Kanıt:** tutanaklarda açılışlar: "selam sıranı kontrol et ve sıradaki işe devam et.", "PO koştu, sıra sende.", "Tasarımcı koştu, sıra sende sanırım. nasıl ilerleyeceğiz?" (gözledim). Korunmuş kanon oturumlarının çoğunda 1–4 insan mesajı (Dönem 1'in korunmuş üç oturumunda 13, 23, 47; örneklem küçük). Ama Batu yine de soruyor: "Bitirdin mi bu oturumdaki işini? sıradaki oturum kim, koordinatör mü?"; "Paralel çalıştırabileceğim rol varsa…" (koordinatör bankacı+yazılımcı paralel önerdi; Batu "sadece bankacıyı çalıştırdım"). 10 Ağu Batu yazılımcıyı açtı, sıra bankacıdaydı; yazılımcı "bu oturumu kapat, `03_roller/bankaci` klasöründe yeni bir oturum aç" dedi.
- **DevOS:** fikri al (tek gündem, iki yazar bölgesi, sıradaki rol satırı); **röleyi alma**: sıradaki rolü orkestratör kendisi çağırır. Batu'ya dönük pano ayrı ve sade.

### M5 — Bekçi: `bekci.sh` + SAGLIK + SessionEnd hook
- **Sorun:** sağlığın beyana değil tekrarlanabilir betiğe dayanması; Batu'nun tek ezberi.
- **Nasıl:** `03_roller/bekci/bekci.sh` (bash + gömülü python, v1.1–1.4). Hook: `~/.claude/settings.json` → `"SessionEnd": … "command": "bash /Users/Batu/…/03_roller/bekci/bekci.sh --hook", "timeout": 30, "statusMessage": "Bekçi sağlık kontrolü koşuyor"`. `--hook` iki kök dışında sessiz çıkar ve sonda `if [ "$HOOK_MODE" = "1" ]; then exit 0; fi`. Kontroller: tavanlar, açılış bütçesi, bayt-ikiz, şema (F9), arşivde açık kalem, sahipsiz görev, spec tazeliği (`kaynak: K-NN @ sha256:`), ikinci kök, kod işaretçisi, "done ama iz boş" (<40 karakter), EL_KITABI kapanış-dışı diff, kirli ağaç + yazar atfı, çapraz-repo golden baseline (sha256 sözlüğü betikte; "oto-güncelleme YOK — yoksa SARI bir sonraki koşuda kendini silerdi = fail-open"), durum sözlüğü, bekleyen soru, OS artefaktı, commit rol-damgası ↔ yazar-başlığı, F8 uyanma, kural kopyası. SAGLIK ve PANO bloğu `tempfile` + `os.replace` ile atomik. §0 koşu kilidi: "30 beklenen artışın 17'si kayıp" gözleminden sonra `flock`; "Kilit alınamazsa HİÇBİR ŞEY yazılmaz ve rc=2: SAGLIK damgası bayatlar = alarmın kendisi (fail-closed)."
- **Kanıt:** 2 Eyl koşu #713 (gözledim); KT-000 boyunca 9 koşu; `--test` 61/61 (bekçi DURUM). Denetçi retrosu (KT-002): "Sayaç ~215 koşu ima, 13 git-çapalı (~%6; session-close modeli, KT-001 ~%12)". Işık satırı kodu: `DAVRANIŞ=VERİ-YOK` sabit metin — hiç hesaplanmadı (gözledim). Kokpit sözleşmesi: 2026-08-05 ölçümünde "dört bozmada **sıfır uyarı + YEŞİL**" → sonra 17/17 test.
- **DevOS:** al (en taşınabilir parça). Uyarla: hook kullanıcı ayarından proje `.claude/settings.json`'a taşınabilir; ama boşta kalan ya da süresi dolan VM'de SessionEnd'in koşacağı bilinmiyor (çalışan shell işleri geri gelmiyor — brief) → bekçi kapanış adımında senkron koşsun, çıktı commit+push edilsin, CI'da da koşsun; ölçülmeyen boyutu ışık gibi gösterme.

### M6 — Kutu (KT) yaşam döngüsü
- **Nasıl (EL_KITABI §3):** Fikir Batu→PO→`HARITA.md` adayı → **görüş turu** ("Koordinatör ilgili rollere … birer görüş görevi açar; her rol ≤1 sayfa değerlendirmesini KENDİ görev dosyasına yazar … Görüş görevleri kapanmadan kutu AÇILAMAZ") → kurulum (Koordinatör görev + kabul ölçütlerini **işten önce** `OLCUTLER.md`'ye yazar; Analist spec'leri yazar, "açılış mühründe spec'ler DONAR") → KUTU.md'de "**Bu kutu bitince gözünle göreceklerin** — 3 somut, gözlemlenebilir iddia, Batu-dilinde" → Batu açılış mührü → yürütme → kapanış ritüeli a–h (bekçi senkron, "taze SAGLIK yok/hata → kapanış YOK (fail-closed)"; ölçüt + bağımsız doğrulama; açık kalem süpürme; demo + Batu mührü + 2 soru "sahte menü gördün mü? / jargonlu soru geldi mi?"; Denetçi retrosu 5 soru; el kitabı düzeltmesi; arşiv; uyanma taraması).
- **Kanıt:** KT-000/001/002 bu ritüelle kapandı (gözledim KUTU durum satırları). İyi örnek: KT-003 "gözünle göreceklerin" 3. madde "…faiz alanında sayı yerine «rotatif faiz sonraki kutuda (KK-B)» diyen dürüst bir boşluk göreceksin. Yanlış sayı yerine dürüst boşluk." Kötü: KT-003 29 göreve çıktı; 22 Tem'den 2 Eyl'e kadar kapanmadı.
- **DevOS:** al (mühür + önceden ölçüt + retro). Uyarla: kutu küçük tutulsun (kendi retro adayları "küçük kutu > dev"); görüş turu yalnız risk varsa.

### M7 — Görev dosyası, iskelet ve tek yazıcı
- **Nasıl:** `01_kutular/KT-NNN/gorevler/G-NN.md` (≤6 KB) başlık: `<!-- yazar: po (iskelet: koordinator) -->`, sonra `Sahip · Kutu · Kabul · Durum`. F3: "Her dosyanın başında yazıcı rolü yazar … başkası yazamaz." Koordinatör iskeleti açar, "atamayla dosya atanan role geçer". Durum sözlüğü kanonik (açık · yapıldı · kapalı · …). Rollerin birbirine sorusu: "soran görev dosyasında sahipli açık kalem"; bekçi `## Açık kalemler` altındaki numaralı satırlarda rol adını görürse PANO'ya "bekleyen soru" basar.
- **Kanıt:** KT-002 retrosu: "G-25 (testci) ve G-26 (yazilimci) … iskeletlerini hiç açmadım ⇒ hiç sevk edilmediler … ikisi de PANO'da hiç görünmedi … üç gün kimse koşmadı." Çare: "tablo satırı **iskeletsiz doğamaz**". `pano-alanlari.txt`: `Bekleyen sorular:` satırı sonradan "ÖLÜ DİZEYDİ" diye ölçüldü.
- **DevOS:** al (dosya başına tek yazar, iskelet+sahip). Görev kaydı makine-okur olsun (tablo ↔ dosya varlığı kontrolü).

### M8 — Geri akış L1/L2/L3
- **Nasıl:** "Yazılımcı'nın işaretleri: **L1** (kod-yerel) kendi çözer · **L2** (spec hatalı) → Analist'e spec-revizyon görevi · **L3** (karar hatalı) → PO'ya karar-revizyon görevi … yeni K-NN eskisini AŞAR ve `KARAR_INDEKSI`'nde eski satır aynı olayda "aşıldı → K-yeni" yapılır." Yazılımcı sözleşmesi: "**Boşlukta: işaretle ve DEVAM et.** … nötr yolda devam et"; bayrak sözdizimi `L2 açık` / `L2 tüketildi→G-NN`.
- **Kanıt:** yazılımcı DURUM: tasarım boşluklarını koda gömmedi, L3→PO/L2→tasarımcı kalemleri açtı (gözledim). Retro: L2/L3 "≥7-12 namespace'e aşırı-yüklü … regex 0 yakalar = **sessiz fail-open**" → kanonik sözdizimi.
- **DevOS:** al (Dönem 1'den beri, `ISARETLER.md` → görev dosyası). Bayrak sözdizimini baştan makine-okur tanımla.

### M9 — Davranış kuralları D1–D5, çatal kapısı, Ç-NN günlüğü
- **Nasıl:** D1 "Sıradaki halka senin elinde değilse tek satır durum raporu yaz ve dur; "ne yapayım? a/b/c" menüsü üretme." D2 "Net sıradaki adımı UYGULA … Batu'ya yalnız gerçek çatal gider (üçü birden: birden fazla meşru yön VAR + seçim araştırmayla değil Batu'nun vizyonuyla çözülür + rol/yapı kendi çözemez)." D3 Batu-dili + her çatal `Ç-NN` olarak KUTU'ya. D5 "Kendi işini kendin "bitti" ilan edemezsin." Kökeni `arsiv/loopinance_setup/01 setup_decisions/027`: Batu "beyin olmak yerine kas gücü oluyorum"; teşhis ""madde-madde onay" kontrol vermiyor, **kontrol tiyatrosu** yapıyor"; iş üçe: kalite→yapı, uzmanlık→rol, yön/değer→Batu.
- **Kanıt:** Denetçi retroları: D1 menü-grep 0 (68 commit + kutu); Batu "sahte menü = GÖRMEDİ · jargonlu soru = GELMEDİ" (öz-bildirim). Ç-05'te şekil kusuru: Batu "zaten benim karar verebileceğim bir uzmanlık değil bu aslında" → ders L-D7 "onay gerektiren ≠ karar gerektiren". Denetçinin önerdiği Batu spot-kontrolü "sunuldu-KULLANILMADI".
- **DevOS:** al. Mekanik sayaç ekle (DAVRANIŞ ışığı Loopinance'ta hiç dolmadı).

### M10 — Bağımsız doğrulama zinciri
- **Nasıl:** EL_KITABI §7 "**Yeşil ref** = tüm kapı sayıları (tip 0 · lint 0 · birim yeşil; kutu kapanışında + e2e) sağlanmış commit'in kimliği. Doğrulama daima yeşil ref'e, doğrulayanın kendi koşumuyla yapılır — çalışan ağaca değil." Testçi: ayrı worktree, çitli alan `tests/tester/`, commit etmez. `kod/playwright.tester.config.ts`: port 3200, ayrı DB, `NEXT_DISTDIR=.next-tester`, `APP_NOW=2026-06-18 APP_NOW_FORCE=1 E2E_SEED=1`, `workers: 1`. `kod/eslint.tester.config.mjs`: `no-restricted-imports` `@/engine`, `@/domain` — "Golden test @/engine + @/domain import EDEMEZ — beklenen değer motordan türetilemez; karar-kaynaklı literal kullan (// oracle: GS-NN / K-NN)." Denetçi: "beklenen değeri ilgili karardan … KENDİN hesapla; ancak ondan sonra mevcut golden'la karşılaştır"; retro 5 soru + en az bir "bitti"nin yeniden türetilmesi.
- **Kanıt:** Koordinatör sözleşmesi: "350 yeşil testin arkasında hiç inşa edilmemiş bir motor yakalandı" (Dönem 1 s057: "gecikme dual-bucket motorunun HİÇ kurulmadığını"). KT-001 kutu hedefi: "'çalışıyor' sözü ilk kez üç bağımsız gözle … mühürlenmiş olacak; bugüne dek yeşil raporlar işi yapanın kendi beyanıydı." Retro örneklemeleri kuruşu kuruşuna (golden-09 Ocak "2.075,18 EXACT"). Açık kalan: KT-001 retro RF-2 kod deposundaki `@golden-source … sha256` pinleri bayat, bekçi görmüyor.
- **DevOS:** al (üreten ≠ doğrulayan, commit'li ref, oracle karardan, lint ile zorlama).

### M11 — Çekişmeli çok-ajanlı doğrulama workflow'ları
- **Nasıl:** rol oturumu içinden Workflow betiği (`_makine/is-akislari/*.js`): `phase('Olgu')` paralel doğrulayıcılar JSON şemasıyla (`DOGRULANDI|KISMEN|YANLIS|BULUNAMADI`), `phase('Çürüt')` çürütücüler (`KAPI_DUSER|SART_EKLENIR|NOT_DUSULUR|ETKI_YOK`, `effort: 'high'`), `phase('Sentez')` tamlık eleştirmeni (`ACILABILIR|SARTLI_ACILABILIR|ACILAMAZ`). Ortak istem: "SEN BİR DOĞRULAYICISIN. Kural: BEYANA GÜVEN YOK (D5). … SATIRI ALINTILA (dosya:satır) … HİÇBİR DOSYAYA YAZMA."
- **Kanıt (json kayıtları, gözledim):** analist g26 9 ajan 32 dk 1,20 M token; koordinatör g26-g23 10 ajan 1,49 M; PO g28 12 ajan 78 dk 2,05 M; tasarımcı g21 12 ajan 47 dk 1,72 M. İşe yaradı: PO "8 çürütücünün 8'i de gerekçeye vurdu ve HAKLIYDI"; analist "İki ara-hükmüm de çürütüldü, geri çektim". Arızalar: "[sentez:tamlik] failed: API Error: Unable to connect to API (ECONNRESET)" (koordinatör: "bağımsız tamlık merceği YOK"), "agent … stalled (no progress) after 405s — retrying (1/5)", "[tamlik-elestirmeni] failed: You've hit your session limit".
- **DevOS:** uyarlayarak al: yalnız yüksek riskli karar/kapıda, bütçe tavanıyla; önce deterministik kontrol. Bulutta alt ajan kendi alt ajanını açamıyor → fan-out orkestratörden yapılmalı. VM süresi dolunca çalışan alt ajanlar geri gelmiyor (brief) → 30–78 dk'lık tek parça koşular yerine kısa dalgalar, her ajanın sonucu hemen dosyaya. (Workflow aracının bulutta varlığı: bilinmiyor → O11.)

### M12 — Dosya disiplini F1–F10 ve ERTELENENLER
- **Nasıl:** F1 tek ev + işaretçi (+sha256), kopya yasak; F2 "Durum taşıyan dosya güncellemede güncel hale DERLENİR … "BAYAT/DÜZELTME katmanı" eklemek yasak"; F6 olay bir kez yazılır; F8 "Erteleme = sahip + uyanma koşulu"; F9 şema dışı = kırmızı, "`gecmis/` gibi arşiv klasörü YOK — tarih git'te"; F10 spec başlığı `kaynak: K-NN @ sha256`. Tavan tablosu §6 (EL_KITABI 13/18 KB, PANO/DURUM 2/3, KUTU 10/15, G-NN 6/9, spec/OLCUTLER 12/18, kanon 64/96, açılış 50). `ERTELENENLER.md` tablosu: `ID | Kalem | Sahip | Uyanma | Kaynak`.
- **Kanıt:** F2 + DURUM ≤2 KB tuttu. Ama: KUTU/OLCUTLER tavanın 5–7 katı; ERTELENENLER'de 31 açık satır (ERT-01…ERT-37); bekçi "30 ertelemenin uyanma koşulu makine-değerlendirilemez". Satır-no işaretçileri: "id 3/3 yaşadı, satır-no 3/3 öldü". Dönemler arası kayıp: `eski_proje…` Gözlem 27'de "BSMV+KKDF oranında tutarsızlık fark edildi (%30 vs muhtemelen %20). "Spec aşamasında netleşecek" notu düşüldü ve geçildi." — Eylül'de hâlâ ERT-31 "KK zemin vergi %20→%30" açık (çıkarım: aynı kalem).
- **DevOS:** al (tek ev, derle-değil-ekle, sahip+uyanma). Uyarla: işaretçi içerik/ID ile; uyanma koşulu makine-okur (olay adı/kutu kimliği).

### M13 — İzinler, hafıza ve git disiplini
- **Nasıl:** `kanon/.claude/settings.json` allow: Read/Edit/Write/Glob/Grep, `git status/add/commit/log/diff/show`, `shasum`, bekçi; ask: `Edit(02_kanon/senaryolar/golden/**)`; deny: `git add -A`, `git add .`, `git push`, `rm -rf`; `"autoMemoryEnabled": false`. Kod deposu ayrıca `git worktree`, `npm run`, `npx tsc/eslint/playwright/vitest`. `kanon-git-info-exclude.txt`: `**/.claude/scheduled_tasks.lock`, `**/.claude/routines/.state/`, `**/.claude/worktrees/`, `**/.claude/mailbox/`… Commit: "`git add <açık yol>` + `git commit -- <açık yol>` … index paylaşımlıdır"; mesaj `<rol>: <G-NN|K-NNN> — <tek satır>`; "Batu asla git komutu koşmaz."
- **Kanıt:** G-06: "eski rollerin ~/.claude/projects altında 10 gizli hafıza deposu var (~700KB …)" → "yeni oturumlar gizli hafıza YAZAMAZ/OKUYAMAZ; rolün hafızası = vault'taki DURUM + görev dosyaları (Batu'nun görebildiği yüzeyler)." B4: "testçi §7'yi **harfiyen** uyguladı ve yine de 11 yabancı dosya commit'ledi"; deny listesi "çıplak `git commit`'i engellemiyor". Bekçi §15 bunu artık KIRMIZI yapar.
- **DevOS:** al (proje `.claude/settings.json`, auto memory kapalı ya da denetimli, dar commit). Bulutta tek yazıcı/tek oturum olursa index çakışması azalır; dal+push zorunlu, vault'taki "uzak sunucu yok" bulutta geçersiz. Kullanıcı ayarındaki 22 plugin (superpowers, context7, hookify, ralph-loop…) repoya `enabledPlugins` yazılarak taşınmaz (brief: marketplace kurmuyor; hesap plugin'i senkronlanıyor); kanon düzeni bunlara dayanmadığı için kayıp yok.

### M14 — Kokpit (`pano/`)
- **Nasıl:** bağımlılıksız Node sunucu, `127.0.0.1:4173`, 15 sn tazeleme, "**Hiçbir şey yazmaz.**"; tazelik: bekçi bir gündür koşmadıysa kırmızı; "sıradaki bayatlığı": SIRADAKİ rolün `DURUM.md` mtime'ı koordinatörünkinden yeniyse "koordinatör sevki bekleniyor". Söz dizimi `PANO_SOZLESMESI.md` + `pano-alanlari.txt` (tek ev; aynı liste önce "ÜÇ evde elle yazılıydı ve üçü de ayrışmıştı"). 2026-07-04'ten beri kod KEEL'in `keel/tools/kokpit/` kopyasıyla aynı (O3 bağlantısı).
- **DevOS:** Mac'e bağlı (yerel sunucu, `.command`) → **alma**; fikri al: repo içinde üretilen tek sayfalık durum + tazelik + "sevk bekleniyor" uyarısı.

## Dönem 1'den (K3) mekanizmalar — kısa

- **Oturumlar-arası mesaj:** `mcp__ccd_session_mgmt__send_message`; hafıza notu: "gönderim **her seferinde Batu onayı** ister, bypass modda **tamamen kapalı**; (2) hedef oturum **kapalıysa** mesaj açılışta düşer; (3) başka oturum transkripti onaysız diskten **okunabilir**." Otomatik mod sınıflandırıcısı rol-dışı yazımı reddetti: "cross-session mesaj doğrudan kullanıcı niyeti sayılmaz". Batu gereksiz durum mesajlarını iptal etti. → **Alma** (canlı döngü); dosya/commit kanalı al.
- **Santral:** 14 Haz paralel rol oturumları "koordinasyon bozuldu" → Audit santral oldu; "Code ve Audit AYNI uygulamayı çalıştırır (aynı kod, aynı test portu **3100**, aynı test DB). **İkisi aynı anda test/build koşamaz**". Çözüm Testçi için ayrı port/distDir (PA-07). → Paylaşılan kaynak = sıralı, ayrıştırılabiliyorsa ayır.
- **Gözlemci panosu:** 4 soru (Neredeyiz / Sıra kimde / Senden gereken / Kim nerede) ~12–15 satır; ilk ~50 satırlık pano "laf salatası" diye geri döndü; `_durum.md` satırını rol "**ancak TAZE oturumda** yazar" → 5 rolden 4'ünün dosyası boş; son oturum mesajı jsonl'dan okundu. → Batu yüzeyi için bu 4 soruluk biçim iyi.
- **Oturum açılış/kapanış (K3 Installer):** tek tetik "Session başlat"; açılış: son closure → task_tracking → agenda → open_questions; kapanışta `session_NNN_closure.md` (ne+neden, kilitlenen/açık, hissiyat, "**TEK** adım" sonraki gündem). Risk kendisi yazmış: "Closure dosyaları oturum sayısıyla doğrusal birikir". Dönem 2 bunu `DURUM.md` yerinde yeniden yazımıyla değiştirdi.
- **Standby disiplini (019–025) + 027:** boştayken tek satır olay-bekleme, aktifken net adımı uygula. Dönem 2'de D1/D2 oldu.
- **Auto memory:** her faz klasörünün `memory/MEMORY.md` + konu dosyaları (dizinler okundu); değerli dersler içeriyor ama Batu göremedi ("neden başka bir ortamda başka bir dosya tutuyorsun?") → Dönem 2'de kapatıldı.

## `kod/` — kodu süren düzen (yalnız yapı)

Next.js 16 + React 19 + Drizzle/libSQL; `src/{app,components/silent,db,domain,engine,lib}`; `tests/unit` 43, `tests/e2e` 20 dosya; `tests/tester/` yalnız README (fence testleri Testçi worktree'sinde, commit'lenmedi — Testçi DURUM "kod-deposuna commit ATMADIM"). Scriptler: `test`, `test:e2e`, `typecheck`, `test:tester`, `test:tester:e2e`, `test:tester:types`, `test:tester:lint`. Kapı sayıları görev dosyasına yazılır (Yazılımcı DURUM: "tsc 0 · lint 0 · vitest 503/503 · tester types/lint 0 · fence e2e 25 passed / 4 skipped", yeşil ref `f36210f`). Testçi kancaları: donmuş saat (`APP_NOW`, globalThis), `POST /api/test-seed` "YALNIZ ham girdi", `<Amount data-value>` "GÖZLENEN çıktıdır … ORACLE DEĞİL". Tuzak notları hafızada: node@22 bozuk → node@20; `run_in_background` dev sunucusunu öldürüyor; mutasyon yapan doğrulama ajanları paylaşılan ağacı bozdu ("Never trust an agent's 'I restored it.'") → `isolation: 'worktree'`.

## Ne işe yaradı (kanıtlı)

- Ürün ilerledi: V1 nakit, V2 banka/KMH (KT-001 kapandı), KT-002 43 görev, KK-A motoru yeşil ref'te (kaynak diyor, DURUM/KUTU).
- Kural dışı davranış azaldı: D1 uyumlu cevaplar ("Koordinatör olarak **beklemedeyim (D1)** — uydurulacak koordinatör işi yok."), retrolarda menü/jargon 0 (öz-bildirim + grep).
- Retro → kural evrimi çalıştı: her kutu sonunda ders listesi → Batu onayı → aynı commit (13 + 8 madde).
- Deterministik kontroller gerçek bozulmaları yakaladı: rol-damgası süpürmesi, golden drift, spec bayatlığı, "done ama iz boş".
- Doğrulama "yeşil rapor"un arkasındaki eksikleri buldu (motor yok, kapanış eksikleri, yanlış hükümler).
- İstenince sade durum anlatımı iyiydi: "motor hazır, kaporta eksik"; "**"o toplam neyi saymalı?"** sorusunun cevabı yazılı kurallarımızda çelişkili çıktı … Bu bir kod hatası değil, cevaplanmamış bir ürün sorusu." (koordinatör, 10 Ağu).

## Ne yaramadı (kanıtlı)

- **Röle/sevk insanda:** Batu sıradaki rolü açmak, "sıra sende" yazmak, bitiş/sıradaki sorularını sormak zorunda kaldı; yanlış rol açıldı; seri akışta ok bekletmesi 5 gün.
- **Ağırlık:** kapı teyidi başına ~1–2 M token; tek ürün sorusu (kart alt-toplamının popülasyonu) G-21, G-24, G-26, G-27, G-28, G-29'u doğurdu, Ağustos'un ilk yarısını yedi ve kutu kapanmadı; kutu, ölçüt ve açılış dosyaları tavanın çok üstünde; "ölçüt yazdıkça bütçe taşıyor ⇒ mekanizma kendi kendini besliyor" (koordinatör, KT-002).
- **Dil:** yargı bloğu ve DURUM'lar yoğun kısaltma/jargon (D3'e rağmen).
- **Hook ve ölçüm boşlukları:** danışman hook, düşük commit oranı, hiç dolmayan DAVRANIŞ ışığı, bekçinin görmediği kod-deposu pinleri, "30 ertelemenin uyanma koşulu makine-değerlendirilemez".
- **Bitmedi:** KT-003 açık kaldı; son rol oturumları 10 Ağu; 2 Eyl'de proje inceleme arşivine dönüştü (çıkarım: durdu).
- **Dönem 1'de:** 30 Haz krizi — "jöle gibisin, sabit bir disiplinin yok. dağılıyorsun odağını kaybediyorsun"; "ben sorunca bu değerlendirmeyi yapabiliyorsun da işi yaparken neden bu değerlendirmeyi yapmıyorsun"; 1 Tem Batu'nun kendi teşhisi: "sana ben yaptırmaya çalıştım, sen de önünde bir plan olmadığı için "bitti" tanımını göremedin".

## Dersler (kök neden → önlem → kaynak)

1. **İnsan röle darboğazı.** Kök: roller ayrı insan-açılışlı oturumlar, otomatik sevk yok. Önlem: tek orkestratör oturumu sevk eder, alt ajanlar rol yürütür; Batu yalnız çatal/mühür. (PANO, tutanaklar 9–10 Ağu, KT-002 "Sıra-kapısı dersi")
2. **Mekanizmasız kural fail-open'dır.** Kök: kural "doğru şeyi yap" diyor, aracı vermiyor. Önlem: kural yazılırken mekanik kontrolü de yazılır. ("*disipline bırakılan her kural, mekanizma verilmedikçe fail-open'dır*", KT-002 retro; B4, ERT-14, görünmez iş)
3. **Tavan kırmızısı büyümeyi durdurmadı.** Kök: kırmızı yalnız kapanışı kilitliyor; kanıt silinemiyor (F2); ölçütler kutu dosyasında. Önlem: tavan aşımı hemen bölme görevi doğursun; kanıt katmanı ayrı, açılış setine girmeyen dosyada. (SAGLIK, Ç-05)
4. **Konum-adresli işaretçi çürür.** Önlem: madde-ID/başlık/içerik ile çapa; satır no yalnız aynı commit içinde ölçülerek. (KT-002 retro)
5. **Yeşil test ≠ var olan mekanizma; LLM denetimi de kusurlu.** Önlem: deterministik kontrol önce (sha/diff/lint/test), çekişmeli LLM denetimi sonra ve bütçeli; doğrulayıcının "uydurma açık madde" de üretebileceğini bil. (Koordinatör SOZLESME; `arastirma_tamamlama_disiplini` §6.7)
6. **Oturumlar-arası "bitti" aşırı-güveni.** Kök: taze ajan durum dosyasındaki ilerlemeye güvenir. Önlem: durum dosyası ne iddia edebileceğiyle sınırlı; "bitti"yi doğrulayıcı kanıttan yeniden türetir; açılışta git HEAD/iş gerçekten var mı kontrolü. (araştırma §0; hafıza "cold-start-direktif-zaten-yapilmis-olabilir"; Gözlem 24 "Kompakt özeti dosya gerçeğinin yerini tutmaz")
7. **Gizli hafıza ve yanlış çalışma dizini.** Önlem: hafıza repo içinde, görünür, kısa; oturum başında talimat/cwd doğrulaması. (G-06; 27 Haz tutanağı)
8. **Paralel ajanların paylaşılan kaynağı.** Sayaç yarışı (17/30 kayıp), paylaşılan git index, aynı port/DB/`.next` kilidi, mutasyon ajanlarının ağacı bozması. Önlem: kilit, dar commit, ayrı port/distDir/DB, worktree izolasyonu, kapıyı orkestratör sıralı koşar. (bekci §0/§15; hafıza "paralel-reskin-orkestrasyon")
9. **Aşırı yapı / süreç tiyatrosu.** meta-os tek olayla öldü; öğretici 150 KB; KT-003 bürokrasisi. Önlem: yapı işin büyüklüğüyle orantılı; "Metodoloji yapmaktan doğar". (architect/journal; Hizalama §10.6; 08_Setup CLAUDE.md)
10. **Batu'ya giden metin kaydı.** Kök: rollerin iç dili panoya sızıyor. Önlem: Batu yüzeyi 4 soruluk sabit şablon; teknik ayrıntı ayrı dosyada. (Gözlemci hafızası; PANO yargı bloğu)
11. **Ertelenen kalem sistem değişikliklerinde kaybolur ya da sürünür.** Önlem: ertelemeler tek tabloda, sahip + makine-okur uyanma; yeni sisteme göçte ertelemeler de göçer. (Gözlem 27 ↔ ERT-31; hafıza "ai-org-erteleme-degil-encode": "her oturum sıfırdan; ertelenen = görünmez = yok")
12. **Metodolojiyi ajana müzakereyle kurdurmak yordu.** Kök: plan/bitti tanımı yokken ajan kendi çalışma sistemini turn-by-turn kurmaya çalıştı. Önlem: DevOS dosya + mekanizma olarak kurulsun, küçük dilimlerle ve önceden yazılmış kabul ölçütüyle. (30 Haz–1 Tem tutanağı; org_redesign 002: "koordinasyon + governance KÂĞITTA tasarlı … ama **SAHİBİ atanmamış**")

## DevOS için al / uyarla / alma — özet tablo

| Mekanizma | Karar | Gerekçe |
|---|---|---|
| Tek kural kaynağı + ID'li kısa rol sözleşmeleri | Al | kanıtlı çalıştı, plugin gerektirmez |
| DURUM ≤2 KB yerinde yeniden yazım, tarih git'te | Al | açılış bütçesi ve bağlam sıkışması için |
| Rol = klasör | Uyarla | bulutta rol = alt ajan/görev paketi; rolsüz salt-okunur guard kalsın |
| PANO iki bölge + SIRADAKİ | Uyarla | sevki orkestratör yapsın; Batu yüzeyi ayrı ve sade |
| Bekçi betiği + tazelik + kilit + `--test` | Al/uyarla | kapanış adımında senkron + CI; SessionEnd'e güvenme |
| Kutu: önceden ölçüt, mühür, retro, EL_KITABI yalnız retroda | Al | kural evrimi kanıtlı |
| Görüş turu | Uyarla | yalnız riskli/yeni alanlarda |
| L1/L2/L3 + görev dosyasında açık kalem | Al | makine-okur sözdizimiyle |
| D1–D5, çatal testi, Ç-NN | Al | K-015 ile uyumlu; davranış sayacı ekle |
| Yeşil ref, Testçi çiti, oracle karardan, import-ban lint | Al | en sağlam doğrulama parçası |
| Çekişmeli çok-ajanlı workflow | Uyarla | pahalı ve kırılgan; bütçe + deterministik önce; fan-out orkestratörden |
| autoMemory kapalı, izin allow/ask/deny | Al | drift kanıtlı |
| Dar add + dar commit | Al | B4 kanıtlı |
| Kokpit (yerel Node) | Alma | Mac'e bağlı; repo içi sayfa ile değiştir |
| Canlı oturumlar-arası mesaj | Alma | onay kapısı, döngü riski |
| meta-os journal/HALT | Alma | hiç kullanılmadı |

## Açık / bilinmeyen

- Commit geçmişi (kanon 233, kod 81, pano 20 commit) bu klonda yok; commit mesajı disiplini ve bekçi damgalarının gerçek dağılımı doğrudan doğrulanamadı.
- KT-003'ün neden 10 Ağu'dan sonra durduğu dosyalarda yazmıyor (çıkarım: bürokrasi + Batu'nun yeni yöne geçişi; kanıt yok).
- Workflow (`phase/agent/parallel`) aracının Claude Code bulutunda aynen kullanılabilirliği: bilinmiyor (O11'e).
- Kokpit/KEEL ilişkisinin ayrıntısı O3'te.
