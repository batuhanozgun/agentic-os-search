# Concepts — Güncel çalışma durumu

2026-09-20 · **B6-T17-C5b tamamlandı; sıradaki iş B6-T17-C5c / ECC U12-A**.

Bu dosya global amaç, yetki ve current/next work yüzeyidir. Ayrıntılı ECC okuma hesabı [READING](studies/ecc/READING.md), kullanım kayıtları [TERMS](studies/ecc/TERMS.md) içindedir. Kaynak araştırmanın kendi STATE'i Concepts'in sonraki işini belirlemez.

## 1. Amaç ve güncel aşama

**B6-SERIAL-EXTRACTION-ACTIVE / ECC-C1–C4-DURABLE-COMPLETE / ECC-C5a-U10-DURABLE-COMPLETE / ECC-C5b-U11-A–E-DURABLE-COMPLETE / ECC-C5-PARTIAL / ECC-PACKAGE-PARTIAL / METHOD-v0.3-WORKING / B7-B8-NOT-STARTED.**

Önce research/studies araştırmalarını kendi bağlamlarında tam okuyarak kullanımları ve ilişkileri çıkarmak; bütün ilgili çıkarımlar ve kapsam/delta kontrolü tamamlandıktan sonra ayrı ortak değerlendirme yapmak. Genel sözlük araştırması, yeni ürün testi, Foundation doğrusu veya SOUL/Development OS mimarisi bu ilk aşamanın yerine geçmez.

Giriş: AGENT ve gereken protokoller → [INDEX](INDEX.md)'in STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE tam okuma yolu → etkin paketin READING/TERMS → gereken kaynak derinliği. Aynı konuşmada tam ve değişmemiş içerik mekanik tekrar edilmez; gerekli gerçek içerik görünür değilse canonical kaynaktan geri kazanılır. Tarihsel reset/pilot/current-next ifadeleri yeni çalışma talimatı değildir.

## 2. Program ve paket durumu

| İş | Durum |
|---|---|
| Pilotlar, B2/B4 ve B5-SCOPE-S1 | Tamamlandı; yöntem v0.3-working korunur |
| CMH, Superpowers, AI Knowledge Strategies | Concepts durable-complete; korunur |
| Multi-Agent Patterns, Anthropic AI-Native SDLC, gstack | Concepts durable-complete; korunur |
| Hermes Concepts | H1–H5 durable-complete / package-complete; korunur |
| Hermes source-study | ACTIVE PARTIAL; Q60 NOT RESEARCHED; Concepts bunu araştırmaz |
| ECC Concepts C1–C4 | U01–U09 durable-complete; korunur |
| ECC C5a | U10-A/U10-B transfer complete; korunur |
| ECC C5b / U11-A–D | Native review/E08, scheduled work, remote intake ve backlog aktarımı complete; korunur |
| ECC C5b / U11-E | Template resolution/launch aktarımı bu tur tamamlandı; C5b dilimi kapandı |
| ECC C5c | U12-A/B1/B2/C sırada; ilk exact next U12-A |
| ECC C6 | Paket geneli reconciliation/final closure bekliyor |
| ECC source-study | ACTIVE/PARTIAL; U12-C / plan 0.29'a kadar published; U13-A/Q07d1 NOT STARTED |
| Post-S1 additions | agentmemory, claude-swap, cli-continues, ponytail B7 öncesi kapsam hesabına alınacak |
| B7/B8 | Başlamadı |

C5a/b/c mevcut C5'in yürütme dilimleridir; yeni phase veya kaynak dışlama kararı değildir. **C5b-COMPLETE, U11-A–E kaynak-ailelerinin bağlamlı aktarımıdır; ECC'nin bütün dosyalarının reconciliation'ı veya source-study closure değildir.** C5'in U12 bölümü ve C6 açıktır. Paket/ID sayıları ilerleme yüzdesi değildir; S1 sonrası eklemeler hesaba katılmadan kaynak evreni tamamlandı denmez.

## 3. Bu turun gerçek sonucu — U11-E

Giriş main **eb7754b34953b57b9c1aeb92ef4885993ded7ca2**, U11-D final kapanışıyla compare-identical bulundu. AGENT fresh tam okundu ve aynı aea3dd845e0f0bbcfb34465edb23782e99f95c80 kimliğindeydi. R01–R09'un, mandatory Concepts dosyalarının, current READING/TERMS ve ECC META/STATE/INDEX'in bu konuşmadaki tam değişmemiş canonical içerikleri korundu. Bu yeni-oturum deneyi veya bütün geçmişi tekrar okuma değildir.

