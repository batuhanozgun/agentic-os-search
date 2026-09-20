# Concepts — Güncel çalışma durumu

2026-09-20, **B6-T11**. Bu dosya araştırma bazlı terim/jargon çıkarımının global amaç, yetki, güncel iş ve devam kaynağıdır. Kaynak araştırmaların STATE dosyaları veya yerel READING/kullanım kayıtlarının yerine geçmez.

## 1. Güncel durum

**PILOTS-AND-B2/B4-COMPLETE / B5-SCOPE-S1-DELIVERED / B6-SERIAL-EXTRACTION-ACTIVE / CMH-DURABLE-COMPLETE / SUPERPOWERS-DURABLE-COMPLETE / AI-KNOWLEDGE-STRATEGIES-DURABLE-COMPLETE / METHOD-v0.3-WORKING / POST-S1-ADDITIONS-PENDING-ACCOUNT.**

Kullanıcının “anlaştık. devam et o zaman.” talebiyle `research/studies/ai-knowledge-strategies/` package'i canonical preflight'tan geçirildi, bütün kaynakları tam okundu ve bağlamlı kullanım envanteri kalıcılaştırıldı. **Concepts açısından 9/9 package dosyası full-read ve durable extraction complete durumundadır.**

Kaynak araştırmanın özgün teknik scope'u altı research dosyasıdır: rationale + RAG + Knowledge Graph + Fine-Tuning + CAG + Long Context. Concepts source-accounting'e current `META.md`, `STATE.md` ve `INDEX.md` de dahil edildiği için yerel READING toplamı dokuzdur. Rationale içindeki “files 1–5 not yet researched” satırı current package state değil, initiation-time historical metadata olarak kaydedildi.

| İş | Güncel durum |
|---|---|
| Amaç, iki risk, başlangıç hazırlığı | Tamamlandı; ORIGIN/SETUP-REVIEW tarihsel kaynak. |
| B1/B2 ve B3/B4 | İki konuşma pilotu ve yöntem değerlendirmeleri tamam. |
| B5 | SCOPE/S1 başlangıç kapsamı ve delta ilkeleri teslim edildi. |
| B6 — CMH | Durable-complete. |
| B6 — Superpowers | Durable-complete. |
| B6 — AI Knowledge Strategies | **Durable-complete; 9/9 concepts source file, READING + TERMS.** |
| B6 — sıradaki paket | **multi-agent-patterns**; concepts çıkarımı henüz başlamadı. |
| B6 — diğer S1 birimleri | Başlangıç sırası SCOPE'da; kalıcı çıkarımları kapanmadı. |
| S1 sonrası eklenen kaynaklar | agentmemory, claude-swap, cli-continues ve ponytail bilinen kapsam deltalarıdır; final scope/B7 öncesi hesapta işlenecekler. |
| B7/B8 | Küresel geçiş kontrolü ve ortak referans değerlendirmesi başlamadı. |

S1 başlangıcından **CMH, Superpowers ve AI Knowledge Strategies** kalıcı çıkarım bakımından kapanmıştır. Bu paket sayısı ilerleme yüzdesi değildir ve S1 sonrası yeni studies yollarını içermez.

## 2. Etkin giriş ve sıradaki yetkili iş

AI Knowledge Strategies artık current partial work değildir. Gerekirse [READING.md](studies/ai-knowledge-strategies/READING.md) ve [TERMS.md](studies/ai-knowledge-strategies/TERMS.md) birlikte okunur; paket yeniden araştırılmaz.

**Sıradaki yetkili iş B6-T12:** `research/studies/multi-agent-patterns/` package'ine canonical preflight ile gir:
- current main ve gerçek package tree/file envanterini sabitle;
- META/STATE/INDEX ve package-local authority/cold-start yolunu recover et;
- kaynak araştırmanın current/historical durumunu concepts extraction durumundan ayır;
- bütün source files'i tam oku;
- terim/jargon/kavramsal ayrımları kaynağın kendi kullanımında çıkar;
- gerekirse `concepts/studies/multi-agent-patterns/READING.md` ve `TERMS.md` oluştur;
- önceki paketlerin RAG/KG/agent/harness vb. kavramlarını başlangıç ontology'si olarak dayatma.

