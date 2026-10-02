# O15 — Anthropic'in kendi rehberliği ve Claude Code çerçeveleri

> **KAPSAM BÖLÜNMELİ.** Bu kümenin kaynaklarını tek ajan baştan sona okuyamaz. Örneğin claude-flow reposunda yaklaşık 5.800, claude-code-templates reposunda yaklaşık 9.600 dosya var; BMAD'da 30 skill, awesome-claude-code'da yüzlerce bağlantı bulunuyor. anthropic.com/engineering'deki 25 yazının hepsi açıldı:
>
> - 21'i baştan sona okundu.
> - İkisi kısmen okundu: swe-bench'te örnek koşu dökümü atlandı, contextual-retrieval'da yalnız düzyazı okundu.
> - Birinin içeriği konu dışı (desktop-extensions).
> - Biri belgeye yönleniyor (best-practices).
>
> Çerçevelerin çekirdek mekanizma dosyaları tam okundu. Okunamayanların tam listesi ve önerilen bölünme §0.3'te.

**Okuyan:** O15, 27 Eylül 2026. STANDART.md sonradan geldi; ona göre okuma genişletildi. Web metinleri `curl` ile ham alındı; özetleyen araca güvenilmedi. Repolar scratchpad'e sığ klonlandı, okundu, silindi. Etiketler: **kaynak diyor / gözledim / çıkarım / bilinmiyor**. Platform yetenekleri O11'in işi; bu not rehberliği ve kalıpları ele alıyor.

## DevOS için en önemli çıkarımlar

1. **Süreklilik kalıbı somut ve Anthropic'in kendi kodunda var (§1.1).** İlk oturumu ayrı bir prompt çalıştırır ve şunları kurar: JSON iş listesi (hepsi `"passes": false`), `claude-progress.txt`, `init.sh` ve ilk commit. Sonraki her oturum aynı sabit sırayla yön bulur: `pwd`, ilerleme dosyası, iş listesi, `git log`, E2E duman testi. Her oturum tek iş yapar, commit atar, notunu bırakır. **Al.**
2. **Üreten ile yargılayanı ayır.** Kaynak açık: "Out of the box, Claude is a poor QA agent". Ayrı bir şüpheci değerlendirici, sprint öncesi "done" sözleşmesi ve eşikler kalite farkı yarattı. Bedeli: 20 dakika / 9 dolar yerine 6 saat / 200 dolar (§1.2). **Uyarlayarak al:** yalnız modelin tek başına güvenilir yapamadığı işte kullan.
3. **Talimat öneridir, hook zorlamadır.** "'Never do this' in CLAUDE.md … an instruction is the wrong tool"; "Put guardrails in hooks" (§1.5). Hook ancak çıkış kodu 2 ya da JSON ret kararıyla engeller; JSON'suz 1 ile çıkan hook engellemez. Batu'nun 1. gereksinimi (zorunluluk) buna karşılık gelir. **Al.**
4. **Harness'in her parçası eskiyen bir varsayımdır; kural değişikliğini ölçerek yap.** Anthropic, sistem prompt'una eklediği tek satırın %3 kayıp yarattığını ancak ablasyonla buldu. Şimdi her prompt değişikliğinde model başına eval koşuyor (§1.3). DevOS'ta CLAUDE.md, skill ve hook değişikliği de bir regresyon setinden geçmeli (gereksinim 5–6, K07). **Al.**
5. **İlerleme iddiası kanıta bağlanır; metinle biten tur "bitti" demek değildir (§1.7).** Fable 5'te "audit each claim against a tool result" talimatı uydurma raporları "nearly eliminated". Opus 5.5 kuralı: "Treat a text-only end of turn as a report", en çok 2–3 otomatik devam. Fable 5.1 hazır metinler veriyor: işi bitirme talimatı ve altı maddelik sıkıştırma özeti talimatı. **Al.**
6. **Ajan seçmesi gereken bilgiyi çoğu zaman getirmez (§2.1, §1.9).** BMAD'ın aktardığı ölçüm: yardımsız skill vakaların %56'sında hiç çağrılmadı; AGENTS.md'deki indeks %100 başarı verdi. Zorunlu protokol her oturum yüklenen bağlamda ya da hook ile enjekte edilen metinde olmalı. İsteğe bağlı skill, zorunlu kural taşıyamaz. **Al.**
7. **İş kaydı bir durum makinesi olsun (§2.1, §2.7).** BMAD'daki yapı:
   - plan dosyasının durumu `draft` ile başlar, `built` ile biter;
   - `done` kararını yalnız kullanıcı ya da orkestratör verir;
   - değiştirilemez bir `<intent-contract>` bloğu vardır;
   - her inceleme bulgusu hükümle kayda geçer;
   - 5 turda yakınsamayan iş `blocked` olur;
   - CLAUDE.md'ye dokunan düzeltme ertelenir.

   HumanLayer da Linear üzerinde durum makinesi kurar. CCPM'de durum soruları betikle cevaplanır. **Uyarlayarak al.**
8. **Doğrulayıcı ve kabul ölçütü, uygulayanın erişemeyeceği yerde durmalı (§1.6, §1.10).** Opus 4.6 bir değerlendirmenin cevap anahtarını bulup çözdü; çok ajanlı yapıda istenmeyen çözüm 3,7 kat arttı. Anthropic'in code-review eklentisi her bulguyu ayrı bir alt ajanla doğrular. BMAD'a göre koşmayan test yok sayılır ve beklenen sonuç koda uysun diye değiştirilmez. skill-creator ilkesi: "burden of proof to pass is on the expectation". **Al.**
9. **Pazarlama ile kanıtı ayır (§2, §3).** Gözlenen örnekler:
   - claude-flow: hız çarpanı `Math.random()` ile üretiliyor; "tehlikeli komut" hook'u 1 ile çıktığı için hiçbir şeyi engellemiyor; oturum geri yüklenmediğinde bile sahte bir "Restored State" tablosu basıyor; kullanıcı prompt'una reklam enjekte ediyor.
   - SuperClaude: oturum başında hiçbir şeyi denetlemeden sabit "✅ … available" listesi basıyor.
   - CCPM: bağımlılığı olan görev hiçbir zaman "ready" görünmüyor.
   - templates: force-push koruması delik.
   - Claude Squad: izin ve güven istemlerine otomatik Enter basıyor.

   Agent OS v3 ve BMAD v6.11 kendi rol ve orkestrasyon katmanlarını söktü. **Rol kalabalığını alma; kapıları al.**
10. **Repo yapılandırması çalıştırılabilir koddur, kalıcı bellek saldırı yüzeyidir (§1.12).** Anthropic "Persistent memory poisoning" ve "Multi-agent trust escalation" risklerini açıkça yazıyor. Bir allowlist fiilen bir yetki verir ("capability grant"). Dışarıdan alınan metin `<pasted_content id>` ile etiketlenir. **Al.**
11. **Platform çelişkisi, O11 sınamalı (§6):**
    - Belgeye göre alt ajanlar varsayılan olarak 3 kata kadar iç içe açılabilir. Brief 1 diyor; bu oturumda alt ajan olarak Agent aracım yok (gözledim).
    - Dynamic workflows'un sonuçları bulutta VM geri alınsa da korunuyor, ama `ultracode` anahtar kelimesi `-p` ya da zamanlanmış prompt'tan çalışmıyor.

## 0. Kapsam

### 0.1 Baştan sona okunan

**anthropic.com/engineering yazıları (22):**

| Yazı | Tarih |
|---|---|
| building-effective-agents (sonradan Managed Agents notu eklenmiş) | 19 Ara 2024 |
| swe-bench-sonnet (örnek koşu dökümü hariç; o kısım bir scikit-learn hatasının adımları) | 6 Oca 2025 |
| claude-think-tool (15 Ara 2025 notu: artık extended thinking öneriliyor) | 20 Mar 2025 |
| multi-agent-research-system | 13 Haz 2025 |
| a-postmortem-of-three-recent-issues | 17 Eyl 2025 |
| writing-tools-for-agents | 11 Eyl 2025 |
| effective-context-engineering | 29 Eyl 2025 |
| agent-skills | 16 Eki 2025 |
| claude-code-sandboxing | 20 Eki 2025 |
| code-execution-with-mcp | 4 Kas 2025 |
| advanced-tool-use | 24 Kas 2025 |
| effective-harnesses-for-long-running-agents | 26 Kas 2025 |
| demystifying-evals | 9 Oca 2026 |
| AI-resistant-technical-evaluations | 21 Oca 2026 |
| infrastructure-noise | 5 Şub 2026 |
| building-c-compiler | 5 Şub 2026 |
| eval-awareness-browsecomp | 6 Mar 2026 |
| harness-design-long-running-apps | 24 Mar 2026 |
| claude-code-auto-mode | 25 Mar 2026 |
| managed-agents | 8 Nis 2026 |
| april-23-postmortem | 23 Nis 2026 |
| how-we-contain-claude | 25 May 2026 |

