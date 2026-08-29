# os-architect — okuma defteri

Repo: `batuhanozgun/os-architect`  
Rol: tarihsel karar/araştırma + çalışma-disiplini + KEEL geliştirme bağlamı  
Okuma stratejisi: indeks → yüksek bilgi değerli tema → kaynak gövdesi → gerektiğinde git arşivi

## Neden önemli

Bu repo yalnız KEEL kaynak kodunun çevresi değildir. Mevcut giriş dosyaları, uzun ömürlü çalışma alanının nasıl tutulduğu, araştırmanın nasıl yapıldığı, kararların ve ürün arızalarının nasıl kaydedildiği ve KEEL'in hangi gerekçelerle evrildiği hakkında yoğun kanıt taşıyor.

Bununla birlikte repo kendi çalışma düzeninin öz-anlatısını da içerir. Bu öz-anlatı SOUL için otomatik doğru model kabul edilmeyecek; tarihsel arıza, ölçüm, mekanik uygulama ve karşı-okuma ile ayrıştırılacaktır.

## Okuma kaydı

| Kaynak | SHA | Tür | Neden | Maddi bulgu / işaretçi |
|---|---|---|---|---|
| kök içerik ağacı | — | index | giriş yüzeyini bulmak | `CLAUDE.md`, `PANO.md`, `NEREDE_NE_VAR.md`, `bilgi/`, `kurallar/`, `tools/`, git'te yaşayan arşivler var |
| `CLAUDE.md` | `2eb682f0` | full | çalışma alanının amaç ve davranış çapası | Explicit iş KEEL'i geliştirmek/bitirmek; ortamın sürdürülebilirliği, kanıt, bağımsız roller, kök neden, drift ve mekanik kapılar yük taşıyor |
| `PANO.md` | `28a9be2a` | full | canlı durumun ne olduğunu görmek | KEEL v0.2 yayın ve kabul/otonomi işleri hâlâ aktif; repo tarihsel arşiv değil, yaşayan geliştirme alanı |
| `NEREDE_NE_VAR.md` | `049d8926` | full | bilgi mimarisini anlamak | tek ev, indeks, canlı/arşiv ayrımı, geri getirme komutları; 87 dosyalık eski araştırma arşivi ve 32 dosyalık KEEL geliştirme kaydı git'te tutuluyor |
| `bilgi/INDEKS.md` | `19b78442` | full | kalıcı bilgi katmanını anlamak | iki ana damar: `calisma-duzeni/` ve `keel/`; durum + çıkış satırıyla bilgi ömrü mekanikleştiriliyor |
| `bilgi/keel/INDEKS.md` | `881c2be4` | full | KEEL bilgi kümelerini haritalamak | kuruluş, proje yönetimi, otonomi, koruma/doğrulama, dış-göz ve araştırma seansları ayrılmış |
| `bilgi/calisma-duzeni/INDEKS.md` | `1f5cef29` | full | meta-yöntem kaynaklarını haritalamak | eski alanın çöküşü, sürdürülebilirlik, araştırma, hasım turu, deney ve dış-göz için ayrı canonical notlar var |
| `bilgi/calisma-duzeni/eski-alanin-cokusu.md` | `5fd38faa` | full | bugünkü çalışma mimarisinin kök failure mode'larını bulmak | ölçülen çöküş: aşırı büyük dosyalar, tavansız ham araştırma, güvenilmeyen arama yüzünden kopya/drift, farklı ömürlü içeriğin aynı dosyada karışması; yapı düzeltilse bile davranış değişmezse hastalık tekrarlıyor |
| `bilgi/calisma-duzeni/sonsuza-kadar-kullanilabilirlik.md` | `4750e45d` | full | uzun ömür hedefinin kapsamını anlamak | üç ayak: veri/kütüphane disiplini + danışmanın çalışma disiplini + ürün geliştirme disiplini; üç ev: ortam + danışman + KEEL. Yalnız statik hijyen yetmemiş; sistem kimin neyi ne zaman güncelleyeceğini ve hareketi de taşımalı |
| `bilgi/calisma-duzeni/arastirma-yontemi.md` | `a6601f3f` | full | araştırma sürecinin kendi failure mode'larını anlamak | T1-T5 kaynak tasnifi; aracın sentezi dış kanıt değil; echo/self-citation denetimi; kritik iddiayı birincilden teyit; ölçüm-önce-tasarım; okuma sözleşmesi; çürütme koşusu |
| `bilgi/calisma-duzeni/hasim-turu-yontemi.md` | `751fafea` | full | adversarial review'un gerçekten ne zaman güven ürettiğini anlamak | çok göz aynı hatayı çoğaltabilir; okuyan ve koşan göz farklı sınıf bulur; yalancı-yeşil avı, eksik merceği yeniden koşma, sentez ajanından kaçınma ve tasarım/uygulama turlarını ayırma gerekli |
| `bilgi/calisma-duzeni/dis-goz-yontemi.md` | `fcc54218` | full | dış doğrulamanın yararı ve sınırlarını anlamak | dış rapor fikir kaynağıdır; repo/makine üzerinde tekrar doğrulanır. Soğuk denetim yeni gerçek bulgular üretebilir fakat statik bakış, teslim bağlamı ve yanlış teşhis riski taşır; taze hakemlik ve eşit-katman kıyası önemli |
| `bilgi/keel/kurulus-ve-sertlestirme.md` | `81493b09` | full | KEEL mekanizmalarının doğuş biçimini anlamak | ilk kit bilinçli minimal; mekanik korkulukların önemli bölümü gerçek kurulum koşularından türetilmiş. İlk gerçek koşular 9 bulgu üretmiş; kuruluşun en kırılgan anında deterministic guard olmadığı da açıkça kaydedilmiş |
| `bilgi/keel/genesis-v2-kanit-zinciri.md` | `8de3d1d7` | full | v2'nin gerekçe ve kabul kanıtını ayırmak | 206 birleşik ders envanteri; v2 öncesi GENESIS'te büyük boşluk; kasıtlı bozma ve davranış sondaları var. Ancak sondalar tek-model/tek-koşu; bazı hükümler öz-beyan ve "tam araştırma mı, damıtılmış model mi" tercihi çürütülmüş değil |
| `bilgi/keel/urun-ariza-kokenleri.md` | `d293234d` | full | tekrar eden ürün arızalarının köklerini bulmak | ana kök: bir hatta öğrenilen ders kardeş hatta taşınmıyor. Ölçülemeyen olguyu ölçülmüş sanma, ilan edilen kapsam/ölçü ile fiili mekanizma farkı ve hiçbir bilgi üretmeyen yeşil kapılar kasıtlı bozmayla bulunmuş |
| `bilgi/keel/defo-cercevesi.md` | `6cacdf34` | full | davranış problem modelinin kanıt statüsünü görmek | KEEL güvenlik sınırı değil; tehdit modeli savruk/onay-arayışlı ajan. 49 mekanizma envanterinde mekanik kapılar güçlü, salt öğüt zayıf; tarihsel olarak doğrulama mekanizmaları davranış anti-defolarından daha güçlü. Asıl kayıp çoğu kez kural değil yakalama-anı makinesi |
| `bilgi/keel/dis-dogrulama.md` | `6c89e66a` | full | dış yakınsama iddiasının gücünü sınamak | dış okumalar bazı bağımsız repo/bağlam yakınsamaları ve yeni teyitli bulgular üretmiş; ancak model bağımsızlığı açıkça yok. Aynı model kopyaları tek kanıt sayılıyor; yakınsama zincirinin dördüncü halkası iki kayıtta çelişkili |

