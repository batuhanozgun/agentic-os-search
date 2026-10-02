# R08 — Anthropic dışı metodolojiler: kalıcı roller, bellek, bağlam ve uzun soluklu yöntem

**Tür:** Alt ajan raporu (model çıktısı), EXP-007 P0.3. Yazım: 27 Eylül 2026. Salt okuma kısıtıyla çalışıldı; yazılan tek dosya bu nottur.
**Soru:** Anthropic dışında, AI ajanlarıyla uzun soluklu proje yürütmek için yerleşmiş ya da yaygınlaşmış metodolojiler kalıcı rolleri, belleği, bağlamı, iş akışını, doğrulamayı ve oturumlar arası devri nasıl çözüyor? Bunlardan EXP-007'ye hangi "standart seviye" uygulamalar aktarılabilir?
**Beslediği karar:** METHOD v1'in hangi yerleşik uygulamalara dayanacağı ve neyi neden onlardan farklı yapacağı.
**Okuma kuralları:** Kaynak kimlikleri §0.2'dedir. Bütün web kaynaklarına erişim tarihi 27.09.2026'dır. Etiketler: *kaynak diyor*, *gözledim*, *çıkarım*, *varsayım*, *bilinmiyor*. "(ikincil)" işareti, birincil sayfa açılamadığı için arama aracının özetinden ya da üçüncü kişinin aktarımından gelen bilgiyi gösterir. Böyle bir bilgide tırnak içindeki ifade o özette geçer; birincil metinde doğrulanmamıştır.

---

## 0. Kaynaklar, erişim ve okuma kapsamı

### 0.1 Erişim durumu
- Kabuktan `curl` ile yalnız şu alan adları açıldı: raw.githubusercontent.com, microsoft.com, cloud.google.com, pypi.org. *gözledim*
- Şu alan adlarına kabuktan bağlanılamadı: kiro.dev, docs.cline.bot, cursor.com, forum.cursor.com, docs.bmad-method.org, docs.letta.com, letta.com, docs.crewai.com, blog.langchain.com, docs.langchain.com, openai.com, cdn.openai.com, openai.github.io, manus.im, cognition.ai, cognition.com, arxiv.org, kaggle.com, google.github.io, microsoft.github.io, cognitect.com, adr.github.io, writethedocs.org, scrumguides.org, sre.google, vercel.com. *gözledim*
  - Proxy durum kaydında görebildiklerim "403 to CONNECT (policy denial ...)" idi. Kayıt yalnız son hataları tuttuğu için birkaçının (ör. cursor.com) nedenini ayrıca göremedim.
  - WebFetch'i şu alan adlarında denedim; hepsi "EGRESS_BLOCKED" döndü: docs.bmad-method.org, kiro.dev, docs.cline.bot, manus.im, cognition.ai, cognition.com.
- Bunlar politika reddi olduğu için tekrar denemedim. Üçüncü taraf kopya ya da arşiv (archive.org, gist, s3 kopyaları, Medium özetleri) kullanmadım.
- Belgesini GitHub'da tutan projelerde resmî depo dosyasını raw.githubusercontent.com'dan okudum. Yayımlanmış siteyle aynı kaynak metindir, ama site sürümünden küçük farkları olabilir. *çıkarım*
- Erişilemeyen kaynaklar için WebSearch özetlerini kullandım ve "(ikincil)" diye işaretledim.
- API ile depo ağacı listelemek kapalıydı (api.github.com 403). Bu yüzden belge yollarını tahmin ederek buldum; bulamadıklarımı "okunmadı" diye yazdım. *gözledim*

### 0.2 Kaynak listesi ve kapsam

