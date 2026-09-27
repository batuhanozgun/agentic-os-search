# T4 — Yön, yetki ve denetimler

**Tür:** P0.4 küme taslağı; alt ajan çıktısı (model çıktısı). 27 Eylül 2026. Salt okumayla çalışıldı; yazılan tek dosya budur.
**Görev tanımı:** `briefs/ORTAK.md`, `briefs/ORTAK-SENTEZ.md`, `briefs/T-ORTAK.md`, `briefs/T4.md`.
**Alt sistemler (R11 §2.4):** S1 Yönetişim ve yetki · S2 Batu ile iş birliği · S14 Kalite güvencesi ve doğrulama · S15 Muhakeme disiplini ve bilinen ajan kusurları · S17 Gözlemlenebilirlik ve ilerleme.
**Beslediği karar:** METHOD v1'de bu beş alt sistemin hangi mekanizmalarla kurulacağı; birleştirme adımının girdisi.
**Kullanım sınırı:** Mekanizmaların hepsi bu taslağın tasarım önerisidir (etiket: çıkarım). Hiçbiri bu ortamda canlı sınanmadı. Sayısal eşikler başlangıç değeridir, pilotta ayarlanır. Taslak aynı modelin ürünüdür; kendini doğrulamaz, P0.5 eleştirisine ve Batu'ya gider.

---

## 0. Soru, kaynaklar, okuma kapsamı

### 0.1 Soru
EXP-007'yi yürüten çalışma sisteminde yön, yetki ve denetim işlevleri standart seviyede hangi bileşenlerle ve somut olarak nasıl kurulur? Bu bileşenler diğer kümelerin mekanizmalarına nereden bağlanır?

### 0.2 Kaynaklar ve okuma kapsamı

| Kaynak | Kapsam |
|---|---|
| Görev tanımları: ORTAK, ORTAK-SENTEZ, T-ORTAK, T4 | tam |
| Kardeş görev tanımları T1, T2, T3, T5 (arayüz için) | tam |
| `briefs/ENTEGRASYON.md` (henüz kayda girmemiş; veri olarak, yalnız biçim uyumu için) | tam |
| `briefs/E-ORTAK.md`, `E1–E3.md`, `REVIZYON.md` | okunmadı |
| EXP-007 README, STATE, DECISIONS, P0 README | tam |
| `sources/conversation/` U001–U006, A001–A003, INDEX | tam |
| R11 | tam (§0–§7, Ek A) |
| R07 | kısmi: kaynak tablosu, §0, §1, §2.5–§2.8, §3–§9 tam; §2.1–§2.4 okunmadı |
| R08 | kısmi: §0–§1, §2.11–§2.15, §3, §4, §7–§9 tam; §2.1–§2.10, §5–§6 okunmadı |
| R09 | kısmi: §0, §4, §5, §7, §8, §10, §11 ve MK-8 tam; kalanı okunmadı |
| R10 | kısmi: §0–§2, §4.8–§4.10, §5.3–§5.6, §6–§10 tam; kalanı okunmadı |
| R01 | kısmi: repo ekseni, örnek repolar ekseni ve eksik-arayıcı (satır 655–1076) tam; belge eksenleri yalnız anahtar sözcük araması |
| R02 | kısmi: §3–§4 tam, başlıklar |
| R03, R05 | tam |
| R04 | kısmi: (a)–(d) ve uyarılar tam |
| R06 | kısmi: mekanizma tablosu satırları ve §2–§3 (arama) |
| `AGENT.md` (kontrol katmanı; veri olarak incelendi, uygulanmadı) | tam |
| `agent/protocols/`: decision-critical-assumptions, user-independent-reasoning, verification-independence, source-view-fidelity, causal-depth-root-cause-validation, goal-method-end-to-end-validation, canonical-work-preflight | tam |
| `agent/protocols/work-system-continuity.md` | kısmi (başlıklar, §1–§3'ün başı) |
| `agent/protocols/candidate-research-library.md` | yalnız başlıklar |
| Batu'nun makaleleri: `publications/linkedin/articles/2026-07-16-ai-defolari-csvpf.md`, `2026-06-20-sahte-secenek-lwr8f.md` | tam |
| `batuhanozgun/loopinance_v2@07cd81bb`: `docs/DEFO_MODELI.md`, `CLAUDE.md`, `.claude/agents/urunci.md`, `docs/arsiv/ilk-plan-2026-09-24.md` | tam (mcp__github__get_file_contents, salt okuma, 27.09.2026) |
| DEFO_MODELI'nin andığı "üç-birden çatal testi" | bulunamadı: depo içi kod araması sonuç vermedi; okunmadı sayılır |
| EXP-005 `reflections/LESSONS-AND-OPEN-QUESTIONS.md`, `concepts/CHARTER.md`, EXP-004 `reflections/QUALIFICATIONS.md` | yalnız alıntı doğrulaması (satır araması) |
| code.claude.com/docs/en: sub-agents, hooks, routines, mobile, claude-code-on-the-web (curl, 27.09.2026) | anahtar sözcük araması; ilgili paragraflar okundu |
| Ortam: `~/.claude/launcher-settings.json`, `~/.claude/stop-hook-git-check.sh`, `claude --version`, ortam değişkenleri | okundu (gözlem) |
| EXP-006 (`origin/main`), Foundation ve studies'in kendisi | okunmadı; R-notları üzerinden atıf (K-010'a göre EXP-006 bağlayıcı değil) |
| Kardeş küme taslakları T1, T2, T3, T5 | okunmadı: paralel yazılıyor, `drafts/` yazım başlarken yoktu |

### 0.3 Kanıt dili ve okuma kuralları
- **Etiketler:** kaynak diyor / gözledim / çıkarım / varsayım / bilinmiyor.
- **Kanıt türü:** Batu'nun sözü · repo olayı · tedarikçi belgesi (Anthropic) · uygulayıcı pratiği (loopinance) · kavramsal analiz (Foundation, EXP-004) · alt ajan raporu (R01–R11; ikincil) · gözlem (bu oturum). Hiçbir mekanizma için bağımsız ölçüm yok.
- **Claude Code iddialarında cloud durumu** R07'nin işaretleriyle verilir: C+ cloud için belgeli · C~ genel belge · C! cloud'da kısıtlı · C? belirsiz · Cg bu oturumda gözlendi.
- R11'in kanıt kodları "R11 K25" biçiminde anılır. Bu taslakta birincil kaynaktan yeniden kontrol edilenler **Ek A**'dadır ("EkA-3" biçiminde anılır).
- **Sahiplik (T-ORTAK):** Dosya yolları öneridir; dosya mimarisinin sahibi T1, Claude Code yapılandırmasının sahibi T5, kalıcı rollerin sahibi T2'dir. Rol adı uydurulmadı; ihtiyaç işlev olarak yazıldı ("çürütücü inceleme işlevi: T2'ye ihtiyaç").
- **Zorlama düzeyi** R07 §2.5'teki ayrımla: tavsiye (talimat metni) / yapısal (şablon, zorunlu alan) / zorlayıcı (hook, izin kuralı, araç listesi). Hook adayları §3.3'te Z1–Z6 diye numaralıdır.
- Dosya adlarında Türkçe karakter kullanılmadı (GUNLUK, KAPANIS); betik ve arama araçlarında sorun çıkmasın diye.

---

## 1. Özet

1. **Batu'nun dikkati bir güvenlik kanalıdır.** K-010 ile ikinci model hattı kapandı; aynı modelden olmayan tek denetçi Batu'dur. S2 buna göre kuruldu: üç bitişli kısa mesaj, commit okumadan denetim veren kontrol noktası raporu, SHA'ya bağlı kabul paketi, önerili soru kuyruğu (çerçeve soruları biriktirilmez), dikkat bütçesi.
2. **Sürekli yetki (K-002) bir yetki zarfına çevrildi:** kendiliğinden geçişler, duraklar, 12 yükseltme tetiği, "sıradaki mantıklı iş ≠ sıradaki yetkili iş" satırı. Zarf dosyadan çözülemezse yeni iş başlamaz. Otomatik uyanışlar hiçbir zaman onay sayılmaz.
3. **Hız varsa fren:** karar düzeyinde ilerleme ölçüsü (kapanan soru, verilen/değişen karar, doğrulanmış teslimat, kabul), iki eşikli takılma alarmı, devre kesici, 5 kalemde bir öz-denetim ve yön kontrolü; kırmızı alarm Batu'ya ulaşmazsa sistem kendini yavaşlatır.
4. **"Doğrulandı" kelimesi aynı modelin okumasına verilmez.** Tamamlanma katları (Y yapıldı → K kaynaktan kontrol → Ç çürütülemedi → İ işe yarıyor → B Batu kabulü @SHA) ve bağımsızlık etiketleri tek sözlükte. Kontrol ağırlığı risk sınıfına (R0–R3) bağlı; genel "tekrar kontrol et" talimatı yasak.
5. **Söz geniş, çıktı dar olmasın:** söz–çıktı matrisi (U003, U004, A003, Batu kararları ve Claude'un verdiği sözler → mekanizma → düzey) ve standart–yeterli denetimi (her "gereksiz/ertelendi" kararı koşul ve bütünsel etki ister; "şimdilik yeter" bir bulgudur).
6. **Muhakeme disiplini iz ilkesiyle kurulur:** 13 defolu model (loopinance'ın on defosu ve bu repoda gözlenen kapsam daraltma, erken kapanış, aşırı kesinlik). Her karşı önlem bir iz alanı ya da mekanik kapıdır; "dikkat edeceğim" karşı önlem değildir.
7. **AGENT.md protokolleri alt ajana routing gate olarak değil, üç taşıyıcıyla gider:** rol dosyasındaki disiplin bloğu, görev tanımı alanları, dönüş iz alanları. AGENT.md'nin Claude'a uyarlanması (tur sınıfları, bloğun yeri, alt ajan yükümlülükleri) Batu'ya tek paket olarak gider; onaya kadar kural harfiyen uygulanır.
8. **Zorlama:** altı denetim hook'a adaydır; hepsi A-04 onayına ve tek repolu oturuma bağlıdır; kurulmazsa yapısal düzeyde kalır.

---

## 2. Alt sistemler

### 2.1 S1 — Yönetişim ve yetki

**Amaç.** Kimin neye karar verdiğini, Batu'nun yetkisinin nasıl devredildiğini, sınırın nerede olduğunu ve kontrol katmanının Claude'da nasıl işlediğini açık, kayıtlı ve konuşmayı görmemiş bir oturumun çözebileceği biçimde tutmak. S1'in hatası iki yönlüdür: ya her şey Batu'ya gider ve "devam" yükü ona döner (R11 E01), ya da Batu adına amaç değiştirilir (R11 E75: EXP-006'da asistanın SOUL'un ilk işini seçmeyi önermesi, D012). Hız (K-002) ile fren burada birlikte tanımlanır.

**R11'e göre değişenler.**
- Eklendi: iş nesnesi başına yetki tablosu. Foundation bu hakları bilerek atamıyor: "does not establish … who may select, commit, reprioritise, waive, accept, terminate or reactivate Work" (R04 (a)4). Yükseltme tetiklerinin tam listesi. Otomatik istemlerin yetki karşısındaki statüsü (EkA-8, EkA-9).
- Genişletildi: "kontrol katmanı değişiklik kuralı" bileşeni; protokollerin ana oturum ve alt ajan işletimini ve AGENT.md uyarlama paketini kapsıyor.
- Sadeleşti: "hatlar arası otorite" K-010 ile tek satıra indi: EXP-006 okunur, EXP-007'yi yönetmez, ona yazılmaz.

**Karar tablosu.**

| Bileşen | Karar | Önlediği hata | Kabul testi | Kaynak | Kart |
|---|---|---|---|---|---|
| Karar katmanları (mekanik / tercih / yön) | gerekli | ya her şey Batu'ya ya Batu adına amaç değişikliği (E01, E75) | 10 karar kaydında katman tabloyla tutarlı | R11 S1; A003 §3.6; R05 satır 22 | S1-M1 |
| İş nesnesi başına yetki tablosu (başlatır, değiştirir, kapatır, yeniden açar, kabul eder) | gerekli | haklar tanımsız kalır; koordinatör akış sahipliğinden karar sahipliğine kayar (E06) | tabloda boş hücre yok | R04 (a)4; R10 §5.4 | S1-M1 |
| Revizyon sınıfları (yürütme / yöntem / başarı anlayışı / amaç) | gerekli | yönü bir önceki tur belirler (E03) | her plan revizyonunda sınıf satırı | R06 DQ03 | S1-M1 |
| Sürekli yetki zarfı ve çözülemezlik kuralı | gerekli | yeni oturum durur ya da kapsam uydurur (E02; R01 SP12) | soğuk başlangıç oturumu "sıradaki yetkili iş"i dosyadan söylüyor | K-002; R01 | S1-M2 |
| Yükseltme tetikleri | gerekli | sessiz değer seçimi; Batu'nun geç öğrenmesi | her tetik için bir örnek olay ve kuyruk izi | R01 eksik-arayıcı | S1-M2 |
| Frenler (ilerleme ölçüsü, alarm, devre kesici, yön kontrolü, durak) | gerekli | frensiz sürekli yetki (E81, Y12) | "ilerlemesiz 3 kalem" senaryosunda alarm | R11 Y12 | S1-M2, S17-M2/M3, S15-M5 |
| Soru sınıflama ve yükseltme kuralı | gerekli | aşırı sorma ya da sessiz değer seçimi (E72) | Batu'ya giden soruların hepsinde sınıf, öneri, "neden sana" | A003 §3.1 | S1-M3 |
| Otomatik seçim (tercih) kaydı | gerekli | kabulde sürpriz (Y16) | kontrol noktası raporlarında tercih listesi | R11 Y16; R05 satır 3 | S1-M3 |
| Karar kaydı (Batu / Claude ayrı; gerekçe, yanlışsa bedeli, yeniden açma koşulu) | gerekli | salınım ya da unutma; parafrazda yaşayan karar (E47) | 5 kayıtta 9 alan dolu | R11 S1; R05 satır 14 | S1-M4 |
| Kontrol katmanı ilişkisi: protokol işletimi, routing bloğu, otomatik uyanışlar | gerekli | disiplin yalnız istemde yaşar (E89); otomatik istem onay sanılır (R07 BZ-5) | Batu'ya giden mesajlarda blok; görev tanımlarında taşıyıcı alanlar | AGENT.md; R01 SP01–SP08 | S1-M5 |
| Alt ajanın routing gate koşması | gereksiz, koşullu (bkz. S1-M5) | — | S15-M2 kabul testi geçiyorsa | R01 repo ekseni | S1-M5 |
| Araç izni ≠ karar yetkisi ayrımı | gerekli; sahibi T2 (S16) | araç gücü yetki sanılır (E04) | rol dosyasında iki ayrı alan | R10 §5.3 | §3.1 İ12 |
| Ayrı "yönetişim dosyası" | gereksiz (ayrı dosya olarak) | — | — | R11 K49 | — |

"Ayrı yönetişim dosyası" gerekçesi: içerik gerekli, ayrı yüzey gerekli değil. Koşul: yetki tablosu METHOD'da, zarfın özeti STATE'te işaretçiyle durur. Ayrı dosya tek kaynak ilkesine karşı bir kopya daha üretir (R11 K49: aynı durumun 5–7 dosyada kopyalanması). Bütünsel etkisi yok, çünkü hiçbir bileşen düşmüyor; yeri T1'in kararıdır.

#### S1-M1 — Karar katmanları ve yetki tablosu
- **Ne:** Her kararı üç katmandan birine yerleştirir ve her iş nesnesinde kimin başlattığını, değiştirdiğini, kapattığını, yeniden açtığını ve kabul ettiğini tek tabloda sabitler.
- **Nerede:** METHOD'un "Yönetişim" bölümü (yol T1'in). İçerik:

```
## Karar katmanları
| Katman | Ne zaman | Kim karar verir | Nereye yazılır | Batu ne zaman görür |
|---|---|---|---|---|
| M mekanik | Cevap kaynaktan ya da kuraldan türetilir; amaç, kapsam, ölçüt değişmez; geri alınabilir | Ana oturum (görev tanımıyla yetkilendirilmişse alt ajan) | Çalışma günlüğü (S17-M1) | Görmez |
| T tercih | Birden çok makul seçenek; seçim bir değer yargısı taşıyabilir; amaç, kapsam, ölçüt değişmez | Ana oturum geçici olarak | Tasarım karar kaydı, "katman: T" (S1-M4) | Sonraki kontrol noktası raporunda toplu |
| Y yön | Amaç, kapsam, kabul ölçütü, harita, durak, yetki zarfı, yeni erişim, kontrol/yapılandırma, geri alınamaz ya da dış etki | Batu | DECISIONS K-xxx, birebir kaynaklı | Hemen: soru kuyruğunda "çerçeve" sınıfı |
Belirsizse bir üst katman seçilir.
Örnekler: M — VM kaybından sonra R10'u aynı görev tanımıyla yeniden başlatmak (STATE "Oturum kesilirse").
T — araştırmayı beş kümeye bölmek; takılma eşiğinin başlangıç değeri.
Y — dalın main'e birleşmesi (K-009, A-07); ChatGPT hattıyla ilişki (K-010); kök CLAUDE.md (A-04); K-002'nin yeni haritaya eşlenmesi.

## Revizyon sınıfları (plan ya da çerçeve değişince)
| Sınıf | Değişen | Kim |
|---|---|---|
| R-a yürütme | işin nasıl yürüdüğü | ana oturum |
| R-b yöntem | seçilen yöntemin uygunluğu | ana oturum; aşama raporunda bildirir |
| R-c başarı anlayışı | ölçütün yorumu | ana oturum önerir; ölçüt Batu'nunsa Batu |
| R-d amaç ya da kapsam | Batu'nun amacı, kapsamı | Batu |
Kendi yanlış iddiasını geri çekmek hiçbir sınıfta onay beklemez (A003 §3.7).

## Yetki tablosu
| Nesne | Başlatır | Değiştirir | Kapatır | Yeniden açar | Kabul eder |
|---|---|---|---|---|---|
| Harita ve duraklar | Batu (ana oturum önerir) | Batu | Batu | Batu | Batu |
| Aşama | Ana oturum, yetki zarfına göre | Aşama içi plan: ana oturum | Ana oturum, kapanış kapısıyla (S14-M7) | Ana oturum; adı konmuş tetikle, en küçük kapsamda; kabul edilmişse Batu'ya hemen (Y10) | Durak aşamasında Batu, SHA'ya bağlı; kendiliğinden geçen aşamayı sonraki durağın kabul paketi kapsar |
| İş kalemi | Ana oturum (kaynağı: plan, keşif, bulgu, Batu) | Ana oturum | Ana oturum, tamamlanma katıyla | Ana oturum, tetikle | Ana oturum (K ya da Ç katı) |
| Soru | Herkes (alt ajan dönüşüyle) | Ana oturum (sınıfı) | Cevabın sahibi: kaynak ya da Batu | Ana oturum, yeni kanıtla | — |
| Batu kararı (K-xxx) | Batu | Batu | Batu (yerine koyarak) | Batu; ana oturum önerir | — |
| Claude tasarım kararı (TK) | Ana oturum | Ana oturum, kayıtla | Ana oturum | Ana oturum, tetikle | Sonraki durakta Batu |
| Alt ajan çalışması | Ana oturum | Ana oturum, yeni sürümlü görev tanımıyla | Ana oturum | Ana oturum; aynı tanımla ikinci gönderim yalnız kayıpta | — |
| METHOD | Batu (P0.8) | Değişiklik türüne göre (T5 S21); yetki genişletmesi ve ölçüt değişikliği Batu'da | Batu | Ana oturum önerir | Batu |
| Rol tanımı | Batu (A-04) | T2'nin değişiklik türü tablosu (R10 §5.4) | Batu | — | Batu |
| Yapılandırma ve kontrol katmanı | Batu (A-04; Mutation Rule) | Batu | Batu | — | Batu |
```

- **Ne zaman:** Her karar anında (katman); her plan revizyonunda (revizyon sınıfı); yeni bir nesne türü doğduğunda (tabloya satır eklemek METHOD değişikliğidir).
- **Kim:** Ana oturum uygular. Tablonun kendisini değiştirmek Y katmanıdır: Batu.
- **Nasıl işler:**
  1. Karar anında sorulur: amaç, kapsam, ölçüt, harita, durak, yetki, erişim, kontrol katmanı ya da geri alınamazlık değişiyor mu? Evet → Y.
  2. Değilse: birden çok makul seçenek ve değer yargısı var mı? Evet → T. Değilse → M.
  3. Belirsizse üst katman.
  4. Katman karar kaydına yazılır.
  5. Y ise soru kuyruğuna çerçeve sınıfıyla, önerisiyle girer; o karara bağlı olmayan işler sürer.
  6. Plan revizyonunda sınıf satırı T3'ün değişiklik kaydına yazılır.
- **Zorlama düzeyi:** Yapısal: karar kaydında "katman" ve "dayanak" zorunlu alan. Tavsiye: sınıflama yargısı. Zorlayıcı parça: DECISIONS'a yalnız ana oturumun yazması (T2 S16) ve yeni K satırında kaynak alanı kontrolü (Z5).
- **Çalıştığını nasıl anlarız:** Aşama sonunda en az 10 karar kaydında katmanla tablonun uyumu (çürütücü okuma, S14-M4). Batu'nun iki tepkisi ayrı kusur türü olarak H kaydına girer: "bunu bana sormalıydın" (Y, T sanılmış) ve "bunu bana sorma" (M ya da T, Batu'ya taşınmış). Bozulma işareti: Batu kaynağı olmayan Y kararı; kontrol noktası raporuna girmeyen T kararı.
- **Bağımlılıklar:** İhtiyaç: S1-M4, S2-M3, T1 (DECISIONS ve TK biçimi), T2 (rol değişikliği tablosu), T5 (METHOD değişikliği kontrolü). Besler: S1-M2, S2-M4, S14-M7, T3'ün revizyon protokolü.
- **Standart seviye kararı:** Gerekli. Önlediği hata: yetki sınırının iki yönde kayması (E01, E03, E06, E75). Kabul testi: rastgele 10 karar kaydında katman ve dayanak tabloyla tutarlı; Y katmanında Batu kaynağı olmayan "verildi" kararı yok.
- **Kaynak:** R11 S1 bileşen 1 ve 5 (çıkarım); A003 §3.6–3.7 (v0 önerisi); R05 satır 21–22: "Mechanical — auto-decide; Taste — auto-decide, record, surface at final gate" (kaynak diyor; alt ajan raporu, gstack ürün kaynağı okuması); R06 DQ03: "SOUL'un kendi iş anlayışını değiştirebilmesi, kullanıcının amacını kendi başına değiştirmesi değildir" (kaynak diyor; ana oturum doğruladı); R04 (a)4; R10 §5.4.
- **Bedel:** Tablonun bir kez yazımı (~1 sayfa); karar başına bir alan. Risk: Y'nin T sanılması. Dengeleyici: belirsizse üst katman ve T kararlarının kontrol noktasında toplu sunumu.

#### S1-M2 — Sürekli yetki zarfı ve frenleri
- **Ne:** K-002'yi, yeni ya da uyandırılmış bir oturumun konuşmayı görmeden okuyabileceği bir yetki zarfına çevirir: kendiliğinden geçişler, duraklar, yükseltme tetikleri, frenler, çözülemezlik kuralı.
- **Nerede:** Batu'nun sözü DECISIONS K-002'de kalır (tek kaynak). Zarfın tam metni METHOD'da; işletim özeti STATE'in başındaki "Yetki" bloğunda. STATE bloğu, bugünkü duruma göre:

```
## Yetki (zarf Z1 · dayanak: K-002, K-005, K-009, K-010 · 2026-09-27)
- Şu anki aşama: P0. P0 içindeki adımlar kendiliğinden yürür (P0 README); P1, Batu'nun "başla"sı olmadan açılmaz (K-005).
- Sıradaki mantıklı iş: P0.4 birleştirme
- Sıradaki yetkili iş: P0.4 birleştirme (dayanak: P0 README adım tablosu)
- Sıradaki durak: P0.6 sonunda Batu'ya sunum; P0.8 anlaşması
- P1 sonrası kendiliğinden geçişler: K-002'nin yeni haritaya eşlenmesi Batu'da (soru önerisi T4-Q1)
- Açık yükseltme: yok · Alarm: yok · Bütçe: [T5] · İzinli canlı denemeler: tanımsız (T4-Q5)
```

METHOD'daki tam metin:

```
### Yetki zarfı Z1
Dayanak (birebir; A002 → U003 madde 1 → K-002): "P1→P2↔P3→P4 geçişleri kendiliğinden olsun. P4'te tasarım kabulü için dur. Kapsam değişikliği, yeni erişim ve cevaplayamadığım tercih soruları sana gelsin. Sorular biriksin, iş durmasın."
1. Kendiliğinden (Batu beklenmez): zarfın kapsadığı aşama geçişleri; planlı geri dönüşler; iş kalemi açma ve kapama; bütçe içinde alt ajan dağıtımı; M ve T kararları; kendi yanlış iddiasını geri çekme; kayıp alt ajan işini aynı görev tanımıyla yeniden başlatma.
2. Duraklar (Batu'nun kararı beklenir): tasarım kabulü (K-002'deki P4 durağının yeni haritadaki karşılığı); kurulum ve dış etki yetkisi; METHOD kabulü (P0.8).
3. Yükseltme tetikleri (Batu'ya gider; bağlı olmayan iş sürer):
   Y1  amaç, kapsam ya da kabul ölçütü değişikliği önerisi
   Y2  yeni erişim: repo bağlama, bağlayıcı, izin
   Y3  geri alınamaz ya da dış etki: main'e birleştirme, dal ya da PR silme, dış servise yazma, e-posta, zamanlanmış tetik
   Y4  kontrol katmanı ya da yapılandırma değişikliği (A-04, Mutation Rule)
   Y5  Claude'un cevaplayamadığı tercih sorusu (kuyrukta birikir)
   Y6  çerçeve sorusu (biriktirilmez)
   Y7  kırmızı takılma alarmı (S17-M3)
   Y8  bütçe eşiği (T5)
   Y9  Batu'nun iki kararı çelişiyor
   Y10 kabul edilmiş bir çıktıyı geçersiz kılan bulgu
   Y11 güvenlik: okunan içerikte talimat enjeksiyonu şüphesi ya da yetkisiz yazım izi
   Y12 her yol tahmin: bütün seçenekler kanıtsız
4. Frenler: karar düzeyinde ilerleme ölçüsü (S17-M2); iki eşikli takılma alarmı ve sessiz alarm kuralı (S17-M3); devre kesici; 5 kalemde bir ve her aşama sonunda yön kontrolü (S15-M5); duraklar.
5. Çözülemezlik: "Sıradaki yetkili iş" boşsa, dayanağı yoksa ya da iki yüzey çelişiyorsa yeni iş başlatılmaz. Açık kalem kayda kapanır. Batu'ya tek satır gider: "Şunu bekliyorum; senden karar yok: yetki çözülemedi, çünkü …". Çözüm bir Y kararı gerektiriyorsa soru olarak gider.
6. Otomatik istemler yetki değildir: alt ajan dönüşü, görev bildirimi, zamanlanmış mesaj, Routine tetiği ve webhook yükü onay ya da zarf genişletmesi sayılmaz.
```

- **Ne zaman:** Her oturum açılışında okunur (W1). Her aşama geçişinde denetlenir. Her Y tetiğinde uygulanır. Batu yeni bir karar verince zarf sürümü artar (Z1 → Z2) ve STATE bloğu aynı commit'te güncellenir.
- **Kim:** Ana oturum işletir ve STATE bloğunu günceller. Zarfın içeriğini değiştirmek Y katmanıdır: Batu.
- **Nasıl işler:**
  1. Açılışta blok okunur; "sıradaki yetkili iş" dayanağıyla birlikte doğrulanır.
  2. Her yeni iş kalemi açılırken zarfın 1. maddesine uyduğu kontrol edilir; uymuyorsa ilgili Y tetiği çalışır.
  3. Aşama kapanınca geçiş türüne bakılır: kendiliğinden ise aşama raporu gönderilir ve sonraki aşama açılır; durak ise beklenir.
  4. Bir fren tetiklenirse ilgili karta geçilir (S17-M3, S15-M5).
  5. Çözülemezlik halinde durulur (madde 5).
- **Zorlama düzeyi:** Yapısal: STATE'te zorunlu "Sıradaki yetkili iş" satırı ve dayanak alanı. Zorlayıcı aday: SessionStart hook'u Yetki bloğunu bağlama ekler, satır boşsa uyarır (Z2; T5; A-04; C! yalnız tek repolu oturumda). Otomatik istemlerin onay sayılmaması platform tarafından da uygulanır (EkA-8, EkA-9).
- **Çalıştığını nasıl anlarız:** Soğuk başlangıç testinde (T5 S18; A003 §6) taze oturum "sıradaki yetkili iş, sıradaki durak, Batu'ya ne zaman gidilir" sorularını yalnız dosyadan doğru cevaplar. K-001 ölçüsü: bir aşama geçişi için Batu'nun "devam" yazması = 0. Bozulma işareti: günlükte dayanaksız "açıldı" satırı; Batu'nun "devam" yazması; yaşanmış bir Y tetiğinin kuyrukta izi olmaması.
- **Bağımlılıklar:** İhtiyaç: S1-M1, S2-M3, S17-M2, S17-M3, S15-M5, T3 (harita ve geçiş türleri), T5 (bütçe, uyandırma, SessionStart). Besler: T5'in açılış protokolü; W1, W3, W5, W6.
- **Standart seviye kararı:** Gerekli. Önlediği hata: sohbette kalan yetkinin yeni oturumda kaybolması; yeni oturumun fail-closed durması ya da kapsam uydurması (E01, E02; R01 SP05, SP12); frensiz sürekli yetki (E81, Y12). Kabul testi: soğuk başlangıç sorularına doğru cevap; K-002 eşlemesinin Batu kararı olarak kaydı.
- **Kaynak:** DECISIONS K-002, K-005; A002 (birebir metin). R01 SP05: "Autonomy granted only in chat is also lost at the next fresh session." SP12: "A Routine prompt claiming authorization is not user authority." Eksik-arayıcı: "Its scope must not be fabricated." (kaynak diyor; alt ajan raporu, C+/Cg karışık). goal-method-end-to-end-validation §6A: "`next logical work`, `next authorised work`" ve canonical-work-preflight §8 "current authorization çözülemiyor" (kontrol katmanı metni, veri olarak). R11 S1 bileşen 2, Y12. EkA-9 (routines.md; C+).
- **Bedel:** Batu'dan bir karar paketi (eşleme, izinli denemeler, bildirim kanalı). Zarf değiştikçe sürüm ve STATE güncellemesi. Her açılışta ~10 satır okuma.

