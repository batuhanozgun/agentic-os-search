# R02 — EXP-006: nasıl çalıştı, nerede kaydı, ne devralınmalı

**Tür:** Alt ajan raporu (model çıktısı). EXP-007 P0 okuması, 27 Eylül 2026. Ajan salt-okuma kısıtıyla çalıştı; hiçbir dosya değiştirmedi.  
**Kullanım sınırı:** Bu metin kaynağın kendisi değil, kaynaktan türetilmiş bir görünümdür. Karar taşıyan her iddiada rapordaki yol/bölüm üzerinden özgün kaynağa dönülür. Rapor İngilizce yazıldı; alıntılar özgün dilindedir. Metin ajanın teslim ettiği haliyle, değiştirilmeden aktarıldı.  
**Soru:** EXP-006'nın düşünme ve değerlendirme yaklaşımları nasıl işledi, iş nasıl evrildi, nerede ve neden kaydı; EXP-007'ye ne taşınmalı, hangi ChatGPT dönemi alışkanlıkları kaymaya yol açar?  
**Ana oturumun kontrolü:** Ana oturum kaynağından kontrol etti: EXP-006 toplam kelime sayısı (53.346) ve `sources/` kelime sayısı (1.494); U001 "4 bacak" ve U002-A "bir önce konuşma bir sonraki konuşmanın içeriğini belirledi" alıntıları; ACTORS.md'deki B3–B6 için tekrarlanan Designer/Steward/Reviewer kalıbı. Diğer iddialar ana oturumca doğrulanmadı.

---

# EXP-006: how it worked, where it drifted, what to carry into EXP-007

Root: `/home/user/agentic-os-search/explorations/EXP-006-development-os-calisma-duzeni/` (all paths below are relative to it). **[F]** means the files say it. **[I]** means it is my inference.

**Git caveat:** the clone is shallow. It has 50 commits, 49 of which touch EXP-006. The oldest visible commit, `23280ab` (26 Sep 13:24), is the graft root, so none of 25 Sep shows in git: U001, actors, RPD, B1–B9 and S1-01–S1-03. I rebuilt that part from `history/` and the dated slices.

**Scale:** between 25 Sep and 27 Sep 00:39 the package grew to about 53k words. Only about 1.5k words of the user's own text are kept verbatim (U001, U002). Every other user correction survives only as the assistant's paraphrase ("anlam özeti; kelimesi kelimesine aktarım değildir", S1-02 §1).

## 1. Evolution timeline

1. **Opening** (25 Sep, U001): the user gave five practical needs, then asked "Önce aktörleri konuşalım mı? Development OS'un içinde kaç aktör olacak onu bulalım."
2. **Actors.** Two actors: human and AI (D002). The human's customer role was narrowed from "amaç, tercih, kapsam, karar ve kabul" down to "yetki ve kabul" (Context; D003).
3. **→ Work discovery.** Trigger was the user: "yapay zekâ rollerini jenerik adlarla çıkarmak yerine önce Development OS'un yaptığı işi tanımlamayı istedi" (`history/2026-09-25-pre-work-system-STATE.md`). RPD was adopted and gave six root works.
4. **→ Making the SOUL target concrete.** Trigger: "“SOUL'u yarat” ifadesi çalışma için hâlâ fazla geniştir" (Context). The user picked five full reads from EXP-001/002/004. The resulting target was accepted as "yeterince somut" (D006).
5. **→ B1–B9.** Here DevOS's work meant developing SOUL's capacities. The branches were opened one by one and produced R1–R25 and M1–M9 (`history/…pre-split-WORK-MAP.md`, `work/B*.md`). The monolith was then split into a living work system (D009).
6. **→ S1 consolidation.** Trigger was the user: not just "rol adlarını gruplamak" but use research examples (S1 master §1).
   - S1-01: produce/review/correct separation; G1 found that no role owned realization.
   - S1-02: the user objected about actor conditions and conflicting motivations. G1 "anlaşılmamıştır" by the user.
   - S1-03: the user asked for another round using OS Architect.
   - S1-04: the user said "ana yönün net olduğunu … devam".
   - S1-05–S1-13: the assistant chose the order itself, one family at a time.
   - The user then ordered a cleanup: "EXP-006 yapısını drift açısından denetle; fazla/eski/çelişkili yüzeyleri temizle" (STATE@59b6499). That produced 36 commits in about 6 minutes, mostly one file each.
   - S1-14 audit → S1-15 (F8) → S1-16 → S1-17 "CLOSURE-READY".
