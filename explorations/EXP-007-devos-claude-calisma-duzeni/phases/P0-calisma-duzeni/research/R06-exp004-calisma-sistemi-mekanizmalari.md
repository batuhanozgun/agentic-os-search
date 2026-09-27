# R06 — EXP-004 (ve EXP-001/002) çalışma sistemi mekanizmalarının EXP-007'ye uygulanması

**Tür:** Alt ajan raporu (model çıktısı). EXP-007 P0 okuması, 27 Eylül 2026. Ajan salt-okuma kısıtıyla çalıştı; hiçbir dosya değiştirmedi.  
**Kullanım sınırı:** Bu metin kaynağın kendisi değil, kaynaktan türetilmiş bir görünümdür. Karar taşıyan her iddiada rapordaki yol/bölüm üzerinden özgün kaynağa dönülür. Rapor İngilizce yazıldı; alıntılar özgün dilindedir. Metin ajanın teslim ettiği haliyle, değiştirilmeden aktarıldı.  
**Soru:** EXP-004'teki (ve kısaca EXP-001/002'deki) uzun iş yürütme mekanizmalarından hangileri EXP-007'nin kendi çalışma düzenini şekillendirmeli; G01–G07 açıklarının hangileri doğrudan ilgili?  
**Ana oturumun kontrolü:** Ana oturum DQ03'teki "SOUL'un kendi iş anlayışını değiştirebilmesi, kullanıcının amacını kendi başına değiştirmesi değildir" alıntısını kaynağında buldu. Diğer alıntılar ana oturumca doğrulanmadı. Rapor, bu mekanizmaların hepsinin denenmemiş kavramsal adaylar olduğunu belirtir.

---

# Report: which EXP-004 mechanisms (plus a few from EXP-001/002) should shape how EXP-007 runs its own work

**Status.** Every item below is a conceptual candidate. They come from explorations that the same assistant built and then reviewed itself; nothing was run. The EXP-004 closure says outright that Batu's positive evaluation is "bütün teknik iddiaların bağımsız doğrulaması … değildir" (STATE §0). Using these ideas to run EXP-007 is itself a transfer to a new setting (DQ04 §3), and the setting is different: Claude Code is the host, subagents start with fresh contexts, and the work is design documents rather than a novel or a question bank. So each row is "denemeye değer aday" (worth trying), not "supported for this use" (DQ01 §6).

