# E2 — Bütünsel etkileşim ve çarpışma testleri: METHOD v1 taslağının karşı-okuması

> **İncelenen:** `phases/P0-calisma-duzeni/METHOD-v1-TASLAK.md` (dal `claude/hopeful-pascal-7bekcd` @ `a4844af`) · **Tür:** P0.5 eleştirisi (E2), çürütme amaçlı karşı-okuma · **Tarih:** 27 Eylül 2026
> **Bağımsızlık:** Taslağı yazanla aynı model, taze bağlam. Taslağın gerekçesi metnin içinde göründüğü için bu okuma, taslağın kendi ölçeğiyle B1'dir; git ve ortam dosyası gözlemine dayanan iddialar ayrı bir kanıt yolu taşır. Bu bir bağımsız doğrulama değildir.

## Genel hüküm

1. Parçalar kâğıt üzerinde birbirine bağlı. R11 §5'in 20 seçiminin her birinin yanında bir kart var. W1–W10 iyi koşullarda uçtan uca yürüyor. Tek günlük, devir bloğu, dönüş zarfı ve R0–R3 omurgası tutarlı.
2. Düşmanca koşullarda iki yerde düzen Batu'nun açık ölçütünü karşılamıyor. Birincisi: P1–P3 boyunca frenlerin hepsini sürücünün kendi beyanı tetikliyor ve ölçüyor. İlerleme ölçüsü koordinatörün kendi T kararlarıyla beslenebiliyor; "hız varsa fren" koşulu ve R11'in öz-onay döngüsü bu yüzden kırılmıyor (E2-01).
3. İkincisi: Batu'nun sessizliği hiçbir freni tetiklemiyor. Konfor seçimleri, tek bağımsız denetçinin devrede olup olmadığını görünmez kılıyor. Onaysız tercih borcu P4'te tek bir "Tamam"la kabule dönüşebiliyor (E2-02). Bu, U004'teki masaj örneğinin tersidir.
4. On önemli bulgunun çoğu tasarımın ortam gerçeğiyle kesiştiği yerde: ortamın Stop hook'u dönüş kapısını deliyor; main'den açılan oturum dalı bulamıyor; alt ajan sıkıştırması yürütülmemiş; limit işçiyi, koordinatörü, nabzı ve alarmı birlikte susturuyor; P1'deki `add_repo` zorlama katmanını kapatabiliyor.
5. Bulguların hemen hepsi omurgayı değiştirmeden, kart içi eklemelerle ya da birkaç yeni tetikle kapanır. En pahalısı, E2-01 ve E2-02'nin gerektirdiği ve Batu'ya sorulması gereken bir K-002 uygulama kararıdır.

## Bulgu sayıları

**Kritik 2 · önemli 10 · küçük 4 · toplam 16.**

| Kimlik | Ciddiyet | Kısa ad |
|---|---|---|
| E2-01 | kritik | Frenler sürücünün elinde: P1–P3'te ilerleme, sınıf, eşik ve alarm aynı aktörün beyanı |
| E2-02 | kritik | Batu'nun sessizliği görünmez; tercih borcu tek "Tamam"la kabule dönüşebiliyor |
| E2-03 | önemli | Ortamın Stop hook'u dönüş kabul kapısını ve "bilinmeyen etki commit edilmez" kuralını deliyor |
| E2-04 | önemli | "TAMAM" diyen yarım dönüş R0/R1'de K katıyla kapanıyor |
| E2-05 | önemli | W4 yalnız koordinatör için; alt ajan sıkıştırması yok, sıkıştırma sonrası öz-denetim düşmüş |
| E2-06 | önemli | Kullanım limiti ortak-kip arızası; bilinmeyen maliyet bütçe frenini körleştiriyor |
| E2-07 | önemli | Dal bilgisinin tek taşıyıcısı Batu; taze oturum kartı `source_revision`'ı kaybetmiş |
| E2-08 | önemli | P1'de koordinatör oturumunda `add_repo`, zorlama katmanını kapatabilir |
| E2-09 | önemli | Y2'nin dengeleyicisi Y5'i ağırlaştırıyor: koordinatörün bağlamı bütçesiz |
| E2-10 | önemli | Tek arıza noktaları: oturum dışı bekçi yok; pilot yedeklerinin hepsi Batu'ya çıkıyor |
| E2-11 | önemli | Bayat kayıt güncel sanılıyor: rol belleği enjeksiyonu, BAYAT-DEVIR ölçütü, devir bloğu kopyası |
| E2-12 | önemli | §8, R11 matrisini kenar düzeyinde kullanmıyor |
| E2-13 | küçük | Rol dosyası değişikliğinin yürürlük anı üç yerde farklı |
| E2-14 | küçük | YT-9 ile K-9 önerisi uzlaşmamış |
| E2-15 | küçük | Talimat biçimli metin "keşfedilen iş" üzerinden aklanabilir |
| E2-16 | küçük | Çalışan ajana giden düzeltmenin metni kaydedilmiyor |

## Soru, kaynaklar, okuma kapsamı ve yöntem

- **Soru (E2):** Taslağın parçaları birlikte çalışıyor mu? Bir alt sistemde "yeterli" görünen seçim başka bir alt sistemi yetersizleştiriyor mu?
- **Kısaltmalar:** METHOD = `phases/P0-calisma-duzeni/METHOD-v1-TASLAK.md`. Ek T1…T5 = `phases/P0-calisma-duzeni/drafts/T1…T5-*.md` (kart kimliğiyle). R11 = `phases/P0-calisma-duzeni/research/R11-sistem-envanteri-ve-etkilesimler.md`. Repo alıntılarının erişim tarihi 27.09.2026.
- **Tam okunan:** `briefs/` ORTAK, ORTAK-SENTEZ, E-ORTAK, E2; METHOD (1.514 satırın tamamı); R11 §4 (4.1–4.6) ve §5; `sources/conversation/U004.md`; STATE; DECISIONS.
- **Kısmi okunan (hedefli kartlar):**
  - Ek T1: M7.5, M8.5, M8.6, M9.5.
  - Ek T2: M11.6, M12.6, M12.7, M12.8, M13.6, §5.1–§5.3.
  - Ek T4: S1-M2, S1-M3, S2-M4, S2-M5, S14-M2, S15-M5, S17 karar tablosu, S17-M2, S17-M3.
  - Ek T5: S18.1, S18.4–S18.8, S20.1, S20.2, S20.6, §9 (CD tablosu).
  - grep ile: Ek T4 S14-M1, Ek T2 [T2-09], Ek T5 CD-13 ve §11.1 soru 5.
- **Okunmadı:** R01–R10; R11 §1–§3, §6–§7, Ek A; U001–U003, U005, U006, A001–A003; taslakların öteki kartları ve kanıt kayıtları; hook betik gövdeleri (taslakta yazılı değil).
- **Gözlem (bu oturumda, salt okuma):**
  - `git ls-tree origin/main explorations/`;
  - origin/main üzerinde "EXP-007" ve dal adı için `git grep`;
  - `git log --numstat -- …/drafts/`;
  - `~/.claude/stop-hook-git-check.sh` ve `~/.claude/launcher-settings.json`;
  - bu oturumun `create_session` araç tanımı.
- **Kanıt etiketleri:** kaynak diyor / gözledim / çıkarım / varsayım / bilinmiyor.
- **Nasıl aradım:**
  1. R11 §5'in 20 seçimi için taslaktaki dengeleyicinin yerini açtım. Her birinde üç şeye baktım: somut mu, kim tetikliyor, pilota bağlı mı (§2.1).
  2. R11 §4.3'te en çok giriş alan beş alt sistemin (S14, S2, S5, S18, S12) 49 kenarını tek tek taslağın kaynak taraftaki mekanizmasıyla eşledim (§2.2).
  3. W1–W10'u E2 brief'indeki dokuz kötü koşulla yeniden yürüttüm. Her kırılmayı ilgili kartın tam metninde doğruladım (§3).
  4. R11 §4.5'in dört döngüsünü halka halka izledim ve yeni döngü aradım (§4).
  5. Koordinatör ve Batu için "çökerse ne olur" listesi çıkardım (§5).
- **Bulgu ölçütü:** Bir kırılmayı ancak ilgili kartın tam metninde karşılığı yoksa bulgu yaptım. Taslağın açık sorularında zaten duran konuları yalnız bütünsel etkisi yazılmamışsa aldım.

## 1. Bulgular

### E2-01 · kritik · Frenler sürücünün elinde: P1–P3'te ilerleme, sınıf, eşik ve alarm aynı aktörün beyanı
- **Yer:** MB-02 (İ olayları); S17-M2 (aynen, Ek T4); S17-M3; MB-08 ZARF md. 4; MB-12; MB-13 hüküm satırı; MB-15; §8.1 Y12; §8.2 döngü 2.
- **Sorun:**
  - **Hızın aktığı aralık:** K-002'nin hızı P1→P2↔P3→P4 arasında Batu durağı olmadan akar. Bu aralıkta KABUL olayı doğamaz, çünkü kabul paketi yalnız duraklarda hazırlanır.
  - **İlerleme olaylarının kaynağı:** Geriye kalan üç ilerleme olayını (SORU-KAPANDI, T katmanlı KARAR, DOGRULAMA) ana oturum kendisi yazar ve işaretler. T kararı, Batu'ya sunulmadan "sunum: bekliyor" statüsündeyken de ilerleme sayılır.
  - **Tek aktörün kararları:** Aynı ana oturum şunları da belirler:
    - kalemin sınıfını (R0–R3), yani hangi denetimin uygulanacağını;
    - kararın katmanını (M/T/Y), yani neyin Batu'ya gideceğini;
    - eşik mesafesini ve alarmın türünü;
    - alarmın gönderilip gönderilmeyeceğini.
  - **Mekanik olmayan frenler:** Sessiz alarm kuralı ve %100 bütçe durağı mekanik değildir. Sessiz alarm kuralı yalnız aşama geçişini ve paralel dağıtımı keser; seri dağıtım bütçe sınırına kadar sürer.
  - **Sonuç:** "Hareket var, ilerleme yok" durumundaki bir koordinatör, kararı bölerek ya da yeniden karar vererek İ üretir; sarı ya da kırmızı eşik hiç dolmaz.
  - **Düşen karşı önlem:** S17-M2 bu şişmeyi kendisi tanıyor ve karşı önlem olarak aşama sonunda "hangi kararlar gerçekten karar?" örneklemini öneriyor. Bu önlem METHOD'un hiçbir yordamında (W3, §7 aşama kapısı, MB-13 şablonu) yok.
  - **Aşama sonu denetimi yetmiyor:** Aşama sonunda eleştirmen öz-denetim satırlarını ve R3 çıktıları okur. Bu okuma aşama içinde hiçbir freni tetiklemez ve kendiliğinden aşamada kapı hükmünü yine ana oturum verir.
  - **§8.2'nin kırıcısı:** Döngü 2 için gösterilen kırıcı ("Y katı ilerleme sayılmaz") öz-onayın yalnız en zayıf biçimini dışlar.
  - **Hüküm:** Frenler var ama sürücü basmadıkça çalışmıyor. U004'teki fren eleştirisi P1–P3 için geçerli kalıyor.
