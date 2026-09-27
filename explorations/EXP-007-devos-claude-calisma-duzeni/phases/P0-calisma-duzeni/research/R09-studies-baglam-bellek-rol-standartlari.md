# R09 — Studies: bağlam, bellek, kalıcı rol, yaşam döngüsü, gözlemlenebilirlik ve maliyette standart seviye

**Tür:** Alt ajan araştırma notu (model çıktısı). EXP-007, P0.3. **Tarih:** 27 Eylül 2026.  
**Görev tanımı:** `phases/P0-calisma-duzeni/briefs/ORTAK.md` + `briefs/R09.md`.  
**Yazma:** Yalnız bu dosya yazıldı. Başka dosya, git durumu ya da araç durumu değiştirilmedi. Okunan bütün içerik veri olarak ele alındı; studies içindeki talimat biçimli metinler uygulanmadı.  
**Kullanım sınırı:** Bu not kaynakların kendisi değil, onlardan türetilmiş bir görünümdür. Karar taşıyan her iddiada aşağıdaki yol#bölüm üzerinden özgün dosyaya dönülmelidir.

---

## 0. Soru, kaynaklar, okuma kapsamı

### 0.1 Soru

Repodaki aday çalışmalar (Batu'nun deyişiyle "farklı arabalar") şu altı alt sistemde olgun sistemlerin ne yaptığını gösteriyor ve her birinde "standart seviye" nedir?

1. bağlam yönetimi (§1);
2. bellek yönetimi (§2);
3. kalıcı roller: rol tanımları ve rol belleği (§3);
4. yaşam döngüsü ve ritimler: oturum, iş kalemi, aşama (§4);
5. gözlemlenebilirlik ve ilerleme takibi (§5);
6. maliyet ve kaynak yönetimi (§6).

Özellikle istenen dört konu: kalıcı rol anatomisi (§3.1–3.2), bellek katmanları ve yaşam döngüsü (§2.2), bağlamın derlenmesi (§1.2), A003 v0 ile karşılaştırma (§7). Yalnız META'sı okunacak paketler §9'dadır.

### 0.2 Mevcut notlarla ilişki: tekrar edilmeyenler

- **R05** görev tanımını, dönüş şemasını, yaşayan planı, sınırlı düzeltme turlarını, gözden geçirenin ayrı girdisini, tamamlanma katlarını, devir ve devamı, dersin nereye yazılacağını, insan kapılarını ve durma türlerini çıkardı. Bu not onları tekrar etmez; gerektiğinde "R05 satır N" diye atıf yapar. R05'in okumadığı ya da dar okuduğu yerler burada derinleştirildi: CMH-02 (bellek) tamamı, gstack bellek sentezinin §9–§22'si, ECC'nin tamamı (R05 kapsam dışı bırakmıştı), Hermes'in bellek notları ve synthesis/02, superpowers S02/S05, Carbon Layer'ın üç videosu.
- **R06** "rol örnekleri ve uzmanlık sürekliliği"ni (rol = talimat + taşıyıcı + bağlam + araç/etki kapsamı + yeterlik dayanağı) ve "fikirlerde statü etiketleri"ni kurdu. Bu not rol dosyasının somut alanlarını ve rol belleğini ekler.
- **R04** özetlerin kullanım kapsamını, revizyonun üzerine yazma olmadığını, "bulamadım"ın arama yöntemini söylemesi gerektiğini ve kaydedilen talimatın yetki taşımadığını kurdu. Burada tekrar edilmez; bellek mekanizmasına dönüştüğü yerde atıf yapılır.
- **R01** Claude Code'un `.claude/agents` alanlarını, `memory: project` rol belleğini, auto-memory'nin makineye bağlı olduğunu ve %80 sıkıştırmayı belgeledi. Burada yalnız bağlantı kurulur.

### 0.3 Kısaltmalar ve kanıt dili

**Dosya kısaltmaları** (hepsi `research/studies/` altında):

| Kısaltma | Dosya |
|---|---|
| CMH-01 … CMH-04 | `context-memory-harness-engineering/01-CONTEXT-ENGINEERING.md`, `02-AGENT-MEMORY-ENGINEERING.md`, `03-HARNESS-ENGINEERING.md`, `04-CROSS-LAYER-SYNTHESIS.md` |
| AKS-RAG, -KG, -FT, -CAG, -LC | `ai-knowledge-strategies/01-RAG.md`, `02-KNOWLEDGE-GRAPH.md`, `03-FINE-TUNING.md`, `04-CAG.md`, `05-LONG-CONTEXT.md` |
| TCL-H08, H10, H11, H12, H16, H17 | `the-carbon-layer/videos/mQfTdNVCOB0-harness-engineering/notes/08-…`, `10-…`, `11-…`, `12-…`, `16-…`, `17-…` |
| TCL-M-META, -RES, -ASM | `the-carbon-layer/videos/PxuMqeIqCEo-agent-memory/META.md`, `RESEARCH.md`, `SOUL-DEVOS-ASSESSMENT.md` |
| TCL-S-RES, -ASM | `the-carbon-layer/videos/-01_NB4SbBY-agent-sandboxing/RESEARCH.md`, `SOUL-DEVOS-ASSESSMENT.md` |
| GS-CORE, GS-MEM, GS-MA, GS-PLAN, GS-RQS, GS-EVAL, GS-DEP | `gstack/CORE.md`; `gstack/syntheses/` altında `memory-learnings-context-gbrain.md`, `multi-agent-cross-model-coordination.md`, `planning-specification-work-admission.md`, `review-qa-ship-delivery-qualification.md`, `testing-eval-routing-compliance-flake-lifecycle.md`, `deploy-canary-production-retrospective-feedback.md` |
| SP-CORE, SP-S01…S05, SP-U03 | `superpowers/CORE.md`; `superpowers/syntheses/S01-…`–`S05-…`; `superpowers/notes/U03-delegation-review-and-acceptance.md` |
| ECC-CORE, ECC-MC, ECC-N06 … N53 | `ecc/CORE.md`, `ecc/METHOD-CASE.md`, `ecc/notes/06-…`, `07-…`, `08-…`, `09-…`, `32-…`, `39-…`, `40-…`, `53-…` |
| HA-S01…S03, HA-N02 … N30 | `hermes-agent/synthesis/01-…`–`03-…`; `hermes-agent/notes/02-…`, `03-…`, `07-…`, `11-…`, `30-…` |
| PB-01, PB-03 | `anthropic-ai-native-sdlc-playbook/01-PLAYBOOK-RESEARCH.md`, `03-SOUL-DEVELOPMENT-OS-ASSESSMENT.md` |
| MAP-A | `multi-agent-patterns/SOUL-DEVELOPMENT-OS-ASSESSMENT.md` |
| R01 … R06, A003, U004 | EXP-007 içindeki araştırma notları ve konuşma kaynakları. R01'in iddia numaraları alt raporlar arasında tekrarlandığı için R01'e satır numarasıyla atıf yapılır. |

**Çalışmanın kendi kanıt sınıfı** (ilgili study o iddia için ne yaptı):
- **K** — sabitlenmiş kaynağı okudu;
- **K+T** — kaynağı ve birinci taraf testlerini okudu, testleri koşmadı;
- **D** — yerel, sentetik bir deneme koşturdu;
- **L** — tedarikçi belgesi ya da akademik literatür;
- **A** — çalışmanın kendi analitik çıkarımı ya da kurgusal senaryosu.

**Kanıt gücü türü** (ORTAK "Kanıt dili"): *tedarikçi iddiası* (Anthropic/OpenAI belgeleri ve yazıları, ürün README'leri); *topluluk pratiği* (açık kaynak uygulamaların kodu: gstack, superpowers, ECC, Hermes; Carbon Layer'ın eğitim anlatımı); *bağımsız ölçüm* (hakemli akademik kıyaslar: LongMemEval, SWE-agent, Lost in the Middle; bizim ortamımızda yapılmadılar). Hiçbir çalışma bu mekanizmaların canlı ajanlarla etkinliğini ölçmedi.

**Bu notun etiketleri:** *kaynak diyor* (ilgili study dosyası bunu söylüyor; dış hedefin kendisini ben okumadım), *gözledim* (repoda kendim okudum), *çıkarım*, *varsayım*, *bilinmiyor*. Standart seviye kontrol listeleri benim sentezimdir; etiketleri *çıkarım*dır ve her maddenin dayanağı yazılıdır.

**Erişim:** Bütün repo dosyaları 27 Eylül 2026'da okundu. Dış URL'lere gidilmedi; dış kaynaklara studies üzerinden atıf yapılır. Erişilemeyen kaynak yok.

### 0.4 Okuma kapsamı

| Paket | Tam | Kısmi | Okunmadı |
|---|---|---|---|
| Kütüphane girişi | CATALOG, INDEX, PACKAGE-CONTRACT | — | — |
| context-memory-harness-engineering | META, STATE, INDEX, 01, 02, 03, 04 | 00 (başlıklar, anahtar satırlar) | — |
| the-carbon-layer (koleksiyon) | META, STATE, INDEX, syntheses/INDEX | — | METHOD, VIDEO-CATALOG, SOURCE-MAP, MIGRATION dosyaları |
| … PxuMqeIqCEo (bellek videosu) | META, STATE, INDEX, RESEARCH, SOUL-DEVOS-ASSESSMENT, evidence/REVIEW-AND-LIMITS | — | README, METHOD, RESEARCH-PLAN, SOURCE, MEDIA-READING |
| … mQfTdNVCOB0 (harness videosu) | META, STATE, INDEX, notes 08, 10, 11, 12, 16, 17 | — | notes 01–07, 09, 13–15; WHY, BRIDGE, METHOD, PLAN, SOURCE-LEDGER, evidence |
| … -01_NB4SbBY (sandbox videosu) | META, STATE, INDEX, SOUL-DEVOS-ASSESSMENT | RESEARCH (başlıklar, §5 onay yorgunluğu) | SOURCE, METHOD, PLAN, REVIEW |
| ai-knowledge-strategies | META, STATE, INDEX | RAG §14–15, §19; KG §25; FT §19; CAG §15–16, §27–28; LC §25–26; hepsinin başlık listesi | 00; mekanizma dosyalarının diğer bölümleri |
| hermes-agent | META, STATE, INDEX, synthesis 01–03, notes 03, 07, 11, 15, 30 | note 02 (§1–7), note 18 (arama) | synthesis 04, diğer notlar, evidence, inventory |
| gstack | META, INDEX, CORE, memory-learnings sentezi | STATE (ilk kısım); multi-agent (özet, §1, §5–7, §10–15); planning-spec (özet, §1–4, §6–8); review-qa-ship (§2–3, başlıklar); testing-eval (§7, §12–17, §19, §25, başlıklar); deploy-retro (§19–21, başlıklar); inventory/STRUCTURE (§1–2) | diğer 8 sentez, CLOSURE-AUDIT, METHOD, SOURCE-LEDGER, revalidation |
| superpowers | META, CORE, S01, S05 | STATE ve INDEX (ilk kısımlar), S02 (§1–5), S03 (§2–7), notes/U03 (§1–4), notes/U06A (arama) | S04, S06, CLOSURE-AUDIT, METHOD, PLAN, diğer notlar, ledger'lar, evidence |
| ecc | META, STATE, CORE, notes 06, 32 | INDEX (ilk kısım), METHOD-CASE (§1–3, §5–10), notes 07 (§1–6), 08 (§1–5), 09 (§1–4), 39 (§1–2, §4–9), 40 ve 53 (başlıklar, arama) | diğer notlar, ROUND/PUBLICATION dosyaları, QUESTIONS, evidence |
| anthropic-ai-native-sdlc-playbook | STATE | META ve INDEX (ilk kısımlar), 01 (§5–9, §11), 03 (§5, başlıklar) | 00, 02, 04 |
| multi-agent-patterns | META | SOUL-DEVELOPMENT-OS-ASSESSMENT (§7, §12 C7–C10, §13) | CONVERSATION-SYNTHESIS (yalnız başlıklar) |
| Yalnız META (9 paket) | llm-wiki, openviking, ai-memory, agentmemory, agent-memory-providers, context-mode, cli-continues, mattpocock-skills, deepseek-harness | — | bu paketlerde başka dosya yok |
| EXP-007 | ORTAK, R09, U004, U005, A003, README, STATE, DECISIONS, P0 README, conversation/INDEX, R05 | R01 (arama), R02–R03 (başlıklar), R04 (başlıklar, (b)), R06 (başlıklar, §1) | — |

---

## 1. Bağlam yönetimi

### 1.1 Olgun sistemler ne yapıyor

- **CMH (odak konu; literatür + tedarikçi deneyimi).** Bağlam, modelin o çağrıda gördüğü çalışma kümesidir. Amaç en çok bilgiyi yüklemek değil, bütçe altında karar için yararlı sinyali en çoğa çıkarmaktır: "maximize decision-relevant signal" [CMH-01 §4]. Bu, seçim kadar bir dışlama problemidir [§4.1]. Bağlama giren şeyler yedi sınıftır: kontrol talimatı, güncel iş durumu, dış kanıt, bellekten geri çağırma, araç arayüzü, araç sonucu, türetilmiş içerik. Her sınıfın tazelik ve yetki sorunu farklıdır [§5]. Güven sınıfları ayrı tutulur: "trusted control instruction / trusted canonical state / trusted/verified source evidence / untrusted external content / model-generated derived content / user-provided claim/preference" [§16]. — *kaynak diyor* · L + A.
- **CMH, DevOS'a dönük.** Repodaki kademeli okuma yolu güçlü bir örnektir, ama "Repository'de iyi routing olması, runtime'ın onu her seferinde uyguladığını otomatik kanıtlamaz"; bilgi mimarisi ile yüklemenin uygulanması iki ayrı iştir [CMH-01 §19]. — *kaynak diyor* · A.
- **ai-knowledge-strategies.** Güncel durum ve yetki zorunlu bir açılışla, kanıt ise uyarlamalı getirmeyle bağlama girer: "mandatory canonical bootstrap + adaptive evidence retrieval" [AKS-RAG §14.4]. Anlamsal yakınlık yetki değildir: "“çok relevant” ≠ “current authority”". Getirmede güncel/tarihsel, kabul/hipotez, kaynak/sentez, kanonik/türetilmiş, SHA ve yerine konma durumu alanları gerekir [§14.2]. Kararlı içerik yeniden kullanılır, değişken durum taze okunur: "Stable verified context'i cache et; dynamic authoritative state'i fresh recover et" [AKS-CAG §27.5]. Uzun bağlam kademeli okumayı gereksiz kılmaz; en güçlü rolü "router'ın belirlediği bounded authoritative çalışma paketini gerektiğinde bütün halinde değerlendirebilmek"tir [AKS-LC §26.5]. — *kaynak diyor* · L + A.
- **Carbon Layer harness videosu** (topluluk anlatımı; Claude Code ve Codex belgeleriyle karşılaştırılmış). Bir talimat için dört ayrı soru vardır: doğru kaydedildi mi, istemci onu bu dizin/oturum için yükledi mi, ilgili model çağrısında korunup doğru yorumlandı mı, modele güvenilemediğinde etkiyi durduran bir kapı var mı [TCL-H08 §2]. Bir kaynak "listed but unread, readable but omitted, included but obsolete, or accurately presented but misunderstood" olabilir [§3]. Karma yükleme önerilir: "A hybrid can supply non-negotiable constraints and a source map up front while retrieving task-specific details as needed" [§3]. — *kaynak diyor* · A + L.
- **Carbon Layer bellek videosu.** Bağlam kurucu dört iş yapar: "retrieve → rank → resolve → assemble" [TCL-M-RES §4]. HERMES belgesinde oturum başında donmuş bellek görünümü ile sonradan diskte yapılan değişiklik ayrıdır; araç yanıtları canlı durumu gösterebilir [§7, D03]. — *kaynak diyor* · topluluk anlatımı + ürün belgesi.
- **gstack** (topluluk pratiği; K+T). Kalıcı bellek herkese değil, iş rolüne göre verilir: "office-hours → product, goals, user-profile, recent-decisions, salience; plan-eng-review → product, recent-decisions". Planlama dışı beceriler (ship, qa, investigate, retro) bu bloğu hiç almaz ve bu testle korunur: "persistent memory is routed according to work role rather than globally flooding every agent context" [GS-MEM §9]. Her bellek varlığının bayt bütçesi, her becerinin toplam bütçesi ve bellekle ilgili talimat bloklarının kendi bütçesi ayrı test edilir: "runtime digest data budget versus resolver instruction budget" [§10]. Claude'a becerinin küçük bir karar-ağacı iskeleti verilir; bölümler "STOP+Read pointer to an on-demand source" ile gerektiğinde okunur [GS-PLAN §6]. Bağlam bilinçli olarak da saklanır: Autoplan'da Claude alt ajanına önceki inceleme verilmez [GS-MA §1.1, §6]; CSO doğrulayıcısı bulguyu ve yanlış-pozitif kurallarını alır, tarayıcının akıl yürütmesini almaz [§7]. Özetle: "context can be loaded / context can be scoped / context can be withheld / context can be independently recomputed" [§13.1].
- **superpowers** (topluluk pratiği; K + D; sahip kabul etti, kanıt gücü artmadı). Bağlamı koordinatör derler: görev bölümü, bağlayıcı gereksinimler, arayüzler, ilgili önceki kararlar ve rapor yeri. İşçiye bütün plan ve geçmiş verilmez; gözden geçirene aynı brief ve global kısıtlar verilir [SP-S03 §3]. Plan bu derlemeyi kolaylaştırır: "Plans carry a Spec pointer, exact Global Constraints, files and consumes/produces interfaces" [§2]. Ama görev ayıklayıcı "is not a requirements compiler"; globalleri koordinatör eklemek zorundadır [§3]. Bir yöntemin kullanılabilir olması bir zincirdir: "source selected ≠ package assembled ≠ files installed ≠ session activated ≠ relevant content loaded ≠ procedure followed ≠ useful outcome" [SP-CORE §5].
- **ECC** (topluluk pratiği; K). Oturum başında (SessionStart hook'u) seçilmiş "içgüdüler" bağlama eklenir: güven eşiği 0,7, en fazla 6 öğe, proje kapsamına +0,25, teknoloji yığını eşleşmesine +0,2 sıralama katkısı; birleşik bağlamın karakter üst sınırı vardır [ECC-N07 §6]. dev-team yönteminde koordinatör konuyu ve PROJECT-CONTEXT.md'yi "bounded declarative summary"ye indirir, sırları ve talimat benzeri metni ayıklar ve her persona istemine güvenilmeyen-veri uyarısı koyar [ECC-N39 §7]. Pi uyarlamasında önbelleklenmiş kurallar her çalıştırmada yeniden girer, bekleyen hook bağlamı yalnız bir kez tüketilir, açık yeniden yükleme tazelik yoludur [ECC-CORE §3.3].
- **Hermes** (topluluk pratiği; K). Saklanan konuşma ile modele gönderilen istek kopyası aynı nesne değildir. Bellek ön-getirimi her turda kullanıcı bağlamına eklenirken sistem istemi önbellekte kalır. Normal sıkıştırma sınırında önbellek geçersizleşir, bellek diskten yeniden yüklenir ve sistem mesajı yeniden kurulur [HA-S02 §3–4].
- **AI-Native SDLC Playbook** (tedarikçi iddiası; Claude Code belgesi). Üç katman: "always-relevant project context → CLAUDE.md / rules; conditionally relevant procedure → Skill; must-not-be-violated behavior → Hook / setting / sandbox / permission / identity / external gate" [PB-01 §7.3]. CLAUDE.md ve auto-memory "context, not enforced configuration"dır [§7.2]. *Bulut:* CLAUDE.md, kurallar ve beceriler bulut oturumuna repodan gelir; repo `settings.json` hook'ları yalnız tek repolu oturumda geçerlidir [R01 satır 527, 624].
- **multi-agent-patterns** (kavramsal değerlendirme). Hiyerarşide her yönetici aşağıdan gelen bağlamı özetledikçe yük taşıyan ayrıntı kaybolur. Denetim yönü: "source pointers, exact artefact binding, retrieval-on-demand, distinction between authoritative source and summary/view" [MAP-A §13 R8]. — *kaynak diyor* · A.

### 1.2 Bağlamın derlenmesi: kim, hangi kuralla (özellikle istenen 3)

Studies üç tür bağlam derleyicisi gösteriyor (*kaynak diyor*, sınıflama *çıkarım*):

1. **Deterministik kod** (gstack çözücüleri, ECC hook'ları, Hermes çalışma zamanı). Kural koddadır: hangi alt küme, hangi sıra, hangi üst sınır. Testle korunabilir. gstack'te `scripts/brain-cache-spec.ts` varlıkları, TTL'yi, bayt bütçesini ve beceri alt kümelerini tek yerde tanımlar; testler planlama dışı becerilerin bloğu almadığını doğrular [GS-MEM §9–10]. ECC'nin SessionStart seçimi bir eşik/sıralama/üst sınır kuralıdır [ECC-N07 §6]. Hermes'te gönderim kopyasını kod kurar [HA-S02 §3].
2. **LLM koordinatör** (superpowers'ın controller'ı, ECC dev-team koordinatörü; A003'teki ana oturum). Kural, koordinatöre verilen yazılı sözleşmedir: hangi alanlar zorunlu, ne saklanır. Güçlü yanı yargıdır; zayıf yanı seçimin denetlenmesidir: "smaller worker contexts reduce repeated history, but increase the importance of the controller's selection and handoff" [SP-S03 §3].
3. **Platform** (Claude Code). CLAUDE.md ve kurallar her oturumda, becerilerin gövdesi ilgili olunca yüklenir; alt ajan yalnız kendi istemini alır. TCL-H11 §3'ün aktardığı Claude Code belgesine göre fork olmayan alt ajanlar "do not inherit the parent's conversation, read files or previously invoked skills"; yapılandırılmış beceriler önceden yüklenebilir. *Bulut:* R01 satır 56'ya göre alt ajanlar bulutta yereldeki gibi çalışır. — *kaynak diyor* (tedarikçi belgesinin aktarımı).

**Paket içerikleri, sistem sistem:**

| Paket öğesi | gstack | superpowers | ECC | Hermes |
|---|---|---|---|---|
| Sabit rol talimatı | beceri iskeleti + ortak çözücüler (preamble, review, learnings, GBrain…) [GS-PLAN §6] | rol şablonu (implementer, reviewer…) [SP-U03 §2] | agent gövdesi; komut gövdesi [ECC-N39 §2, §4] | sistem istemi + beceri dizini [HA-S02 §3] |
| Göreve özgü kısım | önce inceleme hedefi çözülür (plan-eng-review) [GS-PLAN §3] | görev bölümü + rapor yeri [SP-S03 §3] | PRD/plan dosyası, veri olarak [ECC-N39 §6] | kullanıcı turu |
| Globaller, kısıtlar | önceki tasarım belgesinin keşfi [GS-PLAN §2] | "exact Global Constraints" [SP-S03 §2] | PROJECT-CONTEXT.md özeti [ECC-N39 §7] | — |
| Rol başına bellek | beceri başına bellek varlıkları; uzmanlara alan dersleri [GS-MEM §9; GS-MA §1.2] | yok | içgüdüler; rol ayırt etmez [ECC-N07 §6] | ön-getirilen bellek [HA-S02 §3] |
| Bilinçli saklanan | önceki aşama bulguları; tarayıcının gerekçesi [GS-MA §6, §7] | işçiden bütün plan ve geçmiş; gözden geçirenden koordinatörün önceden biçtiği önem derecesi [SP-S03 §3] | sırlar; talimat benzeri metin [ECC-N39 §7] | eski araç sonuç gövdeleri, yardımcı model özetinde [HA-N02 §2] |
| Bütçe | varlık, beceri ve talimat bütçeleri; testli [GS-MEM §10] | açık bütçe yok; nitel "dar bağlam" | birleşik bağlam karakter sınırı; bağlam doluluk uyarısı [ECC-N07 §6; ECC-N32 §6] | inceleme çatalı: 16 yineleme, 600.000 girdi token [HA-N02 §7] |
| Kademeli yükleme | STOP+Read ile istek üzerine bölüm [GS-PLAN §6] | plan → görev → gereken kaynak [SP-S03 §2–3] | /plan'a verilen `.prd.md` dışındaki Markdown yalnız referans bağlamıdır [ECC-N39 §4] | araç yanıtıyla canlı durum [TCL-M-RES §7] |

**Sonuç (*çıkarım*):** Olgun sistemlerde bağlam paketi şu parçalardan oluşur: sabit rol kısmı, göreve özgü kısım, zorunlu globaller ve arayüzler, rol başına bellek alt kümesi, saklananlar listesi ve bütçe. Bu parçaların en az bir kısmı koddan ya da sabit bir sözleşmeden gelir. A003'te hepsi her görev tanımına tek tek yazılıyordu (§7).

### 1.3 Varyantlar ve ödünleşimler

- **Önden yükleme / tam zamanında / karma.** Önden yükleme küçük, kararlı, birlikte düşünülmesi gereken paket için; tam zamanında getirme büyük ve değişken alan için; karma, pazarlık dışı kısıtları ve kaynak haritasını önden verir [TCL-H08 §3; CMH-01 §6]. Tam zamanında getirmenin bedeli keşif gecikmesi ve yanlış yola sapmadır (Anthropic'in kendi uyarısı, TCL-H08 §3'te aktarılmış).
- **Dar işçi bağlamı / tam geçmiş.** Dar bağlam tekrarı ve çapalanmayı azaltır ama koordinatörün seçimini yük taşıyan yapar [SP-S03 §3]. Tam geçmiş bazı eksiklikleri önler ama "can introduce noise, stale assumptions and inappropriate authority cues" [TCL-H11 §3].
- **Paylaşma / saklama.** gstack Autoplan'da Claude alt ajanı önceki bulguları görmez (çapa kırma), Codex görür (birikmiş bağlamla meydan okuma); iki rol bilinçli olarak farklı bağlam alır [GS-MA §6].
- **Genel enjeksiyon / rol başına yönlendirme.** gstack rol başına verir. ECC oturum başında, görev bilinmeden verir: "startup lacks the new task, so it is not a check of the actual current user request" [ECC-N07 §6].
- **Önbellek / sıkıştırma.** "a stable prefix favors computation reuse, while replacing history changes that prefix" [TCL-H08 §4].
- **Satır içi / devretme.** superpowers'ın kısa yolunda iş ana oturumda kalınca ana bağlam yükü arttı (kullanıcı raporu, transkript yok, doğrulanmadı). Çalışma şu hedefleri ayırır: "fewer planning artifacts, lower human interruption, smaller controller context, lower total cost and better delivered work. Improvement in one is not proof of improvement in all" [SP-S03 §6].

### 1.4 Başarısızlıklar ve karşı örnekler

- **gstack, bayat bellek işaretinin kaybı.** Önbellek katmanı içeriği "stale-fallback" diye işaretler; planlama çözücüsü `2>/dev/null` ile bu işareti atar ve model eski içeriği bayat olduğunu bilmeden alır: "gstack's cache **knows** when brain context is stale, but the current planning preflight **does not reliably tell the agent**" [GS-MEM §12]. Arka planda yenileme bunu düzeltmez: "asynchronous warming is performance/future-freshness optimization, not a substitute for preserving current-turn provenance" [§13]. — *kaynak diyor* · K (kaynak izleyerek bulunmuş olumsuz bulgu).
- **ECC, koşulun kaybı.** İçgüdü satırı yalnız kapsamı, güveni ve eylemin ilk satırını taşır: "It does not carry the instinct ID, trigger, evidence block, source path or the rest of a multiline action." Koşullu bir kural böylece koşulsuza dönüşebilir [ECC-N07 §6]. — *kaynak diyor* · K.
- **Carbon harness, sıkıştırmada kısıt kaybı.** Sıkıştırılmış not "prepare release"ı korur, "do not deploy"u düşürür; konu örtüşmesi bunu yakalamaz, "A constraint-retention check against the source would" [TCL-H08 §4]. — *kaynak diyor* · A (kurgusal vaka).
- **Hermes, ikinci modelin gördüğü farklı kanıt.** Farklı bir yardımcı modele giden inceleme özeti son 24 mesajı, kullanıcı metninde 300, asistan metninde 200 karakteri tutar ve eski araç sonuçlarının gövdesini taşımaz: "İkinci modelle karşılaştırma yalnız 'farklı değerlendirici' değişkenini değiştirmiyor; görülen kanıt da değişebiliyor" [HA-N02 §2]. — *kaynak diyor* · K.
- **ECC, bağlam doluluğunun tazeliği.** Bağlam yüzdesi kendi gözlem zamanını değil ortak bir zaman damgasını taşır; eski bir yüzde taze sayılabilir [ECC-N32 §6]. — *kaynak diyor* · K.
- **Tedarikçi deneyimi, dev talimat dosyası.** "too much guidance → no guidance"; tek parça el kitabı çabuk bayatlar [CMH-03 §8]. — *kaynak diyor* · L (OpenAI'nin iç deneyimi, tedarikçi iddiası).

### 1.5 Standart seviye kontrol listesi — bağlam

Her madde: amaç, yokluğunda ne bozulur (diğer alt sistemler dahil), bedel, gerçekten gereksiz olduğu koşul ve EXP-007'de bu koşulun durumu, dayanak. Hepsi *çıkarım*dır.

**BA-1 — Bağlam parçalarının sınıf ve güven etiketi**
- *Amaç:* Talimat, kanonik durum, doğrulanmış kanıt, güvenilmeyen dış içerik, model üretimi özet ve kullanıcı iddiası aynı metin yüzeyinde karışmasın. CMH buna "epistemic status collapse" der [CMH-01 §15].
- *Yokluğunda:* Başka asistan için yazılmış bir kontrol dosyasındaki cümle yetki kazanır (yetki, güvenlik). Alt ajan özeti kanıt gibi okunur (doğrulama). Eski plan güncel sanılır (yaşam döngüsü).
- *Bedel:* Görev tanımında ve dönüşte bir etiket alanı; düşük.
- *Gerçekten gereksiz:* Bağlama tek kaynaktan, tek güven sınıfında içerik giriyorsa. EXP-007'de geçerli değil: AGENT.md ve `agent/` (başka asistan için), EXP-006 adayları, alt ajan dönüşleri ve Batu'nun sözleri aynı işte birlikte okunuyor.
- *Dayanak:* CMH-01 §15–16; TCL-H08 §2 (I2); ECC-N39 §7; R04 (b)6.

**BA-2 — Zorunlu çekirdek ile istek üzerine getirilenlerin ayrılması**
- *Amaç:* Güncel durum, yetki ve bağlayıcı kısıtlar hiçbir zaman arama ya da hatırlama şansına bırakılmasın; kalan kanıt gerektiğinde gelsin. Ayrım her tüketici için (koordinatör ve her rol) yazılı olsun.
- *Yokluğunda:* Oturum ya da alt ajan eski veya eksik durumdan başlar (süreklilik). Ya da çekirdek şişer ve her çağrıda gereksiz yük taşınır (maliyet, sıkıştırma).
- *Bedel:* Çekirdeği küçük tutma disiplini; hangi dosyanın çekirdekte olduğuna karar.
- *Gerçekten gereksiz:* Yok. Her yeni oturum ve her alt ajan boş bağlamla başlar [R01 satır 56].
- *Dayanak:* AKS-RAG §14.4; AKS-LC §26.3–26.4; TCL-H08 §3; GS-PLAN §6. R05 satır 16 ve R05 "top 8" madde 7 devamdaki okuma sırasını verdi; buradaki ek, ayrımın alt ajanlar dahil her tüketici için tanımlanmasıdır.

**BA-3 — Tazelik sınıfları**
- *Amaç:* Neyin her seferinde taze okunacağı (STATE, açık kararlar, dal ve HEAD, Batu'nun son sözleri) ile neyin yeniden kullanılabileceği (belirli SHA'daki kaynak, kabul edilmiş karar metni) önceden belli olsun.
- *Yokluğunda:* Ya her şey her seferinde yeniden okunur (bağlam dolar, maliyet artar) ya da önceki oturumun özeti güncel durumun yerine geçer (yetki, plan).
- *Bedel:* Dosya ya da kayıt başına bir tazelik etiketi.
- *Gerçekten gereksiz:* Tek oturumda biten iş. EXP-007 çok oturumlu.
- *Dayanak:* AKS-CAG §15–16, §27.4–27.5; GS-MEM §11 ("file exists ≠ valid cache"); GS-RQS §3 (geçerlilik gözden geçirilen nesneye göre hesaplanır).

**BA-4 — Tüketici (rol) başına bağlam paketi sözleşmesi**
- *Amaç:* Her rol için paketin zorunlu parçaları sabit olsun: rol dosyasındaki sabit kısım, görev tanımındaki değişken kısım, zorunlu globaller ve arayüzler, ilgili önceki kararlar, rol başına bellek alt kümesi, bilinçli saklananlar listesi, dönüş yeri.
- *Yokluğunda:* Koordinatör her seferinde rolü yeniden biçer (Batu'nun U004 eleştirisi). İşçi ve gözden geçiren aynı eksik brief'i paylaşır (doğrulama). Bellek her role topluca akar (bağlam kirlenmesi).
- *Bedel:* Rol başına şablon bakımı; koordinatörün paket derleme emeği.
- *Gerçekten gereksiz:* Alt ajan kullanılmayan iş. EXP-007 alt ajanlarla yürüyor.
- *Dayanak:* SP-S03 §2–3; SP-CORE §3; GS-MEM §9; GS-MA §1.2, §6, §7; ECC-N39 §7. R05 satır 1 ve satır 11 brief içeriğini ve gözden geçirenden saklanacakları verdi; buradaki ek, sabit/değişken ayrımı, rol başına bellek alt kümesi ve saklananların pakette açıkça listelenmesidir.

**BA-5 — Bağlam bütçeleri: paket, talimat, koordinatör**
- *Amaç:* Rol paketine bir üst sınır; kalıcı talimat dosyalarının (CLAUDE.md, rol dosyaları, METHOD) kendisine ayrı bir üst sınır; koordinatörün bağlam kullanımının izlenmesi.
- *Yokluğunda:* Talimatlar birikir, "too much guidance → no guidance" olur (bakım). Koordinatör sık sıkıştırılır ve açık kararları kaybeder (süreklilik, plan). Maliyet artar.
- *Bedel:* Satır/karakter sayımı; budama kararları.
- *Gerçekten gereksiz:* Bağlamın hiç dolmadığı kısa iş. EXP-007'de sıkıştırma %80'de tetikleniyor [R01 satır 539] ve alt ajanlar P0.3'e kadar yaklaşık 4,1 milyon token harcadı (EXP-007 STATE, *gözledim*).
- *Dayanak:* GS-MEM §10; PB-01 §7.2 (talimat birikimi riski); CMH-03 §8; ECC-N32 §6.

**BA-6 — Sıkıştırma protokolü**
- *Amaç:* Sıkıştırma kayıplı bir dönüşümdür. Öncesinde kayıt (durum dosyası güncel, açık kararlar yazılı), sonrasında kanonik dosyaların yeniden okunması, arada "yapma" türü kısıtların korunup korunmadığının kontrolü.
- *Yokluğunda:* "do not deploy" türü bir kısıt kaybolur ve yanlış eylem çıkar (yetki). Koordinatör açık soruları unutur (plan). R01'in işaret ettiği "tam okuma kuralı ile otomatik sıkıştırma çatışması" plansız kalır [R01 satır 838].
- *Bedel:* Eşiğe yaklaşırken bir kayıt adımı; yeniden okuma token'ı.
- *Gerçekten gereksiz:* Sıkıştırmanın tetiklenmediği iş. EXP-007'de tetikleniyor.
- *Dayanak:* CMH-01 §11; TCL-H08 §4 (M1); HA-S02 §4 (sıkıştırma sınırında yenileme); R01 satır 539–546. R05 satır 17 özet denetim listesini verdi; buradaki ek, sıkıştırma anına bağlı ritimdir.

**BA-7 — Görünüm sınırlarında niteleyicinin korunması**
- *Amaç:* "bayat", "kısmi", "doğrulanmadı", "yerine konmuş" gibi niteleyiciler içerik bir görünümden ötekine geçerken içerikle birlikte gitsin (bellek → paket; alt ajan dönüşü → STATE → Batu'ya mesaj). Son tüketicinin gördüğü görünüm denetlensin.
- *Yokluğunda:* Bayat bilgi taze yetkiyle karar verir (bellek; GS-MEM §12). Kısmi değerlendirme tam sayılır (gözlemlenebilirlik; GS-EVAL §15). Koşullu ders koşulsuz uygulanır (roller; ECC-N07 §6).
- *Bedel:* Etiket alanları; son görünümü okuma alışkanlığı.
- *Gerçekten gereksiz:* Tek görünümlü sistem. EXP-007'de en az dört görünüm var.
- *Dayanak:* GS-CORE §11 F1 ("payload survives; qualifier disappears"); GS-MEM §12; ECC-N06 §5–6; ECC-N07 §6.

**BA-8 — "Bulunamadı" ile "yok"un ayrılması**
- *Amaç:* R04 (b)5 ilkeyi kurdu. Bağlama ilişkin ek: yük taşıyan yokluk iddiasında doğrudan okuma ya da ikinci bir sorgu yapılır; aramayı yapan rolün (eksik-arayıcı) dönüşünde arama yöntemi ve kapsamı alanı bulunur.
- *Yokluğunda:* Eksik-arayıcı yanlış güven verir; okunmamış kaynak "yok" sayılır.
- *Bedel:* Ek sorgu.
- *Gerçekten gereksiz:* Yokluk iddiası yapılmayan iş. EXP-007'de eksik-arayıcı rolü tam olarak bunu yapar.
- *Dayanak:* AKS-RAG §14.3; TCL-H08 §3 (C2); ECC-N06 §6.

**BA-9 — Bağlam yeterlilik sınaması**
- *Amaç:* Bağlam mimarisinin kâğıtta değil uygulamada çalıştığını görmek. En az iki sınama: rol paketlerinin örnek bir görevle denenmesi; beklenen cevaplar verilmeden, yalnız repodan belirli olguların geri bulunması (soğuk başlangıç).
- *Yokluğunda:* Kötü bir paket şablonu fark edilmeden bütün alt ajanlara yayılır ve hatalar birbirine bağlı olur (roller, doğrulama).
- *Bedel:* Bir alt ajan çağrısı ya da taze bir oturum.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* CMH-01 §17 (negatif kontrol: yük taşıyan kanıt çıkarılınca test kırmızı vermeli) ve §19; ECC-MC §6 ("A future conversation-independent check should recover a small predefined set of facts without being supplied the expected answers"); A003 §6 (soğuk başlangıç testi önerisi).

---

## 2. Bellek yönetimi

### 2.1 Olgun sistemler ne yapıyor

- **CMH (odak konu; akademik literatür + tedarikçi).** Bellek depolama değil, zaman içindeki bir yaşam döngüsüdür: aday oluşturma → yazma → niteleme → birleştirme → güncelleme/yerine koyma/çelişki → saklama/unutma → okuma → bağlama enjeksiyon [CMH-02 §4]. "storage ≠ memory correctness / retrieval ≠ recall correctness / recall ≠ context use / retention ≠ truth" [§3]. Yetki sırası: "fresh authoritative source/state > verified persistent derived memory > unverified/heuristic memory" [§6]. Yazma yolu okuma kadar önemlidir: "kötü yazılmış memory'yi kusursuz retrieve etmek sadece yanlışı daha güvenilir şekilde geri getirir" [§7]. Model üretimi bellek ile dışarıdan gözlenmiş bellek aynı sınıfta tutulmaz [§17]. DevOS için sınıf tablosu: güncel iş/yetki, kabul edilmiş karar, araştırma bulgusu, oturum karalaması, ajan yansıması, araç/ortam tuzağı, kullanıcı tercihi, tarihsel durum; her birinin yetkisi ve ana riski ayrıdır [§22]. Bellekten bağlama geçerken taşınacak alanlar: "memory_id, memory_type, epistemic_status, source_refs, created_at, valid_time / superseded_by, actor/work scope, confidence / verification status" [§23]. Ve: "Bir `MEMORY.md` dosyasının varlığı memory harness değildir" [CMH-03 §14]. — *kaynak diyor* · L (LongMemEval, Generative Agents, Reflexion, MemGPT: bağımsız akademik ölçüm, bizim ortamda değil) + A.
- **Carbon Layer bellek videosu** (topluluk anlatımı + dar birincil kaynak kontrolleri). Dört işlev (çalışma, olay, bilgi, yöntem) aynı işte birlikte gerekir ama "Dört tür, zorunlu dört bileşen değil" [TCL-M-RES §3; TCL-M-ASM §5]. Çelişki: farklı zamanlara ait iki kayıt tarihsel olarak doğru olabilir; aynı zamana ait çelişen kaynaklarda tarihe göre sıralamak yetmez; en yeni yorum yanlış işe ait, yetkisiz ya da eski bir onayın alıntısı olabilir [TCL-M-RES §5]. Kısa hali: "old does not mean false and new does not mean authorized" [TCL-M-META]. Unutmanın dört yolu: zamanla önem düşürme, çelişkide güncellemeyi yazıp öncekini tarih olarak tutma, sıkıştırma, elle bakım; sıkıştırmada sınır: "Özetleme bir iddiayı doğrulanmış olguya veya yetkili kurala yükseltmez" [TCL-M-RES §6]. Asıl soru: "neyi saklayıp bugünkü karara hükmettirmeyelim?" [TCL-M-ASM §4].
- **gstack** (topluluk pratiği; K+T). Bellek tek depo değil, dört kanaldır: (a) açık komutla kaydedilen oturum kontrol noktası; alanları durum, dal, zaman, oturum süresi, değişen dosyalar, iş özeti, verilen kararlar, kalan iş, notlar; yalnız eklenir, üzerine yazılmaz; önce aynı dalın en yeni kaydı geri yüklenir, başka dal kullanılırsa uyuşmazlık gösterilir [GS-MEM §2]; (b) proje kapsamlı ders kayıtları; alanları zaman, beceri, tür, anahtar, içgörü, güven, kaynak türü, dal/commit, etkilenen dosyalar, projeler arası güven bayrağı [§4]; (c) türlendirilmiş planlama belleği; varlık başına kapsam, TTL, bayt bütçesi ve beceri alt kümesi [§9]; (d) güven ve içe aktarma politikası; uç nokta güveni (kişisel/paylaşımlı/belirsiz) ve repo başına okuma-yazma/salt-okuma/yasak [§16–18]. Özeti: "gstack does not assign one universal standing to remembered information. It differentiates memory by provenance, scope, age, trust, intended consumer and operational use" [§1].
- **Hermes** (topluluk pratiği; K + sınırlı D). Bellek yazımı ayrı bir kilit dosyası alır ve değiştirmeden önce diski yeniden okur; okunamayan dosya boş sayılıp üzerine yazılmaz; belirsiz eşleşme ve dışarıdan yapılmış düzenleme reddedilir; toplu işlem son bütçe ve anlamsal kontrollerden geçmezse hiçbir şey yazılmaz [HA-N07 §3–4]. Disk, çalışan bellek nesnesi ve oturum başında donmuş istem görüntüsü üç ayrı durumdur: "Normal `_mutate` snapshot'ı güncellemez" [§5]. Yazma onay kapısı yapılandırmaya bağlıdır ve varsayılanı kapalıdır [HA-N02 §6]. Arka planda çalışan bir inceleme çatalı konuşmadan bellek ve beceri değişikliği önerir [HA-N02 §1; HA-S01 §2].
- **ECC** (topluluk pratiği; K + test kaynağı). Memory Vault'ta kayıt türleri (context, decision, fact, handoff, lesson, note, preference, runbook) yalnız sınıflandırmadır; tek güven durumu `unreviewed`dir; durumlar active/rejected/superseded; kabul edilmiş bilgi kasada değil, yönetilen repo belgelerinde yaşar: "unreviewed context → evidence review outside the vault → separately governed artifact" [ECC-N06 §2]. Yazım yalnız-oluşturma (create-only) ilkesiyledir; kapsamlar proje/ekip/kullanıcı, kullanıcı kapsamı hiçbir zaman örtük eklenmez [§3–4]. Buna karşılık "içgüdü" yolu gözlemden model yazımına ve oturum başında bağlama incelemesiz gider [ECC-N07 §1, §3, §6]. ECC'nin genel yargısı: bu mekanizmalar "should not be collapsed into one memory database or one trust ladder" [ECC-CORE §6].
- **superpowers** (topluluk pratiği). Plan başına karalama alanı ve ilerleme defteri devamı sağlar; kayıtlar bilerek kısa ömürlüdür: "Recovery while scratch exists and retaining necessary decisions after cleanup are different promises" [SP-S03 §5]. (Commit edilmemiş defterin olağan temizlikle silinmesi R05 satır 14'te.)
- **Playbook** (tedarikçi iddiası). Aynı hata iki kez olunca CLAUDE.md'ye düzeltme eklemek pratiktir ama "the system can accumulate a growing instruction file that attempts to solve mechanical failure with more prose" [PB-01 §7.2]. Üretim olayları kalıcı değerlendirme vakasına dönüşür [§8.4].
- **ai-knowledge-strategies.** Değişken yönetişim model ağırlıklarına gömülmez: "Development OS için mutable governance/context external and explicit kalmalı" [AKS-FT §19.1]. Önbellek bellek değildir [AKS-CAG §27.2]. İlişki grafiği kullanılırsa kanonik kaynağın yerine değil, "canonical source'a exact provenance ile bağlı derived relation/index layer" olarak [AKS-KG §25.1, §25.4].

### 2.2 Bellek katmanları ve yaşam döngüsü: somut olarak nasıl yapılıyor (özellikle istenen 2)

| İşlem | gstack | ECC | Hermes | İlke (CMH, Carbon) |
|---|---|---|---|---|
| **Yazma** | Kontrol noktası açık komutla. Ders kaydı şema doğrulaması ve talimat-enjeksiyon süzgecinden geçer; zararlı ders "rejected and nothing is persisted" [GS-MEM §2, §7]. Planlama belleğine geri yazım kişisel güven + özellik bayrağı koşullu; sabitlenen sürümde kapalı [§22]. | Kasa: çağıranın içeriği, sabit active/unreviewed, sır desen kontrolü, yalnız-oluşturma [ECC-N06 §2, §4]. İçgüdü: gözlemci model kişisel dizine doğrudan yazar; bekleyen kayıt ya da onay yok [ECC-N07 §3]. | Doğrudan ya da onay kapısıyla bekleyen öneri; kapı varsayılan kapalı [HA-N02 §6; HA-N07 §2]. | Yazma, aday oluşturma ve nitelemeyle başlar [CMH-02 §4.1–4.3]. |
| **Güncelleme** | Yerinde değil; yeni satır eklenir ve "Search resolves duplicate `key + type` rows by selecting the latest winner" [GS-MEM §4]. | Yeni kayıt; eski kayıt değişmez [ECC-N06 §5]. | Değiştirme/silme tam eşleşme ve dış düzenleme kontrolüyle [HA-N07 §3]. | "overwrite mi, version mi, temporal interval mi, conflict set mi, invalidate mi" [CMH-02 §4.5]. |
| **Yerine koyma** | En yeni kazanır; geçmiş satırlar durur [GS-MEM §4]. | "A new record linking to an old one does not change the old record's status"; elle `superseded` durumu gerekir [ECC-N06 §5]. | Değiştirme (replace) ile; okunan notlarda ayrı bir yerine koyma ilişkisi anlatılmıyor [HA-N07 §3]. | `supersedes`, `valid_to` alanları [CMH-02 §8]; güncel durum yenilenir, önceki tarih olarak kalır [TCL-M-RES §6]. |
| **Unutma, budama** | Kullanıcı onaylı budama satırları siler; planlama belleğinde TTL [GS-MEM §4, §8, §9]. | Durum rejected/superseded; bekleyen kayıtlara TTL; aktif içgüdülerde belgelenen haftalık çürüme incelenen yolda uygulanmıyor [ECC-N07 §4]. | Küratör yaş ve kullanıma göre aktif → eski → arşiv; pinli ve zamanlanmış işte anılan beceriler korunur; yeni ve hiç kullanılmamış beceri sırf sıfır kullanım yüzünden arşivlenmez; LLM ile birleştirme varsayılan kapalı [HA-N03 §2, §4]. | Unutma bir yetenektir; aktif seçimden çıkarmak ≠ fiziksel silmek [CMH-02 §15; TCL-M-ASM §4]. |
| **Çakışma** | Aynı anahtarda çelişen dersler budamada model yardımıyla işaretlenir (deterministik değil) [GS-MEM §8]; planlama belleği modele son kararlarla çatışmayı işaretlemesini söyler [§21]. | Projeler arası terfi aynı kimliğe (ID) göre gruplar, anlama göre değil [ECC-N07 §4]. | Belirsiz eşleşme reddi; dış düzenleme farkında yedek alıp ret [HA-N07 §3]. | Zamansal güncelleme ≠ gerçek çatışma [CMH-02 §8; TCL-M-RES §5]. |
| **Tazelik** | Gözlenen ve çıkarılan derslerde yaklaşık 30 günde bir puan güven düşüşü; kullanıcının söylediğinde düşüş yok [GS-MEM §5]. Dayandığı dosya değişince ders geçersizleşmez [§5]. Planlama belleğinde TTL + uç nokta kimliği + şema kimliği + açık geçersizleştirme [§11]. Kontrol noktası anlamca yeniden doğrulanmaz [§2]. | Kayıt zamanları var; otomatik güncellik yok; terminal görünümü statüyü göstermez [ECC-N06 §5]. | Oturum başında donmuş görüntü; sıkıştırma sınırında yenileme [HA-N07 §5; HA-S02 §4]. | `observed_at`, `valid_from` / `valid_to` [CMH-02 §8]. |
| **Köken** | Kaynak türü {observed, user-stated, inferred, cross-model}, beceri, dal/commit, dosyalar, güven bayrağı [GS-MEM §4, §6]. | MCP sunucusu kaynak kimliğini kendisi damgalar; argümanla değiştirilemez [ECC-N06 §7]. | Köken etiketi foreground/background_review [HA-N02 §5]; `created_by` yönetim politikasıdır, tarihsel yazarlık değil [HA-N03 §3]. | `source_refs`, `epistemic_status` [CMH-02 §23]. |
| **Kapsam** | Proje kapsamı; başka projeden yalnız `trusted === true` (kullanıcı ifadesi) gelir; kullanıcı profili bilerek projeler arası; hassas konular diske yazılmadan önce süzülür [GS-MEM §6, §14, §15]. | Proje/ekip/kullanıcı [ECC-N06 §3]. İçgüdüde kapsamı etiket değil konum belirler: "Changing frontmatter to global is therefore not, by itself, global materialization" [ECC-N07 §5]. | Profil ve store bağlama [HA-S01 §2]. | Actor/work kapsamı [CMH-02 §16, §23]. |
| **Tüketim** | Rol başına alt küme; bayat işareti son sınırda kayboluyor [GS-MEM §9, §12]. Planlama belleği "an **active decision input**" [§21]. | SessionStart'ta eşik + sıralama + üst sınır [ECC-N07 §6]. Kimlikle doğrudan okuma tarihsel kaydı da döndürür; tüketici statüye bakmalı [ECC-N06 §5]. | Gönderim kopyası ayrı; bellek ön-getirimi tur başına [HA-S02 §3]. | "recall ≠ context use" [CMH-02 §3]. |

### 2.3 Varyantlar ve ödünleşimler

- **Otomatik yazım / kapılı yazım.** Otomatik yazım (Hermes inceleme çatalı, ECC içgüdüleri) sürekliliği ucuzlatır ama incelemesiz davranışa girer. Kapılı yazım (ECC kasasının `unreviewed` durumu, Hermes onay kapısı, gstack budama onayı) güveni artırır, insan ya da koordinatör dikkati ister.
- **Kaynağa göre çürüme asimetrisi** (gstack). Kullanıcının sözü kalıcıdır, model gözlemi zamanla zayıflar. Çalışma sınırını da yazar: "This is not universally safe — user preferences and facts can also change" [GS-MEM §5].
- **Tek depo / çoklu kanal.** gstack dört kanal kullanır; Carbon dört işlevi dört bileşene çevirmez; ECC tek veritabanına ya da tek güven merdivenine indirgemeyi reddeder [ECC-CORE §6].
- **Etkileşimli / gözetimsiz yolda arıza kutbu.** Etkileşimli kurulum bozuk politika dosyasını karantinaya alıp yeniden sorar; gözetimsiz içe aktarma politikayı okuyamazsa hiçbir şey yazmadan durur, çünkü aksi kayıtlı bir "yasak" kararını atlatabilir [GS-MEM §17–18, M12].

### 2.4 Başarısızlıklar ve karşı örnekler

- **gstack.** Bayat işaretinin tüketimde kaybı [GS-MEM §12]; kontrol noktasındaki iddiaların geri yüklemede yeniden doğrulanmaması [§2]; dayandığı dosya değişince dersin geçersizleşmemesi [§5]. — *kaynak diyor* · K+T.
- **ECC.** Terfi anlamı değil kimliği gruplar: "Different meanings under one ID are a source-derived counterexample to interpreting promotion as semantic agreement" [ECC-N07 §4]. İçgüdüler incelemesiz oturum bağlamına girer [§6]. Kasada bağlantı yerine koyma değildir; terminal görünümü statüyü göstermez; düz komut satırı görünümü geçersiz dosya teşhisini göstermez [ECC-N06 §5–6]. Tek bir başarısızlık değişiklik önerisi üretmeye yeter, oysa gerekçe metni "tekrarlanan başarısızlık" der [ECC-N08 §4]. `healthy_skills` hiç gözlemi olmayan beceriyi de sağlıklı sayabilir [§3]. — *kaynak diyor* · K (+ E04 dar denemesi).
- **Hermes.** Yazma hatasında disk eski, çalışan nesne yeni, donmuş görüntü eski kalabildi (M01) [HA-N11]; toplu işlemde `new_text` takma adı ön taramaya uğramadan yazılabildi (M02, zararsız işaretle sınandı) [HA-N11]; onaylanan yazı uygulandıktan sonra bekleyen kayıt silinemezse "Approved" mesajıyla birlikte kayıt kalabildi (N11) [HA-N11]; birleştirme beyanı (`absorbed_into`) içeriğin korunduğunu kanıtlamaz, rapor argümanları 400 karakterde kesilir [HA-N03 §6]; küratör istemi "ondan az arşivleme"yi erken durma sayıyor, bu gereksiz değişikliğe iten bir nicelik baskısı olabilir (çalışmanın kendi hipotezi) [HA-N03 §8]. — *kaynak diyor* · K + sınırlı D.
- **CMH, kendini besleme.** "model inference → memory write → later recall → model sees its own old inference as context → confidence amplification" [CMH-02 §17]. — *kaynak diyor* · A.

### 2.5 Standart seviye kontrol listesi — bellek

**BE-1 — Bellek sınıfları ve yetki sırası**
- *Amaç:* Her kalıcı kaydın bir sınıfı olsun ve çakışmada hangisinin kazanacağı önceden belli olsun. Önerilen sıra: kanonik durum (STATE, Batu'nun kararları ve birebir sözleri) > kabul edilmiş karar ya da ders > kaynağa bağlı bulgu > doğrulanmamış çıkarım ya da gözlem > oturum karalaması. Tarihsel kayıt yalnız tarih olarak okunur.
- *Yokluğunda:* Rol belleğindeki eski bir ders STATE'teki güncel kararı ezer (bağlam, yetki). Batu'nun sözü ile model çıkarımı eşit ağırlık alır.
- *Bedel:* Sınıf başına yer ya da alan; düşük.
- *Gerçekten gereksiz:* Belleğin tek sınıftan oluştuğu iş (ör. yalnız STATE). Kalıcı roller rol belleği getireceği için EXP-007'de geçerli değil.
- *Dayanak:* CMH-02 §6, §22; ECC-N06 §2; GS-MEM §1.

**BE-2 — Köken etiketi ve yazan rol**
- *Amaç:* Her kayıtta kaynak türü (Batu söyledi / gözlendi / çıkarıldı / başka model), kaynak işaretçisi (yol#bölüm, SHA), yazan rol ve tarih.
- *Yokluğunda:* Model çıkarımı sonraki oturumda "bilinen gerçek" olur ve kendini besler (doğrulama). Batu'nun sözü ile Claude'un yorumu ayrılamaz; A003 §3.1'deki A–B–C ayrımı kaybolur.
- *Bedel:* Yazım başına dört-beş alan.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-MEM §4, §6; CMH-02 §7, §17; ECC-N06 §7. R05 satır 20 dersler için kaynak etiketini verdi; buradaki ek, bütün bellek sınıflarına ve yazan role genişletmedir.

**BE-3 — Aday ile kabul edilmişin ayrılması**
- *Amaç:* Yeni kayıt varsayılan olarak "aday"dır. Kabul, adı konmuş ayrı bir kararla (Batu ya da koordinatör, yetkisine göre) olur ve kayda işlenir.
- *Yokluğunda:* Alt ajanın önerdiği ders ya da karar sessizce yöntem olur (roller, yaşam döngüsü). Batu'nun yetkisindeki bir şey modelce kabul edilmiş görünür.
- *Bedel:* Kabul adımı; biriken adayların gözden geçirilmesi.
- *Gerçekten gereksiz:* Belleğe yalnız Batu'nun yazdığı durum. EXP-007'de alt ajanlar ve koordinatör de yazıyor.
- *Dayanak:* ECC-N06 §2; HA-S01 §2–3; PB-03 §5.5 (gölge modda deneme, sonra sınırlı etkinleştirme). R06 statü etiketlerini tasarım önermeleri için verdi; buradaki ek, bellek kayıtlarına uygulanmasıdır.

**BE-4 — Açık yerine koyma**
- *Amaç:* Yeni kayıt eskisini adıyla geçersiz kılar ve eskinin durumu "yerine konmuş" olur. Bağlantı tek başına yerine koyma değildir. Eski kayıt tarih olarak kalır.
- *Yokluğunda:* Arama eskiyi ve yeniyi aynı ağırlıkta getirir (bağlam). Çelişkili dersler aynı rol paketine birlikte girer (roller).
- *Bedel:* Yazımda "yerine koyduğu" alanı ve eski kaydın durum güncellemesi.
- *Gerçekten gereksiz:* Hiç güncellenmeyen bellek. EXP-007'de kararlar ve dersler değişecek.
- *Dayanak:* ECC-N06 §5; GS-MEM §4; CMH-02 §4.5, §8; TCL-M-RES §6. R04 (b)4 ilkeyi kurdu ("no universal latest-wins"); burada mekanizması.

**BE-5 — Kayıt zamanı, geçerlilik zamanı ve dayandığı sürüm**
- *Amaç:* "Ne zaman yazıldı", "hangi zaman için geçerli" ve "hangi dosya@SHA'ya dayandı" ayrı alanlar olsun.
- *Yokluğunda:* Geçmişte doğru olan bir kayıt bugünkü yanlış eyleme dayanak olur. Carbon'daki CrikIT örneği: eski "onay yok" kaydı güncel sayılırsa, sonradan onay almış iş yanlış durdurulur; kayıt silinirse geçmişte neden durulduğu açıklanamaz [TCL-M-ASM §1]. Dayandığı dosya değiştiğinde fark edilmez.
- *Bedel:* İki-üç alan.
- *Gerçekten gereksiz:* Hiç değişmeyen olgular. EXP-007'deki durum ve kararlar değişken.
- *Dayanak:* CMH-02 §8; TCL-M-ASM §6 ("kayıt zamanı ile geçerlilik zamanı; geçmiş onay ile güncel yetki"); GS-MEM §4 (dal/commit, dosyalar).

**BE-6 — Sınıfa göre tazelik ve geçersizleştirme**
- *Amaç:* Çıkarım ve gözlem türü kayıtlar için gözden geçirme tarihi ya da yaşla düşen güven. Batu'nun sözleri için çürüme yok ama açık yerine koyma var. Dayandığı dosya değişince kayıt "yeniden bak" işareti alır.
- *Yokluğunda:* Eski çıkarımlar süresiz aynı güçte kalır (bağlam kirlenmesi). Ya da her şey her seferinde yeniden sınanır (maliyet).
- *Bedel:* Aşama sonu bakımı; basit bir dosya-değişikliği kontrolü.
- *Gerçekten gereksiz:* Birkaç günlük, tek aşamalı iş. EXP-007 P0–P6 boyunca sürer.
- *Dayanak:* GS-MEM §5 (asimetri ve eksik dosya-değişikliği geçersizleştirmesi), §11 (birden çok sinyalli geçerlilik); R05 satır 20'nin risk sütunu.

**BE-7 — Çakışma kuralı**
- *Amaç:* İki kayıt çeliştiğinde önce "farklı zamanlar mı (güncelleme) yoksa aynı zaman için gerçek çatışma mı" sorulur. Gerçek çatışma tek gerçeğe indirgenmeden açık kalır ve yetki sırasına (BE-1) göre çözülür ya da Batu'ya gider.
- *Yokluğunda:* "En yeni kazanır" kısayolu yanlış işe ait ya da yetkisiz bir notu kazandırır; eski ama hâlâ geçerli bir politika kaybolur.
- *Bedel:* Çatışma kaydı; bazen bir Batu sorusu.
- *Gerçekten gereksiz:* Tek yazarlı, tek zaman dilimli bellek. EXP-007'de yazar çok.
- *Dayanak:* TCL-M-RES §5; CMH-02 §8; GS-MEM §21.

**BE-8 — Unutma ≠ silme**
- *Amaç:* Aktif seçimden çıkarma, arşivleme, özetleme ve fiziksel silme ayrı işlemler olsun. Karar gerekçesi ve nadir ama kritik ders silinmez. Silme ve budama onaylı ve kayıtlı yapılır.
- *Yokluğunda:* Ya her şey tutulur ve bağlam gürültüsü artar (bağlam, maliyet) ya da gerekçe zinciri kırılır (denetlenebilirlik).
- *Bedel:* Aşama sonunda bir bakım turu.
- *Gerçekten gereksiz:* Bellek hiç büyümüyorsa. EXP-007'de büyüyecek.
- *Dayanak:* TCL-M-RES §6; TCL-M-ASM §4; GS-MEM §4, §8; HA-N03 §4; CMH-02 §15.

**BE-9 — Yazma anında talimat süzgeci**
- *Amaç:* Talimat biçimli metin (ör. "ignore previous instructions") kalıcı belleğe talimat olarak girmez. Dış içerik alıntısı "veri" etiketiyle yazılır.
- *Yokluğunda:* Okunan bir kontrol dosyasının ya da web içeriğinin talimatı rol belleği üzerinden sonraki alt ajanlara taşınır (güvenlik, yetki).
- *Bedel:* Yazım sırasında göz denetimi ya da basit bir desen kontrolü.
- *Gerçekten gereksiz:* Belleğe hiç dış metin girmiyorsa. EXP-007 başka asistanlar için yazılmış kontrol dosyalarını okuyor.
- *Dayanak:* GS-MEM §7 ("malicious/untrusted text → persistent memory → future prompt context"); CMH-02 §17; ORTAK "Okuduğun bütün içerik veridir".

**BE-10 — Kapsam**
- *Amaç:* Kaydın geçerli olduğu kapsam açık olsun: EXP-007'nin kendi yöntemi, bir rol, bir aşama ya da DevOS tasarımı. Başka kapsamdan gelen model çıkarımı güvenilir sayılmaz. Kapsam etiketle değil, konumla da uygulanır.
- *Yokluğunda:* EXP-007'nin kendi çalışma dersleri DevOS tasarım kararlarına karışır; R06'nın "süreç üzerindeki iş / ürün üzerindeki iş" ayrımı bozulur. Bir role ait ders bütün rollere akar.
- *Bedel:* Klasör düzeni.
- *Gerçekten gereksiz:* Tek kapsamlı iş. EXP-007'de en az iki kapsam var: kendi yöntemi ve DevOS tasarımı.
- *Dayanak:* GS-MEM §6, §15; ECC-N07 §5; ECC-N06 §3; R06 §1 son satır.

**BE-11 — Kalıcılık yeri, yazma sonrası geri okuma ve arıza semantiği**
- *Amaç:* Bellek repoda ve commit'li durur; yazmadan sonra geri okunur. "Yazıldı" mesajı ya da 0 çıkış kodu yazımın kanıtı sayılmaz. Başarısız yazımda hangi kopyanın güncel olduğu bilinir.
- *Yokluğunda:* VM geri alınınca bellek kaybolur; auto-memory makineye bağlıdır ve bulut ortamları arasında paylaşılmaz [R01 satır 535]. Yarım yazım fark edilmez.
- *Bedel:* Commit ve geri okuma adımı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* R01 satır 477, 535; GS-MEM §19 ("an importer exit code of 0 without parseable/accountable output is not accepted as proof that data landed"); HA-N11; ECC-MC §5, §7. R05 satır 14 commit'i verdi; buradaki ek geri okuma ve arıza semantiğidir.

**BE-12 — Bakım ritmi ve sağlık ölçüsü**
- *Amaç:* Aşama sonunda budama, uzlaştırma ve yerine koyma kontrolü. "Kullanıldı" ya da "okundu" sayısı fayda sayılmaz. Sağlık etiketi veri yokluğunu "sağlıklı" saymaz.
- *Yokluğunda:* Bellek sessizce çürür; sayaçlar yanlış güven verir (gözlemlenebilirlik).
- *Bedel:* Aşama başına bir bakım turu (bir alt ajan).
- *Gerçekten gereksiz:* Aşamasız kısa iş.
- *Dayanak:* HA-N30 ("yüklenmiş veya yeniden kullanılmış diye kaydedilmiş olmak etkili öğrenme/görev başarısı değildir"); HA-S01 §4; ECC-N08 §3; HA-N03 §4, §8.

---

## 3. Kalıcı roller: rol tanımları ve rol belleği

### 3.1 Rol tanımının anatomisi (özellikle istenen 1)

"Rol" üç sistemde farklı biçimde yaşıyor (*kaynak diyor*):
- **gstack:** rol = beceri (skill). `SKILL.md.tmpl` şablonu ve ortak çözücülerden host'a göre `SKILL.md` üretilir. Kök beceri bir yönlendiricidir (router) [GS-PLAN §6–7]. Ayrıca bir becerinin içinde çağrılan geçici uzmanlar vardır (Review Army) [GS-MA §1.2].
- **superpowers:** rol = rol sözleşmesi şablonu (implementer, task reviewer, re-reviewer, final reviewer) + koordinatörün (controller) derlediği görev tanımı. Yöntemler beceri olarak durur [SP-U03 §2; SP-CORE §3].
- **ECC:** rol = agent tanımı (`agents/*.md`, YAML üst bilgi ve gövde), komut (`/plan`, `/prd`, `/tdd`, `/pr`) ya da bir beceri içindeki persona (dev-team) [ECC-N39 §1–2, §4, §7].
- **Hermes:** beceri kütüphanesi ve yönetim meta verisi [HA-N03; HA-N30].
- **Claude Code karşılığı:** `.claude/agents/*.md`, YAML üst bilgi + gövde (gövde sistem istemidir) [R01 satır 35, 72].

| Alan | gstack | superpowers | ECC | Claude Code (R01) |
|---|---|---|---|---|
| Kimlik, çağrılma koşulu | Kök yönlendirici niyeti uzmana eşler; `proactive` tercihi otomatik çağrıyı kapatabilir; bazı beceriler önceki aşamadan `benefits-from` [GS-PLAN §7]; yönlendirme yükünü üst bilgi taşır [GS-EVAL §27, V18] | Ad + açıklama ("ne yapar, ne zaman") [SP notes/U06A, X07] | `name`, `description`; planner'ın "proactive" açıklaması /plan'ın açık seçim kuralıyla aynı değil [ECC-N39 §4] | `name`, `description` zorunlu |
| Amaç, kesin sınır | office-hours "produces design docs, not code, and must not invoke implementation work" [GS-PLAN §1] | Uygulayıcı ve gözden geçiren ayrı; salt-okunur gözden geçirme yazılı [SP-U03 §2–3] | dev-team "analysis-only"; /plan koddan önce onay bekler [ECC-N39 §4, §7] | Gövde (sistem istemi) |
| Girdi sözleşmesi | Uzmana: "checklist; stack context; same diff command; optional prior domain learnings; a strict JSON-lines finding schema" [GS-MA §1.2]; plan-eng-review'da önce hedef çözülür [GS-PLAN §3] | Rol başına zorunlu girdiler tablosu [SP-U03 §2] | Koordinatör özeti + her istemde güvenilmeyen-veri uyarısı [ECC-N39 §7] | Görev istemi |
| Çıktı sözleşmesi | Katı JSON satırları; onaylı tasarım belgesi "decision record, not a transcript"; kapsam dışı listesi, hata kayıtları, karar günlüğü [GS-MA §1.2; GS-PLAN §2–3]; alt akışın makinece okunur sonucu [GS-MA §2.4] | Statü kodları DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT; gözden geçiren: spec kararı + doğrulanamayan gereksinimler + önem sıralı bulgular + kalite kararı; yeniden gözden geçiren: bulgu başına ADDRESSED / NOT ADDRESSED [SP-U03 §2, §4] | Sentezde anlaşmazlıklar korunur; tekrar eden kaygı "blocking" sayılır [ECC-N39 §7] | — |
| Yetki, durma | En az iki seçenekten sonra kullanıcı seçimi için DUR; "one finding → one user decision" [GS-PLAN §1, §8] | Dört durma sınıfı; olağan çatışmada koordinatör kararı; işçi ve gözden geçiren alt ajan açamaz [SP-S03 §4; SP-CORE §3] | Güvenlikle ilgili değişiklik açık insan onayına kadar BLOCKED (optimizer) [ECC-N40 §6] | `permissionMode` |
| Araçlar, model | Rol başına merkezi model seçimi: "Model resolution is centralized and environment-overridable per role (`capture`, `warmup`, `distill`, `judge`)" [GS-EVAL §19.1]; host'a göre araç adı dönüşümü [GS-MA §10] | 4.–5. düzeltme turunda daha yetenekli modelle taze işçi [SP-U03 §4] | `tools` dizisi, ayrı `model` alanı; planner: Read/Grep/Glob ve opus [ECC-N39 §2]; `allowedTools` önceden onaydır, araç kısıtı değil [ECC-N53 §4] | `tools`, `model`, `maxTurns`, `isolation`, `background` |
| Bellek bağlantısı | Beceri başına bellek alt kümesi; ders satırlarında `skill` alanı; uzmanlara alan dersleri [GS-MEM §4, §9; GS-MA §1.2] | Plan başına kısa ömürlü defter [SP-S03 §5] | İçgüdüler oturum başında, rol ayırt etmeden; beceri gözlemleri [ECC-N07; ECC-N08] | `memory: project` → `.claude/agent-memory/<ad>/`; MEMORY.md'nin ilk 200 satırı ya da 25 KB'ı yüklenir [R01 satır 80] |
| Bütçe | Beceri başına bellek bayt bütçesi; talimat bütçesi testi [GS-MEM §10] | Açık bütçe yok; en fazla 5 düzeltme turu [SP-U03 §4] | Profil bütçe alanları; bir kısmı yalnız metin olarak iletilir, yaptırım değil [ECC-CORE §5.3; ECC-N32 §3] | `maxTurns` |
| Kalite, değerlendirme | Gerçek modelle E2E ve LLM yargıç [GS-PLAN §1]; yönlendirme E2E [GS-EVAL §22]; uzman seçiminde "historical hit-rate gating" [GS-MA §1.2] | Ayrı değerlendirme laboratuvarı (yöntemli ve yöntemsiz kollar) [SP-S01 §1–3] | Beceri sağlığı, değişiklik önerisi, değerlendirme; harness karnesi [ECC-N08; ECC-N40] | — |
| Sürüm, köken, sahiplik | Şablon → çözücüler → host'a göre üretim; kaynak ≠ kurulu ≠ çalışan [GS-PLAN §6; TCL-H17 §2] | Arşiv ve eşitleme kanalları farklı içerik taşıyabilir [SP-S02 §3] | Birincil optimizer ile Kiro kopyası ayrıştı [ECC-N40 §7; ECC-N53 §1–3] | Repoya commit, git geçmişi |
| Yaşam döngüsü | Tekrarlanan hata → adı konmuş ayrım → yardımcı → değişmez kural → test → CI [GS-CORE §12] | Yöntem değişikliği döngüsü ve bakımcı kabulü [SP-S01 §2] | `evolve` kümelerden ajan adayı üretir: en az 3 üye, ortalama güven ≥ 0,75 [ECC-N07 §4] | — |

Hermes ayrıca yönetim yetkisini tarihsel yazarlıktan ayırır: "`created_by: agent` … Kullanıcı tarafından sahiplenilen bir becerinin bu alana geçirilmesi, dosyayı tarihsel olarak ajanın yazdığını kanıtlamaz" [HA-N03 §3].

**Ortak anatomi (*çıkarım*).** Üç sistemde tekrar eden ya da başarısızlıkları yokluğunu gösteren alanlar:

1. kimlik ve çağrılma koşulu (ad; "ne yapar, ne zaman kullanılır");
2. amaç ve kesin sınır (asla yapmayacakları);
3. girdi sözleşmesi (zorunlu paket alanları; BA-4);
4. bilinçli saklananlar;
5. çıktı sözleşmesi (biçim, statü kodu, kanıt etiketi, sonraki tüketici);
6. yetki ve durma sınıfları (veremeyeceği kararlar dahil);
7. araçlar, model, tur sınırı ve yürütme semantiği (ön plan/arka plan, iç içe yasağı, zaman aşımı);
8. bellek bağlantısı (okuyacağı alt küme; yazabileceği kayıt türü ve yeri);
9. bütçe (bağlam, token);
10. kalite ölçütü ve regresyon seti;
11. sürüm, sahip, değişiklik geçmişi;
12. yaşam döngüsü durumu (aday, etkin, emekli).

Claude Code'un üst bilgisi bunlardan yalnız 1, 6'nın bir kısmı (`permissionMode`), 7, 8 (`memory`) ve 9'un bir kısmını (`maxTurns`) doğal alan olarak taşır [R01 satır 72, 80]. Kalanlar gövdede ya da yanında bir dosyada yazılı olmak zorundadır (*çıkarım*).

### 3.2 Rol belleği ve rolün kendini geliştirmesi

- **gstack.** Rol belleği ayrı bir depo değil, rol başına yönlendirmedir: planlama belleği beceri başına alt kümeyle gelir; ders satırları hangi beceriden geldiğini taşır; uzman gözden geçirenlere "optional prior domain learnings" verilir; uzmanlar "historical hit-rate gating" ile seçilir [GS-MEM §4, §9; GS-MA §1.2]. Gelişme depo düzeyindedir: "prose / local convention → real failure → named state distinction → reusable helper/resolver/runtime rule → structural invariant/scanner → behavioral/environment E2E → CI/release consequence when justified" [GS-CORE §12]. Retro beceri kullanımını ve dersleri girdi alır ama önerisi iş kabulü değildir [GS-DEP §19–21]. — *kaynak diyor* · K+T.
- **ECC.** Üç yol: (1) araç gözlemleri → isteğe bağlı gözlemci model → kişisel içgüdü dosyaları (tetik, eylem, güven, kanıt) → oturum başında bağlam [ECC-N07 §1–6]; (2) beceri çağrı izleri ve iyileştirme gözlemleri → sağlık raporu → Markdown değişiklik önerisi → değerlendirme; her kolda en az iki kayıt varsa ve yuvarlanmış başarı farkı pozitifse "promote-amendment" [ECC-N08 §1, §4–5]; (3) `evolve`, içgüdü kümelerinden beceri, komut ya da ajan adayı üretir ama "no trial task or correctness oracle occurs in these generator predicates" [ECC-N07 §4]. Harness optimizer ajanı değişiklikten önce geri alınabilirlik, yetenek ve regresyon tanımları ve üç kayıtlı deneme ister [ECC-N40 §6]. — *kaynak diyor* · K (+ E04 dar denemesi).
- **Hermes.** Arka plan inceleme çatalı konuşmadan bellek ve beceri önerisi çıkarır; yazım isteğe bağlı onay kapısından geçer; küratör kütüphaneyi yaş, kullanım, pin ve zamanlanmış iş referansıyla bakar; isteğe bağlı LLM birleştirmesi ayrı bir yoldur [HA-S01 §2–3; HA-N03 §2–5]. Hüküm: "Değişiklik yapılması, sonra kullanılması ve daha iyi sonuç üretmesi üç farklı kanıt gerektirir" [HA-S01 §4]. — *kaynak diyor* · K.
- **superpowers.** Rol başına kalıcı bellek yok. Gelişme yöntem düzeyinde, ayrı bir süreçle olur: hata → uygun müdahale katmanı seçimi (R05 satır 18) → yöntemsiz kontrol ve eski/yeni karşılaştırması ("These are different experiments") → değerlendirme laboratuvarı → bakımcı kabulü → dağıtım [SP-S01 §1–2]. Sınır: "report acceptance is not sound judgment, counted use is not task benefit, and a repaired measuring instrument is not an improved coding agent" [SP-CORE §6]. — *kaynak diyor* · K.
- **Carbon harness.** Değişiklik zinciri: "observed failure → competing explanations → discriminating evidence → candidate intervention → evaluation under stated conditions → authorized acceptance or rejection → later observation" [TCL-H12 §2]. Seçim, kabul, yürürlüğe girme ve sonraki kullanımda fayda ayrı sorulardır [TCL-H16 §4; TCL-H17 §2–3]. Bir yöntemin durumları: "stored, discoverable, loaded, applicable, followed and effective are not equivalent states" [TCL-H11 §4]. Dersin daraltılması ya da emekliye ayrılması da gelişmedir: "Retiring or narrowing a lesson can therefore be improvement too" [TCL-H16 §8]. — *kaynak diyor* · A.
- **Playbook.** Ajanı yönlendiren yapılandırma (CLAUDE.md, beceriler, hook'lar, istemler, model) değişince gerçek görevlerden oluşan bir set koşar; üretim olayları kalıcı vaka olur; vakalar zamanla ayırt ediciliğini yitirir ("challenge-set aging") [PB-01 §8.4]. Yeni otomatik gözden geçiren önce gölge modda çalışır, örnekleme ile denetlenir [PB-03 §5.5]. — *kaynak diyor* · tedarikçi iddiası.

**Sonuç (*çıkarım*):** Rol belleğinin görülen en olgun biçimi "rol başına yönlendirilen, köken etiketli, bakımlı küçük bir alt küme"dir (gstack deseni). Rolün kendini geliştirmesinin standart biçimi ise "öneri → sınama → kabul → yürürlük → sonraki kullanımda gözlem" zinciridir. Hiçbir çalışma otomatik öz-gelişmenin güvenilir çalıştığını göstermedi; ECC ve Hermes'in otomatik yolları başarısızlık örnekleri de üretti (§3.4).

### 3.3 Varyantlar ve ödünleşimler

- **Rolün taşıyıcısı.** Aynı bağlamda yüklenen yöntem (beceri), ayrı bağlamda çalışan alt ajan, paralel analiz personası ya da kullanıcının çağırdığı komut. ECC'de /plan varsayılan olarak satır içidir; planner alt ajanına yalnız çalışma ortamında bulunuyorsa ve kullanıcı açıkça isterse gider [ECC-N39 §4].
- **Kendiliğinden / açık çağrı.** Planner açıklamasındaki "proactive" ifadesi komutun açık seçim kuralıyla aynı değildir [ECC-N39 §4]. mattpocock-skills META'sındaki "kullanıcının çağırdığı / modelin çağırdığı beceri" ayrımı yalnız bir niteleme sinyalidir (§9).
- **Koşullu uzmanlar.** gstack'te büyük değişiklikte test ve bakım uzmanları her zaman çağrılır; güvenlik, performans, veri göçü, API sözleşmesi, tasarım ve sadeleştirme uzmanları değişiklik sinyallerine ve geçmiş isabet oranına göre çağrılır [GS-MA §1.2].
- **Rol başına model.** gstack'te merkezi ve değiştirilebilir [GS-EVAL §19.1]; superpowers'ta tıkanınca daha yetenekli modele geçiş [SP-U03 §4].
- **Tek kaynaktan üretim / elle kopya.** gstack şablondan host'a göre üretir [GS-PLAN §6]; ECC'de elle korunan kopya ana tanımdan ayrıştı [ECC-N40 §7].

### 3.4 Başarısızlıklar ve karşı örnekler

- **gstack, örtük yürütme semantiği.** Claude Code alt ajanları varsayılan olarak arka planda çalıştırmaya geçince eşzamanlı tamamlanma varsayan ebeveyn akışları takılı kaldı; bu üçüncü tekrardı [GS-MA §3; R05 satır 27]. Ders: rolün yürütme semantiği örtük kalmamalı. *Claude Code sürüm davranışı; bulut oturumunda ayrıca doğrulanmadı.*
- **gstack, taşınabilirlik.** Codex host'una çalıştıramayacağı Agent-aracı talimatları gidebiliyor: "Claude-host multi-agent contract ≠ automatically portable gstack-wide multi-agent contract" [GS-MA §10].
- **ECC, kopya ayrışması.** Kiro kopyası ana optimizer tanımındaki değerlendirme tanımlarını, üç deneme şartını ve güvenlik onayı kısıtlarını taşımıyor [ECC-N40 §7; ECC-N53]. Gemini dönüştürücüsü `tools: []` üretip eski liste satırlarını bırakabiliyor ve tanımadığı üst bilgiyi "already compatible" sayıyor [ECC-N39 §2–3]. Ajan kapsamlı karne, hiç ajan tanımı yokken tek bir ayar dosyasıyla 3/3 alabiliyor [ECC-N40 §2].
- **ECC, sınamasız üretim.** `evolve` ajan adaylarını deneme ve doğruluk ölçütü olmadan üretiyor [ECC-N07 §4]; tek başarısızlık değişiklik önerisine yetiyor [ECC-N08 §4].
- **superpowers, yazılı ama uygulatılmayan sınırlar.** Salt-okunur gözden geçirme yazılı ama "The templates do not install a permission boundary themselves" [SP-U03 §3]. İç içe alt ajan yasağı yalnız SDD'de var, paralel dağıtım becerisinde yok [SP-CORE §3].
- **Carbon harness, bağlantılı hata.** "every specialist faithfully applies the same outdated procedure. Consistency has increased, but the error is now correlated" [TCL-H11 §4, P1].
- **multi-agent-patterns, tören.** Yanlışlama yöntemi olmayan eleştirmenin her şeyi onaylayan pahalı bir ritüele dönmesi ("reviewer ritualization") [MAP-A §13 R7].

### 3.5 Standart seviye kontrol listesi — kalıcı roller

**RO-1 — Rol kataloğu ve türetme kaynağı**
- *Amaç:* Roller EXP-007'nin iş döngüsünden ve verilecek kararlardan türetilir; her rolün tek cümlelik amacı ve hangi iş sınıfı için olduğu yazılıdır. "Bu iş için rol gerekmez" de geçerli bir sonuçtur.
- *Yokluğunda:* Rol listesi ya her seferinde yeniden kurulur (Batu'nun U004 eleştirisi) ya da gereksiz rol birikir (maliyet, tören).
- *Bedel:* Bir katalog dosyası.
- *Gerçekten gereksiz:* Alt ajansız iş. EXP-007'de değil.
- *Dayanak:* GS-PLAN §3 ("These are not duplicate “review personalities.” They hold different work responsibilities"); MAP-A §12 C10; R04 (c)1.

**RO-2 — Rol dosyasının sabit alanları**
- *Amaç:* Rolü bir kez ve denetlenebilir biçimde tanımlamak (§3.1'deki 12 alan).
- *Yokluğunda:* Her görev tanımı rolü baştan tarif eder; tarifler kayar; aynı rol iki çağrıda farklı sınırlarla çalışır (tutarlılık, doğrulama).
- *Bedel:* Rol başına bir dosya ve bakımı.
- *Gerçekten gereksiz:* Bir görev kalıbı yalnız bir kez kullanılacaksa; tek seferlik rol görev tanımında kalabilir.
- *Dayanak:* §3.1 tablosu; R01 satır 72.

**RO-3 — Sabit rol metni ile değişken görev tanımının ayrılması**
- *Amaç:* Tekrar eden kısım (amaç, sınır, girdi/çıktı sözleşmesi, yetki, araçlar) rol dosyasında; değişen kısım (soru, kaynaklar, kapsam, dönüş yeri) görev tanımında durur.
- *Yokluğunda:* Görev tanımları uzar, koordinatörün bağlamını yer (BA-5) ve her seferinde farklı yazılır.
- *Bedel:* İki belge arasında tutarlılık bakımı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-PLAN §6 (iskelet + ortak çözücü + istek üzerine bölüm + host'a göre üretim); SP-S03 §3 (rol şablonu + koordinatörün derlediği görev tanımı); ECC-N39 §2, §4.

**RO-4 — Rol ≠ yetki ≠ yetenek**
- *Amaç:* Rol adı yetki vermez. Karar yetkisi DECISIONS'a ya da Batu'ya, araç izinleri ayrı bir alana bağlıdır. Rol dosyası hangi kararları veremeyeceğini açıkça yazar.
- *Yokluğunda:* "Doğrulayıcı" adlı alt ajan düzeltme yapar; araştırmacı kapsamı genişletir (yetki, yaşam döngüsü).
- *Bedel:* Yetki alanı ve durma sınıflarının yazımı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-MA §13.2 ("assigned role ≠ legitimate authority ≠ technical capability ≠ realized effect"); GS-CORE §6; MAP-A §7 (konum, yetki, yeterlik, sorumluluk ve hesap verebilirliğin eşitlenmesinin güvensizliği).

**RO-5 — Rol belleği**
- *Amaç:* Her rolün kendi alt kümesi olsun: rol dersleri, karşı örnekler, sık düşülen tuzaklar, geçmiş isabet (hangi bulgu türü işe yaradı). Kayıtlar köken etiketli (BE-2) ve bakımlıdır (BE-12). Rol dosyası hangi alt kümeyi okuyacağını söyler.
- *Yokluğunda:* Aynı hata her çağrıda yeniden yapılır; ya da bütün dersler bütün rollere akar (bağlam kirlenmesi).
- *Bedel:* Rol başına küçük bir bellek dosyası ve bakımı.
- *Gerçekten gereksiz:* Rol çok nadir kullanılıyorsa.
- *Dayanak:* GS-MEM §9; GS-MA §1.2; ECC-N07; R01 satır 80 (`memory: project`; bulut için belirsiz, bkz. §10).

**RO-6 — Rol değişiklik yolu**
- *Amaç:* Rol dosyası ya da rol belleği şu zincirle değişir: gözlenen hata → rakip açıklamalar → aday değişiklik (değişiklik yapmamak ve daha basit seçenek dahil) → sınama → yetkiye göre kabul → yürürlük (dosya commit'lendi ve sonraki çağrıda gerçekten yüklendi) → sonraki kullanımda gözlem.
- *Yokluğunda:* "Ders kaydedildi" = "rol gelişti" sanılır; ya da her hata bir kural daha ekler (talimat birikimi).
- *Bedel:* Değişiklik başına kısa bir not ve bir sınama çağrısı.
- *Gerçekten gereksiz:* Rol hiç değişmeyecekse.
- *Dayanak:* TCL-H12 §2; TCL-H16 §3–4; TCL-H17 §2–3; SP-S01 §1–2; HA-S01 §4. R05 satır 18–19 dersin nereye yazılacağını ve "değişiklik ≠ kullanım ≠ fayda" ayrımını verdi; buradaki ek, zincirin rol düzeyindeki adımları ve "yürürlük" kontrolüdür.

**RO-7 — Rol regresyon seti**
- *Amaç:* Her rol için birkaç temsili görev ve bilinen karşı örnek. Rol dosyası, model ya da ortam değişince yeniden denenir ve sonuç kaydedilir.
- *Yokluğunda:* Bir rol düzeltmesi başka bir durumu bozar ve fark edilmez. Model değişince eski iskeleler ya gereksiz ya yetersiz kalır: "her harness component modelin neyi kendi başına yapamadığına dair bir assumption taşır" [CMH-03 §17].
- *Bedel:* Rol başına küçük bir set; her değişiklikte birkaç çağrının token maliyeti.
- *Gerçekten gereksiz:* Rol değişmiyor ve model sabitse. EXP-007'de roller P0'da kurulacak ve değişecek.
- *Dayanak:* PB-01 §8.4; PB-03 §5.1 ("behavioral/configuration target + evaluation suite + exact configuration version + change gate"); SP-S01 §1; ECC-N40 §6.

**RO-8 — Açık yürütme semantiği**
- *Amaç:* Rol ön planda mı arka planda mı çalışır, ne kadar beklenir, zaman aşımında ne olur, kısmi başarısızlıkta ebeveyn devam eder mi, ortak çalışma ağacına yazabilir mi, iç içe çağrı yasak mı: hepsi rol dosyasında yazılı.
- *Yokluğunda:* Platform varsayılanı değişince ebeveyn akış takılır (gstack v1.79). Ortak çalışma ağacında yarım etkiler kalır (R05 satır 27).
- *Bedel:* Birkaç satır.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-MA §2.5, §3, §4, §13.4; SP-CORE §3; TCL-H11 §2.

**RO-9 — Tek kaynak ve kopya eşitliği**
- *Amaç:* Rol tanımı tek yerde durur; başka yerlerdeki kopyalar ya ondan üretilir ya da kaynakla eşitliği kontrol edilir.
- *Yokluğunda:* Kısa kopya güvenlik kısıtlarını kaybeder (ECC Kiro); hangi sürümün çalıştığı bilinmez (gözlemlenebilirlik).
- *Bedel:* Kopya yoksa sıfır.
- *Gerçekten gereksiz:* Tek kopya varsa.
- *Dayanak:* ECC-N40 §7; ECC-N53; GS-PLAN §6.

**RO-10 — Rol emekliliği ve birleştirme**
- *Amaç:* Kullanılmayan, işe yaramayan ya da başka rolle çakışan rol kapatılır ya da birleştirilir; gerekçe kayıtlı.
- *Yokluğunda:* Katalog büyür, rol seçim hatası artar (MAP-A C9: yönlendirme kararı da yanlış olabilir), bakım maliyeti artar.
- *Bedel:* Aşama sonu gözden geçirmesi.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* R06 §1 ("Roles can be closed or merged"); HA-N03 §4; TCL-H16 §8.

**RO-11 — Koordinatör de bir roldür**
- *Amaç:* Ana oturumun rol tanımı: neyi yapar (paket derleme, karar, birleştirme, kalıcı dosyalara yazma), neyi yapmaz, hangi kararları verebilir, hangi durma sınıflarında Batu'ya gider. Kararlarının gerekçesi gözlemlenebilir.
- *Yokluğunda:* Koordinatör hem darboğaz hem tek hata noktası olur (A003 §6 bunu zaten tanıdı) ve bu rol denetlenemez; her yeni oturumun koordinatörü farklı davranır.
- *Bedel:* Bir rol tanımı (CLAUDE.md ya da METHOD içinde).
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* SP-S05 §4 ("The controller does more than schedule"); MAP-A §7 ("Manager as a systemic failure point"), §13 R2; A003 §6.

---

## 4. Yaşam döngüsü ve ritimler: oturum, iş kalemi, aşama

### 4.1 Olgun sistemler ne yapıyor

**Oturum düzeyi**
- **gstack.** Açık kaydetme ve geri yükleme komutları; kontrol noktası alanları sabittir (§2.1). Geri yükleme önce aynı dalın en yeni kaydını seçer, başka dala düşerse uyuşmazlığı söyler; kontrol noktasındaki iddiaları yeniden doğrulamaz [GS-MEM §2]. Planlama becerileri başta bellek ön-okuması yapar, sonda engellemeyen bir arka plan yenilemesi başlatır [§9, §13]. — *kaynak diyor* · K+T + seçili E2E.
- **ECC.** Ritimler yaşam döngüsü olaylarına bağlı hook'larla kurulur: SessionStart (içgüdüler, oturum özeti) [ECC-N07 §6], PreToolUse (yapılandırma koruması [ECC-N09 §2]; ilk dokunuşta duraklatıp inceleme isteyen GateGuard [ECC-CORE §7.3]), PostToolUse (ölçüm köprüsü, bağlam izleyici, beceri izleyici) [ECC-N32 §1; ECC-N08 §2], Stop (maliyet satırı) [ECC-N32 §1]. — *kaynak diyor* · K.
- **Hermes.** İç içe yaşam döngüleri: kalıcı iş/amaç > konuşma oturumu > kullanıcı turu > model-araç yinelemesi > API denemesi. Tablonun bir sütunu şunu sorar: "Bir alt düzeyin bitmesi neyi kanıtlamaz?" [HA-S02 §1]. — *kaynak diyor* · K.
- **superpowers.** İki ayrı kurtarma vardır: "restoring the procedure/capability needed to work; recovering the particular task, accepted decisions and valid evidence" [SP-S02 §4]. — *kaynak diyor* · K.
- **Claude Code hook zamanlaması** (tedarikçi belgesinin TCL-H11'deki aktarımı): "PreToolUse can control admission; PostToolUse runs after the operation; Stop and SubagentStop concern normal completion, while StopFailure handles a different exit; asynchronous hooks cannot block the triggering action" [TCL-H11 §2]. *Bulut:* repo `settings.json` hook'ları yalnız tek repolu oturumda çalışır [R01 satır 527, 624].
- **CMH.** Uzun işte her oturum sınırlı bir artım yapıp commit ve ilerleme dosyasıyla kapanır; yeni oturum durumu dışarıdan kurtarır (R05 satır 16; CMH-03 §12).

**İş kalemi düzeyi**
- **superpowers.** Üç rota: kısa yoklama (spike), sınırlı (bounded), mimari (architectural). "The longest preparation route is not required for every request" [SP-CORE §2]. — *kaynak diyor* · K.
- **gstack.** office-hours → CEO ve mühendislik incelemesi → spec → issue → çalışma ağacı. Zincir zorunlu değildir; yönlendirici doğrudan sonraki aşamaya gidebilir [GS-PLAN "Short answer", §7]. Gerekli nitelik geçmiş törenle değil güncel durumla sağlanır: "gstack separates **qualification type** from **workflow provenance**" [GS-RQS §2]. — *kaynak diyor* · K+T.
- **ECC.** PRD → plan → TDD → PR; plan yazmak ve kilometre taşını "in-progress" yapmak koda izinden önce olabilir [ECC-N39 §4–5]. — *kaynak diyor* · K.
- **Hermes.** Görev, koşu, sahiplenme ve terminal durum ayrıdır; hakem modelin "DONE" demesi görevi bitmiş yazmaz, işçiye kapanış istemi üretir [HA-S03 §3]. — *kaynak diyor* · K + sınırlı D.

**Aşama ve uzun ufuk**
- **gstack /retro.** Belli bir dönemi yeniden kurar (commit'ler, test sağlığı, oturum desenleri, önceki retrolar, beceri kullanımı, dersler); trend, kazanımlar, gelişme alanları, alışkanlıklar ve kestirme-borç defteri üretir; anlık görüntüyü saklar [GS-DEP §19–20]. Tazelik koruması vardır: tazelik doğrulanamazsa "degraded" diye söylenir, veri açıkça bayatsa durur [§19.1]. Öneri iş kabulü değildir: "retro says “we should improve X” ≠ Work X has been admitted ≠ Actor Y is obligated" [§21]. — *kaynak diyor* · K+T.
- **Playbook.** Yapılandırma değişince değerlendirme seti koşar; üretim olayları kalıcı vaka olur; "challenge-set aging" [PB-01 §8.4]. — *tedarikçi iddiası*.
- **Carbon harness.** Evrim döngüsü (TCL-H12 §2) ve SRE hata sonrası inceleme benzetmesi; kaynak bu pratiğin "the cost of the process and deliberate trigger selection" boyutunu da kabul eder [TCL-H12 §2]. — *kaynak diyor* · A + L.
- **CMH.** Model ya da sürüm değişince yeniden kıyas ve bileşen çıkarma (ablation) [CMH-03 §17]. — *kaynak diyor* · L (Anthropic'in kendi deneyimi, tedarikçi iddiası).
- **ECC yöntem vakası.** İlişki-sınırı gözden geçirmesi; iddiaya göre durma; dış cevaptan önce sınırlı sonucu yayımlama ve "kaynak tamam" ile "yayın tamam"ı ayırma [ECC-MC §6, §8]. — *kaynak diyor* · çalışmanın kendi geçmişine dair retrospektif.

### 4.2 Varyantlar ve ödünleşimler

- **Açık komut / olaya bağlı otomatik hook.** gstack kaydı kullanıcı komutuyla yapar; ECC olaylara bağlar. EXP-007'de hook'lar hem Batu onayı (A-04) hem tek repolu oturum koşulu ister [R01 satır 527]; yoksa ritimler talimat düzeyinde kalır ve uyulması modele bağlıdır (*çıkarım*).
- **Tek boru hattı / ölçeklenen rotalar.** superpowers'ın üç rotası; tek hat karşı örneği R05 §3 madde 5'te.
- **Takvim ritmi / olay tetikli ritim.** gstack retrosu dönemseldir; playbook değerlendirmeleri değişiklik ve olay tetiklidir.
- **Sürekli ölçüm / dönemsel değerlendirme.** ECC hook'larla sürekli ölçer; gstack retro ile dönemsel değerlendirir.

### 4.3 Başarısızlıklar ve karşı örnekler

- **ECC, yarım işin atlanması.** Kesintiden sonra "sıradaki bekleyen kilometre taşını seç" kuralı yarım kalanı atlayabilir: "It can select a later milestone instead of resuming the already-in-progress one" [ECC-N39 §5]. — *kaynak diyor* · K (koşullu kaynak çıkarımı, olay gözlenmedi).
- **gstack, bayat retro.** Önceki bir hata eski ref'e ya da yanlış "bugün"e karşı tutarlı görünen retrolar üretmişti; koruma sonradan eklendi [GS-DEP §19.1].
- **Hermes, sayaç ile yürütmenin ayrışması.** Kalp atışı sayacı istem gerçekten çalışmadan ilerler; kayıt hatasında çalışan sayaç ilerlerken disk eski kalabildi; önceden yüklenmiş iki yönetici iki istem üretebildi [HA-S03 §5].
- **Hermes, "bitti"nin anlamı.** "`completed` regular loop'un son durumunu anlatır; dış işin kabul ölçütü değildir" [HA-S02 §6].
- **ECC yöntem vakası, tekrar eden yayın hataları.** Kanıt aktarımı ve dosya yeniden yazımı hataları tekrarladı; tespit ve kurtarma işe yaradı ama önleme gösterilmedi [ECC-MC §5, §7].

### 4.4 Standart seviye kontrol listesi — yaşam döngüsü ve ritimler

**YD-1 — Oturum açılış protokolü: yöntem ve görev ayrı**
- *Amaç:* İki ayrı kurtarma: (a) yöntem ve araçlar (CLAUDE.md, rol dosyaları, METHOD gerçekten yüklü mü); (b) görev (STATE, dal ve HEAD, açık kararlar, önceki devrin iddialarının kanıta karşı sınanması). Rol belleğinin hangi kuralla bağlama gireceği de burada tanımlıdır.
- *Yokluğunda:* Yeni oturum yöntemi yüklemeden çalışır: R01'e göre AGENT.md'nin otomatik yüklendiği belgelenmemiş ve bu repoda Claude Code'un kendiliğinden yüklediği bir giriş dosyası yok [R01 satır 531, 830]. Ya da yeni oturum eski devir notunu doğru sayar.
- *Bedel:* Oturum başına sabit bir okuma; bağlamdan pay.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* SP-S02 §4; GS-MEM §2 (dal uyuşmazlığının gösterilmesi); R01 satır 475, 830. R05 satır 15–16 ve R05 "top 8" madde 7 okuma sırasını ve devrin sınanmasını verdi; buradaki ek, yöntem yüklemesinin ayrıca doğrulanmasıdır.

**YD-2 — Oturum içi kontrol noktası ritmi**
- *Amaç:* Her sınırlı artımdan sonra commit (R05); buna ek olarak bağlam eşiğine yaklaşınca sıkıştırma öncesi kayıt (BA-6) ve uzun alt ajan işlerinden önce HEAD kaydı.
- *Yokluğunda:* VM geri alınırsa ya da sıkıştırma olursa son artım ve açık kararlar kaybolur.
- *Bedel:* Sık commit; küçük.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* CMH-03 §12; R01 satır 334, 539–546; GS-MA §4 (R05 satır 27).

**YD-3 — Oturum kapanış protokolü**
- *Amaç:* Sabit alanlı bir kontrol noktası (durum, dal, zaman, değişen dosyalar, yapılanlar, verilen kararlar, kalan işler, notlar) + aday dersler + maliyet satırı (MK-1) + yayın doğrulaması (commit ve geri okuma).
- *Yokluğunda:* Sonraki oturum neyin bittiğini ve neyin yalnız "yazıldığını" ayıramaz.
- *Bedel:* Oturum başına bir kayıt.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-MEM §2; ECC-MC §6 ("publishing a bounded result before its final outward response and keeping source completion distinct from publication completion"); R05 "top 8" madde 7 (devir başlıkları).

**YD-4 — Beklenmedik kesinti protokolü**
- *Amaç:* VM geri alınınca çalışan alt ajanların ve kabuk işlerinin kaybolduğu varsayılır. Yarım etkiler (kısmen yazılmış not, commit edilmemiş değişiklik) mutabakatla bulunur. Eksik iş aynı görev tanımıyla yeniden başlatılır ve bu kayda geçer.
- *Yokluğunda:* Yarım dosya tamam sayılır; kaybolmuş alt ajan "çalışıyor" sanılır.
- *Bedel:* Açılışta `git status` ve eksik not kontrolü.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* R01 satır 118–121 (arka plan işleri geri gelmez); EXP-007 STATE ("Oturum biterse yarım kalan ajan işi kaybolur", *gözledim*); GS-MA §4.3; HA-S03 §5.

**YD-5 — İş kalemi rotasının ölçeklenmesi**
- *Amaç:* En az üç rota (kısa yoklama, sınırlı iş, büyük tasarım) ve her rotanın zorunlu artefaktları. Hangi rotanın neden seçildiği kayıtlıdır.
- *Yokluğunda:* Ya her şey en ağır törenden geçer (maliyet; A003 §7'deki "gereksiz yavaşlık" sorusu) ya da büyük iş hafif yoldan geçer (kalite).
- *Bedel:* Rota seçim kaydı.
- *Gerçekten gereksiz:* Bütün işlerin aynı büyüklükte olduğu durum. EXP-007'de değil.
- *Dayanak:* SP-CORE §2; SP-S05 §8; TCL-H12 §2 (tetik seçimi); R05 §3 madde 5.

**YD-6 — Yarım işin önce devralınması**
- *Amaç:* Yeni iş seçmeden önce başlamış kalemler bulunur ve ya devralınır ya da gerekçesiyle park edilir. "Plan yazıldı ≠ başladı ≠ izin var ≠ bitti".
- *Yokluğunda:* Yarım iş unutulur, sonraki kalem başlar [ECC-N39 §5].
- *Bedel:* Açılışta bir kontrol.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* ECC-N39 §5; HA-S03 §3; R05 satır 13 (tamamlanma katları).

**YD-7 — Aşama kapanışı: retro ve ilişki-sınırı gözden geçirmesi**
- *Amaç:* Dönem, önceki aşamaya göre trend, işe yarayan ve yaramayan, borç defteri, aday dersler ve "gerekli olduğu halde kimseye verilmemiş iş var mı" sorusu. Öneriler iş kabulü değildir. Retronun dayandığı verinin tazeliği kontrol edilir.
- *Yokluğunda:* Aynı sorunlar aşamadan aşamaya taşınır; öneriler sessizce yükümlülüğe dönüşür ya da kaybolur.
- *Bedel:* Aşama başına bir rapor; A003 §3.6 zaten "kısa rapor" öngörüyor.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-DEP §19–21; ECC-MC §8; R05 satır 25.

**YD-8 — Olay tetikli ritimler**
- *Amaç:* Model ya da Claude Code sürümü değişince rol regresyonu (RO-7) ve iskelet varsayımlarının gözden geçirilmesi; Batu'nun düzeltmesi ya da bir olay → değerlendirme vakası; ortam varsayılanı değişince (ör. alt ajan çalışma biçimi) yürütme semantiği kontrolü.
- *Yokluğunda:* Eski varsayım sessizce bozulur (gstack v1.79); aynı düzeltme tekrar gerekir.
- *Bedel:* Olay başına küçük bir sınama.
- *Gerçekten gereksiz:* Model ve ortam sabit kalacaksa. A003 §6 "Claude Code'un özellikleri de değişecek" diyor.
- *Dayanak:* CMH-03 §17; PB-01 §8.4; GS-MA §3.

**YD-9 — Bakım ritmi**
- *Amaç:* Aşama sonunda bellek budaması (BE-12), rol gözden geçirmesi (RO-10) ve talimat bütçesi kontrolü (BA-5).
- *Yokluğunda:* Birikim ve bağlam gürültüsü.
- *Bedel:* Aşama başına bir alt ajan çağrısı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-MEM §8; HA-N03; PB-01 §7.2.

---

## 5. Gözlemlenebilirlik ve ilerleme takibi

### 5.1 Olgun sistemler ne yapıyor

- **CMH.** Gözlemin iki işi vardır: ajanın kendi sonucunu görmesi ve hatanın hangi katmanda (bağlam, bellek, araç, model, koruma, düzenleme) olduğunun ayrılması. "No trace → “agent kötü cevap verdi” aggregate symptom'ında kalırız" [CMH-03 §18]. A'dan J'ye hata sınıfları: algı/bağlam, araç/arayüz, yetki, düzenleme, bellek/durum, doğrulama, durma/yeniden deneme, gözlem, entropi/kayma, model-iskele uyumsuzluğu [§20]. — *kaynak diyor* · L + A.
- **Carbon harness.** Doğrulama, gözlem ve tanı ayrı işlerdir. İzlemenin (tracing) de bir gözlem sınırı vardır: "Missing data can reflect selection, privacy settings or delayed export rather than absence of an event" [TCL-H12 §1]. — *kaynak diyor* · A.
- **Playbook** (tedarikçi iddiası). Claude Code'un OpenTelemetry olayları: istemler ve yanıtlar, araç kararları ve sonuçları, izin modu değişiklikleri, MCP bağlantıları, eklentiler, beceri etkinleşmesi, hook yaşam döngüsü, API hataları ve yeniden denemeler, alt ajan tamamlanması ve soy ağacı, sıkıştırma, kullanım/maliyet/token ölçüleri [PB-01 §11]. Kullanım alanları: kontrollerin gerçekten çalıştığını doğrulamak, baypas yollarını bulmak, düzenleme maliyetini ölçmek, bir geçişi hangi ajanın ve aracın ürettiğini kurmak [PB-03 §5.4]. Sınır: "telemetry existence does not prove semantic correctness" [PB-01 §11]. *Bulut oturumunda kullanılabilirliği bu notta doğrulanmadı.*
- **gstack** (K+T). Değerlendirme kaydı geçti/kaldı ile yetinmez: maliyet, süre, deneme numarası, transkript, tur ve token, çıkış nedeni, zaman aşımı yeri, model, gecikmeler, yargıç puanları; koşu düzeyinde şema sürümü, dal/SHA, paket sürümü, zaman, CLI sürümü, katman, parça, duvar saati ve yeniden-deneme defteri [GS-EVAL §14]. Kısmi ve kesinleşmiş koşular ayrıdır [§15]. Karşılaştırılacak önceki yoksa açıkça söylenir: "NO BASELINE / Nothing was compared / This run says nothing about regressions" [§16]. Yeniden denemede geçen test "flaky" diye kalıcı kaydedilir [§17]. Zaman aşımı iki aşamalıdır: model hiç yanıt vermeye başlamadı mı, yoksa başladı ama bütçeyi mi aştı [§12.1]. Gözden geçirme hazırlık panosu geçerliliği içerik parmak iziyle hesaplar [GS-RQS §2–3].
- **ECC** (K). Araç etkinliği yolu: hook → JSONL üretici → içe aktarma → kayıt → zaman çizelgesi. Risk önerisi geriye dönük bir sınıflamadır, eylemden önceki izin değildir [ECC-CORE §7.1]. İlerleme durumunda "Date, target and evidence must remain attached to a status" [§8].
- **Hermes** (K). Görev, koşu, sahiplenme, oturum ve tur kimlikleri ayrıdır: "Bunları tek bir 'run' terimine sıkıştırmak hem acceptance hem maliyet açıklamasını bozar" [HA-S03 §4].
- **multi-agent-patterns** (kavramsal). Düzen (topoloji) değişiklikleri kalıcı durum olmalıdır: "Material current topology, outstanding branches, acceptance state, and next responsibility should be reconstructable after session loss" [MAP-A C7]. Yönlendirme kararları da yanlış olabilir; gerekçeleri ve sonuçları izlenmelidir [C9].
- **ECC yöntem vakası.** Değerlendirme birimi "an attributable change and its consequence, not a version counter" [ECC-MC §2].

### 5.2 Varyantlar ve ödünleşimler

- **Hesaplanan durum / beyan edilen durum.** gstack panosu kanıttan hesaplar; A003'teki STATE beyan eder.
- **İz / artefakt.** İz (trace) nasıl olduğunu, artefakt ne çıktığını gösterir; ikisinin gözlem sınırı farklıdır [TCL-H12 §1].
- **Sürekli / dönemsel.** ECC hook'larla sürekli ölçer; gstack retrosu dönemseldir.

### 5.3 Başarısızlıklar ve karşı örnekler

- **gstack, kısmi koşunun sızması.** `eval-list` ve `eval-summary` yarım birikimleri koşu gibi sayabiliyor; toplam koşu sayısı, maliyet, verimlilik ve flaky durumu kirlenebiliyor: "upstream artifact knows “partial” → some consumers preserve qualification → eval-list/summary flatten it into ordinary run representation" [GS-EVAL §15.1–15.2].
- **ECC, "sağlıklı" etiketi.** Hiç gözlemi olmayan ya da sürekli sıfır başarılı beceri "declining" olmadığı için sağlıklı sayılabiliyor [ECC-N08 §3]. İlerleme eşitlemesinin işaret kontrolleri canlı dış mutabakat değildir [ECC-CORE §8].
- **Hermes, önden ilerleyen sayaç.** Sayaç yürütmeden önce ilerliyor [HA-S03 §5].

### 5.4 Standart seviye kontrol listesi — gözlemlenebilirlik ve ilerleme

**GZ-1 — Alt ajan çalışma kaydı**
- *Amaç:* Her çağrı için bir satır: görev tanımı kimliği ve sürümü, rol, başlangıç HEAD'i, başlama ve bitiş, statü kodu, çıktı dosyası, dokunduğu dosyalar, token ve süre (ölçülemiyorsa "bilinmiyor"). Kaybolan ve yarım kalanlar dahil.
- *Yokluğunda:* Hangi sonucun hangi görev tanımından geldiği bilinmez (soy). Maliyet bilinmez (MK). Rol regresyonu için veri olmaz (RO-7). Kaybolan işler görünmez (YD-4).
- *Bedel:* Çağrı başına bir satır.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-EVAL §14; PB-01 §11; R06 §1 ("Record which version of the brief each subagent ran under"); R05 satır 27 (HEAD kaydı).

**GZ-2 — Soy ve karar izi**
- *Amaç:* Hangi karar hangi bulgudan, hangi bulgu hangi alt ajan çalışmasından geldi. A003 §3.5'teki "araştırma izi" bu zincirin bir halkasıdır.
- *Yokluğunda:* Bir bulgu geri çekilince etkilediği kararlar bulunamaz.
- *Bedel:* Karar kaydında bir alan.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* PB-01 §11 (alt ajan soy ağacı); MAP-A §15.2; A003 §3.5.

**GZ-3 — Hükmün nesneye bağlanması ve bayatlaması**
- *Amaç:* R05 satır 11–12 hükmü kesin hedefe bağlamayı verdi. Ek: STATE ya da pano, hükmün nesnesi değişince hükmü "bayat" gösterir.
- *Yokluğunda:* Eski sürüme verilmiş "tamam" yeni sürüm için de geçerli sayılır (MAP R4).
- *Bedel:* Hüküm kaydında nesne ve sürüm alanı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-RQS §3 ("validity is evaluated relative to the **object actually reviewed**"); MAP-A §13 R4.

**GZ-4 — Kanıta bağlı durum panosu**
- *Amaç:* STATE'teki her teslimat için durum (güncel, bayat, kısmi, bilinmiyor) kanıttan hesaplanır ya da en azından kanıta (dosya, SHA, gözden geçirme kaydı) bağlanır; beyan tek başına yetmez.
- *Yokluğunda:* STATE bir iddialar listesine dönüşür; yeni oturum yanlış yerden başlar.
- *Bedel:* Pano alanları; her kapanışta kontrol.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-CORE §8.2 ("Current standing often matters more than historical ceremony"); GS-RQS §2.

**GZ-5 — Kısmi, taban yok ve bilinmiyor durumları**
- *Amaç:* Yarım çalışma, karşılaştırılacak önceki olmaması ve ölçülemeyen değerler kendi adlarıyla görünür.
- *Yokluğunda:* Kısmi okuma tam, ilk ölçüm "istikrarlı", ölçülmeyen maliyet "sıfır" sayılır.
- *Bedel:* Üç etiket.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-EVAL §15–16; ECC-N32 §4.

**GZ-6 — İlerleme göstergeleri**
- *Amaç:* Kapanan soru ve değişen karar (R05 satır 26), Batu'ya yapılan hatırlatma sayısı (A003 §3.2), yeniden açılan ya da geri dönülen iş sayısı, aşamalar arası trend.
- *Yokluğunda:* "Hareket var, ilerleme yok" geç fark edilir; düzenin başarısı ölçülemez.
- *Bedel:* Aşama raporunda birkaç sayı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* A003 §3.2, §3.6; GS-DEP §19; ECC-MC §2.

**GZ-7 — Hatanın katmana göre sınıflanması**
- *Amaç:* Her olay ve ders bir katmana bağlanır: kaynak, bağlam, bellek, rol/yöntem, araç/ortam, model, yetki, düzenleme, gözlem.
- *Yokluğunda:* Her hata "daha fazla talimat" ile çözülmeye çalışılır (talimat birikimi); yanlış katman değiştirilir.
- *Bedel:* Olay kaydında bir alan.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* CMH-03 §20; CMH-04 §13; TCL-H12 §2 ("A diagnosis that implicates missing information may justify changing delivery rather than the model"); PB-01 §7.2.

**GZ-8 — Gözlem sınırının beyanı**
- *Amaç:* Kaydın neyi görmediği yazılıdır (alt ajanın ara adımları, kesilen araç çıktıları, VM'de kaybolanlar). "İz yok" = "olmadı" sayılmaz.
- *Yokluğunda:* Yokluk iddiaları yanlış kurulur.
- *Bedel:* Bir paragraf.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* TCL-H12 §1 (V3); PB-01 §11.

---

## 6. Maliyet ve kaynak yönetimi

### 6.1 Olgun sistemler ne yapıyor

- **ECC** (en ayrıntılı örnek; K + test kaynağı, testler koşulmadı). Birbirine bağlı ama farklı üç yol: (1) tahmini kullanım/maliyet: Stop hook'u transkripti okur, mesaj kimliğine göre tekrarları ayıklar, oturum toplamını `costs.jsonl`'a ekler; JavaScript köprüsü son kümülatif satırı alır; (2) bağlam doluluğu: durum satırı → köprü → izleyici → modele uyarı; (3) Rust kaynak denetimi: içe aktarma → oturum ölçüleri → bütçe aşımında gerçek durdurma [ECC-N32 §1–2]. Ayrım bilinçlidir: "a local estimate can support awareness without authorizing interruption, while a separate controller can enforce an explicit threshold" [§1]. Yeniden kullanılabilir mekanizmalar: mesaj düzeyinde tekrar ayıklama, kümülatif toplam sözleşmesine uyan tüketici, sel yapmayan teşhis izleri, bağımsız uyarı denetimleri, önem katmanları, yerel bağlam örneklemesi, saklanan bütçenin gerçekten uygulanması [§9].
- **gstack** (K+T). Doğruluk, verimlilik ve harcama güvenliği ayrı durumlardır: "correctness standing ≠ efficiency standing ≠ spend-safety standing". Araç çağrısı ve tur sayısındaki büyüme, aynı dalın önceki kesinleşmiş koşularıyla karşılaştırılır; kaçak altyapı hataları için yüksek sabit dolar tavanları vardır; aşım açık gerekçe ister ve kayda geçer [GS-EVAL §25]. Hızlı "gate" ile pahalı "periodic" katmanları ayrıdır [§7]. İç içe Codex incelemesi engellenir; gerekçe "nesting would be the same model reviewing itself at multiplied token cost", ve bir örnekte yaklaşık 15M token harcanmıştır [GS-MA §5.2]. Bellek bütçeleri [GS-MEM §10].
- **Hermes** (K). İnceleme çatalına 16 yineleme ve varsayılan 600.000 toplam girdi token bütçesi tanımlanır; uygulanma yolu okunmadı [HA-N02 §7]. İnceleme kullanımı ebeveynin yardımcı kullanım kaydına yazılır [§4]. Tur, amaç turu, döngü tik'i ve işçi çalışma süresi bütçeleri ayrı sayaçlardır [HA-S03 §4].
- **superpowers** (K). Muhasebede bilinen ve bilinmeyen kullanım ayrılır; bir alt toplamın fiyatlanması toplam harcamanın görüldüğü anlamına gelmez [SP-S01 §4]. "Choosing fewer artifacts is not proof of lower total cost, and choosing more subagents is not proof of better outcomes" [SP-S05 §8].
- **CMH** (L + A). Düzenek karmaşıklığı bir maliyettir: "**More harness ≠ better harness.**" Bileşen eklemek için "measurable failure class ve falsifiable expected value" gerekir [CMH-03 §16]. "Harness 20x maliyetle 2x quality veriyorsa task value bunu haklı çıkarıyor mu?" [§21.7].
- **Playbook** (tedarikçi iddiası). Paralel oturumlarda tavan insanın gözden geçirme kapasitesidir: "the human review capacity becomes the ceiling" [PB-01 §7.5].
- **Carbon sandbox videosu.** İnsan dikkati bir tasarım girdisidir; rutin onaylar önemli karara ayrılacak dikkati azaltır. %84 izin istemi azalması Anthropic'in kendi iç kullanım verisidir: "Bu %84 daha az güvenlik olayı, %84 risk azalması veya her kullanıcı için beklenen sonuç değildir" [TCL-S-RES §5]. Aday soru: "insan gerçekten karar vermesi gereken şeyi görüyor mu, yoksa ilerlemeyi açmak için tekrarlanan düğmelere mi basıyor?" [TCL-S-ASM §3]. — *kaynak diyor* · tedarikçi verisinin aktarımı + A.
- **multi-agent-patterns.** Özyinelemeli ajan patlamasına karşı: "explicit concurrency/depth/budget limits, spawn authority, task-value justification, cancellation and recovery" [MAP-A §13 R5].
- **ECC yöntem vakası.** Kendi uzun araştırması için: "No measured total time, token spend, error rate or alternative-method comparison is available here" [ECC-MC §2].

### 6.2 Varyantlar ve ödünleşimler

- **Uyarı / sert durdurma** [ECC-N32 §1, §8].
- **Kümülatif / artımlı satır.** Aynı veri iki tüketicide farklı anlam kazanabilir [ECC-N32 §2].
- **Tahmin / fatura.** ECC'nin aktardığı Claude Code durum satırı sözleşmesine göre yerel `total_cost_usd` "is itself a client-side estimate and may differ from billing" [ECC-N32 §5]. *Bulut oturumu için doğrulanmadı.*
- **Oturum bütçesi / genel bütçe.** ECC'nin genel bütçesi bitmiş oturumlar dahil bütün kayıtlı oturumları toplar; günlük ya da yalnız etkin oturum bütçesi değildir [ECC-N32 §3].
- **Makine kaynağı / insan dikkati** [TCL-S-ASM §3; PB-01 §7.5].

### 6.3 Başarısızlıklar ve karşı örnekler

- **ECC, kümülatif satırların toplanması.** Rust içe aktarıcısı kümülatif satırları toplar; son tahmin 7 iken 10 görünür ve 10'luk bütçe durdurmayı tetikleyebilir: "one producer's snapshot contract reaches a consumer that treats rows as independent increments" [ECC-N32 §2].
- **ECC, kimlik uyuşmazlığı.** Üreticiler oturum kimliğini farklı öncelikle seçiyor; maliyet ve araç etkinliği farklı oturumlara yazılabiliyor; eşleşmeyen satır hata vermeden hiçbir kaydı güncellemiyor [ECC-N32 §3].
- **ECC, ölçüm yokken sıfır.** Transkript okunamazsa satır "0" yazılır: "There is no separate completeness or availability field distinguishing this from observed zero usage" [ECC-N32 §4].
- **ECC, model atfının kaybı.** Birden çok model içeren transkriptte son modelin fiyatı bütün mesajlara uygulanır [ECC-N32 §5].
- **ECC, uyarı kaydı ile teslimin karışması.** Uyarı durumu, uyarı teslim edilmeden kaydedilir; teslim başarısızsa aynı uyarı bastırılabilir: "Record-of-emission preparation and acknowledged receipt are not the same operation" [ECC-N32 §8].
- **gstack, iç içe inceleme.** Yaklaşık 15M token [GS-MA §5.2].
- **EXP-007'nin kendisi.** A003 §6 iki araştırma turunda yaklaşık 4 milyon token harcandığını ve "Kontrolün ağırlığı riske göre ayarlanmazsa haftalık limit yetmez" dediğini yazıyor; bunu yönetecek bir mekanizma önermiyor (*gözledim*).

### 6.4 Standart seviye kontrol listesi — maliyet ve kaynak

**MK-1 — Ölçüm sözleşmesi**
- *Amaç:* Ne ölçüldüğü (alt ajan başına token ve süre), ölçümün kaynağı, satırın kümülatif mi artımlı mı olduğu açık olsun. Ölçülemeyen değer "bilinmiyor" diye yazılır. Tahmin ile fatura ayrılır.
- *Yokluğunda:* Bütçe kararları yanlış sayıya dayanır (ECC'deki yanlış durdurma). Kontrollerin maliyet-değer hesabı yapılamaz (MK-5).
- *Bedel:* Kayıt başına iki alan; ölçüm kaynağını bulma (bkz. §10).
- *Gerçekten gereksiz:* Maliyetin önemsiz olduğu iş. EXP-007'de haftalık limit gerçek bir kısıt (A003 §6).
- *Dayanak:* ECC-N32 §2, §4–5; SP-S01 §4.

**MK-2 — Bütçe kapsamları**
- *Amaç:* Alt ajan başına, iş kalemi başına, aşama başına ve haftalık plan limiti için ayrı bütçe; hangi sayacın hangi kapsamı ölçtüğü yazılı.
- *Yokluğunda:* Tek bir "run" sayacı her şeyi karıştırır [HA-S03 §4]; aşama bütçesinin aşıldığı fark edilmez.
- *Bedel:* Plan dosyasında bütçe alanları.
- *Gerçekten gereksiz:* Tek kalemli iş.
- *Dayanak:* HA-S03 §4; ECC-N32 §3.

**MK-3 — Uyarı ile sert durdurmanın ayrılması**
- *Amaç:* Uyarı koordinatörün kararına bırakılır; durdurma ya da park eşik aşımında zorunludur. İkisi aynı ölçüyü aynı sözleşmeyle okur.
- *Yokluğunda:* Ya her aşım işi durdurur (verim) ya da hiçbir aşım durdurmaz (limit tükenir, yarım iş kaybolur).
- *Bedel:* Eşik tanımları.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* ECC-N32 §1, §8; GS-EVAL §25.

**MK-4 — Kaçak korumaları**
- *Amaç:* Paralel alt ajan üst sınırı; aynı görev tanımının değiştirilmeden tekrar gönderilmemesi (R05 satır 4); alt ajan başına tur ya da süre sınırı. İç içe alt ajan bu ortamda zaten kapalı [R01 satır 6].
- *Yokluğunda:* Yayılma patlaması (MAP R5); 15M token'lık iç içe inceleme türü olaylar.
- *Bedel:* Birkaç kural satırı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* GS-MA §5.2; MAP-A §13 R5; GS-EVAL §12.

**MK-5 — Maliyet-değer gerekçesi**
- *Amaç:* Her kontrol, rol ve ritim için hangi hata sınıfını önlediği ve yaklaşık maliyeti yazılı. Değer göstermeyen bileşen kaldırılabilir.
- *Yokluğunda:* Ya tören birikir (maliyet, Batu'nun zamanı) ya da gerekli bir kontrol "pahalı" diye keyfi atılır; bu, Batu'nun "yeterli seviye" eleştirisinin tam karşılığıdır.
- *Bedel:* Bileşen başına bir satır.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* CMH-03 §16, §21.7; SP-S05 §8.

**MK-6 — Verimlilik karşılaştırması**
- *Amaç:* Benzer iş kalemlerinde token ve süre büyümesi öncekiyle karşılaştırılır; önceki yoksa "taban yok" yazılır.
- *Yokluğunda:* Maliyet artışı fark edilmez; ilk ölçüm "normal" sanılır.
- *Bedel:* Aşama raporunda bir tablo.
- *Gerçekten gereksiz:* Tek aşamalı iş.
- *Dayanak:* GS-EVAL §16.1 ("First-run grace is therefore **absence of comparative evidence**, not proof of efficiency"), §25.

**MK-7 — Koordinatör bağlamı bir kaynaktır**
- *Amaç:* BA-5'in maliyet yüzü: koordinatörün bağlam kullanımı izlenir; ağır okuma alt ajanlara verilir; koordinatör bağlamında uzun araç çıktısı tutulmaz.
- *Yokluğunda:* Sık sıkıştırma ve karar kaybı; ana oturum şişer [SP-S03 §6].
- *Bedel:* İzleme alışkanlığı.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* SP-S03 §6; A003 §3.9; R01 satır 539–546.

**MK-8 — İnsan dikkati bütçesi**
- *Amaç:* Batu'ya giden soru, onay ve bilgilendirmenin sayısı ve biçimi yönetilir: biriktirme, öneriyle birlikte sunma, rutin onayları kaldırma; Batu'nun gerçekten karar vermesi gereken şeyi görmesi.
- *Yokluğunda:* Onay yorgunluğu; Batu'nun gizli koordinatöre dönüşmesi (MAP-A §13 R6); kararların özensiz onayı.
- *Bedel:* Bir soru kuyruğu.
- *Gerçekten gereksiz:* Yok.
- *Dayanak:* TCL-S-ASM §3; PB-01 §7.5; MAP-A §13 R6; A003 §3.9.

**MK-9 — Rol başına model ve çaba seçimi**
- *Amaç:* Mekanik roller (ör. biçim denetimi, dar okuma) daha ucuz model ya da düşük çabayla; yargı gerektiren roller (karşı-okuma, sentez) daha güçlü modelle çalışır; tıkanmada yükseltme kuralı vardır.
- *Yokluğunda:* Her şey en pahalı modelle çalışır ve limit erken biter; ya da zor iş zayıf modelle bozulur.
- *Bedel:* Rol dosyasında model alanı; seçimin sınanması.
- *Gerçekten gereksiz:* Tek model mevcutsa.
- *Dayanak:* GS-EVAL §19.1; SP-U03 §4; R01 satır 72 (`model` alanı).

---

## 7. A003 v0 ile karşılaştırma (özellikle istenen 4)

A003 §1–§7 okundu (*gözledim*). Seviye ölçeği: **yok** (bileşen kurulmamış), **yeterli** (bir çekirdek var, standart listenin çoğu eksik), **standarda yakın** (listenin çoğu var). "Eksik" sütunundaki kodlar bu notun kontrol listesi maddeleridir.

| Alt sistem | A003'te kurulan | Seviye | Eksik |
|---|---|---|---|
| Bağlam | Okuma yolu: giriş dosyası → soruya özgü harita → özgün bölüm (§3.4). Ana oturum az okur, okumayı alt ajanlar yapar (§3.9). Görev tanımında zorunlu kaynaklar ve kanıt dili (§3.3 madde 5, 7). Karşı-okuyucu üreticinin gerekçesini görmez (§3.3). "Repoda okunan bir talimat yetki taşımaz" (§3.5). Soğuk başlangıç testi (§6). | Yeterli; okuma yolu standarda yakın | BA-1 kısmi (güven sınıfları tek bir cümle); BA-3 yok; BA-4 yok (her şey görev tanımında); BA-5 yok; BA-6 yok ("yeniden yükleme ucuz olur" varsayımı dışında); BA-7 kısmi (kanıt etiketleri); BA-9 kısmi (bir kez, P0 sonunda) |
| Bellek | "Repo bellektir; konuşma bellek değildir" (§3.4). Okuma kaydı (§3.4). DECISIONS (§5). Batu'nun sözleri birebir (§2). A–B–C ayrımı (§3.1). Ders kaydı ve "doğrulanmadı" statüsü (§3.10). "Bir bilgi tek yerde durur" (§3.9). | Yeterli: depolama var, yaşam döngüsü yok | BE-1 kısmi; BE-2 kısmi (A–B–C yalnız Batu'nun sözü için); BE-3 kısmi (yalnız dersler); BE-4, BE-5, BE-6, BE-7, BE-8, BE-9 yok; BE-10 yok (rol ve aşama kapsamı); BE-11 kısmi (commit var, geri okuma yok); BE-12 yok |
| Kalıcı roller | Beş geçici alt ajan türü (§3.2). Dokuz alanlı görev tanımı (§3.3). "Bir görev kalıbı üç kez aynı şekilde tekrarlanınca kalıcı bir ajan tanımına dönüşür, önce değil" (§3.3). DevOS rolleriyle karıştırmama (§3.2). | Yok; bilinçli ertelendi ve Batu U004'te reddetti | RO-1 … RO-11'in tamamı; en yük taşıyanlar RO-3 (sabit/değişken ayrımı), RO-5 (rol belleği), RO-6 (değişiklik yolu), RO-7 (regresyon seti), RO-11 (koordinatör rolü) |
| Yaşam döngüsü | Aşama haritası; iş kalemi alanları ve statüler (§3.6). Revizyon tetikleri ve üç tur sınırı (§3.7). Kontrol noktaları: kalemden sonra kayıt, aşama raporu, P4 durağı (§3.6). İletişim ritmi (§3.9). Yeni oturum okuma sırası (§3.9). P0 pilot yolu (§5). | İş kalemi ve aşama düzeyinde yeterli; oturum düzeyinde büyük ölçüde yok | YD-1 kısmi (yöntemin yüklendiği doğrulanmıyor); YD-2 (bağlam eşiği kaydı), YD-3 (kapanış alanları), YD-4 yok; YD-5 kısmi ("kontrolün ağırlığı risk ve geri alınabilirlikle orantılıdır" ilkesi var, rota tanımı yok); YD-6 yok; YD-7 kısmi (aşama raporu var, retro biçimi ve trend yok); YD-8, YD-9 yok |
| Gözlemlenebilirlik | İlerlemenin ölçüsü ve "hareket var, ilerleme yok" alarmı (§3.6). Batu'ya yapılan her hatırlatmanın kusur olarak kaydı (§3.2). Okuma kaydı (§3.4). Araştırma izi (§3.5). Tamamlanma katları (§3.8). | Yeterli; okuma kaydı ve hatırlatma sayısı standarda yakın ve özgün | GZ-1 yok; GZ-2 kısmi; GZ-3 kısmi (R05'te var); GZ-4 yok (STATE beyana dayalı); GZ-5, GZ-7, GZ-8 yok |
| Maliyet | Risk cümlesi: yaklaşık 4 milyon token ve "Kontrolün ağırlığı riske göre ayarlanmazsa haftalık limit yetmez" (§6). Batu'ya yalnız belirli durumlarda gelme ve soruları biriktirme (§3.6 karar katmanları, §3.9). | Yok (yalnız risk tanıma); insan dikkati kısmen | MK-1 … MK-7 ve MK-9 yok; MK-8 kısmi |

**v0'da korunmaya değer olanlar (*çıkarım*).** Bazı v0 bileşenleri studies'teki olgun örneklerle aynı ya da onlardan daha açık:
- okuma kaydının alanları (kaynak, sürüm, ne kadarı okundu, hangi soru için, düşüncede neyi değiştirdi) [A003 §3.4];
- hatırlatma sayısını düzenin başarı ölçüsü yapmak [§3.2]; studies'te bunun karşılığı yok;
- karşı-okuyucudan üreticinin gerekçesini saklamak [§3.3]; gstack CSO doğrulayıcısıyla aynı desen [GS-MA §7];
- aynı görevi aynı tanımla ikinci kez göndermemek [§3.3]; superpowers'ın "unchanged retry" yasağıyla aynı (R05 satır 4);
- soğuk başlangıç testi [§6]; ECC yöntem vakasının eksikliğini söylediği "conversation-independent" sınamanın karşılığı [ECC-MC §6].

**En yük taşıyan yapısal fark (*çıkarım*).** v0 rol, bağlam ve bellek kararlarının neredeyse hepsini ya her görev tanımının içine (§3.3'ün dokuz alanı) ya da koordinatörün kafasına koymuştu. Olgun sistemler bunları ayırır: sabit rol sözleşmesi bir dosyada (gstack becerisi, superpowers rol şablonu, ECC agent tanımı), rol başına bellek alt kümesi bir kuralla (gstack), değişken kısım görev tanımında (superpowers). Batu'nun "her seferinde yeniden alt ajana rol biçmek doğru değil" eleştirisi tam bu ayrımın yokluğuna denk düşer. İkinci fark: v0'ın belleği yaşam döngüsü olmayan bir depodur; üçüncü fark: v0'da oturum düzeyinde ritim yoktur, oysa bu ortamda VM geri alınması ve %80 sıkıştırma olağan olaylardır.

**Batu'nun araba benzetmesiyle eşleme (*çıkarım*).** Hız = paralel alt ajan araştırması (A003 §3.2); fren = bütçe kapsamları, uyarı/durdurma ve kaçak korumaları (MK-2, MK-3, MK-4). Emniyet kemeri = karşı-okuma (A003 §3.3); hava yastığı = kesinti protokolü ve yazma sonrası geri okuma (YD-4, BE-11); engel tanıyan radar = alt ajan çalışma kaydı ve kanıta bağlı durum panosu (GZ-1, GZ-4); sürücünün gözünü izleyen sistem = koordinatör bağlam bütçesi ve sıkıştırma protokolü (BA-5, BA-6, MK-7); yorgunluk uyarısı = bakım ritmi ve bağlam doluluğu (BE-12, YD-9, BA-5). Konfor = Batu'nun dikkat bütçesi (MK-8) ve rol dosyaları sayesinde kısalan görev tanımları (RO-3); bunlar da güvenliğin parçasıdır, çünkü yorgun onay ve şişkin görev tanımı hata üretir.

---

## 8. Alt sistemler arası en yük taşıyan bağlar

Tam etkileşim matrisi R11'in konusudur. Burada yalnız studies'te kanıtı olan bağlar (*çıkarım*, dayanaklarıyla):

1. **Rol belleği ↔ bellek yaşam döngüsü ↔ bağlam paketi.** Rol belleği (RO-5) ancak yerine koyma, tazelik ve unutma (BE-4, BE-6, BE-8) ile güvenlidir; yoksa eski dersler her pakete girer (BA-4) ve bağlantılı hata üretir [TCL-H11 §4 P1]. ECC içgüdüleri incelemesiz bağlama giriyor [ECC-N07 §6]; gstack çıkarım derslerini zamanla zayıflatıyor [GS-MEM §5].
2. **Bağlam bütçesi ↔ sıkıştırma ↔ oturum ritmi ↔ maliyet.** Koordinatör bağlamı dolunca sıkıştırma, sıkıştırmada kısıt ve karar kaybı, sonra yeniden okuma maliyeti gelir (BA-5, BA-6, YD-2, YD-3, MK-7) [R01 satır 539–546, 838; TCL-H08 §4].
3. **Niteleyici kaybı iki alt sistemde aynı hata sınıfıdır.** gstack'te bellekte bayat işaretinin, değerlendirmede "kısmi" işaretinin kaybı [GS-MEM §12; GS-EVAL §15]; gstack bunu tekrar eden kusur sınıfı sayar [GS-CORE §11 F1]. BA-7 ve GZ-5 aynı kuralın iki yüzüdür.
4. **Rol yürütme semantiği ↔ ortam değişikliği ritmi.** Platform varsayılanı değişince örtük semantik bozulur (RO-8, YD-8) [GS-MA §3].
5. **Maliyet ölçümü ↔ gözlem kaydı ↔ sert durdurma.** Ölçüm sözleşmesi hatası durdurmayı yanlış tetikler (MK-1, MK-3, GZ-1) [ECC-N32 §2].
6. **Rol regresyonu ↔ çalışma kaydı ↔ maliyet-değer.** Regresyon (RO-7) çalışma kaydı (GZ-1) olmadan yapılamaz, maliyeti ölçülmeden (MK-5) gerekçelendirilemez.
7. **İnsan dikkati ↔ kabul adımları.** Her ders ve rol değişikliği Batu'ya giderse onay yorgunluğu olur; hiçbiri gitmezse modelce kabul olur (MK-8, BE-3, RO-6). Yetki katmanları R05 satır 21–23'te.
8. **"Değişiklik ≠ kullanım ≠ fayda" üç alt sistemi keser:** rol değişikliği (RO-6), bellek sağlığı (BE-12), ilerleme göstergeleri (GZ-6) [HA-S01 §4; SP-CORE §6; TCL-H17 §3].

---

## 9. Yalnız META'sı okunan paketler: hangi soruları cevaplayacaklar

Dokuzunun durumu da "PLANNED / RESEARCH NOT STARTED"; META'lardaki maddeler bulgu değil, ön niteleme sinyalidir (*kaynak diyor*). Hiçbiri kanıt olarak kullanılamaz.

| Paket | Nesnesi | Bizim alt sistemlerimiz için cevaplayacağı sorular | En çok hangi maddeyi sınar |
|---|---|---|---|
| `llm-wiki` | Karpathy'nin LLM'in bakımını yaptığı, kaynağa bağlı wiki fikir notu (ham kaynak / üretilmiş wiki / şema; ingest, query, lint) | Model tarafından sürdürülen bilgi katmanında güncelleme ve çelişki nasıl yönetilir, kaynaktan iddiaya izlenebilirlik nasıl korunur, üretilmiş değişiklik nasıl doğrulanır, bakım yükü nedir, bilgi sürekliliği ile güncel iş/yetki durumu nasıl ayrılır? | BE-4, BE-7, BE-12, BA-7 |
| `openviking` | Kaynak/bellek/beceriyi tek sanal dosya sisteminde birleştiren bağlam veritabanı; L0/L1/L2 kademeli yükleme | Kademeli yüklemede özetler neyi kaybeder; üretilmiş özetin bayatlığını kendi duyurması (`pending_child_changes`) nasıl çalışır; oturumdan belleğe çıkarımda atla/oluştur/birleştir/sil kararları ve `memory_diff.json` denetim kaydı ne kadar güvenilir; okunabilir ile aranabilir içerik nasıl hizalanır? | BA-2, BA-7, BE-4, BE-11 |
| `ai-memory` | Git sürümlü Markdown'u gerçeğin kaynağı, dizinleri türetilmiş sayan ajanlar arası uzun süreli bellek | Yakalama, arındırma, birleştirme, geri çağırma, devir, pekiştirme, çürüme ve unutma nasıl yönetilir; "current instructions and checkout state remain authoritative over remembered material" ilkesi nasıl uygulanır; sahiplikli devirler ve çok kullanıcı ayrımı nasıl çalışır? | BE-1, BE-8, BE-11, YD-3, YD-4 |
| `agentmemory` | Birden çok kodlama ajanı ve MCP istemcisi için kalıcı bellek | Heterojen ajanlar arasında yakalama, saklama, geri çağırma ve güncelleme nasıl yapılır; yetkili durum ile türetilmiş temsil nasıl ayrılır; köken, tazelik, saklama, çatışma ve arıza kurtarma nasıl ele alınır? | BE-1, BE-5, BE-7 |
| `agent-memory-providers` | Bellek sağlayıcısı (kalıcılık altyapısı) ile bellek yönetimi arasındaki sınır | Sağlayıcının asgari sözleşmesi nedir; zamansal geçerlilik, yerine koyma, köken ve yetki nerede yaşamalı; altyapı düzeyinde silme ile politika düzeyinde unutma nasıl ayrılır; "no memory exists" ile "retrieval failed" ayırt edilebilir mi? | BE-8, BE-11, BA-8 |
| `context-mode` | Araç çıktısını modelin bağlamı dışına yönlendiren, hesabı dışarıda yapan, oturum olaylarından sıkıştırma sonrası durumu yeniden kuran katman | Hangi bilgi modelin bağlamına girmeli, hangisi dışarıda hesaplanmalı; sıkıştırma/devamda etkin dosyalar, hatalar, kararlar, kurallar, görevler, alt ajanlar, roller ve hedefler nasıl yeniden kurulur; hostlar arasında denetim eşdeğer mi? | BA-5, BA-6, YD-2, YD-3, MK-7 |
| `cli-continues` | Kodlama oturumlarını araçlar arasında sürdüren devir aracı | Devam bir oturum çevirisi mi, iş durumu devri mi, ikisinin bileşimi mi; üretilen devir belgesinde ne kaybolur; güncel repo durumu tarihsel konuşma durumuyla nasıl uzlaştırılır? | YD-1, YD-3, YD-4, BA-6 |
| `mattpocock-skills` | Küçük, birleştirilebilir mühendislik becerileri; kullanıcının ve modelin çağırdığı beceri ayrımı | İş akışı başlatma yetkisi insanda nasıl kalır; CONTEXT.md alan dili bağlamı küçültür mü; issue takibine dayalı çok oturumlu "wayfinder" (hedef, karar biletleri, sınır, belirsizlik alanı) nasıl çalışır; retrospektif, tekrarlanan hatayı gezinme, bilgi erişimi, gözden geçiren kuralı ya da mekanik kontrole nasıl çevirir? | RO-1, RO-3, RO-4, YD-5, YD-7 |
| `deepseek-harness` | "Her şey eklenti" düzenekli ajan çalışma zamanı | Salt-eklemeli oturum/olay kaydından modelin gördüğü geçmiş nasıl yeniden kurulur; yetenek ve politika dikişleri nasıl ayrılır; sürdürülebilir alt ajanların yaşam döngüsü ve repo içi ajan geliştirme disiplini nasıldır? | GZ-1, GZ-2, YD-4, RO-8 |

Bu dokuz paketten, bu notun kontrol listelerinde en çok boşluk bırakan sorulara (sıkıştırma sonrası durum kurma, bellek yaşam döngüsünün denetim kaydı, çok oturumlu iş sınırı) doğrudan dokunanlar `context-mode`, `openviking` ve `mattpocock-skills`'tir (*çıkarım*).

---

## 10. Açık sorular

1. **Rol belleğinin yeri.** Claude Code'un `memory: project` alanı (`.claude/agent-memory/<ad>/`) bulut oturumunda yüklenip commit'lenebiliyor mu? R01 bunu "documented_generic_unclear_cloud" diye işaretledi [R01 satır 80]. Olmuyorsa rol belleği EXP-007 içinde, rol dosyasının açıkça okuttuğu bir dosyada tutulmalı. `.claude/` değişiklikleri Batu onayı ister (A-04).
2. **Alt ajan maliyetinin ölçüm kaynağı.** Alt ajan başına token ve süre bu ortamda nereden okunur (Agent aracının sonuç bilgisi, OpenTelemetry, başka bir yol)? Bu notun kaynakları cevap vermiyor; R07 ya da R01'e bakılmalı. *Bilinmiyor.*
3. **Hook'suz ritim.** Repo `settings.json` hook'ları yalnız tek repolu oturumda geçerli [R01 satır 527] ve Batu onayı ister. Hook kurulmazsa YD ve GZ maddeleri talimat düzeyinde kalır; hangilerinin mekanikleştirilmesi (betik, kontrol listesi, commit öncesi denetim) gerektiği METHOD v1'de karar ister.
4. **Regresyon setinin maliyeti.** Studies rol ya da yapılandırma regresyonunun gerçek maliyetini ölçmedi (ECC-MC §2). RO-7'nin hangi sıklıkla ve kaç görevle koşacağı, haftalık limit içinde denenerek belirlenmeli.
5. **Koordinatör bağlamının ölçülmesi.** Koordinatörün bağlam doluluğunu bu ortamda görmenin güvenilir yolu nedir? R01'e göre `/compact` ve `/context` bulutta çalışıyor [R01 satır 539]; alt ajan içinden ve otomatik izleme için durum bilinmiyor.
6. **Rol belleği ile EXP-007 ders kaydının ilişkisi.** R05 satır 18–19'daki ders kaydı ile RO-5'teki rol belleği aynı yerde mi tutulmalı, ayrı mı? Kapsam ayrımı (BE-10) bu kararı etkiler.
7. **Bu standartların DevOS'a taşınması.** Bu not EXP-007'nin kendi işleyişine bakıyor; aynı maddelerin DevOS rol tasarımına (P2) girdi olup olmayacağı ayrı bir karardır (R06: süreç üzerindeki iş ile ürün üzerindeki iş ayrı tutulur).
8. **Mekanik denetim sınırı.** Yerine koyma, tazelik ve niteleyici koruma kuralları elle mi (koordinatör disiplini) yoksa basit bir doğrulama betiğiyle mi denetlenecek? Studies mekanikleştirmeyi öneriyor (gstack değişmez kuralları, OpenAI belge bakımı) ama EXP-007'deki maliyetini göstermiyor.
9. **Paket şablonlarının koordinatör bağlamındaki payı.** Rol dosyaları ve paketler koordinatör bağlamının ne kadarını tüketir? superpowers'taki #2203 raporu benzeri bir etki olabilir [SP-S03 §6]; ölçülmedi.

---

## 11. Bu not neyi kanıtlamıyor

- **Etkinlik.** Hiçbir mekanizmanın EXP-007'de ya da genel olarak işe yaradığını kanıtlamıyor. Studies canlı ajanlarla etkinlik ölçmedi; R05 aynı uyarıyı yapıyor.
- **"Standart" ilanı.** Kontrol listeleri benim sentezimdir (*çıkarım*). Hiçbir study bir "standart" ilan etmiyor. Maddeler olgun sistemlerde tekrar eden bileşenlerden ya da yokluğunun başarısızlık ürettiği gösterilen yerlerden türetildi. Bazı maddeler yalnız bir sistemde görülüyor: bütçe testleri (gstack), ayrıntılı maliyet yolları (ECC), rol başına model seçimi (gstack). Bunlar "tekrar eden bileşen" değil, "yokluğunun bedeli gösterilmiş bileşen"dir.
- **Bağımsız teyit.** Studies büyük ölçüde aynı asistanın sentezleridir; aralarındaki uyum bağımsız doğrulama değildir. Sahip kabulü (superpowers) kanıt gücünü artırmaz.
- **Güncellik.** Sürümler sabittir: gstack v1.79/1.80, Hermes 0.21.0, superpowers 6.3.0, ECC `8321021`. Güncel ürün davranışı değildir.
- **Claude Code davranışı.** Buradaki Claude Code iddiaları, tedarikçi belgelerinin studies içindeki aktarımıdır. Güncel doğrulukları ve bulut oturumundaki geçerlilikleri R01 ve R07'nin konusudur; yukarıda bulut durumu belirtilmeyen yerlerde *bilinmiyor* sayılmalıdır.
- **Tam okuma.** §0.4'te kısmi okunan dosyaların okunmayan bölümleri kararı değiştirebilecek bilgi içerebilir. En büyük boşluklar: gstack'in okunmayan sekiz sentezi, superpowers S04/S06, ECC'nin 56 notundan 48'i, Hermes'in 30 notundan 23'ü.
- **Maliyet.** Hiçbir study toplam maliyet ya da hata paydası ölçmedi (ECC-MC §2). Bileşen "bedel"leri nitel tahmindir.
- **Bütünsel etkileşim.** §8 yalnız studies'te kanıtı olan bağları listeler; tam etkileşim matrisi R11'dedir.
