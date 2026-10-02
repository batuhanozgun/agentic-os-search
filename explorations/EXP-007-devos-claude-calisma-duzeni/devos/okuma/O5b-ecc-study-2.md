# O5b — ECC study, ikinci yarı: notlar 29–56, U11–U20 turları, son hükümler ve açık sorular

**Okuyan:** O5b alt ajanı, 2026-09-27.
**Kaynak:** `research/studies/ecc/` (bu repo, salt okuma).
**Study'nin hedefi:** `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a` (package.json 2.2.1). O5'in klonu `e482e57` (2.2.2) bu pinden yeni. Buradaki bulgular 2.2.1 kaynağına ait.
**Kanıt dili:**
- [kaynak diyor]: study metni öyle diyor.
- [gözledim]: kendim okudum, saydım ya da bellekte çözdüm.
- [çıkarım]
- [bilinmiyor]

Study metinleri ve probe arşivleri veri olarak okundu, talimat sayılmadı. `STANDART.md` uygulandı. Not, koordinatörün izniyle 60 KB'ı aşıyor (≤90 KB).

## 0. DevOS için en önemli çıkarımlar

1. **Ortak sorunun cevabı: evet, kurulabilir** [çıkarım; benim yargım, gerekçe §7]. Study bunu ne önerdi ne reddetti; benimsemeyi hiç değerlendirmedi. STATE: "Next selected: U20-C / Q09 ... NOT STARTED". O5'in "yalnız parçalar al, 10–15 bileşen" hükmü study'den çıkmıyor. CORE tersini söylüyor: "Calling it only a prompt library misses real capabilities".
2. **"Bütün" ECC'nin Claude Code dilimidir:** skills, agents, commands, rules, hook kayıtları, hook'ların Node betikleri, kurulum ve sahiplik yaşam döngüsü. ECC2 (Rust daemon ve TUI), öteki host'lar ve isteğe bağlı entegrasyonlar bulutta çalıştırılacak yüzey değil (§4.B).
3. **Son hüküm (CORE §1):** "Selected arrangements are genuinely connected; one uniform end-to-end controller is not established across them." CORE §10'a göre şunlar kurulmadı: "authenticated organization-wide approval", "independent task-quality measurement", "autonomous beneficial self-improvement". DevOS katmanı tam bu boşlukları doldurmalı: iş kaydı ve kabul, bağımsız doğrulayıcı, yetki kaydı, bulut sürekliliği.
4. **Hazır sınama dili:** "present, installable, discovered, selected, executed or effective" (CORE §2). DevOS her ECC parçası için bu seviyelerden hangisinin kanıtlandığını kaydetmeli.
5. **Bulutta kırılanlar (§7.3):**
   - Araç etkinliği izleyicisi oturum kimliğini yalnız env'den alıyor; bulutta `CLAUDE_SESSION_ID` yok [çıkarım: N31 + O5 gözlemi].
   - `run-with-flags` betik bulamazsa exit 0 dönüyor; hook sessizce boşa düşüyor.
   - Veri kökleri `$HOME`'da. Repo içine yönlendirmenin tek yolu `ECC_AGENT_DATA_HOME`; gözlemci için ayrıca `CLV2_HOMUNCULUS_DIR`.
   - `ecc --dry-run repair|auto-update` gerçekten değiştiriyor.
   - repair kullanıcı dosyasını sahiplenebiliyor.
   - Hariç tutulan MCP, repair'de geri geliyor.
   - `harness-audit` her zaman exit 0 dönüyor.
6. **Düzeltme deseni:**
   - Commit ve paket digest'iyle pinle; auto-update kullanma.
   - Kurulumu DevOS betiği yapsın: ECC installer'ın Claude proje hedefi, açık hook onayı ve taşınabilir kök.
   - Bulutta anlamsız hook'ları `ECC_DISABLED_HOOKS` ile kapat.
   - Her etkin hook için "tetiklendi mi, iz bıraktı mı, modele ulaştı mı" testi koy.
7. **İnsan kapıları yeniden bağlanmalı.** CORE §9, plan onayını, TDD kanıt yargısını ve PR kararını "Intentionally actor-mediated" sayıyor. Batu doğrulayıcı değil (K-015). Bu yüzden her kapının geçiş koşulu açıkça bağımsız doğrulayıcı ajana ve deterministik teste yazılmalı. N54: "preserving a command label and broad intent does not establish preservation of its transition condition".
8. **Kanıt düzeyi:** kaynak okuması ve 3 yerel probe (E08, E09, E10); üçünü bellekte yeniden doğruladım. ECC hiçbir gerçek host'ta ya da modelle koşmadı, kendi testleri çalışmadı. "effective" düzeyinde kanıt yok. Açık soruların hepsi aynı türden: kurulu host uyumu, eşzamanlılık ve çökme, doğrulanmış yetki, kabul edilmiş yararlı sonuç.
9. **E08 (ECC'nin native review workflow'u, bir Claude Code dynamic workflow):**
   - Aynı kanıtlı iki bulgu önce MEDIUM sonra CRITICAL gelirse birleşik bulgu kanıtını kaybediyor, doğrulayıcı onu çürütüyor ve sonuç APPROVE oluyor. Ters sırada CHANGES_REQUESTED [gözledim].
   - "CHANGES_REQUESTED + boş bulgu" da, diff olmayan metin de APPROVE alıyor.
10. **METHOD-CASE, DevOS'un yazma disiplinini belirliyor.**
    - Paylaşılan dosyayı baştan yeniden üretmek, 40 birimin ~24'ünde ilgisiz satırları bozdu [gözledim: makbuz sayımı].
    - Benim yarımdaki üç probe'un üçünde de kanıt aktarımı bozuldu.
    - Diff kapısı bozulmayı yakaladı ama önlemedi: "recovery is not prevention".
    - Kural: cerrahi düzenleme, dokunulmayan içeriğin aynı kaldığını denetleyen kapı, nesne yeniden kullanımı, force yok.
11. **Yeniden giriş kanıtlanmadı:** "No qualifying conversation-independent repository-only test ... was recovered" (STATE).
    - U18-B'de "Batu requested continuation in a new conversation" deniyor ve iş repodan sürüyor. METHOD-CASE bu kaydı incelememiş [gözledim].
    - Önceden belirlenmiş olguları, cevabı verilmeden bulan bir test yok. DevOS bunu kurulum kabul ölçütü yapmalı.
12. **Study'yi ChatGPT yürüttü, GitHub connector ile** ("OpenAI blocked the call ..."). Yayın hataları Claude Code'un Edit aracına birebir taşınmaz, ama kök neden aynı: büyük metni yeniden üretmek [çıkarım].

## 1. Kapsam

### Tam okunanlar (kapsamım)
- `notes/29…56`: 28 not.
- `ROUND-U11-A … ROUND-U20-B`: 40 dosya.
- `PUBLICATION-U11-A … PUBLICATION-U20-B`: 42 dosya, `U17-A-ALIGNMENT` ve `U18-C-ALIGNMENT` dahil. Ayrıca `PUBLICATION.md` (U00–U03-A).
- `evidence/U11-A-SOURCES … U20-B-SOURCES`: 40 kaynak defteri.
- Probe dizinleri:
  - `u11-a-review-flow-probe/`: README, PRECHECK, `probe.cjs`, 4 parça.
  - `u12-c-python-flow-probe/`: README, PRECHECK, `E09.zip.b64`.
  - `u17-a-guidance-adapter-probe/`: README, PRECHECK, `restore_e10.py`, `recovery-check.json`, `E10.zip.b64`.

### Bellekte çözülen arşivler [gözledim]
Repoya dosya yazılmadı. `restore_e10.py` çalıştırılmadı; varsayılan olarak repoya `E10.recovered.zip` yazıyor. Aynı ekleme, satır içi Python ile bellekte yapıldı.
- **E08:**
  - 4 parça → gzip → 101.725 bayt JSON.
  - `run` üst verisi, 18 senaryonun `input/outcome/error` alanları ve `schema_check` okundu (38 yanıt, hepsi geçerli).
  - `calls/logs` alanları bir senaryoda (`medium_then_critical_same_evidence`) tam okundu. Öteki 17 senaryo aynı istem şablonunu kullanıyor; onların istem metinlerini satır satır okumadım.
- **E09:**
  - base64 blob `02441842…`; zip 6.598 bayt, sha256 `f70acdf4…`.
  - Tam okunanlar: MANIFEST, `probe.py`, `results.json`, `exit-code.txt` (0), `stderr.txt` (boş).
- **E10:**
  - Bozuk blob `3b92e3eb…` doğrulandı.
  - 259–356 aralığı ekleme dizgisiyle değiştirilince blob `4d96ed1e…` tuttu: 8.821 bayt, sha256 `d16d24c6…`. `testzip` temiz.
  - Altı üyenin hepsi tam okundu: README, `run_e10.py`, `E10-results.json`, `source-identity.json`, `gemini-adapt-agents.js`, `agent-tools.js`.

### Son hükümler ve açık sorular için ayrıca tam okunanlar
Bunlar O5a ile örtüşüyor:
- `CORE.md`, `STATE.md`, `METHOD-CASE.md`
- `QUESTIONS.md`, `QUESTIONS-THROUGH-U19-C.md`
- `inventory/U15-A-COVERAGE-RECONCILIATION.md`, `inventory/U19-A-OMISSION-REVIEW.md`
- `O5-ecc.md`, `BRIEF.md`, `STANDART.md`, `KAPSAM.md`

### Kapsamım dışında kalanlar
Gerekçe: BRIEF bunları O5a'ya verdi; konu dışı değiller.
- `notes/01…28`
- U03-B…U10-B arası ROUND ve PUBLICATION dosyaları; `PUBLICATION-U08-A-RECOVERY`
- `evidence/U01…U10-SOURCES` ve `u01…u09` probe dizinleri
- METHOD, METHOD-REVIEW, PLAN, INDEX, META, RESEARCH-LOG, SOURCE-LEDGER, 00-WHY, RECOVERY-U08-A
- `inventory/` altında STRUCTURE, TREE-FRONTIER, U01-B-DISCOVERY, U07-A-FAMILY-MAP

