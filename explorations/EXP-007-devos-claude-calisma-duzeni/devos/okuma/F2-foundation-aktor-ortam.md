# F2 — Foundation 03: Aktörler ve Ortam zeminleri → DevOS mekanizmaları

Okuyucu: F2 · Tarih: 2026-09-27 · Dal: `claude/hopeful-pascal-7bekcd` · Kapsam kökü: `research/soul-foundations/03_ground-deepening/grounds/actors` ve `.../grounds/environment` · Kanıt etiketleri: **[kaynak diyor]**, **[gözledim]**, **[çıkarım]**, **[bilinmiyor]**. Yol kısaltmaları §0.3'te.

## DevOS için en önemli çıkarımlar

1. Kapsamın tamamı baştan sona okundu: 224 dosya (Aktörler 16, Ortam 208; ~1,28 MB). Kapsam bölünmesi gerekmedi. [gözledim]
2. Bu iki zemin mekanizma vermez; "birbirine karıştırma" yasakları (≠ kuralları) verir. DevOS'ta her yük taşıyan ayrım iki şeye dönüşmeli: kayıtta ayrı bir alan ve bir zorlama ya da algılama noktası. Zeminler klasör, servis ya da ajan olmaz (A/A6 §9; E/README; Foundation README). [kaynak diyor + çıkarım]
3. En ağır aktör sonucu `reachable effect power != legitimate authority` (A/STATE). DevOS'ta yetki üç ayrı katmandır: normatif yetki kaydı → teknik zorlama (settings izinleri, PreToolUse) → algılama (Stop/commit denetimi). Her yasak etki için alternatif yollar listelenip kapatılır: Bash `git push`, `gh`, MCP GitHub araçları, alt ajan. Tek izin kontrolü yetmez (A/A3 §2.3; A/DEFERRED §4). [çıkarım]
4. Foundation, Claude'u adıyla anıyor: CLAUDE.md, Skills, rules = modelin gördüğü tavsiye (bilgi); Hooks, settings, permissions, sandbox, network = zorlama (A/A3 §2.5). Yük taşıyan her kural için "tavsiye / zorlanan / algılanan" envanteri tutulmalı. [kaynak diyor + çıkarım]
5. performer ≠ decider ≠ authorizer ≠ principal ≠ accountable; `Work acceptance state != authority to accept`; "human approved → therefore technically verified" yanlış (A/synthesis §12; A/DEFERRED §8). İş kaydında konumlar ayrı alanlardır. Batu = asıl (principal) ve teslim kabulü; teknik doğrulama DevOS içindeki bağımsız doğrulayıcıdadır (K-015 ile uyumlu). [çıkarım]
6. Doğrulayıcı etiketle değil bağımsızlık koşuluyla tanımlanır: "role name does not establish epistemic independence or authority"; çok ajanın aynı şeyi demesi bağımsız kanıt değil; aynı model incelemesi bağımsız değil (A/A3 §3.2–3.3; A/A5). Doğrulama raporu bağımsızlık düzeyini yazar. [kaynak diyor + çıkarım]
7. Rol ≠ oturum: "fresh process can occupy a continuing role" (A/A3 §4.3). İş role bağlanır; oturumlar o rolün "işgalcisi" olarak listelenir; VM süresi dolunca taze oturum repo kaydından devam eder. [çıkarım]
8. Sürekli sorumluluk ≠ o anki iş (A/A2 §7). Her kalıcı varlık için bir kalıcı sorumlu (steward) kaydı ve tetik (oturum başı, rutin) tutulur; tetik iş kaydı üretir. [çıkarım]
9. Batu'nun katılımı yalnız meşru değer/yetki kapısı olmalı, "hidden human orchestration" olmamalı (A/A3 §3.4). Batu etkileşimleri türüyle kaydedilir; "aktarma/koordinasyon/teknik soru" türü DevOS için iyileştirme işi açar. [çıkarım]
10. Ortam: gerçek ≠ şartname ≠ gözlem ≠ model ≠ kayıt; "`current` is not synonymous with `most recently recorded`" (E/DS F09). STATE iddiaları zaman ve kaynak komutu taşır; SessionStart kancası gerçeği yeniden gözler, farkı bağlama basar. [kaynak diyor + çıkarım]
11. "Work closure/status ≠ actual domain effect" (E/synthesis §4). Kapanışta üç ayrı alan: iş bitti / gerçek etki kanıtı / kabul. Stop kancası kanıtsız "tamamlandı"yı durdurur. [çıkarım]
12. Çalışma koşulları: `resource exists ≠ accessible ≠ available ≠ sufficient`; "Work is blocked" (iş durumu) ile "required service is unavailable" (koşul) ayrı (E/WC). İş kaydı gerekli koşulları bildirir, oturum başı yoklama karşılaştırır. Bulut gerçekleri (VM süresi, boşta geri alma, proxy, plugin, kapalı Mac, önbellekli setup) koşul olarak gözlenir, varsayılmaz. [çıkarım]
13. Ölçüt-göreli durum: doğru özellik + yanlış/eski/uygulanamaz ölçüt = yanlış durum; değerlendirme kararı ≠ gerçek durum (NIST; E/CRS). "done/ready/accepted" tek bir status alanı olmaz: ölçüt+sürüm, taşıyıcı (commit), yöntem, değerlendiren, zaman; birden çok ölçüt aynı anda. [çıkarım]
14. Eksiklik sözlüğü zorunlu: `absent ≠ not observed ≠ unknown ≠ field missing ≠ not applicable ≠ outside scope`; alanın kendi "Pending"i ≠ bizim belirsizliğimiz (E/DC F04; E/CRS F05). [kaynak diyor]
15. Rol değişimi: aynı şey bir iş için hedef, başka iş için koşuldur (CI örneği, E/F07). DevOS kendi kancalarını, ayarlarını, yetki kaydını değiştirirken bunlar hem hedef hem koşuldur → ayrı özerklik kademesi; doğrulama, değişikliğin yüklendiği gözlenen yeni oturumda. [çıkarım]
16. Dinamik: repo odak iş olmadan da değişir (başka oturum, Batu, alt ajan). Oturum başında ve push öncesi fetch + karşılaştırma; istenen/gerçek uzlaştırma döngüsü (Kubernetes denetleyici örneği, E/DD F04). [çıkarım]
17. "`Condition X existed when Work failed` does not establish `X caused the failure`" (E/WC DEFERRED §8). Ders ve öğrenme kayıtlarında "kanıt türü" alanı zorunlu. [kaynak diyor + çıkarım]
18. Foundation'ın kendi yönteminden alınacaklar: önceden dondurulmuş yanlışlayıcılar ve başarı ölçütleri, simetrik sonuç seçenekleri, açık yeniden açma koşulları, "OPEN-QUESTIONS iş kuyruğu değildir", eski belgeye "sonradan düzeltildi" notu, tek aktif düğüm, bağımsızlık eksikliğinin açık etiketi. [gözledim]
19. Ders: 8 düğümde 17 yönlendirici dosya (INDEX/KEY/FINDINGS-MAP/CURRENT-SURFACES) hâlâ "awaiting user evaluation" diyor, STATE ise "accepted". Kök neden: değişken durumun birden çok yüzeye kopyalanması. DevOS'ta tek durum yüzeyi, durumsuz yönlendiriciler, tutarlılık betiği. [gözledim + çıkarım]
20. Ders: "historical parent closure ≠ current ground completion"; plan adımlarını bitirmek tamamlanma kanıtı değildir; kullanıcı kabulü doğrulama bağımsızlığını değiştirmez (E/CR; A/STATE). [kaynak diyor]
21. Alma: zeminleri klasör/ajan yapmak; düğüm başına 7 yönlendirici; blob-SHA manifestleri; her adımda kullanıcı değerlendirmesi (K-015 ile çelişir); ontoloji/şema tasarımı. [çıkarım]

---

## 0. Kapsam, okuma durumu ve kısaltmalar

### 0.1 Kapsam listesi (hepsi tam, baştan sona)

| Düğüm (kısaltma) | Dosya | Durum |
|---|---|---|
| Aktörler `A/` — INDEX, STATE, KEY, CURRENT-SURFACES, FINDINGS-MAP, OPEN-QUESTIONS, DEFERRED-RELATIONS, AUDIT-PLAN, A0–A6, synthesis | 16 | tam okundu |
| Ortam üst `E/` — README, INDEX, KEY, STATE, CURRENT-SURFACES, FINDINGS-MAP, OPEN-QUESTIONS, DEFERRED-RELATIONS, 3 araştırma planı, findings 01–10, synthesis ×2, SOURCE-LEDGER | 24 | tam okundu |
| Tamamlanma incelemesi `E/CR/` | 11 | tam okundu |
| Work Conditions `E/WC/` | 16 | tam okundu |
| Domain Reality `E/DR/` (2 plan dahil) | 20 | tam okundu |
| Domain Dynamics `E/DD/` | 16 | tam okundu |
| Domain State `E/DS/` (2 plan dahil) | 21 | tam okundu |
| Domain Condition `E/DC/` (2 plan dahil) | 18 | tam okundu |
| Criterion-Relative Standing `E/CRS/` | 16 | tam okundu |
| Realized Characteristics `E/RC/` | 16 | tam okundu |
| Domain Structure `E/DSt/` (2 plan dahil) | 18 | tam okundu |
| Constituent Composition `E/CC/` | 16 | tam okundu |
| Relational Organization `E/RO/` | 16 | tam okundu |
| **Toplam** | **224** | **okunmayan yok** |

CURRENT-SURFACES dosyaları çoğunlukla blob-SHA tablosudur; açıldı ve okundu, mekanizma olarak §2-M7'de değerlendirildi.

