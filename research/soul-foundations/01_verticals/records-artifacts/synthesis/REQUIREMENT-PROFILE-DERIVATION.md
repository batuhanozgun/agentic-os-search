# Records Requirement Profile / Derivation — Bounded Synthesis

**Status:** bounded synthesis for approved requirement-derivation pass  
**Date:** 2026-09-01  
**Scope:** Records / persistent-information semantics and requirements only; not a storage/search/SOUL architecture.

## Research question

Given a specified persistent-information resource and intended future use, how can we derive the **smallest defensible set of Records-side obligations** that must hold — without turning the first five passes into a universal checklist or letting implementation technology determine the requirements?

---

# 1. Executive result

The evidence does not support a static universal `Records profile` selected once by record type.

The stronger result is:

> **Records requirements should be derived through recurrent, context-bound appraisal. A profile is best understood as a dated, evidence-backed snapshot/contract of that appraisal — not as a permanent taxonomy or a metadata template.**

Across ISO appraisal/records-management standards, NARA, NAA, OAIS/IPELTU and PREMIS, requirements vary with combinations of:

- intended use / business and future-use needs;
- resource class and identity granularity;
- value, consequence and risk;
- legal/policy/societal/security constraints;
- retention horizon and expected environmental change;
- expected transformations and transfers;
- users/stakeholders / Designated Community and assumed knowledge;
- required trust, findability, history and reconstruction outcomes.

The same Records obligation may be satisfied through different mechanisms. Therefore four questions must remain separate:

1. **Is this obligation required?**
2. **How strong/deep must it be?**
3. **Where/how may it be satisfied?**
4. **How will sufficiency be verified?**

Collapsing these questions recreates the earlier failures:

- `mandatory = metadata field`;
- `high risk = maximum everything`;
- `long horizon = more fields`;
- `requirement = product feature`.

---

# 2. Direction correction — `profile` is a snapshot, not the stable abstraction

## Evidence

- ISO 15489 includes **recurrent** analysis of business context and identification of records requirements.
- ISO/TR 21946 describes appraisal through scope, business/function context, requirements and risk, and explicitly treats appraisal as recurrent as context/risk changes.
- NAA's fit-for-purpose approach varies by business need, information type, value, stakeholder and sensitivity.
- OAIS allows Designated Community, Knowledge Base and Preservation Objectives to change over time.
- IPELTU captures/refines Additional Information across project phases rather than treating initial metadata assumptions as final.

## Result

A static profile can still be useful as an operational artefact, but the stable semantic concept is:

> **Recurrent Records requirement appraisal → current requirement profile/contract.**

A profile must therefore carry at least:

- scope/resource population;
- assumptions/context;
- protected uses/outcomes;
- active obligations and their rationale;
- satisfaction/verification state;
- residual risk/unknowns;
- review triggers and date/version.

This does not make the profile a Work workflow. It only preserves enough Records-side requirement state to know what assumptions its requirements depend on.

---

# 3. The derivation input model

The pass tested the pre-pass inputs. The strongest bounded input model is below.

## I1 — Resource / identity boundary

Before requirements can be derived, specify what is being profiled:

- individual persistent resource;
- version family;
- representation/instantiation;
- aggregate/case/thread;
- dataset release;
- derived information object;
- system-held record population.

### Why load-bearing

A requirement attached to the wrong granularity can be meaningless. A checksum may describe a file representation while a currentness requirement concerns a version family; an aggregation reconstruction requirement concerns a set/order rather than each member in isolation.

### Prior-pass dependency

Pass 2 already established resource ≠ version ≠ representation/instance and aggregation/derivation boundaries.

---

## I2 — Protected use / outcome

Ask what the information must later support.

Examples:

- known-item operational lookup;
- business continuation;
- current-designation lookup;
- historical/as-of reconstruction;
- audit/accountability;
- citation/reference;
- evidential use;
- semantic/exhaustive discovery;
- migration/re-instantiation;
- independent long-term reuse;
- transfer to another system/archive.

### Why load-bearing

The same object may need different closure depending on intended future use. DataCite-style citation, NARA transfer, operational use and OAIS independent long-term understanding do not protect identical outcomes.

### Rule

