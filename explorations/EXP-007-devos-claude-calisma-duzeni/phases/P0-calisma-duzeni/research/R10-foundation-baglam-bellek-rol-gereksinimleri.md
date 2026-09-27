# R10 — Foundation: bağlam, bellek ve kalıcı rol tasarımının karşılaması gereken ayrımlar

**Tür:** Alt ajan notu (model çıktısı), EXP-007 P0.3. Salt okuma ile çalışıldı; yalnız bu dosya yazıldı.
**Tarih:** 27 Eylül 2026. Bütün repo okumaları bu tarihte yapıldı; web kullanılmadı.
**Görev tanımı:** `briefs/ORTAK.md` ve `briefs/R10.md`.
**Beslediği karar:** METHOD v1'de bağlam, bellek ve kalıcı rol alt sistemlerinin hangi ayrımları taşıması gerektiği ve neyin yanlış birleştirilmemesi gerektiği.

## 0. Soru, kaynaklar, okuma kapsamı

### 0.1 Soru
Foundation bağlam yönetimi, bellek yönetimi ve kalıcı rol yapısı için hangi ayrımları ve gereksinimleri koyuyor? Standart seviyede bir tasarım neyi ayırt edebilmeli, neyi yanlış birleştirmemeli? R04 Foundation'ı genel olarak taradı. Bu not R04'ü tekrar etmez; aynı konuya değdiği yerde "R04 (b3)" gibi atıf yapar ve bir kat aşağı iner.

### 0.2 Kanıt gücü ve etiket düzeni
- **Foundation'ın kanıt türü:** Repo içi analitik araştırmadır. Aynı asistan üretmiş, Batu değerlendirmiştir. Dış birincil kaynaklar yalnız sınama ("holdout", "falsifier") için kullanılmıştır. Karşı incelemeler aynı modelle yapılmıştır. Bağımsız tekrar ve canlı ajan deneyi yoktur. Kaynağın kendi sözü: "independent second-researcher/model replication: **not performed**" (IS-KEY, Verification status); "No ... live worker/learner/LLM experiment or independent cold-start trial is supplied" (STATE, History and verification limits). Yani bu kanıt ne tedarikçi iddiasıdır, ne topluluk pratiğidir, ne de bağımsız ölçümdür.
- **Etiketler:** Tablolarda "Foundation diyor" sütunu **[kaynak diyor]** demektir: Foundation'ın iddiasıdır ve gücü yukarıdaki sınırla bağlıdır. "EXP-007 için" sütunu **[çıkarım]** demektir: Foundation'ı bu işe benim uygulamamdır. Düzyazıda istisnalar ayrıca yazılır: **[gözledim]**, **[varsayım]**, **[bilinmiyor]**.
- **Claude Code iddiaları:** Yalnız R01 üzerinden verilir. R01'in kendi etiketi korunur: `documented_for_cloud` belge buluta uygulandığını söylüyor; `documented_generic_unclear_cloud` belge genel, buluttaki durumu belirsiz.

### 0.3 Kısaltmalar
Yollar `research/soul-foundations/` altındadır.

| Kısaltma | Yol |
|---|---|
| STATE, RUA | `STATE.md`, `RESEARCH-USE-ALIGNMENT.md` |
| REUSE, DH, CA, CSC | `08_foundation-sufficiency-reuse-review/` altında REUSE, DISCUSSION-HANDOFF, CASE-AUDIT, COLD-START-CHECK-2026-09-17 |
| AQ6 | `02_adequacy/findings/06-soul-vs-development-os-adequacy.md` |
| IS, IS-KEY | `03_ground-deepening/grounds/information/informational-state/synthesis/INFORMATIONAL-STATE-SYNTHESIS.md`, aynı klasörde `KEY.md` |
| IDS | `…/information/informational-dynamics/synthesis/INFORMATIONAL-DYNAMICS-SYNTHESIS.md` |
| S5, U5, E5 | `…/informational-dynamics/selection-exposure/` altında S5; `use-conditioned-selection-set-adequacy/U5-…`; `consumer-relative-exposure-availability/E5-…` |
| R1, R2, R6 | `…/derivation-transformation/re-expression-semantic-transfer/` |
| W6 | `…/derivation-transformation/inferential-construction-claim-warrant/W6-…` |
| M1, M2, M5 | `…/derivation-transformation/maintained-information-revision/` |
| F2, F3, F6 | `…/informational-dynamics/formation-acquisition/` |
| I (I1–I5) | `07_selection-dynamics-integration-review/SYNTHESIS.md` |
| REC, REC-KEY | `01_verticals/records-artifacts/synthesis/RECORDS-VERTICAL-SYNTHESIS.md`, `01_verticals/records-artifacts/KEY.md` |
| REC-FS, REC-CTS | `…/records-artifacts/synthesis/current/FAILURE-SURFACES.md`, `…/current/CHANGE-TIME-STANDING.md` |
| REC-CR | `…/records-artifacts/synthesis/COLD-READ-CURRENTNESS-COUNTERCHECK.md` |
| AV | `01_verticals/actors/synthesis/ACTORS-VERTICAL-SYNTHESIS.md` |
| AF-IRP, AF-CAO, AF-RDA, AF-RA, AF-AOD, AF-NH | `01_verticals/actors/findings/` altında IDENTITY-ROLE-PARTICIPATION, CAPABILITY-AUTHORITY-OBLIGATION, REPRESENTATION-DELEGATION-ATTRIBUTION, RESPONSIBILITY-ACCOUNTABILITY, ACTION-OMISSION-DECISION, NONHUMAN-DISTRIBUTED-AGENCY |
| AOQ | `01_verticals/actors/OPEN-QUESTIONS.md` |
| AG, AD, A3 | `03_ground-deepening/grounds/actors/` altında `synthesis/ACTORS-GROUND-AUDIT-SYNTHESIS.md`, `DEFERRED-RELATIONS.md`, `A3-NEW-CANDIDATE-STUDY-HOLDOUTS.md` |
| WV, WG | `01_verticals/work/synthesis/WORK-VERTICAL-SYNTHESIS.md`, `03_ground-deepening/grounds/work/synthesis/WORK-GROUND-AUDIT-SYNTHESIS.md` |
| WF-CSC, WF-FU | `01_verticals/work/findings/` altında CONTROL-STATE-CLOSURE-AND-RECOVERY, WORK-FRAMES-AND-UNITS |
| BND, CS, CC | `05_relation-control-composition/` altında `relational-binding/synthesis/…`, `composite-standing/synthesis/…`, `control-constraint/synthesis/…` |
| TP | `05_…/transition-effect-feedback/transition-propagation/synthesis/TRANSITION-PROPAGATION-SYNTHESIS.md` |
| FA, G6, RI | `05_…/feedback-adaptation/synthesis/FEEDBACK-ADAPTATION-SYNTHESIS.md`; `returned-influence/G6-…`; `returned-influence/synthesis/RETURNED-INFLUENCE-SYNTHESIS.md` |
| D1, D2, D3, D6 | `05_…/feedback-adaptation/persistent-adaptation/` altındaki D dosyaları |
| B1 | `06_integration-frontier-review/B1-PARENT-INTEGRATION.md` |

