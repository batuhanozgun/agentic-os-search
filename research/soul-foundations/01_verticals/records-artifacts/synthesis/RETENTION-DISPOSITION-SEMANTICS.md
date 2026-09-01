# Records Retention / Appraisal / Disposition — Bounded Synthesis

**Status:** bounded synthesis for focused retention/disposition pass  
**Date:** 2026-09-01  
**Scope:** Records-side retention/appraisal/disposition semantics; not legal advice, authority model, deletion architecture, or SOUL design.

## Research question

What semantic information must a Records model preserve about **whether/how long a persistent information resource should continue to exist, when disposition becomes eligible, what final disposition means, and what history must remain after transfer/removal/destruction**?

---

# 1. Executive result

Retention/disposition is a first-order Records dimension that was under-specified by the first six passes.

The evidence rejects a simple model such as:

```text
record.created_at + retention_years → delete
```

The stronger bounded model is:

> **Disposition is a governed transition over a scoped record population. Its semantics require an applicable appraisal/rule, an eligibility trigger, a retention/transfer condition, any active suspension/override, a final action, and evidence of execution where the profile requires reconstruction/accountability.**

This produces several load-bearing distinctions:

- appraisal/value decision ≠ retention duration;
- temporary ≠ low value / short-lived;
- permanent ≠ very long temporary retention;
- cutoff/eligibility trigger ≠ destruction event;
- due/eligible ≠ executed;
- hold/freeze ≠ change in record truth/currentness;
- transfer/custody change ≠ destruction;
- removal/hiding ≠ irreversible payload destruction;
- payload destruction ≠ deletion of every record about the destruction;
- master/source record retention ≠ automatically identical retention for every copy/backup/index;
- disposition schedule/rule ≠ timeless constant.

The Records-side problem is therefore not merely `deletion`. It is **controlled persistence termination / custody transition with reconstructable applicability and outcome**.

---

# 2. Appraisal and disposition classification

## 2.1 Appraisal answers a different question from retention implementation

ISO/TR 21946 and national archives practice treat appraisal as analysis of context, needs, value and risk to determine which records need to exist and how long they must be kept.

This is compatible with the Requirement Profile method:

- resource/population;
- protected use;
- legal/policy/societal constraints;
- value/risk;
- horizon;
- expected future use

can activate retention/disposition obligations.

## 2.2 `Temporary` does not mean unimportant

NARA explicitly notes that temporary records can need very long retention. `Temporary` means they are eventually authorised for destruction rather than selected for permanent archival preservation.

A temporary record can still be:

- legally critical for decades;
- privacy-sensitive;
- necessary for rights/accountability;
- operationally high value.

Therefore:

> **temporary/permanent is a final-disposition class, not a universal value ranking.**

## 2.3 `Permanent` is not `retention = infinity in the source system`

In NARA's model, permanent records are eventually **transferred** to the National Archives; the originating agency does not simply retain them forever in the same operational location.

Thus distinguish:

- **retention under current custody**;
- **transfer/custody transition**;
- **permanent preservation obligation**.

A long fixed temporary period remains semantically different from permanent archival disposition.

---

# 3. The disposition-rule model

The evidence supports decomposing an applicable disposition rule into semantic parts.

## D1 — Scope / record population

Which records/series/aggregate/versions/representations does the rule govern?

Why required:

- schedules can apply to recurring classes, bounded date ranges or aggregates;
- backups/copies can have separate disposition treatment;
- a new schedule may change item scope;
- destruction of the wrong population is irreversible.

The scope must bind to the identity/granularity model from Pass 2.

---

## D2 — Rule / authority identity and applicability

Which schedule/records authority/policy version governs the record?

Records-side facts can include:

- authority/rule identifier;
- version/date;
- applicability scope;
- effective/supersession relation;
- source/reference.

Who has legitimate authority to create/approve it is deferred.

### Why first-class

NARA warns that older schedules may be superseded and the current applicable disposition authority must be verified before action.

A future reviewer may need to reconstruct:

> `Which disposition rule was applicable when this action occurred?`

Therefore the schedule/profile itself participates in Records history.

---

## D3 — Eligibility trigger / cutoff

What event/condition starts the retention or transfer clock?

Two major families recur:

### Age-based

Examples:
- creation;
- receipt.

### Event-based

Examples:
- case closed;
- project completed;
- audit completed;
- publication;
- settlement;
- superseded;
- obsolete;
- revision/cancellation.

### Relation to Pass 4 time semantics

The trigger is a **typed event/standing fact**, not a generic timestamp.

If the event's domain-effective time can differ from when the system learns it, the profile/rule must identify which temporal semantics control eligibility.

Example:

- policy becomes superseded on 1 June;
- system registers supersession on 10 June;
- rule says retain 7 years after supersession.

