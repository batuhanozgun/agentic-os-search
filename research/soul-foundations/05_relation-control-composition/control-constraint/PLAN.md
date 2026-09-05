# Control / Constraint — Research Plan

**Status:** ACTIVE PLAN  
**Date:** 2026-09-05  
**Parent:** accepted Cross-Ground Composition

## 1. Research question

Determine whether `Control / Constraint` is a coherent and sufficiently bounded cross-ground composition region, what minimum semantics it must preserve, whether stable immediate children exist, and where its boundaries lie against Relational Binding, Composite Standing, ground-local Actors/Environment/Work/Information semantics and deferred Transition/Effect/Feedback.

## 2. Protected semantic distinction

The pass must be able to explain, without collapse, cases where all of the following diverge:

```text
norm / policy / instruction exists
legitimate authority exists
Actor is permitted / prohibited / obligated
request satisfies authorization criteria
approval / denial decision occurs
technical mechanism allows / blocks
alternate path remains / is closed
behavior complies / violates
monitoring detects / misses
recovery / escalation occurs
```

A useful result must say which distinctions are universal and which are optional/domain-specific.

## 3. Mandatory boundary checks

### 3.1 Binding boundary
Binding says exactly which anchors/roles/scope/time are connected. Control must not merely rename policy/authority/delegation bindings.

### 3.2 Standing boundary
Standing can say `authorized`, `eligible`, `compliant`, `approval-valid`, `gate-satisfied`, etc. Control must preserve the rule/authority/decision/enforcement semantics that produce or consume such standings without absorbing all qualification.

### 3.3 Actors boundary
Actor-local permission/authority/obligation/delegation remains Actors semantics where the protected question is the bearer/standing itself. Control is cross-ground only where those standings govern Work/Environment/Information transitions or decisions.

### 3.4 Environment boundary
A firewall, sandbox, missing credential, unavailable tool or physical interlock may be realized Environment condition. Control must distinguish `mechanically impossible/blocked` from `normatively prohibited` and determine when realized enforcement is a control-semantic layer rather than only a condition fact.

### 3.5 Work boundary
Approval/review/gate/check Work remains Work. Control must distinguish `approval Work occurred` from `transition was legitimately authorized/blocked/required`.

### 3.6 Information boundary
Policy/rule/configuration/decision records are representations. Control truth must not be equated with text/configuration/report presence.

### 3.7 Transition boundary
Control governs/conditions transitions. Transition child will later study what changed, propagated or caused what. This pass may preserve control-state/current applicability and path closure but must not take over event-history/causal dynamics.

## 4. Candidate semantic structure entering K0

This is a falsifiable starting hypothesis, not a result:

```text
Control episode / regime
├─ governed focus
│  ├─ Actor / Work / action / transition / resource / information operation
│  └─ exact scope / object / operation / context / time
├─ normative / policy basis
├─ authority / competence-to-govern basis
├─ control modality
│  ├─ permitted
│  ├─ prohibited
│  ├─ required
│  ├─ discretionary / conditionally allowed
│  └─ exception / waiver / escalation where material
├─ evaluation / decision / gate semantics
├─ enforcement / intervention semantics
├─ path / coverage / bypass semantics
├─ monitoring / compliance semantics
└─ validity/currentness dependencies
```

K1–K7 must attempt to destroy or simplify this structure.

## 5. Passes

### K0 — Canonical / evidence recovery
Recover current parent/child boundaries, ground-local authority/obligation/capability distinctions, candidate-study holdouts and live falsifiers.

Exit: frozen control hypotheses + source map.

### K1 — Protected question + minimum control signature
Test what must be known for a control claim to be meaningful across domains.

Key pressure:
- governed focus;
- norm/rule;
- authority;
- modality;
- decision/gate;
- enforcement;
- applicability/currentness.

Exit: provisional semantic grammar or collapse finding.

### K2 — Control-layer discrimination
Attack distinctions among:
- norm/policy/instruction;
- legitimate authority;
- deontic standing (permission/prohibition/obligation);
- authorization/approval decision;
- technical enforcement;
- monitoring/observation;
- compliance/violation standing.