EXP-007 dosyaları adlarıyla anılır: A003, U004, U006, R01, R04, R06. "U002-A" EXP-006'nın `sources/U002-cloud-plan-and-autonomy.md` dosyasıdır. "P2-01" `origin/main` üzerindeki (`ed2bf6e`) `explorations/EXP-006-development-os-calisma-duzeni/work/P2-01-named-role-contracts.md` dosyasıdır.

### 0.4 Sürüm bağı
- Okuma başladığında dal `084a25c`'deydi. Okuma sürerken ana oturum `3e6cf6b`'yi (K-010) kaydetti. Bu commit Foundation'a ve `briefs/` klasörüne dokunmadı; `git diff 084a25c 3e6cf6b -- …/briefs/` boş döndü. **[gözledim]**
- Foundation dosyaları görünür geçmişte değişmemiş: `git log -1 -- research/soul-foundations` sığ klonun kökü olan `23280ab`'yi gösteriyor. **[gözledim]**
- Örnek blob kimlikleri: STATE `6d1c3db`, REUSE `b92c29d`, IS `8d53f5a`, I `c2b1138`, REC `76fb18f`, AV `5ae5260`, A3 `f2a3ce9`, A003 `38f1461`.

### 0.5 Okuma kapsamı

| Kapsam | Dosyalar |
|---|---|
| **Tam** | STATE, REUSE, RUA, DH, CA, CSC, AQ6; IS ve IS-KEY; S5, U5, E5; I; R1, R2, R6, W6; M1, M2, M5; F2, F3, F6; REC-KEY, REC, REC-FS, REC-CTS, REC-CR; AV, AG, AD, AOQ; AF-IRP, AF-CAO, AF-NH; WV, WF-CSC; BND, CS, TP; FA, G6, RI; D1, D2, D3, D6 ve Persistent Adaptation güncel sentezi; B1. EXP-007: ORTAK, R10 ve diğer dört görev tanımı, U004, U006, A003, R02, R03, R04, R06; README, STATE, DECISIONS ve P0 README (084a25c hâli) ile K-010 farkı. |
| **Kısmi** | A3 (§2.2–§7 tam; §1–§2.1 yalnız başlık düzeyi); AF-RDA, AF-RA, AF-AOD (bulgu bölümleri; kanıt bölümlerinin bir kısmı); WF-FU (§5, §6, §8); WG (§§2–7); CC ("Shared semantic core"dan dış sınamalara kadar); IDS (§§1–7); 02_adequacy STATE (ilk bölüm); Persistent Adaptation STATE (ilk bölüm); R05 (tablo ve başlıklar); R01 (yalnız bellek ve sıkıştırma satırları); U002-A (alıntının çevresi); P2-01 (§§1–3, DR06–DR09, DR15–DR16, §§5–6). |
| **Okunmadı** | Environment zemini; F1, F4, F5, F7; S1–S4, S6; U1–U4, U6; E1–E4, E6; R3–R5, R7; W1–W5, W7; M3, M4, M6, M5 rakip incelemesi ve kaynak eki; REC kaynak defterleri ve diğer güncel konu dosyaları (OBJECT-IDENTITY, PRESERVATION-CLOSURE, ORGANISATION-RETRIEVAL, RETENTION-DISPOSITION, REQUIREMENT-DERIVATION, MECHANISM-LANDSCAPE, COMPLETENESS); Actors A0–A2, A4–A6 ve COMPLETENESS-OMISSION-CHECK; Work'ün INTAKE ve COORDINATION bulguları; nedensellik yaprakları; 08 SYNTHESIS, RIVALS-AND-REUSE ve COMPLETION-AND-RESIDUALS (bunlar yalnız R04 üzerinden biliniyor); studies (Carbon Layer bellek değerlendirmesi R09'un alanı); kontrol programları (hiçbir test çalıştırılmadı). |
| **Erişilemedi** | Yok. |

**Yol sorunu teyidi:** R04'ün "REUSE'daki Records yolu kırık" tespitini kontrol ettim. `information/INDEX.md` içinde "records" geçmiyor; Records'a `01_verticals/records-artifacts/KEY.md` üzerinden ulaşılıyor. **[gözledim]**

## 1. En önemli bulgular

1. **Foundation, "standart seviye"nin iki yönünü de kendi yöntemi olarak taşıyor.** Bir yanda "a simpler arrangement is not adequate merely because it is simple" (REUSE, Research-to-target reasoning) diyor. Öte yanda "`Keep everything forever` is not neutral" (REC §9) diyor. Karar yöntemi de var: önce korunan kullanım belirlenir, sonra her yükümlülük REQUIRED, NOT REQUIRED FOR CURRENT PROFILE ya da UNKNOWN olarak işaretlenir. Gerekli her yükümlülük "failure it prevents" ve "observable acceptance/falsification outcome" ile bağlanır (REC §8). Bu, ORTAK'taki dört sorunun (ne işe yarar, yokluğunda ne bozulur, bedeli ne, ne zaman gereksiz) Foundation'daki karşılığıdır. **[kaynak diyor + çıkarım]**
2. **"Doğru bilgi, doğru zamanda, doğru kelimelerle" Foundation'da üç ayrı sorudur:**
   - kullanım göreli yeterlik (U5);
   - tüketici göreli erişilebilirlik ve zamanlama (E5, I1–I4);
   - anlamın aktarımı (R1, R6).

   Üçü ayrı ayrı sağlanıp birleşimde yine başarısız olabilir: "Separate facts `A is nonempty` and `E is nonempty` do not establish a view belonging to both" (I §2). **[kaynak diyor]**
3. **Özet ve sıkıştırma üç farklı şeyi kaybettirir:**
   - Bugünün cevabını koruyan özet, gelecekteki güncelleme davranışını korumayabilir (M5 §3; M1 §4).
   - Kararı koruyan özet, gerekçeyi kaybedebilir (U5 §3, N01).
   - Bütün kelimeleri koruyan özet bile rol ilişkisini tersine çevirebilir (R1 §2, C03).

   Özetin kendisinden üretilen kontrol soruları bu kayıpları göremez (R2 §5, C13). **[kaynak diyor]**