- **Kanıt:**
  - METHOD MB-02 — "İlerleme olayları ("İ"): SORU-KAPANDI, T ya da Y katmanlı KARAR, DOGRULAMA, KABUL (S17-M2)." — kaynak diyor.
  - Ek T4 S2-M4 — "kabul paketi yalnız duraklarda hazırlanır. Kendiliğinden geçen aşamada aşama raporu yeter" — kaynak diyor.
  - Ek T4 S17-M2 — "Kim: Ana oturum işaretler" ve "Vekil ölçü notu: Kararı bölmek ya da gereksiz revizyon yapmak ölçüyü şişirir. … aşama sonunda çürütücü işlev "hangi kararlar gerçekten karar?" örneklemi yapar." — kaynak diyor.
  - METHOD'da "gerçekten karar" ifadesi hiç geçmiyor (grep) — gözledim.
  - Ek T4 S17-M3 — "Sessiz alarm kuralı yapısal ve tavsiye düzeyindedir; mekanik zorlaması yok." ve "yeni aşama geçişi ve yeni paralel dağıtım yapılmaz" — kaynak diyor. METHOD MB-10 — "mekanik durdurucu yok" — kaynak diyor.
  - METHOD MB-12 — sınıflama: "kalem açılırken ve kapsam değişince; ana oturum". MB-13 — "hüküm kendiliğinden aşamada ana oturumun" — kaynak diyor.
  - R11 §4.5 döngü 2 — "Öz-onay [K33] ve aynı modelle karşı-okuma [K106] ilerlemeyi şişirir. İlerleme ölçüsü de şişer [K69]. Sürekli yetki frensiz kalır [K90]" — kaynak diyor (döngünün kendisi R11'in çıkarımı).
  - U004 — "hızlı gitmesi engellenmesin diye fren koymadığın ortaya çıkıyor" — kaynak diyor.
  - Frenlerin P1–P3'te yalnız sürücü beyanıyla tetiklendiği — çıkarım (yukarıdaki kart metinlerinin birleşimi).
- **Öneri:**
  1. **İlerlemeyi bağımsız kanıta bağla.** İ olayı sürücünün kendi kaydından bağımsız bir kanıta dayansın:
     - T katmanlı KARAR, yalnız PLAN'daki bir çıkış ölçütüne işaretçi taşıyorsa İ sayılsın;
     - SORU-KAPANDI, yalnız sorunun kaydında etkilediği kalem ya da karar yazılıysa İ sayılsın;
     - DOGRULAMA, yalnız İ katında (canlı gözlem, pilot) ya da B3 kanıt yoluyla İ sayılsın.
  2. **Hesabı betiğe ver.** `kalem-kapanisi`'nin betik adımı ya da `oturum-baglami.sh`, GUNLUK'tan mesafeyi hesaplasın ve eşik aşımında ALARM satırını kendisi yazsın. Koordinatör yalnız takılma türünü ve müdahaleyi seçsin.
  3. **Sınıflamayı örnekle.** Her 5 kalemlik notta rastgele üç sınıflama kararı gerekçesiz olarak `e7-elestirmen`'e verilsin: R0–R3, M/T/Y, soru sınıfı, yayılım etki sınıfı. Alt sınıflama bulunursa sarı alarm verilsin. S17-M2'nin "gerçekten karar mı" örneklemi aynı koşuya ve MB-13 şablonuna girsin.
  4. **Sonradan doğan yükü izle.** Kapanmış bir R0/R1 çıktısına sonradan ikinci bir TK ya da İK dayanırsa sınıf yeniden hesaplansın ve eksik set uygulansın. MB-12'nin (b) sorusu bugün yalnız açılışta soruluyor.
  5. Sessiz alarm kuralının seri işi de sınırlayıp sınırlamayacağı Batu'ya sorulsun (K-3 içinde).

### E2-02 · kritik · Batu'nun sessizliği görünmez: konfor, tek bağımsız denetçiyi körleştiriyor; tercih borcu tek "Tamam"la kabule dönüşebiliyor
- **Yer:** S2-M5 (dikkat bütçesi, kanal); §7 "Tipik bir çalışma günü"; S1-M3; S2-M4; S17-M3 sessiz alarm kuralı; §2 V-H-2; §3 S2 "Bilişsel yükün doğrudan ölçümü"; ilke 9; §14.1 R-4.
- **Sorun:**
  - **Konfor kurulmuş, işaret yok:** Taslak Batu'nun okuma yükünü düşüren her şeyi kurmuş: aşama başına ≤1.500 kelime, "okuması gerekmeyenler" listesi, "okumak zorunda değildir" denen kontrol noktası mesajı. Ama okumanın gerçekleştiğini gösteren hiçbir işaret yok. §3, yanıt gecikmesini bilişsel yükün vekili olarak anıyor; eşiği ve tetiklediği bir eylem yok.
  - **Güvenlik bu kanala dayanıyor:** İlke 9'a göre sistemin aynı modelden olmayan tek denetçisi Batu'nun dikkatidir. R-4 de aynı-model riskini bu dikkate dayanarak "kabul edilir" diye kapatıyor.
  - **Batu günlerce sessiz kalırsa:**
    - kontrol noktası mesajları yalnız oturumda durur, kanal bilinmiyor;
    - tercih soruları "cevap gelmezse" varsayılanıyla T kararına döner;
    - "itiraz yok" kabul sayılmaz, ama sonraki iş bu kararların üstüne kurulmaya devam eder ve bunların sayısına sınır yoktur;
    - sessiz alarm kuralı yalnız kırmızı alarmdan sonra devreye girer; sessizliğin kendisi tetik değildir.
  - **P4'te kabul:** Kabul paketi "Senin adına verilen tercihler" listesini taşır. S2-M4'e göre "Tamam" gibi kısa bir cevap paketin tamamı için SHA'ya bağlı kabul sayılır. Böylece taslağın önlemeye çalıştığı "mühürler itirazsız geçti" (E07) yeniden kurulur.
  - **İzlenmeyen varsayım:** Harita varsayımı V-H-2 ("Batu'nun duraklardaki dikkati yeterli") izlenmiyor. W7'nin revizyon protokolü bu yüzden bu varsayımın çöktüğünü göremez.
  - **Masaj örneğiyle karşıtlık:** U004'teki masaj örneği konforun güvenliği artırmasını ister. Burada konfor, güvenlik kanalının kapalı olup olmadığını gizliyor.
- **Kanıt:**
  - Ek T4 S2-M5 — "Okuması gerekmeyenler: çalışma günlüğü, alt ajan dönüşleri, … Hepsi bağlantıyla erişilebilir; zorunlu değil." ve "Batu'ya kendiliğinden bildirim gidip gitmediği bilinmiyor." — kaynak diyor.
  - METHOD §7 — "Oturum mesajı olarak gider; Batu okumak zorunda değildir." — kaynak diyor.
  - METHOD §3 S2 satırı — "Bilişsel yükün doğrudan ölçümü | bilinmiyor | — | vekiller: okuma yükü, soru sayısı, gecikme" — kaynak diyor.
  - Ek T4 S1-M3 — "İtiraz etmezse "sunuldu, itiraz yok" işaretlenir; bu bir kabul değildir." — kaynak diyor.
  - Ek T4 S2-M4 — ""Tamam" gibi kısa bir cevap, paketin başındaki SHA'ya bağlı kabul sayılır" — kaynak diyor.
  - Ek T4 S17-M3 — "Kırmızı alarm Batu'dan cevap almadan 24 saat kalırsa yeni aşama geçişi ve yeni paralel dağıtım yapılmaz" — kaynak diyor. Tetik yalnız kırmızı alarm.
  - METHOD ilke 9 — "Aynı modelden olmayan tek denetçi Batu'nun dikkatidir; onu korumak güvenlik işidir". R-4 — "Kalan risk kabul edilir". §2 — "V-H-2 Batu'nun duraklardaki dikkati yeterli" — kaynak diyor.
  - METHOD ve taslaklarda Batu'nun çok günlük sessizliğine ya da bir okuma işaretine ait kural yok (grep: "sessizli", "okundu", "okudu mu") — gözledim.
  - U004 — "masaj sadece konforu etkileyen bir şey olarak düşünülmemeli, konfor kullanıcının rahatlamasını, ağrısının olmamasını ve dolayısıyla daha güvenli sürüşü sağlar" — kaynak diyor.
  - R11 E07 — ""Onaylar seremoniye döndü. Mühürler itirazsız geçti."" — kaynak diyor. E08 — "Batu'nun dikkati tükenirse çerçeve hatalarını yakalayan tek aynı-model-olmayan kanal kapanır" — kaynak diyor.
- **Öneri:**
  1. **Batu temasını ölç.** GUNLUK'taki BATU satırlarından şu sayılar devir bloğunun göstergesine girsin: son Batu mesajından bu yana geçen gün, kapanan kalem, aşama geçişi, onaysız T kararı ve bu kararlara dayanan kalem sayısı.
  2. **Sessizliği tetik yap.** Onaysız T kararı ya da Batu'suz aşama geçişi bir eşiği aşınca sessiz alarm kuralındaki yavaşlatma uygulansın: yeni aşama ve paralel dalga yok, seri iş sürer. Örnek eşik: 2 aşama geçişi ya da 10 onaysız T kararı (varsayım). Bu, K-002'nin uygulanışını değiştirir; §12.2 K-3'e Batu için seçenek olarak eklensin.
  3. **Kabulün kapsamını daralt.** Tek bir "Tamam", paketteki "Senin adına verilen tercihler"i B katına taşımasın. Bu tercihler, Batu açıkça "hepsi" diyene ya da tek tek kabul edene kadar "sunuldu, itiraz yok" kalsın.
  4. **Aktif kabul iste.** Paketin başında en riskli üç karar için "reddedersen şu değişir" satırı ve tek harfli bir cevap alanı olsun. Bu, okuma yükünü artırmadan dikkati hedefler.
  5. **V-H-2'yi izle.** Batu'dan tepki gelmeyen ardışık kontrol noktası sayısı tutulsun; eşik aşılınca W7 tetiklensin.

### E2-03 · önemli · Ortamın Stop hook'u dönüş kabul kapısını ve "bilinmeyen etki commit edilmez" kuralını deliyor
- **Yer:** MB-01 (Gözlem); MB-07 (hook seti, zorlama haritası); M13.6 (Ek T2); W2 7.–8. adımlar; W5 4. adım; MB-17 L-001; W10 5. adım.
- **Sorun:**
  - **Hook ne yapıyor:** Ortamın kendi Stop hook'u, izlenmeyen ya da commit edilmemiş tek bir dosya varken ana oturumun turunu kapattırmıyor. Bu hook repo ayarı değildir; her oturumda, çok repolu oturumda da geçerlidir.
  - **Paralel dalgadaki sonucu:** Bir işçi son dosyasını yazıp dönüşünü henüz vermemişken koordinatörün turu biterse (örneğin başka bir işçinin dönüşünü işlediği tur), hook o dosyanın commit'ini ister.
  - **Bu turda yaşandı:** T5'in tek commit'i "agent hand-back pending" notuyla, dönüşten önce atıldı.
  - **Taslak bu olayı eksik okuyor:** Taslak bu olayı L-001'in "doğrulandı" kanıtı ve W10'un canlı örneği olarak kullanıyor. Oysa olay, kurulumdan sonra da işleyecek bir mekanizmayı gösteriyor: M13.6'nın kabul testi ("kontrol edildi" olmadan commit'lenmiş işçi çıktısı yok) paralel dalgada düzenli olarak çiğnenir. Metin bunu söylemiyor.
  - **W5'teki çatışma:** `git status`'taki sahipsiz dosya "commit edilmez, kaynağı bulunur" kuralına tabidir. Ortam hook'u ise her tur sonunda o dosyanın commit'ini ister. Dosya bırakılırsa ve VM geri alınırsa kaybolur (W5 "Kırılma").
  - **Eksik çözüm:** T2 kök nedeni doğru yazmış. METHOD ise yalnız taslakları scratchpad'e taşımış. İşçinin son dosyası ve bilinmeyen etki için kural yok.
  - **Zorlama haritasındaki boşluk:** Haritada dokuz hook var. Her oturumda zorlayıcı olan bu onuncusu kayıt ve kabul kuralı olarak yer almıyor.
- **Kanıt:**
  - `~/.claude/stop-hook-git-check.sh` — "There are untracked files in the repository. Please commit and push these changes to the remote branch." (çıkış kodu 2). `~/.claude/launcher-settings.json` betiği `hooks.Stop` altında kaydediyor — gözledim.
  - `git log --numstat -- …/drafts/` — "3f6e25f 10:22 EXP-007: checkpoint T5 cluster draft (written; agent hand-back pending)"; T5 dosyasının başka commit'i yok — gözledim.
  - Ek T2 M13.6 — "Defterde "kontrol edildi" olmadan commit'lenmiş işçi çıktısı yok" ve "7) Defterde "kontrol edildi" ve commit." — kaynak diyor.
  - METHOD MB-01 — "T1–T5'in beşi de tek commit'le ve tam boyuyla girdi". W5 4. adım — "BILINMEYEN-ETKI; commit edilmez, kaynağı bulunur". W5 Kırılma — "koordinatör commit etmeden VM giderse dosya da gider" — kaynak diyor.
  - Ek T2 M12.7 — "ortamın kendi Stop hook'u, ana oturumun turu biterken izlenmeyen ya da commit edilmemiş dosya görürse turu kapattırmıyor" — kaynak diyor.
  - Beş paralel yazarlı dalgalarda tekrarlanacağı — çıkarım.
