# Candidate Studies — INDEX

## Role

Retrieval router for `research/studies/**`.

This library contains reusable **candidate research**, not Foundation authority or architecture decisions.

Start with `CATALOG.md` when the question is “what prior research might matter here?” Then descend only into selected packages.

## Library semantics

Candidate studies are classified by research object:

- `focused-topic` — concept/problem/mechanism/method/pattern/technical area;
- `external-target` — one defined external repository/article/product/service/standard/dataset/provider/catalogue or other artefact;
- `hybrid` — both roles are materially present.

A study can use external sources without being an `external-target` study.

## Retrieval flow

```text
CATALOG.md
  ↓ select plausible studies
package/META.md
  ↓ confirm relevance / status / revalidation need
package/STATE.md or INDEX.md when present
  ↓
relevant finding / synthesis / assessment / evidence
  ↓
authoritative current external source when decision-critical
```

Do not load every study merely because the library exists.

## Current routes

| Need | Read first | Then if needed |
|---|---|---|
| Scan all known candidate studies | `CATALOG.md` | selected package `META.md` |
| Understand package creation/metadata rules | `PACKAGE-CONTRACT.md` | root `../INDEX.md` |
| Knowledge access / representation / adaptation mechanisms | `ai-knowledge-strategies/META.md` | `STATE.md` → `INDEX.md` / mechanism files |
| Context / memory / harness engineering | `context-memory-harness-engineering/META.md` | `STATE.md` → `INDEX.md` / cross-layer synthesis |
| Multi-agent coordination / control patterns | `multi-agent-patterns/META.md` | assessment / conversation synthesis |
| Hands-On LLM repository as evidence/reference corpus | `hands-on-large-language-models/META.md` | repository research → SOUL/DevOS assessment |
| Public/free API discovery catalogue | `public-apis/META.md` | `RESEARCH.md` → current upstream repository/docs |

## Foundation interaction

Candidate studies may be relevant while Foundation work deepens, but Foundation research controls when and how they are used.

Use studies as applicable for:

- evidence or counterexample;
- falsifier / pressure test;
- concrete mechanism knowledge;
- external capability landscape;
- implementation/reference examples;
- benchmark/test-case ideas.

Do not infer from a relevance tag that a study belongs inside a Foundation node.

## Design / architecture interaction

When SOUL or Development OS design/architecture/implementation is later authorised:

1. recover current project/Foundation state first;
2. use `CATALOG.md` to find candidate prior research;
3. inspect selected `META.md` files;
4. recover detailed findings;
5. revalidate current external facts where needed;
6. make the design decision under the then-current authorization and evidence.

Completion of a study never authorizes adoption.

## Current package list

- `ai-knowledge-strategies/`
- `context-memory-harness-engineering/`
- `hands-on-large-language-models/`
- `multi-agent-patterns/`
- `public-apis/`

The library is expected to grow substantially. `CATALOG.md` should remain a compact discovery surface rather than a second synthesis corpus.
