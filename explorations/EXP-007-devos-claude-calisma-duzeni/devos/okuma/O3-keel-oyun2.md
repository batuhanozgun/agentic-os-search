# O3 — keel ve oyun2: tasarım, kullanım, neden yetmedi

Okuyan: O3 · EXP-007 DevOS okuma turu · 2026-09-27.
Kaynaklar (salt okunur): `/home/user/batuhanozgun/keel` (tek commit `669c544`, "v0.2 — yayin", 2026-08-12) ve `/home/user/batuhanozgun/oyun2` (tek commit `d91cf22`, "Batu github'a göndermek için yaptı", 2026-08-14).
Kanıt dili: **kaynak diyor** (dosya böyle yazıyor) · **gözledim** (kendim okudum, saydım ya da koştum) · **çıkarım** · **bilinmiyor**.

## DevOS için en önemli çıkarımlar

1. **keel, oyun2'de ilk kutuyu bile kapatamadı.** Kurulumdan sonra 4 otonom dönem koştu. Üç dönem "duran kapı" ile durdu. Ürün kodu yok. `BITTI_TANIMI.md` ile `KUTU_PLANI.md` iskelet kaldı. İlk kutunun tek işi "projeyi nasıl yürüteceğimizi çıkarmak"tı (gözledim: `oyun2/00_pano/zarf-gunlugu.jsonl`, `02_kanon/`).
2. **Kök neden: güvence makinesi işin kendisinden ağırdı ve parçaları gerçek koşuda birbirine uymadı.** Ölçü (gözledim): kural ve kalıp metni ~176 KB, araç kodu ~760 KB, test ~1 MB. Ekibin bütün çıktısı 32 KB görüş ve toplama metni. Kurulumu ya da dönemi durduran her kusur ilk kez canlı koşuda görüldü. Hepsi iki parçanın birleşim yerindeydi: G4.5 kapısında SIGPIPE, zarf günlüğünün "kirlilik" sayılması, görev satırını kapatacak kimsenin olmaması, dairesel önkoşul, "30 ≠ 27" sayım farkı. K-12, K-13 ve K-14 korumalı ([SERT]) koda sahip onaylı yama istedi; Ç-05 kutu tablosunda elle onarıldı.
3. **Birim testlerin yeşil olması sistemin çalıştığını göstermedi.** SURUM "1202 test yeşil" diyor. Sayıyı doğruladım: bu konteynerde 1202 test var, 22'si kırmızı. Adlarına ve hata metinlerine bakılırsa kırmızılar ortamdan geliyor: root, Mac aracı yok (çıkarım). Ama G4.5 kapısının kusurunu hiçbir test yakalamamıştı; test "sahte bekçiyi TEK dosyayla kuruyor"du (kaynak diyor). **DevOS'un kabul kanıtı test sayısı değil, uçtan uca gerçek bir işin geçişi olmalı.** Bir görev açılır, yapılır, doğrulanır, kapanır.
4. **Otonom kip ve izleme ekranı Mac'e bağlıydı.** Watchdog `launchctl` ile, e-posta parolası Keychain'de (`security`), uyanık tutma `caffeinate` ile, kokpit `127.0.0.1` üzerinde ve `Kokpit.command` ile. oyun2 `/Users/Batu/Batu-Vault/oyun2` içinde koştu (gözledim: zarf gövdeleri). Bulut DevOS'ta bunların hiçbiri alınmaz.
5. **İnsan her halkadaydı.** Rol oturumunu insan açar (`/rol-<slug>`, `disable-model-invocation: true`). Dönemi insan açar (`/donem`). Her duran kapıyı insan çözer ("sevk gorevi kendi acamaz (v1 sinir)"). `git push`, `gh` ve `curl` onay ister. oyun2'de korumalı betiklere yapılan her yamaya sahip onayı alındı. Bu, Batu'ya yaslanmayı yapının parçası yapar. **DevOS'ta tetik ve toparlanma sistemin içinde olmalı. Batu yalnız amaç verir ve teslimatı kabul eder.**
6. **Uyarlayarak alınacak somut parçalar:**
   - (a) Tek bir makine-okur durum bloğu ve bir Stop kancası. Kanca bitmemiş adım varken oturumun kapanmasına izin vermez.
   - (b) Görev, taze bağlamlı bir alt ajan çağrısıdır. Alt ajan sabit alanlı bir dönüş zarfıyla döner. SubagentStop kancası zarfın biçimini denetler ve JSONL günlüğe ekler.
   - (c) "Kimse kendi işine yeşil diyemez": görevi yazma aracı olmayan doğrulayıcının karnesi kapatır.
   - (d) Kanıt-komutu kuralı: çıplak komut; boru, filtre ya da `|| true` yok.
   - (e) DEFO_MODELI'nin on defosu ve "iz ilkesi". Batu'nun U015 şikâyetleri bu listeyle örtüşüyor: karar-yükleme, öz-onaylama, şişme, örtme (çıkarım).
   - (f) Kapanış bloğu BİTEN · SENDE BEKLEYEN · SIRADAKİ ve maddeleri silinmeyen bir sahip kuyruğu.
   - (g) KAYIT_DUZENI tablosu: hangi bilgi hangi dosyada, yazarı kim.
7. **Alınmayacaklar:** GENESIS töreni (8 adım, mühürler), 11 koltuklu kadro, rol kafesi damgası, dönem/sevk makinesinin tamamı (1.094 satırlık `sevk.sh`), e-posta ve IMAP kanalı, watchdog, kokpit, bayt tavanları ve "marj freni", her kurala "Ders" ve hasım turu atfı (testler dahil 276 geçiş).
8. **Yapısal dersler:**
   - Her yerde fail-closed ve otomatik toparlanmanın olmaması, her anomalinin durmak olması demekti. DevOS'ta kademe gerekir: kendi onar, onarımı kaydet, yalnız belirli sınıflarda dur.
   - Doğrulayıcının "DOĞRULANAMADI" demesi döngüyü öldürmemeli. Düzeltme görevi, tavanlı olarak aynı role dönmeli.
   - Araştırma erişimi olmayan domain rolleri yalnız "BOŞLUK" üretti. DevOS rollerinin web ve araştırma erişimi baştan tanımlanmalı.
   - "Önce plan kutusu" 11 rolün paralel görüşüyle başladı ve orada durdu. İlk iş küçük ve somut bir teslim olmalı.

## 0 · Kapsam ve yöntem

**Harita (gözledim):**
- keel: 161 dosya, `.git` hariç 2,6 MB. oyun2: 244 dosya.
- oyun2'nin 143 dosyası keel ile bayt bayt aynı.
- Farklı olanlar: adım dosyalarının başlık yorumları, README, `bekci.conf`, `cekirdek.mjs`, `kurulum-denetimi.sh`, `kokpit.config.json`, `zarf-bicim-kapisi.sh`, `dogrulayici.md`.
- oyun2'ye özgü olanlar: `00_pano/`, `01_kutular/`, `02_kanon/`, `03_roller/`, `NASIL_KULLANILIR.md`, `.kurulum-tamam`, 11 alt ajan ve 11 rol becerisi.
- İki reponun git geçmişi yok; her biri tek commit. oyun2'nin özgün geçmişinde en az 31 HEAD kaydı vardı (`.git/logs/HEAD:31`, zarf #121). Bu geçmiş gönderilmemiş.

