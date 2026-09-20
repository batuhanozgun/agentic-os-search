# Concepts — Güncel çalışma durumu

2026-09-20, **B6-T14**. Bu dosya araştırma bazlı terim/jargon çıkarımının global amaç, yetki, güncel iş ve devam kaynağıdır. Kaynak araştırmaların STATE dosyaları veya yerel READING/kullanım kayıtlarının yerine geçmez.

## 1. Güncel durum

**PILOTS-AND-B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / CMH-DURABLE-COMPLETE / SUPERPOWERS-DURABLE-COMPLETE / AI-KNOWLEDGE-STRATEGIES-DURABLE-COMPLETE / MULTI-AGENT-PATTERNS-DURABLE-COMPLETE / ANTHROPIC-AI-NATIVE-SDLC-DURABLE-COMPLETE / GSTACK-DURABLE-COMPLETE / METHOD-v0.3-WORKING / POST-S1-ADDITIONS-PENDING-ACCOUNT.**

Kullanıcının “tamam. devam et lütfen.” talebiyle `research/studies/gstack/` package'i canonical preflight'tan geçirildi. Kök kayıtlar, inventory, later revalidation ve on dört synthesis dahil **23/23 source file tam okundu**; büyük iki synthesis'te tool truncation görülen aralıklar ayrı overlapping reads ile tamamlandı. Package'in bağlamlı kullanım envanteri ana TERMS + beş linked topic part olarak kalıcılaştırıldı.

| İş | Güncel durum |
|---|---|
| Amaç, iki risk, başlangıç hazırlığı | Tamamlandı; ORIGIN/SETUP-REVIEW tarihsel kaynak. |
| B1/B2 ve B3/B4 | İki konuşma pilotu ve yöntem değerlendirmeleri tamam. |
| B5 | SCOPE/S1 başlangıç kapsamı ve delta ilkeleri teslim edildi. |
| B6 — CMH | Durable-complete. |
| B6 — Superpowers | Durable-complete. |
| B6 — AI Knowledge Strategies | Durable-complete. |
| B6 — Multi-Agent Patterns | Durable-complete. |
| B6 — Anthropic AI-Native SDLC | Durable-complete. |
| B6 — gstack | **Durable-complete; 23/23 source file, READING + ana TERMS + beş linked TERMS parçası.** |
| B6 — sıradaki paket | **hermes-agent**; concepts çıkarımı henüz başlamadı. |
| B6 — diğer S1 birimleri | Başlangıç sırası SCOPE'da; kalıcı çıkarımları kapanmadı. |
| S1 sonrası eklenen kaynaklar | agentmemory, claude-swap, cli-continues ve ponytail bilinen kapsam deltalarıdır; final scope/B7 öncesi hesapta işlenecekler. |
| B7/B8 | Küresel geçiş kontrolü ve ortak referans değerlendirmesi başlamadı. |

S1 başlangıcından **CMH, Superpowers, AI Knowledge Strategies, Multi-Agent Patterns, Anthropic AI-Native SDLC ve gstack** kalıcı çıkarım bakımından kapanmıştır. Bu paket sayısı ilerleme yüzdesi değildir ve post-S1 additions'ı içermez.

## 2. Etkin giriş ve sıradaki yetkili iş

gstack artık current partial work değildir. Geri çağrılacaksa [READING.md](studies/gstack/READING.md), [TERMS.md](studies/gstack/TERMS.md) ve ana TERMS'in bağladığı beş parça birlikte okunur:

- WORK-DELIVERY;
- RUNTIME-CONTROL;
- EVIDENCE-CONTINUITY;
- COORDINATION-PORTABILITY;
- SYSTEM.

**Sıradaki yetkili iş B6-T15:** `research/studies/hermes-agent/` package'ine canonical preflight ile gir:
- current main ve gerçek package tree/file envanterini sabitle;
- package STATE/META/INDEX ve kendi cold-start/research-plan yolunu tam recover et;
- source-study current status ile concepts extraction status'u ayır;
- package'in bütün source files'ini tam oku; mevcut Hermes research devam talimatlarını current assistant authority sanma;
- terim/jargon/kavramsal ayrımları Hermes araştırmasının kendi kullanımında çıkar;
- package büyüklüğüne göre `concepts/studies/hermes-agent/READING.md`, `TERMS.md` ve gerekirse linked TERMS parts oluştur;
- gstack/Superpowers/CMH gibi önceki package'lerin terim sınırlarını Hermes'e başlangıç ontology'si olarak dayatma.

