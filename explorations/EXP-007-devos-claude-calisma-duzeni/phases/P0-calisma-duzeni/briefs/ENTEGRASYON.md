# ENTEGRASYON — METHOD v1 taslağının birleştirilmesi (P0.4, ikinci adım)

**Önce oku:** `briefs/ORTAK.md`, `briefs/ORTAK-SENTEZ.md`, `briefs/T-ORTAK.md`.

**Sonra tam oku:**
- beş küme taslağı: `drafts/T1-bilgi-tasima.md`, `drafts/T2-aktorler-ve-guvenlik.md`, `drafts/T3-isin-akisi-ve-harita.md`, `drafts/T4-yon-yetki-ve-denetimler.md`, `drafts/T5-dayaniklilik-ve-evrim.md`;
- `DECISIONS.md`;
- `sources/conversation/U003.md`, `U004.md`, `A003.md`;
- R11'in §1, §2, §4.5, §4.6, §5 ve §6 bölümleri.

Gerektiğinde R07–R10'un ilgili bölümlerine in.

**Çıktı dosyası:** `explorations/EXP-007-devos-claude-calisma-duzeni/phases/P0-calisma-duzeni/METHOD-v1-TASLAK.md` (tek seferde yaz).

## Görev
Beş küme taslağını, Claude'un EXP-007'yi baştan sona nasıl yürüteceğini tanımlayan **tek ve tutarlı** bir çalışma düzenine dönüştür. Bu metin Batu'ya sunulacak ve onunla anlaşılacak düzenin taslağıdır.

Kümelerin yazdıklarını yan yana koymak yetmez. Asıl iş şunlardır: çelişkileri çözmek, boşlukları bulmak ve bütünün işlediğini göstermek.

## Yapılacaklar
1. **Çelişkileri çöz.**
   - Kümeler arasındaki her çelişkiyi bul, gerekçeli bir kararla çöz ve karar kaydına yaz.
   - Çözemediğini "açık soru" olarak bırak.
   - Arayüz listelerini eşleştir: her "istiyor" bir "veriyor" ile karşılanmalı. Karşılanmayanı yaz ve kapat.
2. **Rolleri eşleştir.**
   - Diğer kümelerin işlev olarak yazdığı sahiplik ihtiyaçlarını T2'nin rol kataloğuna bağla.
   - Sahipsiz ihtiyaç ya da işi olmayan rol kalmasın.
   - Gerekirse rol ekle ya da birleştir, gerekçesiyle.
3. **Dosya mimarisini tekleştir.** Temel T1'in yapısıdır. Aynı bilgi iki yerde yetkili olmasın.
4. **Standart seviye tablosu çıkar:** 21 alt sistem × bileşen. Her bileşen için:
   - karar: gerekli / gereksiz / bilinmiyor;
   - önlediği hata;
   - kabul testi;
   - mekanizma kartı referansı.
5. **Etkileşimleri kapat.**
   - R11 §5'teki 20 "yeterli görünüp yetersizleştiren" seçimin her biri için, dengeleyicinin METHOD'da nerede olduğunu göster.
   - R11 §4.5'teki birbirini besleyen dört döngü için de aynısını yap.
6. **Çarpışma testlerini yürüt: W1–W10.**
   - Kümelerin katkılarını birleştir ve her senaryoyu baştan sona yürüt.
   - Her adımda hangi mekanizmanın çalıştığını, hangi dosyanın okunup yazıldığını ve kimin işlediğini yaz.
   - Kırılma noktası bulursan yaz ve düzelt.
7. **İzlenebilirlik matrisi kur.** Şu üç kaynağın her maddesini METHOD'daki mekanizma kartlarına bağla:
   - U003'teki her soru;
   - U004'teki her gereksinim;
   - A003'teki her vaat.

   Karşılığı olmayan madde kalırsa açıkça "karşılanmadı" de. Batu'nun eleştirisinin kalıcı cevabı bu matristir: söz geniş, çıktı dar olmamalı.
8. **Ağırlık bütçesini çıkar.** METHOD'un kendi bedelini göster: Batu'nun dikkati, token, dosya sayısı, törenler.
   - Hangi mekanizma hangi ritimde çalışıyor?
   - Hafiflik dengeleyicisi ne? Hız için fren neyse, standart seviye için hafiflik de o.
9. **Batu onayı paketini hazırla.** Kurulması gereken yapılandırma ve kontrol değişikliklerinin tek listesi: CLAUDE.md, `.claude/agents`, skills, hook'lar, settings ve AGENT.md'nin Claude'a uyarlanması. Her biri için:
   - gerekçe;
   - seçenekler;
   - önerilen seçenek;
   - onay verilmezse ne olur.
10. **Pilot planını ve yürürlüğe giriş sırasını yaz.**
    - Pilot planı Batu'nun concepts yöntemine uyar: dosya yazmadan konuşma içi pilot → revizyon → ikinci pilot → revizyon (A-02).
    - METHOD'un hangi parçası hangi pilotta sınanıyor? Başarı ölçütlerini önceden yaz.
    - Yürürlüğe giriş sırası: hangi mekanizma ne zaman devreye giriyor?
11. **Baştan sona haritayı ekle.** T3'teki P0–P6 haritası.
12. **Dosyanın en başına Batu için bir sayfalık özet koy:**
    - ne kuruluyor ve neden;
    - Batu'nun rolü;
    - ondan istenen kararlar.

    Özet kısa, sade ve soyutlamasız olmalı.
13. **Açık soruları, varsayımları, riskleri ve metnin neyi kanıtlamadığını yaz.**

## Ana oturumdan notlar (kümeler dönerken eklendi)

