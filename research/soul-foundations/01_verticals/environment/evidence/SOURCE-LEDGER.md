# Environment — Source Ledger

**Status:** active evidence-recovery surface  
**Date opened:** 2026-09-01  
**Rule:** source observations below are evidence inputs, not accepted Environment findings or architecture.

## Source roles

### E01 — NASA Systems Engineering Handbook, System Design Processes

- Source: NASA, `SEH 4.0 System Design Processes`
- URL: https://www.nasa.gov/reference/4-0-system-design-processes/
- Type: authoritative systems-engineering guidance
- Initial signal: system design explicitly identifies external and enabling systems, physical/functional interfaces and anticipated operating uses. The system-of-interest is engineered in relation to things beyond its development boundary.
- Discriminates: external-world/system-boundary frame vs an intrinsic Environment category.
- Does not prove: that all environment semantics form one foundation leg, or that system-engineering boundaries transfer unchanged to agentic software.

### E02 — SEBoK, Engineered System Context

- Source: Guide to the Systems Engineering Body of Knowledge (SEBoK), `Engineered System Context`
- URL: https://sebokwiki.org/wiki/Engineered_System_Context
- Type: systems-engineering body-of-knowledge synthesis
- Initial signal: system context is used to define an engineered system-of-interest and important relationships between it and systems with which it works; systems approaches are applied in context rather than to an isolated system.
- Discriminates: boundary-relative context and external relations vs environment as a fixed object type.
- Does not prove: a universal ontology of environment or that external entities are necessarily a distinct first-order family.

### E03 — Anind K. Dey, Understanding and Using Context

- Source: Dey, A. K. (2001), `Understanding and Using Context`
- URL: https://sites.cc.gatech.edu/fce/ctk/pubs/PeTe5-1.pdf
- Type: highly cited HCI/context-aware-computing paper
- Initial signal: provides an operational account of context as information that can characterize the situation of relevant entities for an interaction/application.
- Discriminates: context-as-relevant-situational-information from environment-as-everything-outside.
- Does not prove: that context is exhaustively representable as stable attributes or that contextual relevance is independent of activity and interpretation.

### E04 — Paul Dourish, What We Talk About When We Talk About Context

- Source: Dourish, P. (2004), `What We Talk About When We Talk About Context`
- URL: https://www.dourish.com/publications/2004/PUC2004-context.pdf
- Type: peer-reviewed HCI/context theory paper; author-hosted copy
- Initial signal: directly challenges conventional representational treatments of context and advances an interactional alternative in which context is not merely a stable set of external facts specified in advance.
- Discriminates: stable context-data frame vs interactional/emergent context.
- Does not prove: that contextual information cannot be represented, only that a purely representational framing can miss how context acquires relevance in interaction.

### E05 — J. J. Gibson, affordances

- Source: Gibson, J. J. (1979), affordances chapter/excerpt from `The Ecological Approach to Visual Perception`
- URL: https://cs.brown.edu/courses/cs137/2017/readings/Gibson-AFF.pdf
- Type: foundational ecological-psychology primary text excerpt
- Initial signal: affordances concern what an environment offers/provides relative to an organism; action possibility is not safely treated as a property of the actor alone.
- Discriminates: Actor-intrinsic capability from relational environment–actor action possibility.
- Does not prove: how digital/institutional affordances should be represented or that affordance belongs inside an Environment leg rather than a relation layer.

### E06 — Sutton & Barto, Reinforcement Learning: An Introduction

- Source: Sutton, R. S. & Barto, A. G., `Reinforcement Learning: An Introduction`, 2nd ed.
- URL: https://incompleteideas.net/book/the-book-2nd.html
- Type: canonical reinforcement-learning textbook
- Initial signal: a learning agent is modelled through an explicit agent–environment interaction interface involving sensed state/observations, actions and resulting transitions/rewards.
- Discriminates: operational agent boundary and external transition dynamics from Actor-only models.
- Does not prove: that `environment` is ontologically coherent; in RL it can function as the residual dynamics outside the agent boundary.

### E07 — Open Container Initiative Runtime Specification

- Source: Open Container Initiative, Runtime Specification / configuration
- URLs:
  - https://github.com/opencontainers/runtime-spec/blob/main/config.md
  - https://specs.opencontainers.org/runtime-spec/config-linux/