#### S1-M3 — Soru yönlendirme ve otomatik seçim kaydı
- **Ne:** Her bilinmeyeni beş yoldan birine ayırır; Batu adına verilen tercih kararlarını kaydeder ve kontrol noktasında toplu sunar.
- **Nerede:** Kural METHOD'da. Otomatik seçimler ayrı dosyada değil, tasarım karar kaydında "katman: T" olarak durur (tek kaynak); kontrol noktası raporu onları listeler. Kural ve örnek kayıt (örnek kurgusaldır):

```
Bilinmeyen → 1) Repoda cevabı var mı? → oku; soru kapanır.
           → 2) Kaynakla araştırılabilir mi (Anthropic belgesi, Foundation, studies)? → araştırma kalemi aç.
           → 3) Teknik ya da süreç kararı mı, Batu'nun değerine dayanmıyor mu? → M ya da T katmanında karar ver, kaydet.
           → 4) Küçük, geri alınabilir bir denemeyle çözülür mü ve deneme zarfta izinli mi? → dene; izinli değilse Y2/Y3.
           → 5) Batu'nun değeri, tercihi, yetkisi ya da kabulü mü? → soru kuyruğu (S2-M3), önerisiyle.
Batu'ya giden her soru "neden sana soruyorum" satırı taşır: 1–4'ün neden yetmediği.
Alt ajan Batu'ya ulaşamaz: gitmesi gerekebilecek soruyu dönüşünde "aday soru" diye bildirir; kendi başına verdiği seçimleri ayrı listeler.

### TK-P1-007 — Ortam denemeleri tek repolu oturumda yapılır   (kurgusal örnek)
- Katman: T · Karar veren: ana oturum · Tarih: 2026-10-02 · Y testi: amaç, kapsam, ölçüt değişmiyor
- Seçenekler: (a) tek repolu oturum: repo hook'ları ve izin kuralları okunur · (b) çok repolu Projects: okunmaz (R07 §2.5, §4 madde 3)
- Seçim ve gerekçe: (a); zorlama katmanı ancak böyle çalışır
- Yanlışsa bedeli: çok repolu işe geçişte hook'lar sessizce düşer; geri dönüş bir ayar değişikliği
- Batu'ya sunum: bekliyor → KN-P1-03 "Senin adına verdiğim tercihler" · Batu tepkisi: —
```

- **Ne zaman:** Her soru doğduğunda; her T kararında; her kontrol noktası raporunda.
- **Kim:** Ana oturum sınıflar ve karar verir; alt ajanlar aday soru ve kendi seçimlerini bildirir.
- **Nasıl işler:**
  1. Soru günlüğe SORU-ACILDI olarak yazılır.
  2. Beş yol sırayla denenir.
  3. T kararı TK kaydına "sunum: bekliyor" ile yazılır.
  4. Kontrol noktası raporu "bekliyor" olanları listeler.
  5. Batu itiraz ederse karar değişir (S2-M7). İtiraz etmezse "sunuldu, itiraz yok" işaretlenir; bu bir kabul değildir.
- **Zorlama düzeyi:** Yapısal: soru kaydında "sınıf" ve "neden sana", TK'da "katman" ve "sunum" zorunlu alan. Tavsiye: sınıflama.
- **Çalıştığını nasıl anlarız:** Batu'nun "bunu repoda bulabilirdin / araştırabilirdin" tepkisi = 0 (H kaydı türü). Bir aşamada hiç T kararı yoksa incelenir: ya kayıt tutulmuyor ya da her şey Batu'ya gidiyor. Batu'nun itiraz ettiği T kararlarının oranı izlenir; yüksekse sınıflama gevşektir.
- **Bağımlılıklar:** İhtiyaç: S1-M1, S1-M4, S2-M3, T3 S6 (araştırma yolu). Besler: S2-M2, S2-M4, S15-M1 (#8, #9).
- **Standart seviye kararı:** Gerekli. Önlediği hata: aşırı sorma, sahte menü, karar yükleme (E72); sessiz değer seçimi ve kabulde sürpriz (Y16). Kabul testi: bir aşamada Batu'ya giden soruların hepsinde sınıf, öneri ve "neden sana" var; kontrol noktası raporlarında tercih listesi var.
- **Kaynak:** A003 §3.1; R11 S1 bileşen 3–4, Y11, Y16; EkA-4 (urunci.md: "Türet, sorma."); EkA-1 (DEFO_MODELI #8–9); R05 satır 3: "record each auto-choice for parent visibility" (kaynak diyor; alt ajan raporu); decision-critical-assumptions "Bilgi Toplama İlkesi".
- **Bedel:** Soru başına kısa sınıflama; T kararı başına ~6 satır; raporda bir liste.

#### S1-M4 — Karar kaydı alanları
- **Ne:** Batu'nun kararlarını (DECISIONS, birebir kaynaklı) ve Claude'un tasarım kararlarını (TK) ayrı yerlerde, ama yeniden tartışmayı ve unutmayı önleyen aynı çekirdek alanlarla tutar.
- **Nerede:** DECISIONS.md (mevcut) ve T1'in belirleyeceği aşama karar dosyası. Alanlar ve bu taslağın gerçek bir kararıyla örnek:

```
### TK-P0-T4-02 — Aynı modelin karşı-okuması "doğrulandı" diye etiketlenmez
- Durum: öneri (P0.4 taslağı) · Katman: T · Yerine koyduğu: — · Yerine konduğu: —
- Bağlam: EXP-006'da aynı üretici kendi işini denetledi; hiçbir aile elenmedi (R11 K47)
- Karar: S14-M2 sözlüğü
- Karar-kritik varsayım: Farklı bir Claude modeli de ortak kör nokta taşır · yanlışsa: farklı model için etiket gevşetilir · sınandı mı: hayır
- Reddedilen: "karşı-okuma = doğrulama" (verification-independence §3: "Başka bir ajan, başka bir oturum veya başka bir model tek başına bağımsız doğrulama kanıtı değildir.")
- Sonuçlar: kolaylaşan — Batu'nun kabulü şişmiş etikete yaslanmaz · zorlaşan — raporlarda "doğrulandı" az görünür
- Yanlışsa bedeli: gereksiz temkin; maliyeti sınırlı
- Yeniden açma koşulu: farklı sağlayıcıdan model ya da bağımsız insan inceleyici eklenirse
- Araştırma izi: R07 BD-3 (destekledi) · R04 (d)3 (destekledi) · R11 Y6 (destekledi)
```

  Batu kararı satırı için T1'den istenen ek alanlar: "Batu'nun sözü" ile "Claude'un uygulama yorumu" ayrı; kapsam (neyi kapsar, neyi kapsamaz); etkilediği yüzeyler (yayılım listesi); yerine koyduğu karar. Gerekçe: K-009'daki "Dal yalnız EXP-007 klasörüne dokunur" ifadesi Batu'nun değil ana oturumun formülasyonudur (T-ORTAK), bugün Batu'nun sözüyle aynı hücrede duruyor.
- **Ne zaman:** Her T ve Y kararında (M kararları günlükte kalır); bir karar yerine konduğunda (eski kayıt silinmez, "yerine konduğu" alanı dolar).
- **Kim:** Ana oturum yazar (tek yazıcı). Batu kararının içeriği yalnız Batu'nun sözüdür.
- **Nasıl işler:** 1) Alanlar karar anında doldurulur; boş alan nedeniyle "—" bırakılır. 2) Batu kararı aynı iş içinde U-dosyasına bağlanır (S2-M7). 3) Yerine koymada yeni kayıt açılır, eskisine çapraz bağlantı verilir. 4) Yeniden açma koşulu gerçekleşince kalem açılır (T3).
- **Zorlama düzeyi:** Yapısal: şablon. Zorlayıcı aday: DECISIONS'a eklenen K satırında kaynak sütunu `sources/conversation/` yolu içermiyorsa yazımı engelleyen betik (Z5).
- **Çalıştığını nasıl anlarız:** Yeni oturum bir tasarım kararının neden verildiğini ve neyin onu yeniden açacağını yalnız dosyadan söyleyebiliyor (soğuk başlangıç sorusu olarak eklenir). Bozulma işareti: aynı kararın ikinci kez tartışılması; "neden böyle yapmıştık?" sorusu.
- **Bağımlılıklar:** İhtiyaç: T1 (biçim, yerine koyma kuralı), T3 S6 (araştırma izi), S2-M7. Besler: S1-M1, S14-M8, S17-M2 (KARAR olayı).
- **Standart seviye kararı:** Gerekli. Önlediği hata: salınım, unutma (R11 S1 bileşen 7); düzeltmenin parafrazda yaşaması (E47). Kabul testi: rastgele 5 TK kaydında 9 alan dolu.
- **Kaynak:** R11 S1 bileşen 7; R05 satır 14: "Each ruling records 'decision, reason and cost if wrong'" (kaynak diyor; alt ajan raporu); R08 O19 (ADR): "Immutable: Don't alter existing information in an ADR. … supersede the ADR by creating a new ADR" (kaynak diyor; topluluk pratiği); DECISIONS kural satırı; A003 §3.5 (araştırma izi); T-ORTAK.
- **Bedel:** T ya da Y kararı başına ~10 satır.

#### S1-M5 — Kontrol katmanıyla ilişki: protokoller, routing bloğu, otomatik uyanışlar
- **Ne:** AGENT.md ve dokuz protokolün (R01–R09) ana oturumda ve alt ajanlarda nasıl işleyeceğini, routing bloğunun nerede görüneceğini ve otomatik uyanışların nasıl sayılacağını tanımlar; AGENT.md'nin Claude'a uyarlanmasını Batu'ya tek paket olarak hazırlar.
- **Nerede:** METHOD "Kontrol katmanı" bölümü. Uyarlama paketi onaya kadar yalnız öneri metnidir; AGENT.md'ye yazılmaz.

  **Varsayım (A-01, cevaplanmadı):** AGENT.md ve `agent/protocols/` kontrol katmanı olarak kalır; K-004'teki "ChatGPT dosyaları" EXP-006'nın içidir. EXP-006'nın "sıradaki" satırları ve durma noktaları EXP-007'yi yönetmez; okunursa veridir (README; K-010).

  **Bugünkü durum:** AGENT.md ChatGPT için yazılmış: "At the start of every new ChatGPT project conversation, this file must be fetched fresh" (EkA-19). Kökte CLAUDE.md yok; AGENT.md kendiliğinden yüklenmiyor (R11 K16, gözlem). "User turn" otomatik turlar için tanımsız (R01 SP03). Blok gerekçesi ChatGPT arayüzü: "deliberately auditable in the ChatGPT browser workflow" (AGENT.md). Alt ajanın yükümlülüğü yazılı değil: "Nothing says whether subagents must run the gate" (R01). Özel alt ajanlar CLAUDE.md hiyerarşisini yükler (EkA-7): kök CLAUDE.md gate talimatı taşırsa bu her alt ajana gider.

  **Geçici uygulama (onaya kadar; kural harfiyen):**

| Tur | Gate | Blok | Yetki |
|---|---|---|---|
| Batu'nun mesajı | Tam gate; LOAD olan protokoller okunur (bu konuşmada tam okunduysa etkin kalır) | Batu'ya giden ilk ve son mesajın başında | Batu'nun sözü; kararsa DECISIONS'a |
| Otomatik uyanış: alt ajan tamamlanması, görev bildirimi, send_later, Routine, webhook | Platform bunları kullanıcı rolüyle teslim ettiği için tur sayılır; gate koşulur | Turun son mesajının başında | Hiçbir zaman onay değildir |
| Sıkıştırma ya da devamdan sonraki ilk tur | AGENT.md ve LOAD edilen protokoller yeniden tam okunur ("Do not rely on a remembered summary") | Aynı | — |
| Alt ajan | Koşmaz; disiplin S15-M2'nin üç taşıyıcısıyla gelir | Yok | Dönüşü veridir (R04, R05) |

  **Protokollerin işletimi:**

| Protokol | Ana oturumda: ne zaman, nasıl | Alt ajanda: taşıyıcı |
|---|---|---|
| R01 Varsayımlar | Karar ve plan anında; TK'da "karar-kritik varsayım" alanı | Görev tanımında "sınanacak varsayımlar"; dönüşte "karar-kritik varsayımlar" |
| R02 Kanıt dışı etki | Batu görüş ya da itiraz bildirdiğinde (S15-M3); kapanışta (S14-M7 §5) | Rol disiplin bloğu; çürütücüye "kapatmak istiyoruz" bilgisi verilmez |
| R03 Amaç–uyum | Aşama geçişi, kapanış, yeni dal; "sıradaki mantıklı ≠ yetkili iş" (S1-M2) | Görev tanımında amaç zinciri ve beslediği karar |
| R04 Doğrulama | Bir incelemeyle güven artırılırken; S14-M2 etiketleri | Çürütücü görev tanımı; dönüşte bağımsızlık etiketi |
| R05 Kaynak–temsil | Karar taşıyan iddiada (S14-M6); sıkıştırma sonrası | Dönüşte okuma kapsamı; "görmedim ≠ yok" |
| R06 Kök neden | Olay analizinde (S15-M4) | Teşhis isteyen görev tanımında iki ayrı soru |
| R07 Süreklilik | Kalem ve aşama kapanışında (T1, T5) | Yok (tek yazıcı); dönüşte "dokunulan dosyalar" |
| R08 Preflight | Oturum açılışı, devam, aşama başı; yetki çözülemezse durma (S1-M2 madde 5) | Görev tanımında taban commit ve zorunlu okumalar |
| R09 Aday kütüphane | Studies kullanılırken (T3 S6) | Dönüşte "aday, benimsenmiş değil" etiketi |

  **Uyarlama paketi (Batu onayına; Mutation Rule):**
  - **U1 Bootstrap platformdan bağımsız olsun:** Her yeni asistan oturumu (ChatGPT konuşması, Claude Code oturumu, Routine koşusu) AGENT.md'yi kanonik daldan okur. Claude Code'da `git fetch` ve yerel kopyanın kanonik dalla eşleşmesi "fresh" sayılır.
  - **U2 Tur sınıfları:** insan turu (Batu'nun mesajı) ve otomatik tur. Tam gate insan turunda ve maddi geçişte (aşama geçişi, plan revizyonu, yeni iş türü, sıkıştırma sonrası) koşar. Aynı yetkili iş içindeki otomatik turlarda yüklü küme taşınır; mevcut "Re-gating During a Turn" kuralı geçerli kalır.
  - **U3 Bloğun yeri:** Blok Batu'ya yazılan her mesajın (insan turu cevabı, kontrol noktası raporu, soru, alarm) başında görünür. Otomatik turların ara mesajlarında ve alt ajan dönüşlerinde gerekmez. Otomatik turda yüklü küme değişirse günlüğe bir satır yazılır.
  - **U4 Alt ajanlar gate koşmaz:** Ana oturum görevle ilgili protokol disiplinini rol dosyası ve görev tanımı alanlarıyla taşır; alt ajan dönüşü R04/R05 kapsamında veridir.
  - **U5 §6A ve sürekli yetki:** Kanonik durumda kayıtlı, kapsamı belli sürekli yetki (K-002 ve yetki zarfı) R03 §6A'daki "açık kullanıcı yönü" sayılır.
  - **U6 Sıkıştırma:** Sıkıştırma ya da devamdan sonra protokollerin yeniden okunması beklenen davranıştır, erişim hatası değildir.
  - **U7 CLAUDE.md:** Kök CLAUDE.md, AGENT.md'ye yönlendiren kayıtlı kontrol malzemesidir; içeriği T5'in. Özel alt ajanlara da yüklendiği için gate talimatı alt ajanı bağlamayacak biçimde yazılır ("Bu yönlendirme ana oturum içindir") ya da rol dosyalarında `omitClaudeMd: true` kullanılır. Hangisi olacağını T5 seçer.
  - **U8:** R07 ve R08 protokollerindeki "yeni bir ChatGPT oturumu" ifadeleri platformdan bağımsız hale gelir.

  A-01 "hayır" diye cevaplanırsa gate ve blok kalkar. Muhakeme disiplini kaybolmaz, çünkü S15-M2 onu METHOD'da ve rol dosyalarında zaten taşır (çıkarım). Tasarım A-01'in iki cevabına da dayanıklıdır.
- **Ne zaman:** Her tur (geçici kural); her görev tanımı yazımında (taşıyıcı alanlar); P0.6 sunumunda (uyarlama paketi).
- **Kim:** Ana oturum uygular; uyarlama kararı Batu'nun; kurulum T5'in.
- **Nasıl işler:** 1) Turun sınıfı belirlenir. 2) Geçici tabloya göre gate ve blok uygulanır. 3) Görev tanımına protokol tablosundaki taşıyıcı alanlar konur. 4) Sıkıştırma sonrasında yeniden okuma yapılır, günlüğe SIKISTIRMA satırı düşülür. 5) Uyarlama paketi P0.6 sunumunda tek soru olarak gider (T4-Q2).
- **Zorlama düzeyi:** Tavsiye (AGENT.md ve CLAUDE.md bağlamdır, zorlamaz: R07 §1 ilke 3) ve yapısal (blok şablonu, görev tanımı alanları). Mekanik zorlama önerilmez: hangi mesajın Batu'ya gittiğini bir betik güvenle ayıramaz (çıkarım). Denetim aşama sonunda örneklemle yapılır.
- **Çalıştığını nasıl anlarız:** Aşama sonunda Batu'ya giden son 10 mesajın hepsinde blok; 5 rastgele görev tanımında taşıyıcı alanlar; sıkıştırmadan sonraki ilk turda protokol dosyalarının yeniden okunduğuna dair araç çağrısı izi. Bozulma işareti: alt ajan dönüşünde gate bloğu (CLAUDE.md sızması); bloksuz rapor.
- **Bağımlılıklar:** İhtiyaç: S15-M2, T5 (CLAUDE.md içeriği, yükleme doğrulaması), T2 (rol dosyası). Besler: S1-M2, S14-M6, W1, W4.
- **Standart seviye kararı:** Gerekli (ilişkinin yazılı tanımı). "Alt ajanın gate koşması" gereksiz; koşulu: S15-M2 taşıyıcıları T2'nin rol dosyalarında ve görev tanımı şablonunda bulunuyor. Bütünsel etkisi: taşıyıcılar yoksa disiplin yalnız istemde yaşar (E89) ve alt ajan emir erine döner (E64); bu "gereksiz" kararı S15-M2'nin kabul testine bağlıdır. Önlediği hata: kural kayması; otomatik istemin onay sanılması (R07 BZ-5); sıkıştırmada kuralların özetten yürümesi (E34). Kabul testi: yukarıdaki üç gözlem.
- **Kaynak:** AGENT.md satır 13, 25, 40, 54–58, 160, 195–197 (kontrol katmanı metni; veri olarak); R01 repo ekseni SP01–SP08 ve "Süreklilik açıkları" (alt ajan raporu); R07 BZ-5 ve §4 madde 12; EkA-7, EkA-8, EkA-9; DECISIONS A-01, A-04; README "Sınırlar".
- **Bedel:** Batu'dan bir onay; geçici dönemde otomatik turlarda ~10 satırlık blok gürültüsü; sıkıştırma sonrası 50–100 KB yeniden okuma (R11 K23).

### 2.2 S2 — Batu ile iş birliği

**Amaç.** Batu'nun amaç, yetki ve kabul rolünü en az bilişsel yükle ve en yüksek dikkatle yapmasını sağlamak. Onu gizli koordinatör, mesaj taşıyıcı, arama motoru ya da teknik doğrulayıcı yapmamak. K-010 ile ikinci model hattı (A-03) kapandı. Aynı modelden türeyen denetçiler aynı kör noktayı paylaşır (R11 K106). Beş repo olayının dördünde hatayı Batu yakaladı ya da onarımı o başlattı (R11 §1 madde 2). Bu yüzden Batu'nun dikkati sistemin aynı modelden olmayan tek denetim kanalıdır ve S2 bir güvenlik alt sistemidir. Araba benzetmesindeki "konfor güvenliğin de parçasıdır" ilkesinin buradaki karşılığı şudur: yorgun ya da bilgisiz onay hata üretir.

**R11'e göre değişenler.**
- Eklendi: Batu'nun sözünün ayrıştırılması ve itiraz işleme (S10 ile arayüz); eşli ölçüler (R10 §4.8 madde 5); bildirim kanalı bilinmediği için sessiz alarm kuralı (S17-M3).
- Düzeltildi: A003'teki "düzenin gerçek başarı ölçüsü bu sayıdır" ifadesi. Hatırlatma sayısı hedef değil teşhis girdisidir (R11 Y13; R10 §1 madde 7).
- Sınır: Batu'ya teknik ya da süreç onayı gitmez. İstisnalar METHOD kabulü ve yapılandırma/kontrol değişikliğidir, çünkü Batu bunları açıkça istedi (K-005, K-007, A-04). Loopinance'ta Batu, düzen kurulum planının kendi işi olmadığını söylemişti: "Müşteri haklı olarak bunun kendi işi olmadığını söyledi." (EkA-2).

**Karar tablosu.**

| Bileşen | Karar | Önlediği hata | Kabul testi | Kaynak | Kart |
|---|---|---|---|---|---|
| Mesaj biçimi sözleşmesi | gerekli | uzunluk, yönün anlaşılmaması, sahte menü (E72); yazılı kuralın davranışa dönmemesi (R02 E3) | 10 mesaj örnekleminde bitiş biçimi ve sınırlar | R11 S2; A003 §3.9 | S2-M1 |
| Kontrol noktası ve aşama raporu | gerekli | özerk koşu görünmez; Batu commit okumak zorunda (E09) | Batu'nun "neredeyiz?" sorusu = 0 | R01 süreklilik açıkları | S2-M2 |
| Önerili soru kuyruğu; çerçeve istisnası | gerekli | sorular işi durdurur ya da kaybolur (E10); yanlış çerçeve geç fark edilir (Y11) | her soruda 10 alan dolu | K-002; R11 Y11 | S2-M3 |
| SHA'ya bağlı kabul paketi | gerekli | kabul törene döner (E07); Batu teknik doğrulayıcı olur (E70) | her kabulde SHA; sonraki değişiklik "bayat" işaretli | EkA-2; EkA-16 | S2-M4 |
| Dikkat bütçesi | gerekli | onay yorgunluğu; tek bağımsız kanalın zayıflaması (E08) | aşama başına kelime ve soru sınırı içinde | R09 MK-8 | S2-M5 |
| Bildirim kuralları | gerekli | sessiz başarısızlık (E82) | kırmızı alarm aynı turda gönderiliyor | R11 S2 | S2-M5 |
| Bildirim kanalı (cloud) | bilinmiyor | — | kanal pilotunun sonucu | EkA-11 | S2-M5 |
| Hatırlatma ve düzeltme kaydı | gerekli | Batu'nun taşıdığı iş görünmez (E11, E17) | her H kaydında tür, kaynak alt sistem, "sistem yakalayabilir miydi" | A003 §3.2; EkA-13 | S2-M6 |
| Eşli ölçüler | gerekli | Batu yorulunca düşen sayı başarı sanılır (Y13) | raporda sayı tek başına verilmiyor | R10 §4.8 | S2-M6 |
| Batu'nun sözünün ayrıştırılması ve yayılım tetiği | gerekli | kararın yanlış okunması (E47); örneğin kapsam sanılması (E51); kararın çalışan işe ulaşmaması (K-010 olayı) | her U-dosyasında ayrıştırma; çalışan iş varken kararlarda yayılım satırı | R10 §1 madde 8 | S2-M7 |
| İtiraz ve yeni yön işleme | gerekli | refleks katılım ya da inat (E72) | itiraz cevaplarında çürütme izi | user-independent-reasoning | S2-M7, S15-M3 |
| Bilişsel yükün doğrudan ölçümü | bilinmiyor | — | vekiller: okuma yükü, soru sayısı, cevap gecikmesi | R11 §7.1 soru 4 | S2-M5 |
| Ayrı pano | gereksiz (ayrı yüzey olarak) | — | bkz. S17-M4 | — | S17-M4 |
| Teknik ya da süreç onayını Batu'ya götürmek | gereksiz (istisnalar yukarıda) | — | Batu'nun "bu benim işim değil" tepkisi = 0 | EkA-2 | S1-M3 |

"Teknik/süreç onayı" gerekçesi. Koşul: karar Y katmanında değil. Bütünsel etki: Batu'nun dikkati korunur. Ama T kararları görünmez kalmamalıdır; dengeleyici otomatik seçim kaydıdır (S1-M3).

#### S2-M1 — Mesaj biçimi sözleşmesi
- **Ne:** Batu'ya giden her mesajın içerik sırasını, uzunluğunu ve üç bitiş biçimini sabitler.
- **Nerede:** METHOD iletişim bölümü; CLAUDE.md'de 5 satırlık özeti (T5). Şablon:

```
[Routing bloğu — AGENT.md sürdükçe]
**Sonuç:** <1–3 cümle: ne oldu, ne değişti>
**Kararı etkileyen belirsizlik:** <varsa en fazla 2 madde; yoksa satır yazılmaz>
**Haritadaki yer:** <A bitti, B'deyiz, C sonra>
**Senin adına verdiğim tercihler:** <varsa TK kimlikleriyle; yoksa satır yazılmaz>
<Bitiş: üçünden biri>
Şunu yapıyorum: <somut iş; bitince ne olacak>
Şunu bekliyorum; senden karar yok: <neyi, ne zamana kadar>
Karar gerekiyor; önerim: <tek öneri ve gerekçesi; seçenek yalnız gerçek çatalsa ve en fazla 2>
```

  Kurallar: Olağan ilerleme mesajı bloğu saymadan en fazla 200 kelimedir; ayrıntı dosyadadır, bağlantıyla verilir. Bulgu, kanıt ve açık iş her zaman söylenir; "ne yapayım?" menüsü yasaktır. Açık iş hafifletilmez ("paralel hallolur" denmez). "Doğrulandı" ve "artık net" yalnız S14-M2 sözlüğüne uyuyorsa yazılır.

  Örnek (bu turdaki K-010/R10 durumundan):