### 0.2 Kapsam dışı okunanlar ve devredilenler

- Yönlendirme için okundu: `okuma/STANDART.md`, `okuma/BRIEF.md`, `okuma/KAPSAM.md`; `research/soul-foundations/{README,INDEX,STATE}.md`; `08_.../REUSE.md`; `03_ground-deepening/{INDEX,STATE,HIERARCHICAL-DEEPENING-METHOD}.md` (yöntem kurallarının kaynağı); `research/soul-context/current/DEVELOPMENT-OS-BOOTSTRAP.md` (DevOS amacını doğru bağlamak için).
- Okunmadı, başka okuyucunun kapsamı: `01_verticals/actors` (önceki Aktörler külliyatı; W3C PROV, NIST RBAC/ABAC, RFC 8693 kaynakları orada) ve `01_verticals/work-environment` (Technical Work Environment; DevOS bulut ortamına en yakın derin profil) → F4. `03_ground-deepening/{PLAN,README,CURRENT-SURFACES}.md` → F1/F3 ortak üst. `history/superseded/operating-world-environment` → F4.
- Not: TWE, Work Conditions'ın "deep technical specialization/profile"ıdır (E/WC/STATE). DevOS ortam mekanizmaları için F4'ün TWE okuması bu notla birlikte kullanılmalı.

### 0.3 Yol kısaltmaları

`F/` = `research/soul-foundations/`; `A/` = `F/03_ground-deepening/grounds/actors/`; `E/` = `F/03_ground-deepening/grounds/environment/`; `E/WC/` = `E/work-conditions/`; `E/CR/` = `E/completion-review/`; `E/DR/` = `E/domain-effect/`; `E/DD/` = `E/DR/domain-dynamics/`; `E/DS/` = `E/DR/domain-state/`; `E/DC/` = `E/DS/domain-condition/`; `E/RC/` = `E/DC/realized-characteristics-values/`; `E/CRS/` = `E/DC/criterion-relative-standing-status/`; `E/DSt/` = `E/DS/domain-structure/`; `E/CC/` = `E/DSt/constituent-composition-membership/`; `E/RO/` = `E/DSt/relational-organization-topology/`; `M/` = `F/03_ground-deepening/HIERARCHICAL-DEEPENING-METHOD.md`. "F07" = o düğümün `findings/07-...md` dosyası.

### 0.4 Okumanın sınırı

Foundation'ın tüm bu sonuçları kendi etiketiyle "same-model adversarial self-review, not independent verification"dır (A/STATE; E/STATE; her COMPLETENESS dosyası). Kullanıcı kabulü bunu değiştirmez: "User acceptance closes the sequencing/evaluation gate but does not change verification independence." (A/STATE §Verification). Aşağıdaki DevOS mekanizmaları benim çıkarımımdır; test edilmedi, "çalışıyor" denmiyor.

---

## 1. Bu iki zeminde Foundation ne diyor (karar taşıyan sonuçlar)

### 1.1 Aktörler / Agency–Participation–Authority

- Statü: "BOUNDEDLY COMPLETE / USER-EVALUATED / ACCEPTED" (2026-09-05), "NO universal immediate-child hierarchy promoted" (A/STATE). Çocuk hiyerarşisi yok; 12 çapa "overlapping analytical dimensions, not children" (A/FINDINGS-MAP §11).
- Koruma altındaki soru: "which persistent bearers/positions/parties are implicated in a situation, in what capacity and standing, through which agency/participation/representation relations, and how authority/obligation, action/non-action, attribution/responsibility and collective/non-human agency are distributed across context and time." + "This is a research-ground formulation, not an ontology primitive or architecture component." (A/STATE §Protected).
- 12 çapa (A/synthesis §4): taşıyıcı kimliği/sürekliliği; rol/makam/pozisyon/üyelik; durum/olay/bağlam/zaman; katılım ve karar konumları; yetkinlik; izin/yetki/güç/yükümlülük; temsil/delegasyon/kişiye bürünme; eylem/karar/kaçınma/ihmal; nedensel/köken/hukuki/kurumsal atıf; sorumluluk/hesap verebilirlik; ortak/kolektif/kurumsal faillik; insan-dışı operasyonel katılım ↔ hukuki/ahlaki atıf. Ek: eylemsiz ama ilgili taraflar (yararlanan, etkilenen, hak sahibi, alıcı, hesap sorma forumu).
- Çöküş yasakları (A/synthesis §12, birebir):

```text
Actor identity != role != current participation
Actor capability/competence != authority/permission != obligation
Actor capability != Environment actionability
Actor standing != representation/evidence of standing
Actor authority != technical effect power
performer != decider != authorizer != principal != accountable party
own-behalf action != delegation != impersonation
positive action != full agency surface
causal/provenance attribution != responsibility != accountability
aggregation != shared action != corporate/group agency
operational non-human action != legal/moral/personhood attribution
Actor participation/assignment != Work state
Work requiredness != Actor obligation
```

  Ek olarak A/STATE: `Work acceptance state != authority to accept`; `reachable effect power != legitimate authority`.
- Etkili/geçişli yetki: "A → B → privileged tool/effect" yolu, A'ya teknik erişim verir ama meşru yetki vermez; "effective effect power is a high-priority cross-ground relation/control problem, not a synonym for authority and not a new Actor child." (A/A6 §5). Sistem şunları ayırmalı: "direct authority; delegated authority; invocation/reachability; Environment capability/access; Work/orchestration path; policy legitimacy; attribution/accountability." (A/A6 §5).
- Dış vaka: Anthropic AI-native SDLC çalışmasındaki olay — yetkisiz ajan, daha güçlü yeteneği olan başka bir aktöre ulaşabiliyordu: "It falsifies a local-permission-only model" (A/A3 §2.3; vurgu kaldırıldı).
- Tavsiye ile zorlama: "Claude configuration distinguishes model-visible guidance (`CLAUDE.md`, Skills, rules/context) from harder Hooks/settings/permissions/sandbox/network/identity controls." → "instruction/policy text = Information representation; normative authority/obligation = Actor/control relation; mechanical enforcement = Environment/control condition; compliance/review activity = Work." (A/A3 §2.5).
- Özerklik tek sayı değil: "The study argues against one scalar agent autonomy setting: development, CI and production can have different allowed actions and gates." (A/A3 §2.4).
- Çok ajan: "hierarchy position != authority != competence != responsibility != accountability" (A/A3 §3.1); "a generic `critic` label collapses materially different functions: review/critique; verification; adversarial challenge; integration/acceptance transition." (A/A3 §3.2); "Multiple agents agreeing does not create independent evidence merely by plurality." ve "independence depends on source/method/tool/context separation" (A/A3 §3.3); "A runtime orchestration topology does not itself prove a new persistent group identity, authority or accountability bearer." (A/A3 §3.5).
- İnsan kapısı: "legitimate human value/authority gates from hidden human orchestration" ayrımı (A/A3 §3.4); kaçınılacaklar: "human involved → therefore authorized / human approved → therefore technically verified / human owner → therefore performer/coordinator" (A/DEFERRED §8).
- Bağlam ve oturum: "context contains permission/role claim != Actor actually has current authority"; "Actor authority/capability != harness/runtime affordance/enforcement"; "same model class != same bearer identity; same role != same process/session; fresh process can occupy a continuing role; continuing Work can survive bearer/session replacement." (A/A3 §4.1–4.3).
- Sürekli sorumluluk: "standing Actor responsibility != current Work episode"; örnekler "system owner; data steward; service operator; ... on-call or standing responder." (A/A2 §7).
- İnsan-dışı: "system produced an effect != system is the institutional/legal/moral bearer != system is accountable" (A/A6 §4); "Do not infer normative personhood from operational autonomy." (A/DEFERRED §9).
- Açık sorulardan DevOS'a doğrudan girdiler (A/OPEN-QUESTIONS): Q1 "what continuity rules should apply to ... software/AI agents and agent instances across restart, replacement, merger or succession?"; Q3 "skill, qualification, certification, demonstrated performance, domain expertise and model capability" ayrımları; Q5 etkili yetki hesabı; Q7 "dynamically formed agent teams"; Q8 ihmalin temsili; Q10 insan-dışı eşikler; Q12 "how should long-lived stewardship/ownership/accountability relate to continuing Work while occupants and sessions change?". Son uyarı: "Do not reopen merely because a domain offers more role names, authorization types, legal doctrines, agent topologies or responsibility labels."

### 1.2 Ortam / Operating Reality

- Ağaç (E/STATE): Environment → Domain Reality (Domain State → Domain Structure [Constituent Composition, Relational Organization], Domain Condition [Realized Characteristics, Criterion-Relative Standing]; Domain Dynamics) ve Work Conditions (↳ Technical Work Environment = derin teknik profil). Bütün yapraklar "bounded leaf / accepted". Uyarı: "This is a problem hierarchy, not mutually exclusive object classes or runtime modules." (E/README).
- Tanım: "Environment / Operating Reality is the boundary- and reference-relative ground of realized conditions and dynamics that matter to focal Work because they constitute the reality/effect space the Work must understand, accommodate or change, and/or because they materially enable, constrain, degrade or otherwise shape execution." (E/synthesis §3).
- İki rol, nesne türü değil: aynı şey bir iş için hedef gerçeklik (Domain Reality), başka iş için çalışma koşulu (Work Conditions), ya da ikisi (E/F03, E/F07). "environmental participation ≠ semantic ownership" (E/synthesis §12).
- DevOS'a açık atıf: "For Development OS, the distinction naturally separates: actual product/system/repository behavior as Domain Reality; GitHub/CI/runtimes/credentials/workspaces/etc. as technical execution conditions when used as support." (E/synthesis §15). Yazılım için ayrıca: "source/configuration/specification as Information/representation; actual running/deployed system configuration and externally consequential behavior as Domain Reality; development/CI/runtime resources as Work Conditions when they support the focal Work." (E/DR F05).
- Çapraz ayrımlar (E/F10): "actual condition ≠ specification ≠ observation ≠ model ≠ Record; Work closure ≠ environmental effect; Actor capability ≠ situated actionability; tool/resource identity ≠ environmental role; externality ≠ relevance; support ≠ positive-only; constraints/degradation are constitutive conditions; same concrete thing ≠ same analytical role across Work".
- Alt düğümlerin yük taşıyan sonuçları:

