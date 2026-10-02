# O6 — Hermes, Superpowers, gstack, mattpocock-skills: DevOS okuma notu

O6, EXP-007 okuma turu, 2026-09-27. Küme: `research/studies/{hermes-agent,superpowers,gstack,mattpocock-skills}`. Not çalışma metinlerine (ikincil kaynak) dayanır; upstream'e inmedim. İstisna: Hermes çalışmasının `evidence/` altına kopyaladığı upstream kod parçaları.

Kanıt etiketleri: **KD** kaynak diyor (çalışma metni ya da onun aktardığı upstream). **G** gözledim (dosyada kendim gördüm: kopyalanmış upstream kodu, deney çıktısı). **Ç** çıkarım (benim). **B** bilinmiyor.

## DevOS için en önemli çıkarımlar

1. **Kendini geliştiren otomatik döngü hiçbir kaynakta kanıtlanmış değil.** Superpowers CORE: "No universal automatic self-improvement service is demonstrated." Hermes: kullanım sayacı fayda ölçmez (not 30). DevOS öğrenmeyi ayrı adımlarla kurmalı: öneri → onay → uygulama → sonraki işte gerçekten yüklenme → sonuç ölçümü. Metin değişikliği başarı sayılmaz. (KD)
2. **Bellek üç katmana ayrılmalı** (Hermes bellek aracının kuralı, G): her oturuma giren küçük bellek yalnız "facts that apply to EVERY session"; görevde öğrenilen prosedür ve tuzak "belongs in the task's skill"; ilerleme ve TODO bellekte değil. DevOS karşılığı: kısa CLAUDE.md + `.claude/skills/*` + git'e işlenen iş kaydı. **Al.**
3. **Rol düzeni için en uygun şablon Superpowers SDD.** Ana oturum controller'dır. Implementer ve tek task reviewer alt ajandır; reviewer spec ve kalite için iki hüküm verir. SDD, worker ve reviewer'ın alt ajan açmasını zaten yasaklar; bulutun derinlik-1 sınırına uyar. Controller "semantic coordination, not only scheduling" yapar: brief'e global kısıtları ve önceki kararları kendisi koyar. **Uyarlayarak al.**
4. **Görev devri dosya tabanlı ve yapılandırılmış olmalı.** Superpowers: brief ve rapor dosyası; DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT. gstack: son satırda tip kontrollü JSON; alt ajandan yetki çıkarma. Hermes: alt ajan özeti self-report'tur; controller diff ve testle doğrular. Sonucu beklenen Agent çağrısında `run_in_background: false` açıkça yazılmalı; gstack bunu üç kez yaşadı (v1.79). **Al.**
5. **Kalıcı durum git'e işlenmeli.** Superpowers'ın SDD defteri `.gitignore`'lu ve geçici; sıradan worktree silinmesinde kayboldu (E11). Bulutta makine geri alınır. DevOS defteri, kararları ve kanıtları commit+push etmeli; kimliği plan yolu ve revizyonuna bağlamalı (E05'te basename çakıştı). **Uyarlayarak al.**
6. **Sıkıştırmadan sonra iki ayrı iş var.** Superpowers SessionStart hook'u `startup|clear|compact` olaylarında çalışma kurallarını yeniden enjekte ediyor. Ama "Procedure re-entry is not work recovery": controller ayrıca defter ve git log'dan devam etmeli. Aynı hook skill dosyası yokken de exit 0 veriyor, bağlamda skill gövdesi yok (F05). DevOS hook'u eksik içerikte görünür hata vermeli. **Uyarlayarak al.**
7. **İş kabulü ve plan biçimi hazır.** gstack `/spec` sekiz kabul ölçütü ister: etkilenen aktör, doğrulanmış mevcut davranış, istenen davranış, neden şimdi, gözlenebilir tamamlanma ölçütü, kapsam içi/dışı ve bağımlılık, hata ve geri alma, teknik sorudan önce kod kanıtı. Superpowers planı: Spec işaretçisi, "Global Constraints", tam dosya yolları, consumes/produces arayüzleri, test, adım, commit. Hazırlık derinliği rotaya göre ölçeklenir (spike / bounded / architectural). **Al.**
8. **İnsan kapıları yeniden dağıtılmalı.** Kaynaklarda insan spec'i, planı, merge'ü onaylıyor. DevOS'ta Batu teknik onaylayıcı değil (K-015). gstack `/autoplan` sınıfları doğrudan eşlenir: Mechanical otomatik; Taste otomatik, kaydedilir, son kapıda gösterilir; User Challenge (kullanıcının yönünü değiştiren) asla otomatik değil, Batu'ya gider. Controller kararları Superpowers gibi karar + gerekçe + "cost if wrong" ile kaydedilir. **Uyarlayarak al.**
9. **Doğrulama iddiaya bağlı olmalı.** TDD'de üç ayrı iddia var: test önce yazıldı ve doğru sebeple kırmızıydı; oracle ayırt edici; sonuç bugünkü koda ait. Kanıt kaydı: komut, exit, working-tree fingerprint, log yolu (gstack). Teslimden önce plan tamamlama denetimi: DONE / PARTIAL / NOT DONE / CHANGED / UNVERIFIABLE. **Al.**
10. **Kendini geliştirme araçları somut.** gstack merdiveni: tekrarlayan hata → adlandırılmış durum → yardımcı betik → yapısal tarayıcı → davranış testi → CI. Superpowers: skill'siz koşuda hata görülmeden kural yazılmaz; müdahale biçimi hataya göre seçilir. gstack `learnings.jsonl`: kaynak türü, güven, zamanla düşüş, injection filtresi; DevOS'ta `~` altında değil repo içinde. **Uyarlayarak al.**
11. **Koruma hook'ları gerçek ama dar.** gstack `/careful`: Bash için PreToolUse ask/deny. `/freeze`: Edit/Write için dizin sınırı. Bash ile dosya değiştirmek freeze'i aşar. Bulutta "ask" kimseye ulaşmayabilir; DevOS'ta deny + gerekçe daha uygun (Ç). **Uyarlayarak al.**
12. **Alma:** gstack GBrain, tarayıcı daemon'u, iOS, Codex çapraz modeli; Hermes gateway, cron daemon'u, Kanban SQLite. Hepsi sürekli çalışan makine ya da yerel home ister; bulut ve "Mac kapalı" kısıtına uymaz (Ç). Yalnız kalıpları al: role göre bellek yönlendirme ve bütçe; task / run / claim ayrımı.
13. **Kapsam boşluğu:** mattpocock-skills yalnız aday kaydı ("RESEARCH NOT STARTED"). Upstream repo bu oturumda erişilebilir değildi.

