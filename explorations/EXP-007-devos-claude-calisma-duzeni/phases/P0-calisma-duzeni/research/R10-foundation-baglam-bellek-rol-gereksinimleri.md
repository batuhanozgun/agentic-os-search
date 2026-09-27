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
- Yazım sürerken dal yeniden ilerledi. R07, R08 ve R09 eklendi; bu notun yarım hâli `26c05f6`'de ara kayıt olarak commit edildi. Bu commit'lerin hiçbiri Foundation'a ve görev tanımlarına dokunmadı: `git diff 3e6cf6b HEAD -- research/soul-foundations …/briefs` boş döndü. Bu notun son hâli çalışma ağacındaki dosyadır; R07–R09 okunmadı. **[gözledim]**
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
7. **A003'ün başarı ölçütü bir vekil (proxy) ölçüttür.** A003 §3.2, Batu'nun yaptığı hatırlatmaların sayısını başarı ölçüsü yapıyor. Foundation'ın uyarısı bu ölçüte de uygulanır: "fewer reports because reporting declines" (FA §10). Batu hatırlatmayı bıraktığı için sayı düşebilir. **[çıkarım]**
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
  - A003 §3.4'teki "önce giriş dosyası, sonra soruya özgü harita, sonra özgün bölüm" yolu bunun üç katlı bir hâlidir. Eksik olanlar: güncellik kapısı, kendini tarihsel diye işaretleyen dosyalar ve denetim–kanıt yollarının ayrılması. **[çıkarım]**

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

## 4. Bellek yönetimi

### 4.1 Kayıt türleri
Foundation evrensel bir kayıt türü listesi vermiyor. "record = file", "one metadata bundle fits every resource" ve "one hierarchy is the natural organisation of all information" kısayollarını reddediyor (REC-KEY). Bunun yerine kayıtları türlere ayırmak için altı eksen veriyor. **[kaynak diyor]**

| Eksen | Foundation diyor **[kaynak diyor]** |
|---|---|
| Kip ya da duruş | "observed result; external assertion; quotation; assumption; hypothesis; estimate; forecast; simulation result; model prediction; normative/policy representation; candidate alternative" (IS §8) |
| Kabul eylemi | "Faithfully recording that a person reported P, accepting P as a factual premise, accepting a user's authoritative decision about project status, and installing a resulting maintained state are different acts. Authority may settle a designation without settling world truth." (M1 §1) |
| Kayıttaki rol | "A summary/index/query output can be derived **and** become a record in its own right." Tek şart var: "A view/output must not silently stand for a different source/version/standing". Yetkili kaynağın kim olduğu Records'un dışında kalır: "Who assigns a designated-source/authority role remains outside Records." (REC §6) |
| Eksikliğin türü | "An absent field, explicit null, an unknown response and a recorded numeric zero can convey different acquisition outcomes. ... Do not replace ambiguity with a confident value" (F2 §4) |
| Sonucun anlamı | "false != unknown / indeterminate != not evaluated != not applicable != stale" (CS, Result semantics) |
| Temsil ile gerçek | "representation says Work is X != actual Work is X" (WG §2.1). Aynı ayrım aktörün durumu için de geçerli (AG §2.1). |

**Tipik başarısızlık:** "state, evidence, documents, indexes and derived knowledge are collapsed into one undifferentiated persistence/memory concept" (REC-FS §11). **[kaynak diyor]**

EXP-007'deki yüzeylerin bu eksenlerdeki yeri **[çıkarım]**:

| Yüzey | Kip ve kabul | Kayıttaki rol | Yanlış birleştirme riski |
|---|---|---|---|
| `sources/conversation/U*` | Batu'nun birebir sözü (dış iddia ve karar kaynağı) | Kanonik kaynak | Yorumun Batu'nun sözü yerine geçmesi. A003'teki A–B–C ayrımı bunu önlüyor. |
| DECISIONS K-xxx | Batu'nun yetkili kararı; bir belirlemedir, dünya gerçeği değildir (M1 §1) | Belirlenmiş güncel karar | Kararın "doğrulanmış" sanılması: "human approved → therefore technically verified" (AD §8). |
| STATE | Ana oturumun türettiği güncel görünüm | Türetilmiş görünüm | STATE'in kaynakların ve kararların yerine geçmesi (REC §6). "STATE X diyor" ile "iş X durumunda" aynı şey değildir (WG §2.1). |
| `research/R*` | Alt ajan iddiaları; kipleri karışık | Türetilmiş görünüm ve aday | Alt ajan iddiasının bulgu diye okunması; aynı modelden gelen tekrarın doğrulama sayılması (W6). |
| A003 | Aday öneri, statüsü "v0 — yetersiz bulunmuş" | Tarihsel kayıt | Kabul edilmiş bir yöntem gibi okunması. |
| METHOD (gelecek) | Normatif kural | Batu kabul ederse yetkili belirleme | Kuralın var olmasının uygulandığı sanılması (FA §6). |
| Okuma kaydı | Süreç kanıtı | Kanıt kaydı | Okunmuş olmanın anlaşılmış ya da kullanılmış sayılması (E5.5; RI). |
| Dersler | Claude'un çıkarımı; aday normatif kural | Aday | Dersin davranış değişikliği sayılması (§4.8). |
| Konuşma ve sıkıştırma özeti | Geçici, türetilmiş | Kayıt değil | Bellek sanılması. A003 "konuşma bellek değildir" diyor ve bu doğru. |

"Sorulmadı", "soruldu ama cevap yok", "karar: hiçbiri" ve "değerlendirilmedi" ayrı durumlardır. Hepsi boş hücreye düşerse Batu'ya gereksiz soru gider ya da verilmemiş bir karar verilmiş sanılır (F2 §4; CS). **[çıkarım]**

### 4.2 Revizyon türleri
- **Değişiklik türleri ayrıdır; önemli olan anlamsal etkidir.** "creation/generation; capture/registration; revision/versioning; representation migration/re-instantiation; semantic derivation; supersession; correction; retraction/reliance withdrawal; access removal; transfer/custody change; destruction/disposition". Ardından: "The load-bearing issue is the **semantic effect**, not the label." (REC §4) **[kaynak diyor]**
- **Geri çekmenin üç ayrı hedefi var.**
  - Foundation: "A source-level removal asks whether one assertion occurrence or support route remains admitted. A proposition-level contraction asks for a successor in which a particular proposition is no longer derivable ... Revision by its negation asks for a different successor that accepts the contrary claim" (M1 §2). Örnek: "A direct-delete operation could therefore satisfy the source-removal request and fail the proposition-removal request." (C02) **[kaynak diyor]**
  - EXP-007'de üç farklı sonuç doğar:
    - Bir alt ajan notunun geri çekilmesi, o notun iddiası artık tutulmuyor demek değildir; iddia başka bir dosyada türetilmiş olarak yaşıyor olabilir.
    - Bir iddianın artık tutulmaması, tersinin kabul edildiği anlamına gelmez.
    - Tersinin kabulü ayrı bir dayanak ister. **[çıkarım]**
- **Düzeltme ile dünyadaki değişiklik ayrıdır.**
  - Foundation: "A retrospective correction must not manufacture a world transition at the date of correction. Conversely, maintaining an earlier constraint as eternally true can erase a real change." (M2 §1) **[kaynak diyor]**
  - EXP-007 için iki durum ayrı kaydedilmeli:
    - "Batu'yu yanlış anlamıştık": eski kaydın düzeltilmesidir, aynı zamana aittir.
    - "Batu kararını değiştirdi": yeni bir karardır, bir tarihten itibaren geçerlidir. **[çıkarım]**
  - DECISIONS'ta bunun iyi bir örneği zaten var: K-003'ün birleştirme kuralı silinmedi; K-009 onu "askıda" diye işaretledi. **[gözledim]**
- **"En az değişiklik" tek bir onarım vermez.**
  - Foundation: "Minimality is relative to what is counted, which states are admissible and which information has priority." (M2 §2); "State whether a condition must be entailed or merely remain compatible; name the preservation order and choice/skeptical treatment; retain unresolved alternatives." (M5.3); "'Latest wins' can be legitimate when the governing domain explicitly defines a current designation that way. It is not a general truth rule." (M2 §2) **[kaynak diyor]**
- **Eski bir tabana göre hazırlanmış öneri, doğru olsa bile yanlış zamanda uygulanabilir.**
  - Foundation: "Applying the old proposal unconditionally erases the correction; binding it to the observed base version rejects it with zero changed rows." (M2 §4, C08). Dosyanın kendisi değişmese bile dayanak değişmiş olabilir: C09'da odak nesnenin sürümü aynı kaldı ama ayrıca gereken politika değişti. **[kaynak diyor]**
  - A003'teki "kalıcı dosyaları tek başıma yazarım" kuralı eşzamanlı yazmayı önler. Ama alt ajanların eski bir sürümü okuyarak hazırladığı öneriyi önlemez. Tek yazıcı, önerinin hangi tabana göre hazırlandığını kontrol ederse bu risk kapanır. §0.4 bunun somut hâlidir. **[çıkarım]**
- **Eski bir kaydı geri getirmek yeni kanıt değildir.**
  - Foundation: "Returning a rejected claim to current status requires a new adequate basis or an explicitly scoped restoration rule; mere re-import of an older copy cannot be counted as new independent evidence." (M2 §5) **[kaynak diyor]**
  - EXP-007 için: EXP-006'dan ya da eski bir sürümden alınan bir fikir yeniden önerilirse, yeniden önerme nedeni ayrıca yazılmalıdır. **[çıkarım]**
- **Değişmeyen metin, yeniden değerlendirme yapılmadı demek değildir.**
  - Foundation: "No-op content does not prove that no reconsideration occurred, nor prove that it did." (M1 §1) **[kaynak diyor]**
  - Bir iddiayı yeni kanıt karşısında koruma kararı da bir revizyon sonucudur ve kaydedilmelidir. **[çıkarım]**

### 4.3 Tarihsel olan ve güncel olan
- **İki zaman ayrıdır.** "**effective/applicable time** — when a standing/fact/relation applies in the governed/modelled domain; **system-known/recorded time** — when a managing system learns/records/asserts it." (REC §4) **[kaynak diyor]**
- **Tarihsel kayıt ile güncel açıklama kendi kapsamlarında aynı anda doğru olabilir.**
  - C06'da, zamanında "ready" diye kaydedilmiş bir durum sonradan geriye dönük olarak "blocked" diye düzeltiliyor. Eski satır tarihsel sorgu için hâlâ doğru cevaptır.
  - C07'de en son alınan kayıt, ileri bir tarihte yürürlüğe giriyor; önceki sürüm hâlâ geçerli. Foundation'ın sonucu: "Reference time, receipt time and applicability are not interchangeable." (M2 §3) **[kaynak diyor]**
- **"Güncel" kapsamlıdır.** "`current/latest` can be role-, branch-, context- or effective-interval scoped and is not universally `max(timestamp)`"; "future scheduled standing is a legitimate effective-time case." (REC-CTS) **[kaynak diyor]**
- **Durum çok boyutludur.** "version/lineage; role/context-scoped currentness or designation; reliance/editorial standing; availability/presence; preservation/custody history" (REC §4) **[kaynak diyor]**
- **Eski bir onay tarihsel kanıttır, güncel yetki değildir.**
  - CA C4'ten: "For historical reconstruction, the earlier approval is the right evidence of why work proceeded then. For current execution it may be inapplicable." **[kaynak diyor]**
  - E5'ten: "The old view can remain correct for a historical request and wrong for a current request." (E5 §5) **[kaynak diyor]**
  - R04 (b4) buradaki ilkeyi aktarmıştı; aşağıdaki maddeler EXP-007'deki somut yerlerini ekler.

