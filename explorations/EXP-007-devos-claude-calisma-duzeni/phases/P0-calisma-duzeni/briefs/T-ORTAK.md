# P0.4 küme taslakları — ortak bölüm (T1–T5)

**Önce oku:** `briefs/ORTAK.md` ve `briefs/ORTAK-SENTEZ.md`. Sonra bu dosyayı, sonra kendi küme görev tanımını (T1–T5) oku.

## Neden kümelere bölündü
Araştırma notları (R01–R11) toplam ~966 KB; tek bir ajan hepsini tam okuyamaz. Bu yüzden:
1. R11'in 21 alt sistemi beş kümeye bölündü.
2. Her küme kendi alt sistemlerini standart seviyede, mekanizma kartlarıyla tasarlar.
3. Sonra bir birleştirme ajanı beş taslağı tek METHOD taslağında birleştirir ve kümeler arası çelişkileri çözer.

**Küme haritası** (R11 §2.4'teki alt sistem numaralarıyla):

| Küme | Alt sistemler |
|---|---|
| T1 | S7 Bağlam yönetimi · S8 Bellek yönetimi · S9 Kayıt ve bilgi mimarisi · S10 Anlam bütünlüğü |
| T2 | S11 Kalıcı roller · S12 Orkestrasyon ve bütünleştirme · S13 Ajanlar arası arayüzler · S16 Güvenlik ve bütünlük |
| T3 | S3 Metodoloji ve yaşam döngüsü · S4 İhtiyaç ve kapsam keşfi · S5 Plan ve iş yönetimi · S6 Araştırma birikiminden yararlanma · EXP-007'nin baştan sona haritası (P0–P6) |
| T4 | S1 Yönetişim ve yetki · S2 Batu ile iş birliği · S14 Kalite güvencesi ve doğrulama · S15 Muhakeme disiplini ve ajan kusurları · S17 Gözlemlenebilirlik ve ilerleme |
| T5 | S18 Süreklilik ve kurtarma · S19 Ortam, araçlar ve yapılandırma · S20 Maliyet ve kaynak · S21 Öğrenme ve uyarlama |

## Nasıl okursun (hedefli, tam değil)
- **R11:** Mutlaka oku: §1, §2, kendi alt sistemlerinin §3 bölümleri, §4'te kendi alt sistemlerini içeren kenarlar, §5 ve §6. Kanıt kodları (K##) R11 Ek A'dadır.
- **R07–R10:** Kendi konunun bölümlerini ve kontrol listelerini oku. Dosyaların başlık yapısını `grep -n "^#" <dosya>` ile çıkarıp ilgili bölümlere in.
- **R01–R06 ve kaynak konuşmalar:** Gerektiğinde. A003'ün ilgili bölümlerini ve U004'ü mutlaka oku.
- **Birincil kaynak:** Karar taşıyan bir iddiada, notun gösterdiği birincil kaynağa (repo dosyası ya da URL) dön ve kontrol et. Notlar birer görünümdür.
- **Okuma kaydı:** Neyi tam, neyi kısmen okuduğunu dosyanın başına yaz.

## Taslağın yapısı (her küme için aynı)
1. **Özet:** en fazla 15 satır. Bu kümenin en önemli tasarım kararları.
2. **Her alt sistem için:**
   - amaç (bir paragraf);
   - standart seviyedeki bileşenler: R11 §3 temel alınır, R07–R10 ile genişletilir ya da düzeltilir;
   - **karar tablosu:** her bileşen için gerekli / gereksiz / bilinmiyor, önlediği hata, kabul testi, kaynak. R10'un yöntemi uygulanır;
   - **mekanizma kartları:** ORTAK-SENTEZ.md'deki zorunlu biçimle. Somut şablon ya da örnek içerik şart; "bir kayıt tutulur" gibi soyut cümle kabul edilmez.
3. **Arayüzler:** bu kümenin diğer kümelerden ne istediği ve onlara ne verdiği. Kümeler arası uyum bu listeyle sağlanacak.
4. **Çarpışma testlerine katkı:** W1–W10'da bu kümenin mekanizmalarının devreye girdiği adımlar.
5. **Batu onayı gerektirenler:** kontrol ya da yapılandırma değişiklikleri, kapsam kararları (DECISIONS A-01, A-04 ile ilişkisi).
6. **Açık sorular, varsayımlar ve bu taslağın neyi kanıtlamadığı.**

## Kümeler arası kurallar
- **Kalıcı rolleri yalnız T2 tanımlar.** Diğer kümeler rol adı uydurmaz, ihtiyacı işlevle yazar. Örnek: "bellek bakımını yapan bir sahip gerekir: kalıcı rol ya da ana oturum görevi; T2'ye ihtiyaç." Birleştirme ajanı eşleştirir.
- **Dosya ve klasör mimarisinin sahibi T1'dir** (S9). Diğer kümeler dosya ihtiyacını yazar; yolu T1'in yapısına uydurmaya çalışır ama çelişirse bunu açıkça belirtir.
- **Claude Code yapılandırmasının sahibi T5'tir** (S19): CLAUDE.md, `.claude/agents`, skills, hook'lar, settings. T2 rol dosyasının içeriğini, T5 yükleme ve zorlama tarafını yazar.
- **Konumlama:** Repo köküne `.claude/` ya da CLAUDE.md eklemek, bütün oturumları etkileyen bir yapılandırma değişikliğidir ve Batu'nun onayını ister (A-04). K-009'daki "dal yalnız EXP-007 klasörüne dokunur" ifadesi ana oturumun kendi formülasyonudur; Batu'nun sözü "ayrı branch'ta çalış o zaman çakışma olmaz". İki seçeneği karşılaştır:
  - a) Tanımlar önce EXP-007 içinde taslak olarak durur, onaydan sonra kurulur.
  - b) Doğrudan dalda `.claude/` altına kurulur.

## Çıktı
- Kendi taslak dosyanı **tek seferde** yaz: içeriği hazırla, dosyayı bir kerede oluştur.
- Uzunluk serbest; her satır bilgi taşımalı.
- Ana oturuma en fazla 200 kelimelik özet dön.