A requirement is not `minimum` merely because it is useful. Its absence must threaten a protected use or an external obligation.

---

## I3 — Retrieval / reconstruction contract

Specify which questions must be answerable, not just `must be searchable`.

Possible needs from Pass 5:

- exact known-item;
- filter/query;
- semantic/topical discovery;
- exhaustive/high-recall search;
- current standing;
- domain-effective as-of;
- system-known as-of;
- provenance/derivation traversal;
- aggregate/case/thread reconstruction.

### Why separate from I2

Two systems can support the same business purpose but require different retrieval guarantees. `Reference this object by ID` is much cheaper semantically than `prove no responsive record exists in the covered population as of T`.

---

## I4 — Horizon / expected environmental change

Specify the time horizon and what surrounding knowledge/infrastructure may cease to be safely assumed.

Examples:

- session/short operational;
- project/medium-term;
- organisational/regulated;
- archival/indefinite.

But horizon alone is not a score.

### Why load-bearing

Long horizons make implicit software, vocabularies, team knowledge and registries less reliable. OAIS explicitly frames long term around changing technology and changing Designated Community knowledge.

---

## I5 — Value / consequence / risk profile

Specify material consequences if identity, integrity, availability, history, confidentiality or interpretability fails.

### Important correction

Do **not** collapse this to one number.

At minimum, independent consequence dimensions can include:

- loss/unavailability;
- misidentification / wrong version;
- undetected alteration;
- loss of context/provenance;
- disclosure / rights violation;
- incorrect currentness/standing;
- inability to reconstruct history;
- inability to transfer/reuse.

A low-value short-lived record can still have a high confidentiality consequence. NAA's Protective Marking exception directly demonstrates this nonlinearity.

---

## I6 — External constraints

Capture applicable legal, regulatory, contractual, policy, archival, security, privacy or societal obligations.

### Why separate from generic risk

Some requirements are mandatory because an external authority says so even if local probability/consequence scoring is low.

NARA permanent transfer/classified-record requirements and NAA security requirements provide concrete examples.

### Vertical boundary

Records can preserve the existence/content/applicability of these constraints. Which Actor creates/approves/enforces them remains deferred.

---

## I7 — Change / standing characteristics

Does the resource:

- evolve through versions;
- have current/superseded standing;
- receive corrections/retractions;
- have delayed effective vs system-known times;
- branch;
- move between availability/preservation states?

### Why load-bearing

If none of these can happen for the protected use, rich temporal/status closure may be unnecessary. If they can, one timestamp/current snapshot is insufficient.

---

## I8 — Transformation / migration / transfer exposure

Will the information be:

- format migrated;
- normalized;
- exported/imported;
- moved between custody/system boundaries;
- summarized/derived;
- re-instantiated;
- expected to survive software obsolescence?

### Why load-bearing

Transformations activate significant-property, provenance, validation, version/representation identity and portability requirements.

OAIS/IPELTU/PREMIS strongly support this dimension.

---

## I9 — Dependency / aggregation structure

Does meaning/reconstruction depend on:

- other files/components;
- schemas/vocabularies;
- related records;
- order/membership;
- provenance graph;
- external registry;
- algorithm/software/environment;
- inherited system context?

### Why load-bearing

Standalone objects and multi-component/derived resources have materially different closure.

---

## I10 — Target users / knowledge baseline / interoperability boundary

Who must be able to use/understand the information, and what can safely be assumed they already know or can resolve?

Examples:

- same live application/team;
- another team in the organisation;
- another agency/system;
- public consumers;
- a future Designated Community.

### Why load-bearing

Local sufficiency and portable/independent sufficiency are different. PREMIS and OAIS both allow knowledge to exist outside the object, but exchange/long-term use may require explicit materialisation or durable reference.

---

# 4. What did NOT survive as an independent top-level input

## `Record type` alone

Insufficient. The same nominal type can differ in sensitivity, horizon, use, transformation and retrieval needs.

## `Retention period` alone

Insufficient. Short-lived sensitive information can require stronger controls than long-lived public information on some dimensions.

## `Risk score`

Rejected as the sole derivation mechanism. Independent consequences can activate different obligations and are not safely ordered on one scalar.

## `Metadata richness`

Not an input to requirements. It is at most an observed implementation state to compare against derived obligations.