B7/B8 ortak referans aşaması hâlâ yetkili next değildir. S1 sonrası eklenmiş study yolları bütün seri ve delta kontrolünden dışlanamaz.

## 3. Amaç, derinlik ve iki risk

İlk aşama research/studies araştırmalarını tam okuyarak her birinin kendi bağlamında kullanım ve ilişkilerini çıkarmaktır. İkinci aşama bütün çıkarımları tam okuyup ortak referansı değerlendirmektir. İlk pilotun/CMH'nin şeması, hazır sözlük veya kullanıcının açıklayıcı örnekleri sonraki paketlere başlangıç ontolojisi yapılmaz. Kaynakta tanım bulunması veya concepts'e yazılması ortak kabul değildir.

Her concepts turunda iki neden kısa ve görünür tutulur: kullanıcı okuma anındaki anlam seçimlerini denetleyemiyor; önemli yorum/dayanak/belirsizlik/değişiklik izlenebilir olmalı. Ortak sözcükler aynı anlamı garanti etmiyor; kullanıcı onayı, kaynak kullanımı ve assistant yorumu teknik doğruluk yerine geçmemeli. Kullanıcı teknik uzman oracle değildir; ham düşünce değil, denetlenebilir sonuç ve kısa gerekçe gerekir.

Kaynağın genel tanım vermediği kullanımı açık bırakmak geçerli çıktıdır; okunmamış dosya veya atlanmış açıklama gerçek eksiktir. Yalnız genel bilgiyi artıracak ve mevcut aktarımı değiştirmeyecek okuma eklenmez. Açık kaynak soruları kendiliğinden yeni deney/literatür borcu olmaz. Talimat, kod anlatımı, geçmiş yerel deney, dış yazar raporu, sentez ve yeni yorum ayrılır; tekrar bağımsız destek değildir.

P2'nin önceki gruplarındaki özgün satırlar kalıcı aktarım sırasında erişilebilir olduğu ölçüde kullanıldı; B6-T10'da tarihsel SP150–SP160 satır metni güvenilir biçimde recover edilemedi. METHOD §8 uygulanarak sabit kaynaktan U08-R regeneration yapıldı; STATE/summary'den birebir SP anlamı uydurulmadı. Tam ve değişmemiş gerçek içerik sırf yeni tur diye mekanik tekrarlanmaz; eksik zorunlu kontrol veya kaynak canonical yoldan geri kazanılır.

## 4. B6-T11 gerçek çalışma ve AI Knowledge Strategies kapanışı

B6-T11 başlangıç main'i **cfa377639183804cc1fe119591bdd9692681a26a** idi ve tur başlangıcında önceki kapanışla identical doğrulandı. Source package current main'de şu dokuz dosyadan oluşuyordu:

- `00-WHY-THIS-RESEARCH.md`;
- `01-RAG.md`;
- `02-KNOWLEDGE-GRAPH.md`;
- `03-FINE-TUNING.md`;
- `04-CAG.md`;
- `05-LONG-CONTEXT.md`;
- `INDEX.md`;
- `META.md`;
- `STATE.md`.

Dokuz dosyanın tamamı B6-T11'de full-read edildi. Kaynak package kendi current STATE'ine göre original bounded research bakımından complete; architecture/implementation authority yok.

Yeni kalıcı kayıtlar:
- `concepts/studies/ai-knowledge-strategies/READING.md`;
- `concepts/studies/ai-knowledge-strategies/TERMS.md`.