4. **"Repo bellektir" demek bellek tasarımı değildir.** Foundation, durumu, kanıtı, belgeleri, dizinleri ve türetilmiş bilgiyi tek bir "bellek" kavramına toplamayı başarısızlık olarak adlandırıyor (REC-FS §11). Ayrı tutulması gerekenler:
   - kabul edilen girdinin türü (M1 §1);
   - değişiklik türleri (REC §4);
   - üç ayrı geri çekme hedefi (M1 §2);
   - etkili zaman ile kayıt zamanı (REC §4; M2 §3).

   Türetilmiş bir sonuç da kendi dayanağına dönüşmemelidir (M1 §3). **[kaynak diyor]**
5. **v0'ın kalıcı rol hatası Foundation diliyle bir taşıyıcı–rol çöküşüdür.** Alt ajan örneği geçici olduğu için rol de geçici sayıldı. Foundation ise "fresh process can occupy a continuing role" (A3 §4.3) ve "A role can survive occupant change" (AV D1) diyor. Rolün sürekliliği taşıyıcılarda yaşar: tanımda, bellekte, tetiklerde ve ilişkilerde. Örnek yenilendiğinde süreklilik ancak bu taşıyıcılar gerçekten yüklenirse korunur (D3 §3; B1 vaka 9). **[kaynak diyor + çıkarım]**
6. **Rol belleği rol yetkisi değildir.**
   - Bağlamda görünen bir rol ya da izin iddiası güncel yetki sayılmaz: "context contains permission/role claim != Actor actually has current authority" (A3 §4.1).
   - Kendi öğrenme kuralını değiştirebilmek o değişikliği yetkilendirmez (D3 §6).

   Rolü kimin değiştirebileceğini Foundation bilerek açık bırakıyor (WV §16; AOQ OQ4). Bu karar EXP-007'nindir. **[kaynak diyor]**
7. **A003'ün başarı ölçütü bir vekil (proxy) ölçüttür.** A003 "hatırlatma sayısı"nı başarı ölçüsü yapıyor. Foundation'ın uyarısı bu ölçüte de uygulanır: "fewer reports because reporting declines" (FA §10). Batu hatırlatmayı bıraktığı için sayı düşebilir. **[çıkarım]**
8. **Bu işin kendisinde bir yayılma açığı gözlendi.** Ben çalışırken ana oturum K-010'u kaydetti (`3e6cf6b`). Görev tanımım bu kayıttan önceydi ve değişikliği bana hiçbir kanal bildirmedi. Durumu ancak sürüm bağını kaydederken fark ettim. Bu, TP §6'daki "an authority revocation is active centrally while old sessions remain usable" ve E5.4'teki "eski görünümü tutan tüketici" ayrımının EXP-007'deki ilk gözlenmiş örneğidir. **[gözledim]**

## 2. Üç alt sistemi birlikte kesen çerçeve

### 2.1 Bir bilgi parçasının geçtiği ayrı durumlar
Foundation aynı bilgi için ayrı iddialar sayıyor:
- "source exists != state persists != state is retrievable != state is selected into current context != consumer sees/understands it" (IS §14);
- "Being catalogued, having a locator, being accessible through a path, being included in a current working input and being successfully used are different claims." (S5 §4);
- "signal produced/delivered/read != operative use established" (G6, Required distinctions).

Bellek, bağlam ve rol bu zincirin farklı halkalarını sahiplenir. **[kaynak diyor]**

| Durum | Foundation | EXP-007'deki karşılığı **[çıkarım]** | Hangi alt sistem |
|---|---|---|---|
| Kalıcı | "persistence → survives" (IS §14) | Dosya commit edilip push edilmiş. Commit edilmemiş iş makine geri alınınca kaybolabilir (R01 C15, `documented_for_cloud`). | Bellek |
| Bulunabilir | "Retrievable is claim-relative" (REC §7) | Yol biliniyor, giriş dosyasından erişiliyor, arama işe yarıyor. Arama sonucu çıkmaması "yok" demek değil (REC-CR Senaryo 5). | Bellek ve bağlam |
| Seçilmiş | "which view serves an informational use" (I §2) | Görev tanımına ya da okuma listesine alınmış. | Bağlam |
| Tüketiciye ulaşmış | "Bind the exact informational target, consumer, locus and required mode" (E5.1) | Alt ajan dosyayı gerçekten okumuş; ana oturum sıkıştırmadan sonra yeniden yüklemiş. | Bağlam |
| Yorumlanabilir | "Supported representation is not demonstrated understanding" (E5 §6) | Terimler, kısaltmalar ve A–B–C ayrımı alıcıda da mevcut. | Bağlam |
| Kullanılmış | "produced/delivered/read != operative use" (RI) | Alt ajanın sonucu bu bilgiye dayanıyor ve bu izlenebiliyor. | Bağlam ve rol |
| Davranışa dönüşmüş | "stored lesson != adaptation" (FA §4) | Sonraki oturumda aynı durumda farklı davranıldığı gözlendi. | Bellek ve rol |

Ortamdan iki somut örnek:
- **MEMORY.md'nin yalnız başı yüklenir.** Alt ajan belleği `memory: project` alanıyla `.claude/agent-memory/<ad>/` altında tutuluyor ve MEMORY.md'nin yalnız ilk 200 satırı ya da 25 KB'ı yükleniyor (R01 C8, C10; ikisi de `documented_generic_unclear_cloud`). Bu, konuma göre yapılan bir kesmedir, kullanıma göre bir seçim değildir. 250. satırdaki bir ders saklanmıştır ama tüketiciye ulaşmaz. Foundation'daki karşılığı "E07 distinguishes a complete planned bundle from the budgeted view actually supplied" (S5 §4). **[kaynak diyor + çıkarım]**
- **Sıkıştırma bir yeniden ifadedir.** Sıkıştırma konuşmayı yapılandırılmış bir özetle değiştirir; "Full tool outputs and intermediate reasoning are lost" (R01 C12, `documented_generic_unclear_cloud`). Bulutta sıkıştırma pencerenin ortasında tetiklenir (R01 C11, `documented_for_cloud`); bu ortamda eşik %80'dir (ORTAK). Bu nedenle §3.3'teki özet kayıpları ana oturum için teorik değil, düzenli yaşanacak olaylardır. **[kaynak diyor + çıkarım]**

