# EXP-007 — STATE

**Güncelleme:** 27 Eylül 2026.  
**Aşama:** P0 — çalışma düzeni (metodoloji). P1–P6 başlamadı.  
**Şu anki adım:** P0.6, revizyon. Üç eleştiri tamam (5 kritik, 26 önemli, 14 küçük bulgu). Revizyon ajanı çalışıyor: [briefs/REVIZYON](phases/P0-calisma-duzeni/briefs/REVIZYON.md) → `METHOD-v1.md` ve `reviews/DEGISIKLIK-KAYDI.md`. Sonra ana oturum kilit bölümleri kendisi okur ve Batu'ya kısa sunum yapar.
**Sonraki adımlar:** P0.4 METHOD v1 taslağı → P0.5 eleştiri turu → P0.6 revizyon ve Batu'ya kısa sunum. Bu adımlar P0 içindedir, Batu'yu beklemeden yürür. Tanımları: [P0 README](phases/P0-calisma-duzeni/README.md).  
**Batu'dan beklenen:** Şu an yok. Taslak sunulunca: taslağa itirazları, A-01, A-02, A-04 ve A-07. Ayrıntı: [DECISIONS](DECISIONS.md).

**Dal:** EXP-007 yalnız `claude/hopeful-pascal-7bekcd` dalında yaşar ve main'e birleştirilmez (K-009).

## Nerede kaldık
- Batu, EXP-006'daki işi Claude'a devretmek istiyor. Amacı, işin alt ajanlarla ve "devam" beklemeden uzun soluklu yürümesi (K-001).
- Claude'un EXP-006 anlayışı kabul edildi (K-006).
- Claude'un ilk çalışma düzeni önerisi ([A003](sources/conversation/A003.md)) yaklaşım olarak doğru, yapı olarak küçük bulundu (K-007).
- Şimdi yapılan: A003'te söylenen her şeyin "nasıl"ını, en iyi uygulamalara dayanarak ve standart seviyede kuran metodolojiyi (METHOD v1) hazırlamak.
- Batu'nun gerekçesi [U004](sources/conversation/U004.md)'teki araba benzetmesinde: söz geniş, çıktı dar olmamalı; bir alanda "yeterli" görünen seçim diğer alanları yetersizleştirebilir.

- **Batu ile iletişim dersi (U010–U011):** Uzun süren P0 çalışmasında Batu bir an DevOS'un yapıldığını sandı. Bundan sonra her durum mesajı haritadaki yeri söyler: "P0: tasarım ekibinin çalışma düzeni; DevOS tasarımı P1'de başlar." Batu yön değişikliği istemedi (U011).

## Bu aşamanın ölçütü (K-007'den)
METHOD v1 şunları "nasıl" düzeyinde kapsamalı:
- Bağlam yönetimi, bellek yönetimi, kalıcı alt ajan rolleri ve en iyi uygulamalara dayalı bir yöntem.
- A003'teki her vaat için somut bir mekanizma. Vaatler: düşünme sırası, görev tanımı, repodan yararlanma, Foundation ve studies kullanımı, plan yönetimi ve revizyonu, kalite, iletişim, süreklilik, öğrenme.
- Her alt sistemde standart seviye. Ertelenen her şey, bütünsel etkisiyle birlikte gerekçelendirilmeli.
- Alt sistemler arası etkileşim.

## Çalışan alt ajanlar

| İş | Çıktı dosyası | Görev tanımı |
|---|---|---|
| Revizyon (P0.6) | `phases/P0-calisma-duzeni/METHOD-v1.md` ve `phases/P0-calisma-duzeni/reviews/DEGISIKLIK-KAYDI.md` | [briefs/REVIZYON](phases/P0-calisma-duzeni/briefs/REVIZYON.md) |

**Tamamlanan eleştiriler:** [E1](phases/P0-calisma-duzeni/reviews/E1-soz-cikti-ve-standart.md) (0 kritik · 7 önemli · 6 küçük) · [E2](phases/P0-calisma-duzeni/reviews/E2-butunsel-etkilesim.md) (2 · 10 · 4) · [E3](phases/P0-calisma-duzeni/reviews/E3-batu-ilkeleri-ve-uygulanabilirlik.md) (3 · 9 · 4).

