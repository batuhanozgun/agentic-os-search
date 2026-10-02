# O7 — Bellek ve bağlam mühendisliği: çözülmüş kalıplar ve DevOS'ta uygulanışı

**Tür:** okuma notu (alt ajan O7, model çıktısı). **Tarih:** 27 Eylül 2026. **Görev:** `devos/okuma/BRIEF.md`, satır O7. **Dal/HEAD:** `claude/hopeful-pascal-7bekcd` / `ae7cac4`.
**Kanıt dili:** *kaynak diyor* (study dosyası söylüyor; dış hedefi ben okumadım) · *gözledim* (repoda kendim gördüm) · *çıkarım* · *bilinmiyor*. Alıntılar özgün dilindedir. **Kapsam:** §0.
**Kısaltmalar:** CMH-00…04 = `research/studies/context-memory-harness-engineering/0N-…md`; AKS-RAG/KG/FT/CAG/LC = `research/studies/ai-knowledge-strategies/01…05-…md`; VID = `research/studies/the-carbon-layer/videos/PxuMqeIqCEo-agent-memory/`; META(x) = `research/studies/x/META.md`.

## DevOS için en önemli çıkarımlar

1. **Kümenin gerçek durumu.** 9 paketin 6'sı yalnız META ve "PLANNED / RESEARCH NOT STARTED" (ai-memory, agentmemory, agent-memory-providers, context-mode, openviking, llm-wiki). En somut mekanizmalar (FTS5 oturum deposu, L0/L1/L2, `memory_diff.json`, hook ile yakalama) bunlarda ve "qualification signals, not research findings"; upstream kod yerelde yok. Araştırılmış üç paket (CMH, AKS, bellek videosu) literatür sentezidir, yerel test yok. "Çözülmüş kalıp" = kaynakların yakınsadığı kural; bizde çalıştığı gösterilmedi.
2. **Yetki sırası sabit kural olmalı:** "fresh authoritative source/state > verified persistent derived memory > unverified/heuristic memory" (CMH-02 §6). ai-memory'deki karşılığı: "current instructions and checkout state remain authoritative over remembered material". DevOS'ta STATE ve karar dosyaları her bellek notunun, özetin ve auto-memory'nin üstündedir.
3. **Açılış = zorunlu kanonik çekirdek + istek üzerine derinleşme:** "mandatory canonical bootstrap + adaptive evidence retrieval" (AKS-RAG §14.4). Kademeli açılım üç kaynakta aynı kalıp: repodaki `STATE → INDEX → paket → kaynak` zinciri, OpenViking'in L0/L1/L2'si, Karpathy'nin `index.md → sayfa` okuması. Claude Code'da (*çıkarım*): kısa CLAUDE.md + oturum başında taze STATE okuması + INDEX/skill ile derinleşme.
4. **Kararlı olanı yeniden kullan, değişkeni taze oku:** "Stable verified context'i cache et; dynamic authoritative state'i fresh recover et" (AKS-CAG §27.5). CLAUDE.md'ye yalnız kararlı içerik girer; STATE, açık kararlar, dal/HEAD CLAUDE.md'ye kopyalanmaz, her seferinde dosyadan okunur.
5. **Sıkıştırma kayıplı bir türetilmiş görünümdür** (CMH-01 §11). %80 sıkıştırmaya karşı STATE her iş kaleminden sonra güncel tutulur, sıkıştırmadan sonra kanonik dosyalar yeniden okunur. context-mode'un yeniden kurduğu alanlar ("active files, errors, decisions, rules, tasks, environment, subagents, skills, roles, goals and recent user messages") STATE'in "yeniden kurulum" bölümü için hazır bir alan listesidir.
6. **Bellek depo değil yaşam döngüsüdür:** aday → yaz → nitele → birleştir → güncelle/yerine koy → sakla/unut → oku → bağlama taşı (CMH-02 §4). "Bir `MEMORY.md` dosyasının varlığı memory harness değildir" (CMH-03 §14). Her adımın tetiği ve sahibi yazılı olmalı.
7. **Bellek sınıfları ayrı yetki ve risk taşır** (CMH-02 §22; tablo M14'te birebir). Her kayıt `memory_type`, `epistemic_status`, `source_refs`, `valid_time / superseded_by`, kapsam ve doğrulama durumuyla bağlama geçer (§23).
8. **Model üretimi bellek, gözlenmiş ya da yetkili bellekle aynı sınıfta tutulmaz** (CMH-02 §17). Dersler ve alt ajan yansımaları "aday" girer, kanıt ve kapsamla terfi eder. "Özetleme bir iddiayı doğrulanmış olguya veya yetkili kurala yükseltmez" (VID RESEARCH §6). Aynı kaynaktan türemiş üç wiki satırı üç kanıt değildir: "content novelty != evidence novelty" (EXP-003 S008).
9. **Unutma, güncel karardan düşürmektir; silmek değil.** Dört yol: zamanla önem düşürme, çelişkide güncelleyip eskiyi tarihe çevirme, sıkıştırma, elle bakım (VID RESEARCH §6). "old does not mean false and new does not mean authorized" (VID META). Git tarihi zaten tutar; DevOS'ta unutma = `superseded` işareti + aktif görünümden çıkarma.
10. **Bulunamadı ≠ yok** (AKS-RAG §14.3; AKS-KG §14). Yük taşıyan yokluk iddiasında arama yöntemi ve kapsamı yazılır, doğrudan okuma yapılır. Aramada yetki alakadan önce gelir: tarihsel bir handoff'taki "Next action: X" güncel yetki değildir (AKS-RAG §5.2, §14.2).
11. **Bilgi grafı:** DevOS için ilk rolü "canonical source'a exact provenance ile bağlı derived relation/index layer"dır (AKS-KG §25.1). Grafik veritabanı gerekmez; dosya ön bilgisindeki tipli bağlantılar (`supersedes`, `supported_by`, `depends_on`) yeter (*çıkarım*). "Current authorization tam olarak ne?" sorusu her zaman STATE'in doğrudan okunmasıyla cevaplanır (§25.3).
12. **Wiki ve index:** index bayatlarsa içerik sağlam olsa da bellek fiilen bozulur: "memory intact + discoverability damaged = effective memory failure" (EXP-003 S008). INDEX ve STATE için lint ritmi gerekir: çelişki, bayat iddia, yetim sayfa, eksik çapraz bağ, veri boşluğu (Karpathy'nin `lint` işlemi).
13. **Yazılı kural ≠ çalışma zamanında uygulama** (CMH-01 §19; CMH-04 AP-08). Mekanik olan hook ya da betikle yapılır, örneğin oturum başında STATE'i bağlama vermek ve oturum sonunda STATE'in commit'li olduğunu denetlemek (*çıkarım*). Yargı gerektiren kısım yazılı sözleşmede kalır. Bulutta hook'ların geçerliliği O11'e bağlı.
14. **Reponun kendi META/INDEX/STATE düzeni çalışıyor ama iki ders taşıyor** (*gözledim*). İçerik dosyasına gömülen durum satırı bayatladı (AKS-00 başlığı; AKS INDEX "Current-state correction"). Repoya konmayan medya kayboldu: "hash ve eski `/mnt/data` yolu byte'ları geri getirmez" (VID STATE). Sonuç: tek yetkili STATE; commit edilmeyen hiçbir şey bellek değildir, çünkü makine geri alınır.

---

## 0. Kapsam

**Kümedeki 34 dosyanın hepsi tam okundu (yaklaşık 554 KB):**

| Paket | Dosyalar | Durum |
|---|---|---|
| `ai-memory`, `agentmemory`, `agent-memory-providers`, `context-mode`, `openviking`, `llm-wiki` | her birinde yalnız `META.md` (5–13 KB) | tam |
| `context-memory-harness-engineering` | META, INDEX, STATE, 00, 01, 02, 03, 04 (143 KB) | tam |
| `ai-knowledge-strategies` | META, INDEX, STATE, 00, 01-RAG, 02-KG, 03-FT, 04-CAG, 05-LC (300 KB; 1100–1500 satırlık dosyalar parça parça) | tam |
| `the-carbon-layer/videos/PxuMqeIqCEo-agent-memory` | README, INDEX, META, STATE, METHOD, RESEARCH-PLAN, RESEARCH, SOUL-DEVOS-ASSESSMENT, SOURCE, `evidence/REVIEW-AND-LIMITS.md`, `evidence/MEDIA-READING.json` | tam |

**Küme dışında hedefli ve kısmi okunanlar:**
- `explorations/EXP-007-…/phases/P0-calisma-duzeni/research/R09-studies-baglam-bellek-rol-standartlari.md` (123 KB): yalnız §0, §1, §2.1–2.2, §2.5'in başı, §7–§11. Gerekçe: bu kümeyi kısmen okumuş (AKS'yi bölüm bölüm; video paketinin SOURCE/METHOD/PLAN dosyalarını hiç). R09'un kontrol listeleri (BA-1…9, BE-…) burada tekrarlanmadı; bu not onları kaynak düzeyinde tamamlıyor ve her mekanizmaya DevOS kararı ekliyor.
- `explorations/EXP-003-…/STATE.md` (tam), `sources/conversation/assistant/S008.md` satır 1–330 ve `S010.md` satır 1–12, 255–350. Gerekçe: llm-wiki META'sı mekanizmayı tek cümleyle veriyor; S008 gist'in asistan aktarımıdır, gist'i ben okumadım.

**Okunmayanlar:** Upstream repolar (ai-memory, agentmemory, context-mode, OpenViking, memorizz) yerelde yok (`/home/user` altında aradım). Dış URL'ler açılmadı (küme studies ile sınırlı). Gist ve video medyası repoda yok. the-carbon-layer koleksiyon dosyaları O8'in, EXP-003'ün geri kalanı O10'un kümesinde.

## 1. Kümenin yapısı

| Paket | Statü | Ne veriyor |
|---|---|---|
| CMH | "bounded research package COMPLETE; user evaluation pending" | bağlam / bellek / harness ayrımı, başarısızlık yüzeyleri, DevOS değerlendirmesi |
| AKS | "original six-file research scope COMPLETE" | RAG, KG, FT, CAG, LC'nin karar sınırları, DevOS tabloları |
| VID (bellek videosu) | "first source investigation COMPLETE / REVIEW READY" | dört bellek işlevi, context builder, çelişki, unutma |
| ai-memory, context-mode, openviking, llm-wiki, agentmemory, agent-memory-providers | "PLANNED / RESEARCH NOT STARTED" | uygulanmış sistemlerin ön niteleme sinyalleri |

Doğrulama (*kaynak diyor*): CMH STATE §6 "local SOUL/Dev OS context benchmark, memory write/read/update benchmark, harness component ablation…" koşmadığını söylüyor. AKS STATE §5: "decision boundaries and research hypotheses, not production architecture acceptance". VID: `"not_executed": ["memory runtime", "retrieval benchmark", "model API", …]`.

---

## 2. Mekanizmalar

Her mekanizmada kaynak, işleyiş ve DevOS kararı var. Ayrı "Kanıt" satırı olmayanlarda kanıt §1'deki gibidir: literatür ya da tedarikçi sentezi veya ön niteleme; hiçbiri yerelde koşulmadı. "Claude Code'da" satırları *çıkarım*dır, platform ayrıntısını O11 doğrulamalı.

### A. Bağlam: neyin ne zaman bağlama girdiği

**M1 — Çalışma kümesi: seçim ve dışlama, sınıf ve güven etiketleri**
- *Sorun:* Bilgi diskte durur ama modelin önüne gelmezse "working context açısından yoktur" (CMH-01 §2). Fazlası da zararlıdır.
- *Nasıl:* Amaç "maximize decision-relevant signal / subject to: attention / token / latency / cost / trust constraints"; bağlam "bir **selection problem** kadar bir **exclusion problem**'dir" (§4). Kaynak sınıfları: kontrol talimatı, güncel iş durumu, dış kanıt, bellek, araç arayüzü, araç sonucu, türetilmiş içerik (§5). Güven sınıfları: "trusted control instruction / trusted canonical state / trusted/verified source evidence / untrusted external content / model-generated derived content / user-provided claim/preference" (§16). Kirlenme (eski planlar, çözülmüş hatalar, uzun loglar, güvenilmeyen belgeden kopyalanmış talimat, tekrar eden özetler) "**epistemic status collapse**" üretir (§15).
- *DevOS:* **Al.** Görev tanımında ve alt ajan dönüşünde her bağlam parçası sınıf ve güven etiketi taşısın. Repodan okunan başka asistana ait talimat "untrusted external content" sınıfındadır.

**M2 — Zorunlu kanonik açılış ve uyarlamalı getirme (kademeli okuma zinciri)**
- *Sorun:* Soğuk başlangıcın doğruluğu anlamsal aramanın şansına bırakılamaz; her şeyi yüklemek de gürültü üretir.
- *Nasıl:* "Current state / authorization gibi yük taşıyan surfaces deterministic/canonical preflight ile zorunlu kalabilir; RAG bundan sonra bounded retrieval yapabilir" → "mandatory canonical bootstrap + adaptive evidence retrieval" (AKS-RAG §14.4). Repodaki zincir: `STATE → INDEX/router → current package → KEY/synthesis/finding → load-bearing claim için source recovery` (§14.1). Uzun bağlamlı biçimi (AKS-LC §26.4): `fresh canonical control/state → router identifies current bounded package → full authoritative package loaded via Long Context → cross-document reasoning → load-bearing claims direct-source verified → repository receives explicit output/handoff`. Sınır: "context information architecture + context-loading enforcement … İlki repo ile kurulabilir; ikincisi harness/runtime coverage problemidir" (CMH-01 §19).
- *Kanıt:* OpenAI'nin "short map + structured repo system-of-record + progressive disclosure" deneyimiyle bağımsız yakınsama (CMH-03 §8, §24; tedarikçi iddiası). Zinciri repoda gözledim.
- *DevOS:* **Al.** Claude Code'da: CLAUDE.md okuma sırasını söyler; oturum başında STATE taze okunur (mümkünse SessionStart hook'uyla); gerisi INDEX ve skill'lerle istek üzerine gelir.