**EXP-007 için [çıkarım]:**
- **Dala göre güncellik burada gerçek bir durumdur.** Çalışma ağacındaki EXP-006 eski bir kopyadır; güncel hâli `origin/main`'dedir (ORTAK). K-010'dan sonra da main'deki EXP-006, EXP-007 için yalnız okunabilir bir kaynaktır, bağlayıcı bir güncel durum değildir. Bir bellek kaydı hangi dalın ve hangi commit'in güncel durumunu anlattığını yazmalıdır.
- **Eski yüzeylerdeki "sıradaki" ifadeleri tarihsel kayıttır, işletimsel yetki taşımaz.** R02 §6'ya göre bu ifadeler EXP-006'da 27 dosyada kalmış. Foundation'ın çözümü şuydu: tarihsel dosyanın kendisini tarihsel diye işaretlemesi (REC-CR Senaryo 2).
- **Bir kaydın hangi zamanı anlattığı ile ne zaman yazıldığı ayrı tutulur.** Örnek: "27 Eylül'de Batu şunu dedi" ile "28 Eylül'de böyle anladığımızı kaydettik" farklı zamanlardır.

### 4.4 Köken
- **Köken tek bir "kaynak" alanı değildir.** Ayrılması gereken roller: "originator/source; observer; asserter; derivation producer; current holder/store; transmitter; represented perspective; authorizer". Örnek: "The same proposition may be held by A, disputed by B, stored in a shared system and currently visible to neither." (IS §10) **[kaynak diyor]**
- **Teslim kimliği köken kimliği değildir.** "C5 separates delivery identity from origin identity and payload equality. This does not prove that distinct origins are independent" (F3 §5). Üretilmiş ya da kopyalanmış şeyin kökeni korunur: "generated/copied artifacts retain their actual origin" (F6). **[kaynak diyor]**
- **Tipik kayıplar:**
  - "complex lineage is flattened to one ambiguous `source`";
  - "a summary/transformation lacks exact source/version binding";
  - "provenance claims themselves have no recoverable provenance where that matters".

  (REC-FS §6) **[kaynak diyor]**
- **Doğru kanıt yanlış hedefe bağlanabilir.** "correct evidence, wrong target/version"; "represented/asserted binding != actual binding" (BND). **[kaynak diyor]**

**EXP-007 için [çıkarım]:**
- Her bellek kaydı en az şu rolleri ayırır:
  - kim söyledi: Batu, ana oturum ya da hangi alt ajan;
  - kim türetti ya da özetledi;
  - kim kaynağından kontrol etti;
  - hangi kaynağa ve sürüme dayanıyor.
- R01–R06 başlıklarındaki "Ana oturumun kontrolü" satırı gözlemci rolünü zaten ayırıyor. Bu iyi bir uygulama ve korunmalı. **[gözledim]**
- Aynı iddia birkaç notta tekrarlanıyorsa, kökenlerin ortak olup olmadığı sorulur. Aynı modelin aynı kaynaklardan ürettiği notlar bağımsız destek sayılmaz (W6; R04 (b5)).
- **Türetilmiş sonuç, dayanağından koparak kendi dayanağına dönüşmemelidir.**
  - Foundation: "Reusing an old derived b as an unquestioned new premise regenerates a and preserves the obsolete pair." (M1 §3) **[kaynak diyor]**
  - EXP-007'de bu zincir şöyle kurulabilir: R notu → STATE özeti → METHOD gerekçesi → yeni görev tanımı → yeni R notu. Bir halkadaki iddia geri çekilince, türetilmiş kopyalar geri çekilen iddiayı yeniden üretir. Bu yüzden türetilmiş her kayıt kökenine giden bağı taşımalıdır. **[çıkarım]**

### 4.5 Tazelik
- **Tazelik tek bir koşul değildir.** "Latest, currently applicable, mutually coherent and appropriate as-of are different conditions. Their required strength depends on the use; there is no universally mandatory freshest snapshot." (S5 §4) **[kaynak diyor]**
- **Tek zaman damgası yetmez.** Ayrılabilecek zamanlar: "time the content is about; observation/effective/applicable time; time produced/asserted/received; time recorded/known; validity interval; current/superseded/retracted standing". Sonuç: "One generic timestamp is not a foundational solution." (IS §12). Ayrıca "receipt-latest can be reference-oldest" (F3 §5). **[kaynak diyor]**
- **Bayat olmak yanlış olmak değildir.** "Stale/historical views are not inherently wrong. Failure occurs when a view's actual freshness/as-of/coverage semantics do not match the claim/use made from it." (REC §7) **[kaynak diyor]**
- **Arama güncelliği kanıtlamaz.** "search/index visibility can lag canonical repository state; a search miss does not establish absence or currentness." (REC-CR Senaryo 5) **[kaynak diyor]**
- **Güncellik bağı bakım ister.** Foundation'ın kendi uygulaması güncel dosyaları blob kimliklerine bağlamaktır. Ama "Revision binding is a maintained control, not an automatic invariant" (REC-CR R2). **[kaynak diyor]**

**EXP-007 için [çıkarım]:**
- Tazelik bir işarettir, silme kararı değildir. Bir dayanak değişince ilgili kayıt "yeniden değerlendir" diye işaretlenir. Bu, R04'ün aktardığı "dependency changed → standing may require re-evaluation != standing necessarily changed" (CS) ayrımının bellek tarafıdır.
- Claude Code hakkındaki iddiaların tazeliği ayrı bir sorundur, çünkü belgeler değişiyor. A003 §3.5 bunu zaten istiyordu: "Studies'teki teknik bilgi eskimiş olabilir". Bu tür kayıtlar erişim tarihini ve bulut etiketini taşır.

### 4.6 Unutma ve saklama
- **"Her şeyi sakla" tarafsız bir seçim değildir.** "`Keep everything forever` is not neutral." Bunun altında birkaç ayrım var: "removal/hide ≠ irreversible destruction; primary deletion ≠ destruction if in-scope recoverable copies remain; trigger ≠ execution; due/eligible ≠ currently permitted under holds/constraints; supersession can affect current standing and independently start retention; disposition rules/schedules themselves are versioned/applicability-bound information." (REC §9) **[kaynak diyor]**
- **İki tipik başarısızlık:** "over-retention becomes the accidental default"; "in-scope copies/indexes/caches defeat the intended destruction outcome" (REC-FS §10). **[kaynak diyor]**
- **Geri çekmenin dört ayrı sonucu var.** "Revocation, reliance withdrawal, replacement of the displayed view and destruction of copies can protect different outcomes." (E5 §5, X04) **[kaynak diyor]**
- **Unutma, gerileme ve yerine koyma ayrıdır.** Foundation: "A historical claim, a current retention claim and a current adequacy claim can therefore have different truth values. A once-useful behavior may remain strongly retained after the environment changes, while becoming harmful. That is not forgetting by identity." (D2 §4) **[kaynak diyor]**
- **Şimdi seçilmemek atılabilir olmak demek değildir.** Bu varsayım bir aşırı genellemedir. Foundation'ın düzeltmesi: "Separate current selection, recoverable future basis, revalidation, actual availability and demonstrated use." (U5.6) Yalnız bugüne hizmet eden bir durum ise geçmişini bırakabilir: "A local current-only state can legitimately discard its history when no protected use requires it. A persistent research record generally has different obligations." (M2 §6) **[kaynak diyor]**

**EXP-007 için [çıkarım]:**
- **"Unutmak" silmek değil, dört ayrı işlemdir.** Git hiçbir şeyi yok etmediği için bu işlemler şunlardır:
  1. güncel belirlemeden çıkarmak (yerine koyma);
  2. dayanak olmaktan çıkarmak (güvenin geri çekilmesi);
  3. bağlamdan çıkarmak: STATE'ten, CLAUDE.md'den, rol belleğinin yüklenen kısmından;
  4. türetilmiş kopyaları temizlemek: STATE'teki, devir notlarındaki, rol belleğindeki ve çalışan oturumların sıkıştırma özetlerindeki kopyalar.

  Dördüncüsü yapılmazsa geri çekilen bir iddia kopyalarda yaşamaya devam eder. R06, EXP-004 için aynı riski kaydetmişti ("Withdrawn conclusions tend to survive inside summaries").
- **Asıl risk fazla saklamaktır.** EXP-007'de risk fazla silmek değil, bağlamda fazla tutmaktır. Kanıtlar:
  - MEMORY.md'nin yalnız ilk 200 satırı yükleniyor (§2.1). Eski girdiler yeni dersleri yükleme sınırının dışına iter.
  - EXP-006'da aynı durum 5–7 dosyada tekrarlandı (R02 §6).

  Bu yüzden saklama kuralı her yüzey için ayrı yazılmalıdır: ne zaman güncel belirlemeden çıkarılır, ne zaman yüklenen bağlamdan çıkarılır, tarihçe nerede kalır.
- **Rol belleğindeki eski ders zararlı hâle gelebilir.** Ortam, model sürümü ya da yöntem değiştiğinde eski bir dersin gözden geçirilmesi gerekir (D2 §4; D3 §4). Yaşlanan derslerin taranması standart seviyede bir bakım işidir.
- **Budama kuralının kendisi de sürümlenir.** Kural değişince hangi kayıtların hangi kurala göre budandığı bilinmelidir (REC §9).

### 4.7 Çakışma
- **Hizalamadan çelişki denmez.** "Two states should not be called contradictory until comparison conditions are aligned." Karşılaştırılacak koşullar: "referent/property; time/scope; unit/reference frame; mode/stance; granularity; uncertainty; provenance/independence". Çözüm kimde: "Conflict detection/merge/revision belongs to Dynamics; adjudication may additionally involve Work/Actors/authority." (IS §13) **[kaynak diyor]**
- **Alternatifler birlikte iddia edilmeden yan yana durabilir.** "Preserving alternatives is not a defective attempt at consensus. An explicit adjudication may later select an alternative, but simply concatenating the records does not perform that adjudication." Ters yönde de bir uyarı var: "Separate contexts are not an excuse to ignore a genuine conflict within one required scope." (M1 §5) **[kaynak diyor]**
- **Amaç ya da değer çatışması yetki ister.** "Neither the assistant's preferred allocation nor the operator's technical power settles legitimate priority. A feasible bounded fact-finding step may proceed even while the final value decision is unresolved." (CA C2) **[kaynak diyor]**
- **Hangi yüzeyin yetkili olduğunu Records belirlemez.** "Who assigns a designated-source/authority role remains outside Records." (REC §6) **[kaynak diyor]**

**EXP-007 için beş çakışma türü [çıkarım]:**
1. **Zaman ya da kapsam farkından doğan görünür çakışma.** Örnek: main'deki EXP-006 ile daldaki kopyası. Önce hizalanır; çoğu zaman çakışma değildir.
2. **İki alt ajan notu arasındaki çakışma.** Örnek: R07 ile R09. İkisi de korunur. Seçim yapılırsa hangi temele dayandığı yazılır.
3. **Batu'nun farklı zamanlardaki sözleri arasındaki çakışma.** "Sonraki karar geçerlidir" kuralı ancak açıkça tanımlanırsa meşrudur (M2 §2). EXP-007 bu kuralı DECISIONS'ta açıkça yazmalı ve kapsamını belirtmelidir.
4. **Batu'nun kararı ile kanıt arasındaki çakışma.** Karar Batu'nundur. Kanıt kayıtta kalır ve karardan ayrı tutulur (M1 §1).
5. **Değer ya da öncelik çatışması.** Batu'ya gider. Bu arada sınırlı bir bilgi toplama adımı sürebilir (CA C2).

