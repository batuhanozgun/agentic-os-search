# ECC — Browser dashboard exposure and consumer uses

2026-09-23 · **C6 current-snapshot transfer / U18-H active-unpublished source material.** Bu dosya browser dashboard’ın source projection, HTTP admission, rendering ve local action kullanımlarını taşır. BD kimlikleri desktop dashboard veya generic web-security tanımı değildir.

Source standing at extraction:
- canonical source `STATE.md`: **U18-H IN PROGRESS**, last completed/published U18-G;
- Note47 and MR48 describe a bounded source answer, but no U18-H publication receipt/final source STATE closure exists in this extraction snapshot;
- exact ledger: `evidence/U18-H-SOURCES.md`.
Fixed target: `affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a`.
Tests inspected, not run; no server/browser/model/clipboard/MCP/configuration execution.

## 1. Browser role and source projection

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-BD01 — browser dashboard | Local HTTP source catalogue over agents/skills/commands/rules/MCP/hooks. | Live operator, installer, task dispatcher or model controller değil. |
| ECC-BD02 — package-root source | Normal root derived from dashboard script/package location. | Installed host’s active project/config root automatically değil. |
| ECC-BD03 — supplied root | Exported server factory can receive explicit root. | Normal CLI exposes desktop-style editable root selector değil. |
| ECC-BD04 — agent projection | Agent files → name/description/model/tools/body prefix. | Full agent semantics, host loading or available tools proof değil. |
| ECC-BD05 — skill projection | Skill directories/SKILL body prefix → catalogue record. | Full skill body, actual loader state or effectiveness değil. |
| ECC-BD06 — command projection | Direct command Markdown → name/body prefix. | Registered/authorized command or successful execution değil. |
| ECC-BD07 — rule projection | Rule files/directories → language/path-oriented listing. | Active policy/enforcement or complete recursive ruleset değil. |
| ECC-BD08 — MCP projection | Root/template JSON declarations → reduced displayed server entries. | Installed/running MCP connections veya complete runnable configuration değil. |
| ECC-BD09 — hook projection | Source hook config + canonical dispatcher child registries → displayed hooks. | Enabled/profile-selected/executed hooks değil. |
| ECC-BD10 — projected body truncation | Agent/skill/command bodies bounded to finite prefixes. | Source remainder absent/unimportant veya detail view full-source proof değil. |
| ECC-BD11 — request-time data load | New request rereads configured source families. | One response is atomic/version-bound snapshot across all files değil. |
| ECC-BD12 — embedded page dataset | Rendered HTML embeds constant arrays for that delivered page. | Open page live-polls later source changes değil. |

## 2. MCP and hook representation

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-BD13 — root MCP declaration | Repository `.mcp.json` concrete declaration. | Host installed/connected server proof değil. |
| ECC-BD14 — MCP selection template | `mcp-configs/mcp-servers.json` optional catalogue/instructions. | All entries selected, credentials available or providers validated değil. |
| ECC-BD15 — MCP display reduction | Dashboard preserves selected name/command/url/args/env-like fields but omits template guidance/headers/comments. | Display is faithful runnable export değil. |
| ECC-BD16 — env-value masking | MCP environment values replaced before JSON/HTML projection. | All secret-bearing fields masked guarantee değil. |
| ECC-BD17 — unmasked argument/URL surface | Command/url/args do not receive equivalent env masking. | Actual secret exposure observed değil; field-location conditional boundary. |
| ECC-BD18 — tool-list normalization | Scoped/quoted tool expressions normalized without naïve comma splitting. | Tool exists/authorized/usable proof değil. |
| ECC-BD19 — hook sidecar fingerprint | Hook metadata IDs/descriptions checked against matcher/command fingerprints. | Authenticated signature/owner authority or runtime enablement değil. |
| ECC-BD20 — registry membership | Canonical-root dispatcher arrays expose child hook IDs. | Actual runHooks admission or per-hook enable/profile match değil. |
| ECC-BD21 — custom-root registry asymmetry | Child expansion depends on canonical package root/import relation. | Equivalent custom-root files get identical projection automatically değil. |

## 3. HTTP admission and freshness

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-BD22 — loopback listen selection | Normal server resolves and binds loopback address. | Per-user authentication or process isolation değil. |
| ECC-BD23 — Host admission | Missing/malformed/foreign Host rejected before routing. | Exact browser origin/user identity check değil. |
| ECC-BD24 — Origin admission | Present Origin hostname must be loopback-allowed. | Scheme/port equality or authentication değil. |
| ECC-BD25 — absent-Origin allowance | Requests without Origin can proceed for navigation/CLI-style use. | Any remote request accepted değil; Host guard remains. |
| ECC-BD26 — hostname-only origin comparison | Origin parser compares hostname and discards scheme/port distinction. | Browser can read response cross-origin proof değil. |
| ECC-BD27 — server-admission/browser-origin split | Server-side predicate and browser same-origin policy are separate controls. | One implies the other değil. |
| ECC-BD28 — no CORS grant | Dashboard does not emit Access-Control-Allow-Origin. | Universal browser unreadability or no nonbrowser client access değil. |
| ECC-BD29 — no-store response | Response helper sends Cache-Control no-store. | Live synchronization/polling or atomic source freshness değil. |

