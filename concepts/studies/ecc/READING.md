# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-20, **B6-T16-C3 / C1-C2-C3-DURABLE-COMPLETE / PACKAGE-PARTIAL**.

Bu dosya `research/studies/ecc/` paketinin concepts programı açısından gerçek okuma/coverage hesabını taşır. ECC source-study kendi açısından **ACTIVE / PARTIAL** durumundadır; current research next U13-A/Q07d1 **NOT STARTED**. Concepts extractor bu next-work talimatını assistant authority yapmaz; current repository package'ini kaynak olarak okur.

## 1. Kaynak kimliği ve boundary

- Repository: `batuhanozgun/agentic-os-search`
- B6-T16 başlangıç main: **4af0ba7b35152f47e59032c96357ba1269b6e7b1**
- Source package: `research/studies/ecc/`
- Study type: `external-target`
- Pinned upstream: `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a`
- Source-study status: **ACTIVE / PARTIAL**
- Source-study completed through: **U12-C / plan 0.29**
- Source-study next: **U13-A / Q07d1 — NOT STARTED**
- Concepts status: **B6-T16-E1 partial durable extraction**
- Foundation / SOUL / Development OS adoption: none.

## 2. Gerçek package inventory

Current main'deki ECC package:
- root files: **60**
- `notes/`: **27**
- `evidence/`: **68**
- `inventory/`: **4**
- total: **159 files**

Bu toplam semantic concept sayısı değildir.

## 3. ECC concepts partition plan

ECC package 159 dosya olduğu için concepts aktarımı altı bounded checkpoint'e bölündü:

1. **C1 — U01–U02:** surfaces / installation / ownership.
2. **C2 — U03–U04:** work / execution / memory.
3. **C3 — U05–U06:** learning / evaluation / governance.
4. **C4 — U07–U09:** material-family map / Plan Canvas / Rust-session-operator-runtime.
5. **C5 — U10–U12:** evaluation / workflow-distribution / profiles / OpenCode / Python provider family.
6. **C6 — package-wide closure:** rounds/publications/method-history/inventory/remaining evidence roles, cross-TERMS, source delta and final closure.

Bu partition source-study planı değildir; yalnız concepts continuity planıdır.

Current progress:
- **C1 U01–U02 DURABLE-COMPLETE.**
- **C2 U03–U04 DURABLE-COMPLETE.**
- **C3 U05–U06 DURABLE-COMPLETE.**
- Three linked term files exist and C1–C3 are now closed.
- exact next: **C4 U07–U09**. C5'e aynı turda geçilmez.

## 4. C1–C3 için şu ana kadar doğrudan okunan current source files

### Package control / purpose
- `STATE.md`
- `META.md`
- `INDEX.md`
- `METHOD.md`
- `PLAN.md`
- `00-WHY-THIS-RESEARCH.md`

### U01–U06 notes — 11/11 FULL
- notes/01 SURFACES-AND-CODEX-CACHE
- notes/02 INSTALLATION-CHANNELS-AND-MATERIALIZATION
- notes/03 OWNERSHIP-CHECKPOINTS-AND-PROJECTION
- notes/04 WORK-SESSION-RECORDS-AND-CONTROL
- notes/05 EXECUTION-HANDOFF-AND-RECOVERY
- notes/06 MEMORY-SCOPE-RECALL-AND-AUTHORITY
- notes/07 OBSERVATION-INSTINCTS-AND-BEHAVIORAL-CONTEXT
- notes/08 SKILL-OUTCOMES-EVALUATION-AND-CHANGE
- notes/09 CONFIGURATION-PROTECTION-AND-ENFORCEMENT
- notes/10 FACT-FORCING-STATE-AND-DECISION-COMPOSITION
- notes/11 GOVERNANCE-EVENTS-PERSISTENCE-AND-DECISION