## 1. Kapsam

Harita: hermes-agent 368 dosya (md ~1,29 MB), superpowers 52 (~481 KB md), gstack 23 (~556 KB), mattpocock-skills 1 (10 KB). `/home/user` altında bu hedeflerin upstream klonu yok.

**Superpowers.** Tam okunan (17): META, CORE, INDEX, STATE; syntheses S01–S06; notes U01, U01B, U02, U03, U04, U05, U06A. Kısmen: SOURCE-LEDGER ciltlerinde yalnız upstream yol taraması; U02/U05 deney betik ve çıktılarından seçili satırlar; U07B'de grep. Okunmayan: CLOSURE-AUDIT (sonucu STATE ve META'da özetli), PLAN, METHOD, U06B1, U06B2 (değerlendirme laboratuvarı), U07A (görsel companion), diğer evidence. Gerekçe: soruya ikincil; S01/S02 bunları özetliyor.

**gstack.** Tam okunan (12): CORE, META, inventory/STRUCTURE; `syntheses/` altında memory-learnings-context-gbrain, planning-specification-work-admission, multi-agent-cross-model-coordination, review-qa-ship-delivery-qualification, repository-self-development-…, guarded-action-security-review, investigation-root-cause-debug-control, testing-eval-…, deploy-canary-…. Kısmen: host-adapters (satır 1–140, 255–474), four-ground-projection (başlıklar, 703–912), revalidation v1.80 (bölüm 1–5); METHOD/SOURCE-LEDGER/STATE/CLOSURE-AUDIT'te yalnız grep. Okunmayan: browser-runtime-security-evidence, cross-ground-mechanisms, cross-system-composition, INDEX. Gerekçe: tarayıcı runtime'ı soru dışı; cross-* sentezleri CORE'da özetli.

**Hermes.** Tam okunan: META, STATE, INDEX, CURRENT-RESEARCH-MAP, 00-WHY-THIS-RESEARCH; synthesis 01–04; notes 01, 02, 03, 04, 07, 15, 17, 18, 27, 28, 30; `evidence/2026-09-10-kanban-task/RESEARCH.md`. Kısmen: `evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md` (satır 20–89 ve grep); upstream kopyaları `evidence/2026-09-09-memory-pending/upstream/memory_tool_store.py` (1–90, 214–360), `memory_tool.py` (şema, 214–245), `write_approval.py` (1–40); not 05 (grep). Okunmayan: notes 06, 08–14, 16, 19–26, 29 (yalnız başlık); OPEN-QUESTIONS, METHOD, RESEARCH-PLAN, SOURCE-LEDGER, inventory, evidence'ın geri kalanı (~330 dosya). Gerekçe: cron, kurulum, runtime backend, UI onay çağrıları, session lease; soruya ikincil ya da bulutta uygulanamaz.

**mattpocock-skills.** META tam okundu (tek dosya). `mattpocock/skills` GitHub erişimi bu oturumda reddedildi ("not configured for this session"); başka yoldan aşmadım.

## 2. Superpowers

Hedef: `obra/superpowers@b36e0829` (manifest 6.3.0). Statü: "BOUNDED-COMPLETE / USER-EVALUATED / ACCEPTED" (2026-09-18). Canlı ajan koşusu yok; sekiz yerel sentetik deney var (E01–E16). Tanım (KD): "a portable software-development methodology expressed through skill and role contracts, interpreted by host-provided agents and tools, supported by concrete adapters, file/Git helpers and an optional visual runtime".

### S1. Giriş yönlendirme: üç rota
- **Sorun:** Her işe aynı ağır törenle girmemek; onayı her zaman korumak.
- **İşleyiş (KD, `skills/brainstorming/SKILL.md`):** Spike: yaklaşımı onaylat, araştır, raporla; "Probe code remains throwaway; keeping it is a new request." Bounded: mevcut bir akışta dar değişiklik; sohbette kısa tasarım, onay; "No separate written spec or implementation plan". Architectural: alternatifler, bölümlü tasarım, yazılı ve commit edilmiş spec, öz-inceleme, insan incelemesi, ardından writing-plans. Gizli karmaşıklık rotayı yükseltir, aşağı indirmez.
- **Kanıt:** Yalnız kaynak okuması (KD). Issue #2203: bounded iş ana oturumda kalıp bağlamı şişiriyor (kullanıcı raporu).
- **DevOS: Al.** İş kaydında rota alanı; bounded işte ana bağlam yükünü izle (Ç).

### S2. Plan biçimi
- **Sorun:** Az bağlamlı işçinin görevi tek başına yapabilmesi ve incelenebilmesi.
- **İşleyiş (KD, `skills/writing-plans/SKILL.md`):** Görev "an independently testable deliverable with a meaningful review boundary". 2–5 dakika tahmini adım içindir, görev için değil. Başlık: Spec işaretçisi ve "Global Constraints". Görevde tam dosya yolları, consumes/produces arayüzleri, testler, adımlar, commit'ler. Öz-inceleme: spec kapsaması, yer tutucu, tip tutarlılığı. SDD giriş incelemesi: "one ledger row for every task and for each pair sharing a file/interface". Çıplak "temiz" hükmü yetmez.
- **Kanıt:** Spec işaretçisi ve Global Constraints `task-brief` çıktısına girmiyor (KD, U02 F17, yerel deney E05/E06).
- **DevOS: Al.** Plan yürütücüye commit ile ulaşmalı: U02'de commit edilmemiş plan yeni worktree'de yoktu, helper exit 2 verdi (KD).

