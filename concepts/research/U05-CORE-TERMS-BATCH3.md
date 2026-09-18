# Core Terms — U05: Üçüncü 10 Terim İçin Bağlantılı İnceleme

**Tarih / erişim:** 2026-09-18.  
**Statü:** kaynak ve kavram incelemesi; v0.2 working reference'ı Work–Environment–control hattında genişletir. Evrensel sözlük, nihai ontoloji veya SOUL/Development OS tasarımı değildir.  
**Dayanak:** [U03](U03-CORE-TERMS-BATCH1.md), [U04](U04-CORE-TERMS-BATCH2.md), Work Management / Project Control study, Context/Memory/Harness study, Carbon Layer sandboxing study ve sınırlı güncel OpenAI/NIST birincil belgeleri.

## Bu batch neden bu 10 terimi seçti?

v0.2 haritası şu açık ayrımları bıraktı:

- Run/Session/Memory dışında “şu an sistem hangi durumda?” sorusunu taşıyan genel State nedir?
- Work'ün current standing'i ile runtime/session state aynı şey mi?
- Actor/Agent'ın çalıştığı Environment ile Workspace ve Sandbox nasıl ayrılır?
- Policy ile Guardrail aynı kontrol türü mü?
- Verification ile Observability aynı şey mi?
- Persistence bir store/memory türü mü, yoksa state'in sınırlar aşmasıyla ilgili bir özellik mi?

Bu nedenle üçüncü batch:
**State, Work state, Environment, Workspace, Sandbox, Policy, Guardrail, Verification, Observability, Persistence**
üzerinden ilerler.

## Kaynak zemini

### Work Management / Project Control study
[U08 Cross-Unit Synthesis](../../research/studies/work-management-project-control/08-CROSS-UNIT-SYNTHESIS.md) farklı sistemlerde lifecycle status, derived standing, readiness, claim/liveness, execution-attempt state, verification/integration evidence ve actor/session failure'da korunması gereken state katmanlarını ayırıyor.

Önemli sonuç: conversation history tek başına work-control source of truth değildir; persistent state plan/specification, work graph, execution/wait state, scheduling attempts, actor identity/history ve completion/integration evidence gibi birden çok katman taşıyabilir.

### Context / Memory / Harness study
[STATE](../../research/studies/context-memory-harness-engineering/STATE.md) ve Harness araştırması:
- Context = current model-visible working set,
- Memory = cross-time lifecycle,
- Harness = model-external runtime/control substrate.

Bu batch'te State/Persistence/Observability/Verification ayrımları bunlarla çakıştırılır.

### OpenAI Agents SDK — RunState, sessions, guardrails, tracing
2026-09-18 canlı belgeler:
- Run state: https://openai.github.io/openai-agents-python/ref/run_state/
- Running agents / state management: https://openai.github.io/openai-agents-python/running_agents/
- Sessions: https://openai.github.io/openai-agents-python/sessions/
- Guardrails: https://openai.github.io/openai-agents-python/guardrails/
- Tracing: https://openai.github.io/openai-agents-python/tracing/

RunState serializable snapshot ve pause/resume boundary olarak; Session conversation history persistence olarak; Guardrails input/output/tool checks olarak; Tracing ise run olaylarının gözlemlenebilir kaydı olarak kullanılıyor. Bu framework sözleşmesi evrensel kavram standardı değildir.

### OpenAI Sandbox Agents + Carbon Layer sandboxing study
- Sandbox Agents concepts: https://openai.github.io/openai-agents-python/sandbox/guide/
- Quickstart: https://openai.github.io/openai-agents-python/sandbox_agents/
- Existing sandbox study: `research/studies/the-carbon-layer/videos/-01_NB4SbBY-agent-sandboxing/`

OpenAI workspace'i gerekli dosya/repos/mount/environment girdilerinin düzenlendiği çalışma alanı; sandbox session'ı ise komutların çalıştığı live execution environment olarak ayırıyor. Carbon Layer study sandbox seçiminde isolation mechanism ile actual file/network/credential/tool boundary'nin ayrılması gerektiğini koruyor.

### NIST — Policy
- Policy: https://csrc.nist.gov/glossary/term/policy
- Digital policy: https://csrc.nist.gov/glossary/term/digital_policy
- Access control mechanism: https://csrc.nist.gov/glossary/term/access_control_mechanism