**Tamamlanan küme taslakları (dondurulmuş):** [T1](phases/P0-calisma-duzeni/drafts/T1-bilgi-tasima.md) · [T2](phases/P0-calisma-duzeni/drafts/T2-aktorler-ve-guvenlik.md) · [T3](phases/P0-calisma-duzeni/drafts/T3-isin-akisi-ve-harita.md) · [T4](phases/P0-calisma-duzeni/drafts/T4-yon-yetki-ve-denetimler.md) · [T5](phases/P0-calisma-duzeni/drafts/T5-dayaniklilik-ve-evrim.md).

- **Ortak bölümler:** [ORTAK](phases/P0-calisma-duzeni/briefs/ORTAK.md), [ORTAK-SENTEZ](phases/P0-calisma-duzeni/briefs/ORTAK-SENTEZ.md) ve [T-ORTAK](phases/P0-calisma-duzeni/briefs/T-ORTAK.md).
- **Yazma kuralı:** Alt ajanlar yalnız kendi çıktı dosyasını yazar ve dosyayı tek seferde oluşturur. Kayıt ana oturumdadır.
- **Oturum kesilirse:** Yarım kalan ajan işi kaybolur. Yeni oturum, eksik çıktıyı aynı görev tanımıyla yeniden başlatır (aşağıdaki "Yeni oturum ne yapar" tablosu).

**Sonraki turların görev tanımları hazır** (`phases/P0-calisma-duzeni/briefs/`):
- [ENTEGRASYON](phases/P0-calisma-duzeni/briefs/ENTEGRASYON.md): T1–T5 → `METHOD-v1-TASLAK.md` (P0.4, ikinci adım);
- [E-ORTAK](phases/P0-calisma-duzeni/briefs/E-ORTAK.md) ile [E1](phases/P0-calisma-duzeni/briefs/E1.md), [E2](phases/P0-calisma-duzeni/briefs/E2.md), [E3](phases/P0-calisma-duzeni/briefs/E3.md): üç eleştiri → `reviews/` (P0.5);
- [REVIZYON](phases/P0-calisma-duzeni/briefs/REVIZYON.md): eleştirilerin işlenmesi → `METHOD-v1.md` ve `reviews/DEGISIKLIK-KAYDI.md` (P0.6).

## EXP-006 ile ilişki (K-010)
- **Bağlantı yok.** ChatGPT, EXP-006'da ayrı ve bağımsız çalışır. Claude, konuyu (DevOS çalışma düzeninin tasarımı) baştan sona devralmış gibi çalışır. EXP-007 ve dalı Claude'un ana çalışma ortamıdır.
- **Sonuç:** EXP-007'nin haritası, P0'dan P6'ya kadar bütün tasarım hattını kendisi kapsar. EXP-006'nın P1–P6 planı ve ürünleri bağlayıcı değildir. Haritayı METHOD v1 taslağı birlikte getirir (P0.4).
- **Okuma:** EXP-006 yalnız faydalanmak için, isteğe bağlı okunur. Claude oradaki çalışmadan sorumlu değildir ve oraya yazmaz.
  - Bu dal `773cfcd`'den ayrıldığı için çalışma ağacındaki EXP-006 eski sürümdür.
  - Güncel hali: `git fetch origin main` ve `git show origin/main:<yol>`. Son görülen commit `ed2bf6e`; P1-01, P2-01, P3-01 dosyaları ve D019–D020 kararları orada.

## Oturum ve ortam notları
- **Git:**
  - EXP-007 ayrı dalda çalışır ve main'e birleştirilmez (K-009).
  - Dal yalnız EXP-007 klasörüne dokunur; böylece ileride birleştirme çakışmasız olur.
  - PR #34 açık duruyor, birleştirilmedi (A-07).
