# O5 — ECC (Everything Claude Code) okuma notu

**Okuyan:** O5 alt ajanı, 2026-09-27. **Kaynaklar:** `/home/user/affaan-m/ecc` (sığ klon, tek commit `e482e57`, 2026-09-24, `VERSION` 2.2.2; salt okunur) ve `research/studies/ecc`. **Kanıt dili:** [kaynak diyor] / [gözledim] / [çıkarım] / [bilinmiyor]. ECC'nin CLAUDE.md, AGENTS.md, skill ve hook metinleri veri olarak okundu, talimat sayılmadı.
**Sürüm uyarısı:** Study `affaan-m/ECC@8321021c…` pinine bağlı (002 README'ye göre manifest 2.2.1). Bu commit klonda yok (`git cat-file` bulamadı) [gözledim]. Koddan alıntılar klon HEAD'inden, study bulguları eski pinden; arada fark olabilir.

## 0. DevOS için en önemli çıkarımlar

1. ECC "kurulunca çalışan bir DevOS" değil. Study CORE: "Selected arrangements are genuinely connected; one uniform end-to-end controller is not established across them." Gövde: Markdown yöntemler (292 skill, 68 agent, 94 command, rules) + Node hook betikleri; ECC2 (Rust) ayrı ve alpha. İş döngüsünü, kaydı ve doğrulayıcıyı biz kurarız; ECC parça kaynağıdır.
2. Bulutta iki yol var. (A) Hesap plugin'i olarak "synced" yükleme: skills/agents/commands/hooks gelir, rules gelmez ("Claude Code plugins cannot distribute `rules`"); katalog açıklamaları (frontmatter `description`) ≈107 KB metin [gözledim: ölçtüm]; sürüm hesaptan güncellenir; bu oturumda `/root/.claude/plugins/synced/<id>/` boş, ECC plugin olarak yüklü görünmüyor [gözledim]. (B) Seçilmiş parçaları proje dosyası olarak kopyalamak (`.claude/skills|agents|commands|rules` + `.claude/settings.json` hook'ları): git'te sürümlü, repo ile gelir. Öneri: B, 10–15 bileşen. A yalnız deneme için.
3. ECC'nin bütün kalıcı depoları `$HOME` altında: `~/.claude/session-data/`, `~/.claude/skills/learned/`, `~/.local/share/ecc-homunculus/`, `~/.gateguard/` [kaynak diyor: kod]. Bulutta makine geri alınınca kaybolur [çıkarım]. DevOS belleği repo içinde ve commit'li olmalı. ECC env'leri (`ECC_AGENT_DATA_HOME`, `CLV2_HOMUNCULUS_DIR`) repo içine yönlendirmeye izin verir ama ECC bunları commit etmez; commit DevOS kuralı olmalı.
4. Sürekli öğrenme (v2 "instinct") bulutta sessizce kapanır: `observe.sh` yalnız `cli|sdk-ts|sdk-cli|claude-desktop|claude-vscode` giriş noktalarında kayıt tutar; bu oturumda `CLAUDE_CODE_ENTRYPOINT=remote_desktop` [gözledim] → `exit 0` [çıkarım]. Gözlemci varsayılan kapalı (`"enabled": false`), açılınca arka planda `claude --model haiku` süreci ister. v1 Stop hook'u yalnız stderr'e yazar; bu çıktı modele ulaşmaz [çıkarım]. Mekanizmayı alma; fikri al: onaylı ders dosyası + SessionStart'ta sınırlı, tetik koşuluyla birlikte gösterim.
5. Doğrudan alınacak en değerli parçalar: `/save-session` şablonu (özellikle "What Did NOT Work"), SessionStart'taki "HISTORICAL REFERENCE ONLY" koruması, `suggest-compact.js`'in bağlam boyutu uyarısı (additionalContext ile), `/plan` onay kapısı, `orch-pipeline` boyut sınıfı + iki kapı, `tdd-workflow` RED/GREEN kanıt raporu, `code-reviewer` "Pre-Report Gate", `santa-method` (iki bağımsız, taze gözden geçiren), `blueprint` adım başına soğuk-başlatma özeti, `rules/common/agents.md` "Delegation Completion Contract", `config-protection` deseni.
6. İnsan kapıları uyarlanmalı: ECC planı ve commit'i kullanıcıya onaylatır; `/resume-session` "Do NOT start working automatically" der. Batu teknik doğrulayıcı değil (K-015). DevOS'ta bu kapılar bağımsız gözden geçiren ajan + deterministik testle kapanmalı; Batu'ya amaç ve teslim kabulü kalmalı.
7. ECC'nin kendi arızaları DevOS için test listesi: hook stderr'i modele gitmez; allowlist yeni host'u sessizce düşürür (VS Code, #2102; şimdi bulut); hook'lar Node 21+'da sessizce no-op oldu (CHANGELOG 2.0.0); `plugin.json` hooks alanı dört kez eklendi/silindi; belgeler koddan kaydı (`/tdd`, `~/.claude/homunculus`, `/orchestrate custom`). Kural: her mekanizma kurulduğu gerçek ortamda "tetiklendi mi, modele ulaştı mı" diye sınanır; sessiz atlama kayda geçer.
8. Study sonucu: ECC'nin kendi açıklaması (CORE) tamam; SOUL/DevOS değerlendirmesi (Q09, U20-C) "NOT STARTED". METHOD-CASE: konuşmadan bağımsız, yalnız repodan yeniden giriş hiç sınanmadı; büyüyen dosyaları baştan yeniden yazmak ilgisiz satırları bozdu. DevOS bu iki riski baştan sınamalı.
9. Alma: ECC2 daemon/TUI/tmux/worktree yönetimi, `desktop-notify`, Plan Canvas (yerel tarayıcı), dmux, dış cron (LaunchAgent/systemd; Mac'e bağlar), 292 skill'in tamamı, GateGuard.

## 1. Kapsam

**Tam okundu (ECC):** `CLAUDE.md`, `AGENTS.md`, `SOUL.md`; `.claude-plugin/` (plugin.json, marketplace.json, README, PLUGIN_SCHEMA_NOTES); `.mcp.json`; `hooks/README.md`, `hooks/hooks.json`, `hooks/hooks.metadata.json`, `hooks/memory-persistence/*`; `scripts/hooks/`: session-start-bootstrap, session-start, session-end, pre-compact, evaluate-session, observe-runner, suggest-compact, ecc-context-monitor; `scripts/lib/`: observer-sessions, agent-data-home, llm-summary, hook-flags, install-targets/claude-project; `skills/continuous-learning-v2/` SKILL.md, config.json, hooks/observe.sh, agents/observer.md, scripts/lib/homunculus-dir.sh; skill'ler: strategic-compact, context-budget, verification-loop, delivery-gate, eval-harness, autonomous-loops, continuous-agent-loop, orch-pipeline, plan-orchestrate, santa-method, agentic-os, autonomous-agent-harness, unified-memory, blueprint; agent'lar: planner, loop-operator; command'lar: save-session, resume-session, learn, learn-eval, evolve, instinct-status, promote, prune, checkpoint, quality-gate, loop-start, loop-status, plan, harness-audit; `legacy-command-shims/` README, verify, orchestrate; `contexts/` (3); `rules/README.md`, `rules/common/` agents, hooks, performance, development-workflow; `ecc2/README.md`; docs: SKILL-PLACEMENT-POLICY, capability-surface-selection, hook-bug-workarounds, MANUAL-ADAPTATION-GUIDE, skill-adaptation-policy, continuous-learning-v2-spec; `examples/CLAUDE.md`; ECC reposunun kendi `.claude/` klasöründen identity.json, team config, guardrails.

**Kısmen okundu:** README.md (106 KB: başlıklar + 264–473, 649–820, 1179–1368, 1699–1802), `the-longform-guide.md` (36–290), `the-shortform-guide.md` (başlıklar), `agents/tdd-guide.md` (gövde), `agents/code-reviewer.md` (19–112, 259–330), `tdd-workflow` (22–40, 151–262), `iterative-retrieval` (1–200), `skill-stocktake` (1–140), `gateguard` SKILL (1–60), `gateguard-fact-force.js` (1–60, 1195–1265, 1415–1500, 1560–1668), `config-protection.js` (1–80), `observer-loop.sh` (1–40, 236–300, grep), `instinct-cli.py` (grep), `utils.js` (1–120), `install/claude-settings.js` (230–300), `install-targets/helpers.js` (170–230), `resolve-ecc-root.js` (baş), `posttooluse-dispatcher.js` (kayıt listesi), `dmux-workflows`, `team-builder`, `aside`, `skill-health` (baş kısımları), CHANGELOG (1–80, 205–216, grep), `docs/tr/commands/orchestrate.md` (HANDOFF bölümü), `.claude/homunculus/instincts/inherited/*.yaml` (1–60), `tests/hooks/observe-entrypoint-allowlist.test.js` (baş, vaka listesi), `install/plan.js` (130–150), `lifecycle-hook-bootstrap.js` (grep); 7 agent'ın frontmatter'ı ve 68 agent'ın `model:` satırı.

**Okunmadı:** ~260 alan-özel skill (dil, pazarlama, lojistik, video…), ~70 command (dil-özel build/review/test, epic-*, prp-*, multi-*), `rules/` dil klasörleri, `docs/`'un büyük kısmı (19 çeviri klasörü, roadmap'ler, releases), `scripts/`'in geri kalanı, diğer harness klasörleri (`.codex`, `.cursor`, `.kiro`…), `ecc2/src` (yalnız yapı listelendi). Testler (`tests/hooks/` ≈60 dosya) listelendi, hiçbiri çalıştırılmadı (`node_modules` yok; durum değiştirmemek için).
**Study:** tam: META, STATE, CORE, PUBLICATION.md (U00–U03-A makbuzları), QUESTIONS.md, 00-WHY, notes/07, notes/39; kısmen: METHOD-CASE (§1–2, §5–9), QUESTIONS-THROUGH-U19-C (yalnız Q09 satırı); okunmadı: PUBLICATION-U*/ROUND-U* (~110 dosya), evidence/, inventory/, INDEX, METHOD, PLAN, diğer 54 not (06 bellek, 10 GateGuard dahil; CORE özetleri kullanıldı).
**Ortam gözlemi (bu bulut oturumu, salt okuma):** `CLAUDE_CODE_ENTRYPOINT=remote_desktop`, `CLAUDE_CODE_REMOTE=true`, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80`, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`, `HOME=/root`, `XDG_DATA_HOME` yok, `CLAUDE_SESSION_ID` yok (yalnız `CLAUDE_CODE_SESSION_ID`); python3 3.11, node 22; `claude` CLI `/opt/node22/bin/claude`; `/root/.claude/plugins/synced/<id>/` boş. Bunlar alt ajanın ortamı; ana oturumun da aynı olduğu bir varsayımdır [çıkarım].
**Koordinatör düzeltmesi üzerine ayrıca tam okundu:** `development-os/attempts/002/README.md` (§4–§5 synced plugin, tek/çok repolu oturum, ECC2 alpha hükümleri).

