# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-20, **B6-T16-C1 / C1-DURABLE-COMPLETE / PACKAGE-PARTIAL**.

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
- C2/C3 main mechanism notes and source-ledgers were already full-read in the interrupted large turn, but their own round/publication/history reconciliation is still open.
- Three linked term files exist; only SURFACES-INSTALLATION is closed.
- exact next: **C2 closure only**. C3'e aynı turda geçilmez.

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

## 8. Explicit open boundary

ECC concepts package **PACKAGE-COMPLETE değildir**.

C1 kapandı. C2/C3 mechanism/source-ledger okumaları ilerledi fakat kendi closure'ları henüz yok. Package-wide açık alanlar:
- notes 12–27;
- U07–U12 source ledgers;
- relevant rounds/publication receipts;
- METHOD-REVIEW / QUESTIONS / SOURCE-LEDGER / RESEARCH-LOG full package reconciliation;
- inventory files;
- remaining nested evidence;
- package-wide duplicate/role/source-to-TERMS closure.

## 9. Devam

**Sıradaki concepts work B6-T16-C2:** yalnız U03–U04 closure.

C2 exact scope:
- U03-A/U03-B/U04-A ROUND/publication/history reconciliation;
- E02/E03 role/readback reconciliation;
- TERMS-WORK-EXECUTION-MEMORY source-to-record coverage check;
- C2 durable checkpoint.

Aynı turda C3'e geçilmez.

ECC source-study'nin U13-A next research işi concepts next değildir. U13-A yapılmaz. B7/B8 shared terminology başlamaz.