**1. Boyut ve yetki kuralı.**
- Küme taslakları büyük: T4 tek başına 187 KB ve 1.552 satır. Beşi birlikte yaklaşık 1 MB olabilir. METHOD bunları kopyalamaz.
- `METHOD-v1-TASLAK.md` bir **omurgadır**:
  - 0–4 ve 6–14 numaralı bölümler tam metindir;
  - 5. bölümde her alt sistem için bir **kart dizini** tablosu olur. Sütunlar: kart kimliği · ne yaptığı (bir satır) · tetik · sahip rol · zorlama düzeyi · kabul testi · taslaktaki yeri · birleştirme durumu (aynen / değişti / birleşti / çıkarıldı).
- Değişen ya da birleşen her kartın yeni hali METHOD'da yazılır. O noktada METHOD, taslağın önüne geçer.
- Küme taslakları METHOD'un ekleri olur ve **dondurulur**. Bundan sonraki değişiklikler yalnız METHOD'a yazılır.
- Batu özeti bir sayfadır. Omurga okunabilir kalmalı; kaba tavan 1.500 satırdır. Bu bir tavan, kota değil.

**2. Bağlam ve maliyet disiplini (ölçülmüş olay).**
- Bu oturumda alt ajan maliyeti yanlış sayaçla ölçüldü. Ayrıntı: `STATE.md`, "Maliyet". Transcript'e göre:
  - T4 tek başına yaklaşık 20,8 M token işledi; bunun 19 M'si önbellekten yeniden okumaydı;
  - oturum toplamı yaklaşık 413 M işlenen token; fiyat ağırlıklı girdi eşdeğeri 69–84 M.
- Sürücü: büyük bağlam × çok adım.
- Bu olayı S7 ve S20 tasarımına girdi olarak işle. T5'in maliyet kartlarını bu ölçümle karşılaştır. Ağırlık bütçesi (madde 8) gerçek ölçüme dayansın; ölçüm aracı `tools/token-kullanimi.py`.
- **Senin için kural:**
  - Önce ucuz gezin: başlık listesi, grep.
  - Sonra hedefli oku. Her taslakta önce özeti, arayüzleri, W katkılarını, onay listesini ve açık soruları oku; kartlara gerektiği kadar in.
  - Büyük okumaları az sayıda turda, paralel yap. Okuma bittikten sonra gereksiz araç çağrısı yapma.
  - Dosyayı tek seferde yaz.

**3. Kümelerden gelen notlar.**
- **T4, ad çakışması:** "Y" kodları hem yükseltme tetikleri hem R11 seçimleri için kullanılmış. "Z1" de hem yetki zarfı sürümü hem hook adayı için kullanılmış. Yeniden adlandır.
- **T4, en büyük risk:** Frenlerin son halkası Batu'ya ulaşan alarmdır, ama bildirim kanalı bilinmiyor. Ana oturumun gözlemi:
  - ana oturumda `PushNotification` aracı var. Araç açıklamasına göre terminale masaüstü bildirimi gönderir; Remote Control bağlıysa telefona da gider; kullanıcı zaten ekrandaysa göndermez;
  - `SendUserFile` aracının "proactive" durumu var;
  - alt ajanlarda bu araçlar yok (T4, EkA-18).

  Bulutta Batu'nun telefonuna ulaşıp ulaşmadığı bilinmiyor; pilotta sınanır. Alarm yalnız ana oturumdan gönderilebilir; alarm tasarımı buna göre ana oturuma bağlanmalı.
- **T3, harita:** K-002'nin bağlandığı P1–P4'ün numarası ve anlamı korundu. K-002'nin yeni haritaya nasıl uygulanacağı P0.8'de Batu'ya sorulacak; bunu onay paketine (madde 9) koy.
- **T3, en büyük risk:** Oturumlar arası uyandırma denenmedi. Çalışmazsa kendiliğinden geçişler oturum sınırında durur. T4'ün alarm riskiyle aynı kökten geliyor (ana oturum dışında kanal yok); ikisini tek pilot sorusunda birleştir.
- **T3, çıktı sınırı:** T3 metni önce repo dışında parça parça hazırladı, sonra tek dosyada birleştirdi. Senin çıktın da büyükse aynı yolu kullanabilirsin; repoya yine tek seferde yaz.
- Diğer kümelerin notları döndükçe eklenecek.

## Önerilen bölüm yapısı
0. Batu için özet
1. Amaç, kapsam ve ilkeler: Batu'nun ilkeleri (R03) → tasarım ilkeleri
2. Baştan sona harita: P0–P6
3. Sistemin bütünü: 21 alt sistem, altı grup, standart seviye tablosu
4. Kalıcı roller kataloğu: tam sözleşmeler ve ajan dosyası içerikleri
5. Alt sistem tasarımları: mekanizma kartları, gruplara göre
6. Dosya ve klasör mimarisi
7. Ritimler: oturum, iş kalemi, aşama; tipik bir çalışma gününün akışı
8. Etkileşimler ve dengeleyiciler
9. Çarpışma testleri W1–W10
10. İzlenebilirlik matrisi
11. Ağırlık bütçesi ve maliyet
12. Batu onayı paketi
13. Pilot planı ve yürürlüğe giriş sırası
14. Açık sorular, varsayımlar, riskler

**Ek:** Birleştirmede değiştirilen, birleştirilen ya da çıkarılan küme kararlarının gerekçeli listesi.

## Dönüş
Ana oturuma en fazla 250 kelime dön:
- dosya yolu;
- en önemli 5 karar;
- izlenebilirlik matrisinde "karşılanmadı" kalan madde var mı;
- en büyük risk.