### 2.2 Durum, bellek, bağlam ve bilgi ayrı şeylerdir
Foundation'ın benimsenen üst düzey hipotezi (02_adequacy STATE: "ACCEPTED on 2026-09-02 as the working top-level research hypothesis") Development OS için şu tespite dayanıyor:
- "Development OS requires fresh sessions to receive bounded role-relevant context without hiding canonical truth." (AQ6, Gap 2)
- "SOUL non-negotiables explicitly distinguish state, memory, context and knowledge."
- "Their **source** can be Records while the assembled context/information state is not identical to the source corpus."

**[kaynak diyor]**

**EXP-007 için:** Üç alt sistemin başarı koşulları farklıdır:
- bellek: gelecekteki kullanım için doğru şeyin korunmuş ve yeniden kurulabilir olması;
- bağlam: şu anki tüketiciye, şu anki kullanım için yeterli ve kanonik gerçeği gizlemeyen bir görünümün ulaşması;
- rol: aynı sorumluluğun yeni örneklerde de aynı sınırlarla sürmesi.

Üçü aynı mekanizmayla, yani repo dosyalarıyla gerçekleşebilir. Ama birinin başarısı ötekileri kanıtlamaz. "Kaydettim" bellek için bir adımdır; bağlam ya da rol için hiçbir şey kanıtlamaz. **[çıkarım]**

### 2.3 Foundation'da standart seviyeyi belirleme yöntemi
- **Önce ne bilinmesi gerektiği çıkarılır:** "First derive what must remain knowable, retrievable and testable for the protected use; only then judge storage/history/search mechanisms." (REC-KEY)
- **Karar üç durumlu, kabul ölçütlü ve yeniden değerlendirilebilir:** Gereksinim kararı "REQUIRED / NOT REQUIRED FOR CURRENT PROFILE / UNKNOWN / NEEDS EVIDENCE" durumlarından birini alır. Gerekli her yükümlülük şunlara bağlanır: "protected use or external mandate; failure it prevents; required assurance/depth; satisfaction mode/dependency; observable acceptance/falsification outcome". Profil "re-appraisal when assumptions/context/constraints/users/horizon/transformations/retrieval requirements materially change" ister (REC §8). **[kaynak diyor]**
- **"Gereksiz" demenin meşru koşulu:** "A simple profile can merge dimensions that cannot vary independently for that use." (REC-CTS); "A local current-only state can legitimately discard its history when no protected use requires it." (M2 §6). **[kaynak diyor]**
  - EXP-007 için: Bir bileşen ancak korunan kullanım için o boyut bağımsız değişemiyorsa gereksiz sayılabilir. "Şimdilik yeter" bir gerekçe değildir. Batu'nun ölçütü de bunu istiyor. **[çıkarım]**
- **Açık gereksinimler yerel tercihle kaldırılamaz:** "Local context cannot waive a valid external obligation by preference." (REC §8) **[kaynak diyor]**
  - EXP-007 için: Batu'nun K-007'de açıkça koyduğu gereksinimler (bağlam, bellek, kalıcı rol) bu anlamda dış yükümlülüktür; yerel "yeterli" kararıyla kaldırılamaz. **[çıkarım]**
- **Gerekli yükümlülük yeni dosya demek değildir:** Gerekli bir yükümlülük "intrinsically; externally/linked; through relations; through inherited context; reconstructably; by system/control capability" yollarından biriyle karşılanabilir. "`Required` therefore does not mean `object-local metadata field`." (REC §8) **[kaynak diyor]**
  - EXP-007 için: Standart seviye daha çok dosya demek değildir. Her yükümlülüğün bir yerde, doğrulanabilir biçimde karşılanması demektir. Bu, A003'ün "repo ağırlaştı" teşhisiyle çelişmez. **[çıkarım]**
- **Aşırı uçlar da standart değildir:** "Do not create a component/file/requirement for every leaf or place the full research history in every context." (RUA, Specialization is not exhaustive form filling); "A memory need does not automatically imply a vector database." (REUSE) **[kaynak diyor]**

## 3. Bağlam yönetimi

### 3.1 "Doğru bilgi, doğru zamanda, doğru kelimelerle": Foundation'daki karşılığı
Batu'nun birebir cümlesi şöyle (U002-A): "iyi girdi oluşması için bir zincir ya da döngü içinde çalışan rollerin doğru bilgiyi, doğru zamanda, doğru kelimelerle alması gerekir, yani iyi bir token kümesi verilmesi gerekir LLM'e ki çıktısı da o seviyede kaliteli olsun, her ajanın çıktısı da işin devamlılığı için daha sonra girdi olarak kullanılabilir".

Cümlede beş ayrı parça var. Foundation her birini ayrı bir soru olarak araştırmış.