## 2. ECC'nin biçimsel yapısı

- `plugin.json`: `"mcpServers": {}`, `"skills": ["./skills/"]`, `"commands": ["./commands/"]`, `userConfig`: `hooks_enabled` (bool), `hook_profile` (minimal|standard|strict). `agents/` ve `hooks/hooks.json` "by convention" otomatik yüklenir; `agents` ya da `hooks` alanı eklemek doğrulayıcı hatası verir (PLUGIN_SCHEMA_NOTES) [kaynak diyor].
- Agent: Markdown + YAML `name, description, tools (virgüllü skaler), model`. Örnek planner: `tools: Read, Grep, Glob` / `model: opus`. Dağılım: 58 sonnet, 6 haiku, 4 opus [gözledim]. Her gövdede aynı "Prompt Defense Baseline" bloğu.
- Skill: `skills/<ad>/SKILL.md`, frontmatter `name`, `description` ("Use when …" tetikli), `metadata.origin`. Command: `commands/<ad>.md`, frontmatter `description`, gövdede `$ARGUMENTS`. AGENTS.md: "`skills/` is the canonical workflow surface … `commands/` is a legacy slash-entry compatibility surface".
- Rules: `rules/common/*.md` + dil klasörleri; plugin ile dağıtılmaz, elle `~/.claude/rules/ecc/` ya da `.claude/rules/ecc/` [kaynak diyor].
- `contexts/` (dev/research/review) `claude --system-prompt "$(cat …)"` ile kullanılır (longform guide); bulut oturumunda bu bayrak yok [çıkarım] → alma ya da skill'e çevir.
- Bilgi yerleşimi (AGENTS.md): "Personal debugging notes … → auto memory"; "Team/project knowledge (architecture decisions, API changes, runbooks) → the project's existing docs structure"; "If there is no obvious project doc location, ask before creating a new top-level file".