ECC kaynak kodunu okumadım (O5c ve O5d'nin işi). Buradaki kod bilgisi study'nin alıntılarından geliyor.

### Study'nin kendisinin okumadıkları [kaynak diyor]
Sonuçlar bunlara dayanamaz.
- Hiçbir görsel görülmedi: "Images were not viewed" (U19-H).
- ROADMAP'in 761–849. satırları okunmadı.
- Lifecycle testinin yalnız 1–1085. satırları okundu (U16-A1).
- `session-end.js`'in içe aktardığı `llm-summary` denetlenmedi (U19-C).
- CORE'un iddia haritası bazı notları yalnız seçili aralıklarla geri çağırıyor: örneğin N20 1–55, N24 1–75 (U20-A-SOURCES).
- Workflow SDK sayfası boyut sınırı yüzünden alınamadı (U11-A).

### Atanmamış kaynak [gözledim: `ls`]
- `concepts/studies/ecc/` (34 dosya, 732 KB): study'yle eşzamanlı yürüyen ECC terim çıkarımı (TERMS-*, C6-*). PUBLICATION makbuzları bu klasöre giden eşzamanlı commit'leri anıyor.
- Hiçbir okuma notu bu klasöre değinmiyor; KAPSAM'da da yok. Ana oturumun bilgisine.

## 2. Study'nin kimliği, yöntemi ve durumu

### Yürütücü
Study'yi ChatGPT (OpenAI) yürüttü, GitHub connector ile [kaynak diyor]. Kanıtlar:
- PUBLICATION-U17-A: "OpenAI blocked the call because it could not determine the request's safety status".
- N39: "The cause of the ChatGPT thinking failure is not established by this transfer defect".
- PUBLICATION-U19-B: "Batu reported that the preceding response ended with a thinking failure".

Probe'lar `/mnt/data/...` konteynerinde koştu. Ham GitHub indirmesi sürekli DNS hatası verdi (U11-A, U11-B, U19-D).

### Zaman ve sürüm
- Notlar 29–56, CORE ve METHOD-CASE 2026-09-20…25 arasında yazıldı.
- PLAN 0.60'a çıktı, METHOD 0.1'de kaldı.

### Her ROUND'da aynı protokol
1. Taze `AGENT` ve R01–R09 protokolleri okunur; main ve STATE blob'u karşılaştırılır.
2. Önceki birimin kapandığı teyit edilir: "not a repair/upload task".
3. Asıl işten önce açılış MR commit'i ve STATE aktivasyonu yapılır; dönüş ölçütü önceden yazılır.
4. Not ve kaynak defteri yazılır, blob kimliğiyle tam geri okunur.
5. Ardından PLAN, QUESTIONS, INDEX, META, ortak CATALOG satırı, makbuz ve kapanış STATE'i gelir. Bu adımlar önceden "yapıldı" sayılmaz: "subsequent actions ... not preclaimed".

### Main'e yazım (U11-D'den sonra)
1. Main'i oynatmadan aday ağaç ve commit kurulur.
2. Gerçek commit diff'i okunur.
3. Aday commit'in parent'ının main'le aynı olduğu denetlenir.
4. `update_ref(force=false)` yapılır.
5. 422 dönerse taze parent üzerine yeniden kurulur. Force kullanılmaz.

### Kanıt sınıfları
- Kaynak gözlemi.
- "tests inspected, not run".
- Koşullu çıkarım: "Source countercases are not observed incidents".
- Yerel probe.

Benim yarımda yalnız E08, E09 ve E10 koştu. Üçü de yapay girdiyle, sahte ajan ya da sağlayıcıyla koştu.

### Duruş
- U15-C: "The imagined SOUL was not ECC's acceptance oracle."
- ECC'nin iki türlü makinesi var: "ECC contains machinery for operating development work and machinery for developing/distributing ECC itself" (N33). Yayın, hazırlık panosu ve tarayıcı ikinci türe ait.

### Durum (STATE, U20-B kapanışı)
- "Study: ACTIVE / PARTIAL ... **General method validation is unproven**".
- "Neither deliverable authorizes adoption, upstream repair, other-product research or SOUL/Development OS architecture."
- Sıradaki birim (U20-C) başlamadı. Sorusu: "what can these two research deliverables contribute to actual current SOUL/Development OS questions, and what must remain a conditional reference, countercase or unresolved adoption issue?"
- Beklenen ayrım: "Separate reuse as source reference, falsifier, design pressure, implementation/testing example and a proposal needing further evidence."

Yani ortak sorumuz, study'nin sıradaki ama başlamamış birimi. §7.4 bu ayrımı DevOS için uyguluyor.

## 3. Son hükümler

### 3.1 CORE (U20-A, "SOURCE-SYNTHESIS CANDIDATE v0.1")

**Merkez cevap:** "ECC combines reusable operating procedures and host-specific deployment with several implemented work, execution, information, review and control arrangements. Selected arrangements are genuinely connected; one uniform end-to-end controller is not established across them."

**Birim:** "selected combination of entry point, installed assets, host, controller, store and responsible actor".

**§2: Her sorumluluğun yanında kalan koşul.** Örnekler:
- Yöntemler: "A selected host/agent must discover, interpret and follow them; the relevant human owns the procedure's sign-offs".
- İş kaydı: "A record is not itself an allocated process or accepted task; the particular dispatcher must run".
- Denetim: "Each control measures or governs a particular object; its result must reach the correct next consumer".

**§3.3:** "The host remains an active part of the system" ve "Portability is a collection of specific translations and dependencies, not a property proved by shared names."

**§4: İş yolculuğu.** "analytical composition of available routes, not a claim that one default command automatically performs all stages". Öne çıkan cümleler:
- "Neither written TDD guidance nor a running process is a task-quality certificate."
- "A script-level `APPROVE` is not authenticated user consent or proof that every required review dimension was selected. Finding aggregation must also preserve the evidence carrying the finding."
- "Mechanical merge readiness is not synonymous with semantic acceptance".
- "A synthesis that removes the actor-owned steps would invent automation; one that ignores the real software would understate ECC."

**§5.3:** "Even a native allow-tools option may concern preapproval rather than removal of all other tools."

**§6:** "These mechanisms should not be collapsed into one memory database or one trust ladder." Her kayıt için sorulacaklar: "who wrote the record; which scope and version it represents; what is eligible for recall; what the final consumer receives; and which decision that content can influence".

**§7.2: Altı değerlendirme yüzeyi** (scorecard, skill yardımcısı, Rust registry, Node capsule, prototip, native review). Hiçbiri görev kalitesini ölçmüyor.

**§7.3:** "Authority is not a label carried by a record". GateGuard için: "releases a repeated key based on its saved encounter marker, not a checked investigation response."

**§8:** "General JSON subtraction does not reconstruct an overwritten prior value unless a producer actually supplied the relevant snapshot."

**§9: Dört bağlantı türü.**
1. Dar sözleşmeli ama gerçek.
2. Anlamı değiştiren: birikimli maliyet artım gibi toplanıyor.
3. "Intentionally actor-mediated": "Plan confirmation, Canvas feedback interpretation, TDD evidence judgment and PR decision".
4. İzlenen yolda "Not established".

**§10:** Kurulmamış olanlar: "universal host/domain/translation parity; ... authenticated organization-wide approval; crash/concurrency guarantees beyond inspected predicates; complete observation; independent task-quality measurement; or autonomous beneficial self-improvement."
- Uyarı: "For a current deployment decision, revalidate the relevant upstream and host/runtime rather than treating this historical pin as current certification."
- Sınır: CORE, "must not turn candidate mechanisms into Foundation truth or adopted architecture".

### 3.2 METHOD-CASE (U20-B)

**Hüküm:** "Retain the mechanism/consumer-oriented research discipline and proportional counter-tests. Do not carry the publication workflow forward unchanged." Kurulmayan: "best, efficient, independently validated or universally reusable research method".

**Olumlu zincir (Case A):** U15-A'nın geçici sentezi eksik bir teslim ilişkisi buldu. U15-B birleştirmeyi temizlik yoluna kadar izledi ve sistem açıklamasını değiştirdi.

**Olumsuz zincir (Case C, E):** E06'dan E10'a, sonra katalog onarımları. "Detection and recovery improved the admissible evidence; they did not demonstrate prevention."

**Case B, küçük ayırt edici probe'lar:** "Do not run a test just to increase the experiment count, and do not combine heterogeneous probes into one efficacy score."

**Case D:** "It does **not** demonstrate that a fresh agent with no conversation context selected the correct task from the repository alone." Önerilen test: "recover a small predefined set of facts without being supplied the expected answers".

**Case E:** "Prefer exact-source transformations with narrow accepted changes and assertions that untouched content stayed identical. Reuse immutable objects instead of regenerating them."
- Asgari kalıcı roller: "current state, original evidence, an interpretation/change record, retrieval pointers and a publication check".
- Aktarım koşulu: "source bytes → transfer → destination bytes → readable members → reachable repository files before execution evidence is admitted."

**Case F:** "Reject file-count completeness and the opposite rule that every unrun live test must block a bounded source conclusion."

**Aktarım tablosu:**
- RETAIN: kaynak kimliği ve üretici→tüketici izi; küçük ayırt edici probe'lar; kalıcı checkpoint ve force'suz yayın; tek düzeyli soru mirası; ilişki sınırı incelemesi.
- CHANGE: bütün dosyayı üreten yayın yolu.
- WITHHOLD: verimlilik, bağımsız süreklilik, en iyi yöntem.

### 3.3 QUESTIONS ve STATE
- Q01: "PARTIAL / NATIVE ANSWER U20-A".
- Q09: "SELECTED U20-C / NOT STARTED".
- Q10: "BOUNDED RETROSPECTIVE U20-B; STRONGER VALIDATION UNPROVEN".
- "whole-study/user acceptance remains open".
- QUESTIONS.md yalnız değişen satırları tutuyor. Q02–Q08'in ayrıntısı `QUESTIONS-THROUGH-U19-C.md`'de, blob `da764c97…`.
- Açık kalanların listesi §8'de.

## 4. Mekanizmalar (kapsamımdaki notlar)

### 4.A Claude Code bulutuna doğrudan değenler

#### M1. Paylaşılan Claude ayarlarının sahipliği (N38; U16-A2)
- **Sorun:** ECC hook'larını `settings.json`'a ekleyip sonra güvenle yükseltmek ve kaldırmak.
- **Nasıl işler** [kaynak diyor]:
  - Kayıtlar `hooks/hooks.json`'da. Yan dosya `hooks.metadata.json`: "stable IDs/descriptions aligned by event and position; a short SHA-256 fingerprint of matcher and handler content". Sayı, olay ya da yinelenen kimlik uyuşmazsa birleştirme reddediliyor.
  - Birleştirme: eksik kayıt ekleniyor; birebir aynısı benimseniyor; değişmiş kayıt yalnız önceki kayda eşitse yükseltiliyor; beklenmedik değişiklik reddediliyor.
  - Uninstall: "The actual uninstall helper keys by event plus ID and removes only exact recorded entries".
  - Yazıcı işbirlikçi kilit kullanıyor: hard link; 5 dakikadan eski ya da ölü PID'li kilit kurtarılıyor. Ardından no-follow anlık görüntü, rename'den önce yeniden kontrol, en çok 3 deneme. "These controls are nevertheless local and cooperative."
  - "Materialization rewrites the plugin-root placeholders and the recognized environment-reading command prologue to the actual target root. Unresolved root reads are refused."
  - Handler'lar hedef kökteki `scripts/hooks/plugin-hook-bootstrap.js`'e başvuruyor (U16-A2 defteri).
- **Yollar (defter adları):** `claude-settings.js`, `claude-settings-lock.js`, `atomic-write.js`, `hooks-config.js`, `install-state.js`, `mcp-config.js`.
- **Sınırlar:**
  - "preserved configuration text plus a removed local dependency": değiştirilmiş hook kalıyor, bağımlı betik silinebiliyor.
  - JSON çıkarma eski değeri geri getirmiyor. Önceden A varken ECC B yazdıysa, kaldırma B'yi siliyor ama A'yı geri koymuyor.
  - `ECC_DISABLED_MCPS` kurulumda süzülüyor, ama `mergePayload` süzülmemiş haliyle saklanıyor. Repair, hariç tutulan sunucuyu geri getiriyor (`chrome-devtools`, `@latest`).
- **Kanıt:** üç test dosyası incelendi, koşulmadı.
- **Bulut:**
  - Proje `settings.json`'u commit'li olacağı için sahiplik yan dosyası da commit'lenmeli [çıkarım].
  - O5, kökün mutlak yol olarak (base64) yazıldığını gözledi. Sabit bulut yolunda çalışır, başka klonda bozulur. `$CLAUDE_PROJECT_DIR` daha taşınabilir [çıkarım; O5c doğrulamalı].
- **DevOS kararı: al.**
  - Sahiplik defteri DevOS hook'larına dokunmuyor; ayrı ID kullanılırsa çakışma yok.
  - ECC'den önce var olan ayar değerleri DevOS makbuzuna yazılsın.
  - repair kullanılmasın. MCP listesi her bakımdan sonra doğrulansın.

#### M2. Kurulum yolu: consult → plan → install ve hook onayı (N42; U18-C)
- **Sorun:** ihtiyacı bileşen, profil ve modül seçimine çevirip hedefe kurmak.
- **Zincir** [kaynak diyor]: "query + target → local manifests/skill-directory catalog → lexical ranking → command strings → caller invokes plan/install → normalized configuration + dependency/adapter resolution → materialized operations → guarded application/state".
- **Nasıl işler:**
  - `ecc consult` "catalog discovery, not requirements discovery". Olumsuz cümleyi anlamıyor.
  - Birçok bileşen kimliği aynı geniş modüle (`framework-language`) düşüyor. Örneğin react'i dışlamak nextjs'i de dışlıyor.
  - Hedefin desteklemediği bağımlılık sonradan eleniyor: Next.js Codex için öneriliyor, sonra `rules-core` yüzünden atlanıyor.
  - Üç ayrı "plan" var: consult'un metin önerisi; `ecc plan` (projectRoot varsayılanı ECC paket kökü); `ecc install --dry-run`. Üstelik "`ecc install` ... does not ingest the preceding plan report as an immutable approved artifact".
  - Hook onayı: "`applyInstallPlan` invokes `assertHookConsentReady` before its apply body. If the resulting operations would materialize hooks and consent is not enabled, it raises with a capability disclosure and explicit enable/decline choices."
  - Önerilen komutlar sürümsüz: "`npx ecc-universal` without a version. The pinned package declares version2.2.1".
- **Yollar:** `consult.js`, `ecc.js`, `install-plan.js`, `install-apply.js`, `hook-consent.js`, `config.js` (`ecc-install.json`), `install-profiles.json`, `install-components.json`, `install-modules.json` (U18-C defteri).
- **Kanıt:** kaynak ve test tanımları incelendi; kurulum koşulmadı.
- **DevOS kararı: uyarlayarak al.**
  - consult ihtiyaç analizi sayılmasın.
  - Kurulum sabit sürüm ve commit ile, proje kökünden (cwd) koşsun.
  - Hook onayı açıkça verilsin ve makbuza yazılsın.
  - Dry-run çıktısı onaylı plan sayılmasın. Kurulumdan sonra gerçek dosya listesi makbuzla karşılaştırılsın.
  - Bağlam maliyetini ECC'nin kendi profil ve modül sistemiyle ayarlamak "parça seçmek" değildir; ECC'nin mekanizmasını kullanmaktır [çıkarım].

#### M3. Bakım: doctor, repair, auto-update, uninstall (N37; U16-A1)
- **Nasıl işler** [kaynak diyor]:
  - Doctor, kaydedilmiş `contentSha256`'yı kurulu baytlarla karşılaştırıyor; güncel kaynakla karşılaştırmıyor. Kayıt yoksa "checkedCount=0, exit0": "an empty checked population is not a successful installed-system inspection".
  - Repair, kurulumun atladığı kullanıcı dosyası F'yi sahiplenebiliyor. Sonraki uninstall F'yi siliyor: "historical management authority versus membership in the newly desired plan".
  - Repair, köprü durumunu yazımdan önce hash'liyor. Başarısız bir repair, kullanıcı düzenlemesinin hash'ini kaydedebiliyor.
  - Önek dry-run tuzağı:
    - "`ecc --dry-run repair` | Repair receives the environment flag but not the argument; its main reads only parsed options.dryRun and can take the ordinary mutating path".
    - "`ecc --dry-run auto-update` | The updater likewise ignores that environment flag when deciding whether to run Git fetch/pull".
    - Uninstall iki biçimi de tanıyor.
  - Auto-update `git fetch --all --prune` ve `git pull --ff-only` çalıştırıyor. "fast-forward-only is not an assertion that this is the latest reviewed release".
  - Güncellemeden sonra doctor koşmuyor. Sinyalle öldürülen çocuk süreç "updated" diye raporlanabiliyor.
- **DevOS kararları:**
  - doctor: **uyarlayarak al.** Tek başına kanıt değil; sıfır kayıt başarısızlık sayılmalı.
  - repair ve auto-update: **alma.**
  - uninstall: yalnız pin değiştirirken, önce makbuzdaki dosya listesiyle karşılaştırarak kullan.
  - `--dry-run` hiçbir zaman alt komuttan önce yazılmasın.

#### M4. Hook çalıştırıcı, bayraklar ve profiller (N31, N32, N50; U14-B/C, U19-B)
- **Nasıl işler:**
  - `scripts/hooks/run-with-flags.js` bayrak, dry-run ve yol kontrolü yapıyor. `run()` dışa aktaran betiği aynı süreçte çalıştırıyor. Dışa aktarmayanı "legacy subprocess" ile çalıştırıyor; `session-start.js` ve cost-tracker böyle.
  - `scripts/lib/hook-flags.js`: "Environment/plugin/managed configuration precedence, global enable, default standard profile, disabled IDs".
  - PostToolUse dispatcher alt hook'ları senkron ya da asenkron çağırıyor. Ham girdiyi çevirmeden iletiyor. Bayt sınırı var; hatalar hook başına ele alınıyor.
- **Sınırlar** [kaynak diyor]:
  - "RUNNER returns exit0 and the original payload when the named hook script is missing, after writing a diagnostic to stderr."
  - START iç hatayı yakalıyor ve exit 0 dönüyor.
  - "It is inaccurate to generalize either 'all hook failures are warned' or 'all failures are silent'."
  - "minimal alone does not disable these two hooks" (session-start ve session-end-marker).
  - "Disabled and dry-run paths return the input without invoking the selected hook."
- **Bulut:** exit 0'daki stderr modele gitmiyor (O5 M4). Yanlış yol ya da eksik betik sessiz kalır [çıkarım].
- **DevOS kararı: al ve uygunluk testiyle koru.**
  - Kurulumdan sonra her etkin hook'a sahte payload verilsin; beklenen dosya ya da `additionalContext` denetlensin.
  - Bulutta anlamsız hook'lar `ECC_DISABLED_HOOKS` ile kimlik bazında kapatılsın; yalnız profile güvenilmesin.
  - O5'in "Read'de en az 4, Edit'te en az 8 Node süreci" sayımı alt sınırdır; legacy alt süreçler bunun üstüne eklenir. Gerçek gecikme ölçülmeli.

#### M5. Oturum başlangıcı, bitişi ve veri kökü (N50, N51; U19-B/C)
- **Başlangıç** (`scripts/hooks/session-start.js`):
  - Oturum ve learned dizinlerini açıyor, gözlemci projesini çözüyor, süresi dolmuş özetleri budayabiliyor, gözlemci lease'i yazabiliyor.
  - Bağlam üretiyor: instinct eylemleri, uygun önceki özet, learned skill özetleri, proje türü, uzunluk tavanı.
  - "Turning additional-context injection off does not by itself disable those other operations."
  - resume ve fork "resume" sayılıyor; önceki özet dalı atlanıyor.
- **Bitiş:**
  - Seçili bitiş hook'u `session-end-marker`. Yalnız lease'i kaldırıyor, gözlemci PID'ine sinyal gönderebiliyor: "the selected start/end pair is not by itself a self-contained transcript-save-and-restore loop".
  - Özeti yazan `session-end.js` ayrı bir hook. Transcript yoksa yer tutucu kayıt yazabiliyor: "A file's presence is therefore not proof of recovered conversation content."
- **Veri kökü sırası** (N51, birebir): "explicit ECC_AGENT_DATA_HOME; eligible project .cursor/ecc-agent-data.json; Cursor default when explicitly preferred or CURSOR_VERSION/CURSOR_PROJECT_DIR is present; otherwise Claude default".
  - Proje yapılandırması varsayılan köklere sınırlı: "delegates allowed-root containment to path-safety for the default Cursor/Claude directories". Açık env ise "trusted override".
  - Alt dizinler: `R/session-data`, eski `R/sessions`, `R/skills/learned`.
  - Gözlemci kendi kökünü ayrı çözüyor: `CLV2_HOMUNCULUS_DIR`, `XDG_DATA_HOME/ecc-homunculus` ya da `~/.local/share/ecc-homunculus`.
- **Bulut:**
  - İki kök de `$HOME` altında; makine geri alınınca kaybolur [çıkarım].
  - Repo içine yönlendirmenin tek yolu bu iki env. Onları kalıcı olarak nereye yazacağımız (`settings.json` `env` ya da ortam ayarı) O11'in konusu [bilinmiyor].
  - ECC bu dosyaları commit etmiyor.
- **DevOS kararı: uyarlayarak al.**
  - İki env repo içinde bir dizini göstersin (örn. `.devos/ecc-data/`).
  - Commit kuralı DevOS'un olsun: iş kapanışında ve Stop'ta.
  - Budama repo içinde commit gürültüsü üretir. Kapatılsın ya da DevOS arşiv kuralına bağlansın.
  - ECC sıkıştırmadan sonra (source=compact) önceki özeti eklemiyor (O5 M2). Güncel iş durumunu yeniden basan bir DevOS hook'u gerekli. EXP-007'nin `oturum-hatirlat.sh`'si bunun çalışan örneği.

#### M6. Araç etkinliği kaydı (N31; U14-B)
- **Zincir:** "PostToolUse → synchronous dispatcher and hook profile → session-activity-tracker → metrics/tool-usage.jsonl → StateStore::sync_tool_activity_metrics → tool_log → TUI timeline/query".
- **Sınırlar** [kaynak diyor]:
  - Oturum kimliği yalnız `ECC_SESSION_ID`'den, o yoksa `CLAUDE_SESSION_ID`'den okunuyor: "When environment IDs are absent, a JSON session_id alone does not save the row."
  - "The pinned tracker consumes tool_output ..."; güncel belge `tool_response` diyor. Süre sıfıra sabitleniyor.
  - Yazıcı ve okuyucu yolları ayrışabiliyor.
  - Silinmiş oturumu gösteren eski satır FK hatası veriyor ve importu durduruyor.
  - İmza, başarılı içe aktarmadan önce kaydediliyor; study'nin istediği ayrım: "distinguishes 'this file was attempted' from 'this file was successfully consumed'".
  - Risk skoru geriye dönük.
  - Git diff zenginleştirmesi maskelenmiyor; sırlar loga girebilir.
- **Bulut:** O5 bulutta yalnız `CLAUDE_CODE_SESSION_ID`'yi gözledi. Tracker satır yazmaz [çıkarım]. Tüketicisi zaten ECC2 TUI.
- **DevOS kararı: alma, kapat.**
  - Ders: payload alan adları host'un güncel şemasıyla test edilsin.
  - "Denendi" ile "tüketildi" ayrı kaydedilsin.

#### M7. Maliyet ve bağlam izleme (N32; U14-C)
- **Nasıl işler:**
  - Stop'ta cost-tracker `costs.jsonl`'e birikimli satır yazıyor.
  - JS köprüsü son satırı seçiyor.
  - Statusline `remaining_percentage`'ı köprüye yazıyor. Context monitor bunu PostToolUse'da `additionalContext` olarak gösteriyor.
  - Rust importer satırları topluyor ("cost3, then cost7 | 7 | 10"); bu yüzden sert bütçe erken durdurabilir.
- **Sınırlar:**
  - Transcript yoksa sıfır satır yazılıyor: "There is no separate completeness or availability field distinguishing this from observed zero usage."
  - Fiyat son modelle hesaplanıyor. "native total_cost_usd is itself a client-side estimate".
  - Statusline değeri kendi zaman damgasını taşımıyor; monitör tazeliği paylaşılan damgayla (60 sn) ölçüyor.
  - Sabit tampon: "At raw remaining16.5, the adjusted bar can show100% used."
  - Kilitsiz rename; güncellemeler kaybolabiliyor.
  - "Cost messages explicitly say they are informational, not an instruction to stop". Bağlam mesajı ise "asks for a user decision".
  - Uyarı durumu teslimattan önce kaydediliyor; teslim düşerse o kademe bir daha gösterilmiyor.
- **Bulut:** statusline'ın bulut arayüzünde çalışıp çalışmadığı [bilinmiyor; O11]. Çalışmıyorsa köprü değeri hiç tazelenmez.
- **DevOS kararı: uyarlayarak al.**
  - Bağlam ölçümünü transcript `usage`'dan al (O5 M6).
  - Alan başına gözlem zamanı tut.
  - "Ölçüm yok" sıfır diye yazılmasın.
  - Kritik eşikte devir kaydını DevOS kendisi yazsın; Batu'ya sormasın.

#### M8. Rehber uyarlama ve prosedürel devirler (N39; U17-A; E10)
- **Nasıl işler** [kaynak diyor]:
  - **/plan:** Varsayılan olarak satır içi çalışıyor; PRD verilirse artifact modu (`.prd.md` → plan) açılıyor. "Delegation requires both a runtime-exposed specialist and the user's explicit request".
  - **Onaydan önce in-progress:** Milestone onaydan önce `in-progress` yazılıyor. Sonraki çağrı "next pending" kuralıyla başka milestone seçebiliyor: "the file/status convention alone does not guarantee that recovery decision."
  - **Plan–PRD bağı:** Plan, PRD'yi yolla anıyor: "a path is a locator, not automatic change-impact validation".
  - **TDD:** Plan "untrusted" veri sayılıyor. RED, hedeflenen kusuru çalıştırmalı. GREEN aynı hedefte yeniden koşuyor. Squash'tan önce kanıt raporu yazılıyor. "The target description's word enforces does not turn these instructions into a host admission control."
  - **PR:** "Needs testing" durumuna izin veriyor, rebase yapabiliyor. "the described later steps do not automatically repeat the earlier TDD evidence on the rebased revision".
  - **dev-team:** 4 salt analiz persona (PM, Architect, Developer, QA) ve üst sentez var. "All four personas can share the same lossy summary". İç içe alt ajan yasak; yalnız ana koordinatörden çalışıyor.
  - **Ortak ders:** "The shared lesson is not that prose cannot work. Prose can direct real file reads, tests, Git operations and human interaction through a capable actor. The distinction is who interprets a condition and what enforces or records it."
- **Yollar:** `commands/plan.md`, `commands/plan-prd.md`, `docs/PLAN-PRD-PATTERN.md`, `skills/tdd-workflow/SKILL.md`, `commands/pr.md`, `skills/dev-team/SKILL.md`, `agents/planner.md`.
- **Bulut:**
  - Derinlik 1 olduğu için dev-team ve santa gibi çoklu ajan yöntemleri yalnız ana oturumdan çalışır.
  - Batu doğrulayıcı olmadığı için onay satırları yeniden bağlanmalı.
- **DevOS kararı: al; geçiş koşullarını yeniden tasarla.**
  - Yarım kalmış `in-progress` iş uzlaştırılmadan yeni işe geçilmesin.
  - Plan, PRD'yi commit SHA'sıyla ansın.
  - PR ya da rebase'ten sonra TDD kanıtı aynı revizyonda yeniden koşsun.
  - Personalar ayrı ve tam kaynak alsın.
  - Kabul, bağımsız doğrulayıcıya ve deterministik teste bağlansın.

#### M9. Native review workflow (U11-A; N19 O5a'da; E08)
- **Nasıl işler:**
  - `/orch-review`, host'tan `workflows/orch-review.workflow.js`'i çağırmasını istiyor. Bu bir Claude Code dynamic workflow: https://code.claude.com/docs/en/workflows (U11-A defteri).
  - Seçilen boyutlar paralel gözden geçiriliyor; yanıtlar şemalı JSON.
  - Bulgular dosya ve normalize kanıt anahtarıyla birleşiyor. İlk bulgunun alanları kalıyor, önem derecesi yükseltiliyor.
  - Her bulgu "independent skeptic" doğrulayıcıya gidiyor. İstem şunu diyor: "Uncertainty must never clear a blocker." [gözledim: E08 `calls`]
  - "U11A-01 reports to the main conversation and prohibits a fallback approval after Workflow failure".
- **Sınırlar:**
  - "The package's explicit file list omits root workflows". npm paketi bu workflow'u taşımayabilir. Study bunu beyan edilmiş bir seçim sınırı sayıyor, gözlenmiş hata değil.
  - orch-pipeline'ın 5. fazı hâlâ sıradan code-reviewer'ı anıyor.
  - PR komutları yalnız numara taşıyor, `--repo` yok.
  - "Host resume is separate from an ECC durable consent/review record."
- **DevOS kararı: uyarlayarak al.**
  - Birleştirme en güçlü kanıtı ve her gözden geçirenin kararını korusun.
  - "CHANGES_REQUESTED + boş bulgu" hata sayılsın.
  - Diff olmayan girdi reddedilsin.
  - Gözden geçirilen revizyon SHA'sı kaydedilsin.
  - Dynamic workflow'un bulutta çalışıp çalışmadığı [bilinmiyor; O11]. Çalışmıyorsa aynı kurallar ana oturumdan açılan iki taze gözden geçirenle uygulansın.

#### M10. Harness scorecard ve optimizer (N40; U18-A)
- **Nasıl işler:**
  - `scripts/harness-audit.js` yalnız `fs/os/path` kullanıyor. Yerel dosya ve işaretçileri ağırlıklı kontrollerle puanlıyor, en önemli 3 eylemi öneriyor.
  - Repo modunda tavan 80, tüketici modunda 39. Her sağlayıcı kategorisi +10 ekliyor. 37'den 39'a düzeltmeyi study kendisi yaptı.
- **Sınırlar:**
  - "an agents-scoped report can return3/3 and Tool Coverage10/10 from a settings file alone, even with no agent definition."
  - Tam puan alan fixture'ın içi boş: "empty hooks array, placeholder test text, an empty eval JSON and a workflow whose content is only a name".
  - Rapor her durumda exit 0 dönüyor. Optimizer exit kodunu ölçüt aldığı için audit ayağı geri almayı tetikleyemiyor.
  - Plugin tespiti HOME'a bakıyor: "Two users auditing the same project commit can therefore receive different installation points".
  - Eval skill'i `.claude/evals/` öneriyor, audit ise kökte `evals/` arıyor.
  - Optimizer örneği ("PreToolUse hook over a200ms budget") için audit motorunda bir üretici yok.
- **DevOS kararları:**
  - Kapı olarak: **alma.**
  - Periyodik envanter aracı olarak: **uyarlayarak al.** JSON çıktısı DevOS eşiğine bağlansın; girdi sabitlensin (HOME'suz); puan "var olma" ölçüsü diye etiketlensin.

#### M11. İzin semantiği (U12-A/N24, N53; E10 arşivi)
- [kaynak diyor] "Claude allowed-tools is preapproval, not an exclusive tool inventory." CLI başvurusu: "Preapproval, deny rules and tool availability are distinct."
- Kiro için: "this is not a read-only tool set: the preapproval list does not itself remove all other built-ins".
- ECC'nin kendi normalleştiricisi: "Claude Code expects tools to be a comma-separated scalar" (`scripts/lib/agent-tools.js`) [gözledim: E10 arşivi].
- **DevOS kararı: ders olarak al.** Salt okuyan doğrulayıcı gibi rol kısıtlaması, ajan frontmatter'ındaki `tools:` alanıyla ve deny kurallarıyla yapılsın, `allowed-tools` ile değil. Kesin davranışı O11 doğrulamalı.

#### M12. İlerleme eşitleme sözleşmesi (N56; U19-H)
- **Kaynak:** `docs/architecture/progress-sync-contract.md`.
- **Doğruluk yüzeyleri:** GitHub kuyruğu ve review, Linear, yerel devir, roadmap, work-items köprüsü.
- **Kural:** "requires an owner artifact, current evidence and a next action for a lane".
- **İçe aktarma:** `work-items.js sync-github`, GitHub durumunu yerel depoya aktarıyor.
- **Olay ayrımı:** "A supplied status instruction, a local import, a current remote status and an authorized release remain different events."
- **Roadmap için:** "a status by its object, source date and consumer".
- **DevOS kararı: al.**
  - Her iş kaydı sahip artefaktı, güncel kanıtı ve sonraki adımı taşısın.
  - Her durum, nesnesi, kaynak tarihi ve tüketicisiyle yazılsın.

#### M13. Değerlendirici prototipi (N55; U19-G)
- **Ne var:** `examples/evaluator-rag-prototype/` altında senaryo, iz, rapor ve doğrulayıcı sonucu dosyaları.
- **Test ne yapıyor:** "The test treats the supplied decisions as data to compare against hardcoded expectations."
- **Koşu bağı yok:** `run_id` karşılaştırılmıyor: "same-scenario conformance is not same-run evidence binding".
- **Barındırılan iddia:** ECC-Tools iddiasının testi yalnız cümlenin var olduğunu denetliyor.
- **DevOS kararı: alma.**
  - Ders: kararları saklayan fixture doğrulayıcı değildir.
  - Kanıtlar aynı koşu kimliğine bağlansın.
  - Atıf verilen içerik hash'lensin.

#### M14. ECC'nin kendi yayın zinciri (U13-A; N28 O5a'da)
- **Zincir** [kaynak diyor]: "one candidate archive, expected hashes passed to lifecycle jobs, pre-publish digest recheck and registry integrity comparison".
- **Sınırlar:**
  - İmzalı tag doğrulanmıyor: runbook ister, YAML denetlemez, `release.sh` `-s` kullanmaz.
  - Eşzamanlılık anahtarı olmadığı için eski bir iş "latest"ın üstüne yazabilir.
  - SLSA ayrı ve yeni bir arşiv paketliyor.
- **DevOS kararı: pin için güven çıpası olarak al.**
  - Kesin sürüm npm integrity (SHA-512) ve git commit ile sabitlensin; `latest` kullanılmasın.
  - İkisi makbuza yazılsın.
  - İmza doğrulaması yok; varmış gibi yazılmasın.

#### M15. Tedarik zinciri tarayıcısı ve hazırlık yüklemleri (N29, N30; U13-B, U14-A)
- **N29 (tarayıcı):**
  - "a nonexistent requested root can produce a passing text report with zero inspected files".
  - Bütün URL yenilemeleri başarısız olsa bile ready=true dönebiliyor.
  - deny muafiyeti AST konumuna değil, değer aramasına bağlı.
- **N30 (hazırlık):**
  - İşaret temelli: 10 kontrol, 21 puan. "An equivalent ordinary source change that removes behavior while retaining marker strings can leave the readiness predicate unchanged."
  - CLI exit 0 dönüyor ama gerçek bir CI zinciri var: JSON → test assertion → suite exit.
  - `publicationReady` sabit false.
  - `gh` varsayılanı 30 kayıtta kesiyor.
- **DevOS kararı: alma** (ECC'nin kendi bakım işi). Dersleri al:
  - Sıfır kapsam başarısızlıktır.
  - "Atlanan ya da okunamayan", "temiz" sayılmaz.
  - Durum projeksiyonu üreticisinden güçlü olamaz.
  - İşaret metni yetenek kanıtı değildir.

### 4.B Bulutta çalıştırılmayacak ama dersi alınacak mekanizmalar

| Mekanizma (kaynak) | Neden alınmaz | Alınacak ders |
|---|---|---|
| ECC2 worktree birleştirme ve temizlik (N34, U15-B) | Uzun yaşayan Rust daemon; boşta VM geri alınıyor; "alpha control-plane scaffold" (U11-E) | "work retained by the merge/rebase path can subsequently become eligible for deletion by a different cleanup predicate". Failed/Stopped oturum birleşebiliyor. Stale korunmuyor. Temizlik `git worktree remove --force` ve `git branch -D` çalıştırıyor. Git durum hatası boş listeye dönüyor ("unknown-versus-clean" kaybı). → Birleştirme gözden geçirilmiş SHA'ya bağlansın; temizlik çözülmemiş işi korusun. |
| Graf ve recall (N35), Node recall ve yakınlık (N36) | ECC2 ve operatör paneli | Checkpoint yalnız dosya uzunluğu ve mtime. "Pinned" etiketi başka kayda iliştiriliyor. Yakınlık "new-side" satır numarasıyla hesaplanıyor. "leases are not locks and the view does not steer/pause/lock". → Kaynak ve koordinat bağı kurulsun; danışman çıktısı kilit sayılmasın. |
| AURA (N41) | İsteğe bağlı Python ağ geçidi | İstekteki kimlik yanıttakine bağlanmıyor ("did=body.get("did", did)"). → Yanıt kimliği istekle bağlansın; karar makbuzu kullanılan politikayı taşısın. |
| Itô (N43) | Dış istemci köprüsü | Skill `ecc ito accept` diyor, CLI izin listesinde yok. Test tam kümeyi karşılaştırmıyor. → Belge–kod tutarlılığı tam kümeyle denetlensin. |
| Nasiko (N44) | Pinli ikili edinimi | "The trust anchor is still ECC's reviewed source/table". Global `--dry-run` tüketilmiyor. → Pin tablosu iyi desen; önek bayrak tuzağı yine var. |
| NanoClaw (N45) | Terminal REPL, `claude -p` | "the storage grammar uses unescaped content delimiters": `---` içeriği kaybettiriyor. Sıkıştırma arşivsiz, son 20 kaydı tutuyor. Model ve skill seçimi kaydedilmiyor. "SYSTEM CONTEXT" yalnız bir etiket. Hatalar asistan turu olarak saklanıyor. → Bellek dosyaları sağlam biçimde yazılsın (frontmatter/JSON), sıkıştırmadan önce arşivlensin. |
| Masaüstü ve tarayıcı panoları (N46, N47) | Yerel GUI ve sunucu | Yedek kayıt "Ready" görünüyor. Yan dosya uyuşmazlığında 200 ile "No hooks configured" dönüyor. → Bozulmuş durum, "yok" durumundan ayrı gösterilsin. |
| MCP ve Codex eşitleme (N48, N52) | Codex host'u | MERGE'ün desteklediği hariç tutma, CHECK'in zorunlu bölümüyle çatışıyor ve geri alma tetikleniyor. PRECOMMIT `rg` yoksa geçiyor. PREPUSH itilen SHA'ları değil çalışma ağacını test ediyor. → Doğrulayıcı üreticinin politika girdisini okusun; eksik araç başarısızlık sayılsın; kanıt itilen SHA'ya bağlansın. |
| Pi, Cursor, Kiro (N50–N53 host kısımları) | Başka host | Cursor sarmalayıcısı betiği `P/scripts/hooks`'ta arıyor, betik `P/.cursor/scripts/hooks`'a kurulmuş. Kiro kopyaları eski kalıyor: "Updating the primary ECC file, updating a Kiro source copy, copying it to a target and selecting it are four different changes." → Kurulu yerleşim hook'un kök aramasıyla eşleşsin; kopyalar sürüm makbuzu taşısın. |
| Belge iddiaları (N54) | Anlatı, kod değil | "The opening narrative is not proof that every install automatically realizes the whole sequence." Arşivle-sonra-kırp tarifi, sıkıştırma başarısız olsa da kaynağı kırpıyor. Türkçe README bayat. → Yıkıcı adımdan önce başarı denetlensin; belge ile kod tutarlılığı ölçülsün. |

## 5. Deneyler ve benim doğrulamam

### E08: native review workflow (U11-A)
**Koşul:**
- Önkayıt commit'i `6f248ca8`.
- Kaynak blob'u `3fd502da`, 15.454 bayt. Node v22.16.0.
- Adaptör: "export-to-const + AsyncFunction; Promise.all thunks; supplied agent replies only; no native host".
- 18 senaryo. Draft7 şema denetiminden 38 yanıt geçti.

**Senaryolar ve sonuçlar [gözledim]:**

| Senaryo | Sonuç |
|---|---|
| clean_selected_dimensions | APPROVE |
| reviewer_null / reviewer_rejection | CHANGES_REQUESTED, incomplete=true |
| verifier_null / verifier_error | CRITICAL "could not be verified — kept as blocking" |
| verifier_low_false (0.2) | "verifier could not confidently refute — kept as blocking" |
| verifier_low_true (0.2) | istatistikte **confirmed=1** (düşük güven "confirmed" sayılıyor) |
| verifier_confident_false (0.95) | refuted → advisory → APPROVE |
| **medium_then_critical_same_evidence** | **APPROVE**: birleşik bulgu "Style concern" başlığını ve CRITICAL derecesini alıyor, "STRONG_PROOF" kanıtını kaybediyor. Doğrulayıcıya "Finding (CRITICAL) in src/format.ts: Style concern" gidiyor; kanıtsız bulgu çürütülüyor. |
| critical_then_medium_same_evidence | CHANGES_REQUESTED (confirmed) |
| distinct_evidence / different_file | 2 ayrı bulgu korunuyor |
| same_snippet_different_locations | 2 ham bulgu → 1 bulgu (satır anahtarda yok) |
| reviewer_negative_verdict_empty_findings | APPROVE |
| nonempty_not_a_diff | APPROVE (1 boyut) |
| security_path_selects_extra_dimension | 3 boyut, APPROVE |
| empty_diff / malformed_paths | hiçbir ajan çağrılmadan hata |

**Study'nin yorumu:** "That proves information-flow dependence in this fixture, not that a live model missed a real defect."

### E09: Python sağlayıcı ve araç döngüsü (U12-C)
**Koşul:**
- Önkayıt commit'i `97ab9354`, 2026-09-20T00:34:55Z. Python 3.13.5.
- Orijinal `types.py` ve `executor.py` blob'larla eşleşiyor.
- `sdk_network_model_calls: 0`. 8 vakanın hepsinde tahmin tuttu.

**Vakalar [gözledim]:**
1. Araç çağrısı yoksa etki yok.
2. Bilinen araçta tur tamamlanıyor.
3. Listede ilan edilmemiş ama kayıtlı araç çalışıyor.
4. Şema zorlanmıyor: `"not-an-integer"` çağrılabilire ulaşıyor.
5. `max_iterations=1`'de etki gerçekleşiyor ama sonuç "Max iterations reached" ile düşüyor.
6. Taze yeniden deneme etkiyi tekrarlıyor: `[7, 7]`.
7. `is_error` işareti modele giden mesajda kayboluyor.
8. OpenAI biçiminde `type:function` eksik ve argümanlar nesne olarak kalıyor.

**Aktarım olayı:** E09 base64 yüklemesinde "a character transcription error" oldu, düzeltildi (U12-C makbuzu). DevOS ilgisi düşük; ders: ilan ile kayıt ayrı, yeniden denemede idempotentlik yok.

### E10: Gemini ajan dönüştürücüsü (U17-A)
**Koşul:**
- Önkayıt commit'i `7217bce9`, 2026-09-22T13:49:06Z. Node v22.16.0, PyYAML 6.0.3.
- Kaynak blob'ları eşleşiyor: `bea91cb1`, `8b810c88`.

**Vakalar [gözledim]:**
- **C0:** `tools: Read, Grep, Read` → `["read_file", "grep_search"]`; `color` siliniyor.
- **C1:** CRLF dosya değişmiyor ve "already compatible" sayılıyor. Sebep: regex `^---\n([\s\S]*?)\n---(\n|$)` yalnız LF tanıyor.
- **C2:** Frontmatter olmayan dosya "compatible" sayılıyor.
- **C3:** Bilinmeyen araç adı olduğu gibi kalıyor.
- **C4:** Blok liste bozuluyor. Boş değerli `tools:` satırı `normalizeAgentTools('')` → `[]` ile `tools: []` oluyor, alttaki `  - read_file` satırları kalıyor. PyYAML girdiyi kabul ediyor, çıktıyı reddediyor ("expected <block end>, but found '<block sequence start>'").
- **C5:** İdempotent.
- **C6:** Dizin yok; exit 1.

**Kurtarma [gözledim]:** Depodaki base64 geçerli bir ZIP'e çözülmüyordu. Karma korumalı ekleme özgün baytları geri getiriyor. `recovery-check.json`: `"kind": "ARCHIVE_RECOVERY_CHECK_NOT_TARGET_RERUN"`, `"exact_original_zip": true`, `"zip_crc_ok": true`, `"changed_input_rejected": true`, `"new_target_campaigns": 0`. 97 baytlık bozuk aralık 91 baytlık doğrusuyla değişiyor.

**Study'nin yorumu:** "Parser agreement tests syntax, not Gemini loading or model obedience" (METHOD-CASE).

**Üç probe'un ortak dersi:** Üçünde de kanıt aktarımı bozuldu [kaynak diyor: makbuzlar]:
- E08: 193 baytlık kesik yazım.
- E09: karakter hatası.
- E10: bozuk base64.

## 6. O5 notunun iddiaları: doğrulama

| O5 iddiası | Durum | Kanıt |
|---|---|---|
| "ECC 'kurulunca çalışan bir DevOS' değil" | **Doğru** | CORE §1, §10 |
| "İş döngüsünü, kaydı ve doğrulayıcıyı biz kurarız; ECC parça kaynağıdır" | **İlk yarı doğru, ikinci yarı study'den çıkmıyor** | Study benimsemeyi değerlendirmedi (Q09 NOT STARTED). CORE: "Calling it only a prompt library misses real capabilities". |
| "Öneri: B, 10–15 bileşen" | **Study'den çıkmıyor; kısmen karşı kanıt var** | Elle seçip kopyalamak, N53'ün kopya kayması riskini taşıyor. ECC'nin kendi kurulum yaşam döngüsü sahiplik, onay ve makbuz veriyor (N37, N38, N42). "Proje dosyası" kısmı doğru, "10–15 parça" kısmı O-16'ya aykırı. |
| Kalıcı depolar `$HOME`'da; `ECC_AGENT_DATA_HOME` ve `CLV2_HOMUNCULUS_DIR` repo içine yönlendirebilir | **Doğru, inceltildi** | N51 sırası. Proje yapılandırması varsayılan köklere sınırlı, bu yüzden repo için yalnız env. Eski `R/sessions` dizini de var. |
| `hooks.metadata.json` kimlik ve parmak izi taşıyor | **Doğru** | N38 |
| "Read'de en az 4, Edit'te en az 8 Node süreci" | **Alt sınır olarak tutarlı** | N32 ve N50: legacy betikler ek alt süreç açıyor. Gerçek sayı ve gecikme ölçülmedi. |
| minimal profilde session-start/end açık kalıyor | **Doğru** | N50: "minimal alone does not disable these two hooks" |
| Hook stderr'i modele gitmiyor, sessiz arızalar var | **Destekleniyor** | N50: eksik betikte exit 0 + stderr. Ama "It is inaccurate to generalize ... 'all failures are silent'". |
| N39: `in-progress` → "next pending" | **Doğru** | N39 |
| dev-team yalnız ana oturumdan | **Doğru** | N39, U17-A defteri: "no nested subagents" |
| GateGuard ikinci denemeyi olguya bakmadan serbest bırakıyor | **Doğru** | CORE §7.3 |
| harness-audit "deterministik kategori puanı" | **İnceltilmeli** | N40: HOME'a bağlı; aynı commit farklı puan alabilir. Exit hep 0. İçi boş fixture tam puan alıyor. Tüketici tavanı 39. |
| Kurulum önsözü hedef köke yazılıyor | **Uyumlu** | N38: "rewrites ... to the actual target root". Base64 biçimi study'de geçmiyor (O5'in kendi gözlemi). |
| Makbuzlarda 422, force yok | **Doğru, genişletildi** | U11-E ve U19-B'de 422 ve yeniden kurma. U11-D'den sonra aday ağaç + diff + `update_ref(force=false)` yolu. |
| "yalnız repodan yeniden giriş hiç sınanmadı" | **İnceltilmeli** | METHOD-CASE: "not that no such record can exist anywhere". U18-B yeni konuşmada repodan devam etti; METHOD-CASE incelemedi. Koşullu olgu testi yok. |
| "büyük dosyaların yeniden üretimi ve ikili aktarım bozuldu" | **Doğru; ölçek büyük** | ~24/40 birim; üç probe'un üçü |
| Study'nin 56 notundan 2'si okundu | **Doğru** | O5 §1; DERSLER L1 |
| ECC2 alfa, alma | **Doğru** | U11-E: "alpha control-plane scaffold, not a finished product"; N34 |

## 7. Ortak soruya cevap

### 7.1 Hüküm [çıkarım; benim yargım]
DevOS, ECC'nin üstüne kurulabilir. "Bütün" ECC'nin Claude Code dilimidir. Bu dilim sabit commit'le ve ECC'nin kendi kurulum ve sahiplik yaşam döngüsüyle proje dosyası olarak kurulur. Üstüne bir bulut uyarlama katmanı ve DevOS'a özgü katmanlar eklenir.

**Gerekçe:**
- Study, DevOS'un ihtiyaç duyduğu parçaların çoğunun gerçekten var olduğunu ve belirli yollarla bağlandığını kaynak düzeyinde gösteriyor: yöntemler, kurulum ve sahiplik, hook çalışma zamanı, oturum özeti, bağlam uyarısı, gözden geçirme, TDD/PR prosedürü, iş durumu sözleşmesi.
- Aynı study, bağlantısız ya da anlamı kayan yerleri de somut olarak listeliyor. DevOS katmanı tam bu listeden türetilir.

**Sınır:** Etkinlik kanıtı yok ("effective" seviyesi boş). Bu yüzden ECC'yi temel almak, DevOS'un kendi uygunluk ve kabul testleri olmadan güvenli değil [çıkarım].

### 7.2 ECC'nin hazır verdiği (kapsamımdan)

| Parça | Seviye (study kanıtıyla) |
|---|---|
| Yöntem gövdesi: plan, PRD, TDD, PR, dev-team, native review | **present**; insan ya da ajan yorumlar ("actor-mediated") |
| Kurulum, sahiplik, hook onayı, bakım | **installable**, kaynak düzeyinde güçlü denetimler; testler incelendi, koşulmadı |
| Hook çalışma zamanı: flags, profiles, disabled IDs | **present/installable**; bulutta **executed** kanıtı yok |
| Oturum özeti, başlangıç bağlamı, veri kökü yönlendirmesi | kaynak düzeyinde gerçek; Pi host'ta "reaches the qualified host consumer" (CORE §9). Claude bulutunda sınanmadı. |
| Bağlam ve maliyet uyarısı | uyarı, zorlama değil; statusline'a bağlı kısmı bulutta [bilinmiyor] |
| Pin için yayın bütünlüğü | ECC'nin en güçlü artefakt bağı (CORE §8) |
| Sınama dili ve bağlantı türleri | CORE §2, §9: DevOS'un doğrulama sözlüğü olarak doğrudan kullanılabilir |

### 7.3 Bulutta ne kırılıyor, nasıl düzeltilir

| # | Kırılma | Kaynak | Düzeltme | DevOS testi |
|---|---|---|---|---|
| 1 | Veri kökleri `$HOME`'da; makine geri alınınca kayıp | N51; O5 | `ECC_AGENT_DATA_HOME` ve `CLV2_HOMUNCULUS_DIR` repo içine; DevOS commit kuralı | VM yenilendikten sonra yeni oturum önceki özeti görüyor mu |
| 2 | Tracker env kimliği yok; `tool_output` ile `tool_response` uyuşmuyor | N31; O5 env | Hook'u kapat (`ECC_DISABLED_HOOKS`) | Gerçek bulut payload'unu yakala, alan adlarını karşılaştır |
| 3 | Betik yoksa sessiz exit 0 | N50 | Kurulu yolu `$CLAUDE_PROJECT_DIR`'e göre doğrula | Her hook için iz dosyası ve zaman damgası |
| 4 | session-start yan etkileri ve budama | N50 | Saklama süresini ayarla ya da DevOS arşivi | Budamadan sonra `git status` temiz mi |
| 5 | compact/resume'da önceki özet eklenmiyor | O5 M2; N50 | DevOS SessionStart(compact\|resume) hook'u güncel durumu basar | Sıkıştırmadan sonraki ilk turda durum metni bağlamda mı |
| 6 | Hook'lar ancak açık onayla kuruluyor | N42 | Kurulum betiği onayı açıkça verir, makbuza yazar | Kurulum sonrası hook sayısı beklenenle eşit mi |
| 7 | Önek `--dry-run` gerçekten değiştiriyor | N37, N44 | Sarmalayıcı betik öneki reddeder | Betik testi |
| 8 | repair ve auto-update sahiplik ve sürüm kaydırıyor | N37 | Kullanma; pin değişimi ayrı iş | Makbuz ile kurulu dosya hash'leri eşit mi |
| 9 | Hariç tutulan MCP geri geliyor | N38, N48 | repair yok; bakım sonrası `.mcp.json` denetimi | MCP listesi = beklenen liste |
| 10 | Statusline köprüsünün tazeliği | N32 | Transcript `usage` ölçümü | Uyarının kaynağı ve zamanı kayıtlı mı |
| 11 | Bağlam uyarısı kullanıcı kararı istiyor | N32 | DevOS kritik eşikte devri kendisi yazar | Eşikte devir dosyası oluştu mu |
| 12 | Plan, commit ve PR kapıları kullanıcıya bağlı | N39; CORE §9 | Geçişler doğrulayıcı + deterministik test; Batu'ya yalnız hedef ve teslim kabulü | Kapı kaydı: kim, hangi SHA, hangi kanıt |
| 13 | Derinlik 1 | N39; ortam | Çoklu ajan yöntemleri ana oturumdan | Alt ajan içinde alt ajan açma girişimi yok |
| 14 | Dynamic workflow bulutta var mı | U11-A | [bilinmiyor; O11]; yedek: iki taze gözden geçiren | Workflow çağrısı ya da yedek kaydı |
| 15 | Hesap plugin'inin sürümü kayıyor, rules gelmiyor | O5 §4; 002 README | Proje dosyası yolu | Kurulu ECC commit'i = makbuz |
| 16 | Kök mutlak yol olarak yazılıyor | O5 §4; N38 | `$CLAUDE_PROJECT_DIR`'e yeniden yazım, sonra doğrulama | Başka yolda klonlanınca hook çalışıyor mu |
| 17 | Skill, ajan ve komut açıklamalarının bağlam maliyeti (~107 KB, O5 ölçümü) | O5 | ECC profil ve modül seçimi; Claude Code'un listeleme sınırı [bilinmiyor; O11] | Oturum başı bağlam boyutu ölçümü |
| 18 | Çok repolu oturumda proje dosyaları farklı yükleniyor | BRIEF | DevOS oturumu tek repolu çalışır ya da yükleme doğrulanır | Oturum başında yüklenen skill sayısı |

### 7.4 U20-C'nin ayrımıyla DevOS için kullanım sınıfları

| Sınıf (STATE'teki ayrım) | ECC'den |
|---|---|
| **Source reference**, doğrudan temel | Kurulum ve sahiplik (M1–M2), hook çalışma zamanı (M4), yöntem gövdesi (M8), ilerleme sözleşmesi (M12), yayın bütünlüğü (M14) |
| **Falsifier**, DevOS tasarımını sınayan karşı örnek | E08 kanıt kaybı; N34 birleştirme→temizlik; N32 birikimli toplam; N45 ayırıcı kaybı; N50 sessiz başarı |
| **Design pressure** | Batu doğrulayıcı olmadığı için "actor-mediated" kapılar; `$HOME` veri kökleri; derinlik 1; sıkıştırmadan sonra yeniden enjeksiyon |
| **Implementation/testing example** | E08, E09 ve E10'un önkayıtlı probe biçimi; sahiplik yan dosyası; hook onay kapısı |
| **Proposal needing further evidence** | Instinct öğrenmesinin yararı (CORE §6); TDD rehberinin kaliteye etkisi; harness puanının anlamı; METHOD-CASE'in yayın önerisi |

### 7.5 Önerilen katman yapısı (örneğin üstüne kurma)

**K0, host:** Claude Code bulutu.
- Tek repolu oturum; hook'lar, skill'ler ve izinler proje dosyasından.
- Derinlik 1; %80'de sıkıştırma; boşta kalan VM geri alınır.

**K1, ECC temeli:** Commit'le sabitlenmiş Claude dilimi.
- ECC'nin kendi installer'ı kurar; dosyalar pin'e bayt eşit kalır.
- Makbuzda: commit SHA, npm integrity, kurulu dosya listesi ve hash'leri, hook onayı, önceden var olan ayar değerleri.
- ECC dosyaları elle düzenlenmez. Değişiklik ancak pin değişimiyle olur.

**K2, bulut uyarlaması:**
- Env yönlendirmeleri.
- `ECC_DISABLED_HOOKS` listesi ve her kapatmanın gerekçesi.
- Kök yeniden yazımı.
- SessionStart(compact|resume) yeniden enjeksiyonu.
- Uygunluk testleri (§7.3 son sütun). Pin değişince aynı testler koşar.

**K3, DevOS'a özgü katmanlar.** ECC'de "not established" olanları sağlar:
- **İş kaydı:** sahip, kanıt, sonraki adım, commit SHA bağı (M12'yi aşar).
- **Kabul:** yazar ≠ doğrulayıcı. Doğrulayıcı PASS'ı revizyona ve test koşusuna bağlanır. Batu yalnız hedefi ve teslim kabulünü verir.
- **Bağımsız görev kalitesi ölçümü:** CORE §10'daki boşluk.
- **Ders kaydı:** tetik, eylem, kanıt ve kapsam; gözden geçirilmiş.
- **Yazma disiplini:** cerrahi düzenleme; dokunulmayan içerik denetimi; force yok.
- **Yeniden giriş testi:** yalnız repodan, cevabı verilmemiş olgularla.

**K4, üstünlük kuralları.** ECC komutları kullanıcı onayı istediğinde DevOS kuralı onayın sahibini belirler. Bu kural DevOS'un kendi rules/skill dosyalarında durur. ECC metni değiştirilmez [çıkarım]. Uyulup uyulmadığı K2 testleriyle ölçülür; CORE'a göre düzyazı "actor-mediated"dır ve kendiliğinden zorlanmaz.

**Pin yükseltme:**
1. Ayrı dalda yeni pin'le kur.
2. K2 testlerini koş.
3. ECC'ye ait dosyaların diff'ini çıkar.
4. Doğrulayıcı kabul ederse birleştir.

CORE'un uyarısı da gerektiriyor: "revalidate the relevant upstream and host/runtime".

## 8. Açık sorular

### 8.1 Study'nin kendi açık soruları (QUESTIONS.md ve baseline)
- **Bütün study:** Q09 (DevOS değerlendirmesi, NOT STARTED); Q10 (güçlü yöntem doğrulaması kanıtlanmadı); Q01 (bütün study ve kullanıcı kabulü).
- **Kurulu host uyumu:** Q01a2b2 (Pi), Q01a2c2 (Cursor), Q01a2d2 (Codex), Q01a2e2 (Kiro), Q02a2, Q02b3, Q02c2, Q02d2. Q02d2'nin metni tipik: "Installed loader/schema/tool/model availability; actual placement and delegation; semantic preservation; safe plan interpretation, consent and revision-bound evidence; interrupted milestone recovery, model obedience and outcomes."
- **Bakım ve sahiplik:** Q03b (Kimi yeniden deneme), Q03c3: "authenticated ownership and consent; concurrent files/locks/source movement, abrupt crash, durability, recovery and actual preserved user work. No observed loss or safety certification".
- **İş ve yürütme:** Q04b, Q04c, Q04e1b, Q04e2b, Q04e3b, Q04e4b, Q04f2, Q04g1c, Q04g2b, Q04h2 (review: "actual repair/re-review/commit enforcement/cross-session recovery"), Q04i2.
- **Bellek:** Q05b, Q05c (ECC2 izdüşümü ve oturum yakalama/sürdürme dahil gerçek bellek kullanımı: "snapshot/sent message is not complete uptake"), Q05d3.
- **Öğrenme ve değerlendirme:** Q06b, Q06c2 ("Independent oracle and accepted change/use"), Q06d1b, Q06d2b, Q06e2 ("meaningful comparable trials ... causal benefit").
- **Güvenlik ve yetki:** Q07a2, Q07b2, Q07c2 ("authenticated decision and action admission/resume"), Q07d2, Q07d4.
- **Sinyallerin anlamı:** Q08a2, Q08b2, Q08c2, Q08d3, Q08d4.
- **İsteğe bağlı arayüzler:** Q02e2, Q02f2, Q02g2, Q02h2, Q02i2, Q02j2.
- **Belge ve medya:** Q01a2f2, Q01a2g2, Q01a2h2 ("No image viewed ... Do not assert these contain nothing new").

**Ortak desen:** Hepsi kaynak düzeyinde cevaplanmış bir ilişkinin "daha güçlü" hali: kurulu kimlik, eşzamanlılık ve çökme, doğrulanmış yetki, kabul edilmiş yararlı sonuç. Study bunları kasıtlı olarak açık bıraktı: "Source countercases are not observed incidents".

### 8.2 DevOS'un kendisinin sınaması gerekenler (study'den türetilmiş)
1. ECC hook'ları bulut Claude Code'da tetikleniyor mu? Gerçek payload alanları ne (`tool_response`, `session_id`)?
2. SessionStart `additionalContext` bulutta modele ulaşıyor mu? `source` değerleri neler (startup, compact, resume)?
3. Env yönlendirmesi hook alt süreçlerine geçiyor mu? Hangi ayar yolu kalıcı?
4. Async Stop hook'ları VM geri alınırken yarım kalırsa özet dosyası ne halde kalıyor?
5. ECC installer'ın Claude proje hedefi bulutta, setup script önbelleğiyle çalışıyor mu? npm ya da git erişimi var mı?
6. Skill ve ajan listesinin bağlam maliyeti ne? Claude Code bu listeyi kısıyor mu?
7. Dynamic workflow ve statusline bulutta var mı?
8. Yalnız repodan yeniden giriş: önceden yazılmış 5–10 olgu, cevabı verilmeden taze oturumda bulunuyor mu?
9. 2.2.1'den 2.2.2'ye (O5 klonu) study'nin kaynak karşı örnekleri (tracker alanları, dry-run öneki, MCP repair) düzeldi mi? [O5c ve O5d; bilinmiyor]

## 9. Dersler (kök neden, önlem, kaynak)

1. **Büyük paylaşılan dosyayı baştan üretmek ilgisiz satırları bozar.**
   - Olay: 40 birimin ~24'ünde en az bir olay. İkisi (U11-A, U11-C) main'e ulaştı, sonra geri alındı.
   - Kök neden: "verifying a local candidate does not prove that a later manually emitted payload is identical" (U11-C); "The recurring error source is reconstructing a large shared file to alter one row" (U18-C-ALIGNMENT).
   - Önlem: yalnız cerrahi düzenleme; dokunulmayan bölümlerin hash'i aynı mı denetimi; önceden hesaplanan beklenen hash (U18-H); blob yeniden kullanımı (U11-D, U19-D).
2. **Kodlanmış kanıtı elle aktarmak bozar.**
   - Olay: E08, E09 ve E10'un üçünde de oldu.
   - Önlem: "Large manual encoded transfers are a demonstrated publication hazard here" (U17-A); zincir "source bytes → ... → reachable repository files" (METHOD-CASE §5). DevOS ikili veri üretmez; dosyayı git'e yazar ve hash'ler.
3. **Kesilen tur yarım commit bırakır.**
   - Olay: U17-A'da açılış, aktivasyon, PRECHECK ve arşiv yazılmıştı, not yoktu. U19-B'de araştırma bitmiş, yayın kapanmamıştı.
   - Önlem: yeniden girişte main beklenen kapanışla karşılaştırılır; "source completion distinct from publication completion" (METHOD-CASE §6). DevOS iş kaydında "yayın tamam" ayrı bir alandır.
4. **Eşzamanlı yazım (422) karşısında force kullanılmaz.**
   - Olay: U11-E ve U19-B'de başka iş akışları main'i ilerletti.
   - Önlem: "If another concurrent commit intervenes, rebuild rather than force." (U19-B). DevOS push reddinde rebase eder ve testleri yeniden koşar.
5. **Platform güvenlik bloğu atlatılmaz.**
   - Olay: U17-A ve U18-C'de çağrı engellendi; bir sonraki turda aynı yol çalıştı.
   - Önlem: "These are acquisition limits, not target evidence or permission to bypass safeguards" (U18-H).
6. **Arama sonucu yokluk kanıtı değildir.**
   - Olay: U11-E'de `parse_template_vars` aramada çıkmadı; U14-A'da dosya adı araması testi kaçırdı.
   - Önlem: "These failures do not justify code/test-absence claims". Yokluk iddiası için doğrudan, pinli okuma yapılır.
7. **Varsayılan dal pinle karışır.**
   - Olay: U12-B ve U12-C'de arama, pinden farklı revizyonlar döndürdü.
   - Önlem: "Fixed-pin fetches prevented those tests from being credited to8321021." ECC bilgisi her zaman pin kimliğiyle yazılır.
8. **Türetilmiş sayı hatalı olabilir.**
   - Olay: N40'ta tavan 37 yazıldı, doğrusu 39.
   - Önlem: sayı komutla üretilir, elle toplanmaz.
9. **Sessiz başarı gerçek başarı değildir.**
   - Örnekler: run-with-flags eksik betikte exit 0; harness-audit hep exit 0; doctor `checkedCount=0`; tarayıcı sıfır dosyada geçiyor; Git hatası boş listeye dönüyor.
   - Önlem: sıfır kapsam hatadır; her kapı exit kodu taşır; "bilinmiyor", "temiz" diye yazılmaz.
10. **Etiket korunurken geçiş koşulu kaybolabilir.**
    - Örnekler: N54 elle /plan uyarlaması; N39 "enforces" sözcüğü.
    - Önlem: her uyarlanan komutta geçiş koşulu ve sahibi açıkça yazılır.
11. **Doğrulanan nesne, teslim edilen nesne olmayabilir.**
    - Örnekler: PR rebase'ten sonra TDD kanıtı yenilenmiyor; PREPUSH çalışma ağacını test ediyor; birleştirme adları yeniden çözüyor; E08'de doğrulayıcıya giden bulgu kanıtsız.
    - Önlem: kanıt commit SHA'sına ve bulgu kimliğine bağlanır.
12. **Kayıt yetki değildir.**
    - Kaynak: "An `approval_requested` label is not an authenticated request awaiting a human" (CORE §7.3).
    - Önlem: DevOS kabul kaydı kimin, hangi revizyonu, hangi kanıtla kabul ettiğini taşır.
13. **Aynı yazarın kendi denetimi bağımsız doğrulama değildir.**
    - Kaynak: "Same-assistant hashes/readbacks test correspondence, not independent reasoning validity." (U11-A).
    - Önlem: DevOS'ta yazar ile doğrulayıcı ayrıdır. Study'nin hükümleri de bu yüzden "candidate" kabul edilir, kesin gerçek sayılmaz.
