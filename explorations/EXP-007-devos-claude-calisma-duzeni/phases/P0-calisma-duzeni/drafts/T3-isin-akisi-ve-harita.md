# T3 — İşin akışı ve harita: yaşam döngüsü, keşif, plan, araştırma kullanımı, P0–P6

**Tür:** Küme taslağı (alt ajan çıktısı), EXP-007 P0.4. **Tarih:** 27 Eylül 2026.
**Görev tanımı:** `briefs/ORTAK.md`, `briefs/ORTAK-SENTEZ.md`, `briefs/T-ORTAK.md`, `briefs/T3.md`.
**Alt sistemler:** S3 Metodoloji ve yaşam döngüsü · S4 İhtiyaç ve kapsam keşfi · S5 Plan ve iş yönetimi · S6 Araştırma birikiminden yararlanma. **Ek teslimat:** EXP-007'nin P0–P6 haritası (§2).
**Yazma:** Repoda yalnız bu dosya yazıldı, tek seferde oluşturuldu. Çıktı sınırı yüzünden metin önce oturumun geçici çalışma alanında (repo dışı) parçalar halinde hazırlandı, dosya tek bir birleştirmeyle yaratıldı, parçalar silindi. Harness, bir web sayfası taramasının büyük çıktısını kendi `tool-results` dizinine kaydetti; bunu ben yazmadım. Durum değiştiren git komutu ve araç kullanılmadı.
**Kullanım sınırı:** Bu bir tasarım taslağıdır. Hiçbir mekanizma bu ortamda canlı denenmedi. Rol adı uydurulmadı; ihtiyaçlar işlevle yazıldı ("T2'ye ihtiyaç"). Dosya yolları öneridir; dosya mimarisinin sahibi T1'dir.

## 0. Soru, kaynaklar, okuma kapsamı, kanıt dili

### 0.1 Soru
EXP-007 işi baştan sona hangi aşamalardan geçmeli (P0–P6)? Her aşamanın sorusu, teslimatı, kapısı, Batu'nun rolü ve K-002'ye göre geçiş türü ne? Aşama içinde iş nasıl doğar, nasıl keşfedilir, nasıl planlanır, nasıl revize edilir? Foundation ve studies ne zaman ve nasıl kullanılır? Bunlar standart seviyede, mekanizma kartlarıyla nasıl kurulur?

### 0.2 Kaynaklar ve okuma kapsamı
Yollar repo köküne göredir; EXP-007 yolları `explorations/EXP-007-devos-claude-calisma-duzeni/` altındadır. Bütün okumalar 27.09.2026'da yapıldı.

| Kaynak | Kapsam |
|---|---|
| `briefs/` ORTAK, ORTAK-SENTEZ, T-ORTAK, T3 | tam |
| `briefs/` T1, T2, T4, T5 (arayüzler için); ENTEGRASYON (izlenmeyen dosya; birleştirme beklentisini görmek için, veri olarak) | tam |
| EXP-007 README, STATE, DECISIONS, P0 README; `sources/conversation/` INDEX, U001–U006, A001–A003 | tam |
| R02, R03, R04, R05, R06 | tam |
| R11 | tam (§0–§7, Ek A) |
| R07 | kısmi: §0, §1, §2.1 (BY-4…BY-8), §2.6, §2.7, §2.8, §3–§9 |
| R08 | kısmi: §0–§1, §2.1–§2.3, §2.6–§2.7, §2.11–§2.15, §3, §4, §7–§9 |
| R09 | kısmi: §0, §4, §5, §7–§11 |
| R10 | kısmi: §0–§2, §4.2–§4.7, §7–§10 |
| R01 | kısmi: `continuation` ekseni özeti ve açık soruları; örnek repolar ekseni; eksik-arayıcı |
| EXP-006 (`git show origin/main:…`, `ed2bf6e`) | tam: WORK.md, DECISIONS.md, `sources/U001.md`, `sources/U002-cloud-plan-and-autonomy.md`, `work/P3-01-…`; kısmi: `work/P1-01-…` (§1–§2) |
| `AGENT.md` | kısmi (satır 140–160, R08–R09 rotaları; veri olarak incelendi, uygulanmadı) |
| `agent/protocols/candidate-research-library.md` | kısmi (Amaç, Temel İlke, Araştırma Sınıfları, §3–§8) |
| `research/soul-foundations/08_…/REUSE.md` | tam |
| `research/studies/CATALOG.md` | kısmi (baş ve iş/plan ile ilgili satırlar) |
| `research/studies/beads/FINDINGS.md` §2, §4; `recursive-prerequisite-discovery/ASSESSMENT.md` §5 | kısmi (birincil kaynak kontrolü) |
| EXP-004 `continuations/DQ01-…` §1–§2; EXP-005 `reflections/LESSONS-AND-OPEN-QUESTIONS.md` Sonuç | kısmi (birincil kaynak kontrolü) |
| `concepts/ORIGIN.md` U01 | tam |
| code.claude.com/docs/en/best-practices.md | kısmi: "Give Claude a way to verify", "Explore first, then plan, then code", "Let Claude interview you", "Manage your session", "Add an adversarial review step", "Avoid common failure patterns" |
| anthropic.com/engineering/effective-harnesses-for-long-running-agents | kısmi (anahtar paragraf taraması) |
| **Okunmadı** | EXP-006 P2-01, ACTORS, STATE, HANDOFF, B1–B9, S1 dosyaları; Foundation WORK ve INFORMATION sentezleri (doğrudan); WM, superpowers, spec-kit, openspec paketleri (doğrudan); R07 §2.2–§2.5; R09 §1–§3, §6; R10 §3, §4.1, §4.8–§6 |
| **Erişilemedi** | yok |

### 0.3 Kanıt dili
- **Etiketler:** (kd) kaynak diyor · (g) gözledim · (ç) çıkarım · (v) varsayım · (b) bilinmiyor.
- **Kanıt türleri:** Batu'nun sözü; repo olayı; tedarikçi belgesi (Anthropic); topluluk ya da ürün pratiği (kaynağı okunmuş, çalıştırılmamış); kavramsal analiz (Foundation, EXP-004; aynı asistan); alt ajan raporu (R01–R11; ikincil); gözlem. **Bağımsız ölçüm yok.**
- **Atıf biçimi:** R11 kanıt kodları `[R11 K46]`; R07 maddeleri `R07 BS-3`; R08 ortak uygulamaları `R08 O17`; R09 maddeleri `R09 YD-5`. Birincil kaynağı kendim kontrol ettiğim alıntılarda "(g, 27.09.2026)" yazar.
- **Claude Code iddiaları:** cloud geçerliliği ayrıca yazılır: C+ cloud için belgeli · C~ genel belge · C! cloud'da farklı · C? belirsiz · Cg bu oturumda gözlendi (R07'nin etiketleri).
- **Kart kimlikleri:** `MK-3.1` biçimindedir (Mekanizma Kartı, S3'ün 1. kartı). R11'in K-kodlarıyla ve Batu'nun K-001… kararlarıyla karışmasın diye.

## 1. Özet

1. **Harita (§2).** P0–P6 bağımsız olarak yeniden değerlendirildi. K-002'nin bağlandığı P1–P4 numaraları ve anlamları korundu; değişenler şunlar: P1 belge taramasını tekrarlamaz, canlı deneme ister; P2 rolleri iki kaynaktan türetir (DevOS'un SOUL üzerindeki işi ve ekibin kendi iş–bilgi döngüsü); P2 ile P3 ortak bir çıkış kapısından geçer; P3 kurulumsuz küçük bir sınama içerir; P4→P5 ve P6 sonu Batu durağıdır. K-002'nin bu haritaya uygulanması P0 çıkışında Batu'ya teyit ettirilir, uydurulmaz.
2. **Yaşam döngüsü (S3).** Üç katmanlı ritim (oturum, iş kalemi, aşama) ve olay tetikli ritimler. Törene üç rota: yoklama, sınırlı iş, tasarım. Rota dört soruyla seçilir; biri "bu çıktıya kaç karar dayanacak" sorusudur (R11 Y7'nin dengeleyicisi). Anthropic'in "keşfet → planla → uygula → commit" akışı tasarım işine uyarlandı. Aşama açılışı ayrı bir "başlatıcı oturum" işidir (R07 BS-1).
3. **Keşif (S4) plandan ayrı çalışır.** Aşama keşif turu, amaçtan ve kullanımdan geriye akıl yürütür. Eksik cevap uydurulmaz, açık soru kaydına eksik soru yazılır (`return_to` alanıyla). Her yeni işin kökeni ve akıbeti yazılır; Batu'nun bulduğu eksikler ayrıca sayılır. "Kimseye verilmemiş iş" taraması, brief'ten bağımsız bir kaynak alanıyla yapılır.
4. **Plan (S5).** `PLAN.md` haritayı, kabul edilmiş sürüm işaretini, varsayım kaydını ve ekleme-yalnız değişiklik kaydını taşır. Aşama iş listesi, silinmeyen kalem bloklarından oluşur. "Hazır" bir statü değildir, beş bağımlılık türünden hesaplanır. Aynı anda açık iş sınırı vardır. Revizyon önce neyin değiştiğini sınıflar: yürütme mi, yöntem mi, başarı anlayışı mı, Batu'nun amacı mı? Revizyon yetkisi 14 satırlık bir tabloyla bağlanır.
5. **Araştırma kullanımı (S6).** Dokuz başvuru tetiği; Foundation → studies rotası (REUSE soru-ilk tablosu → CATALOG → META → bulgu). Okuma kaydı yalnız karar taşıyan okumalarda tutulur. Her tasarım kararı bir araştırma izi taşır: katkı türü, neyi kanıtlamadığı ve gerekiyorsa "yalnız akıl yürütme" işareti. Ayrıca durma ölçütü, tazelik sınıfları ve alt ajan dönüşünde "şu alana bakılmalı" alanı var.
6. **Hafiflik de standarttır.** Yöntemin ağırlık bütçesi ve meta-iş payı ölçülür. Bütün eşikler (v) olarak işaretlidir ve P0 pilotlarında ayarlanır.
7. **En önemli belirsizlik:** Oturumlar arası uyandırma bu ortamda denenmedi (R01). Denenmezse ritimler ve kendiliğinden geçişler yalnız açık oturumda işler; oturum sınırında iş durur.

## 2. EXP-007'nin baştan sona haritası: P0–P6

### 2.1 Haritanın dayanağı: neden var, neden yeniden değerlendirildi

- **Harita yokluğu, EXP-006 kaymasının birinci nedeniydi.** Batu'nun sözü: "bir önce konuşma bir sonraki konuşmanın içeriğini belirledi" ve "önce bütün harita kabaca belli olmalı" (EXP-006 `sources/U002-cloud-plan-and-autonomy.md` U002-A; kd, Batu'nun sözü; g, 27.09.2026). R11 bunu E12 olarak ● işaretler: aşama haritası yoksa yön bir önceki turdan gelir [R11 K46, K110].
- **K-010:** EXP-006'nın P1–P6 planı bağlayıcı değildir, yalnız girdidir (DECISIONS K-010; kd). Batu'nun EXP-006 kaynaklarındaki birebir sözleri ise niyetinin kanıtı olarak okunur, EXP-007 kararı sayılmaz (ç).
- **K-002 bağı:** Sürekli yetki A002'deki metne verildi: "P1→P2↔P3→P4 geçişleri kendiliğinden olsun. P4'te tasarım kabulü için dur. Kapsam değişikliği, yeni erişim ve cevaplayamadığım tercih soruları sana gelsin. Sorular biriksin, iş durmasın." (A002; U003 madde 1; kd). Bu metin EXP-006'nın aşama adlarına bakarak yazıldı. Harita bu numaraları ve anlamları değiştirirse K-002'nin kapsamı belirsizleşir. R01 bu kapsamın uydurulmamasını açıkça uyarıyor: "Its scope must not be fabricated." (R01 eksik-arayıcı; kd, alt ajan raporu). **Karar:** P1–P4'ün numarası ve ana anlamı korunur. Değişen her ayrıntı §2.4'te listelenir ve P0 çıkışında Batu'ya teyit ettirilir (ç).
- **Genel yaşam döngüsüyle uyum:** Harita "keşfet (P1) → tasarla (P2, P3) → bütünleştir, doğrula ve kabul et (P4) → kur (P5) → canlı sına ve devret (P6)" dizisidir. Bu dizi Anthropic'in "Explore → Plan → Implement → Commit" önerisinin (code.claude.com/docs/en/best-practices, "Explore first, then plan, then code"; kd, T; g, 27.09.2026) ve dış yöntemlerdeki "niyet → tasarım → görev" katmanlarının [R08 O14] aşama ölçeğindeki karşılığıdır (ç).

### 2.2 EXP-006 planından ne alındı, ne değişti

