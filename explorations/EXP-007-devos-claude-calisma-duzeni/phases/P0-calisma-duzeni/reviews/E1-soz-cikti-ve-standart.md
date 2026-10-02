# E1 — Söz–çıktı izlenebilirliği ve standart seviye: METHOD v1 taslağının karşı-okuması

> **Tür:** P0.5 eleştiri turu, E1 · alt ajan çıktısı, model üretimi · 27 Eylül 2026 · okuma tabanı `a4844af` (dal `claude/hopeful-pascal-7bekcd`); incelenen metnin kendi tabanı `5e42216`.
> **Konum:** Taslağı çürütmeye çalışan eleştiri; yeniden yazım değil. Taslakla aynı modelden geldiğim için bu inceleme bağımsız doğrulama değil, taze gözle karşı-okumadır.

## Genel hüküm

- Taslak U004'teki hatayı **kapsam ve kart derinliği** düzeyinde tekrarlamıyor: kaynaklardan kendim çıkardığım 95 maddenin 67'si "nasıl" düzeyinde bir karta bağlı; açtığım 32 kartın hepsi somut; R07–R11 listeleri büyük ölçüde karşılanmış (Ek A, B, D).
- Hata iki katmanda **kısmen tekrar ediyor**. Eyleme dönüş dar: altı çekirdek yordam ve ana kapı betiği yazılmadı, hiçbir mekanizma koşmadı, düzen P0.8'de tek adımda etkinleşiyor (E1-04, E1-06). Beyan geniş: §10 "Karşılanmadı: 0" diyor, ben 3 daralma, 1 düşen söz ve 14 kısmi karşılık buldum (E1-03, E1-08, E1-13).
- Bütünsel en zayıf yer **frenler**: maliyet, bağlam ve takılma frenleri yalnız yapısal; emeklilik kuralı çalışan kapıları "sıfır ihlal" gerekçesiyle söktürebilir (E1-01, E1-02).
- Kritik bulgu yok; ama yedi önemli bulgu P0.6'da kapanmadan verilen kabul, Batu'nun deyişiyle "yeterli görünen" bir kabul olur.

**Bulgu sayıları:** kritik 0 · önemli 7 · küçük 6.

## Soru, kaynaklar, okuma kapsamı ve yöntem

**Soru (briefs/E1.md):** Batu'nun eleştirisi: "cevaplarında konuyu iyi anlamış gibi ifade ediyorsun ama iş aksiyona gelince o anlattıklarına göre sonuç çok daha dar kapsamlı oluyor" (U004). Bu taslak aynı hatayı tekrarlıyor mu? Alt sorular: (1) söylenenlerin karşılığı var mı ve "nasıl" düzeyinde mi; (2) standart seviye kontrol listeleriyle karşılaştırma; (3) ters yön, yani gereksiz ağırlık.

**Kısaltmalar.** Bütün yollar `explorations/EXP-007-devos-claude-calisma-duzeni/` altındadır. METHOD = `phases/P0-calisma-duzeni/METHOD-v1-TASLAK.md` · T1…T5 = `phases/P0-calisma-duzeni/drafts/T1-…` … `T5-…` · R07…R11 = `phases/P0-calisma-duzeni/research/R07-…` … `R11-…` · U003, U004, A003 = `sources/conversation/U003.md` vb. Bütün okumalar 27.09.2026 tarihlidir.

**Okuma kapsamı**
- **Tam:** `briefs/` ORTAK, ORTAK-SENTEZ, E-ORTAK, E1; METHOD (1–1514. satır, bütünü); U003, U004, A003.
- **Kısmi, hedefli:**
  - R07 §2: sekiz kontrol listesinin 60 madde başlığı; BY-8, BB-7, BS-4, BP-4 tam madde.
  - R08 §4: 27 madde başlığı; O1 tam madde.
  - R09 §1.5, §2.5, §3.5, §4.4, §5.4, §6.4: 58 madde başlığı; BA-1, BA-2, BA-5, MK-3, MK-7 tam madde.
  - R10: §3.5, §3.7, §4.10, §4.12, §5.6, §5.8, §8 tam.
  - R11: §1 tam; §3'teki 164 bileşenin adı ve "ne zaman gereksiz" sütunu; S1 tablosu tam.
  - T1: M7.1 ve M7.4 tam; M7.5, M7.8, M7.9, M8.6, M8.7 alan satırları; M9.8 "Kim" satırı.
  - T2: §2.7'deki yedi rol dosyasının başlık yapısı.
  - T3: MK-4.2, MK-4.3 alanları; P1 ve canlı denemeyle ilgili satırlar (grep).
  - T4: S2-M5 ve S15-M5'in seçili satırları.
  - T5: S18.1'in STATE satırları; S18.9 adımları; S19.4 hook tablosu; 5 saatlik limit satırları (grep).
- **Okunmadı:** R01–R06; R07–R11'in geri kalanı; U001, U002, U005, U006, A001, A002; DECISIONS.md, STATE.md; taslakların kanıt kayıtları; hook betik gövdeleri. Web kaynağı kullanılmadı.
- **Erişilemedi:** yok.

**Yöntem**
- Maddeleri U003, U004 ve A003'ten kendim çıkardım, sonra taslağa karşı eşledim; taslağın §10 matrisini ölçüt olarak kullanmadım. Tablo Ek A'dadır.
- Kontrol listelerinin her maddesini taslağın §3 standart seviye tablosuna ve kart dizinine eşledim; kuşkulu maddelerin tam metnini açtım (Ek B).
- Kart somutluğunu 13 taslak kartı ve METHOD'daki 19 MB kartında sınadım (Ek D).
- Zorlama düzeyini §5.1'in "Zorlama" sütunundan betikle saydım (Ek C).
- Kelime sayıları `wc -w` ile alındı; tablolar ve Markdown işaretleri dahildir.

**Kanıt dili:** kaynak diyor / gözledim / çıkarım / varsayım / bilinmiyor. "Gözledim", repodaki metni ya da komut çıktısını kendim okuduğum anlamına gelir.

## Bulgular

### E1-01 — Gaz mekanik, fren tavsiye: gözlenmiş maliyet kaymasına ve takılmaya karşı hiçbir fren zorlayıcı değil
- **Ciddiyet:** önemli.
- **Yer:** §0 "Frenler" ve "Zorlama"; MB-09; MB-10; MB-07 "Kurulmayanlar"; §3 S19 son satırı; §1 ilke 10.
- **Sorun:** Taslağın ilkesi, hook'un gözlenmiş bir kayma noktasına konmasıdır. Bu turda gözlenen en büyük kayma maliyet ve bağlam şişmesidir: T1–T5 ajan başına 21–39 M token işledi, tepe bağlam 620–734 K oldu, eski sayaç harcamayı eksik saydı. Buna rağmen %100'de durma, tepe bağlam sınırı, takılma alarmı ve sessiz alarm kuralı yalnız yapısaldır (ys). Eşiği koordinatör hesaplar, frene de koordinatör basar. Oysa frenin denetlediği aktör odur; R11'in "öz-onay" döngüsü burada kapanır. Go/stop ekseninde mekanik olan tek parça `durma-kapisi.sh`'tir: tur bitiş biçimini zorlar ve sessiz durmayı engeller. Eşik aşıldığında durmayı zorlayan hiçbir mekanizma yoktur. Dağıtım anında freni mekanik yapabilecek olay noktası PreToolUse Agent'tır; T1 ve T2 bunu istemişti. Taslak onu "hook sınırı ≤9" gerekçesiyle dışarıda bıraktı ve işlevinin "dönüşte BRIEF@sha ve TABAN alanlarıyla yakalandığını" yazdı. Bu, token harcandıktan sonraki bir tespittir, fren değildir. Aynı karar `gorev-dagitimi` skill'inin çağrılmasını da modelin seçimine bırakır; R08 O1'e göre isteğe bağlı skill çağrısı güvenilmezdir. Kendi koyduğu sayı sınırını bir bileşeni dışlamanın gerekçesi yapmak, Batu'nun "100 km" örneğinin biçimidir. Dışlamanın S20 freni ve S13 brief disiplini üzerindeki bütünsel etkisi yazılmamış.
- **Kanıt:**
  - METHOD MB-10: "**Kim:** ana oturum ölçer ve önerir ... **Zorlama:** ys; sert tavan zr; mekanik durdurucu yok." (gözledim)
  - METHOD MB-09: "tepe bağlam için zorlayıcı araç yok (`maxTurns` yalnız kaçak koruması)"; "T1–T5'in her biri 21–39 M token işledi ... tepe bağlam 620–734 K" (gözledim)
  - METHOD MB-07: "PreToolUse Agent kapısı (T1 ve T2 isteği) ilk pakette yok: hook sınırı ≤9 (S21.5) ve işlevi dönüşte BRIEF@sha ve TABAN alanlarıyla yakalanıyor" (gözledim)
  - METHOD §1 ilke 10: "Hook yalnız gözlenmiş bir kayma noktasına konur" (gözledim)
  - METHOD §5.1: S17-M2 ve S17-M3 "ys"; MB-15: "Tur sonu: `durma-kapisi.sh` yetkili iş varken turu bitirtmez." (gözledim)
  - R09 MK-3: "durdurma ya da park eşik aşımında zorunludur ... *Gerçekten gereksiz:* Yok." (kaynak diyor; studies derlemesi)
  - R08 §4 O1: "İsteğe bağlı katman güvenilmez: "Agents often skip retrieval they have to choose". Aktarılan denemede beceri vakaların %56'sında hiç çağrılmadı [BM5]." (kaynak diyor; topluluk pratiğinin aktardığı ölçüm)
  - U004: "hızlı gitmesi engellenmesin diye fren koymadığın ortaya çıkıyor" (kaynak diyor)
  - Dağıtım anındaki hook'un bu sürümde bütçe ve brief bilgisini okuyabileceği (çıkarım; canlı sınanmadı).
- **Öneri:**
  - PreToolUse Agent kapısı ilk pakete alınsın. Kapı şunları denetlesin: brief dosyası commit'li mi, DAGITIM satırı yazılmış mı. Aşama bütçesi %100'ü geçtiyse ya da 24 saattir cevapsız kırmızı alarm varsa yeni dağıtımı reddetsin ("DURAK: bütçe" ve sessiz alarm kuralı). Harcama hook'ta ölçülemiyorsa GUNLUK'taki son "Maliyet" satırı ya da dalga başına DAGITIM sayısı vekil olsun.
  - Hook sayısı sınırı korunacaksa, olay dayanağı zayıf bir hook'la yer değiştirsin (E1-02) ya da sınır gerekçesiyle 10'a çıksın.
  - Sayı sınırı bir bileşeni dışlamak için kullanılıyorsa, dışlanan bileşenin bütünsel etkisi yazılsın.
  - Pilota "eşik aşıldı ama durulmadı" senaryosu eklensin.

