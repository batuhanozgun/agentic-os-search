# Concepts — Güncel çalışma durumu

2026-09-20 · **B6-T17-C5a tamamlandı; sıradaki iş B6-T17-C5b / ECC U11-A**.

Bu dosya global current-purpose/authorization/next-work yüzeyidir. Ayrıntılı ECC okuma durumu [yerel READING](studies/ecc/READING.md), kullanım kayıtları [TERMS](studies/ecc/TERMS.md) içindedir. Source-study STATE'leri Concepts next-work authority değildir.

## 1. Amaç ve güncel aşama

**PILOTS/B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / ECC-C1–C4-DURABLE-COMPLETE / ECC-C5a-U10-DURABLE-COMPLETE / ECC-C5-PARTIAL / ECC-PACKAGE-PARTIAL / METHOD-v0.3-WORKING / B7-B8-NOT-STARTED.**

İlk aşama research/studies araştırmalarını kendi bağlamlarında tam okuyup kullanım/ilişkilerini çıkarmaktır. Bütün ilgili çıkarımlar ve kapsam/delta hesabı bitmeden ortak terim değerlendirmesine geçilmez. Bu iş genel sözlük araştırması, source-study'nin yeni teknik deneyleri, Foundation doğrusu veya SOUL/Development OS mimari kararı değildir.

Yeni oturum girişi değişmedi: AGENT ve tetiklenen protokoller → [INDEX](INDEX.md)'in STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE tam okuma yolu → etkin paketin READING/TERMS → gereken kaynak derinliği. Aynı konuşmada tam ve değişmemiş kaynaklar mekanik tekrar edilmez. Eski reset/pilot hazırlık kayıtları current-next sayılmaz.

## 2. Program ve paketlerin durumu

| İş | Güncel durum |
|---|---|
| CMH, Superpowers, AI Knowledge Strategies | Concepts durable-complete; korunur |
| Multi-Agent Patterns, Anthropic AI-Native SDLC, gstack | Concepts durable-complete; korunur |
| Hermes Agent Concepts | H1–H5 durable-complete / package-complete; korunur |
| Hermes source-study | ACTIVE PARTIAL; Q60 NOT RESEARCHED; Concepts bunu araştırmaz |
| ECC Concepts C1–C4 | U01–U09 durable-complete; korunur |
| ECC Concepts C5a | U10-A/U10-B bağlamlı aktarım tamamlandı ve main'e yazıldı |
| ECC Concepts C5b | U11-A–U11-E sırada; ilk exact next U11-A |
| ECC Concepts C5c | U12-A/B1/B2/C bekliyor |
| ECC Concepts C6 | Package-wide reconciliation/final closure bekliyor |
| ECC source-study | ACTIVE/PARTIAL; U12-C / plan 0.29'a kadar yayımlanmış; U13-A/Q07d1 NOT STARTED |
| S1 sonrası additions | agentmemory, claude-swap, cli-continues, ponytail B7 öncesi scope hesabına alınacak |
| B7/B8 | Başlamadı |

C5a/b/c, mevcut C5'in kaynak-ailelerine göre yürütme dilimleridir. Yeni phase, kaynak dışlama veya sabit tur sayısı kararı değildir. Paket sayıları ilerleme yüzdesi sayılmaz; post-S1 kapsam hâlâ reconcile edilmemiştir.

## 3. Bu turun gerçek sonucu — C5a / U10

Giriş main: **753a4c6696740664d359a293ee8d300a45ade6d8**. ECC source package tree: **b6df4013a0f8275da82d6f27a2cd354201c5c70b**. Araştırma upstream pin'i **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a** olarak korundu.

Tam okunan sekiz research dosyası: Note17, U10-A source ledger, ROUND-U10-A, PUBLICATION-U10-A; Note18, U10-B source ledger, ROUND-U10-B, PUBLICATION-U10-B. Exact path/blob/read-range manifesti yerel READING'dedir. Bu okumalar upstream kod/test/SDK'nin bu tur yeniden okunması veya çalıştırılması değildir.

İki yeni kalıcı çıktı:
- [TERMS-EVALUATION-REGISTRY.md](studies/ecc/TERMS-EVALUATION-REGISTRY.md): **ECC-E01–E50**, 50 kullanım satırı.
- [TERMS-OFFLINE-CAPSULES.md](studies/ecc/TERMS-OFFLINE-CAPSULES.md): **ECC-O01–O69**, 69 kullanım satırı.

Toplam 119 source-local adreslenebilir kullanım satırı vardır; bağımsız kavram/kanıt sayısı değildir. Kaynak notunun bölümüne ve ledger kimliğine atıf, söyleyen/ifade rolü ve açıklamanın sınırı her kayıtta korunur. Kaynak tarafından bölüm-kayıt eşlemesi iki dosyada ayrı bulunur.

Önemli anlam sınırları:
- Rust registry'nin conditional pointer update/transaction kontrolü, önceki session-state writer'ına eşitlenmedi.
- Promotion/rollback burada registry seçimi/geri alma olabilir; runtime rollout ve gerçek yarar ayrı sorulardır.
- Distinct seed labels bağımsız deneme, saved criteria preregistration değildir.
- Health snapshot ile callback aynı assertion'a dayanabilir; integrity/correspondence bağımsız sağlık ölçümü değildir.
- Capsule bütünlüğü, tarihin eksiksizliği veya kayıtlı görevin başarısı değildir.
- Replay yanıtı korur; önceki environment/effect'i kendiliğinden geri kurmaz.
- Receipt generic ok sonucu artifact/signature/gate kontrollerinin hangilerinin gerçekten istendiğiyle sınırlıdır.
- Disabled candidate gate, trusted record-mode tool implementation'ının çalışmadığı anlamına gelmez.