### U01–U06 source ledgers — 11/11 FULL
- evidence/U01-A-SOURCES.md
- evidence/U01-B-SOURCES.md
- evidence/U02-A-SOURCES.md
- evidence/U03-A-SOURCES.md
- evidence/U03-B-SOURCES.md
- evidence/U04-A-SOURCES.md
- evidence/U05-A-SOURCES.md
- evidence/U05-B-SOURCES.md
- evidence/U06-A-SOURCES.md
- evidence/U06-B-SOURCES.md
- evidence/U06-C-SOURCES.md

### Bounded execution / recovery surfaces read
- u01-a-cache-probe: README, PROBE-PLAN, RESULTS
- u03-a-work-item-probe: README, PROBE-PLAN, RESULTS
- u03-b-worker-probe: README, PROBE-PLAN, RESULTS
- u05-b-evaluation-probe: README, PLAN; compressed exact result role recorded by source package
- u06-a-config-probe: README, PLAN; compressed exact result role recorded by source package
- u06-a-conversation-record: README; historical E05 identity reconciliation

E04/E05 compressed raw results were not text-read through the connector; their exact-byte/hash/role and derived observations are accounted through README/source-ledger/current note. Binary/compressed carrier ≠ unread semantic omission.

## 5. C1–C3 source roles

- **TARGET CLAIM / instruction contract:** architecture docs, skills, guides.
- **SOURCE OBSERVATION:** pinned code/config/schema.
- **TEST SOURCE INSPECTED:** upstream tests read but not executed.
- **LOCAL EXECUTION:** E01–E05 bounded fixture runs at recorded scope.
- **INFERENCE / counter-path:** code-composition result not newly executed.
- **Publication/recovery record:** transfer/history integrity, not behavior evidence.

Same assistant repeated checks are not independent replication.

## 6. C1–C3 contextual term drafts

Current linked inventory drafts:
- [TERMS-SURFACES-INSTALLATION.md](TERMS-SURFACES-INSTALLATION.md)
- [TERMS-WORK-EXECUTION-MEMORY.md](TERMS-WORK-EXECUTION-MEMORY.md)
- [TERMS-LEARNING-GOVERNANCE.md](TERMS-LEARNING-GOVERNANCE.md)
- [TERMS.md](TERMS.md) — package entry and cross-links.

File grouping is for readability; one file ≠ one term.

## 7. Current strongest interpretation boundaries

- repository/package/plugin/cache/install/runtime are distinct objects;
- provider registration ≠ cached-content completeness ≠ hook trust/invocation ≠ task benefit;
- requested component ≠ resolved module ≠ planned operation ≠ applied operation ≠ owned installed content;
- structurally valid install state ≠ completed installation;
- checkpoint/retry hint ≠ retry admission;
- task record ≠ run/worker ≠ accepted outcome;
- process exit/status ≠ handoff semantics ≠ work acceptance;
- stored memory ≠ reviewed/governed knowledge ≠ model-use;
- observation ≠ analyzed learning ≠ promoted instinct ≠ injected context ≠ behavioral benefit;
- skill invocation outcome ≠ task quality;
- proposal/recommendation ≠ admitted mutation ≠ validated improvement;
- guard decision ≠ host enforcement ≠ authorized effect;
- first-touch marker ≠ verified investigation;
- governance event ≠ persisted governance record ≠ approval decision ≠ enforced effect.

## 7A. C1 durable checkpoint — U01–U02 surfaces / installation / ownership

C1 exact source families:
- U01-A Note01 + U01-A source ledger + E01 plan/result/readme;
- U01-B Note02 + U01-B source ledger;
- U02-A Note03 + U02-A source ledger;
- inventory/STRUCTURE, TREE-FRONTIER and U01-B-DISCOVERY;
- PUBLICATION U01-A/U01-B/U02-A sections;
- METHOD-REVIEW MR01/MR02/MR03;
- RESEARCH-LOG U01-A/U01-B/U02-A sections;
- SOURCE-LEDGER U01-A/U01-B/U02-A sections.

Publication/history files were **selected-read at the exact C1 sections**, not falsely labelled whole-file FULL. Their role is chronology/scope/readback, not new behavior evidence.