## `Storage technology`

Explicitly not a derivation input. Technology may constrain implementation later but must not silently define the requirement.

---

# 5. The architecture-neutral derivation method

The pass supports the following recurrent method.

## Step 0 — Bind the appraisal target

State:

- profiled resource/population;
- identity/granularity level;
- current scope boundaries;
- date/version of appraisal.

**Failure prevented:** applying a requirement to the wrong resource/version/representation/aggregate.

---

## Step 1 — State protected uses and external obligations

List:

- future/business uses that must remain possible;
- required retrieval/reconstruction questions;
- legal/policy/security/archival constraints that apply.

For each, state the consequence if it fails.

**Rule:** do not derive requirements from vague goals such as `keep usable` when a more testable outcome can be named.

---

## Step 2 — Characterise the resource dynamics and environment

Record only dimensions that can change requirements:

- resource class/structure;
- change/standing behaviour;
- dependencies/aggregation;
- transformations/transfers;
- horizon/environmental assumptions;
- target user/knowledge baseline;
- consequence/risk dimensions.

---

## Step 3 — Map failure threats to Records obligation families

Use the prior-pass failure inventory and working model.

Candidate families:

### R1 Referential identity / exact binding
Required when mis-binding or ambiguity can break protected use.

### R2 Interpretability / representation closure
Required to the depth needed for the target user/environment to interpret the resource.

### R3 Provenance / context / origin closure
Required to the depth needed for trust, derivation, accountability or interpretation.

### R4 Change / temporal / standing reconstructability
Required when version/currentness/history/as-of questions matter.

### R5 Integrity / continuity assurance
Required to the level justified by corruption/tampering/misidentification consequence and horizon.

### R6 Relation / aggregation / dependency closure
Required where isolated items are insufficient for reconstruction/meaning.

### R7 Rights / access / use-constraint information
Required where constraints materially affect legitimate preservation/access/use.

### R8 Organisation / descriptive/access-view semantics
Required when context or discovery depends on maintained organisational/derived views.

### R9 Retrieval sufficiency / coverage-freshness contract
Required to the strength of the retrieval claims the profile must support.

### R10 Retention/disposition boundary information
Required where later users must know retention class/status, transfer/destruction event or residual identity/history.

### R11 Transfer / portability / external-dependency survivability
Required when the resource must cross system/custody boundaries or survive external dependency loss.

### R12 Preservation objective / significant-property criteria
Required when transformation/long-term preservation must establish what counts as successful continuity.

These are candidate obligation families, not universal components. A valid profile can legitimately mark some `not required for stated use`.

---

## Step 4 — Apply the necessity test

An obligation is **Required** in the current profile if at least one of these holds:

1. **Protected-use dependency:** without it, a named required use/reconstruction capability can materially fail.
2. **External mandate:** an applicable authoritative requirement demands it.
3. **Dependency closure:** another Required obligation cannot be satisfied durably without it.

An obligation is **Not required for this profile** when:

- no protected use or applicable external requirement depends on it;
- its absence does not create a distinct material failure under the current assumptions;
- and it is not needed to satisfy another Required obligation.

**Unknown / unresolved** must remain a first-class state when evidence is insufficient. Do not silently convert uncertainty into `not required`.

---

## Step 5 — Choose a valid satisfaction mode separately

A Required obligation may be satisfied by:

- intrinsic/object-local information;
- externally linked information/registry;
- relation/provenance structure;
- inherited aggregate/system context;
- preserved policy/business rule;
- deterministic reconstruction from preserved inputs/rules;
- system/control capability rather than descriptive metadata.

### Safety condition

External/inherited/reconstructable satisfaction is valid only if its dependency remains:

- exactly bound;
- version-correct;
- resolvable/reconstructable;
- interpretable;
- sufficiently available for the stated horizon/use;
- portable/materialisable when required by transfer.

This separation is directly consistent with PREMIS's semantic-unit vs metadata-element distinction and NAA's system/governance alternatives.

---

## Step 6 — Set depth/assurance, not just yes/no

Many obligations are required in purpose but variable in depth.

Examples:

- identity: local scoped ID vs cross-system persistent ID + historical mappings;
- provenance: `creator unknown` may suffice for one use; full derivation/custody chain for another;
- integrity: repository-level assurance may suffice for low-risk use; explicit fixity/signature/audit history for higher risk;
- retrieval: known-item lookup vs exhaustive/absence-supporting search;
- interpretation: current shared format knowledge vs full representation-information network;
- history: current version only vs bitemporal/as-of reconstruction.

**Rule:** depth should be justified by protected use, consequence and environmental uncertainty rather than one generic maturity level.

---

## Step 7 — Define acceptance / falsification tests

A profile is incomplete if it merely lists controls.

For each Required obligation, define at least one test such as:

- Can exact requested resource/version/representation be identified?
- Can target users interpret it without unavailable tacit knowledge?
- Can a derived output be traced to exact source versions?
- Can current and required historical/as-of standing be reconstructed?
- Can corruption/material transformation be detected to required assurance?
- Can aggregate membership/order be reconstructed?
- Can retrieval return the required population with the promised coverage/freshness?
- Can transfer to a target environment preserve required dependencies?
- Can the system prove the payload was destroyed while retaining required disposition history?

The exact verification mechanism is later design work, but the expected observable outcome belongs in the requirement profile.

---

## Step 8 — Record residual risk and review triggers

A profile must identify what would make it stale.

Minimum trigger families exposed by sources:

- business/use requirement changes;
- legal/policy/security constraint changes;
- retention/value/risk reassessment;
- new stakeholder/Designated Community or changed Knowledge Base;
- new required retrieval mode or stronger recall/currentness claim;
- new transformation/migration/export/decommissioning plan;
- format/software/dependency obsolescence;
- new resource types/aggregations or identity granularity;
- discovered failure/incident/gap;
- change in system/custody/interoperability boundary.

The trigger causes **re-appraisal**, not automatic requirement escalation.

---

# 6. Requirement-profile output structure

A bounded Records Requirement Profile can therefore be represented conceptually as:

```text
PROFILE CONTEXT
  scope / resource identity
  protected uses + retrieval/reconstruction questions
  external obligations
  horizon / target users / knowledge assumptions
  risk-consequence dimensions
  change / transformation / dependency context

OBLIGATION MATRIX
  obligation family
  necessity: REQUIRED | NOT REQUIRED | UNKNOWN
  rationale / failure prevented / mandate
  required depth / assurance
  satisfaction mode + dependency
  acceptance/falsification test

REVIEW CONTRACT
  residual risks / unresolved assumptions
  triggers for re-appraisal
  profile date/version
```

This is a research structure, not a SOUL schema.

---

# 7. Scenario falsification

The method was run against materially different scenarios to test whether it merely produces `everything required`.

## S1 — Short-lived internal immutable operational note

Assumptions:
- known-item lookup only;
- same live team/application;
- short horizon;
- low consequence;
- no external transfer;
- no versions, derivation or special rights.

Derived result:
- **Required:** R1 identity/binding; minimal R2 interpretability; enough R3 context to know what the note is; R9 known-item retrieval path.
- **Potentially not required:** rich history R4; explicit per-object fixity R5; complex aggregation R6; rights metadata R7; transfer R11; significant properties R12.

Falsification value:
- proves the method does not automatically activate every prior-pass obligation.

---

## S2 — High-volume, short-lived but sensitive transaction records

Assumptions:
- short horizon;
- low/medium long-term value;
- strong confidentiality consequence;
- structured retrieval and accountable deletion needed.

Derived result:
- baseline R1/R2/R3/R9;
- **R7 rights/security constraint information becomes Required despite short horizon**;
- R10 disposition boundary becomes Required if accountable destruction must be shown;
- stronger R5 continuity/access-control assurance may be required by consequence;
- long-term representation network R2 depth may remain low.

Falsification value:
- rejects `longer horizon = stronger everything` and one scalar value score.

---

## S3 — Long-lived policy with supersession/current-standing use

Assumptions:
- users need both current policy and policy-as-of past date;
- revisions/supersession occur;
- public/organizational access;
- medium/long horizon.

Derived result:
- R1 exact family/version binding;
- R3 origin/context;
- **R4 change/effective/system-known/currentness history strongly Required**;
- R8 organisation/access views;
- **R9 current-standing + historical/as-of retrieval contract**;
- R5 integrity appropriate to consequence/horizon;
- R11 if migrated/decommissioned;
- R12 if format transformations must preserve legally/materially significant properties.

