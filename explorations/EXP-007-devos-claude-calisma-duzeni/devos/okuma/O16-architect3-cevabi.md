# O16 — Architect-3'ün os-architect deneyimi cevabı: ana oturumun çıkarımları

**Kaynak:** Batu'nun yapıştırdığı cevabın birebir metni `sources/conversation/U022.md`'dedir. Tek yetkili kaynak orasıdır; bu dosya ondan türetilmiş bir görünümdür. Cevabı yazan Architect-3 de kendisini "taze bir oturum" olarak tanımlıyor. Bilgisi os-architect'in kayıtlarından (231 commit, `bilgi/`, koşu defteri, hafıza dosyaları) ve o gün yaptığı ölçümlerden geliyor. Claude Code gözlemleri 2.1.212 ve 2.1.220 sürümlerine ait; yeniden ölçülmeden güvenilmez.
**Okuyan:** ana oturum, metnin tamamı. O12 (os-architect reposunun okuması) sürüyor; bu dosya O12 ile karşılaştırılacak.

## DevOS için en önemli çıkarımlar

1. **Yanlış yere odaklanma.** Ortam dosya düzenini korudu, ama değer teslim etmedi. Sahibin hükmü olumsuzdu: "ajanlar iyi mi düşünüyor göremiyorum; bu hâliyle kafamdaki KEEL olamaz." 27 denetim yeşildi, ama 26 gündür iş yapılmıyordu: "denetim sağlıklı alanı duran alandan ayıramıyor." DevOS'ta şu ikisi biçim denetimiyle aynı düzeyde ölçülür: teslim edilen değer ve ilerleme (geçen süre, duran iş).
2. **İşe yarayan birinci mekanizma: kasıtlı bozma testi.** `tools/bekci.sh` ve `tools/bozma-testi.sh`: her denetim bilerek bozulur ve kırmızı vermesi beklenir. "Ölü denetimi defalarca yakaladı. Tek şey alacaksan bunu al." DevOS'ta her denetimin bir bozma testi olur. Bu, Batu'nun O-01 madde 6'sıyla örtüşür.
3. **Güvencenin çapası, denetlenenin yazamadığı yerdedir.** Denetim kırmızıyken commit atılamaz. Alt ajanın "okudum" beyanı, ajanın kendi sözünden değil, Claude Code'un oturum dökümünden ölçülür (`tools/okuma-dogrula.sh`). DevOS'ta okuma iddiası transcript'ten doğrulanır. Bu turdaki "yarım okuma" sorununa doğrudan cevaptır.
4. **Satır biçimli iş kuyruğu ve açılışta sıradaki işi basan betik** (`IS_KUYRUGU.md`, `tools/sirada.sh`). "Sıradaki iş danışmanın kafasında" hâlini bitirdi. O9'daki "hazır iş kayıttan türetilir" ilkesiyle birleşir.
5. **Kural ancak eylem anında çağıran bir kapısı varsa yazılır.** Kayıtlı üç vakada yazılı kural eylem anında akla gelmedi. "Kuralın yüklü olması, karar anında çağrılması demek değil." Her kural için bir "ölçeni var mı?" tablosu tutulur.
6. **Bayt tavanları hedefe dönüştü.** Açılış yükü 26.992 / 27.000 oldu; tavan beyanla beş kez yükseltildi. Şişmeyi asıl çözen, "bu içerik nereye gidecek" kuralıydı. DevOS'ta sabit tavan yerine içerik sınıfı denetimi, büyüme hızı alarmı ve mekanik bölme kullanılır.
7. **Denetimin kendisi şişti.** İki denetim betiği toplam 256 KB, koruduğu bilgi ağacı 534 KB. Denetim betiğinin de bütçesi olur ve düzenli olarak "sıfırdan kursak böyle mi kurardık?" sorusuyla gözden geçirilir.
8. **Saklama çözüldü, geri çağırma çözülmedi.** "Bir gün önce yazılmış hüküm ertesi gün ihtiyaç anında çağrılamadı." DevOS'ta bilgi, işe göre çağrılır: iş kaleminin bağlam paketi ilgili hükümleri kendisi taşır.
9. **Tek oturumda yedi işlev olmaz.** Ürün yöneticisi işlevi listede vardı ama hiç yapılmadı; sahip, dosya okumadan dört soruyla dört kusur buldu. Yapan, denetleyen ve işi sıralayan baştan ayrı aktörlerdir.
10. **İş akışı "tamamlandı" dedi, sonuç boştu.** Abonelik kesintisi çürütücü ajanları öldürdü; bulgu diske inmeden kayboldu ve 19 gün sonra sıfırdan yeniden türetildi. Bulgu, çürütmeye gönderilmeden önce diske yazılır. İş akışında boş sonuç kapısı olur.
11. **Çürütme iki aşamalıdır ve arada özetleyen ajan olmaz.** Özetleyen ajan bir turda 30 bulguyu 6'ya indirip sert olanları düşürmüştü.
12. **Süreklilik.**
    - Durumun yalnız dosyada tutulması çalıştı.
    - Bağlam temizliği protokolü çalıştı: temizlemeden önce push, yeşil denetim, güncel kuyruk ve pano.
    - Hafızasız okuyucu sınavında 7 KB'lık özet plan kaldı; dosya adı, yapılacak iş ve bitiş komutu yazan plan geçti.
    - Bağlam dolmasının ilk belirtisi, danışmanın kendi kararını sahibe sormaya başlamasıydı.
