# Superpowers Study — Index

ACTIVE / PARTIAL **external-target candidate study**, not Foundation authority or an adopted stack.

**Continue from [STATE.md](STATE.md)** and its full cold-start path. U01–U05 and U06-A have bounded source investigations. **U06-B evaluation implementation is next; U06 overall remains open.** Primary corpus: `obra/superpowers@b36e0829c6d0140e93cfef2ca599b1b07d4a7797`. Separately pinned eval dependency: `prime-radiant-inc/superpowers-evals@e64684cd1fa270c464ac797747e45bbe8d127e8b`, orientation only. Do not transfer its newer descriptions to the primary target without compatibility checks.

## Package routes

| Need | Entry |
|---|---|
| Purpose, authority, completed/open work and next action | [STATE.md](STATE.md) |
| Classification, reuse and boundaries | [META.md](META.md) |
| Evidence/completion criteria and synthesis method | [METHOD.md](METHOD.md) |
| Provisional sequence and revision/reflection record | [PLAN.md](PLAN.md) |
| Sources through U02 | [SOURCE-LEDGER.md](SOURCE-LEDGER.md) |
| U03 sources/execution | [SOURCE-LEDGER-U03.md](SOURCE-LEDGER-U03.md) |
| U04 sources/execution | [SOURCE-LEDGER-U04.md](SOURCE-LEDGER-U04.md) |
| U05 sources/execution and lifecycle boundaries | [SOURCE-LEDGER-U05.md](SOURCE-LEDGER-U05.md) |
| U06-A sources, external dependency pin and exact partial-read limits | [SOURCE-LEDGER-U06A.md](SOURCE-LEDGER-U06A.md) |
| Request classification, procedural scope, shell bootstrap | [U01-A](notes/U01-entry-routing-and-bootstrap.md) |
| Host delivery, cache and procedure/work recovery | [U01-B](notes/U01B-host-delivery-and-continuity.md) |
| Approval/ruling, plan/workspace identity and brief handoff | [U02](notes/U02-approval-plan-workspace-handoff.md) |
| Actor/reviewer packets, fix/park/complete and evidence range | [U03](notes/U03-delegation-review-and-acceptance.md) |
| Tests/oracles, diagnosis, feedback and verification claims | [U04](notes/U04-testing-diagnosis-and-verification.md) |
| Human integration choice, merged result, cleanup ownership and surviving evidence | [U05](notes/U05-delivery-cleanup-and-retention.md) |
| Intervention forms, authoring/control experiments, pressure criteria and contribution admission | [U06-A](notes/U06A-skill-authoring-and-change-admission.md) |

## Evidence routes

| Experiment | Runner / actual output |
|---|---|
| Shell bootstrap | [U01-A runner](evidence/U01-hook-probes.py) / [output](evidence/U01-hook-probes-results.json) |
| OpenCode callbacks | [U01-B runner](evidence/U01B-opencode-probes.mjs) / [output](evidence/U01B-opencode-probes-results.json) |
| Plan/workspace/extraction | [U02 runner](evidence/U02-handoff-probes.py) / [output](evidence/U02-handoff-probes-results.json) |
| Review-range/description predicate | [U03 runner](evidence/U03-review-probes.py) / [output](evidence/U03-review-probes-results.json) |
| Diagnostic observation versus final claim | [U04 runner](evidence/U04-diagnostic-probes.py) / [output](evidence/U04-diagnostic-probes-results.json) |
| Integration/cleanup/retention; local-only detached push | [U05 runner](evidence/U05-lifecycle-probes.py) / [output](evidence/U05-lifecycle-probes-results.json) |

U06-A is source-only. There is no new experiment, model response, pass rate or execution record. Historical scenario documents are not new test results.

## Claim-directed re-entry

