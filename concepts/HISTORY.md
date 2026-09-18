# Concepts — Geçmiş ve Sadeleştirme Kaydı

**Tarih:** 2026-09-18. Bu kayıt yeni araştırma veya terim kabulü değildir. Güncel iş [STATE](STATE.md)'tedir.

## Branch temizliği kapanışı — 2026-09-18

**TAMAMLANDI.** Kullanıcı dokuz eski concepts branch'ini GitHub'dan sildiğini bildirdi. Ardından repository'nin branch listesi doğrudan yeniden okundu: 11 ref kaldı; main ve başka çalışmalara ait on branch. Aşağıdaki tarihsel tabloda yer alan dokuz concepts branch adı artık listede yok. Diğer on branch'in adları ve uç commit'leri önceki kayıtla aynı. Açık PR listesi de boş döndü. Gözlem sırasında main `c6bc9b17fd999fe296bab9a5ba7cd778b9a72b3f` idi; bu, altı dosyalı sadeleştirmeyi yayımlayan commit'tir.

Bu kontrol branch adlarının kaldırıldığını doğrular; silme işlemini assistant yapmadı. Eski uçların main geçmişinde bulunduğu silme öncesinde ayrıca kontrol edilmişti. Sabit geçmiş bağlantıları branch adlarına bağlı değildir. Concepts için bekleyen branch temizliği kalmadı; yeni branch veya dosya açılmadı. Diğer araştırmaların içeriklerine/ref'lerine müdahale edilmedi.

Bu kapanışta INDEX, STATE, METHOD, WORKING, SOURCES ve HISTORY'nin güncel gövdeleri okundu. Yalnız bu kayıt ile STATE'in bakım/devam bilgisi güncellenir. Tanımlar, harita ve kaynak notları yeniden yazılmaz; dış kaynak doğrulaması veya somut kullanım sınaması yapılmış sayılmaz.

## Neden sadeleştirildi?

İletişimde ortak anlam kurma amacı, önce tek terim kapanışına, ardından her tur yeni onlu ve yeni sürüm üretimine kaydı. Kullanıcı önce molayı, ardından main ve branch'leri dikkate alan gerçek repository temizliğini istedi. Güncel tercih: az sayıda dosya, tek çalışma taslağı, somut kullanımda ortaya çıkan çakışmaya göre gerekçeli düzeltme. Tek tek kullanıcı onayı kuyruğuna dönülmez.

Özgün kullanıcı ifadeleri ve ilk yöntem gerekçesi [eski PURPOSE](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/PURPOSE.md), son mola kaydı [eski STATE](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/STATE.md) içinde korunur. Bu turdaki kullanıcı talebi: “önce reponu toparla. yönü çizdin, şimdi yöne uygun repo olsun lütfen.”

## Sabit geçmiş ve geri bulma

**Sadeleştirme öncesi main:** `4d849afc2e8b6ef6173957e0923606290912da1e`. **Eski concepts ağacı:** `e20a801e82ac1523994d8d200b306aba44dbd936`.