```
**Sonuç:** R07–R11 tamamlandı; beş küme taslağı için alt ajanlar çalışıyor.
**Kararı etkileyen belirsizlik:** K-010, R10 çalışırken alındı; R10 onu görmeden yazdı. Dönüşünü K-010'a göre ben uzlaştıracağım.
**Haritadaki yer:** P0.3 bitti, P0.4'teyiz, P0.5 sonra.
Şunu bekliyorum; senden karar yok: beş taslağın dönüşü. Sonra birleştirmeye geçiyorum.
```
- **Ne zaman:** Batu'ya giden her mesajda.
- **Kim:** Ana oturum.
- **Nasıl işler:** 1) Mesaj şablon sırasıyla yazılır. 2) Göndermeden önce üç denetim: bitiş biçimi var mı; kelime sınırı aşıldı mı (aşıldıysa ayrıntı dosyaya); menü ya da hafifletilmiş açık iş var mı. 3) Batu'nun uzunluk ya da anlaşılmazlık tepkisi H kaydına girer.
- **Zorlama düzeyi:** Yapısal (şablon). Zorlayıcı aday: Stop hook'u `last_assistant_message`in son paragrafının üç önekten biriyle başlamasını denetler, başlamıyorsa turu bir kez engeller; `stop_hook_active` döngüyü önler (Z3; T5; C! tek repolu oturum). Yararı ve gürültüsü pilotta ölçülür (bilinmiyor).
- **Çalıştığını nasıl anlarız:** Aşama sonunda rastgele 10 mesajda bitiş biçimi, kelime sınırı ve menü yokluğu. Batu'nun "uzun" ya da "anlamadım" tepkisi = 0 (H kaydı türü). Bozulma işareti: EXP-006'daki D010 örüntüsü, yani kural yazılı olduğu halde uzunluk şikâyeti (R02 E3).
- **Bağımlılıklar:** İhtiyaç: S1-M3 (tercih listesi), S17-M4 (gösterge satırı), T1 (Batu'nun terim sözlüğü). Besler: S2-M2, S15-M1 (#2, #3, #5, #10).
- **Standart seviye kararı:** Gerekli. Önlediği hata: sahte menü, aşırı sorma (E72); yazılı iletişim kuralının davranışa dönmemesi (R02 E3); "kısa" ile "görünmez"in karışması (Y1; dengeleyici S2-M2). Kabul testi: 10 mesaj örnekleminde üç denetimin hepsi geçiyor.
- **Kaynak:** A003 §3.9; R03 ilke 13, 16 ve §5 madde 8–9; EkA-6 (sahte seçenek makalesi: "kanıt/bulgu/gerçek açık-iş = her zaman serbest"; "\"ne yapayım?\" sahte menüsü = yasak"); EkA-1 (DEFO #5 sahte menü, #10 örtme); canonical-work-preflight §7'deki EXP-006 kısa iletişim sınırı: "Olağan ilerleme cevabını yaklaşık 150–250 kelimenin altında tut" (kontrol katmanı metni; EXP-006'ya özgüdür, burada tasarım seçimi olarak alındı); R02 E3.
- **Bedel:** Yazım disiplini. Hook seçilirse her tur bir betik ve arada bir düzeltme turu.

#### S2-M2 — Kontrol noktası raporu ve aşama raporu
- **Ne:** Özerk koşunun ne yaptığını, hangi kararların değiştiğini, Batu adına neyin seçildiğini ve nereye bakması gerektiğini, commit okumadan görmesini sağlar.
- **Nerede:** Sohbette kısa sürüm (en fazla 250 kelime); repoda tam sürüm `phases/<aşama>/raporlar/KN-<n>.md` (yol T1'in). Şablon (değerler kurgusal):

```
# Kontrol noktası KN-P1-03 — 2026-10-04 · önceki rapor: KN-P1-02 @ <SHA> · bu rapor @ <SHA>
## Bir cümle
<Bu dönemde ne değişti>
## Durum göstergesi (S17-M4)
- Son ilerleme olayı: 2026-10-04, TK-P1-006 kararı · o zamandan beri kapanan kalem: 0 · Alarm: yok
- Bu dönemde: kapanan soru 3 · verilen/değişen karar 4 · doğrulanmış teslimat 1 · kabul 0
- Maliyet (T5): alt ajanlar ≥ 1,2 M token (2 koşu bilinmiyor)
## Değişen kararlar
- TK-P1-004 … (neden, bağlantı) · TK-P1-006 …
## Senin adına verdiğim tercihler (itiraz edersen değişir)
- TK-P1-005 … — itiraz yoksa böyle kalır
## Senden istenen (varsa; en fazla 3)
- A-09: <soru> · önerim: …
## Açık işler ve riskler
- P1-019 KISMEN: canlı deneme yapılmadı, yalnız belge okundu
## Nereye bakmalısın (en fazla 2 bağlantı)
- <dosya#bölüm> — neden
```

  Aşama raporu aynı şablona şunları ekler: kalem denetimi özeti (S14-M7), söz–çıktı özeti (S14-M8), durak aşamasındaysa kabul paketi (S2-M4), retrospektif bağlantısı (T5 S21), gözlem sınırı paragrafı (S17-M5).
- **Ne zaman:** Her aşama sonunda. Özerk koşuda her 5 kapanan iş kaleminde ya da 24 saatte bir, hangisi önce gelirse (başlangıç değeri). Kırmızı alarmda (S17-M3). Batu sorduğunda.
- **Kim:** Ana oturum yazar; Batu okur.
- **Nasıl işler:** 1) Sayılar günlükten hesaplanır (S17-M1), elle yazılmaz. 2) Değişen kararlar ve tercihler karar kaydından çekilir. 3) Açık işler kalem denetiminden gelir. 4) Sohbete özet ve bağlantı gider; tam metin commit'lenir.
- **Zorlama düzeyi:** Yapısal (şablon). Zorlayıcı aday: aşama "TAMAM" işaretlenmeden önce rapor ve kapanış dosyasının varlığının denetimi (Z4).
- **Çalıştığını nasıl anlarız:** Batu'nun "ne oldu?" ya da "neredeyiz?" sorusu = 0. Batu'nun sonraki mesajının rapordaki bir bölüme atıfla gelmesi, raporun okunduğunun işaretidir. Günlükte kontrol noktası aralığı aşılmamış.
- **Bağımlılıklar:** İhtiyaç: S17-M1, S17-M4, S1-M3, S14-M7, T1 (rapor klasörü). Besler: S2-M4, S2-M6 (Batu'nun tepkileri).
- **Standart seviye kararı:** Gerekli. Önlediği hata: özerk koşunun görünmezliği (E09); "kısa" ile "görünmez"in karışması (Y1). Kabul testi: her aşamada rapor var ve sayıları günlükle tutarlı.
- **Kaynak:** R11 S2 bileşen 2; R01 süreklilik açıkları: "Batu cannot audit what happened across unattended steps without reading commits. That is the reading burden D010 was meant to remove." (kaynak diyor; alt ajan raporu); R01 SP13; EkA-2 ("Senden okumanı isteyeceğim tek belge bu."); R09 MK-8.
- **Bedel:** Kontrol noktası başına ~1 sayfa. Batu için okuma süresi 3 dakikanın altında olmalı (varsayım).

#### S2-M3 — Soru kuyruğu
- **Ne:** Batu'ya gidecek her soruyu önerisi, etkisi ve etkilediği kalemlerle kaydeder. Çerçeve sorularını hemen, diğerlerini kontrol noktasında toplu gönderir. İş durmaz.
- **Nerede:** Tek kaynak için önerim: DECISIONS.md'deki "Açık sorular" tablosu genişletilir (bugün A-01…A-07 orada duruyor; cevaplanınca aynı dosyada K-xxx olur). Ayrı SORULAR.md de olabilir; yeri T1 seçer. Genişletilmiş satır örneği:

```
| ID | Soru (sade) | Sınıf | Neden sana | Önerim ve gerekçe | Etkilediği kalemler | Cevap gelmezse | Açıldı | Gönderildi | Durum |
|---|---|---|---|---|---|---|---|---|---|
| A-08 | Sürekli yetki (K-002) yeni haritada hangi geçişleri kapsasın? | çerçeve | Yetki zarfı Y katmanında; tahminle doldurmak yetki uydurmak olur (R01) | K-002'deki "P4 kabul durağı" yeni haritadaki tasarım kabulü aşamasına, öncesi kendiliğinden geçişlere eşlensin | P1 açılışı; STATE Yetki bloğu | P0 işleri sürer; P1'e geçilmez | 2026-09-27 | METHOD sunumuyla | açık |
```

  Kurallar:
  - Tek soru, tek öneri. Gerçek çatal değilse seçenek sunulmaz; gerçek çatalsa en fazla 2 seçenek ve önerilen.
  - Sınıflar: çerçeve (hemen) · erişim/yetki (hemen; iş başka kalemlerde sürer) · tercih (toplu) · kabul (durakta).
  - Çerçeve sorusu: cevabı yanlış çıkarsa sürmekte olan en az bir kalemin ya da aşamanın öncülünü geçersiz kılacak soru. Biriktirilmez.
  - Kontrol noktası başına en fazla 3 soru (S2-M5). Fazlası etki ve geri alınamazlığa göre sıralanır; gerisi kuyrukta kalır.
  - "Cevap gelmezse" alanı zorunludur. Varsayımla sürdürülen kalemler "varsayım: A-08 önerisi" diye işaretlenir. Geç cevap gelince bu kalemler yeniden değerlendirilir.
  - Cevap gelince Batu'nun sözü birebir kaydedilir (T1), soru K-xxx'e dönüşür (S2-M7), etkilenen kalemler güncellenir.
- **Ne zaman:** Soru doğunca (S1-M3'ün 5. yolu); gönderim sınıfa göre.
- **Kim:** Ana oturum.
- **Nasıl işler:** 1) Satır açılır, 10 alan doldurulur. 2) Çerçeve ve erişim soruları aynı turda S2-M1 biçimiyle gönderilir. 3) Tercih soruları bir sonraki kontrol noktası raporunda gider. 4) Cevap gelince kapanış adımları uygulanır; günlüğe SORU-KAPANDI (ilerleme olayı) yazılır.
- **Zorlama düzeyi:** Yapısal (zorunlu alanlar). Zorlayıcı parça yok; alanların doluluğu aşama sonunda denetlenir.
- **Çalıştığını nasıl anlarız:** Her soruda 10 alan dolu. Çerçeve sorularının açıldıkları gün gönderildiği günlükten görülüyor. Cevaplanan sorularda etkilenen kalemlerin güncellendiği görülüyor. Bozulma işareti: aylarca açık kalan tercih sorusu; Batu'nun "bunu neden şimdi soruyorsun" ya da "bunu neden sormadın" tepkisi.
- **Bağımlılıklar:** İhtiyaç: S1-M3, S2-M5, T1 (DECISIONS biçimi), T3 (kalem bağları). Besler: S2-M2, S2-M7, S1-M2 (Y5, Y6).
- **Standart seviye kararı:** Gerekli. Önlediği hata: sahipsiz ya da kaybolan sorular (E10); yanlış çerçevenin uzun süre fark edilmemesi (Y11; EXP-006'da çerçeve 17 dilim boyunca düzeltilmedi, R11 K46); sahte menü (E72). Kabul testi: yukarıdaki üç gözlem.
- **Kaynak:** K-002 ("Sorular biriksin, iş durmasın."); A003 §3.1, §3.9; R11 S2 bileşen 3, Y11; R01 SP10 (biriktirme kuralı önerisi); EkA-4 (urunci.md: "Tek soru, tek öneri; seçenek menüsü sunma."; "etkisiyle (sayı örneği)"); R03 §4 gerilim 5.
- **Bedel:** Soru başına ~1 satır bakım; geç cevapta yeniden iş.

#### S2-M4 — Kabul protokolü ve kabul paketi
- **Ne:** Batu'nun kabulünü, teknik doğrulamadan ayrı ve belirli bir commit SHA'sına bağlı bir karar olarak kaydeder. Kabulden sonra değişen içerik kabulü bayatlatır.
- **Nerede:** Durak aşamasının klasöründe `KABUL.md` (yol T1'in) ve DECISIONS'ta bir K satırı. Şablon (değerler kurgusal):

```
# Kabul paketi — P0 METHOD v1
- Kabul nesnesi: explorations/EXP-007-devos-claude-calisma-duzeni/METHOD-v1.md @ 3f9c2e1
- Kabul ölçütleri (işten önce yazıldı; K-007): 1) bağlam, bellek, kalıcı roller, en iyi uygulamaya dayalı yöntem · 2) A003'teki her vaadin "nasıl"ı · 3) standart seviye · 4) bütünsel etkileşim
- Ölçüt başına durum (S14-M2 sözlüğüyle):
  1) mekanik kontrol: 21/21 alt sistemde kart var · karşı-okuma (aynı model, P0.5 E1): çürütülemedi
  2) söz–çıktı matrisi: 27 madde → 25 "nasıl", 2 "kısmen" (bağlantı)
- Teknik doğrulama durumu (ayrı satır): bağımsız doğrulama yapılmadı; canlı deneme yapılmadı; pilotlar P0.7'de
- Bilinen açıklar: …
- Senin adına verilen tercihler: TK-P0-003, TK-P0-007, …
- Önerim: kabul et / şu değişiklikle kabul et
- Batu'nun cevabı (birebir; kaynak U0xx): …
- Kayıt: "Kabul: P0 METHOD v1 @ 3f9c2e1" → DECISIONS K-0xx
```

  Batu'nun kabul biçimi: serbest cevap yeter. "Tamam" gibi kısa bir cevap, paketin başındaki SHA'ya bağlı kabul sayılır ve birebir kaydedilir. Paketten sonra nesne değiştiyse kabul "bayat" işaretlenir ve fark (git diff özeti) Batu'ya gösterilir.
  Kapsam: kabul paketi yalnız duraklarda hazırlanır. Kendiliğinden geçen aşamada aşama raporu yeter; o aşamanın çıktıları B katına ancak sonraki durağın kapsayıcı paketiyle ulaşır.
- **Ne zaman:** Her durakta (METHOD kabulü, tasarım kabulü, kurulum yetkisi).
- **Kim:** Ana oturum hazırlar; kabul eden yalnız Batu.
- **Nasıl işler:** 1) Kapanış kapısı (S14-M7) geçilir. 2) Paket nesnenin SHA'sıyla yazılır. 3) Sohbete özet ve öneri gider. 4) Cevap birebir kaydedilir, K satırı açılır, kat B işaretlenir. 5) Sonraki her commit'te `git diff <SHA>..HEAD -- <nesne>` boş değilse kabul "bayat" olur.
- **Zorlama düzeyi:** Yapısal (şablon); mekanik denetim (git diff), betiği T5'in; zorlayıcı değil.
- **Çalıştığını nasıl anlarız:** Her kabulde SHA var. Kabulden sonraki değişikliklerde "bayat" işareti var. Kabul paketlerinde "bilinen açıklar" ve "Önerim" hiç boş değil (itirazsız mühür akışına karşı). Batu'nun kabulden sonra bulduğu açık sayısı eşli ölçüdür (S2-M6).
- **Bağımlılıklar:** İhtiyaç: S14-M2, S14-M7, S14-M8, S1-M3, T1. Besler: S1-M1 (kabul hakkı), S17-M2 (KABUL olayı), S2-M6.
- **Standart seviye kararı:** Gerekli. Önlediği hata: kabulün törene dönmesi (E07; loopinance: "Onaylar seremoniye döndü. Mühürler itirazsız geçti."); Batu'nun teknik doğrulayıcıya dönüşmesi (E05, E70); yayın ile içerik kimliğinin karışması (EXP-005 D06). Kabul testi: yukarıdaki üç gözlem.
- **Kaynak:** R11 S2 bileşen 4, E05, E07; EkA-2 (ders 8); EkA-16 (EXP-004 Q15: "Pozitif kullanıcı değerlendirmesi teknik doğrulama veya belirsiz her tasarım seçiminin onayı sayılmaz."); R05 satır 13; R04 (d)2; R09 GZ-3: "validity is evaluated relative to the **object actually reviewed**" (kaynak diyor; gstack).
- **Bedel:** Durak başına bir paket (~1 sayfa); Batu'dan bir cevap.

#### S2-M5 — Dikkat bütçesi ve bildirim kuralları
- **Ne:** Batu'nun okuma ve karar yükünü sınırlar: neyi okuması gerektiğini, neyi okumasına gerek olmadığını, ne zaman ve hangi kanaldan bildirim alacağını belirler.
- **Nerede:** METHOD iletişim bölümü. İçerik (başlangıç değerleri; Batu değiştirebilir):

```
### Dikkat bütçesi
Okuması gerekenler: aşama raporu ve kabul paketi (aşama başına en fazla 2 sayfa); çerçeve soruları; kırmızı alarm mesajı.
Okuması gerekmeyenler: çalışma günlüğü, alt ajan dönüşleri, araştırma notları, küme taslakları, bulgu kayıtları. Hepsi bağlantıyla erişilebilir; zorunlu değil.
Soru sınırı: kontrol noktası başına en fazla 3; çerçeve ve erişim soruları sınır dışı.
Kelime sınırı: olağan mesaj 200; kontrol noktası özeti 250; aşama raporu özeti 400 (tamamı dosyada).
Aşama başına Batu'ya giden toplam okuma: yaklaşık 1.500 kelimenin altında.
Dil: raporda Batu'nun kendi terimi kullanılır (S10 sözlüğü; ör. "motivasyon", "standart seviye", "yeterli seviye").

### Bildirim kuralları
Hemen: çerçeve sorusu; kırmızı takılma alarmı; Y2, Y3, Y4, Y11 tetikleri; bütçe eşiği (T5).
Toplu (kontrol noktasında): tercih kararları; tercih soruları; sarı alarmlar ve nasıl kapandıkları.
Aşama sonunda: aşama raporu; durakta kabul paketi. Kendiliğinden geçişte de rapor gider (K-002).
Hiç: rutin ilerleme; alt ajan başlama ve bitişleri; mekanik kararlar.

### Kanal (bilinmiyor → pilot)
1. Oturum mesajı (varsayılan). Cloud oturumları mobil uygulamadan izlenebilir (belge); Batu'ya kendiliğinden bildirim gidip gitmediği bilinmiyor.
2. Routine bildirimi (push ya da e-posta). Yalnız her tetikte yeni oturum açan Routine'lerde; araç açıklamasında var, belgede doğrulanmadı, denenmedi; her kullanımda yeni oturum açar (maliyet). Y3 → Batu onayı.
3. E-posta (bu oturumda Gmail bağlayıcısı görünüyor): dış etki; Y3 → Batu onayı.
```
- **Ne zaman:** Her mesaj ve rapor yazımında (bütçe); her tetikte (bildirim).
- **Kim:** Ana oturum uygular. Bütçe değerleri Batu'nun tercihidir: METHOD sunumunda tek soru olarak gider (T4-Q4).
- **Nasıl işler:** 1) Rapor yazılırken sınırlar uygulanır; aşan kısım dosyaya gider. 2) Tetik olunca bildirim tablosuna bakılır. 3) Aşama sonunda Batu'ya giden toplam kelime ve soru sayısı günlükten hesaplanıp raporda gösterilir.
- **Zorlama düzeyi:** Yapısal ve tavsiye. Kelime sayımı mekanik yapılabilir (betik); zorlayıcı değil.
- **Çalıştığını nasıl anlarız:** Aşama başına Batu'ya giden okuma yükü ve soru sayısı sınırın içinde. Batu'nun "bunu bana neden gönderdin" ve "bunu bana neden söylemedin" tepkileri ayrı H türleri olarak sıfır. Kırmızı alarmın gönderildiği tur ile alarmın doğduğu tur aynı.
- **Bağımlılıklar:** İhtiyaç: S17-M3 (alarmlar), S2-M3, T1 (terim sözlüğü), T5 (bütçe eşiği, kanal pilotu). Besler: S2-M1, S2-M2.
- **Standart seviye kararı:** Dikkat bütçesi gerekli: önlediği hata onay yorgunluğu ve tek bağımsız denetim kanalının zayıflaması (E08; R09 MK-8); kabul testi yukarıda. Bildirim kuralları gerekli: önlediği hata sessiz başarısızlık (E82). Kanal bilinmiyor; nasıl bilinir hale gelir: P0.7/P1 pilotunda üç kanal Batu'nun izniyle denenir. Bütünsel etkisi: kanal bilinmedikçe fren sinyali Batu'ya ulaşmayabilir; dengeleyici S17-M3'teki sessiz alarm kuralıdır.
- **Kaynak:** R11 S2 bileşen 6–7, §7.1 soru 2 ve 4; R09 MK-8 ("Onay yorgunluğu; Batu'nun gizli koordinatöre dönüşmesi"); R03 ilke 16 ve §3; EkA-2 ("Senden okumanı isteyeceğim tek belge bu."); EkA-11 (mobile.md ve claude-code-on-the-web.md; C+/C?); create_trigger aracının açıklaması (gözledim: bu oturumun araç listesi; denenmedi); R01 "Açık sorular" son madde.
- **Bedel:** Yazım disiplini; kanal pilotu için bir deneme; Batu'dan bir tercih.

#### S2-M6 — Hatırlatma ve düzeltme kaydı, eşli ölçüler
- **Ne:** Batu'nun sisteme yaptığı her hatırlatmayı, düzeltmeyi ve yakaladığı hatayı türü ve kaynak alt sistemiyle kaydeder. Sayıyı hedef değil teşhis girdisi yapar; vekil ölçü tuzağına karşı Batu'dan bağımsız eşli ölçülerle birlikte okur.
- **Nerede:** `HATIRLATMALAR.md` (EXP-007 düzeyinde; yol T1'in). Bu turdan gerçek satırlarla:

```
| ID | Tarih | Batu'nun sözü (kaynak) | Tür | Kaynak alt sistem | Sistem yakalayabilir miydi? Hangi mekanizma? | Neden analizi (S15-M4) | Karşılık | Durum |
|---|---|---|---|---|---|---|---|---|
| H-001 | 2026-09-27 | "yapıyı basit tutmuşsun … sözde geniş kapsam ama çıktıda "yeterli seviye" şeklinde bir yaklaşımın var" (U004) | kapsam daraltma (söz–çıktı açığı) | S14, S15, S4 | Evet: söz–çıktı matrisi ve standart–yeterli denetimi (S14-M8, S14-M9); v0'da yoktu (R11 §6) | yakın neden: v0'ın kapsamı okunan araştırmanın kapsamını izledi (R11 §6, çıkarım) · önleme açığı: envanter adımı yoktu | P0.3 envanteri (R11); bu küme taslakları | karşılık kuruldu; davranış değişimi doğrulanmadı |
| H-002 | 2026-09-27 | "sen ayrı branch'ta çalış o zaman çakışma olmaz." (U005) | yön/yetki (dal politikası) | S1, S9, S18 | Kısmen: main'e dokunan çakışma çözümü bir Y3 (dış etki) adımıydı; zarf olsaydı soru olarak giderdi | yakın neden: main'i dala birleştirerek çakışma çözülmeye başlandı · önleme açığı: dal politikası yazılı değildi | K-009; S1-M2 Y3 | kuruldu |
```

  Ne sayılır: Batu'nun, sistemin kendi başına yapması ya da bilmesi gereken bir şeyi söylemesi (eksik iş, eksik kaynak, bayat durum, yanlış yön, unutulan karar, uzunluk ya da biçim, erişim, yayın kontrolü). Ne sayılmaz: yeni amaç ya da tercih beyanı, sorulan soruya cevap, kabul.

  Eşli ölçüler (aşama raporunda birlikte verilir):

| Ölçü | Tanım | Neyi dengeler |
|---|---|---|
| Hatırlatma sayısı ve türü | H kayıtları | gizli koordinasyon yükü |
| Sistemin kendi yakaladığı hata sayısı ve türü | karşı-okuma, kaynak kontrolü, mekanik kontrol ve alt ajan bildirimlerinin bulguları (akıbetli) | Batu yorulunca düşen sayı (vekil kusuru) |
| Kabulde Batu'nun bulduğu açık | kabul paketine Batu'nun eklediği itirazlar | itirazsız mühür |
| Kaçak oranı | H kayıtlarında "sistem yakalayabilirdi" denenlerin payı | hangi mekanizmanın çalışmadığı |
| Erken uyarılar | yayılım uyuşmazlıkları (T1), kimseye verilmemiş iş bulguları (T3), sarı alarmlar (S17) | ölçünün gecikmesi |
| Soğuk başlangıç sonucu | taze oturumun cevaplarının Batu'nun niyetiyle karşılaştırılması (T5 S18) | Batu'dan bağımsız süreklilik ölçüsü |
| Sessizlik | Batu'nun mesaj atmadığı süre ve raporların okunup okunmadığı işareti | "hatırlatma yok = başarı" yanılgısı |

  Sistemin kendi yakaladığı gerçek örnekler: R10 ajanı K-010'un kendisine iletilmediğini sürüm bağını kaydederken fark etti (R10 §1 madde 8, gözledim); ana oturum "alt ajanlar üç kat iç içe çalışabilir" iddiasını ortamda sınayıp düzeltti (A003 §3.3).
- **Ne zaman:** Batu'nun her mesajından sonra (S2-M7'nin ilk adımı sınıflar); aşama sonunda analiz ve eşli ölçü tablosu.
- **Kim:** Ana oturum kaydeder ve analiz eder; Batu'dan etiketleme istenmez.
- **Nasıl işler:** 1) Mesaj ayrıştırılırken hatırlatma ya da düzeltme varsa H satırı açılır. 2) Aynı gün "sistem yakalayabilir miydi" ve kaynak alt sistem doldurulur. 3) Kısa neden analizi yapılır (S15-M4). 4) Karşılık ders kaydına gider (T5 S21). 5) Aşama raporunda sayı eşli ölçülerle birlikte verilir.
- **Zorlama düzeyi:** Yapısal (şablon); tavsiye (neyin hatırlatma sayılacağı yargısı).
- **Çalıştığını nasıl anlarız:** Raporda sayı hiçbir zaman tek başına verilmiyor. Her H satırında "sistem yakalayabilir miydi" ve karşılık dolu. Aynı türde ikinci H kaydı, önceki karşılığın çalışmadığını gösterir (T5).
- **Bağımlılıklar:** İhtiyaç: S2-M7, S15-M4, S14 bulguları, T3 (keşif kökeni kaydı), T5 (ders kaydı, soğuk başlangıç). Besler: S15-M1 (defo türleri), T5 S21, S2-M2.
- **Standart seviye kararı:** Gerekli; eşli ölçüler de gerekli. Önlediği hata: Batu'nun taşıdığı keşif yükünün görünmezliği (E11, E17); vekil ölçü tuzağı (Y13); aynı şeyin yeniden anlatılması (E99). Kabul testi: yukarıdaki üç gözlem.
- **Kaynak:** A003 §3.2: "Bana yaptığın her hatırlatma bir kusur olarak kayda geçer; düzenin gerçek başarı ölçüsü bu sayıdır." (v0); R10 §4.8 madde 5: Foundation'ın "fewer reports because reporting declines" uyarısı (kaynak diyor; kavramsal analiz); R11 S2 bileşen 5, Y13, §4.5 ("Batu bir havuz"); EkA-13 (EXP-005: "... kullanıcıdan geldi."); R03 ilke 4; ORTAK-SENTEZ "Vekil ölçü".
- **Bedel:** Mesaj başına kısa bir sınıflama; H satırı başına ~5 dakika analiz; aşama başına bir tablo.

#### S2-M7 — Batu'nun sözünün kayda geçişi, itiraz ve yeni yön
- **Ne:** Batu'nun her mesajı birebir kayda alındıktan sonra (T1 S10) içindeki kararı, kısıtı, tercihi, örneği, soruyu ve itirazı ayırır ve doğru yüzeye taşır. Karar varsa yayılım tetiğini başlatır.
- **Nerede:** `sources/conversation/U0xx.md`'nin sonundaki mevcut "Karşılığında yapılan" bölümü genişletilir; kararlar DECISIONS'a gider; işlem günlüğe yazılır. Şablon (U005 için doldurulmuş):

```
**Ayrıştırma (S2-M7):**
- Karar: "sen ayrı branch'ta çalış o zaman çakışma olmaz." → K-009 · kapsam: EXP-007'nin dalı; main'e birleştirme askıda
- Claude'un uygulama yorumu (Batu'nun sözü değil): "Dal yalnız EXP-007 klasörüne dokunur" (T-ORTAK bunu ayrıca işaretledi)
- Kısıt: — · Tercih: — · Örnek (kapsam değildir): —
- Doğurduğu açık soru: A-07 (EXP-007 ne zaman main'e birleşecek?)
- İtiraz mı: evet, birleştirme adımına → S15-M3: pozisyon değişti; gerekçe: dal politikası Y katmanı, Batu'nun yetkisi
- Etkilenen yüzeyler: STATE "Oturum ve ortam notları"; PR #34 · Çalışan alt ajan: yok
- Yayılım: STATE güncellendi; kataloğa eklenen satır geri alındı (U005 "Karşılığında yapılan")
```

  Yayılım tetiği (W6): 1) DECISIONS satırı. 2) Günlükteki açık dağıtımlar listelenir (DAGITIM var, DONUS yok). 3) Her çalışan alt ajan için ya bildirim yapılır (T2 S12'nin mekanizması) ya da "dönüşü K-xxx'e göre uzlaştırılacak" işareti konur. 4) Bağlı dosyalar güncellenir (T1 S9'un yayılım kontrolü). 5) Günlüğe "YAYILIM: n yüzey, m çalışan iş" satırı yazılır.
  Belirsiz söz: Batu'nun kendi statü işaretleri korunur ("hayal ettiğim için yazdım", "kesin olarak savunmuyorum": R03 §4 gerilim 4). Örnek kapsam sayılmaz. Karar mı tercih mi belli değilse en yüksek bilgi değeri taşıyan tek soru, önerisiyle sorulur (decision-critical-assumptions "Bilgi Toplama İlkesi").
- **Ne zaman:** Batu'nun her mesajında, aynı iş içinde.
- **Kim:** Ana oturum. Birebir depolama ve statü etiketi sözlüğü T1'in (S10).
- **Nasıl işler:** 1) Mesaj birebir kaydedilir (T1). 2) Ayrıştırma bölümü doldurulur. 3) Karar varsa K satırı ve yayılım tetiği. 4) İtiraz varsa S15-M3. 5) Hatırlatma varsa S2-M6. 6) Tercih ya da soru varsa ilgili yüzeye gider.
- **Zorlama düzeyi:** Yapısal (U-dosyası şablonunda zorunlu bölüm). Zorlayıcı aday: kaynaksız K satırının yazımını engelleyen Z5.
- **Çalıştığını nasıl anlarız:** Her U-dosyasında ayrıştırma var. K kararlarının hepsi birebir kaynağa bağlı. Çalışan iş varken alınan her kararda YAYILIM satırı var ve her açık dağıtım için bir karşılık yazılı. Bozulma işareti: K-010/R10 türü olay (çalışan işin karardan habersiz sürmesi) ya da Batu'nun "ben bunu öyle demedim" tepkisi.
- **Bağımlılıklar:** İhtiyaç: T1 (S10 birebir depo ve statü etiketi; S9 yayılım kontrolü), T2 (çalışan alt ajana bildirim; geç dönüşün uzlaştırılması), S15-M3, S2-M6. Besler: S1-M4, S1-M2 (zarf sürümü), W6, W8.
- **Standart seviye kararı:** Gerekli. Önlediği hata: düzeltmelerin parafrazda yaşayıp kararların yanlış okunması (E47); örneğin kapsam sanılması (E51); kararın çalışan işe ulaşmaması (ORTAK-SENTEZ "Karar yayılmadı"). Kabul testi: yukarıdaki üç gözlem.
- **Kaynak:** DECISIONS kuralı ("Bir karar yalnız Batu'nun sözüne dayanır"); R11 S10 bileşen 1 (statü etiketi; sahibi T1); R03 §4 gerilim 4; R10 §1 madde 8 ("Görev tanımım bu kayıttan önceydi ve değişikliği bana hiçbir kanal bildirmedi.", gözledim; alt ajan); U005 ve bağlam notu; T-ORTAK.
- **Bedel:** Batu'nun mesajı başına 5–10 satır; kararda yayılım taraması.

