# R05 — Studies'teki çalışma mekanizmaları

**Tür:** Alt ajan raporu (model çıktısı). EXP-007 P0 okuması, 27 Eylül 2026. Ajan salt-okuma kısıtıyla çalıştı; hiçbir dosya değiştirmedi.  
**Kullanım sınırı:** Bu metin kaynağın kendisi değil, kaynaktan türetilmiş bir görünümdür. Karar taşıyan her iddiada rapordaki yol/bölüm üzerinden özgün kaynağa dönülür. Rapor İngilizce yazıldı; alıntılar özgün dilindedir. Metin ajanın teslim ettiği haliyle, değiştirilmeden aktarıldı.  
**Soru:** Aday çalışmalar; alt ajan görev tanımı, yaşayan plan, plan revizyonu, tamamlanmadan önce doğrulama, oturumlar arası devir, öğrenme, insan kapıları ve ilerlemesiz hareketin tespiti için hangi kaynak-dayanaklı mekanizmaları gösteriyor?  
**Ana oturumun kontrolü:** Ana oturum bu raporun alıntılarını ayrıca doğrulamadı. Rapordaki çalışmaların hepsi aday girdidir; benimsenmiş mimari değildir (R09).

---

## Study mechanisms for running EXP-007: briefing, planning, verification, handoff, learning, human gates and stall detection

Base path: `/home/user/agentic-os-search/research/studies/`. Every item below is a candidate input to consider, not an adopted design.

**Package abbreviations:** SP superpowers, GS gstack, WM work-management-project-control, RPD recursive-prerequisite-discovery, MAP multi-agent-patterns, CMH context-memory-harness-engineering, PB anthropic-ai-native-sdlc-playbook, OS openspec, SK spec-kit, BD beads, HA hermes-agent, GT gastown.

**Evidence codes:**
- **S**: the study read the pinned source only.
- **S+T**: source plus first-party tests or CI, which the study inspected but did not run.
- **P**: the study ran local synthetic probes.
- **C**: conceptual or conversation assessment.
- **L**: vendor documents or literature.
- **UA**: the owner evaluated and accepted the study. Only SP has this, and it says acceptance "does not upgrade evidence strength".
- WM is review-ready and still awaiting user evaluation. CMH also awaits user evaluation. HA is active and partial, with provisional syntheses.

**No study measured how well any of these mechanisms work with live agents.** Several syntheses were written by the same assistant from overlapping inputs, so they do not corroborate each other independently.

### 1. Mechanism table