C1 source-to-TERMS check found three concrete omissions and closed them:
- **ECC-S54 install profile**;
- **ECC-S55 hook profile**;
- **ECC-S56 source/runtime version binding**.

C1 term inventory now runs **ECC-S01–ECC-S56**. No duplicate/gap is intended; final package-wide ID validation remains C6.

C1 strongest closure boundaries:
- root/source family map is partial discovery, not complete ECC topology;
- harness name is not install-channel identity;
- install profile, hook profile, plugin enablement, hook trust and runtime/source version are separate dimensions;
- research pin does not force provider marketplace/runtime to install that pin;
- provider registration/readback is narrower than cache-content/hook/task readiness;
- planned/applied/owned/projected/healthy states are distinct;
- bridge/checkpoint can preserve recovery information without proving completed effects or retry admission;
- E01 is a bounded checker false-green observation, not a live Codex/product failure rate;
- U01/U02 publication and same-assistant method review do not upgrade source/test/local-execution evidence class.

**C1-DURABLE-COMPLETE** means U01–U02 contextual transfer is closed at the current source package. It does not close U01/U02 residual research questions, P1 inventory debt or ECC source-study.

## 7B. C2 durable checkpoint — U03–U04 work / execution / memory

C2 exact source families:
- U03-A Note04 + U03-A source ledger + E02 README/plan/result;
- U03-B Note05 + U03-B source ledger + E03 README/plan/result;
- U04-A Note06 + U04-A source ledger;
- PUBLICATION.md U03-A section;
- PUBLICATION-U03-B.md;
- PUBLICATION-U04-A.md;
- METHOD-REVIEW MR04/MR05;
- RESEARCH-LOG U03-A/U03-B sections;
- SOURCE-LEDGER U03-A/U03-B sections;
- ROUND-U04-A including MR06.

History/publication files were read at exact relevant sections or as bounded standalone unit files. Publication/readback evidence is chronology/integrity, not runtime evidence.

C2 source-to-TERMS check found and closed eleven source-local omissions:
- **ECC-W79** inspection persistence side effect;
- **ECC-W80** worker input identity;
- **ECC-W81** coordination-dir preservation vs content preservation;
- **ECC-W82** rollback resource scope vs produced value;
- **ECC-W83** worker enumeration set;
- **ECC-W84** observation-failure collapse;
- **ECC-W85** status timestamp vs heartbeat;
- **ECC-W86** session locator identity;
- **ECC-W87** user-scope two-stage opt-in;
- **ECC-W88** memory read status projection;
- **ECC-W89** doctor ok vs process exit.

C2 term inventory now runs **ECC-W01–ECC-W89**.

C2 strongest boundaries:
- work item/status/owner/session link are records, not exclusive live execution authority;
- bounded candidate retrieval is not complete remote truth;
- adapter session snapshot, fallback history and SQLite session rows are different persistence contracts;
- inspection itself can create a fallback recording;
- base ref is insufficient as exact worker-input identity when overlays and rendered launchers matter;
- command dispatch, process completion, raw handoff, parsed representation and accepted outcome are distinct;
- created-resource rollback can conflict with preserving newly valuable output;
- keeping a coordination directory does not preserve its prior files;
- empty pane list can represent observation failure, not only no session;
- timestamp-derived stale health is not a heartbeat;
- memory storage/trust/status/scope/target, review/governance and actual consumer use remain distinct;
- structured memory views can retain qualifiers that plain CLI views omit;
- doctor/process success is not a healthy-vault certificate.

**C2-DURABLE-COMPLETE** means U03–U04 contextual transfer is closed at the current source package. It does not close Q04b/c/e, Q05b/c, product runtime integration or ECC source-study.

## 7C. C3 durable checkpoint — U05–U06 learning / evaluation / governance