TERMS şu kaynak-native ve research-synthesis ayrımlarını korur:
- RAG = external evidence access family; vector DB ile eşit değil;
- KG = relation-centric representation family; graph DB/ontology/GraphRAG ile eşit değil;
- Fine-Tuning = parametric adaptation family; SFT/PEFT/preference/continued pretraining ayrımları korunur;
- narrow CAG = bounded Long Context + reusable KV state + no query-time retrieval; prompt/semantic/cache-accelerated RAG ile aynı değil;
- Long Context = whole-package working-context capability; advertised/effective/governed context ayrımları korunur;
- authority/provenance/freshness/access/verification gibi knowledge-governance sorunları altıncı peer strategy yapılmaz.

Ayrıca paket içi kompozisyonlar ve project-specific SOUL/Development OS interpretations ayrı statülerle tutuldu; bunlar architecture decision olarak promote edilmedi.

Source-side coverage kontrolünde bütün rationale/deep-dive/STATE/META/INDEX kullanımları TERMS'e bağlandı; unread source file veya somut aktarım borcu kalmadı. Kapanış aynı-assistant source extraction'dır; independent verification veya universal terminology sertifikası değildir.

## 5. Yetki ve yazma kapsamı

B6-T11 mevcut seri çıkarım yetkisi içindedir; yeni research phase veya architecture work değildir.

Bu tur dört concepts yolu değişir:
- yeni `concepts/studies/ai-knowledge-strategies/READING.md`;
- yeni `concepts/studies/ai-knowledge-strategies/TERMS.md`;
- `concepts/INDEX.md` — gerçekten oluşturulmuş durable package kaydı eklendi;
- bu `concepts/STATE.md`.

Özgün `research/studies/ai-knowledge-strategies/**`, diğer studies, CMH/Superpowers durable kayıtları, METHOD/PLAN/SCOPE/CHARTER/ORIGIN/SETUP-REVIEW, Foundation ve agent-control bu iş adına değiştirilmez.

## 6. Değişen korpus ve değişmez devam kayıtları

SCOPE/S1 başlangıç ref'i ve post-S1 delta ilkeleri değişmedi. Bilinen yeni study yolları `agentmemory`, `claude-swap`, `cli-continues`, `ponytail` olarak açık kalır; yeni yollar eklenirse aynı şekilde final tree-delta hesabına dahil edilir.

B6-T11 başlangıcından bu STATE öncesine kadar main'de AI Knowledge Strategies source package'i değiştirilmedi; yapılan writes concepts katmanıyla sınırlıdır:
- READING create commit **e0607f1ecb19b810c586c42198d26b552f14c45c**;
- TERMS create commit **86cb21ce573376106146721769ec36d2ad669611**;
- concepts INDEX update commit **4b2c280f755804ba7d91b50347b2c75168128d76**.

Source package blob identities yerel READING'de korunur. Time-sensitive dış provider/model/library claim'leri daha sonraki adoption/design kararında current source'tan yeniden doğrulanmalıdır.

| Değişmez kayıt | Korunan kapsam |
|---|---|
| P1/P2 pilot checkpoints | METHOD v0.3'e gelen yöntem kanıtı. |
| CMH durable closure | İlk kalıcı package ve source-boundary örneği. |
| Superpowers B6-T10 durable closure | 52/52 source package ve source-regeneration sınırı. |
| AI Knowledge Strategies B6-T11 READING | 9/9 current concepts source account ve package closure. |

Eski package handoff/“next file” cümleleri chronological research history'dir; current concepts next work global STATE'den alınır.

## 7. Yayın kontrolü ve yeni oturum

Yeni READING ve TERMS main'den geri okunup içerik/bağlantı/kapanış tutarlılığı kontrol edilir; INDEX'in yeni satırı gerçekten durable path'lere yönlenmelidir. Bu STATE kendi henüz bilinmeyen commit'ini uydurmaz. Yayından sonra actual diff ve main placement kontrolü yapılır.

Yeni oturum cold-start: AGENT + triggered protocols → concepts/INDEX zorunlu dosyaları → bu STATE → **multi-agent-patterns package preflight**. AI Knowledge Strategies yalnız durable-complete source olarak gerektiğinde geri çağrılır. B7/B8 hâlâ ileriki aşamadır.