### E1-02 — Emeklilik kuralı ve hook kaldırma koşulları hava yastığını söktürebilir
- **Ciddiyet:** önemli.
- **Yer:** §11.4; MB-07 (kaldırma koşulları Ek T5 S19.4'te); §1 ilke 10; §0 "Zorlama".
- **Sorun:** Taslak üç kuralı yan yana koyuyor. Birincisi: hiç tetiklenmeyen hook kaldırma adayıdır. İkincisi: iki aşama sıfır değer gösteren mekanizma kaldırılır. Üçüncüsü: "son zamanlarda bir şey bozulmadı" gerekçe sayılmaz. Ek T5 S19.4'teki kaldırma koşulları ilk ikisine göre yazılmış: `donus-kapisi.sh` "şema ihlali iki aşama boyunca 0" olunca, `alt-ajan-tabani.sh` "taban kaynaklı sorun 0" olunca kalkar. Ama kapı çalıştığı için ihlal ve sorun sıfır görünür; ölçü, frenin işe yaradığını frenin gereksizliği diye okur. Bu, Batu'nun "100 km gidilecek diye" örneğinin zaman içindeki biçimidir. Ayrıca §0 ve ilke 10, hook'ların "yalnız gözlenmiş kayma noktalarında" olduğunu söylüyor. T5'in kendi tablosunda ise `uzak-arac-siniri.sh` bir kabiliyet gözlemine ("Alt ajanlarda Remote araçları"), `hata-kaydi.sh` bir riske ("Limit riski") bağlı. `bash-kapisi.sh`'in sır taraması da bir olaya değil bir riske dayanıyor. Bu korkuluklar standart seviyede doğrudur; güvenlik olay beklemez. Ama ilkenin metni onları dışlıyor, emeklilik kuralı da onları söktürüyor.
- **Kanıt:**
  - METHOD §11.4: "Emeklilik kuralı: iki aşama sıfır değer gösteren ya da önlediği hata başka yolla imkânsız hale gelen mekanizma kaldırılır. "Son zamanlarda bir şey bozulmadı" gerekçe sayılmaz." ve "Hiç tetiklenmeyen ya da hep yanlış engelleyen hook kaldırma adayıdır (MB-07)." (gözledim)
  - T5 S19.4 tablosu: `donus-kapisi.sh` → "Şema ihlali iki aşama boyunca 0 ise"; `alt-ajan-tabani.sh` → "İki aşama boyunca taban kaynaklı sorun 0 ve görev tanımına taban alanı yerleşmişse"; `uzak-arac-siniri.sh` → bağlı risk "Alt ajanlarda Remote araçları [R11 K24]"; `hata-kaydi.sh` → "Limit riski [R11 K22]" (gözledim)
  - METHOD §0: "dokuz hook yalnız gözlenmiş kayma noktalarında" (gözledim)
  - U004: "sadece 100 km gidilecek diye arabayla, koltukta masaj olmamasına gerek yok diye bir karar yeterli seviye değil yetersiz seviye olarak görülmeli" (kaynak diyor)
  - Engelleyen bir kapıdaki sıfır ihlal kapının etkisidir; kapının gereksizliğini göstermez (çıkarım).
- **Öneri:**
  - Hook'lar iki sınıfa ayrılsın. Süreç kapıları olay dayanaklı olsun; kaldırılmaları yalnız "önlediği hata başka yolla imkânsız" dalıyla olsun. Güvenlik korkulukları (yazma sınırı, uzak araç sınırı, yıkıcı işlem, sır taraması) olay beklemesin; sıfır tetik onlar için kaldırma gerekçesi sayılmasın.
  - Bir kapının "değer" ölçüsü, engellediği girişim sayısını ve önlediği hatanın bedelini içersin. "İhlal 0" tek başına kaldırma koşulu olmasın.
  - İlke 10 ve §0'daki cümle buna göre düzeltilsin.

### E1-03 — "Karşılanmadı: 0" iddiası tutmuyor: daralan ve düşen sözler "kart var" diye etiketli
- **Ciddiyet:** önemli.
- **Yer:** §10 başlığı ve satırları; §2 P1 çıkış ölçütü.
- **Sorun:** Batu'nun U004 eleştirisinin doğrudan ölçüsü bu matristir. Maddeleri kendim çıkarıp karşılaştırdım (Ek A); tasarımın kapsamı geniş, ama matrisin etiketleri beş yerde daralmayı gizliyor. (a) A003 §3.8'deki "P1'in yarısı canlı deneme olmalı" sözü matriste yok; §2'deki P1 çıkış ölçütü, "denenemedi + neden + etkisi" yazılarak sıfır canlı denemeyle kapanmaya izin veriyor, oysa aynı bölüm "P1 ... canlı denemeyle kapanır" diyor. (b) A003 §6 soğuk başlangıç için "Cevap senin niyetinle karşılaştırılır" dedi; MB-16'da beklenen cevapları koordinatör yazıyor ve puanlıyor (E1-05), satırın düzeyi ise "kart var". (c) A003 §3.4 okuma kaydını "her okuma için" vaat etti; MK-6.3'te kayıt "yalnız karar taşıyan okuma"ya indi. Y14 gerekçesi var, ama düzey "bilerek değiştirildi" değil "kart var". (d) U004-8 ("nasıl") "kart var" etiketli; oysa altı skill'in metni ve ana hook betiği yok (E1-04), matrisin kendi tanımına ("mekanizma kartı ve şablonu yazılı") göre bu "kısmen"dir. (e) U003'te Batu dal birikmesini istemedi ve bu işi Claude'a verdi; taslak dal silmeyi Batu'ya veriyor (E1-11), satır yalnız "askıda" diyor. Farklar tek tek küçük, ama matris "0 karşılanmadı" deyince Batu'nun tam da aradığı daralmayı görmesi zorlaşıyor: U004'teki hata beyan katmanında tekrar ediyor.
- **Kanıt:**
  - METHOD §10: "**Karşılanmadı: 0 madde.**" (gözledim)
  - A003 §3.8: "P1'in yarısı canlı deneme olmalı." (kaynak diyor). METHOD §10.3'ün §3.8 satırı: "ölçüt önce; katlar; kanıt gücü; "kimseye verilmemiş iş"; risk orantılı kontrol" ("yarısı" yok; gözledim)
  - METHOD §2 P1 satırı: "asgari deneme seti koşuldu ya da "denenemedi + neden + etkisi" yazıldı"; aynı bölümde: "P1 belge taramasını tekrarlamaz, canlı denemeyle kapanır" (gözledim)
  - A003 §6: "Cevap senin niyetinle karşılaştırılır." (kaynak diyor). METHOD §10.3: "§6 | soğuk başlangıç testi | MB-16 | kart var" (gözledim)
  - A003 §3.4: "Okuma kaydı: her okuma için şunlar yazılır" (kaynak diyor). METHOD §10.3: "MK-6.3 (yalnız karar taşıyan okumada; Y14) | kart var" (gözledim)
  - METHOD §10 düzey tanımı: "**kart var** (mekanizma kartı ve şablonu yazılı; hiçbiri canlı sınanmadı)"; U004-8 satırı: "kart var; altı skill'in tam metni yok" (gözledim)
  - U003: "branchların birikmesini istemiyorum" (kaynak diyor). METHOD §12.2 K-8: "eski dalları Batu siler" (gözledim)
- **Öneri:**
  - Matrise "daraldı (gerekçe)" düzeyi eklensin ve yukarıdaki beş satır yeniden etiketlensin.
  - A003 §3.8'deki "yarısı" ölçüsü ya P1 çıkış ölçütüne konsun (ör. yük taşıyan kabiliyetlerin en az yarısı canlı denemeyle) ya da gerekçesiyle "bilerek değiştirildi" yazılsın.
  - "Karşılanmadı: 0" cümlesinin yerine "karşılanmadı / daraldı / askıda" sayıları verilsin. Bu sayılar §0'a ve kabul paketine taşınsın.

### E1-04 — "Nasıl"ın eyleme dönen katmanı eksik: çekirdek döngünün altı yordamı ve ana kapı betiği yazılmadı
- **Ciddiyet:** önemli.
- **Yer:** §12.3; §14.1 R-6; §0 madde 4; §10.2 U004-8; MB-07'deki `yazma-siniri.sh` kuralı.
- **Sorun:** Kartların çoğu "nasıl" düzeyinde (Ek D). Ama kartları eylem anında yükleyecek taşıyıcıların önemli bir kısmı yok. W2 döngüsünün iki ucunun (`gorev-dagitimi`, `donus-alma`) skill metni yok. Aşama kapısının (`asama-kapanisi`), ders kaydının, yöntem değişikliğinin ve soğuk başlangıç testinin skill metinleri de yok. En çok kolu taşıyan `bash-kapisi.sh` yazılmadı. Hook gövdeleri okunmadı ve hiçbiri çalıştırılmadı. Taslak bu değişikliklerden birini metinsiz yapmış. `yazma-siniri.sh`'in alt ajan kuralı, T5'teki "yalnız `phases/` altında yeni dosya"dan "yalnız brief'teki ÇIKTI yolunda yeni dosya"ya çevrildi. Betiğin bir yazma çağrısını hangi brief'e eşleyeceği (alt ajan kimliği → DAGITIM satırı → ÇIKTI yolu) yazılmadı. Taslak bunları §12.3 ve §14'te dürüstçe söylüyor. Ama Batu'ya "yeter" denen §0, "10 skill, 9 hook ... P0.8'de tek commit'le kurulur" diyor ve eksik metinden söz etmiyor. Taslağın ilke 3'ü ("Kalıcı olan, yüklenmedikçe işe yaramaz") bu eksiği doğrudan adlandırıyor.
- **Kanıt:**
  - METHOD §12.3: "`gorev-dagitimi/`, `donus-alma/`, `ders-kaydi/`, `asama-kapanisi/`, `yontem-degisikligi/`, `soguk-baslangic-testi/` | ... | **metin yok**"; "`.claude/hooks/*.sh` (9) | ... | birleşik `bash-kapisi.sh` yazılmadı; betik gövdeleri bu adımda okunmadı" (gözledim)
  - METHOD §14.4: "Hiçbir mekanizma canlı sınanmadı." (gözledim)
  - METHOD §0 madde 4: "kök CLAUDE.md, 8 rol dosyası, 10 skill, 9 hook ve izin kuralları; P0.8'de tek commit'le kurulur" (gözledim)
  - T5 S19.4: "Alt ajan: yalnız `phases/` altında yeni dosya, tek Write, Edit yok"; METHOD MB-07: "alt ajan: yalnız brief'teki ÇIKTI yolunda yeni dosya" (gözledim)
  - METHOD "Bu metin hakkında": "Betikle çıkarılan: beş taslağın bütün kartlarının "Ne, Ne zaman, Kim, Zorlama düzeyi" alanları ... kısaltılmış olarak" (gözledim)
  - Hook girdisinde alt ajan kimliğini taşıyan bir alan bu sürümde var mı: bilinmiyor. §14.2 madde 15 iki farklı sürüm numarası kaydediyor (gözledim).
- **Öneri:**
  - P0.6'nın çıkış koşulu şu olsun: altı skill ve `bash-kapisi.sh` yazıldı, bir eleştiriden geçti ve en az bir kuru koşuda çalıştı. Kuru koşu kurulum gerektirmez: betiğe örnek JSON girdisi verilir.
  - §0 madde 4'e "6 skill ve 1 betik henüz yazılmadı" satırı eklensin.
  - `yazma-siniri.sh`'in eşleme yolu (hangi girdi alanıyla, hangi dosyadan) karta yazılsın. Bu yol kurulamıyorsa T5'in basit kuralına dönülsün.

### E1-05 — Soğuk başlangıç testi aynı modelin kendi anahtarıyla puanlanıyor; A003'ün "senin niyetinle" sözü ve T1'in denetimi düştü
- **Ciddiyet:** önemli.
- **Yer:** MB-16; §2 P0 çıkış ölçütü ("soğuk başlangıç geçti"); §10.3'teki A003 §6 satırı; BK-21.
- **Sorun:** A003 soğuk başlangıcı sürekliliği ölçmenin "dürüst yolu" olarak önerdi ve cevabın Batu'nun niyetiyle karşılaştırılacağını söyledi. Taslakta beklenen cevapları ana oturum yazıyor, puanlamayı da ana oturum yapıyor. T1 M7.9'daki "T4 denetler" birleştirmede kayboldu ve BK-21 bunu kaydetmiyor. Bu test P0'ın çıkış ölçütüdür. Taslağın ilke 9'u "doğrulandı" sözünü aynı modelin okumasına vermiyor ve Batu'yu tek farklı denetçi sayıyor. Buna rağmen sürekliliğin tek bağımsız sınaması, anahtarı ve puanı aynı elde olan bir koşuya dönüşüyor; R11'in öz-onay döngüsü burada kapanıyor. Batu'nun bu işe katılmasının bedeli çok küçüktür: dört cevap, 300 kelimenin altında. Bu küçük bedelden kaçınmak, bir konfor seçiminin güvenliği zayıflatmasıdır.
- **Kanıt:**
  - A003 §6: "Bu konuşmayı hiç görmemiş taze bir oturuma yalnız repo verilir ve dört şey sorulur ... Cevap senin niyetinle karşılaştırılır." (kaynak diyor)
  - METHOD MB-16: "beklenen cevaplar önceden scratchpad'de"; "ana oturum başlatır ve puanlar" (gözledim)
  - T1 M7.9: "puanlamayı ana oturum yapar, T4 denetler." (gözledim)
  - T5 S18.9: "Ana oturum beklenen cevapları testten **önce** repo dışına, scratchpad'e yazar." (gözledim)
  - METHOD §1 ilke 9: ""Doğrulandı" aynı modelin okumasına verilmez. Aynı modelden olmayan tek denetçi Batu'nun dikkatidir" (gözledim)
  - R10 §4.10 soru 11: "Bu, gerçekten bağımsız bir oturumla sınandı mı?" (kaynak diyor)
- **Öneri:**
  - P0 sonunda taze okuyucunun dört süreklilik cevabı (≤150 kelime) kabul paketine birebir konsun. Batu tek satırla "niyetime uyuyor / uymuyor" desin.
  - Öteki aşama sonlarında puanlamayı, anahtarı ve cevapları gören `e7-elestirmen` (B2) yapsın; T1'deki denetim geri gelsin.
  - Değişiklik BK kaydına eklensin.

### E1-06 — Ters yön: birleştirme hiçbir kartı çıkarmadı, sınırlar tasarımın sayısına eşit, etkinleştirme tek adımda
- **Ciddiyet:** önemli.
- **Yer:** §5.1 sayım satırı; §11.2 yüzey sınırları; §12.1 O-4; §13.2 pilot kapsamı; §13.3.
- **Sorun:** ORTAK-SENTEZ hem "daha basiti yeter" yaklaşımını hem "her şeyi koru" yaklaşımını reddediyor. R11 §1 madde 6 da "hiç koşulmamış töreni önceden inşa etme" uyarısını aktarıyor. Taslak ise beş paralel taslağı birleştirirken tek kart çıkarmadı: 157 kartın 97'si aynen kaldı. Ağırlık sınırları tasarımın kendi sayısıyla aynı (en çok 9 hook ve 9 hook; en çok 10 skill ve 10 skill); sınır yalnız bir hook'u dışarıda bıraktı (E1-01). O-4'te T4'ün aşamalı sırası yerine dokuz hook'un birlikte kurulması öneriliyor. §6 mimarisi, göç, 8 rol ve 10 skill de aynı commit'te kuruluyor. Pilotlar 18 kartı ve ortak sözleşmenin §7'sini, kurulu yapılandırma olmadan sınıyor; dizinde 157 kart var. Kurulu bütün P0.8'de yalnız mekanik denemelerden (CD) ve soğuk başlangıçtan geçiyor, gerçek bir işte ilk kez P1'de çalışıyor. Hafiflik dengeleyicilerinin çoğu (hook değer incelemesi, rol sayısı gözden geçirmesi, eşik kalibrasyonu) "iki aşama sonra" devreye giriyor. Tek adımlı etkinleştirme taslağın kendi MK-3.7 kartıyla ("Yeni şablon ya da rol önce tek kalemde") ve R07 BO-6 ile çelişiyor. Bu, "standart seviye fazla" eleştirisi değildir; kartların çoğu gerekli olabilir. Sorun, hangi kartın ne zaman etkin olacağının olaya ve sıraya bağlanmadan topluca belirlenmesidir.
- **Kanıt:**
  - METHOD §5.1: "Sayım: 157 kart; 97 aynen, 31 değişti, 29 birleşti; çıkarılan kart yok." (gözledim)
  - METHOD §11.2: "skill ≤10, her biri ≤120 satır · hook ≤9"; §12.3'te 10 skill ve 9 hook (gözledim)
  - METHOD §12.1 O-4: "b) T4'ün sırası: önce dönüş, açılış ve commit kapıları (Z1, Z2, Z4, Z5), durma kapısı ve sıkıştırma kolu (Z3, Z6) pilottan sonra"; önerim: "a, kaldırma koşullarıyla" (gözledim)
  - METHOD §13.2: Pilot-1'de 10 kart; Pilot-2'de 8 kart ve "ortak sözleşme §7"; §13.3: "İki aşama sonra | Hook değer incelemesi ..., rol sayısı gözden geçirmesi (MB-18), eşik kalibrasyonu" (gözledim)
  - R11 §1 madde 6: "Defo modeli "hiç koşulmamış töreni önceden inşa etme" diyor [K33]." (kaynak diyor)
  - R07 BO-6: "Önce küçük dilim, sonra hepsi." (kaynak diyor; tedarikçi belgesi)
  - METHOD §5.1 MK-3.7: "Yeni şablon ya da rol önce tek kalemde" (gözledim)
- **Öneri:**
  - Kartlar kaldırılmasın; her karta bir "etkinleşme" alanı eklensin: kurulumda etkin / ilk kullanımda tek kalemde denenir (MK-3.7) / olay tetikli.
  - Hook'larda O-4 (b) sırası seçilsin; güvenlik korkulukları (E1-02) ilk pakette kalsın.
  - Ağırlık sınırları tasarımdan bağımsız bir dayanakla yeniden yazılsın (ör. K0 bütçesi ya da ölçülen açılış maliyeti).
  - Pilot başarı ölçütlerine iki sayı eklensin: etkin olmayan ama gereken kart, etkin olan ama kullanılmayan kart.

### E1-07 — Taslak ilk uygulandığı yerde kendi dikkat bütçesini aşıyor
- **Ciddiyet:** önemli.
- **Yer:** §0 ("Senin rolün", "Senden istenen kararlar"); başlıktaki "Okuma yolu"; §11.2 "Batu'nun dikkati"; §12.
- **Sorun:** Taslak Batu'ya "Aşama başına okuman gereken metin yaklaşık 1.500 kelimenin altında kalır" diyor ve kontrol noktası başına en çok 3 önerili soru koyuyor. Aynı taslak, karar için §0, §2, §12, §13 ve §14'ün okunmasını istiyor; bu bölümler yaklaşık 4.600 kelimedir. §0'da yedi karar grubu, §12'de on sekiz madde (O-1…O-8, K-1…K-10) ve altı Batu eylemi var. Bunların bir kısmı çerçeve ve erişim sorusu olarak sınır dışı sayılabilir, ama tercih niteliğindekiler (ör. K-2, K-5…K-9, O-7) üçü aşıyor. Kabul nesnesi 31 bin kelimelik, 157 kartlık bir metin; taslağın kendi S2-M4 satırı bu durumun riskini "kabul törene döner" diye adlandırıyor. R11 §1 madde 2'ye göre Batu'nun dikkati sistemin aynı modelden olmayan tek denetim kanalıdır; Batu'nun konfor ile güvenlik arasında kurduğu bağın bu sistemdeki karşılığı budur. P0'ın istisna sayılması makul olabilir, ama istisna yazılmamış ve §0'daki söz metnin kendisiyle çelişiyor. "Cevapsız kalırsa son sütun geçerli" kuralı iyi bir hafifleticidir, ama okuma yükünü azaltmıyor.
- **Kanıt:**
  - METHOD §0: "Aşama başına okuman gereken metin yaklaşık 1.500 kelimenin altında kalır." (gözledim)
  - METHOD başlığı: "Karar için §0, §2, §12, §13, §14." `wc -w` ile: §0 530, §2 607, §12 2.153, §13 665, §14 661 kelime; bütün metin 31.421 kelime (gözledim)
  - METHOD §11.2: "kontrol noktası başına ≤3 soru, her biri önerili; ... aşama başına ≤1 onay paketi" (gözledim)
  - T4 S2-M5: "Okuması gerekenler: aşama raporu ve kabul paketi (aşama başına en fazla 2 sayfa)" (gözledim)
  - METHOD §3, S2 satırı (S2-M4): "kabul törene döner; Batu teknik doğrulayıcı olur" (gözledim)
  - R11 §1 madde 2: "Bu yüzden Batu'nun dikkati bugün sistemin tek "aynı model olmayan" denetim kanalıdır." (kaynak diyor)
  - U004: "konfor kullanıcının rahatlamasını, ağrısının olmamasını ve dolayısıyla daha güvenli sürüşü sağlar" (kaynak diyor)
- **Öneri:**
  - P0 istisnası ve sınırı açıkça yazılsın.
  - Batu'nun zorunlu okuması 1.500 kelimenin altında bir kabul paketine insin. Paket şunları içersin: kabul edilen nesne (@SHA); bilinen açıklar ve daralmalar (E1-03); en çok 3 tercih sorusu; geri kalan kararlar varsayılanlarıyla tek tabloda.
  - §0'daki söz P0 dahil ölçülüp aşama raporunda gösterilsin.

### E1-08 — L-001'in "doğrulandı" etiketi taslağın kendi doğrulama sözlüğünü aşıyor
- **Ciddiyet:** küçük.
- **Yer:** MB-17 örneği; W10 adım 5; §10.3 (A003 §3.10 satırı); BK-01; §14.4.
- **Sorun:** §4.1'e göre "doğrulandı" yalnız B3 ve üstünde kullanılır: B2 taze bağlam ve gerekçeyi görmeme ister, B3 buna ayrı bir kanıt yolu ekler. L-001'in kontrolünü birleştirmeyi yapan ajanın kendisi `git log` ile yaptı; bu, B0 artı mekanik gözlemdir. Tek bir fırsat (bir dalga) gözlendi ve kural o dalganın görev tanımında açıkça yazılıydı. R10 §8, "ders yazıldı ≠ yüklendi ≠ kullanıldı ≠ davranış değişti ≠ korundu ≠ yararlı oldu" ayrımını birleştirilmemesi gerekenler arasında sayıyor. MB-17'nin statü merdiveni bu basamakları "doğrulandı"da topluyor. L-001 Batu'ya taslağın tek canlı doğrulama örneği olarak sunulduğu için etiketin doğruluğu önemlidir.
- **Kanıt:**
  - METHOD §4.1: ""Doğrulandı" kelimesi yalnız B3 ve üstünde kullanılır." (gözledim)
  - METHOD MB-17: "sonuç: T1–T5'in beşi tek commit'le ve tam boyuyla girdi ... → **doğrulandı (gözlem, 27.09.2026)**" (gözledim)
  - R10 §8: "ders yazıldı ≠ yüklendi ≠ kullanıldı ≠ davranış değişti ≠ korundu ≠ yararlı oldu" (kaynak diyor)
  - R10 §4.10 soru 9: "Kanıt, sınamanın kendisinin öğretmediği bir yoldan mı elde edildi?" (kaynak diyor)
  - `briefs/ORTAK-SENTEZ.md` Kurallar: "**Çıktı dosyasını tek seferde yaz.**" (gözledim; kural gözlenen dalganın brief'indeydi)
- **Öneri:** L-001 "yürürlükte; kullanıldı (1 fırsat; B0 + git gözlemi)" olarak yazılsın. MB-17'nin statüleri R10 §8'in basamaklarıyla (yüklendi / kullanıldı / korundu) hizalansın. "Doğrulandı" yalnız §4.1'deki anlamında kalsın.

### E1-09 — Koordinatörün bağlam bütçesi yetkili metinde yok; K0 bütçesi gerekçesi yazılmadan üçe çıktı
- **Ciddiyet:** küçük.
- **Yer:** MB-09 bütçe listesi; BK-07; §3'teki S7 satırı "Koordinatörün kendi doluluğunu görmesi".
- **Sorun:** Taslak "bir taslakla çelişirse bu metin geçerlidir" diyor ve MB-09'u bağlam bütçelerinin tek yeri yapıyor. Listede alt ajan ve açılış bütçeleri var, koordinatörün bütçesi yok. T1 M7.4'teki "iş kalemi başına doğrudan kaynak okuması yaklaşık 30 KB" sınırı yalnız §11.2'de dolaylı geçiyor ("Dönüş ... ≤30 KB okuma"). Ölçüm (CD-10) P1'e bırakılmış; oysa ana oturum bu oturumda 792 K'da sıkıştırıldı. R09 BA-5 ve MK-7, koordinatör bağlamının izlenmesini "gerçekten gereksiz: yok" diye işaretliyor. Ayrıca T1'in "toplam K0 ≤10 KB" sınırı MB-09'da 30 KB oldu; bu sırada K0'ın tanımı da genişledi (skill ve rol açıklamaları eklendi). BK-07'nin yazılı gerekçesi alt ajanların tepe bağlamıdır; K0'daki artışı açıklamıyor.
- **Kanıt:**
  - METHOD MB-09 "Bütçeler" satırı: koordinatör kalemi yok (gözledim)
  - T1 M7.4: "ana oturumun doğrudan kaynak okuması ≈ 30 KB'ı geçmez" (gözledim)
  - T1 M7.1: "toplam K0 ≤ 10 KB" (gözledim); METHOD MB-09: "K0 (...) ≤30 KB"; BK-07 gerekçesi: "Ölçülmüş olay: tepe 620–734 K" (gözledim)
  - R09 BA-5: "koordinatörün bağlam kullanımının izlenmesi"; MK-7: "*Gerçekten gereksiz:* Yok." (kaynak diyor)
  - METHOD §11.1: "Ana oturum | 792 K'da sıkıştırıldı (%80; pencere ≈1 M)" (gözledim)
- **Öneri:** MB-09'a koordinatör kalemi eklensin: kalem başına yaklaşık 30 KB doğrudan okuma, dönüş başına en çok 30 KB. CD-10'a kadar bir vekil ölçü tanımlansın; ör. oturum başına işlenen dönüş sayısı ya da `tools/token-kullanimi.py` ile oturum ortasında ölçüm. K0 artışının gerekçesi BK-07'ye yazılsın.

### E1-10 — İki "bilinmiyor" satırının kabul testi, planda olmayan bir pilota bağlı
- **Ciddiyet:** küçük.
- **Yer:** §3'te S14 "Farklı model ya da sağlayıcıdan doğrulayıcı" ve S12 "Dinamik workflow" satırları; §13.
- **Sorun:** Farklı model doğrulayıcının "pilotta maliyet ve fayda" ile, dinamik workflow'un "pilotta bir doğrulama dalgası" ile sınanacağı yazılmış. §13'teki pilotlar ve erken denemeler ikisini de içermiyor. Ayrıca §4.1 B4'ü "bu ortamda yok" diye tanımlıyor. O zaman ilk satırın durumu "bilinmiyor" değil "ortamda yok"tur. Bunun bütünsel etkisi satıra yazılmalıdır: öz-onay döngüsünde Batu tek farklı denetçi kalır ve R-4 riski kabul edilmiştir. Bu satırın "önlediği hata" sütunu da "—".
- **Kanıt:**
  - METHOD §3: "S14 | Farklı model ya da sağlayıcıdan doğrulayıcı | bilinmiyor | — | pilotta maliyet ve fayda | §14" ve "S12 | Dinamik workflow | bilinmiyor | ... | pilotta bir doğrulama dalgası | M12.1" (gözledim)
  - METHOD §4.1: "B4 farklı model ailesi (bu ortamda yok)" (gözledim)
  - METHOD §13.2: pilot ve erken deneme listelerinde bu iki sınama yok (gözledim); §14.1 R-4: "Kalan risk kabul edilir" (gözledim)
- **Öneri:** Ya iki sınama §13'e eklensin ya da satırlar gerçek durumlarıyla yeniden yazılsın. Farklı model satırı için kısmi ikameler ve maliyetleri değerlendirilsin: farklı Claude katmanı ve koşulabilir betik kontrolü.

### E1-11 — Dal silme, "aynen" diye işaretli bir kartta sessizce Batu'ya geçti
- **Ciddiyet:** küçük.
- **Yer:** §5.1'deki M9.8 satırı; §12.2 K-8; §10.1 U003-2.
- **Sorun:** T1 M9.8'de dal silmeyi ana oturum, Batu'ya haber vererek yapıyordu. Kart dizininde M9.8 "aynen" görünüyor, ama sahip alanı "dal silme Batu" olmuş; K-8 de "eski dalları Batu siler" diyor. Batu U003'te dal birikmesini istemediğini söyledi ve bu işi açıkça Claude'a verdi. A003 §3.2 de "Mesaj taşımazsın" diyordu. Değişikliğin BK kaydı ve gerekçesi yok. Ortamın uzak dal silmeye izin vermemesi gibi bir kısıt varsa, o da yazılmamış. Bu, R-7'nin tarif ettiği "farkında olmadan ezilme" türünden bir değişikliktir.
- **Kanıt:**
  - T1 M9.8: "Dal silme ve PR kararları Batu'ya haber verilerek yapılır." (gözledim)
  - METHOD §5.1: "M9.8 | ... | ana oturum; dal silme Batu | zr (proxy) | yerel = uzak | T1:1162 | aynen" (gözledim)
  - U003: "Main'i birleştirmeyi sen yap. main ile birleştirilem branch zaten siliniyormuş. branchların birikmesini istemiyorum." (kaynak diyor)
  - T5, satır 1701 (madde 7, "Dal politikası"): "silmeyi Batu yapar" (gözledim)
- **Öneri:** Karar BK kaydına alınsın. Teknik bir kısıt varsa kanıtıyla yazılsın; yoksa T1'in kuralı geri gelsin ve Batu'ya yalnız bildirim gitsin.

### E1-12 — Hook'suz açılışta okuma sırası düz yazı "oku" talimatına kalıyor ve STATE listede yok
- **Ciddiyet:** küçük.
- **Yer:** §12.4 CLAUDE.md §2 adım 3; MB-06'nın kaynak satırı; §10.3 (A003 §3.9 satırı).
- **Sorun:** CLAUDE.md §2 okuma sırasının "tek yeri" olduğunu söylüyor, ama listede STATE.md yok. STATE ya SessionStart enjeksiyonuyla ya da `oturum-acilis` skill'indeki `sed` komutuyla geliyor. Çok repolu oturumda ve kurulum doğrulanana kadar hook yok; skill'in çağrılması da düz yazı bir talimat. R07 BB-7 tam bu durumu anlatıyor. MB-06 kaynak olarak BB-7'yi gösteriyor, ama onu hook'suz yolda uygulamıyor. Matris A003 §3.9'daki okuma sırasını ("CLAUDE.md, AGENT.md, durum dosyası, harita") "kart var" diye işaretliyor.
- **Kanıt:**
  - METHOD §12.4, CLAUDE.md §2 adım 3: "`E7/README.md` → `E7/DECISIONS.md` → `E7/PLAN.md` ... → `GUNLUK.md` son 30 satır" (gözledim)
  - T5 S18.1: `sed -n '/<!-- DEVIR-BASLA -->/,/<!-- DEVIR-BITIR -->/p' .../STATE.md` (gözledim)
  - R07 BB-7: "A `CLAUDE.md` that tells Claude in words to read `AGENTS.md`: Claude sees `AGENTS.md` only if it decides to open the file." ve "Yokluğunda: A003 §3.9'daki okuma sırası ... yalnız istek olarak kalır." (kaynak diyor; tedarikçi belgesi)
- **Öneri:** STATE.md okuma sırasının başına yazılsın. Hook'suz yol için devir bloğunun küçük bir dosyada tutulup CLAUDE.md'ye `@` ile içe aktarılması, K0 bütçesi içinde değerlendirilsin. CD-01'e "kanaryasız açılışta STATE okundu mu" gözlemi eklensin.

### E1-13 — "zr" etiketleri koşullu zorlamayı koşulsuz gösteriyor
- **Ciddiyet:** küçük.
- **Yer:** §0 "Zorlama"; §5.1'in lejandı ve "Zorlama" sütunu; MB-03.
- **Sorun:** Lejand "zr" için "zorlayıcı (her oturumda)" diyor. "zr" taşıyan 15 kartın dökümü şöyle (Ek C): 4'ü ortamın kendi mekanizması (Stop hook'u, proxy); 8'i rol dosyasındaki araç ya da model alanına dayanıyor ve rol dosyalarının yüklenmesi PS-2'ye bağlı, yani bilinmiyor; 2'si Batu'nun ortam penceresinde yapacağı eşzamanlılık ayarına (O-8) bağlı; 1'i izin kuralı ve ortam değişkeni (S19.5). MB-03'te rol belleğine yazma yasağı "zr (rollerin yazma yolu `memory/`'yi içermez)" diye etiketli. Oysa araç listesi Write'ı yol sınırı olmadan veriyor; yol sınırını yalnız `yazma-siniri.sh` koyuyor, bu da zr¹ demektir. §0'daki "rollerin araç listeleri her oturumda geçerli" cümlesi PS-2 koşulunu taşımıyor. R10 §8'e göre "rol metni ≠ yetki ≠ zorlama ≠ uyum".
- **Kanıt:**
  - METHOD §5.1 lejandı: "zr zorlayıcı (her oturumda) · zr¹ zorlayıcı yalnız tek repolu oturumda" (gözledim)
  - METHOD MB-03: "**Zorlama:** yazma zr (rollerin yazma yolu `memory/`'yi içermez)"; §4.1: `e7-okuyucu` araç özeti "okuma, Bash, Write" (gözledim)
  - METHOD §0: "Zorlama: rollerin araç listeleri her oturumda geçerli" (gözledim); §14.1 R-2: "Yapılandırma yüklenmez: dal dışında açılan oturum, başlangıçta olmayan `.claude/agents` ..." (gözledim)
  - R10 §8: "rol metni ≠ yetki ≠ zorlama ≠ uyum" (kaynak diyor)
- **Öneri:** Lejanda "zr (PS-2 koşullu)" ve "ortam" ayrımları eklensin. MB-03'teki yazma yasağı zr¹ olarak düzeltilsin. §0'daki cümleye koşul eklensin.

## Ek A — Söz–çıktı tablosu (maddeler kaynaklardan bağımsız çıkarıldı)

**Düzeyler:**
- **nasıl:** şablonu, tetiği, sahibi ve kontrolü olan kart var.
- **bilerek değiştirildi:** söz gerekçeyle değiştirildi.
- **karşılandı (Batu):** Batu'nun kabulüyle kapandı.
- **kısmen:** kart var ama bir parçası eksik ya da bir koşula bağlı.
- **daraldı:** karşılık sözden dar ve bu yazılmamış.
- **düştü:** karşılık yok.
- **askıda:** Batu kararı bekliyor.

"Nasıl" düzeyi, kartın metinde yazılı olduğunu gösterir; kartın çalıştığını göstermez (§14.4: hiçbir mekanizma canlı sınanmadı).

### A.1 U003 (13 madde)
| # | Söz | Karşılık | Düzey | Not |
|---|---|---|---|---|
| 1 | "Sürekli yetki için onay veriyorum." | MB-08 ZARF-v1; S1-M1 | nasıl | Haritaya uygulanışı K-3'te |
| 2 | "Main'i birleştirmeyi sen yap ... branchların birikmesini istemiyorum" | S18.8; M9.8; K-8 | daraldı | Birleştirme K-009 ile askıda; dal silme Batu'ya geçti (E1-11) |
| 3 | EXP-007'de başla; "drift yaşatmasını istemem" | §6; M16.3; M7.1 K∅ | nasıl | — |
| 4 | "izinleri konuşmak bile detay" | izinler §12.1'de tek listede | nasıl | — |
| 5 | "bu mesajımı "başla" olarak algılama" | §2 P0→P1 durak | nasıl | — |
| 6 | EXP-006'nın amacını ve düşünme yaklaşımını anla | K-006 | karşılandı (Batu) | U004: "evet çok iyi anlamışsın" |
| 7 | Baştan başlasaydık "nasıl yönetirdik, nasıl bir yapı kurardın" | METHOD bütünü; §2, §6, §7 | nasıl | — |
| 8 | "alt ajanlar nasıl düşünürdü" | T2 §2.7 rol dosyalarındaki "## Yöntem"; ortak sözleşme §7; MB-05 ÇÜRÜTME İZİ; MB-04 "Sınanacak varsayımlar" | nasıl | Düşünme yöntemi rol katmanında; brief'te tekrarlanmıyor |
| 9 | "düşünmek için repodan nasıl yararlanırdı" | M7.1–M7.4; MB-04 BAĞLAM PAKETİ; MK-6.2 | nasıl | — |
| 10 | Foundation ve studies'ten "nasıl ve ne zaman" | MK-6.1 (9 tetik); MK-6.2; MK-6.9 | nasıl | — |
| 11 | "planı nasıl yönetirdin" | MK-5.1–MK-5.5; MB-12 | nasıl | — |
| 12 | "planı nasıl revize ederdin" | MK-5.6 (8 adım); MB-14; S1-M1 | nasıl | — |
| 13 | "net bir şekilde ortaya konmadan başlamaman lazım" | 21 alt sistem, 157 kart | kısmen | Yordam ve betik metinleri eksik (E1-04) |

### A.2 U004 (15 madde)
| # | Söz ya da gereksinim | Karşılık | Düzey | Not |
|---|---|---|---|---|
| 1 | "yeni konuşmada bu konuya devam edebilmemiz için repoda bir hazırlık" | MB-08; S18.1; MB-02 | nasıl | Bugün STATE ile uygulanıyor |
| 2 | "yapıyı basit tutmuşsun ... küçük" | 21 alt sistem; 157 kart | nasıl | Ters yön: E1-06 |
| 3 | "context management önemli bir yer tutacak" | M7.1–M7.9; MB-04; MB-06; MB-09 | nasıl | Koordinatör bütçesi eksik (E1-09); tepe bağlam freni yok (E1-01) |
| 4 | "memory yönetimi de aynı şekilde" | M8.1–M8.9; MB-03; MB-17 | nasıl | Yazma M8.3, yerine koyma M8.4, tazelik M8.5, çakışma M8.6, unutma M8.7, köken M8.2 |
| 5 | "kalıcı bir rol yapısına ihtiyacı var ... her seferinde yeninden alt ajana rol biçmek doğru değil" | §4; T2 §2.7; MB-04 (brief'te rol yok); MB-03 | nasıl | Yüklenmesi PS-2'ye bağlı; PS-2 düşerse (iii) yedeği v0'a döner |
| 6 | "best practice'lere göre bir metodoloji" | kartların Kaynak alanı (R07–R11) | nasıl | Kanıt türü: tedarikçi belgesi ve topluluk pratiği |
| 7 | "dünyada ilk defa konuşan ... olamayız" | MK-6.1 (mekanizma icadından önce bak) | nasıl | — |
| 8 | "bütün bunları nasıl yapacağını ortaya dökmen gerekiyor" | kartlar | kısmen | 6 skill ve `bash-kapisi.sh` yok (E1-04) |
| 9 | "konuyu iyi anlamış gibi ifade ediyorsun ama ... sonuç çok daha dar" | S14-M8; §10 | kısmen | Matris daralmayı gizliyor (E1-03) |
| 10 | "fren koymadığın ortaya çıkıyor" | S17-M2; S17-M3; MB-08; MB-10; MB-15 | kısmen | Frenler yalnız yapısal (E1-01) |
| 11 | Güvenlik: "hava yastığı ... radar ... gözlerini takip eden sistem ... uyarı" | §10.2 U004-11 eşlemesi | nasıl | Korkulukların sökülme riski (E1-02) |
| 12 | Konfor: "bel desteği ... ayarlanabilir ... masaj" | S2-M1; S2-M5; MB-11; MK-3.8 | kısmen | İlk uygulamada dikkat bütçesi aşılıyor (E1-07) |
| 13 | "yeterli seviye ile standart seviye arasında fark var" | §3 (209 satır); S14-M9 | nasıl | Bir dışlamanın gerekçesi kendi sayı sınırı (E1-01) |
| 14 | "bütünsel bakıldığında ... diğer mekanizmaların yetersizleşmesine sebebiyet verir" | §8; W1–W10 | nasıl | İki bütünsel boşluk: E1-01, E1-02 |
| 15 | "bunlar sana repoda ... verilmiş (studies) ... (foundation)" | MK-6.1; MK-6.2 | nasıl | — |

### A.3 A003 (67 madde)
| A003 | Söz | Karşılık | Düzey | Not |
|---|---|---|---|---|
| §1 | "her role doğru bilgiyi doğru zamanda veren, yapılanı kaydeden ve kontrol eden bir düzen" | MB-04; M7.7; MB-02; S14 | nasıl | — |
| §1 | "benim burada nasıl çalıştığım, DevOS'un ilk canlı örneği olacak" | S21.6 | nasıl | — |
| §2 | "İlk gün kaba haritayı çıkarırdım." | §2; MK-3.1 | nasıl | — |
| §2 | "Ortamı ilk hafta öğrenirdim." | §13.2 erken denemeler; MB-19 | kısmen | K-4 izni bekleniyor |
| §2 | "Rolleri iki kaynaktan türetirdim" | §2 P2 çıkış ölçütü; MK-4.6 | nasıl | P2'de işler |
| §2 | Kontrol ayrı alt ajanlarda; okuma iddiası kayıtla | `e7-elestirmen`, `e7-dogrulayici`; MB-05 OKUMA KAPSAMI | nasıl | — |
| §2 | "Senin sözlerini birebir saklardım." | M10.1; `bash-kapisi.sh` Z5 kolu | nasıl | UserPromptSubmit ertelendi |
| §2 | "Durumu tek yerde tutardım." | MB-08; M9.2 | nasıl | — |
| §2 | "erken, küçük denemelerle sınardım" | §13; MK-3.7 | kısmen | Kurulu bütün tek adımda etkinleşiyor (E1-06) |
| §3.1 | Amaç zinciri | MB-04 | nasıl | — |
| §3.1 | Söylenen, kastedilen ve anlayış ayrımı | M10.2 | nasıl | — |
| §3.1 | Bilinmeyeni sınıflandırmak; "Sana sormak son seçenektir." | S1-M3; MB-11 | bilerek değiştirildi | Y16 dengeleyicisi |
| §3.1 | Bitti tanımı ve kararı neyin değiştireceği baştan | S14-M1; MB-04 | nasıl | — |
| §3.1 | Yap, karşı-okut, kaydet | MK-3.3; S14-M4 | nasıl | — |
| §3.2 | "Mesaj taşımazsın, eksik de aramazsın." | S1-M1; MK-4.5 | kısmen | Uyanma PS-1'e bağlı; dal silme Batu'da (E1-11) |
| §3.2 | "her hatırlatma bir kusur olarak kayda geçer; ... başarı ölçüsü bu sayıdır" | S2-M6 | bilerek değiştirildi | Eşli ölçüler (Y13) |
| §3.2 | Ana oturumun görevleri | M11.9; §4.6; M12.5 | nasıl | — |
| §3.2 | "tek soruluk, geçici çalışanlar. Beş türü var" | §4 sekiz kalıcı rol | bilerek değiştirildi | K-007 |
| §3.2 | "Bunlar DevOS'un rolleri değil." | `e7-` öneki | nasıl | — |
| §3.2 | Alt ajan alt ajan açamaz; iletişim ana oturumdan ya da repodan | M13.4; §14.3 | nasıl | — |
| §3.3 | Dokuz alanlı görev tanımı | MB-04 | nasıl | Yöntem, kanıt dili ve dönüş biçimi rol katmanına taşındı |
| §3.3 | "Aynı görevi aynı tanımla ikinci kez göndermem." | M12.8 | bilerek değiştirildi | Kayıp iş istisnası gerekçeli |
| §3.3 | "Dönen sonuç veridir, kanıt değildir." | M13.6; S14-M6 | nasıl | — |
| §3.3 | Karşı-okuyucu gerekçeyi görmez | `e7-elestirmen` (B2); MB-04 adım 4 | nasıl | — |
| §3.3 | "üç kez aynı şekilde tekrarlanınca kalıcı bir ajan tanımına dönüşür" | M11.1; MB-18 | bilerek değiştirildi | Y4 |
| §3.4 | "Repo bellektir; konuşma bellek değildir." | ilke 1; M8.1 | nasıl | — |
| §3.4 | Okuma yolu: giriş → harita → özgün bölüm | CLAUDE.md §2; MK-6.2 | nasıl | — |
| §3.4 | "Okuma kaydı: her okuma için" | MK-6.3 (yalnız karar taşıyan okuma) | daraldı | Gerekçesi var (Y14), etiketi yok (E1-03) |
| §3.4 | "Okumak karşılaştırmak demek değildir." | MK-6.5 | nasıl | — |
| §3.5 | Önce Foundation, sonra studies | MK-6.2 | nasıl | — |
| §3.5 | Altı başvuru anı | MK-6.1 (9 tetik) | nasıl | — |
| §3.5 | "şu alana bakılmalı" bildirimi | MK-6.9; MB-05 KAYNAK BOŞLUĞU | nasıl | — |
| §3.5 | Araştırma izi; "yalnız akıl yürütme"; durma | MK-6.4; MK-6.8 | nasıl | — |
| §3.5 | Foundation'dan altı ayrım | S14-M2; MB-12; S1-M3; S21.2; MK-6.7; M16.3 | nasıl | — |
| §3.6 | Tek ana harita | §2; MK-3.1 | nasıl | — |
| §3.6 | İş listesi alanları; "seçtiğimiz sıra" ≠ "zorunlu önkoşul" | MB-12; MK-5.3 | nasıl | — |
| §3.6 | "Durum dosyası tek ekranı geçmez" | MB-08 (≤40 satır) | nasıl | — |
| §3.6 | Karar katmanları | S1-M1 | nasıl | — |
| §3.6 | Kontrol noktaları: kalem sonrası kayıt; aşama sonu rapor, main'e birleştirme, dal silme; P4 durağı | S18.3; S2-M2; §2 | kısmen | K-009 askıda; dal silme Batu'da |
| §3.6 | İlerleme ölçüsü; "hareket var, ilerleme yok" | S17-M2; S17-M3 | nasıl | Fren düzeyi ys (E1-01) |
| §3.7 | Revizyon tetikleri; önce neyin değiştiği | MK-5.6; S1-M1 | nasıl | — |
| §3.7 | Kim karar verir; kendi yanlışını hemen geri çekme | MB-14 | nasıl | — |
| §3.7 | Tarihli not; kabul sürümü; sapma; ölçüt değişmez | MK-5.6; MK-5.8; S14-M1 | nasıl | — |
| §3.7 | En çok üç eleştiri turu; yeniden açma | S14-M4; MK-5.9 | nasıl | — |
| §3.8 | Ölçüt önce; katlar; kanıt gücü adıyla | S14-M1; S14-M2; MK-6.7 | nasıl | — |
| §3.8 | "P1'in yarısı canlı deneme olmalı." | — | düştü | P1 çıkış ölçütü "denenemedi" ile kapanabiliyor (E1-03) |
| §3.8 | "kimseye verilmemiş iş var mı?" | MK-4.5; MB-13 §3 | nasıl | — |
| §3.8 | Kontrol ağırlığı risk ve geri alınabilirlikle orantılı | MB-12 | nasıl | — |
| §3.9 | Sohbet kısa; yalnız dört durumda gelinir | S2-M1; S2-M5 | nasıl | P0'da aşım (E1-07) |
| §3.9 | Üç bitiş biçimi; sahte seçenek yok; "bilmiyorum" | CLAUDE.md §4; S18.7 | nasıl | — |
| §3.9 | Yeni oturumun okuma sırası; devir notu git'le karşılaştırılır | CLAUDE.md §2; S18.1 | kısmen | STATE listede yok; hook'suz yolda düz yazı (E1-12) |
| §3.9 | "Bir bilgi tek yerde durur." | M9.2 | nasıl | — |
| §3.9 | "Ana oturum az okur, okumayı alt ajanlar yapar." | M7.4 | bilerek değiştirildi | Y2 |
| §3.10 | Ders kaydı; davranış görülene kadar "doğrulanmadı" | MB-17; S21.2 | nasıl | L-001 etiketi (E1-08) |
| §3.10 | Düzenin gözlemleri P3 için ayrı yazılır | S21.6 | nasıl | — |
| §4 | Alınanlar (Batu'nun EXP-006 mesajları, D001–D018, K1–K2 ...) | K-010 sonrası aşama girdisi | bilerek değiştirildi | K-010 |
| §4 | Bırakılanlar; "senin kelimene dönülür" | M16.3; M9.2; M10.5; M10.3; §4.4 D1 | nasıl | — |
| §4 | Yön tabelaları EXP-007'ye çevrilir | A-05 | askıda | K-009 |
| §5 | Kısa CLAUDE.md ve dosya yapısı | MB-06; §6; §12.4 | nasıl | — |
| §5 | Concepts yöntemi: iki deneme, iki gözden geçirme, sonra dosyalar | §13 | kısmen | Pilotlar kurulu yapılandırmayı sınamıyor (E1-06) |
| §5 | AGENT.md kontrol katmanı; ChatGPT'ye özgü kısımlar tek öneri | S1-M5; §12.1 O-5 | nasıl | A-01 bekleniyor |
| §6 | Tek koordinatör riski; kararlar gerekçesiyle repoda | M11.9; MB-02; `butunsel` merceği | nasıl | — |
| §6 | Maliyet ve haftalık limit | MB-10; S20 | kısmen | PS-3; mekanik fren yok (E1-01) |
| §6 | Düzenin ağırlaşması | S21.5; MK-3.8; §11 | kısmen | Dengeleyiciler iki aşama sonra (E1-06) |
| §6 | "düzen belli özelliklere değil, üç ilkeye dayanmalı" | ilke 1, 2, 5; CLAUDE.md §5 | kısmen | Zorlama belirli hook olaylarına ve rol alanlarına dayanıyor; yedeği yalnız tavsiye |
| §6 | Soğuk başlangıç; "Cevap senin niyetinle karşılaştırılır." | MB-16 | daraldı | Anahtar ve puan koordinatörde (E1-05) |
| §7 | Batu'ya üç soru | K-006; A-01; A-02 | karşılandı (Batu) | İkisi Batu'da |

**Sayım (95 madde):** nasıl 67 · bilerek değiştirildi 7 · karşılandı (Batu) 2 · kısmen 14 · daraldı 3 · düştü 1 · askıda 1.

**Taslağın §10'uyla farkları:**
- "düştü" ve "daraldı" olan dört maddeyi taslak "kart var", "askıda" ya da hiç yazmıyor: A003 §3.8, §3.4, §6 soğuk başlangıç; U003-2.
- "kısmen" olan 14 maddenin dokuzunu taslak "kart var" diye işaretliyor: U003-13; U004-8, -9, -12; A003 §2 "erken, küçük denemeler"; §3.9 okuma sırası; §5 concepts yöntemi; §6 ağırlaşma; §6 "üç ilke". Kalan beşini taslak da "kısmen" sayıyor.
- Taslağın "Karşılanmadı: 0" sonucu bu farklardan doğuyor.

## Ek B — Standart seviye karşılaştırması

Her maddeyi taslağın §3 tablosuna ve §5.1 kart dizinine eşledim. Kuşkulu maddelerin tam metnini açtım; öbürlerini başlıklarıyla eşledim.

### B.1 R07 §2 kontrol listeleri (60 madde)
| Grup | Eşleme | Not |
|---|---|---|
| BY-1…8 bağlam | BY-1 MB-06 · BY-2 M7.1 · BY-3 M7.4 · BY-4 M7.5 ve "Compact Instructions" · BY-5 M7.6 · BY-6 MB-09, M7.8 · BY-7 §6 · BY-8 T1 M7.5 | BY-3 gerekçeyle değişti (Y2). BY-8'in "state kaydet" yarısı M7.5'te. "Bütçe kaygısıyla erken bitirme" yarısı için ne istem satırı ne §3'te karar var; R07'ye göre Opus 5.5 için bilinmiyor. BY-2'deki yola bağlı `rules` kademesi kullanılmıyor, kararı yazılmamış. |
| BB-1…7 bellek | BB-1 M8.1 · BB-2 M9.8, S18.3 · BB-3 MB-03 · BB-4 M8.3 · BB-5 M8.6, M8.7 · BB-6 S21.2, MB-17 · BB-7 SessionStart enjeksiyonu | BB-3 gerekçeyle değişti (`memory: project` yerine dosya). BB-7 yalnız hook'lu yolda (E1-12). |
| BR-1…8 roller | BR-1 §4, S19.3 · BR-2 `description` · BR-3 M11.2, T2 §2.7 · BR-4 M16.1 · BR-5 §4.1, S20.4 · BR-6 önyüklenen ortak sözleşme · BR-7 M11.6 · BR-8 M11.7, S14-M5 | Tamamı karşılanmış. |
| BP-1…7 skill'ler | BP-1 S19.6 · BP-2 skill ≤120 satır; W4'te yeniden çağrı · BP-3 rollerde Skill aracı yok · BP-4 — · BP-5 "çağrı sayıları retroda" · BP-6 M12.1 · BP-7 — | BP-1'de altı skill metinsiz (E1-04). BP-5 çağrılmayan skill'i yakalamaz (E1-01). BP-4 (`context: fork`) ve BP-7 (skill güvenliği) için karar yazılmamış. R07'nin BP-4 için yazdığı gereksiz koşulu ("yordamın adım adım izlenmesi isteniyorsa") koordinatör yordamlarında büyük olasılıkla geçerli (çıkarım). |
| BZ-1…7 zorlama | BZ-1 M16.7 · BZ-2 MB-07, S19.5 · BZ-3 `durma-kapisi`, `donus-kapisi` · BZ-4 `oturum-baglami` (compact) · BZ-5 S19.5 · BZ-6 MB-19 · BZ-7 ilke 10 | BZ-7'nin sözü ile uygulaması arasında fark var (E1-02). |
| BO-1…8 orkestrasyon | BO-1 §4.6, MB-02 · BO-2 MB-04 · BO-3 M12.1, MB-12 · BO-4 M12.2 · BO-5 MB-05 · BO-6 MK-3.7 · BO-7 MB-02 · BO-8 M16.3, M13.6 | BO-6 kurulumda uygulanmıyor (E1-06). |
| BS-1…7 süreklilik | BS-1 MK-3.2 · BS-2 S18.1 · BS-3 S18.3 · BS-4 JSON: S5 "bilinmiyor", S9 "gereksiz" · BS-5 MB-08, M7.6 · BS-6 MB-15 · BS-7 S18.7 | BS-4'ün gerekçesi R07'nin kendi gereksiz koşuluyla ("kalem sayısı çok azsa") uyumlu. BS-6'nın mekanizması bilinmiyor (PS-1). |
| BD-1…8 doğrulama | BD-1 S14-M1 · BD-2 MB-05 · BD-3 S14-M4, S14-M5 · BD-4 MB-05 durum kodları · BD-5 S14-M4 · BD-6 S14-M4 · BD-7 MB-12 · BD-8 S14-M5 | Tamamı karşılanmış. |

**Sonuç (R07):** 55 madde karşılanmış ya da gerekçeyle değiştirilmiş; 2 madde kısmen (BB-7, BP-5); 3 maddede karar yazılmamış (BY-8'in bir yarısı, BP-4, BP-7). Bu üçünün etkisi düşük olduğu için bulgu yazmadım.

### B.2 R08 §4 ortak uygulamalar (27 madde)
| Madde | Eşleme |
|---|---|
| O1 katmanlı yükleme, gözlenebilir tetik | M7.1 (kısmen: skill çağrısı modelin seçiminde; E1-01) |
| O2–O5 | MB-06 ve M7.1 · MB-04 ve MB-05 · M7.4 (gerekçeyle değişti, Y2) · M7.5 |
| O6–O10 bellek | §6 ve M9.8 · M8.1 · M8.3 · M8.7 · M8.2 |
| O11–O13 roller | §4 · M16.1 ve MB-07 · MB-05 |
| O14–O18 plan | MB-17 ve S15-M4 · MB-12 · MK-3.3 ve MK-5.3 ("gerekli (uyarlanmış)") · S17-M2, S17-M3, MK-5.10 · M12.5 ve S2-M4 |
| O19–O20 iz | MB-02 ve S1-M4 · M11.6 ve MB-04'teki `METHOD@sha` |
| O21–O25 doğrulama ve öğrenme | S14-M4 · MB-12 ve S14-M2 · S21.3 · MB-17 · S21.5 |
| O26–O27 | S2-M1…S2-M5 · S20.5 |

**Sonuç (R08):** 26 madde karşılanmış (O4 gerekçeyle değişmiş); 1 madde kısmen (O1).

### B.3 R09 standart seviye listeleri (58 madde)
| Liste | Eşleme | Not |
|---|---|---|
| BA-1…9 bağlam | M16.3, MB-04 ve MB-05 etiketleri · M7.1 · M8.5 · M7.3 ve MB-04 · MB-09 · M7.5 · M10.5 · ortak sözleşme §7 madde 3 · MB-16 | BA-5'in koordinatör kolu eksik (E1-09). |
| BE-1…12 bellek | M8.1–M8.9; geri okuma M9.8 | Tamamı karşılanmış. |
| RO-1…11 roller | §3'ün S11 satırları; RO-9 için §4.3 §8 ve `hijyen.sh` | Tamamı karşılanmış. |
| YD-1…9 yaşam döngüsü | S18.1 · §7 · S18.3 · S18.4 · MB-12 · W1 adım 5 · S21.3 · §7 olay satırı · M8.7 | Tamamı karşılanmış. |
| GZ-1…8 gözlem | MB-02 · S1-M4 · S2-M4 · STATE bloğundaki gösterge · S17-M5 · S17-M2 · MB-17 · S17-M5 | GZ-4'teki ayrı pano gerekçeyle gereksiz sayılmış. |
| MK-1…9 maliyet | MB-10 · MB-10 · MB-10 · `maxTurns`, S20.3 · MB-10 · S21.5 · — · S2-M5 · S20.4 | MK-3 kısmen (E1-01); MK-7 kısmen (E1-09); MK-8 ilk uygulamada aşılıyor (E1-07). |

**Sonuç (R09):** 55 madde karşılanmış; 3 madde kısmen (BA-5, MK-3, MK-7).

### B.4 R10
- **Bileşenler (§3.7'de 8, §4.12'de 10, §5.8'de 8):** 26 bileşenin hepsinin karşılığı var.
  - Bağlam: kullanım sözleşmesi → MB-04 "Karar ... kabul edilen kayıp"; tüketici tanımı → MB-04 "Alıcıda var / yok"; sürüm bağı → M9.4; uç nokta kanıtı → MB-05 OKUMA KAPSAMI; okuma yolu → M9.6; yeniden ifade → MB-05 ve M10.5; karar anı → MK-6.1; taban değişikliği → M12.6 ve TABAN.
  - Bellek: tür, kip, köken ve iki zaman → M8.2; durum boyutları → M8.4 ve M9.3; taban kontrolü → M13.6; geri çekmenin yayılması → M9.5 ve S1-M4; çakışma → M8.6; saklama → M8.7; ders → MB-17; soğuk başlangıç → MB-16.
  - Rol: sorumluluk ve ayrık alanlar → M11.2; "Çağrılır" sütunu ve "çağrılmazsa görünen iz"; MB-03; M11.6; MB-14; B0–B5; M11.7.
- **Test soruları (§3.5'te 11, §4.10'da 12, §5.6'da 12):** 18'ini sınadım (§3.5: 1, 3, 4, 7, 8, 10; §4.10: 2, 3, 6, 9, 11, 12; §5.6: 1, 4, 5, 7, 9, 12). Hepsinin cevabı bir kartta var. İkisinin cevabı zayıf: §4.10/9 (E1-08) ve §4.10/11'in puanlama tarafı (E1-05).
- **§8, yanlış birleştirilmemesi gerekenler:** iki ihlal buldum. Ders basamakları "doğrulandı"da toplanmış (E1-08); "rol metni" ile "zorlama" etiketlerde birleşmiş (E1-13).

### B.5 R11 §3 (164 bileşen) ve §1 madde 6
- 162 bileşenin §3 tablosunda doğrudan karşılığı var.
- İkisinin karşılığı dolaylı:
  - S4 "Amaç ihtiyacı ile yöntem ihtiyacı ayrımı": yalnız MK-3.8'deki `hedef: yöntem` alanıyla.
  - S18 "Uyandırma ve devam mekanizması (... send_later ve Routine'ler ...)": nabız `send_later` ile var; oturumsuz ilerleme v1'de "gereksiz" sayılmış ve CD-03 düşerse yeniden değerlendirilecek.
- §1 madde 6'daki ağırlık dengesi için E1-06'ya bakın.

### B.6 "Gereksiz" ve "sonra" diye bırakılanların gerekçesi
§3'te 15 "gereksiz" ve 11 "bilinmiyor" satırı var. Her "gereksiz" satırında kısa bir gerekçe var; "önlediği hata" sütunu bu satırlarda tasarım gereği "—". Bütünsel etki satırlarda yazılı değil. Taslak bunun "kartında ya da taslağın karar tablosunda yazılı" olduğunu söylüyor (§3 girişi); bunu satır satır sınamadım. Sınadığım ertelemeler:
- **PreToolUse Agent:** gerekçesi "hook sınırı ≤9"; bütünsel etkisi yazılmamış (E1-01).
- **Routines ile oturumsuz ilerleme, "gereksiz (v1)":** koşullu gerekçe var (CD-03); R-1 ile bağı MB-15'te yazılı. Yeterli.
- **UserPromptSubmit ile ham söz kaydı, "ertelendi":** yeniden açma koşulu yazılı. Yeterli.
- **Farklı model doğrulayıcı ve dinamik workflow:** kabul testleri planda yok (E1-10).

Batu'nun "100 km" örneğine uyan, yalnız ölçeğe ya da taslağın kendi sınırına dayanan gerekçelerden biri kesin: hook ≤9. JSON durum dosyası için verilen "kalem sayısı az" gerekçesi sınırda, ama R07 BS-4'ün kendi koşuluyla uyumlu olduğu için bulgu yazmadım.

## Ek C — Zorlama haritası (§5.1'in "Zorlama" sütunundan betikle sayıldı)

| Düzey | Kart | Döküm |
|---|---|---|
| zr (etikette) | 15 | 4'ü ortamın kendi mekanizması: M8.3 (ortamın Stop hook'u), M9.8 (proxy), S18.3 (ortam), S18.8 (proxy) · 8'i rol dosyası alanına dayanıyor ve PS-2'ye bağlı: M11.2, M11.4, M13.4, S14-M4, M16.1, M16.4, S19.3, S20.4 · 2'si eşzamanlılık tavanı ve O-8'e bağlı: M12.2, S20.3 · 1'i izin kuralı ve env: S19.5 |
| yalnız zr¹ | 29 | Yalnız tek repolu oturumda; P0.8 kurulumundan ve CD denemelerinden sonra |
| en çok ys | 106 | Şablon ve zorunlu alan |
| yalnız tv | 6 | M7.2, M7.8, M8.9, M9.2, M16.3, S19.2 |
| betik | 1 | M9.7 |

- **Kurulumdan önce (şimdi → P0.8):** taslağın tasarladığı zorlamanın hiçbiri etkin değil; yalnız ortamın kendi mekanizmaları çalışıyor. Kaynaklar: W1 "Kırılma 2" ve §13.3 "Şimdi ... Yeni bir şey yok". Taslak bunu açıkça yazıyor.
- **Batu'nun ölçütüne doğrudan bağlı kuralların düzeyi:**

| Kural | Kart | Düzey |
|---|---|---|
| Batu'nun sözü birebir | M10.1 | ys; commit'te yeni K satırı için Z5 kolu zr¹ |
| Rol yeniden biçilmez (brief'te rol yok) | MB-04 | ys; brief'i denetleyen kapı yok |
| Karar yayılımı (K-010 olayı) | M12.6 | ys; taban enjeksiyonu zr¹; SendMessage PS-4'e bağlı |
| Tek seferde yazım (L-001) | MB-01 | zr¹ |
| Takılma alarmı | S17-M3, MB-15 | ys; göstergenin enjeksiyonu zr¹ |
| Bütçe durdurma | MB-10 | ys |
| Söz–çıktı ve standart–yeterli denetimi | S14-M8, S14-M9 | ys |
| Rol araç sınırı | M16.1 | zr, ama PS-2'ye bağlı |
| Yıkıcı işlem ve sır koruması | M16.5, MB-07 | zr¹ |

- **Özet:** Zorlama, yazma ve araç sınırlarında yoğun; fren ve anlam denetimlerinde yok. Bu dağılım R07 BZ-7 ile uyumlu olabilir. Ama gözlenmiş maliyet kaymasında taslak kendi ilke 10'unu uygulamıyor (E1-01).

## Ek D — Kart somutluğu örneklemi (32 kart)

| Kart | Somut şablon ya da örnek | Tetik, sahip, kontrol | Hüküm |
|---|---|---|---|
| T1 M7.1 | K0–K∅ tablosu, bütçeler | var; bozulma işareti var | somut |
| T1 M7.4 | okuma tablosu, kalem başına ≈30 KB | var | somut |
| T1 M7.5 | STATE bloğu şablonu, S1–S5 adımları | var | somut |
| T1 M7.8 | kural listesi | var | somut; yalnız tavsiye |
| T1 M7.9 | soru seti, bozuk STATE ile sınama | var | somut (puanlama: E1-05) |
| T1 M8.6 | kayıt şablonu, 1–5 türleri ve yetki | var | somut |
| T1 M8.7 | dört işlem, "Arşiv (yüklenmez)" başlığı, BAKIM satırı | var | somut |
| T3 MK-4.2 | A–H mercekleri, boş hücre yasağı | var | somut |
| T3 MK-4.3 | sınıflama adımları, `return_to` | var | somut |
| T4 S2-M5 | sınırlar, bildirim tablosu | var | somut |
| T4 S15-M5 | ÖZ-DENETİM şablonu | var | somut |
| T5 S18.1 | açılış skill'inin metni, `sed` komutu | var | somut |
| T5 S18.9 | adımlar, puanlama | var | somut (E1-05) |
| METHOD MB-01…MB-19 | on bir alan; MB-02, MB-04, MB-05, MB-08 ve MB-13'te şablon bloğu; MB-07 ve MB-14'te tablo | var | somut |

**Sonuç:** Örneklemde soyut kart yok. Sınır: 157 kartın 125'ini açmadım. §5.1 dizini betikle üretildiği için §0'daki "her kartın ... şablonu ... var" iddiası yalnız örneklemle desteklenebiliyor.

## Özellikle bakılan dört alan (E1 görev tanımı)
- **Kalıcı roller:**
  - Rol sözleşmeleri tam. T2 §2.7'deki yedi dosyanın her birinde şu bölümler var: Sorumluluk, Girdi / Modlar / Mercekler, Yöntem, Çıktı, Yapmayacakların, Durma, Rol belleği. Sekizinci rol §4.5'te.
  - Görev tanımı rolü yeniden biçmiyor. MB-04: "Rol tarifi, kanıt dili ve dönüş biçimi brief'e yazılmaz"; rolden sapma yalnız "Sapma izni" satırıyla olur.
  - İki bilinçli istisna var: P0.7 pilotları ve PS-2 düşerse (iii) yedeği. İkisinde de `general-purpose` ajan birebir rol metniyle kullanılır (MB-18).
  - Kalan risk yüklenmedir (PS-2) ve etiketlerdir (E1-13).
- **Bağlam ve bellek:**
  - Yaşam döngüsü somut: köken ve iki zaman M8.2'de, yazma anları M8.3'te, statü ve yerine koyma M8.4'te, tazelik M8.5'te, çakışma M8.6'da, silmeden unutma M8.7'de.
  - Sıkıştırma politikası var: M7.5 (önce, sırasında, sonra), CLAUDE.md'deki "Compact Instructions", S18.5 ve ikinci sıkıştırmada taze oturum. Taze oturumun mekanizması CD-04'e bağlı.
  - Boşluklar: koordinatör bütçesi (E1-09) ve hook'suz açılış (E1-12).
- **Zorlama katmanı:** Ek C. A003'te hiç zorlama yoktu; taslakta var, ama fren tarafında yok ve kurulumdan önce hiçbiri etkin değil.
- **Maliyet:**
  - v0'da maliyet yoktu. Taslakta MB-09, MB-10, S20.3–S20.6 ve §11 var: transcript'ten ölçüm; tür, dalga ve aşama bütçesi; %80 ve %100 eşikleri; CD-15 kalibrasyonu; 5 saatlik ve haftalık limit davranışı (T5 S20.6).
  - Boşluklar: fren mekanik değil (E1-01). Ölçümün girdisi olan transcript'lerin VM kaybından sonra korunup korunmadığı bilinmiyor (§14.2 madde 4).

## Açık sorular
1. Bu sürümde PreToolUse hook'u alt ajan dağıtımını (Agent aracı) görüyor mu? Girdisinde bütçe ve brief kontrolüne yetecek alan var mı? (E1-01)
2. Hook girdisi, bir Write çağrısının hangi alt ajandan geldiğini ayırt eden bir alan taşıyor mu? (E1-04; §14.2 madde 15'teki sürüm çelişkisi)
3. Uzak dal silme bu ortamda Claude'a açık mı? (E1-11)
4. P0 kabulü için Batu'nun kabul edebileceği okuma yükü nedir? (E1-07)
5. Kurulu bütün, P1'den önce gerçek bir kalemde denenmeli mi, yoksa P1'in ilk kalemleri pilot mu sayılmalı? (E1-06)
6. "Gereksiz" satırlarının bütünsel etkisi, taslağın dediği gibi kartlarda ve karar tablolarında yazılı mı? Bunu satır satır sınamadım.

## Bu notun kanıtlamadıkları
- Taslakla aynı modelden geldiğim için bu inceleme taze gözle karşı-okumadır, bağımsız doğrulama değildir. Taslakla ortak kör noktalarım olabilir.
- Hiçbir mekanizmayı çalıştırmadım; bulgular metne ve git gözlemine dayanıyor.
- 157 kartın 32'sini açtım; kalan kartlar için somutluk yargısı örneklemden genellenmiştir.
- Kontrol listesi maddelerinin çoğunu başlıklarıyla eşledim; tam metni yalnız kuşkulu maddelerde okudum. Başlıkla eşlenen bir maddenin bir alt gereği gözden kaçmış olabilir.
- Zorlama sayımı §5.1'in etiketlerine dayanıyor; o etiketler de betikle çıkarılmış kısaltmalardır. Sayım etiketlerin doğruluğunu kanıtlamaz; E1-13 yanlış bir etiket gösteriyor.
- Kelime sayıları, Markdown ve tablolar dahil, ham `wc -w` değerleridir.
- Claude Code özellikleri (hook olayları, girdi alanları) için güncel belgeye bakmadım.
- Bulgular taslağın işlemeyeceğini göstermez. Daralmaları, beyandaki fazlalıkları ve fren zayıflığını gösterir.