| Batu'nun parçası | Foundation diyor **[kaynak diyor]** | Tasarım gereksinimi **[çıkarım]** |
|---|---|---|
| **"doğru bilgi"** | Yeterlik kullanıma bağlıdır: "A view's adequacy therefore belongs to a use relation, not to its file once and for all." (U5 §2). İyi parçalar iyi bir küme demek değildir: "Several individually relevant documents can repeat the same evidence while omitting a blocker, exception or complementary premise." (S5 §3). Parçalar birlikte değer taşıyabilir: "complementary information whose individual gain is zero while the pair is worthwhile" (U5 §5). İddianın niceliği önemlidir: "Missing a counterexample is not the same observation as showing it cannot exist." (U5 §4). Payda iddiaya uymalıdır: "all listed sources checked != all materially relevant sources listed" (F2 §1). | Her bağlam paketi (görev tanımı, devir notu, rol bağlamı) hangi kararı beslediğini, açık alternatifleri ve kabul edilebilir kaybı yazar. Paket parça parça değil küme olarak sınanır: engel, istisna ya da karşı kanıt eksik mi? "Hiç yok" ya da "hepsi" diyen iddialar arama kapsamını da taşır. |
| **"doğru zamanda"** | Zamanlama ve sıra erişimin parçasıdır: "State timing/order, permitted waiting, dependency and resource conditions, horizon" (E5.2). Foundation'ın kendi gözlemi: "available research need not be applied at the right time" (STATE, Important correction). Bir karşı örnek: "no permitted working procedure brings the required distinctions to the actual decision point" (CA C3). Tazelik tek bir koşul değildir: "Latest, currently applicable, mutually coherent and appropriate as-of are different conditions." (S5 §4). Okumaların birbiriyle uyumu ayrıca kanıt ister: "individually legitimate reads can require an additional joint-consistency argument for a particular use" (I §5; I4). Geri bildirim de zamanında gelmelidir: "feedback occurred != feedback current enough for decision" (FA §8). | Bağlam kararın verildiği andan önce gelmeli. Bu anlar adlandırılır: görev tanımı yazımı, sonuç birleştirme, plan revizyonu, kapanış, Batu'ya sunum. Her paket hangi commit'e göre hazırlandığını yazar. Bir alt ajanın okuduğu dosyalar aynı commit'ten gelir. Taban commit değişirse çalışan tüketiciler işaretlenir; §0.4'teki K-010 olayı bunun gerekçesidir. |
| **"doğru kelimelerle"** | Alıcının yorum kaynakları iddianın parçasıdır: "the identical code A7 means blocked in one stipulated dictionary and ready in another" (R1 §4). Aynı kelimeler başka bir ilişki kurabilir: "C03 swaps reviewer and approver assignments ... Every token is retained, but the role relation changes." (R1 §2). Kip kaybı iddiayı değiştirir: "someone reports X" ifadesi "X is established"a dönüşebilir (IS §8). Neler korunmalı: "Preserve material relations, order, scope, modality, attribution and unresolved alternatives; a bag of tokens cannot establish them." (R6 §2). Doğru baytlar anlama demek değildir (E5.5). | Ortak sözlük alıcının erişebileceği bir yerde durmalı, yalnız ana oturumun kafasında değil. Kanıt dili (kaynak diyor, gözledim, çıkarım...) her yeniden ifadede korunur. Kim yaptı, kim denetledi gibi rol ilişkileri açık yazılır. Batu'nun sözü ile yorumu karışmaz (A003'teki A–B–C ayrımı). Kelime kayması da anlam kaybıdır: "motivasyon" kelimesinin "başarı yönü"ne dönmesi (R02) buna bir örnektir. |
| **"rollerin ... alması"** | Tüketici iddianın parçasıdır: "Consumer identity can be a person, account, process, session or invocation, depending on the claim. Availability to one does not by itself establish availability to another." (E5 §2). Tüketiciler birleştirilmez: "Do not pool consumers, branches, sessions or times" (I2). Alıcının zaten sahip olduğu bilgi de sayılır: "do not require every new handoff to reproduce everything the recipient already has; equally, do not assume unobserved model knowledge, a forgotten earlier session or another worker's private state as that side information." (I §3) | Bağlam her tüketici için ayrı tasarlanır. Bu tüketiciler birbirinden farklıdır: sıkıştırma sonrası ana oturum, alt ajan, yeni oturum ve Batu. Her paket tüketicinin zaten neye sahip olduğunu varsaydığını yazar ve bu varsayım sınanır. Örneğin rol dosyası ya da CLAUDE.md gerçekten yüklendi mi? Bu satır R04 (b2)'yi derinleştirir: R04 "yol içerik değildir" demişti; burada ek olarak "alıcıda ne var" sorusu ekleniyor. |
| **"her ajanın çıktısı ... girdi olarak"** | Türetilmiş sonuç yeni dayanak olmamalı: "Reusing an old derived b as an unquestioned new premise regenerates a and preserves the obsolete pair." (M1 §3). Yenilik türleri ayrıdır: "Token/receiver novelty, origin-episode novelty, content novelty and independent evidence are not interchangeable." (F6). Görünüm kaynağın yerine geçmemeli: "A view/output must not silently stand for a different source/version/standing or support stronger claims than its binding, coverage and freshness justify." (REC §6) | Bir sonraki girdiye giren her çıktı şunları taşır: kökeni (hangi ajan, hangi görev tanımı, hangi kaynaklar), kipi ve hangi sürüme göre hazırlandığı. Türetilmiş bir not, kaynağına dönülmeden öncül yapılmaz. Birkaç ajanın aynı şeyi söylemesi doğrulama sayılmaz. |

### 3.2 R04'te bulunmayan başka bağlam ayrımları

- **İhtiyaç anında okumak meşru bir yeterlik yoludur.**
  - Foundation: "K06 shows a contingent two-read strategy succeeding where every fixed two-item bundle fails" (U5 §5). Ayrıca: "A viable permitted read path can meet an on-demand contract without eager copying. A particular invocation can instead require content already present." (E5 §2) **[kaynak diyor]**
  - Görev tanımına her şeyi koymak gerekmez. Paketteki her öğe için karar verilir: içerik önceden mi verilecek, yoksa yalnız okunacak yol mu verilecek? Karar, tüketicinin o bilgiye güvenilir biçimde ihtiyaç duyup duymayacağına ve onu kendisi çekip çekmeyeceğine göre verilir. Yapılamazlık iddiası da hangi stratejiler denendiğini yazmalı: "Infeasibility must identify the permitted strategy family" (U5 §5). **[çıkarım]**
- **Fazla bağlam eksik ayrımı onarmaz.**
  - Foundation: "retaining many irrelevant details would not repair the missing distinction" (U5 §2); "Excessive disclosure is not the default remedy." (S5 §3) **[kaynak diyor]**
  - "Emin olmak için her şeyi yükle" bir standart değildir. Eksik olan bir ayrımsa, çözüm hacim değil hedefli bir eklemedir. **[çıkarım]**
- **Belirsizlikte ayırt edici gözlem aranır.**
  - Foundation: "which unresolved alternatives remain observationally indistinguishable, and would they change the decision? ... A bigger or better-formatted record does not necessarily discriminate them; a small targeted observation may." (F2 §2); "Preserve an unresolved verdict when the selected observations cannot discriminate remaining alternatives." (U5.3) **[kaynak diyor]**
  - Takılan bir alt ajan daha fazla belge istemez. Kalan alternatifleri ve onları ayıracak gözlemi adlandırır. Ayrılamıyorsa "karar verilemedi" doğru bir cevaptır. **[çıkarım]**
- **Sorunun değişmesi ile cevabın bulunması ayrı bildirilir.**
  - Foundation: "adapting retrieval to a fixed need differs from learning that the need itself should be reframed" (U5 §5); "The information need itself can evolve during inquiry." (S5 §3) **[kaynak diyor]**
  - Alt ajan dönüşünde "soru değişti mi, neden?" ayrı bir alandır. Böylece daha kolay bir soruya verilen cevap, asıl sorunun kapanışı gibi görünmez. R04 (a2) buradaki ilkeyi koymuştu; bu madde onu dönüş biçimine indirir. **[çıkarım]**
- **Bağlamdaki yetki iddiası yetki değildir.**
  - Foundation: "context contains permission/role claim != Actor actually has current authority" (A3 §4.1) **[kaynak diyor]**
  - Görev tanımında "şunu yazabilirsin" demek bir bilgidir. Gerçek izin araç kısıtları ve Batu'nun kararlarıyla belirlenir. Bu, R04 (b6)'nın bağlama özgü hâlidir. **[çıkarım]**