A system that stores only `updated_at = 10 June` cannot necessarily reconstruct the intended retention clock.

---

## D4 — Retention / transfer condition

After the trigger, what condition must be satisfied before final action?

Common forms:

- fixed duration;
- fixed duration after event;
- transfer after period;
- minimum retention followed by optional later action;
- maximum retention with earlier permitted disposal under stated conditions;
- event/condition without additional duration (`destroy when superseded/obsolete`) where allowed.

### Important correction

A retention condition is not always a single numeric duration.

It can be a rule over:

`trigger + elapsed time + additional conditions`.

---

## D5 — Final action

What happens when disposition is executed?

Possible source-domain actions include:

- transfer to another custodian/agency;
- transfer for permanent archival preservation;
- destruction/deletion of temporary records;
- authorized donation/other disposition in some regimes.

The Records abstraction should not assume `disposition = delete`.

---

## D6 — Suspension / override / exception state

A normally eligible record can become temporarily non-disposable.

Examples:

- litigation hold;
- audit/investigation hold;
- disposal freeze;
- reappraisal pending;
- temporary retention extension.

### Semantics

A hold/freeze changes:

> **disposition eligibility / permission to execute**

It does not by itself change:

- record content;
- version identity;
- currentness/designation;
- factual correctness;
- ordinary retention rule identity.

When lifted, normal disposition can resume according to the governing rule and any revised authority.

Authority to issue/lift holds remains cross-vertical.

---

## D7 — Execution event / outcome evidence

Eligibility does not prove that the final action occurred.

A disposition execution fact can require:

- target resource/population identity;
- action type;
- occurrence time;
- executing/custody context where applicable;
- governing rule/authority binding;
- outcome/scope;
- destruction/transfer method or certificate where required;
- exception/failure status if execution was incomplete.

NAA explicitly requires documented destruction details including what, when, how and under which records authority.

### Result

Distinguish:

```text
scheduled / governed
→ trigger occurred
→ due / eligible
→ suspended? / permitted?
→ execution attempted
→ completed / failed / partial
```

These are semantic states/events, not a proposed workflow engine.

---

# 4. `Keep everything forever` is not a neutral safe default

The research strongly rejects indefinite retention as a universally conservative choice.

## Failure surfaces

### Security/privacy exposure

Unneeded confidential/personal information remains available for accidental or malicious disclosure.

### Searchability / information overload

NARA explicitly identifies improved searchability as a benefit of disposing of unneeded information.

### Cost / operational burden

Physical/digital preservation/storage/management costs continue.

### Compliance risk

Retention beyond allowed/appropriate periods can itself be problematic.

### Ambiguous currentness

Keeping every representation/version without standing/retention semantics can make retrieval worse, not safer.

### Principle

> **Preservation and disposition are dual Records obligations. Correct persistence includes knowing when continued persistence is no longer justified or permitted.**

This does not imply aggressive deletion. It means `retain forever` must itself be justified by the profile/authority rather than treated as absence of a decision.

---

# 5. Fixed vs event-based vs flexible retention

## 5.1 Fixed/age-based retention

Useful where creation/receipt is a reliable starting event and business/legal need is predictable.

Strength:
- simple and automatable.

Risk:
- can under/over-retain when active use or legal value depends on later events.

## 5.2 Event-based retention

Useful where the relevant lifecycle meaning is tied to:

- completion;
- closure;
- settlement;
- supersession;
- obsolescence;
- termination of a relationship.

Strength:
- aligns persistence with semantic lifecycle.

Risk:
- event may be missing/ambiguous/late-recorded;
- event scope can vary across an aggregate;
- automation fails if trigger semantics are underspecified.

## 5.3 Flexible retention bands

Examples can include:

- minimum period with longer retention allowed;
- maximum period with earlier destruction permitted if business need ends.

### Records-side requirement

Flexible retention needs explicit semantics for:

- hard minimum/maximum if any;
- optionality condition;
- additional risk/rights constraints;
- rationale when retention is extended/shortened where required;
- applicable authority.

A vague `until no longer needed` rule is especially dangerous because it hides who/what evaluates need and creates inconsistent outcomes.

The decision authority itself remains deferred, but the result/rationale can be a record.

---

# 6. Supersession/currentness and retention are related but not identical

Pass 4 established that supersession is a standing relation: another resource/version becomes preferred/effective for a role.

Retention research shows supersession can also be an **eligibility trigger**.

Therefore one fact can participate in two semantic contexts:

```text
policy B supersedes policy A
        │
        ├─ standing effect: A no longer current for role X
        └─ retention effect: start A's retention clock
```

Do not collapse them into one state.

A superseded resource may remain legally/historically required for years or permanently.

---

# 7. Copies, versions, backups and representations

## 7.1 Same logical source does not imply identical disposition rule for every copy

NARA backup guidance provides a clear counterexample:

- backup copies of permanent source records can themselves be temporary;
- backup replacement/transfer events can govern backup deletion;
- source records with unique information not captured in a conversion remain independently scheduled.

### Principle

Retention/disposition should follow the **record function / preservation obligation / unique information / dependency role** of each representation/copy, not blind byte identity.

## 7.2 But destruction scope must be explicit

NAA guidance for cloud information expects contracts to ensure all required copies are destroyed.

These facts reconcile if we distinguish:

- copies that are within the same destruction obligation/scope;
- copies/backups that are distinct managed records with their own governing schedule;
- residual control metadata that is intentionally retained.

### Rule

> A destruction instruction must define the **population/representation scope whose continued recoverability is meant to end**, while excluding separately governed records or required residual evidence.

## 7.3 Derived views / indexes / caches

Pass 5 established that derived views have independent lifecycle roles.

When the source payload is disposed, a derived structure must be evaluated by its own profile:

- Does it contain reconstructable/full content?
- Is it merely a pointer/index entry?
- Is it itself a record?
- Does retaining it defeat the intended destruction/privacy outcome?
- Is a residual tombstone/identifier required?

There is no universal `delete every index entry` rule, but silent retained replicas are a failure if destruction was intended to terminate recoverability.

---

# 8. Payload destruction and residual history

## 8.1 Destruction is not the same as erasing every trace

NAA requires destruction/disposal documentation and notes master control records about destroyed information can themselves be retained as archives.

A Records system may therefore need to preserve after payload destruction:

- resource/record identifier;
- description/class sufficient to know what was disposed;
- governing disposition authority/rule;
- disposal/destruction event time;
- action/method/outcome;
- scope/quantity where required;
- hold/exception history if material.

## 8.2 Residual history is itself subject to appraisal

The evidence does **not** support `tombstones/destruction certificates must live forever` universally.

Residual disposition evidence is another record/resource with its own:

- protected uses;
- retention/appraisal requirements;
- rights/privacy constraints;
- eventual disposition.

### Principle

> **Payload terminality and metadata/history terminality are independent decisions.**

---

# 9. Destruction semantics

A robust Records-side destruction claim must be scoped.

Possible meanings include:

- removed from current access;
- logical delete/tombstone;
- source representation deleted but replicas/backups remain;
- cryptographic/key destruction makes content inaccessible;
- all in-scope recoverable copies irreversibly destroyed;
- custody transferred and local operational copy deleted;
- metadata/history retained while payload is gone.

This pass does not choose a deletion mechanism.

### Requirement-profile rule

If a profile needs `destruction`, it must define the required **observable terminal outcome**, for example:

> the payload must no longer be recoverable from the systems/copies within disposition scope, while the specified disposition evidence remains retrievable.

The implementation may use different mechanisms and needs later verification.

---

# 10. Transfer is a lifecycle transition, not destruction

For permanent records, transfer changes custody/preservation responsibility while preserving the information.

Records-side transfer semantics can require:

- source/resource identity continuity;
- transferred version/representation scope;
- transfer date/custody history;
- receiving context;
- preservation/rights/metadata package;
- verification that transferred information is complete/usable;
- local-copy disposition if separately governed.

This connects Pass 3 transfer/portability closure with retention/disposition.

Do not infer that the originating copy must instantly disappear merely because custody transfers; source-copy treatment is separately governed.

---

# 11. Schedule/rule evolution and historical reconstruction

Schedules and policies change.

NARA notes:

- newer disposition authority can supersede older authority;
- schedules may need revision when record function/scope/format or retention/disposition changes;
- current authority should be verified before execution.

Therefore a Records model that only stores:

`current_retention_policy_id`

can lose historical compliance/reconstruction context.

The requirement profile may need:

- policy/schedule identity/version;
- applicability/effective range;
- supersession relation;
- record-population binding;
- rule that actually governed an execution event.

This reuses Pass 4 effective/system-known historical semantics.

---

# 12. Architecture-neutral retention/disposition model

```text
PROFILE / APPRAISAL CONTEXT
  protected uses + value/risk + external mandates
                ↓

DISPOSITION RULE
  scope / population
  rule identity + version + applicability
  disposition class / intended final action
  cutoff / eligibility trigger
  retention / transfer condition
                ↓

CURRENT ELIGIBILITY STATE
  trigger known/effective?
  elapsed/conditions satisfied?
  hold/freeze/extension active?
                ↓

DISPOSITION EXECUTION
  transfer | destruction | other governed action
  occurrence + outcome + scope
                ↓

RESIDUAL RECORDS
  execution evidence / tombstone / custody history
  each with its own requirement profile / retention
```

This is a semantic model, not an implementation workflow.

---

# 13. Integration with Records Requirement Profile

The Requirement Profile method should treat retention/disposition as a first-order obligation family rather than a final implementation detail.

