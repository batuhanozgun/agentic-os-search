# R07 — Anthropic ve Claude Code: uzun soluklu, çok oturumlu, çok ajanlı iş için en iyi uygulamalar

**Tür:** Alt ajan araştırma notu (model çıktısı), EXP-007 P0.3. Görev tanımı: [briefs/R07](../briefs/R07.md). Ortak kurallar: [briefs/ORTAK](../briefs/ORTAK.md).  
**Tarih ve erişim:** 27 Eylül 2026. Bütün web kaynaklarına bu tarihte `curl` ile erişildi.  
**Yazma kısıtı:** Bu dosya dışında dosya yazılmadı. Durum değiştiren git komutu ya da araç çağrısı yapılmadı. Ortam gözlemleri salt okumayla yapıldı: ortam değişkenleri, `~/.claude.json` anahtarları, `~/.claude/` dizini.  
**Kanıt gücü uyarısı:** Dış kanıtların hepsi Anthropic kaynaklıdır: ürün belgesi, mühendislik yazısı ya da Anthropic'in kendi iç ölçümü. Bağımsız ölçüm aranmadı; Anthropic dışı yöntemler R08'in konusu. "Topluluk pratiği" yalnız Anthropic'in aktardığı kadarıyla geçer (ör. "Ralph Wiggum" döngüsü, E-HD).

## Soru

Anthropic, Claude ile uzun soluklu, çok oturumlu ve çok ajanlı çalışmayı nasıl kurmayı öneriyor? Sekiz alt sistemde standart seviye ne? Alt sistemler: bağlam, bellek, kalıcı roller, prosedürler, zorlayıcı kontroller, orkestrasyon, süreklilik, doğrulama. Bu önerilerden hangileri Claude Code cloud oturumunda gerçekten uygulanabilir?

**Beslediği karar:** METHOD v1'de bu alt sistemlerin hangi mekanizmalarla kurulacağı.

## Kaynaklar ve okuma kapsamı

Claude Code belgeleri `https://code.claude.com/docs/en/<sayfa>.md` biçiminde okundu. Kısaltmalar metin boyunca kullanılır.

| Kısaltma | Kaynak | Kapsam |
|---|---|---|
| BP | best-practices | tam |
| MEM | memory | tam |
| SA | sub-agents | kısmi. Okunan: kapsam, dosya biçimi, frontmatter tablosu, model, araçlar, izin kipi, skill önyükleme, kalıcı bellek, hook'lar, delegasyon, ön/arka plan, çıktı taraması, iç içe açma, eşzamanlılık, başlangıç bağlamı, sürdürme, sıkıştırma, fork. Okunmayan: yerleşik alt ajanlar, hızlı başlangıç, örnekler |
| SK | skills | kısmi. Okunan: konumlar, cloud, içerik türleri, frontmatter, destek dosyaları, çağırma denetimi, yaşam döngüsü, `allowed-tools`, alt ajanda çalıştırma, değerlendirme, sorun giderme. Okunmayan: argümanlar, dinamik bağlam, paylaşım |
| HG | hooks-guide | kısmi. Okunan: olay tablosu, sıkıştırma sonrası enjeksiyon, prompt/agent/http hook, sınırlamalar, izin kipleriyle ilişki, Stop sınırı |
| HR | hooks (başvuru) | hedefli kısmi. Okunan: giriş ve cloud notu, eşleyiciler, `SessionStart`, `Stop`, `SubagentStop` girdisi, `PreCompact`/`PostCompact`, skill ve ajan hook'ları, çalışma alanı güveni, `agent_type` alanı |
| SET | settings | kısmi: "Settings in cloud sessions", "When edits take effect" |
| CW | context-window | kısmi: yazılı bölümler; etkileşimli bileşenin kodu okunmadı |
| CWF | common-workflows | kısmi |
| HOW | how-claude-code-works | kısmi: agentic loop, bağlam penceresi, delegasyon |
| FO | features-overview | tama yakın |
| DIR | claude-directory | kısmi: dosya seçimi ve dosya başvuru tabloları, `agent-memory` notları |
| WF | workflows | kısmi: ne zaman kullanılır, yerleşik iş akışı, çalışma biçimi, sınırlar, maliyet |
| AT | agent-teams | kısmi: ne zaman, plan onayı, kalite kapıları, ajanlar arası mesaj, bağlam, en iyi uygulamalar |
| PRJ | claude-projects | kısmi: ne zaman, yapı, bağlam, ayar, kalıcı bağlam, talimat yazımı, sorun giderme |
| PC | prompt-caching | kısmi: sıkıştırma, CLAUDE.md düzenlemesi, önbellek ömrü, alt ajanlar |
| OS | output-styles | kısmi (baş kısım) |
| PM | permission-modes | kısmi: auto kipi, alt ajanlar, geri düşme |
| PERM | permissions | kısmi: "What runs before you trust a folder" |
| GOAL | goal | kısmi: koşul yazımı, değerlendirme, cloud notu |
| ST | scheduled-tasks | kısmi: yalnız "cloud" geçen satırlar. Ayrıntıda R01'e dayandım |
| WEB | claude-code-on-the-web | kısmi: "Manage context" ve komut tablosu |
| CENV | cloud-environments | kısmi: taşınanlar tablosu, süre sınırları, kurulum betiği ve `SessionStart` |
| COST | costs | kısmi |
| E-CTX | anthropic.com/engineering/effective-context-engineering-for-ai-agents (29 Eyl 2025) | tam |
| E-MARS | …/multi-agent-research-system (13 Haz 2025) | tam |
| E-HAR | …/effective-harnesses-for-long-running-agents (26 Kas 2025) | tam |
| E-HD | …/harness-design-long-running-apps (24 Mar 2026) | tam; ekteki örnek plan kısmi |
| E-BEA | …/building-effective-agents (19 Ara 2024) | tam |
| E-TOOL | …/writing-tools-for-agents (11 Eyl 2025) | kısmi (giriş ve ilkeler) |
| E-SKILL | …/equipping-agents-for-the-real-world-with-agent-skills (16 Eki 2025) | tam |
| E-EVAL | …/demystifying-evals-for-ai-agents (9 Oca 2026) | kısmi (anahtar bölümler) |
| E-MA | …/managed-agents (8 Nis 2026) | tam |
| E-CC | …/building-c-compiler (5 Şub 2026) | tam |
| E-AUTO | …/claude-code-auto-mode (25 Mar 2026) | kısmi |
| — | …/engineering/claude-code-best-practices | 308 ile BP'ye yönleniyor; ayrı metin yok |
| — | "context management / memory tool" başlıklı mühendislik yazısı | engineering dizininde bulunamadı. Karşılığı olarak N-CTX ve P-* okundu |
| N-CTX | anthropic.com/news/context-management (29 Eyl 2025) | tam |
| BLOG | claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more (18 Haz 2026) | tam |
| P-MEM | platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | kısmi |
| P-CE | …/build-with-claude/context-editing | kısmi (giriş) |
| P-CMP | …/build-with-claude/compaction | kısmi (giriş) |
| P-PBP | …/build-with-claude/prompt-engineering/claude-prompting-best-practices | kısmi; "Agentic systems" bölümü tam |
| P-O5 | …/build-with-claude/prompt-engineering/prompting-claude-opus-5 | kısmi: uzunluk, kapsam, alt ajan, öz-düzeltme |

**Repo kaynakları:**
- Tam okunanlar: ORTAK, R07 görev tanımı, [U004](../../../sources/conversation/U004.md), [A003](../../../sources/conversation/A003.md), [R01](R01-ortam-ve-ozerklik-degerlendirmesi.md), R02, R05, EXP-007 STATE, README, DECISIONS, P0 README; `git show origin/main:explorations/EXP-006-development-os-calisma-duzeni/work/P1-01-claude-cloud-environment-map.md` (bundan sonra "P1-01").
- Kısmi okunanlar (anahtar kelime taraması): R03, R04, R06.
- `AGENT.md` ve `agent/protocols/`: yalnız satır ve bayt sayıları alındı.

**Okunmayanlar:**
- Mühendislik yazıları: claude-think-tool, advanced-tool-use, code-execution-with-mcp, how-we-contain-claude, claude-code-sandboxing, contextual-retrieval ve postmortem yazıları.
- Belge sayfaları: agents, tools-reference, sessions, env-vars, large-codebases, debug-your-config.

**Erişilemeyen kaynak yok.**

### Etiketler
- **İddia etiketi:** kaynak diyor / gözledim / çıkarım / varsayım / bilinmiyor.
- **Kanıt gücü:**
  - **T**: tedarikçinin (Anthropic) belgesi ya da iddiası.
  - **Tö**: tedarikçinin kendi iç ölçümü.
  - Bu notta bağımsız ölçüm yok.
- **Cloud etiketi:**
  - **C+**: cloud için açıkça belgelenmiş.
  - **C~**: genel belge; cloud'a özel ifade yok.
  - **C!**: cloud'da kısıtlı ya da farklı.
  - **C?**: belirsiz.
  - **Cg**: bu cloud oturumunda gözlendi.

### Bu oturumda gözlenenler (Cg, 27 Eylül 2026)
- **Ortam değişkenleri:**
  - `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`
  - `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80`
  - `CLAUDE_CODE_REMOTE=true`
  - `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_default`
  - `CLAUDE_CODE_ENTRYPOINT=remote_desktop`
- **Güven kaydı:** `~/.claude.json` içinde `projects` anahtarı yok. Yani bu klasör için kayıtlı bir çalışma alanı güveni (`hasTrustDialogAccepted`) yok.
- **Auto memory:** `~/.claude/projects/-home-user-agentic-os-search/` altında `memory/` dizini yok. Oturum yaklaşık 11 saattir açık.
- **Ortamın kendi hook'u:** `~/.claude/launcher-settings.json` bir `Stop` hook'u kaydediyor (`stop-hook-git-check.sh`) ve `Skill` iznini veriyor. Bu hook repodan değil, ortamdan geliyor.
- **Repo:** `CLAUDE.md`, `AGENTS.md` ya da `.claude/` yok. `AGENT.md` 205 satır, 12,4 KB. `agent/protocols/` altında 9 dosya var, toplam 1.908 satır ve yaklaşık 102 KB.
- **Bu alt ajanın araç listesi:** Durum değiştiren araçları içeriyor: `mcp__Claude_Code_Remote__create_session`, `send_later`, `create_trigger`, `Artifact`, `SendMessage`. Görev tanımı bunları yalnız düz yazıyla yasaklıyor.

---

## 0. Kısa sonuç