NIST policy'yi expected/correct behavior veya access conditions belirleyen rules/statements olarak; digital policy'yi machine-executable access-control rules olarak; mechanism'i policy kararını uygulayan/enforce eden bileşen olarak ayırıyor.

## 21. State

**Çalışma tanımı:**  
> **State:** Bir entity, process veya system'in belirli bir anda continuation, decision veya control açısından anlam taşıyan mevcut durumunun temsil edilebilir bilgisi.

State tek bir status alanı değildir. Gerektiğinde:
- lifecycle position,
- current values,
- pending effects,
- interruption/approval status,
- active references,
- relevant history-derived standing

gibi unsurları içerebilir.

**Ayrımlar:**
- State ≠ Memory. State şu anki condition; Memory geçmişten geleceğe bilgi taşıyan lifecycle.
- State ≠ Context. State'in yalnız Model'e gösterilen kısmı Context'e girebilir.
- State ≠ Persistence. State bir bilgi/condition'dır; Persistence onun sınırlar aşarak korunma özelliği olabilir.
- State ≠ status. Status, State'in bir alanı olabilir.

OpenAI RunState'in serialized run snapshot olması bu ayrımı somutlaştırır.

## 22. Work state

**Çalışma tanımı:**  
> **Work state:** Belirli Work'ün ne olduğunu, şu anda nerede durduğunu, neyin tamamlandığını/açık kaldığını, hangi standing/blocker/owner/evidence ile hangi sonraki hareketlerin anlamlı veya izinli olduğunu geri kazanmak için gereken durable/current state kümesi.

Work state yalnız task status değildir. Duruma göre:
- work identity/scope,
- decomposition/dependencies,
- lifecycle status,
- derived readiness/blocked standing,
- ownership/claim,
- current plan/artifacts,
- verification/integration evidence,
- open decisions,
- next/resume information

taşıyabilir.

**Ayrımlar:**
- Work state ≠ Session history.
- Work state ≠ RunState; runtime state bunun bir alt/ilişkili yüzü olabilir.
- Work state ≠ Memory; Memory Work state'i besleyebilir ama work-control standing farklıdır.
- Work state ≠ plan. Plan Work state'in bir parçası olabilir.

Work Management study'nin “persistent state needs multiple layers” sonucu bu yerel ayrımın temel dayanağıdır.

## 23. Environment

**Çalışma tanımı:**  
> **Environment:** Actor/Agent/Runtime'ın Work'ü gerçekleştirdiği ve gözlem/eylem yaptığı dış çalışma koşulları ve erişilebilir kaynaklar bütünü; dosya sistemleri, services, network, credentials, compute, OS/runtime surfaces, external systems ve fiziksel/organizasyonel constraints içerebilir.

**Ayrımlar:**
- Environment ≠ Workspace. Workspace, Work için ayrılmış/düzenlenmiş çalışma alanıdır; Environment daha geniştir.
- Environment ≠ Sandbox. Sandbox, Environment'in execution/isolation boundary taşıyan belirli bir düzenidir.
- Environment ≠ Tool. Tool, Environment içindeki capability'ye erişim interface'i olabilir.
- Environment ≠ Runtime. Runtime Work'ü Environment içinde yürütür.

Carbon Layer study'nin “agent nerede çalışıyor, neye dokunabilir?” sorusu Environment sınırının neden load-bearing olduğunu gösterir.

## 24. Workspace

**Çalışma tanımı:**  
> **Workspace:** Belirli Work için materyallerin, dosyaların, repo/artefact'ların ve çalışma çıktılarının düzenlendiği mantıksal veya fiziksel çalışma alanı.

Workspace:
- persistent veya ephemeral olabilir,
- sandbox içinde veya dışında olabilir,
- bir Environment'in yalnız belirli görünümünü temsil edebilir.

**Ayrımlar:**
- Workspace ≠ Environment.
- Workspace ≠ Sandbox.
- Workspace varlığı isolation garantisi değildir.
- Workspace ≠ Work state; Work state workspace'te saklanabilir ama aynı şey değildir.

OpenAI Sandbox Agents'da Manifest workspace'in başlangıç içeriğini/layout'ını tanımlar; sandbox session ise live execution environment'dır.

## 25. Sandbox

**Çalışma tanımı:**  
> **Sandbox:** Work/Run execution'ının hangi files, processes, network, credentials, resources ve host/external surfaces'e hangi biçimde erişebileceğini sınırlandırmak için tasarlanmış izole veya kısıtlı execution environment/boundary.