**Dört araştırma dosyası tam okundu:** Note23, U11-E-SOURCES, ROUND-U11-E ve PUBLICATION-U11-E. Exact ref/blob/aralık hesabı yerel READING §3'tedir. Araştırmada atfedilen upstream Rust/regex/test kaynakları bu tur yeniden okunmuş veya çalıştırılmış sayılmaz. Source-only inquiry yeni deney/E09 gibi gösterilmedi.

Yeni çıktı: [TERMS-TEMPLATE-LAUNCH.md](studies/ecc/TERMS-TEMPLATE-LAUNCH.md), **ECC-TL01–TL74**. Yetmiş dört adreslenebilir kullanım kaydıdır; bağımsız kavram veya kanıt sayısı değildir. N23 §1–8 ve ledger kapsamı, K/B/Y/T/H rolleriyle kullanım ve ilişki kayıtlarına bağlandı.

Önemli anlam sınırları:
- Template metnindeki cwd/source değişkenleri gerçek launch directory veya authenticated origin değildir.
- Explicit default agent ile agent/profile alanlarını vermemek farklı profile-selection yollarına girebilir. Global default hazırlığı ve step başına effective seçim ayrı işlemlerdir.
- Bütün step'lerin önceden çözümlenmesi gerçek pre-effect korumadır; sonraki launch etkilerinin atomikliği değildir.
- Template mevcut Pending/Running/Idle/Stale kayıtlarını kapasiteden düşer. Bu kontrol scheduler'ın batch limit'inden güçlüdür, fakat multi-caller reservation değildir.
- Ordered admission, predecessor process completion ve accepted predecessor output ayrı olaylardır. Common anchor/handoff ilişkisi dependency zinciri değildir.
- Sonraki worktree step'i hata verdiğinde önceki step kalabilir; retry yeni çözümleme/creation yapar, başarısız step checkpoint'inden devam etmez.
- Seçilip saklanan profile alanı, host tarafından uygulanmış kısıt değildir; U12-A bunun ayrı kaynak/consumer kapsamıdır.

**Extractor düzeltmeleri:** İlk ilişki özetinde profile selection tek pre-loop faz gibi görünüyordu; global hazırlık/step içi seçim ayrıldı. TL38 miktar ile TL74 ret işlemi; TL50 process completion ile TL73 accepted output ayrı adreslendi. Ledger'daki dependency-sync warning TL72 eklendi. İlk sürüm, dayanak ve etkilenen kayıtların kontrolü TERMS §10'da korunur. Önceki kullanım dosyaları veya source-study değiştirilmedi.

Olumlu resolver/profile/cycle/capacity kontrolleri, Pending queue retention ve individual cleanup girişimi korundu. Koşullu interpolation/profile/partial-failure örnekleri canlı incident veya privilege escalation sayılmadı. Q04e4b ve önceki güçlü doğrulama soruları açık kalır. C5c/U12-A gövdesi bu tur okunmadı.

## 4. Exact next — C5c / U12-A

**research/studies/ecc/notes/24-EXECUTION-PROFILES-AND-HARNESS-CONSUMERS.md** → evidence/U12-A-SOURCES.md → ROUND-U12-A.md → PUBLICATION-U12-A.md; bağlı evidence gerçek kapsamıyla devralınır.

Amaç mevcut araştırmadaki execution profile, harness seçimi, command argv/environment/text projection, native flags/custom runner ve gerçek consumer kullanımlarını çıkarmaktır. Bir profilin varlığını, bir güvenlik talimatının metne yazılmasını veya bir flag'in üretilmesini uygulanmış host güvencesi sayma. Yeni harness/model/test çalıştırmak veya ECC source-study'yi sürdürmek bu yetkinin parçası değildir. Exact Note24 yolu önceki tam source INDEX'ten bilinir; yolu bilmek gövde okuması değildir.

Sonra U12-B1/B2 OpenCode ve U12-C Python. C5c bitince C6, READING'nin üç tam tarihsel manifesti ve current kaydı, bütün ECC TERMS, kalan history/inventory/evidence ve source delta üzerinden paket-geneli coverage/role/ID kontrolünü yapar. C6 yalnız current özetle kapanmaz. ECC sonrası paket SCOPE sırasına göre work-management-project-control'dür. B7 tamamlanmadan B8 ortak referans başlamaz. U10 ve U11-A–E sırf yeni tur diye yeniden yapılmaz.

