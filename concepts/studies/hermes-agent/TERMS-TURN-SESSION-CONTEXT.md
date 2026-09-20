# Hermes Agent — Turn, session and context terms

2026-09-20, **B6-T15 / PARTIAL DURABLE TRANSFER**. [TERMS.md](TERMS.md)'nin bağlı parçasıdır. Kaynak: Hermes notes 05–16, synthesis/02 ve related evidence/coverage.

## 1. Lifecycle identities

| ID / ifade | Hermes araştırmasındaki kullanım | Sınır |
|---|---|---|
| HA-T01 — persistent work | Birden fazla turn/session/process boyunca sürebilen user/system pursuit. | Session veya turn ile aynı değil. |
| HA-T02 — session | Conversation continuity/history/storage için kullanılan lifecycle/container identity. | Current context version veya active worker demek değil. |
| HA-T03 — session ID | Session record/continuation'ı adresleyen identity. | Same ID ≠ same exact history/context. |
| HA-T04 — turn | Bir user/system input'un admitted model/tool work cycle'ı. | Session'dan kısa lifecycle. |
| HA-T05 — turn ID | Exact admitted turn/lease/work attempt identity. | Session ID veya task/run ID değil. |
| HA-T06 — model-tool iteration | Tek turn içindeki request→tool/result→next request döngüsünün bir adımı. | Turn completion ile aynı değil. |
| HA-T07 — provider attempt | Provider/model transportunda bir request/retry/fallback denemesi. | Model-tool iteration veya user turn ile aynı değil. |
| HA-T08 — run_conversation | AIAgent facade üzerinden admitted conversation-turn execution entry. | Her backend aynı inner loop'u kullanmaz. |
| HA-T09 — durable turn lease | Aynı session/work üzerinde cross-process turn ownership/admission hakkı. | Local running flag ile aynı değil. |
| HA-T10 — local running slot | TUI/session object üzerinde turn başlatma/çalışıyor durumunu tutan local control. | Durable lease veya model-start receipt değil. |
| HA-T11 — turn admission | History/session/lease/current ownership uygunluğuna göre turn'ün başlayabilme kararı. | Thread schedule ile aynı değil. |
| HA-T12 — thread scheduled | Local worker thread'in oluşturulup start edilmesi. | First model request'in gerçekleştiğini kanıtlamaz. |
| HA-T13 — first model request | Prepared context/history'nin provider/native backend'e ilk actual model invocation'a dönüşmesi. | Current source-study'de birçok yol için hâlâ residual. |
| HA-T14 — terminal turn result | Turn'un completed/interrupted/error/empty gibi outer completion representation'ı. | Work acceptance veya persistence receipt değil. |

## 2. History and context representations

| ID / ifade | Yerel kullanım | Sınır |
|---|---|---|
| HA-T15 — conversation history | Session/turn için stored message sequence veya selected copy. | Provider wire payload ile aynı değil. |
| HA-T16 — history snapshot | Turn başlarken current history'nin list-copy/version-bound görünümü. | Later concurrent writes'i otomatik içermez. |
| HA-T17 — history version | Snapshot/current session history arasındaki change identity/check. | Semantic equivalence garantisi değil. |
| HA-T18 — stored transcript | SessionDB veya HERMES messages görünümündeki kalıcı representation. | Native backend authoritative thread ile aynı değil. |
| HA-T19 — api_content | Provider/model request assembly için selected/normalized message content. | Stored transcript'in birebir kopyası değil. |
| HA-T20 — wire view | Actual provider/native transport'a giden representation. | HERMES local history ile aynı olmayabilir. |
| HA-T21 — context engine | Prompt/history/context selection/transformation yapan ordinary runtime component family. | “Context” genel teriminin tek anlamı değil. |
| HA-T22 — context reference expansion | Turn input içindeki references'in model-visible content'e genişletilmesi. | CLI/TUI notification paths aynı davranmayabilir. |
| HA-T23 — prompt snapshot | Belirli turn/request için dondurulmuş model-visible prompt/history view. | Disk/live memory state ile aynı değil. |
| HA-T24 — prepared request | Context/history/tool definitions'in model/provider call'a hazır hale gelmiş formu. | Request gerçekten gönderildi receipt'i değil. |

## 3. Compaction, restore and continuation