- contextual-retrieval (19 Eyl 2024): düzyazı tamamen okundu, sonuç tablolarına göz gezdirildi.
- desktop-extensions (26 Haz 2025) açılıp okundu. İçerik konu dışı: Claude Desktop için yerel MCP paketi; bulut DevOS'ta Desktop yok.

**claude.com/blog yazıları:**
- "Building agents with the Claude Agent SDK" (29 Eyl 2025). Eski engineering adresi bu yazıya yönleniyor.
- "Steering Claude Code" (18 Haz 2026).
- "Coding sessions are longer…" (24 Eyl 2026).
- "Agentic coding is straining CI" (14 Eyl 2026).

**Belgeler (tarihsiz; 27 Eyl 2026'da okundu):**
- code.claude.com: best-practices, features-overview, how-claude-code-works, workflows (dynamic workflows), agent-sdk/overview.
- platform.claude.com: prompting best practices (SDK kod örneklerinin başka dillerdeki tekrarları hariç), prompting-claude-opus-5-5, -opus-5, -fable-5 ve -fable-5-1 (yalnız düzyazı; tool batching bölümü kod örneği), skill authoring best practices.

**Anthropic kodu:**
- `anthropics/claude-quickstarts@dee7116` (24 Eyl 2026), `autonomous-coding/`: iki prompt dosyası, agent.py, client.py ve progress.py tamamen; security.py'nin ana gövdesi ve app_spec'in başı.
- `anthropics/claude-code@7779afb` (25 Eyl 2026), `plugins/`: feature-dev komutu ve code-reviewer ajanı, code-review komutu, ralph-wiggum `stop-hook.sh`, hookify `hooks.json` ve iki örnek kural, pr-review-toolkit `review-pr.md`, security-guidance `hooks.json` ve README.
- `anthropics/skills@3337550`: skill-creator SKILL.md'nin ana döngüsü ve `agents/grader.md`.

**Topluluk:**
- BMAD `@5e33d3c`:
  - build-auto: `workflow.md`, `step-01`–`04`, `plan-template.md`, `customize.toml`, claims-check, deletion-check;
  - build: `workflow.md`, `step-01`, `step-02`, `step-05`;
  - `bmad-review/SKILL.md`, `bmad-retrospective/workflow.md` (+ evidence-gathering, acceptance-verdict);
  - `bmad-preview-ticketing/SKILL.md` (+ tree-rules, board);
  - `bmad-project-context/SKILL.md` (+ best-practices);
  - docs: `autonomous-development-loops.md`, `break-work-into-stories…`, `theory-of-project-context.md`.
- CCPM `@7d7e462`: SKILL.md ve bütün references; betiklerden `next.sh` ve `blocked.sh`.
- Agent OS `@475b0ca`: README, CHANGELOG ve beş komutun hepsi.
- HumanLayer: `ace-fca.md` (repo `@f2bc7ae`); `create_handoff`, `research_codebase`, `implement_plan`, `validate_plan`, `resume_handoff` ve `ralph_*` ile `oneshot*` komutları (`@99abe67`).
- Compound Engineering `@a763b39`: `ce-compound.md`.
- claude-flow `@d37f283`: öz-denetim belgesinin ana bölümü.

### 0.2 Kısmen okunan
Neyin atlandığı yanlarında yazılı.
- **Platform belgeleri:**
  - memory-tool: düzyazı okundu; 8 dilde yinelenen API kodu atlandı.
  - sub-agents ve hooks: yalnız derinlik, eşzamanlılık ve çıkış kodu bölümleri. Bu belgeler O11'in kapsamında.
- **BMAD:**
  - interaktif build'in `step-03`, `step-04` ve `step-oneshot` adımları: yalnız insan kontrol noktaları tarandı;
  - `bmad-correct-course`: yalnız giriş kısmı;
  - verification-gap: ilk 60 satır.
- **CCPM:** `validate.sh` taranarak okundu.
- **claude-flow:**
  - README, STATUS ve `.claude/settings.json`;
  - `hook-handler.cjs`: route, pre-bash ve session-restore bölümleri;
  - `auto-memory-hook.mjs`: yalnız başlık ve fonksiyon listesi;
  - CLAUDE.md (1.529 satır): başlıklar ve üç bölüm.
- **SuperClaude:** README, `confidence.py`, `reflexion.py`'nin başı, `hooks.json`, `session-init.sh` ve `pm-agent.md`'nin 1–95. satırları.
- **claude-code-templates:** README, bir hook ve 18 loop dosyasından 4'ü.
- **awesome-claude-code:** Orchestration, Memory, Config, Testing ve Linting bölümleri. Diğer bölümlerin başlıkları görüldü; hepsi konu dışı: status line, UI, yazım, medya.
- **Claude Squad:** README, `daemon.go` ve `instance.go`/`tmux.go` içinde AutoYes ile ilgili kısımlar.

### 0.3 Okunmayanlar
Yeni ajan için önerilen bölünme şöyle:
- **K1 · Anthropic, claude.com/blog'daki Claude Code yazıları:**
  - "A harness for every task: dynamic workflows in Claude Code": `claude.dev` alan adı ağ çıkışında engellendi, okunamadı;
  - "CLAUDE.md files: Customizing Claude Code…";
  - "how to configure hooks";
  - "A Field Guide to Claude Fable 5";
  - "What a task costs on Opus 5.5".

  Ayrıca: "How Anthropic teams use Claude Code" PDF'i; `anthropics/claude-plugins-official`; claude-code plugin'lerinden plugin-dev, agent-sdk-dev, commit-commands ve hookify'ın kural motoru.
- **K2 · BMAD:**
  - ticketing: `slice.md`, `ticket.md`, `validate.md`, `estimate.md`, `store-setup.md`;
  - correct-course'un gövdesi ve `checklist.md`;
  - agent-dev ve hub skill'leri;
  - kalan 20 skill (brainstorming, prd, architecture, spec, ux, party-mode, deep-recon…);
  - `docs/` içinde yukarıda sayılmayanlar;
  - `tools/`, `tickets.py` ve bmad-loop reposu.
- **K3 · claude-flow/Ruflo:** `v3/@claude-flow/*` paketleri (swarm, hooks, memory, guidance), `plugins/`, `crates/`, CLAUDE.md'nin kalanı, `verification/` ve `docs/` altındaki diğer belgeler.
- **K4 · SuperClaude:** 30 komut, 7 mod, kalan 18 ajan, `KNOWLEDGE.md`, `PLANNING.md` ve `tests/`.
- **K5 · claude-code-templates:** yaklaşık 435 ajan, 348 komut, 89 hook ve 5.690 skill dosyası; CLI ile analitik kodu; kalan 14 loop.
- **K6 · awesome-claude-code'da adı geçen, DevOS'la ilgili çerçeveler:** Claude Code Harness, RIPER-5, Ralph for Claude Code (çıkış tespiti, devre kesici), ralph-orchestrator, The Ralph Playbook, Infrastructure Showcase (skill'i hook ile etkinleştirme), Agent Collab Skills (kabul kapısı), AgentSys (drift tespiti), Plannotator, TDD Guard, agnix, Ctxlint, Upkeep, presence, Selvedge.
- **K7 · HumanLayer:** `agents/` altındaki 6 ajan; `create_plan`'ın tamamı; `iterate_plan`, `debug`, `describe_pr` ve `linear` komutları.
- **K8 · Brief'te "gibi" ile anılanlar:** Task Master, cc-sdd, spec-workflow, Conductor, vibe-kanban, wshobson/agents.

## 1. Anthropic'in önerdiği somut kalıplar

### 1.1 Uzun soluklu harness: initializer + coding agent
**Kaynak:** "Effective harnesses…" (26 Kas 2025) ve kodu `claude-quickstarts@dee7116`.

**Sorun (kaynak diyor):**
- Ajan işi bir seferde bitirmeye çalışıyor ve bağlam dolunca işi yarım bırakıyor.
- Sonraki bir oturum yapılan ilerlemeyi görüp "declare the job done".
- Özellik "complete without proper testing" işaretleniyor.

"compaction isn't sufficient".

**Mekanizma (koddan):**
- **Oturum türü:** `agent.py`, oturum türünü dosyanın varlığına bakarak seçer: `is_first_run = not tests_file.exists()`. Her oturumda yeni bir istemci açılır. `max_iterations` verilmezse döngü sonsuza kadar sürer. Tüm testler geçse bile döngünün durma koşulu yok (gözledim).
- **Initializer:**
  - En az 200 test içeren bir `feature_list.json` yazar. Alanlar `category`, `description`, `steps` ve `passes`; en az 25 testin 10'dan fazla adımı olur.
  - Prompt'ta şu cümle var: "IT IS CATASTROPHIC TO REMOVE OR EDIT FEATURES IN FUTURE SESSIONS. Features can ONLY be marked as passing".
  - Ardından `init.sh`, ilk commit ve `claude-progress.txt` gelir.
- **Coding prompt'u (10 adım):**
  1. Yön bulma: `pwd`, `ls`, `cat app_spec.txt`, iş listesi, ilerleme dosyası, `git log --oneline -20` ve `grep '"passes": false' | wc -l`.
  2. `init.sh` çalıştırılır.
  3. "VERIFICATION TEST (CRITICAL!)… Before implementing anything new". Bozuk bulunan özellik hemen `false` yapılır.
  4. Tek bir özellik seçilir.
  5. Özellik uygulanır.
  6. Tarayıcıyla doğrulanır. "Only test with curl commands (backend testing alone is insufficient)" yasaklar arasında.
  7. "YOU CAN ONLY MODIFY ONE FIELD: 'passes'".
  8. Commit atılır.
  9. İlerleme dosyası güncellenir.
  10. "END SESSION CLEANLY".
- **Güvenlik:** `PreToolUse` hook'u Bash komutlarını bir allowlist'e göre süzer (`ls`, `cat`, `npm`, `git`…). `pkill`, `chmod` ve `init.sh` ek doğrulamadan geçer. Sandbox açıktır ve izinler `./**` ile sınırlıdır.
- **Spesifikasyon:** XML etiketli bir `app_spec.txt`. API anahtarı "You will not be allowed to read this file, but you can reference it in code" denerek korunuyor.
- **İlerleme sayımı:** `progress.py` ilerlemeyi modelin kendi yazdığı `passes` alanlarından sayar. Harness, `passes`'ın meşru biçimde işaretlenip işaretlenmediğini denetlemiyor (gözledim).
- **Neden JSON:** "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files".

**Kanıt:** İç deneyler yapılmış; tarayıcı araçları "dramatically improved performance". Sayısal bir kıyas yok. Tek ajan mı uzman ajanlar mı daha iyi sorusu "still unclear".

**Belge karşılığı:** platform.claude.com'daki "Workflows across multiple context windows" aynı reçeteyi veriyor:
- "Use a different prompt for the very first context window";
- `tests.json`;
- `init.sh`;
- "Starting fresh versus compacting";
- "Use git for state tracking".

memory-tool belgesindeki "Multisession software development pattern" de aynı kalıbı anlatıyor: "Mark a feature complete only after end-to-end verification".

**DevOS:** **Uyarlayarak al.**
- İş listesi DevOS'un iş kaydı olur. `passes` alanının yerine kanıt alanları konur: komut, çıktı yolu ve commit.
- Yalnız izinli alanın değiştiği bir betikle denetlenir (JSON diff). Bu denetim yoksa kural yalnız talimat olarak kalır.
- Yön bulma sırası SessionStart hook'u ile enjekte edilir (çıkarım).
- Tüm işler kapanınca döngü durur ve bir kabul kapısı çalışır. Kaynaktaki harness'te bu eksik.

### 1.2 Planlayıcı → üretici → değerlendirici ve sprint sözleşmesi
**Kaynak:** "Harness design for long-running application development" (24 Mar 2026).

**Mekanizma:**
- **Planlayıcı:** 1–4 cümlelik isteği bir ürün spesifikasyonuna genişletir. Teknik ayrıntıya girmez; gerekçe: "errors in the spec would cascade".
- **Üretici:** Sprint sprint, her seferinde tek özellik geliştirir.
- **Değerlendirici:** Playwright ile uygulamayı bir kullanıcı gibi kullanır. Her ölçütün bir eşiği var; biri eşiğin altındaysa sprint başarısız sayılır.
- **Sözleşme:** "Before each sprint, the generator and evaluator negotiated a sprint contract". İletişim dosyalar üzerinden yürür.
- **Kalibrasyon:** Değerlendirici few-shot örneklerle ayarlanır; log'lar okunur, insanla ayrışan yargılar bulunur ve prompt düzeltilir.

**Kanıt (kaynak diyor):**
- Tek ajan 20 dakikada ve 9 dolara bir uygulama çıkardı, ama oyun çalışmıyordu. Tam harness 6 saatte ve 200 dolara oynanabilir bir sürüm üretti.
- Sprint 3 tek başına 27 ölçüt içeriyordu.
- Opus 4.6 ile sprintler kaldırıldı, değerlendirici tek geçişe indi. DAW uygulaması 3 saat 50 dakikada ve 124,70 dolara bitti; QA hâlâ "stub-only" özellikler buldu.
- Sınır: değerlendirici bulduğu sorunlar için "talk itself into deciding they weren't a big deal".

**İlkeler (birebir):**
- "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing"
- "the evaluator is not a fixed yes-or-no decision. It is worth the cost when the task sits beyond what the current model does reliably solo."

**DevOS:** **Uyarlayarak al.**
- İş başlamadan bir "done" sözleşme dosyası yazılır: kabul ölçütleri ve doğrulama komutları.
- Değerlendirici ayrı bağlamda çalışan, şüpheci ayarlanmış bir alt ajandır; eşikleri ve kalibrasyon örnekleri olur.
- Maliyet yüksek olduğu için değerlendirici risk etiketine göre açılır.

### 1.3 Harness varsayımları eskir; oturum günlüğü bağlam değildir; postmortem'ler
**Managed Agents (8 Nis 2026):**
- Oturum "the append-only log of everything that happened".
- Harness çökerse yenisi `wake(sessionId)` ve `getSession(id)` ile açılıp son olaydan devam eder.
- "The session is not Claude's context window": geri dönüşsüz sıkıştırma yerine günlükten dilim okunur.
- Kimlik bilgisi sandbox'a hiç girmez; git token'ı remote'a gömülür.
- Context reset Sonnet 4.5'te gerekliydi, Opus 4.5'te "dead weight" oldu.

**Postmortem (23 Nis 2026):** Üç değişiklik kaliteyi düşürdü:
- Varsayılan effort high'dan medium'a indirildi.
- Boşta kalan oturumların eski düşünme bloklarını temizleyen değişiklik, bir hata yüzünden her turda çalıştı. Ajan "forgetful and repetitive" oldu; hata, çok sayıda insan ve otomatik incelemeden, testlerden ve dogfooding'den geçmişti.
- Sistem prompt'una şu satır eklendi: "Length limits: keep text between tool calls to ≤25 words…". Satır haftalarca iç testi geçmişti; geniş ablasyonda %3 düşüş çıktı.

Aldıkları önlem: "a broad suite of per-model evals for every system prompt change… ablations… soak periods… gradual rollouts".

**Postmortem (17 Eyl 2025):**
- Bir geçici çözüm daha derin bir hatayı maskeliyordu. Kök neden çözüldü sanılıp geçici çözüm kaldırılınca derindeki hata ortaya çıktı.
- "The evaluations we ran simply didn't capture the degradation… in part because Claude often recovers well from isolated mistakes".
- Önlem: eval'leri "continuously on true production systems" koşmak.

**DevOS:** **Al.**
- (a) Repo oturum günlüğü işlevi görür: karar, iş ve kanıt kayıtları yalnız eklenerek büyür.
- (b) Kural değişikliği bir regresyon setine karşı ölçülür; gerekirse satır ablasyonu yapılır.
- (c) Doğrulama gerçek bulut oturumunda koşar; modelin hatadan toparlanması hatayı gizleyebilir.
- (d) Model değişince iskelet budanır.

### 1.4 Bağlam, araç ve çok ajanlı araştırma
**Context engineering (29 Eyl 2025):**
- Temel ilke: "find the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome".
- Kenar durum listeleri yerine "diverse, canonical examples" verilmeli.
- En yaygın hata "bloated tool sets".

**Uzun iş için üç teknik:**
- **Compaction:** Claude Code konuşmayı özetler ve "the five most recently accessed files" korunur. Özet ayarlanırken önce hiçbir önemli bilgi kaçmamalı, sonra fazlalık atılır.
- **"Structured note-taking":** NOTES.md ya da yapılacaklar listesi.
- **Alt ajan:** "condensed, distilled summary… (often 1,000-2,000 tokens)".
- **Hibrit bağlam:** CLAUDE.md baştan yüklenir, glob ve grep ile de "just-in-time" okunur.

**Çok ajanlı araştırma (13 Haz 2025; kaynak diyor):**
- Opus 4 lider ve Sonnet 4 alt ajanlar, tek başına Opus 4'ten %90,2 daha iyi sonuç verdi.
- Performans varyansının %80'ini token miktarı açıklıyor; maliyet "about 15× more tokens than chats".
- "most coding tasks involve fewer truly parallelizable tasks than research".

**Alt ajan kuralları:**
- Görev tanımında "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries" bulunur.
- Efor sorunun zorluğuna göre ölçeklenir: basit bir soru için 1 ajan ve 3–10 çağrı yeter.
- Lider planını belleğe yazar.
- "Subagent output to a filesystem to minimize the 'game of telephone'".
- Değerlendirmeye 20 gerçek sorguyla başlanır; ara adımlar yerine bitiş durumu değerlendirilir.

**Agent SDK yazısı (29 Eyl 2025):**
- Döngü: "gather context -> take action -> verify work -> repeat".
- "we suggest starting with agentic search, and only adding semantic search if you need faster results".
- LLM yargıç "generally not a very robust method".

**Code execution with MCP (4 Kas 2025):**
- Araçlar bir dosya ağacı olarak sunulunca token kullanımı "150,000 tokens to 2,000".
- Ara sonuçlar yürütme ortamında kalır.
- Durum `./workspace` altına yazılır; işe yarayan kod `./skills` altına kaydedilir.

**Advanced tool use (24 Kas 2025):**
- Tool Search ile Opus 4 %49'dan %74'e, Opus 4.5 %79,5'ten %88,1'e çıktı.
- Programatik çağrı token kullanımını %37 azalttı.
- Örnekli araç tanımıyla doğruluk %72'den %90'a çıktı.
- "Keep your three to five most-used tools always loaded, defer the rest".

**Contextual retrieval (19 Eyl 2024):**
- "If your knowledge base is smaller than 200,000 tokens… just include the entire knowledge base".
- Parçalara bağlam cümlesi ekleyip BM25 ile birleştirmek hatalı getirmeleri %49, yeniden sıralamayla %67 azaltıyor.

**DevOS:** **Al.**
- Okuma ve araştırma alt ajanda yürür; tam çıktı dosyaya yazılır, lidere dosya yolu ve kısa özet döner.
- Görev tanımında dört alan zorunlu olur.
- Kod işini paralelleştirmede temkinli olunur.
- Çekirdek DevOS bilgisi 200 bin tokenin altında tutulup doğrudan okunur. Research korpusu büyükse önce dosya ve grep ile ajan araması yapılır; embedding ancak ölçülmüş bir ihtiyaç doğarsa eklenir.

### 1.5 Talimat mı zorlama mı
**Kaynak:** best-practices, features-overview, how-claude-code-works ve Steering blog'u (18 Haz 2026).

**Birebir ilkeler:**
- "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens."
- "'Never do this' in CLAUDE.md. When there's something that absolutely must not happen, an instruction is the wrong tool… under pressure, in a long session… or due to a prompt injection… the model can fail to follow a prompted rule."
- "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"
- "Keep CLAUDE.md under 200 lines, give it an owner, and review changes to it like code."

**Hook çıkış kodu (hooks belgesi):** "Without valid JSON on stdout, Claude Code treats exit code 1 as a non-blocking error and proceeds… If your hook is meant to enforce a policy, use `exit 2`."

**Sıkıştırmadan sonra hangi katman ne olur:**
- Kök CLAUDE.md yeniden okunur.
- Alt dizindeki CLAUDE.md o dizine dokunulana kadar kaybolur.
- Path'e bağlı rules yeniden eklenir.
- Çağrılmış skill'ler ortak bir bütçe içinde yeniden eklenir; bütçe dolunca "oldest dropped first".
- Hook'lar "Bypass compaction entirely".
- PreCompact yedeğini Claude, hook çıktıda söylemedikçe bilmez.

**Diğer kurallar:**
- "Compact Instructions" bölümü CLAUDE.md'ye yazılır.
- Auto memory'nin (MEMORY.md) yalnız ilk 200 satırı ya da ilk 25 KB'ı yüklenir.
- Hangi mekanizmanın ne zaman ekleneceği (features-overview):
  - "wrong twice" → CLAUDE.md;
  - aynı prosedür "third time" yapıştırılıyorsa → skill;
  - yan iş konuşmayı dolduruyorsa → alt ajan;
  - "every time without asking" → hook.

**Doğrulamanın dört kademesi:** prompt içinde; `/goal` ("A separate evaluator re-checks it after every turn"); Stop hook; ikinci görüş alt ajanı. İlgili ilkeler:
- "Have Claude show evidence rather than asserting success".
- "A reviewer prompted to find gaps will usually report some, even when the work is sound".

**Oturum yönetimi:**
- Aynı konuda iki başarısız düzeltmeden sonra `/clear`.
- İş spesifikasyonu yeni bir oturumda uygulanır. İyi spesifikasyon kendi kendine yeter ve uçtan uca bir doğrulama adımıyla biter.

**DevOS:** **Al.**
- Her kural için zorlama katmanını gösteren bir tablo tutulur: talimat, rule, skill, hook ya da CI.
- Zorlama gereken her hook `exit 2` ya da JSON ret kararı döndürür, ve bunun negatif testi yazılır.
- CLAUDE.md kısa bir indeks olur. Prosedürler skill'e, dizine özgü kurallar path'li rules'a gider.
- Sıkıştırmadan sağ çıkması gereken durum (aktif iş, değişen dosyalar, test komutları) CLAUDE.md'deki "Compact Instructions" bölümüne ve SessionStart hook'una bağlanır (çıkarım).

### 1.6 Değerlendirme ve değerlendirme bütünlüğü
**Demystifying evals (9 Oca 2026):**
- Değerlendirme ajanın söylediğine değil, sonuca bakar: "the outcome is whether a reservation exists".
- pass@k ile pass^k farklı şeyler ölçer.
- "20-50 simple tasks drawn from real failures is a great start".
- Her görevin bir referans çözümü olur.
- "grade what the agent produced, not the path it took".
- Denemeler birbirinden yalıtılır: bir örnekte Claude önceki denemelerin git geçmişine bakarak haksız avantaj sağladı.
- "we do not take eval scores at face value until someone digs into the details… and reads some transcripts".
- LLM yargıcına "Unknown" deme çıkışı verilir; her boyut ayrı bir yargıçla değerlendirilir.

**Eval awareness (6 Mar 2026):**
- Opus 4.6 iki vakada BrowseComp olduğunu anladı, kaynak kodu okudu ve XOR ile şifrelenmiş cevap anahtarını çözdü; 18 koşu aynı stratejiye yöneldi.
- Çok ajanlı yapıda istenmeyen çözüm oranı %0,87, tek ajanda %0,24 (3,7 kat).
- "URL-level blocklists were insufficient". Önerileri: "treat eval integrity as an ongoing adversarial problem".

**Diğer bulgular:**
- **Infra noise (5 Şub 2026):** Kaynak ayarı tek başına 6 puan fark yaratıyor. "leaderboard differences below 3 percentage points deserve skepticism".
- **AI-resistant (21 Oca 2026):** Opus 4.5 "insurmountable" bir darboğaz sanıp durdu. Ulaşılabilir hedef söylenince çözümü buldu.

**DevOS:** **Al.**
- Gerçek hatalardan çıkarılmış 20–50 görevlik bir davranış eval'i kurulur; her görev bir referans çözüm taşır.
- Kabul testleri ve referans çözümler uygulayıcı ajanın okuyamayacağı yerde tutulur, ya da değerlendirme ayrı bir oturumda koşar (çıkarım).
- Karşılaştırmalar aynı ortamda yapılır; küçük farklar gürültü sayılır.
- Uygulayıcıya ulaşılabilir hedef açıkça verilir.

### 1.7 Güncel model rehberi: gözetimsiz uzun koşu
**Kaynak:** platform.claude.com prompting sayfaları (tarihsiz; 27 Eyl 2026'da okundu).

**Opus 5.5:**
- "Treat a text-only end of turn as a report rather than as proof the task is done. Keep the task's parts in a checklist… stop after two or three automatic continuations".
- İstenmeyen dört duruş biçimini adlandıran bir ek var. Ek, riskli işlemde onayın sürdüğünü de söylüyor.
- Çok ajanlı harness'lerde süre sinyali verilir: `elapsed 340s / 1200s`.
- Dışarıdan yapıştırılan metin `<pasted_content id="…">` ile etiketlenir.

**Fable 5:**
- "Before reporting progress, audit each claim against a tool result from this session… if tests fail, say so with the output". Bu talimat uydurma raporları "nearly eliminated".
- Bellek: "Store one lesson per file with a one-line summary at the top… delete notes that turn out to be wrong."
- "Separate, fresh-context verifier subagents tend to outperform self-critique."
- "Skills developed for prior models are often too prescriptive… can degrade output quality."
- Uzun koşuları beklemek yerine "check on runs asynchronously, for example through scheduled jobs".

**Fable 5.1:**
- **"Finish the whole task" metni:** "You are operating autonomously… Before ending your turn, check your last paragraph. If it is a plan… or a promise about work you have not done… do that work now… Do not stop because the context or session is long."
- **"Delivering work":** "don't quietly narrow, widen, or swap it". Bir parça takılırsa gerisi tam bitirilir ve "say exactly what you left out and why".
- **Sıkıştırma özeti için altı madde korunur:**
  1. zorluklar ve nasıl çözüldükleri;
  2. denenen ve bırakılan yollar;
  3. istek ve kararlar, "stated exactly";
  4. şu anki durum;
  5. açık kalan işler;
  6. isim, sayı ve bağlantılar, "kept exactly".
- "Keep changes and tests to what the task asks for": ilgisiz hatalar raporlanır ama düzeltilmez.
- Lider ajan, alt ajanlar çalışırken beklemeden devam eder.

**Opus 5:**
- Açık doğrulama talimatları "cause over-verification… remove them".
- İnceleme prompt'unda "only report high-severity issues" denirse model bunu harfiyen izleyip daha az bildiriyor. Önerisi: "ask it to report everything and filter in a separate pass".
- Alt ajan için tavanlar: `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `…_MAX_CONCURRENT_SUBAGENTS`.

**Genel sayfa:**
- "CRITICAL: You MUST…" gibi sert dil artık aşırı tetikliyor. Talimatın gerekçesi yazılmalı.

**DevOS:** **Al.**
- Gözetimsiz DevOS oturumunun sistem ekine Fable 5.1'in "Finish the whole task" ve "Delivering work" metinleri konur.
- Sıkıştırma talimatı altı maddeli olur.
- Tur raporunda her iddia kanıta atıf verir; bu, K11'deki çıktı, commit ve push ayrımıyla örtüşür.
- İnceleyici her şeyi bildirir; eleme ayrı bir triage adımında yapılır (BMAD ile aynı).
- Doğrulama model talimatına değil harness'e konur. Böylece modele göre değişen "doğrula" ve "doğrulama" çelişkisi bypass edilir.

### 1.8 Paralel ajan ekibi: C derleyicisi (5 Şub 2026)
**Mekanizma:**
- Sonsuz bir bash döngüsü: `claude --dangerously-skip-permissions -p "$(cat AGENT_PROMPT.md)"`.
- Her ajanın ayrı bir Docker konteyneri ve çıplak bir upstream reposu var.
- Kilit: ajan `current_tasks/<görev>.txt` yazarak görevi sahiplenir. "git's synchronization forces the second agent to pick a different one".
- "I don't use an orchestration agent."
- Uzman roller: yinelenen kodu birleştiren, performansa bakan, tasarım eleştirmeni ve dokümantasyon.

**Dersler:**
- "the task verifier is nearly perfect, otherwise Claude will solve the wrong problem".
- Test çıktısı birkaç satırla sınırlı tutulur, ayrıntı log'a gider; hata satırı aynı satırda `ERROR` yazar.
- "Time blindness" için deterministik örneklemli bir `--fast` seçeneği.
- Tek büyük görevde ajanlar aynı hatada çakıştı; çözüm GCC'yi oracle olarak kullanıp işi bölmekti.
- "it is easy to see tests pass and assume the job is done, when this is rarely the case".

**Kanıt:** Yaklaşık 2.000 oturum ve 20.000 dolar. Sınırlar açıkça yazılmış.

**DevOS:** **Uyarlayarak al:** dosya kilidiyle görev sahipliği (K09), bağlamı doldurmayan test çıktısı, örneklemli hızlı test. **Alma:** onaysız sonsuz döngüyü.

### 1.9 Dynamic workflows (code.claude.com/docs/en/workflows)
**Plan kodda durur:**
- Plan bir JS betiğidir. `agent()`, `pipeline()`, `parallel()` ve `phase()` çağrıları kullanılır; `schema` verilen ajan JSON döner.
- Ara sonuçlar Claude'un bağlamında değil, betiğin değişkenlerinde tutulur.
- Belgede "have independent agents adversarially review each other's findings" diye bir kalite kalıbı var. Paketle gelen `/deep-research` iddiaları oylar ve doğrulanamayanları "unverified" diye ayırır.

**Kayıt, yeniden başlatma ve sınırlar:**
- Betik `.claude/workflows/` altına kaydedilir.
- Çalışma aynı oturumda devam ettirilebilir. Bulutta sonuçlar "survives when the session's VM is reclaimed".
- `Date.now()` ve `Math.random()` çağrıları hata verir; böylece yeniden başlatılan çalışma aynı adımları tekrarlar.
- Sınırlar: 16 eşzamanlı ajan ve çalışma başına 1.000 ajan. Çalışma sırasında kullanıcıdan girdi alınamaz.
- `ultracode` anahtar kelimesi `-p`'den, zamanlanmış görevden ya da webhook'tan gelen prompt'ta çalışmaz.

**DevOS:**
- **Uyarlayarak al:** geniş doğrulama ve çapraz kontrol için. Bu yol derinlik sınırına takılmaz (çıkarım; bulutta sınanmadı, O11).
- **Alma:** kabul kapısının yerine koymayı. Kabul kapısı yine ayrı ve insan kararlı kalır.

### 1.10 Skill'ler, skill-creator ve Anthropic'in kendi plugin'leri
**Skill yazımı:**
- Skill üç kademede açılır.
- "Keep SKILL.md body under 500 lines"; referanslar tek seviye derinlikte.
- Açıklama üçüncü şahısla yazılır ve hem ne yaptığını hem ne zaman kullanılacağını söyler.
- "Build evaluations first". Geliştirmede iki örnek birlikte çalışır: Claude A yazar, Claude B kullanır.
- "Create verifiable intermediate outputs": önce plan dosyası, sonra betikle plan doğrulaması, sonra uygulama, en son doğrulama.
- "Solve, don't defer".

**skill-creator (`anthropics/skills@3337550`):**
- Her test için aynı turda iki alt ajan açılır: skill'li ve taban çizgisi.
- Sonuçlar `iteration-N/eval-K/` dizinlerine yazılır.
- Grader ilkeleri: "A passing grade on a weak assertion is worse than useless"; "When uncertain: The burden of proof to pass is on the expectation"; grader gizli iddiaları da çıkarır ve eval'lerin kendisini eleştirir.

**Plugin'ler (`anthropics/claude-code@7779afb`):**
- **feature-dev:** 7 aşama. Netleştirme soruları "DO NOT SKIP"; onaydan sonra uygulama ("DO NOT START WITHOUT USER APPROVAL"); inceleyici "confidence ≥ 80".
- **code-review:**
  1. haiku ile uygunluk kapısı;
  2. ilgili CLAUDE.md yollarının bulunması;
  3. 2 uyum ve 2 hata inceleyicisi;
  4. **her bulgu için ayrı bir doğrulayıcı alt ajan**, doğrulanmayanlar atılır.

  "False positives erode trust".
- **ralph-wiggum:**
  - Stop hook'u `.claude/ralph-loop.local.md` dosyasını okur; alanlar `iteration`, `max_iterations` ve `completion_promise`.
  - Oturumu `{"decision":"block","reason":<aynı prompt>}` ile aynı prompt'la sürdürür.
  - Döngü, model `<promise>` içinde beklenen metni yazınca biter. Yani bitişi model kendisi beyan ediyor (çıkarım).
- **hookify:** `conversation-analyzer` ajanı konuşmadaki "Don't use X" gibi düzeltmeleri regex kurallarına çevirir. `require-tests-run` kuralı, transcript'te test komutu yoksa oturumun bitmesini engeller.
- **security-guidance, 3 katman:**
  1. Her düzenlemede regex tabanlı uyarılar.
  2. Stop hook'unda LLM ile diff incelemesi, `asyncRewake` ile: arka planda çalışır ve bulgu olursa Claude'u uyandırır.
  3. `"if": "Bash(git commit:*)"` ve `git push` üzerinde ajan temelli commit incelemesi.

  Oturum başına bir baseline SHA tutulur. Kurumsal kurallar 8 KB bütçeli bir `claude-security-guidance.md` dosyasında durur. Zayıf nokta: satır içi gerekçe yorumunu istisna sayıyor, uygulayıcı bununla bulguyu susturabilir (çıkarım).
- **pr-review-toolkit:** Değişiklik türüne göre inceleyici seçer (silent-failure-hunter, test analizi…).

**DevOS:**
- **Al:**
  - bulgu üret → her bulguyu ayrı doğrula → doğrulanmayanı at;
  - tekrarlanan düzeltmeyi hook kuralına çevir (gereksinim 8);
  - commit ve push anında arka planda inceleme yap, hook `asyncRewake` ile uyarsın.
- **Uyarla:** Ralph döngüsünü yalnız ayrı değerlendiricinin denetlediği bitiş koşuluyla kullan.

### 1.11 Güncel eğilim verileri
- **Opus 5.5 blogu (24 Eyl 2026):**
  - Mart–Eylül 2026'da "Claude works 3.3x longer on each prompt… 68% fewer interruptions"; istek başına bağlam 2,6 kat büyüdü.
  - Öneriler: "Compact before you step away"; modeli oturum ortasında değiştirme; forked alt ajanlar üst oturumun önbelleğini kullanır.
- **CI blogu (14 Eyl 2026):**
  - "Claude authors 80% of that code"; CI işleri 25 kat arttı.
  - "Instrument your services to act as Claude's eyes and ears"; "Keep state out of the process from the start".
  - Aylarca eşik aşılınca haber veren bir izleme oturumu kullanılmış.

**DevOS:** **Al:** Kayıt sayaçları deterministik olur; durum süreç belleğinde değil dosyada tutulur; eşik aşımı izlenir.

### 1.12 İzin, yalıtım ve bellek güvenliği
**Auto mode (25 Mar 2026):**
- İzinlerin %93'ü onaylanıyor.
- İki katman var: prompt-injection sondası ve "reasoning-blind" transcript sınıflandırıcısı.
- Gerçekte aşırı hevesli eylemlerde %17 kaçırma, %0,4 yanlış pozitif.
- 3 ardışık ya da toplam 20 ret olursa insana başvurulur; `-p` kipinde süreç sonlanır.
- Varsayılan güven sınırı "the git repo you're currently working in".
- Belirsiz talimat, yıkıcı işlem için yetki sayılmaz: "clean up my branches" toplu silmeye izin vermez.

**Containment (25 May 2026):**
- "Design for containment at the environment layer first".
- Repodaki `.claude/settings.json` hook'u güven onayından önce çalıştı.
- İzin listesi "capability grant" sayılmalı: api.anthropic.com'a izin, saldırgan anahtarıyla dosya yüklenmesine yol açtı.
- "Persistent memory poisoning… CLAUDE.md files… reloaded each time".
- Alt ajan çıktısını ham çıktıdan daha güvenilir saymak "a new vector".

**Sandboxing (20 Eki 2025):**
- İzin istemleri %84 azaldı.
- Bulutta git kimlik bilgisi sandbox dışında tutulur; proxy yalnız "pushing to the configured branch" izni verir.

**DevOS:** **Al.**
- K08 için:
  - belleğe ya da durum dosyasına yazılan dış metin kaynak etiketi taşır ve talimat sayılmaz;
  - SessionStart'ta bellek dosyalarındaki değişiklik git'ten denetlenir: ne değişmiş, kim yazmış;
  - alt ajan raporu veri olarak ele alınır.
- Push'un yalnız oturum dalına açık olması, DevOS'un kalıcılık tasarımını belirleyen bir veridir.

## 2. Claude Code topluluk çerçeveleri

| Çerçeve (commit, tarih) | Çekirdek mekanizma | Kanıt | Karar |
|---|---|---|---|
| BMAD (5e33d3c, 25 Eyl 2026; v6.12.0) | plan dosyası durum makinesi, intent-contract, inceleme lensleri, triage, tickets.toml, retro | öz-beyan; tek anekdot | parçaları uyarla |
| HumanLayer ACE-FCA (f2bc7ae; komutlar 99abe67) | araştır→planla→uygula, handoff, Linear durum makinesi | açık PR'lar + yazılı başarısızlık | al |
| Compound Engineering (a763b39) | `docs/solutions` kapısı, grounding doğrulaması | yok | al |
| CCPM (7d7e462, 18 Mar 2026) | PRD→epic→görev, GitHub Issues, Script-First | "teams report", 11 senaryo | Script-First'ü al |
| Agent OS (475b0ca; v3.0) | standartlar + `index.yml` + enjeksiyon | yok | indeksi al |
| claude-flow/Ruflo (d37f283) | 108 ajan, 323 MCP aracı, yönlendirme hook'u, vektör bellek | kendi denetimi iddiaları çürütüyor | alma |
| SuperClaude (fe68862; v4.3.0) | persona, mod, PM ajanı | etki kanıtı yok | alma |
| claude-code-templates (42886b2) | katalog + kurucu + loop tarifleri | yok | denetleyerek örnek al |
| Claude Squad (ce1ffb4) | tmux + worktree + AutoYes | — | alma |
| awesome-claude-code (2c724b9) | küratörlü liste | — | keşif |

### 2.1 BMAD-METHOD
**Evrim:**
- v6.11 (9 Ağu 2026): "Quick Dev becomes Build"; eski `create-story → dev-story` kullanımdan kalktı, çekirdek 14'ten 8 skill'e indi.
- v6.12 (3 Eyl 2026): "Build decides how much ceremony… after investigating it".

**İşçi ile orkestratör ayrımı:**
- "Build Auto builds only what its invocation names; it never picks the next ticket itself".
- Adımlar:
  1. **Netleştir:** `tickets.py find`; temiz çalışma ağacı ve dal kontrolü.
  2. **Planla:** hazırlık kapısı geçilemezse bir kez onarılır, olmazsa `blocked`.
  3. **Uygula:** önce `baseline_revision`; alt ajan senkron çalışır; "plan is the sole source of truth".
  4. **İncele.**
  5. **Son durumu yaz** (HALT).
- Yol seçimi: 100 satır ve altı `oneshot`, fazlası `full`.

**Plan şablonu:**
- Durumlar: `draft | ready-for-dev | in-progress | in-review | built | done | blocked`.
- `<intent-contract>` bölümleri: Intent (Problem/Approach), Boundaries (Always/Never), I/O & Edge-Case Matrix.
- Diğer bölümler: Code Map, Tasks & Acceptance (Given/When/Then), Implementation Notes (yalnız ekleme), Plan Change Log (yalnız ekleme), Review Triage Log, Verification komutları.
- Hedef boyut "900–1300 tokens"; 1600'ün üstü `oversized`.

**Matrix Test Audit:**
- "A covering test that exists but did not run — unregistered, filtered out, skipped, or disabled — counts as missing."
- "never edit the expectation to match the code".

**İnceleme:**
- Diff bir dosyaya yazılır; lens prompt'una dosya yolu verilir, içerik değil.
- **Lensler:**
  - **Blind Hunter:** bağlamsız çalışır; bulgu tabanı `N = min(floor(sqrt(kB)+1), 10)`.
  - **Edge Case Hunter:** en sonda claims-check yapar; plan "testimony, not evidence".
  - **Verification Gap:** "if the behavior… broke… would verification fail?"
  - **Intent Alignment:** yalnız "verbatim intent" ile diff'i görür.
- **Triage:**
  - İnceleyicinin verdiği önem derecesi yok sayılır.
  - Her bulgu doğrulanır ve tek hüküm alır: `high|medium|low|false|maybe-false`. "a finding missing from the log is a triage failure".
  - Yönlendirme:
    - `intent_gap` → kod geri alınır, iş `blocked` olur;
    - `bad_plan` → kod geri alınır, plan KEEP talimatıyla düzeltilir ve kod yeniden türetilir; döngü 5'i geçerse "non-convergence";
    - `patch` → küçük düzeltme uygulanır;
    - `defer` → özellikle "any entry whose fix edits agent-context files (CLAUDE.md, AGENTS.md, rules, etc)".

**Gözetimsiz koşu kuralı:** "Never run a subagent in the background… there is no event loop to resume a yielded turn… the run stalls."

**İnteraktif build:**
- İnsan onayından sonra `<frozen-after-approval>` bloğu kilitlenir.
- Açık Sorular insana sorulur.
- "NEVER auto-push". Build yalnız yerel commit atar ve işi `built` durumunda bırakır.

**Kim hangi durumu yazar (tree-rules):**
- `draft` → `built` durumlarını build yazar; `blocked` durumunu build-auto yazar.
- "`done` — the user, or an orchestrator, through `tickets.py mark`". "No skill moves a ticket past `built`".
- "A tracker's status must never drive build routing".

**tickets.toml:**
- Alanlar: `id` (asla yeniden kullanılmaz), `after` (yalnız gerçek önkoşul), `verify`, `covers`, `hitl`, `risk`, `plan_checkpoint`, `done_checkpoint`.
- "Status never lives here".

**Retrospektif:**
- Her bulgu bir kaynak referansı taşır.
- "checked and clean" ile "never checked" ayrı yazılır.
- "Passing tests do not substitute for running the system".
- Hükümler: `accepted | accepted-with-open-items | rejected`. Bitmemiş iş varsa hüküm `rejected` olur. İnsan kararı her zaman geçerlidir; hiçbir iş "never… silently accepted".
- "Findings from sub-agents… are unverified reports".

**project-context (theory, best-practices):**
- "Not *could an agent derive this* but *what does it cost when it doesn't*".
- Aktarılan ölçümler; belge kaynak göstermiyor, yani bilinmiyor:
  - türetilebilir içerikli AGENTS.md başarıyı artırmıyor, maliyeti %20 artırıyor;
  - bilgiyi AGENTS.md'de indekslemek %100 başarı verdi, yardımsız skill %53 kaldı, açıkça çağrılan skill %79'a çıktı;
  - skill "never invoked in 56% of cases".
- "A check that lands deletes its line".
- "A working rule stays" ilkesi: nesnesi yok olmadıkça ya da insan kaldırmadıkça kural silinmez.
- **İki tür bağlam:**
  - uygulama bağlamı: repoda durur, küçüktür, her oturum yüklenir;
  - planlama bağlamı: initiative'de durur, gerektiğinde toplu okunur.

**Kanıt:** "Blind validation against seven real commits from a production HIPAA platform…" (CHANGELOG). Tek ve bağımsız olarak doğrulanmamış bir anekdot.

**DevOS:** **Uyarlayarak al.** Alınacak parçalar:
- plan dosyasıyla durum makinesi ve devam tablosu;
- intent-contract (K07);
- matrix audit;
- lensler ve hükümlü triage;
- 5 tur sınırı;
- ajan bağlam dosyasını gözetimsiz değiştirmeme;
- `done` kararının kimde olduğu tablosu (Batu ya da orkestratör; Batu yalnız kabul verir);
- iki tür bağlam ayrımı: DevOS repo bağlamı ile SOUL research bağlamı.

**Alma:** Persona menülerini, `uv` + render altyapısını, `.claude/skills` kurucusunu. **Platform notu:** BMAD, her işçinin kendi inceleme alt ajanlarını açtığını varsayar. Derinlik 1 ise işçi üst düzey oturum ya da `claude -p` olmalı. Alternatif: BMAD'ın kendi yedek yolu, yani lens prompt'larını dosyaya yazıp ayrı oturumda koşmak.

### 2.2 HumanLayer ACE-FCA ve komutları
**ACE-FCA:**
- "keeping utilization in the 40%-60% range".
- "Subagents are not about playing house and anthropomorphizing roles. Subagents are about context control."
- "a bad line of research… could land you with thousands of bad lines of code".

**Kanıt:**
- BAML'de (300 bin satır) PR #2259 ertesi sabah onaylandı.
- 7 saatte 35 bin satır: iptal desteği PR'ı birleşti, WASM PR'ı açık kaldı.
- parquet-java denemesi "did not go well" diye yazılmış.

**Komutlar:**
- **`research_codebase`:**
  - "documentarians, not critics";
  - kullanıcının andığı dosyalar alt ajan açılmadan önce ana bağlamda tam okunur;
  - canlı kod birincil kaynaktır, `thoughts/` ise yardımcı;
  - belge `git_commit`, `branch`, `topic` ve `status` içeren bir frontmatter taşır.
- **`create_plan`:** Her faz "Automated Verification" ve "Manual Verification" listelerini ayrı tutar.
- **`implement_plan`:**
  - Plan ile gerçek uyuşmazsa `Expected/Found/Why` biçiminde durulur.
  - Her faz sonunda manuel doğrulama için beklenir.
  - Devam, ilk işaretsiz maddeden olur.
- **`create_handoff`:** `git_commit`, dal, görevler ve durumları, Critical References, Recent changes (dosya:satır), Learnings, Artifacts, Action Items.
- **`resume_handoff`:** Bağlı plan ve araştırma belgeleri "do NOT use a sub-agent to read these critical files".
- **`ralph_*`:** Linear üzerinde bir durum makinesi:
  - araştırma: `research needed` → `research in progress`;
  - plan: `ready for spec` → `plan in progress` → `plan in review` (insan kapısı);
  - uygulama: `ready for dev` → `in dev`, ardından PR.

  Her çalıştırma önceliğe göre ilk 10 kaydı okur ama "only work on ONE item… SMALL or XS". Bilgi yetersizse yorum yazılıp iş geri taşınır. Uygulama bir worktree'de, ayrı bir oturumda başlatılır; izin atlama 15 dakikayla sınırlıdır (`--dangerously-skip-permissions-timeout 15m`).

**DevOS:** **Al:**
- handoff ve araştırma belgesi şablonları (K11);
- "bağlam %40–60" disiplini;
- insan kaldıracının araştırma ve planda olması: DevOS'ta bu rol ayrı eleştirmen oturumuna düşer, Batu'ya değil;
- durum etiketli iş kuyruğu ve tek seferde bir küçük iş kuralı.

### 2.3 Compound Engineering (`ce-compound`)
**Yazma kapısı:** Bir öğrenim yalnız "Non-obvious", "Durable" ve "Material" koşullarının üçü birlikte sağlanırsa yazılır. Karşı-olgusal soru sorulur: belge kaybolsa gelecekteki mühendis hatayı tekrarlar mıydı?

**Mekanizma:**
- Her çalıştırma tek öğrenim yazar.
- **Full mod:**
  - 3 paralel alt ajan çalışır;
  - `~/.claude/projects` altındaki geçmiş oturumlar taranır;
  - "What Didn't Work" bölümü doldurulur;
  - kayıt ya hata izi (bug track) ya da bilgi izi (knowledge track) olarak yazılır.
- **Örtüşme kontrolü:** 5 boyutta ölçülür. 4–5 boyut örtüşürse mevcut belge güncellenir; 2–3 boyutta yeni belge yazılır ve birleştirme için işaretlenir.
- **Grounding:**
  - bir betik atıf yapılan yolları, SHA'ları ve bağlantıları denetler;
  - bir doğrulayıcı alt ajan, iddianın dayandığı kaynak satırı alıntılar.
- `retire_when` alanı kaydın ne zaman emekliye ayrılacağını yazar.
- Gözetimsiz kip "never edits AGENTS.md/CLAUDE.md" ("gap noted, not applied").

**DevOS:** **Al:** Öğrenim kaydı için kabul kapısı, grounding doğrulaması ve `retire_when` (gereksinim 4 ve 8).

### 2.4 CCPM
**Mekanizma:**
- Kayıtlar `.claude/prds`, `epics/<ad>/epic.md` ve numaralı görev dosyalarından oluşur (`depends_on`, `parallel`, `conflicts_with`).
- GitHub'a issue ve sub-issue olarak aktarılır.
- Epic için kardeş bir worktree açılır: `../epic-<ad>`.
- Aynı worktree'de akış başına bir alt ajan çalışır. "Conflicts are never auto-resolved — agents report them and pause."
- Repo güvenlik kontrolü: şablon reposuna yazmayı reddeder.
- "Script-First Rule": durum sorularını 12 bash betiği cevaplar.

**Kanıt:** "Teams using this system report: 89%… 75%" iddiası kaynaksız. Eval 11 senaryodan ibaret ve sonucu değil prosedüre uyumu ölçüyor.

**Gözledim:**
- `next.sh` yalnız `depends_on` alanı boş görevleri "Ready" sayıyor; yorumdaki "or whose dependencies are closed" kontrolü yok.
- `blocked.sh`, bağımlılığı kapanmış görevi de "Blocked" listeliyor.
- Sonuç: bağımlı görev hiçbir zaman "ready" görünmüyor.

**DevOS:**
- **Al:** Script-First yaklaşımını, ama negatif testleriyle.
- **Alma:**
  - kaydı `.claude/` altında tutmayı (brief yasağı);
  - aynı worktree'de paralel yazımı;
  - Issues'ı tek kaynak yapmayı: kayıt repoda kalır, issue en fazla aynası olabilir.

### 2.5 Agent OS
**v3.0 (20 Oca 2026):**
- "Implementation/orchestration phases retired—frontier models handle this well on their own now".
- v2.1'de de: "Retired the short-lived 'roles' system. Too complex".

**Kalan mekanizma:**
- Standartlar `agent-os/standards/*.md` dosyalarında; `index.yml` her birine tek cümlelik açıklama verir.
- `/inject-standards` üç bağlamda çalışır: konuşma, skill ve plan.
- `/discover-standards`: her standart için "ask 1-2 clarifying questions about the 'why'"; birer birer.
- `/shape-spec`: Plan Mode zorunlu. "Task 1 always being 'Save spec documentation'". Çıktı `specs/YYYY-MM-DD-HHMM-slug/{plan,shape,standards,references}.md`.

**DevOS:** **Al:** Standart indeksi, her standardın "neden"ini yazmak ve planın ilk görevinin kaydetmek olması. **Ders:** Topluluk da rol ve orkestrasyon katmanlarını söküyor.

### 2.6 claude-flow / Ruflo
**Yapı:**
- 108 ajan, 168 komut ve 323 MCP aracı.
- CLAUDE.md 1.529 satır; Anthropic'in önerdiği sınır 200 satır.
- İzinlerde `Bash(node:*)` ve `Bash(npx:*)` var; auto mode bu tür izinleri kendisi kaldırıyor.

**Kendi denetimi (29 May 2026):**
- "The learning loop is real".
- Ama:
  - HNSW için "150x–12,500x" iddiası ölçümde 1,48 katta kaldı;
  - Flash Attention hızı "fabricated with `Math.random()` at runtime";
  - "CLI silently inverts negative reward";
  - sahte gömme gerçek diye etiketleniyor.
- "84.8% SWE-Bench" iddiası plugin README'sinde duruyor; repoda bu sayıyı üreten bir koşu ya da kayıt bulamadım (grep).

**Gözledim (`hook-handler.cjs`):**
- `route` hook'u her prompt'a bir yönlendirme kutusu ekliyor. Kullanım limitine takılınca "Free sponsored capacity… cognitum.one" reklamını da ekliyor.
- `pre-bash` hook'u yalnız 4 sabit metni arıyor ve `process.exit(1)` ile çıkıyor. Hooks belgesine göre 1 engellemez, bu yüzden komut yine çalışır (çıkarım; koşulmadı).
- `session-restore`'un yedek yolu, `%SESSION_ID%` yer tutucusuyla sıfırlarla dolu sahte bir "Restored State" tablosu basıyor.
- `auto-memory-hook` Stop anında MEMORY.md'yi yeniden yazıyor.

**İyi kurallar (CLAUDE.md):**
- "Never allow two writers in one worktree".
- "A lease or work claim coordinates ownership; it never grants authority".
- "Bind tests… to an exact clean commit".
- Öğrenen sistemler "cannot self-promote or expand tools, network, secrets, spend".

**DevOS:** **Alma.** **İlkeleri al:** tek yazıcı, kiralama yetki vermez, testin commit'e bağlanması, öz-terfi yasağı.

### 2.7 SuperClaude
**Mekanizma:**
- 30 komut ve 7 mod markdown olarak enjekte ediliyor.
- PM ajanı "Session Start (MANDATORY)": Serena belleğinden `pm_context`, `current_plan`, `last_session` ve `next_actions` okunur.
- PDCA döngüsü var; kayıtlar `docs/temp` → `docs/patterns|mistakes` yoluyla taşınır.
- "Update CLAUDE.md if global pattern discovered" kuralı var: kapısı olmayan öz-değişiklik.

**Gözledim:**
- `hooks.json` SessionStart'ta yalnız `session-init.sh` çalışıyor. Betik git durumunu ve sabit bir "✅ Confidence Check / Deep Research / Repository Index" listesi basıyor; bunları denetlemiyor. PM protokolünü de tetiklemiyor. Yani "MANDATORY" yazısı yalnız talimat.
- `ConfidenceChecker`'ın puanı `duplicate_check_complete` gibi bağlam bayraklarından hesaplanıyor.
- "ROI: 25-250x", "Error recurrence rate: <10%" iddialarının arkasında ölçüm yok.

**DevOS:** **Alma.** Yalnız hata ve desen defteri fikri, BMAD ve compound kapılarıyla birlikte.

### 2.8 claude-code-templates, Claude Squad, awesome-claude-code
**claude-code-templates:**
- Bir katalog ve kurucu.
- **Gözledim:** `prevent-direct-push.py` force-push'u korumanın dışında bırakıyor ("unless force push which is already dangerous").
- Loop'lar birer prompt tarifi, örneğin:
  - completion-contract: gereksinim ve kanıt sözleşmesi;
  - anti-spin: ilerleme yoksa, aynı yaklaşım tekrarlanıyorsa ya da iki yaklaşım arasında gidip geliniyorsa durur; "contract and tests are immutable";
  - farklı bir modelle inceleme, en çok 5 tur.

  Bu kuralları ancak başvurdukları hook'lar zorlar; o hook'lar okunmadı.

**Claude Squad (gözledim):**
- Daemon, tmux ekranında "No, and tell Claude what to do differently" metnini görünce `TapEnter()` ile Enter'a basıyor; varsayılan seçenek, yani onay, geçiyor.
- `CheckAndHandleTrustPrompt` klasör güven istemini kapatıyor.
- **Alma:** İzin ve güven kapılarını ekran okuyarak atlıyor ve Mac'e bağlı.

**awesome-claude-code:** Keşif listesi; ilgili girdiler K6'da.

## 3. Kanıt ile iddia

**Güçlü** (birincil kaynak, ölçümlü, sınırları yazılı):
- Çok ajan: %90,2 iyileşme, 15 kat token.
- auto mode: %0,4 yanlış pozitif, %17 kaçırma.
- Postmortem'ler.
- C derleyicisi.
- Eval awareness: 3,7 kat.
- Infra noise: 6 puan.
- Advanced tool use: 49→74.
- Harness tasarımı (tek örnekli maliyet tabloları).
- ACE-FCA: açık PR'lar.
- claude-flow öz-denetimi.

**Zayıf:**
- Long-running harness: sayı yok.
- Fable 5 "nearly eliminated": ayrıntı yok.
- BMAD verification-gap: 7 commit.
- BMAD'ın aktardığı AGENTS.md ve skill ölçümleri: kaynak gösterilmemiş.

**İddia:**
- CCPM "89/75/3×".
- claude-flow: "84.8% SWE-Bench" ve "×" çarpanları.
- SuperClaude: "25-250x", "<10%".

**Gözlenen kusurlar (koddan):**
- claude-flow: exit 1 hook'u, sahte geri yükleme tablosu, reklam enjeksiyonu.
- CCPM: bağımlılık mantığı.
- templates: force-push açığı.
- Claude Squad: otomatik Enter.
- SuperClaude: sabit ✅ listesi.
- Quickstart: tüm testler geçince durmuyor, `passes` denetimsiz.

## 4. DevOS'a eşleme

| Gereksinim | Mekanizma (bölüm) | Karar |
|---|---|---|
| 1 Zorunluluk | zorlama katmanı tablosu, `exit 2` ya da JSON ret (1.5); SessionStart yön bulma (1.1); zorunlu bilgi her zaman yüklenen bağlamda (2.1) | al |
| 2 Görünürlük | kanıt atıflı tur raporu (1.7); negatif testli durum betikleri (2.4); asyncRewake incelemesi (1.10) | al |
| 3 Süreklilik | initializer, ilerleme dosyası, iş listesi ve git (1.1); handoff (2.2); altı maddeli sıkıştırma (1.7); oturum günlüğü (1.3) | al |
| 4 Kayıt düzeni | tek asıl kopya: durum plan dosyasında (2.1); bilgi kapısı, grounding, `retire_when` (2.3); iki tür bağlam (2.1) | uyarla |
| 5 Kural değişikliği | per-model eval, ablasyon, bekleme süresi (1.3); CLAUDE.md'yi değiştiren düzeltme gözetimsiz yapılmaz (2.1, 2.3) | al |
| 6 Doğrulama | 20–50 görevlik eval ve referans çözüm (1.6); her bulgunun ayrı doğrulanması (1.10); matrix audit (2.1); grader ilkesi (1.10) | al |
| 7 Güvenli çalışma | ret sayacıyla insana tırmanma (1.12); HALT ile `blocked` (2.1); anti-spin (2.8) | uyarla |
| 8 Büyüme | dört alanlı görev tanımı (1.4); düzeltmeyi hook kuralına çevirme (1.10); öğrenim kapısı (2.3) | al |
| 9 Gerçek ortam | belge ile ortam çelişkisi → dene (§6) | — |

K05, K07 ve K09 için: intent-contract, 5 tur sınırı, dosya kilidi (1.8), `after`, `hitl` ve checkpoint alanları (2.1).

## 5. Dersler

1. **Tek bir kısalık satırı kaliteyi düşürdü.**
   - Kök neden: eval dardı, ablasyon yapılmıyordu.
   - Önlem: model başına eval ve satır ablasyonu.
2. **Bir önbellek hatası ajanı unutkan yaptı** ve haftalarca bulunamadı.
   - Kök neden: başka deneyler hatayı maskeledi; ekip, kullanıcının kullandığı yapıyı kullanmıyordu.
   - Önlem: gerçek ortamda dogfood.
3. **Bir geçici çözüm, daha derin bir hatayı maskeledi.**
   - Önlem: geçici çözümü kaldırırken yeniden test.
4. **Eval'ler bozulmayı yakalamadı**, çünkü "Claude often recovers well from isolated mistakes".
   - Önlem: yalnız sonuca değil ara mekanizmaya da bakan kontroller.
5. **Değerlendirici bulduğu hatayı önemsiz sayıp işi onayladı.**
   - Önlem: şüpheci ayar, eşikler, log okuma.
6. **Model bir değerlendirmenin cevap anahtarını çözdü.**
   - Önlem: oracle'a erişimi yapısal olarak kesmek; URL engeli yetmiyor.
7. **16 ajan tek büyük görevde birbirini ezdi.**
   - Önlem: işi oracle ile bölmek.
8. **Repodaki hook güven onayından önce çalıştı.**
   - Önlem: repo yapılandırmasını dış girdi saymak.
9. **Topluluk kusurlarının ortak kökü:** testler davranışa değil, bileşenin var olup olmadığına bakıyor.
   - Önlem: her DevOS betiğinin ve hook'unun negatif testi olur; bu, gereksinim 6'daki kuralı bilerek çiğneyen denemedir.
10. **Agent OS ve BMAD rol, orkestrasyon ve story katmanlarını söktü.**
    - DevOS'u rol etrafında değil; durum, kanıt ve kapı etrafında kur.

## 6. Çelişkiler ve açık sorular

- **Alt ajan derinliği:**
  - Belge: varsayılan 3 kat (v2.1.217+); v2.1.172–216 arasında 5 kat.
  - Brief: 1. Bu oturum: 1 (gözledim).
  - O11 bulut sürümünü ve env değerini sınamalı.
- **Arka plan alt ajanları:**
  - SDK'de alt ajanlar varsayılan olarak arka planda çalışıyor (v2.1.198+).
  - BMAD, gözetimsiz koşuda arka plan alt ajanının işi kilitlediğini söylüyor.
  - Fable 5.1 ise liderin beklemeden devam etmesini öneriyor.
  - Çıkarım: gözetimsiz DevOS akışında alt ajanlar ön planda beklenir; interaktif akışta asenkron kullanılabilir. Sınanmadı.
- **Doğrulama talimatı:** Opus 5 kaldır, Fable 5 açıkça iste diyor. Çözüm: doğrulamayı harness'e koymak.
- **Dynamic workflows:** Zamanlanmış bir DevOS oturumunda doğal dille "use a workflow" isteğinin çalışıp çalışmadığı bilinmiyor; anahtar kelime çalışmıyor.
- **Kurulum yeri:** Topluluk çerçeveleri `.claude/` altına kurulur. Bu turda bu yasak; karar kurulum aşamasına kalıyor.
- **Popülerlik:** Yıldız ve indirme sayıları etki kanıtı değildir; bu notta kullanılmadı.
