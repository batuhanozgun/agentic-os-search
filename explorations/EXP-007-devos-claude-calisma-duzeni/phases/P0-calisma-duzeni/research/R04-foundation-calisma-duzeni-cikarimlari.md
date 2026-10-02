# R04 — Foundation'ın uzun soluklu AI çalışmasının işletimine dair söyledikleri

**Tür:** Alt ajan raporu (model çıktısı). EXP-007 P0 okuması, 27 Eylül 2026. Ajan salt-okuma kısıtıyla çalıştı; hiçbir dosya değiştirmedi.  
**Kullanım sınırı:** Bu metin kaynağın kendisi değil, kaynaktan türetilmiş bir görünümdür. Karar taşıyan her iddiada rapordaki yol/bölüm üzerinden özgün kaynağa dönülür. Rapor İngilizce yazıldı; alıntılar özgün dilindedir. Metin ajanın teslim ettiği haliyle, değiştirilmeden aktarıldı.  
**Soru:** Foundation'ın planlama/kabul/kapanış/yeniden açma, bilgi seçimi ve sunumu, aktör/yetki ve bileşim/geri bildirim üzerine hangi bulguları EXP-007'nin çalışma düzenini şekillendirmeli?  
**Ana oturumun kontrolü:** Ana oturum şu ifadeleri kaynağında kendisi okudu: 08/SYNTHESIS §4 "Discovering a missing decision is not permission to make it on the owner's behalf."; 08/REUSE "A role need does not imply an AI agent..."; Foundation STATE "Structural coverage is not engineering sufficiency." ve soru bankası örneğinde kapanışın erken ilan edilmesi. Rota sorunları (Records yolu, çelişen STATE'ler) ve diğer iddialar ana oturumca doğrulanmadı.

---

**Foundation findings that should shape EXP-007's operating model**

Paths are relative to `/home/user/agentic-os-search/research/soul-foundations/`.
Key: **WV** `01_verticals/work/synthesis/WORK-VERTICAL-SYNTHESIS.md`; **WI** `01_verticals/work/findings/INTAKE-SELECTION-COMMITMENT-AND-PRIORITY.md`; **WG** `03_ground-deepening/grounds/work/synthesis/WORK-GROUND-AUDIT-SYNTHESIS.md`; **AV** `01_verticals/actors/synthesis/ACTORS-VERTICAL-SYNTHESIS.md`; **AG** `03_ground-deepening/grounds/actors/synthesis/ACTORS-GROUND-AUDIT-SYNTHESIS.md`; **AD** `03_…/actors/DEFERRED-RELATIONS.md`; **DYN** `03_…/information/informational-dynamics/` (S5/U5/E5 under `selection-exposure/`; R6, M5 and the Warrant KEY under `derivation-transformation/`; F2/F3/KEY under `formation-acquisition/`); **IS** `03_…/informational-state/synthesis/INFORMATIONAL-STATE-SYNTHESIS.md`; **REC** `01_verticals/records-artifacts/synthesis/RECORDS-VERTICAL-SYNTHESIS.md`; **I** `07_selection-dynamics-integration-review/SYNTHESIS.md`; under `05_relation-control-composition/`: **CC** control synthesis, **CK** control KEY, **CS** standing synthesis, **BK** binding KEY, **TP** propagation KEY, and **G6** and **D1–D3** under `transition-effect-feedback/feedback-adaptation/`; **B1** `06_integration-frontier-review/B1-PARENT-INTEGRATION.md`; **08/** `08_foundation-sufficiency-reuse-review/`; **RUA** `RESEARCH-USE-ALIGNMENT.md`.

Each quote is what Foundation says. The text after it is my implication for EXP-007. [direct] means Foundation itself applies the point to handoffs, workers, SOUL or Development OS. [inference] means I am applying it.

### (a) Planning, admission, execution, closure, reopening, frame authority

1. **A candidate is not admitted work, and "not done" has several meanings.** WV §4; WI §5. Quote: "Demand is not automatically commitment; backlog is not automatically WIP" and "Treating all of these as `cancelled` destroys the reason Work ceased or never began." Implication: keep the candidate pool separate from admitted work. Admission should be an explicit act with a named person or role behind it. Record why work did not happen: rejected, deferred, superseded, terminated or failed. [inference]

2. **A deviation is not a failure, and changing the frame needs the owner.** WV §5; 08/SYNTHESIS §4; U5 §5. Quote: "A plan deviation cannot be classified as failure from the deviation alone." Also: "Discovering a missing decision is not permission to make it on the owner's behalf." And: "do not count success against an easier substituted goal as completion." Implication: classify each plan revision. Elaboration inside the granted scope can be the coordinator's call. A change of purpose, criteria or scope is proposed with its reason and decided by Batu. Drift is reported, not quietly absorbed. [direct on the principle; the mechanism is inference]

3. **Completion is several separate facts.** WV §11 and §15 ("checklist fallacy"). Quote: "`done` is often a vector of predicates rather than one fact. Completion of child tasks is evidence, not logical proof…" Implication: close a package only on separate predicates: executed, verified against the stated criteria, validated for Batu's use, and accepted by Batu. [inference]

4. **Foundation deliberately leaves open who may change Work state.** WV §16; AG §2.4. Quote: the synthesis "does not establish … who may select, commit, reprioritise, waive, accept, terminate or reactivate Work"; also "Work acceptance state != authority to accept." Implication: EXP-007 must assign each right explicitly: admit, reprioritize, waive, terminate, accept, reopen and change the frame. Foundation gives no default. [direct that the question is open]

5. **Reopening is named and bounded.** 08/COMPLETION-AND-RESIDUALS "Reopening threshold"; CS "Currentness". Quote: "A useful reopening request names the failed claim or lost distinction … It may invalidate only one leaf." Also: "dependency changed → standing may require re-evaluation != standing necessarily changed." Implication: reopen a result only with a named trigger, at the smallest affected scope. A changed dependency means "re-evaluate", not "invalid". [inference, modelled on Foundation's own practice]

6. **Rework and meta-work are ordinary work.** WV §§7, 8, 12; WG §6. Quotes: "Failure can be a generator of new Work"; "Coordination is itself Work…"; "Meta-work—Work that changes workflow, agent configuration, verifier, tooling or the working system—is ordinary Work at another target level"; "more work started does not logically entail better end-to-end system progress." Implications:
   - Rejected subagent output creates typed rework. Partial writes need to be reconciled; do not assume they were rolled back.
   - Changes to the operating model itself are admitted and accepted like any package.
   - Put a limit on how many subagents run in parallel.
   [inference]

### (b) Information: selection, exposure, acquisition, summaries, warrant, revision

1. **A brief is adequate only for a stated use.** U5 §2; S5 §7. Quote: "A view's adequacy therefore belongs to a use relation, not to its file once and for all." Also: "A useful handoff must identify the protected informational need and the actual availability it establishes, without claiming that the receiving actor has understood or acted on it." Implication: each subagent brief states the use it serves, the alternatives, scope, criterion and acceptable loss. [direct]

2. **A pointer is not content, content is not use, and consumers are not pooled.** E5 §7 (E5.1) and §9; S5.5; I §3 and §7 (I2). Quotes: "Locator, content presence, interpretation, acceptance and action are not equivalent"; "Do not pool consumers, branches, sessions or times…"; "do not assume unobserved model knowledge, a forgotten earlier session or another worker's private state as that side information." Implications:
   - A file path in a brief gives the subagent a chance to read something; it does not give it the content.
   - What the coordinator or Batu's chat knows is not what the subagent knows.
   - Supply the background the subagent needs, and check content wherever a claim depends on it.
   - Never record "the subagent knew X" just because X was included.
   [direct: E5 §9 describes exactly these research-worker failures]

3. **Summaries and derived records are limited to their scope.** R6 §2; IS §8; REC §6. Quotes: "Bind the protected purpose, question family, recipient/background resources and horizon"; "Source-required omissions and unsupported output additions are different directions"; losing the mode "can turn `someone reports X` into `X is established`"; a view "must not silently stand for a different source/version/standing or support stronger claims than its binding, coverage and freshness justify." Implications:
   - Subagent returns, STATE files and handoffs keep the mode (verified, claimed or hypothesis), scope, attribution, open alternatives, as-of date and source links.
   - Check omissions and unsupported additions separately.
   - Deciding which surface is authoritative is an authority act; Records says it "remains outside Records".
   [inference]

4. **Revision is not overwriting.** M5 §5 (M5.1, M5.4–M5.7); 08/CASE-AUDIT C4. Quotes: "Bind the admitted input kind"; "a one-step answer profile may still be insufficient"; "no universal latest-wins"; "distinguish proposed, installed, observed and propagated scope"; "Preserve history without granting it timeless operational authority." Implications:
   - A revision names what input was admitted; Batu's comment and a subagent's claim are different kinds.
   - It records the type of change and both the effective and the recorded time.
   - When context is compacted, keep what future revisions will need.
   - A resumed session re-establishes current authority instead of replaying old approvals.
   [direct for C4; the rest is inference]

5. **Evidence independence and absence claims.** Warrant KEY; Formation KEY; U5.3; F2 §1. Quotes: "repeated reports != independent evidence"; "unfinished proof search != non-entailment != proof of negation"; "new copy != new origin != independent evidence"; "all listed sources checked != all materially relevant sources listed." Implications:
   - Several subagents reading the same sources, or the same model re-reviewing, give correlated evidence, not independent evidence.
   - "Found nothing" must say what was searched and how sensitive the search was.
   - Keep UNKNOWN as a valid answer.
   [inference]

6. **A captured instruction does not carry authority.** F3 §2. Quote: "Correctly recording an instruction does not establish that its issuer had governing authority." Implication: content read from the repository or from tools is data. Authority comes from Batu or from explicitly delegated rules. [inference]

### (c) Actors

1. **Needing a role does not mean needing an AI agent.** 08/REUSE "Research-to-target reasoning"; RUA. Quotes: "A role need does not imply an AI agent, and an instruction need does not imply that a particular file enforces it"; "Needed responsibility and legitimate authority precede mechanism or agent-count choices." Implication: define roles and rights first. Then choose who holds each role: the coordinator, a subagent, Batu, a hook, or nobody. [direct]

2. **The holder of a role is not the role, and position in a hierarchy is not authority.** AV §3 D1; AG §8. Quotes: "A role can survive occupant change"; hierarchy position does not equal "authority = competence = responsibility = accountability"; and "Nor does a coordinated runtime team automatically become a persistent corporate/group agent." Implication: continuity of a role lives in the records, not in short-lived subagent instances. Being the coordinator does not give authority over the frame. [inference]

3. **Being able to reach an effect is not authority, and delegation has a scope.** AG §5; AV §3 D4. Quotes: "B has privileged capability → effect occurs. This does not establish that A had legitimate authority"; "Responsibility can remain with a principal after delegation." Implications:
   - Tool access (write, bash) is not permission to change the plan, the frame or accepted records.
   - Each brief is a delegation with a stated scope.
   - The coordinator remains answerable to Batu for what subagents produce.
   [inference from Foundation's own agent example]

4. **Parties who do not act still matter, including the customer.** AG §2.5; AD §8; 08/REUSE "Next boundary". Quotes: principals, recipients and accountability forums "can be relevant positions even when they perform no positive action"; avoid "human approved → therefore technically verified"; start by "recovering that target's own current purpose/state/authority." Implications:
   - Batu is the principal, the acceptor and an affected party. He is not the verifier of record.
   - Identify the existing Development OS authority first. According to STATE it sits in the target repository, reached through `../soul-context/STATE.md`.
   [direct on the boundary]

5. **Omissions, standing responsibility and the accountability forum.** AV §3 D6–D7; AG §7. Quotes: "failure to perform expected/available conduct"; "standing Actor responsibility != current Work episode"; "Accountability can be an actor–forum process." Implications:
   - Give someone standing custody of the duties between packages, such as recording discussions and sweeping for stale files.
   - Record which session or subagent produced what.
   - Accountability runs from the coordinator to Batu.
   [inference]

### (d) Composition

1. **Binding.** BK. Quotes: "represented/asserted binding != actual binding"; "graph reachability != legitimate transitive relation." Implication: evidence links should name the exact version, section and role, as Foundation does with commit and blob IDs. A bare filename is not enough. [inference]

2. **Standing has layers.** CS "Strongest three-layer distinction" and "Result semantics". Quotes: "object/constitutive standing != epistemic assessment != decision/recognition outcome != Information record/status field"; "false != unknown / indeterminate != not evaluated != not applicable != stale." Implications:
   - Status must be able to say "not evaluated" and "stale".
   - A verifier's output is an assessment, and Batu's acceptance is a recognition decision. Neither is the status field itself.
   [inference]

3. **Gates and separation of duties.** CC "Gate decomposition" and "Authority and separation of duties". Quotes: "review complete != gate satisfied != authorized go decision != enforced progression"; "two role labels != two independent Actors"; "producer self-check != independent verification." Implication: a verifier subagent from the same model is a new role label, not an independent actor. State what independence it actually has, such as a fresh context or different evidence. [inference]

4. **Enforcement coverage.** CC "External holdout result" and "Currentness"; CK; RUA. Quotes: "advisory instruction != deterministic enforcement"; "one denied tool path != all effect paths closed"; "policy changed != every enforcement point updated instantly"; "waiver record != valid/applicable waiver"; an instruction file's "existence does not establish real capability, current authority, actual loading or enforcement." Implications:
   - Rules written in CLAUDE.md or in briefs are advisory.
   - For each effect you want to protect, list the paths that could reach it. Then decide whether to enforce (permissions or hooks) or to detect.
   - After changing a rule, check which sessions are still running on the old briefs.
   [direct, via RUA]

5. **Propagation.** TP. Quotes: "approved / committed / issued change != incorporated / realized change"; "all known targets updated != all materially applicable targets known != full propagation established." Implication: a decision recorded in one place must reach the files that depend on it. Closing a package includes checking that it did. [inference]

6. **Feedback must actually be used.** G6 "Required distinctions" and "SOUL interpretation". Quotes: "signal produced/delivered/read != operative use established"; "can SOUL distinguish a signal merely present in context from an applicable response that actually used it"; "more self-review messages are not automatically more independent knowledge." Implication: for each of Batu's comments and each verifier finding, record the response and where it took effect. A deliberate decision to hold also counts as a response. [direct]

7. **A stored lesson is not a behaviour change.** D1 §4; D3 §§2–4; D2 §6; B1 §2; 08/CASE-AUDIT C4. Quotes:
   - "A durable lesson can be inaccessible, unselected, overridden or irrelevant. Its mere existence is Information state."
   - "carrier written != candidate path installed != relevant path traverses carrier != response disposition changed at that locus != all applicable paths changed != retained after the claimed lifecycle transition"
   - "Testing can be an intervention."
   - "A new operator, model version, tool interface or coordination pattern can change applicability even when the lesson text is unchanged."
   - "Measure the claimed behavioral/effect property rather than infer it from a changed file."

   Implication: for each lesson, record:
   - who is supposed to behave differently;
   - where the lesson is stored;
   - how it gets loaded into that future consumer's context;
   - which situations it applies to;
   - how long it should hold (next session, after compaction, after a model change);
   - the evidence that it worked, from a trace or a matched probe, noting that the probe itself can teach the target.

   B1 also says a before/after improvement does not prove causal benefit. [direct on the distinctions; the mechanism is inference]

### Warnings and counterexamples most relevant to an AI team running long work

1. **Structure is not engineering.** STATE: "Structural coverage is not engineering sufficiency. A branch is not a mandatory service, file or agent; four grounds are not four independent boxes or a required execution order." Do not turn Foundation into a checklist or assign one subagent per ground.
2. **The knowledge existed but was not applied (a real episode in this repository).** 08/DISCUSSION-HANDOFF §§2–3: "The assistant nevertheless declared the example finished." Also: "The adequacy of the knowledge, its discoverability and its actual application must remain separable questions." Closing too early, anchored on the first salient view, is the failure actually observed. Batu's challenge was a legitimate reopening. No fix has been proven.
3. **Lossy application of the framework.** 08/RIVALS-AND-REUSE §7 names the main risk as "silently centralizing goals/authority, confusing stored representations with realized effects or treating a routed requirement as technically solved." §4 adds that folding plural purposes "into one agent's plan" fails.
4. **Same-model review is not independent, and readback is not benefit.** WG §12: "User evaluation can close sequencing but does not change this verification status." STATE: "Repository readback tests recorded availability and consistency, not future comprehension or behavioral benefit."
5. **Continuity failures happened in this corpus.** DISCUSSION-HANDOFF §1: "The intervening discussion and its correction had not been persisted." RIVALS §6 found three stale surfaces that looked current. More remain; see route problems below.
6. **Expressed direction is not a grant.** STATE: "Do not fabricate a formal approval or a target execution grant. Equally, do not pretend the discussion never happened." I5: "Carry separate status for … acceptance, publication, target evidence and independent verification." Record Batu's exact words and what they cover.

### Reading coverage and route problems

**Read in full:**
- STATE and RUA.
- 08/: REUSE, SYNTHESIS, CASE-AUDIT, RIVALS-AND-REUSE, COMPLETION-AND-RESIDUALS, DISCUSSION-HANDOFF.
- Work: INDEX, KEY, FINDINGS-MAP, WG, DEFERRED-RELATIONS, OPEN-QUESTIONS, and WV.
- Actors: INDEX, AG, AD, OPEN-QUESTIONS, and AV.
- Information: INDEX, KEY, STATE; the full Informational State route.
- Selection: INDEX, KEY, S5, U5, E5; and I.
- R6, W6 and M5 with their KEYs; Formation INDEX, KEY, F2, F3, F6.
- Composition: INDEX, KEY, FINDINGS-MAP, parent synthesis; CC.
- KEYs for Binding, Standing, Propagation, Causal, Feedback, Returned Influence and Persistent Adaptation.
- G6, D6, B1, and the Records KEY.

**Read in part:** CS (the layer and profile sections); D1 §§1–5, D2, D3 §§1–4; REC §§4–7; WI; the status lines of the Selection, 07 and Feedback/Adaptation STATE files.

**Not read:**
- The Environment ground.
- The numbered research passes.
- U4 and E4.
- The Binding, Propagation and Causal syntheses.
- 07 COMPLETION-DEPTH; 08 PLAN, SOURCE-LEDGER, PUBLICATION; 06 B2–B5.
- The checks programs, `../soul-context/STATE.md`, and the studies and explorations.

**Route problems:**
1. **Broken Records route.** REUSE's revision row points to "Information INDEX → Records profile", but that INDEX has no Records entry. Records is actually at `01_verticals/records-artifacts/KEY.md` → REC.
2. **Work and Actors routes point to thin files.** The rows send readers to the ground-audit syntheses §§2 and 4–8, which mostly just name the families.
   - The distinctions that matter here are in WV and AV: admission, completion predicates, recovery, delegation, omission, and the open "who may…" question.
   - CASE-AUDIT cites "Work synthesis §§…" without saying which of the two Work syntheses it means, and their section numbers differ.
3. **Conflicting status files.**
   - Selection STATE says "separate I1–I5 evaluation pending", and Selection KEY agrees. Both contradict 07 STATE and the root STATE, which record I1–I5 as accepted.
   - The Feedback/Adaptation INDEX says "Three promoted Information children remain unresearched". That INDEX's KEY and the Transition KEY also remain stale, even though the Feedback/Adaptation STATE was corrected.
   - The root STATE resolves these conflicts. They are a live example of the propagation failure TP describes, which makes them concrete input for how EXP-007 revises records.
4. **Historical labels.** REUSE's "Next boundary" section and many synthesis headers still read as awaiting evaluation. These are labels from when each pass was written; the root STATE governs.