- **Ortam sınırları:**
  - Bu ortamda alt ajan kendi alt ajanını açamaz (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`).
  - Bağlam %80'de otomatik sıkıştırılır.
  - Ayrıntı: [R01](phases/P0-calisma-duzeni/research/R01-ortam-ve-ozerklik-degerlendirmesi.md).
- **Erişim:**
  - code.claude.com ve anthropic.com açık.
  - Bu oturuma bağlı olmayan github.com repoları ve bazı dış siteler (ör. docs.cline.bot) kabuktan kapalı.
  - İki Loopinance reposu bu oturuma salt okuma için bağlandı ve klonlanmadı. Yeni oturumda gerekirse yeniden bağlanmalı.
- **Maliyet (27 Eylül 10:20'de düzeltildi):**
  - **Eski rakam yanlıştı.** "Yaklaşık 6,5 milyon token" görev bildirimlerindeki `subagent_tokens` alanından toplanmıştı. Bu alan ajanın toplam harcamasını göstermiyor. Örnek: T4 için bildirim 77,9 K diyor; transcript'e göre T4 20,8 M token işledi.
  - **Yeni ölçüm:** [tools/token-kullanimi.py](tools/token-kullanimi.py). Transcript'lerdeki `usage` alanlarını mesaj kimliğine göre tekilleştirip toplar. Sınırları betiğin başında yazılı.
  - **Oturum toplamı (10:20, T1–T3 ve T5 sürerken):** yaklaşık 413 M işlenen token.
    - Bunun yaklaşık 392 M'si önbellekten yeniden okuma, 20 M'si önbelleğe yazma, 0,9 M'si çıktı. Çıktı eksik sayılıyor olabilir.
    - Fiyat ağırlıklı girdi eşdeğeri yaklaşık 69–84 M. Ağırlıklar: önbellekten okuma 0,1×, önbelleğe yazma 1,25×–2×, çıktı 5×. Abonelik limitlerinin bunları nasıl saydığı bilinmiyor.
  - **Dağılım (işlenen):** ana oturum ≈ 53 M · R01 workflow (27 ajan) ≈ 27 M · R02–R06 ≈ 30 M · R07–R11 ≈ 168 M · T1–T5 ≈ 130 M (sürerken).
  - **Eleştiriler (E1–E3):** 70 çağrı, 19,6 M işlenen token; ajan başına 4,7–10 M, tepe bağlam 454–487 K. Okuma disiplini burada işe yaradı.
  - **Oturum toplamı (12:15):** ≈ 476 M işlenen token; girdi eşdeğeri ≈ 83–102 M.
  - **Bütün harita için kaba tahmin (E3-12, doğrulanmadı):** aşama başına 135–500 M işlenen token; P1–P6 için 1,2–2,3 milyar. Revizyon bunu sınayacak.
  - **Birleştirme:** 67 çağrı, 14,9 M işlenen token; tepe bağlam 776 K (sıkıştırma eşiğine yakın; ana oturum not gönderdi, son bölümler yeniden okumasız yazıldı).
  - **T1–T5 turu tamamlandı:** 408 çağrı, 154,6 M işlenen token (145,9 M önbellekten okuma), girdi eşdeğeri 26–33 M. Ajan başına 21–39 M işlenen; tepe bağlam 620–734 K, yani %80 sıkıştırma eşiğine (≈ 800 K) yakın. Beş taslak toplam ≈ 947 KB.
  - **Ana maliyet sürücüsü: büyük bağlam × çok adım.** Ajanlar araştırma notlarını baştan okuyup bağlamı 600–780 bin token'a çıkarıyor, sonra 70–120 adım atıyor. Her adımda bütün bağlam yeniden okunuyor.
  - **Sonuç:** Bu, S7 (bağlam) ve S20 (maliyet) için ölçülmüş bir olaydır. Kalan görev tanımlarına bağlam disiplini eklendi. Bağlam penceresi yaklaşık 1 M; ana oturum 792 K'da sıkıştırıldı (%80).

## Yeni oturum ne yapar
0. EXP-007 main'de yoktur. Batu yeni oturuma dal adını verir: `claude/hopeful-pascal-7bekcd`. Oturum dalı alır: `git fetch origin claude/hopeful-pascal-7bekcd`.
   - Oturum bu dalda çalışabiliyorsa onunla devam eder.
   - Ortam oturuma kendi dalını veriyorsa, o dalı bu dalın üzerine kurar (`git checkout -B <oturum-dalı> origin/claude/hopeful-pascal-7bekcd`) ve yeni dal adını bu STATE'e yazar. Dal birikmesin diye eski dal, Batu'ya haber verilerek silinir.
1. [README](README.md)'deki okuma yolunu izler.
2. Hangi çıktının eksik olduğuna bakar ve sıradaki adımı aynı görev tanımıyla başlatır:
   - `drafts/` altında T1–T5'ten eksik olan varsa → onu yeniden başlatır;
   - beşi tamam, `METHOD-v1-TASLAK.md` yoksa → ENTEGRASYON;
   - taslak var, `reviews/E1–E3` eksikse → eksik eleştiri;
   - üç eleştiri tamam, `METHOD-v1.md` yoksa → REVIZYON;
   - `METHOD-v1.md` varsa → ana oturum kilit bölümleri kendisi okur ve Batu'ya kısa sunumu hazırlar.
3. Batu'ya nerede olduğunu kısaca söyler; P0 içindeki adımlar için Batu'yu beklemez.