### 2.3 S14 — Kalite güvencesi ve doğrulama

**Amaç.** Ölçütü önceden koymak; çıktıyı üretenden ayrı bir yolla sınamak; tamamlanma katlarını ayırmak; kanıt gücünü adıyla söylemek; kontrolün ağırlığını riske bağlamak. Aynı modelin karşı-okuması doğrulama sayılmaz. S14 en çok etkilenen alt sistemdir (12 giriş, R11 §4.3). Doğrulama yalnız kendisine verileni sınayabilir; ne yakalayabileceğini girdileri belirler: plandaki iş kapsamı (S4), özetin sadakati (S10), okuma iddiası (S6), birleştirme (S12), dönüş biçimi (S13). Bu girdilerin sahibi diğer kümelerdir; bu yüzden S14'ün kartları onlara açık arayüz ister (§3).

**R11'e göre değişenler.**
- Eklendi: söz–çıktı matrisi ve söz kaydı; standart–yeterli denetimi; risk sınıfının açık ölçütleri (aşağı akış yükü dahil); dönüş kapısı.
- Düzeltildi: BMAD'in "en az on somut bulgu" şartı (R08 O21) ile Anthropic'in "bulgu aramaya ayarlanan inceleyici iş sağlam olsa bile bulgu raporlar" uyarısı (R07 BD-5) çelişiyor. Çözüm: asgari bulgu sayısı yok; her hata sınıfı için "denendi, nasıl arandı, bulgu var/yok" izi zorunlu.
- Düzeltildi: R07 BZ-3'teki "SubagentStop girdisinde `last_assistant_message`" önerisi bu ortamda yetmez. Alt ajanlar raporu `SubagentHandback` aracıyla teslim ediyor (gözledim, EkA-18); rapor o aracın `tool_input.message` alanındadır (EkA-10).

**Karar tablosu.**

| Bileşen | Karar | Önlediği hata | Kabul testi | Kaynak | Kart |
|---|---|---|---|---|---|
| Önceden yazılı ölçüt ve ölçüt bütünlüğü | gerekli | sonucu gördükten sonra ölçüt değiştirmek (K62); erken zafer | 5 kalemde ölçüt dönüşten önce yazılmış | R11 S14; R07 BD-1 | S14-M1 |
| Tamamlanma katları | gerekli | sahte kapanış (E69) | raporda kat ve kanıt | A003 §3.8; R05 satır 13 | S14-M2 |
| Bağımsızlık etiketleri; "doğrulandı"nın sınırı | gerekli | etiket şişmesi (Y6) | "doğrulandı" geçen her yerde etiket | verification-independence §11 | S14-M2 |
| Risk sınıfı → kontrol ağırlığı | gerekli | ya tören ya kontrolsüzlük (E15, Y7) | R3 kalemlerde eksik set yok; R0'da çürütücü yok | R07 BD-7 | S14-M3 |
| Genel "tekrar kontrol et" talimatı | gereksiz (zararlı) | aşırı doğrulama (R07 P-O5) | görev tanımlarında yok | R07 BD-7 | S14-M3 |
| Ayrı girdili çürütücü inceleme | gerekli (R2/R3) | öz-onay (E67) | R2/R3 kalemlerde inceleme dosyası | R05 satır 11 | S14-M4 |
| Uç durum ve rakip hipotez araması | gerekli (çürütücü görev tanımında) | tek makul açıklamada durmak (R07 BD-6) | inceleme dönüşünde rakip açıklama alanı | R07 BD-6 | S14-M4 |
| Bulgu akıbeti ve tur sınırı | gerekli | bulguların kaybı; sonsuz döngü ya da sessiz kapanış (Y8) | akıbetsiz bulgu yok | R11 S14; A003 §3.7 | S14-M4 |
| Hata duyarlılığı sınaması (rol sürümü başına) | gerekli; her incelemede gereksiz | ayırt edemeyen denetçi (E68) | kalibrasyon kaydı var | EkA-14 | S14-M5 |
| Dönüş kapısı ve kaynaktan kontrol | gerekli | yanlış iddianın karara girmesi (E63) | kapıdan geçmeden K katına çıkan dönüş yok | A003 §3.3 | S14-M6 |
| Kalem denetimi | gerekli | sessiz toptan onay | kapanışta her kalem ayrı satır | R05 satır 12 | S14-M7 |
| Kimseye verilmemiş iş (kapanışta) | gerekli; yöntemi T3 S4 | doğrulama yalnız plandakini sınar (E19) | kapanış dosyasında tarama bölümü | A003 §3.8 | S14-M7 |
| Bütünsel inceleme | gerekli (çok parçalı çıktıda) | parçalar sağlam, bütün yanlış (E56) | R3 çıktıda nesnenin tamamı incelendi | R11 S14 | S14-M7 |
| Söz–çıktı izlenebilirliği | gerekli | söz geniş, çıktı dar (U004; H-001) | "karşılanmadı" satırları açıkça yazılı | U004; T4.md | S14-M8 |
| Standart–yeterli denetimi | gerekli | gerekçesiz "gereksiz"; "şimdilik yeter" | her "gereksiz"de 4 alan | R10 §2.3 | S14-M9 |
| Farklı model ya da sağlayıcıdan doğrulayıcı | bilinmiyor | — | pilotta maliyet/fayda | K-010; A-03 | §6 |
| Soğuk başlangıç testi | gerekli; sahibi T5 (S18) | sürekliliğin yalnız okumayla sınanması (K62) | aşama sonunda bir koşu | A003 §6 | S14-M2 (tür) |

"Farklı model" gerekçesi: A-03 K-010 ile kapandı; ChatGPT hattı yok. Farklı bir Claude modeli aynı sağlayıcının eğitim soyundan gelir; bağımsızlığı kısmi olur (varsayım). Bağımsızlığın gerçek kaynakları yöntem ve kanıt ayrılığıdır: mekanik kontrol, kaynaktan kontrol, canlı gözlem, soğuk başlangıç (verification-independence §3: "farklı ve bağımsız kaynak kullan … deterministik ya da dış oracle kullan"). Bütünsel etkisi: model bağımsızlığı yoksa S2'nin ağırlığı artar; bu taslağın S2'yi güvenlik alt sistemi olarak kurmasının gerekçesi budur.

#### S14-M1 — Ölçüt önce ve ölçüt bütünlüğü
- **Ne:** Her iş kaleminin bitti tanımı ve kabul testleri iş başlamadan yazılır. Sonuç görüldükten sonra değişen ölçüt "post-hoc" etiketi alır; taze kanıtla sınanmadıkça doğrulama sayılmaz.
- **Nerede:** Kalem kaydı (T3 S5 şeması) içinde üç zorunlu alan. Bu taslağın kendi kalemiyle örnek:

```
Kalem P0.4-T4
- Bitti tanımı (görev tanımıyla yazıldı: briefs/T4.md @ 8e82c34): S1, S2, S14, S15, S17 için amaç, bileşenler, karar tablosu ve mekanizma kartları; arayüzler; W1–W10 katkısı; Batu onayı gerektirenler; açık sorular.
- Kabul testleri:
  (1) mekanik: beş alt sistemde "Karar tablosu" başlığı var
  (2) mekanik: her kartta 11 alan başlığı var
  (3) söz–çıktı: T4.md "Özellikle karara bağlanacaklar"ın her maddesine en az bir kart ya da tablo satırı karşılık geliyor (§2.6.4)
  (4) çürütücü (R2): soyut kalan vaat (H3) ve gerekçesiz "gereksiz" (H4) bulgusu yok
- Ölçüt değişikliği: yok · olursa: "tarih — hangi test — neden — post-hoc: evet — taze kanıt: …"
Araştırma kalemi (bitiş önceden bilinemiyorsa): bitti tanımı yerine "durma ölçütü" ve "dönüş koşulu" yazılır: "Ek okuma kararı değiştirmeyecekse dur; bütçe bitince 'park', 'bitti' değil."
```
- **Ne zaman:** Kalem açılırken, dağıtımdan önce; ölçüt değişirse değişiklik anında.
- **Kim:** Ana oturum yazar. Kalem alt ajana gidiyorsa ölçüt görev tanımına aynen girer (S15-M2 b).
- **Nasıl işler:** 1) Üç alan dolmadan DAGITIM yapılmaz. 2) Dönüş gelince testler uygulanır. 3) Test değişecekse değişiklik satırı yazılır, eski test silinmez. 4) Post-hoc etiketli sonuç Ç katına sayılmaz; taze kanıt gerekir.
- **Zorlama düzeyi:** Yapısal (zorunlu alan). Zorlayıcı aday önerilmez: tasarım işinde testlerin çoğu yargı ister; hook yalnız mekanik koşula kurulur (R07 BZ-7). Mekanik testler (grep) kalemin içinde koşulur.
- **Çalıştığını nasıl anlarız:** Kalem kayıtlarında bitti tanımının tarihi dönüşten önce. Post-hoc değişiklik oranı raporda. Bozulma işareti: bitti tanımı iş bittikten sonra yazılmış kalem; testi geçecek biçimde gevşetilmiş ölçüt.
- **Bağımlılıklar:** İhtiyaç: T3 (kalem şeması), T2 (görev tanımı şablonu). Besler: S14-M2, S14-M4, S14-M7, S17-M2.
- **Standart seviye kararı:** Gerekli. Önlediği hata: sonucu gördükten sonra ölçüt değiştirmek (R11 K62); erken zafer ilanı (R07 §3); bitiş ölçütü yokluğundan doğan sahte menü ve şişme (A4). Kabul testi: rastgele 5 kalemde üç alan dönüşten önce yazılmış.
- **Kaynak:** R11 S14 bileşen 1; R07 BD-1: "agreeing on what 'done' looked like for that chunk of work before any code was written" (kaynak diyor; tedarikçi, E-HD); verification-independence §6: "Sonucu gördükten sonra değiştirilen doğrulama kuralı, aynı sonuç tarafından bağımsız biçimde doğrulanmış sayılamaz." (kontrol katmanı metni); user-independent-reasoning §9; EkA-5 (A4: "Talebin hangi koşullarda karşılanmış sayılacağını tanımlamanız gerekir."); R06 T11: "«token bütçesi bitti» birer faaliyet/kaynak olayıdır; doğrulama sonucu değildir".
- **Bedel:** Kalem başına 3–6 satır. Tasarım işinde ölçütü denetlenebilir ifadeye çevirmek başlı başına iştir (R07 BD-1 bedel notu).

#### S14-M2 — Tamamlanma katları ve doğrulama sözlüğü
- **Ne:** "Bitti" iddiasını ayrı katlara, her doğrulamayı da bağımsızlığıyla adlandıran tek bir sözlüğe bağlar. "Doğrulandı" kelimesi aynı modelin okumasına verilmez.
- **Nerede:** METHOD'un KG bölümü; kalem ve teslimat kayıtlarında "Kat" alanı; dönüş şemasında durum kodu (T2). Sözlük:

```
## Tamamlanma katları
| Kat | Anlamı | Kanıtı | Kim işaretler |
|---|---|---|---|
| Y yapıldı | Üretici "tamam" dedi | dönüş dosyası @ SHA | ana oturum, dönüş gelince |
| K kaynaktan kontrol edildi | Karar taşıyan iddialar kaynağında bulundu | kontrol listesi: iddia → yol#bölüm → sonuç | ana oturum |
| Ç çürütülemedi | Ayrı girdili inceleme hata bulamadı ya da bulgular kapandı | inceleme dosyası ve bulgu akıbeti | ana oturum, çürütücünün dönüşüyle |
| İ işe yarıyor | Kullanımda gözlendi: canlı deneme, pilot, soğuk başlangıç | deneme kaydı | ana oturum |
| B kabul edildi | Batu kabul etti | kabul paketi @ SHA ve DECISIONS K-xxx | yalnız Batu'nun sözüyle |

## Doğrulama türleri ve etiketleri (dönüşlerde ve raporlarda tek sözlük)
| Etiket | Anlamı | Örnek | Neyi gösterir |
|---|---|---|---|
| öz-kontrol | üretenin kendi kontrolü | alt ajanın "okudum, doğru" demesi | "doğrulama" sayılmaz |
| mekanik kontrol | deterministik betik, grep, git | "21 alt sistemin hepsinde kart var" | yalnız ölçtüğü biçimi; içerik doğruluğunu değil |
| kaynaktan kontrol | ana oturum iddiayı birincil kaynakta buldu | "üç kat iç içe" iddiasının ortam değişkeniyle sınanması | alıntı sadakatini; kaynağın doğruluğu ayrıdır |
| karşı-okuma (aynı model, taze bağlam) | gerekçeyi görmeyen aynı modelli okuma | P0.5 eleştirileri | ortak kör nokta dışlanmaz |
| çürütme sınaması yapılmış inceleme | kasıtlı bozuk örnekte kırmızı verdiği gösterilmiş inceleme | S14-M5 | kontrolün ayırt etme gücü bilinir |
| canlı gözlem | ortamda denenmiş davranış | send_later denemesi | davranışı; tek örnekten genelleme sınırlı |
| soğuk başlangıç | konuşmayı görmemiş oturumun yalnız repodan doğru davranışı | A003 §6 testi | sürekliliği |
| Batu kabulü | yetki kararı | kabul paketi | teknik doğrulama değildir |

Yasak ifadeler: "doğrulandı" (öz-kontrol ya da aynı model karşı-okuma için) · "bağımsız doğrulandı" (farklı yöntem ya da kanıt yoksa) · "tam okundu" (okuma kapsamı kanıtı yoksa) · "artık net".
Sınırlı statüler: "bağımsız doğrulanmadı" · "çürütme sınaması yapılmadı" · "post-hoc bulgu" · "bayat inceleme" (nesne değişti).
```
- **Ne zaman:** Her dönüşte (Y), her kontrolde (K, Ç, İ), her kabulde (B); her rapor ve karar kaydı yazımında (etiketler).
- **Kim:** Ana oturum işaretler; B yalnız Batu'nun sözüyle.
- **Nasıl işler:** 1) Teslimatın katı her olayda bir üst kata geçer; atlama yapılmaz (Y'den doğrudan Ç'ye geçilmez). 2) Her "doğrulandı" iddiasının yanına tür etiketi yazılır. 3) Nesne değişince önceki Ç ve İ katları "bayat" olur.
- **Zorlama düzeyi:** Yapısal (zorunlu kat alanı, sözlük). Mekanik destek: kapanış kapısında (S14-M7) rapor ve karar dosyalarında "doğrulandı" geçen satırların etiket içerip içermediğini listeleyen grep. Zorlayıcı değil.
- **Çalıştığını nasıl anlarız:** Aşama raporlarında "doğrulandı" geçen her yerde tür etiketi var. Kabul paketlerinde "teknik doğrulama durumu" satırı ayrı ve dürüst. Bozulma işareti: aynı model karşı-okumasına "doğrulandı" denmesi; Batu'nun kabulünün böyle bir etikete yaslanması.
- **Bağımlılıklar:** İhtiyaç: T2 (dönüş şemasında durum kodu ve etiket), T5 (soğuk başlangıç testi). Besler: S14-M3, S14-M7, S2-M4, S17-M2 (DOGRULAMA olayı).
- **Standart seviye kararı:** Gerekli. Önlediği hata: "doğrulandı" etiketinin şişmesi ve ortak kör noktanın görünmez olması (Y6; E67); kabulün teknik doğrulama sanılması (E05). Kabul testi: yukarıdaki iki gözlem.
- **Kaynak:** R11 S14 bileşen 2 ve 4; A003 §3.8 ve §3.3 ("Aynı model olduğu için buna 'bağımsız doğrulama' değil, 'taze gözle karşı-okuma' derim."); R05 satır 13; R04 (d)2–3: "review complete != gate satisfied"; "two role labels != two independent Actors" (kaynak diyor; kavramsal analiz); verification-independence §3 ve §11; R11 K69 (gstack: "Work performed != target condition achieved != evidence supports success != authorized acceptance/progression"); R11 K106.
- **Bedel:** Düşük: kayıt başına bir alan; raporlarda "doğrulandı" daha seyrek görünür.

#### S14-M3 — Risk sınıfı ve kontrol ağırlığı
- **Ne:** Her iş kaleminin doğrulama setini risk sınıfından türetir; genel "tekrar kontrol et" talimatını yasaklar.
- **Nerede:** METHOD KG bölümü; kalem kaydında "Risk sınıfı" alanı; görev tanımında "doğrulama beklentisi" alanı (T2). İçerik:

```
Sınıflama soruları (her biri evet/hayır):
a) Geri alınamaz mı ya da dış etkisi var mı?
b) Aşağı akış yükü: bu çıktıya 3'ten çok karar ya da kalem dayanacak mı?
c) Batu'ya kabul ya da sunum için gidecek mi?
d) Belirsizlik yüksek mi (kaynak yok ya da çelişkili, yeni alan)?
e) Tasarım kararı taşıyor mu (yalnız okuma ya da özet değil)?

| Sınıf | Koşul | Zorunlu doğrulama seti | Örnek |
|---|---|---|---|
| R0 | hepsi hayır | öz-kontrol; varsa mekanik kontrol | dosya taşıma, biçim düzeltme, okuma listesi |
| R1 | 1 evet | + karar taşıyan iddialarda kaynaktan kontrol | tek kaynaklı okuma notu |
| R2 | 2–3 evet | + ayrı girdili çürütücü (S14-M4) | küme taslağı; araştırma notu (R07–R11) |
| R3 | 4–5 evet ya da (a) | + bütünsel inceleme + söz–çıktı matrisi + standart–yeterli denetimi + uygunsa canlı deneme ya da soğuk başlangıç | METHOD v1; aşama çıktısı; yapılandırma kurulumu |

Kurallar:
- Görev tanımına "sonunda her şeyi tekrar kontrol et" ya da "bir alt ajanla doğrula" yazılmaz; doğrulama beklentisi sınıfın adıyla ve setiyle yazılır.
- Belirsizse bir üst sınıf.
- "Git geri alır" gerekçesiyle R0'a inilmez: aşağı akış yükü (b) ayrıca sorulur.
```
- **Ne zaman:** Kalem açılırken (S14-M1 ile aynı anda); kalemin kapsamı değişirse yeniden.
- **Kim:** Ana oturum.
- **Nasıl işler:** 1) Beş soru cevaplanır. 2) Sınıf ve set kalem kaydına yazılır. 3) Görev tanımına beklenti girer. 4) Kapanışta setin tamamlandığı denetlenir (S14-M7).
- **Zorlama düzeyi:** Yapısal (zorunlu alan). Tavsiye (sınıflama yargısı).
- **Çalıştığını nasıl anlarız:** Aşama sonu örnekleminde sınıf ile uygulanan set uyumlu. R3 kalemlerde eksik set yok. Doğrulama maliyeti (T5 ölçüsü) sınıflara göre dağılıyor; R0 kaleme çürütücü açılmamış. Bozulma işareti: her kaleme çürütücü (tören, maliyet) ya da R2/R3 kalemde çürütücü yok.
- **Bağımlılıklar:** İhtiyaç: T3 (kalem şeması, rota ölçekleme S3), T5 (maliyet ölçümü), T2 (görev tanımı alanı). Besler: S14-M4, S14-M7, S15-M2 (b).
- **Standart seviye kararı:** Gerekli. Önlediği hata: "düşük risk" sınıfının eleştirisiz kararları yayması (Y7); ya her şeye tören ya hiçbir şeye kontrol (E15); aşırı doğrulama (R07 P-O5). Kabul testi: yukarıdaki iki gözlem. Genel "tekrar kontrol et" talimatı: gereksiz; koşul her zaman geçerli, çünkü Anthropic bunun Opus 5'te aşırı doğrulama ürettiğini söylüyor; Opus 5.5 için geçerliliği bilinmiyor (R07 §8 soru 6).
- **Kaynak:** A003 §3.8 ("Kontrolün ağırlığı risk ve geri alınabilirlikle orantılıdır."); R07 BD-7: "The longer Claude works unattended, the more an independent check matters before you count the work as done." ve P-O5: "instructions like these cause over-verification on Claude Opus 5" (kaynak diyor; tedarikçi, C~); R11 Y7; R08 O15 (BMAD: tören incelemeden sonra seçilir; ölçütler niyet boşlukları, geri alınamaz eylemler, ayak izi); R09 YD-5 (üç rota).
- **Bedel:** Kalem başına bir sınıflama. Yanlış sınıflama riski; dengeleyici: belirsizse üst sınıf.

#### S14-M4 — Ayrı girdili çürütücü inceleme, bulgu akıbeti, tur sınırı
- **Ne:** R2 ve R3 çıktıları, üreticinin gerekçesini görmeyen, yalnız ölçütü, nesneyi (@SHA) ve Batu'nun birebir sözlerini alan, çürütmeye ayarlı bir inceleme işlevine verilir. Her bulgu bir akıbet alır; tur sayısı sınırlıdır.
- **Nerede:** Görev tanımının göreve özgü kısmı aşağıdadır; sabit kısmı çürütücü işlevin rol dosyasında durur. **T2'ye ihtiyaç:** çürütücü inceleme işlevini taşıyan kalıcı rol. Bu işlev ana oturumda yapılamaz, çünkü ana oturum üreticinin gerekçesini taşır; taze bağlamlı bir alt ajan gerekir. Bulgular `reviews/<nesne>-BULGULAR.md` dosyasına yazılır (yol T1'in). Görev tanımı şablonu:

```
# İnceleme — <nesne> @ <SHA>
Amaç zinciri: SOUL → DevOS → EXP-007 <aşama> → bu çıktı → beslediği karar: <…>
İncelenen nesne: <yol> @ <SHA> (başka sürümü inceleme)
Ölçütler (işten önce yazılmış; birebir): <S14-M1 alanından>
Batu'nun bağlayıcı sözleri (birebir): <U003/U004 alıntıları; ilgili K-xxx>
Bilerek verilmeyenler: üreticinin gerekçesi; önceki inceleme bulguları; "kapatmak istiyoruz" bilgisi
Görev: Nesneyi çürütmeye çalış. Her hata sınıfı için "denendi — nasıl arandı — bulgu var/yok" yaz:
  H1 ölçütü karşılamayan bölüm
  H2 kaynakta olmayan ya da kaynağın gücünü aşan iddia
  H3 soyut kalan vaat (mekanizması, sahibi ya da tetiği yok)
  H4 gerekçesiz "gereksiz", "ertelendi" ya da "yeterli"
  H5 iç çelişki
  H6 kimseye verilmemiş iş
  H7 Batu'nun sözünün yorumla değiştirilmesi
Varsa en az bir rakip açıklama ya da alternatif tasarım öner.
Triyaj: yalnız doğruluğu ya da yazılı ölçütü etkileyen bulgular "zorunlu"; diğerleri "isteğe bağlı".
"Bilmiyorum" ve "doğrulanamadı" geçerli cevaptır. Bulgu yoksa "bulgu yok" yaz ve nasıl aradığını söyle.
Dönüş: bulgu tablosu + okuma kapsamı + bu incelemenin neyi sınamadığı.
```

  Bulgu tablosu (inceleyici doldurur, akıbeti ana oturum yazar):
```
| B# | Hata sınıfı | Yer | Bulgu | Kanıt (alıntı, yol) | Zorunlu mu | Akıbet: uygulandı @SHA / gerekçeyle reddedildi / park (yeniden açma tetiği) |
```
  Tur sınırı: bir nesne en fazla 3 inceleme–düzeltme turu görür. Her tur bir şeyi değiştirmek zorundadır; aynı görev tanımıyla tekrar yoktur. 3. turdan sonra açık zorunlu bulgu kalırsa ya park edilir ve kabul paketine "bilinen açık" olarak girer, ya da Y10 ile Batu'ya gider.
- **Ne zaman:** R2 ve R3 kalemlerin dönüşünden sonra, K katına ulaşıldığında; aşama sonunda iz denetimi için (S15-M5).
- **Kim:** İnceleme: çürütücü işlev (T2'nin rolü). Akıbet ve tur kararı: ana oturum.
- **Nasıl işler:** 1) Görev tanımı şablondan üretilir; nesne SHA'sı sabitlenir. 2) İnceleme dönüşü dönüş kapısından geçer (S14-M6). 3) Ana oturum her bulguya akıbet yazar. 4) Zorunlu bulgular düzeltilir, yeni SHA ile gerekirse ikinci tur. 5) Kat Ç işaretlenir ya da park ve yükseltme uygulanır.
- **Zorlama düzeyi:** Yapısal (şablon). Zorlayıcı: çürütücü işlevin rol dosyasında salt okuma araç listesi (Read, Grep, Glob; yazma, oturum açma ve zamanlama araçları yok) (T2, T5); dönüş biçimi kapısı (Z1).
- **Çalıştığını nasıl anlarız:** Akıbetsiz bulgu yok. H1–H7 sınıf dağılımı izlenir. Çürütücünün hata duyarlılığı biliniyor (S14-M5). Batu'nun kabulde bulduğu ve çürütücünün kaçırdığı açıklar ayrı sayılıyor (S2-M6). Bozulma işareti: uzun süre hep "bulgu yok" (körleşme ya da ritüelleşme; verification-independence §8) ya da hep çok sayıda isteğe bağlı bulgu (aşırı mühendislik; R07 BD-5).
- **Bağımlılıklar:** İhtiyaç: T2 (kalıcı rol, araç listesi), S14-M1, S14-M5, S14-M6, T1 (reviews klasörü). Besler: S14-M2 (Ç katı), S14-M7, S2-M4 (bilinen açıklar), S2-M6 (sistemin yakaladıkları).
- **Standart seviye kararı:** Gerekli (R2, R3). R0 ve R1'de gereksiz; koşul: aşağı akış yükü yok ve karar taşımıyor. Önlediği hata: öz-onay (E67; EXP-006'da hiçbir aile elenmedi); park edilen bulguların görünmez birikmesi (Y8); sorunu görüp "önemsiz" sayan inceleme (R07 §3). Kabul testi: R2/R3 kalemlerin hepsinde inceleme dosyası ve akıbetli bulgu tablosu.
- **Kaynak:** R11 S14 bileşen 3, 8, 9; A003 §3.3 ("Karşı-okuyucu, sonucu üretenin gerekçesini görmez"); R05 satır 11: "The verifier gets the original work definition, the exact target version, the criterion and direct evidence. It reports and does not repair." (kaynak diyor; alt ajan raporu); R07 BD-3, BD-4, BD-5 ve BD-6 (kaynak diyor; tedarikçi); R08 O21 (BMAD niyet uyumu denetçisine niyetin birebir verilmesi); EkA-6 ("4 ayrı bağımsız AI merceği … çürütmeye çalıştı"); verification-independence §8, §10.
- **Bedel:** R2/R3 kalem başına bir alt ajan koşusu (P0.3'te araştırma notu başına 0,13–0,66 M token ölçüldü, STATE; bir inceleme koşusunun bundan az olması beklenir, varsayım); akıbet yazımı.

#### S14-M5 — Hata duyarlılığı sınaması
- **Ne:** Bir inceleme işlevinin (rol sürümünün) kasıtlı bozulmuş bir nesnede kırmızı verebildiğini gösterir; sonuç incelemenin güven etiketine yazılır.
- **Nerede:** `reviews/kalibrasyon/<işlev>-<sürüm>.md` (yol T1'in). Örnek:

```
Nesne: drafts/T4-yon-yetki-ve-denetimler.md @ <SHA> kopyası (yalnız bu deneme için, geçici)
Ekilen hatalar (inceleyiciye söylenmez):
  E1 S2-M4'ten "SHA" alanı silindi (H1)
  E2 S14-M2'ye "karşı-okuma = doğrulandı" cümlesi eklendi (H2/H7)
  E3 S17-M3 eşiği "gerektiğinde" diye soyutlandı (H3)
  E4 bir bileşen "şimdilik yeter" gerekçesiyle gereksiz sayıldı (H4)
Sonuç: 3/4 yakalandı (E3 kaçtı) → etiket: "çürütme sınaması 3/4; soyutlama sınıfında zayıf"
Kalibrasyon: kaçan sınıf için rol dosyasına kısa bir örnek eklendi; rol sürümü +1 (T2'nin değişiklik yolu)
```
- **Ne zaman:** Çürütücü işlevin ilk sürümünde; rol dosyası ya da model değişince (T2'nin rol regresyonuyla birlikte); aşama başına en fazla bir kez.
- **Kim:** Ana oturum hazırlar; çürütücü işlev koşar; kalibrasyon kararı T2'nin değişiklik yoluyla.
- **Nasıl işler:** 1) Nesnenin geçici bir kopyasına 3–5 hata ekilir. 2) Normal inceleme görev tanımıyla koşulur; ekildiği bilgisi inceleyicinin bağlamına girmez. 3) Yakalanan/kaçan sayılır. 4) Etiket ve kalibrasyon yazılır. 5) Geçici kopya silinir, kayıt kalır.
- **Zorlama düzeyi:** Yapısal (şablon; ritim T3'ün tablosunda).
- **Çalıştığını nasıl anlarız:** Her çürütücü rol sürümü için bir kalibrasyon kaydı var. İnceleme raporlarında etiket bu kayda atıf yapıyor. Kaçan sınıflar sonraki sürümde yakalanıyor.
- **Bağımlılıklar:** İhtiyaç: S14-M4, T2 (rol sürümü, regresyon), T5 (maliyet). Besler: S14-M2 (etiket), S2-M4 (güven dili).
- **Standart seviye kararı:** Rol sürümü başına gerekli. Her incelemede gereksiz; koşul: rol ve model değişmemişse. Bütünsel etkisi: sınama seyrekse körleşme geç fark edilir; dengeleyici S14-M4'teki "hep bulgu yok" işaretidir. Önlediği hata: ayırt edemeyen denetçi (E68; EXP-005'te iki yöntem de aynı sonucu aldı). Kabul testi: kalibrasyon kaydının varlığı ve raporlardaki atıf.
- **Kaynak:** R11 S14 bileşen 5, E68; EkA-14 (EXP-005 D05: "İki taraf da 4/4 PASS ve 23/23 gözlem aldı"); verification-independence §4: "Bir kontrolün yeşil vermesi ancak yanlış durumda kırmızı verebildiği ölçüde anlamlıdır."; R07 BD-3 (kalibrasyon) ve BD-8: "we do not take eval scores at face value until someone digs into the details of the eval and reads some transcripts" (kaynak diyor; tedarikçi); R10 §4.8 madde 4 ("Testing can be an intervention.").
- **Bedel:** Hazırlık ~1 saat; bir inceleme koşusu; transkript okuma.