- **Öneri:**
  1. Ortam Stop hook'unu MB-07'nin zorlama haritasına ve W2/W5 yürüyüşlerine "her oturumda zorlayıcı, repo dışı" satırıyla ekle.
  2. **Kayıt ile kabulü ayır:**
     - Dönüşten önce commit'e giren işçi çıktısı GUNLUK'ta "DONUS-BEKLIYOR, kat Y, kontrol edilmedi" diye işaretlensin.
     - TK, KAPI ve DECISIONS, kontrol satırı olmayan bir yolu dayanak gösteremesin.
     - M13.6'nın kabul testi buna göre yeniden yazılsın.
  3. **Bilinmeyen etki için karantina uygula.** "Commit etme" yerine dosya scratchpad'e taşınsın; yolu ve özeti BILINMEYEN-ETKI satırına yazılsın. Böylece ortam hook'u susar ve geçmişe sahipsiz dosya girmez.
  4. MB-01 ve MB-17'deki gözlem cümlesine T5'in dönüşten önceki commit'i eklensin. L-001'in kanıtı "tek yazım" için geçerlidir, "kayıt dönüşten sonra" kuralı için değil.

### E2-04 · önemli · "TAMAM" diyen yarım dönüş R0/R1'de K katıyla kapanıyor
- **Yer:** W2 7. adım; §7 "Dönüş" satırı; MB-05; M13.6 (Ek T2); S14-M1 ve S14-M2 (Ek T4); MB-12; §12.3 `donus-alma`.
- **Sorun:**
  - **Ölçüt var, ölçüm yok:** Bitti tanımı ve kabul ölçütü işten önce yazılıyor (S14-M1). Ama dönüşü işleyen hiçbir METHOD yüzeyi çıktıyı bu tanıma karşı ölçmüyor.
  - **Kontrolün kapsamı:** W2'nin kontrol adımı, §7'nin dönüş satırı ve M13.6'nın yedi adımı şunlarla sınırlı: şema, taban, dokunulan dosyalar, karar-kritik iddia örneklemi ve talimat biçimli metin. K katı "karar taşıyan iddialar kaynağında bulundu" demektir.
  - **İsabet ile kapsam farkı:** Bu kontrol isabeti örnekler, yani yazılanın doğruluğunu. Kapsamı örneklemez, yani istenenin yazılıp yazılmadığını.
  - **Senaryo:** Brief'in on maddesinden altısını karşılayıp "TAMAM" diyen bir dönüş, yazdığı iddialar doğruysa K katıyla kapanır. R0/R1'de çürütücü yoktur.
  - **Tek kapsam denetimi:** Kapsamı denetleyen tek şey işçinin kendi öz-denetimidir (ortak sözleşme §7 madde 6).
  - **Kartta kalmış adım:** S14-M1'in "dönüş gelince testler uygulanır" adımı kartta duruyor. Ama `donus-alma` skill'inin metni yok ve METHOD'un yordamları bu adımı anmıyor.
  - **Zincirleme etki:** Kapanan yarım iş bir İ olayı üretirse (E2-01) takılma alarmı da susar. Eksik ancak aşama kapısında görünebilir: eksik-arayıcı "kimseye verilmemiş iş" ararken ona rastlarsa. Oysa bu iş "verilmiş" bir iştir.
- **Kanıt:**
  - Ek T4 S14-M1 — "2) Dönüş gelince testler uygulanır." — kaynak diyor.
  - METHOD W2 7. adım — "Kontrol: M13.6 (şema, taban farkı ve uzlaştırma, dokunulan dosyalar, ≥2 karar-kritik iddia kaynağında, talimat biçimli metin); kat Y→K" — kaynak diyor.
  - METHOD §7 — "`donus-alma`: zarf kapısı, M13.6, taban farkı, ≥2 iddianın kaynağında okunması, DONUS + ölçüm, rol belleği önerileri" — kaynak diyor.
  - Ek T4 S14-M2 — "K kaynaktan kontrol edildi … Karar taşıyan iddialar kaynağında bulundu" — kaynak diyor.
  - METHOD §12.3 — `donus-alma` için "**metin yok**; P0.6'da yazılır" — kaynak diyor.
  - METHOD §4.3 (ortak sözleşme §7) — "6. Kapsam: brief'in her maddesinin çıktıda karşılığı var mı?" — kaynak diyor. Bu bir öz-denetimdir.
  - Yarım dönüşün K katıyla kapanabileceği — çıkarım.
- **Öneri:**
  1. Zarfa "BİTTİ TANIMI KARŞILIĞI: madde → yol#bölüm | karşılanmadı" alanı ekle. `donus-kapisi.sh`, brief'teki numaralı maddelerin hepsinin zarfta geçtiğini mekanik olarak denetlesin.
  2. M13.6'ya bir adım ekle: en az bir bitti tanımı maddesinin karşılığı çıktıda açılsın. "Karşılanmadı" varsa durum en iyi ihtimalle ÇEKİNCELİ-TAMAM olur ve K katı verilmez.
  3. S14-M2'de K katının tanımına "bitti tanımı maddeleri karşılandı" eklensin. W2 7. adım ve §7 "Dönüş" satırı bunu ansın.

### E2-05 · önemli · W4 yalnız koordinatör için yürütülmüş: alt ajan sıkıştırması yok, sıkıştırma sonrası öz-denetim birleştirmede düşmüş
- **Yer:** W4; §4.4 ortak frontmatter (`omitClaudeMd: true`); MB-09; MB-05; §7 "Her 5 kapanan kalem" satırı (BK-32); S15-M5 (aynen, Ek T4).
- **Sorun:**
  - **Alt ajanlar da sıkıştırılıyor:** Taslağın kaynakları alt ajanların da %80'de sıkıştırıldığını söylüyor. Bu turda ajanlar eşiğe dayandı: tepe bağlam 620–734 K, birleştirmede 776 K. MB-09'un 300 K hedefi zorlanmıyor.
  - **Yönlendirme ve iz yok:**
    - e7 rolleri `omitClaudeMd: true` ile çalıştığı için CLAUDE.md'deki "Compact Instructions" onların özetini yönlendirmez.
    - Ortak sözleşmede sıkıştırma için tek satır yok.
    - Zarfta sıkıştırma olup olmadığını söyleyen alan yok.
  - **Sonucu:** Sıkıştırılmış bir işçi, okuma kapsamını ve karar-kritik iddialarını kaynaktan değil özetten yazabilir. Koordinatörün iki iddialık örneklemi tek yakalama noktasıdır.
  - **Birleştirmede düşen tetikler:** T4 S15-M5'in öz-denetim tetikleri dörttür: 5 kalem, dalga sonu, sıkıştırmadan sonraki ilk tur, 40 dakikayı aşan özerk koşu. METHOD §7 bunu BK-32 ile "her 5 kalem ya da oturum başına bir kez"e indirmiş.
  - **Fiilen kalkan denetim:** METHOD taslakla çelişirse METHOD geçerlidir. Bu yüzden çapanın en çok kaydığı an olan sıkıştırma sonrasındaki öz-denetim fiilen kalkmış; W4 bunu anmıyor.
- **Kanıt:**
  - Ek T2 M12.7 — "alt ajanlar da %80'de sıkıştırılır [T2-09]" — kaynak diyor. [T2-09] — "`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` applies to subagents as well" — kaynak diyor (tedarikçi belgesinden aktarım; bulutta geçerliliği denenmedi).
  - STATE "Maliyet" — "tepe bağlam 620–734 K, yani %80 sıkıştırma eşiğine (≈ 800 K) yakın" ve "Birleştirme: … tepe bağlam 776 K" — kaynak diyor (ölçüm).
  - METHOD MB-09 — "tepe bağlam için zorlayıcı araç yok (`maxTurns` yalnız kaçak koruması)". §4.4 — "`omitClaudeMd: true` (taze okuyucu hariç)" — kaynak diyor.
  - Ek T4 S15-M5 — "Tetikler: her 5 kapanan kalem; her alt ajan dalgasının (en az 3 paralel dönüş) sonu; sıkıştırmadan sonraki ilk tur; 40 dakikayı aşan kesintisiz özerk koşu." — kaynak diyor.
  - METHOD §7 — "Her 5 kapanan kalem ya da oturum başına en az bir kez | yön notu … + öz-denetim (S15-M5) …: tek not, tek ritim (BK-32)" — kaynak diyor. Başlık — "Bu metin bir taslakla çelişirse bu metin geçerlidir" — kaynak diyor.
  - Taslaklarda alt ajan sıkıştırmasını yürüten bir kart yok (grep) — gözledim.
- **Öneri:**
  1. W4'e alt ajan kolu ekle. Ortak sözleşme §5'e şu satır girsin: "Sıkıştırıldıysan brief'i ve kendi taslağını yeniden oku. Okuma kapsamında yalnız sıkıştırmadan sonra yeniden açtığın kaynağı 'tam' yaz."
  2. Zarfa "SIKIŞTIRMA: yok | oldu (n)" alanı ekle. "Oldu" ise koordinatör örneklemi ikiden üçe çıkarsın ve TAMAM'ı ÇEKİNCELİ saysın. Bir hook alt ajan sıkıştırmasını görebiliyorsa (bilinmiyor) bu mekanik yapılsın.
  3. §7'ye S15-M5'in sıkıştırma sonrası ve dalga sonu tetiklerini geri koy. Ya da BK-32'de bunların neden düştüğünü bütünsel etkisiyle yaz.

### E2-06 · önemli · Kullanım limiti ortak-kip arızası: işçi, koordinatör, nabız ve alarm birlikte susuyor; bilinmeyen maliyet bütçe frenini körleştiriyor
- **Yer:** MB-15; MB-10; MB-08 "Maliyet" satırı; §13.1 PS-3; Ek T5 S18.6 tablosu, S20.2, S20.6; §14.2 soru 4.
- **Sorun:**
  - **Taslağın cevabı:** Haftalık limit dolunca taslağın cevabı "`DURAK: bütçe` (Batu karar verir)".
  - **Tur olmadan adım yok:** DURAK'ı yazacak, Batu'ya haber verecek ve nabzı yenileyecek her adım bir model turu ister. Limit dolduğunda tur API hatasıyla biter.
  - **Nabız zinciri kopar:** Kısa ve uzun nabız limit içinde ateşlenip boşa gider. Nabız yalnız kalem kapanışında yeniden kurulduğu için zincir kopar. Limit sıfırlandığında oturumu uyandıracak bir şey kalmaz.
  - **Kayıt ve alarm da düşer:** StopFailure satırı diske yazılır ama commit edilmez; VM geri alınırsa o da gider. Limit kırmızı alarm listesinde yok. PushNotification da bir tur ister.
  - **Önceden sezme koşullu:** Limiti önceden sezmenin tek aracı durum satırı köprüsüdür (CD-10) ve bulutta çalışıp çalışmadığı bilinmiyor. Çalışmazsa sensör Batu'nun /usage okumasıdır.
  - **Ölçüm körlüğü:** Harcama, dalga bittikten sonra transcript'ten ölçülür. VM kaybında transcript'in korunup korunmadığı bilinmiyor. Bilinmeyen satır "bilinmiyor" yazılır ve 0 sayılmaz, ama eşik hesabına nasıl gireceği yazılı değil.
  - **İki kuralın birleşimi:** Dürüst ölçüm kuralı ile eşik kuralı birleşince, %100 durağı arızalardan sonra, yani tam da maliyetin belirsizleştiği anda, tetiklenemeyebilir.
  - **Ölçek:** Beş derin ajanlık bir dalga ~155 M işlenen token tuttu (ölçüm). Limitteki karşılığı bilinmiyor.
