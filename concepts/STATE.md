# Concepts — Güncel çalışma durumu

2026-09-20, **B6-T12**. Bu dosya araştırma bazlı terim/jargon çıkarımının global amaç, yetki, güncel iş ve devam kaynağıdır. Kaynak araştırmaların STATE dosyaları veya yerel READING/kullanım kayıtlarının yerine geçmez.

## 1. Güncel durum

**PILOTS-AND-B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / CMH-DURABLE-COMPLETE / SUPERPOWERS-DURABLE-COMPLETE / AI-KNOWLEDGE-STRATEGIES-DURABLE-COMPLETE / MULTI-AGENT-PATTERNS-DURABLE-COMPLETE / METHOD-v0.3-WORKING / POST-S1-ADDITIONS-PENDING-ACCOUNT.**

Kullanıcının “tamam. devam et lütfen.” talebiyle `research/studies/multi-agent-patterns/` package'i canonical preflight'tan geçirildi, current package yapısı recover edildi, üç source file tam okundu ve bağlamlı kullanım envanteri kalıcılaştırıldı. **Concepts açısından 3/3 package source file full-read ve durable extraction complete durumundadır.**

Bu package'in ayrı `STATE.md` veya `INDEX.md` dosyası yoktur; `META.md` bunu explicit biçimde kaydeder ve iki entry point verir. Bu nedenle başka package'lerin cold-start şeması buraya zorla uygulanmadı.

| İş | Güncel durum |
|---|---|
| Amaç, iki risk, başlangıç hazırlığı | Tamamlandı; ORIGIN/SETUP-REVIEW tarihsel kaynak. |
| B1/B2 ve B3/B4 | İki konuşma pilotu ve yöntem değerlendirmeleri tamam. |
| B5 | SCOPE/S1 başlangıç kapsamı ve delta ilkeleri teslim edildi. |
| B6 — CMH | Durable-complete. |
| B6 — Superpowers | Durable-complete. |
| B6 — AI Knowledge Strategies | Durable-complete. |
| B6 — Multi-Agent Patterns | **Durable-complete; 3/3 source file, READING + TERMS.** |
| B6 — sıradaki paket | **anthropic-ai-native-sdlc-playbook**; concepts çıkarımı henüz başlamadı. |
| B6 — diğer S1 birimleri | Başlangıç sırası SCOPE'da; kalıcı çıkarımları kapanmadı. |
| S1 sonrası eklenen kaynaklar | agentmemory, claude-swap, cli-continues ve ponytail bilinen kapsam deltalarıdır; final scope/B7 öncesi hesapta işlenecekler. |
| B7/B8 | Küresel geçiş kontrolü ve ortak referans değerlendirmesi başlamadı. |

S1 başlangıcından **CMH, Superpowers, AI Knowledge Strategies ve Multi-Agent Patterns** kalıcı çıkarım bakımından kapanmıştır. Bu paket sayısı ilerleme yüzdesi değildir ve post-S1 additions'ı içermez.

## 2. Etkin giriş ve sıradaki yetkili iş

Multi-Agent Patterns artık current partial work değildir. Gerekirse [READING.md](studies/multi-agent-patterns/READING.md) ve [TERMS.md](studies/multi-agent-patterns/TERMS.md) birlikte okunur; package yeniden araştırılmaz.

**Sıradaki yetkili iş B6-T13:** `research/studies/anthropic-ai-native-sdlc-playbook/` package'ine canonical preflight ile gir:
- current main ve gerçek package tree/file envanterini sabitle;
- package META/STATE/INDEX mevcutsa current authority/cold-start yolunu recover et; yoksa bunu explicit kaydet;
- kaynak araştırmanın current/historical durumunu concepts extraction durumundan ayır;
- bütün source files'i tam oku;
- terim/jargon/kavramsal ayrımları kaynağın kendi kullanımında çıkar;
- gerekirse `concepts/studies/anthropic-ai-native-sdlc-playbook/READING.md` ve `TERMS.md` oluştur;
- önceki paketlerin agent/orchestrator/harness/workflow kavramlarını başlangıç ontology'si olarak dayatma.