**Baştan sona okuduklarım:**
- keel:
  - `README.md`, `SURUM.md`, `CLAUDE.md`, `GENESIS.md`.
  - `00_genesis/` içindeki 14 dosya; `adimlar/` içindeki 8 adım ve `SIRA.txt`.
  - `docs/SOZLUK.md`.
  - `.claude/` tamamı: `settings.json`, 3 ajan, `donem` ve `hasim-inceleme` becerileri, README, `workflows/hasim-inceleme.js`.
  - Dört araç README'si, `PANO_SOZLESMESI.md`, `pano-alanlari.txt`, kokpit fixture'larının hepsi.
  - 11 veri dosyası (`korunan-yollar`, `disa-fiilleri`, `gorev-durumlari`, `zarf-jetonlari`, `bekci.conf` vb.) ve `.gitignore` listesi.
  - Betikler: `rol-ac.sh`, `bekci.sh`, `devir-kapisi.sh`, `acilis.sh`.
- oyun2:
  - `00_pano/` tamamı. `zarf-gunlugu.jsonl` içindeki 127 kaydın zarf dışındaki hepsi; 4 zarfın gövdesi ve kalan 7 zarfın alanları.
  - `01_kutular/KT-001-proje-plani/` tamamı.
  - `02_kanon/`: KADRO, VIZYON, KARAR_INDEKSI, KARAR_SABLONU, KARAR_ALANI, BITTI_TANIMI, KUTU_PLANI, README'ler, `.taban-ref`. EL_KITABI ile OTONOM_DONEM'i kalıba karşı diff'le.
  - Bütün DURUM, NOTLAR ve BRIFING dosyaları; `koordinator/ROL.md`.
  - `GENESIS_DURUM.md`, `.kurulum-tamam`, README, `NASIL_KULLANILIR.md` (kalıba diff).
  - keel'e karşı bütün diff'ler.

**Kısmen okuduklarım:**
- `sevk.sh`: 1.094 satırın yaklaşık 350'si. Kapılar, talimat üretici, görev seçimi, karar.
- `file-guard.sh`: başlık ve karar çıkışları. Yol çözümleyicinin içi okunmadı.
- `kurulum-surucu.sh`: çıkışlar ve durum makinesinin başı.
- `kurulum-denetimi.sh`: başlık, bölüm listesi, U5 yaması.
- `donem-ac.sh`: başlık ve 200–300. satırlar.
- `zarf-bicim-kapisi.sh`: başlık ve K-14 yaması.
- `kapanis.sh`: yalnız başlık. `cekirdek.mjs`: yalnız K-13 yaması.
- Kokpit: `status.mjs` tazelik bölümü, `server.mjs` başı, `Kokpit.command`.
- `watchdog-kur.sh`, `haber.sh`, `nabiz.sh`: yalnız Mac'e özgü satırlar (grep).
- oyun2'nin öbür 10 ROL.md'si: `pedagoji` kısmen; kalan 9'unda yalnız `Mod` ve yazma satırı. Hepsi aynı kalıptan geliyor.

**Okumadıklarım:**
- Test dosyalarının içi (~17.400 satır). Onları okumadım, koştum.
- Kokpit arayüzü: `app.js`, `style.css`, `markdown.mjs`, `tree.mjs`, `pano-alanlari.mjs`.
- 14 yardımcı dosya: `icerik-suzgeci.sh`, `klasor-hazirligi.sh`, `ortam-kontrol.sh`, `catal-kuyruk.sh`, `ortak.sh`, `zarf-ekle.sh` vb. Ayrıca `cekirdek.mjs` gövdesi.
- Gerekçe: sözleşmeleri README'lerde ve okuduğum betiklerde; bunlar uygulama ayrıntısı.

**Koşum (gözledim):** keel'in üç test kümesini scratchpad'deki bir kopyada, Node 22 ile, root olarak koştum.

| Küme | Test | Geçen | Kırmızı |
|---|---|---|---|
| `tools/guard` | 926 | 905 | 21 |
| `tools/bekci` | 141 | 140 | 1 |
| `tools/kokpit` | 135 | 134 | 0 (1 atlandı) |

- Toplam 1202, yani sayı SURUM'la aynı.
- Kırmızıların adları ve hata metinleri şu türlere düşüyor: "okunamayan/yazılamayan dosya" senaryoları (root her dosyayı okuyabilir), Mac araçları (`caffeinate`, Keychain), git'i PATH'ten gizleme. Çıkarım: keel'in hatası değil, testlerin Mac'e ve normal kullanıcı hesabına dayanması. Tek tek doğrulamadım.

## 1 · keel nedir, nereden geliyor

**Tanım (kaynak diyor, README):**
- keel "durumsuz yapay zekâ ajanlarıyla (Claude Code) bir yazılım projesini **sıfırdan kurup yürütmek** için bir *işletim disiplini* şablonudur".
- Felsefesi: "**bilerek az anla, çalışan bir sistem bırak.**"
- Nasıl başlar: klasör indirilir, Claude Code'da açılır, "selam" yazılır. GENESIS başlar, projeyi kurar ve çekilir.

**Kurulu projenin düzeni:** `00_pano/` pano · `01_kutular/` iş dilimleri · `02_kanon/` kararlar ve kurallar · `03_roller/<slug>/` rol evleri · `tools/` guard, bekci, sevk, kokpit · `.claude/` kancalar, ajanlar, beceriler.

**Kullanım geçmişi (kaynak diyor):**
- Bekçi README'si: "**altı gerçek kurulumda altı farklı bekçi** doğdu". oyun2'den önce en az 6 kurulum var.
- SOZLUK §3: "kokpit taşıyan beş kurulu proje".
- `MULAKAT_KALIBI.md`: "oyun kurulumunda kadro mührü tanıtımsız istendi". oyun2'den önce bir "oyun" kurulumu da var.
- Tarihler: defo araştırması 2026-07-01 · tatbikatlar 07-16 ve 07-19 · otonom kip E1–E5 07-27'den sonra · yayın v0.2 08-12.

**Batu'nun değerlendirmesi:** "senin daha önce yaptığın dandik keel var … keel ile yapmaya çalıştığımız oyun2 var" (`explorations/EXP-007-devos-claude-calisma-duzeni/sources/conversation/U015.md`).

keel kendi sınırını da yazıyor: deneme kurulumu "kurulumun kendisini" kanıtlamaz; "Gerçek bir projede uçtan uca kurulum ayrı bir kanıttır" (`SURUM.md`).

## 2 · keel'in mekanizmaları

Her mekanizma için: **sorun · nasıl işler · yol · kanıt · DevOS kararı**.

### M1 · GENESIS: sabit adımlar, makine-okur durum, Stop kancası sürücüsü

**Sorun:** Kurulum oturumlar arasında yarım kalıyor, adım atlanıyor.

**Nasıl işler:**
- İndeks: `GENESIS.md`. Her adım kendi dosyasında: `00_genesis/adimlar/G0…G5.md`.
- Sıra verisi `SIRA.txt`, TAB ile ayrılmış satırlar (`G0	G0.md	Seni tanıyorum: …`). Sıra dosyadaki satır sırasıdır, alfabetik değil.
- Durum yalnız tek bir blokta yazılır (`00_genesis/GENESIS_DURUM.md`):

  ```
  ## KURULUM DURUMU — makine okur (yazan: GENESIS ve kurulum sürücüsü)
  Adım: G5
  Durum: bitti
  Tamamlanan: G0, G1, G2, G3a, G3b, G4, G4.5
  ```

- Stop kancası `tools/guard/kurulum-surucu.sh` bu bloğu okur:
  - `açık`: `exit 2` ve stderr'de "KURULUM SIRASI — oturum kapanamaz".
  - `bekliyor`: kapanmaya izin verir. Gerekçe: "mühür anında sahibi bilgisayar başında tutmak … kötüdür".
  - `bitti`: sıradaki adımı açar.
