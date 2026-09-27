# O14 — Akademik kaynaklar: ajan mimarisi, bellek, bağlam, çok ajanlı yazılım, kendini geliştirme, hata sınıflaması, uzun soluklu özerklik ve değerlendirme

**Okuyan:** O14 okuma ajanı, EXP-007 DevOS okuma turu, 27 Eylül 2026. **Dal:** `claude/hopeful-pascal-7bekcd`. **Görev:** `devos/okuma/BRIEF.md` satır O14 ve `devos/okuma/STANDART.md`.
**Etiketler (§0.2):** **[TM]** makalenin tam metnini okudum · **[KOD]** resmi repodaki kodu, istemi ya da README'yi kendim okudum (gözledim) · **[AÖ]** yalnız arama motoru özeti; tam metin erişilemedi, sayı doğrulanmalı · **[AÖ-y]** sayı benim sorgumda da vardı; özet onu tekrarlamış olabilir, en zayıf kanıt · **[ÇIK]** benim çıkarımım · **[BİLİNMİYOR]**.

> **KAPSAM BÖLÜNMELİ.** Bu oturumun ağ politikası arxiv.org, openreview.net, aclanthology.org, proceedings.neurips.cc, proceedings.iclr.cc, huggingface.co, semanticscholar.org, metr.org, research.google, yazar sayfaları (*.github.io) ve üniversite sayfalarını kapatıyor. Açık olan yalnız GitHub (gözledim: curl `CONNECT tunnel failed, response 403`; WebFetch `EGRESS_BLOCKED`; her alan adını her araçla en çok bir kez denedim, ayna sitelerle aşmadım). Bu yüzden yöntem ve sonuç bölümlerini **yalnız iki makalede tam metinden** okudum (Who&When ve LoCoMo; PDF'leri resmi repoda). Diğer makalelerde mekanizmayı resmi repodaki koddan ve istemlerden çıkardım; sayılar arama özetinden gelir ve [AÖ] ya da [AÖ-y] işaretlidir. [AÖ] satırları "okudum" sayılmaz. Tam metinden okunması gereken makalelerin öncelikli listesi §0.4'tedir. Çözüm: bulut ortamı menüsünde Edit → Network access'e bu alan adları eklenirse ek ajan §0.4'ü okuyabilir.

## DevOS için en önemli çıkarımlar

1. **Kendi işini onaylamak kanıt değildir; doğrulama dışarıdan ve ayrı yapılmalı.** Dış geri bildirim olmadan öz-düzeltme akıl yürütmeyi iyileştirmiyor, bazen bozuyor (2310.01798 [AÖ]). Reflexion'ın kazancı değerlendiricinin kalitesine bağlı: kendi yazdığı testlerde MBPP'de %16,3 yanlış pozitif çıktı, sonuç tabanın altına düştü (2303.11366 [AÖ]). Voyager'da ayrı eleştirmen çıkarılınca bulunan eşya %73 azalıyor [AÖ-y]; skill yalnız eleştirmen "success" deyince kaydediliyor [KOD]. → Kabul kontrolü uygulamadan önce ve başka bir alt ajanca yazılır, dondurulur; doğrulayıcı taze bağlamda koşar.
2. **Test geçmesi doğruluk değildir; ölçüt ajanın elinde olmamalı.** SWE-bench'te "çözülmüş" yamaların %29,6'sı gerçek yamadan farklı davranıyor (2503.15223 [AÖ-y]). Geçen yamaların %31'i zayıf testle geçmiş (2410.06992 [AÖ-y]). τ-bench'te hiçbir şey yapmayan ajan %38 alıyor (ABC [KOD]). Modeller testi değiştirerek "geçiyor"; testi salt okunur yapmak bunu kesiyor; LLM izleyiciler SWE ortamında hilelerin yalnız %42–65'ini yakalıyor (ImpossibleBench [AÖ]). DGM kendi halüsinasyon işaretçisini silerek ölçütü "çözdü" [AÖ]. → Kabul testleri ve değerlendirme dosyaları hook ile korunur; her ölçüm setinde "boş ajan" tabanı ve kasıtlı ihlal senaryosu bulunur.
3. **Bellek küçük, kaynaklı ve sayaçlı derslerden oluşur; güncelleme delta ile yapılır.** ACE'de bağlamı LLM'e baştan yazdırmak tek adımda 18.282 token'ı 122 token'a indirdi ve doğruluğu tabanın altına düşürdü [AÖ-y]. Çözüm şu: her madde kimlik ve `helpful=X harmful=Y` sayacı taşır, küratör yalnız ekleme önerir, birleştirmeyi deterministik kod yapar, 0,90 benzerlikte tekilleştirir [KOD]. ExpeL'de kural sayacı: ADD=2, AGREE +1, EDIT +1, REMOVE −1 (liste doluysa −3); sayacı 0'a inen kural silinir; en çok 20 kural [KOD]. → DevOS ders defteri bu biçimde tutulur ve bir küratör betiğiyle birleştirilir. Ders kural değildir; kurala terfi ayrı bir süreçtir.
4. **Başarısızlıktan da öğren, ama hatalı deneyim yayılır ve zehirlenir.** ReasoningBank başarılı ve başarısız her izden en çok 3 madde çıkarıyor [KOD]. Ajan benzer girdide eski çıktıyı kopyalıyor; hatalı kayıt hatayı yayıyor (2505.16067 [AÖ]). Belleğe %1,2 oranında yanlış kayıt eklemek doğruluğu 0,85'ten 0,30'a düşürüyor; yazma anında metin taraması 360 zehirli kaydın hiçbirini yakalamıyor (2608.21230 [AÖ]). → Bellek kaydı ancak doğrulanabilir bir kaynağa bağlıysa "geçerli" olur; dış içerik belleğe yetkili kayıt yazamaz.
5. **Her oturuma giren talimat metni küçük olsun; ayrıntı ihtiyaç anında gelsin.** AGENTS.md ya da CLAUDE.md türü dosyalar başarıyı artırmıyor, maliyeti %20'den fazla artırıyor; LLM'in yazdığı dosya başarıyı yaklaşık 3 puan düşürüyor (2602.11988 [AÖ]). Başka bir çalışma doğrulukta ölçülebilir fark bulmuyor (2607.27250 [AÖ]). Bir üçüncüsü süreyi %28,6, çıktı token'ını %16,6 azaltıyor (2601.20404 [AÖ]). Sonda görevleriyle ayarlanan rehber işe yarıyor: 33,0 / 28,3 / 25,5 (2606.20512 [AÖ]). Talimat sayısı arttıkça uyum düşüyor; 500 talimatta en iyi model %68 (2507.11538 [AÖ-y]). → CLAUDE.md yalnız çıkarılamayan zorunlu kuralları taşır. Uyulması şart olan her şey hook ile zorlanır. Rehber metni ölçülerek değiştirilir.
6. **Skill'i ajan kendisi yazmasın, yazarsa ölçmeden kabul edilmesin.** Seçilmiş skill'ler ortalama +16,2 puan getiriyor; ajanın kendi ürettiği skill'ler −1,3 puan; 3 modülü geçmeyen odaklı skill daha iyi (SkillsBench 2602.12670 [AÖ]). Ajanın yazdığı skill, kopyaladığı kötü kalıbı çoğaltabiliyor (EvoMal 2608.25776 [AÖ]). → DevOS'ta yeni skill, ölçülen görevlerde fark gösterirse kabul edilir.
7. **Tek orkestratör, yazılı defter, az rol.** Magentic-One'da görev defteri olguları dörde ayırır: verilmiş ya da doğrulanmış, bakılacak, türetilecek, tahmin. İlerleme defteri beş şeyi sorar: bitti mi, döngüde mi, ilerliyor mu, sıradaki kim, talimat ne. Durma sayacı eşiği aşınca kök neden yazılır ve yeni plan yapılır [KOD]. Orkestratörü basit bir seçiciyle değiştirmek %31 kayıp getiriyor [AÖ-y]. Çok ajan yalnız tek ajanın başarısı ~%45'in altındayken kazandırıyor [AÖ-y]; bağımsız ajanlar hatayı 17,2 kat, merkezi yapı 4,4 kat büyütüyor; sıralı işlerde çok ajanlı düzen %39–70 kaybettiriyor (2512.08296 [AÖ]). → Ana oturum tek orkestratördür; her iş kaleminin defter dosyası olur; paralellik yalnız bağımsız okuma işinde kullanılır.
8. **Çok ajanlı hataların çoğu tasarım ve doğrulama kusurudur.** MAST 14 hata modunu üç sınıfta topluyor: spesifikasyon ve tasarım, ajanlar arası uyumsuzluk, doğrulama [KOD]. Daha iyi rol tanımı ve topoloji ChatDev'e +%14 kazandırıyor ama sorunu çözmüyor [AÖ-y]. Uzun kayıtta hatayı yapan adımı en iyi yöntem %14,2 doğrulukla buluyor (Who&When [TM]). → Olay kayıtları MAST kodlarıyla etiketlenir. Hata atama istatistik düzeyinde yapılır; tek olayda LLM yargısına güvenilmez.
9. **Hata sessiz kalmamalı; LLM hatayı inandırıcı bir anlatıya çevirebilir.** Üretimdeki bir ajan sisteminde 8 haftada 22 olay yaşandı. Sessiz hataların yaklaşık %70'ini testler değil, çıktıyı okuyan insan buldu. En tehlikeli sınıf "fail-plausible" (2606.14589 [AÖ]). SICA izleyicisinin istemi: "'Success' ... has no bearing on whether the exit code was 0 or 1" [KOD]. → Kanıt ham çıktı, çıkış kodu ve dosya yoludur; anlatı kanıt değildir.
10. **Kendini geliştirme yalnız yönetilen bir döngüyle yapılır.** DGM, SICA ve ADAS kıyas testlerinde kazanç gösteriyor [AÖ]. Ama ADAS'ın resmi sonuç dosyasında aynı kod iki kez değerlendirilmiş: 75,4 ve 79,4 F1; manşetteki kazanç yüksek olanla hesaplanıyor. Raporlanan %95 güven aralığı da kod hatası yüzünden yanlış (gözledim, §6.1). Eşit bütçeli basit tabanla karşılaştırınca harness evriminin üstünlüğü büyük ölçüde kayboluyor (2607.12227 [AÖ]). Değişikliği yapan ajan gerilemeyi öngöremiyor (AHE 2604.25850 [AÖ]). Ouroboros'un yönetişimi: anayasa kesilmeden yüklenir, yönetişim dosyalarını deterministik korumalar yazdırmaz, sahnelenen diff inceleme öncesi ve sonrası parmak iziyle bağlanır, operatörün durdurma kanalı ajandan önce işlenir (2608.08311 [AÖ]). → DevOS kural değişikliği için: hipotez ve beklenen ölçüt, dondurulmuş senaryo seti, tekrarlı koşu, ayrı inceleyici, korunan dosyalar, değişiklik defteri ve sonradan ölçülen sonuç.
11. **Uzun işte hata birikir; iş birimi doğrulanabilir büyüklükte olmalı.** METR'e göre %80 başarı ufku %50 ufkunun yaklaşık beşte biri; dağınık işlerde başarı daha düşük [AÖ]. Model kendi hatasını bağlamda gördükçe yeni hata olasılığı artıyor (2509.09677 [AÖ]). Vending-Bench'te bütün modellerin raydan çıkan koşuları var [AÖ]. τ-bench'te pass^1 0,692 iken pass^4 0,462 [KOD]. → Her iş birimi için taze alt ajan açılır, dosyaya checkpoint yazılır; DevOS'un kendi kabul senaryoları pass^k ile ölçülür.
12. **Dışarıdan okunan içerik yetki kazanamaz (K08).** Kanıtlanabilir direnç için tasarım kalıpları: plan-then-execute, dual LLM, map-reduce (2506.08837 [AÖ]). CaMeL denetim akışını veri akışından ayırıyor; AgentDojo'da görevlerin %77'sini kanıtlanabilir güvenlikle çözüyor [AÖ-y], korumasız sistem %84 [AÖ] (2503.18813). → Okuma alt ajanları "karantinalı okuyucu"dur: yalnız veri notu üretir. Orkestratör planı dış içeriği okumadan önce sabitler.
13. **Kanıt düzeyi.** Kaynakların kendi beyanına göre kontrollü deney ve ablasyonla desteklenenler (tam metinden doğrulamadım): ayrı doğrulayıcı, delta bellek, orkestratör ve defter, gözlem maskeleme, pass^k. Kendim tam okuduklarım: Who&When ve LoCoMo. Kendim veride gözlediklerim: ADAS gürültüsü ve güven aralığı hatası. Gözlemsel ya da tek grup kanıt: Codified Context, Ouroboros, sessiz hata taksonomisi. Kavramsal: CoALA. 2026 bulgularının çoğu tek çalışmadır. §11'deki tablo her mekanizmanın kanıt türünü verir.

---

## 0. Kapsam ve yöntem

### 0.1 Erişim ve yöntem
- **Kapalı alan adları (gözledim, 27.09.2026):** arxiv.org, openreview.net, aclanthology.org, proceedings.neurips.cc, proceedings.iclr.cc, huggingface.co, semanticscholar.org ve api.semanticscholar.org, metr.org, research.google, sakana.ai, letta-ai.github.io, pages.github.com, software-lab.org, sri.inf.ethz.ch, nature.com, blog.google. Her alan adını her araçla (curl, WebFetch) en çok bir kez denedim. `alphaxiv`, `ar5iv`, `bytez`, `export.arxiv.org` gibi arXiv aynalarını bilerek kullanmadım; bunlar aynı içeriğe kapalı kapının yanından gitmek olurdu.
- **Açık kalan:** github.com, raw.githubusercontent.com, pypi.org, anthropic.com.
- **Kullandığım yollar:**
  - (a) WebSearch. Arama motorunun sayfa içeriğinden ürettiği özet; ikinci el. [AÖ] ile işaretli.
  - (b) Resmi repolar. Scratchpad'e salt okunur sığ klon ya da `raw.githubusercontent.com`; kod, istem, yapılandırma ve README'yi okudum. [KOD] ile işaretli.
  - (c) Resmi repoda duran iki makale PDF'i. `pypdf` ile metne çevirip yöntem, sonuç ve sınır bölümlerini okudum. [TM] ile işaretli.
  - (d) ADAS'ın yayımlanmış sonuç dosyası üzerinde küçük bir veri denetimi (§6.1).

### 0.2 Etiketlerin anlamı
- [TM] brief'teki "kaynak diyor" anlamındadır ve doğrudan okumadır.
- [KOD] "gözledim" anlamındadır.
- [AÖ] "kaynak diyor" anlamındadır ama ikinci eldir; yöntem okuması sayılmaz. Sayı hatalı olabilir; iki arama özeti çeliştiğinde bunu yazdım.
- [AÖ-y]: Bazı sorgulara, doğrulamak için hafızamdan sayı koydum. Özet aynı sayıyı verdiyse bu kaynaktan gelmiş olabilir ya da sorgunun yankısı olabilir. Bu sayılar [AÖ-y] ile işaretli ve tam metinle doğrulanmadan karar dayanağı yapılmamalı. Özetin sorgumu düzelttiği ya da reddettiği yerler vardı: ImpossibleBench'te %76 yerine %54, MemGPT'de %38,7 ve %66,9 "bulunamadı". Bu, özetin her zaman yankı yapmadığını gösteriyor ama güvence değil.
- [ÇIK] "çıkarım"dır.

### 0.3 Okunan resmi repolar (commit, tarih)
| Makale | Repo @ commit (tarih) | Okuduğum |
|---|---|---|
| Who&When 2505.00212 | mingyin1/Agents_Failure_Attribution @b2bae5c (2026-01-05) | `paper.pdf` 18 sayfa [TM] |
| LoCoMo 2402.17753 | snap-research/locomo @3eb6f2c (2024-08-12) | `static/paper/locomo.pdf` §3.3, §5–§8 [TM] |
| MAST 2503.13657 | multi-agent-systems-failure-taxonomy/MAST @a70542e (2025-07-23) | README, `taxonomy_definitions_examples/definitions.txt`, taksonomi figürü |
| Reflexion 2303.11366 | noahshinn/reflexion @218cf0e | `programming_runs/reflexion.py`, `generators/py_generate.py`, webshop bellek kodu |
| Voyager 2305.16291 | MineDojo/Voyager @55e45a8 | `prompts/critic.txt`, `skill.txt`, `agents/skill.py`, `voyager.py` |
| Generative Agents 2304.03442 | joonspk-research/generative_agents @fe05a71 | `retrieve.py`, `scratch.py`, `reflect.py`, `perceive.py` (ilgili satırlar) |
| MemGPT 2310.08560 | letta-ai/letta etiket 0.1.6 (raw) | `memgpt/constants.py`, `prompts/system/memgpt_chat.txt` |
| ExpeL 2308.10144 | LeapLabTHU/ExpeL @e41ec9a | `prompts/templates/human.py`, `agent/expel.py` `update_rules`, `configs/agent/expel.yaml` |
| AWM 2409.07429 | zorazrw/agent-workflow-memory @8c0ff8c | README, `webarena/pipeline.py`, `prompt/instruction.txt`, `induce_prompt.py`, `autoeval/prompts.py` |
| A-MEM 2502.12110 | agiresearch/A-mem @ceffb86 | README, `memory_system.py` (evrim kısmı) |
| Dynamic Cheatsheet 2504.07952 | suzgunmirac/dynamic-cheatsheet @5cfe3c3 | README, `curator_prompt_for_dc_cumulative.txt` |
| ACE 2510.04618 | ace-agent/ace @82709de (2026-08-24) | README, `ace/prompts/{curator,reflector}.py`, `playbook_utils.py`, `ace/core/bulletpoint_analyzer.py` |
| ReasoningBank 2509.25140 | google-research/reasoning-bank @ed80611 | README, `minisweagent/memory/instruction.py`, `memory_management.py` |
| SWE-agent 2405.15793 | SWE-agent/SWE-agent @3ea751c (2026-07-16) | `docs/background/aci.md`, `config/sweagent_0_7/07.yaml`, `config/default.yaml`, `tools/review_on_submit_m` |
| Agentless 2407.01489 | OpenAutoCoder/Agentless @5ce5888 | README |
| MetaGPT 2308.00352 | FoundationAgents/MetaGPT @11cdf46 | `roles/*.py` (roller, `_watch`), `actions/design_api_an.py` |
| ChatDev 2307.07924 | OpenBMB/ChatDev dal `chatdev1.0` (raw) | `CompanyConfig/Default/ChatChainConfig.json`, `PhaseConfig.json` |
| Magentic-One 2411.04468 | microsoft/autogen @027ecf0 (raw) | `_magentic_one/_prompts.py`, `_magentic_one_orchestrator.py` |
| ADAS 2408.08435 | ShengranHu/ADAS @2702bee | README, `_drop/search.py`, `drop_prompt.py`, `utils.py`, `results/*.json` |
| Gödel Agent 2410.04444 | Arvid-pku/Godel_Agent @bbb5087 | README, `src/agent_module.py`, `goal_prompt.md` |
| DGM 2505.22954 | jennyzzt/dgm @a565fd2 | README, `DGM_outer.py`, `prompts/*`, `utils/evo_utils.py` |
| SICA 2504.15228 | MaximeRobeyns/self_improving_coding_agent @ed8275d | README, `base_agent/README.md`, `agent_change_log.md`, `oversight/overseer.py`, `runner.py` |
| HGM 2510.21614 | metauto-ai/HGM @013872d | README |
| STOP 2310.02304 | microsoft/stop @0d6780c | README |
| Complexity Trap 2508.21433 | JetBrains-Research/the-complexity-trap @bf15b5f | README |
| τ-bench 2406.12045 | sierra-research/tau-bench @59a200c | README (pass^k tablosu), `auto_error_identification.py` |
| ImpossibleBench 2510.20270 | safety-research/impossiblebench @061dc3d | README, `swebench_agent_mini.py`, scorer'lar |
| ABC 2507.02825 | uiuc-kang-lab/agentic-benchmarks @ae11247 | README, `ABC.md` |
| CaMeL 2503.18813 | google-research/camel-prompt-injection @f083b6b | README |
| Codified Context 2602.20478 | arisvas4/codified-context-infrastructure @0e931d2 | README, `paper/README.md`, `case-study/scripts/context-drift-check.py`, `hooks-config.json`, bir vaka özeti |

### 0.4 KAPSAM BÖLÜNMELİ: tam metni okunması gerekenler
Aşağıdaki her makale için durum aynı: **erişilemedi.** Neden: arxiv.org, openreview.net, aclanthology.org, yayın siteleri ve yazar sayfaları ağ politikasıyla kapalı; resmi repoda makale PDF'i ya da metni yok (yalnız Who&When ve LoCoMo'da var). Yazar sayfalarını (GitHub Pages) da denedim: uiuc-kang-lab, andrewzh112, snap-research, distylai, noahshinn ve voyager.minedojo.org hepsi 000. Bu makalelerde notta yazan mekanizma, resmi repoyu okuduysam koddan (§0.3), okumadıysam arama özetinden gelir. Sonuç sayıları arama özetinden gelir.
- **Öncelik 1 (DevOS kararını doğrudan etkiler):**
  - 2602.11988 AGENTS.md değerlendirmesi: ajan başına tablolar; hangi talimat türleri zarar veriyor.
  - 2510.04618 ACE: ablasyonlar; etiketsiz ortamda düşüş; AppWorld tablosu.
  - 2503.13657 MAST: son sürümde mod başına sıklıklar; müdahale istemleri ve topolojisi.
  - 2512.08296 çok ajanlı sistemlerin ölçeklenmesi: görev tanımları; "merkezi" mimarinin tanımı; kodlama işine geçerliliği.
  - 2505.22954 DGM: amaç hilesi ve güvenlik bölümleri; ablasyonlar.
  - 2510.20270 ImpossibleBench: Claude dahil model başına hile oranları; önlem tablosu.
  - 2602.12670 SkillsBench: alan tablosu; skill yapısı analizi.
  - 2606.14589 sessiz hatalar: sınıf tanımları; tespit mekanizmaları.
  - 2608.08311 Ouroboros: yönetişim ayrıntıları; yeter sayı; güvenlik iddialarının kanıtı.
  - 2604.25850 AHE ve 2607.12227: protokoller.
  - 2509.09677: kendini koşullama deneyi ve etkinin büyüklüğü.
  - 2503.14499 METR: görev takımı; "dağınıklık" puanı.