#### S14-M6 — Dönüş kapısı ve kaynaktan kontrol
- **Ne:** Her alt ajan dönüşü kabul edilmeden önce zorunlu alanlar açısından mekanik olarak, karar taşıyan iddiaları açısından ana oturumca kaynağında denetlenir. Dönüş veridir.
- **Nerede:** Dönüş şeması T2'nin (S13); kapının kontrol listesi burada. Kalem kaydında:

```
Dönüş kapısı — <kalem>, görev tanımı <yol> @ <SHA>, dönüş dosyası @ <SHA>
[ ] Zorunlu alanlar: Durum kodu · Bulgular (iddia, kanıt, etiket) · Karar-kritik varsayımlar · Kendi seçimleri · Açık sorular · Okuma kapsamı (tam/kısmi/okunmadı/erişilemedi) · Dokunulan dosyalar · Görev tanımı sürümü
[ ] Dokunulan dosyalar izinli yazma listesinin içinde (git diff --name-only <dağıtım HEAD'i>..HEAD)
[ ] Bu dönüşten bir karara girecek iddialar listelendi: n adet
[ ] Her biri kaynağında kontrol edildi: yol#bölüm → bulundu / bulunamadı / kaynak yok
[ ] Taban değişti mi? Dağıtımdan bu yana Batu kararı ya da zarf değişikliği varsa (ör. K-010) uzlaştırma notu yazıldı
[ ] Kat: Y → K
```
  Gerçek örnekler: "alt ajanlar üç kat iç içe çalışabilir" iddiası ortam değişkeniyle sınandı ve düştü (A003 §3.3). R10'un dönüşü K-010'dan önceki tabana göre yazılmıştı (R10 §0.4).
- **Ne zaman:** Her alt ajan dönüşünde.
- **Kim:** Mekanik kısım hook (varsa) ya da ana oturum; kaynaktan kontrol ana oturum.
- **Nasıl işler:** 1) Dönüş gelir; alanlar denetlenir, eksikse dönüş reddedilir ya da "BAĞLAM EKSİK" sayılır. 2) Yazma listesi git ile denetlenir. 3) Karar taşıyan iddialar seçilir ve kaynağında aranır. 4) Taban değişikliği uzlaştırılır. 5) Kat K işaretlenir, günlüğe KAPI satırı yazılır.
- **Zorlama düzeyi:** Zorlayıcı aday (Z1): `SubagentHandback` aracına eşlenen PreToolUse hook'u `tool_input.message` içinde zorunlu başlıkları arar; eksikse çıkış kodu 2 ile eksik başlıkları bildirir ve alt ajan dönüşünü düzeltir. Yedek: SubagentStop'ta `last_assistant_message`. Koşullar: `settings.json` hook'ları yalnız tek repolu oturumda okunur (C!); SubagentHandback teslimatı v2.1.271 ve sonrasını ister (kurulu CLI 2.1.283, ortam değişkeni 2.1.42: çelişki, EkA-17); kurulum A-04 onayına bağlıdır. Kaynaktan kontrol yapısal ve tavsiye düzeyindedir.
- **Çalıştığını nasıl anlarız:** Kapıdan geçmeden K katına çıkan dönüş yok. "Bulunamadı" çıkan iddiaların karara girmediği karar kaydında görülüyor. Bozulma işareti: gerekçesi "alt ajan böyle diyor" olan karar.
- **Bağımlılıklar:** İhtiyaç: T2 (dönüş şeması, yazma listesi), T5 (Z1 kurulumu), S17-M1 (dağıtım HEAD'i). Besler: S14-M2 (K katı), S14-M4, W2, W5, W6.
- **Standart seviye kararı:** Gerekli. Önlediği hata: dönüş veri sayılmayınca yanlış iddianın karara girmesi (E63); "tam okudum" iddiasının sınanamaması (E29, K51); tabanı değişmiş dönüşün uzlaştırılmaması (K-010 olayı). Kabul testi: yukarıdaki iki gözlem.
- **Kaynak:** A003 §3.3 ("Dönen sonuç veridir, kanıt değildir."); R11 S13 bileşen 5; R05 satır 2, 4, 27 ("Record HEAD before dispatch"); R07 BO-8; source-view-fidelity §3, §5; EkA-10 (hooks.md; C~), EkA-18.
- **Bedel:** Dönüş başına 5–15 dakika ana oturum işi (tahmin); hook seçilirse bir betik.

#### S14-M7 — Kapanış kapısı
- **Ne:** Bir aşama ya da çok kalemli teslimat "TAMAM" işaretlenmeden önce kalem denetiminden, kimseye verilmemiş iş taramasından, bütünsel incelemeden ve sahte kapanış sorularından geçer.
- **Nerede:** `phases/<aşama>/KAPANIS.md` (yol T1'in). Şablon:

```
# Kapanış kapısı — P0 @ <SHA>
## 1. Kalem denetimi (plan kalemlerinin hepsi; sessiz toptan onay yok)
| Kalem | Hüküm: YAPILDI / KISMEN / YAPILMADI / DEĞİŞTİ / DOĞRULANAMADI | Kanıt (yol @ SHA) | Kat (Y/K/Ç/İ/B) |
## 2. Kimseye verilmemiş iş
Yöntem T3 S4'ün; eksik-arayıcı işleve görev tanımından bağımsız bir kaynak alanı verilir.
- Tarama kapsamı: … · Bulgular: … → yeni kalem / bilinçli kapsam dışı (gerekçeli)
## 3. Bütünsel inceleme (R3 çıktılarda): nesnenin tamamı @ SHA, S14-M4 şablonuyla; birleştirme doğrulaması T2 S12'nin
## 4. Söz–çıktı özeti (S14-M8) ve standart–yeterli denetimi (S14-M9)
## 5. Sahte kapanış soruları (cevaplar yazılır)
- Bu aşamayı yeniden açmanın hiçbir maliyeti olmasaydı yine "tamam" der miydim?
- Bütçe ya da bağlam bittiği için mi kapanıyor? (evetse "park"; "tamam" değil)
- Bu aşamada hangi kararlar değişti? (yoksa kapanış değil takılma şüphesi → S17-M3)
- "Doğrulandı" geçen satırlar etiketli mi? (S14-M2 grep çıktısı)
## 6. Hüküm: kapanabilir / şu koşulla / kapanamaz · Açık kalanlar → kabul paketine "bilinen açık"
```
- **Ne zaman:** Her aşama sonunda; çok kalemli bir teslimat (ör. METHOD taslağı) "TAMAM" yapılmadan önce.
- **Kim:** Ana oturum; §2'de eksik-arayıcı işlev (T2 ve T3'e ihtiyaç); §3'te çürütücü işlev.
- **Nasıl işler:** 1) Plan kalemleri listelenir ve tek tek hükme bağlanır. 2) Tarama ve bütünsel inceleme koşulur. 3) S14-M8 ve S14-M9 özetleri eklenir. 4) Sahte kapanış soruları cevaplanır. 5) Hüküm yazılır; STATE'te aşama ancak bundan sonra "TAMAM" olur.
- **Zorlama düzeyi:** Yapısal (şablon). Zorlayıcı aday (Z4): STATE.md'de bir aşamayı "TAMAM" yapan yazımı, ilgili KAPANIS dosyası yoksa ya da §6 boşsa engelleyen PreToolUse betiği (T5; A-04; C!).
- **Çalıştığını nasıl anlarız:** Her aşama kapanışında dosya var. §1'de YAPILDI dışındaki hükümler kabul paketine ya da aşama raporuna taşınmış. Batu'nun kapanıştan sonra "şu eksik" demesi (H türü) azalıyor.
- **Bağımlılıklar:** İhtiyaç: T3 (plan kalemleri, S4 yöntemi), T2 (eksik-arayıcı ve çürütücü işlevler; birleştirme doğrulaması), S14-M2, S14-M4, S14-M8, S14-M9. Besler: S2-M2, S2-M4, S1-M2 (geçiş).
- **Standart seviye kararı:** Gerekli. Önlediği hata: doğrulamanın yalnız plandaki işi sınaması ve eksik işin "tamam" damgası alması (E19; Foundation: "The assistant nevertheless declared the example finished."); şişen "tamam" (E69); sessiz toptan onay (R05 satır 12); erken zafer (R07 §3). Kabul testi: yukarıdaki üç gözlem.
- **Kaynak:** R11 S14 bileşen 6–7; R05 satır 12 ("forbids silent blanket confirmation"), 25, 26; A003 §3.8 ("gerekli olduğu halde kimseye verilmemiş iş var mı?"); R11 K41; user-independent-reasoning §6; R06 T11.
- **Bedel:** Aşama başına 2–3 alt ajan koşusu ve ~2 sayfa.

#### S14-M8 — Söz–çıktı izlenebilirliği ve söz kaydı
- **Ne:** Batu'nun gereksinimlerini, sorularını ve kararlarını ve Claude'un ona verdiği sözleri, onları karşılayan mekanizmalara ve karşılanma düzeyine bağlar; karşılığı olmayanı görünür kılar. Batu'nun "söz geniş, çıktı dar" eleştirisinin kalıcı denetimidir.
- **Nerede:** `phases/<aşama>/SOZ-CIKTI.md` (METHOD için entegrasyonda üretilir; yol T1'in). Şablon:

```
| Söz ID | Kaynak (birebir) | Söz | Karşılayan mekanizma | Düzey: nasıl / kısmen / ilke / karşılanmadı | Kanıt (kart, dosya @ SHA) | Kısmen ya da karşılanmadıysa: neden ve bütünsel etki |
|---|---|---|---|---|---|---|
| U004-3 | U004: "context management önemli bir yer tutacak bence" | bağlam yönetimi | T1 S7 kartları | (entegrasyonda) | | |
| U003-5 | U003: "planı nasıl revize ederdin" | plan revizyonu | T3 S5; S1-M1 revizyon sınıfları | | | |
| A003-3.6-g | A003 §3.6: "Birkaç kalem boyunca hiçbir karar değişmezse 'hareket var, ilerleme yok' diye durur, sana haber veririm." | takılma alarmı | S17-M2, S17-M3, S2-M5 | nasıl | bu taslak | — |
| C-2026-10-03-1 | Claude, KN-P1-02 (kurgusal): "P1 sonunda ortam haritasını canlı denemeyle sınayacağım" | canlı deneme | P1 kalemi P1-021 | | | |
```
  Söz kaydı: Claude'un Batu'ya verdiği her ileriye dönük taahhüt ("yapacağım", "ekleyeceğim", "kuracağım") mesaj yazılırken matrise "C-tarih-n" satırı olarak eklenir; aşama kapanışında düzeyi işaretlenir.
- **Ne zaman:** Entegrasyonda (METHOD için ilk tam matris); her aşama kapanışında; Claude her taahhüt verdiğinde (C satırı).
- **Kim:** Ana oturum; kapanışta düzey işaretlerini çürütücü işlev okur (H3 sınıfı).
- **Nasıl işler:** 1) Kaynak metinler madde madde bölünür; her madde bir satır olur. 2) Karşılayan mekanizma ve düzey yazılır. 3) "Kısmen" ve "karşılanmadı" satırları gerekçe ve bütünsel etki ister. 4) C satırları aşama kapanışında kapanır ya da gerekçeyle devreder. 5) Özet aşama raporuna ve kabul paketine girer.
- **Zorlama düzeyi:** Yapısal (şablon; kapanış kapısında zorunlu bölüm). Mekanik destek adayı: Stop hook'u `last_assistant_message`te gelecek zaman taahhüt kalıplarını (-acağım, -eceğim) arar ve matrise ekleme hatırlatması verir; yanlış pozitif oranı bilinmiyor.
- **Çalıştığını nasıl anlarız:** Entegrasyonda "karşılanmadı" satırları açıkça yazılı ve sayısı raporda. P0.5'in söz–çıktı eleştirisinin (E1) bulduğu eksikler matriste zaten görünüyor. C satırlarının hepsinin akıbeti var. Batu'nun "şunu söylemiştin" tepkisi = 0.
- **Bağımlılıklar:** İhtiyaç: T3 (her aşamanın vaatleri; plan tarafı), T1 (birebir kaynaklar), bütün kümelerin kart kimlikleri. Besler: S14-M7, S2-M4, P0.5 eleştiri 1.
- **Standart seviye kararı:** Gerekli. Önlediği hata: U004 eleştirisinin kendisi (H-001); v0'ın kapsamının sistemin ihtiyacını değil okunan araştırmayı izlemesi (R11 §6). Kabul testi: yukarıdaki dört gözlem.
- **Kaynak:** U004 ("cevaplarında konuyu iyi anlamış gibi ifade ediyorsun ama iş aksiyona gelince o anlattıklarına göre sonuç çok daha dar kapsamlı oluyor"); T4.md; P0 README (P0.5 eleştiri 1); R03 ilke 8 ("büyük laflar edip küçük işler yapmanı istemiyorum"); R11 §6.
- **Bedel:** Entegrasyonda bir kez ~60 satır; aşama başına güncelleme; taahhüt başına bir satır.

#### S14-M9 — Standart–yeterli denetimi
- **Ne:** Her "gereksiz", "ertelendi" ya da "bilinmiyor" kararını ve her "yeterli" ifadesini, koşul ve bütünsel etki gerekçesi taşıyıp taşımadığına göre denetler.
- **Nerede:** METHOD KG bölümü; çürütücü görev tanımında H4 sınıfı; kapanış kapısında §4. Kural:

```
Bir bileşen "gereksiz" sayılabilir ancak:
 (1) koruduğu kullanım bu işte yoksa ya da o boyut bu kullanım için bağımsız değişemiyorsa,
 (2) yokluğunun başka alt sistemlere etkisi R11 matrisinde (E-kenarları) incelenip yazılmışsa,
 (3) gerekçe "şimdilik yeter", "basit tutalım", "yeterli" gibi bir yeterlilik ifadesine dayanmıyorsa,
 (4) yeniden değerlendirme tetiği yazılmışsa.
"Ertelendi" ayrıca: hangi aşamada, hangi tetikle; ertelemenin bütünsel etkisi.
"Bilinmiyor": nasıl bilinir hale gelecek (pilot, deneme, Batu).
Ters hata da bulgudur: gerekçesiz "gerekli" (her şeyi koruma) ağırlık bütçesini (T3) bozar.
Mekanik ön tarama: taslak ve METHOD dosyalarında "şimdilik yeter|yeterli seviye|basit tutalım|gerek yok" arayan grep; her eşleşme ya gerekçeli ya bulgu.
```
- **Ne zaman:** Her tasarım kararında (TK'da "gereksiz" varsa); entegrasyonda standart seviye tablosu kurulurken; kapanışta.
- **Kim:** Ana oturum uygular; çürütücü işlev denetler.
- **Nasıl işler:** 1) Karar anında dört alan doldurulur. 2) Grep ön taraması koşulur. 3) Çürütücü H4 sınıfını dener. 4) Bulgular akıbet alır (S14-M4).
- **Zorlama düzeyi:** Yapısal (dört alan zorunlu); mekanik ön tarama (grep).
- **Çalıştığını nasıl anlarız:** Entegrasyondaki standart seviye tablosunda her "gereksiz"in dört alanı dolu. P0.5'in "yeterli seviye" bulguları kapandı. Bozulma işareti: gerekçesiz "gereksiz" ya da her şeyin "gerekli" olması.
- **Bağımlılıklar:** İhtiyaç: R11 matrisi, T3 (ağırlık bütçesi), S14-M4. Besler: S14-M7, S14-M8, entegrasyonun standart seviye tablosu.
- **Standart seviye kararı:** Gerekli. Önlediği hata: "yeterli seviye" yaklaşımı (U004); iki yönlü aşırılık (ORTAK-SENTEZ: "Hem 'daha basiti yeter' hem 'her şeyi koru' reddedilir"). Kabul testi: yukarıdaki iki gözlem.
- **Kaynak:** U004 ("yeterli seviye ile standart seviye arasında fark var"); ORTAK "Standart seviye ne demek"; ORTAK-SENTEZ madde 3; R10 §2.3 (Foundation: "a simpler arrangement is not adequate merely because it is simple"; "`Keep everything forever` is not neutral"); R11 §2.3 ve §5.
- **Bedel:** Karar başına dört alan; aşama başına bir grep.

### 2.4 S15 — Muhakeme disiplini ve bilinen ajan kusurları

**Amaç.** Üretim sırasındaki düşünmenin kalitesini iz bırakan uygulamalarla korumak: varsayımların görünürlüğü, alternatif üretme, nedensel derinlik, onay baskısına direnç, "bilmiyorum" diyebilme. Kalite güvencesi çıktıyı sonradan sınar; bu alt sistem çıktının nasıl üretildiğini korur. Batu'nun sorusu buydu: "alt ajanlar nasıl düşünürdü" (U003). Bu işi repo bugün ayrı bir katmanda yürütüyor (AGENT.md protokolleri) ve loopinance'ta "sürecin en değerli çıktısı" olarak anılan defo modeli var (EkA-2 ders 10).

**R11'e göre değişenler.**
- Defo modeline, bu repoda gözlenen üç defo eklendi: kapsam daraltma (U004), erken kapanış (Foundation soru bankası), aşırı kesinlik (R01 "Abartılı iddialar"). Görev tanımının adını koyduğu dalkavukluk, modeldeki "yağcılık"tır.
- Öz-denetimin tek başına yetmediği açıkça yazıldı: "Yumuşak öz-yargı kendini geçirir" (EkA-1). Uzun koşu öz-denetimi aşama sonunda başka bir okumayla denetlenir.

**Karar tablosu.**

| Bileşen | Karar | Önlediği hata | Kabul testi | Kaynak | Kart |
|---|---|---|---|---|---|
| Defo modeli (EXP-007 sürümü) | gerekli | makul görünen defoların yakalanmaması (E71–E74) | aşama sonu iz denetiminde doluluk | EkA-1; EkA-5 | S15-M1 |
| İz ilkesi (mekanik kapı > iz isteyen prosedür > öğüt) | gerekli | "daha dikkatli olacağım" vaatleri | her karşı önlemin düzeyi yazılı | EkA-1 | S15-M1 |
| Karar-kritik varsayım disiplini | gerekli | tek senaryonun kesin sanılması | TK ve dönüşlerde varsayım alanı | decision-critical-assumptions | S15-M2 |
| Kanıt dışı etkiye direnç | gerekli | "haklısın, bunu düşünmemiştim" döngüsü | itiraz cevaplarında çürütme izi | user-independent-reasoning | S15-M3 |
| Nedensel derinlik | gerekli (olay analizinde) | yanlış düzeltme | H kayıtlarında iki soru | causal-depth | S15-M4 |
| Alternatif ve karşı kanıt arama | gerekli | tek seçenekli tasarım | TK'da "reddedilen" alanı | A003 §3.3 | S15-M2, S1-M4 |
| Belirsizlik beyanı | gerekli | uydurma, boşluğun düzlenmesi | dönüşlerde "bilinmiyor/erişilemedi" kullanımı | EkA-1 #6 | S15-M2 |
| Uzun koşu öz-denetimi ve iz denetimi | gerekli | drift, öz-onay döngüsü (E73) | 5 kalemde bir ÖZ-DENETİM satırı | EkA-5 | S15-M5 |
| Disiplinin alt ajanlara taşınması | gerekli | emir eri (E64); disiplin yalnız istemde (E89) | 5 rol ve görev tanımında taşıyıcılar | R11 S15 | S15-M2 |
| Alt ajanların routing gate koşması | gereksiz, koşullu | — | S1-M5'e bakınız | R01 | S1-M5 |
| Düşünmeyi hook'la denetlemek | gereksiz (mümkün değil) | — | — | EkA-5 | S15-M1 |
| "Daha dikkatli ol" türü talimat | gereksiz (zararlı) | — | görev tanımlarında yok | EkA-1 | S15-M1 |

"Düşünmeyi hook'la denetlemek" gerekçesi. Koşul her zaman geçerli: hook mekaniktir, "Böyle düşünme" diyemez (A4). Hook yalnız iz alanlarının varlığına kurulur (Z1, Z3, Z4). Bütünsel etkisi yok; düşünme disiplini taşıyıcılarla ve aşama sonu iz denetimiyle korunur.

