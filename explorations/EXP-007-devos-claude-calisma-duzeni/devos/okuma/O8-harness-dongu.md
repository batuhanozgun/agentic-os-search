# O8 — Harness ve döngü mühendisliği: ajan döngüsü, süreklilik, devam, değerlendirme, evrim

**Okuyan:** O8 okuma ajanı, EXP-007 DevOS okuma turu, 2026-09-27. **Soru:** Ajan döngüsü, oturum sürekliliği, devam ettirme, değerlendirme ve evrim için somut yapılar neler?
**Kanıt dili:** [kaynak diyor] / [gözledim] / [çıkarım] / [bilinmiyor]. **Kısaltmalar:** `CL1/` = `research/studies/the-carbon-layer/videos/mQfTdNVCOB0-harness-engineering/`; NoteNN = `CL1/notes/NN-*.md`; D01–D13 kimlikleri `CL1/evidence/2026-09-13-u02a-responsibilities/SOURCES.md`, D14–D22 `CL1/evidence/2026-09-15-u02b-coordination/SOURCES.md` içinde. K01–K12 ve "Batu gereksinimi" numaraları `O0-ana-oturum-okumalari.md` §4'ten.

## DevOS için en önemli çıkarımlar

1. Kümenin bütün içeriği tek yerde: `harness-engineering-and-evolution` yalnız yönlendirme; asıl çalışma `CL1/` (17 not, 34 kanıt dosyası). `deepseek-harness`, `cli-continues`, `claude-swap` yalnız aday kaydı; araştırma başlamamış, mekanizma vermiyorlar. [gözledim]
2. Kaynağın modeli: video 10 sorumluluk ve ayrı bir "ratchet" evrim döngüsü; Meta-Harness makalesi sabit model etrafındaki harness kodunu geçmiş izlere bakarak arayan dış döngü. Çalışmanın sonucu: bunlar katman değil, döngüsel etkileşen sorumluluklar; küçük bir iş birkaçını tek dosyada karşılayabilir. [kaynak diyor]
3. En güçlü aktarılabilir kural: "an improvement loop needs qualified feedback, not merely more feedback." Her kontrol sonucu hangi artefakta (commit SHA), hangi beklenen kümeye, hangi karşılaştırma tabanına ve hangi etkili yapılandırmaya ait olduğunu taşımalı. Meta-Harness kodunda bu bağ yok: yerel denemede eksik görev dizinleri başarı oranını 1.0'a çıkardı, 0.60→0.75 iyileşmesi özet dosyasına 0.0 yazıldı. (K05, K07) [kaynak diyor]
4. Devam ettirme kayıt geri yüklemekle aynı şey değil. Üç ayrı tuzak: kayıt ≠ dış etki (makbuz kaydedilmeden süreç ölürse tekrar deneme etkiyi ikiler); eski onay ≠ bugünkü izin; geçerli bayt ≠ doğru iş kimliği. DevOS'ta "etki bilinmiyor" ayrı bir durum olmalı; tekrar denemeden önce uzlaştırma yapılmalı (ör. push gerçekleşti mi?). (K09, K11) [kaynak diyor, analitik]
5. Sıkıştırma konuyu korurken yasağı düşürebilir: "prepare release" kalır, "do not deploy" düşer. STATE ve devir notu olumlu sonucun yanında açık soruları, dışlamaları, eylem kısıtlarını ve kanıta dönüş yollarını taşımalı; sıkıştırma sonrası kısıt-koruma kontrolü gerekir. (Batu gereksinimi 3) [kaynak diyor]
6. "The repository, not conversation recall, must support a cold start." Carbon Layer dosyaları bunu somut uyguluyor: tek yetkili yüzey tablosu, her STATE'te cold-start sırası, "next logical" ile "next authorized" ayrımı, eski notlardaki "next" cümlelerinin yetki sayılmaması. Makinenin geri alındığı ve bağlamın %80'de sıkıştığı bulut için doğrudan alınabilir. [kaynak diyor + gözledim]
7. Değişiklik üç türdür ve başarı kanıtları farklıdır: iş durumu / yeniden kullanılabilir bilgi-prosedür / çalışma politikası-harness. Ayrıca seçim ≠ kabul ≠ materyalizasyon ≠ tüketim ≠ etkinlik: skill dosyasını güncellemek alıcının onu aldığını ya da işin iyileştiğini göstermez. [kaynak diyor + çıkarım]
8. Evrim yolu: "observed failure → competing explanations → discriminating evidence → candidate intervention → evaluation under stated conditions → authorized acceptance or rejection → later observation". Değişmemek, sadeleştirmek, dersi emekliye ayırmak da meşru sonuç. Her hata kalıcı kural olmamalı; tetik seçimi gerekir. [kaynak diyor]
9. Doğrulama için hazır kalıp (U01-B, U03-C): çalıştırmadan önce SPEC, bilerek bozulmuş negatif kontroller (5 mutantın 5'i fark edildi), bayt-özdeş ikinci koşu, hash manifest, başarısız ilk koşunun saklanması. Batu'nun "kuralları bilerek çiğneyen denemelerle doğrulama" gereksinimine (6) birebir uyuyor. [kaynak diyor + gözledim: dosyalar]
10. Alt ajana devir paketi: amaç, kaynak kimliği (yol+SHA), bağlayıcı kısıtlar (yasaklar dahil), kabul beklentisi; dönüşte incelenen artefakt, kapsam, belirsizlik. Belgeye göre non-fork alt ajan ana konuşmayı, okunan dosyaları ve çağrılmış skill'leri almaz. Aynı prosedürü uygulayan ek ajan bağımsız doğrulama değil, korelasyonlu hatadır. [kaynak diyor]
11. Talimat ≠ zorlama: CLAUDE.md bağlamdır, zorlanan yapılandırma değil. Hook zamanlaması belirleyici: PreToolUse eylemi durdurabilir; PostToolUse sonradan görür; async hook engelleyemez; Stop normal bitişi, StopFailure ayrı çıkışı kapsar. Geri dönüşsüz eylemler hook/izin ile, tercihler talimatla. (Belge okuması 2026-09-13/15; O11 doğrulamalı) [kaynak diyor]
12. Kendini tamamlama ≠ doğrulama: incelenen ajanda çift `task_complete` aynı ajanın yeniden düşünmesi; smoke testi yalnız "çalıştı mı"; eylemden önce geçmişe `executed` yazılıyor. Üç yüzey ayrı kaydedilmeli: önerilen eylem, gözlenen etki, değerlendirici kararı. (K06) [kaynak diyor]
13. Ön-çıkarım ortam anlık görüntüsü (pwd, ls, sürümler) kodlama deneyinde öne çıkarılan otomatik bulunmuş ekleme; ama "fail-soft" hali başarısız `ls`'i "(empty directory)" diye yazdı. Oturum başı anlık görüntü alınacaksa her bölüm dönüş kodu ve "bilinmiyor" işareti taşımalı. (K10) [kaynak diyor]
14. Roadmap'in asıl sinyali: "evaluation infrastructure / operational evidence" boşluğu. DevOS neyi ölçeceğini yazmalı (kabul edilen teslim, yeniden iş, kullanım/maliyet, süre, sürüm-yapılandırma kimliği). Yönetişim "en son katman" değil, her adımı bağlar. [kaynak diyor + çıkarım]
15. Dersler (§4): çift yetki kaydı taşıma işine yol açtı; eşzamanlı main değişikliği non-force yayını reddettirdi; yüklenen medya kalıcı değil; roadmap görselinin repo kopyası geçerli görüntü değil ve hash'i kayda uymuyor. [kaynak diyor + gözledim]
16. Sınır: çalışma OPEN/PARTIAL; kendi SOUL/DevOS projeksiyonu (U06) hiç yapılmadı; canlı koşu ve bağımsız doğrulama yok. Aşağıdaki "DevOS: al/uyarla/alma" yargıları benim çıkarımımdır.

## 1. Kapsam

**Baştan sona okunan:**
- `research/studies/harness-engineering-and-evolution/`: 9 dosyanın hepsi (hepsi yönlendirme).
- `research/studies/the-carbon-layer/`: README, META, STATE, INDEX, METHOD, VIDEO-CATALOG, SOURCE-MAP, MIGRATION-2026-09-16, MIGRATION-VERIFICATION, syntheses/INDEX.
- `CL1/` kök: README, META, STATE, INDEX, RESEARCH-ROUTE, 00-WHY-THIS-RESEARCH, METHOD, RESEARCH-PLAN, SOURCE-LEDGER, BRIDGE-QUESTIONS.
- `CL1/notes/01…17` (17 not, ~210 KB).
- `CL1/evidence/`: MEDIA-MANIFEST.json; U01-A SOURCES, CHECKS-NOT-RUN; U01-B'nin 7 dosyasının hepsi (SOURCES, CHECKS, MANIFEST, checks/SPEC, probes.py, RESULT, EXCERPT-IDENTITIES); U02-A SOURCES, REVIEW, PUBLICATION, MEDIA-READING; U02-B SOURCES, REVIEW, MEDIA-READING; U03-A/B/C REVIEW; U03-C audit_reported_numbers.py; U04 SOURCES, REVIEW.
- `the-carbon-layer/videos/-01_NB4SbBY-agent-sandboxing/`: README, STATE, INDEX, RESEARCH, SOUL-DEVOS-ASSESSMENT.
- `deepseek-harness/META.md`, `cli-continues/META.md`, `claude-swap/META.md` (her paketin tek dosyası).
- `agentic-ai-systems-roadmap/`: INDEX, META, STATE, SOURCE-VISUAL, INITIAL-ASSESSMENT.
- Bağlam için: okuma `BRIEF.md`, `O0-ana-oturum-okumalari.md`.

**Kısmen okunan:** U03-C `ARITHMETIC.json` (ilk 60 satır).

**Okunmayan ve gerekçesi:**
- U03-A/B/C `SOURCES.md`, `REPORTED-DATA.json`, U03-A/B script ve `ARITHMETIC.json`: makale tablolarının elle aktarımı ve aritmetiği; sonuçlarını not 13–15 ve REVIEW'larda okudum; döngü sorusuna ek mekanizma yok.
- Sandboxing videosunun META, METHOD, RESEARCH-PLAN, SOURCE, `evidence/*`: içerik RESEARCH ve ASSESSMENT'ta okundu; genel yapı için yeterli.
- `PxuMqeIqCEo-agent-memory/` içeriği: O7 kümesinde; yalnız koleksiyon STATE'teki özetini gördüm.
- `agentic-ai-systems-roadmap/source/agentic-ai-systems-roadmap.jpg`: açılamadı. `file` çıktısı "data", 14.998 bayt, SHA-256 `9695899a…`; kayıttaki değer `b35a607c…`. İçeriği SOURCE-VISUAL.md transkripsiyonundan okudum. [gözledim]
- Üç aday hedefin upstream'i (deepseek-ai/deepseek-harness, yigitkonur/cli-continues, realiti4/claude-swap): `/home/user` altında klon yok; brief bu küme için web okuması tanımlamıyor.
- Dış birincil kaynakları (makale, video, Meta-Harness kodu, Claude Code/LangGraph/MCP belgeleri) yeniden açmadım; çalışmanın okuma kayıtlarından aktarıyorum.

**Kümenin durumu:** `CL1/STATE.md`: "OPEN / PARTIAL, checkpoint after U04". U05 (rakip açıklamalar, probe), U06 (Foundation ve SOUL/DevOS projeksiyonu), U07 (ters inceleme, CORE) yapılmadı. Notlardaki DevOS yorumları "provisional". Notlar ve kanıt ağaç kimlikleri taşıma kaydıyla aynı: `git rev-parse` notes = `b683a251…`, evidence = `8f80c512…`. [gözledim]

## 2. Kaynakların ana modeli (kısa)

**Video** (`mQfTdNVCOB0`, ~28 dk; 714 altyazı cue'su tam, seçili kareler; ses hizalaması yok). Sorumluluklar: Instructions, Context Delivery, Context Management, Tool Interface, Execution Environment, Durable State, Orchestration, Subagents, Skills & Procedures, Verification & Observability. Evrim ayrı döngü: "At approximately 25:14–26:26, repeated failures feed changes to retrieval rules, schemas, permission gates, tests, memory or reusable procedures. The diagrams at 26:00 and 26:45 label a separate ratchet loop." (Note12). 27:20 teşhis matrisi için çalışma: "Treat the rows as diagnostic leads, not one-to-one causal rules." [kaynak diyor]

**Makale** (Meta-Harness, arXiv 2603.28052v1): "`task/interface + baseline candidates → inspect prior experience → propose code → validate/evaluate → retain code/results/traces → propose again → select a candidate`" (Note01). Önerici Claude Code (Opus 4.6); çözücü model sabit. Üç deney: çevrimiçi sınıflandırma, matematik retrieval, TerminalBench kodlama.

**Çalışmanın sentezi** (Note16 §4, "Analytical synthesis; not a verbatim architecture from either source"):

```text
An authorized work objective and its constraints
  → select relevant information, methods and usable capabilities
  → act, observe, coordinate and preserve progress
  → judge the result against the actual work
  → retain useful evidence, uncertainty and unfinished responsibilities
                         ↓ when a change is worth investigating
Recover relevant experience and candidate explanations
  → propose a bounded change, including simpler/no-change alternatives
  → evaluate the identified candidate under stated conditions
  → compare and select, or reject/defer
                         ↓ not supplied by selection alone
Resolve acceptance authority and intended scope
  → materialize the accepted change for the actual consumer
  → check what that consumer now receives and can do
  → observe subsequent work, regressions and changed conditions
```

Özet cümle: "An operating arrangement enables work; an improvement loop proposes changes from experience; qualified reuse requires the right evidence and authority to survive into what a later worker actually receives and does."

## 3. Mekanizmalar

### M1. Tek yetkili yüzey tablosu ve durumsuz takma adlar
- **Sorun:** Aynı iş iki yerde durum taşıyınca hangi dosyanın karar verdiği belirsizleşir.
- **Nasıl:** Koleksiyon STATE'inde "| Concern | Sole authoritative surface |" tablosu; örnek satırlar: "Selected video, priorities and sequencing | This collection STATE", "Collection discovery | VIDEO-CATALOG, derived from child records". Eski konum yalnız işaretçi: "This directory contains **navigation only**. It has no independent research status, findings, evidence, continuation queue or completion authority." Eski derin yollar için önek kuralı: "replace `research/studies/harness-engineering-and-evolution/` with `research/studies/the-carbon-layer/videos/mQfTdNVCOB0-harness-engineering/`, keeping the suffix."
- **Yol:** `research/studies/the-carbon-layer/STATE.md`, `.../MIGRATION-2026-09-16.md`, `research/studies/harness-engineering-and-evolution/README.md`.
- **Kanıt:** MIGRATION-VERIFICATION: "All 51 note/evidence moves reported as renames with zero additions and zero deletions". Ağaç kimliklerini bu checkout'ta aynı buldum. [kaynak diyor + gözledim]
- **DevOS: Al.** Batu gereksinimi 4 ("tek asıl kopya"). Türetilmiş görünümler (katalog, pano) "derived" diye etiketlenmeli ve karar vermemeli.

### M2. Soğuk başlangıç sırası: "repo, sohbet hafızası değil"
- **Sorun:** Yeni oturumun eski sohbete ya da oturum dosyalarına dayanması.
- **Nasıl:** `CL1/METHOD.md` §9: "Save current authority, completed unit, genuine limitations and next executable research step. The repository, not conversation recall, must support a cold start." Her STATE'in sonunda "Cold start"/"Recovery" bölümü; koleksiyon STATE: "After current agent-control recovery, fully read this STATE, META, INDEX, METHOD and VIDEO-CATALOG." Ayrıca: "Do not recover a live media file from an old path or hash without checking its actual presence."
- **Kanıt:** Çalışma 2026-09-12…16 arasında birçok oturumda bu dosyalarla sürdü; birim yayın commit'leri kayıtlı. [kaynak diyor] Taze oturumla ölçülmüş geri kazanım testi yok. [bilinmiyor]
- **DevOS: Al.** Bulutta makine geri alınıyor, bağlam %80'de sıkışıyor. Cold-start sırası STATE içinde, kısa ve seçici olmalı ("descend only for the selected unit"). K01, K11, köprü koşulu 9.

### M3. "Next logical" ile "next authorized" ayrımı
- **Sorun:** Ajanın eski bir notta yazan "sıradaki iş"i kendiliğinden başlatması.
- **Nasıl:** `CL1/STATE.md`: "**Next logical work within this dossier:** U05. **Next authorized research execution:** none selected by the organizational repair." `CL1/README.md`: "Historical `next` statements in them are not current scheduling authority." Koleksiyon METHOD §5: "A useful next phase inside one dossier is not automatically the best or authorized next channel task."
- **Kanıt:** Kanal üçüncü videoya geçti, birinci videonun U05'i başlamadı; iki durum dosyası bunu tutarlı gösteriyor. [kaynak diyor]
- **DevOS: Uyarlayarak al.** DevOS'ta teknik sıralama ekibindir (K-015), yani "authorized" çoğu zaman Batu'yu değil iş seçme disiplinini gösterir. Alanlar: önerilen sıradaki iş / başlatılmış iş / Batu kabulü ya da kararı gereken iş (O0 §2 listesi). Tarihli notlardaki "next" STATE'i ezmez.

### M4. Birim planı, soru kaydı, iddia etiketleri, sınırlı kapanış
- **Sorun:** Araştırmanın dosya sayısıyla ilerlemiş sayılması; iddia, gözlem ve çıkarımın karışması.
- **Nasıl:** Birim tanımı (`CL1/METHOD.md` §2): "`intended need → input/authority → selection/configuration → caller/implementation → state/effect → observation/evaluation → failure/recovery → reuse boundary`". Evrim için ek: "who may change what; what stays fixed; where feedback comes from; candidate lineage; evaluator ownership; selection and deployment authority." "A file-count quota is not a research unit." Plan tablosunda her birimin "Actual standing" alanı (U00–U07) ve Q01–Q14 soru kaydı. Etiketler (§4): "TARGET CLAIM for what authors say; OBSERVATION for what is present in a specified document/code/frame; INFERENCE for our interpretation; HYPOTHESIS/OPEN for an untested explanation; EXECUTED RESULT only with actual run identity and artifacts." Kapanış (§8): "No percentage complete from pages, files, tokens or tests."
- **Kanıt:** U00–U04 teslim edildi, U05–U07 açık. [kaynak diyor]
- **DevOS: Uyarlayarak al.** Etiketler Batu'nun kayıt düzeni gereksinimine (4) oturur. Araştırma yöntemi geliştirme işi için ağır; birim tanımı kısaltılmalı. Uyarı: bu çalışma 5 günde 17 not üretti ama proje projeksiyonuna (U06) ulaşmadı (bkz. D8).

### M5. Yayın protokolü: sınırlı commit, force yok, diff, geri okuma
- **Sorun:** "Yazdım" demekle uzak depoda gerçekten var olmak arasındaki fark; eşzamanlı değişikliği ezmek.
- **Nasıl:** Koleksiyon METHOD §8: "Build a bounded commit over current main, preserve unrelated research, advance without force, inspect the actual diff and read back canonical entrypoints. A prepared tree or a successful write response alone is not verified publication." `CL1/METHOD.md` §9: "Rebase the bounded delta if another study publishes concurrently; never restore an older shared file wholesale."
- **Kanıt:** `CL1/evidence/2026-09-13-u02a-responsibilities/PUBLICATION.md`: "The first prepared commit, `3a6182ab…`, was not published to main: its non-force ref advance was rejected as not fast-forward. No force update or helper branch was used." Taze main'de yalnız HERMES planı değişmişti; o dosya korunarak yeniden taban alındı. [kaynak diyor]
- **DevOS: Al.** K11 (yerel çıktı, commit, push, uzak içerik ayrı gösterilir). Bulutta atanmış dala push + `git fetch` ile uzak geri okuma; birden çok yazıcı varsa tek yazıcı kuralı (K09).

### M6. Ön-SPEC, negatif kontrol, deterministik tekrar, hash manifest, başarısızlığı saklama
- **Sorun:** Bir kontrolün gerçekten hatayı yakalayabildiğini ve sonradan ölçüt gevşetilmediğini göstermek.
- **Nasıl:** `checks/SPEC.md` koşudan önce yazıldı ("Status at creation: specified, not run."): hedefler, dışlamalar ("No credentials, dependency installation or upstream quick-start execution"), B01–B08 soruları ve beklenen gözlemler. Negatif kontroller: "missing-result default changed to one; threshold `r > 0` changed to `r >= 0`; source comparator changed from post-update to predeclared 0.60; incomplete LS label suppressed; shell `.env` sourcing removed." `probes.py` kaynak fonksiyonlarını AST hash'iyle doğrular, yalnız seçili fonksiyonları derler, kabuk betiğini sahte `uv` ile geçici kökte çalıştırır; sonuçta `assert all(mutants.values()), mutants`. `RESULT.json`: `"groups_completed": 8`, `"negative_controls_discriminated": 5`. `CHECKS.md`: "Two runs produced byte-identical stable RESULT.json." Dürüst sınırlar: "this is not blinded confirmatory testing. No criterion was relaxed after an unfavorable result."
- **Başarısızlığı saklama:** U03-C'de yanlış yazılmış beklenen değer ilk koşuyu durdurdu; düzeltme "post-observation repair" diye kayıtlı (D3). Betik yanlış girdileri de reddediyor ("different model", "different scope", "nonfinite rate", "incomplete group declaration").
- **Yol:** `CL1/evidence/2026-09-12-u01b-terminalbench/{CHECKS.md,MANIFEST.json,checks/*}`, `CL1/evidence/2026-09-16-u03c-coding/`.
- **Kanıt:** Koşu kayıtları [kaynak diyor]; ben yeniden koşmadım.
- **DevOS: Uyarlayarak al.** Batu gereksinimi 6 için hazır kalıp: her hook/kontrol için önceden yazılmış beklenen sonuç + "bozuk girdi yakalanmalı" negatif testi + sonuç dosyası hash'i; platform güncellenince aynı betik yeniden koşulur. Başarısız koşu ve ölçüt değişikliği silinmez (K07).

### M7. Meta-Harness dış döngüsü: dosya aracılı aday arama
- **Sorun:** Sabit model etrafındaki harness'i geçmiş deneyime bakarak otomatik iyileştirmek.
- **Nasıl (sınıflandırma referansı, Note03):** `run_evolve` `config.yaml` okur, adlı log dizini açar; "`pending_eval.json`, `frontier_val.json`, `evolution_summary.jsonl`, `results/` and `finalized.json` are scoped to that run. Candidate Python files remain in the shared `agents/` directory." Her öneriden önce eski `pending_eval.json` silinir: "A successful wrapper exit plus a newly present file admits the next parsing step." Önerici: "`propose_claude` invokes `claude_wrapper.run` with a loaded proposer skill, an Opus model label, a working directory and tools including Read, Grep, Write, Edit, Bash and Agent. The wrapper injects the skill into the system prompt". TerminalBench skill'i (Note05): "one candidate and one mechanism per iteration. It uses one Agent subagent for analysis and another for implementation … It asks the analyst to inspect successful as well as failed trajectories, predict both success and efficiency changes, and preserve a falsifiable hypothesis." Aşamalar: import testi → sınıf bulma → benchmark → frontier (doğruluk × bağlam uzunluğu Pareto) → ayrı final: "writes an in-progress marker … Only after successful completion is the marker changed to complete." "A completed marker blocks further evolution under that run name. An in-progress marker does not."
- **Ön koşullar:** "`ONBOARDING.md` asks for the task unit, fixed model and tool boundary, mutable interface, evaluation split, baselines and budget before an implementation is specified. It also warns that an unstable evaluation loop or a need primarily to change the model can make this approach a poor fit."
- **Kanıt:** Makaleye göre ham iz erişimi özetten iyi: "Scores Only … Scores + Summary … The full interface adds trace access. Reported median/best accuracies are 34.6/41.3, 34.9/38.7 and 50.0/56.7" (tek deney, tekrar yok). Kodlamada Opus 4.6 için KIRA'ya göre +1.7 puan (74.7→76.4); arama ve final "the same 89 tasks". Kod için: "the code was cleaned up and testing was limited to checking that it runs." Zayıf yan: "its wrapper command disables interactive permission checks"; "a cooperative research arrangement, not demonstrated adversarial isolation." [kaynak diyor]
- **DevOS: Kavramı uyarlayarak al, aracı alma.** Alınacak: makbuz dosyası kabulü (eski silinir, temiz çıkış + yeni dosya), öneri başına tek mekanizma + yanlışlanabilir hipotez, başarılı ve başarısız izleri birlikte inceleme, ayrı ve kilitli final değerlendirme, ham izlerin özet yerine erişilebilir tutulması. Alınmayacak: otomatik harness kodu araması (sabit benchmark ve bütçe yok), izin denetimini kapatan wrapper. Bulut: analist + uygulayıcı alt ajan deseni yalnız ana oturumdan açılabilir (derinlik 1).

### M8. Değerlendirmeyi bağlama kuralları (kod okuması ve yerel denemeler)
- **Sorun:** Doğru görünen bir skorun yanlış nesneye, eksik kümeye ya da kaymış tabana ait olması.
- **Bulgular [kaynak diyor]:**
  - Küme: "the parser is driven by discovered directories, not an independently enumerated expected task/attempt manifest." B02: bir görevin bütün dizinleri silinince ortalama 1.0 oldu, uyarı çıkmadı, eksik aday tam 0.75 tabanını geçti.
  - Taban: B04 "Stored delta was 0.0, not the independently calculated 0.15."
  - Kimlik: "`_has_usable_result` finds a dictionary with numeric accuracy. The address is based on dataset, candidate name, short model name and seed." Kod değişse de eski sonuç yeniden kullanılır.
  - Yapılandırma: B07'de yerel `.env` modeli `synthetic/parent` → `synthetic/override` yaptı.
  - Tüketici: "`harbor_run` returns no success signal on timeout. Candidate evaluation checks it. Baseline seeding later parses whatever directory exists".
  - Kısmi final: tamamlanmamış final evrime dönüşe izin veriyor; bazı test sonuçları çıkmış olabilir (F04).
- **DevOS: Al (kural olarak).** Her doğrulama kaydı: artefakt kimliği (commit SHA ya da dosya hash), beklenen küme ile gerçekleşen küme ayrı, karşılaştırma tabanı ve zamanı, etkili yapılandırma (model, ortam). Kimlik ya da ölçüt değişince eski PASS geçersiz. "Controls must compose across the consumer boundary, not merely exist inside a helper." K05, K06, K07.

### M9. Ortam önyükleme (ilk model çağrısından önce anlık görüntü)
- **Sorun:** Modelin ilk turlarını ortamı keşfetmeye harcaması.
- **Nasıl (Note07):** `_gather_env_snapshot` döngüden önce çağrılır. "A single compound command emits section markers and collects `pwd`, `ls -la /app/`, selected language/compiler versions, selected package-manager versions and memory information. The inner exec has a 15-second timeout and the async wrapper 20 seconds. Exceptions/no session/empty output return no snapshot". Liste 25 satırı geçince ilk 20 satır + "more files" etiketi.
- **Kanıt:** Makalede otomatik bulunan ana ekleme; net katkısı ayrıştırılmadı. Yerel deneme (B05/B08): "The `&&` chain stopped before the later sections; the final `|| true` produced exit zero. Feeding that actual partial stdout to the snapshot method again produced the empty-directory label." İlk isteğe girdiği de gösterilmedi: "The snapshot can be appended successfully yet later be replaced by a proactive-summary prompt." [kaynak diyor]
- **DevOS: Uyarlayarak al.** Oturum başında kısa ortam + repo görüntüsü (dal, HEAD, `git status`, araç sürümleri). Setup script önbellekli ve resume'da çalışmıyor (O0 §5), bu yüzden SessionStart tarafı düşünülmeli (O11). Her bölüm dönüş kodu taşır; hata "bilinmiyor" yazılır, "boş" değil. Sabit liste yerine görev koşullu keşif alternatif olarak kalsın. K10.

### M10. Sürekli durum ve nitelikli devam
- **Sorun:** Kesintiden sonra doğru yerden, doğru yetkiyle, etkiyi ikilemeden devam etmek.
- **Nasıl (Note10 tablosu, "What storage alone does not establish" sütunuyla):** "Progress checkpoint | Recover work position and completed results | External effects agree with the checkpoint"; "Learned note or lesson | Guide similar future work | Its generalization is valid or authorized as a rule"; "Action/result receipt | Reconcile an attempted operation | The target has not changed since observation"; "Conversation summary | Reconstruct a usable working view | All decisive constraints and unknowns survived".
- **Üç tuzak:** S1 "a worker publishes a package … then the process stops before saving the returned receipt. Its checkpoint still says publication is pending. Replaying that step can repeat an already completed effect." Çözüm adayları: "a stable operation identity understood by the service, a postcondition query, or human escalation". S2 "Replaying the same historical decision can correctly reproduce what was approved then without establishing what is permitted now." S3 "Loading a well-formed checkpoint for a different task or thread can recover valid bytes but the wrong work." Kesinti örneği: "an acknowledgment is lost; its summary compresses 'effect unknown' into 'failed'; a later worker reads that summary and retries." Araç düzeyi (Note09 T1): "A transport timeout cannot distinguish 'nothing happened' from 'effect occurred, acknowledgment missing'."
- **Birincil belge (çalışmanın okuması):** LangGraph'ta "resumption re-enters the entrypoint and restores completed task results. A task that started but did not complete can run again; its guidance therefore separately calls for idempotent side effects."
- **Koşul cümlesi:** "A useful continuation needs the current work and constraints, appropriately selected evidence, an admitted operation in the right environment, and a recoverable account of what happened and what remains uncertain."
- **Kanıt:** Analitik; çökme/kurtarma testi yok. [bilinmiyor]
- **DevOS: Al.** Bulutta VM süresi dolunca konuşma dönüyor ama alt ajan ve shell işleri dönmüyor (O0 §5). Buna göre: dış etkiden (push, PR, yorum) hemen sonra makbuz (SHA, URL) dosyaya; yarım iş "etki bilinmiyor" diye işaretlenir; devamda önce uzlaştırma (`git ls-remote`, PR listesi), sonra yeniden deneme; devam kaydı iş kimliğini (dal + iş no) taşır; eski onay yeni etki için yeniden sınanır. K09, K10, K11.

### M11. Bağlam teslimi ve yönetimi: karar-ilgili anlamı korumak
- **Sorun:** Kaynağın "erişilebilir" olmasıyla isteğe doğru biçimde girmesi arasındaki fark; özetin kısıt kaybetmesi.
- **Nasıl (Note08):** Durumlar: "A source can be listed but unread, readable but omitted, included but obsolete, or accurately presented but misunderstood." M1: "a compacted note preserves 'prepare release' but drops 'do not deploy'. … A word-count or topic-overlap check would not discriminate this error. A constraint-retention check against the source would." Öneri: "retain not only positive conclusions but unresolved questions, exclusions, action constraints and routes back to evidence".
- **Kanıt:** Analitik + belge (Anthropic bağlam mühendisliği yazısı); deney yok. [kaynak diyor]
- **DevOS: Al.** STATE ve devir şablonunda zorunlu alanlar: bağlayıcı kısıtlar, açık sorular, dışlananlar, kanıt yolları. Sıkıştırmadan sonra kısıt listesinin yeniden yüklendiği bir mekanizma (hook olayı O11'e bağlı). Batu gereksinimi 3.

### M12. Talimat, yükleme ve zorlama; hook zamanlaması
- **Sorun:** Kuralın yazılı olması, yüklenmesi, doğru yorumlanması ve eylem yolunda zorlanması farklı şeyler.
- **Nasıl (Note08 dört soru):** "Is the intended rule recorded accurately? Did the client load the rule for this directory/session/task? Was the rule retained and interpreted correctly in the relevant model call? Does the relevant action path enforce a constraint when model compliance is insufficient?" Claude Code belgesi (D01): "CLAUDE.md and automatic notes as context, not enforced configuration; … AGENTS.md is not automatically its instruction filename." Hook belgesi (D16): "PreToolUse can control admission; PostToolUse runs after the operation; Stop and SubagentStop concern normal completion, while StopFailure handles a different exit; asynchronous hooks cannot block the triggering action." I2: "Treating all visible text as equally instructive would erase the difference between a rule, a quoted request and untrusted work data."
- **Kanıt:** Belge okuması, çalıştırma yok. [kaynak diyor]
- **DevOS: Al.** Batu gereksinimi 1 ve 2; K08. Geri dönüşsüz eylemler PreToolUse/izin ile; görünürlük PostToolUse kaydı ile; hata çıkışı için ayrı olay. Her kural için "talimat mı, zorlama mı" gerekçesi. Belge ayrıntıları O11'de doğrulanmalı.

### M13. Alt ajana devir ve bütünleştirme
- **Sorun:** Dar bağlamla giden işin belirleyici kısıtı kaybetmesi; farklı revizyonlara ait raporların birleştirilmesi.
- **Nasıl (Note11):** "Our inference is that a delegated job needs enough purpose, source identity, constraints and acceptance expectations for its recipient to act correctly." "The return path matters equally: a worker supplies a result and its evidence limits; the integrating owner decides whether it addresses the assigned question." Claude Code (D18): "non-fork subagents: they do not inherit the parent's conversation, read files or previously invoked skills. Fork mode is an explicit exception. Configured skills can be preloaded". A1: "a specialist receives a narrow code-review request but not the prohibition on deployment." A2: "two workers return individually accurate reports about different revisions." P1: "every specialist faithfully applies the same outdated procedure. … Agreement among these workers is not independent confirmation."
- **Kanıt:** Belge + analitik. [kaynak diyor]
- **DevOS: Al.** Devir paketi ve dönüş paketi şablonu (incelenen yol/SHA, kapsam, bulunamayan, belirsizlik). Ana oturum raporların aynı revizyona ait olduğunu kontrol eder. Derinlik 1: bölme işi ana oturumda. K02, K04, K05, Batu gereksinimi 8.

### M14. Doğrulama, gözlemlenebilirlik, teşhis ayrı işler
- **Sorun:** Emin bir son cevabın, log hacminin ya da ajanın "bitti" demesinin kabul kanıtı sanılması.
- **Nasıl (Note12):** "**Verification** asks whether specified evidence supports a particular claim about a particular result." "**Observability** makes relevant events and dependencies inspectable. More logs can reveal the point at which a workflow diverged, but log volume does not establish correctness." "**Diagnosis** explains why the failure arose and what intervention could change it." V1: testler doğru ama C0 revizyonunda, yama C1. V3: iz yok diye araç çalışmadı sanmak.
- **Kodda somut örnekler (Note05–06, 15):** Smoke testi: "Its acceptance checks successful launcher exit, a top-level result file and zero reported errors, not positive task reward." Protokol: "append tool-result text `executed` to chat history before the outer agent loop actually performs commands". "The double `task_complete` confirmation is a same-agent reconsideration gate. It is not the task verifier's verdict or independent review." Dış doğrulayıcı: path-tracing görevinde "The shell writes a binary reward from pytest's exit status."; "Figure 9's completion-checklist pass is the worker's internal completion path, not this task's separate pytest result."
- **Kanıt:** Kod ve test kaynağı okuması + belge; ajan koşusu yok. [kaynak diyor]
- **DevOS: Al.** Kabul = aynı revizyonda ayrı başlatılmış değerlendirme (K06). Kayıtta üç yüzey ayrı: önerilen eylem, gözlenen etki, değerlendirici kararı. Koşmayan ya da atlanan test yeşil sayılmaz.

### M15. Evrim döngüsü: nitelikli değişiklik
- **Sorun:** Tekrarlayan hatayı sistem değişikliğine çevirirken yanlış teşhis, aşırı uyum ve gerilemeyi önlemek.
- **Nasıl:** Video (Note01): "The final practical question is broader than whether the model was capable: where did the surrounding system fail?" Dayanak (D21, SRE postmortem): olay kaydı, katkı nedenleri, önleyici eylem, gözden geçirilmiş takip; sürecin maliyeti ve "deliberate trigger selection". Çalışmanın yolu (Note12): "`observed failure → competing explanations → discriminating evidence → candidate intervention → evaluation under stated conditions → authorized acceptance or rejection → later observation`." Üç değişiklik türü (Note16 §3): "Current work state | … | A reusable method has improved."; "Reusable knowledge or procedure | … | The lesson is applicable, correctly loaded or beneficial on future work."; "Operating policy or executable harness | … | The candidate is accepted, installed or actually used by the intended consumer." (üçüncü sütun: tek başına kanıtlamadıkları).
- **Uyarılar:** "A winning candidate is still separate from permission to modify the working system." "Replaying the motivating incident can show that a candidate addresses that instance. It does not alone establish transfer or absence of regressions." Gözlem de değişebilir: "a context-saving policy might keep fewer records of failed attempts. A review based only on retained results could look better without any increase in actual task success." "Retiring or narrowing a lesson can therefore be improvement too." Araştırma kütüphanesi girdi olabilir: Appendix D "making relevant prior experience, solved-example corpora and research papers navigable to the proposer" önerir ama "engineering lessons rather than scientific claims".
- **Kanıt:** Analitik; hiçbir evrim döngüsü çalıştırılmadı. [bilinmiyor]
- **DevOS: Uyarlayarak al.** DevOS "kendi çalışma sistemini yönetilen koşullarda geliştirir" (O0 §3). Somut akış: olay kaydı (ne oldu, rakip açıklamalar, ayırt edici kanıt) → aday değişiklik (skill, hook, şablon ya da kaldırma) → motive eden olay + bozulmaması gereken meşru durumlarda deneme → kabul (kimin yetkisi olduğu DevOS dokümanında tanımlanmalı) → materyalizasyon kontrolü (yeni oturumda gerçekten yükleniyor mu) → sonraki gözlem. Kural değişikliği kayda geçer (O-20); köprü koşulu 10 ("kendi kabul kurallarını sessizce değiştirmeden").

### M16. Skill/prosedür yaşam döngüsü ve materyalizasyon
- **Sorun:** Dersin skill'e yazılmasının onun kullanıldığı ve işe yaradığı sanılması.
- **Nasıl:** Note11: "stored, discoverable, loaded, applicable, followed and effective are not equivalent states." Agent Skills spec (D17): "allowed-tools field is experimental and support varies by implementation; format validation checks package structure, not successful task performance." HERMES (Note17): `_skill_view_with_bump` "increments view/use counters for the resolved skill" — bakım anlamı var, etkinlik ölçüsü değil. GSTACK: "prepare a candidate rendering outside the canonical checkout, preserve the live representation on a failed preparation path, and switch the live path after successful preparation."
- **Kanıt:** HERMES handler'ı ve GSTACK test kaynağı okundu, koşulmadı (Note17, U04 SOURCES). [kaynak diyor]
- **DevOS: Al (ayrımlar).** Skill değişikliğinden sonra iki ayrı kontrol: materyalizasyon (yeni oturumda ya da alt ajanda gerçekten listeleniyor/önyükleniyor mu) ve etkinlik (sonraki işte sonuç). Görüntülenme sayısı başarı ölçütü değil. Bulutta bileşenler proje dosyası olduğu için hazırlık dalda, canlıya geçiş birleştirmeyle olur. [çıkarım]

### M17. Operasyonel kontrol döngüsü ve değerlendirme altyapısı (roadmap)
- **Sorun:** Çalışan sistemin hâlâ başarılı, doğru yapılandırılmış ve devam etmeye yetkili olup olmadığını sürekli bilmek.
- **Nasıl (`agentic-ai-systems-roadmap/INITIAL-ASSESSMENT.md`):**
```text
execute
→ observe
→ measure / evaluate
→ determine standing / risk
→ constrain or change policy
→ retry / route / approve / deploy / stop / adapt
→ execute again
```
  Öncelik: "**Agentic Evaluation Infrastructure / Operational Evidence & Qualification** — highest information value and least cleanly covered as its own study." Katman eleştirisi: "Governance is probably not “last”"; "Evaluation and observability are not merely post-build". Yeni konu için sınıflama kuralı (INDEX): "already well covered by an existing study; fragmented across studies and needing synthesis; genuinely under-researched and worthy of a new focused-topic package; later-phase design/implementation concern that should wait for authorization."
- **Kanıt:** Uygulayıcı infografiği + ilk değerlendirme; derin araştırma yok. [kaynak diyor]
- **DevOS: Uyarlayarak al.** DevOS'un ölçtüğü şeyler yazılmalı: kabul edilen teslim, yeniden iş, kullanım/maliyet, süre, sürüm ve yapılandırma kimliği. Sınıflama kuralı repo çöplüğünü önler (O-18).

### M18. Yürütme ortamı ve etki alanı (sandboxing videosu)
- **Sorun:** Yanlış bir eylemin zararının nerede durduğunu bilmek.
- **Nasıl (`the-carbon-layer/videos/-01_NB4SbBY-agent-sandboxing/RESEARCH.md`, `SOUL-DEVOS-ASSESSMENT.md`):** Üç soru: "agent nerede çalışıyor; neye dokunabilir; insan veya politika durdurana kadar ne kadar şey yapabilir?" Ana ayrım intent/containment. Beş ilke: "kapalı varsayılanlarla başlamak; dosya ve ağı birlikte ele almak; çocuk süreç ağacını kapsamak; sınırı etki alanına göre seçmek; güvenli yolu kolaylaştırmak." Kritik karşı örnek: "agentın geçerli üretim API anahtarı ve izinli bağlantısı varsa, normal HTTPS çağrısıyla üretim verisini silebilir." Gecikmiş etki: "Üretilmiş değişikliği sonradan yüksek yetkiyle çalıştıran CI veya insan da ayrı bir tüketicidir." Onay yorgunluğundaki %84 yalnız izin istemi sayısındaki düşüş, risk azalması değil. Note09'un üç boyutu: "Usability", "Authority: may this actor perform this operation on this target now?", "Containment".
- **Kanıt:** 859 cue tam okuma + belge kontrolleri; sandbox testi yok; Batu araştırmayı "uygun" buldu (güvenlik onayı değil). [kaynak diyor]
- **DevOS: Uyarlayarak al.** Bulut konteyneri yerel etki alanını sınırlar; GitHub kimliği ve izinli dış API ayrı soru (hangi token hangi repo/dalda ne yapabilir). Batu rutin adımları onaylamamalı; yalnız O0 §2'deki anlamlı sınır geçişleri ona gelir. CI ayrı tüketici olarak ele alınmalı.

### M19. Aday hedefler (yalnız kayıt, araştırma yok)
- **deepseek-harness:** kayıt sinyalleri "append-only session/event sourcing and reconstruction of model-visible history", "continuable subagent/delegation mechanisms"; ama "qualification signals, not research findings" ve "developer-preview software with compatibility-breaking changes expected". **DevOS: Şimdilik alma**; olay kaynaklı oturum fikri için ileride bakılabilir. [bilinmiyor]
- **cli-continues:** "discovers native AI coding sessions, parses heterogeneous session formats, supports same-tool native resume and builds structured handoff context for continuation in another coding agent." Asıl soru: "whether cross-agent continuation is fundamentally a session-transcoding problem, a work-state handoff problem, or a composition of both." Uyarı: "Current checkout/repository truth must not be assumed equivalent to historical session state." **DevOS: Aracı alma** (tek araç, Mac'e bağlanmamalı); **fikri al**: devam = iş durumu devri + güncel repo ile uzlaştırma, transkript taşımak değil.
- **claude-swap:** hesaplar arası geçiş, "usage-aware automatic switching"; "Registration is not endorsement of quota circumvention or account-policy bypass." **DevOS: Alma.** Kimlik bilgisi ve hesap Batu kararı (O0 §2); politika riski.

## 4. Dersler

- **D1 Çift yetki.** Ne oldu: ilk videonun araştırması kardeş pakette kaldı, video klasörü takma addı. "the layout and copied continuation checkpoints made one source dossier appear to be another independent research line. The assistant's phrase another research reinforced that ambiguity." Kök neden: kaynak kimliği ile iş sahipliğinin ayrılmaması, durum kopyalama. Önlem: bir iş nesnesi = bir kanonik ev; takma ad yalnız işaretçi; taşıma kaydı + ağaç kimliği doğrulaması. Kaynak: `the-carbon-layer/MIGRATION-2026-09-16.md`.
- **D2 Eşzamanlı yazım.** Ne oldu: non-force yayın "rejected as not fast-forward". Kök neden: paylaşılan main'e paralel yazım. Önlem: taze main, sınırlı delta, force yok, geri okuma. Kaynak: U02-A `PUBLICATION.md`. DevOS'ta çok oturum/alt ajan yazıyorsa tek yazıcı (K09).
- **D3 Elle yazılmış beklenen değer.** 6800.5 yerine 6801.5. Önlem: bağımsız ikinci türetme ("integer-tenths arithmetic"), başarısızlığı saklama. Kaynak: U03-C `REVIEW-AND-LIMITS.md`.
- **D4 Kalıcı olmayan girdi.** "No original video/audio file was present under `/mnt/data` when checked during this setup." Kök neden: oturum dosyası ≠ repo. Önlem: hash + kurtarma yolu kaydı; kalıcı olması gereken repoya. Bulutta aynen geçerli. Kaynak: `the-carbon-layer/SOURCE-MAP.md`, `CL1/evidence/MEDIA-MANIFEST.json`.
- **D5 Bozuk repo varlığı.** Roadmap görselinin repo kopyası JPEG değil; SHA kayıtla tutmuyor. Kök neden bilinmiyor (sığ klon; yol yalnız `23280ab` commit'inde görünüyor). Önlem: kayıtlı hash okuma anında doğrulanmalı; "File existence is insufficient." (O0 §4.3). [gözledim]
- **D6 Belge yolları değişiyor.** "Codex's AGENTS.md guide redirected; LangGraph's old durable-execution route redirected to a persistence landing page". Önlem: platform iddiası tarih + URL ile; kullanımda yeniden doğrulama (Batu gereksinimi 9). Kaynak: U02-A `REVIEW-AND-LIMITS.md`.
- **D7 Yardımcıdaki güvenli dönüşü tüketici atabilir.** Zaman aşımı sinyali aday yolunda kontrol ediliyor, taban ve final yollarında atılıyor (E02). Önlem: bir kontrolün sonucu onu tüketen her yolda sınanmalı. Kaynak: Note05–06.
- **D8 Sınırsız derinleşme riski.** Yöntem uyarıyor: "Do not replace a video-by-video goal with an indefinitely expanding implementation or benchmark inquiry." Yine de çalışma proje projeksiyonuna (U06) ulaşmadan kanal başka videoya geçti. Önlem: kullanım amacına yönelik projeksiyonu erken yap; sınırlı kapanış ölçütü koy. [çıkarım] Kaynak: koleksiyon METHOD §5, `CL1/RESEARCH-PLAN.md`.
- **D9 Aynı modelin incelemesi bağımsız değil.** "Same-model adversarial review is not independent verification." DevOS'ta ayrı başlatılmış değerlendirme de aynı model olabilir; bağımsızlık derecesi kayda yazılmalı (K06). Kaynak: `CL1/METHOD.md` §8.

## 5. Açık kalanlar ve kapsam boşlukları

- Çalışmanın kendi DevOS projeksiyonu (U06) yok; canlı koşu, bağımsız doğrulama, maliyet ölçümü, çökme/kurtarma testi yok. U01-A'nın P01–P07 denemeleri koşulmadı.
- Üç aday hedefin (deepseek-harness, cli-continues, claude-swap) upstream'i okunmadı; somut şema ya da kod yok. cli-continues'un devir belgesi yapısı DevOS devir şablonu için bakılmaya değer olabilir. [çıkarım]
- DevOS'ta süreç değişikliğini kimin kabul edeceği bu kümede cevaplanmıyor. [bilinmiyor]
- Hook olay adları ve alt ajan bağlam davranışı 2026-09-13/15 belge okumaları; güncelliği O11'de doğrulanmalı.