[Önceki concepts dizininin tamamı](https://github.com/batuhanozgun/agentic-os-search/tree/4d849afc2e8b6ef6173957e0923606290912da1e/concepts) 23 dosyayı özgün gövdeleriyle taşır. Aşağıdaki bağlantılar branch adına veya değişebilir main'e değil bu commit'e bağlıdır. Normal Git geçmişi korunur; eski commit geri yazılmaz, force uygulanmaz. Dolayısıyla eski dosyaları çalışan dizinde veya ikinci bir archive klasöründe çoğaltmak gerekmez.

Araçla geri okumak için repository `batuhanozgun/agentic-os-search`, ref `4d849afc2e8b6ef6173957e0923606290912da1e`, path `concepts/<aşağıdaki eski yol>` kullanılır. Geçmiş dosyadaki göreli bağlantı da aynı ref içinde takip edilir; kaldırılmış yolu bugünkü main'de aramak gerekmez.

## Dosya bazında 23 → 6 geçiş

Yeni düz yapı: INDEX, STATE, METHOD, WORKING, SOURCES, HISTORY. Yirmi eski yol çalışma ağacından çıkarıldı; üç mevcut dosya güncellendi ve üç dosya eklendi. İç alt klasör kalmadı. Eski içerik aşağıdaki sabit kaynaklarda erişilebilirdir.

| Eski yol / özgün kayıt | Yeni konum veya korunma gerekçesi |
|---|---|
| [INDEX.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/INDEX.md) | INDEX: tek giriş ve alan sınırı. |
| [STATE.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/STATE.md) | STATE: yalnız güncel iş/yetki; önceki yayın gövdeleri Git geçmişinde. |
| [PURPOSE.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/PURPOSE.md) | INDEX ve METHOD: amaç, kullanıcı yönü ve sınırlar birleştirildi. |
| [METHOD.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/METHOD.md) | METHOD: güncel iş devri, somut kullanım döngüsü ve kayıt disiplini. |
| [PLAN.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/PLAN.md) | STATE ve METHOD: güncel devam/yayın; bitmiş hazırlık Git geçmişinde. |
| [TERM-INVENTORY.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/TERM-INVENTORY.md) | WORKING açık sorunları + HISTORY: başlangıç listeleri burada sabit geçmişten erişilir; kuyruk kaldırıldı. |
| [research/INDEX.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/INDEX.md) | SOURCES: tek kaynak girişine birleştirildi. |
| [research/agent/BRIEF.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/agent/BRIEF.md) | WORKING ve STATE: eski v0.1 yönlendirmesi kaldırıldı. |
| [research/agent/U01-SOURCE-USES.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/agent/U01-SOURCE-USES.md) | SOURCES üzerinden özgün kayıt; gövde sabit geçmişte. |
| [research/agent/U02-AGENT-MODEL-BOUNDARY.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/agent/U02-AGENT-MODEL-BOUNDARY.md) | SOURCES üzerinden özgün kayıt; gövde sabit geçmişte. |
| [research/U03-CORE-TERMS-BATCH1.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U03-CORE-TERMS-BATCH1.md) | SOURCES üzerinden özgün kayıt; iddialar yeniden doğrulanmış sayılmaz. |
| [research/U04-CORE-TERMS-BATCH2.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U04-CORE-TERMS-BATCH2.md) | SOURCES üzerinden özgün kayıt; ayrıntılı nitelemeler geri bulunabilir. |
| [research/U05-CORE-TERMS-BATCH3.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U05-CORE-TERMS-BATCH3.md) | SOURCES üzerinden özgün kayıt; canlı güvenlik testi sayılmaz. |
| [research/U06-CORE-TERMS-BATCH4.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/research/U06-CORE-TERMS-BATCH4.md) | SOURCES üzerinden özgün kayıt; yerel tanım ile kaynak ayrılır. |
| [synthesis/INDEX.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/INDEX.md) | INDEX + WORKING: tek güncel taslak. |
| [synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md) | Tarihsel Agent A/B gerekçesi; aşağıdaki sabit bağlantı. |
| [synthesis/CORE-TERMS-WORKING-v0.1.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/CORE-TERMS-WORKING-v0.1.md) | Tarihsel 10 maddelik görünüm; aşağıdaki sabit bağlantı. |
| [synthesis/CORE-TERMS-WORKING-v0.2.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/CORE-TERMS-WORKING-v0.2.md) | Tarihsel 20 maddelik görünüm; aşağıdaki sabit bağlantı. |
| [synthesis/CORE-TERMS-WORKING-v0.3.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/CORE-TERMS-WORKING-v0.3.md) | Tarihsel 30 maddelik görünüm; aşağıdaki sabit bağlantı. |
| [synthesis/CORE-TERMS-WORKING-v0.4.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/CORE-TERMS-WORKING-v0.4.md) | WORKING: tanım/harita/ayrım gövdeleri aktarılmış devralınan taslak. |
| [reference/INDEX.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/reference/INDEX.md) | INDEX/METHOD/WORKING: kabul statüsü açık; boş kabul klasörü yok. |
| [checks/SETUP-VERIFICATION.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/checks/SETUP-VERIFICATION.md) | Bitmiş hazırlık kanıtı; aşağıdaki sabit bağlantı. |
| [checks/METHOD-ALIGNMENT-2026-09-18.md](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/checks/METHOD-ALIGNMENT-2026-09-18.md) | Önceki yöntem/yayın kanıtı; aşağıdaki sabit bağlantı. |

WORKING'e aktarılan v0.4 kaynağının blob kimliği `464b9419d6f30bc6195b3b2924b4fb7562bb8112` ve boyutu 9.326 bayttır. Yerel baseline bu kimlikle eşleştirildi. Tanım, harita ve kısa ayrım gövdeleri korunur; eski “oturdu” yorumu, sürüm çoğaltma ve sonraki-onlu yönü güncel talimat olarak taşınmaz. Eski daha ayrıntılı nitelemeler SOURCES üzerinden geri bulunur.

## Branch incelemesi — silme öncesi tarihsel kayıt

Branch listesi 20 ref gösterdi: main, dokuz concepts branch'i ve diğer çalışmalara ait on branch. Dokuz concepts branch'i için ayrı ayrı `base=main`, `head=branch` karşılaştırması yapıldı. Taban her çağrıda yukarıdaki main commit'i kaldı. Hepsinde `status=behind`, `ahead_by=0`, değişen dosya listesi boş ve merge-base ilgili branch ucu çıktı. Böylece bu uçların main geçmişinde bulunduğu doğrulandı. Açık PR listesi boş döndü.

| Eski concepts branch'i | Kontrol edilen uç | Main'e göre önde / geride commit |
|---|---|---|
| `setup/concepts-reference-20260918` | `d4c5368e30dd5997b15b28bedc4337ac9d5d03f4` | 0 / 155 |
| `maintenance/concepts-connected-inquiry-20260918` | `70ab7a108ce925cd962c75af931175e6f4d717b4` | 0 / 60 |
| `maintenance/concepts-pause-orientation-20260918` | `e9f7169802dac5d798140451d99c57d7d36ac76d` | 0 / 1 |
| `research/concepts-agent-u01-20260918` | `75179c8fd73411a0be8c5ac2b379ec47197c5afb` | 0 / 76 |
| `research/concepts-agent-boundaries-20260918` | `2442ab22cf4e1ea873917ccc85a84bed063aa2e4` | 0 / 50 |
| `research/concepts-core-terms-batch1-20260918` | `625b60f76990060bda84b0738eaf772ad7d6f89a` | 0 / 39 |
| `research/concepts-core-terms-batch2-20260918` | `7e452b0c9d8f81f1069fbe4bbaf8938f6e7346ab` | 0 / 24 |
| `research/concepts-core-terms-batch3-20260918` | `168c2939396633eaa2ca7d05a56c421625754638` | 0 / 14 |
| `research/concepts-core-terms-batch4-20260918` | `9e74c91930f057d694761e99ea7083216f7e6831` | 0 / 4 |

**Silme öncesi sonuç:** Bu branch'lerde main'e alınmayı bekleyen concepts commit'i yoktu. Güncel çalışma alanı main'dir; eski branch'lerden devam edilmez.

**Önceki turdaki erişim sınırı — artık açık iş değil:** Uzak branch ref'leri assistant tarafından silinemedi. Kullanılan GitHub bağlantısının keşfedilen işlemleri dosya silmeye izin veriyor, branch/ref silme işlemi sunmuyordu. Ek bağlantı araması kullanılabilir ayrı bir GitHub silme yolu sağlamadı. Yerel git'in GitHub'a erişimi de DNS hatasıyla sonuçlandı. Branch'ler yeniden adlandırılmadı veya sahte bir kapanış commit'iyle değiştirilmedi. Bu düzenleme için yeni branch açılmadı.

Silme öncesi koşul, uçların tabloda yazan kimliklerde kalması ve yeni açık PR/çalışma eklenmemesiydi. Kullanıcının sonraki silme işlemi yukarıdaki kapanış bölümünde doğrulanır; bu tablo artık yapılacaklar listesi değildir. ECC, Foundation ve Hermes branch'leri temizliğin kapsamında değildir; içeriklerine veya ref'lerine yazılmadı.

## İnceleme ve kontrol kapsamı

Önceki turda concepts altındaki 23 dosya tam okunmuştu. Bu tur güncel ağacın blob kimlikleri o okumayla eşleştirildi; değişen STATE tam yeniden okundu. AGENT güncel main'den alındı; kontrol ağacı önceki tam okumayla aynı kaldı. Kaynak araştırması yeniden yapılmadı.

Beklenen yayın farkı yalnız concepts altıdır. Bilinen dış girişler (kök README, research INDEX, studies INDEX/katalog giriş paragrafı/PACKAGE-CONTRACT ve explorations INDEX) INDEX/STATE/METHOD yollarına başvurur; bu yollar korunur. GitHub metin araması sonuç vermedi; bu, bütün repository'de başka bağlantı olmadığına kanıt sayılmadı. Yeni altı dosyanın iç bağlantıları ayrıca kontrol edilir; bütün Foundation/studies külliyatı üzerinde tam metin link taraması iddiası yoktur.

Yayın; hazırlanan concepts alt ağacının mevcut kök ağaçtaki tek yerini değiştirir. Eski main parent alınır. Aday diff'i ve kök ağaç karşılaştırılır; sonra main force kullanılmadan ilerletilir. Eşzamanlı main ilerlemesi varsa bu işlem onu ezmek için kullanılmaz. Yayın sonrasında gerçek main ağacı ve giriş içeriği geri okunur.

Kontroller içerik aktarımı, kapsam, geçmiş erişimi ve yön tutarlılığı içindir. Bağımsız iletişim deneyi, dış kaynak doğrulaması, bütün tanımların doğruluğu veya branch silme kanıtı değildir. Gerçek yayın commit'i bu dosyanın Git geçmişinden bulunur; gelecekteki commit kimliği önceden yazılmaz.

## Yayın öncesi gerçekleştirilen yerel kontroller

Altı dosyalı düz yapı ve WORKING'deki 40 numaralı madde + Task alt kullanımı kontrol edildi. Devralınan tanım/harita/ayrım gövdesi, Git blob kimliği eşleşmiş v0.4 baseline'ıyla birebir karşılaştırıldı. Yeni dosyaların yerel bağlantıları ve sabit eski-path hedefleri kayıtlı dosya listesine göre kontrol edildi; dış web sayfalarının erişilebilirliği tekrar sınanmadı. Kasıtlı tanım değişikliği ve kaldırılmış yerel yola bağlantı içeren iki olumsuz örnek kontrol tarafından reddedildi. Bu örnekler yayımlanan içeriğe yazılmadı.