**M3 — L0/L1/L2 kademeli açılım: önce harita, sonra ayrıntı**
- *Nasıl (kaynak diyor):* OpenViking: "directory-level L0 abstracts and L1 overviews guide relevance/navigation before L2 original detail is loaded", ayrıca "explicit sidecar provenance/freshness metadata and known-staleness signaling (`pending_child_changes`) rather than treating generated summaries as timeless truth" (META(openviking)). Karpathy: "`index.md` önce okunuyor, sonra ilgili sayfalara iniliyor" (EXP-003 S008). Repoda (*gözledim*): her META'da "Reuse modes", "Likely revisit triggers", "Freshness / revalidation" başlıkları var; bunlar ne zaman yükleneceğini söyleyen L0 kartlarıdır. INDEX'teki `| Need | Read first | Then if needed |` tablosu L1'dir.
- *Sınır:* "The L0/L1 model may reduce model-visible context while introducing summary omission, staleness and navigation-selection failure" (META(openviking)).
- *Kanıt:* OpenViking doğrulanmamış. Repo düzeni için zayıf ama gerçek kanıt: AKS-00 "The next session/turn can begin from this file and research `01-RAG.md` without reconstructing the Instagram-post conversation from chat history" diyor; 01–05 sonra tamamlandı, CMH de AKS'nin tamamını girdi aldı.
- *DevOS:* **Uyarlayarak al.** L0 = CLAUDE.md, skill `description`, INDEX satırı; L1 = paket STATE'i ya da sentezi, skill gövdesi; L2 = kaynak. Özet, dayandığı kaynağın SHA'sını taşır; kaynak değişince "bayat" işaretlenir (`pending_child_changes` fikri).