#### S15-M1 — Defo modeli ve iz ilkesi
- **Ne:** Ajanın bilinen eğilimlerini, EXP-007'de ateşlendikleri anları ve her biri için gözlemlenebilir iz kontrolünü tek, kısa bir belgede toplar. Her karşı önlemi bir iz alanına ya da mekanik kapıya bağlar.
- **Nerede:** `DEFO-MODELI.md`, METHOD'un eki (en fazla 6 KB; yol T1'in). Rol dosyaları (T2) ilgili satırları taşır; CLAUDE.md (T5) işaretçi verir. İçerik (ilk on satır loopinance_v2 DEFO_MODELI'nden uyarlamadır; 11–13 bu repodaki olaylardan):

```
Kök itki (kaynaktan): "Ajan, cevabı oluştururken anlık onay / 'iyi görünme' olasılığını maksimize etmeye itilir — kullanıcının sonraki-adımdaki gerçek hedefini değil."

| # | Defo | EXP-007'de ateşlendiği an | İz kontrolü (öz-yargı değil) | Bağlı kart |
|---|---|---|---|---|
| 1 | Yağcılık | Batu görüş bildirince ya da itiraz edince | Onaylayan cevapta "şunu çürütmeyi denedim, şu yüzden tuttu" satırı; yoksa bayrak | S15-M3 |
| 2 | Aynalama | Batu'nun mesajını özetlerken; ekleyecek şey yokken | Batu'nun metninde olmayan bir delta gösterilebiliyor mu; yoksa "ekleyecek şeyim yok, yalnız teyit" | S2-M1 |
| 3 | Şişme | rapor, not ya da görev tanımı yazarken | "Neyi kırptım?" satırı; kelime sınırı | S2-M1, S2-M5 |
| 4 | Drift | çapasız başlanan tur; sıkıştırma sonrası; uzun özerk koşu | Çapa tek cümle ve "bu çıktı ona hizmet ediyor mu" satırı; çapa dosyada | S15-M5, S1-M2 |
| 5 | Sahte menü | tur sonu, devir, bekleme anı | Üç bitişten biri; "ne yapayım?" yok | S2-M1 |
| 6 | Uydurma | boşluk, belirsizlik, erişilemeyen kaynak | Taşıyıcı iddiada kaynak işaretçisi ve etiket; "erişilemedi" yazılı | S15-M2, S14-M6 |
| 7 | Öz-onaylama | üretimi bitirirken | Başarı iddiasında kat ve kanıt; "araç başarılı döndü ≠ sonuç doğru" | S14-M2 |
| 8 | Donma / aşırı sorma | belirsizlik taşıyan eylem anında | Soru yönlendirme izi: 1–4 neden yetmedi | S1-M3 |
| 9 | Karar yükleme | çözülebilir karar anında | "Neden sana" satırı; türetilebilir olan Batu'ya taşınmaz | S1-M3, S2-M3 |
| 10 | Örtme | devir, rapor, kapanış | "Açık işler" bölümü dolu; "engel değil, paralel" diye hafifletilen kalem bayrak | S2-M2, S14-M7 |
| 11 | Kapsam daraltma (söz geniş, çıktı dar) | "anladım" deyip üretime geçerken | Söz–çıktı satırı; standart–yeterli denetimi | S14-M8, S14-M9 |
| 12 | Erken kapanış | "tamam" anı | Kapanış kapısı soruları; değişen karar yoksa kapanış yok | S14-M7 |
| 13 | Aşırı kesinlik | belge okumasından kabiliyet çıkarırken; özetlerken | Kanıt gücü ve cloud etiketi; "belgede var ≠ burada çalışıyor" | S14-M2, S15-M2 |

İz ilkesi (birebir): "Yumuşak öz-yargı kendini geçirir … Bağlayan tek şey gözlemlenebilir izdir … mekanik kapı > iz isteyen yazılı prosedür > salt öğüt. Salt öğüt en zayıf biçimdir; ancak geçici köprü olarak meşrudur."
EXP-007 kuralı: Her karşı önlem bu üç düzeyden birine yerleştirilir ve düzeyi yazılır. "Daha dikkatli olacağım" karşı önlem sayılmaz.
Doğuş kuralı: Yeni defo satırı ya da iz kontrolü yalnız yakalanmış bir olaydan doğar; olay satırın yanına adıyla yazılır. Hiç koşulmamış tören önceden kurulmaz.
```
  11–13'ün olay dayanağı: #11 U004 (Batu'nun Claude'a koyduğu teşhis; H-001). #12 Foundation soru bankası: "The assistant nevertheless declared the example finished." (R11 K41). #13 R01'in eksik-arayıcısı, belgeden çıkarılan kabiliyetleri "Abartılı iddialar" başlığıyla listeledi; ana oturum "üç kat iç içe" iddiasını ortamda düşürdü (A003 §3.3).
- **Ne zaman:** Rol dosyası ve görev tanımı yazılırken (ilgili satırlar taşınır); her ateşlenme anında (iz alanı doldurulur); aşama sonunda (iz denetimi, S15-M5); yeni bir olay yakalandığında (doğuş kuralı).
- **Kim:** Ana oturum ve bütün roller uygular. Belgeyi değiştirmek bir METHOD değişikliğidir (S1-M1; T5 S21).
- **Nasıl işler:** 1) Her kartın şablonunda ilgili defonun iz alanı vardır. 2) Ateşlenme anında alan doldurulur. 3) Aşama sonunda çürütücü işlev örneklemde izleri okur. 4) Batu bir defoyu yakalarsa H kaydına defo numarasıyla girer; aynı defo ikinci kez yakalanırsa iz kontrolü güçlendirilir (öğüt → prosedür → mekanik kapı).
- **Zorlama düzeyi:** Yapısal (iz alanları şablonlarda zorunlu) ve zorlayıcı yalnız izin varlığı için (Z1, Z3, Z4). Düşünmenin kendisi zorlanamaz.
- **Çalıştığını nasıl anlarız:** Aşama sonu iz denetiminde örneklemdeki iz alanlarının doluluk oranı. H kayıtlarında defo türlerinin dağılımı. Aynı defonun Batu tarafından ikinci kez yakalanması, karşılığın çalışmadığını gösterir (T5 S21).
- **Bağımlılıklar:** İhtiyaç: T2 (rol dosyalarına satırların taşınması), T5 (CLAUDE.md işaretçisi, ders kaydı), S2-M6. Besler: S15-M2 … S15-M5, S2-M1, S14-M2, S14-M7.
- **Standart seviye kararı:** Gerekli. Önlediği hata: makul görünen çıktı üreten defoların kendiliğinden yakalanmaması (DEFO_MODELI: "makul görünen çıktı üreten defolar (1-4) kendiliğinden asla yakalanmaz"); E71–E74. Kabul testi: aşama sonu iz denetiminde doluluk oranı raporlanıyor ve düşükse karşılık açılıyor.
- **Kaynak:** EkA-1 (loopinance_v2 DEFO_MODELI; uygulayıcı pratiği, bağımsız ölçüm yok); EkA-5 (A4, Batu'nun yazısı: yağcılık, aynalama, şişme, drift, sahte menü, uydurma, öz-onaylama, donma/aşırı sorma, karar yükleme); EkA-6 (sahte seçenek makalesi; †AI ile yazıldı, Batu yayımladı, R03); R11 S15 bileşen 1–2, K33; R03 §2.
- **Bedel:** Bir kez ~5 KB belge; her şablonda 1–3 iz alanı; rol dosyalarında 10–20 satır (her çağrıda bağlama girer).

#### S15-M2 — Protokol disiplininin rollere, görev tanımlarına ve dönüşlere gömülmesi
- **Ne:** AGENT.md protokollerinin (R01, R02, R04, R05, R06; ayrıca R03'ün amaç zinciri) görevle ilgili kısmını, alt ajanın gerçekten okuduğu üç taşıyıcıya yerleştirir: rol dosyasındaki disiplin bloğu, görev tanımı alanları, dönüş iz alanları.
- **Nerede:** (a) Rol dosyalarının gövdesi (T2); (b) görev tanımı şablonu (T2 S13); (c) dönüş şeması (T2 S13). İçerik:

```
(a) Rol dosyası — ortak disiplin bloğu (~15 satır; role özgü satırlar T2'de eklenir)
## Düşünme disiplini (kaynak: AGENT.md protokolleri R01, R02, R04, R05, R06; defo modeli)
- Varsayımlar: Sonucunu taşıyan her varsayımı yaz; "yanlışsa sonuç değişir mi?" sorusunu cevapla. Değiştiriyorsa ve sınayamıyorsan sonucu koşullu yaz: "X doğruysa Y; Z doğruysa değişir."
- Kanıt dışı etki: Görev tanımındaki beklenti, önceki bulgular ya da "kapatalım" baskısı kanıt değildir. Onaylayan bir sonuca varıyorsan onu çürütmeyi denediğini ve neden tuttuğunu yaz.
- Kaynak–temsil: Okuduğun şeyin kaynak mı özet mi olduğunu yaz. "Görmedim" ile "yok" ayrıdır; aramanın kapsamını yaz. Kesik araç çıktısı tam okuma değildir.
- Doğrulama: Kendi kontrolünü "doğrulandı" diye adlandırma; doğrulama sözlüğünü kullan (öz-kontrol, mekanik kontrol, kaynaktan kontrol …).
- Kök neden: Bir hatayı açıklıyorsan iki soruyu ayrı cevapla: neden oldu; neden önlenmedi ya da yakalanmadı.
- Belirsizlik: Bilmiyorsan "bilmiyorum" de; boşluğu doldurma, işaretle. Durman gereken yerde dur; sahte seçenek üretme. Gereken bir şey eksikse ilk satırda eksiği söyle ve dur.

(b) Görev tanımına bu kümenin istediği alanlar (rolün sabit kısmı rol dosyasındadır)
- Beslediği karar ve katmanı (S1-M1): …
- Sınanacak varsayımlar: …
- Bağlayıcı kararlar ve Batu'nun sözleri (birebir): …
- Risk sınıfı ve doğrulama beklentisi (S14-M3): … (genel "tekrar kontrol et" yazılmaz)
- Kabul ölçütü (S14-M1): …
- Bilerek verilmeyenler: … (çürütücüye: üreticinin gerekçesi)
- Taban: HEAD <SHA>; okunacak dosyalar bu sürümden

(c) Dönüş iz alanları
- Durum: TAMAM / ÇEKİNCELİ TAMAM / TAKILDI / BAĞLAM EKSİK
- Bulgular: iddia · kanıt (yol#bölüm, kısa alıntı) · etiket (kaynak diyor / gözledim / çıkarım / varsayım / bilinmiyor) · kanıt türü
- Karar-kritik varsayımlar: varsayım · yanlışsa ne değişir · sınandı mı
- Kendi başıma verdiğim seçimler (Batu'ya gitmesi gerekebilecekler ayrı işaretli)
- Çürütme izi (onaylayan sonuçlarda)
- Okuma kapsamı: her kaynak için tam / kısmi / okunmadı / erişilemedi
- Bu dönüşün kanıtlamadıkları
- Dokunulan dosyalar · Görev tanımı sürümü
```
- **Ne zaman:** Rol dosyası yazılırken (bir kez; rol sürümüyle güncellenir); her görev tanımında; her dönüşte.
- **Kim:** T2 rol dosyasına ve şablonlara yerleştirir; ana oturum görev tanımını doldurur; alt ajan dönüşü doldurur; ana oturum dönüş kapısında denetler (S14-M6).
- **Nasıl işler:** 1) Rol çağrılınca disiplin bloğu rol dosyasının gövdesi olarak sistem istemine girer (EkA-7). 2) Görev tanımı göreve özgü alanları taşır. 3) Dönüş iz alanlarıyla gelir. 4) Dönüş kapısı alanların varlığını, ana oturum içeriklerini denetler.
- **Zorlama düzeyi:** Yapısal (rol dosyası, şablon alanları). Zorlayıcı kısmen: dönüş kapısı alanların varlığını denetler (Z1). Rol dosyasının araç listesi zorlanır, gövdesi tavsiyedir (R07 §4 madde 2).
- **Çalıştığını nasıl anlarız:** Dönüş örnekleminde iz alanlarının doluluğu. "BAĞLAM EKSİK" durum kodunun gerçekten kullanıldığı görülür; hiç kullanılmıyorsa uydurma şüphesi doğar. Çürütücünün H7 bulguları (Batu'nun sözünün yorumla değişmesi) azalır.
- **Bağımlılıklar:** İhtiyaç: T2 (rol dosyaları, şablonlar), T5 (CLAUDE.md'nin alt ajana sızmaması, U7), S15-M1. Besler: S1-M5 (gate'siz alt ajan kararının koşulu), S14-M6, S14-M4.
- **Standart seviye kararı:** Gerekli. Önlediği hata: alt ajanın emir erine dönmesi (E64); disiplinin yalnız istemde yaşaması (E89); R01'in tespiti: "Nothing says whether subagents must run the gate". Kabul testi: 5 rol dosyasında ve 5 görev tanımında taşıyıcılar var; 10 dönüşte iz alanları dolu.
- **Kaynak:** R11 S15 bileşen 9; AGENT.md protokolleri (veri olarak); A003 §3.3 (dokuz alan); R05 satır 1–4; EkA-7 (sub-agents.md: "Subagents receive only this system prompt plus basic environment details like the working directory, not the Claude Code system prompt." — kaynak diyor, C~); R07 §4 madde 7 (konuşma geçmişi alt ajana taşınmaz); R07 §2.6 PRJ ("say exactly what's missing in your first message and stop").
- **Bedel:** Rol başına ~15 satır (her çağrıda bağlam); görev tanımına ~7 satır; dönüşe ~8 alan.

#### S15-M3 — İtiraz ve onay baskısı protokolü
- **Ne:** Batu itiraz ettiğinde, görüş bildirdiğinde ya da bir sonucun kapanmasını istediğinde, pozisyonun kanıta göre değişip değişmediğini açık ve izli biçimde yazar; ne refleks katılım ne inat.
- **Nerede:** METHOD; S2-M1 şablonunun itiraz alt biçimi:

```
**İtirazın:** <birebir kısa alıntı>
**Yeniden inceledim:** <neye baktım: kaynak, kanıt>
**Pozisyonum:** değişti / kısmen değişti / değişmedi — çünkü <kanıt>
**Çürütme izi:** <önceki pozisyonumun en güçlü karşı kanıtı; neden tuttu ya da düştü>
**Yetki:** Konu Y katmanıysa senin kararın geçerli; yalnız kanıt tarafını ve riskini yazdım.
<bitiş biçimi>
```
  Kurallar: Batu'nun Y katmanındaki kararı (amaç, kapsam, yetki) uygulanır; kanıt ve risk açıkça yazılır. Meşru karar girdisi epistemik iddiadan ayrıdır. Batu'nun olgusal ya da teknik iddiası kanıtla sınanır. "Haklısın, bunu düşünmemiştim" cümlesi ancak çürütme iziyle birlikte yazılabilir.
- **Ne zaman:** Batu'nun her itiraz ya da görüş mesajında; kapanış baskısında (S14-M7 §5).
- **Kim:** Ana oturum.
- **Nasıl işler:** 1) İtiraz birebir alınır (S2-M7). 2) Kaynak ve kanıt yeniden okunur. 3) Karşı-olgusal test: "Batu tam tersine inanıyor olsaydı, aynı kanıtlarla aynı sonuca varır mıydım?" 4) Şablonla cevap verilir. 5) İtiraz bir kusuru gösteriyorsa H kaydı açılır.
- **Zorlama düzeyi:** Yapısal (şablon); tavsiye (yeniden inceleme).
- **Çalıştığını nasıl anlarız:** İtiraz cevaplarında çürütme izi var. Arada "değişmedi" cevapları da var; hiç yoksa yağcılık şüphesi doğar. Batu'nun "bir o yana bir bu yana kayıyorsun" tepkisi = 0.
- **Bağımlılıklar:** İhtiyaç: S2-M7, S15-M1 (#1). Besler: S2-M6, W8.
- **Standart seviye kararı:** Gerekli. Önlediği hata: yağcılık ve yönün itirazla savrulması (E72, DEFO #1); öz-onaylı kapanışın yetki sınırını zorlaması (E75). Kabul testi: itiraz cevaplarının hepsinde beş alan dolu.
- **Kaynak:** user-independent-reasoning §2, §6, §11 ve Nihai Kontrol ("Kullanıcı veya stakeholder tam tersine inanıyor olsaydı, aynı kanıtlarla yine aynı sonuca ulaşır mıydım?"); R03 ilke 11 (E5U-01 U002: "Her konuşmada 'haklısın bunu düşünmemiştim' tarzında bir sonuca varacağımız senaryo yaşatırsın bana."), §2 ("bir o yana bir bu yana kayıyor tercihlerin"), §5 madde 12; EkA-1 #1; EkA-5 ("Yağcılık").
- **Bedel:** İtiraz başına ~8 satır; yeniden okuma.

#### S15-M4 — Nedensel derinlik şablonu (olay analizi)
- **Ne:** Batu'nun yakaladığı hata, takılma, doğrulama başarısızlığı ya da kurtarma olayı için yakın nedeni ve "neden önlenmedi ya da yakalanmadı" sorusunu ayrı cevaplayan kısa bir şablon.
- **Nerede:** H kaydının (S2-M6) ve takılma kaydının (S17-M3) alanları; ders kaydına (T5 S21) girdi. H-002 için doldurulmuş örnek:

```
Olay: H-002 (U005; birleştirme çakışması adımı durduruldu)
Yakın neden: main dala birleştirilerek çakışma çözülmeye başlandı
Katkı koşulu: EXP-006 main'de ChatGPT hattında ilerliyordu; dal politikası yazılı değildi
Önleme açığı: main'e dokunan adım bir Y3 (dış etki) idi, ama tetik listesi yoktu; soru olarak gitmedi
Yakalama açığı: sistem yakalamadı; Batu yakaladı
Sistemik neden: yetki sınırları sohbette kaldı; K-002 onaylıydı ama tetikleri yazılı değildi
Düzeltmenin hedefi: önleme (S1-M2 Y3) · Aynı hata sınıfı başka yoldan olur mu: evet (dal silme, PR birleştirme) → hepsi Y3 listesinde
Durma ölçütü: daha derine inmek müdahaleyi değiştirmiyor
```
- **Ne zaman:** H kaydı açılınca; kırmızı alarm çözülünce; devre kesici tetiklenince; kurtarma olayından sonra.
- **Kim:** Ana oturum; tekrar eden ya da yüksek etkili olaylarda çürütücü işlev şablonu denetler.
- **Nasıl işler:** 1) Olay tek cümleyle adlandırılır. 2) Yakın neden, katkı koşulu, önleme açığı, yakalama açığı, sistemik neden ayrı yazılır. 3) Düzeltmenin hangi halkayı değiştirdiği ve aynı hata sınıfının başka yoldan olup olamayacağı yazılır. 4) Durma ölçütü uygulanır.
- **Zorlama düzeyi:** Yapısal (şablon alanları).
- **Çalıştığını nasıl anlarız:** H kayıtlarında iki sorunun (neden oldu; neden önlenmedi/yakalanmadı) ikisi de cevaplı. Düzeltmeler çoğunlukla önleme ya da yakalama halkasını hedefliyor, yalnız semptomu değil. Aynı hata sınıfının tekrarı azalıyor.
- **Bağımlılıklar:** İhtiyaç: S2-M6, S17-M3. Besler: T5 S21 (ders kaydı ve dersin yeri), S15-M1 (doğuş kuralı).
- **Standart seviye kararı:** Olay analizinde gerekli. Küçük mekanik hatada gereksiz; koşul: tek seferlik, tekrar riski yok, kimse dayanmıyor. Önlediği hata: yanlış düzeltme; sorunun adının çözüm sanılması (R11 S15 bileşen 5). Kabul testi: H kayıtlarında şablon dolu.
- **Kaynak:** causal-depth-root-cause-validation §3–§4, §8 (kontrol katmanı metni: "Bu olayın oluşmasına veya bu kadar ilerlemesine neden izin verdik"); R11 S15 bileşen 5; EkA-6 (sahte seçenek makalesi: "Bu bir 'okuma' hatası değil, bir 'sunum' refleksiydi." — kök neden ayrımının örneği).
- **Bedel:** Olay başına ~10 satır.

#### S15-M5 — Uzun koşu öz-denetimi ve iz denetimi
- **Ne:** Uzun özerk koşuda yağcılık, drift, öz-onay ve örtme için kendiliğinden tetiklenen kısa bir iz kontrolü yapar; aşama sonunda bu izleri üreticiden ayrı bir okumayla denetletir.
- **Nerede:** Günlükte ÖZ-DENETİM satırı ve ekli blok; aşama sonunda KAPANIS §5'e ek. Şablon:

```
ÖZ-DENETİM #7 — tetik: 5 kalem kapandı (P1-011 … P1-015)
- Çapa (tek cümle): <aşamanın sorusu> · son 5 kalem ona hizmet ediyor mu: 4 evet, 1 yan dal (P1-014 → park)
- Son 5 Batu etkileşiminde onaylayan cevap: 2 · çürütme izi olan: 2
- Son 5 kapanışta kat ve kanıt: 5/5
- Açık iş deklarasyonu: raporda 3 açık iş yazılı · "paralel hallolur" hafifletmesi: yok
- Sahte menü taraması (son 10 mesaj): 0
- Sonuç: sürdür / yön kontrolüne git (S1-M2) / Batu'ya yükselt
```
  Tetikler: her 5 kapanan kalem; her alt ajan dalgasının (en az 3 paralel dönüş) sonu; sıkıştırmadan sonraki ilk tur; 40 dakikayı aşan kesintisiz özerk koşu. Aşama sonunda çürütücü işlev bu satırları ve örneklem mesajları okur; hata sınıfları: yağcılık, drift, öz-onay, örtme izleri.
- **Ne zaman:** Tetiklerde; aşama sonunda.
- **Kim:** Ana oturum doldurur; aşama sonu denetimi çürütücü işlev (T2).
- **Nasıl işler:** 1) Tetik günlükten sayılır. 2) Beş satır doldurulur. 3) Sonuç "yön kontrolü" ise aşamanın sorusu ve plan yeniden okunur, yan dallar park edilir. 4) Aşama sonunda denetim bulguları S14-M4 akıbetine girer.
- **Zorlama düzeyi:** Yapısal (günlük satırı). Zorlayıcı aday: sıkıştırma sonrası ve oturum açılışında hatırlatma enjekte eden hook (Z6; T5).
- **Çalıştığını nasıl anlarız:** Günlükte her 5 kalemde bir ÖZ-DENETİM satırı var. Aşama sonu denetiminin bulduğu, öz-denetimin kaçırdığı defolar ayrı sayılıyor; bu sayı yüksekse öz-denetim kendini geçiriyor demektir. Batu'nun drift ya da yağcılık yakalaması (H türü) azalıyor.
- **Bağımlılıklar:** İhtiyaç: S17-M1 (sayaç), S15-M1, S14-M4, T3 (ritim tablosu). Besler: S1-M2 (fren), S17-M3 (sarı alarmda ilk adım), W4, W9.
- **Standart seviye kararı:** Gerekli. Kısa işte (5 kalemin altında) gereksiz; koşul: tetik hiç dolmuyorsa. Önlediği hata: çapa yeniden yüklenmeyince turun yerel optimuma çekilmesi (E73); öz-onay döngüsü (R11 §4.5 döngü 2); periyodik yön gözden geçirmesi eksikliği (Y12). Kabul testi: yukarıdaki iki gözlem.
- **Kaynak:** EkA-5 (A4: "Bunu sohbet ortamında yapmak daha kolay. Fakat bir agent oturum içinde 40 dakika boyunca kendi kendine çalışıyorsa, bu kontrolü kendisinin tetiklemesini sağlamak gerekir."); EkA-1 (#4: "çapa DOSYADA yaşar, tur başında okunur"; "Yumuşak öz-yargı kendini geçirir"); R11 S15 bileşen 8; goal-method-end-to-end-validation §6 (çapa yenilemesi maddi geçişlerde).
- **Bedel:** 5 kalemde bir ~10 satır; aşama sonunda bir inceleme koşusu.

### 2.5 S17 — Gözlemlenebilirlik ve ilerleme

**Amaç.** Ne olduğunu, ne kadar ilerlendiğini ve nerede takılındığını görünür kılmak; bunu canlılığı değil ilerlemeyi ölçerek yapmak. Loopinance kanonundaki bekçi 742 kez koştu ama "54 gündür kod yok" demedi; çünkü canlılığı ölçüyordu (EkA-2). Sürekli yetkinin (K-002) freni bu alt sistemdedir. Gözlem güvence değildir; kanıt altyapısıdır (R11 K72 F18).

**R11'e göre değişenler.**
- Düzeltildi: R01 eksik-arayıcının önerdiği "N saat yeni kanonik commit yoksa Batu'ya bildirim" kuralı canlılık ölçüsüdür; commit hareket gösterir, ilerleme göstermez. Burada karar olaylarına çevrildi (çıkarım).
- Eklendi: sessiz alarm kuralı; ara kayıt commit'lerinin ilerleme sayılmaması (ORTAK-SENTEZ "Ara sürümler"); "Batu için gösterge" kararı (ayrı pano yok).
- Gözlem: R01'in önerdiği "PushNotification" aracı bu alt ajanın araç listesinde yok (EkA-18); ana oturumunkinde olup olmadığı bilinmiyor.

**Karar tablosu.**

| Bileşen | Karar | Önlediği hata | Kabul testi | Kaynak | Kart |
|---|---|---|---|---|---|
| Olay ve iş günlüğü | gerekli | ne olduğu sonradan kurulamaz; kayıp iş fark edilmez | W5 günlükten yeniden kuruluyor | R09 GZ-1 | S17-M1 |
| Karar düzeyinde ilerleme ölçüsü | gerekli | canlılığın ilerleme sanılması (E80) | "ilerlemesiz hareket" senaryosunda ölçü "yok" diyor | EkA-2; A003 §3.6 | S17-M2 |
| Takılma türleri | gerekli | yanlış teşhis ve yanlış müdahale | her alarmda tür yazılı | R05 satır 24 | S17-M3 |
| Alarm eşikleri ve devre kesici | gerekli | frensiz sürekli yetki (E81); kör tekrar | eşik aşımında alarm satırı | R08 O17 | S17-M3 |
| Sessiz alarm kuralı | gerekli | fren sinyalinin Batu'ya ulaşmaması (E82) | yanıtsız kırmızıda yeni geçiş yok | çıkarım | S17-M3 |
| Açılış sinyali | gerekli | takılmanın oturumlar boyunca sessiz kalması | her açılışta ilk bilgi | EkA-3 | S17-M4 |
| Kanıta bağlı durum göstergesi | gerekli | beyana dayalı, bayat durum (E82) | gösterge günlükten türetilmiş | R09 GZ-4 | S17-M4 |
| Ayrı Batu panosu | gereksiz (ayrı yüzey olarak) | — | — | — | S17-M4 |
| Ölçü bütünlüğü (bilinmeyen ≠ 0; kısmi ≠ tam; kümülatif toplanmaz) | gerekli | yanlış durdurma ya da kör harcama (E84) | raporlarda "bilinmiyor" sıfır yazılmıyor | R11 K74 | S17-M5 |
| Gözlem sınırı beyanı | gerekli | "iz yok = olmadı" yanılgısı | aşama raporunda paragraf | R09 GZ-8 | S17-M5 |
| Maliyet görünürlüğü | gerekli; ölçüm kaynağı ve bütçe T5 | maliyetin değerden kopması | raporda token ve ilerleme olayı yan yana | R11 S20 | S17-M5 |
| Soy ve karar izi | gerekli; alanları T1 ve T3 | geri çekilen bulgunun etkilediği kararın bulunamaması | TK'da dayanak zinciri | R09 GZ-2 | S1-M4 |
| Platform telemetrisi (OpenTelemetry) | bilinmiyor | — | cloud'da kullanılabilirliği T5 araştırır | R09 §5.1 | §6 |
| Alt ajan transkriptlerinin saklanması | bilinmiyor | — | VM kaybından sonra var mı (R07 §8 soru 5) | R07 BO-7 | §6 |

"Ayrı pano" gerekçesi: Koşul: gösterge STATE'te ve her raporda taşınıyor, günlükten türetiliyor (tek kaynak). Bütünsel etki: Batu oturumu açmazsa göstergeyi görmez; bu risk S2-M5'in kanal pilotu ve S17-M3'ün sessiz alarm kuralıyla karşılanır. Yeniden değerlendirme tetiği: Batu "durumu tek yerde görmek istiyorum" derse ya da pilot sohbetin yetmediğini gösterirse.

#### S17-M1 — Çalışma günlüğü
- **Ne:** Oturumlar arası "ne oldu"yu tek yerde, ekleme-yalnız ve makinece sayılabilir satırlarla tutar.
- **Nerede:** `GUNLUK.md` (EXP-007 düzeyinde; aşama başına dosyaya bölünebilir; yol T1'in). Tek yazıcı: ana oturum. Bir olay bir satır, sabit sütun sırası. Örnek (bu turun olaylarından; zaman ve SHA'lar temsilidir):

```
| Zaman (UTC) | Oturum | Olay | Kalem | Aktör | Referans | İ | Token | Not |
|---|---|---|---|---|---|---|---|---|
| 2026-09-27T09:33 | s-01MaRi | DAGITIM | P0.4-T4 | ana oturum → T4 küme ajanı | briefs/T4.md @ 8e82c34 · HEAD 8e82c34 | | | 5 paralel |
| 2026-09-27T11:40 | s-01MaRi | DONUS | P0.4-T4 | T4 küme ajanı | drafts/T4-yon-yetki-ve-denetimler.md @ <sha> | | bilinmiyor | durum: TAMAM |
| 2026-09-27T11:55 | s-01MaRi | KAPI | P0.4-T4 | ana oturum | dönüş kapısı listesi | | | kat Y→K |
| 2026-09-27T12:10 | s-01MaRi | KARAR | P0.4 | ana oturum | TK-P0-004 | İ | | katman T |
| 2026-09-27T12:20 | s-01MaRi | YAYILIM | K-011 | ana oturum | 3 yüzey · 2 çalışan iş | | | 1 bildirildi, 1 uzlaştırılacak |
```
  Olay sözlüğü (sabit): DAGITIM · DONUS · KAYIP · KAPI · KARAR · SORU-ACILDI · SORU-KAPANDI · DOGRULAMA · KABUL · YAYILIM · ALARM-SARI · ALARM-KIRMIZI · ALARM-KAPANDI · OZ-DENETIM · SIKISTIRMA · OTURUM-ACILIS · OTURUM-KAPANIS · KONTROL-NOKTASI · HATIRLATMA · DUZELTME.
  "İ" sütunu yalnız S17-M2'deki ilerleme olaylarında dolar. "Token" görev bildirimindeki alt ajan değeridir; yoksa "bilinmiyor" yazılır, 0 yazılmaz.
  Kurallar: Satır silinmez; düzeltme yeni DUZELTME satırıyla yapılır. Alt ajanlar günlüğe yazmaz.
- **Ne zaman:** Her olayda; en geç kalem kapanışında toplu. Ortamın Stop hook'u her tur sonunda commit ve push'u zorladığı için satırlar her turda kalıcılaşır (EkA-12).
- **Kim:** Ana oturum.
- **Nasıl işler:** 1) Olay olunca satır eklenir. 2) DAGITIM satırına dağıtım anındaki HEAD yazılır. 3) DONUS yoksa ve süre ya da oturum değiştiyse KAYIP şüphesi (S17-M3). 4) Rapor ve gösterge sayıları buradan hesaplanır.
- **Zorlama düzeyi:** Yapısal (sabit sütun ve olay sözlüğü). Zorlayıcı aday önerilmez: dağıtım satırının hook'la otomatik yazılması mümkün görünüyor (PostToolUse), ama görev tanımı yolunun hook girdisinden güvenle alınıp alınamayacağı bilinmiyor.
- **Çalıştığını nasıl anlarız:** W5 senaryosu günlükten yeniden kuruluyor (açık dağıtımlar = DONUS'u olmayan DAGITIM'lar). STATE'teki maliyet notu gibi özetler günlükten türetilebiliyor. Bozulma işareti: DONUS'u olmayan eski DAGITIM; "0" yazılmış token.
- **Bağımlılıklar:** İhtiyaç: T1 (yer, arşivleme ve budama; T1'in bellek türlerindeki "oturum günlüğü" ile aynı dosya olmalı), T5 (token kaynağı). Besler: S17-M2 … M5, S2-M2, S2-M7 (yayılım), S15-M5, W5, W6.
- **Standart seviye kararı:** Gerekli. Önlediği hata: ne olduğunun sonradan kurulamaması (R11 S17 bileşen 1); commit okumadan denetleyememe (E09); VM'de kalan transkriptlere bağımlılık (R07 BO-7: kalıcılığı C?). Kabul testi: W5'in günlükten yeniden kurulması.
- **Kaynak:** R11 S17 bileşen 1; R09 GZ-1: "Her çağrı için bir satır: görev tanımı kimliği ve sürümü, rol, başlangıç HEAD'i, başlama ve bitiş, statü kodu, çıktı dosyası, dokunduğu dosyalar, token ve süre (ölçülemiyorsa 'bilinmiyor')" (çıkarım; R09 sentezi); R08 O19 (ekleme-yalnız günlük) ve §8 "Gözlemlenebilirlik: Al"; R07 BO-7.
- **Bedel:** Olay başına ~100 bayt; P0 hızında günde tahminen 30–60 satır; dosya büyür, aşama sonunda arşivlenir (T1).

#### S17-M2 — Karar düzeyinde ilerleme ölçüsü
- **Ne:** İlerlemeyi dosya, commit ya da ajan sayısıyla değil dört olay türüyle ölçer; "son ilerleme olayından bu yana" mesafeyi her an hesaplanabilir tutar.
- **Nerede:** METHOD'da tanım; günlükte "İ" sütunu; STATE ve raporlarda gösterge (S17-M4). Tanım:

```
| İlerleme olayı (İ) | Sayılır, eğer | Sayılmaz |
|---|---|---|
| Kapanan soru | Kuyruktaki ya da plandaki bir soru kanıtla ya da Batu kararıyla kapandı (SORU-KAPANDI) | sorunun yeniden ifadesi ya da alt sorulara bölünmesi |
| Verilen ya da değişen karar | K-xxx ya da yeni/yerine koyan TK (KARAR; katman T ya da Y) | M kararları; biçim, yeniden adlandırma; aynı kararın kopyası |
| Doğrulanmış teslimat | Teslimat K katından Ç ya da İ katına çıktı (DOGRULAMA) | Y katı ("alt ajan bitti dedi") |
| Kabul | Batu kabulü @ SHA (KABUL) | Batu'nun paket dışı olumlu yorumu |

Mesafe ölçüleri: (a) son İ olayından bu yana kapanan kalem sayısı · (b) alt ajan dalgası sayısı · (c) takvim süresi ve bu sürede hareket satırı olup olmadığı · (d) son KABUL'den bu yana aşama geçişi.
Hareket satırı: İ olmayan her günlük satırı. "Hareket var, ilerleme yok" = hareket satırları birikirken İ olayı yok.
Vekil ölçü notu: Kararı bölmek ya da gereksiz revizyon yapmak ölçüyü şişirir. Bu yüzden raporda kararlar sayıyla değil adıyla verilir; aşama sonunda çürütücü işlev "hangi kararlar gerçekten karar?" örneklemi yapar.
```
- **Ne zaman:** Her günlük satırında (İ işareti); açılışta, her kontrol noktasında ve alarm denetiminde (mesafe hesabı).
- **Kim:** Ana oturum işaretler; hesap betikle ya da elle yapılır.
- **Nasıl işler:** 1) Olay türü tabloya göre İ alır ya da almaz. 2) Mesafe ölçüleri son İ satırından hesaplanır. 3) Sonuç göstergeye ve alarm denetimine gider.
- **Zorlama düzeyi:** Yapısal (tanım ve sütun); hesap mekanik (Z2 betiği).
- **Çalıştığını nasıl anlarız:** Senaryo testi (W9): yalnız dosya ve ajan hareketi olan 3 kalemlik bir günlük parçasında ölçünün "ilerleme yok" vermesi. Gerçek kullanımda sarı alarmların ne kadarının gerçek takılma çıktığı izlenir (yanlış pozitif oranı).
- **Bağımlılıklar:** İhtiyaç: S17-M1, S14-M2 (katlar), S1-M4 (karar kayıtları), S2-M3 (sorular), T3 (kalem kapanışı). Besler: S17-M3, S17-M4, S2-M2, S1-M2 (fren).
- **Standart seviye kararı:** Gerekli. Önlediği hata: canlılığın ilerleme sanılması (E80: "İlerleme ölçülmedi, sadece canlılık ölçüldü."); özerk döngünün ilerleme yokken ilerleme bildirmesi (E81); şişen "tamam"ın ilerleme sayılması (E69). Kabul testi: senaryo testinin geçmesi.
- **Kaynak:** A003 §3.6 ("İlerlemenin ölçüsü: dosya ya da ajan sayısı değil; kapanan soru, verilen karar, kabul edilen çıktı."); R05 satır 26: "Count progress as a changed decision or explanation, not as documents or subagent runs" (kaynak diyor; alt ajan raporu); EkA-2 (§2, §3 ders 5); R11 S17 bileşen 2; R09 GZ-6; R08 O17 (Magentic `is_progress_being_made`).
- **Bedel:** Olay başına bir sütun; raporda dört sayı ve bir liste.

