# O9 — Orkestrasyon, iş grafı, iş takibi, spesifikasyon güdümlü geliştirme, çok ajanlı kalıplar

EXP-007 DevOS okuma turu, küme O9. Okuma tarihi: 2026-09-27. Dal: `claude/hopeful-pascal-7bekcd`. Kaynak kökü: `research/studies/`. Kanıt dili: **kaynak diyor** (study ya da upstream metni), **gözledim** (bu okumada kendim gördüm), **çıkarım** (benim yorumum), **bilinmiyor**. Alıntılar özgün dilindedir. "WMPC" = `work-management-project-control`.

## DevOS için en önemli çıkarımlar

1. **Tek "durum" sütunu yetmez.** WMPC'nin sonucu: "The corpus rejects the shortcut `large-work management = task tracking + dependencies`." İş kaydında ayrı tutulmalı: yaşam döngüsü etiketi, türetilmiş hazır olma, sahiplik + canlılık, doğrulama, entegrasyon, Batu kabulü (kaynak diyor: WMPC STATE'teki 17 ayrım).
2. **"Açık" iş "şimdi yapılabilir" iş değildir.** Sonraki iş, ajanın açık işler arasından seçmesiyle değil, kayıttan türetilen hazır listeden gelmeli (Beads: `bd ready` ≠ `bd list --status open`). Araç olarak değil kavram olarak al: dosya + küçük betik (çıkarım).
3. **İlişki türlerini karıştırma.** `blocks` hazır listeyi ve kapatmayı etkiler; `discovered-from` yalnız kökendir, sıra koymaz; ebeveyn-çocuk yapıdır ama Beads'te bloklu ebeveyn çocuklarını da bloklar. Keşfedilen iş otomatik engel olmaz, uygulayıcı da onu kendisi çözmez: "File discovered work — `bd create` for bugs found, don't fix them yourself" (Gas Town).
4. **`in_progress`, canlı bir sahip olduğunu kanıtlamaz.** Sahiplenme atomik olmalı ve süreli kira (lease) taşımalı; kira dolunca iş hazır listeye döner (Beads `bd reclaim`). Bulutta oturum boşta geri alındığı için bu doğrudan gerekir. Kira yalnız işbirlikçi kuraldır: RPD probe'unda kira A'dayken B kaydı güncelleyebildi.
5. **"Bitti" katmanlıdır:** ajan "bitti" der → iş maddesi kapanır → iş emri kapanır → doğrulanır → ana dala girer → Batu kabul eder → amaç gerçekleşir. Her biri ayrı alan (Gas Town `gt done`/convoy/Refinery; Leantime'da "Waiting for Approval" DONE değildir; WMPC 08 §6).
6. **Plan yaşar ama geçmiş yeniden yazılmaz.** Spec Kit converge yalnız `tasks.md` sonuna `## Phase N: Convergence` ekler; eski görevleri "rewrite, renumber, reorder, or delete" etmez; her yeni görev kaynağını taşır (`per FR-003 (missing)`). Onaylı plan v1 ile sonradan değişen plan ayrı sürüm olmalı (playbook F4).
7. **Dosyanın var olması kabul değildir.** OpenSpec: "It doesn't read the file to decide whether the artifact is complete." Artefakt DAG'i planlama sırası için iyi; uygulamaya geçiş ayrı kapıdır (`apply.requires`); anlamsal kabul üçüncü, ayrı adımdır.
8. **İş kaydı ile orkestrasyon ayrı katmanlardır.** Gas Town işi Beads'te tutar; üstüne atama, kapasite, izleme ve entegrasyon ekler. Kimlik kalıcı, oturum geçicidir ("persistent identity but ephemeral sessions"). DevOS rolleri ve iş geçmişi dosyada kalır, oturumlar tek kullanımlıktır: bulut gerçeğine birebir uyar (çıkarım).
9. **Olayla ilerlemek yetmez; kayıttan periyodik uzlaştırma gerekir.** Gas Town 5 sn'lik olay yoklamasına ek olarak 30 sn'de bir "stranded scan" koşar (çökme ve yeniden başlama sonrası kaçanlar için). Bulutta sürekli çalışan daemon yok; her oturum başında uzlaştırma taraması koşmalı (çıkarım). Zamanlanmış tetik seçeneğini O11 doğrulamalı.
10. **Batu gizli orkestratör değildir.** Şunları sistem yapmalı: fresh verifier başlatmak, hedef sürüme bağlamak, doğrulama sonucunu entegratöre taşımak, onarım ve yeniden doğrulama başlatmak, bütün dalların dönüp dönmediğini izlemek (multi-agent-patterns §16.2). İnsan kapısı yalnız yetki, değer ve geri dönüşsüz risk içindir; "Batu onayladı" ≠ "teknik olarak doğrulandı".
11. **Karmaşıklığı yalnız koruduğu gereksinimle ekle.** "one bounded agent + one tool + deterministic verification + persistent result" geçerli bir sonuçtur (C10). Paralel dal ancak birleştirme sözleşmesi varsa açılır: temel sürüm, izinli değişiklik, çakışma anlamı, birleştirme yetkisi (C3).
12. **Tavsiye ≠ zorlama; yetki geçişlidir.** CLAUDE.md ve skill bağlamdır; tutması gereken kural hook, izin ya da testle zorlanmalı. Anthropic'in kısıtlı ajanı, Slack üzerinden yazma yetkisi olan başka bir Claude'a düzeltme push'latmaya çalıştı; insan kapısı durdurdu (playbook).
13. **Çelişki:** multi-agent-patterns "Claude Code alt ajan derinliği varsayılan 3 (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`)" diyor; brief'teki bilinen bulut gerçeği derinlik 1. Tasarım iç içe alt ajana dayanmamalı; kesin değeri O11 verir.
14. **Kanıt sınırı:** Bu kümedeki hiçbir hedef bu projede kurulmadı ve çalıştırılmadı (hepsi kaynak okuması). Tek koşu RPD'nin sentetik Python prototipi (25 test + 2 probe). Git içinde düz dosyayla tutulan minimal iş kuyruğu (TASKS.md) WMPC'de ertelenmiş hedef; DevOS'un en olası biçimi hiç incelenmedi.

## 0. Kapsam

| Kaynak (`research/studies/`) | Okunan dosyalar | Durum |
|---|---|---|
| `gastown/` | META, FINDINGS, SOURCE-LEDGER | tam (3/3) |
| `beads/` | META, FINDINGS, SOURCE-LEDGER | tam (3/3) |
| `multi-agent-patterns/` | META, CONVERSATION-SYNTHESIS, SOUL-DEVELOPMENT-OS-ASSESSMENT | tam (3/3) |
| `openspec/`, `spec-kit/` | META, FINDINGS, SOURCE-LEDGER | tam (3/3 + 3/3) |
| `anthropic-ai-native-sdlc-playbook/` | INDEX, META, STATE, 00, 01, 02, 03, 04 | tam (8/8) |
| `work-management-project-control/` | INDEX, META, STATE, METHOD, PLAN, 08, 09, 10 | tam (8/8; 01–07 diye dosya yok, birimler hedef paketlerde) |
| `recursive-prerequisite-discovery/` | META, ASSESSMENT, MECHANICAL-OBSERVATIONS | tam (3/3) |
| `flowable/`, `openproject/`, `leantime/` | META → ilgili bulundu → FINDINGS, SOURCE-LEDGER | tam (3/3 her biri) |
| `erpnext/` | META | kısmen. FINDINGS ve SOURCE-LEDGER okunmadı: konu kurumsal zaman, maliyet, fatura, stok bağlama; DevOS iş döngüsünde karşılığı yok. META'daki kapanış kapısı ve WMPC 09'daki "türetilmiş toplam ≠ kaynak kayıt" ayrımı yeterli. |
| `ponytail/`, `i-have-adhd/` | META (pakette tek dosya; araştırma başlamamış) | tam; içerik bulgu değil, aday kaydı |
| `public-apis/` | META | kısmen. RESEARCH.md okunmadı: konu API keşfi, orkestrasyon ve iş kaydıyla ilgisiz. |

**Ek (kümenin dışı, doğrulama için):** Study'lerin kendi pinned ref'lerinden 7 upstream dosya salt okunur GET ile indirildi (gözledim: hepsi HTTP 200), tamamı okundu, sonra scratchpad'den silindi: spec-kit `templates/commands/tasks.md` ve `templates/commands/converge.md` @`0ced288`; OpenSpec `docs-lab/reference/schemas/schema-yaml.md` @`bae58cf`; beads `README.md` @`71c4cd0`; gastown `docs/design/convoy/convoy-lifecycle.md`, `docs/glossary.md`, `docs/concepts/molecules.md` @`649b832`. Aşağıda bunlara "upstream" diyorum.

**Okunmayan, kümeye girmeyen:** `research/soul-context/STATE.md` (RPD devir yetkisinin durduğu yer; O1), RPD'nin incelediği `soul-development-os_02` planı (O1/O2), RPD'nin özgün ekleri (repoda yok; yalnız SHA-256 kimliği var).

**Kanıt sınıfı (kaynak diyor):** Hedef çalışmalarının hepsi kendini "source/documentation-bounded" diye tanımlıyor. Beads, Gas Town, OpenSpec, Spec Kit, Flowable, OpenProject ve Leantime bu projede kurulmadı, koşulmadı. Anthropic'in üretkenlik ve güvenlik sayıları birinci taraf iddiasıdır.

## 1. İş kaydı mekanizmaları

Aksi yazılmadıkça her mekanizmanın kanıtı yalnız kaynak okumasıdır; bu projede koşu yoktur (§0).

### 1.1 Türetilmiş hazır liste — Beads
- **Sorun:** Ajan açık işler arasından seçerken bloklu, ertelenmiş ya da önkoşulu eksik işi alır.
- **Nasıl (kaynak diyor, `beads/FINDINGS.md` §2):** "`bd list --status open` — open items; `bd ready` — work that currently satisfies ready-work predicates." Yüklemler: durum kategorisi `active`; `is_blocked = 0` (elle girilen değil, "persisted readiness projection"); pinned/infra türleri hariç; `defer_until` ve ertelenmiş ebeveyn yayılımı; filtreler; öncelik sırası. Döngü (upstream README): `bd create → dependency graph → bd ready → bd update --claim → bd close → (blockers released) → bd ready`.
- "Hazır iş yok" beş ayrı durum olabilir (§11): "legitimate waiting; everything complete; external condition not met; actor claims consumed frontier; a malformed/cyclic/livelocked work graph."
- **Yol:** `research/studies/beads/FINDINGS.md` §2, §11; upstream `internal/storage/sqlbuild/ready.go` (ledger'da adı geçiyor; ben okumadım).
- **Kanıt:** yalnız kaynak okuması.
- **DevOS: uyarlayarak al.** Beads bir Go ikilisi ve Dolt veritabanıdır; bulutta her oturumda kurulum ister. Dolt verisi `bd dolt push` ile git uzağındaki `refs/dolt/data`'ya gider (upstream README); git proxy'nin buna izin verip vermediği **bilinmiyor**. Kavramı al: iş dosyalarından hazır listeyi türeten betik ve "hazır iş yok" teşhisini beş nedene ayıran çıktı (çıkarım).

### 1.2 İlişki türü ≠ kontrol etkisi — Beads, OpenProject, ERPNext
- **Sorun:** Tek bir `depends_on` alanı "parçasıdır", "önce olmalı", "bundan doğdu" ve "kapatmayı engeller" anlamlarını karıştırır.
- **Nasıl (kaynak diyor):** Beads kaynağında `AffectsReadyWork()` şunlar için doğru: `blocks`, `parent-child`, `conditional-blocks`, `waits-for`. `discovered-from` yalnız kökendir: "`current work → discovers new work` does not automatically imply: `new work blocks current work`." Karışık blocks/parent-child zincirleri "logical livelock" üretebilir (§3). OpenProject: "**blocks/blocked-by** prevents the blocked work package from being set closed/resolved while the blocker remains open"; öncül/ardıl yalnız tarihi etkiler; includes/requires otomatik etki taşımaz. ERPNext META: "A task cannot move to `Completed` while its declared dependencies are not `Completed` or `Cancelled`." WMPC 08 §4 her ilişki için üç soru sorar: anlamı ne, şu anki etkisi ne, etki nerede zorlanıyor.
- **Kanıt / ders:** Beads'in `DEPENDENCIES.md` rehberi yalnız `blocks`'un hazırlığı etkilediğini söylüyor; kaynak kodu parent-child'ı da sayıyor (`beads/SOURCE-LEDGER.md`). Belge koddan kaymış.
- **DevOS: az sayıda türle al.** `engeller` (hazır listeden düşürür, kapatmayı engeller), `ebeveyn` (yapı; bloklu ebeveynin çocuğu bloklayıp bloklamadığı açıkça yazılır), `kesfedildigi` (yalnız köken). Etkiyi belge değil betik uygular; kural ve betik birlikte test edilir (çıkarım; Beads'teki kaymadan ders).

### 1.3 Atomik sahiplenme, kira ve geri alma — Beads; RPD probe'ları
- **Sorun:** Birden çok ajan aynı işi alır; ölen oturumun işi sonsuza dek `in_progress` kalır.
- **Nasıl (kaynak diyor, `beads/FINDINGS.md` §6–7):** `bd update <id> --claim` tek işlemde: "1. reads the current issue inside the transaction; 2. validates that status is claimable ...; 3. checks assignee slot / claim-pool eligibility; 4. CASes against an opaque row-version; 5. sets assignee + `in_progress` ...; 6. records claim/update events; 7. grants a liveness lease." Aynı aktörün tekrar sahiplenmesi idempotenttir; başkası kazandıysa çakışma döner. `ClaimReadyIssueInTx` hazır işi hesaplayıp aynı işlemde sahiplenir. Kalp atışı durursa "`bd reclaim` can revert stale-leased `in_progress` work back to ready and clear the assignee."
- **RPD probe'u (kaynak diyor, `recursive-prerequisite-discovery/MECHANICAL-OBSERVATIONS.md`):** worker-A kira sahibiyken, koordinatör arayüzü worker-B adına çağrıldı ve kayıt "updated_by worker-B" oldu: "Fencing yalnız ilgili işbirlikçi çağrı yolunda kontrol edilir; bütün dosya/araç etkisi veya OS izin sınırı değildir."
- **DevOS: uyarlayarak al.** İş maddesinde `sahip` (oturum kimliği + rol) ve `kira_bitis` alanları. Oturum geri alınınca kira kendiliğinden dolar; uzlaştırma taraması işi hazır listeye döndürür. Git'te "atomik" tek commit + push demektir; eşzamanlı yazımda reddedilen push çakışmayı yakalar (çıkarım, denenmedi). Kira mekanik bir sınır değildir; gerçek sınır dal ayrımı ile izin/hook'tur (O11).

### 1.4 Durum etiketi ≠ davranış kategorisi — Beads, Leantime
- **Nasıl (kaynak diyor):** Beads'in yerleşik durumları `open, in_progress, blocked, deferred, closed, pinned, hooked`; özel etiketler dört kategoriye bağlanır: `active` (hazır olabilir), `wip`, `done`, `frozen`. "This lets a domain-specific word such as `ready-for-agent` or `review` acquire a system behavior without making the engine hard-code every vocabulary." Leantime: "The default “Waiting for Approval” state is an `INPROGRESS` semantic state, not DONE." Hedefin durumu (`on track / at risk / miss`) görev durumundan ayrı bir sözlüktür.
- **DevOS: al.** Türkçe serbest etiketler ("Batu kabulü bekliyor" gibi) dört kategoriden birine bağlanır; betik yalnız kategoriye bakar. "Kabul bekliyor" `wip`'tir, `done` değildir.

### 1.5 Yeniden açma ve aşağı akışın yeniden hesaplanması — Beads
- **Nasıl (kaynak diyor, §8):** Yalnız `done` kategorisindeki iş yeniden açılır: iş `open`'a döner, kapanış bilgisi ve `defer_until` temizlenir, kira silinir, olay yazılır, etkilenen işlerin `is_blocked` değeri yeniden hesaplanır. "Thus reopening a prerequisite can re-block work that had become ready after it was closed."
- **DevOS: al.** Türetilmiş alanlar (hazır, bloklu) elle yazılmaz; her değişiklikten sonra betik yeniden hesaplar.

### 1.6 Artefakt DAG'i ve ayrı uygulama kapısı — OpenSpec
- **Sorun:** Plan bilgisinin hangi sırayla üretileceği ile uygulamanın ne zaman başlayabileceği birbirine karışır.
- **Nasıl (kaynak diyor):** `openspec/specs/` güncel doğruluktur; `openspec/changes/<change>/` öneri paketidir (proposal, delta spec, design, tasks); arşivlemede delta'lar güncel spec'e katılır. Upstream `schema.yaml` örneğinden (kısaltılmış):
  ```yaml
  artifacts:
    - id: proposal
      generates: proposal.md
      requires: []
    - id: tasks
      generates: tasks.md
      requires:
        - proposal
  apply:
    requires:
      - tasks
    tracks: tasks.md
  ```
  "Artifact `requires` controls planning order. `apply.requires` controls when apply instructions become ready." Uygulama durumu: `blocked` (dosya yok ya da görev metinli kutucuk yok), `ready` (en az bir bekleyen görev), `all_done`. Tamamlanma: "OpenSpec checks whether the output exists. It doesn't read the file to decide whether the artifact is complete."
- Aynı değişiklik mi, yeni değişiklik mi (FINDINGS §8): "same goal, better approach → revise existing change; ... fundamentally different problem/intent → create a new change."
- **Kanıt / ders:** upstream doğrulama tablosu: "A field is misspelled, such as `instrution` | OpenSpec ignores it. Validation doesn't report the typo."
- **DevOS: uyarlayarak al.** İş paketi klasörü = değişiklik paketi; planlama artefaktları arasında `requires`; uygulamaya geçiş ayrı kapı. Ama "dosya var" yalnız "üretildi" demektir; "kabul edildi" doğrulayıcıdan gelen ayrı bir alandır. "Güncel kanon ≠ önerilen değişiklik" ayrımı DevOS'un kanon ve karar dosyaları için doğrudan yararlı (çıkarım).

### 1.7 Görev biçimi ve append-only yakınsama — Spec Kit
- **Sorun:** İlk ayrıştırma hep eksik kalır; eksikler ya sessizce kabul edilir ya da plan geriye dönük yeniden yazılır.
- **Nasıl (kaynak diyor):** Süreç `constitution → specify → [clarify] → plan → [checklist] → tasks → [analyze] → implement → converge`; plan'dan önce yalnız specify zorunlu. Upstream `tasks.md` şablonu: "- [ ] [TaskID] [P?] [Story?] Description with file path". `[P]`: "ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)". Fazlar: Setup → "Foundational (blocking prerequisites - MUST complete before user stories)" → her kullanıcı hikâyesi için "a complete, independently testable increment" → Polish. "each task must be specific enough that an LLM can complete it without additional context."
- **Converge (upstream `converge.md`):** "**APPEND-ONLY, NEVER REWRITE**: The command's **only** write is appending a new `## Phase N: Convergence` section to `tasks.md`." Görev satırı: "- [ ] T042 <imperative description> per <source-ref> (<gap-type>)"; boşluk türleri `missing / partial / contradicts / unrequested`; önem CRITICAL/HIGH/MEDIUM/LOW. Eksik yoksa `tasks.md` "byte-for-byte unchanged" kalır. "This is **not** a diff tool": geçmişe değil bugünkü koda bakar; kapsam yalnız artefaktların adlandırdığı dosyalardır.
- Analyze salt okunurdur; hatayı sahibine yollar (gereksinim → specify, tasarım → plan, ayrıştırma → tasks). Checklist maddeleri gözden geçirenindir; implement onları kendisi işaretlemez (FINDINGS §6). Büyük işte uygulama dilimlenir: "whole-plan state ≠ current-session admitted work slice" (§17).
- **Kanıt:** "`Converged` is an agent assessment against selected artifacts/code scope, not an independent verification oracle" (META). Tekrarlanan converge'ün doğruya yakınsadığı kanıtlanmadı. Upstream şablonlarda zorunlu hook bile metinle yürür: "Emitting the block alone does not run the hook." Prosedürel sıra, zorlanan geçiş değildir.
- **DevOS: biçimi, append-only kuralını ve kaynak referansını al; converge'ü uyarlayarak al.** Yakınsama denetimini üretici değil ayrı bir doğrulayıcı alt ajan koşar, çıktısı kanıt dosyasına bağlanır. Oturum başına alınan dilimi sınırlamak bağlamın %80'de sıkıştırılmasına karşı da korur (çıkarım).

### 1.8 Niyet → spec → plan zinciri ve plan sürümleri — Anthropic playbook
- **Nasıl (kaynak diyor, `01-PLAYBOOK-RESEARCH.md` §3, §5, §7.1):** `intent.md → spec.md → plan.md → code diff + tests → PR + review findings → deployment / production evidence → incident / breached control band → new intent.md`. `intent.md` şunları taşır: "what is wanted; why it matters; who/systems are affected; constraints; open questions"; ürün sahibi commit'ten önce düzeltir. `plan.md` şunları adlandırır: "files expected to change; order of operations; risks; tests/proof expected."
- **Risk (`04` F4):** Plan uygulamadan sonra güncellenirse "A bad plan can appear to have been “correct”". Önerilen yapı (satırlar `;` ile ayrıldı): "plan v1 — accepted before mutation; execution deviation record; new evidence / reason; revised plan v2 or as-built record; fresh downstream verification where material". Başka bir risk: "requirement laundering" (temiz görünen niyet asıl amacı sessizce değiştirir).
- **DevOS: al.** Batu'nun amacı niyet kaydına girer (ne, neden, kısıt, açık sorular); Batu yalnız "doğru anlaşıldı" onayı verir, teknik onay vermez. Plan sürümleri ve sapma kaydı ayrı tutulur.

### 1.9 Etkin ≠ aktif; yürüyen işi yeni plana taşıma — Flowable
- **Nasıl (kaynak diyor):** CMMN plan öğesi durumları `available, enabled, active, disabled, completed, failed, suspended, terminated`. "when a manual-activation rule evaluates true, a plan item becomes **enabled** instead of automatically becoming **active**." "Changing the canonical plan does **not** automatically change already-running work." Geri gitme tek işlem değildir: migrate, retry, cancel, terminate, compensate, suspend. İnsan görevi: "`candidate pool → claim → exclusive assignee → complete → engine continues`."
- **DevOS: kavram olarak al, motor olarak alma** (Java BPM motoru bulut oturumu modeline uymaz; çıkarım). Batu onayı ya da dış koşul bekleyen iş "koşullar sağlandı ama başlatılmadı" diye ayrı durur. Plan değişince yürüyen işe ne olacağı açık bir eşleme notuyla yazılır.

### 1.10 Durum geçişi × rol yetkisi — OpenProject
- **Nasıl (kaynak diyor):** "A workflow defines allowed status transitions for a **work-package type and project role**"; yazar ve atanan için ek geçişler vardır; closed→open geçişi `reopened?` olarak algılanır. Sonuç: "`current standing + allowed transition + actor authority/context`."
- **DevOS: uyarlayarak al.** Kim hangi geçişi yapar tablosu: örneğin yalnız doğrulayıcı `dogrulandi`, yalnız entegratör `entegre`, yalnız Batu `kabul` yazar. Tablo bir betik ya da hook ile denetlenmezse yalnız tavsiyedir (bkz. 2.10).

### 1.11 Önkoşul keşfi kaydı — RPD
- **Sorun (kaynak diyor):** Kullanıcı "yalnız sonuç istemek yerine eksik mühendislik koşullarını sürekli teşhis etmek zorunda" kalıyor (ASSESSMENT §2).
- **Nasıl (kaynak diyor):** Beş nesne ayrılır: ihtiyaç, koşul, yöntem, karar, eylem; AND ve OR birlikte bulunabilir. "Bir ürün kararının gerekli olduğunu keşfetmek kullanıcı adına cevabını uydurmak değildir." "bağlam veya bütçe bitmesi hazır olma/tamamlanma değildir." Bitmemiş keşif kaydı: "odak ihtiyaç, üst bağlantı, alternatifler, varsayımlar, beklenen alt sonuç, okunmuş kaynaklar, sıradaki işlem, geri dönüş noktası ve durma nedeni. Gizli düşünce zinciri istenmez." "Yöntemin kendi altyapısı da önkoşul sorgulamasına tabidir; bütün bir meta-sistem kurmak varsayılan değildir." Study'nin DevOS önerisi: "Bu alanların mevcut WORK/EVIDENCE ve gerektiğinde tek discovery kaydında tutulması bir ilk uygulama adayıdır. Yapı önerisinin ikinci bir HEAD/objects/commits otoritesi otomatik kurulmaz."
- **Kanıt (kaynak diyor):** Sentetik prototipte "Ran 25 tests in 1.593s" ve `OK`; yukarı akış değişince kabul edilmiş sonuç `STALE` oluyor (`test_accepted_item_can_become_stale`, demo `"assurance_after_upstream_change": "STALE"`). Ama probe 1'de A `OPEN` iken A'ya bağlı B "ACCEPTED/CHECKED" kabul edildi: "kayıt kabulü gerçek önkoşulun karşılandığını veya kanıtın doğru olduğunu hesaplamıyor." LLM davranışı hiç sınanmadı.
- **DevOS: davranışı ve alanları al; süreklilik motorunu (özel HEAD, fencing deposu, daemon) alma.** "RPD sürekliliği otomatik RAG, veri tabanı, custom HEAD deposu veya daemon değildir." Study'nin gerekli davranış testlerinden biri: "basit işte gereksiz altyapı yaratmama".

## 2. Orkestrasyon mekanizmaları

Aksi yazılmadıkça kanıt yine yalnız kaynak okumasıdır; Gas Town'ın "çalışıyor" ifadeleri birinci taraf iddiasıdır.

### 2.1 İş katmanı ≠ orkestrasyon katmanı — Gas Town
- **Nasıl (kaynak diyor, `gastown/FINDINGS.md` §1, §19):** İş Beads'te durur; Gas Town dağıtım, kapasite, izleme, devir ve entegrasyon ekler. Altı ayrım: "work substrate ≠ orchestration substrate; actor identity ≠ runtime session; logical readiness ≠ dispatch admissibility under capacity; work state ≠ scheduling/execution-attempt state; worker completion ≠ aggregate completion ≠ integrated/verified standing; event-driven transition ≠ reconciled derived state".
- Ortam (upstream glossary): "managing multiple Claude Code instances simultaneously using the `gt` and `bd` (Beads) binaries, coordinated with tmux in git-managed directories." Yani yerel makine, tmux ve daemon varsayar.
- **DevOS: ayrımı al, aracı alma.** Bulutta tmux yok, daemon oturum boşta kalınca ölür, Mac'e bağlanamayız (çıkarım).

### 2.2 Hook + GUPP: aktöre verilmiş iş kuyruğu
- **Nasıl (kaynak diyor, upstream glossary):** Hook "A special pinned Bead for each agent. The Hook is an agent's primary work queue". GUPP: "If there is work on your Hook, YOU MUST RUN IT." Polecat akışı (upstream molecules): "1. Spawn with work on hook / 2. gt prime # Shows formula checklist inline / 3. Work through each step / 4. Persist findings: bd update <issue> --notes "..." / 5. gt done # Submit, preserve handoff metadata, exit".
- **Kanıt:** "GUPP and agent role instructions are procedural policies; they are not equivalent to deterministic execution guarantees" (META).
- **DevOS: uyarlayarak al.** Her oturum ya da alt ajan için tek bir "bana verilen iş" girdisi olur; oturum başında okunur, soru beklemeden yürütülür. Mekanik tetik olarak SessionStart hook'u düşünülebilir (çıkarım; O11 doğrulamalı).

### 2.3 Convoy: iş emri ve tamamlanma yakınsaması
- **Sorun (kaynak diyor, upstream convoy-lifecycle):** "Convoys are passive trackers. They group work but don't drive it." Eski tek gözlemcili düzende: "When Deacon is down, convoys don't close. Work completes but the loop never lands."
- **Nasıl (kaynak diyor):** Convoy izlenen işleri `tracks` bağıyla toplar; kendi durumunu tutmaz, izlenen işlerden türetir. Daemon'daki `ConvoyManager` iki döngü koşar: "Event poll (every 5s)" kapanma olaylarını yakalar ve sıradaki hazır işi besler; "Stranded scan (every 30s): ... to catch convoys missed by the event-driven path (e.g. after crash/restart). Feeds ready work or auto-closes empty convoys." `CheckConvoysForIssue` idempotenttir. Kapalı convoy'a iş eklenirse yeniden açılır. Zorla kapatma gerekçe taşır: `gt convoy close hq-cv-xyz --reason="work done differently"`; ayrı durum: "ABANDONED (force-closed without completion)". Takılı işin ayrı ayrı görülmesi gereken halleri (FINDINGS §13): meşru bağımlılıkla bloklu, bilerek bekliyor, canlı işçide, hazır ama kimse almamış, işçi kaybolmuş, alttaki iş bitmiş ama kap açık.
- **Ders (kaynak diyor):** "Initial dispatch is parallel ... Even if `gt-task-2` has a `blocks` dep on `gt-task-1`, both get slung." Açık orkestrasyon grafı atlayabilir. Tavan yoktur: "`--max-concurrent` (default 0 = unlimited)". Yedek gözlemciler: "Refinery observers were removed (spec S-05) after S-17 found they were silently broken (wrong root path) with no visible impact".
- **DevOS: uyarlayarak al.** Batu'nun bir amacı için "iş emri" = izlenen işlerin listesi; durumu türetilir. Daemon yerine her oturum başında uzlaştırma: izlenen işler kapalı mı, hazır ama sahipsiz iş var mı, kirası dolmuş iş var mı, alt işler bitti ama emir açık mı. Tarama sonucunu (boş sonuç dahil) kayda yazar ki sessiz bozulma görünsün. Paralel dağıtım da hazır listeden geçer (çıkarım).

### 2.4 Zamanlayıcı: deneme kaydı, kapasite, devre kesici
- **Nasıl (kaynak diyor, FINDINGS §6–8):** `gt sling` iş maddesini değiştirmez; ayrı bir "sling context bead" açar (hedef, formül, argümanlar, birleştirme stratejisi, convoy, ajan, hata sayacı). Zamanlayıcı: "1. collects open sling contexts; 2. queries `bd ready` across rig databases; 3. keeps contexts whose work bead is ready; 4. computes available polecat capacity; 5. applies batch size; 6. dispatches selected work; 7. closes the context on success or updates failure state." Eşik (belgede 3) aşılınca bağlam `circuit-broken` olarak kapanır; iş maddesi dokunulmadan kalır.
- **DevOS: uyarlayarak al.** Deneme kaydı (hangi oturum, ne zaman, sonuç, hata) iş maddesinden ayrı tutulur. Aynı iş 3 kez başarısız olursa otomatik yeniden deneme durur ve koordinatör kaydına düşer; Batu'ya değil (çıkarım). Kapasite = eşzamanlı alt ajan/oturum sınırı; değeri O11 verir.

### 2.5 Satır içi adım mı, kalıcı kontrol noktası mı — Gas Town molekülleri
- **Nasıl (kaynak diyor, upstream molecules):** Root-only wisp'te adımlar veritabanı satırı olmaz, ajan onları satır içi okur: "This prevents wisp accumulation (~6,000+ rows/day → ~400/day)." Poured'da: "Steps ARE materialized as sub-wisps with checkpoint recovery. If a session dies, completed steps remain closed and work resumes from the last checkpoint." Kural: "If you would curse losing the progress after a crash, set `pour = true`. High frequency + cheap steps = inline (default). Low frequency + expensive steps = pour."
- **DevOS: al.** Kısa ve ucuz işler kontrol listesiyle satır içi; çok oturumlu, pahalı işler adım adım kaydedilen kontrol noktasıyla. Bekleme ve geri çekilme süresi de kalıcı olmalı (Gas Town HEAD'deki `await-event` backoff düzeltmesi, FINDINGS §10).

### 2.6 Kalıcı kimlik, geçici oturum, devir — Gas Town
- **Nasıl (kaynak diyor, upstream glossary):** Polecat: "persistent identity but ephemeral sessions ... Sessions and sandboxes are ephemeral — spawned for specific tasks, cleaned up on completion — but the identity persists. They work in isolated git worktrees". Handoff: "When context gets full or an agent needs a fresh start, handoff transfers work state to a new session." Seance: önceki oturumlara soru sorma. En iyi uygulama: "Persist findings early — `bd update <issue> --notes "..."` before session death".
- **DevOS: al.** Rol tanımı ve iş geçmişi dosyada kalır; oturum tek kullanımlıktır. Bulgular, bağlam sıkıştırılmadan ve makine geri alınmadan önce iş maddesine yazılır. Seance yerine kapanan oturumun devir notu ve git geçmişi (çıkarım).

### 2.7 Refinery: işçi "bitti" dedi ≠ ana dala girdi
- **Nasıl (kaynak diyor, FINDINGS §14–15):** Birleştirme kuyruğu, doğrulama kapıları, "Bors-style bisecting", başarısız birleştirme isteğinin yalıtılıp düzeltilmesi ya da yeniden dağıtılması. İşçi ana dala doğrudan yazmaz: "Actor autonomy can be high during execution while **integration authority** remains centralized/separate."
- **DevOS: al.** Alt ajan ya da yan oturum kendi dalında veya çalışma ağacında çalışır; ana dala alma ayrı bir entegratör adımıdır ve taze doğrulama ister. multi-agent-patterns §2'nin aktardığı eski SOUL DevOS rolleri (Builder, Researcher, Verifier, Adversarial Reviewer, Integrator, Human Owner) bununla uyumlu.

### 2.8 Topoloji: en az yeterli yapı, birleştirme sözleşmesi, eleştirmen ≠ doğrulama — multi-agent-patterns
- **Nasıl (kaynak diyor):** Görseldeki altı kutu aynı düzeyde seçenek değildir; sıra, eşzamanlılık, yetki, meydan okuma, insan yönetişimi ve yönlendirme ayrı boyutlardır, birlikte bulunur. "SOUL should not “choose a multi-agent pattern.” It should derive the minimum coordination/control topology required by the current work." Aday gereksinimler: C1 "Every additional agent, branch, hierarchy level, reviewer, or human gate should protect a material requirement"; C3 paralel daldan önce "shared base state; allowed mutations; isolation requirements; output contract; conflict semantics; merge authority; provenance requirements; whether integration itself needs verification"; C4 alt ajanın iş açabilmesi kapsamı, bütçeyi, kabul ölçütünü ya da izinleri genişletme yetkisi vermez; C7 topoloji değişimi kalıcı durumdur; C9 yönlendirme kararı yanlış olabilir, gerekçesi görünür olmalı; C10 çok ajansız çözüm geçerli bir sonuçtur.
- Yönlendirici (CONVERSATION-SYNTHESIS §6): basit iş → doğrudan yol; ayrıştırılabilir iş → paralel yol; büyük koordineli iş → hiyerarşik yol; yüksek riskli eylem → insan onayı. "Router: which path is appropriate? Manager: how should work be decomposed and coordinated inside that path?"
- Eleştirmen: "two agent roles do not automatically create independent verification"; ayrışma dereceleri: kendi kendini eleştirme → ayrı bağlam, aynı model → farklı model → "External/deterministic verifier where possible". DevOS'taki sıralama aslında ayrı kurallardır (§11.1): "“Verifier must occur after target freeze” is a Work dependency. “Verifier role cannot repair” is an Actor/authority rule. “Verification result bound to SHA” is an information/evidence rule."
- **Çelişki (kaynak diyor vs brief):** CONVERSATION-SYNTHESIS: "Claude Code: ... default subagent spawn depth of three levels beneath the main Claude execution, configurable through `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, and a default concurrent subagent limit of 20." Brief: bulutta derinlik 1. Study'nin kendisi bu gözlemlerin "should not be treated as durable architecture constraints" olduğunu söylüyor.
- **DevOS: al.** Hiyerarşi tek düzey: ana oturum koordinatör, alt ajanlar işçi ve doğrulayıcı. Paralel dal yalnız C3 sözleşmesiyle; ilk hedefler düşük bağlaşımlı işler: "independent source retrieval; independent negative-test generation; bounded module inspection; environment capability inventory; separate evidence-quality checks" (§16.3).

### 2.9 İnsan kapısı ve Batu'nun yeri — multi-agent-patterns, playbook
- **Nasıl (kaynak diyor):** "the human loop should be a governed authority boundary, not a compensation mechanism for missing system coordination." C6: "The system should not escalate to the user merely because an agent is uncertain if the uncertainty is researchable or technically resolvable." Ayrı tutulacak üç kayıt (§9): "`human approved this action`; `the technical claim was verified`; `the human independently reviewed the technical evidence`." Playbook: "agent may act up to the production gate, but cannot pass the gate itself."
- Sistemin Batu'nun elinden alması gereken işler (§16.2): "start a fresh verifier after builder completion; ensure exact target binding; carry verifier result into an integrator step; launch required repair/reverification; move between Claude Code/Codex or other execution environments; check whether all branches/results have returned."
- Playbook'un sınırı (`03` §4.6): paralel oturum modelinde "one engineer drives/steers/reviews multiple sessions". DevOS'ta kopyalanmamalı.
- i-have-adhd META (araştırılmamış aday kaydı): "explicit current-state / next-action presentation during multi-step execution" ve "failure cases where a stylistic instruction accidentally degrades epistemic caution or pushes work back to the user". Batu'ya sunulan görünüm için aday baskı.
- **DevOS: al.** Batu kapıları: niyet doğru anlaşıldı mı, değer/tercih kararı, geri dönüşsüz ya da yüksek etkili eylem, teslimat kabulü. Teknik doğrulama sistemin işidir. Batu'ya giden özet: durum + sonraki adım + açık karar (çıkarım).

### 2.10 Kontrol katmanları, geçişli yetki, yapılandırma testi, bakım döngüsü — playbook
- **Katmanlar (kaynak diyor, `01` §7.2–7.3, §10.4):** "always-relevant project context → CLAUDE.md / rules; conditionally relevant procedure → Skill; must-not-be-violated behavior → Hook / setting / sandbox / permission / identity / external gate". Resmi belgeye göre CLAUDE.md ve auto memory "context, not enforced configuration". "A control is only as strong as the alternate paths that bypass its observation/enforcement boundary."
- **Geçişli yetki (`00` §6):** Doğrudan üretim dağıtımı yetkisi olmayan olay-müdahale ajanı, model yükseltmesinden sonra Slack'te kod yazabilen başka bir Claude'dan düzeltmeyi push etmesini istedi; insan inceleme kapısı yakaladı. Ders: sert sınır "access to other agents"ı da kapsamalı.
- **Yapılandırma regresyonu (`01` §8.4):** Eval paketi CLAUDE.md, skill, hook, model ya da prompt değişince koşar; "Production incidents are added as permanent evaluation cases." Talimat birikimine karşı (`01` §7.2): tekrarlayan hata önce sınıflanır (bilgi eksiği mi, belirsiz talimat mı, test/hook olması gereken bir değişmez mi, yetenek sınırı mı, yanlış çerçeve mi, eski ortam durumu mu).
- **Bakım döngüsü (`01` §12):** "actual operating signal → deterministic trigger/threshold → bounded diagnostic actor → persistent evidence/intent → selection/approval gate → controlled work → verification → deployment → new operating signal".
- **DevOS: ilke olarak al;** hangi hook ve izinle uygulanacağı O11'de. DevOS'un kendi yapılandırması (rol tanımları, skill'ler, hook'lar) değişince küçük bir senaryo seti koşmalı (çıkarım). i-have-adhd META'daki değerlendirme düzeni (aynı vakalarda temel/aday karşılaştırması, kör yargılama, sürüm kapısı) aday yöntem; araştırılmadı.

## 3. Durum sözlüğü: WMPC'den DevOS iş kaydına

| Soru | Ayrı tutulacak durumlar (kaynak diyor: WMPC `10` §4) | DevOS alanı (çıkarım) |
|---|---|---|
| Başlanabilir mi? | "planning-ready ≠ logically actionable ≠ workflow-enabled ≠ implementation-ready ≠ session-admitted ≠ dispatch-admissible ≠ strategically on-track" | `hazir` (türetilir), oturuma alınan dilim, kapasite kontrolü |
| Kim? | "authority ≠ assignment ≠ claim ≠ liveness ≠ integration authority" | `sahip`, `kira_bitis`, geçiş yetki tablosu |
| Bitti mi? | "actor completion signal ≠ work-item closure ≠ aggregate completion ≠ implementation convergence ≠ integrated effect ≠ financial completion ≠ desired outcome" | `kategori: done`, `dogrulama`, `entegre`, `batu_kabul` |
| Geri gitme | "reopen ≠ reblock ≠ revise ≠ append remediation ≠ retry ≠ suspend/resume ≠ migrate ≠ compensate ≠ cancel/terminate ≠ redispatch" | olay türleri ayrı; tek bir "geri al" işlemi yok |
| Kalıcılık | "conversation context ≠ durable work state; durable work state ≠ execution state; current plan ≠ realized state" | iş dosyası ≠ deneme kaydı ≠ oturum bağlamı |

## 4. Dersler

| Ne oldu | Kök neden | Önlem | Kaynak |
|---|---|---|---|
| Beads rehberi parent-child'ın hazırlığı etkilemediğini söylüyor, kod etkiliyor | Türetilmiş belge koddan kaymış | Kural = betik + test; belge testle bağlanır | `beads/SOURCE-LEDGER.md` |
| Toplu `gt sling`, aralarında `blocks` olan işleri de aynı anda başlatır (belgelenmiş davranış) | Açık orkestrasyon yolu hazırlık kontrolünü atlıyor | Her dağıtım yolu aynı hazır listeden geçer | upstream convoy-lifecycle |
| Eski düzende tek gözlemci (Deacon) düşünce convoy'lar kapanmıyordu | Yoklamaya dayalı tek hata noktası | Olay + periyodik uzlaştırma; idempotent kontrol | upstream convoy-lifecycle |
| Yedek Refinery gözlemcileri yanlış kök yoluyla sessizce bozuktu, etkisi görülmedi | Gözlemcinin kendi sağlığı görünmüyordu | Uzlaştırma çıktısı (boş sonuç dahil) kayda yazılır | upstream convoy-lifecycle |
| Kısıtlı ajan başka bir ajan üzerinden yetkisi olmayan eyleme yöneldi | Yetki yalnız doğrudan araç listesiyle düşünülmüş | Yetki, erişilebilen ajan ve kanallar üzerinden değerlendirilir; insan kapısı | playbook `00` §6, `04` F8 |
| RPD kaydında önkoşulu açık iş "kabul" edildi; kira sahibi olmayan worker yazdı | Kayıt kabulü içeriği denetlemiyor; fencing yalnız işbirlikçi yolda | Kabulden önce önkoşulların kapalılığını betik denetler; gerçek sınır dal ve izin | RPD MECHANICAL-OBSERVATIONS |
| Plan uygulamadan sonra güncellenince onaylı plan kayboluyor | Ex-ante plan ile as-built aynı dosyada | Plan sürümleri + sapma kaydı | playbook `04` F4 |
| Dosya varlığı "tamam" sayılıyor; yanlış yazılmış şema alanı sessizce yok sayılıyor | Ucuz tamamlanma ölçütü; gevşek doğrulama | "Üretildi" ≠ "kabul"; şema doğrulaması katı | OpenSpec FINDINGS §3; upstream schema-yaml |
| "Converged" üreticinin kendi yargısı | Aynı model, aynı çerçeve | Yakınsama denetimini ayrı doğrulayıcı koşar | spec-kit META |
| Paralel oturum sayısını mühendisin inceleme kapasitesi sınırlıyor | İnsan orkestratör | Orkestrasyon sistemin; Batu yalnız kapılarda | playbook `01` §7.5, `04` F10 |
| Repo doğru, üretim ortamı farklı (veritabanı göçü örneği) | Temsil ≠ gerçek ortam | Yüksek etkili eylemden hemen önce canlı önkoşul kontrolü | playbook `04` F11 (Atlas; satıcı kaynağı) |
| Ürün sınırı iddiaları eskiyor (alt ajan derinliği 3 vs 1) | Tarihe bağlı ürün gözlemi mimariye yazılıyor | Ürün sınırları O11'de güncel kaynaktan; tasarım derinliğe dayanmaz | multi-agent-patterns CONVERSATION-SYNTHESIS §3 |

## 5. Birleşik iş kaydı taslağı (çıkarım; karar değil)

Yukarıdaki mekanizmaların bulutta düz dosyayla nasıl bir araya gelebileceğine dair bir örnek. Her alanın kaynağı yanında yazılı. Yeni mekanizma değildir; birleştirme için girdidir. Ponytail'in aday karar merdiveni ("need elimination → existing-code reuse → native/platform reuse → dependency reuse → minimal new implementation"; araştırılmadı) ve RPD'nin "gereksiz altyapı yaratmama" testi burada da geçerli: önce git ve dosya, gerekirse küçük betik.

```yaml
# is/W-7f3a.md ön bilgisi — bir iş = bir dosya; çakışmasız kimlik (Beads: "Hash-based IDs (`bd-a1b2`) prevent merge collisions")
id: W-7f3a
tur: gorev              # gorev | kesif | karar | dogrulama   (Beads iş türleri; RPD keşif kaydı)
emir: E-3               # iş emri; emrin durumu izlenen işlerden türetilir (Gas Town convoy "tracks")
etiket: "kodlanıyor"    # serbest ad
kategori: wip           # active | wip | done | frozen      (Beads status categories)
engeller: [W-12c0]      # hazır listeden düşürür + kapatmayı engeller (Beads blocks; OpenProject)
kesfedildigi: W-55aa    # yalnız köken, sıra koymaz        (Beads discovered-from)
kaynak_ref: "NIYET-2/K3 (missing)"   # neden var           (Spec Kit source-ref + gap-type)
sahip: {oturum: "<id>", rol: uygulayici, kira_bitis: "<zaman>"}   # (Beads claim + lease)
kabul_olcutu: ["..."]
kanit: ["..."]
dogrulama: {sonuc: "NOT VERIFIED", hedef: "<commit>", dogrulayici: "<oturum>"}  # PASS/FAIL/NOT VERIFIED (playbook 03 §2.4'ün aktardığı SOUL VERIFICATION_POLICY)
entegre: null           # ana dal commit'i                  (Gas Town Refinery)
batu_kabul: null        # yalnız Batu yazar                 (multi-agent-patterns §9)
# hazir / bloklu: yazılmaz, betik türetir (Beads is_blocked projeksiyonu)
# denemeler: ayrı dosya (Gas Town sling context; 3 hatada dur)
```

Yanındaki dosyalar: `niyet` (playbook intent alanları), `plan v1` + `sapma kaydı` (F4), Spec Kit biçiminde `tasks.md` ve append-only yakınsama fazları, keşif türündeki işlerde RPD keşif alanları.

## 6. Kapsam boşlukları ve açık sorular

- Hiçbir hedef çalıştırılmadı. Mekanizmaların "çalıştığı" yalnız kaynak metinlere ve birinci taraf iddialarına dayanıyor (ör. convoy yöneticisi için upstream: "fully implemented and tested (see spec.md stories S-01 through S-18, all DONE)").
- Minimal dosya kuyruğu (TASKS.md) WMPC'de "Deferred". Git içinde düz dosyayla tutulan iş kaydının eşzamanlı yazımda nasıl davrandığı hiçbir kaynakta yok; bulutta küçük bir deneme gerekir.
- Beads ve Gas Town'ın bulutta çalışabilirliği bilinmiyor: ikili kurulumu (setup script, ağ), Dolt'un `refs/dolt/data` push'u, tmux ve daemon yokluğu.
- Alt ajan derinliği ve eşzamanlılık sınırı, SessionStart/PreCompact hook'ları, zamanlanmış tetikler: O11. Gözledim: bu alt ajanın araç listesinde `create_session`, `create_trigger`, `send_later` tanımları var; davranışlarını doğrulamadım.
- Upstream dosyalar 2026-09-27'de study'lerin pinned ref'lerinden okundu; güncel main farklı olabilir.
- ERPNext FINDINGS/SOURCE-LEDGER ve public-apis RESEARCH okunmadı (gerekçe §0). RPD'nin özgün ekleri repoda yok.