Yetkili yüzeyi belirlemek bir yetki işidir. EXP-007 README bunu zaten yapıyor: "Güncel durum yalnız [STATE](STATE.md)'tedir." **[gözledim]** Kaynaklar ile STATE çatışırsa ne olacağı ise yazılı değil. Foundation'da benzer durumlarda kök STATE'in belirleyici sayıldığını R04 kaydediyor (R04, "Conflicting status files"). Bunu ben doğrulamadım.

### 4.8 Bir dersin davranışa gerçekten dönüşmesi
R04 (d7) temel listeyi verdi: kimin farklı davranacağı, dersin nerede saklandığı, nasıl yükleneceği, hangi durumlara uygulanacağı, ne kadar süre geçerli olacağı ve kanıtı. Bu bölüm o listeye eksik kalan beş ayrımı ekler.

1. **Dersi taşıyan model değil, taşıyıcıdır.**
   - Foundation: "Two systems can run exactly the same interpreter while one uses a retained history-derived record and the other does not." (D1 §2). Aynı sonuç B1'de: "The adaptation bearer must include the relevant carrier and access path; the model alone is not thereby shown to have changed." (B1 vaka 6) **[kaynak diyor]**
   - Ters yön de geçerli: "parameters can change while the implemented function remains equivalent" (D1 §2). **[kaynak diyor]**
   - EXP-007'de model öğrenmez; öğrenen, dosyalar ve onları yükleyen yollardır. METHOD'da yapılan bir değişiklik davranışı hiç etkilemeyebilir. **[çıkarım]**
2. **Gerçekleşme zinciri EXP-007'de somut halkalara ayrılır.** D3 §2'deki zincir R04'te alıntılandı. Aşağıdaki tablo halkaları bu ortamın taşıyıcılarına bağlar. **[çıkarım; ortam bilgisi R01'den]**

   | Halka (D3 §2) | EXP-007'de |
   |---|---|
   | "carrier written" | Ders METHOD'a, bir ders dosyasına ya da rol belleğine yazılıp commit edildi. |
   | "candidate path installed" | Ders rol dosyasına, görev tanımı şablonuna ya da CLAUDE.md'ye işlendi. |
   | "relevant path traverses carrier" | İlgili tüketici o anda o metni gerçekten yüklüyor. Alt ajan rol dosyasını ya da görev tanımını okuyor. Ana oturum sıkıştırmadan sonra CLAUDE.md'yi yeniden yüklüyor; R01 C12 bunu söylüyor ama etiketi `documented_generic_unclear_cloud`. Rol belleğinde ders MEMORY.md'nin ilk 200 satırına giriyor. |
   | "response disposition changed at that locus" | O durumda davranış gerçekten farklı. |
   | "all applicable paths changed" | Bütün ilgili rollerde, görev tanımlarında ve yeni oturumlarda farklı. |
   | "retained after the claimed lifecycle transition" | Sıkıştırmadan, yeni oturumdan, makinenin geri alınmasından ve model sürümü değişiminden sonra da sürüyor. D3 §4: "A new operator, model version, tool interface or coordination pattern can change applicability even when the lesson text is unchanged." |

3. **Görülmemek unutulmak değildir; görülmek de kullanılmış olmak değildir.**
   - Foundation: "acquired in the past != retained now; no observed expression != erasure established; same current output != same retained disposition; retained disposition != currently appropriate disposition" (D2 §3). Ayrıca: "unchanged output != no feedback; unchanged output != proof of feedback use" (G6). **[kaynak diyor]**
   - A003 §3.10'daki kural doğru ama eksik: "Değişim görülene kadar ders 'doğrulanmadı' sayılır." Dersin uygulanacağı durum hiç doğmadıysa bu bir başarısızlık değildir. Kanıt için dersin uygulandığı türden bir durum (fırsat sınıfı) tanımlanmalıdır. **[çıkarım]**
4. **Hatanın tekrarını beklemek gerekmez, ama sınama hedefi değiştirebilir.**
   - Foundation: "A controlled discriminating probe, or a sufficiently established mechanism and operative path, can support a bounded conditional claim before natural recurrence." (D1 §4). Ama: "Testing can be an intervention." (D2 §6) **[kaynak diyor]**
   - A003'ün önerdiği soğuk başlangıç testi, soru ipucu verirse ya da dersin adını anarsa ölçtüğü şeyi öğretmiş olur. Soruların tarafsız yazılması ve ders metninin sınama isteminde geçmemesi gerekir. **[çıkarım]**
5. **Başarı ölçüsü vekil olabilir ve çerçeve kör olabilir.**
   - Foundation: "measured/local objective improved != intended/global target improved". Örnekleri arasında "fewer reports because reporting declines" var (FA §10). Ayrıca "all observed signals handled != all material outcomes observed" (FA §11). **[kaynak diyor]**
   - A003 §3.2 "Bana yaptığın her hatırlatma bir kusur olarak kayda geçer; düzenin gerçek başarı ölçüsü bu sayıdır" diyor. Bu sayı iki yoldan yanıltabilir:
     - Batu yorulup hatırlatmayı bırakırsa sayı düşer (vekil kusuru).
     - Batu'nun fark etmediği kusurlar hiç sayılmaz (çerçeve körlüğü).

     Ölçütün yanına, Batu'dan bağımsız en az bir ölçü konmalıdır. Örnekler: karşı okumanın bulduğu kusurlar ya da soğuk başlangıç testinin sonucu. **[çıkarım]**

**Kim karar verir?** Öğrenmeyi kuralı değiştirmeye dönüştürmek bir yetki işidir: "Control owns governing semantics of any new rule/regime." (FA §13); "A system's ability to alter its learning rule does not authorize the alteration." (D3 §6). **[kaynak diyor]** Rol belleğine yazmak ile yöntemi değiştirmek bu yüzden ayrı kararlardır (§5.4). **[çıkarım]**

### 4.9 Tipik başarısızlıklar: Foundation ve bu repodan örnekler
- **Tartışma kaydedilmemişti.** "The intervening discussion and its correction had not been persisted. A cold reader could recover the original review, but not this later progression." (DH §1) **[kaynak diyor]**
- **Soğuk başlangıç kontrolü bağımsız değildi.** CSC'ye göre önceki giriş verisi bayattı: "Earlier cold-entry metadata was stale". Onarım da aynı oturumda kontrol edildi: "The assistant still had conversation context; no independent fresh-session run ... was performed." **[kaynak diyor]** Yani Foundation hiçbir zaman bağımsız bir soğuk başlangıç testi çalıştırmadı. A003'ün önerdiği test bu repoda ilk olacak. **[çıkarım]**
- **Derin okuma eski sonuçları güncel gösteriyordu.** Records'ta daha derin okuma, karşı kontrol öncesi eski sentezleri güncelmiş gibi gösteriyordu. Foundation bunu "prior central defect" olarak adlandırdı ve düzeltti (REC-CR, Verdict). **[kaynak diyor]**
- **Düzeltme saklandı ama yol değişmedi.** "An incident lesson exists but is not selected or used." (B1 vaka 5) **[kaynak diyor]**
- **Güncellemeler kayboldu, eski sonuçlar geri geldi.**
  - C08'de araya giren düzeltme eski bir öneriyle silindi.
  - C03'te türetilmiş bir çift yeniden üretildi.
  - X03'te eski görünüm tüketicide kaldı.
  - CA C4'te işe dönen işçi eski görünümle çalıştı.

  (M2 §4; M1 §3; E5 §5; CA C4) **[kaynak diyor]**
- **Bu repodan bir örnek.** EXP-006'da kısa cevap kuralı (D010) 26 Eylül'de yazılıydı. Batu yine de 27 Eylül'de cevapların uzunluğundan şikâyet etti (R02 §4, E3). Yazılı bir kural davranışa dönüşmemişti. **[kaynak diyor]** (R02)
- **Yayılma açığı.** R04'e göre Foundation'da çelişen STATE dosyaları vardı ve kök STATE belirleyiciydi. R04 bunu TP'nin tarif ettiği yayılma başarısızlığının canlı örneği sayıyor (R04, "Conflicting status files"). Ben doğrulamadım.