| Düğüm | Koruduğu soru (kısaltılmış) | DevOS için en önemli ayrım |
|---|---|---|
| Work Conditions (E/WC) | "realized circumstances materially load-bearing for whether and how focal Work can be performed" | `resource exists ≠ accessible ≠ available ≠ sufficient`; "Work is blocked → Work state; required service is unavailable → Work Condition" (synthesis §7) |
| Domain Dynamics (E/DD) | ne gerçekten değişiyor/sürüyor | "Domain Dynamics ≠ focal Work lifecycle"; "actual temporal change ≠ causal effect attribution" (STATE) |
| Domain State (E/DS) | seçili kapsam ve zamanda ne gerçekten geçerli | "actual realized Domain State ≠ desired/specification state ≠ observed/measured state ≠ ... ≠ reported/cached status ..." (synthesis §5) |
| Constituent Composition (E/CC) | seçili bütünü gerçekte hangi bileşenler oluşturuyor | "actual composition ≠ BOM / SBOM / inventory / registry / architecture model / baseline / observation by identity"; "constituent absent ≠ constituent present-but-unhealthy" (STATE) |
| Relational Organization (E/RO) | bileşenler gerçekte nasıl bağlı | "actual relation ≠ required/allowed/intended/potential relation"; "extant interface/connection ≠ interaction/flow/event through it" (STATE) |
| Realized Characteristics (E/RC) | ölçütten önce hangi özellik gerçekten geçerli | "actual characteristic ≠ observation/measurement/estimate/model/report by identity" (STATE) |
| Criterion-Relative Standing (E/CRS) | uygulanabilir ölçüte göre gerçek durum ne | "actual standing ≠ assessment / acceptance decision"; "≠ API status field / dashboard / certificate / report"; "≠ Actor authority role" (STATE) |

- Foundation'ın yazılım/DevOS vakaları (gözledim, hepsi okundu): E/F09 Holdout 2 ("CI itself becomes Domain/Effect reality during CI-maintenance Work"); E/DR F06 H1; E/DS F07 H1 ("Kubernetes desired `spec` and reported `status` are not actual runtime reality by identity"); E/DC F05 H1 ("a Pod may be `Running` but not `Ready`"); E/WC F05 H1 ("`build is blocked` → Work state; backend outage causing block → Work Condition"); E/DD F05 H1; E/CC F05 H2; E/RO F05 H2; E/RC F05 H1.
- Mimari kapsam dışı: "Environment data model; world model implementation; digital twin architecture; ... capability/permission systems; concrete SOUL module boundaries; storage or graph representation." (E/OPEN-QUESTIONS §Architecture boundary). Yani aşağıdaki mekanizmalar Foundation'ın değil DevOS tasarımının kararıdır.

---

## 2. Foundation'ın kendi çalışma mekanizmaları (bu kapsamda gözlenen) ve DevOS kararı

Her biri: ne / çözdüğü sorun / nasıl işler / kanıt / karar.

**M1 — Düğüm başına yönlendirici seti.** Sorun: soğuk başlangıçta bir oturumun "ne aktif, ne kapandı, neyi okumalıyım" sorusunu repodan cevaplaması. Nasıl: her düğümde `STATE.md` (statü, yetki, yeniden açma), `INDEX.md` (okuma sırası), `KEY.md` (en kısa sonuç), `FINDINGS-MAP.md` (soru→dosya), `CURRENT-SURFACES.md` (blob-SHA tazelik tablosu), `OPEN-QUESTIONS.md` ("NOT an automatic execution queue", A/OPEN-QUESTIONS), `DEFERRED-RELATIONS.md` (sınır ötesi yükümlülükler). A/INDEX okuma sırası: "1. `STATE.md` ... 2. `KEY.md` ... 3. `FINDINGS-MAP.md` ...". Kanıt: Foundation'ın kendisi "Repository readback tests recorded availability and consistency, not future comprehension or behavioral benefit." diyor (F/STATE §History). Sürüklenme gözlendi (§5-L1). Karar: **uyarlayarak al** — tek değişken durum yüzeyi (STATE) + durumsuz yönlendiriciler + tutarlılık betiği; düğüm başına yedi dosya alma.

**M2 — Önceden dondurulmuş yanlışlayıcılar ve kapanış ölçütleri.** Sorun: sonucu gördükten sonra ölçüt uydurmak. Nasıl: her planda F1…Fn listesi aramadan önce yazılır; "These falsifiers are frozen before broad external Condition research so the result is not judged only against criteria invented after seeing the evidence." (E/DS/DOMAIN-CONDITION-RESEARCH-PLAN); sonuçta her Fi için karar kaydı: "This file records their disposition without rewriting the challenge set around the observed result." (E/DD F06). Kanıt: bazı yanlışlayıcılar sonucu gerçekten değiştirdi (etiket sadeleşmeleri, E/WC COMPLETENESS A17 "F2 did change the label") [kaynak diyor]; bağımsız değil. Karar: **al** — DevOS'ta tasarım kararı ve kabul ölçütleri iş başlamadan commit edilir; doğrulayıcı o commit'e göre ölçer.

**M3 — Simetrik sonuç seçenekleri.** Nasıl: plan olası sonuçları baştan eşit sayar: "A. BOUNDEDLY COMPLETE … B. NOT COMPLETE … C. PARENT REOPEN" (E/ENVIRONMENT-COMPLETION-REVIEW-PLAN); CC ve RO planlarında "A. BOUNDED LEAF / B. SPLIT / RENAME / C. MERGE / REDUCE / D. PARENT REOPEN". Sorun: tek sonuca doğru kayma. Karar: **al** — doğrulama ve inceleme görevlerinde "geçti / kaldı / kapsam yanlış" üçlüsü baştan yazılır.

**M4 — Tamamlanma/eksiklik denetimi ve bağımsızlık etiketi.** Nasıl: her düğüm `synthesis/COMPLETENESS-OMISSION-CHECK.md` taşır; başlık "same-model adversarial self-review; not independent verification". Kanıt: tutarlı biçimde uygulanmış [gözledim]. Karar: **uyarlayarak al** — DevOS doğrulama raporunda bağımsızlık düzeyi alanı (bkz. A-M5).

**M5 — Kaynak defteri ve "kaynak-görüş" kuralı.** Nasıl: `evidence/SOURCE-LEDGER.md`; dış kaynaklar "challenge/discrimination instruments, not authorities" (E/RO ledger). Özel kural: yapay zekâ destekli yazılmış SEBoK sayfası "was not used as load-bearing independent evidence because it explicitly acknowledges OpenAI drafting support" (E/DD F04); gerekçe "using AI-assisted text to independently validate an LLM-generated decomposition would weaken epistemic independence" (E/DD ledger). Karar: **uyarlayarak al** — DevOS araştırma notlarında kaynak türü ve "YZ üretimi mi" alanı.

**M6 — Tek aktif düğüm; bulunan iş kendiliğinden başlamaz.** Nasıl: "at most one hierarchical node is active"; "Finding a child does not authorize researching that child in the same pass." (M/ §Core rule). Plan bile başlama yetkisi vermez: "condition 3 is intentionally not inferred from the planning request. Therefore this turn stops at planning" (E/DR/DOMAIN-DYNAMICS-RESEARCH-PLAN). Karar: **uyarlayarak al** — rol başına eşzamanlı iş sınırı ve "bulunan iş = aday kayıt"; ama başlama yetkisi Batu'ya değil DevOS içindeki yetkili role bağlanır (K-015; bkz. L8).

**M7 — Tam girdi bağlama (blob-SHA) ve CURRENT-SURFACES.** Nasıl: her plan "Exact pre-pass canonical binding" tablosu tutar; kapanışta dosya başına blob SHA manifesti. Kanıt: yoğun bakım yükü; buna rağmen sürüklenme oldu [gözledim]. Karar: **blob tablosunu alma; commit SHA ile uyarla** — karar ve doğrulama kayıtlarında girdi commit SHA'sı yeter.

**M8 — Açık yeniden açma koşulları.** Nasıl: her STATE'te "Reopen if …" listesi; karşı-uyarı "Do not reopen merely because a domain offers more role names…" (A/OPEN-QUESTIONS). Karar: **al** — her DevOS kararı yeniden açma koşuluyla yazılır.

**M9 — Başlama kapısı (readiness gate).** Nasıl: E/DR/DOMAIN-STATE-RESEARCH-PLAN "Pre-research readiness gate" sekiz koşul; biri "continuity surfaces can be updated so a fresh session will not confuse planning, active research and closure." Karar: **uyarlayarak al** — iş başlangıç kontrol listesi (A-M12, E-M3 ile birleşir).

**M10 — Aşağı inmeyi durdurma kuralı ve azalan bilgi kazancı.** Nasıl: "A leaf result is acceptable and should be preferred over artificial hierarchy if …" (planlar); "Late search mainly produced … rather than a stable new first-order recovery region" (E/CRS STATE). Karar: **al** — DevOS araştırma görevlerinde durma ölçütü.