Falsification value:
- shows versioning is not sufficient unless standing and as-of semantics are requirements.

---

## S4 — Derived analytical report used for audit/reproducibility

Assumptions:
- report derives from datasets and processing;
- medium horizon;
- later reviewer must trace source versions and transformation;
- report itself may be a record.

Derived result:
- R1 report + exact source-version binding;
- **R3 derivation provenance depth elevated**;
- R4 version/change history if sources/report evolve;
- **R6 derivation relations Required**;
- R9 provenance traversal and exact retrieval;
- R11 if external dependencies/processing artefacts live elsewhere;
- R12 required when validation depends on preserved significant inputs/processing semantics.

Falsification value:
- a rich Title/Description cannot substitute for source-version/derivation requirements.

---

## S5 — Multi-file scientific dataset for independent archival reuse

Assumptions:
- long/indefinite horizon;
- future Designated Community may differ from creators;
- multi-file structure/schema/units/software dependencies;
- transfer to archive;
- broad discovery and independent interpretation.

Derived result:
- R1 strong persistent identity/binding;
- **R2 deep representation/interpretation closure**;
- R3 rich provenance/context;
- R5 long-term integrity/continuity evidence;
- **R6 aggregation/dependency closure**;
- R7 rights where applicable;
- R8/R9 descriptive discovery + retrieval;
- **R11 transfer/dependency survivability**;
- **R12 preservation objectives/significant properties**;
- R4 only to the change/history depth relevant to releases/transformations.

Falsification value:
- demonstrates why OAIS-like obligations are not wrong, but are inappropriate as the universal baseline for S1/S2.

---

## S6 — Stable public reference publication with no need for provenance-sensitive audit

Assumptions:
- long-ish horizon;
- public known-item/semantic discovery;
- stable widely interpretable format;
- provenance detail beyond publisher/source not important to stated use;
- no restricted access.

Derived result:
- R1/R2/R9 Required;
- descriptive R8 useful/Required for semantic discovery;
- R3 only shallow provenance/context;
- R7 not required if genuinely unrestricted and ambiguity around rights is not material;
- R4 modest if no version/currentness problem;
- R5 depth proportionate to preservation expectation.

Falsification value:
- `long-lived` does not itself imply detailed provenance, rights workflow or rich temporal history.

---

# 8. What the method falsified

## `Every prior-pass distinction becomes a requirement`

Rejected.

Prior passes define failure/semantic dimensions. Profiles activate only the dimensions needed for their protected use/mandates.

## `Requirement profile = metadata profile`

Rejected.

Requirements can be satisfied by metadata, relations, external registries, preserved rules, procedures/controls or reconstruction.

## `High risk = maximum controls on every dimension`

Rejected.

Risk/consequence is multidimensional. Confidentiality can be high while long-term interpretation need is low; preservation can be high while confidentiality is nil.

## `One Must/Should list is enough`

Rejected as universal derivation logic.

NARA's Must/Should baseline is useful, but NARA itself describes tailoring final system requirements. Context-specific `Required/Not Required/Unknown + rationale/depth` is more suitable for this research layer.

## `Profile can be permanent once approved`

Rejected.

ISO appraisal, OAIS community/objective change, IPELTU lifecycle refinement and NAA system/risk review all support recurrence.

## `Long-term archive requirements should govern all Records`

Rejected.

OAIS/IPELTU are powerful for long-term scenarios, but operational records can safely inherit more context and need less preservation closure.

## `Storage/search capability proves requirement satisfaction`

Rejected.

A search engine can exist without coverage/currentness guarantees; version storage can exist without standing semantics; checksum can exist without correct identity binding.

---

# 9. Admissible requirement states

A binary `required/not required` is insufficient during research/assessment.

The profile should permit:

- **REQUIRED** — justified by protected use, mandate, or dependency closure;
- **NOT REQUIRED FOR CURRENT PROFILE** — explicit bounded exclusion under stated assumptions;
- **UNKNOWN / NEEDS EVIDENCE** — requirement decision cannot yet be justified.

