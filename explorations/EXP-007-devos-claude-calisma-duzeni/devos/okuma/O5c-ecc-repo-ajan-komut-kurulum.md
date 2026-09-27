# O5c — ECC reposu: ajanlar, komutlar, kurallar, kurulum (derin okuma)

**Okuyan:** O5c alt ajanı, 2026-09-27. **Kaynak:** `/home/user/affaan-m/ecc` (sığ klon, HEAD `e482e57`, `VERSION` 2.2.2; salt okunur). **Standart:** BRIEF.md + STANDART.md. **Kanıt dili:** [kaynak diyor] / [gözledim] / [çıkarım] / [bilinmiyor]. ECC'nin CLAUDE.md, AGENTS.md, ajan, komut ve kural metinleri veri olarak okundu; talimat sayılmadı.

> **KAPSAM BÖLÜNMELİ.** Kapsamın ajanlar, komutlar, kök belgeler, `.claude-plugin/`, `contexts/`, `rules/common`, kurulum rehberleri, Claude kurulum hattı ve kurulum yaşam döngüsü motoru (`install-lifecycle.js` dahil) tam okundu. Şunlar **tam okunmadı**: `rules/` altındaki 111 dil kuralı dosyası (yalnız `paths:` başlıkları açıldı), `scripts/lib`'in kurulum dışı bölümü (~1 MB), rehberli kurucu ve Claude dışı hedef adaptörleri, `scripts/` altındaki orkestrasyon ve iş takibi CLI'leri (`auto-update.js` yalnız grep ile). Tam liste §1.3'te. Ek ajan gönderilmeli.

## 0. DevOS için en önemli çıkarımlar

1. **ECC bütün olarak, sabit sürümle, proje dosyası olarak kurulabiliyor.** ECC'nin kendi kurucusu bunu yapıyor: `install.sh --target claude-project --profile full`. Kuru koşuyla gözledim: 1198 işlem, ~8 MB, 292 skill'in hepsi, 68 ajan, 94 komut, 122 kural dosyası, hook çalışma zamanı ve `.claude/settings.json` içine 24 hook kaydı. `node_modules` gerekmedi, hiçbir dosya yazılmadı. O5'in "yalnız parçalar alınır" hükmü platform zorunluluğu değil, bir tercihti.
2. **Bütün kurulum bulutta kısmen bozuk çalışır.** Bozulan her yerin kök nedeni aynı üç varsayım:
   - ECC'nin kök araması `~/.claude` ve plugin dizinlerine bağlı; proje `.claude/` ve `plugins/synced` bu aramada yok.
   - Ajan adları plugin önekiyle yazılmış (`ecc:planner`); proje kurulumunda ajanlar öneksiz (`planner`).
   - Bellek, öğrenme ve oturum depoları `$HOME` altında.
   Ayrıca: `gh`, `codex` ve `gemini` bu ortamda yok; `workflows/orch-review.workflow.js` hiçbir kurulum modülünde yok.
3. **Hook komutları mutlak yol taşıyor.** Kurucu her hook komutuna `<proje>/.claude` yolunu base64 olarak gömüyor [gözledim: kuru koşu]. Bulutta repo `/home/user/<repo>` altında; yol oturumlar arasında sabit kalırsa çalışır, değişirse kırılır [bilinmiyor]. Düzeltme: önsözü `CLAUDE_PROJECT_DIR` ile yeniden yazmak.
4. **Kurucu dolaylı ayar da değiştiriyor.** Kurucu, açık tercih yoksa `.claude/settings.json` içine `"includeCoAuthoredBy": false` yazıyor [kaynak diyor: `claude-commit-attribution.js`]. Bu, bulutun commit atıf kuralıyla çatışır. DevOS kurulumunda açıkça `attribution` ayarlanmalı.
5. **Bağlam maliyeti ölçüldü.** Tam katalogun açıklama metni 108 KB tutuyor: skill 84 KB, ajan 14 KB, komut 10 KB [gözledim]. `rules/common` 18 KB ve her oturumda yükleniyor. 111 dil kuralı `paths:` ile kapsamlı; yalnız eşleşen dosyada yükleniyor [kaynak diyor: frontmatter].
6. **Hook yükü yüksek.** 24 hook var; bir Edit çağrısı 8, bir Read çağrısı 4 Node süreci açıyor [gözledim]. `ECC_HOOK_PROFILE=minimal` ve `ECC_DISABLED_HOOKS` ile kısılabiliyor [kaynak diyor].
7. **Orkestrasyonun en olgun parçası `/orch-review` iş akışı.** Tasarımı en sıkı doğrulayıcı kalıbı bu (README tek bir yerel deneme bildiriyor; ben koşmadım): boyut başına bir gözden geçiren, kanıt parçasına göre tekilleştirme, her CRITICAL/HIGH bulguya düşmanca doğrulayıcı. Belirsizlik engeli kaldırmaz; bir boyut çökerse sonuç onay olamaz. DevOS'un bağımsız doğrulayıcısı için doğrudan örnek. Ancak ajan adları `ecc:` önekli ve betik kurulumla gelmiyor; uyarlanmalı.
8. **Kapılar Batu'ya bağlı.** ECC kapıları kullanıcıya bağlıyor: `/plan` onay bekler, `orch-*` iki kapı (plan, commit), `/resume-session` "Do NOT start working automatically", `santa-loop` 3 turdan sonra insana döner. DevOS'ta bu kapılar bağımsız doğrulayıcıya ve deterministik teste bağlanmalı (K-015).
9. **Döngü desenleri somut ama motor yok.**
   - `gan-build`: en çok 15 tur, eşik 7.0, 3. turdan sonra iki tur iyileşme yoksa dur.
   - `santa-loop`: iki taze gözden geçiren, en çok 3 tur.
   - `loop-operator`: "no progress across two consecutive checkpoints" → eskale.
   - `/loop-start` yalnız talimat; arkasında betik yok [gözledim].
10. **Derinlik 1 ile uyumlu.** Hiçbir ajanın Task/Agent aracı yok. Ajan içi "hand off to security-reviewer" yalnız öneri; zincir ana oturumdan yürür. `harness-optimizer` bunu açıkça söylüyor: "subagents cannot invoke slash commands".
11. **İş kaydı adayları.**
    - `/epic-*`: GitHub issue gövdesinde koordinasyon bloğu, etiket, denetim yorumu, bağımlılık açma. `gh` ve `scripts/github-coordination.js` ister; bulutta `gh` yok.
    - PRD→plan→rapor zinciri: `.claude/prds`, `.claude/plans`, `.claude/PRPs/{prds,plans,reports}`; faz durumu `pending→in-progress→complete`. Repo içinde yaşar; DevOS iş kaydına en yakın hazır biçim.
12. **Belgeler koddan kaymış.** COMMAND-AGENT-MAP, COMMANDS-QUICK-REF, CLAUDE.md, TROUBLESHOOTING, `spec-miner` ve `/checkpoint` koddan farklı şeyler söylüyor (§2, §9). DevOS, ECC'yi kodundan okumalı; belge-kod tutarlılığı denetimini kendi kuralı yapmalı.
13. **Kurulum defteri güçlü ama yerinde yamaya izin vermiyor.** Kurucu her dosyayı sha256 ile deftere yazıyor. `doctor` sapmayı buluyor, `repair` sapan dosyayı kaynaktan geri yazıyor, `uninstall` değişmiş dosyayı koruyor [kaynak diyor: `install-lifecycle.js`]. Sonuçları:
    - ECC dosyasını yerinde yamalamak `repair`'de geri alınır. Yama ayrı dosyada durmalı ya da her kurulumdan sonra yeniden koşmalı.
    - Defterde olmayan, önceden var olan dosyaya kurucu dokunmuyor ("Skipped user-owned file"). DevOS, aynı adla dosya koyarak bir ECC parçasını bilerek gölgeleyebilir.
    - Defter mutlak yol taşıyor. Repo başka yolda açılırsa kurucu yeniden kurmayı reddediyor. Bulutta yol sabitse sorun yok [çıkarım: kod].
    - `/auto-update` `git pull --ff-only` yapıyor; sabit sürümü bozar, kullanılmamalı [kaynak diyor: grep].
14. **Önerim: "kopyala-seç" değil, "sabitle-kur-yamala-üstüne ekle".**
    - ECC'yi pinli commit'ten kendi kurucusuyla, `ecc-install.json` ile kur.
    - Bulut yama katmanını ayrı dosyalarla yaz: kök çözümü, `ecc:` adları, `$HOME` depoları, hook profili, atıf.
    - DevOS katmanını ayrı adlarla ekle.
    - Profil `developer` ya da `full`; hook profili `minimal`'den başlayıp ölçülerek açılır.
    Ayrıntı §7.6 ve §8.

## 1. Kapsam

### 1.1 Tam okundu

- **Kök belgeler:** `CLAUDE.md`, `SOUL.md`, `AGENTS.md`, `README.md` (2039 satır, baştan sona), `agent.yaml`, `.mcp.json`, `.claude-plugin/` (4 dosya).
- **`agents/`:** 68 dosyanın hepsi. "Prompt Defense Baseline" bloğu 65 dosyada özdeş (md5 ile karşılaştırdım); bu yüzden bu 65 dosyada blok bir kez okundu. İki değişik blok (`rag-pipeline-reviewer`, `spec-miner`) ayrıca okundu.
- **`commands/`:** 94 dosyanın hepsi. Liste script ile karşılaştırıldı, eksik yok.
- **Diğer yüzeyler:** `legacy-command-shims/` (README + 12 shim), `contexts/` (3), `rules/README.md`, `rules/common/` (10 dosya), `workflows/` (README + `orch-review.workflow.js`).
- **Kurulum:** `manifests/` (`install-modules.json` tam; `install-profiles.json` tam; `install-components.json` 84 girdinin id/aile/modül alanları, açıklamalar 110 karakterde kesik; assets), `install.sh`, `install.ps1`.
- **`scripts/`:** `install-apply.js`, `install-plan.js`, `ecc.js`, `doctor.js`, `repair.js`, `uninstall.js`, `list-installed.js`, `setup.js`.
- **`scripts/lib`:** `install-executor.js`, `install/{request,runtime,config,plan,apply,claude-settings,hook-consent,link-rewrite,ownership-guard,claude-skill-migration,excluded-paths-reconciliation,inventory,claude-settings-lock}.js`, `install-targets/{claude-project,claude-home,registry,helpers}.js`, `install-manifests.js`, `install-state.js`, `install-lifecycle.js` (2453 satır, parça parça sonuna kadar), `resolve-ecc-root.js`, `hooks-config.js`, `claude-plugin-setup.js`, `claude-scope-migration.js`, `claude-dry-run-sandbox.js`, `claude-commit-attribution.js`, `install-state-store-sync.js`, `invocation-environment.js`, `path-safety.js`, `atomic-write.js`, `hook-flags.js`, `agent-data-home.js`, `missing-dependency.js`, `mcp-config.js`, `compute-sponsor.js` (sponsor metni; konu dışı).
- **Rehberler:** `the-shortform-guide.md`, `the-longform-guide.md` (boş satırlar ve görsel satırları atlanarak), `docs/token-optimization.md`, `docs/SELECTIVE-INSTALL-ARCHITECTURE.md`, `docs/MIGRATION-1X-TO-2.0.md`, `docs/COMMAND-AGENT-MAP.md`, `COMMANDS-QUICK-REF.md`, `TROUBLESHOOTING.md`, `docs/TROUBLESHOOTING.md`, `docs/MANUAL-ADAPTATION-GUIDE.md`.
- **ECC2:** `ecc2/README.md`, `Cargo.toml`, kaynak dosya listesi (17 dosya, 54.5 bin satır) ve CLI alt komut adları. Rust gövdesi okunmadı; kapsam "genel yapı" idi.