| EXP-006 (v1.3) | EXP-007 kararı | Gerekçe ve kanıt |
|---|---|---|
| P0 yok; plan P1'den başlıyor | **P0 eklendi:** Claude'un çalışma düzeni (METHOD) | K-005 ve K-007: "nasıl çalışılacağı … net biçimde ortaya konmadan başlanmaz" (DECISIONS; kd) |
| P1: kaynak incelemesi tamam, "RUNTIME SINANMADI" | **P1 canlı denemeyle kapanır.** Belge taraması tekrarlanmaz; R01, R07 ve P1-01 girdidir | "belge okumak canlı test sayılmaz" (A001'in aktardığı EXP-006 plan kuralı; kd). R01: "No continuation mechanism has been tested live in this environment." [R11 K104] |
| P2: roller aile ve sorumluluklardan (S1, F1–F8) türetildi | **P2 rolleri iki kaynaktan türetir:** DevOS'un SOUL üzerindeki işi ve ekibin kendi iş–bilgi döngüsü (P3) | A003 §1 teşhisi, K-006 ile kabul edildi: "Roller yanlış kaynaktan türedi" [R11 K52] |
| P2↔P3 iki yönlü, ayrı kapanış | **P2 ve P3 ortak çıkış kapısından geçer** | İki yönlü bağ, bir aşamanın ötekini beklemeden "tamam" demesine izin veriyordu (ç). Çerçeve yeterliği sınaması S4'ün bileşenidir [R11 S4] |
| P3: tartışma bazı (P3-01), sınama yok | **P3 kurulumsuz küçük bir sınama içerir** (EXP-007 içinde, alt ajanlarla canlandırılan istek → yanıt → kullanım zinciri) | A003 §2: "17 tur kâğıt üstünde ilerlemek yerine erken, küçük denemelerle sınardım." [R11 K46: "17 slices … platform was never researched"] |
| P4: bütünleşik tasarım, kabul durağı | **Korundu.** Kabulden önce üç mercekli eleştiri ve DevOS için çarpışma yürüyüşleri eklendi | K-002 durağı; P0.5'teki eleştiri modelinin P4'e taşınması (ç) |
| P5: kurulum; geçiş türü tanımsız | **P4→P5 Batu durağıdır** (kurulum yetkisi, hedef konum) | A002'deki varsayım: "P5'teki kurulum yetkisi sende kalacak" (kd); K-002 kapsamı P4'te biter; A-04 yapılandırma onayı |
| P6: sınama ve devir | **Korundu.** Ölçütler önceden yazılır; DevOS'un ilk SOUL işini Claude seçmez | U002-A: "senin tek işin development os'ta aktörlerin çalışabileceği düzenin ne olduğunu ortaya koymak" (EXP-006 kaynağı; kd, Batu'nun sözü) |
| Geri dönüş: "P6 kusuru ilgili P aşamasına döndürür" | **Korundu,** hedefli ve en küçük kapsamlı dönüş kalemi olarak (MK-5.9) | EXP-006 WORK §3 (kd); R04 (a)5 yeniden açma kuralı |
| Kesişen kanal yok | **Eklendi:** EXP-007'nin kendi işleyişinin gözlemleri P3'e "öz-kanıt" etiketiyle girer | A003 §3.10: "Bu düzenin nasıl işlediğine dair gözlemler, P3 için kanıt olarak ayrı yazılır. Ama bu düzen DevOS'un düzeni sayılmaz." (kd) |

### 2.3 Aşama kartları

Her kart aynı alanları taşır; `PLAN.md` §1'deki şablon MK-3.1'dedir. Varsayım kimlikleri (V-Pn-k) §2.6'daki kayda ve MK-5.5'e bağlanır. "İşlev" satırları T2'nin rol kataloğuna eşlenecek ihtiyaçlardır; rol adı değildir.

#### P0 — Çalışma düzeni (METHOD) · **şu an: P0.4**
- **Ana soru:** Claude (ana oturum ve kalıcı rollü alt ajanlar) EXP-007'yi P0–P6 boyunca nasıl yürütecek? Bağlam, bellek, kalıcı roller, plan, kalite ve süreklilik standart seviyede ve "nasıl" düzeyinde nasıl kurulur?
- **Teslimat:**
  - METHOD v1, Batu'nun kabul ettiği sürüm olarak bir commit SHA'ya bağlı;
  - bu harita (`PLAN.md` §1);
  - Batu onay paketi: A-04 yapılandırmaları, P1 deneme izni, K-002 eşlemesinin teyidi, §2.4'teki sorular;
  - pilot sonuçları (A-02 kabul edilirse);
  - kurulmuş ve yüklendiği gözlenmiş yapılandırma;
  - soğuk başlangıç testi sonucu.
- **İç adımlar:** P0 README'deki P0.1–P0.8. Pilotlar P0.7'dedir (§2.5).
- **Giriş ölçütü:** K-007 (U004). Karşılandı.
- **Çıkış ölçütü** (hepsi kanıtla):
  1. Batu METHOD v1'i açık bir mesajla kabul etti ve "başla" dedi. Kabul bir SHA'ya bağlı (K-005).
  2. Pilotlar yapıldı ve revizyona işlendi, ya da Batu pilotsuz geçişi seçti (A-02).
  3. Onaylanan yapılandırmalar kuruldu ve yeni bir oturumda yüklendikleri gözlendi (T5).
  4. Soğuk başlangıç testi geçti: konuşmayı görmemiş taze bir oturum yalnız repoyla dört soruyu doğru cevapladı: ne yapılıyor, sıradaki iş ne, neden, neyi yapmamalı (A003 §6).
  5. P1'in aşama kartı ve ilk keşif turu girdileri hazır.
- **Batu'nun rolü:** Taslağa itiraz; A-01, A-02, A-04, A-07 kararları; METHOD kabulü; "başla".
- **Geçiş P0→P1: DURAK.** Dayanak: K-005 ("U003 'başla' değildir") ve K-002'nin durumu: "P1 başlayınca işler".
- **Varsayımlar:** V-P0-1: Batu'nun P0.6 sunumunu değerlendirecek dikkati var, sunum bir sayfalık özetle başlar (T4). V-P0-2: METHOD'un ağırlığı pilotta taşınabilir çıkar. V-P0-3: A-04 yapılandırmaları bu dalda kurulabilir (T-ORTAK a/b seçimi; T5).
- **Meta-iş sınırı:** P0'ın tamamı meta-iştir. P0.5–P0.7 arasında en fazla iki revizyon turu yapılır (A003 §3.7'deki üç tur sınırının P0'a uygulanması; ç). Üçüncü revizyon gerekirse açık bulgular listesiyle Batu'ya gidilir.
- **İşlev ihtiyaçları (T2):** sentez ve birleştirme; üç ayrı eleştiri merceği; soğuk başlangıç sınayıcısı.

#### P1 — Ortam gerçekliği, DevOS açısından ve canlı sınamalı
- **Ana soru:** Claude Code cloud, çok rollü ve uzun soluklu bir ekibin iki ihtiyacını hangi gerçek yollarla ve hangi sınırlarla karşılar? K1: bir rolün başka rolden istediği iş, sonuca ve kullanıma döner. K2: rutin akışı Batu elle tetiklemez. Hangi yürütme yolları bu hesapta ve bu ortamda gerçekten çalışıyor: ana oturum ve alt ajan, Workflow, ajan takımları, Projects, Routines, `send_later`, oturumlar arası mesaj?
- **Teslimat:**
  - Kabiliyet ve sınır haritası; her satırda kanıt türü (belge / gözlem / denenmedi) ve cloud etiketi;
  - deneme seti sonuçları, denenemeyenler dahil;
  - topoloji seçeneklerinin kısıt tablosu (seçim P4'tedir);
  - P2/P3'e devredilen açık sorular.
- **Girdiler:** R01, R07, EXP-006 P1-01 (karşılaştırma için). T5'in canlı doğrulama setiyle aynı denemeler tek sefer koşulur.
- **Giriş ölçütü:** P0 kapandı. Deneme izni P0.8 paketinde alındı ya da hangi denemenin izinsiz yapılamadığı yazıldı.
- **Çıkış ölçütü:**
  1. K1 ve K2 için yük taşıyan her kabiliyetin kanıt türü var.
  2. Asgari deneme seti koşuldu, ya da her deneme için "denenemedi + neden + tasarıma etkisi" yazıldı. Asgari set: oturum boşta kalınca `send_later` ile uyanma; tek seferlik tetik ve hangi dalı açtığı; `SendMessage` ile devam; yazma izni olan alt ajanın kendi dosyası dışına yazma davranışı; derinlik değişkeninin değiştirilebilirliği. Kaynak: R01 eksik-arayıcı, R07 §8.
  3. En az iki yürütme yolu için hüküm yazıldı: çalışır / çalışmaz / bilinmiyor.
  4. "Kimseye verilmemiş iş" taraması yapıldı (MK-4.5).
- **Batu'nun rolü:** Deneme izni (K-002: "yeni erişim"). Hesap bilgisi tek toplu soruyla istenir: Projects ve Routines açık mı, plan ve limitler ne? Kabul gerekmez.
- **Geçiş P1→P2: KENDİLİĞİNDEN** (K-002).
- **Varsayımlar:** V-P1-1: deneme izni verilir. V-P1-2: `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` ortam tarafından sabittir (b; R07 §8 soru 2). V-P1-3: `send_later` ve `create_trigger` bu hesapta kullanılabilir.
- **Geri dönüş:** P2–P4'te yük taşıyan yeni bir ortam sorusu çıkarsa P1'e hedefli bir dönüş kalemi açılır. P1'in bütünü yeniden açılmaz (MK-5.9).
- **İşlev ihtiyaçları (T2):** ortam deneyicisi (durum değiştiren araçları yalnız ana oturum çağırır; T2 S16); belge okuyucu; karşı-okuyucu.

#### P2 — DevOS rolleri: SOUL'u geliştirecek ekip
- **Ana soru:** DevOS hangi kalıcı rollerden oluşmalı ve her rolün sözleşmesi ne? Batu'nun aktör → aile → rol → motivasyon önerisi (EXP-006 U002-A: "ben motivasyonları birer agent gibi düşünüyorum. Bunu tartışabiliriz.") nasıl yorumlanır?
- **Teslimat:**
  - rol kataloğu ve sözleşmeler: amaç ve başarı yönü, girdi ve yeterlik, tetik, teslimat ve tüketici, yetki ve olumsuz sınır, araç sınırı;
  - **türetme izi:** her rolün hangi iş ihtiyacından doğduğu, iki kaynaktan: (a) DevOS'un SOUL üzerindeki işi (EXP-006'nın altı kök işi ve B1–B9 alanları, girdi olarak); (b) ekibin kendi iş–bilgi döngüsünün adımları (P3);
  - EXP-006 P2-01 (DR01–DR16) ile karşılaştırma: alınan, reddedilen, gerekçe.
  - **Ajan dosyası P2'de yazılmaz;** P5'te yazılır.
- **Giriş ölçütü:** P1 çıkışı. P3'ün döngü iskeleti P2 ile eşzamanlı açılır; ortak kapıya kadar ikisi birlikte ilerler.
- **Çıkış ölçütü (P3 ile ortak kapı, MK-3.5):**
  1. Her rol en az bir P3 döngü adımına ve en az bir SOUL iş alanına bağlı. Bağlanamayan rol düşer ya da gerekçesi yazılır.
  2. Döngünün her adımının bir sahibi var.
  3. Hiyerarşi önerisinin yorumu yazıldı; Batu'ya giden tercih sorusu kuyrukta ya da cevaplandı.
  4. Çerçeve yeterliği sınaması yapıldı (MK-4.6).
- **Batu'nun rolü:** Hiyerarşi yorumu bir tercih sorusudur ve biriktirilir. Çerçeve sorusu çıkarsa hemen gider (MK-4.3).
- **Geçiş P2↔P3: KENDİLİĞİNDEN,** iki yönlü (K-002).
- **Varsayımlar:** V-P2-1: EXP-006'nın SOUL hedef tanımı (D006) rol türetmek için yeterince somut; K-010'a göre yeniden teyit edilir. V-P2-2: roller yürütme yolundan bağımsız tanımlanabilir; "rol ≠ taşıyıcı" [R10 §1 madde 5].
- **İşlev ihtiyaçları (T2):** rol tasarımı taslakçısı; eski kararlarla karşılaştırıcı; karşı-okuyucu.

#### P3 — Çalışmak ne demek: DevOS'un iş–bilgi döngüsü
- **Ana soru:** DevOS'ta iş nasıl doğar, kabul edilir, planlanır, yürütülür, doğrulanır, kaydedilir ve devredilir? SOUL ürün dosyaları ile DevOS'un kendi kayıtları nasıl tutulur, seçilir, rol bağlamına girer ve kullanılır? Roller arası istek (K1) nasıl işe dönüşür? Rutin akış (K2) nasıl sürer?
- **Teslimat:**
  - döngü tasarımı;
  - DevOS kayıt mimarisi (ürün dosyası ≠ çalışma kaydı; EXP-006 D015, girdi olarak);
  - roller arası istek sözleşmesi;
  - **küçük sınama raporu:** EXP-007 içinde, kurulum yapmadan, alt ajanlarla canlandırılan bir istek → çalışma → yanıt → kullanım zinciri.
- **Girdiler:**
  - Foundation WORK ve INFORMATION: REUSE soru-ilk tablosunun Work, Information ve Selection satırları;
  - studies: work-management-project-control, recursive-prerequisite-discovery, beads, superpowers S03, context-memory-harness-engineering;
  - EXP-006 P3-01 (aday);
  - EXP-007'nin kendi işleyiş gözlemleri, "öz-kanıt" etiketiyle.
- **Çıkış ölçütü (P2 ile ortak kapı):**
  1. Döngünün her adımı için sahip rol, girdi ve çıktı kaydı ve tetik yazılı.
  2. En az bir uçtan uca yürüyüş yapıldı; bu bir tasarım senaryosudur, gerçek bir SOUL işi değildir.
  3. Küçük sınama yapıldı ya da neden yapılamadığı yazıldı.
  4. P1'den gelen kısıtlara uyum kontrol edildi.
  5. "Kimseye verilmemiş iş" taraması yapıldı.
- **Batu'nun rolü:**
  - Tercih soruları biriktirilir.
  - P3 çıkışında Batu'ya bir kontrol noktası raporu gider; iş durmaz.
  - Gerekçe: Batu EXP-006'da P3 için "burayı biraz derin konuşalım. hemen karar verme" demişti (EXP-006 P3-01 girişi; kd, Batu'nun sözü; K-010'a göre bağlayıcı değil). K-002 ise P3→P4'ü kendiliğinden yapıyor.
  - Batu'ya sorulur: "P3 çıkışında durak ister misin?" (§2.4).
- **Geçiş P3→P4: KENDİLİĞİNDEN** (K-002), yalnız ortak kapı geçince.
- **Varsayımlar:** V-P3-1: döngü, gerçek bir SOUL işi seçilmeden tasarım senaryolarıyla sınanabilir. V-P3-2: EXP-007'nin kendi düzeni DevOS için kanıt değeri taşır, ama "tasarlayan = denenen" olduğu için yalnız öz-kanıttır (A003 §6).
- **İşlev ihtiyaçları (T2):** döngü taslakçısı; Foundation okuyucusu; birlikte okuma işçisi; sınamayı canlandıran alt ajanlar; karşı-okuyucu.

#### P4 — Bütünleşik DevOS tasarımı ve kabul
- **Ana soru:** P1'in ortam gerçekliği, P2'nin rolleri ve P3'ün döngüsüyle DevOS'un uçtan uca düzeni ne olmalı? Hangi yürütme yolu seçilmeli (alt ajan, takım, Projects, Routines ya da gerekçeli bir birleşim) ve neden? K1 ve K2 uçtan uca nasıl sağlanıyor?
- **Teslimat:**
  - tek ve bütünsel DevOS tasarım belgesi;
  - seçim gerekçesi ve reddedilen seçenekler;
  - DevOS için çarpışma yürüyüşleri: W1–W10'un DevOS karşılıkları;
  - üç mercekli eleştiri: söz–çıktı izlenebilirliği, bütünsel etkileşim, ortamda uygulanabilirlik;
  - kabul paketi (biçimi T4'te).
- **Giriş ölçütü:** P2/P3 ortak kapısı geçildi. Seçilecek yolun yük taşıyan kabiliyetleri P1'de "gözlem" düzeyinde; değilse önce P1'e hedefli dönüş kalemi açılır.
- **Çıkış ölçütü:** Batu'nun açık kabulü, SHA'ya bağlı. Kabul edilmezse düzeltme kalemleri açılır.
- **Batu'nun rolü:** Kabul, ret ya da düzeltme. Kurulum yetkisi ve hedef konum kararı da bu durakta sorulur: DevOS hangi repoya ve dala kurulacak? EXP-006 D015'e göre fiziksel şema açıktı.
- **Geçiş: DURAK** (K-002: "P4'te tasarım kabulü için dur").
- **Durakta sürebilecek işler (v; Batu'ya sorulur):** Kabulü varsaymayan işler sürer: açık soruların araştırılması, hijyen, retro. Kurulum hazırlığı yalnız "aday" kalem olarak yazılır.
- **Varsayımlar:** V-P4-1: seçilen yürütme yolu Batu'nun hesabında mevcut. V-P4-2: Batu kabul paketini bir oturumda değerlendirebilir.
- **İşlev ihtiyaçları (T2):** bütünleştirici; üç eleştiri merceği; kabul paketi hazırlayıcısı.

#### P5 — Kurulum: dosyalar ve mekanizmalar
- **Ana soru:** Kabul edilen tasarım, Claude'un gerçekten yüklediği ve uyguladığı dosya ve mekanizmalarla nasıl kurulur?
- **Teslimat:**
  - rol ajan dosyaları, CLAUDE.md, skills, hook ve izin ayarları;
  - DevOS iş ve bilgi kayıtlarının iskeleti;
  - kurulum raporu: yükleme doğrulaması, rol etkinleşmesi, izin davranışı. Ölçüt "dosya var" değildir; yükleme ve tüketim gösterilir (EXP-006 WORK §3 P5 ölçütü; kd).
- **Giriş ölçütü:** P4 kabulü, Batu'nun kurulum yetkisi, hedef konum ve gerekli erişim.
- **Çıkış ölçütü:**
  1. Kurulan her bileşen için yükleme ya da etkinleşme gözlemi var.
  2. Basit sınama görevleriyle regresyon kontrolü yapıldı (T5).
  3. Açıklar listesi yazıldı.
- **Batu'nun rolü:** Kurulum yetkisi; erişim.
- **Geçiş P4→P5: DURAK.** Dayanak: K-002'nin kapsamı P4'te biter; A002'deki varsayım: "P5'teki kurulum yetkisi sende kalacak"; yapılandırma değişikliği A-04 türündendir.
- **Geçiş P5→P6: bilinmiyor.** Batu'nun P5 yetkisi P6'nın canlı sınamasını da kapsıyorsa kendiliğinden olur, kapsamıyorsa durak olur. P4 kabul paketinde sorulur.
- **Varsayımlar:** V-P5-1: hedef konumda `.claude/` ve CLAUDE.md cloud'a taşınır (R07 §7: repoya commit edilen yapılandırma C+). V-P5-2: hook'lar tek repolu oturumda çalışır; çok repolu kurulumda zorlama katmanı sessizce kapanır (R07 §4 madde 3).

#### P6 — Sınama ve devir
- **Ana soru:** Kurulan DevOS gerçek bir başlangıçta hedefi ve birikimi devralıp kendi işini keşfedebiliyor mu? K1 (istek → yanıt → kullanım) ve K2 (rutin elle tetiklenmeme) sağlanıyor mu? Müdahaleden sonra doğru devam ediyor mu?
- **Teslimat:**
  - önceden yazılmış sınama protokolü ve ölçütleri (ölçüt bütünlüğü: T4);
  - sonuçlar, başarısız ve açık durumlar dahil;
  - kusurlar için ilgili aşamaya dönüş kalemleri;
  - devir paketi;
  - EXP-007 kapanış raporu (METHOD gözlemleri P3 kanıtı olarak).
- **Kural:** DevOS'un ilk SOUL işini Claude seçmez; ekip kendisi keşfeder. Dayanak Batu'nun EXP-006'daki sözüdür; K-010 nedeniyle teyit sorusu olarak §2.4'e alındı.
- **Giriş ölçütü:** P5 çıkışı; sınama izni ve bütçesi.
- **Çıkış ölçütü:** Batu devir kabulünü verdi (SHA'ya bağlı).
- **Geçiş: DURAK.** Kabul Batu'dadır (K-002 ruhu; A003 §3.2). Sonrası Batu'nun kararıdır.
- **Varsayımlar:** V-P6-1: sınama gerçek bir SOUL başlangıcıyla yapılabilir; bunun erişim, repo ve maliyet koşulları henüz bilinmiyor (b).

### 2.4 Geçiş tablosu ve Batu'ya sorulacaklar

| Geçiş | Tür | Dayanak |
|---|---|---|
| P0 → P1 | **durak** | K-005; P0 README P0.8 |
| P1 → P2 | kendiliğinden | K-002 |
| P2 ↔ P3 | kendiliğinden, iki yönlü | K-002 |
| P3 → P4 | kendiliğinden, yalnız ortak kapıdan sonra | K-002; bu taslak (ç) |
| P4 kabulü | **durak** | K-002 |
| P4 → P5 | **durak** | K-002 kapsamı dışında; A002 varsayımı; A-04 |
| P5 → P6 | **bilinmiyor**, Batu'ya sorulur | — |
| P6 devir kabulü | **durak** | kabul Batu'da |
| Hedefli geri dönüş (P2/P3/P4 → P1; P6 → Pn) | kendiliğinden; aşama raporunda bildirilir | A003 §3.7: "planda öngörülen geri dönüşlere … ben" |
| Harita değişikliği: aşama ekleme, çıkarma, sıra değişikliği | **Batu** | A003 §3.7: "haritaya … sen" |

**Aşama içinde her zaman Batu'ya gidenler (K-002):** kapsam değişikliği, yeni erişim, Claude'un cevaplayamadığı tercih soruları. Çerçeve soruları biriktirilmez (MK-4.3).

**P0.8 onay paketine girecek sorular** (T4'ün kabul paketine eklenir):
1. Harita değişiklikleri (§2.2) kabul mü?
2. K-002, bu haritanın aynı numaralı P1–P4'üne aynen uygulanır mı?
3. P3 çıkışında durak ister misin, yoksa kontrol noktası raporu yeter mi?
4. P5 → P6 geçişi kendiliğinden mi olsun, durak mı?
5. Duraklarda hangi işler sürebilir (§P4'teki öneri)?
6. P1 deneme izni: hangi araçlar, hangi bütçe? Loopinance repoları için salt okuma `add_repo` gerekli mi?
7. "DevOS'un ilk SOUL işini Claude seçmez" kuralı EXP-007'de de geçerli mi?
8. A-02: P0 pilotları yapılsın mı (§2.5)?

### 2.5 P0 pilotlarının yeri (A-02)

- **Yer:** P0.7, Batu'nun taslak itirazlarından sonra ve P0.8'den önce.
- **Yöntem:** Batu'nun kendi "concepts" sırası uygulanır: "taslak plan sonrasında, konuşma ortamında bir dosya yaratmadan sadece bir studies çalışmasında planı uygulayacaksın. planı revize edip etmeyeceğimizi düşüneceksin. ikinci bir studies çalışması için tekrar deneyeceksin. planı tekrar revize edip etmeyeceğini düşüneceksin." (`concepts/ORIGIN.md` U01, adım 6–10; kd, Batu'nun sözü; g, 27.09.2026).
- **Pilot-1 (A003 §5 önerisi):** Gerçek bir P1 sorusu: "Bu ortamda roller birbirine nasıl ulaşır?" Yalnız belge ve salt-okuma gözlemiyle yapılır; durum değiştiren araç kullanılmaz.
  - **Sınanan kartlar:** MK-4.1 keşif turu, MK-3.6 rota seçimi, MK-3.3 iş kalemi döngüsü, T2'nin brief ve dönüş şeması, MK-6.3 okuma kaydı, MK-6.4 araştırma izi, MK-3.5 kalem kapısı.
- **Pilot-2:** Bir Foundation "soruyu genişletme" adımı: "DevOS'ta iş nasıl doğar?" sorusu REUSE'un Work ve Information satırlarıyla genişletilir, sonra ilgili studies okunur.
  - **Sınanan kartlar:** MK-6.1 tetik, MK-6.2 rota, MK-4.2 bakış açısı taraması, MK-4.5 "kimseye verilmemiş iş" taraması, MK-6.5 birlikte okuma, MK-6.8 durma ölçütü.
- **Önceden yazılan başarı ölçütleri:**
  1. Her pilot sonunda bir mekanizma kullanım tablosu çıkar: kullanıldı mı, kararı değiştirdi mi, bedeli ne (R06 G06).
  2. En az bir "ağır geldi" ya da "işe yaramadı" bulgusu çıkar, ya da "bulgu yok" gerekçesiyle yazılır.
  3. Batu'nun pilot sırasındaki hatırlatma ve düzeltmeleri türleriyle kaydedilir (T4).
  4. Meta-iş payı ölçülür (MK-3.8).
- **Pilotların çıktısı:** Sonuçlar çöpe gitmez; P1 ve P3'ün girdisi olur (A003 §5).
- **A-02 reddedilirse:** P1'in ilk iki kalemi "üretimde pilot" sayılır. Bu kalemlere ek karşı-okuma yapılır ve ikinci kalemden sonra bir METHOD revizyon kontrol noktası konur. Bu nokta durak değildir; sonucu aşama raporunda görünür.

### 2.6 Haritanın varsayım kaydı ve kesişen kanallar

**Harita düzeyindeki varsayımlar** (`PLAN.md` §3'e taşınır, MK-5.5 biçiminde):

| ID | Varsayım | Sınıf (MK-5.5) | Çökerse ne olur | Nasıl sınanır |
|---|---|---|---|---|
| V-H-1 | Uzun işi taşıyan uyandırma yolları bu hesapta çalışır | tahmin | Kendiliğinden geçişler oturum sınırında durur; Batu oturum açan olur | P1 deneme seti (T5) |
| V-H-2 | Batu'nun duraklardaki dikkati yeterli (P0, P4, P5, P6) | tahmin | Kabul törene döner [R11 K29] | T4 dikkat bütçesi; kabul paketinde okuma süresi |
| V-H-3 | EXP-006 girdileri (SOUL hedefi, P2-01, P3-01) yeniden kullanılabilir | bakılacak | P2/P3 kapsamı büyür | P2 ve P3 keşif turları |
| V-H-4 | DevOS tasarımı EXP-007 dalında, main'e birleşmeden yürüyebilir (K-009) | verilen olgu | Birleşme zamanı (A-07) P5'i etkileyebilir | P4 durağında sorulur |
| V-H-5 | Haftalık kullanım limiti aşama bütçelerini taşır | tahmin | Aşama ortasında iş durur | T5 bütçe ve limit kaydı |

**Kesişen kanallar:**
- **METHOD → P3 kanıtı.** EXP-007'nin kendi iş kalemi, kapı ve revizyon kayıtları P3'e "öz-kanıt" etiketiyle girer. DevOS'a "işe yaradı" diye kanıtsız taşınmaz (A003 §6 "12–24 ay").
- **Geri dönüşler.** Her geri dönüş, en küçük kapsamlı ve adı konmuş gerekçeli bir kalemdir (MK-5.9). Tüm aşamayı yeniden açmaz.
- **Bütçe şekli (T5'e girdi).**
  - P1: deneme ağırlıklıdır; az ama pahalı denemeler.
  - P2 ve P3: okuma ve taslak ağırlıklıdır; paralel okuma yoğundur.
  - P4: eleştiri ve birleştirme ağırlıklıdır.
  - P5 ve P6: kurulum ve canlı sınama.
  - Sayısal bütçeyi T5 koyar. T3 her aşama açılışında tahmini kalem sayısını, rota karışımını (yoklama, sınırlı, tasarım) ve paralellik ihtiyacını verir (MK-3.2).

## 3. S3 — Metodoloji ve yaşam döngüsü

### 3.1 Amaç
İşin hangi aşamalardan, hangi iş kalemi döngüsüyle, hangi ritimle ve hangi kapılardan geçtiğini tanımlamak. Tören düzeyini risk, belirsizlik, geri dönülebilirlik ve aşağı akış yüküyle orantılı tutmak. Yöntemin kendisinin ürünün yerine geçmesini ölçerek önlemek. Hız (K-002'nin kendiliğinden geçişleri) varsa fren de aynı yerde tanımlanır: kapılar, periyodik yön gözden geçirmesi ve T4'ün ilerleme ölçüsü [R11 §1 madde 4].

### 3.2 Standart seviyedeki bileşenler ve karar tablosu
Temel R11 §3 S3'tür. R07 (BP, E-HAR, BS-1…BS-3), R08 (O14–O17) ve R09 (YD-1…YD-9) ile genişletildi. "Kabul testi", bileşenin kurulduğunu değil işlediğini gösteren sınamadır.

| Bileşen | Karar | Önlediği hata | Kabul testi | Kart | Kaynak |
|---|---|---|---|---|---|
| Aşama haritası (soru, teslimat, giriş/çıkış ölçütü, Batu'nun rolü, geçiş türü, varsayımlar) | gerekli | Yönü bir önceki tur belirler (EXP-006 E1) | Soğuk başlangıç testinde taze oturum "hangi aşamadayız, çıkış ölçütü ne, sıradaki geçiş durak mı" sorularını `PLAN.md`'den doğru cevaplar | MK-3.1 | [R11 K46, K110]; U002-A |
| Aşama açılış oturumu (başlatıcı) | gerekli | Her oturum işi yeniden tanımlar; aşama keşfi atlanır | Her aşamanın ilk commit'inde aşama README'si, keşif turu kaydı ve açık statülü kalem listesi var | MK-3.2 | R07 BS-1 (E-HAR) |
| İş kalemi döngüsü, tasarım işine uyarlanmış "keşfet → planla → uygula → doğrula → kaydet" | gerekli | Kalem kalem değişen kalite; yanlış problemi çözmek | Kapanan kalemlerin her birinde bitti tanımı işten önce yazılmış (commit sırası) ve kapanış satırları dolu | MK-3.3 | BP "Explore first…"; R07 BD-1; A003 §3.1 |
| Rota ölçekleme: yoklama, sınırlı iş, tasarım | gerekli | Ya her işe ağır tören ya büyük işe hafif yol | Her kalem bloğunda rota ve gerekçe var; örneklem incelemesinde rota ile risk soruları tutarlı | MK-3.6 | R09 YD-5; R08 O15; BP "If you could describe the diff in one sentence, skip the plan" |
| Ritimler: oturum, kalem, aşama, periyodik yön gözden geçirmesi, olay tetikli | gerekli | Kontrol noktaları "hatırlanınca" yapılır; kayıt ve yön kontrolü unutulur | Ritim takvimindeki her olay için kayıtta iz var (kalem kapanış satırları, yön gözden geçirme notları) | MK-3.4 | [R11 K34, K79]; R09 YD-1…YD-9 |
| Kapılar ve durma koşulları; tamamlanma katları | gerekli | Ya durmadan akış (kayma) ya her aşamada durma | Her aşama geçişinde doldurulmuş bir kapı kaydı var; "geç" kararlarının hepsinde her ölçüt için kanıt işaretçisi var | MK-3.5 | K-002; [R11 K15, K88, K69] |
| Tören orantısı, aşağı akış yükü dahil | gerekli | "Düşük risk" sınıfı eleştirisiz kararları yayar (Y7) | Rota seçimi dört risk sorusuyla yapılmış; aşağı akışı ≥2 karar olan kalemlerin hiçbiri yoklama rotasında değil | MK-3.6 | [R11 K10, K76, K28]; R11 §5 Y7 |
| Pilot, sonra ölçekle (ilk örnek kuralı) | gerekli | Aynı brief ya da prosedür hatası N kez ödenir; yöntem kâğıtta kalır | Yeni bir brief şablonu, rol ya da prosedür ilk kez tek kalemde kullanılır ve gözden geçirme notu olmadan çoğaltılmaz | MK-3.7 | R07 BO-6; A003 §5; `concepts/ORIGIN.md` U01 |
| Yöntemin ağırlık bütçesi ve meta-iş sınırı | gerekli | "Süreç kendisi ürün oldu" [R11 K27]; önceki düzenler kendi ağırlığı altında durdu [K28] | Aşama raporunda meta-iş payı ve "son ürün katkısından bu yana geçen süre" var; eşik aşımı raporun ilk satırında | MK-3.8 | [R11 K27, K28, K46]; R08 O25 |
| Olay tetikli ritimler (model ya da sürüm değişikliği) | gerekli; **sahibi T5** | Eski varsayım sessizce bozulur | T5'in kartında | — | R09 YD-8 |
| Bakım ritmi (budama, rol gözden geçirmesi) | gerekli; **sahibi T1/T5** | Birikim ve bağlam gürültüsü | T1/T5'in kartında; aşama kapısında adım olarak yer alır (MK-3.5) | — | R09 YD-9 |
| Oturum başına tek iş birimi (E-HAR'ın "incremental") | **uyarlanarak gerekli:** bir alt ajan çağrısı tek kaleme hizmet eder; ana oturum WIP sınırıyla birden çok kalemi sürdürebilir | Uzun oturumda bağlam çürür; VM kaybında çok iş gider | Her brief'te tek kalem kimliği var; WIP sınırı aşılmamış (MK-5.3) | MK-3.3, MK-5.3 | R07 BS-3; R08 O16 |
| Harness bileşenlerinin model değişiminde yeniden sorgulanması | gerekli; **sahibi T5** | Model güçlendikçe iskele işi engeller | T5 | — | R07 §1 ilke 2 (E-HD, E-MA) |

**Gereksiz sayılan bileşen yok.** Kaynaklarda geçen iki öğe bu bağlamda ayrı mekanizma olarak kurulmadı:
- **Tek sabit zincir** (ör. her kalemde plan → TDD → inceleme → commit). Rota ölçeklemesiyle çelişir. R05 §3 madde 5: "One heavy lifecycle for every step … fails".
- **Takvim zamanlayıcısıyla ritim.** Uyandırma denenmedi. Ritimler şimdilik olaya bağlıdır; zamanlayıcı ihtiyacı P1 denemelerinden sonra T5'te karara bağlanır (b).

### 3.3 Mekanizma kartları

#### MK-3.1 Aşama haritası ve aşama kartı

| Alan | İçerik |
|---|---|
| Ne | P0–P6'nın her biri için sabit alanlı bir aşama kartı ve tek sayfalık geçiş tablosu; yönün tek kaynağı. |
| Nerede | `PLAN.md` §1 (EXP-007 kökü; T1 yapısına uydurulur). Şablon aşağıda. `STATE.md` yalnız "şu anki aşama: Pn; kart: PLAN.md §1 Pn" işaretçisini taşır, kartı kopyalamaz. |
| Ne zaman | P0.4'te ilk kez yazılır; aşama açılışında (MK-3.2) ve kapısında (MK-3.5) güncellenir; harita revizyonunda (MK-5.6) değişir. |
| Kim | Yazıcı: ana oturum (tek yazıcı; T2). Harita değişikliğinin yetkisi Batu'dadır (MK-5.7). |
| Nasıl işler | 1) Her kart bu taslağın §2.3'teki alanlarını taşır. 2) "Durum" alanı yalnız kapı kaydıyla (MK-3.5) değişir. 3) Oturum açılışında okunan ilk plan yüzeyi burasıdır; açılış sinyali durum alanını ve son kapı tarihini gösterir (T5). 4) Kartın değişen her alanı değişiklik kaydına (MK-5.6) bir satır ekler. |
| Zorlama düzeyi | Yapısal: şablon ve zorunlu alanlar. Zorlayıcı değil; hook önerilmedi (ağırlık bütçesi). |
| Çalıştığını nasıl anlarız | Soğuk başlangıç testi (A003 §6) harita sorularını doğru cevaplar. **Bozulma işareti:** bir oturumun ilk eylemi karttaki "sıradaki geçiş"le çelişir; ya da bir kalem, hiçbir aşama kartının çıkış ölçütüne bağlanamaz. |
| Bağımlılıklar | İhtiyaç: T1 (dosya yeri, statü sözlüğü), T4 (kapı ve yetki). Beslediği: MK-3.2, MK-3.5, MK-5.1, T5 açılış protokolü. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: yönün bir önceki turdan gelmesi. Kabul testi: yukarıdaki soğuk başlangıç soruları. |
| Kaynak | [R11 K46, K110]; R11 E12; EXP-006 U002-A (Batu'nun sözü); A003 §3.6. |
| Bedel | Bir kez yazım, yaklaşık 3–4 KB. Aşama başına birkaç satır bakım. Batu'nun okuma yükü: yalnız harita değişince. |

```text
### Pn — <ad>
- Durum: BEKLİYOR | AÇIK (açılış: <tarih>, <SHA>) | KAPIDA | KAPANDI (<tarih>, <SHA>, kapı kaydı: <yol#>)
- Ana soru: <tek cümle>
- Teslimat: <liste; her biri bir dosya yolu ya da "karar kaydı">
- Giriş ölçütü: <liste>          - Çıkış ölçütü: <numaralı liste; her biri kanıtla sınanabilir>
- Batu'nun rolü: <yetki / kabul / tercih soruları>
- Geçiş: kendiliğinden (K-002) | DURAK (<dayanak>) | bilinmiyor (<soru ID>)
- Varsayımlar: V-Pn-1, V-Pn-2 (→ PLAN.md §3)
- Geri dönüş kuralı: <hangi durumda hangi aşamaya hedefli kalem açılır>
- Bütçe: <T5'in koyduğu tavan>   - İşlev ihtiyaçları: <T2 eşlemesi>
```

#### MK-3.2 Aşama açılış oturumu (başlatıcı)

| Alan | İçerik |
|---|---|
| Ne | Her aşamanın ilk oturumunda, iş yapmadan önce aşamanın çerçevesini kuran sabit bir iş: aşama README'si, keşif turu, açık statülü ilk kalem listesi, varsayımlar, bütçe girdisi. |
| Nerede | `phases/<Pn-ad>/README.md` (aşama çerçevesi) ve `phases/<Pn-ad>/ISLER.md` (kalem listesi; MK-5.2). Şablon aşağıda. |
| Ne zaman | Kapı kaydı "geç" dediği anda (kendiliğinden geçişte aynı oturumda; durakta Batu'nun onay mesajından sonra). Hedefli geri dönüşte açılış yapılmaz; dönüş kalemi hedef aşamanın ISLER'ine eklenir. |
| Kim | Ana oturum yürütür. Keşif turunun okumaları alt ajanlara dağıtılır (T2: okuyucu ve eksik-arayıcı işlevleri). |
| Nasıl işler | 1) Aşama kartını `BEKLİYOR`'dan `AÇIK`'a çevir; SHA'yı yaz. 2) Keşif turunu koş (MK-4.1) ve bakış açısı taramasını yap (MK-4.2). 3) Çerçeve yeterliği sorusunu yaz (MK-4.6). 4) Çıkan işleri `aday` kalem olarak ISLER'e ekle; kabul edilenleri `kabul`e çevir (MK-5.7). 5) Varsayımları kaydet (MK-5.5). 6) Tahmini kalem sayısı, rota karışımı ve paralellik ihtiyacını T5'in bütçe mekanizmasına ver. 7) Commit et. Açılış kendisi bir kalemdir (`İK-Pn-000`) ve kalem kapısından geçer. |
| Zorlama düzeyi | Yapısal: README şablonu; `İK-Pn-000` kapanmadan başka kalem `sürüyor`a geçmez (MK-5.2 geçiş kuralı). |
| Çalıştığını nasıl anlarız | Her aşamanın git geçmişinde ilk commit bu dosyaları içerir. **Bozulma işareti:** aşamanın ilk alt ajan brief'i, açılış kalemi kapanmadan önce yazılmış. |
| Bağımlılıklar | İhtiyaç: MK-3.1, MK-4.1, MK-4.2, MK-4.6, MK-5.5; T2 okuyucu rolleri. Beslediği: MK-5.2, MK-5.3, T5 bütçe. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: her oturumun işi yeniden tanımlaması (EXP-006 kayması; R07 BS-1 "Yokluğunda"); keşfin atlanması. Kabul testi: yukarıdaki git geçmişi kontrolü. |
| Kaynak | R07 BS-1: "Use a different prompt for the very first context window…" (P-PBP; kd, T); E-HAR "Initializer agent" (g, 27.09.2026); R09 YD-1. |
| Bedel | Aşama başına bir oturumun önemli bölümü; keşif turunun okuma tokeni (tahmini 0,2–0,5 M; v). Batu'ya yük yok. |

```text
# Pn — <ad> · Aşama çerçevesi
Açılış: <tarih> · SHA <kısa> · Kart: PLAN.md §1 Pn
## Amaç zinciri    SOUL → DevOS → Pn: <soru> → beslediği karar: <…>
## Çıkış ölçütü    (PLAN.md'den işaretçi; kopyalanmaz)
## Keşif turu kaydı   → MK-4.1 şablonu
## Bakış açısı taraması → MK-4.2 şablonu
## Çerçeve notu      → MK-4.6 şablonu
## Bu aşamanın varsayımları → V-Pn-k (PLAN.md §3'e işaretçi)
## Bütçe girdisi     tahmini kalem: <n> · rota: yoklama <a> / sınırlı <b> / tasarım <c> · paralellik: <en fazla k>
```

#### MK-3.3 İş kalemi döngüsü: tasarım işinde "keşfet → planla → uygula → doğrula → kaydet"

| Alan | İçerik |
|---|---|
| Ne | Her iş kaleminin geçtiği sabit asgari döngü. Adımların derinliği rotaya göre değişir (MK-3.6). |
| Nerede | Kalem bloğu (`phases/<Pn>/ISLER.md`; MK-5.2); brief ve dönüş (T2); kalem kapanış satırları kalem bloğunun sonunda. |
| Ne zaman | Bir kalem `hazır` hesabını geçip seçildiğinde (MK-5.3). |
| Kim | Ana oturum yürütür; alt ajan çağrıları T2'nin rollerine gider. Kalem kapanışını alt ajan yapamaz. |
| Nasıl işler | **1) Keşfet** (salt okuma): amaç zincirini yaz (SOUL → DevOS → aşama → kalem → beslediği karar); mevcut kayıtları ve okuma rotasını belirle (MK-6.2). Tasarım rotasında bakış açısı taraması yapılır. **2) Planla:** bitti tanımını, kabul testini ve kapsam dışını işten önce yaz; tasarım rotasında 2–3 seçenek ve değerlendirme ölçütü. Bu, üreten ile değerlendiren arasındaki önceden anlaşmadır (E-HD "sprint contract"). **3) Uygula:** alt ajan brief'i (T2) → tek seferde yazılan çıktı dosyası. **4) Doğrula:** rotanın gerektirdiği kontrol (MK-3.6): yoklamada yalnız ana oturumun kaynak kontrolü, sınırlı işte hedefli karşı-okuma, tasarımda ayrı girdili karşı-okuma ve bütünsel inceleme (T4). **5) Kaydet:** kalem kapanış satırları, araştırma izi (MK-6.4), okuma kaydı (MK-6.3), yeni keşifler (MK-4.4), varsayım güncellemesi (MK-5.5), statü `doğrulandı`, commit. |
| Zorlama düzeyi | Yapısal: kalem bloğunda `bitti_tanımı` alanı `sürüyor`dan önce dolu olmak zorunda; kapanış satırları zorunlu alan. Zorlayıcı kontrol isteğe bağlıdır (T5): commit öncesi betik bu alanları arayabilir. |
| Çalıştığını nasıl anlarız | `git log -p ISLER.md` ile bitti tanımının statü `sürüyor`dan önce yazıldığı görülür. **Bozulma işareti:** bitti tanımı kapanış commit'inde değişmiş (ölçüt kaydırma; T4 ölçüt bütünlüğü). |
| Bağımlılıklar | İhtiyaç: MK-5.2, MK-5.3, MK-3.6, MK-6.2; T2 brief ve dönüş şeması; T4 karşı-okuma. Beslediği: MK-3.4 kalem ritmi, MK-4.4, MK-6.3, MK-6.4, T4 ilerleme ölçüsü. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Letting Claude jump straight to coding can produce code that solves the wrong problem" (BP) → tasarım işinde yanlış soruya cevap; "looks done" tek sinyal olur (BP). Kabul testi: yukarıdaki git kontrolü ve örneklem denetimi. |
| Kaynak | code.claude.com/docs/en/best-practices: "The recommended workflow has four phases" (Explore, Plan, Implement, Commit); "Separate research and planning from implementation to avoid solving the wrong problem." (kd, T; g, 27.09.2026). R07 BD-1, BD-2; A003 §3.1 madde 4–5. Tasarım işine uyarlama: ç. |
| Bedel | Kalem başına 5–8 kayıt satırı; yoklama rotasında 3. Token bedeli rotaya bağlı. |

```text
# Kalem kapanış satırları (kalem bloğunun sonuna eklenir)
kapanış: <tarih> · SHA <kısa> · statü: doğrulandı | bitti(doğrulanamadı: <neden>)
kanıt: <yol#bölüm> ; kontrol: <kim, hangi girdiyle, hüküm>
karar_değişti_mi: evet → <karar kaydı yolu> | hayır → <neden bu kalem yine de gerekliydi>
yeni_keşif: <İK-… / AS-… listesi ya da "yok">
varsayım_etkisi: <V-… güncellendi / yok>
```

#### MK-3.4 Ritim takvimi

| Alan | İçerik |
|---|---|
| Ne | Hangi kontrolün hangi olayda ya da ritimde yapıldığını tek tabloda sabitleyen takvim. İçeriği başka kartlarda ve kümelerdedir; bu kart "ne zaman"ın tek kaynağıdır. |
| Nerede | METHOD'un ritim bölümü (birleştirme dosyasında §7 "Ritimler"). Takvim aşağıda. |
| Ne zaman | Sürekli geçerli; olaylar tabloda. |
| Kim | Ana oturum. T5 açılış, kapanış ve uyandırma protokollerinin içeriğini, T4 raporların biçimini, T1 bellek yazımını sağlar. |
| Nasıl işler | Her olayda tablodaki adımlar sırayla yapılır ve izi yazılır. Periyodik yön gözden geçirmesi beş soruluk bir nottur (aşağıda). |
| Zorlama düzeyi | Tavsiye + yapısal: kalem kapanış satırları ve kapı kaydı zorunlu alandır. Oturum açılış sinyali bir `SessionStart` hook'uyla zorlayıcı yapılabilir; bu yalnız tek repolu oturumda çalışır ve A-04 onayı ister (R07 §7; T5'in kararı). |
| Çalıştığını nasıl anlarız | Her kapanan kalemde kapanış satırı; her 5 kalemde bir yön notu; her aşama kapısında kapı kaydı. **Bozulma işareti:** yön notları arasında 5'ten çok kalem kapanmış, ya da kapı kaydı olmadan aşama durumu değişmiş. |
| Bağımlılıklar | İhtiyaç: T5 (açılış, kapanış, uyandırma), T4 (rapor, alarm), T1 (bellek yazma anları). Beslediği: bütün S3–S6 kartları. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: kontrol noktalarının "hatırlanınca" yapılması; kayıt ve yön kontrolünün unutulması [R11 S3 "Ritimler"]. Kabul testi: yukarıdaki iz sayımı aşama raporunda yer alır. |
| Kaynak | R09 §4.4 YD-1…YD-9; R07 BS-2, BS-3; [R11 K34, K79]; A003 §3.6. |
| Bedel | Kalem başına kapanış satırları; 5 kalemde bir yaklaşık 10 satırlık yön notu; aşama başına kapı kaydı. |

| Olay / ritim | Yapılan (sahip kart) | Uyandırma gerekir mi? (T5 ile ilişki) |
|---|---|---|
| Oturum açılışı | Açılış sinyali: son karardan bu yana süre, `sürüyor` kalemler, bayat varsayımlar (T5, T4). **Yarım kalem önce devralınır** (R09 YD-6). Sonra hazır iş hesabı (MK-5.3). | Oturumu biri açmalı. Uyandırma denenmediği için bugün bu Batu'dur (V-H-1). |
| Alt ajan dönüşü | Dönüş veri sayılır; kaynak boşluğu alanı işlenir (MK-6.9); commit (T5 kontrol noktası). | Hayır: oturum içinde yeniden çağrılma bu oturumda gözlendi (R01; Cg). |
| Kalem kapanışı | MK-3.3'ün 5. adımı; kapanış satırları; kalem kapısı (MK-3.5). | Hayır. |
| Her 5 kapanan kalem ya da oturum başına en az bir kez (hangisi önce gelirse; v) | **Periyodik yön gözden geçirmesi**, beş soru: (1) Açık kalemler hâlâ aşamanın çıkış ölçütüne hizmet ediyor mu? (2) Son 5 kalemde kaç karar değişti? (3) Meta-iş payı (MK-3.8)? (4) Varsayım kaydında çöken ya da bayatlayan var mı? (5) Batu'nun son mesajı bir çerçeve değişikliği içeriyor mu? | Hayır. |
| Bağlam eşiğine yaklaşma (T1/T5) | Açık kalemin kapanış satırlarının ara hali yazılır; plan yüzeyleri güncel olmalı. | Hayır. |
| Aşama kapısı | MK-3.5 kapı kaydı → retro (T5) → bakım (T1/T5) → Batu'ya aşama raporu (T4) → geçiş türü (§2.4). | Kendiliğinden geçiş aynı oturumda sürer. Oturum kapanırsa bir sonraki açılışı bekler (V-H-1). |
| Batu'nun mesajı | Sınıflama (MK-5.6 1. adım); köken=Batu keşif kaydı (MK-4.4); çerçeve sorusuysa ilgili kalemler `park`. | — |
| Varsayım çöküşü, takılma alarmı | MK-5.6 revizyon; MK-5.10 takılma tepkisi. | Alarmın oturum dışında ateşlenmesi T5'e bağlı (b). |

**Önemli sınır (ç):** Uyandırma yoksa hiçbir ritim oturumlar arası boşlukta çalışmaz. Bu yüzden açılış sinyali, "son karardan bu yana X gün" satırını ilk satırda gösterir. Kanondaki ders budur: "Her oturum açılışında 'son koddan bu yana X gün' yazılır." [R11 K25]

#### MK-3.5 Kapılar ve durma koşulları

| Alan | İçerik |
|---|---|
| Ne | Dört kapı türü ve her birinin sabit kaydı: kalem kapısı, P2/P3 ortak kapısı, aşama çıkış kapısı, Batu kapısı (P0, P4, P5, P6). Tamamlanma katları ayrı tutulur: yapıldı ≠ doğrulandı ≠ işe yarıyor ≠ Batu kabul etti. |
| Nerede | Kalem kapısı: kapanış satırları (MK-3.3). Aşama ve ortak kapı: `phases/<Pn>/README.md` sonundaki "Kapı kaydı" bölümü. Batu kapısında kabul paketi T4'tedir; kapı kaydı pakete işaret eder. |
| Ne zaman | Kalem kapanışında; aşamanın bütün çıkış ölçütleri "karşılandı" görününce; Batu durağında. |
| Kim | Kalem ve aşama kapısında hükmü ana oturum verir. Karşı-okuma T4'ün kurallarıyla, ayrı girdili bir alt ajana yaptırılır. Batu kapısında hüküm Batu'nundur. |
| Nasıl işler | 1) Çıkış ölçütleri **değiştirilmeden** listelenir (ölçüt bütünlüğü; T4). 2) Her ölçüt için hüküm ve kanıt işaretçisi yazılır: karşılandı / karşılanmadı / doğrulanamadı. 3) "Kimseye verilmemiş iş" taraması eklenir (MK-4.5). 4) Kabul edilmiş plana göre sapmalar listelenir (MK-5.8). 5) Açık bulgular ve akıbetleri yazılır. 6) Hüküm: geç / geçme / koşullu geç (koşul yazılı). 7) Geçiş türü haritadan okunur: kendiliğinden ya da durak. |
| Zorlama düzeyi | Yapısal: kapı kaydı şablonu. Aşama kartının durumu kapı kaydı olmadan değişmez (MK-3.1). Zorlayıcı değil. |
| Çalıştığını nasıl anlarız | Her aşama geçişinde bir kapı kaydı var. **Bozulma işaretleri:** "koşullu geç" kararlarının koşulları sonraki aşamada izlenmemiş; kapı kaydında "doğrulanamadı" olduğu halde hüküm "geç" ve gerekçe yok; ölçüt metni kapı günü değişmiş. |
| Bağımlılıklar | İhtiyaç: T4 (karşı-okuma, bağımsızlık etiketi, kabul paketi, ilerleme ölçüsü), MK-4.5, MK-5.8. Beslediği: MK-3.1 durum alanı, T4 raporları, T5 retro. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: kendiliğinden geçişin frensiz kalması [R11 §5 Y12]; "work performed ≠ … authorized acceptance" [R11 K69]. Kabul testi: rastgele seçilen bir kapı kaydında her "karşılandı" hükmünün işaretçisi açılıp kanıtın gerçekten orada olduğu görülür. |
| Kaynak | K-002; A003 §3.5 ("'Bitti' dört ayrı şeydir"), §3.8; [R11 K15, K69, K88]; R04 (d)3: "review complete != gate satisfied != authorized go decision != enforced progression". |
| Bedel | Aşama başına tek sayfalık bir kayıt ve bir karşı-okuma çağrısı. Batu yalnız durak kapılarında okur. |

