# R03 — Batu'nun AI ile çalışma ilkeleri

**Tür:** Alt ajan raporu (model çıktısı). EXP-007 P0 okuması, 27 Eylül 2026. Ajan salt-okuma kısıtıyla çalıştı; hiçbir dosya değiştirmedi.  
**Kullanım sınırı:** Bu metin kaynağın kendisi değil, kaynaktan türetilmiş bir görünümdür. Karar taşıyan her iddiada rapordaki yol/bölüm üzerinden özgün kaynağa dönülür. Rapor İngilizce yazıldı; alıntılar özgün dilindedir. Metin ajanın teslim ettiği haliyle, değiştirilmeden aktarıldı.  
**Soru:** Batu'nun yazılarında ve mesajlarında AI ile çalışma, bilgi, bağlam, kayma, süreklilik, yöntem ve doğrulama hakkındaki kendi ilkeleri neler; AI iş arkadaşından ne bekliyor, neyi eleştiriyor?  
**Ana oturumun kontrolü:** Ana oturum şu alıntıları kaynağında birebir buldu: "yanlış cevaba kolayca ulaşamayacağı bir çalışma düzeni kurmak" (A5), "Yapan ile kontrol eden ayrılmalı ve her ikisi de başarı kriterlerini çok net bilmelidir", "emir erine dönüşmüştür", "Durman gereken yerde dur" (A4), "Nereye yazdığın ne yazdığından önemli" (Post 7), "Ben bunu geçen hafta da aynı şekilde anlatmıştım" (skills postu), "izlerin temizlenmesi lazım ki sana drift yaptırmasın" (concepts ORIGIN U03), "neden bu kadar bilgiyi sana ben araştırtmak zorundayım" (EXP-005 U003); concepts ORIGIN U01'deki 10 adımlık pilot-revize sırası. Diğer alıntılar ana oturumca doğrulanmadı. Rapor, bazı yazıların AI ile birlikte yazıldığını (†) ayrıca işaretler.

---

# Batu's principles for working with AI: source-based report

**Who wrote what.** Paths are relative to `/home/user/agentic-os-search/`.
- **Batu's own words:** his chat messages (OR, E4U, E5U, E6U), A1, A5 (he says he wrote it himself because the AI kept softening it, see PA5), the announcement posts and the loop post. A4 carries no note that AI wrote it and reads like him; that is my judgment.
- **† = AI drafted it, Batu published it as his view:** Posts 1–8 ("Özü, yapıyı, sırayı, kararları ben verdim. Cümleleri AI ile birlikte çalıştım.", PI), A2 (written by his Claude "Setup" role) and A3 ("bu yazıyı da AI yazıyor").
- **‡ = an assistant's summary, not his words.**
- The statistics in Posts 1–8 were drafted by AI and I have not checked them. Don't quote them back to him as facts.

**Path legend**
- **Articles** (`publications/linkedin/articles/`): A1 `2026-05-20-calisma-prensipleri-20q5f.md`, A2† `2026-06-20-sahte-secenek-lwr8f.md`, A3† `2026-07-04-yanlis-seyi-iyi-yapar-2z2tf.md`, A4 `2026-07-16-ai-defolari-csvpf.md`, A5 `2026-09-11-llm-dusunmez-zaxzf.md`.
- **Posts** (`publications/linkedin/posts/`): Pn† = `*-post-n-*.md`, PI `7458283954308018176-ai-serisi-giris.md`, PS `7468685461926944769-seriyi-bastan-alalim-skills.md`, PL `7486204143343366144-loop-engineering.md`, PA3 `7479108750402936832-yanlis-seyi-iyi-yapar-makale-duyurusu.md`, PA5 `7504240409825533952-llm-dusunmez-makale-duyurusu.md`.
- **Concepts:** OR `concepts/ORIGIN.md`, CH‡ `concepts/CHARTER.md`.
- **EXP-004** (`explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/`): E4U `sources/conversation/USER-MESSAGES.md`, E4R‡ `reflections/RV01-DIRECTION-REVIEW-AND-MECHANISM-TARGET.md`.
- **EXP-005** (`explorations/EXP-005-ihtiyac-kesfi-ve-calisma-disiplini/`): E5U-NN `sources/conversation/NN-*.md`, E5L‡ `reflections/LESSONS-AND-OPEN-QUESTIONS.md`.
- **EXP-006** (`explorations/EXP-006-development-os-calisma-duzeni/`): E6U1 `sources/U001.md`, E6U2 `sources/U002-cloud-plan-and-autonomy.md`, E6D‡ `DECISIONS.md`.