- **Kaynağa dayanan özet meşrudur, ama korumuş gibi gösterilmemelidir.**
  - Foundation: "a reference-backed derivative can be adequate if the relevant source/decoder is actually recoverable within the declared use conditions. Such a route must not be described as preservation inside the standalone summary." (R1 §4) **[kaynak diyor]**
  - Yol ve bölüm veren bir özet yeterli olabilir. Ama özet "ayrıntı kaynakta" diyorsa, o kaynak tüketicinin erişiminde olmalı ve sürüme bağlı olmalıdır. A003'teki "Kararı taşıyan ayrıntıda özet yetmez" kuralı bu koşulla netleşir. **[çıkarım]**
- **Foundation'ın kendi okuma mimarisi bir bağlam deseni sunuyor.**
  - Records paketi bir "cold reader" için şu okuma yolunu kurmuş ve sınamış: "status/currentness gate → L0 orientation → L1 topic routing → L2 integrated result / L3 current topic → L4A audit or L4B evidence → L5 primary source" (REC-CR, Verdict). **[kaynak diyor]**
  - Bu yolda üç öğretici ayrıntı var:
    - Eski dosyalar kendilerini tarihsel olarak işaretliyor: "Do not infer currentness merely from a filename or because search surfaced a legacy synthesis first." (Records synthesis README). **[kaynak diyor]**
    - Denetim yolu ile kanıt yolu ayrı: "A countercheck is not evidence independence; a ledger is not a primary source." (aynı yer). **[kaynak diyor]**
    - Derinlik kelime sayısıyla ölçülmüyor: "`Deeper` means stronger contextual/audit recovery, not simply more words in each next file." (REC-CR R4). **[kaynak diyor]**
  - A003 §3.4'teki "giriş dosyası → harita → özgün bölüm" yolu bunun üç katlı bir hâlidir. Eksik olanlar: güncellik kapısı, kendini tarihsel diye işaretleyen dosyalar ve denetim–kanıt yollarının ayrılması. **[çıkarım]**

### 3.3 Özet ve sıkıştırma neyi kaybettirir
R04 (b3) genel ilkeyi koymuştu: kip, kapsam, köken, açık alternatifler, tarih ve kaynak bağı korunmalı; eksik ile desteksiz ek ayrı ayrı kontrol edilmeli. Bu tablo aynı ilkenin altındaki **kayıp mekanizmalarını** ve bunların EXP-007'de nerede ortaya çıkacağını ekler. EXP-007'de dört tür özet var:
- alt ajan dönüşü;
- ana oturumun birleştirmesi;
- sıkıştırma özeti;
- devir notu ya da STATE.

