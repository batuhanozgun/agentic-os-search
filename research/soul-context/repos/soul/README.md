# soul — okuma defteri

Repo: `batuhanozgun/soul`  
Rol: bugünkü explicit intent ve yeniden başlangıç çapası  
Okuma stratejisi: mevcut kaynak → commit doğrulaması → dış repolardan gerekçe rekonstrüksiyonu

## Neden önemli

Bu repo şu an çok küçük; bu yüzden dosya sayısından çok yazdığı açık ayrımlar önem taşıyor. Buradaki ifadeler SOUL'un bugünkü yetkilendirilmiş yönünü tanımlar; fakat bu yönün **neden** seçildiği, hangi geçmiş sorunlardan doğduğu ve araştırma programının hangi sorulara cevap vermesi gerektiği diğer iki repodan çıkarılacaktır.

## Okuma kaydı

| Kaynak | SHA / commit | Tür | Neden | Maddi bulgu / işaretçi |
|---|---|---|---|---|
| kök içerik ağacı | — | index | repo kapsamını doğrulamak | ana dalda yalnız `README.md` var |
| `README.md` | `9dbded30` | full | explicit SOUL amacı | first principles'tan genel amaçlı agentic architecture; intended outcome → controlled, verifiable working system |
| bootstrap commit | `7b2a9a4` | history/full diff | önceki ana-dal içeriği var mı kontrolü | bağlı GitHub görünümünde tek commit; yalnız README oluşturulmuş |

## Explicit çapa

Mevcut README dört yük taşıyan iddia taşıyor:

1. SOUL **first principles** yaklaşımıyla yeniden kuruluyor.
2. Amaç genel amaçlı bir agentic architecture: intended outcome'u kontrollü, doğrulanabilir çalışan sisteme dönüştürmek.
3. `development/` ile `system/` bilinçli olarak ayrılıyor.
4. İlk work package, ürün mimarisinden önce **SOUL Development Operating System**.

Bu maddeler araştırmanın sonucu değildir; araştırmanın açıklaması gereken başlangıç koşullarıdır.

## Kritik bilinmeyenler

- Neden "rebuild from first principles" kararı verildi?
- Önceki yaklaşımlarda hangi failure mode'lar bu yeniden başlangıcı gerekli kıldı?
- Neden development OS ürün mimarisinden önce geliyor?
- "controlled" ve "verifiable" hangi hata sınıflarına cevap veriyor?
- Genel amaçlı olma hedefi KEEL'in yazılım-projesi odağından hangi soyutlama sıçramasını gerektiriyor?
- `development/` ve `system/` ayrımı yalnız organizasyonel mi, yoksa epistemik/denetim bağımsızlığı da mı amaçlıyor?

## Sonraki okuma

Bu repoda şimdilik ek kaynak yok. Yeni commit/dosya gelmedikçe burada kör arama yapılmayacak.

Gerekçe rekonstrüksiyonu önce:

1. `os-architect` çalışma düzeni failure kayıtlarından,
2. `os-architect` KEEL kuruluş/kanıt kayıtlarından,
3. KEEL'in mekanik tasarımından

yapılacak; ardından buradaki explicit çapa ile uyum/çelişki kontrolü yapılacak.