- Type: current technical specification
- Initial signal: an execution environment can include process settings, injected environment variables, mounts, namespaces, isolation and resource limitations; feasibility/behavior depends on execution substrate conditions external to application logic.
- Discriminates: Actor capability / Work description from runtime feasibility and resource/isolation conditions.
- Does not prove: that software runtime is representative of physical/social/domain environments generally.

### E08 — Kubernetes Pods

- Source: Kubernetes documentation, `Pods`
- URL: https://kubernetes.io/docs/concepts/workloads/pods/
- Type: current official platform documentation
- Initial signal: a workload executes within shared networking and storage resources and platform-managed runtime conditions. Resource/service availability can be constitutive of what execution is possible without being an intrinsic property of the workload itself.
- Discriminates: Work unit from execution substrate/resources.
- Does not prove: foundation-level ontology; it is a concrete software systems example.

### E09 — W3C Web of Things Thing Description

- Source: W3C, `Web of Things (WoT) Thing Description 2.0`
- URL: https://www.w3.org/TR/wot-thing-description-2.0/
- Type: W3C technical specification
- Initial signal: interaction affordances are described as possible choices for consumers and are typed into properties, actions and events. An external thing's usable interaction surface is represented explicitly rather than collapsed into consumer capability.
- Discriminates: external interface/affordance semantics from Actor-only capability.
- Does not prove: Gibsonian affordance theory or a universal Environment schema.

### E10 — Star, The Ethnography of Infrastructure

- Source: Star, S. L. (1999), `The Ethnography of Infrastructure`
- URL: https://journals.sagepub.com/doi/10.1177/00027649921955326
- Type: peer-reviewed infrastructure studies paper
- Initial signal: infrastructure is relational/ecological, embedded in practice, often transparent in use and visible upon breakdown; what functions as infrastructure depends on the activity/community relation, not merely on an object's intrinsic type.
- Discriminates: infrastructure-as-object/environment bucket from relation/practice-dependent infrastructure.
- Does not prove: that infrastructure should be assigned to Work, Actors, Environment or a relation fabric in SOUL.

### E11 — Clark & Chalmers, The Extended Mind

- Source: Clark, A. & Chalmers, D. (1998), `The Extended Mind`
- URL: https://www.jstor.org/stable/3328150
- Type: peer-reviewed philosophy of mind paper
- Initial signal: argues that sufficiently coupled external resources can become constitutive parts of a cognitive process rather than merely external surroundings.
- Discriminates: fixed actor/environment boundary from boundary-shift or distributed-system framings.
- Does not prove: that SOUL should adopt extended-mind criteria or treat tools as Actors.

### E12 — Environment Ontology (ENVO)

- Source: Buttigieg et al. (2013), `The environment ontology: contextualising biological and biomedical entities`
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/
- Type: peer-reviewed ontology paper / domain ontology
- Initial signal: demonstrates that `environment` can be decomposed into systems, components/materials/processes and contextual relations at multiple granularities; ENVO treats environments as a substantive modeling domain rather than one undifferentiated field.
- Discriminates: environment-as-single-attribute/bucket from structured environmental region.
- Does not prove: generality beyond ecological/biomedical use or relevance of ENVO's exact ontology to SOUL.

## Initial cross-source observations — not yet promoted findings

1. **Environment is strongly boundary-relative in systems and agent traditions.** NASA/SEBoK and RL all require an explicit system/agent of interest before `environment` becomes determinate.
2. **Context is not equivalent to environment.** Dey narrows context by relevance to a situation; Dourish challenges context as a stable representational container and treats relevance as interactionally achieved.
3. **Capability is not enough.** Gibson, W3C WoT and runtime examples all expose action possibility as dependent on conditions/resources/interfaces outside the bearer alone.
4. **Technical substrate is materially real but may be only one subregion.** OCI/Kubernetes show execution-environment semantics with clear consequences for feasibility and behavior, but do not establish unity with social/physical/domain context.
5. **Boundary membership can change with framing/coupling.** Extended-mind and infrastructure accounts warn that tools and infrastructure can move from `external thing` to constitutive/embedded system element depending on analytical purpose and practice.
6. **The null hypothesis remains live.** Much of the strongest evidence can be read as support for explicit boundary/context/affordance/resource relations rather than for an independent fourth leg.

## Recovery rule

When a claim becomes load-bearing, recover the primary/authoritative source directly and record the exact supported distinction. Search snippets and this ledger are not sufficient for exact wording, exhaustive absence claims or architecture decisions.