## Geçiş 1 — çalışma düzeni ve araştırma yöntemi: TAMAMLANDI

Üç failure seviyesi ayrıldı:

1. **Depo/temsil failure'ı:** şişme, kopya, arama güvensizliği, ömür karışması, açılamayan canonical dosya.
2. **Çalışma-döngüsü failure'ı:** hareket, sorumluluk ve güncelleme yaşam döngüsü taşınmıyorsa doğru dosya yapısı bile yalnız depo olur.
3. **Epistemik süreç failure'ı:** çok kaynak/reviewer görünümü bağımsız kanıt sanılabilir; echo/self-citation, ortak kaynak, öz-onaylama, yalancı-yeşil test ve dış raporun yanlış teşhisi sahte güven üretir.

## Geçiş 2 — KEEL problem/kanıt modeli: TAMAMLANDI

Şimdilik dört katman ayrılıyor:

1. **Gözlenen arıza / saha olayı:** gerçek kurulum ve ürün koşularında çıkan somut defolar.
2. **Ölçüm / tatbikat:** envanter sayıları, kasıtlı bozma, soğuk koşu, test ve davranış sondaları.
3. **Tasarım hükmü:** gözlemden türetilen mekanizma veya tercih; hepsi ölçümle zorunlu hale gelmiş değil.
4. **Dış yakınsama:** başka repo/araç/bağlamlarda benzer problemler ve çözümler; model bağımsızlığı sınırlı, dolayısıyla kanıt gücü ayrıca kalibre edilmeli.

Önemli sonuç değil, çalışma hipotezi: SOUL için KEEL'den aktarılabilir olan şey muhtemelen dosya/ritüel isimleri değil; **failure → ölçüm → mekanizma → falsification → yaşam döngüsü** zincirinin kendisi olabilir. Bunun genellenebilirliği C ve D geçişlerinde sınanacak.

## Öncelikli geçiş 3 — önceki araştırmanın kendisi

Sıradaki giriş kapıları:

1. `bilgi/keel/arastirma-seansi-2026-08-kunye.md`
2. ardından yalnız künyenin işaret ettiği araştırma dosyaları
3. `bilgi/keel/disgoz-seansi-2026-08-kunye.md`
4. ardından gerekli dış-göz kayıtları

Künye okunmadan alt dosyalara toplu girilmez. Önce araştırma sorusu, kapsamı ve yöntem anlaşılır; sonra sonuç dosyaları okunur.

## Arşiv politikası

`NEREDE_NE_VAR.md` git'te yaşayan önemli arşivleri açıkça listeliyor. Canlı notların kaynak veya iddia zinciri arşive dayanıyorsa ilgili commit/path doğrudan okunacak. "Arşiv var" bilgisi, içeriği görülmüş sayılmayacak.

Özellikle gelecekte gerekebilecek iki arşiv:

- eski `Araştırmalar/` — 87 dosya / yaklaşık 1.2 MB,
- KEEL geliştirme kayıtları — iki turda 32 dosya / yaklaşık 622 KB.

Bunlara ancak canlı indeks/not kaynak zinciri veya açık soru işaret ettiğinde girilecek; baştan toplu okunmayacak.

## Açık sorular

- KEEL'in problem modeli ne kadar yazılım-projesi bağlamına özgü, ne kadarı genel agentic çalışma problemi?
- DEFO modelinin kök itki iddiası hangi ölçüm düzeyinde destekleniyor; hangi kısmı tasarım hipotezi?
- Dış araştırma seansları mevcut KEEL tezlerini gerçekten challenge etmiş mi, yoksa mevcut çerçeveyi zenginleştirmiş mi?
- Dış yakınsama zincirindeki kayıt çelişkisi epistemik hikâyeyi ne ölçüde etkiliyor?
- SOUL'un `development/` işletim sistemi fikrinin doğrudan tarihsel öncülleri hangi olay ve karar zincirinde görünüyor?
