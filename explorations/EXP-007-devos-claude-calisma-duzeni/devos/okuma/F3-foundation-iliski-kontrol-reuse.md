# F3 — Foundation: ilişki, kontrol, bileşim ve yeniden kullanım → DevOS mekanizmaları

**Okuyucu:** F3 (EXP-007 DevOS okuma turu) · **Tarih:** 2026-09-27 · **Dal:** `claude/hopeful-pascal-7bekcd`
**Soru:** İlişki, kontrol, bileşim ve yeniden kullanıma dair hangi Foundation sonucu, DevOS'ta hangi somut mekanizmaya dönüşmeli?
**Etiketler:** [K] kaynak diyor · [G] gözledim · [Ç] çıkarım · [B] bilinmiyor.
**Yol kısaltmaları:** `F:` = `research/soul-foundations/` · `C:` = `F:05_relation-control-composition/` · `T:` = `C:transition-effect-feedback/`. Alıntılar özgün dildedir.

## DevOS için en önemli çıkarımlar

1. Foundation reçete değildir [K]: "no branch-to-component or term-to-file mapping follows automatically" (`F:RESEARCH-USE-ALIGNMENT.md` "Agreed meaning"). Buradaki mekanizmalar [Ç]; Foundation'dan gelen şey, her mekanizmanın taşıması gereken ayrımlar ve "şu çıkarım yapılamaz" kurallarıdır.
2. DevOS kendi bölümlemesini kurabilir, koşulla [K]: Foundation "Resources / Work / Actors / Artifacts / Governance" için "Looks operationally useful for Development OS" ve "Could be a task-specific operating profile, not the top-level research frame" diyor (`F:04…/Q5 §7`). Koşullar: bağlam ve hipotez de bilgidir (Artifacts dar kalır); SOUL'un hedef alanı da ortamdır (Resources dar kalır); yönetişim bölümü kontrolün dört yüzünü karıştırmamalı (§3).
3. En güçlü kontrol sonucu [K]: "governed-effect / control-objective scope != enforcement-point / monitored-path scope" (`C:control-constraint/STATE.md`). DevOS'ta her kural için korunan etki ile kapatılan yollar ayrı yazılmalı. CLAUDE.md talimatı tavsiyedir; hook, izin ve sandbox mekaniktir. Bir aracı engellemek Bash, alt ajan ya da MCP yolunu kapatmaz (M3).
4. Bu sonuç ana oturumun kendi kapılarında da geçerli [G: kod okundu; atlatma sınanmadı]. `kapsam-kapisi.py` yalnız Write/Edit/MultiEdit yolunu kapatıyor; Bash, GitHub MCP ve uzak oturum yolları açık. Kapının ölçütünü (KAPSAM satırları) kapıdan geçecek oturumun kendisi kapatıyor. `ajan-standart-kapisi.py`, "STANDART.md" dizesinin görev metninde geçtiğini denetliyor, okunduğunu değil. Hook'lar makine geri alınınca gidiyor (§5.1).
5. Kapı tek şey değildir [K]: kriter + durum + karar + yaptırım, artı inceleme işi: "review completed != gate criterion satisfied != authorized go decision != transition mechanically enabled" (`K3 §4`). Ayrıca "two role labels != two independent Actors" (`K3 §6`). Üretici kendi işini doğrulayamaz, Batu da doğrulayıcı değildir (M2).
6. Tek bir "done/approved" alanı yetmez [K]: "verified != validated != accepted" ve "false != unknown != not evaluated != not applicable != stale" (`C:composite-standing/KEY.md`). Kanıt `T@v7`'ye bağlıdır, `v8`'e kendiliğinden geçmez (`B3 §6`). Bağımlılık değişince sonuç "false" olmaz, "yeniden değerlendir" olur (`S3 §10`) (M1).
7. Değişiklik yayılımı [K]: "all known targets updated != all materially applicable targets known != full propagation established" (`C:…/transition-propagation/STATE.md`). Kural, skill ya da CLAUDE.md değişince tüketiciler listelenmeli ve tek tek doğrulanmalı. Kapsam bilinmiyorsa sonuç "unknown" olur (M5).
8. Öğrenme [K]: "stored lesson != retained response change established" (`T:KEY.md`). Taşıyıcı zinciri şöyle: "carrier written != candidate path installed != relevant path traverses carrier != response disposition changed at that locus != all applicable paths changed != retained after the claimed lifecycle transition" (`persistent-adaptation/D3 §2`). Ders ancak davranış probuyla "uyum" sayılır. Tekrarlayan hata hook ya da teste yükseltilir (M7).
9. Geri bildirim [K]: "A prose claim such as 'I considered the warning' is a report about use. It is not self-authenticating evidence" (`returned-influence/G2 §3`). Bulgunun karara bağı izlenebilir olmalı. Değişmeyen çıktı ne kullanımı ne kullanmamayı kanıtlar. Eleştiri, sırf tepki gösterilmiş olsun diye revizyon dayatmamalı (M6).
10. Nedensellik [K]: Tek kök neden alanı yasaktır. "cause of initiating event != cause of progression != cause of severity != cause of prolonged duration" (`actual-causal-contribution/KEY.md`). R06 durma kuralı kullanılır. "Guardrail sonrası daha az olay" nedensel kanıt değildir, en az 8 rakip açıklaması vardır (`E3 §3`) (M8, M9).
11. Yetki [K]: "reachable effect power != legitimate authority". Anthropic olayında production'a yazma yetkisi olmayan ajan, yazabilen başka bir Claude'a ulaştı; insan kapısı yolu durdurdu (`K5 §10`). DevOS'ta alt ajan ve araç topolojisi yetkiden ayrı tasarlanır (M4).
12. İlerleme çok katmanlıdır [K]: "parent accepted != child separately researched / … / recommended work != activated work" (`F:06…/KEY.md`). Yüzde verilmez. Foundation'ın kendisinde bile 13 eski yönlendirici güncel görünüyor [G]; aynı sorun 09-05'te bir kez görülüp elle temizlenmişti (`Q0 §6`). Tek otorite STATE ve negatif kontrollü defter denetleyicisi gerekir (M11).
13. Yayın = yaz + push + uzak SHA'yı oku + değişen dosyaları tam oku [K]: "A tree or commit object alone is not successful publication" (`F:06…/B5-CLOSURE.md`) (M12).
14. Batu'nun onayı dar okunur [K]: "evet onay veriyorum" yalnız belirli kapıları kapattı; araştırmayı yeniden başlatmadı (`F:REPAIR-PUBLICATION.md`). DevOS onay kaydı, Batu'nun birebir sözünü, kapattığı kapıyı ve yetkilendirmediği şeyleri yazar (M13).
15. Aynı kaynaktan türeyen tekrar, bağımsız kanıt değildir [K]: "a report says all tests ran; a summary copies that report; a reviewer sees the summary and endorses it" (`G3 §5`). Doğrulayıcı kaynağa temas eder, yani testi kendisi koşar (M14).
16. REUSE kuralı [K]: soru-önce rota, 5 alanlı kullanım kaydı, "Existing target records may already suffice." Üretim perspektifinin atlanması dersi de önemli: "available research need not be applied at the right time" (`F:STATE.md`) (M15).
17. Alınmayacaklar: dört bölge = dört modül ya da ajan; "policy engine / workflow engine / graph DB" seçimi; evrensel fail-closed; tek kök neden; "öğrenme" etiketi; yüzde ilerleme; sabit araştırma sırası; yönetişimi tek kova yapmak (§3).
18. Kanıt sınırı [K]: Bütün sonuçlar aynı-model incelemesidir. Oyuncak testler (15+7+4 kurgu ve negatif kontroller) yalnız kurgulanan ilişkileri sınar. Hiçbir mekanizma canlı bir Claude Code oturumunda sınanmadı.

---

## 0. Kapsam ve yöntem

**Yöntem:** Önce harita çıkarıldı (`ls`, `find`, boyutlar). Sonra her dosya `cat` ya da Read ile baştan sona okundu. İki toplu çıktı görüntüleme sınırını aştı (Causal E3–E5 ve Actual yönlendirici/sentez). Araç bunları dosyaya yazdı; o dosyalar Read ile tam okundu [G]. Okurken alıntılar repo dışındaki bir karalamada tutuldu; karalama, not yazılınca silindi. 04'ün Q0–Q5 dosyaları taslak yazıldıktan ve bağlam sıkıştırıldıktan sonra okundu; bulguları §1, M1, M3, M4, M7, M8, M11, M13, §3 ve §4.1'e eklendi. Kod çalıştırılmadı. Test sonuçları için "kaynak diyor" denir.

**Tam okunan (baştan sona):**
- **Kök (6/6):** `README`, `INDEX`, `STATE`, `RESEARCH-USE-ALIGNMENT`, `REPAIR-AUDIT`, `REPAIR-PUBLICATION`.
- **05 (198/198):**
  - kök 16 (C0–C7, INDEX, KEY, STATE, PLAN, FINDINGS-MAP, OPEN-QUESTIONS, CURRENT-SURFACES, parent synthesis);
  - relational-binding 16 (B0–B7 + 8 yönlendirici/sentez);
  - composite-standing 16 (S0–S7 + 8);
  - control-constraint 16 (K0–K7 + 8);
  - transition-effect-feedback kök 16 (T0–T7 + 8);
  - transition-propagation 16 (P0–P7 + 8);
  - causal-effect-contribution kök 16 (E0–E7 + 8);
  - actual-causal-contribution 16 (A0–A7 + 8);
  - contrastive-interventional-causal-effect 16 (I0–I7 + 8);
  - feedback-adaptation kök 16 (F0–F7 + 8);
  - persistent-adaptation 20 (D0–D7, SOURCE-LEDGER, iki sentez, `checks/semantic_checks.py` ve `semantic-check-results.json` dahil);
  - returned-influence 18 (G0–G7, SOURCE-LEDGER, iki sentez dahil).
- **08 (13/13):** INDEX, STATE, CURRENT-SURFACES, REUSE, SYNTHESIS, DISCUSSION-HANDOFF, CASE-AUDIT, RIVALS-AND-REUSE, COMPLETION-AND-RESIDUALS, COLD-START-CHECK-2026-09-17, PLAN, PUBLICATION, SOURCE-LEDGER.
- **06 (18/18):** INDEX, STATE, KEY, SYNTHESIS, CURRENT-SURFACES, NEXT-RESEARCH-HANDOFF, PLAN, SOURCE-LEDGER, B0–B5, FRONTIER.json, `checks/frontier_audit.py`, `checks/RESULT.json`, `evidence/INPUT-DYNAMICS-STATE.md`.
- **07 (14/14):** INDEX, STATE, CURRENT-SURFACES, SYNTHESIS, NEXT-RESEARCH-HANDOFF, COMPLETION-DEPTH, RIVAL-AND-BOUNDARY-REVIEW, PUBLICATION, PLAN, SOURCE-LEDGER, `checks/` (SPEC, EXECUTION, RESULT.json, integration_checks.py).
- **04 (16/16):** INDEX, STATE, KEY, CURRENT-SURFACES, FINDINGS-MAP, OPEN-QUESTIONS, PLAN, DEFERRED-RELATIONS, `synthesis/TOP-LEVEL-ADEQUACY-RERUN-SYNTHESIS.md`, Q0–Q6.