**Ayrımlar:**
- Sandbox ≠ Workspace.
- Sandbox ≠ Environment'in tamamı; belirli bir controlled execution environment'dır.
- Sandbox ≠ Permission policy tek başına. Isolation mechanism + configuration + exposed capabilities birlikte sınırı belirler.
- Sandbox ≠ safety guarantee. İzinli external API ve valid credential sandbox dışı etki üretebilir.
- Sandbox ≠ Harness; Harness sandbox'ı seçebilir/yönetebilir.

Carbon Layer study'nin intent/containment ve local containment vs authorized remote API ayrımı burada korunur.

## 26. Policy

**Çalışma tanımı:**  
> **Policy:** Belirli bir scope içinde beklenen, izin verilen, yasaklanan veya koşula bağlanan davranış/kararları tanımlayan kural ve ilkeler bütünü.

Policy:
- prose/organizational olabilir,
- machine-readable olabilir,
- digital/machine-enforced forma çevrilebilir.

**Ayrımlar:**
- Policy ≠ Guardrail.
- Policy ≠ Permission. Permission policy'nin belirli entity/action/resource sonucunda verdiği somut izin olabilir.
- Policy ≠ enforcement. Yazılı rule uygulanmıyorsa actual control guarantee oluşmaz.
- Policy ≠ Authority; policy Authority sınırlarını tanımlayabilir.

NIST policy ve digital policy ayrımı, “kural” ile “machine executable/enforced rule” arasındaki farkı destekler.

## 27. Guardrail

**Çalışma tanımı:**  
> **Guardrail:** Bir input, output, Tool action veya başka execution event'ini Policy/criteria/risk koşullarına göre kontrol eden ve gerektiğinde block, reject, tripwire, transform veya escalation üreten aktif kontrol mekanizması.

**Ayrımlar:**
- Guardrail ≠ Policy. Policy ne olması gerektiğini söyler; Guardrail belirli execution point'te bunu check/enforce etmeye çalışır.
- Guardrail ≠ Verification. Guardrail execution control'dür; Verification daha geniş biçimde claim/effect/outcome doğruluğunu değerlendirebilir.
- Guardrail ≠ Sandbox. Guardrail semantic/policy check yapabilir; Sandbox capability/containment boundary sağlar.
- Guardrail kapsamı execution coverage'a bağlıdır; bir guardrail bulunması her path'in korunduğunu kanıtlamaz.

OpenAI Agents SDK input/output/tool guardrails ve workflow-boundary limits bu ayrımı somutlaştırır.

## 28. Verification

**Çalışma tanımı:**  
> **Verification:** Bir claim, artefact, completion signal, state transition veya observed effect'in tanımlı kriter/expected property/evidence karşısında gerçekten desteklenip desteklenmediğini değerlendirme süreci.

Verification:
- deterministic test/check,
- independent review,
- external evidence,
- qualified evaluator
gibi farklı oracle/mechanism'ler kullanabilir.

**Ayrımlar:**
- Verification ≠ Observability. Görmek/kaydetmek doğru olduğunu kanıtlamaz.
- Verification ≠ Guardrail. Guardrail execution sırasında belirli risk/kural check'i; Verification daha geniş sonuç/claim değerlendirmesi.
- Verification ≠ validation of user goal; gerekli olduğunda end-to-end validation ayrıca yapılır.
- completion signal ≠ verified effect ≠ desired outcome.

Work Management study bu son ayrımı doğrudan korur.

## 29. Observability

**Çalışma tanımı:**  
> **Observability:** Bir System/Run/Workflow'un fiilen ne yaptığı, hangi event/state transition/Tool call/Handoff/Guardrail/failure'ın oluştuğu hakkında telemetry, traces, logs ve inspectable state üzerinden yeterli görünürlük elde edebilme özelliği.

**Ayrımlar:**
- Observability ≠ Verification.
- Observability ≠ logging. Log bir mekanizma olabilir; observability karar/diagnosis için yeterli görünürlük sorusudur.
- Observability ≠ transparency of reasoning; internal chain-of-thought erişimi gerektirmez.
- Trace bulunması bütün external effects'in gözlemlendiğini kanıtlamaz.

OpenAI Tracing, LLM generations, Tool calls, handoffs, guardrails ve custom events kaydıyla concrete observability surface örneğidir.

## 30. Persistence

