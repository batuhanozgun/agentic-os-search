# Concepts — Güncel Durum

## Güncel mola ve yön değerlendirmesi — 2026-09-18

**Güncel durum:** YENİ TERİM / BATCH GENİŞLEMESİ DURDURULDU. Kullanıcı, konuşmanın ve repository'nin yeniden okunmasını, konunun toparlanmasını ve yönün ortaya konmasını istedi; drift riski uyarısı yaptı.

**Son kullanıcı yönü:** “Burada bir mola ver, şimdi konuşmayı baştan sona tam okuma yap, repoyu da oku. Konuyu toparlaman ve yönü ortaya koyman lazım. drift yapmaya başlamak üzeresin.”

Bu yön, aşağıdaki son yayın kaydının ve diğer girişlerdeki sonraki-batch adaylarının önündedir. Outcome ile başlayan liste otomatik sıradaki iş değildir. Mevcut 40 maddelik v0.4 korunur; bütün maddelerin kaynak doğrulaması ve birlikte kullanım sınaması tamamlanmış sayılmaz. Yeni terim, v0.5, kabul edilmiş referans veya SOUL/Development OS kararı bu mola kaydıyla üretilmez.

**Bu turun kapsamı:** Amaç/yöntem/çıktı tutarlılığını incelemek ve kullanıcıya gerekçeli yön değerlendirmesi sunmak. İncelenen yayın tabanı `b750e4a020114b7a158b37d98513f3fa0f6b6535`; concepts altındaki 23 dosya tam geri okundu. Bu, bütün Foundation/studies corpus'unun veya geçmişte anılan bütün dış kaynakların yeniden doğrulandığı anlamına gelmez.

**Assistant'ın değerlendirme yönü; yeni uygulama planı kabulü değil:** Bağlı kavramlarla ilerleme korunmalı; terim sayısını büyütmek yerine mevcut anlamların somut kullanımları ve kaynakla ilişkisi sınanmalı. Güncel yönlendirmelerin eski v0.1'e dönmesi, yöntem/planın son kullanıcı iş devrini tam taşımaması, kısa tanımlarda kapsam kaybı ve ayrım listelerinin gerçek çakışma testi gibi sunulması gözden geçirilmelidir. Son batch'lerdeki canlı-kaynak okuma iddiaları yalnız URL/tarih kaydından doğrulanmış kabul edilmemelidir.

Kullanıcı daha önce çalışma tanımlarını assistant'ın seçip ilişkili kavramlarla ilerlerken düzeltmesini istedi; bu mola tek tek terim onayı döngüsüne dönüş gerekçesi değildir. Sonraki sorumluluk, yön değerlendirmesini ele almaktır; yeni bir 10'luya kendiliğinden geçmek değildir. Bu kayıt yalnız güncel durdurma ve değerlendirme sınırını korur; yöntem, tanımlar ve eski araştırma gövdeleri bu tur yeniden yazılmaz.

## Mola öncesindeki son yayın kaydı

Aşağıdaki bölüm v0.4 yayınının tarihsel durumunu korur; yeni devam yetkisi değildir.

**Kayıt tarihi:** 2026-09-18.  
**Mevcut iş:** Dördüncü 10-terim batch'i tamamlandı; toplam 40 terim için working local reference v0.4 hazırlandı. Bu turun dönüş noktası sonucu kullanıcıya sunmaktır.  
**Yöntem:** [METHOD v0.2](METHOD.md) — bağlantılı batch + ilişki haritası + çakışma üzerinden fine-tune.  
**Mevcut araştırma:** [U03](research/U03-CORE-TERMS-BATCH1.md) + [U04](research/U04-CORE-TERMS-BATCH2.md) + [U05](research/U05-CORE-TERMS-BATCH3.md) + [U06](research/U06-CORE-TERMS-BATCH4.md).  
**Aktif working reference:** [CORE-TERMS-WORKING-v0.4](synthesis/CORE-TERMS-WORKING-v0.4.md).  
**ACCEPTED reference:** Henüz yok; tek tek terim onayı beklenmez.

## Working reference kapsamı — 40 terim

### Batch 1
Agent; Model; LLM; Actor; Role; Run; Session; Workflow; Tool; Harness.

### Batch 2
Runtime; Context; Memory; Identity; Capability; Authority; Permission; Orchestration; Handoff; Subagent.

### Batch 3
State; Work state; Environment; Workspace; Sandbox; Policy; Guardrail; Verification; Observability; Persistence.

### Batch 4
Intent; Goal; Plan; Task / Work item; Dependency; Readiness; Completion; Validation; Evaluation; Evidence.

## v0.4'ün en önemli yeni sınırları