| # | Mechanism | Source | What it does (quote) | Evid. | Use in EXP-007's own operation | Risk / counterexample |
|---|---|---|---|---|---|---|
| **(1) Briefing and context scoping** |
| 1 | Coordinator writes each brief | SP syntheses/S03 §3; S06 §4 | Brief contains the task, binding global constraints, interfaces, earlier rulings and where to put the report. "Workers are explicitly not given the whole plan/history." The coordinator must not "predetermine reviewer severity". | S+P, UA | The main session writes every brief; a subagent sees only its brief and the repo | "A worker and reviewer can share the same omission when they share an incomplete brief" |
| 2 | Fixed return format; result treated as data; child authority reduced | GS syntheses/multi-agent-cross-model-coordination §2.3–2.4 | The child's last line is JSON (files_updated, commit_sha, decisions, or error) and the parent checks its types. The returned content is handled "as untrusted markdown data". Effects the parent owns are excluded from the child's scope. | S+T | Use one return schema for all subagents | SP CLOSURE-AUDIT §3 (issue #2202): a worker "returned a promise instead of a report" |
| 3 | Rules for a child that cannot ask the user | same §2.2 | No questions to the user; take the recommended option; take the conservative option if destructive; "record each auto-choice for parent visibility" | S+T; the trust chain is "partly prose" | Subagents cannot reach Batu, so they list their assumptions for the coordinator to ratify | Value choices made silently |
| 4 | Status codes; a retry must change something | SP notes/U03; S04 §3 | DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT. Blocked work gets more context, a stronger model, a split, or a plan fix; the rule "forbids unchanged retries" | S, UA | Never send the same brief twice | DONE only starts review; it is not acceptance |
| **(2) Living plan, ready work and newly found work** |
| 5 | Editable task list; a new intent is a new change | OS FINDINGS §6–8 | Tasks are "added when new work is discovered", removed or reordered. A fundamentally different intent becomes a new change. | S | The plan can change mid-flight; a change of intent goes to Batu | §3: "A filename on disk is not an epistemic approval" |
| 6 | Record where new work came from; compute readiness separately | BD FINDINGS §2, §4; WM 08 §5 | `discovered-from` records origin "without becoming a prerequisite by default". "open does not mean actionable". The slice admitted to a session is not the whole plan. | S | For each discovered item, record its origin, what it blocks, and which session it is admitted to | WM 08 §2C: the list of ready work is "only as correct as the recorded graph" |
| 7 | Record for an unfinished inquiry | RPD ASSESSMENT §2, §5 | Store the need being pursued, parent link, alternatives, assumptions, expected sub-result, sources read, next step, return_to and stop reason. Keep it in the existing work and evidence files, with no second state store. | C + synthetic tests; the original sources are not in the repo | Open design questions survive across sessions | MECHANICAL-OBSERVATIONS: item B was saved as "ACCEPTED/CHECKED" while its prerequisite A was still "OPEN" |
| **(3) Plan revision, convergence and remediation** |
| 8 | New work is appended; defects are fixed at their source | SK FINDINGS §7, §9–13 | Converge appends "Phase N" tasks that cite the requirement or decision behind them. Existing tasks are "never reordered, renumbered, deleted or rewritten". A read-only analyze step sends each defect back to the artifact that owns it. | S | Append new work with its reason; fix the upstream artifact, not the easiest downstream one | "convergence procedure ≠ proof of correctness" |
| 9 | Keep the accepted plan, the deviations and the as-built state apart | PB 04 §5 (F4); WM 08 §7 | "A bad plan can appear to have been 'correct' because it is revised after implementation." Reopening, revising, appending and retrying are different moves. | L; S | Mark the version Batu accepted; log each deviation with its reason | Extra overhead |
| 10 | Capped fix loops, then a ruling | SP S04 §3; GS review-qa-ship §8 | SP: rounds 1–3 use the same worker, rounds 4–5 a fresh stronger one, then park with a reason or unblock explicitly. GS: loop until a pass makes zero fixes, "bounded to three cycles; non-convergence then becomes a blocker". | S (GS also has tests) | Cap critique-and-revise rounds; escalate non-convergence | "Neither five rounds nor a final fix wave establishes that a remaining issue is false" |
| **(4) Verification and review** |
| 11 | Reviewer gets its own inputs; the coordinator's conclusions are withheld | MAP SOUL-DEVELOPMENT-OS-ASSESSMENT §8, C5, R4; GS multi-agent §1.1, §6; PB 01 §8.2; SP S04 §2, §4 | The verifier gets the original work definition, the exact target version, the criterion and direct evidence. It reports and does not repair. Earlier findings are withheld from it. It treats rationales "as unverified". Review that comes back "requires technical evaluation" before anyone acts on it. | C; S+T; L | Read-only reviewer on file@SHA with Batu's criteria; the coordinator rules on each finding; re-review after any material change | "new context window ≠ independent model ≠ independent oracle"; MAP R7 "reviewer ritualization" |
| 12 | Explicit states for missing or failed checks | GS review-qa-ship §4, §11; testing-eval §10.2 | Plan items are marked DONE / PARTIAL / NOT DONE / CHANGED / UNVERIFIABLE. It "forbids silent blanket confirmation". A timeout counts as missing coverage. "execution count is part of verification evidence". | S+T | Audit the plan items before claiming completion | "No plan file found → plan completion audit skips" |
| 13 | Completion has several levels; approval is not verification | GT FINDINGS §14; PB 04 §10 (F9) | A worker saying it is done ≠ the item closed ≠ the whole order complete ≠ integrated and accepted. "Human approved" is recorded separately from "technical claim verified". | S; L | Subagent done ≠ coordinator accepted ≠ Batu accepted | Merging these creates "false assurance" |
| **(5) Handoff and continuity across sessions** |
| 14 | Committed ledger; each ruling records its cost if wrong | SP S03 §5; notes/U02, U05 | "prefer the ledger and Git history over recollection". Each ruling records "decision, reason and cost if wrong" and is copied into the final message to the human before scratch files are deleted. | S+P, UA | Keep the ledger committed inside the package | U05 synthetic test: a git-ignored ledger was deleted by normal cleanup ("retention challenge FAIL"); an uncommitted plan was absent in a new worktree |
| 15 | A checkpoint is not current truth | GS memory-learnings §2; CORE F5 | The checkpoint is a summary written by the model and is not revalidated on restore. "checkpoint exists + is newest ≠ checkpoint claims are still current truth" | S+T (save-and-restore test only) | Re-check the handoff note against the repo when resuming | A stale handoff steers the work |
| 16 | Work state lives outside the conversation | CMH 03 §12; WM 08 §9; GT §9–10 | Start-up step, then a bounded increment, then commits and progress files, then a fresh session picks up. Conversation history alone is not enough. Persist expensive steps and "findings ... before session death". | L; S | Each session is one bounded increment ending in a commit | PB F2: the fidelity of an artifact chain is "assumed more than proven" |
| 17 | Summaries lose information | CMH 01 §11, §13; GS CORE F1 | Check each summary for: decisions kept, unresolved issues, rejected alternatives, source references, uncertainty turned into certainty, status labels. Subagent summaries need checking twice. | L | Fixed headings in handoff notes and subagent reports | "payload survives; qualifier disappears" |
| **(6) Memory and learning** |
| 18 | Choose where a lesson should live | SP S01 §1; PB 01 §7.2; GS CORE §12 | Options: a prohibition, a recipe, a required field, a condition, a mechanical check, or "no new skill". Classify the failure before adding more instruction text. GS's pattern: prose, then a named distinction, then a helper, then an invariant, then a test. | S; L | A lesson becomes a template field or check, not more prose | Instructions pile up |
| 19 | A change, its later use and its benefit are separate | HA synthesis/01 §4; notes/30, 15; SP CORE §6 | Making a change, using it later and getting better results "require three different kinds of evidence" (translated from Turkish). Being recorded as reused ≠ effective learning. A stored prompt can hide memory edits. | S + bounded synthetic runs | A lesson counts only when a later session is seen to behave differently | HA notes/02 §8 (a hypothesis): the review prompt pushes an update in most sessions, so rules accumulate |
| 20 | Learnings tagged by where they came from | GS memory-learnings §4–7 | Tags: observed / user-stated / inferred / cross-model. Rows the model derived lose confidence over time; user-stated rows do not. A filter blocks instruction-injection text at write time. | S+T | Tag lessons as Batu-stated or model-inferred | Nothing invalidates a lesson automatically when the files it cites change |
| **(7) What needs Batu and what does not** |
| 21 | Stop classes plus recorded rulings | SP notes/U02; CORE §7; CLOSURE-AUDIT §4 | The coordinator rules on most conflicts. It stops only for irreversible or destructive actions, security-sensitive actions, external effects that normally need consent, and cases where "every way forward is a guess". | S, UA | Default autonomy contract for the coordinator | The release notes cut this to one class; the lesson: "preserve the object, trigger, scope and exceptions of a guarantee". Q13 (scope change and re-approval) is unresolved. |
| 22 | Three decision tiers | GS planning-spec §1, §4, §5 | "Mechanical — auto-decide; Taste — auto-decide, record, surface at final gate". "User Challenge" (a change to the user's stated direction) is never auto-decided. After at least two alternatives, it stops for the user to choose. Questions the source can answer are not "bounced back to the user". | S+T (static tests; the end-to-end test is non-blocking) | Tier DevOS design choices | Combining workflows creates contradictory gates |
| 23 | Human gates are for authority, not uncertainty | MAP §9, C6, R6; RPD ASSESSMENT §2 | The human is not "the hidden merge algorithm". Finding that a decision is needed ≠ inventing its answer. Measure the user's burden of filling in missing technical discovery, not the number of questions. | C | Ask Batu about values, scope and acceptance only | PB F10: parallel output is limited by review capacity |
| **(8) Motion without progress** |
| 24 | Kinds of stall; circuit breaker | GT §8, §13; BD §11 | Blocked, waiting, running, no worker, worker gone, or container still open: "All can look superficially like 'not progressing'". A dispatch is "circuit-broken" after 3 failures. | S | Classify each stall; stop after 3 failures | An empty ready list may mean the plan graph itself is broken |
| 25 | Check for necessary work nobody was assigned | SP S06 §3 (PC2) | The assistant "declared closure before sufficiently considering how the output would be produced. The owner exposed the missing perspective." | A recorded omission in this project | Ask this before closing any step | Plan self-review only covers work already in the plan |
| 26 | Budget and proxy traps; no stockpiling | RPD ASSESSMENT §2; HA STATE, synthesis/01 §6; SP S01 §5, S03 §6 | "Context or budget running out is not readiness/completion" (translated). Don't start a second slice before the current one is published and read back (the repo's own research rule, not a Hermes product feature). Don't repeat narrow confirmation tests. A parser fix raised accepted-report counts without better agent work. | C; S | Count progress as a changed decision or explanation, not as documents or subagent runs | PB F13/F14: metrics become proxy targets |
| 27 | Subagents that stall or collide | GS multi-agent §3–4 | Claude Code's switch to background-by-default subagents left parent workflows waiting forever ("third recurrence"). Fix: bounded wait, no duplicate launch, cancel, reconcile against the commit recorded before dispatch. Fresh context ≠ filesystem isolation. | S+T+commit history | Record HEAD before dispatch; never launch a second writer on the same files | Partial edits left in the shared working tree |

### 2. Top 8 for EXP-007's own operation

The environment limit (subagents cannot spawn subagents) matches SP's own contract, which forbids workers and reviewers from nesting. GS suppresses nested reviews by the same model after one cost about 15M tokens. So the limit costs EXP-007 little.

1. **A committed control surface (rows 5–8, 14, 16).** Three files in the package:
   - STATE: current phase, the admitted slice, next responsibility, open inquiries with return_to.
   - PLAN: the version Batu accepted, plus appended items with origin, what each blocks, and a status from a fixed set.
   - DECISIONS: each ruling with reason, cost if wrong, and who decided.

   Commit after each step. Never keep these in ignored scratch.
2. **One brief template and one return schema (rows 1–4).**
   - The brief states: the purpose chain, the admitted slice, Batu's binding decisions, the files to read at a given SHA, what is out of scope, and which files may be written.
   - The return gives: a status code, claims each with an evidence pointer and evidence status, assumptions and auto-choices, open questions, and files touched.
   - The coordinator treats the return as data. It re-dispatches only with a changed brief.
3. **A read-only reviewer with its own inputs (row 11).** The reviewer gets Batu's original request and acceptance criteria and the artifact at a SHA, not the coordinator's reasoning. It must state which failure classes it checked. The coordinator records a ruling on each finding. Label the result "same-model fresh-context review", not independent verification.
4. **A checkpoint audit before any claim of completion (rows 12, 13, 24–26).** Mark each item DONE / PARTIAL / NOT DONE / CHANGED / UNVERIFIABLE with an evidence pointer. Ask which necessary work is unassigned. Classify anything stalled. Add one line saying which decision changed. NOT DONE and UNVERIFIABLE items go to Batu one by one.
5. **Decision tiers plus stop classes (rows 21–23).**
   - Mechanical choices: decide and log.
   - Taste choices: decide, log, and batch them to Batu at the checkpoint.
   - Stop and ask for: a change of scope or intent, value trade-offs, acceptance, irreversible or external effects, and cases where every option is a guess.
   - Research anything the repo can answer. Record Batu's approval separately from verification.
6. **Bounded revision (rows 8–10, 24).** At most 3 critique-and-revise rounds per artifact, and each retry must change something. Then park the finding with a reason, or escalate it. Three failures of the same step trip a circuit breaker. Fix the upstream artifact and keep the accepted plan version.
7. **A resume protocol with honest handoffs (rows 15, 17).** On resume, read STATE, then PLAN, then DECISIONS, then the git log. Treat the previous handoff as claims to re-check. The handoff note uses fixed headings: decisions, unresolved items, rejected alternatives, sources, evidence labels, next responsibility.
8. **Lessons as targeted changes (rows 18–20).** Each lesson records the failure that triggered it, its source (Batu-stated or inferred), where it lives (a template field, a check, a brief rule, or nothing), and the later session where the changed behavior was seen. Until then it is marked "unverified".

### 3. Avoid or postpone

1. **A custom state engine** (its own head/object store, leases, fencing, atomic claims, daemons: the RPD continuity design and the BD/GT substrates). Only one writer exists here. RPD itself says a second state authority is not built by default, and its probe shows that records do not compute truth.
2. **Agreement counting or reviewer fan-out as verification.** Rules of the form "agent count ≠ epistemic independence" apply: GS's confidence boost for agreeing specialists is "not a calibrated probability update", and the combined output also outruns Batu's review capacity (PB F10). Use parallel subagents only for independent read-only evidence gathering, under an explicit merge contract (MAP C3).
3. **Automatic memory pipelines** (a Hermes-style background review, GBrain, auto-decay, auto-editing CLAUDE.md). They accumulate rules, and use counts are not benefit.
4. **Regression evals for agent configuration, CI, or hooks treated as governance, before there is a need** (PB DP-01). Test suites go stale (F13), and "written rule ≠ runtime enforcement" (CMH AP-08). For now, state which EXP-007 rules are only advisory.
5. **One heavy lifecycle for every step** (six stages, a spec and plan for everything, a reviewer on every artifact). SP's own counter-example ("every request goes through design → written plan → SDD") fails; MAP R7 warns against reviewer ritualization and C10 treats "no multi-agent complexity needed" as a valid answer. Scale the ceremony to risk and to the cost of a missed dependency.

### 4. Reading coverage

- **Read fully:**
  - CATALOG.md and INDEX.md.
  - SP: META, CORE, CLOSURE-AUDIT, S01, S03, S04, S06.
  - GS: META, CORE.
  - WM: STATE, 10-CLOSURE-EVALUATION.
  - RPD: META, ASSESSMENT, MECHANICAL-OBSERVATIONS.
  - MAP: META.
  - HA: META, STATE, synthesis/01 and /03, notes 02, 15, 18, 28 and 30.
- **Read partially:**
  - GS syntheses: multi-agent §§0–6, memory-learnings §§1–8, review-qa-ship §§0–4 and 8–12, planning-spec §§0–5, testing-eval §10 and §28.
  - WM: META header, 08 §§2C–15.
  - MAP: SOUL-DEVOS-ASSESSMENT §§8–19; CONVERSATION-SYNTHESIS on merge, generator–critic and §8.
  - CMH: META, STATE header, 04 §§11–25, 01 §§11 and 13, 03 §§12–14, 20 and 24–26.
  - PB: META, 01 §§3, 7–8 and 13.3, 03 §§3.7–4.7 and 6, 04 §§3–11 and 14.
  - OS: META header, FINDINGS §§3–11. SK: FINDINGS §§6–13. BD: FINDINGS §§2–13. GT: FINDINGS §§1–19.
  - SP notes U02, U03 and U05: grep excerpts only.
- **Not read:**
  - SP: STATE, INDEX, METHOD, PLAN, S02, S05, ledgers, evidence.
  - GS: STATE, INDEX, CLOSURE-AUDIT, and seven other syntheses.
  - WM: METHOD, PLAN, 09.
  - META files for SK, BD and GT (catalog rows only), and all SOURCE-LEDGER files.
  - CMH 00 and 02. PB STATE, INDEX, 00 and 02. HA synthesis/02 and /04 and the remaining notes.
  - ECC is out of scope and unread. Its catalog entry flags "recurrent publication failures and unproven independent re-entry", which may be relevant to handoff (area 5).