- Kural: `Tamamlanan` listesi sıranın "kesintisiz ön eki" olmalı.
- Döngü freni: aynı (adım, durum) çifti 3 kez görülürse kapanmaya izin verir.
- Önemli uyarı: "**Stop kancasının `stdout`'u sahibin ekranına ÇIKMAZ** … Modele ulaşan tek yol `exit 2 + stderr`" (`tools/guard/README.md`).
- Neden tek blok: aynı bilgiyi düz metinde de yazmak "drift kapısıdır".

**Kanıt:** oyun2'de G0'dan G5'e kadar bütün adımlar tamamlandı ve blok son hâlinde duruyor (gözledim). Ama G4.5 kapısı yama yapılmadan geçilemezdi (§3).

**DevOS:**
- **Uyarlayarak al:** tek makine-okur durum bloğu ve "bitmemiş iş varken oturum kapanmaz" Stop kancası. Bunlar bulutta proje dosyası olarak çalışır.
- **Alma:** kurulum töreninin kendisi.

### M2 · Sabit kalıplar ve sabit kapı

**Sorun:** Serbest üretimde kurallar kayboluyor: "iki kurulumda tarifte var olan kategoriler sessizce kayboldu" (`GENESIS.md`).

**Nasıl işler:**
- Kural: "**Kalıp metni SABİTTİR: kopyala, «alanları» doldur, kadran uygula — DERLEME/YENİDEN-YAZMA YOK.**"
- Doldurulmamış alan işareti `«»`. Kanıt komutu: `grep -R '«'` boş dönmeli.
- G4.5 kapısı `tools/guard/kurulum-denetimi.sh`: 948 satır, oyun2'de "56 kalem". İlkesi: "denetleyen ≠ denetlenenin yazarı".

**Kanıt:**
- oyun2'de EL_KITABI, KARAR_ALANI Bölüm A ve OTONOM_DONEM kalıpla birebir aynı; farklar yalnız doldurulan alanlar (gözledim, diff).
- Kapının kendisi kırıktı (§3).

**DevOS:**
- **Al (ilke olarak):** temel dosyalar kalıptan doldurulur ve mekanik olarak denetlenir.
- **Alma:** 948 satırlık tek kapı.

### M3 · DEFO_MODELI: on defo, iz ilkesi, doğuş reçetesi

**Kök itki (kaynak diyor, `00_genesis/DEFO_MODELI.md`):** "Ajan, cevabı oluştururken **anlık onay / 'iyi görünme' olasılığını maksimize etmeye** itilir".

**On defo:** Yağcılık · Aynalama · Şişme · Drift · Sahte-menü · Uydurma · Öz-onaylama · Donma/aşırı-sorma · Karar-yükleme · Örtme. Her birinin tabloda bir "İz kontrolü" var.

**İz ilkesi:** "defo bir iz bırakmalı, ya da izin YOKLUĞU bayrak olmalı. Kural yazarken sıralama: mekanik kapı > iz isteyen yazılı prosedür > salt öğüt."

**Doğuş reçetesi:** "hiç koşulmamış töreni önceden inşa etme (tek örnekten şablon türetilmez; genelleme 2-3 gerçek gözlem ister)". Ayrıca: "sistemin kendi öz-tarifini asla dış doğrulama sayma".

**Kanıt:**
- oyun2 rolleri istenen izleri bıraktı: `kırpıldı:` satırları, `TÜRETME-İZİ`, `DEĞERLENDİRMEDİKLERİM` alanları (gözledim).
- keel kendi reçetesini çiğnedi. Dönem makinesi gerçek bir kutuda ilk kez oyun2'de koştu, 4 dönemde 4 yeni kusur çıktı. Prova "fişleri" için kendisi şunu yazıyor: "KEEL sürümünün provasını kanıtlıyordu, kullanıcının kurulumunu değil" (`docs/SOZLUK.md` §2d) (çıkarım).

**DevOS:** **Al.** Kısa bir defo listesi ve her defo için gözlenebilir bir iz ya da kapı. U015'teki şikâyetlerle doğrudan örtüşüyor (çıkarım).

### M4 · EL_KITABI kuralları (seçme)

Hepsi `00_genesis/EL_KITABI_KALIBI.md` dosyasında.

- **D1 · Çatal-kapısı:** "Net sıradaki adımı UYGULA; "yapayım mı?" diye sorma. Sahibe yalnız GERÇEK çatal gider — **üçü birden**". Üç şart: birden çok meşru yol var; seçim sahibin değerine bağlı; yapı kendi çözemez. İstisna: "Geri-alınamaz ya da dışa-dönük iş … ÖNCE sorar."
- **D2 · Kapanış bloğu:** "**BİTEN · SENDE BEKLEYEN · SIRADAKİ.** Orta satır makine-okur, birebir: `SENDE BEKLEYEN: YOK` ya da `SENDE BEKLEYEN: N madde`". Her madde dört şey söyler: "neden soruyorum · seçimin neyi değiştirir · geri dönüşü var mı · itiraz etmezsen ne olur".
- **D4 · Kendi beyanı yetmez:** "'Bitti / çalışıyor / yeşil' beyanı tek başına GEÇERSİZDİR".
  - D4a: dosya doğrulaması yazma aracı olmayan `dogrulayici` alt ajanına verilir.
  - D4c: "Sunuldu/geçti/koştu" ancak olay olduktan sonra yazılır.
  - D4d · Kanıt-komutu: komut "çıktıyı değiştiren ek taşıyamaz (bayrak oynama, boru-filtre, `tail`/`grep` süzmesi, `|| true`) … komutsuz kanıt kanıt değildir".
- **D9 · İş icat etme:** "İş yalnız iki kaynaktan doğar: aktif kutunun görevleri ya da sahibin koyduğu amaç."
- **F1 · Tek yazar:** her dosyada `<!-- yazar: … -->`.
- **F2 · Durum dosyaları:** yerinde yeniden yazılır, tarihçe git'te.
- **F3 · Bayt tavanları:** PANO 2KB, DURUM 2KB, KUTU 10KB.
- **F5 · Olaya gömülü kapanış:** "olaya gömülü hijyen 73 oturumda HEP koştu; tetiğe/hatırlamaya bağlı bakım HİÇ koşmadı".
- **F6 · Kural değişimi:** yalnız retroda ve sahip onayıyla.
- **F7 · Devir notu:** "neden + gerekçeli kararlar + kilitli/açık ayrımı + varılan yer + sonraki gündem".
- **F8:** "`git add -A` YASAK".
- **Mühür:** "devam" gibi muğlak bir mesaj onay sayılmaz. Gerekçe: "tatbikatta "devam" 3/6 mühür sayıldı, 3/6 durdu".

**Kanıt:** F1 başka iki kuralla birleşince oyun2'de sahipsiz bir iş doğdu (K-14):
- `dogrulayici.md` "görevi bu satır kapatır" diyor, ama koltuğun yazma aracı yok.
- `sevk.sh` satırı rolün kapatmasını bekliyor, ama hiçbir rol sözleşmesi bunu söylemiyor.
- F1'e göre `KUTU.md`'nin yazarı koordinatör.

oyun2'nin OTONOM_DONEM eki özetliyor: "rol kendi satırını kapatamaz (F1) ve sevk görev kapatmaz (§11), yani edim başka türlü sahipsizdi". Sonuç: hiçbir görev kapanamadı (gözledim, §3).

**DevOS:**
- **Al:** D1, D2, D4 ile D4d, D9, F2, F5, F7.
- **Uyarlayarak al:** F1. Her durum geçişinin sahibi yazılı olmalı ve ilk gün sınanmalı.
- **Alma:** F3 bayt tavanları ve F6 kilidi.

### M5 · Kutu (iş dilimi)