**How EXP-004's components map onto EXP-007.** MS01 §7 already sketches a minimal setup that looks like EXP-007: "K1/K2/K4'ün muhakemesi B0'daki farklı görevler; K3 seçim/erişim araçları; K5 üretim/inceleme çağrıları; K6 host kodu; K7 olayla çağrılan uzlaştırma Work'leri". In EXP-007 terms:
- The main session plays B0 and does K1, K2 and K4: interpreting the mission, coordinating work, choosing methods.
- The briefs written for subagents play K3, the context builder.
- The subagents play K5, the domain workbench (reading, drafting, reviewing).
- K6, the control layer, is Claude Code's permissions, git, and Batu's acceptance.
- K7, change and recovery, is reconciliation work opened when something happens (Batu's feedback, a session break).

**Path abbreviations** (all under `/home/user/agentic-os-search/explorations/`):

| Abbreviation | Path |
|---|---|
| MS01 | `EXP-004-…/artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md` |
| SY01 | `EXP-004-…/artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md` |
| COV | `EXP-004-…/artifacts/MS01-COVERAGE-AND-OPEN-MECHANISMS.md` |
| DQ0n, Tnn | `EXP-004-…/continuations/` |
| L | `EXP-004-…/reflections/LEARNINGS.md` |
| RV01 | `EXP-004-…/reflections/RV01-DIRECTION-REVIEW-AND-MECHANISM-TARGET.md` |
| E1 | `EXP-001-soul-calisma-modeli/artifacts/consolidation-v0.1/SOUL_Calisma_Anlayisi_Konsolidasyon_v0_1.md` |
| E1-S016, E1-S017 | `EXP-001-…/sources/conversation/assistant/` |
| E2 | `EXP-002-soul-baz-yapi-ve-entelektuel-taban/artifacts/CONSOLIDATION.md` |
| E2-Q | `EXP-002-…/reflections/QUALIFICATIONS.md` |

## 1. Mechanisms and distinctions

| Mechanism | Where | Quote | Plain meaning | How it applies to EXP-007's own work | Cost |
|---|---|---|---|---|---|
| Start from the authority actually granted | MS01 §2 | "verilmemiş yetki B0 tarafından üretilemez"; "hayalî aktör planlanmaz" | The first piece of work runs on what the owner actually granted. No authority the owner didn't give, and no imagined helpers. | The first work is a draft operating model, done under Batu's opening brief. Plan only with subagents and tools that really exist in the session. | Cheap now |
| A–B–C, and what goes to the owner | E1 §§3.1–3.3 | "bütün bilinmeyenleri kullanıcıya sormak, keşif sorumluluğunu tekrar kullanıcıya yükler" | A is what the owner said, B is the owner's mental model, C is our revisable working understanding. Classify each unknown (look it up, research it, decide it technically, ask the owner, try it) before asking anyone. | Keep Batu's words verbatim and keep C in a separate record. Ask Batu only about goals, preferences and authority. | Cheap now |
| First writable work is a bounded probe | T12 §§4, 8; MS01 P6; E1 §6.1 | "exhaustive planning'den hafif; `write anything` düzeyindeki kontrolsüz başlangıçtan güçlü" | Before starting, state: the question being tested, the constraints to keep, what is accepted vs. open, the mode (probe or final), and where the result returns. Exploratory work isn't blocked just because acceptance is missing. | The first subagent dispatch or pilot declares its mode and its return point. Neither wait for a complete design nor let a first draft quietly become the accepted version. | Cheap now |
| Discovery by reasoning from outcome to use; goal need vs. method need | DQ01 §§2–3 | "Eksik cevabı uydurmak yerine eksik soruyu kurmak, keşfin bir parçasıdır." | Ask how this output gets us to the outcome. Links with no support become questions to investigate. Something the chosen method needs isn't necessarily something the goal needs. Finding a need does not grant new scope. | For each need EXP-007 discovers, record whether it comes from the goal or from a chosen method, and where it came from. | Cheap now |
| Research briefs that say what they feed and where they return | MS01 K1–K2; T11 §7; DQ02 §4 | "hangi kararı beslediği, neyin o kararı değiştireceği, izinli kaynak yolu ve dönüş noktasıyla kurulur" | Each research step names the decision it feeds, which result would change that decision, its bounds, where it returns, and who owns it if it stays open. It also states what it cannot show. | Every subagent brief carries these fields plus a one-line reason for the chosen method. Also plan one small pass that reads the sources "against" our current framing, not just for known keywords. | Cheap now |
| The plan is a living document, not the work | L07; E1-S016 §4; E1-S017 §2; SY01 §8.2 | "planın sırası ile zorunlu bağımlılık aynı şey değil" | The plan is revisable information about the work: its hierarchy, current focus, notes parked for later, and change history. Once accepted, a plan can authorize steps. | Keep one living plan that separates "order we chose" from "hard dependency" and holds current focus and parked notes. Batu's acceptance is what gives it force. | Cheap now |
| Status labels on ideas | T12 §§5–6 | "current/accepted, provisional, rejected/superseded ve intentionally unresolved ayrımı korunmalıdır" | Drafting produces candidates, not decisions. Rejected options must not come back in through summaries. | Tag every design statement with one of these statuses, and keep rejected options on record rather than deleting them. | Cheap now |
| Who may revise the work frame | DQ03 §§3, 5, 11; E2 §9 | "**SOUL'un kendi iş anlayışını değiştirebilmesi, kullanıcının amacını kendi başına değiştirmesi değildir.**" | First locate what the new information actually changed: how the work was carried out, whether the method fits, whether "success" was inferred correctly, our interpretation, or the owner's real goal. Narrowing your own claims needs no approval. Changes to cost, scope or acceptance criteria do. A criterion the owner set can never be quietly redefined. | The main session may correct its own claims and change methods within the discretion it was given. Anything touching Batu's goal, acceptance criteria, scope or cost goes to Batu as a proposal. | Cheap now |
| Keep valid old work, and check that changes actually take effect | DQ03 §§4, 6, 9; MS01 K7; T08 §5 | "Koruma tek global «valid/invalid» bayrağıyla yapılmaz."; "Bir dosyanın yeni metni taşıması, devam eden aktörün onu kullandığını göstermez." | There is no single valid/invalid switch. Keep history and any other support a conclusion still has. Withdrawn conclusions tend to survive inside summaries, and a worker already running may still be using the old version. | Mark things superseded rather than deleting them. Search STATE files and handoff notes for withdrawn claims. Record which version of the brief each subagent ran under, and reconcile late results against that version. | Cheap now |
| How much evidence is enough depends on the next step | T11 §§4–5; DQ01 §6 | "hangi sonraki etkiyi hangi kapsamda kabul etmeye yetecek dayanak var?" | Three levels are different: worth trying, supported for this use, accepted. Repeating the same review adds no confidence. Two complementary reviews can matter together even if neither does alone. | Before any extra reading or review pass, ask which possible result would change which decision. | Cheap now |
| Honest stopping and local closure | T11 §§6, 8 | "«token bütçesi bitti» birer faaliyet/kaynak olayıdır; doğrulama sonucu değildir"; "Beklemede olmak unutulmak veya sessizce silinmek değildir." | Stopped, accepted, parked and closed are different states. A closure records what scope and version it covers, the evidence, what is still uncertain, and what would reopen it. | Running out of context counts as "parked", not "done". Each closed step lists what would reopen it. Starting a new session is not by itself a reason to reopen. | Cheap now |
| Reading every part is not the same as comparing the parts | T14 §§3, 5, 10 | "Okuma izi süreç kanıtıdır; anlama ve gerekçeli hüküm için otomatik oracle değildir." | Five separate claims: the source is available, it was read, related parts were compared, the comparison could tell right from wrong, and the whole is supported. A conclusion can't go beyond what was actually read. | When sources are split across subagents, schedule explicit joint reading for the cross-source claims that carry weight. Report coverage as full, partial, or not read. A summary is fine when it keeps the distinction that matters (T14, case C14-8). | Cheap now |
| Handoffs must carry source locations and status | T08 §2; MS01 K3–K4 | "devir notunu kısaltma, karar-kritik statüyü silme izni değildir; kısa source locator + statüyle taşıma denenebilir" | Summaries drop qualifiers such as "not yet accepted". The list of sources you chose is not the context the worker actually saw. | A subagent's return is always a summary. Require path#section references, quotes, status and reading coverage in every return, and keep the prompt that was sent. | Cheap now |
| Builder–verifier separation | E2 §2; E2-Q Q02–Q03; DQ02 §6 | "üreticinin “neredeyse bitti” anlayışına bağlanmadan doğruluğu sorgulayabilmelidir"; "**Bir yolun kaçırabileceği şu ilgili yanlışı diğer yol neden görebilsin?**" | The verifier has a different aim from the builder. Its verdict can be positive, negative, or limited. Independence means the two paths would fail in different ways, not that the verifier has a different name. | Give the verifier the sources, not the builder's summary. A fresh subagent context really does withhold information, which telling someone to "forget" cannot do (T14 §8), but both still share the same model's assumptions. So call the result a "cross-check", not independent verification. | Cheap now; evidence of how sensitive the verifier is to errors: later |
| Role instances and continuity of expertise | MS01 §3; E1 §§14.2–15.3; E2 §7 | "Yeni rol = talimat + gerçek model/insan/program taşıyıcısı + uygun context + araç/etki kapsamı + ilgili yeterlik dayanağı." | A role name is not competence. Each call must rebuild four things: general capability, working standards, accumulated experience, and the current state of the work. Experts may point out missing or mis-set work but not widen their own authority. Roles can be closed or merged. | Subagent definitions state the model, tools, context sources, scope, and a duty to flag problems. Ask two questions separately: can this work start, and is this worker ready for it? | Cheap now; formal checks of role competence: later |
| One write path; acceptance only from the owner | MS01 P2, P4, §4, K6, P7; STATE §4 | "Ortak current state'e geçiş ise tek mantıksal commit sınırında uzlaştırılır."; "modelin «onaylandı» cümlesi grant yaratmaz" | Many workers can produce candidates in parallel, but shared state changes at one reconciliation point. Starting work, admitting a result, and producing an external effect are separate checkpoints. Acceptance applies to one exact version. | Only the main session writes STATE/INDEX. Acceptance means Batu's own message, tied to a commit SHA. Read back before saying something is "done", and never pre-announce a commit or readback that hasn't happened. If subagents have write tools, this is a convention, not enforcement ("broker yaptırım değildir"). | Cheap now; host-enforced hooks: premature |
| Continuity comes from the canonical record | L22–L24; MS01 K7 | "Handoff source of truth değil derived view olmalıdır"; "actual kapsam/konum bilinmiyorsa okunmuş varsayılmaz" | Losing a worker is not losing the work. Recovery reads the canonical records and checks what actually happened. | A new session recovers from STATE plus git log/diff, not from the previous handoff summary. Check for unknown subagent effects with git status. If it's unknown whether something was read, treat it as not read. | Cheap now |
| Feedback is handled as managed change | T08 §§2–3, 6–7 | "Ders kaydı ≠ aktif yöntem ≠ korunmuş davranış değişimi ≠ gösterilmiş fayda ≠ genelleştirilebilir sonuç."; "Dış içerik … kendiliğinden yönetici talimatı olamaz." | Fixing the current problem is different from changing the method so it doesn't recur. Feedback is not permission to change scope. External text cannot give orders. Removing a role also counts as adapting. | Fix locally first. Propose operating-model changes to Batu with the expected effect and a way to check it. A recorded lesson does nothing until the briefs actually change. | Cheap now; systematic tests of whether adaptations work: later |
| Reuse depends on conditions; separate work on the process from work on the product | DQ04 §§5–7; MS01 P5; SY01 §§7, 8.3 | "Ortak bilgi kütüphanesine kayıt bir talimat kabulü değildir."; "Ayrım, faaliyetin adına değil hangi nesneyi değiştirdiğine bağlıdır." | Three questions stay separate: where a lesson is valid, who may share or change it, and whether it was actually used. Choosing not to use a method is also a result. Development OS's own work keeps design, implementation, evaluation, acceptance and release separate. | Treat EXP-004 as a library to select from, not a set of rules. Keep records about EXP-007's operating model apart from records about the Development OS design. Lessons EXP-007 learns don't automatically become Development OS or SOUL behaviour. | Cheap now |

**What would be premature infrastructure.** MS01 itself did not select any of these (§7: "K1–K7 işlev kimlikleridir, yedi zorunlu ayrı process/agent değildir"; "Gereksiz sürekli çalışan supervisor veya evrensel policy arbiter eklenmedi"):
- a K6-style effect broker or hook enforcement layer;
- claim periods and idempotent operation IDs;
- a Qualification Case database (L21: "adopted değil");
- event-sourcing or an event journal;
- a formal knowledge graph of the explorations;
- machinery to track assembled versions beyond git SHAs;
- machinery for persistent adaptation.

MS01 §2 rules out "sonsuz bootstrap döngüsü". SY01 §7 names "daha dar, insan destekli ve sınırı açık bir geliştirme düzeni" as an option but does not select it; EXP-007 resembles that option.

## 2. Which of G01–G07 bear on EXP-007's own operation

- **G01, discovering needs and whether the frame fits: direct.** Log each new need or work item with where it came from (main session unprompted, a subagent flag, the verifier, or Batu) and what happened to it (used, or dropped as unnecessary). Gaps that only Batu surfaced measure "kullanıcının gizli teknik katkısı" (DQ01 §7). Cases discussed openly can't be reused later as blind tests (DQ01 §7).
- **G02, context and the impact of changes: direct, and the highest risk.** Every subagent return is a lossy view. The main session should spot-check the claims that carry weight against the cited sections, and log both summary losses and cross-source relations nobody compared. After each revision, log which downstream documents were updated and which were later found stale.
- **G03, host boundary and recovery: partial.** Claude Code is the host. Record real session breaks and context compaction, and whether recovery from STATE plus git was correct. Record permission or tool gaps as "unavailable". External effects are mostly git operations, so machinery for unknown effects is unnecessary for now.
- **G04, whether qualification checks are valid: direct.** Compare verifier verdicts with what was later found (Batu's review, later discovery). Where it's cheap, give verifiers both sound and flawed variants, because "Yalnız hata konmuş örnekleri kullanmak, her yerde hata ilan eden sistemi ödüllendirebilir" (DQ02 §8).
- **G05, useful progress and capacity: direct; this is the risk RV01 diagnosed.** Track:
  - turns or sessions until the first reviewable deliverable;
  - research steps opened vs. returned to their decision;
  - the share of work on the process vs. the product;
  - chains of "next narrow question" that never get integrated.
- **G06, combining and transferring methods: direct; EXP-007 is itself a transfer test.** For each EXP-004 mechanism adopted, record:
  - whether it was used;
  - whether it changed a decision;
  - what it cost;
  - any conflicts with other mechanisms (for example, keeping handoffs short vs. keeping status);
  - whether later sessions pick it unprompted or only when reminded, since choosing a method and applying it are different (DQ04 §7).
- **G07, producing and accepting a whole novel: not direct.** The only analogy is a whole-document review of the multi-part operating model against one exact version. Low priority.

## 3. Warnings about how this kind of work goes wrong

1. **Drifting into chains of narrow questions.** "Her tur yeni bir dikkat/kanıt koşulu ve sonraki dar soru üretti"; "alt-soruların bitişi, ana taslağa dönüş ve kapanış teslimatıyla bağlanmadı". Batu's "continue" messages "ilgili turları yetkilendirdi; daha üst amacı ortadan kaldırmadı" (RV01 §3).
2. **Caution turning into deferral.** "Kabul edilmiş mimari/implementasyon üretmemek ile geçici mekanizma ve yapı adayı konuşmamak aynı şey değildir" (RV01 §4).
3. **A "smart coordinator" box that absorbs every hard problem.** "bütün zor yükleri adı konmuş «akıllı koordinatör halleder» kutusuna bırakmak yeterli taslak değildir" (RV01 §7). Relatedly, if the coordinator must discover all needed work up front, "uzmanlığın önemli bölümü zaten koordinatöre yüklenmiş olur" (E1 §15.1).
4. **Endless auditing.** "her değerlendirici için yeni değerlendirici, her açık soru için yeni komite kurarsa hiçbir object work'e dönemeyebilir" (T11 §7).
5. **Discovery and evaluation sharing the same blind spot.** "bütün testler geçerken asıl kullanım başarısız olabilir" (DQ01 §7). And: "Farklı rol, taze çağrı veya farklı isim, aynı varsayım/kaynak/yanılgıların paylaşılmasını dışlamaz" (E2-Q Q03).
6. **Lossy summaries.** In T08 §2, the qualifiers dropped out of a summary and the next worker treated an unaccepted result as current. In T14 §2, a summary with no false sentence still hid who had seen the letter.
7. **Mistaking records for capability.** "Bir `DEPENDENCIES` dosyası … Henüz keşfedilmemiş bağı kendiliğinden bulmuş sayılmaz" (SY01 §6). And: "İş sayısı, dosya sayısı veya taxonomy coverage'ı başarı puanı yapılmaz" (SY01 §10).
8. **Turning the owner into a hidden worker.** "Kullanıcı … gizli işçi veya orkestratör olarak tamamlamak zorunda bırakılmamalıdır" (SY01 §3). A correction supplied by the owner "SOUL'un kendiliğinden keşif başarısı diye sayamayız" (DQ02 §2).
9. **Losing fidelity to the source.** The early EXP-004 archive had been "kısaltılmış, yeniden ifade edilmiş ve yer yer sonradan yorum eklenmişti" (EXP-004 QUALIFICATIONS Q13). Keep Batu's messages verbatim.
10. **Inflating approval.** "Pozitif kullanıcı değerlendirmesi teknik doğrulama … sayılmaz" (Q15).
11. **Both too little and too much structure fail.** Reflexively proposing fewer files and mechanisms "kullanıcının asıl farkındalığını kaçırır" (E1 §12.1). On the other side, "Her yeni ihtiyacı yeni ajan, yeni dosya veya yeni kontrol katmanı kurmaya çevirmek gerekmez" (E1 §16). How much to scale "mesleki bir karar olmalıdır" (E1 §13.4).
12. **Quietly redefining success.** When the success criterion changes, "gerekçesi yalnız kötü sonucu iyi göstermek olmamalı" (DQ03 §7).

## 4. What I actually read

- **Read in full:** MS01-SOUL-WORKING-SYSTEM-DRAFT, SY01, DQ01–DQ04, EXP-004 STATE, T08, T11, T12, T14 (the brief asked only for their main conclusions), MS01-COVERAGE-AND-OPEN-MECHANISMS, LEARNINGS, EXP-004 QUALIFICATIONS and OPEN-QUESTIONS, EXP-002 CONSOLIDATION and QUALIFICATIONS.
- **Read in part:**
  - EXP-001 consolidation: lines 1–186 (§§1–6) and 426–636 (§§12–18). I skipped the demo and file sections (§§7–11) and the appendices.
  - EXP-001 S016 (lines 60–106) and S017 (lines 60–139). I opened these because, as S018 notes, the consolidation doesn't fully cover the living plan.
  - RV01: lines 1–103 (§§1–7).
- **Not read:** T09, T10, T13, T15, SC02; the two MS01 walkthroughs (question bank and novel); MS01-RESEARCH-TO-MECHANISM-MAP; EXP-004's T1–T7 consolidation; the EXP-004 source conversation S001–S015; FRAME-CLARIFICATION, TERMS, EVOLUTION; EXP-003, EXP-005, EXP-006; and the Foundation/studies primary sources those documents cite.

No files were created or modified.