### S3. SDD: controller, implementer, task reviewer
- **Sorun:** İşçiye tüm geçmişi vermeden anlamı korumak; DONE ile kabul arasını ayırmak.
- **İşleyiş (KD, `skills/subagent-driven-development/{SKILL.md, implementer-prompt.md, task-reviewer-prompt.md, re-review-prompt.md, scripts/*}`):**
  - "the spec is binding, the plan argues from it, and the controller rules on most conflicts/ambiguities rather than stopping for the user. Each ruling must record the decision, reason and cost if wrong."
  - Dört durma sınıfı insana gider: yıkıcı/geri dönüşsüz; güvenlik; normalde onay isteyen dış etki; her yolun tahmin olduğu bozuk plan.
  - "Workers are explicitly not given the whole plan/history." Controller brief'e görev, arayüz, global kısıt ve önceki kararları koyar; `task-brief` bunları taşımaz. Worker ve reviewer alt ajan açamaz (paralel dispatch skill'inde bu yasak yok, LC1).
  - Dönüş: DONE incelemeyi başlatır; DONE_WITH_CONCERNS'ü controller sınıflar; BLOCKED/NEEDS_CONTEXT değişmiş yanıt ister (bağlam, güçlü model, bölme, plan düzeltmesi). Aynı denemeyi tekrarlamak yasak.
  - Tek reviewer "reads the diff once and returns two verdicts" (spec + kalite). Rapor doğrulanmamış iddia sayılır. Diff dışı gereksinim "`Cannot verify from diff`" döner; controller tamamlamadan önce çözer, bulguyu bastırmaz.
  - Düzeltme: spec hatası, Critical/Important, doğrulanmış boşluk düzeltilir; Minor deftere. "Rounds 1–3 normally resume the original implementer; rounds 4–5 use a fresh implementer and a more capable model." 5. turdan sonra hakemlik: yük taşımayan bulgu gerekçeyle park edilir, yük taşıyan açık karar ister. Defter "`complete (..., review clean)` and `complete (..., K parked)`" ayırır. Son dal incelemesi: bir düzeltme dalgası + bir yeniden inceleme.
  - BASE dispatch'ten önce kaydedilir; `review-package` BASE..HEAD commit, stat ve diff üretir. Genel örnekteki HEAD~1 çok commit'li görevde yasak.
  - Kalıcılık: `sdd-workspace` → `.superpowers/sdd/<plan-basename>/` (G, U05 çıktısı), `.gitignore`'lu. Defterin ilk satırı plan yolu. Devam eden controller "prefer the ledger and Git history over recollection". Silmeden önce her "`Ruling:`" girdisi maliyetiyle son insan mesajına kopyalanır.
- **Kanıt (KD, sentetik yerel deneyler):** E05/E06: `team-a/shared.md` ve `team-b/shared.md` aynı klasöre düştü, brief ezildi; aynı yolda plan değişince tamamlandı satırı kaldı. E07/E08: yanlış BASE geçerli ama eksik paket verdi. E11: ignore'lu defter sıradan worktree silmesiyle kayboldu.
- **DevOS: Uyarlayarak al.** Controller ana oturum olmalı. Defter, brief, rapor ve kararlar commit edilmeli; kimlik = plan yolu + revizyon + görev no. "Cost if wrong" alanlı karar kaydı aynen alınabilir.

### S4. TDD, doğrulama, sistematik hata ayıklama
- **Sorun:** Kanıtsız "bitti/düzeldi" iddiası ve tahminle düzeltme.
- **İşleyiş (KD):** `test-driven-development/SKILL.md`: beklenen başarısızlık, minimal kod, geçiş, yeşilde refactor. "A typo, test setup error or unrelated failure is not the intended RED." `writing-good-tests.md`: testin yakaladığı kırılmayı adlandır; beklenen değer üretim kodundan türetilmez ("literals and hand-checked fixtures are preferred"). Mock'a argüman, sıra ya da sayı sınır sözleşmesiyse izin var. Mutasyon kontrolü "**mental**"; araç değil.
  - `verification-before-completion/SKILL.md`: "identifying the command relevant to the claim, executing and reading its complete output and exit status, then either reporting the actual failure or making an evidenced claim". Build ≠ lint; test ≠ gereksinim; "child completed" iddiası VCS değişikliği incelenerek verilir. Regresyon kontrolü: geç → düzeltmeyi kaldır → kırıl → geri koy → geç.
  - `systematic-debugging/SKILL.md`: yeniden üret, izle, çalışan örnekle karşılaştır, tek hipotez, tek değişken; üç başarısız düzeltmede mimari tartışma. `receiving-code-review/SKILL.md`: öneriyi kod tabanında doğrula, sonra kabul et ya da itiraz et.
- **Kanıt:** `find-polluter.sh` sıfır eşleşmede ve launcher 127 hatasında da "all tests clean" yazdı (E09/E10, KD). Açık gerilim Q24: genel skill "bu mesajda koş" der; SDD reviewer implementer'ın test kanıtını yeniden kullanır.
- **DevOS: Al.** Q24'ü DevOS kendisi karara bağlamalı (Ç): reviewer kanıtı yeniden kullanabilir, ama komut + working-tree kimliği eşleşmeli (gstack `gstack-evidence`: aynı komut + yaş sınırı + aynı fingerprint, yoksa yeniden koş; deploy §5.2).

### S5. Bitirme ve entegrasyon
- **Sorun:** Görevin bitmesi ile güvenli entegrasyonu ayırmak.
- **İşleyiş (KD, `finishing-a-development-branch/SKILL.md`):** Önce tam test. Menü: merge / push + PR / keep. "discard requires an explicit request followed by the exact confirmation word". Reddedilen push force edilmez. Yerel merge sonrası birleşik sonuç yeniden test edilir. `git worktree remove --force` kendiliğinden kullanılmaz.
- **Kanıt:** E11: iki ayrı yeşil dal çakışmasız birleşti; `a + b <= 1` değişmezi bozuldu (KD).
- **DevOS: Uyarlayarak al.** Merge kararı Batu'ya değil, DevOS politikasına bağlanmalı (K-015). Birleşik sonuç testi zorunlu olmalı.

### S6. Bootstrap hook'u (Claude Code'a özgü)
- **Sorun:** Yöntemin her oturumda ve sıkıştırmadan sonra bağlamda olması.
- **İşleyiş (KD, `hooks/hooks.json`, `hooks/session-start`):** "The Claude-oriented configuration registers a synchronous Bash wrapper for SessionStart, with matcher `startup|clear|compact`." Betik `using-superpowers` skill'ini okur, JSON'a kaçışlar, `hookSpecificOutput.additionalContext` olarak basar. Bootstrap ana ajana ilgili skill'i çağırmayı söyler. Ama "explicitly exempts a subagent dispatched for a specific task from this bootstrap skill and gives user instructions precedence over skill instructions."
- **Kanıt:** F05: skill dosyası yok ya da boşken de exit 0 ve boş olmayan zarf. "valid JSON and a nonempty context field are compatible with no useful bootstrap body." (yerel deney, KD)
- **DevOS: Uyarlayarak al.** Proje `settings.json` hook'u olarak (O11 doğrulamalı), eksik içerikte görünür hata. Ek olarak mevcut işin defter yolunu da enjekte et; "Procedure re-entry is not work recovery" (U01B F12).