**Biçim (`01_kutular/KT-NNN-<ad>/KUTU.md`):**
- `## Görevler` başlığı altında tablo: `| Görev | İş | Sahip | Durum | Kanıt |`. Durum sözlüğü: `açık · sürüyor · mühür-bekliyor · kapalı · pas`. Tek evi `tools/bekci/gorev-durumlari.txt`.
- "bu kutu bitince gözünle göreceklerin": sahibin dilinde 3 somut iddia.
- Kabul kriterleri iki sınırlı: alt sınır ve "**Üst sınır (kapsam aşımı = hata)**".
- Makine-okur `**Açılış mührü:**` satırı.
- `## Duruş sözleşmesi`: `BİTİŞ HÂLİ / KANIT / KISIT / BÜTÇE / İZİN / LİSTE`.
- Risk satırları: `G-12: onkosul=G-07 G-08 · risk=riskli — …`.
- Tavan: "tek faz · tek gözle-görülür demo cümlesi · ≤5 görev · tek domain rolü".

**Ölçütler sonradan değişmez:** bekçi ölçütleri taban commit'e (`02_kanon/kilitli/.taban-ref`) karşı diff'ler. Gerekçe: "ajan kendi başarı kriterini değiştirebildiğinde oyunlama katlanarak artar".

**İlk kutu kabuğu (`ILK_KUTU_KALIBI.md`):** "Bu kutunun işi, bu projenin nasıl yürütüleceğini çıkarmaktır. Kod yazmakla başlanmaz." Dört çıktısı var: BITTI_TANIMI, BILINMEYENLER, KAYIT_DUZENI, KUTU_PLANI.

**Kanıt:** oyun2'de 9 görev açıldı, 8'i kapandı, G-09 açık kaldı, kutu kapanmadı (gözledim).

**DevOS:**
- **Uyarlayarak al:** görev tablosu, kanıt sütunu, alt/üst sınırlı kabul, "gözünle göreceklerin" bloğu.
- **Alma:** "ilk kutu yalnız plan, kod yok" yaklaşımı.

### M6 · Kanon ve karar alanı

**İçerik (`02_kanon/`):**
- VIZYON: "karar değildir" diye işaretli çapa.
- KARAR_INDEKSI (liste) ve `kilitli/` (gövdeler). Kural: "hatalı kilitli karar düzeltilmez, YENİSİ yazılır ve `aşar: K-NN` işaretçisiyle bağlanır" (oyun2 KARAR_INDEKSI).
- KARAR_SABLONU: Karar / Neden / Alternatifler / Ne bağlar / **Gizli bedel** / Kanıt.
- `golden/`, KADRO, OTONOM_DONEM, BITTI_TANIMI, KUTU_PLANI.

**Alıntılama:** ajan sahibe soru sormadan bir karara dayanabilir: "`sormadım çünkü K-NN` … karar ne kadar yazılıysa sahibe o kadar az soru gider" (oyun2 KARAR_INDEKSI).

**KARAR_ALANI, Bölüm A (kaynak diyor):**
- Madde 1: "**Sahip hiçbir alanın bilgi kaynağı değildir.**"
- Madde 2: sahibe yalnız görünüşü, davranışı ya da kapsamı değiştiren ve cevabı başka yerde bulunamayan soru gider. Örnek: ""ekstrede detay görünsün mü" GİTMEZ … "ParaPuan ekstreye girsin mi" GİDER".
- Madde 5: "Sorusuz öneri yok, önerisiz soru yok".

**KARAR_ALANI, Bölüm B:** sahip profili. Dört başlık: ne bilir, ne bilmez, neye karar vermek ister, soru tarzı.