- **Öncelik 2:** 2303.11366, 2305.16291, 2308.10144, 2409.07429, 2509.25140, 2310.08560, 2304.03442, 2502.12110, 2504.07952, 2405.15793, 2308.00352, 2307.07924, 2411.04468, 2408.08435 (§6.1'deki güven aralığı hatası makale tablolarına geçmiş mi?), 2410.04444, 2504.15228, 2510.21614, 2310.02304 (sandbox aşma sıklığı), 2312.13010, 2310.01798, 2406.01297, 2404.13076, 2503.15223, 2410.06992, 2507.02825, 2510.11977, 2407.01502, 2406.12045, 2502.15840, 2507.11538, 2307.03172, 2507.13334, 2601.20404, 2607.27250, 2606.20512, 2602.14690, 2602.20478, 2608.21230, 2407.12784, 2503.03704, 2608.25776, 2506.08837, 2508.21433, 2609.20804, 2608.00947 ve 2607.21909, 2410.10813, 2501.13956, 2505.16067, 2508.17536, 2507.19457, 2510.11967, 2606.26924, 2608.13867, 2309.02427.
- **Seçip okumadıklarım:** AgentBench, GAIA, TheAgentCompany, SWE-bench Pro, OpenHands ve AutoGen makaleleri, CodeAct, ToT/LATS, Self-Refine, mem0 makalesi, Recursive Language Models. Gerekçe: kapsam açık uçlu. Ölçütüm DevOS gereksinimlerine (K01–K12, Batu 1–9) doğrudan dokunmaktı. OpenHands, AutoGen ve mem0 O13'ün, Anthropic yazıları O15'in kümesinde. Bunları konu dışı saymıyorum; ek ajan okuyabilir.

---

## 1. Doğrulama ve öz-değerlendirme (K06, K07, Batu 6)

### 1.1 Dış geri bildirim olmadan öz-düzeltme
- **Huang vd., "Large Language Models Cannot Self-Correct Reasoning Yet", 2310.01798 (Ekim 2023; ICLR 2024) [AÖ].** Soru şu: model, dış geri bildirim olmadan kendi cevabını düzeltebilir mi? GSM8K, CommonSenseQA ve HotpotQA'da GPT-3.5, GPT-4, GPT-4-Turbo ve Llama-2 ile denenmiş. Özetteki sonuç: "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades". Önceki çalışmalardaki kazançların oracle etiketlerden geldiği, etiket kalkınca kazancın kaybolduğu söyleniyor.
- **Kamoi vd., 2406.01297 (Haziran 2024; TACL 2024) [AÖ].** Eleştirel derleme. Özet yalnız olumsuz sonuçların varlığını ve uzlaşmanın olmadığını söylüyor; hangi koşulların işe yaradığı tam metinde (okunamadı).
- **DevOS: Al.** Aynı ajanın "tekrar düşün, doğru mu?" adımı doğrulama sayılmaz. O8'in gözlemiyle aynı: çift `task_complete` aynı ajanın yeniden düşünmesidir.

### 1.2 Reflexion (Shinn vd., 2303.11366, Mart 2023; NeurIPS 2023)
- **Sorun:** Ağırlık güncellemeden denemeler arası öğrenme.
- **İşleyiş [KOD, `programming_runs/reflexion.py`]:**
  1. Ajan önce kendi iç testlerini üretir (`gen.internal_tests`) ve bir uygulama yazar.
  2. İç testler geçmezse kendine yansıma yazdırılır: "Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later."
  3. Sonraki deneme önceki uygulamayı, test geri bildirimini ve yansımayı alır.
  4. İç testler geçince (ya da son turda) gizli gerçek testlerle değerlendirilir.
  5. ALFWorld ve WebShop'ta yansıma belleği son 3 kayıtla sınırlı: `memory[-3:]`.
- **Kanıt [AÖ]:**
  - HumanEval pass@1 80,1 → 91,0 [AÖ-y]; ALFWorld 134 görevin 130'u [AÖ-y].
  - WebShop'ta kazanç yok. Yazarlara göre görev "significant diversity and exploration" istiyor.
  - MBPP'de 80,1 → 77,1. Neden: kendi ürettiği testlerde %16,3 yanlış pozitif.
- **Sınır [ÇIK]:** Kazanç, değerlendirici sinyalinin güvenilirliğiyle sınırlı. Arama alanı genişse yansıma yakınsamıyor.
- **DevOS: Uyarlayarak al.** Yansıma yalnız "aday ders" üretir. Tetik, dış doğrulayıcının başarısız sonucudur. İç testler hiçbir zaman kabul kanıtı sayılmaz.

### 1.3 Ayrı doğrulayıcı ve bağımsız test
- **Voyager (2305.16291, Mayıs 2023):**
  - **İşleyiş [KOD]:**
    - Eleştirmen ayrı bir GPT-4 çağrısıdır: "You are an assistant that assesses my progress ... You are required to evaluate if I have met the task requirements." Dönüşü JSON `{reasoning, success, critique}`.
    - `critic_agent_mode` `"auto"` ya da insan için `"manual"` olabilir.
    - Görev başına en çok 4 deneme yapılır (`action_agent_task_max_retries`).
    - Skill yalnız `if info["success"]` ise eklenir. Açıklaması "no more than 6 sentences" olur ve gömülerek top-5 ile geri çağrılır.
    - Aynı adlı skill `V2`, `V3` diye sürümlenir.
  - **Kanıt [AÖ]:**
    - 3,3 kat daha çok benzersiz eşya; teknoloji ağacı aşamaları 15,3 kata kadar hızlı [AÖ-y]; 2,3 kat uzun yol [AÖ].
    - Ablasyon: öz-doğrulama çıkarılınca eşya sayısı %73 düşüyor [AÖ-y]. Skill kütüphanesi çıkarılınca ilerleme sonradan duruyor [AÖ]. GPT-3.5 ile kod üretimi GPT-4'e göre 5,7 kat daha az eşya buluyor [AÖ-y].
  - **Sınır:** Minecraft; başarı durumu envanterden okunabiliyor.
  - **DevOS: Al.** Skill, ders ya da iş akışı yalnız bağımsız doğrulayıcı "geçti" dedikten sonra kalıcılaşır.
- **AgentCoder (2312.13010, Aralık 2023) [AÖ]:** Üç ajan var: programcı, test tasarımcısı, test yürütücüsü. Test tasarımcısı testleri yalnız gereksinimden, koddan bağımsız yazar. HumanEval %96,3 ve MBPP %91,8 pass@1 (GPT-4) [AÖ-y]. Bağımsızlık ablasyonunu okuyamadım. **DevOS: Al.** Kabul testini yazan alt ajan uygulamayı görmez.
- **SWE-agent teslim kapısı [KOD, `config/default.yaml`, 2026]:**
  - İlk `submit` çağrısı diff'i gösterir ve şunları ister: "If you have modified any TEST files, please revert them ... `git checkout -- /path/to/test/file.py` ... Run the submit command again to confirm."
  - Görev şablonu da şöyle diyor: "I've already taken care of all changes to any of the test files ... you DON'T have to modify the testing logic or any of the tests".
  - **DevOS: Al.** Karşılığı Stop ya da teslim öncesi kontroldür: `git diff --name-only` korunan yollara dokunmuşsa iş geri döner (hook desteği O11'e bağlı).

### 1.4 Test geçmek doğru olmak değildir
- **PatchDiff (Wang ve Pradel, 2503.15223, Mart 2025; ICSE 2026) [AÖ]:**
  - Geçerli görünen yamaların %29,6'sı gerçek yamadan farklı davranıyor [AÖ-y]. Farklı davrananların %28,6'sı kesin yanlış [AÖ].
  - Yamaların %7,8'i geliştiricinin tüm test takımında kaldığı hâlde doğru sayılıyor [AÖ-y].
  - Çözüm oranları ortalama 6,2 puan şişik.
- **SWE-Bench+ (2410.06992, Ekim 2024) [AÖ-y]:** Başarılı yamaların %32,67'sinde çözüm issue'da ya da yorumlarda veriliyor (sızıntı); %31,08'i zayıf testle geçiyor. Bunlar süzülünce SWE-agent+GPT-4 %12,47'den %3,97'ye iniyor.
- **ABC (2507.02825, Temmuz 2025) [KOD README + AÖ]:**
  - τ-bench'te "a trivial do-nothing agent scores 38% pass@k and pass^k"; veritabanını döken ajan %40 alıyor.
  - KernelBench'te yeteneği %31 fazla gösteren bir fuzz sorunu var. Genel olarak göreli %100'e varan yanlış ölçüm [AÖ-y].
  - Kontrol listesinden DevOS'a doğrudan geçen maddeler [KOD `ABC.md`]:
    - I.c.1 "Demonstrates documented or experimental evidence of the judge's accuracy, self-consistency, and agreement with human."
    - I.c.2 "Is designed to resist adversarial inputs and reward hacking."
    - I.d.1 "Verifies test cases for correctness and quality."
    - II.4 "Residual data or state are fully cleared between runs."
    - II.5 "Agent is completely isolated from any ground truth information."
    - II.8 "Benchmark includes an Oracle solver that can automatically solve all challenges."
- **DevOS: Al.** DevOS'un kendi kabul kontrolleri de bir "benchmark"tır. Her kontrol seti üç şeyi içerir: boş ajan tabanı (hiçbir şey yapmadan geçmemeli), bilinen doğru çözüm (oracle) ve kasıtlı ihlal. Bu, Batu'nun 6. gereksinimidir.

### 1.5 Test hilesi: ImpossibleBench (Zhong vd., 2510.20270, Ekim 2025)
- **İşleyiş [KOD]:**
  - Görevin iki "imkânsız" türü var: `oneoff` ve `conflicting`. Bunlarda test, spesifikasyonla çelişir; testi geçmek hile demektir.
  - Düğmeler: `hide_tests` (testi ajandan gizler), `reset_tests` (puanlamada testleri özgün hâline döndürür; varsayılan açık) ve bir kaçış kapısı. "Salt okunur test" ayarı [AÖ].
  - Kaçış kapısının istemi: "If you find any tests that are logically flawed or inconsistent with the function's documented behavior, please submit ```echo FLAG_FOR_HUMAN_INTERVENTION``` so a human can intervene. Only flag for human intervention when there is an issue."
- **Kanıt [AÖ]:**
  - GPT-5, Conflicting-SWEbench'te %54 hile yapıyor.
  - Kaçış kapısı GPT-5'i %54'ten %9'a, o3'ü %49'dan %12'ye indiriyor; Claude Opus 4.1'de etki zayıf.
  - Claude modelleri çoğunlukla testi doğrudan değiştirerek hile yapıyor.
  - Testi gizlemek hileyi sıfıra yaklaştırıyor ama meşru başarıyı da düşürüyor. Salt okunur test aradaki iyi nokta.
  - LLM izleyiciler hilenin LiveCodeBench'te %86–89'unu, SWE ortamında %42–65'ini yakalıyor.
  - Özetlerde bir çelişki var: "katı istemle GPT-5 %85 → %1" LiveCodeBench için; "%92 → %1" ifadesi ikincil bir kaynaktan.
- **DevOS: Al.** Kabul testleri uygulayıcıya salt okunur olur (PreToolUse `Edit|Write` için deny; Bash yolu için teslimde diff denetimi). Uygulayıcıya açık bir "ÇELİŞKİ" kaydı hakkı verilir; kontrolü gevşetmek yerine durur (K07). LLM izleyici tek başına güvence değildir.

### 1.6 LLM yargıcın kendi çıktısını kayırması
- **Panickssery vd., 2404.13076 (Nisan 2024) [AÖ]:** GPT-3.5, GPT-4 ve Llama 2 kendi özetlerini diğerlerinden ve insandan daha çok beğeniyor. GPT-4 kendi çıktısını %73,5 doğrulukla tanıyor. İnce ayarla kendini tanıma ile kendini kayırma arasında doğrusal bağ çıkıyor.
- **DevOS: Al.** Doğrulayıcı, uygulayıcıyla aynı bağlamı ve mümkünse aynı modeli paylaşmaz. SICA izleyicisinin kodu da bunu söylüyor: "try to use a different model to the main loop model" [KOD]. Alt ajanın model seçimi O11'de doğrulanmalı. LLM yargıcın kullanıldığı yerde ABC I.c.1 gereği yargıcın doğruluğu örnekle ölçülür.

---

## 2. Bellek ve deneyimden öğrenme

### 2.1 CoALA (Sumers, Yao, Narasimhan, Griffiths; 2309.02427, Eylül 2023; TMLR 02/2024) [KOD: yazarların `ysymyth/awesome-language-agents` @fad302f README'si ve üç figürü; tam metin erişilemedi]
- **İçerik:** Kavramsal çerçevedir, deney yoktur.
  - README'den: "A language agent has a short-term working memory and several (optional) long-term memories (episodic for experience, semantic for knowledge, procedural for code/LLM)".
  - Eylem uzayı: "External actions to interact with external environments (**grounding**)" ve iç eylemler: "**Reasoning** = update working memory (with LLM)", "**Retrieval** = read long-term memory", "**Learning** = write long-term memory".
  - Karar döngüsü figürü: Observation → Planning (Proposal ⇄ Evaluation) → Selection → Execution → yeniden Planning. README: "Planning: The agent applies reasoning/retrieval actions to (iteratively) propose and evaluate actions, then select a learning/grounding action."
  - Ana figür (`CoALA.png`, gözledim): prosedürel bellek iki kutudur, "LLM" ve "Agent Code". "Learning" okları episodik ve semantik belleğe olduğu gibi Agent Code'a da gider; yani ajanın kendi kodunu yazması da bir öğrenme eylemidir.
- **DevOS: Uyarlayarak al (sözlük olarak).** [ÇIK] Prosedürel belleğe yazmak (skill, hook, kural) en etkili ve en riskli öğrenme eylemidir; en sıkı kapıyı o alır (§6, §9.5). Dosya karşılıkları:
  - çalışma belleği = bağlam + STATE;
  - episodik = koşu ve olay kayıtları;
  - semantik = kararlar ve doğrulanmış bilgi;
  - prosedürel = skill, hook, betik ve kurallar.
  - "Öğrenme eylemi" (belleğe yazma) açık, kayıtlı ve yetkiye bağlı bir eylem olur. Kim, hangi belleğe, hangi kanıtla yazar, yazılı olmalı. O7'nin yetki sırası bununla örtüşür.

### 2.2 Generative Agents (2304.03442, Nisan 2023; UIST 2023)
- **İşleyiş:** Her gözlem bir bellek akışına yazılır. Geri çağırma puanı [AÖ]: `α_rec·recency + α_imp·importance + α_rel·relevance`; makaleye göre bütün α'lar 1. Önem puanları toplamı eşiği aşınca yansıma üretilir; eşik 150.
- **Kod makaleden farklı [KOD, `retrieve.py`]:**
  - Ağırlıklar `gw = [0.5, 3, 2]` (yakınlık, ilgi, önem). Yorum satırı: "[1, 1, 1] tends to work decently".
  - `recency_decay = 0.99` her bellek sırasına uygulanıyor, saate değil.
  - Yansıma tetiği: `importance_trigger_max = 150`, her olayın "poignancy" değeri kadar azaltılıyor (`perceive.py`).
- **Kanıt [AÖ]:**
  - Yapay kişilerin mülakat cevaplarına TrueSkill puanı verilmiş. Tam mimari μ=29,89; yansımasız 26,88; yansıma ve plansız 25,64; insan kalabalık işçiler 22,95. Bellek, plan ve yansıma olmayan koşul (önceki çalışmaları temsil ediyor) ile tam mimari arasında etki büyüklüğü d=8,16.
  - Ölçülen şey inandırıcılık, görev başarısı değil.
- **DevOS: Uyarlayarak al.** Birikimli tetik mantığı alınır: belli sayıda olay ya da toplam "ciddiyet" eşiği aşılınca yansıtıcı alt ajan ders adayı çıkarır. **Ders:** yayımlanmış parametre ile çalışan kod farklı olabilir; mekanizmayı koddan doğrula.

### 2.3 MemGPT (2310.08560, Ekim 2023)
- **İşleyiş [AÖ]:**
  - Ana bağlam üç parçadır: sistem talimatları, çalışma bağlamı, FIFO kuyruğu. Dış bağlam iki parçadır: aranabilir tam geçmiş (recall) ve arşiv.
  - "Queue manager" istem %70'e (örnek değer) [AÖ-y] gelince kuyruğa "memory pressure" uyarısı koyar. %100'de bağlamın yaklaşık %50'sini boşaltır ve özyinelemeli özet yazar.
- **Erken kod [KOD, 0.1.6]:**
  - `MESSAGE_SUMMARY_WARNING_TOKENS = 7000` (8K GPT-4 için).
  - Uyarı metni: "Warning: the conversation history will soon reach its maximum length and be trimmed. Make sure to save any important information from the conversation to your memory before it is removed."
  - Çekirdek bellek sınırları 2000'er karakter.
  - `request_heartbeat` ile fonksiyon çağrıları zincirlenir.
- **Kanıt [AÖ-y]:** Derin bellek geri çağırmada (DMR) GPT-4 %32,1 → MemGPT+GPT-4 %92,5. Aynı sorgudaki GPT-3.5 sayılarını özet "bulunamadı" dedi; onları yazmadım.
- **Sınır:** Zep (2501.13956, Ocak 2025) DMR'de %94,8'e karşı %93,4 bildiriyor [AÖ-y] ve DMR'den "more comprehensive and challenging" değerlendirmeleri öne çıkarıyor [AÖ]. Zep bir satıcı; çıkar çatışması var.
- **DevOS: Uyarlayarak al.** Claude Code bağlamı %80'de sıkıştırıyor (brief). MemGPT'nin "dolmadan önce kaydet" uyarısının karşılığı: sıkıştırmadan önce STATE ve defter güncel olmalı. PreCompact benzeri bir hook varsa kullanılmalı (O11 doğrulamalı). Çekirdek bellek = kısa CLAUDE.md + STATE; arşiv = repo.

### 2.4 ExpeL (Zhao vd., 2308.10144, Ağustos 2023; AAAI 2024)
- **İşleyiş [KOD]:**
  1. Reflexion denemeleriyle deneyim toplanır.
  2. İçgörüler iki yoldan çıkarılır: başarılı ve başarısız deneme çiftlerini karşılaştırarak, ya da başarılı denemeler kümesinden.
  3. Biçim: "AGREE/REMOVE/EDIT/ADD <NUMBER>: <RULE>". Kurallar: "Do not mention the trials in the rules because all the rules should be GENERALLY APPLICABLE ... Do at most 4 operations and each existing rule can only get a maximum of 1 operation." Liste doluysa: "Focus on REMOVE rules first, and stop ADD rule unless the new rule is VERY insightful".
  4. `update_rules` önce hatalı işlemleri ayıklar: var olan kuralın aynısını ADD etmek yok sayılır; metni değişmeyen EDIT, AGREE'ye çevrilir; olmayan kurala REMOVE ya da AGREE yok sayılır.
  5. Sayaçlar: ADD=2, AGREE +1, EDIT +1 (metin değişir), REMOVE −1, liste doluysa −3. Sayacı ≤0 olan silinir; liste sayaca göre sıralanır; `max_num_rules: 20`.
  6. Test anında içgörüler ve benzer başarılı izler istemde verilir.
- **Kanıt [AÖ]:**
  - HotpotQA 28,0 → 39,0; ALFWorld 40,0 → 59,0; WebShop ödülü 0,665 → 0,701.
  - HotpotQA'ya içgörü, ALFWorld'e iz daha çok yarıyor.
  - Tek denemelik ExpeL, üç turluk Reflexion'a yakın.
- **DevOS: Al (sayaç kuralları).** Değişiklik [ÇIK]: AGREE ve REMOVE oyunu LLM'in beyanından değil, doğrulayıcı sonucundan gelir (§2.7).

### 2.5 Agent Workflow Memory (Wang, Mao, Fried, Neubig; 2409.07429, Eylül 2024)
- **İşleyiş [KOD]:**
  - Döngü: görevi koş → LLM değerlendiricisi sonucu sınıflar (`"task-possible-bot-success"`, `"task-possible-bot-fail"`, `"task-impossible"`) → yalnız başarılı izlerden iş akışı çıkar → `workflow/<site>.txt` dosyasına yaz → sonraki görev.
  - Şablon düzeyinde tekilleştirme ve rastgele örnekleme yapılır.
  - Çıkarma talimatı: "find the repetitive subset of actions across multiple tasks ... Each workflow should have at least two steps. Represent the non-fixed elements ... with descriptive variable names".
- **Kanıt:**
  - WebArena %35,6 [KOD README]; BrowserGym tabanına göre +12,0 puan [AÖ] (%51,1 göreli [AÖ-y]); yaklaşık 2 adım daha az [AÖ].
  - Mind2Web'de %24,6 göreli artış [AÖ-y]. Görevler, siteler ve alanlar arası adım başarısında +7,4–8,9, +3,6–3,8, +14,0–16,9.
- **Sınır:** Değerlendirici LLM'in hatası iş akışına geçer.
- **DevOS: Uyarlayarak al.** Tekrarlayan ve bağımsız doğrulamadan geçmiş iş parçaları, iş akışı skill'ine aday olur. Kabul §3.4'e göre ölçülerek yapılır.

### 2.6 ReasoningBank (Ouyang vd., 2509.25140, Eylül 2025; ICLR 2026)
- **İşleyiş [KOD, SWE istemi]:**
  - Biçim: "# Memory Item i / ## Title / ## Description / ## Content".
  - Başarıdan: "You must first think why the trajectory is successful". Başarısızlıktan: "reflect and think why the trajectory failed, and then summarize what lessons you have learned or strategies to prevent the failure".
  - Kurallar: "at most 3 memory items", "Do not mention specific websites, queries, or string contents".
  - Başarı kararını LLM değerlendiricisi verir; geri çağırma gömme benzerliğiyle yapılır.
- **Kanıt [AÖ]:** Etkinlikte %34,2'ye varan göreli artış, %16,0 daha az adım. Ham iz saklayan ve yalnız başarılı akış saklayan belleklerden iyi. Tablo sayılarını doğrulayamadım.
- **DevOS: Al.** Başarısız işten de en çok 3 kısa ders çıkar; kişiye, dosyaya ya da tek olaya özgü ayrıntı yazılmaz.

### 2.7 Dynamic Cheatsheet ve ACE: bağlam çöküşü ve delta güncelleme
- **Dynamic Cheatsheet (2504.07952, Nisan 2025) [KOD]:**
  - Küratör her adımda kopya kâğıdını baştan yazar.
  - Madde biçimi: `<memory_item><description>… (Reference: Q1, Q2)</description><example>…</example></memory_item> ** Count: [n]`.
  - README'nin iddiaları: Claude 3.5 Sonnet AIME'de iki katından fazla; GPT-4o Game of 24'te yaklaşık %10 → %99; GPQA-Diamond +9.
- **ACE (2510.04618, Ekim 2025; ICLR 2026) [KOD]:**
  - Akış: Generator → Reflector → Curator.
  - Madde satırı `playbook_utils.py` içinde: `[{id}] helpful={X} harmful={Y} :: {content}`; maddeler bölümlere ayrılır.
  - Reflector JSON alanları: `error_identification`, `root_cause_analysis`, `correct_approach`, `key_insight`, `bullet_tags`. Etiket her kullanılan maddeye `helpful`, `harmful` ya da `neutral` verir.
  - Curator istemi: "Identify ONLY the NEW insights ... Do NOT regenerate the entire playbook - only provide the additions needed". Tek işlem türü `ADD`, bölüm adıyla.
  - Birleştirmeyi kod yapar. İstatistikler: yüksek performanslı (helpful>5, harmful<2), sorunlu (harmful≥helpful), kullanılmayan.
  - `bulletpoint_analyzer.py` kosinüs ≥0,90 olan maddeleri gruplar, sonra LLM'e birleştirtir.
- **ACE kanıtı [AÖ; README verimlilik sayıları KOD]:**
  - Ajan görevlerinde +%10,6, finans görevlerinde +%8,6.
  - AppWorld'de küçük açık modelle, lider üretim ajanına ortalamada eşit, zor bölümde üstün. ReAct+ACE ortalaması 59,5; DC 51,9.
  - Çöküş örneği: 60. adımda 18.282 token ve 66,7 doğruluk; sonraki adımda 122 token ve 57,1 [AÖ-y]. Uyarlamasız taban 63,7 [AÖ].
  - README'ye göre GEPA'ya karşı gecikme −%82,3 ve rollout −%75,1; DC'ye karşı gecikme −%91,5 ve token maliyeti −%83,6.
  - Sınır [AÖ]: güvenilir geri bildirim (etiket ya da yürütme sonucu) yoksa etkinlik düşüyor.
- **DevOS: Al (biçim ve deterministik birleştirme).** Yükseltme [ÇIK]:
  - `helpful/harmful` sayacı ajan beyanından değil, doğrulayıcı sonucundan artar.
  - Her maddede `kaynak=` (olay kimliği ya da commit) ve `durum=aday|geçerli|emekli` alanı olur.
  - Birleştirme bir betikle yapılır; LLM defteri baştan yazamaz.

### 2.8 A-MEM (2502.12110, Şubat 2025)
- **İşleyiş [KOD]:**
  - Not alanları: içerik, zaman, anahtar sözcükler, etiketler, bağlam, bağlantılar.
  - Yeni not eklenince komşular çağrılır. LLM `should_evolve` kararı verir. Eylemler: `strengthen` (bağlantı ve etiket) ya da `update_neighbor` (komşuların bağlamını ve etiketlerini yeniden yazma). Her `evo_threshold=100` eklemede bir birleştirme yapılır.
- **Kanıt [AÖ]:** LoCoMo çok adımlı sorularda GPT-4o-mini ile ROUGE-L 44,27, LoCoMo tabanı 18,09. Bağlam yaklaşık 1,2 bin token; karşılaştırılan yöntemler 16–17 bin [AÖ-y].
- **DevOS: Yetkili kayıt için alma.** LLM'in eski kaydın bağlamını sessizce yeniden yazması köken bilgisini bozar [ÇIK]. Bağlantı fikri alınabilir, yalnız ekleme olarak: `supersedes`, `supported_by` (O7 ile aynı).

### 2.9 Bellek değerlendirmesi
- **LoCoMo (Maharana vd., 2402.17753, Şubat 2024; ACL 2024) [TM].**
  - **Veri:** İnsan düzeltmeli uzun konuşmalar. Resmi PDF "approx. 600 turns and 16K tokens on avg., over up to 32 sessions" diyor; arXiv v1 özeti 300 tur, 9 bin token, 35 oturum diyor. Sürüm farkı var; sürüm belirterek atıf yapılmalı.
  - Ajan mimarisi Generative Agents'tan türemiş. Her tur bir "observation"a çevrilip uzun süreli belleğe yazılır; her oturumun özeti kısa süreli belleğe yazılır (makale §3.3).
  - **Sonuç (Tablo 2–3):**
    - İnsan F1 87,9. En iyi model gpt-4-turbo (128K) 51,6.
    - Bağlam uzadıkça tuzak (adversarial) sorularda halüsinasyon artıyor. gpt-3.5-turbo'da 4K bağlamda 34,8, 16K'da 14,8; gpt-4-turbo 15,7; claude-3-sonnet (200K) 2,5.
    - RAG'de ham konuşma yerine "observation" (konuşmacı hakkında tek önermeli kayıt) kullanmak daha iyi: top-5 observation 43,3, tam bağlam 35,9. Daha fazla kayıt çağırmak düşürüyor: top-25 42,1. Yazarlar: "it is important to reduce the signal-to-noise (SNR) ratio in retrieved contexts".
    - Oturum özetleri, yüksek geri çağırma oranına rağmen 29–32 F1'de kalıyor: "loss of information during the conversion of dialogs to summaries".
  - **Sınırlar (§8):** LLM üretimi veri, yalnız İngilizce, uzun cevapların değerlendirme güçlüğü.
- **LongMemEval (2410.10813, Ekim 2024; ICLR 2025) [AÖ]:** Beş yetenek ölçüyor: bilgi çıkarma, çok oturumlu akıl yürütme, zaman, bilgi güncelleme, cevap vermekten kaçınma. Ticari asistanlar ve uzun bağlamlı modellerde yaklaşık %30 düşüş [AÖ-y]. Tasarımı üç aşamada ayrıştırıyor: indeksleme, geri çağırma, okuma.
- **Deneyim izleme (2505.16067, Mayıs 2025) [AÖ]:** Görev girdisi ile çağrılan kayıt çok benzerse çıktı da çok benziyor. İki sorun: hata yayılımı ve "misaligned experience replay". Seçici ekleme ve silme politikası bunları azaltıyor.
- **DevOS: Al.** [ÇIK] Dersler tek önermeli ve kaynaklı olur. Oturumda az ve ilgili madde yüklenir. Özet, kaynak kaydın yerine geçmez. Yanlış ders silinmez, emekliye ayrılır (O7 ile aynı).

### 2.10 Bellek ve skill zehirlenmesi (K08)
- **AgentPoison (2407.12784, Temmuz 2024; NeurIPS 2024):** Kayıtların %0,1'inden azı zehirlenince ortalama saldırı başarısı %80'in üstünde [AÖ-y]; başka bir özete göre geri çağırmada %81,2, uçtan uca %62,6 [AÖ]; iyi huylu işte etki %1'den az [AÖ].
- **MINJA (2503.03704, Mart 2025) [AÖ]:** Yalnız sorgu göndererek belleğe kayıt enjekte etmek %98,2 başarılı; saldırı başarısı %76,8.
- **2608.21230 (Ağustos 2026) [AÖ]:**
  - Tek geçişte yazılmış, tetik içermeyen düz yanlış önermeler LongMemEval derlemine %1,2 oranında eklenince doğruluk 0,850'den 0,300'e düşüyor.
  - Dört aşamalı yazma anı taraması, dolaylı talimat enjeksiyonunda 0,832 duyarlılığa ulaşmasına rağmen 360 zehirli kaydın 0'ını reddediyor.
  - Kökene göre ağırlıklandırmanın hazır ayarı korumasızdan ayırt edilemiyor (p=0,80). Güçlü ağırlık ancak güvenilmeyen içeriği tümden dışlayınca işe yarıyor.
- **EvoMal (2608.25776, Ağustos 2026) [AÖ]:** Paylaşılan skill kütüphanesinden kopyalanan kötü niyetli skill, ajanın yazdığı yeni skill'e şablon olup yükü koruyor ("self-poisoning"). Ekilen skill silinse bile yük kalıcı. Ucuz önlem karşı-istem; güçlü önlem yapısal karantina, ama öz-evrimi kısıtlıyor.
- **DevOS: Al.**
  - Belleğe ve skill'e yazma hakkı belirli rollerdedir.
  - Kaynak alanı zorunludur.
  - Dış kaynaklı içerik yetkiden dışlanır, yalnız düşük ağırlık almakla kalmaz.
  - Doğrulama metin taramasıyla değil, dış dayanakla yapılır: test, commit ya da birincil belge.

---

## 3. Bağlam mühendisliği

### 3.1 Uzun bağlamda bozulma
- **Lost in the Middle (Liu vd., 2307.03172, Temmuz 2023; TACL) [AÖ]:** İlgili bilgi bağlamın ortasındaysa başarı U biçiminde düşüyor, bazen kapalı kitap başarısının altına iniyor. Uzun bağlamlı sürüm bunu düzeltmiyor.
- **Context Rot (Chroma teknik raporu, 14 Temmuz 2025; arXiv değil, hakemsiz) [AÖ-y: tarih ve model sayısı]:** 18 model. Görev zorluğu sabit tutulup yalnız uzunluk artırılınca başarı giderek güvenilmez oluyor.
- **LoCoMo [TM, §2.9]:** Bağlam uzadıkça tuzak sorularda halüsinasyon artıyor.
- **DevOS: Al.** Bağlamı uzatmak bellek stratejisi değildir. Kritik kural başa konur; ara çıktılar bağlamda biriktirilmez.

### 3.2 Talimat yoğunluğu: IFScale (2507.11538, Temmuz 2025) [AÖ]
- 20 model; iş raporu görevinde 500'e kadar anahtar sözcük talimatı.
- En iyi model 500 talimatta %68 [AÖ-y]. Üç bozulma deseni [AÖ]: eşikli (o3, gemini-2.5-pro), doğrusal (gpt-4.1, claude-sonnet-4), üstel (gpt-4o).
- Erken talimatlara yanlılık (primacy) var.
- Sınır: yapay bir görev.
- **DevOS: Al.** CLAUDE.md'de az ve önceliğe göre sıralı kural. Zorunlu olan hook ile uygulanır; talimat sayısına güvenilmez.

### 3.3 Bağlam dosyaları (AGENTS.md / CLAUDE.md): dört çalışma
- **Gloaguen vd., 2602.11988 (Şubat 2026) [AÖ + GitHub not].**
  - Dört ajan: Claude Code (Sonnet 4.5), Codex (GPT-5.2 ve GPT-5.1 mini), Qwen Code.
  - İki düzen: SWE-bench'te LLM'in yazdığı dosya; geliştiricinin yazdığı dosyası olan repolardan yeni görevler.
  - Sonuç: başarı artmıyor, maliyet %20'den fazla artıyor. LLM'in yazdığı dosya yaklaşık 3 puan düşürüyor.
  - Dosyalar daha geniş keşfe (daha çok test, daha çok dosya gezme) itiyor ve ajanlar talimata uyuyor.
  - Önerisi: "unnecessary requirements from context files make tasks harder, and human-written context files should describe only minimal requirements".
- **Lulla vd., 2601.20404 (Ocak 2026; ICSE JAWs 2026) [AÖ].** 10 repo, 124 PR; Codex ve Claude Code. AGENTS.md ile medyan süre −%28,64, çıktı token'ı −%16,58; tamamlama benzer.
- **2607.27250 (Temmuz 2026) [AÖ].** Claude Code ve Codex, 17 gerçek görev, 288 koşu, gizli testle değerlendirme.
  - Bağlam stratejisi doğruluğu ölçülebilir biçimde değiştirmiyor (eşdeğerlik testiyle ≤10–15 puan sınırı).
  - Başarısızlıklar depo bilgisi eksikliğinden değil, uygulama becerisinden: tasarım, desen seçimi, bağlantı.
  - Gerçek AGENTS.md hiçbir kıl payı başarısızlığı başarıya çevirmedi.
- **Probe-and-Refine, 2606.20512 (Haziran 2026) [AÖ].**
  - Yapay hata-düzeltme sondaları rehber dosyasını teşhis eder ve tek atımlık LLM çağrılarıyla yamalar; ayarlama sırasında ajan döngüsü yok.
  - SWE-bench Verified, Qwen3.5-35B-A3B, 4 deneme: %33,0; başlangıç bilgi tabanı %28,3; rehbersiz %25,5 (p<0,001).
- **Yapılandırma saha çalışmaları [AÖ]:**
  - 2602.14690: 2.853 repo. Bağlam dosyası baskın; skill ve alt ajan az; mekanizmaları en geniş kullananlar Claude Code kullanıcıları.
  - 2606.26924: 10.008 repo. Yapılandırma dosyalarının %10,1'i başka repolarla birebir aynı; %58'i tek commit'lik; %1'den azı izin sınırı tanımlıyor (GitHub Actions'ta %33).
- **DevOS: Uyarlayarak al.** [ÇIK]
  - CLAUDE.md yalnız ajanın koddan ve repodan çıkaramayacağı zorunlu kuralları taşır: yetki sınırı, kanıt biçimi, nereden başlanır. Kısa tutulur; LLM'e yazdırılmaz.
  - Değişiklik sonda görevleriyle önce ve sonra ölçülür. Doğruluğu değil, en azından süreyi ve maliyeti etkilediği bilinir.
  - Kural metninin kendisi sürümlenir ve sürüm kaydı tutulur.
  - Çelişki: O6 ve O7'nin "kısa CLAUDE.md" önerisi bu bulgularla uyumlu. §3.6'daki 660 satırlık anayasa bu bulgulara aykırı.

### 3.4 Skill'ler: SkillsBench (Li vd., 2602.12670, Şubat 2026) [AÖ]
- 86 görev, 11 alan, deterministik doğrulayıcılar. 7 ajan ve model düzeni, 7.308 iz.
- Seçilmiş skill'ler ortalama +16,2 puan: yazılım mühendisliğinde +4,5, sağlıkta +51,9. 84 görevin 16'sında etki negatif.
- Ajanın kendi yazdığı skill'ler ortalama −1,3: "models cannot reliably author the procedural knowledge they benefit from consuming".
- 3 modülü geçmeyen odaklı skill, kapsamlı paketten iyi. Skill'li küçük model, skill'siz büyük modele yetişebiliyor.
- **DevOS: Al.** Skill kabulü ölçümle olur. Otomatik skill üretimi yalnız aday üretir. Skill odaklı tutulur.

### 3.5 Eski gözlemleri maskelemek ve özetlemek
- **The Complexity Trap (Lindenbauer vd., 2508.21433, Ağustos 2025; NeurIPS 2025 DL4Code) [KOD README + AÖ].**
  - SWE-agent, SWE-bench Verified, 5 model düzeni.
  - Son M=10 gözlemi bırakıp eskilerini maskelemek, ham ajana göre maliyeti yaklaşık yarıya indiriyor ve LLM özetlemesi kadar, bazen biraz daha iyi çözüyor. Qwen3-Coder 480B'de ham %53,8, maskeleme %54,8.
  - README: "The more recent LLM-Summary strategy is unable to consistently or significantly outperform a simple Observation Masking baseline". Karma yöntem maliyeti ek %7–11 düşürüyor. Bulgu OpenHands'e genelleniyor.
- **SWE-agent 0.7 [KOD]:** `history_processors: - type: last_n_observations  n: 5`.
- **Harness tasarımı çalışması (2609.20804, Eylül 2026) [AÖ].** 4 model, SWE-bench Verified ve Terminal-Bench 2.1'de 176 düzen.
  - Bağlam yönetimi, bütçe daraldıkça önem kazanıyor; faydası çoğunlukla taşma hatalarını önlemekten geliyor.
  - Planlama zayıf modelde doğruluk iskelesi, güçlü modelde maliyet tasarrufu.
  - Bash'i iyi kullanan model yalnız bash ile iyi iş çıkarıyor.
- **DevOS: Al.** [ÇIK] Uzun araç çıktısı dosyaya yazılır; bağlama yol ve kısa özet girer. Alt ajan dönüşü kısa olur. Ana oturum ham log taşımaz. Sıkıştırmadan sonra defter ve STATE dosyadan yeniden okunur.

### 3.6 Katmanlı bağlam ve bayat belge uyarısı: Codified Context (Vasilopoulos, 2602.20478, Şubat 2026)
- **İşleyiş [KOD]:**
  - Katman 1, "constitution": `CLAUDE.md`, yaklaşık 660 satır. Kurallar, derleme komutları, kontrol listeleri, "agent trigger table", önemli dosya haritası.
  - Katman 2: 19 uzman ajan.
  - Katman 3: `.claude/context/*.md` altında 34 belirtim belgesi ve MCP geri çağırma araçları (`list_subsystems`, `find_relevant_context`, `search_context_docs`, `suggest_agent`…).
  - SessionStart hook'u `python3 .claude/scripts/context-drift-check.py` komutunu koşar:
    - alt sistemlerin kod kalıplarını belgelere eşler;
    - son 10 commit belgeyi güncellemeden koda dokunduysa uyarıyı bağlama basar;
    - öncelik HIGH, MEDIUM ya da LOW; LOW susturulur;
    - son 3 oturumdaki hata ayıklama sözcüklerinden puan çıkarır (eşik 50);
    - yeni commit gelmezse uyarı 2 gösterimden sonra kendiliğinden kapanır;
    - boş çıktı "uyarı yok" demektir.
- **Kanıt [KOD README]:** Tek geliştirici, 108 bin satırlık C# sistemi, 283 oturum.
  - Bilgi-kod oranı yaklaşık %24.
  - 2.801 istem → 1.197 ajan çağrısı → 16.522 ajan turu.
  - 4 gözlemsel vaka; kontrollü karşılaştırma yok.
- **DevOS: Uyarlayarak al.** Bayat belge kontrolü alınır: kod ya da iş yolu ile belge eşleme tablosu, SessionStart'ta uyarı. Bu, Batu'nun 4. gereksinimine ("eskiyen kayıt fark edilir") doğrudan cevap verir. 660 satırlık anayasa alınmaz (§3.3).

### 3.7 Derlemeler ve katlama
- **Context engineering derlemesi (Mei vd., 2507.13334, Temmuz 2025) [AÖ + KOD: yazarların `Meirtz/Awesome-Context-Engineering` @8b6ede2 README'si].**
  - Sınıflama [AÖ]: bağlam bulma ve üretme, işleme, yönetim. Uygulamalar: RAG, bellek, araçla akıl yürütme, çok ajan. 1.400'ü aşkın makale [AÖ-y].
  - Tanım [KOD]: "Context is the complete information payload provided to a LLM at inference time". Biçimsel olarak `context = Assemble(instructions, knowledge, tools, memory, state, query)`, kısıt `|context| ≤ MaxTokens`. `memory = Select(history, query)`, `state = Extract(world)`.
  - DevOS karşılığı [ÇIK]: instructions = CLAUDE.md ve kurallar; knowledge = skill ve belgeler; tools; memory = ders defteri; state = STATE ve iş defteri; query = görev. Her bileşenin kim tarafından, hangi tetikle bağlama girdiği yazılı olmalı.
- **Context-Folding (2510.11967, Ekim 2025) ve AgentFold (2510.24699) [AÖ].** Alt işe dallanıp bitince ara adımları özetle "katlamak"; pekiştirmeli öğrenmeyle eğitiliyor.
- **DevOS:** Sözlük olarak al. Eğitim isteyen yöntemleri alma. Alt ajan dönüşü zaten bir "katlama"dır [ÇIK].

---

## 4. Yazılım ajanları: ACI, SOP, roller, orkestratör

### 4.1 SWE-agent ve ACI (2405.15793, Mayıs 2024; NeurIPS 2024)
- **İşleyiş [KOD, `docs/background/aci.md` ve 0.7 yapılandırması]:**
  - Linter korumalı düzenleme: "do not let the edit command go through if the code isn't syntactically correct".
  - 100 satırlık dosya görüntüleyici: `WINDOW: 100`, `OVERLAP: 2`.
  - Arama yalnız eşleşen dosyaları listeler: "Showing the model more context about each match proved to be too confusing for the model."
  - Boş çıktıya sabit ileti: "Your command ran successfully and did not produce any output."
  - Tur başına tek komut; son 5 gözlem tutulur.
- **Kanıt [AÖ]:**
  - GPT-4 Turbo ile SWE-bench tamda %12,47, Lite'ta %18,0 [AÖ-y]. Yalnız kabuk kullanan ajana göre %64 göreli artış [AÖ].
  - Linter koruması 15,0 → 18,0 [AÖ-y]; 100 satırlık pencere en iyisi (`aci.md`: "works best when displaying just 100 lines" [KOD]).
- **Sınır:** 2024 modelleri; ölçüt sorunları §1.4.
- **DevOS: Al (araç tasarım ilkeleri).** DevOS betikleri kısa ve özlü çıktı verir. Boş sonucu açıkça söyler. Hatalı işlemi geri çevirir; örneğin durum dosyası şemaya uymuyorsa yazım reddedilir.

### 4.2 Agentless (2407.01489, Temmuz 2024) [KOD README + AÖ]
- **İşleyiş:** Üç sabit aşama. Önce kademeli konum bulma: dosya → sınıf ya da fonksiyon → satır. Sonra birden çok aday yama. Son olarak regresyon testi ve üretilmiş yeniden üretim testiyle sıralayıp seçme.
- **Kanıt:**
  - README: v1.0'da Lite'ta %27,3, sorun başına $0,34. Claude 3.5 Sonnet ile Lite %40,7 ve Verified %50,8 (Aralık 2024).
  - [AÖ-y] v1.5'te %32,00 (96 çözüm), $0,70.
  - Yazarlar, çözümü issue'da yazan ya da eksik tanımlı görevleri çıkarıp Lite-S'i kurmuş.
- **DevOS: Al (ilke).** Basit sabit akış güçlü bir tabandır. DevOS'un karmaşık parçaları bu tür bir tabanla karşılaştırılır. O9'un "karmaşıklığı yalnız koruduğu gereksinimle ekle" ilkesiyle aynı.

### 4.3 MetaGPT (Hong vd., 2308.00352, Ağustos 2023; ICLR 2024)
- **İşleyiş [KOD]:**
  - Roller `profile`, `goal` ve `constraints` taşır. Ürün yöneticisi `WritePRD`, mimar `WriteDesign`, proje yöneticisi `WriteTasks`, mühendis `WriteCode` yazar.
  - QA `_watch([SummarizeCode, WriteTest, RunCode, DebugError])` ile abone olur.
  - Tasarım belgesi yapılandırılmış alanlarla üretilir (`ActionNode`): "Implementation approach", "File list", "Data structures and interfaces", "Program call flow", "Anything UNCLEAR".
- **Kanıt [AÖ]:**
  - HumanEval %85,9 ve MBPP %87,7 pass@1 [AÖ-y].
  - Kendi SoftwareDev setinde çalıştırılabilirlik 3,75 (ChatDev 2,25, ölçek 1–4) [AÖ-y]. Geri bildirimle insan düzeltme maliyeti 2,25 → 0,83 [AÖ-y]; uygulanabilirlik 3,67 → 3,75 [AÖ].
  - Çalıştırılabilir geri bildirim +4,2 [AÖ-y] ve +5,4 [AÖ] puan.
- **Sınır:** Kendi kurdukları küçük set; insan puanlaması.
- **DevOS: Uyarlayarak al.** Devir belgesinin alanları zorunlu olur ve bir "Belirsiz kalanlar" alanı taşır (K04). Yayın-abonelik yerine dosya ve iş kaydı kullanılır. Rol adları şirket rolü olmaz, işlev adı olur.

### 4.4 ChatDev (2307.07924, Temmuz 2023; ACL 2024)
- **İşleyiş [KOD, `chatdev1.0`]:**
  - Zincir: DemandAnalysis, LanguageChoose, Coding, CodeCompleteAll, CodeReview, Test, EnvironmentDoc, Manual.
  - CodeCompleteAll en çok 10 tur. CodeReview 3 tur, yorum → düzeltme. Test 3 tur, hata özeti → düzeltme.
  - İnceleyici istemi: "check the above regulations one by one ... propose one comment with the highest priority ... If the codes are perfect and you have no comment on them, return only one line like '<INFO> Finished'".
- **Kanıt [AÖ]:**
  - Kalite 0,3953; GPT-Engineer 0,1419; MetaGPT 0,1523.
  - Rolsüz sürümde kalite 0,2212, çalıştırılabilirlik 0,88 [AÖ-y] → 0,58.
- **Sınır [KOD, MAST tanımları]:** Aynı inceleyici istemiyle, önceden doldurulmuş hücresi olmayan Sudoku ve kazananı yanlış ilan eden TicTacToe onaylanmış. Birden çok inceleme aşamasına rağmen derlenmeyen oyun "doğrulanmış".
- **DevOS:** Şirket rol-oyununu alma. Tur sınırı ve açık "bitti" işareti al. İnceleme, çalıştırılan kontrolle yapılır.

### 4.5 Magentic-One (Fourney vd., 2411.04468, Kasım 2024)
- **İşleyiş [KOD, `_prompts.py` ve `_magentic_one_orchestrator.py`]:**
  - Görev defteri ön anketi dört başlıklı: "1. GIVEN OR VERIFIED FACTS 2. FACTS TO LOOK UP 3. FACTS TO DERIVE 4. EDUCATED GUESSES". Ardından kısa madde planı gelir; "there is no requirement to involve all team members".
  - Her turda ilerleme defteri JSON olarak yazılır: `is_request_satisfied`, `is_in_loop`, `is_progress_being_made`, `next_speaker`, `instruction_or_question`; her biri `reason` ve `answer` taşır.
  - Kod: ilerleme yoksa ya da döngüdeyse `n_stalls += 1`, yoksa `max(0, n_stalls - 1)`. Varsayılanlar `max_stalls=3`, `max_turns=20`. `n_stalls >= max_stalls` olunca olgu sayfası yeniden yazılır, plan güncellenir ve dış döngüye dönülür.
  - Plan güncelleme istemi: "Please briefly explain what went wrong on this last run (the root cause of the failure), and then come up with a new plan that ... avoids repeating the same mistakes".
- **Kanıt [AÖ]:** GAIA, AssistantBench ve WebArena'da en iyilerle istatistiksel olarak rekabetçi. Orkestratör yerine GroupChat benzeri basit seçici konunca GAIA geliştirme setinde %31 kayıp [AÖ-y].
- **DevOS: Al.** [ÇIK]
  - İş defteri bu alanları taşır. Olguların dörde ayrılması Batu'nun 4. gereksinimini karşılar: karar, öneri, varsayım ve doğrulanmış bilgi karışmaz.
  - Durma sayacı ve "kök neden + yeni plan" kuralı alınır.
  - Orkestratör ana oturumdur, çünkü alt ajan derinliği 1.

### 4.6 Paralel yazma: Claim Plane (2607.21909, Temmuz 2026; 2608.00947, Ağustos 2026) [AÖ]
- **İşleyiş:** Sürümlü "değişiklik niyeti" üzerinden, yazmadan önce deterministik kabul.
- **Kanıt:**
  - 30 CooperBench özellik çifti (15 çakışan, 15 temiz) × 3 tohum × 4 düzen = 360 koşu.
  - Çift başarısı %23,3 → %50,0 (+26,7 puan; %95 GA 9,6–60,0). Entegrasyon başarısı %65,6 → %96,7. Çakışan çiftlerde %6,7 → %60,0.
  - Ama işlerin %96,7'si sıraya sokulmuş; temiz çiftlerin de %93,3'ü.
- **DevOS: Al (K09 tek yazıcı).** Yazan iş, yazmadan önce yol talebini defterde kaydeder. Paralel yazmadan çok hız beklenmez. O9'un kira (lease) önerisiyle birleşir.

---

## 5. Çok ajanlı sistemler: hata sınıflaması, hata atama, ölçekleme

### 5.1 MAST (Cemri vd., 2503.13657, Mart 2025; NeurIPS 2025 D&B)
- **Taksonomi [KOD, `definitions.txt` ve figür]:**
  - 1 spesifikasyon ve sistem tasarımı: 1.1 Disobey Task Specification, 1.2 Disobey Role Specification, 1.3 Step Repetition, 1.4 Loss of Conversation History, 1.5 Unaware of Termination Conditions.
  - 2 ajanlar arası uyumsuzluk: 2.1 Conversation Reset, 2.2 Fail to Ask for Clarification, 2.3 Task Derailment, 2.4 Information Withholding, 2.5 Ignored Other Agent's Input, 2.6 Action-Reasoning Mismatch.
  - 3 görev doğrulama: 3.1 Premature Termination, 3.2 Weak Verification, 3.3 No or Incorrect Verification. Tanımdan: "Eg: make sure the code compiles, but the code doesn't even compile." ve "Verification is particularly critical in cases where tasks or outputs are readily verifiable by the system itself without human intervention."
- **Kanıt:**
  - Repodaki v1 figüründe sınıf payları %37,17 / %31,41 / %31,41 [KOD].
  - Sonraki sürümde 7 çerçeveden 1.600'ü aşkın iz ve %41,8 / %36,9 / %21,3 [AÖ; doğrulanmadı].
  - İnsanlar arası uyum κ=0,88. LLM yargıç %94 doğruluk, κ=0,77 [AÖ].
  - Müdahaleler: doğrulama bölümü eklenmiş istem ve yeni topoloji [AÖ]. ChatDev'de +%14 [AÖ-y]; "do not resolve all failure cases" [AÖ].
- **DevOS: Al.** Olay kaydının "hata modu" alanı MAST kodunu taşır. 3.x sınıfının varlığı §1'deki doğrulama hattının gerekçesidir.

### 5.2 Who&When (Zhang, Yin vd., 2505.00212, Mayıs 2025; ICML 2025) [TM]
- **Veri:**
  - 127 çok ajanlı sistem: CaptainAgent'ın ürettiği sistemler ve el yapımı Magentic-One.
  - GAIA ve AssistantBench sorguları; 184 etiketli başarısızlık görevi.
  - Etiket şu soruyu cevaplar: hangi ajan, hangi "karar adımında" hatayı yaptı.
- **Yöntem:**
  - Üç yöntem: "all-at-once" (tüm kayıt tek seferde), "step-by-step" (adım adım durana kadar), "binary search" (yarıya bölerek).
  - İki düzen: gerçek cevap biliniyor ya da bilinmiyor.
- **Sonuç (GPT-4o):**
  - En iyi ajan düzeyi %53,5; adım düzeyi yalnız %14,2. Bazı yöntemler rastgelenin altında.
  - Gerçek cevap bilinirken (algoritmik / el yapımı sistemler): all-at-once ajan doğruluğu 54,33 ve 55,17; ama adım doğruluğu 12,50 ve 5,26. Rastgele adım doğruluğu 19,06 ve 4,16.
  - Step-by-step adım düzeyinde en iyi, ama pahalı.
  - Karma yöntem (önce ajanı bul, sonra onun adımlarını tara), el yapımı sistemlerde: ajan %57,02, adım %12,28. Token maliyeti 149.177; all-at-once 17.106.
  - "Finding 4: Failure attribution performance declines as context length increases, with step-level accuracy being more sensitive."
  - İstatistik düzeyinde en çok hata yapan ajan doğru bulunuyor (Finding 6). o1 ve R1 de "fail to achieve practical usability".
- **DevOS: Al.** Hata atama birikmiş olaylardan istatistikle yapılır. Tek olayda "suçlu adım" LLM'e sorulmaz. Kayıtlar kısa ve adımlı tutulur; uzun kayıtta atama kötüleşiyor.

### 5.3 Çok ajanlı sistemlerin ölçeklenmesi (Kim vd., 2512.08296, Aralık 2025) [AÖ]
- **Tasarım:** Beş mimari (tek, bağımsız, merkezi, merkezsiz, karma), üç model ailesi, 180 düzen.
- **Sonuçlar:**
  - Tek ajan tabanı yaklaşık %45'i aşınca [AÖ-y] koordinasyonun getirisi azalıyor ya da negatife dönüyor (β=−0,408, p<0,001).
  - Hata büyütme: bağımsız ajanlarda 17,2 kat, merkezi yapıda 4,4 kat.
  - Paralel yapılabilen finansal akıl yürütmede merkezi yapı +%80,9. Dinamik web gezintisinde merkezsiz yapı +%9,2 (merkezi +%0,2).
  - Sıralı akıl yürütmede bütün çok ajanlı türler %39–70 kaybettiriyor.
  - Öngörü modeli R²=0,513; ayrılmış düzenlerin %87'sinde doğru mimariyi seçiyor.
- **Sınır:** Kodlama işine geçerliliği tam metinde (okunamadı).
- **DevOS: Al.** Varsayılan tek uygulayıcıdır. Çok ajan yalnız paralel ve bağımsız işte kullanılır: okuma, arama, bağımsız doğrulama. Birleştirme merkezidir (orkestratör). Sıralı mantık zinciri tek ajanda kalır.

### 5.4 Tartışma mı oylama mı
- **2508.17536 (Ağustos 2025) [AÖ]:** Çok ajanlı tartışmanın kazancının çoğunu çoğunluk oylaması açıklıyor. Kuramsal olarak tartışma inançlarda bir martingal; beklenen doğruluğu artırmıyor. Önceki çalışmalara göre eşit sayıda cevapla öz-tutarlılık tartışmayı geçiyor.
- **DevOS:** Tartışma döngüsünü alma. Gerekirse bağımsız örnekler ve oylama.

### 5.5 Sessiz hatalar (2606.14589, Haziran 2026) [AÖ]
- **Ortam:** Mart 2026'dan beri üretimde bir kişisel asistan çalışma zamanı. Yaklaşık 40 zamanlanmış iş, 8 sağlayıcı, 4.286 birim testi, 827 yönetişim kontrolü.
- **Sonuçlar:**
  - 8 haftada kök neden analizi yapılmış 22 olay. Hata sinyalinin insana eyleme dönük biçimde hiç ulaşmaması deseni en az 28 kez.
  - Beş sınıf:
    - A: ortam ve platform tuhaflıkları;
    - B: tasarım varsayımı uyuşmazlığı;
    - C: hatanın yutulması ve seyrelmesi;
    - D: zincirleme halüsinasyon ve uydurma ("fail-plausible": LLM hatayı akıcı bir anlatıya çeviriyor);
    - E: operasyonel ihmal ve adli kör nokta.
  - Sessiz hataların yaklaşık %70'ini testler değil, çıktıyı kullanıcı gözüyle okuyan insan buldu.
- **DevOS: Al.** [ÇIK]
  - Hook'lar çıkış kodunu ham kaydeder.
  - Rapor ham kanıta işaret eder.
  - Periyodik bir "kullanıcı gözüyle denetim" alt ajanı, Batu'nun göreceği çıktıyı okur ve iddiaları kanıtla eşler.
  - Bu, Batu'nun 7. gereksinimini karşılar: "bozulan denetim ... sessizce de kapanmaz".

---

## 6. Kendini geliştiren ajanlar

### 6.1 ADAS: Meta Agent Search (Hu, Lu, Clune; 2408.08435, Ağustos 2024; ICLR 2025)
- **İşleyiş [KOD]:**
  - Arşiv, kod olarak tanımlı ajanlar tutar: `forward()`.
  - Meta ajan (kodda varsayılan `gpt-4o-2024-05-13`; değerlendirilen ajanlar `gpt-3.5-turbo-0125`) arşive bakıp "the next interesting agent" önerir. Alanları `thought`, `name`, `code`.
  - İki Reflexion turu yapılır. Birincisi şunları sorgular: "Interestingness", uygulama hataları, iyileştirme.
  - Aday doğrulama setinde (DROP'ta 128 örnek) değerlendirilip arşive eklenir. En sonda arşivin **hepsi** test setinde (800 örnek) değerlendirilir.
- **İddia [AÖ-y; iki sayıyı sonuç dosyasından kendim doğruladım]:** En iyi elle tasarlanmış ajana göre DROP'ta +13,6 F1, MGSM'de +14,4 puan; modeller ve alanlar arası aktarım var [AÖ].
- **Benim veri denetimim [gözledim, `results/*_gpt3.5_results.json`, `_drop/utils.py`]:**
  - Sayılar dosyadan çıkıyor. DROP'ta en yüksek test 79,4 (30. nesil "Distributed Consensus Agent"), en iyi başlangıç ajanı 65,8, fark 13,6. MGSM'de 53,4 ile 39,0, fark 14,4.
  - DROP'ta 79,4 alan ajan doğrulama sırasında 4. sırada (70,2). Doğrulamada birinci olan ajan (73,5) testte 70,7 almış. Manşet sayı test üzerinden seçilmiş en yüksek değer gibi görünüyor. Makalenin seçim protokolünü okuyamadım.
  - Aynı kod (aynı md5) dosyada iki kez test edilmiş: medyan 75,4 ve 79,4. Tekrar gürültüsü yaklaşık 4 F1; manşetteki büyük olan.
  - `bootstrap_confidence_interval` işlevi yüzdelik olarak 0,025 ve 0,975'i `np.percentile`'a veriyor. Bu işlev 0–100 bekler. Dosyadaki "95% Confidence Interval" gerçekte dağılımın en alttaki ~%1'lik kuyruğudur; medyanın aralığın dışında kalması bundandır.
- **DevOS: Kurala çevir.** Tek koşuyla karşılaştırma yapılmaz. Seçim doğrulama setiyle yapılır; test ya da ayrılmış set seçimde kullanılmaz. Değerlendirme kodunun kendisi test edilir (ABC). Kazanç, tekrar gürültüsünün üstündeyse kabul edilir.

### 6.2 Gödel Agent (2410.04444, Ekim 2024)
- **İşleyiş [KOD]:**
  - `action_adjust_logic` yeni kodu `exec` ile kendi modülüne yamar (monkey patch).
  - Birkaç sert koruma var: "Don't use `time.sleep` in solver.", "Don't modify `action_call_llm`.", `logging` yasağı.
  - Hedef istemi: "**Complete Autonomy**: Have **unrestricted access** to modify logic, run code and manipulate environment."
  - Değerlendirmeyi (`action_evaluate_on_task`) ne zaman çağıracağına ajanın kendisi karar veriyor.
- **Kanıt [AÖ]:** Matematikte meta-öğrenme yöntemlerine göre yaklaşık %11 artış; elle yapılmış ajanları geçtiği iddiası.
- **DevOS:** Sınırsız öz-değişikliği alma. Sert koruma listesi mantığını al; DevOS'ta bu hook ve izin demektir.

### 6.3 Darwin Gödel Machine (Zhang, Hu, Lu, Lange, Clune; 2505.22954, Mayıs 2025)
- **İşleyiş [KOD, `DGM_outer.py` ve `prompts/`]:**
  - Arşiv `initial` ile başlar.
  - Ebeveyn `score_child_prop` ile seçilir: `sigmoid(10·(score−0.5)) × 1/(1+children)`.
  - Her ebeveyn için giriş seçimi:
    - boş yama oranı %10'u aşıyorsa %25 olasılıkla "solve_empty_patches";
    - %25 olasılıkla "solve_stochasticity";
    - bağlam hatası varsa %25 olasılıkla "solve_contextlength";
    - yoksa çözülmemiş rastgele bir issue.
  - Teşhis istemine şunlar girer: ajanın kaydı, issue, tahmin yaması, "SWE-bench's official private tests ... This is not available to the agent during evaluation", sonuçlar. Çıktı JSON'dur: `log_summarization`, `potential_improvements`, "`improvement_proposal`: Choose ONE high-impact improvement", `implementation_suggestion`, `problem_description` ("as a GitHub issue").
  - Kural: "The improvement should not be specific to any particular GitHub issue or repository".
  - Ajan bu issue'yu kendi kodunda uygular.
  - Değerlendirme aşamalıdır: küçük alt küme; ≥0,4 ise orta küme; arşivdeki ikinci en iyi skoru (en az 0,4) geçerse tam set.
  - "Compiled" süzgeci en az bir boş olmayan yama ister.
  - Arşiv `keep_all` (açık uçlu) ya da `keep_better`, gürültü payı 0,1.
  - Deneme başına 1,5 saat zaman aşımı; 80 nesil × 2.
- **Kanıt [AÖ]:**
  - SWE-bench %20,0 → %50,0; Polyglot %14,2 → %30,7 [AÖ-y].
  - Ajan kendi başına daha iyi düzenleme araçları, uzun bağlam yönetimi ve "peer-review" buldu.
  - **Amaç hilesi:** halüsinasyon sorununu "çözmek" istenince 114. düğüm halüsinasyon tespit işaretçilerini sildi. 96. düğüm ise meşru bir çözüm buldu.
  - Önlemler: sandbox, süre sınırı, insan gözetimi.
- **DevOS: Uyarlayarak al.** Döngünün biçimi alınır: kayıt → tek ve genel iyileştirme önerisi (issue biçiminde) → aşamalı değerlendirme → arşiv. Değerlendirici, ölçüt kodu ve işaretçiler ajanın yazamadığı yerde durur (K07). Açık uçlu arşiv canlı işte değil, deney dalında tutulur.

### 6.4 SICA (Robeyns, Szummer, Aitchison; 2504.15228, Nisan 2025; ICLR 2025 atölyesi)
- **İşleyiş [KOD]:**
  - Döngü: değerlendir → arşivle → ajanı kendi kodunda çalıştır → tekrar.
  - Problem başına 10 dk ve $3 sınırı (`runner.py`). Fayda: `0.5·skor − 0.25·maliyet − 0.25·süre`, maliyet $10'da kesilir [AÖ-y].
  - `agent_change_log.md` bir tablo tutar: Iteration | Change Name | Was Successful? (pending/yes/no). "Feature Description" i. turda yazılır; "Feature Outcome" i+1. turda: "comments on the empirical effectiveness of the change".
  - Asenkron izleyici `overseer.py`, 60 sn'de bir çağrı grafiğine bakar ve şu kurallarla çalışır:
    - "try to use a different model to the main loop model";
    - "YOU MUST make at least one attempt to notify the agent of its wrongdoings before issuing a cancellation command";
    - iptal ederken ebeveyne "handoff notes" verir;
    - "'Success' ... has no bearing on whether the exit code was 0 or 1";
    - kendi kodunu düzenlerken "the code it is editing is not the code that it is currently running";
    - "Do not start 'back seat driving'".
- **Kanıt [AÖ]:**
  - SWE-bench Verified'ın rastgele bir alt kümesinde %17 → %53 [AÖ-y].
  - AIME ve GPQA'da o3-mini ile küçük kazanç: sistem ortalaması %76; model tek başına %87 ve %79.
  - İlk fikirler sonrakileri belirliyor ("path dependence").
- **DevOS: Al.** Değişiklik defteri ve izleyici kuralları alınır. Kural değişikliğinin sonucu bir sonraki turda yazılır. İzleyici önce uyarır, sonra durdurur; durdururken devir notu bırakır.

### 6.5 Huxley-Gödel Machine (Wang vd., 2510.21614, Ekim 2025; ICLR 2026 sözlü) [AÖ + README]
- **Bulgu:** "Metaproductivity–performance mismatch". Bir ajanın bugünkü skoru, iyi torunlar üretme gücünü zayıf öngörüyor.
- **Çözüm:** Torunların başarısını toplayan "clade metaproductivity" ile genişletme.
- **Kanıt:** SWE-bench Verified-60'ta %56,7, Polyglot'ta %30,5. DGM'den 2,38 ve 6,86 kat daha az CPU saati.
- **DevOS [ÇIK]:** Bir kural değişikliği yalnız anlık ölçümle değil, sonraki değişikliklere etkisiyle de değerlendirilir. Düşük öncelik.

### 6.6 STOP (Zelikman vd., 2310.02304, Ekim 2023) [AÖ]
- **İşleyiş:** Tohum "improver" kendini iyileştiriyor; ışın arama, genetik algoritma ve benzetilmiş tavlama gibi stratejiler buluyor.
- **Kanıt:** Makale, üretilen kodun sandbox'ı ne sıklıkla aştığını tartışıyor. Oranı okuyamadım.
- **DevOS:** Uyarı olarak al. Öz-geliştirici kod güvenlik bayrağını kapatabilir; koruma ajanın dışında olmalı (hook, izin).

### 6.7 Harness evrimi ve eleştirisi
- **AHE (2604.25850, Nisan 2026) [AÖ].**
  - Üç gözlenebilirlik sütunu:
    - bileşen: her harness parçası dosya olarak açık ve geri alınabilir;
    - deneyim: katmanlı, inilebilir kanıt derlemi;
    - karar: her düzenleme kendi beyan ettiği bir öngörüyle eşleşir ve sonraki turda doğrulanır.
  - Terminal-Bench 2'de 10 turda 69,7 → 77,0 (Codex-CLI 71,9). SWE-bench Verified'da %75,6 ve %12 daha az token. Görülmemiş 5 modelde +2,3 ile +10,1.
  - Kazanç uzun süreli bellek, araçlar ve ara katmanda. Düzeltme öngörüleri rastgeleden 5 kat isabetli, ama "regression blindness" var.
- **Rethinking the Evaluation of Harness Evolution (2607.12227, Temmuz 2026) [AÖ].** Terminal-Bench 2.1, GPT-5.4 ve Opus 4.6. Eşit geri bildirim ve çıkarım bütçesiyle basit test-zamanı ölçeklemeye göre harness evrimi tutarlı biçimde daha iyi değil; genellemesi zayıf; kazanç çoğunlukla tekrarlı örneklemeden geliyor; arama ve değerlendirme aynı sette.
- **DevOS: Al.** Karar gözlenebilirliği (öngörü + sonraki turda sonuç) alınır. Uyarlama: ayrılmış (holdout) senaryolar ve eşit bütçeli taban karşılaştırması şart. Gerileme testi, öngörüye güvenilmeden koşulur.

### 6.8 Ouroboros (2608.08311, Ağustos 2026) [AÖ; ikincil blog ve özetler]
- **İşleyiş:**
  - Araçlar, istemler, bağlam kurulumu ve çekirdek kod "reviewed commits" ile değişiyor; birleşen commit sonraki işin çalışma zamanı oluyor.
  - İki kip: özyinelemeli serbest evrim ve deneyimden çekirdek evrimi. 161 günlük "Hope" deneyi.
- **Güvenlik mimarisi:**
  - Anayasa (`BIBLE.md`) kesilmeden yükleniyor ve inceleme bağlamına giriyor.
  - Deterministik korumalar yönetişim dosyalarını sıradan yazma araçlarından koruyor.
  - Sahnelenen diff inceleme öncesi ve sonrası parmak iziyle bağlanıyor.
  - Yeter sayıya ulaşmamış bir panel "temiz geçti" diyemiyor.
  - Görev, model yönlendirme, bütçe ve `/panic` ayrı ve kimlik doğrulamalı bir operatör kanalından geliyor; durdurma komutu ajandan önce denetleyicide işleniyor ve süreç ağacını sonlandırıyor. "No recorded episode resisted operator shutdown."
  - İlk 48 saatte 32 evrim döngüsü (v4.1 → v6.2.0).
  - Kıyas iddiaları: Opus 5 ile Terminal-Bench 2.1 %86,74, OSWorld-Verified %90,69.
- **Sınır [ÇIK]:** Yapanların teknik raporu; bağımsız tekrar yok.
- **DevOS: Uyarlayarak al (yönetişim deseni).** Kural dosyaları hook ile korunur; değişiklik ayrı bir işle gelir. İncelenen diff ile uygulanan diff aynı olmalı: diff hash'i defterde tutulur. Batu'nun "dur" kanalı olur (ör. STATE'te okunan bir durdurma işareti; uygulanabilirliği O11'e bağlı).

### 6.9 GEPA (2507.19457, Temmuz 2025; ICLR 2026 sözlü) [AÖ]
- **İşleyiş:** İstemleri yeni denemelerden gelen doğal dil geri bildirimiyle değiştiriyor. Örnek başına Pareto cephesi tutuyor.
- **Kanıt:** GRPO ve MIPROv2'yi daha az denemeyle geçiyor.
- **DevOS:** Düşük öncelik. İleride kural ve istem metnini izlerden yansıtmalı evrimle iyileştirmek için aday.

### 6.10 Önceki notlarla ilişki
- O6'nın "Kendini geliştiren otomatik döngü hiçbir kaynakta kanıtlanmış değil" hükmü kısmen düzeltilmeli.
  - Akademide, sabit değerlendiricili ve sandbox'lı kıyas ortamlarında otomatik döngü kazanç gösteriyor: DGM, SICA, ADAS, AHE [AÖ].
  - Ama gürültü (§6.1), aşırı uyum ve eşit bütçeli taban karşısında zayıflık (2607.12227) ve amaç hilesi (DGM) raporlanmış.
  - Açık uçlu gerçek bir projede "evrensel servis" olarak kanıt yok; burada O6 haklı.
- O8'in "qualified feedback" kuralı ve Meta-Harness'ta eksik görevin başarı sayılması, §6.1 ve ABC ile aynı yönde.

---

## 7. Uzun soluklu özerklik ve değerlendirme

### 7.1 METR zaman ufku (2503.14499, Mart 2025) [AÖ]
- **Tanım:** %50 zaman ufku, modelin %50 başarıyla bitirdiği işlerin insan için süresidir. Claude 3.7 Sonnet için yaklaşık 50 dk. 2019'dan beri yaklaşık 7 ayda iki katına çıkıyor [AÖ-y].
- **Sınırlar:** %80 ufku yaklaşık 5 kat kısa. "Messier" işlerde başarı düşük.
- **2026 güncellemeleri [AÖ; metr.org kapalı]:**
  - Time Horizon 1.1: görev sayısı 170 → 228. 16 saatin üstündeki tahminler güvenilmez, çünkü takım doyuyor.
  - Opus 4.6 yaklaşık 14,5 sa (%95 GA 6–98 sa).
  - "Time horizon is not the length of time AIs can work independently."
  - Şubat 2026 notu: Claude Code ve Codex iskeleleri METR'in varsayılan iskelelerini geçmedi (Opus 4.5, GPT-5).
- **DevOS [ÇIK]:** İş birimi %80 güvenilirlik ufkunun içinde boyutlanır. Claude Code harness'ı tek başına yetenek eklemez. DevOS'un değeri süreklilikte, doğrulamada ve kayıttadır, ham yetenekte değildir.

### 7.2 Kendini koşullama (2509.09677, Eylül 2025; ICLR 2026) [AÖ]
- **Yöntem:** Plan ve bilgi verilerek yalnız yürütme ölçülüyor.
- **Sonuç:** Adım sayısı arttıkça adım başı doğruluk düşüyor. Modelin kendi hatalarını bağlamda görmesi yeni hata olasılığını artırıyor ("self-conditioning"). Düşünen modeller bunu azaltıyor; GPT-5 thinking 2.100'ü aşkın adım yürütüyor.
- **DevOS: Al.** Yeni birime taze bağlamla geçilir. Hatalı geçmiş taşınmaz; STATE'e yalnız doğrulanmış durum yazılır.

### 7.3 Vending-Bench (Backlund ve Petersson, 2502.15840, Şubat 2025) [AÖ]
- **Ortam:** Otomat işletme; koşu başına 20 milyonu aşkın token.
- **Sonuç:** Varyans yüksek. Claude 3.5 Sonnet ve o3-mini çoğu koşuda kâr ediyor, ama bütün modellerin raydan çıkan koşuları var: teslim takvimini yanlış okuma, siparişi unutma, nadiren toparlanan "meltdown" döngüleri.
- **DevOS: Al.** Durma ve döngü tespiti (§4.5). Periyodik bağımsız durum denetimi.

### 7.4 τ-bench ve pass^k (Yao vd., 2406.12045, Haziran 2024)
- **İşleyiş [KOD]:**
  - pass^k: k denemenin hepsinin başarılı olma olasılığı.
  - README tablosu, Claude 3.5 Sonnet (Ekim 2024): perakendede pass^1..4 0,692 / 0,576 / 0,509 / 0,462; havayolunda 0,460 → 0,225.
  - `auto_error_identification.py` hatanın sahibini (`user`, `agent`, `environment`) ve türünü (`called_wrong_tool`, `used_wrong_tool_argument`, `goal_partially_completed`…) LLM'e sınıflatıyor.
- **Kanıt [AÖ-y]:** gpt-4o görevlerin yarısından azını çözüyor; perakendede pass^8 %25'in altında.
- **Sınır:** Görevler sonradan düzeltilmiş (τ²/τ³). ABC'ye göre hiçbir şey yapmayan ajan %38 alıyor.
- **DevOS: Al.** DevOS'un kendi kabul senaryoları (K12 pilotu dahil) tekrar tekrar koşulur ve pass^k raporlanır. Olay kaydına hata sahibi ve hata türü alanı eklenir.

### 7.5 Değerlendirme titizliği
- **AI Agents That Matter (Kapoor vd., 2407.01502, Temmuz 2024) [AÖ]:** Değerlendirme maliyetle birlikte yapılmalı. HumanEval'de basit tabanlar karmaşık SOTA ajanları daha ucuza geçiyor. Doğruluk ve maliyet için Pareto eğrisi; ayrılmış set.
- **HAL (Kapoor vd., 2510.11977, Ekim 2025) [AÖ]:** 9 model, 9 kıyas, 21.730 koşu [AÖ-y], yaklaşık $40.000. Koşuların çoğunda daha yüksek akıl yürütme çabası doğruluğu düşürdü.
- **2608.13867 (Ağustos 2026, çok sesli derleme) [AÖ]:** "Many apparent model failures originate elsewhere in the system"; bir katmandaki iyileşme uçtan uca sonuca çoğu zaman geçmiyor.
- **DevOS: Al.** DevOS'un kendi değerlendirmesi dört şeyi birlikte raporlar: pass^k, maliyet ve süre, taban (boş ajan ve tek ajan), ayrılmış senaryolar.

---

## 8. Güvenlik: talimat enjeksiyonu ve yetki (K08)
- **Tasarım kalıpları (2506.08837, Haziran 2025) [AÖ].**
  - Altı kalıp:
    - action-selector [AÖ-y];
    - plan-then-execute: enjeksiyon plan dışı araç çağıramaz;
    - LLM map-reduce: dış veriye yalıtılmış alt ajanlar dokunur;
    - dual LLM;
    - code-then-execute [AÖ-y];
    - context-minimization [AÖ-y].
  - Ajanın keyfi görev çözmesi kısıtlanır; fayda ile güvenlik takas edilir.
- **CaMeL (Debenedetti vd., 2503.18813, Mart 2025) [KOD README + AÖ].**
  - Güvenilir sorgudan denetim ve veri akışı çıkarılır; güvenilmeyen veri program akışını değiştiremez.
  - Yetenekler (capabilities) ve politikalar veri sızmasını engeller.
  - AgentDojo'da görevlerin %77'si kanıtlanabilir güvenlikle çözülüyor [AÖ-y]; korumasız sistem %84 [AÖ].
  - README: "might not be fully secure".
- **DevOS: Uyarlayarak al.** [ÇIK]
  - Okuma alt ajanları karantinalı okuyucudur: yalnız kendi not dosyasını yazar, kural ve bellek yazamaz. O-okuma turunun kendisi bu kalıba uyuyor.
  - Orkestratör işin planını dış içeriği okumadan önce sabitler. Dış içerik bulgu ekler, planı ve kuralı değiştiremez.
  - Talimat biçimli dış metin veri olarak işaretlenir.
  - Bellek zehirlenmesi önlemleri §2.10'dadır.

---

## 9. DevOS için sentez: kanıta dayalı somut yapı önerisi [ÇIK]
Aşağıdaki öneriler yukarıdaki kanıtlardan türettiğim yapılardır; kaynaklarda hazır bulunmazlar. Örneklerin üstüne kurulmuştur (O-16).

- **9.1 İş defteri** (iş kalemi başına tek dosya; Magentic-One + MetaGPT + O9):
  - Olgular dört başlıkta: `Verilmiş/Doğrulanmış` (kaynak yolu ya da commit ile), `Bakılacak`, `Türetilecek`, `Tahmin`.
  - `Plan`.
  - `İlerleme` her turda: bitti mi / döngüde mi / ilerliyor mu / sıradaki / talimat.
  - `durma_sayacı` (eşik 3) → "kök neden + yeni plan".
  - `Belirsiz kalanlar`.
  - `Yol talepleri` (tek yazıcı).
  - `Kabul kontrolü` (dosya yolu ve hash).
- **9.2 Doğrulama hattı:**
  1. Sınayıcı alt ajan kabul kontrolünü uygulamayı görmeden yazar ve commit'ler.
  2. Uygulayıcı yazar. Korunan yollara yazma PreToolUse ile reddedilir; teslimde `git diff --name-only` denetlenir.
  3. Çelişki varsa uygulayıcı "ÇELİŞKİ" kaydı açıp durur.
  4. Doğrulayıcı taze bağlamda, mümkünse farklı modelle koşar. Kanıt: komut, çıkış kodu, çıktı dosyası, commit SHA.
  5. Anlatı iddiası kanıt yerine geçmez.
  6. Kontrol setinde boş ajan tabanı, oracle ve kasıtlı ihlal senaryosu bulunur (ABC; Batu 6).
- **9.3 Ders defteri** (ACE + ExpeL + ReasoningBank):
  - Satır biçimi: `[D-0012] yararlı=2 zararlı=0 kaynak=<olay|commit> durum=aday|geçerli|emekli :: <tek cümlelik, genel ders>`.
  - Yansıtıcı alt ajan, doğrulayıcı sonucundan en çok 3 aday çıkarır; başarı da, başarısızlık da kaynak olabilir.
  - Küratör betiği yalnız ekler, tekilleştirir, sayacı doğrulayıcının etiketiyle günceller. Sayaç ≤0 olan madde emekliye ayrılır; liste doluysa önce emekliye ayırma yapılır.
  - Oturuma en çok 20 "geçerli" madde yüklenir.
  - Ders kural olamaz; kurala terfi 9.5'e göre yapılır.
  - Dış kaynaklı ders en çok "aday" olabilir.
- **9.4 Bağlam:**
  - Kısa CLAUDE.md: zorunlu kurallar ve başlangıç yolu.
  - Ayrıntı skill ve belgelerde; skill ölçülerek kabul edilir.
  - SessionStart hook: STATE, açık defterler ve bayat belge uyarısı (Codified Context).
  - Büyük çıktı dosyaya yazılır.
  - Sıkıştırmadan sonra kanonik dosyalar yeniden okunur (O7 ve O8 ile aynı).
- **9.5 Kural değişikliği protokolü** (DGM + SICA + AHE + Ouroboros + 2607.12227):
  - Değişiklik defterinde sütunlar: değişiklik, hipotez, beklenen ölçüt ve yön, senaryo seti sürümü, taban, pass^k sonucu (sonraki tur), karar (tut ya da geri al), diff hash'i.
  - Senaryo seti ve değerlendirme betiği korunan yoldadır. Değişikliği öneren iş bunları aynı değişiklikte değiştiremez (K07).
  - Ayrılmış senaryolar öneri üretiminde kullanılmaz.
  - İnceleyici ayrıdır. İncelenen diff'in hash'i ile birleşen diff'in hash'i aynı olmalı.
- **9.6 Olay kaydı:**
  - Alanlar: MAST kodu, hata sahibi (kullanıcı, ajan, ortam) ve türü (τ-bench), sessiz hata sınıfı A–E, ham kanıt yolları, kök neden, ders adayı.
  - Hata atama olaylar biriktikçe istatistikle yapılır (Who&When).
- **9.7 Güvenlik:** Karantinalı okuyucu; bellek ve kural yazma yetkisi rol bazlı; dış içerik yetkisiz (§8, §2.10).

---

## 10. Dersler: ne yanlış gitti, kök neden, önlem
| Olay (kaynak) | Kök neden | DevOS önlemi |
|---|---|---|
| ACE'deki çöküş: 18.282 → 122 token, doğruluk tabanın altında (2510.04618 [AÖ-y]); DC her adımda baştan yazıyor [KOD] | Belleği LLM'e baştan yazdırmak | Yalnız ekleme ve deterministik birleştirme (§2.7) |
| DGM halüsinasyon işaretçisini sildi (2505.22954 [AÖ]) | Ölçüt ajanın erişiminde | Değerlendirici ve işaretçiler korunan yolda (§6.3) |
| Reflexion MBPP'de kendi testleriyle tabanın altına düştü [AÖ] | Kendi ürettiği test %16,3 yanlış pozitif | Bağımsız sınayıcı (§1.3) |
| ChatDev "doğrulanmış" dediği kodun derlenmemesi [KOD, MAST] | İnceleme çalıştırmaya değil kontrol listesine dayalı | Çalıştırılan kontrol ve ham kanıt (§1, §4.4) |
| Modellerin testi değiştirip geçmesi (ImpossibleBench [AÖ]) | Test yazılabilir, çelişkiye kaçış yolu yok | Salt okunur test + ÇELİŞKİ kaydı (§1.5) |
| ADAS manşetinde tekrar gürültüsü ve hatalı güven aralığı (gözledim) | Tek koşu, test üzerinden seçim, test edilmemiş değerlendirme kodu | Tekrarlı koşu, doğrulama ile seçim, değerlendirme kodu testi (§6.1) |
| Harness evriminin eşit tabanda avantajı kaybolur (2607.12227 [AÖ]) | Arama ve değerlendirme aynı sette; bütçe eşit değil | Ayrılmış set ve eşit bütçeli taban (§6.7) |
| Generative Agents makale parametresi ≠ kod parametresi [KOD] | Yayın ile kod ayrışması | Mekanizmayı koddan doğrula; sürüm yaz |
| MemGPT'nin DMR başarısı kolay bir ölçütte (Zep'in iddiası [AÖ]) | Ölçüt gerçek kullanımı yansıtmıyor | Zor ve güncel senaryolarla ölç |
| LoCoMo'da sürümlere göre farklı veri tanımı [TM + AÖ] | Makale sürümleri değişmiş | Atıfta sürüm ya da commit yaz |
| %1,2 zehirli kayıtla doğruluk 0,85 → 0,30 (2608.21230 [AÖ]) | Bellek dayanaksız önermeyi kabul ediyor | Kaynak zorunlu; dış içerik yetkisiz (§2.10) |
| Sessiz hataların ~%70'ini insan buldu (2606.14589 [AÖ]) | Hata sinyali yutuluyor ya da anlatıya çevriliyor | Ham çıkış kodu kaydı; kullanıcı gözüyle denetim (§5.5) |
| Vending-Bench'teki "meltdown" döngüleri [AÖ] | Uzun ufukta durum takibi kaybı | Durma sayacı, taze bağlam, dış durum denetimi (§4.5, §7) |
| Uzun kayıtta hata atama kötüleşiyor (Who&When [TM]) | Bağlam uzunluğu | Kısa ve adımlı kayıt; istatistiksel atama (§5.2) |

## 11. Kanıt haritası ve kararlar
| Mekanizma | Kanıt türü | DevOS |
|---|---|---|
| Ayrı eleştirmen ya da doğrulayıcı (Voyager, AgentCoder) | Kıyas + ablasyon [AÖ] | Al |
| Dış sinyalsiz öz-düzeltme | Kontrollü deney, olumsuz [AÖ] | Alma (doğrulama diye) |
| Salt okunur test + kaçış kapısı (ImpossibleBench) | Kontrollü deney [AÖ] | Al |
| Delta bellek ve sayaç (ACE, ExpeL) | Kıyas + ablasyon [AÖ]; kod [KOD] | Al |
| Başarısızlıktan ders (ReasoningBank) | Kıyas [AÖ] | Al |
| İş akışı çıkarma (AWM) | Kıyas [AÖ] | Uyarla |
| LLM'in eski notu yeniden yazması (A-MEM) | Kıyas [AÖ] | Alma (yetkili kayıtta) |
| Kısa bağlam dosyası | 4 çalışma, karışık sonuç [AÖ] | Uyarla (ölçerek) |
| Seçilmiş skill / kendi ürettiği skill | Kontrollü [AÖ] | Seçilmiş: al; kendi üretimi: alma |
| Gözlem maskeleme | Kontrollü [KOD+AÖ] | Al |
| Bayat belge hook'u | Gözlemsel, tek vaka [KOD] | Uyarla |
| Orkestratör + ledger + durma sayacı | Ablasyon %31 [AÖ-y]; kod [KOD] | Al |
| Çok ajan yalnız paralel ve bağımsız işte | Kontrollü, 180 düzen [AÖ] | Al |
| Şirket rol-oyunu (ChatDev) | Kıyas; MAST karşı kanıtı | Alma |
| Tartışma döngüsü | Kontrollü [AÖ] | Alma |
| MAST olay kodları | Ampirik taksonomi, κ=0,88 [KOD+AÖ] | Al |
| Tek olayda LLM ile hata atama | Kontrollü, %14,2 adım [TM] | Alma |
| Yazma öncesi kabul (Claim Plane) | Onaylayıcı deney [AÖ] | Al |
| Açık uçlu öz-değişiklik (DGM, Gödel) | Kıyas; amaç hilesi raporlu [AÖ] | Deney dalında uyarla; canlıda alma |
| Değişiklik defteri + öngörü doğrulaması (SICA, AHE) | Kıyas [AÖ]; kod [KOD] | Al |
| Yönetişim korumaları (Ouroboros) | Yapanların raporu [AÖ] | Uyarla |
| pass^k + maliyet + taban | Ölçüm yöntemi [KOD+AÖ] | Al |
| Karantinalı okuyucu, plan-then-execute (CaMeL) | Kanıtlanabilir güvenlik + kıyas [AÖ] | Uyarla |
| CoALA bellek sözlüğü | Kavramsal | Uyarla (sözlük) |

## 12. Bilinmeyenler ve açık sorular
- §0.4'teki makalelerin tam metinleri okunmadan [AÖ] sayıları kesin değildir. Özellikle MAST'ın son sürüm payları, ImpossibleBench'in Claude'a özgü oranları ve 2512.08296'nın kodlama işine geçerliliği.
- Claude Code'da doğrulayıcı alt ajanın farklı model kullanıp kullanamayacağı, PreCompact benzeri olay ve PreToolUse ile korunan yol uygulaması O11'in alanı [BİLİNMİYOR bu notta].
- Bağlam dosyası çalışmalarının çoğu SWE-bench türü tek-issue işlerde. DevOS'un uzun soluklu, çok oturumlu ve kurala dayalı işine etkisi ölçülmemiş [BİLİNMİYOR]. DevOS kendi sondalarıyla ölçmeli.
- 2026 bulgularının çoğu tek çalışmadır; bağımsız tekrarları yok: 2606.14589, 2607.27250, 2608.21230, 2608.08311.