13. **Baştan kurulsaydı:**
    - döngüden ve "sahibe teslim edilen değer" tanımından başlanır;
    - önce ince bir uçtan uca dilim koşulur;
    - sahip için tek sayfalık bir güven yüzeyi kurulur: sistemin iyi düşündüğünü sahibin okuyabildiği sayfa;
    - yapan, denetleyen ve sıralayan ayrı aktörler olur;
    - sahip testinden önce uçtan uca tatbikat yapılır: 1202 yeşil test iki yapısal ölümü yakalamadı.

## Claude Code gerçekleri (2.1.212 ve 2.1.220; yeniden ölçülecek)

- `CLAUDE.md` talimatı yükler, ama çağrılmasını garanti etmez.
- SessionStart güvenilir, ama yalnız bağlama basar; durduramaz.
- PreToolUse, izin kipinden bağımsız olarak durdurabilir. Kör noktası: düzenleme ile commit aynı kabuk çağrısındaysa hook değişiklikten önceki hali görür. İkinci çapa git'in kendi hook'u oldu.
- **Ajan tanımının içine yazılan hook'lar hiç ateşlenmedi.**
- Skill'deki `allowed-tools` bir kısıt değil, ön onaydır. Rol bazlı araç sınırı onunla kurulamaz.
- `settings` içindeki `allow`, başsız (headless) alt ajanda işlemez.
- Oturum sonu hook'u 24 koşunun 2'sinde iptal oldu.
- **Alt ajan aracının adı `Agent`.** Eşleştirici yalnız `Task` derse kapı hiç çalışmaz ve bunu kimse fark etmez.
- Otomatik izin kipi sahibe sormadan karar verir; aynı girdide farklı sonuç verebilir.
- Etkileşimli onay sorusunun zaman aşımı yok; cevapsız soru koşuyu askıda bırakır.
- Alt ajanın iç araç çağrıları ana dökümde görünmez.
- İzin pencerelerinde teknik olmayan sahip anlamadan "Allow" dedi; koruma fiilen devre dışı kaldı.
- Koşu süresinin %88–90'ı tek bir alt ajanı beklemekle geçti. Bir donmada hiçbir katman alarm vermedi.
- Hafıza klasörü hiçbir git deposunda değil; repoda tek yönlü bir ayna gerekti.
- Genel katmanda bir eklentinin hook'u ilk kabuk komutunu durdurdu. Açılış bağlamının büyük kısmı, ölçülmeyen bu genel katmandan geliyor.

## Kanıtın yeri (os-architect reposunda; O12 okuyor)
`bilgi/calisma-duzeni/eski-alanin-cokusu.md` · `bilgi/calisma-duzeni/sonsuza-kadar-kullanilabilirlik.md` · `bilgi/calisma-duzeni/roller.md` · `bilgi/keel/harness-gercekleri.md` · `bilgi/keel/urun-ariza-kokenleri.md` · `bilgi/keel/degerlendirme-gunu-defteri.md` · `bilgi/keel/sahip-seansi-2026-08-cerceve-korlugu.md` · `bilgi/keel/sahip-seansi-2026-08-13-kok-neden.md` · `Açık işler/K10-kabul-kosusu.md`
