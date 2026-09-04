# External Research Reuse Registry

## Purpose

This is the canonical cross-phase continuity surface for **externally researched sources, capabilities, services, datasets, patterns, standards, repositories and discovery indexes that may later be useful to SOUL or Development OS**.

The intent is not to turn every external source into a dependency or architecture choice. The intent is to prevent useful external research from disappearing after its immediate question is answered.

This surface should remain relevant across the transition from research into later SOUL / Development OS design and implementation work.

## Accepted continuity intent

When substantive external research is performed, preserve two distinct outputs when they are materially useful:

1. the research result needed for the current question; and
2. a **reuse candidate** describing whether the researched thing may later help SOUL or Development OS, and if so, how it might be used.

The second output is prospective design memory, not a design decision.

A future SOUL / Development OS design or implementation phase should explicitly review this registry before assuming that needed capabilities, data, patterns or discovery mechanisms must be invented from scratch.

## What belongs here

Add or refresh an entry when external research exposes something with plausible later reuse value, for example:

- a capability or service SOUL could call on behalf of a user;
- an API, tool, provider or integration surface;
- a discovery index that helps find capabilities or data sources;
- a dataset, benchmark, standard or authoritative knowledge source;
- a reusable software or agent pattern;
- a repository, framework or reference implementation;
- an external source family that could inform build-vs-integrate decisions;
- an important negative result showing that a tempting external dependency is unsuitable.

Do **not** add every link, citation or primary source used as evidence. Detailed evidence belongs in the relevant research package. This registry is a selective retrieval surface for later reuse decisions.

## Reuse entry semantics

Each material entry should preserve, as applicable:

- **Target** — what was researched;
- **Kind** — capability, service, repository, dataset, pattern, standard, discovery index, evidence source, etc.;
- **Current status** — candidate, rejected, superseded, adopted, or another explicit state;
- **Potential SOUL use** — what user-facing or system capability it might support;
- **Potential Development OS use** — what development/workflow/build-vs-integrate decision it might support;
- **Reuse mode** — direct integration, discovery only, evidence/reference, implementation pattern, benchmark, dataset, etc.;
- **Why it matters** — the prospective value discovered by the research;
- **Constraints / risks** — freshness, trust, licensing, privacy, security, cost, auth, availability, lock-in, maintenance or other material limits;
- **Revalidation needed** — what must be checked again before real adoption;
- **Detailed research route** — repository path when a durable research package exists;
- **External source** — canonical external URL or identifier when useful.

Missing fields are allowed when the current research did not establish them. Do not fill gaps by assumption.

## Epistemic boundary

An entry here means:

> “This may be useful later and is worth recovering.”

It does **not** mean:

- SOUL or Development OS should adopt it;
- its provider is reliable enough for production;
- its current pricing, license, terms, API or availability will remain unchanged;
- the current research result is independently verified;
- the item belongs in the final architecture.

Before adoption, retrieve the relevant detailed research and re-check decision-critical current facts against authoritative sources.

## Revisit triggers

Review relevant entries when work reaches any of these conditions:

- SOUL or Development OS architecture/design begins;
- a project needs an external capability, data source, service or knowledge channel;
- a build-vs-integrate decision is being made;
- Environment/capability design asks what the system can reach outside itself;
- retrieval, tool-use, external knowledge or integration architecture is being designed;
- a candidate dependency/provider is being selected or replaced.

## Registry

### public-apis/public-apis

- **Target:** `public-apis/public-apis`
- **Kind:** community-curated API discovery index / repository
- **Current status:** reuse candidate; discovery value established at a general level, adoption not evaluated
- **Potential SOUL use:** help discover project-relevant external APIs/capabilities when SOUL needs a user-benefiting channel that is not native to the system itself
- **Potential Development OS use:** support early capability discovery and build-vs-integrate exploration before implementing a service from scratch
- **Reuse mode:** discovery only; provider-specific APIs must be evaluated separately
- **Why it matters:** broad category coverage can act as a starting catalogue for finding external capabilities and data/service providers
- **Constraints / risks:** community curation can be stale or uneven; “public/free” does not imply permanently free, production-ready, trustworthy or unrestricted; individual provider documentation remains authoritative
- **Revalidation needed:** before using any discovered API, verify current provider documentation, availability, authentication, limits, pricing, licensing/terms, security/privacy fit and operational suitability
- **Detailed research route:** no dedicated durable research package yet; current evaluation originated in project conversation and this registry preserves only the prospective reuse conclusion
- **External source:** https://github.com/public-apis/public-apis

## Maintenance rule

Prefer updating an existing entry over creating duplicate authoritative copies. If later research produces a dedicated package, link to it here rather than copying its full findings.

If an item is rejected, superseded or adopted, preserve that state explicitly rather than silently deleting the history when the history may prevent repeated work.