7. **→ Correction** (fea5d50). S1-17 proposed "somut bir DevOS geliştirme işi üzerinde etkin görevlendirme". The user objected to "“ilk somut SOUL geliştirme işini assistant seçsin”", which became D012.
8. **→ U002** (27 Sep). The user said:
   - "haddinden fazla uzun cevap … laf ebeliği yapıyorsun"
   - "Şu ana kadar yönümüz belli olmadan ilerledik, bir önce konuşma bir sonraki konuşmanın içeriğini belirledi"
   - "Burada henüz rolleri ortaya koymadık"
   - the target is Claude Code cloud; the assistant should research subagents vs agent teams
   - "motivasyonları birer agent gibi düşünüyorum"
   - K1 (communication) and K2 ("ekip kendi kendine işi yürütebilmeli")
   - autonomy is bounded, and the plan must be saved to the repo first.

   The result is the P1–P6 plan in `WORK.md`, marked "P1 NEXT / NOT STARTED".

## 2. Thinking approaches actually used

- **Ordering rule:** "Önce ihtiyaç ve iş; sonra sorumluluk ve rol; en son mekanizma ve araç" (Context; D004/D005/D008). The user later relaxed it; D005 now reads "D011'in belirlediği Environment önce tanınır".
- **RPD root question:** "SOUL'u yaratma hedefinin gerçekleşmesi için önce ne doğru olmak zorunda?" Plus a habit of reducing ideas to minimal distinctions, such as yetki+kabul.
- **Per-B derivation:** Work → capabilities (C) → carriers. A carrier is an AI role (R), a mechanism (M) or the human boundary (D008).
  - [I] Each B area got an almost identical Designer/Steward/Reviewer trio: B3 R7–R9, B4 R10–R12, B5 R13–R15, B6 R16–R18.
  - S1-05 then "found" families F1/F3/F5 in that very pattern ("Bu tekrar deseni özellikle B3–B6'da güçlüdür"). So the consolidation partly rediscovered its own derivation template.
- **Layers kept apart:** actor ≠ family ≠ specialization ≠ effective assignment. Working formula: "family × specialization × exact assignment object × actor operating profile" (ACTORS; S1-14 §7).
- **Success direction** (the assistant's rename of the user's "motivasyon"):
  - "başarı yönü açık ve kendi içinde tutarlı olmalı" (S1-02 §3)
  - an incentive check: "hangi sonuçla ödüllendirilmemesi gerektiği" (S1-03 A1)
  - triggers, handoff and consumer treated as part of a role (S1-03 A3).
- **Reading sources in their own context:** each source gets "Gösterdiği / Göstermediği" (S1-01 §2).
- **Development chain:** requirement→design→realization→integration→test→diagnosis (S1-04 §3). It comes with a version-evidence chain: "hangi gereksinim ve sürüm → hangi değişiklik → hangi test veya gözlem → … → hangi yeni sürüm ve yeniden sınama" (S1-01 A4).
- **Control type per expectation:** instruction vs evaluation vs mechanical enforcement (B1-C4). Failures are diagnosed by layer (B1-C6, B4-C11).
- **Level separation:** DevOS building SOUL vs SOUL's future operation vs EXP-006's own records (S1 master §3; S1-17 §3.2).
- **Rival models:** S1-14 §10; S1-15 §3, including "Güçlü karşı seçenek: F5'i genişletmek". Coverage/overlap audits in S1-14 and S1-17 §3.

## 3. Evaluation approaches and how reliable they were

**Labels used:**
- B files: "EXPLORED / candidate decomposition"
- slices: "aday"
- S1-17: "S1-CLOSURE-READY / CANDIDATE / USER-EVALUATION-PENDING"
- DECISIONS: statuses such as "accepted method" and "accepted stage gate"
- plan: "NEXT / NOT STARTED"

**Instruments:**
- counterexamples reasoned on paper (S1-01 §5; S1-17 §4.2)
- falsification tests written down but never run (S1-04 §6, "henüz koşulmadı")
- 100 named C responsibilities routed into 62 groups (S1-17 §3.2)
- a Python record-integrity check with deliberate faults: "B3-C7 bilerek kaldırıldığında missing; B2-C3 tekrarlandığında duplicate saptandı" (§6)
- reading ledgers pinned to git blob hashes.

**Reliability:**
- **One producer judged everything, and says so:** "Aynı assistant'ın kaynak bağlı nitel ikinci incelemesi … Bağımsız doğrulama … değildir" (S1-17 header). The C inventory it checked against is also self-made: "bağımsız bir semantic oracle değildir" (§6).
- **[I] Leaning toward confirmation.** S1-07–S1-13 each kept its family ("… ailesi olarak ayakta kalıyor", S1-08, S1-10). None was rejected; several were only renamed (F2, F6).
  - Those nine slices have zero reading-trace or blob entries. Their "Araştırma karşı-kontrolü" sections are one-paragraph summaries.
  - S1-15 §6 admits that S1-14's reuse of the studies was "metadata düzeyindeki".
