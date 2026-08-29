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
| `NEREDE_NE_VAR.md` | `049d8926` | full | bilgi mimarisini anlamak | tek ev, indeks, canlı/aşiv ayrımı, geri getirme komutları; 87 dosyalık eski araştırma arşivi ve 32 dosyalık KEEL geliştirme kaydı git'te tutuluyor |
| `bilgi/INDEKS.md` | `19b78442` | full | kalıcı bilgi katmanını anlamak | iki ana damar: `calisma-duzeni/` ve `keel/`; durum + çıkış satırıyla bilgi ömrü mekanikleştiriliyor |
| `bilgi/keel/INDEKS.md` | `881c2be4` | full | KEEL bilgi kümelerini haritalamak | kuruluş, proje yönetimi, otonomi, koruma/doğrulama, dış-göz ve araştırma seansları ayrılmış |
| `bilgi/calisma-duzeni/INDEKS.md` | `1f5cef29` | full | meta-yöntem kaynaklarını haritalamak | eski alanın çöküşü, sürdürülebilirlik, araştırma, hasım turu, deney ve dış-göz için ayrı canonical notlar var |

## Öncelikli geçiş 1 — çalışma düzeninin kök nedenleri

Sıra:

1. `bilgi/calisma-duzeni/eski-alanin-cokusu.md`
2. `bilgi/calisma-duzeni/sonsuza-kadar-kullanilabilirlik.md`
3. `bilgi/calisma-duzeni/arastirma-yontemi.md`
4. `bilgi/calisma-duzeni/hasim-turu-yontemi.md`
5. `bilgi/calisma-duzeni/dis-goz-yontemi.md`

Amaç: bugün görülen dosya/indeks sistemini tasarım tercihi olarak değil, hangi gerçek failure mode'ların sonucu olduğunu anlamak.

## Öncelikli geçiş 2 — KEEL'in problem/kanıt modeli

1. `bilgi/keel/kurulus-ve-sertlestirme.md`
2. `bilgi/keel/genesis-v2-kanit-zinciri.md`
3. `bilgi/keel/urun-ariza-kokenleri.md`
4. `bilgi/keel/defo-cercevesi.md`
5. `bilgi/keel/dis-dogrulama.md`

Amaç: KEEL'in bugünkü mekanizmalarının neyi çözmek için doğduğunu ve hangi kanıta dayandığını ayırmak.

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

- Eski çalışma alanı tam olarak hangi failure mode'lar yüzünden çöktü?
- "Sonsuza kadar kullanılabilirlik" hedefi hangi gözlemlerden doğdu ve hangi parçaları genellenebilir?
- Araştırma yöntemi echo/cherry-picking/coverage problemlerini nasıl ele alıyor?
- KEEL'in defo modeli deneysel kanıt, saha gözlemi ve tasarım varsayımı olarak nasıl ayrılıyor?
- Dış doğrulamalar gerçekten bağımsız mı; hangi ortak varsayımları taşıyor?
- SOUL'un `development/` işletim sistemi fikrinin doğrudan tarihsel öncülleri burada nerede?