| ID / ifade | Yerel kullanım | Sınır |
|---|---|---|
| HA-T25 — compaction | Uzun history/context'in model window için compressed/derived continuation state'e dönüştürülmesi. | Session ID değişimi zorunlu değil. |
| HA-T26 — compression lineage | Compacted continuation'ın hangi prior session/history state'ten türediğini bağlayan relation. | Simple same-session equality değil. |
| HA-T27 — compression checkpoint | Compaction öncesi truthful boundary/history state'i korumaya yönelik checkpoint requirement. | Bütün native backendlerde aynı implementation değil. |
| HA-T28 — context rebuild | Compaction/restore/config changes sonrası prompt/history view'in yeniden oluşturulması. | Original context'in lossless replay'i değil. |
| HA-T29 — session restore | Persisted session/history state'ten yeni process/runtime continuation kurma. | Old worker'ı reanimate etmek değil. |
| HA-T30 — history substitution | Durable lease/admission'ın selected persisted history'yi current turn'e bağlaması. | Whole session object equality değil. |
| HA-T31 — continuation | Prior work/session state'ten yeni admitted turn/work execution'a geçiş. | “Same agent object” yeterli condition değil. |
| HA-T32 — resume admission | Saved/restored state'in gerçekten new active work right/session turn'e alınması. | Record exists ≠ resumed work. |
| HA-T33 — driver recovery | Restart/rotation sonrası queue/driver/session machinery'nin persisted state'i yeniden execution'a taşıması. | State load ile same thing değil. |

## 4. Backend-specific context ownership

| ID / ifade | Yerel kullanım | Sınır |
|---|---|---|
| HA-T34 — ordinary HERMES loop | HERMES request assembly/retry/tool round/finalization sahibi olan inner conversation loop. | codex_app_server whole-turn path ile aynı değil. |
| HA-T35 — codex_responses | Ordinary HERMES loop içinde farklı model transport/API mode. | codex_app_server ile eşit değil. |
| HA-T36 — codex_app_server | Whole turn'ü external/native app-server session'a devreden runtime path. | HERMES facade admission tamamen bypass ediliyor demek değil. |
| HA-T37 — native thread | Codex app-server'ın kendi thread/session history owner'ı. | HERMES stored transcript değil. |
| HA-T38 — projected messages | Native completed events/items'tan HERMES message shape'e dönüştürülen mirror representation. | Authoritative native history'nin lossless copy'si değil. |
| HA-T39 — native compaction | Native runtime'ın kendi thread context'ini compact etmesi. | HERMES transcript rewrite ile aynı değil. |
| HA-T40 — context ownership | Hangi runtime'ın history/compaction/request assembly üzerinde authoritative çalışma kontrolü taşıdığı. | Agent class identity'den otomatik çıkmaz. |

## 5. Notification/re-entry context

| ID / ifade | Yerel kullanım | Sınır |
|---|---|---|
| HA-T41 — synthetic notification | Child/process completion event'inden parent turn'e girecek yeni text representation. | Child transcript'in tamamı değil. |
| HA-T42 — SubagentNotification | CLI path'te notification text + metadata taşıyan input carrier. | UI short display ile aynı değil. |
| HA-T43 — notification ownership | Event'in hangi current session/continuation tarafından consume edilebileceğinin routing predicate'i. | Queue'da görünmek ownership kanıtı değil. |
| HA-T44 — compression-aware routing | Old session key'i current continuation lineage'a bağlamaya çalışan ownership route. | Random new session authority vermez. |
| HA-T45 — current-history re-entry | Completion notification'ın current parent history snapshot ile yeni turn'e girme amacı. | Ack veya queue insertion bunu tek başına kanıtlamaz. |
| HA-T46 — interim notice | Child'ın early failure/progress gibi final completion hakkını tüketmemesi gereken event. | Final completion ile aynı delivery token semantics değil. |
| HA-T47 — restored completion | Restart'tan sonra durable completion'ın queue'ya yeniden sunulması. | Child work'ün yeniden yürütülmesi değil. |

## 6. Repeated non-collapse rules

Hermes source current coverage şu ayrımları tekrar tekrar taşır:

- persistent work ≠ session;
- session ≠ turn;
- turn ≠ model-tool iteration;
- provider attempt ≠ turn;
- session ID ≠ exact current history;
- stored transcript ≠ api_content ≠ wire view;
- local running flag ≠ durable turn lease;
- thread scheduled ≠ first model request;
- session restored ≠ old work re-executed;
- completion notification exists ≠ parent model admitted/used it;
- ordinary HERMES history ≠ native app-server authoritative thread.

Q55 native model/system/history→wire binding ve process-restart native-thread continuity current source-study'de açık residual olarak kalır.