Exit: which layers are irreducible, optional and compositional.

### K3 — Modality / gate / authority / path / bypass audit
Stress:
- allow/deny/require;
- preconditions/gates;
- exceptions/waivers;
- delegation;
- separation of duties;
- human approval;
- alternate routes and transitive effect power;
- fail-open/fail-closed;
- control coverage over reachable paths.

Exit: whether path-closure/bypass semantics require a distinct child/fifth region.

### K4 — Family discovery + rival decompositions
Test candidate child/rival structures:
- Normative Control / Decision Control / Enforcement Control;
- Preventive / Detective / Corrective;
- Authorization / Obligation / Safety / Quality;
- Policy / Decision / Enforcement / Monitoring;
- Constraint / Gate / Intervention;
- governance-only versus technical-only frames;
- pure state-machine/guard or pure access-control reductions.

Promotion criteria:
1. distinct protected question;
2. recurrent cross-domain failure family;
3. low overlap;
4. does not duplicate accepted ground/sibling semantics;
5. useful at Foundation level before architecture.

### K5 — Authoritative external + candidate-study holdouts
Use materially different traditions as pressure, including as available/relevant:
- NIST ABAC;
- NIST Zero Trust Architecture;
- NIST access-control/security control material;
- safety/interlock or systems-engineering gate concepts;
- governance/risk controls;
- selected Anthropic AI-native SDLC, multi-agent, context/harness studies.

Do not import implementation taxonomies as Foundation structure.

### K6 — Synthesis / immediate-child decision
Decide:
- coherent child or collapse/reopen;
- bounded leaf versus promoted children;
- final control semantic grammar;
- retained profiles/dimensions;
- next sequencing pressure toward Transition.

### K7 — Adversarial closure
Attack at least:
- Control duplicates Actors authority;
- Control duplicates Standing;
- Control duplicates Environment enforcement;
- Control is merely Work gating;
- policy/decision/enforcement should be children;
- preventive/detective/corrective should be children;
- alternate-path closure is graph/architecture detail only;
- monitoring/compliance belongs entirely elsewhere;
- deontic modality is too legalistic/domain-specific;
- control currentness belongs entirely Transition;
- bounded-leaf result reflects under-research;
- a fifth composition region/ground appears.

Return user-evaluation gate after K7.

## 6. Required hard cases

At minimum:

1. policy says no, runtime still permits;
2. runtime blocks, but no legitimate policy/authority supports block;
3. direct path denied, delegated/alternate path can still achieve effect;
4. approval recorded but approver lacks authority;
5. Actor permitted but not capable/actionable;
6. Actor obligated but technically unable;
7. criterion/gate satisfied but authorization absent;
8. authorization decision permits but enforcement stale/misconfigured;
9. compliant behavior occurs without monitoring evidence;
10. monitoring says compliant while actual behavior violates;
11. emergency override/waiver changes control applicability;
12. separation-of-duties requirement fails because producer verifies own work;
13. advisory instruction influences but does not mechanically constrain an AI agent;
14. deterministic sandbox blocks one tool but indirect agent/tool path remains.

## 7. Stop rules

Stop as bounded leaf when late pressure mainly generates:
- more domain control labels;
- mechanism-specific taxonomies;
- implementation choices;
- overlapping profiles already explained by one grammar;
- no new stable protected question.

Promote a child only if it clears all promotion criteria.

Reopen an upstream result only on a surviving decision-critical falsifier.

## 8. Verification boundary

Same-model adversarial review is not independent verification. External standards discriminate specific claims but do not validate the project decomposition by authority.

User acceptance closes sequencing only; it does not change verification independence.

## 9. Non-goals

Do not design:
- policy engine;
- RBAC/ABAC schema;
- authorization service;
- workflow gate implementation;
- sandbox/runtime architecture;
- event bus;
- SOUL/Development OS component architecture;
- ontology or database schema.