- **Full-read claims were unreliable.** S1-16 §8 labelled five sources "Tam" although the bulk tool output had been cut off. S1-17 §7 withdrew that: "`Tam` etiketleri … model-visible tam okuma kanıtı kabul edilemez".
  - S1-17 itself still relies on "aynı konuşmadaki önceki tam içerikleri" for B1–B9 and S1-01–S1-13. [I] That is weak evidence in a long chat.
- **No live test was ever run.**
- **Counter-evidence (where the method worked):**
  - scoping was honest, and it corrected its own ledger
  - alternatives stayed open ("sekiz sayısına ayrıcalık tanınmaz", S1-17 §4.2)
  - S1-14 reopened the research question instead of forcing closure
  - S1 found a real gap: no R role owned realization, which became F2.
  - U002 does not reject S1's content. The complaint is about invisible direction and answer length.

## 4. Drift and stalls

**Episodes:**
- **E1 – each step chosen by the last turn.** Every slice from S1-05 on ends with a next step the assistant chose itself ("Sıradaki aile **F1**…", S1-07 §10). The chain ran F2 → F3 → F4 → F6 → F7 → audit → F8 test → specializations → closure → "somut … görevlendirme", which the user rejected. The user named this pattern exactly in U002-A.
- **E2 – abstraction that never landed.** 17 slices turned R1–R25 into F1–F8 plus specializations. No role was named and the platform was never researched. [I] EXP-006's own B7-C10 warned against this: "formation Work'ünü asıl teslimatı sürekli erteleyen meta-work'e çevirmeme".
- **E3 – a written rule failed.** D010 and the Context "iletişim disiplini" section already existed at `23280ab` (26 Sep), yet U002-A on 27 Sep still complains about length. [I] This is EXP-006's own B1-C4 lesson: a principle does not hold just by saying it ("yalnız “aktöre söylemekle”").
- **E4 – the environment was deferred.** The pre-work STATE says "“Sen ya da Claude Code” ifadesi … zorunlu kılan karar değildir" and the runtime was "henüz seçilmedi", until the user fixed it (D011).
- **E5 – level slip.** The assistant offered to pick SOUL's first job (fea5d50).

**Causes, by type:**
- **(a) Platform limits.**
  - The ChatGPT GitHub tool output was cut off again and again: "ilk yanıt kesildi" (S1-01 §6), S1-02 §8, "1–170 isteği kesildi" (S1-04 §8), S1-15 §6, and S1-16 as corrected in S1-17 §7.
  - Files were written one at a time (36 commits in 6 minutes).
  - Each user turn produced one slice.
  - "Full read" claims rested on chat memory.
- **(b) Method and structure.**
  - "Mechanism last" kept platform reality out of scope.
  - The Designer/Steward/Reviewer template produced a taxonomy that invited classification about classification.
  - [I] Roles were derived from SOUL's target capacities (B1–B9), not from the DevOS team's own working loop. The user wanted that loop from the start: "foundation'daki 4 bacak her anında geçerli olacak bu development os SOUL'u yaratırken" (U001). U002-A item 4 lists memory updates, deciding the next job and recording cause and effect. That loop appears only now, as P3.
- **(c) Rules written into the repo.**
  - AGENT.md requires "every user turn … pass through the complete routing gate", allows "`SKIP` … only when the route can be rejected confidently", and puts a status block at the top of every answer.
  - About 1,900 lines of protocols sit behind it.
  - The R07 continuity protocol makes each result get rewritten across 5–7 files; a8e7a92, fb8a49d and 02b9180 each touch 7 files.
  - The authorization discipline produced "Bu tur yapılmayanlar" lists and stop points.
  - The drift cleanup left "Authority notu" boilerplate in 27 files.
- **(d) The user had to steer.** There were nine or more corrections (§1). [I] The user ended up carrying direction-setting, the "kullanıcının üstlendiği gizli koordinasyon yükü" that EXP-005 had warned about (`history/…pre-work-system-INDEX.md`).

## 5. What is worth carrying into EXP-007

Suggested handling: EXP-006 stays read-only. EXP-007 cites it by path and ID.

**Accepted decisions (primary sources):**
- `sources/U001.md` and `sources/U002-cloud-plan-and-autonomy.md`, which are verbatim. Use these, not the paraphrases.
- DECISIONS D002–D004 and D010–D018:
  - Claude Code cloud is the target
  - the team discovers SOUL's work itself
  - K1: "talep→etkin çalışma→geri dönen/kullanılan sonuç" (S1 master §7)
  - K2: no routine manual triggering, with bounded autonomy
  - SOUL outputs and DevOS records are kept separate
  - Foundation and studies serve as a lens
  - the whole map comes first
  - the loopinance examples have bounded relevance.