```text
## Kapı kaydı — <Pn çıkışı | P2/P3 ortak | İK-… kalem>
Tarih: <…> · Nesne: <dosya yolları> @ SHA <…> · Tür: kendiliğinden | DURAK
| # | Çıkış ölçütü (PLAN.md'den aynen) | Hüküm | Kanıt işaretçisi |
| 1 | …                                | karşılandı / karşılanmadı / doğrulanamadı | <yol#bölüm> |
Kimseye verilmemiş iş taraması: <tarih, kim, sonuç → İK-… / "yok">
Kabul edilmiş plana göre sapmalar: <SAP-… listesi>
Açık bulgular: <bulgu → akıbet: uygulandı / gerekçeyle reddedildi / park (tetik)>
Karşı-okuma: <rol, girdiler, bağımsızlık etiketi (T4)>
Hüküm: GEÇ | GEÇME | KOŞULLU GEÇ (koşul: … ; izleyen kalem: İK-…)
Karar veren: ana oturum (K-002) | Batu (mesaj: U0xx)
```

#### MK-3.6 Rota seçimi ve tören orantısı

| Alan | İçerik |
|---|---|
| Ne | Her kalemin üç rotadan birine dört risk sorusuyla atanması. Kontrol ağırlığı rotayı izler. |
| Nerede | Kalem bloğundaki `rota` ve `rota_gerekçesi` alanları (MK-5.2). Sorular aşağıda. |
| Ne zaman | Kalem `aday`dan `kabul`e geçerken; kapsam değişirse yeniden. |
| Kim | Ana oturum. |
| Nasıl işler | Dört soru: **S1** Bu çıktıya kaç karar ya da kalem dayanacak (aşağı akış yükü)? **S2** Etkisi geri alınabilir mi, yoksa dış etki mi (Batu'ya giden, kurulum, oturum ya da tetik açan)? **S3** Yaklaşım belirsiz mi (seçenekler belli değil)? **S4** Batu'nun sözüne, ölçütüne ya da kapsamına dokunuyor mu? **Atama:** S4 evet ya da S2 "dış etki" ise → **tasarım**. S1 ≥ 2 ya da S3 evet ise → **tasarım**. Bitti tanımı tek cümleyle yazılabiliyor ve tek karar besliyorsa → **sınırlı iş**. Tek olgu sorusuysa ve hiçbir karar doğrudan dayanmıyorsa → **yoklama**. **Rotaların asgari töreni:** yoklama = brief + dönüş + ana oturumun kaynak kontrolü; sınırlı iş = + önceden bitti tanımı + hedefli karşı-okuma (yalnız doğruluk ve yazılı gereksinim bulguları; BP); tasarım = + keşif ve bakış açısı + 2–3 seçenek + ayrı girdili karşı-okuma + bütünsel inceleme + yayılım kontrolü (T1). |
| Zorlama düzeyi | Yapısal: `rota` alanı zorunlu. |
| Çalıştığını nasıl anlarız | Aşama raporunda rota dağılımı ve yeniden rotalanan kalem sayısı. **Bozulma işaretleri:** yoklama rotasında kapanıp sonra bir karara dayanak olmuş kalem (aşağı akış hatası); tasarım rotasında olup kararı değiştirmemiş kalem oranı yüksek (boş tören). |
| Bağımlılıklar | İhtiyaç: T4 (karşı-okuma türleri), T5 (model ve efor seçimi rotaya bağlanabilir), T1 (yayılım kontrolü). Beslediği: MK-3.3, MK-3.8, T5 maliyet. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: ya "boş tören" ya eksik kontrol [R11 E15]; "düşük risk" sınıfının eleştirisiz kararları yayması (Y7). Kabul testi: yukarıdaki iki bozulma işaretinin sayımı aşama sonunda sıfır ya da gerekçeli. |
| Kaynak | BP: "Planning is most useful when you're uncertain about the approach … If you could describe the diff in one sentence, skip the plan." (kd, T; g, 27.09.2026); R07 BD-7; R09 YD-5 (superpowers üç rota); R08 O15 (BMAD: "intent gaps …, irreversible actions, and footprint"); R11 §5 Y7. |
| Bedel | Kalem başına iki satır. Yanlış sınıflama riski: S1'in tahmini yanılabilir (ç). |

#### MK-3.7 Pilot, sonra ölçekle (ilk örnek kuralı)

| Alan | İçerik |
|---|---|
| Ne | Yeni bir brief şablonu, rol, prosedür ya da paralel dağıtım önce tek bir kalemde denenir, gözden geçirilir, sonra çoğaltılır. P0'da Batu'nun concepts yöntemi (§2.5), P3'te döngünün küçük sınaması bu kuralın aşama ölçeğindeki karşılığıdır. |
| Nerede | Kalem bloğunda `ilk_ornek: evet` işareti ve `ilk_ornek_notu` (aşağıda). |
| Ne zaman | Bir mekanizma, şablon ya da rol ilk kez kullanıldığında; aynı brief N > 2 alt ajana dağıtılmadan önce. |
| Kim | Ana oturum. |
| Nasıl işler | 1) İlk kalemde uygula. 2) Dönüşü oku (R07 BO-7: "watched agents work step-by-step"). 3) Not yaz: ne işe yaradı, ne ters gitti, brief ya da şablonda ne değişti. 4) Değişikliği uygula ve sürümle (T2 brief sürümü). 5) Ancak sonra çoğalt. |
| Zorlama düzeyi | Tavsiye + yapısal (işaret alanı). |
| Çalıştığını nasıl anlarız | Her paralel dağıtımdan önce aynı brief'in bir `ilk_ornek_notu` var. **Bozulma işareti:** aynı brief hatası birden çok dönüşte tekrarlanmış. |
| Bağımlılıklar | İhtiyaç: T2 (brief sürümü, paralellik), T5 (paralellik bütçesi). Beslediği: MK-3.3, T5 öğrenme. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: aynı brief hatasının N kez ödenmesi (R07 BO-6); yöntemin kâğıtta kalması. **Sınır:** Bu kural kalıcı rol tanımını geciktirmez. Rol iskeleti işin döngüsünden şimdiden türetilir [R11 §5 Y4]. Kabul testi: yukarıdaki bozulma işaretinin yokluğu. |
| Kaynak | BP: "Refine your prompt based on what goes wrong with the first 2-3 files, then run on the full set." (R07 BO-6'nın aktarımı; kd, T); A003 §5; `concepts/ORIGIN.md` U01 adım 6–9 (Batu'nun sözü). |
| Bedel | Paralel işte bir dalga gecikme. |

```text
ilk_ornek: evet · ilk_ornek_notu: <tarih> — işe yarayan: … · ters giden: … · değişiklik: brief v<n>→v<n+1> (<ne>) · çoğaltma: <İK-… listesi>
```

#### MK-3.8 Yöntemin ağırlık bütçesi ve meta-iş sınırı

| Alan | İçerik |
|---|---|
| Ne | Yöntem işinin ürün işinin yerine geçtiğini erken gösteren üç ölçü ve eşikleri. |
| Nerede | Kalem bloğunda `hedef: ürün | yöntem` alanı (MK-5.2); ölçüler aşama raporunda (T4) ve periyodik yön notunda (MK-3.4). |
| Ne zaman | Her 5 kalemde ve aşama kapısında hesaplanır. |
| Kim | Ana oturum hesaplar. Eşik aşımı Batu'ya aşama raporunun ilk satırında gider. |
| Nasıl işler | **Ölçü 1 — meta-iş payı:** Aşamada kapanan kalemlerden `hedef: yöntem` olanların oranı. Yöntem kalemleri: METHOD, şablon, rol ya da yapılandırma değişikliği. P0 dışındaki eşik %25 (v). **Ölçü 2 — son ürün katkısından bu yana:** Aşamanın ana teslimatına katkı veren son commit'ten bu yana geçen kalem ve oturum sayısı. Eşik: 5 kalem ya da 2 oturum (v); T4'ün takılma alarmıyla birleşir. **Ölçü 3 — plan yüzeylerinin boyutu:** `PLAN.md` ve aktif `ISLER.md` boyutu. T1'in açılış seti bütçesine girer. **Aşım olursa:** yön gözden geçirmesi yapılır, raporda ilk satır olur ve bir sadeleştirme sorusu sorulur: "Hangi mekanizma bu aşamada hiçbir kararı değiştirmedi?" (R08 §8). Cevap T5'in sadeleştirme işine gider. |
| Zorlama düzeyi | Yapısal (alan ve rapor satırı). |
| Çalıştığını nasıl anlarız | Her aşama raporunda üç ölçü var. **Bozulma işareti:** meta-iş payı üst üste iki aşamada eşiği aşmış ve sadeleştirme kalemi açılmamış. |
| Bağımlılıklar | İhtiyaç: T4 (rapor, alarm), T5 (sadeleştirme, bütçe), T1 (açılış seti). Beslediği: MK-3.4, T5 öğrenme. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Süreç kendisi ürün oldu. Aynı dönemde süreç şablonuna (KEEL) yaklaşık 90 commit gitti." [R11 K27]; EXP-006'nın 17 dilimi [K46]. **Karşı ağırlık:** Eşik bir hedef değil teşhis girdisidir; düşük meta-iş payı tek başına iyi sayılmaz (R11 §5 Y13, vekil ölçü). Kabul testi: P0 pilotlarında ölçü hesaplanır ve eşik ayarlanır. |
| Kaynak | [R11 K27, K28, K46]; R11 §7.1 soru 6 ("süreç ürüne dönüşüyor sinyalini erken veren ölçü tanımlanmadı"); R08 O25; R06 G05. |
| Bedel | Kalem başına bir alan; aşama başına üç sayı. |

## 4. S4 — İhtiyaç ve kapsam keşfi

### 4.1 Amaç
Gerekli ama kimseye verilmemiş işi, önkoşulu, bakış açısını ve kaynak alanını Batu'nun hatırlatmasına gerek kalmadan bulmak. Bunları gerekçesiyle plana sokmak; eksik cevabı uydurmak yerine eksik soruyu kurmak. Keşif plandan ayrı bir alt sistemdir, çünkü "Plan self-review only covers work already in the plan" [R11 K79]. Repodaki üç olay keşif hatasıdır: EXP-005'in sonucu [K38], soru bankası [K41], EXP-006'nın rol türetimi [K52]. R11'in bulgusuna göre olayla desteklenen dört çıkış kenarı S4'ten başlar; bu alt sistem Batu'nun yükünün kaynağıdır [R11 §4.5].

### 4.2 Bileşenler ve karar tablosu