## 3. Mekanizmalar

### M1. Hook çatısı: kök çözümü, profil, kimlikli kayıt
- **Sorun:** hook'ları farklı kurulumlarda bulmak ve tek tek kapatabilmek.
- **İşleyiş:** Her `hooks.json` komutu aynı `node -e` önsözüyle başlar: `var e=process.env.CLAUDE_PLUGIN_ROOT;if(e&&e.trim())return e.trim();var d=p.join(o.homedir(),'.claude');…`; sonra `~/.claude/plugins/{ecc,ecc@ecc,marketplaces/ecc,…}` ve `plugins/cache/…` aranır, bulunamazsa `~/.claude`'a düşer; ardından `run-with-flags.js <hookId> <script> <profiller>`. `hook-flags.js`: `ECC_HOOKS_ENABLED`, `ECC_HOOK_PROFILE`, `ECC_DISABLED_HOOKS="id1,id2"`; plugin seçenekleri `CLAUDE_PLUGIN_OPTION_*`. Kimlik ve açıklama `hooks.metadata.json`'da, "fingerprint" ile sıraya bağlı; CI kaymayı yakalar.
- **Kayıtlı olaylar:** PreToolUse 9 (bash dispatcher, doc-file-warning, suggest-compact, observe, governance-capture, config-protection, mcp-health-check, gateguard ×2), PreCompact 1, SessionStart 2, PostToolUse 2 dispatcher (içeride quality-gate, observe, metrics-bridge, context-monitor, activity-tracker…), PostToolUseFailure 2, Stop 7, SessionEnd 1. Bir Read çağrısında en az 4, Edit'te en az 8 Node süreci açılır [gözledim: matcher sayımı]. `minimal` profilde GateGuard, observe, suggest-compact kapalı; session-start/end, evaluate-session, cost-tracker açık kalır.
- **Yollar:** `hooks/hooks.json`, `hooks/hooks.metadata.json`, `scripts/hooks/run-with-flags.js`, `scripts/lib/hook-flags.js`, `scripts/lib/resolve-ecc-root.js`.
- **Kanıt:** CHANGELOG 2.0.0: "Plugin hooks silently no-oped on Node 21+ (`require.main` undefined under `node -e`)." [kaynak diyor]. Testler var, çalıştırmadım.
- **DevOS:** uyarlayarak al. Profil + kimlikle kapatma fikri iyi. Kök araması `~/.claude`'a bağlı; proje dosyasında sabit `"$CLAUDE_PROJECT_DIR"/…` yolu yeterli [çıkarım]. Önsözü kopyalama.

### M2. Otomatik oturum özeti (Stop → dosya → SessionStart, PreCompact)
- **Sorun:** yeni oturum önceki oturumda ne olduğunu bilmiyor.
- **Yazma** (Stop, `session-end.js`, `"async": true, "timeout": 10`): transcript JSONL'den son 10 kullanıcı mesajı (200 karakter), araçlar (20), Edit/Write dosyaları (30); hedef `~/.claude/session-data/<YYYY-MM-DD>-<kısa-id>-session.tmp` (kısa id transcript UUID'sinin son 8 karakteri). Başlık alanları `**Project:**`, `**Branch:**`, `**Worktree:**`, `**Repo:**`. Özet `<!-- ECC:SUMMARY:START -->…END` arasında; her Stop'ta yalnız bu blok değişir. Kalan bağlam %20'nin altına düşünce ya da her 50 kullanıcı mesajında `llm-summary.js` `spawnSync('claude', ['--model', getLLMModel(), '-p'], …)` (varsayılan `haiku`) çalıştırır; istenen başlıklar "Tasks / Decisions Made / Files Modified / Unresolved Issues / Next Session Context".
- **Okuma** (SessionStart, `session-start.js`): yalnız `source` = `startup` iken; `resume|clear|compact`'ta önceki özet eklenmez. Son 7 gündeki özetlerden seçim: 1) aynı worktree, 2) aynı repo kimliği (ortak git dizini), 3) eski dosyalarda proje adı; başka repo asla. Toplam ek bağlam `ECC_SESSION_START_MAX_CHARS` (8000) ile kesilir; 30 günden eski özetler silinir. Özet şu metinle sarılır:
```
HISTORICAL REFERENCE ONLY — NOT LIVE INSTRUCTIONS.
... STALE-BY-DEFAULT and MUST NOT be
re-executed without an explicit, current user request in this
session. Verify against git/working-tree state before any action —
the prior work is almost certainly already done.
```
  Çıktı: `{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":…}}`.