B7/B8 ortak referans aşaması hâlâ yetkili next değildir. S1 sonrası eklenmiş study yolları bütün seri ve delta kontrolünden dışlanamaz.

## 3. Amaç, derinlik ve iki risk

İlk aşama research/studies araştırmalarını tam okuyarak her birinin kendi bağlamında kullanım ve ilişkilerini çıkarmaktır. İkinci aşama bütün çıkarımları tam okuyup ortak referansı değerlendirmektir. İlk pilotun/CMH'nin şeması, hazır sözlük veya kullanıcının açıklayıcı örnekleri sonraki paketlere başlangıç ontolojisi yapılmaz. Kaynakta tanım bulunması veya concepts'e yazılması ortak kabul değildir.

Her concepts turunda iki neden kısa ve görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişiklik izlenebilir olmalı. Ortak sözcükler aynı anlamı garanti etmiyor; kullanıcı onayı, kaynak kullanımı ve assistant yorumu teknik doğruluk yerine geçmemeli. Kullanıcı teknik uzman oracle değildir; ham düşünce değil, denetlenebilir sonuç ve kısa gerekçe gerekir.

Kaynağın genel tanım vermediği kullanımı açık bırakmak geçerli çıktıdır; okunmamış dosya veya atlanmış açıklama gerçek eksiktir. Yalnız genel bilgiyi artıracak ve mevcut aktarımı değiştirmeyecek okuma eklenmez. Açık kaynak soruları kendiliğinden yeni deney/literatür borcu olmaz. Talimat, kod anlatımı, geçmiş yerel deney, dış yazar raporu, sentez ve yeni yorum ayrılır; tekrar bağımsız destek değildir.

P2'nin önceki gruplarındaki özgün satırlar kalıcı aktarım sırasında erişilebilir olduğu ölçüde kullanıldı; B6-T10'da tarihsel SP150–SP160 satır metni güvenilir biçimde recover edilemedi. METHOD §8 uygulanarak sabit kaynaktan U08-R regeneration yapıldı; STATE/summary'den birebir SP anlamı uydurulmadı. Tam ve değişmemiş gerçek içerik sırf yeni tur diye mekanik tekrarlanmaz; eksik zorunlu kontrol veya kaynak canonical yoldan geri kazanılır.

## 4. B6-T14 gerçek çalışma ve gstack kapanışı

B6-T14 başlangıç main'i **45b2f57a0ca5b3845b0db6b729b39582a58196cb** idi. Source package 23 files: 7 root records, inventory/STRUCTURE, one v1.80 revalidation record and 14 syntheses.

Pinned source identity `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618` / v1.79.0.0 korunur. Later `c24121663732644c56280474a1720475dbe53127` / v1.80.0.0 read is bounded revalidation, silent repin değildir.

Kalıcı records:
- `concepts/studies/gstack/READING.md`;
- `concepts/studies/gstack/TERMS.md`;
- `TERMS-WORK-DELIVERY.md`;
- `TERMS-RUNTIME-CONTROL.md`;
- `TERMS-EVIDENCE-CONTINUITY.md`;
- `TERMS-COORDINATION-PORTABILITY.md`;
- `TERMS-SYSTEM.md`.

Ana source-native/result distinctions:
- gstack = artifact-mediated, qualification-driven software-development operating-system prior art; SOUL architecture değil;
- candidate intent / admitted Work / performed Work / qualification / authorized progression / realized target state ayrı;
- current qualification type historical ceremony provenance'den ayrı;
- review, QA, ship, merge, deploy, live health, rollback/restoration ayrı standings;
- browser persistent runtime evidence ve runtime authority/resource scopes ayrı;
- careful/freeze/guard preventive controls, one-way doors decision authority, CSO detective security ayrı control families;
- fresh context/model diversity/independent verification aynı değil;
- memory plural: checkpoint, local learning, typed brain cache, trust/ingest policy farklı semantics;
- stale GBrain qualifier'ın planning view'da kaybolması strong source→view negative finding;
- test exists/selected/executed/oracle valid/finalized/independent standings ayrı; green derived view;
- host/model/adaptation/install/runtime/behavioral-validation standings ayrı; “supported host” binary değil;
- source→generated→installed→running→release propagation tek update marker'a collapse edilmez;
- command/transition attempt ≠ realized state; authoritative readback recurring control;
- feedback/recommendation ≠ Work admission;
- native Qualified Transition Loop: situation binding → evidence → standing → authority/control → bounded effect → realized-state readback → invalidation → continuation/recovery/adaptation.

