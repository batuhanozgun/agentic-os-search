# DEVOS-001 — değerlendirme, karşı kanıt ve öğrenme

**Statü:** başlangıç değerlendirmesi; Claude'dan bu kanalda henüz yanıt yok. **Tarih:** 23 Eylül 2026.
Amaç taraflardan birini haklı çıkarmak değil, doğru müdahaleyi ve kanıt sınırını belirlemektir. Güncel iş statüsü WORK'tedir.

## Açılışta elde olan kanıt

Research snapshot `1be22a362df2aa527da09b50a19389d167fcf98e`. Bu konuşmada root/context/preparation girişleri, Foundation STATE/handoff/REUSE, studies catalog ve seçilmiş gstack/Hermes/ECC/work-management girişleri okunmuştur. Önceki turdaki Records INDEX, STATE, ORGANISATION-RETRIEVAL ve COLD-READ-CURRENTNESS-COUNTERCHECK tam okumaları kullanılır; bütün corpus yeniden tam okunmuş sayılmaz. Agent-control dosyaları araştırma kanıtı değildir.

Hedef önce `669556c7...`, sonra `af248bde386259a29c610ec784ca32a523e60637`, bu açılışta `411a5ee38a997ba0ba93b81fea0411a134a50adc` üzerinden görüldü. Son STATE tam, PLAN'ın ilgili aşama ve E12–E20 kesimleri doğrudan okundu. Bütün bilgi notlarının doğruluğu, yerel çalışma ağacı ve canlı Claude runtime bu tur denetlenmedi.

## Sorular / karşı kanıt

| Kimlik | Gözlem veya hipotez | Sınır ve sonraki ayırt edici adım |
|---|---|---|
| Q01 | Çok dosya, bilgiye erişim ve kullanım riskini artırmış olabilir | Dosya sayısı başarısızlık kanıtı değil. `knowledge/README.md` rol, kaynak ve freshness ayrımları taşıyor. Claude'dan adını önceden vermediğimiz bir ihtiyaçta gerçek kaynak→karar yolu istenir |
| Q02 | STATE, KR1'i açık inceleme; PLAN bırakılmış/değiştirilmiş karar gösteriyor | `411a5ee.../STATE.md` ve PLAN KR1 satırı. Dar temsil uyuşmazlığıdır; bütün sistemin başarısızlığı değil. Claude current authority ve düzeltme durumunu açıklamalı |
| Q03 | Önceki review E15/E16'nın E17'den sonra olmasını fazla kesin bir sıralama hatası saydı | Son STATE ve E17, araştırma/başlangıç kapısını tasarımdan önce içeriyor; E15/E16 satırları eski sıra tercihini taşıyor. Gerçek tasarım kararının hangi girdiye bağlı olduğu sorulmalı; tek zorunlu lineer sıra dayatılmamalı |
| Q04 | E13 başlangıç yönünü geri bulabildi | `test/e13-fresh-session/E13-RAPOR.md` ve `knowledge/environment/E5-deneyler.md`: iş yürütmek yasaktı. Sadece yön bulma kanıtıdır. Yeni koşulda doğru iş devamı ayrıca sınanmalı |
| Q05 | E19 bilgi değerlendirmesi yararlı olabilir ama işte doğru zamanda kullanımın tamamını ölçmez | Son E19 satırı kendi sınırını açıkça yazıyor: kayıt/bulma/kullanma, önde olma/tetik değil. Bunu fark etmiyor diye suçlama. Gerçek işte eksik kalan ölçüm yolu sorulmalı; holdout içeriği açığa çıkarılmamalı |
| Q06 | Repo yeniden düzenlenebilir; boş repo aynı sorunu tekrar üretebilir | Research çıkarımıdır, seçilmiş nihai tasarım değil. Yerinde düzenleme ile seçici yeni-repo aktarımının kayıp, erişim, yetki ve geçiş riskleri karşılaştırılır |

## Research'ün geri çektiği aşırı hükümler

Önceki yanıtın “Markdown yapısı çalışma sistemi değildir” ifadesi fazla genişti. Prosedürel ve dosya tabanlı mekanizmalar işe yarayabilir; yeterlik gereken yükümlülük ve gerçek kullanımdan sınanır. Ayrıca Git'teki `.claude/settings.json` tüm runtime değildir: `E5-deneyler.md` geçici, commit edilmemiş hook gözlemleri içerir. Bu sebeple repo ağacında görülmeyenden genel mekanizma yokluğu çıkarılmaz.