- **Intent ≠ Goal ≠ Plan** — amaçlanan yön / explicit target / proposed route.
- **Work item ≠ Run** — yönetilen Work birimi / tek execution olayı.
- **Dependency ≠ hierarchy ≠ generic relation** — control/validity/timing/closure etkisi olan typed relation.
- **Readiness ≠ priority ≠ open status** — belirli next action için derived admissibility/actionability standing.
- **Completion ≠ Verification ≠ Validation** — lifecycle closure / specified claim doğrulama / intended-use ve Goal uygunluğu.
- **Evaluation ≠ Verification ≠ Validation** — systematic performance/quality/risk assessment ayrı eksen.
- **Evidence ≠ truth ≠ Observability** — traceable ground / conclusion değil / observability evidence üretebilir.

## Güncel Work-success hattı

```text
Intent
└── clarified-as → Goal
      ├── guides → Plan
      ├── target-for → Validation
      └── measured/judged-by → Evaluation

Plan
├── decomposes → Work items
├── proposes → Dependencies / sequencing / Actors
└── revised-by → Evidence / State / discovered Work

Work item
├── may depend-on → Work item / Artefact / Decision / external condition
├── has-derived → Readiness
├── progresses-through → Work state
└── may reach → Completion
                    │
                    ├── may trigger → Verification
                    └── does NOT imply → Goal achievement / Validation

Observability ─produces→ Evidence
Evidence
├── supports/challenges → Verification
├── supports/challenges → Validation
└── feeds → Evaluation

Verification ─asks→ specified claim/requirement satisfied?
Validation ─asks→ intended use / Goal / need satisfied?
Evaluation ─asks→ how well / under what criteria / at what risk?
```

## Büyük haritayla birleşim

Bu yeni Work-success hattı v0.3'teki execution/control/state haritasına bağlanır:

- Plan ve Work items → Work state içinde current standing üretir.
- Dependency → Readiness'i etkiler.
- Readiness → Orchestration/Runtime admission kararlarını etkileyebilir.
- Actor/Authority/Permission → hangi Work item'ın kim tarafından hangi koşulla yürütülebileceğini etkiler.
- Environment/Capability → dispatch/readiness'i etkileyebilir.
- Completion → Verification veya Validation'ın yerine geçmez.
- Observability → Evidence üretir; Evidence → Verification/Validation/Evaluation besler.
- Persistence → Plan/Work state/Evidence'in session/run sınırlarını aşmasını sağlar.

## Yeni oturumda devam yolu

Güncel AGENT ve gereken protokoller → [INDEX](INDEX.md) → bu STATE → [METHOD](METHOD.md) → [working v0.4](synthesis/CORE-TERMS-WORKING-v0.4.md). Ayrıntılı kanıt gerekirse U06 → U05 → U04 → U03 → Agent U01/U02.

Yeni oturum bu 40 terimi tek tek kullanıcıya sormaz. v0.4'ü working map olarak kullanır ve yalnız yeni batch/gerçek kullanım çakışması olduğunda ilgili sınırları yeniden açar.

## Sonraki batch için doğal adaylar

- Outcome
- Success criterion
- Requirement
- Constraint
- Acceptance criterion
- Metric
- Benchmark
- Oracle
- Review
- Approval

Bunlar zorunlu sıra değildir; v0.4 haritasında en fazla ayrım temizleyecek kombinasyon seçilir.

## Yayın durumu

**Yayın:** [PR #26](https://github.com/batuhanozgun/agentic-os-search/pull/26); branch `research/concepts-core-terms-batch4-20260918`; exact head `9e74c91930f057d694761e99ea7083216f7e6831`; main merge commit `051ed2c848edda8493fd27051a794abad4628534`.

Sekiz concepts yolu değişti: yeni U06 ve working v0.4; v0.3 historical snapshot işareti; research/synthesis/reference index, envanter ve bu STATE. Agent-control, Foundation, studies paketleri ve explorations değişmedi.

PR merge öncesi `mergeable=true` idi. Exact head'e bağlı normal merge başarılı oldu; head → merge karşılaştırması sıfır dosya farkı verdi. Working v0.4 ve U06 main üzerinden yayımlandı.

Bu yayın tanımların evrensel doğruluğunu veya ileride hiç değişmeyeceğini kanıtlamaz. v0.4 evolving working reference olarak kullanılacak ve sonraki batch/gerçek kullanım çakışmalarıyla fine-tune edilecektir. ACCEPTED reference hâlâ yoktur.

## Korunan geçmiş

- v0.1–v0.3 tarihsel snapshots olarak korunur.
- Agent boundary adayı daha eski ara sentezdir.
- v0.2 yöntem, P0 ve yayın doğrulama geçmişleri checks/STATE kayıtlarında korunur.