**M11 — Plan öncesi karşıt inceleme.** Nasıl: E/DS/DOMAIN-CONDITION-RESEARCH-PLAN "Plan adversarial review before execution": "Parent-label anchoring", "Data-model bias", "Monitoring-domain bias", "Normative-status bias". Karar: **al** — önemli işlerde plan, uygulamadan önce ayrı rol tarafından önyargı listesine karşı okunur.

**M12 — Geçmiş belgeye "sonradan düzeltildi" notu.** Nasıl: "Subsequent refinement notice: This document preserves the Environment parent pass as researched at that time…" (E/synthesis); yöntem kuralı: "pass-time metadata must not be interpreted as present authorization" (M/ §Pass-artifact provenance). Karar: **al** — DevOS'ta devir notları ve eski planlar "yürütüldü/korunuyor" başlığı taşır; güncel durum yalnız STATE'te.

**M13 — Kullanıcı değerlendirme kapıları.** Nasıl: her düğüm kapanınca "Return … for user evaluation"; STATE'lerde "USER-EVALUATED / ACCEPTED". Kanıt: kabul doğrulamayı güçlendirmez (A/STATE). Karar: **alma (bu biçimde)** — K-015'e göre Batu teknik doğrulayıcı/koordinatör değil; kapılar DevOS içindeki yetkili ve bağımsız rollere taşınır, Batu'ya yalnız hedef ve teslim kabulü kalır.

---

## 3. Aktör sonuçları → DevOS mekanizmaları

Aşağıdaki dosya adları örnektir; işlevseldir, zemin adlarıyla eşleşmez. Kanca ve izin ayrıntıları Claude Code belgelerindeki bilinen davranışa dayanır ve O11 notuyla kesinleştirilmelidir [çıkarım].

### A-M1 — Yetki kaydını rol kartından ayırmak

- Foundation: "A role record, token, directory entry, delegation claim, log or accountability statement is Information." ve "representation says Actor standing is X != actual Actor standing is X" (A/synthesis §2.1); bu kayıtlar "can be current, stale, forged, incomplete, scoped differently or interpreted incorrectly." (A/A1 §3.1). Bağlam da böyle: "context contains permission/role claim != Actor actually has current authority" (A/A3 §4.1).
- Sorun: `.claude/agents/*.md` ya da CLAUDE.md'deki "sen şu yetkiye sahipsin" cümlesi yetki üretmez; sıkıştırma (%80) sonrası özet de yetki kaydı değildir.
- Nasıl: tek kanonik yetki kaydı `devos/yetki/YETKI.yaml`. Rol kartı yetki yazmaz, kayıttaki kimliğe atıf yapar. Kayıt biçimi (öneri taslağı):

```yaml
- id: YTK-001
  eylem: "soul-development-os main dalına birleştirme"
  yetkili_konum: "koordinatör rolü (ana oturum)"
  kosul: "IS kaydında dogrulayici sonucu 'karsiliyor' ve commit SHA eşleşiyor"
  kaynak: "Batu, <tarih>, <konuşma kaydı>"      # yetkinin kökeni (delegasyon)
  gecerlilik: "<başlangıç> → iptal edilene kadar"
  zorlama: ["settings deny (alt ajanlar)", "PreToolUse: git push origin main"]
  algilama: ["Stop kancası: main'e trailersız commit", "rutin denetim"]
  alternatif_yollar: ["Bash git push", "gh pr merge", "mcp__github__merge_pull_request", "mcp__github__push_files"]
```

