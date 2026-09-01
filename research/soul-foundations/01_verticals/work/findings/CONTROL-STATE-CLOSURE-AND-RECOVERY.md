# Work — Control, State, Closure and Recovery

**Status:** substantive findings; current interpretation is consolidated in the vertical synthesis

## Question

What semantic distinctions are hidden when Work is treated as a scalar status moving from `todo` to `done`?

## 1. Lifecycle state is richer than pending / active / done

OMG CMMN provides an instructive counterexample rather than a prescribed foundation model. Its Stage/Task lifecycle distinguishes states including Available, Enabled, Disabled, Active, Suspended, Failed, Completed and Terminated, with different transitions and meanings [S02].

Notably:

- Enabled can mean waiting for explicit start/disable action;
- Disabled is a deliberate semi-terminal non-execution state;
- Suspended preserves the possibility of resumption;
- Failed denotes an exception/failure condition with possible reactivation;
- Completed denotes normal termination;
- Terminated denotes a different terminal path, including exit criteria or explicit termination.

### Finding

A scalar `status` cannot safely conflate:

- availability/readiness;
- permission/activation condition;
- active execution;
- intentional suspension;
- failure;
- deliberate non-execution;
- normal completion;
- abnormal/alternative termination.

The exact CMMN state machine is domain-specific; the first-order result is that these semantics can matter independently.

## 2. Completion is not identical to success

CMMN defines a task completing normally in terms of its purpose being accomplished, while separately retaining failure and termination states [S02]. NASA systems-engineering guidance separately distinguishes verification, validation, acceptance and certification activities [S12].

### Finding

At least four closure/evaluation questions can diverge:

1. **Execution closure:** did the planned/permitted activity stop normally?
2. **Requirement verification:** does the result conform to specified requirements?
3. **Validation / fitness:** does it satisfy intended use or stakeholder expectations in the relevant context?
4. **Acceptance / readiness:** has the result passed the relevant acceptance or readiness gate?

A task may be execution-complete while later verification fails; a technically conforming result may fail intended-use validation; a validated result may still await an explicit acceptance/certification process.

Therefore `done` is often a vector of distinct predicates, not one fact.

## 3. Cancellation and termination are not deletion

CMMN distinguishes termination from completion and allows exit from several nonterminal states [S02]. This already establishes that `stop this work` can have meaning independent of `the purpose was achieved`.

Long-running transaction research goes further. Sagas allow partial steps to commit and then use compensating transactions if the overall long-running unit cannot finish successfully [S11]. A compensating transaction semantically amends prior effects but need not restore the exact previous state because other concurrent work may have observed or changed the world in the meantime.

### Finding

A foundation must keep conceptually distinct:

- **cancel / terminate:** stop pursuing the work;
- **rollback:** restore a previous state where that is possible;
- **compensate:** perform new work that semantically counteracts prior effects;
- **reconcile / repair:** establish an acceptable consistent state after partial effects;
- **retry / reactivate:** resume or repeat after resolving the failure condition.

These are not interchangeable lifecycle labels. They imply different causal and operational consequences.

## 4. Failure can create additional Work

Saga recovery is a clear example: an unsuccessful long-running unit can require compensating actions [S11]. CMMN failure can transition back toward active execution after the failure source is resolved [S02].

### Finding

Failure is not merely a terminal classification. It can be a **work generator**.

A failure path may create:

- diagnosis;
- remediation;
- compensation;
- retry/replay;
- revalidation;
- re-coordination;
- cleanup or reconciliation.

A model that treats failure as `closed = true` can therefore erase the work necessary to restore acceptable conditions.

## 5. Partial effects matter

Saga theory intentionally permits interleaving of subtransactions. Other work may observe partial effects before compensation occurs [S11]. This means the world after a failed long-running activity may not be equivalent to the world before it began.

### Finding

The semantics of Work cannot always be reduced to internal lifecycle state. Work may have externally visible effects during execution, and later recovery must reason about those effects.

This does not decide how records of effects are represented; that is a deferred Records relation.

## 6. Completion of children does not mechanically prove the parent outcome

HTN planning shows that tasks can be realised by different methods/task networks [S04]. NASA's separation of execution, verification, validation and acceptance [S12] shows independently that executing prescribed activities is not sufficient evidence of outcome fitness.

### Finding

Checklist completion is at best one kind of evidence about a parent objective. It does not logically entail that:

- the selected decomposition was sufficient;
- the resulting state satisfies requirements;
- the intended outcome was achieved;
- downstream acceptance is warranted.

This is a major failure mode for any Work model that defines parent completion as `all children complete` without an independent parent-level closure condition.

## 7. Requiredness and execution are separate dimensions

CMMN distinguishes requiredness/control rules from actual lifecycle execution [S02]. An item can also become disabled by a decision not to execute it in a case.

### Finding

Whether work **must** occur is not the same question as whether it **has** occurred or is currently executable.

At foundation level it is useful to keep apart:

- required / optional / discretionary;
- applicable / inapplicable;
- available / blocked;
- active / suspended;
- successful / failed / terminated.

The evidence does not yet justify a universal field set; it does justify the orthogonality of these questions.

## 8. Temporal state includes waiting and deadlines, not only duration

Coordination theory identifies prerequisite and simultaneity constraints [S05]. CMMN uses entry/exit criteria and event-driven transitions [S01][S02]. HTN task networks may contain ordering and interval constraints [S04].

### Finding

Work time has multiple semantics:

- processing duration;
- waiting for prerequisites/events;
- earliest/latest admissible timing;
- synchronization or overlap constraints;
- elapsed time across suspension;
- recurrence or repeated execution.

A single `start_at/end_at` pair cannot represent all of these meanings without losing why time matters.

## 9. Closure semantics for continuing work differ from bounded work

The earlier units analysis found that ongoing operations/durable activities do not have one natural final completion event [S08][S14].

### Finding

For continuing work, meaningful control may concern:

- maintaining a condition;
- periodic service or monitoring;
- satisfying rolling obligations;
- responding when a trigger occurs;
- remaining within performance/safety bounds.

Such work may have completed **episodes** while the larger responsibility remains open. Forcing the durable activity itself into `done` produces a false terminal state.

## 10. Failure modes exposed by this lens

Premature `todo / doing / done` semantics create predictable failure classes:

- **status collapse:** readiness, execution, suspension, failure and termination become indistinguishable;
- **completion leakage:** execution completion is mistaken for validated/accepted outcome;
- **checklist fallacy:** child closure automatically closes the parent;
- **cancellation-as-erasure:** externally visible partial effects and recovery work disappear;
- **failure-as-terminal:** remediation/compensation/retry work is not represented;
- **requiredness conflation:** optionality/applicability and execution state are mixed;
- **temporal blindness:** waiting, synchronization and deadline semantics collapse into elapsed duration;
- **false terminality:** ongoing responsibilities are forced into artificial completion.

## Causal-depth note

These failure modes are not merely UI/status naming problems. Their systemic cause would be a framing assumption that Work has one local lifecycle and one terminal success predicate. Renaming statuses without separating the underlying dimensions would address the symptom rather than the failure class.

## Deferred cross-vertical questions

- Evidence required to prove verification, validation, compensation or acceptance touches Records but is not solved here.
- Who may terminate, waive, accept or reactivate work belongs to Actors/authority synthesis.
- Whether durable obligations originate in actor roles, policies or records remains deliberately unresolved.