A separate satisfaction state can record:

- satisfied intrinsic;
- satisfied external/linked;
- satisfied inherited/system-level;
- satisfied reconstructably;
- partially satisfied;
- unsatisfied;
- not yet verified.

This prevents `not implemented` from being mistaken for `not required`, and `required` from being mistaken for `must be an object field`.

---

# 10. Acceptance discipline

A derived profile is not validated merely because every box has an answer.

Minimum validity conditions:

1. **Scope-bound:** exact resource/population/granularity is stated.
2. **Use-bound:** protected future uses/retrieval claims are stated.
3. **Constraint-bound:** external obligations and assumptions are explicit.
4. **Failure-linked:** every Required obligation states the material failure/mandate it addresses.
5. **Mechanism-independent:** requirement is not merely a preferred implementation.
6. **Satisfaction-traceable:** claimed external/inherited/reconstructed satisfaction has a durable binding/dependency story.
7. **Testable:** acceptance/falsification outcome is defined.
8. **Residual uncertainty explicit:** unknowns are not silently downgraded.
9. **Reviewable:** triggers/date/version exist.

A profile that cannot meet these conditions is a requirements opinion, not a sufficiently grounded Records requirement contract.

---

# 11. Relationship to architecture

This pass deliberately stops before mechanism selection.

The derived profile can later be used to evaluate competing mechanism families such as:

- current-state stores;
- multiversion stores;
- immutable/versioned object stores;
- content-addressed graphs;
- event/history logs;
- relational/document stores;
- archival packages;
- relationship graphs;
- search/semantic indexes.

But no one mechanism should be evaluated without a profile, because the same mechanism can be excellent for one requirement contract and inadequate for another.

Therefore:

> **requirements profile is an evaluation input to mechanism comparison, not an architecture output.**

---

# 12. Residual uncertainties

## U1 — Profile derivation granularity

When should one profile cover an entire record class/population versus individual resource/version/aggregate subclasses?

Too broad causes universal-schema failure; too narrow creates unmanageable profile explosion.

## U2 — Identity/significant-property threshold

The method can require `preserve identity across transformation according to significant properties`, but the exact threshold for same representation vs new version vs new derived resource remains domain/purpose dependent.

## U3 — Assurance calibration

The method identifies dimensions whose depth should rise with consequence/risk/horizon, but it does not yet provide domain-independent assurance levels.

## U4 — External dependency operational criteria

Binding/survivability requirements are clear conceptually; exact operational thresholds for acceptable dependency risk remain profile/domain specific.

## U5 — Authority ownership

Who approves a profile, sets legal/business obligations or accepts residual risk belongs to Actors/Work/governance synthesis. Records can preserve the profile/rationale/approval record but cannot assign authority from this vertical.

---

# 13. Highest-information next Records direction

The first six passes now provide:

1. object/recordhood boundaries;
2. preservation closure;
3. change/status/time semantics;
4. organisation/retrieval semantics;
5. a method for deriving context-specific Records requirements.

This materially changes the next-step frontier.

The strongest next Records question is now:

> **How do major persistence/history/organisation/retrieval mechanism families satisfy or fail different Records requirement profiles — and which trade-offs/failure modes are intrinsic to each pattern before any SOUL architecture is selected?**

This would compare mechanism families against derived profiles rather than choose technology by familiarity.

Competing unresolved conceptual questions (identity/significant-property thresholds, neutral umbrella category) remain open, but they no longer block a bounded pattern-comparison pass because a profile can state its identity assumptions explicitly.

This is next logical work, not a SOUL architecture decision.

---

# 14. Return-condition review

1. Candidate derivation inputs tested across independent authoritative lenses: **met**.
2. Architecture-neutral derivation method exists: **met**.
3. Requirement purpose separated from implementation/storage/metadata: **met**.
4. Inclusion/exclusion rules explicit and scenario-falsified: **met**.
5. Materially different scenarios tested: **met**.
6. Adverse pass still required separately before final return: **pending companion counter-check**.
7. Recurrence/re-appraisal triggers explicit: **met**.
8. Source trace persisted: **met**.
9. Next direction re-derived: **met provisionally — mechanism-pattern comparison**.

Pass is ready for adversarial counter-check before repository state is closed.