| Bileşen | Karar | Önlediği hata | Kabul testi | Kart | Kaynak |
|---|---|---|---|---|---|
| Amaçtan ve kullanımdan geriye önkoşul keşfi ("bu amaç için önce ne doğru olmak zorunda?", "bu çıktıyı kim, hangi kararda kullanacak?") | gerekli | Keşif yükü Batu'ya döner (EXP-005) | Her aşama açılışında keşif turu kaydı var; turdan çıkan kalemlerin en az biri tüketiciden geriye akıl yürütmeyle bulunmuş ya da "yok" gerekçesi yazılmış | MK-4.1 | [R11 K38, K60]; EXP-004 DQ01 §2–3 |
| Bakış açısı taraması (üretim, kullanım, etki, bakım, başarısızlık, Batu yükü, ortam; Foundation'ın dört zemini) | gerekli | Soru bankası olayı: üretim perspektifi kaçtı [K41] | Tasarım rotasındaki her kalemde tarama tablosu dolu; boş hücreler "bulgu yok" diye yazılmış | MK-4.2 | [R11 K41, K42] |
| Eksik soruyu kurmak: açık soru kaydı (`return_to` dahil) | gerekli | Boşluk uydurmayla doldurulur; bitmemiş keşif oturum devrinde kaybolur | Her açık sorunun `return_to` alanı dolu; kapanan soruların cevabının nerede kullanıldığı yazılı | MK-4.3 | DQ01: "Eksik cevabı uydurmak yerine eksik soruyu kurmak, keşfin bir parçasıdır." (g); RPD ASSESSMENT §5 (g) |
| Keşfin kökeni ve akıbeti; amaç ihtiyacı ile yöntem ihtiyacı ayrımı; Batu'nun bulduklarının işaretlenmesi | gerekli | Keşif başarısı Batu'nun katkısıyla şişer; seçilen yöntemin doğurduğu iş amaç sanılır | Her kalemde `köken` ve `neden` dolu; aşama raporunda köken dağılımı var | MK-4.4 | [R11 K60, K79, K83]; R06 G01 |
| "Kimseye verilmemiş iş var mı?" taraması ve eksik-arayıcı işlevi, brief'ten bağımsız kaynak alanıyla | gerekli | Erken kapanış; eksik iş "tamam" damgası alır [R11 E19] | Her aşama kapısında tarama kaydı var; eksik-arayıcıya verilen kaynak alanı brief'in kaynak listesinin üst kümesi | MK-4.5 | [R11 K41, K79, K110]; R11 §5 Y15 |
| Kaynak alanı seçimi keşfin parçasıdır (verilen liste bütün alan sayılmaz) | gerekli | "niye sadece EXP-004'e gönderiyorsun?" [K40] | Keşif turu kaydında seçilen ve bilerek dışarıda bırakılan kaynaklar gerekçeli | MK-4.1 adım 5; MK-6.2 | [R11 K40]; R09 protokolü: "Retrieval miss study absence değildir" (g) |
| Çerçeve yeterliği sınaması | gerekli | Roller yanlış kaynaktan türer [K52] | Her aşama açılışında ve her türetme kararında çerçeve notu var | MK-4.6 | [R11 K52]; A003 §1 |

Gereksiz sayılan bileşen yok. R11'in "iş tamamen önceden tanımlıysa" koşulu bu işte sağlanmıyor: harita bile P0.4'te yazılıyor (ç).

### 4.3 Mekanizma kartları

#### MK-4.1 Aşama keşif turu: amaçtan ve kullanımdan geriye akıl yürütme

| Alan | İçerik |
|---|---|
| Ne | Aşama açılışında (ve yeni bir teslimat ortaya çıktığında) gerekli işi, önkoşulları, açık soruları ve kaynak alanını çıkaran sabit adımlı tur. |
| Nerede | `phases/<Pn>/README.md` "Keşif turu kaydı" bölümü (şablon aşağıda). Çıktılar `ISLER.md`'ye aday kalem ve açık soru olarak girer. |
| Ne zaman | MK-3.2'nin 2. adımı. Ayrıca tasarım rotasındaki bir kalemin "keşfet" adımında küçültülmüş haliyle koşulur. |
| Kim | Ana oturum yürütür. Okumalar alt ajanlara gider (T2: okuyucu işlevi). Aşama kapsamı büyükse bir eksik-arayıcı paralel ve bağımsız bir tur yapar (MK-4.5). |
| Nasıl işler | 1) **Amaç zinciri:** SOUL → DevOS → aşama → çıkış ölçütü → beslediği karar. 2) **Önkoşul sorusu** iki kat derine: "Çıkış ölçütü k'nin sağlanması için önce ne doğru olmak zorunda?" Her cevap için aynı soru bir kez daha sorulur (RPD'nin kök sorusu; EXP-006'da kullanıldı [R02 §2]). 3) **Kullanımdan geriye:** "Bu aşamanın teslimatını kim, hangi kararda, hangi biçimde kullanacak? O kullanım için neyin doğru ve erişilebilir olması gerekir?" (DQ01 §2–3). 4) **Sınıflama** (A003 §3.1): her bulgu repoda var / araştırılır / teknik karar / denenir / Batu'nun değeri, tercihi ya da yetkisi. 5) **Kaynak alanı:** hangi Foundation girişleri (REUSE satırları), hangi studies (CATALOG'dan ihtiyaç ve işlev adıyla aranır), hangi dış kaynak. Bilerek dışarıda bırakılanlar gerekçesiyle yazılır. 6) **Çıktı:** aday kalemler (MK-5.2), açık sorular (MK-4.3), varsayımlar (MK-5.5). |
| Zorlama düzeyi | Yapısal: şablon. `İK-Pn-000` açılış kalemi bu kayıt dolmadan kapanamaz (MK-3.2). |
| Çalıştığını nasıl anlarız | Aşama boyunca keşfedilen kalemlerin kökeni izlenir (MK-4.4): açılış turunda bulunanlar ile sonradan bulunanların (özellikle Batu kökenlilerin) oranı. **Bozulma işareti:** aşama ortasında Batu'nun yakaladığı bir eksik, açılış turunun sorularından birinin doğrudan cevabıymış. |
| Bağımlılıklar | İhtiyaç: MK-6.1/6.2 (araştırma rotası), MK-4.2, T2 okuyucu, T1 bağlam paketi. Beslediği: MK-5.2, MK-4.3, MK-5.5, MK-4.5. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Önlemeye çalışılan kullanıcıya bağımlı ihtiyaç/önkoşul/devir keşfi sorunu, onu düzeltmek için yürütülen süreçte yeniden ortaya çıktı." (EXP-005 LESSONS, Sonuç; kd, repo olayı; g, 27.09.2026). Kabul testi: P0 Pilot-2'de tur koşulur; turun bulmadığı ama Batu'nun bulduğu eksik sayısı kaydedilir. |
| Kaynak | [R11 K38, K60]; EXP-004 DQ01 §2 (g); RPD kök sorusu (R02 §2); A003 §3.1; R03 ilke 4: "ilk iş işi yapmaya başlamak değil işi ortaya çıkarmak". |
| Bedel | Aşama başına bir tur; tasarım kalemlerinde küçük bir tur. Okuma tokeni aşama bütçesine yazılır (T5). |

```text
## Keşif turu kaydı — Pn · <tarih> · SHA <kısa>
Amaç zinciri: SOUL → DevOS → Pn (<ana soru>) → beslediği karar: <…>
| Çıkış ölçütü | Önce doğru olmak zorunda (1. kat) | (2. kat) | Sınıf | Çıktı |
| Ö1 | … | … | araştırılır | AS-Pn-003 |
Kullanımdan geriye: tüketici <kim/rol> · karar <…> · gereken <…> → <İK/AS>
Kaynak alanı: seçilen <REUSE satırı / study META / dış> · bilerek dışarıda <kaynak — neden>
Sonuç: aday kalemler <İK-…> · açık sorular <AS-…> · varsayımlar <V-…>
```

#### MK-4.2 Bakış açısı taraması

| Alan | İçerik |
|---|---|
| Ne | İlk göze çarpan görüşe çapalanmayı önleyen sabit mercek listesi. Her mercekten ya bir bulgu ya da "bulgu yok" çıkar. |
| Nerede | Aşama README'sinde "Bakış açısı taraması" bölümü; tasarım rotasındaki kalemlerde kalem bloğuna eklenen küçük tablo. |
| Ne zaman | Aşama açılışında (MK-3.2), tasarım rotasındaki her kalemin "keşfet" adımında, kapıdan önce (MK-4.5 ile birlikte). |
| Kim | Ana oturum. Kapıdan önceki taramayı, üreticinin gerekçesini görmeyen bir alt ajan yapar (T4 karşı-okuma kuralı). |
| Nasıl işler | Mercekler (A–G) ve Foundation zeminleri (H): **A üretim** (bu nasıl gerçekten üretilecek, kim, hangi araçla?) · **B kullanım** (kim tüketecek, hangi kararda?) · **C etki** (neyi ve kimi değiştirir?) · **D bakım** (zamanla nasıl güncel tutulur, kim tutar?) · **E başarısızlık** (nasıl bozulur, bozulduğunu kim görür?) · **F Batu yükü** (Batu'ya hangi okuma, karar ya da hatırlatma yükünü bırakır?) · **G ortam** (cloud'da gerçekten mümkün mü; P1 kanıtı var mı?) · **H Foundation zeminleri** (Work, Information, Actors, Environment; Composition): REUSE soru-ilk tablosunun ilgili satırı sorulur. |
| Zorlama düzeyi | Yapısal: tablo; boş hücre yasak ("bulgu yok" yazılır). |
| Çalıştığını nasıl anlarız | Tarama bulgularının akıbeti (MK-4.4): kaçının kaleme dönüştüğü. **Bozulma işaretleri:** bütün hücreler "bulgu yok" ve aynı gün doldurulmuş (tören); ya da kapıdan sonra, bir merceğin tam da soracağı bir eksik bulunmuş. |
| Bağımlılıklar | İhtiyaç: MK-6.2 (Foundation rotası), T4 karşı-okuma. Beslediği: MK-4.1, MK-4.5, MK-5.2. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "The assistant nevertheless declared the example finished." (Foundation DISCUSSION-HANDOFF; kd, repo olayı; ana oturum doğruladı, R04 başlığı) → eksik perspektif Batu'ya kaldı [R11 K41]. Kabul testi: Pilot-2'de tarama koşulur; soru bankası olayı geriye dönük bir sınama vakası olarak taramaya verilir (üretim merceği eksiği yakalıyor mu?). |
| Kaynak | [R11 K41, K42]; REUSE "Question-first entry" (g); R03 ilke 3 ("aslında bu da var"). |
| Bedel | Tasarım kalemi başına 7–8 satır; aşama başına bir tablo. |

```text
| Mercek | Soru | Bulgu | Çıktı |
| A üretim | Bu nasıl gerçekten üretilecek? | … / bulgu yok | İK-… / — |
| … | … | … | … |
| H Work (REUSE) | "What pursuit is authorized, what is only a plan…?" | … | AS-… |
```

#### MK-4.3 Açık soru kaydı: eksik soruyu kurmak

| Alan | İçerik |
|---|---|
| Ne | Cevabı bilinmeyen her yük taşıyan sorunun, hangi karar için gerektiği, nereye döneceği ve hangi yolla cevaplanacağıyla birlikte kaydı. Batu'ya giden soru kuyruğu (T4) bu kaydın bir alt kümesidir; ayrı kopya tutulmaz. |
| Nerede | `phases/<Pn>/ISLER.md` "Açık sorular" bölümü (T1 başka bir yer seçebilir; tek kaynak şartı). |
| Ne zaman | Bir kalem, keşif turu, alt ajan dönüşü (MK-6.9) ya da karşı-okuma bir boşluk bulduğunda. Bir cevap uydurulmak üzereyken (A003 §3.1: "bilmiyorsam 'bilmiyorum' derim"). |
| Kim | Ana oturum yazar. Alt ajan yalnız dönüşünde önerir. |
| Nasıl işler | 1) Soruyu tek cümleyle yaz, hangi karar ya da kalem için olduğunu ekle. 2) **Sınıfla** (A003 §3.1 sırası; Batu'ya sormak son seçenektir): repoda var → okuma kalemi · araştırılır → araştırma kalemi · teknik karar → ana oturum karar verir, otomatik seçim kaydına yazar (T4) · denenir → deneme kalemi · Batu'nun değeri, tercihi ya da yetkisi → T4 soru kuyruğu. 3) **Çerçeve sorusu mu?** Amaç, kapsam ya da ölçüte dokunuyorsa biriktirilmez, hemen Batu'ya gider; etkilediği kalemler `park` edilir [R11 §5 Y11 dengeleyicisi]. 4) `return_to` alanı doldurulur: cevap gelince hangi kalem ya da karar yeniden ele alınır. 5) Cevap gelince "nerede kullanıldı" alanı doldurulur. Cevabın kullanılmaması da gerekçesiyle yazılır. |
| Zorlama düzeyi | Yapısal: zorunlu alanlar. |
| Çalıştığını nasıl anlarız | Açık soruların yaşı ve `return_to` karşılanma oranı aşama raporunda. **Bozulma işaretleri:** cevaplanmış ama "nerede kullanıldı" boş olan soru; bir çerçeve sorusunun kuyrukta bekletilmesi. |
| Bağımlılıklar | İhtiyaç: T4 (soru kuyruğu biçimi, otomatik seçim kaydı), T2 (dönüş şemasında soru alanı). Beslediği: MK-5.3 (hazır hesabı: açık çerçeve sorusu olan kalem hazır değildir), MK-5.6, T4 ilerleme ölçüsü ("kapanan soru"). |
| Standart seviye kararı | **Gerekli.** Önlediği hata: boşluğun uydurmayla düzlenmesi [R11 S15 "Belirsizlik beyanı"]; bitmemiş keşfin devirde kaybolması: "Bir işin `next action` kaydı, bitmemiş keşfin `odak ihtiyaç / açık soru / beklenen alt sonuç / return_to / yöntem-alternatif / geçerlilik` durumunu her zaman korumaz." (RPD ASSESSMENT §5; kd, ürün kaynağı değil kavramsal değerlendirme; g, 27.09.2026). Kabul testi: soğuk başlangıç testinde taze oturum açık soruları ve neyi beklediklerini doğru sayar. |
| Kaynak | DQ01 (g); RPD ASSESSMENT §5 (g); A003 §3.1, §3.9; R05 #7; [R11 K15] ("Sorular biriksin, iş durmasın"). |
| Bedel | Soru başına bir blok; kuyruk bakımı. |

```text
AS-P2-004 · durum: açık | cevaplandı | park(tetik: …)
soru: <tek cümle> · hangi karar/kalem için: <İK-…/karar>
sınıf: repoda var | araştırılır | teknik karar | denenir | Batu (tercih | yetki | değer) · çerçeve_sorusu: evet/hayır
beklenen alt sonuç: <…> · yöntem/alternatif: <…> · geçerlilik: <ne zaman bayatlar>
return_to: <İK-… / karar> · köken: <MK-4.4 değerleri>
cevap: <özet + kaynak yolu> · nerede kullanıldı: <karar kaydı yolu | kullanılmadı: neden>
```

#### MK-4.4 Keşif kaydı: köken, akıbet ve ihtiyacın nedeni