## 1. Principles
Each principle and its quote are Batu's explicit position. The "→" line is my inference of what it asks of Claude.

1. **LLMs don't think. Only the input can be steered, so build a way of working rather than pleading for better answers.** "müdahale edebildiğimiz tek kısım "Girdi" kısmı"; "Mesele ona doğru cevabı söylemek değil; yanlış cevaba kolayca ulaşamayacağı bir çalışma düzeni kurmak." (A5)
   → Briefs should name the conditions to test, the assumptions the answer rests on ("içinde varsayım var mı", A5) and the outside facts still missing. "Think harder" is not a fix.
2. **In a field you don't know, results are close to zero. Using an LLM only for execution is its worst use.** "Olasılıksal noktaları benim belirlediğim LLM'e sadece eylemi bıraktığım alan LLM'in en değersiz kullanım biçimi." (A5)
   → Claude brings the expertise and leads on "how".
3. **The research exists to fill Claude's context so that Claude says "aslında bu da var" ("there's also this").** (E5U-01 U001); "araştırmalar senin kullanman için yapıldı." His stated order: Foundation WORK/INFORMATION widens the lens, then studies are read "bakış açını genişlettiğin halinle" (E6U2-A).
   → Consult research without being asked, choose the sources yourself, and show what the research changed.
4. **Finding the work and its prerequisites is the AI's job.** "neden bu kadar bilgiyi sana ben araştırtmak zorundayım?" (E5U-02 U003); "bunu ben söyleyip hatırlatınca bir anlamı kalmıyor" (E5U-09 U045); "ilk iş işi yapmaya başlamak değil işi ortaya çıkarmak" (E4U U007)
   → Every reminder he has to give counts as a defect.
5. **Set the mode before acting.** ""Dur" demek geç kalınan bir müdahale" (P1†); "roket gibi daldık konuya ... böyle plansız programsız iş olmaz" (E5U-09 U045); "hemen aksiyon almanı da istemiyorum, ... netleşen ve netleşmeyen kısımları söylemeni ve netleştiği kadarıyla planını paylaşmanı istiyorum" (E6U2-A)
6. **Rough map of the whole first. The plan grows. Pilot, then revise.** "önce bütün harita kabaca belli olmalı ... bir önce konuşma bir sonraki konuşmanın içeriğini belirledi" (E6U2-A); "plan işi yaparken büyüyecek" (E6U1). OR U01 steps 6–9: run the plan on one study with no files written, reconsider it, run a second study, reconsider again.
7. **Arrive at named, concrete structure.** "taslakda olsa bir yapı çıkarabilir, bazı şeylerin adını koyabilir şekilde tamamlanmalı" (his words, quoted in E4R‡)
8. **Define "done", or the AI does the wrong thing well.** "ihtiyacının kriterlerini öyle ver ki AI'a kalanları varsayımla tamamlayacak az şey kalsın" (PA3); "büyük laflar edip küçük işler yapmanı istemiyorum" (E5U-03 U006); "Bu çıktı hangi işi bitirdi?" (A3†)
   → Every work item gets a purpose, a definition of done and a ceiling.