1. **Tek kısıt, üç katman.** Anthropic'in önerilerinin çoğu tek bir kısıttan türüyor: bağlam penceresi sonlu bir "dikkat bütçesi"dir ve doldukça başarım düşer (*context rot*).
   - Standart düzen üç katmanlıdır:
     - her oturumda yüklenen az ve öz talimat (kök CLAUDE.md, 200 satırın altında);
     - gerektiğinde yüklenen bilgi (`paths` alanlı rules, skill gövdeleri, alt dizin CLAUDE.md'leri, dosyalar);
     - bağlamın dışında tutulan durum (dosya, git, alt ajan bağlamları).
   - Kaynak: BP, MEM, E-CTX.
2. **Tavsiye ile zorlama ayrı katmanlardır.**
   - Tavsiye katmanı: CLAUDE.md, rules, skills, output style, proje talimatı ve proje belleği. Bunlar istektir.
   - Zorlama katmanı: hook'lar, izin kuralları ve ajan dosyasındaki araç listesi.
   - v0'ın (A003) kalite ve süreklilik vaatlerinin tamamı tavsiye katmanındaydı. Oysa kendi teşhisi "yazılı kural davranışa dönüşmedi" idi.
3. **Kalıcı rolün karşılığı commit'li bir ajan dosyasıdır.** Anthropic'te kalıcı rol, commit'lenmiş `.claude/agents/<rol>.md` dosyasıdır.
   - `memory: project` alanı role repoda duran kendi belleğini verir.
   - Anthropic'in tetiği şudur: aynı tür işçiyi aynı talimatla tekrar tekrar açıyorsan tanımla.
   - Bu tetik repoda zaten sağlanmış: R07–R11 aynı ORTAK görev tanımıyla açıldı.
4. **Uzun işin test edilmiş kalıbı.**
   - Ayrı istemle çalışan bir başlatıcı oturum. Ardından her oturumda tek artım yapan çalışan oturumlar.
   - Yapılandırılmış iş listesi (JSON), ilerleme dosyası ve her artımda git commit.
   - Oturum başında "yönünü bul" rutini; oturum sonunda temiz durum.
   - Sıkıştırma tek başına yetmedi. Bazı modellerde bağlamı sıfırlayıp yeniden başlamak daha iyi sonuç verdi. Kaynak: E-HAR, E-HD, P-PBP.
5. **Doğrulamanın standardı.**
   - Gereken parçalar: işten önce yazılmış ve koşulabilir bir kontrol, kanıt gösterme, üretenden ayrı bir değerlendirici. Değerlendirici şüpheci ayarlanır ve kalibre edilir; somut ölçüt ve sert eşikle çalışır. Kaynak: BP, E-HD.
   - Karşı uyarı: Opus 5 için Anthropic, genel "yeniden kontrol et" ya da "alt ajanla doğrula" talimatlarının aşırı doğrulama ürettiğini söylüyor (P-O5).
   - Ayrı değerlendirici, görev modelin tek başına güvenilir yaptığı sınırın ötesindeyse değer katar (E-HD).
6. **Cloud'da neyin geçerli olduğu.**
   - Repoya commit edilen CLAUDE.md, rules, skills ve agents cloud'a gelir.
   - `.claude/settings.json` hook'ları ve izin kuralları yalnız tek repolu oturumda okunur.
   - Kullanıcının `~/.claude` dizini cloud'a gelmez.
   - Auto memory cloud'da kalıcı bellek değildir. Bu oturumda bellek dizini hiç oluşmamış.
   - Alt ajan frontmatter hook'larının cloud'da çalışıp çalışmadığı belgelenmemiş (çalışma alanı güveni şartı) ve denenmedi.
7. **Ortamın bir sınırı ve P0'da zaten var olan bir kalıp.**
   - Bu ortamda derinlik sınırı 1'dir; alt ajan kendi alt ajanını açamaz.
   - Anthropic'in "alt ajan çıktısını dosyaya yazsın, koordinatöre yalnız referans dönsün" kalıbı P0'da zaten uygulanıyor: R07–R11 sonuçlarını dosyaya yazıp en fazla 200 kelimelik özet dönüyor (gözledim).
8. **Anthropic'in açık uyarıları.** Ayrıntı §3'te.
   - Oturum ve bağlam: ilgisiz işleri aynı oturumda karıştırmak ("kitchen sink"), üst üste düzeltmelerle kirlenmiş bağlam, şişmiş CLAUDE.md, kapsamsız keşif.
   - Doğrulama ve ilerleme: doğrulamasız güven, erken zafer ilanı, işi tek seferde yapmaya çalışmak, kendi işini notlarken cömertlik.
   - Orkestrasyon: basit işe onlarca alt ajan, belirsiz görev tanımıyla mükerrer iş, ajanlar arası aktarımda "kulaktan kulağa" bilgi kaybı.
   - Harness: harness varsayımlarının modeller geliştikçe eskimesi.

---

## 1. Bütün alt sistemlere geçen altı ilke

1. **Bağlam sonlu bir bütçedir.** Hedef, istenen sonucu en olası kılan en küçük ve yüksek sinyalli token kümesidir.
   - "good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome" (E-CTX).
   - "Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills." (BP).
   - Etiket: kaynak diyor, T.
2. **En basit çalışan çözüm.** Her harness bileşeni, modelin tek başına yapamadığı bir şeye dair bir varsayımdır ve modeller geliştikçe eskir.
   - "find the simplest solution possible, and only increase complexity when needed" (E-BEA).
   - "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing" (E-HD).
   - "those assumptions need to be frequently questioned because they can go stale as models improve" (E-MA).
   - Etiket: kaynak diyor, T.
3. **Tavsiye zorlama değildir.**
   - "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens." (BP).
   - "A real guardrail needs to be deterministic, and the enforcement methods are hooks and permissions." (BLOG).
   - Etiket: kaynak diyor, T.
4. **Durum bağlamın dışında yaşar.**
   - "ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory." (P-MEM; API'nin memory aracı için otomatik eklediği sistem talimatı).
   - "The session is not Claude's context window" (E-MA, bölüm başlığı).
   - Etiket: kaynak diyor, T.
5. **Doğrulama döngüsü kapalı olmalı.**
   - "Claude stops when the work looks done. Without a check it can run, "looks done" is the only signal available, and you become the verification loop" (BP).
   - Etiket: kaynak diyor, T.
6. **Çok ajan pahalıdır ve yalnız belirli işlerde kazandırır.**
   - "multi-agent systems use about 15× more tokens than chats" (E-MARS, Tö).
   - "most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time" (E-MARS).
   - Etiket: kaynak diyor.

---

## 2. Alt sistemler: Anthropic ne öneriyor, standart seviyede ne olmalı

Her kontrol listesi maddesi şu biçimdedir:
- **Ne:** bileşen ne işe yarar.
- **Kanıt:** kaynak ve alıntı, etiketiyle.
- **Cloud:** cloud etiketi.
- **Yokluğunda:** ne bozulur; başka alt sistemler dahil.
- **Bedel.**
- **Gereksiz:** hangi koşulda gerçekten gereksizdir.

### 2.1 Bağlam yönetimi

**Anthropic'in önerisi:**
- **İlkeler (E-CTX, T):**
  - Az ama yüksek sinyalli token. "minimal does not necessarily mean short".
  - Gerektiğinde getirme (*just-in-time*): "maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime".
  - Kademeli açma (*progressive disclosure*): ajan bağlamı keşfederek adım adım bulur.
  - Karma model: "Claude Code is an agent that employs this hybrid model: CLAUDE.md files are naively dropped into context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time".
- **Context rot:** "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases" (E-CTX).
- **Uzun ufuklu işte üç teknik (E-CTX):** sıkıştırma, yapılandırılmış not tutma ve çok ajanlı mimari. Seçim ölçütü:
  - "Compaction maintains conversational flow for tasks requiring extensive back-and-forth;"
  - "Note-taking excels for iterative development with clear milestones;"
  - "Multi-agent architectures handle complex research and analysis where parallel exploration pays dividends."
- **Claude Code'da sıkıştırma:** "It clears older tool outputs first, then summarizes the conversation if needed. Your requests and key code snippets are preserved; detailed instructions from early in the conversation may be lost." (HOW).
  - Cloud'da sıkıştırma pencerenin bir kısmı dolunca tetiklenir (WEB, C+). Bu oturumda eşik %80 (Cg).
  - `/clear` cloud'da yoktur: "Start a new session from the sidebar instead" (WEB, C!).

**Ne her zaman, ne gerektiğinde yüklenir; sıkıştırmadan sonra ne olur** (MEM, SK, SA, CW, FO, OS, BLOG; kaynak diyor, T; C~):

| Mekanizma | Bağlama ne zaman girer | Sıkıştırmadan sonra |
|---|---|---|
| Kök CLAUDE.md ve `paths` alanı olmayan rules | Oturum başında; her istekte | Diskten yeniden eklenir |
| `@` ile içe aktarılan dosyalar | Oturum başında, en çok 4 atlama | Kök CLAUDE.md ile birlikte |
| Alt dizin CLAUDE.md'leri, `paths` alanlı rules | Eşleşen dosya okununca | Özetlenip gider; eşleşen dosya yeniden okununca döner |
| Auto memory (`MEMORY.md`'nin ilk 200 satırı ya da ilk 25 KB'ı) | Oturum başında | Diskten yeniden eklenir |
| Skill listesi (ad ve açıklama) | Oturum başında. Liste bütçesi bağlamın %1'i; açıklama ile `when_to_use` birlikte en çok 1.536 karakter | Liste yeniden eklenmez |
| Çağrılmış skill gövdesi | Çağrılınca; sonraki turlarda bağlamda kalır | Skill başına ilk 5.000 token, toplamda 25.000 token; en eski skill önce düşer |
| Alt ajan açıklamaları | Oturum başında; toplamı 15.000 tokeni aşarsa uyarı | — |
| Alt ajanın gövdesi ve bütün çalışması | Yalnız alt ajanın kendi bağlamında | Ana bağlama yalnız son mesaj döner |
| Hook çıktısı | Yalnız hook bir şey döndürürse | Önceki hook çıktıları özetlenir. `compact` eşleyicili `SessionStart` hook'u yeniden çalışır |
| Output style | Sistem isteminde | Etkilenmez |
| Plan kipinde yazılmış plan | — | Diskten yeniden eklenir |
| Okunmuş ya da düzenlenmiş dosyalar | Okununca | En son değişen en çok 5 dosya yeniden okunur; 5.000 tokenden büyük olanın yalnız yolu gelir |
| Arka plan alt ajanları ve komutları | — | Çalışmaya devam eder; Claude'a hangilerinin sürdüğü hatırlatılır |

#### Standart seviye kontrol listesi

**BY-1 · Kök CLAUDE.md kısa ve bir dizin gibi çalışır.**
- **Ne:** Yalnız her oturumda gereken olgular burada durur: komutlar, yapı, "her zaman" ve "asla" kuralları, nerede ne olduğu. Ayrıntı başka yere taşınır. Hedef 200 satırın altı.
- **Kanıt (kaynak diyor, T):**
  - "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence." (MEM)
  - "For each line, ask: "Would removing this cause Claude to make mistakes?" If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" (BP)
  - "Think of this file as giving Claude an overview of your codebase, or as an index pointing to other files" (BLOG)
- **Cloud:** C+. Repodaki CLAUDE.md klonla gelir (CENV). Cg: repoda CLAUDE.md yok. `AGENT.md` tek başına 205 satır; `@AGENT.md` ile içe aktarmak 200 satır önerisini aşar (çıkarım).
- **Yokluğunda:**
  - Kural gürültüde kaybolur.
  - Alt ajanlar da CLAUDE.md hiyerarşisini yüklediği için (SA) şişkinlik her alt ajanda yinelenir (çıkarım).
  - Sıkıştırmadan sonra yeniden yükleme de pahalanır.
- **Bedel:** Bilgiyi skill, rules ve dosyalara dağıtmak ve yönlendirmeyi güncel tutmak.
- **Gereksiz:** Hiçbir koşulda. Kısa tutmanın ek bedeli yok; tek bedel dağıtma disiplinidir.

**BY-2 · Yükleme kademeleri bilinçli seçilir.**
- **Ne:** Her bilgi parçası için karar verilir:
  - her zaman (kök CLAUDE.md ya da `paths` alanı olmayan rule);
  - dosyaya bağlı (`paths` alanlı rule ya da alt dizin CLAUDE.md);
  - istek üzerine (skill gövdesi, destek dosyası);
  - hiç yüklenmez, gerektiğinde okunur (repo dosyası).
- **Kanıt (kaynak diyor, T):**
  - "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill or a path-scoped rule instead." (MEM)
  - "An unscoped rule is mechanically identical to putting the content in CLAUDE.md: always loaded, always costing tokens." (BLOG)
- **Cloud:** C+ (rules, skills ve CLAUDE.md klonla gelir; CENV).
- **Yokluğunda:**
  - Ya her şey her zaman yüklenir ve bağlam çürür.
  - Ya da gereken kural sıkıştırmadan sonra kaybolur. Örneğin `paths` alanlı bir rule sıkıştırmada özetlenip gider: "If a rule must persist across compaction, drop the `paths:` frontmatter or move it to the project-root CLAUDE.md." (CW)
- **Bedel:** Her yeni kuralda sınıflandırma kararı ve dosya disiplini.
- **Gereksiz:** Toplam talimat birkaç düzine satırsa kademe ayrımı ertelenebilir. Bütünsel etkisi: talimat büyüdükçe bu erteleme, BR ve BP katmanlarının yükünü CLAUDE.md'ye yığar.

**BY-3 · Ağır okuma alt ajanda yapılır; ana bağlama kısa özet ya da dosya referansı döner.**
- **Ne:** Yoğun okuma ve arama alt ajanın kendi bağlamında yapılır. Dönüş kısa tutulur; ayrıntı dosyaya yazılır.
- **Kanıt:**
  - "Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)." (E-CTX)
  - "Subagents call tools to store their work in external systems, then pass lightweight references back to the coordinator." (E-MARS)
  - "Running many subagents that each return detailed results can consume significant context" (SA)
  - Etiket: kaynak diyor, T.
- **Cloud:** C+. Alt ajanlar cloud'da yereldeki gibi çalışır (WEB, R01). Cg: P0'daki R07–R11 bu kalıbı uyguluyor.
- **Yokluğunda:**
  - Koordinatörün bağlamı okumayla dolar ve erken talimatlar sıkıştırmada kaybolur (BY-4).
  - Alt ajan uzun sonuç dönerse yalıtımın kazancı yok olur.
- **Bedel:**
  - Alt ajan başına ayrı token harcanır.
  - Özet bilgi kaybeder; niteleyiciler düşebilir. R05 ve R06 bunun örneklerini topladı.
- **Gereksiz:** İş, sık karşılıklı konuşma ya da yakından paylaşılan bağlam gerektiriyorsa: "Use the main conversation when … Multiple phases share significant context" (SA).

**BY-4 · Sıkıştırma politikası yazılıdır.**
- **Ne:** Sıkıştırmanın ne zaman ve nasıl olacağı önceden belirlenir:
  - Kök CLAUDE.md'de bir "Compact Instructions" bölümü: sıkıştırmada neyin korunacağı.
  - `/compact <odak>` doğal kırılma noktalarında çalıştırılır.
  - Tasarım "sıkıştırmada ne hayatta kalır" tablosuna göre yapılır.
  - İsteğe bağlı: `compact` eşleyicili `SessionStart` hook'u ile STATE yeniden enjekte edilir.
- **Kanıt (kaynak diyor, T):**
  - "To control what's preserved during compaction, add a "Compact Instructions" section to CLAUDE.md or run `/compact` with a focus" (HOW)
  - "run `/compact` at a natural break in your work, such as between tasks, instead of waiting for auto-compaction to trigger mid-task" (PC)
  - "Use a `SessionStart` hook with a `compact` matcher to re-inject critical context after every compaction." (HG)
  - "overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later" (E-CTX)
- **Cloud:**
  - `/compact`: C+.
  - `SessionStart` hook: C+, ama yalnız tek repolu oturumda (CENV).
  - Otomatik eşiğin yüzdesini cloud ortamı kendisi belirler ve kullanıcı değeri bunu geçemez. Pencere boyutu ise `CLAUDE_CODE_AUTO_COMPACT_WINDOW` ya da `/autocompact` ile değiştirilebilir (WEB, C!).
- **Yokluğunda:**
  - Otomatik özet neyin önemli olduğunu tahmin eder.
  - Koordinatörün yalnız sohbette verilmiş kararları kaybolur. Bu da süreklilik alt sistemine (BS) sızar: yeni oturum yanlış özetten devam eder.
- **Bedel:**
  - CLAUDE.md'de birkaç satır.
  - Hook kullanılırsa betik bakımı ve A-04 onayı.
- **Gereksiz:** Oturumlar hiçbir zaman sıkıştırma eşiğine varmıyorsa. EXP-007'de koordinatör oturumları uzun sürdüğü için bu koşul yok (çıkarım).

**BY-5 · Temiz başlangıç ile sıkıştırma arasında kural vardır.**
- **Ne:** Hangi durumda yeni oturum açılacağı, hangi durumda sıkıştırılacağı önceden belirlidir:
  - İlgisiz işe geçerken yeni oturum.
  - Aynı konuda iki başarısız düzeltmeden sonra yeni oturum ve daha iyi bir istem.
  - Uzun bir iş spec'e yazıldıktan sonra uygulama temiz oturumda yapılır.
- **Kanıt (kaynak diyor, T):**
  - "If you've corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches." (BP)
  - "Once the spec is complete, start a fresh session to execute it." (BP)
  - "consider starting with a brand new context window rather than using compaction. Claude's latest models are extremely effective at discovering state from the local filesystem." (P-PBP)
  - E-HD, Sonnet 4.5'te "context anxiety" yüzünden sıfırlamayı zorunlu buldu; Opus 4.5 ile sıfırlamayı kaldırdı. Model bağımlı.
- **Cloud:** C! `/clear` yok; temiz başlangıç "yeni oturum" demektir (WEB). Bu da STATE'in repoda olmasını şart koşar.
- **Yokluğunda:** Kirlenmiş bağlamda üst üste düzeltme yapılır. EXP-006'da ChatGPT'yle yaşanan "bir önceki konuşma sonrakini belirledi" kayması bu türdendir (çıkarım; R02).
- **Bedel:** Yeni oturumun yeniden yönlenme maliyeti. BS-2 rutini bu maliyeti düşürür.
- **Gereksiz:** Kısa, tek konulu işlerde.

**BY-6 · Bağlam ölçülür ve gürültü kaynakta kısılır.**
- **Ne:**
  - `/context` ile ne yüklendiği düzenli kontrol edilir.
  - Araç ve komut çıktıları kısa tutulur: ayrıntı dosyaya, bağlama tek satırlık özet.
  - Büyük tek bir çıktı "thrashing" yaratmamalıdır: "If a single file or tool output is so large that context refills immediately after each summary, Claude Code stops auto-compacting after a few attempts" (HOW).
- **Kanıt (kaynak diyor, T):**
  - "The test harness should not print thousands of useless bytes. At most, it should print a few lines of output and log all important information to a file" (E-CC)
  - "For Claude Code, we restrict tool responses to 25,000 tokens by default." (E-TOOL)
- **Cloud:** `/context` C+ (WEB). Cg: bu ortamda harness büyük araç çıktılarını kendiliğinden bir dosyaya aktarıyor.
- **Yokluğunda:** Bağlamın neyle dolduğu görünmez. Sıkıştırma döngüye girebilir ve iş durur.
- **Bedel:** Düşük; alışkanlık gerektirir.
- **Gereksiz:** Yok.

**BY-7 · Repo, anlık erişim için düzenlenir.**
- **Ne:** Dosya ve klasör adları, dizin dosyaları ve tek yerde duran bilgi sayesinde ajan, gereken dosyayı tahmin edip okuyabilir.
- **Kanıt:** "Folder hierarchies, naming conventions, and timestamps all provide important signals that help both humans and agents understand how and when to utilize information." (E-CTX; kaynak diyor, T)
- **Cloud:** C~.
- **Yokluğunda:** Keşif sınırsızlaşır: "The infinite exploration … Claude reads hundreds of files, filling the context." (BP)
- **Bedel:** Dizin dosyalarının bakımı.
- **Gereksiz:** Yok. EXP-007 README'deki "Dosya görevleri" tablosu bunun erken biçimi (gözledim).

**BY-8 · Bağlam sınırına karşı modele bilgi verilir.**
- **Ne:** Sıkıştırma olan bir harness'ta modele bu söylenir. Böylece bütçe kaygısıyla işi erken bitirmez; bitmeden önce durumunu kaydeder.
- **Kanıt:** P-PBP örnek istemi: "Your context window will be automatically compacted as it approaches its limit … do not stop tasks early due to token budget concerns. As you approach your token budget limit, save your current progress and state to memory before the context window refreshes." (kaynak diyor, T)
- **Cloud:** C~.
- **Yokluğunda:** Bazı modellerde işler erken toparlanır. E-HD bunu "context anxiety" diye adlandırıyor.
- **Bedel:** Birkaç satır istem.
- **Gereksiz:** Model bu eğilimi göstermiyorsa. E-HD'ye göre Opus 4.5 "largely removed that behavior". Opus 5.5 için ölçülmedi (bilinmiyor).

### 2.2 Bellek yönetimi

**Anthropic'in önerisi:**
- İki yerleşik mekanizma vardır: "**CLAUDE.md files**: instructions you write … **Auto memory**: notes Claude writes itself" (MEM).
- İkisi de bağlamdır, zorlama değildir: "Claude treats them as context, not enforced configuration." (MEM)
- CLAUDE.md sistem istemi değildir: "CLAUDE.md content is delivered as a user message after the system prompt, not as part of the system prompt itself." (MEM)
- Bunlara ek olarak:
  - alt ajan belleği (`memory:` alanı);
  - Projects'te proje belleği ve proje talimatı (PRJ);
  - API'de memory aracı (P-MEM).
- Etiket: kaynak diyor, T.

**Hiyerarşi ve kalıcılık:**

| Katman | Yer | Kimin için | Cloud'da kalıcı mı |
|---|---|---|---|
| Kurumsal (managed) CLAUDE.md | `/etc/claude-code/CLAUDE.md` ya da managed ayar `claudeMd` | Bütün kullanıcılar | Yalnız sunucudan yönetilen ayar gelir; cihaz dosyası gelmez (CENV, C!) |
| Kullanıcı CLAUDE.md ve `~/.claude/rules/` | `~/.claude/` | Tek kişi, bütün projeler | Hayır (CENV, C!) |
| Proje CLAUDE.md ve `.claude/rules/` | Repo | Ekip | Evet; commit edilirse klonla gelir (C+) |
| `CLAUDE.local.md` | Repo kökü, gitignore'da | Tek kişi | Hayır; klonda yok (çıkarım) |
| `@` içe aktarım | CLAUDE.md içinden; en çok 4 atlama | — | İçe aktarılan dosya repodaysa evet |
| Auto memory | `~/.claude/projects/<proje>/memory/` | Makineye bağlı | Hayır: "Files are not shared across machines or cloud environments" (MEM). Cg: bu oturumda dizin yok |
| Alt ajan belleği, `memory: project` | `.claude/agent-memory/<ad>/` | Ekip (DIR: "committed") | Commit ve push edilirse evet (çıkarım; R01 ile aynı) |
| Alt ajan belleği, `memory: local` ya da `user` | `.claude/agent-memory-local/` ya da `~/.claude/agent-memory/` | Tek kişi | Hayır (çıkarım) |
| Proje belleği ve proje talimatı (Projects) | Projenin kendisinde (Project settings > Memory); repoda değil. Talimat en çok 16.000 karakter | Projenin bütün thread'leri; her cloud thread başlarken `MEMORY.md`'yi okur | Evet, Projects kullanılıyorsa (PRJ, C+). Hesapta var mı bilinmiyor (R01) |
| Memory aracı (API) | Uygulamanın kendi deposu | — | Claude Code oturumunda kullanılmıyor (C? / uygulanamaz) |

#### Standart seviye kontrol listesi

**BB-1 · Bellek türleri ayrı yerlerde tutulur.**
- **Ne:** Dört tür bellek birbirinden ayrılır:
  - talimat: CLAUDE.md ve rules;
  - öğrenilmiş örüntü: rol belleği;
  - iş durumu: STATE, ilerleme dosyası, git;
  - kaynak: sözler birebir.
- **Kanıt (kaynak diyor, T):**
  - MEM tablosu: CLAUDE.md "Instructions and rules", auto memory "Learnings and patterns".
  - Auto memory'nin `project` türü "ongoing work, deadlines, and decisions that Claude can't derive from the code or git history" içerir.
  - Projects notu: "put instructions about a repository in its `CLAUDE.md` and notes about the project in project memory" (PRJ).
- **Cloud:** C~.
- **Yokluğunda:** Talimat ile durum karışır. Kural dosyası şişer (BY-1) ve eskiyen durum satırları kural gibi okunur. R02'de EXP-006 için kaydedilen "eski 'sıradaki' satırları" riski budur.
- **Bedel:** Bir sınıflandırma kuralı yazmak ve uygulamak.
- **Gereksiz:** Yok.

**BB-2 · Cloud'da kalıcı olan yalnız commit ve push edilendir.**
- **Ne:** Kalıcı bellek repoda tutulur. Auto memory'ye güvenilmez.
- **Kanıt:**
  - MEM: auto memory makineye bağlıdır.
  - PRJ: "uncommitted changes can be lost. On long tasks, ask Claude to commit and push work in progress."
  - Etiket: kaynak diyor, T. Cg: bellek dizini yok.
- **Cloud:** C+.
- **Yokluğunda:** Öğrenilen şey VM geri alınınca kaybolur. "Ders kaydedildi" iddiası yanlış olur; bu da öğrenme döngüsünü bozar (R05 madde 19).
- **Bedel:** Bellek güncellemeleri commit akışına girer. Dal politikası (K-009) belleği de bağlar.
- **Gereksiz:** Yok.

**BB-3 · Rol belleği (`memory: project`) okunur, güncellenir ve budanır.**
- **Ne:**
  - Her kalıcı role `.claude/agent-memory/<rol>/MEMORY.md` verilir.
  - Rol gövdesinde iki talimat bulunur: "işe başlamadan belleğine bak" ve "bitince öğrendiğini yaz".
  - `MEMORY.md` yalnız bir dizindir; ayrıntı konu dosyalarında durur.
- **Kanıt:**
  - "`project` is the recommended default scope. It makes subagent knowledge shareable via version control." (SA)
  - "The subagent's system prompt also includes the first 200 lines or 25KB of `MEMORY.md` … with instructions to curate `MEMORY.md` if it exceeds that limit." (SA)
  - "Read, Write, and Edit tools are automatically enabled" (SA)
  - "Ask the subagent to consult its memory before starting work … Ask the subagent to update its memory after completing a task" (SA)
  - Etiket: kaynak diyor, T.
- **Cloud:** C~. Dosyalar repoda olduğu için commit edilirse taşınır (çıkarım). Cloud'da denenmedi.
- **Yokluğunda:** Batu'nun şikâyeti sürer: rol her seferinde sıfırdan biçilir ve rolün deneyimi birikmez (U004).
- **Bedel:**
  - Rol her çalıştığında bellek okuma ve yazma tokenleri harcanır.
  - Yazma araçları otomatik açıldığı için okuyucu gibi salt-okur roller bile yazabilir. Bu, BZ katmanındaki yazma sınırını gerektirir (çıkarım).
  - Aynı role paralel iki örnek aynı `MEMORY.md`'ye yazarsa çakışma olur (çıkarım).
  - `memory` alanı auto memory kapalıysa etkisizdir: "if you turn auto memory off … the `memory` field has no effect" (SA).
- **Gereksiz:** Tek seferlik işçilerde. Kalıcı rollerde değil.

**BB-4 · Belleği güncelleme tetikleri tanımlıdır.**
- **Ne:** CLAUDE.md ne zaman güncellenir:
  - "Claude makes the same mistake a second time";
  - "A code review catches something Claude should have known";
  - "You type the same correction … that you typed last session" (MEM).
- **Kanıt:** "A repeated mistake or a recurring review comment is a CLAUDE.md edit, not a one-off correction in chat." (FO; kaynak diyor, T)
- **Cloud:** C~.
- **Yokluğunda:** Batu'nun "Ben bunu geçen hafta da aynı şekilde anlatmıştım" durumu yinelenir (R03).
- **Bedel:** Düşük.
- **Gereksiz:** Yok.

**BB-5 · Bellek budanır ve çelişkiler temizlenir.**
- **Ne:** Düzenli budama yapılır. Çelişen kurallar ayıklanır. Eski bellek dosyaları silinir.
- **Kanıt:**
  - "Treat CLAUDE.md like code: review it when things go wrong, prune it regularly" (BP)
  - "if two rules contradict each other, Claude may pick one arbitrarily" (MEM)
  - "Periodically delete memory files that haven't been accessed in a long time." (P-MEM)
  - Claude Code bellek dosyasına `modified` zaman damgası yazar (MEM). `MEMORY.md` sınırı aşınca Claude'a dizini yeniden yazmasını söyler (MEM).
  - `/doctor`, commit'li CLAUDE.md için kesinti önerir (MEM).
  - Etiket: kaynak diyor, T.
- **Cloud:** `/doctor` cloud'da denenmedi (C?). Diğerleri C~.
- **Yokluğunda:** Bellek büyür; BY-1'deki uyum kaybı başlar.
- **Bedel:** Periyodik bakım işi.
- **Gereksiz:** Bellek küçük kaldıkça ertelenebilir.

**BB-6 · Bir kuralın etkisi davranışta sınanır.**
- **Ne:** Bir kural değişikliği davranışta gözlenmeden "işledi" sayılmaz.
- **Kanıt:**
  - "test changes by observing whether Claude's behavior actually shifts" (BP)
  - Kritik ayrıntı: "Editing them mid-session does not invalidate the cache, but the edit also doesn't apply. … The new content loads on the next `/clear`, `/compact`, or restart." (PC)
  - Etiket: kaynak diyor, T.
- **Cloud:** C~. Cloud'da `/clear` olmadığı için CLAUDE.md değişikliği ancak `/compact` ya da yeni oturumla devreye girer (çıkarım).
- **Yokluğunda:** Koordinatör oturum ortasında CLAUDE.md'yi düzeltir ve düzeltmenin hemen etkili olduğunu sanır; olmaz. A003 §3.10'daki "ders doğrulanmadı" ayrımı tam da bunun için var.
- **Bedel:** Bir sonraki oturumda ya da sıkıştırmadan sonra kontrol.
- **Gereksiz:** Yok.

**BB-7 · Mutlaka yüklenmesi gereken içerik `@` ile içe aktarılır, düz yazıyla "oku" denmez.**
- **Ne:** Düz yazıyla verilen "şunu oku" talimatı, Claude'un o dosyayı açmaya karar vermesine bağlıdır. Mutlaka yüklenmesi gereken içerik `@path` ile içe aktarılır. Ancak içe aktarma bağlam maliyetini düşürmez.
- **Kanıt (kaynak diyor, T):**
  - "A `CLAUDE.md` that tells Claude in words to read `AGENTS.md`: Claude sees `AGENTS.md` only if it decides to open the file." (MEM)
  - "imported files still load and enter the context window at launch" (MEM)
- **Cloud:** C~.
- **Yokluğunda:** A003 §3.9'daki okuma sırası ("CLAUDE.md, AGENT.md, durum dosyası, harita") yalnız istek olarak kalır.
- **Bedel:** Her içe aktarılan satır, her istekte token harcar.
- **Gereksiz:** İçerik yalnız bazı işlerde gerekiyorsa. O zaman içe aktarma yerine skill ya da rule kullanılır.

### 2.3 Kalıcı roller (alt ajan tanımları)

**Anthropic'in önerisi:**
- "Define a custom subagent when you keep spawning the same kind of worker with the same instructions." (SA)
- "Project subagents (`.claude/agents/`) are ideal for subagents specific to a codebase. Check them into version control" (SA)
- Dosya, YAML frontmatter ve ardından Markdown gövdeden oluşur. Gövde, alt ajanın sistem istemidir: "Subagents receive only this system prompt plus basic environment details like the working directory, not the Claude Code system prompt." (SA)
- Başlangıçta yüklenenler: kendi istemi, görev mesajı, CLAUDE.md hiyerarşisi, git durumu ve önyüklenen skill'ler. Konuşma geçmişi yüklenmez (SA).
- Etiket: kaynak diyor, T. C+: repodaki `.claude/agents/` cloud'da otomatik yüklenir (WEB, CENV).

**Bütün frontmatter alanları** (SA; yalnız `name` ve `description` zorunlu; "Claude Code ignores a field it doesn't recognize without reporting an error"):

| Alan | Ne yapar | EXP-007 için not |
|---|---|---|
| `name` | Kimliktir; hook'lara `agent_type` olarak gider. `:` içeremez, `-` ile başlayamaz; bütün ağaçta tekil olmalıdır | Sürüm adın içinde olabilir, ör. `reviewer-v2` (SA örneği) |
| `description` | Claude'un ne zaman devredeceğini belirler | Kısa tutulur; kendiliğinden devir için "use proactively" |
| `tools` | İzinli araçlar. Yazılmazsa alt ajanlara açık bütün araçlar miras alınır | Rol sözleşmesinin zorlama kısmı |
| `disallowedTools` | Çıkarılacak araçlar. `mcp__<sunucu>` kalıbıyla bir sunucunun bütün araçları çıkarılır | İşçilerden durum değiştiren Remote araçlarını çıkarmak (çıkarım) |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, tam model kimliği ya da `inherit` | Çözümleme sırası: çağrıdaki parametre → frontmatter → `CLAUDE_CODE_SUBAGENT_MODEL` → ana model |
| `permissionMode` | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan` | Ana oturum auto kipindeyse **yok sayılır** |
| `maxTurns` | Tur sınırı. Sınıra varınca çıktı "partial" işaretlenir; ajan sürdürülebilir | Durma ölçütünün mekanik parçası |
| `skills` | Başlangıçta skill'in tam içeriğini yükler | Ortak kanıt dili ve dönüş biçimi için |
| `mcpServers` | Role özel MCP sunucusu | — |
| `hooks` | Yalnız bu ajan çalışırken geçerli; `Stop` → `SubagentStop` olur | Cloud'da güven şartı belirsiz (BZ) |
| `memory` | `user`, `project` ya da `local` kalıcı dizin | `project` önerilir |
| `background` | Ajan hep arka planda çalışır | — |
| `effort` | `low` … `max` | — |
| `isolation` | `worktree`: ajan ayrı bir git çalışma ağacında çalışır | Paralel yazıcılar için |
| `omitClaudeMd` | Kullanıcı, proje ve yerel CLAUDE.md olmadan başlatır | Değerlendiricinin proje talimatından etkilenmemesi istenirse (çıkarım) |
| `color` | Görünüm | — |
| `initialPrompt` | Ajan ana oturum olarak (`--agent` ya da `agent` ayarı) çalışınca ilk tur | Koordinatörü rol dosyası olarak tanımlamak (cloud'da C?) |
| `experimental.cacheTtl` | `5m` ya da `1h` önbellek ömrü | Uzun çalışan işçiler |

#### Standart seviye kontrol listesi

**BR-1 · Roller proje kapsamında, commit'li ve doğrulanmış dosyalardır.**
- **Ne:** Her kalıcı rol `.claude/agents/<rol>.md` dosyasıdır.
- **Kanıt (kaynak diyor, T):**
  - Hatalı dosya sessizce atlanır: "Claude Code skips a file … without reporting it in the session" (SA). Nedenleri: `name` yok, `description` yok, YAML ayrışmıyor.
  - Kontrol aracı: `claude plugin validate .claude/agents` (SA; v2.1.233+).
- **Cloud:** C+.
- **Yokluğunda:**
  - Rol her görev tanımında yeniden anlatılır (U004 eleştirisi).
  - Rolün araç sınırı, modeli ve belleği tanımlanamaz; bu da BZ ve BB katmanlarını boşaltır.
- **Bedel:**
  - Dosya bakımı.
  - A-04 onayı: `.claude/agents` kontrol yapılandırması sayılıyor (README).
- **Gereksiz:** Yok. Tetik koşulu sağlanmış: R02–R06 sohbet içinde, R07–R11 ise aynı ORTAK görev tanımıyla açıldı (gözledim).

**BR-2 · Description iyi yazılır.**
- **Ne:** Ne zaman devredileceği, tetik sözcükleriyle birlikte kısa bir description'da yazılır. Ayrıntı gövdeye gider.
- **Kanıt:**
  - "Claude uses each subagent's description to decide when to delegate tasks." (SA)
  - "include phrases like "use proactively"" (SA)
  - "Those descriptions take up context, so keep them short." (SA)
  - Toplam 15.000 tokeni aşınca uyarı verilir.
  - Etiket: kaynak diyor, T.
- **Cloud:** C~.
- **Yokluğunda:** Otomatik devir yanlış ya da hiç olmaz. Koordinatör her seferinde rolü adıyla çağırmak zorunda kalır.
- **Bedel:** Açıklamalar her oturumda bağlamda durur.
- **Gereksiz:** Rol yalnız adıyla (açıkça) çağrılacaksa otomatik devir gerekmez. Açıklama yine de kısa tutulur.

**BR-3 · Gövde, rol sözleşmesini taşır.**
- **Ne:** Gövdede amaç, girdi, çalışma yöntemi, çıktı biçimi, durma koşulu ve yapmayacakları yazılır. Alt ajan Claude Code sistem istemini almaz; gereken genel alışkanlıklar gövdeye yazılır. Kritik kural delegasyon mesajında yinelenir.
- **Kanıt:**
  - "If a rule must, such as "ignore the `vendor/` directory," restate it in the prompt you give Claude when delegating." (SA)
  - Yazım düzeyi: "specific enough to guide behavior effectively, yet flexible enough to provide the model with strong heuristics" (E-CTX)
  - Örnekler: "curate a set of diverse, canonical examples" (E-CTX), uç durum listesi değil.
  - Etiket: kaynak diyor, T.
- **Cloud:** C~.
- **Yokluğunda:** Görev tanımı her seferinde rolü de taşımak zorunda kalır; tanımlar arası tutarsızlık doğar.
- **Bedel:** Gövde yalnız rol çağrılınca yüklenir; ana bağlama maliyeti yoktur (BLOG).
- **Gereksiz:** Yok.

**BR-4 · Araç sınırı rol dosyasında zorlanır.**
- **Ne:** Her role yalnız işi için gereken araçlar verilir: `tools` ile izin listesi ya da `disallowedTools` ile yasak listesi. Örneğin okuyucu rol kendi çıktısı dışında yazmaz. Oturum başlatma ve zamanlama araçları yalnız koordinatörde kalır.
- **Kanıt:**
  - "Enforce constraints by limiting which tools a subagent can use" (SA)
  - "a background subagent keeps every MCP tool" (SA)
  - "When the main conversation is in … auto mode, the subagent runs in that same mode and Claude Code ignores the `permissionMode` you set." (SA)
  - Etiket: kaynak diyor, T.
- **Cloud:** C~. Cg: bu alt ajan durum değiştiren Remote araçlarına sahip. Görev tanımı yasağı yalnız düz yazıyla koyuyor (tavsiye).
- **Yokluğunda:**
  - Auto kipinde rolün izin kipi yok sayıldığı için tek kalan kısıt araç listesidir (çıkarım).
  - İşçi düz yazıdaki yasağı çiğneyebilir. R01 eksik-arayıcısı bu riski "Governance of the Remote tools" başlığıyla kaydetti.
- **Bedel:** Rol için yanlış dar tanımlanmış araç listesi işi keser. Hiçbir araç çözümlenmezse ajan açılmaz (SA).
- **Gereksiz:** Salt okur ve dış etkisi olmayan bir ortamda. EXP-007 böyle bir ortam değil.

**BR-5 · Model ve efor role göre seçilir.**
- **Ne:** Koordinatör güçlü modelde çalışır. İşçi, işin gerektirdiği en ucuz yeterli modelde çalışır.
- **Kanıt:**
  - "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval" (E-MARS, Tö)
  - "Control costs by routing tasks to faster, cheaper models like Haiku" (SA; T)
- **Cloud:** C~.
- **Yokluğunda:** Hep en pahalı model kullanılır. Haftalık limit baskısı artar (A003 §6: 4 milyon token).
- **Bedel:** Daha küçük modelde kalite riski. Rol başına denenmelidir.
- **Gereksiz:** Maliyet sorun değilse.

**BR-6 · Rol ek bilgisi önyüklenir.**
- **Ne:** Ortak kanıt dili, dönüş biçimi ve rol yöntemi gibi ortak parçalar skill olarak tutulur ve role `skills:` ile önyüklenir.
- **Kanıt:** "The full content of each listed skill is injected into the subagent's context at startup." (SA; T)
- **Cloud:** C+ (repo skill'leri cloud'a gelir; SK).
- **Yokluğunda:** Aynı metin her görev tanımına kopyalanır. ORTAK.md bugün bunu elle yapıyor (gözledim).
- **Bedel:**
  - Önyüklenen skill her çalıştırmada tam yüklenir.
  - `disable-model-invocation: true` olan skill önyüklenemez (SA).
- **Gereksiz:** Ortak parça yoksa.

**BR-7 · Rol sürümlenir ve eskiyen parçası ayıklanır.**
- **Ne:**
  - Rol dosyası git'te sürümlenir.
  - Değişiklik canlı devreye girer; çalışan ajan eski sürümle biter.
  - Yeni model gelince rolün hangi parçasının hâlâ yük taşıdığı tek tek çıkarılarak sınanır.
- **Kanıt:**
  - "the next delegation uses the updated definition, with no restart needed" (SA). İstisna: yeni bir `agents` dizinindeki ilk dosya yeniden başlatma ister.
  - "we use rainbow deployments to avoid disrupting running agents" (E-MARS)
  - "removing one component at a time and reviewing what impact it had on the final result" (E-HD)
  - Etiket: kaynak diyor, T.
- **Cloud:** C~. Dizin cloud'da ilk kez oturum içinde oluşturulursa yeniden başlatma gerekebilir (çıkarım).
- **Yokluğunda:**
  - Hangi sonucun hangi rol sürümüyle üretildiği bilinmez. R06, alt ajanın hangi görev tanımı sürümüyle çalıştığını kaydetmeyi istemişti.
  - Eskimiş iskele pahalı yük olarak kalır (E-MA).
- **Bedel:** Sonuç kaydına rol sürümü (commit) eklenir.
- **Gereksiz:** Yok.

**BR-8 · Rol davranışı ölçülür.**
- **Ne:** Rolün doğru tetiklenip tetiklenmediği ve çıktısının ölçüte uyup uymadığı temiz oturumda sınanır. Yazarın kendi bağlamında sınamak yanıltır.
- **Kanıt:**
  - "Seeing a skill trigger tells you Claude found it, not that it did what you intended." (SK)
  - "A fresh session matters because leftover context from authoring the skill will mask gaps in the written instructions." (SK)
  - Bu cümleler skill'ler için yazılmış; alt ajan için `claude plugin eval` yalnız plugin'lerde var (SA).
  - Etiket: kaynak diyor, T. Alt ajana uygulanması çıkarım.
- **Cloud:** C?
- **Yokluğunda:** "Rol çalışıyor" iddiası sınanmamış kalır. A003'teki soğuk başlangıç testi bunun oturum düzeyindeki biçimi.
- **Bedel:** Rol başına birkaç temiz oturum denemesi.
- **Gereksiz:** Rol çok basitse. İlk sürümde değil.

### 2.4 Prosedürler (skills)

**Anthropic'in önerisi:**
- **Skill ne zaman yazılır:** "Create a skill when you keep pasting the same instructions, checklist, or multi-step procedure into chat, or when a section of CLAUDE.md has grown into a procedure rather than a fact." (SK)
- **Kademeli açmanın üç düzeyi (E-SKILL):**
  1. Ad ve açıklama sistem isteminde durur.
  2. SKILL.md gövdesi ilgili olunca okunur.
  3. Destek dosyaları gerektikçe okunur. "the amount of context that can be bundled into a skill is effectively unbounded."
- **Kod da taşıyabilir:** "certain operations are better suited for traditional code execution … the deterministic reliability that only code can provide" (E-SKILL).
- **Büyüklük:** "Keep `SKILL.md` under 500 lines." (SK)
- **Yaşam döngüsü:** Çağrılan skill sonraki turlarda bağlamda kalır ve dosya yeniden okunmaz: "write guidance that should apply throughout a task as standing instructions rather than one-time steps" (SK).
- **Sıkıştırmada:** skill başına ilk 5.000, toplam 25.000 token korunur; en eski skill önce düşer (SK).
- Etiket: kaynak diyor, T. C+: cloud oturumu commit'li proje skill'lerini ve claude.ai hesabında açık skill'leri yükler. Kişisel `~/.claude/skills/` gelmez (SK, CENV). Cg: bu ortamda `~/.claude/skills/synced` var.

**Hangi mekanizma ne zaman** (FO, BLOG, SA, SK, WF; kaynak diyor, T):

| İhtiyaç | Mekanizma | Anthropic'in gerekçesi |
|---|---|---|
| Her oturumda bilinmesi gereken olgu ya da "her zaman" kuralı | Kök CLAUDE.md | "Put it in CLAUDE.md if Claude should always know it" (FO) |
| Belli dosya ya da dizinlere özgü kural | `paths` alanlı rule | "keeps it out of context during unrelated work" (BLOG) |
| Tekrarlanan yordam ya da ara sıra gereken başvuru bilgisi | Skill | "A 30-line procedure in CLAUDE.md. Procedures belong in skills." (BLOG) |
| Ana akışta görülüp yönlendirilmesi gereken yordam | Skill | "Use a skill when you want the procedure to play out inside the main thread so you can see and steer each step." (BLOG) |
| Yalıtılmış, özet dönen yan iş; araç ya da izin kısıtı | Alt ajan | "Use a subagent when a side task … would clutter your main conversation" (BLOG) |
| Birkaç alt ajanı aşan, tekrarlanabilir orkestrasyon ya da çapraz kontrol | Dinamik workflow; kayıtlıysa `.claude/workflows/*.js` | "A workflow moves the plan into code" (WF) |
| Her seferinde istisnasız olması gereken eylem ya da yasak | Hook ya da izin kuralı | "If a rule must hold every time, make it a hook rather than a prompt instruction." (FO) |
| Yanıtın biçimi, rolü, tonu (bütün oturum) | Output style | "output styles carry the highest instruction-following weight of any method that we've covered so far" (BLOG). Özel stil, Claude Code'un yazılım mühendisliği talimatlarını varsayılan olarak düşürür; `keep-coding-instructions: true` gerekir (BLOG) |
| Tek oturumu aşan, çok thread'li iş | Projects: proje talimatı ve proje belleği | "a goal that outlasts one session and keeps producing tasks" (PRJ) |

#### Standart seviye kontrol listesi

**BP-1 · Tekrarlanan yordam skill'e taşınır.**
- **Ne:** Aynı yordam üçüncü kez sohbete yapıştırılıyorsa skill'e taşınır. CLAUDE.md'de yordam tutulmaz.
- **Kanıt:** Tetik tablosu: "You paste the same playbook or multi-step procedure into chat for the third time → Capture it as a skill" (FO; kaynak diyor, T).
- **Cloud:** C+.
- **Yokluğunda:**
  - Yordam ya CLAUDE.md'yi şişirir (BY-1) ya da her görev tanımında yeniden yazılır.
  - EXP-007'deki adaylar (gözledim): görev tanımı şablonu (ORTAK), kanıt dili, okuma kaydı biçimi, devir ve durum güncelleme, karşı-okuma istemi.
- **Bedel:** Skill yazma ve bakım. Skill açıklamaları her oturumda bağlamdadır (düşük).
- **Gereksiz:** Yordam bir kez yapılıyorsa.

**BP-2 · SKILL.md yapısı sıkıştırmaya dayanıklıdır.**
- **Ne:** Kısa gövde; en önemli talimat başta; ayrıntı destek dosyalarında; deterministik işler betikte.
- **Kanıt:** "Truncation keeps the start of the file, so put the most important instructions near the top of `SKILL.md`." (CW; T)
- **Cloud:** C+.
- **Yokluğunda:** Uzun oturumda skill'in son kısmı kesilir. Skill'in davranışı etkilemesi "kaybolur" (SK sorun giderme).
- **Bedel:** Yazım disiplini.
- **Gereksiz:** Kısa skill'lerde.

**BP-3 · Kimin çağıracağı denetlenir.**
- **Ne:**
  - Yan etkili ya da zamanlaması önemli yordamlar (commit, birleştirme, Batu'ya rapor): `disable-model-invocation: true`.
  - Arka plan bilgisi: `user-invocable: false`.
  - Açıklamada kullanıcının doğal olarak söyleyeceği sözcükler bulunur.
- **Kanıt:** "You don't want Claude deciding to deploy because your code looks ready." (SK; T)
- **Cloud:** C~.
- **Yokluğunda:** Yanlış zamanda tetiklenen yan etki olur ya da skill hiç tetiklenmez.
- **Bedel:** Düşük.
- **Gereksiz:** Yan etkisiz bilgi skill'lerinde ilk madde gereksizdir.

**BP-4 · Yalıtılmış yordamlar ayrı bağlamda koşar.**
- **Ne:** Kendi başına anlamlı bir görev içeren yordam `context: fork` ve `agent:` ile ayrı bağlamda çalıştırılır.
- **Kanıt (kaynak diyor, T):**
  - "`context: fork` only makes sense for skills with explicit instructions." (SK)
  - Arka planda koşan fork, arka plan araç kısıtına uyar (SK).
- **Cloud:** C~. Cg: bu ortamda derinlik 1. Bir alt ajan içinden fork'lu skill çağrılabilir mi, belli değil (C?).
- **Yokluğunda:** Uzun yordam ana bağlamı doldurur.
- **Bedel:** Yordam konuşma geçmişini görmez; talimatın kendine yetmesi gerekir.
- **Gereksiz:** Yordamın adım adım izlenmesi isteniyorsa.

**BP-5 · Skill'in işe yaradığı ölçülür.**
- **Ne:** Birkaç gerçekçi istem temiz oturumda skill'li ve skill'siz koşulup sonuçlar karşılaştırılır.
- **Kanıt:**
  - "Start with evaluation: Identify specific gaps in your agents' capabilities by running them on representative tasks" (E-SKILL)
  - "Iterate with Claude: … ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill." (E-SKILL)
  - Etiket: kaynak diyor, T.
- **Cloud:** C? `skill-creator` eklentisi cloud'a repo ayarıyla gelmez (CENV). claude.ai hesabında açık skill olarak gelebilir mi, bilinmiyor.
- **Yokluğunda:** Prosedürün kendisinin kaymaya yol açıp açmadığı görünmez.
- **Bedel:** Birkaç deneme oturumu.
- **Gereksiz:** Basit başvuru skill'lerinde.

**BP-6 · Tekrarlanan orkestrasyon betiğe dönüşür.**
- **Ne:** P0.3'teki gibi aynı yelpazede işçi açma ve karşı-okuma deseni tekrarlanıyorsa, orkestrasyon kayıtlı bir workflow'a dönüşür.
- **Kanıt:** "What's repeatable … The orchestration itself" (WF; T). Kayıtlı betik `/ad` komutu olur (DIR).
- **Cloud:** C+. Sonuçlar cloud konuşma geçmişiyle saklanır (R01).
- **Yokluğunda:** Koordinatör her seferinde orkestrasyonu yeniden kurar.
- **Bedel:**
  - Çalışma sırasında kullanıcı girdisi yok: "For sign-off between stages, run each stage as its own workflow" (WF).
  - Token maliyeti yüksek.
- **Gereksiz:** Orkestrasyon bir kez yapılıyorsa.

**BP-7 · Skill güvenliği gözetilir.**
- **Ne:** Yalnız güvenilir skill kullanılır. Skill içinde dış ağa bağlanma talimatı olup olmadığına bakılır.
- **Kanıt:** "We recommend installing skills only from trusted sources." (E-SKILL; T)
- **Cloud:** C~.
- **Yokluğunda:** Bir skill, alt ajanın okuduğu dış içerik gibi komut enjeksiyonu kanalı olur.
- **Bedel:** İnceleme.
- **Gereksiz:** Yalnız kendi yazdığımız skill'ler varsa.

### 2.5 Zorlayıcı kontroller

**Anthropic'in önerisi:**

| Katman | Öğeler | Güvence türü |
|---|---|---|
| Tavsiye | CLAUDE.md, rules, skill, output style, proje talimatı ve belleği, görev tanımı | Claude'un yorumuna bağlı. "Claude follows both as instructions, so neither is enforced." (FO) |
| Zorlama | `command`, `http`, `mcp_tool` hook'ları; izin kuralları (allow, ask, deny); ajan dosyasındaki `tools` ve `disallowedTools`; managed settings | Deterministik tetik. "Hooks can tighten restrictions but not loosen them past what permission rules allow." (HG) |
| Yargıya dayalı kapı | `prompt` ve `agent` hook'ları, `/goal` değerlendiricisi | Tetik deterministik, karar modele ait (BLOG). `/goal` değerlendiricisi "doesn't run commands or read files independently" (GOAL) |
| Olasılıklı güvenlik ağı | auto kipinin sınıflandırıcısı | "Auto mode reduces permission prompts but does not guarantee safety." (PM). Gerçek aşırı hevesli eylemlerde %17 yanlış negatif (E-AUTO, Tö) |

**Uzun iş için önemli hook olayları** (HG, HR; kaynak diyor, T):
- **`SessionStart`:** eşleyiciler `startup`, `resume`, `clear`, `compact`, `fork`. Komutun stdout'a yazdığı metin bağlama eklenir.
- **`UserPromptSubmit`:** istem işlenmeden önce çalışır.
- **`PreToolUse`:** aracı engelleyebilir. "A hook that returns `permissionDecision: "deny"` blocks the tool even in `bypassPermissions` mode".
- **`PostToolUse`:** "can't undo actions".
- **`Stop` ve `SubagentStop`:**
  - `decision: "block"` ile devam ettirir.
  - Üst üste 8 devamdan sonra sınır devreye girer; `stop_hook_active` alanıyla döngü önlenir.
  - `SubagentStop` girdisi `last_assistant_message` ve `agent_transcript_path` içerir.
- **`PreCompact`:** "Exit with code 2 to block compaction." `PostCompact` ise `compact_summary` alır.
- **Ekip olayları:** `SubagentStart`, `TaskCreated`, `TaskCompleted`, `TeammateIdle`.
- **Tanı olayları:** `InstructionsLoaded` (hangi CLAUDE.md ya da rule yüklendi), `ConfigChange`, `StopFailure`.
- **`SessionEnd`:** bütün hook'lar 1,5 saniyelik ortak bütçeyle çalışır.
- **Hook'ların yapamadıkları:** "Command hooks communicate through stdout, stderr, and exit codes only. They can't trigger `/` commands or tool calls." `Stop` hook'u işin bittiği anda değil, "whenever Claude finishes responding" çalışır (HG).

**Cloud'daki geçerlilik:**
- **C+:** "Claude Code fires the same hook events wherever it runs: … cloud sessions" (HR).
- **C!:** Repodaki `.claude/settings.json` hook'ları ve izin kuralları "Yes, in a session with one repository" (CENV). Çok repolu oturumda ve çok repolu Projects thread'inde okunmazlar. Kullanıcının `~/.claude/settings.json` dosyası gelmez. Sunucudan yönetilen ayarlar gelir.
- **C~:** Ayar dosyası oturum ortasında değişirse yeniden yüklenir: "applies most edits to the running session without a restart, including edits to `permissions`, `hooks`" (SET). Bu, R01'in açık sorusunu belge düzeyinde yanıtlıyor; cloud'da denenmedi.
- **C?:** Proje alt ajanlarının frontmatter hook'ları için şu şart var: "run only after you accept the workspace trust dialog … A `-p` session doesn't count as accepting it" (HR).
  - Cloud oturumunun güven durumu belgelenmemiş.
  - Cg: `~/.claude.json`'da güven kaydı yok.
  - Çıkarım: cloud'da bu hook'lar çalışmayabilir.
  - Belgelenmiş bir karşılık var: ayar dosyasındaki hook'lar alt ajan içinde de çalışır ve girdide `agent_id` ile `agent_type` alanları bulunur (HR). Role özel kural böylece ayar dosyasından, `agent_type`'a bakarak uygulanabilir.
- **C~:** Proje skill'lerinin frontmatter hook'ları, ayar dosyası kuralına uyar ve oturumun geri kalanında kayıtlı kalır; `once: true` seçeneği var (HR).
- **Cg:** Ortamın kendi `Stop` hook'u, commit edilmemiş ya da push edilmemiş değişiklikte turun bitmesini engelliyor (`launcher-settings.json`).

#### Standart seviye kontrol listesi

**BZ-1 · Her "asla" ve "her zaman" kuralı için zorlama kararı verilir.**
- **Ne:** Her kural için bir kayıt tutulur:
  - kural tavsiye mi, zorlama mı;
  - zorlamaysa korunmak istenen etkiye giden yollar hangileri.
- **Kanıt:** "When there's something that absolutely must not happen, an instruction is the wrong tool. Claude will follow the instruction most of the time, but when under pressure, in a long session or an ambiguous situation, or due to a prompt injection in a file accessed as part of the task, the model can fail to follow a prompted rule." (BLOG; T). R04 aynı ayrımı Foundation'dan çıkarmıştı.
- **Cloud:** C! Zorlamanın bir kısmı yalnız tek repolu oturumda çalışır.
- **Yokluğunda:** A003'teki gibi kural kâğıtta kalır; EXP-006'nın E3 kayması yinelenir (R02).
- **Bedel:** Kayıt tutma. Her kural zorlanmaz (BZ-7).
- **Gereksiz:** Yok.

**BZ-2 · Yazma sınırı ve tehlikeli eylem engeli vardır.**
- **Ne:**
  - `PreToolUse` hook'u ya da izin `deny` kuralı. Örnekler: işçi yalnız kendi çıktı dosyasına yazar; kontrol katmanı ve EXP-006 dosyalarına yazılmaz; `git push` yalnız koordinatörden yapılır.
  - Rol dosyasında araç sınırı (BR-4).
- **Kanıt:**
  - "To block an action regardless of what Claude decides, use a PreToolUse hook instead." (MEM)
  - Çok hook'un kararı: "the most restrictive answer applies, in the order `deny`, `defer`, `ask`, `allow`" (HG).
  - Etiket: kaynak diyor, T.
- **Cloud:** C! Yalnız tek repolu oturumda (CENV).
- **Yokluğunda:** "Yalnız oku" gibi sınırlar düz yazıyla korunur. Bu notun kendi görev tanımı da öyle (gözledim).
- **Bedel:** Betik bakımı, yanlış engelleme riski, A-04 onayı.
- **Gereksiz:** Etkinin geri alınabilir ve düşük maliyetli olduğu durumlarda. Git çoğu dosya hatasını geri alır; asıl risk dal ve dış etkilerde (çıkarım).

**BZ-3 · Bitiş kapıları vardır.**
- **Ne:** `Stop` ve `SubagentStop` hook'ları mekanik koşulları sınar:
  - alt ajanın son mesajında zorunlu başlıklar var mı;
  - çıktı dosyası yazılmış mı;
  - STATE güncellenmiş ve commit edilmiş mi.

  Kapının kendisi de sınanır: döngü koruması ve 8'li sınır.
- **Kanıt:**
  - "a Stop hook runs your check as a script and blocks the turn from ending until it passes" (BP)
  - `SubagentStop` girdisinde `last_assistant_message` alanı (HR)
  - Etiket: kaynak diyor, T.
- **Cloud:** C! Tek repolu oturumda. Cg: ortamın git kontrolü zaten böyle bir kapı.
- **Yokluğunda:** "Tamam" iddiası mekanik kontrolsüz kalır; §2.8'deki erken zafer ilanı riski artar.
- **Bedel:**
  - Yanlış kurulan kapı sonsuz devam üretir; sınır ve `stop_hook_active` gerekir.
  - `Stop` her yanıtta çalışır, maliyeti vardır.
- **Gereksiz:** Kontrol mekanik değilse, yani yargı gerektiriyorsa. O zaman `prompt` ya da `agent` hook'u, ya da ayrı değerlendirici (BD-3) kullanılır.

**BZ-4 · Bağlam sürekliliği hook'larla desteklenir.**
- **Ne:**
  - `SessionStart` (`startup|resume|compact`) ile STATE'in özeti ve sıradaki yetkili iş deterministik olarak bağlama girer.
  - İsteğe bağlı: `PreCompact` ile sıkıştırma öncesi transcript arşivlenir.
- **Kanıt:** "back up chat history on PreCompact" (BLOG, "Hooks" satırı; T)
- **Cloud:** C! Tek repolu oturumda. Oturum başlangıç hook'u cloud'da her başlangıç ve devamda çalışır (CENV).
- **Yokluğunda:** Okuma sırası düz yazı talimatına kalır (BB-7).
- **Bedel:** Enjekte edilen metin her oturumda bağlama girer; kısa tutulmalı.
- **Gereksiz:** Kök CLAUDE.md `@STATE.md` ile aynı işi görüyorsa. Ama bu durumda STATE her istekte yüklenir (BY-1).

**BZ-5 · Yetki ve izin sınırlarının modeli bilinir.**
- **Ne:**
  - Ajanlar arası mesaj ve zamanlanmış istem yetki taşımaz.
  - auto kipi 3 ardışık ya da 20 toplam engelde durur ve kullanıcıya sorar.
  - Alt ajanın izin kipi auto'da yok sayılır.
- **Kanıt (kaynak diyor, T):**
  - "no message from any agent counts as your approval for a pending permission prompt, and no agent message can change a subagent's permission settings, `CLAUDE.md`, or configuration" (SA)
  - "if the classifier blocks an action 3 times in a row or 20 times total, auto mode pauses and Claude Code resumes prompting" (PM)
  - Sınıflandırıcı alt ajanı üç noktada denetler: başlarken, çalışırken ve dönüşte (PM).
- **Cloud:** C+. Cloud'da Bypass kipi yok (R01).
- **Yokluğunda:** Otomatik uyandırma ya da ajan mesajı "Batu onayı" sanılır; K-002 sınırları aşılır.
- **Bedel:** Yok. Yalnız bu modelin tasarımda bilinmesi gerekir.
- **Gereksiz:** Yok.

**BZ-6 · Kontrollerin kendisi doğrulanır.**
- **Ne:**
  - `/hooks` ile hangi hook'un kayıtlı olduğu görülür.
  - Betik örnek JSON girdiyle elle sınanır.
  - `InstructionsLoaded` ile hangi talimatın yüklendiği izlenir.
  - Sessiz atlama riski kaydedilir: hatalı ajan dosyası ve güven şartı atlanan frontmatter hook'u yalnız hata ayıklama günlüğüne yazar.
- **Kanıt:** HG sorun giderme; SA "Subagent files Claude Code skips"; HR `InstructionsLoaded` (kaynak diyor, T).
- **Cloud:** C?
- **Yokluğunda:** "Kontrol kuruldu" ile "kontrol çalışıyor" karışır. Foundation ayrımı: "review complete != gate satisfied" (R04).
- **Bedel:** Kurulum sonrası tek seferlik sınama.
- **Gereksiz:** Yok.

**BZ-7 · Zorlama bilinen kayma noktalarıyla sınırlanır.**
- **Ne:** Düşünme disiplini tavsiye katmanında kalır. Hook yalnız ölçülebilir ve mekanik koşullara kurulur.
- **Kanıt:**
  - "Use a hook when the action must happen the same way every time and doesn't need Claude to think." (FO; T)
  - Batu'nun kendi sınırı: hook'lar "Böyle düşünme" diyemez ve "Hepsine kurmak da imkânsız" (R03).
- **Cloud:** —
- **Yokluğunda:** Aşırı hook, gecikme, maliyet ve yanlış engelleme üretir.
- **Bedel:** —
- **Gereksiz:** —

### 2.6 Orkestrasyon

**Anthropic'in önerisi:**
- **Desenler (E-BEA):**
  - prompt chaining (programatik kapılarla);
  - routing;
  - paralelleştirme (bölümleme ve oylama);
  - orkestratör–işçi ("a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results");
  - değerlendirici–iyileştirici;
  - ajanlar.
- **Durma koşulu:** "it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control" (E-BEA).
- **Araştırma sistemi (E-MARS):**
  - Lider ajan strateji kurar, planını belleğe kaydeder ve paralel alt ajanlar açar.
  - Bir CitationAgent kaynak atfını ayrıca yapar.
  - "The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated".

**Claude Code mekanizmaları** (WF, AT, PRJ, SA; ayrıntı ve cloud koşulları R01'de):

| Mekanizma | Planı kim tutar | Ara sonuçlar | Cloud |
|---|---|---|---|
| Alt ajan | Claude, tur tur | Ana bağlam (özet) | C+. Cg: derinlik 1 |
| Dinamik workflow | Betik | Betik değişkenleri | C+. Sonuçlar oturumla saklanır; çalışırken kullanıcı girdisi yok |
| Agent teams | Lider | Ortak görev listesi | C+ ortam değişkeniyle; deneysel. Plan onayı "without the lead reviewing it" (AT) |
| Projects | Koordinatör konuşma | Thread raporları ve proje belleği | C+ (Pro/Max beta). Hesapta var mı bilinmiyor |

**Görev tanımında neler olmalı** (birleşik standart; kaynak diyor, T):
- **Hedef, çıktı biçimi, araç ve kaynak rehberi, net sınırlar (E-MARS):** "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries. Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."
- **Efor bütçesi ve iş bölümü (E-MARS):** "frameworks for collaboration that define the division of labor, problem-solving approaches, and effort budgets".
- **Projects'in thread'lere verdiği brifin beş parçası (PRJ):**
  - işin amacı;
  - nerede çalışılacağı;
  - thread'in "bitti" demeden önce kendi işini nasıl kontrol edeceği;
  - gereken bir şey eksikse ne yapacağı: "say exactly what's missing in your first message and stop. Don't substitute, mock, or guess.";
  - neyin onay gerektirdiği.
- **Başarının ve sonuçla ne yapılacağının açıkça yazılması (CWF):** "The task runs autonomously, so it can't ask clarifying questions."
- **Kendine yeten spec (BP):** "name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step".
- **Ana bağlamda olup alt ajana taşınmayanlar (SA):** konuşma geçmişi, auto memory, output style. Kritik kural delegasyon mesajında yinelenir.

#### Standart seviye kontrol listesi

**BO-1 · Orkestratör ile işçi ayrıdır; plan kalıcıdır.**
- **Ne:** Orkestratör planı dosyaya yazar, işi böler ve sentezi yapar. İşçi dar bir işi yapar.
- **Kanıt:** E-MARS mimarisi; "saving its plan to Memory" (kaynak diyor, T).
- **Cloud:** C+. Cg: derinlik 1 olduğu için yalnız ana oturum orkestratör olabilir.
- **Yokluğunda:** Plan yalnız koordinatörün bağlamında kalır ve sıkıştırmada kaybolur (BY-4).
- **Bedel:** Plan dosyasının bakımı.
- **Gereksiz:** Tek adımlık işlerde.

**BO-2 · Görev tanımı şablonu standarttır.**
- **Ne:** Yukarıdaki birleşik liste bir skill ya da şablon olarak tutulur.
- **Kanıt:** yukarıda.
- **Cloud:** C~.
- **Yokluğunda:** Mükerrer iş, boşluk ve yanlış yorum doğar. E-MARS örneği: üç işçinin ikisi aynı konuyu aradı.
- **Bedel:** Şablon bakımı.
- **Gereksiz:** Yok.

**BO-3 · Efor ölçeklenir ve fazla delegasyon frenlenir.**
- **Ne:** İşin karmaşıklığına göre ajan ve araç çağrısı sayısı kuralı konur. Paralel ajan sayısına üst sınır konur.
- **Kanıt:**
  - "Simple fact-finding requires just 1 agent with 3-10 tool calls, direct comparisons might need 2-4 subagents with 10-15 calls each, and complex research might use more than 10 subagents with clearly divided responsibilities." (E-MARS)
  - "Early agents made errors like spawning 50 subagents for simple queries" (E-MARS)
  - "Claude Opus 5 delegates to subagents more readily than prior models. Delegation pays off on genuinely independent, sizeable tracks of work, but it multiplies cost and time when applied to small tasks." (P-O5)
  - Deterministik sınırlar: `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (P-O5, SA).
  - Workflow 25 ajanı ya da 1,5 milyon tokeni aşınca "Large workflow" uyarısı verir (WF).
  - Etiket: kaynak diyor, T ve Tö.
- **Cloud:** C+. Ortam değişkeni cloud ortam ayarından verilebilir; ancak derinlik değerinin ortam tarafından sabitlenip sabitlenmediği bilinmiyor (C?).
- **Yokluğunda:** Haftalık limit tükenir (R01: "A single burst of heavy activity … can exhaust the weekly allowance"). Maliyet ile değer ilişkisi görünmez.
- **Bedel:** Kural yazmak. Yanlış düşük sınır derinliği keser.
- **Gereksiz:** Yok.

**BO-4 · Paralellik bağımsızlığa bağlıdır.**
- **Ne:**
  - Yalnız birbirinden bağımsız işler paralelleştirilir.
  - Aynı dosyaya iki yazıcı konmaz. Gerekiyorsa her yazıcı kendi çalışma ağacında çalışır ya da kilit dosyası kullanılır.
  - Hepsinin aynı engele yığılması izlenir.
- **Kanıt (kaynak diyor, T):**
  - "Two teammates editing the same file leads to overwrites." (AT)
  - "Every agent would hit the same bug, fix that bug, and then overwrite each other's changes." (E-CC)
  - Kilit: "Claude takes a "lock" on a task by writing a text file to current_tasks/" (E-CC)
- **Cloud:** `isolation: worktree` için C~.
- **Yokluğunda:** Çakışan yazmalar ve "hareket var, ilerleme yok" durumu.
- **Bedel:** İşi bölme tasarımı.
- **Gereksiz:** Tek yazıcı varsa. P0'da yalnız ana oturum ortak dosyaları yazıyor (gözledim).

**BO-5 · Sonuç sıkıştırılarak döner; ayrıntı dosyada kalır.**
- **Ne:** Sabit dönüş biçimi kullanılır. Ayrıntı dosyaya yazılır, koordinatöre referans döner.
- **Kanıt:** "Subagent output to a filesystem to minimize the 'game of telephone.'" (E-MARS; T)
- **Cloud:** Cg: P0'da uygulanıyor.
- **Yokluğunda:** Bilgi her aktarımda aşınır (R05 madde 17). Koordinatörün bağlamı dolar.
- **Bedel:** Dosya disiplini. Çok sayıda not dosyası repoyu ağırlaştırır (R02: 53 bin kelime).
- **Gereksiz:** Dönüş zaten kısaysa.

**BO-6 · Önce küçük dilim, sonra hepsi.**
- **Ne:** Yeni bir görev tanımı ya da yelpaze önce bir iki örnekte denenir; sonra bütününe uygulanır.
- **Kanıt (kaynak diyor, T):**
  - "Refine your prompt based on what goes wrong with the first 2-3 files, then run on the full set." (BP)
  - "Fix the gap once, in project instructions or the environment, then send one thread before sending the rest" (PRJ)
  - "run the workflow on a small slice first" (WF)
- **Cloud:** C~.
- **Yokluğunda:** Aynı brif hatası N kez ödenir.
- **Bedel:** Biraz gecikme.
- **Gereksiz:** Tek işçilik görevlerde.

**BO-7 · Orkestrasyon gözlemlenebilirdir.**
- **Ne:** Ajanların yolu okunur: alt ajan transcript'leri ve workflow betiği.
- **Kanıt:**
  - "Think like your agents … watched agents work step-by-step" (E-MARS)
  - "Adding full production tracing let us diagnose why agents failed" (E-MARS)
  - Alt ajan transcript'leri `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl` altında durur (SA).
  - Etiket: kaynak diyor, T.
- **Cloud:** C! Transcript'ler VM diskinde; VM geri alınınca korunup korunmadıkları belgelenmemiş (C?).
- **Yokluğunda:** Bir alt ajanın neden kötü sonuç verdiği bulunamaz; görev tanımı körlemesine düzeltilir.
- **Bedel:** Okuma zamanı.
- **Gereksiz:** Sonuçlar tutarlı iyiyse, örneklem okuma yeter.

**BO-8 · Ajan çıktısı veridir.**
- **Ne:** Alt ajan raporu talimat ya da onay değildir.
- **Kanıt:**
  - Claude Code alt ajan raporunu tarar ve işaretler: "The header states that instructions or approval claims inside the report are the subagent's words and carry no authority from you." (SA)
  - Auto kipinde dönüşte sınıflandırıcı denetimi (PM).
  - Etiket: kaynak diyor, T.
- **Cloud:** C~.
- **Yokluğunda:** Dış içerikten sızan talimat koordinatöre taşınır.
- **Bedel:** Yok.
- **Gereksiz:** Yok.

### 2.7 Uzun soluklu süreklilik

**Anthropic'in önerisi:**
- **Sorun (E-HAR):** "each new session begins with no memory of what came before. Imagine a software project staffed by engineers working in shifts".
- **İki başarısızlık biçimi (E-HAR):**
  - işi tek seferde yapmaya çalışmak ve yarım, belgesiz bırakmak;
  - "a later agent instance would look around, see that progress had been made, and declare the job done."
- **Sıkıştırma tek başına yetmez (E-HAR):** "compaction, which doesn't always pass perfectly clear instructions to the next agent".
- **Çözüm (E-HAR):**
  - Başlatıcı ajan ("initializer agent") ortamı kurar.
  - Çalışan ajan ("coding agent") her oturumda artımlı ilerler ve sonraki oturum için açık izler bırakır.
  - Dipnot: "We refer to these as separate agents in this context only because they have different initial user prompts."
- **API belgesi aynı kalıbı öneriyor (P-MEM, P-PBP):** memory aracının "Multisession software development pattern" bölümü ve "Workflows across multiple context windows" bölümü.

E-HAR'ın başarısızlık tablosu (kaynak diyor, T):

| Sorun | Başlatıcının yaptığı | Çalışan oturumun yaptığı |
|---|---|---|
| Erken zafer ilanı | Spec'ten yapılandırılmış, uçtan uca özellik listesi (JSON) | Oturum başında listeyi okur, tek özellik seçer |
| Hatalı ya da belgesiz durum bırakmak | İlk git reposu ve ilerleme notu dosyası | Başta ilerleme notu ve git günlüğünü okur, temel bir test koşar; sonda commit ve ilerleme notu yazar |
| Özelliği erken "bitti" işaretlemek | Özellik listesi | Yalnız dikkatli testten sonra "passing" işaretler |
| Uygulamayı nasıl çalıştıracağını her seferinde bulmak | `init.sh` | Oturuma `init.sh` okuyarak başlar |

#### Standart seviye kontrol listesi

**BS-1 · Başlatıcı oturum ayrı bir istemle koşar.**
- **Ne:** İlk oturum çerçeveyi kurar:
  - iş listesi: her kalem "passes: false" ya da açık durumda;
  - ilerleme dosyası;
  - kurulum ve başlatma betiği;
  - ilk commit.
- **Kanıt:**
  - "Use a different prompt for the very first context window: Use the first context window to set up a framework (write tests, create setup scripts), then use future context windows to iterate on a todo-list." (P-PBP)
  - E-HAR yukarıda.
  - Etiket: kaynak diyor, T.
- **Cloud:** C~. Cloud'da oturum başlatan bir koordinatörün (Projects ya da Remote araçları) başlatıcıyı ayrı istemle açması mümkün görünüyor; denenmedi (çıkarım).
- **Yokluğunda:** Her oturum işi yeniden tanımlar. EXP-006'daki "her tur bir sonrakini belirledi" kayması budur (R02).
- **Bedel:** İlk oturumun büyük bir kısmı kuruluma gider.
- **Gereksiz:** İş tek oturuma sığıyorsa.

**BS-2 · Çalışan oturum "yönünü bul" rutiniyle başlar.**
- **Ne:** Sabit başlangıç adımları:
  1. Çalışma dizinini doğrula (`pwd`).
  2. İlerleme dosyasını ve git günlüğünü oku.
  3. İş listesinden en öncelikli açık kalemi seç.
  4. Temel doğrulamayı koş.
- **Kanıt:**
  - E-HAR "Getting up to speed" adımları.
  - "Be prescriptive about how it should start: "Call pwd …" "Review progress.txt, tests.json, and the git logs."" (P-PBP)
  - Etiket: kaynak diyor, T.
- **Cloud:** C~. Rutin bir skill olabilir; `SessionStart` hook'u ile tetiklenebilir (BZ-4).
- **Yokluğunda:** Devir notu doğrulanmadan kabul edilir. R05 madde 15: "checkpoint exists + is newest ≠ checkpoint claims are still current truth".
- **Bedel:** Her oturumda birkaç araç çağrısı.
- **Gereksiz:** Yok.

**BS-3 · İlerleme artımlıdır; her artım commit'le kapanır.**
- **Ne:**
  - Oturumda tek bir iş kalemi yapılır.
  - Sonunda descriptive commit ve ilerleme notu yazılır.
  - Oturum "temiz durum"da bırakılır: bir sonraki oturum önce dağınıklık toplamak zorunda kalmamalıdır.
- **Kanıt:**
  - "the best way to elicit this behavior was to ask the model to commit its progress to git with descriptive commit messages and to write summaries of its progress in a progress file" (E-HAR)
  - "Use git for state tracking" (P-PBP)
  - Etiket: kaynak diyor, T.
- **Cloud:** C+. "On long tasks, ask Claude to commit and push work in progress." (PRJ). Cg: ortamın `Stop` hook'u commit ve push'u zorluyor.
- **Yokluğunda:**
  - VM geri alındığında yarım iş kaybolur (R01).
  - Git'le geri dönme imkânı kalmaz.
- **Bedel:** Commit sayısı artar. EXP-006'da 36 commit/6 dakika gibi kırıntılaşma riski var (R02). Commit, anlamlı bir artım olmalıdır.
- **Gereksiz:** Yok.

**BS-4 · Durum yapılandırılmıştır.**
- **Ne:**
  - Makinece okunacak durum yapılandırılmış biçimde tutulur (JSON): iş listesi, test ya da kabul durumu.
  - Serbest ilerleme notu ayrı tutulur.
  - Koruma cümlesi eklenir: kalemler yalnız durum alanı değiştirilerek güncellenir.
- **Kanıt (kaynak diyor, T):**
  - "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files" (E-HAR)
  - "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality." (E-HAR, P-PBP)
  - "Use structured formats for state data … Use unstructured text for progress notes" (P-PBP)
- **Cloud:** C~.
- **Yokluğunda:** Model kapsamı sessizce daraltır ya da kalemi siler. R05 madde 8'deki "never reordered, renumbered, deleted" kuralı bunun karşılığı.
- **Bedel:** Batu'nun okuması için Markdown görünümü gerekir; iki biçimin tutarlılığı sağlanmalıdır (çıkarım).
- **Gereksiz:** Kalem sayısı çok azsa.

**BS-5 · Devir kendine yeter; temiz bağlam tercih edilebilir.**
- **Ne:** Devir ya da spec dosyası tek başına yeterli olur. Uygulama temiz oturumda yapılır.
- **Kanıt:**
  - "Context resets—clearing the context window entirely and starting a fresh agent, combined with a structured handoff that carries the previous agent's state and the next steps" (E-HD)
  - "The most useful specs are self-contained" (BP)
  - Etiket: kaynak diyor, T.
- **Cloud:** C! `/clear` yok; sıfırlama = yeni oturum (WEB).
- **Yokluğunda:** Koordinatör oturumu sonsuza dek sıkıştırılarak yaşar; erken kararlar özetlerde aşınır.
- **Bedel:** Devir yazma ve yeni oturumun başlangıç maliyeti. Ayrıca bir saati aşan aradan sonra önbellek soğur ve pahalanır (PC).
- **Gereksiz:** Model uzun oturumda tutarlı kalıyorsa. E-HD Opus 4.5+ ile sıfırlamayı kaldırdı; seçim modele bağlı.

**BS-6 · Cloud'a özgü süreklilik önlemleri alınır.**
- **Ne:**
  - VM geri alınınca yarım kalan alt ajanlar kaybolur. Bu yüzden görev tanımları repoda tutulur ve eksik iş aynı tanımla yeniden başlatılır. EXP-007 STATE bunu zaten yapıyor (gözledim).
  - Uzun işi oturum dışından uyandırma yolları vardır: Projects, routines, `send_later` ve `claude -p --cloud`. Ayrıntı ve koşullar R01'de.
- **Kanıt:** R01 (C+, CENV, WEB).
- **Cloud:** C+.
- **Yokluğunda:** Batu "devam" yazan gizli koordinatör olur (K-001).
- **Bedel:** R01'deki denemeler ve yetki kaydı.
- **Gereksiz:** Yok.

**BS-7 · Durma ve devam koşulu ölçülebilir yazılır.**
- **Ne:** `/goal` ya da `Stop` kapısı kullanılıyorsa koşul şöyle yazılır:
  - tek bir ölçülebilir son durum;
  - bunun nasıl kanıtlanacağı;
  - korunacak kısıtlar;
  - tur ya da zaman sınırı.
- **Kanıt:** "One measurable end state … A stated check … Constraints that matter"; "include a turn or time clause in the condition, such as `or stop after 20 turns`" (GOAL; T).
- **Cloud:** C? `/goal`'ün cloud'da çalışıp çalışmadığı R01'de açık.
- **Yokluğunda:** Otomatik devam, ilerlemesiz harekete dönüşür. R01'deki kanon bekçisi 742 kez koştu ama "54 gündür kod yok" demedi.
- **Bedel:** Değerlendirici tokenleri.
- **Gereksiz:** Otomatik devam kullanılmıyorsa.

### 2.8 Doğrulama

**Anthropic'in önerisi:**
- **Kapının sertliği dört düzeyde seçilir (BP):**
  - aynı istemde;
  - `/goal` koşuluyla;
  - `Stop` hook'u ile deterministik kapı;
  - "By a second opinion: a verification subagent or a dynamic workflow that checks its own findings has a fresh model try to refute the result, so the agent doing the work isn't the one grading it."
- **Öz-değerlendirme cömerttir (E-HD):** "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work … particularly pronounced for subjective tasks like design".
- **Ayrı değerlendiricinin de sınırı vardır (E-HD):**
  - "Out of the box, Claude is a poor QA agent. In early runs, I watched it identify legitimate issues, then talk itself into deciding they weren't a big deal and approve the work anyway."
  - "tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work".
- **Opus 5 için karşı uyarı (P-O5):** "If your prompt contains explicit verification instructions ("include a final verification step for any non-trivial task," "use a subagent to verify"), remove them: instructions like these cause over-verification on Claude Opus 5".
  - Aynı sayfa "effective writer-verifier patterns" ifadesini de kullanıyor.
  - Uzlaştırma (çıkarım): genel "yeniden kontrol et" talimatı kaldırılır. Ayrı değerlendirici hedefli kullanılır.
- Etiket: kaynak diyor, T.

#### Standart seviye kontrol listesi

**BD-1 · "Bitti" işten önce ve koşulabilir biçimde tanımlıdır.**
- **Ne:** Koşulabilir bir kontrol ve kabul ölçütü yazılır. Uzun işte her dilim için üreten ile değerlendiren "bitti"de önceden anlaşır: *sprint contract*.
- **Kanıt:**
  - "Give Claude a check it can run: tests, a build, a screenshot to compare." (BP)
  - "Before each sprint, the generator and evaluator negotiated a sprint contract: agreeing on what "done" looked like for that chunk of work before any code was written." (E-HD)
  - Etiket: kaynak diyor, T.
- **Cloud:** C~.
- **Yokluğunda:** "Görünüşte bitti" tek sinyal olur ve Batu doğrulama döngüsüne dönüşür (BP). Bu, K-001 ve D003 ile çelişir.
- **Bedel:**
  - Tasarım işinde koşulabilir kontrol azdır. Ölçütler çoğu zaman "denetlenebilir ifadeler"e çevrilmek zorunda (E-HD: "turn subjective judgments … into concrete, gradable terms").
  - Çıkarım: bu çeviri başlı başına bir iş.
- **Gereksiz:** Yok.

**BD-2 · Kanıt gösterilir, başarı iddia edilmez.**
- **Ne:** Çıktı kanıtıyla gelir: koşulan komut ve sonucu, alıntı, dosya yolu.
- **Kanıt:** "Have Claude show evidence rather than asserting success" (BP; T)
- **Cloud:** C~.
- **Yokluğunda:** Okuma iddiaları sınanamaz. EXP-006'da "tam okudum" iddiaları geri çekildi (R02).
- **Bedel:** Daha uzun dönüş. Ayrıntı dosyada tutulur (BO-5).
- **Gereksiz:** Yok.

**BD-3 · Değerlendirici ayrı, şüpheci ve kalibre edilmiştir.**
- **Ne:**
  - Taze bağlamda çalışır; yalnız ölçütü ve çıktıyı görür, üretenin gerekçesini görmez.
  - İstemi "şüpheci" ayarlanır.
  - Birkaç örnekle ve değerlendiricinin günlükleri okunarak insan yargısına kalibre edilir.
- **Kanıt:**
  - "A reviewer running in a fresh subagent context sees only the diff and the criteria you give it, not the reasoning that produced the change" (BP)
  - "I calibrated the evaluator using few-shot examples with detailed score breakdowns." (E-HD)
  - "read the evaluator's logs, find examples where its judgment diverged from mine, and update the QAs prompt" (E-HD)
  - Etiket: kaynak diyor, T.
- **Cloud:** C+ (alt ajan).
- **Yokluğunda:** A003'ün kendi teşhisi yinelenir: "değerlendirme kendini onayladı".
- **Bedel:**
  - Kalibrasyon işi.
  - Aynı model olduğu için bağımsızlık sınırlıdır. R04 ve R06: "new context window ≠ independent model".
- **Gereksiz:** Görev modelin tek başına güvenilir yaptığı alandaysa: "the evaluator is not a fixed yes-or-no decision. It is worth the cost when the task sits beyond what the current model does reliably solo." (E-HD)

**BD-4 · Ölçütler somut, eşikler serttir; "bilmiyorum" çıkışı vardır.**
- **Ne:**
  - Rubrik ve her ölçüt için bir eşik; biri eşiğin altındaysa iş geçmez.
  - Değerlendiriciye "Unknown" deme hakkı verilir.
  - Boyutlar ayrı değerlendirilir.
- **Kanıt:**
  - "Each criterion had a hard threshold, and if any one fell below it, the sprint failed" (E-HD)
  - "give the LLM a way out, like providing an instruction to return "Unknown" when it doesn't have enough information" (E-EVAL)
  - "grade each dimension with an isolated LLM-as-judge rather than using one to grade all dimensions" (E-EVAL)
  - Araştırma rubriği: "factual accuracy … citation accuracy … completeness … source quality … tool efficiency"; tek çağrıda 0.0–1.0 puan ve pass/fail "the most consistent" (E-MARS).
  - Etiket: kaynak diyor, T ve Tö.
- **Cloud:** C~.
- **Yokluğunda:** Değerlendirici sorunu görür ama "önemsiz" sayıp onaylar (E-HD).
- **Bedel:** Rubrik tasarımı. Ölçütün dili üretimi de yönlendirir: "the wording of the criteria steered the generator" (E-HD).
- **Gereksiz:** Yok.
- **Kaynaklar arası gerilim:** E-MARS tek çağrılı yargıcı en tutarlı buldu (2025, araştırma). E-EVAL boyut başına ayrı yargıç öneriyor (2026, genel). Bu not hangisinin EXP-007'ye uyduğunu çözmüyor.

**BD-5 · Değerlendirici bulguları triyajdan geçer.**
- **Ne:** Değerlendirici yalnız doğruluğu ya da yazılı gereksinimi etkileyen boşlukları bildirir. Geri kalanı isteğe bağlıdır. Her bulguya bir karar kaydedilir.
- **Kanıt:** "A reviewer prompted to find gaps will usually report some, even when the work is sound … Chasing every finding leads to over-engineering … Tell the reviewer to flag only gaps that affect correctness or the stated requirements" (BP; T)
- **Cloud:** C~.
- **Yokluğunda:** Sonsuz düzeltme ve şişen yapı. A003'teki "en fazla üç eleştiri turu" sınırı bunun bir yarısı.
- **Bedel:** Karar kaydı.
- **Gereksiz:** Yok.

**BD-6 · Uç durumlar ayrıca aranır.**
- **Ne:**
  - Spec'e uç durumlar yazılır.
  - Değerlendiricinin yüzeysel test eğilimi bilinir.
  - Rakip hipotezler kurulur.
  - İnsan testi otomatiğin kaçırdığını yakalar.
- **Kanıt (kaynak diyor, T):**
  - "It also tended to test superficially, rather than probing edge cases" (E-HD)
  - "People testing agents find edge cases that evals miss." (E-MARS)
  - "a single agent tends to find one plausible explanation and stop looking … teammates explicitly adversarial" (AT)
  - "develop several competing hypotheses. Track your confidence levels" (P-PBP)
- **Cloud:** C~.
- **Yokluğunda:** BP'nin "trust-then-verify gap" dediği şey: "Claude produces a plausible-looking implementation that doesn't handle edge cases."
- **Bedel:** Ek değerlendirme turu.
- **Gereksiz:** Düşük riskli, geri alınabilir işlerde.

**BD-7 · Doğrulamanın ağırlığı riske orantılıdır.**
- **Ne:** Doğrulama riske ve geri alınabilirliğe göre ölçeklenir. Genel "yeniden kontrol et" talimatı verilmez.
- **Kanıt:**
  - P-O5 (yukarıda).
  - "Consider the reversibility and potential impact of your actions." (P-PBP)
  - "The longer Claude works unattended, the more an independent check matters before you count the work as done." (BP)
  - Etiket: kaynak diyor, T.
- **Cloud:** C~.
- **Yokluğunda:** Ya her şeye tören yapılır (maliyet, limit) ya da hiçbir şey sınanmaz.
- **Bedel:** Risk sınıflandırması.
- **Gereksiz:** Yok.

**BD-8 · Değerlendirmenin kendisi değerlendirilir.**
- **Ne:**
  - Küçük bir örnek setiyle erken başlanır (yaklaşık 20 görev).
  - Transcript'ler okunur.
  - Puanlar yüzeyden kabul edilmez.
  - Denemeler yalıtılır; önceki denemenin izleri sonrakini beslemez.
- **Kanıt (kaynak diyor, T ve Tö):**
  - "We started with a set of about 20 queries" (E-MARS)
  - "we do not take eval scores at face value until someone digs into the details of the eval and reads some transcripts" (E-EVAL)
  - "Claude gaining an unfair advantage on some tasks by examining the git history from previous trials" (E-EVAL)
  - "A good task is one where two domain experts would independently reach the same pass/fail verdict." (E-EVAL)
- **Cloud:** C~.
- **Yokluğunda:** Değerlendirici yanlış şeyi ölçer. R01'deki kanon bekçisi 742 kez koştu, ilerlemesizliği görmedi.
- **Bedel:** Okuma zamanı.
- **Gereksiz:** Değerlendirme tek seferlikse.

---

## 3. Anthropic'in açıkça uyardığı hatalar ve önlemleri

| Hata | Kaynak ve kısa alıntı | Anthropic'in önlemi | EXP-007'deki karşılığı |
|---|---|---|---|
| İlgisiz işleri aynı oturumda karıştırmak ("kitchen sink") | BP: "Context is full of irrelevant information." | `/clear` (cloud'da yeni oturum) | Koordinatör oturumunun her işi taşıması |
| Üst üste düzeltme | BP: "Context is polluted with failed approaches." | İki düzeltmeden sonra temiz oturum ve daha iyi istem | A003: "aynı görevi aynı tanımla ikinci kez göndermem" |
| Şişmiş CLAUDE.md | BP: "Claude ignores half of it" | Buda; gerekiyorsa hook'a çevir | AGENT.md 205 satır ve protokoller 1.908 satır (gözledim) |
| Doğrulamasız güven | BP: "doesn't handle edge cases" | Test, betik, ekran görüntüsü | Tasarım işinde koşulabilir kontrol azlığı |
| Kapsamsız keşif | BP: "reads hundreds of files" | Dar kapsam ya da alt ajan | Foundation ve studies okumaları |
| Tek seferde her şeyi yapmak | E-HAR: "attempt to one-shot the app" | Tek özellik / tek kalem | P0'ın 8 adıma bölünmesi uyumlu (gözledim) |
| Erken zafer ilanı | E-HAR: "declare the job done" | Açık durumlu iş listesi | Aşama "tamam" etiketleri |
| Testsiz "bitti" | E-HAR: "mark a feature as complete without proper testing" | Uçtan uca kontrol | Tamamlanma katları (A003 §3.8) |
| Bağlam kaygısı ve erken kapanış | E-HD: "wrapping up work prematurely" | Sıfırlama ya da bağlam bilgisi istemi | Model bağımlı |
| Öz-değerlendirmede cömertlik | E-HD: "confidently praising the work" | Ayrı ve şüpheci değerlendirici | EXP-006'nın kendini onaylaması (R02) |
| Sorunu görüp "önemsiz" sayan QA | E-HD: "talk itself into deciding they weren't a big deal" | Kalibrasyon ve sert eşik | Karşı-okuyucu |
| Değerlendiricinin her şeyde kusur bulması | BP: "Chasing every finding leads to over-engineering" | Yalnız doğruluk ve gereksinim bulguları | Eleştiri turu sınırı |
| Basit işe çok alt ajan | E-MARS: "spawning 50 subagents for simple queries"; P-O5 | Efor kuralları, sınırlar | A003 §6: 4 milyon token |
| Belirsiz görev tanımıyla mükerrer iş | E-MARS: "duplicate work, leave gaps" | Hedef, çıktı biçimi, kaynak, sınır | ORTAK ve görev tanımları |
| Var olmayan kaynağı sonsuza dek aramak | E-MARS: "scouring the web endlessly for nonexistent sources" | Durma kuralı | "Erişilemedi diye yaz" kuralı (ORTAK) |
| Düşük kaliteli kaynağa kayma | E-MARS: "SEO-optimized content farms" | Kaynak kalitesi sezgileri | Birincil kaynak kuralı |
| "Kulaktan kulağa" bilgi kaybı | E-MARS | Çıktı dosyaya, koordinatöre referans | P0'da uygulanıyor |
| Hataların birikmesi, baştan başlamanın pahalılığı | E-MARS: "errors compound" | Kaldığı yerden devam, düzenli kontrol noktası | VM geri alınması |
| Çalışan ajanlar sürerken sistemi değiştirmek | E-MARS: "rainbow deployments" | Sürüm geçişini yönetmek | Rol ya da görev tanımı değişirken çalışan alt ajan |
| Şişkin araç seti ve belirsiz araç seçimi | E-CTX: "bloated tool sets" | En küçük yeterli araç seti | Alt ajanlara açık Remote araçları (gözledim) |
| İsteme uç durum listesi doldurmak | E-CTX: "laundry list of edge cases" | Birkaç kanonik örnek | Görev tanımı yazımı |
| Aşırı sert ya da aşırı genel istem | E-CTX: "right altitude" | Orta düzey sezgiler | Rol gövdesi |
| Aşırı hevesli ve kapsam genişletme | P-PBP "Overeagerness"; P-O5 "can also expand the scope"; E-AUTO | Kapsam cümlesi, geri alınamaz eylemde sorma | Batu'nun "Durman gereken yerde dur" ilkesi (R03) |
| Aşırı doğrulama (Opus 5) | P-O5 | Genel doğrulama talimatını kaldırma | Her işe karşı-okuma töreni riski |
| Uzun rapor ve anlatım (Opus 5) | P-O5: "files … are often longer" | Uzunluk kalibrasyonu istemi | Batu'nun "tuğla gibi cevap" eleştirisi (R03) |
| Test geçirmeye odaklanıp kural atlamak | P-PBP: "hard-code values" | Genel çözüm istemi; yanlış testi bildirme | Ölçüte göre sonucu eğmek |
| Açılmamış dosya hakkında konuşmak | P-PBP: "Never speculate about code you have not opened" | Önce oku | Okuma kaydı |
| Zaman körlüğü | E-CC: "Claude can't tell time" | Seyrek ilerleme çıktısı, hızlı örneklem | Uzun okuma turları |
| Paralel ajanların aynı engele yığılması | E-CC | İşi bağımsız parçalara bölmek, oracle | Paralel araştırmacılar |
| Testler geçti diye bitti sanmak | E-CC: "it is easy to see tests pass and assume the job is done, when this is rarely the case" | İnsan kabulü | K-002: P4'te kabul Batu'da |
| Liderin kendisi işe girişmesi | AT: "Wait for your teammates to complete their tasks" | Bekleme talimatı | Koordinatörün kendi okuması |
| Ekibi uzun süre gözetimsiz bırakmak | AT: "increases the risk of wasted effort" | İzleme ve yönlendirme | "Hareket var, ilerleme yok" alarmı (A003) |
| Güvenilmeyen skill | E-SKILL | Denetim | — |
| Sonsuz Stop döngüsü | HR: 8'li sınır | `stop_hook_active` kontrolü | Otomatik devam |
| Çelişen talimatlar | MEM: "Claude may pick one arbitrarily" | Periyodik temizlik | AGENT.md ile EXP-007 kuralları |
| Harness varsayımlarının eskimesi | E-HD, E-MA | Yeni modelde bileşenleri tek tek sınamak | METHOD'un modele bağımlı parçaları |

---

## 4. Alt sistemler arası etkileşimler

Batu'nun ölçütü şuydu: bir alt sistemde "yeterli" görünen seçim ötekini yetersizleştirebilir. Anthropic kaynaklarından çıkan bağlar aşağıda. Hepsi, belgelerin birleştirilmesiyle yapılmış çıkarımdır.

1. **Rol belleği ↔ dal politikası ↔ yazma sınırı.** `memory: project` repoya yazar ve yazma araçlarını otomatik açar (SA).
   - Kalıcı olması için commit ve push gerekir (BB-2); K-009'daki dal politikası rol belleğini de bağlar.
   - Salt okur bir rolde bile yazma yolu açılır. Yazma sınırı (BZ-2) rol belleği dizinini ayrıca izinli kılmalıdır.
2. **Auto kipi ↔ rol izin kipi ↔ araç listesi.** Ana oturum auto kipindeyse rolün `permissionMode` alanı yok sayılır (SA). Rol sözleşmesinin tek zorlanan kısmı araç listesi ve hook'lardır. "Rol dosyası var, öyleyse kısıt var" varsayımı yanlış olur.
3. **Tek repo koşulu ↔ Projects ↔ bütün zorlama katmanı.** Repo `settings.json` hook'ları ve izin kuralları yalnız tek repolu oturumda okunur (CENV, PRJ).
   - Çok repolu bir Projects kurulumuna geçmek, BZ katmanının tamamını sessizce kapatır.
   - Proje talimatı ve proje belleği tavsiye katmanıdır: "They're instructions Claude keeps to, not enforced settings" (PRJ).
4. **CLAUDE.md düzenlemesi ↔ öğrenme döngüsü ↔ `/clear` yokluğu.** Oturum ortasındaki CLAUDE.md düzeltmesi uygulanmaz (PC). Cloud'da `/clear` yok. Ders ancak `/compact` ya da yeni oturumla etkili olur. BB-6'daki "davranış değişti mi" kontrolü, bir sonraki oturuma bağlanmalıdır.
5. **Skill bütçesi ↔ sıkıştırma ↔ uzun koordinatör oturumu.** Çok skill çağıran uzun oturumda en eski skill'ler sıkıştırmadan sonra düşer (SK, CW). Uzun koordinatör oturumu, prosedür katmanını da aşındırır. Temiz oturum kuralı (BY-5) prosedür güvenilirliğini de korur.
6. **`paths` alanlı rules ↔ sıkıştırma.** Dosyaya bağlı kurallar sıkıştırmada kaybolur (CW). Bağlam tasarrufu (BY-2) ile kuralın kalıcılığı arasında bir takas vardır. Her zaman geçerli olması gereken kural kök düzeyde durmalıdır.
7. **Alt ajana taşınmayanlar ↔ görev tanımı.** Konuşma geçmişi, auto memory ve output style alt ajana taşınmaz (SA). Koordinatörün sohbette öğrendiği her şey ya repoya ya da görev tanımına girmeli. Aksi halde bağlam yalıtımı (BY-3) bilgi kaybına dönüşür.
8. **Derinlik 1 ↔ orkestrasyon ↔ değerlendirme.** Bu ortamda işçi kendi doğrulayıcısını açamaz (Cg). Her karşı-okuma koordinatör üzerinden kurulur. Bu da koordinatörün bağlamını ve darboğaz riskini büyütür (A003 §6).
9. **Değerlendirici ↔ maliyet ↔ Opus 5.** Ayrı değerlendirici öz-değerlendirme cömertliğini azaltır (E-HD). Ancak Opus 5'te genel doğrulama talimatı aşırı doğrulama üretir (P-O5). Risk sınıflandırması (BD-7) hem kaliteyi hem haftalık limiti belirler.
10. **Gürültülü çıktı ↔ sıkıştırma döngüsü ↔ süreklilik.** Büyük araç çıktısı otomatik sıkıştırmayı durdurabilir (HOW). Bağlam hijyeni (BY-6) doğrudan sürekliliğin (BS) ön koşuludur.
11. **Hook çıktısı ↔ bağlam.** Hook'lar varsayılan olarak bağlam harcamaz. `SessionStart` ve `additionalContext` ise harcar (FO). Zorlama katmanını büyütmek bağlam katmanına geri yük bindirebilir.
12. **Ajan mesajı ve zamanlanmış istem ↔ yetki.** Ajanlar arası mesaj ve routine istemi onay sayılmaz (SA; R01: routines). Orkestrasyonu otomatikleştirmek (BS-6), Batu'nun yetki kapılarını (K-002) kendiliğinden açmaz. Kapılar repoda kayıtlı yetkiye bağlanmalıdır (R01).
13. **Output style ↔ alt ajanlar.** Output style alt ajana geçmez (SA). Bu, iletişim biçimi kuralının yalnız ana oturumu bağladığı anlamına gelir. Bu kural koordinatörün Batu'ya yazdığı mesajlar için belki yeterli, alt ajan raporları için değil.

---

## 5. A003 (v0) ile karşılaştırma

| Alt sistem | v0'da ne var | Karşıladığı | Eksik bıraktığı | Yanlış kurduğu ya da risk |
|---|---|---|---|---|
| Bağlam | "Ana oturum az okur, okumayı alt ajanlar yapar"; STATE tek ekran; "bir bilgi tek yerde durur" | BY-3 ve BY-7'nin özü (BP: "use subagents to investigate") | Sıkıştırma politikası (BY-4), temiz oturum kuralı (BY-5), ölçüm (BY-6), yükleme kademeleri (BY-2), CLAUDE.md boyut ve içerik kuralları (BY-1) | CLAUDE.md'yi "AGENT.md'ye yönlendiren kısa giriş" olarak kurmak: düz yazıyla yönlendirme okumayı garanti etmez (BB-7). `@AGENT.md` ise 205 satırla sınırı aşar |
| Bellek | "Repo bellektir; konuşma bellek değildir"; DECISIONS, sources, READING-LOG | BB-1 ve BB-2'nin ilkesi | Rol belleği (BB-3), güncelleme tetikleri (BB-4), budama (BB-5), CLAUDE.md değişikliğinin ne zaman etkili olduğu (BB-6), cloud kalıcılık tablosu | READING-LOG'un Anthropic kaynaklarında karşılığı yok. Anthropic'in karşılığı ilerleme dosyası ve git günlüğü. Değeri ve bedeli ölçülmeli (çıkarım) |
| Kalıcı roller | Beş geçici işçi türü; "üç tekrar → kalıcı tanım" | Tetik fikri, Anthropic'in kademeli yaklaşımıyla uyumlu (FO, SA) | `.claude/agents` dosyası, frontmatter, araç sınırı, model seçimi, rol belleği, sürüm | Tetik sağlandığı halde uygulanmadı: R02–R06 ve R07–R11 aynı türde işçi (gözledim). Roller sohbette tarif edilince her seferinde yeniden biçildi; U004 şikâyeti tam olarak bu |
| Prosedürler | Görev tanımında 9 alan, dönüş biçimi, okuma kaydı biçimi, plan revizyon kuralları | İçerik olarak zengin; E-MARS ve PRJ listesinin çoğunu karşılıyor | Hiçbiri skill değil; hepsi düz metin ya da bellekte. Efor bütçesi, "eksik bir şey varsa dur ve söyle", öz-kontrol ölçütü ve kanonik örnek görev tanımında yok | Yordamlar A003 metninde, yani bir sohbet dökümünde yaşıyor. Anthropic'e göre yordamın yeri skill (BP-1) |
| Zorlayıcı kontroller | Yok. Bütün kurallar yazılı söz | — | BZ-1…BZ-6'nın hepsi | v0 kendi teşhisinde "Yazılı kural davranışa dönüşmedi" dedi ama çözümü yine yazılı kural oldu. Standart seviyede bu tutarsızlık yanlış kurulum sayılır |
| Orkestrasyon | Koordinatör–işçi; tek soruluk görevler; sonuçlar veri; karar taşıyan iddialar kaynağından kontrol | BO-1, BO-5 (P0'da dosyaya yazma), BO-8 | Efor ölçekleme ve delegasyon freni (BO-3), paralellik ve çakışma kuralı (BO-4), önce küçük dilim (BO-6), gözlemlenebilirlik (BO-7), görev tanımına efor bütçesi | — |
| Süreklilik | Yeni oturum okuma sırası; devir notu git'le karşılaştırılır; soğuk başlangıç testi | BS-2'nin bir kısmı; soğuk başlangıç testi SK'nin "fresh session" ölçümüyle uyumlu | Başlatıcı/çalışan ayrımı (BS-1), yapılandırılmış iş listesi (BS-4), oturum başına tek artım ve temiz durum tanımı (BS-3), sıkıştırma mı sıfırlama mı kuralı (BS-5) | Okuma sırası tavsiye katmanında. `SessionStart` ya da `@` ile desteklenmedi |
| Doğrulama | Ölçüt önce; tamamlanma katları; karşı-okuyucu gerekçeyi görmez; "taze gözle karşı-okuma" adlandırması; kontrol riske orantılı | BD-1, BD-3'ün yarısı, BD-7; aynı modelin bağımsız olmadığı dürüstçe söylenmiş | Kalibrasyon, sert eşik, "Unknown" çıkışı (BD-3, BD-4), bulgu triyajı (BD-5), uç durum araştırması (BD-6), değerlendirmenin değerlendirilmesi (BD-8) | — |
| Uyarılar | Kendi eğilimleri: uzun yazma, kendini onaylama | Dürüst öz-teşhis | §3'teki listenin çoğu | — |

**Özet hüküm (çıkarım):**
- v0'ın yaklaşımı Anthropic'in ilkeleriyle büyük ölçüde örtüşüyor. Örtüşen ilkeler:
  - repo bellektir;
  - oturum geçicidir;
  - görev tanımı girdi kalitesini belirler;
  - yapan ile kontrol eden ayrıdır;
  - kontrol riske orantılıdır.
- Eksik olan, bu ilkelerin Claude Code'daki mekanizma karşılıklarıdır: ajan dosyası, skill, hook, rules, sıkıştırma politikası, rol belleği.
- Tek gerçek "yanlış kurulum", zorlama katmanının tamamen yokluğu. Bu da v0'ın kendi teşhisiyle çelişiyor.

---

## 6. EXP-006 P1-01 ve R01 ile karşılaştırma

### Örtüşenler
- **Cloud'a taşınanlar:** Repodaki CLAUDE.md, rules, agents ve skills cloud'a gelir; kullanıcı `~/.claude` gelmez. P1-01 E01/A02, R01 C8 ve CENV aynı şeyi söylüyor.
- **CLAUDE.md zorlama değildir:** P1-01 E05: "CLAUDE.md davranış girdisidir, teknik izin duvarı değildir". MEM ve BLOG ile tutarlı.
- **Auto memory yereldir:** P1-01 E05, R01 C10 ve MEM tutarlı. Cg: bu oturumda bellek dizini yok.
- **`/goal` değerlendiricisi araçsızdır:** P1-01 E06: "araçsız biçimde transcript'e bakar". GOAL ile tutarlı.
- **Agent teams planı incelemeden onaylanır:** P1-01 E03: "plan isteğinin … inceleme yapılmadan otomatik onaylandığını". AT'nin bugünkü metniyle tutarlı.
- **Stop hook sınırı:** R01'deki 8'li sınır HR ile tutarlı.

### Çelişenler ya da düzeltilmesi gerekenler
1. **Alt ajan iç içe açma.**
   - P1-01 E02: "eski 'alt ajan hiçbir alt ajan açamaz' genellemesi kullanılmaz".
   - Belge varsayılanı 3 katman (SA; v2.1.219+). BLOG (Haziran 2026) "up to five levels deep" diyor; bu, SA'ya göre v2.1.172–216 dönemine ait eski bilgi.
   - Bu ortamda derinlik 1 (Cg, R01). Yani EXP-007'nin gerçek ortamında eski genelleme fiilen doğru. P1-01 belgesel geneli, ortam gözlemiyle karıştırmamalı.
2. **Q03: eklenti çelişkisi.** P1-01, A02 ile A13'ün repo eklentileri konusunda çeliştiğini kaydetmişti. Bugünkü metinlerde çelişki yok. Üç sayfa aynı şeyi söylüyor:
   - CENV tablosu: "Plugins and marketplaces declared in your repo's `.claude/settings.json` | No";
   - SK cloud bölümü: "don't load in cloud sessions";
   - SET cloud bölümü.
   Ya sayfalar değişti ya da ChatGPT hattı yanlış okudu; hangisi olduğunu ayırt edemiyorum (bilinmiyor). Bugün için belgesel cevap: yüklenmez.
3. **Hook'ların cloud'daki geçerliliği.**
   - R01, ayar dosyası hook'larının tek repolu oturumda geçerli olduğunu doğru yazıyor.
   - Eksik bıraktığı şart: proje alt ajan frontmatter hook'ları çalışma alanı güvenine bağlı. `-p` bu güveni sağlamıyor (HR, PERM). Cloud'un güven durumu belirsiz; bu oturumda güven kaydı yok (Cg).
   - Bu yüzden R01 ve P1-01'in "rol hook'u" imasını koşullu okumak gerekir.
4. **R01'in açık sorusu: "Stop hook commit edilirse bu oturumda geçerli olur mu?"** SET, ayar dosyasındaki hook ve izin değişikliklerinin çalışan oturuma yeniden başlatmadan uygulandığını söylüyor. Soru belge düzeyinde yanıtlandı; cloud'da denenmedi (C~).

### P1-01'de eksik olanlar
- Projects ve routines hiç anılmıyor. R01 bunları çok oturumlu iş için belgelenmiş tek yol olarak buldu.
- Bağlam mekaniği yok: sıkıştırmada neyin kaldığı, skill bütçesi, CLAUDE.md'nin oturum ortasında uygulanmaması.
- Alt ajan `memory:` alanı, output style, auto kipinin rol izin kipini yok sayması, `agent_type` ile hook'ta rol ayrımı, ayar dosyasının yeniden yüklenmesi yok.
- Mühendislik yazılarındaki uzun iş dersleri yok: başlatıcı/çalışan oturum, değerlendirici–üretici, sıfırlama mı sıkıştırma mı.

Bu eksikler P1-01'in kapsamından kaynaklanıyor: P1-01 DevOS'un ortam haritası, Claude'un çalışma yöntemi değil.

### R01'de eksik olanlar
- Mühendislik yazıları ve yöntem katmanı: bağlam mühendisliği, skills, rol tasarımı, değerlendirici kalibrasyonu.
- Opus 5'e özgü delegasyon ve doğrulama uyarıları.
- Sıkıştırmada neyin hayatta kaldığı.

R01'in kapsamı ortam ve özerklikti; bu eksikler kusur değil, bu notun kapsamı.

### Bu notta eksik olan
Canlı deneme yok. R01'in önerdiği denemelere, bu notun cloud belirsizlikleri eklenmeli (§8).

---

## 7. Cloud'da uygulanabilirlik özeti

| Mekanizma | Cloud durumu | Koşul ve kaynak |
|---|---|---|
| Kök CLAUDE.md, rules, `@` içe aktarım | C+ | Commit edilirse (CENV) |
| Skills (proje) | C+ | Commit edilirse. Kişisel skill'ler gelmez; claude.ai hesabında açık skill'ler gelir (SK) |
| Alt ajan tanımları `.claude/agents` | C+ | Commit edilirse (WEB, CENV) |
| Alt ajan iç içe açma | C! | Cg: derinlik 1 |
| Alt ajan belleği `memory: project` | C~ | Commit ve push gerekir (çıkarım). Denenmedi |
| Auto memory | C! | Makineye bağlı (MEM). Cg: dizin yok |
| `.claude/settings.json` hook'ları ve izinleri | C! | Yalnız tek repolu oturumda (CENV, SET) |
| Proje alt ajan frontmatter hook'ları | C? | Çalışma alanı güveni şartı (HR, PERM). Cg: güven kaydı yok |
| Proje skill hook'ları | C~ | Ayar dosyası kuralına uyar (HR) |
| Ayar dosyasının oturum ortasında yeniden yüklenmesi | C~ | SET. Denenmedi |
| `SessionStart` hook'u | C+ | Tek repolu oturumda (CENV) |
| `/compact`, `/context` | C+ | WEB |
| `/clear` | yok | Yeni oturum (WEB) |
| Otomatik sıkıştırma eşiği | C! | Ortam belirliyor (WEB). Cg: %80 |
| Output style (repoda, `settings.json` ile) | C? | Belgesi okunan kısımda cloud'a özel ifade yok. `/config` cloud'da değer değiştirmez (SET) |
| Dinamik workflow | C+ | Sonuçlar konuşmayla saklanır (R01) |
| Agent teams | C+ | Ortam değişkeniyle; deneysel (R01) |
| Projects (proje belleği ve talimatı) | C+ | Pro/Max beta; hesapta var mı bilinmiyor (R01) |
| `/goal` | C? | R01 |
| Auto kipi | C+ | Kurum ve model şartı (R01). Rolün izin kipini yok sayar (SA) |
| Repoda eklenti (`enabledPlugins`) | yok | CENV, SK, SET |

---

## 8. Açık sorular

1. **Cloud oturumu çalışma alanı güveni açısından ne sayılıyor?** Etkileşimli mi, `-p`/SDK mi, yoksa ayrı bir durum mu? Proje alt ajan frontmatter hook'ları cloud'da çalışır mı? Belgelenmemiş. Tek repolu oturumda küçük bir deneme ister; A-04 onayı gerekir.
2. **`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` kimin ayarı?** Cloud ortamının ortam değişkenleriyle değiştirilebilir mi, yoksa `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` gibi ortam tarafından mı sabitleniyor? Bilinmiyor.
3. **`memory: project` ile yazılan rol belleği cloud'da nasıl davranıyor?** Commit ve push akışına sorunsuz giriyor mu? Paralel iki örneğin çakışması nasıl yönetilir? Denenmedi.
4. **Output style cloud'da repodan etkinleştirilebilir mi?** `.claude/output-styles/` ve `settings.json` üzerinden. Belgenin okunan kısmı bunu cloud için açıkça söylemiyor.
5. **Alt ajan transcript'leri VM geri alınınca korunuyor mu?** `~/.claude/projects/…/subagents/` altındalar. Gözlemlenebilirlik ve kanıt saklama buna bağlı.
6. **P-O5'in Opus 5 uyarıları Opus 5.5'e de geçerli mi?** Bu oturum Opus 5.5. Aşırı doğrulama ve fazla delegasyon uyarıları ölçülmedi (bilinmiyor).
7. **Tasarım işi için "koşulabilir kontrol" ne olacak?** Anthropic'in doğrulama örnekleri çoğunlukla yazılım üzerine. Tasarım belgeleri için rubrik ve sert eşik tasarımı Anthropic kaynaklarında yok. Yakın örnek E-HD'nin öznel tasarım ölçütleri.
8. **READING-LOG gibi okuma kanıtı mekanizmaları gerekli mi?** Anthropic kaynaklarında karşılığı yok. Değerini EXP-006 deneyimi (R02) ve Foundation (R04) destekliyor; bedeli ölçülmedi.
9. **Hangi yargıç düzeni?** E-MARS'ın tek çağrılı yargıcı mı, E-EVAL'in boyut başına ayrı yargıcı mı EXP-007'ye uyuyor? Çözülmedi.
10. **Kontrol katmanı skill'e dönüşebilir mi?** AGENT.md'nin yönlendirme kapısı, protokolleri elle "gerektiğinde yükleme" düzenidir. Claude Code'daki doğal karşılığı skill açıklamaları ve kademeli açma olabilir (çıkarım). Bu, A-01 ve A-04 kapsamında Batu'nun kararı; bu not önermez, yalnız eşleşmeyi kaydeder.

## 9. Bu notun kanıtlamadıkları

- **Hiçbir mekanizma bu ortamda canlı denenmedi.** "C+" etiketi belgenin cloud'u açıkça andığını gösterir, davranışın gözlendiğini göstermez. Cg etiketleri yalnız dosya ve değişken varlığına dayanır.
- **Kanıtların hepsi tedarikçi kaynaklı.** Anthropic'in iç ölçümleri bağımsız değil: %90,2 çok ajan kazancı, 15× token, +%39 bellek ile bağlam düzenleme, %17 yanlış negatif. Anthropic dışı karşılaştırma bu notun kapsamında değil (R08).
- **Belgeler hızla değişiyor.** Sürüm notları v2.1.19x–v2.1.28x arasında davranış değişiklikleri gösteriyor. Blog ile belge arasında da tutarsızlık var: iç içe açma derinliği 5'e karşı 3. Bu not 27 Eylül 2026 metnini yansıtır. Kurulu Claude Code sürümü kontrol edilmedi.
- **Sayfaların bir kısmı kısmen okundu.** Kapsam tablosunda belirtildi. Okunmayan bölümlerde bu notu değiştirecek bir istisna olabilir.
- **Kontrol listeleri Anthropic'in "standart seviye"sidir, EXP-007'nin değil.** Hangilerinin kurulacağı METHOD v1'in ve Batu'nun kararıdır (A-04). "Gereksiz olduğu koşul" satırları bu kararı kolaylaştırmak için yazıldı, kararı vermez.
- **Uygulanabilirlik ile yeterlik ayrıdır.** Mühendislik yazılarının örnekleri yazılım üretimi üzerine: web uygulaması, derleyici, araştırma sistemi. DevOS tasarım işine aktarılabilirlik çıkarımdır. E-HAR da bunu açık soru olarak bırakıyor: "A future direction is to generalize these findings to other fields."
