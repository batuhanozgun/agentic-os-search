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

## Geçiş 1 — çalışma düzeni ve araştırma yöntemi: TAMAMLANDI

İlk iki kök-neden kaydı problemi iki seviyede ayırıyor:

1. **Depo/temsil failure'ı:** şişme, kopya, arama güvensizliği, ömür karışması, açılamayan canonical dosya.
2. **Çalışma-döngüsü failure'ı:** doğru dosya yapısı kurulsa bile hareket, sorumluluk ve güncelleme yaşam döngüsü tanımlı değilse alan yalnız depo oluyor; tezgâh olmuyor.

Metodoloji dosyaları üçüncü bir seviye ekliyor:

3. **Epistemik süreç failure'ı:** çok kaynak veya çok reviewer görünümü bağımsız kanıt sanılabilir; echo/self-citation, ortak kaynak, öz-onaylama, yalancı-yeşil test ve dış raporun yanlış teşhisi güveni sahte biçimde yükseltebilir.

Bu yüzden SOUL için şimdilik yalnız bir hipotez taşınıyor: development OS, bilgi saklamanın yanında **çalışmanın ve doğrulamanın yaşam döngüsünü** de taşımalı olabilir. Bu henüz gereksinim veya mimari hüküm değildir.

## Öncelikli geçiş 2 — KEEL'in problem/kanıt modeli

Sıradaki:

1. `bilgi/keel/kurulus-ve-sertlestirme.md`
2. `bilgi/keel/genesis-v2-kanit-zinciri.md`
3. `bilgi/keel/urun-ariza-kokenleri.md`
4. `bilgi/keel/defo-cercevesi.md`
5. `bilgi/keel/dis-dogrulama.md`

Amaç: KEEL'in bugünkü mekanizmalarının neyi çözmek için doğduğunu ve hangi kanıta dayandığını ayırmak. Özellikle ürünün kendi öz-anlatısını, ölçüm/saha kanıtı ve dış doğrulama ile ayrı tutmak.

## Öncelikli geçiş 3 — önceki araştırmanın kendisi

Giriş kapıları:

- `bilgi/keel/arastirma-seansi-2026-08-kunye.md`
- `bilgi/keel/disgoz-seansi-2026-08-kunye.md`

Künye okunmadan alt dosyalara toplu girilmez. Önce araştırma sorusu, kapsamı ve yöntem anlaşılır; sonra sonuç dosyaları okunur.

## Arşiv politikası

`NEREDE_NE_VAR.md` git'te yaşayan önemli arşivleri açıkça listeliyor. Canlı notların kaynak veya iddia zinciri arşive dayanıyorsa ilgili commit/path doğrudan okunacak. "Arşiv var" bilgisi, içeriği görülmüş sayılmayacak.

Özellikle gelecekte gerekebilecek iki arşiv:

- eski `Araştırmalar/` — 87 dosya / yaklaşık 1.2 MB,
- KEEL geliştirme kayıtları — iki turda 32 dosya / yaklaşık 622 KB.

Bunlara ancak canlı indeks/not kaynak zinciri veya açık soru işaret ettiğinde girilecek; baştan toplu okunmayacak.

## Açık sorular

- Eski çalışma alanının ölçülen failure mode'larından hangileri doğrudan LLM/agent özelliği, hangileri sıradan bilgi mimarisi problemi?
- KEEL'in kuruluş mekanizmaları hangi somut arıza/ölçüm zincirinden doğdu?
- KEEL'in defo modeli deneysel kanıt, saha gözlemi ve tasarım varsayımı olarak nasıl ayrılıyor?
- Dış doğrulamalar gerçekten bağımsız mı; hangi ortak varsayımları taşıyor?
- SOUL'un `development/` işletim sistemi fikrinin doğrudan tarihsel öncülleri burada nerede?