| Alan | İçerik |
|---|---|
| Ne | Her yeni ihtiyacın, kalemin ve açık sorunun **kim tarafından bulunduğu**, **amaçtan mı yoksa seçilen yöntemden mi doğduğu** ve **ne olduğu** (kabul, düştü, park). Batu'nun bulduğu eksikler ayrıca işaretlenir ve sayılır. |
| Nerede | Kalem ve soru bloklarında `köken`, `neden`, `akıbet` alanları (MK-5.2, MK-4.3). Batu kökenli kayıtlar, T4'ün hatırlatma ve düzeltme kaydına bir işaretçi satır da ekler (tek kaynak: ayrıntı kalem bloğunda). |
| Ne zaman | Kalem ya da soru yaratıldığı anda; akıbet değiştiğinde. |
| Kim | Ana oturum. |
| Nasıl işler | 1) `köken` değerleri: `ana-oturum` · `alt-ajan:<brief ID>` · `karşı-okuma:<brief ID>` · `eksik-arayıcı:<brief ID>` · `keşif-turu:<Pn>` · `Batu:<U0xx>`. 2) `neden` değerleri: `amaç` (Batu'nun amacından ya da aşamanın çıkış ölçütünden) · `yöntem:<hangi seçim>` (seçilen bir yöntemin doğurduğu koşul; DQ01 §2). 3) `akıbet`: `kabul` · `düştü:<reddedildi | yerine kondu | sonlandırıldı | başarısız>` · `park:<tetik>`. 4) Köken `Batu` ise ek alan: `kaçıran_alt_sistem`: hangi keşif ya da denetim mekanizması bunu yakalamalıydı (MK-4.1 soru no, MK-4.2 mercek ya da T4 kontrolü). 5) Aşama raporunda köken dağılımı ve Batu kökenli keşif sayısı verilir. |
| Zorlama düzeyi | Yapısal: zorunlu alanlar. |
| Çalıştığını nasıl anlarız | Aşama raporunda köken dağılımı; Batu kökenli keşiflerin "kaçıran alt sistem" alanı dolu. **Bozulma işaretleri:** Batu kökenli keşif oranının aşamadan aşamaya düşmemesi; `yöntem` kökenli kalemlerin aşama çıkış ölçütüne bağlanmadan çoğalması (meta-iş; MK-3.8). |
| Bağımlılıklar | İhtiyaç: T4 (hatırlatma kaydı, ilerleme raporu). Beslediği: MK-3.8, T4 ölçüleri, T5 öğrenme (hata sınıflandırması). |
| Standart seviye kararı | **Gerekli.** Önlediği hata: keşif başarısının Batu'nun katkısıyla şişmesi: "A correction supplied by the owner 'SOUL'un kendiliğinden keşif başarısı diye sayamayız'" (R06 §3 madde 8; EXP-004 DQ02). Seçilen yöntemin doğurduğu işin amaç sanılması (DQ01 §2). **Vekil ölçü uyarısı:** Batu kökenli keşif sayısı hedef değil, teşhis girdisidir. Batu yorulup hatırlatmayı bırakırsa sayı yanıltıcı biçimde düşer (R10 §1 madde 7; R11 §5 Y13). Bu yüzden `kaçıran_alt_sistem` alanı sayıdan önemlidir. Kabul testi: P0 pilotlarında köken alanları doldurulur ve raporda görünür. |
| Kaynak | [R11 K60, K79]; R06 G01: "Log each new need or work item with where it came from … and what happened to it"; EXP-004 DQ01 §2 (g): "Bazı ihtiyaçlar da önceden var olan gerçeğin keşfi değil, seçilen yöntem ya da yeni yaratıcı kararın doğurduğu koşullardır."; A003 §3.6 ("nereden çıktığı"). |
| Bedel | Kalem başına üç alan. |

#### MK-4.5 "Kimseye verilmemiş iş" taraması

| Alan | İçerik |
|---|---|
| Ne | Planın kendi kör noktasını, plan dışından bakarak kapatan tarama. Sahibi bir eksik-arayıcı işlevidir (T2). Bu işlev brief'in kaynak listesiyle sınırlanmaz. |
| Nerede | Kapı kaydındaki "Kimseye verilmemiş iş taraması" satırı (MK-3.5); tarama sonucunun kendisi bir alt ajan dönüş dosyasıdır (T2'nin dönüş yeri). |
| Ne zaman | Her aşama kapısından önce; tasarım rotasındaki kalemin kapanışında; Batu'ya kabul paketi gitmeden önce. Geri alınması ucuz ve kimsenin dayanmadığı ara adımda yapılmaz (R11'in "gereksiz" koşulu). |
| Kim | Eksik-arayıcı işlevi (T2'ye ihtiyaç: kalıcı rol ya da ana oturum görevi). Hükmü ana oturum verir. |
| Nasıl işler | 1) Eksik-arayıcıya verilir: aşamanın çıkış ölçütleri, Batu'nun ilgili sözleri **birebir** (T1/S10), aşamanın teslimatları @SHA, **ve brief'ten bağımsız bir kaynak alanı** (aşamanın bütün girdi klasörleri, REUSE tablosu, CATALOG). Ana oturumun gerekçesi ve plan kalemlerinin listesi **verilmez**: gerekçeyi görmeyen okuma ilkesi (T4). 2) Sorular: (a) "Çıkış ölçütlerinin sağlanması için gerekli olduğu halde hiçbir kaleme verilmemiş iş var mı?" (b) "Okunması gerekip okunmamış kaynak var mı?" (c) "Bu teslimatı kullanacak kişi ya da rol için eksik ne?" (d) "Batu'nun sözlerinden hangisinin karşılığı teslimatta yok?" 3) Dönüş: bulgu listesi; her bulgunun gerekçesi ve kanıt işaretçisi; "bulgu yok" geçerli bir sonuçtur. 4) Ana oturum her bulguya akıbet yazar: yeni kalem (köken `eksik-arayıcı`) / gerekçeyle reddedildi / park. |
| Zorlama düzeyi | Yapısal: kapı kaydında zorunlu satır. Gerekçeyi görmeyen okuma bir tavsiyedir; yapısal hali, brief şablonunda "verilmeyecekler" alanıdır (T2). |
| Çalıştığını nasıl anlarız | Kapı sonrası bulunan eksiklerin sayısı ve kaynağı. **Bozulma işareti:** kapıdan sonra Batu'nun bulduğu bir eksik, tarama sorularından birinin doğrudan cevabı. Aynı eksik hem üretende hem tarayanda varsa bu ortak brief eksiğinin işaretidir [R11 E65]. |
| Bağımlılıklar | İhtiyaç: T2 (eksik-arayıcı işlevi, brief şablonu), T4 (karşı-okuma ilkeleri, bağımsızlık etiketi), T1 (Batu'nun sözlerinin birebir deposu). Beslediği: MK-3.5, MK-4.4, MK-5.2. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Plan self-review only covers work already in the plan" [R11 K79]; soru bankası olayında eksik perspektifi Batu gösterdi [K41]; kaynak seçimini brief'e bırakınca eksik hem üretene hem inceleyene geçer (R11 §5 Y15). Kabul testi: Pilot-2'de tarama, üreticinin kaynak listesinde olmayan en az bir ilgili kaynağı bulabiliyor mu ya da "yok" gerekçesi inandırıcı mı? Karşı-okuyucu bunu değerlendirir. |
| Kaynak | A003 §3.8: "gerekli olduğu halde kimseye verilmemiş iş var mı?"; A003 §3.2 (eksik-arayıcı); [R11 K41, K79, K101]; R05 #25. |
| Bedel | Kapı başına bir alt ajan çağrısı (orta boy okuma). Batu'ya yük yok. |

#### MK-4.6 Çerçeve yeterliği sınaması

| Alan | İçerik |
|---|---|
| Ne | Bir türetmenin (rol listesi, döngü, kayıt mimarisi, yürütme yolu seçimi) doğru kaynaktan ve doğru çerçeveden gelip gelmediğini soran kısa sınama. |
| Nerede | Aşama README'sinde "Çerçeve notu"; türetme içeren tasarım kalemlerinde kalem bloğuna bir satır. |
| Ne zaman | Aşama açılışında; bir türetme kararından önce; Batu bir itiraz ya da yeni yön verdiğinde (W8). |
| Kim | Ana oturum. Tasarım rotasında karşı-okuyucu da aynı soruları bağımsız cevaplar. |
| Nasıl işler | Dört soru: (1) "Bu türetme hangi kaynaktan yapılıyor? Batu'nun sözü hangi kaynağı ya da çerçeveyi istiyor?" (birebir alıntıyla). (2) "Hangi alternatif çerçeve farklı bir sonuç verirdi?" (en az bir tane). (3) "Kaynak çerçeve, türetilen şeyin kendi işini de kapsıyor mu?" Örnek: roller yalnız SOUL yeteneklerinden türetilirse ekibin kendi döngüsü dışarıda kalır. (4) "Bu çerçeve, kendi türetme kalıbını sonuç olarak geri bulma riski taşıyor mu?" (EXP-006'da aileler, türetme kalıbını büyük ölçüde geri buldu [R02 §2]). Yetersizlik bulunursa: çerçeve değişikliği amaç, kapsam ya da ölçüte dokunuyorsa Batu'ya gider (MK-4.3 çerçeve sorusu). Dokunmuyorsa revizyon protokolü işler (MK-5.6). |
| Zorlama düzeyi | Yapısal: not şablonu. |
| Çalıştığını nasıl anlarız | P2 ve P3 kapısında çerçeve notu var ve alternatif çerçeve gerçekten değerlendirilmiş. **Bozulma işareti:** kapıdan sonra Batu ya da karşı-okuma "yanlış kaynaktan türetildi" türü bir itiraz getiriyor. |
| Bağımlılıklar | İhtiyaç: T1 (Batu'nun sözleri birebir), T4 (karşı-okuma). Beslediği: MK-5.6, MK-4.3, P2/P3 ortak kapısı. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Roles were derived from SOUL's target capacities (B1–B9), not from the DevOS team's own working loop." [R11 K52]. Kabul testi: P2 kapısında her rolün türetme izinde iki kaynağın da yer alması (§2.3 P2 çıkış ölçütü 1). |
| Kaynak | [R11 K52]; R02 §2, §4(b); A003 §1–§2; R11 S4 "Çerçeve yeterliği sınaması"; EXP-004 G01 ("Discovery/Frame Adequacy") [R11 K60]. |
| Bedel | Türetme başına 4–6 satır. |

```text
Çerçeve notu — <türetme konusu> · <tarih>
Kaynak çerçeve: <…> · Batu'nun istediği (birebir): "<alıntı>" (<U0xx>)
Alternatif çerçeve: <…> → farklı sonuç: <…>
Kapsama: türetilen şeyin kendi işi dahil mi? <evet/hayır + neden>
Geri bulma riski: <var/yok + gerekçe> · Hüküm: yeterli | yetersiz → <AS-… çerçeve sorusu | revizyon DEĞ-…>
```

## 5. S5 — Plan ve iş yönetimi

### 5.1 Amaç
Bilinen işi yaşayan bir planda tutmak: statüleri, bağımlılıkları, sahipleri, varsayımları ve değişiklik geçmişiyle birlikte. Hazır işi hesaplamak ve aynı anda açık işi sınırlamak. Revizyonu kontrollü yapmak: kabul edilmiş sürüm korunur, sapma ayrı yazılır, kimin neyi değiştirebileceği bellidir. R11'e göre plan, uzun soluklu işte bozulmaların toplandığı yerlerden biridir (9 giriş kenarı, 7'si olayla destekli) [R11 §4.3].

### 5.2 Bileşenler ve karar tablosu

| Bileşen | Karar | Önlediği hata | Kabul testi | Kart | Kaynak |
|---|---|---|---|---|---|
| Tek ana harita ve aşama iş listesi (tek kaynak yüzeyleri) | gerekli | Yön dağılır; durum 5–7 dosyada kopyalanır [K49] | Aynı kalem ya da aşama durumu iki dosyada yetkili olarak geçmiyor (STATE yalnız işaretçi) | MK-5.1 | [R11 K110, K49] |
| Kalem şeması ve statü makinesi (aday → kabul → sürüyor → bitti → doğrulandı; park; düştü + neden türü) | gerekli | Bütün kalemler "iptal" ya da "bitti"ye çöker; "olmadı"nın nedeni kaybolur [K112] | Her kalemde zorunlu alanlar dolu; hiçbir kalem bloğu silinmemiş | MK-5.2 | [R11 K110, K112]; R04 (a)1 |
| Bağımlılık türleri ve hazır iş hesabı; aynı anda açık iş sınırı | gerekli | Gereksiz bekleme ya da yanlış sıra; çok iş başlatmak ilerleme sanılır | Hazır hesabı yalnız `önkoşul` bağlarını kullanıyor; `sürüyor` kalem sayısı sınırı aşmıyor | MK-5.3 | beads FINDINGS §2, §4 (g); [R11 K79, K83, K112] |
| Dilim boyutlandırma | gerekli | Soru üreten dilim: "16 görevin hiçbiri kod üretmedi" [K30] | Kapanan kalemlerin her biri bitti tanımındaki sonucu üretmiş; soru üreterek kapanan kalem sayısı raporda | MK-5.4 | [R11 K30] |
| Varsayım ve risk kaydı | gerekli | Çöken varsayım plan boyunca taşınır | Her aşama kartındaki varsayımlar kayıtta; periyodik yön gözden geçirmesinde durumları güncel | MK-5.5 | [R11 K110]; R08 §2.11 (Magentic olgu sınıfları) |
| Revizyon protokolü: tetik, sınıflama, yetki, not, yayılım | gerekli | Plan geçmişi yeniden yazılır; yön sessizce kayar | Her revizyonda değişiklik kaydı satırı ve sınıflama var; etkilenen kalemler işaretli | MK-5.6 | [R11 K100, K110, K46, K111]; R10 §4.2 |
| Revizyon yetkisi tablosu | gerekli | Ya her şey Batu'ya gider ya Claude Batu adına amaç değiştirir | Değişiklik kaydındaki her satırda "karar veren" alanı tabloyla tutarlı | MK-5.7 | R04 (a)4; A003 §3.7 |
| Kabul edilmiş plan sürümü ve sapma kaydı | gerekli | "A bad plan can appear to have been 'correct'…" [K100] | Kapı kaydında sapma listesi, kabul edilmiş sürüme işaret ediyor | MK-5.8 | [R11 K100]; R05 #9 |
| Park, düşürme ve yeniden açma kuralı | gerekli | Sessiz kayıp ya da sonsuz yeniden açma | Her `park` kaleminde tetik; her yeniden açmada adı konmuş gerekçe ve daraltılmış kapsam | MK-5.9 | [R11 K83, K110]; R04 (a)5 |
| Takılmaya plan tepkisi ve yeniden planlama (tespit T4'te) | gerekli | Aynı hata tekrarlanır; hareket var, ilerleme yok | Her takılma alarmının ardından sınıflanmış bir tepki kaydı var; aynı brief değiştirilmeden tekrar gönderilmemiş | MK-5.10 | R08 O17; [R11 K25, K79] |
| JSON biçiminde yapılandırılmış iş listesi (E-HAR) | **bilinmiyor** | Modelin kalemleri sessizce değiştirmesi ya da silmesi | P0 pilotlarında blok biçimli Markdown kalemlerde silme ya da yeniden yazma olayı olursa JSON/YAML'a geçilir | MK-5.2 notu | R07 BS-4: "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files" (E-HAR; kd, T; yazılım işi için) |

### 5.3 Mekanizma kartları

#### MK-5.1 Yaşayan plan yüzeyleri

| Alan | İçerik |
|---|---|
| Ne | Planın üç yüzeyi ve tek kaynak kuralı: `PLAN.md` (harita düzeyi), `phases/<Pn>/ISLER.md` (aşama iş listesi ve açık sorular), `STATE.md` (yalnız işaretçiler). |
| Nerede | Yollar önerilir; T1'in dosya mimarisine uydurulur. Çelişirse birleştirme ajanı karar verir. A003 §5'teki "PLAN.md: harita + aşama iş listeleri + tarihli değişiklikler" önerisi ikiye bölündü: iş listesi aşama klasörüne taşındı, çünkü kök dosya her aşamada büyüyüp açılış setini şişirir (R11 §4.5 şişme döngüsü). |
| Ne zaman | Sürekli; yazma anları MK-3.4 ritimleridir. |
| Kim | Tek yazıcı ana oturumdur (T2). Alt ajanlar plan yüzeylerine yazmaz; önerileri dönüşte gelir. |
| Nasıl işler | `PLAN.md` bölümleri: §1 Harita (aşama kartları; MK-3.1) · §2 Kabul edilmiş sürüm işaretleri (MK-5.8) · §3 Varsayım ve risk kaydı, harita düzeyi (MK-5.5) · §4 Değişiklik kaydı, ekleme-yalnız (MK-5.6). `ISLER.md` bölümleri: §1 Kalem blokları (MK-5.2), ekleme-yalnız; yalnız statü, akıbet ve kapanış alanları güncellenir · §2 Açık sorular (MK-4.3) · §3 Aşama varsayımları (MK-5.5). `STATE.md`'de yalnız şu satırlar bulunur: şu anki aşama; `sürüyor` kalem kimlikleri; sıradaki yetkili kalem kimliği; Batu'dan beklenen soru kimlikleri. İçerik kopyalanmaz. |
| Zorlama düzeyi | Yapısal: şablonlar ve "kalem bloğu silinmez" kuralı. Zorlayıcı seçenek T5'te: commit öncesi ya da `Stop` hook'unda, bir önceki commit'teki `İK-` kimliklerinin hâlâ var olduğunu denetleyen tek satırlık betik. Tek repolu oturum koşulu ve A-04 onayı gerekir. |
| Çalıştığını nasıl anlarız | `git diff` ile silinen kalem bloğu yok. STATE ile ISLER'deki statüler çelişmiyor. **Bozulma işareti:** STATE'te ISLER'de olmayan bir kalem durumu; ya da iki yüzeyde farklı statü. |
| Bağımlılıklar | İhtiyaç: T1 (dosya mimarisi, statü sözlüğü, yayılım kontrolü, açılış seti bütçesi), T5 (isteğe bağlı betik). Beslediği: bütün S5 kartları, T5 açılış protokolü, T4 raporları. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "'NOT STARTED' appears in INDEX, STATE, HANDOFF, DECISIONS and the S1 master, and 7 times in WORK." [R11 K49]. Kabul testi: soğuk başlangıç testinde taze oturum sıradaki kalemi tek bir yüzeyden bulur ve yüzeyler çelişmez. |
| Kaynak | A003 §3.6, §5; [R11 K49, K110]; R07 BO-1 (plan kalıcıdır; E-MARS "saving its plan to Memory"); R08 O19 (ekleme-yalnız günlük). |
| Bedel | Aşama başına bir `ISLER.md` (tahmini 15–40 KB; v). `PLAN.md` 8–15 KB (v). Açılış setine yalnız `PLAN.md` §1'in ilgili kartı ve aktif `ISLER.md`'nin açık kalemleri girer (T1). |

#### MK-5.2 İş kalemi şeması ve statü makinesi

| Alan | İçerik |
|---|---|
| Ne | Her iş kaleminin sabit alanlı bloğu ve izinli statü geçişleri. "Hazır" bir statü değildir; MK-5.3'te hesaplanır. |
| Nerede | `phases/<Pn>/ISLER.md` §1; blok şablonu aşağıda. Kimlik biçimi `İK-<aşama>-<üç hane>`. Kimlik yeniden kullanılmaz, numara değişmez. |
| Ne zaman | Kalem yaratılırken (`aday`); her statü değişiminde; kapanışta (MK-3.3 kapanış satırları). |
| Kim | Ana oturum. Geçiş yetkileri MK-5.7'dedir. Alt ajan hiçbir statüyü değiştirmez ve sıradaki kalemi seçmez. |
| Nasıl işler | **Statüler** (T1'in statü sözlüğüyle hizalanır): `aday` (keşfedildi, plana alınmadı) → `kabul` (plana alındı; kim, ne zaman) → `sürüyor` (brief kimliği ve başlangıç HEAD'i yazıldı) → `bitti` (çıktı üretildi; üreticinin beyanı) → `doğrulandı` (kalem kapısı geçti). Yan statüler: `park` (tetik zorunlu) · `düştü` (neden türü zorunlu: reddedildi / yerine kondu:<İK-…> / sonlandırıldı / başarısız) · `yeniden-değerlendir` (bir önkoşul ya da dayandığı karar değişti; sonucu değişmiş sayılmaz). **Geçiş kuralları:** (1) `bitti_tanımı` boşsa `sürüyor`a geçilmez. (2) `sürüyor` → `bitti` yalnız bir dönüş dosyası ya da commit kanıtıyla olur. Zaman aşımı ya da kayıp "bitti" sayılmaz; bu durumda `sürüyor` kalır ve yarım iş işlenir (T5 W5). (3) `bitti` → `doğrulandı` kapı hükmüyle olur. (4) Hiçbir blok silinmez; yerine koyma `düştü:yerine kondu` ile yapılır. (5) Bağlam ya da bütçe bitmesi `park` sayılır, `bitti` sayılmaz. **Biçim notu:** Blok biçimli Markdown seçildi, çünkü Batu ve alt ajan okuyabilir. JSON/YAML kararı bilinmiyor (§5.2 son satır). |
| Zorlama düzeyi | Yapısal: zorunlu alanlar ve geçiş kuralları. Zorlayıcı seçenek T5'te (MK-5.1'deki kimlik denetimi betiği; zorunlu alan denetimi). |
| Çalıştığını nasıl anlarız | Aşama kapısında örneklem denetimi: zorunlu alanlar dolu mu, geçişler kurala uygun mu (`git log -p`)? **Bozulma işaretleri:** kanıtsız `bitti`; nedensiz `düştü`; tetiksiz `park`; silinmiş blok. |
| Bağımlılıklar | İhtiyaç: T1 (statü sözlüğü), T2 (brief kimliği ve sürümü; dönüş durum kodları), T5 (HEAD kaydı ve yarım iş protokolü). Beslediği: MK-5.3, MK-3.3, MK-3.8, T4 ilerleme ölçüsü, T5 süreklilik. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Treating all of these as `cancelled` destroys the reason Work ceased or never began." [R11 K112]; aday işin kabul edilmiş iş sanılması (A003 §3.5: "Aday iş, kabul edilmiş iş değildir"). Kabul testi: Pilot-1'deki kalemler şablonla açılır ve kapanır; soğuk başlangıç testinde taze oturum her kalemin durumunu ve nedenini doğru okur. |
| Kaynak | A003 §3.6 (statüler); R04 (a)1, (a)3; [R11 K110, K112]; R07 BS-4 ("kalemler yalnız durum alanı değiştirilerek güncellenir"); R05 #8 (Spec Kit: "never reordered, renumbered, deleted or rewritten"). |
| Bedel | Kalem başına yaklaşık 15 satır. Batu bu dosyayı okumak zorunda değildir; STATE ve raporlar ona yeter (T4). |

```text
### İK-P2-007 · <kısa başlık>
statü: aday | kabul | sürüyor | bitti | doğrulandı | park(tetik: …) | düştü(<neden türü>) | yeniden-değerlendir(<neden>)
hedef: ürün | yöntem                        kaynak_söz: <U00x / A003 §x / aşama çıkış ölçütü n>
amaç: <hangi karar ya da teslimat; SOUL→DevOS→P2→…>
bitti_tanımı: <işten önce; tek paragraf; sınanabilir>   kabul_testi: <nasıl sınanacak>
kapsam_dışı: <…>                            rota: yoklama | sınırlı | tasarım · rota_gerekçesi: S1..S4 cevapları
sahip_işlev: <T2 eşlemesi>                  köken: <MK-4.4> · neden: amaç | yöntem:<…>
bağlar: önkoşul:<İK-…> · sıra:<İK-…>(gerekçe) · keşfedildiği:<İK-…> · etkilenir:<karar/İK> · katkı:<üst sonuç>
kabul: <tarih, kim> · başlangıç: <tarih, brief ID vN, HEAD kısa> · ilk_ornek: evet/hayır
<kapanış satırları: MK-3.3>
```

#### MK-5.3 Bağımlılık türleri, hazır iş hesabı ve aynı anda açık iş sınırı

| Alan | İçerik |
|---|---|
| Ne | Beş bağımlılık türü, bunlardan yalnız birinin hazırlığı engellediği bir hazır iş (ready frontier) kuralı ve eşzamanlı `sürüyor` kalem sınırı. |
| Nerede | Kalem bloğundaki `bağlar` satırı (MK-5.2); hesaplama kuralı METHOD'da; seçilen sıradaki kalem STATE'te. |
| Ne zaman | Oturum açılışında (yarım iş devralındıktan sonra), her kalem kapanışında, her revizyonda. |
| Kim | Ana oturum. Alt ajan sıradaki işi seçmez. |
| Nasıl işler | **Bağ türleri:** `önkoşul` (zorunlu; önkoşul `doğrulandı` olmadan kalem hazır olamaz) · `sıra` (seçtiğimiz sıra; hazırlığı engellemez; gerekçe ister) · `keşfedildiği` (köken; engellemez) · `etkilenir` (bir karardan etkilenir; karar değişince `yeniden-değerlendir` işareti tetiklenir) · `katkı` (aynı üst sonuca katkı; engellemez). **Hazır kuralı:** Statüsü `kabul` olan bir kalem hazırdır, eğer (a) bütün `önkoşul` bağları `doğrulandı` ise; (b) bağlı açık bir çerçeve sorusu yoksa (MK-4.3); (c) sahip işlevi mevcut ve aşama bütçesinde yer varsa (T5); (d) kalem `yeniden-değerlendir` işareti taşımıyorsa. **Seçim sırası:** 1) yarım kalem (`sürüyor`, sahipsiz); 2) hazır kalemler arasında çıkış ölçütüne doğrudan katkı verenler; 3) `sıra` bağı gerekçeli olanlar; 4) en eski kabul. **Sınır:** Aynı anda en fazla 3 `sürüyor` kalem (v; T5'in paralellik bütçesiyle hizalanır). Yarım bir kalem varken yeni kalem ancak bağımsız ve salt-okuma ise açılır. |
| Zorlama düzeyi | Yapısal (bağ alanları) + tavsiye (seçim sırası). |
| Çalıştığını nasıl anlarız | Oturum açılışında hazır listesi kurala göre yeniden üretilebilir. **Bozulma işaretleri:** hazır listesi boş ama `kabul` kalemleri var (bağ grafiği kırık olabilir; beads: ready listesi "only as correct as the recorded graph" [R05 #6]); sınır aşımı; `sıra` bağının kalemi fiilen beklettiği görülüyor. |
| Bağımlılıklar | İhtiyaç: MK-5.2, MK-4.3, T5 (bütçe, paralellik), T2 (sahip işlevleri). Beslediği: MK-3.3, T4 takılma türleri ("engelli / bekliyor / işçi yok"). |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Calling a work item `open` does not mean it is actionable." (beads FINDINGS §2; g, 27.09.2026); "more work started does not logically entail better end-to-end system progress" [R11 K112]; bağımlılık türleri ayrılmazsa paralel dağıtım yanlış sıralanır [R11 E25]. Kabul testi: Pilot-1'de hazır hesabı elle yapılır ve sonucu ikinci bir okuyucuyla karşılaştırılır. |
| Kaynak | beads FINDINGS §2, §4 (g): "`discovered-from` as provenance … without becoming a prerequisite by default"; A003 §3.6 ("'Seçtiğimiz sıra' ile 'zorunlu önkoşul' ayrı işaretlenir"); EXP-004 L07: "planın sırası ile zorunlu bağımlılık aynı şey değil" (R06); EXP-006 P3-01 §2 (ilişki türleri; aday). |
| Bedel | Kalem başına bir satır; açılışta hesaplama birkaç dakika. |

#### MK-5.4 Dilim boyutlandırma

| Alan | İçerik |
|---|---|
| Ne | Bir kalemin, bitti tanımındaki sonucu tek başına doğru üretebilecek kadar büyük ve tek bir alt ajan dalgasında kapanabilecek kadar küçük tutulması kuralı. |
| Nerede | Kalem kabulünde üç sorulu kontrol; sonuç kalem bloğunda `rota_gerekçesi` yanına tek satır. |
| Ne zaman | `aday` → `kabul` geçişinde; bir kalem soru üreterek kapandığında. |
| Kim | Ana oturum. |
| Nasıl işler | Üç soru: (1) "Bu kalemin çıktısı hangi soruyu kapatıyor ya da hangi kararı mümkün kılıyor?" Cevap yoksa kalem yeniden tanımlanır. (2) "Çıktı, başka bir kalemin sonucu olmadan doğru üretilebilir mi?" Hayırsa `önkoşul` bağı eklenir ya da kalem birleştirilir. (3) "Tek alt ajan dalgası ve tek dönüş dosyasıyla kapanabilir mi?" Hayırsa bölünür. Her parçanın kendi bitti tanımı olur. **Tepki kuralı:** Kapanışında `karar_değişti_mi: hayır` ve yeni açık soru üreten kalemler sayılır. Aynı aşamada bu oran yükselirse dilimleme gözden geçirilir. Eşik: son 5 kalemde 3 (v). |
| Zorlama düzeyi | Tavsiye + yapısal (kabul satırı). |
| Çalıştığını nasıl anlarız | "Soru üreten kalem" oranı aşama raporunda. **Bozulma işareti:** ardışık kalemler Batu'ya teknik soru üretiyor [R11 E24]. |
| Bağımlılıklar | İhtiyaç: MK-5.2, MK-3.6. Beslediği: MK-5.10, T4 takılma tespiti. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Dilim doğru sayı üretemiyorsa soru üretir." ve "Sonraki 16 görevin hepsi … tartışmasıydı ve hiçbiri kod üretmedi." [R11 K30]. Kabul testi: P1'in ilk 10 kaleminde soru üreten kalem oranı raporlanır. |
| Kaynak | [R11 K30]; R01 örnek repolar ekseni (v2 dilim kuralı: "Bir dilim, gösterdiği sayıyı doğru üretebilecek kadar büyük tanımlanır"); R08 O16. |
| Bedel | Kabul başına bir satır. |

#### MK-5.5 Varsayım ve risk kaydı

| Alan | İçerik |
|---|---|
| Ne | Aşamaların ve yük taşıyan kalemlerin dayandığı varsayımların, olgu sınıflarıyla, "çökerse ne olur" ve "nasıl sınanır" alanlarıyla kaydı. Çökme, revizyon tetiğidir. |
| Nerede | Harita düzeyinde `PLAN.md` §3; aşama düzeyinde `ISLER.md` §3. Şablon aşağıda. Operasyonel riskler (VM kaybı, limit) T5'indir; burada yalnız işaretçileri durur. |
| Ne zaman | Aşama açılışında; tasarım rotasındaki kalemin planlama adımında; periyodik yön gözden geçirmesinde (MK-3.4 soru 4); bir olgu değiştiğinde. |
| Kim | Ana oturum yazar. Karşı-okuyucu tasarım kalemlerinde eksik varsayım bildirebilir. |
| Nasıl işler | 1) **Sınıf** (Magentic görev defterinden uyarlandı): `verilen/doğrulanmış olgu` · `bakılacak olgu` · `türetilecek olgu` · `tahmin`. 2) Her varsayıma "dayananlar" yazılır: aşama, kalem, karar. 3) "Çökerse ne olur" ve "nasıl sınanır" alanları doldurulur. 4) **Durum:** `açık` · `doğrulandı` (sınıfı olguya yükselir) · `çöktü` (→ MK-5.6) · `bayat` (son kontrol, geçerlilik süresini aştı). 5) Tahmin sınıfındaki bir varsayım, üzerine ikinci bir karar kurulmadan önce ya sınanır ya da "sınanmadan kullanıldı" diye işaretlenir. |
| Zorlama düzeyi | Yapısal. |
| Çalıştığını nasıl anlarız | Çöken varsayımların hepsi bir revizyon kaydına bağlı. **Bozulma işareti:** bir karar, kayıtta olmayan bir varsayıma dayanıyor. Karşı-okuma bunu "gizli varsayım" bulgusu olarak getirir (T4 S15). |
| Bağımlılıklar | İhtiyaç: T4 (S15 karar-kritik varsayım disiplini), T5 (operasyonel risk kaydı). Beslediği: MK-5.6, MK-3.4, aşama kartları. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: çöken varsayımın plan boyunca taşınması [R11 S5; E73 ile ilişkili]. Kabul testi: W7 yürüyüşü (§9) bu kayıttan başlar ve çöküşü etkilenen kalemlere kadar izler. |
| Kaynak | A003 §3.7 ("her aşama dayandığı varsayımları listeler"); R08 §2.11 (Magentic: "GIVEN OR VERIFIED FACTS / FACTS TO LOOK UP / FACTS TO DERIVE / EDUCATED GUESSES"; kd, kaynak kod); [R11 K110]. |
| Bedel | Aşama başına 3–8 satır. |

```text
| ID | Varsayım | Sınıf | Dayananlar | Çökerse | Nasıl sınanır | Durum | Son kontrol |
| V-P1-2 | Alt ajan derinliği 1 ortam tarafından sabit | bakılacak olgu | P1 topoloji tablosu; P4 seçimi | Rol-rol doğrudan istek tasarımı açılır | P1 deneme: derinlik değişkeni | açık | 27.09.2026 |
```

#### MK-5.6 Revizyon protokolü