9. **Drift is built into how the model works, and even his own sentences can cause it.** "Her kelimeden drift yapabilir." (A4); "yazdığım her cümlenin yönü belirlerken aynı zamanda kapsamı daraltma potansiyelinin" (E4U U016); "eski kararların, izlerin temizlenmesi lazım ki sana drift yaptırmasın" (OR U03); "her turda hatırlamadıkça drift kaçınılmaz" (OR U04)
10. **Continuity comes from where things are written down, not from the model remembering.** "Kural basit; bir konuşma, bir bağlam." (P5†); "Nereye yazdığın ne yazdığından önemli." (P7†); "Özet değil, karar bağlamı." (P8†); "Kafandaki listeyi AI görmüyor." (P3†); "repoya yansıtmak için geç olmaması da önemli" (E4U U013)
11. **Neither Batu nor the sources are the final authority on truth. No agreeing by reflex.** "ne beni ne de kaynakları doğru kabul etmemelisin" (OR U04); "Her konuşmada "haklısın bunu düşünmemiştim" tarzında bir sonuca varacağımız senaryo yaşatırsın bana." (E5U-01 U002)
    → His approval is not technical validation (CH‡).
12. **The one who makes something is not the one who checks it.** "Yapan ile kontrol eden ayrılmalı ve her ikisi de başarı kriterlerini çok net bilmelidir." An agent running alone for 40 minutes must trigger its own check for flattery (A4).
13. **No fake menus, and no quietly downplaying unfinished work.** "çoğu zaman elinde gerçek bir iş kalmamıştır. Fakat "bitti" diyebileceği net bir kriter de yoktur". For research work: "Alternatifleri göstermekten çekinme; fakat belirsizlik anlarında sahte seçenekler üretme. Belirsizlik varsa açıkça söyle. ... Durman gereken yerde dur." (A4)
14. **Give the route, the goal and the criteria, or you get an order-taker.** "rotayı, hedefi ve kriterleri vermeden yalnızca görevleri sırayla dağıtırsanız ... Artık emir erine dönüşmüştür." (A4)
    → This also applies to Claude briefing its own subagents.
15. **The team runs itself, but the human keeps authority.** "Bu işler süreci elle yürütmeme neden olmamalı" (E6U2-B); "sonsuza kadar benden bağımsız çalışsınlar demek istemiyorum ... ama ... her adımda benim "şimdi sıra sende" demem değil" (E6U2-C); "benden bir cevap bekleme, hata yapma ve iş bitene kadar da durma" (E5U-03 U006)
16. **Short answers. Don't hand him your thinking out loud.** "kendi kendine fikir jimnastiği yaptığın bir metni bana dayatıyorsun ... laf ebeliği yapıyorsun"; "kalıcı şekilde davranış haline getir" (E6U2-A)
17. **Know what the environment can really do before designing for it.** "Onun gerçekliğini bilmeden tasarım yapamayız."; "Anthropic'ten araştır bunu" (E6U2); "erişemiyorsa neden çalışmaya başlattın ki?" (E5U-05 U021)
18. **Skills, loops and hooks are tools with limits.**
    - A skill is worth making when you think "Ben bunu geçen hafta da aynı şekilde anlatmıştım." (PS)
    - Loops fit only work whose "bitti tanımı" (definition of done) is clear; "loop engineering metodolojisi AI'yı küçümsüyor" (PL).
    - Hooks can't say "Böyle düşünme", and "Hepsine kurmak da imkânsız." (A4)

