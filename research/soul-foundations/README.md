# SOUL Foundations Research

## Purpose

This research package studies the foundational problem domains that may underlie SOUL before attempting a full SOUL architecture synthesis.

It is intentionally layered. Earlier research may change the structure, scope, or even the necessity of later research. The repository records the path actually supported by research; it does not pre-create future layers as if their necessity were already known.

## Current research hypothesis

The current starting hypothesis is that three problem domains deserve independent vertical research:

1. **Records / Artifacts** — what persists, how information is represented, stored, organised, governed, changed, traced, and retrieved.
2. **Work** — what must be done, changed, investigated, verified, or completed, and how such work is represented and controlled.
3. **Actors** — what performs work or exercises authority, and how identity, capability, responsibility, delegation, and accountability are represented.

These are research starting points, not accepted SOUL primitives or architecture truth.

## Layering rule

- Layer 0 provides bounded context and problem reconstruction from prior repository research.
- Layer 1 researches each current vertical independently.
- Later layers are **undetermined** until the evidence from the current layers justifies them.

A later synthesis may confirm, refine, add to, replace, or dissolve the current three-part framing.

## Vertical isolation rule

Each Layer-1 vertical should stay focused on its own problem domain. When research encounters a materially important relation to another vertical, record it as a deferred relational question rather than allowing the research to drift into the other domain.

Isolation is methodological, not ontological: the research must not assume that the domains are truly independent in reality.

## Epistemic rule

Research findings, taxonomies, models, and synthesis produced here are evidence and research outputs. They do not automatically become SOUL architecture decisions.

## Relationship to `research/soul-context/`

`research/soul-context/` remains the existing bounded context-reconstruction package. It is not duplicated here. `00_context/` records only the dependency from that completed context work into this foundations research.