**Çalışma tanımı:**  
> **Persistence:** Belirli State, Memory, Work state, artefact veya identity-linked bilginin bir Run/process/session/runtime sınırı sona erdikten sonra da saklanıp daha sonra geri alınabilmesini sağlayan süreklilik özelliği/mekanizması.

**Ayrımlar:**
- Persistence ≠ Memory. Memory persistent olabilir; her persistent state Memory değildir.
- Persistence ≠ Session. Session persistence sağlayabilir ama persistence daha genel özelliktir.
- Persistence ≠ database. Database bir storage mechanism olabilir.
- Persistence ≠ continuity'nin tamamı. Bilginin kalması, doğru yeniden bağlanacağı veya güncel olduğu garantisi değildir.

OpenAI Session persistent conversation layer ve RunState serialization örnekleri ile Work Management study'nin durable multi-layer state bulguları bu ayrımı destekler.

## Üçüncü batch ilişki haritası

```text
Environment
├── contains/accesses → Workspace
├── may provide → external Systems / Network / Credentials / Compute
└── may contain → Sandbox
    └── constrains → Runtime / Processes / Files / Network / Resources

Workspace
└── holds → Work artefacts / files / outputs
    └── may persist → Work state

Policy
├── defines → expected / allowed / forbidden behavior
├── may determine → Authority / Permission rules
└── may be enforced-by → Guardrail / Sandbox / Runtime controls

Guardrail
└── checks/enforces-at → input / output / Tool / execution boundaries

State
├── has-specialization → Work state
├── may be persisted-via → Persistence mechanisms
└── may be exposed-as → Context

Work state
├── includes → standing / blockers / ownership / evidence / next-resume
├── may be stored-in → Workspace / external store
└── persists-across → Runs / Sessions / Actors

Persistence
├── preserves → State / Work state / Memory / Identity-linked data
└── enables → recovery / resume / continuity

Observability
└── exposes → events / transitions / Tool calls / Handoffs / Guardrails / failures
    └── supplies-evidence-to → Verification

Verification
└── evaluates → claims / effects / completion / artefacts
    against → criteria / evidence / oracle
```

## v0.2 üzerinde yapılan fine-tune'lar

### Harness
Harness'ın kapsamı daha açık:
- Runtime'ı içerebilir/konfigüre edebilir,
- Policy/Guardrail/Sandbox gibi control surfaces'i bağlayabilir,
- Observability/Verification yüzeylerini sağlayabilir.

Ama bunların hiçbiri Harness ile eşit değildir.

### Environment / Capability
Capability tanımı artık daha açık okunur:
> Capability = Actor/Agent/System'in Model + Tool + Runtime + **Environment** koşulları altında fiilen yapabildiği şey.

Bir Environment değişikliği Capability'yi değiştirebilir, Agent tanımı değişmese bile.

### Authority / Permission / Policy
- Policy kuralları tanımlar,
- Authority meşru sorumluluk/decision scope,
- Permission spesifik action/resource izni,
- Guardrail/Runtime/Sandbox bu sınırların bir kısmını enforce edebilir.

### Session / Memory / Persistence / Work state
- Session = conversation/run continuity container,
- Memory = future decisions'i besleyen cross-time knowledge/state,
- Persistence = bilginin boundary ötesinde korunabilme özelliği,
- Work state = Work'ün current standing ve continuation bilgisi.

Bu dört kavram artık farklı eksenlerdedir.

### Verification / Observability
- Observability = ne olduğunu görebilmek/reconstruct edebilmek.
- Verification = olanın/iddianın kriteri gerçekten karşılayıp karşılamadığını değerlendirmek.

Trace görmek verification değildir.

## Çakışma kontrolleri

1. State ≠ status.
2. State ≠ Memory.
3. Work state ≠ Session history.
4. Work state ≠ RunState.
5. Workspace ≠ Environment.
6. Workspace ≠ Sandbox.
7. Sandbox ≠ safety guarantee.
8. Policy ≠ Guardrail.
9. Policy ≠ enforcement.
10. Guardrail ≠ Sandbox.
11. Guardrail ≠ Verification.
12. Observability ≠ Verification.
13. Persistence ≠ Memory.
14. Persistence ≠ Session.
15. Persistence ≠ database/storage product.

## Bu batch'in açtığı sonraki kavramlar

- Goal
- Intent
- Plan
- Task / Work item
- Dependency
- Readiness
- Completion
- Validation
- Evaluation
- Evidence

Bunlar sonraki batch için adaydır; zorunlu sıra değildir.
