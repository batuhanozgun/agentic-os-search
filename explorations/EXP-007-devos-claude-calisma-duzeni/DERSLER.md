# DERSLER — ana oturumun kendi hatalarından çıkan kurallar

Bu dosya, ana oturumun (Claude) bu çalışmada yaptığı hataları, onlardan çıkan kuralları ve her kuralın nasıl zorlandığını tutar. Batu'nun isteğiyle yazıldı (K-017): "kendini değerlendir, dosyalarını değerlendir, düzelt, ders çıkar, hatandan öğren, öğrendiğini uygulayabileceğin yapıda çalış."

**Temel ilke** (loopinance ve os-architect deneyimi, O4 ve O16): "Metin hatırlatır; mekanizma zorlar." Bir kuralın mekanizması yoksa "zorlama: yok (metin)" diye açıkça yazılır ve bir ölçeni aranır.

**Kurulu hook'lar** (`tools/oturum-disiplini/`; kurulum `kur.sh`; `~/.claude/settings.json`):
- `ajan-standart-kapisi.py`: `PreToolUse(Agent)`;
- `kapsam-kapisi.py`: `PreToolUse(Write|Edit|MultiEdit)`;
- `oturum-hatirlat.sh`: `SessionStart(compact|resume)`.

27 Eylül'de üçü de bilerek tetiklenerek sınandı:
- betik düzeyinde 6 bozma testi geçti;
- canlı oturumda iki kapı gerçekten durdurdu: standart dosyası taşımayan Agent çağrısı ve KAPSAM açıkken MIMARI-KARARLAR yazımı.

Makine geri alınınca hook'lar gider; yeni oturum `kur.sh`'yi çalıştırır.