**M4 — Önce yetki, sonra alaka; arama türleri; görünür başarısızlık**
- *Nasıl:* "**Authority relevance'dan önce gelir.**" (AKS-RAG §6.1). DevOS için eleme alanları: "current vs historical, accepted vs hypothesis, source vs synthesis, canonical vs derived, branch/ref/SHA, superseded status, authorization scope" (§14.2). Sorgu türleri farklı yol ister: "“current authorization” → metadata/path/canonical status ağırlıklı", "“F-AR-009 nerede?” → lexical/exact identifier", benzer başarısızlık → semantik, kaynak zinciri → ilişki/köken (§5.1). Parça kopunca: "“Next action: X” bir historical handoff içinde bulunuyorsa current authority değildir … **representation doğru, interpretation yanlış**" (§5.2). "search/retrieval'da görünmedi ≠ kaynakta yok" dendiğinde tırmanma yolu: "query reformulation, alternate index, broader search, exact path/source read, human clarification" (§14.3). Ayrılması gereken durumlar: "evidence found, evidence partially found, evidence conflict, source unavailable, source scope incomplete, retrieval confidence low, no eligible authoritative source" (§13.4).
- *DevOS:* **Al.** Claude Code'da arama `grep` ve `glob` ile yapılır (tam eşleşme); vektör araması gerekmez (*çıkarım*). Eksik-arayıcı rolünün dönüşü yukarıdaki durum etiketlerinden birini, yöntemi ve kapsamı taşısın.

**M5 — Kararlı önek, değişken sonek ve tazelik sınıfları**
- *Nasıl:* AKS-CAG §16 tablosundan (kısaltılmış): "Immutable source at exact SHA — güçlü aday"; "Stable prompt/tool schema — generic prompt cache için güçlü aday"; "Current `STATE.md` — zayıf cross-session default — freshness yük taşıyor"; "Authorization/current Work — çok zayıf stale-cache tolerance"; "Mixed stable + dynamic package — hybrid güçlü aday — stable prefix + fresh retrieval/direct read". Kural: "canonical freshness check ≠ repeated compute reuse" (§15). Ajan iş yüklerindeki ölçüm (Lumer 2026, AKS aktarımı): önbellek "API cost'larını %45–80, TTFT'yi %13–31 azaltabildiğini … Dynamic content'i sona koymak ve tool results gibi volatile content'i stable prefix'ten ayırmak daha tutarlı sonuç vermiştir" (§12). RAG tazelik zinciri: `source changed → change detected → re-ingestion / re-parse → old chunks invalidated → new chunks indexed → permissions/version metadata updated → query sees correct version` (AKS-RAG §7).
- *DevOS:* **Al.** CLAUDE.md kısa ve kararlı kalır; güncel durum yalnız STATE'te olur (iki yerde durum = bayatlama; bkz. D1). Özet ya da türetilmiş her görünüm, dayandığı dosyaların commit'ini yazar.