| Alan | İçerik |
|---|---|
| Ne | Plan değiştiğinde izlenen sabit sekiz adım. Önce neyin değiştiği sınıflanır; kayıt ekleme-yalnızdır; değişiklik bağlı kayıtlara yayılır. |
| Nerede | `PLAN.md` §4 Değişiklik kaydı (`DEĞ-<n>`); etkilenen kalem ve varsayım blokları; sapma varsa MK-5.8. |
| Ne zaman | **Tetikler:** (a) varsayım çöktü (MK-5.5); (b) karşı-okuma geri dönmeyi gerektiren bir açık buldu; (c) Batu yeni bir yön, itiraz ya da karar verdi; (d) iş beklenenden büyük ya da küçük çıktı; (e) takılma (MK-5.10); (f) çerçeve yetersiz bulundu (MK-4.6); (g) P1 kanıtı bir kabiliyet varsayımını çürüttü; (h) dayanılan bir kaynak ya da karar geri çekildi. |
| Kim | Ana oturum yürütür. Karar, MK-5.7'deki yetki sahibinindir. |
| Nasıl işler | **1) Sınıfla: ne değişti?** Dört seçenek: işin *yürütülüşü* · *yöntem* · *başarı anlayışımız* (bizim yorumumuz) · *Batu'nun amacı*. Kaynak: EXP-004 DQ03, "SOUL'un kendi iş anlayışını değiştirebilmesi, kullanıcının amacını kendi başına değiştirmesi değildir" (R06; ana oturum doğruladı). Ayrıca iki durum ayrılır: **düzeltme** ("Batu'yu yanlış anlamıştık"; eski kaydın düzeltilmesi, aynı zamana aittir) ve **dünyadaki değişiklik** ("Batu kararını değiştirdi"; bir tarihten itibaren geçerli). Kaynak: R10 §4.2. **2) Yetki:** MK-5.7'den bak. Yetki Batu'daysa öneri yazılır, cevap beklenirken bağımsız işler sürer. **3) Katman:** Hata ait olduğu katmanda düzeltilir: amaç → harita/METHOD → aşama tasarımı → kalem. Aşağıda yamalanmaz [R08 O14]. **4) Taban kontrolü:** Öneri hangi SHA'ya göre hazırlandı? Araya giren değişiklik varsa öneri yeni tabana göre yeniden değerlendirilir (R10 §4.2, M2 §4). **5) Kayıt:** `DEĞ` satırı eklenir; eski satır değiştirilmez. **6) Yayılım:** `etkilenir` bağlı kalemler `yeniden-değerlendir` olur. Türetilmiş kopyalar (STATE, devir notu, rol belleği) T1'in yayılım kontrolüyle taranır. Çalışan alt ajanlar T2'nin kuralıyla bilgilendirilir ya da geç sonuçları eski sürüme göre uzlaştırılır (W6). **7) Sapma:** Kabul edilmiş sürümden sapıyorsa `SAP` kaydı açılır (MK-5.8). **8) Bildirim:** Batu'nun yetkisindeyse öneri olarak (T4 biçimi), Claude'un yetkisindeyse aşama raporunda. |
| Zorlama düzeyi | Yapısal: `DEĞ` şablonu, zorunlu sınıflama ve yetki alanları. |
| Çalıştığını nasıl anlarız | Her `DEĞ` satırında sınıf, yetki ve yayılım alanı dolu. **Bozulma işaretleri:** değişiklik kaydında olmayan bir plan farkı (`git diff PLAN.md` ile yakalanır); "Batu'nun amacı" sınıfında olup Batu kararı bulunmayan bir `DEĞ`; yayılım alanı boş bir karar değişikliği (K-010'un çalışan R10 ajanına ulaşmaması bu türdendi; ORTAK-SENTEZ "Karar yayılmadı"). |
| Bağımlılıklar | İhtiyaç: MK-5.7, MK-5.8, T1 (yayılım kontrolü, düzeltme ve yerine koyma kuralları), T2 (çalışan ajanlara karar yayılımı), T4 (öneri biçimi). Beslediği: W6, W7, W8; T5 öğrenme. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "A bad plan can appear to have been 'correct' because it is revised after implementation." [R11 K100]; çerçeve değişikliği kontrolü yoksa plan bir önceki turun seçimiyle kayar [R11 E03]. Kabul testi: W6 ve W7 yürüyüşleri (§9) bu protokolle baştan sona izlenir; P0 pilotlarında en az bir `DEĞ` kaydı yazılır. |
| Kaynak | A003 §3.7 (tetikler, sınıflama, kayıt, sınırlar); R06 (DQ03); R10 §4.2; [R11 K46, K100, K111]; R08 O14 (BMAD "goes back to that layer and regenerates from there"). |
| Bedel | Revizyon başına bir kayıt satırı ve bir yayılım taraması. |

```text
DEĞ-012 · 2026-10-03 · taban SHA <kısa> · tetik: (c) Batu U0xx
ne değişti: yürütme | yöntem | başarı anlayışı | Batu'nun amacı · tür: düzeltme | dünyadaki değişiklik (geçerlilik: <tarihten itibaren>)
değişiklik: <eski> → <yeni> · katman: amaç | harita | aşama tasarımı | kalem
karar veren: ana oturum | Batu (mesaj: U0xx) | öneri—Batu'nun cevabı bekleniyor (AS-…)
reddedilen seçenekler: <…> · yayılım: yeniden-değerlendir → İK-…; T1 taraması <tarih>; çalışan ajanlar <brief ID: bildirildi/uzlaştırılacak>
sapma: SAP-… | yok
```

#### MK-5.7 Revizyon yetkisi tablosu

| Alan | İçerik |
|---|---|
| Ne | Plan üzerindeki her değişiklik hakkının kime ait olduğunu açıkça atayan tablo. Foundation bu hakların sahibini bilerek açık bırakıyor: "does not establish … who may select, commit, reprioritise, waive, accept, terminate or reactivate Work" (R04 (a)4; kd). |
| Nerede | METHOD'un yetki bölümü (T4'ün karar hakları tablosuyla tek tabloda birleşir); tablo aşağıda. Her `DEĞ` satırının "karar veren" alanı bu tabloya uyar. |
| Ne zaman | Her statü değişiminde ve revizyonda başvurulur. |
| Kim | Tabloyu Batu onaylar (A003 §3.7'deki dağılımın ayrıntılı hali). |
| Nasıl işler | Tablo aşağıda. Belirsiz bir durumda dar yorum uygulanır: hak Batu'ya aitmiş gibi davranılır ve soru olarak kaydedilir; iş durmaz. |
| Zorlama düzeyi | Tavsiye + yapısal ("karar veren" alanı). Zorlayıcı değil. |
| Çalıştığını nasıl anlarız | Kapı denetiminde `DEĞ` ve statü geçişlerinin "karar veren" alanı tabloyla çelişmez. **Bozulma işareti:** Batu hakkı olan bir değişikliğin Batu mesajı olmadan yapılmış olması (E75'in türü: öz-onay kapanışı hızlandırır, kapanış da yetki sınırını zorlar [R11 K111, K47]). |
| Bağımlılıklar | İhtiyaç: T4 (S1 karar katmanları, sürekli yetki kaydı). Beslediği: MK-5.2, MK-5.6, MK-3.5. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: ya her şey Batu'ya gider ya da Claude Batu adına amaç değiştirir [R11 S1]; "Discovering a missing decision is not permission to make it on the owner's behalf." (R04 (a)2; ana oturum doğruladı). Kabul testi: W6, W7, W8 yürüyüşlerinde her adımın yetki sahibi tablodan tek anlamlı okunur. |
| Kaynak | A003 §3.6–§3.7; R04 (a)2, (a)4; R05 #22 (gstack: "Mechanical — auto-decide; Taste — auto-decide, record, surface at final gate"; "User Challenge … never auto-decided"); R08 §2.1 (BMAD: gözetimsiz işçi sıradaki işi seçmez). |
| Bedel | Tek seferlik tablo; Batu'dan bir onay. |

| # | Hak | Ana oturum | Batu | Not |
|---|---|---|---|---|
| 1 | Aday kalem eklemek | evet | — | Alt ajanlar yalnız dönüşte önerir |
| 2 | Kalemi kabul etmek (plana almak) | evet, aşama kapsamı içinde | kapsam dışına çıkıyorsa | Kapsam sorusu biriktirilmez |
| 3 | Öncelik ya da sırayı değiştirmek | evet, gerekçeyle (`sıra` bağı) | — | |
| 4 | Kalemden vazgeçmek (kapsam dışı bırakmak) | çıkış ölçütünü etkilemiyorsa | etkiliyorsa | |
| 5 | Kalemi sonlandırmak (`düştü`) | evet, neden türüyle | — | Reddedilen seçenek korunur |
| 6 | Kalemi kapatmak (`doğrulandı`) | evet, rotanın kontrol hükmüyle | — | Alt ajan kapatamaz |
| 7 | Aşama çıkış kapısı | kendiliğinden aşamalarda (K-002) | durak aşamalarında | §2.4 |
| 8 | Çıkış ölçütünü sıkılaştırmak | evet, `DEĞ` ile | — | |
| 9 | Çıkış ölçütünü gevşetmek ya da çıkarmak | — | evet | "Kötü sonucu iyi göstermek için ölçüt değiştirilmez" (A003 §3.7) |
| 10 | Planda öngörülen hedefli geri dönüş | evet; aşama raporunda bildirilir | — | MK-5.9 |
| 11 | Harita değişikliği (aşama ekleme, çıkarma, sıra, geçiş türü) | öneri | evet | |
| 12 | Amaç, kapsam ya da Batu'nun kabul ölçütünü değiştirmek | öneri; beklerken bağımsız işe devam | evet | Çerçeve sorusu (MK-4.3) |
| 13 | Kapanmış kalemi ya da kararı yeniden açmak | evet, adı konmuş gerekçe ve en küçük kapsamla | Batu'nun kabul ettiği bir çıktıysa bildirim; kapsamı etkiliyorsa karar | MK-5.9 |
| 14 | Kendi yanlış iddiasını geri çekmek | evet, onay beklemeden; yayılım kontrolüyle | — | A003 §3.7 |

Not: METHOD ya da yapılandırma değişikliği bu tablonun değil, T5'in yöntem değişikliği kontrolünün (S21) konusudur. A-04 kapsamındakiler Batu'ya gider.

#### MK-5.8 Kabul edilmiş plan sürümü ve sapma kaydı

| Alan | İçerik |
|---|---|
| Ne | Batu'nun kabul ettiği plan (harita, METHOD, aşama kartı) sürümünün SHA'ya bağlı işareti ve bu sürümden her sapmanın ayrı kaydı. |
| Nerede | `PLAN.md` §2 (kabul işaretleri) ve §4 içinde `SAP-<n>` satırları. |
| Ne zaman | Batu bir plan sürümünü kabul ettiğinde; kabul edilmiş sürümden sapan her revizyonda; her kapıda (sapma listesi). |
| Kim | Ana oturum yazar. Kabul Batu'nundur. |
| Nasıl işler | 1) Kabul işareti yazılır: `KABUL-<konu>-v<n>`: SHA, Batu'nun mesajı (birebir kaynak yolu), kapsam. 2) Kabul edilmiş metin yeniden yazılmaz. Git'te SHA ile durur; güncel metin değişebilir, ama kabul işareti eski SHA'yı gösterir. 3) Her fark `SAP` satırıdır: kabul edilen, fiili, neden, sınıf (MK-5.6 adım 1), karar veren, etki. 4) Kapı kaydı ve Batu raporu sapma listesini gösterir. 5) Yeni sürüm kabul edilince yeni işaret eklenir, eskisi silinmez. |
| Zorlama düzeyi | Yapısal. |
| Çalıştığını nasıl anlarız | `git diff <kabul SHA> HEAD -- PLAN.md` ile çıkan her maddi farkın bir `SAP` ya da `DEĞ` satırı var. **Bozulma işareti:** raporlarda "plan hep bunu diyordu" türü ifade; kabul SHA'sından sonraki bir farkın kayıtsız olması. |
| Bağımlılıklar | İhtiyaç: T4 (kabul paketi, kabulün SHA'ya bağlanması), MK-5.6. Beslediği: MK-3.5, T4 raporları, T5 retro. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: sapma kaydı yoksa kötü plan sonradan hep doğruymuş görünür [R11 E26, K100]. Kabul testi: P0 çıkışında ilk işaret (`KABUL-METHOD-v1`) yazılır; P1'in ilk kapısında `git diff` denetimi yapılır. |
| Kaynak | A003 §3.7: "Kabul ettiğin plan sürümü korunur. Sapmalar ayrı yazılır ki plan sonradan hep doğruymuş gibi görünmesin."; R05 #9 (PB F4; WM 08 §7); R08 O19 (ADR "superseded"). |
| Bedel | Kabul başına bir satır; sapma başına bir satır. |

#### MK-5.9 Park, düşürme ve yeniden açma kuralı

| Alan | İçerik |
|---|---|
| Ne | Bekleyen işin unutulmadığı, kapanan işin keyfî açılmadığı üç kural. |
| Nerede | Kalem bloğundaki statü ve tetik alanları; kapı kaydındaki "park edilenler" listesi. |
| Ne zaman | Kalem beklemeye alınırken, düşürülürken ya da yeniden açılırken; her kapıda park listesi gözden geçirilir. |
| Kim | Ana oturum; Batu'nun kabul ettiği bir çıktının yeniden açılması MK-5.7 satır 13'e tabidir. |
| Nasıl işler | **Park:** Yeniden bakma tetiği zorunludur: bir olay ("P1 denemesi D-3 sonuçlanınca"), kalem sayısı ya da kapı. Tetiği gerçekleşen kalem hazır hesabına döner. Bağlam ya da bütçe bitmesi, eleştiri turu sınırına (üç tur; A003 §3.7) ulaşmak ve Batu cevabı beklemek park nedenidir; "bitti" değildir. **Düşürme:** Neden türü zorunlu (MK-5.2). Reddedilen seçenek, özetlerden geri sızmasın diye gerekçesiyle korunur (T1 S10). **Yeniden açma:** (a) adı konmuş, başarısız olmuş bir iddia ya da kaybolmuş bir ayrım gerekir; (b) en küçük kapsam: yalnız etkilenen kalem ya da bölüm; (c) bağımlılık değiştiyse önce `yeniden-değerlendir` yapılır. Bu işaret sonucun geçersiz olduğu anlamına gelmez. (d) Yeni bir oturum açmak tek başına yeniden açma nedeni değildir. |
| Zorlama düzeyi | Yapısal (tetik ve gerekçe alanları). |
| Çalıştığını nasıl anlarız | Kapı kaydında park listesi ve tetik durumları. **Bozulma işaretleri:** tetiği gerçekleştiği halde hazır hesabına dönmemiş park kalemi; gerekçesiz yeniden açma; aynı kalemin ikiden fazla yeniden açılması (eleştiri döngüsü). |
| Bağımlılıklar | İhtiyaç: MK-5.2, MK-5.3, MK-5.7; T4 (bulgu akıbeti, eleştiri turu sınırı). Beslediği: MK-3.5, T4 raporları. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: sessiz kayıp ya da sonsuz yeniden açma; park edilen bulguların görünmez birikmesi (R11 §5 Y8'in dengeleyicisi: park kaydı, yükseltme yolu, kapanışta açık bulgular listesi). Kabul testi: her kapıda park listesi okunur ve tetiği geçenler işlenmiş görünür. |
| Kaynak | R04 (a)5: "A useful reopening request names the failed claim or lost distinction … It may invalidate only one leaf." ve "dependency changed → standing may require re-evaluation != standing necessarily changed"; R06 (T11): "Beklemede olmak unutulmak veya sessizce silinmek değildir."; A003 §3.7. |
| Bedel | Düşük. |

#### MK-5.10 Takılmaya plan tepkisi ve yeniden planlama

| Alan | İçerik |
|---|---|
| Ne | T4'ün takılma alarmı ya da periyodik yön gözden geçirmesi bir takılma gösterdiğinde, takılmanın türüne göre plan tepkisi. Aynı brief değiştirilmeden tekrar gönderilmez. Aynı kalemde üç başarısız denemede devre kesilir. |
| Nerede | `ISLER.md` içinde `TAK-<n>` kayıtları (şablon aşağıda); ilgili kalem bloklarına işaretçi. |
| Ne zaman | T4'ün alarmı ateşlendiğinde; bir kalemin ikinci başarısız denemesinde; yön gözden geçirmesinde "son 5 kalemde karar değişmedi" çıktığında. |
| Kim | Ana oturum. Tespit ve eşikler T4'ündür (S17). |
| Nasıl işler | **Türe göre tepki** (türler: R05 #24, gastown): **engelli** (önkoşul doğrulanmadı) → önkoşul kalemine odaklan, onun bağlarını incele. **bekliyor** (Batu cevabı ya da dış olay) → etkilenen kalemleri park et, bağımsız hazır işe geç (K-002: "iş durmasın"). **işçi yok** (sahip işlev tanımsız) → T2'ye rol ihtiyacı; geçici olarak ana oturum görevi yapılır. **işçi kayıp** (VM geri alındı, dönüş yok) → T5'in yarım iş protokolü; aynı brief'le yeniden. **hareket var, ilerleme yok** → yeniden plan: kök neden yazılır ("what went wrong … avoid repeating the same mistakes"; Magentic), dilim yeniden boyutlandırılır (MK-5.4), çerçeve sınanır (MK-4.6), aşama raporunda ilk satır olur. **Devre kesici:** Aynı kalemde üç başarısız deneme (her biri değiştirilmiş brief'le) → kalem `park`, Batu'ya raporda satır. |
| Zorlama düzeyi | Tavsiye + yapısal (`TAK` şablonu). Tespitin zorlayıcı kısmı T4/T5'tedir. |
| Çalıştığını nasıl anlarız | Her alarmı bir `TAK` kaydı ve sınıflanmış bir tepki izliyor. **Bozulma işaretleri:** aynı brief'in değiştirilmeden tekrar gönderilmesi (T2 brief sürümüyle görünür); bir alarmın tepkisiz kalması; `TAK` sonrasında aynı türün aynı kalemde tekrarı. |
| Bağımlılıklar | İhtiyaç: T4 (ilerleme ölçüsü, takılma türleri, alarm), T5 (yarım iş, uyandırma), T2 (brief sürümü). Beslediği: MK-5.6, MK-3.8. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Bekçi 742 kez koştu ama '54 gündür kod yok' demedi." [R11 K25]; kör tekrar ve dönüp duran ajan (R08 O17; 12-Factor "your agent will start to spin out"). Kabul testi: W9 yürüyüşü (§9); pilotlarda yapay bir "hareket var, ilerleme yok" durumu (üç kalem art arda karar değiştirmiyor) tepki üretiyor mu? |
| Kaynak | R08 §2.11 (Magentic: `max_stalls` = 3, "re-planning with the outer loop"); R05 #4 ("forbids unchanged retries"), #24 ("circuit-broken" after 3 failures); A003 §3.6 ("hareket var, ilerleme yok" alarmı). |
| Bedel | Alarm başına bir kayıt ve kısa bir yeniden plan işi. |

```text
TAK-003 · <tarih> · tür: engelli | bekliyor | işçi yok | işçi kayıp | hareket var, ilerleme yok
kanıt: <T4 ölçüsü / son 5 kalemin karar_değişti_mi satırları>
kök neden: <…> · tepki: <park İK-… / yeniden dilim → İK-… / brief vN→vN+1 / DEĞ-… / Batu raporu>
deneme sayacı (kalem): 1 | 2 | 3 → devre kesildi
```

## 6. S6 — Araştırma birikiminden yararlanma

### 6.1 Amaç
Foundation, studies, explorations ve dış kaynakları doğru anda, doğru derinlikte ve doğru sırayla kullanmak. Kullanımın kararı nasıl değiştirdiğini izlenebilir kılmak. Batu'nun sözü: "araştırmalar senin kullanman için yapıldı" (R03 ilke 3). Sırası da onun: önce Foundation bakışı genişletir, sonra "foundation'u okuyarak bakış açını genişlettiğin halinle" studies okunur (EXP-006 U002-A; kd, Batu'nun sözü; g, 27.09.2026). Eleştirisi: "neden bu kadar bilgiyi sana ben araştırtmak zorundayım?" (R03). S6 zayıfsa keşif beslenmez (S4), tasarım "yalnız akıl yürütme"ye kalır (S15), iddialar kaynaksız doğrulanır (S14) [R11 S6].

**AGENT.md R09 ile uyum** (A-01 varsayımına göre kontrol katmanı kalıyor): S6, `agent/protocols/candidate-research-library.md`'nin geri çağırma yolunu (CATALOG → META → STATE/INDEX → bulgu) ve epistemik statü kuralını ("Bunların hiçbiri tek başına `adopted` anlamına gelmez") aynen kullanır. Protokolün aynı yerdeki hafiflik kuralını da korur: "her yanıtta ayrı rapor veya her dosya için katkı kaydı zorunlu değildir." Bu yüzden okuma kaydı ve araştırma izi yalnız karar taşıyan kullanımlarda tutulur (g, 27.09.2026; veri olarak okundu). Alt ajanlar rota kapısını kendiliğinden koşmaz [R11 K78]. Bu disiplin onlara brief'in "okuma rotası" alanıyla (MK-6.2) ve rol tanımıyla (T2) taşınır.

### 6.2 Bileşenler ve karar tablosu

| Bileşen | Karar | Önlediği hata | Kabul testi | Kart | Kaynak |
|---|---|---|---|---|---|
| Başvuru tetikleri | gerekli | Birikim var ama kullanılmaz; araştırma rastlantıya kalır | Her aşama kapısında "bu aşamanın kararlarına hangi araştırma bakıldı" boşluk kontrolü yapılmış | MK-6.1 | A003 §3.5 [R11 K110]; E27 |
| Sıra: Foundation (mercek) → studies (örnekler); ihtiyaç ve işlev adıyla arama | gerekli | Örneklere dar bakışla gidilir; katalog kaçırmaları "yok" sanılır | Brief'lerin okuma rotası alanında Foundation girişi studies'ten önce; arama terimleri ihtiyaç ve işlev içeriyor | MK-6.2 | U002-A; REUSE (g); R09 protokolü §4 (g) |
| Okuma kaydı (yalnız karar taşıyan okumalar) | gerekli | Kesik araç çıktısı "tam" etiketi alır [K51]; tekrar okuma | Karar taşıyan her okumada satır var; "neyi değiştirdi" alanı boş değil | MK-6.3 | [R11 K51]; A003 §3.4; R11 §5 Y14 |
| Araştırma izi (karar başına) | gerekli | Tasarım gerekçesiz kalır; araştırmanın kullanıldığı görünmez | Her tasarım kararında iz ya da "yalnız akıl yürütme" işareti var | MK-6.4 | A003 §3.5; REUSE "A minimal use record" (g); [K43] |
| Birlikte okuma (bölünmüş kaynaklarda) | gerekli, koşullu | Her parça okunur ama ilişki kaybolur | Kaynaklar arası yük taşıyan her iddia için birlikte okuma kalemi ya da gerekçeli muafiyet | MK-6.5 | [R11 K56]; A003 §3.4 |
| Tazelik ve yeniden doğrulama | gerekli | "Üç kat iç içe" yanılgısı [K91] | Yük taşıyan Claude Code iddialarının hepsinde erişim tarihi ve cloud etiketi; 30 günü aşanlar yeniden doğrulanmış (v) | MK-6.6 | [R11 K91, K71]; R09 protokolü §6 (g) |
| Kanıt gücü ve epistemik rol etiketi | gerekli | Aynı kaynaktan türeyen kopyalar bağımsız kanıt sanılır [K45]; aday çalışma benimsenmiş mimari sanılır | Karar izlerinde kanıt türü ve rol etiketi var | MK-6.7 | [R11 K45]; R09 protokolü §7 (g) |
| Durma ölçütü | gerekli | Sonsuz okuma ya da sahte kapanış; "bütçe bitti = bitti" | Her ek okuma kaleminde "hangi olası sonuç hangi kararı değiştirir" satırı | MK-6.8 | A003 §3.3 madde 9; [K83] |
| "Şu alana bakılmalı" bildirimi (alt ajanın kaynak boşluğu) | gerekli | Keşif, koordinatörün kaynak seçimiyle sınırlanır (Y15) | Dönüş şemasında alan var; her bildirimin akıbeti yazılı | MK-6.9 | A003 §3.5; R11 §5 Y15 |

### 6.3 Mekanizma kartları

#### MK-6.1 Başvuru tetikleri

| Alan | İçerik |
|---|---|
| Ne | Araştırmaya başvurmayı rastlantıdan çıkaran dokuz tetik. Her tetik için ne okunacağı ve çıktının nereye gideceği sabittir. |
| Nerede | METHOD'un S6 bölümü (tablo aşağıda). Tetiği ateşleyen kalemin bloğunda `tetik: T-n` alanı. |
| Ne zaman | Tabloda. |
| Kim | Ana oturum tetiği fark eder ve okuma kalemini açar. Okumayı alt ajan yapar (T2: okuyucu işlevi). Tetik 8'i alt ajan ateşler. |
| Nasıl işler | Tetik ateşlenince bir okuma kalemi açılır. Rota yoklama ya da sınırlı iştir (MK-3.6). Okuma rotası MK-6.2'den, durma ölçütü MK-6.8'den alınır. Sonuç araştırma izine (MK-6.4) ya da açık soru kaydına (MK-4.3) gider. |
| Zorlama düzeyi | Tavsiye + yapısal (kapıdaki boşluk kontrolü, tetik 9). |
| Çalıştığını nasıl anlarız | Tetik 9'un boşluk kontrolü: aşamanın tasarım kararlarının yüzde kaçında bir araştırma izi var? **Bozulma işareti:** bir tasarım seçimi, ilgili bir study ya da Foundation bulgusu olduğu halde "yalnız akıl yürütme" ile verilmiş. Bunu genelde Batu ya da karşı-okuma bulur. |
| Bağımlılıklar | İhtiyaç: MK-6.2, MK-6.8; T2 okuyucu rolü. Beslediği: MK-4.1, MK-4.2, MK-6.4, T4 S15. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: "Birikim uygulanmazsa keşif ilk göze çarpan görüşe çapalanır" [R11 E27, K41]. Kabul testi: Pilot-2 tetik 1 ile başlar; aşama kapısında boşluk kontrolü raporlanır. |
| Kaynak | A003 §3.5 "Hangi anlarda" (tetik 1–6); R03 §5 madde 5; R10 §7 satır 5 ("Dersler, bellek ve kapanış için yok; kapanışta 'bu karara hangi bulgu bakıldı' satırı yok" → tetik 9). |
| Bedel | Tetik başına bir okuma kalemi; bütçe aşama bütçesinden (T5). |

| # | Tetik | Ne okunur | Çıktı |
|---|---|---|---|
| 1 | Aşama açılışı: soruyu genişletme | REUSE soru-ilk tablosunun ilgili satırları → ilgili zemin INDEX'i ve sentez bölümü | Keşif turu (MK-4.1) ve bakış açısı taraması (MK-4.2) girdisi: yeni ayrımlar ve sorular; yoksa "yok" |
| 2 | Bir tasarım seçimi belirdi | CATALOG → ilgili META → STATE/INDEX → bulgu (ve gerekiyorsa kaynak) | Seçenekler, karşı örnekler, "yapmama" nedenleri → araştırma izi |
| 3 | Bir mekanizma icat edilmek üzere | Aynı rota: "Başkası bunu nasıl yaptı, nerede battı, neden yapmadı?" | Mekanizma kartının "Kaynak" alanı; icat gerekiyorsa gerekçesi |
| 4 | Sürpriz, çelişki ya da karşı-okuyucu itirazı | İlgili kaynakların özgün bölümleri; gerekiyorsa birlikte okuma (MK-6.5) | Çelişki hizalaması; revizyon (MK-5.6) ya da ret gerekçesi |
| 5 | Bir terim iki anlama kaymaya başladı | Terim sözlüğü (T1 S10); `concepts/` (varsa ilgili dosya); kaynaktaki kullanım | Sözlük güncellemesi ya da Batu'nun kelimesine dönüş |
| 6 | Claude Code hakkında yük taşıyan bir iddia | Güncel resmî belge (code.claude.com) + erişim tarihi + cloud etiketi; yük taşıyorsa canlı deneme (P1) | Kabiliyet haritası satırı (T5 S19); tazelik alanı (MK-6.6) |
| 7 | Batu'nun yeni yönü ya da itirazı | Foundation ya da studies'te karşılığı var mı; önceki kararların araştırma izi | Revizyon sınıflaması (MK-5.6) için girdi; kanıt dışı etkiye direnç (T4 S15) |
| 8 | Alt ajanın "şu alana bakılmalı" bildirimi | Bildirilen alan | Açık soru ya da yeni okuma kalemi ya da gerekçeli ret (MK-6.9) |
| 9 | Aşama kapısı: araştırma boşluk kontrolü | Aşamanın karar kayıtları ve araştırma izleri | "İzsiz karar" listesi → ya iz eklenir ya "yalnız akıl yürütme" bilinçli olarak onaylanır |

#### MK-6.2 Okuma sırası ve rotası

| Alan | İçerik |
|---|---|
| Ne | Foundation → studies → explorations → dış kaynak sırası ve her birinin giriş kapısı. Arama terim adıyla değil, ihtiyaç, işlev, kısıt ve olası hata adıyla yapılır. |
| Nerede | Brief şablonundaki `okuma_rotası` alanı (T2'nin şablonuna eklenecek alan; örnek aşağıda). Aşama README'sindeki keşif turu kaydında "kaynak alanı" satırı. |
| Ne zaman | Her okuma kalemi ve her keşif turu. |
| Kim | Ana oturum rotayı yazar. Alt ajan rotayı izler ve sapmayı bildirir (A003 §3.3 madde 5: "Başka bir şey okursa bildirir"). |
| Nasıl işler | 1) **Foundation önce:** `research/soul-foundations/STATE.md` → `08_…/REUSE.md` "Question-first entry" tablosunun ilgili satırı → satırın gösterdiği INDEX ve sentez bölümü. Çıktı yeni ayrımlar ve sorulardır; Foundation reçete değildir ("A Foundation result may supply a necessary distinction … It need not become a field, service, prompt or agent."; REUSE; g). 2) **Sonra studies, o mercekle:** `research/studies/CATALOG.md` → yalnız ilgili adayların `META.md`'si → gerekiyorsa `STATE.md`/`INDEX.md` → bulgu → yük taşıyan dış olgu için güncel kaynak. İlgisiz paketler bağlama yüklenmez. 3) **Explorations:** geçici modeller olarak okunur; "A useful example can inspire a candidate without becoming verified evidence" (REUSE). 4) **Dış kaynak:** özellikle Claude Code için resmî belge (MK-6.6). 5) **Arama kuralı:** ihtiyaç, işlev, kısıt ve olası hata terimleriyle ara; "Retrieval miss study absence değildir" (R09 protokolü §4). 6) **Çoklu kaynak:** kararı taşıyan ayrıntıda özet yetmez, özgün bölüme inilir (A003 §3.4). |
| Zorlama düzeyi | Yapısal: brief alanı. |
| Çalıştığını nasıl anlarız | Okuma kayıtlarında Foundation girişlerinin studies'ten önce geldiği görülür. **Bozulma işaretleri:** studies'e Foundation merceği olmadan gidilmiş bir tasarım kalemi; "katalogda yok" denip ihtiyaç adıyla ikinci arama yapılmamış. |
| Bağımlılıklar | İhtiyaç: T2 (brief şablonu), T1 (bağlam paketi: yol ile birlikte ilgili pasaj; "pointer ≠ content" [R11 K84]). Beslediği: MK-6.3, MK-4.1, MK-4.2. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: örneklere dar bakışla gidilmesi [R11 S6]; Batu'nun "niye sadece EXP-004'e gönderiyorsun?" eleştirisi [K40]. Kabul testi: Pilot-2 bu rotayla yürür; rota sapmaları dönüşte bildirilir. |
| Kaynak | EXP-006 U002-A (Batu'nun sözü, g); REUSE (g); `agent/protocols/candidate-research-library.md` §4 (g, veri); A003 §3.4–§3.5; [R11 K82]. |
| Bedel | Brief başına birkaç satır. |

```text
okuma_rotası:
  foundation: REUSE satırı "Which information is sufficient and is it available to this consumer?" → Selection INDEX → U5/E5; 07 SYNTHESIS I1–I5 §2
  studies: CATALOG'da ara: "context handoff", "brief", "scoped context" → superpowers META → syntheses/S03 §3 · work-management-project-control META → 08 §5
  dış: yok | code.claude.com/docs/en/sub-agents.md (erişim tarihi yazılacak)
  bilerek dışarıda: hermes-agent (bu soruya katkısı META'da düşük; gerekirse tetik 4)
  sapma kuralı: rota dışı okuma dönüşte "okunan ek kaynak + neden" olarak bildirilir
```

#### MK-6.3 Okuma kaydı

| Alan | İçerik |
|---|---|
| Ne | Karar taşıyan her okumanın kaydı: hangi kaynak, hangi sürüm, ne kadarı okundu, hangi soru için, düşüncede neyi değiştirdi. |
| Nerede | `phases/<Pn>/OKUMA.md`, ekleme-yalnız (öneri; yeri T1 seçer, A003 §5'teki kök `READING-LOG.md` önerisinin aşama başına bölünmüş hali). Alt ajan dönüşleri okuma kapsamını zaten taşır (T2 dönüş şeması). Ana oturum yalnız karar taşıyanları buraya aktarır. |
| Ne zaman | Bir okuma, bir karara ya da kaleme dayanak olacağı anda. Göz atma kaydedilmez. |
| Kim | Ana oturum yazar (tek yazıcı). Satırın içeriği alt ajan dönüşündendir. |
| Nasıl işler | Alanlar aşağıda. "Neyi değiştirdi" zorunludur ve değerleri sabittir: `destekledi` / `değiştirdi` / `seçenek ekledi` / `seçenek eledi` / `değiştirmedi`. Kapsam değerleri: `tam` / `kısmi (bölümler)` / `okunmadı` / `erişilemedi`. Araç çıktısı kesildiyse "tam" yazılmaz (EXP-006 S1-16 dersi). |
| Zorlama düzeyi | Yapısal: zorunlu alanlar. |
| Çalıştığını nasıl anlarız | Rastgele bir kararın dayandığı okuma satırı bulunur ve kaynağın o sürümünde iddia edilen bölüm gerçekten vardır. **Bozulma işaretleri:** "tam" etiketi olup araç çıktısı kesilmiş okuma; "değiştirmedi" oranı çok yüksek (okuma kararı beslemiyor → durma ölçütü uygulanmıyor olabilir). |
| Bağımlılıklar | İhtiyaç: T2 (dönüş şemasında okuma kapsamı alanı), T1 (sürüm bağlama kuralı, dosya yeri). Beslediği: MK-6.4, MK-6.8, T4 (kaynak kontrolü), T1 (tekrar okumanın önlenmesi). |
| Standart seviye kararı | **Gerekli, daraltılmış kapsamla.** Önlediği hata: "S1-16 §8 labelled five sources 'Tam' although the bulk tool output had been cut off." [R11 K51]. **Dengeleyici** [R11 §5 Y14]: kayıt yalnız karar taşıyan okumada tutulur; kayıt anlamanın kanıtı sayılmaz ("Okuma izi süreç kanıtıdır; anlama … için otomatik oracle değildir" [K56]). Kabul testi: P0 pilotlarında okuma kaydının bedeli (satır ve dakika) ve kararlara bağlanma oranı ölçülür. |
| Kaynak | A003 §3.4 (alanlar); R09 §7 ("okuma kaydının alanları … olgun örneklerle aynı ya da onlardan daha açık"); R07 §8 soru 8 (Anthropic kaynaklarında karşılığı yok; değeri ölçülmedi). |
| Bedel | Karar taşıyan okuma başına bir satır. |

```text
| Tarih | Okuyan (brief ID vN) | Kaynak (yol#bölüm) | Sürüm (SHA/blob) | Kapsam | Soru / kalem | Neyi değiştirdi | Not |
| 2026-10-02 | B-P1-004 v2 | code.claude.com/docs/en/sub-agents.md#… | erişim 02.10.2026 | kısmi (§Scope, §Nesting) | İK-P1-004 | değiştirdi: V-P1-2 "bakılacak"→"doğrulandı" | C+ |
```

#### MK-6.4 Araştırma izi

| Alan | İçerik |
|---|---|
| Ne | Her tasarım kararına eklenen iz. Hangi bulgu kullanıldı, katkısı ne oldu (destekledi, değiştirdi, seçenek eledi, hiçbir şey değiştirmedi), neyi kanıtlamıyor, hangi hedef kanıtı hâlâ eksik. İzi olmayan karar "yalnız akıl yürütme" diye işaretlenir. |
| Nerede | Tasarım kararının kaydında bir alan grubu. EXP-007 DECISIONS'a göre Claude'un tasarım kararları ilgili aşama dosyasına yazılır ("Claude'un tasarım kararları buraya değil, ilgili aşama dosyasına gerekçesiyle yazılır"; DECISIONS kural satırı). Kesin yeri T1 belirler. Şablon aşağıda. |
| Ne zaman | Bir tasarım kararı kaydedilirken; karar revize edilince iz de güncellenir (MK-5.6). |
| Kim | Ana oturum. |
| Nasıl işler | Alanlar REUSE'un "minimal use record" önerisini ve A003 §3.5'i birleştirir: hedef soru; bulgu (yol#bölüm@sürüm) ve kanıt türü (MK-6.7); **katkı türü** (R09 protokolünün listesi: varsayım sınadı / çerçeve değiştirdi / seçenek ekledi / seçenek eledi / tercihi destekledi / kanıt gereksinimini netleştirdi / değiştirmedi); uygulanabilirlik ve karşı durum; neyi kanıtlamıyor; hâlâ eksik hedef kanıtı. İz yoksa: `yalnız akıl yürütme` ve nedeni (ör. "ilgili araştırma bulunmadı: arama terimleri …"). Sonucun değişmemesi meşrudur; "araştırmayı kullanmış görünmek için zorla yenilik veya öneri üretme" (R09 protokolü §4). |
| Zorlama düzeyi | Yapısal: karar kaydında zorunlu alan grubu. |
| Çalıştığını nasıl anlarız | Kapı boşluk kontrolünde (MK-6.1 tetik 9) izsiz karar oranı. Bir bulgu geri çekildiğinde, etkilediği kararlar iz alanlarından bulunabiliyor (R09 GZ-2 soy izi). **Bozulma işareti:** "destekledi" yazılmış ama bulgu kararla ilgisiz (karşı-okuma örneklem denetimi). |
| Bağımlılıklar | İhtiyaç: MK-6.3, MK-6.7, T1 (karar kaydı yeri), T4 (karşı-okuma). Beslediği: T4 S15 (muhakeme disiplini), MK-5.6 (geri çekmenin yayılımı), P0.5 söz–çıktı izlenebilirliği. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: tasarımın gerekçesiz kalması ve araştırmanın kullanıldığının görünmemesi [R11 E28]; Batu'nun "neden bu kadar bilgiyi sana ben araştırtmak zorundayım" eleştirisi (R03). Kabul testi: P0 pilotlarında her tasarım kararı iz taşır; karşı-okuyucu üç izi kaynağından sınar. |
| Kaynak | A003 §3.5 ("Araştırma izi"); REUSE "A minimal use record, when material" (g): "the target question; the exact research claim/path/version; its applicability and contrary case; the situated requirement or choice it informed; and what target evidence is still missing"; `candidate-research-library.md` §4 (g). |
| Bedel | Karar başına 4–6 satır. |

```text
Araştırma izi — Karar TK-P3-005 "roller arası istek: aracılı model"
hedef soru: K1'de istek → yanıt → kullanım nasıl kapanır?
| Bulgu (yol#bölüm@sürüm) | Kanıt türü / rol (MK-6.7) | Katkı | Uygulanabilirlik / karşı durum | Kanıtlamadığı |
| research/studies/superpowers/syntheses/S03…#§3 @<blob> | ürün kaynağı okuması / candidate mechanism | seçenek ekledi | tek koordinatörlü yapıda geçerli | canlı ajanlarla etkinlik |
| R01 eksik-arayıcı (depth=1) | alt ajan raporu + gözlem | seçenek eledi (rol→rol doğrudan) | bu ortam | başka ortamlar |
hâlâ eksik hedef kanıtı: P1 D-4 (SendMessage devamı) sonucu · işaret: — (yalnız akıl yürütme değil)
```

#### MK-6.5 Birlikte okuma işi

| Alan | İçerik |
|---|---|
| Ne | Kaynaklar farklı alt ajanlara bölündüğünde, kaynaklar arası yük taşıyan iddialar için ayrı açılan bir karşılaştırma kalemi. Özetler değil, özgün bölümler yan yana okunur. |
| Nerede | Kalem bloğunda `tür: birlikte-okuma` işareti; girdiler: iddia + özgün bölümlerin yolları @SHA. Çıktı: hizalama tablosu (aşağıda). |
| Ne zaman | Bir karar, iki ya da daha fazla kaynağın ilişkisine dayandığında ve bu kaynaklar ayrı okunduğunda. Örnek: T1–T5 birleştirmesi; P2'de SOUL işi ile ekip döngüsünün eşlenmesi. Tek kaynaklı soruda gereksizdir. |
| Kim | Bir alt ajan (T2: birlikte okuma işlevi); tercihen parça okumalarını yapmamış bir örnek. Hükmü ana oturum verir. |
| Nasıl işler | 1) Kaynaklar arası iddia tek cümleyle yazılır. 2) Karşılaştırma koşulları hizalanır: aynı şeyden mi, aynı zaman ve kapsamda mı, aynı birimde mi, aynı kipte mi (öneri / olgu / tahmin) bahsediyorlar, kökenleri bağımsız mı? (R10 §4.7, IS §13). 3) Hüküm: `tutarlı` / `çelişkili` / `farklı kapsam (çelişki değil)` / `hizalanamadı` / `bağımsız değil (aynı köken)`. 4) Çelişki varsa iki görüş de korunur, seçim yapılırsa dayanağı yazılır. |
| Zorlama düzeyi | Tavsiye + yapısal (tür işareti ve tablo). |
| Çalıştığını nasıl anlarız | Kaynaklar arası iddia taşıyan kararların hepsinde birlikte okuma ya da gerekçeli muafiyet var. **Bozulma işareti:** bir çelişki, birleştirme sonrasında karşı-okuma ya da Batu tarafından bulunuyor. |
| Bağımlılıklar | İhtiyaç: T2 (işlev), T1 (sürüm bağlama). Beslediği: MK-6.4, T2 birleştirme sözleşmesi (S12), MK-5.6. |
| Standart seviye kararı | **Gerekli, koşullu.** Önlediği hata: "Bu özet … içerik bakımından yanlış olmak zorunda değildir; fakat mektubu kimin gördüğünü kaybeder." [R11 K56]; ana oturum yalnız özetlerle birleştirince kaynaklar arası ilişkiler karşılaştırılmaz [R11 E31; §5 Y2 dengeleyicisi]. Kabul testi: Pilot-2'de en az bir birlikte okuma yapılır ve özetlerden çıkan hükümle karşılaştırılır. |
| Kaynak | A003 §3.4: "Okumak karşılaştırmak demek değildir."; R06 (T14 §§3,5,10); R10 §4.7. |
| Bedel | Yük taşıyan kaynaklar arası iddia başına bir alt ajan çağrısı. |

```text
Birlikte okuma — İK-P2-011 · iddia: "P3 döngüsünün her adımı en az bir P2 rolünün sahipliğinde"
| Koşul | Kaynak A (yol#§@SHA) | Kaynak B | Hizalı mı? |
| referans / kapsam / zaman / kip / köken bağımsızlığı | … | … | evet / hayır: … |
Hüküm: tutarlı | çelişkili | farklı kapsam | hizalanamadı | bağımsız değil → etki: <TK-… / DEĞ-…>
```

#### MK-6.6 Tazelik ve yeniden doğrulama

| Alan | İçerik |
|---|---|
| Ne | Dört bilgi sınıfı için tazelik kuralı. "Bayat" bir işarettir, silme ya da geçersizlik kararı değildir. |
| Nerede | Okuma kaydının sürüm ve erişim tarihi alanları (MK-6.3); T5'in kabiliyet haritası satırlarındaki kanıt türü; araştırma izinde "tazelik" notu. |
| Ne zaman | Yük taşıyan bir kullanımdan önce; bağımlılık değiştiğinde; aşama açılışında (Claude Code iddiaları için). |
| Kim | Ana oturum. Ortam iddialarının canlı sınaması T5 ve P1'dedir. |
| Nasıl işler | **Sınıf A, Claude Code ve ürün davranışı:** Güncel resmî belgeden, erişim tarihi ve cloud etiketiyle alınır. Yük taşıyorsa canlı denenir (P1). Erişim tarihi 30 günü aşmışsa yük taşıyan kullanımdan önce yeniden doğrulanır (v). **Sınıf B, studies'teki sabitlenmiş dış hedef bilgisi** (sürüm, API, fiyat, bakım durumu): study'nin pin'ine bağlıdır. Güncel bir karar için "authoritative current source'a dön" (R09 protokolü §6). **Sınıf C, Foundation'ın kavramsal ayrımları:** tazelik gerekmez, uygulanabilirlik denetlenir ("bu ayrım bu kullanıma uyuyor mu?"). **Sınıf D, Batu'nun kararları:** DECISIONS'taki güncel statüye bakılır. Askıda, yerine konmuş ya da kapanmış olabilir (ör. K-003 askıda, A-03 kapandı). **Genel kural:** Dayanak değişince ilgili kayıt `yeniden-değerlendir` işareti alır; "dependency changed → standing may require re-evaluation != standing necessarily changed" (R04 (a)5). |
| Zorlama düzeyi | Yapısal (tarih ve etiket alanları). |
| Çalıştığını nasıl anlarız | Yük taşıyan her Claude Code iddiasında erişim tarihi ve cloud etiketi var. **Bozulma işareti:** eski bir belgeden ya da raporun özetinden çıkarılan bir kabiliyetin ortamda yanlış çıkması ("bir rapor 'alt ajanlar üç kat iç içe çalışabilir' dedi; ortamda bakınca burada bunun kapalı olduğunu gördüm" [R11 K91]). |
| Bağımlılıklar | İhtiyaç: T5 (S19 kabiliyet haritası, platform değişikliği takibi, canlı doğrulama seti), T1 (bayat statüsü). Beslediği: MK-6.4, MK-5.5, P1. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: eski belgeden yanlış kabiliyet çıkarılması [R11 E30, K91]; tarihsel doğrunun güncel yetki sanılması (R10 §4.3). Kabul testi: P1 kapısında kabiliyet haritasının her satırında kanıt türü ve tarih var. |
| Kaynak | A003 §3.5 madde 6; R09 protokolü §6 (g); R10 §4.5 ("Bayat olmak yanlış olmak değildir"); R07 §9 ("Belgeler hızla değişiyor"). |
| Bedel | Yeniden doğrulama okumaları; canlı denemeler P1 bütçesinde. |

#### MK-6.7 Kanıt gücü ve epistemik rol etiketi

| Alan | İçerik |
|---|---|
| Ne | Her kullanılan bulguya iki etiket: kanıt türü (ne kadar güçlü, kimden) ve epistemik rol (bu kararda ne işe yaradı). Aday çalışmalar varsayılan olarak "benimsenmiş değil" sayılır. |
| Nerede | Araştırma izinin "Kanıt türü / rol" sütunu (MK-6.4); okuma kaydının "Not" sütunu. |
| Ne zaman | Bir bulgu bir karara dayanak yapıldığında. |
| Kim | Ana oturum; alt ajan dönüşünde öneri olarak gelir (T2 dönüş şeması). |
| Nasıl işler | **Kanıt türü** (R11 §0.3 düzeni): Batu'nun sözü · repo olayı · tedarikçi belgesi · tedarikçinin iç ölçümü · ürün kaynağı okuması (çalıştırılmamış) · kavramsal analiz (aynı asistan) · alt ajan raporu (ikincil) · gözlem · bağımsız ölçüm (bugün hiç yok). **Epistemik rol** (R09 protokolü §7): evidence/reference · falsifier/counterexample · design pressure · capability source · implementation-learning reference · test-case source · candidate mechanism · rejected option. **Bağımsızlık kontrolü:** Aynı bulgu birkaç notta geçiyorsa kökenleri ortak mı? Aynı modelin aynı kaynaklardan ürettiği notlar bağımsız destek sayılmaz ("Multiplying copies does not increase independent observation count." [R11 K45]). |
| Zorlama düzeyi | Yapısal (sütun). |
| Çalıştığını nasıl anlarız | Karşı-okuma örneklem denetiminde etiketler kaynağın gerçek türüyle uyuşuyor. **Bozulma işareti:** "birkaç kaynak aynı şeyi söylüyor" gerekçesi ile ortak kökenli notların bağımsız sayılması (R01–R11'in çoğu aynı modelin notlarıdır). |
| Bağımlılıklar | İhtiyaç: T4 (S14 kanıt gücü beyanı). Beslediği: MK-6.4, T4 kabul paketi ("bunu kimse bağımsız doğrulamadı" satırı; R11 §5 Y6). |
| Standart seviye kararı | **Gerekli.** Önlediği hata: güvenin şişmesi; aday çalışmanın benimsenmiş mimari sanılması ("Bir candidate study'nin mevcut olması onun … architecture component'i veya kullanılacak dependency olduğu anlamına gelmez."; R09 protokolü "Temel İlke"; g). Kabul testi: P4 kabul paketinde her yük taşıyan iddianın kanıt türü görünür. |
| Kaynak | [R11 K45]; R11 §0.3; `candidate-research-library.md` §7 (g); ORTAK "Kanıt dili". |
| Bedel | Bulgu başına iki kısa etiket. |

#### MK-6.8 Durma ölçütü

| Alan | İçerik |
|---|---|
| Ne | Ek okumanın ne zaman durdurulacağını belirleyen soru ve kural. Bütçenin bitmesi "bitti" değil "park" sayılır. |
| Nerede | Okuma kaleminin bloğunda `durma_ölçütü` alanı; brief'te aynı alan (A003 §3.3 madde 9). |
| Ne zaman | Her ek okuma ya da ek inceleme turundan önce; bütçe eşiğine yaklaşıldığında. |
| Kim | Ana oturum; alt ajan kendi brief'indeki ölçütü uygular. |
| Nasıl işler | 1) Soru: **"Hangi olası sonuç hangi kararı değiştirir?"** (R06, T11 §§4–5). Cevap "hiçbiri" ise okuma yapılmaz, gerekçe tek satırla yazılır. 2) Okuma sürerken karar için yeterli derinliğe inildiyse durulur. Kalan kısım `okunmadı` olarak kayda geçer. 3) Bütçe bittiyse kalem `park` olur ve ne kaldığı yazılır. 4) Erişilemeyen kaynak "erişilemedi" diye yazılır; içeriği tahmin edilmez; var olmayan kaynak sonsuza dek aranmaz (E-MARS; R07 §3). 5) Aynı soru için ikinci bir inceleme ya da okuma turu, yalnız ilkinden farklı bir girdi ya da yöntemle açılır; aynı incelemeyi tekrarlamak güven eklemez (R06). |
| Zorlama düzeyi | Yapısal (alan). |
| Çalıştığını nasıl anlarız | Okuma kaydında "değiştirmedi" oranı ve park edilen okuma sayısı. **Bozulma işaretleri:** aynı kaynağın aynı soru için birden çok kez okunması; bütçesi bittiği için "tamam" işaretlenmiş bir okuma. |
| Bağımlılıklar | İhtiyaç: T5 (bütçe), MK-6.3. Beslediği: MK-3.8 (ağırlık), T5 maliyet. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: sonsuz okuma ya da sahte kapanış; "«token bütçesi bitti» birer faaliyet/kaynak olayıdır; doğrulama sonucu değildir" [R11 K83]. Kabul testi: pilotlarda her ek okuma kaleminde durma sorusunun cevabı var. |
| Kaynak | A003 §3.3 madde 9 ("Bütçenin bitmesi 'bitti' sayılmaz, 'park edildi' sayılır"), §3.5 ("Ek okuma kararı değiştirmeyecekse durulur"); R06 (T11); R07 §3 (E-MARS: "scouring the web endlessly for nonexistent sources"). |
| Bedel | Okuma başına bir satır. |

