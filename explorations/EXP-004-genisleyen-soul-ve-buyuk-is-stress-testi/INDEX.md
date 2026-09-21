# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

**Tür:** Kavramsal diyalog + araştırma yeniden-kullanımı + sentetik büyük-iş stress testi.  
**Kaynak oturum:** 20–21 Eylül 2026; tekil mesaj saatleri üretilmez.  
**Kaynak kesimi:** U001–U014 ve S001–S013: 27 substantive kaynak mesaj. U014 repository'ye kayıt yetkisidir.  
**Önceki denemeler:** [EXP-001](../EXP-001-soul-calisma-modeli/INDEX.md) → [EXP-002](../EXP-002-soul-baz-yapi-ve-entelektuel-taban/INDEX.md) → [EXP-003](../EXP-003-ek-hafiza-ve-arastirma-temelli-guvenilirlik/INDEX.md).  
**Arşiv durumu:** [STATE](STATE.md).

## Bu denemenin konusu

Kullanıcı, Foundation ve studies birikimini kullanarak SOUL'un büyük, uzun soluklı ve baştan tamamen bilinmeyen bir işi yapmak için nasıl bir çalışma yapısına ihtiyaç duyacağını düşünmek istedi. Başlangıçta agent'lar, roller, ortadaki iş, iş akışı/plan ve memory adayları vardı. Konuşma boyunca bu beşli doğrudan mimariye çevrilmedi; Foundation'ın Work / Actors / Information / Environment ground'ları ve Composition sonuçları ile candidate studies'teki mekanizma/failure-mode'lar kullanılarak model art arda stress-test edildi.

Sentetik test nesnesi, bir eğitim yılı boyunca kullanılacak kapsamlı bir 4. sınıf matematik soru bankasını üretme, yayımlama ve sürdürülebilir biçimde işletme gibi büyük bir programdır. Amaç eğitim ürünü tasarlamak değil, SOUL çalışma modelini kırmaya çalışmaktır. Ülke, gerçek müfredat, mevzuat veya gerçek kullanıcı grubu seçilmedi; dış domain iddiaları bu denemenin bulgusu değildir.

## En kısa güncel model

Konuşmanın sonunda güçlü çalışma hipotezi şuna dönüştü:

```text
BASE SOUL
   │
   │ Mission ve Work ile karşılaşır
   │ Work keşfeder / admit eder
   │ Actors, Information ve Environment düzenini oluşturur
   │ Binding / Standing / Control / Transition ilişkilerini kurar
   │ verification / recovery / adaptation organları ekler
   ▼
EXPANDED SOUL / WORKING SYSTEM
   │
   └─ iş ilerledikçe yeniden genişler, daralır veya yeniden yapılandırılır
```

SOUL ile “SOUL'un ürettiği sistem” sözlü olarak ayrılabilir; fakat bu deneme kesiminde aralarında zorunlu sert bir kopuş kurulmadı. Baz SOUL'un işi yapmak için kendi çalışma organizmasını genişletmesi daha güçlü hipotez haline geldi.

Foundation düzeyindeki mevcut ayrımlar stress test boyunca kırılmadı:

```text
Work
Actors
Information
Environment

+

Binding
Standing / Qualification
Control / Constraint
Transition / Effect / Feedback
```

Bu sonuç yeni Foundation doğrulaması değildir; aynı assistant'ın sentetik vakada mevcut araştırmayı kullanarak yaptığı kavramsal stress testidir.

## Test boyunca belirginleşen yaşam döngüsü

```text
Intent
→ Mission qualification
→ Need / required-condition discovery
→ Work discovery
→ Work formation / admission
→ readiness / actionable frontier
→ capability / role / Actor formation
→ Actor-specific context formation
→ Environment/capability materialization
→ execution attempt
→ realized-effect readback
→ evidence formation
→ qualification / verification
→ acceptance / progression
→ integration / delivery
→ outcome observation
→ Mission standing
→ new Work / recovery / adaptation
↺
```

Bu evreler zorunlu tek bir linear pipeline veya ayrı software modülleri değildir. Aynı çalışma farklı yollar izleyebilir; bazı evreler paralel, iç içe veya tekrar eden Work olabilir.

## Hangi okuma için geldin?

| İhtiyaç | Yol |
|---|---|
| Konuşmayı baştan sona okumak | [Diyalog INDEX](sources/conversation/INDEX.md) → U001/S001 … U014 |
| Bütünlüklü model ve stress-test özeti | [CONSOLIDATION](artifacts/CONSOLIDATION.md) |
| Kaynak bağlı kazanımlar | [LEARNINGS](reflections/LEARNINGS.md) |
| Görüş nasıl değişti? | [EVOLUTION](reflections/EVOLUTION.md) |
| Terimler bu konuşmada hangi geçici anlamda kullanıldı? | [TERMS](reflections/TERMS.md) |
| Güçlü ifadelerin sınırları | [QUALIFICATIONS](reflections/QUALIFICATIONS.md) |
| Açık kalan sorular | [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md) |
| “Mission composite miydi / actionable frontier / Run / Qualification Case / persistence ≠ continuity” gibi hattı bulmak | [TOPIC-MAP](retrieval/TOPIC-MAP.md) |
| Önceki denemelerle birlikte okumak | [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md) |
| Foundation / studies yeniden-kullanımı | [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md) |
| Aktarım ve arşiv sınırı | [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md) |

## Yanlış devralınmaması gerekenler

- Bu konuşma SOUL mimarisini kabul etmedi ve Development OS implementasyonu başlatmadı.
- Matematik soru bankası gerçek ürün planı, eğitim araştırması veya domain recommendation değildir.
- “Baz SOUL işe göre genişler” güçlü bir çalışma hipotezidir; ürün/runtime kanıtı değildir.
- `Run / Execution Attempt` ve `Qualification Case` stress testinden çıkan aday runtime/work nesneleridir; kabul edilmiş schema/primitive değildir.
- Need/Condition, Work, plan, role, Actor, context, memory, readiness, verification ve acceptance ayrımları bu denemede yararlı oldu; bunların tek evrensel veri modeli olduğu kanıtlanmadı.
- Foundation'ın dört ground + Composition yapısının bu sentetik testte kırılmaması exhaustive adequacy veya bağımsız doğrulama değildir.
- Repository araştırmaları bu denemeye mekanizma ve counterexample sağladı; study'nin varlığı o mekanizmanın SOUL'a benimsenmesi anlamına gelmez.

## Sonraki kullanım

Bu paket, bir sonraki exploration turunun aynı noktadan devam etmesini sağlar. Doğal sonraki stress hattı Feedback / Learning / Persistent Adaptation ve ardından farklı bir büyük-domain karşı testi olabilir. Bunlar otomatik next authorised work değildir. Gerçek mimari/Development OS geçişinde ilgili target repository state'i ve güncel kullanıcı yetkisi ayrıca recover edilir.