B7/B8 ortak referans aşaması hâlâ yetkili next değildir. S1 sonrası eklenmiş study yolları bütün seri ve delta kontrolünden dışlanamaz.

## 3. Amaç, derinlik ve iki risk

İlk aşama research/studies araştırmalarını tam okuyarak her birinin kendi bağlamında kullanım ve ilişkilerini çıkarmaktır. İkinci aşama bütün çıkarımları tam okuyup ortak referansı değerlendirmektir. İlk pilotun/CMH'nin şeması, hazır sözlük veya kullanıcının açıklayıcı örnekleri sonraki paketlere başlangıç ontolojisi yapılmaz. Kaynakta tanım bulunması veya concepts'e yazılması ortak kabul değildir.

Her concepts turunda iki neden kısa ve görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişiklik izlenebilir olmalı. Ortak sözcükler aynı anlamı garanti etmiyor; kullanıcı onayı, kaynak kullanımı ve assistant yorumu teknik doğruluk yerine geçmemeli. Kullanıcı teknik uzman oracle değildir; ham düşünce değil, denetlenebilir sonuç ve kısa gerekçe gerekir.

Kaynağın genel tanım vermediği kullanımı açık bırakmak geçerli çıktıdır; okunmamış dosya veya atlanmış açıklama gerçek eksiktir. Yalnız genel bilgiyi artıracak ve mevcut aktarımı değiştirmeyecek okuma eklenmez. Açık kaynak soruları kendiliğinden yeni deney/literatür borcu olmaz. Talimat, kod anlatımı, geçmiş yerel deney, dış yazar raporu, sentez ve yeni yorum ayrılır; tekrar bağımsız destek değildir.

P2'nin önceki gruplarındaki özgün satırlar kalıcı aktarım sırasında erişilebilir olduğu ölçüde kullanıldı; B6-T10'da tarihsel SP150–SP160 satır metni güvenilir biçimde recover edilemedi. METHOD §8 uygulanarak sabit kaynaktan U08-R regeneration yapıldı; STATE/summary'den birebir SP anlamı uydurulmadı. Tam ve değişmemiş gerçek içerik sırf yeni tur diye mekanik tekrarlanmaz; eksik zorunlu kontrol veya kaynak canonical yoldan geri kazanılır.

## 4. B6-T12 gerçek çalışma ve Multi-Agent Patterns kapanışı

B6-T12 başlangıç main'i **ee763da635d8b147ddcbdf787a22a7dd3edc8d2f** idi. Source package current main'de üç dosyadan oluşuyordu:

- `META.md`;
- `CONVERSATION-SYNTHESIS.md`;
- `SOUL-DEVELOPMENT-OS-ASSESSMENT.md`.

`META.md` ayrı package `STATE.md` olmadığını explicit biçimde belirtir. Package status: triggering conversation için exploratory systems assessment complete; Foundation veya architecture'a promote edilmemiş.

Üç dosyanın tamamı B6-T12'de full-read edildi. Yeni kalıcı kayıtlar:
- `concepts/studies/multi-agent-patterns/READING.md`;
- `concepts/studies/multi-agent-patterns/TERMS.md`.

TERMS şu source-native/project-synthesis ayrımlarını korur:
- Sequential = dependency/execution ordering;
- Parallel = concurrency; decomposition ve redundancy/ensemble ayrı;
- Hierarchical = delegation/authority/coordination topology;
- Generator–Critic = production/challenge relation; critic ≠ independent verifier;
- Human-in-the-Loop = human authority/judgement insertion; human approval ≠ technical verification;
- Composite = conditional composition; universal mega-workflow değil;
- Router, Manager ve Orchestrator ayrı questions/functions taşır;
- Agent/Subagent/Thread/Session ayrı operational boundaries;
- epistemic independence agent count'tan ayrı;
- review, verification ve adversarial challenge ayrı;
- Work topology, Actor topology, authority/capability/accountability ve Environment feasibility ayrı;
- system formation / minimum sufficient topology project-facing synthesis statüsünde tutulur.