- **Kanıt:**
  - Ek T5 S18.6 tablosu — "Haftalık limit doldu | `DURAK: bütçe` (Batu karar verir)" ve "Nabız yalnız kalem kapanışında yeniden kurulur." — kaynak diyor.
  - Ek T5 S20.6 — "Anında (ana oturum) | Tur API hatasıyla biter; StopFailure olay satırı yazılır" ve "Bozulma işareti: limitten sonra Batu'nun oturumu açmak zorunda kalması (nabız çalışmadı)" — kaynak diyor.
  - METHOD MB-15 — alarm "(b) varsa PushNotification gönderir". Kırmızı eşik listesi (5 kalem, 4 dalga ya da 24 saat …) limit olayını içermiyor — kaynak diyor.
  - METHOD W5 Kırılma — "koordinatör commit etmeden VM giderse dosya da gider" — kaynak diyor.
  - Ek T5 S20.2 — "Durum satırı çalışıyorsa (CD-10) … Çalışmıyorsa Batu her aşama raporunda /usage'daki haftalık yüzdeyi bir sayı olarak yazar." — kaynak diyor.
  - METHOD MB-02 — "ölçülmediyse "bilinmiyor", asla 0". MB-08 — "Maliyet (aşama): <işlenen M / bütçe> (bilinmeyen satır <n>)". §14.2 soru 4 — "VM kaybından sonra transcript'ler, yani ölçümün girdisi, korunuyor mu?" — kaynak diyor.
  - METHOD §11.1 — "T1–T5 … 154,6 M işlenen" — kaynak diyor (ölçüm). R11 E95 — "Limit dolunca paralel iş durur ve yarım kalır." — kaynak diyor.
  - Nabız zincirinin limit içinde tükeneceği ve alarmın gönderilemeyeceği — çıkarım (denenmedi).
- **Öneri:**
  1. **Tüketilmeyen bir uyandırma kur.** İki tek seferlik nabzın yanında, ateşlendiğinde hata alsa da yaşayan düşük sıklıklı bir yinelenen tetik olsun (ör. bu oturuma 6 saatte bir `create_trigger` cron). İlk işi limit ve takılma kontrolüdür. CD-03'ün limit varyantı pilota alınsın.
  2. **Limitten önce dur.** Dağıtımdan önce dalga bütçesi × kalibrasyon oranıyla haftalık yüzde tahmin edilsin. Kalibrasyon yoksa (PS-3 düşerse) üçten çok derin ajanlık dalga açılmasın. "Limit yaklaşıyor" kırmızı alarm listesine girsin ve limitten önce gönderilsin.
  3. **Bilinmeyeni eşiğe kat.** Bilinmeyen satır eşik hesabında tür bütçesiyle doldurulsun ("tahmini" etiketiyle). Bilinmeyen satır sayısı bir eşiği aşarsa sarı alarm verilsin.
  4. **HATA satırını koru.** `hata-kaydi.sh` HATA satırını commit etsin. Ya da kartta bu satırın VM kaybında gidebileceği yazılsın.

### E2-07 · önemli · Dal bilgisinin tek taşıyıcısı Batu; planlı taze oturum kartı `source_revision`'ı kaybetmiş
- **Yer:** W1 "Kırılma 1"; MB-15 madde 4; S18.6 ve S18.8 (Ek T5); MB-19 CD-04 ve CD-18; §13.1 PS-2; §14.2 soru 9.
- **Sorun:**
  - **Main'de EXP-007 yok:** EXP-007 main'de yok ve main'de ona işaret eden tek bir satır bile yok. Batu main'den bir oturum açarsa CLAUDE.md, roller, skill'ler ve hook'lar yüklenmez; oturum EXP-007'nin varlığından bile habersizdir.
  - **W1'in düzeltmesi işlemiyor:** W1, dal bilgisinin "README'nin ilk satırı ve STATE'teki adım" ile taşınacağını söylüyor. İkisi de yalnız dalda duruyor; onları okuyabilen oturum dalı zaten biliyordur.
  - **Gerçek taşıyıcı Batu:** Bugünkü STATE bunu açıkça söylüyor: "Batu yeni oturuma dal adını verir." A003'ün "mesaj taşımazsın" sözü bu noktada karşılanmıyor ve bu bağımlılık risk tablosunda adıyla yer almıyor.
  - **Koordinatörün açtığı oturum da aynı yere düşebilir:** T5 S18.6'daki yordam iki adım taşıyordu: `source_revision` = kanonik dal ve "kendi NABIZ tetiklerini sil". Yetkili metin olan MB-15 yalnız "`create_session` + `outcome_branch`" diyor.
    - Araç tanımına göre `source_revision` verilmezse varsayılan dal (main) açılır. Yeni koordinatör yapılandırmasız başlar; kurtuluşu PS-2'nin en belirsiz yoluna ("main'den başlayıp dala geçen" oturum) kalır.
    - Silinmeyen eski nabızlar devirden sonra eski oturumu uyandırır. En iyi ihtimalle bu boşa bir uyanmadır; kötüsünde "iki koordinatör" durağı ve Batu'ya giden bir karar doğar.
- **Kanıt:**
  - `git ls-tree --name-only origin/main explorations/` — EXP-001…EXP-006, CATALOG, INDEX, PACKAGE-CONTRACT; EXP-007 yok — gözledim. `git grep -e EXP-007 -e hopeful-pascal origin/main` — sonuç yok — gözledim.
  - STATE "Yeni oturum ne yapar" 0. adım — "EXP-007 main'de yoktur. Batu yeni oturuma dal adını verir" — kaynak diyor.
  - METHOD W1 Kırılma 1 — "README'nin ilk satırı ve STATE'teki "yeni oturum ne yapar" adımı dal bilgisini taşımaya devam eder" — kaynak diyor.
  - METHOD §10.3 — "Batu: amaç, yetki, kabul, tercih; "mesaj taşımazsın, eksik de aramazsın"" (A003 §3.2) — kaynak diyor.
  - Ek T5 S18.6 "Planlı taze oturum" — "2. Kendi NABIZ tetikleri silinir. 3. `create_session` çağrılır: `source_url` = repo, `source_revision` = kanonik dal, `outcome_branch` = kanonik dal" — kaynak diyor. METHOD MB-15 — "`create_session` + `outcome_branch` ile planlı taze oturum" — kaynak diyor.
  - Bu oturumun `create_session` araç tanımı — "source_revision: Optional git branch, tag, or commit to check out. Requires source_url. Defaults to the repo's default branch." — gözledim.
  - Ek T5 §9 CD-04 — geçme ölçütü "Commit kanonik dalda; yeni dal yok; iki koordinatör kontrolü çalışır"; yapılandırmanın yüklendiğini sınamıyor — kaynak diyor.
- **Öneri:**
  1. MB-15'e T5'in iki adımını geri koy: `source_revision` = kanonik dal; devirden önce kendi NABIZ tetiklerini sil. CD-04'ün geçme ölçütüne "yeni oturumda kanarya ve rol adları görünür" ekle.
  2. W1 Kırılma 1'i düzelt: taşıyıcının Batu olduğunu yaz ve bunu §14.1'e tek arıza noktası olarak ekle.
  3. Batu'ya A-04/O-6 içinde taşıyıcı gerektirmeyen yollar öner:
     - (a) main'de dal adını ve "oradan oku" notunu taşıyan tek satırlık bir işaretçi. Proxy ve K-009 yorumu nedeniyle bunu main'e yazmak Batu'nun işidir.
     - (b) Batu yeni oturum açmak yerine mevcut koordinatör oturumunu sürdürür.
     - (c) Her koordinatör oturumunun başlığına dal adı yazılır (`set_session_title`).
  4. PS-2'ye "Batu arayüzden dalı seçebiliyor mu" denemesi eklensin (§14.2 soru 9 zaten açık).