### 4.10 Bellek tasarımını sınamak için sorular
1. Tasarım, geçmişte doğru olan ama bugün geçersiz bir kaydı güncel olandan ayırabiliyor mu? Bunu kaydı silmeden yapabiliyor mu? (REC §4; CA C4)
2. Bir kayıtta şu ifadeler ayrı mı: "Batu dedi", "Batu karar verdi", "Claude çıkardı", "alt ajan iddia etti", "ana oturum kaynağından doğruladı"? (M1 §1; IS §10)
3. Bir iddia geri çekildiğinde türetilmiş kopyaları (STATE, devir notu, rol belleği, METHOD gerekçesi) bulunup işaretleniyor mu? (M1 §3; REC-FS §10)
4. "Düzeltme" ile "karar değişikliği" ayrı kaydediliyor mu? Hangisinin hangi tarihten itibaren geçerli olduğu okunabiliyor mu? (M2 §1)
5. Alt ajanın önerdiği değişiklik, hangi tabana göre hazırlandığı bilgisiyle mi geliyor? Tek yazıcı bu tabanı kontrol ediyor mu? (M2 §4)
6. Şu durumlar birbirinden ayrı gösterilebiliyor mu: "sorulmadı", "cevapsız", "karar: hiçbiri", "değerlendirilmedi", "uygulanamaz", "bayat"? (F2 §4; CS)
7. "Çelişki" denmeden önce zaman, kapsam, kip ve köken hizalanıyor mu? Çözülemeyen çelişki görünür kalıyor mu? (IS §13; M1 §5)
8. Sıkıştırmadan ya da oturum sonundan önce yazılan kayıt, sonraki revizyonun ihtiyaç duyacağı durumu taşıyor mu? Yani reddedilenler, dayanılan varsayımlar ve yeniden açma tetikleri kayıtta var mı? (M5.4)
9. Her ders için taşıyıcı, yükleme yolu, fırsat sınıfı, ufuk, karşılaştırma ve kanıt yazılı mı? Kanıt, sınamanın kendisinin öğretmediği bir yoldan mı elde edildi? (D1–D3)
10. Saklama kuralı her yüzey için ayrı mı? Yüklenen bağlamın (MEMORY.md'nin ilk 200 satırı, CLAUDE.md) neyi dışarıda bıraktığı biliniyor mu? (REC §9; S5 §4)
11. Konuşmayı hiç görmemiş yeni bir oturum, yalnız repodan son tartışmayı ve düzeltmeleri kurabiliyor mu? Bu, gerçekten bağımsız bir oturumla sınandı mı? (DH §1; CSC)
12. Başarı ölçütünün yanında, vekil ölçüt kusuruna karşı Batu'dan bağımsız ikinci bir ölçü var mı? (FA §10–11)

### 4.11 Foundation'ın bilerek açık bıraktığı, EXP-007'nin karar vermesi gereken noktalar
- **Yetkili yüzeyi kimin belirleyeceği:** "who declares current/designated/authoritative standing" (REC §12C) Records'un dışındadır. **[kaynak diyor]**
- **Revizyon politikası:** "The selected preservation/priority rule is part of the revision basis" (M2 §2). Foundation'ın ayrımları "do not supply the appropriate empirical policy for SOUL" (M5 §4). **[kaynak diyor]**
- **Yeni sürüm ile yeni türev arasındaki eşik ve güvence düzeyi:** "No universal rule decides same representation vs new version vs new derived resource." Güvence gücü de profile özgüdür (REC §12A). **[kaynak diyor]**
- **Opak bir ajanın bağımlılık kümesi:** "We have not established how to discover a complete dependency set for an opaque agent." (M2 §4) **[kaynak diyor]**
- **Saklama ufku:** "It supplies no normative retention threshold" (D2 §1). **[kaynak diyor]**
- **Geri getirmenin uygunluğu:** "Whether reinstatement is appropriate remains target- and policy-dependent" (M2 §5). **[kaynak diyor]**
- **Doğrulanmamış kalanlar:** "Actual retained state, needed history horizon, source custody, runtime use and causal benefit remain unverified." (CA C4) **[kaynak diyor]**
- **Mekanizma uzman araştırmasına bırakılmış:** "Memory and Learning remain useful specialist inquiries across existing distinctions, not automatically additional Foundation peers or mandatory services." (CA C4) **[kaynak diyor]** Bellek mekanizmasının seçimi bu yüzden R07–R09'un konusudur. **[çıkarım]**

### 4.12 Bellek için standart seviye bileşenleri **[çıkarım]**

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur (başka alt sistemler dahil) | Bedeli | Ne zaman gerçekten gereksiz |
|---|---|---|---|---|
| **Tür ve kip etiketi** (M1 §1; IS §8) | İddianın gerçekle, kararın doğrulamayla karışmasını önler. | Bağlamda kip kaybı olur (§3.3). Batu'nun onayı teknik doğrulama sayılır (kalite). | Etiketleme disiplini. | Yüzeyin tek türden kayıt tuttuğu yerde. Örneğin `sources/` yalnız birebir kayıt tutar; orada etiket yüzey düzeyinde verilebilir. |
| **Köken bağı:** kim söyledi, kim türetti, kim doğruladı; kaynak ve sürüm (IS §10; REC-FS §6) | Geri çekmenin ve bağımsızlık sayımının doğru yapılmasını sağlar. | Türetilmiş sonuç dayanağa dönüşür. Aynı kökten gelen tekrar doğrulama sanılır (kalite). | Her kayıtta bir satır; alıntı ve yol. | Kalıcı karar taşımayan geçici çalışma notlarında. |
| **Değişiklik türü ve iki zaman:** etkili zaman ve kayıt zamanı (REC §4; M2 §1, §3) | Düzeltme ile karar değişikliğini ve tarihsel ile güncel olanı ayırır. | Tarihsel kayıt ya silinir ya güncel sanılır. Eski onay yetki gibi kullanılır (yönetişim). | Değişiklik notu. | Geçmişinin korunması gereken hiçbir kullanımı olmayan, yalnız güncel durumu tutan yüzeylerde (M2 §6). Git geçmişi zaten tutar. |
| **Durum boyutları:** güncel, yerine konmuş, geri çekilmiş, askıda; değerlendirilmedi, bayat (REC §4; CS) | "Askıda" gibi ara durumları okunabilir kılar. | K-003 türü askıdaki kararlar ya geçerli ya iptal sanılır (plan). | Durum sütunu ve bakımı. | Bu kullanım için boyutlar birbirinden bağımsız değişemiyorsa (REC-CTS). |
| **Taban kontrolü:** öneri hangi sürüme göre hazırlandı (M2 §4) | Kayıp güncellemeyi önler. | Araya giren düzeltme silinir. Eski görev tanımıyla üretilmiş bir sonuç yeni kararı ezer (§0.4; bağlam). | Commit kimliği ve birleştirmede karşılaştırma. | Yazıcı tekse ve önerinin üretimiyle uygulanması arasında taban değişmiyorsa. |
| **Geri çekmenin kopyalara yayılması:** türetme bağlarının listesi (M1 §3; REC-FS §10; TP §15) | Geri çekilen iddianın kopyalarda yaşamasını önler. | Eski iddia devir notunda ve bağlamda yeniden doğar (bağlam, süreklilik). | Türetme bağlarını tutmak; geri çekmede tarama. | Türetilmiş kopya hiç yoksa. A003'teki "Bir bilgi tek yerde durur" ilkesi bu bedeli düşürür ama sıkıştırma özetlerini kapsamaz. |
| **Çakışma kaydı ve karar yolu** (IS §13; M1 §5) | Çelişkinin sessizce uzlaştırılmasını ya da her farkın çelişki sanılmasını önler. | Yetki gerektiren değer çatışmaları ana oturumca çözülür (yönetişim). | Ayrı bir bölüm ve karar gerekçesi. | Tek kaynaklı alanlarda. |
| **Yüzey başına saklama ve budama kuralı:** bağlamdan çıkarmak silmek değildir (REC §9; D2 §4) | Fazla saklamanın varsayılan olmasını ve eski derslerin zararlı biçimde kalmasını önler. | Yüklenen bağlam eski girdilerle dolar ve yeni dersler yükleme sınırının dışında kalır (bağlam, öğrenme). | Kural yazımı ve düzenli tarama. | Yüzey hiç yüklenmiyorsa ve büyümüyorsa. |
| **Ders kaydı ve davranış kanıtı** (§4.8; D1–D3; FA) | Yazılı kuralın davranışa dönüşüp dönüşmediğini görünür kılar. | EXP-006'daki D010 örneği tekrar eder. Başarı vekil ölçüte kayar (gözlemlenebilirlik). | Sınama ve izleme; sınamanın öğretme etkisini yönetmek. | Ders bir kerelik ve geri dönüşsüz bir olaya aitse ve yeniden kullanılmayacaksa. D1: "one-off response != adaptation"; o durumda uyum iddiası da gerekmez. |
| **Bağımsız soğuk başlangıç sınaması** (DH §1; CSC) | Sürekliliği aynı bağlamın okumasıyla değil, taze bir okuyucuyla sınar. | Kaydedilmemiş tartışma fark edilmez (süreklilik). | Taze bir oturum ve karşılaştırma. | İş tek oturumda bitiyorsa. EXP-007 için bu koşul geçerli değil. |

## 5. Kalıcı rol yapısı

### 5.1 Rol tanımının dayanağı
R04 (c1) iki ilkeyi aktarmıştı: rol ihtiyacı AI ajanı ihtiyacı demek değildir, ve sorumluluk ile meşru yetki mekanizma seçiminden önce gelir (RUA; REUSE). Bu bölüm, bir rol tanımının **neye dayanması gerektiğini** Foundation'dan çıkarır.

- **Süregelen sorumluluk, Foundation'da neredeyse bir rol tanımı iskeletidir.**
  - Foundation: "Standing responsibility can persist without current Work. It is expressible through: persistent bearer; role/office; obligation/duty; scope/context/time; accountability/forum; triggered Work when action becomes due." Anti-collapse kuralı: "standing Actor responsibility != current Work episode". (AG §7) **[kaynak diyor]**
  - Bu altı öğe kalıcı bir rolün taşıması gerekenleri verir: taşıyıcı, konum, görev, kapsam, hesap verilen yer ve tetik. A003'teki "Bir görev kalıbı üç kez aynı şekilde tekrarlanınca kalıcı bir ajan tanımına dönüşür, önce değil." kuralı (§3.3) ise rolü **sıklıktan** türetiyor. Foundation'a göre dayanak sıklık değil, **gereken sorumluluktur**. Batu'nun "her seferinde yeninden alt ajana rol biçmek doğru değil" sözü (U004; yazım özgün metindeki gibi) bu ayrımla örtüşüyor. **[çıkarım]**
- **Yapabilmek, yetkin olmak, izinli olmak, yetkili olmak ve yükümlü olmak ayrı şeylerdir.**
  - Foundation: "`Can`, `is skilled/competent`, `may`, `has power/authority`, and `must/ought` are not synonyms." (AV D2). Ayrıca: "Being permitted or empowered to act does not by itself create a duty to act. Likewise, being responsible for an area may create duties without giving unilateral authority to execute every related action." (AF-CAO §6) **[kaynak diyor]**
  - Bir rol tanımı bunları ayrı yazar: yetkinlik iddiası ve kanıtı; araç izni; karar yetkisi; görevler. Örneğin karşı okuyucunun görevi çürütmeyi denemektir. Buna karşılık sonucu kabul etme yetkisi yoktur. **[çıkarım]**
- **Rol adı yetki, yetkinlik ya da bağımsızlık kanıtlamaz.**
  - Foundation: "role name does not establish epistemic independence or authority" (A3 §3.2); "role labels do not establish authority, competence, independence or accountability" (A3 §6); "role label != valid verifier/authority standing" (CS, Candidate studies) **[kaynak diyor]**
  - Genel bir "eleştirmen" etiketi aslında ayrı işlevleri toplar: "review/critique; verification; adversarial challenge; integration/acceptance transition" (A3 §3.2). **[kaynak diyor]**
  - Roller etiketle değil işlevle tanımlanır. Rolün yeterliği ayrıca kanıtlanır. **[çıkarım]**
- **Hesap verebilirlik bir ilişkidir.**
  - Foundation: "`is accountable` is incomplete without at least the relevant forum, subject matter/standard and process or consequence context." (AF-RA §4) **[kaynak diyor]**
  - Her rolün kime, hangi ölçüte göre ve hangi süreçle hesap verdiği yazılır. EXP-007'de zincir alt ajandan ana oturuma, ana oturumdan Batu'ya gider. Alt ajan rollerinin ekibi ayrı bir hesap veren değildir: "Nor does a coordinated runtime team automatically become a persistent corporate/group agent." (AG §8) **[kaynak diyor + çıkarım]**
- **Beklenen davranış yazılmazsa ihmal görünmez.**
  - Foundation: "Agency and responsibility can concern deliberate non-action or failure to perform expected/available conduct. An event-only model can erase meaningful omission." (AV D6). İhmalin bir dayanağı vardır: "an available or possible action; an expectation, duty, plan, intention or opportunity" (AF-AOD §2) **[kaynak diyor]**
  - Rol tanımı, rolün hangi durumlarda devreye girmesi gerektiğini yazar. Aksi hâlde eksik arayıcının hiç çağrılmaması kayıtlarda iz bırakmaz. **[çıkarım]**
- **Destek ve koordinasyon da iştir.**
  - Foundation: "Coordination is itself Work" (WV §7); "Some Work exists to sustain, coordinate, protect or enable the conditions under which other Work can proceed." (WF-CSC §9) **[kaynak diyor]**
  - Kayıt bakımı, bayat dosya taraması ve dersleri yaşlandırma gibi bakım işleri de bir role verilmelidir. R04 (c5) bunun için "standing custody" demişti; burada bu işin bir rol tanımına girmesi gerektiği ekleniyor. **[çıkarım]**
- **Çapraz atıf:** R06, EXP-004'ten bir rol formülü aktarıyor: "Yeni rol = talimat + gerçek model/insan/program taşıyıcısı + uygun context + araç/etki kapsamı + ilgili yeterlik dayanağı." Foundation ayrımları bu formülü destekliyor ve ona görev, hesap verme ve tetik öğelerini ekliyor. **[çıkarım]**

### 5.2 Rolün oturumlar arası sürekliliği
- **Foundation süreklilik sorusunu doğrudan cevaplıyor.** "An agent/process can be recreated in a new session while Work and persistent representations continue." Dört ayrım: "same model class != same bearer identity; same role != same process/session; fresh process can occupy a continuing role; continuing Work can survive bearer/session replacement." (A3 §4.3) **[kaynak diyor]**
- **Rolün tanımlı, çağrılabilir ve etkin olması ayrıdır.**
  - Foundation: "`has role`, `may activate role`, and `is acting in role now` are not interchangeable." (AF-IRP §2). Ayrıca dört soru sorulmalı: "who/what persists across time; which role/office/position is held; which role/position is active in a context; which episode is under discussion; how the bearer participates in that episode." (AF-IRP, Decision-critical implication) **[kaynak diyor]**
  - EXP-007'de bu üç durumun karşılığı: `.claude/agents/` altında bir tanımın bulunması; ana oturumun o rolü o iş için çağırabilmesi; o anda o rolle çalışan bir alt ajan örneğinin bulunması. **[çıkarım]**
- **Süreklilik taşıyıcılarda ve ilişkilerde yaşar.**
  - Foundation: "Replacing an individual need not erase a system-level disposition if its operative carrier and relations survive; retaining every individual need not preserve it if coordination or access is lost." (D3 §3; B1 vaka 9) **[kaynak diyor]**
  - Geçici alt ajan örneği değiştiğinde rolün sürekliliği bozulmaz, yeter ki taşıyıcılar gerçekten yüklensin: tanım, bellek, tetik ve girdi–çıktı sözleşmesi. Ters yön de doğru: tanım dosyası repoda dursa bile rol çağrılmıyor ya da belleği yüklenmiyorsa süreklilik yoktur. **[çıkarım]**
- **Aynı rol ne demek? Foundation bu soruyu açık bırakıyor.**
  - "What makes a person, organization, office, software system or other bearer `the same` across time for the specific semantic purpose at hand?" Bu soru "domain-sensitive" diye açık bırakılmış (AOQ OQ1). **[kaynak diyor]**
  - EXP-007'nin tanımlaması gerekir: "aynı rol" aynı tanım sürümü mü, aynı bellek mi, aynı sorumluluk mu? Model sürümü değişince rol aynı mı kalır? D3 §4'e göre model değişimi dersin uygulanabilirliğini değiştirebilir. **[çıkarım]**
- **Süren sorumluluk, tamamlanan bölümlerden oluşur.**
  - Foundation: "Continuing Work may have completed episodes while the larger responsibility remains open." (WV §13) **[kaynak diyor]**
  - Her alt ajan çağrısı bir bölümdür. Rolün sorumluluğu bölüm kapanınca kapanmaz. **[çıkarım]**
- **Tetiklenmeyen sorumluluk kâğıt üzerinde kalır.**
  - Süregelen sorumluluk "triggered Work when action becomes due" ile işe dönüşür (AG §7). **[kaynak diyor]**
  - Bu ortamda alt ajan kendi alt ajanını açamıyor (ORTAK). Bu yüzden bütün rol çağrıları ana oturumdan gelir ve tetiklerin tümü koordinatörde toplanır. Bu, R06'nın "akıllı koordinatör halleder" uyarısının tam yeridir. Tetikler koordinatörün hafızasında değil, dosyada yazılı durmalıdır. **[çıkarım]**
- **Tanım değişikliği çalışan örneklere kendiliğinden ulaşmaz.**
  - Foundation: "an authority revocation is active centrally while old sessions remain usable" (TP §6). Ayrıca: "actual authority can end while apparent authority persists until third parties receive notice" (AF-RDA §5) **[kaynak diyor]**
  - Rol tanımı değişirse, eski tanımla çalışan örneklerin sonuçları hangi sürüme göre üretildikleriyle birlikte değerlendirilir. **[çıkarım]**
- **Katılım kayıtları örnek düzeyinde tutulur.**
  - Foundation: "Actor A performs Work W at t1 / Actor A verifies Work W at t2 must not be reduced to an ambiguous bag containing both roles and both times." (BND). Ayrıca: "two role labels != two independent Actors" (CC, Authority and separation of duties) **[kaynak diyor]**
  - Kayıt hangi örneğin, hangi rol sürümüyle, hangi işte, ne zaman ne yaptığını tutar. Böylece "aynı örnek hem üretip hem denetledi mi?" sorusu cevaplanabilir. **[çıkarım]**

### 5.3 Rol belleği ile rol yetkisi ayrı tutulmalı
- **Bir metin dört ayrı şeye karşılık gelir.** Model tarafından görülen talimat ile zorlanan kontrol ayrıdır. Foundation bir rol dosyasının karşılığını dörde ayırıyor: "instruction/policy text = Information representation; normative authority/obligation = Actor/control relation; mechanical enforcement = Environment/control condition; compliance/review activity = Work." (A3 §2.5) **[kaynak diyor]**
- **Temsil gerçek durumu kanıtlamaz.** "representation says Actor standing is X != actual Actor standing is X" (AG §2.1). Foundation'ın ertelediği ilişkiler arasında şunlar da var: "identity/role/delegation records vs current standing"; "context-visible permissions/roles vs actual authority" (AD §1). **[kaynak diyor]**
- **Doğru bir düzeltme bile her şeyi yeniden yazma yetkisi vermez.** "a well-supported factual correction does not grant its author every permission to rewrite a managed corpus." (M1 §1) **[kaynak diyor]**
- **Değiştirebilmek yetkili olmak değildir.** "A system's ability to alter its learning rule does not authorize the alteration. Control/Actors remain responsible for governing basis and authority. Self-generated agreement does not create independent evidence; adaptation of the verifier does not automatically validate the verifier's new criteria." (D3 §6) **[kaynak diyor]**
- **Uzmanlık da, konum da, erişim bilgisi de tek başına yetki değildir.** "expertise != authority; manager/owner != every decision authority; credential possession != legitimate authority" (CC, Authority / legitimacy). Ayrıca: "A submanager may coordinate/decompose while lacking authority to alter acceptance criteria or widen permissions." (A3 §3.1) **[kaynak diyor]**
- R04 (c3) teknik erişim ile yetkinin ayrı olduğunu genel ilke olarak koymuştu. Bu bölüm o ilkeyi rol belleğine uyguluyor.

**EXP-007 için: kalıcı bir rolün üç ayrı katmanı [çıkarım]**
1. **Rol tanımı (normatif katman).** Sorumluluk, görevler, sınırlar, tetikler ve hesap verme ilişkisi. Dayanağı yetkili bir karardır; A-04'e göre bu karar Batu'nundur. Değiştirilmesi yetki ister (§5.4).
2. **Rol belleği (bilgi katmanı).** Rolün birikimi: dersler, desenler, tuzaklar ve kaynak yolları. Kipi model çıkarımıdır ve yetki taşımaz.
   - Tanımla çelişirse tanım geçerli olur.
   - Bellekteki "bunu yapabilirim" cümlesi bir yetki devri değildir.
   - Kural gibi yazılmış bir bellek girdisi ancak öneri olarak yukarı taşınabilir.
3. **Yetki ve zorlama.**
   - Araç izinleri (rol dosyasının `tools` alanı, izin modu) teknik bir etki gücüdür.
   - Batu'nun devrettiği karar yetkisi normatif bir yetkidir.
   - İkisi ayrı yazılır. Tavsiye niteliğindeki metin ile zorlanan kontrol ayrı kalır (R04 d4).

**Ortamdaki gerilim:** R01 C8'e göre `memory: project` alanı role `.claude/agent-memory/<ad>/` altında kendi belleğini veriyor (`documented_generic_unclear_cloud`). Bulutta bu belleğin kalıcı olması ancak commit ve push ile mümkün; belgeler bulut durumunu ele almıyor (R01). **[kaynak diyor]** (R01)
- Rol belleğini, tasarım gereği rolün kendisi yazar. A003 ise kalıcı dosyaları yalnız ana oturumun yazmasını öngörüyor. Bu iki öngörü çatışıyor.
- Foundation'ın çözümü "kim yazar" sorusundan çok "yazılan ne tür bir kayıttır" sorusudur. Rolün yazdığı içerik bilgi olarak etiketlenir. Kural niteliği taşıyan her şey öneri olarak ana oturuma ve Batu'ya gider. Hangi taşıyıcının kullanılacağı R07'nin konusudur. **[çıkarım]**

### 5.4 Rolü kim değiştirebilir?
- **Foundation bu soruyu bilerek açık bırakıyor.**
  - Work sentezi "does not establish ... who may select, commit, reprioritise, waive, accept, terminate or reactivate Work" (WV §16).
  - İzin, yetki ve güç arasındaki sınır açık bir sorudur (AOQ OQ4).
  - Kurumsal kontroller "may depend on the scoped authority to issue, approve, waive, delegate or revoke a rule/decision" (CC).

  **[kaynak diyor]**
- **Rolü değiştirmek sıradan bir iştir, yalnız başka düzeydedir.** "Meta-work—Work that changes workflow, agent configuration, verifier, tooling or the working system—is ordinary Work at another target level." (WG §6) **[kaynak diyor]** R04 (a6) bu yüzden yöntem değişikliklerinin de kabulden geçmesini önermişti. Burada ek bir tespit var: rol değişiklikleri **türlerine göre farklı yetki** ister. **[çıkarım]**
- **Yetki devrinin geçmişi izlenebilir olmalı.** "the subject on whose behalf a request is made; the current actor; a party authorized to become an actor; delegation history through nested actor claims" (AF-RDA §4) **[kaynak diyor]**
- **EXP-007'de zaten bir kural var.** "Kontrol ve yapılandırma değişiklikleri (CLAUDE.md, `.claude/agents`, skills, hook'lar) Batu onaylamadan kurulmaz" (EXP-007 README, Sınırlar; DECISIONS A-04). Bu kural ilk kurulumu kapsıyor. Kurulumdan sonraki değişikliklerin kimde olduğu yazılı değil. **[gözledim]**