#### S17-M3 — Takılma tespiti, alarm eşikleri, devre kesici
- **Ne:** İlerleme olaylarının kesilmesini ve döngüleri türüne göre tespit eder; iki eşikli alarmla müdahaleyi seçer; aynı işin kör tekrarını keser; alarm Batu'ya ulaşmazsa sistemi yavaşlatır.
- **Nerede:** METHOD; günlükte ALARM satırları; gerekirse olay analizi (S15-M4). İçerik:

```
## Takılma türleri
| Tür | Günlükteki işaret | Müdahale |
|---|---|---|
| Engelli | açık Y-tetikli soru var; bağlı kalemler bekliyor | etkilenmeyen kalemlere geç; soru gönderilmediyse hemen gönder |
| Bekliyor | DAGITIM var, DONUS yok, süre beklenen içinde | bekle; mesaj "Şunu bekliyorum; senden karar yok" |
| İşçi kayıp | DAGITIM var, DONUS yok; oturum ya da VM değişti ya da süre aşıldı | kısmi yazımı uzlaştır (git status); aynı görev tanımıyla yeniden başlat (T5 S18); ikinci kayıpta sarı |
| İşçi yok | plan açık kalem gösteriyor ama hazır kalem yok | plan grafiğini denetle (T3); boş hazır liste bozuk grafik olabilir |
| Döngü | aynı kalem 3 kez yeniden açıldı ya da aynı adım 3 kez TAKILDI/başarısız | devre kesici: kör tekrar yok; park ve yeniden plan ya da yükseltme |
| Hareket var, ilerleme yok | İ olmadan eşik aşıldı | dilim ve çerçeve kontrolü: karar üretemeyen dilim soru üretir; daralt |

## Eşikler (başlangıç değerleri; pilotta ayarlanır)
Sarı: son İ olayından bu yana 3 kalem kapandı ya da 2 alt ajan dalgası döndü ya da 12 saat boyunca hareket satırı var ama İ yok.
  → S15-M5 öz-denetim ve yön kontrolü; türe göre müdahale; ALARM-SARI satırı; Batu'ya sonraki kontrol noktasında.
Kırmızı: 5 kalem ya da 4 dalga ya da 24 saat; ya da devre kesicinin ikinci tetiklenmesi; ya da sarının 2 kontrol noktası boyunca kapanmaması.
  → Batu'ya hemen alarm mesajı (S2-M1 biçimi; öneriyle: "Sıkıştık; önerim şu kalemi şöyle daraltmak"); ALARM-KIRMIZI satırı.
Sessiz alarm kuralı: Kırmızı alarm Batu'dan cevap almadan 24 saat kalırsa yeni aşama geçişi ve yeni paralel dağıtım yapılmaz; açık kalemler kapatılır.
Devre kesici: Aynı adım (aynı görev tanımı türü ya da aynı düzeltme) 3 başarısızlıktan sonra durur. Dördüncü deneme yalnız değişmiş görev tanımı ya da planla ve günlükte gerekçeyle yapılır.
```
- **Ne zaman:** Her kalem kapanışında ve her dalga dönüşünde (eşik denetimi); her oturum açılışında (Z2).
- **Kim:** Ana oturum; kırmızıda Batu bilgilendirilir; karar Batu'nun ise soru kuyruğuna.
- **Nasıl işler:** 1) Mesafe (S17-M2) eşiklerle karşılaştırılır. 2) Tür günlükten belirlenir. 3) Müdahale uygulanır ve ALARM satırı yazılır. 4) Çözülünce ALARM-KAPANDI satırı ve kısa neden analizi (S15-M4). 5) Sessiz alarm kuralının süresi günlükten izlenir.
- **Zorlama düzeyi:** Yapısal (eşikler METHOD'da; hesap günlükten). Zorlayıcı aday: açılışta eşiği hesaplayıp alarmı bağlamın başına koyan SessionStart hook'u (Z2). Sessiz alarm kuralı yapısal ve tavsiye düzeyindedir; mekanik zorlaması yok.
- **Çalıştığını nasıl anlarız:** W9 senaryo testi. Gerçek sarı alarmların sonucu (gerçek takılma ya da yanlış pozitif) günlükte. Batu'nun takılmayı Claude'dan önce fark etmesi = 0 (H türü "takılma").
- **Bağımlılıklar:** İhtiyaç: S17-M1, S17-M2, S15-M5, S15-M4, S2-M5 (bildirim), T3 (plan grafiği, dilim boyutu), T5 (yeniden başlatma, kanal). Besler: S1-M2 (Y7, fren), S2-M2, W5, W9.
- **Standart seviye kararı:** Gerekli; eşiklerin doğru değerleri bilinmiyor (pilotta ayarlanır, R11 §7.1 soru 2). Önlediği hata: 742 koşu / 54 gün (E80); frensiz sürekli yetki (E81); bayat pano ile Batu'nun tek döngüsünün yanlış yönlenmesi (E82); kör tekrarın maliyeti. Kabul testi: senaryo testinin geçmesi; ilk iki aşamada yanlış pozitif oranının raporlanması.
- **Kaynak:** EkA-2 (loopinance: "7 gün ya da kod üretmeyen 3 oturum olursa ilk söylenen şey bu olur: 'Sıkıştık, daraltalım.'"; "Dilim doğru sayı üretemiyorsa soru üretir."); R05 satır 24: "All can look superficially like 'not progressing'" ve "circuit-broken" after 3 failures (kaynak diyor; alt ajan raporu); R08 O17 (Magentic `max_stalls`=3; BMAD v4 "3 failures"); R01 eksik-arayıcı (stall kuralı önerisi; burada karar olayına çevrildi); R11 S17 bileşen 3–4.
- **Bedel:** Kalem başına bir karşılaştırma; alarm başına birkaç satır; yanlış pozitiflerin maliyeti.

#### S17-M4 — Açılış sinyali ve durum göstergesi (Batu için gösterge)
- **Ne:** Her oturumun ilk işi ilerleme ve takılma durumunu söylemektir. Aynı gösterge STATE'in başında ve her kontrol noktası raporunda, kanıta bağlı olarak durur. Ayrı pano kurulmaz.
- **Nerede:** STATE.md'nin başında "Durum göstergesi" bloğu (6 satır); S2-M2 raporundaki blok. Şablon (değerler kurgusal):

```
## Durum göstergesi (günlükten hesaplandı: 2026-10-04T08:00Z · GUNLUK @ <sha>)
- Son ilerleme olayı: 2026-10-03, KARAR TK-P1-006 · o zamandan beri: 1 kalem, 0 dalga
- Alarm: yok (son sarı: 2026-10-01; kapandı: dilim daraltıldı)
- Açık: soru 2 (çerçeve 0) · çalışan alt ajan 1 (DAGITIM 2026-10-04T07:40) · bekleyen kabul: yok
- Bu aşamada: İ olayları 14 · doğrulanmış teslimat 3 · kabul 0
- Son kontrol noktası: KN-P1-03 (2026-10-03) · sonraki: 5 kalemde ya da 2026-10-05
- Maliyet (T5): aşama toplamı ≥ 3,1 M token (2 koşu bilinmiyor)
```
  Açılış sinyali: Yeni oturum ve sıkıştırmadan sonraki ilk tur bu bloğu günlükten yeniden hesaplar. Günlükte bloktan yeni satır varsa blok bayattır; önce güncellenir. Sarı ya da kırmızı alarm varsa ilk söylenen şey odur.
  Hook betiği örneği (Z2; T5 sınar; çalıştırılmadı):
```bash
#!/bin/bash
# .claude/hooks/acilis-sinyali.sh — SessionStart (startup|resume|compact)
G="$CLAUDE_PROJECT_DIR/explorations/EXP-007-devos-claude-calisma-duzeni/GUNLUK.md"
[ -f "$G" ] || exit 0
son_i=$(awk -F'|' '$8 ~ /İ/ {z=$2} END {gsub(/ /,"",z); print z}' "$G")
kalem=$(awk -F'|' -v t="$son_i" '{gsub(/ /,"",$2)} $2 > t && $4 ~ /KAPI/ {n++} END {print n+0}' "$G")
alarm=$(grep -E 'ALARM-(SARI|KIRMIZI)' "$G" | tail -1 | cut -d'|' -f2,4,10)
yetki=$(sed -n '/^## Yetki/,/^## /p' "$CLAUDE_PROJECT_DIR/explorations/EXP-007-devos-claude-calisma-duzeni/STATE.md" | head -8)
jq -n --arg c "Açılış sinyali: son ilerleme olayı ${son_i:-yok}; o zamandan beri kapanan kalem $kalem. Son alarm: ${alarm:-yok}. Alarm varsa ilk söyleyeceğin şey budur.
$yetki" '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:$c}}'
```
- **Ne zaman:** Her oturum açılışında, devamda ve sıkıştırma sonrasında; her kontrol noktası raporunda; STATE güncellenirken.
- **Kim:** Ana oturum (ya da Z2 hook'u); STATE bloğunu ana oturum yazar.
- **Nasıl işler:** 1) Blok günlükten hesaplanır. 2) Alarm varsa ilk mesaj alarmı söyler (S2-M1). 3) Yoksa açılış protokolü sürer (T5). 4) Rapor aynı bloğu taşır.
- **Zorlama düzeyi:** Zorlayıcı aday: SessionStart hook'u (Z2); kaynak diyor: SessionStart `additionalContext` "String added to Claude's context at the start of the conversation" ve 10.000 karakter sınırı (EkA-10); C! yalnız tek repolu oturumda; A-04. Kurulmazsa yapısal: açılış protokolünün ilk adımı günlüğün son 30 satırını okumaktır.
- **Çalıştığını nasıl anlarız:** Açılıştan sonraki ilk mesajlarda gösterge var; alarm varsa ilk cümle alarm. Gösterge ile günlük arasında tutarsızlık yok. Bozulma işareti: kanondaki bayat "sıradaki oturum" satırı türünden bayat gösterge.
- **Bağımlılıklar:** İhtiyaç: S17-M1, S17-M2, S17-M3, S1-M2 (Yetki bloğu), T1 (STATE biçimi), T5 (Z2 kurulumu, açılış protokolü). Besler: W1, W4, S2-M2.
- **Standart seviye kararı:** Açılış sinyali gerekli; STATE göstergesi gerekli; ayrı pano gereksiz (gerekçe tablonun altında). Önlediği hata: takılmanın oturumlar boyunca sessiz kalması; bayat pano (E82). Kabul testi: yukarıdaki iki gözlem.
- **Kaynak:** EkA-3 (loopinance_v2 CLAUDE.md: "oturum açılışında son koddan bu yana geçen günü basar. Eski düzen iki ay kod üretmeden koşmuştu. Durma sinyali varsa, ilk söylenen şey o olur."); EkA-2 ("Panodaki 'sıradaki oturum' satırı bile bayat ve yanlıştı."); R09 GZ-3, GZ-4; R07 BZ-4; R11 S17 bileşen 6.
- **Bedel:** Açılışta birkaç satır okuma; hook seçilirse bir betik bakımı; bağlama ~600 karakter.

#### S17-M5 — Ölçü bütünlüğü, gözlem sınırı, maliyet görünürlüğü
- **Ne:** Ölçülerin her tüketicide aynı anlamı taşımasını, bilinmeyenin sıfır sayılmamasını, kısmi olanın tam sayılmamasını ve kaydın neyi görmediğinin yazılmasını sağlar; maliyeti ilerlemeyle yan yana gösterir.
- **Nerede:** METHOD; günlük kuralları; rapor blokları. Kurallar:

```
1. Bilinmeyen ≠ 0: token ya da süre ölçülemediyse "bilinmiyor"; toplamda "≥ X (n koşu bilinmiyor)".
2. Kümülatif değerler toplanmaz: aynı koşunun ara ve son değerlerinden yalnız son değer alınır.
3. Kısmi ≠ tam: yarım yazılmış dosya ya da ara kayıt commit'i ("checkpoint … while … still writing") teslimat değildir; günlükte "kısmi" notu; İ olayı üretmez.
4. Taban yok: karşılaştırılacak önceki ölçüm yoksa "taban yok" yazılır; ilk ölçüm "istikrarlı" sayılmaz.
5. Gözlem sınırı: her aşama raporunda bir paragraf: görülmeyenler (alt ajanın ara adımları, kesilen araç çıktıları, VM'de kaybolan transkriptler, Batu'nun fark etmediği hatalar). "İz yok" = "olmadı" değildir.
6. Maliyet ile değer birlikte: aşama raporunda token ile İ olayı sayısı yan yana verilir; tek başına token verimlilik sayılmaz.
```
  Bu turdan gerçek örnekler: STATE'in maliyet notu, "R09'un sayacı düşük görünüyor; ölçüm güvenilirliği açık bir soru." (gözledim). Ara kayıt commit'leri: `26c05f6 EXP-007: checkpoint R10 and R11 notes while their agents are still writing (in progress)` (EkA-20; gözledim) — bu commit'lerdeki notlar teslimat değildi.
- **Ne zaman:** Her ölçü yazımında; her aşama raporunda (gözlem sınırı ve maliyet).
- **Kim:** Ana oturum; token kaynağı ve bütçe T5'in (S20).
- **Nasıl işler:** 1) Günlüğe yazarken kurallar uygulanır. 2) Rapor hesaplanırken 1–4 denetlenir. 3) Aşama raporuna 5 ve 6 eklenir.
- **Zorlama düzeyi:** Yapısal ve tavsiye; mekanik destek: günlükte "Token" sütununda "0" arayan grep.
- **Çalıştığını nasıl anlarız:** Raporlarda "bilinmiyor" hiçbir yerde sıfır olarak yazılmamış. Kısmi dosyalar teslimat sayılmamış. Her aşama raporunda gözlem sınırı paragrafı var.
- **Bağımlılıklar:** İhtiyaç: S17-M1, T5 (S20 ölçüm kaynağı: görev bildirimindeki alt ajan tokenı; bütçe eşikleri). Besler: S2-M2, S17-M4, T5 S20.
- **Standart seviye kararı:** Gerekli. Önlediği hata: maliyet ölçüsünün anlamını kaybedip durdurma kararını yanlış tetiklemesi (E84; ECC'de kümülatif satırların toplanması); kısmi koşunun tam sayılması (R09 §5.3); yokluk iddialarının yanlış kurulması (R09 GZ-8). Kabul testi: yukarıdaki üç gözlem.
- **Kaynak:** R11 S17 bileşen 5 ve 7, K74 (ECC: "No usable measurement can become a new zero rather than an unknown"); R09 GZ-5, GZ-8 ve §5.3; STATE (maliyet notu); ORTAK-SENTEZ "Ara sürümler".
- **Bedel:** Düşük: yazım kuralı; aşama başına bir paragraf.

### 2.6 Bütünsel etkileşim, döngü kırıcılar, kümenin ağırlığı ve kendi söz–çıktı kontrolü

#### 2.6.1 R11 §5'teki "yeterli görünüp yetersizleştiren" seçimlerin bu kümedeki dengeleyicileri

| Seçim (R11 §5) | Zayıflattığı | Bu kümedeki dengeleyici |
|---|---|---|
| Y1 Kısa sohbet, ayrıntı repoda | kabul ve yön düzeltmesi körleşir | S2-M2 kontrol noktası raporu (commit okumadan denetim), S2-M4 kabul paketi, bağlantılar |
| Y2 Ana oturum az okur | koordinatör yalnız özetle karar verir | S14-M6 karar taşıyan iddiaların kaynaktan kontrolü |
| Y6 Aynı modelle karşı-okuma | "doğrulandı" şişer, ortak kör nokta görünmez | S14-M2 sözlüğü, S14-M5 hata duyarlılığı, kabul paketinde "bağımsız doğrulama yapılmadı" satırı |
| Y7 Riske orantılı kontrol | "düşük risk" eleştirisiz kararları yayar | S14-M3 aşağı akış yükü sorusu (b) |
| Y8 En fazla üç eleştiri turu | park edilen bulgular birikir | S14-M4 bulgu akıbeti, park kaydı; kabul paketinde bilinen açıklar |
| Y11 Sorular birikir, iş durmaz | yanlış çerçeve geç fark edilir | S2-M3 çerçeve sorusu istisnası; "etkilediği kalemler" ve "cevap gelmezse" alanları |
| Y12 Sürekli yetkiyle kendiliğinden geçiş | tek fren gözlem olur | S17-M2, S17-M3 (sessiz alarm dahil), S15-M5 yön kontrolü, S1-M2 duraklar |
| Y13 Hatırlatma sayısı başarı ölçüsü | vekil ölçü tuzağı | S2-M6 eşli ölçüler |
| Y16 "Batu'ya sormak son seçenek" | değer seçimleri sessizce verilir | S1-M3 otomatik seçim kaydı ve toplu sunum |
| Y19 Güvenliği hook'larla zorlamak | gereksiz durma; kapsam yanılsaması | S15-M1 iz ilkesi: hook yalnız bilinen kayma noktalarında ve yalnız izin varlığına (Z1–Z6, her birinin olay dayanağı §3.3'te) |

#### 2.6.2 R11 §4.5'teki döngüler ve bu kümenin kırıcıları
- **Öz-onay döngüsü (S15 → S14 → S17 → S1 → S15):** S14-M2 "doğrulandı" sınırı; S17-M2'de Y katı ilerleme sayılmaz; S1-M2 frenleri; S15-M5'te öz-denetimin aşama sonunda başka bir okumayla denetlenmesi. Döngünün her halkasında bir kırıcı var (çıkarım).
- **Batu yükü döngüsü (S4 → S2 → S14 → S2):** S2-M5 dikkat bütçesi; S2-M6 kaçak oranı ("sistem yakalayabilir miydi?") hangi mekanizmanın çalışmadığını gösterir; S14-M7 §2 kimseye verilmemiş iş taraması (yöntem T3); S1-M3 "türet, sorma".
- **Kural birikimi döngüsü (S21 → S19 → S7 → S15 → S21):** S15-M1 doğuş kuralı (olaysız kural yok) ve iz ilkesi (öğüt → prosedür → mekanik kapı sırası). Dersin yerini seçmek T5'in.
- **Şişme döngüsü (S9 → S7 → S20 → S10 → S18 → S9):** S2-M5 kelime sınırları; DEFO #3 "neyi kırptım?" izi; ayrı pano ve ayrı yönetişim dosyasının kurulmaması.

#### 2.6.3 Kümenin ağırlığı (ENTEGRASYON'un ağırlık bütçesine girdi)

| Ritim | Mekanizma | Tahmini bedel |
|---|---|---|
| Her mesaj | S2-M1 bitiş biçimi; geçici olarak routing bloğu | ~10 satır blok ve yazım disiplini |
| Her olay | S17-M1 günlük satırı | ~100 bayt |
| Her kalem | S14-M1 ölçüt, S14-M3 risk sınıfı, S1-M1 katman, S14-M6 dönüş kapısı | 5–15 dakika ana oturum işi |
| R2/R3 kalem | S14-M4 çürütücü | bir alt ajan koşusu |
| Her 5 kalem | S15-M5 öz-denetim ve S2-M2 kontrol noktası (aynı anda) | ~1 sayfa |
| Her aşama | S14-M7 kapanış, S14-M8, S14-M9, S2-M2 aşama raporu, S2-M4 kabul (durakta), S15-M5 iz denetimi | 2–3 alt ajan koşusu ve 2–3 sayfa |
| Rol sürümü değişince | S14-M5 hata duyarlılığı | bir koşu ve ~1 saat hazırlık |
| Batu'nun dikkati | aşama başına ≤ ~1.500 kelime; kontrol noktası başına ≤ 3 soru | — |

Hafiflik dengeleyicileri: R0 kalemlerde çürütücü yok; M kararları Batu'ya görünmez; ayrı pano ve ayrı yönetişim dosyası yok; alt ajanda gate yok; hata duyarlılığı yalnız rol sürümü başına; genel "tekrar kontrol et" yasak; öz-denetim ve kontrol noktası aynı ritimde birleşik.

#### 2.6.4 Bu taslağın kendi söz–çıktı kontrolü (T4.md → kartlar)

| T4.md maddesi | Karşılık |
|---|---|
| S1 karar katmanları | S1-M1 |
| S1 sürekli yetki ve frenleri (ilerleme ölçüsü, takılma alarmı, yükseltme tetikleri) | S1-M2; S17-M2; S17-M3; S15-M5 |
| S1 yetki tablosu | S1-M1 |
| S1 AGENT.md ilişkisi; A-01 varsayımı | S1-M5 |
| S1 protokollerin ana oturumda ve alt ajanlarda işleyişi | S1-M5 (tablo); S15-M2 |
| S1 routing bloğunun ne zaman görüneceği | S1-M5 (geçici tablo; U3) |
| S1 otomatik uyandırmaların kullanıcı turu sayılıp sayılmadığı | S1-M5 (geçici tablo; U2); S1-M2 madde 6 |
| S2 rapor biçimi ve uzunluğu (D010) | S2-M1; S2-M2 |
| S2 Batu'nun dikkati: bütçe; ne okur, ne okumaz | S2-M5 |
| S2 soruların biriktirilmesi ve önerisiyle gelmesi | S2-M3 |
| S2 kabul protokolü; SHA'ya bağlılık | S2-M4 |
| S2 bildirim zamanlaması | S2-M5 |
| S2 Batu'nun sözünün kayda geçişi; S10 arayüzü | S2-M7; §3.1 İ1 |
| S2 Batu'nun yakaladığı hataların ölçülmesi; tamamlayıcı ölçüler | S2-M6 |
| S14 ölçüt işten önce | S14-M1 |
| S14 tamamlanma katları | S14-M2 |
| S14 doğrulama türleri, bağımsızlık etiketleri, çürütme; aynı model karşı-okuması doğrulama değil | S14-M2; S14-M4; S14-M5 |
| S14 kimseye verilmemiş iş | S14-M7 §2 (yöntem T3 S4) |
| S14 "standart mı, yeterli mi" | S14-M9 |
| S14 söz–çıktı izlenebilirliği | S14-M8 |
| S14 kontrolün riskle orantılı ağırlığı | S14-M3 |
| S15 protokollerin rollere ve görev tanımlarına gömülmesi | S15-M2; S1-M5 |
| S15 defo modeli (A4, loopinance, dalkavukluk, aşırı kesinlik, erken kapanış, kapsam daraltma) | S15-M1 |
| S15 karşı önlemler | S15-M1 tablosu; S15-M3; S15-M4; S15-M5 |
| S17 çalışma günlüğü | S17-M1 |
| S17 karar düzeyinde ilerleme | S17-M2 |
| S17 takılma tespiti ve devre kesici | S17-M3 |
| S17 maliyet görünürlüğü | S17-M5; S17-M1 (Token sütunu) |
| S17 Batu için gösterge | S17-M4 |
| Arayüz: T2'den doğrulayıcı ve eleştirmen rolleri | §3.1 İ7–İ9 |
| Arayüz: T3'ten kapılar ve plan | §3.1 İ14–İ20 |
| Arayüz: T1'den özet sadakati kontrolleri | §3.1 İ4 |
| Arayüz: T5'ten hook'lar ve maliyet ölçümü | §3.1 İ21–İ22; §3.3 |
| U004 eleştirisinin kalıcı kontrole dönüşmesi | S14-M8; S14-M9; S15-M1 #11 |

Karşılanmadı olarak kalan madde yok. Kısmen karşılananlar: bildirim kanalı (bilinmiyor; pilot), eşiklerin doğru değerleri (pilot), Batu'nun bilişsel yükünün doğrudan ölçümü (vekillerle).

---

## 3. Arayüzler

### 3.1 T4'ün diğer kümelerden istedikleri

| No | Kimden | İstenen | Hangi kart için |
|---|---|---|---|
| İ1 | T1 | Batu'nun sözlerinin birebir deposu ve statü etiketi sözlüğü (amaç / kısıt / karar / örnek / çağrışım / açık soru) | S2-M7 |
| İ2 | T1 | Dosya yerleri: GUNLUK, HATIRLATMALAR, SOZ-CIKTI, KAPANIS, KABUL, raporlar/, reviews/, reviews/kalibrasyon/, DEFO-MODELI; DECISIONS "Açık sorular" tablosunun genişletilmesi; TK kayıt biçimi; STATE'te "Yetki" ve "Durum göstergesi" blokları | hepsi |
| İ3 | T1 | Yayılım kontrolü: bir karar değişince bağlı yüzeylerin listesi ve güncellenmesi (S9) | S2-M7, W6 |
| İ4 | T1 | Özet sadakati kontrolleri (nitelik koruyan özet şablonu; özet yeterliği sınaması); S14 bunları doğrulama türü olarak kullanır, çürütücünün H2/H7 sınıfları buna dayanır | S14-M4 |
| İ5 | T1 | Sıkıştırma sonrası yeniden okuma listesine AGENT.md, yüklü protokoller ve STATE Yetki bloğu | S1-M5, W4 |
| İ6 | T1 | Batu'nun terim sözlüğü | S2-M1, S2-M5 |
| İ7 | T2 | Çürütücü inceleme işlevini taşıyan kalıcı rol: taze bağlam, salt okuma araç listesi, ayrı girdi, H1–H7 hata sınıfları, bağımsızlık etiketi, sürüm ve kalibrasyon kaydı | S14-M4, S14-M5, S15-M5 |
| İ8 | T2 (ve T3) | Eksik-arayıcı işlev: görev tanımından bağımsız kaynak alanı | S14-M7 §2 |
| İ9 | T2 | Rol dosyalarına S15-M2(a) disiplin bloğu ve defo modelinin role özgü satırları; görev tanımı şablonuna S15-M2(b), dönüş şemasına S15-M2(c) alanları | S15-M2, S14-M6 |
| İ10 | T2 | Rol değişikliği yetki tablosu (R10 §5.4); S1-M1 buna atıf yapar | S1-M1 |
| İ11 | T2 | Çalışan alt ajana karar bildirimi mekanizması ve geç dönüşün görev tanımı sürümüne göre uzlaştırılması (W6) | S2-M7 |
| İ12 | T2 | Rol dosyasında araç izni ile karar yetkisinin ayrı alanlar olması (E04) | S1-M1 |
| İ13 | T2 | Tek yazıcı: GUNLUK, DECISIONS, STATE yalnız ana oturumda; alt ajanın yazma listesi | S17-M1, S14-M6 |
| İ14 | T3 | P0–P6 haritası ve geçiş türleri (kendiliğinden / durak); K-002 eşlemesi için | S1-M2 |
| İ15 | T3 | Kalem şemasında "Bitti tanımı", "Kabul testleri", "Risk sınıfı", "Kat" alanları | S14-M1, S14-M2, S14-M3 |
| İ16 | T3 | Plan revizyon protokolünde S1-M1 revizyon sınıfı satırı | S1-M1, W7 |
| İ17 | T3 | Kimseye verilmemiş iş taramasının yöntemi (S4) | S14-M7 |
| İ18 | T3 | Dilim boyutlandırma kuralı ve plan grafiği denetimi (takılma müdahalesi) | S17-M3 |
| İ19 | T3 | Her aşamanın vaatleri (söz–çıktı matrisinin plan tarafı) | S14-M8 |
| İ20 | T3 | Karar kaydında araştırma izi alanı; ritim tablosunda 5 kalemde bir öz-denetim ve kontrol noktası | S1-M4, S15-M5, S2-M2 |
| İ21 | T5 | Hook kurulumları Z1–Z6 (§3.3), yükleme doğrulaması ve regresyon sınaması | S14-M6, S17-M4, S2-M1, S14-M7, S1-M4, S15-M5 |
| İ22 | T5 | Maliyet ölçümü (alt ajan token kaynağı) ve bütçe eşikleri (Y8 tetiği) | S17-M5, S1-M2 |
| İ23 | T5 | Uyandırma mekanizmaları ve bildirim kanalı pilotu | S2-M5 |
| İ24 | T5 | Ders kaydı ve davranış değişiminin doğrulanması; H kayıtları ve defo modeli ders kaynağıdır | S2-M6, S15-M1, W10 |
| İ25 | T5 | CLAUDE.md'de mesaj sözleşmesinin 5 satırlık özeti; gate talimatının alt ajanlara sızmaması (U7) | S2-M1, S1-M5 |
| İ26 | T5 | Soğuk başlangıç testi (S18); yetki ve karar kaydı soruları eklenir | S1-M2, S1-M4, S14-M2 |
| İ27 | T5 | AGENT.md uyarlamasının (U1–U8) onaydan sonra kurulumu | S1-M5 |

### 3.2 T4'ün verdikleri

| Kime | Verilen |
|---|---|
| T1 | Dosya ihtiyaçları ve alanları (İ2); karar kaydı alanları (S1-M4); Batu sözünün ayrıştırma bölümü (S2-M7); günlük biçimi (S17-M1) |
| T2 | Çürütücü ve eksik-arayıcı işlevlerin gereksinimleri (S14-M4, S14-M5, S14-M7); iz alanları ve disiplin bloğu (S15-M2); defo modeli (S15-M1); doğrulama sözlüğü (S14-M2); risk sınıfı → doğrulama beklentisi (S14-M3) |
| T3 | Yetki zarfı ve geçiş türleri (S1-M2); karar katmanları ve revizyon sınıfları (S1-M1); soru yönlendirme (S1-M3); kapanış kapısı (S14-M7); ilerleme ölçüsü ve takılma türleri (S17-M2, S17-M3) |
| T5 | Zorlanabilir denetimlerin spesifikasyonu (§3.3); alarm eşikleri ve sessiz alarm kuralı (S17-M3); ölçü bütünlüğü kuralları (S17-M5); AGENT.md uyarlama metni (S1-M5); dikkat bütçesi ve bildirim kuralları (S2-M5) |

### 3.3 Hook adayları (T5'e istek; hepsi A-04 onayına bağlı)