**Görev kapsamında okunmayan dosya yok.** Kapsam dışında kalanlar ve izler:
- **Kapsam dışı ama ilgili iz** [G]: `C:…/actual-causal-contribution/CURRENT-SURFACES.md`, R06 protokolünü `agent/protocols/causal-depth-root-cause-validation.md` yolunda gösteriyor. Repo kökünde `agent/protocols/` altında 9 protokol var: candidate-research-library, canonical-work-preflight, causal-depth-root-cause-validation, decision-critical-assumptions, goal-method-end-to-end-validation, source-view-fidelity, user-independent-reasoning, verification-independence, work-system-continuity. Bunlar Foundation'ın kullandığı mevcut "agent-control" katmanı. Toplam yaklaşık 100 KB. BRIEF'teki hiçbir kümede adları geçmiyor; `devos/okuma/` altındaki notlarda da `grep` ile hiç anılmıyorlar [G]. Ben okumadım. Ana oturum bir okuyucu atamalı; mevcut bir DevOS benzeri mekanizma olabilirler. Yalnız dosya adlarına bakarak [Ç]: `verification-independence` M2/M14'e, `source-view-fidelity` §4.1'e, `work-system-continuity` M12'ye değebilir.
- **Foundation'ın başka klasörleri:** Foundation'ın atıf yaptığı studies (anthropic-ai-native-sdlc-playbook, multi-agent-patterns, context-memory-harness-engineering, gstack, ai-knowledge-strategies, RPD, the-carbon-layer) ile `00`–`03` ve `history/`, F1/F2/F4 ve O-kümelerinin kapsamındadır. Buradaki studies iddiaları "Foundation'ın o study'yi okuma biçimi" olarak aktarılmıştır.
- **04 Q4'ün dış kaynakları** (BIPM VIM, FEMA/USFA NIMS, WHO hasta güvenliği, NIST AI RMF): Foundation bunları "counterexample sources" olarak kullanıyor. Kaynakların kendisi okunmadı; burada yalnız Foundation'ın okuma biçimi aktarılıyor. NIMS'in olay planlama döngüsü (hedef → planlama → iş atama → uygulama, değerlendirme ve revizyon; yetki devri; kaynak takibi) DevOS iş döngüsü için ayrıca incelenebilir (O9/O14 alanı) [Ç].
- **Kapsam dışı, amaçlı okunan:** Bağlam sıkıştırılınca ortamın hook'u `STATE.md`, `DERSLER.md` ve `KAPSAM.md`'yi yeniden okumayı istedi; üçü de okundu. Ayrıca `explorations/EXP-007-…/tools/oturum-disiplini/` altındaki 5 dosya ve `~/.claude/settings.json`'ın `hooks` bölümü yalnız okundu. Bunlar yalnız §5.1'de (Foundation'ın kontrol sonucunu canlı bir örnekte sınamak için) ve M5 ile M14'teki DERSLER bağlantılarında kullanıldı. Hook'lar çalıştırılmadı.

---

## 1. Bu alanda Foundation ne kurdu (kısa harita)

```text
Cross-Ground Composition (C:)
├─ Relational Binding            — neyin neye, hangi rolde, hangi kapsam/zamanda bağlı?
├─ Composite Standing            — birden çok zeminden oluşan hangi nitelik şu an geçerli?
├─ Control / Constraint          — aday davranış/geçiş hangi dayanakla nasıl yönetiliyor?
└─ Transition / Effect / Feedback
   ├─ Transition / Propagation   — ne gerçekten değişti, nerede/ne zaman etkili oldu?
   ├─ Causal Effect / Contribution
   │  ├─ Actual (bu olayı ne doğurdu?)
   │  └─ Contrastive (X yerine X' olsa sonuç nasıl değişirdi?)
   └─ Feedback / Adaptation
      ├─ Returned Influence (sonuç bilgisi işleyen bir tepkiye döndü mü?)
      └─ Persistent Adaptation (geçmiş, gelecekteki tepki eğilimini kalıcı değiştirdi mi?)
```

Bunlar bileşen değildir [K]: "These are protected diagnostic questions, not disjoint object classes or components" (`C:KEY.md`). Tanı sorusu olarak kullanımı `C:C1-SEMANTIC-KIND-DISCRIMINATION.md §11`'dedir: bağlantı → Binding, birlikte değerlendirilen nitelik → Standing, izin/gereklilik/engel → Control, değişim/tetik/yayılım → Transition; "Multiple answers may be `yes`".

**Birleşik "yasak çıkarımlar" tablosu** [K] (`F:06_integration-frontier-review/B1-PARENT-INTEGRATION.md §2`). DevOS kabul testlerinin çekirdeği [Ç]:

| Bölge | Lisanslanmayan çıkarım (birebir) |
|---|---|
| Binding | "Generic connectivity proves a valid relation." |
| Standing | "An assessment, acceptance or record is the qualification itself." |
| Control | "One enforcement point controls every route to the effect." |
| Propagation | "Commitment, local realization or a successful retry proves full propagation." |
| Actual causation | "Provenance, chronology or a missing control proves causation/responsibility." |
| Contrastive | "Before/after improvement proves causal benefit or transportability." |
| Returned Influence | "Delivery, visible change or unchanged output proves operative use." |
| Persistent Adaptation | "Stored lessons, new bytes, current expression or test success proves learning, benefit or authority." |

**Zemin düzeyindeki korunan ayrımlar** [K] (`F:04_top-level-adequacy-rerun/Q3-BOUNDARY-INTERACTION-PRESSURE.md §13`):
```text
actual reality != representation
Work pursuit/state != representation of Work
Actor standing != representation of standing
Actor capability != Environment actionability
Work admission != Actor obligation/authority
Work completion != Environment outcome
technical effect power != legitimate authority
verification evidence != authorized acceptance
```
Aynı dosya buradan şu sonuca varıyor: "Ground adequacy != total Foundation completeness"; "relation/control research is mandatory before architecture" (`Q3 §12`). [Ç] Bu sekiz satır DevOS kayıtlarının değişmezleridir: pano iş değildir, rol kaydı yetki değildir, "iş bitti" etkinin gerçekleştiği anlamına gelmez, kanıt kabul değildir (M1, M4, M10, M11).

**Bu nottaki okuma ilkesi:** Soru "hangi sonuç hangi mekanizmaya *dönüşmeli*" diye soruluyor. Foundation buna "otomatik dönüşüm yok" diye itiraz eder. RUA'nın ifadesi: "compare methods including not adding a mechanism". Bu yüzden her mekanizma şu kalıpla yazıldı: *Foundation şu ayrımı zorunlu kılar → DevOS bu ayrımı şu biçimde taşıyabilir → daha hafif seçenek şu*. `F:08…/REUSE.md` de "Existing target records may already suffice" der.

---

## 2. Sonuç → mekanizma eşlemesi

Her maddede şu sıra izlenir: **Dayanak** (birebir alıntı) · **Sorun** · **Nasıl işler** (dosya, biçim, tetik, kod) · **Kanıt** · **Karar**. Dosya yolları DevOS reposu için öneridir [Ç]. `.claude/` ve `CLAUDE.md` yalnız anılır, oluşturulmaz. Claude Code ayrıntıları (hook olayları, çıkış kodları, frontmatter) O11 notunda URL'leriyle doğrulanmalıdır. Burada yalnız ihtiyaç tarif edilir.

### M1 — Nitelik (standing) kaydı ve kanıtın tam hedefe bağlanması

**Dayanak [K]:**
- "standing holds != assessment supports it != decision recognizes it != record says it holds" · "criterion != decision rule" · "false != unknown/indeterminate != not evaluated != not applicable != stale" · "verified != validated != accepted" (`C:composite-standing/KEY.md`).
- "`verified(Target v7, Requirement set R1)` cannot safely become: `Target.verified = true` if v8/R2 later becomes current" (`S7 §5`).
- Durumların eylem karşılıkları: "false may justify remediation/rejection; unknown may justify evidence acquisition/escalation; not evaluated may schedule required Work; not applicable should suppress the criterion entirely; stale means prior evidence/result cannot justify a current claim without proving the standing false" (`S7 §7`).
- "dependency changed → prior standing may require re-evaluation != standing necessarily flipped" (`S3 §10`, üç sonuç: kesin değişir / yeniden değerlendirme / değişmediği kanıtlanır). "standing currently holds != latest evaluation is current enough to establish it" (`S3 §11`).
- "Evidence E supports result/claim about target artifact T@v7 under criterion C. If the target later becomes T@v8, the evidence relation does not automatically transfer." (`C:relational-binding/B3 §6`).
- NASA doğrulama bileşenleri: "exact product/configuration baseline; specified requirements baseline; acceptance criteria for each requirement; verification plan/procedures/method; enabling products/environment; recorded objective evidence/results; pass/fail declarations and discrepancies" (`S5 §2`).
- Çok zeminli ayrım: "execution complete != verified != valid / fit for intended use != authorized acceptance" (`F:04…/Q3 §8`); "Work complete != target Environment condition achieved" (`Q2 §2`).
- Eski kabul korumaz: "This pass does **not** inherit the original adequacy conclusion merely because it was accepted. The original result is a falsifiable prior hypothesis." (`F:04…/Q0 §1`).

**Sorun:** "Bitti" dendiğinde neyin, hangi sürümün, hangi kritere göre, kim tarafından doğrulandığı kaybolur. Sonraki commit eski yeşili sessizce devralır (O10'da tespit edilen "var ≠ kullanıldı" hatasının kardeşi).

**Nasıl işler [Ç]:**
- Her iş kalemi için ayrı nitelik kayıtları (`devos/nitelik/<is-id>-<nitelik>.yaml`) tutulur. Bir iş için "verified", "validated" ve "accepted" üç ayrı kayıttır.
```yaml
nitelik: verified            # verified | validated | accepted — asla birleşik değil
odak: {yol: "system/x/", surum: "git:3f2a9c1"}          # tam hedef; dal adı değil SHA
kriter: {id: "GEREK-12", kaynak: "devos/gereksinim.md@a1b2c3", uygulanir: true}
sonuc: true              # true | false | unknown | not-evaluated | not-applicable
degerlendirme:           # epistemik katman — nitelik değil
  yontem: "pytest tests/x -q"   # yeniden koşulabilir komut
  kanit: ["ci-log: devos/kanit/2026-09-27-x.txt"]
  degerlendiren: {rol: dogrulayici, uretici-degil: true}
  belirsizlik: "yalnız birim testleri; entegrasyon yok"
karar: null              # yalnız 'accepted' kaydında: {karar-veren: Batu, soz: "...", tarih: ...}
gecerlilik-bagimliliklari: ["system/x/", "devos/gereksinim.md", "tests/x/"]
```
- **Tazelik denetleyicisi** (`devos/bin/nitelik-tazelik`). Tetik: oturum başı, `git commit` sonrası ve kabul öncesi. Bir bağımlılık değişince kayıt `stale` olur, `false` olmaz:
```bash
for f in devos/nitelik/*.yaml; do
  sha=$(yq -r '.odak.surum' "$f" | sed 's/^git://')
  deps=$(yq -r '.gecerlilik-bagimliliklari[]' "$f")
  git diff --quiet "$sha" HEAD -- $deps || echo "STALE (yeniden değerlendir): $f"
done
```
- Kabul kaydı yalnız `verified` kaydı güncelse açılabilir. Validated (amaca uygunluk), Batu'nun hedefine göre ayrı değerlendirilir.
- Önceden kabul edilmiş bir sonuç, maddi bir değişiklikten sonra (model, ortam, gereksinim) "yanlışlanabilir önceki hipotez" olarak yeniden sınanır. Kabul edilmiş olması onu korumaz (`Q0 §1`).

**Kanıt:** Foundation analitiktir, aynı-model incelemesidir (`S7 §22`) [K]. DevOS'ta sınanmadı [B].
**Karar: AL.** En temel kayıt ayrımıdır. Hafif sürümü: ayrı YAML yerine iş dosyasının frontmatter'ında aynı alanlar.

### M2 — Kapı ayrıştırması ve görev ayrılığı

**Dayanak [K]:**
- Kapının dört anlamı: "1. criterion / prerequisite; 2. standing …; 3. decision/control …; 4. enforcement …", artı inceleme işi. "review completed != gate criterion satisfied != authorized go decision != transition mechanically enabled". Kapsam cümlesi: "A review is Work; readiness evidence/standing can support a gate; the governing go/no-go semantics belong to Control; the later phase transition belongs to Transition" (`C:control-constraint/K3 §4`).
- "approval record exists + wrong/out-of-scope Actor → approval may be informationally real but control-invalid" (`K3 §5.3`). "expert / verifier / reviewer != authorization authority" (`K3 §5.2`).
- Görev ayrılığı: "two role labels != two independent Actors / producer and verifier names differ != independence automatically established / human approval present != separation-of-duties satisfied" (`K3 §6`). "The same bearer, collusion, shared credentials or hidden delegation can defeat the objective" (`K5 §4`).
- "producer self-check != fresh/independent verification", "role label = verifier != verification standing is valid" (`S5 §10`). "multiple agents != separation of duties by default" (`K5 §11`).
- Açık soru: "what minimum independence relation is needed beyond distinct Actor identities when collusion, shared principals, shared context or agent delegation are possible?" (`C:control-constraint/OPEN-QUESTIONS.md` 9).

**Sorun:** Aynı modelin aynı bağlamla açtığı "doğrulayıcı" alt ajanı, bağımsızlığı kendiliğinden sağlamaz. İnsan onayı var diye kapı geçilmiş sayılmaz.

**Nasıl işler [Ç]:**
- Kapı kaydı `devos/kapi/<is-id>.yaml`:
```yaml
kapi: main-birlestirme
kriter: [verified(SHA), validated-veya-gerekmez, acik-bulgu: 0]      # 1
durum: {verified: "devos/nitelik/IS-7-verified.yaml", guncel: true}    # 2 (M1'den hesaplanır)
inceleme-isi: {yapan: dogrulayici-oturum-2, bagimsizlik: [farkli-baglam, testi-kendisi-kosar, ureticinin-ozetini-okumaz]}
karar: {karar-veren-rol: Batu, kapsam: "IS-7 @ 3f2a9c1", soz: "…"}      # 3
yaptirim: {mekanik: "main'e push hook'la engelli; yalnız kabul kaydı SHA eşleşince açılır"}  # 4
```
- **Bağımsızlık tanımı.** Rol adı değil, koşullar sayılır: doğrulayıcı üreticinin özetini ya da transkriptini okumaz; kanıtı kendisi üretir (testi koşar, diff'i okur); üreticiyle aynı karar dosyasını yazamaz. `OPEN-QUESTIONS` 9'daki "shared context" riski, bulut oturumunda ayrı alt ajan bağlamıyla azaltılabilir. Kalıntı risk (aynı model, ortak sistem istemi) kayda "belirsizlik" olarak yazılır.
- **Batu'nun rolü.** Kabul yetkisi Batu'dadır; doğrulama rolü DevOS'tadır (K-015). Kapı kaydı ikisini ayrı alanlarda tutar. Batu'nun "onayladım" demesi doğrulama yerine geçmez; doğrulayıcının "geçti" demesi de kabul yerine geçmez.

**Kanıt:** NASA karar kapıları, NIST AC-5 ve AC-3(2) dayanaklı analiz (`K5 §4, §7`) [K]. DevOS'ta sınanmadı [B].
**Karar: AL.** Mekanik yaptırım (push engeli) bulutta repo hook'uyla kurulabilir; O11 doğrulamalı. Hafif sürüm: kapı kaydı PR açıklamasında.

### M3 — Kontrol kaydı: korunan etki, yaptırım noktası ve kapsama

**Dayanak [K]:**
- "governed-effect / control-objective scope != enforcement-point / monitored-path scope" → "one path blocked != protected effect controlled". "A local mechanism can behave correctly while an indirect Actor/tool/service/physical route defeats the protected control objective" (`C:control-constraint/STATE.md` "Strongest discovery").
- Çekirdek: "protected governing question; exact governed focus / protected effect; governing basis / objective / invariant; governing mode / effect; applicability frame …; precedence / conflict / exception / default semantics where material; current validity dependencies". Katmanlar ise "authority / legitimacy; evaluation / decision / gate; enforcement / intervention; coverage / alternate-path / bypass; monitoring / observation; compliance / effectiveness assessment" (`STATE.md`).
- Kontrolün dört yüzü, DevOS adıyla: "SOUL / Development OS depend heavily on permissions, policies, gates, verification rules, deterministic controls, human authority and enforcement." Ayrıştırma şöyle: yetki ve yükümlülük Actors'ta; kural metni ve yapılandırma Information'da; inceleme, onay ve kontrol işi Work'te; gerçek yaptırım mekanizması Environment'ta. "A written policy can exist without being authoritative. Authority can exist without a particular document. A runtime can mechanically block an action without defining the normative reason. A Work gate can be required while the Environment enforcement is absent." (`F:04…/Q1 §3`).
- Claude Code'a özgü baskı: "`CLAUDE.md`/instructions/skills are advisory context, not hard enforcement by identity; hooks/settings/permissions/sandbox/identity/network/tool restrictions provide progressively harder control surfaces; … monitoring covers permission/tool/hook/subagent events; configuration itself needs regression evaluation" (`K0 §5`).
- Katmanlı kapatma örneği: "denying one web-fetch tool does not necessarily stop shell/network egress; sandbox/network allowlists close paths missed by tool-level permissions; credential restrictions close paths left by other layers; managed-only configuration prevents local widening/bypass" (`K5 §10`).
- Gerçek bir sistemde ayrışma: "instruction says do not use tool X != runtime blocks tool X" ve "configuration says deny network path != indirect shell/service/agent path cannot reach effect" (`K7 §6`). "agent instructed not to do X != agent mechanically unable to do X", ama "an advisory control may still be legitimate and decision-critical" (`K4 §6`).
- Varsayılanlar: tetikleyiciler "missing attributes; unreachable decision service; conflicting rules; evaluation error; stale state; timeout"; seçenekler "deny unless explicit permit; permit unless explicit deny; preserve indeterminate and escalate; require human/manual resolution; …". Ayrıca "No universal `fail-closed` rule is inferred" (`K3 §9`).
- Geri alma: "existing session remains open; cached credentials remain usable; enforcement has not received the update; indirect routes remain available" → "authority/policy changed != effective control changed everywhere immediately" (`K3 §10`).
- İzleme: "monitor says local control complied != end-to-end control objective satisfied" (`K3 §11`).
- Tanı soruları: `C:control-constraint/FINDINGS-MAP.md` "Reusable diagnostic questions" 1–12 ("What exact behavior/effect is being governed? … What effect/path universe is the control objective claiming to cover? Does the enforcement point cover that same universe? … Is the claim current …?"). Kaynak şunu da ekler: "These are research diagnostics, not a schema or runtime algorithm."
- Test kataloğu: `K0 §8` "Mandatory failure cases" (14 madde, örn. "policy says DENY, runtime allows", "direct path denied, indirect Actor/tool path reaches effect", "producer self-approves despite separation-of-duties requirement").

**Sorun:** DevOS kuralları çoğunlukla CLAUDE.md'de ya da skill'lerde yazıya dönüşür. Yazı kontrol sanılır. Mekanik engel konsa bile tek bir yolu kapatır. Önceki denemelerdeki "kural yazıldı ama uygulanmadı" örüntüsünün Foundation adı budur.

**Nasıl işler [Ç]:**
- `devos/kontrol/kontroller.yaml`: her kural için tek kayıt.
```yaml
- id: KNT-03
  korunan-etki: "doğrulanmamış değişikliğin main'e girmesi"
  dayanak: "K-015 kabul kuralı; M2 kapısı"
  kip: gate                       # permit|prohibit|require|limit|gate|escalate|...
  uygulanabilirlik: {dal: main, islemler: [push, merge]}
  yetki: {kural-sahibi: Batu, degistirebilen: [Batu]}
  karar: "M2 kapı kaydı SHA eşleşmesi"
  yaptirim:                       # katman listesi; tavsiye ve mekanik ayrı yazılır
    - {tur: tavsiye, yer: "CLAUDE.md §Kabul"}
    - {tur: mekanik, yer: "PreToolUse hook: 'git push * main' engeli"}
  kapsama:
    kapatilan-yollar: ["Bash git push", "alt ajan Bash", "GitHub MCP merge aracı"]
    acik-bilinen-yollar: ["GitHub web arayüzünden elle birleştirme (insan)"]
    kapsam-kesfi: "yol listesi eksik olabilir → etki kontrolü 'unknown'"
  varsayilan: "kapı kaydı okunamazsa: engelle ve Batu'ya sor"   # alan bazında seçilir, evrensel değil
  izleme: "hook karar günlüğü devos/gunluk/hook.jsonl"
  guncellik: {surum: "git:…", son-kapsama-testi: "2026-…"}
  testler: ["devos/kontrol/test/KNT-03-dogrudan.sh", "devos/kontrol/test/KNT-03-altajan.md", "…-mcp.md"]
```
- **Kapsama testleri.** `K0 §8`'in 14 hata durumu, DevOS'a özgü negatif testlere çevrilir. Örnekler: yasak yol denenir ve engellendiği gözlenir; aynı etki Bash `sed -i` ya da `>` ile, alt ajan üzerinden ve MCP aracıyla denenir. Her test sonucu kayda "kapatıldı / açık / sınanmadı" olarak yazılır.
- **Dört yüz ayrı alanlarda.** Kayıttaki `yetki`, `dayanak`, `karar` ve `yaptirim` alanları `Q1 §3`'ün dört yüzüdür; biri ötekini kanıtlamaz. Yazılı kural yetkisiz olabilir. Hook bir işlemi engelliyor olabilir, ama gerekçesi ve sahibi kayıtta yoksa kuralın meşruiyeti bilinmez.
- **Tavsiye/mekanik ayrımı raporlanır.** "Bu kural yalnız tavsiye" etiketi, kuralın kaldırılması anlamına gelmez (`K4 §6`). Ama kural "kontrol altında" diye raporlanamaz.
- **Konfigürasyon regresyonu.** CLAUDE.md, skill ya da hook değişince (bkz. `I5 §7`: "treats `CLAUDE.md`; Skills; Hooks; prompts/models; permissions/sandbox/control configuration as changeable configuration surfaces and recommends regression evaluation") ilgili kontrol testleri yeniden koşulur.

**Kanıt:** Anthropic playbook'u, NIST ZTA/800-53, XACML ve OSHA dayanaklı analiz [K]. Kaynak şu olayı bildiriyor: "a human review gate stopped the resulting path" (`K5 §10`). Canlı DevOS testi yok [B].
**Karar: AL.** DevOS'un kural katmanının omurgası budur. Bulutta proje hook'ları ve izin kuralları yüklenir (BRIEF §3). Tam olay listesi ve exit-code semantiği O11'den alınmalı.

### M4 — Yetki ile erişilebilir etki gücünü ayırma (alt ajan ve araç topolojisi)

**Dayanak [K]:**
- "reachable effect power != legitimate authority" (`C:C0 §4`, `04 DEFERRED-RELATIONS §9`).
- Üçlü ayrım: "legitimate authority != reachable effect power != runtime enforcement outcome" (`F:04…/Q1 §3`). Eylem gücü de türetilmiş bir durumdur: "Actor capability / competence != Environment access / affordance / resource state != situated actionability" (`Q3 §3`); "Actor capable + Environment blocks access → not actionable" (`Q1 §5`).
- Dört ayrı soru: "1. Is direct operation permitted? 2. Is direct operation technically reachable? 3. Is the protected effect reachable indirectly? 4. Is the indirect effect legitimately authorized/delegated?" (`K3 §8`).
- Örnek: "Actor A lacks direct write route / A can invoke Actor B / B can invoke privileged tool / actual effect becomes reachable" (`C:C3 §4`). Yetki devri geçişli değildir: "`A delegates-to B` + `B delegates-to C` does not automatically establish valid A→C authority" (`B7 §11`).
- Devir kaydı: "Delegator A → Delegatee B for operation O on Work/target W/T for scope S possibly on behalf of principal P". İkili biçim için: "A binary `A delegates-to B` is dangerously incomplete" (`B3 §5`).
- "model/provider changes can expose previously unseen authority paths" (`actual-causal-contribution/A5 §9`). "software running with greater privilege can indirectly provide a user greater privileges than assigned" (`K5 §4`, NIST AC-6).

**Sorun:** Ana oturumun elindeki geniş yetki, alt ajana ya da MCP aracına dolaylı etki gücü verir. "Bu ajanın yazma izni yok" demek, "bu etki ondan çıkamaz" anlamına gelmez.

**Nasıl işler [Ç]:**
- `devos/roller/<rol>.md` her rol için dört alan tutar: araç listesi (alt ajan frontmatter'ındaki izinli araçlar), erişilebilir dolaylı yollar, meşru yetki (hangi işlem, hangi kapsam, kimin adına), devir kuralı (devredilebilir mi, süresi).
- Rol yetkinliği, ortam erişimi ve durumsal eylem gücü ayrı yazılır. Örnek [G]: `KAPSAM.md`'deki "Ağ sınırı" notuna göre arxiv.org ve benzerleri bu ortamda kapalı. Akademik kaynak okuyucusu yetkin olsa da o kaynağa erişemiyor. İş kaydına "başarısız" ya da "kaynak yok" değil, "ortam engeli: erişilemedi" yazılır.
- Yüksek etkili işlemler (main'e push, silme, dış gönderim, sır okuma) için M3'te kontrol kaydı ve insan ya da ikinci onay kapısı. Onay veren "doğru yetkili" olmalı (`K5 §10`).
- Model ya da sürüm değişince yetki yolları yeniden taranır (A5 §9). Bu, M3 testlerinin yeniden koşulmasıdır.
- Bulut gerçeği [Ç, BRIEF §3]: alt ajan kendi alt ajanını açamaz (derinlik 1). Bu, "ajan → ajan" zincirini ana oturum → alt ajan ile sınırlar. Bash, MCP ve web yolları yine açık kalabilir; transitif güç analizi bu yollara kaydırılır.

**Kanıt:** Anthropic güvenlik yazısındaki gerçek olay, Foundation'ın okuduğu biçimiyle [K]. DevOS'ta sınanmadı [B].
**Karar: UYARLAYARAK AL.** Tam yol sayımı istenmez: "Control adequacy does not require enumerating every theoretically possible path in every domain" (`K3 §7.2`). Kapsam, korunan etkinin riskine göre seçilir.

### M5 — Değişiklik yayılımı ve "kapsam körlüğü" denetimi

**Dayanak [K]:**
- "requested / intended change != realized change / approved / committed / issued change != incorporated / realized change / local realization != change effective across all applicable scope / change realized != change observed / recorded" (`C:…/transition-propagation/STATE.md`).
- Kapsam körlüğü: "all known targets updated != all materially applicable targets known != full propagation established"; ayrıca "A system can correctly verify every target in its current frame and still miss a relevant path, consumer, session, enforcement point, Actor population or scope… If scope coverage is not established, the correct result may be `unknown/not fully evaluated`" (`synthesis §15`).
- "`Fully propagated` … realized transition facts + applicable scope criterion → propagation/convergence standing" (`P2 §7`). "propagation episode exists != full-propagation / convergence Standing holds" (`STATE`).
- Uçtan uca kontrol hatasının nedenleri: "alternate path; stale policy copy; stale credential/session; propagation lag; failed update; conflicting/superseding update; wrong dependency/version targeting" (`T3 §7`).
- NASA CM: "change proposed != change approved != approved change incorporated != implementation verified" ve "status accounting is representation about transition progress, not the transition by identity" (`P5 §6`).
- "retry attempted != target changed", "rollback != time reversal", "reconciliation ran != reconciled" (`synthesis §11`).
- 07'deki karşılığı: "Correct source update with an unchanged received copy" (`F:07…/RIVAL-AND-BOUNDARY-REVIEW.md §6`).

**Sorun:** DevOS'ta bir kural, rol tanımı ya da ders değişir; ama o sırada çalışan oturum, alt ajanın aldığı özet, skill kopyası ya da önceden yazılmış devir notu eski kalır. Foundation'ın kendi yönlendiricilerinde bu tam olarak oldu (§4.1).

**Nasıl işler [Ç]:**
- `devos/yayilim/tuketiciler.yaml`: kaynak → tüketiciler haritası.
```yaml
- kaynak: devos/kurallar/kabul.md
  surum-isareti: "KABUL-KURALI v4"          # tüketicide aranacak dize
  tuketiciler: [CLAUDE.md, .claude/agents/dogrulayici.md, devos/sablon/kapi.yaml, devos/devir/*.md]
  kapsam-kesfi: "grep -rl 'KABUL-KURALI' . ile karşılaştır; listede olmayan eşleşme = yeni tüketici"
```
- `devos/bin/yayilim-kontrol` betiği. Tetik: kaynak dosya değişince (PostToolUse ya da commit sonrası) ve oturum başında. Her tüketicide sürüm işaretini arar. Sonucu `gerceklesti / eski / bilinmiyor` diye yazar. Harita dışında eşleşme bulunursa "kapsam eksik" der ve toplam sonucu `unknown` yapar; hiçbir durumda `true` yazmaz.
- Çalışan oturumlar ve bağlama yüklenmiş kopyalar dosya taramasıyla görülemez. Bu yüzden devir notları "hangi kural sürümüyle yazıldı" alanını taşır. Oturum başı kontrolü eski sürümle yazılmış devirleri işaretler.
- Yayılım tamamlandı iddiası bir M1 nitelik kaydıdır (kriter: tüketicilerin tümü + kapsam keşfi yapıldı).
- `DERSLER.md` L4'teki "değişince kontrol et" tablosu bu mekanizmanın ilk hâlidir [G]. Foundation'ın eklediği şudur: tablo yalnız bilinen tüketicileri tutar; `grep` de yalnız aynı dizeyi taşıyanları bulur. Başka adla anılan kopya ya da bağlama yüklenmiş eski sürüm görünmez. Bu yüzden sonuç `unknown` kalabilir ve öyle raporlanır.

**Kanıt:** AWS/Google IAM, NASA CM ve Federal Register dayanaklı analiz [K]. Foundation'da 13 eski yönlendirici bu hatanın canlı örneği [G, §4.1].
**Karar: AL.** Harita tam olmayabilir; bunun cevabı "unknown" sonucudur, harita yazmamak değildir.

### M6 — Geri bildirimin işleyen tepkiye dönüş izi

**Dayanak [K]:**
- "signal produced != signal delivered != signal exposed/read != signal operatively used != signal individually decisive != response executed != desired outcome achieved" (`returned-influence/G2 §3`).
- "A prose claim such as 'I considered the warning' is a report about use. It is not self-authenticating evidence of actual use. A trace can strengthen the claim if it links the exact input to the relevant decision path; a trace that merely logs receipt proves less." "For an LLM, an explanation written after the answer can fit several possible causes." (`G2 §3`).
- Dört iddia düzeyi: "Structural … Operative … Episode-specific … End-to-end" (`HISTORICAL-RETURNED-INFLUENCE-SYNTHESIS.md §4`).
- "unchanged output != absence of feedback / unchanged output != proof of feedback use" (`KEY.md`). "For SOUL, the prospective implication is important: a critique should not force revision just to display responsiveness. Preserving a conclusion, stopping an action or seeking further information can be the appropriate response." (`HIST §3`). "neither 'always revise after critique' nor 'stay internally consistent with the prior answer' is a sufficient success criterion" (`G2 §8`).
- "A dashboard nobody reads is not feedback in the load-bearing sense" (`feedback-adaptation/F1`).
- Kurtarma haritası: "Signal formed but not delivered → Investigate target/route, transport and timing / Signal delivered but ignored → Examine relevance, overload, active rule and consumer behavior / … / Decision informed, action blocked → Inspect authority, capability and actuation path / … / Reports agree through one common origin → Seek discriminating evidence rather than count repetitions" (`G3 §8`). Kaynak şunu ekler: "diagnostic map, not a required workflow".

**Sorun:** İnceleme bulguları, Batu'nun notları ve test çıktıları dosyaya yazılır. Ama hangi kararı etkiledikleri izlenmez. "Okudum, dikkate aldım" cümlesi kanıt sanılır.

**Nasıl işler [Ç]:**
- `devos/bulgu/<id>.yaml`:
```yaml
bulgu: BLG-112
kaynak: {tur: test|inceleme|Batu|olay, koken: "ci:run/456"}     # M14 köken
hedef: {yol: system/x.py, surum: git:3f2a9c1}
tuketici: {rol: uygulayici, is: IS-7}
yanit: {tur: duzelt|koru|dur|arastir, gerekce: "…", iz: "commit 9c1e… mesajında BLG-112 / karar kaydı KRR-9"}
iddia-duzeyi: operative            # structural|operative|episode|end-to-end
uc-etki: {durum: unknown, kanit: null}   # düzeltme gerçekleşti mi, amaç sağlandı mı — ayrı
```
- Kural: kapanan her bulgu için `yanit.iz` zorunludur. "koru" (değiştirmeme) geçerli bir yanıttır; gerekçesi ve kanıtı yazılır.
- Oturum başı denetimi: `yanit` boş bulgular ve `iz` göstermeyen kapanışlar listelenir. Bu, "raporlandı ama tüketilmedi" hatasını görünür kılar.
- Eylem engellendiyse (izin kapısı) bulgu "karar etkilendi, uygulama engellendi" diye ayrı yazılır (`G2 §6`).

**Kanıt:** Kubernetes HPA, Google SRE ve FAA dayanaklı analiz; 7 oyuncak kontrol (G7) [K]. DevOS'ta sınanmadı [B].
**Karar: AL.**

### M7 — Ders merdiveni: kayıttan kalıcı davranışa

**Dayanak [K]:**
- "stored lesson != retained response change established" ve "fixed code/weights != fixed effective response regime" (`T:feedback-adaptation/KEY.md`).
- Gelecek-tepki testi: "Holding a materially comparable future situation constant, would the system now respond differently because of prior feedback/history? If not, persistent adaptation is not established by storage or documentation alone." (`FEEDBACK-ADAPTATION-SYNTHESIS.md §5`).
- Taşıyıcı zinciri: "carrier written != candidate path installed != relevant path traverses carrier != response disposition changed at that locus != all applicable paths changed != retained after the claimed lifecycle transition" (`persistent-adaptation/D3 §2`).
- Dış taşıyıcı meşrudur ama görünür olmalı: "A system can use the same model and interpreter while a history-derived external carrier changes later responses." "A memory-backed system can retain its disposition through retrieval/reload, while the model alone cannot. But that dependence must remain visible." (`HISTORICAL-PERSISTENT-ADAPTATION-SYNTHESIS.md §2, §4`).
- İş tamamlanması uyum değildir: "training created but not required/used; regression test added but not executed by the relevant pipeline; policy updated in source but not propagated to runtime; action item closed administratively without changed behavior." (`F2 §7`).
- Prob kirlenmesi: "A probe may feed back a score, write a memory, train a participant or trigger an update… Separate the pre-probe and post-probe target, freeze or isolate updates where feasible" (`HIST §6`). "A record, developer assertion or agent self-report alone does not settle that question." (`D1 §4`).
- Yetki: "It does not grant the system authority to change its own governing rules or make its self-assessment independent evidence." (`HIST §9`). "The present SOUL research likewise does not authorize self-modification of agent-control files." (`G3 §7`).
- Fayda ayrı bir iddiadır: "adaptation occurrence != benefit != authority != transfer" (`KEY`). Vekil hedef riski: "fewer review findings because reviewer sensitivity degraded; agent optimizes eval suite rather than target behavior" (`F3 §5`).
- Yükseltme örüntüsü: gstack'te "prose/local convention → real failure → named distinction → reusable helper/runtime rule → invariant/scanner → behavioral/environment E2E → CI/release consequence" (`F5 §6`). Ayrıca "repeated failures may later become deterministic controls" (`F:04…/DEFERRED-RELATIONS.md §14`; aynı fikir `Q3 §10`'da da var).

**Sorun:** Önceki DevOS denemelerindeki "ders yazıldı, davranış değişmedi" hatası (O10 §4). Bulut özel riskleri [Ç, BRIEF §3]: yeni oturum, bağlam sıkıştırması ve geri alınan makine birer "lifecycle transition"dır. Ders taşıyıcısı her oturumda yüklenmiyorsa kalıcılık yoktur. Ana oturumun kendi hook'ları da bu riski taşıyor (§5.1).

**Nasıl işler [Ç]:**
- `devos/ders/<id>.yaml`, basamak başına ayrı kanıt taşır:
```yaml
ders: DRS-031
gecmis: {olay: devos/olay/2026-09-20-yanlis-dal.md, bulgu: BLG-88}
tasiyici: {tur: hook|skill|CLAUDE.md|test|betik, yol: "…", surum: "git:…"}
basamaklar:
  yazildi:        {durum: true,  kanit: "commit …"}
  yola-kuruldu:   {durum: true,  kanit: "settings.json hook kaydı / skill description"}
  yol-kullaniliyor: {durum: unknown, kanit: "hook günlüğünde tetiklenme izi aranıyor"}
  davranis-degisti: {durum: not-evaluated, prob: devos/prob/DRS-031.md, kirletme: "prob bellek/ders yazmaz; ayrı dalda"}
  tum-yollar:     {durum: unknown, kapsam: [ana-oturum, alt-ajanlar, headless]}
  kalicilik:      {durum: unknown, ufuk: "yeni oturum + sıkıştırma sonrası", destek: "her oturum yüklenen dosyada"}
  fayda:          {durum: not-evaluated, not: "ayrı nedensel iddia → M9"}
yukseltme: "aynı hata 2. kez → hook/test'e çevir (deterministik kontrol)"
```
- **Prob.** Aynı durumun sabit kurgusu hazırlanır (örneğin yanlış dala push girişimi) ve ayrı bir oturumda ya da alt ajanda koşulur. Beklenen tepki (hook engeli ya da ajan reddi) gözlenir. Prob ders dosyasını değiştiremez.
- **Yetki.** Ders, kural dosyasını kendiliğinden değiştiremez. Kural değişikliği M13'e göre Batu'nun yetki kapsamındaysa onunla, değilse DevOS'un kural sahibi rolüyle yapılır ve M3 kaydına işlenir.
- "Öğrendi" kelimesi kullanılmaz; "uyum gerçekleşti (şu basamağa kadar)" denir (`F7 Attack F`: "retain Adaptation terminology; do not equate with successful learning").

**Kanıt:** 15 kurgu vaka + 4 yanlış kural reddi, kaynağa göre PASS (`persistent-adaptation/checks/semantic-check-results.json`) [K]. Kaynak sınırı da yazıyor: "No actual DB, worker process, host lifecycle, agent conversation, model training, human intervention or organizational change was executed." (`D7 §4`). Kurgudaki `Agent(lessons, connected)` yapısı DevOS'a birebir benzer: ders dosyası var ama yola bağlı değilse tepki değişmez (`inert_record`).
**Karar: AL.** DevOS öğrenme döngüsünün çekirdeğidir.

### M8 — Olay analizi (gerçek nedensellik)

**Dayanak [K]:**
- Tam açıklanan etki önce gelir: "ambiguous effect target → ambiguous causal question" (`causal-effect-contribution/E1 §2`). "initial fault / outage / user harm / outage duration / recovery delay are distinct effects" (`actual…/synthesis §2`).
- İkili soru: "1. Why did the initiating adverse event occur? 2. Why did it progress far enough to create this broader effect?". Örnek: "bug introduced → unit test misses → review misses → production monitor misses → user harm" (`E2 §6`).
- Derinlik ağacı: "Exact effect E ├─ immediate/direct mechanism(s) ├─ enabling/contributing conditions ├─ prevention/barrier failures where relevant ├─ detection/containment failures where relevant └─ deeper systemic/framing conditions where they materially change intervention/recurrence analysis" (`E2 §13`).
- R06 durma kuralı: "Continue deeper while another causal layer materially changes intervention choice, recurrence risk, control design, responsibility boundary or decision outcome. Stop when additional depth no longer changes those materially." (`causal…/synthesis §8`).
- Birleşik ve rakip nedenler: "joint causal configuration != collection of independent cause edges" (`actual…/STATE`). "never require: root_cause = exactly one value" (`synthesis §11`). "actual cause unresolved among {H1, H2, H3}" ayırt edici testlerle korunur (`A3 §8`).
- Kanıt: "high-confidence timeline != high-confidence causal explanation" (`A3 §2`). "no trace observed != event/path absent when instrumentation/selection/retention is incomplete" (`A3 §11`). "Incident conditions can disable telemetry, corrupt records or select which evidence survives." (`A3 §12`).
- Kontrol kusuru: "Control defect != actual causal contribution by identity". "A defective barrier can be causally irrelevant if another barrier stops the path or the hazard never reaches it." (`synthesis §9`).
- Suçlama ayrımı: "causal contribution != responsibility != accountability … critical for avoiding blame-driven causal models" (`causal…/synthesis §14`).
- Beşli zincir: "Work occurred != target effect occurred != Work caused effect != evidence establishes causation != Actor is institutionally/morally accountable" (`F:04…/Q3 §11`).
- Olay kaydı olayın kendisi değildir. Foundation, WHO'nun olay raporlama rehberini şöyle okuyor: "report data have strengths and limitations and that conclusions must be drawn cautiously; the purpose is learning that reduces future risk/harm". Eşleme: "actual harm/safety condition → Environment / incident/report/analysis → Information" (`Q4 §4`).

**Nasıl işler [Ç]:** `devos/olay/<tarih>-<ad>.md` şablonu:
```markdown
# Olay <id>
## Açıklanan etkiler (ayrı ayrı): oluş | ilerleme | şiddet | süre/kurtarma gecikmesi
## Olgular: zaman çizelgesi (güven) + gözlem kapsamı (hangi yollar görünmüyor, hangi kayıt eksik)
## Katkıda bulunanlar: rol (tetik / doğrudan / olanaklı kılan / önleme hatası / tespit-sınırlama hatası / sistemik)
   + birlikte-yeterli kümeler ("A VE B") + alternatif yeterli yollar
## Rakip açıklamalar: H1 / H2 / H3 — ayırt edici test — durum (çözüldü / çözülmedi)
## Derinlik: R06 — bir kat daha şunu değiştiriyor mu? müdahale | yinelenme riski | kontrol tasarımı | sorumluluk sınırı | karar
## Sorumluluk ayrımı: nedensel katkı ≠ sorumluluk ≠ hesap verebilirlik (Batu'ya yük bindirilmez)
## Çıktılar: → M7 ders(ler)i, → M3 kontrol değişikliği, → M9 etki iddiası (önceden/sonradan kanıt değildir)
```
**Kanıt:** NASA, NTSB, FAA, CDC, WHO ve MIT CAST dayanaklı analiz [K]. Actual ve Contrastive geçişlerinde "Fresh public-web retrieval failed technically" (`actual…/STATE`); dış kaynak ebeveynden devralındı [K].
**Karar: AL.** O8/O9'daki olay/devir yapılarına alan listesi olarak eklenir.

### M9 — Etki iddiası (karşıtsal nedensellik): "bu değişiklik işe yaradı" demenin koşulu

**Dayanak [K]:**
- ""X works" != well-formed causal-effect claim" ve "causal effect identity = outcome + target + X vs X' + applicability frame (+ exact regime/configuration semantics where material)" (`contrastive…/KEY.md`).
- Ajan örneği: "permanent eval E reduced recurrence" iddiası şunları ister: "failure/outcome definition; target task/agent/environment population; E version and enforcement semantics; comparator regime; actual execution/fidelity; model/prompt/routing co-changes; spillover/interference; time horizon; eval/staging→production transport; confounding/selection/reporting changes." (`contrastive…/synthesis §20`).
- Rakip açıklamalar: "guardrail causal effect; lower workload; different task mix; newer model release; unrelated infrastructure change; reporting change; regression to mean; random fluctuation" (`E3 §3`).
- Aynı ad, aynı müdahale değildir: "Hook G v1: blocks direct Write only / Hook G v2: blocks direct + shell-equivalent paths / Hook G v3: blocks all known material paths + logs decision … Calling all three `G = on` can erase causal differences." (`I2 §5`). "review before execution != review after execution" (`I2 §11`).
- Paket değişiklik: "bundle effect != component effect" (model, prompt, guardrail, routing ve telemetry birlikte değiştiğinde; `synthesis §9`).
- Seçilim yanlılığı: "high-risk tasks → more likely to receive stronger guardrail → more likely to fail anyway" (`I3 §2`). "only failures receive deep traces" (`I3 §4`).
- Sürüm taşınması: "The historical effect is not retroactively false; its applicability to the new target is no longer established." (`I3 §15`).
- Kontrol etkinliği bir bileşimdir: "Control present != implemented != enforced != complied with != causally effective != sufficiently effective for criterion" → "Control + Contrastive Causal Effect + Composite Standing" (`KEY`).

**Nasıl işler [Ç]:** DevOS'taki her "iyileşme" iddiası (retrospektif, sürüm notu, Batu'ya rapor) iki sınıftan birine konur. **Gözlem:** "önce/sonra şunu gördük" dili kullanılır. **Nedensel iddia:** şu blok zorunludur:
```yaml
etki-iddiasi:
  sonuc: "yanlış dala push girişimi / oturum"     # tam tanım + ufuk
  hedef: "DevOS bulut oturumları, Eylül–Ekim"
  X: "KNT-03 v3 (hook, tüm bilinen yollar)"      X': "KNT-03 v1 (yalnız doğrudan push)"
  sadakat: "hook tüm oturumlarda yüklendi mi? kanıt: günlük"
  eszamanli-degisiklikler: ["model sürümü", "CLAUDE.md §4"]   # varsa: paket etkisi
  rakipler-elendi-mi: {is-karisimi: ?, raporlama-degisimi: ?, ortalamaya-donus: ?}
  tasima: "staging → gerçek iş için varsayımlar"
  durum: unknown | desteklenen | ayırt-edilemedi
```
**Kanıt:** Dawid/Musio, CDC ve NIST dayanakları ebeveynden devralındı; web erişimi başarısızdı (`I5 §2`) [K].
**Karar: UYARLAYARAK AL.** Tam nedensel çıkarım DevOS ölçeğinde çoğu zaman mümkün değildir. Asgari kural, gözlemin nedensel diye raporlanmamasıdır (`G3`'teki "proxy" ve `F3 §5` riskleri).

### M10 — Kayıt bağlama kuralları (Binding)

**Dayanak [K]:**
- İmza: "relation meaning … exact anchors … each occupying typed semantic positions … applicability structure (scope/reference frame; effective/reference time when material; operation/method/stage/state/version/role qualifiers when material) … relation-instance individuation … qualified/n-ary structure when binary decomposition loses association" (`C:relational-binding/STATE.md`).
- "A repository can contain "Actor A is authorized for Work W". That informational state does not prove that the authority relation actually holds." (`B1 §11`). "status says `assigned` ≠ actual participation" (`B1 §11`).
- "A performs W at t1 / A verifies W at t2" ayrı kalmalı (`B3 §2`). Dört zaman: "effective interval; assertion/observation time; event time; reference time". Örnek: "delegation effective until 17:00; record updated at 17:10; revocation event occurred at 16:55; query asked about authority as-of 16:30" (`B3 §10`).
- "W depends-on R" yöntemsiz yazılırsa "Work is globally blocked when R is unavailable; alternative method M2 is impossible" gibi yanlış sonuçlar çıkar (`B3 §4`).
- "Work W requires two independent reviewers" küme düzeyinde bir Control/Standing kısıtıdır; tek bağın özelliği değildir (`B3 §11`).

**Nasıl işler [Ç]:** DevOS kayıt biçim kuralı (bütün `devos/` YAML'ları için):
- (a) hedefe dal adı değil `yol@sha` yazılır;
- (b) rol alanı zorunludur (`uretici/dogrulayici/karar-veren/etkilenen`);
- (c) aynı kişi ya da ajanın iki rolü iki ayrı kayıttır;
- (d) zaman alanları ayrıdır (`gecerli-baslangic/bitis`, `kaydedildi`, `olay-zamani`, `hakkinda-oldugu-an`);
- (e) devir kaydı `devreden, devralan, islem, kapsam, adina, bitis` alanlarını taşır.

Basit bir şema denetimi (`devos/bin/kayit-sema`), Stop hook'unda ya da commit öncesi koşar.
**Karar: AL.** Maliyeti düşüktür, M1–M6'nın ön koşuludur.

### M11 — Tek otorite durum, çok katmanlı ilerleme ve negatif kontrollü defter denetleyicisi

**Dayanak [K]:**
- "parent accepted != child separately researched / child pass complete != all descendants complete / accepted != independently verified / semantic route != target-specific proof / recommended work != activated work" (`F:06…/KEY.md`).
- Atama zinciri: "Actor assigned to Work → therefore Work admitted → therefore Actor obligated → therefore Actor authorized → therefore Actor accountable. Every implication can fail." (`F:04…/Q3 §2`).
- Pano iş değildir: "Work representation/status != actual Work state". Aynı yerdeki baskı örnekleri: "ticket/status/dashboard versus actual Work state" ve "handoff/continuity information versus Work suspension/resumption" (`Q3 §6`).
- "A current reader must distinguish: a node was identified; its place was accepted; its own pass was completed; its descendants were separately researched; its semantic result was accepted; its result was independently verified. None of these transitions should be inferred solely from the previous one." (`F:06…/SYNTHESIS.md`).
- I5: "Carry separate status for dedicated research, descendant depth, acceptance, publication, target evidence and independent verification." (`F:07…/SYNTHESIS.md §7`).
- "No percentage-complete metric is warranted: file counts, node counts and research depth are different denominators." (`06 B2 §1`).
- Kaba özet ayrımı kaybettirir: "A consumer that reads only the coarse view can lose the distinction." (`06 B3`). "Do not demote the three promoted Information children into mere optional vocabulary to make the dashboard green." (`06 B2 §4`).
- Denetleyici deseni: `F:06…/checks/frontier_audit.py`. Anlık görüntünün git blob SHA'sını doğrular, beyan edilen defter değişmezlerini sınar ve bilinen dört kötü varyantı reddetmek zorundadır: "inherited_completion", "acceptance_regression", "wrong_frontier_member", "unauthorized_activation". Kaynak kendi sınırını da yazar: "Declared source/ledger invariants only; no proof of taxonomy, literature coverage or live behavior." (`checks/RESULT.json`).

**Sorun:** DevOS iş defteri (pano ya da backlog) ile rol notları ve devir notları ayrı ayrı "durum" taşır ve zamanla çelişir. Foundation'da bu çelişki gerçekten görüldü (§4.1).

**Nasıl işler [Ç]:**
- Her iş için **tek otorite** `devos/is/<id>.yaml`. Diğer bütün görünümler (pano, KEY benzeri özetler, devir notları) ya bu dosyadan üretilir ya da "türev, otorite değil" başlığı taşır.
- Durum alanları çok katmanlıdır: `tanimlandi, planlandi, atandi, etkinlestirildi (Batu/rol yetkisiyle), yapildi, dogrulandi(M1), kabul-edildi(M13), yayinlandi(M12), bagimsiz-dogrulandi`. Hiçbiri öncekinden türetilmez. `atandi`, işin etkinleştirildiği ya da atanan rolün yetkili olduğu anlamına gelmez (`Q3 §2`).
- `devos/bin/defter-denetle` (frontier_audit uyarlaması) şunları yapar:
  1. otorite dosyalarından değişmezleri sınar (kabul edilmemiş iş `yayinlandi` olamaz; `etkinlestirildi` alanı yetkili rol ya da onay kaydı ister; alt iş durumu üstten miras alınamaz);
  2. her koşuda kopyalanan kötü varyantları üretir ve **reddettiğini** gösterir;
  3. türev dosyalarda otoriteyle çelişen durum kelimelerini arar.
```python
bad = {"miras_tamamlanma": lambda d: set_child(d, "yapildi", from_parent=True),
       "kabul_gerilemesi": lambda d: set_field(d, "kabul-edildi", False),
       "yetkisiz_etkinlestirme": lambda d: set_field(d, "etkinlestirildi", True, yetki=None)}
for name, mutate in bad.items():
    assert raises(audit, mutate(copy(ledger))), f"kötü varyant kaçtı: {name}"
```
- **Sınır:** Denetleyici kaydın tutarlılığını sınar, işin gerçek durumunu değil (`Q3 §6`). Gerçek durum M1 kanıtıyla kurulur. Devir notu da işin askıya alınmış hâlinin kendisi değildir, yalnız temsilidir.

**Kanıt:** 06 denetleyicisinin koşu sonucu "baseline PASS" ve 4 reddedilen varyanttır [K]. DevOS'ta sınanmadı [B].
**Karar: AL** (uyarlanmış defter). Negatif kontrol fikri özellikle değerli: denetleyici, bozuk defteri yakalayabildiğini her koşuda kanıtlar.

### M12 — Yayın ve geri okuma (write ≠ publish)

**Dayanak [K]:**
- "Publication is a separate operation: verify candidate diff is confined to Foundation, preserve concurrent changes, update main without force, then read back current main and the key state/result files. A tree or commit object alone is not successful publication." (`F:06…/B5-CLOSURE.md`).
- Uygulama kaydı: "Immediately before the update, main still matched the input. The new commit was installed with `force=false` … All eight changed files were then fetched through main with their complete text, without requested line truncation … A separate main-ref read after those checks returned the published update" (`F:08…/COLD-START-CHECK-2026-09-17.md`).
- "Before mutation, the actual PR head and main ref still matched the reviewed head and baseline … merged … with `expected_head_sha` bound to the exact reviewed head." (`F:REPAIR-PUBLICATION.md`).
- Kesilme durumu: "Root STATE then recorded the active work and unfinished synchronization explicitly, preventing an interrupted session from mistaking the discussion-only state for current authority." (`F:08…/PUBLICATION.md`).
- Dürüst sınır: "Some identity reads intentionally requested only the opening line plus returned Git SHA; they are not claimed as fresh full text readings." (`PUBLICATION.md`).

**Nasıl işler [Ç]:** `devos/bin/yayinla` adımları:
1. `git fetch`; beklenen taban SHA ile uzak dalı karşılaştır, fark varsa dur;
2. değişen dosya listesinin beklenen klasörle sınırlı olduğunu denetle;
3. `git push` (force yok);
4. `git ls-remote` ile uzak SHA = yerel SHA;
5. değişen durum/sonuç dosyalarını uzaktan (`git show origin/<dal>:<yol>`) tam oku ve yerel içerikle karşılaştır;
6. ancak sonra iş kaydına `yayinlandi: {sha, dogrulandi: true}` yaz.

İşlem yarıda kalırsa STATE'e "senkronizasyon tamamlanmadı" satırı yazılır. VM geri alınabilir (BRIEF §3), bu yüzden bu satır önemlidir.
**Karar: AL.** Bulutta dal ve push kısıtları O11'de doğrulanmalı.

### M13 — Batu (sahip) onayının kapsam kaydı

**Dayanak [K]:**
- "The user answered "evet onay veriyorum" … That closes the repair evaluation and merge-authorization gates only. It does not accept Revision's leading leaf hypothesis or authorize research resumption." (`F:REPAIR-PUBLICATION.md`).
- "This is contextual acceptance, not a fabricated verbatim statement of agreement with each refinement." (`F:07…/PLAN.md §1`). "User acceptance closes the sequencing/evaluation gate; it does not change verification independence." (her X7 kapanışı).
- "Support in direction is not recorded as an unconditional acceptance of every scientific claim or a build grant." (`F:README.md`). "Do not fabricate a formal approval or a target execution grant. Equally, do not pretend the discussion never happened" (`F:STATE.md`).
- "Discovering a missing decision is not permission to make it on the owner's behalf." (`F:08…/SYNTHESIS.md §4`).
- Aynı söz, dar okuma: "anlaştık. Devam et. Operasyonel sınırına kadar çalış." → "This authorizes the previously proposed integration review, not architecture or an unlimited sequence of new child passes." (`F:06…/PLAN.md` "Authority"). [G] "operasyonel sınırına kadar çalış" kalıbı 03, 05 ve 06 altında en az 10 kayıtta geçiyor (`grep`). Her kayıt, sözün neyi yetkilendirdiğini ve neyi yetkilendirmediğini ayrı yazıyor.

**Sorun:** K-015'e göre Batu müşteridir: amaç verir ve kabul eder. Kısa bir "tamam" geniş yetki sanılırsa DevOS kendi kendini yetkilendirir. Tersine, yetki kaydı tutulmazsa her adımda Batu'ya tekrar sorulur; Batu'nun sorumluluk yüklenme yasağı (STANDART) da ihlal edilir.

**Nasıl işler [Ç]:** `devos/onay/<tarih>-<kisa>.yaml`:
```yaml
soz: "anlaştık. Devam et. Operasyonel sınırına kadar çalış."   # birebir + kaynak mesaj kimliği (örnek: F:06…/PLAN.md "Authority")
baglam: "Kalıcı Uyum sonucu + D6 rafinmanları sunulmuştu"
kapattigi-kapilar: [PA-kabul, entegrasyon-incelemesi-baslat]
yetkilendirmedikleri: [mimari, yeni-alt-dal, agent-control-degisikligi]
yorum-turu: acik | baglamsal        # bağlamsal ise gerekçesi
```
Kural: "etkinleştirildi" alanı (M11) ancak bir onay kaydına ya da DevOS rol yetkisine atıf yaparak doldurulabilir.
**Karar: AL.** Foundation'ın gözlenen pratiğidir ve işe yaradığına dair repo içi kayıt vardır [G]: onaylar bu biçimde saklanmış ve sonraki oturumlar bunlardan devam etmiş.

### M14 — Kanıt kökeni ve bağımsızlık

**Dayanak [K]:**
- "more messages / reviewers / revisions != more independent evidence"; ayrıca "a report says all tests ran; a summary copies that report; a reviewer sees the summary and endorses it. The endorsement can genuinely change the release decision while adding no evidence that the tests executed." (`returned-influence/G3 §4–§5`).
- "A release dossier contains twelve accurate summaries of one test run … Multiplying copies does not increase independent observation count." "A receipt for the dossier does not show an actor read, understood or accepted it." (`F:08…/CASE-AUDIT.md C1`).
- Aynı-model sınırı: "'No new contradiction found' independently proves the model | Rejected. The same model uses shared assumptions" (`06 B3`). "Testing the same constructed object again is useful reproducibility, not independent validation" (`persistent-adaptation/D2 §7`).

**Nasıl işler [Ç]:** Her kanıt satırı `koken:` alanı taşır (test koşusu kimliği, komut + çıktı dosyası, Batu mesajı). Bir karar için sayılan kanıtlar farklı kökenlerden olmalıdır. Özet ya da devir notu kanıt sayılmaz, yalnız işaretçidir. Doğrulayıcı "kaynağa temas" etmek zorundadır: testi kendisi koşar ya da diff'i kendisi okur (M2). `DERSLER.md` L1'deki "beyan / doğrulandı" ayrımı, bu kuralın alt ajan dönüşündeki biçimidir [G]: alt ajanın kendi kapsamı hakkındaki sözü `koken: beyan` taşır, kaynağından doğrulanınca `koken: dogrulama` olur.
**Karar: AL.** O10'un "var ≠ kullanıldı" dersinin kanıt tarafıdır.

### M15 — Foundation kullanım kaydı ve perspektif keşfi (üretim dersi)

**Dayanak [K]:**
- Asgari kullanım kaydı: "the target question; the exact research claim/path/version; its applicability and contrary case; the situated requirement or choice it informed; and what target evidence is still missing." Kaynak şunu da ekler: "not a compulsory schema … Existing target records may already suffice." (`F:08…/REUSE.md`).
- "A role need does not imply an AI agent, and an instruction need does not imply that a particular file enforces it. A memory need does not automatically imply a vector database. Conversely, a simpler arrangement is not adequate merely because it is simple." (`REUSE.md`).
- Üretim dersi: sahibin düzeltmesi "who researches and writes questions, who plans and assigns work, who sets priorities, what rules apply, where workers operate, and how they use information". Asistan "withdrew its early example-closure claim". Sonuç: "useful production-side research existed, but the assistant did not apply that perspective sufficiently before declaring the example complete" ve "The adequacy of the knowledge, its discoverability and its actual application must remain separable questions." (`F:08…/DISCUSSION-HANDOFF.md §2–§3`).
- Üretim tarafının karşıt örnekleri doğrudan DevOS hata sınıflarıdır: "every assigned task succeeds but an unassigned requirement is missing; a qualified worker lacks the needed information/access; a review is performed but fails to detect relevant errors; a new version is approved but the old version is published; and a procedure is rewritten without demonstrating retained behavioral improvement." (`§2`).
- "The strongest remaining risk is … lossy application of a rich framework, particularly silently centralizing goals/authority, confusing stored representations with realized effects or treating a routed requirement as technically solved." (`RIVALS-AND-REUSE.md §7`).

**Nasıl işler [Ç]:**
- DevOS tasarım belgelerinde Foundation'a dayanan her karar 5 alanlı kısa bir blok taşır.
- DevOS'un kendi iş döngüsünde "kapanıştan önce perspektif taraması" yapılır: üretim, kullanım ve etki. DISCUSSION-HANDOFF'un 5 karşıt örneği, kapanış öncesi kontrol sorularına çevrilir (atanmamış gereksinim var mı, çalışanın bilgi/erişimi var mı, inceleme neyi kaçırabilir, onaylanan sürüm mü yayınlandı, prosedür değişikliği davranışta görüldü mü).
- Foundation bunun bir **aday** olduğunu söyler: "candidate later design concern, not an adopted checklist". Bu yüzden DevOS bunu sınanacak bir mekanizma olarak kurar; etkisi M9 ile ölçülür.

**Karar: UYARLAYARAK AL.** Kullanım kaydı hafif tutulur. Perspektif taraması 5 soruyla sınırlı, ölçülen bir deneydir.

### M16 — Araştırma paketi düzeni (Foundation'ın kendi çalışma mekanizması)

**Gözlem [G]:** Foundation'ın her paketi aynı iskeleti izliyor:
- `X0` kanıt kurtarma (dondurulmuş yanlışlayıcılarla);
- `X1` asgari imza;
- `X2`/`X3` ayrım ve zor vakalar;
- `X4` rakip ayrıştırmalar;
- `X5` dış ve aday baskı;
- `X6` sentez ve çocuk kararı;
- `X7` çekişmeli kapanış;
- ayrıca STATE (otorite), KEY (L0 özet), INDEX, FINDINGS-MAP, OPEN-QUESTIONS (açma ve açmama koşulları), CURRENT-SURFACES (blob SHA manifesti) ve kullanıcı değerlendirme kapısı.

Bu iskelet 198 dosyalık 05'te tutarlı biçimde uygulanmış. Güçlü yanları:
- plan sonuç görülmeden yazılıyor (`07 PLAN §5`, `checks/SPEC.md`: "No outcome is inspected before this program/specification publication");
- ilk koşu saklanıyor ve değiştirilmemiş tekrarla karşılaştırılıyor (`07 checks/EXECUTION.md`);
- "non-reopen conditions" gereksiz yeniden açılmayı engelliyor;
- sıra baştan dondurulmuyor. `C7 §13` kendi sıra önerisini düzeltti: "Relational Binding should be first. After its closure, re-select … rather than pre-committing to a fixed full sequence."

Zayıf yanları:
- yönlendiriciler bayatlıyor (§4.1);
- aynı-model kapanışı bağımsızlık sağlamıyor;
- ağır iskelet, küçük sorular için pahalı.

**Karar: UYARLAYARAK AL.** DevOS'un *araştırma tipi* işleri için hafifletilmiş sürüm: X0 (kaynak ve yanlışlayıcı), X4 (rakip), X7 (çekişmeli kapanış), STATE ve OPEN-QUESTIONS. Kodlama işleri için alınmaz; onlarda M1, M2 ve M12 yeter.

---

## 3. Alınmayacaklar (gerekçeli)

| Aday | Karar | Gerekçe (birebir) |
|---|---|---|
| Dört zemin ya da dört bileşim bölgesini klasör, servis veya ajan yapmak | ALMA | "not architecture modules" (`C:synthesis/COMPOSITION-PARENT-SYNTHESIS.md`); "A branch is not a mandatory service, file or agent" (`F:STATE.md`) |
| Politika motoru, iş akışı motoru, graf DB, olay otobüsü seçmek | ALMA (bu gerekçeyle) | "These can realize one or more composition semantics but cannot define the research map." (`C:C1 §9`); Standing ve Control'ün "non-reopen conditions"ı bu mekanizmaları özellikle anıyor. Yalnız ilişki ağından oluşan model için: "the same relation name can drift across incompatible endpoint meanings"; "it does not replace the need for stable semantic anchors" (`F:04…/Q5 §10`) |
| Evrensel fail-closed | ALMA | "No universal `fail-closed` rule is inferred" (`K3 §9`); varsayılan kontrol başına seçilir (M3) |
| Tek `kök neden` alanı | ALMA | "never require: root_cause = exactly one value" (`causal…/synthesis §11`) |
| "Sistem öğrendi" dili | ALMA | "do not equate with successful learning" (`F7`); "stored lesson != adaptation" |
| Yüzde ilerleme ve yeşil pano | ALMA | "No percentage-complete metric is warranted" (`06 B2 §1`) |
| Sabit araştırma veya iş sırası (Binding → Standing → Control → Transition gibi) | ALMA | `C7 §13` düzeltmesi; "Do not import a fixed sequential/parallel/hierarchical taxonomy as Foundation truth." (`04 DEFERRED §10`) |
| Kapanış öncesi evrensel zorunlu kontrol listesi | ALMA (M15'teki ölçülü deney hariç) | "not an adopted checklist, harness or other mechanism" (`F:README.md`) |
| "Doğrulayıcı" etiketli ikinci ajanı bağımsızlık saymak | ALMA | "multiple agents != separation of duties by default" (`K5 §11`) |
| Yönetişimi tek kova yapmak: kural metni, yetki, kontrol işi ve gerçek yaptırımı tek bir bileşenin ya da ajanın "sahipliğinde" birleştirmek | ALMA (bu biçimde) [Ç] | "one peer ground would mix normative standing, informational rules, Work control activities and realized enforcement" (`F:04…/Q1 §3`). Foundation, NIST AI RMF'yi de şöyle okuyor: "Govern explicitly cross-cutting" (`Q4 §5`). Bir kural sahibi rolü olabilir; ama rolün varlığı yaptırımın varlığı değildir (M3) |

**Koşullu izin: DevOS'a özgü işletim profili** [K]. Foundation, yazılım teslimine uygun bir bölümlemeyi açıkça DevOS için tartıyor: "Resources / Work / Actors / Artifacts / Governance … Looks operationally useful for Development OS and software delivery." Bunu genel Foundation çerçevesi olarak reddediyor, ama şunu ekliyor: "Could be a task-specific operating profile, not the top-level research frame." (`F:04…/Q5-RIVAL-DECOMPOSITIONS.md §7`). Yani DevOS kendi bölümlemesini kurabilir. Foundation'ın aynı yerde saydığı üç kayıp ise kapatılmalıdır [Ç]:
1. "`Artifacts` is narrower than Information; observations, transient context, hypotheses, signals, models and non-persistent representations do not cleanly fit." DevOS'ta bağlam, hipotez ve oturum içi sinyal de bilgidir. Bellek ve bağlam tasarımı yalnız dosyalara bakamaz.
2. "`Resources` is much narrower than actual Domain Reality and turns Environment into a support-only frame." DevOS'un ortamı yalnız araç, izin ve kota değildir; SOUL'un hedef alanındaki gerçek durum da ortamdır. "İş bitti" ile "hedefte etki oldu" ayrı kalmalıdır (M1, M9).
3. "`Governance` repeats the cross-ground norm/control problem". Yönetişim bölümü olsa bile her kontrol kaydı dört yüzü ayrı tutar (M3).

---

## 4. Dersler

### 4.1 Bayat yönlendiriciler: Foundation'ın kendisinde gözlenen durum [G]

Aşağıdakiler otorite STATE ile çelişen, "güncel" görünen ifadelerdir. Hepsi 2026-09-27'de bu dalda okundu.
1. `C:relational-binding/KEY.md`: Composite Standing "is now awaiting user evaluation"; STATE ise kabul edildi diyor.
2. `C:composite-standing/FINDINGS-MAP.md` başlığı: "awaiting user evaluation".
3. `T:KEY.md` (09-12): 06 incelemesi "findings await evaluation"; `T:STATE.md` (09-14) ise "accepted and closed".
4. `T:OPEN-QUESTIONS.md`: "Review evaluation is next; Formation is not active."
5. `T:feedback-adaptation/INDEX.md`: "Three promoted Information children remain unresearched."; oysa `F:07…/COMPLETION-DEPTH.md §2` üçünü de araştırılmış gösteriyor.
6. `T:feedback-adaptation/KEY.md`: "That review awaits evaluation; Formation is recommended but inactive."
7. `…/persistent-adaptation/STATE.md`: 06 incelemesi "awaits separate evaluation".
8. `…/returned-influence/INDEX.md`: "awaiting evaluation".
9. `T:causal-effect-contribution/STATE.md`: "Cross-Ground Feedback / Adaptation: recommended next / inactive".
10. `…/contrastive…/STATE.md`: aynı ifade.
11. `T:transition-propagation/STATE.md`: "Cross-Ground Causal Effect / Contribution — active after acceptance".
12. `F:04…/INDEX.md`: "Parent-level relation/control/composition research is active under `../05`".
13. `F:06…/FRONTIER.json`: `"review_state": "user_evaluation_pending"`. Makinece okunan dosya, tarihsel olduğunu söylemiyor.

**Kök neden [K+Ç]:** Durum bilgisi birden çok görünümde elle kopyalanıyor. Onarımlar yalnız "çekirdek rotaları" kapsadı. `C:CURRENT-SURFACES.md` bunu itiraf ediyor: "This does not prove every old child router is free of stale wording." `REPAIR-AUDIT §4` de öyle. Sorun yeni de değil [K]. 04'ün ilk geçişi, 2026-09-05'te `03…/information/OPEN-QUESTIONS.md`'de aynı türden bayat bir ifade buldu. Doğru olanı yaptı: "The stale residual wording was **not** used as status authority." Sonra o tek dosyayı elle temizledi (`F:04…/Q0 §6`). 22 gün sonra bu okumada 13 yeni örnek görüldü [G]. Tek tek elle temizlik, yinelenmeyi önlemiyor.
**Önlem:** M11 (tek otorite, türev görünüm üretimi ya da denetimi) ve M5 (yayılım denetimi).

### 4.2 Diğer dersler

| Ne oldu | Kök neden | Önlem | Kaynak |
|---|---|---|---|
| Soru bankası örneği, üretim tarafı sınanmadan "bitti" dendi | İlk göze çarpan bakış açısına sabitlenme; bilginin varlığı ≠ uygulanması | M15 perspektif taraması (ölçülü) | `F:08…/DISCUSSION-HANDOFF.md §2–§3`; `F:STATE.md` |
| Tartışma ve düzeltme depoya yazılmadı; soğuk başlangıç eski noktayı gösterdi | Konuşma durumu depoya işlenmedi | Her kararda STATE güncellemesi + M12 geri okuma | `DISCUSSION-HANDOFF.md §1`; `COLD-START-CHECK` |
| Kaba "tüm zeminler kabul" özeti, araştırılmamış üç Information çocuğunu gizledi | Özet, kapsam niteleyicisini düşürdü | M11 katmanlı durum | `06 B3` "Error-path explanation" |
| Son olaya göre program seçme eğilimi | Göze çarpanlık (salience) yanlılığı | Sonraki işi seçmeden önce aday karşılaştırması | `06 B3`: "salience bias" |
| Tahmin edilen dosya adı 404 verdi; "sonuç yok" sanılabilirdi | Yol tahmini | INDEX üzerinden yol bul; 404 ≠ yokluk | `F:07…/SOURCE-LEDGER.md §1` |
| Eksik bir rota iddiası, yeniden okununca geri çekildi | Okumadan kusur ilanı | Kusur raporundan önce sabitlenmiş kaynağı yeniden oku | `F:REPAIR-AUDIT.md §2` |
| Kesik araç çıktısı | Araç sınırı | Kalan satırlar tamamlandı ve bu kayda geçti | `07 SOURCE-LEDGER §3`; bu notta da aynısı yapıldı [G] |
| Web erişimi çöktü | Araç hatası | Sonuç daraltıldı; "yeni doğrulama yok" dendi; hafızadan olgu üretilmedi | `actual…/A0 §6`; `contrastive…/I5 §2` |
| Sıra önerisi aşırı belirlenmişti | Erken bağlanma | Her kapanıştan sonra yeniden seçim | `C:C7 §13` |
| Aynı-model inceleme, bağımsızlık gibi sunulabilirdi | Doğrulama sınıfının karışması | Her kapanış "same-model adversarial review; NOT independent replication" diyor | tüm X7'ler |

---

## 5. Önceki notların iddialarıyla karşılaştırma

- **O10 (§5 ve kapsam satırı):** "Foundation, kısmen: … CONTROL-CONSTRAINT-SYNTHESIS.md (370 satırın 1–200'ü)". Bu boşluk kapandı: dosyanın tamamı ve K0–K7 okundu. Okunmayan kısımda "Coverage / alternate-path / bypass", Anthropic "agent-to-agent route" örneği ve "Why no immediate children" vardı. O10'un "kapı (gate) ayrışımı hook tasarımı için" çıkarımı **doğrulanır**. Ama kontrolün asıl yükü kapı değil, **korunan etki ile yaptırım noktası kapsamının ayrılmasıdır** (M3). O10 bunu vurgulamıyordu.
- **O10 "Hiçbiri canlı ajanda sınanmadı; hepsi aynı asistanın analizi"** doğrulanır. Tek ek: Foundation'da gerçekten **koşulmuş** kurgu testleri de var: `persistent-adaptation/checks` 15+4, `returned-influence/G7` 7, `06 checks` (4 kötü varyant), `07 checks` (4 kurgu + 5 yanlış kural). Kaynak bunları yalnız kurgulanan ilişkiler için geçerli sayıyor [K].
- **O10 "stored lesson != adaptation" öğrenme ölçütü için** doğrulanır ve somutlaşır: taşıyıcı zinciri ve prob kirlenmesi (M7).
- **BRIEF'in öncülü** ("hangi sonuç hangi mekanizmaya dönüşmeli") Foundation'ın "otomatik eşleme yok" ilkesiyle gerilimlidir. Bu not, sonuçları *mekanizmanın taşıması gereken ayrım ve yasak çıkarım* olarak okudu (§1). Mekanizma biçimleri [Ç] ve DevOS'ta sınanmalı.

### 5.1 Canlı örnek: ana oturumun kendi kapılarına M3 kapsama sorusu

`DERSLER.md` üç hook'u DevOS'a aktarılacak ilk mekanizmalar olarak sayıyor ("Bu derslerin DevOS'a aktarımı"). Foundation'ın kontrol sonucunu bunlara uyguladım. Kod ve ayar okundu [G]; atlatma yolları **sınanmadı** [Ç]. DERSLER'deki "canlı sınandı" kaydı, sınanan yol için doğrudur. Eksik olan kapsama iddiasıdır: "one path blocked != protected effect controlled" (`C:control-constraint/STATE.md`).

| Kapı | Korunan etki | Kapatılan yol [G] | Açık kalan bilinen yollar [Ç] | Öneri [Ç] |
|---|---|---|---|---|
| `kapsam-kapisi.py` | KAPSAM kapanmadan yapı kararı ya da DevOS dokümanı yazılmaz (L5, L8) | `PreToolUse` matcher'ı `Write\|Edit\|MultiEdit`. Betik yalnız `file_path` şu kalıba uyarsa durdurur: `/devos/(MIMARI-KARARLAR\.md\|DEVOS\.md\|dokuman/)` | Bash ile yazım (`cat >`, `cp`, `sed -i`, `tee`). GitHub MCP'nin `create_or_update_file` ya da `push_files` aracıyla uzak dala doğrudan yazım. Kararın başka bir dosya adına yazılması. Hook'u kurulu olmayan uzak oturum (`create_session`). | Kontrol kaydında (M3) bu yollar "kapatılan / açık" diye yazılır. Bash çağrısının komut metni korunan yollar için taranır. Asıl yaptırım push anında, değişen dosya listesiyle yapılır (M12 adım 2). Kapsama "unknown" diye raporlanır. |
| Aynı kapının ölçütü | KAPSAM gerçekten kapandı | `KAPSAM.md`'de `SÜRÜYOR`, `BOŞLUK VAR` ya da `SIRADA` dizesi aranır | Satırı `TAMAM` yapan oturum, kapıdan geçmek isteyen ana oturumun kendisidir. Kapı kaydı denetliyor, niteliği değil: "record says it holds != standing holds" (`C:composite-standing/KEY.md`). `K0 §8`'deki "producer self-approves" durumu budur. | Satır kapanışı, notun kapsam bölümüne atıf taşır (M1 kaydı gibi). Kapanışı ikinci bir okuyucu denetler (M2). |
| `ajan-standart-kapisi.py` | Her alt işçi STANDART'ı ilk okuma olarak alır (L2) | Matcher `Agent`. Görev metninde `STANDART.md` dizesi aranır. | Dizenin geçmesi okunduğunu göstermez: "signal delivered != signal exposed/read != signal operatively used" (`G2 §3`). Başka devir yolları da var: `create_session` ve `send_message`, zamanlanmış rutin, Bash'ten başsız `claude -p`. | Alt ajanın dönüşünde STANDART'tan bir denetim sorusuna yanıt istenir (okuma probu, M7). Diğer devir yolları kayda "açık" diye yazılır. |
| Kalıcılık | Hook'lar her oturumda etkin | `~/.claude/settings.json` (kullanıcı düzeyi) ve `kur.sh` | Makine geri alınınca hook'lar gider. Yeniden kurmayı hatırlatacak SessionStart hook'u da onlarla gider; geriye yalnız STATE ve DERSLER'deki metin kalır. `kur.sh`'deki bozma testleri yalnız ajan kapısını sınıyor. | Taşıyıcı, ortamın kendiliğinden yüklediği yere konur: proje ayarları ya da ortam kurulum betiği (O11b/O11c doğrulamalı). Her kurulumda her kapı için bozma testi koşar. Dayanaklar: "configuration itself needs regression evaluation" (`K0 §5`); "retained after the claimed lifecycle transition" (`D3 §2`). |

**Bir gözlem daha** [G]: Bu notun yazımı sırasında bağlam sıkıştırıldı. `oturum-hatirlat.sh` çıktısı bu alt ajanın bağlamına da geldi. Demek ki kullanıcı düzeyi SessionStart hook'u alt ajan oturumunda da çalışıyor; PreToolUse hook'larının alt ajan çağrılarında çalışıp çalışmadığını doğrulamadım [B]. Mesaj ana oturuma yazılmış ("SIRADA olan kalemleri başlat"), ama alt ajan ajan açamaz ve bu işi yapmamalı. Hook alıcının rolünü ayırmıyor. M6'daki `tuketici` alanı ve M10'daki rol niteleyicisi tam burada gerekiyor: hatırlatma, alıcının rolüne göre (ana oturum ya da alt ajan) ayrı metin basmalı. Hook girdisinde alt ajanı ayırt eden bir alan olup olmadığı O11b'de doğrulanmalı [B].

Bu tablo, DevOS kontrol kaydının (M3) ilk dört satırı olabilir.

---

## 6. DevOS'un kendi kanıtıyla kapatması gerekenler

Foundation'ın hedefe özgü dediği ve genel araştırmayla çözülemeyecek sorular [K] (`C:OPEN-QUESTIONS.md`: "causal identification, transfer/interference, all-path control, opaque feedback use, persistence/support horizons and benefit"):
1. **Kapsama eşiği:** DevOS kontrollerinde hangi yollar "önemli" sayılır (`control…/OPEN-QUESTIONS` 2–3)? → M3 test kataloğu ve risk sınıfı.
2. **Opak tüketici:** Bir kuralın ya da dersin model bağlamında gerçekten kullanıldığı nasıl kanıtlanır (`returned-influence/OPEN-QUESTIONS` 1; `persistent-adaptation/OPEN-QUESTIONS` 1)? → hook günlüğü, prob ve iz; kalıntı "unknown" kalabilir.
3. **Kalıcılık ufku:** Yeni oturum, sıkıştırma ve makine geri alınması sonrası taşıyıcının yüklendiği nasıl ölçülür (`persistent…/OPEN-QUESTIONS` 2, 7)? → M7 prob seti.
4. **Sürüm ve model taşınması:** Model ya da sağlayıcı değişince eski etki iddiasının geçerliliği nasıl düşürülür (`contrastive…/OPEN-QUESTIONS` 5, 10)? → M1 bağımlılığına "model sürümü" eklenmesi.
5. **Görev ayrılığı:** Aynı model, ortak bağlam ve devir varken asgari bağımsızlık nedir (`control…/OPEN-QUESTIONS` 9)? → M2 kalıntı risk kaydı.
6. **Kural yayılımı:** Yüksek etkili bir işlem için yeni kontrol ne zaman "yeterince yayılmış" sayılır (`transition-propagation/OPEN-QUESTIONS` 11)? → M5 + M1.