| Kimlik | Kaynak | Yer | Tür | Kapsam |
|---|---|---|---|---|
| BM1 | BMAD-METHOD README (main) | `raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md` | proje belgesi | tam |
| BM2 | BMAD CHANGELOG (en üstte v6.12.0, 2026-09-03) | `.../main/CHANGELOG.md` | proje sürüm notu | kısmi: v6.9.0–v6.12.0 tam; öncesi anahtar sözcük taraması |
| BM3 | Choose a Planning Path | `.../main/docs/plan/choose-a-planning-path.md` | proje belgesi | tam |
| BM4 | Set and Maintain Project Context | `.../main/docs/existing-codebases/set-and-maintain-project-context.md` | proje belgesi | tam |
| BM5 | The Theory of Project Context | `.../main/docs/existing-codebases/theory-of-project-context.md` | proje belgesi | tam |
| BM6 | Customize BMad | `.../main/docs/customize/customize-bmad.md` | proje belgesi | kısmi (ilk ~200 satır) |
| BM7 | Skills and Agents | `.../main/docs/reference/skills-and-agents.md` | proje belgesi | kısmi (ajanlar ve çekirdek beceriler) |
| BM8 | Build a Change | `.../main/docs/build/build-a-change.md` | proje belgesi | kısmi (ilk ~140 satır) |
| BM9 | Finish an Epic | `.../main/docs/build/finish-an-epic.md` | proje belgesi | kısmi (ilk ~110 satır) |
| BM10 | Autonomous Development Loops | `.../main/docs/build/autonomous-development-loops.md` | proje belgesi | kısmi (ilk ~130 satır) |
| BM11 | BMAD v4.44.3 README ve `bmad-core/agents/sm.md`, `dev.md` | `.../v4.44.3/...` | eski sürüm belgesi | README ve dev.md tarama; sm.md tam |
| BM12 | BMAD depo `AGENTS.md` | `.../main/AGENTS.md` | proje kuralı | tam |
| SK1 | Repo çalışması: `research/studies/spec-kit/` (META, FINDINGS, SOURCE-LEDGER; pin `0ced288`, v1.0.7, 2026-09-17) | repo | repo çalışması | tam |
| SK2 | Spec Kit README ve CHANGELOG başı (v1.0.10–v1.0.12, 2026-09-22..25) | `raw.githubusercontent.com/github/spec-kit/main/` | proje belgesi | kısmi (v1.0.8–v1.0.9 içeriği okunmadı) |
| KR1 | Kiro README | `raw.githubusercontent.com/kirodotdev/Kiro/main/README.md` | tedarikçi (AWS) | tam |
| KR2 | Kiro Crew README | `raw.githubusercontent.com/kirodotdev/KiroCrew/main/README.md` | tedarikçi | kısmi (ilk ~330 satır) |
| KR3 | kiro.dev: specs, steering, blog | kiro.dev | tedarikçi | erişilemedi; arama özetleri (ikincil) |
| CL1 | Cline Memory Bank kuralı (v1.0, "Cline Core") | `raw.githubusercontent.com/cline/prompts/main/.clinerules/memory-bank.md` | tedarikçi deposu | tam |
| CL2 | docs.cline.bot Memory Bank sayfası | docs.cline.bot | tedarikçi | erişilemedi |
| RO1 | Roo Code: Using Modes | `raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/basic-usage/using-modes.md` | tedarikçi | kısmi |
| RO2 | Roo Code: Custom Modes | `.../docs/features/custom-modes.mdx` | tedarikçi | kısmi |
| RO3 | Roo Code: Boomerang Tasks | `.../docs/features/boomerang-tasks.mdx` | tedarikçi | tam |
| RO4 | Roo Code Memory Bank (GreatScottyMac) | `raw.githubusercontent.com/GreatScottyMac/roo-code-memory-bank/main/README.md` | topluluk | kısmi |
| CU1 | Cursor kuralları, bellekler, forum | cursor.com, forum.cursor.com | tedarikçi / topluluk | erişilemedi; arama özetleri (ikincil) |
| AI1 | Aider: Specifying coding conventions | `raw.githubusercontent.com/Aider-AI/aider/main/aider/website/docs/usage/conventions.md` | proje belgesi | tam |
| AI2 | Aider: Repository map | `.../aider/website/docs/repomap.md` | proje belgesi | kısmi |
| AG1 | AGENTS.md açık biçimi | `raw.githubusercontent.com/agentsmd/agents.md/main/README.md` | topluluk standardı | kısmi |
| TF1 | 12-Factor Agents README | `raw.githubusercontent.com/humanlayer/12-factor-agents/main/README.md` | uygulayıcı denemesi | kısmi (ilk ~200 satır) |
| TF2 | 12-Factor faktör 2, 3, 5, 6, 7, 8, 9, 10 | `.../content/factor-*.md` | uygulayıcı denemesi | kısmi (metin; kod örnekleri atlandı) |
| OA1 | OpenAI, "A practical guide to building agents" (PDF) | cdn.openai.com | tedarikçi | erişilemedi; arama özetleri (ikincil) |
| OA2 | OpenAI Agents SDK: Agent orchestration | `raw.githubusercontent.com/openai/openai-agents-python/main/docs/multi_agent.md` | tedarikçi | tam |
| LC1 | LangChain `context_engineering` README | `raw.githubusercontent.com/langchain-ai/context_engineering/main/README.md` | tedarikçi | tam |
| LC2 | LangGraph "Memory overview" | `raw.githubusercontent.com/langchain-ai/docs/main/src/oss/concepts/memory.mdx` | tedarikçi | tam |
| LC3 | LangChain blogu, "Context Engineering for Agents" | blog.langchain.com | tedarikçi | erişilemedi |
| LE1 | Letta README | `raw.githubusercontent.com/letta-ai/letta/main/README.md` | tedarikçi | tam |
| LE2 | Letta Code README | `raw.githubusercontent.com/letta-ai/letta-code/main/README.md` | tedarikçi | tam |
| LE3 | Letta belgeleri ve blogu (bellek hiyerarşisi) | docs.letta.com, letta.com | tedarikçi | erişilemedi; arama özeti (ikincil) |
| LE4 | MemGPT makalesi (Packer vd., 2023) | repo: `research/studies/context-memory-harness-engineering/02-AGENT-MEMORY-ENGINEERING.md` §12, [S4] | makale (repo aktarımı) | birincil okunmadı |
| CR1 | CrewAI: Agents | `raw.githubusercontent.com/crewAIInc/crewAI/main/docs/edge/en/concepts/agents.mdx` | tedarikçi | kısmi (öznitelikler, yapılandırma) |
| CR2 | CrewAI: Memory | `.../docs/edge/en/concepts/memory.mdx` | tedarikçi | kısmi (genel bakış, kapsam, birleştirme, köken) |
| MS1 | Microsoft Research, "Magentic-One: A Generalist Multi-Agent System..." | microsoft.com/en-us/research/articles/... | tedarikçi araştırması | kısmi (HTML'den metin) |
| MS2 | AutoGen: Magentic-One `_prompts.py`, `_magentic_one_orchestrator.py`, `_magentic_one_group_chat.py` | `raw.githubusercontent.com/microsoft/autogen/main/python/packages/autogen-agentchat/.../_magentic_one/` | kaynak kod | `_prompts.py` tam; diğerleri tarama |
| MS3 | AutoGen README; Microsoft Agent Framework README | `raw.githubusercontent.com/microsoft/{autogen,agent-framework}/main/README.md` | tedarikçi | tarama |
| GO1 | Google ADK: Session, State, Memory | `raw.githubusercontent.com/google/adk-docs/main/docs/sessions/index.md` | tedarikçi | tam |
| GO2 | ADK: State | `.../docs/sessions/state.md` | tedarikçi | kısmi (tarama) |
| GO3 | ADK: Memory | `.../docs/sessions/memory.md` | tedarikçi | kısmi (tarama) |
| GO4 | Google "Agents" (Wiesinger, Marlow, Vuskovic, 2024) ve "Context Engineering: Sessions & Memory" (Milam, Gulli, Kasım 2025) | kaggle.com | tedarikçi | erişilemedi; arama özetleri (ikincil) |
| MA1 | Manus, "Context Engineering for AI Agents: Lessons from Building Manus" (Yichao "Peak" Ji, 18.07.2025) | manus.im | tedarikçi deneyimi | erişilemedi; arama özetleri (ikincil) |
| MA2 | Lance Martin, "Context Engineering in Manus" (15.10.2025) | yazarın blog deposu: `raw.githubusercontent.com/rlancemartin/rlancemartin.github.io/master/_posts/2025-10-15-manus.md` | ikincil; webinarı birlikte yürütenin notu | tam |
| CO1 | Cognition, "Don't Build Multi-Agents" (Walden Yan, Haziran 2025) | cognition.ai | tedarikçi denemesi | erişilemedi; arama özetleri (ikincil) |
| CO2 | Cognition, "Multi-Agents: What's Actually Working" (22.04.2026) | cognition.com | tedarikçi denemesi | erişilemedi; arama özetleri (ikincil) |
| AD1 | Nygard, "Documenting Architecture Decisions" (2011) | cognitect.com | özgün yazı | erişilemedi |
| AD2 | joelparkerhenderson/architecture-decision-record: Nygard şablonu ve README | `raw.githubusercontent.com/joelparkerhenderson/architecture-decision-record/main/` | topluluk | şablon tam; README tarama |
| AD3 | npryce/adr-tools README ve şablon | `raw.githubusercontent.com/npryce/adr-tools/master/` | topluluk aracı | tam |
| DC1 | Write the Docs, "Docs as Code" | `raw.githubusercontent.com/writethedocs/www/master/docs/guide/docs-as-code.rst` | topluluk | kısmi (ilk ~60 satır) |
| EL1 | "Engineering daybook" (The Pragmatic Programmer, 20. yıl baskısı) | — | kitap | erişilemedi; arama özeti (ikincil) |
| RE1 | Scrum Guide 2020 (retrospektif), Kerth "Prime Directive", Google SRE "Postmortem Culture" | scrumguides.org, retrospectivewiki.org, sre.google | normatif rehber / uygulama | erişilemedi; arama özetleri (ikincil) |
| ME1 | Gloaguen vd., "Evaluating AGENTS.md..." (ETH Zürih, Şubat 2026); Vercel, "AGENTS.md outperforms skills in our agent evals" | arxiv.org, vercel.com | ölçüm | erişilemedi; içerik BM5'in aktarımından, künye arama sonucundan (ikincil) |

### 0.3 Repo girdileri
- Tam okundu: ORTAK.md, R08.md, U004, A003, EXP-007 README/STATE/DECISIONS, P0 README, R02–R06, `research/studies/spec-kit/` (üç dosya).
- Kısmi: R01 (başlık, `multiagent` ekseni özeti ve başlık yapısı), CMH `02-AGENT-MEMORY-ENGINEERING.md` (§12 ve kaynakça).
- Okunmadı: R07, R09–R11 (bu not yazılırken henüz yoktu), EXP-006'nın main'deki yeni dosyaları (bu görev tanımı istemiyor; R11'in girdisi).

---

## 1. Kısa sonuç

1. **Standart çekirdek:** İncelenen 15 metodoloji grubunda tekrar eden uygulamalar §4'te 27 madde olarak çıkarıldı. Maddelerin çoğu üç ya da daha fazla kaynakta görülüyor; O27 yalnız iki-üç kaynakta görüldüğü için "aday" sayıldı. En güçlüleri şunlar:
   - repo içinde, sürümlü ve türlerine ayrılmış dosya belleği;
   - katmanlı bağlam yükleme: her zaman yüklenen, tetikle yüklenen ve istek üzerine okunan bilgi ayrı tutulur;
   - alt ajanla bağlam yalıtımı ve açık aşağı/yukarı aktarım;
   - proje düzeyinde sürümlü rol dosyası;
   - tek yazıcı ve insan kabulü;
   - ilerleme defteri, durma sayacı ve eşikte yeniden planlama;
   - temiz bağlamlı gözden geçiren;
   - kanıta dayalı retrospektif;
   - değiştirilmeyen karar kaydı ve ekleme-yalnız günlük;
   - açık budama kuralı.
2. **Güncellik uyarısı:** Görev tanımındaki bazı çerçeveler eskidi.
   - BMAD, Nisan 2026'da Scrum Master, QA ve tek kişilik geliştirici personalarını Developer ajanında birleştirdi. Ağustos 2026'da da "story dosyası ile bağlam taşıma" çiftini kullanımdan kaldırdı [BM2].
   - CrewAI ayrı bellek türlerini tek bir `Memory` sınıfında birleştirdi [CR2].
   - AutoGen bakım moduna geçti [MS3].
   - Letta'nın etkin kaynak kodu artık `letta-code`'da. Bellek bloklarını git'te izliyor [LE1, LE2].
   - Manus, `todo.md` ile hedefi yeniden okumayı, eylemlerin yaklaşık üçte birini tükettiği için bir planlayıcı ajanla değiştirdi [MA2, ikincil].
   - Cognition 2026'da çok ajanı dar bir koşulla kabul etti: yazma tek iş parçacığında kalır, ek ajanlar yalnız "zekâ" katar [CO2, ikincil].
3. **Kalıcı rol:** Yerleşik olan, "persona" değil, sürümlü bir **işlev sözleşmesi**dir. Sözleşmede kimlik, ne zaman kullanılacağı, sorumluluk, hedef, olumsuz kısıtlar, araç ve yazma kapsamı, model, yüklenen bağlam, prosedür, çıktı biçimi ve durma koşulları bulunur. Persona çerçevesinin etkisine dair bulduğum tek ölçüm BMAD'ın küçük A/B denemesi: inceleme personası sonuç değiştirmedi, yöntem şartı değiştirdi [BM2]. *kaynak diyor; tedarikçinin iç ölçümü*
4. **Bellek:** Olgun sistemler şunları ayrı tutuyor:
   - çalışma durumu;
   - proje özü;
   - kararlar;
   - olay günlüğü;
   - prosedürel kurallar;
   - dersler;
   - arşiv.

   Belleğe ne zaman yazılacağı tanımlıdır. Budama ve yerine koyma kuralı açıktır. Köken, güven ve kapsam etiketi taşınır. En yaygın açık, budama kuralının hiç olmamasıdır; örneğin Cline Memory Bank'te yoktur [CL1]. *gözledim*
5. **A003 v0 ile fark:** v0'da şunlar hiç yok (ayrıntı §7):
   - sıkıştırma politikası;
   - bellek budama ve yerine koyma;
   - rol dosyası anatomisi;
   - ekleme-yalnız çalışma günlüğü;
   - ilerlemesizliği sayan sayaç;
   - önbellek ve maliyet mekanizması;
   - bellek türlerinin ve kapsamlarının ayrılması.

---

## 2. Metodolojiler tek tek

Her başlıkta sırayla şunlar var: çekirdek yapı, kanıt gücü, sınırlar ve eleştiriler, aktarılabilecekler. Aktarılabilecekler §4'teki madde numaralarıyla (O1–O27) gösterilir.

### 2.1 BMAD-METHOD (v6.12.0, 3 Eylül 2026)

**Roller.**
- Güncel sürüm beş adlı ajan kuruyor: Analyst (Mary), Product Manager (John), Architect (Winston), Developer (Amelia), UX Designer (Sally). Teknik yazar "on hiatus" (ara verdi) [BM7]. *kaynak diyor*
- v6.3.0'da (2026-04-09) şu karar alındı: "Consolidate three agent personas into Developer agent (Amelia): remove Barry quick-flow-solo-dev (#2177), Quinn QA agent (#2179), and Bob Scrum Master agent (#2186)" [BM2]. *kaynak diyor*
- Görev tanımının saydığı Scrum Master ve QA personaları artık ayrı ajan değil. *gözledim*
- v6 ajan anatomisi: "Name, title, and domain are fixed ... Everything else is customizable: role, identity statement, communication style, principles, icon, menu, persistent facts, and activation hooks" [BM6]. *kaynak diyor*
- Özelleştirme üç katmanlıdır. Kişisel ve git'e girmeyen dosya en üstte, takımın commit ettiği dosya ortada, dağıtılan varsayılan en alttadır. "No removal": üst katman taban öğeyi silemez [BM6]. *kaynak diyor*
- v4 ajan dosyasının anatomisi [BM11, `sm.md`]:
  - `agent{name,id,title,icon,whenToUse}`;
  - `persona{role,style,identity,focus,core_principles}`;
  - `commands`;
  - `dependencies{checklists,tasks,templates}`.
- v4 dosyası olumsuz kısıt da taşıyordu: "You are NOT allowed to implement stories or modify code EVER!" *kaynak diyor*

**Bağlam taşıma: v4'ten v6.11'e.**
- v4'te bağlam story dosyasıyla taşınıyordu: "The Scrum Master agent then transforms these detailed plans into hyper-detailed development stories that contain everything the Dev agent needs" [BM11 README]. *kaynak diyor*
- Dev ajanına iki kural konmuştu: "NEVER load PRD/architecture/other docs files unless explicitly directed" ve "ONLY authorized to edit these specific sections of story files" [BM11 `dev.md`]. *kaynak diyor*
- v6.11.0'da (2026-08-09) bu çift kaldırıldı: "the `bmad-create-story` → `bmad-dev-story` pair is deprecated, and Phase 4 is a single chain: `bmad-sprint-planning → bmad-build → bmad-code-review`" [BM2]. *kaynak diyor*
- Şimdiki yapı:
  - spec klasörü (`SPEC.md`);
  - yapım sırasındaki `tickets.toml`;
  - her story için bir Build oturumu: "no story file is needed" [BM3].
- Build kodu ve üst belgeleri kendisi inceliyor [BM8]. Yani bağlam, önceden paketlenmiş story yerine, ajanın kanıttan kendi derlemesiyle geliyor. *çıkarım*
- Kalan gerekçe: "Dividing work can lose information: a requirement weakens, a constraint disappears, or two correct stories fail when combined. The PRD, architecture, and specs exist so later sessions can still see the whole." [BM3] *kaynak diyor*
- Girdi tavanı: "the practical ceiling is a few tens of thousands of tokens, roughly a 40-page document ... it silently loses the parts that mattered; condense them first" [BM3]. *kaynak diyor*
- Oturum yalıtımı: "Open a **fresh chat** ... Reusing a session from another workflow can mix contexts and confuse the run." Tipik oturum "one goal: about 500 lines of code" [BM8]. *kaynak diyor*

**Bellek.**
- Proje bağlamı `AGENTS.md` içinde tek bir küçük, doğrulanmış bloktur. Beş niyetle yönetilir: setup, adopt, refresh, record, audit [BM4]. *kaynak diyor*
- Kabul testi: "anything derivable from source is read live and never stored" [BM2 v6.11]. *kaynak diyor*
- Ders kaydı: "A pitfall goes in only when someone has seen the mistake." [BM4] *kaynak diyor*
- Denetim: "the block ends smaller or equal, never larger" [BM4]. *kaynak diyor*
- Emeklilik: "A rule stays until what it is about is gone, or you retire it. 'Nothing broke lately' is never a reason to delete one — a working rule erases the evidence that it is still needed." [BM4] *kaynak diyor*
- Yazma izni: "It asks before it writes; you approve every change." "It never commits." [BM4] *kaynak diyor*
- İki bağlam türü ayrılıyor: uygulama bağlamı her oturumda yüklenir, küçük tutulur. Planlama bağlamı ("rationale, rejected approaches, ownership, domain meaning") ise "consulted in bursts rather than loaded continuously" [BM5]. *kaynak diyor*
- Kararlar: v6.7.0'da `.decision-log` geldi: "memory of what was decided and why will be remembered" [BM2]. *kaynak diyor*
- Çalışma günlüğü: v6.9.0'da ortak `memlog` geldi: "append-only chronological working memory with init/append/set ops, no lifecycle-status design" [BM2]. *kaynak diyor*
- Ajan belleği: v6.0.0-alpha.17'de `_bmad/_memory` altında "sidecar" klasörü geldi [BM2]. Güncel belgelerde bu mekanizmayı görmedim; hâlâ kullanılıp kullanılmadığı *bilinmiyor*.

**İş akışı.**
- "Every path runs the same loop. Bigger work enters it earlier and goes round it more often" (docs/index.md). *kaynak diyor*
- Build önce inceler, sonra "three facts about the settled design: intent gaps ..., irreversible actions, and footprint" raporlar. Bunlara göre hafif yolu ya da yazılı tam planı seçer [BM8]. *kaynak diyor*
- Hata ait olduğu katmana döner: "If the code is wrong because the plan was weak, or the plan is wrong because the goal was wrong, it goes back to that layer and regenerates from there" [BM8]. *kaynak diyor*
- Gözetimsiz işçi sıradaki işi seçmez: "never picks the next ticket itself ... A human or an orchestrator ... owns backlog policy and dispatch" [BM10]. *kaynak diyor*
- İşçi, plan dosyasının `status` alanından sürdürür. Alan şu değerleri alır: draft, ready-for-dev, in-progress, in-review, built, done, blocked [BM10]. *kaynak diyor*

**Doğrulama.**
- Paralel inceleme katmanları var.
  - "Blind" katman: "blind to intent, not to the codebase" [BM2 v6.10].
  - Doğrulama boşluğu katmanı: "if this behavior broke, would any test fail?".
  - "Intent Alignment Auditor" katmanı: "fed the verbatim invocation intent alongside the diff" [BM2 v6.11].
- Triyaj her bulguya hüküm ve kanıt yazar: "so nothing gets dropped silently" [BM2 v6.12]. *kaynak diyor*
- Görev tanımı yeniden yazılmıyor: "Reviewers are dispatched by path to their prompt file instead of having the parent transcribe it, which was truncating instructions" [BM2 v6.11]. *kaynak diyor*
- Uygulama devrinde üst ajanın alanı daraltıldı: "The parent is barred from restating goals, listing files, or injecting acceptance criteria into the dispatch" [BM2 v6.11]. *kaynak diyor*
- Persona yerine yöntem: "A/B piloting on Claude and Codex showed the 'cynical, jaded reviewer' framing made no difference to residual-bug hit rate, while requiring at least ten concrete findings and asking what is missing did." [BM2 v6.11] *kaynak diyor; tedarikçinin iç ölçümü, örneklem büyüklüğü bilinmiyor*
- Retrospektif kanıta dayanır:
  - "Every finding carries a source reference ... A claim it can't point at doesn't make the report" [BM9];
  - önceki epic'in eylem maddelerinin yapılıp yapılmadığını kontrol eder;
  - hüküm üçlüdür: `accepted`, `accepted-with-open-items`, `rejected`;
  - bitmemiş bilet varsa hüküm `rejected` olur [BM9]. *kaynak diyor*
- Retrospektifin gerekçesi: "Each ticket passed its own review in isolation, so the bugs that survive to this point are the ones isolation hides." [BM9] *kaynak diyor*

**İnsanın rolü.**
- Kullanıcı planı onaylar.
- Bileti yalnız insan `done` yapar ("only you mark a ticket done") [BM9].
- "Give those decisions human attention before automating repetitions of them" [BM3]. *kaynak diyor*

**Kanıt gücü.**
- Açık kaynak proje belgesi ve sürüm notları. Proje BMad Code LLC'nin ve topluluğun (BM1).
- Ölçümler projenin kendi küçük denemeleri: A/B pilotu, "16 reviewer runs", "seven real commits".
- Bağlam teorisi dış ölçümlere dayanıyor [BM5 → ME1]; bunları okumadım.

**Sınırlar ve eleştiriler.**
- Beş ayda persona sayısı, story modeli ve beceri kataloğu değişti ("Core drops from fourteen skills to eight") [BM2]. Tazelik riski yüksek. *gözledim*
- Proje kendi sürüm notunda, ajanların prosedür adımlarını atladığını yazıyor: "LLM agents were short-circuiting activation sequences ... silently skipping append steps and `on_complete` hooks" [BM2 v6.8.0]. *kaynak diyor*
- Buna çözüm olarak belirlenimci işleri betiğe taşıdı: "Judgment stays with the LLM" [BM2 v6.11]. *kaynak diyor*
- Metin kuralı kendiliğinden işlemiyor. EXP-006'daki E3 kaymasıyla aynı ders (R02 §4). *çıkarım*

**Aktarılabilecekler.**
- Bağlam: O2, O4, O16.
- Bellek: O8, O9, O10.
- Rol: O11, O12.
- Plan: O14, O15.
- Doğrulama: O21, O22.
- Öğrenme: O23, O24, O25.
- Süreklilik: O17 (plan durumundan sürdürme), O20 (BMAD'ın içerik adresli çalıştırma kaydı: "publishes an immutable, inspectable copy of exactly what ran" [BM2 v6.11]).

### 2.2 GitHub Spec Kit (yalnız repodaki çalışmaya ek)

**Repodaki bulgular.** SK1 ve R05 (#8) şunları zaten kaydetti:
- constitution → specify → plan → tasks → implement → converge sırası;
- ekleme-yalnız düzeltme görevleri;
- salt-okunur `analyze` adımı;
- gözden geçirene ait kontrol listeleri;
- "oturuma kabul edilen dilim ≠ tüm plan" (SK1 §8).

Bunları tekrar etmiyorum.

**Çalışmadan (v1.0.7, 17 Eylül) sonra değişen.**
- v1.0.10–v1.0.12 sürüm notlarında (22–25 Eylül) çekirdek süreçte değişiklik görmedim. v1.0.8 ve v1.0.9'un içeriğini okumadım.
- Değişiklikler eklenti, hazır ayar (preset) ve katalog düzeyinde. Örneğin: "Autonomous Run Governance preset", "Intake Review Governance preset" [SK2]. *gözledim*
- README'de iki cümle doğrudan aktarılmaya değer:
  - Hata süreci: "Keep diagnosis, repair, and verification separate so the agent fixes the assessed cause and checks the original symptom." Hüküm üçlüsü `verified` / `partial` / `failed`; "Missing verification is not a successful fix." [SK2] *kaynak diyor*
  - Fikir değerlendirme: "go / needs-clarification / kill" kararıyla biter; "stopping with a documented reason is also a useful result"; "Resolve unknowns by refining the existing Markdown artifacts ... rather than regenerating whole stages" [SK2]. *kaynak diyor*

**Kanıt gücü.** Tedarikçi (GitHub) belgesi. Canlı etkinlik ölçümü yok (SK1 "What should not be inferred").

**Aktarılabilecekler:** O14, O22. Ek olarak, araştırmada "öldür" (kill) kararının geçerli bir sonuç sayılması.

### 2.3 AWS Kiro (specs, steering, custom agents, Kiro Crew)

**Çekirdek (birincil) [KR1].**
- Kiro kendini şöyle tanıtıyor: "Turn prompts into executable specs, validate correctness, work across large codebases with parallel agents, and carry the same project context across the IDE, CLI, Web, Mobile, and Crew".
- Specs, steering, izinler, hook'lar ve özel ajanlar tek bir "unified agent harness" ile projeyle taşınıyor.
- Gereksinim analizi "to find contradictions, ambiguities, and gaps before coding begins".
- Özellik tabanlı test ("property-based testing") ile koda karşı doğruluk.
- Özel ajanlar "with focused instructions and tools".
- `.kiroignore`, "checkpoints and rewind" (kontrol noktasına dönüş).
- *kaynak diyor*

**Specs ve steering (ikincil) [KR3].**
- Spec üç dosyadır: `requirements.md`, `design.md`, `tasks.md`. Gereksinimler EARS kalıbında yazılır: "WHEN [condition/event] THE SYSTEM SHALL [expected behavior]".
- İki akış var: "Requirements-First" ve "Design-First". Ayrıca hata spec'leri (bugfix) var.
- "Run all tasks" görevlerin bağımlılık grafiğini çıkarır ve bağımsız görevleri dalgalar halinde paralel koşar.
- Spec'in kodla eşitlenmesi için Kiro'dan spec'i güncellemesi istenebilir.
- Steering `.kiro/steering/` altındadır. `product.md`, `tech.md`, `structure.md` "included in every interaction by default".
- Yükleme modları: `always`, `fileMatch`, `manual`, `auto`. `auto`da açıklamaya bakarak ilgili olup olmadığına karar verilir.
- İyi uygulama önerileri: "one domain per file"; API anahtarı ve gizli bilgi konmaz; kural "neden"iyle ve örnekle yazılır.
- *kaynak diyor (ikincil)*

**Kiro Crew [KR2].**
- "Persistent. Sessions, memory, schedules, and task checkpoints survive Gateway restarts".
- "Self-learning. Corrections and task failures become durable lessons."
- "Lessons can apply globally or carry a `repo_scope` that limits them to one repository; Crew Members keep private lessons in their own memory store."
- "Repeated patterns become reusable skills. Memory, lessons, and skills stay visible and editable".
- Uzun görevler: "plans steps, executes them, validates results, retries failures, and resumes from checkpoints".
- Görünürlük: "Watch tool calls, subagent progress, context usage, approvals, schedules, memory, and logs from the dashboard."
- *kaynak diyor; tedarikçi iddiası*

**Kanıt gücü.** Tedarikçi (AWS) belgesi. Belgelerin çoğu ancak ikincil yoldan okunabildi. Bağımsız ölçüm yok.

**Sınırlar.**
- Otomatik ders öğrenmenin yararı bir tedarikçi iddiası.
- R05 (#19) şunu gösteriyor: bir dersin kaydedilmesi, sonraki oturumda davranışın değişmesi değildir. *çıkarım*

**Aktarılabilecekler.**
- O1: her zaman yüklenen üç temel dosya ve modlar.
- O10: ders kapsamı ve role özel dersler.
- O14.
- O16.
- O20: görünür yürütme.
- O24.
- Paralellik: yalnız bağımlılığı olmayan işler dalga halinde.

### 2.4 Cline Memory Bank ve Roo Code

**Cline Memory Bank [CL1].**
- Temel ilke: "My memory resets completely between sessions ... I MUST read ALL memory bank files at the start of EVERY task - this is not optional." *kaynak diyor*
- Altı çekirdek dosya hiyerarşik bağlıdır: `projectBrief.md` → `productContext.md`, `systemPatterns.md`, `techContext.md` → `activeContext.md` → `progress.md`.
- Dosyaların içeriği:
  - `projectBrief.md`: "Source of truth for project scope";
  - `productContext.md`: projenin neden var olduğu;
  - `systemPatterns.md`: "Key technical decisions";
  - `techContext.md`: teknik bağlam;
  - `activeContext.md`: "Current work focus", "Next steps", "Active decisions and considerations";
  - `progress.md`: "What works", "What's left to build", "Known issues", "Evolution of project decisions".
- Güncelleme dört durumda yapılır: yeni desen bulunduğunda; önemli değişiklikten sonra; kullanıcı **update memory bank** dediğinde ("MUST review ALL files"); bağlam netleştirme gerektiğinde.
- Plan modunda sıra: oku → doğrula → strateji. Act modunda sıra: oku → güncelle → uygula → belgele. *kaynak diyor*
- Metinde hiç bulunmayanlar *gözledim*:
  - budama ya da boyut kuralı;
  - kayıt düzeyinde köken ya da durum alanı ("doğrulandı / varsayım");
  - eski kaydı yerine koyma kuralı.
- Karar geçmişi `progress.md` ile `systemPatterns.md` arasında dağılıyor. *gözledim*

**Roo Code [RO1–RO3].**
- Modlar "specialized personas". Her modun araç erişimi ayrıdır:
  - Ask: yalnız okuma ve MCP;
  - Architect: okuma, MCP ve "restricted edit (markdown files only)";
  - Orchestrator: "No direct tool access (uses `new_task` tool ...)".
- Özel mod alanları: `slug`, `name`, `description`, `roleDefinition` ("placed at the beginning of the system prompt"), `groups` (araç grupları ve `fileRegex`), `whenToUse` ("guidance for Roo's automated decision-making, particularly for mode selection and task orchestration"), `customInstructions`, kurallar için `.roo/rules-{slug}/`.
- Proje modları `.roomodes` dosyasında, küresel modlar kullanıcı ayarında durur. Her mod son kullandığı modeli hatırlar ("Sticky Models").
- *kaynak diyor*

**Orchestrator ve alt görevler [RO3].**
- Aktarım kuralı: "Each subtask operates in complete isolation with its own conversation history. It does not automatically inherit the parent's context. Information must be explicitly passed: Down: Via the initial instructions ... Up: Via the final summary ... only this summary returns to the parent." *kaynak diyor*
- Orkestratöre neden dosya okuma verilmediği: "Giving it the ability to read files by default causes the context to become filled with file reads, hampering its ability to remain focused on orchestration." Bu kısıt "context poisoning"i (bağlamın ilgisiz ya da aşırı bilgiyle kirlenmesini) önlüyor. *kaynak diyor*
- Alt görev talimatında şunlar bulunmalı: "All necessary context", "A clearly defined scope", "only perform the work outlined". Dönen özet "the source of truth used to keep track of what was completed". Ayrıca "these specific instructions supersede any conflicting general instructions". *kaynak diyor*
- Alt görevin açılması ve kapanması varsayılan olarak kullanıcı onayı ister. *kaynak diyor*

**Roo topluluk memory bank'i [RO4].**
- Dosyalar: `activeContext`, `productContext`, `progress`, `decisionLog` ve `projectBrief`. Moda özgü strateji dosyaları da var.
- Cline sürümünden farkı ayrı bir karar günlüğü tutması.
- README'nin başı artık aynı yazarın yeni "Context Portal MCP" projesine yönlendiriyor. *gözledim* O projenin yapısını okumadım.

**Kanıt gücü.** Tedarikçi belgesi ve topluluk pratiği. Ölçüm yok.

**Eleştiri.**
- "Her görevde bütün dosyaları oku" kuralı bağlam maliyetini her görevde öder. BMAD'ın aktardığı ölçümler türetilebilir özet belgelerin yardım etmediğini söylüyor [BM5, ME1].
- Memory Bank'in `activeContext` ve `progress` dosyaları ise türetilemez durum bilgisidir. Yani eleştiri özellikle `techContext` ve `systemPatterns` gibi koddan türetilebilir kısımlara isabet eder. *çıkarım*

**Aktarılabilecekler:** O3, O4, O7, O8, O11, O12, O13, O26.

### 2.5 Cursor kuralları ve bellekleri, Aider convention dosyası, AGENTS.md

**Cursor [CU1, ikincil].**
- Kurallar `.cursor/rules/*.mdc` dosyalarında durur. Ön bilgi (frontmatter) alanları: `description`, `globs`, `alwaysApply`.
- Dört tür var: Always, Auto Attached (dosya kalıbıyla), Agent Requested (açıklamaya göre), Manual (`@ruleName`). Cursor `AGENTS.md`'yi de okur.
- Memories v1.0'da (Haziran 2025) çıktı: "Memories are stored per project on an individual level". Arka planda üretilen belleklere kullanıcı onayı eklendi.
- Topluluk forumunda "Custom modes and memories gone in 2.1" başlığı var. Belleklerin güncel durumu *bilinmiyor*.
- *kaynak diyor (ikincil)*

**Aider [AI1, AI2].**
- "The easiest way to do that with aider is to simply create a small markdown file and include it in the chat."
- "It's best to load the conventions file with `/read CONVENTIONS.md` ... This way it is marked as read-only, and cached if prompt caching is enabled."
- Her oturumda yükleme için `.aider.conf.yml` içinde `read:` kullanılır.
- Repo haritası: "a concise map of your whole git repository". Harita "most relevant" parçaları bir grafik sıralamasıyla seçer, "active token budget"e sığdırır. Bütçe `--map-tokens` ile ayarlanır, varsayılanı 1k token.
- *kaynak diyor*

**AGENTS.md [AG1].** "a simple, open format for guiding coding agents ... a README for agents: a dedicated, predictable place to provide context and instructions". BMAD, Kiro ve Cursor bu dosyayı okuyor ya da yazıyor [BM4, KR3, CU1]. *kaynak diyor*

**Kanıt gücü.** Tedarikçi belgeleri. Aider'in "convention dosyasıyla ve dosyasız" karşılaştırması tek bir örnek, ölçüm değil.

**Aktarılabilecekler:**
- O1: kural türleri, yükleme katmanlarının adlandırılmış bir örneği.
- O2: küçük, salt-okunur, önbelleğe alınan kural dosyası.
- O27.
- Token bütçeli harita fikri: araştırma kütüphanesi için dizin dosyası.

### 2.6 12-Factor Agents (HumanLayer)

**Çekirdek [TF1, TF2].**
- Temel tespit: "Agents, at least the good ones, don't follow the 'here's your prompt, here's a bag of tools, loop until you hit the goal' pattern. Rather, they are comprised of mostly just software." *kaynak diyor*
- Faktör 2: "Don't outsource your prompt engineering to a framework". Örnekte `Agent(role=..., goal=..., personality=..., tools=...)` biçimindeki kara kutu ajan kalıbı eleştiriliyor. *kaynak diyor* Bu kalıp CrewAI'ın role/goal/backstory yapısına çok benziyor. *çıkarım*
- Faktör 3: "At any given point, your input to an LLM in an agent is 'here's what's happened so far, what's the next step'"; "Everything is context engineering." *kaynak diyor*
- Faktör 5: "you can engineer your application so that you can infer all execution state from the context window". Sayılan faydalar: "One source of truth for all state", "Recovery", "Forking", "Human Interfaces and Observability". *kaynak diyor*
- Faktör 7–8:
  - İnsanla temas bir araç çağrısıdır (`request_human_input`, `done_for_now`).
  - Netleştirme ve yüksek riskli eylemde döngü kırılır ve insan beklenir.
  - Kontrol akışına şunlar eklenebilir: "LLM-as-judge on structured output", "context window compaction", "logging, tracing, and metrics".
  - *kaynak diyor*
- Faktör 9:
  - Aynı araçta "limit to ~3 attempts".
  - "Hitting some consecutive-error-threshold might be a great place to escalate to a human".
  - Hata çok birikirse "your agent will start to spin out".
  - *kaynak diyor*
- Faktör 10: "By keeping agents focused on specific domains with 3-10, maybe 20 steps max, we keep context windows manageable"; "As context grows, LLMs are more likely to get lost or lose focus". *kaynak diyor*

**Kanıt gücü.** Uygulayıcı denemesi ("talked to at least 100 SaaS builders"). Topluluk pratiği; ölçüm yok.

**Sınırlar.** Müşteriye dönük ürün ajanları için yazılmış; çok oturumlu tasarım işine doğrudan değinmiyor. Durumun tek olay dizisinden yeniden kurulması ve eşikli insan teması ilkeleri yine de aktarılabilir. *çıkarım*

**Aktarılabilecekler:** O5, O16, O17, O19, O26.

### 2.7 OpenAI

**"A practical guide to building agents" [OA1, erişilemedi; ikincil].**
- Önce tek ajanın yeteneği en üst düzeye çıkarılır. Bölmeye ancak karmaşık koşullu mantık ya da çakışan araçlar varsa gidilir.
- İki desen: yönetici (manager) ve merkezsiz devir (handoff).
- Katmanlı korkuluklar (guardrails).
- İnsana iki durumda gidilir: "Exceeding failure thresholds" ve "High-risk actions".
- *kaynak diyor (ikincil)*

**Agents SDK orkestrasyon belgesi [OA2].**
- "Agents as tools": "A manager agent keeps control of the conversation and calls specialist agents".
- "Handoffs": uzman ajan konuşmanın geri kalanını devralır.
- Önerilen taktikler:
  - "Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything";
  - "Invest in evals";
  - "Monitor your app and iterate".
- Kodla orkestrasyonda değerlendirici döngüsü: "run an evaluator agent to assess that output and provide feedback; stop when the evaluator says the output passes the required criteria".
- *kaynak diyor*

**Repoda zaten olan.** OpenAI'nin "Harness engineering" yazısı ve SDK'nin sessions, guardrails ve tracing sayfaları CMH çalışmasında okunmuş (`01-CONTEXT-ENGINEERING.md`, `03-HARNESS-ENGINEERING.md`). R09'un alanı.

**Kanıt gücü.** Tedarikçi belgesi.

**Aktarılabilecekler:** yönetici deseni (EXP-007'nin ana oturum–alt ajan yapısıyla aynı), O15, O21, O26.

### 2.8 LangChain / LangGraph

**Bağlam mühendisliği [LC1].**
- Tanım: "Context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory." *kaynak diyor*
- Dört strateji *kaynak diyor*:
  - "Writing context - saving it outside the context window";
  - "Selecting context - pulling it into the context window";
  - "Compressing context - retaining only the tokens required";
  - "Isolating context - splitting it up".
- Örnekler:
  - karalama alanı (scratchpad);
  - ad alanlı (namespace) bellekler;
  - araçların RAG ile seçilmesi;
  - konuşmayı özetleme (örnekte 115k token 60k'ya indi);
  - yalıtılmış bağlamlı denetçi (supervisor) ve uzman ajanlar.
- Aynı README, Anthropic'in bir tespitini alıntılıyor: "Agents often engage in conversations spanning hundreds of turns, requiring careful context management strategies". *kaynak diyor*

**Bellek [LC2].**
- Kısa süreli bellek "thread-scoped"tır ve checkpointer ile kalıcı olur. Uyarı: "most LLMs still perform poorly over long contexts. They get 'distracted' by stale or off-topic content". *kaynak diyor*
- Uzun süreli bellek iş parçacıkları arasında paylaşılır ve ad alanlarında tutulur. *kaynak diyor*
- Tür tablosu *kaynak diyor*:
  - Semantic: "Facts";
  - Episodic: "Experiences", "Past agent actions";
  - Procedural: "Instructions", "Agent system prompt".
- Semantik bellek için iki biçim ve ödünleşimi:
  - profil biçimi "error-prone as the profile gets larger";
  - koleksiyon biçimi daha yüksek geri çağırma sağlar, ama güncelleme ve silme zorlaşır: "some models may default to over-inserting and others may default to over-updating".
  - *kaynak diyor*
- Prosedürel bellek "Reflection" ile güncellenir: ajan kendi talimatını geri bildirimle yeniden yazar. *kaynak diyor*
- Yazma zamanı iki türlü:
  - "in the hot path" (anında görünür, gecikme ekler);
  - "in the background" (ana işi yavaşlatmaz, zamanlaması kritiktir).
  - *kaynak diyor*

**Kanıt gücü.** Tedarikçi kavram belgesi; CoALA makalesine dayanıyor. Ölçüm yok.

**Aktarılabilecekler:**
- O5, O7, O8.
- Dört strateji, bağlam alt sistemi için kontrol listesi olarak kullanılabilir. *çıkarım*
- Profil / koleksiyon ayrımı: STATE profildir, DECISIONS ve günlük koleksiyondur. *çıkarım*

### 2.9 Letta / MemGPT

**Güncel durum [LE1, LE2].**
- "Letta (f.k.a. MemGPT) is actively developed. The current source code lives in `letta-ai/letta-code`". V1 API sunucusu arşiv dalına alındı. *kaynak diyor*
- Letta Code şunları söylüyor *kaynak diyor*:
  - "Agents programmatically rewrite their context to improve and adapt over time, including system prompt learning (through memory blocks) and skill learning";
  - "Configure periodic dreaming with `/sleeptime`";
  - "MemFS: All context (including memory blocks) is tracked via git";
  - ajan "can also search their own conversations or the conversations of other agents";
  - alt ajanlar: "general-purpose, forked, recall".

**Hiyerarşi [LE3, ikincil].**
- Çekirdek bellek: bağlamda sabit duran ("pinned") ve düzenlenebilen bloklar (persona, kullanıcı, görev).
- Recall bellek: bütün etkileşim geçmişi; aranarak geri çağrılır.
- Archival bellek: dış depoda, araç çağrısıyla yazılan ve sorgulanan uzun süreli bilgi.
- "Sleep-time" ajanları bu blokları düzenleyebilir.
- *kaynak diyor (ikincil)*

**Makale.** MemGPT'nin "virtual context" yaklaşımı repoda CMH çalışmasında özetli: sınırlı hızlı bağlam ile büyük dış bellek arasında veri taşır (CMH 02 §12). *kaynak diyor (repo aktarımı)*

**Kanıt gücü.** Tedarikçi belgesi ve makale; makalenin birincil metni okunmadı.

**Sınırlar.**
- Kendi belleğini yeniden yazan ajan, kendini güçlendiren yanlış (memory poisoning, self-reinforcement) riski taşır (CMH 02 §17; R05 #19–20). *çıkarım*

**Aktarılabilecekler:**
- O6: git'te izlenen bellek. EXP-007 bunu zaten yapıyor.
- O7 eşlemesi *çıkarım*:
  - çekirdek → her zaman yüklenen CLAUDE.md ve STATE;
  - archival → `research/` ve `sources/`;
  - recall → git günlüğü ve konuşma kayıtları.

### 2.10 CrewAI

**Ajan [CR1].** Alanlar:
- `role`: "Defines the agent's function and expertise within the crew";
- `goal`: "The individual objective that guides the agent's decision-making";
- `backstory`: "Provides context and personality";
- `llm`, `tools`;
- `max_iter` (varsayılan 20), `max_execution_time`;
- `allow_delegation` (varsayılan False);
- `respect_context_window`: "Keep messages under context window size by summarizing";
- `reasoning`: "reflect and create a plan before executing";
- `knowledge_sources`, `guardrail`.

Tanım `agents/<ad>.jsonc` dosyasında durur. Görev `description`, `expected_output` ve `agent` alanlarıyla tanımlanır. *kaynak diyor*

**Bellek [CR2].**
- "a single `Memory` class that replaces separate short-term, long-term, entity, and external memory types".
- Kayıtta dil modeli kapsamı, kategoriyi ve önemi kendisi çıkarır. Geri çağırma puanı anlamsal benzerlik, tazelik ve önemin bileşimidir.
- "After each task, the crew automatically extracts discrete facts from the task output and stores them. Before each task, the agent recalls relevant context from memory and injects it into the task prompt."
- Kapsamlar hiyerarşik bir ağaçtır. Ajanın özel kapsamı ile ekibin paylaşılan belleği ayrıdır; salt-okunur dilimler tanımlanabilir.
- Birleştirme (consolidation): benzerlik 0,85'in üstündeyse model dört karardan birini verir:
  - `keep`;
  - `update`;
  - `delete` ("outdated, superseded, or contradicted");
  - `insert_new`.
- Köken ve erişim: "a `source` tag for provenance tracking and a `private` flag".
- *kaynak diyor*

**Kanıt gücü.** Tedarikçi belgesi; ölçüm yok.

**Eleştiri.**
- 12-Factor'ün faktör 2 eleştirisi buna çok benzeyen bir kalıba yöneliyor; örnekte alanlar role/goal/personality [TF2]. *kaynak diyor; benzerlik çıkarım*
- Görev tanımının varsaydığı "kısa süreli / uzun süreli / varlık belleği" ayrımı CrewAI'da artık yok. *gözledim*

**Aktarılabilecekler:**
- O10, O11, O13.
- O17: `max_iter` ve süre sınırı.
- Birleştirme karar sözlüğü (`keep` / `update` / `delete` / `insert_new`), otomatik kullanılmadan, elle yapılan bellek gözden geçirmesinin kategorileri olarak kullanılabilir. *çıkarım*

### 2.11 Microsoft AutoGen ve Magentic-One

**Yapı [MS1].**
- "a lead agent, the Orchestrator, directs four other agents ... The Orchestrator plans, tracks progress, and re-plans to recover from errors".
- İki döngü var:
  - dış döngü "task ledger (containing facts, guesses, and plan)";
  - iç döngü "progress ledger (containing current progress, task assignment to agents)".
- İlerleme yeterince uzun süre yoksa ("if ... progress is not being made for enough steps") görev defteri güncellenir ve yeni plan yapılır.
- Orkestratör için "a strong reasoning model" öneriliyor.
- Değerlendirme aracı AutoGenBench "repetition and isolation" sağlıyor.
- *kaynak diyor*

**Defterlerin kodu [MS2].**
- Görev defterinin olgu listesi dört başlıklı *kaynak diyor*:
  - "GIVEN OR VERIFIED FACTS";
  - "FACTS TO LOOK UP";
  - "FACTS TO DERIVE";
  - "EDUCATED GUESSES".
- Plan ekibin tamamını kullanmak zorunda değil: "there is no requirement to involve all team members". *kaynak diyor*
- İlerleme defteri her adımda beş soruyu gerekçeli (`reason` alanıyla) cevaplar *kaynak diyor*:
  - `is_request_satisfied`;
  - `is_in_loop`;
  - `is_progress_being_made`;
  - `next_speaker`;
  - `instruction_or_question`.
- Kod ilerleme yoksa ya da döngü varsa sayacı bir artırır, aksi halde bir azaltır. `max_stalls`a (varsayılan 3) ulaşınca "Stall count exceeded, re-planning with the outer loop..." olur. *kaynak diyor*
- Yeniden planlamada iki şey yapılır *kaynak diyor*:
  - olgu listesi güncellenir: "moving educated guesses to verified facts if appropriate";
  - yeni plan istenir: "explain what went wrong ... (the root cause of the failure) ... avoids repeating the same mistakes".

**Durum [MS3].** "AutoGen is now in maintenance mode". Önerilen halef Microsoft Agent Framework. Onun README'si "checkpointing, streaming, human-in-the-loop, and time-travel" sayıyor. Magentic deseninin orada sürüp sürmediğini doğrulamadım. *kaynak diyor; bilinmiyor*

**Kanıt gücü.** Tedarikçi araştırması ve kıyas testi ölçümleri (GAIA, AssistantBench, WebArena: "statistically comparable performance"). Bu ölçümler sistemin bütününe ait. Defterlerin ayrı katkısını gösterip göstermedikleri *bilinmiyor*; makaleyi okumadım.

**Aktarılabilecekler:**
- O10: olgu sınıfları.
- O17: soru seti, sayaç ve yeniden plan.
- Uzmanlar persona olarak değil, yetenekle tanımlanıyor (WebSurfer, FileSurfer, Coder, ComputerTerminal).

### 2.12 Google (ADK; whitepaper'lar)

**ADK [GO1–GO3].**
- Üç kavram ayrılıyor *kaynak diyor*:
  - `Session`: tek etkileşimin olay (event) dizisi;
  - `State`: o oturuma ait veri;
  - `Memory`: "Searchable, Cross-Session Information".
- Uyarı: "all data stored using these in-memory options ... is lost when your application restarts". *kaynak diyor*
- State anahtarındaki önek kapsamı ve kalıcılığı belirler *kaynak diyor*:
  - önek yok: oturum;
  - `user:`: kullanıcının bütün oturumları;
  - `app:`: bütün kullanıcılar;
  - `temp:`: "Discarded after the invocation completes".
- Güncelleme kuralı: "State should **always** be updated as part of adding an `Event` to the session history using `session_service.append_event()`". *kaynak diyor*
- `output_key` ajan çıktısını state'e yazar. State değerleri talimata `{key}` ile yerleştirilir. *kaynak diyor*
- Bellek servisi *kaynak diyor*:
  - `add_session_to_memory` biten oturumu uzun süreli belleğe alır;
  - `search_memory` bellekte arar;
  - Vertex Memory Bank "Extracts meaningful information from conversations and consolidates it with existing memories powered by LLM".

**Whitepaper'lar [GO4, erişilemedi; ikincil].**
- "Agents" (2024): model, araç (extensions, functions, data stores) ve orkestrasyon katmanı; ReAct, CoT, ToT.
- "Context Engineering: Sessions & Memory" (Kasım 2025):
  - oturum ile bellek ayrımı;
  - köken takibi: "recording where each memory came from and how confident we should be in it";
  - çatışmada "higher-trust sources override lower-trust ones".
- *kaynak diyor (ikincil)*

**Kanıt gücü.** Tedarikçi belgesi.

**Aktarılabilecekler:**
- O7: kapsam önekleri. EXP-007 eşlemesi *çıkarım*:
  - `temp:` → oturum içi not;
  - oturum → iş kalemi;
  - `user:` → Batu'nun tercihleri;
  - `app:` → METHOD.
- O8: oturum sonunda belleğe alma.
- O10.
- O19: her durum değişikliği kayıtlı bir olayla.

### 2.13 Manus

**Blog yazısı [MA1, erişilemedi; ikincil].** Yazar Yichao "Peak" Ji, 18 Temmuz 2025. Arama özetlerinde geçen dersler:
- çerçeve dört kez baştan yazıldı;
- KV-cache isabet oranı üretim ajanında "single most important metric";
- Claude Sonnet'te önbellekli girdi 0,30 $/MTok, önbelleksiz 3 $/MTok;
- kararlı önek ve ekleme-yalnız bağlam;
- araçlar silinmez, maskelenir;
- dosya sistemi "the ultimate context"tır; sıkıştırma geri alınabilir tutulur (URL ya da yol korunur, içerik düşülür);
- `todo.md` sürekli yeniden yazılır ve böylece hedef bağlamın sonuna "recite" edilir;
- hatalar bağlamda bırakılır ("keep the wrong stuff in");
- tek düze örneklerle kendini kalıba sokmamak için yapılandırılmış çeşitlilik ("don't get few-shotted");
- ortalama görev yaklaşık 50 araç çağrısı; girdi/çıktı token oranı yaklaşık 100:1.
- *kaynak diyor (ikincil)*

**Ekim 2025 webinar notları [MA2].** Bu kaynak ikincil, ama webinarı birlikte yürütenin notudur.
- Üç strateji: "Reduce Context", "Offload Context", "Isolate Context". *kaynak diyor*
- Sıkıştırma *kaynak diyor*:
  - araç sonucunun "full" ve "compact" iki temsili var; kompakt olan tam sonuca işaret eder (dosya yolu);
  - bayat sonuçlar önce kompakta çevrilir;
  - bu yeterli olmayınca, bir şemayla tanımlanmış alanlarla özetlenir.
- Rol yaklaşımı: "Manus takes a pragmatic approach to multi-agent, avoiding anthropomorphized divisions of labor. While humans organize by role (designer, engineer, project manager) due to cognitive limitations, LLMs don't necessarily share these same constraints." *kaynak diyor*
- "the primary goal of sub-agents in Manus is to *isolate context*". *kaynak diyor*
- Üç işlev: görev atayan planlayıcı; "a knowledge manager that reviews conversations and determines what should be saved in the filesystem"; yürütücü. *kaynak diyor*
- `todo.md`'den vazgeçilme gerekçesi: "roughly one-third of all actions were spent updating the todo list, wasting valuable tokens. They shifted to a dedicated planner agent". *kaynak diyor*
- Bağlam paylaşımı iki türlü *kaynak diyor*:
  - basit işte alt ajana yalnız talimat gider;
  - alt ajan planlayıcının da kullandığı dosyalara yazacaksa planlayıcı "shares its *full* context".
- Her iki durumda "the planner defines the sub-agent's output schema". Alt ajan sonucu bir `submit results` aracıyla, kısıtlı çözümlemeyle bu şemaya uygun döndürür. *kaynak diyor*
- 20'den az atomik araç; indeks yerine `glob` ve `grep`. *kaynak diyor*
- "Manus has been refactored five times since their launch in March!" *kaynak diyor*
- Harness sınaması: "If performance doesn't improve with stronger models, your harness may be hobbling the agent." *kaynak diyor*

**Kanıt gücü.** Tedarikçinin kendi deneyim raporu. Sayılar kendi beyanı; bağımsız ölçüm yok. İkincil erişim.

**Aktarılabilecekler:**
- O3.
- O4: planlayıcı.
- O5: tam/kompakt temsil ve şemalı özet.
- O6.
- O13: şemayı ana ajan tanımlar.
- O25.
- O27.
- "Bilgi yöneticisi" işlevi: neyin kalıcı belleğe gireceğine karar veren sorumluluk.

### 2.14 Cognition (Devin)

**2025 [CO1, erişilemedi; ikincil].**
- İlkeler: "Share context, and share full agent traces, not just individual messages" ve "Actions carry implicit decisions, and conflicting decisions carry bad results".
- Öneri: bağlamı kararlar arasında olabildiğince paylaşmak ve karar vermeyi çatışacak biçimde bölmemek.
- *kaynak diyor (ikincil)*

**2026 [CO2, erişilemedi; ikincil].** "Multi-Agents: What's Actually Working" (22.04.2026).
- İşleyen dar sınıf: "multiple agents contribute intelligence to a task while writes stay single-threaded".
- Örnekler:
  - "A clean-context reviewer catches bugs the coder can't see";
  - "A frontier-level smart friend catches subtleties a weaker primary misses";
  - "A manager coordinates scope across child agents without fragmenting decisions".
- Açık sorunlar iletişim sorunları:
  - zayıf model ne zaman yükseltmeli;
  - bir çocuk ajan kardeşlerinin işini değiştirecek bulguyu nasıl iletmeli;
  - bağlam "without drowning the receiver" nasıl aktarılmalı.
- Özetlere göre kodlayan ve gözden geçiren ajan önceden bağlam paylaşmadığında inceleme daha iyi çalışıyor.
- *kaynak diyor (ikincil)*

**Kanıt gücü.** Tedarikçinin kendi deneyimi; ikincil erişim.

**Aktarılabilecekler:** O18, O21. Açık sorunlar listesi, EXP-007'nin koordinatör–alt ajan riskleriyle birebir örtüşüyor (§9). *çıkarım*

### 2.15 Yerleşik mühendislik uygulamaları

**ADR.**
- Nygard şablonunun bölümleri: Title; Status ("proposed, accepted, rejected, deprecated, superseded"); Context; Decision; Consequences ("What becomes easier or more difficult to do because of this change?") [AD2]. *kaynak diyor*
- `adr-tools` bir tarih alanı ekliyor. Yeni bir ADR eskisinin yerini aldığında (`-s`) aracın yaptığı: "changes the status of ADR 9 to indicate that it is superceded by the new ADR" [AD3]. *kaynak diyor*
- Topluluk rehberinin kuralı: "Immutable: Don't alter existing information in an ADR. Instead, amend the ADR by adding new information, or supersede the ADR by creating a new ADR." [AD2 README] *kaynak diyor; topluluk*
- Nygard'ın özgün yazısı erişilemedi.

**Docs-as-code [DC1].**
- "writing documentation with the same tools as code": sorun takibi, git, düz metin işaretleme, kod incelemesi, otomatik test.
- "You can block merging of new features if they don't include documentation".
- *kaynak diyor; topluluk*

**Çalışma günlüğü.**
- Kitaptaki "engineering daybook" önerisi: gün içinde yapılanı, öğrenileni ve okuma notlarını kaydetmek [EL1]. *kaynak diyor (ikincil)*
- Ajan sistemlerindeki karşılıkları:
  - BMAD `memlog` [BM2];
  - 12-Factor'ün olay dizisi [TF2 faktör 5];
  - ADK `append_event` [GO2];
  - Kiro Crew'un günlük ve pano görünümü [KR2].
  - *kaynak diyor*

**Retrospektif ve postmortem [RE1, ikincil].**
- Scrum Guide 2020: "The purpose of the Sprint Retrospective is to plan ways to increase quality and effectiveness ... The most impactful improvements are addressed as soon as possible. They may even be added to the Sprint Backlog for the next Sprint."
- Kerth'in "Prime Directive"i: "everyone did the best job they could, given what they knew at the time...".
- Google SRE: suçlamasız postmortem "focus on identifying the contributing causes ... without indicting any individual"; "An unreviewed postmortem might as well never have existed".
- *kaynak diyor (ikincil)*

**Kanıt gücü.** Onlarca yıllık topluluk pratiği ve normatif rehber. AI ajan işinde ölçülmüş değil.

**Aktarılabilecekler:**
- O19, O23.
- Belgeleme kapısı: STATE ve DECISIONS, işin kendisiyle aynı commit'te güncellenir. *çıkarım*
- Suçlamasız ilkenin ajan karşılığı: "kim hata yaptı" yerine "hangi girdi ya da bağlam eksikti". Batu'nun "LLM düşünmez, girdisi yönetilir" ilkesiyle uyumlu (R03 ilke 1). *çıkarım*

---

## 3. Karşılaştırma tabloları

"–" işareti, okuduğum kaynakta bu alt sisteme dair bir şey görmediğimi gösterir; sistemde olmadığı anlamına gelmez. "(ik.)" ikincil kaynaktan gelen bilgiyi gösterir.

### 3.1 Bağlam, bellek, roller, plan

| Metodoloji | Bağlam | Bellek | Roller | Plan / yaşam döngüsü |
|---|---|---|---|---|
| BMAD | Her iş için taze sohbet; girdi tavanı ~40 sayfa; AGENTS.md'de küçük doğrulanmış blok; türetilebilir bilgi saklanmaz | AGENTS.md bloğu (record/audit); `.decision-log`; ekleme-yalnız `memlog`; `persistent_facts` | 5 adlı ajan; ad ve alan sabit; rol, kimlik, ilke, menü, olgu ve kanca özelleştirilebilir; 3 katmanlı özelleştirme | Niyet → spec → bilet → her bilete bir Build; tören incelemeden sonra seçilir; durum plan dosyasında |
| Spec Kit | Oturuma kabul edilen dilim ≠ tüm plan | constitution/spec/plan/tasks dosyaları; converge ekleme-yalnız | Yok; gözden geçirene ait listeler | specify→plan→tasks→implement→converge; hata sahibine döner |
| Kiro | Steering: 3 temel dosya her zaman; always/fileMatch/manual/auto (ik.) | Steering ve spec repoda; Crew: kalıcı bellek, dersler (global, repo, role özel) | Odaklı talimat ve araçlı özel ajanlar | requirements (EARS) → design → tasks; bağımlılık dalgalarıyla paralel (ik.) |
| Cline Memory Bank | Her görevde bütün bellek okunur | 6 hiyerarşik çekirdek dosya | Plan / Act modları | Oku → doğrula → strateji / oku → güncelle → uygula → belgele |
| Roo Code | Alt görev yalıtılmış; aşağı talimat, yukarı yalnız özet; orkestratör dosya okumaz | Topluluk memory bank'i (+ `decisionLog`) | Mod = `roleDefinition` + `whenToUse` + araç grupları + `fileRegex` + kurallar | Orkestratör böler, uzmana devreder, özetle sürer |
| Cursor / Aider / AGENTS.md | Always / Auto Attached / Agent Requested / Manual (ik.); salt-okunur, önbellekli CONVENTIONS; 1k token repo haritası | Kural dosyaları repoda; Cursor Memories (durumu belirsiz) | – | – |
| 12-Factor | Bağlam penceresi sahiplenilir; hatalar sıkıştırılır; ajan 3–10 adım | Yürütme durumu = iş durumu; tek olay dizisi | Küçük, odaklı ajan | Kontrol akışı kodda; duraklat/sürdür |
| OpenAI | Önce tek ajan (ik.) | (SDK sessions; CMH) | Yönetici ("agents as tools") ya da devir | Ölçüt geçene kadar değerlendirici döngüsü |
| LangChain / LangGraph | write / select / compress / isolate | Kısa (iş parçacığı) / uzun (ad alanı); semantik / epizodik / prosedürel; anında ya da arka planda yazım | Denetçi + uzman ajan | Graf; checkpoint'ten sürdürme |
| Letta | Çekirdek bloklar bağlamda; recall ve archival araçla (ik.) | Bloklar git'te (MemFS); "dreaming" ile birleştirme | Kalıcı kimlikli ajan | Ajan kendi belleğini yeniden yazar |
| CrewAI | Özetle bağlamı sınırda tutma; görev öncesi bellekten geri çağırma | Tek `Memory`: kapsam ağacı, önem ve tazelik puanı, birleştirme, köken etiketi | role / goal / backstory + araç + sınırlar | Görev: description + expected_output + agent |
| Magentic-One | Orkestratör defterlerle yönetir | Görev defteri (olgular, tahminler, plan); ilerleme defteri | Yetenek bazlı 4 uzman + orkestratör | Dış döngü plan, iç döngü adım; 3 takılmada yeniden plan |
| Google ADK | Talimata `{key}` ile durum yerleştirme | Session / State (önek, `user:`, `app:`, `temp:`) / Memory; güncelleme olayla | LlmAgent ve alt ajanlar | Oturum sonunda belleğe alma |
| Manus | KV-cache; kararlı önek; tam/kompakt sonuç; şemalı özet (ik.) | Dosya sistemi; bilgi yöneticisi neyin saklanacağına karar verir | Antropomorfik rol yok: planlayıcı / bilgi yöneticisi / yürütücü | todo.md'den planlayıcı ajana (eylemlerin ~1/3 israfı) |
| Cognition | Tam iz paylaşılır (2025, ik.) | – | Yönetici + çocuk ajanlar; ek ajan zekâ katar, yazma tek elde (2026, ik.) | "Map-reduce-and-manage" (ik.) |
| ADR / docs-as-code / günlük / retro | – | ADR (durum, bağlam, karar, sonuç; yerine koyma); belgeler git'te; günlük | – | Sprint sonu retro; postmortem |

### 3.2 Doğrulama, süreklilik, gözlemlenebilirlik, öğrenme, insan

| Metodoloji | Doğrulama | Süreklilik | Gözlemlenebilirlik | Öğrenme | İnsan |
|---|---|---|---|---|---|
| BMAD | Paralel katmanlar (niyete kör, uç durum, doğrulama boşluğu, niyet uyumu); her bulguya hüküm ve kanıt; kanıta dayalı retro | Plan `status` alanından sürdürme; `sprint-status.yaml` | Değişmez çalıştırma anlık görüntüsü ve manifest | record (gözlenmiş hata); audit (küçülür); retro eylem maddeleri izlenir | Plan onayı; `done`u yalnız insan verir |
| Spec Kit | Salt-okunur analyze; converge; verified / partial / failed | Ekleme-yalnız tasks.md | – | Converge'ün eklediği görevler | Gözden geçirene ait kontrol listesi |
| Kiro | Gereksinim analizi; özellik tabanlı test | Crew: kontrol noktasından sürdürme | Crew panosu: araç, bağlam kullanımı, onay, bellek, günlük | Crew: düzeltme → ders; tekrar → beceri | İzinler; checkpoint ve geri alma |
| Cline Memory Bank | – | Oturumlar arası tek bağ memory bank | – | "update memory bank" ile desen kaydı | Güncellemeyi ister |
| Roo Code | Debug modu: "confirm before fixing" | Alt görev özeti "source of truth" | Arayüzde görev hiyerarşisi | – | Alt görev açma ve kapama onayı |
| Cursor / Aider | – | Kural dosyaları | – | Cursor: önerilen belleğe kullanıcı onayı (ik.) | – |
| 12-Factor | Yapılandırılmış çıktıya LLM yargıç | Olay dizisinden her noktadan sürdürme; çatallama | İnsan okunur iş parçacığı; izleme | – | İnsanla temas araç çağrısı; yüksek riskte döngü kırılır |
| OpenAI | Değerlendirici ajan; korkuluklar; eval | – | (SDK tracing; CMH) | "introspect and improve" | Hata eşiği ve yüksek riskli eylemde insan (ik.) |
| LangChain / LangGraph | – | Checkpointer | – | Prosedürel bellek: yansımayla talimatı yeniden yazma | Anında yazımda kullanıcıya bildirim |
| Letta | `/doctor` ile davranış inceleme | Durum bulutta; makineler arası | `/palace` bellek görünümü | Dreaming; beceri öğrenme | – |
| CrewAI | `guardrail`; `max_iter` | Kalıcı bellek deposu | `match_reasons` (belleğin neden seçildiği) | Görev sonrası otomatik olgu çıkarımı | – |
| Magentic-One | Her adımda `is_request_satisfied`; tekrar ve yalıtımla kıyas testi | Defterler | Defterler her adımda loglanır | Yeniden planda kök neden ve "aynı hatayı tekrarlama" | Halef MAF'ta human-in-the-loop |
| Google ADK | – (eval sayfaları okunmadı) | Kalıcı SessionService; olay günlüğü | Olaylar | Memory Bank birleştirmesi | – |
| Manus | Hatalar bağlamda kalır (ik.) | Dosya sistemi | – | Harness'i daha güçlü modelle sınamak | – |
| Cognition | Temiz bağlamlı gözden geçiren (ik.) | – | – | – | – |
| ADR / docs / günlük / retro | Belgesiz birleştirme engellenir | ADR, git | Günlük | Retro ve postmortem eylem maddeleri | Suçlamasız ilke |

---

## 4. Tekrar eden ortak uygulamalar: "standart seviye" adayları

Bu bölümdeki derleme *çıkarım*dır; dayanakları §2'deki *kaynak diyor* satırlarıdır. Her madde için sırayla şunlar yazıldı:
- **Görüldüğü yer.**
- **İşlev:** ne işe yarar.
- **Yokluğunda:** ne bozulur, başka alt sistemler dahil.
- **Bedel.**
- **Gereksiz:** hangi koşulda gerçekten gereksiz.

### Bağlam

**O1. Katmanlı yükleme ve gözlenebilir tetik.**
- Görüldüğü yer: Kiro steering modları (ik.), Cursor kural türleri (ik.), Roo `.roo/rules-{slug}/`, Aider `read:`, BMAD `persistent_facts` ve işaretçi kuralı, Letta çekirdek/archival (ik.), ADK `{key}`.
- İşlev: Her oturumda gereken az bilgi her zaman yüklenir. İşe, role ya da dosyaya bağlı bilgi tetikle yüklenir. Gerisi istek üzerine okunur.
- Yokluğunda:
  - Ya her şey yüklenir: bağlam çürür, maliyet artar, önemli kural gömülür. BMAD'ın aktardığı ölçüme göre depo talimat dosyaları başarıyı artırmadı, maliyeti %20'nin üstünde artırdı [BM5, ME1].
  - Ya hiçbir şey yüklenmez: her oturum yeniden keşfeder, dersler uygulanmaz (öğrenme bozulur), roller eksik kuralla çalışır.
- Bedel:
  - Tetik tasarımı ve bakımı.
  - İsteğe bağlı katman güvenilmez: "Agents often skip retrieval they have to choose". Aktarılan denemede beceri vakaların %56'sında hiç çağrılmadı [BM5]. Bu yüzden tetik "a path, a file type, a concrete task" gibi gözlenebilir bir şey olmalı, ajanın yargısına kalmamalı [BM5].
- Gereksiz: Bütün yönergeler ve durum birkaç bin tokenı geçmiyorsa ve iş tek oturumluksa.

**O2. Her zaman yüklenen çekirdeği küçük ve türetilemez bilgiye sınırlamak.**
- Görüldüğü yer:
  - BMAD: "Extra context is a cost"; "When the evidence supports ten lines, ten lines is the deliverable".
  - Kiro: "one domain per file" (ik.).
  - 12-Factor faktör 3.
  - Aider: "small markdown file".
  - BMAD'ın kendi prompt kuralı: "Length and ambiguity are paid on every run; a corner case is paid only when it occurs" [BM12].
- İşlev: Her çağrıda ödenen bağlamı, davranışı değiştiren satırlarla sınırlamak.
- Yokluğunda: Çekirdek büyür, önemli kural gömülür. Türetilebilir kopyalar bayatlar ve yanlış yönlendirir; eski bilgi güncel sanılınca süreklilik ve doğrulama bozulur.
- Bedel: Her satıra "bu satır silinirse davranış değişir mi?" testi [BM5] ve düzenli denetim.
- Gereksiz: Çekirdek zaten tek ekranlıksa ayrı ölçüm yapmak gereksiz olabilir; test yine uygulanır.

**O3. Alt ajan yalıtımı ve açık aşağı/yukarı aktarım.**
- Görüldüğü yer: Roo Boomerang, LangChain "isolate", Manus, OpenAI "agents as tools", Kiro Crew "isolated subagents", Letta alt ajanları, BMAD #2557 (planlayıcı keşfi alt ajana bırakır).
- İşlev: Ayrıntılı okuma alt ajanın bağlamında kalır, ana bağlama yalnız sonuç gelir. Aşağıya giden bağlam açıkça yazılır.
- Yokluğunda:
  - Ana bağlam dolar, otomatik sıkıştırma erken gelir, karar izi düşer (süreklilik).
  - Aktarım açık değilse alt ajan bağlamsız karar verir. Cognition'ın uyarısı: çatışan örtük kararlar.
- Bedel:
  - Her görev tanımına gereken bağlamı yazmak.
  - Dönen özetin kayıpları (R05 #17).
  - "Only this summary returns" [RO3]: özet tek kanıt olur.
- Gereksiz: İş, ana bağlamda birkaç kısa okumayla bitiyorsa.

**O4. Koordinatörün ayrıntı okumaması.**
- Görüldüğü yer: Roo Orchestrator (gerekçesiyle), BMAD #2557, Manus planlayıcı, Magentic orkestratör (web ve dosya işini uzmanlara verir).
- İşlev: Yönlendirme ve karar bağlamını temiz tutmak.
- Yokluğunda: Koordinatör bağlamı ham okumayla kirlenir ("context poisoning" [RO3]). Plan izi ve kararlar sıkıştırmada kaybolur. Maliyet artar.
- Bedel: Koordinatör bilgiyi ikinci elden alır. Kararı taşıyan iddiaları kaynağından kontrol etmesi gerekir (A003 §3.3 kuralı).
- Gereksiz: Okunacak şey kısa ve karar için kritikse, koordinatör kendisi okumalı. Örnek: Batu'nun mesajı, alt ajanın dayandığı tek alıntı.

**O5. Sıkıştırma politikası.**
- Görüldüğü yer: Manus (ik. ve MA2), LangChain "compress", 12-Factor faktör 9, CrewAI `respect_context_window`, Roo "only summary returns".
- İşlev: Tam ve kompakt temsil ayrılır: eski ayrıntı dosyaya konur, bağlamda yerine işaretçi kalır. Özet şemalı alanlarla üretilir. Hata izleri seçilerek tutulur.
- Yokluğunda: Otomatik sıkıştırma gelişigüzel kaybettirir. Niteleyiciler düşer (R05 #17; R06 §3.6). Açık sorular ve reddedilen seçenekler kaybolur. Yeniden yükleme pahalılaşır.
- Bedel: Özet şeması; ayrıntıyı dosyaya boşaltma disiplini.
- Gereksiz: Bağlam hiçbir zaman eşiğe yaklaşmıyorsa. Bu ortamda eşik %80 (ORTAK).

### Bellek

**O6. Repo içinde, sürümlü, insan okunur dosya belleği.**
- Görüldüğü yer: Cline, Roo memory bank, BMAD (commit edilen takım dosyası ve AGENTS.md bloğu), Kiro steering ve specs, Letta MemFS, Manus dosya sistemi, ADR, docs-as-code.
- İşlev: Bellek oturum ve makine kaybından bağımsız olur. Farkı görülür, geri alınabilir.
- Yokluğunda: Bellek konuşmada kalır; VM geri alınınca ya da sıkıştırmada kaybolur. Kimin neyi ne zaman değiştirdiği görünmez (gözlemlenebilirlik). Doğrulayıcı belirli bir sürüme bağlanamaz.
- Bedel: Commit disiplini. Dosya çoğalması riski; EXP-006 53 bin kelimeye ulaştı (R02).
- Gereksiz: Bu ortamda değil; repo tek kalıcı yüzey (ORTAK).

**O7. Bellek türlerini ve kapsamlarını ayırmak.**
- Görüldüğü yer:
  - Cline: altı dosya.
  - LangGraph: semantik / epizodik / prosedürel; kısa / uzun.
  - Letta: çekirdek / recall / archival (ik.).
  - ADK: oturum / `user:` / `app:` / `temp:`.
  - CrewAI: kapsam ağacı; özel / paylaşılan.
  - Kiro Crew: global / `repo_scope` / role özel.
  - BMAD: uygulama bağlamı / planlama bağlamı; takım / kişisel.
- İşlev: Türlerin güncelleme hızı, okuyucusu ve budama kuralı farklıdır. Ayrı dosya ya da alanda tutulunca her birine kendi kuralı uygulanır.
- Yokluğunda: Hızlı değişen durum ile yavaş değişen kararlar aynı yerde kalır; ya durum bayatlar ya kararların üstüne yazılır. Geçmişte doğru olan kayıt ile bugün geçerli kayıt ayrışmaz (R10'un sınama sorusu).
- Bedel: Dosya sayısı ve "hangi bilgi nereye" kuralı.
- Gereksiz: Birkaç oturumluk kısa işte.

**O8. Tanımlı güncelleme anları.**
- Görüldüğü yer: Cline (dört tetik ve komut), BMAD (refresh / record / audit), CrewAI (her görevden sonra), ADK (oturum sonunda), LangGraph (anında ya da arka planda), Magentic (her adımda ilerleme defteri, takılmada görev defteri).
- İşlev: Belleğin ne zaman yazılacağını rastlantıdan çıkarmak; sıkıştırmadan ve oturum sonundan önce yazmak.
- Yokluğunda:
  - Yazım unutulur. R02: Batu'nun düzeltmelerinin çoğu yalnız özetle yaşadı.
  - Ya da her adımda yazılır. Manus'ta eylemlerin yaklaşık üçte biri plan güncellemesine gitti [MA2].
- Bedel: Tetik disiplini ve biraz tekrar.
- Gereksiz: Tek oturumluk işte.

**O9. Budama ve yerine koyma.**
- Görüldüğü yer: BMAD (audit küçülür ya da eşit kalır; emeklilik kuralı), CrewAI (`forget(scope)`, tazelik bozunumu, `delete`), ADR (yerine koyma, değiştirme yok), Manus (kompakta çevirme), LangGraph ("remove or forget stale information").
- İşlev: Bellek büyümesini ve çelişkileri sınırlamak; bunu geçmişi kaybetmeden yapmak.
- Yokluğunda:
  - Bellek büyür, O1 ve O2 bozulur.
  - Çelişkili kayıtlar yan yana kalır; bağlam yanlışlaşır, doğrulama ve karar kalitesi düşer.
  - Silmeyle budanırsa "neden" sorusu cevapsız kalır.
- Bedel: Periyodik denetim ve yerine koyma bağlantıları.
- Gereksiz: Ömrü tek aşama olan geçici notlarda.

**O10. Köken, güven ve kapsam etiketi.**
- Görüldüğü yer: CrewAI (`source`, `private`), Google (köken ve güven sırası; ik.), Magentic (olgu sınıfları), Kiro Crew (`repo_scope`), ADK önekleri. BMAD eski becerisini "no way to tell an inference from a confirmed fact" diye eleştirdi [BM5].
- İşlev: Kaydın kimden geldiğini, ne kadar güvenilir olduğunu ve nerede geçerli olduğunu bilmek.
- Yokluğunda: Çıkarım gerçek gibi taşınır (R04 (b)3). Batu'nun sözü ile model yorumu karışır; A003 §3.1'deki A–B–C ayrımı bozulur. Çatışmada hangi kaydın geçerli olduğu bilinmez.
- Bedel: Her kayda etiket. A003'ün kanıt dili bunun yarısını zaten veriyor.
- Gereksiz: Değil.

### Roller

**O11. Proje düzeyinde, sürümlü rol dosyası** (anatomisi §5'te).
- Görüldüğü yer: BMAD, Roo, CrewAI, Kiro özel ajanları, OpenAI `Agent`. Claude Code karşılığı `.claude/agents/`; R07'nin alanı; cloud'da repodan yüklenir (R01 `multiagent` ekseni).
- İşlev: Rolü her seferinde yeniden biçmemek. Rol sürümlü ve gözden geçirilebilir olur. Dersler role işlenebilir.
- Yokluğunda: Aynı rol farklı görev tanımlarında farklı kurallarla çalışır. Dersin konacağı yer olmaz (öğrenme). Araç sınırı tanımlanamaz (güvenlik). Rolün davranışı izlenemez.
- Bedel:
  - Bakım.
  - Rol şişmesi. BMAD'da 5 ay içinde kataloğun küçülmesi bunun izi: 3 persona birleştirildi, çekirdek beceri 14'ten 8'e indi.
  - Yanlış soyutlamanın erken donması.
- Gereksiz: Kalıp bir kez kullanılacaksa. Kiro Crew'un "Repeated patterns become reusable skills" ilkesi ile A003'ün "üç tekrar" kuralı bu koşulu anlatıyor. Batu ise çekirdek rollerin baştan kalıcı olmasını istedi (K-007).

**O12. Rol başına araç ve yazma kapsamı.**
- Görüldüğü yer: Roo (`groups`, `fileRegex`; orkestratörde araç yok), BMAD v4 (olumsuz izin; story'de izinli bölümler), CrewAI (`tools`, `allow_delegation`), Kiro izinleri, Kiro Crew. Claude Code `tools` alanı R07'nin alanı.
- İşlev: Rolün etkisini sınırlamak; tek yazıcı ilkesini tavsiye olmaktan çıkarıp zorlamaya yaklaştırmak.
- Yokluğunda: Okuyucu ajan yanlışlıkla yazar. Paralel yazmalar çakışır (süreklilik). Kayıtlar güvenilmez olur.
- Bedel: İzin yapılandırması; zaman zaman işin engellenmesi.
- Gereksiz: Değil.

**O13. Tek biçimli çıktı sözleşmesi.**
- Görüldüğü yer: Manus (şemayı planlayıcı tanımlar; ik.), Magentic (JSON defter), Roo (`attempt_completion` özeti), CrewAI (`expected_output`), BMAD ("findings in one shape"; "Zero findings is a valid outcome" [BM7]), Spec Kit hüküm sözlüğü.
- İşlev: Dönüşleri karşılaştırılabilir ve denetlenebilir yapmak.
- Yokluğunda: Özetler niteleyici kaybeder. Birleştirme zorlaşır. Kanıt izi kopar.
- Bedel: Şemanın bakımı.
- Gereksiz: Değil.

### Plan ve yaşam döngüsü

**O14. Niyet ve ölçüt → tasarım → görev ayrımı; hatayı sahibi olan katmana döndürmek.**
- Görüldüğü yer: Spec Kit (SK1 §7), Kiro (ik.), BMAD ("goes back to that layer"), R05 #8.
- İşlev: Hata ait olduğu katmanda düzeltilir; niyet sessizce değişmez.
- Yokluğunda: Aşağı akışta yamalanır. Plan "hep doğruymuş" görünür (R05 #9). Batu'nun ölçütü kayar.
- Bedel: Artefakt sayısı.
- Gereksiz: Niyeti açık, küçük işlerde. BMAD: "Small changes go straight to build" [BM1].

**O15. Törenin risk ve büyüklüğe göre ölçeklenmesi.**
- Görüldüğü yer: BMAD (tören incelemeden sonra seçilir; ölçütler niyet boşlukları, geri alınamaz eylemler, ayak izi), Spec Kit (isteğe bağlı kapılar), OpenAI (önce tek ajan; ik.), 12-Factor (küçük ajan).
- İşlev: Denetimin ağırlığını riske göre ayarlamak.
- Yokluğunda:
  - Her şeye tören: ilerleme durur, Batu yorulur. A2'deki "boş bir tören" kaygısı (R03 §3).
  - Hiçbir şeye tören: hatalar kaçar.
- Bedel: Bir sınıflandırma adımı.
- Gereksiz: Değil. A003 §3.8 ilkeyi koymuştu; ölçütleri koymamıştı.

**O16. Oturum ya da çağrı başına tek iş birimi.**
- Görüldüğü yer: BMAD ("fresh chat"; bilet başına bir Build, yaklaşık 500 satır; "exactly one ticket per invocation" [BM10]), Spec Kit (büyük özellikte sınırlı implement), 12-Factor (3–10 adım), Roo (alt görev).
- İşlev: Bağlamı ve hatanın yayılmasını sınırlamak; doğal kontrol noktası yaratmak.
- Yokluğunda: Uzun oturumda bağlam çürür. Sıkıştırmada durum kaybolur. VM geri alınınca daha çok iş gider (ORTAK).
- Bedel: Daha çok devir ve devir notu disiplini.
- Gereksiz: Değil.

### Süreklilik ve gözlemlenebilirlik

**O17. İlerleme defteri, durma sayacı, eşikte yeniden plan ya da yükseltme.**
- Görüldüğü yer: Magentic (beş soru; `max_stalls`=3), 12-Factor (yaklaşık 3 deneme sonra insan), BMAD v4 ("3 failures attempting to implement or fix something repeatedly" → HALT [BM11]), OpenAI (hata eşiği; ik.), CrewAI (`max_iter`), R05 #10 ve #24.
- İşlev: Hareketi ilerlemeden ayırmak; döngüyü erken yakalamak.
- Yokluğunda: Ajan döner, bütçe tükenir, durumu Batu fark eder. A003'e göre Batu'nun her hatırlatması bir kusurdur.
- Bedel: Her adımda kısa bir öz değerlendirme; yanlış pozitifler.
- Gereksiz: Tek adımlık işte.

**O18. Tek yazıcı; kabul insanda.**
- Görüldüğü yer: Cognition 2026 (ik.), Manus (yazan alt ajana tam bağlam; ik.), BMAD (işçi sıradaki işi seçmez; `done`u yalnız insan verir), Magentic (defterleri yalnız orkestratör günceller), R05, R06.
- İşlev: Çatışan örtük kararları önlemek; tek doğruluk kaynağı tutmak.
- Yokluğunda: Paralel yazmalar çelişir. STATE güvenilmez olur. Birleştirme işi Batu'ya kalır.
- Bedel: Koordinatör darboğazı (A003 §6).
- Gereksiz: Yazılan yüzeyler tamamen ayrık ve hiç birleşmeyecekse.

**O19. Ekleme-yalnız çalışma günlüğü ve ADR biçiminde karar kaydı.**
- Görüldüğü yer: BMAD (`memlog`, `.decision-log`), 12-Factor (olay dizisi), ADK (`append_event`), ADR, Roo (`decisionLog`), günlük defteri (ik.).
- İşlev: "Ne oldu" (günlük) ile "ne karar verildi ve neden" (ADR) ayrı tutulur. Geçmiş yeniden yazılmaz. Kararın "sonuçlar" alanı neyi kolaylaştırıp neyi zorlaştırdığını söyler.
- Yokluğunda: Devirde "neden" kaybolur. Eski karar sessizce değişir. Retrospektif kanıtsız kalır.
- Bedel: Yazım zamanı. Günlük büyür; özet ve budama gerekir (O9).
- Gereksiz: Değil.

**O20. Neyin hangi talimat sürümüyle koştuğunun izi.**
- Görüldüğü yer: BMAD (içerik adresli çalıştırma kaydı ve manifest), Magentic (defter her adımda loglanır), Kiro Crew (pano), 12-Factor (iş parçacığı = gözlemlenebilirlik), R06 ("hangi brief sürümü").
- İşlev: Sonucu, onu üreten talimat sürümüne bağlamak.
- Yokluğunda: Hatanın görev tanımından mı, modelden mi, kaynaktan mı geldiği ayrılamaz. Ders "işe yaradı mı" diye doğrulanamaz (öğrenme).
- Bedel: Görev tanımlarını sürümlü saklamak. EXP-007 bunu `briefs/` ile kısmen yapıyor.
- Gereksiz: Değil.

### Doğrulama

**O21. Temiz bağlamlı, yöntem odaklı gözden geçiren; her bulguya hüküm.**
- Görüldüğü yer:
  - Cognition 2026 (ik.).
  - BMAD: niyete kör katman; doğrulama boşluğu katmanı; niyet uyumu denetçisine niyetin birebir verilmesi; üst ajanın görev tanımını yeniden anlatma yasağı; "at least ten concrete findings and asking what is missing".
  - Spec Kit: salt-okunur analyze.
  - R05 #11.
- İşlev: Üreticinin kör noktasını görmek.
- Yokluğunda: Değerlendirme kendini onaylar. Bu, EXP-006'daki ana kayma (R02 §3).
- Bedel: Ek ajan maliyeti. Aynı model kullanıldığı için sonuç bağımsız doğrulama değil, "taze gözle karşı-okuma"dır (A003 §3.3).
- Gereksiz: Geri alınabilir, düşük riskli küçük adımlarda.

**O22. Kanıtsız "bitti" yok; açık hüküm sözlüğü.**
- Görüldüğü yer: Spec Kit ("Missing verification is not a successful fix"), BMAD retro ("A claim it can't point at doesn't make the report"; üçlü hüküm), Magentic (gerekçeli `is_request_satisfied`), R05 #12–13.
- İşlev: "Bitti" iddiasını kanıta ve sabit bir sözlüğe bağlamak.
- Yokluğunda: Sahte ilerleme. Batu: "Sahte ilerleme artık çok ucuz" (R03 §2).
- Bedel: Kanıt toplamak.
- Gereksiz: Değil.

### Öğrenme

**O23. Kanıta dayalı retrospektif ve önceki eylem maddelerinin takibi.**
- Görüldüğü yer: BMAD (retro; `action_items` `sprint-status.yaml`'da izlenir), Scrum (iyileştirme sonraki sprint iş listesine girer; ik.), SRE (eylem maddeleri, incelenmeyen postmortem; ik.), Kerth (suçlamasız; ik.).
- İşlev: Dersi işe dönüştürmek ve dönüşüp dönüşmediğini izlemek.
- Yokluğunda: Aynı hata tekrarlanır. Ders kaydı davranış değişimi sanılır (R04 (d)7).
- Bedel: Her aşama sonunda zaman.
- Gereksiz: Aşama çok kısaysa ve hiç olay yoksa. "Olay yok" bulgusu da kayda geçer.

**O24. Ders kabul testi, kapsamı ve emekliliği.**
- Görüldüğü yer: BMAD (yalnız gözlenmiş hata; tarama bulgusu kural değil soru olur; emeklilik kuralı), Kiro Crew (global / repo / role özel ders), LangGraph ve Letta (yansıma ile talimat güncelleme; dikkatle), R05 #18–20.
- İşlev: Dersin ne zaman kurala dönüşeceğini, kime uygulanacağını ve ne zaman kalkacağını belirlemek.
- Yokluğunda: Kurallar birikir (R05'teki Hermes örneği) ya da ders kaybolur.
- Bedel: Kanıt eşiği yüzünden bazı dersler gecikir.
- Gereksiz: Değil.

**O25. Harness'in periyodik sadeleştirilmesi.**
- Görüldüğü yer: Manus (beş kez yeniden yazım; daha güçlü modelle sınama), BMAD ("deletes about 1,900 more lines than it adds"; "do not add instructions for exotic cases" [BM12]), 12-Factor ("What if LLMs get smarter?").
- İşlev: Yapının modelin önünde engel olmasını ve düzenin ağırlaşmasını önlemek (A003 §6 riski).
- Yokluğunda: Düzen şişer. Batu'nun "ağır repo" eleştirisi tekrar eder (R02 §6).
- Bedel: Periyodik gözden geçirme.
- Gereksiz: Değil.

### İnsan etkileşimi ve maliyet

**O26. Yapılandırılmış, eşikli insan teması.**
- Görüldüğü yer: 12-Factor (faktör 7–8), OpenAI (ik.), Roo (onaylar), BMAD (plan onayı; `done`), Spec Kit (gözden geçirene ait liste), Kiro (izinler).
- İşlev: İnsanın dikkatini yalnız eşikte ve yetki konusunda harcamak.
- Yokluğunda: Ya Batu gizli koordinatöre döner ya da riskli karar insansız verilir.
- Bedel: Eşiklerin tanımı.
- Gereksiz: Değil.

**O27. Önbellek dostu bağlam (aday).**
- Görüldüğü yer: Manus (KV-cache, kararlı önek, ekleme-yalnız; ik.), Aider (salt-okunur convention dosyası önbelleğe alınır), MA2 (sistem talimatları ve eski araç sonuçları önbelleklenir).
- İşlev: Maliyeti ve gecikmeyi düşürmek. Manus'un aktardığı önbellekli/önbelleksiz fiyat farkı 10 kat.
- Yokluğunda: Aynı bağlam her çağrıda tam fiyatla ödenir. A003 §6: iki araştırma turunda alt ajanlar yaklaşık 4 milyon token harcadı. Önbellek yoksa haftalık limit daha çabuk dolar. *çıkarım*
- Bedel: Çekirdek dosyaları sık değiştirmemek.
- Gereksiz: Maliyet sınırı yoksa. Claude Code'un önbellek davranışı R07'nin alanı; bu not doğrulamadı.

---

## 5. Kalıcı rol tanımlarının ortak anatomisi

| Alan | İşlev | Görüldüğü yer |
|---|---|---|
| Kimlik (ad, slug, id) | Rolü sabit adla çağırmak ve sürümlemek | BMAD (ad, unvan, alan sabit), Roo `slug`/`name`, CrewAI dosya adı, OpenAI `Agent` |
| Kısa açıklama ve "ne zaman kullanılır" | Koordinatörün ya da aracın rolü seçmesi | Roo `description` + `whenToUse`; BMAD v4 `whenToUse`; Kiro `auto` açıklaması (ik.); Cursor "Agent Requested" açıklaması (ik.) |
| Rol tanımı ve sorumluluk | Rolün işi ve uzmanlığı | Roo `roleDefinition`, BMAD `role`/`identity`, CrewAI `role`, OpenAI `instructions` |
| Hedef (başarı yönü) | Rolün kararlarını yönlendiren amaç | CrewAI `goal` ("guides the agent's decision-making"), BMAD `focus`, `principles` |
| İlkeler ve olumsuz kısıtlar | Yapmayacağı şeyler | BMAD v4 "NOT allowed to implement stories or modify code EVER!"; Roo `customInstructions`; BMAD: "Negative constraints over positive guidance, which measured better", izin verilen alternatifle birlikte yazılır [BM5] |
| Araç ve dosya erişimi | Etkiyi sınırlamak | Roo `groups` + `fileRegex`; CrewAI `tools`, `allow_code_execution`; BMAD v4 izinli story bölümleri; Kiro izinleri |
| Model seçimi | Maliyet ve yetenek dengesi | Roo "Sticky Models", CrewAI `llm`, Magentic (orkestratöre güçlü model), Manus (görev düzeyinde yönlendirme; ik.), BMAD (`implementation_handoff` yapılandırma anahtarı) |
| Her zaman yüklenen bağlam | Rolün başlangıç bilgisi | BMAD `persistent_facts`, `activation_steps_*`, v4 `devLoadAlwaysFiles`; CrewAI `knowledge_sources`; Roo `.roo/rules-{slug}/` |
| Prosedürler, komutlar, bağımlılıklar | Rolün iş yapma yolları | BMAD `menu`, `commands`, `dependencies` (görev, şablon, kontrol listesi); Kiro ve Letta becerileri |
| Çıktı sözleşmesi | Dönüş biçimi | CrewAI görevde `expected_output`; Manus şeması (ik.); Roo `attempt_completion`; BMAD tek biçimli bulgu |
| Durma, bütçe, yükseltme | Döngüyü ve israfı sınırlamak | CrewAI `max_iter` (20), `max_execution_time`, `max_retry_limit` (2); BMAD v4 HALT koşulları; Magentic `max_stalls` |
| Devretme hakkı | Başka role iş verebilir mi | CrewAI `allow_delegation` (varsayılan False); Roo orkestratörü `new_task`; OpenAI handoffs |
| Rol belleği | Role özgü birikim | BMAD `_bmad/_memory` (alpha.17); CrewAI ajanın özel kapsamı; Kiro Crew üyesinin özel dersleri; Letta ajana özgü beceri ve bloklar |
| Özelleştirme katmanları ve sürüm | Takım ve kişisel ayarı ayırmak, güncellemede kaybetmemek | BMAD 3 katman, "No removal"; Roo proje (`.roomodes`) / küresel; CrewAI `.jsonc` repoda |
| Persona ve üslup (isteğe bağlı) | Etkileşim tonu | BMAD `communication_style`, `icon`; CrewAI `backstory` ("personality"); Roo "specialized personas" |

**Persona hakkındaki kanıt.**
- BMAD'ın küçük A/B denemesi: inceleme personası kalan hataları yakalama oranını değiştirmedi, yöntem şartı değiştirdi [BM2]. *kaynak diyor; tedarikçinin iç ölçümü*
- Manus insan benzeri rol bölümünden bilinçli kaçınıyor [MA2]. *kaynak diyor*
- 12-Factor, role/goal/personality alanlarıyla tanımlanan hazır ajan kalıbını kara kutu diye eleştiriyor [TF2]. *kaynak diyor*
- Magentic uzmanlarını yetenekle tanımlıyor [MS1]. *kaynak diyor*
- Sonuç: yerleşik ve tekrar eden şey alanların işlevsel çekirdeğidir: kimlik, ne zaman, sorumluluk, hedef, kısıt, araç/yazma, bağlam, prosedür, çıktı, durma. Persona alanları kanıtsız süstür. *çıkarım*

**Rolün kendini geliştirmesi.**
- Letta kendi bloklarını ve becerilerini yeniden yazıyor; "dreaming" ile birleştiriyor [LE2].
- Kiro Crew düzeltmeleri derse, tekrar eden kalıpları beceriye çeviriyor [KR2].
- LangGraph prosedürel belleği yansımayla güncelliyor [LC2].
- BMAD aynı işi insan onayıyla yapıyor: "Every write is shown first"; "It asks before it writes" [BM2, BM4].
- Hepsinde ortak çizgi: kendini değiştiren içerik ya insan onaylı ya da görünür ve düzenlenebilir ("stay visible and editable" [KR2]). *çıkarım*
- Rol tanımının kimin yetkisiyle değişeceği Foundation tarafında R10'un konusu.

---

## 6. Bellek yapılarının ortak anatomisi

### 6.1 Ayrı tutulan türler

| Tür | İçerik | Örnekler | Değişme hızı |
|---|---|---|---|
| Çalışma durumu | Şu anki odak, sıradaki adım, açık kararlar | Cline `activeContext.md`; Magentic ilerleme defteri; ADK `temp:` ve oturum state'i; Manus `todo.md` | Her adım ya da iş kalemi |
| Proje özü ve amaç | Kapsam, neden, başarı | Cline `projectBrief`, `productContext`; Kiro `product.md` (ik.); BMAD brief ve PRD; Letta çekirdek blok (ik.) | Aşamalar boyunca yavaş |
| Yöntem ve sistem desenleri | Mimari, kurallar, teknik bağlam | Cline `systemPatterns`, `techContext`; Kiro `tech.md`, `structure.md` (ik.) | Yavaş |
| İlerleme | Yapılan, kalan, bilinen sorunlar | Cline `progress.md`; BMAD `sprint-status.yaml`; Spec Kit `tasks.md` | İş kalemi sonunda |
| Kararlar ve gerekçe | Karar, bağlam, sonuç, durum, yerine koyan | ADR; Roo `decisionLog.md`; BMAD `.decision-log` | Karar anında; değişmez |
| Olay günlüğü (epizodik) | Ne oldu, sırayla | ADK olayları; 12-Factor iş parçacığı; BMAD `memlog`; Letta recall (ik.); Kiro Crew günlükleri | Sürekli; ekleme-yalnız |
| Olgular ve güven sınıfı | Verili ya da doğrulanmış / aranacak / türetilecek / tahmin | Magentic olgu listesi; CrewAI `source`; Google köken (ik.) | Yeni kanıtla |
| Prosedürel | Kurallar, beceriler, rol talimatı | Kiro steering; Cursor kuralları; Roo kuralları; Letta becerileri; LangGraph prosedürel bellek | Nadiren; onaylı |
| Dersler ve tuzaklar | Gözlenmiş hata ve karşılığı | BMAD "record"; Kiro Crew dersleri | Olay sonrası |
| Arşiv ve ham kaynak | Tam araç sonuçları, belgeler, eski konuşmalar | Letta archival (ik.); ADK MemoryService; Manus'ta dosyaya konan tam sonuçlar | Ekleme |

Türlere dik bir ikinci eksen de ayrı tutuluyor: **kapsam.**
- ADK: oturum / kullanıcı / uygulama / çağrı.
- Kiro Crew: global / repo / role özel.
- CrewAI: paylaşılan / özel.
- BMAD: takım (commit edilen) / kişisel (git dışı).

### 6.2 Nasıl güncelleniyor
- **Açık komutla:** Cline'da "update memory bank" (bütün dosyalar gözden geçirilir). BMAD'da refresh / record / audit.
- **İş sınırında otomatik:** CrewAI her görevden sonra olgu çıkarır. ADK oturum bitince belleğe alır. Magentic her adımda ilerleme defterini, takılmada görev defterini günceller.
- **Arka planda:** LangGraph arka plan yazımı. Letta "dreaming". Vertex Memory Bank birleştirmesi.
- **Olay üzerinden:** ADK'de state değişikliği yalnız kayıtlı bir olayla yapılır.
- **İnsan onayıyla:** BMAD her yazımı önce gösterir ve commit etmez. Cursor arka planda üretilen belleği kullanıcı onayına sunar (ik.).
- **Profil mi, koleksiyon mu?**
  - Tek belgeyi güncellemek: büyüdükçe hataya açık.
  - Yeni kayıt eklemek: silme ve güncelleme zorlaşır; kimi model fazla ekler, kimi fazla günceller [LC2].

### 6.3 Nasıl budanıyor ve unutuluyor
- **Denetimle küçültme:** Denetim sonunda blok küçülür ya da eşit kalır, asla büyümez [BM4].
- **Emeklilik:** Kural, konusu ortadan kalkınca ya da bir araçla zorlanınca kalkar. "Nothing broke lately" gerekçe sayılmaz [BM4, BM5].
- **Hiç saklamamak:** Türetilebilir bilgi baştan saklanmaz [BM5].
- **Kapsamla unutma:** `forget(scope)`. Tazelik yarı ömrü silmede değil, sıralamada kullanılır [CR2].
- **Birleştirme:** Benzer kayıtta `keep` / `update` / `delete` / `insert_new` kararı [CR2]. Vertex Memory Bank birleştirmesi [GO3].
- **Sıkıştırma:** Tam temsil kompakt işaretçiye, o da şemalı özete çevrilir [MA2].
- **Yerine koyma:** ADR'de eski karar silinmez, durumu "superseded" olur [AD2, AD3].
- **Kaynak kaybolunca:** "When a claim's source disappears, the claim is fixed or removed, never silently pointed at a different document that still mentions it." [BM5]
- **Açık:** Cline Memory Bank'te budama kuralı yok [CL1]. *gözledim*

### 6.4 Çatışma ve köken
- CrewAI çelişen kaydı birleştirmede siler ("outdated, superseded, or contradicted").
- Google güven sırası önerir (ik.).
- ADR durum alanı taşır.
- Magentic tahmini doğrulanmış olgudan ayırır ve yeniden planda tahmini doğrulanmış olguya "taşır".
- Otomatik silme ile yerine koyma arasında bir seçim var. Denetlenebilirlik isteniyorsa yerine koyma tercih ediliyor: ADR ve BMAD'ın insan onaylı silmesi. *çıkarım*

---

## 7. A003 v0 ile karşılaştırma

Durum sütunu: **var**, **kısmen** ya da **yok**. Dayanak sütunu A003 bölümüne atıftır.

| Ortak uygulama | v0 | v0 dayanağı | Standart seviyeye göre eksik |
|---|---|---|---|
| O1 Katmanlı yükleme | kısmen | §3.4 okuma yolu; §3.9 "Ana oturum az okur" | Her zaman / tetikle / istek üzerine katmanları ve gözlenebilir tetikler yok; CLAUDE.md'nin içeriği ve boyutu tanımsız |
| O2 Küçük çekirdek | kısmen | §3.6 "tek ekranı geçmez" | Çekirdeğe kabul testi (türetilemez olmalı, davranışı değiştirmeli) yok |
| O3 Yalıtım ve açık aktarım | var | §3.3 görev tanımı; dönüş biçimi | "Özet tek kanıt" riskine karşı kural yok |
| O4 Koordinatör okumaz | var | §3.9 | — |
| O5 Sıkıştırma politikası | yok | §3.9 "yeniden yüklemek ucuz olur" (amaç, mekanizma değil) | %80 sıkıştırmadan önce neyin yazılacağı, özet şeması, tam/kompakt ayrımı yok |
| O6 Repo belleği | var | §3.4 "Repo bellektir"; §3.6 her iş kaleminden sonra kayıt | — |
| O7 Tür ve kapsam ayrımı | kısmen | §5: STATE, PLAN, DECISIONS, READING-LOG | Olay günlüğü, olgu defteri, dersler, prosedürel bellek (rol dosyaları) ve kapsam ekseni yok |
| O8 Güncelleme anları | kısmen | §3.6 kontrol noktaları | Sıkıştırma öncesi ve oturum sonu tetikleri yok |
| O9 Budama ve yerine koyma | yok | §3.7 "kabul edilen plan sürümü korunur" (yalnız plan için) | Bellek denetimi, emeklilik kuralı, kararlar için yerine koyma yok |
| O10 Köken, güven, kapsam | kısmen | §3.1 A–B–C; §3.3 kanıt dili | Kayıt düzeyinde köken alanı ve çatışma kuralı yok |
| O11 Rol dosyası | yok (bilinçli erteleme) | §3.2 "tek soruluk, geçici çalışanlar"; §3.3 "üç kez tekrarlanınca" | Batu reddetti (K-007); anatomi tanımsız |
| O12 Araç ve yazma kapsamı | kısmen | §3.2 "kalıcı dosyaları tek başıma yazarım" | Role göre araç sınırı ve zorlama yok |
| O13 Çıktı sözleşmesi | var (metin olarak) | §3.3 madde 8 | Sabit şema ya da başlık yok |
| O14 Niyet → tasarım → görev | kısmen | §3.1 bitti tanımı; §3.6 | "Hatayı sahibi olan katmana döndür" kuralı yok |
| O15 Tören ölçekleme | var (ilke) | §3.8 son madde | Sınıflandırma ölçütleri (geri alınamazlık, ayak izi, niyet boşluğu) yok |
| O16 Oturum başına iş birimi | kısmen | §3.9 okuma sırası | İş kalemi ya da oturum büyüklüğü ölçüsü yok |
| O17 İlerleme defteri ve sayaç | kısmen | §3.6 "hareket var, ilerleme yok"; §3.7 üç eleştiri sınırı | Adım düzeyinde "döngüde miyiz / ilerliyor muyuz" soruları ve sayaç yok |
| O18 Tek yazıcı, insan kabulü | var | §3.2; §3.8 tamamlanma katları | — |
| O19 Günlük ve ADR | kısmen | §3.7 tarihli değişiklik notu; §5 DECISIONS | Ekleme-yalnız çalışma günlüğü yok; kararda "sonuçlar" ve "durum / yerine koyan" alanları yok |
| O20 Talimat sürümü izi | kısmen | §3.4 okuma kaydı (kaynak sürümü) | Hangi ajanın hangi görev tanımı sürümüyle koştuğu kaydı yok |
| O21 Temiz bağlamlı gözden geçiren | var | §3.3 karşı-okuyucu gerekçeyi görmez | Yöntem şartları (asgari bulgu sayısı, "ne eksik?", mercekler) yok |
| O22 Kanıtsız bitti yok | var | §3.8 tamamlanma katları | Hüküm sözlüğü (doğrulandı / kısmen / başarısız / doğrulanamadı) yok |
| O23 Retrospektif | kısmen | §3.10 | Aşama sonu ritmi ve önceki eylem maddelerinin takibi yok |
| O24 Ders kabulü ve emekliliği | kısmen | §3.10 "doğrulanmadı" | Kabul eşiği, kapsam ve emeklilik yok |
| O25 Sadeleştirme | kısmen | §6 "düzen ağırlaşabilir" | Mekanizma yok |
| O26 Eşikli insan teması | var | §3.6 karar katmanları; §3.9 üç biçim | Durma sayacı aşımı gibi otomatik eşikler yok |
| O27 Önbellek dostu bağlam | yok | §6 maliyet riski | Mekanizma yok |

**v0'ın hiç içermedikleri:**
- sıkıştırma politikası (O5);
- budama ve yerine koyma (O9);
- rol dosyası ve anatomisi (O11);
- önbellek ve maliyet (O27);
- O7 içinde olay günlüğü, olgu defteri, dersler ve kapsam ekseni;
- O17 içinde sayaç.

v0 bunların yerine ilke cümleleri koymuş ("ağırlaşabilir", "maliyet", "ucuz olur"). Batu'nun U004'teki "söz geniş, çıktı dar" eleştirisinin somut karşılığı bu listedir. *çıkarım*

---

## 8. EXP-007'ye aktarım: ne alınır, ne farklı yapılır

Bu bölüm *çıkarım*dır. Claude Code'a değen maddelerde cloud geçerliliği parantezde verilmiştir. Kaynağı R01 ve ORTAK'tır; R07 doğrulayacaktır.

**Bağlam**
- **Al:** Üç katman kur.
  - Çekirdek: CLAUDE.md ve STATE. Küçük, türetilemez, sık değişmeyen. Cloud'da CLAUDE.md taşınır (ORTAK).
  - Tetikle: aşama README'leri ve rol dosyaları. Tetik bir yol ya da iş türüdür.
  - İstek üzerine: `research/`, `sources/`, Foundation, studies. Dizin ve harita dosyasıyla.
- **Al:** Sıkıştırma öncesi yazım kuralı (O5, O8). Bağlam %80'e varmadan STATE ve günlük güncel olmalı. Özet başlıkları R05 #17'deki sabit başlıklar olabilir.
- **Farklı yap:** Cline'ın "her görevde bütün bellek dosyalarını oku" kuralı alınmaz. Gerekçe: bağlam maliyeti ve BMAD'ın aktardığı ölçüm. BMAD'ın ayrımına göre EXP-007'nin işi büyük ölçüde "planlama bağlamı"dır: "consulted in bursts rather than loaded continuously" [BM5]. Karar için kritik kurallar yine de çekirdekte kalır.

**Bellek**
- **Al:** Türlere göre ayrı yüzeyler:
  - STATE: çalışma durumu;
  - PLAN: ilerleme;
  - DECISIONS: ADR biçiminde; alanları durum / bağlam / karar / sonuçlar / yerine koyan;
  - ekleme-yalnız çalışma günlüğü;
  - dersler: tetikleyen olay, kapsam, işlendiği yer, doğrulama;
  - READING-LOG (A003).
- **Al:** Her kayıtta köken ve kapsam etiketi. Köken değerleri: Batu'nun sözü / model çıkarımı / kaynaktan doğrulanmış. Kapsam değerleri: proje / aşama / rol.
- **Al:** Denetim kuralı. Çekirdek dosyalar denetimde küçülür ya da eşit kalır. Kararlar silinmez, yerine konur.
- **Farklı yap:** Otomatik, dil modeli güdümlü bellek çıkarımı ve birleştirmesi kurulmaz (CrewAI, Letta dreaming, Kiro Crew, Vertex Memory Bank tarzı). Gerekçeler: tek yazıcı ilkesi; denetlenebilirlik; R05 §3.3 uyarısı ("They accumulate rules"); Batu'nun "Nereye yazdığın ne yazdığından önemli" ilkesi. Yazma ana oturumda ve commit ile yapılır.
- **Farklı yap:** Vektör arama kurulmaz; Markdown, dizin dosyaları ve `grep` yeterli (Manus ve Claude Code aynı yolu izliyor [MA2]). Korpusun bu yaklaşım için yeterince küçük olduğu bir *varsayım*dır; ölçülmedi.

**Roller**
- **Al:** `.claude/agents/` altında sürümlü rol dosyaları. Cloud'da geçerli; repodan otomatik yüklenir (R01).
  - Alanlar §5'teki işlevsel çekirdek: kimlik, ne zaman kullanılır, sorumluluk, hedef, olumsuz kısıtlar, araç ve yazma kapsamı, model, her zaman yüklenen bağlam, prosedür, çıktı şeması, durma ve yükseltme koşulları, rol belleğinin yeri, değişiklik yetkisi.
- **Farklı yap:** Persona alanları (ad, üslup, geçmiş hikâyesi) kullanılmaz. Gerekçe: BMAD'ın A/B denemesi, Manus ve 12-Factor. Rol sayısı küçük başlar, kanıtla büyür. BMAD Nisan–Ağustos 2026 arasında dört adlı ajanı kaldırdı: üçü Developer'da birleştirildi, teknik yazar ara verdi. Bugün beş adlı ajan var [BM2, BM7].
- **Rol belleği:** `memory: project` alanı `.claude/agent-memory/<ad>/` altına yazar. Cloud'da ancak commit edilirse kalır (R01 açık soru). Bu belirsizlik çözülene kadar rol dersleri, rol kapsamı etiketiyle ortak ders dosyasında tutulabilir. *varsayım*

**Plan ve yaşam döngüsü**
- **Al:** Batu'nun niyeti ve ölçütü → METHOD ya da aşama tasarımı → iş kalemleri. Hata sahibi olan katmana döner. Plan revizyonu ekleme-yalnızdır (R05 #8).
- **Al:** Oturum ya da dalga başına tek iş birimi. Paralel alt ajan yalnız bağımsız, salt-okuma işlerde (Kiro dalgaları; Cognition "intelligence, not writes").
- **Farklı yap:** EARS, dosya yollu `tasks.md`, özellik tabanlı test gibi yazılım SDD artefaktları birebir alınmaz. EXP-007'nin çıktısı tasarım belgesidir. Alınan, katman ayrımı ve "converge" türü uyum denetimidir.

**Doğrulama**
- **Al:** Temiz bağlamlı karşı-okuyucuya yöntem şartları:
  - asgari somut bulgu sayısı;
  - "ne eksik?" sorusu;
  - mercekler: niyet uyumu (Batu'nun sözü birebir verilir), boşluk, tutarlılık;
  - her bulguya hüküm ve kanıt (BMAD triyajı).
- **Al:** Hüküm sözlüğü: doğrulandı / kısmen / başarısız / doğrulanamadı. Doğrulanmamış düzeltme başarı sayılmaz.
- **Farklı yap:** BMAD'ın "üst ajan görev tanımını yeniden anlatamaz" kuralı birebir alınamaz; EXP-007'de alt ajanın tek girdisi görev tanımıdır. Karşılığı: gözden geçirene koordinatörün yorumu değil, Batu'nun birebir sözü ve ölçüt verilir. A003 §3.3 bunu zaten söylüyor.

**Süreklilik**
- **Al:** Her iş kalemi sonunda ilerleme defterinin beş sorusu:
  - istek karşılandı mı;
  - döngüde miyiz;
  - ilerleme var mı;
  - sıradaki kim;
  - talimat ne.
  - Sayaç 3'e ulaşınca yeniden plan yapılır ya da Batu'ya gidilir (Magentic; 12-Factor; BMAD v4).
- **Al:** Her iş kaleminde durum alanı tutulur; yeni oturum bu alandan sürdürür (BMAD `status` makinesi).
- **Farklı yap:** Manus'un `todo.md`'yi her adımda yeniden yazması alınmaz; Manus da bundan vazgeçti. Kalıcı plan iş kalemi sınırında güncellenir. Oturum içi yapılacaklar için Claude Code'un kendi aracı kullanılabilir. *varsayım; R07 doğrulamalı*

**Gözlemlenebilirlik**
- **Al:** Her alt ajan çağrısı için günlükte bir satır:
  - görev tanımının yolu ve commit'i;
  - dönüş durumu;
  - çıktı dosyası;
  - biliniyorsa token harcaması.
- Dayanaklar: BMAD'ın çalıştırma kaydı fikri ve R06.

**Öğrenme**
- **Al:** Aşama sonu retrospektifi:
  - her bulgu kaynağa bağlı;
  - önceki eylem maddelerinin takibi;
  - suçlamasız dil ("hangi girdi eksikti").
- **Al:** Ders kabul testi (gözlenmiş hata şartı), kapsam ve emeklilik kuralı.
- **Al:** Her aşama sonunda sadeleştirme sorusu: "Hangi mekanizma hiçbir kararı değiştirmedi?"

**İnsan**
- **Al:** Batu'ya giden eşikler:
  - geri alınamaz ya da dış etkili eylem;
  - kapsam ya da ölçüt değişikliği;
  - sayaç aşımı.
  - Diğer sorular birikir (A003; K-002).
- **Farklı yap:** BMAD'da her bileti insan kapatır. EXP-007'de Batu aşama sonunda kabul eder (K-002). Batu'nun yükünü azaltmak ve gizli koordinatörlüğü önlemek için.

**Maliyet**
- **Al:** Kararlı çekirdek dosyalar ve ekleme-yalnız günlük (O27). Claude Code'un önbellek davranışı R07'nin alanı.

---

## 9. Açık sorular ve bu notun kanıtlamadıkları

1. **Kanıtın gücü sınırlı.**
   - Kaynakların çoğu tedarikçi belgesi ya da uygulayıcı beyanı.
   - Bağımsız ölçüm yalnız ETH çalışması. Onu da okumadım; BMAD'ın aktarımı ve arama sonucuyla tanıyorum [ME1].
   - Magentic'in kıyas testi sonuçları sistemin bütününe ait; defterlerin ayrı katkısını göstermiyor olabilir. *bilinmiyor*
2. **Alan farkı.** Kanıtların neredeyse tamamı yazılım geliştirmeden geliyor. Tasarım ve araştırma işine aktarımları denenmedi.
3. **Kalıcı rol.** Kalıcı rol dosyasının, iyi yazılmış bir görev tanımına göre sonucu iyileştirdiğine dair ölçüm bulamadım. Bulunan tek ilgili ölçüm, persona çerçevesinin etkisizliği (BMAD). Batu'nun kalıcı rol gereksinimi (K-007) bu yüzden ölçüme değil, tutarlılık, öğrenmenin yeri ve araç sınırı gerekçelerine dayanıyor. *çıkarım*
4. **Erişilemeyen birincil kaynaklar:** Kiro, Cline, Cursor ve Letta belgeleri; OpenAI rehberi; Google whitepaper'ları; Manus blogu; Cognition'ın iki yazısı; Nygard; Scrum Guide; SRE kitabı; ETH ve Vercel ölçümleri. Bunlara dayanan satırlar arama özetine dayanıyor ve yanlış olabilir.
5. **Belirsiz durumlar.**
   - Cursor Memories'in güncel durumu *bilinmiyor*.
   - Letta'nın çekirdek/recall/archival hiyerarşisinin Letta Code'daki bugünkü karşılığı yalnız README düzeyinde görüldü.
6. **Claude Code karşılıkları:** rol belleğinin cloud'da kalıcılığı, hook'lar, önbellek, oturum içi yapılacaklar aracı. Bunları doğrulamadım; R01 ve R07'ye bağlılar.
7. **Tazelik riski.** BMAD 5 ayda persona ve bağlam modelini değiştirdi. Bu not 27.09.2026 durumunu yansıtıyor; yeniden kullanımda sürüm notları tekrar okunmalı.
8. **Kardeş notlarla örtüşme.** R07 ve R09–R11 bu not yazılırken yoktu. Örtüşme ve çelişki denetimi yapılmadı.
9. **Cognition'ın açık sorunları EXP-007'de de açık.** Bu not bunlara mekanizma önermedi:
   - bir alt ajanın bulgusu kardeş işleri nasıl etkiler (koordinatör üzerinden mi);
   - alt ajan ne zaman "yükseltir";
   - bağlam alıcıyı boğmadan nasıl aktarılır.
10. **Önerinin kendisi sınanmadı.** §4'teki 27 maddenin hepsi birlikte kurulursa düzen ağırlaşabilir (O25 riski). Hangilerinin EXP-007'de gerçekten karar değiştireceği, ancak A003'te önerilen pilotlarla görülebilir.