**M6 — Sınırlı yetkili paketin bütün halinde okunması; etkili bağlam ≠ ilan edilen bağlam**
- *Nasıl:* Altı ayrı bağlam kavramı: advertised, trained, benchmark-effective, workload-effective, economically usable, governed (AKS-LC §3). Kusursuz getirmede bile düşüş var: "context uzadıkça performance'ın **%13.9–85** arasında düştüğü raporlandı"; ayrıca "evidence'i önce recite ettirerek short-context-like reasoning phase'e geçme yaklaşımı … sınırlı fakat tutarlı iyileşme" (§9). Rolü: "progressive retrieval'ın yerine geçmek değil; router'ın belirlediği bounded authoritative çalışma paketini gerektiğinde bütün halinde değerlendirebilmek" (§26.5). Dahil edilen her parça şu alanları taşır: "source identity, version/ref/SHA, current/historical, canonical/derived, accepted/hypothesis/rejected, valid-from / valid-to, actor/access scope" (§22).
- *Kanıt:* Hakemli benchmark'lar (Lost in the Middle, RULER, NoLiMa, Du 2025); bizim modelle ölçülmedi.
- *DevOS:* **Uyarlayarak al.** Büyük paketi alt ajan okur, ana oturum küçük kalır. Alt ajan önce yük taşıyan kanıtı alıntılar, sonra akıl yürütür. "Tüm repoyu yükle" yapılmaz (F-LC-15).

**M7 — Sıkıştırma protokolü ve oturum olaylarından yeniden kurulum**
- *Nasıl:* Sıkıştırma nötr değildir, bir "**derived view**" üretir. Test listesi: "load-bearing decisions korundu mu? / unresolved issues korundu mu? / negatives / rejected alternatives kayboldu mu? / source references korundu mu? / uncertainty certainty'ye dönüştü mü? / authority/status labels korundu mu?" (CMH-01 §11). context-mode (kaynak diyor, doğrulanmadı): "a separate persistent session-event store and compact/resume reconstruction path; snapshot reconstruction of active files, errors, decisions, rules, tasks, environment, subagents, skills, roles, goals and recent user messages" (META(context-mode)). HERMES belgesi oturum başındaki donmuş bellek görünümünü sonradan diske yazılandan ayırıyor (VID RESEARCH §7 D03).
- *DevOS:* **Uyarlayarak al.** context-mode'un kendisi alınmaz: `/plugin` yok ve yerel SQLite deposu makine geri alınınca kaybolur. Alan listesi STATE'in "yeniden kurulum" bölümüne şablon olur. STATE her iş kaleminden sonra güncellenip commit edilir; sıkıştırmadan sonra STATE ve INDEX yeniden okunur, "yapma" türü kısıtlar kontrol edilir. Oturum ortasında değişen CLAUDE.md'nin bağlama yansıması *bilinmiyor* (HERMES'teki donmuş görünüm sorusu; O11).