### 1.2 Koşu ve ortam gözlemi (salt okuma)

- **Kuru koşu:** `cd <boş dizin> && HOME=<boş dizin> node scripts/install-apply.js --target claude-project --profile full --dry-run --json`. Çıkış 0. Ardından iki boş dizinde `find` ile kontrol ettim: dosya oluşmadı. Plan JSON'u scratchpad'e yazıldı; analizden sonra silindi.
- **Bu alt ajanın ortamı:**
  - Araçlar: `claude` 2.1.42, node 22.22.2, python3 ve jq var; `gh`, `codex` ve `gemini` yok.
  - Ortam değişkenleri: `CLAUDE_CODE_ENTRYPOINT=remote_desktop`, `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_default`, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80`. Bash aracında `CLAUDE_PLUGIN_ROOT` ve `CLAUDE_PROJECT_DIR` tanımsız.
  - `~/.claude` içeriği: `/root/.claude/plugins/synced/<id>/` boş. `/root/.claude/sessions/` Claude'un kendi dosyalarını tutuyor (`105.json`); ECC'nin eski `~/.claude/sessions/` yolu bununla aynı adı taşıyor. Bulutun kendi hook betikleri de burada: `stop-hook-git-check.sh`, `stop-hook-reply-gate.py`.
- Bu gözlemler alt ajan ortamına ait. Ana oturumun da aynı olduğu bir varsayım [çıkarım].

### 1.3 Okunmadı — KAPSAM BÖLÜNMELİ listesi (ek ajan için)

- **`rules/` dil klasörleri (111 dosya, 8816 satır):** angular, arkts, cpp, csharp, dart, fsharp, golang, java, kotlin, nuxt, perl ve php'de 5'er; python 6; react 5; react-native 8; ruby, rust, swift, typescript ve vue'da 5'er; web 7. Hepsinin başlığını açtım: dile özgü kodlama, test, güvenlik ve hook önerileri, her biri `paths:` ile kapsamlı. Mekanizma (yükleme davranışı) çıkarıldı. İçerik DevOS'un yığını belli olunca okunmalı.
- **`scripts/lib` kurulum yardımcıları (kalan):**
  - Rehberli kurucu: `install-guided.js` (scripts/), `harness-capabilities.js`, `multi-harness-setup.js`. `--guided` yolu etkileşimli; bulut reçetesinde kullanılmıyor. Okunmadı.
  - `state-store/*`: kurulum sonrası SQLite projeksiyonu. BRIEF'e göre oturum ve durum modülleri O5e'nin.
  - Hook çalışma zamanı kütüphaneleri: `utils.js`, `package-manager.js`, `project-detect.js`. Bunları hook betikleri ve `session-start` kullanıyor [gözledim: grep]; O5d/O5e kapsamına düşer.
  - **Konu dışı (açıldı):** 13 Claude dışı adaptör (`install-targets/{adal,antigravity,codebuddy,cursor,gemini,joycode,kimi,zed}-project.js`, `{codex,hermes,openclaw,opencode,qwen}-home.js`) ve `install/{codex-user-config,antigravity-agent,antigravity-legacy-migration,opencode-legacy-migration}.js`. Başlıklarını ve `target` alanlarını açtım: hepsi başka harness'lere ait.
- **`scripts/lib` kurulum dışı (~1 MB):** `control-pane/*`, `plan-canvas/*`, `github-coordination*`, `eval-harness/*`, `agent-proximity/*`, `skill-evolution/*`, `skill-improvement/*`, `session-adapters/*`, `mcp-inventory/*`, `worktree-lifecycle/*`, `memory-vault*`, `session-manager.js`, `session-aliases.js`, `orchestration-session.js`, `tmux-worktree-orchestrator.js`, `nasiko-release.js`, `powershell-destructive-command.js`, `codex-*` ve diğerleri. Orkestrasyon ve iş takibiyle ilgili olanlar ek ajan için öncelikli: `github-coordination*`, `orchestration-session.js`, `tmux-worktree-orchestrator.js`, `worktree-lifecycle/*`, `control-pane/*`.
- **`scripts/` kurulum dışı:** `auto-update.js` (yalnız grep: satır 16, 73-78, 273-274), `harness-audit.js` (35 KB), `loop-status.js` (24 KB), `status.js`, `work-items.js`, `claw.js`, `consult.js`, `gan-harness.sh`, `github-coordination.js`, `setup-package-manager.js`, `catalog.js`, `skills-health.js`, `orchestrate-codex-worker.sh`, `orchestrate-worktrees.js`, `orchestration-status.js` (bu 15'i ~220 KB) ve diğer 30'a yakın CLI. Öncelik sırası: `harness-audit.js`, `gan-harness.sh`, `loop-status.js`, `work-items.js`, `github-coordination.js`, `auto-update.js`; bunlar kapsamdaki orkestrasyon ajanlarını ve iş takibini süren betikler. Kuru koşu planına göre `.claude/scripts/`'e yalnız sekizi kopyalanıyor: `auto-update`, `claw`, `harness-audit`, `orchestrate-worktrees`, `orchestration-status`, `setup-package-manager`, `skills-health` ve `orchestrate-codex-worker.sh`. `gan-harness.sh`, `loop-status.js`, `work-items.js` ve `github-coordination.js` kopyalanmıyor; bunlara dayanan komutlar proje kurulumunda ECC checkout'u ya da `npx` paketi ister [gözledim: plan JSON; bağımlılık çıkarım].
- **`docs/`:** `COMMAND-REGISTRY.json`, `ECC-2.0-*` yol haritaları, 13 çeviri klasörü, `releases/`, `the-security-guide.md`. BRIEF'in saydığı dört rehber türüne (longform, shortform, token, kurulum) girmiyorlar; okunmadılar. `COMMAND-REGISTRY.json` komut kataloğunu doğrulamak için ek ajana önerilir.
- **Kapsam dışı (O5d'nin):** `skills/`, `hooks/`, `scripts/hooks/`.

## 2. O5 notunun iddiaları: doğrulama

| O5 iddiası | Hüküm | Kanıt |
|---|---|---|
| 292 skill, 68 ajan, 94 komut | Doğru | Sayım [gözledim] |
| Katalog açıklamaları ≈107 KB | Doğru (108.5 KB) | Frontmatter ölçümü [gözledim] |
| 58 sonnet, 6 haiku, 4 opus | Doğru | `grep '^model:'` [gözledim] |
| "Her gövdede aynı Prompt Defense Baseline bloğu" | Kısmen yanlış | 65 özdeş, 2 genişletilmiş (`rag-pipeline-reviewer`, `spec-miner`), `agent-evaluator`'da yok [gözledim] |
| Plugin rules dağıtamaz | Doğru | README: "Claude Code plugins cannot distribute `rules`" [kaynak diyor] |
| Bu oturumda synced plugin klasörü boş | Doğru | `ls` [gözledim] |
| "ECC'nin bütün kalıcı depoları `$HOME` altında" | Fazla geniş | Bellek, oturum ve öğrenme depoları `$HOME`'da. İş ürünleri ise proje içinde: `.claude/plans`, `.claude/prds`, `.claude/PRPs/*`, `.claude/reviews`, `.claude/checkpoints.log`, `gan-harness/`, `.claude/hookify.*.local.md`, `.claude/ecc/install-state.json`, `.claude/campaigns/` [kaynak diyor: komutlar] |
| Kurucu hook önsözüne base64 mutlak yol gömer | Doğru | Kuru koşu: 24 hook komutunun hepsinde `Buffer.from('<b64>','base64')` var, düz yol yok [gözledim] |
| Komutların kök araması `plugins/synced`'i bilmez | Doğru, daha geniş | `resolve-ecc-root.js` ne `plugins/synced`'i ne proje `.claude`'u arar. Proje kurulumunda da `/sessions`, `/skill-health`, `/instinct-status` ve `/auto-update` `~/.claude`'a düşer [kaynak diyor: kod] |
| Read'de ≥4, Edit'te ≥8 Node süreci | Doğru | Kuru koşudaki matcher'lar [gözledim] |
| `/plan` inline, onay bekler, PRD'de `.claude/plans/` | Doğru | `commands/plan.md` [kaynak diyor] |
| `/orchestrate` shim'inde HANDOFF yok | Doğru | shim okundu [gözledim] |
| `/checkpoint` → `.claude/checkpoints.log` | Doğru, eksik | Ayrıca emekli `/verify quick`'e atıf yapıyor [gözledim] |
| Belge kayması (homunculus yolu, `/tdd`) | Doğru, daha yaygın | §9: COMMAND-AGENT-MAP, QUICK-REF, TROUBLESHOOTING, `spec-miner` |
| `contexts/` `--system-prompt` ile | Doğru | longform: `alias claude-dev='claude --system-prompt "$(cat ~/.claude/contexts/dev.md)"'` [kaynak diyor] |
| "Öneri: B, 10–15 bileşen; 68 ajanı alma; 292 skill'in tamamını alma" | Çürütülüyor (öncül eksik) | Platform tam kurulumu engellemiyor (§7). Maliyet ölçülebilir ve ayarlanabilir: açıklama 108 KB, profil ve hook bayrakları var. ECC'nin kendisi elle seçmeyi yalnız yerel desteği olmayan harness'ler için öneriyor ve kaybı sayıyor: "automatic install and sync", "native hook execution", "true command plumbing", "reliable skill discovery at runtime"; kural: "use native ECC targets whenever you want the full system" [kaynak diyor: `docs/MANUAL-ADAPTATION-GUIDE.md`]. Seçme kararı, bütün kurulup ölçüldükten sonra verilmeli (O-16) |
| "ECC2 alma" | Doğru | README: "It is usable as an alpha for local experimentation, but it is **not** the finished ECC 2.0 product yet." [kaynak diyor] |

## 3. Ajan kataloğu (68)

**Biçim:**
- `agents/<ad>.md`; YAML alanları `name`, `description`, `tools` (virgüllü skaler), `model`, isteğe bağlı `color`.
- PLUGIN_SCHEMA_NOTES: "Omitting the `tools` field grants the agent access to all tools, but ECC agents declare explicit allowlists".
- Hiçbir ajanda Task/Agent aracı yok [gözledim]. Yani ajanlar alt ajan açamaz; bulutun derinlik 1 sınırıyla çelişmez.
- Ortak iskelet: "Your Role" → iş akışı → çıktı biçimi → onay ölçütü → ilgili skill.

**Kısaltmalar:** R=Read, W=Write, E=Edit, B=Bash, G=Grep, Gl=Glob.

**Çekirdek iş akışı**

| Ajan | Model | Araçlar | Ne yapar |
|---|---|---|---|
| planner | opus | R,G,Gl | Uygulama planı: Overview / Requirements / Architecture Changes / fazlı adımlar (File / Action / Why / Dependencies / Risk) / Testing / Risks / Success Criteria; "Each phase should be mergeable independently." |
| architect | opus | R,G,Gl | Mimari; her kararda Pros/Cons/Alternatives/Decision; ADR şablonu; kontrol listesi. |
| code-architect | sonnet | R,G,Gl,B | Mevcut kalıplardan özellik planı: Files to Create/Modify, Data Flow, Build Sequence. |
| code-explorer | sonnet | R,G,Gl | Giriş noktasından yürütme yolunu izler: Entry Points / Execution Flow / Key Files. |
| tdd-guide | sonnet | R,W,E,B,G | RED→GREEN→REFACTOR, %80; "v1.8 Eval-Driven TDD Addendum": pass@1/pass@3, sürüm-kritikte pass^3. |
| code-reviewer | sonnet | R,G,Gl,B | >%80 güven; Pre-Report Gate; HIGH/CRITICAL için satır + senaryo + neden yakalanmadığı; "It Is Acceptable And Expected To Return Zero Findings"; Approve/Warning/Block. |
| security-reviewer | sonnet | R,G,Gl,B | OWASP 10, `npm audit`, desen tablosu, acil durum adımları. |
| build-error-resolver | sonnet | R,W,E,B,G,Gl | Yalnız derleme hatası; dosyanın <%5'i kadar değişiklik; "When NOT to Use" yönlendirmesi. |
| e2e-runner | sonnet | R,W,E,B,G,Gl | Önce agent-browser, yedek Playwright; flaky testi karantinaya alır. |
| refactor-cleaner | sonnet | R,W,E,B,G,Gl | knip/depcheck/ts-prune; SAFE/CAREFUL/RISKY; her partide test ve commit. |
| doc-updater | haiku | R,W,E,B,G,Gl | `docs/CODEMAPS/*`; README ve rehberleri koddan günceller. |
| docs-lookup | haiku | R,G,`mcp__context7__*` | Context7'den güncel API belgesi; en çok 3 çağrı. |
| code-simplifier | sonnet | R,W,E,B,G,Gl | Davranışı birebir koruyarak sadeleştirir. |
| comment-analyzer | haiku | R,G,Gl | Yorum çürümesi: Inaccurate / Stale / Incomplete / Low-value. |
| pr-test-analyzer | sonnet | R,G,Gl,B | PR testleri değişen davranışı kapsıyor mu. |
| silent-failure-hunter | sonnet | R,G,Gl,B | Boş catch, tehlikeli fallback, kaybolan hata. |
| type-design-analyzer | sonnet | R,G,Gl | Tiplerin geçersiz durumları engelleyip engellemediği. |
| conversation-analyzer | haiku | R,G | `/hookify` için transcript'teki düzeltmelerden hook kuralı önerir (yaml). |
| spec-miner | opus | R,G,Gl,B,W | Brownfield koddan `openspec/specs/<cap>/spec.md`; Requirement/Invariant blokları; "sample and expand" (en çok 15 dosya). |
| performance-optimizer | sonnet | R,W,E,B,G,Gl | Bundle, Web Vitals, bellek sızıntısı, algoritma. |
| database-reviewer | sonnet | R,G,Gl,B | PostgreSQL/Supabase: index, RLS, EXPLAIN. |

**Orkestrasyon ve meta**

| Ajan | Model | Araçlar | Ne yapar |
|---|---|---|---|
| loop-operator | sonnet | R,G,Gl,B,E | Döngüyü güvenli yürütür, durmayı saptar, eskale eder (§5.2). |
| harness-optimizer | sonnet | R,G,Gl,B,E | Harness yapılandırmasını eval ile iyileştirir; güvenlik değişikliği insan onayına kadar BLOCKED (§5.6). |
| agent-evaluator | sonnet | R,G,Gl,B | Çıktıya 5 eksenli karne; kanıtsız 5 puan yok (§5.7). |
| chief-of-staff | sonnet | R,G,Gl,B,E,W | E-posta/Slack/LINE/Messenger triyajı; gönderim sonrası kontrol listesini hook ile zorlar (§5.8). |
| gan-planner | sonnet | R,W,G,Gl | Tek satırlık istekten `gan-harness/spec.md` ve `eval-rubric.md` yazar. |
| gan-generator | sonnet | R,W,E,B,G,Gl | Spec ve feedback'e göre kurar; "iteration-NNN" commit'i; `generator-state.md`. |
| gan-evaluator | sonnet | R,W,B,G,Gl,`mcp__playwright__*` | Canlı uygulamayı test eder; 4 ölçüt ağırlıklı; eşik 7.0; `feedback-NNN.md`. |

**Açık kaynak hattı**

| Ajan | Model | Ne yapar |
|---|---|---|
| opensource-forker | haiku | Kopyalar; sırları `.env.example`'a taşır; tek commit; `FORK_REPORT.md`. |
| opensource-sanitizer | sonnet | "never trust the forker's work"; salt okuma; PASS/FAIL raporu. |
| opensource-packager | haiku | CLAUDE.md (<100 satır), `setup.sh`, README, LICENSE, CONTRIBUTING. |

**Alan uzmanları** (araçlar parantezde)
- a11y-architect — sonnet (R,W,E,G,Gl); WCAG 2.2, ADR-ACC şablonu.
- marketing-agent — sonnet (R,G,Gl,WebSearch,WebFetch); kampanya ve metin.
- seo-specialist — sonnet (aynı araçlar); teknik SEO.
- healthcare-reviewer — opus (R,G,Gl); CDSS ve PHI.
- mle-reviewer — sonnet (R,G,Gl,B); üretim ML; diğer inceleme şeritlerine yönlendirir.
- rag-pipeline-reviewer — sonnet (R,G,Gl,B); reranking, RAGAS eşikleri.
- network-architect, network-config-reviewer — sonnet (R,G).
- network-troubleshooter — sonnet (R,B,G).
- homelab-architect — sonnet (R,G).

**Dil inceleyicileri** (16 ajan, hepsi sonnet, R,G,Gl,B; "report findings only")
- Ajanlar: typescript-reviewer, python-reviewer, go-reviewer, cpp-reviewer, csharp-reviewer, fsharp-reviewer, rust-reviewer, php-reviewer, swift-reviewer, kotlin-reviewer, java-reviewer (Spring ya da Quarkus'u algılar), django-reviewer, fastapi-reviewer, flutter-reviewer, react-reviewer, vue-reviewer.
- Ortak kalıp: dile göre `git diff` → statik araç → CRITICAL/HIGH/MEDIUM → Approve/Warning/Block.
- react-reviewer ve vue-reviewer typescript-reviewer ile şerit tablosu paylaşır: "For a JSX/TSX PR, invoke both agents."

**Derleme çözücüler** (11 ajan, hepsi sonnet, R,W,E,B,G,Gl)
- Ajanlar: go-, cpp-, rust-, kotlin-, java-, dart-, django-, pytorch-, react- ve swift-build-resolver; bir de harmonyos-app-resolver (ArkTS/ArkUI V2 zorunlu).
- Ortak kural: "Same error persists after 3 fix attempts" → dur ve raporla.

**Gözlemler**
- Ajan içi yönlendirmeler yalnız öneri. Örnekler: kotlin/java/flutter-reviewer "stop and hand off to `security-reviewer`"; mle-reviewer "Use `python-reviewer` ...". Ajan başka ajan açamaz; bunları ana oturum yürütür [çıkarım: araç listeleri].
- `spec-miner` bir bütünleşme vaat ediyor: "`planner` will add `## ADDED Requirements` blocks; `tdd-guide` will read `#### Scenario:` blocks …; `code-reviewer` will grep `<!-- enforced: -->`". Oysa bu üç ajanda "openspec" hiç geçmiyor [gözledim: grep]. Vaat edilen bütünleşme kodda yok.
- `docs-lookup` araç adı `mcp__context7__…` (küçük c). Bu buluttaki Context7 araçları `mcp__Context7__…` adını taşıyor. İzin listesi eşleşmezse ajan aracı alamaz [çıkarım].

## 4. Komut kataloğu (94 + 12 emekli shim)

**Biçim:**
- `commands/<ad>.md`; frontmatter'da `description`, bazen `argument-hint`, `allowed-tools`, `disable-model-invocation`.
- Gövde bir prompt; `$ARGUMENTS` içerir.
- AGENTS.md: "`commands/` is a legacy slash-entry compatibility surface".
- Plugin kurulumunda ad `/ecc:plan`, elle kurulumda `/plan` [kaynak diyor: README].

**Planlama ve gereksinim**
- `/plan` — Inline çalışır: "Do not call the Task tool or any subagent by default". PRD verilirse `.claude/plans/{name}.plan.md` yazar, PRD satırını `pending→in-progress` yapar. Pattern Grounding tablosu var: "Do not invent a pattern". Onay bekler.
- `/plan-prd` — Yalın PRD `.claude/prds/{name}.prd.md`; Delivery Milestones tablosu; 4 kapılı soru turu. Kural: "Never invent plausible-sounding requirements."
- `/prp-prd` — Etkileşimli PRD `.claude/PRPs/prds/`; Implementation Phases tablosu (Status/Parallel/Depends).
- `/prp-plan` — Tek geçişte uygulanabilir plan `.claude/PRPs/plans/`; "No Prior Knowledge Test"; PRD fazını `in-progress` yapar.
- `/prp-implement` — Her dosya değişikliğinden sonra typecheck; 5 doğrulama seviyesi; rapor `.claude/PRPs/reports/`, "Assessment vs Reality" bölümüyle; plan `completed/`'a taşınır.
- `/plan-canvas` — Planı yerel tarayıcı tuvalinde işaretleyip onaylatır (`ecc-plan-canvas`).
- `/feature-dev` — 7 fazlı akış: code-explorer → sorular → code-architect → onay → uygulama → code-reviewer.
- `/model-route` — haiku/sonnet/opus önerisi.
- `/jira` — Bilet okur, yorum yazar, durum geçişi yapar (MCP ya da REST).

**Orkestrasyon**
- `/orch-add-feature`, `/orch-fix-defect`, `/orch-change-feature`, `/orch-refine-code`, `/orch-build-mvp` — `orch-*` skill'lerinin sarmalayıcıları. Kapılar: GATE 1 plan onayı, GATE 2 commit onayı (§5.5).
- `/orch-review` — Workflow aracıyla `workflows/orch-review.workflow.js` çalıştırır; fail-closed (§5.5).
- `/gan-build` — Planner/generator/evaluator döngüsü (Task aracıyla); `/gan-design` — tasarım döngüsü (§5.3).
- `/santa-loop` — İki bağımsız gözden geçiren; ikisi PASS verirse push (§5.4).
- `/loop-start` — Yalnız talimat: desen `sequential|continuous-pr|rfc-dag|infinite`, `--mode safe|fast`, runbook `.claude/plans/`'a yazılır.
- `/loop-status` — `ecc loop-status` CLI'si `~/.claude/projects/**` transcript'lerinde bayat `ScheduleWakeup` ve cevapsız `Bash` arar.
- `/multi-plan`, `/multi-execute`, `/multi-workflow`, `/multi-backend`, `/multi-frontend` — Dış `ccg-workflow` çalışma zamanı ister (`~/.claude/bin/codeagent-wrapper`, Codex/Antigravity/Gemini). Kural: "External models have **zero filesystem write access**". Buluta uygun değil.
- `/epic-claim`, `/epic-decompose`, `/epic-validate`, `/epic-sync`, `/epic-review`, `/epic-publish`, `/epic-unblock` — `node scripts/github-coordination.js <eylem>`; GitHub issue koordinasyon bloğu, etiketler, SQLite önbellek, denetim yorumu.

**İnceleme ve doğrulama**
- `/code-review` — Yerel ya da PR modu; `.claude/reviews/pr-N-review.md`; `gh pr review` ile yayınlar. Karar tablosu: APPROVE / REQUEST CHANGES / BLOCK.
- `/review-pr` — 6 ajan: code-reviewer, comment-analyzer, pr-test-analyzer, silent-failure-hunter, type-design-analyzer, code-simplifier. Güven ≥80.
- `/quality-gate` — Tek dosya için formatter kapısı (`scripts/hooks/quality-gate.js`, hook girdisiyle çalışır).
- `/checkpoint` — `.claude/checkpoints.log` dosyasına `tarih | ad | sha` yazar; emekli `/verify quick`'e atıf yapıyor.
- `/test-coverage` — %80'e kadar eksik test üretir.
- `/security-scan` — `npx ecc-agentshield scan`. Frontmatter'daki `agent:` ve `subtask:` alanları Claude Code alanı değil [çıkarım].
- `/harness-audit` — `node scripts/harness-audit.js`; 12 kategori; "Do not invent additional dimensions".
- `/build-fix` — Hataları tek tek düzeltir, inline; delege etmiyor.
- `/refactor-clean` — Ölü kod: SAFE/CAUTION/DANGER; her silmede test.

**Oturum, bellek, öğrenme**
- `/save-session`, `/resume-session` (§5.13).
- `/sessions` — `node -e` + `scripts/lib/session-manager`; takma adlar `~/.claude/session-aliases.json`'da.
- `/aside` — Görevi bozmadan yan soru yanıtlar.
- `/learn` — `~/.claude/skills/<ad>/SKILL.md` yazar; guarded-write; description'ın "Use when" ile başladığını doğrular.
- `/learn-eval` — Örtüşme grep'i, sonra Save / Improve / Absorb / Drop kararı; Global mi Project mi (`.claude/skills`).
- `/instinct-status`, `/instinct-import`, `/instinct-export`, `/evolve`, `/promote`, `/prune`, `/projects` — `python3 …/continuous-learning-v2/scripts/instinct-cli.py`.
- `/skill-create` — git geçmişinden SKILL.md (ve instinct) üretir.
- `/skill-health` — `scripts/skills-health.js` paneli.
- `/cost-report` — `~/.claude/metrics/costs.jsonl` dosyasından maliyet özeti.

**Kurulum ve araç**
- `/project-init` — Yığını algılar, kuru kurulum planı çıkarır. Kural: "Use ECC's installer and manifest tooling. Do not hand-copy files".
- `/ecc-guide` — ECC yüzeyinde gezinme rehberi.
- `/auto-update` — install-state'ten yeniden kurar; `/setup-pm` — paket yöneticisi seçimi. İkisinde de `disable-model-invocation`.
- `/pm2` — Windows odaklı PM2 komutları; CLAUDE.md'ye ekleme yapar.
- `/hookify`, `/hookify-list`, `/hookify-configure`, `/hookify-help` — `.claude/hookify.{ad}.local.md` kural dosyası yazar (§5.14).
- `/update-codemaps` — `docs/CODEMAPS/`; >%30 fark varsa onay ister.
- `/update-docs` — `<!-- AUTO-GENERATED -->` işaretli bölümler; RUNBOOK.
- `/marketing-campaign` — Kampanya içeriği `.claude/campaigns/`'a.
- `/pr`, `/prp-pr` — `gh pr create`. `/prp-commit` — doğal dille hedeflenen commit.

**Dil komutları (22)**
- Liste: `/go-review|test|build`, `/cpp-review|test|build`, `/rust-review|test|build`, `/kotlin-review|test|build`, `/gradle-build`, `/flutter-review|test|build`, `/react-review|test|build`, `/python-review`, `/fastapi-review`, `/vue-review`.
- Hepsi ilgili ajanı anlatır; örnek oturum ve onay tablosu içerir.

**Emekli shim'ler** (`legacy-command-shims/commands`, varsayılan kurulmaz)
- `/tdd`, `/e2e`, `/eval`, `/verify`, `/orchestrate`, `/docs`, `/context-budget`, `/devfleet`, `/claw`, `/agent-sort`, `/prompt-optimize`, `/rules-distill`.
- Her biri ilgili skill'e yönlendirir.
- `/orchestrate` shim'inde HANDOFF biçimi ve `custom` modu yok.

## 5. Orkestrasyon mekanizmaları

### 5.1 Plan üreticileri: planner, architect, code-architect, /plan, /prp-plan

- **Sorun:** Kod yazılmadan önce doğrulanabilir bir iş dökümü gerekiyor.
- **Nasıl işler:**
  - `planner` salt okuma araçlarıyla çalışır.
  - Kırmızı bayrakları: "Plans with no testing strategy", "Steps without clear file paths", "Phases that cannot be delivered independently".
  - `/plan` ajanı çağırmaz; gerekçesi: "This keeps `/plan` usable from plugin installs that ship commands without agent files". Ajan yoksa: "continue planning inline instead of surfacing an "Agent type 'planner' not found" error".
  - `/prp-plan` en katı biçim: her görev ACTION / IMPLEMENT / MIRROR / IMPORTS / GOTCHA / VALIDATE alanlarını taşır. Kural: "A developer unfamiliar with this codebase should be able to implement the feature using ONLY this plan".
- **Yollar:** `agents/planner.md`, `agents/architect.md`, `commands/plan.md`, `commands/prp-plan.md`, `commands/plan-prd.md`.
- **Kanıt:** Etkinlik ölçümü yok. Yalnız biçim var [kaynak diyor].
- **DevOS:** Al.
  - `/prp-plan`'ın görev şeması ve "No Prior Knowledge Test" DevOS'un soğuk-başlatma iş kaydı için doğrudan uygun.
  - Onay kapısını doğrulayıcı ajana çevir.
  - PRD durum sütunu (`pending/in-progress/complete`) iş kaydının durum alanı olsun.
  - Yeni işe geçmeden önce yarım kalmış `in-progress` işi uzlaştırma kuralı ekle (O5, study N39).

### 5.2 Döngü operatörü: loop-operator, /loop-start, /loop-status

- **Sorun:** Özerk döngü ilerlemeden dönebilir, maliyet kayabilir.
- **Nasıl işler (loop-operator):**
  - "Required Checks: quality gates are active / eval baseline exists / rollback path exists / branch/worktree isolation is configured".
  - "Escalate when any condition is true: no progress across two consecutive checkpoints / repeated failures with identical stack traces / cost drift outside budget window / merge conflicts blocking queue advancement".
- **Nasıl işler (`/loop-start`):** Yalnız akış tarifi (depo durumu → desen → hook profili → `.claude/plans/` runbook). Arkasında betik yok [gözledim]. Kısa başvuru belgesi farklı bir şey anlatıyor: "Start a recurring agent loop on an interval" [kaynak diyor: `COMMANDS-QUICK-REF.md`].
- **Nasıl işler (`/loop-status`):** CLI transcript JSONL'lerini tarar; bayat `ScheduleWakeup` ya da `tool_result`'u olmayan `Bash` bulursa `--exit-code 2` ile çıkar. `--write-dir` başka süreçler için anlık görüntü yazar.
- **Bulut:** Transcript'ler `/root/.claude/projects/-home-user-<repo>/` altında [gözledim]. Salt okuma bir izleme aracı olarak çalışabilir. Ancak `npx ecc-universal` ağdan paket ister [bilinmiyor: proxy].
- **DevOS:** Uyarlayarak al.
  - Dört ön koşul ve dört eskalasyon koşulu DevOS döngü sözleşmesine birebir girsin.
  - "İki checkpoint ilerlemesiz" kuralı ölçülebilir olsun: checkpoint = iş kaydındaki doğrulanmış durum değişikliği.
  - `loop-status` fikri, ana oturumun takılı alt işleri bulmasına uyarlansın.

### 5.3 GAN üçlüsü: gan-planner / gan-generator / gan-evaluator, /gan-build, /gan-design

- **Sorun:** Üretici kendi işini cömert değerlendirir.
- **Nasıl işler:**
  - Dosya sözleşmesi: `gan-harness/spec.md`, `eval-rubric.md`, `generator-state.md`, `feedback/feedback-NNN.md`, `build-report.md`.
  - Üretici: "Don't self-evaluate — Your job is to build, not to judge." Her tur "iteration-NNN" commit'i atar.
  - Değerlendirici: "**Your natural tendency is to be generous.** Fight it." Ayrıca: "The requested mode is not proof that its tools were available". Gerçekte elde edilen modu (`playwright|screenshot|code-only`) yazmak zorunlu.
  - Puan: `weighted = (design * 0.3) + (originality * 0.2) + (craft * 0.3) + (functionality * 0.2)`; geçme eşiği 7.0.
  - `/gan-build` döngüsü: en çok 15 tur. Kural: "if iteration >= 3 and score has not improved in last 2 iterations: … PLATEAU detected — stopping early".
  - `/gan-design`: en çok 10 tur, eşik 7.5, ağırlıklar .35 / .30 / .25 / .10.
- **Bulut:** Ajanlar ana oturumdan Task ile açılır; derinlik 1'e uyar. `mcp__playwright__*` bu ortamda yok, değerlendirici `code-only` moduna düşer ve bunu yazmak zorunda. Uzun süren dev server VM ömrüne bağlı [çıkarım].
- **DevOS:** Uyarlayarak al: yazar ≠ değerlendirici, dosya ile devir, plato durdurma, "gerçek modu yaz" dürüstlük kuralı. Web tasarımına özgü rubriği alma; SOUL'un kabul ölçütlerine çevir.

### 5.4 Çift bağımsız inceleme: /santa-loop

- **Sorun:** Tek gözden geçiren kör noktası olan bir onay verebilir.
- **Nasıl işler:**
  - Her ölçütün nesnel PASS/FAIL koşulu olan bir rubrik kurulur.
  - Reviewer A: Agent aracı, `subagent_type: code-reviewer`, `model: opus`. Talimat: "You are an independent quality reviewer. You have NOT seen any other review".
  - Reviewer B önce `codex exec --sandbox read-only` ya da `gemini` dener. İkisi de yoksa ikinci bir Claude açılır: "Log a warning that both reviewers share the same model family".
  - İkisi PASS → `git push -u origin HEAD`. Değilse yalnız işaretlenen düzeltilir, tur başına bir commit atılır, "fresh reviewers" ile en çok 3 tur yapılır, sonra insana döner.
- **Bulut:** codex ve gemini yok [gözledim]; model çeşitliliği kaybolur, bağlam yalıtımı kalır. Plugin kurulumunda ajan adı `ecc:code-reviewer` olabilir; `code-reviewer` çözülmeyebilir [çıkarım].
- **DevOS:** Al: taze iki gözden geçiren, JSON karar, tur sınırı. Kapanışı Batu'ya değil, doğrulayıcı kurala bağla.

### 5.5 Kapılı hat ve fail-closed inceleme: orch-* ve /orch-review

- **Nasıl işler (`orch-*` sarmalayıcıları):**
  - Hepsi aynı cümleyle biter: "Honor both gates — do not write implementation before Gate 1, do not commit before Gate 2."
  - Fark tanımları: `/orch-fix-defect`: "Proving the bug first is what makes this a fix, not a tweak." `/orch-change-feature`: "Changing the tests first is what makes this a tweak, not a fix."
  - `/orch-refine-code`: dokunmadan önce testler yeşil olmalı; kapsama zayıfsa önce karakterizasyon testi yazılır.
- **Nasıl işler (`/orch-review`, `workflows/orch-review.workflow.js`):**
  - Boyutlar: her zaman `ecc:code-reviewer`; dil verilmişse `ecc:<dil>-reviewer`; `SECURITY_TRIGGER` regex'i eşleşirse `ecc:security-reviewer`.
  - Çıktı şeması HIGH/CRITICAL için `proof` alanını zorunlu kılar (`allOf: if severity ∈ {CRITICAL,HIGH} then required proof`).
  - Tekilleştirme anahtarı `file::normalize(evidence)`.
  - Doğrulayıcı: "Set isReal=false ONLY if you can affirmatively demonstrate … report a high `confidence` (>= 0.8)… Uncertainty must never clear a blocker."
  - Sonuç: `verdict: blocking.length > 0 || incomplete ? 'CHANGES_REQUESTED' : 'APPROVE'`.
  - README: "native workflows run autonomously in the background and cannot pause for interactive approval". Bu yüzden kapılar ana konuşmada kalır.
- **Kanıt:** README'ye göre yerel denemede "11 raw findings collapsed to 4 unique" [kaynak diyor]. Ben koşmadım.
- **Bozulanlar:**
  - Ajan adları `ecc:` önekli; proje kurulumunda ajanlar öneksiz. Boyut çöker, sonuç fail-closed olarak `CHANGES_REQUESTED` çıkar [çıkarım: kod].
  - Betik hiçbir kurulum modülünde yok. README: "Not in this PR (follow-ups): … Installer / manifest wiring so the script ships to `~/.claude/` on install" [kaynak diyor].
  - Workflow aracının bulutta olup olmadığı O11'in konusu [bilinmiyor].
- **DevOS:** Uyarlayarak al. DevOS'un bağımsız doğrulayıcısının iskeleti olsun: şema zorunlu kanıt, tekilleştirme, düşmanca doğrulama, eksik boyutta asla onay yok. Ajan adlarını DevOS rollerine bağla; betiği repoya koy.

### 5.6 Harness iyileştirici: harness-optimizer, /harness-audit

- **Nasıl işler (harness-optimizer):**
  - Sınır: "Do NOT rewrite application/product code".
  - Temel ölçüm: `node scripts/harness-audit.js repo --format json`.
  - Değişmeden önce anlık görüntü alır; başarısızlıkta geri yükler: "never hand back a partially-applied change".
  - Yetenek evalleri üç denemeyle pass@3; güvenlik-kritik regresyon pass^3.
  - İnsan kapısı: "a security-sensitive diff may never report SHIP IT; it stays BLOCKED until human approval is recorded".
- **Nasıl işler (`/harness-audit`):** Rubrik sürümü `2026-05-19`; 12 kategori; "Scores are derived from explicit file/rule checks". Puan yapılandırmanın varlığını ölçer, sonucu ölçmez (O5, CORE §7.2).
- **Bulut:** `scripts/harness-audit.js` yalnız `commands-core` modülüyle `.claude/scripts/`'e kopyalanır. Komut ise göreli `scripts/harness-audit.js` çağırır: proje kökünde bu yol yok. Yol yamalanmalı [çıkarım: manifest + komut].
- **DevOS:** Uyarlayarak al: kendini iyileştirmenin sınırları (yalnız harness yüzeyi, anlık görüntü ve geri alma, pass^k, güvenlik değişikliğinde bağımsız onay). Puanı "varlık" diye etiketle.

### 5.7 Çıktı değerlendirici: agent-evaluator

- **Nasıl işler:**
  - Eksenler: Accuracy / Completeness / Clarity / Actionability / Conciseness.
  - Kanıt kuralları: "Every score below 5 MUST cite specific evidence from the output". "DO NOT assign score 5 without citing evidence of correctness". "DO NOT re-perform the original task".
  - Bash yalnız salt okuma; izin listesi ve yasak listesi yazılı.
  - Rapor biçimi `skills/agent-self-evaluation/scripts/evaluate.py` çıktısıyla aynı.
- **Kusur:** Prompt Defense Baseline bu ajanda yok [gözledim].
- **DevOS:** Al: teslim kabulünden önce bağımsız karne. VERDICT'i doğrulayıcı kararına bağla.

### 5.8 Kalıcı iş akışı örneği: chief-of-staff

- **Nasıl işler:**
  - İletişim triyajı: 4 kademe, sırayla: skip → info_only → meeting_info → action_required.
  - Gönderim sonrası 7 adım: takvim, ilişki notu, todo, bekleyen yanıtlar, arşiv, triyaj dosyaları, "Git commit & push".
  - Zorlama: "enforced by a `PostToolUse` hook that blocks completion until all steps are done".
  - İlkeler: "Hooks over prompts for reliability: LLMs forget instructions ~20% of the time"; "Knowledge files are memory: `relationships.md`, `preferences.md`, `todo.md` persist across stateless sessions via git".
- **Kanıt:** Hook dosyası ECC'de yok; ajan onu varsayıyor. %20 rakamının kaynağı yok [kaynak diyor / kanıtsız].
- **DevOS:** İlkeyi al: bellek = git'teki bilgi dosyaları; kontrol listesi hook ile zorlanır. İletişim işlevini alma.

### 5.9 Dil inceleme ve derleme çiftleri, /review-pr, /feature-dev

- Ortak sözleşme: inceleyici yalnız bulgu yazar; çözücü minimum düzeltme yapar ve 3 denemede durur.
- `/review-pr` altı dar ajanı paralel koşar; bulguları tekilleştirip önem sırasına dizer. `orch-review`'dan farkı: doğrulayıcı yok, fail-closed yok.
- **DevOS:** Uyarlayarak al: dar ve tek konulu inceleyiciler + tekilleştirme; doğrulama katmanını `orch-review`'dan al.

### 5.10 İş kaydı zinciri: /plan-prd → /plan ya da /prp-plan → /prp-implement → /pr

- **Sorun:** Plan sohbette kaybolur.
- **Nasıl işler:**
  - PRD tablosu: `| # | Milestone | Outcome | Status | Plan |`, durumlar `pending | in-progress | complete`.
  - `/prp-implement` her dosya değişikliğinde typecheck yapar. Kural: "If a validation fails, fix it before moving on. Never accumulate broken state."
  - Sonunda rapor yazılır, PRD fazı `complete` olur, plan `completed/`'a arşivlenir.
  - `/pr` bu dosyaları PR gövdesine bağlar.
- **Bulut:** Hepsi repo içinde; commit'lenirse bulutta kalıcı [çıkarım]. `gh` yok: `/pr` durur ("GitHub CLI (`gh`) is required"). GitHub MCP ile yeniden yazılmalı.
- **DevOS:** Al: iş kaydının dosya biçimi ve durum geçişleri. "Assessment vs Reality" tablosu tahmin doğruluğunu ölçmek için kullanılsın.

### 5.11 GitHub koordinasyonu ve ECC2: /epic-*, `ecc work-items`, `ecc2`

- **Nasıl işler (`/epic-*`):**
  - Issue gövdesi kanonik durumdur. Adımlar: "Reads issue bodies as the canonical epic state", "Reconciles the coordination block with labels", "Checks each blocked epic's dependency list. Moves fully unblocked epics to ready".
  - Her eylem bir denetim yorumu bırakır; yerel SQLite önbellek tutulur.
- **`ecc work-items`:** "Track linked Linear, GitHub, handoff, and manual work items" [kaynak diyor: `ecc.js`]. Betik okunmadı (§1.3).
- **ECC2:** Rust, 17 dosya, 54.5 bin satır. CLI'da `Delegate`, `Assign`, `AutoDispatch`, `CoordinateBacklog`, `MergeQueue`, `LogDecision`, `Decisions`, `Graph`, `Schedule`, `Daemon` gibi alt komutlar var. Buna karşın README eksikleri sayıyor: "richer multi-agent orchestration", "explicit agent-to-agent delegation and summaries". Yani iskelet alfa [kaynak diyor].
- **DevOS:** Epic modelini uyarlayarak al (issue ya da repo dosyası kanonik, bağımlılık açma, denetim izi) ve GitHub MCP ile uygula. ECC2'yi alma: uzun yaşayan daemon ve tmux, VM ömrüyle çelişir.

### 5.12 Çok modelli komutlar: multi-*

- **Nasıl işler:** Claude orkestratör ve tek yazar ("Code Sovereignty"). Dış modellerin diff'i "dirty prototype" sayılır. Oturum kimlikleri `resume <SESSION_ID>` ile devam ettirilir.
- **Bulut:** `codeagent-wrapper`, Codex ve Antigravity yok → çalışmaz [gözledim: araçlar yok]. Komut adları iç tutarsız: dosya `multi-plan`, metin `/ccg:plan`, `/workflow`, `/backend`.
- **DevOS:** Alma. "Tek yazar, diğerleri öneri üretir" ilkesini not et.

### 5.13 Oturum devri: /save-session, /resume-session, /sessions, /aside, /checkpoint

- O5'in M3 anlatımı doğru. Ek ayrıntılar:
  - Aday sıralaması 5 kurallı ve deterministik (en son eşitlikte sözlük sırası).
  - Açık yol verilirse sıralama yapılmaz: "Do not apply candidate ranking or substitute a different file".
  - Brifing biçimi sabit; "WHAT NOT TO RETRY" her zaman gösterilir.
- **Bulut:** Depo `~/.claude/session-data/` → VM gidince kaybolur [çıkarım].
- **DevOS:** Şablonu ve sıralama kurallarını al. Depoyu repo içine taşı. "Otomatik başlama yok" kuralını "Exact Next Step netse devam et" ile değiştir (K-015).

### 5.14 Öğrenme ve kural üretimi: /learn-eval, /skill-create, /hookify

- **`/learn-eval`:** Örtüşme denetimi zorunlu: "Grep `~/.claude/skills/` and relevant project `.claude/skills/` … Check MEMORY.md". Karar Save / Improve then Save / Absorb into [X] / Drop. Kural: "never default uncertain content to Global persistence". Yazdıktan sonra keşfedilebilirliği doğrular.
- **`/skill-create`:** Önce geçici kardeş dosyaya yazar, doğrular, sonra atomik olarak değiştirir. Commit mesajları "untrusted" sayılır.
- **`/hookify`:** `.claude/hookify.{name}.local.md` yazar (`event: bash|file|stop|prompt|all`, `action: block|warn`, `pattern`). ECC içinde bu dosyaları okuyan hiçbir hook yok [gözledim: js/json/sh/py grep'i]. Kurallar dış bir motor olmadan etkisiz [çıkarım].
- **DevOS:** `/learn-eval` kapısını ve atomik yazmayı al; ders dosyası repo içinde olsun. `/hookify` biçimini alma; DevOS kendi hook'unu yazar.

## 6. Kurallar ve bağlamlar

- **Yükleme:**
  - `rules/common` (10 dosya, 18 KB) frontmatter taşımaz; her oturumda yüklenir [çıkarım: Claude Code kural davranışı, O11].
  - 111 dil dosyasının hepsi `paths:` taşır (örnek: `python/*.md` için `"**/*.py"`, `"**/*.pyi"`); yalnız eşleşen dosyada yüklenir [kaynak diyor: frontmatter].
  - Kurucu kuralları `.claude/rules/ecc/<dil>/` altına koyar. README uyarısı: "Copy entire directories — do NOT flatten".
- **`rules/common/agents.md`:**
  - Plugin varsayımı: "ECC agents ship with the `ecc@ecc` plugin, not in `~/.claude/agents/`. They are invoked through the Agent tool with a plugin-scoped `subagent_type`: `Agent(subagent_type: "ecc:planner", prompt: "...")`". Proje kurulumunda yanlış bilgi olur. Yamalanmalı.
  - "Delegation Completion Contract": "Applies to every agent at every depth (parent, child, grandchild)" + "Your final message IS the deliverable." Bulutta derinlik 1; torun yok.
- **`common/development-workflow.md`:** Adım 0: "GitHub code search first: Run `gh search repos` and `gh search code`". Bulutta `gh` yok; GitHub MCP araması ile değiştirilmeli.
- **`common/git-workflow.md`:** "ECC-managed installs set `"includeCoAuthoredBy": false`" [kaynak diyor]. Bulutun atıf kuralıyla çatışır.
- **`common/performance.md`:** "Avoid last 20% of context window for: Large-scale refactoring …". Bulutta otomatik sıkıştırma %80'de [gözledim: env]; bu eşik tam oraya denk geliyor.
- **`contexts/`:** Üç küçük mod dosyası (dev / research / review). `--system-prompt` ile kullanılıyor. Buluta uymaz [çıkarım]. İçerik tek satırlık rol kartına indirgenebilir; önemsiz.
- **DevOS:** `rules/common`'ı yama ile al: ajan adları, `gh` ve atıf satırları değişsin. DevOS'un kalıcı kuralları da aynı `paths:` mekanizmasıyla kapsamlı yazılsın.

## 7. ECC'yi bulutta proje dosyası olarak bütün halinde kurmak

### 7.1 Yollar

| Yol | Ne kurar | Bulut durumu |
|---|---|---|
| Plugin, `ecc setup` ya da `/plugin install ecc@ecc` (user / project / local kapsam) | skills, agents, commands, hooks; rules yok | `/plugin` bulutta kapalı. Hesap plugin'i "synced" olarak gelebilir, ama bu oturumda synced klasörü boş [gözledim]. Sürüm hesaptan kayar. `project` kapsamı repo'ya `enabledPlugins` yazar; bulutta marketplace kurmaz (002 README) [kaynak diyor] |
| Elle kurucu, `--target claude-project` | `.claude/` altına her şey + `.claude/settings.json` hook'ları + install-state | Çalışır (kuru koşu gözlendi); yamalar gerekir (§7.4) |
| Elle kopya, README "Manual component-by-component copying" | Seçilen klasörler | Hook'lar için README uyarıyor: "Do not copy the raw repo `hooks/hooks.json` … use the installer so hook command paths are rewritten correctly" |

### 7.2 Gözlenen kuru koşu (`--target claude-project --profile full`)

- **Seçilen modüller (27):** `full` profilinin tamamı; yalnız 10 çeviri modülü dışarıda. Atlanan ya da dışlanan modül yok.
- **İşlemler:** 1198 (1197 `copy-file` + 1 `update-claude-settings`); kaynak boyutu 8.05 MB.
- **Hedef dağılımı (`.claude/` altında):**

| Hedef | Dosya | Not |
|---|---|---|
| `skills/` | 584 | 292 dizin |
| `scripts/lib` | 162 | Kütüphanenin tamamı |
| `rules/ecc/` | 122 | |
| `commands/` | 94 | |
| `.agents/` | 89 | Claude okumaz; HOME kurulumunda hariç, proje kurulumunda değil |
| `agents/` | 68 | |
| `scripts/hooks` | 56 | |
| `hooks/` | 4 | README + `memory-persistence/` + `codex-hooks.json` |
| `.pi/` | 3 | Başka harness'e ait; Claude okumaz |
| Tekil dosyalar | — | `AGENTS.md` (Claude okumaz), `plugin.json`, `marketplace.json`, `README.md`, `PLUGIN_SCHEMA_NOTES.md`, `mcp-configs/mcp-servers.json`, `the-security-guide.md`, `scripts/{harness-audit,skills-health,auto-update,setup-package-manager,orchestrate-worktrees,orchestration-status,claw}.js`, `orchestrate-codex-worker.sh` |

- **Uyarı:** "Applying this plan requires an explicit hook decision: --enable-hooks or --no-hooks."
- **Hook olmadan uygulama:** Kurucu durur ve altı yetenek grubunu listeler: `automatic-source-writes`, `command-rewrite-and-process-control`, `transcript-derived-llm-egress`, `mcp-network-and-process-activity`, `automatic-permission-gates`, `session-observation-and-cost-records` [kaynak diyor: `hook-consent.js`].
- **`settings.json` hook'ları (24 kayıt):**
  - PreToolUse 9: bash dispatcher; powershell ve edit/write için gateguard; doc-file-warning; suggest-compact; observe (async); governance-capture; config-protection; mcp-health-check.
  - PreCompact 1; SessionStart 2 (session:start, plan-canvas-sessions).
  - PostToolUse 2: dispatcher sync 30 sn, async 45 sn.
  - PostToolUseFailure 2: mcp-health-check, skill:track.
  - Stop 7: plan-canvas-pending, format-typecheck (300 sn), check-console-log, session-end, evaluate-session, cost-tracker, desktop-notify.
  - SessionEnd 1.
- **Komut biçimi (kuru koşu çıktısından):** `node -e "…var e=Buffer.from('<base64: <proje>/.claude>','base64').toString('utf8');…const s=p.join(r,'scripts/hooks/plugin-hook-bootstrap.js');process.env.CLAUDE_PLUGIN_ROOT=r;…require(s)" …`. Yaşam döngüsü hook'ları dosya yoksa şunu yazıp atlar: `'[Hook] lifecycle bootstrap unavailable; skipping hook'` (yalnız stderr).
- **Yazmanın kalan etkileri:**
  - `includeCoAuthoredBy:false` yazılır.
  - `.claude/ecc/install-state.json` sha256 özetleriyle yazılır.
  - Kurulumdan sonra install-state-store-sync, `sql.js` ile `$HOME` altındaki bir SQLite'a projeksiyon yazar.
  - `node_modules` yoksa: dosyalar yazıldıktan sonra `require('sql.js')` hata verir, betik 1 ile çıkar [çıkarım: kod]. `install.sh` bunu önlemek için önce `npm install --ignore-scripts` çalıştırır.

### 7.3 Pinli kurulum reçetesi (önerilen; uygulanmadı)

1. ECC'yi sabit commit'te repo dışına getir: `git clone --depth 1` + `git checkout <sha>`, ya da scratch'te. `/home/user/affaan-m/ecc` `e482e57`'de hazır.
2. SOUL/DevOS repo kökünde `ecc-install.json` yaz:
   ```json
   {"version":1,"target":"claude-project","profile":"developer","exclude":[...],"options":{}}
   ```
   Şema `schemas/ecc-install-config.schema.json`; `ajv` ister.
3. Kurucuyu **repo kökünden** koş. Proje kökü `process.cwd()`; `--project-root` bayrağı yok [kaynak diyor: `install-apply.js:177`, grep]. Komut: `bash <ecc>/install.sh --config ecc-install.json --enable-hooks` (ya da önce `--no-hooks`). Önce `--dry-run --json` ile planı kaydet.
4. Yama katmanını ECC dosyalarının dışında tut (§7.6). Kaynak commit'ini ve install-state'i commit'le.
5. Doğrula:
   - `ecc doctor` bir ECC checkout'u ister (`repoRoot = ECC dizini`); repo kökünden koşulur.
   - Oturum başında "hook tetiklendi mi, modele ulaştı mı" duman testi.
   - `/context` ile katalog maliyeti ölç (O11).
6. Güncelleme: pinli SHA'yı değiştir, yeni checkout'tan kurucuyu aynı config ile yeniden koş, sonra yamaları yeniden uygula ve `doctor` koş. `/auto-update` kullanma (§7.6).

### 7.4 Bulutta ne bozulur, nasıl düzeltilir

| Bozulan | Neden (kanıt) | Düzeltme |
|---|---|---|
| Hook komutları mutlak yol taşıyor | base64 `<proje>/.claude` [gözledim] | Önsözü `var e=process.env.CLAUDE_PROJECT_DIR+'/.claude'` biçimine çeviren bir yama. `CLAUDE_PROJECT_DIR`'in hook ortamında olduğu Claude Code belgesine dayanıyor (O11) |
| `/sessions`, `/skill-health`, `/instinct-status`, `/auto-update` kök bulamıyor | `resolve-ecc-root.js` proje `.claude`'u aramıyor [kaynak diyor: kod] | Komutlarda `ECC_ROOT="$CLAUDE_PROJECT_DIR/.claude"`; ya da `CLAUDE_PLUGIN_ROOT`'u settings `env` ile vermek. Hook'ta `process.env.CLAUDE_PLUGIN_ROOT` önceliklidir |
| `/instinct-import`, `/evolve`, `/promote`, `/prune`, `/projects` | `${CLAUDE_PLUGIN_ROOT}` ya da `~/.claude/skills/...` [kaynak diyor] | Aynı yama; ya da bu komutları alma (öğrenme v2 bulutta zaten kapalı, O5) |
| `ecc:` ajan adları | AGENTS.md, `rules/common/agents.md`, `orch-review.workflow.js` [kaynak diyor]; proje ajanları öneksiz | Metin yaması: `ecc:` önekini kaldır (ya da DevOS rol adlarına eşle). Kurucu yalnız markdown bağlantılarını yeniden yazıyor, adları değil [kaynak diyor: `link-rewrite.js`] |
| `/orch-review` betiği yok | Hiçbir modülde `workflows/` yok [gözledim] | Betiği repoya kopyala; `agentType` adlarını yamala |
| `harness-audit`, `skills-health` yolları | Komut `node scripts/…` diyor, dosya `.claude/scripts/…`'te [çıkarım] | Komut yolunu yamala |
| Oturum özeti, instinct, metrikler `$HOME`'da | README'nin agent data home bölümü, komutlar [kaynak diyor] | Settings `env`: `ECC_AGENT_DATA_HOME` mutlak yol (`/home/user/<repo>/.devos/ecc-data`) ya da göreli yol (`.devos/ecc-data`; hook'un cwd'sine göre çözülür). ECC `~` ve mutlak yolu çözüyor, `$VAR` genişletmiyor [kaynak diyor: `agent-data-home.js`]. Proje config dosyası repo içini gösteremiyor: "agentDataHome must stay within the default Cursor or Claude data directories". `CLV2_HOMUNCULUS_DIR` için de aynı yöntem. Commit kuralını DevOS koyar; hook cwd'si O11'e göre doğrulanmalı [bilinmiyor] |
| `includeCoAuthoredBy:false` | `claude-commit-attribution.js` [kaynak diyor] | Kurulumdan önce `.claude/settings.json`'a açık `attribution` yaz; ECC açık tercihe dokunmuyor |
| `gh` gerektiren komutlar (`/pr`, `/code-review` PR modu, `/epic-*`, geliştirme akışı adım 0) | `gh` yok [gözledim] | GitHub MCP araçlarıyla yeniden yaz, ya da kurulum betiğiyle `gh`'yi kur ve kimlik doğrula [bilinmiyor: ağ ve kimlik] |
| `multi-*`, santa'nın dış gözden geçireni | codex, gemini ve ccg yok [gözledim] | Alma; santa için Claude yedeği yeterli |
| GateGuard ilk Edit/Bash'i reddediyor, `desktop-notify`, `observe` no-op | O5 ve O5d | Settings `env`: `ECC_HOOK_PROFILE=minimal` + `ECC_DISABLED_HOOKS="pre:edit-write:gateguard-fact-force,pre:powershell:gateguard-fact-force,stop:desktop-notify,pre:observe:continuous-learning"`. Profil için dosya yedeği de var: `.claude/ecc/setup.json` = `{"hooks":{"profile":"minimal"}}`. Hook önsözü `CLAUDE_PLUGIN_ROOT`'u `<proje>/.claude` yaptığı için `hook-flags.js` bu dosyayı okur [çıkarım: kod]. Bu dosyayı yazan ECC kodu yok [gözledim: grep]. `ECC_DISABLED_HOOKS`'un dosya yedeği yok |
| Hook yükü (Edit başına 8 süreç) | Kuru koşu [gözledim] | Profil + ölçüm; `post:dispatcher:async` ve `stop:format-typecheck` (300 sn) izlenmeli |
| Kurulum sonrası çıkış kodu 1 (`sql.js` yok) | Kod [çıkarım] | `install.sh` kullan (`npm install --ignore-scripts`); ya da `node_modules`'ü kurulum betiğinde hazırla |
| `.claude/.agents`, `.claude/.pi`, `.claude/AGENTS.md`, `plugin.json` gereksiz | Kuru koşu [gözledim] | Bırak (zararsız) ya da `--without` ile dışla; install-state bunları sahiplenir |
| Workflow aracı, Playwright MCP, Context7 adı | O11 [bilinmiyor] | Ajan araç listelerini buluttaki adlarla eşle (`mcp__Context7__…`) |
| Bulutun kendi Stop hook'ları (`stop-hook-git-check.sh`, `stop-hook-reply-gate.py`) | `/root/.claude` [gözledim] | ECC'nin 7 Stop hook'u bunlarla aynı olayda çalışır; etkileşim sınanmalı [bilinmiyor] |
| Yerinde yama `repair`'de geri alınır | `repair` sapan dosyayı kaynaktan yeniden yazar [kaynak diyor: `install-lifecycle.js`] | Yamayı ayrı dosyada tut ya da gölgelemeyi kullan (§7.6). Yerinde yama zorunluysa, her kurulum ve `repair`'den sonra yama betiği yeniden koşar |
| install-state mutlak yol taşıyor | Kuru koşu `statePreview`: `target.root` ve her `destinationPath` mutlak [gözledim] | Bulutta repo yolu sabit kalmalı. Başka yolda açılırsa state silinip temiz kurulum yapılır (§7.6) |
| `/auto-update` sürümü kaydırır | `git fetch --all --prune` + `git pull --ff-only`; ECC checkout'unu kayıttaki mutlak `sourcePath`'ten bulur [kaynak diyor: `auto-update.js` grep] | Kullanma; güncelleme pinli SHA ile (§7.3 adım 6) |

### 7.5 Bağlam maliyeti ve kontrol

- Skill, ajan ve komut açıklamaları 108 KB tutuyor [gözledim]. README: "The plugin advertises the installed catalog to the model; use a selective/manual profile when context footprint matters." Claude Code'un listeyi kısıp kısmadığı O11'in konusu.
- Kontrol düğmeleri:
  - Profil: `minimal` / `core` / `developer` / `full`.
  - Bileşen seçimi: `--with` / `--without`.
  - Hook profilleri ve kimlikle kapatma: `ECC_HOOK_PROFILE`, `ECC_DISABLED_HOOKS`.
  - SessionStart tavanı: `ECC_SESSION_START_MAX_CHARS` (varsayılan 8000).
  - SessionStart bağlamını kapatma: `ECC_SESSION_START_CONTEXT=off`.
  [kaynak diyor: README]
- `docs/token-optimization.md` önerisi: `MAX_THINKING_TOKENS=10000`, `CLAUDE_CODE_SUBAGENT_MODEL=haiku`. Aynı belgede bir topluluk notu: "`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` can only lower the compaction threshold" [kaynak diyor].

### 7.6 Yaşam döngüsü: defter, doctor, repair, uninstall, güncelleme

- **Defter:** `.claude/ecc/install-state.json`, şema `ecc.install.v1`.
  - Alanlar: `target{id,target,kind,root,installStatePath}`, `request{profile,modules,includeComponents,excludeComponents,legacyLanguages,legacyMode,hookConsent}`, `resolution{selectedModules,skippedModules}`, `source{repoVersion,repoCommit,manifestVersion}`, `operations[]` (`kind`, `moduleId`, `sourceRelativePath`, `destinationPath`, `strategy`, `ownership`, `scaffoldOnly`, `contentSha256`).
  - Doğrulayıcı bağımlılıksız yazılmış: "The installer closure must not require any non-builtin package (enterprise supply-chain vetting: the vetted bytes must be the installed bytes)" [kaynak diyor: `install-state.js`]. Buna karşın kurulum sonrası projeksiyon `sql.js`, config `ajv` istiyor (§7.2).
  - Kuru koşudaki kayıt: `repoVersion 2.2.2`, `repoCommit e482e579…`; stratejiler `preserve-relative-path` 1193, `sync-root-children` 4, `merge-hook-ids` 1 [gözledim].
- **Güven kökü:** "Install-state files are project-local and therefore attacker-controllable … every write/delete destination MUST be confined to the adapter-derived trusted root" [kaynak diyor: `path-safety.js`].
  - Kök `<cwd>/.claude`. Yazmalar `O_NOFOLLOW` ile yapılır; son bileşen symlink ise ret; yazma sırasında dosya kimliği değişirse ret.
  - Silme bir karantina dizini (`.ecc-remove-*`) üzerinden yapılır.
- **Sahiplik koruması:**
  - Hedefte dosya var ama defterde yoksa işlem atlanır: "Skipped user-owned file … the existing file is not recorded in ECC install-state" [kaynak diyor: `ownership-guard.js`].
  - Skill'de bütün dizin atlanır: "the flat skill directory is user-owned because it is not recorded in ECC install-state" [kaynak diyor: `claude-skill-migration.js`].
  - Defterdeki kök planla uyuşmazsa: "Refusing install: install-state target does not match the current plan".
- **doctor** [kaynak diyor: `install-lifecycle.js`]:
  - Hata kodları: `missing-target-root`, `unsafe-managed-destination`, `unsafe-repair-source`, `invalid-claude-settings`, `missing-managed-files`, `missing-source-files`, `resolution-unavailable`.
  - Uyarı kodları: `target-root-mismatch`, `install-state-path-mismatch`, `drifted-managed-files`, `unverified-managed-operations`, `manifest-version-mismatch`, `repo-version-mismatch`, `resolution-drift`.
  - Sapma ölçütü: kayıtlı sha256. Özet yoksa bayt eşitliği; markdown'da bağlantıları yeniden yazılmış içerik.
- **repair:**
  - Eksik ve sapmış dosyaları o an koşan ECC checkout'undan (`sourceRelativePath` ile) yeniden yazar.
  - `settings.json.ecc.lock` kilidini alır; defteri güncel sha256 ile yeniden yazar.
  - Defterde kopya dışı bir işlem varsa (hook kurulumunda `update-claude-settings` var) "recorded" modda çalışır: yalnız kayıtlı dosya listesini onarır; yeni sürümün yeni dosyalarını eklemez [çıkarım: kod, `createRepairPlanFromRecord`].
- **uninstall:** Yalnız özeti tutan dosyaları siler; değişmiş olanları korur: "Modified or unverifiable managed files were preserved together with install-state for review." Hook girdilerinden de yalnız değişmemiş olanları çıkarır.
- **Yeniden kurulum:**
  - Defter birikir: "Selective reinstalls retain earlier modules in the ledger" [kaynak diyor: `ownership-guard.js`]. Profil küçültmek dosya silmez; önce `uninstall` gerekir.
  - Yeni sürümde silinmiş bir kaynak dosya defterde kalırsa `doctor` `missing-source-files` verir ve `repair` durur [çıkarım: kod].
- **DevOS için anlamı:**
  - L1 yamaları ECC dosyalarının dışında durmalı: settings `env`, `.claude/ecc/setup.json`, DevOS'un kendi kuralları ve ajanları.
  - ECC metninde yerinde düzeltme şartsa (ör. `ecc:` adları) iki yol var. (a) Gölgeleme: kurulumdan önce aynı yola DevOS sürümü konur; kurucu dosyayı atlar, sahibi DevOS olur. Gölgelenen dosya ECC güncellemelerinden kopar; DevOS bunu kendi testiyle izler. (b) Yama betiği: her kurulum ve `repair`'den sonra koşar; `doctor`'un "drifted" listesi beklenen yama listesiyle karşılaştırılır.
  - Defteri commit'lemek bulutta yararlı, çünkü yol sabit. Yerel makinede yol farklıysa state silinip temiz kurulum yapılır.
  - Defter, güven kökü ve sahiplik koruması DevOS'un kendi dağıtımı için de alınacak desenler.

## 8. Ortak soru: DevOS ECC'nin üstüne kurulabilir mi?

**Kısa cevap:** Evet, koşullu. ECC bütün olarak ve sabit sürümle proje dosyası kurulabiliyor (§7.2). Çekirdeğin çoğu Markdown yöntem; bunlar bulutta olduğu gibi çalışır. Bozulan kısım kök çözümü, adlandırma, `$HOME` depoları, dış araçlar ve hook yükü; bir yama katmanıyla düzeltilebilir (§7.4). Ancak ECC bir DevOS değil. İş kaydı, zamanlayıcı, repo-bellek ve bağımsız doğrulayıcı üstüne kurulmalı.

**ECC'nin hazır verdiği**
- **Rol kütüphanesi:** 68 ajan; dar kapsam, açık araç listesi, çıktı biçimi.
- **Yöntem kütüphanesi:** 292 skill (O5d), 94 komut; plan, PRD, TDD, inceleme, doğrulama, devir şablonları.
- **Kapılı iş hattı ve fail-closed çok boyutlu inceleme** (`orch-*`, `orch-review`).
- **Döngü sözleşmeleri:** loop-operator koşulları, GAN plato kuralı, santa tur sınırı.
- **Sürümlenebilir kurulum sistemi:** manifest, profil, bileşen, install-state (sha256), doctor/repair/uninstall, hook kimlikleri ve drift koruması, hook onay kapısı.
- **Kural katmanı:** her zaman yüklenen çekirdek + `paths:` ile kapsamlı dil kuralları.

**ECC'nin vermediği ya da kanıtlamadığı**
- DevOS iş kaydı yok. En yakınları: PRD/plan dosyaları; `gh` gerektiren epic koordinasyonu; alfa ECC2.
- Buluta uygun zamanlayıcı yok: `/loop-start` betiksiz; dış cron Mac'e bağlar.
- Repo-bellek yok; depolar `$HOME`'da.
- Kapılar kullanıcıya bağlı; bağımsız doğrulayıcı yok.
- Etkinlik kanıtı yok:
  - Ajanların ve komutların çıktı kalitesine dair ölçüm yok.
  - `harness-audit` varlığı ölçüyor.
  - GAN, santa ve orch-review için yalnız tasarım gerekçesi var ("11 raw findings collapsed to 4 unique" tek sayısal iddia, tek yerel deneme) [kaynak diyor].

**Önerilen katmanlama (O-16 ile uyumlu: örneğin üstüne kur)**
1. **L0 ECC çekirdeği.** Pinli commit, kendi kurucusuyla `claude-project` kurulumu, `ecc-install.json` commit'li. Profil `developer`; `full` bağlam ölçümü sonrasına.
2. **L1 bulut yama katmanı.** Küçük, sürümlü `.devos/patches/ecc/` dizini ve yeniden uygulanabilir betik. İçerik: kök çözümü, `ecc:` adları, yollar, `gh`→MCP, atıf, hook profili ve kapatılan hook'lar, `$HOME`→repo env'leri. Önce ECC dosyalarına dokunmayan yollar kullanılır (settings `env`, `.claude/ecc/setup.json`, gölgeleme); yerinde yama yalnız zorunluysa yapılır, çünkü `repair` onu geri alır (§7.6). Her ECC güncellemesinde `ecc doctor` ve yama betiği yeniden koşulur.
3. **L2 DevOS katmanı.** Ayrı adlarla (`devos-*`):
   - İş kaydı (PRD/plan biçiminden türetilmiş, repo içinde).
   - Bağımsız doğrulayıcı (`orch-review` iskeleti).
   - Oturum devri (save-session şablonu, repo içinde).
   - Döngü sözleşmesi (loop-operator koşulları).
   - Ders kaydı (`/learn-eval` kapısı).
   - Batu kapılarının yerine doğrulayıcı kuralları.
4. **L3 ölçüm.** Her mekanizma için "tetiklendi mi, modele ulaştı mı" testi ve maliyet ölçümü. Kullanılmayan ECC parçaları ölçüm sonrasında `--without` ile kapatılır; seçim tahminle değil veriyle yapılır.

**Kanıt durumu özeti**
- Kurulum yolunun planlama kısmı çalışıyor [gözledim].
- Uygulama, hook'ların bulutta tetiklenmesi, synced plugin davranışı ve Workflow aracı sınanmadı [bilinmiyor].
- ECC'nin kalite iddiaları kanıtsız [kaynak diyor / kanıt yok].

## 9. Dersler (ne yanlış gitti, kök neden, önlem)

1. **Belge koddan kayıyor.**
   - COMMAND-AGENT-MAP: `/plan`→planner ve `/code-review`→code-reviewer diyor; komutlar inline çalışıyor. `/loop-start`→loop-operator diyor; komut ajanı anmıyor.
   - QUICK-REF: `/build-fix` "delegates to the right build-resolver agent automatically" diyor; komut inline. `/cost-report` "SQLite database" diyor; komut `costs.jsonl` okuyor.
   - CLAUDE.md `/tdd` ve `/e2e`'yi anıyor; ikisi emekli. `/checkpoint` `/verify quick`'e atıf yapıyor.
   - TROUBLESHOOTING eski `~/.claude/homunculus` yolunu ve "Requires Claude Code 2.0+" diyor; README 2.1+ diyor.
   - Longform'daki `examples/sessions` bağlantısı yok [gözledim].
   - **Kök neden:** Tek kaynak yok; belge ve kod ayrı büyüyor.
   - **Önlem:** DevOS'ta belge-kod tutarlılık testi (CI grep).
2. **Vaat edilen bütünleşme yok.** spec-miner'ın anlattığı planner/tdd-guide/code-reviewer bütünleşmesi o ajanlarda yok [gözledim].
   - **Önlem:** Bir mekanizma, çağıranı ve çağrılanı birlikte test edilmeden "var" sayılmasın.
3. **Ad alanı varsayımı taşınabilirliği bozuyor.** `ecc:` öneki plugin kurulumuna özgü; aynı içerik proje kurulumunda çözülmüyor.
   - **Önlem:** DevOS rol adları tek yerde tanımlansın ve kurulum biçiminden bağımsız olsun.
4. **Kurulum yan etkisi.** Atıf ayarı sessizce `false` yapılıyor.
   - **Önlem:** Kurucu çıktısındaki settings farkı her kurulumda incelenip commit'lensin.
5. **Kök arama zinciri eksik.** Yeni bir kurulum yeri (proje, synced) eklenince komutlar sessizce `~/.claude`'a düşüyor.
   - **Önlem:** Kök tek env'den gelsin; bulunamazsa açık hata versin.
6. **Etkisiz yapılandırma üretimi.** `/hookify` kural dosyası yazıyor, onu okuyan hook yok.
   - **Önlem:** Üretilen her yapılandırmanın tüketicisi ve testi olsun.
7. **Dış araç varsayımı.** `gh`, codex, gemini, ccg, Playwright MCP varsayılıyor; eksiklikte bazıları açık hata veriyor (`/pr`), bazıları sessizce düşüyor (santa yedeği uyarı basıyor, `gan-evaluator` mod yazmak zorunda).
   - **Önlem:** DevOS başlangıç kontrolü: araç envanteri → etkin mekanizma listesi.

## 10. Aktarım tablosu

| Parça | Karar | Gerekçe ve bulut uyarlaması |
|---|---|---|
| ECC'nin tamamı (L0), pinli, kendi kurucusuyla | Uyarlayarak al | Kurulabiliyor; yama katmanı zorunlu (§7.4); profil ölçümle; `/auto-update` yerine pinli SHA |
| Kurulum defteri, güven kökü, sahiplik koruması, doctor/repair | Al (desen olarak da) | sha256 defter + kök sınırı + "kullanıcı dosyasına dokunma" DevOS'un kendi kurulumunda da kullanılsın (§7.6) |
| planner / architect / code-architect / code-explorer | Al | Plan biçimleri; ana oturumdan çağrılır |
| `/prp-plan` + PRD + `/prp-implement` zinciri | Al | İş kaydı biçimi; `gh`→MCP |
| code-reviewer + dil inceleyicileri + `/review-pr` | Al | Dar şeritler; doğrulayıcıya bağlanır |
| `/orch-review` workflow | Uyarlayarak al | Bağımsız doğrulayıcı iskeleti; ad ve yol yaması |
| `orch-*` kapılı hat | Uyarlayarak al | Kapılar Batu yerine doğrulayıcıya |
| santa-loop | Uyarlayarak al | İki taze Claude gözden geçiren |
| GAN üçlüsü, `/gan-build` | Uyarlayarak al | Yazar ≠ değerlendirici, plato; rubrik SOUL'a göre |
| loop-operator koşulları | Al | DevOS döngü sözleşmesi |
| harness-optimizer ilkeleri | Uyarlayarak al | Kendini iyileştirme sınırı; güvenlikte bağımsız onay |
| agent-evaluator | Al | Teslim öncesi karne |
| save/resume-session, sessions | Uyarlayarak al | Depo repo içine; otomatik devam |
| `/learn-eval`, `/skill-create` atomik yazma | Al | Ders kaydı kapısı |
| rules/common | Uyarlayarak al | `ecc:`, `gh`, atıf satırları yamalı |
| Dil kuralları (`paths:`) | Al (yığına göre) | Bağlam maliyeti düşük |
| epic-* modeli | Uyarlayarak al | GitHub MCP ile; ya da repo dosyası kanonik |
| multi-*, pm2, marketing, ito, nasiko, ECC2, plan-canvas, contexts | Alma | Bulut ya da amaç dışı |
| `/hookify` | Alma | Tüketicisi yok |
| `/loop-start` | Alma (metin olarak) | Arkasında motor yok; DevOS kendi döngüsünü yazar |
