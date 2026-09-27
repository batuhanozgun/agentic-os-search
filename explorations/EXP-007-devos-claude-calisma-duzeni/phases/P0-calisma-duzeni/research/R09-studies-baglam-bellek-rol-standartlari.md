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
| gstack | META, INDEX, CORE, memory-learnings sentezi | STATE (ilk kısım); multi-agent (özet, §1, §5–7, §10–15); planning-spec (özet, §1–4, §6–8); review-qa-ship (§2–3, başlıklar); testing-eval (§7, §12–17, §19, §25, başlıklar); deploy-retro (§19–21, başlıklar); inventory/STRUCTURE (§1–2) | diğer 6 sentez, CLOSURE-AUDIT, METHOD, SOURCE-LEDGER, revalidation |
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
| Bilinçli saklanan | önceki aşama bulguları; tarayıcının gerekçesi [GS-MA §6, §7] | bütün plan ve geçmiş; beklenen önem derecesi [SP-S03 §3] | sırlar; talimat benzeri metin [ECC-N39 §7] | eski araç sonuç gövdeleri, yardımcı model özetinde [HA-N02 §2] |
| Bütçe | varlık, beceri ve talimat bütçeleri; testli [GS-MEM §10] | açık bütçe yok; nitel "dar bağlam" | birleşik bağlam karakter sınırı; bağlam doluluk uyarısı [ECC-N07 §6; ECC-N32 §6] | inceleme çatalı: 16 yineleme, 600.000 girdi token [HA-N02 §7] |
| Kademeli yükleme | STOP+Read ile istek üzerine bölüm [GS-PLAN §6] | plan → görev → gereken kaynak [SP-S03 §2–3] | /plan'da PRD yalnız referans [ECC-N39 §4] | araç yanıtıyla canlı durum [TCL-M-RES §7] |

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

<!-- R09-DEVAM -->