## 4. Failure, missingness and view standing

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-BD30 — outer 500 boundary | Escaping load/render failure → generic 500 while server logs detail. | Every family-specific parse error reaches 500 değil. |
| ECC-BD31 — inner MCP omission | Malformed MCP JSON can be logged then omitted from returned data. | Genuine no MCP config ile distinguish edilen API status guarantee değil. |
| ECC-BD32 — inner hook omission | Hook/sidecar mismatch can be correctly rejected then caught as empty hook list. | Actual host hook disabled/absent proof değil. |
| ECC-BD33 — successful-empty projection | Family-specific source failure can still yield HTTP200 + “none found/configured” view. | Failure hidden everywhere değil; server diagnostic can remain. |
| ECC-BD34 — validation-to-absence collapse | Correct metadata rejection reason can disappear at later catalogue projection. | Validator itself permissive or incorrect proof değil. |
| ECC-BD35 — request success ≠ source completeness | Valid HTTP/HTML response does not certify every loader succeeded. | Whole page useless/invalid değil. |

## 5. Encoding, DOM and client actions

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-BD36 — initial JSON angle-bracket escaping | Serialized embedded data replaces literal '<' before initial script parse. | Later rendering contexts automatically safe değil. |
| ECC-BD37 — text-safe consumers | Many client fields use esc/textContent/function handlers. | Every DOM sink context-safe guarantee değil. |
| ECC-BD38 — MCP args innerHTML sink | Joined MCP argument text concatenated into HTML assigned to `innerHTML`. | Executed exploit veya real credential payload değil. |
| ECC-BD39 — two-stage encoding boundary | Initial script-data escape is consumed before later string reaches HTML parser. | Initial test failure or browser exploit frequency proof değil. |
| ECC-BD40 — benign markup countercase | Stipulated `<b>sample</b>` argument becomes markup in detail consumer. | Malicious script execution demonstrated değil. |
| ECC-BD41 — generated-attribute context | Some metadata enters generated attributes/badges under different escaping needs. | Every attribute injection exploitable proof değil. |
| ECC-BD42 — server-string escaping test | Upstream test checks Unicode-escaped angle brackets in generated HTML source. | Embedded client DOM result or MCP detail sink tested değil. |
| ECC-BD43 — command copy action | UI copies slash-command name; no execution occurs. | Valid installed command or command outcome proof değil. |
| ECC-BD44 — clipboard promise | `writeText` returns asynchronous completion/rejection. | Immediate UI feedback = completed copy değil. |
| ECC-BD45 — optimistic copied feedback | UI can show Copied outside observed promise fulfillment; fallback result also ignored. | Every copy fails or user acted on copied text değil. |
| ECC-BD46 — localStorage continuity | Theme/language/recent-view state retained locally. | ECC work state, authentication or durable task history değil. |

## 6. Test/evidence and source-standing distinctions

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-BD47 — HTTP fixture tests | Test definitions include loopback requests, Host/Origin rejection, no-store and continued service after injected errors. | Tests ran, installed network environment or browser DOM behavior proof değil. |
| ECC-BD48 — malformed-source tests | Selected malformed MCP/hooks fixtures expect empty arrays. | HTTP success = complete source data guarantee değil. |
| ECC-BD49 — render failure tests | Injected outer load/render failures exercise generic 500 path. | Same as caught family-specific parse failure değil. |
| ECC-BD50 — source answer / publication standing split | Note47/MR48 call the bounded inquiry source-complete while canonical source STATE remains IN PROGRESS pending entry/publication closure. | Concepts may call it published/closed source unit değil. |
| ECC-BD51 — active source snapshot | Existing Note47/ledger/round are legitimate current corpus material despite source publication not closed. | Future U18-H publication/result files are already known or implicitly complete değil. |
| ECC-BD52 — desktop/browser non-equivalence | Desktop Q08d1 and browser Q08d2 have different implementations/consumers. | Shared dashboard name means same controls or risks değil. |

## 7. U18-H non-collapse

- source declaration ≠ active capability;
- registry membership ≠ hook execution;
- masked env ≠ all-field secrecy;
- Host/Origin admission ≠ user authentication;
- server admission ≠ browser readability;
- no-store ≠ live synchronization;
- validation refusal ≠ visible degraded status;
- HTTP200 ≠ source completeness;
- initial serialization escape ≠ final DOM encoding;
- copied feedback ≠ clipboard completion;
- clipboard completion ≠ command execution;
- bounded source answer ≠ checked source publication.

This Concepts transfer is explicitly snapshot-scoped to the existing U18-H files. Future source-study publication or U18-I material is a later delta, not silently pre-extracted.