Önceki 2.204 dosya/~%81 okuma ve ajan/token sayıları Claude planının raporlarıdır; Research tarafından bütün okuma davranışı bağımsız doğrulanmış değildir. Çok emek veya çok çıktı yeterlik kanıtı yapılmaz. Kullanıcının kaygısı da ters yönde otomatik kanıt sayılmaz.

## Bu denemeye katkı veren araştırma rotaları

- Records: `research/soul-foundations/01_verticals/records-artifacts/INDEX.md` → `synthesis/current/ORGANISATION-RETRIEVAL.md` ve `synthesis/COLD-READ-CURRENTNESS-COUNTERCHECK.md`. Katkı: köken/konu/erişim düzenleri ayrılabilir; current/source/audit yolları ve doğrudan aramada eski kaydın rolü korunur. Eski paket self-review'ü Claude yeterliği değildir.
- Foundation current STATE → `08_foundation-sufficiency-reuse-review/REUSE.md`. Katkı: sorudan kaynağa git; yapısal araştırma kapsamını mühendislik yeterliği veya dört zorunlu bileşen sanma.
- `research/studies/gstack/CORE.md`. Katkı: artefaktın değerini gerçek tüketici ve current standing üzerinden sor. Kayıtlı snapshot öğreticidir; bugünkü ürün davranışı veya benimsenmiş mimari değildir.
- `research/studies/work-management-project-control/10-CLOSURE-EVALUATION.md`. Katkı: iş, attempt, readiness, claim, verification ve integration ayrımını kaybetme; hepsini peşinen ayrı servis kurmak gerekmez.
- Hermes ve ECC package INDEX/META → ilgili özgün note/evidence. Katkı: varlık/listelenme/yükleme/tüketim/kullanım ile kayıt/gerçek etkiyi ayır. Paketler kısmi araştırmadır; current adoption için dış hedef yeniden doğrulanır.

Bunlar kaynakların kopyası veya kapalı feature listesi değil. R-001 sonrası ihtiyaç gerektirirse daha derin veya yeni uzman kaynak seçilir.

## Seçilecek değerlendirmede korunacak koşullar

İlk kanal testi yalnız exact mesaj alımını gösterir. Çalışma düzeni için ayrıca: (a) geçmiş sohbet olmadan doğru güncel yetki ve iş; (b) dosya adı verilmeden ilgili bilginin keşfi ve doğru kullanımı; (c) değişmiş kaynak/karar sonrası eski standing'in kullanılmaması; (d) yarım işte doğru devam/geri dönüş; (e) kullanıcı teknik ipucu vermeden eksik önkoşulun bulunup üst işe dönülmesi gerekir. Bunların kapsamı somut işten belirlenir; hazır ezber sınavı veya bütün DevOS sertifikası değildir.

Ölçütler ilgili koşudan önce sabitlenir; kırık referans ve yanlış/eski kayıt gibi negatif örnekler doğru ret sinyali verebilmeli. Kriter değişirse aynı sonuçla yeni başarı iddiası kurulmaz. Ayrılmış yeni varyantlar kullanılır; mekanik kontroller içerik anlamının doğruluğu gibi sunulmaz. Hedefte dış etki yaratan deneyler mevcut yetki ve güvenli izolasyona bağlıdır.

## Öğrenme kaydı ve kapanış

Henüz tamamlanmış deneme sonucu veya kanıtlanmış iyileşme yoktur. Başlangıç dersi adayı: Research'ün geniş emir listesi, Claude'un gerekçesi ve mevcut işi anlaşılmadan yeni belge üretimini artırabilir; bu nedenle önce diyalog seçildi. Etkisi henüz sınanmadı.

Her maddi döngüde kaynak-bağlı gözlem, rakip açıklama, seçilen müdahale, gerçek sonuç ve kalan belirsizlik buraya eklenir; sadece konuşma özeti biriktirilmez. Kapanışta hangi dersin sonraki denemeye hangi sınırla taşınacağı belirtilir. Başarısızlık, iptal, kanıt yetersizliği ve sonuç vermiş müdahale ayrı kaydedilir.