| Kayıp | Foundation diyor **[kaynak diyor]** | EXP-007'de nerede **[çıkarım]** | Nasıl yakalanır **[çıkarım]** |
|---|---|---|---|
| Doğru ama zayıflatılmış özet, engeli düşürür | "A derivative asserting only completion is a source-supported weakening, yet cannot settle the blocker question." (R2 §1, C02) | Alt ajan "çekinceli tamam" der, birleştirmede yalnız "tamam" kalır. STATE'te "R07 tamam" yazılır ama çekincesi yazılmaz. | Dönüş biçiminde ayrı bir engel ve çekince alanı. Kaynaktan özete doğru "engel var mıydı?" sorusu. |
| Desteksiz daraltma; çelişkinin uzlaşmaya çevrilmesi | "Re-expressing two remaining alternatives as one confident answer is unsupported narrowing unless a legitimate additional basis is introduced and marked." Ayrıca: "A source that records conflicting assertions can be faithfully represented as a conflict; it need not be flattened into a supposedly coherent consensus." (R1 §3) | R07–R11 birleştirilirken iki notun çelişkisi sessizce "uzlaştırılır". METHOD taslağı tek bir sesmiş gibi yazılır. | Çelişkiler ayrı bir bölümde tutulur. Seçim yapıldıysa hangi ek temele dayandığı yazılır. |
| Kelimeler korunur, ilişki ya da sıra bozulur | "C03 swaps reviewer and approver assignments ... Every token is retained, but the role relation changes." C04: iki adımın sırası değişince sonuç değişir (R1 §2). | "X'i Y denetledi" ifadesinin "Y'yi X denetledi"ye dönmesi. Pilot sırası ya da önkoşul sırası. | Rol ilişkisi ve sıra, özetin ayrı yapısal alanları olur; serbest metne gömülmez. |
| Kip kaybı | "It can turn `someone reports X` into `X is established`, or `forecast X` into `X happened`." (IS §8) | Bu işte yaşandı: bir alt ajan raporu "alt ajanlar üç kat iç içe çalışabilir" dedi, ortamda bu kapalıydı ve ana oturum kontrolle yakaladı (A003 §3.3). Belgeye dayanan bir iddianın "ortam böyle" diye aktarılması da aynı türdendir (R01'in bulut etiketleri bu yüzden var). | Kanıt etiketi özetten özete taşınır ve düşürülmez. |
| Karar korunur, gerekçe ya da ikinci destek kaybolur | "N01 keeps the action HOLD in two records but loses which recorded reason applies." N02: seçilen alt küme, sonucu koruyan başka bir tanığı kaybeder (U5 §3). | DECISIONS'ta karar durur, gerekçesi durmaz. Bir iddianın tek kaynağı yazılır; o kaynak geri çekilince, iddianın başka dayanağı olup olmadığı bilinmez. | Karar kaydı gerekçeyi ve bütün dayanakları taşır. U5.2'ye göre açıklama ve denetim ayrı kullanım profilleridir. |
| Bugünkü cevap korunur, gelecekteki güncelleme davranışı kaybolur | "a summary that preserves today's answer, or even an entire one-step answer profile, is not automatically an adequate substitute for the maintained state when further revision is part of the protected use." (M5 §3). Ayrıca: "A current-answer view must not be silently promoted to a faithful replacement for future revisable knowledge." (I §4) | Sıkıştırma "şu an neredeyiz"i korur. Ama neyin neden reddedildiği, hangi varsayıma dayanıldığı ve neyin kararı yeniden açacağı kaybolabilir. Sonraki revizyon, reddedilmiş bir seçeneği yeniden önerir. | Sıkıştırmadan ve devirden önce dosyaya üç şey yazılır: reddedilen seçenekler ve nedenleri, dayanılan varsayımlar, yeniden açma tetikleri. Tam konuşma kaydı ne gereklidir ne yeterli: "Keeping the entire chronological conversation is neither automatically necessary nor sufficient" (M1 §4). |
| Yorum bağımlılığı kaybolur | "a parser can emit valid syntax while dropping a negation, unit, scope, source identity or uncertainty qualifier." (F3 §1). Ayrıca R1 §4'teki A7 kodu örneği. | K-007, A-04, R04 (b3), "P0.4" gibi kısaltmalar alıcıda tanımsız kalır. "Tamam" kelimesi hangi tamamlanma katını kastediyor, belirsizleşir. | Kısaltmaların ve durum kelimelerinin tanımı alıcının okuyacağı bir yerde durur. |
| Özetin kendisiyle yapılan kontrol kördür | "C13 asks questions only about the surviving completed field after a blocker is dropped. Every such check passes." (R2 §5). Ayrıca: "Source-required omissions and unsupported output additions are different directions" (R6 §2). | Ana oturum alt ajan dönüşünü yalnız dönüşün kendi iddialarına bakarak kontrol ederse her şey tutarlı görünür. | İki yönlü kontrol yapılır. Kaynaktan ve görevden türetilen sorular eksikleri yakalar. Özetten kaynağa gidilerek desteksiz ekler bulunur. |
| Eşik yakınındaki küçük hata büyük karar hatasıdır | "C09 maps 49.6 to 50 ... a decision using >=50 changes." (R2 §4) | Bağlam doluluğu, token bütçesi ya da haftalık limit gibi eşik kararlarında yuvarlanmış sayılar. | Eşiğe yakın durumlarda aralık ya da "karar verilemedi" yazılır. |

**Meşru kayıp da vardır.** Foundation her kaybı yasaklamıyor:
- "An abstraction can legitimately lose detail." (R6 §3)
- "A low-cost orientation may legitimately defer detail to recoverable sources." (R2 §3)

Sınır şudur: "The relevant question family cannot be selected solely by what the derivative happens to contain. Its justification comes from the source task and protected use" (R2 §3). **[kaynak diyor]** Kısacası, neyin korunacağını özet değil kullanım belirler. **[çıkarım]**

### 3.4 Tipik başarısızlıklar: Foundation'ın kendi örnekleri

- **Bilgi vardı ama doğru anda uygulanmadı.**
  - Soru bankası tartışmasında üretim tarafı araştırması mevcuttu ama örnek erken kapatıldı: "useful production-side research existed, but the assistant did not apply that perspective sufficiently before declaring the example complete" (DH §3). Foundation bu dersten şu ayrımı çıkarıyor: "The adequacy of the knowledge, its discoverability and its actual application must remain separable questions." (DH §3) **[kaynak diyor]**
  - R04 bunu genel bir uyarı olarak aktarmıştı. Bağlam açısından yeni olan şu: bu, "doğru zamanda" parçasının başarısızlığıdır. Bulgu, kararın verildiği ana (kapanışa) bağlı değildi. DH aynı yerde bir tasarım ihtiyacı da adlandırıyor: "discover relevant perspectives ... rather than remain anchored to the first salient view". **[kaynak diyor + çıkarım]**
- **Doğru kopyalar daha güçlü bir iddiayı taşımaz.**
  - Tek bir test koşusunun on iki doğru özeti "sistem güvenli" iddiasını taşımaz. "A receipt for the dossier does not show an actor read, understood or accepted it." (CA C1) **[kaynak diyor]**
- **Doğru kaynak, yanlış paket.**
  - "A future research worker may possess correct sources yet give another actor a redundant or incomplete evidence set. It may also choose the right evidence but leave the next actor with only filenames, an old view or missing qualifications." (S5 §7) **[kaynak diyor]**
- **Doğru sonuç, ulaşmayan sonuç.**
  - "may find the right result yet still lack a working source route, applicable version, required decoder or evidence that the next actor received it. Another actor may retain a withdrawn view after source access is closed." (E5 §9) **[kaynak diyor]**
- **Bilgi sistemde var ama karar noktasına gelmiyor.**
  - "information exists across the participants but no permitted working procedure brings the required distinctions to the actual decision point" (CA C3). Aynı durumun bir çeşidi: "a qualified worker lacks the needed information/access" (DH §2). **[kaynak diyor]**
- **Bu işte gözlenen örnekler.**
  - A003 §3.3'teki "üç kat iç içe" kip kaybı. **[kaynak diyor]** (A003)
  - §0.4'teki K-010 taban değişikliği. **[gözledim]**

### 3.5 Bağlam tasarımını sınamak için sorular
1. Bu görev tanımı hangi kararı besliyor ve hangi kaybı kabul ediyor? Paket bir küme olarak engel, istisna ya da karşı kanıt içeriyor mu? (U5.1; S5.3)
2. Alt ajan gerçekte hangi dosyaları, hangi commit'ten ve ne kadarını okudu? Birlikte okunan dosyalar aynı sürümden mi? (E5.3; I4)
3. Tüketicide zaten var sayılan bilgi (rol dosyası, CLAUDE.md, önceki oturumun sonucu) yazılı mı? Gerçekten yüklendiği sınandı mı? (I §3)
4. Sıkıştırmadan sonra ana oturum, daha önce verdiği bir kararın gerekçesini, reddettiği seçenekleri ve yeniden açma tetiklerini dosyalardan kurabiliyor mu? (M5.4; I §4)
5. Alt ajan özetindeki bir iddia, özetin kendisinden değil kaynaktan ya da görevden türetilmiş bir soruyla sınandı mı? Desteksiz ekler ayrıca arandı mı? (R2 §5; R6 §2)
6. Kapanış ya da plan revizyonu anında ilgili araştırma bulgusu o karara getirildi mi, yoksa yalnız bir dosyada mı duruyor? (STATE; DH §3)
7. Görev tanımı yazıldıktan sonra taban değişirse (yeni bir Batu kararı ya da yeni bir STATE), çalışan alt ajanlar ve onların sonuçları nasıl işaretleniyor? (TP §6; E5.4; bu notun §0.4'ü)
8. Aktarılan kısaltmaların ve kanıt etiketlerinin tanımı alıcının erişebileceği bir yerde mi? (R1 §4)
9. "Bulunamadı" ya da "yok" diyen bir dönüş, aramanın kapsamını ve duyarlılığını yazıyor mu? (F2 §3; U5.3)
10. Dönüşte "soru değişti" ile "cevap bulundu" ayrı mı? (U5.5)
11. Paket "şunu yapabilirsin" gibi bir yetki iddiası taşıyorsa, bu iddia bir Batu kararına ya da araç iznine bağlı mı? (A3 §4.1)

### 3.6 Foundation'ın bilerek açık bıraktığı, EXP-007'nin karar vermesi gereken noktalar
- **Hangi ayrımların açıkça taşınacağı:** "The map says what kinds of distinctions can be decision-critical. Later design must decide which are explicit for a given task-specific system." (IS §24) **[kaynak diyor]**
- **Kabul edilebilir çıktı ve kayıp ölçütü:** "The hard substantive task is determining B_u, the candidate states and what counts as evidence for them." (U5 §3). Ayrıca: "Loss tolerance, expected loss and worst-case regret are different contracts. None supplies the correct actual world model or utility function." (U5 §2) **[kaynak diyor]**
- **Durma kuralı ve ihtiyaç keşfi:** "No complete unknown-need-discovery test or universal stopping rule has been established." (U5 §5) **[kaynak diyor]**
- **Gerçek kullanımın ölçülmesi:** "how to measure uptake, reproduce a decision, choose a stability criterion or inspect an opaque consumer. They may require domain work" (G6, Why the leaf retains enough depth) **[kaynak diyor]**
- **Mimari:** Foundation "context/memory architecture" kurmuyor (IS §24). Ayrıca: "No guarantee is made that all Foundation findings will be used, that every source must be preloaded, or that a new infrastructure should be installed." (E5 §9) **[kaynak diyor]**
- **Aktörün gerçek davranışı:** "It does not show that a real actor will notice the relevant condition, choose the right strategy, use the selected content correctly or improve outcomes." (U5 §7) **[kaynak diyor]**

**EXP-007'nin karar vermesi gerekenler [çıkarım]:**
- bağlam bütçesinin dağılımı: ana oturum ile alt ajan arasında ve sıkıştırma eşiğine göre;
- hangi karar anında hangi paketin getirileceği;
- önceden yükleme ile ihtiyaç anında okuma arasındaki sınır;
- "kullanıldı" kanıtının biçimi;
- taban değişikliğinin nasıl bildirileceği.

### 3.7 Bağlam için standart seviye bileşenleri **[çıkarım]**
Bileşenler Foundation'ın ayrımlarından türetildi. Mekanizma seçimi R07–R09'un konusudur.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur (başka alt sistemler dahil) | Bedeli | Ne zaman gerçekten gereksiz |
|---|---|---|---|---|
| **Kullanım sözleşmesi:** her pakette beslenen karar, alternatifler ve kabul edilen kayıp (U5.1) | Yeterliği sınanabilir kılar. | Alt ajan kendi sorusunu kurar. Doğrulamanın ölçütü olmaz (kalite). Kapanış erken ilan edilir (plan). | Görev tanımı başına birkaç satır ve yazanın düşünme süresi. | Kullanımın zaten açık olduğu tek adımlık, geri alınabilir mekanik işlerde. |
| **Tüketici tanımı ve yan bilgi beyanı:** paket kime gidiyor, tüketicide ne var sayılıyor (I2, I3) | Ana oturumun bildiğinin alt ajanın bildiği sanılmasını önler. | Devir notları ya aşırı uzar ya eksik kalır. Rol sürekliliği sessizce kopar (rol). | Paket başına kısa bir "alıcıda var sayılan" listesi ve bir kontrol. | Tüketici aynı bağlamla devam ediyorsa ve arada sıkıştırma olmadıysa. |
| **Sürüm bağı ve ortak anlık görüntü:** commit kimliği, aynı sürümden okuma (S5.4, I4) | Eski görünümün güncel sanılmasını ve farklı zamanlardan okunan dosyaların karışmasını önler. | Bellek güncellemesi eski tabana göre yazılır ve araya giren düzeltme silinir (M2 §4; bellek). | Commit kimliğini yazmak; taban değişince işaret koymak. | Sonucu karar taşımayan keşif okumalarında: "an exploratory title search does not need the same granularity" (S5 §4). |
| **Uç nokta kanıtı:** okuma kaydı (ne okundu, hangi sürüm, ne kadarı) (E5.3) | "Okudum" iddiasını sınanabilir kılar. | EXP-006'daki "Tam" etiketlerinin geri çekilmesi yaşanır (R02 §3). "Bulunamadı" kanıtsız biçimde "yok"a döner. | Dönüş biçiminde bir bölüm; ana oturumun örnekleme kontrolü. | İddia okuma kapsamına dayanmıyorsa. |
| **Kademeli okuma yolu ve güncellik kapısı** (REC-CR) | Yeni oturumun ucuz ama doğru yönlenmesini sağlar. | Eski dosya güncel sanılır; Foundation'da gözlenen "prior central defect" budur. Ana oturum bağlamı gereksiz okumayla dolar ve sıkıştırma sıklaşır (R01'deki "Autocompact is thrashing" uyarısı). | Giriş dosyalarının bakımı; tarihsel dosyaların işaretlenmesi. | Repo birkaç dosyadan ibaretse. EXP-007 için bu koşul geçerli değil. |
| **Yeniden ifade sözleşmesi:** özet, sıkıştırma ve dönüşte kip, köken, çelişki, engel, gerekçe, reddedilenler ve yeniden açma tetikleri; iki yönlü kontrol (R6, R2, M5.4) | §3.3'teki kayıpları önler ya da görünür kılar. | Türetilmiş sonuçlar bellekte dayanağa dönüşür (M1 §3; bellek). Karar gerekçesi kaybolur (plan). | Dönüş şablonu uzar; ana oturumun kontrolü zaman alır. | Özet yalnız yönlendirme için kullanılıyorsa ve kaynak aynı bağlamda erişilebiliyorsa (R2 §3). |
| **Karar anına bağlama:** hangi karar anında hangi bilgi getirilecek (STATE; CA C3) | Bilginin var olduğu hâlde kullanılmamasını önler. | Soru bankası olayı tekrar eder. Batu hatırlatıcı olur (insan iş birliği). | Karar anları için kısa kontrol listeleri; her kapanışta "bu karara hangi araştırma bakıldı" satırı. | Kararın hiçbir araştırma bulgusuna duyarlı olmadığı mekanik adımlarda. |
| **Taban değişikliği bildirimi:** çalışan tüketicilerin işaretlenmesi (TP §6; E5.4) | Eski görev tanımıyla üretilen sonucun yeni kararla çelişmesini fark ettirir. | Çelişki birleştirme sırasında görünmez kalır (§0.4). | Birleştirme anında iki soru: görev tanımı hangi commit'e göreydi, o zamandan beri ne değişti? | Alt ajanlar kısa sürüyorsa ve arada taban değişmiyorsa. §0.4 bunun bu oturumda bile olduğunu gösterdi. |