**M8 — Alt ajanla bağlam bölme ve özetin sadakati**
- *Nasıl:* Uzman alt ajan geniş bağlamda çalışır, ana ajana yoğun sonuç döner; ama `subagent source context → summary → lead context` zincirinde "source fidelity ve omission iki kez test edilmelidir. Sub-agent sayısı otomatik reliability değildir" (CMH-01 §13). Açık soru olarak soruluyor: "Subagent summary'leri source refs taşımak zorunda mı?" (§22).
- *DevOS:* **Al.** Derinlik 1 olduğundan paketi yalnız koordinatör derler. Alt ajan dönüşü `source_refs` (yol#bölüm, commit), statü etiketi ve "okumadım" listesi taşır.

**M9 — Büyük araç çıktısını bağlamın dışında tutmak ("think in code")**
- *Nasıl:* SWE-agent'ta kısa arama özeti ve sınırlı satırlı dosya görüntüleyici performansı artırdı: "Context Engineering yalnız “hangi document?” değil, tool'un observation'ı modele hangi shape'te verdiği problemidir" (CMH-01 §12). context-mode'daki karşılığı (doğrulanmadı): "tool-output routing/interception intended to keep large raw outputs outside model-visible context" ve "a “think in code” pattern that moves some information processing into executable computation and returns only selected results to the model". Uyarı: "“sandboxed execution” terminology must not be silently equated with strong process/security isolation" (META(context-mode)).
- *DevOS:* **Uyarlayarak al.** Uzun çıktı (test logu, büyük diff) dosyaya yazılır, bağlama yol ve özet döner; sayma ve karşılaştırma betikle yapılır.

**M10 — Bağlamın yeterliliğini sınamak, negatif kontrolle**
- *Nasıl:* Sınama eksenleri: sufficiency, precision, authority correctness, freshness, fidelity, position robustness, conflict robustness, budget curve, security. Negatif kontrol: "Context'ten load-bearing evidence çıkarıldığında test kırmızı veriyor mu? Aksi halde test cevap shortcut'ını ölçüyor olabilir" (CMH-01 §17).
- *DevOS:* **Al**, küçük ölçekte. Soğuk başlangıç sınaması: taze oturum yalnız repodan, beklenen cevaplar verilmeden, belirli olguları (güncel aşama, açık kararlar, sonraki izinli adım) bulabilmeli.

**M11 — Context builder ve sıralama**
- *Nasıl:* Videodaki şema: kalıcı depolar → context builder → aktif bağlam. Ortadaki adımlar "**retrieve → rank → resolve → assemble**" (VID RESEARCH §4). Sıralama boyutları (CMH-01 §14): "control before untrusted data, current canonical before historical alternatives, source identity adjacent to content, task-local evidence near relevant question, conflicting evidence explicitly grouped, large low-value tool outputs pruned or referenced". Kaynak bunları "universal fixed ordering rule"a çevirmez.
- *DevOS:* **Al** (koordinatörün paket derleme kuralı). "resolve" adımı yazılı olsun: çelişkide hangisinin güncel olduğu bir kanonik dosyaya dayanarak belirtilir.

### B. Bellek: türler, saklama, geri çağırma, birleştirme, unutma

**M12 — Yaşam döngüsü ve yazma yolunun doğruluğu**
- *Nasıl:* Aşamalar: observe/candidate → write/encode → validate/qualify → consolidate → update/supersede/contradiction → retain/expire/forget → read/retrieve → inject/use (CMH-02 §4). Temel ayrım: "storage ≠ memory correctness / retrieval ≠ recall correctness / recall ≠ context use / retention ≠ truth" (§3). Yazma yolu: "kötü yazılmış memory'yi kusursuz retrieve etmek sadece yanlışı daha güvenilir şekilde geri getirir"; başarısızlıklar: "hallucinated fact persist edildi, temporary hypothesis fact olarak yazıldı, old state current diye snapshotlandı, … user correction eski memory'yi supersede etmedi" (§7). Güncellemede seçim: "overwrite mi, version mi, temporal interval mi, conflict set mi, invalidate mi" (§4.5).
- *DevOS:* **Al.** Her bellek dosya türü için "kim yazar, ne zaman, hangi statüyle, neyle geçersizleşir" yazılı olsun.

**M13 — Dört işlev, bir de kanonik durum**
- *Nasıl:* Working = "modelin mevcut çağrıda görebildiği aktif bağlam"; episodic = belirli olay "zamanıyla birlikte"; semantic = "proje dizini, uygulama kökü, kişi–hesap eşlemesi, kullanıcı tercihleri ve geçerli iş kuralları"; procedural = "Runbook, checklist, skill ve … uygulama kodu" (VID RESEARCH §3). Ek sınıf: "Canonical operational/project state … “agent'ın hatırladığı bir şey” ile aynı statüde olmamalıdır" (CMH-02 §5.5). Sınır: "Dört tür, zorunlu dört bileşen değil" (VID ASSESSMENT §5). "Bilgiyi öğrenme olayını yeniden oynatmadan kullanmak, bilginin zamansız veya değişmez olması değildir" (VID RESEARCH §3).
- *DevOS:* **Uyarlayarak al** (eşleme *çıkarım*): working = bağlam + STATE; kanonik durum = STATE + kararlar; episodic = yalnız eklenen günlük + git log; semantic = bilgi ve karar sayfaları; procedural = skill, runbook, rol dosyası. Dört ayrı depo kurulmaz.

**M14 — Yetki sırası, bellek sınıfları ve devir alanları**
- *Nasıl:* Yetki sırası: `fresh authoritative source/state > verified persistent derived memory > unverified/heuristic memory` (CMH-02 §6). "Memory availability, source authority üretmez." Sınıf tablosu (§22, birebir):

| Memory/state class | Candidate persistence | Authority | Main risk |
|---|---|---:|---|
| Current Work/authorization | canonical repository state | high | stale read |
| Accepted decision | decision/state artifact + source refs | high/qualified | decision context loss |
| Research finding | versioned evidence-backed file | qualified | synthesis overreach |
| Session scratch | ephemeral/short-lived | low | accidental promotion |
| Agent reflection | derived persistent note if useful | low until verified | self-reinforcement |
| Tool/environment gotcha | candidate learned procedure | medium after validation | obsolete workaround |
| User/project stable preference | scoped memory | context-dependent | privacy/staleness |
| Historical state | archive | historical only | current contamination |

  Bellekten bağlama geçerken taşınacak alanlar: `memory_id, memory_type, epistemic_status, source_refs, created_at, valid_time / superseded_by, actor/work scope, confidence / verification status`. Context builder bunlarla şunlardan birine karar verir: "include, exclude, retrieve source, compare with canonical state, compress, ask clarification" (§23).
- *DevOS:* **Al.** Tablo DevOS bellek sınıflarının iskeletidir; "Session scratch" commit edilmez ya da geçici işaretlenir.

**M15 — Zamansal geçerlilik, çelişki ve yerine koyma**
- *Nasıl:* Zamanla değişen değer çelişki değildir; aynı zaman aralığında farklı değer gerçek çelişkidir. Taşınacak alanlar: "observed_at, valid_from / valid_to, source identity, source authority, supersedes, confidence/status, work/project scope" (CMH-02 §8). Videonun örneği: eski kayıtta onay yok, yeni kayıtta `@codex implement` var; ama "sonradan eklenmiş bir yorum yanlış issue'ya aitse, yetkisiz biri tarafından yazılmışsa veya sadece eski bir onayı alıntılıyorsa en yeni metin olması yeterli değildir. Öte yandan eski bir politika hâlâ geçerli olabilir" (VID RESEARCH §5). KG'deki karşılığı: `valid_from, valid_to, recorded_at, superseded_by` (AKS-KG §13).
- *DevOS:* **Uyarlayarak al.** Karar ve onay kayıtları nesneye (iş kimliği), zamana ve yazana bağlanır. Batu'nun onayı birebir alıntı ve tarihle kaydedilir. Yeni karar eskisini `supersedes` alanıyla gösterir; eski dosya silinmez, `superseded_by` alır.

**M16 — Model üretimi bellek ayrı tutulur; terfi kapısı**
- *Nasıl:* Döngü: "model inference → memory write → later recall → model sees its own old inference as context → confidence amplification"; kural: "model-generated memory ile externally observed/authoritative memory aynı epistemic class'ta tutulmamalıdır" (CMH-02 §17). Yansıma riski: "yanlış causal lesson kalıcılaşır, tek failure overgeneralize edilir, self-assessment “truth” olur" (§14). Birikim: "Bir çalışmada önerilen hipotezin sonraki özetlerde doğrulanmış bulguya, bir örneğin bütün işler için kurala dönüşmesi yanlış öğrenme üretebilir" (VID ASSESSMENT §2). Wiki'de: "“Wiki'de üç yerde aynı şey yazıyor.” diye bunu üç bağımsız evidence gibi algılayabilir. Halbuki üçü de aynı raw source A'dan türemiş olabilir" (EXP-003 S008).
- *DevOS:* **Al.** Dersler, alt ajan yansımaları ve "öğrenilenler" `statu: aday` ile yazılır. Terfi için kaynak, kapsam ve kanıt (test ya da tekrar) gerekir. Terfiyi kimin yapacağı açık karardır (§5).

**M17 — Unutma ve saklama**
- *Nasıl:* VID RESEARCH §6 tablosu (birebir):

| Strateji | Kaynağın işlevi | Korunan sınır |
|---|---|---|
| Temporal decay | Eski kaydın önceliğini azaltmak; pinned, kullanılan veya kalıcı politikaya bağlı kayıtları ayırmak | Yaş, doğruluk veya yetkinin tek ölçütü değildir. |
| Contradiction handling | Güncel durumu yenileyip önceki durumu tarih olarak korumak | Yeni iddianın gerçekten geçerli değişiklik olduğu belirlenmelidir. |
| Compression | Oturumdan özet, gerektiğinde daha genel bilgi/yöntem çıkarmak | Özetleme bir iddiayı doğrulanmış olguya veya yetkili kurala yükseltmez. |
| Manual curation | Kritik proje kuralları ve prosedürler için sahiplik | İnsan onayı da tek başına teknik etkililik deneyi değildir. |

  Asıl soru: "neyi saklayıp bugünkü karara hükmettirmeyelim?" (VID ASSESSMENT §4). Unutmanın riski: "rare but critical lesson silinir, provenance chain kırılır" (CMH-02 §15). Altyapıda silme ile politikada unutma ayrı sorulardır (META(agent-memory-providers) Q7).
- *DevOS:* **Uyarlayarak al.** Git fiziksel tarihi korur. "Unutma" üç işlemdir: `superseded`/`reddedildi` işareti koymak, INDEX'ten ve CLAUDE.md'den çıkarmak, gerekiyorsa `arsiv/` altına taşımak. Kişisel ya da gizli veri için gerçek silme ayrı karardır ve git geçmişi nedeniyle zordur (*çıkarım*).

**M18 — Prosedürel bellek: kuralı bilmek ile uygulamak farklıdır**
- *Nasıl:* "uygulama için onay gerektiğini bilmek bir kural bilgisidir; issue'yu getir, yorumları incele, öneriyi ve ardından gelen onayı doğrula, onboarding belgesini oku, sınırlandırılmış dizinlerde çalış, odaklı testleri yap, draft PR aç ve sonucu bildir dizisi bir prosedürdür". Kaynak "prosedürü yalnız prompt olarak düşünmez; tool schema ve orchestration kodu da taşıyabilir". Sınır: "bir şemada `approval_comment_id` alanı istemek, verilen yorumun gerçekten ilgili, geçerli ve yetkili olduğunu tek başına kanıtlamaz" (VID RESEARCH §3). `@codex implement` yayıncının kendi yerel sözleşmesidir, evrensel kural değildir (VID SOURCE).
- *DevOS:* **Al.** Prosedürler skill ya da runbook dosyası olur. Kapı kontrolleri (onay var mı, hangi işe ait) biçim kontrolüyle yetinmez; nesne, zaman ve yetki eşleşmesini de denetler.

**M19 — Dosya önce: kanonik dosyalar, türetilmiş dizinler, denetimli güncelleme (aday sistemler)**
- *Nasıl (kaynak diyor; hepsi doğrulanmamış ön niteleme):*
  - ai-memory: "a git-versioned markdown wiki is declared the durable source of truth and SQLite/FTS/entity/graph/vector structures are derived indexes"; "automatic lifecycle-hook capture of prompts, tool use and session boundaries, with a typed sanitization/privacy boundary before durable storage"; "capture, session-end consolidation, retrieval, handoff, reinforcement, decay/forgetting and backup/restore"; "typed cross-agent handoffs with ownership/claim semantics"; "zero-LLM default operation for capture/search/handoff". DevOS'a dönük sinyal: "bounded startup briefs and progressive retrieval instead of replaying full history".
  - OpenViking: "the vector index stores retrieval references/metadata rather than authoritative file bodies"; "session commit semantics that archive messages synchronously and perform summary generation plus long-term-memory extraction asynchronously"; "a memory update pipeline that compares extracted candidates with existing memory and can skip, create, merge or delete, while writing `memory_diff.json` audit material for each commit". Olgunluk "Alpha", lisans "AGPL-3.0".
  - memorizz (agent-memory-providers): "MemAgent = model + memory provider + runtime policies + optional capabilities"; açık soru: "can the system distinguish “no memory exists” from “retrieval failed”?". Lisans "PolyForm Noncommercial 1.0.0". agentmemory'de README düzeyinden fazlası yok.
- *DevOS:* **İlkeleri uyarlayarak al; ürünleri alma.** İlkeler: (1) kanonik kayıt git'teki Markdown'dır, her dizin ya da önbellek türetilmiş ve yeniden kurulabilir; (2) oturum sonunda birleştirme: STATE, günlük, aday dersler; (3) bellek değişikliği denetlenebilir: commit mesajında "eklendi / birleştirildi / yerine kondu / silindi" (`memory_diff`in dosya karşılığı); (4) sırlar bellek dosyasına yazılmaz; (5) "yok" ile "arama başarısız" ayrılır. Ürünler alınmaz: plugin yok, yerel veritabanı makineyle kaybolur, lisans ve olgunluk uygun değil, hiçbiri doğrulanmadı.

**M20 — Belleği sınamak**
- *Nasıl:* CMH-02 §18'in başlıkları: Write precision, Write recall, Update correctness, Temporal reasoning, Contradiction handling, Retrieval / recall, Abstention, Authority precedence, Forgetting / deletion, Privacy/access, Downstream decision impact. Koşullu test tasarımı: "doğru eski kayıt, geçerli yeni güncelleme, yetkisiz/yanlış yeni kayıt, yanlış issue eşleşmesi ve değişmemiş kalıcı politika gibi ayırt edici örnekler; … Önce oracle ve yan etkileri belirle" (VID RESEARCH-PLAN). Ayrıca: "“session memory enabled” = “memory architecture solved” değildir" (CMH-02 §19).
- *DevOS:* **Uyarlayarak al.** Beş ayırt edici vakadan oluşan küçük bir sınama seti, soğuk başlangıç sınamasıyla (M10) birlikte koşulur. Claude Code'un oturum devamı (resume) ya da auto memory, bellek mimarisi yerine geçmez.

### C. Bilgi grafı ve wiki

**M21 — LLM'in bakımını yaptığı wiki: ham kaynak, wiki, şema; ingest, query, lint**
- *Nasıl (EXP-003 S008'in gist aktarımı; gist'i ben okumadım):* Üç katman: "Raw source'lar immutable; wiki LLM tarafından yaratılıyor ve sürekli değiştiriliyor; schema ise wiki'nin nasıl tutulacağını ve ingest/query/maintenance workflow'larını tarif ediyor". İşlemler: "`ingest`: source'u oku → summary oluştur → ilgili entity/concept sayfalarını güncelle → index'i güncelle → log'a kayıt ekle"; "`query`: … değerli cevapları tekrar wiki'ye yazabilirsin"; "`lint`: contradiction, stale claim, orphan page, eksik cross-reference ve data gap ara". Destek dosyaları: "`index.md` → bilgi nerede / ne var?" ve "`log.md` → sistemde ne oldu / ne zaman oldu?". Bir kaynak 10–15 sayfaya dokunabilir. META(llm-wiki) aynı ayrımı tek cümleyle veriyor.
- *Sınırlar (S008):* `raw source = authoritative preserved source representation ≠ represented proposition is true`; `log.md` "operation history"dir, "semantic change history" değildir ("Karpathy version history sağlıyor; **revision semantics** sağlamayı implementere bırakıyor"); çok sayfalı güncellemede tutarlılık açık kalıyor; ayrıca kendini kaynaklaştırma (M16).
- *DevOS:* **Uyarlayarak al** (araştırma ve bilgi katmanı için). `bilgi/` sayfaları kaynak yolu ve SHA taşır. INDEX = `index.md`, günlük = `log.md`. Lint ritmi eklenir. Değişiklik gerekçesi ("düzeltme mi, yeni kanıt mı, dünya mı değişti, yorum mu değişti") commit ya da günlük satırında yazılır. Wiki güncel iş ve yetki durumunu taşımaz; o STATE'in işidir.

**M22 — Türetilmiş ilişki dizini (bilgi grafı)**
- *Nasıl:* Epistemik zincir: `relation represented ≠ relation validated ≠ relation current ≠ relation authoritative ≠ relation causal` (AKS-KG §5). Kimlik için kararlı anahtarlar: "repository + path, commit/blob SHA, work package ID, decision ID, Actor ID, explicit canonical entity key" (§9.2). Yüklem ayrımları: "`proposes` vs `decides`, `supports` vs `proves`, `references` vs `depends_on`, `observed_in` vs `inferred_from`, `authorised_for` vs `performed`, `supersedes` vs `contradicts`, `current` vs `historical`" (§10). "graph miss ≠ world/source absence" (§14). Tahmin edilen kenar "Burada olası eksik relation var; kontrol et" diye kullanılır, olgu diye değil (§15). Bakım zinciri kurulmazsa grafik "“structured stale memory”ye dönüşür" (§22). Yönlendirme (§25.3): `exact/current authority → direct canonical source; relation/impact query → graph-assisted retrieval; semantic similarity → text/vector retrieval; global synthesis → GraphRAG or broader context`. Her kenarın alanları: "exact source pointer, repo/ref/SHA, extraction method, epistemic status, valid time, last verified time" (§25.4). GraphRAG basit olgu aramasında vanilla RAG'ın altında kalabiliyor (§20.2).
- *DevOS:* **Uyarlayarak al; grafik veritabanı ve GraphRAG alma.** İlişkiler dosya ön bilgisinde tipli alanlar olarak durur (`supersedes`, `supported_by`, `depends_on`, `derived_from`). Gerekirse bir betik bunlardan etki listesi çıkarır ("bu kaynak değişirse hangi kararlar yeniden bakılmalı"). SOUL Foundations hiyerarşisi ontolojiye çevrilmez (F-KG-10).

### D. Harness bağlantısı: politika ≠ yürütme

**M23 — Bellek ve bağlam politikasının gerçekten çalışması**
- *Nasıl:* Harness soruları: "hangi event write trigger? write before/after verifier mı? … session end'de handoff oluşuyor mu? memory recall her turn mü, on-demand mı? …" (CMH-02 §24). Uygulama merdiveni: `prose preference < explicit protocol < runtime guard/check < deterministic invariant enforcement`; hedef "**mekanik olanı mekanikleştirmek ve judgement-required surface'i görünür bırakmak**" (CMH-03 §9). Uzun işte süreklilik: `initial environment / feature state → agent works bounded increment → commits/progress artefacts → next fresh session recovers state`; "long-running autonomy yalnız longer context değil, **recoverable external work state** gerektirir" (§12). Model değişince: `model/version change → re-benchmark → component ablation → simplify / add new capability` (§17). Uyarı: "More harness ≠ better harness" (§16).
- *DevOS:* **Al.** Her bellek ve bağlam kuralının yanına "uygulama biçimi: yazılı / hook / betik / kapı" yazılır.

### E. Alınmayacaklar (gerekçesiyle)

- **İnce ayarla bellek:** "Development OS için mutable governance/context external and explicit kalmalı" (AKS-FT §19.1); Claude Code'da zaten yok. Opak, makineye bağlı auto memory de aynı nedenle güncel durum için kullanılmaz (makineye bağlılığı R09'un R01 aktarımı; O11 doğrulamalı).
- **Önbelleği bellek saymak:** "Cache persistent computational state olabilir; fakat agent memory ile eş anlamlı değildir" (CMH-02 §11).
- **Varsayılan vektör veritabanı ve RAG:** Dev OS'un kademeli okuması "RAG ile değiştirilmesi gereken eski sistem" değil, "controlled retrieval baseline"dır (F-RAG-06).
- **Bellek ürünleri ve MCP bellek sunucuları (şimdilik):** M19'daki gerekçeler.