v1.80 revalidation exact `/freeze` state-root fail-open defect'ini fixed olarak düzeltir; broader scope/host limits ve diğer qualification seam findings korunur. Concepts records current defect ile historical fixed defect'i karıştırmaz.

Closure-audit holdouts (iOS, scrape→skillify, health/benchmark, artifact-output) ayrı first-order semantic subsystem üretmedi; mevcut mechanism families'i compose eden verticals/views olarak tutuldu.

Source-side coverage 23/23 full-read ve bütün native/cross-system/projection/closure/revalidation families TERMS parçalarına bağlıdır. Concrete transfer omission bulunmadı. Bu same-assistant source extraction'dır; independent validation veya shared cross-study vocabulary değildir.

## 5. Yetki ve yazma kapsamı

B6-T14 mevcut seri çıkarım yetkisi içindedir; gstack source study'yi yeniden açmak, Foundation mutation, architecture adoption veya upstream implementation değildir.

Bu tur concepts katmanında:
- yeni gstack READING;
- yeni ana TERMS;
- beş yeni linked TERMS parçası;
- `concepts/INDEX.md`;
- bu `concepts/STATE.md`

değişir.

Özgün `research/studies/gstack/**`, diğer studies, önceki durable package records, METHOD/PLAN/SCOPE/CHARTER/ORIGIN/SETUP-REVIEW, Foundation ve agent-control bu iş adına değiştirilmedi.

## 6. Değişen korpus ve değişmez devam kayıtları

SCOPE/S1 başlangıç ref'i ve post-S1 delta ilkeleri değişmedi. Bilinen yeni study yolları `agentmemory`, `claude-swap`, `cli-continues`, `ponytail` olarak açık kalır; final tree-delta hesabında işlenecekler.

B6-T14 concepts publication checkpoints:
- gstack READING create: **70a88ca3d28a59ef24632217e7beb8c24218bfc4**
- WORK-DELIVERY: **f5496deeadcb0c8f5d2d4a293e1fc30703b94807**
- RUNTIME-CONTROL: **b3e8e994c83c3c6da9b8dcec525a995d48193c58**
- EVIDENCE-CONTINUITY: **782a2647adbd36121221377f6d8868b34ec19ce4**
- COORDINATION-PORTABILITY: **ac6038bd16d4c52b461da3dab6a3cb4eebaa81ec**
- SYSTEM: **f4e9d8d748c424d719e9e5dcdce13bd7a9b58d47**
- TERMS entry: **2a127d4333c22e27cf1712089b48247e0bcc35cd**
- READING closure update: **7629f4094a64fe7122bd47ce953aab465f53d14e**
- INDEX update: **3cf64c372775409c0f3b1804e54e5c3b0006e13a**

Source package files bu concepts writes tarafından değiştirilmedi. Later load-bearing gstack/current-product use, pinned v1.79 package ve bounded v1.80 revalidation'dan daha fresh upstream check gerektirebilir.

| Değişmez kayıt | Korunan kapsam |
|---|---|
| CMH durable closure | ilk durable package. |
| Superpowers B6-T10 closure | 52/52 source package. |
| AI Knowledge Strategies B6-T11 closure | 9/9 source package. |
| Multi-Agent Patterns B6-T12 closure | 3/3 source package. |
| Anthropic AI-Native SDLC B6-T13 closure | 8/8 source package. |
| gstack B6-T14 READING | 23/23 source accounting, pinned/revalidation boundary ve linked TERMS layout. |

Eski package next/action cümleleri chronological research history'dir; current concepts next work global STATE'den alınır.

## 7. Yayın kontrolü ve yeni oturum

gstack READING, ana TERMS ve beş linked part main'den readback edilerek file identity, group linkage ve source coverage kontrolü yapıldı. INDEX'in gstack row'u durable path'lere bağlandı. Bu STATE kendi henüz bilinmeyen commit'ini uydurmaz; yazımdan sonra actual diff ve main placement ayrıca doğrulanır.

Yeni oturum cold-start: AGENT + triggered protocols → concepts/INDEX zorunlu dosyaları → bu STATE → **hermes-agent package preflight**. gstack yalnız durable-complete source olarak gerektiğinde geri çağrılır. B7/B8 hâlâ ileriki aşamadır.