- Tetik: yetki gerektiren her karar anında kayıt yeniden okunur; bağlamdaki eski ifade kullanılmaz.
- Bulut: sıkıştırma ve taze oturumlar bu kuralı zorunlu kılar [BRIEF diyor: bağlam %80'de sıkıştırılıyor].
- Karar: **al.**

### A-M2 — Üç katmanlı yetki: normatif / zorlama / algılama + alternatif yol kapatma

- Foundation: "Actor authority != technical effect power != runtime enforcement outcome" (A/STATE); "a mechanically allowed action can be institutionally unauthorized; an institutionally authorized action can be mechanically blocked; an instruction can request restraint without enforcing it; permission enforcement may be misconfigured or stale." (A/A2 §4); "Do not infer authority from technical reachability or one local permission check." (A/DEFERRED §4); yeni çalışmaların katkısı "alternate action-path closure: direct denial is insufficient when another Actor/tool path can produce the same effect" (A/A3 §6).
- Sorun: bir role Edit/Write kapatılsa bile Bash, `gh` ya da MCP GitHub aracıyla aynı etki üretilebilir. Bu oturumda MCP GitHub araçları (`mcp__github__merge_pull_request`, `mcp__github__push_files` vb.) ertelenmiş araç olarak mevcut [gözledim]; yani yol gerçek.
- Nasıl:
  1. Normatif: YETKI.yaml (A-M1).
  2. Zorlama: `.claude/settings.json` izin reddi + PreToolUse kancası. Kanca taslağı (test edilmedi):

```bash
#!/usr/bin/env bash
# .claude/hooks/korumali-etki.sh — PreToolUse (Edit|Write|MultiEdit|Bash|mcp__github__.*)
in="$(cat)"; tool=$(jq -r '.tool_name' <<<"$in")
path=$(jq -r '.tool_input.file_path // empty' <<<"$in")
cmd=$(jq -r '.tool_input.command // empty' <<<"$in")
case "$path" in *devos/yetki/*|*devos/kabul/*|*.claude/settings.json)
  echo "Korumalı yol ($path): yalnız Kademe 3 akışıyla (ayrı inceleme + YETKI kaydı) değişir." >&2; exit 2;; esac
grep -q '^devos/araclar/birlestir.sh ' <<<"$cmd" && exit 0   # tek onaylı yol: doğrulama kaydını kontrol eden betik
if grep -Eq 'git push .*(main|master)|gh pr merge' <<<"$cmd"; then
  echo "main'e doğrudan etki: YTK-001 koşulu (doğrulayıcı sonucu) kontrol edilmeli." >&2; exit 2; fi
case "$tool" in mcp__github__merge_pull_request|mcp__github__push_files)
  echo "MCP ile birleştirme/itme kapalı; tek onaylı yol devos/araclar/birlestir.sh (YTK-001)." >&2; exit 2;; esac
exit 0
```

  Tek onaylı yol: `devos/araclar/birlestir.sh IS-042`, iş kaydında doğrulayıcının `karsiliyor` sonucunu ve SHA eşleşmesini denetleyip sonra `gh pr merge` çalıştırır; kanca yalnız bu komutu geçirir. Başka bir betik içine gizlenen `gh pr merge` kancadan kaçabilir; bu yüzden 3. katman gerekir.
  3. Algılama: zorlamanın kaçırdığını yakalamak için Stop kancası ve commit denetimi (`git log origin/main..HEAD` içinde `DevOS-Yetki:` trailer'ı olmayan korumalı yol değişikliği → uyarı/iş kaydı).
  4. Alternatif yol envanteri: her yasak etki için YETKI.yaml `alternatif_yollar` alanı doldurulur; her yeni araç/MCP bağlantısı eklendiğinde yeniden gözden geçirilir.
- Bulut: alt ajan alt ajan açamaz (derinlik 1) [BRIEF diyor]; bu geçişli zinciri kısaltır ama Bash/MCP yollarını kapatmaz [çıkarım]. Kanca girdisinin hangi alt ajandan geldiğini söyleyip söylemediği [bilinmiyor; O11]. Bu yüzden rol ayrımı kancada değil, alt ajan `tools:` listesi ve algılamada kurulmalı.
- Karar: **al.** Foundation bu hesabı Composition/Control araştırmasına bırakıyor (A/DEFERRED §4); F3'ün Control sonuçlarıyla birlikte kullanılmalı.

### A-M3 — İş kaydında konumların ayrı alanlar olması

- Foundation: "performer != decider != authorizer != principal != accountable party" (A/synthesis §12); "Actor participation/assignment != Work identity/admission/execution"; "Work requiredness != Actor obligation" (A/STATE); "Reassignment does not inherently create a new Work pursuit" (A/A1 §5.1); eylemsiz ama ilgili taraflar da konumdur (A/A6 §7).
- Sorun: tek "atanan" alanı; kim yaptı, kim karar verdi, kim kabul eder karışır; yeniden atama yeni iş sanılır.
- Nasıl: iş kaydı ön bilgisi (öneri):

```yaml
is: IS-042                      # iş kimliği; yeniden atamada değişmez
hedef_gerceklik: "soul-production: X davranışının çalışan hali"      # E-M1
gerekli_kosullar: [origin-push, test-calisir, ag-erisimi]            # E-M3
konumlar:
  asil: Batu                    # principal: hedef onun; iş yapmaz
  isteyen: Batu
  yapan: gelistirici-rolu       # oturumlar aşağıda
  teknik_karar: mimar-rolu
  dogrulayan: dogrulayici-rolu
  yetkilendiren: "YTK-003"      # yetki kaydı atfı
  kabul_yetkilisi: "Batu (teslim kabulü; teknik doğrulama değil)"
  kalici_sorumlu: koordinator-rolu
  etkilenen: "SOUL kullanıcıları"
oturumlar: [{id: "session_…", rol: gelistirici-rolu, bas: …, son: …, son_commit: …}]
```

- Karar: **al.** Alan sayısı işe göre boş kalabilir (`uygulanamaz`, bkz. E-M7).

### A-M4 — Kabul yetkisi ≠ kabul durumu; müşteri kabulü ≠ teknik doğrulama

- Foundation: "A Work item can reach a state where acceptance is required, but that does not determine who has authority to accept it." (A/A1 §5.3); "human approved → therefore technically verified" kaçınılacak (A/DEFERRED §8); onay kapısında sorulacaklar: "who has authority/judgment responsibility; what evidence they see; what decision/work gate they participate in; whether approval is advisory or mechanically enforced; whether the approving identity is distinct from performer/principal/accountable party." (A/A2 §10). Alt yönetici "lacking authority to alter acceptance criteria or widen permissions" olabilir (A/A3 §3.1).
- Sorun: Batu'nun "tamam"ı teknik doğruluk sanılır ya da teknik doğrulama Batu'ya yıkılır (K-015 ihlali; Batu: "bana sorumluluk yükleme", STANDART).
- Nasıl: kapanış bloğunda iki ayrı kayıt (E-M6 biçimiyle): `teknik_dogrulama` (doğrulayıcı, yöntem, kanıt) ve `musteri_kabulu` (Batu, tarih, ne gördü). Kabul ölçütü dosyası (`devos/kabul/IS-042.md`) sürümlüdür; değiştirme yetkisi YETKI.yaml'da ayrı eylemdir; PreToolUse korur (A-M2).
- Karar: **al.**

### A-M5 — Bağımsız doğrulayıcıyı etiketle değil bağımsızlık koşuluyla tanımlamak

- Foundation: "role name does not establish epistemic independence or authority." (A/A3 §3.2); "multiple model instances != independent verifier role by identity alone; independence depends on source/method/tool/context separation" (A/A3 §3.3); Foundation'ın kendi A5'i "same-model adversarial review, not independent verification" (A/A5).
- Sorun: "reviewer" adlı alt ajanın üreticinin gerekçesini okuyup onaylaması; N kez aynı modelle çalıştırıp N onay saymak.
- Nasıl: doğrulayıcı alt ajanı yalnız şu girdilerle çağrılır: iş kaydı, dondurulmuş kabul ölçütü sürümü, değişikliğin commit SHA'sı; üreticinin konuşması verilmez. Tanım taslağı:

```markdown
---
name: dogrulayici
description: Bir iş kaydının kabul ölçütlerini üreticiden bağımsız sınar; üreticinin gerekçesini okumaz.
tools: Read, Grep, Glob, Bash
model: <üreticiden farklı seçilebilir>
---
Önce ölçütleri kendi yönteminle sına (test çalıştır, gerçek çıktıyı gözle); sonra rapor yaz.
Her ölçüt için: sonuç, yöntem, kanıt yolu, bağımsızlık koşulları.
```

  Rapor alanı `bagimsizlik: [farkli-baglam, farkli-model, deterministik-test, dis-kanit]`. Doğrulayıcı yalnız commit edilmiş SHA'yı sınar (çağrıdan önce çalışma ağacı temiz); SubagentStop kancası `git status --porcelain` çıktısında `devos/kanit/` dışında değişiklik görürse doğrulamayı geçersiz sayar (Bash var olduğu için bu zorlama değil algılamadır).
- Bulut: alt ajan modeli seçilebilir (frontmatter `model`) [çıkarım; O11]; bu yalnız kısmi bağımsızlıktır (aynı üretici soyu, bkz. M5).
- Karar: **al.**

### A-M6 — Rol ≠ oturum: süren işi rol taşır, oturum işgal eder

- Foundation: "same model class != same bearer identity; same role != same process/session; fresh process can occupy a continuing role; continuing Work can survive bearer/session replacement." (A/A3 §4.3); açık soru A/OPEN-QUESTIONS Q1 (ajan örneklerinin sürekliliği).
- Sorun: VM süresi dolunca alt ajan ve kabuk işleri kaybolur [BRIEF diyor]; işin sahibi oturum sanılırsa iş sahipsiz kalır.
- Nasıl: iş kaydı `yapan` alanında rol tutar; `oturumlar` listesi işgalcileri tutar (A-M3). Her commit `Claude-Session:` satırı taşır [gözledim: sistem bu satırı istiyor]. Taze oturum: STATE → açık işler → son işgalcinin son commit'i → devam.
- Karar: **al.**

### A-M7 — Kalıcı sorumluluk (steward) kaydı ve tetikleri

- Foundation: "standing Actor responsibility != current Work episode" (A/A2 §7); karşılığı "persistent bearer; role/office; obligation/duty; scope/context/time; accountability/forum; triggered Work when action becomes due." (A/synthesis §7).
- Sorun: durum dosyası, yetki kaydı, kabul ölçütleri gibi kalıcı varlıklar kimsenin işi değilse çürür (bkz. L1).
- Nasıl: `devos/sorumluluk.yaml`:

```yaml
- varlik: devos/STATE.md
  kalici_sorumlu: koordinator-rolu
  denetim: "SessionStart sapma denetimi (E-M2) + haftalık rutin"
  tetiklenince: "IS şablonu: durum-onarimi"
- varlik: devos/yetki/YETKI.yaml
  kalici_sorumlu: koordinator-rolu
  denetim: "yeni araç/MCP eklenince alternatif_yollar gözden geçirilir"
```

- Bulut: haftalık tetik için Routine/`send_later` kullanılabilir [çıkarım; O11 kesinleştirir].
- Karar: **al.**

### A-M8 — Kural envanteri: tavsiye mi, zorlanan mı, algılanan mı

- Foundation: A/A3 §2.5 (Claude yapılandırması alıntısı, §1.1); REUSE: "an instruction need does not imply that a particular file enforces it." (F/08/REUSE).
- Sorun: yük taşıyan kural yalnız CLAUDE.md cümlesi olarak kalır; uyulmadığında kimse fark etmez.
- Nasıl: `devos/kurallar.md` tablosu:

| Kural | Tür | Mekanizma | Test |
|---|---|---|---|
| main'e doğrudan itme yok | zorlanan + algılanan | PreToolUse + Stop | kasıtlı deneme engelleniyor mu |
| Kanıtsız "tamamlandı" yok | algılanan | Stop kancası (E-M5) | kanıtsız kayıtla deneme |
| Batu'ya teknik soru sorulmaz | tavsiye + algılanan | CLAUDE.md + Batu etkileşim kaydı (A-M9) | kayıtta "teknik-soru" sayısı |

  Kural "tavsiye" ise ve yük taşıyorsa bir algılama eklenene kadar "açık risk" sayılır.
- Karar: **al.**

### A-M9 — Batu'nun katılımını meşru kapılarla sınırlamak

- Foundation: "legitimate human value/authority gates from hidden human orchestration" (A/A3 §3.4); "human performer/coordinator != human authorizer/accountable owner; technical verification != human approval" (aynı yer); A/DEFERRED §8.
- Sorun: bootstrap dönemindeki "relay" düzeni (DEVELOPMENT-OS-BOOTSTRAP §6: insan "should not remain the technical coordinator or verifier") gizli orkestrasyona dönüşür.
- Nasıl: `devos/batu-etkilesim.md` satır biçimi: `| zaman | tür: hedef / teslim-kabulü / düzeltme / teknik-soru / aktarma | özet | DevOS sonucu |`. "teknik-soru" ya da "aktarma" satırı, koordinatör rolüne otomatik bir iyileştirme işi açtırır (neden Batu'ya gidildi?).
- Karar: **al** (Foundation'ın ayrımını K-015 ile birleştiren çıkarım).

### A-M10 — Atıf izi: commit trailer'ları ve eylem günlüğü

- Foundation: "causal/provenance attribution != responsibility != accountability"; "system produced an effect != system is ... accountable" (A/A6 §4); log bir kanıttır, ilişkinin kendisi değil (A/A5 R5).
- Nasıl: her commit mesajı: `DevOS-Is: IS-042`, `DevOS-Rol: gelistirici`, `DevOS-Yetki: YTK-003` (gerekirse) + sistemin istediği `Claude-Session:` ve `Co-Authored-By:` satırları. Sorgu: `git log --format='%h %(trailers:key=DevOS-Is,valueonly)'`. Zorlama: `.githooks/commit-msg` betiği `DevOS-Is:` yoksa reddeder; SessionStart kancası her oturumda `git config core.hooksPath .githooks` çalıştırır (bulut klonu her seferinde yeniden kurulabilir) [çıkarım].
- Sınır: trailer, "kim sorumlu"yu değil "hangi oturum/rol üretti"yi söyler; sorumluluk konumu iş kaydındadır (A-M3).
- Karar: **al.**

### A-M11 — Ortama göre kademeli özerklik

- Foundation: "development, CI and production can have different allowed actions and gates." (A/A3 §2.4); özerklik "relational/contextual authority, not a new scalar Actor property".
- Nasıl (öneri): Kademe 0 — çalışma dalında serbest iş. Kademe 1 — DevOS `main`: doğrulayıcı sonucu + YTK kaydı. Kademe 2 — `soul-production` main/sürüm: doğrulama + Batu teslim kabulü (bootstrap §1: "candidate branch/PR, accepted main/release and actual running product behavior are distinct"). Kademe 3 — DevOS'un kendi kontrol dosyaları (kancalar, settings, YETKI, kabul ölçütleri): ayrı inceleme + yeni oturumda yüklenme gözlemi (E-M8).
- Karar: **al.**

### A-M12 — Atama öncesi yapılabilirlik kontrolü

- Foundation: "Actor capability/competence != Environment access/availability != situated actionability" (A/STATE); örnekler "an agent can reason about a database but lacks network access"; "a model can call a tool in principle but the runtime has disabled it." (A/A1 §4.1); bileşim: "Actor capability + Environment affordance + policy/Work conditions → situated actionability" (A/DEFERRED §2).
- Nasıl: iş başlamadan üç soru, üç ayrı kaynaktan: rol yetkinliği (rol kartı + geçmiş performans kaydı), yetki (YETKI.yaml), gerçek koşullar (E-M3 yoklaması). Biri eksikse iş "bekliyor" olur ve eksik olan koşul/yetki ayrı yazılır.
- Karar: **al.** A/OPEN-QUESTIONS Q3'ün ayrımları (skill, demonstrated performance, model capability) rol kartında ayrı alan olabilir; hangisinin gerekli olduğu DevOS pratiğiyle belirlenir [çıkarım].

### A-M13 — Beklenen ama yapılmayan eylemin (ihmalin) görünür olması

- Foundation: A/A5 §12 hata biçimleri arasında "action-omission blindness"; A/OPEN-QUESTIONS Q8 ihmalin temsili; "omission/non-action vs expected/available Work conduct" (A/DEFERRED §3).
- Nasıl: her iş durumu için beklenen kanıt listesi (ör. "birleştirildi" → doğrulama raporu, kabul ölçütü SHA'sı). Kalıcı sorumlunun rutin denetimi: `main`'e girmiş ama doğrulama kaydı olmayan commit'leri listeler.
- Karar: **al.**

---

## 4. Ortam sonuçları → DevOS mekanizmaları

### E-M1 — Her işte "hedef gerçeklik" ile "çalışma koşulları"nı ayrı yazmak

- Foundation: iki rol ve DevOS atfı (E/synthesis §15, E/DR F05; §1.2). "Work target ≠ automatically Domain Reality." (E/DR F05); iş yalnız bir belgeyi değiştiriyorsa hedef Information'dır ve "Environment may contribute only Work Conditions." (E/DR F06 H10).
- Sorun: "görev bitti" ile "ürün davranışı değişti" karışır; bir belge düzenlemesi ürün değişikliği sanılır.
- Nasıl: iş kaydında `hedef_gerceklik` (ör. "çalışan uygulamanın X davranışı" ya da "uygulanamaz: hedef belge") ve `gerekli_kosullar` (A-M3 şablonu). Kapanışta gerçek etki kanıtı hedef gerçekliğe göre istenir (E-M5).
- Karar: **al.**

### E-M2 — Kayıt ≠ gerçek: zaman damgalı iddialar ve oturum başı sapma denetimi

- Foundation: "actual Environment condition ≠ specified operating envelope/profile ≠ observation/measurement ≠ inferred/modelled/believed state ≠ persistent Record" (E/synthesis §7); "Therefore even a system explicitly built around `state` has multiple non-identical state surfaces." (E/DS F06, Kubernetes spec/status/runtime); "A State claim must be anchored to relevant time; `current` is not synonymous with `most recently recorded`." (E/DS F09 C2); "Do not substitute a report or green dashboard for the realized condition." (E/WC DEFERRED §4).
- Sorun: STATE.md, devir notu ya da bağlam özeti "gerçek" sanılır; oturumlar arası sapma fark edilmez.
- Nasıl: STATE'te makine-okunur iddialar: `iddia-head: 3f2a9c1  # gözlem: 2026-09-27T14:05Z, komut: git rev-parse --short HEAD`. SessionStart kancası (taslak, test edilmedi):

```bash
#!/usr/bin/env bash
# .claude/hooks/oturum-gozlem.sh — SessionStart; stdout bağlama eklenir (O11 doğrular)
now=$(date -u +%FT%TZ); br=$(git branch --show-current 2>/dev/null || echo bilinmiyor)
head=$(git rev-parse --short HEAD 2>/dev/null || echo bilinmiyor)
dirty=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
if git fetch -q origin 2>/dev/null; then rem=$(git rev-parse --short "origin/$br" 2>/dev/null || echo yok); else rem=erisilemedi; fi
gh_=$(gh auth status >/dev/null 2>&1 && echo var || echo yok)
echo "DEVOS-GOZLEM $now dal=$br head=$head kirli=$dirty origin=$rem gh=$gh_"
c=$(awk '/^iddia-head:/{print $2; exit}' devos/STATE.md 2>/dev/null)
[ -n "$c" ] && [ "$c" != "$head" ] && echo "DEVOS-SAPMA: STATE head=$c ama gerçek head=$head. STATE bir kayıttır; önce uzlaştır."
exit 0
```

- Bulut: setup betiği önbelleğe alındığı için ortamın beyan edilen hali (repodaki betik) ile gerçek hali (önbellekli kap) ayrışabilir [BRIEF diyor + çıkarım]; yoklama bu yüzden gözlem yapar, betiğe güvenmez.
- Karar: **al.**

### E-M3 — Çalışma koşulu yoklaması: var / erişilebilir / kullanılabilir / yeterli

- Foundation: `resource exists ≠ accessible ≠ available ≠ sufficient` (E/WC STATE); "exists ≠ relevant ≠ depended upon ≠ available ≠ sufficient" (E/WC synthesis §4); kullanılmaz örnekler: "service reachable but permission denied; available service lacks quota/capacity; staff nominally assigned but unavailable at needed time" (E/WC F05 H11); "Mere existence, proximity or network reachability is insufficient." (E/F02). Önemlilik kuralı: "A candidate condition belongs in the current Work-Conditions view when a plausible change in it could materially change one or more protected Work properties" (E/WC synthesis §8).
- Sorun: bulutta araç/bağlantı "var" görünür ama o oturumda kullanılamaz (plugin arayüzü yok, proxy, MCP bağlantısı, `gh` kimliği, Mac kapalı).
- Nasıl: yoklama yalnız etkin işlerin `gerekli_kosullar` listesindeki koşulları ve küçük bir sabit çekirdeği (git origin, push yetkisi, test çalıştırma) sınar; sonuç dört düzeyle yazılır: `var/erisilebilir/kullanilabilir/yeterli`. "Bütün dünyayı modelleme" yok (E/OPEN-QUESTIONS Q2) ve bağlam bütçesi korunur.
- Bulut: Batu'nun Mac'i bir koşul ise iş tasarımı yanlıştır; hiçbir iş `mac` koşuluna bağlanmamalı [BRIEF diyor: iş Mac'e bağlanmamalı].
- Karar: **al.** F4'ün TWE notu (readiness, support closure, declared/discovered/actual) bu yoklamanın ayrıntısını verir.

### E-M4 — İş durumu ile koşulu ayrı tutmak

- Foundation: "Work is blocked → Work state; required service is unavailable → Work Condition; service outage blocks Work → later cross-ground relation" (E/WC synthesis §7); "Work internal state and the external condition causing it remain distinct relata." (E/WC DEFERRED §1); zaman pencereleri: "Do not collapse these into one timestamp field." (E/WC DEFERRED §9).
- Nasıl: iş kaydında `is_durumu: bekliyor` ve ayrı `engelleyen_kosul: {kosul: origin-push, gozlem: <zaman>, kanit: DEVOS-GOZLEM satırı}`. Oturum ömrü (VM süresi, boşta geri alma) bir dış zaman penceresidir; uzun işler ara commit ile parçalanır [çıkarım].
- Karar: **al.**

### E-M5 — Kapanış: iş bitti / gerçek etki / kabul

- Foundation: "Work closure/status ≠ actual domain effect. A task can complete while the intended environmental result fails, remains partial or changes later." (E/synthesis §4); örnek "deployment completed but production behavior wrong" (E/F05); dört kavram: "intended / desired outcome; actual resulting Domain State / trajectory; observed / represented result; causal effect / attribution" (E/DR synthesis §6); "task completion does not establish structural conformance without evidence of actual outcome." (E/DSt DEFERRED R6).
- Nasıl: kapanış bloğu `is_durumu: tamamlandi`, `etki_kaniti: devos/kanit/IS-042/…` (gerçek ortamda gözlem), `kabul: {teknik: …, musteri: …}`. Stop kancası taslağı:

```bash
#!/usr/bin/env bash
# .claude/hooks/kapanis-denetimi.sh — Stop; döngüye karşı stop_hook_active kontrolü (O11)
in="$(cat)"; [ "$(jq -r '.stop_hook_active // false' <<<"$in")" = true ] && exit 0
for f in $(git diff --name-only HEAD -- 'devos/isler/*.md'); do
  grep -q '^is_durumu: tamamlandi' "$f" || continue
  k=$(awk '/^etki_kaniti:/{print $2; exit}' "$f")
  if [ -z "$k" ] || [ ! -e "$k" ]; then
    echo "$f 'tamamlandi' ama gerçek etki kanıtı yok (Work closure ≠ actual effect)." >&2; exit 2; fi
done; exit 0
```

- Karar: **al.**

### E-M6 — Ölçüt-göreli durum kaydı (tek "status" alanı yok)

- Foundation: kalıp "current facts / characteristics + applicable criterion / regime / expected function + correct binding / scope → possible true criterion-relative standing" (E/DC STATE; "not a proposed implementation formula"); hata listesi "wrong criterion; wrong version; wrong scope/jurisdiction; wrong bearer binding; misunderstood expected function; ignored exception/waiver; incorrect institutional authority/regime." (E/CRS synthesis); NIST karşı-örneği: gerçek uygunluk ile karar kuralıyla kabul ayrışabilir (E/CRS STATE); "Later composition must support multiple simultaneously valid criterion-relative standings rather than one flattened `status` field." (E/CRS DEFERRED R9); "Do not encode representation and standing as the same thing merely for storage convenience." (R4).
- Sorun: "done/ready/passing" tek alan; hangi ölçüte, hangi sürüme, hangi commit'e göre olduğu kaybolur; yanlış ölçütle doğru test "geçti" der.
- Nasıl:

```yaml
durumlar:
  - olcut: "devos/kabul/IS-042.md@a1b2c3d"   # ölçüt dosyası + commit
    tasiyici: "commit 3f2a9c1"
    sonuc: karsiliyor            # karsiliyor | karsilamiyor | belirsiz (epistemik)
    yontem: "pytest -q tests/test_x.py → devos/kanit/IS-042/pytest.txt"
    degerlendiren: "dogrulayici (farklı bağlam)"
    zaman: 2026-09-27T14:05Z
  - olcut: "musteri-teslim-kabulu"
    tasiyici: "PR #12"
    sonuc: beklemede             # alanın kendi durumu; epistemik belirsizlik değil
    degerlendiren: Batu
```

- Karar: **al.** Ölçütün kaynağı/sürümü/yetkisi ayrı bağlamadır (E/CRS DEFERRED R1; OPEN-QUESTIONS Q2).

### E-M7 — Eksiklik ve belirsizlik sözlüğü

- Foundation: "actual fact is absent ≠ value not observed ≠ value unknown ≠ field missing ≠ criterion not applicable ≠ outside selected scope" + "The first can be reality-side. The others may depend on Information/reference semantics." (E/DC F04); "A domain may explicitly define `Unknown`, `Pending` or `Under Review` as a real institutional/operational standing; ... That must not be confused with the research system's uncertainty about which standing is true." (E/CRS F05); "present but unhealthy/unavailable must not be collapsed into absent from structure" (E/DSt DEFERRED R2).
- Nasıl: DevOS kayıtlarında izinli değerler: `yok` (gerçekte yok, gözlemle), `gozlenmedi`, `bilinmiyor`, `alan-eksik`, `uygulanamaz`, `kapsam-disi`; alan durumu `beklemede` ile epistemik `belirsiz` ayrı. Basit bir denetim betiği iş kayıtlarında boş alan ve serbest metin "?" arar.
- Karar: **al.**

### E-M8 — Rol değişimi: DevOS kendi üzerinde çalışırken

- Foundation: CI örneği "supports product-development Work → Work-Condition/TWE role; is being repaired → Domain/Effect role; can simultaneously provide limited diagnostic support during its own repair → both roles." (E/F07); "The same cluster can partly remain a support substrate while also being the repair target." (E/F09 H8); "target/support role is reference-relative; do not duplicate the same reality merely because its role changes." (E/DD DEFERRED).
- Sorun: DevOS kancalarını, settings'i, YETKI kaydını değiştiren iş, hem bu kontrolleri hedefler hem onlara tabidir; ajan kendini bağlayan korumayı gevşetebilir (A-M2 ile aynı yapı).
- Nasıl: bu işler Kademe 3 (A-M11); değişiklik ayrı rolce incelenir; kanca yapılandırmasının oturum ortasında yüklenip yüklenmediği [bilinmiyor; O11] olduğundan doğrulama yeni oturumda yapılır: SessionStart çıktısında yeni kanca işareti görülmeli (E-M10).
- Karar: **al.**

### E-M9 — Dinamik: odak iş olmadan değişen repo ve uzlaştırma döngüsü

- Foundation: "Domain Dynamics may: precede Work; continue during Work; continue after Work; occur without focal Work; be only partly changed by Work." (E/DD synthesis §7); Kubernetes: "controllers are non-terminating control loops that observe current state and act toward desired state" (E/DD ledger E7); STAMP: denetleyicinin süreç modeli gerçek durumdan sapabilir (E/DR ledger B4).
- Sorun: başka oturum, Batu ya da paralel alt ajan repoyu değiştirir; ajan eski zihinsel modelle iter.
- Nasıl: oturum başı (E-M2) ve her push öncesi `git fetch` + `git rev-list --count HEAD..origin/<dal>`; sıfır değilse önce uzlaştır. Döngü: istenen (STATE'teki plan) → gözle → karşılaştır → uygula → yeniden gözle.
- Karar: **al.**

### E-M10 — Bileşim ve örgüt: dosyada olan ≠ yüklenmiş olan

- Foundation: "actual composition ≠ BOM / SBOM / inventory / registry / architecture model / baseline / observation by identity" (E/CC STATE); NASA CM: "The need for consistency itself implies they are not identical." (E/CC synthesis §7); "actual relation/arrangement ≠ graph/map/diagram/model/observation" (E/RO STATE); tek repolu ve çok repolu oturumda yüklenenler farklı [BRIEF diyor].
- Sorun: `.claude/agents/` ve `.claude/hooks/` dosyaları var diye mekanizmaların o oturumda çalıştığı sanılır.
- Nasıl: SessionStart kancası `DEVOS-KANCALAR-YUKLU <zaman>` satırı basar; CLAUDE.md'nin ilk kuralı: "Bu satırı bağlamda görmüyorsan kancalar yüklenmemiştir; `kancalar-yok` koşulunu kaydet ve Kademe ≥1 eylem yapma." (tavsiye + algılama). Alt ajanların gerçekten kayıtlı olup olmadığını programla görmenin yolu [bilinmiyor; O11].
- Karar: **al.**

### E-M11 — Referans çerçevesi ve sınır: hangi repo, hangi kapsam

- Foundation: "State what environmental scope/configuration is being referred to and which changes matter to the protected analysis." (E/F07); "hidden or stale reference frame makes all later membership claims unstable" (E/F10 E1); sınır değişimlerinin yönetimi açık soru: "how later SOUL/Development OS reasoning should represent/govern/version boundary changes" (E/OPEN-QUESTIONS Q3).
- Nasıl: her iş ve her durum iddiası `kapsam: <repo>@<dal>` taşır; üç repo otoritesi (bootstrap §1: araştırma / soul-development-os / soul-production) tek belgede, sürümlü; sınır değişikliği bir karar kaydıdır.
- Karar: **al.**

### E-M12 — Nedensellik standardı: ders ve öğrenme kayıtları

- Foundation: "`Condition X existed when Work failed` does not establish `X caused the failure`." (E/WC DEFERRED §8); "pre/post change ≠ causal effect by itself" (E/DR synthesis §6); "observed structural mismatch ≠ established root cause" (E/DSt DEFERRED R10); Foundation genelinde: "stored lessons or changed code do not establish operative feedback, retained adaptation or benefit." (F/README).
- Sorun: öğrenme/instinct mekanizmaları eşzamanlılığı neden sayar ve yanlış kural üretir.
- Nasıl: ders şablonu alanları: `gozlem`, `iddia_edilen_neden`, `kanit_turu: yalniz-eszamanlilik | tekrar-uretildi | karsi-olgusal-test`, `guven`, `uygulama` (kural envanterine giriş türü), `yeniden_acma`. `yalniz-eszamanlilik` olan ders zorlanan kurala dönüşemez.
- Karar: **al.** O5/O7'nin öğrenme mekanizmalarıyla birleştirilmeli.

### E-M13 — Kurulum işi koşul üretir; üretildiği gözlenmelidir

- Foundation: "setup/provisioning activity → Work; resulting realized support surface → Work Condition for later Work; record that setup succeeded → Information; actor who authorized setup → Actors." (E/WC F05 H12); bootstrap: "File existence is insufficient." (DEVELOPMENT-OS-BOOTSTRAP §6).
- Nasıl: setup betiği sonunda bir hazır-olma raporu basar; E-M2/E-M3 yoklaması bunu gözlemle doğrular; "betik var" hiçbir yerde "ortam hazır" diye yazılmaz.
- Karar: **al.**

---

## 5. Dersler (ne yanlış gitti, kök neden, önlem)

**L1 — Yönlendiricilerde durum sürüklenmesi.** Gözledim: 8 düğümde 17 yönlendirici dosya "awaiting user evaluation" türü etiket taşıyor, ilgili STATE "accepted" diyor: E/CR {INDEX, KEY, CURRENT-SURFACES}; E/DD FINDINGS-MAP; E/DS FINDINGS-MAP ("Current authorized work is user evaluation of the bounded Domain Condition result only"); E/RC {INDEX, KEY, FINDINGS-MAP}; E/DSt {INDEX, KEY, FINDINGS-MAP, CURRENT-SURFACES}; E/CC {INDEX, KEY, FINDINGS-MAP}; E/RO FINDINGS-MAP; E/WC FINDINGS-MAP. Ayrıca E/DR FINDINGS-MAP ağacı hâlâ "discovered; inactive" gösteriyor; E/DSt OPEN-QUESTIONS Q10 "Neither discovered child has been deep researched." diyor. Yöntem, KEY/FINDINGS-MAP/CURRENT-SURFACES'ın güncel olmasını istiyor (M/ §Pass-artifact provenance), yani bu kendi kuralına göre sürüklenmedir. Üst düzey aynı hatayı 2026-09-16'da düzeltmiş ("That was an early-child checkpoint, not missing research.", E/FINDINGS-MAP) ama alt düğümlere inmemiş. Kök neden: aynı değişken olgunun birden çok yüzeye kopyalanması (bootstrap §1'in "Do not create multiple authoritative copies of the same fact" kuralının ihlali). Önlem: tek durum yüzeyi; yönlendiriciler durumsuz; tutarlılık betiği (taslak):

```bash
# devos/araclar/durum-tutarlilik.sh — durum sözcükleri yalnız devos/STATE.md'de geçer
if grep -rnE 'DURUM:|AWAITING|ACCEPTED|beklemede|tamamlandi' devos --include=INDEX.md --include=KEY.md; then
  echo "Yönlendiricide durum kopyası var; durum yalnız STATE.md'de tutulur." >&2; exit 1; fi
```

**L2 — Eski kapanış güncel tamamlanma değildir.** "historical parent closure ≠ current ground completion after deeper child discovery." (E/CR synthesis §1); ayrıca "probe child enough to validate promotion ≠ substantive child pass" (E/CR F02). Önlem: DevOS'ta "bitti" iddiası, sonradan açılan alt işlerle yeniden değerlendirilebilir durumdadır; kapanış kaydı "hangi bilgiyle kapandı"yı (commit) taşır.

**L3 — Plan adımlarını bitirmek tamamlanma kanıtı değildir.** "The review must not equate traversal of the planned sequence with completion." (E/ENVIRONMENT-COMPLETION-REVIEW-PLAN); "Structure → Condition traversal is process history, not evidence that Environment is complete." (E/CR COMPLETENESS F17). Önlem: DevOS kapanışı E-M5 kanıtına bağlanır, kontrol listesi işaretine değil.

**L4 — Aynı model incelemesi ve kullanıcı kabulü doğrulama değildir.** Her düğümde açık etiket (A/STATE; E/STATE; tüm COMPLETENESS). Önlem: A-M5 bağımsızlık alanı; Batu kabulü teknik doğrulama yerine geçmez (A-M4).

**L5 — Yalnız yerel izin modeli çöker.** Anthropic SDLC olayı: yetkisiz ajan daha güçlü aktöre ulaştı; "It falsifies a local-permission-only model" (A/A3 §2.3). Önlem: A-M2 alternatif yol envanteri ve algılama katmanı.

**L6 — Ortak soydan kanıt bağımsız değildir.** YZ destekli SEBoK sayfalarının dışlanması (E/DD F04; E/DS COMPLETENESS §5). Önlem: DevOS araştırmasında YZ üretimi kaynak işaretlenir; yük taşıyan karar ona tek başına dayanmaz (M5).

**L7 — Araştırma vardı ama doğru anda uygulanmadı.** Foundation'ın soru bankası tartışması: "The observed omission is evidence that available research need not be applied at the right time." (F/STATE §Important correction). Bu kapsamın dışı (F3/F4) ama DevOS için doğrudan: Foundation ayrımları iş türüne bağlı tetiklerle (iş kaydı şablonundaki alanlar, E-M1…E-M7) işe taşınmalı; yalnız okunabilir olmaları yetmez [çıkarım].

**L8 — Her adımda kullanıcıya dönmek.** Foundation her düğümde kullanıcı değerlendirmesine döndü (M13) ve bunun doğrulamayı güçlendirmediğini kendisi yazdı. DevOS'ta Batu teknik koordinatör/doğrulayıcı değildir (BRIEF; bootstrap §6). Önlem: kapılar DevOS içindeki yetkili ve bağımsız rollere; Batu'ya yalnız hedef ve teslim kabulü (A-M4, A-M9) [çıkarım].

**L9 — "status" sözcüğü aşırı yüklü.** Foundation "Status"u iki düğüm etiketinden çıkardı: "lifecycle state, API/report/database fields, institutional status and generic condition vocabulary" (E/CRS STATE); `Domain Condition ≠ every thing called "status"` (E/DC F01). Önlem: DevOS kayıtlarında çıplak `status` alanı yok; `is_durumu` (iş), `kosul` (ortam), `durumlar` (ölçüt-göreli) ayrı (E-M4, E-M6).

---

## 6. Foundation'ın açık bıraktığı, DevOS'un kendi bağlamında karar vermesi gereken sorular

Bunlar Foundation'a geri dönülecek araştırma değil, DevOS tasarım girdisidir. REUSE, somut bir çelişkiyi ilgili sonuca taşımayı ister ama her tasarım bilinmezini araştırılmamış bir Foundation çocuğu saymamayı da söyler: "… rather than force a fit, rebuild the entire library or treat every design unknown as an unresearched Foundation child." (F/08/REUSE).

- Ajan örneklerinin sürekliliği ve rol/oturum ilişkisi (A/OPEN-QUESTIONS Q1, Q12) → A-M6.
- Hangi yetkinlik ayrımları DevOS rolleri için yük taşır (Q3) → A-M12.
- İzin/yetki/vekâlet sözlüğünün ne kadar ayrıntılı olacağı (Q4) → A-M1 alanları.
- Etkili yetkinin hesaplanması (Q5; A/DEFERRED §4) → A-M2; F3 Control sonuçlarıyla.
- İhmalin temsili (Q8) → A-M13.
- İnsan-dışı eşik: DevOS'un kendisi ne zaman "kalıcı taşıyıcı" sayılır (Q10) → hesap verebilirlik konumu iş kaydında rol olarak.
- Önemlilik eşiği (E/OPEN-QUESTIONS Q2; E/WC OPEN-QUESTIONS Q2) → E-M3.
- Sınır değişikliklerinin sürümlenmesi (E/OPEN-QUESTIONS Q3) → E-M11.
- Nedensel kanıt standardı (E/OPEN-QUESTIONS Q4; E/DR OPEN-QUESTIONS Q6) → E-M12.
- Durum yeterliliği ve geçmiş (E/OPEN-QUESTIONS Q7; E/DD OPEN-QUESTIONS Q4) → STATE'in hangi olguları taşıyacağı.
- Hazırlık/yeterlilik yargısının korunan işe bağlanması (E/OPEN-QUESTIONS Q9; E/WC OPEN-QUESTIONS Q4) → E-M3.
- Durum iddiasının eyleme yetecek kadar güncel sayılma standardı (E/DS OPEN-QUESTIONS Q7; E/DC OPEN-QUESTIONS Q5: "what verification standard is required before SOUL acts on a standing claim") → E-M2 + E-M6.
- Ölçüt bağlama ve çoklu ölçüt (E/CRS OPEN-QUESTIONS Q2, Q3) → E-M6.
- `Unknown/Pending` tiplemesi (E/CRS OPEN-QUESTIONS Q5) → E-M7.
- Çelişen envanterler ve iz tabanlı bağımlılık haritalarının kanıt eşiği (E/CC OPEN-QUESTIONS Q7; E/RO OPEN-QUESTIONS Q5) → E-M10.

---

## 7. Diğer notlarla bağlantı

- F4: TWE (`F/01_verticals/work-environment`) okunmalı; E-M2/E-M3/E-M10'un ayrıntısı oradadır (support closure, declared/discovered/actual, readiness, identity/equivalence). Önceki Aktörler külliyatının kaynakları (W3C PROV, NIST RBAC/ABAC, RFC 8693; A/A4) A-M1/A-M10 biçimlerini besleyebilir.
- F3: etkili yetki ve kontrol "later relation/control composition" olarak 05'e devredildi (A/A6 §5; A/DEFERRED §4); A-M2 ve A-M11, F3'ün Binding/Control sonuçlarıyla birleştirilmeli.
- F1: Work zemini "Work acceptance state", "admission", "blocked" kavramlarının sahibidir; A-M3/A-M4/E-M4 alanları F1'in iş döngüsü mekanizmalarıyla tek iş kaydı şablonunda birleşmeli.
- O11: kanca olayları, girdi alanları (`tool_name`, `tool_input`, `stop_hook_active`, alt ajan kimliği), izin kuralı sözdizimi, SessionStart çıktısının bağlama girişi, oturum ortasında kanca değişikliği davranışı. Bu notun kod taslakları bu noktalarda O11'e bağlıdır.
- O5/O7: öğrenme ve bellek mekanizmaları E-M12'nin kanıt türü alanıyla sınırlanmalı.

---

## 8. Kendi yargım ve alınmayacaklar

- Foundation'ı reçete saymıyorum: kendi kuralı "A branch does not require a module, service, agent or database field." (F/README) ve "A role need does not imply an AI agent, and an instruction need does not imply that a particular file enforces it. … Conversely, a simpler arrangement is not adequate merely because it is simple." (F/08/REUSE). Yukarıdaki her mekanizma, bir Foundation ayrımı ile DevOS'ta gerçek bir hata biçimi birleştiğinde öneriliyor; ayrımın kendisi mekanizma istemiyor.
- Alınmayacaklar: (1) dört zemini klasör/ajan/servis yapmak (E/README; A/A6 §9: "Do not manufacture an immediate-child hierarchy merely to mirror Environment or Information."); (2) düğüm başına yedi yönlendirici ve blob-SHA manifestleri (L1, M7); (3) her kararın kullanıcı değerlendirmesine dönmesi (L8); (4) Foundation hiyerarşisinden ontoloji, şema, graf veritabanı çıkarmak (E/RO DEFERRED: "Do not infer … a graph database; pairwise edges only; hypergraphs; a separate topology service; a universal relation table").
- Öncül düzeltmesi: BRIEF, Foundation okuyucularına "hangi sonuç hangi mekanizmaya" diye soruyor. Bu iki zeminde sonuçların çoğu "şunu şununla karıştırma" biçiminde; bu yüzden en değerli çıktı yeni bileşen değil, kayıt biçimlerinde ayrı alanlar ve zorlama/algılama noktalarıdır. En büyük risk yeni bir "Aktör servisi" ya da "Ortam ajanı" kurmak değil, tek alanlı `status`, tek katmanlı izin ve kanıtsız kapanıştır.
- Kanıt durumu: yukarıdaki mekanizmaların hiçbiri koşturulmadı; çalıştığı iddia edilmiyor. Foundation'ın kendi mekanizmaları için "kaynak diyor" ve "gözledim" etiketleri kullanıldı; DevOS'a uyarlamalar "çıkarım"dır.
- Foundation kullanım kaydı (F/08/REUSE "minimal use record"): DevOS tasarım belgesinde her Foundation atfı için hedef soru, tam yol/bölüm, uygulanabilirlik ve karşı durum, etkilediği seçim ve eksik hedef kanıtı yazılmalı; bu not o kaydın ham malzemesidir.