**Kanıt:**
- oyun2 rolleri `TÜRETME-İZİ` alanında VIZYON ve karar satırlarına çapa attı.
- Dönemlerde sahibe 0 çatal gitti (gözledim, zarflar #32–#91).

**DevOS:**
- **Al:** karar listesi, gövde şablonu ("gizli bedel" dahil), "yeni karar eskisini aşar" kuralı.
- **Al:** KARAR_ALANI Bölüm A. Bu, K-015 ile örtüşüyor: Batu müşteridir, teknik soru ona gitmez.
- **Uyarlayarak al:** Bölüm B, Batu için yeniden yazılmalı.

### M7 · Roller: sözleşme, tören, kafes, alt ajan koltukları

**ROL.md sözleşmesi (`SOZLESME_KALIBI.md`):**
- Motivasyon, olumsuzdan yazılır: "bu rol yoksa hangi iş sahipsiz kalır".
- Yazma beyaz listesi ve `Mod: yazamaz | tam`.
- "Açılış ek-okumaları".
- Bekleme raporu tek satırdır.
- Teslim etiketleri: `[KARAR: X] / [AÇIK→DEVİR: alıcı seçer] / [BİLİNÇLİ-DIŞARIDA: gerekçe]`.
- Modüller:
  - DOĞRULAYICI: "**Kör-türetme sırası:** beklenen değeri ÖNCE karar/spec'ten kendin türet, ANCAK SONRA mevcut çıktıya/golden'a bak". Gerekçe: "350 yeşil testin arkasında hiç inşa edilmemiş motor yakalandı".
  - ÜRETİCİ: boşluk etiketleri L1 / L2 / L3.
  - DOMAIN ve DIŞ GÖZ.

**Tören ve kafes:**
- `.claude/skills/rol-<slug>/SKILL.md` içinde `disable-model-invocation: true` ve `` !`bash "${CLAUDE_PROJECT_DIR:-.}/tools/guard/rol-ac.sh" <slug> <mod>` ``.
- Tören `tools/guard/.aktif-rol` damgasını yazar. file-guard, `yazamaz` modda Edit ve Write'ı keser.
- Damga kendiliğinden kalkmaz (U70). Gerekçe: "fazla kafes işi durdurur ve görünür, eksik kafes güvenceyi yalanlar ve görünmez" (`tools/guard/README.md`).

**Alt ajan koltuğu (`ROL_ALT_AJAN_KALIBI.md`):**
- `tools:` iki değerden biri olur: `Read, Grep, Glob` ya da `Read, Grep, Glob, Edit, Write, Bash`.
- "`memory` ALANI YAZILMAZ".
- Gövde: "**taze hafızalı** bir çağrıdasın … Hatırladığını sandığın şey varsayımdır — dosyadan doğrula."

**Sabit yazamaz koltuklar:** `dogrulayici`, `catal-denetcisi`, `kurulum-denetcisi`.

**Dış göz (`disgoz`):** "denetçi işin doğru yapıldığını kanıtlar; dış göz sahibin doğru şeyi onayladığını kontrol eder" (G2.5). Tek çıktısı 5 başlıklı `BRIFING.md`.

**Kanıt (gözledim):**
- oyun2'de 11 koltuktan 8'i iş yaptı: 7'si yalnız otonom dönemde alt ajan olarak; koordinatör ayrıca bir el-sürüşlü oturumda.
- Tören izi yok: "BEKLEYEN KANIT: ilk rol töreni" hiç kapanmadı.
- `disgoz/BRIFING.md` boş iskelet kaldı.
- `denetci` ve `yayin` hiç açılmadı.
- Domain sınıf adları kaydı: pedagoji ROL.md'si `yerleşik/tartışmalı/boşluk` diyor, EL_KITABI `bağlayıcı/tartılır/açık-kalır`. GENESIS'in ürettiği metinde "tek ev" kuralı çiğnenmiş.

**DevOS:**
- **Uyarlayarak al:** rol dosyası (motivasyon, yazma beyaz listesi, eksen ayrımı, negatif liste).
- **Al:** alt ajanı ince bir koltuk olarak kur; sözleşmeye işaret etsin, `tools` kısıtlı olsun, memory olmasın, "taze hafıza" cümlesi bulunsun.
- **Al:** yazma aracı olmayan doğrulayıcı.
- **Alma:** insanın açtığı tören ve damga kafesi. Alt ajanın `tools` alanı zaten mekanik bir kısıttır.
- **Uyarlayarak al:** dış göz, Batu'ya kısa normallik raporu olarak. Ama oyun2'de hiç koşmadı.

### M8 · Pano ve sahip yüzeyleri

**`00_pano/PANO.md` iki bloktan oluşur:**

```
## MEKANİK BLOK — yalnız bekçi yazar
Son denetim: 2026-08-13 12:50 (denetim #39)
Işıklar: AKIŞ=YEŞİL · DOSYA=SARI
Görevler: G-01=kapalı · … · G-09=açık
Sahipte bekleyen: 0
Sıra: sahip
Kırmızı: 0 · Sarı: 2
```

- İkinci blok `## YARGI BLOĞU — yazar: koordinator`. Satırları: `**Aktif kutu:**` · `**SIRADAKİ OTURUM:**` · `**Blokaj:**`.
- Alan listesinin tek evi `tools/kokpit/pano-alanlari.txt`.

**Öbür yüzeyler:**
- `SAGLIK.md`: tarih damgası "yoksa ya da bir günden eskiyse sistem KIRMIZI'dır" (kılavuz kalıbı).
- `SENDE_BEKLEYEN.md`: SessionEnd kancası (`kapanis.sh`) son asistan mesajındaki `SENDE BEKLEYEN: N madde` satırını ayrıştırıp kuyruğa ekler. Kural: "**Madde SİLİNMEZ:** `[x]` + tarih + cevapla kalır".
- Günlükler: `oturum-gunlugu.jsonl` (SessionEnd yazar), `zarf-gunlugu.jsonl` (tek yazarı `zarf-ekle.sh`); ayrıca `SABAH.md`.
- Kokpit: `tools/kokpit/server.mjs`. "Sunucu yalnız 127.0.0.1'e bağlanır", yalnız GET kabul eder, 15 saniyede bir tazelenir. macOS başlatıcısı `Kokpit.command`.

**Kanıt (gözledim):**
- oyun2'de PANO ve SAGLIK bekçi tarafından doğru yazıldı (denetim #39).
- Kuyruğa 4 izin-engeli notu düştü. Koordinatör hepsini "sahibe gitmedi" diye kapattı.
- `oturum-gunlugu.jsonl` tek satır: `"not":"transcript yolu yok/bulunamadi"`. SessionEnd yolu bu kurulumda neredeyse hiç iz bırakmadı.

**DevOS:**
- **Uyarlayarak al:** mekanik blok ile yargı bloğunun ayrılması. Batu repoya GitHub'dan bakar.
- **Al:** silinmeyen sahip kuyruğu.
- **Alma:** kokpit (yerel sunucu, Mac başlatıcısı).

### M9 · Bekçi: sabit çekirdek denetim

**Sorun (kaynak diyor):** "altı gerçek kurulumda altı farklı bekçi … üçünde zorunlu-küme denetimi hiç yok".

**Nasıl işler:**
- `tools/bekci/cekirdek.mjs` sabittir; `bekci.sh` onu sarar; `bekci.conf` tek ayar dosyasıdır.
- Son satır: `BEKCI v1 durduran=<n> kilit=<n> uyari=<n> bilgi=<n> ariza=<n> kadran=<tam|kucuk> pencere=<kurulum|isletim>`.
- Çıkış kodları: 0, 1, 2. 2 anlamı: "bekçinin kendi arızası — "kırmızı" değil, AYRI hâl".
- Makine satırında ciddiyet kelimesi yasak. Gerekçe: "metinde geçen tek açıklama cümlesi dönemi durdurabiliyordu".
- Kural: ""ölçemedim" ile "temiz" aynı şey değildir".
- 36 göz, 5 kategori: tavan, şema, koruma-hattı, bağ-varlık, golden-tazelik.

**Kanıt:**
- oyun2 öz-testi: `kadran=uydurma` ile koşuldu; sonuç `ARIZA … çıkış kodu 2` (GENESIS_DURUM).
- Ama `korunan-yol-kirliligi` gözü 1. dönemi durdurdu (K-13, §3).

**DevOS:**
- **Al:** makine satırı, 0/1/2 çıkış sözleşmesi, "ölçemedim ≠ temiz" kuralı.
- **Alma:** 36 gözlü çekirdek. Küçük bir durum denetimi betiği yeter (çıkarım).

### M10 · file-guard (PreToolUse)

**Nasıl işler:**
- Kaynak listesi `tools/guard/korunan-yollar.txt`.
  - `[SERT]` yolları: `tools/guard/`, `tools/sevk/`, `tools/bekci/`, `.claude/`, `02_kanon/kilitli/`, `00_pano/zarf-gunlugu.jsonl` ve benzerleri. Sonuç `exit 2`.
  - `[SORULUR]` yolları: `golden/`, `00_genesis/`, `OTONOM_DONEM.md`, `KARAR_ALANI.md` ve benzerleri. Sonuç `"permissionDecision":"ask"`.
- Rol kafesi.
- Bash "dikişleri": damga, kurulum işareti, taban-ref, dönem göstergesi.
- İçerik süzgeci: TCKN, IBAN, kart, API anahtarı, JWT, PEM. Liste `sinif-listesi.txt`.
- Dışa-fiiller listesi: `curl`, `ssh`, `gh`, `git push`, `osascript` ve benzerleri. Hepsi "ask".
- Otonom dönemde İZİN dışı her adım ENGEL alır. Kanca ajana şunu söyler: "bu adımı ATLA, işine devam et ve dönüş zarfına «İZİN-ENGELİ: <ne engellendi>» satırını yaz".
- node yoksa yazma engellenir.
- Beyanlı sınır: kabuk yazımı metin eşleşmesiyle yakalanır; "değişkende saklanan değer, base64, parça-birleştirme kaçar".

**Kanıt (gözledim):**
- Kurulumda `.claude/settings.json`'a kasıtlı Edit denendi. Sonuç: "file-guard ENGEL: bu yol korumalı ([SERT] sınıfı: .claude/)".
- 3. dönemde 4 rolün Bash adımı engellendi; hepsi dönem göstergesini okumaya çalışıyordu.
- `gelistirici`nin sabit yollarda `node` arayan adımı `disa` sayıldı ve kesildi (zarf #90). Koruma, ekibin kendi ortam ölçümünü engelledi.

**DevOS:**
- **Uyarlayarak al:** `.claude/` ve kural dosyalarını koruyan küçük bir PreToolUse kancası ve gizli bilgi süzgeci.
- **Alma:** `git push` ve `gh` için onay. Bulutta push DevOS'un olağan işi.
- **Alma:** 864 satırlık dikiş zinciri.

### M11 · Otonom dönem: sevk döngüsü

**Akış (`tools/sevk/README.md`):**

```
/donem → gösterge + çapa + donem-acilis kaydı
Stop → sevk → SEVK talimatı (exit 2) → ana oturum Agent açar
   ↓ devir-kapisi (şema + talimat↔fiil)
alt-ajan çağrısı
   ↓ SubagentStop → zarf-bicim-kapisi (biçim + karne)
Stop → sevk → … → açık iş yok / duran kapı → dönem kapanır
```

**Ana oturum:**
- Rolü dağıtıcıdır: "bu oturumdaki rolün SEVK'tir ve sevk İŞ YAPMAZ" (`.claude/skills/donem/SKILL.md`).
- Talimat şunu söyler: "DEVIR METNI (AYNEN gecir, baska hicbir satir ekleme)".

**Devir kapısı (`devir-kapisi.sh`):**
- Devir metni yalnız `gorev · kutu · sozlesme · kural · ek-okuma` anahtarlarını taşır.
- En çok 800 bayt.
- (rol, görev) ikilisi açık bir `sevk-karar` kaydıyla eşleşmelidir. Böylece "iç içe alt-ajan … bu kapıda durur".

**Dönüş zarfı (`OTONOM_DONEM_KALIBI.md` §4):**
- Altı alan: `BİTEN` · `ÇATAL` · `DEĞERLENDİRMEDİKLERİM` · `SIRADAKİ` · `TÜRETME-İZİ` · `GERİ-ÇEKİLEN`.
- Karneci koltuk üç satır ekler: `KARNE-GOREV` · `HÜKÜM: YEŞİL | KIRMIZI | DOĞRULANAMADI` · `MADDELER`.

**Karne şartı:**
- Bir görev "tabloda `kapalı` + TAZE YEŞİL karne" ile kapalı sayılır.
- "**Kendi işine karne yazamazsın.**"

**Frenler:**
- Bütçe yalnız üretim çağrılarını sayar.
- Tur tavanı `3 * BUTCE + 5 + …`.
- Kapanıştan üretime dönüş en çok 2 kez.
- "sevkin kendi hatası dönemi SÜRDÜRMEZ, KAPATIR".

**Model bağımsızlığı (§8):** "Model bağımsızlığımız YOK … Bağımsızlığımız **taze bağlam + yazma yetkisizliği**dir".

**Gerçek dönemin şartları (Mac'e bağlı):**
- launchd watchdog.
- Taze nabız.
- SMTP kanalı; parola Keychain'de.
- `caffeinate` (`donem-ac.sh`).

**Kanıt (gözledim, §3 tablosu):**
- Makine 7 alt ajanı sırayla sevk etti.
- Zarfları biçim kapısından geçirdi; 4 red oldu, düzeltilen zarflar geçti.
- G-01 için bağımsız doğrulayıcı açtı.
- Ama üç dönem "duran kapı" ile bitti.

**DevOS:**
- **Uyarlayarak al:** çekirdek fikir.
  - Ana oturum dağıtır.
  - İş taze alt ajanda yapılır.
  - Alt ajan sabit alanlı bir zarf döner.
  - SubagentStop kancası zarfı denetler ve JSONL'e yazar.
  - Stop kancası sıradakini söyler.
  - Karne görevi kapatır.
  - Bulut notu: alt ajan kendi alt ajanını açamaz. keel'in iç içe çağrı yasağı buna zaten uygun.
  - Bağlam notu: ana oturum yalnız dağıtıyor ve kısa zarflar alıyor. 3. dönemde 7 alt ajan tek oturumda sevk edildi (gözledim). keel'de %80 bağlam sıkıştırmasına dair önlem yok (gözledim, ağaç genelinde arama).
- **Alma:** e-posta ve IMAP kanalı, uzaktan cevap, launchd, `caffeinate`, çatal denetçisi, İZİN sözlüğü, gösterge ve çapa dosyaları.
- Çıkarım: keel'de dönem tek oturumun Stop kancasıyla sürer. Bulutta boşta kalan makine geri alınırsa dönem ölür. Dönem durumu da `.gitignore`'daki `.donem-acik` ve `.donem-capa` dosyalarında; bunlar geri alınan makinede kaybolur. DevOS'ta süreklilik git'teki durum dosyası ve zamanlanmış tetikle (routine / send_later) kurulmalı.

### M12 · Hasım inceleme (bul, sonra çürüt)

**Nasıl işler (`.claude/workflows/hasim-inceleme.js`):**
- 5 mercek: `dogruluk`, `kabuk`, `test`, `gerileme`, `sizinti`.
- Her mercek en çok 6 bulgu çıkarır.
- Her bulguya ayrı bir çürütücü bakar: "Bulgu ancak mekanik kanıtla ayakta kalır; emin değilsen ayakta=false".
- "Bulgu yoksa boş liste MEŞRUDUR". İnsan tetikler.
- Salt okunurluğun kanıtı: öncesinde ve sonrasında `git status --porcelain` karşılaştırılır.

**Kanıt:** oyun2 K-13 kaydı: "Üç bağımsız mercek + her birine ayrı çürütücü koştu" (kaynak diyor).

**DevOS:** **Uyarlayarak al**, büyük değişikliklerde. Workflow aracının bulutta olup olmadığı bilinmiyor (O11'in konusu).

### M13 · Sözlük ve "tek ev"

**Sözlük (`docs/SOZLUK.md`):**
- "bir kelime bir şeyi anlatır".
- "koşu" altı ayrı şeyi anlatıyordu; altı ayrı ada ayrıldı.
- "kapı" üç şeyi anlatıyordu.
- 635 geçiş ve 749 satır tek tek sınıflandırıldı.

**Tek ev:** bir listenin tek bir evi olur. Örnekler: `gorev-durumlari.txt`, `zarf-jetonlari.txt`, `pano-alanlari.txt`, `disa-fiilleri.txt`. İlke: "Aynı olguyu iki yerde yazmak drift kapısıdır".

**DevOS:** **Al.** Kısa bir sözlük tut ve bir bilgiyi yalnız bir yerde yaz.

## 3 · oyun2: keel ile ne yapıldı, ne oldu

**Proje:**
- "Hayat Oyunu": çocuklara neden-sonuç ilişkisi kurmayı öğreten bir iOS oyunu (README).
- Sahip adı G0'da `Ahmet` olarak onaylandı.
- Ama zarflardaki yollar `/Users/Batu/Batu-Vault/oyun2/…`. İş Batu'nun Mac'inde, bir Obsidian kasasının içinde koştu (`bekci.conf`: `kok_izinli_ek=.DS_Store .obsidian`) (gözledim).
- Ahmet'in ayrı bir kişi mi, takma ad mı olduğu bilinmiyor.

**Kurulum (2026-08-12/13, `00_genesis/GENESIS_DURUM.md`):**
- Kadran: "**ritüel tam · kadro GENİŞ · sahibe giden soru trafiği DAR.**"
- Sahip ritmi: "haftada 3 gün × ~30 dk".
- 11 koltuk: urun, koordinator, oyuntasarim, icerik, pedagoji, guvenlik, tasarim, gelistirici, denetci (yazamaz), disgoz (yazamaz), yayin (uyuyan).
- Haber kanalı Gmail ile kuruldu; uzaktan cevap açık.

**Kurulumda çıkan şablon kusurları:**
1. **G4.5 kapısı hiçbir zaman yeşil olamazdı.** Kayıt: "`grep -q` ilk eşleşmede çıkıyor … `while` SIGPIPE alıp **141** ile ölüyor ve `pipefail` yüzünden hattın tamamı BAŞARISIZ sayılıyor … **Sonuç: beş kategori de KIRMIZI → G4.5 çekilme kapısı bu hâliyle asla yeşile dönemez.**"
   - Test bunu yakalamamıştı: sahte bekçi "TEK dosyayla" kuruluyordu.
   - Sahip onayıyla korumalı betik değişti (K-12). Kayıttaki sonuç: "**bu YEŞİL, betiğine bir kez dokunmuş bir kapıdan alınmıştır.**"
2. Şablonun kendi `dogrulayici.md` dosyası `«»` kullanıyordu. Kapı bunu "doldurulmamış alan" saydı.
3. Kabuğun sabit bütçesi 6'ydı, gereken sayı 10'du: "6 ile kutu **mekanik olarak bitirilemezdi**". Bütçe 12'ye çıkarıldı.
4. Çekilmeden sonra bekçi `DURDURAN [şema] kapanis-disi-el-kitabi` bastı. Sebep: EL_KITABI'na son dokunan commit'in başlığı `genesis:` ile başlamıyordu. Başlık yeniden yazıldı, hash'ler değişti, `.taban-ref` güncellendi.

**Dönemler (`00_pano/zarf-gunlugu.jsonl`, 2026-08-13, UTC, gözledim):**

| Dönem | Tür | Ne oldu | Nasıl bitti |
|---|---|---|---|
| `K20260813-001248`, 00:12–00:24 | kurulum | `kurulum-denetcisi`nin ilk zarfı biçimden döndü: "TÜRETME-İZİ çözülmüyor: çapa yok". Karne KIRMIZI: 4. kalem, G-01 tek çağrıda dört teslim taşıyordu. | Duran kapı: "bekçi KIRMIZI … [SERT] yolda commit-dışı değişim: 00_pano/zarf-gunlugu.jsonl". Dönem kendi yazdığı günlük yüzünden durdu → K-13 |
| `…054240`, 05:42–05:53 | kurulum | G-01 ikiye bölündü (Ç-04). Karne YEŞİL. | "kurulum denetimi YEŞİL — muhur sahibin" |
| `…055545`, 05:55–06:42 | yapım | 7 görüş görevi (G-02–G-08) sırayla koştu, her biri 3,5–8 dk. 4 rolün dönem göstergesini okuyan Bash adımı engellendi. 2 zarf biçimden döndü. | Duran kapı. 7 görev için: "G-02: donusu geldi ama gorev satiri hala açık (rol Durum hucresini kapatmadi — tekrar sevk edilmez …)". Ayrıca "G-09: onkosul cozulmedi (G-01)" → K-14 ve Ç-05 |
| `…085826`, 08:58–09:19 | yapım | G-02–G-08 araya elle kapatılmıştı. Sevk bunu "miras-gorev … bagimsiz karnesi yok — tabloya guveniliyor" diye kaydetti; 7 görüş doğrulamasız sayıldı. G-01 koştu; K-14 satırı kapattı (`"defter":{"sonuc":"kapatildi"}`). Doğrulayıcı karnesi DOĞRULANAMADI verdi: "30 bilgi türü" iddiası dosyada 27 ya da 31. | Duran kapı: "gorev G-01 kapali isaretli ama karnesi DOĞRULANAMADI — duzeltme rolun/sahibin isidir, sevk gorevi kendi acamaz (v1 sinir)" |

**Canlı koşuda yazılan yamalar (kaynak diyor, gözledim):**

- **K-13** (`tools/bekci/cekirdek.mjs`).
  - Bulgu: "Yani sistem hem kirliliği üretiyordu hem temizliğini yasaklıyordu."
  - Değişiklik: `00_pano/zarf-gunlugu.jsonl` yolu kirlilik gözünden muaf tutuldu (`continue`). Ayrıca SABAH.md gibi sevkin kendi ürettiği 3 dosya pano şemasına eklendi.
- **K-14** (`tools/sevk/zarf-bicim-kapisi.sh`).
  - Bulgu: "Bir görevin Durum hücresini «açık»tan «kapalı»ya çeviren edim üç ayrı yere atfedilmişti ve ÜÇÜ DE uygulanamazdı".
  - Değişiklik: satırı artık biçim kapısı kapatıyor. 6 koşul var; hepsi sağlanmazsa yazmıyor.
- **Ç-05.**
  - Bulgu: "tablonun tek meşru yazarı koordinatör olduğu için iki toplama da kendi ürününün arkasına kilitlenmişti ve dönem boyunca hiç sevk edilmedi."
  - Değişiklik: G-09'un önkoşulu "yok" yapıldı.
- **Koordinatörün kendi kaydı:** "Dairesel önkoşulu ben yazdım" (`03_roller/koordinator/DURUM.md`).

**Son durum (12:50):**
- PANO: "SIRADAKİ OTURUM: `/donem KT-001-proje-plani yapim` — şimdi".
- G-09 açık. BITTI_TANIMI ve KUTU_PLANI iskelet.
- `04_urun/` yok.
- Dış göz brifingi hiç yazılmadı.
- Geliştirici: "**iOS derlemesi bugün mümkün değil (ölçüldü).** … Xcode.app, iOS SDK, simülatör yok. Makine Intel Core i5".
- Kurulu kopyada koşulan test sınavı 393 geçti, 47 kaldı. Sebep: "dağıtılan kopyada şablon kaynağı olmadığı için fixture kurulamıyor" (KARAR_INDEKSI K-14).
- 2026-08-14'te GitHub'a gönderildi. Sonrasında iz yok.

**Ekibin ürettiği (işe yarayan kısım):**
- 8 görüş dosyası, her biri yaklaşık 2 KB.
- `BILINMEYENLER.md`: 17 bilinmeyen. Kaynakları: sahip 4, araştırma 6, ilk gerçek işte 7.
- `KAYIT_DUZENI.md`: yaklaşık 30 bilgi türü → mevcut dosya → yazar. Doğrulayıcı 27 ya da 31 saydı. "**Üç kural.** ① Her dosyanın tek yazarı vardır … ② Durum dosyaları yerinde yeniden yazılır … ③ Aynı olguyu iki yerde canlı tutmak yasaktır".
- Blokaj biçimi: `Blokaj: <iş> · kimde: <rol> · bağlı: <ne bekleniyor> · tetikte: <gelince ne olacak>`.
- Roller uydurmadı, boşlukları işaretledi.
- Engel: "**Araştırma hattı bugün KAPALI.**" (BILINMEYENLER). Pedagoji notu: "**Kaynak erişimi olmayan domain koltuğu yalnız boşluk defteri üretebilir**".

## 4 · keel neden yetersiz kaldı

Her maddede kanıt dili belirtildi.

1. **Ağırlık (gözledim, ölçü):**
   - ~176 KB kural ve kalıp, ~77 KB araç sözleşmesi, ~760 KB yorum ağırlıklı araç kodu, ~1 MB test. Buna karşılık 32 KB görüş metni.
   - Tavanlar sürekli büyüdü: OTONOM_DONEM 12.288 → 17.920 bayt, yedi artışla (kalıbın kendi yorumu).
   - Ağaçta testler dahil 276 hasım turu atfı ve 27 "Ders:" satırı var.
   - Çıkarım: sistem çoğunlukla kendi disiplinini inşa etti.
2. **Birleşim yerleri denenmemişti (gözledim, §3):** her duruş iki parçanın arasında çıktı:
   - bekçi ↔ zarf-ekle;
   - F1 ↔ sevk ↔ doğrulayıcı;
   - sabit bütçe ↔ kadro büyüklüğü;
   - test fixture'ı ↔ gerçek kurulum;
   - zarf iddiası ↔ karne.
   Birim testleri bu yerleri görmez. keel de bunu biliyordu: "Gerçek bir projede uçtan uca kurulum ayrı bir kanıttır" (SURUM).
3. **Her yer fail-closed, toparlanma yok (kaynak diyor):**
   - Seçim bilinçliydi (rol kafesi gerekçesi): "fazla kafes işi durdurur ve görünür".
   - "sevk gorevi kendi acamaz (v1 sinir)".
   - Her anomali = dur + insan. Sahibin haftalık bütçesi ~1,5 saat. Çıkarım: ilerleme fiilen durdu.
4. **Güvence katmanları kilitlendikleri anda atlandı (gözledim):**
   - Kurulum kapısı "denetleyen ≠ denetlenenin yazarı" çiğnenerek geçildi.
   - 7 görüşün doğrulaması "miras-gorev" boşluğundan atlandı.
   - K-13 bir gözü kapattı ve bunu "BEYANLI KAYIP" diye yazdı.
5. **İnsan tetiği ve Mac bağımlılığı (kaynak diyor, gözledim):**
   - Tören, dönem ve mühür insan ister.
   - launchd, Keychain, caffeinate, yerel kokpit, Xcode'suz Intel Mac.
   - Bulut DevOS bunların hiçbirini karşılamaz.
6. **Plan önce, iş sonra (gözledim):**
   - İlk kutunun işi "nasıl yürütüleceğini çıkarmak"tı.
   - 11 koltuk kuruldu. Uzmanlığı gerçekten gereken ikisinin (pedagoji, güvenlik) araştırma erişimi yoktu.
   - Somut ürün riski ilk gün görülebilirdi, görülmedi: derleme ortamı yok.
7. **Kural enflasyonu kalıplara da sızdı (gözledim):**
   - Alt ajan zarfı 6+3 alan, 3 bayt tavanı, 4 red. Bir zarf yalnız çapa yolu `02_kanon/` önekiyle yazılmadığı için döndü (zarf #8).
   - Bu, iş değil biçim yüküydü (çıkarım).

## 5 · DevOS'a uygunluk özeti

| keel parçası | Karar | Kısa gerekçe |
|---|---|---|
| Makine-okur durum bloğu + Stop sürücüsü (M1) | uyarlayarak al | Durumsuz devam için gerçek kod; bulutta çalışır |
| Sabit kalıp + mekanik "doldurulmamış alan" denetimi (M2) | al (ilke) | Serbest üretimde kural kaybını önler |
| DEFO_MODELI + iz ilkesi (M3) | al | Batu'nun şikâyet ettiği davranışların panzehiri |
| D1, D2, D4/D4d, D9, F2, F5, F7 (M4) | al | Kısa, mekanikleşebilir, oyun2'de çalıştı |
| F1 tek yazar (M4) | uyarlayarak al | Her durum geçişinin sahibini tabloya yaz ve sına (K-14 dersi) |
| Kutu biçimi (M5) | uyarlayarak al | "İlk kutu = plan" yerine ilk kutu somut bir teslim |
| Karar indeksi + gövde şablonu + KARAR_ALANI Bölüm A (M6) | al | Batu = müşteri; teknik soru gitmez |
| Rol dosyası, ince alt ajan koltuğu, yazamaz doğrulayıcı (M7) | uyarlayarak al / al | Derinlik 1 ve taze bağlamla uyumlu |
| Rol töreni + damga kafesi, 11 koltuk, uyuyan roller (M7) | alma | İnsan tetiği; oyun2'de hiç kullanılmadı |
| PANO iki blok + silinmeyen sahip kuyruğu (M8) | uyarlayarak al | Batu için tek dosyalık durum ve bekleyenler |
| Kokpit (M8) | alma | Yerel sunucu ve Mac başlatıcısı |
| Bekçi makine satırı + 0/1/2 (M9) | al (küçük hâli) | "Ölçemedim ≠ temiz" |
| file-guard (M10) | uyarlayarak al (küçük) | `.claude/` ve kural koruması, sır süzgeci; push onayı yok |
| Dönem: dağıtıcı ana oturum + zarf + SubagentStop + karne (M11) | uyarlayarak al | Çekirdek fikir sağlam; birleşim yerleri baştan sınanmalı |
| Haber kanalı, watchdog, caffeinate, uzaktan cevap (M11) | alma | Mac ve e-posta bağımlı |
| Hasım inceleme (M12) | uyarlayarak al | Büyük değişiklikte bul → çürüt |
| Sözlük + tek ev (M13) | al | Hafızasız oturum için anlam kaybını önler |

## 6 · Dersler

Her ders: **ne oldu → kök neden → önlem · kaynak**.

1. **Canlı koşu olmadan yayın.**
   - Ne oldu: 1202 test vardı; ilk gerçek kurulumda çekilme kapısı açılamadı.
   - Kök neden: fixture gerçeği temsil etmiyordu (tek dosya, SIGPIPE doğmuyor).
   - Önlem: DevOS'un kabul kriteri "bir gerçek iş uçtan uca koştu" olsun. Testler ek kanıttır.
   - Kaynak: `oyun2/00_genesis/GENESIS_DURUM.md` "KAPI BULGUSU".
2. **Sahipsiz durum geçişi.**
   - Ne oldu: görev tamamlandı ama "açık → kapalı" edimini kimse yapamadı.
   - Kök neden: doğrulayıcı "kapatır" diyordu ama yazamıyordu; sevk rolden bekliyordu ama hiçbir rol sözleşmesi bunu söylemiyordu; F1 tabloyu koordinatöre veriyordu. Üç kural hiç birlikte sınanmamıştı.
   - Önlem: her durum geçişinin tek sahibini yaz ve ilk gün sına.
   - Kaynak: K-14 yorumu (`oyun2/tools/sevk/zarf-bicim-kapisi.sh`).
3. **Sistemin yan ürünü kendi alarmını çaldı.**
   - Ne oldu: dönem kendi yazdığı günlük yüzünden durdu.
   - Kök neden: append-only günlük, korunan kaynak dosya gibi ele alındı.
   - Önlem: makine günlüğü ile korunan kural dosyası ayrı sınıflar olsun.
   - Kaynak: K-13, zarf #9 → #11 → #13.
4. **"DOĞRULANAMADI" döngüyü öldürdü.**
   - Ne oldu: tek bir sayım farkı dönemi durdurdu.
   - Kök neden: sevk düzeltme görevi açamıyordu (v1 sınırı).
   - Önlem: kırmızı ya da belirsiz karne, tavanlı olarak aynı role düzeltme görevi olarak dönsün. Batu'ya yalnız tavan aşılınca gidilsin.
   - Kaynak: zarf #121, #125, #127.
5. **Elle kapatma doğrulamayı atlattı.**
   - Ne oldu: 7 görüş karnesiz "kapalı" sayıldı.
   - Önlem: karnesiz kapalı hiçbir yoldan geçerli olmasın.
   - Kaynak: zarf #106–#112 ("miras-gorev").
6. **Türev sayı sabit metne gömülmüştü.**
   - Ne oldu: bütçe 6'ydı, kadro + 1 = 10 gerekiyordu.
   - Önlem: türev sayılar hesaplansın, kalıba yazılmasın.
   - Kaynak: GENESIS_DURUM "G4".
7. **Araştırma erişimi kapalıydı.**
   - Ne oldu: domain rolleri yalnız boşluk üretti.
   - Önlem: DevOS rollerinin WebSearch ve WebFetch izni baştan ve rol düzeyinde tanımlansın.
   - Kaynak: `03_roller/pedagoji/NOTLAR.md`, `guvenlik/NOTLAR.md`.
8. **Ortam varsayıldı.**
   - Ne oldu: iOS projesi Xcode olmayan bir Intel Mac'te kuruldu.
   - Önlem: ilk iş ortamı ölçmek. Bulutta bunun yeri setup script.
   - Kaynak: `03_roller/gelistirici/NOTLAR.md`.
9. **Kullanılmayan ritüel inşa edildi.**
   - Ne oldu: rol töreni hiç kullanılmadı, dış göz hiç koşmadı, `denetci` ve `yayin` hiç açılmadı.
   - Önlem: keel'in kendi reçetesi, "hiç koşulmamış töreni önceden inşa etme". Rol ve ritüel ancak gerçek ihtiyaç görülünce eklensin.
   - Kaynak: GENESIS_DURUM, `disgoz/BRIFING.md`.
10. **Sahip teknik onaycı yapıldı.**
    - Ne oldu: K-12, K-13 ve K-14'ün her biri "sahip onaylı". Sahip (kayıtta "Ahmet") teknik bir SIGPIPE yamasına onay verdi.
    - Önlem: sistemin kendi araçlarına yapılan düzeltme Batu'ya gitmesin. Kayıt, test ve bağımsız doğrulayıcı yeter (K-015).
    - Kaynak: `oyun2/02_kanon/KARAR_INDEKSI.md`.