### S7. Skill yazma ve değişiklik kabulü
- **Sorun:** Skill ve kural değişikliğinin gerçekten işe yaraması.
- **İşleyiş (KD, `skills/writing-skills/SKILL.md`, `testing-skills-with-subagents.md`):** Açıklama alanı ne zaman yükleneceğini söyler: "The description should answer when the skill should be loaded, not abbreviate its full procedure." Mekanik kısıt yazıya değil otomasyona. Döngü: skill'siz senaryoda hatayı ve bahaneleri kaydet, odaklı müdahale ekle, skill'le koş, düzelt. "If the control does not exhibit the failure, it says not to author guidance". Mikro test: her örnek taze bağlam, müdahalesiz kontrol, varyant başına en az 5 tekrar. Baskı testleri: zaman, batık maliyet, sosyal, otorite.
  - Müdahale biçimi hatadan seçilir: baskı altında atlanan kural → yasak + bahane karşılığı + kırmızı bayrak; kötü biçimli çıktı → olumlu tarif; tekrar tekrar eksik öğe → şablonda zorunlu alan; koşula bağlı davranış → gözlenebilir koşul.
  - Katkı kabulü: yaşanmış sorun, önce/sonra değerlendirme, tam diff'in insan incelemesi.
- **Kanıt:** Kalite etkisi ölçülmedi. Ayrı değerlendirme laboratuvarı (Quorum/Drill) pass/fail/indeterminate tutar; parser onarımı kabul sayısını artırdı, ajanı iyileştirmedi (KD, S01).
- **DevOS: Al.** Skill ve kural değişikliği için RED-GREEN kuralı ve müdahale biçimi tablosu.

## 3. gstack

Hedef: `garrytan/gstack@0d1bd561` (v1.79.0); 2026-09-06'da `c2412166` (v1.80) ile yeniden doğrulandı, repin yok. Statü: "BOUNDED RESEARCH COMPLETE / ADVERSARIAL CLOSURE AUDITED". Kanıt: kaynak ve birinci taraf test dosyalarının okunması; v1.80 için GitHub CI sonuçları (KD). Çalışmanın testleri kendisinin koştuğuna dair kayıt görmedim (B). Model: "SITUATE → KNOW → QUALIFY → GOVERN → ACT → VERIFY REALITY → REFRESH / RECOVER / LEARN".

### G1. Planlamadan iş kabulüne
- **Sorun:** Belirsiz isteğin olgunlaşmadan uygulamaya geçmesi.
- **İşleyiş (KD):** `/office-hours` kod yazmaz. En az iki alternatif üretir ve "STOPs and requires explicit user selection before generating the design record." Tasarım belgesi "**decision record, not a transcript**": `docs/designs/` kopyası, `Supersedes:` soyu, DRAFT → Approve/Revise/Start-over → APPROVED. `/plan-ceo-review` kapsam modları (expansion / selective / hold / reduction) ve kayıtlar: NOT in scope, What already exists, Error & Rescue Registry, Failure Modes Registry, decision log. `/plan-eng-review` önce "what exactly is being reviewed?" sorar; hedef belli olmadan repo okumaz.
  - `/spec`: yukarıdaki sekiz ölçüt (çıkarım 7). "questions answerable from source should not be bounced back to the user." Onaydan sonra mekanik kuyruk: fail-closed redaction, tam byte yeniden tarama, dirty-worktree kapısı, TOCTOU kontrolü, SHA pin, benzersiz worktree/dal, ajan başlatmadan önce son onay. Issue numarası `/ship` için kaydedilir.
  - Skill üretimi: `.tmpl` → resolver genişletme → üretilmiş `SKILL.md`. Claude'a iskelet verilir; bölüm yer tutucusu "a STOP+Read pointer to an on-demand source" olur.
- **Kanıt:** `test/spec-template-invariants.test.ts` statik sözleşmeleri sabitler; model uyumunu kanıtlamaz (KD).
- **DevOS: Al** (spec ölçütleri, karar kaydı biçimi, "önce kodu oku"). **Uyarlayarak al** (onay adımları → DevOS rolleri; Batu yalnız yön ve kabul).

### G2. `/autoplan`: karar yetkisini sınıflama
- **Sorun:** Her ara kararda insanı beklemeden kullanıcı yetkisini korumak.
- **İşleyiş (KD):** Ara kararların çoğu altı ilkeyle verilir. "**Mechanical** — auto-decide; **Taste** — auto-decide, record, surface at final gate; **User Challenge** — both models want to change the user's stated direction; never auto-decide". Sıra: CEO → Design → DX → Eng (hep son). Karar denetim izi ve tek son onay kapısı var. Ebeveyn, çocuk skill'lerin kapsam kapılarını bastırır (skip-list testte sabit).
- **Kanıt:** Skip-list `test/skill-validation.test.ts` ile sabit; dual-voice E2E periyodik ve kısmi (KD).
- **DevOS: Al.** Batu'ya gidecek kararın tanımı için en net kalıp (Ç).

### G3. Teslim niteliklendirme (`/review`, `/qa`, `/ship`)
- **Sorun:** Eski ya da eksik kanıtla teslim.
- **İşleyiş (KD):**
  - Eng Review varsayılan tek kapıdır. `plan-eng-review` ya da `review` kaydı geçer. "Entries older than seven days are ignored"; diff kaydının tazeliği working-tree fingerprint ile ölçülür. Kayıt yoksa `/ship` kendi taze incelemesini yapar: nitelik türü ≠ iş akışı geçmişi.
  - Test kanıt defteri: komut, exit, fingerprint, log yolu. Başarısızlık sahipliği: dalın mı, önceden var mı, belirsiz mi? "Ambiguity defaults to in-branch".
  - Plan tamamlama taze alt ajanda yapılır. Sınıflar: DONE / PARTIAL / NOT DONE / CHANGED / UNVERIFIABLE. NOT DONE'da seçenekler: dur ve yap / ertele / düşür. UNVERIFIABLE tek tek onaylanır. "No plan file found → plan completion audit skips."
  - Düzeltme döngüsü: düzelt → commit → test + review; sıfır düzeltmeli tur gelene kadar, en çok 3 tur; yakınsamazsa engel.
  - `/review` yüksek güvenli bulguda kaynak satırını ister; atlanan bulgu yalnız aynı fingerprint ve değişmemiş dosyada bastırılır.
- **Kanıt:** `test/ship-plan-completion-invariants.test.ts` (yapısal); QA E2E'de `/qa-only` Edit olmadan koştu, ağaç temiz kaldı (birinci taraf).
- **DevOS: Al.** Plan tamamlama denetimi ve test kanıt defteri. Batu'ya teslimden önceki kabul kapısı olarak.