| Claim or uncertainty | Re-enter |
|---|---|
| Every task requires written spec/plan | U01-A F01; U02 F13–F14; S10: three paths differ. |
| Mandatory wording technically constrains every actor | U01-A F02; U02 F13; U03 F21: instructions, authority and capabilities differ. |
| Shared skills imply identical host behavior | U01-B F07/F10 and host matrix. |
| Marker/successful output proves valid current bootstrap | U01-A F04–F06; U01-B F08/E03/E04. |
| New session reloads source | U01-B F08/Q09: module/session/source lifetimes differ. |
| No work recovery exists | U02 F16: ledger/artifacts exist, with identity/retention limits. |
| Per-plan folders are disjoint; same path means same revision | U02 F16/E05/E06/Q14. |
| Task extraction supplies all requirements | U02 F17; U03 F20–F21: controller globals/coverage transfer. |
| Saved plan is available to executor | U02 F18: materialisation prerequisite. |
| Successful ignore check qualifies chosen path | U02 F19: wrong-alternative predicate. |
| Two verdicts mean two independent reviewers | U03 F20/S37: one task reviewer, separate scoped/final reviews. |
| DONE/complete means all defects fixed | U03 F22: clean and parked completion differ. |
| Fresh reviewer context proves independent test execution | U03 F21; U04 F33: shared evidence/reuse. |
| All work is parallel, or parallel rules universally conflict | U03 F24: independent-domain dispatch versus serial SDD. |
| Generated packet covers whole task/current worktree | U03 F25/E07/E08: caller-selected commit endpoints. |
| Existing test measures current rule | U03 F26; U05 F42: predicate/source-policy scope. |
| Generic/specialised skills compose automatically | U03 F27; U04 F28/F29/F31/F33; U05 F41; U06-A F44/F46. |
| Test-first or one RED–GREEN proves adequate coverage | U04 F28/S44/S47: chronology, sensitivity and oracle validity differ. |
| Three failed fixes prove architectural cause | U04 F29: escalation rule, not independent causal evidence. |
| Waited-for event belongs to current operation | U04 F30/S51/S52/Q25: type/count versus bound predicate. |
| Feedback is automatically an implementation order | U04 F31/S46: understand and evaluate first. |
| Passing tests prove all requirements | U04 F32/S45; U05 F36/F41: acceptance and integration/disclosure differ. |
| Reused report equals current-message verification | U04 F33/Q18/Q24: actor/claim/stage and dependencies. |
| No polluter found proves successful clean test execution | U04 F34–F35/E09/E10: zero, skipped and failed-launch cases. |
| Every string assertion is a source-text test | U04 F35: runtime output can be a valid but scoped observable. |
| Task completion authorises merge/discard | U05 F36/S55: human choice; explicit discard request/confirmation. |
| Separately green branches imply green merged result | U05 F37/E11/E12: source requires retest; combined fixture fails after clean merge. |
| A merge conflict automatically rolls back | U05 F37/E12: unmerged state and MERGE_HEAD remain. |
| Detached HEAD itself forbids pushing | U05 F38/E12: Git capability versus host policy; local-only refspec test. |
| Directory name proves cleanup ownership | U05 F38–F39/Q26: convention versus actual creator/authority. |
| Kept worktree permits its checked-out branch to be deleted | U05 F39/E12/Q29: deletion refused without host exit/detach. |
| Non-force removal protects all only-copy records | U05 F40/E12: ordinary untracked note protected; ignored SDD ledger removed. |
| PR/keep guarantees all SDD evidence survives | U05 F41: inner scratch and outer worktree have separate lifecycles. |
| Code history contains every ruling/report | U05 F40–F41/Q27: committed code, disclosed decisions and detailed evidence differ. |
| Source-policy/native-preference tests prove lifecycle ownership | U05 F42/S56/S57; evaluator implementation remains U06-B. |
| Every failure calls for another skill or stricter prohibition | U06-A F43/F45: intervention layer and failure type matter. |
| Description guidance is the format specification or the full procedure | U06-A F44/S58/X07: distinct authorities/roles; historical review anecdote is not current topology. |
| No-guidance benefit proves a new revision beats the old one | U06-A F43/F46/Q30: different comparison and confounders. |
| Pressure compliance proves useful general task performance | U06-A F46/Q31/Q32: criterion, observable and outcome differ. |
| A worked campaign/creation log is raw current execution evidence | U06-A F47/S64–S69: design, expected result and historical narrative differ. |
| A completed PR template proves actual review or release | U06-A F48/Q34: admission contract versus realized enforcement. |
| External current evals automatically qualify this primary pin | U06-A F49/D01–D03/Q33: separately versioned dependency, README partial, compatibility open. |

## Synthesis and evidence status

Seven chronological notes and six local experiment records exist. All fourteen observed SKILL bodies are fully read, but their supporting dependencies, evaluator implementation, runtime/release and whole-system explanation remain incomplete. No CORE, Foundation projection, completed cross-study comparison or whole-study closure exists.

U06-A has twelve new primary full-file reads and no new behavioral execution. The external lab's metadata/root tree and README lines 1–165 are orientation, not implementation or results validation. The primary corpus was not repinned. Earlier E01–E12 and failed criteria remain unchanged.

Five chronological source-ledger volumes preserve identities and observations. Historical next-action lines are checkpoints; current authority is STATE. Earlier unexecuted statuses change only when a later volume records actual execution of the named source.

## Library navigation

- [Candidate catalog](../CATALOG.md)
- [Candidate-library index](../INDEX.md)
- [gstack method precedent](../gstack/METHOD.md)

Upstream instructions remain research objects, not active agent-control.