Değişiklik türlerine göre bir ayrım önerisi **[çıkarım; karar Batu'nun]**:

| Değişiklik türü | Örnek | Dayandığı Foundation ayrımı | Önerilen yetki |
|---|---|---|---|
| Rol belleğine ders eklemek | "Bu kaynakta tablo kesik geliyor, tam oku" | Kabul edilen girdinin türü (M1 §1); saklamak davranış değişikliği değildir (D1 §4) | Rol yazar ya da ana oturum yazar; köken ve kip etiketi taşır. |
| Rolün yöntemini değiştirmek (sorumluluk ve yetki aynı kalır) | Dönüş biçimine bir alan eklemek | Yöntem değişikliği de iştir (WG §6); kendini yetkilendirme olmaz (D3 §6) | Ana oturum karar verir, aşama raporunda bildirir; davranış kanıtı istenir. |
| Rolün kapsamını, yetkisini, araç iznini ya da kabul ölçütünü değiştirmek | Karşı okuyucuya yazma izni vermek | Alt yönetici kabul ölçütünü değiştiremez ve izinleri genişletemez (A3 §3.1); ulaşılabilir etki gücü yetki değildir (AD §4) | Batu. |
| Rol açmak, kapatmak, birleştirmek | Eksik arayıcıyı karşı okuyucuyla birleştirmek | Süregelen sorumluluk (AG §7): kapanan rolün görevleri başka bir role verilmezse ihmal oluşur (AV D6) | Ana oturum önerir. Yapılandırma değişikliği olduğu için A-04 kapsamında Batu onaylar. |
| Denetleyici rolün ölçütünü değiştirmek | Karşı okumanın geçme eşiği | "adaptation of the verifier does not automatically validate the verifier's new criteria" (D3 §6); üretenin kendi kontrolü bağımsız doğrulama değildir (CC) | Batu, ya da en azından denetlenen işten bağımsız bir onay. Denetleyici kendi ölçütünü değiştirip kendini onaylayamaz. |

Her değişiklik için dört şey yazılır:
- sürüm ve değişiklik notu;
- çalışan örneklere nasıl bildirileceği (TP §6);
- bağımlı sonuçların yeniden değerlendirilip değerlendirilmeyeceği: "dependency changed → standing may require re-evaluation" (CS);
- eski tanımla üretilen sonuçların nasıl işaretleneceği.

**[çıkarım]**

### 5.5 Tipik başarısızlıklar
- **Taşıyıcı ile rolün birleştirilmesi (v0).**
  - A003'teki ifadeler: "Alt ajanlar: tek soruluk, geçici çalışanlar" (A003 §3.2) ve "Bir görev kalıbı üç kez aynı şekilde tekrarlanınca kalıcı bir ajan tanımına dönüşür, önce değil." (A003 §3.3)
  - Örnek geçici olduğu için rol de geçici sayılmış. Foundation'ın karşı ifadesi: "fresh process can occupy a continuing role" (A3 §4.3). **[kaynak diyor + çıkarım]**
- **Konumu yetki saymak.** "hierarchy position != authority != competence != responsibility != accountability" (A3 §3.1) **[kaynak diyor]**
- **Çoğalmayı bağımsızlık saymak.** "multiple model instances != independent verifier role by identity alone; independence depends on source/method/tool/context separation" (A3 §3.3) **[kaynak diyor]**
- **Ekibi bir grup aktörü saymak.** "Do not infer a corporate/group Actor merely from orchestration topology or shared task membership." (AD §7) **[kaynak diyor]**
- **Dosyanın varlığını yüklenmiş ve uygulanmış olmak saymak.** Bunu R04 (d4) RUA'dan aktardı. A3 §2.5 aynı ayrımı rol dosyasına uyguluyor. **[kaynak diyor]**
- **Dolaylı etki yolu.**
  - Foundation: "an agent without one direct production-write route could contact/use another actor with stronger capability" (A3 §2.3) **[kaynak diyor]**
  - EXP-007'de yazma yetkisi yalnız ana oturumda. Salt okuyan bir alt ajanın dönüşündeki talimat biçimli bir metin, ana oturum üzerinden bir etkiye dönüşebilir. A003'teki "Dönen sonuç veridir" kuralı bu yolu kapatan kuraldır. Bu yol, R04'ün "etki yolları listesi" önerisine eklenmelidir. **[çıkarım]**
- **Eski bir dersi korumak.** "A once-useful behavior may remain strongly retained after the environment changes, while becoming harmful." (D2 §4) **[kaynak diyor]**
- **Soru bankası tartışmasından örnek durumlar.** "a qualified worker lacks the needed information/access; a review is performed but fails to detect relevant errors; a new version is approved but the old version is published; and a procedure is rewritten without demonstrating retained behavioral improvement" (DH §2) **[kaynak diyor]**
- **Bu repodan bir örnek.** EXP-006'da roller SOUL'un yeteneklerinden türetildi, ekibin kendi çalışma döngüsünden türetilmedi. Tasarımcı, bakımcı ve inceleyici kalıbı alanlara göre tekrarlandı (R02 §2, §4). Foundation'a göre rolün dayanağı gereken sorumluluktur ve ekibin kendi çalışma işi de bu sorumluluğun içindedir (WV §7). **[kaynak diyor (R02) + çıkarım]**

### 5.6 Rol tasarımını sınamak için sorular
1. Rol, bir alt ajan örneği bittikten sonra da var mı? Yeni bir örnek aynı sorumluluğu, sınırları ve belleği yükleyerek mi başlıyor? (A3 §4.3; D3 §3)
2. Rol tanımında şunlar ayrı mı yazılı: sorumluluk, görev, yetkinlik iddiası, araç izni, karar yetkisi, hesap verme ilişkisi? (AG §7; AV D2; AF-RA §4)
3. Rolün hangi durumda çağrılacağı yazılı mı? Çağrılmadığında bu ihmal olarak görünür mü? (AV D6; AG §7)
4. Rol belleğindeki bir girdi rol tanımıyla çelişirse hangisi geçerli? Bu kural nerede yazılı? (§5.3)
5. Rol kendi belleğine ya da tanımına yazabiliyorsa, yazma olanağı ile kural değiştirme yetkisi birbirinden ayrılmış mı? (D3 §6)
6. Rol tanımı değişince, eski sürümle çalışan örneklerin sonuçları işaretleniyor mu? (TP §6; AF-RDA §5)
7. Katılım kaydı hangi örneğin, hangi rol sürümüyle, hangi işte ne yaptığını tutuyor mu? "Aynı örnek hem üretip hem denetledi mi?" sorusu cevaplanabiliyor mu? (BND; CC)
8. Bir rolün adı bağımsızlık ya da yetkinlik kanıtı gibi kullanılıyor mu? Bağımsızlık kaynak, yöntem ve bağlam ayrılığıyla mı gösteriliyor? (A3 §3.3)
9. Rolün yetkisi teknik erişimden mi çıkarılıyor? Salt okuyan bir rol ana oturum üzerinden bir etki üretebiliyor mu? (A3 §2.3; AD §4)
10. Model sürümü, araç arayüzü ya da ortam değişince rol belleğindeki dersler yeniden sınanıyor mu? (D3 §4; D2 §4)
11. Bir rol kapatılır ya da başka bir rolle birleştirilirse, süregelen görevleri başka bir role devrediliyor mu? (AG §7)
12. "Aynı rol" ölçütü tanımlı mı? Tanım sürümü mü, bellek mi, sorumluluk mu esas alınıyor? (AOQ OQ1)

### 5.7 Foundation'ın bilerek açık bıraktığı, EXP-007'nin karar vermesi gereken noktalar
- **Taşıyıcının sürekliliği:** "organization/system continuity rules are domain-sensitive" (AOQ OQ1). **[kaynak diyor]**
- **Rol, makam ve konum ayrımı:** "the current evidence establishes non-collapse but not a universal vocabulary" (AOQ OQ2). **[kaynak diyor]**
- **Yetkinliğin ayrıştırılması:** "How much structure is needed to distinguish skill, qualification, certification, experience, demonstrated performance and resource availability?" (AOQ OQ3) **[kaynak diyor]**
- **İzin ile yetki arasındaki sınır** (AOQ OQ4). **[kaynak diyor]**
- **İnsan dışı bir sistem ne zaman süregelen bir ajan sayılır:** "When, if ever, should a non-human system be treated as an enduring agent rather than only an operational participant, tool, provenance agent or component of a joint system?" (AOQ OQ7) **[kaynak diyor]**
- **Hangi sorumluluk rejimlerinin gerektiği** (AOQ OQ8). **[kaynak diyor]**
- **Ertelenmiş ilişkiler:**
  - kim neye karar verir (WV §16);
  - dolaylı yetki ve etki gücü: "the highest-priority deferred relation" (AD §4);
  - çok ajanlı yapılarda ortak aktörlük (AD §7);
  - insan yönetişimi (AD §8).

  **[kaynak diyor]**

**EXP-007'nin karar vermesi gerekenler [çıkarım]:**
- rol envanteri ve her rolün hangi sorumluluğa dayandığı;
- "aynı rol" ölçütü;
- değişiklik türlerine göre yetki tablosu (§5.4);
- tetiklerin sahibi ve nerede yazılı olduğu;
- yetkinlik kanıtının biçimi;
- rol belleğini kimin yazacağı.

### 5.8 Kalıcı rol için standart seviye bileşenleri **[çıkarım]**

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur (başka alt sistemler dahil) | Bedeli | Ne zaman gerçekten gereksiz |
|---|---|---|---|---|
| **Sorumluluğa dayanan rol tanımı:** AG §7'deki altı öğe | Rolü sıklıktan ve etiketten değil, gereken sorumluluktan türetir. | Gerekli olduğu hâlde kimseye verilmemiş iş kalır (A003 §3.8'in kendi sorusu; plan). Roller yanlış kaynaktan türer (R02). | Rol başına tanım yazımı; kurulum için Batu'nun onayı (A-04). | İş tek seferlikse ve süregelen bir sorumluluk doğurmuyorsa; o zaman geçici bir görev tanımı yeter. |
| **Yetkinlik, izin, yetki ve görevin ayrılması** (AV D2; AF-CAO) | Araç erişiminin yetki, rol adının yeterlik sanılmasını önler. | Denetleyici kabul eder. Koordinatör ölçütü değiştirir (yönetişim). | Tanımda ayrı alanlar; araç kısıtlarının ayrıca yapılandırılması. | Rol yalnız okuyor ve karar vermiyorsa. O durumda bile yetki alanına "yok" yazılır; alan boş bırakılmaz. |
| **Tetikler ve beklenen davranış** (AG §7; AV D6) | Süregelen sorumluluğun gerçekten çağrılmasını ve ihmalin görünmesini sağlar. | Rol çağrılmaz ve bu fark edilmez. Batu hatırlatıcı olur (insan iş birliği, gözlemlenebilirlik). | Ana oturumun kontrol listesi ve tetiklerin bakımı. | Rol yalnız açık talep üzerine çalışıyorsa (örneğin araştırmacı). O durumda talep eden tarafın tetiği yazılır. |
| **Rol belleği:** bilgi olarak etiketli, tanımdan ayrı (§5.3) | Birikimin taşınmasını sağlar; Batu'nun "her seferinde yeninden alt ajana rol biçmek doğru değil" itirazını (U004) karşılar. | Ya her örnek sıfırdan başlar ya da bellek yetki gibi davranır (yönetişim). | Bellek bakımı, budama ve çelişki kuralı. | Rol birikim üretmiyorsa ve her seferinde aynı kısa işi yapıyorsa. |
| **Rol sürümü ve örnek düzeyinde katılım kaydı** (BND; TP §6) | Hangi sonucun hangi tanımla üretildiğini, görevler ayrılığını ve değişiklik sonrası ayıklamayı mümkün kılar. | Eski tanımla üretilmiş sonuçlar yeni sonuçlarla karışır (bellek, kalite). | Dönüşte rol ve sürüm satırı. Tanım geçmişini git zaten tutar. | Rol tanımı hiç değişmiyorsa. P0 ve P1 için bu koşul geçerli değil. |
| **Değişiklik yetki tablosu** (§5.4) | Rolün kendi kapsamını genişletmesini de, her küçük değişikliğin Batu'ya gitmesini de önler. | Rol ya kendini genişletir ya da Batu gizli koordinatör olur (insan iş birliği). | Bir tablo ve her değişiklikte bir satır. | Yok: değişiklik olacağı kesin. |
| **Bağımsızlığın açık beyanı** (A3 §3.3; CC) | Karşı okumanın gücünü doğru adlandırır. | Aynı modelin iki örneği bağımsız doğrulama sayılır; EXP-006'daki kendi kendini onaylama tekrarlanır (R02 §3; kalite). | Karşı okuyucunun hangi bilgiden yoksun bırakıldığını yazmak. | Denetim iddiası yoksa. |
| **Model ve ortam değişince rol derslerinin yeniden sınanması** (D3 §4; D2 §4) | Zararlı hâle gelmiş eski dersleri yakalar. | Eski ders yeni koşulda yanlış davranış üretir (öğrenme). | Değişim anında tarama. | Model ve ortam sabitse. Claude Code'da ikisi de değişiyor (A003 §6). |