**Somut extractor düzeltmesi:** İlk O03 capsule/journal'ı birleştirdi. Source-side/readback kontrolü sonrasında O03 yalnız capsule, O69 journal olarak ayrıldı. İlk sürüm, gerekçe ve O22/O26/O27/O41/O42 etki kontrolü Node TERMS §8'de kayıtlıdır. Önceki C4 source/use kayıtları veya araştırma bulguları bu nedenle yeniden yazılmadı. R10/R11 için ayrıntılı capsule/static-inspection karşılığı O serisine bağlandı; ortak tanım ilan edilmedi.

## 4. Exact next — C5b / önce U11-A

İlk dosya: **research/studies/ecc/notes/19-NATIVE-REVIEW-CALLER-AND-DECISION-BOUNDARIES.md**.

Ardından U11-A-SOURCES, ROUND-U11-A, PUBLICATION-U11-A ve ilişkili E08 evidence kaydı gerçek source-study kapsamıyla devralınır. E08'in adapted-run statüsü native Workflow/model çalıştırmasıyla karıştırılmaz. Bu tur Note19/E08 içeriği okunmuş veya Concepts'e aktarılmış sayılmaz.

U11-B scheduling, U11-C remote intake, U11-D backlog coordination, U11-E template/launch composition aynı C5b hattında sonraki işlerdir. U12 profiles/OpenCode/Python C5c'dir. Kaynak/sürüm değişiklikleri girişte kontrol edilir; yalnız özet veya önceki verdict yeni kaynak okumasının yerine geçmez. U10-A/B sırf yeni tur diye tekrar yapılmaz.

C5 tamamlandıktan sonra C6; kalan root history/inventory/evidence hesapları, bütün ECC TERMS, kaynak değişimleri ve nihai package coverage kontrolünü yapar. ECC'den sonraki paket work-management-project-control'dür; SCOPE sırası korunur. B7 tamamlanmadan B8 ortak referans başlamaz.

## 5. İki risk ve yetki sınırı

Batu okuma anındaki anlam seçimlerini denetleyemiyor; bu nedenle önemli yorum, dayanak, belirsizlik ve değişiklik denetlenebilir kayıtta görünür olmalıdır. Aynı sözcük ortak anlamı garanti etmez: kaynak kullanımı, eski araştırmacı yorumu, extractor yorumu ve kullanıcı onayı ayrı tutulur; kullanıcı teknik uzman oracle değildir. Bu turdaki somut karşılık capsule/journal düzeltmesi ve aynı promotion/verification sözcüklerinin ayrı mekanizma kapsamlarıdır.

Kaynakta açıklanmayan etiket genel bilgiyle doldurulmaz; kaynakta açık ayrımın atlanması da belirsizlik bahanesiyle kapatılmaz. C5a'nın Q06d1b/Q06d2b gibi daha güçlü doğrulama soruları araştırılmış sayılmaz ve otomatik yeni Concepts deney borcu değildir. E04/E07 ve iki E05 geçmişi korunur, E06 NOT VERIFIED/EXCLUDED kalır. Yeni fixture, upstream test, model/provider, installation, DB/runtime, release veya upstream mutation yapılmadı.

Yazma kapsamı yalnız ilgili Concepts kullanım/READING/TERMS/global STATE dosyalarıdır. Agent-control, Foundation, studies source packages, CATALOG, diğer Concepts paketleri, explorations ve publications bu işin mutation scope'u değildir.

## 6. Korunmuş devam geçmişi ve yayın kanıtı

Önceki uzun Hermes H1–H5/C4 kapanış anlatıları ve bütün commit listeleri [753a4c6 checkpoint'indeki önceki STATE'in tam içeriğinde](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/STATE.md) korunur (blob 0a9d147c5c8a206964ea99e5e199d76e211b0a98). Güncel dosyada yalnız current authority ve gerektiğinde geri dönüş yolu tutulur; tarihsel içeriğin artık current-next olmadığı açıktır. Eski package-local kullanım kayıtları yerinde kalır. ECC C1–C4 ayrıntılı READING kaydının değişmez bağlantısı yeni yerel READING'dedir; C6 bunu tam recover eder.

Gerçek bu-tur checkpoints:
- Rust TERMS: **153114995173de76a95772ed259eb982336bdbc4**.
- Node TERMS ilk yayın: **4f002b274c7542c1861c392282e8fbc90195f464**.
- Capsule/journal düzeltmesi: **3e4005d047b592eea06ed110681b51ccc8cce773**.
- Yerel READING: **be6f1bb3bf4d4719057c7460a96ee15a77f249e6**.
- TERMS router: **4207f22ea393af9d620f79d95fbe00c90f507d70**.

Yeni TERMS metinleri tam source aralıklarıyla geri okundu; Node düzeltmesinin gerçek diff'i ayrıca incelendi. Otomatik bütün-repository ID/link testi veya bağımsız aktör doğrulaması iddiası yoktur. Raw yardımcı indirme başarısızlığı source okuma/yazmayı durdurmadı; GitHub connector çalıştı. Son main/ref/diff ve güncel dosya readback kontrolü bu STATE yayınından sonra yapılır; bu dosya kendi gelecekteki hash'ini veya henüz yapılmamış kontrolü uydurmaz. Kaynak-kayıt/readback kontrolü bilimsel veya ürün düzeyi bağımsız doğrulama değildir.