---

## 3. Claude Code bulutunda uygulama taslağı (*çıkarım*; platform ayrıntısı O11'de doğrulanmalı)

Bulut gerçekleri (`/plugin` yok, alt ajan derinliği 1, boşta makine geri alınır, %80 sıkıştırma, Mac kapalı olabilir) yüzünden tek kalıcı taşıyıcı commit edilip push edilmiş dosyalardır. R09'un R01 aktarımı (okumadım): repo `settings.json` hook'ları yalnız tek repolu oturumda geçerli (R01 satır 527); `/compact` ve `/context` bulutta çalışıyor (R01 satır 539).

**Dosya yerleşimi (öneri):**
```text
CLAUDE.md                     L0; her oturumda yüklenir; kısa: yetki sırası, okuma sırası, yazma yerleri, etiketler. Güncel durum YOK.
devos/STATE.md                kanonik güncel durum: hedef, aşama, aktif iş, açık kararlar, sonraki izinli adım,
                              "yeniden kurulum" alanları (M7), son güncelleyen + commit
devos/INDEX.md                L1: | İhtiyaç | Önce oku | Sonra gerekirse |
devos/kararlar/K-NNN.md       kabul edilmiş karar (yüksek yetki); supersedes / superseded_by
devos/bilgi/<konu>.md         kaynağa bağlı bulgu ve wiki sayfası (nitelikli); source_refs + SHA
devos/dersler/L-NNN.md        ders ve ortam tuzağı: aday → doğrulandı / reddedildi
devos/gunluk/YYYY-MM-DD.md    olay günlüğü, yalnız ekleme: ne oldu, kim, hangi commit, neden
.claude/skills/<ad>/SKILL.md  prosedürel bellek: description = L0, gövde = L1, ek dosyalar = L2
.claude/agents/<rol>.md       rolün sabit sözleşmesi
```