## 5. İki risk ve yetki

Batu okuma anındaki anlam seçimlerini denetleyemediğinden önemli dayanak, yorum, belirsizlik ve değişiklik görünür olmalıdır. Ortak sözcükler ortak anlamı garanti etmez; kaynak kullanımı, araştırmacı yorumu, extractor açıklaması ve kullanıcı onayı teknik doğruluk yerine geçmez. Kullanıcı teknik oracle değildir. Bu turun somut karşılığı profil hazırlığı/seçimi, kapasite miktarı/ret, admission/completion/accepted output ve relation-summary düzeltmesidir.

Kaynakta tanımlanmayan anlam dış genel bilgiyle doldurulmaz; açık kaynak ayrımı da belirsizlik bahanesiyle atlanmaz. Q04e4b ve önceki güçlü runtime/authority/acceptance soruları çözülmüş veya otomatik yeni Concepts deney borcu sayılmaz. E06 NOT VERIFIED/EXCLUDED; iki E05 geçmişi ve E04/E07/E08/E09 kendi kapsamlarında korunur.

Yazma yetkisi yalnız ilgili Concepts kullanım dosyası, yerel READING/TERMS ve global STATE bakımındandır. Agent-control, Foundation, source studies, CATALOG, diğer Concepts paketleri, explorations ve publications değiştirilemez. Yeni endpoint, dış request, provider/model, installation, test/fixture, DB/runtime, release veya upstream mutation bu tur yapılmadı.

## 6. Korunmuş tarih ve yayın kontrolü

U11-C/U11-D ayrıntılı global kayıt ve önceki checkpoint bağlantıları [eb7754b STATE](https://github.com/batuhanozgun/agentic-os-search/blob/eb7754b34953b57b9c1aeb92ef4885993ded7ca2/concepts/STATE.md) içinde tam korunur; blob **c402a9cf29d4a7be70d1b081bc1bc2724551c96d**. Daha eski ayrıntı için [f0d9ae3 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/f0d9ae31062459cf7b2cd982eaf484cbdfc336e8/concepts/STATE.md), blob **d8f8c4c3af9094a278f24db9e4feeec26eeaa759**, ve [753a4c6 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/STATE.md), blob **0a9d147c5c8a206964ea99e5e199d76e211b0a98**, korunur. Eski current-next ifadeleri kendi tarihlerine aittir; eski TERMS ve düzeltme izleri yerinde kalır.

Global STATE okuma günlüğünün ikinci kopyası değildir. Yerel READING de önceki U11-C/D manifestini eb7754b tam sürümüne bağladı; C1–C4 ve C5a/U11-A/B için mevcut değişmez bağlar korundu. Kapsam veya tarih düşürülmedi; C6 bu tam dosyaları devralır.

U11-E gerçek checkpoints:
- Yeni TERMS: **a7fbf6a67dfba609c6651c619c2346b6bd067f99**, ilk blob **d6d4aa22a118c5b688a68f247bd6931b5538fac2**; tam içerik readback yapıldı.
- Kaynak/ilişki düzeltmesi: **a3453a63396d8dc8976aac139154970118c3efda**, blob **2315c72fe4b067a7a14826965b116795684fe2ba**; görülen diff hunks ve final tail ayrıca okundu. Kontrolün kesilen görünüm sınırı READING §5'te açık.
- Yerel READING: **fc32fe9dded766d9336904bf18710eb38f805350**, blob **08a3ea459fb34170d0ee356620b22f0f739526c9**.
- TERMS router: **a5136cb0ec2df1f6f88d863cfe20aa3083a1ca1a**, blob **5689233bd7969511749d017bf60fa34f0a31e2ef**.

Final current-ref/diff ve güncellenmiş girişlerin readback'i bu STATE yazımından sonra yapılır. Bu chronological uyarı ayrı next-work üretmez; dosya kendi gelecekteki hash'ini uydurmaz. Otomatik tüm-repo ID/link suite'i, bağımsız aktör incelemesi veya local full-byte/hash-match iddiası yoktur. Aynı-assistant source-to-record/readback kontrolü bilimsel ya da ürün düzeyi bağımsız doğrulama değildir.
