# Work — Foundational Research Plan

**Status:** active foundational pass  
**Date opened:** 2026-09-01

## Why this vertical starts from zero

`Work` was a Layer-1 research hypothesis, not a proven SOUL primitive.

The completed Records vertical must not define Work by analogy. This pass therefore asks independently what kinds of concepts are needed to represent **something that ought to be done and what actually happens when it is pursued**.

## Primary question

> **What is Work? Which distinctions among goal, requirement/obligation, task, action, activity, job, process, workflow, plan, execution, attempt, transition and outcome are load-bearing for representing and controlling purposeful change?**

## Competing starting frames

Test at least:

1. **Work as desired state transition** — work exists because the current state differs from a desired/required state.
2. **Work as specification** — a task/job/work item is a description/commitment of what needs doing.
3. **Work as occurrence/activity** — work is the actual performance/execution event/process.
4. **Work as process/network** — work is an ordered/conditional structure of related activities.
5. **Work as plan** — work is a chosen sequence/partial order of actions intended to achieve a goal.
6. **Work as obligation/commitment** — work exists because some condition must be satisfied, even before a plan exists.
7. **Situated/emergent work** — actual work can diverge from formal process/plan and require exception/articulation/coordination.

Do not assume these are mutually exclusive; they may address different layers.

## Research lenses

- business process / BPMN semantics;
- workflow theory / Petri-net/workflow-net correctness;
- classical planning / action/state/goal/plan models;
- hierarchical task/decomposition models;
- scheduling / operations research (jobs, precedence, resources, time);
- project/work-package/task models;
- state machines / transition systems where they clarify execution state;
- transaction/compensation/idempotency ideas only when they expose work semantics;
- human-computer interaction / task analysis;
- CSCW / situated work / articulation work / exception handling;
- case management / knowledge-work models where fixed workflow assumptions fail.

These are evidence lenses, not candidate SOUL components.

## Questions

1. Is `work` one natural object type or an umbrella over specification, execution and outcome?
2. What is the boundary among goal, task, action, process and plan?
3. Can work exist before a concrete plan exists?
4. Can the same work specification have multiple attempts/executions?
5. Can an execution succeed operationally while failing the intended outcome, or vice versa?
6. What kinds of dependency/order/condition relations are semantically distinct?
7. When is decomposition hierarchical, sequential, partial-order, conditional, iterative or emergent?
8. What makes work `complete`? Completion of execution, satisfaction of goal, acceptance/verification, or another condition?
9. How should failure, retry, cancellation, compensation, suspension and abandonment differ conceptually?
10. Is a fixed workflow/process model adequate for all work, or do case/adaptive/situated models expose a separate class?
11. Which dimensions belong intrinsically to Work and which depend on Actors/resources/tools/authority and must be deferred?
12. What information is required to know the current state/progress of work without choosing an orchestration implementation?

## Counter-frames / falsifiers

Actively challenge:

- work = task;
- work = plan;
- plan = execution;
- process = workflow = project;
- one DAG is the natural structure of all work;
- all work can be decomposed before execution;
- completion means `all steps ran`;
- success is binary and intrinsic to the task;
- retry is simply the same execution again;
- failure means no useful outcome was produced;
- every work item needs an Actor/resource model inside Work;
- human/knowledge work should be forced into deterministic workflow semantics;
- software orchestration patterns are universal work ontology.

## Vertical isolation

When evidence exposes relations to Records, Actors, resources/tools or authority:

- preserve the relation as a deferred question;
- do not solve the other vertical from Work;
- do not import the Records vertical's object model as an axiom.

## Scope exclusions

Do not yet:

- design SOUL orchestration;
- select Temporal/Airflow/BPM engine/queue/scheduler;
- define Worker/Agent/Actor ontology;
- choose database/state storage;
- design permissions/delegation;
- optimize scheduling algorithms;
- build a universal task schema;
- treat LLM-agent frameworks as foundational evidence.

## Operational return condition

The foundational Work pass is complete when:

1. major competing work/task/process/action models have been compared across independent disciplines;
2. load-bearing distinctions among specification, execution/occurrence and outcome are tested;
3. goal/task/plan/action/process/workflow boundaries are explicit enough to falsify simple models;
4. dependency/decomposition/control-flow families are mapped without prescribing implementation;
5. completion/success/failure/cancellation/retry ambiguities are exposed;
6. fixed workflow assumptions are challenged with adaptive/situated/case-work evidence;
7. cross-vertical relations are deferred explicitly;
8. an adversarial omission/counterexample pass is completed;
9. source trace and bounded synthesis are persisted;
10. the next Work research direction is re-derived from findings.

Meeting this condition does not complete the Work vertical.