### G4. Çok ajanlı çalışma ve görev devri
- **Sorun:** Alt ajan sonucunu güvenle almak; ebeveynin takılmaması.
- **İşleyiş (KD):** Altı biçim: taze bağlam uzmanı, paralel fan-out, iş akışı devri, çapraz model, uzak eşleme, worktree paralelliği.
  - Review Army: büyük diff'te Testing ve Maintainability hep; Security, Performance, Data Migration, API Contract, Design, Simplification koşullu. Tek mesajda birden çok Agent çağrısı, her biri `run_in_background: false`. JSON-lines bulgu şeması, fingerprint, tekilleştirme, "`MULTI-SPECIALIST CONFIRMED`". Biri düşerse devam.
  - `/ship` Step 18 → `/document-release`: inline değil Agent (taze bağlam). Çocuk `GSTACK_SESSION_KIND=spawned` ile işaretlenir; işaret prompt metninden değil `gstack-skill-start` çıktısından kabul edilir. Spawned kuralları: "do not call AskUserQuestion; auto-choose the recommended option; for destructive/irreversible decisions, choose the conservative non-destructive option; record each auto-choice". Yetki çıkarma: merge/rebase, VERSION, CHANGELOG yeniden yazımı, force-push yok. Son satır JSON: `files_updated`, `commit_sha`, `pushed`, `documentation_section`, `decisions` ya da `error`; ebeveyn tipleri doğrular, metni güvenilmeyen veri sayar. Çalışma ağacı ortak; ebeveyn dispatch öncesi HEAD'i kaydedip sonra uzlaştırır.
  - CSO doğrulayıcısı: bulgu + yanlış-pozitif kuralları verilir, ilk tarayıcının akıl yürütmesi verilmez.
  - "new context window ≠ independent model ≠ independent oracle ≠ independent evidence source".
- **Kanıt ve olay:** "Claude Code v2.1.198 changed Agent-tool subagents to **background by default**"; ebeveyn senkron JSON bekleyip takıldı; "third recurrence of the class (`#497 → #2440 → Step 18`)". Düzeltme: açık bayrak, yapısal tarayıcı `test/run-in-background-guidance.test.ts`, yakalanan tool-call argümanını kontrol eden E2E, ~10 dk sınırlı bekleme (kopya çocuk yok, iptal, gerekirse duraklat). PreToolUse zorlama hook'u hâlâ TODO. Review Army E2E'leri modele alt ajan açmamasını söylüyor; topoloji davranışsal olarak test edilmemiş.
- **DevOS: Al** (JSON sonuç sözleşmesi, yetki çıkarma, spawned kuralları, ön-dispatch HEAD kaydı, açık foreground). Derinlik-1'e uyar: bütün dispatch ana oturumdan.

### G5. Korumalı eylem hook'ları
- **Sorun:** Yıkıcı komut, kapsam dışı düzenleme, tercihle atlanan onay.
- **İşleyiş (KD):** `/careful`: Bash için PreToolUse → `careful/bin/check-careful.sh`. Güvenli → karar yok. Orta risk (özyinelemeli `rm`, `DROP TABLE`, force-push, `reset --hard`, `kubectl delete`…) → `permissionDecision: ask`. Yüksek risk (kök/home silme, varsayılan dala force-push; yalnız basit komut) → `deny`, "best-effort advisory hard-stop, not a policy boundary". Bileşik ya da gizlenmiş komut → ask. Proje regex'i kural ekler, çıkaramaz. `/freeze`: Edit/Write için `freeze-dir.txt` sınırı, dışı deny; Bash kapsanmaz; kendiliğinden çözülmez (`/unfreeze`).
  - One-way door: `scripts/question-registry.ts` birincil tip kaynağı; `scripts/one-way-doors.ts` anahtar kelime ağı ikincil. AskUserQuestion PreToolUse hook'u: "never ask" tercihi iki yönlü soruyu otomatik karara çevirir; tek yönlü soruyu geçirir. "convenience preference is not authority to erase human confirmation on irreversible/high-stakes choices."
- **Kanıt:** `test/hook-scripts.test.ts`, `test/question-preference-hook.test.ts` (birinci taraf, deterministik). Claude dışı host'ta hook silinir, "Safety Advisory" metni kalır. v1.80 freeze'deki fail-open hatayı düzeltti.
- **DevOS: Uyarlayarak al.** Bash deny listesi ve iş dizini sınırı proje hook'u olarak. Ask yerine deny + gerekçe (Batu teknik soruyu yanıtlamaz). Tek yönlü kararlar listesi Batu'nun görmesi gerekenleri tanımlar.

### G6. Bellek ve bağlam
- **Sorun:** Oturumlar arası süreklilik; bağlamı şişirmeden hatırlamak.
- **İşleyiş (KD):** "not one generic memory".
  - A. `/context-save`: kod değiştirmez; eklemeli Markdown checkpoint. Alanlar: status, branch, timestamp, değişen dosyalar, iş özeti, kararlar, kalan iş, notlar. `/context-restore`: önce aynı daldaki en yeni, yoksa başka dal (uyuşmazlık gösterilir). Sınır: "checkpoint exists + is newest ≠ checkpoint claims are still current truth".
  - B. `~/.gstack/projects/<slug>/learnings.jsonl`. Alanlar: timestamp, skill, type, key, insight, confidence, source, branch/commit, files, trusted. Kaynak: `observed` / `user-stated` / `inferred` / `cross-model`. Eklemeli; key+type için son kayıt geçerli. "removes roughly one confidence point per 30 days" (observed/inferred); user-stated düşmez. Başka projeden yalnız `trusted === true`. Talimat benzeri içerik reddedilir. Dosya değişince kayıt geçersizleşmez.
  - C. GBrain önbelleği (`scripts/brain-cache-spec.ts`): varlık başına kapsam, TTL, bayt bütçesi (goals 12 sa, salience 4 sa…). Skill başına alt küme: `office-hours` → product, goals, user-profile, recent-decisions, salience; `plan-eng-review` → product, recent-decisions; ship/qa/investigate hiçbirini almaz. "persistent memory is routed according to work role rather than globally flooding every agent context."