C3 exact source families:
- U05-A Note07 + U05-A source ledger;
- U05-B Note08 + U05-B source ledger + E04 README/PLAN;
- U06-A Note09 + U06-A source ledger + E05 main README/PLAN;
- U06-B Note10 + U06-B source ledger;
- U06-C Note11 + U06-C source ledger;
- ROUND-U05-A / PUBLICATION-U05-A;
- ROUND-U05-B / PUBLICATION-U05-B;
- ROUND-U06-A / PUBLICATION-U06-A;
- ROUND-U06-B / PUBLICATION-U06-B;
- ROUND-U06-C / PUBLICATION-U06-C;
- u06-a-conversation-record README for the historical dual-E05 evidence identity reconciliation.

C3 evidence lineage preserves **two different historical E05 records**:
- main-path Node `probe.cjs`, 15 cases;
- conversation-bundle Python `probe.py`, 16 cases.
They share target blobs but case IDs/driver/results are not pooled into one larger validation score and are not treated as independent replications merely because drivers differ.

Publication/round files confirm chronology, evidence identity, scope/readback and maintenance failures. They do not upgrade source/local-execution evidence into independent product validation.

C3 source-to-TERMS check added:
- **ECC-L99** location-derived instinct scope;
- **ECC-L100** analyzed set vs archived set;
- **ECC-L101** current version label;
- **ECC-L102** governance host-field adaptation;
- **ECC-L103** governance event correlation identity;
- **ECC-L104** governance data minimization.

C3 term inventory now runs **ECC-L01–ECC-L104**.

C3 strongest boundaries:
- observation capture can exist without analysis;
- analyzer completion marker is an invocation-boundary receipt, not semantic learning validity;
- analyzed observations and archived observations need not be the same set;
- same-ID/multi-project promotion is not semantic agreement or independent evidence;
- generated evolved artifacts and learned-skill discovery paths are distinct;
- SessionStart context can inject compressed instinct action while dropping trigger/evidence/ID;
- skill invocation telemetry, improvement observations and instinct evidence are separate contracts;
- skill health labels are criterion-specific and can produce non-intuitive “healthy/non-declining” views under no-data or constant-failure cases;
- amendment recommendation and success-rate delta are not independent causal efficacy proof;
- version label/snapshot is not a content-bound experiment identity;
- config-protection object-name guard, GateGuard first-touch marker and governance capture are distinct control families;
- first-touch denial does not verify that investigation occurred;
- zero-exit structured deny can still be a host refusal, while internal output composition can conditionally drop that deny representation;
- governance event classification, stderr transport, database persistence, pending standing, resolution and enforced effect are separate transitions;
- capture field/correlation/data-minimization choices constrain what later consumers can infer;
- zero pending rows is not evidence of complete capture/clean system.

**C3-DURABLE-COMPLETE** means U05–U06 contextual transfer is closed at the current source package. It does not close Q06c2, Q07a2/b2/c2, scanner/deployment controls, host efficacy or ECC source-study.

## 8. Explicit open boundary

ECC concepts package **PACKAGE-COMPLETE değildir**.

C1, C2 ve C3 kapandı. Package-wide açık alanlar:
- notes 12–27;
- U07–U12 source ledgers;
- relevant rounds/publication receipts;
- METHOD-REVIEW / QUESTIONS / SOURCE-LEDGER / RESEARCH-LOG full package reconciliation;
- inventory files;
- remaining nested evidence;
- package-wide duplicate/role/source-to-TERMS closure.

## 9. Devam

**Sıradaki concepts work B6-T16-C4:** yalnız U07–U09.

C4 exact scope:
- U07-A material-family accounting / reverse frontier;
- U08-A Plan Canvas / related mechanism family;
- U09-A/A2/A3/B Rust/session/operator/runtime families;
- exact notes/source-ledgers/round/publication and bounded evidence;
- C4-linked term inventory creation or refinement;
- C4 durable checkpoint.

Aynı turda C5'e geçilmez.

ECC source-study'nin U13-A next research işi concepts next değildir. U13-A yapılmaz. B7/B8 shared terminology başlamaz.