- The U002-A principle that good output needs "doğru bilgiyi, doğru zamanda, doğru kelimelerle".

**Candidate models (hypotheses to test in P2/P3, not truths):**
- `ACTORS.md`: the F1–F8 success directions and the assignment formula
- S1-17 §2 boundaries: writing a file does not make something F2 work; keeping a record does not create truth or authority
- S1-01 A1–A4: a producer's own test is not an independent review; whoever fixes something becomes its producer; finding, diagnosis, decision and fix are separate
- S1-03 A1–A4: incentives, triggers, and transfer from developer to the role it builds
- S1-04: the development chain, the realization task card, and the falsification tests
- the user's actor→family→role→motivation hierarchy, still open in DECISIONS.

**Reference lenses:**
- B-file distinctions as checklists:
  - B2: stored ≠ discoverable ≠ selected ≠ shown to the actor ≠ used; canonical memory vs derived memory
  - B4: candidate ≠ admitted ≠ active; plan ≠ actual; done ≠ verified ≠ accepted
  - B8: re-entry
  - B9: falsifiable claims and test leakage (B9-C4)
  - B7-C10: guard against endless meta-work.
- M1–M9 as a checklist to map against Claude Code features.
- The S1-17 §5 table of what remains open.
- The P1 research axes in WORK §4 and the Foundation/studies routes in WORK §5.

**Do not carry as instructions:** any "next" statement or stop point; R1–R25 as an org chart; or P1–P6 as a fixed sequence rather than a candidate plan.

## 6. ChatGPT-era habits that would mislead EXP-007

1. **Routing ritual.** "At the start of every new ChatGPT project conversation, this file must be fetched fresh", plus a status block on every answer (AGENT.md).
2. **The same state repeated across files.**
   - "NOT STARTED" appears in INDEX, STATE, HANDOFF, DECISIONS and the S1 master, and 7 times in WORK.
   - The S1-17 §7 caveat is repeated in STATE, HANDOFF, WORK, ACTORS and the S1 master.
   - D010 lives in DECISIONS, Context, HANDOFF §6 and `agent/protocols/canonical-work-preflight.md`.
   - The reading orders disagree. Context says "INDEX → STATE → HANDOFF → WORK → ACTORS → active phase master/slice"; `history/README` says "STATE → HANDOFF → WORK → ACTORS"; STATE and INDEX add DECISIONS and U002.
3. **Historical "next" lines** remain in 27 files, neutralized only by a header note.
4. **Stop points that re-create manual triggering:** "Plan hazırlığında dur. P1'i aynı tur içinde otomatik başlatma." (STATE).
5. **Over-qualification.** Lines like "Sekiz familyanın zorunlu/optimal olduğu veya gerçek sistemde çalıştığı kanıtlanmadı" (ACTORS) and "Buradaki gereksinimler gösterilmiş platform kabiliyeti değildir" (STATE) are right once and noise when attached to every claim.
6. **Jargon and vocabulary drift.** The user's "motivasyon" became "başarı yönü/success direction". Mixed-language terms pile up: "exact assignment object", "Actor / Role Participation Lifecycle Operations", "composite standing".
7. **File proliferation.** One file per turn (17 S1 slices plus a master, 9 B files, 3 history snapshots). The blob ledgers existed mainly to compensate for truncated tool output.
8. **Closure labels issued by the producer itself**, plus "aynı assistant" disclaimers, instead of an actual independent reviewer. In Claude Code, spawn one.

## 7. Reading coverage

- **Read fully:** U001, U002, EXP-006_Context, all of `history/`, STATE, HANDOFF, WORK, DECISIONS, INDEX, ACTORS, the S1 master, S1-01, S1-02, S1-04, S1-14, S1-17, B1, B4.
- **Read in part:**
  - S1-03 (§1–6), S1-05 (§3–6), S1-15 (§1, §3, §6–7), S1-16 (§1–2, §8–9)
  - AGENT.md lines 1–80
  - the EXP-006 section of `canonical-work-preflight`
  - the opening of `work-system-continuity`.
- **Skimmed** (headers, headings, closing sections, counter-checks): S1-06–S1-13; B2, B3 and B5–B9, plus B7-C10 and B9-C4 in full.
- **Git:** the log; diffs of c94195d, 8a40349, and STATE/HANDOFF at 59b6499 and fea5d50; D010 as of `23280ab`.
- **Not read:** the other agent protocols, EXP-001–005, Foundation, studies, and the external repos (Keel, OS Architect, loopinance).