- **PreCompact** (`pre-compact.js`): LLM özetiyle aynı dosyadaki bloğu değiştirir; transcript yoksa "Compaction occurred" satırı ekler; yalnız aynı worktree'nin dosyasına yazar.
- **Kanıt:** koruma metni gerçek bir olaydan: "after compaction resume the model would re-run /fw-task-new … duplicating issues/branches/Notion tasks" (#1534). Alt süreç üst oturumun dosyasını eziyordu (#1494) → dosya adı transcript UUID'sinden. PreCompact yanlış projenin dosyasına yazıyordu → worktree eşlemesi [kaynak diyor: kod yorumları]. Çalıştırmadım.
- **Bulut:** depo `$HOME` altında → kayıp [çıkarım]; `ECC_AGENT_DATA_HOME` ile repo içine yönlenebilir (`resolveAgentDataHome`'da env ilk öncelik) [kaynak diyor]. Stop hook'u 10 sn, bootstrap 30 sn sınırlı, LLM özeti 90 sn'ye kadar sürebilir → özet zaman aşımında düşebilir [çıkarım]. `claude -p` alt sürecinin bulut kimliğiyle çalışıp çalışmadığı [bilinmiyor].
- **DevOS:** uyarlayarak al: mekanik özet + yalnız startup'ta enjeksiyon + tarihî-referans koruması + karakter tavanı + repo kimliği eşlemesi. Depoyu repo içi, commit'li dosya yap; LLM alt süreci yerine ana ajan yazsın.

### M3. Elle devir: /save-session ve /resume-session
- **Sorun:** bağlam dolmadan ya da oturum biterken eksiksiz devir.
- **Şablon** (`commands/save-session.md`): "What We Are Building", "What WORKED (with evidence)" ("Without evidence, move it to "Not Tried Yet" instead"), "What Did NOT Work (and why)" ("This is the most important section"), "What Has NOT Been Tried Yet", "Current State of Files" (tablo: PASS/In Progress/FAIL/Not Started), "Decisions Made", "Blockers & Open Questions", "Exact Next Step", "Environment & Setup Notes". Kural: "Each session gets its own file — never append to a previous session's file"; yazınca kullanıcıya gösterip onay ister.
- **Okuma** (`resume-session.md`): aday sıralama (boş/placeholder dosyayı ele, "substantive" olanı seç, sonra en yeni mtime), sabit brifing (SESSION LOADED / WHAT NOT TO RETRY / NEXT STEP), 7 günden eskiyse uyarı, diskte olmayan dosya uyarısı; "Do NOT start working automatically. Do NOT touch any files."
- **DevOS:** şablonu al, kapıyı uyarla. Şablon DevOS devir kaydı için neredeyse hazır. "Kullanıcı onayı" yerine bağımsız okur kontrolü; "otomatik başlama yok" kuralı tersine: "Exact Next Step" netse devam et. Konum `~/.claude` değil, repo.

### M4. Öğrenme v1: evaluate-session, /learn, /learn-eval
- `evaluate-session.js` (Stop): transcript'te `"type":"user"` sayar; ≥10 ise yalnız `log(…"evaluate for extractable patterns")`; `log` = `console.error`. ECC'nin kendi notu (`suggest-compact.js`): "non-blocking PreToolUse stderr (exit 0) is only written to the debug log; it does not reach the model." → v1 Stop hook'u modele bir şey söylemiyor [çıkarım; iki kaynağın birleşimi].
- `/learn`: kullanıcı çağırır; `~/.claude/skills/<pattern-name>/SKILL.md` yazar; "guarded-write": sırları ayıkla, slug doğrula, var olanı sessiz ezme, onay al; sonra keşfedilebilirliği doğrula ("`description:` beginning with an observable `Use when ...` trigger").
- `/learn-eval`: kaydetmeden önce skills/ ve MEMORY.md'de grep ile örtüşme, karar "Save / Improve then Save / Absorb into [X] / Drop"; global mi proje mi (`.claude/skills/`) seçimi, "never default uncertain content to Global persistence".
- **DevOS:** `/learn-eval` desenini al (ders → örtüşme kontrolü → karar → doğrulama). evaluate-session'ı alma.

### M5. Öğrenme v2: instinct'ler
- **Veri akışı:** PreToolUse/PostToolUse → `observe-runner.js` → `skills/continuous-learning-v2/hooks/observe.sh` → `~/.local/share/ecc-homunculus/projects/<12-hex>/observations.jsonl` (girdi/çıktı 5000 karakterle kesilir, sır deseni maskelenir, 10 MB'da arşiv) → (etkinse) arka plan gözlemci → `projects/<id>/instincts/personal/<id>.md` → SessionStart'ta güven ≥0.7, en çok 6, proje kapsamı +0.25 ve yığın eşleşmesi +0.2 ile sıralanıp `- [project 70%] <Action'ın ilk satırı>` olarak eklenir.
- **Biçim:** `id`, `trigger: "when writing new functions"`, `confidence: 0.7`, `domain`, `scope: project`, `project_id` + `## Action`, `## Evidence`.
- **Gözlemci:** `config.json` → `"enabled": false`. Açılırsa `observer-loop.sh` son 500 satırı örnekler ve `claude --model "${ECC_OBSERVER_MODEL:-haiku}" --max-turns "$max_turns" --print --allowedTools "Read,Write" -p …` çalıştırır; prompt: "If you find 3+ occurrences of the same pattern, you MUST write an instinct file directly". 30 dk boşta kapanır.
- **Komutlar:** `/instinct-status`, `/evolve [--generate]` (anahtar kelime kümeleme → skill/command/agent taslağı), `/promote` (≥2 projede aynı id, ort. güven ≥0.8), `/prune` (30 günlük pending), `/instinct-import|export`. ECC kendi reposunda seçilmiş instinct'leri `.claude/homunculus/instincts/inherited/*.yaml` olarak commit'liyor (içe aktarma `/instinct-import` ile) [gözledim].
- **Bulut:** `observe.sh` Layer 1: `case "${CLAUDE_CODE_ENTRYPOINT:-cli}" in cli|sdk-ts|sdk-cli|claude-desktop|claude-vscode) ;; *) exit 0 ;; esac` → bu oturumda `remote_desktop` [gözledim] → gözlem yok [çıkarım]; Layer 4: alt ajan (`agent_id`) gözlenmez. VM süresi dolunca çalışan shell işleri geri gelmez (BRIEF §3, 002 D3) → gözlemci döngüsü de gelmez [çıkarım].
- **Study N07:** "The rendered instinct line contains scope, the stored confidence as a percentage, and the first non-empty action line. It does not carry the instinct ID, trigger, evidence block, source path or the rest of a multiline action." Promote aynı id'yi gruplar, anlamı karşılaştırmaz. CORE §6: "Stored confidence and repeated project labels are not independent demonstrations of usefulness."
- **Belge kayması:** `/evolve`, `/instinct-status`, `/promote` hâlâ `~/.claude/homunculus/…` der; kod `~/.local/share/ecc-homunculus` kullanır, eskisi için uyarı basar [gözledim].
- **DevOS:** mekanizmayı alma. Fikri uyarlayarak al: "atomik ders = tetik + eylem + kanıt + kapsam", SessionStart'ta az sayıda ve tetikle birlikte gösterim, eskime ve budama. Otomatik gözlemci yerine iş kapanışında ajanın yazdığı, bağımsız okurun onayladığı ders kaydı.

### M6. Bağlam yönetimi
- `suggest-compact.js` (PreToolUse Edit|Write): transcript'teki son `usage` kaydından bağlam büyüklüğü (input + cache_read + cache_creation); 200k pencerede 160k, 1M'de 250k eşik, sonra her +60k'da; ayrıca 50. araç çağrısında ve her 25'te. Mesaj stderr değil, `hookSpecificOutput.additionalContext` ile modele gider.
- `strategic-compact` skill: "Research → Planning | Yes", "Mid-implementation | No", "After a failed approach | Yes"; "Write the plan to a file before compacting — a file persists on every version and every model." Ayrıca "Claude Code 2.1.233 removed the todo/task tools by default" [kaynak diyor].
- `ecc-context-monitor.js` (PostToolUse): kalan bağlam ≤%35 uyarı, ≤%25 kritik; >20 dosya değişirse "SCOPE WARNING"; son 5 çağrı aynı araç+parametre ise "LOOP WARNING"; aynı kademe tekrar gösterilmez. Kritik metin: "Do NOT autonomously save state or write handoff files unless the user asks."
- `context-budget` skill: agent açıklaması her Task çağrısında yüklenir, ">30 words" şişkin sayılır; MCP araç başına ~500 token; CLAUDE.md zinciri >300 satırsa uyarı. `rules/common/performance.md`: "Avoid last 20% of context window for: Large-scale refactoring…". `iterative-retrieval`: alt ajana amacı ver, en çok 3 geri besleme döngüsü.
- **Bulut:** autocompact %80 [gözledim: env]. ECC'nin 160k/200k eşiği tam %80'e denk; uyarı otomatik sıkıştırmayla aynı anda gelir [çıkarım] → DevOS eşiği daha erken olmalı (örn. %60).
- **DevOS:** uyarlayarak al: transcript usage'dan ölçüm, additionalContext ile uyarı, kademe başına bir kez. Kritik eşikte ECC'nin tersine davran: devir kaydını otomatik yaz (Batu'ya sorma).

### M7. Eylem öncesi kapılar: GateGuard, config-protection
- **GateGuard** (`gateguard-fact-force.js`, PreToolUse): oturumda bir dosyaya ilk Edit/Write'ı reddeder ve ister: "1. List ALL files that import/require this file … 2. List the public functions/classes affected by this change 3. If this file reads/writes data files, show field names … 4. Quote the user's current instruction verbatim". Yıkıcı Bash ilk denemede "Write a one-line rollback procedure" ister; oturumun ilk Bash'inde "The current user request in one sentence". 3 tam retten sonra tek satırlık ret. Durum `~/.gateguard/state-*.json`, 30 dk. Alt ajanda Edit/Write kapısı atlanır.
- **Kanıt/eleştiri:** "+2.25 points" iddiası iki A/B denemeye dayanır [kaynak diyor]. Kod ikinci denemeyi sunulan olgulara bakmadan serbest bırakır (`markChecked` → retry allow) [gözledim]; CORE §7.3 aynı şeyi söyler.
- **config-protection:** var olan `.eslintrc*`, `.prettierrc*`, `biome.json`, `ruff.toml`, `.markdownlint*` düzenlemesini `exit 2` ile engeller; gerekçe: "Agents frequently modify these to make checks pass instead of fixing the actual code."
- **DevOS:** config-protection desenini al (korunacaklar: test yapılandırması, doğrulayıcı kuralları, kanon/karar dosyaları). GateGuard'ı alma (her dosyada sürtünme, retry kontrolsüz); fikrini plan şablonuna koy ("etkilenen çağıranları listele").

### M8. Ajanlar ve delege sözleşmesi
- AGENTS.md: "Use agents proactively without user prompt" (karmaşık özellik → `ecc:planner`, yeni yazılan kod → `ecc:code-reviewer`, güvenlik → `ecc:security-reviewer` …). CLAUDE.md: "When spawning subagents, always pass conventions from the respective skill into the agent's prompt."
- `planner`: salt okuma araçları; plan: Overview, Requirements, Architecture Changes, adımlar (File/Action/Why/Dependencies/Risk), Testing Strategy, Risks & Mitigations, Success Criteria; "Each phase should be mergeable independently."
- `code-reviewer`: ">80% confident"; "Pre-Report Gate" dört soru ("Can I cite the exact line?", "Can I describe the concrete failure mode?", "Have I read the surrounding context?", "Is the severity defensible?"); HIGH/CRITICAL için satır + senaryo + neden yakalanmadığı; "It Is Acceptable And Expected To Return Zero Findings"; yaygın yanlış pozitif listesi; Approve/Warning/Block.
- `rules/common/agents.md` "Delegation Completion Contract": "Your final message IS the deliverable. Never end your turn with "waiting for background agents"… If you delegate, you own collection… Decompose only when the work cannot fit in one context." Gerekçe: "research agents … returned "waiting" as their final answer. All children completed successfully but their results were orphaned."
- **Bulut:** alt ajan derinliği 1 [gözledim: env]; ECC'nin "parent, child, grandchild" varsayımı geçersiz. `dev-team` gibi 4 alt ajan açan yöntemler yalnız ana oturumdan çalışır (study N39 aynı sınırı Gemini için yazar).
- **DevOS:** uyarlayarak al: code-reviewer rapor kapısı ve sıfır-bulgu kuralı, delege sözleşmesi, planner plan biçimi, "kuralları alt ajan prompt'una koy". 68 ajanı alma; 4–6 rol yeter.

### M9. Planlama ve kapılı iş hattı
- `/plan`: "Run inline by default. Do not call the Task tool or any subagent by default."; PRD verilirse `.claude/plans/{name}.plan.md` yazar, PRD'de seçilen satırı `pending`→`in-progress` yapar; "WAIT for user CONFIRM before touching any code". Şablon: Patterns to Mirror (`path:line`), Files to Change, Tasks (Action/Mirror/Validate), Validation, Risks, Acceptance.
- `orch-pipeline`: boyut sınıfı trivial/small/standard/large (dosya sayısı, yeni bağımlılık/sözleşme, tasarım belirsizliği; güvenlik ya da API dokunan en az standard); fazlar 0 Intake → 1 Research&Reuse → 2 Plan → (3 Scaffold) → 4 TDD → 5 Review → 6 Commit; "This family is **gated, not autonomous**": GATE 1 plan onayı, GATE 2 commit onayı; "The pipeline carries no hidden state — the planning docs *are* the handoff".
- `blueprint`: hedefi 3–12 PR boyutlu adıma böler; "Every step includes a context brief, task list, verification commands, and exit criteria — so a fresh agent can execute any step without reading prior steps"; en güçlü modelle düşmanca gözden geçirme; plan değişiklik protokolü.
- `plan-orchestrate`: plan dokümanından `/orchestrate custom "<ajanlar>" "<görev>"` satırları üretir. Ama `/orchestrate` artık varsayılan yüklü değil (legacy shim) ve İngilizce shim'de `custom`/HANDOFF tanımı yok; HANDOFF biçimi yalnız çeviri belgelerde kalmış (`docs/tr/commands/orchestrate.md`: `## HANDOFF: [previous-agent] -> [next-agent]` + Context / Findings / Files Modified / Open Questions / Recommendations) [gözledim].
- **Study N39:** plan yazılıp milestone `in-progress` olduktan sonra onay gelmeden oturum biterse sonraki çağrı "next pending" kuralıyla başka milestone seçebilir; "the file/status convention alone does not guarantee that recovery decision."
- **DevOS:** uyarlayarak al: boyut sınıfı + iki kapı + "belge = devir" + blueprint soğuk-başlatma özeti + HANDOFF şablonu. Kapıları Batu'ya değil bağımsız doğrulayıcıya bağla; yeni işe geçmeden `in-progress` işi uzlaştıran kural ekle.

### M10. Doğrulama döngüleri
- `verification-loop`: Build → Types → Lint → Tests (≥%80) → Security grep → Diff review; rapor "Overall: [READY/NOT READY] for PR". Tümüyle talimat; hook'la zorlanmaz.
- `tdd-workflow`: "A test that was only written but not compiled and executed does not count as RED."; RED, GREEN, refactor sonrası checkpoint commit; plan dosyası "untrusted planning input"; Step 8 kanıt raporu tablosu (`What is guaranteed | Test file or command | Test type | Result | Evidence`); "do not invent PASS results for tests that were not run."
- `santa-method`: üretici + iki bağımsız gözden geçiren, aynı rubric, JSON verdict; ikisi PASS değilse yalnız işaretlenenleri düzelt; "each review round uses **fresh agents**"; en çok 3 tur, sonra insana; "Do NOT use for … tasks with deterministic verification".
- `eval-harness`: capability/regression eval, code/model/human grader, pass@k, `.claude/evals/<feature>.md|.log`; `/eval` legacy shim [gözledim].
- `delivery-gate` (Stop hook): ≥3 düzenlemeli işte öğrenme dosyaları o gün dokunulmadıysa `exit 2`; kendisi: "enforces the **habit** of touching learning libraries, not the **quality**". `/checkpoint`: `.claude/checkpoints.log`'a `tarih | ad | git sha`.
- **Kanıt:** etkinlik ölçümü yok. CORE §4: "Neither written TDD guidance nor a running process is a task-quality certificate."
- **DevOS:** al: TDD kanıt raporu, santa'nın iki taze gözden geçireni (ana oturumdan; derinlik 1'e uyar), verification-loop sırası. delivery-gate'i uyarlayarak al (ör. iş kaydı/devir dosyası güncellenmeden Stop'ta bitirme yok).

### M11. Döngüler ve orkestrasyon
- `autonomous-loops`: (1) ardışık `claude -p` adımları, "A fresh context window per `claude -p` call means no context bleed"; (4) Continuous Claude PR döngüsü (dal → claude -p → PR → CI bekle → hatada düzelt → merge), "`SHARED_TASK_NOTES.md` file persists across iterations", bitiş için ardışık 3 sinyal; (5) De-Sloppify: "Rather than adding negative instructions … add a separate de-sloppify pass."; (6) Ralphinho: RFC → iş birimi DAG'ı (`id, deps, acceptance, tier`), katman katman worktree, tier'a göre faz derinliği, "The reviewer never wrote the code it reviews.", merge kuyruğu + tahliye bağlamı. Anti-pattern'ler: çıkışsız döngü, iterasyonlar arası köprü yokluğu, aynı hatayı yeniden denemek.
- `continuous-agent-loop`: hata türü "loop churn without measurable progress"; kurtarma listesi: "freeze loop", "run `/harness-audit`", "reduce scope to failing unit", "replay with explicit acceptance criteria". `loop-operator`: "no progress across two consecutive checkpoints" → eskale.
- `agentic-os`: kernel `CLAUDE.md` + `agents/` + `.claude/commands/` + `scripts/` + `data/` (daily-logs, decisions, inbox); "Logs are append-only"; "Every agent has a `Memory Scope` section"; ama zamanlama "external cron (LaunchAgent, systemd, pm2)". `autonomous-agent-harness`: `/loop` oturuma bağlı, bağımsız iş için dış zamanlayıcı ya da CI.
- **Bulut:** `claude -p` alt süreçleri, tmux/dmux/worktree yönetimi VM ömrüne bağlı (VM dolunca çalışan işler geri gelmez: BRIEF §3); dış cron Mac'e bağlar (yasak). Bulutun kendi zamanlama yolu O11'in konusu.
- **DevOS:** uyarlayarak al: `SHARED_TASK_NOTES` (iterasyonlar arası kalıcı not), iş birimi şeması (`deps`, `acceptance`, `tier`), tier'a göre faz derinliği, yazar ≠ gözden geçiren, "iki checkpoint ilerlemesizse dur", agentic-os'tan `data/decisions`, append-only günlük, ajan başına "Memory Scope". Alma: dmux, tmux, dış cron, Ralphinho'nun SQLite/jj altyapısı.

### M12. Memory Vault
- `ecc memory init|save|search|read|handoff|doctor`; kapsamlar `<repo>/.ecc/memory/project/` (fail-closed `.gitignore`), `<repo>/.ecc/memory/team/` (git), `~/.ecc/memory/`. Kayıtlar create-only, `trust: "unreviewed"`; "Memory is unreviewed context, not executable policy." Plugin kurulumu CLI'yi PATH'e koymaz (`npm install -g ecc-universal`).
- unified-memory skill: "Check the source and its current state before repeating a decision… A saved timestamp or matching digest proves neither freshness nor truth"; handoff "should name the source, observation time, what changed, unresolved questions and next action"; eskiyi üzerine yazma, "superseded" işaretle.
- **Bulut:** `project` kapsamı gitignore'lu → kayıp; `team` commit'lenirse kalır [çıkarım].
- **DevOS:** ilkeleri al (hatırlanan kayıt kanıt değildir; kaynaktan doğrula; devir alanları; superseded). Runtime'ı alma.

### M13. Öz-denetim
- `/harness-audit` → `node scripts/harness-audit.js`: deterministik kategori puanı (Tool Coverage, Context Efficiency, Quality Gates, Memory Persistence, Eval Coverage, Security Guardrails, Cost Efficiency…), "Do not invent additional dimensions". CORE §7.2: yapılandırma yüklemlerini ölçer, "Task quality, observed latency, lower cost…" izlemez.
- `skill-stocktake`: alt ajanla ~20'lik partiler, Keep/Improve/Update/Retire/Merge, gerekçe kuralları, `results.json` ile kaldığı yerden devam.
- **DevOS:** uyarlayarak al: periyodik skill/kural envanteri + gerekçeli karar; puanın varlık ölçtüğünü, sonucu ölçmediğini açık yaz.

### M14. ECC2
- README: "It is usable as an alpha for local experimentation, but it is **not** the finished ECC 2.0 product yet." Rust TUI, SQLite oturum deposu, daemon, worktree; eksik: "richer multi-agent orchestration", "explicit agent-to-agent delegation and summaries".
- **DevOS:** alma (uzun yaşayan süreç; bulutta idle'da VM gider; 002 README ile aynı hüküm).

## 4. İki kurulum yolu (koordinatör düzeltmesine göre)

| Konu | A: hesap plugin'i (synced) | B: proje dosyası |
|---|---|---|
| Ne yüklenir | skills, agents, hooks (002 README D2) ve plugin.json'daki commands [çıkarım]; MCP `{}` ile kapalı | yalnız kopyalanan skill/agent/command/rule + `.claude/settings.json` hook'ları; tek repolu oturumda yüklenir, çok repolu oturumda repo ayar/hook'ları farklı (002 §4) |
| Rules | gelmez [kaynak diyor] | `.claude/rules/…` olarak gelir |
| Bağlam | 292 skill + 68 agent + 94 command açıklaması ≈107 KB [gözledim]; README: "The plugin advertises the installed catalog to the model". Claude Code'un listeyi kısıp kısmadığı [bilinmiyor; O11] | yalnız seçilenler |
| Sürüm | hesaptan sync ile değişir, sabit değil (002) | git'te, gözden geçirilmiş, sabit |
| Hook kökü | `CLAUDE_PLUGIN_ROOT` hook ortamında verilir [çıkarım] | ECC `claude-project` hedefi var (rules → `.claude/rules/ecc/`, skills → `.claude/skills/`, hooks → settings.json "merge-hook-ids") ama önsözü `var e=Buffer.from('<base64 mutlak yol>','base64')…` ile değiştirir → mutlak yol commit'lenir [gözledim: `install/claude-settings.js`, `install/plan.js`]. Elle `$CLAUDE_PROJECT_DIR` yolu daha sağlam [çıkarım] |
| Komutların betik araması | `/instinct-status` vb. Bash'te `${CLAUDE_PLUGIN_ROOT:-…}` arar; arama listesinde `plugins/synced` yok → `~/.claude`'a düşebilir [çıkarım] | kopyalanan komutlar yeniden yazılmalı |
| Veri depoları | `$HOME` → makine geri alınınca kayıp [çıkarım] | env ile repo içine; commit'i DevOS kuralı yapmalı |
| Yük | Read'de 4, Edit'te 8 Node süreci; GateGuard ilk Edit/Bash'i reddeder | yalnız seçilen hook'lar |
| Bu oturum | synced klasör boş → ECC yüklü değil [gözledim] | — |

ECC README'nin "declarative" yolu (`~/.claude/settings.json` içinde `extraKnownMarketplaces` + `"enabledPlugins": {"ecc@ecc": true}`) bulutta işe yaramaz: 002 README §4'e göre repo `enabledPlugins` bildirimi bulutta marketplace kurulumu yapmaz; kullanıcı ayarı da Mac'ten buluta geçmez.

**Karar önerisi:** B. DevOS çekirdeği A'ya bağlanmasın (sürüm kayar, rules yok, bağlam şişer, veri kaybolur, hook yükü). A yalnız "ECC'yi denemek" için; denenirse ilk iş plugin seçeneği `hook_profile: minimal` (ya da `ECC_HOOK_PROFILE=minimal`) ve ölçüm. B'de ECC'nin installer'ını çalıştırmak yerine seçilen dosyaları elle, kaynak commit'i not edilerek kopyala (ECC'nin kendi politikası: "copy the underlying idea, not the external dependency").

## 5. Study ne sonuca vardı

- **Merkez cevap (CORE §1):** "ECC combines reusable operating procedures and host-specific deployment with several implemented work, execution, information, review and control arrangements. Selected arrangements are genuinely connected; one uniform end-to-end controller is not established across them." Birim, depo adı değil "entry point, installed assets, host, controller, store and responsible actor" birleşimidir.
- **Ölçüt (CORE §2):** "the question “does ECC support X?” needs a route and a meaning of support: present, installable, discovered, selected, executed or effective." DevOS için doğrudan kullanılabilir bir sınama dili.
- **Öğrenme (CORE §6):** instinct yolu "a real information-to-behavior route … Its evidence is nevertheless sampled and compressed; a first action line can survive while its trigger, evidence and identity do not."
- **Bağlantı türleri (CORE §9):** dar sözleşmeyle gerçek; dönüştürülmüş/tutarsız; bilinçli olarak aktör aracılı (plan onayı, TDD kanıt yargısı, PR kararı); izlenen yolda kurulmamış.
- **Kurulamayanlar (CORE §10):** "authenticated organization-wide approval", "independent task-quality measurement", "autonomous beneficial self-improvement".
- **DevOS değerlendirmesi:** STATE: "Next selected: U20-C / Q09, bounded project-facing/joint-evaluation preparation, **NOT STARTED**." Yani study ECC'yi DevOS için hiç değerlendirmedi.
- **METHOD-CASE:** üretici→tüketici izini ve küçük ayırt edici denemeleri koru; yayın yolunu değiştir. "It does **not** demonstrate that a fresh agent with no conversation context selected the correct task from the repository alone." Önerilen asgari kalıcı roller: "current state, original evidence, an interpretation/change record, retrieval pointers and a publication check".
- **PUBLICATION makbuzları:** main ilerlediği için force'suz güncellemeler birkaç kez 422 ile reddedildi; çözüm main'i yeniden okuyup yalnız study alt ağacını bağlamak ya da dal + PR; force yok, eşzamanlı işler korundu [kaynak diyor].

## 6. Dersler (ne yanlış gitti, kök neden, önlem, kaynak)

1. **Hook çıktısı modele ulaşmadı.** v1 öğrenme Stop hook'u yalnız stderr'e yazar. Kök: exit 0'da stderr debug log'a gider. Önlem: modele gidecek her şey `additionalContext` ya da dosya; "ulaştı mı" testi. Kaynak: `evaluate-session.js`, `suggest-compact.js` yorumu.
2. **Allowlist yeni host'u sessizce düştü.** VS Code gözlemleri kayboldu (#2102); aynı kural bulutu (`remote_desktop`) da düşürür. Kök: sessiz `exit 0`, gerçek ortamda test yok. Önlem: bilinmeyen ortamda uyarı kaydı; kurulum sonrası ortam duman testi. Kaynak: `observe.sh`, `tests/hooks/observe-entrypoint-allowlist.test.js`.
3. **Bütün hook'lar sessizce no-op.** Node 21+'da `require.main` tanımsız. Önlem: her platform/Node değişiminde "hook gerçekten çalıştı" izi (ör. zaman damgalı dosya). Kaynak: CHANGELOG 2.0.0.
4. **Platform davranışı değişti, yapılandırma dört kez ekle/sil.** `plugin.json` "hooks" alanı; Claude Code v2.1 otomatik yüklemeye geçti. Önlem: platform sürümünü kaydet, regresyon testi. Kaynak: `PLUGIN_SCHEMA_NOTES.md` tablosu.
5. **Sıkıştırma sonrası eski komut yeniden çalıştı.** Kopya issue/branch/Notion işleri (#1534). Önlem: devir metni "tarihî referans" etiketli, eylemden önce git durumu doğrulanır. Kaynak: `session-start.js`.
6. **Kayıt ezildi / yanlış projeye yazıldı.** Alt süreç üst oturum dosyasını ezdi (#1494); PreCompact paylaşılan dizinde başka projenin dosyasına yazdı. Önlem: kayıt kimliği oturuma özgü, depo repo kapsamlı. Kaynak: `session-end.js`, `pre-compact.js`.
7. **Belgeler koddan kaydı.** `/tdd`, `/e2e` (CLAUDE.md'de) artık yüklü değil; komutlar eski homunculus yolunu söylüyor; `/orchestrate custom` tanımı yalnız çevirilerde; longform'un `examples/sessions` bağlantısı yok. Önlem: tek kaynak + belge-kod tutarlılık denetimi. Kaynak: `legacy-command-shims/README.md`, `commands/evolve.md`, `instinct-cli.py`.
8. **Alt ajan sonuçları sahipsiz kaldı.** Ajanlar "waiting" diye bitirdi. Önlem: delege eden toplar; son mesaj teslimattır. Kaynak: `rules/common/agents.md`.
9. **Arka plan gözlemci kaçtı.** Paralel Claude analiz süreçleri, bellek patlaması (#521, #536). Önlem: arka plan işi sınırlı (bekleme, yeniden giriş kilidi, örnekleme); bulutta arka plana güvenme. Kaynak: `observer-loop.sh`, CHANGELOG.
10. **Plan durumu onaydan önce ilerledi.** `in-progress` iş yarım kalınca sonraki çağrı başka işi seçebilir. Önlem: yeni işten önce yarım işi uzlaştır. Kaynak: study N39.
11. **Sıkıştırılan ders koşulunu kaybetti.** Instinct satırı tetiği taşımaz. Önlem: tetik + eylem birlikte, kaynak yolu ile. Kaynak: study N07.
12. **Kalite iddiası zayıf kanıta dayandı.** GateGuard "+2.25" iki denemeden; retry olguya bakmadan serbest. Önlem: bir mekanizmayı kanıt olmadan "kalite kapısı" sayma. Kaynak: `skills/gateguard/SKILL.md`, `gateguard-fact-force.js`.
13. **Araştırma sürekliliği: yeniden giriş sınanmadı; büyük dosyaların yeniden üretimi ve ikili aktarım bozuldu.** Önlem: DevOS'ta konuşmasız yeniden giriş testi (önceden belirli olguları yalnız repodan bulma), küçük yamayla düzenleme, ikili veri üretmeme. Kaynak: METHOD-CASE §5–7.

## 7. Kısa aktarım tablosu

| Parça | Karar | Bulut uyarlaması |
|---|---|---|
| save/resume-session şablonu | al | repo içi devir dosyası; otomatik devam |
| SessionStart özeti + "HISTORICAL REFERENCE ONLY" | uyarlayarak al | proje hook'u, repo içi kaynak, startup'ta |
| suggest-compact + context-monitor | uyarlayarak al | eşik %80'den önce; kritikte otomatik devir |
| /learn-eval kalite kapısı | al | ders dosyası repo'da, bağımsız okur onayı |
| CLv2 instinct/gözlemci | alma | fikir: tetik+eylem+kanıt dersleri |
| config-protection | al | doğrulayıcı/test/kanon dosyalarını koru |
| GateGuard | alma | plan şablonuna "etkilenenler" alanı |
| code-reviewer, santa-method | al | ana oturumdan iki taze gözden geçiren |
| tdd-workflow kanıt raporu | al | iş kaydına RED/GREEN kanıtı |
| orch-pipeline boyut + kapılar | uyarlayarak al | kapılar doğrulayıcıya, Batu'ya değil |
| blueprint, HANDOFF | al | adım başına soğuk-başlatma özeti |
| Delegation Completion Contract | al | derinlik 1'e göre yeniden yaz |
| SHARED_TASK_NOTES, DAG şeması | uyarlayarak al | iş kaydı alanları: deps, acceptance, tier |
| Memory Vault ilkeleri | ilkeyi al | runtime yok |
| harness-audit, skill-stocktake | uyarlayarak al | periyodik envanter |
| ECC2, dmux, tmux, dış cron, Plan Canvas, desktop-notify | alma | Mac/uzun süreç bağımlı |