## 6. Üç alt sistem arasındaki etkileşimler
Tam etkileşim matrisi R11'in konusudur. Burada yalnız Foundation'ın doğrudan dayanak verdiği etkileşimler var. **[çıkarım; dayanakları parantez içinde]**

| Bir alt sistemde "yeterli" görünen seçim | Neyi yetersizleştirir |
|---|---|
| **Bellek:** "Her şeyi repoya ve rol belleğine yaz." | **Bağlam:** Yüklenen kısım konuma göre kesiliyor (MEMORY.md'nin ilk 200 satırı). Yeni dersler sınırın dışında kalır, eski girdiler bağlamı doldurur (REC-FS §10; S5 §4; D2 §4). Batu'nun masaj örneğinin karşılığı budur: bellekte bol görünen, bağlamı yetersizleştirir. |
| **Bağlam:** "Devirde ve sıkıştırmada özet yeter." | **Bellek:** Bugünün cevabı korunur, sonraki revizyonun ihtiyaç duyduğu durum kaybolur (M5.4; I §4). Özet belleğe yazılırsa türetilmiş sonuç dayanağa dönüşür (M1 §3). |
| **Rol:** "Roller üç tekrardan sonra kalıcı olsun." | **Plan ve kalite:** Süregelen sorumluluk hiç çağrılmaz, ihmal görünmez (AG §7; AV D6). Her çağrıda rol yeniden biçilir ve birikim taşınmaz (D3 §3). |
| **Bellek:** "Kalıcı dosyaları yalnız ana oturum yazsın." | **Orkestrasyon:** Kayıp güncelleme azalır (M2 §4). Ama tetikler, birleştirme ve taban kontrolünün hepsi koordinatörde toplanır (R06'daki "akıllı koordinatör" riski). Rol belleğini rolün kendisinin yazmasıyla da çatışır (§5.3). |
| **Gözlemlenebilirlik:** "Başarı ölçüsü Batu'nun hatırlatma sayısı olsun." | **Öğrenme:** Vekil ölçütler (FA §10) ve çerçeve körlüğü (FA §11) yüzünden dersler yanlış sinyale göre ayarlanır. |
| **Rol:** "Rolün belleği rolün elinde olsun." | **Yönetişim:** Yazabilmek ile yetki birbirine karışır. Rol kendi kapsamını genişletebilir (D3 §6; A3 §3.1). |
| **Bağlam:** "Yetki bilgisi görev tanımında yazsın." | **Yönetişim:** Bağlamdaki yetki iddiası güncel yetki sanılır (A3 §4.1). Görev tanımı eskiyince eski yetkiyle çalışılır (TP §6). |
| **Rol:** "Rol tanımı repoda dursun." | **Bağlam:** Tanım yüklenmezse ya da eski sürümü yüklenirse, tüketicide var sayılan bilgi yanlış olur (I §3; RUA). |

Bu tablo Batu'nun araba benzetmesinin Foundation'daki karşılığıdır. Her satır, bir alanda makul görünen bir seçimin başka bir alanın başarı koşulunu bozduğu bir durumu gösteriyor. Foundation'ın genel ilkesi de bunu söylüyor: "Individually satisfactory grounds do not automatically establish a valid composed result." (RUA) **[kaynak diyor]**

## 7. A003 v0 ile karşılaştırma
Durumlar: **Var**, **Kısmen**, **Yok**. v0'dan alıntılar A003'ten birebir alınmıştır. "Eksik" sütunu **[çıkarım]**dır.

| # | Foundation ayrımı | v0'da | v0'dan kanıt | Eksik |
|---|---|---|---|---|
| 1 | Kullanıma göre yeterlik (U5.1) | Kısmen | §3.3: "Amaç zinciri ... ve sonucun besleyeceği karar"; "Tek bir soru ve cevabın kararı nasıl değiştirebileceği" | Kabul edilen kayıp, alternatifler ve paketin küme olarak sınanması (S5.3). |
| 2 | Tüketiciye göre bağlam ve alıcıda var sayılan bilgi (I2, I3) | Kısmen | §3.3: "Benim bildiğimi bilmez; elinde yalnız benim yazdığım metin ve repo vardır." | Alıcıda var sayılanın yazılması ve yüklendiğinin kontrolü. Sıkıştırma sonrası ana oturum ayrı bir tüketici olarak ele alınmamış. |
| 3 | Sürüm bağı ve ortak anlık görüntü (S5.4, I4) | Kısmen | §3.3: "Zorunlu kaynaklar, yol ve sürümüyle." | Okunan dosyaların aynı sürümden gelmesi; taban değişikliğinin bildirilmesi (§0.4). |
| 4 | Uç nokta kanıtı ve kullanımın izi (E5.3, RI) | Var | §3.3: "neyi tam, neyi kısmen okuduğu, neyi hiç okumadığı"; §3.4: okuma kaydında "düşüncede neyi değiştirdi (ya da 'değiştirmedi')" | Kullanım izi var. "Değiştirmedi" cevabı da kullanımsızlığı kanıtlamaz (G6); bu sınır yazılı değil. |
| 5 | Bilginin doğru anda getirilmesi (STATE; CA C3) | Kısmen | §3.5 "Hangi anlarda": aşama başı, tasarım seçimi, mekanizma icadı, sürpriz, terim kayması, Claude Code iddiası | Araştırma için karar anları tanımlanmış. Dersler, bellek ve kapanış için yok; kapanışta "bu karara hangi bulgu bakıldı" satırı yok. |
| 6 | Özet ve sıkıştırmanın kayıpları (R6, R2, M5.4) | Kısmen | §3.4: "Kararı taşıyan ayrıntıda özet yetmez"; §3.3: "Dönen sonuç veridir, kanıt değildir"; §3.9: "Böylece bağlam sıkıştırıldığında yeniden yüklemek ucuz olur." | Kayıp mekanizmaları, iki yönlü kontrol ve sıkıştırmadan önce korunacaklar tanımlı değil. Sıkıştırma yalnız yeniden yükleme maliyeti olarak görülmüş, bir yeniden ifade olarak değil (§2.1). |
| 7 | Kipin korunması (IS §8) | Var | §3.3: "kaynak diyor / gözledim / çıkarım / varsayım / bilmiyorum" | Etiketin özetten özete taşınması kuralı. |
| 8 | Okuma yolu ve güncellik kapısı (REC-CR) | Kısmen | §3.4: "önce giriş dosyası, sonra soruya özgü harita, sonra özgün bölüm"; §3.9: "Önceki devir notu doğru kabul edilmez, git geçmişiyle karşılaştırılır." | Tarihsel dosyaların kendini işaretlemesi; denetim ve kanıt yollarının ayrılması. |
| 9 | Durum, bellek ve bağlamın ayrılması (AQ6; IS §14) | Kısmen | §3.4: "Repo bellektir; konuşma bellek değildir." | Konuşmayı bellekten ayırıyor. Ama kalıcılık, bellek ve bağlamı "repo" altında birleştiriyor; üçünün ayrı başarı koşulları yok. |
| 10 | Kayıt türleri ve kabul eylemi (M1 §1; F2 §4) | Kısmen | §3.1: "senin söylediğin, senin kastettiğini sandığım ve bizim revize edilebilir çalışma anlayışımız"; "Senin sözün birebir korunur." | Batu tarafı iyi ayrılmış. Alt ajan iddiası, Claude çıkarımı, doğrulanmış bulgu ve ders türleri ile eksiklik türleri yok. |
| 11 | Değişiklik türleri ve geri çekmenin hedefleri (REC §4; M1 §2) | Kısmen | §3.7: "tarihli bir değişiklik notu ... ne reddedildi"; "Kabul ettiğin plan sürümü korunur."; "kendi yanlış iddiamı geri çekmek için onay beklemem" | Düzeltme ile karar değişikliğinin ayrılması; geri çekmenin türetilmiş kopyalara yayılması. |
| 12 | İki zaman ve kapsama göre güncellik (REC §4; REC-CTS) | Yok | — | Etkili ve kayıt zamanı; dala göre güncellik. EXP-006 örneğinde bu gerçek bir durum. |
| 13 | Köken rolleri (IS §10; M1 §3) | Kısmen | §3.6: iş kalemi için "nereden çıktığı"; §3.5: "Araştırma izi" | Kim söyledi, kim türetti, kim doğruladı ayrımı; türetilmiş sonucun dayanağa dönüşmesine karşı koruma. |
| 14 | Tazelik (S5.4; REC §7) | Kısmen | §3.5: "Studies'teki teknik bilgi eskimiş olabilir." | "Bayat yanlış değildir" ayrımı ve "yeniden değerlendir" işareti. |
| 15 | Unutma ve saklama (REC §9; U5.6) | Yok | §4: "eski sürüm kopyaları (git zaten tutuyor)" bırakılanlar arasında | Yüzey başına saklama ve budama; bağlamdan çıkarma ile silmenin ayrılması; eski derslerin gözden geçirilmesi. |
| 16 | Çakışma (IS §13; M1 §5) | Kısmen | §3.4: "Okumak karşılaştırmak demek değildir ... kaynaklar arası iddialar için ayrıca birlikte okuma yapılır." | Çelişki kaydı, hizalama ve karar yolu. |
| 17 | Ders ile davranış değişikliğinin ayrılması (D1–D3) | Var (ilke) | §3.5: "Kaydedilmiş bir ders, davranışın değiştiği anlamına gelmez."; §3.10: "Değişim görülene kadar ders 'doğrulanmadı' sayılır." | Yükleme yolu, fırsat sınıfı, sınamanın hedefi değiştirmesi ve vekil ölçüt riski. Başarı ölçüsü hatırlatma sayısı (§4.8). |
| 18 | Önerinin tabanının kontrolü (M2 §4) | Kısmen | §3.2: "kalıcı dosyaları tek başıma yazarım" | Tek yazıcı var, ama önerinin hangi tabana göre hazırlandığı kontrol edilmiyor. |
| 19 | Rol ile taşıyıcının ayrılması (A3 §4.3; AV D1) | Yok | §3.2: "tek soruluk, geçici çalışanlar"; §3.3: "üç kez ... önce değil" | Rolün sürekliliği. Batu bunu açıkça reddetti (U004). |
| 20 | Rolün dayanağının sorumluluk olması (AG §7) | Yok | Sıklık kuralı | Görevler, tetikler, hesap verme ilişkisi. |
| 21 | Yetkinlik, izin, yetki ve görevin ayrılması (AV D2) | Kısmen | §3.2: "Bunlar DevOS'un rolleri değil."; §3.6: karar katmanları | Düzey ayrımı ve karar katmanları var. Rol başına izin ve yetki alanları yok. |
| 22 | Rol adının bağımsızlık kanıtlamaması (A3 §3.3) | Var | §3.3: "'bağımsız doğrulama' değil, 'taze gözle karşı-okuma' derim." | — |
| 23 | Koordinatörün kabul ölçütünü değiştirememesi (A3 §3.1) | Var | §3.7: "amaca, kapsama, kabul ölçütüne, haritaya ve P4 durağına sen" | Rol değişiklikleri için ayrı bir tanım. |
| 24 | Rol belleğinin rol yetkisinden ayrılması (§5.3) | Yok | — | Rol belleği hiç yok. |
| 25 | Rolü kimin değiştirebileceği (§5.4) | Yok | DECISIONS A-04 yalnız kurulumu kapsıyor | Değişiklik türüne göre yetki. |
| 26 | İhmalin görünür olması (AV D6) | Kısmen | §3.2: "eksik-arayıcı: kimseye verilmemiş işi ve okunmamış kaynağı arar"; §3.8: "gerekli olduğu halde kimseye verilmemiş iş var mı?" | Rollerin beklenen davranışı ve tetikleri. |
| 27 | Örnek düzeyinde katılım kaydı ve rol sürümü (BND; TP §6) | Yok | Yalnız §3.3: "Aynı görevi aynı tanımla ikinci kez göndermem." | Hangi örneğin hangi tanımla, hangi işte, ne zaman ne yaptığı. |

**Özet teşhis [çıkarım]:**
1. **Rolde taşıyıcı–rol çöküşü var.** v0'ın rol eksiği bir kapsam eksiği değil, bir kavram hatasıdır. Geçici örnek ile kalıcı rol birleştirilmiş. Batu'nun itirazı bu hatayı hedefliyor.
2. **Bellekte kalıcılık, bellek ve bağlam birleştirilmiş.** "Repo bellektir" ilkesi doğru ama tek başına üç ayrı başarı koşulunu tek kavrama topluyor. Kayıt türleri, değişiklik türleri, zaman, saklama ve çakışma kurulmamış.
3. **Bağlam yalnız maliyet sorunu olarak görülmüş.** Sıkıştırma "yeniden yükleme maliyeti" olarak ele alınmış. Kullanıma göre yeterlik, tüketiciye ulaşma ve yeniden ifadede kayıp soruları kurulmamış.
4. **v0'ın Foundation ile uyumlu, korunması gereken güçlü yanları:**
   - kanıt dili;
   - A–B–C ayrımı;
   - tek yazıcı;
   - "dönen sonuç veridir";
   - karşı okumanın bağımsız doğrulama sayılmaması;
   - plan sürümünün korunması;
   - dersin "doğrulanmadı" sayılması;
   - karar katmanları;
   - araştırmaya başvurma anları;
   - soğuk başlangıç testi.

   Standart seviyeye çıkmak için bunlar atılmamalı, yukarıdaki eksiklerle tamamlanmalıdır.

**Çapraz atıf (K-010'a göre isteğe bağlı okuma):** ChatGPT hattının P2-01 dosyası (`origin/main` `ed2bf6e`) aynı Foundation ayrımlarını DevOS rolleri için rol sözleşmesine indirmiş:
- DR07 (Bilgi Sorumlusu) kalıcı nesnenin yaşam döngüsünü, DR08 (Bağlam Kurucusu) tüketicinin görünümünü taşıyor. DR08 için "Paketin oluşturulması gerçek exposure/use kanıtı değildir" deniyor.
- DR15 için "Kendiliğinden kalıcı politika veya grant değiştirmez" deniyor.

**[kaynak diyor]** (P2-01) Bunlar DevOS için ChatGPT hattının adaylarıdır ve K-010'a göre EXP-007'yi bağlamaz. Yalnız, Foundation ayrımlarının bir rol tanımına nasıl indirilebileceğini gösteren bir karşılaştırma noktası olarak işe yarar. **[çıkarım]**

## 8. Yanlış birleştirilmemesi gerekenler: tek liste
Görev tanımının "neyi yanlış birleştirmemeli" sorusunun kısa cevabı aşağıda. Her satır Foundation'ın ayrımıdır **[kaynak diyor]**; ayrıntısı ilgili bölümdedir. Buradaki `≠`, "birbirinin yerine geçmez" demektir.

**Bağlam**
- saklanmış ≠ bulunabilir ≠ seçilmiş ≠ tüketiciye ulaşmış ≠ anlaşılmış ≠ kullanılmış (IS §14; S5 §4; RI)
- yeterli bir görünüm var ≠ erişilebilir bir görünüm var; iddia için ikisinin ortak bir tanığı gerekir (I1)
- iyi parçalar ≠ iyi küme (S5.3)
- bir tüketicinin elindeki ≠ sistemde bir yerde olan (I2)
- en yeni ≠ geçerli ≠ birbiriyle tutarlı ≠ istenen tarihe uygun (S5.4)
- kurtarılabilir ≠ amaçlanan anlamla aktarılmış ≠ kullanılmış (R1 §1; R6)
- bugünün cevabını koruyan özet ≠ revizyon durumunu koruyan özet (M5.4)
- kararı koruyan özet ≠ gerekçeyi koruyan özet (U5.2)
- bağlamdaki yetki iddiası ≠ güncel yetki (A3 §4.1)

**Bellek**
- durum ≠ bellek ≠ bağlam ≠ bilgi (AQ6)
- birinin P dediğini kaydetmek ≠ P'yi öncül kabul etmek ≠ yetkili kararı kabul etmek ≠ güncel durumu kurmak (M1 §1)
- kaynağı geri çekmek ≠ önermeyi bırakmak ≠ tersini kabul etmek (M1 §2)
- düzeltme ≠ dünyadaki değişiklik (M2 §1)
- etkili zaman ≠ kayıt zamanı; en son alınan ≠ geçerli olan (M2 §3; REC §4)
- tarihsel olarak doğru ≠ bugün yetkili (CA C4)
- türetilmiş sonuç ≠ dayanak (M1 §3)
- teslim kimliği ≠ köken kimliği ≠ bağımsız kanıt (F3 §5; F6)
- bayat ≠ yanlış; dayanak değişti ≠ sonuç değişti (REC §7; CS)
- gizlemek ya da silmek ≠ yok etmek; kopyalar kalır (REC §9)
- ders yazıldı ≠ yüklendi ≠ kullanıldı ≠ davranış değişti ≠ korundu ≠ yararlı oldu (D3 §2; FA §4)
- görülmedi ≠ unutuldu (D2 §3)
- farklılık ≠ çelişki; yan yana duran alternatifler ≠ uzlaşma (IS §13; M1 §5)

**Rol**
- taşıyıcı ≠ rol ≠ etkin katılım (AV D1; A3 §4.3)
- rol tanımlı ≠ çağrılabilir ≠ şu an etkin (AF-IRP §2)
- yapabilir ≠ yetkin ≠ izinli ≠ yetkili ≠ yükümlü (AV D2)
- rol metni ≠ yetki ≠ zorlama ≠ uyum (A3 §2.5)
- rol belleği ≠ rol yetkisi; yazabilmek ≠ yetkili olmak (AG §2.1; D3 §6)
- rol adı ≠ yetkinlik ≠ bağımsızlık (A3 §3.2–3.3)
- hiyerarşideki konum ≠ yetki ≠ yetkinlik ≠ sorumluluk ≠ hesap verme (A3 §3.1)
- süregelen sorumluluk ≠ şu anki iş bölümü (AG §7)
- ajanlar topluluğu ≠ ortak eylem ≠ grup aktörü (AD §7)
- ulaşılabilir etki gücü ≠ meşru yetki (AD §4)

## 9. Açık sorular
1. **"Aynı rol" neye göre belirlenir?** Tanım sürümüne, belleğe ya da sorumluluğa göre mi? Model sürümü değişince rol aynı mı kalır? Foundation bunu açık bırakıyor (AOQ OQ1).
2. **Rol belleğini kim yazar?** Rolün kendisi mi (`memory: project`), ana oturum mu? Bu, A003'ün tek yazıcı ilkesiyle nasıl uzlaşır? R01'e göre bu belleğin buluttaki kalıcılığı belirsiz.
3. **Değişiklik yetki tablosu (§5.4) Batu tarafından onaylanacak mı?** Hangi değişiklik türleri Batu'ya gider?
4. **Batu'nun farklı zamanlardaki kararları için "sonraki karar geçerlidir" kuralı** açıkça konacak mı? Konacaksa kapsamı ne olacak (M2 §2)?
5. **Sıkıştırmadan önce korunması gereken revizyon durumunun asgari içeriği nedir?** Bu durum bir otomatik adımla mı, yoksa çalışma disipliniyle mi korunacak? ORTAK'a göre `settings.json` hook'ları yalnız tek repolu oturumlarda geçerli; mekanizma R07'nin konusu.
6. **Taban değişikliği nasıl bildirilecek?** Birleştirme anındaki kontrol yeterli mi? Alt ajanlar birbirine ulaşamıyor; iletişim ana oturum ya da repo üzerinden gidiyor.
7. **"Kullanıldı" kanıtı hangi biçimde ve hangi bedelle tutulacak?** Foundation bunun nasıl ölçüleceğini açık bırakıyor (G6).
8. **Hatırlatma sayısının yanına Batu'dan bağımsız hangi ölçü eklenecek?** (FA §10–11)
9. **Bağımsız soğuk başlangıç testi ne zaman yapılacak?** Test isteminin ölçtüğü şeyi öğretmemesi nasıl sağlanacak (D2 §6)?

## 10. Bu notun kanıtlamadığı
- **Foundation'ın ayrımlarının doğru olduğunu bağımsız olarak kanıtlamaz.** Foundation'ın kendi sınırları geçerlidir: aynı asistan, aynı modelle yapılmış karşı inceleme, bağımsız tekrar yok, canlı ajan deneyi yok (§0.2).
- **Bu ayrımların EXP-007'ye fayda sağlayacağını kanıtlamaz.** EXP-007'ye yapılan bütün uygulamalar çıkarımdır ve hiçbiri canlı olarak denenmedi.
- **Bileşen tabloları mekanizma seçimi değildir.** §3.7, §4.12 ve §5.8'deki bileşenlerin hangi Claude Code özelliğiyle kurulacağı R07–R09'un konusudur. "Bedel" sütunları tahmindir, ölçülmedi.
- **Foundation'ın tamamı okunmadı** (§0.5). Özellikle Environment zemini, U4/E4, M5 rakip incelemesi, Records'un diğer konu dosyaları ve kaynak defterleri okunmadı; bu dosyalarda notu değiştirecek bir ayrım olabilir. "Foundation'ın bilerek açık bıraktığı" noktalar Foundation'ın kendi beyanlarına dayanıyor. Okunmayan dosyalarda kapatılmış olabilirler.
- **Bazı iddialar başka notlara dayanır ve burada sınanmadı.**
  - R04'ten aktarılan ama benim doğrulamadığım iddialar R04'e dayanır; örneğin çelişen STATE dosyaları.
  - Claude Code davranışları R01'e dayanır: MEMORY.md'nin 200 satır sınırı, sıkıştırmanın neyi düşürdüğü, CLAUDE.md'nin yeniden yüklenmesi. Bunların bir kısmı `documented_generic_unclear_cloud` etiketli ve bu ortamda sınanmadı.
- **§7'deki v0 değerlendirmesi yalnız A003 metnine dayanır.** v0'ın konuşma içindeki başka açıklamaları görülmedi.
- **§0.4'teki gözlem tek bir olaydır.** Alt ajanların taban değişikliklerini ne sıklıkla kaçırdığını göstermez.