- **Kanıt ve kusur:** Checkpoint için deterministik ve canlı E2E testler var. Kusur: resolver `gstack-brain-cache get ... 2>/dev/null` çalıştırıyor; stderr'deki `stale-fallback` etiketi atılıyor; model bayat bağlamı etiketsiz görüyor (kaynak izi, KD).
- **DevOS:** A: **uyarlayarak al** (checkpoint alanları iyi; açılışta git'e karşı doğrula). B: **uyarlayarak al** (repo içine taşı; kaynak türü ve güven alanları). C: **alma** (altyapı); kalıbını al: role göre bağlam yükle, bütçe koy, bayatlık etiketini modele kadar taşı.

### G7. `/investigate`
- **Sorun:** Kök neden bulunmadan yamama ve deneme-yanılma.
- **İşleyiş (KD):** "**NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.**" Belirtiler → kod yolu → son commit'ler → yeniden üretme → önceki öğrenimler → "Root cause hypothesis: <specific claim about what is wrong and why>" → log/assert ile sına. Üç hipotez düşerse dur; kullanıcı seçer: devam, uzmana devret, ölçüm ekleyip bekle. Hipotezden sonra en dar dizine freeze. Minimal düzeltme; düzeltmesiz kırılan, düzeltmeyle geçen regresyon testi; 5 dosyadan fazlası onay ister. Bitiş: tam test + ilk hatayı yeniden üretme. Rapor durumu DONE / DONE_WITH_CONCERNS / BLOCKED. Öğrenim `learnings.jsonl`'a.
- **Kanıt:** Kapsam matrisi "investigate: gate: [skill-coverage-floor] periodic: []"; yöntemin davranış testi yok. Sistemik "neden önlenmedi" analizi zorunlu değil.
- **DevOS: Al.** Üç hipotez eşiğinde durum Batu'ya değil, controller'a ya da reviewer'a gitmeli (Ç).

### G8. Geri besleme ve kendini geliştirme
- **Sorun:** Tekrarlayan hatayı kalıcı olarak önlemek.
- **`/retro` (KD):** Varsayılan dal geçmişi, testler, PR'lar, TODO, önceki retrolar, review/plan logları, skill kullanımı ve öğrenimlerden okur. Çıktı: trendler, "3 Things to Improve", "3 Habits for Next Week", kestirme borç defteri; anlık görüntü `.context/retros/YYYY-MM-DD-N.json`. Ref bayatsa BLOCK. "retro says “we should improve X” ≠ Work X has been admitted".
- **Kendini geliştirme merdiveni (KD):** "prose / local convention → real failure → named state distinction → reusable helper/resolver/runtime rule → structural invariant/scanner → behavioral/environment E2E → CI/release consequence". Örnek: sürüm bump durum makinesi, alt ajan takılması tarayıcısı. Skill akışı: `SKILL.md.tmpl` düzenle → `bun run gen:skill-docs` → ikisini birlikte commit et; CI yeniden üretip `git diff --exit-code` bakar.
- **Skill testleri (KD):** `runSkillTest()` "launches a separate `claude -p` process and captures real tool calls". Yönlendirme E2E'si fixture'daki cevap tablosunu kaldırdı; seçim yalnız açıklamalara bağlı. Kural: "test exists ≠ selected ≠ executed ≠ intended runtime exercised ≠ oracle valid ≠ finalized ≠ independently verified".
- **Kanıt:** Retro tazelik koruması regresyon testiyle sabit; merdiven birinci taraf commit geçmişinden (KD).
- **DevOS: Al.** Retro'yu iş kabulünden ayır. Tekrarlayan hatayı yazılı kurala değil hook, betik ya da teste çevir. Skill'leri `claude -p` ile tool-call düzeyinde sına (Ç: bulutta koşulabilirliği O11 doğrulamalı).

## 4. Hermes Agent

Hedef: `NousResearch/hermes-agent@c4a5deef` (manifest 0.21.0). Statü: "ACTIVE PARTIAL"; dört geçici sentez, final CORE yok; görev kalitesi sorusu (Q60) araştırılmadı. Kanıt: kaynak okuması + sınırlı bileşen deneyleri; kurulu Hermes çalıştırılmadı.

### H1. Kalıcı bellek: MEMORY.md / USER.md
- **Sorun:** Her oturumda gereken bilgiyi küçük ve güvenli tutmak.
- **İşleyiş (G, `evidence/2026-09-09-memory-pending/upstream/memory_tool_store.py`, `memory_tool.py`):** İki dosya. "MEMORY (your personal notes)" ve "USER PROFILE (who the user is)". Girdiler `ENTRY_DELIMITER = "\n§\n"` ile ayrılır. Sınır karakterle: `memory_char_limit: int = 2200, user_char_limit: int = 1375`. Oturum başında donmuş anlık görüntü: "Frozen load-time snapshot (NOT live state — mid-session writes don't touch it, preserving the prefix cache)". Araç açıklaması:
  > "WHEN: only for facts that apply to EVERY session regardless of task: who the user is, stable environment facts, standing conventions with no task home. Anything learned while doing a task (procedures, pitfalls, and the user's preferences and corrections for that kind of work) belongs in the task's skill via skill_manage, where it loads only when relevant; memory is injected into every turn and must stay small."
  > "SKIP: trivial/obvious info, easily re-discovered facts, raw data dumps, task progress, completed-work logs, temporary TODO state (use session_search for those). Reusable procedures belong in a skill, not memory."
  - Dolunca ekleme reddedilir: "Consolidate now: use 'replace' to merge overlapping entries into shorter ones or 'remove' stale or less important entries … then retry this add — all in this turn." Toplu işlem ya hep ya hiç; bütçe son durumda ölçülür; turda en çok 3 başarısız birleştirme. Başarı yanıtı girdileri geri göstermez: "echoing entries invites the model to "find more to fix"".
  - Yazmadan önce ayrı `.lock`, diskten yeniden okuma, dış değişiklikte `.bak` + ret, atomik yazma. İçerik injection/exfil taramasından geçer; bellek sistem prompt'una girer.
  - Sıkıştırmada (KD, synthesis 02): "normal kabul edilmiş compaction sınırında HERMES cache'i geçersizleştirir, belleği diskten yeniden yükler, sistem mesajını gerçekten yeniden oluşturur".
- **Kanıt ve kusur (KD):** M4: saklı sistem mesajı yeniden kullanılınca onaylanmış yeni bellek görünmeyebiliyor; karşılaştırıcı bellek revizyonuna bakmıyor. M01: yazma hatasında canlı liste ile disk ayrışabilir.
- **DevOS: Al** (politika metni ve sınıflama). CLAUDE.md = her oturum gerçekleri; skill = prosedür; iş kaydı = ilerleme. **Uyarlayarak al** (karakter bütçesi CLAUDE.md'ye; dolunca birleştirme kuralı).

### H2. Arka plan inceleme: deneyimden öneriye
- **Sorun:** Konuşmadan yeniden kullanılabilir dersi ana işi bozmadan çıkarmak.
- **İşleyiş (KD, `agent/background_review.py`):** Konuşma bitince snapshot ayrı bir AIAgent fork'unda yeniden işlenir. Farklı modele giden özet son 24 mesajı tutar; eski kullanıcı metni 300, asistan metni 200 karaktere kısılır; eski araç sonuçları düşer. Şema ebeveynle aynı görünür ama izinli küme dar: memory/skills + `read_file`/`search_files`. "`write_file`, genel `patch`, terminal, mesaj gönderme ve delegation varsayılan review kümesine dahil edilmez." Korumalar: pinned, bundled/hub, dış ve kullanıcıya ait skill'e yazma yok; sahiplik belirsizse ret; tam okunmamış dosyaya yazma yok; birleştirme silmesi `absorbed_into` ister. Bütçe: 16 iterasyon, 600.000 girdi token.
  - Prompt'un iyi yanı: "class-level, yeniden kullanılabilir prosedürleri; transient hataları kalıcı yasaklara dönüştürmemeyi; çözülememiş denemeleri çalışır yöntem diye kaydetmemeyi ister." Riskli yanı: "çoğu oturumda bir güncelleme yapmayı kuvvetle teşvik eder; no-op'u kaçırılmış öğrenme olarak çerçeveler". Hipotez: aşırı kural üretimi.
- **Kanıt:** Kaynak ve whitelist test kaynağı okundu, testler koşulmadı (KD).
- **DevOS: Uyarlayarak al.** Her iş sonunda "öğrenim önerisi" adımı; salt okur araçlarla; önerileri bekleyen kayıt olarak yaz. "Değişiklik yok" geçerli sonuç olsun. Arka planda değil, oturum boşa düşmeden önce çalışmalı.

### H3. Yazma onayı ve bekleyen kayıt
- **Sorun:** Kalıcı bellek/skill yazımını onaya bağlamak.
- **İşleyiş (G, `write_approval.py`):** "``false`` (default) writes freely; ``true`` never commits directly: it prompts inline (memory, interactive CLI only) or **stages** the write under ``<HERMES_HOME>/pending/{memory,skills}/<id>.json`` for out-of-band review." Kayıtta payload, origin, tarih, özet. Onaylanınca `apply_memory_pending` / `apply_skill_pending`; başarıda kayıt silinir.
- **Kusurlar (KD, yerel bileşen deneyleri):** Toplu skill değişikliğinin önizlemesi yalnız "(batch on '')" gösteriyor (D02). Yeniden adlandırma hatasında bile kimlik ve `staged:true` dönüyor, kayıt bulunamıyor (D05). Alt işlemde istisna olunca geri alma yok (B04). Onay sonrası uygulamada origin yeniden bağlanmıyor.
- **DevOS: Uyarlayarak al.** Öneriler `pending/` benzeri commit edilmiş dosyalarda dursun. Onaylayan reviewer rolü olsun, Batu değil. Onay ekranı gerçek diff'i göstermeli.

### H4. Curator: skill kütüphanesinin bakımı
- **Sorun:** Kütüphanenin şişmesi ve bayatlaması.
- **İşleyiş (KD, `agent/curator.py`, `tools/skill_usage.py`):** "bakım varsayılan olarak etkin, LLM consolidation varsayılan olarak kapalıdır." Durumlar: active / stale / archived. İlk görüşte yalnız zaman kaydedilir. Pinned ya da cron'un andığı skill atlanır. Yeni ve hiç kullanılmamış skill arşivlenmez. Bayat skill kullanılırsa tekrar active olur. Değişiklik öncesi snapshot denenir; hata olursa bakım yine sürer. Birleştirme sonrası cron'daki skill referansları yeniden yazılır. Sayaçlar: `bump_use`, `bump_patch`. Not 30: "**yüklenmiş veya yeniden kullanılmış diye kaydedilmiş olmak etkili öğrenme/görev başarısı değildir.**"
- **Kusur (KD):** C-A: boş aday metni "No curator-managed skills to review." ama kontrol "No agent-created skills" arıyor; atlama hiç tetiklenmiyor. C-B: prompt 10'dan az arşivi erken durma sayıyor; sayı hedefi baskısı.
- **DevOS: Uyarlayarak al.** Az sayıda skill için yaş/kullanım kuralı gereksiz (Ç). Alınacak: pinned koruması, arşivle-silme, değişiklik öncesi snapshot, "kullanım ≠ fayda".

### H5. Alt ajana görev devri (`delegate_task`)
- **Sorun:** Alt ajana yeterli ama sınırlı bağlam ve yetki vermek.
- **İşleyiş (KD, `evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md`):** Çocuk yeni AIAgent. Hedef/bağlamdan odak prompt'u üretilir. "`skip_context_files=True`, `skip_memory=True`, clarify_callback=None ve platform=subagent belirtilir"; ebeveyn geçmişi geçmez. Rol derinlik ve `orchestrator_enabled` ile belirlenir, modelin istediği rolle değil; `max_spawn_depth` var. Bütçe ayrıdır. Worktree isteğe bağlı; kurulamazsa paylaşılan alan. Sonuç: önce yapılandırılmış hata alanları. "`status=completed` ile `exit_reason=max_iterations` ve `truncated=True` birlikte bulunabilir". Şema istenirse bir düzeltme turu. Şemanın kendisi özeti self-report sayar. Ebeveyne transcript değil özet + metadata gider. Uzun özet baş/son kesilir, tamamı spill dosyasına.
- **Kanıt:** Yalnız kaynak okuması; çalıştırma yok (KD, CHECKS-NOT-RUN).
- **DevOS: Al** (hedef + bağlamı açık ver; tarihçeye güvenme; özeti doğrula; `truncated` benzeri alanı rapor şemasına koy). Orchestrator rolü **alma** (derinlik-1).

### H6. Kalıcı iş: Kanban task / run / claim
- **Sorun:** Çok denemeli işte hangi sonucun geçerli olduğu.
- **İşleyiş (KD, `evidence/2026-09-10-kanban-task/RESEARCH.md`):** "`tasks` işi, `task_runs` o işi yürütme denemelerini, `task_events` geçişleri, `task_links` bağımlılıkları" taşır; `current_run_id` etkin denemeyi gösterir. Durumlar: todo, ready, running, blocked, triage, done. Claim alınırken ebeveyn işler yeniden kontrol edilir. `complete_task(expected_run_id)` geçersiz kalmış denemenin geç tamamlamasını reddeder (K03). "Running kartı bırakıp rc=0 ile çıkan çalışan, görev completion'ı olarak kabul edilmez". `request_review` implementer/reviewer kökenini kaydeder; `request_changes` işi kayıtlı implementer'a döndürür. `build_worker_context`: görev gövdesi, ekler, önceki denemeler, tamamlanmış ebeveyn devirleri (anlık görüntü olarak), yorumlar; sınırlı liste ve metin. Goal modunda: "Judge DONE, Kanban'da worker'a finalize istemi üretir; doğrudan task done yazmaz."
- **Kanıt (KD):** K01–K08 gerçek SQLite ama indirgenmiş DDL ve seçilmiş fonksiyonlar. K06: commit sonrası callback hatasında çağıran istisna görür, görev yine done.
- **DevOS: Uyarlayarak al.** DB yerine iş başına dosya: denemeler, olaylar, bağımlılıklar, devir notları. Kavramlar: deneme kimliği, beklenen denemeyle tamamlama, "süreç bitti ≠ iş kabul edildi". Tek controller'da claim kilidi gereksiz (Ç).

### H7. Devam mekanizmaları: goal, loop, heartbeat, cron
- **Sorun:** İşi zaman içinde sürdürmek ve yeniden uyandırmak.
- **KD (synthesis 03, 04):** Kimlikler ayrı: task ID süreklilik, run ID deneme, claim çalışma hakkı, session ID konuşma, turn ID yürütme. Dört durum ayrı: kayıtta done / çalışma durdu / ölçüt karşılandı / teslim edildi. Cron `context_from=self` en yeni çıktıyı seçer; boş ya da hatalı yeni dosya eski anlamlı raporu gölgeleyebilir.
- **DevOS: Alma** (daemon, gateway). Dört durum ayrımını ve "en yeni çıktı ≠ son geçerli rapor" dersini **al**. Zamanlama için routines / send_later (O11).

## 5. mattpocock-skills

Statü (G): "**PLANNED / RESEARCH NOT STARTED**". Yalnız ön eleme sinyalleri var; META'nın kendi uyarısı: bunlar bulgu değil. Sinyaller (alıntı): "an explicit split between **user-invoked** orchestration skills and **model-invoked** reusable disciplines"; "user-invoked skills cannot silently chain into other user-owned workflows, while they may delegate to model-invoked disciplines"; "project-level domain-language artifacts (`CONTEXT.md`, optional context maps and ADRs)"; `wayfinder` ile issue tracker üzerinde çok oturumlu plan ("destination, decision tickets, blocking relationships, frontier and deliberately unresolved “fog of war”"); "Standards vs Spec review axes delegated to separate subagents"; tekrarlayan hataları "deterministic checks"e çeviren retrospektif, "preferring mechanical enforcement over prompt rules when possible".
- **DevOS:** Kanıt yok; kontrol listesi olarak tut: kullanıcı/model çağırımı ayrımı (`disable-model-invocation`? O11), alan sözlüğü dosyası, Standards/Spec reviewer ayrımı. Upstream okunmadan alma.

## 6. Roller karşılaştırması

| Sistem | Roller | Yetki ayrımı |
|---|---|---|
| Superpowers | insan; controller (ana oturum); implementer; task reviewer (2 hüküm); re-reviewer; final reviewer | insan: ne yapılacak + merge/PR/keep/discard; controller: çoğu çatışma (karar kaydıyla); 4 durma sınıfı insana |
| gstack | CEO, Eng, Design, DX reviewer; güvenlik (CSO) + doğrulayıcı; Review Army uzmanları; Red Team; Codex dış ses; doc-sync çocuğu; QA; ship ebeveyni | Roller "one operational agent instance occupying a role/participation position for a bounded episode"; insan: yön, kapsam, merge, rollback, tek yönlü kapılar |
| Hermes | ön plan ajanı; background_review fork'u; curator; delegate çocuğu (leaf/orchestrator); Kanban worker; reviewer; goal judge | origin ContextVar (`foreground` / `background_review`); sahiplik korumaları; yazma onay kapısı |

Ortak ders (Ç): Rol etiketi yetki değildir; yetki araç listesi ve hook'la sınırlanmalı. gstack CSO "Read-only" der ama Write aracına sahiptir.

## 7. Dersler

| Ne oldu | Kök neden | Önlem | Kaynak |
|---|---|---|---|
| Ebeveyn alt ajanı beklerken takıldı (3. tekrar) | Senkron bekleme örtük; Claude Code varsayılanı değişti | Foreground'u açık yaz; tarayıcı + tool-call E2E | gstack multi-agent §3 |
| Bayat bellek etiketsiz sunuldu | Etiket stderr'deydi, `2>/dev/null` attı | Etiket içerikle aynı kanalda | gstack memory §12 |
| Uzak sürüm okunamadı → `UP_TO_DATE`; setup düştü → yine `UPDATED` | Hata olumlu duruma çevrildi | Bilinmeyen = UNKNOWN | gstack self-dev §7–8 |
| `REVERTED` yazıldı, üretimin döndüğü doğrulanmadı | Eylem, hedef durum sayıldı | Etkiden sonra gerçek durumu oku | gstack deploy §16 |
| Hook skill yokken exit 0 verdi | Okuma hatası içeriğe çevrildi | Eksik/boşsa görünür hata | Superpowers U01 F05 |
| SDD defteri worktree silinince kayboldu | Kayıt `.gitignore`'lu geçici alanda | Karar ve kanıtı commit et | Superpowers U05 F40 |
| İki plan aynı alana yazdı | Kimlik basename'e bağlı | Tam yol + revizyon | Superpowers U02 F16 |
| Test eski sözleşmeyi ödüllendirdi; fixture cevabı sızdırdı | Anahtar kelime grep'i; oracle sızıntısı | Davranışı sına | Superpowers U03 F26; gstack testing §22 |
| Review Army ve `/investigate` davranışsal test edilmedi | Test topolojiyi dışladı; matris yapısal zeminle doldu | Test edilen iddiayı adlandır | gstack multi-agent §11, investigate §14 |
| Onay önizlemesi gerçek değişikliği göstermedi | Önizleme ve uygulama farklı biçim okuyor | Onay nesnesi = uygulanacak diff | Hermes not 04 F02 |
| Boş aday atlaması hiç çalışmadı | İki metin sabiti uyuşmuyor | Durumu yapıyla ilet | Hermes not 03 C-A |
| Güncelleme ve birleştirme baskısı | No-op başarısızlık sayılıyor; kota | "Değişiklik yok" geçerli; kota yok | Hermes not 02 §8, 03 C-B |
| Onaylı bellek sonraki turda görünmeyebilir | Saklı prompt revizyonsuz yeniden kullanıldı | Bellek revizyonunu prompt kimliğine bağla | Hermes not 15 |
| Belge ile kod çelişti | Türetilmiş belge güncellenmedi | Belgeyi testle bağla | Hermes not 03; gstack host-adapters §8 |