Assessment'in C1–C10 candidate requirements ve R1–R10 risk register'ı accepted architecture olarak promote edilmedi. 2026-09-03 Codex/Claude Code product observations source'un kendi time-sensitive sınırıyla tutuldu; current product claim olarak yeniden doğrulanmış sayılmadı. MCP/A2A lower-image bölümü kaynakta substantively değerlendirilmediği için concepts tanımı üretilmedi.

Source-side coverage kontrolünde 3/3 source file ve bütün ana sections TERMS'e bağlandı; unread source file veya somut aktarım borcu kalmadı. Kapanış aynı-assistant source extraction'dır; independent verification veya universal multi-agent taxonomy sertifikası değildir.

## 5. Yetki ve yazma kapsamı

B6-T12 mevcut seri çıkarım yetkisi içindedir; yeni research phase, Foundation synthesis veya architecture work değildir.

Bu tur dört concepts yolu değişir:
- yeni `concepts/studies/multi-agent-patterns/READING.md`;
- yeni `concepts/studies/multi-agent-patterns/TERMS.md`;
- `concepts/INDEX.md` — durable package kaydı eklendi;
- bu `concepts/STATE.md`.

Özgün `research/studies/multi-agent-patterns/**`, diğer studies, önceki durable package kayıtları, METHOD/PLAN/SCOPE/CHARTER/ORIGIN/SETUP-REVIEW, Foundation ve agent-control bu iş adına değiştirilmez.

## 6. Değişen korpus ve değişmez devam kayıtları

SCOPE/S1 başlangıç ref'i ve post-S1 delta ilkeleri değişmedi. Bilinen yeni study yolları `agentmemory`, `claude-swap`, `cli-continues`, `ponytail` olarak açık kalır; yeni yollar eklenirse final tree-delta hesabına aynı ilkeyle dahil edilir.

B6-T12 başlangıcından bu STATE öncesine kadar yapılan writes concepts katmanıyla sınırlıdır:
- Multi-Agent READING create commit **78fb6cc68e0b123eb614c43f5cb17ae8d71d41a0**;
- Multi-Agent TERMS create commit **7d3e4894662cee5d64292ada76b970041c3575ee**;
- concepts INDEX update commit **c25815337eb04cfabbefabf9c41dc7dd5c25b0af**.

Source package blob identities yerel READING'de korunur. Product-specific depth/concurrency/CLI notları daha sonraki load-bearing kullanımda current first-party source'tan revalidate edilmelidir.

| Değişmez kayıt | Korunan kapsam |
|---|---|
| P1/P2 pilot checkpoints | METHOD v0.3'e gelen yöntem kanıtı. |
| CMH durable closure | İlk kalıcı package. |
| Superpowers B6-T10 durable closure | 52/52 source package. |
| AI Knowledge Strategies B6-T11 durable closure | 9/9 source package. |
| Multi-Agent Patterns B6-T12 READING | 3/3 current package source account ve no-STATE/INDEX boundary. |

Eski package handoff/“next” cümleleri chronological research history'dir; current concepts next work global STATE'den alınır.

## 7. Yayın kontrolü ve yeni oturum

Yeni READING ve TERMS main'den geri okunup içerik/bağlantı/kapanış tutarlılığı kontrol edilir; INDEX'in yeni satırı gerçekten durable path'lere yönlenmelidir. Bu STATE kendi henüz bilinmeyen commit'ini uydurmaz. Yayından sonra actual diff ve main placement kontrolü yapılır.

Yeni oturum cold-start: AGENT + triggered protocols → concepts/INDEX zorunlu dosyaları → bu STATE → **anthropic-ai-native-sdlc-playbook package preflight**. Multi-Agent Patterns yalnız durable-complete source olarak gerektiğinde geri çağrılır. B7/B8 hâlâ ileriki aşamadır.