| # | Ne oldu (kanıt) | Kural | Zorlama | Durum |
|---|---|---|---|---|
| L1 | Alt ajanın kendi hakkındaki beyanını doğrulamadan Batu'ya aktardım: METHOD taslağının "karşılanmadı 0" beyanı; O5'in "ECC'den parça al" hükmü, oysa O5 study'nin 56 notundan 2'sini okumuştu. | Batu'ya aktarılan her alt ajan iddiası ya kaynağından doğrulanır ya da "beyan" diye etiketlenir. Bir not, kapsam bölümü okunmadan kabul edilmez. | Yarı mekanik: KAPSAM kabul kuralı ve `kapsam-kapisi` karar dosyasını kilitler. İddia etiketinin ölçeni yok (metin). | Uygulanıyor |
| L2 | Batu'nun standardını ajanlara aktarmadım. Kısa görev metinleri ve not boyutu sınırı verdim, ajanlar da okumayı ayıkladı (U021). | Her ajan görev metni `devos/okuma/STANDART.md`'yi ilk okuma olarak taşır. | **Hook:** `ajan-standart-kapisi.py`, `STANDART.md` geçmeyen her Agent çağrısını durdurur. Bozuk girdide de kapalı kalır. | Canlı sınandı ✔ |
| L3 | Repoda yazılı olan cevabı okumadan Batu'ya sordum: limit (O-20), sorumluluk (O-01), teknik koordinatörlük (BOOTSTRAP §6). | Batu'ya soru yok (K-014–K-017). Belirsizlik kaynakta aranır. | Metin. Ölçen: Batu'ya giden mesajlarda soru işareti sayımı, turdan sonra kontrol (henüz betik yok). | Uygulanıyor |
| L4 | Bir düzeltmeyi bağımlı dosyalara yaymadım: "6,5 M" rakamı STATE'te düzeldi, E3 görev tanımında kaldı. | Bir sayı ya da karar değişince onu anan bütün dosyalar `grep` ile bulunur ve aynı commit'te düzeltilir. | Metin. DevOS tasarımında "değişince kontrol et" tablosu olarak mekanizmaya dönüşecek. | Uygulanıyor |
| L5 | Bir boşluğu "sonra"ya bırakmaya kalktım: KAPSAM'da O4'ün eksiklerini "sonraki tur" diye yazdım, hemen G7'ye çevirdim. | Tetiksiz erteleme yok. Her boşluk ya bir kapatıcıya ya da dosya açıldıktan sonra yazılmış "konu dışı" gerekçesine bağlanır. | **Hook:** `kapsam-kapisi.py`, KAPSAM'da SÜRÜYOR, BOŞLUK VAR ya da SIRADA satırı varken MIMARI-KARARLAR, DEVOS ve `dokuman/` yazımını durdurur. | Canlı sınandı ✔ |
| L6 | Ölçmeden varsaydım: kullanım yüzdesinin tamamını bu oturuma bağladım (U013). | Sayı iddiası ölçüme dayanır. Varsayım etiketlenir ve doğrulama yolu yazılır. | Metin. | Uygulanıyor |
| L7 | Yaranma ve yanlış atıf: Batu'nun kendi karışıklığını "en önemli düzeltme" diye sundum (U014). | Olgu yazılır; övgü ve atıf süsü yazılmaz. | Metin. DevOS eleştiri kontrol listesine girecek. | Uygulanıyor |
| L8 | Okumadan karar verdim: ECC hakkında iki not okuyup "parça al" dedim; METHOD tasarımını mevcut DevOS belgelerini okumadan kurdum (U015, U020). | KAPSAM kapanmadan yapı kararı verilmez. | **Hook:** `kapsam-kapisi.py` (L5 ile aynı). | Canlı sınandı ✔ |
| L9 | Bağlam sıkıştırıldığında ayrıntıyı kaybetme riski: ana oturum bağlamı yaklaşık 560 K; eşik 800 K. | Sıkıştırmadan ya da sürdürmeden sonra STATE, DERSLER, KAPSAM ve STANDART baştan sona yeniden okunur. | **Hook:** `oturum-hatirlat.sh` (SessionStart compact ve resume) hatırlatmayı ve açık KAPSAM satırlarını bağlama basar. | Betik sınandı; canlı sıkıştırmada gözlenecek |
| L10 | Meta işe kaydım: DevOS'un kendisi yerine, onu tasarlayacak çalışma düzenini büyüttüm (P0 METHOD, 157 kart). | Her iş, DevOS teslimatına bağlı olur (STATE'teki üretim sırası). Meta iş ancak teslimatı hızlandırıyorsa yapılır. | Metin, STATE'te sıra. | Uygulanıyor |
| L11 | Uzun süren ajanın sessizliği takılma sanıldı; bekçi sonradan kuruldu. | Uzun süren her ajan için bir bekçi olur: bitişi ya da 25 dakikalık sessizliği bildiren arka plan betiği. | Uygulama pratiği (Bash arka plan döngüsü). | Uygulanıyor |
| L12 | Bir mesaj yolunu denemeden söz verdim (Architect-3). | Yol önce denenir, sonra söz verilir. | Metin. | Uygulanıyor |
| L13 | Ortam sınırını baştan bilmiyordum: 20 alt ajan sınırı yüzünden F4 başlatılamadı. | Paralel dağıtımdan önce çalışan ajan sayısı kontrol edilir; sınırı aşan iş KAPSAM'da SIRADA olarak kaydedilir. | KAPSAM'daki SIRADA satırı ve `oturum-hatirlat.sh`. | Uygulanıyor |

## Bu derslerin DevOS'a aktarımı
Her ders DevOS tasarımında bir mekanizmaya dönüşür:
- **L1:** alt ajan dönüş zarfında "beyan" ile "doğrulandı" ayrımı; doğrulayıcı rol.
- **L2:** rol dosyası ve görev tanımı şablonu; eksik görev metnini durduran hook.
- **L4:** "değişince kontrol et" tablosu.
- **L5 ve L8:** kapsam ve hazır olma kapıları.
- **L9:** SessionStart ile sıkıştırma sonrası yeniden okuma.
- **L11:** takılma bekçisi.
- **L13:** kapasite farkındalığı.

Bu bölüm, DevOS dokümanının "kendini bilen ve öğrenen yapı" bölümüne girdidir.