#### MK-6.9 "Şu alana bakılmalı" bildirimi

| Alan | İçerik |
|---|---|
| Ne | Alt ajanın kendi sorusu verilen kaynaklarda cevapsız kaldığında bunu yapılandırılmış biçimde bildirme yükümlülüğü, ve ana oturumun her bildirime akıbet yazması. |
| Nerede | T2'nin dönüş şemasına eklenecek alan (`kaynak_boşluğu`; şablon aşağıda). İşlenmiş hali açık soru kaydında (MK-4.3) ya da yeni okuma kaleminde. |
| Ne zaman | Her alt ajan dönüşünde (boş olabilir); ana oturum dönüşü işlerken (MK-3.4 "alt ajan dönüşü"). |
| Kim | Bildirir: alt ajan. Akıbete ana oturum karar verir. |
| Nasıl işler | 1) Alt ajan kaynak dışına kendi başına dalmaz; hangi kaynağa bakacağını brief söyler (A003 §3.5). Ama cevapsız kalan soruyu yazmak zorundadır. 2) Bildirimde şu var: soru; verilen kaynaklarda neden cevapsız kaldığı; bakılması önerilen alan (Foundation satırı, study, dış kaynak); cevap kararı değiştirebilir mi. 3) Ana oturumun akıbet seçenekleri: açık soru (AS) / yeni okuma kalemi (tetik 8) / gerekçeli ret. 4) "Kaynakta cevap yok" ile "kaynağı bulamadım" ayrı yazılır; hangi aramanın yapıldığı eklenir ("'Found nothing' must say what was searched"; R04 (b)5). |
| Zorlama düzeyi | Yapısal (dönüş şemasında zorunlu alan; boş değer "yok" yazılır). |
| Çalıştığını nasıl anlarız | Bildirimlerin akıbet oranı; bildirimden doğup kararı değiştiren okuma sayısı. **Bozulma işareti:** bir alt ajanın cevapsız bıraktığı soruyu dönüşünde "kesin" bir iddiaya çevirmesi (uydurma; T4 S15). |
| Bağımlılıklar | İhtiyaç: T2 (dönüş şeması). Beslediği: MK-4.3, MK-6.1 (tetik 8), MK-4.5. |
| Standart seviye kararı | **Gerekli.** Önlediği hata: keşfin, koordinatörün kaynak seçimiyle sınırlanması (R11 §5 Y15'in dengeleyicisi "'Şu alana bakılmalı' bildirim yükümlülüğü"). Kabul testi: pilotlarda dönüşlerin hepsinde alan var (boşsa "yok"). |
| Kaynak | A003 §3.5: "verilen kaynakların cevaplamadığı bir soruya çarparsa, bunu 'şu alana bakılmalı' diye bildirmek zorundadır"; R07 §2.6 (PRJ: "say exactly what's missing in your first message and stop. Don't substitute, mock, or guess."). |
| Bedel | Dönüş başına 0–4 satır. |

```text
kaynak_boşluğu:
  - soru: "Routines'in günlük koşu tavanı nedir?"
    neden cevapsız: verilen R01 ve R07 bölümlerinde yalnız "daily run cap" var, değer yok
    bakılması önerilen: claude.ai/code/routines arayüzü (Batu'nun hesabı) — belge değil hesap bilgisi
    arama: R01, R07 içinde "cap", "daily" (grep) · kararı değiştirebilir mi: evet (P1 bütçesi, V-P1-3)
```

## 7. Arayüzler: diğer kümelerden istenenler ve onlara verilenler

Her "istenen", birleştirmede bir "verilen" ile karşılanmalıdır. Karşılanmazsa birleştirme ajanı kapatır.

### 7.1 T1'den istenenler (bilgi taşıma, dosya mimarisi)
| # | İstenen | Kullanan kart | Not |
|---|---|---|---|
| T1-a | Plan ve iş kaydı dosyalarının yeri ve biçimi. Önerim: `PLAN.md` (kök), `phases/<Pn>/README.md`, `ISLER.md`, `OKUMA.md` | MK-5.1, MK-5.2, MK-6.3 | Çelişirse T1'in yapısı esastır; tek kaynak şartı korunmalı |
| T1-b | Statü sözlüğü: kalem statüleri (aday, kabul, sürüyor, bitti, doğrulandı, park, düştü, yeniden-değerlendir) ile T1'in sözlüğünün hizalanması; "bilinmiyor, değerlendirilmedi, bayat" | MK-5.2, MK-3.5 | "Hazır" statü değil, hesaplanan bir yüklemdir |
| T1-c | Yayılım kontrolü: karar değişince türetilmiş kopyaların (STATE, devir notu, rol belleği) taranması | MK-5.6 adım 6 | W6 |
| T1-d | Tasarım kararı kaydının yeri; araştırma izi alan grubu bu kayda eklenir | MK-6.4 | DECISIONS yalnız Batu'nundur |
| T1-e | Batu'nun sözlerinin birebir deposu ve alıntı yolu | MK-4.5, MK-4.6 | Eksik-arayıcıya ve çerçeve notuna birebir verilir |
| T1-f | Açılış seti bütçesi içinde plan yüzeylerinin payı | MK-3.8 ölçü 3 | Plan dosyası büyümesi şişme döngüsüne girer |
| T1-g | Bağlam paketinde "yol ile birlikte ilgili pasaj" kuralı | MK-6.2 | "pointer ≠ content" [R11 K84] |

### 7.2 T2'den istenenler (roller, orkestrasyon, arayüzler)
| # | İstenen | Kullanan kart |
|---|---|---|
| T2-a | Bu taslağın işlev ihtiyaçlarının role eşlenmesi: planlama ve koordinasyon (ana oturum), okuyucu ve araştırmacı, **eksik-arayıcı** (brief'ten bağımsız kaynak alanıyla), karşı-okuyucu, birlikte okuma işçisi, ortam deneyicisi (P1), taslakçı ve bütünleştirici (P2–P4), soğuk başlangıç sınayıcısı (P0) | MK-3.2, MK-4.5, MK-6.5, §2.3 |
| T2-b | "Hangi rol hangi aşamada ve hangi işte çalışır" tablosu (T3 brief'inin isteği) | §2.3 aşama kartlarının "işlev" satırları |
| T2-c | Brief şablonuna alanlar: `kalem_ID`, `rota`, `okuma_rotası`, `durma_ölçütü`, `verilmeyecekler` (karşı-okuma ve eksik-arayıcı için) | MK-3.3, MK-6.2, MK-6.8, MK-4.5 |
| T2-d | Dönüş şemasına alanlar: `kaynak_boşluğu`, `okuma_kapsamı` (tam / kısmi / okunmadı / erişilemedi, kesik çıktı işareti), `keşfedilen_iş`, `varsayımlar_ve_otomatik_seçimler`, `karar_değişti_mi` | MK-6.9, MK-6.3, MK-4.4, MK-5.5 |
| T2-e | Kural: alt ajan plan yüzeylerine yazmaz, statü değiştirmez, sıradaki kalemi seçmez | MK-5.1, MK-5.2, MK-5.3 |
| T2-f | Brief sürümü ve HEAD kaydı (kalem bloğunda `başlangıç` alanına yazılır) | MK-5.2, MK-5.10 |
| T2-g | Çalışan alt ajanlara karar yayılımı kuralı (W6) | MK-5.6 adım 6 |

### 7.3 T4'e verilenler ve T4'ten istenenler (yönetişim, Batu, kalite, gözlem)
**Verilenler:**
- Kapı türleri ve kapı kaydı (MK-3.5); geçiş tablosu ve duraklar (§2.4). T4 durakları ve ilerleme ölçüsünü bunlara bağlar.
- Revizyon yetkisi tablosu (MK-5.7). T4'ün karar hakları tablosuyla tek tabloda birleşir; çelişki varsa birleştirmede çözülür.
- **Söz–çıktı izlenebilirliğinin plan tarafı:** Her kalem bloğunda `kaynak_söz` alanı var (U00x, A003 §x ya da çıkış ölçütü). Böylece "Batu'nun her sözü → hangi kalem ya da mekanizma" matrisi kalem bloklarından çıkarılabilir. Harita düzeyinde her aşama kartı, beslediği Batu gereksinimini gösterir.
- İlerleme ölçüsünün girdileri: kapanan soru (MK-4.3), değişen karar (`karar_değişti_mi` satırı; MK-3.3), kabul edilen çıktı (kapı kaydı), meta-iş payı (MK-3.8), Batu kökenli keşif ve "kaçıran alt sistem" (MK-4.4).
- Batu'ya giden soruların kaynağı: açık soru kaydının `sınıf: Batu` alt kümesi (MK-4.3). T4'ün soru kuyruğu ayrı bir kopya tutmamalı.
- P0.8 onay paketine girecek sorular (§2.4).

**İstenenler:**
- İlerleme ölçüsü, takılma türleri ve alarm eşikleri → MK-5.10'un tetiği.
- Soru kuyruğu ve kontrol noktası raporu biçimi; kabul paketi (P0, P4, P6).
- Karşı-okuma türleri, "gerekçeyi görmeyen" okuma kuralı ve bağımsızlık etiketi (MK-3.5, MK-3.6, MK-4.5).
- Ölçüt bütünlüğü kuralı (MK-3.3'teki bitti tanımının sonradan değişmemesi).
- Otomatik seçim kaydı (MK-4.3 "teknik karar" sınıfı).

### 7.4 T5'e verilenler ve T5'ten istenenler (süreklilik, ortam, maliyet, öğrenme)
**Verilenler:**
- Ritim takvimi ve her ritmin uyandırma ihtiyacı (MK-3.4 tablosu). Uyandırma olmadan oturumlar arası boşlukta ritim çalışmaz.
- Aşama bütçesi girdileri: her aşama açılışında tahmini kalem sayısı, rota karışımı ve paralellik ihtiyacı (MK-3.2); aşama başına bütçe şekli (§2.6).
- P1 asgari deneme seti (§2.3 P1 çıkış ölçütü 2). T5'in canlı doğrulama setiyle aynı denemeler tek sefer koşulur.
- Retronun ve bakımın aşama kapısındaki yeri (MK-3.5, MK-3.4); sadeleştirme sorusu (MK-3.8).
- `hedef: yöntem` kalemleri: yöntem değişikliği kontrolüne (S21) giren işler.

**İstenenler:**
- Oturum açılış ve kapanış protokolünün içeriği (MK-3.4 ilk satır), açılış sinyali ("son karardan bu yana X gün").
- Uyandırma mekanizmalarının durumu ve kullanım kuralı (V-H-1); yarım iş protokolü (MK-5.2 geçiş kuralı 2; MK-5.10 "işçi kayıp").
- Bütçe ve limit davranışı; paralellik tavanı (MK-5.3 WIP sınırıyla hizalanır).
- İsteğe bağlı zorlayıcı kontroller: `İK-` kimliklerinin silinmediğini ve zorunlu alanların dolu olduğunu denetleyen betik; tek repolu oturum koşulu ve A-04 onayı (MK-5.1, MK-5.2).
- Kabiliyet haritası ve platform değişikliği takibi (MK-6.6 sınıf A).

## 8. Etkileşimler ve dengeleyiciler

### 8.1 R11 §4.4'teki T3 kenarları ve bu taslaktaki karşılıkları
| Kenar | Bozulma | Bu taslakta önleyen |
|---|---|---|
| E12 S3→S5 ● | Harita yoksa yön bir önceki turdan gelir | §2 harita; MK-3.1 |
| E13 S3→S17 ◐ | Bitti tanımı ve kapı yoksa ilerleme ölçülemez | MK-3.3 (bitti tanımı işten önce); MK-3.5 |
| E14 S3→S20 ● | Tören orantısı yoksa yöntem kendi ağırlığı altında durur | MK-3.6; MK-3.8 |
| E15 S3→S14 ◐ | Kapı tanımsızsa ya hep tören ya hiç kontrol | MK-3.5; MK-3.6 |
| E16 S3→S21 ● | Meta-iş sınırı yoksa süreç ürüne dönüşür | MK-3.8 |
| E17 S4→S2 ● | Eksik işi Batu bulur | MK-4.1, MK-4.2, MK-4.5; ölçü: MK-4.4 |
| E18 S4→S5 ● | Plan yalnız bilinen işi taşır | MK-4.5 (plan dışından tarama) |
| E19 S4→S14 ● | Eksik iş "tamam" damgası alır | MK-4.5 kapı kaydında zorunlu satır |
| E20 S4→S11 ● | Roller yanlış kaynaktan türer | MK-4.6; P2 çıkış ölçütü 1 |
| E21 S4→S6 ◐ | Kaynak alanı dar seçilir | MK-4.1 adım 5; MK-6.2; MK-6.9 |
| E22 S5→S17 ◐ | Kalem statüsü yoksa ilerleme ölçüsünün dayanağı kalmaz | MK-5.2 |
| E23 S5→S18 ● | Neyin kapandığı ve devralındığı kayıtlı değil | MK-5.2 (`sürüyor` + brief + HEAD); MK-3.4 "yarım kalem önce" |
| E24 S5→S2 ● | Kötü dilim Batu'ya soru üretir | MK-5.4 |
| E25 S5→S12 ○ | Bağımlılık türleri ayrılmazsa paralel dağıtım yanlış sıralanır | MK-5.3 |
| E26 S5→S9 ◐ | Sapma kaydı yoksa kötü plan hep doğruymuş görünür | MK-5.8 |
| E27 S6→S4 ● | Birikim uygulanmazsa keşif çapalanır | MK-6.1 tetik 1; MK-4.2 mercek H |
| E28 S6→S15 ◐ | İz yoksa tasarım "yalnız akıl yürütme"ye kalır | MK-6.4 |
| E29 S6→S14 ● | "Tam okudum" sınanamaz | MK-6.3 |
| E30 S6→S19 ● | Claude Code iddiası ortamda sınanmaz | MK-6.6; P1 canlı deneme |

**Gelen kenarlar** (başka kümelerin zayıflığı T3'ü bozar): E03 S1→S5 (çerçeve değişikliği kontrolü; T4 ve MK-5.6 birlikte), E10 S2→S5 (soru kuyruğu; MK-4.3 kaynağı), E11 S2→S4 (keşif sisteme verilmezse Batu keşfeder), E42 S9→S5 (tek kaynak; T1-a), E73 S15→S5 (çapa dosyadan yüklenmezse drift; MK-3.1 haritası çapadır), E77 S16→S5 (eski "sıradaki" satırları talimat sayılırsa plan eski yöne çekilir; §2.1: EXP-006 girdidir, talimat değildir), E80 S17→S5 (canlılık ölçülüp ilerleme ölçülmezse; T4 + MK-5.10), E86 S18→S5 (yeniden girişte iz; MK-5.2 + T5).

### 8.2 "Yeterli görünüp yetersizleştiren" seçimler (R11 §5): T3 kapsamındakiler
| Seçim | Neyi zayıflatır | Dengeleyicinin yeri |
|---|---|---|
| Y7 Kontrol riskle orantılı | "Düşük risk" sınıfı eleştirisiz kararları yayar | MK-3.6'da aşağı akış yükü sorusu (S1) |
| Y8 En fazla üç eleştiri turu | Park edilen bulgular görünmez birikir | MK-5.9 park ve tetik; MK-3.5 kapı kaydında açık bulgular ve akıbet |
| Y11 Sorular birikir, iş durmaz | Yanlış çerçeve geç fark edilir | MK-4.3: çerçeve sorusu biriktirilmez; etkilenen kalemler park |
| Y12 Kendiliğinden geçiş | Aşamalar arasında doğal kontrol noktası kalmaz | MK-3.5 kapı kaydı; P2/P3 ortak kapısı; MK-3.4 periyodik yön gözden geçirmesi; T4 alarmı |
| Y14 Her okuma için okuma kaydı | Maliyet; kayıt anlama sanılır | MK-6.3 yalnız karar taşıyan okumada; "neyi değiştirdi" zorunlu |
| Y15 Kaynak seçimini brief'e bırakmak | Keşif koordinatörün seçimiyle sınırlanır | MK-6.9; MK-4.5 bağımsız kaynak alanı |
| Y16 Batu'ya sormak son seçenek | Değer seçimleri sessizce verilir | MK-4.3 sınıflaması; T4 otomatik seçim kaydı |
| Y4 Üç tekrardan sonra kalıcı ajan | Kalıcı roller gecikir | MK-3.7'nin sınırı: pilot kuralı rol iskeletini geciktirmez (T2) |
| Y10 Her şeyi repoya yaz | Kayıt şişer, kopyalar çelişir | MK-5.1 tek kaynak; STATE yalnız işaretçi; MK-3.8 ölçü 3 |

### 8.3 Birbirini besleyen döngüler (R11 §4.5) ve T3'ün payı
- **Şişme döngüsü** (S9 → S7 → S20 → S10 → S18): Plan yüzeyleri de büyür. Kalem blokları ekleme-yalnızdır; bu, silmeyi önler ama büyümeyi artırır. **Fren:** aşama başına ayrı `ISLER.md`; açılış setine yalnız açık kalemler girer (T1); MK-3.8 ölçü 3. Kapanmış aşamanın ISLER dosyası arşiv niteliğindedir; bağlama ancak soru üzerine girer (ç).
- **Batu yükü döngüsü** (S4 → S2 → S14 → S2): T3'ün en büyük payı burada. **Fren:** keşif turu, bakış açısı taraması ve bağımsız eksik-arayıcı; "kaçıran alt sistem" alanı, döngünün kaynağını görünür yapar (MK-4.4).
- **Öz-onay döngüsü** (S15 → S14 → S17 → S1): Kendiliğinden geçiş (K-002) bu döngüyü hızlandırabilir. **Fren:** kapı kaydında karşı-okumanın bağımsızlık etiketi (T4) ve "doğrulanamadı" hükmünün gerekçesiz "geç"e dönüşmemesi (MK-3.5).
- **Kural birikimi döngüsü** (S21 → S19 → S7 → S15): T3'ün şablonları da birikebilir. **Fren:** MK-3.8'deki sadeleştirme sorusu; yeni şablon alanı yalnız gözlenmiş bir hatayla eklenir (T5'in ders kabul testi).

### 8.4 Bütünsel gerilim: standart seviye ile hafiflik
Bu taslak 33 mekanizma kartı kuruyor. Hepsi aynı anda ağır törenle çalışırsa R11 §1 madde 6'daki karşı ağırlık ihlal edilir: "standart seviye, her alt sistem için ayrı dosya, ajan ya da tören demek değildir". Hafiflik üç yolla sağlanır:
1. Kartların çoğu bir şablon alanı ya da bir kontrol sorusudur, ayrı bir iş değildir. Yeni dosya yalnız dört tanedir (`PLAN.md` ve aşama başına üç dosya).
2. Rota ölçeklemesi (MK-3.6): yoklama rotası yalnız üç kayıt satırı ister.
3. Pilotlar ve ağırlık bütçesi (MK-3.7, MK-3.8): "hiçbir kararı değiştirmeyen" mekanizma sadeleştirme adayıdır.

"Daha basiti yeter" gerekçesiyle bileşen düşürülmedi; her bileşen bir olaya ya da kaynağa bağlı (karar tabloları).

## 9. Çarpışma testlerine katkı: W1–W10

Aşağıda yalnız T3'ün mekanizmalarının devreye girdiği adımlar var. Okunan (O) ve yazılan (Y) dosyalar önerilen yollarla gösterildi. Tam yürüyüşü birleştirme ajanı kurar.

**W1 Soğuk başlangıç.**
1. T5'in açılış protokolü STATE'i okutur (O: `STATE.md`) → şu anki aşama ve `sürüyor` kalem kimlikleri.
2. O: `PLAN.md` §1'de aşama kartı → ana soru, çıkış ölçütü, sıradaki geçişin türü (MK-3.1).
3. O: `phases/<Pn>/README.md` (çerçeve) ve `ISLER.md`'nin açık kalemleri, açık soruları ve varsayımları.
4. **İlk eylem:** `sürüyor` statülü ve dönüşü olmayan kalem varsa önce o devralınır (MK-3.4; T5 yarım iş protokolü). Yoksa hazır iş hesabı yapılır (MK-5.3) ve seçilen kalem STATE'e yazılır (Y: `STATE.md`).
5. Varsayım kaydında `bayat` olan varsa önce o sınanır (MK-5.5).

**W2 Bir iş kalemi döngüsü.**
1. Soru doğar: açık soru (MK-4.3) ya da keşif bulgusu (MK-4.4) → aday kalem (Y: `ISLER.md`).
2. Kabul (MK-5.7 satır 2) → rota dört soruyla seçilir (MK-3.6) → dilim kontrolü (MK-5.4).
3. Hazır mı (MK-5.3)? → rol seçimi (T2) → bağlam paketi (T1) → brief, okuma rotası ve durma ölçütüyle (MK-6.2, MK-6.8; T2).
4. `sürüyor` + brief kimliği + HEAD (Y: `ISLER.md`) → alt ajan çalışır.
5. Dönüş: `kaynak_boşluğu` işlenir (MK-6.9), okuma kapsamı aktarılır (Y: `OKUMA.md`; MK-6.3).
6. Kontrol: rotaya göre (T4) → kalem kapısı (MK-3.5) → kapanış satırları (MK-3.3; Y: `ISLER.md`).
7. Karar değiştiyse karar kaydı ve araştırma izi (MK-6.4; T1 yeri) → yeni keşifler ve varsayım etkisi → bellek güncellemesi (T1).
8. Plan güncellemesi: statü `doğrulandı`, gerekiyorsa `DEĞ` (MK-5.6) → her 5 kalemde yön gözden geçirmesi (MK-3.4).

**W3 Aşama sonu.**
1. Bütün çıkış ölçütleri "karşılandı" görününce kapı kaydı açılır (MK-3.5; Y: `phases/<Pn>/README.md`).
2. Ölçütler aynen listelenir; kanıt işaretçileri yazılır.
3. Bağımsız eksik-arayıcı taraması (MK-4.5) ve araştırma boşluk kontrolü (MK-6.1 tetik 9).
4. Kabul edilmiş sürüme göre sapma listesi (MK-5.8); park listesi (MK-5.9); ağırlık bütçesi ölçüleri (MK-3.8).
5. Retro (T5), bakım (T1/T5) → Batu'ya aşama raporu (T4).
6. Geçiş türü okunur (§2.4): kendiliğinden ise aynı oturumda sonraki aşamanın açılış oturumu (MK-3.2; Y: `PLAN.md` durum alanları, yeni aşama klasörü); durak ise bekleme (P4 kartındaki "durakta sürebilecek işler").

**W4 Bağlam sıkıştırma anı.**
- **Öncesi:** Plan durumu zaten dosyadadır (MK-5.1). Açık kalemin kapanış satırlarının ara hali yazılır (MK-3.4 "bağlam eşiği").
- **Sonrası:** T1/T5'in yeniden yükleme protokolü aşama kartını ve açık kalem bloğunu yeniden okutur.
- **Korunan:** harita, kabul işaretleri, kalem statüleri, açık sorular ve `return_to`'ları, varsayım durumları.
- **Kaybolabilen:** kapanış satırına yazılmamış ara akıl yürütme. Bunun için kural: kararı taşıyan her ara sonuç önce `ISLER.md`'ye yazılır (ç).

**W5 Oturum ya da makine kaybı.**
1. Yeni oturum W1'i yürütür.
2. `sürüyor` kalemlerin brief kimliği ve başlangıç HEAD'i (MK-5.2) ile `git status` ve `git log` karşılaştırılır (T5).
3. Dönüş dosyası yoksa ya da yarımsa kalem `bitti` sayılmaz (geçiş kuralı 2). Aynı brief'le yeniden başlatılır ve bu kalem bloğuna yazılır.
4. Kısmi yazımlar uzlaştırılır (T2/T5). Zaman aşımı "olmadı" demek değildir [R11 S18].

**W6 Karar değişikliğinin yayılması** (K-010 olayı).
1. Batu'nun mesajı gelir → MK-5.6 adım 1: sınıflama (Batu'nun amacı ya da kapsamı; dünyadaki değişiklik, geçerlilik tarihiyle).
2. Adım 2: yetki (MK-5.7 satır 12) → Batu'nun kararıdır, kayda geçer (T1: DECISIONS).
3. Adım 5: `DEĞ` satırı (Y: `PLAN.md` §4).
4. Adım 6: `etkilenir` bağlarıyla etkilenen kalemler bulunur ve `yeniden-değerlendir` olur (MK-5.3). Açık soruların `return_to` alanları taranır (MK-4.3). Türetilmiş kopyalar T1'in yayılım kontrolüyle taranır. Çalışan alt ajanlar T2'nin kuralıyla bilgilendirilir.
5. Geç dönen sonuç, brief sürümüne göre uzlaştırılır (taban kontrolü, adım 4).
- **T3'ün katkısı:** Etkilenen işin *bulunabilir* olması: `etkilenir` bağ türü ve `return_to` alanı.

**W7 Plan revizyonu: bir varsayım çöker.**
1. Varsayım kaydında durum `çöktü` (MK-5.5; Y: `PLAN.md` §3 ya da `ISLER.md` §3).
2. "Dayananlar" alanından etkilenen aşama ve kalemler bulunur → MK-5.6 tetik (a).
3. Sınıflama → yetki: harita değişiyorsa Batu (satır 11), aşama içi ise ana oturum.
4. Hata ait olduğu katmanda düzeltilir → hedefli geri dönüş kalemi (MK-5.9; ör. P3→P1).
5. Kabul edilmiş sürümden sapıyorsa `SAP` (MK-5.8) → aşama raporunda bildirim.

**W8 Batu'nun itirazı ya da yeni yönü.**
1. Keşif kaydı: `köken: Batu`, `kaçıran_alt_sistem` (MK-4.4). T4'ün hatırlatma kaydına işaretçi eklenir.
2. Çerçeve yeterliği sınaması yeniden koşulur (MK-4.6).
3. Tetik 7: araştırmada karşılığı var mı (MK-6.1).
4. MK-5.6'nın sınıflaması: "Batu'yu yanlış anlamıştık" (düzeltme) mı, "Batu yön değiştirdi" (dünyadaki değişiklik) mi?
5. Çerçeve sorusu ise ilgili kalemler park edilir (MK-4.3).
6. Kanıt dışı etkiye direnç ve açık tutum beyanı T4/S15'tedir: "When he objects, re-examine and state plainly whether and why my position changes" (R03 §5 madde 12).

**W9 Takılma: hareket var, ilerleme yok.**
1. T4'ün alarmı ya da yön gözden geçirmesinin 2. sorusu ("son 5 kalemde kaç karar değişti?") tetikler.
2. `TAK` kaydı (MK-5.10): tür → türe göre tepki (yeniden dilim MK-5.4, brief değişikliği, çerçeve sınaması MK-4.6, park, Batu raporu).
3. Aynı kalemde üç başarısız denemede devre kesilir.
4. Meta-iş payı ve "son ürün katkısından bu yana" ölçüleri (MK-3.8) raporun ilk satırıdır.

**W10 Bir dersin davranışa dönüşmesi.** Sahibi T5'tir. T3'ün katkısı iki yönlüdür:
1. Ders bir plan yüzeyine işlenirse (ör. kalem şablonuna yeni zorunlu alan, rota sorusuna ek), bu bir `hedef: yöntem` kalemidir (MK-3.8) ve ilk örnek kuralıyla tek kalemde denenir (MK-3.7).
2. Davranış değişiminin doğrulanması ayrı bir kalem olarak planlanır. Bitti tanımı: "İK-… kaleminde, dersin hedeflediği durumda farklı davranış gözlendi (kanıt: …)". Gözlenene kadar ders "doğrulanmadı" kalır (A003 §3.10).

## 10. Batu onayı gerektirenler

| # | Konu | Neden onay | İlişki | Önerim |
|---|---|---|---|---|
| 1 | P0–P6 haritası ve EXP-006'ya göre değişiklikler (§2.2) | Harita Batu'nundur (A003 §3.7) | K-010 | Kabul |
| 2 | K-002'nin bu haritaya uygulanması: aynı numaralı P1–P4 aynı yetkiyle | Sürekli yetkinin kapsamı uydurulamaz [R01] | K-002 | Aynen uygulansın |
| 3 | P3 çıkışında durak mı, kontrol noktası raporu mu? | Batu'nun P3'ü derin konuşma isteği (EXP-006) ile K-002'nin kendiliğinden geçişi arasında seçim | K-002 | Rapor; iş durmaz |
| 4 | P5→P6 geçişinin türü; duraklarda sürebilecek işler | K-002 kapsamı dışında | K-002, A002 varsayımı | P6 canlı sınaması ayrı yetkiyle; durakta yalnız kabulü varsaymayan işler |
| 5 | P1 deneme izni: araçlar (`send_later`, `create_trigger`, gerekirse `create_session`), bütçe, Loopinance repoları için salt okuma `add_repo` | "Yeni erişim" K-002'ye göre Batu'nundur; maliyet ve dış etki | K-002; T5 | P0.8 paketinde tek seferde |
| 6 | A-02: P0 pilotları (§2.5) | Batu'nun cevabı bekleniyor | A-02 | Yapılsın; Pilot-1 ve Pilot-2 |
| 7 | Revizyon yetkisi tablosu (MK-5.7) | Claude ile Batu arasındaki sınırı çizer | T4 S1 | Kabul (T4'ün tablosuyla birleşik) |
| 8 | "DevOS'un ilk SOUL işini Claude seçmez" kuralı | Batu'nun sözü EXP-006'da; K-010 nedeniyle yeniden teyit | K-010 | Geçerli |
| 9 | Plan kontrol betiği ya da hook'u (isteğe bağlı; MK-5.1, MK-5.2) | Yapılandırma değişikliği; tek repolu oturum koşulu | A-04; T5 | Önce pilot. Silme ya da yeniden yazma olayı olursa önerilir |

**A-01 ile ilişki:** S6, AGENT.md R09 protokolünün geri çağırma ve statü kurallarına dayanıyor (§6.1). A-01'in cevabı "AGENT.md kalmıyor" olursa bu kurallar METHOD'a taşınır. İçerikleri değişmez. **A-04 ile ilişki:** T3'ün önerdiği dosyaların hepsi EXP-007 klasöründedir ve A-04 kapsamında değildir. Yalnız 9. satırdaki zorlayıcı kontrol A-04'e girer.

## 11. Açık sorular, varsayımlar ve bu taslağın kanıtlamadıkları

### 11.1 Açık sorular
1. **Uyandırma:** Oturumlar arası uyandırma (`send_later`, Routines, Projects) bu hesapta çalışıyor mu? Çalışmıyorsa kendiliğinden geçişler oturum sınırında durur ve oturumu Batu açar (V-H-1). Ritim takviminin oturumlar arası kısmı buna bağlı (b; T5, P1).
2. **Plan kaydı biçimi:** Blok biçimli Markdown mı, JSON/YAML mı? E-HAR'ın JSON önerisi yazılım iş listesi içindir; tasarım işindeki etkisi ölçülmedi (b). Pilotlar karar verir.
3. **Eşikler:** Bütün eşikler (v) etiketlidir: WIP 3, meta-iş %25, yön gözden geçirmesi 5 kalem, "son ürün katkısı" 5 kalem ya da 2 oturum, dilim kontrolü 3/5, Claude Code iddiası tazeliği 30 gün, devre kesici 3. Kaynaklarda bu işe özgü eşik yok. Pilotlarda ayarlanacak.
4. **Tasarım işinde "koşulabilir kontrol":** Kapılar çoğunlukla denetlenebilir ifade ve karşı-okumayla işler. Mekanik kontrol azdır (R07 §8 soru 7). Kapı kaydının sertliği T4'ün rubrik kararına bağlı.
5. **DevOS'un hedef konumu:** Hangi repo ve dal (EXP-006 D015 açıktı; A-07 birleştirme zamanı)? P5'in girişini belirler.
6. **Batu'nun hiyerarşi önerisi:** Aktör → aile → rol → motivasyon (EXP-006 U002-A) P2'nin tercih sorusu; cevap P2'nin rol sayısını ve dosya yapısını etkiler.
7. **P3'ün küçük sınaması:** Kurulum yapmadan hangi ölçüde temsil edicidir? `.claude/agents` yüklenmeden canlandırılan roller, gerçek yükleme davranışını sınamaz (ç). Bu yüzden sınama P5'in yerine geçmez.
8. **T4 soru kuyruğu ile açık soru kaydının tek kaynak ilişkisi:** Birleştirmede kesinleşmeli (§7.3).

### 11.2 Varsayımlar
- EXP-006'nın SOUL hedef tanımı ve altı kök işi P2 için girdi olarak kullanılabilir (V-P2-1). K-010 nedeniyle bağlayıcı değildir; P2 açılışında yeniden teyit edilir.
- Batu'nun EXP-006 kaynaklarındaki birebir sözleri, EXP-007'de niyet kanıtı olarak okunabilir (ç). Karar olarak kullanılan yerler §10'da teyide bağlandı.
- A-01'deki varsayım (AGENT.md kontrol katmanı olarak kalır) geçerlidir. S6 buna göre yazıldı.
- EXP-007'nin kendi işleyişi DevOS için öz-kanıt değeri taşır, bağımsız kanıt değildir (V-P3-2).

### 11.3 Bu taslak neyi kanıtlamıyor
- **Hiçbir mekanizmanın işe yaradığını.** Hiçbiri bu ortamda ya da başka bir yerde canlı sınanmadı. Kabul testleri tasarlandı, koşulmadı.
- **Haritanın doğru olduğunu.** Harita bir plandır. Aşama sayısı ve sırası kanıtla değil, Batu'nun sözleri, EXP-006 deneyimi ve genel yaşam döngüsü önerileriyle gerekçelendirildi. En zayıf halka P5 ve P6'dır: hedef konum, erişim ve canlı sınama koşulları bilinmiyor.
- **Kaynakların bağımsızlığını.** Kanıtların çoğu aynı asistanın notları (R01–R11), tedarikçi belgeleri (Anthropic; yazılım işi örnekleri), kaynağı okunmuş ama çalıştırılmamış ürünler ve aynı asistanın kavramsal analizleridir. Bağımsız ölçüm yoktur. "Keşfet → planla → uygula → commit"in tasarım işine uyarlanması çıkarımdır; Anthropic'in örnekleri kod üzerinedir.
- **Tam okumayı.** §0.2'de kısmi ya da okunmamış görünen kaynaklarda bu taslağı değiştirecek bilgi olabilir. En önemlileri: EXP-006 P2-01 (P2 için karşılaştırma girdisi), Foundation WORK ve INFORMATION sentezleri (doğrudan okunmadı; R04, R10 ve REUSE üzerinden kullanıldı), work-management-project-control paketi (R05 üzerinden).
- **Kümeler arası tutarlılığı.** T1, T2, T4 ve T5 taslakları bu yazılırken yoktu; arayüzler yalnız görev tanımlarına göre yazıldı. Bağımsız bir karşı-okuma P0.5'te yapılmalı.