### E2-08 · önemli · P1'de koordinatör oturumunda `add_repo`, ilk özerk aşamada zorlama katmanını kapatabilir
- **Yer:** §14.3 varsayımlar; §12.2 K-4; MB-07; MB-15 (son çare alarm yolu); W5 3. adım.
- **Sorun:**
  - **Planlanan çok repolu çalışma:** Taslak EXP-007 oturumlarını tek repolu varsayıyor, "P1'deki `add_repo` hariç". K-4'te P1 için Loopinance repolarının salt okuma bağlanmasını istiyor.
  - **Taslağın kendi kaynağına göre sonuç:** Kendi kaynakları, başka bir repo bağlanınca settings katmanının sessizce tavsiyeye düştüğünü söylüyor.
  - **Zamanlama:** P1, K-002 hızının ilk kez devreye girdiği aşamadır. O oturumda düşecek olanlar:
    - durma kapısı (K-002'nin gazı);
    - zarf ve yazma kapıları;
    - SubagentStart'ın taban ve rol belleği enjeksiyonu;
    - SessionStart enjeksiyonu, yani MB-15'in son çare alarm yolu ("bir sonraki açılışta enjeksiyonun ilk satırı");
    - StopFailure kaydı ve deny kuralları (main'e push'u proxy yine keser).
  - **W5'e etkisi:** W5'in "çıktı dosyası varsa tamdır" çıkarımı yazma sınırı hook'una dayanır. O oturumda bu çıkarım geçersizdir.
  - **Eksik kural:** Taslak bunu CD-13 ile ölçmeyi planlıyor, ama repo bağlama işini koordinatör oturumundan ayıran bir kural koymuyor. Bu oturum da P0'da iki Loopinance reposunu bağlamıştı.
- **Kanıt:**
  - METHOD §14.3 — "EXP-007 oturumları tek repoludur (P1'deki `add_repo` hariç)". §12.2 K-4 — "P1'de CD-10, CD-13 ve Loopinance repoları için salt okuma `add_repo`" — kaynak diyor.
  - Ek T2 §5.3 — "Çok repolu oturumda (başka bir repo bağlanırsa) bu satırlar sessizce tavsiyeye düşer [T2-14]." — kaynak diyor (belgeden aktarım; bulutta farklı, denenmedi).
  - Ek T5 §11.1 soru 5 — "Kaybediyorsa P1'deki repo bağlama işleri zorlama katmanını kapatır." — kaynak diyor.
  - METHOD MB-15 — "nabız da çalışmazsa bir sonraki açılışta enjeksiyonun ilk satırıdır". W5 3. adım — "çıktı dosyası varsa tek yazım kuralı gereği tamdır" — kaynak diyor.
  - STATE — "İki Loopinance reposu bu oturuma salt okuma için bağlandı" — kaynak diyor.
- **Öneri:**
  1. Kural koy: koordinatör oturumu `add_repo` yapmaz. Dış repo okuması `e7-arastirmaci`'nin GitHub okuma araçlarıyla ya da yalnız o iş için açılan kısa ömürlü ayrı bir oturumda yapılır; sonuç dala dosya olarak döner.
  2. CD-13, P1'deki ilk repo bağlamasından önce koşan bir kapı olsun. Sonucu kabiliyet haritasına girmeden `add_repo` yapılmasın.
  3. W5'in tamlık çıkarımı "kanarya var" koşuluna bağlansın. Kanarya yoksa her çıktı "dönüşsüz, tamlığı bilinmiyor" sayılsın.

### E2-09 · önemli · Y2'nin dengeleyicisi Y5'i ağırlaştırıyor: koordinatörün kendi bağlamı bütçesiz
- **Yer:** §4.6 "Okuma"; M7.4; M13.6 (≥2 iddia); MB-09 bütçeleri; §11.2; §8.1 Y2 ve Y5; MB-15 (taze oturum); §14.2 soru 5 ve 6.
- **Sorun:**
  - **Dengeleyicinin yükü:** "Ana oturum az okur" seçiminin (Y2) dengeleyicisi koordinatöre derin okuma yüklüyor:
    - her dönüşte en az iki iddiayı kaynağında açmak (dönüş başına ≤30 KB);
    - her TK'de "kendim okudum" yazmak;
    - birleştirme, kayıt ve ölçüm.
  - **Hacim:** Beş ajanlık bir dalga yalnız dönüş kontrolünde en çok ~150 KB demek. Bir sıkıştırma sonrası yeniden okuma 50–100 KB daha ekler.
  - **Aynı aktör darboğaz:** Bu koordinatör aynı zamanda Y5'in (tek koordinatör, tek yazıcı) darboğazıdır.
  - **Bütçe yok:** MB-09'un bütçeleri alt ajanın zorunlu okuması ve açılış seti içindir. Koordinatörün çalışan bağlamı için sayı, ölçü ya da eşik yok.
  - **Görünürlük ve çıkış yolu bilinmiyor:** Koordinatörün kendi doluluğunu görüp göremeyeceği bilinmiyor (CD-10). İkinci sıkıştırmadaki planlı taze oturum da bilinmiyor (CD-04) ve kartı eksik (E2-07).
  - **Bu turda ölçülen:** Ana oturum 792 K'da sıkıştırıldı. Birleştirme ajanı 776 K'ya çıktı ve son bölümleri yeniden okumadan yazdı; METHOD bunu son satırında kendisi söylüyor.
  - **Hüküm:** Bir frenin (derin okuma) bedeli, aynı aktörde başka bir freni zayıflatıyor: sıkıştırmadan korunmayı ve karar kalitesini. §8.1 ise bu iki satırı ayrı ayrı "karşılandı" sayıyor.
- **Kanıt:**
  - METHOD §4.6 — "kendi bağlamını bütçe içinde tutar, ikinci sıkıştırmada planlı taze oturuma geçer (M7.6)" (bütçe değeri yok) — kaynak diyor.
  - METHOD MB-09 "Bütçeler" satırı — koordinatörün çalışan bağlamı için değer yok — kaynak diyor.
  - METHOD §11.2 — "Dönüş | … | 3–5 dk; ≤30 KB okuma" ve "Sıkıştırma | … | 50–100 KB okuma" — kaynak diyor.
  - METHOD §14.2 — "5. Koordinatör kendi bağlam doluluğunu görebilir mi? (CD-10)" ve "6. En az iki iddiayı kaynağında okuma kuralı, … bağlamı gereksiz büyütür mü? (MB-09 ile gerilim)" — kaynak diyor.
  - STATE — "ana oturum 792 K'da sıkıştırıldı (%80)" ve "Birleştirme: … tepe bağlam 776 K (… son bölümler yeniden okumasız yazıldı)" — kaynak diyor (ölçüm).
  - METHOD son satır — "§11–§14 ve Ek, yeni okuma yapılmadan elde edilmiş bilgiyle yazıldı" — kaynak diyor.
  - Dengeleyicinin öteki seçimi zayıflattığı — çıkarım.
- **Öneri:**
  1. **Koordinatöre çalışan bağlam bütçesi koy.** Son sıkıştırmadan bu yana okunan KB ve işlenen dönüş sayısı GUNLUK'tan sayılsın. Eşikte, bir sonraki kalem sınırında ya taze oturuma geçilsin (CD-04 geçtiyse) ya da derin okuma `e7-dogrulayici`'ye devredilsin.
  2. **Dalga başına kontrolü toplu yap.** Beş dönüşün "≥2 iddia" kontrolü tek bir doğrulayıcı koşusunda toplanabilsin (B3, ayrı bağlam). Koordinatör yalnız kararı doğrudan taşıyan tek iddiayı kendisi açsın.
  3. **CD-04 düşerse ne olacağını yaz.** Bugün tek cevap "Batu yeni oturum açar"; bu, E2-10'daki Batu yüküne eklenir.

### E2-10 · önemli · Tek arıza noktaları: koordinatörün oturum dışı bekçisi yok; pilotların bütün yedekleri Batu'ya çıkıyor
- **Yer:** §4.1 koordinatör satırı; MB-15; §13.1 PS-1…PS-4 "Sonuca göre" sütunu; §12.2 "Batu'nun eylemleri"; S20.2 (Ek T5); §14.1 R-1; W9 "Kırılma".
- **Sorun:**
  - **Tek oturumda toplanan işler:** Yazma, sınıflama, ölçüm, alarm, dağıtım, uzak araçlar ve Batu ile konuşma tek oturumdadır.
  - **Dışarıdan fark eden yok:** Oturum takılır, yanlış özetle sıkıştırılır ya da limite takılırsa, onu dışarıdan fark edecek bir şey yoktur; nabız yalnız aynı oturumu uyandırır. Taslak bu boşluğu "o arada Batu tek dedektördür" diye kapatıyor.
  - **Yedeklerin hepsi Batu:** Pilotlar düşerse yedek yine Batu'dur:
    - PS-1 düşerse oturumu Batu açar ve günlük bakar;
    - PS-2 düşerse main'e dosyayı Batu koyar ya da oturumu dalda Batu açar;
    - PS-3 ya da CD-10 düşerse haftalık yüzdeyi her raporda Batu yazar;
    - CD-04 düşerse taze oturumu Batu açar;
    - dal adını Batu taşır (E2-07);
    - deneme oturumlarını ve eski oturumu Batu kapatır.
  - **Toplamı hesaplanmamış:** Tek tek bakıldığında her yedek makul. Birlikte düştüklerinde Batu zamanlayıcı, sensör ve kurye olur. Bu, R11'in "koordinasyon sistemde değilse Batu zamanlayıcıya dönüşür" (E59) dediği ve A003'ün kaldırmayı vaat ettiği durumdur. Taslak yedekleri tek tek yazıyor, toplam Batu yükünü hiçbir senaryoda hesaplamıyor.
- **Kanıt:**
  - METHOD §4.1 — koordinatör: "Remote, GitHub yazma, SendMessage, PushNotification'ın tek kullanıcısı". MB-15 — "alarmı yalnız ana oturum gönderebilir" — kaynak diyor.
  - METHOD W9 Kırılma — "nabız çalışmazsa alarm bir sonraki açılışta enjeksiyonun ilk satırıdır ve o arada Batu tek dedektördür" — kaynak diyor.
  - METHOD §13.1 PS-1 — "CD-03 düşerse oturumu Batu açar … Kanal yoksa sessiz alarm kuralı ve Batu'nun günlük bakışı kalır". PS-2 — "(ii) olmazsa main'e boş `.claude/agents` (K-009 değişikliği; Batu)" — kaynak diyor.
  - Ek T5 S20.2 — "Çalışmıyorsa Batu her aşama raporunda /usage'daki haftalık yüzdeyi bir sayı olarak yazar." S18.6 — "Eski oturumu Batu arşivler." — kaynak diyor.
  - METHOD §12.2 — "Batu'nun eylemleri: O-8 için ortam penceresinde tek ayar · CD-05 için … /goal · CD-15 için … /usage okuması · … /compact · açılan deneme oturumlarını kapatmak · gerekirse oturumu bu dalda açmak." — kaynak diyor.
  - R11 E59 — "Koordinasyon sistemde değilse Batu zamanlayıcıya dönüşür (kanon)." — kaynak diyor.
- **Öneri:**
  1. **§13.1'e bir "yedek yük tablosu" ekle.** Her PS düşüşünde Batu'nun haftalık yinelenen eylemleri yazılsın. PS-1 ile PS-3'ün birlikte düştüğü senaryo için ayrı bir çalışma biçimi Batu'ya açıkça seçenek olarak sunulsun; süreklilik varmış gibi yapılmasın. Örnek: Batu'nun belli saatlerde, bir gündem dosyasıyla açtığı sınırlı oturumlar.
  2. **Oturum dışı, ilerleme ölçen bir bekçi değerlendir.** Günde bir kez taze oturumda koşan bir Routine yalnız dalı okur: GUNLUK'taki son İ olayı ve son OTURUM-ACILIS. Eşik aşılmışsa Batu'ya bildirim gönderir.
     - R11 §4.6 (d)'nin dersi gereği canlılığı değil ilerlemeyi ölçer.
     - Yazma yetkisi yoktur.
     - Bedeli ve limit içinde çalışıp çalışmadığı PS-1'e eklensin.
  3. **Koordinatör riskini üç önlemle karşıla.** Koordinatörün sınıflama yetkisi E2-01'deki örneklemle, bağlamı E2-09'daki bütçeyle denetlensin. Bu iki önlem ve bekçi birlikte "tek koordinatör" riskinin somut karşılığıdır.

### E2-11 · önemli · Bayat kayıt güncel sanılıyor: rol belleği dayanağı sınanmadan enjekte ediliyor, BAYAT-DEVIR ölçütü tanımsız, devir bloğu GUNLUK'u kopyalıyor
- **Yer:** MB-03 1. adım; M8.2 ve M8.5; MB-08 şablonu; MB-02 1.–2. adım; S18.1 3. adım (Ek T5 skill); §6.5 göç.
- **Sorun:** Üç ayrı yerde bayat bilgi güncel diye kullanılabilir.
  - **(a) Rol belleği enjeksiyonu:**
    - `alt-ajan-tabani.sh` rol belleğinin Çekirdek bölümünü "ROL BELLEĞİ — Çekirdek" başlığıyla her çağrıya enjekte eder.
    - Kayıtlar dayanak@SHA taşır, ama enjeksiyon anında dayanağın değişip değişmediğine bakılmaz.
    - Rol belleği tazelikte "yaşla zayıflayan" sınıftadır ve yalnız aşama sonunda gözden geçirilir.
    - Sonuç: aşama içinde yerine konmuş bir K'ya ya da §6.5 göçüyle taşınan bir yola dayanan kayıt, en yüksek görünürlükle her çağrıya girer.
  - **(b) BAYAT-DEVIR sınaması:**
    - Açılıştaki "devir iddiadır" sınaması şunu soruyor: son kapanıştan sonra başka commit var mı; çelişki var mı?
    - Dalga, brief ve karar commit'leri ile ortam hook'unun zorladığı commit'ler (E2-03) yüzünden, son kapanıştan sonra hemen her açılışta commit vardır.
    - Neyin "çelişki" sayılacağı tanımlı değil. Sınama ya her açılışta BAYAT-DEVIR üretir (gürültü) ya da koordinatörün yorumuna kalır.
  - **(c) Devir bloğundaki kopya:**
    - Devir bloğu "dönmemiş G" listesini taşıyor, ama blok yalnız kalem kapanışında güncelleniyor.
    - Dağıtım kalemin ortasında olduğu için liste, dağıtımla kapanış arasında bayattır.
    - Yetkili kaynak GUNLUK'tur. Bu kopya, ilke 4'ün ("başka yerde işaretçi durur") yasakladığı türdendir ve hook'un olmadığı oturumda okunan tam da bu kopyadır.
- **Kanıt:**
  - METHOD MB-03 — "1) Tek repolu oturumda `alt-ajan-tabani.sh` Çekirdek bölümünü "ROL BELLEĞİ — Çekirdek" başlığıyla enjekte eder" — kaynak diyor.
  - METHOD §3 S8 — "Ortak kayıt şeması (köken, dayanak@SHA, iki zaman, statü)" — kaynak diyor.
  - Ek T1 M8.5 — "T3 yaşla zayıflayan | Çıkarım ve gözlem türü dersler; rol belleği maddeleri | Aşama sonu bakımında gözden geçirilir" — kaynak diyor.
  - Ek T5 S18.1 skill 3. adım — "Devir bloğundaki "son kapanış" commit'i git log'da var mı; sonrasında başka commit var mı? Çelişki varsa git'e güven, bloğu düzelt ve olay günlüğüne `BAYAT-DEVİR` yaz." — kaynak diyor.
  - METHOD MB-02 — "1) DAGITIM dağıtımdan önce yazılır, dalga başına tek commit" — kaynak diyor.
  - METHOD MB-08 şablonu — "Açık yükler: dönmemiş G: <…>" ve "Ne zaman: her kalem kapanışında, her DURAK'ta, devirden önce yazılır" — kaynak diyor. İlke 4 — "Bir bilgi tek yerde yetkilidir; başka yerde işaretçi durur" — kaynak diyor.
  - Sınamanın hemen her açılışta tetikleneceği ya da yoruma kalacağı — çıkarım.
- **Öneri:**
  1. `alt-ajan-tabani.sh` her Çekirdek kaydı için `git diff --quiet <sha> HEAD -- <yol>` koşsun. Dayanak değişmişse kayıt "YENİDEN-BAK: dayanak değişti" etiketiyle enjekte edilsin. Bedeli milisaniyelerdir.
  2. Devir bloğundan "dönmemiş G" kopyasını kaldır; yerine "açık G: GUNLUK'tan hesaplanır" işaretçisi koy. Hook yoksa hesap, T5'in açılış skill'indeki awk satırıyla yapılsın.
  3. BAYAT-DEVIR'i betikle tanımla. Son kapanıştan sonra DECISIONS, PLAN, ISLER ya da KAPI'ya dokunan bir commit varsa ve blok o commit'te güncellenmemişse devir bayattır. Dalga ve brief commit'leri sayılmaz.

### E2-12 · önemli · §8, R11'in etkileşim matrisini kenar düzeyinde kullanmıyor
- **Yer:** §8 (8.1–8.4); §6.3 kimlik tablosu; §1 "Kabul ölçütü" (4).
- **Sorun:**
  - **Kabul ölçütü:** ORTAK-SENTEZ'in 4. kabul ölçütü "R11'in etkileşim matrisi kullanılır" diyor.
  - **Kullanılan ve kullanılmayan kısım:** §8, R11 §5'in 20 seçimini, §4.5'in döngülerini ve §4.6'nın olaylarını eşliyor. §4.2'deki matris ve §4.4'teki 101 kenar ise hiçbir yerde tek tek bir karta bağlanmıyor. Bu yüzden "hangi kenar hangi kartla kesildi, hangisi pilota bağlı, hangisi canlı" sorusunun cevabı taslakta yok.
  - **Elle eşlemenin sonucu (§2.2):** En çok giriş alan beş alt sistemin 49 kenarını elle eşledim:
    - 31'i somut bir kartla kesiliyor;
    - 2'si yalnız pilota bağlı;
    - 1'i kabul edilmiş kalıntı risk;
    - 15'i bu incelemenin bulgularıyla kısmen canlı.

    Sistematik bir eşleme bu 15 kenarın çoğunu birleştirme sırasında yakalardı.
  - **Kimlik aralığı hatalı:** §6.3, R11 kenarlarını "E01–E113" diye anıyor; R11'de kenarlar E101'de bitiyor.
- **Kanıt:**
  - ORTAK-SENTEZ "Batu'nun ölçütü" 4 — "Bir alt sistemdeki seçimin başka alt sistemleri nasıl etkilediği yazılır. R11'in etkileşim matrisi kullanılır." — kaynak diyor.
  - R11 §4.3 — "Toplam 101 kenar" — kaynak diyor. R11'de E101'den büyük kenar kimliği yok (grep) — gözledim.
  - METHOD §6.3 — "Y1–Y20 · E01–E113 · R11 Knn" — kaynak diyor.
  - §2.2'deki eşleme — gözledim (kart metinleriyle); canlılık hükmü çıkarımdır.
- **Öneri:** §8'e bir kenar tablosu ekle. Her kenar için kaynak taraftaki kart, zorlama düzeyi (zr, zr¹, ys, tv) ve pilot bağımlılığı yazılsın. "Canlı" kalan kenarlar §14'e risk olarak geçsin. §6.3'teki aralık E01–E101 olarak düzeltilsin.

### E2-13 · küçük · Rol dosyası çalışma sürerken değişince yürürlük anı üç yerde farklı yazılmış; hiçbir CD sınamıyor
- **Yer:** §12.4 CLAUDE.md §3; MB-14 tablosu; M11.6 (Ek T2); MB-07 `yapilandirma-dondurma.sh`; MB-19.
- **Sorun:**
  - **Üç ayrı ifade:**
    - CLAUDE.md: "yapılandırma değişikliği sonraki oturumda yürürlüğe girer".
    - MB-14, rol gövdesi için: "sonraki çağrı ya da oturum".
    - T2 M11.6: platform rol dosyasını bir sonraki çağrıda yeni haliyle kullanır.
  - **Dondurma dar:** Dondurma hook'u yalnız settings ve skill değişikliğini kapsıyor.
  - **T2 haklıysa:** Sürekli izinle ya da Batu onayıyla yapılan bir rol değişikliği, regresyondan önce, bir sonraki dağıtımda devreye girebilir. CLAUDE.md'nin cümlesi de yanlış olur.
  - **T2 haksızsa:** SubagentStart'ın diskten hesapladığı "rol sürümü ve özeti" çalışan tanımı göstermez ve M11.6'nın köken kaydı bozulur.
  - **Sınama yok:** CD-18 yalnız açılıştaki yüklemeyi sınıyor.
- **Kanıt:**
  - METHOD §12.4 CLAUDE.md §3 — "Yapılandırma değişikliği sonraki oturumda yürürlüğe girer." — kaynak diyor.
  - METHOD MB-14 — "… | sonraki çağrı ya da oturum" — kaynak diyor.
  - Ek T2 M11.6 — "Rol dosyası değişince bir sonraki çağrı yeni tanımı kullanır, yeniden başlatma gerekmez; çalışan örnek eski tanımla biter [T2-05]" — kaynak diyor (belgeden aktarım; bulutta denenmedi).
  - METHOD MB-07 — "`yapilandirma-dondurma.sh` | ConfigChange | … | settings ve skill değişikliği bu oturumda uygulanmaz" — kaynak diyor.
- **Öneri:**
  1. Tek bir kural yaz: rol dosyası yalnız açık dağıtım yokken ve regresyon (M11.7) geçtikten sonra değişir; değişiklik commit'i regresyon kaydını işaret eder.
  2. MB-19'a bir CD ekle: oturum ortasında bir deneme rolünde zararsız bir satır değişir; sonraki çağrının hangi sürümle koştuğu, zarftaki sürüm ile dosya özeti karşılaştırılarak bulunur.

### E2-14 · küçük · İki Batu kararı çelişince YT-9 ile K-9 önerisi uzlaşmamış
- **Yer:** MB-08 ZARF YT-9; §12.2 K-9; M8.6 (Ek T1).
- **Sorun:**
  - **İki kural:** YT-9, "Batu'nun iki kararı çelişiyor" durumunu Batu'ya yükseltir. K-9 ise "Batu'nun sonraki sözü öncekinin yerine geçer" kuralını ve etkilenen eski kararın ana oturumca işaretlenmesini öneriyor.
  - **Belirsizlik:** K-9 kabul edilirse hangi çelişkinin YT-9'a gideceği, hangisinin sessizce çözüleceği belirsizleşir.
  - **Sınıflayan ana oturum:** Çelişki türünü (görünür, gerçek, değer) de ana oturum sınıflar. M8.6 ise "latest wins"i genel bir doğruluk kuralı saymıyor.
  - **Sessizlikte yetki:** Batu sessizken "hangi eski karar etkilendi" yorumu fiilen yetki olur.
  - **Açık hücre:** K-9'un "onay verilmezse" hücresi iki zıt davranışı "ya da" ile bırakıyor.
- **Kanıt:**
  - METHOD MB-08 — "YT-9 Batu'nun iki kararı çelişiyor" — kaynak diyor.
  - METHOD §12.2 K-9 — ""Batu'nun sonraki sözü öncekinin yerine geçer" kuralı … Etkilenen eski karar işaretlenir ve bir sonraki raporda gösterilir" ve "Her çakışma soru olur (yük) ya da sessizce "en yeni kazanır" uygulanır (risk)" — kaynak diyor.
  - Ek T1 M8.6 — ""Latest wins" genel bir doğruluk kuralı değildir [T1K-46]" — kaynak diyor.
- **Öneri:**
  1. K-9'u yalnız aynı konuda, Batu'nun kendi sözüyle açıkça yerine koyduğu durumlara sınırla.
  2. Öteki bütün Batu–Batu çelişkileri YT-9 ile gitsin. Ana oturumun "görünür çelişki" diyerek kendisi çözdüğü her K çelişkisi bir sonraki raporda ayrı satırda listelensin.
  3. "Onay verilmezse" hücresi tek bir davranış seçsin (öneri: soru olur).

### E2-15 · küçük · Talimat biçimli metin "keşfedilen iş" üzerinden aklanıp açılış enjeksiyonuna taşınabilir
- **Yer:** MB-05 (KEŞFEDİLEN İŞ, KAYNAK BOŞLUĞU, TALİMAT-BİÇİMLİ METİN); MB-08 ZARF md. 1 ve md. 6; M8.9; MK-4.4.
- **Sorun:**
  - **Aklanma yolu:**
    - İşçi, kaynaktaki talimat biçimli satırı doğru biçimde TALİMAT-BİÇİMLİ METİN alanına yazsa da aynı içeriği "X yapılmalı" diye KEŞFEDİLEN İŞ alanına da koyabilir.
    - Koordinatör kalem açmayı kendiliğinden yapabilir.
    - Açılan kalem, "sıradaki yetkili iş (dayanak: İK-…)" dayanak sınamasını geçer ve devir bloğuyla her açılışta enjekte edilir.
  - **Eksik korumalar:** Yazarken süzgeç (M8.9) yalnız bellek yazımına uygulanıyor. ZARF md. 6'nın "otomatik istemler yetki değildir" listesinde SessionStart enjeksiyonu yok.
  - **Yeniden açılan yol:** R11 E77'nin tarif ettiği yol (eski "sıradaki" satırları planı eski yöne çeker) bu kanaldan yeniden açılabilir.
- **Kanıt:**
  - METHOD MB-08 md. 1 — "Kendiliğinden: … kalem açma ve kapama" — kaynak diyor.
  - METHOD MB-08 md. 6 — "Otomatik istemler (alt ajan dönüşü, görev bildirimi, NABIZ, Routine, webhook) yetki değildir." — kaynak diyor.
  - METHOD §3 S8 — "Yazarken süzgeç ve geri okuma | … | dış talimat belleğe sızar" — kaynak diyor.
  - R11 E77 — "Eski "sıradaki" satırları talimat sayılırsa plan eski yöne çekilir (K-004)." — kaynak diyor.
  - Aklanma yolu — çıkarım.
- **Öneri:**
  1. KEŞFEDİLEN İŞ'ten açılan kalemin köken alanı (MK-4.4) zarfı ve kaynak yerini göstersin.
  2. Kaynak yeri TALİMAT-BİÇİMLİ METİN alanında da geçiyorsa, kalem amaç zincirinden bağımsız bir gerekçe yazılmadan "kabul"e geçmesin.
  3. ZARF md. 6'ya "SessionStart ve SubagentStart enjeksiyonları" eklensin.

### E2-16 · küçük · Çalışan ajana giden düzeltmenin metni kaydedilmiyor
- **Yer:** M12.6 5. adım (Ek T2); M13.5; W6 3. adım.
- **Sorun:**
  - **Kaydedilen yalnız zaman:** Karar yayılımında koordinatör çalışan ajana SendMessage ile düzeltme gönderir ve deftere yalnız "bildirildi <zaman>" yazar.
  - **Brief artık görevi tanımlamıyor:** Ajanın fiilen çalıştığı görev artık brief@sha değildir.
  - **Etkisi:** Brief ve dönüş kaydının (M13.5) yeniden çalıştırılabilirlik amacı zarar görür. Dönüşteki TABAN uzlaştırması da gönderilen metni görmeden yapılır.
- **Kanıt:**
  - Ek T2 M12.6 — "5) Deftere "bildirildi <zaman>" yaz." — kaynak diyor.
  - METHOD §3 S13 — "Brief ve dönüşlerin kaydı | gerekli | yeniden çalıştırılamama | her G brief@sha ve zarfla bulunuyor" — kaynak diyor.
- **Öneri:** Gönderilen metin brief'e "## Görev içi düzeltmeler" bölümü olarak yeni bir commit'le eklensin (brief v1.1). Zarfın BRIEF alanı bu sürümü göstersin.

## 2. Dengeleyicilerin sınanması

### 2.1 R11 §5: yirmi seçim
Hüküm ölçeği:
- **Somut:** kart, şablon ya da ölçü var; tetiği sürücüden bağımsız ya da mekanik.
- **Zayıf:** kart var, ama tetik sürücüde, pilota bağlı ya da bir bulgu onu deliyor.
- **Yok:** dengeleyici yok.

| Seçim | R11'in istediği dengeleyici | Taslaktaki yer | Hüküm |
|---|---|---|---|
| Y1 Kısa sohbet | rapor, bağlantılar, kabul paketi; "kısa" ile "görünmez" aynı şey değil | S2-M2, S2-M4, S2-M5 | zayıf: raporun okunduğunu gösteren işaret yok, kanal bilinmiyor (E2-02) |
| Y2 Ana oturum az okur | kaynaktan kontrol, birlikte okuma, birleştirme sözleşmesi, nitelikli dönüş | M7.4, M13.6, MK-6.5, M12.4, MB-05 | somut; ama Y5'i ağırlaştırıyor (E2-09) |
| Y3 Geçici ajanlar | kalıcı rol, rol belleği, brief yalnız değişken | §4, MB-03, MB-04 | somut; yüklenmesi PS-2'ye bağlı, bellek tazeliği açık (E2-11) |
| Y4 Üç tekrar kuralı | iskelet şimdi, özel roller kanıtla | M11.1, MB-18 | somut |
| Y5 Tek koordinatör | yazma devri, gerekçe repoda, bağlam bütçesi, taze oturum | MB-01, MB-03, M11.9, MB-02, M7.6, MB-15 | zayıf: koordinatörün bağlam bütçesi yok; taze oturum bilinmiyor ve kartı eksik (E2-07, E2-09) |
| Y6 Aynı modelle karşı-okuma | duyarlılık sınaması, bağımsızlık beyanı, "kimse bağımsız doğrulamadı" satırı | S14-M2, B0–B5, S14-M5, S2-M4 | somut; kabulün "Tamam"la bu etikete yaslanması açık (E2-02) |
| Y7 Riske orantılı kontrol | "bu çıktıya kaç karar dayanacak" sorusu | MB-12 (b) | zayıf: soru yalnız açılışta soruluyor; sınıflamayı tek aktör yapıyor (E2-01) |
| Y8 En çok üç eleştiri turu | park kaydı, yükseltme, açık bulgular, akıbet | S14-M4, MK-5.9, MB-13 §5 | somut |
| Y9 Tek ekranlık durum | işaretçi ve statü; devir notu git'le sınanır | MB-08, S18.1 | zayıf: sınama ölçütü tanımsız; blok GUNLUK'u kopyalıyor (E2-11) |
| Y10 Her şeyi repoya yaz | tek kaynak, dosya görevleri, açılış bütçesi, hijyen | M9.2, MB-09, M8.7, M9.7, §6.4 | somut (ölçülebilir sınırlar) |
| Y11 Sorular birikir | etkilenen kalem işareti; çerçeve sorusu biriktirilmez | MB-11 | somut; ama soru sınıfını tek aktör seçiyor ve sessizlik fren değil (E2-01, E2-02) |
| Y12 Kendiliğinden geçiş | ilerleme ölçüsü, takılma alarmı, yön kontrolü, P4 durağı | MB-08, S17-M2, S17-M3, §7, MB-15 | zayıf: frenlerin hepsi sürücü beyanıyla çalışıyor (E2-01) |
| Y13 Hatırlatma sayısı | eşli ölçüler | S2-M6, S21.6, MK-3.8 | somut; ama "kabulde bulunan açık" ölçüsü Batu'nun bakmasına bağlı (E2-02) |
| Y14 Her okumaya kayıt | yalnız karar taşıyan okuma; "neyi değiştirdi" alanı | MK-6.3 | somut |
| Y15 Kaynağı brief seçer | "şu alana bakılmalı" bildirimi; eksik-arayıcıya bağımsız alan | MK-6.9, MB-05, MK-4.5 | somut görünüyor; MK-4.5'te alanı kimin seçtiğine bakmadım |
| Y16 Sormak son seçenek | otomatik seçim kaydı, toplu sunum | S1-M3 | zayıf: birikim sınırı yok, P4'te toplu kabul var (E2-02) |
| Y17 Ders CLAUDE.md'ye | yer merdiveni, davranış doğrulaması | S21.2, MB-06, S21.5, S15-M1 | somut |
| Y18 Çok sayıda rol | işten türetme, az sayı, sürüm, gözden geçirme tetiği | M11.1, M11.6, MB-18 | somut; değişikliğin yürürlük anı tutarsız (E2-13) |
| Y19 Hook'larla güvenlik | zorlama haritası; hook yalnız bilinen noktalara | MB-07, M16.7, kanarya | zayıf: ortamın Stop hook'u haritada yok (E2-03); P1'de katman düşebilir (E2-08) |
| Y20 Paralel çok ajan | paralellik bütçesi, bağımsızlık koşulu, birleştirme sözleşmesi | M12.2, MB-10, M12.4 | zayıf: ölçüm harcamadan sonra yapılıyor; limitte ortak-kip arızası var (E2-06) |

**Sayım:** 11 somut, 1 somut görünen (Y15), 8 zayıf, 0 yok.

§8.1'in "her satırda fren, seçimin yanına kurulu bir karttır" cümlesi doğru. Ama sekiz kart, düşmanca koşulda çalışacak kadar somut değil.

### 2.2 R11 §4 matrisi: en çok giriş alan beş alt sistemin kenarları
**Seçim:** R11 §4.3'e göre giriş sayısı en yüksek beş alt sistem: S14 (12), S2 (11), S5 (9), S18 (9), S12 (8). Toplam 49 kenar.

**Yöntem:** Her kenar için kaynak alt sistemdeki mekanizmanın taslaktaki karşılığına baktım.

| Alt sistem (giriş) | Somut kartla kesilen | Pilota bağlı | Kabul edilmiş kalıntı | Bulguyla kısmen canlı |
|---|---|---|---|---|
| S2 Batu (11) | E17, E24, E44, E50, E72, E99 | E01 (PS-1) | — | E59 (E2-10), E70 (E2-01, E2-04), E82 (E2-11), E85 (E2-07) |
| S14 KG (12) | E05, E15, E46, E49, E56, E93, E94 | — | E71 (R-4, aynı model) | E08 (E2-02), E19 (E2-04), E29 (E2-05), E63 (E2-03) |
| S5 Plan (9) | E03, E10, E12, E18, E42, E86 | — | — | E73 (E2-05), E77 (E2-15), E80 (E2-01) |
| S18 Süreklilik (9) | E02, E23, E36, E48, E60 | E91 (PS-1) | — | E32 (E2-05), E41 (E2-11), E96 (E2-07, E2-09) |
| S12 Orkestrasyon (8) | E06, E25, E31, E54, E65, E88, E90 | — | — | E95 (E2-06) |
| **Toplam 49** | **31** | **2** | **1** | **15** |

**Kapsam dışı:** Kalan 52 kenarı sınamadım.

**Gözlem:** R11 §4.3'ün "Batu bir havuz" tespiti taslakta da geçerli. S2'ye giren 11 kenarın 4'ü, bu incelemenin bulgularıyla hâlâ canlı.

## 3. Çarpışma testleri: düşmanca yürüyüş

Her satır W1–W10'dan birine E2 brief'indeki kötü koşullardan birini ekler ve düzenin kırıldığı adımı gösterir. Brief'in dokuz koşulunun hepsi yürütüldü.

| W | Eklenen kötü koşul | Kırıldığı adım | Eksik ya da delik mekanizma | Bulgu |
|---|---|---|---|---|
| W1 | Yeni oturum main'den açılıyor, dal adını bilmiyor | 1. adım: CLAUDE.md, rol, skill ve hook yüklenmez; W1'in düzeltmesi dalda duran dosyalara dayanıyor | main'de işaretçi ya da Batu'dan bağımsız bir taşıyıcı | E2-07 |
| W1 | Devir bloğu bayat (dağıtımdan sonra, kapanıştan önce) | 2. adım: "son kapanıştan sonra commit" ölçütü tanımsız; hook yoksa bloktaki bayat G listesi okunur | betikli BAYAT-DEVIR; blokta kopya yok | E2-11 |
| W2 | İşçi brief'in bir kısmını yapıp "TAMAM" diyor | 7. adım: M13.6 bitti tanımına karşı ölçmüyor; R0/R1'de K katıyla kapanır | zarfta bitti tanımı karşılığı; M13.6 adımı | E2-04 |
| W2 | İşçi iş ortasında sıkıştırılıyor | 5.–6. adım: sıkıştırma zarfta görünmez; okuma kapsamı özetten yazılabilir | ortak sözleşmede sıkıştırma yönergesi; zarf alanı | E2-05 |
| W2 | Paralel dalgada bir işçi dosyasını yazdı, dönüşü bekleniyor; koordinatörün turu bitiyor | 8. adım: ortamın Stop hook'u kontrol edilmemiş çıktıyı commit ettiriyor | kayıt ile kabulün ayrılması | E2-03 |
| W2 | Kaynakta talimat biçimli metin var | 7. adım: talimat raporlanır, ama aynı içerik "keşfedilen iş"ten kaleme dönebilir | köken kontrolü; ZARF md. 6 | E2-15 |
| W3 | Batu günlerce sessiz | 7.–8. adım: kendiliğinden geçişte kapı hükmünü ana oturum verir; rapor okunmasa da geçiş olur; tercih borcu birikir | Batu temas ölçüsü; sessizlik tetiği | E2-02 |
| W3 | Bir kalemin sınıfı düşük tutulmuş | 3. adım: bütünsel inceleme yalnız R3 çıktıda yapılıyor; alt sınıflanmış çıktı kapıdan incelenmeden geçer | sınıflama örneklemi | E2-01 |
| W4 | Koordinatör dalganın ortasında sıkıştırılıyor | "Sonra": dosyadan kurulum çalışır, ama sıkıştırma sonrası öz-denetim METHOD'da yok; 50–100 KB yeniden okuma ikinci sıkıştırmayı yaklaştırır | S15-M5 tetiği; koordinatör bütçesi | E2-05, E2-09 |
| W4 | Bir işçi sıkıştırılıyor | yürüyüş yok | alt ajan kolu | E2-05 |
| W5 | Haftalık limit dalganın ortasında doluyor | 1.–2. adım: nabızlar limit içinde tükenir; uyandıracak ve haber verecek aktör kalmaz | tüketilmeyen uyandırma; limitten önce durma | E2-06 |
| W5 | Koordinatör planlı taze oturumla yenileniyor | yeni oturum main'i açar (`source_revision` yok); eski nabızlar eski oturumu uyandırır | MB-15'e T5'in iki adımı | E2-07 |
| W5 | Oturum `add_repo` ile çok repolu | 3. adım: "çıktı varsa tamdır" çıkarımı hook'a dayanır, geçersizdir | koordinatör oturumunda `add_repo` yasağı | E2-08 |
| W6 | SendMessage işlemiyor (PS-4 düşer) | 3. adım: bildirim ulaşmaz; 5. adımda TABAN farkıyla geç yakalanır; iş boşa gider ama yanlış karara girmez | — (taslağın yedeği yeterli) | — |
| W6 | Batu'nun iki kararı çelişiyor | 1. adım: YT-9 mu K-9 mu işleyecek, belirsiz | öncelik kuralı | E2-14 |
| W6 | Düzeltme mesajı gönderildi | 3. adım: mesajın metni kaydedilmiyor | brief v1.1 | E2-16 |
| W7 | Çöken varsayım V-H-2 (Batu'nun dikkati) | 1. adım: bu varsayımın çöktüğünü gösteren ölçü yok; protokol tetiklenmez | V-H-2 izlemesi | E2-02 |
| W8 | Batu'nun itirazı eski bir K ile çelişiyor | 4. adım: iş W6'ya gider; oradaki belirsizlik burada da geçerli | öncelik kuralı | E2-14 |
| W9 | Koordinatör kararları bölerek "ilerliyor" | 1. adım: İ olayı üretildiği için eşik dolmaz | bağımsız İ tanımı; betikli eşik | E2-01 |
| W9 | Koordinatör ölü, oturum çok repolu | "Kırılma": son çare yol olan açılış enjeksiyonu da düşer | oturum dışı bekçi; `add_repo` yasağı | E2-08, E2-10 |
| W10 | Ders, rol çalışırken bir rol gövdesi değişikliğiyle işleniyor | 3. adım: yürürlük anı belirsiz; sürüm kaydı yanlış olabilir | tek yürürlük kuralı; CD | E2-13 |
| W10 | Canlı örnek L-001 | 5. adım: kanıt, T5'in dönüşten önce atılan commit'ini içeriyor | gözlem cümlesinin düzeltilmesi | E2-03 |

**Dayanıklı çıkan adımlar:**
- W6'da SendMessage olmadan çalışan TABAN yedeği;
- W4'te koordinatör için "karar bir sonraki araç çağrısından önce dosyada" kuralı ve compact enjeksiyonu;
- W7'nin ekleme-yalnız DEĞ ve SAP kaydı;
- W8'in itiraz protokolü;
- W10'un yer merdiveni;
- W5'te hook'lar yüklüyken GUNLUK'tan açık G hesabı.

## 4. Döngüler

### 4.1 R11 §4.5'in dört döngüsü

| Döngü | Taslağın kırıcısı (§8.2) | Hüküm |
|---|---|---|
| 1 Şişme | ölçülebilir sınırlar (CLAUDE.md ≤100 satır, enjeksiyon ≤4.000 karakter, blok ≤40 satır, K0 ≤30 KB, açılış ≤50 KB); tek kaynak; emeklilik | frenli: ölçüler mekanik, eşikler yazılı. Tek sızıntı koordinatörün çalışan bağlamı (E2-09). |
| 2 Öz-onay | Y katı sayılmaz; "doğrulandı" B3'e bağlı; MB-08 frenleri; aşama sonu iz denetimi | frenlenmiyor: İ olayları, sınıf, eşik ve alarm aynı aktörde; S17-M2'nin karşı önlemi METHOD'a taşınmamış (E2-01). |
| 3 Batu yükü | keşif sistemde (MK-4.1, MK-4.5); dikkat bütçesi; "sistem yakalayabilir miydi" sorusu | kısmen: keşif halkası frenli; "Batu'nun dikkati tükenir" halkası ölçülmüyor ve pilot yedekleri Batu'ya dönüyor (E2-02, E2-10). |
| 4 Kural birikimi | yer merdiveni; hook ≤9, skill ≤10 ve her biri ≤120 satır, CLAUDE.md ≤100 satır; emeklilik | frenli: merdiven basamağını ana oturum seçse de sayısal tavanlar büyümeyi mekanik olarak sınırlıyor. |

### 4.2 Yeni döngüler
1. **Sessiz onay döngüsü** (brief'teki örnek):
   - Aynı modelin kontrolü K ve Ç katı üretir.
   - Raporlar "sorun yok" der.
   - Batu okumayı azaltır; zaten okumak zorunda değildir.
   - T kararları "itiraz yok" diye birikir ve sonraki iş onların üstüne kurulur.
   - P4'te tek bir "Tamam" hepsini kabule taşır.
   - **Kırıcı:** yok (E2-02).
2. **Limit–yeniden dağıtım döngüsü:**
   - Limit dolar ve işçiler kaybolur.
   - Kör tekrar yasağı kayıp işe uygulanmaz; aynı derin brief'ler yeniden dağıtılır.
   - Limit yeniden dolar.
   - **Kırıcı:** kısmen var. İkinci kayıpta sarı alarm, üçüncüde devre kesici çalışır (W5 5. adım). Ama sayacın kalem başına mı dalga başına mı işlediği yazılı değil; beş kalemin her biri bir kez kaybolursa hiçbiri eşiğe ulaşmaz (E2-06).
3. **Koordinatör sıkıştırma döngüsü:**
   - Derin okuma ve dönüş kontrolleri koordinatörün bağlamını doldurur.
   - Sıkıştırmadan sonra 50–100 KB yeniden okunur ve ikinci sıkıştırma gelir.
   - Taze oturum bilinmiyor ve kartı eksik; o yoksa döngü sürer.
   - **Kırıcı:** M7.8'in "thrashing 0" hedefi var, ama frenin kendisi pilota bağlı (E2-07, E2-09).
4. **Sınıflama döngüsü:**
   - Düşük sınıf, az kontrol demektir; az kontrol az bulgu üretir.
   - R-4'ün belirtisi ("eleştiriler hep küçük bulgu döndürür") kaliteye yorulur ve düşük sınıf haklı görünür.
   - **Kırıcı:** yok (E2-01).
5. **Özetten zarf döngüsü (alt ajan):**
   - Büyük okuma işçiyi sıkıştırmaya iter; zarf özetten yazılır.
   - İki iddialık örneklem geçer ve özetten türemiş bir iddia karara girer.
   - Uzlaştırma için daha çok okuma gerekir.
   - **Kırıcı:** yok (E2-05).

## 5. Tek arıza noktaları

### Ana oturum
Tek başına sahip olduğu işler:
- kanonik yazım;
- sınıflama: R0–R3, M/T/Y, soru ve çelişki sınıfı, yayılım etkisi;
- eşik hesabı, alarm gönderimi ve ölçüm;
- dağıtım;
- uzak araçlar: oturum, tetik, bildirim;
- Batu ile konuşma.

| Arıza biçimi | Taslaktaki karşılık | Durum |
|---|---|---|
| Oturum ölür (VM) | Nabız aynı oturumu uyandırır (PS-1'e bağlı); GUNLUK'tan kurtarma var | karşılık var, denenmedi |
| Limit dolar | Nabız, alarm ve DURAK birlikte susar (E2-06) | karşılık yok |
| Yanlış özetle sıkıştırılır | Dosyadan yeniden kurulum ve S1–S5 soruları var; sıkıştırma sonrası öz-denetim düşmüş (E2-05) | kısmen |
| Kendi beyanıyla yanılır (sınıf, ilerleme, alarm) | Bağımsız örneklem yok (E2-01) | karşılık yok |
| Takılır ama canlıdır (ör. hook döngüsü, bekleyen istem) | Durma kapısı ve ortam hook'u "bir kez" engeller; Auto kipi önerisi (O-8) var; dışarıdan fark eden yok (E2-10) | kısmen |
| Çift koordinatör oluşur | `list_sessions` sınaması var; taze oturum kartı eksik (E2-07) | kısmen |

### Batu
Tek başına sahip olduğu işler:
- amaç, yetki ve kabul;
- sistemin aynı modelden olmayan tek denetçisi olmak;
- uyanma çalışmazsa oturumu açmak;
- dal adını taşımak;
- CD-10 düşerse limit ve haftalık yüzde sensörü olmak;
- kanal yoksa alarmın tek alıcısı olmak;
- deneme oturumlarını ve dalları temizlemek.

Yokluğunda ne olur:
- **P0'da:** iş durur (K-005). Bu doğrudur.
- **P1–P3'te:** iş sürer, ama denetimsiz birikir (E2-02).
- **Pilotlar da düştüyse:** süreklilik de durur (E2-10).

Taslak, Batu'nun yokluğunu bir durum olarak tanımlamıyor.

### Gizli tek noktalar
- **`tools/token-kullanimi.py`:** tek maliyet sensörü. Transcript'e bağlı; transcript'in VM kaybından sonra korunup korunmadığı bilinmiyor (E2-06).
- **`oturum-baglami.sh`:** her oturumun ilk bağlamını üretir. Kanaryanın yokluğu yakalanır, yanlış içerik yakalanmaz; MB-07 bozulma işareti olarak yalnız "hep yanlış engelleyen hook"u anıyor.
- **GUNLUK:** aşama başına tek dosya, ama git geçmişiyle korunuyor. Sorun değil.

## 6. "Özellikle bak" soruları

### Hız varsa fren: K-002, ilerleme ölçüsü ve takılma alarmı birbirine bağlı mı?
**Kâğıt üzerinde evet.** ZARF md. 4 frenleri sayıyor. S17-M2 → S17-M3 → MB-15 zinciri ve sessiz alarm kuralı yazılı. Nabız ilerlemeye bağlı.

**Ama bağ tek yönlü ve kendinden tahrikli:**
- P1–P3'te ilerleme olaylarını, eşik mesafesini, sınıfı ve alarmı aynı aktör üretiyor.
- Sessiz alarm kuralı ve bütçe durağı mekanik değil.
- Çok repolu oturumda son çare alarm yolu düşüyor.

Bu haliyle fren, sürücünün "fren gerekiyor" demesine bağlı (E2-01, E2-08).

### Bağlam, bellek ve kayıt mimarisi birlikte W4 ve W5'i kurtarıyor mu?
**W4:** Koordinatör için büyük ölçüde evet. Karar anında yazım, Compact Instructions, compact enjeksiyonu ve S1–S5 soruları birbirini tamamlıyor. Alt ajan tarafı yürütülmemiş ve sıkıştırma sonrası öz-denetim düşmüş (E2-05).

**W5:** Hook'lar yüklüyken GUNLUK, tek yazım ve TABAN ile kurtarılabilir. Kırıldığı yerler:
- yeni oturumun dalı bulması (E2-07);
- limit (E2-06);
- çok repolu oturum (E2-08);
- zarfın varlığı içeriğin tamlığını değil, işçinin beyanını gösteriyor (E2-04);
- dönüşten önce zorla commit (E2-03). Bu, W5'in dayanıklılığına yardım eder ama M13.6'ya zarar verir.

### W6: K-010 olayı taslakla tekrar yaşanır mı?
**Hook'lar yüklü ve PS-4 geçerse büyük ölçüde hayır.** Zincir şöyle işliyor:
1. Karar önce dosyaya yazılır, sonra yayılır.
2. Açık G listesi çıkarılır.
3. Etkilenen ajana adla SendMessage gider ya da ajan durdurulup yeniden başlatılır.
4. Yeni ajan SubagentStart'la güncel tabanı alır.
5. Geç dönüşte TABAN farkı uzlaştırılır.

SendMessage işlemese bile TABAN farkı dönüşte yakalanır; iş boşa gider ama yanlış karara girmez.

**Kalan açıklar:**
- Etki sınıfını (etkilemez / bildir / durdur) ana oturum tek başına seçiyor (E2-01'in sınıflama noktası).
- Çok repolu oturumda yeni ajanlara taban enjeksiyonu yok (E2-08).
- Gönderilen düzeltmenin metni kaydedilmiyor (E2-16).
- İki Batu kararı çelişirse hangi yolun işleyeceği belirsiz (E2-14).

## 7. Açık sorular ve bu incelemenin kanıtlamadıkları

### Açık sorular
1. Ortamın Stop hook'u, dönüşünü bekleyen bir dosya için her dalgada commit ister mi? Yoksa T5'teki olay zamanlamaya bağlı tekil bir durum muydu? Bir dalgada GUNLUK ile commit zamanları karşılaştırılarak ölçülebilir.
2. Limit dolduğunda `send_later` ile kurulan nabız ateşlenirse ne olur: tur hatayla mı biter, yoksa mesaj limit sonrasına mı bekletilir? E2-06'nın ağırlığı buna bağlı.
3. Alt ajan sıkıştırması bir hook'la görülebilir mi? Yani PreCompact alt ajan bağlamında çalışıyor mu?
4. `add_repo` oturum ortasında settings katmanını düşürür mü, yoksa yalnız çok repolu açılan oturumu mu etkiler? (CD-13.)
5. Rol dosyası değişikliği aynı oturumda bir sonraki çağrıya yansır mı? (E2-13'ün önerdiği CD.)
6. Batu arayüzde mevcut dalı seçebiliyor mu (taslağın §14.2 soru 9'u)? E2-07'nin hangi çözüm yolunu alacağını bu belirler.

### Bu incelemenin kanıtlamadıkları
- Bu, aynı modelden ve taslağın gerekçesini görerek yapılmış bir karşı-okumadır (taslağın ölçeğiyle B1). Bulgular düzenin çalışmayacağını göstermez; belirtilen koşullarda hangi adımın dayanaksız kaldığını gösterir.
- Hiçbir senaryo canlı koşulmadı. Kırılmaların hepsi kart metni, git geçmişi ve ortam dosyası üzerinden yapılmış çıkarımdır. Doğrudan gözlem olanlar yalnız E2-03'ün olay kısmı ile E2-07'nin main gözlemidir.
- R11 matrisinin 101 kenarından 49'u sınandı. Kalan 52 kenar ve açmadığım kartlar (ör. MK-4.5, M7.7, S18.3'ün skill metni) başka bulgular üretebilir.
- Hook betiklerinin gövdesi yazılı değil ve okunmadı. E2-03, E2-08 ve E2-11'deki hook davranışı kart metnindeki tarife dayanıyor.
- Önerilerin bedeli (token, Batu'nun dakikası) ölçülmedi. E2-02 ve E2-10'un önerileri K-002'nin uygulanışına dokunduğu için Batu'nun kararıdır.