## 2. His recurring criticisms of AI behaviour (all explicit)
- **Acts before being asked:** P1† (the story of the game for his daughter); U045 "roket gibi".
- **Shallow, narrow output:** "Hep bir sığ, dar bakış açısı ile bir çıktı üretiyorsun" (E5U-01 U002).
- **Looks like work without being work:** "Sahte ilerleme artık çok ucuz" (A3†).
- **Bloat:** "Tuğla gibi cevap vermenin iyi bir şey olduğunu sanır" (A4). In agent systems, bloat pollutes other agents' context (A4).
- **Mirroring his words back as if understood:** "Biz de bunu "anladı" sanıyoruz." (A4)
- **Making things up instead of saying "bilmiyorum" (I don't know), and freezing:** "cevabı öteler" (A4).
- **Wavering between recommendations:** "bir o yana bir bu yana kayıyor tercihlerin" (E5U-06 U030).
- **Side detours:** "bunu da halledelim 2 sn'lik iş" (P3†).
- **Promises instead of mechanisms:** ""Daha dikkatli olacağım" der" (A3†).
- **Starting without access, or choosing sources too narrowly:** "niye sadece EXP-004'e gönderiyorsun?" (E5U-05 U023).
- **Softening LLM limits for commercial reasons:** "ticari kaygılardan dolayı LLM'i kötü göstermemek için" (PA5).
- **Hype that shows results but not the process:** "Bize süreci göstermiyorlar ama sonuçlarını paylaşıyorlar" (A1).

## 3. What he expects from the process
- **Planning:** first a playback of what Claude understood, split into clear and unclear, then a plan. Rough whole map, pilots, and revisions with reasons (principles 5–7).
- **Communication:** short and plain. At any moment "ne yapıyoruz şu anda?" (E5U-05 U011, "what are we doing right now?") should have an obvious answer. No menus (principles 13 and 16).
- **Research:** Claude starts it, and reads fully. "Başlık, özet, anahtar sözcük araması ... tam okuma yerine geçmez" (CH‡). Widen the perspective before looking at examples. Anthropic's own docs for the environment (principles 3 and 17).
- **Autonomy:** don't wait for his technical answers. Stop when the work is done or truly blocked. He steps in for authority and acceptance (principle 15; E6D‡ D003: "yetki + kabul").
- **Verification:** independent, based on evidence, and tied to the criteria. Reviews should try to refute the work, as in A2†'s "4 ayrı bağımsız AI merceği". Match the amount of checking to the case; A2† rejected a heavy check that would have become "boş bir tören".
- **Continuity:** the repo is the memory. Decisions are recorded with their reasons. New sessions continue from the same perspective (OR U05).

## 4. Tensions between his principles
1. **Short answers vs rigor.** He wants short replies (E6U2-A). He also wants Claude aware of what it read and how its reading changed: "ne okudun, daha önce ne okumuştun ... şimdi ne düşünüyorsun" (OR U04). The records resolve it this way: chat stays short, and a checkable trail goes in the repo. "Ham düşünce dökümü değil, denetlenebilir sonuç ve gerekçe özeti" (CH‡, D010‡). Rigor is not volume (A3†).
2. **Autonomy vs approval.**
   - He says "benden bir cevap bekleme" (U006).
   - He also says "onaylarsam devam edeceksin" (OR U01), and P1† says "adım atmadan önce her zaman benden onay al".
   - The resolution: gates sit at understanding, plan and acceptance, never on each step (E6U2-C). E5L‡ adds "yetkilendirme ile hazır olma ayrı" (being authorised is not the same as being ready).
   - He has not said when a revised plan needs his approval again. My guess: changes to purpose, scope or authority do; changes of method don't.
3. **Heavy research vs name-dropping.** He built the research corpus for Claude's use. But he mocks listicles (PA3) and refuses a "5 skill" list (A5). A3†'s first draft drew on a 26,000-word research summary yet "fikri ileri taşımıyordu". Research earns its place only when it changes a decision or reveals a need. Sources prove how they themselves use a term, not universal truth (CH‡).
4. **"Give detail" vs "your words narrow the scope".** He handles this by labelling his own status. "hayal ettiğim için yazdım" (E4U U001) and "kesin olarak savunmuyorum" (U010) mark imagining and not firmly claiming. "bilmediğim için öyle yazdım" (E6U2-B) marks not knowing. Claude must respect these labels and not turn examples into scope (D018‡).
5. **"Don't ask me" vs "no menus" vs "bring me real decisions".** A2†: "kanıt/bulgu/gerçek açık-iş = her zaman serbest", meaning findings and real open work may always be raised. A real decision comes with a recommendation. When to stop is set by the definition of done ("Durman gereken yerde dur"), not by his attention.
6. **"LLMs don't think" vs "work out yourself what I don't know" (U003).** His own answer: discovery comes from the way of working, which must give roles "doğru bilgiyi, doğru zamanda, doğru kelimelerle" (E6U2-A). It cannot rest on the model thinking better.
7. **He wants a team that runs itself like loopinance_v2, yet criticises loop engineering.** Loops belong only inside tightly bounded work (PL). He did not ask for loopinance_v2's whole setup, or ECC, to be adopted (D018‡).
8. **He is not an expert, yet he is the only one who accepts the work.** Checkers built on the same model share its blind spots: "Tüm roller aynı temel modeli ... paylaştığı için, defekt hepsinde aynı kökten çıkıyor" (A2†). This is unresolved. The partial answer is adversarial independent review plus a visible record of how things were interpreted.

## 5. Implications for EXP-007 (my inference)
The first test comes from E5L‡: the problem of discovery depending on him "onu düzeltmek için yürütülen süreçte yeniden ortaya çıktı" (came back inside the process meant to fix it). EXP-007 must not repeat that.

1. **Opening message.** Keep it to about 10 lines: what I understood, what's unclear, my assumptions, where his wording may narrow the scope, and a rough master map. Write nothing to the repo until he confirms the direction. The playback must interpret, not just rephrase him.
2. **Log his inputs.** Tag each as purpose, constraint, decision, example, association or open question. Retire old directions explicitly.
3. **Every work item** has a purpose (which decision it feeds), a definition of done, what's out of scope, and how uncertain it is. If "done" can't be known yet, say it's research mode, using his wording (principle 13).
4. **Subagent briefs** say where the work sits on the map and why it matters. They list the chosen sources with reasons, the conditions to test, the assumptions to flag and what not to do. Returns are short: result, evidence, key assumptions, open items. Each return becomes the next agent's input.
5. **When to consult research:**
   - a choice needs expertise Batu lacks;
   - any claim about Claude Code cloud (check Anthropic's docs and test it in the live environment);
   - before fixing any role or mechanism in place.
   Read Foundation WORK/INFORMATION first, then studies. Each research return states what it changed, or "nothing".
6. **Check before long runs.** Confirm access, sources, tools and handoff state in the real environment. Log every reminder Batu has to give.
7. **A separate reviewer checks each item.** It uses the same definition of done and is briefed to refute. Evidence means readback, diffs or run output. Match the review effort to the item.
8. **End each turn in one of three forms only:** "şunu yapıyorum" (I'm doing this), "şunu bekliyorum, senin karar vereceğin bir şey yok" (I'm waiting on this; nothing for you to decide), or a real fork with my recommendation. Never downplay open work.
9. **Chat:** the result, any uncertainty that affects a decision, and the next point on the map, in plain Turkish. Detail lives in the repo. Never say "artık net" (it's clear now) without having verified it.
10. **Plan:**
    - The master map lives in the repo.
    - Each turn shows where we are: "A açık, B'deyiz, C sonra" (A is open, we're on B, C comes later).
    - New work is added with a reason; revisions record why and what was rejected.
    - Pilot on one real work item, revise, run a second pilot, then scale up.
11. **Continuity:** close each work item with what was done, the decisions and why, the rejected options and the next starting point. Write it back before the context fills up.
12. **Pushback and autonomy:**
    - When he objects, re-examine and state plainly whether and why my position changes.
    - Within the approved map, go ahead without routine approvals.
    - Long runs check themselves for flattery and drift.
    - Use hooks only at known points where drift starts.

## 6. What I read
- **Read in full:** all 5 articles; all 18 posts; CHARTER.md; ORIGIN.md (in full, not skimmed); E5L in full; EXP-004 FRAME-CLARIFICATION-20260921.md and RV01; EXP-006 U001 and U002.
- **Also read, to get his exact words:** E4U in full; EXP-006 DECISIONS.md; in the EXP-005 conversation files 01–10, Batu's turns only (U001–U048). I did not read the assistant's turns.
- **Not read:** AGENT.md, README.md, `agent/` protocols, the other `concepts/` files, the rest of EXP-006 (WORK, ACTORS, STATE, HANDOFF, EXP-006_Context, history, work), EXP-001–003, `research/`, `development-os/`, the post images and the surreal-ai app.