**Bellek kaydı ön bilgisi** (alanlar CMH-02 §8 ve §23 ile AKS-KG §25.4'ten):
```yaml
---
id: L-014
tur: ders              # karar | bulgu | ders | tercih | yansima | tarihsel
statu: aday            # aday | dogrulandi | reddedildi | yerine-kondu
yazan: alt-ajan/O7     # batu | koordinator | alt-ajan/<rol>   (model üretimi ayrı sınıf, M16)
kaynak: [devos/gunluk/2026-09-27.md, "commit ae7cac4"]
gozlem: 2026-09-27
gecerlilik: {baslangic: 2026-09-27, bitis: null}
supersedes: null
kapsam: rol/dogrulayici
dogrulama: yok         # yok | test:<ad> | batu-onayi:<tarih>
---
```

**Oturum ritmi:**
1. *Açılış:* CLAUDE.md otomatik yüklenir. STATE taze okunur; mümkünse SessionStart hook'u (startup, resume, compact eşleyicileri) `STATE.md` ve `INDEX.md`'yi bağlama basar. Sonra yalnız işin paketi (M2, M3).
2. *İş kalemi sonu:* STATE güncellenir (tek yer), günlüğe bir satır, dersler `aday`; sonra commit ve push, çünkü makine geri alınabilir (M12, M16).
3. *Sıkıştırma:* STATE güncel olduğundan kayıp sınırlı; sonrasında STATE ve INDEX yeniden okunur, M7 listesiyle kısıt kaybı kontrol edilir.
4. *Alt ajan:* Paketi koordinatör derler: sabit rol + görev + globaller + bellek alt kümesi + saklananlar. Dönüş `source_refs`, statü etiketleri ve okunmayanlar listesi taşır. Alt ajan kanonik dosyaya yazmaz, aday yazar (M8, M16).
5. *Bakım:* INDEX lint'i (bayat satır, yetim dosya, kırık bağ), `superseded` işaretleri, derslerin terfisi ya da reddi (M17, M21).

**Mekanikleştirilebilir olanlar:** oturum başında STATE'i bağlama vermek; Stop hook'uyla "STATE güncellendi ve commit edildi mi" denetimi; ön bilgi şeması ve INDEX yolları için lint betiği. Arama dizini gerekmez, `grep` yeter; ileride FTS gerekirse oturumda yeniden kurulur, kanonik sayılmaz (ai-memory ilkesi).
**Yargıda kalacaklar:** terfi, çelişki çözümü, neyin unutulacağı, paketin içeriği.

---

## 4. Dersler

| # | Ne yanlış gitti | Kök neden | Önlem | Kaynak |
|---|---|---|---|---|
| D1 | AKS-00 başlığı "files 1–5 not yet researched" diye bayatladı; dosya içi "stop here" handoff'ları güncel yetki gibi okunabilir | durum içerik dosyalarına gömülü | tek yetkili STATE; INDEX düzeltmeyi söyler: "Treat that specific package-status line as a historical initiation snapshot" | AKS INDEX, AKS STATE §1 (*gözledim*) |
| D2 | Video ve kareler kayboldu; yalnız hash kaldı | çalışma girdisi oturum dosya sisteminde tutuldu | yük taşıyan türetilmiş bilgi repoya yazılır; hash kimlik içindir, byte'ları geri getirmez | VID STATE, SOURCE; `MEDIA-READING.json` `"repository_persists_original_media": false` |
| D3 | Ön değerlendirme sayıları kazanım gibi sunuldu, sonra geri çekildi | niteleme sinyali bulgu sanıldı | statü etiketi: PLANNED / ön niteleme / bulgu | EXP-003 STATE: "S009/S010'daki 100→180 ve 240–345 puanları … geri çekildi"; bütün META'lar |
| D4 | "CAG, RAG'dan hızlı ve iyi" başlığı kendi tablolarıyla çelişiyor | başlık iddiası tablolar okunmadan aktarıldı | kaynağın tablosunu oku | AKS-CAG §6.3: "sparse RAG top-3 her üç size'da da CAG'dan daha hızlıdır" |
| D5 | Benchmark betikleri ile paket sürümü uyuşmuyor | ürün hızlı değişiyor | commit'i sabitle, yeniden üret | META(context-mode): "`BENCHMARK.md` referenced some reproduction scripts not present … in the observed `package.json`" |
| D6 | Aynı terim farklı anlamda | CAG'nin üç açılımı; "working memory" videoda ve CoALA'da farklı; "sandbox" | DevOS sözlüğü; terim ilk kullanımda tanımlanır | AKS-CAG §2.1; VID RESEARCH §7 D01; META(context-mode) |
| D7 | Dev talimat dosyası işe yaramadı | "too much guidance → no guidance" | kısa harita, kademeli açılım, mekanik tazelik denetimi | CMH-03 §8 (OpenAI) |
| D8 | Ürün etiketi garanti sanıldı | Graphiti'de toplu giriş kenarları geçersizleştirmiyor | işlem yolu bazında doğrula | VID RESEARCH §7 D05 |
| D9 | Türetilmiş bilgi kendini kaynaklaştırıyor | köken ve statü taşınmıyor | `yazan`, `kaynak`, `statu` alanları | EXP-003 S008; CMH-02 §17 |
| D10 | Değerlendirici eklemek bağımsız doğrulama sanıldı | değerlendirici sorunu rasyonalize edip onaylayabiliyor | oracle ve kapsam ayrıca sınanır | CMH-03 §11 |
| D11 | Yerel sözleşme evrensel sanılabilir | `@codex implement` yayıncının otomasyonu | kaynağın kapsamını yaz | VID SOURCE |

---

## 5. Açık sorular ve bilinmeyenler

- SessionStart, PreCompact ve Stop hook'ları bulutta, çok repolu oturumda çalışıyor mu (R09→R01 satır 527)? Sıkıştırmada neyin korunacağı yönlendirilebiliyor mu? Oturum ortasında değişen CLAUDE.md bağlama yansıyor mu? → O11.
- Alt ajanın `memory: project` alanı bulutta commit'lenebiliyor mu? R09 açık soru 1 → O11.
- Bizim modelin DevOS paketleri için etkili bağlam uzunluğu ölçülmedi (AKS-LC §29).
- Hiçbir bellek mekanizması yerelde denenmedi. CMH-02 §18'deki gibi bir sınama seti yok.
- Aday sistemlerin gerçek davranışı *bilinmiyor* (context-mode snapshot içeriği, `memory_diff.json` biçimi, ai-memory devir şeması). Upstream okunmadan tasarıma taşınmamalı.
- Terfi kapısının sahibi kim: koordinatör mü, doğrulayıcı alt ajan mı? Batu teknik doğrulayıcı değil (K-015); cevap DevOS rol tasarımına bağlı.