For a resource/population, derive when applicable:

1. **governing baseline/authority** — required floor/constraint;
2. **disposition class/outcome** — temporary destruction, permanent transfer, etc.;
3. **eligibility trigger and time semantics**;
4. **minimum/maximum/flexible retention conditions**;
5. **hold/freeze/exception requirements**;
6. **copy/version/derived-view scope**;
7. **transfer/destruction acceptance outcome**;
8. **residual history requirement**;
9. **rule/profile review triggers**.

A profile can legitimately say `no terminal disposition requirement inside current horizon` where that is justified, but this is different from silently assuming indefinite retention.

---

# 14. Scenario tests

## S1 — Short-lived sensitive transaction records

Need:
- event/age-based short retention;
- confidential destruction;
- accountable destruction evidence;
- possible hold override.

Result:
- retention/disposition highly active despite short horizon;
- `keep forever` directly worsens privacy/security risk.

## S2 — Long-lived temporary legal-rights record

Need:
- very long fixed/event-based retention;
- reliable trigger;
- hold support;
- eventual destruction.

Result:
- long duration does not convert temporary disposition into permanent archival disposition.

## S3 — Permanent archival policy records

Need:
- retain under current custody until transfer trigger/period;
- transfer to archive;
- preserve lineage/metadata/rights;
- possibly dispose local working copies separately.

Result:
- final disposition is custody transfer, not payload destruction.

## S4 — Superseded operational policy

Need:
- supersession ends current standing;
- same supersession event may start retention period;
- historical/as-of retrieval remains required during retention.

Result:
- currentness and retention share an event but remain different semantics.

## S5 — Cloud-hosted record with backups

Need:
- destruction outcome covers all in-scope recoverable copies under contract;
- backups that are separately governed must follow their own schedule;
- destruction evidence survives if required.

Result:
- `delete primary object` is insufficient as a destruction claim.

## S6 — Record under litigation/investigation hold

Need:
- original schedule remains known;
- disposition eligibility suspended;
- hold scope/effective state historically recoverable;
- after lift, disposition calculation resumes/reappraises as applicable.

Result:
- hold is an override, not a new factual/currentness state of the record.

---

# 15. What the pass falsified

## `Retention = number of years`

Rejected. Retention may be event-based, age-based, conditional or flexible and needs final-action semantics.

## `Permanent = very long retention`

Rejected. Permanent is an archival/final-disposition category involving transfer/preservation.

## `Disposition = delete`

Rejected. Transfer is a disposition action; temporary disposal/destruction is another.

## `Eligible = destroyed`

Rejected. Eligibility, suspension/hold and execution/outcome are separate.

## `Superseded = destroy now`

Rejected. Supersession can be a retention trigger while the resource remains required for historical/legal use.

## `Same bytes/copy = same retention`

Rejected. Backup/convenience/converted copies can have different record roles and schedules.

## `Delete primary = record destroyed`

Rejected when in-scope recoverable copies/replicas remain.

## `Destruction means no metadata can remain`

Rejected. Destruction evidence can be required and separately retained.

## `Retention schedule is timeless`

Rejected. Authorities/rules are versioned/applicability-bound and can be superseded/frozen/reappraised.

---

# 16. Remaining boundary questions

## U1 — Physical execution completeness across distributed replicas/backups

Semantics are clear enough to say what `in-scope irrecoverable destruction` means, but verifying it across distributed/cloud/backup systems is an implementation-assurance/security problem.

## U2 — Cryptographic erasure

Key destruction can make encrypted payload inaccessible while ciphertext persists. Whether this satisfies a particular destruction obligation is legal/security/profile specific and requires later implementation verification.

## U3 — Residual metadata minimisation

Which destruction evidence must survive and for how long remains profile/appraisal specific; no universal tombstone duration exists.

## U4 — Authority and legal holds

Who establishes schedules, declares holds, accepts exceptions or authorises destruction is cross-vertical governance/Actor/Work scope.

---

# 17. Pass result for vertical completeness

Retention/appraisal/disposition is confirmed as a **first-order Records semantic dimension** and is now sufficiently covered at the current foundational level.

The remaining hard questions are mostly:

- profile-specific appraisal/calibration;
- authority/governance;
- implementation assurance of destruction/replicas/security;
- concrete mechanism verification.

This result should now feed back into the vertical completeness review.

---

# 18. Return-condition status

1. retention/disposition components source-grounded: **met**;
2. temporary/permanent/transfer/destruction explicit: **met**;
3. trigger/time reconciled with Pass 4: **met**;
4. residual history and multi-representation cases tested: **met**;
5. hold/freeze/flexible retention addressed: **met**;
6. Requirement Profile integration explicit: **met**;
7. adversarial counter-check: **pending companion file**;
8. source trace persisted: **met**;
9. ready to return to completeness review after counter-check: **yes**.