Genel koşullar: Repo `.claude/settings.json` hook'ları yalnız tek repolu oturumda okunur (C!; R07 §2.5). Ayar dosyasındaki hook'lar alt ajan içinde de çalışır ve girdide `agent_type` alanı bulunur; role özgü kural buna bakarak uygulanabilir (R07 §2.5; C?). Kurulmazsa her denetim yapısal düzeyde kalır.

| No | Olay ve eşleyici | Ne denetler | Başarısızlıkta | Olay dayanağı (bilinen kayma noktası) |
|---|---|---|---|---|
| Z1 | PreToolUse, `SubagentHandback` (`tool_input.message`); yedek SubagentStop (`last_assistant_message`) | Dönüşte zorunlu başlıklar (S15-M2 c) | Çıkış kodu 2; eksik başlıkların listesi | kesik araç çıktısının "tam" sayılması (R11 K51); "returned a promise instead of a report" (R05 satır 2) |
| Z2 | SessionStart (`startup`, `resume`, `compact`) | Günlükten açılış sinyali; STATE Yetki bloğu | Bağlama ekler; "Sıradaki yetkili iş" boşsa uyarı | 742 koşu ve bayat pano (EkA-2) |
| Z3 | Stop (`last_assistant_message`) | Son paragraf üç bitiş önekinden biriyle başlıyor mu | Bir kez engeller (`stop_hook_active` ile döngü koruması) | yazılı kısa iletişim kuralının davranışa dönmemesi (R02 E3); sahte menü (EkA-6) |
| Z4 | PreToolUse, `Edit|Write` → STATE.md | Bir aşamayı "TAMAM" yapan yazımda KAPANIS dosyası ve §6 hükmü var mı | Yazımı reddeder, nedenini söyler | "declared the example finished" (R11 K41); erken zafer (R07 §3) |
| Z5 | PreToolUse, `Edit|Write` → DECISIONS.md | Yeni K satırının kaynak sütununda `sources/conversation/U` yolu var mı; yazan ana oturum mu (`agent_type`) | Yazımı reddeder | düzeltmelerin parafrazda yaşaması (R11 K49); K-009 formülasyonu (T-ORTAK) |
| Z6 | SessionStart (`compact`) ya da PostCompact | Sıkıştırma sonrası hatırlatma: AGENT.md ve protokolleri yeniden oku; çapa tek cümle; öz-denetim | Bağlama ekler | "Claude may start 'forgetting' earlier instructions" (R11 K18) |

Z3'ün değeri bilinmiyor: her turda çalışır ve arada bir düzeltme turu doğurur; pilotta gürültüsü ölçülür. Z1 için teslim biçimi sürüme bağlıdır (EkA-10, EkA-17).

### 3.4 Birleştirmede çözülmesi gereken çelişki adayları
1. **Soru kuyruğunun yeri:** DECISIONS'ın "Açık sorular" tablosu (önerim; tek kaynak) mı, ayrı dosya mı (T1).
2. **Otomatik seçimlerin yeri:** TK kaydında "katman: T" (önerim) mi, ayrı dosya mı (T1).
3. **Günlük:** T1'in bellek türlerindeki "oturum günlüğü" ile S17-M1 günlüğü tek dosya olmalı.
4. **H kaydı ile ders kaydı (T5 S21):** H kaydı girdi, ders kaydı ayrı; kopya değil bağlantı.
5. **Kimseye verilmemiş iş:** R11'de S4'te, T4.md'de S14'te. Çözüm önerisi: yöntem T3 (S4), kapanış kapısındaki yeri T4 (S14-M7).
6. **Ritimler:** 5 kalemde bir öz-denetim ve kontrol noktası T3'ün ritim tablosuna girmeli.
7. **Kök yapılandırma ile K-009 formülasyonu:** kök `.claude/` ve CLAUDE.md, ana oturumun "dal yalnız EXP-007 klasörüne dokunur" formülasyonuyla çelişir; bu Batu'nun sözü değildir (T-ORTAK). Batu'ya konumlama sorusuyla birlikte gider (§5.2).

---

## 4. Çarpışma testlerine katkı (W1–W10)

Her adımda: mekanizma — okunan/yazılan dosya — kim.

**W1 Soğuk başlangıç**
1. Açılış protokolü (T5 S18): CLAUDE.md (kurulduysa) → AGENT.md tam okunur (S1-M5 geçici kural) — ana oturum.
2. S17-M4 açılış sinyali: Z2 varsa bağlamda; yoksa GUNLUK.md'nin son 30 satırı okunur, STATE "Durum göstergesi" ile karşılaştırılır; bayatsa güncellenir.
3. S1-M2: STATE "Yetki" bloğu → sıradaki yetkili iş ve dayanağı (DECISIONS K-xxx) doğrulanır; çözülemezse durulur ve tek satırlık "Şunu bekliyorum" yazılır.
4. S2-M3: DECISIONS "Açık sorular"da açık çerçeve sorusu var mı?
5. İlk eylem: kırmızı alarm varsa alarm mesajı (S2-M1). Yoksa günlükte DONUS'u olmayan DAGITIM var mı (yarım iş; W5) bakılır; varsa önce o. Yoksa sıradaki yetkili iş.
6. Batu'nun mesajı varsa ilk cevap: routing bloğu, yönelim özeti (R08 §7), üç bitişten biri. Günlüğe OTURUM-ACILIS.

**W2 Bir iş kalemi döngüsü**
1. Soru doğar → S1-M3 beş yol. Batu'ya gidecekse S2-M3 kuyruğu (DECISIONS); değilse kalem açılır (T3).
2. S14-M1 bitti tanımı ve kabul testleri; S14-M3 risk sınıfı; S1-M1 beslediği kararın katmanı — kalem kaydı.
3. Rol seçimi (T2), bağlam paketi (T1), görev tanımı (T2 şablonu + S15-M2 b alanları). Günlüğe DAGITIM ve HEAD (S17-M1).
4. Alt ajan: rol dosyasındaki disiplin bloğu (S15-M2 a) ve defo iz alanlarıyla çalışır.
5. Dönüş: S14-M6 dönüş kapısı (Z1 varsa mekanik) ve kaynaktan kontrol → kat Y→K; günlüğe DONUS ve KAPI.
6. R2/R3 ise S14-M4 çürütücü → bulgu akıbeti → kat Ç (reviews/…-BULGULAR.md).
7. Karar kaydı (S1-M4); T katmanıysa otomatik seçim (S1-M3); günlüğe KARAR (İ).
8. Bellek ve plan güncellemesi (T1, T3); S15-M5 sayacı; S17-M3 eşik denetimi.
9. Mesaj gerekiyorsa S2-M1; bildirim tablosunda "Hiç" ise mesaj yok.

**W3 Aşama sonu**
1. S14-M7 kapanış kapısı (KAPANIS.md): kalem denetimi; kimseye verilmemiş iş (T3); R3 çıktıda bütünsel inceleme; S14-M8 ve S14-M9 özetleri; sahte kapanış soruları.
2. S15-M5 aşama sonu iz denetimi (çürütücü işlev).
3. S17: aşama ölçüleri (İ olayları, kabul, maliyet, alarm geçmişi); S2-M6 eşli ölçüler.
4. S2-M2 aşama raporu; durak aşamasındaysa S2-M4 kabul paketi @ SHA.
5. S1-M2 geçiş türü: durak → beklenir, yalnız aşama içi açık kalemler kapatılır; kendiliğinden → rapor gider, sonraki aşama açılır (K-002), günlüğe KONTROL-NOKTASI. Batu itiraz ederse W8.
6. Retrospektif (T5 S21); gerekirse defo modeline satır (S15-M1 doğuş kuralı).

**W4 Bağlam sıkıştırma anı**
- Öncesi: Bu kümenin durumları zaten dosyadadır: kararlar (DECISIONS, TK), sorular (Açık sorular), tercihler (TK katman T), alarmlar ve çalışan dağıtımlar (GUNLUK). Hiçbiri yalnız bağlamda tutulmaz. (PreCompact adımları T1 ve T5'in.)
- Sonrası: S1-M5 → AGENT.md ve LOAD edilmiş protokoller yeniden tam okunur; S1-M2 → Yetki bloğu yeniden okunur; S15-M5 → sıkıştırma sonrası öz-denetim (çapa tek cümle); S17-M1 → SIKISTIRMA satırı; S17-M4 → gösterge yeniden hesaplanır (Z6 ve Z2 varsa hatırlatma olarak gelir).
- Korunan: yetki, açık sorular, açık bulgular, alarm durumu, çalışan dağıtımlar. Kabul edilen kayıp: ara akıl yürütme ve araç çıktıları.

**W5 Oturum ya da makine kaybı**
1. Yeni oturum W1 adımlarını izler.
2. S17-M1 ve S17-M3: GUNLUK'ta DONUS'u olmayan DAGITIM'lar "işçi kayıp" türüdür; `git status` ve `drafts/` denetlenir (kısmi dosya var mı; T5).
3. S1-M1: aynı görev tanımıyla yeniden başlatma M katmanıdır, Batu'ya sorulmaz. Günlüğe KAYIP ve aynı sürümle yeni DAGITIM.
4. İkinci kayıpta sarı alarm; üçüncüde devre kesici (S17-M3) ve neden analizi (S15-M4: VM neden alındı, örneğin boşta kalma).
5. Batu'ya yalnız kırmızıda hemen; değilse sonraki kontrol noktasında bir satır.

**W6 Karar değişikliğinin yayılması (K-010/R10 vakası)**
1. Batu'nun mesajı birebir kaydedilir (T1, U-dosyası) → S2-M7 ayrıştırma: karar mı, kapsamı ne → DECISIONS K-xxx; Batu'nun sözü ile Claude'un uygulama yorumu ayrı.
2. S1-M1: Y katmanı; S1-M2: zarf etkileniyorsa sürüm artar, STATE bloğu aynı commit'te güncellenir.
3. S17-M1: açık dağıtımlar günlükten listelenir (bu turda R10 çalışıyordu).
4. Her çalışan alt ajan için ya bildirim (T2 mekanizması) ya da "dönüşü K-xxx'e göre uzlaştırılacak" işareti; bağlı yüzeyler güncellenir (T1 S9).
5. S14-M6: dönüş kapısının "taban değişti mi" kutusu R10 dönüşünü K-010'a göre uzlaştırır.
6. Günlüğe YAYILIM satırı. Kabul testi: her açık dağıtım için bir karşılık yazılı.

**W7 Plan revizyonu (varsayım çöker)**
1. Tetik T3'ün varsayım kaydından gelir → S15-M4 kısa neden analizi (neden çöktü; neden erken fark edilmedi).
2. S1-M1 revizyon sınıfı: yürütme ya da yöntem → ana oturum; başarı anlayışı ya da amaç → Batu (S2-M3 çerçeve sorusu, hemen); etkilenmeyen işler sürer.
3. S14-M2: çöken varsayıma dayanan Ç ve İ katları "bayat"; yeniden kontrol; kabul edilmiş bir çıktı etkileniyorsa Y10 → Batu.
4. S17-M2: revizyon kararı İ olayıdır, ama üç revizyon üst üste teslimatsız kalırsa "döngü" türü takılmadır (S17-M3).
5. S2-M2: sonraki raporda "değişen kararlar"; T3 değişiklik kaydı.

**W8 Batu'nun itirazı ya da yeni yönü**
1. U-dosyası ve S2-M7 ayrıştırma: itiraz / yeni yön / tercih / örnek.
2. S15-M3 itiraz protokolü: yeniden inceleme, pozisyon ve çürütme izi. Y katmanındaysa karar uygulanır; kanıt ve risk yazılır.
3. Belirsizse tek hedefli soru ve önerisi (decision-critical-assumptions: en yüksek bilgi değerli soru).
4. İtiraz sistemin yakalaması gereken bir hatayı gösteriyorsa S2-M6 H kaydı ve S15-M4.
5. Yeni yönse W6 adımları; S1-M2 zarf güncellenir.

**W9 Takılma: hareket var, ilerleme yok**
1. S17-M2 mesafesi → S17-M3 eşiği (sarı/kırmızı) ve türü (günlükten).
2. Sarı: S15-M5 öz-denetim; türe göre müdahale (dilim daraltma, plan grafiği denetimi, devre kesici); ALARM-SARI.
3. Kırmızı: S2-M1 alarm mesajı (öneriyle), S2-M5 hemen bildirim; cevap yoksa sessiz alarm kuralı.
4. Çözülünce ALARM-KAPANDI ve neden analizi (S15-M4) → ders (T5).

**W10 Bir dersin davranışa dönüşmesi ve doğrulanması**
1. Kaynak: H kaydı (S2-M6) ya da olay (S17) → S15-M4 neden analizi.
2. Ders kaydı ve dersin yeri (T5 S21); yer seçiminde iz ilkesi: mekanik kapı > iz isteyen prosedür > öğüt (S15-M1).
3. Gerekirse defo modeline olay adıyla satır ya da mevcut satırın iz kontrolüne ek.
4. Doğrulama (S14-M2 türleriyle): dersin fırsat sınıfı doğduğunda günlükte gözlem ya da hedefi söylemeyen sınama (soğuk başlangıç; sınama öğretebilir, R10 §4.8 madde 4). Somut örnek: "ara sürümler" dersi bu turda "dosyayı tek seferde yaz" kuralına dönüştü (ORTAK-SENTEZ, T-ORTAK). Mekanik doğrulama: P0.4 sonunda `git log --stat -- phases/P0-calisma-duzeni/drafts/` ile hiçbir T taslağının kısmi haliyle commit'lenmediği denetlenir. Bu denetim yapılana kadar ders "doğrulanmadı" sayılır.
5. S17: aynı türde yeni bir H kaydı dersin çalışmadığını gösterir.

---

## 5. Batu onayı gerektirenler

### 5.1 Onay ya da karar listesi

| No | Konu | İlişki | Önerim | Onay verilmezse |
|---|---|---|---|---|
| O1 | AGENT.md'nin Claude'a uyarlanması (U1–U8) | A-01; Mutation Rule | Tek paket olarak onayla | Kural harfiyen sürer: her otomatik turda gate ve blok; alt ajan yükümlülüğü yazısız kalır; bootstrap ChatGPT'ye göre yazılı kalır |
| O2 | K-002'nin yeni haritaya eşlenmesi ve zarfın eksik öğeleri (yükseltme tetikleri Y1–Y12, izinli canlı denemeler ve temizliği, bütçe eşikleri) | K-002; K-010 | S1-M2'deki eşleme ve liste | P1'den sonra her aşama sınırında Batu'ya dönülür (K-001 amacı zayıflar) |
| O3 | Hook'lar Z1–Z6 ve kök yapılandırma | A-04 | Z1, Z2, Z4, Z5 ilk pakette; Z3 ve Z6 pilottan sonra | Denetimler yapısal düzeyde kalır (tavsiye + şablon) |
| O4 | Çürütücü ve eksik-arayıcı işlevlerin kalıcı rol olarak kurulumu | A-04; K-007 | T2'nin önerisiyle | İşlev her seferinde görev tanımında yeniden anlatılır (K-007'nin eleştirdiği durum) |
| O5 | Bildirim kanalı ve dış etki (Routine bildirimi, e-posta) | Y3 | Pilotta oturum mesajı + bir Routine bildirimi denemesi, izinle | Yalnız oturum mesajı; sessiz alarm kuralı devrede |
| O6 | Dikkat bütçesinin başlangıç değerleri | Batu'nun tercihi | S2-M5'teki değerler | Değerler Claude'un tahmini olarak kalır ve Batu'nun tepkisiyle ayarlanır |
| O7 | Kabul biçimi (serbest cevap + SHA'ya bağlanma) | K-002 (P4 durağı) | S2-M4 | — (bilgi; itiraz yoksa böyle) |
| O8 | METHOD kabulü | K-005, P0.8 | Kabul paketiyle | P1 başlamaz |

### 5.2 Konumlama: (a) mı, (b) mi
- **(a) Tanımlar önce EXP-007 içinde taslak durur, onaydan sonra kurulur.** Artıları: A-04 ile uyumlu; K-009 formülasyonuyla uyumlu. Eksileri: onaya kadar zorlama yok, her şey tavsiye ve yapısal; taslak ile kurulan arasında kopya kayması riski (T5'in regresyon kontrolü gerekir).
- **(b) Doğrudan dalda `.claude/` altına kurulur.** Artıları: zorlama erken başlar; pilotlar gerçek yapılandırmayla yapılır. Eksileri: onaysız kurulum A-04'ü çiğner (yönetişim açısından kabul edilemez); ayar dosyası değişikliği çalışan oturuma da uygulanır (R07 §2.5, SET; cloud'da denenmedi).
- **Önerim (S1 açısından):** (a), ardından onaylı paketin dalda tek commit'le kurulması ve yükleme doğrulaması; yani (b), ama yalnız onaydan sonra. Kök dosyaların (CLAUDE.md, `.claude/`) ileride main'e birleşmesi main'deki ChatGPT hattını da etkiler; bu yüzden A-07 ile birlikte ayrıca sorulur. Not: A-02'deki pilotlar dosya yazmadan yapılırsa hook'lu mekanizmalar pilotta sınanamaz; bu mekanizmalar kurulumdan sonraki ilk aşamada canlı denemeye alınır.

### 5.3 Soru önerileri (DECISIONS'a girerken ID'yi birleştirme verir)
- **T4-Q1 (çerçeve):** Sürekli yetki (K-002) yeni haritada hangi geçişleri kapsasın? Önerim: K-002'deki "P4 kabul durağı" yeni haritadaki tasarım kabulü aşamasına, ondan önceki geçişler kendiliğinden geçişlere eşlensin; kurulum ve dış etki yetkisi durak olarak kalsın.
- **T4-Q2:** AGENT.md uyarlama paketi (U1–U8) tek paket olarak onaylanıyor mu? Önerim: evet.
- **T4-Q3:** Bildirim için oturum mesajı dışında bir kanal denensin mi? Önerim: pilotta bir Routine bildirimi, izinle ve temizlikle.
- **T4-Q4:** Dikkat bütçesinin başlangıç değerleri (aşama başına ~1.500 kelime; kontrol noktası başına en fazla 3 soru) uygun mu? Önerim: evet; iki aşamada bir gözden geçirilsin.
- **T4-Q5:** Hangi canlı denemeler sormadan yapılabilir? Önerim: R01 eksik-arayıcının dört denemesi (send_later ile uyandırma, boşta VM kaybı sonrası uyandırma, web arayüzünde `/goal`, yeni oturum açan tek atımlık tetik), sayı sınırı ve temizlikle.

---

## 6. Açık sorular, varsayımlar ve bu taslağın kanıtlamadıkları

### 6.1 Açık sorular
1. **Bildirim kanalı:** Cloud oturumu bittiğinde ya da karar gerektiğinde Batu'ya kendiliğinden bildirim gidiyor mu? Belgede push bildirimi Remote Control için var (EkA-11); cloud için bilinmiyor.
2. **Eşikler:** Sarı ve kırmızı alarm, kontrol noktası ve öz-denetim aralıklarının doğru değerleri bilinmiyor; başlangıç değerleri loopinance ve Magentic örneklerinden türetildi.
3. **Farklı model:** Farklı bir Claude modeliyle yapılan inceleme ne kadar bağımsızlık katar? Maliyet/fayda bilinmiyor.
4. **Hook'ların bu oturumda çalışması:** Bu oturum tek repolu mu, `.claude/settings.json` hook'ları okunur mu, SubagentHandback'e eşlenen PreToolUse hook'u rapor biçimini denetleyebilir mi? Kurulu CLI 2.1.283 ile ortam değişkenindeki 2.1.42 çelişiyor (EkA-17).
5. **CLAUDE.md ve alt ajanlar:** Kök CLAUDE.md her özel alt ajana yükleneceği için gate talimatının sızmasını önlemenin yolu (`omitClaudeMd` ya da açık not) T5'te seçilmeli.
6. **Opus 5.5 ve doğrulama:** Anthropic'in Opus 5 için verdiği aşırı doğrulama uyarısı bu model için de geçerli mi (R07 §8 soru 6)?
7. **Bilişsel yük:** Batu'nun yükünün doğrudan ölçüsü yok (R11 §7.1 soru 4); vekillerle çalışılıyor.
8. **Pilotlar:** A-02'deki dosya yazmayan pilotlar hook'lu mekanizmaları sınayamaz.
9. **DEFO_MODELI'nin andığı "üç-birden çatal testi":** Tanımı bulunamadı; S1-M3'teki soru yönlendirmesiyle ilişkisi kurulamadı.
10. **PushNotification:** R01'in önerdiği araç bu alt ajanda yok; ana oturumda olup olmadığı bilinmiyor.

### 6.2 Varsayımlar
- A-01: AGENT.md kontrol katmanı olarak kalır (tasarım her iki cevaba da dayanıklı; S1-M5).
- T1 önerilen dosya yerlerini ve alanları kabul eder; etmezse yollar değişir, alanlar kalır.
- T2 çürütücü ve eksik-arayıcı işlevleri için kalıcı rol tanımlar; tanımlamazsa S14-M4 ve S14-M7 her seferinde görev tanımıyla anlatılır.
- Batu raporları sohbette okur (bu konuşmadaki davranış; ölçülmedi).
- Günlükten "kalem", "dalga" ve takvim süresi güvenle hesaplanabilir.

### 6.3 Bu taslağın kanıtlamadıkları
- Hiçbir mekanizma bu ortamda canlı sınanmadı; hook betikleri çalıştırılmadı. "Belgede var" ile "burada çalışıyor" ayrıdır.
- Eşikler ve bedeller tahmindir; ölçülmedi.
- Taslak aynı modelin tasarımıdır. Kendi söz–çıktı kontrolü (§2.6.4) bir öz-kontroldür, doğrulama değildir; P0.5 eleştirisine ve Batu'ya gider.
- Kardeş taslaklar okunmadı (paralel yazılıyor); §3'teki arayüzler öneridir.
- Defo modeli uygulayıcı pratiğidir; etkisi bağımsız olarak ölçülmedi.
- R07–R10'un okunmayan bölümlerinde bu taslağı değiştirecek bilgi olabilir (§0.2).
- Batu'nun yakaladığı hataların sayısı, fark etmediği hataları içermez; bu kümenin ölçüleri de bu seçim etkisini taşır.

---

## Ek A — Birincil kaynaktan yeniden kontrol edilenler

Erişim tarihi hepsi için 27.09.2026. İngilizce alıntılar özgün dilindedir.

| ID | İddia | Kaynak | Kısa alıntı | Etiket · tür · cloud |
|---|---|---|---|---|
| EkA-1 | On defo, iz ilkesi, doğuş reçetesi | `batuhanozgun/loopinance_v2@07cd81bb:docs/DEFO_MODELI.md` (mcp__github__get_file_contents) | "mekanik kapı > iz isteyen yazılı prosedür > salt öğüt. Salt öğüt en zayıf biçimdir" · "Yumuşak öz-yargı kendini geçirir" · "makul görünen çıktı üreten defolar (1-4) kendiliğinden asla yakalanmaz" | kaynak diyor · uygulayıcı pratiği · — (yerel) |
| EkA-2 | 742 koşu; ilerleme ve canlılık; alarm eşiği; tek belge; seremoni; arşiv notu | aynı depo `docs/arsiv/ilk-plan-2026-09-24.md` §2, §3, §7 | "Bekçi 742 kez koştu ama \"54 gündür kod yok\" demedi." · "7 gün ya da kod üretmeyen 3 oturum olursa ilk söylenen şey bu olur: \"Sıkıştık, daraltalım.\"" · "Senden okumanı isteyeceğim tek belge bu." · "Onaylar seremoniye döndü. Mühürler itirazsız geçti." · "Müşteri haklı olarak bunun kendi işi olmadığını söyledi." | kaynak diyor · repo olayı (asistanın retrospektifi) · — |
| EkA-3 | Açılışta ilerleme sinyali | aynı depo `CLAUDE.md` | "oturum açılışında son koddan bu yana geçen günü basar. Eski düzen iki ay kod üretmeden koşmuştu. Durma sinyali varsa, ilk söylenen şey o olur." | kaynak diyor · uygulayıcı pratiği · — |
| EkA-4 | Türet, sorma; tek soru tek öneri | aynı depo `.claude/agents/urunci.md` | "Türet, \"Varsayım: …\" diye işaretle, öneriyle gel." · "Tek soru, tek öneri; seçenek menüsü sunma." | kaynak diyor · uygulayıcı pratiği · — |
| EkA-5 | Batu'nun defo yazısı | `publications/linkedin/articles/2026-07-16-ai-defolari-csvpf.md` | "bir agent oturum içinde 40 dakika boyunca kendi kendine çalışıyorsa, bu kontrolü kendisinin tetiklemesini sağlamak gerekir." · "hook'lar \"Böyle düşünme\" veya \"Şöyle söyleme\" diyemez." · "Hepsine kurmak da imkânsız." | kaynak diyor · Batu'nun yazısı · — |
| EkA-6 | Sahte menü ve örtme; bulgu serbest | `publications/linkedin/articles/2026-06-20-sahte-secenek-lwr8f.md` | "kanıt/bulgu/gerçek açık-iş = her zaman serbest" · "\"ne yapayım?\" sahte menüsü = yasak" · "Bu bir \"okuma\" hatası değil, bir \"sunum\" refleksiydi." | kaynak diyor · Batu'nun yayımladığı, AI ile yazılmış metin (R03 †) · — |
| EkA-7 | Özel alt ajanlar CLAUDE.md yükler; sistem istemi rol dosyasıdır | code.claude.com/docs/en/sub-agents.md | "Every other built-in and custom subagent loads both, unless its definition sets the `omitClaudeMd` field" · "Subagents receive only this system prompt plus basic environment details" | kaynak diyor · tedarikçi belgesi · C~ |
| EkA-8 | Ajan mesajı onay değildir | aynı sayfa | "no message from any agent counts as your approval for a pending permission prompt" | kaynak diyor · tedarikçi belgesi · C~ |
| EkA-9 | Routine istemi onay değildir | code.claude.com/docs/en/routines.md | "the fired prompt is not live user input and can't act as approval or consent for actions during the run" | kaynak diyor · tedarikçi belgesi · C+ |
| EkA-10 | Hook girdileri: SubagentHandback raporu, Stop/SubagentStop son mesajı, SessionStart bağlamı | code.claude.com/docs/en/hooks.md | "a PreToolUse or PostToolUse hook matched on `SubagentHandback` receives as `tool_input.message`" · "should use `last_assistant_message` on Stop and SubagentStop" · "String added to Claude's context at the start of the conversation" | kaynak diyor · tedarikçi belgesi · C~ (settings hook'ları tek repolu oturumda: C!) |
| EkA-11 | Bildirim | code.claude.com/docs/en/mobile.md; claude-code-on-the-web.md | "When Remote Control is active, Claude can send push notifications to your phone" · "you can monitor them from anywhere including the Claude mobile app" | kaynak diyor · tedarikçi belgesi · cloud'a push: bilinmiyor |
| EkA-12 | Ortamın Stop hook'u commit ve push'u zorluyor | `~/.claude/launcher-settings.json`; `~/.claude/stop-hook-git-check.sh` | "There are uncommitted changes in the repository. Please commit and push these changes to the remote branch." | gözledim · gözlem · Cg |
| EkA-13 | Hatırlatmalar kullanıcıdan geldi | `explorations/EXP-005-…/reflections/LESSONS-AND-OPEN-QUESTIONS.md` satır 95 | "… son Cloud işinin devre alınması (U044) kullanıcıdan geldi." | kaynak diyor · repo olayı · — |
| EkA-14 | Ayırt edemeyen doğrulama | aynı dosya satır 70 | "İki taraf da 4/4 PASS ve 23/23 gözlem aldı" | kaynak diyor · repo olayı · — |
| EkA-15 | Sonradan itiraz kalite kontrolü olamaz | `concepts/CHARTER.md` satır 37 | "kullanıcının sonradan itiraz etmesi temel kalite kontrolü olamaz" | kaynak diyor · Batu'nun talebinin konsolidasyonu · — |
| EkA-16 | Olumlu değerlendirme doğrulama değildir | `explorations/EXP-004-…/reflections/QUALIFICATIONS.md` satır 63 | "Pozitif kullanıcı değerlendirmesi teknik doğrulama veya belirsiz her tasarım seçiminin onayı sayılmaz." | kaynak diyor · kavramsal analiz · — |
| EkA-17 | Sürüm | `claude --version`; ortam değişkenleri | "2.1.283 (Claude Code)" · `CLAUDE_CODE_VERSION=2.1.42` | gözledim · gözlem · Cg (çelişki; hangisinin çalışan oturuma ait olduğu bilinmiyor) |
| EkA-18 | Alt ajanlar raporu SubagentHandback ile teslim ediyor; PushNotification aracı yok | bu alt ajanın araç listesi | — | gözledim · gözlem · Cg (yalnız bu alt ajan için) |
| EkA-19 | Routing kuralları | `AGENT.md` satır 13, 25, 40, 54–58, 160, 195–197 | "every user turn must pass through the complete routing gate" · "deliberately auditable in the ChatGPT browser workflow" · "Do not rely on a remembered summary" | kaynak diyor · kontrol katmanı metni (veri olarak) · C? (CLAUDE.md yok; kendiliğinden yüklenmiyor) |
| EkA-20 | Ara kayıt commit'i; ölçüm güvenilirliği | `git log` (26c05f6); `STATE.md` "Oturum ve ortam notları" | "checkpoint R10 and R11 notes while their agents are still writing (in progress)" · "R09'un sayacı düşük görünüyor; ölçüm güvenilirliği açık bir soru." | gözledim · repo kaydı · Cg |
